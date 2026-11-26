from pathlib import Path
import re,json,hashlib,shutil
D=Path('/private/tmp/md-quantitative-appendices'); R=Path('/private/tmp/murakamis_dream-publication')
e=(D/'E-intro.tex').read_text()+(D/'converted-E.tex').read_text()
f=(D/'F-intro.tex').read_text()+(D/'converted-F.tex').read_text()
for old,new in [
 ('The dependencies are the current authoritative notes:', 'The finite identities used below have the following roles. Their separately available proofs are linked for reference:'),
 ('Dependencies and where the old proof used longness','Finite identities and the four uses of long twists'),
 ('Longness enters the present published joint proof','The long-twist hypothesis enters the joint Fourier argument'),
 ('the current joint-transform proof','the joint Fourier transform'),
 ('The critical action in the limit is defined in Sections 4 and 7.',r'The critical action in the limit is defined in Sections~\ref{sec:qe-4} and~\ref{sec:qe-7}.'),
 ('Section 7 places the whole path',r'Section~\ref{sec:qe-7} places the whole path'),
 ('These examples retain the original knot/parity qualification. They are not claims of a new topological family or priority.', 'These examples retain the original knot/parity qualification.'),
]:e=e.replace(old,new)
f=f.replace('Thus (1), with those transported frames',r'Thus \eqref{eq:ft-1}, with those transported frames')
f=f.replace(r'\hyperref[sec:ft]{ordered disk-page proof}, Section 6',r'ordered disk-page proof in Section~\ref{sec:ft-6}')
f=f.replace(r'Section 4 of the \hyperref[sec:fg]{completion proof}',r'Section~\ref{sec:fg-4}')
f=f.replace(r'Section 3 of the \hyperref[sec:fg]{completion proof}',r'Section~\ref{sec:fg-3}')
f=f.replace(r'Sections~\ref{sec:fc-2}--6 of the preferred-cusp note',r'Sections 2--6 of the \href{https://sashakolpakov.github.io/murakamis_dream/notes/actual_main_meridian_preferred_cusp.html}{preferred-longitude calculation}')
f=f.replace('This note identifies','This section identifies')
# Make existing numbered formulas readable in native manuscript source.
for key,text in [('E',e),('F',f)]:
 text=text.replace(' \\begin{equation}', '\n\\begin{equation}').replace('\\end{equation} ', '\\end{equation}\n')
 text=text.replace(' \\[','\n\\[').replace('\\] ','\\]\n')
 text=re.sub(r'\n{3,}','\n\n',text)
 (D/('appendix-'+key+'.tex')).write_text(text)
 rel={'E':'manuscript/sections/E-quantitative-finite-sums.tex','F':'manuscript/sections/F-quantitative-octahedral-geometry.tex'}[key]
 (R/rel).write_text(text)
# Archive files before the narrow two-line integration changes.
a=D/'originals';a.mkdir(exist_ok=True)
for rel in ['manuscript/main.tex','manuscript/sections/09-reproduction.tex']:
 target=a/Path(rel).name
 if not target.exists():shutil.copy2(R/rel,target)
p=R/'manuscript/main.tex';s=p.read_text();marker=r'\input{sections/D-marked-cell-calibration}'
addition='\n'+r'\input{sections/E-quantitative-finite-sums}'+'\n'+r'\input{sections/F-quantitative-octahedral-geometry}'
if r'\input{sections/E-quantitative-finite-sums}' not in s:s=s.replace(marker,marker+addition)
p.write_text(s)
p=R/'manuscript/sections/09-reproduction.tex';s=p.read_text();old='The linked companions describe the precise input conventions for these checks. Such finite checks can detect sign or indexing errors; the arbitrary-tree induction, uniform Fourier bounds and completeness argument remain written proofs.'
new=r'Appendix~\ref{app:quantitative-sums} gives the full quantitative finite-sum proof, including both uniform Newton estimates, the weighted contraction and the charge-tail bounds. Appendix~\ref{app:quantitative-geometry} gives the complete ordered attachment, positive angular charts, primitive-period completion, volume calibration and preferred-cusp argument. The linked versions are optional separately available copies of those proofs. Such finite checks can detect sign or indexing errors; they do not replace the written proofs.'
assert old in s or new in s
s=s.replace(old,new);p.write_text(s)
