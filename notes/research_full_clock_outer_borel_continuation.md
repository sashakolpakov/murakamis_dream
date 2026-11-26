# Joint continuation of the actual full-clock Borel family

Private written proof, 18 November 2026.

The initial full-clock family continues jointly along every fixed
compact path on its exceptional square-root cover away from the fold.
The transverse convergence radius is independent of all clock values.
The proof uses a norm bound for the whole Cauchy density and retains
the factorials in the transverse clock coefficients. It does not
estimate the individual graph coefficients.

## 1. The original family and the asserted continuation

Keep the original highest-cut source and the actual simple two-branch
node assumptions of [D]. Write
\[
 z=Y-\alpha,\qquad h=z^2\varepsilon,\qquad m=\nu/z,\qquad
 F(z,\eta,\nu)
       =z\,\mathcal B_h\mathscr W_{\nu/z}(\alpha+z,z^2\eta),
 \tag{1}
\]
with its holomorphic extension through \(z=0\) from [D]. The Borel
convention is \(\varepsilon^j\mapsto\eta^j/j!\).
Use the nonzero constants and vector in the actual profile
\[
 F(0,\eta,\nu)=\frac r w e^{(\mu\cdot\nu)a(w)},\qquad
 w^2=1-4\sigma\eta,\qquad w(0)=1,\qquad
 a(w)=\frac{1-w}{2\sigma}.
 \tag{2}
\]
The independent marks are all the path coordinates of the fixed word.
By [T], \(\mu\ne0\). Set
\[
 v=-\beta(\alpha)/\alpha,\qquad \mu\cdot v=1,
 \qquad
 \nu=\lambda v+J\omega,\qquad
 \lambda=\mu\cdot\nu,
 \tag{3}
\]
where the columns of a fixed matrix \(J\) form a basis of
\(\ker\mu\). Thus \(\omega\in\mathbb C^{d-1}\) retains all the
remaining clock coordinates. If \(d=1\), these coordinates are empty.

**Theorem.** Let a finite compact \(w\)-path start in the original
neighborhood of \(w=1\) and avoid zero. There is a bounded open
neighborhood \(U\Subset\mathbb C^*\) of that path and a number
\(\rho_U>0\) such that the actual family (1) continues to
\[
             |z|<\rho_U,\qquad w\in U,\qquad \nu\in\mathbb C^d.
 \tag{4}
\]
It is jointly holomorphic there and entire in all clocks. The
\(z\)-radius is independent of the clock values.

For suitable constants \(M_U,B_U,c,R>0\), on a smaller closed
neighborhood of the path and \(B_U|z|<1\),
\[
 |F(z,w,\lambda v+J\omega)|
  \le \frac{M_U}{1-B_U|z|}
       \exp\!\left(R|\lambda|
                     +c\sqrt{B_U|z|}\,\|\omega\|_1\right).
 \tag{5}
\]
In particular the continued clock type stays finite. The bound
is not uniform as the path approaches \(w=0\).

This is an outer continuation theorem about the actual source near
the exceptional divisor \(z=0\). It does not locate its singular set
at a fixed nonzero \(z\), produce a regular moving minor, or identify
the closed physical scalar.

## 2. Uniform initial estimates with their clock factorials

The initial theorem [D] supplies fixed product disks and constants
with
\[
               |F(z,\eta,\nu)|\le M e^{C\|\nu\|_1}
 \tag{6}
\]
on smaller closed disks, for every complex clock vector. Choose
\(0<\epsilon<1\) so that
\[
 \eta(w)=\frac{1-w^2}{4\sigma},\qquad |w-1|\le\epsilon,
 \tag{7}
\]
stays in that initial \(\eta\)-disk. Take a fixed positive
\(z\)-coefficient circle inside its initial disk. Cauchy's estimate
on that circle, and the fixed linear change (3), give
\[
 F(z,w,\lambda v+J\omega)=\sum_{k\ge0}z^kF_k(w,\lambda,\omega),
 \quad
 |F_k|\le M_0A^k
              e^{C_\lambda|\lambda|+C_\omega\|\omega\|_1}.
 \tag{8}
\]
Increase the constants so \(C_\lambda,C_\omega\ge1\).
They are independent of \(k,\lambda,\omega\).

The exact finite-core theorem [C] says that \(F_k\) is a polynomial
of degree at most \(2k\) in \(\omega\):
\[
                 F_k=\sum_{|\gamma|\le2k}
                           \omega^\gamma f_{k,\gamma}(w,\lambda).
 \tag{9}
\]
Its coefficients remain entire in \(\lambda\).
Cauchy extraction in \(\omega_i\) at radius
\(\gamma_i/C_\omega\), for positive \(\gamma_i\), gives
\[
 |f_{k,\gamma}(w,\lambda)|
       \le M_0A^k e^{C_\lambda|\lambda|}
                        \frac{c^{|\gamma|}}{\gamma!},
               \qquad c=eC_\omega .
 \tag{10}
\]
Coordinates with zero exponent are set to zero during extraction.
Indeed the optimized bound is
\(\prod(eC_\omega/\gamma_i)^{\gamma_i}\), which is at most
\(c^{|\gamma|}/\gamma!\).
Keeping this factorial, rather than extracting on a fixed unit
clock circle, is essential for the clock-independent radius in (4).

## 3. The canonical longitudinal density and its source class

For \(|w-1|\le\epsilon\), define the canonical exterior density
\[
 g_{k,\gamma}(w,\theta)
       =\sum_{n\ge0}
           \partial_\lambda^n f_{k,\gamma}(w,0)\,
                                      \theta^{-n-1}.
 \tag{11}
\]
From (10), optimized Cauchy estimation in \(\lambda\) yields
\[
 |\partial_\lambda^n f_{k,\gamma}(w,0)|
       \le M_0A^k\frac{c^{|\gamma|}}{\gamma!}
                                      (eC_\lambda)^n.
 \tag{12}
\]
Choose \(R>eC_\lambda\), also larger than every \(|a(w)|\) on
a fixed bounded neighborhood of the desired \(w\)-path.
On the initial product contour
\(\mathbb T=\{|w-1|=\epsilon,\ |\theta|=R\}\), (11) converges
normally and satisfies
\[
 \sup_{\mathbb T}|g_{k,\gamma}|
          \le M_1 A^k\frac{c^{|\gamma|}}{\gamma!}.
 \tag{13}
\]
Termwise Cauchy integration gives the exact identity
\[
 f_{k,\gamma}(w,\lambda)
       =\frac1{2\pi i}\int_{|\theta|=R}
                         e^{\lambda\theta}g_{k,\gamma}(w,\theta)
                                                        \,d\theta.
 \tag{14}
\]

There is more information here than an exponential-type estimate.
The source calculation [C] gives
\[
 g_{k,\gamma}(w,\theta)
   =\frac{A_{k,\gamma}(w,\theta)
            +B_{k,\gamma}(w,\theta)
                         \log(1-a(w)/\theta)}
          {w^{r_{w,k}}\theta^{r_{0,k}}
                              (\theta-a(w))^{r_{a,k}}},
 \tag{15}
\]
where the numerators are polynomials and, for one fixed \(C_0\),
\[
 \max(\deg_w A_{k,\gamma},\deg_\theta A_{k,\gamma},
      \deg_w B_{k,\gamma},\deg_\theta B_{k,\gamma})
             +r_{w,k}+r_{0,k}+r_{a,k}+1
                   \le C_0(k+1).
 \tag{16}
\]
The same bounds hold for every \(\gamma\). The logarithm in (15)
has its original exterior branch. The scalar coefficients of these
polynomials need no separate bound.

To identify [C]'s representative with (11), note that its endpoint
and segment Cauchy transforms, and all their spectral derivatives,
have only negative Laurent powers at infinity. Their moments are
exactly \(f_{k,\gamma}\). Equality of those negative Laurent
coefficients identifies the two densities on their common exterior.
No quotient equation has been promoted to an unprojected density
equation in this step.

## 4. Joint continuation and normal summation of all corrections

Apply the product-contour estimate [P] to (15), using (13).
For every fixed continued compact \(K\) away from
\[
                          w\theta(\theta-a(w))=0,
 \tag{17}
\]
its degree bound (16) gives constants independent of \(k,\gamma\):
\[
             \sup_K|g_{k,\gamma}|
                  \le M_K B_K^k
                                \frac{c^{|\gamma|}}{\gamma!}.
 \tag{18}
\]
The estimate of [P] is homogeneous in the initial norm. It therefore
preserves the complete factorial factor in (13). In particular no
bound on individual graph coefficients or on the summands of (15)
is being substituted for the norm of their sum.

Define on such a chart
\[
 G(z,w,\theta,\omega)
      =\sum_{k\ge0}z^k
                   \sum_{|\gamma|\le2k}
                           \omega^\gamma g_{k,\gamma}(w,\theta).
 \tag{19}
\]
Put \(t=B_K|z|<1\). Equations (18)--(19) give
\[
 \begin{split}
 |G|
  &\le M_K\sum_{k\ge0}t^k
              \sum_{|\gamma|\le2k}
                    \frac{c^{|\gamma|}|\omega^\gamma|}{\gamma!}\\
  &\le\frac{M_K}{1-t}
                    \exp(c\sqrt t\,\|\omega\|_1).
 \end{split}
 \tag{20}
\]
For the last inequality, reverse the absolutely nonnegative
majorant sums. A multiindex of degree \(j\) first occurs at
\(k=\lceil j/2\rceil\), so its summed weight is
\(t^{\lceil j/2\rceil}/(1-t)\le t^{j/2}/(1-t)\).
The multinomial exponential series finishes the estimate.

Thus (19) converges normally in \(z,w,\theta\) and on every compact
clock set, with one positive \(z\)-radius for all \(\omega\).
It is jointly holomorphic and entire in the transverse clocks.
The same estimates hold on compact neighborhoods after increasing
the constants once.

## 5. Reconstructing the actual continued clock source

Choose a bounded open neighborhood \(U\Subset\mathbb C^*\) of the
given \(w\)-path and its starting neighborhood. Take \(R\) as in
Section 3 with a positive margin outside all \(a(w)\), \(w\in U\).
Use a slightly smaller closed neighborhood and a buffered annulus
about the circle \(|\theta|=R\). Their product is a compact set
of the form required in (18), with the exterior logarithm.
All three divisor distances are positive.

Define
\[
 \widetilde F(z,w,\lambda,\omega)
       =\frac1{2\pi i}\int_{|\theta|=R}
                  e^{\lambda\theta}G(z,w,\theta,\omega)\,d\theta.
 \tag{21}
\]
Normal convergence justifies the integral, its derivatives, and
termwise reconstruction. Equations (9), (14), and (19) show that
(21) equals the original family on its initial product disk.
It is consequently continuation of that actual family, rather than
a new solution chosen from the formal equations.

The contour has length \(2\pi R\); (20) gives (5), after absorbing
the fixed factor \(R\) into \(M_U\). It is entire in \(\lambda,\omega\).
Different sufficiently large circles give the same integral on
overlapping domains, by Cauchy's theorem on the intervening annulus.
Both circles enclose both endpoints and retain their connecting
source contribution. The logarithm is its unique exterior series
throughout that annulus.

On overlapping \(w\)-neighborhoods these constructions agree first
in their original germs and then by analytic uniqueness; a common
larger exterior circle also gives the same comparison directly.
This proves the asserted joint continuation along the whole finite
path. Each path has its own positive radius, as in (4).

## 6. Consequences and limits of the argument

The proof pays continuation of the whole marked family with all
clocks, rather than a fixed finite collection of moments. It also
constructs its longitudinal Cauchy density on continued charts
away from the three displayed divisors, with the transverse clocks
retained as entire parameters.

The \(w\)-cover in this theorem is the exceptional square-root
coordinate. The permissible \(z\)-radius can shrink as \(w\to0\).
For fixed nonzero \(z\), this result does not identify a moving
singular divisor or the support of a regular marked minor. It does
not establish multiplicative clock ratios on that divisor.

The spectral contour in (21) surrounds both endpoints. Extracting
only one endpoint or canceling an interior zero of a Ward factor
still needs an argument about the actual period class. No boundary
factor, framing scalar, source connector or physical endpoint
current has been removed here. The geometric branch and original
closed scalar lower bound remain outside this theorem.

## 7. Proof directs

| Label | Complete direct source | SHA256 |
|---|---|---|
| D | notes/research_full_clock_initial_borel_family.md | d498ddfad641c85bba0257d22dcad53679ccd2cfb7e0c16f6cc790444f9e9b77 |
| T | notes/research_classical_clock_torus_meridian_adapter.md | 7fbcc973a55eb6f38156b9efb0b18121bc248e5e0d60ed213728ad19f53fc515 |
| C | notes/research_actual_clock_finite_core_volterra_carriers.md | 7c7630796cb2d7ee2e81d0efceb9c9008bbb5214169ce4da5b76f068c0341d9a |
| P | notes/research_two_variable_polynomial_log_continuation_bound.md | 8d7966c484f535c06421d54a0569ffea6eb572cd4bd5abbc114a876401a3d3a1 |

D supplies the actual convergent initial family and its uniform clock
type. T supplies the nonzero full-clock direction and its explicit
dual. C supplies the exact finite-core identity, polynomial transverse
degree and joint polynomial-log Cauchy class. P supplies the
whole-density norm continuation estimate. The factorial extraction,
canonical exterior identification, uniform all-clock summation and
reconstruction of the actual continued family are proved here.

The entire final and all complete proof directs were read, and their
used implications checked. Only written mathematics and text/hash
operations were used. Frozen proofs and public manuscripts are unchanged.
