# The preferred knot cusp along the angular filling path

1 November 2026.

A horospherical cross-section of the knot cusp is a Euclidean torus.
Normalize the meridian's translation to one. The translation of the
preferred longitude, which follows the knot once and has linking
number zero with it, is its preferred cusp shape.

The ordered page decomposition and its positive angular realization
construct a representation of the original augmented exterior. This
note identifies its preferred main-cusp translation. The argument does
not use a quantum asymptotic to identify a representation or a cusp.
The small-neighborhood argument below is used only to establish an
identity of holomorphic germs. The identity then continues along the
entire positive angular chart, even when the original auxiliary
meridian logarithms are no longer small.

The geometric inputs are the
[ordered decomposition](actual_all_circle_octahedral_decomposition.md),
the [positive angular charts](actual_all_circle_angular_octahedra.md),
and their [actual filling completion](actual_all_circle_geometric_completion.md).
The [analytic criterion](actual_all_circle_curvature_filling_limit.md)
constructs the path used in the
[quantitative volume theorem](actual_all_circle_quantitative_volume.md).
The original marked inputs are the face-map theorem
[the original marked face maps](actual_conway_general_mask_marked_filling.md)
and the full rational translation proof
[the preferred-longitude translation proof](actual_main_meridian_preferred_cusp.md).

## 1. Statement

Fix an original ordered all-circle tree with at least one edge. Retain
the original disk frames, half twists
\(\epsilon_v\in\{0,1,-1\}\), and one main knot component. Let
\(\mathcal E\) be its physical quarter-turn edges. Set
\[
 y_v=\tan(\tau_v/2),\qquad
 k_e=(1+y_v^2+y_w^2)^{-1/2},\qquad
 \tan(\pi x_e)=k_e,\qquad x_e(\mathbf0)=\frac14,
 \quad e=vw.
\tag{1}
\]
All roots and inverse functions use their branches at zero. The local
positive chart is \(|\tau_v|<10^{-2}\). The ordered page construction
gives an actual marked representation there, with main meridian
parabolic and primitive auxiliary longitude logarithm \(V_v=2i\tau_v\).

Let \(L_{\mathrm{path}}\) be exactly the framed main path in Sections
2--6 of the preferred-cusp note. Let \(\lambda_K\) be the preferred
longitude in the augmented exterior. Write \(w_\epsilon\) for the
oriented writhe of its retained-half-twist diagram and \(\ell_v\) for
the linking number of crossing circle \(v\) with the main knot.
In the coordinate where the main meridian translates by one,
their translations in the angular representation are
\[
 \begin{split}
 \operatorname{trn}(L_{\mathrm{path}})
    &=2i\sum_{e\in\mathcal E}\cot(\pi x_e)-\sum_v\epsilon_v,\\
 \operatorname{trn}(\lambda_K)
    &=2i\sum_{e\in\mathcal E}\cot(\pi x_e)
                        -\sum_v\epsilon_v-w_\epsilon .
 \end{split}
\tag{2}
\]
Here \(\operatorname{trn}\) denotes Euclidean translation, not matrix
trace. The signs are those of the original positive checked crossing
and the actual oriented writhe.

For fixed integers \(p_v\), put \(n_v=\epsilon_v-2p_v\), and follow
the positive charge path
\[
 U_v+p_vV_v=-2\pi i c,\qquad 0\le c\le1.
\tag{3}
\]
Assume the path stays in the chart and has
\(\operatorname{Im}\tau_v<0\) for \(c>0\), as supplied by the
curvature-supported certificate. The completion theorem gives a
smooth actual filled knot complement at \(c=1\). Its preferred cusp is
\[
 \boxed{\displaystyle
 \tau_K=-w_{\mathbf n}-\sum_vn_v
        +2i\sum_{e\in\mathcal E}\cot(\pi x_e(\boldsymbol\tau(1))).}
\tag{4}
\]
Here \(w_{\mathbf n}\) is the oriented writhe of the diagram with
the filled powers \(n_v\).
Equivalently, the last sum is
\(2i\sum_{vw\in\mathcal E}\sqrt{1+y_v^2+y_w^2}\), with the same
branches. There is no smallness condition on the total \(U_v\) in
this conclusion.

## 2. Why actual representations can be compared near zero

There are two different geometric cell descriptions, so a source
Hessian by itself does not identify their holonomies. We use the
marked positive-gluing rigidity proved in
[the marked multicusp gluing theorem](general_marked_multicusp_gluing_rigidity.md),
Sections 2--3 and 5. It is also used in Section 2 of
[the original geometric deformation](actual_complete_core_geometric_deformation.md).
Here are the precise parts needed.

The new complete triangulation consists of eight positive ideal
tetrahedra per tree edge. Its face labels and peripheral paths are
those of the original exterior, by the ordered page proof. The old
complete construction gives that same marked exterior. Their complete
holonomies are conjugate by an orientation-preserving marked isometry.
This is the geometric uniqueness of the complete finite-volume metric.
It can also be obtained from the existing maximal-volume conjugacy
argument in
[the geometric conjugacy theorem](actual_fejer_unique_geometric_maximizer.md),
Section 1: the page representation is an actual representation of the
original group and its positive complete tetrahedra have volume
\(2|\mathcal E|v_8=2\pi F_0\), the known complete volume. This use of
rigidity is after the actual topological identification; an equality
of cell volumes alone would not identify exteriors.

For completeness, the positive-gluing uniqueness argument applies
with an auxiliary longitude rather than a meridian prescribed at
each auxiliary cusp. If there are \(t\) ideal tetrahedra and \(q\)
cusps, select \(t-q\) independent edge equations and one primitive
peripheral row at each cusp. The integral edge/peripheral identities
identify the symplectic quotient of the edge row space with
\(H_1(\partial M;\mathbb R)\). Thus these rows form a full-rank real
Lagrangian matrix \((A\ B)\). Choose the main meridian row and all
auxiliary longitude rows. They are independent and isotropic because
they are one primitive nonzero class on each different torus.

In the positive local orders write
\[
 u_j=\log z_j,\qquad v_j=\log(1-z_j^{-1}),\qquad
 D_j=\frac{dv_j}{du_j}=\frac1{z_j-1},\qquad
 \operatorname{Im}D_j<0.
\tag{5}
\]
The Jacobian at fixed chosen peripheral logs is
\(A+B\operatorname{diag}(D_j)\). If it killed a nonzero vector
\(a\), then \((a,\operatorname{diag}(D_j)a)\) would lie in the
complexification of a real Lagrangian subspace. Its symplectic
pairing with its conjugate would vanish. The same pairing is, up to
the fixed nonzero imaginary factor,
\(\sum_j\operatorname{Im}D_j|a_j|^2<0\), a contradiction.
The implicit-function theorem therefore gives one decorated shape
germ for the main meridian log zero and the auxiliary logs
\(V_v=2i\tau_v\). The cited multicusp theorem proves the rank and
decorated-representation statements for exactly these mixed
peripheral coordinates. Its polarization is the all-cusp form of
the proof in
[the polarized gluing argument](geometric_rigidity_and_cyclic_source.md),
Section 1.

This is a statement about the entire nearby marked representation,
not just a formal equality of its peripheral eigenvalues. To apply
it to the old family, develop the vertices of the new ideal
triangulation using the old representation and its recorded cusp
flags. For a lifted ideal vertex \(gP_v\), use
\(\rho(g)\xi_v\), where \(\xi_v\) is the selected peripheral fixed
point. This is independent of the coset representative. Every
complete tetrahedron has four distinct vertices, so the resulting
cross ratios are holomorphic nearby and remain positive. They obey
all the same edge and peripheral equations, with the same log
branches by continuity. This puts the old representation into the
new shape chart and justifies applying its uniqueness. No individual
tetrahedron or subtree is separately conjugated.

The old auxiliary longitude coordinates are valid near zero: the
marked theorem gives a diagonal, nonzero derivative of \(V\) with
respect to the original auxiliary colors. Thus the old family can
indeed be parametrized by these same \(V_v=2i\tau_v\). The preceding
uniqueness identifies its representation, with all original paths,
with the new page representation on a neighborhood of zero.

## 3. Identification of the retained wire coordinates

Equality of representation germs must also use the same variables
in the cotangent expression. Here that identification follows from
the exact classical Legendre calculation, not a comparison of
volumes.

In the original physical-edge variables the local angular action is
\[
 b(x,\theta)
 =\int_0^x\log(2\cos2\pi u+2\cos\theta)\,du-2J(x),
 \qquad
 J(x)=\int_0^x\log(2\sin\pi u)\,du .
\tag{6}
\]
For a circle vertex, the analytic elimination of its original
hidden variables gives
\[
 \operatorname{stat}_{\theta_v}\left[
       \sum_{e\sim v}b(x_e,\theta_v)
       +\frac{i\epsilon_v\theta_v^2}{4\pi}
       +i\chi_v\theta_v\right].
\tag{7}
\]
This is the original selected circle action, with its original
physical-edge indices: the one-leaf identity is derived explicitly
in
[the regular crossing-circle action](actual_main_meridian_regular_circle_trace.md),
Section 7, its circle-junction extension is in Section 9, and the
joint-wire Legendre identity is (38)--(39) of
[the joint filling transform](actual_main_meridian_joint_filling_transform.md).
The nondegenerate hidden Hessian makes these analytic eliminations
unique near the original complete state. The identity retains the
physical-edge variables before eliminating them.

There are no bare junctions in the present tree. Set
\(\theta_v=-\tau_v\), so that the original relation
\(V_v=-2i\theta_v\) becomes the geometric convention \(V_v=2i\tau_v\).
Separate evenness leaves \(b\) unchanged. Every retained edge \(vw\)
therefore has the stationary equation
\[
 \partial_x\{b(x,\tau_v)+b(x,\tau_w)\}=0.
\tag{8}
\]
Writing \(c_e=\cos2\pi x_e\), this is
\[
 (c_e+\cos\tau_v)(c_e+\cos\tau_w)=(1-c_e)^2.
\tag{9}
\]
The branch through \(x_e=1/4\) gives
\[
 c_e=\frac{1-\cos\tau_v\cos\tau_w}
               {2+\cos\tau_v+\cos\tau_w},
\tag{10}
\]
which is exactly (1). The derivative of (8) at zero is nonzero.
Thus these are the retained old physical-turn labels as analytic
germs, not merely variables with the same complete values.

The color itself also matches the primitive geometric meridian.
Let \(\Psi(\boldsymbol\tau)\) be the sum of the stationary edge
actions. The \(\theta\)-stationarity in (7) gives
\[
 \chi_v=-i\Psi_{\tau_v}
                   +\frac{\epsilon_v\tau_v}{2\pi},\qquad
 -2\pi i\chi_v
       =-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v=U_v .
\tag{11}
\]
The last expression is the actual page-by-page primitive word from
the ordered decomposition. Near zero it has derivative
\(d_v-i\epsilon_v\) in \(\tau_v\), where \(d_v\) is the circle's
degree. This is nonzero. Equation (11) is not used as a substitute
for the representation comparison in Section 2.

## 4. Holomorphic continuation of the actual main translation

The old preferred-cusp proof establishes its rational identities
before imposing any auxiliary filling equation. Its product
potential, endpoint rebasing rule, actual quarter-turn maps, and
pure and odd leaf words give
\[
 \operatorname{trn}(L_{\mathrm{path}})
             =2i\sum_e\cot(\pi x_e)-\sum_v\epsilon_v .
\tag{12}
\]
on the old nearby marked family. By Sections 2--3, (12) holds for
the actual new page representation near zero.

Both sides are holomorphic on the connected angular chart. For the
right side this follows directly from (1). For the left side, keep
the actual based main meridian and longitudinal words. The meridian
is nonidentity parabolic throughout the chart: it is conjugate to
one of the nontrivial local pants meridians. Locally send its marked
fixed point to infinity and normalize its translation to one. The
commuting longitudinal holonomy is then a translation as well.
Its coefficient is holomorphic and independent of the remaining
translation in this normalization. These local functions agree
on overlaps, so they define one holomorphic translation ratio on
the entire chart.

Equivalently, choose the local trace-two unipotent lifts and write
\(M=I+N\), \(L=I+\lambda N\). Since \(N\ne0\), the coefficient
\(\lambda\) is a holomorphic function on any open set where a chosen
entry of \(N\) is nonzero. The formulas agree on overlaps. This
description uses no logarithm of the main longitude and therefore
has no \(2\pi i\) or integer translation ambiguity.

The identity theorem now extends (12) throughout that chart. A
continuation along the positive charge path would suffice; no
uniform neighborhood in the original summed meridian coordinates
is required. The original endpoint-sign convention remains part
of the word: when an arc is reversed, both its traversal and its
unit-meridian orientation reverse. The affine multipliers \(-1\)
at odd seams are not replaced by \(+1\).

The homological computation of the fixed word is independent of
the representation. It is exactly
\[
 [L_{\mathrm{path}}]
     =w_\epsilon[\mu_K]+\sum_v\ell_v[\mu_v],\qquad
 \lambda_K=L_{\mathrm{path}}\mu_K^{-w_\epsilon}.
\tag{13}
\]
Hence the second identity in (2) continues with the first.

## 5. The preferred longitude after the actual fillings

The original crossing circles are pairwise unlinked, and their
primitive disk longitudes satisfy
\([\lambda_v]=\ell_v[\mu_K]\). Filling the original slopes
\(\mu_v+p_v\lambda_v\) gives
\[
 \lambda_{\mathrm{fill}}
       =\lambda_K\mu_K^{\sum_vp_v\ell_v^2}.
\tag{14}
\]
This remains a fixed word on the main boundary throughout the cone
path. At \(c=1\) it is precisely the preferred zero-linking longitude
of the smooth filled knot exterior. At intermediate \(c\) its
translation is simply the translation of that same boundary curve;
no smooth filling at an intermediate nonintegral cone angle is
asserted.

The disk orientations give
\(\ell_v^2=2(1+o_v)\) with \(o_v=1\) for parallel strands and
\(o_v=-1\) for antiparallel strands, while
\(w_\epsilon=\sum_vo_v\epsilon_v\) and
\(w_{\mathbf n}=\sum_vo_vn_v\). Therefore
\[
 -\sum_v\epsilon_v-w_\epsilon+\sum_vp_v\ell_v^2
                =-\sum_vn_v-w_{\mathbf n}.
\tag{15}
\]
Adding the meridian translations in (14) to (2) proves (4).

The new conclusion is a geometric identity on the positive angular
continuation of this actual all-circle class. It does not extend
the original real angle chamber, and it does not assert a formula
on unrelated algebraic solutions. Its proof uses the exact marked
representation, actual path words, local geometric uniqueness,
and analytic continuation. The independent scalar calculation and
the new source asymptotic may subsequently use (4), but neither
was used to identify this cusp.
