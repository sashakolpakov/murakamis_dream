# A global source-error bound from the original Conway closing

Research proof, 23 November 2026.

The highest product's endpoint identity controls every lower quadratic
error, giving a global exponentially small remainder coefficient without
local polar decompositions. The computed polar radius of [P] remains
at least as strong; the improvement is over its earlier inexpensive
global radius.

## 1. The original tree and its coherent correction

Fix \(N\ge2\), put \(D=N-1\), and use
\(H_N=\mathbb C[X]/(2T_N(X/2)+2)\) with Newton basis \(e_0,\ldots,e_D\).

The coefficient Hermitian norm makes these basis vectors orthonormal.
All first normals at repeated roots are retained. The original turn,
Frobenius row and marked evaluation row satisfy

\[
 Je_j=e_{D-j},\quad \phi(f)=f_D,\quad \lambda_0(f)=f_0,
 \quad \phi(uv)=u^{\mathsf T}Jv,\quad
 \lambda_0(uv)=u_0v_0,\quad \lambda_0J=\phi,\quad\phi J=\lambda_0.
 \tag{1}
\]

Here \(f_j\) denotes a Newton coefficient, and transpose has no complex
conjugation. These are the full original algebra identities in [P,C].

Take a fixed literal Conway tree with distinct child occurrences.
Its proper gates are prescribed leaves, turns \(J\), and products
\(M(u,w)=uw\).

Use the original budgets of [C], with \(\sigma=1/16\):

\[
 b_v=16\max(1,\|T_v\|_{\rm HS}),\qquad
 \Phi_v=M/b_v\ \text{at a product},\qquad
 \Phi_v=J/b_v\ \text{at a turn}.
 \tag{2}
\]

Here \(T_v\) is the corresponding unnormalized physical tensor.
The original closing is \(L=\chi\lambda_\varepsilon/b_\rho\), with
\(\varepsilon\in\{0,D\}\) and \(\lambda_D=\phi\).

The scalar \(\chi\), its closing budget \(b_\rho\), every other budget,
and their product \(B_{\rm tot}\) are retained. In particular
\(\|L\|=|\chi|/b_\rho\le\sigma\).

Let \(a\) be the true normalized forward field and \(x\) any feasible
trial field, meaning \(\|x_v\|\le1\) at every proper vertex. Define

\[
 e=a-x,\quad r=\Phi(x)-x,\quad A=D\Phi(x),\quad
 c=(0,\ldots,L\text{ on the top packet},\ldots,0),
\]
\[
 d=c(I-A)^{-1},\qquad z=Lx_{\rm top},\qquad
 k=K_N/B_{\rm tot},\qquad \widehat k=z+dr.
 \tag{3}
\]

The inverse is a finite triangular sum. If \(Q_v(h)=\Phi_v(h_L,h_R)\)
at products and is zero elsewhere, [R] proves the exact identities

\[
 (I-A)e=r+Q(e),\qquad k-\widehat k=dQ(e).
 \tag{4}
\]

Because the tree has one parent per packet, its backward rows obey

\[
 d_{\rm top}=L,\qquad
 d_u=d_vD_u\Phi_v(x)\quad(u\text{ a child of }v).
 \tag{5}
\]

## 2. The highest product fixes the global coefficient

Suppose first that the tree contains a product, and let \(v_*\) be
the first product encountered going downward from the closing.
Every proper gate above it is a turn. Let
\(\mathcal U\) be that turn corridor and put

\[
 \eta=\frac{\chi}{b_\rho\prod_{u\in\mathcal U}b_u},\qquad
 \zeta=\frac{|\eta|}{b_{v_*}}.
 \tag{6}
\]

Empty products equal one. By (1) and (5),
\(d_{v_*}=\eta\lambda_\nu\), with \(\nu\in\{0,D\}\) determined
by the corridor parity. No turn has been moved through a product.
Thus the contracted bilinear matrix at \(v_*\) is exactly

\[
 B_{v_*}=\begin{cases}
 (\eta/b_{v_*})J,&\nu=D,\\
 (\eta/b_{v_*})e_0e_0^{\mathsf T},&\nu=0,
 \end{cases}
 \qquad \|B_{v_*}\|=\zeta.
 \tag{7}
\]

Here \(u^{\mathsf T}B_vw=d_v\Phi_v(u,w)\). For either child \(u\)
of \(v_*\), its sibling packet \(x_{\rm sib}\) gives, by (1),

\[
 \|d_u\|\le\zeta\|x_{\rm sib}\|\le\zeta.
 \tag{8}
\]

This uses the endpoint contraction. Each lower derivative block has
norm at most \(\sigma\). At a product this follows from
\(\|D_u\Phi_v(x)\|\le\|\Phi_v\|_{\rm bil}\|x_{\rm sib}\|
\le\sigma\); at a turn it follows from (2). Consequently a proper
descendant \(v\) at distance \(j\ge1\) below \(v_*\) satisfies

\[
 \|d_v\|\le\zeta\sigma^{j-1},\qquad
 \|B_v\|\le\sigma\|d_v\|\le\zeta\sigma^j
       \quad\text{if }v\text{ is a product}.
 \tag{9}
\]

All product matrices have norm at most \(\zeta\), with equality at
the highest one. Thus the block polar majorant \(\mathcal S_x\) of
[P,(10a)] satisfies, uniformly over feasible \(x\),

\[
                         \|\mathcal S_x\|=\zeta.
 \tag{10}
\]

## 3. The whole remainder and an inexpensive source disk

For any full variation field \(h\), distinct product sibling pairs
are disjoint. Equations (7)--(9) and \(2ab\le a^2+b^2\) give

\[
 |dQ(h)|\le\sum_{v\ {\rm product}}\|B_v\|\|h_L\|\|h_R\|
                         \le\frac\zeta2\|h\|^2.
 \tag{11}
\]

The true and trial fields lie in the original product of unit balls.
On their joining segment, the derivative of \(\Phi\) has norm at
most \(\sqrt2\sigma\le1/8\): a row has at most two child blocks
and every child occurs once. Integrating that derivative, or using
[R]'s residual estimate, proves \(\|e\|\le(8/7)\|r\|\).
Combining this with (4),(11) yields

\[
 |k-\widehat k|\le R_{\rm end}(x),\qquad
 R_{\rm end}(x)=\frac{32\zeta}{49}\|r\|^2,
\]
\[
 B_{\rm tot}(|\widehat k|-R_{\rm end})_+
 \le |K_N|\le B_{\rm tot}(|\widehat k|+R_{\rm end}).
 \tag{12}
\]

Here \((t)_+=\max(t,0)\). With no product, \(Q=0\), \(k=\widehat k\) exactly, and the radius is zero.

Write \(H_M=\max(1,\|M\|_{\rm HS})\). Since all corridor budgets
are at least one and \(b_{v_*}=16H_M\),

\[
 \zeta\le\frac1{256H_M},\qquad
 R_{\rm end}\le\frac{\|r\|^2}{392H_M}
                  \le\frac{\|r\|^2}{392}<\frac{\|r\|^2}{343}
                       \quad(r\ne0).
 \tag{13}
\]

Thus (12) improves the earlier inexpensive global coefficient uniformly.
It does not improve the computed polar radius \(R_{\rm pol}\) of [P].
Indeed its scalar majorants obey
\(\Delta_v=\|r_v\|+\sigma\sum_c\Delta_c\), hence
\(\|\Delta\|\le(8/7)\|r\|\) by the same one-parent norm bound.
Since [P]'s \(t_{vc}\le\sqrt{\|B_v\|}\Delta_c\),

\[
 R_{\rm pol}\le\frac\zeta2\|\Delta\|^2\le R_{\rm end}.
 \tag{14}
\]

One may use (12) without forming any polar matrix, or keep the stronger
computed polar disk. The coherent center and every budget are identical.

## 4. Exponential saving and scope

For \(j=\lfloor N/4\rfloor\), [P,(20)] proves from the actual
sine-factorial coefficient that

\[
 \|M\|_{\rm HS}\ge\|M\|_{\rm bil}\ge
 \frac{s_{2j}^{\,2}}{s_j^{\,4}}
 =\exp\{(2G_{\rm Cat}/\pi)N+O(\log N)\},
 \qquad s_j=\prod_{a=1}^j2\sin(\pi a/N).
 \tag{15}
\]

Here \(G_{\rm Cat}=\int_0^{\pi/4}\log(\cot t)dt\).
Consequently \(\zeta\le\exp\{-(2G_{\rm Cat}/\pi)N+O(\log N)\}\).
The saving is global for the stated literal compiler, at every parity
and composite level; (15) is its large-level quantitative consequence.
Restoring \(B_{\rm tot}\) retains all lower product budgets. No claim
that every multiplication cost disappears is made.

For a sequence of feasible trials, suppose
\(|\widehat k_N|=\exp(-\alpha N+o(N))\),
\(\|r_N\|\le\exp(-\beta N+o(N))\), and
\(\zeta_N\le\exp(-\gamma N+o(N))\).
Then (12) is negligible relative to its coherent center whenever
\(2\beta+\gamma>\alpha\). With the older constant coefficient, the
corresponding sufficient condition was \(2\beta>\alpha\). A bounded residual permits \(\beta=0\);
the hypotheses still require the stated actual center estimate.

The pure-turn corridor and the two original endpoint closings are
essential hypotheses. Fixed short proper subtrees may be inserted as
their full prescribed leaves. General precomposed unary maps and shared
descendants are outside this literal compiler; parameter derivatives
of the closing need their own transport. All physical Hermite normals
and original phases remain present. No actual center or positive
difference has been assigned a geometric rate, and no finite-exception
theorem follows.

## Complete proof sources

All three complete matching proof texts were read:

- [P] [Source-sensitive polar bound](research_conway_source_polar_error_bound.md), 321 lines, SHA-256 `3d1e77ad6f3cac830a5290145e4f05111bb39856f67866a126782f6dd27debc4`.
- [R] [Source-visible residual transport](research_conway_source_visible_residual_transport.md), 420 lines, SHA-256 `0d344301b0df65246551cf81498eff84582f796a03271b201f8fbba6c7742007`.
- [C] [Normalized original source](research_convex_normalized_conway_source.md), 329 lines, SHA-256 `6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c`.

Only written mathematics and text/hash operations were used. No earlier
final, manuscript or public document was edited.
