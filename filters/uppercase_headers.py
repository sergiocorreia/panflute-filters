"""
Convert the text in all headers to uppercase
"""

import panflute as pf

def upper_str(elem, doc):
    if isinstance(elem, pf.Str):
        elem.text = elem.text.upper()

def upper_header(elem, doc):
    if isinstance(elem, pf.Header):
        return elem.walk(upper_str)

if __name__ == '__main__':
    pf.toJSONFilter(upper_header)
