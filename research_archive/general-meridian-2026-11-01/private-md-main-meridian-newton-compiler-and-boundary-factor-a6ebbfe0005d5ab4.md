# A typed Newton compiler and its exact main-meridian boundary factor

Private proof, 1 November 2026. No repository file is changed.

There are two distinct operations in a main-meridian deformation: changing the polynomial coordinates of a coupon, and changing the multiplication and turn tensors of the physical source. The first operation has a uniform polynomial bound in the microscopic color. The second is not controlled by that bound: formerly zero multiplication channels can open. This note proves the basis statement, constructs an exact formal compiler for a fixed oriented Conway tree, and retains the actual primitive closing trace. Its scalar normalization supplies one factor \(H_N\), but does not force the remaining regular contraction to tend to one.

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
for equal colors, and the constant algebra \(\mathcal A_0\) for opposite colors. The exact typed duality and the distinction between these algebras are proved in [the preceding private note](/private/tmp/md-main-meridian-typed-turn-and-geometric-obstruction.md).

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
For generic \(p,a,b\), the following finite identity holds:
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
An oriented two-string tangle preserves the total sign of these objects. Thus there are six relevant intertwiner spaces: the four endomorphism spaces and the two maps between \(+-\) and \(-+\). All have rank \(N\) over the fixed-level formal ring \(\mathbb C[[u]]\), \(M=e^u\), near completeness.

For any object \((\epsilon_1,\epsilon_2)\), its full formal centralizer is the rank-\(N\) Casimir order
\[
\mathbb C[[u]][z]\big/
\left(\mathcal T_N(z)+M^{N(\epsilon_1+\epsilon_2)}
+M^{-N(\epsilon_1+\epsilon_2)}\right).
\tag{16a}
\]
The proof is the same unit-moment and complete-fiber dimension argument as in the preceding note: all special fibers are the complete tensor square, and the actual moment scalar is the unit \(s_x\). This proves the full order, not just a selected commuting subalgebra.

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
The preceding note proves the analogous maps are regular in physical coordinates and gives their first variation. After the turn, remove the chosen output carrier and recover the unique polynomial by the actual partial pivotal trace. Equivalently, if \(G\) is the resulting endomorphism and \(e_r^\sigma\) is its selected Newton basis, its coefficient is
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
For the product identity, divide \(F_d\) by \(F_{d-a}\) and replace each factor \(1-Q^{N-r}\) by \(-Q^{-r}(1-Q^r)\). Thus the balanced duality coefficients have ratio \(x^{a-b}\); their common scalar cancels in currying. Formula (19) in these coordinates is the transpose of the original turn in equation (2) of [the complete Newton turn theorem](/Users/sasha/volume-conjecture/notes/actual_newton_turn_positive_gram.md): its \((jb;ak)\) entry is \(x^{a-b}A_{(d-a,j);(k,d-b)}\). The output of that original turn is a polynomial in the balanced Casimir, which is complex symmetric on every degree block. Taking its transpose therefore makes no change.

At \(M=1\), every carrier is the identity, every Newton basis is the complete one, and this calculation identifies the retained physical dualities with the original unscaled turn. Consequently the compiler specializes to the proved complete multiplication table, coordinate reversal \(e_r\mapsto e_{d-r}\), and original closing functional. This checks its actual complete source fiber, not only its abstract algebra. The identity \(G_{-+}(1)=I\) does not by itself bound this carrier uniformly on a microscopic color disk.

The only color-dependent denominator in the trace-dual recovery (20) is \(s_x\). The factors \(\sigma_r\) are nonzero constants at each fixed level; the pivot, Casimir matrices, physical duality maps and actual mixed braiding and inverse are holomorphic for nonzero \(M\) on the retained logarithmic cover. The common Cartan scalar is included; after factoring it out, the remaining entries are Laurent expressions in \(M\).

An iterative evaluation therefore has a coarse pole-order bound depending only on the fixed tree: one power of \(s_x^{-1}\) for each physical leaf whose coordinates are extracted and each internal turn. When the leaves are the original \(h=T(R^n)\), evaluate each such leaf from its physical matrix and extract once; this count is at most the number of all displayed turns, including those leaf turns. A bare \(R^n\) leaf need not have a regular polynomial representative, so a bound solely by internal turns would be false.

There is a stronger final cancellation statement. Apply (20) directly to the entire physical tangle, after removing its single chosen carrier. Every resulting coordinate has the form
\[
f_r(M)=\frac{s_0}{s_x(M)}\,b_r(M),
\tag{20a}
\]
with \(b_r\) holomorphic at every nonzero ordinary-color point. Those zeros of \(s_x\) are simple. Thus every final Newton coordinate has at most a simple ordinary-color pole, irrespective of the apparent higher pole orders in the recursive calculation. The same holds for every fixed subtree. This is an exact cancellation identity, with no quantitative bound on \(b_r\) relative to the selected closing scalar.

The polynomial basis estimate (11) applies to the changes between the Newton frames occurring here. It does not estimate the complete typed turn tensor (20), the actual crossing coordinates through a resonance, or the signed sum of the resulting tree.

## 5. The primitive closing trace leaves one boundary factor

Orient and cut one of the actual cylindrical closing arcs of the knot. The whole remaining two-string tangle is an endomorphism of the ordered object determined by those two arcs; the cylindrical closing matching gives the same input and output object. If the presentation uses the other cap closure, retain the actual closing turn before taking this cut. The selected side of the pivot and the zero-framing correction are retained.

Let \(f_{K,M}\) be the polynomial of this entire physical operator, with its framing scalar included. The exact two-color pivotal moment formula gives
\[
F_N(M)=s_x[z^d]f_{K,M}
=\frac{s_x}{s_0}\,\phi_s(f_{K,M}).
\tag{21}
\]
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
This is the primitive reduced cut, not the ordinary zero-dimensional pivotal trace. Equivalently, the full modified factor satisfies \(d_N(M)s_x=Nq^{N(1-N)/2}\); multiplying (21) by \(d_N\) makes the full trace constant.

There is a corresponding Euler-characteristic bookkeeping rule for the computation tree. Lower every operation's output with the actual pairing \((s_x/s_0)\phi_s\). Each lowered vertex contributes the common scalar \(s_x/s_0\), and each internal contraction uses its inverse. A connected tree has one more such vertex, counting its terminal closing functional, than internal edges. Exactly one scalar survives, giving (23). This counts the tensor computation, not the Euler characteristic of a hyperbolic manifold. The leaf coefficients and turn tensors still carry their genuine color dependence.

The factorization is not holomorphic across every resonance. For example, at \(s=1\), exact root pointing gives \(F_N(q)=C_1=1\), while
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
For fixed microscopic \(s\), \(\Delta_s\) is of order one, not of order \(N^{-1}\). A polynomially controlled basis change does not suppress this new term. If one insists on a constant opposite-color algebra at every step, the same issue is transported into the exact typed turns and carrier coefficients, rather than removed.

Finally let \(P_N\) denote the actual ordinary-color interpolation polynomial and let \(\rho_N\) be the canonical regular profile. The already proved exact decomposition is
\[
\frac{F_N(e^{z/(2N)})}{K_N}
=H_N(z)\rho_N(z)+\pi_N(z),\qquad
\pi_N(z)=\frac{P_N(e^{z/N})}{K_N}.
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

The concrete advance is therefore an exact whole-tangle formal compiler with a polynomially controlled Newton basis deformation and a fully retained boundary factor. A general source theorem still needs control of the typed operation tensors and the resulting signed contraction, including the channels opened in (25), followed by a condition that identifies its normalized regular limit.

