---
author: Author Name
cmd: cls & pandoc -F ./filters/convert_lists.py .\tests\convert_lists.md --to=markdown
#testcmd: cls & test_filter.py unformat_abstract action
---

# A title

1. First ordered list item
2. Another item
    * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
    1. Ordered sub-list
4. And another item.

Some text

* Unordered list can use asterisks
- Or minuses
+ Or pluses

## Subtitle

0. Other list
1. Lorem
2. Ipsum
