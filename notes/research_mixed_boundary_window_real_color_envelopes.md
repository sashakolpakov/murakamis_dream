# Real-color source envelopes through boundary-window height tapers

Research deduction, 6 November 2026. The literal first-cap envelope
extends to every intermediate height used by the mixed contour, as
long as its outgoing real coordinate remains in the central interval.
The regular currents and compact physical tails retain strict angular
decay. The true index-end sectors retain a separate constant ceiling.
This supplies a common real-color input for boundary windows, without
requiring a new color comparison for each selection pattern. It does
not prove the missing calibrated boundary sign or cover outer real
targets outside that interval.

## 1. The literal cap and the full height ranges

Put \(P=[.22,.45]\), \(r=e^{-2\pi i/N}\),
\(P_i=(r;r)_i\), and \(p_i(X)=(rX;r)_i\). Keep exactly
\[
 U_{\alpha,N}(w,X)=\sum_{i=0}^{N-1}
       \frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\alpha}},
 \qquad \alpha\in\{0,1\},\qquad X=e^{-2\pi iz}.
 \tag{1}
\]
The coefficient, scalar and branches are those of the original
[cap contour theorem](research_mixed_cap_outer_contour_reduction.md).
In particular, its retained interpolant is
\[
 D_N(e)^{-1}C_N(e,w)
 \frac{\widehat P_N(N(e+z))}
      {\widehat P_N(Nz)\widehat P_N(Ne)^\alpha}.
 \tag{2}
\]
The whole coherent coefficient \(C_N\) is retained before the
outer residue decomposition. The constant residue coefficient is
\(+N\).

Let
\[
 E_c=[.27,.49]+i[-.055,.04],\qquad
 \begin{cases}
 z=y+ih,\quad y\in P,\quad -.072\le h\le .021,
                                      &\alpha=0,\\
 z=y+ih,\quad y\in P,\quad -.108\le h\le .014,
                                      &\alpha=1.
 \end{cases}
 \tag{3}
\]
No requirement identifies \(h\) with a critical height or one of
the previously chosen selected heights. The intervals include all
convex combinations of the respective original attached heights,
zero, and the allowed selected height \(7/500\) in type four.

Use the original complete-color phase
\[
 \Psi_\alpha(e,z)
   =S(e)+J(e+z)-J(z)-i\pi ez-\alpha g(e).
 \tag{4}
\]
Choose a private main height \(h_e\in(-.055,.04)\); an original
reference height is allowed, but no new stationary point is required.
Define the five current bounds
\[
 \begin{split}
 A_{\alpha,0}(z)&=\max_{.27\le x\le .49}
                       \Re\Psi_\alpha(x+ih_e,z),\\
 A_{\alpha,L}(z)&=\Re\Psi_\alpha(.27,z),\qquad
 A_{\alpha,R}(z)=\Re\Psi_\alpha(.49,z),\\
 A_{\alpha,-}(z)&=\max_{.27\le x\le .49}
                       \Re\Psi_\alpha(x-.055i,z)-.11\pi,\\
 A_{\alpha,+}(z)&=\max_{.27\le x\le .49}
                       \Re\Psi_\alpha(x+.04i,z)-.08\pi,\\
 A_\alpha(z;h_e)&=\max(A_{\alpha,0},A_{\alpha,L},
                       A_{\alpha,R},A_{\alpha,-},A_{\alpha,+}).
 \end{split}
 \tag{5}
\]
The two real cuts have height zero. Alias penalties and chirps have
their original signs.

**Theorem 1.** There is \(c>0\) such that, for every
\(\eta>0\), the original finite cap obeys
\[
 \begin{split}
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi iz})|
 \le C_\eta N^{a_\eta}
 \left[
   e^{N\{A_\alpha(z;h_e)-c(1-\cos\theta)+\eta\}}
    +e^{N(3/4+\eta)}
 \right],
 \qquad -\pi\le\theta\le\pi .
 \end{split}
 \tag{6}
\]
This holds uniformly on (3), for both level parities and for
private heights in any fixed compact subinterval of
\((-.055,.04)\). Each fixed ordinary-color derivative has the
same two exponents with a different polynomial prefactor.

*Regular currents.* The original coefficient theorem
[endpoint real-color decay](research_mixed_endpoint_real_color_decay.md),
Theorem 1, gives
\[
 |C_N(e,-2\cos\theta)|
   \le C N^a e^{N\{\Re S(e)-c_E(1-\cos\theta)\}},
                       \qquad e\in E_c,\quad c_E>0.
 \tag{7}
\]
Every other factor in (2) is color independent. All primitive
arguments stay regular on (3): in particular
\(.49\le\Re(e+z)\le .94\). Insert (7) into each exact
current before taking its upper bound. Lemma 1 of the
[full cap phase theorem](research_mixed_first_cap_plateau_phase.md)
proves private vertical convexity on the larger product
\(E_c\times(P+i[-.108,.021])\). Hence zero-mode joins are
bounded by their real-cut and main-height endpoints, and each
half of a vertical alias is bounded by its real-cut or horizontal
alias endpoint. This gives (5), with the common angular loss in
(7), for every retained current. No far-color saddle or far-color
Hessian has been used.

*Compact physical tails.* On the original physical indices in
\([.01,.99]\), the physical-index part of the same coefficient
theorem has a uniform positive angular constant \(c_I\).
After including the original factorials, its upper phase is
\[
 R_\alpha(t,z)=\Re S(t)+
       \int_0^t\log|1-e^{2\pi h-2\pi i(y+x)}|\,dx
                         -\alpha J(t).
 \tag{8}
\]
This bound retains \(-c_I(1-\cos\theta)\). For any sign of
\(h\), the exact reflection of the integral in (8) is
\[
 2\pi h_+t+
    \int_0^t\log|1-e^{-2\pi|h|-2\pi i(y+x)}|\,dx .
 \tag{9}
\]
The nonnegative \(2\pi h_+t\) term is not canceled or discarded.

For type three the complete tail monotonicity proof in Section 5
of the full cap phase theorem applies to the entire first interval
in (3), not just to one reference height. For type four its lower
tail proof also applies throughout (3): the smoothed radius
exceeds \(1/2\), and for \(0<t\le .27\),
\(.22\le y+t\le .72\) gives \(\cos(2\pi(y+t))<1/5\).
Thus the numerator logarithm in (9) is positive. The existing
\(\lambda'(.27)>27/50\), \(\lambda''<0\) and
\(J'(.27)<41/100\), where \(\lambda=\Re S\), imply
\(R_1'>13/100\) on the compact lower tail.

On the upper tail, at every height in (3),
\[
 |1-e^{2\pi h-2\pi i(y+t)}|
       \le 1+e^{.028\pi}<9/4.
 \tag{10}
\]
For instance \(.028\pi<.088\) and
\(e^x\le(1-x)^{-1}\) give this strict bound. The unchanged
endpoint inequality \(\lambda'-J'\le-\log4\) for
\(t\ge1/2\) now gives \(R_1'<\log(9/16)<0\).
On \([.49,.5]\), use
\(\lambda'<-3/5\), \(J'>3/5\), and
\(\log(9/4)<6/5\), giving the same strict direction.
This includes positive and intermediate selected heights as well
as the negative original heights. At numerator zeros, integrate
on the adjoining intervals using the continuous integrated logarithm.
The compact tails therefore reduce to the real anchors in (5),
with their positive angular loss intact.

*The actual index ends.* For \(i/N\le .01\), physical support
puts every Newton index below one half; the exact inequality
\(V_\theta\le V_0\) preserves the old rate ceiling \(1/4\).
For \(i/N\ge .99\), use \(V_\theta\le V_0\) only below
one half and \(V_\theta\le0\) above it. These are the
[zero-safe real-color Newton bounds](research_mixed_newton_color_tubes.md),
not a comparison to a possibly zero complete-color value. They
give the unchanged endpoint entropy ceiling \(3/5\).
The literal identity
\[
 p_i(X)=\frac{1-X^N}{\prod_{j=i+1}^N(1-r^jX)}
 \tag{11}
\]
and the original denominator-angle bound give
\[
 |p_i(X)|\le2e^{2\pi Nh_+}(20/19)^{N-i},\qquad
 \frac35+2\pi h_++\frac1{100}\log(40/19)<\frac34
 \tag{12}
\]
throughout (3), since \(h_+\le.021\). The extra reciprocal
factorial in type four has nonpositive rate in this upper sector.
These two extreme sectors require no angular-loss assertion.
The exact finite product estimates are uniform through zeros.

Combining the currents, compact tails and the two extreme sectors,
with one aggregate tolerance, proves (6), taking
\(c\le\min(c_E,c_I)\). The same coefficient/physical estimates
hold for fixed ordinary derivatives; the color-independent
interpolation, currents and products preserve them. Equivalently,
the original degree bound and Cauchy at ordinary-color radius
\(N^{-2}\) give only polynomial cost, including \(w=\pm2\).
\(\square\)

## 2. A quantitative angular consequence, with its required surplus

If on a given compact set of targets and private heights
\[
                 A_\alpha(z;h_e)\ge\frac34+\delta,
                       \qquad \delta>0,
 \tag{13}
\]
then (6) implies the single-envelope bound
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi iz})|
 \le C_\eta N^{a_\eta}
 e^{N\{A_\alpha(z;h_e)-c'(1-\cos\theta)+\eta\}},
 \qquad c'=\min(c,\delta/2)>0 .
 \tag{14}
\]
Indeed \(0\le1-\cos\theta\le2\), so the second exponent
in (6) is at most the one in (14). No comparison of two
canceled cap moduli is involved.

For the actual selected-first families at heights \(7/625\)
or \(1/100\), the original
[selected-cap reduction](research_mixed_selected_four_three_finite_reduction.md)
and its
[wider original-height proof](research_mixed_selected_four_three_last_rows.md),
Section 5, give \(A_{1,0}>199/250\). Thus (13) holds with
\(\delta=23/500\). The already completed first-only and
first-two-selected profile inequalities can consequently retain
the additional loss \(c'(1-\cos\theta_L)\), with
\(c'=\min(c,23/1000)\), in their raw bounds. Their original
normalizations, complex marginals and independent target intervals
are unchanged. This strengthens the period-only statement of the
[selected-prefix real-color lift](research_mixed_selected_first_prefix_real_color_lift.md).
No surplus (13) is asserted for every target in (3).

## 3. Consequence for arbitrary surrounding boundary factors

The theorem is an inequality for the literal polynomial (1);
it does not depend on the width or selection pattern of an attached
boundary window. Multiply it by any of the original color-independent
conditional factors and complete retained Fourier weights, allocating
each modulus halfweight only after this step. Whenever the cap
target lies in (3), the same upper envelope applies pointwise even
if its height depends on other real coordinates through a hybrid
cutoff. No derivative of that height is used in the scalar bound.
If an outer integration uses such a graph, its original bounded
Jacobian and its exact homology justification are still required.

At the other end, the existing
[terminal real-color envelope](research_mixed_terminal_profile_real_color_lift.md)
already supplies the unchanged 27-profile bound for every incoming
target in \(P+i[-.12,.12]\). Hence after legitimate exact
terminal contraction, boundary-window comparisons whose two
boundary targets remain in these respective tubes can be formulated
once using the complete-color current phases and the explicit
physical ceilings. Their color-uniformity does not require separate
casework for each internal selection or height-taper state. In
particular the occupation costs, closing tangents and relative
pinning terms in the
[finite boundary-window reduction](research_mixed_open_finite_boundary_windows.md)
are color independent and need no alteration.

This is not a reduction of those windows to their plateau targets:
their target heights and internal configurations remain exactly
as given. Nor does it provide the needed calibrated sign. Full
outer real targets outside \(P\), the uncontracted terminal
factor at an arbitrary complex private argument, and any
whole-source comparison using them require their own source inputs.
No full open-source, short-filling or nonzero-amplitude conclusion
is inferred.

## 4. Why an arbitrary complete-color estimate cannot be lifted

The restriction to these proved source envelopes is essential.
In the original Newton basis
\[
 e_l(w)=S_l^{-2}\prod_{j<l}(c_j-w),\qquad
                c_j=2\cos((2j+1)\pi/N),
 \tag{15}
\]
take \(N=2L+1\). Then \(c_L=-2\), so
\(e_{L+1}(-2)=0\), while \(e_{L+1}(w)\ne0\) at
every real \(w\) avoiding its finitely many original nodes.
These upper-half rows occur in the exact physical source before
any eligible tail estimate. Thus even a rowwise bound by a finite
multiple of its complete-color modulus is false. Cancellation
in a complete cap or boundary-window sum cannot repair that as
a general implication.

The successful estimates above instead retain the entire coherent
coefficient on its certified complex rectangle, and use the weaker
upper-half physical bound \(V_\theta\le0\). The remaining
complete-source question is therefore a calibrated bound for these
actual envelopes over the omitted boundary configurations, not a
new case-by-case analysis of the real ordinary color on the tubes
already covered here.
