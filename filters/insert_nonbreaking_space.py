"""
Pandoc filter to exchange regular spaces for non-breaking spaces between numbers (400 000) or between number and unit (4 Wh)
"""

from panflute import run_filter, Str, Space
import itertools
import re

nonbreakingspace = " "


def make_unit_list():
    unitlist = ["t", "%", "%-wt", "%-vol", "°C"]
    prefixes = ["m", "c", "", "k", "M", "G", "T"]
    units = ["J", "g", "m", "W", "Wh", "s", "K", "A", "mol"]
    unitlist += ["".join(t) for t in itertools.product(prefixes, units)]
    return unitlist


# check if Str element represents a number
def is_numeric_string(elem, doc):
    if type(elem) == Str:
        return doc.punctuation.sub("",elem.text).isnumeric()
    return False

def is_unit_string(elem, doc):
    if type(elem) == Str:
        return any([x in doc.unitlist for x in doc.punctuation.sub(" ",elem.text).split(" ")])
    return False

# check string and next neighbors for combination: number space number
def is_number_space_number(elem, doc):
    if elem.next:
        if elem.next.next:
            return is_numeric_string(elem, doc) \
                   & (type(elem.next) == Space) \
                   & is_numeric_string(elem.next.next, doc)
    return False

# check string and next neighbors for combination: number space unit
def is_number_space_unit(elem, doc):
    if elem.next:
        if elem.next.next:
            return is_numeric_string(elem, doc) \
                   & (type(elem.next) == Space) \
                   & is_unit_string(elem.next.next, doc)
    return False

# make nonbreaking space if:
# - number space number
# - number space unit
def make_nonbreaking_space(elem, doc):
    if is_number_space_number(elem, doc) or is_number_space_unit(elem, doc):
        # replace space by Str element with non-breaking space as content
        elem.container.list[elem.index+1] = Str(nonbreakingspace)



def prepare(doc):
    # generate list of units
    doc.unitlist = make_unit_list()
    # generate re for punctuation detection
    doc.punctuation = re.compile("\/|\)|\(|\.|\;|\-|\,|\+")


# check document all for spaces to replace
def action(elem, doc):
    if type(elem) == Str:
        make_nonbreaking_space(elem, doc)
        return elem


def main(doc=None):
    return run_filter(action, doc=doc, prepare=prepare)


if __name__ == "__main__":
    main()

