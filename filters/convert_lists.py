"""
Convert all ordered lists into bullet lists
"""

import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.OrderedList):
        return pf.BulletList(*elem.content)


def main(doc=None):
    return pf.run_filter(action, doc=doc) 


if __name__ == '__main__':
    main()
