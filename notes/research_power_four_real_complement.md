# A real-index bound for the power-four finite source

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The symmetric two-index formula for the original power-four kernel
allows its real-index complement to be bounded before deforming any
contour. The reduction below is analytic: under explicit inequalities
on the two boundary parameters, the maximum over a triangle reduces
to four concave functions of one variable. At the alternating
three/four reference their tangent bounds lie below \(0.841\).
This note does not estimate the central complex contours or their
Fourier aliases.

## 1. The finite source and its real exponent

Use the [exact original formula](research_power_four_finite_source.md):
\[
 V_{4,N}(x,y)=\kappa^2 N c_xc_y
       \sum_{\substack{i,j\ge0\\i+j<N}}T_{ij}(X,Y),\qquad
 T_{ij}=
 \frac{X^iY^j(r;r)_{i+j}}
 {(r;r)_i(r;r)_j(X;r)_{i+1}(Y;r)_{j+1}},
 \tag{1}
\]
where \(r=e^{-2\pi i/N}\), \(X=e^{2\pi ix}\),
\(Y=e^{2\pi iy}\), and
\(c_x=N^{-1}e^{-\pi i(N-1)x}(1-X^N)\).
Let
\[
 \Delta=\{(s,t):s,t\ge0,\ s+t\le1\},\qquad
 a=\frac15,\quad b=\frac25,\quad B=[a,b]^2.
 \tag{2}
\]
For real \(0\le v\le1\), define
\[
 J(v)=\int_0^v\log(2\sin\pi u)\,du,\qquad
 I_A(v)=
 \frac{\operatorname{Li}_2(Ae^{-2\pi iv})
                       -\operatorname{Li}_2(A)}{2\pi i}.
 \tag{3}
\]
When \(|X|,|Y|<1\), the real exponential rate including
the cardinal prefactors is the continuous function
\[
 \begin{split}
 H_{X,Y}(s,t)={}&J(s+t)-J(s)-J(t)
       +s\log|X|+t\log|Y|\\
       &-\Re I_X(s)-\Re I_Y(t)
                     -\tfrac12\log|XY|.
 \end{split}
 \tag{4}
\]
The dilogarithms in (3) use their convergent disk branches.

## 2. A parameter region defined by algebraic inequalities

Let \(\mathcal R\) consist of \(A\) with \(0<|A|<1\) such that
\[
 \frac{\pi}{5}<\arg A<\frac{2\pi}{5},\qquad
 \frac1{2\cos(\pi/5)}
          <\frac{|A|}{|1-A|}<\sin(2\pi/5).
 \tag{5}
\]
These conditions are elementary algebraic inequalities on the real
and imaginary parts. For example, the squared ratio lies between
\((3-\sqrt5)/2\) and \((5+\sqrt5)/8\), and the sector
is bounded by the rays of slopes
\(\sqrt{5-2\sqrt5}\) and \(\sqrt{5+2\sqrt5}\).

**Theorem 1.** If \(X,Y\in\mathcal R\), then
\[
 \max_{\Delta\setminus(a,b)^2}H_{X,Y}
 \le
 \max_{\substack{c\in\{a,b\}\\a\le t\le b}}
       \{H_{X,Y}(c,t),\,H_{X,Y}(t,c)\}.
 \tag{6}
\]
Each of the four functions on the right is strictly concave.
In particular, its tangent at any one interior point is a global
upper bound on its entire interval.

*Proof.* Write \(R=|X|\), \(d=|1-X|\) and \(\theta=\arg X\).
The same argument applies to the other coordinate with parameter
\(Y\). Differentiating (4) in the interior gives
\[
 \partial_s H_{X,Y}
  =\log\frac{R\sin\pi(s+t)}
              {\sin\pi s\,|1-Xe^{-2\pi is}|}.
 \tag{7}
\]
For \(0\le s\le a\), the angles
\(\theta-2\pi s\) lie in \([-\theta,\theta]\), because
\(\theta>\pi a\). Thus
\[
             |1-Xe^{-2\pi is}|\le d\quad(0\le s\le a).
 \tag{8}
\]
For \(b\le s\le1\), the angles instead lie in
\([\theta-2\pi,-\theta]\), because \(\theta<\pi b\).
Hence the inequality reverses on that interval.

If \(s\ge b\), then
\(\sin\pi(s+t)/\sin\pi s\le1/\sin\pi b\):
on \(b\le s\le1/2\) use the bound one for the numerator;
on \(s\ge1/2\) the numerator is no larger than the denominator.
Equations (5), (7) and (8) therefore give
\(\partial_s H<0\). Reducing such a coordinate to \(b\)
keeps the point in \(\Delta\) and increases \(H\). If both
coordinates exceed \(b\), reduce both in turn.

Next suppose \(0<s\le a\) and \(a\le t\le b\). The sine
ratio is decreasing as a function of \(s\), since
\[
 \frac{\sin\pi(s+t)}{\sin\pi s}
                  =\cos\pi t+\cot\pi s\sin\pi t.
 \tag{9}
\]
At \(s=a\) the right side is a positive concave function of
\(t\in[a,b]\). Its two endpoint values are both
\(2\cos(\pi/5)\). The lower inequality in (5) now gives
\(\partial_s H>0\). Raising this small coordinate to \(a\)
therefore increases \(H\).

Finally, if \(0<s\le t\le a\), then
\(2s\le s+t\le2a<1/2\), so
\[
 \frac{\sin\pi(s+t)}{\sin\pi s}
       \ge 2\cos\pi s\ge2\cos\pi a.
 \tag{10}
\]
The smaller coordinate has positive derivative. Increase it
until the coordinates coincide, and then increase both to \(a\).
The case \(t\le s\) is the same with \(Y\). Continuity covers
the coordinate axes and the origin. These operations reduce
every point in the complement to one of the four edges in (6).

For an edge \(s=c\in\{a,b\}\), its second derivative is
\[
 \partial_t^2 H_{X,Y}(c,t)
   =-\frac{\pi\sin\pi c}
             {\sin\pi(c+t)\sin\pi t}
        +\frac{2\pi\Im(Ye^{-2\pi it})}
                    {|1-Ye^{-2\pi it}|^2}<0.
 \tag{11}
\]
The first term is negative. The second is nonpositive since
\(\arg Y-2\pi t\in(-3\pi/5,0)\).
The transposed edges have the same proof. This establishes
strict concavity and the tangent assertion. \(\square\)

## 3. The alternating reference and the original finite remainder

Let \(K=e^{2\pi ix_{34}}\) be the validated reference in
[the interface proof](research_three_four_source_interface.md).
Its original algebraic root enclosure gives
\[
 .365<\frac{\arg K}{\pi}<.367,\qquad
 .652<\frac{|K|}{|1-K|}<.653.
 \tag{12}
\]
In particular \(K\in\mathcal R\). At \(X=Y=K\) the transposed
edges coincide. For the two remaining edges take the rational
support points
\[
 t_a=\frac{312863}{10^6},\qquad
 t_b=\frac{2888}{10^4}.
 \tag{13}
\]
Direct outward evaluation of (3), (4) and (7) proves
\[
 H_{K,K}(c,t_c)+
 \max\{\partial_tH_{K,K}(c,t_c)(a-t_c),
       \partial_tH_{K,K}(c,t_c)(b-t_c)\}
                    <\frac{841}{1000},
           \qquad c\in\{a,b\}.
 \tag{14}
\]
These are tangent bounds for whole intervals, not a sample of
their values. Theorem 1 proves the same strict upper bound
over the entire real triangle outside the central square.
All four tangent bounds and the parameter conditions are
continuous in \(X,Y\), so the conclusion persists in a fixed
complex neighborhood of \((K,K)\).

**Corollary 2.** On a fixed neighborhood of \((x_{34},x_{34})\),
the part of the original finite sum (1) with
\((i/N,j/N)\notin(a,b)^2\), including its original prefactors,
has the bound
\[
 \left|\kappa^2Nc_xc_y
       \sum_{\substack{i,j\ge0,\ i+j<N\\
                     (i/N,j/N)\notin(a,b)^2}}T_{ij}(X,Y)\right|
              \le C N^d e^{841N/1000}.
 \tag{15}
\]
This holds along all integer levels and with every fixed wire
derivative on a smaller neighborhood. The same bound holds for
any subset of the displayed indices and for half-grid cuts
within \(O(N^{-1})\) of \(a,b\).

*Proof.* The uniform finite sine-factorial estimate gives
\[
 \log\prod_{l=1}^{k}2\sin(\pi l/N)
                     =NJ(k/N)+O(\log N),\quad 0\le k<N.
 \tag{16}
\]
It includes both factorial ends. It follows by subtracting
\(\log s+\log(1-s)\) from the integrand in (3), applying
the elementary factorial estimates to those two terms, and
using a smooth Riemann sum for the remainder.
The denominator logarithms are uniformly smooth because
\(|X|,|Y|\) stay below one. Thus (16) and their Riemann sums
bound each absolute original summand, with its prefactors,
by a polynomial times \(e^{NH_{X,Y}(i/N,j/N)}\).
There are at most \(N^2\) summands. The strict margin in (14)
proves (15), including after small parameter perturbations.

Uniform continuity of (4) on the closed triangle and the
strict tangent margin allow \(O(N^{-1})\) shifts of the cuts.
The partial finite sum is holomorphic in the boundary
parameters on this neighborhood. Cauchy estimates on a
slightly larger neighborhood prove the derivative assertion.
The proof used no parity restriction. \(\square\)

This removes the real-index complement from the remaining
power-four source problem. The central square still requires
its exact lattice contour, nonzero Gaussian coefficient, and
estimates for every vertical side and alias.
