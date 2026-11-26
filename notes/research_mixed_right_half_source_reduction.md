# A full-source reduction on the right outer half-period

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note reduces a right-half supporting-plane comparison to explicit
scalar extrema. It retains the complete conditional sum and the actual
Fourier weight. It does **not** assert that the resulting scalar bound lies
below every geometric supporting plane. In particular, a numerical test
on unrelated reference rectangles is not a mixed-word theorem.

## 1. The right-half Fourier weight

Use the notation of the
[exact Fourier-weight theorem](research_mixed_fourier_weight_continuation.md):
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad \nu(z)=-\Re g(z),\qquad X=e^{-2\pi iz}.
 \tag{1}
\]
The branch is the original one on \(0<\Re z<1\). Fix
\(0<H<\log 2/(2\pi)\). For every \(\eta>0\), uniformly for
\(1/2\le x\le1\) and \(|h|\le H\), the actual degree-less-than-\(N\)
Fourier polynomial satisfies
\[
 |d_N(e^{-2\pi i(x+ih)})|
 \le C_\eta N^A\exp N\{2\pi\max(h,0)+\eta\}.
 \tag{2}
\]

For \(h\le0\), the argument of the dilogarithm in (1) lies in the
closed upper half of the unit disk when \(x\in[1/2,1]\).
The integral \(-\int_0^1\log(1-tZ)\,dt/t\) shows that its imaginary
part is nonnegative. Hence \(\nu(x+ih)\le0\). For \(h\ge0\),
the inversion identity with the same branch gives
\[
 \nu(x+ih)=\nu(x-ih)+\pi h(1-2x)\le0.
 \tag{3}
\]
On a compact substrip ending before \(x=1\), (2) therefore follows
from the general absolute bound in §5 of the Fourier-weight theorem.

The endpoint \(x=1\) requires the forcing, not a continuation of a
root-grid value. By periodicity write \(x-1\in[-\delta,0]\), start
at real coordinate in \([2\delta,2\delta+1/N]\) with the same
height, and iterate the exact recurrence
\[
 d_N(r^{-1}X)=(1-X)d_N(X)+\frac{X}{N^2}\sum_{j=0}^{N-1}X^j,
 \qquad r=e^{-2\pi i/N}.
 \tag{4}
\]
The number of steps is chosen to reach the target coordinate exactly.
For sufficiently small fixed \(\delta\), all multipliers have modulus
at most a common \(\kappa<1\): at zero angle their largest modulus
is \(\max(1-e^{-2\pi H},e^{2\pi H}-1)<1\).
The forcing has rate at most \(2\pi h_+\). At the starting point,
the general absolute bound has rate at most \(2\pi h_++o(1)\),
uniformly in \(|h|\le H\), as \(\delta\downarrow0\).
This follows either from (3) near the positive side of the seam or
from continuity of the lower-half-disk dilogarithm there; the limiting
upper-side value is \(\nu(ih)=\pi h\) for \(h>0\).
The contracting geometric sum in (4) proves (2) through the seam.
Thus no exponentially large reciprocal-factorial branch is assigned
to the right half-period.

If a type-four variable is selected in the wrapped factor, its modulus
is multiplied by \(|X^{-N}|=e^{-2\pi Nh}\). For positive height,
this cancels the rate in (2). With the half-weight allocation below,
the corresponding cancellation is \(\pi h\) in each incident block.

## 2. The original finite sum and its angular envelope

Put \(P_j=(r;r)_j\), \(p_j(X)=(rX;r)_j\), and retain
\[
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
      \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},
 \qquad \epsilon\in\{0,1\}.
 \tag{5}
\]
For real \(h,x\) and \(0\le u\le1\), define
\[
 I_h(u,x)=\int_0^u\log|1-e^{2\pi h-2\pi i(x+t)}|\,dt,
 \qquad J(u)=\Re g(u).
 \tag{6}
\]
The logarithmic integrals are continuous through their integrable zeros.
The truncated-log Riemann-sum argument in
[the whole-period product bound](research_mixed_boundary_strip_bounds.md#2-a-product-bound-that-includes-the-whole-finite-period)
gives, uniformly on bounded height ranges and all angles,
\[
 |p_j(e^{-2\pi i(x+ih)})|
       \le N^A e^{N I_h(j/N,x)},\qquad
 |P_j|=e^{N J(j/N)+O(\log N)}.
 \tag{7}
\]
For clarity, the same proof works at every radius: truncate the logarithm
below \(-\log N\); its total variation is \(O(\log N)\), and the
added integral is \(O(1/N)\), uniformly as the radius crosses one.

Let the left type be \(\eta\in\{0,1\}\), and allocate the actual
Fourier modulus as
\(\mathcal B=|C_\epsilon(X,Y)|\,|d_N(X)|^{\eta/2}
|d_N(Y)|^{\epsilon/2}\). On a compact interior angle range use
\(D_h(x)=\max\{\nu(x+ih),2\pi h_+\}\); through a seam its upper
semicontinuous limiting rate is justified by (4).
Equations (2), (5), and (7) give the full-source upper rate
\[
 \sup_{0\le u\le1}\left[
 I_h(u,x)+I_k(u,y)-(2+\epsilon)J(u)-2\pi hu
       +\frac\eta2D_h(x)+\frac\epsilon2D_k(y)\right].
 \tag{8}
\]
An arbitrarily small fixed positive error in the rate is allowed.
Every row, including \(j=N-1\), and both parities are included.
For selected type-four variables subtract their actual half-wrap
rates \(\pi h\) or \(\pi k\); these factors are not omitted.

## 3. An explicit finite candidate set

For a real supporting slope \(p\), set
\[
 M_h(u;p)=\max_{1/2\le x\le1}\{I_h(u,x)-px\}.
 \tag{9}
\]
If \(0<u<1\), every smooth interior maximizer satisfies, with
\(\theta=2\pi x\),
\[
 (\cos(2\pi u)-e^{2p})\cos\theta
       -\sin(2\pi u)\sin\theta
       =\cosh(2\pi h)(1-e^{2p}).
 \tag{10}
\]
There are at most two such points in a period. Thus (9) is exactly
the largest value at \(x=1/2,1\) and the solutions of (10) in
\([1/2,1]\). If \(h=0\), a possible internal product zero
\(x=1-u\) is not an extra maximum: the derivative tends to
\(-\infty\) on both sides, so the function decreases there.
One may include that point harmlessly in the candidate list.
For \(u=0,1\), the integral is independent of \(x\), and the two
endpoints suffice.

Indeed, away from zeros,
\(\partial_x I_h=\log|1-Re^{-2\pi i(x+u)}|
-\log|1-Re^{-2\pi ix}|\), with \(R=e^{2\pi h}\).
Squaring the equation \(\partial_x I_h=p\) gives (10), using
\(|1-Re^{-i\theta}|^2=2R(\cosh(2\pi h)-\cos\theta)\).
The coefficients of the sine and cosine in (10) cannot both vanish
for \(0<u<1\). No squaring ambiguity remains because both moduli
are nonnegative and the factor \(e^p\) is positive.

In particular, without the supporting slope the integral decreases
then increases on the right half, with its unique minimum at
\(x=1-u/2\). Its largest value is at \(1/2\) for \(u\le1/2\),
and at \(1\) for \(u\ge1/2\). To compare these endpoints, use
the symmetry of \(\log|1-Re^{-2\pi it}|\) about \(1/2\): the
difference of their derivatives in \(u\) changes sign at \(1/4\)
and \(3/4\), and their values agree at \(u=0,1/2,1\).
The weighted problem (9) must still use (10); unweighted
unimodality alone does not justify discarding interior candidates.

For example, if the right-half coordinate is \(x\), a plane with
real slopes \((p,q)\) reduces (8), after subtracting \(px+qy\), to
\[
 \sup_{u,y}\left[
 M_h(u;p)+I_k(u,y)-(2+\epsilon)J(u)-2\pi hu
 +\eta\pi h_++\frac\epsilon2D_k(y)-qy\right].
 \tag{11}
\]
The constant and imaginary-height terms of the actual complex
supporting plane must also be retained. The corresponding formula
for a right-half \(y\) uses \(M_k(u;q)\) and leaves
\(-2\pi hu\) unchanged. Equation (11) is a usable reduction of
the original finite source; proving a uniform strict comparison
with the calibrated geometric plane is a separate remaining task.

## 4. Elimination of the extra candidate on the concave core

Here the right-half target has height zero. This refinement is conditional
only on the explicitly stated bound for its real supporting slope; it
does not assert that bound for every geometric reference.

**Lemma 1.** Suppose \(p\ge-1/5\), \(0\le u\le1\), and the
other angle lies in \([13/100,1/2]\) at height
\(-57/1000\le h\le1/50\). For each of the two Fourier branches
in (8), its maximum over the right angle and over \(u\in[0,1/2]\)
is attained with the right angle equal to \(1/2\) or \(1\).
For \(u\in[1/2,1]\), the right-angle maximum is already at
these endpoints pointwise in every other variable.

*Proof.* At zero height,
\[
 \partial_{xx}I_0(u,x)
       =-\frac{\pi\sin\pi u}{\sin\pi x\sin\pi(x+u)}.
 \tag{12}
\]
For \(u\ge1/2\), this is nonnegative on the open right interval.
For \(0<u<1/2\), it is negative before \(x=1-u\) and positive
afterward. The only possible extra maximum is on the first piece,
and exists only if \(p<\log\cos\pi u\). In that case it is the
unique point satisfying
\[
 \cot\pi x=\frac{e^p-\cos\pi u}{\sin\pi u}.
 \tag{13}
\]
Because \(-1/5>\log\cos(\pi/5)\), no such point is possible
for \(u\ge1/5\). On the first piece in (12), the product of the
two sines is at most \(\cos\pi u\). Its gain over the value at
\(x=1/2\) is consequently at most
\[
 \min\left\{d_+(1/2-u),
                 \frac{d_+^2}{2\pi\tan\pi u}\right\}
       \le 3(1/5-u)^2,\qquad 0<u<1/5,
 \quad d=1/5+\log\cos\pi u.
 \tag{14}
\]
The first bound uses the tangent slope and interval length; the second
uses the curvature lower bound \(\pi\tan\pi u\).
For an exact elementary verification of the last inequality, put
\[
 a=197/20<\pi^2,\qquad
 D(u)=1/5-au^2/2-a^2u^4/12.
 \tag{15}
\]
The inequalities \(\tan t\ge t+t^3/3\) and integration imply
\(d\le D(u)\). On \([0,21/1000]\), the polynomial
\(3(1/5-u)^2-D(u)(1/2-u)\) is positive. On
\([21/1000,49/250]\), the polynomial
\(6au(1/5-u)^2-D(u)^2\) is positive. The exact rational Sturm
checks recorded below verify both claims (zero roots and a positive
endpoint value). Finally \(D(49/250)<0\) and \(D\) decreases.
These three intervals prove (14), including its continuous value at zero.

Let \(\beta\in\{0,1\}\) be the type of the other leg; it need not
equal the own type \(\epsilon\) when the right coordinate is \(Y\).
At right angle \(1/2\), the part of either branch depending on the
row and other angle is, up to affine terms and constants,
\[
 E(u,y)=J(1/2+u)+\Re g(u+y+ih)
        -(1+q/2)\Re g(y+ih)-(2+\epsilon)J(u),
 \qquad q\in\{0,\beta\}.
 \tag{16}
\]
The possible original factor \(X^{-j}\) adds either zero or
\(-2\pi hu\); all supporting-plane and wrap terms have zero
second derivative in \(u\). On this core the complex triangle
\(\Re[g(u+z)-g(u)-g(z)]\), \(z=y+ih\), is concave: the
[triangle criterion](research_mixed_boundary_strip_bounds.md#1-the-complex-triangle-criterion)
applies because \(u\) is real and
\(\cos(2\pi y)\le\cos(13\pi/50)<e^{-57\pi/500}\).
The remainder \(J(1/2+u)-(1+\epsilon)J(u)\) has negative second
derivative at least \(\pi(\tan\pi u+\cot\pi u)\ge2\pi\).
It follows that \(E_{uu}\le-2\pi\).

Moreover \(E_u(1/5,y)>19/100\), including the possible
\(-2\pi h\) term. A uniform explicit lower bound is
\[
 \log(2\cos(\pi/5))
 +\tfrac12\log\{1+R^2-2R\cos(7\pi/5)\}
 -3\log(2\sin(\pi/5))-\pi/25>19/100,
 \qquad R=e^{-57\pi/500}.
 \tag{17}
\]
Indeed \(1/5+y\in[33/100,7/10]\), whose cosine is at most
\(\cos(7\pi/5)<0\), and the modulus increases with its radius
on this arc. The smallest radius is \(R\); the worst linear
height term is \(-2\pi/50=-\pi/25\).
For every fixed \(y\), strong concavity therefore gives
\(E(u,y)\le E(1/5,y)-\pi(1/5-u)^2\) when \(u<1/5\).
This loss absorbs (14), since \(3<\pi\). Thus an extra right-angle
candidate cannot exceed the value already available at row \(1/5\)
and right angle \(1/2\). The argument applies separately to each
Fourier branch, so taking their maximum is legitimate. Continuous
limits retain the row and angular boundary points. \(\square\)

The lemma does not dispose of the remaining source regions where the
other angle is below \(13/100\) or above \(1/2\), nor does it bound
the row maximum itself. Its purpose is to remove the extra right-angle
candidate on the main source region before an outward support comparison.

## 5. Elimination of the small other-angle strip

**Theorem 2.** In addition to \(p\ge-1/5\), suppose the real
supporting slope \(\kappa\) of the other angle is at most \(1/4\).
Keep its height in \([-57/1000,1/50]\). The maximum of the full
rate envelope (8), with its supporting-plane and half-wrap terms,
over
\[
 0\le u\le1/2,\qquad 1/2\le x\le1,\qquad 0\le y\le1/2
 \tag{18}
\]
is already attained on the union of
\[
 \{x=1\}\quad\hbox{and}\quad
 \{x=1/2,\ 13/100\le y\le1/2\}.
 \tag{19}
\]
Here \(x\) denotes whichever original outer coordinate is on the
right half, and \(y\) denotes the other. The original factor
\(X^{-j}\) remains in its original orientation. Thus the theorem
covers all four \((\eta,\epsilon)\) type pairs in both orientations:
eight full-source cases, or twelve analytic Fourier-branch cases
(four with \(\beta=0\), eight with \(\beta=1\)). Selected type-four
half-wrap factors change only constants in this argument. Both
parities and every finite row are retained by (8).

*Proof.* Write \(L_h(t)=\log|1-e^{2\pi h-2\pi it}|\).
On either branch \(q\in\{0,\beta\}\), at right angle \(1/2\),
\[
 E_y=L_h(u+y)-(1+q/2)L_h(y)-\kappa.
 \tag{20}
\]
For \(0\le y\le13/100\) and the stated heights, \(L_h(y)\le0\).
Indeed the squared modulus increases with \(y\) in this range and
is convex in its radius, so it is enough to check the two height
endpoints at \(y=13/100\); their moduli are less than one.
For \(1/10\le u\le1/2\), the same angular monotonicity gives
\(L_h(u+y)\ge L_h(y+1/10)\): reflect the upper endpoint
\(1/2+y\) about \(1/2\), and use
\(1/2-y\ge1/10+y\).

The difference \(L_h(y+1/10)-L_h(y)\) has derivative of the
sign
\[
 \cosh(2\pi h)\cos(2\pi y+\pi/10)-\cos(\pi/10).
 \tag{21}
\]
This expression decreases with \(y\), so the difference has no
interior minimum on the small strip. Its squared-modulus ratio
decreases with \(\cosh(2\pi h)\). Consequently its minimum is
at \(y=0\) or \(13/100\), with \(|h|=57/1000\). Both endpoint
differences exceed \(9/20\); the smaller is greater than
\(0.45222\). Hence (20) is greater than \(1/5\).
For these rows, increasing \(y\) to \(13/100\) increases every
branch, after which Lemma 1 applies.

For \(0<u<1/10\), \(0\le y\le13/100\), one has
\(u+y<23/100<1/4\). Completing the square in the radius gives
\[
 |1-Re^{-2\pi i(u+y)}|\ge\sin(2\pi(u+y))
                         \ge\sin(2\pi u).
 \tag{22}
\]
Thus, at right angle \(1/2\), including the worst original linear
height term,
\[
 E_u\ge\log2+2\log\cos(\pi u)
            -\log(2\sin\pi u)-\pi/25>9/10.
 \tag{23}
\]
The own type \(\epsilon=0\) is the worst case because
\(\log(2\sin\pi u)<0\). The displayed lower bound decreases
with \(u\), and at \(u=1/10\) it is greater than \(0.94833\).
Increase the row to \(1/10\), then the other angle to \(13/100\).
The core row estimate used in Lemma 1 then gives an additional
gain of at least \(\pi/100\) on comparing row \(1/10\) with
row \(1/5\). The total gain absorbs the possible right-angle
stationary improvement (14), since exactly
\[
 \frac9{10}(1/10-u)+\frac\pi{100}
       -3(1/5-u)^2-\frac{\pi-3}{100}
           =3u(1/10-u)\ge0.
 \tag{24}
\]
The endpoint \(x=1\) is kept throughout. All remaining candidate
values therefore move into (19). Endpoint limits cover \(u=0\),
\(y=0\), and logarithmic zeros. Taking the maximum of the two
Fourier branches preserves the conclusion. \(\square\)

The remaining regions are the high rows \(u>1/2\), the other
right half \(y>1/2\), and the retained endpoint \(x=1\), together
with the actual scalar comparison on the core. No global exterior
supporting-plane theorem is inferred from Theorem 2 alone.

## 6. Reproduction and scope

The focused checker
`python3 experiments/check_mixed_right_half_source_reduction.py`
verifies the elementary squared-modulus and stationary-candidate
identities, the two exact Sturm signs, and the outward scalar
margins in Lemma 1, and records the source hashes. It does not certify a geometric supporting-plane
gap, the analytic Riemann-sum argument, or a global mixed-word
lower bound. No floating pilot is a premise of the statements above.
