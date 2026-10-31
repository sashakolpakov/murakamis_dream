# Complete and marked Conway geometry with single-leaf attachments

31 October 2026. Internally reviewed geometric extension and source-interface
audit. Keep the original crossing-circle leaf \(h\), literal turn \(T\),
identity stacks, source marking and fixed disk framings. Define **completed**
expressions by
\[
E::=hh\mid T(E)\mid E_1E_2\mid hE\mid Eh.
\tag{1}
\]
Every occurrence has its own leaves. The closed class here is \(C(FG)\),
where both root children are completed expressions in (1). Turns act on
completed expressions; independently turned bare leaves are not additional
atoms of this grammar.

This class has strict complete states, a unique complete optimizer and the
actual complete augmented-link metric. Every physical complete leaf satisfies
\(1/2<\cot(\pi a)<1\). The original local complex packet, primitive marked
deformation and actual filled-volume action remain valid. The
[source composition theorem](actual_conway_single_leaf_source_composition.md)
and [single-leaf alias comparison](actual_conway_single_leaf_alias_composition.md)
supply the separate global source estimates. Geometry alone is not used to
infer an alias gap. The root-leaf closures discussed in §6 remain outside
the high-index packet conclusion.

## 1. Strict feasibility and the only deleted flat gate

Each completed expression has a strict pure wire state at every prescribed
output \(b\in(0,1)\). For \(hh\), choose equal leaves
\[
\frac b2<a<\min\left(b,\frac12\right).
\]
At \(E_1E_2\), choose both child outputs in this same interval. At \(hE\) or
\(Eh\), use this \(a\) for the bare leaf and for the completed child output,
then use the child's strict state. At \(T(E)\), prescribe child output
\(1-b\). This is an induction using the original product inequalities
\[
\max(x,y)<z<x+y<1.
\]

At \(C(FG)\), delete only the final forced gate. Its exact finite coefficient
is one and its inputs sum to \(d=N-1\). Choose limiting root-child outputs
\(1/2,1/2\); both completed children have the strict states just constructed.
Every retained leaf and product is therefore strict.

The [original complete boundary barrier](actual_positive_conway_hyperbolic_volume.md),
§2, applies. An endpoint wire descends to a leaf endpoint or a product atom
\((0,a,1-a)\); every other retained product boundary also exposes such an
atom. Moving toward the strict state has positive infinite derivative there
and no negative infinite derivative elsewhere. There are no additional
forced-flat or maximizing-flat retained cells in this grammar.

The original angle maps recover all independent leaf and product wires.
Consequently the complete reduced Hessian is negative definite and the
strict maximizer is unique. Proper output profiles are analytic on
\((0,1)\). This is a sufficient combinatorial criterion for nondegeneracy,
with the grammar in (1) retained.

The excluded \(C(hh)=C(A_2)\) has two leaves whose forced sum is one, so both
equal \(1/2\) and no strict retained state exists. Initial turns of an entire
closed expression retain the existing
[original \(C/D\) cap-sum reduction](actual_conway_cap_sum_reduction.md);
they are not silently included in the completed-root statement.

## 2. The strict completed-port invariant survives \(hE\) and \(Eh\)

At a stationary proper output \(b\), set
\[
B=\cot(\pi b),\qquad \kappa=e^{-f_E'(b)},\qquad
X=\sqrt{\frac{1+B^2}{1+\kappa}},\qquad Y=\sqrt{\kappa}\,X.
\]
Then \(X,Y>0\) and \(X^2+Y^2-B^2=1\). An actual bare leaf has
\[
B=X=\cot(\pi a)>0,\qquad Y=1.
\tag{2}
\]
The [original stationary product formulas](actual_conway_strict_leaf_quarter_bound.md)
use a common \(X\):
\[
B_{\mathrm{out}}=\frac{B_1B_2+X^2-1}{B_1+B_2},
\qquad
Y_{\mathrm{out}}=\frac{Y_1Y_2}{B_1+B_2},
\qquad B_1+B_2>0.
\tag{3}
\]
Every completed expression in (1) obeys
\[
-Y<B<X.
\tag{4}
\]
The \(hh\) base is \(B=X-1/(2X)\), \(Y=1/(2X)\). A turn sends
\((B,X,Y)\) to \((-B,Y,X)\), preserving (4), and the
completed/completed product is the original exact preservation proof.

For the new \(hE\) product, write \(B\) for the completed child's first
coordinate. Formula (3) becomes
\[
B_{\mathrm{parent}}=X-\frac1{X+B},\qquad
Y_{\mathrm{parent}}=\frac{Y}{X+B},\qquad X+B>0.
\tag{5}
\]
If \(X\ge1\), (4) and the hyperboloid identity give \(B>0\) and
\(B>\sqrt{X^2-1}\). Thus \(B_{\mathrm{parent}}>0\) and
\(B_{\mathrm{parent}}<X\); its lower inequality is automatic.

If \(0<X<1\), put \(\alpha=\arccos X\) and \(h_0=\sin\alpha\).
The bare leaf has angle \(\alpha\) in the exact cotangent chart:
\[
(B_h,Y_h)=(h_0\cot\alpha,h_0\csc\alpha)=(X,1).
\]
The completed child has
\[
(B,Y)=(h_0\cot\beta,h_0\csc\beta),\qquad \beta>\alpha.
\]
The positive denominator in (5) selects \(\alpha+\beta<\pi\).
The parent angle is \(\alpha+\beta\), so its upper inequality is strict,
and
\[
B_{\mathrm{parent}}+Y_{\mathrm{parent}}
 =h_0\cot\frac{\alpha+\beta}{2}>0.
\]
This proves (4). The \(Eh\) order gives the same inequalities by the
exact symmetry of (3), without changing its physical frame.

## 3. Closed propagation and the stronger leaf bound

At the completed root, the two completed ports are \((B,X,Y)\) and
\((-B,X,Y)\). Applying (4) to both gives \(|B|<\min(X,Y)\).
The hyperboloid identity then implies
\[
0<X<1,\qquad 0<Y<1
\tag{6}
\]
for both root children.

These bounds propagate to every completed descendant in (1).
Turns exchange \(X\) and \(Y\). At a retained product the common \(X\)
already lies below one. Write each child in the angle chart of §2.
A completed child has angle strictly greater than \(\alpha\); a bare
leaf has angle exactly \(\alpha\). The positive denominator selects
a total angle below \(\pi\). Parent \(Y<1\) gives
\[
\alpha<\theta_1+\theta_2<\pi-\alpha.
\]
Every child angle is at least \(\alpha\), so a completed child's angle
lies strictly between \(\alpha\) and \(\pi-\alpha\). Hence its \(Y<1\),
and its \(X\) is the common \(X<1\). A bare leaf keeps \(Y=1\);
that equality is not propagated as a strict completed-port bound.

Every physical leaf occurs either in an \(hh\) base or at a single
\(hE/Eh\) attachment. At the base, \(Y_{\mathrm{parent}}=1/(2X)<1\)
gives \(X>1/2\). For a single attachment, (5), the completed child
hyperboloid and \(Y_{\mathrm{parent}}<1\) imply
\[
1+B^2-X^2<(X+B)^2,\qquad
1<2X(X+B)<4X^2,
\tag{7}
\]
where the last strict inequality is \(B<X\). Again \(X>1/2\).
The inherited \(X<1\) holds in both cases. Thus every actual complete
leaf satisfies
\[
\frac12<X_\ell=\cot(\pi a_\ell)<1,\qquad
\frac14<a_\ell<\frac{\arctan2}{\pi}<\frac12.
\tag{8}
\]
This conclusion uses the completed-root grammar. It does not assert the
stronger individual-leaf cutoff \(X\ge2/3\), which is a separate source
certificate.

For later source bounds, an attachment with \(X\le2/3\) has
\[
\begin{aligned}
\frac1{2X}-X&<B<X,\\
\mu=f_{\mathrm{child}}'(b_{\mathrm{child}})
 &=\log\frac{X^2}{1+B^2-X^2},\\
\lambda=f_{\mathrm{parent}}'(b_{\mathrm{parent}})
 &=\mu+2\log(X+B).
\end{aligned}
\tag{9}
\]
On \(1/2<X\le2/3\), both slopes belong to \((-2\log2,0)\).
For either the child or parent, \(Y<1\) gives
\(2\log(X/Y)>2\log X>-2\log2\). Its hyperboloid identity gives
\(Y^2=1+B_{\mathrm{port}}^2-X^2\ge1-X^2>X^2\), since \(X^2<1/2\);
therefore \(2\log(X/Y)<0\). These are the geometric parameter bounds
used by the separate alias comparison.

## 4. Actual complete metric and topology

Each new \(hE/Eh\) product is an attachment already used inside the
original \(h^s\) seeds: one genuine leaf pyramid, one completed child
cell and the original ideal multiplication prism. The strict variables
of §1 give the same positive tetrahedra and ordered input-face metrics.
Use the original
[ordered prism maps](actual_newton_ideal_prism_and_associativity.md)
\[
\begin{aligned}
F:(C_0,C_1,C_2,C_3)&\longmapsto(v_0,v_1,P,\infty),\\
G:(C_0,C_1,C_2,C_3)&\longmapsto(\infty,P,v_2,v_3).
\end{aligned}
\]
The leaf-side CAP sums are \(\pi/2\) where the corresponding completed
child sum would be \(\pi\); every other seam angle is the same original
strict angle or flat \(\pi\) sum. These are exactly the one-leaf
attachment cases of the
[complete cell construction](actual_positive_conway_hyperbolic_volume.md),
§4. Supported-face gluing is convex, creates no accidental vertex
identifications off the common face, and yields the completed output
corner pattern PORT, WHITE, SHADED, WHITE.

All expressions in (1) are therefore actual convex ideal completed cells.
Turns apply only to those cells, so their original ordered rotation and
color pattern apply. The root has two completed children. Its original
\(j\mapsto3-j\) closing map matches both FREE and CAP pairs with angle
sum \(\pi\); the resulting closed polyhedron is right angled.

The [literal crossing-disk bowtie cut](actual_conway_bowtie_projection_cut.md)
uses the original leaves, stacks and turns, without a lower bound on
the size of a child subtree. Its segment pairings and white facial
cycles agree with the metric prism maps. It gives the actual closed
augmented-link exterior with degree one. Canonical rectangular cusp
decorations and the four-step pointwise edge words prove complete
finite volume.

Retained signed half twists replace only the original shaded pairings
within their leaf disks by the
[checked cross-copy pairings](actual_conway_half_twist_partner_geometry.md).
Both complete cusp decorations and all pointwise pure/odd edge words
remain valid. For every fixed half-twist pattern,
\[
\operatorname{Vol}(Y_E^\epsilon)
 =\operatorname{Vol}(Y_E^0)=2\pi F_0.
\tag{10}
\]
This identifies the actual augmented-link geometry with its original
marking.

The constructive knot parity survives the new operations. A leaf has
the two choices \(\{U,X\}\), and the \(hh\) base has \(\{I,U\}\).
The original loop-free product table sends every pair of two-element
feasible sets to a set with at least two elements, after excluding
its sole circle-producing pair \(U\) times \(U\). This applies to
\(hE/Eh\) and to \(EE\), and a turn permutes the three types.
Each completed expression consequently has at least two loop-free
choices. The root can be chosen \(U\) or \(X\), whose cylindrical
closures have one main component. Either half-twist sign realizes an
odd leaf; integral full twists preserve the selected endpoint pairing.

## 5. Primitive lattice, selected packet and marked deformation

With \(H\) physical leaves, the original full binary source tree has
\(H-1\) products. Removing the forced final gate leaves \(H-2\).
Contract all turns integrally by \(r_{\mathrm{out}}=d-r_{\mathrm{in}}\)
and solve the single root input relation for a variable in one of its
disjoint child trees. The remaining original wire lattice is primitive
\(\mathbb Z^{2H-3}\). No relation \(2r=d\) is introduced. The strict
state gives a parity-independent integer window and every-level
rounding for all sufficiently large \(N\), as detailed in the
[finite source composition proof](actual_conway_single_leaf_source_composition.md).

By (8), every leaf lies in a fixed compact high-index interval
\((1/4,1/2)\), and every retained factorial argument is strict.
The exact pure/signed local coefficient formulas, continuous chirp,
selected transport root and exponential interpolation error in the
[original signed packet](actual_odd_conway_complex_color_packet.md)
therefore apply on a fixed complex tube. They do not require both
inputs of every retained product to be completed.

The \(H\) leaf factors and \(H-2\) gates have total prefactor
\(N^{3-H}\). The primitive \((2H-3)\)-dimensional lattice Gaussian
contributes \(N^{(2H-3)/2}\), giving \(N^{3/2}\). All original integer
offsets are retained with the changed local derivatives \(f_\epsilon\)
and the unchanged gate derivatives. The external phase remains
\[
\eta_N=\exp\left(\frac{i\pi(N-1)}4\sum_\ell\epsilon_\ell\right).
\]
At completeness the normalized amplitude is the positive pure one
times
\[
\prod_{\epsilon_\ell\ne0}
 \sqrt{\sin(\pi a_\ell)}
 \exp\left(-\frac{i\epsilon_\ell\pi a_\ell}{2}\right),
\]
and is nonzero. The color Hessian entries are
\[
-\frac{2\pi X_\ell}{1-\epsilon_\ell iX_\ell},
\tag{11}
\]
with strictly negative real part. The original finite
tensor-cotangent rectangle proof retains every boundary connector
and nonconstant kernel mode. It supplies the same exact finite
complex packet locally, with the original lattice and normalization.

For the geometric interpretation, the selected local shear
\[
\chi=t-\frac{\epsilon g_t}{2\pi i},\qquad
f_\epsilon=g-\frac{\epsilon g_t^2}{4\pi i}
\]
is regular because every leaf is strictly high in (8).
The nine [original rational prism identities](actual_odd_conway_marked_peripheral_deformation.md)
also cover \(hE/Eh\): a leaf input is already a permitted prism input.
The turn and completed/completed closing identities remain unchanged.
They give one actual white-face map and the same pure/odd shaded edge
words on the original bowtie quotient.

The resulting signed augmented-link representation has its original
parabolic main cusps, primitive auxiliary logs
\[
U_\ell=-2\pi i\chi_\ell,\qquad
V_\ell=-2\partial_\ell\Phi_\epsilon,
\]
and the absolute primitive \(G=2\pi i\Phi_\epsilon\), including the
correction \(-\epsilon_\ell V_\ell^2/8\). Its complete anchor is (10).
The original regulator identity and geometric completion give
\[
\begin{aligned}
U_\ell+p_\ell V_\ell&=-2\pi i,\\
\operatorname{Vol}\bigl(Y_E^\epsilon(p)\bigr)
 &=2\pi\operatorname{Re}\left[
   \Phi_\epsilon(\chi_*)+
   \frac{\pi i}{2}\sum_{\ell\ \mathrm{filled}}
       \frac{(\chi_\ell-1)^2}{p_\ell}\right].
\end{aligned}
\tag{12}
\]
The physical powers are \(\epsilon_\ell-2p_\ell\). After all auxiliary
fillings and a loop-free one-main-component parity choice, (12) is
the actual knot complement volume. The knot cusp remains unfilled.

The whole mixed-source alias and complement estimates are separate
inputs to the full invariant limit. The existing all-core majorant
and far-color local estimate apply by (8); the
[single-leaf alias theorem](actual_conway_single_leaf_alias_composition.md)
and its finite source companion supply the new block comparison.
The local geometric and packet conclusions above do not substitute
for those estimates.

## 6. The root-leaf frontier is genuine

The theorem above requires two completed root children. For the different
closure \(C(hT(A_s))\), \(s\ge2\), the exact state is
\[
\begin{aligned}
A_s:&\quad X=1,\quad B=Y=1/s,\\
T(A_s):&\quad(B,X,Y)=(-1/s,1/s,1),\\
h:&\quad(B,X,Y)=(1/s,1/s,1).
\end{aligned}
\tag{13}
\]
The inner seed leaves all equal \(1/4\); the root leaf equals
\(\arctan(s)/\pi\), with cotangent \(1/s\). Every retained seed gate
is strict. Its successive output labels are \(b_j=\arctan(j)/\pi\),
and
\[
b_{j-1}<b_j<b_{j-1}+\frac14<1.
\]
The complete source therefore has a genuine strict optimizer.
The original one-leaf/completed-child closing case has CAP sum
\(\pi/2\), rather than \(\pi\), and the remaining convex cut/cusp
proof gives the actual complete finite-volume metric. A flat-cell
argument does not rule out this configuration as nonhyperbolic.
The same local complete half-twist pairing proof applies.

The limitation on reusing the signed high-index packet is its inner
leaves at exactly \(1/4\). In the complete local source recurrence,
the selected transport root and its competitor have equal modulus
there, while their algebraic values remain distinct. For example,
the original characteristic equation at \(x=1/4,t=0\) has roots
\(\mu=\pm i\). This is a dominance boundary, not an eigenvalue
collision. The old uniform high-index interpolation and
decaying-competitor proof does not extend across it without
additional source analysis.

For \(s\ge3\), the root leaf even has cotangent below \(1/2\).
These facts do not contradict (8): in (13), the root completed
port has \(Y=1\), and its top turn exposes an internal completed
\(X=1\). The strict root bounds (6) are unavailable.

The still broader syntax \(C(hT(h))\) has the exact complete scalar
\(\sum_r a_{N,r}^2\) and leaves at \(1/4\). This is a source-level
warning against deducing a strict high-quarter packet from strict
feasibility alone. Its separate complete geometric realization is
not needed for the completed-root theorem.

## Dependencies and internal review scope

The geometric inputs are the
[ordered ideal prism](actual_newton_ideal_prism_and_associativity.md),
[complete cell and cap construction](actual_positive_conway_hyperbolic_volume.md),
[stationary port identities](actual_conway_strict_leaf_quarter_bound.md),
and [literal bowtie cut](actual_conway_bowtie_projection_cut.md).
The [two-leaf geometry audit](actual_conway_two_leaf_seed_geometry.md)
records the retained base and original primitive conventions.
The local analytic inputs are the
[signed complex packet](actual_odd_conway_complex_color_packet.md)
and [actual marked deformation](actual_odd_conway_marked_peripheral_deformation.md).
The separate new source and alias companions are linked above.

The author, root and two independent internal reviewers completed
full analytical and source-interface reviews of §§1–6, including
the actual one-leaf CAP maps, completed-root propagation, primitive
lattice, marked action constants, knot parity and the distinct
quarter-angle frontier. This is internal proof review, not external
peer review or a numerical audit. The note does not assert a theorem
for arbitrary turned-leaf syntax or all arborescent links.
