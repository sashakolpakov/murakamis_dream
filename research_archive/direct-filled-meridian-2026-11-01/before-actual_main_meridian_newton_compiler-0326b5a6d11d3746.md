# Computing oriented tangles as the main meridian varies

1 November 2026.

A two-strand tangle is a piece of a knot diagram inside a box, with four ordered boundary points. Its quantum operator can be encoded by a polynomial in the two-strand Casimir. Turning or joining boxes then becomes a finite calculation on polynomial coefficients. The main meridian parameter is the eigenvalue assigned to a small loop around the knot itself; it is distinct from any auxiliary crossing-circle color.

There are two distinct operations in a main-meridian deformation: changing the polynomial coordinates of a coupon, and changing the multiplication and turn tensors of the physical source. A bound for the first operation does not by itself control the second: [products that vanish at completeness can acquire nonzero coefficients](actual_main_meridian_newton_multiplication.md). This note proves the polynomial basis bound, constructs an exact formal compiler for a fixed oriented Conway tree, and retains the actual primitive closing trace. The separate [quarter-turn comparison](actual_main_meridian_turn_comparison.md) now computes all six physical turn types in fixed polynomial coordinates and bounds them relative to the complete turn. The closing normalization still supplies only one factor \(H_N\); it does not force the remaining regular contraction to tend to one.

## 1. The moving Newton basis and its exact dual

Fix
\[
N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
M=q^s,\quad Y=M^2,\quad p=Q^{-1}.
\]
Write
\[
\sigma_r=\prod_{v=1}^r2\sin(\pi v/N),\qquad \sigma_0=1.
\]
Thus \(\sigma_d=N\) and \(\sigma_r\sigma_{d-r}=N\). For \(a\ne0\), set
\[
c_j(a)=ap^j+a^{-1}p^{-j},\qquad
B_r(a;z)=\prod_{j=0}^{r-1}(c_j(a)-z),\qquad
e_r(a;z)=\frac{B_r(a;z)}{\sigma_r^2}.
\tag{1}
\]
The same-color moving nodes use \(a_s=q^{-1}Y\); the complete nodes use \(a_0=q^{-1}\). For clarity put \(e_r^s=e_r(a_s)\).

Let \(\mathcal T_0=2,\mathcal T_1=z,\mathcal T_{r+1}=z\mathcal T_r-\mathcal T_{r-1}\). The two relevant algebras are
\[
\mathcal A_s=\mathbb C[z]/P_s(z),\qquad
P_s(z)=\mathcal T_N(z)+Y^N+Y^{-N},
\tag{2}
\]
for equal colors, and the constant algebra \(\mathcal A_0\) for opposite colors. Section 4 derives the physical duality that distinguishes these two algebras. The Casimir and pivotal moment identities used there are the exact identities of [the intrinsic cut calculation](intrinsic_cut_and_meridian_atlas.md).

The elementary identity
\[
c_{d-j}(a_s)=c_j(a_{-s})
\tag{3}
\]
gives an exact dual basis, even though the forward basis is no longer self-dual. Define
\[
\phi_s(f)=(-1)^dN^2[z^d](f\bmod P_s).
\]
Then
\[
\boxed{\quad \phi_s(e_i^s e_j^{-s})=\mathbf1_{i+j=d}.\quad}
\tag{4}
\]
For \(i+j<d\) this is degree. For \(i+j=d\), compare leading coefficients and use \(\sigma_i\sigma_j=N\). For \(i+j\ge N\), the first \(i\) nodes in forward order together with the first \(j\) nodes in reverse order contain all \(N\) indexed nodes. Their product is divisible by \(P_s\), with multiplicities retained. This proves (4) at collisions as well.

In particular, if \(f=\sum_{r=0}^d f_r e_r^s\), then
\[
f_r=\phi_s(f e_{d-r}^{-s}),\qquad
\phi_s(f)=f_d.
\tag{5}
\]
This is an exact finite coefficient extractor. It is not a positivity assertion for the deformed multiplication.

## 2. An elementary finite connection formula

For an indeterminate \(z\), define
\[
\Psi_n(a;z)=\prod_{j=0}^{n-1}(1-ap^jz+a^2p^{2j}).
\]
For generic \(p,a,b\), the following finite identity holds. It is the standard connection relation for the Askey–Wilson factorial basis, recorded in Ismail and Stanton, [*Expansions in the Askey–Wilson Polynomials*, equation (2.4), PDF page 7](https://www-users.cse.umn.edu/~stant001/PAPERS/AF-Ismail-Stanton.pdf#page=7). Indeed, with \(z=v+v^{-1}\), one has \(\Psi_n(a;z)=(av,a/v;p)_n\); clearing the finite factorial denominators in their formula gives (6). We give the elementary induction because it also justifies specialization at roots of unity. No physical turn or quotient-algebra assertion is imported from that connection relation.
\[
\Psi_n(a;z)=
\sum_{k=0}^n
{n\brack k}_p(a/b)^k
(abp^k;p)_{n-k}(a/b;p)_{n-k}\Psi_k(b;z),
\tag{6}
\]
where \((v;p)_r=\prod_{j=0}^{r-1}(1-vp^j)\) and
\({n\brack k}_p=(p;p)_n/((p;p)_k(p;p)_{n-k})\).

Here is a direct induction. Multiplying the \(k\)-th basis polynomial by the new factor gives
\[
(1-ap^nz+a^2p^{2n})\Psi_k(b;z)
=(a/b)p^{n-k}\Psi_{k+1}(b;z)
 +(1-(a/b)p^{n-k})(1-abp^{n+k})\Psi_k(b;z).
\tag{7}
\]
Thus the proposed coefficients in (6) must satisfy the recurrence given by (7). For \(1\le k\le n\), write \(m=n+1-k\), substitute the displayed factorial products, and cancel their common factors. The remaining identity is
\[
p^m(1-p^k)(1-abp^{k-1})
 +(1-p^m)(1-abp^{n+k})
 =(1-p^{n+1})(1-abp^n).
\tag{8}
\]
The constant terms agree because \(m+k=n+1\); the coefficients of \(ab\) agree after factoring out \(p^n\). The endpoint cases follow from their single surviving term. The case \(n=0\) starts the induction. Clearing the denominators proves the polynomial identity wherever the resulting finite expressions are defined. In particular it applies at the present root for \(n<N\).

Since
\[
B_n(a;z)=a^{-n}p^{-n(n-1)/2}\Psi_n(a;z),
\]
equation (6) gives the normalized connection
\[
e_n(a;z)=\sum_{k=0}^n C_{nk}(a,b)e_k(b;z),
\tag{9}
\]
with
\[
\boxed{\quad
C_{nk}(a,b)=
\frac{\sigma_k^2}{\sigma_n^2}
a^{k-n}p^{[k(k-1)-n(n-1)]/2}
{n\brack k}_p
(abp^k;p)_{n-k}(a/b;p)_{n-k}.
\quad}
\tag{10}
\]
Every diagonal entry is one. Interchanging \(a,b\) gives the inverse change of coordinates, because both are bases of the same space of polynomials of degree less than \(N\).

## 3. Uniform polynomial bounds, including all endpoint indices

**Proposition.** For every fixed \(R<\infty\), the connection from \(e_r^s\) to \(e_r^0\) and its inverse have coefficient \(\ell^2\)-operator norms at most
\[
C_R N^{A_R}\qquad (|s|\le R),
\tag{11}
\]
for constants independent of \(N\) and its parity. The assertion includes \(k=0\), \(n-k=1\), and all indices \(0\le k\le n<N\). It also holds for every fixed derivative in \(s\), with possibly different constants.

To prove it, first let \(m=n-k\ge1\). At \(|p|=1\),
\[
\left|{n\brack k}_p\right|
=\frac{\sigma_n}{\sigma_k\sigma_m}.
\]
For \(a=a_s\), \(b=a_0\), equation (10) therefore becomes
\[
|C_{nk}(a_s,a_0)|
=|a_s|^{-m}
\frac{|(Yp^{k+1};p)_m|}{\prod_{r=k+1}^n|1-p^r|}
\frac{|(Y;p)_m|}{\prod_{r=1}^m|1-p^r|}.
\tag{12}
\]
There is no missing factorial factor in this cancellation.

Let \(d_r=\min(r,N-r)\), \(1\le r<N\). Then
\[
|1-p^r|=2\sin(\pi r/N)\ge\frac{4d_r}{N}.
\tag{13}
\]
For \(|w|\le R+1\),
\[
|e^{2\pi iw/N}-1|
\le\frac{2\pi(R+1)e^{\pi(R+1)}}N.
\tag{14}
\]
Comparing \(1-Yp^r\) with \(1-p^r\), and \(1-Yp^{r-1}\) with \(1-p^r\), bounds each ratio in (12) by
\[
1+\frac{K_R}{d_r},
\qquad K_R=\frac{\pi(R+1)e^{\pi(R+1)}}2.
\tag{15}
\]
This uses \(w=s\) in the first product and \(w=s+1\) in the second. Consequently each product is at most
\[
\prod_{r=1}^{N-1}\left(1+\frac{K_R}{d_r}\right)
\le \exp\left(K_R\sum_{r=1}^{N-1}\frac1{d_r}\right)
\le C_RN^{2K_R}.
\tag{16}
\]
Also \(|a_s|^{-m}\le e^{2\pi R}\). Thus every entry has a uniform polynomial bound. When \(m=0\), the entry is exactly one and no denominator of index zero is used.

For the inverse, take \(a=a_0,b=a_s\). The product \(ab\) is unchanged, and \(a/b=Y^{-1}\). The two products are bounded in exactly the same manner, now with shifts \(s\) and \(1-s\); the prefactor has modulus one. This proves the same entry bound for the inverse. A matrix of size \(N\) with entries bounded by \(B\) has \(\ell^2\)-operator norm at most \(NB\), proving (11). Each entry is entire in \(s\); Cauchy's estimate on the larger disk \(|s|\le R+1\) gives the derivative assertion.

The estimate is deliberately not optimized. Its role is to prove that changing the normalized Newton coordinates on a bounded microscopic disk has no exponential cost. In particular the ordinary resonance at \(s=1\) is not a singularity of this polynomial basis change. The actual realization of the polynomial algebra by tensor operators can nevertheless lose rank there, and a physical coupon's canonical polynomial coefficients can have poles.

## 4. An exact finite compiler with all orientation types

Choose an orientation of the actual knot. A strand directed with the chosen vertical coordinate carries \(V_+=V_{-q^{-1}M}\); a reversed strand carries its dual \(V_-=V_{-q^{-1}M^{-1}}\). The possible ordered two-strand objects are
\[
++,\quad --,\quad +-,\quad -+.
\]
An oriented two-string tangle preserves the total sign of these objects. Thus there are six relevant intertwiner spaces: the four endomorphism spaces and the two maps between \(+-\) and \(-+\). An intertwiner is a linear map commuting with the quantum-group action on these two-strand objects. We will show that each of these six spaces has rank \(N\) over the fixed-level formal ring \(\mathbb C[[u]]\), where \(M=e^u\), near completeness.

Here are the duality conventions. Write \(\rho=q-q^{-1}\), and use the nilpotent module basis
\[
Kv_a=xQ^{-a}v_a,\qquad Fv_a=v_{a+1},\qquad
Ev_a=[a]\frac{xq^{1-a}-x^{-1}q^{a-1}}{\rho}v_{a-1},
\qquad [a]=\frac{q^a-q^{-a}}{\rho}.
\tag{16c}
\]
Outside-basis arrows are omitted. The coproduct and antipode are
\[
\begin{aligned}
\Delta E&=E\otimes K+1\otimes E,& S(E)&=-EK^{-1},\\
\Delta F&=F\otimes1+K^{-1}\otimes F,& S(F)&=-KF,\\
\Delta K&=K\otimes K,& S(K)&=K^{-1}.
\end{aligned}
\tag{16d}
\]
These are the conventions of [the intrinsic cut and meridian atlas](intrinsic_cut_and_meridian_atlas.md). If \(\varphi_a\) is dual to \(v_a\) and \(y=x^{-1}Q^{-1}\), the actual duality is
\[
J_x:V_y\longrightarrow V_x^*,\qquad
J_xw_a=c_a(x)\varphi_{d-a},\qquad
c_a(x)=(-x)^aQ^{a(a+1)/2}.
\tag{16e}
\]
For example, the dual action is \(F\varphi_a=-xQ^{-a}\varphi_{a-1}\), so equivariance under \(F\) is precisely \(c_{a+1}=-xQ^{a+1}c_a\). Equivariance under \(K\) uses \(Q^d=Q^{-1}\). Under \(E\), it follows from \(e_a(y)=e_{N-a}(x)\), where \(e_a(x)\) denotes the coefficient of \(E\) in (16c). Thus \(J_x\) is an invertible module map for every \(x\ne0\), including ordinary-color resonances. For \(x=-q^{-1}M\), its dual root is exactly \(-q^{-1}M^{-1}\).

For general roots \(x_1,x_2\), the physical Casimir is
\[
\Omega=\rho^2F_{\mathrm{tot}}E_{\mathrm{tot}}
       +qK_{\mathrm{tot}}+q^{-1}K_{\mathrm{tot}}^{-1}.
\]
The intrinsic cut calculation gives
\[
\begin{gathered}
\prod_{j=0}^{N-1}\left(z-qx_1x_2Q^{-j}
                         -q^{-1}(x_1x_2)^{-1}Q^j\right)
=\mathcal T_N(z)+(x_1x_2)^N+(x_1x_2)^{-N},\\
P_{x_1,x_2}(\Omega)=0,\qquad
\operatorname{ptr}_{g_2}\Omega^r=0\quad(0\le r<d),\qquad
\operatorname{ptr}_{g_2}\Omega^d=s_{x_1}I,\qquad g_2=K_2^{1-N}.
\end{gathered}
\tag{16f}
\]
For either root \(x_1=-q^{-1}M^{\pm1}\),
\[
s_{x_1}=(-1)^dN\frac{\sinh(Nu)}{\sinh u},\qquad
s_{x_1}(0)=(-1)^dN^2.
\tag{16g}
\]
The partial trace means that the second strand is closed with its pivotal operator \(g_2\), while the first remains open. Its scalar is a unit in the formal ring at \(u=0\). These exact matrix identities hold at colliding eigenvalues as well.

For any object \((\epsilon_1,\epsilon_2)\), its full formal centralizer is the rank-\(N\) Casimir order
\[
\mathbb C[[u]][z]\big/
\left(\mathcal T_N(z)+M^{N(\epsilon_1+\epsilon_2)}
+M^{-N(\epsilon_1+\epsilon_2)}\right).
\tag{16a}
\]
Here is a proof of the full formal centralizer. At \(u=0\), all four objects specialize to the complete tensor square. Its centralizer has dimension \(N\), by [the physical pair-commutant theorem](actual_pair_casimir_commutant_and_rotated_trace.md). The kernel dimension of the intertwining equations over the fraction field cannot exceed this special-fiber dimension. On the other hand, (16f) makes \(1,\Omega,\ldots,\Omega^d\) independent: multiply any putative relation of degree \(r<N\) by \(\Omega^{d-r}\) and take the partial trace. Its leading coefficient must vanish.

The same moment calculation proves that these powers span the integral formal order. Their pairing matrix has determinant
\[
\det\left(\operatorname{ptr}_{g_2}\Omega^{i+j}\right)_{0\le i,j<N}
=(-1)^{N(N-1)/2}s_{x_1}^{\,N}.
\tag{16h}
\]
Reversing its columns gives a triangular matrix with diagonal \(s_{x_1}\). An integral intertwiner is a fraction-field linear combination of the powers; pairing with every power and using this unit determinant forces its coefficients into \(\mathbb C[[u]]\). This proves (16a), including its lattice. It does not assert a uniformly bounded inverse on a color disk as \(N\) varies.

For \(++\) and \(--\), (16a) is the moving order (2), using respectively \(e_r^s\) and \(e_r^{-s}\). For \(+-\) and \(-+\), it is the constant opposite-color order. Choose one reference object in each sign class. In the zero-sign class choose reference \(+-\), and normalize its carrier as follows. Let \(r_0\) be the full original complete checked-crossing polynomial in \(\mathcal A_0\), including its common Cartan scalar and its first coefficients at repeated roots. It is a unit in this algebra, because all of its nodal values are nonzero. Let \(r_0^{-1}\) denote its fixed polynomial inverse modulo \(P_0\), and put
\[
G_{-+}(M)=
\check R_{+,-}(M)\,r_0^{-1}(\Omega_{+,-}(M)):
V_+\otimes V_-\longrightarrow V_-\otimes V_+,
\qquad G_{+-}=I.
\tag{16b}
\]
The universal identity \(P_0(\Omega_{+,-})=0\) makes the polynomial factor and its inverse regular at every nonzero color, including the ordinary resonances. The physical mixed braiding is invertible there too. In the complete physical identifications used by the original turn theorem, \(\check R_{+,-}(1)=r_0(\Omega_{+,-}(1))\). Consequently \(G_{-+}(1)=I\), with no omitted scalar.

Set \(C_{B,A}=G_BG_A^{-1}\). For the other classes the carrier is the identity. Every intertwiner from object \(A\) to object \(B\) then has a unique form
\[
C_{B,A}f(\Omega_A),\qquad \deg f<N.
\tag{17}
\]
All original Cartan and framing scalars remain in the physical maps or their polynomial coefficients.

These coherent carrier choices make serial composition literal polynomial multiplication:
\[
(C_{C,B}g(\Omega_B))(C_{B,A}f(\Omega_A))
=C_{C,A}(gf)(\Omega_A).
\tag{18}
\]
Indeed the Casimir is natural under intertwiners, and the carriers multiply to \(C_{C,A}\). This is a coordinate identity, not a tangle isotopy or a new crossing inserted in the diagram.

A quarter-turn is the actual evaluation/coevaluation currying, with its ordered duality maps. For example, in the original nilpotent basis,
\[
\mathcal T_x(A)^{\,jb}_{ak}
=\frac{c_a(x)}{c_b(x)}A^{\,d-a,j}_{k,d-b},
\qquad c_a(x)=(-x)^aQ^{a(a+1)/2}.
\tag{19}
\]
To derive (19), insert \(\sum_l v_l\otimes\varphi_l\), apply \(A\) to the middle two strands, and evaluate the first two. Before using \(J_x\), the resulting map sends
\[
\varphi_i\otimes v_k\longmapsto
\sum_{j,l}A^{ij}_{kl}\,v_j\otimes\varphi_l.
\]
Applying (16e) to the two dual factors gives (19). Its domain is \(V_y\otimes V_x\), and its target is \(V_x\otimes V_y\); it is not an endomorphism of the same-color tensor square. Every matrix entry is regular for \(x\ne0\). On a fixed microscopic disk \(|s|\le R\), the entry rearrangement and \(|c_a/c_b|=|M|^{a-b}\) even give
\[
e^{-\pi R}\|A\|_{\mathrm{HS}}
\le\|\mathcal T_x(A)\|_{\mathrm{HS}}
\le e^{\pi R}\|A\|_{\mathrm{HS}}.
\tag{19d}
\]
Here \(\|\cdot\|_{\mathrm{HS}}\) is the Euclidean norm of all matrix entries. This physical matrix estimate is not a Newton coefficient or spectral estimate. Left bends retain their actual inverse pivotal maps. After the turn, remove the chosen output carrier and recover the unique polynomial by the actual partial pivotal trace. Equivalently, if \(G\) is the resulting endomorphism and \(e_r^\sigma\) is its selected Newton basis, its coefficient is
\[
f_r=\frac{s_0}{s_x}
\left(\operatorname{ptr}_{g_{\mathrm{second}}}
\left(G\,e_{d-r}^{-\sigma}(\Omega)\right)\right)_{\mathrm{scalar}},
\qquad s_0=(-1)^dN^2.
\tag{20}
\]
For an opposite-color object, \(\sigma=0\). For a left closing convention, use the already proved left partial trace and its actual inverse pivot; it has the same scalar factor. Formula (20) is just the exact duality (4) and the intrinsic two-color moment identity. It keeps all repeated-node derivatives.

Equations (17)--(20), together with the actual leaf crossings and their inverse powers, give a finite recursive compiler for every fixed oriented Conway expression. At each node its original object type is recorded. Its multiplication tensors can be extracted using (4); its turn tensors are the physical currying tensors expressed by (20). This is an equality of the original tensor contractions over the formal ring, not a proposed substitute source. It remains an exact meromorphic coefficient presentation wherever these coordinates continue; the physical tensor contraction itself is regular at ordinary-color resonances.

The identification with the original complete turn also requires its physical basis calibration. Set \(\rho=q-q^{-1}\), \(F_a=(Q;Q)_a\), and at \(M=1\) use
\[
|a\rangle=\delta_a v_a,\qquad \delta_a=\frac{\rho^a}{F_a}.
\tag{19a}
\]
The rescaled generators \(E_{\mathrm{bal}}=\rho E_{\mathrm{std}}\), \(F_{\mathrm{bal}}=\rho F_{\mathrm{std}}\) then have the original balanced entries
\[
E_{\mathrm{bal}}|a\rangle=(Q^{-a}-1)|a-1\rangle,\qquad
F_{\mathrm{bal}}|a\rangle=(1-Q^{a+1})|a+1\rangle.
\tag{19b}
\]
The diagonal change of basis leaves \(K\) and the pivotal operator unchanged. Since \(x=-q^{-1}\), one has \(c_a(x)=q^{a^2}\). The finite product \(F_d=N\) gives
\[
F_aF_{d-a}=N(-1)^aQ^{a(a+1)/2},\qquad
\delta_a\delta_{d-a}c_a(x)=\frac{\rho^d}{N}x^a.
\tag{19c}
\]
For the product identity, divide \(F_d\) by \(F_{d-a}\) and replace each factor \(1-Q^{N-r}\) by \(-Q^{-r}(1-Q^r)\). Thus the balanced duality coefficients have ratio \(x^{a-b}\); their common scalar cancels in currying. Formula (19) in these coordinates is the transpose of the original turn in equation (2) of [the complete Newton turn theorem](actual_newton_turn_positive_gram.md): its \((jb;ak)\) entry is \(x^{a-b}A_{(d-a,j);(k,d-b)}\). The output of that original turn is a polynomial in the balanced Casimir, which is complex symmetric on every degree block. Taking its transpose therefore makes no change.

At \(M=1\), every carrier is the identity, every Newton basis is the complete one, and this calculation identifies the retained physical dualities with the original unscaled turn. Consequently the compiler specializes to the proved complete multiplication table, coordinate reversal \(e_r\mapsto e_{d-r}\), and original closing functional. This checks its actual complete source fiber, not only its abstract algebra. The identity \(G_{-+}(1)=I\) does not by itself bound this carrier uniformly on a microscopic color disk.

The only color-dependent denominator in the trace-dual recovery (20) is \(s_x\). The factors \(\sigma_r\) are nonzero constants at each fixed level; the pivot, Casimir matrices, physical duality maps and actual mixed braiding and inverse are holomorphic for nonzero \(M\) on the retained logarithmic cover. The common Cartan scalar is included; after factoring it out, the remaining entries are Laurent expressions in \(M\).

An iterative evaluation therefore has a coarse pole-order bound depending only on the fixed tree: one power of \(s_x^{-1}\) for each physical leaf whose coordinates are extracted and each internal turn. When the leaves are the original \(h=T(R^n)\), evaluate each such leaf from its physical matrix and extract once; this count is at most the number of all displayed turns, including those leaf turns. A bare \(R^n\) leaf need not have a regular polynomial representative, so a bound solely by internal turns would be false.

There is a stronger final cancellation statement. Apply (20) directly to the entire physical tangle, after removing its single chosen carrier. Every resulting coordinate has the form
\[
f_r(M)=\frac{s_0}{s_x(M)}\,b_r(M),
\tag{20a}
\]
with \(b_r\) holomorphic at every nonzero ordinary-color point. Those zeros of \(s_x\) are simple. Thus every final Newton coordinate has at most a simple ordinary-color pole, irrespective of the apparent higher pole orders in the recursive calculation. The same holds for every fixed subtree. This is an exact cancellation identity, with no quantitative bound on \(b_r\) relative to the selected closing scalar.

The polynomial basis estimate (11) applies to the changes between the Newton frames occurring here. A separate physical calculation now evaluates the turn tensor (20): in fixed complete polynomial coordinates it is coefficient reversal multiplied by the paired sine product \(W_n(s)/H_N(s)\) and a specified scalar \(1\) or \(q^{\pm s^2/2}\). The [quarter-turn theorem](actual_main_meridian_turn_comparison.md) bounds these factors and their inverses uniformly for \(|s|\le R<1\). On \(|s|\le1/16\), it also compares the full spectral-jet norm with the complete turn of the same polynomial, with factors at most \(CN^7\). This local comparison does not estimate crossing coordinates through a resonance. The later [source-growth theorem](actual_main_meridian_source_bounds.md) controls the signed contraction for strict trees whose bare product junctions are not adjacent, on each fixed disk \(0\le R<1\).

## 5. The primitive closing trace leaves one boundary factor

Orient and cut one of the actual cylindrical closing arcs of the knot. The whole remaining two-string tangle is an endomorphism of the ordered object determined by those two arcs; the cylindrical closing matching gives the same input and output object. If the presentation uses the other cap closure, retain the actual closing turn before taking this cut. The selected side of the pivot and the zero-framing correction are retained.

Let \(f_{K,M}\) be the polynomial of this entire physical operator, with its framing scalar included. The exact two-color pivotal moment formula gives
\[
F_N(M)=s_x[z^d]f_{K,M}
=\frac{s_x}{s_0}\,\phi_s(f_{K,M}).
\tag{21}
\]
Here \(F_N(M)\) is the zero-framed reduced cut invariant, normalized so that the reduced unknot has value one. Its complete value is \(K_N=F_N(1)\). The coefficient polynomial \(f_{K,M}\) and the scalar function \(F_N(M)\) are different objects: the former encodes the remaining two-strand operator, while the latter is obtained after closing one strand. The [intrinsic cut normalization](intrinsic_cut_and_meridian_atlas.md) fixes this distinction and the pivotal scalar.

The same \(s_x\) occurs for either strand orientation:
\[
s_x=(-1)^dN\,\frac{\sinh(Nu)}{\sinh u},
\qquad s_x(1)=s_0.
\tag{22}
\]
For an opposite-color root, use the constant \(P_0\) in \(\phi_s\). In its Newton coordinates, \(\phi_s(f_{K,M})\) is exactly the last coordinate, by (5).

On the microscopic scale \(M=e^{z/(2N)}\), this yields the exact formal/meromorphic identity
\[
\boxed{\quad
\frac{F_N(e^{z/(2N)})}{K_N}
=H_N(z)\,A_{K,N}(z),\qquad
H_N(z)=\frac{\sinh(z/2)}{N\sinh(z/(2N))},
\quad}
\tag{23}
\]
where \(K_N=F_N(1)\ne0\) and
\[
A_{K,N}(z)=\frac{\phi_s(f_{K,e^{z/(2N)}})}{K_N},
\qquad s=\frac{z}{2\pi i},\qquad A_{K,N}(0)=1.
\]
This is the primitive reduced cut, not the ordinary zero-dimensional pivotal trace. With the prescribed full modified dimension
\[
d_N(M)=i^{N+3}\frac{M-M^{-1}}{M^N-M^{-N}},
\]
one has \(d_N(M)s_x=Nq^{N(1-N)/2}\); multiplying (21) by \(d_N\) makes the full trace constant.

There is a corresponding Euler-characteristic bookkeeping rule for the computation tree. Lower every operation's output with the actual pairing \((s_x/s_0)\phi_s\). Each lowered vertex contributes the common scalar \(s_x/s_0\), and each internal contraction uses its inverse. A connected tree has one more such vertex, counting its terminal closing functional, than internal edges. Exactly one scalar survives, giving (23). This counts the tensor computation, not the Euler characteristic of a hyperbolic manifold. The leaf coefficients and turn tensors still carry their genuine color dependence.

The factorization is not holomorphic across every resonance. For example, at \(s=1\), [ordinary-color pointing](actual_ado_complete_meridian_zero_accumulation.md) gives \(F_N(q)=C_1=1\), while
\[
\frac{s_x}{s_0}=\frac{\sin(\pi s)}{N\sin(\pi s/N)}
\]
has a simple zero. Consequently the normalized coefficient contraction in (23) has a pole at \(z=2\pi i\). In the \(s\)-coordinate its residue is
\[
-\frac{N\sin(\pi/N)}{\pi K_N}.
\tag{24}
\]
It may be exponentially small, but it is not zero. Thus no uniform holomorphic compiler bound on a disk containing that resonance follows just by factoring out \(H_N\).

## 6. What support and normalization do not prove

For opposite colors, the fixed abstract multiplication retains the complete Newton support. For equal colors, a formerly forbidden product need not vanish. One exact way to see the change is to keep the complete basis as a vector-space basis and write
\[
P_s=P_0+\Delta_s,\qquad
\Delta_s=Y^N+Y^{-N}-2=2\cos(2\pi s)-2.
\]
If \(i+j\ge N\), then the complete-basis product has a polynomial factorization
\(e_i^0e_j^0=P_0h_{ij}\), with \(\deg h_{ij}\le N-2\). Therefore in the moving algebra
\[
e_i^0e_j^0\equiv-\Delta_s h_{ij}\pmod{P_s}.
\tag{25}
\]
For fixed microscopic \(s\), \(\Delta_s\) is of order one, not of order \(N^{-1}\). A polynomially controlled basis change does not suppress this new term. The exact turn comparison retains the distinction between equal-color and opposite-color objects; its fixed polynomial coordinates do not identify their multiplication algebras. The additional products in (25) therefore remain in the physical calculation.

At first order there is a useful distinction: \(\Delta'_0=0\), so the multiplication of fixed degree-\(<N\) polynomials has zero first derivative at completeness. The moving Newton coefficients can nevertheless have nonzero first derivatives. The [multiplication note](actual_main_meridian_newton_multiplication.md) computes the exact connection derivative and shows that these first derivatives are precisely its basis-change contribution; they do not by themselves give a coordinate-independent first-order obstruction.

Finally write the even reduced state as \(F_N(M)=f_N(Y)\), with \(Y=M^2\). Let \(P_N^{\mathrm{ord}}\) be the unique polynomial of degree at most \(N-2\) matching \(f_N\) at the \(N-1\) nontrivial \(N\)-th roots of unity. Define
\[
S_N(Y)=1+Y+\cdots+Y^{N-1},\qquad
R_N(Y)=\frac{f_N(Y)-P_N^{\mathrm{ord}}(Y)}{S_N(Y)},\qquad
\rho_N(z)=e^{(N-1)z/(2N)}
                  \frac{N R_N(e^{z/N})}{K_N}.
\]
The numerator vanishes at every zero of \(S_N\), so this quotient has no pole there. The exponential factor retains the centered normalization of the full state. The [canonical ordinary-color subtraction](regularized_kashaev_period.md) gives the exact decomposition
\[
\frac{F_N(e^{z/(2N)})}{K_N}
=H_N(z)\rho_N(z)+\pi_N(z),\qquad
\pi_N(z)=\frac{P_N^{\mathrm{ord}}(e^{z/N})}{K_N}.
\tag{26}
\]
Thus the coefficient contraction of (23) is precisely
\[
A_{K,N}=\rho_N+\frac{\pi_N}{H_N}.
\tag{27}
\]
This identifies the pole in (24) and the required subtraction in the same primitive trace normalization.

For knots with positive complete exponential rate, \(\pi_N\) is exponentially small on compact sets, but its quotient by \(H_N\) still has the actual finite poles. After subtracting it, a bounded signed contraction gives normality of \(\rho_N\) and subsequential limits
\[
g(z)=H(z)a(z),\qquad H(z)=2\sinh(z/2)/z,\qquad a(0)=1.
\]
Boundedness and the boundary normalization do not force \(a=1\). Even reciprocal central multipliers with value one and vanishing first derivative at \(U=1\) can change this limiting function while preserving all root orbit values and the marked ramified normal fibre. They are not new actual knot sources; they show why the weaker data cannot imply the missing estimate or identification.

The result is an exact whole-tangle compiler with a polynomially controlled Newton basis deformation and the retained boundary factor. Its application to [separated bare product junctions](actual_main_meridian_source_bounds.md) now gives an exact supremum-volume limit for the auxiliary-colored source on \(M=q^s\), \(|s|\le R<1\), at both parities. A bare junction has no distinguished original crossing-circle operator; the condition is that no two such junctions are adjacent. The comparison includes the channels opened in (25) after summing them inside the actual junction. The geometric constant is the volume with the auxiliary circles unfilled, and the lower witness is the complete value. The subsequent [component extension](actual_main_meridian_component_extension.md) controls adjacent bare junctions under a finite path condition. The [filled-meridian theorem](actual_main_meridian_filled_volume.md) then proves a normalized profile and a uniform knot-volume limit on these microscopic disks, with additional complex-contour and geometric arguments. Continuation of the ordinary-color-subtracted state through its resonances remains a further question. Polynomial spectral stability of an arbitrary turn does not itself preserve a localized jet profile.



## 7. Reproducing the finite identities

From the repository root, with SymPy, mpmath and Matplotlib installed, run

~~~sh
python3 experiments/audit_main_meridian_newton_algebra.py
~~~

The [script](../experiments/audit_main_meridian_newton_algebra.py) compares independently expanded rational polynomials for the multiplication and connection identities, and reduces mixed-duality products in exact cyclotomic fields. It also records high-precision evaluations of the opened-sector factorization. The [output record](../experiments/main_meridian_newton_algebra_results.json) separates exact identities from asymptotic diagnostics. The uniform estimates are proved above and in [the multiplication theorem](actual_main_meridian_newton_multiplication.md), rather than inferred from these finite checks.
