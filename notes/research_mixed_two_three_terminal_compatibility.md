# The two-vertex three-three terminal input is compatible

Research deduction, 5 November 2026. The length-two word \((3,3)\)
does not have an ordinary penultimate vertex. Reflection of its original
open action instead supplies the compatibility needed by the already
proved terminal multiplier inequality. No new critical root is computed.

## 1. Reflection and the endpoint fixed point

Use the original full action and uniqueness theorem from
[the open Hessian proof](research_mixed_open_word_hessian.md) and
[open localization](research_mixed_open_word_critical_localization.md).
For this word reflection is
\[
 (s_1,t_1,s_2,t_2,u_L,u_R)
       \longmapsto(t_2,s_2,t_1,s_1,u_R,u_L).               \tag{1}
\]
All \(J\) terms and the two ordinary endpoint terms are interchanged
in pairs. The quadratic chirp
\[
 Q_2=t_1s_2-s_1t_1-s_2t_2+s_1u_L+t_2u_R                \tag{2}
\]
is exactly invariant. Both ordinary colors are at their complete
reference for this critical-point statement. The product chamber is
reflection invariant, so strict Hessian uniqueness implies
\[
                         t_1=s_2=:a.                   \tag{3}
\]
The last original endpoint map has attached output \(t_0(a)=s_2\);
therefore the actual input satisfies
\[
                              a=t_0(a).                \tag{4}
\]
This is an endpoint fixed-point identity, not the ordinary two-leg
equation used for longer words.

The actual nonprivate coordinate lies in the common smaller disk
\(D=\{|a-(.35-.01i)|\le.083\}\).
For the holomorphic function \(\mathcal U\) in
[the accepted coupling theorem](research_mixed_terminal_coupled_disk_gap.md),
put \(V=e^{-2\pi ia}\) and \(B=e^{-2\pi it_0(a)}\).
Define the separate holomorphic expression
\[
             \mathcal U_{\rm fp}(a)=\frac{1+V^2}{V(1+V)}.
                                                               \tag{5}
\]
The denominator is nonzero on the retained cells below.
At (4), \(B=V\), so the original coupling function satisfies
\(\mathcal U(a)=\mathcal U_{\rm fp}(a)\). This equality is
asserted only at fixed points, not throughout the surrounding rectangles.
The expression (5) does not identify a fictitious ordinary leg.

## 2. Restricting the old endpoint tree

The original \((\epsilon,\nu)=(0,0)\) endpoint tree contains
3,439 nodes, including 1,645 accepted leaves and 75 outside-disk
exclusions. Each accepted leaf has an exact input rectangle \(A_i\)
and a certified attached-output disk, hence its enclosing rectangle
\(T_i\). A fixed point in that leaf must lie in
\[
                               A_i\cap T_i.             \tag{6}
\]
All endpoints of these two rectangles are rational: they use the
original dyadic input cell, stored rational center and stored radius.
Thus the disjointness decisions and intersections in (6) are exact.
The old author and independent replay establish the output enclosures
for every leaf before this extraction is applied.

Exactly six leaves survive, with node indices
\[
                 2030,\ 2031,\ 2033,\ 2034,\ 2123,\ 2126.
                                                               \tag{7}
\]
The focused checker also revalidates the original zero-log self-map
on these six whole input cells. Their clipped rectangles lie strictly
inside \(D\). On every one of them outward evaluation of (5) proves
\[
 \psi_{\rm fp}(a):=\log|\mathcal U_{\rm fp}(a)|+13\pi/100>0.
                                                               \tag{8}
\]
The proof uses the exponential modulus only. No inverse logarithm,
new root proposal, or parameter subdivision is involved.

**Theorem 1.** The actual complete-color terminal neighbor of the
open word \((3,3)\) belongs to the feasible set
\(\{a\in D:\psi(a)\ge0\}\) of the coupling theorem.
Consequently
\[
             \Re P_0(a)-h_h-\mathcal R_0(a)>1/4000.      \tag{9}
\]

Indeed the actual fixed point belongs to one accepted leaf, hence
to one of (7), where (8) holds. At that fixed point,
\(\psi=\psi_{\rm fp}>0\). The feasible-set conclusion of the
coupling theorem applies to every point satisfying its displayed
constraint; it does not require that the constraint be proved by an
ordinary vertex. This proves (9).

## 3. Finite terminal-sector consequence and scope

The strict gap has a small ambient neighborhood around the actual
input. As in the accepted coupling proof, choose that neighborhood
with gap \(9/40000\), and spend a single finite source tolerance
less than \(1/40000\). The complete endpoint polynomial theorem
then gives the original finite product bound
\[
 \left|C_{0,N}(e^{-2\pi ia},e^{-2\pi ie})
                  H_N(w_R,e^{2\pi ie})\right|
 \le C N^A
       \exp N\{\Re P_0(a)-1/5000-K(e)\},
 \qquad \tfrac12\le e\le1,                              \tag{10}
\]
on a sufficiently small fixed ordinary-color disk, with the same
rate for each fixed ordinary derivative. Here
\(K(e)=-\int_{1/2}^e\log\sin\pi t\,dt\ge0\).
Both parities and all terminal finite rows are retained.

Only the complete-color reference was required to satisfy (4).
Nearby integration targets and moving ordinary colors are not
required to solve it. At the critical reference the remaining
one-ended local phases retain their ordinary Schur completion loss.
This does not control large variations at the first boundary,
other outgoing contours, or the full open source. The length-one
case has no such terminal conditional factor and is not covered
by this deduction.

## 4. Reproduction

    python3 experiments/check_mixed_two_three_terminal_compatibility.py --precision 256
    python3 experiments/check_mixed_two_three_terminal_compatibility.py --precision 320 --input repro/results/research-mixed-two-three-terminal-compatibility.json --output repro/results/research-mixed-two-three-terminal-compatibility-replay.json

The record binds the original endpoint author/replay and the accepted
coupling author/replay, traverses every original tree node, retains all
six exact clipped rectangles, and records the strict
\(\psi_{\rm fp}\) margins. It does not claim that the original
coupling function is positive at every nonfixed point of these rectangles.
