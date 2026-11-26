from pathlib import Path
import shutil
root=Path('/private/tmp/murakamis_dream-publication')
src=Path('/private/tmp/md-all-circle-volume-publication')
shutil.copy2(src/'manuscript-quantitative-circle-trees.tex',root/'manuscript/sections/08a-quantitative-circle-trees.tex')
shutil.copy2(src/'octahedral-page-attachment.tex',root/'manuscript/figures/octahedral-page-attachment.tex')
figure=(src/'octahedral-page-attachment.tex').read_text()
standalone=r'''\documentclass[tikz,border=9pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath}
\usetikzlibrary{arrows.meta,calc}
\begin{document}
'''+figure+r'''
\end{document}
'''
(root/'book/figures/octahedral-page-attachment.tex').write_text(standalone)
for ext in ('svg','png'):
 shutil.copy2(src/f'octahedral-page-attachment.{ext}',root/f'book/figures/octahedral-page-attachment.{ext}')
shutil.copy2(src/'octahedral-page-attachment-standalone.pdf',root/'book/figures/octahedral-page-attachment.pdf')
p=root/'manuscript/main.tex';s=p.read_text()
start=s.index('\\title{');end=s.index('\\begin{document}',start)
s=s[:start]+r'''\title{\Huge Volume limits for arborescent knots\\[8pt]\Large Long twists and an explicit condition\\for ordered tangle trees\\[18pt]\large Finite knot invariants, hyperbolic filling,\\and the preferred cusp shape}
\author{}
\date{1 November 2026}
'''+s[end:]
start=s.index('\\chapter*{Abstract}');end=s.index('\\tableofcontents',start)
s=s[:start]+r'''\chapter*{Abstract}
We prove the volume conjecture for two specified classes of arborescent knot diagrams built by ordered stacking and quarter-turns of two-string tangles. The first is a recursive construction in which independently sufficiently large signed twist numbers give a hyperbolic knot and the volume limit. Its elementary pieces retain their original crossing circles, disk framings and endpoint order.

The second result gives an explicit numerical condition for ordered trees with one crossing-circle operator at every vertex. If $d_v$ is the degree of a vertex and $n_v$ is its signed crossing power, then
\[
                    \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}
\]
suffices whenever the original strand pairing gives a knot. This condition permits short or zero powers at sufficiently large-degree vertices. It also gives the explicit sufficient bound $|n_v|\ge8192\sqrt E$ for a tree with $E$ edges. Every diagram, parity choice and integer power is fixed before the root-of-unity level $N$ tends to infinity. The limits include both parities and composite levels, and only auxiliary circles are filled.

The proof starts with the finite matrices defining the invariant and retains their derivative data at repeated spectral roots. For the long-twist construction, positive multiplication coefficients and exact rational inequalities control the signed color terms. For the quantitative tree theorem, a literal projection cut gives two octahedra per edge. Positive deformations of these cells fit in the original cyclic order, and their actual primitive periods give smooth filling even when the total meridian logarithm has left a small neighborhood of zero. The full Fourier calculation keeps the charge tails and boundary contributions, identifies a nonzero leading term, and matches its calibrated action with the volume of the original knot complement.

For the quantitative class we also prove a uniform microscopic main-meridian profile for the zero-framed reduced ADO invariant. Its exact crossing and framing factor is retained, and its first correction is the preferred cusp shape of the filled knot. The construction hypotheses and the knot-pairing test are stated explicitly; the results do not classify all arborescent knots.

'''+s[end:]
s=s.replace('\\input{sections/08-filling}\n','\\input{sections/08-filling}\n\\input{sections/08a-quantitative-circle-trees}\n')
p.write_text(s)
p=root/'manuscript/sections/01-introduction.tex';s=p.read_text()
s=s.replace('\\chapter{The knots, the theorem, and the proof}', '\\chapter{The knots, the theorems, and their proofs}')
s=s.replace('We prove this limit for the family of knot diagrams constructed below, once every designated twist region has sufficiently many twists. The family permits arbitrary finite branching and nesting of tangles, subject to a precise recursive rule. We first explain the geometric operations and only then give symbols for the rule. A construction expression records an actual diagram: it includes the order of the pieces and the positions where they are joined.',r'''The first theorem proves this limit for the recursive family of knot diagrams constructed below, once every designated twist region has sufficiently many twists. The family permits arbitrary finite branching and nesting, subject to its precise construction rule. Chapter~\ref{ch:quantitative-circle-trees} proves a second theorem for ordered trees with one crossing-circle operator at every junction: an explicit condition involving their degrees and signed crossing powers permits some short coefficients. We first explain the geometric operations and then state both scopes. Every construction records an actual diagram, including the order of its pieces and the positions where they are joined.''')
s=s.replace('There are two different limiting questions, and our theorem uses only one at a time. Choose a finite construction, choose the signs and sufficiently large integer numbers of twists, and hold all these choices fixed. Then let $N$ tend to infinity. The theorem does not let the diagram or its twist numbers grow with $N$. Different twist regions may have different signs and arbitrarily different large magnitudes.',r'''Both theorems take the same quantum limit. Choose a finite construction and signed integer twist numbers satisfying the applicable hypothesis, and hold them fixed. Then let $N$ tend to infinity. Neither the diagram nor its twist numbers grow with $N$. In the first theorem the individual twists can have different signs and arbitrarily different large magnitudes. In the quantitative theorem their sizes and junction degrees enter the explicit sum in Theorem~\ref{thm:circle-quantitative}.''')
s=s.replace("This paper does not extend its theorem by replacing that condition with a more general feasibility test.",r'''Chapters~\ref{ch:source}--\ref{ch:filling} retain this condition. The different class in Chapter~\ref{ch:quantitative-circle-trees} has its own finite-source estimates and geometric completion; it is not inserted into this recursive proof by changing the meaning of ``completed.''''')
s=s.replace("For instance, $C(h\\Turn(h^s))$ places the inner complete leaf parameters at $1/4$, outside the strict interval used in this paper's local asymptotic argument. These exclusions describe the scope of this proof, not an assertion that no other methods apply to those knots.",r'''For instance, $C(h\Turn(h^s))$ places the inner complete leaf parameters at $1/4$, outside the interval used in the first proof. Such a circle-tree presentation can instead fall under Theorem~\ref{thm:circle-quantitative} when its explicit degree and twist condition holds. The exclusions in this paragraph concern Theorem~\ref{thm:main}.''')
anchor='\\section{A guide to the proof and its terminology}'
addition=r'''\section{An explicit criterion for circle trees}
The second construction uses the same actual stacking, quarter-turn and closing operations. At each vertex of a finite ordered tree put one crossing box with signed power $n_v$; its augmented version retains that box's crossing circle. Each tree edge is a quarter-turn of a child tangle. There are no unmarked product junctions, and terminal crossing circles are vertices of degree one. The cyclic order and the position of the crossing box among its children remain part of the diagram. Section~\ref{sec:circle-the-knot-construction} gives the full recursion.

If $d_v$ is the degree of vertex $v$, Theorem~\ref{thm:circle-quantitative} proves hyperbolicity and the same volume limit under the explicit condition
\[
                       \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25},
\]
provided the original endpoint pairing gives a knot. The angle feasibility required by the proof is automatic for this literal tree construction. Every $|n_v|\ge8192\sqrt E$ suffices when the tree has $E$ edges, but individual powers may be short or zero at vertices of sufficiently large degree. Adding an identity braid at an unmarked junction also gives an application when the sum bound holds; its added crossing circle contributes $1/d_v$, rather than zero.

The quantitative theorem uses a direct cut of the actual augmented exterior into two octahedra per tree edge. Its positive geometric path keeps track of the original primitive slopes even when their accumulated logarithms are not small. The finite invariant has a uniform main-meridian profile, with its exact scalar retained; the first correction is the preferred cusp shape of the resulting knot complement. The size of the tree and every crossing power remain fixed as $N$ grows.

'''
s=s.replace(anchor,addition+anchor)
s=s.replace('The proof first studies the augmented diagram,', 'The long-twist proof first studies the augmented diagram,')
s=s.replace('The appendices give the finite identities and detailed analytic estimates.', 'The appendices give the finite identities and detailed analytic estimates for the long-twist argument. Chapter~\\ref{ch:quantitative-circle-trees} gives the quantitative theorem and links its complete finite-sum, ordered-cut and geometric completion proofs.')
p.write_text(s)
p=root/'manuscript/sections/09-reproduction.tex';s=p.read_text()
s=s.replace("The theorem has two kinds of proof obligations. Most are analytic or geometric arguments written in this manuscript. Two local inequalities are reduced to finite rational certificates supplied with the paper. This chapter explains how to inspect and replay those certificates, what a successful replay establishes, and what remains outside the theorem's construction class.","The two theorems combine written analytic and geometric arguments with finite checks of different kinds. The long-twist proof reduces two local inequalities to exact rational certificates supplied with the paper. The quantitative circle-tree proof establishes its uniform bounds analytically; separate finite checks verify its edge formulas, face identifications and peripheral identities. This chapter distinguishes those roles and records the scope of each theorem.")
anchor='\\section{Building the two reading views}'
addition=r'''\section{Checking the quantitative tree formulas}
The elementary edge equations and complex-strip estimates used by Chapter~\ref{ch:quantitative-circle-trees} have a portable reproduction command:
\begin{verbatim}
python3 repro/run_research_checks.py curvature-fillings
\end{verbatim}
The runner checks exact symbolic edge identities and finite samples of the stated complex inequality. Its output separates those computations from the uniform analytic proof. The linked ordered-decomposition and geometric-completion companions also provide finite checks of labeled cell attachments and the full peripheral matrix words. Such finite checks can detect sign or indexing errors; the arbitrary-tree induction, uniform Fourier bounds and completeness argument remain written proofs.

'''
s=s.replace(anchor,addition+'\\section{Building the manuscript and illustrated guide}')
start=s.index('The Sphinx reading site and the existing Markdown book are built separately:')
end=s.index('\\section{What has and has not been proved}',start)
s=s[:start]+r'''The illustrated guide is built separately:
\begin{verbatim}
python3 tools/build_book.py
python3 tools/check_book.py
\end{verbatim}
It is written to \sourcefile{docs/} and links the same authored PDF. Documentation builds do not execute research scripts. The guide also links the broader research companions and states their hypotheses separately from the two theorem classes developed here.

'''+s[end:]
start=s.index('\\section{What has and has not been proved}')
s=s[:start]+r'''\section{What has and has not been proved}
Theorem~\ref{thm:main} is uniform in the level for each fixed finite completed expression and each fixed sufficiently long signed filling tuple. It includes both parity sequences and composite levels. Its threshold can depend on the expression, its complete geometry and its retained half-twist pattern, but imposes no bound on ratios between the long slopes.

Theorem~\ref{thm:circle-quantitative} uses a different sufficient hypothesis: the literal ordered circle tree and the explicit sum $\sum_vd_v/(d_v^2+n_v^2)\le2^{-25}$. The full diagram, all degrees and all integer powers are fixed before the limit. The theorem gives actual hyperbolicity and volume equality, a uniform microscopic meridian profile with its exact scalar, and the preferred-cusp correction. It permits short coefficients under this condition; it does not prove a statement about arbitrary short or rational fillings.

Both results keep the original strand order, knot-pairing test, disk framings and unfilled main cusp. The octahedral attachment is proved by actual labeled cuts. A scalar equality in $\cH_N$ is not used as a tangle isotopy. The continued boundary word used for the preferred-cusp calculation becomes the preferred longitude of the smooth filled knot only at the endpoint of the geometric path.

These are sufficient construction hypotheses, not a classification of all arborescent knots. The completed-box condition remains part of Theorem~\ref{thm:main}; the quarter-index states in circle trees are treated by the separate proof in Chapter~\ref{ch:quantitative-circle-trees}. More general strict ordered Conway trees have a long-twist theorem in the linked research companions, with their own full source and marked-geometry proofs. No general short-filling theorem follows merely from the existence of complete augmented cells or from an upper bound on the absolute values of a larger sum.
'''
p.write_text(s)
