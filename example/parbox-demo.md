Some Markdown text with  *mark-up* that works.

# Original

\parbox[t]{0.4\linewidth}{Some Markdown text with  *mark-up* that does not work.}\hfill
\includegraphics[width=0.4\linewidth]{image.png}

# New

![Some Markdown text with  *mark-up* that **should** work](image.png){.parbox}
