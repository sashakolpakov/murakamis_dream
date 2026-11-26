# The complete Newton column norm and an elementary upper rate

Private written source deduction, 9 November 2026. The original
complete column has a positive norm asymptotic governed by the
midpoint cap action. Every original row is included. The endpoint
rows are estimated directly, without continuing an interior packet
to either endpoint. A small ordinary incoming neighborhood permits
an arbitrary positive rate allowance.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, test or frozen-source edit is used. In particular no
saved cap-action enclosure is used in the scalar upper bound below.

## 1. The actual column and the statement

Retain \(D=N-1\), \(q=e^{\pi i/N}\), \(\kappa=q^{D^2/2}\), and
the original complete Newton vector and crossing matrix:
\[
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(w)=S_j^{-2}\prod_{\nu<j}(2\cos((2\nu+1)\pi/N)-w),
 \qquad \mathbf e(w)=(e_0(w),\ldots,e_D(w))^T,
\]
\[
 M_{j\ell}=\kappa(-1)^j q^{j(\ell+1)}
            \frac{S_j}{S_\ell S_{j-\ell}}\quad(0\le\ell\le j<N).
                                                                    \tag{1}
\]
Put
\[
 C_{j,N}(w)=\sum_{\ell=0}^j
          \frac{q^{j\ell}e_\ell(w)}{S_\ell S_{j-\ell}},\qquad
 C_{j,N}=C_{j,N}(-2).
\]
The unchanged exact identity is
\[
 (M\mathbf e(w))_j=\kappa(-q)^jS_jC_{j,N}(w),\qquad
 \|M\mathbf e(-2)\|_2^2=\sum_{j=0}^D S_j^2|C_{j,N}|^2.           \tag{2}
\]
The full-index cap action and coefficient are
\[
 F(s,z)=-2J(1/2-z)-3J(z)-J(s-z)+i\pi sz,
\]
\[
 z_c(s)=\pi^{-1}\arctan\frac{i+\sqrt{1-2e^{2\pi is}}}{2},\quad
 S_{\rm cap}(s)=F(s,z_c(s)),\quad\lambda(s)=\Re S_{\rm cap}(s),
\]
\[
 A_0(s)=\frac{\sqrt{2\pi}}{\sqrt{-F_{zz}(s,z_c)}}
 \frac1{(2\sin\pi z_c)^{3/2}(2\sin\pi(s-z_c))^{1/2}},\qquad
 \lambda_*:=\lambda(1/2).                                      \tag{3}
\]
All primitives and roots are the original calibrated ones. Write
\(b_2=-4J(1/4)\) for the original real Newton exponent.

**Theorem.** At both level parities, for the actual complete column,
\[
 \boxed{\quad
 \|M\mathbf e(-2)\|_2
   =2^{-5/4}3^{-1/8}N^{-3/4}e^{N\lambda_*}
                          (1+O(N^{-1})),\qquad
                 b_2+1/9<\lambda_*<175/216.
 \quad}                                                         \tag{4}
\]
For every fixed \(\tau>0\), a fixed ordinary disk
\(\mathcal D_\tau\) about \(-2\) and constants \(C_\tau,A_\tau\)
give
\[
 \sup_{w\in\mathcal D_\tau}\|M\mathbf e(w)\|_2
       \le C_\tau N^{A_\tau}e^{N(\lambda_*+\tau)}.               \tag{5}
\]
Every fixed ordinary derivative has the same allowed rate on a
smaller disk. No all-real incoming version of (5) is asserted.

## 2. The whole real-index profile has one maximum

On each compact \(I\subset(0,1)\), the full-index coefficient
theorem gives the actual finite-source expansion
\[
 C_{j,N}=N^{-3/2}A_0(j/N)e^{NS_{\rm cap}(j/N)}
                  (1+O_I(N^{-1})),\qquad j/N\in I.              \tag{6}
\]
It holds uniformly through \(s=1/2\) and at both parities.
The ordinary sine-factorial symbol on the same compact is
\[
 S_j=\sqrt{2N\sin(\pi s)}\,e^{NJ(s)}(1+O_I(N^{-1})),
                         \qquad s=j/N.                          \tag{7}
\]
For example apply the original midpoint formula
\(G_N(Nx-1/2)=\sqrt N e^{NJ(x)}(1+O(N^{-1}))\) at
\(x=s+1/(2N)\); Taylor expansion of the same primitive supplies
the factor \(\sqrt{2\sin\pi s}\).

Thus the relevant real profile is
\[
                            f(s)=\lambda(s)+J(s).               \tag{8}
\]
Here is its original exact derivative calculation, without any
action evaluation. Write
\[
 \sqrt{1-2e^{2\pi is}}=a+ib,\qquad
 \sigma=\sqrt{1-b^2}>0,\qquad A=1+\sigma+b.
\]
On \(0<s<1\), \(a>0\), \(-1<b<1\); the sign of \(b\) is
negative below \(1/2\) and positive above it. The original
critical derivative and modulus identities are
\[
 \lambda'(s)-J'(s)=-2\log A,\qquad
 4\sin^2\pi s=2\sigma(1+\sigma),\qquad
 A^2=2(1+\sigma)(1+b).                                         \tag{9}
\]
They are the algebraic identities in Section 2 of the seam-source
proof; that section uses no scalar certificate. All denominators
and logarithm arguments in (9) are positive. Consequently
\[
 f'(s)=\log\frac{\sigma}{1+b}
                 =\frac12\log\frac{1-b}{1+b}.                  \tag{10}
\]
This is positive before \(1/2\) and negative after it. The unique
global interior maximum of (8) is therefore
\(f(1/2)=\lambda_*\), because \(J(1/2)=0\).
Differentiating the original square root at the midpoint gives
\[
 b'(1/2)=2\pi/\sqrt3,\qquad
                    f''(1/2)=-2\pi/\sqrt3.                     \tag{11}
\]
In particular the positive norm profile has a nondegenerate maximum.

## 3. Both endpoint regions are genuinely included

Fix \(\delta_0=1/100\). Sine concavity on \([0,1/6]\) gives
\(2\sin\pi x\ge6x\). Therefore
\[
 -J(\delta_0)
 \le\delta_0\{1-\log(6\delta_0)\}<1/25.                        \tag{12}
\]
For the last strict inequality use \(\log(50/3)<3\), witnessed by
\[
 e^3>1+3+9/2+27/6+81/24+243/120=92/5>50/3.
\]
Also \(\log2<1\). These are elementary positive-series comparisons.

Suppose first \(j/N=s\le\delta_0\). All factors of \(S_j\) are
less than one, so \(S_j\le1\). The original nonnegative Newton
values obey \(e_\ell(-2)\le4^\ell/S_\ell^2\). Hence (2) gives
\[
 |(M\mathbf e(-2))_j|
     \le\sum_{\ell=0}^j\frac{4^\ell}{S_\ell^3S_{j-\ell}}.
                                                                    \tag{13}
\]
The uniform endpoint sine-factorial estimate
\(\log S_j=NJ(j/N)+O(\log N)\), valid also at zero, bounds each
term's rate by \(2s\log2-4J(s)\). Indeed \(J\) decreases on
\([0,\delta_0]\), so replacing both partial arguments by \(s\)
only increases this bound. Equations (12)--(13) prove
\[
 |(M\mathbf e(-2))_j|\le CN^A e^{9N/50}
                              \qquad(j/N\le\delta_0).           \tag{14}
\]

At the other endpoint put \(k=D-j\). Exact reflection
\(S_{D-r}=N/S_r\) gives, before taking absolute values,
\[
 S_jC_{j,N}
   =\frac1{S_k}\sum_{\ell=0}^j
                     q^{j\ell}e_\ell(-2)\frac{S_{k+\ell}}{S_\ell}.
                                                                    \tag{15}
\]
Every index \(k+\ell\) is at most \(D\). The ratio in (15)
has at most \(k\) sine factors, each at most two. The original
all-index real Newton theorem bounds
\(\sum_{\ell=0}^D e_\ell(-2)\le CN^A e^{Nb_2}\). Thus
\[
 |(M\mathbf e(-2))_j|
 \le\frac{2^k}{S_k}CN^A e^{Nb_2}
 \le CN^{A'}e^{N(b_2+1/20)}
                            \qquad(k/N\le\delta_0),             \tag{16}
\]
by (12), \(\log2<1\), and monotonicity of \(-J\) on this interval.
The argument includes \(k=0\). It keeps every odd Newton zero;
no vanishing value has been canceled.

The adopted exact-column lower proof gives
\(\lambda_*>b_2+1/9\), with \(b_2>56/99\), using no saved action.
Both (14) and (16) consequently have a fixed positive gap below
\(\lambda_*\); a gap \(1/20\) is smaller than both available gaps.
All remaining rows have \(j/N\) in a fixed compact subinterval
of \((0,1)\), where (6)--(10) apply. The two literal endpoint
estimates and that compact packet cover every \(0\le j<N\).

## 4. The full positive norm asymptotic

From (6)--(8), uniformly on a compact interval about the midpoint,
\[
 S_j^2|C_{j,N}|^2
  =2N^{-2}\sin(\pi s)|A_0(s)|^2e^{2Nf(s)}(1+O(N^{-1})).        \tag{17}
\]
Every compact portion away from the midpoint has a strict gap by
(10); Section 3 handles both excluded endpoint regions. Thus the
complete sum in (2) is a positive discrete Laplace sum with its
unique maximum at \(1/2\).

For precision, choose a smooth cutoff equal to one near that point.
For the normalized summand on its support, the integral of the
absolute second derivative is \(O(N^{1/2})\), by the local negative
quadratic bound for \(f-f(1/2)\). The two-derivative trapezoidal
remainder on mesh \(1/N\) is therefore \(O(N^{-3/2})\), while
the corresponding integral is of order \(N^{-1/2}\).
The usual real Gaussian expansion of this integral has relative
error \(O(N^{-1})\): the first cubic correction is odd. These
estimates apply to the same mesh at either parity; no midpoint
sample is required. The uniform relative error already present
in (17) has the same order after summation.

With \(a_*=-f''(1/2)=2\pi/\sqrt3\), this gives
\[
 \|M\mathbf e(-2)\|_2^2
 =2|A_0(1/2)|^2\sqrt{\frac\pi{a_*}}\,
       N^{-3/2}e^{2N\lambda_*}(1+O(N^{-1})).                    \tag{18}
\]
The original critical point is
\(z_c(1/2)=1/4+i\log3/(4\pi)\). On its original sheet,
\[
 -F_{zz}(1/2,z_c)=3\sqrt3\pi,\qquad
 |2\sin\pi z_c|^2=|2\sin\pi(1/2-z_c)|^2=4/\sqrt3.
\]
Substitution in (3) gives
\[
 |A_0(1/2)|^2=1/(8\sqrt3),\qquad
 2|A_0(1/2)|^2\sqrt{\pi/a_*}=2^{-5/2}3^{-1/4}.                 \tag{19}
\]
Taking the positive square root of (18) proves the norm asymptotic
and its exact constant in (4).

## 5. The evaluation-free upper rate

Set \(\ell=\log3\), \(h_* =\ell/(4\pi)\), and
\(L(h)=\Re F(1/2,1/4+ih)\). The original segment calculation is
\[
 L(0)=3b_2/2,\quad L'(0)=-\pi/2,\quad
 L''(h)=\frac{6\pi\operatorname{sech}^2(\pi h)}
                      {1+\tanh^2(\pi h)}\le6\pi.
\]
Taylor's integral formula, with its original constant, gives
\[
 \lambda_*=L(h_*)
 \le\frac32b_2-\frac\ell8+\frac{3\ell^2}{16\pi}.              \tag{20}
\]
The established real Newton inequality \(b_2<7/12\) and
\(\pi>25/8\) bound the right side strictly by
\(7/8-\ell/8+3\ell^2/50\).

Both needed logarithm bounds have positive-series witnesses.
The series \(e=\sum 1/n!<3\), since \(n!\ge2^{n-1}\) for
\(n\ge2\), with strict inequality after \(n=2\). Thus \(\ell>1\).
Also
\[
 e^{10/9}>1+10/9+50/81+500/2187+1250/19683
                         =59453/19683>3,
\]
because \(59453>59049\). Hence \(\ell<10/9\).
The displayed quadratic is convex, so its maximum on
\([1,10/9]\) is attained at an endpoint. Its two endpoint values
are \(81/100\) and \(175/216\), respectively, and
\(17500>17496\). Therefore
\[
                              \lambda_*<175/216.                \tag{21}
\]
Only the original analytic phase and elementary inequalities
entered this ceiling. In particular neither scalar enclosure
in the seam-source certificate was used.

## 6. Ordinary incoming neighborhoods and the three-crossing column

The physical identity (2) is valid for every ordinary \(w\).
On the retained compact index interval, Theorem 2 of the full-index
source gives the joint packet for \(C_{j,N}(w)\) in a fixed disk
about \(-2\). Its holomorphic phase differs from
\(S_{\rm cap}(s)\) by \(O(|w+2|)\), uniformly in that interval.
Thus its contribution to (5) costs an arbitrarily small rate when
the disk is shrunk.

The small-index proof remains literal: replace \(4^\ell\) in
(13) by \((4+\rho)^\ell\) for \(|w+2|\le\rho\).
Its added rate is at most \(\delta_0\log(1+\rho/4)\), which tends
to zero. For the large-index proof, (15) remains exact with
\(e_\ell(w)\). The same full-index source proves directly from
the regularized Newton products, including their odd zero,
\[
 \sum_{\ell=0}^{D}|e_\ell(w)|
       \le C_\rho N^A e^{N(b_2+C\sqrt\rho)}.                    \tag{22}
\]
It follows that the two fixed endpoint gaps persist for sufficiently
small \(\rho\). Together with the compact packet this proves (5).
Vector-valued Cauchy estimates on a smaller disk give every fixed
ordinary derivative with the same allowance.

Finally the adopted complete matrix bound
\(\|M^2\|_2\le CN^A e^{Nb_2}\) gives the source-specific consequence
\[
 \sup_{w\in\mathcal D_\tau}\|M^3\mathbf e(w)\|_2
       \le C_\tau N^{A_\tau}e^{N(b_2+\lambda_*+\tau)}.          \tag{23}
\]
The same is true for fixed incoming derivatives on smaller disks.
This is a complete-column upper bound, not a nonzero observation
of that column. Whether (23) pays a remaining signed closing
contour still requires its actual evaluation vector and crossing
rate. No such final comparison is asserted here.

## Frozen source bindings

- Exact complete column, midpoint lower bound and unchanged normalization:
  [column obstruction](research_mixed_symmetric_closing_complete_column_obstruction.md),
  c709d3cd53e32c54e036a952588357d1f3e50e422eafc2967fa1f898e1e005cf.
- Complete full-index cap packet and joint ordinary-color neighborhood:
  [full-index theorem](research_complete_boundary_full_index_interval.md),
  450cd41db9c49049e9b80a41c83828a2f0fafa43f986803bc57b93be580a57ef.
- Original exact seam derivative identity, only its algebraic Section 2:
  [seam-source profile](research_mixed_cap_seam_source_bounds.md),
  88e07855c29788902c79ba9727f633a213e8fea5a0cc224092725b2e706dc75d.
- Original midpoint factorial symbol and cap normalization:
  [coefficient theorem](research_complete_boundary_coefficient_asymptotic.md),
  4a3c2037315991d4c63e0c99964789cef0a38937fc0fa218255b5b596699e65a.
- Complete zero-safe Newton and sine-factorial estimates:
  [real-period theorem](research_three_crossing_real_period_newton_bound.md),
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.
- Full two-crossing matrix norm and original \(b_2\):
  [preparation-error theorem](research_three_crossing_global_preparation_error.md),
  c1e80c6efbc9ff936d889eebd1f449e85c81820a64fb046e6dfe8e1003d2d239.
