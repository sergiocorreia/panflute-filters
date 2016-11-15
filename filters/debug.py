"""
Pretty print contents of the filters' input (both sys.argv and the JSON)

Usage:
    pandoc foobar.md -F ./debug.py -o foobar.html --toc
"""

import sys
import json
import pprint
import pkg_resources

import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.Doc):
        version = pkg_resources.get_distribution("panflute").version
        json_serializer = lambda elem: elem.to_json()
        raw = json.dumps(elem, default=json_serializer)
        raw = json.loads(raw)
        raw = json.dumps(raw, check_circular=False,
                         indent=4, separators=(',', ': '))
        disclaimer = pf.Para(pf.Emph(pf.Str('Note: sort order not preserved')))
        elem.content = [
          pf.Header(pf.Str('Python version:'), level=2),
          pf.Para(pf.Str(sys.version)),
          pf.Header(pf.Str('Panflute version:'), level=2),
          pf.Para(pf.Str(version)),
          pf.Header(pf.Str('sys.argv:'), level=2),
          pf.Plain(pf.Str(str(sys.argv))),
          pf.Header(pf.Str('JSON Input:'), level=2),
          disclaimer,
          pf.CodeBlock(raw)
        ]


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
