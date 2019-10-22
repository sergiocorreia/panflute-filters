import panflute as pf

def prepare(doc):
    doc
    pass

def collapse(elem, doc):
    if isinstance(elem, pf.CodeBlock) and "html" in doc.format:
        content = [
            pf.RawBlock("<details>", format="html"),
            pf.RawBlock(
                """
                <summary onclick="this.innerHTML == ' Show code ' ? this.innerHTML = ' Hide code ': this.innerHTML = ' Show code '"> Show code </summary>
                """
            ),
            elem,
            pf.RawBlock("</details>", format="html"),
        ]
        div = pf.Div(*content, classes=["collapsible_code"])
        return div

def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(collapse,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc)

if __name__ == '__main__':
    main()
