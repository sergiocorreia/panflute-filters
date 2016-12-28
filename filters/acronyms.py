"""
Panflute filter that allows for acronyms in latex

Usage:

- In markdown, use it as links: [SO](acro "Stack Overflow")
- When outputting to latex, you must add this line to the preamble:
\\usepackage[acronym,smallcaps]{glossaries}
- Then, this filter will add "\newacronym{LRU}{LRU}{Least Recently Used} for the definition of LRU and finally \gls{LRU} to every time the term is used in the text."

(see https://groups.google.com/forum/#!topic/pandoc-discuss/Bz1cG55BKjM)
"""

from string import Template  # using .format() is hard because of {} in tex
import panflute as pf

TEMPLATE_GLS = Template(r"\gls{$acronym}")
TEMPLATE_NEWACRONYM = Template(r"\newacronym{$acronym}{$acronym}{$definition}")


def prepare(doc):
    doc.acronyms = {}


def action(e, doc):
    if isinstance(e, pf.Link) and e.url == 'acro' and doc.format == 'latex':
        acronym = pf.stringify(e)
        definition = e.title
        # Only update dictionary if definition is not empty
        if definition:
            doc.acronyms[acronym] = definition
        tex = '\gls{{}}'.format(acronym)
        tex = TEMPLATE_GLS.safe_substitute(acronym=acronym)
        return pf.RawInline(tex, format='latex')
        # return None -> element unchanged
        # return [] -> delete element


def finalize(doc):
    tex = [r'\usepackage[acronym,smallcaps]{glossaries}', '\makeglossaries']
    for acronym, definition in doc.acronyms.items():
        tex_acronym = TEMPLATE_NEWACRONYM.safe_substitute(acronym=acronym, definition=definition)
        tex.append(tex_acronym)
    tex = '\n'.join(tex)

    with open('acronyms_header.tex', 'w', encoding='utf-8') as fh:
        fh.write(tex)


def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc) 


if __name__ == '__main__':
    main()
