"""
Test a filter directly from python instead of through markdown

Note: this is an experimental program
"""

# Test a filter in ./filters
# Use markdown text from ./tests
# Avoid pandoc with its ineffective error messages

# https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/


import os
import io
import sys
import importlib
import panflute as pf

def run_test(name, action):
    input_fn = os.path.join('tests', name + '.md')
    
    # Read markdown, convert to JSON and then to elements
    with open(input_fn, encoding='utf-8') as f:
        md = f.read()
        print('~' * 80)
        print(' ' * 30, 'INPUT')
        print('~' * 80)
        print(md)
        print('~' * 80, '\n')
        print('... Parsing markdown')
        doc = pf.convert_text(md, output_format='doc')
        doc.format = 'markdown'
        assert type(doc) == pf.Doc
        print('    Done.')

    # Walk through AST
    sys.path.append('filters')
    print('... Importing module')
    mod = importlib.import_module(name)
    print('    Done.')
    f_action = mod.__dict__[action]

    print('... Applying filters')
    altered = doc.walk(f_action, doc)
    print('    Done.')

    # Convert AST into JSON
    print('... Converting document into JSON')
    with io.StringIO() as f:
        pf.dump(altered, f)
        contents = f.getvalue()
    print('    Done.')

    # Convert JSON into markdown
    print('... Converting JSON into markdown')
    md = pf.convert_text(contents, input_format='json', output_format='markdown')
    print('    Done.')

    print('~' * 80)
    print(' ' * 30, 'OUTPUT')
    print('~' * 80)
    print(md)
    print('~' * 80, '\n')

    # Create markdown


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Invalid syntax')
        raise Exception
    name = sys.argv[1]
    action = sys.argv[2]
    # TODO: add support for prepare ..  output format, etc.
    run_test(name, action)
    print('Done!')