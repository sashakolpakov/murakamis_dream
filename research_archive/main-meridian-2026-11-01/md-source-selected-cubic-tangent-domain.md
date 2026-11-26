# The tangent domain selected by genuine complete branches

Private reduction of a geometric question, 1 November 2026. No global return inequality is claimed.

The unrestricted local tangent comparison fails, but an old cubic vertex inside a genuine complete tree is not an arbitrary point of its positive domain. The adjacent original branches impose the following exact derivative restrictions. This gives a smaller, explicit domain on which a local certificate could be investigated.

## 1. Hypotheses and the selected inequalities

Use the all-turn trivalent, effective-\(L\)-leaf source of Sections 1–3 of /private/tmp/md-conway-single-return-cluster-geometric-comparison.md, now at its original strict complete maximizing state. Write \(t(x,y,z)\) for its cubic action and \(f_2\) for the original profile of \(hh\).

At an internal edge incident to the vertex, cut off the opposite complete branch. Its root is an unturned \(A\)-product, for the same reason as in the clamping proof. If the covariant incident label is \(x\), the branch contributes \(f_A(1-x)\). Stationarity gives
\[
\partial_x t=f_A'(1-x)\ge f_2'(1-x)=-f_2'(x).
\tag{1}
\]
The inequality is the unturned-product theorem, valid on the entire output interval. The last equality uses the symmetry \(f_2(1-x)=f_2(x)\).

For an external effective \(L\) leaf, \(0<x<1/2\), the contribution is \(g(x)+c\), and
\[
\partial_x t=-g'(x)\ge-f_2'(x).
\tag{2}
\]
To check the last comparison, put \(B=\cot\pi x>0\) and
\[
X_2(B)=\frac{B+\sqrt{B^2+2}}2,\qquad
g'(x)=2\log B,\qquad
f_2'(x)=2\log(2X_2(B)^2).
\tag{3}
\]
Since \(X_2(B)>1/\sqrt2\) and \(2X_2^2=1+2BX_2>B\), (2) follows.

Thus every original complete maximizing cubic vertex satisfies
\[
\boxed{\quad
\partial_x t+f_2'(x)\ge0,\qquad
\partial_y t+f_2'(y)\ge0,\qquad
\partial_z t+f_2'(z)\ge0.
\quad}
\tag{4}
\]
This statement includes the additive constants of the branches, which disappear only after differentiation. It makes no assertion about an enlarged absolute return-containing branch profile.

For the explicit near-half symmetric counterexample \(x=y=z=1/2-\epsilon\),
\[
\partial_x t
 =\log\frac{\sin^2(2\pi\epsilon)}
                 {\cos(\pi\epsilon)\cos(3\pi\epsilon)}
 \longrightarrow-\infty,
\qquad f_2'(x)\longrightarrow0.
\tag{5}
\]
Consequently that family is excluded by (4). This does not prove tangent domination on the remaining domain.

## 2. A finite geometric inequality that would suffice

At a selected old state \(a=(x,y,z)\), let
\[
L_a(u)=t(a)+\nabla t(a)\cdot(u-a).
\tag{6}
\]
The return domain in covariant labels is the tetrahedron
\[
\mathcal P_{\mathrm{ret}}
 =\{u\in[0,1]^3:u_1+u_2+u_3\ge2\}.
\tag{7}
\]
Its pair inequalities follow from the upper bounds \(u_i\le1\). Its four vertices are
\[
(1,1,1),\qquad(0,1,1),\qquad(1,0,1),\qquad(1,1,0).
\tag{8}
\]
Because the return action is nonpositive, the four inequalities
\[
L_a(v)\ge0\qquad(v\text{ one of }(8))
\tag{9}
\]
would imply tangent domination of every return state at that old vertex. This is only a sufficient condition; it does not use the negative interior return action.

If (9) held for every old strict cubic state satisfying the explicit branch constraints (4), then summing the old tangent planes over an all-turn trivalent tree would cancel every internal derivative by the original stationarity equations. Concavity of the original leaf profiles supplies their tangent inequalities. This would compare every assignment of complete and return sectors with the original complete maximum, without independent branch-pressure budgets. Strictness would still require excluding equality on the return boundary.

No proof of (9) on the old cubic domain subject to (4) is supplied here. The point of this reduction is to retain the actual source-selected constraints rather than retry an already false unrestricted tangent claim. It also remains a trivalent all-turn question: higher-valence hubs resolved through complementary edges do not automatically satisfy this setup.
