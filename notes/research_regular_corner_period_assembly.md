# Primitive periods through regular square corners

Private written proof, 16 November 2026.

A finite regular corner can flatten four of an original edge's eight
tetrahedra without making the coupled primitive filling equations
singular. In particular, for a proper selected set in a connected
original graph, the Hermitian part of the complete selected period
Jacobian remains positive definite when every edge is positive or has
only one regular corner square. The conclusion holds for arbitrary
real signed powers. This note proves the exact kernel transport when
there is no fixed outside vertex, and extends the existing exact wire
contour construction to these corners.

All periods, face maps, wire kernels and logarithmic lifts are the
original ones. A continuation of the analytic equations through a
corner is not a positive-cell decomposition or a completed hyperbolic
metric beyond it. No noncancellation assertion for the quantum source
is made.

## 1. The original edge at a regular corner

For an ordered edge with angular coordinates \((t,u)\), put

\[
 a=\tan(t/2),\quad b=\tan(u/2),\quad q^2=1+a^2+b^2,
 \qquad
 J_e=\frac1{2q}
 \begin{pmatrix}1+a^2&-ab\\-ab&1+b^2\end{pmatrix}.
 \tag{1}
\]

Here \(J_e\) is the derivative of the two original meridian returns,
not the Hessian of a substituted positive invariant. Its determinant
is \(1/4\), and \(J_e=-\pi\psi_e''\), with the continued original
edge phase \(\psi_e\). For a symmetric complex matrix, \(\Re J_e\)
denotes its Hermitian part, equivalently its entrywise real part.

Use the original disk and strip coordinates

\[
 \zeta=\frac{a+ib}{q+1}=\tanh P,\qquad
 \xi=\frac{a-ib}{q+1}=\tanh Q,
 \quad
 q=\frac{1+\zeta\xi}{1-\zeta\xi},\quad
 a=\frac{\zeta+\xi}{1-\zeta\xi},\quad
 b=\frac{\zeta-\xi}{i(1-\zeta\xi)}.
 \tag{2}
\]

A positive edge has \(|\zeta|,|\xi|<1\). A regular single-square
corner has exactly one disk coordinate on the unit circle, away from
\(\{1,-1,i,-i\}\), and the other strictly inside. The pinned
corner classification proves that its face chart is regular:
\(\Re q>0\), and all \(a\pm i,b\pm i,q\pm a,q\pm b,q\pm i\)
are nonzero. Four original tetrahedra are flat with distinct vertices;
the other four are positive. This excludes two-square corners and
all ramified or infinite limits.

**Lemma 1.** At a \(P\)-corner \(\zeta=e^{i\theta}\),

\[
 \Re J_e=\kappa_P
 \binom{\cos\theta}{-\sin\theta}
 (\cos\theta,-\sin\theta),\qquad
 \kappa_P=\frac{1-|\xi|^4}{|1-\zeta^2\xi^2|^2}>0,
 \tag{3}
\]
\[
 k_P=\binom{\sin\theta}{\cos\theta},\qquad
 J_e k_P=\frac i2\binom{\cos\theta}{-\sin\theta}.
 \tag{4}
\]

At a \(Q\)-corner \(\xi=e^{i\varphi}\),

\[
 \Re J_e=\kappa_Q
 \binom{\cos\varphi}{\sin\varphi}
 (\cos\varphi,\sin\varphi),\qquad
 \kappa_Q=\frac{1-|\zeta|^4}{|1-\zeta^2\xi^2|^2}>0,
 \tag{5}
\]
\[
 k_Q=\binom{-\sin\varphi}{\cos\varphi},\qquad
 J_e k_Q=-\frac i2\binom{\cos\varphi}{\sin\varphi}.
 \tag{6}
\]

In particular every corner kernel has two nonzero coordinates.

**Proof.** Substitution in (1) gives

\[
 J_e=\frac1{2(1-\zeta^2\xi^2)}
 \begin{pmatrix}
 (1+\zeta^2)(1+\xi^2)&i(\zeta^2-\xi^2)\\
 i(\zeta^2-\xi^2)&(1-\zeta^2)(1-\xi^2)
 \end{pmatrix}.
 \tag{7}
\]

One can read its kernel and imaginary action without taking lengthy
real parts. The original strip dictionary, with
\(f(P)=\arctan\tanh P\), is

\[
 t=2(f(P)+f(Q)),\quad u=-2i(P-Q),\quad
 r_t=P+Q,\quad r_u=i(f(Q)-f(P)).
 \tag{8}
\]

Consequently the real energy of a complex variation is

\[
 \Re(\delta r_t\overline{\delta t}
             +\delta r_u\overline{\delta u})
 =4\Re f'(P)|\delta P|^2+4\Re f'(Q)|\delta Q|^2.
 \tag{9}
\]

At the \(P\)-corner, \(f'(P)=-i\tan\theta\), while
\(\Re f'(Q)>0\). The coordinate Jacobian in (8) has determinant
\(4i(f'(P)+f'(Q))\ne0\). Thus (9) is positive semidefinite
of rank one. Set \(\delta Q=0\) and
\(\delta P=i\cos\theta/2\); (8) gives (4).
At the \(Q\)-corner set \(\delta P=0\) and
\(\delta Q=-i\cos\varphi/2\), obtaining (6).
The real kernel therefore determines the rank-one directions in
(3) and (5). Their coefficients equal the trace, which is

\[
 \operatorname{tr}\Re J_e
 =\tfrac12\Re(q+q^{-1})
 =\Re\frac{1+\zeta^2\xi^2}{1-\zeta^2\xi^2}.
 \tag{10}
\]

At the two respective walls this is exactly \(\kappa_P\) or
\(\kappa_Q\). The excluded four disk points make every displayed
sine and cosine nonzero. \(\square\)

## 2. The assembled kernel and the anchored theorem

Let \(G\) be a finite graph with the original endpoint incidence,
and let \(S\) be its selected vertices. Outside angular coordinates
are fixed. Each selected vertex is incident to an edge. Keep all
edges incident to \(S\), each once, with both occurrences of a loop.
Assume every such edge is positive or a regular single-square corner.
Write \(\iota_e w\) for its ordered endpoint vector, putting zero
at an outside endpoint. The actual period and its derivative are

\[
 \mathcal P_v=\sum_{e\ni v}r_{v,e}-\frac{i n_vt_v}{2},\qquad
 J_S=D\mathcal P
 =\sum_e\iota_e^T J_e\iota_e-\frac i2\operatorname{diag}(n_v),
 \quad n_v\in\mathbb R.
 \tag{11}
\]

Form the graph of corner edges. Mark as pinned every outside vertex
and every selected vertex incident to a positive edge. Orient each
corner edge temporarily. Its nonzero real gain is

\[
 g_e=\cot\theta\quad(P\text{-corner}),\qquad
 g_e=-\cot\varphi\quad(Q\text{-corner}).
 \tag{12}
\]

Reversing traversal replaces the gain by its reciprocal.

**Theorem 2.** The real kernel of \(\Re J_S\) is exactly the
space of assignments satisfying zero at all pins and
\(w_{\mathrm{head}(e)}=g_e w_{\mathrm{tail}(e)}\) on every
corner edge. Each connected corner component meeting a pin has zero
kernel. An unpinned connected component has a one-dimensional kernel
precisely when every oriented cycle has gain product one, and has
zero kernel otherwise. Its nonzero kernel generator has no zero
coordinate. These statements include parallel edges; a loop imposes
\((1-g_e)w_v=0\).

In particular, if \(G\) is connected and
\(\varnothing\ne S\ne V(G)\), then

\[
                           \Re J_S>0.
 \tag{13}
\]

**Proof.** Every edge Hermitian form is nonnegative. A positive edge
has zero form only when its full endpoint variation is zero. By
Lemma 1 a corner has zero form exactly when its endpoint variation
obeys (12). The filling term contributes no Hermitian part. Thus
the kernel is exactly the stated simultaneous constraint space.
Propagation from one vertex determines all values on a connected
corner component. A pin forces them all to vanish. Otherwise the
path values are consistent precisely when all cycle products are
one, proving the dimension statement.

For (13), extend a kernel assignment by zero outside \(S\).
Along any original graph path, a positive edge makes both endpoint
values zero, and a corner propagates a zero in either direction.
Every selected vertex has a path to an outside vertex. Thus the
whole assignment is zero. Positive semidefiniteness now gives
positive definiteness. The same reasoning applies to complex
vectors by complexification. \(\square\)

When the fixed outside angles are zero, a boundary edge in fact
cannot be a single-square corner: (2) gives \(\zeta=\xi\) if
its second endpoint has \(b=0\). Under our alternatives that edge
must therefore be positive. The pin proof does not require this
extra observation and also allows other fixed regular angles.

On a compact family with these hypotheses, fixed graph and selected
set, continuity and (13) give a uniform constant
\(\Re J_S\ge\gamma I\), \(\gamma>0\). This assertion excludes
approach to two-square corners or any of the specified singular
limits. No constant uniform over arbitrary graphs is claimed.

## 3. The exact imaginary obstruction when there is no anchor

The gain criterion also determines when a null direction of the
Hermitian part can be a null direction of the complex Jacobian.
Let \(\mathcal K=\ker_{\mathbb R}\Re J_S\). Define a real skew
matrix \(K\) on selected vertices by adding, for each oriented
corner edge \(v\to w\),

\[
 K_{vw}=+1,\ K_{wv}=-1\quad(P\text{-corner}),\qquad
 K_{vw}=-1,\ K_{wv}=+1\quad(Q\text{-corner}).
 \tag{14}
\]

Contributions are summed; the two entries of a loop cancel.
The ordered edge chart fixes whether (14) is the P or Q case.

**Proposition 3.** For \(w\in\mathcal K\),

\[
 J_Sw=\frac i2(K-\operatorname{diag}n)w,
 \tag{15}
\]
\[
 \ker_{\mathbb C}J_S=
 \{w\in\mathcal K\otimes\mathbb C:
                 (K-\operatorname{diag}n)w=0\}.
 \tag{16}
\]

Consequently each unpinned gain-balanced component can be tested
using its single real generator \(h\). A necessary condition for
singularity on that component is

\[
                         \sum_v n_vh_v^2=0.
 \tag{17}
\]

If on each such component all powers have one weak sign and at
least one is nonzero, \(J_S\) is nonsingular.

**Proof.** Equations (4) and (6) give (15) edge by edge; positive
edges vanish on \(\mathcal K\). If \(J_Sz=0\), then
\(z^*(\Re J_S)z=0\), whence \(z\in\mathcal K\otimes\mathbb C\).
Equation (15) proves (16). The residual matrix is real, so a complex
kernel exists precisely when a real one exists. Distinct unpinned
corner components do not couple in (15). On one such component a
nonzero vector is a multiple of \(h\); multiply its residual
equation by \(h^T\) and use \(h^TKh=0\) to obtain (17).
All entries of \(h\) are nonzero, giving the sign conclusion.
\(\square\)

This last conclusion gives a nonsingular complex Jacobian. It does
not give strict horizontal descent when \(\mathcal K\ne0\).

## 4. Marked continuation and local descent

Retain the original logarithms from a supplied positive germ up to
the regular corner, and their local continuation there. The original
face denominators and (1) are regular, so this continuation exists
without resetting any logarithmic period. With cone charges \(c_v\),
the original reduced phase is

\[
 F=\sum_e\psi_e(t_v,t_w)
       +\frac i{4\pi}\sum_{v\in S}n_vt_v^2
       -i\sum_{v\in S}c_vt_v,
 \qquad F'=-\mathcal P/\pi-ic,
 \qquad -F''=J_S/\pi.
 \tag{18}
\]

At a supplied solution \(\mathcal P=-\pi ic\), Theorem 2 for
a proper selected set gives a unique local holomorphic solution of
the primitive equations as their parameters vary through the wall.
In a sufficiently small convex neighborhood the Hermitian part
remains positive definite, even on the side where some original
tetrahedra have become negatively oriented. If
\(\Re J_S\ge\gamma I\) there, then for real \(h\) in that
neighborhood,

\[
 \Re F(t_*+h)\le\Re F(t_*)-\frac\gamma{2\pi}|h|^2.
 \tag{19}
\]

This follows by integrating (18) twice on the horizontal segment.
The same positivity proves local injectivity of the period map by
integrating its Jacobian along complex straight segments.
The compact-family bound after Theorem 2 supplies uniform local
coercivity; the usual finite subcover argument supplies local
continuation neighborhoods on a compact family of marked solutions.

For actual integral fillings, the original carrier \(\eta_v\)
and coefficient \(p_v\) give \(n_v=\eta_v-2p_v\), and

\[
 U_v=2\sum_{e\ni v}r_{v,e}-i\eta_vt_v,\qquad
 V_v=2it_v,\qquad
 U_v+p_vV_v=-2\pi ic_v.
 \tag{20}
\]

Thus the continuation is of the marked primitive period, including
the carrier. It is not merely an exponentiated slope equation.
It does not assert that an arbitrary short hyperbolic filling reaches
this configuration, or that the continued representation is discrete
and faithful beyond it.

## 5. An exact wire contour through the regular corner

The product-contour theorem has a useful extension at these same
points. This statement uses the original same-index wire phase;
reversed wires require their own retained phase dictionary.

**Lemma 4.** If \((a,b)\) is a regular single-square corner, every
proper independent contraction \((\lambda a,\mu b)\),
\(0\le\lambda,\mu\le1\), is positive. The unchanged endpoint
retains \(\Re q>0\).

**Proof.** The canonical angles still obey
\(|\Re t|,|\Re u|<\pi\), by (8). Thus
\(a,b\in\mathcal A=\mathbb C\setminus(i[1,\infty)\cup-i[1,\infty))\).
Write \(a=A+i\alpha,b=B+i\beta\), and
\(X=A^2+B^2,\ C=A\beta-B\alpha\).
The boundary of the positive-edge criterion at this regular point
is \(C^2=X\). Here \(X>0\): otherwise both tangents are purely
imaginary and the boundary would have \(q=0\), contrary to
\(\Re q>0\). Moreover \(A,B\ne0\). For example, if
\(A=0\) and \(B\ne0\), equality implies \(\alpha^2=1\),
excluded by \(a\in\mathcal A\).

For \(\lambda\mu>0\),

\[
 \lambda^2A^2+\mu^2B^2-\lambda^2\mu^2C^2
 =\lambda^2(1-\mu^2)A^2+\mu^2(1-\lambda^2)B^2>0
 \tag{21}
\]

unless \(\lambda=\mu=1\). The strict positive-edge criterion
therefore holds at every such proper contraction. If one factor is
zero, the other tangent stays in \(\mathcal A\); the complete-end
edge is positive there. \(\square\)

For a target graph made of positive edges and regular single-square
corners, Lemma 4 and the existing positive contraction lemma show
that every pair on the finite arms
\([-a_v^*,a_v^*]\times[-a_w^*,a_w^*]\) has discriminant
\(1+a^2+b^2\) off \((-\infty,0]\). At unchanged corner pairs
this follows from \(\Re q>0\); sign changes preserve the square.
Pairs on \((\mathbb R\cup[-a_v^*,a_v^*])\times
(\mathbb R\cup[-a_w^*,a_w^*])\) have the same property:
if one tangent is real, the other belongs to \(\mathcal A\),
and a real nonpositive discriminant is impossible.

The explicit compact-and-tail neighborhood proof in the pinned
product-contour theorem now applies without change to this skeleton.
Namely, take the union of a sufficiently thin horizontal strip and
a sufficiently thin neighborhood of each finite arm. On real tails
the real part of the discriminant is positive; on the remaining
compact pairs its distance from the excluded ray is positive. These
give symmetric star-shaped tangent domains and simply connected
angular domains \(V_v\), chosen independently of \(N\), containing
the full intervals \((-\pi,\pi)\) and the corner target. On their
product,

\[
 \Re q_e>0,\qquad \cot(\pi x_e^*)=q_e,
 \quad 0<\Re x_e^*<\tfrac12,
 \qquad
 H_e=\frac{2\pi q_e(1+q_e^2)^2}
              {(1+a_v^2)(1+a_w^2)}\ne0.
 \tag{22}
\]

The branches are even in each angle and agree with the original
ones along the contraction to completeness.

**Corollary 5.** Suppose the traced target angles have negative
imaginary parts. The exact full-Hermite joint factorial-lens source
has a representative whose fixed-endpoint wire paths pass through
the stationary graph (22), including this regular corner. Every
original coupon, normal, free boundary polynomial and framing factor
is retained. No wire seam current is introduced.

**Proof.** Put \(b_N=-1/(2N)\), \(N\ge2\). The pinned exact
factorial theorem gives holomorphy of both direct and reflected
halfwires on compact subsets of
\(\Re x\in[b_N,b_N+1],\ |\Re t|<\pi\), without a bound
on their finite imaginary heights. Choose full lower angular arcs
in \(V_v\) through the targets and retain the exact lens trace.
For each angular tuple replace the horizontal wire interval by

\[
 b_N+ih_e\longrightarrow x_e^*(t_v,t_w)
                    \longrightarrow b_N+1+ih_e.
 \tag{23}
\]

The real parts stay inside the same convex interval. Straight
interpolation gives a compact holomorphic homotopy fixing both
endpoints. Cauchy's theorem on each fiber, followed by the retained
angular integrals, proves exact equality. Angular derivatives of
the wire paths wedge to zero against the angular volume form. This
is the proof of the pinned exact source theorem, with the extended
product domain now justified by Lemma 4. In particular it retains
the odd simple node and all double-node normals. \(\square\)

At a marked primitive critical point covered by Theorem 2, these
paths can include coherent local wire coordinates with
\(F_e=\psi_e-\xi_e^2/2\), since \(H_e\ne0\). Real
\(\xi_e\) and horizontal selected angular coordinates give,
by (18)--(19), a strictly descending local contour for the continued
original selected phase. The square-root construction of those
coordinates is exactly the one in the pinned unsummed-source proof.
It remains valid at the corner because every factor in (22) is a
unit. Small connectors join this local segment to (23) without
moving its endpoints.

This last stationary interpretation requires the same-index phase
at each endpoint; the exact identity with a true free boundary
polynomial does not identify its asymptotic phase with a factorial
phase. Nor does holomorphy of the exact reciprocal factorials imply
their nonvanishing. All factorial zeros, connectors, other angular
sectors and coherent trace terms remain present. No estimate here
shows they are smaller or prevents cancellation of the local term.

## Direct sources and scope of the extension

The earlier positive-domain theorems establish strict positivity
before a corner. The new assertions are the rank-one boundary
identities, their exact graph kernel and skew-action tests, the
automatic anchored coercivity, and the extension of the existing
exact contour construction to regular single-square corners.

- [Original positive edge periods](research_positive_edge_global_monotonicity.md):
  disk/strip dictionary, positive criterion, original returns and
  marked graph periods. Full proof read at SHA256
  `da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500`.
- [Original corner classification](research_square_corner_flat_geometry.md):
  Sections 1--3, regularity and the distinction from two-square
  corners. Full proof read at SHA256
  `511c2c93d61482664cf62ed3b146c0af19ffbb149fa8772a4d1eb5ca7026eed0`.
- [Original phase Hessian](research_cone_chamber_accretivity.md):
  (1)--(5), (12)--(15), (19)--(20), phase normalization, Hermitian
  interpretation and primitive carrier. Full proof read at SHA256
  `7dd2888717147bd7e48c2d8a08c8ea9819c12329a9b2e83e02c40c27cf8da803`.
- [Unsummed original phase](research_unsummed_network_phase_coercivity.md):
  (1)--(4), Section 5, same-index scope, stationary wire, Hessian and
  parameter Morse construction. Full text read at SHA256
  `b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e`.
- [Exact product source contour](research_positive_wire_product_contour.md):
  Sections 1--5, skeleton construction, reciprocal-factorial
  holomorphy, exact full-Hermite source and fixed wire endpoints.
  Full proof read at SHA256
  `5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230`.

All work is written mathematics; no mathematical program, numerical
evaluation or test is used. The result is local analytic continuation
and exact contour reachability at a specified regular corner. It does
not prove existence of the corner solution, arbitrary-short-filling
coverage, a positive retriangulation, or survival of its coefficient
in the original finite source.
