"""Create table of contents from multiple files

Usage:

    pandoc --number-sections --file-scope --toc -s *.md | pandoc -s -f html -o toc.html -F fixtoc.py -M files:"*.md"
"""

import glob
import panflute as pf


def prepare(doc):
    # Create file list
    fns = doc.get_metadata('files')
    pf.debug('-' * 64)
    pf.debug('Expanding pattern:', fns)
    fns = glob.glob(fns)
    pf.debug('Files:', fns)
    fns = [fn.replace('.md', '.html') for fn in fns]    
    doc.fns = fns
    pf.debug('-' * 64)

    # Clear all contents except TOC
    doc.content.list = doc.content.list[:1]


def action(e, doc):
    if isinstance(e, pf.Div) and e.identifier=='TOC':
        e.walk(fix_links)


def fix_links(e, doc):
    if isinstance(e, pf.Link):
        e.url = doc.fns[0] + e.url
    elif isinstance(e, pf.ListItem) and isinstance(e.parent.parent, pf.Div):
        doc.fns.pop(0)  # Switch to the next filename


if __name__ == '__main__':
    pf.run_filter(action, prepare=prepare) 
