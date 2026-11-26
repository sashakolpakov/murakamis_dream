# The remaining terminal families on their full smaller input disks

Research deduction, 5 November 2026. Three terminal own/external type
families have a strict full-row comparison on the entire smaller input
disk, without a coupling multiplier. Together with the separate coupled
three-three theorem, this supplies the terminal right-sector estimate
near every actual open reference of length at least three. The
three-three word of length two remains outside this combined statement.
No dominance of the remaining open source is asserted.

## 1. Original action and the complete row envelope

Let \(\epsilon\) denote the last type minus three and \(\nu\)
the type minus three of its unchanged attached external leg \(a\).
Use the closed disks
\[
 D'_3=\{|a-(.35-.01i)|\le.083\},\qquad
 D'_4=\{|a-(.30-.052i)|\le.060\}.                       \tag{1}
\]
The original holomorphic endpoint map
\((e(a),t(a),u(a))\) exists on a neighborhood of the larger original
typed disk. Its optimized action is
\[
 \begin{split}
 P_\epsilon(a)&=\mathcal X_\epsilon(a,e(a),t(a),u(a)),\\
 \mathcal X_\epsilon(a,e,t,u)
   &=g(t+a)+g(t+e)-(2+\epsilon)g(t)+2\pi iat\\
   &\quad-g(a)-(1+\epsilon)g(e)+J(e)+F(e,u),\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu.
 \end{split}                                                   \tag{2}
\]
These are precisely the original phases and logarithmic lifts of
[the terminal comparison](research_mixed_terminal_half_endpoint_gap.md).
In particular the full terminal diagonal contributes
\(-\epsilon g(e)\); it has not been dropped.

Set
\[
 h_h=\Re\{J(1/2)+F(1/2,1/4+i\log3/(4\pi))\},
 \qquad b_2=-4J(1/4).
 \tag{3}
\]
For \(a=x+ih\), the complete bare raw envelope at the real
terminal half-period is
\[
 \mathcal R_\epsilon(a)=\max_{0\le v\le1}
 \left\{\int_0^v\log|1-e^{-2\pi i(a+s)}|\,ds
     +J(v+1/2)-(2+\epsilon)J(v)-2\pi hv\right\}.
 \tag{4}
\]
The periodic real primitive is used in (4), so revived upper rows
remain present. The [all-height row theorem](research_mixed_terminal_half_row_envelope.md)
gives the continuous subharmonic majorant
\[
 \mathcal R_\epsilon(a)\le
 \max\{R_-(a),-2\pi h,b_2/2,b_2/2-\pi h\},
 \tag{5}
\]
where
\[
 R_-(a)=\max_{0<v<1/2}
 \Re\{J(a+v)-J(a)+J(v+1/2)-(2+\epsilon)J(v)+i\pi av\}.
 \tag{6}
\]
The omitted zero branch is redundant because the lower maximum is
at least its endpoint value zero. The lower maximizer is unique and
its real second derivative is less than \(-2\pi\), at every
finite neighboring height with \(0<x<1/2\). Neither (5) nor
the present proof deletes upper rows outside the old cyclic height
bands.

**Theorem 1.** For
\[
             (\epsilon,\nu)\in\{(0,1),(1,0),(1,1)\},
 \tag{7}
\]
one has
\[
 \Re P_\epsilon(a)-h_h-\mathcal R_\epsilon(a)>1/500
                         \qquad(a\in D'_{3+\nu}).       \tag{8}
\]

The numerical premise is the strict boundary comparison with each
of the four branches in (5), certified on the original cells below.
Each branch is continuous and subharmonic; \(P_\epsilon\) is
holomorphic on a neighborhood of the whole disk. The superharmonic
minimum principle therefore extends each strict gap to the disk and
proves (8). This uses the actual row-rate subharmonicity, not a
holomorphic interpretation of the real maximizing row.

## 2. First-order whole-cell bounds with the saved endpoint witnesses

For every old endpoint cell meeting the circle in (1), revalidate
its original zero-log root enclosure on the whole parameter cell.
The same saved centers and inverse also validate a midpoint root
disk of radius \(10^{-10}\). No complex root is proposed.

At the cell midpoint \(a_0\), enclose the scalar lower-row
maximizer by rational endpoints with opposite signs of its exact
derivative. The saved replay uses these same endpoints. On the whole
cell the derivative is positive at \(v=1/5\) and negative at
\(v=2/5\). Strict concavity and its derivative bound enclose the
whole moving maximizer from the midpoint trial \(v_0\):
\[
 |v_*(a)-v_0|\le\frac{|E_v(a,v_0)|}{2\pi}.
 \tag{9}
\]
Here \(E\) denotes the rate in (6). The enclosure is intersected
with \([1/5,2/5]\); this intersection preserves the exact maximizer.
Sign-validated scalar bisection supplies only the author midpoint
brackets, not a new conditional complex root or parameter subdivision.

Stationarity cancels all endpoint response terms, giving
\[
 P_\epsilon'(a)=g'(t(a)+a)+2\pi it(a)-g'(a).
 \tag{10}
\]
For the lower-row gap \(G_-=\Re P_\epsilon-h_h-R_-\),
the real gradient is represented by the complex quantity
\[
 d_-(a)=g'(t(a)+a)+2\pi it(a)
                         -g'(a+v_*(a))-2\pi iv_*(a):
 \quad\nabla G_-=(\Re d_-,-\Im d_-).
 \tag{11}
\]
For the other three branches the representatives are, respectively,
\(P_\epsilon'-2\pi i,P_\epsilon',P_\epsilon'-\pi i\).
If the physical parameter cell has midpoint \(a_0\) and real and
imaginary halfwidths \(r_x,r_y\), each branch satisfies
\[
 G_j(a)\ge G_j(a_0)
       -\sup_{\rm cell}|\Re d_j|\,r_x
       -\sup_{\rm cell}|\Im d_j|\,r_y.
 \tag{12}
\]
The midpoint values use the original tiny root disks and a bracket
containing the actual maximizing row. Thus (12) is a whole-cell
lower bound, not a sampled phase comparison. Independent interval
enclosures of correlated quantities only enlarge the outward error.

The new circles have normalized radii \(83/90\) and \(15/16\)
in the original endpoint parameter squares. An exact rational
minimum/maximum squared-norm test selects every old closed leaf
meeting the appropriate circle. The checker traverses the complete
original four-family tree, checks all split addresses and old
exclusions, and performs (12) on only the three families (7).
Their circle-cell counts are respectively \(184,135,138\):
457 old cells and 1,828 branch inequalities. No old excluded box
meets either smaller circle. The fixed acceptance floor in every
case is \(1/500\); no diagnostic output, trial multiplier, or
new cover is an acceptance input.

## 3. The finite terminal right sector and actual-word coverage

Compactness and continuity extend (8) to an ambient neighborhood of
each entire disk (1), with gap greater than \(3/2000\). Apply
[the full terminal right-angle reduction](research_mixed_endpoint_polynomial_collar.md),
which includes every raw row and the physical endpoint layer. With one
total finite-source and ordinary-color tolerance \(\eta<1/2000\),
it gives, uniformly in that neighborhood,
\[
 \begin{split}
 &\left|C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ie})
          H_N(w_R,e^{2\pi ie})
          d_N(e^{-2\pi ie})^\epsilon e^{2\pi iN\sigma e}\right|\\
 &\hspace{1cm}\le C N^A
      \exp N\{\Re P_\epsilon(a)-1/1000-K(e)\},\\
 &\qquad 1/2\le e\le1,\quad\sigma\in\{0,\epsilon\},
       \qquad K(e)=-\int_{1/2}^e\log\sin\pi t\,dt\ge0.
 \end{split}                                                   \tag{13}
\]
The actual terminal Fourier polynomial has uniform upper rate zero
on this real sector, including its endpoint layer, and the selected
monomial has unit modulus. The full terminal factor is nevertheless
retained in both (2) and (13). Any allocated external halfweight is
the same on both sides and can be multiplied without dividing by a
finite polynomial. Both level parities and every fixed ordinary
color derivative hold on smaller color disks.

**Corollary 2.** Estimate (13) applies near every actual terminal
reference of a word of length \(m\ge2\) whose last two types are
\((4,3),(3,4)\), or \((4,4)\). Combining it with the completed
[coupled three-three estimate](research_mixed_terminal_coupled_disk_gap.md)
gives the same estimate with the common smaller loss \(1/5000\)
near every actual terminal reference of every word with \(m\ge3\).

Indeed every nonprivate attached leg is in its corresponding smaller
disk by [the exact open-leg coverage theorem](research_mixed_open_local_factor_coverage.md),
including the first endpoint's attached leg when \(m=2\). For
the three families (7) no preceding critical equation is needed.
For the remaining ending \((3,3)\), the coupled theorem requires
that the penultimate block be ordinary, hence \(m\ge3\).
The ending \((3,3)\) case at length two and the single-vertex
normalization are not added by this corollary.

The estimate is available on a genuine neighborhood of the actual
reference; subsequent targets there need not satisfy any critical
equation. It does not follow that arbitrary height attenuation or
arbitrary motion of the other boundary coordinates remains in that
neighborhood. Attaching the unchanged local interior phases still
retains their completion loss and the surviving cut tangent. No
global boundary inequality or whole open-source asymptotic is
inferred from this terminal-sector result alone.

## Reproduction

    python3 experiments/check_mixed_terminal_remaining_disk_gaps.py --precision 256
    python3 experiments/check_mixed_terminal_remaining_disk_gaps.py --precision 320 --input repro/results/research-mixed-terminal-remaining-disk-gaps.json --output repro/results/research-mixed-terminal-remaining-disk-gaps-replay.json

The focused checker binds the original endpoint author and replay,
the completed source lemmas, the smaller-disk extraction, and the
coupled theorem's saved replay. Saved mode keeps every row bracket
and old parameter address unchanged. It makes no new complex-root
proposal and performs no parameter refinement.
