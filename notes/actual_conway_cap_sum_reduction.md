# Exact cap-sum reduction of the source and its volume problem

29 October 2026. There is a general topological reduction of the actual
positive Conway class, before any hyperbolic gluing problem is attempted.
A cap closure of a stack is a componentwise connected sum of its cap
closures. Its original full-normal quantum source factors exactly, and
its entire angle polytope and volume functional factor with it.

This does not turn a Conway four-punctured sphere into a rigid pair of
pants. The separating surface used here is an explicitly different
sphere: it crosses only the TWO wires between stacked boxes, after the
outer cap closure has been made. The result applies to arbitrary boxes
in the actual Conway algebra, not just to a pure run of circles.

## 1. Two closures and the exact source identity

Use the physical boxes, genuine turn R, Newton basis Bhat_r, and original
pointed functional phi of the
[actual Conway compiler](actual_positive_complete_circle_conway_trees.md).
Put d=N-1. For a box F write

    C_N(F)=phi(F),           D_N(F)=phi(R F).

The first is its ordinary two-strand cylindrical closure. Rotating the
second diagram back to the original position of F identifies it with
the cap closure: the two upper ports are joined to each other and the
two lower ports are joined to each other. The same actual cups, caps,
and single mark are retained. This is a description of a literal
closed diagram, not of an extra functional invented for the proof.

For F=sum f_r Bhat_r the established actual turn gives

    C_N(F)=f_d,              D_N(F)=f_0.

The full repeated-root multiplication rule has only ONE contribution
at coordinate zero: i=j=k=0, with coefficient one. Therefore for ANY
two actual boxes in this algebra,

    D_N(FG)=D_N(F)D_N(G).                              (1)

There is no positivity hypothesis in (1); no root normal, auxiliary
color, or framing scalar is removed. All factors are the raw sources
of their recorded diagrams. Framing conversions, if desired, retain
their separately recorded unit characters. This equality is proved
in the actual full Newton algebra, not by citing a multiplicativity
theorem for a different link invariant.

For the robust positive class, D_N(F),D_N(G)>0 for N>=3. Iterating (1)
gives an exact product for every finite cap-closed stack. The two turns
also satisfy C_N(RF)=D_N(F) and D_N(RF)=C_N(F), because R reverses all
Newton coordinates. At the level of unmarked closed diagrams, these
last relations are realized by rotating the whole closed diagram;
when a point is recorded, it must be transported with that rotation.

The supplied source identities already specify their marks. They do
not assert that arbitrary choices of a marked component of an arbitrary
link have been proved equivalent.

## 2. The actual separating sphere and its component labels

Put the lower box F and upper box G in disjoint balls, and connect their
two interface ports by two short vertical arcs in an otherwise empty
collar. Perform the cap closure outside the two boxes: the lower pair
of F is capped, as is the upper pair of G. Every auxiliary component
stays in its own box. Choose a horizontal disk through the middle of
the interface collar. Closing that disk around the lower ball and its
lower cap in the empty exterior gives a sphere S which meets the link
in exactly the TWO interface arcs, once each, and no other component.

Cut along S and cap its two punctures on each side by a trivial arc.
The lower resulting link is exactly the cap closure of F: the newly
inserted arc is its upper cap. The upper resulting link is exactly the
cap closure of G: the inserted arc is its lower cap. This is a reversible
construction, with the original ribbon framing inherited by each arc.
Thus, as an actual unmarked link,

    cap(FG)=cap(F) #_(upper cap of F, lower cap of G) cap(G). (2)

The subscript is essential. A general cap-closed box can have its
upper and lower caps on DIFFERENT main components. Equation (2) does
not silently choose an arbitrary distinguished component in either
factor. Nor does the proof use a linking matrix to recognize the link:
the empty collar and its two-punctured sphere exhibit the connected
sum directly.

If c(F) counts all components in cap(F), then

    c(FG)=c(F)+c(G)-1.                                 (3)

All components other than the two named cap components remain intact.
For more than two factors, use parallel interface spheres, obtaining a
tree of componentwise connected sums with the cap labels retained.
The original marked point can be followed through this construction;
(1) is independently the exact identity for the compiler's specified
marked source, so no change-of-mark theorem is needed to infer it.

This reduction is special to the cap closure. An ordinary cylindrical
closure of FG has an outside return running across the same cut and
does NOT give this two-punctured sphere. Its exact source is instead
the full pairing sum_i f_i g_(d-i), which in general does not factor.

## 3. The entire variational problem splits, including its boundary

For any fixed robust expression F, let P_F^0 be its wire polytope from
the [whole-source variational theorem](actual_positive_conway_variational_limit.md),
but with final output 0 instead of 1. Let V_F^0 be the SAME sum of
leaf and multiplication tetrahedral volumes, restricted to this face.
Equivalently these are the polytope and volume function for R F with
its final turn wire deleted. Thus the proved full-sequence limit is

    lim_N (2pi/N)log D_N(F)=2 max_(P_F^0) V_F^0.         (4)

For the cap-closed product FG, the final product has output z=0.
The exact constraints max(x,y)<=z<=x+y force x=y=0. Its product
weight is exactly one at every level, and its continuous product
action is m(0,0,0)=0. More explicitly, the three product angle triples
are all (0,0,1), so the entire final gate is flat.

Deleting the forced wires therefore gives the literal affine identity

    P_(FG)^0 = P_F^0 x P_G^0,
    V_(FG)^0 = V_F^0 + V_G^0.                          (5)

These equalities hold on the whole CLOSED polytopes, not just near a
saddle. They include boundary maxima and every shared wire inside
each factor. Consequently

    max V_(FG)^0 = max V_F^0 + max V_G^0.               (6)

At the exact integer level the state sets have the same Cartesian
product and the weights multiply. Thus (5) is stronger than deriving
additivity after taking a limit: both its quantum and angle versions
come from the same forced zero-coordinate conservation law.

The stationarity equations for nonflat atoms split into the two
independent systems as well. Any claim of a single nondegenerate
geometric critical point for the unreduced whole expression must first
remove this forced-flat gate and respect the topological decomposition
(2). Uniqueness or algebraicity of the two reduced optima does not
erase the connected-sum sphere.

## 4. A general boundary reduction procedure

Retain a closure flag C or D alongside the actual expression tree.
At a turn, switch the flag and retain the child's diagram and mark.
At a product with flag D, split into the two children, each with flag D,
and record the sphere and its upper/lower cap labels from section 2.
At a product with flag C, stop at that factor. Leaves are retained.

This terminates since each step removes at least one expression vertex.
It yields simultaneously:

* an exact product of original source scalars;
* an exhibited componentwise connected-sum decomposition of the
  unmarked closed diagram, with transported marked data recorded;
* a Cartesian product decomposition of its reduced angle polytopes,
  and an additive decomposition of their volume functions.

No assertion of primeness is attached to the factors at which this
procedure stops. A four-punctured Conway seam inside such a factor
still needs its actual incidence and completeness proof. This is an
exact boundary reduction, not a complete JSJ algorithm.

## 5. Positive exponential growth can come from several hyperbolic pieces

Let A=h^3 be the robust seed and set, for k>=1,

    E_k=R((R A)^k).

The whole original scalar satisfies, at EVERY N>=3,

    C_N(E_k)=C_N(A)^k.                                  (7)

This follows from (1) and R^2=1 on the actual algebra. In this particular
family there is no ambiguity about the connected-sum component:
A has U main pairing and two internal main circles; R A has through
pairing and the same two internal circles. In its cap closure the
upper and lower caps therefore lie on ONE main component. Every
interface sphere in section 2 joins those components. Rotating the
closed factor back identifies it with the actual theta closure C(A),
including the transported point on that component.

The [theta-link geometry](actual_marked_theta_link_and_angle_geometry.md)
already proves that this factor is the literal untwisted six-component
augmented theta link, has four regular ideal octahedra, and satisfies
the original-source limit 4v8. Consequently E_k is an actual
componentwise connected sum of k such theta links and has

    number of components = 5k+1,
    lim_N (2pi/N)log C_N(E_k)=4k v8.                    (8)

For k>=2 its complement is not a complete finite-volume hyperbolic
manifold. Here is a group proof which avoids inferring topology from
the scalar. The explicit sum sphere gives, by cutting collars and
van Kampen, an amalgam of the two summand groups over the infinite
cyclic subgroup generated by the glued component's meridian mu.
Each theta summand is already proved complete hyperbolic, so its cusp
group injects as Z^2. Choose a longitude lambda_1 and lambda_2 in the
two adjacent summands. Each commutes with mu, and neither lies in
<mu>. The amalgam normal-form argument says that their commutator
lambda_1 lambda_2 lambda_1^-1 lambda_2^-1 is nontrivial: its four
letters alternate between the factors and none lies in the amalgamated
cyclic subgroup. Their images remain nontrivial after further sums by
the same normal form.

In a torsion-free orientation-preserving hyperbolic manifold group,
the centralizer of a nontrivial parabolic is abelian. To see this
directly, conjugate that parabolic to z->z+1. A commuting Mobius map
must fix infinity, hence has form z->az+b; commutation forces a=1.
All such translations commute. Here mu would be the meridian of an
actual cusp and hence a nontrivial parabolic, contradicting the two
noncommuting longitudes in its centralizer. This proves the stated
nonhyperbolicity.

Equation (8) is therefore equality with the SUM of the volumes of
the exhibited hyperbolic summands, not the volume of a nonexistent
complete hyperbolic structure on the whole complement. No general
simplicial-volume or JSJ-identification theorem is needed or claimed
for this statement. It supplies a necessary scope check for any
proposed universal Conway volume theorem, while preserving the exact
whole-source and variational information.

## 6. What remains after the reduction

This result supplies a general topology-compatible reduction rather
than a new primitive hyperbolic equality. It strengthens the earlier
pure cap-run example: the obstruction persists with arbitrary positive
rates and with genuine complete hyperbolic factors, so a nonzero
variational maximum is not a hyperbolicity certificate.

For each retained cylindrical factor, the outstanding task remains
the actual global face/edge/peripheral dictionary for its nonflat
angle functional. The two-punctured sum spheres above can be removed
before that task. An internal four-punctured seam cannot be removed
by the same argument.

Audit: [exact full-source, support, and component checks](../experiments/audit_actual_conway_cap_sum_reduction.py)
and [results](../experiments/actual_conway_cap_sum_reduction_results.json).
The finite calculations supplement the uniform algebraic identity,
explicit sphere construction, and variational Cartesian-product proof;
they are not numerical manifold recognition or a proof for unreduced
primitive factors.

The cap-sum decomposition identifies connected sums. It does not identify an unreduced diagram with a primitive hyperbolic complement.