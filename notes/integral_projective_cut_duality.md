# The entire integral knot centralizer is self-dual under its actual cut

Research note, 26 October 2026. This extends the local two-factor
residue pairing to every tensor power at the Kashaev color. The proof
constructs a symmetric PBW coefficient form, realizes the actual
complete-color module as a projective summand, and calibrates the
induced trace to the original ADO dimension. It does not invoke a
published modified-trace or projectivity theorem.

The result controls the full integral centralizer, not just a chosen
fusion algebra. It also proves that every complete-color E,F,K
intertwiner lifts through the actual meridian deformation. The
geometric quantum-A source and its selected regulator norm remain
unidentified; this is no volume-conjecture proof.

## 1. Statement with the original cut and phase

Fix N>=2, q=exp(pi*i/N), Q=q^2, rho=q-q^(-1). Put

    R=C[[u]], M=exp(u), x=-M/q,
    k_x=x^N=(-1)^(N+1)M^N,
    W_b=V_x^(tensor b).

Use the original matrices, coproduct and pivot from
[the intrinsic cut calculation](intrinsic_cut_and_meridian_atlas.md):

    Delta E=E tensor K+1 tensor E,
    Delta F=F tensor 1+K^(-1) tensor F,
    g=K^(1-N).

Every centralizer below means commutation with these actual total
E,F,K matrices. Let

    C_(b,R)=End_(E,F,K;R)(W_b),
    t_b(A)=Tr((P_0 tensor g^(tensor(b-1)))A),
    mathfrak_t_b(A)=d_N(M)t_b(A),
    d_N(M)=eta_N(M-M^(-1))/(M^N-M^(-N)),
    eta_N=(-1)^(N+1)q^(N(1-N)/2)=i^(N+3).           (1.1)

The whole value d_N(1)=eta_N/N is a unit of R. The zero-framing
factor remains theta_x^(-writhe) in the braid operator being traced.

For every b>=1, C_(b,R) is a finite free symmetric R-algebra with
perfect pairing

    (A,B) -> mathfrak_t_b(AB).                      (1.2)

Its full cut dual is exactly itself. For b>=2 its rank is
N^(2b-3); at b=1 it is R. In addition,

    C_(b,R)/u C_(b,R)
      =End_(E,F,K;C)(V_(-q^(-1))^(tensor b)).       (1.3)

Thus the pairing remains perfect on the entire complete-color
centralizer, including its nonreduced parts. No higher-tensor
matrix-algebra description over the confluent center is asserted.

## 2. A finite PBW algebra over a varying central character

For any unit k in R define

    H_k=R<E,F,K,K^(-1)>/
      (K E=Q E K, K F=Q^(-1)F K,
       E F-F E=(K-K^(-1))/rho,
       E^N=F^N=0, K^N=k).                          (2.1)

It has R-basis

    F^a K^b E^c, 0<=a,b,c<N.                       (2.2)

Here is a direct normal-form justification. Order F before K before
E, reduce K powers modulo N with their full k factors, and use

    E F^a=F^a E+[a]F^(a-1)
                    (q^(1-a)K-q^(a-1)K^(-1))/rho. (2.3)

The only additional boundary ambiguities are commutations with
K^N, E^N or F^N. K^N commutes because Q^N=1; the extra term in
(2.3) vanishes for a=N because [N]=0. The corresponding formula
for E^N F has the same property. The ordinary K E F ambiguity
reduces to the same (K-K^(-1))/rho on both paths. Disjoint and
power-overlap reductions agree. These rules are terminating and
resolve the critical overlaps, proving (2.2).

Define one PBW coefficient functional, with no unknown scalar:

    mu_k(F^a K^b E^c)=delta_(a,N-1)delta_(b,0)delta_(c,N-1). (2.4)

This is symmetric. For E, the lower term in (2.3) cannot contribute
to (2.4), since it lowers the F exponent. The leading commutation
with K^b contributes Q^(-b), which equals one whenever (2.4)
is nonzero. The F calculation is the same with E and F exchanged.
Commuting K gives identical factors when a=c=N-1. Thus
mu_k(g h)=mu_k(h g) for g=E,F,K and every h, hence for every
pair of algebra elements.

Its pairing is perfect over R. Filter by total E,F degree. In the
associated graded algebra E and F commute and K retains the two
inverse Q actions. Every basis monomial has a unique complementary
pair of E,F exponents and a complementary K power that gives the
coefficient (2.4), with a unit Q and k multiplier. This is a perfect
graded pairing. Products of total degree below 2N-2 contribute
zero to mu, so the ungraded pairing matrix is block triangular
after ordering by complementary degrees. Its diagonal blocks are
these invertible graded pairings. This proves perfection in R.

## 3. The simple complete color is an actual projective summand

Use the central Casimir

    Omega=rho^2 F E+q K+q^(-1)K^(-1).

Successive commutation gives the exact identity

    rho^(2N) F^N E^N
      =product_(j=0)^(N-1)(Omega-q^(2j+1)K-q^(-2j-1)K^(-1)).

The product is T_N(Omega)+K^N+K^(-N), where
T_0=2,T_1=z,T_(j+1)=z T_j-T_(j-1). Therefore H_k satisfies

    P_k(Omega)=0, P_k(z)=T_N(z)+k+k^(-1).           (3.1)

For k=k_x, the actual highest-root branch is

    c_x=q x+q^(-1)x^(-1)=-M-M^(-1).

At M=1 it equals -2 and

    P_(k_x)'(c_x)|_(M=1)=(-1)^(N+1)N^2,            (3.2)

which is nonzero for all N. Other roots are distinct from this
one at that point. Consequently the following actual polynomial
is a central idempotent over R:

    e_St=(P_(k_x)(Omega)/(Omega-c_x))/P_(k_x)'(c_x). (3.3)

The quotient denotes polynomial division before evaluation. All
its coefficients belong to R; there is no inverse of a vanishing
Casimir difference in (3.3).

The K-root projectors on this block are

    pi_a=(1/N)sum_(r=0)^(N-1)(K/(x Q^(-a)))^r,
    0<=a<N.

On e_St H_(k_x), the relations FE and EF on adjacent weight
spaces have scalars e_a(x) and e_(a+1)(x), respectively. Each
e_a(x), 0<a<N, is a unit at M=1. Thus every interior E,F edge
is invertible up to that unit. The remaining boundary F edge
is zero because F^N=0 and all other edges are invertible;
E^N=0 kills the boundary E edge in the same way. This leaves
one length-N chain and its full matrix units. In particular

    e_St H_(k_x)=Mat_N(R).

The primitive idempotent e=e_St pi_0 has left ideal H_(k_x)e
free of rank N over R. The basis F^a e identifies it with the
original V_x: F has coefficient one, K has root x Q^(-a), and
E has exactly e_a(x). It is a direct summand of H_(k_x), hence
is projective over that algebra. This is an explicit projective
realization of the actual complete-color deformation.

## 4. Tensoring preserves this projectivity

Before fixing K^N, the nilpotent algebra is a Hopf algebra.
Its central group-like K^N gives coproducts

    Delta_(k,l):H_(kl)->H_k tensor H_l,
    S:H_(l^(-1))->H_l.

The primitive-root binomial identity ensures E^N=F^N=0 is
respected. If W is an H_l-module free over R, the explicit map

    Phi:H_(kl) tensor_R W -> H_k tensor_R W,
    h tensor w -> sum h_(1) tensor h_(2)w           (4.1)

intertwines the free action on the first domain factor with
the diagonal action on the target. Its inverse is

    a tensor w -> sum a_(1) tensor S(a_(2))w,
    Delta_(kl,l^(-1))(a)=sum a_(1) tensor a_(2).   (4.2)

These are the two usual multiplication/antipode identities,
checked before central reduction. They descend because K^N
has character kl on the domain and character k times l on
the target, while the inverse uses kl times l^(-1)=k.
The nilpotent powers descend as well. Thus H_k tensor W is
a free H_(kl)-module of rank dim_R W.

A projective H_k-module is a direct summand of a finite free
one. Tensoring its inclusion and retraction with W, and using
(4.1), proves it remains projective over H_(kl). Starting with
Section 3 proves W_b is projective over H_(k_x^b) for every b.

## 5. Calibrating the symmetric trace to the full ADO cut

Write F=Frac(R). When k^2!=1 in F, as for k=k_x^b, H_k over F
is the direct product of N full N-by-N matrix algebras. This follows from the same
weight-chain construction in Section 3 applied to all distinct
roots c_j=q z_j+q^(-1)z_j^(-1), z_j^N=k. On each root, the
interior e_a(z_j) are nonzero and the boundary edges vanish.

On each simple module pi_x has ordinary trace one. Direct PBW
degree counting gives

    mu_k(pi_x Omega^m)=0, 0<=m<N-1,
    mu_k(pi_x Omega^(N-1))=rho^(2N-2)/N.

The last equality uses the leading term
rho^(2N-2)F^(N-1)E^(N-1); only the zeroth K coefficient of
pi_x contributes to (2.4). Lagrange interpolation therefore
shows that mu_k has the simple-block weight

    w_j=rho^(2N-2)/(N P_k'(c_j)).

Use the exact, k-independent factor

    gamma_N=N^2 q^(N(1-N)/2)/rho^(2N-2).           (5.1)

Differentiating T_N(t+t^(-1))=t^N+t^(-N) gives

    gamma_N w_j=N q^(N(1-N)/2)/P_k'(c_j)
               =-q^(N(1-N)/2)
                  (q z_j-q^(-1)z_j^(-1))/(z_j^N-z_j^(-N))
               =d_(z_j).                         (5.2)

These are exactly the original ADO dimensions from the intrinsic
cut proof. No phase or finite numerical multiplier is adjusted.
In particular gamma_N mu_(k_x)(e)=d_N(M), including its regular
complete value eta_N/N.

## 6. From the PBW form to every integral centralizer

For a symmetric finite free R-algebra (H,mu) and a finite
projective left H-module P, choose a splitting P -> H^m -> P.
On End_H(P), define the trace by applying mu to the diagonal
of its corresponding endomorphism of H^m and summing.

This is independent of the splitting: if A and B are the two
rectangular matrices comparing two splittings, the required
identity is sum mu((AB)_(ii))=sum mu((BA)_(jj)), which follows
termwise from mu(ab)=mu(ba). It is cyclic for the same reason.

It is perfect. In an idempotent presentation it is the restriction
of the matrix trace pairing to e Mat_m(H^op)e. For any X in that
corner, cyclicity gives t(XY)=t(X eYe) for every Y. Since the
whole matrix pairing is perfect and the corner is a direct
R-summand, every functional on the corner extends by projection
Y->eYe and is represented uniquely by an element of the corner.
This proves the corner pairing is perfect, over R itself.

Apply this construction to H_(k_x^b), W_b and gamma_N mu.
Over F its formula is sum_j d_(z_j)Tr(A_j), by (5.2).
The [intrinsic cut proof](intrinsic_cut_and_meridian_atlas.md)
independently identifies exactly that expression with the actual
d_N(M)t_b. The latter is R-valued because the actual matrices,
pivot and whole d_N(M) are integral at M=1. The two linear
functionals agree over F, hence agree on the entire integral
centralizer. The corner argument proves (1.2).

The same idempotent presentation commutes with R->R/(u), so
End_H(W_b) has exactly the base change (1.3). In particular no
additional complete-color intertwiner needs a separate lifting
assumption. The generic multiplicity formula from the intrinsic
cut proof gives rank N^(2b-3) for b>=2. This completes the theorem.

## 7. The integral gauge torsor and a comparison criterion

An integral H_k-linear idempotent p on W_b gives another
projective module pW_b. Its endomorphism order is p C_(b,R) p,
and its inherited cut pairing is perfect by the same corner
argument. In particular, regular commuting finite-order edge
operators that commute with H_k can be reduced by their exact
averaging projector without losing cut duality. Their character
roots and all scalar factors remain part of that projector.
For geometric edge gluing, this H_k-linearity and regularity
must be proved in the actual relative source realization; the
abstract quantum-torus edge-rank theorem does not supply them.

There is a local constraint on such a construction. On just two
generic colors the full H_k centralizer is commutative, by the
multiplicity-one decomposition. It cannot contain an invertible
Weyl pair X,Y with XY=QYX and Q!=1: commutativity would imply
(1-Q)YX=0. Thus the geometric clock and shift on an individual
relative face cannot both be treated as H_k-linear operators on
that two-color module. The full edge products and their retained
source terms are the objects whose H_k-linearity must be checked.

The integral comparison group is now specified:

    G_(b,R)=C_(b,R)^times.                         (7.1)

Because C_(b,R) is finite free, its units form the principal open
set where left multiplication has invertible determinant. Thus
this is a smooth affine R-group. Nilpotent ideals in the special-fiber
algebra are retained through their unipotent units. An automorphism of the complete
fiber lifts directly: lift its centralizer element using (1.3);
its determinant on W_b has a nonzero constant term, so the lift
is invertible. Cyclicity preserves the actual cut under its
inner action. This is an integral version of the generic product
of general linear groups, retaining the special-fiber algebra and
its nilpotent ideals.

More generally, if P and Q are finite projective H_k-modules and
an isomorphism P/uP -> Q/uQ is supplied, projectivity makes
Hom_(H_k)(P,Q) commute with base change. Lift that isomorphism;
its determinant is a unit, so it is an isomorphism over R.
This is formal local rigidity with specified common H_k data.
It does not supply the common module, an algebraic comparison
over the whole A-curve, or a selected period section.

Let C and D be full R-orders in the same finite-dimensional
F-algebra, equipped with the same symmetric F-linear trace t.
Suppose both are self-dual for t. Then

    C subset D implies C=D.                       (7.2)

Indeed dualizing the inclusion gives D^vee subset C^vee, or
D subset C. The reverse inclusion was the hypothesis. This
requires a common calibrated trace and perfection on both
orders; matching generic ranks alone would not suffice.

For the knot centralizer the source order and its calibrated
trace are now available uniformly. If a proposed triangulation
presentation supplies a second self-dual order and a compatible
generic comparison, one integral inclusion will prove equality
of these orders and their cut pairings. The selected section,
the relevant operator action, and the prescribed lattice still
need to be transported; equality of endomorphism orders by
itself does not select a period vector.

The subsequent [sewn-source construction](sewn_source_and_meridian_charge.md)
now supplies an explicit two-copy projective corner for the actual
cup/cap residue with one helper strand. Its regular rational lift
uses V_(-M^3/q) on the first surviving strand, so the total central
character remains the original one. The cut on that corner is
the original calibrated trace. This application retains the full
meridian charge factor and identifies sewn residues, while the
entire polar projector, global source and selected period remain
additional comparisons.

The subsequent [adjacent-source normal form](adjacent_source_normal_form.md)
now determines the full local projectors with their regular parts.
It also constrains any common-order proposal: the ordinary trace
of two adjacent actual polar projectors has a nonzero double pole.
No one finite lattice can make both integral, even without an
H-linearity requirement. The integral numerators form a regular
matrix source algebra, while their unscaled projector arrows
require a groupoid of lattice changes. The self-dual-order
criterion above still applies to genuinely common integral
operators; it does not remove this pole obstruction.

At the first shifted color x=-M, e_1(x) is no longer a unit at
M=1, so Section 3 cannot be applied to that color. Its actual
[elementary modification and conductor](intrinsic_cut_and_meridian_atlas.md#the-first-meridian-wall-is-an-elementary-integral-modification)
must be retained. This theorem does not turn a polar meridian
comparison into an invertible integral matrix.

## 8. What this contributes to the ideal triangulation program

The earlier generic cut formula and two-factor self-duality are
now extended to the full integral tensor centralizer, for all
N and every strand count. This identifies a precise setting
for integral source descent: projective modules over symmetric
finite orders, with their calibrated trace, plus the conductor
modifications at the meridian wall.

This is an algebraic bilinear pairing. For b>=2 it even has
mathfrak_t_b(1)=0, since the ordinary quantum dimension vanishes.
Perfection therefore supplies no positivity or growth bound for
the selected contraction. Its norm still needs to be compared
with the marked Bloch-regulator norm.

The positive ideal triangulation supplies its marked Bloch lift
and regulator norm. The actual quantum source still needs a
compatible relative triangulated realization. Nothing here
identifies the central Casimir polynomial with the knot A-curve,
matches a fixed hyperbolic root character to the actual ADO
character, or estimates the selected quantum period across N.
Those comparisons remain necessary for the volume conjecture.

## 9. Coverage and diagnostics

The abstract of
[Beliakova--Blanchet--Gainutdinov, 1801.00321v2](https://arxiv.org/abs/1801.00321v2)
covers modified traces on projectives and their realization by
symmetric forms from Hopf integrals, including restricted quantum
groups. That theory is existing literature; no novelty claim is
made. Its theorems and proofs are not premises here. The PBW,
idempotent, tensor, corner and normalization calculations above
independently supply the particular statement over C[[log M]],
with the exact ADO factor and every parity retained.

[The audit](../experiments/audit_integral_centralizer_duality.py)
checks 15 PBW Frobenius forms at N=2,3,4,5,6 with generic and
both sign central characters. It verifies all left-regular
generator relations, the central polynomial, symmetry and a
nonzero Gram determinant. Five primitive-idempotent cases
realize the original complete color as a rank-N left ideal;
five generic cases calibrate every simple-block weight to the
original ADO dimension. Six explicit free-tensor maps at
N=2,3,4, including the shifted second color, are invertible
and intertwine all E,F,K.

Ten further cases compute the entire complete-color centralizer
directly from its commutator equations, without specializing any
fusion frame. Levels 2 through 6 and up to five strands give 279
basis elements in total. Every one is checked against the full
E,F,K matrices. The original full cut is symmetric and its Gram
determinant is nonzero in every case. These diagnostics test the
uniform proofs rather than establishing a volume limit.
[Results](../experiments/integral_centralizer_duality_results.json).

Reproduce with:

    python3 experiments/audit_integral_centralizer_duality.py
