# Arbitrary widths in the actual Conway seed grammar

30 October 2026. The restriction to the seed h^3 is unnecessary.
Let A_s=h^s for any fixed integer s>=3, using s separate original
complete-circle coupons and their actual stack product. Expressions
may use any finite mixture of these seeds, literal turns, and products.
Every retained C(FG) with two such expressions has the same strict
source geometry and signed mixed-source estimates as the original
three-leaf grammar. The proof below checks the changed seed hypotheses;
it does not infer them just from an expression name.

There is also an extension to the isolated cylinder C(A_s) for s>=4.
The isolated C(A_3) remains outside the whole mixed-color gap proved
here. All sizes, trees, signs and filling slopes are fixed before the
level tends to infinity. No uniform estimate over unbounded diagrams
is asserted.

## 1. Full finite support and an interior optimizer

The full Newton coefficients of h_N are positive at every index
0<=r<=M=floor((N-1)/2), including its constant coefficient N^2.
For N>=3, A_3 already has strictly positive coefficients at EVERY
index 0,...,N-1. Since Bhat_r Bhat_0=Bhat_r, multiplication by h
preserves that full strict support. Thus A_s=A_3 h^(s-3) has full
support for all s>=3 and every N>=3. This is the actual repeated-root
algebra identity, including its normal directions. The old N=2
exception is unchanged.

Here is the continuous strict-feasibility argument, separately from
the finite support. A strict state of a seed has leaves in (0,1/2)
and, at every gate (x,y)->z,

    max(x,y)<z<x+y<1.                                      (1)

A_3 admits such a state at every prescribed output b in (0,1).
Given this property for A_(s-1), choose

    0<c<min(b/2,1-b,1/4),   t=b-c/2.

Use its strict state at output t and a last leaf c. The gate
(t,c)->b obeys (1). This proves feasibility for every A_s. At a
macro-product choose both child outputs in
(b/2,min(b,1/2)); at a turn use the child output 1-b. Hence every
proper expression admits a strict state at every interior output.

For C(FG), delete only the forced last gate: its inputs sum to 1
and its exact finite coefficient equals one. Choose both child
outputs 1/2 to obtain a strict state of the reduced problem. For
C(A_s), s>=4, choose its last leaf c in (0,1/2) and the preceding
A_(s-1) output 1-c. Again every retained atom is strict.

The boundary barrier is unchanged but is worth making explicit.
The leaf atoms are (x,1/2-x,1/2), twice; with
p=z-x,q=z-y,r=x+y-z,w=1-x-y the gate atoms are

    (y,x,w), (p,q,2r+w), (p+q,r,r+w).                       (2)

Every nonvertex-flat atom (0,a,1-a), 0<a<1, has positive infinite
directional derivative toward the constructed strict state. A
vertex-flat atom has a finite derivative and cannot cancel it.
A proper endpoint wire propagates down through turns and products
until either a product has interior inputs summing to one, or a
leaf equals zero. Both exhibit a nonvertex-flat atom. A leaf at
1/2 does also. With every proper wire interior, any equality in
(1) displays such an atom directly in (2). Therefore no boundary
state maximizes the action.

Each positive tetrahedron is strictly concave in its independent
angles. The retained angle maps recover every leaf and product wire;
turns then recover their wires too. The removed last gate adds no
free tangent direction. Thus the reduced Hessian is negative definite,
the optimizer is unique and strict, and every fixed proper-output
profile is real analytic on (0,1). This proof uses no special property
of the number three after constructing a strict seed state.

## 2. Exact open seed ports for every width

For the optimized output b set B=cot(pi b), kappa=exp(-f'(b)),

    X=sqrt((1+B^2)/(1+kappa)),   Y=sqrt(kappa) X.

Then X^2+Y^2-B^2=1. The actual product stationarity equations give
one common X for its two inputs and output, and

    B_out=(B_left B_right+X^2-1)/(B_left+B_right),
    Y_out=Y_left Y_right/(B_left+B_right),
    B_left+B_right>0.                                      (3)

A leaf has B=X=cot(pi a)>0 and Y=1. Consequently every optimized
A_s has the SAME a at all its s leaves. Iterating (3), with no
restriction placed on the finite source labels, gives

    B_s=T_s(X)/U_(s-1)(X),   Y_s=1/U_(s-1)(X),              (4)

where T and U are the usual Chebyshev polynomials. These are formulas
for the optimizer, not a reduction of the original sum to equal labels.
For example the open optimum is on the algebraic branch

    T_s(X)-cot(pi b) U_(s-1)(X)=0.                          (5)

The output b here is the Newton coordinate, not a renamed physical
meridian.

The branch and its inequalities follow directly from the positive
denominators in (3). If 0<X<1 put alpha=arccos X and h0=sin alpha.
Induction gives

    B_j=h0 cot(j alpha),   Y_j=h0 csc(j alpha),
    0<j alpha<pi, 1<=j<=s.                                (6)

Indeed B_j+X=h0 sin((j+1)alpha)/(sin(j alpha)sin alpha).
Starting at alpha in (0,pi/2), positivity forces the next angle to
remain below pi; it cannot skip the entire negative-sine interval.
Thus X>cos(pi/s). At X=1 the limit is B_s=Y_s=1/s.
For X>1, put beta=arcosh X and h0=sinh beta; then

    B_s=h0 coth(s beta),   Y_s=h0 csch(s beta).             (7)

In every case, for s>=2,

    -Y_s<B_s<X.                                           (8)

For (6), the upper inequality is strict monotonicity of cotangent
and the lower is cot(t)+csc(t)=cot(t/2)>0. For (7), B_s>0 and
coth(s beta)<coth beta; X=1 is immediate. This proves the entire
seed input needed by the old macro-port argument.

## 3. Closure gives a stronger leaf interval at larger widths

The inequality -Y<B<X is preserved by a turn
(B,X,Y)->(-B,Y,X) and by every stationary macro-product. For X<1,
write its child ports as

    (B_1,Y_1)=(h0 cot u,h0 csc u),
    (B_2,Y_2)=(h0 cot v,h0 csc v).

The inequalities give u,v>alpha=arccos X and (3) gives u+v<pi.
The output has angle u+v, so (8) persists. For X>=1, (8) forces
both child B's positive and between sqrt(X^2-1) and X. Therefore
0<X-B_i<1 and

    B_out-X=[(X-B_1)(X-B_2)-1]/(B_1+B_2)<0;

its lower inequality follows from B_out>0.

In a closed C(FG) the two root ports are (B,X,Y) and (-B,X,Y).
Applying (8) to both gives |B|<min(X,Y), hence X,Y<1. These bounds
propagate down every macro-product: its common X<1 is fixed, and
Y_out<1 implies u+v<pi-alpha, while u,v>alpha. Hence each child
has alpha<u,v<pi-alpha and therefore Y_child<1. Turns exchange X,Y.
Stop this induction at a seed, not at its individual leaves, whose
Y equals one.

At a proper A_s seed, (6) and Y_s<1 say

    sin(s alpha)>sin alpha, 0<alpha<s alpha<pi.

Equivalently (s+1)alpha<pi. Its complete leaf label thus satisfies

    cos(pi/(s+1))<X<1,
    1/4<a<atan(sec(pi/(s+1)))/pi
                         <=atan(sqrt(2))/pi=:a0.           (9)

In particular every leaf is in the strict high-index source regime,
and the old universal alias tangent margin applies. Increasing the
seed width strengthens the upper bound; it does not degrade it.

The isolated cylinder C(A_s) is explicit. Its final flat relation
gives B_(s-1)=-X. Formula (3) excludes X>=1; formula (6) then gives
s alpha=pi. Thus

    X=cos(pi/s),   a=atan(sec(pi/s))/pi.                    (10)

For s>=4 this belongs to (1/4,a0], so all required inequalities
hold, including the endpoint a=a0 when s=4. For s=3 it is
atan(2)/pi>a0; that isolated cylinder is still excluded here.

## 4. The actual source and geometry interfaces extend

The extension of the existing signed long-filling proof now follows
by its explicit interfaces, rather than by changing its vocabulary.

* Exact source: every leaf is still the original
  T(R^epsilon L_j), epsilon in {0,+1,-1}. Full Newton multiplication,
  turns, ordinary caps and the exposed mark are unchanged.
* Whole-source bounds: at every complete leaf in (9) or (10), the
  proved tangent inequality dominates the full alias profile by
  c0=2 Catalan/pi-(3/4)log 2>0. The all-color core majorant, actual
  gate concavity and affine-wire cancellation are unchanged. This
  proves the same gap for every alias subset and the physical color
  complement, including the isolated s=4 endpoint.
* Exact complex packet: its leaf finite functions and selected
  changed actions are unchanged. Strictness and the negative Hessian
  provide its fixed window. With H actual leaves the full primitive
  grid still has dimension 2H-3, with every D=N-1 offset retained.
  Its power is N^(3-H+(2H-3)/2)=N^(3/2); equal optimal seed labels
  do not reduce that dimension. The same nonzero odd amplitude and
  exponentially controlled interpolation residual apply.
* Geometry: the seed is the literal stack of the same pyramids and
  prisms. The existing local convex gluing and FREE/CAP angle
  induction apply at each one of its gates. Strictness supplies
  all their required inequalities. Their ordered corner maps are
  the original stack maps, so the closed bowtie cut is unchanged.
  Every complete edge is a leaf bowtie edge, and the same pure/odd
  edge words and canonical rectangle decorations prove completeness.
* Marked deformation: its rational white/prism/turn identities and
  actual signed shaded maps are local. The strict critical branch
  therefore assembles them with the same primitive peripheral paths,
  U=-2pi i chi and V=-2 partial_chi Phi. No new slope or phase
  convention is introduced by a larger seed.

Consequently the quantum and geometric inputs of the
[signed long-filling assembly](actual_odd_conway_long_filling_volume.md)
hold for these enlarged classes. For every fixed signed coupon pattern
and independently sufficiently long signed integral full-twist fillings
of any selected auxiliary circles, the same original-source limit
equals the actual filled hyperbolic volume. The source normalization,
both level parities and the marked peripheral filling equation are
exactly those of that assembly.

## 5. Constructive knot parity for every width

Use the original endpoint pairings I,U,X. A pure leaf has U, an odd
leaf X, and the only loop-creating stack choice is U times U.
An odd-length seed can realize {U,X} without loops: use exactly one
pure leaf or use all odd leaves. An even-length seed realizes {I,U}
without loops by the same two choices. Thus every seed supplies at
least two loop-free types. Turns permute I,U,X; the already checked
set-product table preserves at least two choices under every product.
Backtracking a root choice U or X gives one main component after the
cylindrical closure. Full-twist fillings preserve that connectivity.

Therefore filling all auxiliary circles produces a constructive
knot subfamily for every allowed fixed expression, including isolated
C(A_s) with s>=4. Partial fillings retain one main component together
with the unfilled auxiliary components. This is still a specified
diagram grammar, not a claim covering all arborescent or alternating
knots.

Audit: [seed recurrences, support and interval certificates](../experiments/audit_actual_conway_arbitrary_width_seeds.py).
The proof for unbounded fixed seed widths is the induction and
trigonometric argument above; a finite list of widths does not prove it.

Independent internal review: separate source and geometry readers
checked the all-width strictness/port argument, isolated s=4 endpoint,
full primitive lattice, signed packet interfaces, actual bowtie/cusp
reconstruction and loop-free knot parity choices. The primary agent
checked the displayed recurrences, boundary argument and extension
scope and replayed the focused audit: PASS. The claim remains the
stated grammar, not all k-bridge or alternating knots.
