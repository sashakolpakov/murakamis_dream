# Zero-safe color tubes for the original Newton polynomials

Research deduction, 5 November 2026. The complete real-color entropy
bound is already proved in
[Newton evaluation on the real boundary period](research_three_crossing_real_period_newton_bound.md),
Lemmas 1--3. This note adds a quantitative complex-color tube and
pointwise bounds for all fixed ordinary derivatives, without dividing
by a Newton polynomial or a possibly zero product factor. It also
records literal triangular bounds for the original endpoint factors.
These are absolute upper bounds, not a lower bound for a contracted
source.

## 1. The existing real envelope

Retain the original normalization
\[
 S_l=\prod_{j=1}^l2\sin(\pi j/N),\qquad
 c_j=2\cos\frac{(2j+1)\pi}{N},\qquad
 e_l(w)=S_l^{-2}\prod_{j=0}^{l-1}(c_j-w),
 \quad 0\le l<N.                                      \tag{1}
\]
Let
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\quad
 f(t)=\log(2|\cos\pi t|),\quad
 A(u,y)=\int_{y-u}^{y+u}f(t)\,dt.                       \tag{2}
\]
The logarithmic singularities are integrable. For
\(w_0=-2\cos\theta\), \(0\le\theta\le\pi\), put
\[
 y=\frac{\theta}{2\pi},\qquad
 V_\theta(u)=A(u,y)-2J(u),\qquad 0\le u\le1.             \tag{3}
\]
The cited real-envelope theorem proves, uniformly in every original
row, angle and level parity,
\[
 |e_l(w_0)|\le C N^A e^{N V_\theta(l/N)}.                \tag{4}
\]
It also proves
\[
 0\le V_\theta(u)\le V_0(u)\quad(0\le u\le1/2),
 \qquad V_\theta(1-u)=-V_\theta(u).                    \tag{5}
\]
Thus all upper-half rows have nonpositive real-color entropy. These
facts include exact zeros and do not use positivity of coefficients
in a later contraction.

Fix constants \(C_F,A_F\) from the already proved uniform factorial
bound, so that
\[
 S_l^{-2}\le C_F N^{A_F}e^{-2NJ(l/N)}
                       \quad(N\ge2,\ 0\le l<N).         \tag{6}
\]
No new factorial estimate is needed below.

## 2. A quantified complex tube

**Theorem 1.** For every \(0<\delta\le1\), every
\(|w-w_0|\le\delta\), every \(N\ge2\), and every original
row \(0\le l<N\),
\[
 |e_l(w)|\le C_F N^{A_F}
       \left(\frac{4+\delta}{\delta}\right)^2
       \exp\left\{N\left[V_\theta(l/N)
                   +2\operatorname{arsinh}(\sqrt\delta/2)\right]\right\}.
                                                               \tag{7}
\]
In particular the excess rate is at most \(\sqrt\delta\), with
the explicit prefactor at most \(25C_F N^{A_F}\delta^{-2}\).

*Proof.* At \(t_j=(j+1/2)/N\), the exact numerator factor is
\[
 c_j-w_0=a(t_j)b(t_j),\quad
 a(t)=2\cos\pi(t+y),\quad b(t)=2\cos\pi(t-y).
\]
For any real \(a,b\),
\[
 |ab|+\delta\le\sqrt{(a^2+\delta)(b^2+\delta)},          \tag{8}
\]
because the squared difference is
\(\delta(|a|-|b|)^2\ge0\). Define the smooth periodic function
\[
 f_\delta(t)=\tfrac12\log(4\cos^2\pi t+\delta).
\]
It has total variation on one period exactly
\(\log((4+\delta)/\delta)\). For a function of bounded variation,
the error between a midpoint sum and \(N\) times the integral over
the corresponding union of mesh cells is at most its total variation
on that union. The union here has length \(l/N\le1\), and its
variation is at most the one-period variation, independently of the
shift. Applying this separately to the two terms in (8) gives
\[
 \log\left|\prod_{j<l}(c_j-w)\right|
 \le N\int_0^{l/N}[f_\delta(t+y)+f_\delta(t-y)]\,dt
                    +2\log\frac{4+\delta}{\delta}.       \tag{9}
\]
The left side may be minus infinity; the inequality still holds.

The integrand difference \(f_\delta-f\) is nonnegative, periodic,
and has the exact full-period integral
\[
 \int_0^1(f_\delta(t)-f(t))\,dt
                 =\operatorname{arsinh}(\sqrt\delta/2). \tag{10}
\]
For example, differentiating in \(\delta>0\) gives
\(1/(2\sqrt{\delta(\delta+4)})\) on both sides, and the
integrals tend to zero as \(\delta\downarrow0\). The elementary
integral for the derivative follows by \(v=\tan\pi t\) on the
two half-periods. Each shifted interval in (9) has length at most
one, so its excess is at most (10). The unregularized sum of its
two integrals is precisely \(A(l/N,y)\). Combine (9), (10), and
(6) to obtain (7). Finally
\(2\operatorname{arsinh}(\sqrt\delta/2)\le\sqrt\delta\).
\(\square\)

**Corollary 2 (ordinary derivatives at every real color).** For each
fixed nonnegative integer \(k\),
\[
 |e_l^{(k)}(w_0)|
 \le25e C_F k!\,N^{A_F+4+2k}
                    e^{N V_\theta(l/N)}.                \tag{11}
\]
The constants are uniform over all rows, real colors and level
parities, including colors where \(e_l\) vanishes.

Apply Cauchy's formula to the entire polynomial on the circle of
radius \(\delta=N^{-2}\). Its tube rate cost in (7) is at most
\(N\sqrt\delta=1\), its extra prefactor is at most \(25N^4\),
and Cauchy's derivative cost is \(k!N^{2k}\). No quotient by a
Newton factor occurs. This also explains why the real upper-half
bound remains polynomial for every fixed derivative, even at an
exact finite zero whose derivative does not vanish.

## 3. A sharp compact-row color deficit

For \(u\in(0,1/2)\), let
\(D(u,y)=A(u,0)-A(u,y)\). The monotonicity proof behind (5)
gives
\[
 D_y(u,y)=\log\left|
                 \frac{\cos\pi(u-y)}{\cos\pi(u+y)}\right|>0
                         \quad(0<y<1/2),                \tag{12}
\]
away from its integrable singularity. If \(u+y<1/2\), then
\[
 D_y(u,y)=2\operatorname{artanh}(\tan\pi u\tan\pi y)
                      \ge2\pi\tan\pi u\,y.              \tag{13}
\]
Consequently, for any fixed \(0<a\le b<1/2\),
\[
 D(u,y)\ge \pi\tan(\pi a)
                 \min\{y^2,(1/2-b)^2\}
       \quad(u\in[a,b],\ 0\le y\le1/2).                \tag{14}
\]
First integrate (13) up to \(y\le1/2-b\), including the endpoint
by continuity; for larger \(y\), use (12). Uniformly on the compact
row interval,
\[
 D(u,y)=\pi\tan(\pi u)y^2+O_{a,b}(y^4)\quad(y\to0).    \tag{15}
\]
Indeed \(A_{yy}(u,0)=-2\pi\tan(\pi u)\). Thus the
coefficient \(\pi\tan(\pi a)\) in the local quadratic part of
(14) is sharp uniformly on \([a,b]\).

Combining (7) with (14) preserves any strict real-color absolute-rate
gap when the tube radius is sufficiently small. Combining (11) with
(14) preserves the same real-color exponent for fixed ordinary
derivatives. Neither assertion compares a signed contracted source
with its own value at completeness.

## 4. The literal endpoint triangular envelopes

Use exactly the endpoint polynomials in
[mixed torus composition](research_mixed_conditional_torus_composition.md),
equation (21):
\[
\begin{split}
 r&=e^{-2\pi i/N},\quad q=e^{\pi i/N},\quad
 P_j=(r;r)_j,\quad p_i(X)=(rX;r)_i,\\
 H_N(w,Y)&=\sum_{l=0}^{N-1}
          \frac{(-q)^{-l}e_l(w)}{P_l}(Y;r)_l,\\
 U_{\epsilon,N}(w,X)&=\sum_{i=0}^{N-1}
                \frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\epsilon}}.
\end{split}                                                   \tag{16}
\]
Set \(C_k(N)=25e C_F k!N^{A_F+4+2k}\). For arbitrary complex
\(X,Y\), the same original finite sums satisfy
\[
\begin{split}
 |\partial_w^k H_N(w_0,Y)|
 &\le C_k(N)\sum_{l<N}
        \frac{|(Y;r)_l|}{S_l}e^{N V_\theta(l/N)},\\
 |\partial_w^k U_{\epsilon,N}(w_0,X)|
 &\le C_k(N)\sum_{0\le l\le i<N}
        \frac{|p_i(X)|}{S_i^\epsilon S_lS_{i-l}}
                                   e^{N V_\theta(l/N)}.
\end{split}                                                   \tag{17}
\]
The first line follows term by term from (11). For the second, use
the exact physical-index identity
\[
 |(r^{-i};r)_l|=
 \begin{cases}S_i/S_{i-l},&l\le i,\\0,&l>i,\end{cases}   \tag{18}
\]
inside (16), then apply the triangle inequality. This deletion of
\(l>i\) is an exact zero of the original physical factor, not an
off-grid support assumption. The private index \(i\) still runs
over all \(0,\ldots,N-1\), and no row of the general \(H_N(w,Y)\)
is deleted.

For the undifferentiated polynomials on a fixed complex tube, the
corresponding bounds use the prefactor and common excess from (7)
instead of \(C_0(N)\). Fixed derivatives on a smaller tube follow
by Cauchy's formula, with its stated radius cost. Restricting the
Newton index \(l/N\) in either positive majorant to \([a,b]\)
gives the explicit factor \(e^{-ND(l/N,y)}\) relative to its
complete-color majorant, with (14) as a uniform lower bound.
The other Newton rows retain their own rates from (5).

The factors \(d_N(X)\) and \(1+X^{-N}\) in the original torus
composition are untouched. One may multiply these upper bounds by
their literal moduli or by already proved full upper envelopes.
No Fourier factor is divided out and no cancellation or nonzero
leading coefficient for the complete \(H_N\), \(U_{\epsilon,N}\),
or the contracted open word is inferred. A strict absolute-source
gap can survive this operation; a signed-source lower bound still
requires its own complete contour argument.
