---
author:
- My name
subtitle: Some subtitle
title: Some title
cmd: cls & pandoc ../tests/acronyms.md --to=latex -F acronyms.py && cls && pandoc ../tests/acronyms.md -s -F acronyms.py -H acronyms_header.tex --to=latex
header-includes:
	- \usepackage{RandomExample}
	- \usepackage{YetAnotherExample}
---

# List of Acronyms

\printglossary[type=\acronymtype,title=Acronyms]

# A Title

Lorem ipsum dolor [SA](acro "sit amet"), consectetur adipisicing elit
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Some examples are [AFK](acro "away from keyboard") and [ANFSCD](acro "and now for something completely different"). You can also repeat them: [SA](acro) or [AFK](acro).