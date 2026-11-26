# The original-source error as a Euclidean boundary-kernel norm

Private written proof, 19 November 2026.

The polynomial Ward primitive sees only a specified vacuum-input
block of the marked current. This note gives an exact positive coherent
resolution for that block in the physical coefficient Euclidean metric,
and an explicit bound for the original-source error by its unnormalized
mixed-kernel \(L^2\) norm. No change of metric is hidden in the bound.

The sole complete direct W supplies the actual primitive, source identity,
and whole-meridian polynomial bounds. The support compression, coherent
resolution, exact Hilbert--Schmidt constant, and metric comparison are
proved here. They do not estimate the required kernel at a geometric
window or select a contributing relative cycle.

## 1. The literal source and the supported current

Fix \(N\ge2\), \(d=N-1\), \(m\ge2\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad M=e^\mu,\quad
 x=-M/q,\quad x_0=-q^{-1}.
 \tag{1}
\]
The quantum root is fixed in every meridian derivative. On the physical
head \(V=\operatorname{span}\{w_0,\ldots,w_d\}\), the vectors \(w_a\)
are orthonormal. All tensor products have the corresponding Euclidean
metric. Write \(Jw_a=aw_a\), \(\Pi_0=|0\rangle\langle0|\), and use
\[
 E(M)w_a=(MQ^{-a}-M^{-1})w_{a-1}\ (a>0),\qquad E(M)w_0=0,
 \qquad K(M)w_a=xQ^{-a}w_a.
 \tag{2}
\]
Put \(Z=V^{\otimes(m-2)}\). The empty spectator tensor for \(m=2\)
means \(Z=\mathbb C\), \(K_Z=I\), and \(E_Z=0\). With the actual
ordered coproduct,
\[
 E_\Sigma=(E_1K_2+E_2)K_Z+E_Z.
\]
The original and top coupons are
\[
 \begin{split}
 Q_{\rm pt}&=\Pi_0\otimes K_2^{-d}\otimes K_Z^{-d},\\
 Q_{\rm top}&=|0\rangle\langle d|\otimes|d\rangle\langle0|
                                      \otimes K_Z^{-d},\\
 \Phi_M(C)&=\operatorname{Tr}(Q_{\rm pt}C),\qquad
 \Delta_M(C)=\Phi_M(C)-\operatorname{Tr}(Q_{\rm top}C).
 \end{split}\tag{3}
\]
The matrix \(C\) may contain arbitrary prescribed marks. Crossing
scalars, framing factors, and any outside normalization remain in
\(C\), or outside every term with their full product rule.

Here is the primitive from W, in notation sufficient for the support
calculation. Let \(Rw_a=w_{a+1}\) for \(a<d\), \(Rw_d=0\), and set
\[
 \mathcal A_{12,0}
 =\sum_{a=0}^{d-1}
   \frac{x_0^{a-d}}{1-Q^{-a-1}}\,|0\rangle\langle a|\otimes R^{a+1}.
 \tag{4}
\]
This \(R\) is the unit raising shift, not a crossing. Define
\[
 h_a(M)=M^{-a}\frac{(Q;Q)_a}{(M^{-2}Q;Q)_a},\quad
 D_h w_a=h_a w_a,\quad
 \mathcal D_{12}=(D_hM^{-J_1})\otimes D_h,
\]
\[
 \mathcal A(M)
 =M^{-d}\mathcal D_{12}\mathcal A_{12,0}\mathcal D_{12}^{-1}
                                                   \otimes K_Z^{-N}.
 \tag{5}
\]
Here \((z;Q)_a=\prod_{j=0}^{a-1}(1-zQ^j)\). W proves, on the
meridian germ and on the scaled collars used below,
\[
 [\mathcal A,E_\Sigma]=Q_{\rm pt}-Q_{\rm top},\qquad
 \Delta_M(C)=\operatorname{Tr}\bigl(\mathcal A[E_\Sigma,C]\bigr).
 \tag{6}
\]
All bottom and top arrows in this identity are the finite physical ones.

Define two fixed orthogonal projections:
\[
 P=\Pi_0^{(1)}\otimes(I-\Pi_0)^{(2)}\otimes I_Z,\qquad
 L=\mathbf1_{\{J_1+J_2\le d-1\}}\otimes I_Z.
 \tag{7}
\]
Every nonzero entry of the summand indexed by \(a\) in (4) sends
\[
             |a,b\rangle\longmapsto |0,b+a+1\rangle,
       \qquad 0\le b\le d-a-1.
 \tag{8}
\]
Its input pair degree is at most \(d-1\), and its second output
occupation lies in \(1,\ldots,d\). The diagonal matrices in (5)
commute with \(P,L\). Consequently, exactly throughout the family,
\[
 \mathcal A=P\mathcal A L,\qquad
 \partial_\mu^k\mathcal A=P(\partial_\mu^k\mathcal A)L.
 \tag{9}
\]
For
\[
                         Y=L[E_\Sigma,C]P
 \tag{10}
\]
cyclicity of the finite trace therefore gives
\[
                         \boxed{\ \Delta_M(C)=\operatorname{Tr}(\mathcal A Y).\ }
 \tag{11}
\]
No hypothesis that \(C\) preserves degree or intertwines a generator
is needed. In particular only this supported current, rather than the
entire commutator, is needed in any trace-, operator-, or
Hilbert--Schmidt-norm estimate from W.

## 2. An exact resolution in the stated metric

For \(z\in\mathbb C\), define the unit vector
\[
 \psi_z=(1+|z|^2)^{-d/2}
                  \sum_{a=0}^d\sqrt{\binom da}\,z^a w_a,\qquad
 d\nu(z)=\frac{d\Re z\,d\Im z}{\pi(1+|z|^2)^2}.
 \tag{12}
\]
The measure has mass one. At infinity the projector extends with
range \(\mathbb Cw_d\); choices of vector phase do not affect the
following integrals. The angular integral removes distinct powers,
and the radial integral gives
\[
 \binom da\int_0^\infty
              \frac{t^a}{(1+t)^{d+2}}\,dt=\frac1{d+1}=\frac1N.
 \tag{13}
\]
For example the substitution \(u=t/(1+t)\), followed by repeated
integration by parts, evaluates the integral as
\(a!(d-a)!/(d+1)!\). Thus, exactly,
\[
                  N\int|\psi_z\rangle\langle\psi_z|\,d\nu(z)=I.
 \tag{14}
\]
Write \(\psi_{\mathbf z}\) for tensor products. If \(Y=YP\), its
first input head is fixed at \(w_0\). Applying (14) on all output
heads and on the remaining input heads proves
\[
 \boxed{\quad
 \|Y\|_{\rm HS}^{\,2}
 =N^{2m-1}\int
  \left|\left\langle\psi_{\mathbf y},
          Y(w_0\otimes\psi_{\mathbf z})\right\rangle\right|^2
                d\nu^{[m]}(\mathbf y)d\nu^{[m-1]}(\mathbf z).
 \quad}\tag{15}
\]
Indeed the output resolution first gives the squared norm of
\(Y(w_0\otimes\psi_{\mathbf z})\); the input resolution then gives
the trace of \(Y^*Y\) on the subspace with first head \(w_0\).
That is its full Hilbert--Schmidt norm because \(Y=YP\).
The second-head factor \(I-\Pi_0\) and the output projection \(L\)
remain inside \(Y\); neither has been replaced by a scalar.

Denote the unnormalized mixed kernel in (15) by
\(\mathcal K_Y(\mathbf y,\mathbf z)\), and its norm for the displayed
probability product measure by \(\|\mathcal K_Y\|_{L^2}\).
Then \(\|Y\|_{\rm HS}=N^{m-1/2}\|\mathcal K_Y\|_{L^2}\).
This includes all occupation caps and every point of the compact
coherent resolutions.

## 3. The exact root constant

In (4), different \(a\)'s have disjoint input columns and
\(\|R^{a+1}\|_{\rm HS}^2=d-a\). At \(M=1\), the spectator scalar
\(K_Z^{-N}\) has modulus one. Hence
\[
 \|\mathcal A_0\|_{\rm HS}^2
 =N^{m-2}\sum_{j=1}^{N-1}
                  \frac{N-j}{|1-Q^j|^2}.
 \tag{16}
\]
The finite polynomial \(p(t)=1+t+\cdots+t^{N-1}\) has roots
\(Q^j\), \(1\le j<N\). Logarithmic differentiation at \(t=1\)
gives
\[
 \sum_{j=1}^{N-1}|1-Q^j|^{-2}
 =\left.\frac{d}{dt}\left(t\frac{p'(t)}{p(t)}\right)\right|_{t=1}
 =\frac{N^2-1}{12}.
 \tag{17}
\]
The first equality uses
\(-Q^j/(1-Q^j)^2=|1-Q^j|^{-2}\). For the last equality use
\(p(1)=N\), \(p'(1)=N(N-1)/2\), and
\(p''(1)=N(N-1)(N-2)/3\). Pairing \(j\) with \(N-j\) in (16)
therefore proves, for every level, including even or composite ones,
\[
                 \|\mathcal A_0\|_{\rm HS}^2
                         =\frac{N^{m-1}(N^2-1)}{24}.
 \tag{18}
\]
Hilbert--Schmidt trace duality and (15) now give the explicit source
bound
\[
 \boxed{\quad
 |\Delta_{M=1}(C)|
 \le
 \sqrt{\frac{N^{3m-2}(N^2-1)}{24}}\,
                       \|\mathcal K_{\,L[E_{\Sigma,0},C]P}\|_{L^2}.
 \quad}\tag{19}
\]
Equivalently the left side is
\(|\Phi_{M=1}(C)-\operatorname{Tr}(Q_{{\rm top},0}C)|\).
The separate root estimates from W remain valid with the same
supported current:
\[
 |\Delta_{M=1}(C)|\le
 \min\left\{\frac N2\|Y_0\|_1,\,
                    \frac{N^m}{2}\|Y_0\|,\,
 \sqrt{\frac{N^{m-1}(N^2-1)}{24}}\|Y_0\|_{\rm HS}\right\}.
 \tag{20}
\]
These are separate trace-duality estimates, not a chain of norm
inequalities. A relative geometric error requires a relative bound
for the actual kernel in (19); (19) does not assert such a bound.

## 4. The whole meridian family and true normals

Let \(C(M)\) be a holomorphic marked matrix on the meridian collar.
Fix \(0<\eta<\eta'<\pi\) and \(m\). W proves on
\(|N\mu|\le\eta\), for each fixed \(k\),
\[
 \|\partial_\mu^k\mathcal A\|
 \le C_kN^k(N+1)^{p_{\eta'}},\qquad
 \operatorname{rank}(\partial_\mu^k\mathcal A)\le dN^{m-2}.
 \tag{21}
\]
The exponent \(p_{\eta'}\) does not depend on \(m\). All displayed
families are holomorphic on the larger buffered collar. Because
\(P,L\) and the coherent frame are independent of \(\mu\), (15)
applies unchanged to every \(\partial_\mu^\ell Y\). The product
rule in (11), followed by (21), yields
\[
 N^{-k}|\partial_\mu^k\Delta_M(C(M))|
 \le C_k(N+1)^{p_{\eta'}}N^{(3m-2)/2}
       \sum_{\ell=0}^k N^{-\ell}
                         \|\mathcal K_{\partial_\mu^\ell Y}\|_{L^2}.
 \tag{22}
\]
The constants may depend on \(m,\eta,\eta'\) and \(k\). No derivatives
of a root-only symbol are used. In particular, with subscripts now
denoting the value and true first derivative at \(\mu=0\),
\[
 Y_0=L[E_{\Sigma,0},C_0]P,\qquad
 Y_1=L\bigl([E_{\Sigma,1},C_0]+[E_{\Sigma,0},C_1]\bigr)P,
\]
\[
 \left.\partial_\mu\Delta_M(C(M))\right|_0
                         =\operatorname{Tr}(\mathcal A_1Y_0+\mathcal A_0Y_1).
 \tag{23}
\]
The left side contains the actual pivot derivatives:
it equals
\(\operatorname{Tr}Q_{{\rm pt},0}(C_1-d(m-1)C_0)
-\operatorname{Tr}Q_{{\rm top},0}(C_1-d(m-2)C_0)\).
An outside scalar is multiplied into every term before differentiation.
Root commutation alone kills \(Y_0\), not \(Y_1\).

## 5. Why the metric and the mixed kernel matter

The other common coherent metric has
\(\|w_a\|_{\rm bin}^2=\binom da^{-1}\), so its orthonormal basis is
\(u_a=\sqrt{\binom da}\,w_a\). It is not the metric of (12)--(22).
This distinction is visible in this very primitive. On the root
input \((a,d-a-1)\) and output \((0,d)\), its matrix entry in the
binomial orthonormal basis has modulus
\[
 \frac{\sqrt{\binom da\binom d{a+1}}}{|1-Q^{-a-1}|}.
 \tag{24}
\]
Take \(a=\lfloor(d-1)/2\rfloor\). The largest binomial coefficient
is at least \(2^d/(d+1)\), its indicated adjacent coefficient is at
least half as large, and \(|1-Q^{-a-1}|\le2\). Thus (24) is at least
\(2^d/(2\sqrt2(d+1))\). This particular primitive has exponential
binomial-metric norm. This does not claim the same lower bound for
every possible Ward primitive.

The top source is the mixed corner
\(\langle d,0|C|0,d\rangle\), with spectators closed by their
literal pivot. In (12), \(w_0\) and \(w_d\) are the two antipodal
coherent endpoints. Their identity overlap is zero for \(N\ge2\).
Consequently (15) uses the unnormalized mixed kernel and never
divides by an identity overlap such as \((1+wz)^d\).

Local normalized symbol estimates, estimates in the binomial metric,
and estimates on a small output disk do not by themselves bound the
full integral in (15). The bridge retains the original source and
all its true normals, but supplies no geometric window, mixed-kernel
decay estimate, opposite-polarization return, or nonzero closing
coefficient. No new volume-conjecture case is asserted.

## Complete direct and author verification

* W: [research_polynomial_top_source_ward_transport.md](research_polynomial_top_source_ward_transport.md),
  376 lines, SHA256
  \(\texttt{fe6493819fa24ce3ccf27b4625be57f34513d6542830f9aeb591fed6e495d8ad}\).

The complete direct was freshly read nontruncated in two covering
chunks in this author sequence. Its literal source, primitive,
meridian frame, cap, and polynomial jet implications were checked.
Only written mathematics and text/hash operations were used.
No mathematical programs, numerical tests, builds, or frozen-file
edits were performed. The entire matching final was freshly reread
nontruncated after the final notation and holomorphy clarifications;
its direct and final pins were then renewed. Independent matching-final
review and parent adoption remain separate.
