# Filtered continuation of the actual scalar Borel exponential

Private written proof, 18 November 2026.

The meromorphic derivative of the literal interval Borel logarithm
can be exponentiated by convolution along every path satisfying an
explicit finite length and singularity condition. A face-preserving
flow supplies the continued convolution simplices. Its estimates
are uniform in their dimension, so the convolution exponential
converges on the resulting path charts.

Only filtered additive singular sets are used. Their unfiltered
union is not assumed to be locally finite. The construction retains
the original primitive from zero and every endpoint constant.

## 1. Hypotheses, filtration, and statement

Let \(\Omega\subset\mathbb C\setminus\{0\}\) be closed and locally
finite. Let \(g\) be single-valued and holomorphic on
\(\mathbb C\setminus\Omega\); meromorphic functions with poles in
\(\Omega\) are the application. Candidate poles whose residues
cancel may remain in \(\Omega\).
Choose \(r_*>0\) with
\[
                    \operatorname{dist}(0,\Omega)\ge r_* .
 \tag{1}
\]
If \(\Omega\) is empty, any \(r_*>0\) may be used.
For \(B>0\) define the finite set
\[
 \Sigma_B=\{0\}\cup
 \left\{\omega_1+\cdots+\omega_q:
    q\ge1,\ \omega_j\in\Omega,\
                          \sum_{j=1}^q|\omega_j|\le B\right\}.
 \tag{2}
\]
It is finite: only \(\Omega\cap\{|\omega|\le B\}\) occurs and
\(q\le B/r_*\). Repetitions and cancellations are allowed.

Start at \(0<|\xi_0|<r_*/2\). Let
\(\gamma:[0,1]\to\mathbb C\) be a piecewise \(C^1\) path
with \(\gamma(0)=\xi_0\). Fix \(L,\varepsilon,\delta>0\)
such that
\[
 |\xi_0|+\operatorname{len}(\gamma)\le L,\qquad
 \operatorname{dist}\bigl(\gamma([0,1]),\Sigma_{L+\varepsilon}\bigr)
                                                       \ge\delta .
 \tag{3}
\]
The initial germ is reached from zero by the straight segment to
\(\xi_0\). This is the only permitted occurrence of the base zero
in the prescribed path; (3) excludes returning to zero on another
sheet. Write
\[
 d=\min(\varepsilon,\delta),\quad
 \ell=\operatorname{len}(\gamma),\quad
 E=\exp(2\ell/d),\quad
                   \rho_*=(r_*/2)e^{-\ell/d}.
 \tag{4}
\]

**Theorem.** Every convolution power \(g^{*n}\) continues along
\(\gamma\), with common local continuation disks for all \(n\).
There are constants \(M,A>0\), independent of \(n\), such that
on those disks
\[
                     |g^{*n}|
                \le \frac{M^n A^{n-1}}{(n-1)!}.
 \tag{5}
\]
On the path itself one may take
\[
 A=2|\xi_0|E,\qquad
 M=\sup_{\substack{|\zeta|\le L\\
                    \operatorname{dist}(\zeta,\Omega)\ge\rho_*}}
                                                    |g(\zeta)|.
 \tag{6}
\]
For an empty \(\Omega\), the distance restriction is omitted.
The displayed supremum is finite.
Consequently
\[
                         H=\sum_{n\ge1}\frac{g^{*n}}{n!}
 \tag{7}
\]
is a normally convergent analytic continuation of its initial germ
on the same path charts. No uniform bound over unbounded path lengths
or over a vanishing separation in (3) is asserted.

## 2. The lifted simplex and its flow

For \(n\ge2\), write
\[
 \Delta_{n-1}=\{s_i\ge0:\ \sum_{i=1}^{n-1}s_i\le1\},
 \qquad s_n=1-\sum_{i<n}s_i.
 \tag{8}
\]
The initial simplex in \(\mathbb C^n\) is
\(\zeta_i(0,s)=s_i\xi_0\). Set
\[
 d_i(\zeta)=\operatorname{dist}(\zeta_i,\Omega\cup\{0\}),
 \quad D(\zeta)=\sum_i d_i(\zeta),\qquad
 \dot\zeta_i=\frac{d_i(\zeta)}{D(\zeta)}\,\dot\gamma .
 \tag{9}
\]
The same formula applies to \(n=1\), with its zero-dimensional
simplex. The vector field is locally Lipschitz where \(D>0\).
Until its maximal solution stops, it satisfies
\[
 \sum_i\zeta_i(t,s)=\gamma(t),\qquad
 \sum_i|\zeta_i(t,s)|
             \le|\xi_0|+\operatorname{len}(\gamma|_{[0,t]})\le L.
 \tag{10}
\]
The first identity follows by summing (9). For the second use
\(\sum_i|\dot\zeta_i|=|\dot\gamma|\), since the weights in (9)
are nonnegative and sum to one.

There is a dimension-independent lower bound
\[
                                  D(\zeta(t,s))\ge d .
 \tag{11}
\]
Indeed choose nearest \(\omega_i\in\Omega\cup\{0\}\).
If \(D<d\), then
\[
 \sum_i|\omega_i|\le L+D<L+\varepsilon,\qquad
 \left|\gamma-\sum_i\omega_i\right|\le D<\delta.
 \tag{12}
\]
After omitting the zero choices, their sum belongs to (2), in
contradiction with (3). Nearest points exist because the set is
closed and locally finite.

When \(\Omega\ne\varnothing\), for the distance to candidate poles,
\(r_i(t)=\operatorname{dist}(\zeta_i(t),\Omega)\), the
Lipschitz distance function gives almost everywhere
\[
 \dot r_i\ge-|\dot\zeta_i|
                 \ge-(|\dot\gamma|/d)r_i .
 \tag{13}
\]
Here \(d_i\le r_i\). Initially \(r_i\ge r_*/2\), so
\(r_i\ge\rho_*\) throughout. Also \(d_i\le|\zeta_i|\);
thus a nonzero initial coordinate cannot reach zero in finite
time by the same differential inequality.
If \(s_i=0\), uniqueness in (9) makes \(\zeta_i\equiv0\).
Every original boundary face is therefore retained in its exact
coordinate hyperplane.

Equations (10)--(13) keep each fixed-dimensional solution in a
bounded region with \(D\) bounded away from zero. The local
Lipschitz flow extends to the whole time interval. They also
prove that the transported simplex avoids all pole hyperplanes.
These arguments apply to arclength-parametrized Lipschitz paths
as well, with (9) understood as its integral equation.

## 3. Uniform derivatives and the convolution bound

For two configurations with \(D,D'\ge d\), the one-Lipschitz
property of distance gives
\[
 \sum_i\left|\frac{d_i}{D}-\frac{d'_i}{D'}\right|
       \le \frac{2}{d}\sum_i|\zeta_i-\zeta'_i|.
 \tag{14}
\]
For example split the difference with denominator \(D\);
the two terms are bounded by
\(\sum|d_i-d'_i|/D\) and \(|D-D'|/D\).
Gronwall applied in the \(\ell^1\) norm now shows that the
time-\(t\) flow has Lipschitz constant at most \(E\) on the
initial simplex. No factor depending on \(n\) enters (14).

Each parameter column of the initial simplex has \(\ell^1\)
norm \(2|\xi_0|\). Thus each derivative column of the flowed
simplex, defined almost everywhere, has norm at most
\(2|\xi_0|E\). On the affine fiber \(\sum\zeta_i=\xi\), use
the holomorphic top form
\[
 \omega_{n,\xi}
       =\left(\prod_{i=1}^n g(\zeta_i)\right)
                           d\zeta_1\wedge\cdots\wedge d\zeta_{n-1}.
 \tag{15}
\]
At \(t=0\), its simplex integral is exactly the usual convolution
power, by the substitution \(\zeta_i=s_i\xi_0\).
Hadamard's determinant bound, (6), and
\(\operatorname{vol}(\Delta_{n-1})=1/(n-1)!\) give
\[
 \left|\int_{\zeta(t,\Delta_{n-1})}\omega_{n,\gamma(t)}\right|
       \le \frac{M^n(2|\xi_0|E)^{n-1}}{(n-1)!}.
 \tag{16}
\]
For \(n=1\) this is simply the bound for \(g(\gamma(t))\).
It remains to show that these integrals are holomorphic
continuation germs, not just bounded pathwise numbers.

## 4. Holomorphic collars and relative-chain uniqueness

Fix \(t_0\), set \(\xi_*=\gamma(t_0)\), and freeze the weights
\(\alpha_i(s)=d_i(\zeta(t_0,s))/D(\zeta(t_0,s))\).
For \(w\) close to \(\xi_*\), define the chain
\[
 \zeta_i^{\,w}(s)=\zeta_i(t_0,s)+(w-\xi_*)\alpha_i(s).
 \tag{17}
\]
Its sum is \(w\). If \(s_i=0\), both terms in (17) are zero.
Since \(0\le\alpha_i\le1\), every coordinate moves by at most
\(|w-\xi_*|\). Take, for example,
\[
              |w-\xi_*|<\sigma,\qquad
              0<\sigma<\min(\rho_*/4,d/4,1).
 \tag{18}
\]
All factors then remain a fixed distance from the poles,
uniformly in \(n\) and \(t_0\).

The map (17) is holomorphic in \(w\). Its parameter derivatives
are affine in \(w\) almost everywhere. By (14), their column
norms are bounded by
\[
                       2|\xi_0|E(1+2\sigma/d).
 \tag{19}
\]
The integral of (15) over (17) is therefore holomorphic in \(w\):
one may differentiate under the bounded parameter integral, or
apply the scalar Cauchy formula there. Equations (18)--(19)
and a supremum of \(g\) on the slightly enlarged pole-safe
compact set prove (5) on a disk of common radius.

For a nearby time \(t\), compare the flowed chain with (17)
at \(w=\gamma(t)\). Both have the same sum and the same zero
faces. Their straight interpolation is in that fixed affine
fiber, and remains pole-free when \(t\) is sufficiently close
to \(t_0\): each chain differs coordinatewise from the old one
by at most the short path length plus its endpoint displacement.
The form (15) is closed on the fiber. On each face
\(\zeta_i=0\), its restriction is zero, since that face has
complex dimension at most \(n-2\). This includes \(i=n\),
where \(\sum_{i<n}d\zeta_i=0\) on the face.
Relative Stokes therefore gives equality of the two integrals.

The same argument is legitimate for the Lipschitz chains used
here. Triangulate the parameter simplex and its homotopy prism
by successively finer shape-regular meshes, and interpolate the
map's vertex values affinely. Its affine sum constraint and every
coordinate zero face remain exact. Uniform convergence preserves
the positive pole buffer. The interpolants have a common Lipschitz
bound at each fixed dimension. At a point of differentiability
of the original map, its affine first-order approximation has
vertex errors \(o(\text{mesh size})\); shape regularity therefore
gives convergence of the interpolant derivatives at that point.
Lipschitz maps are differentiable almost everywhere, so dominated
convergence applies to the pulled-back forms, on the prism and
on its separately triangulated boundary faces. Ordinary Stokes
on the affine simplices cancels all shared faces. Passing to the
limit proves the asserted relative Stokes identity. Dimension-
dependent constants in this approximation argument cause no loss
in (16), which was proved directly for the original flow.
The zero-dimensional case is immediate.

Consequently (17) is a holomorphic germ agreeing with all nearby
flowed values. Consecutive germs agree by the identity theorem
when the path is nonconstant; on constant segments the transported
chains and collars themselves are unchanged. They start with
the original convolution germ, so
give its analytic continuation along the specified path.
Piecewise \(C^1\) families of admissible path deformations with common
buffers give the same relative-chain comparison. No endpoint-only
single-valuedness is asserted.

## 5. The convolution exponential and source parameters

The bound (5) makes (7) normally convergent on every one of the
common continuation disks:
\[
             \sum_{n\ge1}
                \frac{M^n A^{n-1}}{n!(n-1)!}<\infty.
 \tag{20}
\]
This proves the theorem, including a common germ for the full
sum rather than only separate continuation of each coefficient.

The proof is joint in any source parameters for which \(g\) is
holomorphic on a common neighborhood of the compact sets used
above. Keep the flows fixed at a parameter base point and shrink
its parameter chart to retain that neighborhood. Then (17),
the integrals, and the series (20) are jointly holomorphic.
In the application [D], the candidate singular divisors are
locally finite on compact endpoint/meridian charts. Their
positive endpoint separation and the pole buffer (13) permit
precisely this shrinking. Candidate poles are retained even
when their residues cancel at the parameter base point.
No assertion is made across an endpoint singularity or without
a uniform buffer for the moving candidate divisors.

Let
\[
 V(h)=v_0+\sum_{j\ge1}v_jh^j,\qquad
 \widehat V=\mathcal B_0V
       =\sum_{j\ge0}v_j\xi^j/j!,\qquad
                           g=\partial_\xi\widehat V.
 \tag{21}
\]
The product rule for the minor transform is elementary:
for positive powers of \(h\), convolution of
\(\xi^{j-1}/(j-1)!\) and \(\xi^{k-1}/(k-1)!\)
is \(\xi^{j+k-1}/(j+k-1)!\), by one integration.
Thus the initial coefficient identity is exactly
\[
 \boxed{\quad
 \mathcal B_0(e^{V(h)})
    =e^{v_0}\left(1+
          I_0\sum_{n\ge1}\frac{g^{*n}}{n!}\right).
 \quad}
 \tag{22}
\]
Here \(I_0\) is the continued primitive with its original value
zero at \(\xi=0\). It follows the initial segment and then
the prescribed path, without resetting after a loop.
The continuation proved above therefore constructs the actual
Borel germ of the scalar exponential, including its original
constant \(v_0\) and all subsequent monodromy.

## 6. Literal factorial application and scope

By [D], every actual literal interval defect logarithm has
exactly the convention (21). Its derivative \(g\) is
single-valued meromorphic, with candidate poles
\[
 \bigcup_{n\ne0}
       \{2\pi i n(\tau-s),\ 2\pi i n\tau\},
 \tag{23}
\]
where \(\tau\) is a zero or pole of the literal endpoint
function. Both endpoints and all integer-offset corrections
are retained. Those corrections add entire functions to \(g\).
Finite signed sums of the original intervals likewise have
meromorphic \(g\), using the finite union of their candidate
sets and the sum of their exact constants. Apply (22) to that
sum to obtain filtered continuation of its scalar defect
factor. The principal integral, monomial terms, pivot and
framing remain the separately specified original factors;
none has been inferred from the derivative alone.

This pays scalar Borel convolution and quantum exponentiation
for the literal interval defects. It does not yet prove the
same closure under the source's normal products or hard
stationary contractions, nor an infinite-Laplace growth bound,
a full prefix/cap continuation, or a physical-cycle coefficient.
The filtration (2) controls each stated finite path; it is not
replaced by a globally discrete additive singular set.

## 7. Complete proof direct

| Label | Complete proof source | SHA256 |
|---|---|---|
| D | notes/research_literal_interval_global_borel_log.md | d0885ed0ae7f050ad72d8d128a1edb7bef4200f1b02f624612a8946bbef72a2e |

D supplies only the actual scalar logarithm, its meromorphic
derivative, candidate divisors and endpoint conventions.
The filtered flow, uniform dimension estimates, relative-chain
holomorphic continuation and exponential reconstruction are
proved above. The entire source was read and its used
implications checked.

Only written mathematics, source reads and hash checks were
used. Frozen notes and public manuscripts are unchanged.
