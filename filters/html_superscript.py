"""
Render superscript with html <sup> tags:
    >> echo 2^10^ is 1024 | pandoc --to=markdown -F html_superscript.py
    2<sup>10</sup> is 1024
"""

import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.Superscript) and doc.format == 'markdown':
        text = '<sup>' + pf.stringify(elem) + '</sup>'
        return pf.RawInline(text)


if __name__ == '__main__':
    pf.run_filter(action)
