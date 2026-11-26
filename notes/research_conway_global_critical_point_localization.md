# Global critical-point localization for the original Conway quartic

Written proof, 23 November 2026. The normalized Conway quartic has one real critical
point on the entire packet space. A single sweep of real scalar
path minimizations brings any field into the radius-\(1/16\) packet
balls without increasing the energy. The known contracting iteration
then applies. A gradient test and continuous-flow convergence are
also proved. These finite-level statements concern the literal
uncompressed tree, not the minimum's hyperbolic-volume rate.

## 1. Complete physical packets and the original closing

Use [P]'s full \(N\)-dimensional physical pair algebra \(H_N\)
with its uniform physical Hilbert metric, for every \(N\ge2\).
All independent first normals at repeated Casimir roots remain.
The proof also applies in [C]'s normalized Newton metric, keeping
that metric's own maps and budgets together.

Fix a finite rooted literal Conway tree with distinct child
occurrences. Every proper vertex is a prescribed constant leaf,
a homogeneous complex-linear turn, or a complex-bilinear product.
Every proper packet has one parent. There are no shared variables
or compressed affine gates. The closing root is the original
complex-linear row \(L\), with all its recorded scalar factors.
Equal prescribed leaf data still have distinct trial variables.

Write \(V\) for the proper vertices, \(v_0\) for the top one, and
\[
 \mathcal X=\bigoplus_{v\in V}H_N,\qquad
 \mathcal D=\prod_{v\in V}\{\|x_v\|\le1\},\qquad
 \sigma=1/16.
 \tag{1}
\]
Keep exactly one of the normalizations above. Its prescribed leaf
vectors \(a_\ell\), unary maps, bilinear maps, and closing row all
have their respective vector, operator, or bilinear norms at most
\(\sigma\). Define on the whole space \(\mathcal X\)
\[
 G_v(x)=\Phi_v((x_c)_c)-x_v,\qquad
 E(x)=\sum_{v\in V}\|G_v(x)\|^2+|Lx_{v_0}|^2.
 \tag{2}
\]
At a leaf, \(\Phi_\ell=a_\ell\). Gradients are real gradients for
\(\operatorname{Re}\sum_v x_v^*y_v\). The actual source theorem
gives, with its unchanged budget product \(B\),
\[
 I\le D_{\mathbb R}^2E\le3I\quad\hbox{on }\mathcal D,
 \qquad
 B^2\min_{\mathcal D}E\le |K_N|^2
 \le\frac{197}{196}B^2\min_{\mathcal D}E.
 \tag{3}
\]
No change of metric, cap, framing, or peripheral normalization is
made in applying these estimates.

## 2. The exact leaf-path identity

For a literal leaf \(\ell\), let \(P_\ell\subset V\) be its
ancestor path, including the leaf and the top packet. Put
\[
 X^{(\ell)}_v=\begin{cases}x_v,&v\in P_\ell,\\0,&v\notin P_\ell.
 \end{cases}
\]
Scale these path packets by a real number \(t\), leaving all other
packets fixed. Exactly one child of each internal path vertex is
scaled. Homogeneity therefore scales its entire residual by \(t\).
The original closing also scales by \(t\). Only the leaf residual
has the form \(a_\ell-tx_\ell\). Differentiating at \(t=1\) proves
the identity, valid for every field without a feasibility assumption,
\[
 \boxed{\quad
 \left\|x_\ell-\frac{a_\ell}{2}\right\|^2
 +\sum_{v\in P_\ell\setminus\{\ell\}}\|G_v(x)\|^2
 +|Lx_{v_0}|^2
 =\frac{\|a_\ell\|^2}{4}
 +\frac12\langle\nabla E(x),X^{(\ell)}\rangle_{\mathbb R}.
 \quad}                                                     \tag{4}
\]
Every internal proper vertex is on at least one such path.
Distinct leaf occurrences, rather than identified repeated inputs,
are essential to this scaling argument.

## 3. A global gradient membership test

Set
\[
 g=\|\nabla E(x)\|,\qquad h=\|x\|,\qquad
 q_x=\sqrt{\frac{\sigma^2}{4}+\frac{gh}{2}},\qquad
 R(q)=\max\left\{\frac\sigma2+q,\frac{q}{1-\sigma}\right\}.
 \tag{5}
\]
Cauchy--Schwarz in (4), with \(\|X^{(\ell)}\|\le h\), gives
\[
 \|x_\ell-a_\ell/2\|\le q_x\quad\hbox{at every leaf},
 \qquad \|G_v(x)\|\le q_x\quad\hbox{at every internal vertex}.
 \tag{6}
\]
If \(q_x\le1-\sigma\), then \(R(q_x)\le1\) and
\[
                         \|x_v\|\le R(q_x)\quad(v\in V).
 \tag{7}
\]
Indeed leaves satisfy this by (6). If all children obey this
bound, a unary gate has output norm at most \(\sigma R\), and
a binary gate at most \(\sigma R^2\le\sigma R\). Thus
\(\|x_v\|\le\sigma R+q_x\le R\), proving (7) inductively.

In particular the following tests are valid on the entire space:
\[
 \boxed{\quad
 gh\le\frac{899}{512}\ \Longrightarrow\ x\in\mathcal D,
 \qquad
 gh\le\frac7{16}\ \Longrightarrow\
 \max_v\|x_v\|\le\frac1{32}
             +\sqrt{\frac1{1024}+\frac{gh}{2}}\le\frac12.
 \quad}                                                     \tag{8}
\]
For the first constant use
\(2[(1-\sigma)^2-\sigma^2/4]=899/512\).
For the second, \(q_x\le15/32=(1-\sigma)/2\), so the first
term in the maximum defining \(R\) is the larger one.
These tests bound \(gh\), not the gradient norm alone.

## 4. One real critical point on the whole space

The causal residual map is a polynomial automorphism. Given any
residual field \(r\), solve successively from leaves to root by
\[
                       x_v=\Phi_v((x_c)_c)-r_v.
 \tag{9}
\]
This is its polynomial inverse. Consequently \(E\) is coercive:
an energy sublevel is a closed subset of the compact image under
\(G^{-1}\) of a closed residual ball. A global minimum therefore
exists and is a real critical point.

At any real critical point, \(g=0\). Equations (5)--(7) give
\[
 \boxed{\qquad
 \|x_v\|\le\sigma\quad(v\in V),\qquad
 \|G_v(x)\|\le\sigma/2\quad(v\hbox{ internal}).
 \qquad}                                                    \tag{10}
\]
For example every internal packet has the sharper bound
\(\sigma^2+\sigma/2=9/256<\sigma\).
All real critical points thus lie inside \(\mathcal D\), where
(3) makes the gradient strictly monotone. There can be only one.
It is the unique global minimum \(x_*\), and
\[
 \min_{\mathcal X}E=\min_{\mathcal D}E=E(x_*).
 \tag{11}
\]
Thus the real stationary equations of degree at most three specify the minimum
without any competing real critical points. This is not a statement
about critical points of a complexification of the real polynomial.

## 5. One scalar sweep enters the convex region

At any current field, process a leaf \(\ell\) by scaling its path
packets by one real scalar. With current quantities put
\[
 u=\|x_\ell\|,\quad
 A=u^2+\sum_{v\in P_\ell\setminus\{\ell\}}\|G_v(x)\|^2
                +|Lx_{v_0}|^2,\quad
 b=\operatorname{Re}\langle a_\ell,x_\ell\rangle.
 \tag{12}
\]
The same homogeneity gives \(E(t)=C_\ell-2bt+At^2\). Minimize
this quadratic on the segment \([0,1]\): choose
\[
 t=\min\{1,\max\{0,b/A\}\}\quad(A>0),\qquad t=1\quad(A=0).
 \tag{13}
\]
Energy cannot increase, since \(t=1\) is allowed. The updated leaf
has norm at most \(\sigma\), and every updated internal path
residual has norm at most \(\sigma/2\). If \(A>0\) and \(b\le0\), this follows
from \(t=0\). If \(0<b<A\), use \(b\le\sigma u\) to obtain
\(tu\le\sigma u^2/A\le\sigma\) and
\(t\|G_v\|\le\sigma u\|G_v\|/A\le\sigma/2\).
Here \(2u\|G_v\|\le u^2+\|G_v\|^2\le A\).
If \(b\ge A>0\), then \(t=1\),
\(u^2\le A\le\sigma u\), and
\(\|G_v\|^2\le A-u^2\le\sigma u-u^2\le\sigma^2/4\).
If \(A=0\), the leaf and all these residuals are already zero.
Homogeneity then forces all path packets to be zero successively.
The update is continuous even there, since \(0\le t\le1\).

Process every literal leaf once, in any order. An off-path residual
is unchanged. Distinct leaf paths never include another leaf, so a
processed leaf stays bounded by \(\sigma\). Every subsequent touch
of an internal residual preserves its bound; packet norms and internal
residual norms never increase. Every internal vertex is touched.
At the end, upward induction as in (10) bounds all packets by \(\sigma\).
Thus this finite sweep maps \(\mathcal X\) into \(\sigma\mathcal D\)
with nonincreasing energy, using no unknown closed source.
Starting there, the known step \(x^{j+1}=x^j-\nabla E(x^j)/2\)
stays in \(\mathcal D\) and contracts by \(1/2\). If \(s=|V|\),
\[
 \|x^j-x_*\|\le2\sigma\sqrt{s}\,2^{-j},\qquad
 0\le E(x^j)-E(x_*)\le6\sigma^2s\,4^{-j}.
 \tag{14}
\]
This is global initialization followed by the established local-domain
iteration, not a claim about the raw fixed step outside that domain.
The errors in (14) are absolute; source-relative precision does
not follow when the minimum is exponentially small.

## 6. Continuous gradient flow from arbitrary initial data

For any finite initial field solve \(\dot x=-\nabla E(x)\).
The polynomial vector field is locally Lipschitz and
\[
 \frac d{dt}E(x(t))=-\|\nabla E(x(t))\|^2.
 \tag{15}
\]
The compact initial energy sublevel contains the trajectory, so local
existence extends to all \(t\ge0\) and \(\int_0^\infty g(t)^2dt<\infty\).
The gradient and Hessian are bounded there. Thus \(g(t)^2\) has bounded
derivative and is uniformly continuous. It tends to zero: otherwise
disjoint intervals would contribute a fixed positive amount to its
integral. Every cluster point is therefore critical. Compactness and
uniqueness imply \(x(t)\to x_*\). Since \(h\) stays bounded, (8)
eventually applies. No uniform flow entry time, global
Polyak--Lojasiewicz inequality, or global flow rate is asserted.

## 7. Scope, coverage, and complete inputs

Fixed signed twists and fixed short fillings remain their full leaf
packets in the unchanged literal tree, with the original cap and
all physical normals. A component with unknown incoming packets
is not replaced by a known constant leaf.

[J] already proves coercivity and the unique global minimum.
The path identity and initialization add global critical-point control.
The original comparison (3) is unchanged; its minimum can still
be zero or exponentially small. Uniqueness here concerns the real
quartic, not complex source-phase saddles or geometric thimbles.
No source growth rate or finite-exception volume theorem is proved.

All three complete texts were read and their matching pins renewed:

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| P | [Uniform physical compiler](research_conway_uniform_physical_quartic.md) | 477 | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| C | [Normalized Newton source, coverage](research_convex_normalized_conway_source.md) | 329 | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| J | [Residual Jacobian and global minimum, coverage](research_conway_residual_jacobian_gaussian_determinant.md) | 265 | db22b86a97302926fed77385f82ff2284109e288ec3d03dd99538d3671c926b2 |

Only written mathematics and text/hash operations were used. No
mathematical program, test, build, git operation, manuscript edit,
public-document edit, or earlier-final edit was performed.
