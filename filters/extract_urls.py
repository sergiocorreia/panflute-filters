import io

import pypandoc
import panflute


def prepare(doc):
	doc.images = []
	doc.links = []


def action(elem, doc):
    if isinstance(elem, panflute.Image):
    	doc.images.append(elem)
    elif isinstance(elem, panflute.Link):
    	doc.links.append(elem)


if __name__ == '__main__':
	data = pypandoc.convert_file('example.md', 'json')
	f = io.StringIO(data)
	doc = panflute.load(f)
	doc = panflute.run_filter(action, prepare=prepare, doc=doc)
	
	print("\nImages:")
	for image in doc.images:
		print(image.url)

	print("\nLinks:")
	for link in doc.links:
		print(link.url)
