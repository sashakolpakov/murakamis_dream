# A coupled height reduction with both neighboring incidences

Research deduction, 7 November 2026. When the moving neighbor has
own type four, the entire regular first-boundary derivative, including
both incidences of its changing height, is minimized at zero height
of the first ordinary index. This holds for either first-cap type.
For a following nonpositive index height, the next index also
reduces to its lower real endpoint and one prescribed height endpoint.

These are derivative reductions, not a sign theorem. In particular
the already paid uniform first-coordinate slopes alone do not pay
the possible negative neighboring term. No finite-source estimate
for a new following target domain is inferred.

## 1. The actual two-incidence expression

Use the original allocations and moving-height conventions of
[the complete adjoining envelope](research_mixed_first_attached_complete_contour_envelope.md)
and Section 4 of
[the moving-height reduction](research_mixed_first_attached_moving_height_reduction.md).
Let the first cap have type \(3+\alpha\), and the moving neighbor
\(b\) have type four. On a first-minimum segment set
\[
 \begin{gathered}
 d=x-.1,\quad .1\le x\le.22,\quad x\le z\le.5,\\
 a=x-i\lambda_a d,\qquad b=z-i\lambda_b d,\qquad
 0\le\lambda_b=-c_bR(z)/.12\le17/20,\\
 \lambda_a\in[-7/40,3/5]\quad(\alpha=0),\qquad
 \lambda_a\in[0,13/20]\quad(\alpha=1).
 \end{gathered}                                                \tag{1}
\]
The own-four first coefficient uses the actual attached \(m\ge3\)
compatibility theorem, as in the
[own-four comparison](research_mixed_first_four_moving_height_comparison.md).
For the neighbor, the full ordinary own-four height bound is
\(-.102<c_b<-.001\). Its upper cutoff \(R(z)\) is the original
one, including \(400(.5-z)^2\) above \(.45\).
Thus its derivative coefficient and actual height in (1) share
the same \(\lambda_b\); they are not released independently.

Let
\[
 s=v+i\eta,\quad .22\le v\le.49,\quad -.108\le\eta\le0,
 \qquad t=w+i\zeta,\quad .22\le w\le.49 .                       \tag{2}
\]
The following factor is represented here by one of its original
regular profiles. Its source estimate must independently be valid
where this calculation is applied. In particular no moving-root
packet is imported merely from root eligibility.

After the two halves at \(b\) are combined, the exact derivative is
\[
 \begin{split}
 \mathcal H={}&\Re[(1-i\lambda_a)D_a-i\lambda_bD_b],\\
 D_a={}&g'(e+a)+g'(s+a)-(2+\alpha)g'(a)+2\pi is,\\
 D_b={}&g'(s+b)+g'(t+b)-3g'(b)+2\pi it,
                    \qquad .27\le e\le.49.
 \end{split}                                                  \tag{3}
\]
The last chirp belongs to the following factor.
Its other target and own-type allocation disappear only from this
particular derivative, since that target is held fixed.
Both original \(b\) incidences remain in \(D_b\).
The protected middle terms and relative pinning fee retain their
original values as in the moving-height reduction.

## 2. The first ordinary index height can still be raised

**Proposition 1.** Throughout (1)--(3), regardless of the fixed
following index \(t\),
\[
                     \partial_\eta\mathcal H
                                <-\frac{47\pi}{2009}<0.       \tag{4}
\]
Consequently
\[
 \mathcal H(e,v,\eta,t)\ge
 \mathcal H(e,v,0,t)+\frac{47\pi}{2009}(-\eta).                 \tag{5}
\]

*Proof.* Differentiating the exact original logarithms and chirps,
with \(g''=\pi\cot\pi z-\pi i\), gives
\[
 \frac{\partial_\eta\mathcal H}{\pi}
 =-1-\Im\cot\pi(s+a)
       +\lambda_a\Re\cot\pi(s+a)
       +\lambda_b\Re\cot\pi(s+b).                            \tag{6}
\]
For any finite height, the real cotangent is at most
\(\cot(.32\pi)\) when its real argument belongs to
\([.32,.99]\). On the first half this follows by increasing the
denominator \(\cosh(2\pi h)-\cos(2\pi y)\); on the second
half the real cotangent is nonpositive. An elementary bound is
\[
 \cot(.32\pi)=\tan(.18\pi)
                         <\frac{1308}{2009}<\frac23.           \tag{7}
\]
Indeed \(.18\pi<4/7\), and for \(0\le u\le4/7\),
\(\sin u\le u-u^3/7\), \(\cos u\ge1-u^2/2\).
The numerator bound is increasing on this interval, so their
endpoint ratio is \(1308/2009\).

If \(\lambda_a\ge0\), then \(\Im(s+a)\le0\), so its
imaginary cotangent is nonnegative.
Since \(\lambda_a+\lambda_b\le3/2\), (6)--(7) give
\[
       \partial_\eta\mathcal H/\pi
                     <-1+\frac32\frac{1308}{2009}
                      =-\frac{47}{2009}.                    \tag{8}
\]

If \(\lambda_a<0\), only own three occurs and
\(\Im a\le.021\), \(|\lambda_a|\le7/40\).
The real argument of \(s+a\) lies in \([.32,.71]\), where
its angular cosine is less than \(-6/25\). Hence
\[
                 \Re\cot\pi(s+a)>-25/31.
                                                               \tag{9}
\]
When its height is positive, \(e^{2\pi\Im(s+a)}<23/20\)
and therefore its hyperbolic-sine numerator has modulus less
than \(129/920\). Its denominator exceeds \(31/25\).
For negative height its imaginary cotangent is nonnegative.
In either case
\[
                       \Im\cot\pi(s+a)>-1/8.                 \tag{10}
\]
Using (7), (9)--(10) in (6),
\[
 \partial_\eta\mathcal H/\pi
 <-1+\frac18+\frac7{40}+\frac{17}{20}\frac23
 =-\frac2{15}<-\frac{47}{2009}.                              \tag{11}
\]
This proves (4), and integration proves (5).
No profile critical-point condition has been imposed. \(\square\)

The real-private cap index \(e\) enters only \(D_a\).
Its established endpoint-minimum argument is consequently unchanged:
after (5), a lower bound still reduces \(e\) to \(.27,.49\).
There is no corresponding claimed endpoint reduction in \(v\)
once the last term of (6) is retained.

## 3. A following nonpositive index has one remaining endpoint

Suppose additionally \(-.108\le\zeta\le0\).
For fixed \(b\), the only \(t\)-dependent expression in (3) is
\(\lambda_b\Im[g'(t+b)+2\pi it]\).
Let \(R=e^{2\pi(\zeta+\Im b)}\le1\),
\(\theta=2\pi(w+z)\). Then
\[
 \partial_w\Im[g'(t+b)+2\pi it]
   =\frac{2\pi(1-R\cos\theta)}{1+R^2-2R\cos\theta}
                                                \ge\pi>0.   \tag{12}
\]
Thus its minimum is at \(w=.22\).
At that endpoint the derivative with respect to \(\zeta\)
is \(\Re g''(.22+b+i\zeta)\), whose sign is the sign of
\(\sin(2\pi(.22+z))\). Accordingly it suffices to use
\[
 \zeta_0(z)=
 \begin{cases}
 -.108,&z<.28,\\
 0,&z>.28,
 \end{cases}                                                \tag{13}
\]
with either value at \(z=.28\). At equality the shifted argument
has real part \(1/2\), so its original logarithm is real and
the expression is independent of \(\zeta\).
A tighter known height interval may use its corresponding endpoint.
The conclusion is trivial if \(\lambda_b=0\).

In particular, put
\[
 r_b=e^{-2\pi\lambda_b d},\qquad
 R_0=e^{2\pi\zeta_0(z)},\qquad
 A(y,r)=\arg(1-re^{-2\pi i y})
\]
on the original lift. After (5), (12)--(13), a sufficient lower
expression for the complete coupled derivative is exactly
\[
 \begin{split}
 &\mathcal H_\alpha(e,v,0;x,-.12\lambda_a)\\
 &\quad+\lambda_b\{
      A(v+z,r_b)+A(.22+z,r_bR_0)-3A(z,r_b)+.44\pi\}.
 \end{split}                                                 \tag{14}
\]
Here \(\mathcal H_\alpha\) is the first-coordinate expression of
the moving-height reduction, and \(e=.27,.49\) suffices.
Every radius in (14) retains the actual minimum-level coefficient.
There are no independently optimized imaginary arguments.
Equation (14) is a lower expression, not a claimed nonnegative one.

## 4. Why the earlier slope constants alone are insufficient

At the seam \(x=.1\), the actual \(a,b\) heights in (1) vanish.
For the real lower-cut profiles \(s=t=.22\) and \(z=.22\),
the original logarithmic arguments give exactly
\[
 \Im D_b
   =\pi(w-v+z-1/2)=-\frac{7\pi}{25}.                         \tag{15}
\]
This is compatible with every actual negative own-four reference
coefficient. At this \(z\), \(R(z)=1\), so
\(\lambda_b=-c_b/.12>1/120\). The neighboring contribution
in (3) is consequently less than
\[
                         -\frac{7\pi}{3000}<-\frac1{300}.
                                                               \tag{16}
\]
Thus retaining only the uniform own-four first-coordinate slope
\(1/300\) discards information needed to pay even this cut
configuration. This does not say that the full derivative is
negative there: its actual first-coordinate term is much larger
than that deliberately coarse floor.

A successful coupled proof must retain more of (14), the actual
maximizing-profile restrictions, or another quantitative correlation.
The high physical-tail profiles still require their own derivative
formulas. Nothing in (4)--(16) identifies a new finite packet,
pays the neighbor term, or changes the calibrated boundary
reference and its relative pinning fee.

