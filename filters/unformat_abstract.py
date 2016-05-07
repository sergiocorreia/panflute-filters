"""
Remove formatting from abstract
"""

from panflute import *

format_element = (Emph, Strong, Strikeout, Subscript, Superscript, SmallCaps)

def remove_format(e, doc):
    if isinstance(e, format_element):
        return Span(*e.content)

def remove_all(e, doc):
    # This filters removes formatting from all of metadata
    # Not used; kept here as a comparison
    if isinstance(e, MetaValue):
        return e.walk(remove_format, doc)

def remove_abstract(e, doc) :
    if isinstance(e, MetaMap) and 'abstract' in e.content:
        # Note that even if we don't <return e>, it has already been modified
        e.content['abstract'].walk(remove_format, doc)

if __name__ == '__main__':
    toJSONFilter(remove_abstract)
