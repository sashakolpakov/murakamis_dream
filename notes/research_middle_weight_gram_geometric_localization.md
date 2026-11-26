# Geometric localization of the actual middle-weight Gram

21 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

The positive Gram of the genuine middle-weight turn has an explicit
ideal-tetrahedron growth profile. After normalizing each row by its
actual norm, macroscopically separated interior indices have a strict
exponential overlap loss. Each exact endpoint also has exponentially
small overlap with the interior. The two endpoints themselves retain
an overlap of order \(N^{-1/2}\).

These are local estimates for the correct Gram and its inverse. They
do not give a smallest-eigenvalue bound or a lower bound for an
arbitrary original knot closing.

## 1. The actual Gram and existing covariance coverage

Use the full physical coordinates and source of the
[middle-weight turn theorem](research_middle_weight_turn_gram_kernel.md).
Put \(d=N-1\), \(q=e^{\pi i/N}\), and
\[
 s_0=1,\qquad s_j=\prod_{h=1}^j2\sin(\pi h/N),\qquad
 \beta_{ra}=\frac{s_r}{s_as_{r-a}}\quad(a\le r\le d).
\]
Set \(\beta_{ra}=0\) outside this support. The actual cyclic-column
matrix and its positive Gram are
\[
 C_{ar}=(-1)^rq^{r(a+1)}\beta_{ra},\qquad H=CC^*.
 \tag{1}
\]
In particular
\[
 H_{aa}=\sum_{r=a}^d\beta_{ra}^2,\qquad
 H_{ab}=\sum_{r\ge\max(a,b)}q^{r(a-b)}\beta_{ra}\beta_{rb}.
 \tag{2}
\]
Define normalized correlations by
\[
                         R_{ab}=\frac{H_{ab}}{\sqrt{H_{aa}H_{bb}}}.
 \tag{3}
\]
Every row norm is retained in this definition.

There is an exact connection with the existing
[Newton covariance theorem](research_actual_newton_crossing_gaussian_covariance.md).
Let \(T_1\) be the original Newton crossing and \(P\) index reversal.
The identities \(C=\kappa^{-1}T_1^{\mathsf T}\) and
\(PT_1P=T_1^{\mathsf T}\) give
\[
                              H=P(T_1T_1^*)P.
 \tag{4}
\]
Thus the previously proved local Gaussian kernel and fixed endpoint
windows already apply by reflection. They are not new claims here.
We derive the uniform macroscopic separation and keep the exact
endpoint-to-interior phases, which a positive overlap majorant alone
would miss.

## 2. The row action and its unique maximum

Put
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 \Lambda(\theta)=-\int_0^\theta\log(2\sin u)\,du.
\]
The endpoint-uniform factorial estimate from the covariance theorem is
\[
          \log s_j=NJ(j/N)+O(\log N),\qquad 0\le j<N.
 \tag{5}
\]
It includes \(s_0=1\). One elementary proof subtracts
\(\log t+\log(1-t)\) from the integrand, leaving a smooth function
on \([0,1]\); integral comparison for the two logarithms gives the
uniform error in (5).

For \(\xi=a/N\), \(u=r/N\), the squared coefficient in (2)
has action
\[
 \ell_\xi(u)=2\{J(u)-J(\xi)-J(u-\xi)\},\qquad \xi\le u\le1.
 \tag{6}
\]
In the interior of that interval,
\[
 \ell_\xi'(u)=2\log\frac{\sin\pi u}{\sin\pi(u-\xi)},\qquad
 \ell_\xi''(u)=
 -\frac{2\pi\sin\pi\xi}{\sin\pi u\sin\pi(u-\xi)}<0.
 \tag{7}
\]
Its unique maximum is at \(u_\xi=(1+\xi)/2\). Since
\(J(1-t)=-J(t)\), the maximum is
\[
 h(\xi)=-2J(\xi)-4J((1-\xi)/2)
  =\frac2\pi\left\{\Lambda(\pi\xi)
                      +2\Lambda(\pi(1-\xi)/2)\right\}.
 \tag{8}
\]
The three angles \(\pi\xi,\pi(1-\xi)/2,\pi(1-\xi)/2\)
sum to \(\pi\); the expression in braces is their usual ideal
tetrahedron volume. It is positive for \(0<\xi<1\). Positivity
also follows directly here: \(\ell_\xi(\xi)=0\), and its strictly
concave profile has an interior maximum.

For each fixed \(0<\delta<1/2\), uniformly when
\(\delta\le a/N\le1-\delta\),
\[
                         \log H_{aa}=Nh(a/N)+O_\delta(\log N).
 \tag{9}
\]
Indeed (5) bounds every summand in (2) by its action with a uniform
polynomial factor. There are at most \(N\) summands. For the reverse
bound choose the integer \(r\) nearest \(Nu_\xi\). This point is
uniformly inside the allowed interval for all sufficiently large
\(N\), and its action differs from the maximum by \(O_\delta(N^{-1})\)
or less. The same factorial estimate gives the lower bound.

## 3. Strict macroscopic separation in the interior

For \(a/N=\xi\in[\delta,1-\delta]\), define the exact probability
distribution
\[
                  p_a(r)=\beta_{ra}^2/H_{aa}.
\]
Equations (5)--(9) give a fixed power of \(N\), uniform in \(a,r\),
times the exponential of
\(N\{\ell_\xi(r/N)-h(\xi)\}\). From (7), on the whole allowed
interval,
\[
 \ell_\xi(u)\le h(\xi)
               -\pi\sin(\pi\delta)(u-u_\xi)^2.
 \tag{10}
\]
The inequality extends to both ends by continuity.

Keeping the actual phases in (2) before taking an upper bound yields
the Hellinger-affinity estimate
\[
 |R_{ab}|\le\sum_r\sqrt{p_a(r)p_b(r)}.
 \tag{11}
\]
For two interior indices, the two maximizing positions differ by
\((a-b)/(2N)\). Use
\((u-v)^2+(u-w)^2\ge(v-w)^2/2\) in (10), and sum at most
\(N\) terms in (11). There are constants \(C_\delta,M_\delta\),
independent of the level and the two indices, such that
\[
 \boxed{\quad
 |R_{ab}|\le C_\delta N^{M_\delta}
       \exp\left\{-\frac{\pi\sin(\pi\delta)}{16N}(a-b)^2\right\}.
 \quad}
 \tag{12}
\]
In particular, for every fixed \(\varepsilon>0\), the overlap has
a strict uniform exponential loss when \(|a-b|\ge\varepsilon N\)
and both indices are in that interior interval. The statement is an
upper bound, not a nonzero asymptotic for a mixed matrix entry.

## 4. Both exact endpoints

The exact endpoint formulas for the turn, with \(H=\mathcal JP\),
give
\[
 |H_{0b}|=s_{d-b},\qquad |H_{db}|=1,\qquad
                         H_{00}=N,\quad H_{dd}=1.
 \tag{13}
\]
Consequently, uniformly for \(\xi=b/N\in[\delta,1-\delta]\),
\[
 \log|R_{0b}|=2NJ((1-\xi)/2)+O_\delta(\log N),\qquad
 \log|R_{db}|=-Nh(\xi)/2+O_\delta(\log N).
 \tag{14}
\]
For the first equality use (5), (9), and
\(J(1-\xi)=-J(\xi)\). The shift from \((d-b)/N\) to
\(1-\xi\) costs only \(O_\delta(1)\) in its logarithm.
Both rates are strictly negative on the stated compact interval:
\(J(t)<0\) for \(0<t<1/2\), and \(h(\xi)>0\).

The two endpoints themselves instead obey exactly
\[
                                  |R_{0d}|=N^{-1/2}.
 \tag{15}
\]
Thus they must be kept together if only exponential separation is
being used. The first endpoint-to-interior estimate in (14) uses the
actual phase cancellation in (13). Its Hellinger majorant need not
have that exponential loss, because the zeroth row's positive
distribution is uniform.

The correctly transported metric is \(G=H^{-1}=PHP\). Its normalized
correlations are the corresponding reflected correlations of \(H\).
Therefore the same bulk and endpoint separation statements apply to
the inverse metric, with the endpoint roles exchanged. These assertions
do not bound either matrix's smallest eigenvalue: their unnormalized
diagonal energies and conditioning can be exponential.

## 5. What this localizes

Equations (12) and (14) give exponentially small normalized cross
blocks between separated interior macroscopic intervals, and between
either exact endpoint and an interior compact interval. Taking an
operator norm of such a cross block adds at most a further factor
\(N\). The remaining two-endpoint block retains (15). The near-diagonal
Gaussian and fixed endpoint-window refinements are already supplied
by (4) and the earlier covariance theorem.

This is geometric localization of the actual boundary Gram, with its
original factorial weights. It is not a statement that an arbitrary
short component preserves a chosen packet band, nor that its original
closing has a nonzero geometric coefficient. Every diagonal weight
must still be retained in a source estimate. No lower bound for the
full knot invariant or new volume identity is inferred.

## Complete proof sources and coverage

Both complete matching proof sources were read. The earlier diagonal,
Gaussian and endpoint-window calculations are credited through (4);
the uniform separation estimates above are derived directly from their
actual finite coefficients.

| Source | SHA-256 |
|---|---|
| [Middle-weight turn and correct Gram](research_middle_weight_turn_gram_kernel.md) | 01f2c9d5724eca87c6bef1ffa8a6faae53f47d5dbdc7e71513165c39cb674e41 |
| [Actual Newton covariance](research_actual_newton_crossing_gaussian_covariance.md) | ce2b1b8efbbcffa8bafe0d0de4f7ce12febf193e433d8e3291f7d2a8c826fa3f |

Hellinger affinity, Laplace comparison and Cauchy--Schwarz are standard
methods; no novelty is claimed for them. Only written mathematics and
text/hash operations were used. No mathematical program, test,
numerical optimization, build, git operation or earlier-final edit was
performed.
