
"""
Pandoc filter to wrap all math-mode subscripts and superscripts in \textrm{}
if they are wrapped in curly braces {} AND if they do start with a backslash \
The script also removes any nested sub- and superscripts.
e.g.:
a_{text-subscript} -> a_{\textrm{text-subscript}}
a^{text-superscript} -> a^{\textrm{text-superscript}}
a^{CO_2}} -> a^{\textrm{CO2}}
BUT
a^{\frac{1}{2}} -> a^{\frac{1}{2}}
"""

from panflute import run_filter, Math
import re

def omit_nested_super_subscript(m):
    return m.group(1).replace('_','').replace('^','')

def action(elem, doc):
    if type(elem) == Math:
        # wrap subscript in textrm and remove nested sub/superscripts
        text = re.sub(r'_{([^\\}]+)}', lambda x:r'_{\textrm{'+omit_nested_super_subscript(x)+'}}', elem.text)
        # wrap superscript in textrm and remove nested sub/superscripts
        text = re.sub(r'\^{([^\\}]+)}', lambda x:r'^{\textrm{'+omit_nested_super_subscript(x)+'}}', text)
        elem.text = text
        return elem


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
