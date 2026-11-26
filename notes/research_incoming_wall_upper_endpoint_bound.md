# An endpoint bound at the incoming numerator wall

Private written proof, 11 November 2026. A weighted upper connection
at a numerator wall need not decrease throughout its height interval.
For the phases with two or three denominator factorials, it is
nevertheless bounded by its two endpoints. This removes the need
for a positive lower bound on its height derivative throughout
the connection.

## 1. An elementary argument inequality

For \(0<\theta<1/2\) and \(\rho\ge1\), define
\[
 A_\theta(\rho)=\arg(1-\rho e^{-2\pi i\theta})\in(0,\pi).
 \tag{1}
\]
At the endpoints use \(A_{1/2}(\rho)=0\) and
\(A_0(\rho)=\pi\) for \(\rho>1\). The latter is the limit
as \(\theta\downarrow0\) at fixed \(\rho>1\).
For \(0<\theta<1/2\),
\[
 \frac{d A_\theta}{d\rho}
     =\frac{\sin(2\pi\theta)}
                {1+\rho^2-2\rho\cos(2\pi\theta)}>0,\qquad
 A_\theta(1)=\pi(1/2-\theta).
 \tag{2}
\]
Both formulas follow by differentiating the argument of the
nonzero complex number in (1).

Fix \(0\le d<t\le1/2\), and let \(m\) be either two or three.
Put
\[
 I_m(\rho)=\pi(1-2t)+A_d(\rho)-mA_t(\rho),\qquad \rho>1.
 \tag{3}
\]

**Lemma.** If a real function \(F\) is continuous on \([0,H]\),
differentiable on \((0,H)\), and
\[
                 F'(\eta)=-I_m(e^{2\pi\eta}),
 \tag{4}
\]
then
\[
                     F(\eta)\le\max\{F(0),F(H)\}
                              \quad(0\le\eta\le H).
 \tag{5}
\]
For \(m=2\), \(F\) is nonincreasing.

First suppose \(0<d<t<1/2\). The quotient of the two
derivatives in (2) is
\[
 \frac{A_d'(\rho)}{A_t'(\rho)}
 =\frac{\sin(2\pi d)}{\sin(2\pi t)}
       \frac{x-\cos(2\pi t)}{x-\cos(2\pi d)},\qquad
 x=\frac{\rho+\rho^{-1}}2 .
 \tag{6}
\]
As \(\rho\) increases from one, \(x\) increases. The last
quotient decreases in \(x\), because its derivative has the
sign of \(\cos(2\pi t)-\cos(2\pi d)<0\).
It follows that
\[
       I_m'(\rho)=A_t'(\rho)
                         \left(\frac{A_d'(\rho)}{A_t'(\rho)}-m\right)
 \tag{7}
\]
can change sign at most once, from positive to negative.
Thus \(I_m\) first increases and then decreases, allowing either
part to be empty. Its initial value is positive:
\[
 I_3(1)=\pi(t-d)>0,\qquad I_2(1)=\pi(1/2-d)>0.
 \tag{8}
\]
Consequently it has at most one zero for \(\rho>1\), and any
sign change there is from positive to negative. Equation (4)
then makes \(F\) first decrease and then increase. Its maximum
is at an endpoint, proving (5).

For \(m=2\), the limit at infinity is also positive:
\[
       \lim_{\rho\to\infty}I_2(\rho)=2\pi(t-d)>0.
 \tag{9}
\]
An increasing-then-decreasing function with both endpoint limits
positive stays positive. This proves the additional assertion.

If \(d=0<t<1/2\), (3) becomes
\[
                 I_m(\rho)=\pi(2-2t)-mA_t(\rho).
 \tag{10}
\]
It decreases in \(\rho\). Its limit at \(\rho\downarrow1\)
is \(\pi(1/2+t)\) for \(m=3\), and \(\pi\) for \(m=2\).
The preceding sign-change argument still applies. For \(m=2\)
its limit at infinity is \(2\pi t>0\).
Finally, if \(t=1/2\), then \(I_m=A_d>0\).
These cases prove the lemma on its entire stated domain.
No derivative at \(\eta=0\) is required.

## 2. Application to the upper weighted connection

Use the original conditional phase
\[
 Q_m(s;a,q)=g(a+s)+g(q+s)-m g(s)-g(a)-g(q)+2\pi ias,
                  \qquad g'(w)=\operatorname{Log}(1-e^{-2\pi iw}).
 \tag{11}
\]
Here \(a,q\in[1/2,1)\), with the original continuations.
At the incoming numerator wall put
\[
                    t=1-a,\qquad s=t+i\eta .
 \tag{12}
\]
We consider the continuous limiting real rate obtained by
approaching that wall from the pre-incoming side.

If \(q<a\), the outgoing numerator is still before its wall.
For positive \(\eta\), the incoming cotangent has zero real
part, the outgoing cotangent has negative real part, and the
own cotangent has nonnegative real part. Hence
\[
 \Re (Q_m)_{ss}
 =\pi\Re\{\cot\pi(a+s)+\cot\pi(q+s)-m\cot\pi s\}\le0 .
 \tag{13}
\]
The function \(\eta\mapsto\Re Q_m(t+i\eta;a,q)-2\pi\eta\)
is convex: its second derivative is \(-\Re(Q_m)_{ss}\).
It is therefore bounded by its two endpoint values.

Suppose instead that \(q\ge a\). Set \(d=q-a\); then
\(0\le d<t\), since \(q<1\).
The incoming logarithm at its wall has argument \(-\pi\).
The outgoing numerator has passed one period. Its exact factor
\[
                    \Pi_N(w+1)=(1-e^{-2\pi iNw})\Pi_N(w)
 \tag{14}
\]
has upper exponential rate \(2\pi\eta\), which cancels the
upper sampling penalty. It is retained, not divided out.
After this cancellation the imaginary derivative governing the
weighted rate is
\[
          -\pi+A_d(e^{2\pi\eta})-mA_t(e^{2\pi\eta})+2\pi a
          =I_m(e^{2\pi\eta}).
 \tag{15}
\]
Equivalently, before cancellation the original imaginary
derivative is \(I_m-2\pi\); subtracting the sampling penalty
gives the height derivative \(-I_m\).
This records the sign of the period contribution explicitly.

When \(q=a\), the two numerator walls coincide. The prewall
outgoing argument is \(-\pi\); replacing it by \(A_0=\pi\)
and retaining the period correction \(-2\pi\) gives the same
derivative. Thus (15) also gives the correct one-sided rate
at coincident walls.

The lemma now proves the endpoint bound for every finite
upper height \(H\), throughout \(q\ge a\), for both \(m=2,3\).
Together with (13), it covers all real \(a,q\in[1/2,1)\).
For a compact parameter family bounded away from \(a=1,q=1\),
uniform continuity of the integrated logarithmic rates permits
nearby fixed cuts before the wall with an arbitrarily small
fixed rate allowance. The bound concerns rates; a finite
factorial estimate is still needed to use that allowance
uniformly in \(N\).

## 3. Scope

This endpoint principle replaces the sufficient pointwise
condition \(I_3>0\) used in Section 6 of
research_mixed_443_real_first_fixed_half_contour.md.
The pointwise condition was proved there only on its smaller
parameter rectangle. The present argument allows \(I_3\)
to become negative, because the resulting change gives a
minimum of the weighted rate, not a maximum.

This note does not bound the endpoints themselves, the upper
horizontal current, other connections, or the physical rows.
It therefore supplies no complete conditional-sum estimate
and no additional knot-volume theorem.

The elementary lemma is proved without imported mathematical
results. The application uses the original phase and exact
period-factor conventions in Sections 6--7 of
research_mixed_443_real_first_fixed_half_contour.md,
version e65a5c9d69db49c633b06b02c070e9fa005566ad07ec02dd91d7bb182618f950.
The author has read the complete final proof and these directly
used identities. Independent complete proof and source review
is required before adoption. No numerical evaluation, test,
import, or compilation is used.
