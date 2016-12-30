"""
Convert strong text to normal text

EXAMPLE:
    >>>> echo Lorem **ip sum** example | pandoc -F remove-strong.py
    <p>Lorem ip sum example</p>
"""

import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.Strong):
        return list(elem.content)
        #return elem.content.list
        #return pf.Span(*elem.content)

def main(doc=None):
	return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()
