# The entire even low-demand range: a subexponential signed contraction

31 October 2026. analytical theorem. This extends the low-quarter estimate using its exact original-source recurrence. It
retains the original two half-block cutoffs. The conclusion is
subexponential, not a polynomial estimate, and does not cover odd levels
or the remaining projected middle-demand range.

## 1. Statement and exact scalar reduction

Let \(N=2m\ge4\), \(M=m-1\), \(d=N-1\), and \(\theta=\pi/N\).
Use the original fixed-pair cap/CROSS coefficient \(S_{N,n}\), endpoint
comparator \(D_{N,n}\), and coefficient \(C_{0,n}>0\) of
[the Newton source theorem](research_cap_cross_low_demand_newton_contraction.md).
In particular the original \(A^d\) demand, unused products, raw signs,
and actual spectral pair \((+2,-2)\) have not changed.

**Theorem.** Uniformly over the whole original low range,
\[
 \limsup_{\substack{N\to\infty\\N\ {\mathrm{even}}}}
 \frac1N\log\max_{0\le n\le M}
       \frac{|S_{N,n}|}{D_{N,n}}\le0.                    \tag{1}
\]
Equivalently, for every \(\varepsilon>0\), all sufficiently large even
\(N\) obey \(|S_{N,n}|\le e^{\varepsilon N}D_{N,n}\) for every
\(0\le n\le M\). The threshold may depend on \(\varepsilon\).

The exact source theorem gives
\[
 R_n=\frac{\gamma_n S_{N,n}}{4C_{0,n}},\quad
 R_0=1,\quad R_n=1-t_nR_{n-1},\qquad
 t_n=\frac{4\sin^4(n\theta)}{\sin^2((2n-1)\theta)},
 \quad\gamma_n=2-2\cos((2n+1)\theta).                    \tag{2}
\]
For this range the original cutoff is precisely
\(J_n=\{\max(0,n-M),\ldots,\min(M,n)\}=\{0,\ldots,n\}\).
The auxiliary full slice therefore equals the original projected sum.
No such identification is used above \(M\).

Write
\[
 P_0=1,\quad P_j=\prod_{r=1}^j t_r,\quad A_j=P_j^{-1}.
 \qquad
 R_n=(-1)^n P_n\sum_{j=0}^n(-1)^j A_j.                 \tag{3}
\]
The elementary sine products and monotonicity of \(t_r\) give
\[
 P_M=\frac{N^2\sin^2(\pi/N)}4,\qquad
             0<P_j\le\pi^2/4\quad(0\le j\le M).        \tag{4}
\]
Indeed \(\prod_{r=1}^{m-1}4\sin^2(r\theta)=m\), whereas
\(\prod_{r=1}^{m-1}4\sin^2((2r-1)\theta)=1/\sin^2\theta\).
Moreover
\(\partial_v\log t(v)=4\theta[\cot(v\theta)-\cot((2v-1)\theta)]
\ge0\) for \(1\le v\le M\). Thus \(\log P_j\) is convex and its
maximum occurs at an endpoint. This alone does not bound the signed
sum in (3).

## 2. Exact endpoint factors and an analytic interpolant

Define the removable-value functions
\[
 g(t)=\frac{\sin(2\pi t)}{2\pi t(1-2t)},\qquad
 s(t)=\frac{\sin(\pi t)}{\pi t}.
\]
Both are positive on \([0,1/2]\). They have holomorphic logarithms
\(L_g,L_s\), real there, throughout the vertical strip
\(-1/2<\Re t<1\). For \(g\), the zeros at \(0,1/2\) have been
removed and the next zeros are \(-1/2,1\); for \(s\), the next zeros
are \(-1,1\).

Direct factorization of every sine in \(A_j\) yields exactly
\[
 A_j=
 \left(\frac2\pi\right)^{2j}
 \frac{\Gamma(j+1/2)^2\Gamma(m+1/2)^2}
      {\pi\,\Gamma(j+1)^4\Gamma(m-j+1/2)^2}
 \exp\!\left\{
 2\sum_{r=1}^jL_g((r-1/2)/N)
 -4\sum_{r=1}^jL_s(r/N)\right\}.                        \tag{5}
\]
This retains both real endpoint singularities in exact Gamma factors.

Fix any finite \(Y>0\), and use Cauchy radius \(\rho=1/5\).
All derivatives of \(L_g,L_s\) on the rectangles needed below obey
\[
 |L^{(k)}(t)|\le M_Y\,k!\rho^{-k},                       \tag{6}
\]
where \(M_Y\) is finite and independent of \(N\). One may obtain (6)
by taking a slightly larger fixed rectangle inside the indicated
zero-free vertical strip. Let \(p=\lfloor\pi\rho N\rfloor\).
For all sufficiently large \(N\) define
\[
\begin{aligned}
 \mathcal{E}_{1/2,N}(L;u)
 &=N\int_0^uL(t)\,dt+
   \sum_{k=1}^{p-1}
    \frac{B_{2k}(1/2)}{(2k)!\,N^{2k-1}}
          [L^{(2k-1)}(u)-L^{(2k-1)}(0)],\\
 \mathcal{E}_{1,N}(L;u)
 &=N\int_0^uL(t)\,dt+\frac{L(u)-L(0)}2+
   \sum_{k=1}^{p-1}
    \frac{B_{2k}}{(2k)!\,N^{2k-1}}
          [L^{(2k-1)}(u)-L^{(2k-1)}(0)].
\end{aligned}                                          \tag{7}
\]
Here the integrals use the analytic primitive on that strip.
At \(u=j/N\), the two formulas approximate respectively the midpoint
and right-endpoint sums in (5).

For precision, the shifted Euler--Maclaurin remainder, the bound
\(\sup_x|B_{2p}(\{x\})|\le4(2p)!/(2\pi)^{2p}\), and (6) give
\[
 |{\mathrm{remainder}}|
 \le C_Y N\,\frac{(2p)!}{(2\pi\rho N)^{2p}}
 =\exp[-(2\pi\rho+o(1))N]                              \tag{8}
\]
uniformly for every real integer \(0\le j\le M\).
The same bound holds for the translated periodic Bernoulli remainder
of the midpoint sum. The omitted next endpoint correction, if the
chosen remainder convention includes it, has the same exponential
bound and is absorbed in (8).
Since \(2\pi/5>6/5\), the combined error in the exponent of (5)
is at most \(e^{-6N/5}\) for sufficiently large \(N\).

Replace the two sums in (5) by (7), with \(u=z/N\), and call the
resulting function \(\mathcal{A}_N(z)\). It is analytic on
\[
 -1/4\le\Re z\le M+1/4,\qquad |\Im z|\le NY
\]
and a neighborhood of that rectangle. The numerator Gamma poles start
at \(z=-1/2\); the other numerator Gamma factor is constant. Reciprocal
Gamma factors introduce no poles. All analytic logarithms in (7)
remain in their stated strip. Equation (8) gives the nodal estimate
\[
 \mathcal{A}_N(j)=A_j\exp(e_{N,j}),\qquad
       |e_{N,j}|\le e^{-6N/5},\quad0\le j\le M.          \tag{9}
\]
No guessed degree interpolation is used: the values are matched with
an explicit exponentially controlled error.

## 3. Uniform complex growth, including the endpoint layers

Put
\[
 f(u)=-\int_0^u\log\tan(\pi t)\,dt,\qquad0\le u\le1/2.
\]
Use its analytic continuation to \(0<\Re u<1/2,\Im u>0\),
with the logarithm continued from the positive real tangent. Reflect
by conjugation below the real axis. The primitive has continuous
boundary values on both vertical edges of this strip.

The derivative bound (6) also shows, uniformly for complex
\(u\) in any fixed-height rectangle considered here,
\[
 \mathcal{E}_{1/2,N}(L;u)=N\int_0^uL+O_Y(N^{-1}),\qquad
 \mathcal{E}_{1,N}(L;u)=N\int_0^uL+\tfrac12[L(u)-L(0)]
                                      +O_Y(N^{-1}).     \tag{10}
\]
For example the correction terms are bounded by constant multiples
of \(N(2k-1)!/(2\pi\rho N)^{2k}\). Up to half the optimal truncation
their successive ratios are bounded below one; the remaining terms
are exponentially small. The differentiated corrections are bounded
as well. No estimate uniform as \(Y\to\infty\) is asserted.

Uniform Stirling estimates in the right half-plane, applied to the
exact Gamma factors in (5), now give
\[
 \log|\mathcal{A}_N(x+iNy)|
      =N\Re[2f(x/N+iy)]+O_Y(\log N),
 \quad0\le x\le M,\quad |y|\le Y.                      \tag{11}
\]
Here and below the lower half-plane uses the conjugate branch.
There is no unbounded-endpoint Stirling substitution: for
\(\Re w\ge0, |w|\le C_YN\),
\[
 \log\Gamma(w+a)=w\log w-w+O_Y(\log N),
 \qquad a=1/2\text{ or }1,
\]
with \(w\log w=0\) at zero. For \(|w|\le1\) this follows directly
from the analytic nonzero Gamma function; outside that disk it is the
uniform sectorial Stirling formula. Apply this to \(w=z,m,m-z\).
Their real parts are nonnegative on (11).

One can also check the leading primitive without any Stirling constant
ambiguity. The Gamma contribution has derivative
\(2\log[(1-2u)/(\pi u)]\), while the smooth-product contribution has
derivative \(2L_g(u)-4L_s(u)\). Their sum is exactly
\(-2\log\tan(\pi u)\), and their value at \(u=0\) is zero.

On the full slightly enlarged \(z\)-rectangle,
\[
             |\partial_z\log\mathcal{A}_N(z)|=O_Y(\log N). \tag{12}
\]
All Gamma arguments have real part at least \(1/4\), their digammas
are \(O_Y(\log N)\), and (6)--(7) give the same bound for the smooth
factor. Thus moving \(x\) by at most \(1/4\) in (11) changes its real
logarithm by only \(O_Y(\log N)\). This handles the left vertical
contour at \(-1/4\) without choosing a logarithm across the endpoint
singularity of \(f\). The right contour is handled in the same way.
At real nodes, (9)--(11) in particular give
\[
 \log A_j=2Nf(j/N)+O(\log N),\qquad
 \log P_j=-2Nf(j/N)+O(\log N),                          \tag{13}
\]
uniformly down to \(j=0\) and up to \(M\).

For \(0\le u\le1/2\), \(y\ge0\), define
\[
 h(u,y)=\Re[2f(u+iy)]-\pi y .
\]
For \(0<u<1/2,y>0\), the tangent has positive real and imaginary
parts. Hence
\[
 \partial_yh=2\arg\tan(\pi(u+iy))-\pi<0,\qquad
       h(u,y)\le2f(u).                                 \tag{14}
\]
The boundary values satisfy \(h(0,y)=h(1/2,y)=0\).
For \(y>0\) the absolutely convergent series is
\[
 h(u,y)=\frac2\pi
  \sum_{\substack{k\ge1\\ k\ {\mathrm{odd}}}}
       \frac{e^{-2\pi ky}\sin(2\pi ku)}{k^2}.            \tag{15}
\]
It follows either by integrating
\(-\log\tan(\pi z)=-i\pi/2+
2\sum_{k\ {\mathrm{odd}}}e^{2\pi ikz}/k\), with its value at zero,
or by differentiating and matching the boundary value. Consequently
\[
 \sup_{0\le u\le1/2}|h(u,Y)|\le
 \epsilon_Y:=
 \frac{2e^{-2\pi Y}}{\pi(1-e^{-4\pi Y})}
                  \longrightarrow0.                  \tag{16}
\]

## 4. Alternating residues and the uniform subexponential bound

For each \(0\le n\le M\), take the rectangle with real edges
\(-1/4,n+1/4\) and imaginary edges \(\pm NY\).
The poles of \(\pi/\sin(\pi z)\) enclosed are exactly the integers
\(0,\ldots,n\), with residues \((-1)^j\). Therefore
\[
 \sum_{j=0}^n(-1)^j\mathcal{A}_N(j)
  =\frac1{2\pi i}\oint
     \frac{\pi\mathcal{A}_N(z)}{\sin(\pi z)}\,dz.           \tag{17}
\]
There are no poles of the interpolant in this contour.
On the vertical edges
\(|\sin(\pi z)|^{-1}\le C e^{-\pi|\Im z|}\);
the same holds on the horizontal edges for large \(N\).

Multiply (17) by \(P_n\). On the left edge use (4), (11)--(12),
and \(h(0,y)=0\). Its integral is at most a fixed \(Y\)-dependent
power of \(N\). On the right edge use (13)--(14):
the exponent is bounded by
\[
       N[h(n/N,|y|)-2f(n/N)]+O_Y(\log N)\le O_Y(\log N).
\]
The shift from \(n\) to \(n+1/4\) costs only (12). Thus this integral
has the same polynomial bound. On either horizontal edge use (4),
(11)--(12), and (16). The integral is bounded by
\[
                       N^{C_Y}e^{N\epsilon_Y}.          \tag{18}
\]
All estimates are uniform in \(n\), including \(n=0\).

The nodal replacement error in (9) is exponentially negligible even
after absolute values. Indeed \(f\) is maximal at \(1/4\), and
\[
 2f(1/4)\le\frac{1+\log2}{2}<1
\]
by \(\tan(\pi t)\ge2t\) on \(0<t\le1/4\).
Equations (4), (9), and (13) imply
\[
 P_n\sum_{j=0}^n|\mathcal{A}_N(j)-A_j|
             \le e^{-N/5+O(\log N)}.                  \tag{19}
\]
Combining (3), (17)--(19) gives, for every fixed \(Y>0\),
\[
 \max_{0\le n\le M}|R_n|
          \le N^{C_Y}e^{N\epsilon_Y}
                         +e^{-N/5+O(\log N)}.          \tag{20}
\]
First let the even level tend to infinity with \(Y\) fixed, and only
then let \(Y\to\infty\). Equation (16) proves
\[
 \limsup_{\substack{N\to\infty\\N\ {\mathrm{even}}}}
       \frac1N\log\max_{0\le n\le M}|R_n|\le0.          \tag{21}
\]
This does not require any \(Y\)-uniform Stirling or interpolation
constant, nor a scaled contour height \(Y\) growing with \(N\).

Finally the original positive comparator contains
\(V_0C_{0,n}=4C_{0,n}/a_0\), where \(a_0=2+2\cos\theta\).
Thus, exactly as in the quarter-range proof,
\[
 \frac{|S_{N,n}|}{D_{N,n}}
       \le\frac{a_0}{\gamma_n}|R_n|
       \le N^2 |R_n| .
\]
This and (21) prove (1). The recorded raw common sign does not affect
the modulus. No other face demand or power has been altered.

## 5. Scope

This is a cancellation estimate for the actual fixed spectral pair
and every original even low-demand coefficient \(0\le n\le M\).
It is stronger than a coefficient-norm or residue-variation bound:
those can be exponentially excessive in this same problem.
The new argument retains the alternating sign through the contour.

The low-quarter theorem still provides its sharper polynomial
factor there. The present proof does not establish a polynomial bound
on the whole low range. It also does not identify the auxiliary full
slice with the original projected sum when \(n>M\), prove the analogous
odd-level low bound, control nearby complex spectra, or give a whole
source/filling theorem. Those are separate tasks.

The source input is the exact Newton recurrence with its original cutoff. The analytical estimates are (5)–(20). The [odd extension](research_cap_cross_odd_low_demand_subexponential_extension.md) proves the corresponding odd-source statement with its regularized positive comparator.