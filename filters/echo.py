"""
Print Pandoc reader options as definition lists
"""

import os
import json
from collections import OrderedDict

import panflute as pf


def action(elem, doc):
    pass


def finalize(doc):
    reader_options = pf.load_reader_options()
    definitions = []
    for k, v in reader_options.items():
        term = [pf.Str(k)]
        definition = pf.Definition(pf.Para(pf.Str(repr(v))))
        definitions.append(pf.DefinitionItem(term, [definition]))
    doc.content.append(pf.DefinitionList(*definitions))


def main(doc=None):
    return pf.run_filter(action, finalize=finalize, doc=doc) 


if __name__ == '__main__':
    main()
