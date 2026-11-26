# The full original four-vertex conditional on real neighboring indices

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The exact conditional sum at a four-crossing vertex has a nonzero
one-dimensional packet over its entire physical support, uniformly for
both neighboring index ratios in \([1/5,9/20]\). Its selected critical
height can have either sign. The proof keeps both Fourier aliases and
the endpoint currents. The source statement concerns physical integer
neighbors; it does not establish a packet at arbitrary complex
neighboring indices or for a whole mixed word.

## 1. Literal source, branches and statement

Let \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and let \(a,b\) be
physical integers with
\[
             \alpha=a/N,\quad\beta=b/N\in[1/5,9/20].
 \tag{1}
\]
The [exact conditional-leg identity](research_mixed_conditional_leg_sum.md)
gives
\[
 L_1(a,b)=\sum_{i=0}^{N-1-\max(a,b)}
           \frac{r^{-ai}P_{i+a}P_{i+b}}{P_i^3}.
 \tag{2}
\]
It retains the original crossing algebra, including its repeated
physical roots and normal data. In particular (2) is not obtained by
removing the forcing from the four-vertex moment recurrence.

Use \(J'(z)=\Log(2\sin\pi z)\) on \(0<\Re z<1\), with \(J\)
real on the real interval, and set
\[
 \begin{split}
 \varphi(z)&=\frac\pi2(z-z^2),\\
 F(s;\alpha,\beta)
   &=J(s+\alpha)+J(s+\beta)-3J(s)
          +i\pi\{s(\alpha-\beta)+(s^2-s)/2\},\\
 Q_4(s;\alpha,\beta)&=F(s;\alpha,\beta)
                             +i\varphi(\alpha)+i\varphi(\beta).
 \end{split}
 \tag{3}
\]
All three sine arguments below stay in that original strip.
The sine logarithms have positive-real-part arguments and their
principal lifts are unambiguous. The equivalent primitive used
for interval evaluation is
\[
 J(z)=\frac{\pi^2/6-\operatorname{Li}_2(e^{2\pi iz})}{2\pi i}
                           +\frac{i\pi}{2}z(1-z).
 \tag{4}
\]

**Theorem 1.** For every real pair (1), there is exactly one zero
\(s_*(\alpha,\beta)\) of the actual logarithmic derivative \(F_s\)
in the rectangle of Section 2. It satisfies
\[
             .24<\Re s_*<.34,\qquad -.17<\Im s_*<.01.
 \tag{5}
\]
Uniformly over all physical pairs (1), along both level parities,
\[
 L_1(a,b)=
 \frac{\sqrt{2\pi}\,A_4(s_*;\alpha,\beta)}
             {\sqrt{-F_{ss}(s_*;\alpha,\beta)}}
       e^{NQ_4(s_*;\alpha,\beta)}\{1+O(N^{-1})\},
 \tag{6}
\]
where
\[
 A_4(s;\alpha,\beta)=e^{i\pi(s-\alpha-\beta)/2}
       \frac{\sqrt{2\sin\pi(s+\alpha)}
             \sqrt{2\sin\pi(s+\beta)}}
                  {\{\sqrt{2\sin\pi s}\}^{3}}.
 \tag{7}
\]
The sine roots continue the positive real roots; the Hessian root
is its accretive branch. The coefficient is nonzero and uniformly
bounded above and away from zero. Thus \(L_1(a,b)\ne0\) for all
sufficiently large \(N\), uniformly in (1).

Dividing by the literal \(P_a^2P_b\) gives \(T_1\), and
multiplication by its original \(\kappa^2N\) gives a transfer
with power \(N^{-1/2}\). The sum \(L_1\) itself has power \(N^0\).
No ordinary boundary vector is replaced in this conditional statement.

## 2. A uniform complex middle rectangle

Put
\[
              l=\frac1{10},\qquad u=\frac9{20},\qquad
       \mathcal R=[l,u]+i[-1/5,1/5].
 \tag{8}
\]
For every pair (1), throughout \(\mathcal R\),
\[
                  -\Re F_{ss}>\frac13,\qquad |F_{ss}|<56.
 \tag{9}
\]
Indeed, writing \(s=x+ih\),
\[
 R(x,h)=\Re\cot\pi(x+ih)
       =\frac{\sin(2\pi x)}{\cosh(2\pi h)-\cos(2\pi x)}
 \tag{10}
\]
is positive for \(l\le x\le u\). If \(x+\alpha\ge1/2\),
then \(R(x+\alpha,h)\le0<R(x,h)\). Otherwise the sign of
their difference is the sign of
\[
       \cosh(2\pi h)\cos\pi(2x+\alpha)-\cos\pi\alpha.
 \tag{11}
\]
When \(2x+\alpha\ge1/2\), this is negative directly. In the
remaining range it decreases with both \(x\) and \(\alpha\).
Its maximum is at \(x=1/10,\alpha=1/5\), and is negative because
\[
                 \cosh(2\pi/5)\cos(2\pi/5)<\cos(\pi/5).
 \tag{12}
\]
The same applies to \(\beta\), giving
\(-\Re F_{ss}>\pi R(x,h)\). At fixed \(|h|\), the only
possible interior extremum of \(R\) is a maximum. Its smaller
endpoint value is at \(u\), and therefore
\[
 \pi R(x,h)\ge
 \frac{\pi\sin(\pi/10)}{\cosh(2\pi/5)+\cos(\pi/10)}>\frac13.
 \tag{13}
\]
For every sine argument in the rectangle,
\(|\cot\pi z|\le\cot(\pi/10)\). Hence
\[
                  |F_{ss}|\le\pi\{5\cot(\pi/10)+1\}<56.
 \tag{14}
\]
The focused checker verifies the strict scalar margins.

Integrating \(F_{ss}\) along a segment and pairing with its
conjugate difference proves that \(F_s\) has at most one zero
in this convex complex rectangle. Every horizontal line through
such a zero obeys
\[
 \Re F(x+i\Im s_*)\le M-\frac16(x-\Re s_*)^2,\qquad
                       M=\Re F(s_*).
 \tag{15}
\]
At fixed \(x\), \(\Re F(x+ih)\) is strictly convex in \(h\).

## 3. The compact root and action certificate

The [outward certificate](../experiments/certify_mixed_four_conditional_packet.py)
covers the whole closed parameter square (1) by dyadic rectangles.
Every rectangle has a complex Newton self-map for the actual \(F_s\),
not just its exponential. It also proves
\[
              M-\Re F(l;\alpha,\beta)>\frac1{50},\qquad
              M-\Re F(u;\alpha,\beta)>\frac1{50}.
 \tag{16}
\]
These compare the two actions at the same parameters.

A numerical root only proposes a rational center \(s_c\). A point
Newton square of radius \(10^{-40}\) is checked first. On the
whole parameter rectangle, the recorded radius \(r\) satisfies,
for a fixed inverse derivative \(B\),
\[
 \|1-BF_{ss}\|_\infty<\frac12,\qquad
       \|BF_s(s_c)\|_\infty+r\|1-BF_{ss}\|_\infty<r.
 \tag{17}
\]
Complex multiplication uses its real two-dimensional row norm.
The square lies strictly inside (5). Banach's theorem gives a
zero for every parameter in the rectangle; (9) identifies the
zeros on overlaps.

The action at the rectangle center uses the point root enclosure.
The parameter derivatives of either endpoint gap
\(D_c=\Re\{F(s_*)-F(c)\}\), \(c=l,u\), are exactly
\[
 \begin{split}
 \partial_\alpha D_c
   &=\Re\{\Log(2\sin\pi(s_*+\alpha))
            -\Log(2\sin\pi(c+\alpha))+i\pi(s_*-c)\},\\
 \partial_\beta D_c
   &=\Re\{\Log(2\sin\pi(s_*+\beta))
            -\Log(2\sin\pi(c+\beta))-i\pi(s_*-c)\}.
 \end{split}
 \tag{18}
\]
The stationary equation eliminates the derivative of \(s_*\).
Interval bounds for (18), multiplied by the two half-widths,
are subtracted from the point gap. Each result exceeds \(1/50\).
An exact binary-tree audit proves coverage. No sampled root or
sampled action establishes (5) or (16).

The equivalent algebraic equation is
\[
 (1-AU)(1-BU)=A(1-U)^3,\quad
 A=e^{-2\pi i\alpha},\ B=e^{-2\pi i\beta},\
 U=e^{-2\pi is_*}.
 \tag{19}
\]
Its polynomial is
\((1-A)+(2A-B)U+A(B-3)U^2+AU^3\).
The actual zero logarithmic lift is checked directly; no root
is selected by its height sign.

## 4. Both real tails of the original sum

On \(0<s<1-\max(\alpha,\beta)\),
\[
 \partial_s\Re F
  =\log\frac{\sin\pi(s+\alpha)\sin\pi(s+\beta)}
                         {2\sin^3\pi s}.
 \tag{20}
\]
For \(0<s\le l\), the numerator sines are at least
\(\sin(\pi/5)\), whereas the denominator is at most
\(2\sin^3(\pi/10)<\sin^2(\pi/5)\). The entropy increases
to the left cut. For \(u\le s\le1/2\), the derivative is
negative because \(2\sin^3(9\pi/20)>1\). For \(s\ge1/2\),
both numerator sines are at most \(\sin\pi s\), and
\(\sin\pi s\ge\sin(\pi/5)>1/2\), since \(s\le4/5\).
The entropy decreases on the whole right tail.

The uniform physical estimate
\(\log S_j=NJ(j/N)+O(\log N)\), including \(j=0,N-1\),
and (16) bound both omitted tails by
\[
                       \operatorname{poly}(N)e^{N(M-1/50)}.
 \tag{21}
\]
The first and last physical rows are included. We may choose
physical half-grid cuts \(l_N,u_N\) tending to \(l,u\).
All strict compact inequalities persist with slightly smaller
margins, uniformly for sufficiently large \(N\).

## 5. Original cotangent contour, both aliases and all endpoints

Interpolate the factors of (2) by their original marked factorials
from [the exact interpolation theorem](exact_factorial_interpolation_and_complex_contours.md).
The resulting literal summand \(\mathcal T_N(s)\) is holomorphic
on a fixed neighborhood of all rectangles below and agrees with
every enclosed physical summand. Uniformly on that compact set,
\[
 \mathcal T_N(s)=N^{-1/2}A_4(s;\alpha,\beta)
                         e^{NQ_4(s;\alpha,\beta)}\{1+O(N^{-1})\}.
 \tag{22}
\]
Indeed \(P_j=e^{iN\varphi(j/N)-i\pi j/(2N)}S_j\).
The two numerator and three denominator factorials give
\(N^{-1/2}\); their roots and order-one phase are exactly (7).

Write \(\eta_*=\Im s_*\), and choose
\[
 \varepsilon=10^{-5},\quad Y=|\eta_*|+\varepsilon<1/5,\quad
 \sigma=\operatorname{sign}(\eta_*),
 \quad \sigma=1\ \hbox{when }\eta_*=0.
 \tag{23}
\]
On the counterclockwise rectangle \([l_N,u_N]+i[-Y,Y]\),
the exact residue formula is
\[
 \sum_{l_N<i/N<u_N}\mathcal T_N(i/N)
       =\frac{N}{2i}\oint\mathcal T_N(s)\cot(\pi Ns)\,ds.
 \tag{24}
\]
Split the cotangent into its upper constant \(-i\), lower
constant \(i\), and their remainders. The constant contribution
is exactly \(N\int_{l_N}^{u_N}\mathcal T_N(x)\,dx\).
Its deformation to height \(\eta_*\) retains
\[
 N\int_{l_N}^{l_N+i\eta_*}\mathcal T_N(s)\,ds
       -N\int_{u_N}^{u_N+i\eta_*}\mathcal T_N(s)\,ds.
 \tag{25}
\]
The horizontal zero-mode coefficient is exactly \(+N\).
Each horizontal cotangent remainder is bounded by
\(Ce^{-2\pi NY}\). On the vertical half-grid sides its bound
is \(2e^{-2\pi N|h|}\), including near \(h=0\), since the
denominator there is \(1+e^{-2\pi N|h|}\).

By (9), (15), and \(F_s(s_*)=0\),
\[
 \Re F(x+i\sigma Y)
 \le M-\frac16d^2+56\varepsilon|d|+28\varepsilon^2
 \le M+4732\varepsilon^2,\qquad d=x-\Re s_*.
 \tag{26}
\]
Reflection is exact:
\[
 \Re F(x-ih)-\Re F(x+ih)
                      =2\pi h(\alpha-\beta+x-1/2).
 \tag{27}
\]
The parenthesized coefficient has absolute value at most \(3/4\)
on the retained interval. Both horizontal alias exponents are
therefore bounded by
\[
 M+4732\varepsilon^2-\frac\pi2Y
                      \le M-\frac1{100000}.
 \tag{28}
\]
The last scalar inequality has a strict margin and holds through
the change of sign of \(\eta_*\).

At either unrounded endpoint \(|d|>.11\). Equation (26) gives
\[
 \Re F(c+i\sigma Y)
 \le M-\frac{(.11)^2}{6}
               +56\varepsilon(.11)+28\varepsilon^2
 <M-\frac1{600},\qquad c=l,u.
 \tag{29}
\]
Together with (16), height convexity bounds the entire same-side
endpoint segment from zero to \(\sigma Y\) by this rate.
Reflection (27) and the alias penalty bound the opposite segment
by the same rate. The currents (25) are subsegments of the former
ones and satisfy the same bound without an alias penalty.
This includes every vertical side and corner. Half-grid rounding
preserves uniform strict gaps; all final remainder gaps may be
replaced by \(1/200000\).

## 6. Gaussian coefficient and scope

The horizontal zero mode has the unique maximum (15).
Its original factorial arguments stay in a fixed compact subset
of their strips. Gaussian integration of (22) gives
\[
 N\cdot N^{-1/2}\sqrt{\frac{2\pi}{N}}\,
      \frac{A_4(s_*)}{\sqrt{-F_{ss}(s_*)}}
                  e^{NQ_4(s_*)}\{1+O(N^{-1})\}.
 \tag{30}
\]
This is (6), with every scalar power retained. The cubic
correction is odd on a symmetric local cutoff, and the analytic
expansion gives a uniform relative \(O(N^{-1})\) error.
Equations (21), (25), and (28)--(29) bound the entire remainder
strictly below this action.

The saddle and coefficient vary analytically as classical
functions near the real parameter square. The finite-source
assertion remains the physical-neighbor statement (1). No
varying-degree polynomial has been continued to complex neighbors,
and no remaining cyclic or ordinary-boundary sum is estimated.

Reproduce the compact certificate with:

    python3 experiments/certify_mixed_four_conditional_packet.py --precision 256

The record stores every accepted dyadic rectangle and rational
Newton center. The written comparisons supply the all-level
contour argument; the certificate supplies the full-parameter
root and its two endpoint action gaps.
