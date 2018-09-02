"""
A Pandoc filter to create tables from nested divs (in a similar manner to html).

This is useful for creating more complex tables with cells containing other markdown block elements

author: chris sewell
contact: https://github.com/chrisjsewell

Example
-------

::::: {.divtable}

:::: {.tcaption}
a caption here (optional), only the first paragraph is used.
::::

:::: {.thead}
[Header 1]{width=0.4 align=center}
[Header 2]{width=0.6 align=default}
::::

:::: {.trow}
::: {.tcell}

1. any
2. normal markdown
3. can go in a cell

:::
::: {.tcell}
![myimage](path/to/image.png)

some text
:::
::::
:::: {.trow bypara=true}
If bypara=true

Then each paragraph will be treated as a separate column
::::

any text outside a div will be ignored

:::::

Notes
-----

- thead and tcation are optional. 
- Within thead each column is designated by a span
    - there must be as many spans as columns
    - the width attribute is optional and refers to a relative column width
    - the align attribute is optional and can be either: left, right, center or default
    - if all headers are empty (e.g. []{align=center}), then no header row will be created
- 

"""
import panflute as pf


def action(element, doc):
    """
    return None -> element unchanged
    return [] -> delete element
    """
    if not isinstance(element, pf.Div):
        return None
    if not "divtable" in element.classes:
        return None

    rows = []
    headers = []
    header_found = False
    widths = []
    aligns = []
    caption = None
    for tbl_el in element.content:
        
        if isinstance(tbl_el, pf.Div) and "thead" in tbl_el.classes:
            headers = []
            assert isinstance(tbl_el.content[0], pf.Para), "the table header div must contain a paragraph"
            for head_el in tbl_el.content[0].content:

                if isinstance(head_el, pf.Span):
                    if list(head_el.content):
                        header_found = True              
                    headers.append(pf.TableCell(pf.Plain(*head_el.content))) 
                    if "width" in head_el.attributes:
                        widths.append(float(head_el.attributes["width"]))
                    else:
                        widths.append(0)
                    if "align" in head_el.attributes:
                        align = str(head_el.attributes["align"]).capitalize()
                        assert align in ["Left", "Right", "Center", "Default"], "table alignment must be one of left, right, center or default"
                        aligns.append("Align"+align)   
                    else:
                        aligns.append("AlignDefault")  
        
        elif isinstance(tbl_el, pf.Div) and "tcaption" in tbl_el.classes:
            assert isinstance(tbl_el.content[0], pf.Para), "the table caption div must contain a paragraph"
            caption = list(tbl_el.content[0].content)
                                 
        elif isinstance(tbl_el, pf.Div) and "trow" in tbl_el.classes:
            row = []
            if tbl_el.attributes.get("bypara", False):
                col = []
                for row_el in tbl_el.content:
                    if isinstance(row_el, pf.Para):
                        row.append(pf.TableCell(row_el))
            else:
                for row_el in tbl_el.content:
                    if isinstance(row_el, pf.Div) and "tcell" in row_el.classes:
                        col = []
                        for col_el in row_el.content:
                            col.append(col_el)
                        row.append(pf.TableCell(*col))

            rows.append(pf.TableRow(*row))
        
        else:
            pass
     
    kwargs = {}
    if header_found:
        kwargs["header"] = pf.TableRow(*headers) 
    if widths:
        kwargs["width"] = widths
    if aligns:
        kwargs["alignment"] = aligns
    if not caption is None:
        kwargs["caption"] = caption
    
    return pf.Table(*rows, **kwargs)


def prepare(doc):
    pass


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action, doc=doc, prepare=prepare, finalize=finalize)

if __name__ == "__main__":
   main()
