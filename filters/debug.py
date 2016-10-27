"""
Pretty print contents of the filters' input (both sys.argv and the JSON)
"""

import json
import pprint
import sys
import panflute as pf

def action(elem, doc):
	if isinstance(elem, pf.Doc):
          json_serializer = lambda elem: elem.to_json()
          raw = json.dumps(elem, default=json_serializer)
          raw = json.loads(raw)
          raw = json.dumps(raw, check_circular=False,
                           indent=4, separators=(',', ': '))
          pf.debug(dir(elem))
          disclaimer = pf.Para(pf.Emph(pf.Str('Note: sort order not preserved')))
          elem.content = [pf.Header(pf.Str('sys.argv:'), level=2),
                          pf.Plain(pf.Str(str(sys.argv))),
                          pf.Header(pf.Str('JSON Input:'), level=2),
                          disclaimer,
                          pf.CodeBlock(raw)]


def main():
    pf.toJSONFilter(action)
     

if __name__ == '__main__':
     main()
