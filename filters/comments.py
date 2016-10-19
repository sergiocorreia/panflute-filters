#!/usr/bin/env python

import panflute as pf

def action(e, doc):
    if isinstance(e, pf.RawBlock) and (doc.format == 'latex'):
        if e.text.startswith('<!--') and e.text.endswith('-->'):
            e.format = 'latex'
            e.text = '% ' + e.text


def main():
    pf.toJSONFilter(action=action)


if __name__ == "__main__":
    main()
