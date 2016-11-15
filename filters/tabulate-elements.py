"""
Count frequency of each element

Sample usage:

	> pandoc example.md  -F tabulate-elements.py --to=markdown
     Element       Freqency
     ------------- ----------
     MetaBool      2
     SoftBreak     1
     Str           46
     MetaInlines   18
     RawInline     7
     Doc           1
     MetaBlocks    1
     Emph          1
     MetaMap       2
     Space         24
     Para          2
     MetaList      2
"""

from collections import Counter
import panflute as pf

def prepare(doc):
	doc.counter = Counter()


def action(elem, doc):
	doc.counter[elem.tag] += 1


def finalize(doc):
	c1 = pf.TableCell(pf.Plain(pf.Str("Element")))
	c2 = pf.TableCell(pf.Plain(pf.Str("Frequency")))
	header = pf.TableRow(c1, c2)
	rows = []
	for tag in doc.counter:
		c1 = pf.TableCell(pf.Plain(pf.Str(tag)))
		c2 = pf.TableCell(pf.Plain(pf.Str(str(doc.counter[tag]))))
		rows.append(pf.TableRow(c1, c2))
	table = pf.Table(*rows, header=header)
	doc.content = [table] # bugbug?


def main(doc=None):
     return pf.run_filter(action, prepare, finalize, doc=doc)


if __name__ == '__main__':
    main()
