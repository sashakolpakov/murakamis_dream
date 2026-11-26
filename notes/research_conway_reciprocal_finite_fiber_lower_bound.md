# Finite-fiber orthogonality and exact integration of linear Conway packets

Written proof, 24 November 2026.

The unchanged positive reciprocal integral gives an all-level lower
bound for the original scalar with loss at most the number of leaves.
The proof uses the finite degree of the actual residual closing and
orthogonal projection on the fibers of an explicit rational map.
It is a shorter, weaker comparison than the relative asymptotic of [W].
All linearly entering packets can also be integrated out exactly,
leaving one variable packet per binary product.
It does not estimate the integral from hyperbolic geometry.

## 1. The original source and statement

Use the full physical Conway compiler of [P] at any level \(N\ge2\).
Fix a literal tree with \(s\ge1\) proper vertices and \(L\ge1\)
prescribed leaf occurrences. Each packet has all \(N\) complex
coordinates of \(\mathcal A_N\), including the first normals at
double Casimir roots. Put \(D=Ns\), and use physical orthonormal
coordinates \(x\in\mathbb C^D\), with real Lebesgue measure \(dx\).
Keep the normalized maps, the original closing row \(c\), and the
positive budget product \(\mathcal B_N\) unchanged. Set
\[
 G_v(x)=\Phi_v((x_j)_{j\text{ child of }v})-x_v,\qquad
 E_N(x)=\|G(x)\|^2+|cx|^2,\qquad
 \mathcal P_N={D!\over\pi^D}
       \int_{\mathbb C^D}E_N(x)^{-D-1}\,dx .                 \tag{1}
\]
This is exactly the undamped integral of [U,W]. Its base has degree
at most four; its denominator exponent grows with \(D\).
The entire original mark, phases, turns, framing and external factors
remain in (1). The integral is extended and nonnegative.

**Theorem.** With \(1/(+\infty)=0\), at every level and for every
prescribed complex leaf choice,
\[
 \boxed{\qquad {\mathcal B_N^2\over L\mathcal P_N}
                                      \le |K_N|^2 .\qquad} \tag{2}
\]
The integral is finite and positive when \(K_N\ne0\), and infinite
when \(K_N=0\). No prior nonvanishing assumption, physical coefficient
smallness estimate, or large-level asymptotic is needed for (2).

Order children before parents. The exact inverse of the residual map
is the polynomial recursion
\[
 H(r)_v=\Phi_v((H(r)_j)_j)-r_v,\qquad
 \det_{\mathbb C}DG=(-1)^D,\qquad
                         |\det_{\mathbb R}DH|=1 .          \tag{3}
\]
Indeed each step solves uniquely for its output packet. A leaf has
degree one in \(r\); a turn preserves degree; at a product, the two
child degree bounds add. Each subtree has at least one leaf, so the
additional term \(-r_v\) respects that bound. Consequently
\[
 f(r)=cH(r),\qquad \deg f\le L,\qquad
                   k=f(0)=K_N/\mathcal B_N .               \tag{4}
\]
The original coefficients define \(H,f\) by finite recursion.
The scalar \(k\) is used in the proof, not supplied to define (1).
Changing variables by (3) makes its denominator
\(\|r\|^2+|f(r)|^2\), with exactly the same measure.

## 2. A finite-fiber change of variables

We prove the needed polynomial integral statement explicitly. Let
\(f\in\mathbb C[r_1,\ldots,r_D]\), \(D\ge1\), satisfy
\(k=f(0)\ne0\), and put \(\nu=\max(1,\deg f)\). Define
\[
 J(r)=f(r)-\sum_{a=1}^D r_a\partial_a f(r),\qquad
 T(r)={r\over f(r)},\qquad
 d\mu_D(w)={D!\over\pi^D}
                   {dw\over(1+\|w\|^2)^{D+1}} .           \tag{5}
\]
The map \(T\) is used on \(\{f\ne0\}\). Radial integration gives
\[
 \int_{\mathbb C^D}d\mu_D
       =D\int_0^\infty {t^{D-1}\over(1+t)^{D+1}}\,dt=1,   \tag{6}
\]
by the substitution \(u=t/(1+t)\).
The rank-one determinant identity gives
\[
 DT={1\over f}\left(I-{r(\nabla f)^{\mathsf T}\over f}\right),
 \qquad \det_{\mathbb C}DT={J\over f^{D+1}} .              \tag{7}
\]
Here \(\nabla f\) denotes the column of holomorphic derivatives;
the transpose in (7) does not conjugate.

For a generic \(w\), all points of its fiber have the form
\[
 r_j=t_jw,\qquad p_w(t_j)=0,\qquad
                         p_w(t)=f(tw)-t .                 \tag{8}
\]
Its constant coefficient is \(k\), so no \(t_j\) is zero.
Except on an algebraic set of measure zero, \(p_w\) has degree
\(\nu\) and \(\nu\) distinct roots. Here is a direct check of
the distinct-root assertion. For degree at least two, choose a
direction \(v\) with nonzero highest homogeneous coefficient and
put \(g(u)=f(uv)\). Along \(w=av\), a repeated root requires
\(g(u)-ug'(u)=0\). This is a nonzero polynomial, since its
constant coefficient is \(k\). Its finitely many roots exclude
only finitely many nonzero \(a\) in \(g(u)=u/a\); a root with
\(g(u)=0\) cannot solve that equation. Thus the discriminant is
not identically zero. For constant or affine \(f\), the assertion
is immediate after excluding a possible zero linear coefficient.

At a root in (8),
\[
 J(t_jw)=-t_jp_w'(t_j)\ne0 .                              \tag{9}
\]
For any nonnegative measurable \(F\), ordinary real change of
variables on inverse charts therefore yields
\[
 {D!\over\pi^D}\int_{\mathbb C^D}
 {F(r)|J(r)|^2\over(\|r\|^2+|f(r)|^2)^{D+1}}\,dr
       =\int_{\mathbb C^D}\sum_{T(r_j)=w}F(r_j)\,d\mu_D(w).
                                                               \tag{10}
\]
The exceptional sets do not conceal a boundary term. The polynomial
zero sets \(f=0\) and \(J=0\) have measure zero, since both are
nonzero at zero. The degree-drop and discriminant sets in the target
also have measure zero. On the remaining regular set, partition a
countable cover by inverse charts into disjoint measurable pieces,
apply the usual change of variables on each, and sum by Tonelli.
Preimages of exceptional target sets on these charts are null.
This proves (10) without a properness assumption at infinity.
Setting \(F=1\) gives the finite-degree area identity
\[
 {D!\over\pi^D}\int
 { |J(r)|^2\,dr\over(\|r\|^2+|f(r)|^2)^{D+1}}=\nu .      \tag{11}
\]
Setting \(F=|J|^{-2}\) away from its null zero set instead gives
\[
 \mathcal P(f):={D!\over\pi^D}\int
 {dr\over(\|r\|^2+|f(r)|^2)^{D+1}}
       =\int\sum_{j=1}^{\nu}{1\over|J(r_j)|^2}\,d\mu_D . \tag{12}
\]

## 3. The original constant is an exact fiber trace

The partial-fraction identity for \(1/p_w(t)\) follows by clearing
denominators: the remaining polynomial has degree at most \(\nu-1\)
and vanishes at all \(\nu\) roots. Evaluating it at zero gives
\[
 {1\over k}=-\sum_{j=1}^{\nu}{1\over t_jp_w'(t_j)}
                         =\sum_{j=1}^{\nu}{1\over J(r_j)} .\tag{13}
\]
This can also be read as the elementary one-variable residue identity.
It retains the complex phases of every sheet. No root ordering or
continuous choice of individual roots is needed.

In the standard counting inner product on a regular fiber, the vector
\((1/J(r_j))_j\) has constant projection \((1/(\nu k))_j\).
Its remaining component has zero sum and is orthogonal to that vector.
Equations (6), (12), and (13) give the exact nonnegative decomposition
\[
 \mathcal P(f)={1\over\nu|k|^2}
   +\int\sum_{j=1}^{\nu}
       \left|{1\over J(r_j)}-{1\over\nu k}\right|^2d\mu_D .\tag{14}
\]
In particular \(|k|^2\mathcal P(f)\ge1/\nu\).
This orthogonality is on the fibers of the explicit source map (5),
not an assertion that the original physical cap is a positive trace.

For completeness, \(\mathcal P(f)\) is finite when \(k\ne0\).
Its denominator has no zero. It is bounded away from zero on each
compact set, and at infinity it dominates \(\|r\|^2\); the normalized
tail outside radius \(R\) is at most \(D/R^2\).
If \(f(0)=0\), holomorphy gives \(|f(r)|\le C\|r\|\) near zero.
The integral then dominates a positive multiple of
\(\int_0^\rho t^{-3}dt\), and is infinite.

## 4. Consequence for the unchanged Conway quartic

Apply (14) to (4). For nonzero source, \(\nu\le L\), so
\(\mathcal P_N\ge1/(L|k|^2)\). Multiplying and rearranging proves
(2). At a source zero the radial divergence just proved makes its
right-hand comparison zero as prescribed. All levels, arbitrary
complex leaf phases, and every full Hermite direction are retained.

The same lower comparison holds for any prescribed positive Hermitian
metric on each complete packet space, with any known nonzero scalar
normalizations retaining \(K_N=\mathcal B_N f(0)\).
Choose new orthonormal coordinates and rebuild both
the residual energy and its product Lebesgue measure in them. Each
residual still has coefficient \(-I\) in its own output variable;
thus (3), the degree bound, and the proof are unchanged. Restore the
known normalization by \(|\mathcal B_N|^2\) if it is complex.
No comparison with the old metric is required. This permits a metric
specified from geometric data, independently of the unknown source.
It does not keep the same numerical integral under a metric change,
or give a two-sided approximation for arbitrary new metrics.

For fixed \(L\), the logarithmic lower comparison is
\[
 {2\pi\over N}\log|K_N|
 \ge -{\pi\over N}\log(\mathcal P_N/\mathcal B_N^2)
                              -{\pi\over N}\log L .       \tag{15}
\]
Use extended logarithms at zeros. The last term tends to zero.
Thus a lower-bound argument can use this finite-fiber proof in place
of the longer asymptotic calibration in [W]. The latter remains
stronger: it gives a two-sided relative error tending to zero.
Neither comparison supplies a geometric upper estimate for
\(\mathcal P_N/\mathcal B_N^2\). Such an estimate is still required
to obtain a hyperbolic-volume lower bound. No new knot class or
finite-exception theorem is established here.

## 5. Integrating all packets that enter linearly

There is also an exact reduction of the same integral to its nonlinear
packets. Follow [L]: at each of the \(p=L-1\) binary products retain
one child packet. These selected packets are distinct because every
proper packet has a unique parent. Write their coordinates as
\(u\in\mathbb C^n\), \(n=Np\), and all remaining coordinates as
\(z\in\mathbb C^m\), \(m=D-n\). At fixed \(u\), no product has
two variable children. Split the original residuals into the eliminated
packets' own equations and all other equations, including the scalar
closing:
\[
 r_z=T(u)z+b_z(u),\qquad r_o=C(u)z+b_o(u),\qquad
 E_N(u,z)=\|r_z\|^2+\|r_o\|^2 .                           \tag{16}
\]
Here \(r_z\in\mathbb C^m\), \(r_o\in\mathbb C^{n+1}\), and
\(T=-I+\text{strictly triangular}\) in the tree order. These
identities hold on the whole complex spaces. Thus \(T\) is invertible
for every \(u\), with \(|\det T|=1\); its inverse is a finite
polynomial. No packet-ball restriction or small norm of \(u\) is used.

Set
\[
 \mathsf D=CT^{-1},\qquad F=b_o-CT^{-1}b_z,\qquad
 R=I_{n+1}+\mathsf D\mathsf D^*,\qquad q=F^*R^{-1}F .       \tag{17}
\]
The matrix and scalar depend on \(u\), and \(R\) is positive definite.
Changing to \(v=Tz+b_z\) preserves Lebesgue measure and gives
\(E_N=\|v\|^2+\|\mathsf Dv+F\|^2\).
Complete its Hermitian square with
\(A=I_m+\mathsf D^*\mathsf D\). The remaining constant is \(q\),
and \(\det A=\det R\). Diagonalization and radial integration give
\[
 \int_{\mathbb C^m}
 (\|v\|^2+\|\mathsf Dv+F\|^2)^{-n-m-1}\,dv
       ={\pi^m n!\over(n+m)!\,\det R\,q^{n+1}} .          \tag{18}
\]
For \(q>0\), the radial beta integral proves the displayed constant;
for \(q=0\), both sides are infinite. Tonelli now proves the exact
whole-source formula
\[
 \boxed{\qquad
 \mathcal P_N={n!\over\pi^n}
       \int_{\mathbb C^n}{du\over\det R(u)\,q(u)^{n+1}} .
 \qquad}                                                  \tag{19}
\]
It is an extended nonnegative equality, including source zeros.
If \(p=0\), then \(n=0\), \(R\) is scalar and
\(\det R\,q=|k|^2\), recovering the exact affine reciprocal.
For branching trees, (19) retains both the boundary Gram and its
determinant. It integrates the eliminated packets rather than
minimizing them, so its normalization differs from a Schur minimum.
The scalar closing is still a row of (16), with all original phases.
Equation (2) applies to precisely this reduced integral as well.
The lower comparison and this elimination remain valid in the
consistently rebuilt packet metrics described in Section 4.

## Complete inputs and standard coverage

All four complete matching texts were read. The residual recursion,
degree bound and finite-fiber integral proof are written above.

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| P | [Original physical compiler](research_conway_uniform_physical_quartic.md) | 477 | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| U | [Unchanged undamped reciprocal source](research_conway_undamped_reciprocal_source.md) | 311 | 4ce9ae44a5ed6f7f54145d96712a7937f2e8c4181e2292aa5f2c44e84ffb3a8a |
| W | [Stronger Wick calibration](research_conway_wick_undamped_reciprocal_asymptotic.md) | 331 | 6ffed298445828f2476989d29505c568a78a0793c03062eb37333cbd14dc5c83 |
| L | [Linear packet elimination](research_conway_orthogonal_linear_elimination.md) | 344 | aa53b79685296193d5bf7fc66e53f3a3fbe03fc72a36481fb3aee23afe2ae113 |

Change of variables, partial fractions and orthogonal projection are
standard. For residue context see [NIST DLMF, Section 1.10(iv)](https://dlmf.nist.gov/1.10#iv).
[Cattani, Dickenstein and Sturmfels, *Computing Multidimensional Residues*](https://arxiv.org/abs/alg-geom/9404011)
provides primary coverage for the broader global-residue and trace setting;
only its title and abstract were consulted, and no proof is imported.
Only written mathematics, text reads and metadata operations were used.
Earlier final notes and public manuscripts remain unchanged.
