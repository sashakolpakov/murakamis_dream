# A finite real-algebraic certificate for the geometric volume branch

29 October 2026. The positive complete gluing certificate can be stated
without numerical logarithms, without a separate Jacobian hypothesis,
and without a restriction to alternating, pretzel, or bounded-bridge
diagrams. The existence of a positive chart is an actual hypothesis;
this note does not prove that every chosen triangulation has one.

This is a finite test for the GEOMETRIC side of the requested equality.
It does not infer the growth of an original quantum period merely from
its classical support. The source value/normal and absolute regulator
requirements in [the source audit](algebraic_source_geometry_criteria_audit.md)
still apply. In particular, the theorem below must not be counted as
an enlargement of the proved quantum-equality family.

## 1. Certificate and conclusion

Supply a finite oriented ideal triangulation T of the intended manifold
X, together with its actual marking. Check orientation-reversing face
pairings, circular edge links, and connected torus ideal-vertex links.
The identification with the intended knot/link exterior is an actual
oriented homeomorphism (or a verified sequence of elementary cellulation
moves proving it), carrying the relative fundamental class with degree
one and the displayed peripheral curves to the intended primitive
meridians and longitudes. A degree-one map alone is not this topological
identification. A different manifold or an unmarked cover is not
certified as X by its shape equations alone.

Write t for the number of tetrahedra and h for the number of cusp tori.
For every positively ordered tetrahedron specify

    z_j,  z'_j=1/(1-z_j),  z''_j=(z_j-1)/z_j.

The data to check are:

1. Im(z_j)>0 for every j. All three displayed shapes then have positive
   imaginary part and their arguments lie strictly between zero and pi.
2. The product of the incident shapes around every actual edge is 1,
   with the actual incidences and multiplicities.
3. The integer winding of that edge product is ONE, computed by the
   finite sign rule in section 2. Product 1 alone is insufficient.
4. The actual complex similarity multipliers of BOTH marked peripheral
   generators on every cusp are 1. These are Laurent monomials in the
   shape triples, with their actual signs and orientation conventions.

All denominators are kept nonzero by saturation with product z_j(1-z_j).
If shapes are supplied as algebraic numbers, every test above is exact
real-algebraic arithmetic. More generally the existence of such shapes
is a finite semialgebraic condition over Q: write z_j=x_j+i y_j, clear
denominators only on their specified nonzero locus, and retain the sign
conditions. The winding condition is a finite Boolean combination of
polynomial sign tests. No comparison of a numerically evaluated angle
with 2pi is part of this certificate.

**Geometric certificate theorem.** These data construct a complete
finite-volume hyperbolic metric on the ACTUAL manifold X. Its volume is

    Vol(X)=sum_j D(z_j),                                  (1)

where D is the Bloch--Wigner dilogarithm and the orientation is the one
already specified by the positive tetrahedra. This positive angle point
is the unique global maximizer of ideal tetrahedral volume on the closed
edge-angle polytope for T. Its complete shapes are algebraic over Q.
The marked meridian multipliers give algebraic etale local coordinates
on the gluing variety at this point.

The last two assertions are CONSEQUENCES of positivity and the actual
edge/peripheral incidence, rather than independent regularity assumptions.
The local statement does not assert that the global gluing variety has
one component or that its plane peripheral image is nonsingular.

## 2. Exact edge winding from algebraic signs

Let w_1,...,w_m be the incident shapes in cyclic order around one edge,
and set p_0=1, p_k=w_1...w_k. Under Im(w_k)>0 and p_m=1, define

    n=sum_(k=1)^m 1_{Im(p_(k-1))<0 and Im(p_k)>=0}.        (2)

Then

    sum_k Arg(w_k)=2pi n,   Arg(w_k) in (0,pi).            (3)

Proof. Follow the continuously increasing argument of the partial
product, adding Arg(w_k) at the kth step. Each step is strictly less
than pi. A passage from the open lower half-plane to the closed upper
half-plane therefore passes through, or ends on, the POSITIVE real ray.
It cannot go from that lower half-plane to the negative real ray in
one positive step shorter than pi. Conversely each crossing of a
positive multiple of 2pi has exactly the sign change in (2).
Starting on a real ray does not produce a spurious count: the positive
ray enters the upper half-plane, and the negative ray enters the lower
half-plane. Landing on the positive ray is counted once, while landing
on the negative ray is not. Thus real intermediate products cause no
ambiguity. The endpoint p_m=1 proves (3).

For example eight factors i have product 1 but n=2: the angle is 4pi.
Four factors i have n=1. Also let w=(3+4i)/5 and v=(-3+4i)/5. The list
(w,v,w,v) has exact rational complex coefficients, product 1 and n=1,
although its individual angles need not be rational multiples of pi.

Each p_k is rational in the algebraic shapes. Thus (2) is a finite
exact sign certificate for nonsingularity around an edge. No choice of
a logarithm branch is silently suppressed in passing to polynomials.

## 3. Why the metric is the metric of X

Realize each tetrahedron with its prescribed positive ideal shape.
The actual face identifications have unique ideal face isometries.
Away from edges they define an oriented hyperbolic metric. Around an
edge the shape product fixes the real dilation and the rotational
holonomy, while (2) fixes the total angle to exactly 2pi. The developed
link makes precisely one turn. Hence the local metric extends across
that edge without a cone singularity or a branched cover.

Cut the corners by small horospheres. Their triangles form a Euclidean
similarity structure on each topological cusp torus. Edge angle 2pi
removes its vertex cone singularities. The similarity multiplier is
trivial on a contractible loop and, by condition 4, on both generators
of the torus fundamental group. Propagate the scale of one triangle
across adjacent triangles: the trivial multiplier makes this propagation
independent of path. This produces a genuine flat metric on the entire
compact cusp torus.

A compact flat torus is complete. Its simply connected complete flat
cover develops isometrically onto the Euclidean plane, and its deck
group is a rank-two lattice of translations. In particular the two
translation periods cannot secretly vanish or be real-collinear; this
follows from the completed compact metric, not from an additional
numerical peripheral check. Simultaneously shrinking the finitely many
corner sections gives the usual embedded complete cusp ends. Their
volume is finite, and the complement of those ends is compact.

The resulting metric is therefore complete on X. The sum in (1) is
its actual tetrahedral volume; internal faces and edges have measure
zero. Completeness of the development identifies its universal cover
with hyperbolic space, so this is not merely a representation-volume
bound or a possibly branched local structure on X.
If X is already equipped with a complete finite-volume hyperbolic
metric, the sharp representation-volume bound applied in both identity-
marked directions identifies its volume with (1); this is the
bidirectional comparison in
[the general equality theorem](general_source_regulator_hyperbolic_equality.md).

## 4. Positivity forces the marked Jacobian to be invertible

Use local logarithms x_j=Log(z_j), y_j=Log(z''_j). Their derivative is

    dy_j=tau_j dx_j,  tau_j=1/(z_j-1),  Im(tau_j)<0.       (4)

Select t-h independent edge exponent rows and one primitive meridian
row per cusp. In these coordinates they give a real integer matrix

    R=(A B),  rank R=t,  A B^T=B A^T.                    (5)

These facts are properties of the ACTUAL ideal-manifold incidence.
For clarity, the needed finite incidence proof is the one in section 4
of [the positive ideal certificate](actual_pretzel_positive_ideal_angle_certificate.md):
an edge-row relation has local coefficients lambda_ab=c_a+c_b in each
tetrahedron; face matching propagates c_a to one constant per connected
ideal vertex link. There are h relations among t edge rows. The local
skew corner contributions cancel across paired faces, so edge rows are
isotropic. Peripheral normal-curve intersections give one nonzero
meridian/longitude pairing per torus and zero between different tori.
Thus the peripheral quotient has dimension 2h, and adding the h
meridians gives exactly the real Lagrangian system (5).

One may instead verify the displayed integer rank and symplectic
identities directly in a supplied certificate. This does not require
guessing the rank from a reduced source or from the number of equations.

The linearized edge-plus-meridian system is

    (A+B diag(tau))v=0.                                  (6)

Here is a direct proof that its kernel is zero. By (5), ker R is a
real Lagrangian subspace for Omega=sum dx_j wedge dy_j. If (6) holds,
w=(v,diag(tau)v) belongs to its complexification, as does bar(w).
Consequently

    0=Omega(bar(w),w)=2i sum_j Im(tau_j)|v_j|^2.

Every coefficient in the final sum is strictly negative, so v=0.
This proves the nonzero complex Jacobian without a numerical determinant.

The remaining edge equations are locally implied by the selected ones:
their exponent rows lie in the same rational span, and their logarithmic
constants agree at the specified point. Thus the full gluing germ is
smooth of dimension h, and the meridian map is locally etale. At the
complete rational values of the meridian multipliers, the shapes give
an isolated solution of a polynomial system over Q. An isolated complex
point of such a system has algebraic coordinates. Equivalently its
zero-dimensional component has finite residue field over Q.

This also explains the precise sense in which the local optimum is
algebraic over the peripheral parameters. After restricting to the
selected smooth branch and its denominators, its shapes are algebraic
functions of the meridian multipliers. Their marked longitudes are
algebraic functions on the same branch. This statement concerns the
shape germ; it does not make the regulator value an algebraic number.

## 5. The full Casson--Rivin maximum, not a restricted source maximum

Let theta be the positive angle point and let r=(Re x,Re y).
The real edge equations place r in the edge coisotropic subspace.
For EVERY edge-angle tangent delta, the sine rule in a tetrahedron gives

    dV(delta)=Omega(r,delta)
      =(1/2)sum_i[Re V_i delta Im U_i-Re U_i delta Im V_i]. (7)

The quotient identity in (7) is exactly the actual peripheral pairing
from (5). At the complete point both real peripheral logs vanish, so
the derivative vanishes on the full edge-angle tangent space. No
surjectivity of a quantum-source parametrization is being assumed.

For one tetrahedron, use independent angles alpha,gamma with
beta=pi-alpha-gamma. The negative volume Hessian is

    [[cot alpha+cot beta, cot beta],
     [cot beta, cot gamma+cot beta]].

Its determinant is 1, and its first diagonal entry is
sin(gamma)/(sin(alpha)sin(beta))>0. It is positive definite. The sum
over tetrahedra is therefore strictly concave on every affine angle
slice. On a segment from the complete point to any other point of the
closed angle polytope, the derivative starts at zero and strictly
decreases for every positive segment parameter less than one.
Continuity at the final zero/pi angles gives a strictly smaller value
at the other endpoint as well. This proves the unique GLOBAL maximum.

It also proves uniqueness of the COMPLETE POSITIVE SHAPE ASSIGNMENT
on this fixed marked triangulation. Any two certified assignments would
both be stationary maxima on the same edge-angle polytope, and hence
have identical angles. The positive ideal angles determine the complex
shape by the sine rule, so their shapes coincide. Thus the finite
semialgebraic existence test, when successful, selects one positive
complete point and its geometric meridian germ. It makes no uniqueness
assertion for other complex or nonpositive components of the gluing
ideal or for the original quantum solution space.

The corresponding filled-slope assertion needs the actual primitive
logarithmic filling periods, in addition to its exponential equations.
It is treated in [the general geometric completion](general_source_regulator_hyperbolic_equality.md).
The complete-cusp test above does not silently replace that tube-end
condition by an equation modulo 2pi i.

## 6. A simple sufficient test on the plane A-curve

There is also a useful algebraic branch test at a signed complete point
(M_0,L_0). Put u=M/M_0-1, v=L/L_0-1. For a reduced relevant peripheral
factor write its local equation as

    A(u,v)=H_m(u,v)+terms of total degree greater than m,

where H_m is its first nonzero homogeneous part. If

    H_m(1,tau)=0,   partial_t H_m(1,tau) != 0,             (8)

substitute v=u t and divide by u^m. The strict-transform equation is
H_m(1,t)+u R(u,t)=0. The implicit function theorem gives a unique
algebraic analytic branch t=t(u) through tau, and hence v=u t(u).
This branch is unramified over u, even if the original plane curve is
singular and partial_L A vanishes at the complete point.

A positive imaginary part of tau, in the correctly oriented primitive
peripheral basis, selects a candidate geometric tangent. The actual
positive marked gluing lift above is what certifies it as geometric.
Condition (8) is sufficient, not necessary: coincident tangent lines
may require further blowups, and a plane image may lose distinctions
between smooth decorated branches.

Neither (8) nor a nonsingular gluing scheme reconstructs the absolute
Bloch class or the original normal quantum evaluation. In particular
f_N(Y)=(1-Y)F_N(Y) has the same localized classical support as F_N,
but f_N(1)=0 whereas -f'_N(1)=F_N(1) is the original invariant. The
integral pointed source and its specified jet must accompany the curve.

## 7. Coverage and what remains on the critical path

The classical implications are established territory: the coverage
check found Choi's 2004 *Positively oriented ideal triangulations on
hyperbolic three-manifolds* (Topology 43, 1345--1371,
https://doi.org/10.1016/j.top.2004.02.002), whose statement includes smooth
positive gluing varieties and local peripheral coordinates, and
[Futer--Gueritaud's Casson--Rivin exposition](https://arxiv.org/abs/1004.0440).
They are recorded for coverage; the proofs used above are displayed
directly or refer to the independently checked incidence calculation.
The exact sign test exposes the integer winding that a saturated
exponentiated gluing ideal alone forgets. No novelty claim for the
underlying rigidity or variational theorem is intended.

This certificate applies at arbitrary bridge number whenever its actual
positive ideal chart is supplied. Alternatingness is not a premise.
Fully augmented links with more general graphs and their independently
long fillings remain a broad target, but their actual original-source
packet and complementary-source estimates are additional work.

There is now an exact pointed crossing alphabet and actual parabolic
character gluing for [every four-plat word](actual_newton_twist_canonical_graph.md).
There is also a sharp complete-source norm estimate for
[the two-twist packet](actual_newton_two_twist_interaction_packet.md),
using an exact reset, a reflected boundary current and an independently
evaluated nonzero opposite endpoint. Those are genuine source data
beyond simple-spectrum or smooth-curve assumptions. Extending that
estimate to arbitrary reduced words, and controlling the corresponding
original marked closure, remains the quantum critical path.

Independent analytical review passed the written winding, cusp,
polarized-Jacobian, algebraicity and full-angle arguments. The
[exact winding audit](../experiments/audit_finite_real_algebraic_geometric_certificate.py)
checks all eight edges of the actual reflected two-octahedron base
in 284 exact shape orders, positive/negative real intermediate
products, and rejection of product-one lists of winding two or three.
These finite checks supplement the general proof; they do not prove
the existence of positive charts or quantum asymptotics in general.
