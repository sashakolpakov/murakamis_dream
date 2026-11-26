# Enclosing the original prepared-cap action from its gradient residual

Research deduction, 7 November 2026. The prepared three-four critical
point now exists by the completed original boundary update. Its action
can therefore be enclosed without another root-existence test: the
existing strong-monotonicity estimate certifies a proposed center, and
a whole-domain Hessian bound makes the action error quadratic in its
certified radius. This note fixes the exact action, original branches
and enclosure arithmetic. It does not evaluate a proposal, residual,
action, physical face or alias.

## 1. The established root and the unreduced action

Use [the completed Fourier-boundary existence theorem](research_mixed_fourier_boundary_critical_existence.md).
Its sole inclusion record is
[research-mixed-fourier-boundary-update.json](../repro/results/research-mixed-fourier-boundary-update.json),
SHA-256
`5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514`.
For the word \(34\), it establishes a unique original-log zero
\(x_*=(u_*,s_*,t_*,p_*,q_*)\) in the convex product
\[
\begin{split}
 \mathcal D&=U\times E\times Q^3,\\
 U&=[.21,.25]+i[.01,.10],\qquad
 E=[.33,.47]+i[-.09,.08],\\
 Q&=[.23,.45]+i[-.12,.12].
\end{split}
 \tag{1}
\]
The same theorem proves, on a neighborhood of this entire product,
\[
       -\Re\widehat F''\succ\mu I_5,
                     \qquad \mu=6\pi/49.
 \tag{2}
\]
All derivatives here and below are in the order \((u,s,t,p,q)\).

Keep the original normalized primitives
\(J'(z)=\Log(2\sin\pi z)\), \(J(0)=J(1/2)=0\),
and \(g(z)=J(z)+i\pi(z-z^2)/2\). At complete ordinary
color the exact unreduced action is
\[
\begin{split}
 \widehat F(x;K)={}&-2J(1/2-u)-3J(u)-J(s-u)
           +i\pi su-\frac{i\pi}{2}(s-s^2)\\
 &+g(s+t)+g(t+p)+g(p+q)-2g(t)-3g(p)-g(q)\\
 &+2\pi itp+\ell_q(K),\\
 \ell_q(K)={}&(q-1/2)\Log K-
       \frac{\operatorname{Li}_2(Ke^{-2\pi iq})-
                         \operatorname{Li}_2(K)}{2\pi i}.
\end{split}
 \tag{3}
\]
Here
\[
 K=(1+2a-4a^2)^{-1}=e^{2\pi ix_0},\qquad
                       \Log K=2\pi ix_0,
 \tag{4}
\]
with the same isolated quartic root and logarithmic branch as
[the original reference packet](research_three_vertex_mixed_reference_packet.md).
The entire certified square for \(a\), of radius \(10^{-26}\),
is retained whenever (3)--(4) are evaluated outward. Its center
is not the exact root.

Equation (3) is equation (1) of
[the prepared critical-curve theorem](research_mixed_prepared_three_four_cap_critical_curve.md),
with the outgoing incidence written in \(K\). Its endpoint
constant and chirp are fixed by
[the original endpoint action calibration](research_mixed_endpoint_action_calibration.md),
Theorem 1. At the established zero, \(u_*=u_c(s_*)\), so
\[
 \widehat F(x_*;K)
       =\mathcal F_{\mathrm{cap}}(s_*,t_*,p_*,q_*;x_0,-2)
       =\Phi_{\mathrm{cap}}(x_0,-2).
 \tag{5}
\]
This is equality of the original complex actions, including their
additive constants. The five-variable representation is used for
residual localization and value enclosure; it is not a new
five-index finite sum. The prepared source still has its original
four-index row and local power \(\kappa^3N^{-1}\).

## 2. An exact primitive formula usable at a nonstationary center

Every argument in the following table belongs to the original regular
strip on a neighborhood of \(\mathcal D\):
\[
 \begin{array}{c|c}
 \text{argument}&\text{real interval}\\\hline
 1/2-u&[.25,.29]\\
 u&[.21,.25]\\
 s-u&[.08,.26]\\
 s+t&[.56,.92]\\
 t+p,\ p+q&[.46,.90]\\
 t,\ p,\ q&[.23,.45].
 \end{array}
 \tag{6}
\]
The original primitive has the exact expression
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
                       \qquad 0<\Re z<1,
 \tag{7}
\]
with the principal dilogarithm continued off \([1,\infty)\).
This was proved, with its constant, in Section 4 of
[the enlarged paired rectangle](research_mixed_contracted_pair_enlarged_rectangle.md).
The exponential of a point in this open strip never meets that cut.
The formula differentiates to the original
\(g'(z)=\Log(1-e^{-2\pi iz})\), and its limit at the
positive real zero is zero.

Substituting \(J(z)=g(z)-i\pi(z-z^2)/2\) in just the
endpoint part of (3) gives the exact identity, before stationarity,
\[
\begin{split}
 \widehat F(x;K)={}&-2g(1/2-u)-3g(u)-g(s-u)
 +g(s+t)+g(t+p)+g(p+q)\\
 &-2g(t)-3g(p)-g(q)\\
 &+i\pi\{1/4+u+2su-3u^2+2tp\}+\ell_q(K).
\end{split}
 \tag{8}
\]
In particular the constant \(i\pi/4\) is required. It
cancels \(-2g(1/2)=-i\pi/4\) in the limiting endpoint
normalization; deleting it would change the original complex action.
No stationary equation was used to obtain (8), so it is valid
at any proposed center in (1).

For the incidence, the original bounds imply
\(9/50<\Re x_0<37/200\). Hence on \(Q\)
the number \(Ke^{-2\pi iq}\) lies strictly in the lower
half-plane. Its logarithm and dilogarithm stay on the original
branches, even at points of (1) where its modulus exceeds one.
This is an action-domain assertion. It does not extend the finite
root-Pochhammer interpolation beyond its separately proved domain;
the actual root already lies in the smaller source rectangle.

For completeness, the full original gradient used to certify a
center is
\[
\begin{split}
 f_u={}&2\Log\cos\pi u+\Log\sin\pi(s-u)
                         -3\Log\sin\pi u+i\pi s,\\
 f_s={}&g'(s+t)-g'(s-u)+2\pi iu,\\
 f_t={}&g'(s+t)+g'(t+p)-2g'(t)+2\pi ip,\\
 f_p={}&g'(t+p)+g'(p+q)-3g'(p)+2\pi it,\\
 f_q={}&g'(p+q)-g'(q)-\Log(1-Ke^{-2\pi iq})+\Log K.
\end{split}
 \tag{9}
\]
All components are unscaled. The sine and cosine logarithms on
the first line have positive real parts in their arguments on
(1); their three \(\log 2\) constants cancel. Equations
(8) and (9) describe the same function and its exact gradient,
not only its value on the stationary set.

## 3. A concrete whole-domain Hessian norm

**Lemma 1.** At the original fixed \(K\), throughout
\(\mathcal D\),
\[
                         \|\widehat F''\|_2<120.
 \tag{10}
\]

*Proof.* If a real coordinate stays at distance at least \(.08\)
from the integer poles, the cotangent identity gives
\[
 |\cot\pi(x+iy)|^2
 =\frac{\cos^2\pi x+\sinh^2\pi y}
        {\sin^2\pi x+\sinh^2\pi y}
 \le\max\{\cot^2\pi x,1\}<16.
 \tag{11}
\]
Indeed \(\tan(.08\pi)>.08\pi>1/4\). The same bound
applies to \(\tan\pi u=\cot\pi(1/2-u)\).
Thus every \(J''\) appearing in the Hessian has modulus
less than \(4\pi\), and every \(g''=J''-i\pi\)
has modulus less than \(5\pi\).

Write \(Ke^{-2\pi iq}=r e^{-i\theta}\), \(r>0\),
\(\theta=2\pi(\Re q-\Re x_0)\). The original bounds
give
\[
                 7/25<\theta<2\pi/3,\qquad
                 \sin\theta>1/4.
 \tag{12}
\]
For the lower angle use \(\Re q-\Re x_0>9/200\)
and \(\pi>28/9\); the upper follows from
\(\Re q-\Re x_0<27/100\). The sine comparison follows
from concavity on \([7/25,2\pi/3]\), its endpoint values,
and \(\sin(7/25)>7/25-(7/25)^3/6>1/4\).
The identity
\[
 |1-r e^{-i\theta}|^2-r^2\sin^2\theta
                         =(1-r\cos\theta)^2\ge0
\]
therefore gives
\[
 \left|\ell_{q,qq}\right|
 =2\pi\left|\frac{Ke^{-2\pi iq}}{1-Ke^{-2\pi iq}}\right|
                         <8\pi.
 \tag{13}
\]
No modulus-less-than-one assumption is used in this estimate.

The Hessian is tridiagonal in \((u,s,t,p,q)\). Its nonzero
entries, with the lower triangle fixed by symmetry, are
\[
\begin{split}
 H_{uu}&=-2J''(1/2-u)-3J''(u)-J''(s-u),\\
 H_{us}&=J''(s-u)+i\pi,\\
 H_{ss}&=-J''(s-u)+i\pi+g''(s+t),\qquad H_{st}=g''(s+t),\\
 H_{tt}&=g''(s+t)+g''(t+p)-2g''(t),\qquad
 H_{tp}=g''(t+p)+2\pi i,\\
 H_{pp}&=g''(t+p)+g''(p+q)-3g''(p),\qquad H_{pq}=g''(p+q),\\
 H_{qq}&=g''(p+q)-g''(q)+\ell_{q,qq}.
\end{split}
 \tag{14}
\]
The corresponding absolute row sums are strictly less than
\[
                         (29,20,32,37,23)\pi.
 \tag{15}
\]
Complex symmetry makes the maximum absolute column sum equal
to the maximum absolute row sum. Hence
\(\|H\|_2\le\sqrt{\|H\|_1\|H\|_\infty}<37\pi<120\).
\(\square\)

## 4. Residual localization and the quadratic action error

Let \(x^0\) be any exact Gaussian-rational point of
\(\mathcal D\). Its proposed origin has no proof role.
The argument of Theorem 1 in
[original prefix residual localization](research_mixed_prefix_residual_localization.md)
applies directly using (2) and the already established existence:
\[
                  \|x^0-x_*\|_2
                    \le\frac{\|f(x^0;K)\|_2}{\mu}.
 \tag{16}
\]
Indeed integrate the complex symmetric Hessian along the segment
from \(x_*\) to \(x^0\), pair with the conjugate displacement,
and use its Hermitian part \(\Re H\). This is the same
strong-monotonicity proof as the cited theorem, not a separate
Banach test or new existence argument. The whole segment stays
in the convex product (1).

**Theorem 2.** If a rigorous bound certifies
\(\|f(x^0;K)\|_2\le\mu r\), then
\[
 \left|\Phi_{\mathrm{cap}}(x_0,-2)-\widehat F(x^0;K)\right|
                            <60r^2
 \tag{17}
\]
unless \(x^0=x_*\), in which case the difference is zero.
In particular the non-strict bound \(60r^2\) always applies.

*Proof.* Put \(d=x^0-x_*\). Taylor's formula from the
actual root, whose full original gradient is zero, gives
\[
 \widehat F(x^0;K)-\widehat F(x_*;K)
   =\int_0^1(1-\tau)\,d^{\mathsf T}
           H(x_*+\tau d;K)d\,d\tau.
 \tag{18}
\]
This is a complex bilinear product without conjugation. Its
modulus is at most \(\|H\|_2\|d\|_2^2\).
Equations (10), (16) and \(\int_0^1(1-\tau)d\tau=1/2\)
prove (17), and (5) identifies its action. Stationarity is used
at \(x_*\), not falsely imposed at the stored center.
\(\square\)

The error is two-sided in both the real and imaginary action.
Accretivity along complex displacements does not license replacing
(17) by a one-sided real concavity inequality for the value at
an arbitrary complex center.

## 5. Exact enclosure arithmetic for a future fixed proposal

Retain the complete original algebraic square in (4) throughout
the outward residual and value evaluations. Suppose the ten real
and imaginary residual components have rational interval endpoints
\([l_j,u_j]\). Define
\[
 R^2=\sum_{j=1}^{10}\max(|l_j|,|u_j|)^2,
 \qquad \mu_-:=\frac{471}{1225}<\frac{6\pi}{49}.
 \tag{19}
\]
The last inequality uses \(\pi>157/50\). An exact check
\(R^2<\mu_-^2r^2\) certifies (16) with radius \(r\).
For example, \(r=10^{-16}\) is a possible prescribed radius
for a future fixed protocol; no claim that this test passes is
made here. A radius below the uncertainty of the fixed algebraic
input must not be assumed merely from the proposal's precision.

If an outward evaluation of the exact off-shell formula (8)
at that same \(x^0\), with the entire original input square,
gives
\[
 \widehat F(x^0;K)\in[A_-,A_+]+i[B_-,B_+],
\]
then the original critical action belongs to
\[
 [A_--60r^2,A_++60r^2]
           +i[B_--60r^2,B_++60r^2].
 \tag{20}
\]
In particular a rigorous common action lower bound for physical
and alias comparisons is
\[
                     M_-:=A_--60r^2.
 \tag{21}
\]
Every rounding enclosure in (8), including \(\pi\),
\(K\), \(\Log K\), and each primitive value, is retained
in \([A_-,A_+]\) and \([B_-,B_+]\). These intervals
cannot be replaced by favorable midpoints. The quadratic coordinate
error does not remove the original algebraic input uncertainty.

The future record may report the exact rational proposal, its
domain checks, all residual intervals, (19), the prescribed radius,
the original value interval, the error radius \(60r^2\),
(20), and \(M_-\). Its source and analytic input bindings
must identify the same original quartic root, boundary-update
existence result, endpoint calibration and phase. A deterministic
fixed Newton procedure may propose \(x^0\); neither convergence
of that procedure nor a computed inverse is a certificate. Failure
of its domain, residual, branch or value enclosure leaves the
action comparison inconclusive.

This proof authorizes no proposal or evaluation run. It supplies
the exact acceptance arithmetic for a separately frozen and reviewed
protocol. A successful action enclosure would still need to be
compared with the new physical faces, far ceiling and alias maxima
in [the prepared full-source criterion](research_mixed_prepared_cap_full_source_criterion.md).
It does not supply those signs or an outgoing whole-period bound.
