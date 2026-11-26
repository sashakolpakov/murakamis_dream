# Branch-preserving evaluation of the six half-row tests

Research specification, 6 November 2026. This records an outward
evaluation procedure for the six scalar bounds in
[the half-row majorant](research_mixed_selected_four_three_half_row_majorant.md).
No scalar test, cover, source sum, root solve or replay is executed
here. In particular this note supplies no sign for those six bounds.

## 1. Original primitives and the reference parameter

Use the same auxiliary rectangle
\[
 u\in[.217,.234]+i[.027,.045],\qquad U=e^{2\pi iu},
 \tag{1}
\]
and the rational maps \(E(U),Z(U),S(U),B(U)\) of
[the coupled-log proof](research_mixed_endpoint_coupled_log_increments.md).
Here the rational function \(S(U)\) is the ordinary exponential,
not the private endpoint action. Recover reference coordinates by
\[
 e_*=\frac{i}{2\pi}\Log E,\quad z_*=\frac{i}{2\pi}\Log Z,\quad
 s_*=\frac{i}{2\pi}\Log S,\quad b_*=\frac{i}{2\pi}\Log B.
 \tag{2}
\]
Keep exactly the necessary coordinate ranges, reduced disks,
pair-sum bounds and next-external \(K_3\cup K_4\) test used in
[the central scalar proof](research_mixed_first_four_next_three_central_gap.md).
The underlying interval map implementation is
[the original scalar driver](../experiments/certify_mixed_endpoint_log_budget.py).
An interval which cannot resolve a logarithm or a denominator must
be retained or subdivided; nonfiniteness is never an exclusion.

The original primitive has the explicit formula
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},
 \qquad
 J(w)=g(w)-\frac{i\pi}{2}w(1-w).
 \tag{3}
\]
This is exactly the g convention in
[the original conditional driver](../experiments/certify_mixed_reduced_disk_conditional_packets.py).
On \(0<\Re w<1\), the exponential in (3) avoids the positive
real axis, and hence the principal dilogarithm cut \([1,\infty)\).
The formula has derivative
\(\Log(1-e^{-2\pi iw})\) and the original zero normalization.
It therefore gives the original continuation throughout that strip.
No separate polylogarithm branch is chosen cell by cell.

Every primitive argument needed below lies in this regular strip:
the original coordinates and sums, \(z_H^*=\Re z_*+iH\),
\(e_*+z_H^*\), \(e_0+z_H^*\), and the half-row arguments
\(v+ih_b,\ v+1/2+ih_b\), where
\[
 H=7/625,\quad v\in[.22,.45],\quad e_0\in\{.27,.49\}.
 \tag{4}
\]
For example the last summed arguments have real part in
\([.72,.95]\); none crosses an integer even when the height
changes sign. Finite interval enclosures must certify the strip
before applying (3); a wide enclosure can instead be subdivided.

Write \(\mathscr S(e)\) for the canonical private action in this
note, to distinguish it from \(S(U)\). At the actual reference,
the auxiliary variable in (1) is already its private critical
coordinate, so
\[
 \mathscr S(e_*)=
 -2J(1/2-u)-3J(u)-J(e_*-u)+i\pi e_*u.
 \tag{5}
\]
This uses no implicit root construction. At either fixed cut,
\[
 \begin{split}
 u_0&=\frac1\pi\arctan
       \frac{i+\sqrt{1-2e^{2\pi i e_0}}}{2},\\
 \mathscr S(e_0)&=-2J(1/2-u_0)-3J(u_0)-J(e_0-u_0)
                                      +i\pi e_0u_0.
 \end{split}
 \tag{6}
\]
These are the fixed canonical branches in
[the endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md).
The square-root argument has real part greater than one at both
cuts. The chosen square root and arctangent give the original
continuation; its retained inequalities
\(0<\Re u_0<1/2\), \(0<\Re(e_0-u_0)<1/2\) can also be
checked outward when enclosing these two constants. Formula (6)
does not propose a root at a varying target.

## 2. Interval optimization without a target grid

All logarithmic ratios and slopes are evaluated from the same
enclosed reference, as in equations (9) and (19) of the half-row
note. The outgoing optimum uses
\[
 p_R=\log\frac{|1-SB|}{|1-B|},\qquad
 \zeta_b=\frac{|B|+|B|^{-1}}2\tanh p_R.
 \tag{7}
\]
For an interval enclosure of \(\zeta_b\), the following equivalent
form is convenient:
\[
 \widehat v=
 \operatorname{clip}_{[.22,.45]}
 \left(\frac{\arccos(\operatorname{clip}_{[-1,1]}\zeta_b)}
                   {2\pi}\right).
 \tag{8}
\]
Both clips are monotone and \(\arccos\) is decreasing. Applying
them to outward endpoints therefore encloses every true optimizer,
including an endpoint optimizer or a cell crossing a clipping
transition. Evaluating
\[
 \Re\{g(\widehat v+1/2+ih_b)-g(\widehat v+ih_b)\}
                         -p_R(\widehat v-\Re b_*)
 \tag{9}
\]
on that enclosure gives a valid upper bound for \(\mathcal O_*\).
An unresolved branch enclosure is subdivided, not discarded.

The remaining clipped quadratic gains also admit an elementary
one-sided outward rule. For \(\mu>0,\ \beta,L\ge0\), put
\[
 \mathcal G_\mu(\beta,L)=
 \begin{cases}
   \beta L-\mu L^2/2,&\beta\ge\mu L,\\
   \beta^2/(2\mu),&\beta\le\mu L.
 \end{cases}
 \tag{10}
\]
This is increasing in both nonnegative arguments. Suppose
\(p\in[p_-,p_+]\), \(l\le0\le r\), and
\(-l\le L_-,\ r\le L_+\). Then
\[
 \Gamma_\mu(p;l,r)\le
 \max\{\mathcal G_\mu(\max(0,-p_-),L_-),
       \mathcal G_\mu(\max(0,p_+),L_+)\}.
 \tag{11}
\]
All endpoint data in (11) can be exact dyadic rationals extracted
from directed interval endpoints; each \(\mu\) is one of the
rational constants in the half-row proof or its strengthening below.
Thus the comparison in (10) and its two values can be formed with
exact rational arithmetic. Alternatively, the already used outward
one-sided gain rule gives the same upper bound, using the
unconstrained gain whenever the clipping comparison is inconclusive.
No floating maximizer or target partition is needed.

The existing [strong private curvature theorem](research_mixed_private_cap_curvature_bound.md)
improves the main private gain before any scalar evaluation. On
the entire required rectangle, \(-\Re\mathscr S''/\pi>68/45\).
Together with \(u_e>3/10\) and \(C\le0\) in the half-row
Hessian decomposition, this gives
\[
 -\nabla^2F_\nu\succ
 \begin{cases}
  \operatorname{diag}(28/5,7),&\nu=1,\\
  \operatorname{diag}(28/5,33/5),&\nu=0,
 \end{cases}
 \qquad
 \pi(68/45+3/10)=163\pi/90>28/5.
 \tag{12}
\]
The same original trial and gradient therefore give a stronger
main-profile upper bound \(\mathcal H^{+}_{0,\nu}\), obtained
by replacing \(\Gamma_1(A;\cdot,\cdot)\) with
\(\Gamma_{28/5}(A;\cdot,\cdot)\) in its equation (20).
All other terms are unchanged. This is a proved upper-bound
improvement, not an assertion of its sign.

For instance the strengthened main private gain takes
\(L_-=e_{*,R}^{\rm upper}-.3\) and
\(L_+=.4-e_{*,R}^{\rm lower}\). The incoming gain takes
\(L_-=a^{\rm upper}-.22\) and
\(L_+=.45-a^{\rm lower}\).
These are containing displacement intervals, not a claim that their
endpoints and the extremal slope occur at the same reference.

## 3. Cancellations to preserve in the implementation

For the main profile use equation (21) of the half-row note
literally: it cancels \(\mathscr S(e_*)\) before interval evaluation.
For a real cut, form the relative cap action
\[
 \begin{split}
 \Delta_{e_0}={}&\mathscr S(e_0)-\mathscr S(e_*)\\
 &+J(e_0+z_H^*)-J(e_*+z_*)-J(z_H^*)+J(z_*)\\
 &-i\pi(e_0z_H^*-e_*z_*)-g(e_0)+g(e_*).
 \end{split}
 \tag{13}
\]
This is exactly \(\Psi(e_0,z_H^*)-\Psi(e_*,z_*)\).
The first line of the cut majorant can therefore be evaluated as
\[
 \Re\Delta_{e_0}+\Re q(z_H^*)-\pi H+W_\nu(a)
       +\mathcal O_*-\Re Q(s_*;z_*,b_*)+\Re g(z_*).
 \tag{14}
\]
The common outgoing tangent and original chirps are present in
(7), (9), (13)--(14). Neither the action nor the calibrated slope
is replaced by an independent range before forming these formulas.

Consequently a prospective scalar checker needs only the original
two-real-dimensional reference subdivision and the elementary,
polylogarithmic and clipped evaluations (2)--(14). It can record
all six outward upper bounds. The new
[pointwise right-cut comparison](research_mixed_selected_cap_right_rows.md)
also proves \(A_R<A_0-1/1250\). Consequently only the four
main/left-cut half-row tests, both Fourier alternatives included,
need independent acceptance: the two right-cut profiles then inherit
the accepted main-profile gap plus \(1/1250\). This reduction does
not require the right-cut scalar majorants themselves to be negative.
The necessary-reference
exclusions are separate from such acceptance. Pending cells remain
pending, and a failed upper test is not an original-source
counterexample.

All numerical constants and transcendental enclosures must be
created after setting the requested precision; copying a helper
must not silently retain a module-level low-precision value of
\(\pi\). A future checker should bind the half-row proof, this
specification, the original map/branch sources and its own bytes.
This specification does not authorize or report an execution.
