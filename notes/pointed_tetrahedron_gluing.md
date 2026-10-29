# Pointed tetrahedron modules and all-level edge reduction

Research note, 26 October 2026. This constructs strict shape-ordering
maps, including explicit pointed root intertwiners, and proves integral
edge-lattice primitivity for link exteriors in S^3. It extends the
earlier odd-level edge reduction to every N. In particular a positive
geometric triangulation of a hyperbolic knot supplies a nonzero
rank-N quantum boundary block at every level on the stated central
cover, without a global branching assumption for this module construction.

The projected tensor generator is specified, but its nonvanishing,
its identification with the actual relative ADO source, and its
marked Bloch-regulator norm are not proved. Shape-module order
changes are not automatically tensor-face adapters for the full
[Verma period](verma_tetrahedral_transport.md). The marked
peripheral lattice at even N requires a separate distinction in
Section 7.

## 1. A pointed shape module and its strict order changes

For local parameter R use the quantum Laurent algebra

    A_R=<X^(+/-1),Y^(+/-1): XY=R YX>,
    D_R=A_R/A_R L, L=X+Y-1,

with distinguished generator [1]. For an oriented tetrahedron
R=Q^(-epsilon), epsilon=+/-1. Its shape triad is

    Z_0=X, Z_1=Y^(-1), Z_2=-X^(-1)Y,
    Z_0 Z_1 Z_2=-R^(-1).

The cyclic ordering map and reflection are

    rho(X)=Y^(-1), rho(Y)=-Y^(-1)X,
    sigma(X)=Y, sigma(Y)=X, sigma(R)=R^(-1).        (1.1)

Reflection is understood either semilinearly in the local parameter
or as a linear map to the oppositely oriented algebra. Exact
noncommutative substitution gives

    rho^3=1, sigma^2=1, sigma rho sigma=rho^(-1),
    rho(L)=-Y^(-1)L, sigma(L)=L.                  (1.2)

The unit in rho(L) is on the left. Thus these maps preserve the
correct left ideal and give actual pointed module maps, with
[1] sent to [1]. Their coherence is exact rather than projective.
The ordinary S_4 action on the six cross-ratios factors through
this S_3. This supplies shape-module changes under local vertex
orderings. It does not assert that the Klein-four action on face
tensor legs has been constructed merely because it is trivial
on shape coordinates.

The module is related directly to the compact tetrahedral operator.
If psi(a)=P_Q(a)^(-1), then psi(Qa)=(1-a)psi(a). Multiplication
by a and the shift a->Qa give X+Y-1 on this generator, with
parameter R=Q^(-1). Multiplying by the exact monomial shear in
the preceding note transports this relation to its tetrahedral
kernel module. This is an algebraic statement about the local
functional module, not a termwise root evaluation of psi.

## 2. Explicit pointed root intertwiners

Let R=r^2 have order N, with r^N=-1. On the nondegenerate shape
cover choose s,t satisfying

    s^N+t^N=1, st!=0.

Use the clock/shift representation

    X e_a=s R^a e_a, Y e_a=t e_(a+1 mod N).

It is the full matrix algebra. The kernel of L is one-dimensional:
normalize p_0=1 and use

    p_a/p_(a-1)=t/(1-sR^a), 1<=a<N.              (2.1)

The last cyclic equation is exactly s^N+t^N=1. All components
are nonzero. The left-ideal quotient D_R at this center is an
N-dimensional simple module: a matrix L of rank N-1 gives a
left-ideal quotient of dimension N, and a[1]->a p identifies it
with this representation.

The root cover itself has exact order changes

    rho:(s,t,r)->(t^(-1),r s/t,r),
    sigma:(s,t,r)->(t,s,r^(-1)).                  (2.2)

They obey the same S_3 relations. The factor r in rho is required:
its N-th power gives the minus sign in 1-t^(-N)=-s^N/t^N.

There is an explicit canonical matrix adapter. For rho use
(A,B)=(Y^(-1),-Y^(-1)X); for sigma use (A,B)=(Y,X). Let (s',t',r')
be (2.2), and let p' be (2.1) at that target. Put

    P_0=(1/N)sum_(j=0)^(N-1)(A/s')^j,
    v=P_0 e_0,
    J e_a=(B/t')^a v.

The spectral projector and cyclic arrows show that J is invertible
and intertwines both clock/shift generators. Its kernel image
Jp' is a nonzero multiple of p. Divide J by its zeroth component
to impose

    Jp'=p.                                      (2.3)

This fixes its entire scalar. The module relations (1.2) imply
that a composition for an S_3 relation commutes with the full
matrix algebra; (2.3) makes that scalar one. Thus cyclic rotation
three times, reflection twice, and the braid relation have exact
pointed coherence at every N, including even and composite N.
No determinant-normalized or unitary metric assertion is needed.

The subsequent [Regge/cover calculation](regge_period_covers_and_a_curves.md#the-quantum-ordering-maps-are-explicit-gaussians)
now writes these same adapters as explicit Gaussian Fourier
matrices divided by their actual pointing scalar. It retains
the quadratic Gauss phase in the unpointed order-three cycle,
and gives the scalar's exact Hermitian norm as a ratio of
the two kernel norms. This solves the finite ordering part;
it is not a full face-tensor S_4 or global selected-state theorem.

## 3. The integral edge lattice, without a branching

Let K be a connected oriented triangulated 3-dimensional
pseudomanifold whose vertex links are closed orientable surfaces;
this includes an ideal triangulation of a cusped manifold and
ordinary finite vertices with sphere links. Let T,E,V denote
the numbers of tetrahedra, global edges and vertices. Write

    Lambda=direct-sum_j Z^2,
    Omega=direct-sum_j epsilon_j [[0,1],[-1,0]].

In tetrahedron j the opposite pairs are (01,23), (02,13), (03,12).
For a global edge e let a_e,b_e,c_e be its incidence counts in
these pairs. Its vector in Lambda is

    beta(e)_j=epsilon_j(a_e-c_e,b_e-c_e).

Let E_ed=im beta. This definition uses arbitrary local vertex
orders and their orientation signs, not a global branching.
The sign gives the physical edge equation when an odd local
reordering inverts the corresponding ordered shape. Omitting it
from the incidence calculation gives an integrally symplectically
isomorphic lattice, by multiplication of that tetrahedron block
by -1, so the rank and saturation statements are the same.

Isotropy has a direct face proof. Assign values lambda and mu
to global edges, and form the local opposite-pair sums a,b,c
and u,v,w. After factoring out epsilon_j, their local symplectic
contribution is

    (a-c)(v-w)-(b-c)(u-w).

For three ordered edge values put
omega(l,m)=sum_cyclic(l_i m_(i+1)-l_(i+1)m_i). The displayed
contribution is exactly minus the alternating sum of omega
over the four ordered faces. Each pair of nonopposite edges
occurs on its unique face, which verifies the formula termwise.
The face expressions cancel under the orientation-reversing
face identifications. Therefore

    Omega(E_ed,E_ed)=0.                           (3.1)

This argument is unaffected by arbitrary local reordering, because
both the face orientation and the three-edge alternating form
transform by the same permutation sign.

## 4. Exact saturation and the missing prime 2

Put h=dim H^1(K;F_2). The nonzero Smith entries of beta are

    1 repeated E-V-h times, 2 repeated h times.    (4.1)

Here is an independent proof.

Over any field of odd characteristic, a row dependence says
a=b=c in each tetrahedron. These equations are equivalent to
lambda_ij=t_i+t_j. The local t's are uniquely recovered from
the three edge values of a face by division by 2. They therefore
descend to one t at every global vertex. The vertex-sum map is
injective, since a triangle's three zero endpoint sums force
all its t's to vanish. Hence rank beta=E-V in every odd
characteristic, as well as over Q.

In characteristic two, a=b=c is instead equivalent to the four
triangle sums being equal. Face pairing makes their common
value one global constant sigma. Subtract sigma times the
constant edge assignment. The result is exactly a simplicial
1-cocycle on K. Conversely every such cocycle and every sigma
give a dependence. The constant assignment has triangle sum
one and is independent of the cocycles. Thus

    dim ker(beta mod 2)=1+dim Z^1(K;F_2)=V+h.       (4.2)

It remains to exclude Smith factors 4,8,..., not merely odd
factors. Work with a dependence lambda valued in Q/Z. Locally
one can solve lambda_ij=t_i+t_j, since multiplication by 2 is
surjective on Q/Z. Two choices on a paired face differ by the
same element of order at most 2 at its three vertices. Therefore
2t descends to global vertex values u, and 2lambda_ij=u_i+u_j.
This is the reduction of a rational vertex-sum dependence.

By Smith normal form, the quotient of Q/Z-valued dependences
by reductions of rational dependences is the dual of the torsion
in Lambda/E_ed. The preceding calculation kills it by 2.
All nonzero Smith entries therefore equal 1 or 2; (4.2) counts
exactly h entries equal to 2. This proves (4.1).

For an exterior of a link in S^3, H^1(K;F_2)=0. Attach cones
to each boundary component to obtain K; finite sphere vertices
do not affect H_1. The cone Mayer--Vietoris sequence identifies
H_1(K) with the cokernel of H_1(boundary M)->H_1(M).
The meridians generate H_1(M)=Z^c for a c-component link, so
this cokernel vanishes, including over F_2. Consequently

    E_ed is primitive in Lambda for S^3 link exteriors.        (4.3)

For a knot all edge-row dependences are constants, and the sum
of all edge rows is zero integrally. Deleting any one edge row
therefore gives an integral basis of E_ed, with no index hidden
at 2. Equation (4.3) strengthens the odd-level argument in
the [earlier Heisenberg reduction](heisenberg_period_torsor.md).

## 5. Edge reduction at every root level

Fix nondegenerate tetrahedral central shapes satisfying the
classical edge equations, and choose the recorded central-root
cover. The tensor product of the root tetrahedron modules is
a split irreducible quantum-torus module W of dimension N^T.
This follows directly from their clock/shift matrix units.

Use lambda^2=Q, lambda^N=(-1)^(N-1), for example lambda=-q_N.
Use A_j=Z_(0,j), B_j=Z_(1,j), so A_j B_j=Q^epsilon_j B_j A_j.
These are the first two triad variables, rather than the original
X,Y pair of Section 1. For integer vectors v=(a,b) the Weyl
convention is

    W(v)=lambda^(-sum epsilon_j a_j b_j) A^a B^b.

It has the exact multiplication with factor lambda^Omega and
its N-th power is precisely its classical central monomial.
These statements include all even-level signs. Shape identities
such as Z_0 Z_1 Z_2=-Q^epsilon and their induced edge units
are part of the specified characters, not discarded constants.

Choose a basis e_1,...,e_r of the primitive isotropic E_ed and
specified commuting edge characters c_i with
c_i^N=W(e_i)^N. All dependencies and their units must be matched.
Such characters have an explicit realization on the central-root
cover: if s_j,t_j are the roots of X_j^N,Y_j^N in Section 2,
then eta(e)=product_j s_j^(a_j)t_j^(-b_j) is a multiplicative
root character for W(e). A different compatible prescribed lift
differs by a mu_N-valued character. This labels the lifts; it
does not select the actual ADO source lift by nonvanishing.
Then U_i=c_i^(-1)W(e_i) commute and U_i^N=1. The exact projector is

    Pi_chi=product_i (1/N)sum_(a=0)^(N-1)chi_i^(-a)U_i^a,
    chi_i in mu_N.                               (5.1)

Every nonidentity term has zero trace: primitivity implies that
a nonzero linear combination of the e_i modulo N is nonzero
in Lambda/N Lambda, and noncentral clock/shift monomials have
zero trace. Therefore

    rank Pi_chi=N^(T-r)                           (5.2)

for every compatible prescribed character and every N>=2.
The coinvariant quotient is canonically the image of Pi_chi.
This supplies nonzero reductions at all levels; it does not
permit choosing a character to force the desired period.

The saturated lattice B=E_ed^perp/E_ed is free and unimodular
symplectic. One can extend E_ed to an integral symplectic basis:
choose a primitive e, solve Omega(e,f)=1 by Bezout, split off
that pair and continue. Its remaining pairs act on im Pi_chi.
The N-th-power central characters are retained on the same root
cover. Their nonidentity Weyl operators have zero trace on the
reduced space, by inserting (5.1) in the full trace. The resulting
N^(2(T-r)) trace-orthogonal matrices span its entire endomorphism
algebra. This proves irreducibility for the saturated boundary
algebra, with no inversion of 2 modulo N.

For a torus-cusped link exterior, Euler characteristic gives
T-r=c. The module has dimension N^c; for a knot it has dimension
N. The assertion remains valid with finite sphere vertices,
since their genus contribution is zero.

## 6. The gluing vector and its ordering compatibility

Let p_j be the specified tetrahedron generator in its splitting
frame. The reduction has a specified candidate vector

    s_(T,N,chi)=Pi_chi(p_1 tensor ... tensor p_T). (6.1)

The later [factorial source-torsor theorem](factorial_source_torsor.md)
identifies this local tetrahedron kernel, after reversing its
index, with the pointed cyclic dilogarithm phi_a. The actual
factorial boundary is p_a=nu^a phi_a, nu^N=1-h^N; this is a
singular frame at the Kashaev wall h=1. Its full affine source
and cut-root adapters are explicit. This supplies local relative
data; it does not identify the nondegenerate geometric root
fiber with that degenerate actual boundary fiber.

This is the root block of the usual left/right quantum gluing
quotient: first impose the tetrahedron left ideals, then the
edge coinvariants. A centralizer of the edge action, including
the saturated boundary algebra, acts on it.

The pointed order-change maps of Sections 1--2 intertwine the
whole edge operators and their transported characters. Hence
they intertwine (5.1), carry (6.1) to its corresponding vector,
and obey the same exact cocycle relations. This proves local
shape-order independence of the module and its projected vector.
A global branching is unnecessary for this module construction.

The vector (6.1) can still be zero even though the reduction has
the nonzero rank (5.2). The trace of a projector does not prove
that it is nonzero on a particular tensor. Nor has this candidate
gluing vector been identified with the selected relative Verma
trace or actual ADO source. In particular the root tetrahedron
module was obtained by its algebraic relation, not by evaluating
the four singular compact factors separately.

## 7. The marked peripheral lattice and its integral half-longitude

For a knot the saturated boundary lattice B is unimodular of
rank two. The earlier audited unhalved meridian/longitude rows
have symplectic pairing -2. Whenever these are the chosen marked
vectors, their span has index two in B. This is a peripheral
index; it does not contradict the primitivity of the edge lattice.

The subsequent [integral half-longitude proof](integral_half_longitude.md)
identifies the missing half using the knot marking itself:

    B=Z delta(mu) + Z ell,  ell=delta(lambda)/2,
    Omega(delta(mu),ell)=-1.

A mod-two dual-face cochain proves that delta(lambda) pairs
evenly with every balanced integral vector, because the preferred
longitude is nullhomologous in the exterior. Unimodularity gives
the unique half in B. An explicit edge correction constructs its
integer representative before specializing N.

Thus the unhalved algebra is generated by Y,T^2 inside the
saturated algebra generated by Y,T, with TY=q^2 YT. At odd N
these give the same finite Weyl algebra. At even N the unhalved
algebra has two sectors distinguished by Y^(N/2), each of
dimension N/2 after central normalization, and T exchanges them.
The scalar lift satisfies T^2=Lambda_hat only after the full
edge character and the specified square root are retained.
In particular changing T to -T at even N does not change T^N.
The actual central longitude and source pointing must still
be matched. The [even-meridian ADO normalization](even_meridian_norm_descent.md)
records its separate full-state sign character; no arbitrary
choice of a sector or square-root sign identifies the states.

If h in (4.1) is nonzero for a different manifold, the edge
lattice itself can also be nonprimitive. Already E=<2f> has
compatible reductions of dimension gcd(2,N) and vanishing reductions
for incompatible even-level characters. Lens-space examples
verify this distinction in the audit. The S^3-link hypothesis
in (4.3) is doing actual work.

## 8. Consequence for the ideal-triangulation route

The audited positive triangulation theorem supplies nondegenerate
classical shapes for every hyperbolic knot. Sections 1--6 then
supply order-compatible pointed tetrahedron modules and a nonzero
rank-N geometric boundary block at every level on the specified
cover, without a global branching requirement for this reduction.
This upgrades the earlier local central-support calculation to
an actual nonzero geometric quantum module.

Placing that block in the actual affine meridian source extension,
matching its projected vector and boundary functional to the
relative Verma period, and identifying the marked Bloch-regulator
norm are still necessary. The marked peripheral scalar lift
in Section 7 must be transported explicitly. No geometric
factor of the minimal actual A-operator or noncancellation in
the selected period follows from module rank alone.

## 9. Coverage and independent diagnostics

The integral edge complex and its 2-primary phenomena belong
to Neumann's existing triangulation framework; see the statement
coverage in
[Combinatorics of triangulations and the Chern--Simons invariant](https://www.math.columbia.edu/department/neumann/preprints/cspaper.pdf).
No integral exactness proof from it is used above. The elementary
face pairing, endpoint-potential and Q/Z arguments prove the
needed lattice statements here.

The abstracts of
[Garoufalidis--Yu, 2403.12424](https://arxiv.org/abs/2403.12424)
and [Panitch--Park, 2403.12850](https://arxiv.org/abs/2403.12850)
cover quantum gluing quotients and quantum trace maps. Their
comparison, move and state-identification proofs are not premises.
No novelty claim is made for the general quantum gluing framework.
The point here is the explicit ordering/root phases and the
all-level reduction with the remaining selected-period issue
kept separate.

[The audit](../experiments/audit_pointed_tetrahedron_gluing.py)
checks the abstract pointed S_3 maps, finite root adapters in
both orientation parameters, the six-edge face identity, exact
edge Smith forms and mod-2 cohomology with arbitrary tetrahedron
relabelings, and finite projectors including even N. Closed
nonprimitive examples and index-two peripheral sectors are
included as scope checks. The
[results](../experiments/pointed_tetrahedron_gluing_results.json)
support the uniform proofs; no volume asymptotic is inferred.

The saved full audit has 49 abstract Laurent checks, 18 pointed
root-adapter cases through level 12 in both orientation parameters,
45 exact incidence/Smith/cohomology checks including arbitrary
tetrahedron relabelings and nonprimitive closed examples, and 11
edge-projector checks. The figure-eight projector checks include
the full saturated boundary trace basis at every listed level;
the Whitehead-link checks have the predicted N^2 dimensions.
Nine parity tests retain incompatible nonprimitive characters
and the two marked peripheral sectors at even N.

The full reproduction command in this workspace is

    PYTHONPATH=.venv/lib/python3.14/site-packages python3 experiments/audit_pointed_tetrahedron_gluing.py --regina
