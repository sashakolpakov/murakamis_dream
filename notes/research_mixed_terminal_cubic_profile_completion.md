# Stronger complete terminal bounds from the saved cubic costs

Research deduction and exact saved-data completion, 6 November 2026.
The original four canonical comparisons admit raw profile gap \(1/125\)
and finite two-factor rate gap \(1/250\). This strengthens their earlier
\(1/800\) and \(1/1600\) gaps without changing a reference, contour,
source row, primitive value or selected height. Every comparison here
uses \(H=.01\), including both alternatives of the complete Fourier
weight. No conclusion over a new external-reference domain is asserted.

## 1. Replace each old scalar cost once

Retain the four original references
\[
 b_0=.35-.01i,\qquad b_1=.30-.052i,\qquad
 (\beta,\epsilon)\in\{0,1\}^2,\qquad H=1/100.
 \tag{1}
\]
Use the action, incoming marginal, targets and source hypotheses of the
[complete all-profile theorem](research_mixed_terminal_all_profile_completion.md).
Its source is the original adjacent ordinary/terminal product, with
the selected coordinate of own type four.

The [new scalar-cost theorem](research_mixed_terminal_cubic_cost_and_response_bounds.md),
Sections 1--4, retains the simultaneous three-node curvature allocation.
Its cubic tangent inequalities, under the already verified reference and
force guards, replace the old upper gains by
\[
                     G_s<7/1000,\qquad G_t<9/500.
 \tag{2}
\]
The selected-coordinate cost and all trial values remain unchanged.
The resulting common main upper bounds at (1) are
\[
 \begin{split}
 \sup D_1&<-\frac{463}{10000}+\frac7{1000}+\frac9{500}
                    +\frac{867}{80000}
             =-\frac{837}{80000}<-\frac1{100},\\
 \sup_{a_R\in P}D_0&<-\frac{109}{1000}+\frac7{1000}+\frac9{500}
                    +\frac{1071}{20000}
             =-\frac{609}{20000}<-\frac1{100}.
 \end{split}
 \tag{3}
\]
Here \(D_1\) is factorial and \(D_0\) is forced. The latter is a
full-\(P\) estimate at the same height; no branch domain or estimate
from \(H=.0135\) is substituted.

For the reserved terminal plane, only its ordinary-index cost changes.
Let \(E_{\nu,j}^{\rm old}\) and \(S_j^{\rm old}\) be the exact saved
branch upper and positive ordinary-index gain for canonical case \(j\)
in the [reserved-plane record](../repro/results/research-mixed-terminal-reserved-plane-transfer.json).
Define
\[
 E_{\nu,j}^{\rm new}
       =E_{\nu,j}^{\rm old}-S_j^{\rm old}+\frac7{1000}.
 \tag{4}
\]
This is a replacement of the identified cost in the saved sum, not a
subtraction from an unrelated upper bound. The proof's coarse sums
give, with \(S^{\rm coarse}=19881/1587200\),
\[
 \begin{split}
 E_1^{\rm new}
 &<\frac{19}{500}+\frac7{1000}
                          +\frac{(127/1000)^2}{4}<\frac{99}{2000},\\
 E_0^{\rm new}
 &<\frac3{500}+\frac7{1000}
                          +\frac{33}{200}\frac{17}{100}
                          <\frac{99}{2000}.
 \end{split}
 \tag{5}
\]
Equivalently one replaces \(S^{\rm coarse}\) in each original coarse
sum. One cannot subtract this coarse gain from each case-specific
upper in place of its own saved \(S_j^{\rm old}\).

## 2. All nonmain terminal labels

The original sixteen alias endpoint labels have bare plane reserve
greater than \(.059\), and the constant label has reserve greater than
\(.063\), as retained in the
[reserved-profile completion](research_mixed_terminal_reserved_profile_completion.md).
Thus (5) gives their joined gaps greater than
\[
             .059-.0495=.0095>1/125,\qquad
             .063-.0495=.0135>1/125.
 \tag{6}
\]
The eight real-cut labels and the physical entropy label per case are
the same nine families in the old
[all-profile saved completion](../repro/results/research-mixed-terminal-all-profile-completion.json).
For the 34 families not using the direct private-left transfer, retain
their saved bare upper \(U_{j,\rho}\) and recombine
\[
       U_{j,\rho}+\max_{\nu\in\{0,1\}}E_{\nu,j}^{\rm new}<-1/125.
 \tag{7}
\]
The exact endpoint check is performed for every family separately;
the maximum belongs to \((\beta,\epsilon,\rho)=(1,1,\text{four family }0)\).
Neither the old analytic evaluations nor their source-cell extraction
is repeated.

The two remaining real faces have terminal type four, transform on
its main height and private coordinate \(e=.27\). Their unchanged
[direct transfer](research_mixed_terminal_private_left_joint_transfer.md)
has \(U_L<0\), adds \(U_L\) to the trial value, and changes only the
negative transform force by \(0<d_L<.2<-A_t\). Every useful cost is
retained. The negative-force cubic gain decreases when that force is
moved toward zero. Consequently each face inherits (3), with the
additional negative \(U_L\), and also has gap greater than \(1/125\).

Equations (3), (6), (7) and these two direct faces cover the same
27 labels in each case: main, sixteen alias endpoints, eight real cuts,
entropy and constant. Every zero-mode join and vertical alias side is
then controlled by the original height-convex envelope, with all its
real endpoints retained.

The [new standalone checker](../experiments/check_mixed_terminal_cubic_profile_completion.py)
uses only standard-library exact fractions. It verifies every inherited
input hash from the completed all-profile record, all four source-case
associations and original height/force guards, the new polynomial
witnesses, each replacement (4), and all 36 real-cut/entropy comparisons.
Its [result](../repro/results/research-mixed-terminal-cubic-profile-completion.json)
records the old and new costs and the exact inequalities. It imports
no analytic evaluator and performs no source or root replay.

## 3. Complete finite source and unchanged scope

With the original \(M,p\) and \(\Lambda(b)=\Re\{M+p(b-b_*)\}\),
the exact finite source obeys
\[
 \begin{split}
 &|C_{1,N}(X_b,X_a)\mathcal V_{\epsilon,N}(w,X_a)
       d_N(X_a)X_a^{-N}|\,|d_N(X_b)|^{\beta/2}\\
 &\hspace{20mm}\le C_\tau N^{A_\tau}
       \exp N\{\Lambda(b)-1/125+\tau\},
       \qquad \tau>0,
 \end{split}
 \tag{8}
\]
at each reference (1), for all the original horizontal targets.
The ordinary-label replacements remain in their already proved scope:
both canonical input heights are in \([-.078,.021]\). The old complete
source and all branch allocations are therefore unchanged.

Taking a fixed tolerance, for example \(1/1000\), and absorbing the
polynomial prefactor leaves a finite exponential rate gap \(1/250\).
The strict spare amount is
\(1/125-1/1000-1/250=3/1000\).
Both level parities, the original ordinary-color neighborhood and its
fixed derivative orders are inherited from the complete source theorem.
All differentiations concern the original holomorphic source before
taking modulus bounds.

The reference points are certified canonical suffixes. This strengthens
their complete local finite-kernel inequalities; it does not establish
finite-word realization, a uniform comparison on \(K_3,K_4\) or
\(D_3,D_4\), an entire original invariant asymptotic, or a new knot-family
volume theorem.
