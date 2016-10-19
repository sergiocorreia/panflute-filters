#!/usr/bin/env python

import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Header):
        pagebreak = pf.RawBlock('\pagebreak{}', format='latex')
        return [pagebreak, elem]


def main():
    # pf.run_filter(action)
    pf.toJSONFilter(action=action)


if __name__ == "__main__":
    main()
