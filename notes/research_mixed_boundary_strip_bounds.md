# Full conditional-kernel bounds near an outer period seam

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note gives uniform bounds for the whole original conditional
kernel near either tapered endpoint \(X=1\), and near the left
period seam while retaining the original or selected-alias height. Every finite row and the true Fourier
polynomial are retained. These estimates can supply the thin-end
part of an outer-contour decomposition. They do not yet compare
every outer point with its actual geometric supporting plane.

## 1. The complex triangle criterion

Write \(V(s,a)=g(s+a)-g(s)-g(a)\), with the original primitive
\(g''(z)=\pi\cot(\pi z)-\pi i\). Suppose
\(0<\Re s,\Re a<1/2\), and put
\[
 \cot\pi s=u+iv,\qquad \cot\pi a=p+iq,\qquad u,p>0.
\]
The cotangent addition identity gives exactly
\[
 \det\bigl(-\Re V''/\pi\bigr)
 =\frac{(u+p)^2-(pv-uq)^2}{(u+p)^2+(v+q)^2}.                  \tag{1}
\]
Consequently this real symmetric Hessian is positive definite if and
only if \( |pv-uq|<u+p\). Indeed a positive determinant forces
\(\Re\cot\pi(s+a)<up/(u+p)<\min(u,p)\), which also makes both
diagonal entries positive.

In particular, the sufficient conditions
\[
                 |\Im\cot\pi s|<1,\qquad
                 |\Im\cot\pi a|<1                            \tag{2}
\]
make the pair positive. For \(z=x+ih\), \(0<x<1/2\), (2) is equivalent to
\[
 \cos(2\pi x)<e^{-2\pi|h|}.
 \tag{3}
\]
It holds for arbitrary finite heights at \(x\ge1/4\). At \(x<1/4\),
it asks for \( |h|<-\log\cos(2\pi x)/(2\pi)\), a quadratic
height taper near zero. When all relevant legs satisfy (2), the
local three-variable phase in the central outer theorem is a sum
of two positive pair forms and positive own-index cotangents.
The same forms add with the original incidence multiplicities.

The fixed-height version cannot hold all the way to zero. If
\(a=x+ih\), \(h\ne0\), and \(x\downarrow0\), then
\(p\to0\) and \(q\to-\coth(\pi h)\), whose modulus exceeds one.
For fixed \(s\), the numerator in (1) tends to
\(u^2(1-q^2)<0\). More directly the outer diagonal of the local
negative real Hessian tends to
\(-\pi\Re\cot\pi(s+ih)<0\).
This rules out a global unsummed constant-height concavity proof.
It does not rule out a supporting-plane bound for the finite sum,
which still contains cancellation.

## 2. A product bound that includes the whole finite period

Let
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad S_j=|P_j|,
 \quad p_j(X)=(rX;r)_j,
\]
and retain the original finite kernel
\[
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
           \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}}.
 \tag{4}
\]
For \(u\in[0,1]\), define
\[
 L(u)=-2J((1-u)/2),\qquad
 F_\epsilon(u;C)=L(u)-(1+\epsilon)J(u)+Cu,
 \quad M_\epsilon(C)=\max_{0\le u\le1}F_\epsilon(u;C).
 \tag{5}
\]
Here \(J\) is the continuous real primitive on \([0,1]\).
Uniformly for every complex \(Y\),
\[
 |p_j(Y)|\le N^A
       \exp N\{L(j/N)+(j/N)\log_+|Y|\}.                       \tag{6}
\]
On a fixed compact annulus the exponent \(A\) can be fixed.

To prove (6) on the unit circle, integrate
\(\log(2|\sin\pi t|)\) over an arc of length \(u\).
Its largest integral is on the arc centered at \(1/2\), and equals
\(J((1+u)/2)-J((1-u)/2)=L(u)\). This is the elementary rearrangement
inequality for a periodic function increasing up to \(1/2\) and
then decreasing. Replace the logarithm below \(-\log N\) by that
constant. Its total variation is \(O(\log N)\), and its integral
increases by \(O(1/N)\). The shifted Riemann sum therefore differs
from its integral by \(O(\log N)\), uniformly through every zero
and every upper row. This proves the unit-circle bound. The maximum
principle proves the same bound inside that circle. Outside it use
\[
 |p_j(Y)|=|Y|^j|p_j(1/\overline Y)|,
\]
which follows from the exact reciprocal polynomial identity;
its omitted phase has modulus one. This proves (6).

There is an analogous all-row sine-factorial estimate
\(S_j=\exp\{NJ(j/N)+O(\log N)\}\), including both ends.
Consequently the bounds below do not drop high conditional indices
or replace the original finite support by a local saddle.

## 3. The actual Fourier weight near one

Let \(d_N\) be the original degree-less-than-\(N\) polynomial with
\(d_N(r^j)=1/P_j\). On and inside the unit circle,
\[
                  |d_N(X)|\le N^A e^{N/6}.                    \tag{7}
\]
Indeed the root-interpolation cardinal polynomials have modulus at
most one on the unit circle, so \( |d_N|\le N\max_j1/S_j\);
then use \(\max_{[0,1]}(-J)<1/6\) and the maximum principle.

A stronger bound holds near \(X=1\). There is a function
\(\omega(\delta)\downarrow0\) such that for every fixed sufficiently
small \(\delta>0\),
\[
 \sup_{|\Re z|,|\Im z|\le\delta}
       |d_N(e^{-2\pi iz})|
         \le C_\delta N^A e^{N\omega(\delta)}.                \tag{8}
\]
For precision, this is not inferred from \(d_N(1)=1\).
Use the exact forced recurrence
\[
 d_N(r^{-1}X)=(1-X)d_N(X)
                      +\frac{X}{N^2}\sum_{j=0}^{N-1}X^j.       \tag{9}
\]
Starting at a logarithmic coordinate whose real part lies in
\([2\delta,2\delta+1/N]\), iterate (9) until the desired real part
in \([-\delta,\delta]\) is reached. All imaginary parts remain
unchanged. For small fixed \(\delta\), every multiplier \(1-X\)
on the path has modulus less than \(1/2\). The forcing is bounded by
\(C_\delta N^{-1}e^{2\pi N\delta}\).
At the starting coordinate, the general absolute estimate from
[the Fourier-weight comparison](research_mixed_fourier_weight_continuation.md#5-a-criterion-for-relative-exponential-accuracy)
gives rate at most
\(\max\{-\Re g(z),2\pi\max(\Im z,0)\}+\delta\).
Since \(g(z)=O(z\log z)\) near zero, this tends to zero uniformly
on that starting interval as \(\delta\downarrow0\). Iterating the
contracting recurrence proves (8), including the physical point
\(X=1\), with its forcing retained.

## 4. Explicit full-source endpoint bounds

For types \(\eta,\epsilon\in\{0,1\}\), use the actual nonnegative
modulus of the local weighted factor
\[
 \mathcal B_{\eta\epsilon,N}(X,Y)
   =|C_{\epsilon,N}(X,Y)|\,
                  |d_N(X)|^{\eta/2}|d_N(Y)|^{\epsilon/2}.
 \tag{10}
\]
The square roots in this upper bound are just real modulus powers;
no holomorphic branch of a half Fourier weight is assumed.
The geometric height ranges used here are
\[
 h_3\in[-.03,.02],\qquad h_4\in[-.057,-.001].                 \tag{11}
\]
These ranges concern the unchanged other variable; the variable
approaching the endpoint is allowed to taper to height zero.
All real parts of the other variable run through its entire period.

**Theorem 1.** At \(X=1\), with \(Y=e^{-2\pi ib}\) at its own-type
height from (11), the whole source (10) has the following upper rates:
\[
 \begin{array}{c|cc}
 \epsilon&0&1\\\hline
 \text{left endpoint rate}&37/100&11/20.
 \end{array}                                                     \tag{12}
\]
At \(Y=1\), with \(X=e^{-2\pi ia}\) at its left-type height,
the upper rates are
\[
 \begin{array}{c|cc}
 &\eta=0&\eta=1\\\hline
 \epsilon=0&2/5&14/25\\
 \epsilon=1&51/100&16/25.
 \end{array}                                                     \tag{13}
\]
Every inequality is strict at the exponential level, uniformly in
the whole real period of the other variable. Each bound remains
valid on a fixed sufficiently small complex neighborhood of the
indicated endpoint variable and on slightly enlarged other-height
intervals. It retains all rows and both parities. The underlying
holomorphic kernel and integer Fourier-weight factors have the
corresponding fixed-derivative bounds on smaller neighborhoods, as
specified below; no derivative is asserted for the nonholomorphic
quantity \(\mathcal B\) itself.

*Proof.* At \(X=1\), \(p_j(1)=P_j\), so the triangle estimate in the
literal sum is
\[
 |C_{\epsilon,N}(1,Y)|
       \le\sum_{j<N}|p_j(Y)|/S_j^{1+\epsilon}.
\]
Equation (6) bounds its rate by \(M_\epsilon(\log_+|Y|)\).
If \(\epsilon=0\), the other height is at most .02, so the rate
is at most \(M_0(.04\pi)<.37\). If \(\epsilon=1\), the other
height is negative, so its rate is at most \(M_1(0)\). Its actual
half Fourier weight adds at most \(1/12\), by (7). Thus
\(M_1(0)+1/12<.55\). The weight at one is exactly one.

At \(Y=1\), the reciprocal identity instead gives
\[
 |C_{\epsilon,N}(X,1)|
       \le\sum_{j<N}|p_j(1/\overline X)|/S_j^{1+\epsilon}.
\]
For \(\eta=0\), the radius cost is at most \(.06\pi\); there is
no left weight. For \(\eta=1\), it is at most \(.114\pi\), and
(7) adds \(1/12\). These are precisely the four comparisons (13).

For reference the scalar comparisons follow from one-variable
critical equations, not from a grid. For \(\epsilon=0\),
\[
 F'_0=C-\log(2\sin(\pi u/2)),
\]
so the sole maximum is at
\(u=2\arcsin(e^C/2)/\pi\). For \(\epsilon=1\), writing
\(v=\sin^2(\pi u/2)\), the critical equation is
\[
                    64v^2(1-v)=e^{2C}.                        \tag{14}
\]
Its lower root in \((0,2/3)\) is a local maximum, and its upper
root is a local minimum. Compare that maximum with the two endpoint
values zero and \(C\); the checker verifies the strict budgets
(12)--(13) with outward arithmetic and certified rational root brackets.

Finally let one endpoint variable have logarithmic modulus less than
\(\delta\). The exact finite-product estimate
\(|1-r^hX|\le|1-r^h|+C\delta\) gives
\[
 |p_j(X)|\le C_\delta N^A
       e^{N\{J(j/N)+C\delta(1+|\log\delta|)\}},
\]
uniformly through all rows and zeros. Its extra factor \(X^{-j}\),
if present, costs \(O(N\delta)\). The corresponding half Fourier
weight costs \(N\omega(\delta)/2\), by (8). Thus the strict budgets
persist on a fixed endpoint neighborhood. The other-variable height
bounds can also be enlarged slightly by continuity of the scalar
maxima and the maximum-modulus polynomial bounds. Cauchy's estimates
on smaller neighborhoods bound every fixed derivative of the actual
holomorphic kernel and of the original integer-power Fourier factors.
In a literal contraction each Fourier factor is charged once, distributed
between its two incident bounds (10). The product rule therefore preserves
the resulting full-contraction exponent. This argument never differentiates
\(\mathcal B\) or selects a holomorphic half-weight. \(\square\)

The all-level statement concerns the actual finite expression (4),
not a continued conditional saddle outside its established packet
domain. It is useful only where the contour really approaches \(X=1\)
or \(Y=1\) with small height. At a fixed nonzero endpoint height, the
extra costs need not tend to zero.

At the exact endpoint there are stronger coherent identities:
\[
 C_{0,N}(1,Y)=Nd_N(Y),\qquad
 C_{0,N}(X,1)=N\overline{d_N(1/\overline X)}.                   \tag{15}
\]
Indeed the original coefficient identity gives \(L_0(0,b)=N\),
so \(C_{0,N}(1,r^b)=N/P_b\). Both sides of the first identity
are polynomials of degree less than \(N\). The second follows from
the exact Hermitian Gram identity on the unit circle and then
Laurent-polynomial identity. Thus at the literal left endpoint
and the current type-three height interval, the true rate is at most
\(1/6+.04\pi<3/10\), improving (12) at that endpoint.
Here the standard polynomial maximum-modulus bound outside the unit
circle costs \(N\log_+|Y|\). We do not infer the same improved rate
on a fixed endpoint neighborhood from cancellation only at \(X=1\);
the robust neighborhood assertion above uses its separate product proof.

## 5. The left period seam without a height taper

There is also a full-source bound on a small real strip around the
left period seam, at the unchanged actual or selected-alias height.
Let \(\sigma_a,\sigma_b\in\{0,1\}\), with a selected index possible
only at type four, and define
\[
 \mathcal B^{\sigma_a,\sigma_b}_{\eta\epsilon,N}
 =|C_{\epsilon,N}(X,Y)|\,
 |d_N(X)X^{-N\sigma_a}|^{\eta/2}
 |d_N(Y)Y^{-N\sigma_b}|^{\epsilon/2}.                           \tag{16}
\]
An unselected type-four variable has the negative height in (11);
a selected one has height \(7/500=.014\). Type-three heights remain
in (11). The other real angle is unrestricted.

For comparison, the tapered left bound (12) changes only when the
other variable is selected type four: its rate is then
\(M_1(.028\pi)+1/12<.57\). The tapered right table (13) is unchanged.
Indeed Bernstein's elementary polynomial bound gives, for \(R\ge1\),
\[
 \sup_{|X|=R}|d_N(X)X^{-N}|
       \le R^{-1}\sup_{|X|=1}|d_N(X)|
       \le N^A e^{N/6}.                                      \tag{17}
\]
The extra positive other height costs only \(.028\pi u\) in (6).
This assertion follows directly from the same scalar formula (14);
the numerical value of its bound is \(0.56365014\) from above.
No alias has been removed from (16).

Now put \(H_0=.03\), \(H_1=.057\), and let
\(h_+=.02\) if \(\epsilon=0\); if \(\epsilon=1\), set
\(h_+=0\) or \(h_+=.014\) according as the other variable is
unselected or selected. Define
\[
 \begin{split}
 \mathcal M_{\eta\epsilon}(h_+)
  =\frac{\epsilon}{12}
   +\max_{0\le u\le1}\{&
     \Re g(u-iH_\eta)-2J((1-u)/2)\\
     &-(2+\epsilon)J(u)+2\pi(H_\eta+h_+)u\}.
 \end{split}                                                   \tag{18}
\]

**Proposition 2.** The following are upper rates for the complete
finite expression (16), uniformly at \(\Re a=0\) modulo one and
at all the indicated heights:
\[
 \begin{array}{c|cc}
 &\eta=0&\eta=1\\\hline
 \epsilon=0&.454&.534\\
 \epsilon=1,\ \sigma_b=0&.612&.673\\
 \epsilon=1,\ \sigma_b=1&.634&.697 .
 \end{array}                                                    \tag{19}
\]
They remain valid on the explicit real strip
\(\operatorname{dist}(\Re a,\mathbb Z)\le10^{-6}\), with the same
unchanged heights. This conclusion requires no vertical taper
or joining-current estimate inside that strip. It does not compare
(19) with the geometric supporting plane.

*Proof.* At the seam \(a=ih_a\),
\[
 |X^{-j}p_j(X)|=\prod_{k=1}^j|e^{-2\pi h_a}-r^k|
                   \le\prod_{k=1}^j|e^{2\pi H_\eta}-r^k| .
 \tag{20}
\]
This holds throughout \(-H_\eta\le h_a\le H_\eta\), including every
height specified above. To see it factorwise, put \(R=e^{2\pi H_\eta}\).
For every \(R^{-1}\le\rho\le R\) and \(|\zeta|=1\),
\[
 |R-\zeta|^2-|\rho-\zeta|^2
       =(R-\rho)(R+\rho-2\Re\zeta)\ge0,
\]
since \(R+\rho\ge R+R^{-1}\ge2\).
The logarithm of the right product in (20), divided by \(N\), is
\[
                  2\pi H_\eta u+\Re g(u-iH_\eta)+O(N^{-1}),
 \qquad u=j/N.                                                \tag{21}
\]
Its integrand is uniformly regular because \(R>1\).
The maximum-modulus product bound (6), the sine-factorial estimate,
and the other true half-weight bound (7) or (17) now give (18).

The left Fourier factor in (16) has zero upper exponential rate at
the seam, and rate tending to zero uniformly near it. For the
unselected negative heights this follows from the absolute comparison
for \(d_N\): \(-\Re g(x+ih_a)\to0\) as \(x\to0\), uniformly in the
negative height interval. For the positive selected height, apply the
same comparison after multiplying by \(X^{-N}\); its rate is at most
\[
 \max\{-\Re g(x+ih_a)-2\pi h_a,0\}+o(1).
\]
As \(x\downarrow0\), the expression inside the first alternative tends
to \(-\pi h_a<0\), by the exact reflection identity for \(g\).
To include the seam itself and its other side uniformly, iterate (9)
as in the proof of (8), now normalizing by \(X^{-N}\) in the selected
case. This normalization is unchanged by \(X\mapsto r^{-1}X\).
The multipliers have modulus less than one uniformly on these
height intervals near the seam, and the normalized forcing has
polynomial size. Thus the stated zero-rate estimate includes the
entire small real strip, without division by a possibly vanishing
Fourier polynomial.

The maxima in (18) have a complete scalar verification. Write
\[
 R=e^{2\pi H_\eta},\quad E=e^{4\pi h_+},\quad
                         v=\sin^2(\pi u/2).
\]
Their derivative vanishes exactly when
\[
 16^{2+\epsilon}v^{2+\epsilon}(1-v)^{1+\epsilon}
       -4E\{(R-1)^2+16Rv(1-v)\}=0.                            \tag{22}
\]
After \(v=w/(1+w)\), the coefficient signs are
\((-,-,+,-)\) for type three and \((-,-,-,+,-,-)\) for type four.
The single positive coefficient is certified respectively by
\[
 256-4E\{3(R-1)^2+16R\}>0,\qquad
 4096-4E\{10(R-1)^2+48R\}>0.                                  \tag{23}
\]
The polynomial in (22) is negative at zero and one, and positive
at \(v=1/2\), also checked outward. Descartes' rule and these signs
give exactly two roots in \((0,1)\). The first gives the sole local
maximum and the second a local minimum. Exact rational brackets
for the first root, followed by comparison with endpoint values
zero and \(2\pi(H_\eta+h_+)\), prove every bound (19).
No row-variable sampling is used.

For real parts within \(\delta\) of the seam, each factor on the
left of (20) changes by at most \(C\delta\). Its majorant on the
right has modulus at least \(R-1>0\), so the product rate increases
by only \(C\delta\). Combine this with the just-proved vanishing
left-weight cost and the strict scalar margins in (19). This
proves the whole strip assertion. The same compact holomorphic
upper bounds preserve fixed derivatives of original integer-power
products, with the scope specified after (14). \(\square\)

For the claimed explicit width, set \(\delta=10^{-6}\).
The factorwise perturbation in (20) has rate cost at most
\[
 \frac{2\pi e^{2\pi H_\eta}}{e^{2\pi H_\eta}-1}\,\delta
                         <37\delta.                          \tag{24}
\]
For the negative left-weight heights, the derivative of
\(-\Re g(x+ih)\) in \(x\) is at most
\[
 -\log(1-e^{-.002\pi})<51/10.
\]
Its value at \(x=0\) is zero. Hence at the forced-recurrence
starting point \(x=2\delta+\theta/N\), \(0\le\theta<1\), the
factorial upper exponent is at most \(10.2\delta+5.1/N\).
The absolute polynomial comparison with tolerance \(\delta\)
therefore gives left-weight rate at most \(11.2\delta\), with
the last \(5.1/N\) absorbed into a constant.

For the selected height \(h=.014\), reflection gives
\[
 -\Re g(x+ih)-2\pi h
 \le (5/2)x-\pi h<0\qquad(0\le x\le3\delta);
\]
the bound \(5/2\) follows from
\(-\log(1-e^{-.028\pi})<5/2\).
The normalized selected polynomial at the start has rate at most
\(\delta\). The two recurrence multipliers on the path are less
than \(1/2\); this follows uniformly from
\[
 1-e^{-.114\pi}+6\pi e^{.028\pi}\delta<1/2,\qquad
 e^{.028\pi}-1+6\pi e^{.028\pi}\delta<1/2.                      \tag{25}
\]
The normalized forcing is \(O(1/N)\) in either case. Thus the
left half-weight costs at most \(5.6\delta\), uniformly across
the entire strip. Combined with (24) this is less than
\(43\delta\). Every outward scalar margin in (19) exceeds
\(1/8000\), whereas \(43\delta<1/8000\). This proves the explicit
width with a strictly positive remaining exponential reserve.
All assertions are for sufficiently large \(N\); finitely many
smaller levels are absorbed by the uniform constant.

## 6. Remaining supporting-plane comparison

The local rates (12)--(13) and (19) are independent of the word length. To add
them to the existing central concavity estimate, one still needs a
comparison with the actual local geometric supporting plane, including
its linear terms, and control of the intervening outer region. Neither
comparison is asserted here. The triangle criterion (1)--(3) describes
an explicit height restriction under which the usual positive-form
argument can be extended; existence of a full source contour obeying
that restriction is a separate requirement.

## 7. Reproduction

```sh
python3 experiments/check_mixed_boundary_strip_bounds.py
```

The checker verifies the exact complex triangle determinant, the scalar
critical equations, all endpoint rate budgets, and their prescribed
root intervals, the six whole seam maxima, and thirty exact endpoint
polynomial coefficients. The all-level product and forcing arguments are written
above; no finite-kernel sampling is used as acceptance evidence.
