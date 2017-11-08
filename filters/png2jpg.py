"""
Change image extensions from .png to .jpg

EXAMPLE:
    >>>> echo An ![image](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png) | pandoc -F png2jpg.py
"""

import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.Image):
        elem.url = elem.url.replace('.png', '.jpg')
        return elem

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()
