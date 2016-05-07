"""
Fenced code block; replace blocks of class 'foo' with # horizontal rules
"""

import panflute as pf

def fenced_action(options, data, element, doc):
	count = options.get('count', 1)
	div = pf.Div(attributes={'count': str(count)})
	div.content.extend([pf.HorizontalRule] * count)
	return div

if __name__ == '__main__':
    pf.toJSONFilter(pf.yaml_filter, tag='foo', function=fenced_action)
