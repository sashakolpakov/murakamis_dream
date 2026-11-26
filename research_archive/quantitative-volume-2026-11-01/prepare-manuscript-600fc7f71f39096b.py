from pathlib import Path
import re
root=Path(__file__).resolve().parent
p=root/'manuscript-quantitative-circle-trees.tex'
s=p.read_text()
s=re.sub(r'\\label\{([^}]+)\}',lambda m:r'\label{sec:circle-'+m.group(1)+'}',s)
s=s.replace(r'\textbf{Theorem.}',r'\begin{theorem}[A degree and twist criterion]\label{thm:circle-quantitative}')
s=s.replace('\nThe constant in (5) is conservative.', '\n\\end{theorem}\n\nThe constant in (5) is conservative.')
def eq(m):
    body=m.group(1)
    tag=re.search(r'\\tag\{(\d+)\}',body)
    if not tag:return m.group(0)
    n=tag.group(1)
    body=re.sub(r'\\tag\{\d+\}',lambda m:r'\label{eq:circle-'+n+'}',body)
    return '\\begin{equation}'+body+'\\end{equation}'
s=re.sub(r'\\\[(.*?)\\\]',eq,s,flags=re.S)
# Plain-text equation references only. Parenthesized function arguments
# are protected by a preceding letter or underscore.
s=re.sub(r'(?<![A-Za-z0-9_\\])\(([1-9][0-9]?)\)',lambda m:r'\eqref{eq:circle-'+m.group(1)+'}',s)
s=s.replace(r'\tightlist','')
s=re.sub(r'\\href\{([a-z0-9_]+)\.md\}',lambda m:r'\href{https://sashakolpakov.github.io/murakamis_dream/notes/'+m.group(1)+'.html}',s)
s=s.replace(r'\label{sec:circle-an-explicit-volume-theorem-for-ordered-trees-of-crossing-circles}',r'\label{ch:quantitative-circle-trees}')
start=s.index('\\begin{figure}')
end=s.index('\\end{figure}',start)+len('\\end{figure}')
fig=r'''\begin{figure}[ht]
\centering
\input{figures/octahedral-page-attachment}
\caption{Attaching one octahedron in a projection half of the actual
augmented tangle diagram. Equal labels are identified, and the blue
faces have opposite boundary orientations. The triangle becomes
internal; the other three shaded disk faces retain the parent circle
and introduce the child circle, as listed in
\eqref{eq:circle-10}. Only the attachment faces are blue. The labels
$O_v,O_w$ belong to the original auxiliary crossing circles.
The same attachment is made in the other projection half.}
\label{fig:circle-octahedral-attachment}
\end{figure}'''
s=s[:start]+fig+s[end:]
p.write_text(s)
(root/'figures').mkdir(exist_ok=True)
(root/'figures/octahedral-page-attachment.tex').write_bytes((root/'octahedral-page-attachment.tex').read_bytes())
main=Path('/Users/sasha/volume-conjecture/manuscript/main.tex').read_text()
preamble=main.split('\\title{',1)[0]
(root/'manuscript-preview.tex').write_text(preamble+r'''
\begin{document}
\setcounter{chapter}{8}
\input{manuscript-quantitative-circle-trees}
\end{document}
''')
