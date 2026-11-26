# A centered evaluation plan for the next-four half-row bounds

Research specification, 6 November 2026. This gives an outward
evaluation procedure for all four scalar upper bounds in
[the next-four half-row theorem](research_mixed_selected_four_four_half_row_majorant.md),
using the actual-reference maps and necessary filters of the completed
next-four central certificate. It also fixes one inherited auxiliary
box for a prospective diagnostic. No evaluator, numerical diagnostic,
root calculation or cover is executed by this note.

## 1. The four expressions and their allocation

Use \(H=1/100\), \(\nu=1\) for the factorial Fourier
alternative and \(\nu=0\) for the forced alternative. The four
tests are
\[
 \mathcal H^{(4)}_{0,1},\quad\mathcal H^{(4)}_{0,0},\quad
 \mathcal H^{(4)}_{L,1},\quad\mathcal H^{(4)}_{L,0}.
\tag{1}
\]
Every quantity uses the same actual first-four/next-four reference
\((e_*,s_*;z_*,b_*)\) of a word of length at least three.
The outgoing leg carries its own halfweight. In particular
\[
 \begin{split}
 Q_4(s;z,b)&=g(s+z)+g(s+b)-3g(s)-g(z)-g(b)+2\pi izs,\\
 p&=g'(s_*+b_*)-\tfrac32g'(b_*),\\
 M&=\Re\Psi(e_*,z_*)+\Re Q_4(s_*;z_*,b_*)
                      -\Re g(z_*)-\tfrac12\Re g(b_*).
 \end{split}
\tag{2}
\]
The outgoing nonlinear half-row objective is
\(j(v)=\Re q(v+ih_b)-\Re g(v+ih_b)/2\), with
\(q(w)=g(w+1/2)-g(w)\). Its trial gradient after the
original tangent subtraction is
\[
 D_* =\log\left|\frac{1+B_*}{1-S_*B_*}\right|,
 \qquad G_b=\Gamma_{41/10}(D_*;\ .22-\Re b_*,\ .45-\Re b_*).
\tag{3}
\]
This is the clipped quadratic bound proved in the half-row theorem.
It must not be replaced by the next-three clipped-arccos optimizer:
the two outgoing objectives have different factorial powers.

## 2. Original next-four maps and filters

Let \(u\in[.217,.234]+i[.027,.045]\), \(U=e^{2\pi iu}\).
The maps \(E(U),Z(U),S(U)\) are the original endpoint maps.
The outgoing map is the own-four map
\[
 B_*(U)=\frac{1-Z(1-S)^3/(1-ZS)}{S},\qquad
 C_{\rm next}=
 \frac{1-SB_*}{B_*(1-SB_*)+(1-B_*)^3}.
\tag{4}
\]
Use the factored polynomial implementation in
[the next-four map provider](../experiments/certify_mixed_next_four_endpoint_budget.py),
and the same Horner/whole-box mean-value enclosure as
[the completed adaptive driver](../experiments/certify_mixed_next_four_adaptive_budget.py).
No old scalar \(\texttt{inspect}\) routine is called. Importing
its fixed maps or pure enclosure helpers is distinct from repeating
an old certificate evaluation.

The coordinate logarithms and every necessary filter are those in
Section 3 of the
[completed next-four central theorem](research_mixed_first_four_next_four_central_gap.md):
\[
 \begin{array}{c|c|c}
 &\Re&\Im\\\hline
 e_*&[.333,.363]&[-.051,-.019]\\
 z_*&[.246,.350]&[-.078,-.020]\\
 s_*,b_*&[.240,.360]&[-.102,-.001].
 \end{array}
\tag{5}
\]
The nonprivate coordinates \(z_*,s_*,b_*\) lie in the disk
of radius \(.060\) centered at \(.30-.052i\).
The real pair sums lie in
\[
 \Re(z_*+s_*)\in[.545,.77],\qquad
 \Re(s_*+b_*)\in[.527,.77].
\tag{6}
\]
The next external coordinate belongs to the same \(K_3\cup K_4\)
domain as in that theorem; its exponential has negative imaginary
part at every actual reference. The external coordinate can be
attached when the word has length three. It is not a private index.

For literal agreement with the adaptive reference filter, retain its
additional necessary scalar conditions
\[
 0\le d\le1,\qquad .045\le\Re(s_*+z_*)-.5\le.21,
 \qquad \Re\cot(\pi s_*)\ge2/5,
\tag{7}
\]
with \(d\) formed from the same \(S_*,Z_*\) and radial
increment. The coordinate height conditions in its scalar clipping
are already contained in (5). These are only necessary conditions;
they do not assert that every retained auxiliary point is realized
by an open word.

All exclusions require strict whole-box separation from a necessary
condition. Unresolved poles, logarithms or nonfinite enclosures cause
an inconclusive diagnostic, never an exclusion. After applying the
filters, coordinatewise intersections with (5) may be used to tighten
these pointwise scalar evaluations: every actual reference remains
in the resulting enclosure. No parameter derivative or integration
along those clipped coordinate boxes is used here.

## 3. Centered original primitives and the four outward values

Set precision before forming any transcendental constant. The
original primitive is
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},
 \qquad J(w)=g(w)-\frac{i\pi}{2}w(1-w),\quad0<\Re w<1.
\tag{8}
\]
Use the same centered enclosure as in
[the centered-primitive proof](research_mixed_centered_primitive_enclosure.md):
\[
 g(W)\subseteq g(w_0)+
     \Log(1-e^{-2\pi iW})(W-w_0),
\tag{9}
\]
where \(w_0\) is the exact dyadic rectangular center and the
whole convex rectangle \(W\) is inside the regular strip.
The point value uses the original principal dilogarithm in (8).
The exponential avoids its cut throughout that strip. Any primitive
argument failing this regularity check is inconclusive.

The actual private action uses the same auxiliary \(u\) directly:
\[
 S_{\rm cap}(e_*)=-2J(1/2-u)-3J(u)-J(e_*-u)+i\pi e_*u.
\tag{10}
\]
Only the fixed cut \(e_0=.27\) uses the original explicit
canonical square root and arctangent for \(u_c(e_0)\).
This is a fixed constant enclosure, not a proposed target root.

Write \(z_H^*=\Re z_*+iH\), \(\lambda=e^{2\pi H}/|Z_*|\),
and evaluate the two relative cap actions as follows:
\[
 \begin{split}
 \Delta_0={}&g(e_*+z_H^*)-g(e_*+z_*)-g(z_H^*)+g(z_*),\\
 \Delta_L={}&S_{\rm cap}(.27)-S_{\rm cap}(e_*)
       +J(.27+z_H^*)-J(e_*+z_*)-J(z_H^*)+J(z_*)\\
 &-i\pi(.27z_H^*-e_*z_*)-g(.27)+g(e_*).
 \end{split}
\tag{11}
\]
The main expression cancels the actual private action before
evaluation. The cut expression retains its exact canonical
difference, actual private height and original chirp.

Put
\[
 \begin{split}
 R_{\rm common}&=\Re q(z_H^*)+\Re q(b_*)-\pi H
                         -\Re Q_4(s_*;z_*,b_*)+\Re g(z_*),\\
 W_\nu&=-\nu\Re g(z_H^*)-2\nu\pi H,\\
 A&=\log|1-\lambda E_*Z_*|-\log|1-E_*Z_*|,\\
 P_{e,\nu}&=\log|1-\lambda E Z_*|+\log|1+\lambda Z_*|
                              -(2+\nu)\log|1-\lambda Z_*|.
 \end{split}
\tag{12}
\]
Use \(E=E_*\) for the main line and \(E=e^{-2\pi i(.27)}\)
for the left cut. Every modulus passed to a logarithm must be
strictly separated from zero. The four resulting outward bounds are
\[
 \begin{split}
 \mathcal H^{(4)}_{0,\nu}={}&
 \Re\Delta_0+R_{\rm common}+W_\nu+G_b
 +\Gamma_{28/5}(A;\ .3-\Re e_*,\ .4-\Re e_*)\\
 &+\Gamma_{\mu_\nu}(P_{e_*,\nu};\ .22-\Re z_*,\ .45-\Re z_*),\\
 \mathcal H^{(4)}_{L,\nu}={}&
 \Re\Delta_L+R_{\rm common}+W_\nu+G_b
 +\Gamma_{\widehat\mu_\nu}(P_{.27,\nu};\ .22-\Re z_*,\ .45-\Re z_*),\\
 &\mu_1=7,\quad\mu_0=33/5,
 \qquad\widehat\mu_1=69/10,\quad\widehat\mu_0=13/2.
 \end{split}
\tag{13}
\]
All clipped gains use the exact rational one-sided upper rule in
[the half-row evaluation specification](research_mixed_selected_half_row_evaluation_design.md).
Their slopes and displacement endpoints are directed interval
endpoints, and their maximizing displacements are rational arithmetic
on those endpoints. There is no free-target grid or moving optimizer.

The absence of an explicit \(-\Re g(b_*)/2\) in
\(R_{\rm common}\) is the exact cancellation proved in
equations (22)--(24) of the next-four half-row theorem. That
halfweight remains indispensable in (2)--(3) and in the outgoing
curvature \(41/10\). The evaluator must record the outgoing
gradient and gain rather than silently importing the next-three
outgoing formula. Likewise its ordinary reference phase must use
\(-3g(s_*)\), and its selected height must be \(.01\).

Equations (8)--(13), with outward arithmetic and the stated
regularity checks, enclose all four proved scalar upper bounds on
every actual reference in the input box. No assumption about their
signs is used in this evaluation statement.

## 4. One deterministic diagnostic, pending implementation review

Use only the completed next-four central record
[attempt02](../repro/results/research-mixed-next-four-adaptive-budget-attempt02.json),
SHA256
`6e3520360bf93d779c359f39f33e479cf422ef2fa7eadbfe23ce0b5383af7d27`.
Among its accepted leaves, choose one of maximal accepted depth and
then the lexicographically smallest address. This rule, applied
only to saved metadata, selects
\[
 \texttt{001111101111010111},\qquad\text{depth }18,
\tag{14}
\]
whose exact inherited box is
\[
 \Re u\in[115337/512000,57677/256000],\qquad
 \Im u\in[8919/256000,279/8000].
\tag{15}
\]
Reconstruct (15) from the original root rectangle and alternating
real/imaginary dyadic splits, without importing or calling any old
scalar inspection routine. The selection does not claim that this
necessary-superset box contains a realized word reference; it is a
previously accepted reference enclosure with a deterministic choice.

The proposed diagnostic has fixed 160-bit precision, one input box,
one evaluation of all four quantities (13), and no subdivisions,
continuations, alternate boxes, precision escalation or automatic
retry. It reports comparison with both zero and the candidate
\(-1/2000\), but one box cannot establish a uniform source gap.
An unsuccessful sufficient upper bound is not a source counterexample.

The record should retain the inherited leaf and address, exact box,
all reference coordinate/shape enclosures, original action
differences, outgoing gradient and gain, both incoming gradients and
gains, private gradient/gain, and the four total upper enclosures.
Serialize every real directed endpoint as an exact rational in
addition to its readable display. Bind this specification, the
next-four half-row proof, centered-primitive proof, all original map
and branch providers, the completed central record and its
dependencies, and the new diagnostic's own bytes before and after
the evaluation. Require a fresh output path.

This note authorizes no execution. A new diagnostic implementation
must receive proof/code review before any run. A later complete
four-test cover would settle the next-four main/left-cut half-row
pairs only; the other finite-source comparisons would still require
their own proofs.
