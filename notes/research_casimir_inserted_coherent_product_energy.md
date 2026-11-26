# Fixed polynomial insertions preserve the coherent product rate

Written research proof, 22 November 2026.

The full original centered tensor has an exact polynomial-insertion
identity with an explicit value-and-normal source. On its generating
norm wall, that source vanishes and every fixed-degree insertion is
an explicit scalar multiplier, uniformly close to evaluation at the
classical common Casimir. Combined with the coherent product energy
theorem, this proves that every fixed nonzero Casimir polynomial
preserves the full output exponential rate.

The norm is the centered coefficient Euclidean norm, equivalently
the declared positive Newton Gram. It is not the uniform physical
Hilbert--Schmidt metric. No equivalence to that other metric, or a
lower bound after an arbitrary final closing, is assumed.

## 1. Original tensor and inserted periods

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\qquad
 D_N(t)=1-\eta t^N,
\]
\[
 P_N(\zeta)=2T_N(\zeta/2)+2,\qquad
 \mathcal H_N=\mathbb C[\zeta]/(P_N).
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind. All
fractional powers mean the displayed exponential. Use the original
Frobenius trace \(\phi_N\), positive crossing \(R\), and centered
orthonormal coefficient basis
\[
 f_a=N^{-1/2}R\,p_a(\zeta),\qquad
 A_N(t,\zeta)=\sum_{a=0}^dp_a(\zeta)t^a .
 \tag{2}
\]
For an ordinary polynomial \(P\), set
\[
 \Phi_{N,P}(\mathbf t)=N^{-3/2}\phi_N\!\left[
       P(\zeta)R^3\prod_{i=1}^3A_N(t_i,\zeta)\right],
 \qquad \mathcal C_N=\Phi_{N,1}.
 \tag{3}
\]
These are the original full Hermite periods. Every double Casimir
root retains its first normal; the last odd-level root is simple.
Write \(e_1,e_2,e_3\) for the elementary symmetric polynomials in
\(\mathbf t=(t_1,t_2,t_3)\).

The common insertion operator is
\[
 Z_iF=
 \frac{(1+q^{-1}t_i)^2F(t_1,\ldots,Q^{-1}t_i,\ldots,t_3)
                         -(1+t_i^2)F(\mathbf t)}{t_i}.
 \tag{4}
\]
Its numerator vanishes at \(t_i=0\). On polynomials of degree below
\(N\) in that argument it remains of degree below \(N\): the apparent
top coefficient is \(q^{-2}Q^{-d}-1=0\). The exact forced equation
for \(A_N\), reduced in \(\mathcal H_N\), proves
\[
                    Z_i\Phi_{N,P}=\Phi_{N,\zeta P}.
 \tag{5}
\]
In particular \(Z_i\mathcal C_N=Z_j\mathcal C_N\), with the full
source rather than only its distinct spectral values.

## 2. A polynomial Pearson operator with its full source

Introduce a Laurent variable \(v\), and put
\[
 \zeta(v)=v+v^{-1},\quad
 U(v)=\prod_{i=1}^3(1+vt_i),\quad
 V(v)=\prod_{i=1}^3(v+t_i).
\]
For any polynomial \(P\), define
\[
 K_P(v)=v^{-1}\left[
      Q\,U(v)P(\zeta(v))
          +q^3 V(v)P(\zeta(Qv))\right],
\]
\[
 \boxed{\qquad
 (\mathcal L_{\mathbf t}P)(\zeta(v))
       =\frac{K_P(v)-K_P(v^{-1})}{Q(v-v^{-1})}.
 \qquad}
 \tag{6}
\]
The numerator is inversion-odd. Each difference \(v^a-v^{-a}\)
is divisible by \(v-v^{-1}\), with invariant polynomial quotient.
Thus (6) is an ordinary polynomial in \(\zeta\), including the
removable values \(v=\pm1\). If \(P\) is monic of degree \(k\),
its degree is at most \(k+1\), and its coefficient of \(\zeta^{k+1}\) is
\[
                         e_3+qQ^k.
 \tag{7}
\]
Indeed the coefficient of \(v^{k+2}\) in \(K_P\) is
\(Qe_3+q^3Q^k\), whereas its least possible power is \(-k-1\).
Taking the odd part and dividing as in (6) proves (7).

Let \(c_0=q+q^{-1}\). The exact inserted source identity is
\[
 \boxed{\quad
 \Phi_{N,\mathcal L_{\mathbf t}P}(\mathbf t)
       =S_N(\mathbf t)\,\epsilon_N(P),\qquad
 S_N=-\frac{\eta q^{-1}\kappa^3}{N^{3/2}}
                         \prod_{i=1}^3D_N(t_i),\qquad
 \epsilon_N(P)=P(c_0)+2(q-q^{-1})P'(c_0).
 \quad}
 \tag{8}
\]
The derivative in this source is required. Its proof follows without
assigning a normal by interpolation of ordinary values.

Put \(v_j=qQ^j\), \(0\le j<N\), and \(D=v\partial_v\). For a
Laurent germ define \(\mathfrak T(F)=\sum_j(DF)(v_j)\). Reindexing
the grid gives \(\mathfrak T(F(Qv))=\mathfrak T(F(v))\).
The literal original trace has the circle expression
\[
 \phi_N(F(\zeta))=-\frac{\eta}{2}
       \mathfrak T\!\left[(v-v^{-1})F(\zeta(v))\right].
 \tag{9}
\]
At a paired double root \(c=v+v^{-1}\),
\(D[(v-v^{-1})F]=cF+(c^2-4)F'\); the two occurrences give
the exact value-and-normal trace weights. At the odd fixed root
\(v=-1\), the same expression is \(-2F(-2)\), yielding its
simple-node weight one since then \(\eta=1\).

For clarity we verify every first jet in the ensuing finite shift.
The full-tensor products are
\[
 A_N(t,c_j)=D_j(t)^2B_j(t),\quad
 D_j(t)=\prod_{r=-j+1}^{0}(1+q^{-1}Q^rt),\quad
 B_j(t)=\prod_{r=j+2}^{N-j}(1+q^{-1}Q^rt)
 \tag{10}
\]
for \(0\le j\le\lfloor d/2\rfloor\), with empty products allowed.
Their independent spectral normal is
\(\partial_\zeta A_N=D_j^2tB_j'/(v_j-v_j^{-1})\) at double
nodes. Thus, for \(\ell_j(t)=D\log A_N(t,\zeta(v))|_{v=v_j}\),
\[
 \ell_j=tB_j'/B_j,\qquad
 \ell_{d-j}=-\ell_j.
 \tag{11}
\]
At the odd simple node the lifted \(v\)-derivative is zero, and
the empty \(B_j\) gives the same value.
Deleting the two end factors of \(B_j\) gives, for \(j<d\),
\[
 \frac{A_N(t,c_{j+1})}{A_N(t,c_j)}
    =\frac{1+v_j^{-1}t}{1+Qv_jt},\qquad
 \ell_{j+1}-\ell_j
    =-\frac{v_j^{-1}t}{1+v_j^{-1}t}
                        -\frac{Qv_jt}{1+Qv_jt}.
 \tag{12}
\]
At the even middle pair \(Qv_j=v_j^{-1}\), the one-factor
\(B_j\) makes this difference \(-2\ell_j\), as required.
At the odd center \(B_j=1\); its neighbors have two factors,
so the same formula holds. The second half follows by inversion.
All rational equalities extend after clearing denominators.

The original crossing has the full circle data
\[
 R(c_j)=\kappa(-1)^jq^{j(j+1)},\qquad
 D\log R(\zeta(v))|_{v_j}=j-d/2.
 \tag{13}
\]
For the second formula on the first half, multiply the original
spectral logarithmic derivative
\(i(N-2j-1)/(4\sin((2j+1)\pi/N))\) by \(v_j-v_j^{-1}\).
Inversion proves the other half; the odd fixed node again has
lifted derivative zero. For every \(j<d\) the crossing shift has
value ratio \(-qv_j\) and logarithmic derivative difference one.

Now let
\[
 H(v)=R(\zeta(v))^3\prod_iA_N(t_i,\zeta(v)),\qquad
 E(v)=U(Qv)H(Qv)+q^3V(v)H(v).
\]
Equations (12)--(13) show \(E(v_j)=(DE)(v_j)=0\) for \(j<d\).
At the remaining seam \(s=v_d=q^{-1}\), use inversion symmetry
of the actual polynomial \(H\), rather than an incorrect periodic
extension of its crossing phase. Write
\[
 H(s)=H(q)=H_0,\qquad (DH)(q)=-(DH)(s),\qquad
 G=U(Qs)=q^3V(s)=\prod_i(1+qt_i).
\]
The two scalar logarithmic derivatives in \(E\) sum to three:
\(\sum_i[qt_i/(1+qt_i)+1/(1+qt_i)]=3\).
Consequently the full seam has
\[
                         E(s)=2GH_0,\qquad (DE)(s)=3GH_0.
 \tag{14}
\]
Multiplying by \(P(\zeta(Qv))/v\) before taking the circle
derivative therefore gives
\[
 \mathfrak T\!\left[v^{-1}P(\zeta(Qv))E(v)\right]
       =qGH_0\{P(c_0)+2(q-q^{-1})P'(c_0)\}.
 \tag{15}
\]
The derivative term comes from
\(D\zeta(Qv)|_{s}=q-q^{-1}\), multiplied by the nonzero
seam value \(2GH_0\).

Reindex the first term on the left of (15). It becomes
\(\mathfrak T(K_PH)\). Since \(H(v)=H(v^{-1})\),
the inversion-even part of \(K_P\) contributes zero to
\(\mathfrak T\). Equations (6) and (9) give
\[
                 \mathfrak T(K_PH)
       =-\eta Q\,\phi_N((\mathcal L_{\mathbf t}P)H).
\]
Finally (10) at \(j=0\) gives
\[
 GH_0=\kappa^3\prod_i(1+qt_i)B_0(t_i)
                         =\kappa^3\prod_iD_N(t_i).
\]
Substitution in (15) proves (8), including its phase and normal.

The operator is independent of the polynomial representative in the
full quotient. Indeed \(Q^N=1\) gives
\[
 P_N(\zeta(Qv))=P_N(\zeta(v)),\qquad
       \mathcal L_{\mathbf t}(P_NS)=P_N\mathcal L_{\mathbf t}S.
 \tag{16}
\]
Also \(P_N(c_0)=P_N'(c_0)=0\), for every \(N\ge2\).
Thus both sides of (8) descend to \(\mathcal H_N\), with its
nilpotents. No simple-root substitution is used at this seam.

## 3. Exact moment propagation and a fixed-degree estimate

For \(P=1\), (6) is the already-known common affine equation:
\[
 \mathcal L_{\mathbf t}1
    =(q+e_3)\zeta+e_2+qe_1-1-qe_3 .
 \tag{17}
\]
It is equivalent to the initialized forced Rogers connection.
The new use here is its inserted identity (8), including the
source normal and a controlled fixed-degree observation.

Fix \(D<\infty\) and \(0<\rho<1\), and consider
\[
       |t_1|\le1,\qquad |t_2|,|t_3|\le\rho .
 \tag{18}
\]
For \(0\le k<D\), write
\[
 \mathcal L_{\mathbf t}(\zeta^k)
      =a_k\zeta^{k+1}+\sum_{r=0}^k b_{kr}\zeta^r,\qquad
                         a_k=e_3+qQ^k .
 \tag{19}
\]
Every \(a_k\) has modulus at least \(1-\rho^2\).
Set \(m_k=\Phi_{N,\zeta^k}\). Equation (8) gives
\[
 a_km_{k+1}+\sum_{r=0}^kb_{kr}m_r
                           =S_N\epsilon_N(\zeta^k).
 \tag{20}
\]
Induction therefore defines explicit analytic coefficients
\(r_{N,k},b_{N,k}\), with \(r_{N,0}=1,b_{N,0}=0\), such that
\[
                     m_k=r_{N,k}\mathcal C_N+b_{N,k}S_N
                              \quad(0\le k\le D).
 \tag{21}
\]
No division by \(\mathcal C_N\) occurs. For
\(P=\sum_{k=0}^D p_k\zeta^k\), put
\(r_{N,P}=\sum p_kr_{N,k}\) and
\(b_{N,P}=\sum p_kb_{N,k}\).

Define the classical common Casimir
\[
              \Lambda(\mathbf t)
                    =1-\frac{e_1+e_2}{1+e_3}.
 \tag{22}
\]
Uniformly on (18), the finite coefficient formula (6) tends, as
\(q\to1\), to multiplication by
\((1+e_3)(\zeta-\Lambda)\). For each fixed \(k\), the
coefficient error is \(O_{\rho,k}(N^{-1})\): only finitely many
Laurent powers of \(q\) occur, with \(q-1=O(N^{-1})\).
All coefficients remain bounded on (18), and the same is true of
\(\epsilon_N(\zeta^k)\). The nonvanishing bound for \(a_k\)
and induction in (20) consequently prove
\[
 r_{N,P}=P(\Lambda)+O_{\rho,D}(\|P\|_{\rm coeff}/N),\qquad
             |b_{N,P}|\le C_{\rho,D}\|P\|_{\rm coeff},
 \tag{23}
\]
where \(\|P\|_{\rm coeff}=\sum_k|p_k|\).
Since \(|S_N|\le8N^{-3/2}\), this gives the actual estimate
\[
 \boxed{\quad
 |\Phi_{N,P}-P(\Lambda)\mathcal C_N|
       \le C_{\rho,D}\|P\|_{\rm coeff}
             \left(N^{-1}|\mathcal C_N|+N^{-3/2}\right).
 \quad}
 \tag{24}
\]

There is no scalar leading-coefficient resonance in (19) on this
domain, even when \(k\) approaches \(N\). This does not extend the
fixed-\(D\) constants uniformly to degrees of order \(N\).
At \(k=N-1\), the next monomial is already constrained by the
characteristic relation \(P_N\); it is not a new independent moment.
The exact identity (8) still holds for every polynomial, but no
boundedly conditioned full-channel moment solver is asserted.

## 4. Consequence for the full coherent output energy

Write \(\mathbb D=\{t\in\mathbb C:|t|<1\}\).
Let \(\mathcal F_N(t)=\sum_{a=0}^df_at^a\), and use normalized
coherent inputs
\[
 \xi_N(t)=\mathcal F_N(t)/\sqrt{Z_N(t)},\qquad
                         Z_N(t)=\sum_{a=0}^d|t|^{2a}.
\]
For \(|y|,|z|<1\), retain the original multiplication and define
\[
 w_N^P(y,z)=P(\zeta)\,\xi_N(y)\xi_N(z),\qquad
                  E_N^P(y,z)=\|w_N^P(y,z)\|_{\rm coeff}^2 .
 \tag{25}
\]
This is the full coefficient norm of the actual output packet.
Its generating polynomial, before the two input normalizations,
is \(\Phi_{N,P}(x,y,z)\). Indeed the original bilinear dual
of \(f_c\) is \(f_c\), so its coefficient is
\(\phi_N(f_cP\mathcal F_N(y)\mathcal F_N(z))\).
Every output index \(0\le c<N\) remains present.

At the generating wall \(X_j=-qQ^j\), \(0\le j<N\),
\(D_N(X_j)=0\). Finite Fourier Parseval therefore gives exactly
\[
 E_N^P(y,z)=\frac1{N Z_N(y)Z_N(z)}
      \sum_{j=0}^{N-1}|\Phi_{N,P}(X_j,y,z)|^2,\qquad
 \Phi_{N,P}(X_j,y,z)
                 =r_{N,P}(X_j,y,z)\mathcal C_N(X_j,y,z).
 \tag{26}
\]
The second equality uses the full identity (21), not a homogeneous
replacement before taking the wall. This generating grid is an
invertible coordinate system on all \(N\) output coefficients;
it is not evaluation at only distinct physical Casimir roots.

Use the coherent product energy theorem for \(P=1\).
For each \((y,z)\in\mathbb D^2\) its actual positive wall sum
has one strict positive nondegenerate maximum, at a bulk point
\(u_*(y,z)\in(0,1)\). Write its rate as \(\mathcal E(y,z)>0\).
The theorem gives
\[
                    \frac1N\log E_N^1(y,z)
                                    \longrightarrow\mathcal E(y,z)
 \tag{27}
\]
locally uniformly, and supplies the actual wall product profile
uniformly on bulk intervals. Its endpoint layers are included
in the global bound; they are not additional discarded sectors.

**Theorem.** For every fixed nonzero complex polynomial \(P\),
\[
             \boxed{\qquad
             \frac1N\log E_N^P(y,z)\longrightarrow\mathcal E(y,z),
                            \qquad (y,z)\in\mathbb D^2.
             \qquad}
 \tag{28}
\]
The convergence is locally uniform. In particular the full output
norm has rate \(\mathcal E/2\), unchanged by this insertion.

For the upper bound, (23) bounds \(r_{N,P}\) uniformly at every
wall point on compact subsets of \(\mathbb D^2\). Equation (26)
then gives \(E_N^P\le C E_N^1\).
For the lower bound it is not necessary that \(P\) be nonzero at
the maximizing Casimir. With \(x\) variable,
\[
 \partial_x\Lambda(x,y,z)
       =-\frac{(1+y)(1+z)(1-yz)}{(1+xyz)^2}\ne0
                \quad(|x|=1,\ |y|,|z|<1).
 \tag{29}
\]
Thus \(P(\Lambda(-e^{2\pi iu},y,z))\) cannot vanish on an
interval around \(u_*\). Choose a nearby bulk interval on which
its modulus is positive and the energy profile is within any
prescribed \(\varepsilon>0\) of its maximum.
Equation (23) gives the same lower bound for \(|r_{N,P}|\)
there for large \(N\). The actual wall profile and (26) yield
\(\liminf N^{-1}\log E_N^P\ge\mathcal E-\varepsilon\).
Let \(\varepsilon\) decrease to zero.

The reasoning is uniform on compact parameter sets. The maximizing
points stay in a common bulk interval and vary continuously.
Choose a common sufficiently small radius around them so that the
profile stays above \(\mathcal E-\varepsilon\) on each resulting
interval. The unweighted integral of \(|P\circ\Lambda|^2\) on
that interval is positive by (29), and is continuous in the
parameters. It therefore has a uniform positive lower bound on
the compact parameter set. Uniform convergence in (23) and
Riemann sums give the same bound for
\(N^{-1}\sum|r_{N,P}(X_j,y,z)|^2\) over those intervals.
The actual uniform bulk wall profile in (26) now proves
\(\liminf N^{-1}\log E_N^P\ge\mathcal E-\varepsilon\)
uniformly there. Letting \(\varepsilon\) decrease proves (28).
No polynomial prefactor is claimed when \(P\) vanishes at the maximum.

For a general incoming component \(B_N=\sum_a u_{N,a}f_a\),
sewing one leg is represented exactly by
\(P_{B_N}=\sum_a u_{N,a}p_a=\sqrt N R^{-1}B_N\), at \(t_1=0\)
in (3). Its degree can be \(N-1\).
The exact identity (8) applies, but the fixed-degree estimate (24)
and rate theorem (28) do not supply uniform constants for that
general sequence. Fixed crossing powers are not silently treated
as fixed-degree Casimir polynomials.

## 5. Scope and proof sources

The inserted identity retains the original crossing phases, the
complete Frobenius value-and-normal trace, both level parities and
the \(N=2\) seam. Its degree refers to the inserted Casimir
polynomial, not to the degree-four variational objective.
The result stabilizes a full positive output energy.
It neither changes the original final closing nor proves that its
projection onto this output has a nonzero geometric coefficient.
No new finite-exception theorem or knot class is asserted.

Both complete matching proof sources were read:

| Source | SHA-256 |
|---|---|
| [Full tensor source, 482 lines](research_centered_fourier_full_tensor_source.md) | 8426410354feb509c2780e1207613899bda8ab5eb46ad22fd4ab008bf5841bf1 |
| [Coherent product energy, 393 lines](research_centered_coherent_product_energy.md) | 73152328a77ba5d63a2a8eaa17647ed38b7683c613e0947e3bda9e451dda76e2 |

For coverage, the complete common-Casimir note, forced Rogers note,
full-degree generating-section note, wall-Cauchy source, bounded
quotient/Ward-homotopy note and projected-node Ward-source note were
read. They already supply the \(P=1\) equation, original finite
coefficient sewing and several distinct source-aware Ward procedures.
No novelty is claimed for those equations or for fixed-degree
semiclassical observation in general. The finite inserted operator,
its source normal, and the output-energy consequence are proved here.
No mathematical programs, experiments, tests, builds, git operations,
or edits of earlier finals were used.
