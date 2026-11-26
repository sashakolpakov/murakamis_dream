# Half-boundary pressure comparison for complete whole-hub regions

Private proof, 1 November 2026. This note concerns the old positive
source only. It does not estimate moving higher-valence trace terms.

The simultaneous-half comparison extends from trivalent old regions
to arbitrary finite trees of old product hubs of valence at least
three. The strict witness is constructed on the physical edges first
and then extended through each ordered binary resolution. The
artificial unturned edges do not receive the physical-edge label
\(3/8\).

## 1. The pressure and the statement

Use the original positive Newton product action
\[
\begin{split}
 m(x,y,b)={}&J(x+y)+J(b)-J(x)-J(y)\\
            &-J(b-x)-J(b-y)-J(x+y-b),\qquad
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,
\end{split}
 \tag{1}
\]
on \(\max(x,y)\le b\le x+y\le1\), and the pure boundary action
\[
                 g(a)=J(2a)-4J(a),\qquad 0\le a\le1/2.
 \tag{2}
\]
Consider a finite connected tree of old whole-hub tensors. A hub has
full valence \(D_v\ge3\), counting its external incidences. Each
hub-to-hub edge is a physical quarter-turn and identifies equal
covariant labels. At an ordinary external incidence put the free
profile \(g(a)+c\). A marked incidence has a prescribed covariant
label \(z_i\) and contributes no variable boundary action. Assume
that each hub has at most one marked incidence and that there is at
least one marked incidence in the region. With no marked incidence
there is no boundary comparison to make.

Resolve each old hub by its original ordered positive binary
products, retaining their hidden variables and the exact final
complementary pairing. The artificial internal edges are unturned;
their covariant labels are complementary. Equivalently, after rooting
the region, their ordinary output and input coordinates agree without
a turn. Let \(\Psi(\mathbf z)\) be the maximum of the sum of (1) and
all ordinary boundary profiles, over this full compact wire polytope.

For changing the root, one can keep the very same resolved tree.
The cubic action \(t(x,y,z)=m(x,y,1-z)\) is symmetric in its three
covariant labels. An unturned edge has complementary labels at its
ends, whereas a physical-turn edge has equal labels. These relations
remain the same when the direction of recursive evaluation reverses.
Thus rooting at another marked terminal is an exact reexpression of
the same real action and constraints.

The positive associative identities also imply that this boundary pressure
is independent of the chosen resolution. This is an equality of the
old finite positive contraction and its coefficient action; it is not
an assertion about isotopies of arbitrary tangles. The fixed-label
support and resolution statement is proved in
notes/actual_conway_reduced_hub_source_normal_form.md, Section 2.

**Theorem.** At \(\mathbf z_0=\tfrac12\mathbf1\), the resolved
constrained maximum is unique and strict. Its pressure is analytic
near \(\mathbf z_0\), with negative definite Hessian, and
\[
              \partial_{z_i}\Psi(\mathbf z_0)\le0.
 \tag{3}
\]
For every feasible boundary vector with all \(z_i\ge1/2\),
\[
                      \Psi(\mathbf z)\le\Psi(\mathbf z_0).
 \tag{4}
\]
The inequality is strict if \(\mathbf z\ne\mathbf z_0\). It compares
all marked coordinates simultaneously and does not assert monotonicity
in one coordinate while the others remain above half.

## 2. A strict witness in every prescribed resolution

For positive input labels \(a_1,\ldots,a_k\), the exact strict product
lemma is
\[
 a_i+a_j<1\quad(i\ne j),\qquad
 \max_i a_i<b<\min\left(1,\sum_i a_i\right).
 \tag{5}
\]
These conditions are necessary and sufficient for strict intermediate
gates with output \(b\), for every fixed binary association.

Here is the constructive part of that lemma. For a child set \(S\),
write \(L_S=\max_{i\in S}a_i\) and
\(U_S=\min(1,\sum_{i\in S}a_i)\). A nonsingleton child may take any
value in \((L_S,U_S)\); a singleton takes its prescribed label. At a
parent with target \(b\), restrict both child values below \(b\).
Their lower sum is less than one, by the pair condition, and their
upper sum is greater than \(b\), by the total condition. Choose a sum
strictly between \(b\) and one. If both children are singletons, their
fixed sum is already in this interval. The two chosen child values
are less than \(b\), so the parent is strict; repeat down the fixed
binary tree. This constructs every hidden wire.

For a whole hub with external covariant labels \(a_1,\ldots,a_D\),
exposing incidence \(D\) makes the ordinary product output
\(b=1-a_D\). Thus (5) is equivalent to
\[
       a_i+a_j<1\quad(i\ne j),\qquad \sum_{i=1}^D a_i>1.
 \tag{6}
\]
It proves strict feasibility in every prescribed resolution of the
closed hub, with only the final forced flat pairing omitted.

Now set every marked physical label to half and every other physical
edge or ordinary boundary label to \(3/8\). At an unmarked hub all
pair sums are \(3/4\), and its total is at least \(9/8\). At a marked
hub the largest pair sum is \(7/8\), and its total is at least
\(5/4\). Hence (6) holds at every hub. Apply the constructive lemma
inside each hub independently, keeping the already assigned physical
edge labels. It supplies a global strict state in the fixed original
resolution. The same inequalities have positive margins under small
independent changes of all marked labels, so the feasible boundary
domain contains an open neighborhood of \(\mathbf z_0\).

This is the point at which the higher-valence argument differs from
assigning \(3/8\) to an artificially resolved trivalent graph. Only
physical edges receive that assignment. Hidden ordinary output wires
are constructed from (5); complementary covariant coordinates on
unturned edges are then automatic.

## 3. The constrained maximum is strict and analytic

Root the whole region at a marked incidence. A local hub is an
ordered product of its other inputs with ordinary output equal to one
minus its parent covariant label. The binary gates inside it are
unturned. At a physical edge the actual turn supplies the complement
before the next hub. Marked terminals other than the root remain
fixed at half, without a leaf volume atom.

Apply the original nonvertex-flat barrier to the segment toward the
strict witness. An atom \((0,a,1-a)\), \(0<a<1\), has inward derivative
\(+\infty\); positive atoms and vertex-flat atoms have finite
derivatives. No negative infinite term can cancel it.

An ordinary product output zero forces its two inputs to zero. An
output one either gives two interior inputs summing to one, hence a
nonvertex-flat atom, or has an endpoint input through which the
descent continues. A physical turn exchanges zero and one; an
unturned artificial edge leaves that ordinary endpoint unchanged.
The descent strictly follows child edges in the finite resolved
tree. It cannot end at a fixed half terminal or at the fixed root
output. It must reach an ordinary leaf endpoint or a nonvertex-flat
interior pair. An ordinary leaf at either zero or half supplies its
own nonvertex-flat atom. Thus all variable wires and ordinary leaves
are interior at the maximum.

With these wires interior, the original gate-face check applies
unchanged: setting any of
\(b-x,b-y,x+y-b,1-x-y\) to zero gives a nonvertex-flat tetrahedron.
Every retained gate is therefore strict. This argument is exactly the
old boundary proof in
notes/actual_conway_boundary_volume_relation.md, Section 4, with fixed
half terminals added and both kinds of internal edge kept explicit.

The sum of the strict gate Hessians is negative definite on all
resolved free coordinates; each variable occurs at a gate, and its
three-label angle map has no kernel. Ordinary leaf Hessians reinforce
this. The same statement holds when the marked boundary labels are
allowed to vary: each of them also occurs at a gate. Consequently the
constrained optimizer is unique, its implicit continuation is analytic,
and the Schur complement giving the Hessian of \(\Psi\) is negative
definite near \(\mathbf z_0\). Compactness keeps this local critical
point as the global constrained maximum near the all-half boundary.

## 4. Response induction through both types of edge

At a strict boundary response put
\[
 B=\cot\pi b,\qquad
 X^2=\frac{1+B^2}{1+\kappa},\qquad Y^2=\kappa X^2,
 \qquad \kappa=e^{-f'(b)}.
 \tag{7}
\]
An ordinary \(g\) leaf has \(B=X>0,Y=1\). A fixed half terminal has
no profile derivative; choose its positive response from the incident
strict prism, \(\kappa=e^{m_x}\) in an input coordinate. Since its
cotangent is zero, it satisfies the proper inequality \(-Y<B<X\).
This assignment adds no action and does not interpret the fixed
terminal as a new physical leaf.

At a stationary internal wire, direct differentiation of the original
product action gives a common positive \(X\) and
\[
 B=\frac{B_1B_2+X^2-1}{B_1+B_2},\qquad
 Y=\frac{Y_1Y_2}{B_1+B_2},\qquad B_1+B_2>0.
 \tag{8}
\]
Inputs satisfying \(-Y_i<B_i\le X\) produce a proper output. For
\(X\ge1\), the inputs are positive and
\[
 B-X=\frac{(X-B_1)(X-B_2)-1}{B_1+B_2}<0;
 \tag{9}
\]
the factors are zero for a leaf input, or smaller than
\(X-\sqrt{X^2-1}\le1\) for a proper input. Also \(B>0>-Y\).
For \(X<1\), put \(h=\sqrt{1-X^2}\) and write
\(B_i=h\cot\alpha_i,Y_i=h\csc\alpha_i\). The input bounds give
\(\alpha_i\ge\arccos X\), and the positive denominator in (8) gives
\(\alpha_1+\alpha_2<\pi\). The output is
\(B=h\cot(\alpha_1+\alpha_2),Y=h\csc(\alpha_1+\alpha_2)\), which is
proper as well.

Along an artificial unturned edge, this proper product output is used
directly as the next product input. Along a physical turn it becomes
\((-B,Y,X)\), which is again proper. Thus the induction is valid
through arbitrary ordered resolutions and arbitrary physical turns.
No turn of an ordinary boundary leaf is inserted into this induction.

Choose marked incidence \(i\) as the root. Its ordinary output is
\(b=1-z_i=1/2\). At the final binary product, strict support makes
both input labels less than half. Thus \(B_1,B_2>0\), and (8) gives
\[
       1-X^2=Y^2=B_1B_2\le X^2,
       \qquad \partial_{z_i}\Psi(\mathbf z_0)
                       =-\log(X^2/Y^2)\le0.
 \tag{10}
\]
The pressure is independent of the rooted positive resolution, so the
same argument may expose each marked incidence in turn. This proves
all components of (3) for the same boundary pressure. No geometric
isotopy is inferred from that scalar reexpression.

## 5. Simultaneous comparison and its strictness

The joint pressure is concave: combine feasible maximizing resolved
states by convex interpolation. Its supporting plane at
\(\mathbf z_0\), together with (3), gives (4).

This also applies at a closed feasible endpoint. For
\(\mathbf v=\mathbf z-\mathbf z_0\ge0\), concavity gives
\[
 \Psi(\mathbf z)-\Psi(\mathbf z_0)
 \le\frac{\Psi(\mathbf z_0+t\mathbf v)-\Psi(\mathbf z_0)}t.
 \tag{11}
\]
For small positive \(t\), the right side is evaluated on the analytic
strict branch. Its limit is \(\nabla\Psi(\mathbf z_0)\cdot\mathbf v
\le0\), proving the endpoint inequality without differentiating a
degenerate optimizer. If \(\mathbf v\ne0\), the negative definite
Hessian gives a strictly smaller right side for sufficiently small
positive \(t\). This proves the strict assertion in the theorem.

The gradient is in fact strictly negative at a marked incidence
unless the whole region is one trivalent hub with two ordinary leaf
inputs. In every other case the final binary product has a proper
composite child, so one bound \(B_i\le X\) in (10) is strict. In the
exceptional two-leaf product the derivative at half is zero, while
the strict inequality in (4) away from half still follows from (11).

## 6. What this does not prove about moving higher-valence hubs

The theorem is a geometric inequality for the old positive pressure,
with every hidden resolution variable retained. It can compare old
regions with several high boundary labels without assigning them
independent capped volumes. The requirement of at most one marked
incidence per actual hub is essential to the strict all-half witness:
two prescribed half incidences at the same hub already saturate one
pair inequality.

This does not supply the missing moving-hub comparison. A moving
higher-valence trace can have additional terms with every exterior
index low. An artificial unturned resolution can also have adjacent
moving additional terms, with complementary labels on their common
edge. Such terms do not furnish the two-high/one-low pattern used by
the trivalent replacement argument. Nothing above discards them or
adds a replacement leaf profile to each of their arms.

Accordingly no new full-source, meridian-profile, or filled-volume
class follows from this old-pressure theorem alone. The remaining
problem is a whole-hub moving estimate compatible with this coupled
old pressure.
