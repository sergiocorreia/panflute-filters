#!/usr/bin/env python

from string import Template
import panflute as pf

# Constants

TEX_BEFORE = """\parbox[t]{0.4\linewidth}{"""

TEX_AFTER = Template(r"""}\hfill\
includegraphics[width=0.4\linewidth]{$image}
""")


def action(e, doc):
    if isinstance(e, pf.Image) and (doc.format == 'latex') and ('parbox' in e.classes):
        subs = {'image':e.url}
        before = pf.RawInline(TEX_BEFORE, format='latex')
        after = pf.RawInline(TEX_AFTER.safe_substitute(subs), format='latex')
        span = pf.Span(before, *e.content, after, classes=e.classes, identifier=e.identifier, attributes=e.attributes)
        return(span)


def main():
    pf.toJSONFilter(action=action)


if __name__ == "__main__":
    main()
