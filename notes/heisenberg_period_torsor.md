# A Heisenberg torsor and a uniform finite period

Research note, 25 October 2026. The purpose is structural: replace
matrix-chart restrictions and individual knot calculations by an intrinsic
algebraic object. Definitions of the local cyclic quantum dilogarithm
already exist. The results below reconstruct its normalization as a
Heisenberg torsor, give an exact finite face reduction, and identify the
boundary module that any global construction must preserve.

This is not a proof of the full volume conjecture. The missing assertion
is identified in Section 7. In particular a splitting module, a selected
period vector, and a numerical growth law are different data.

The comparison with existing literature is in
`structural_literature_delta.md`. No novelty is claimed for Hilbert 90,
finite Heisenberg representations, cyclic dilogarithms, or Heisenberg
covers of Fermat curves.

## 1. The norm equation identifies the first cover

Fix an odd integer n>=3, a field k of characteristic zero containing
a primitive n-th root omega, and t on U=P^1 minus {0,1,infinity}.
Let x^n=t. The elementary identity

    Norm_(k(x)/k(t))(1-x)=product_j(1-omega^j x)=1-t       (1.1)

is the Steinberg norm relation. It gives a direct splitting of the
cyclic algebra

    A_t=k(t)<X,Y>/(X^n=t, Y^n=1-t, XY=omega YX).

Indeed on E=k(t)[x]/(x^n-t), let X be multiplication by x and let

    Y f(x)=(1-x)f(omega^(-1)x).

These operators satisfy all three relations. After adjoining x they
are a diagonal operator with distinct eigenvalues and a cyclic shift
with nonzero coefficients, and generate the full matrix algebra.
Consequently A_t is already End_(k(t))(E). This proves the splitting;
it does not assume a norm-residue or Brauer-group theorem.

Now choose c^n=1-t. The ratio

    r(x)=(1-x)/c

has cyclic norm one. The equation

    d(omega x)=r(x)d(x)                                 (1.2)

is exactly a Hilbert 90 equation over k(t,c). Its explicit solution on
the cyclic spectrum, with its initial value left free, is

    w_0=1,
    w_j=c^(-j) product_(a=0)^(j-1)(1-omega^a x),
    d_j=s w_j, 0<=j<n.

Equation (1.1) closes the recurrence at j=n. Conversely the recurrence
determines all d_j from s. Thus the solution set is a G_m-torsor before
normalization. This is an elementary proof of the Hilbert 90 instance
needed here, rather than an invocation without a specified cocycle.

One can also solve it in the cyclic function field itself. Write
sigma(x)=omega*x, sigma(c)=c, and for a in k(t,c)(x) set

    H(a)=sum_(j=0)^(n-1) w_j^(-1) sigma^j(a).

The recurrence and w_n=1 give sigma H(a)=r H(a). At least one
H(x^k), 0<=k<n, is nonzero: after division by x^k these expressions
are the finite Fourier transform of the nonzero vector (w_j^(-1)).
The Fourier matrix is invertible. This proves the required field
descent constructively as well. Determinant normalization still
requires its separately recorded n-th root.

For the user's generic peripheral factor, put t=-M^n. Since n is odd,

    product_j(1+omega^j M)=1+M^n.                        (1.3)

The factor is a cyclic norm, not a disposable numerical multiplier.
An unnormalized recurrence changes its n-step central character by
this factor. At M=1 it equals 2. This identifies an exact mechanism
for such factors; it does not identify the multiplier of the earlier
positive factorial model from its one factor-eight test.

## 2. Determinant normalization gives a Heisenberg cover

Set Delta=product_(j=0)^(n-1) w_j. The determinant-one normalization
of the diagonal intertwiner D=diag(d_0,...,d_(n-1)) is

    s^n=Delta^(-1).

Because n is odd, the expression simplifies to

    s^n=product_(a=0)^(n-1)
                       (1-omega^a x)^(a-(n-1)/2).       (2.1)

Thus all coefficients live on the finite etale cover of U

    T_n: x^n=t, c^n=1-t, s^n=Delta^(-1).                (2.2)

Its degree is n^3 as a finite locally free cover. Every factor is a
unit over U, so these are actual torsors there, rather than equations
silently evaluated at a branch point.

There are three deck transformations, written as maps of points:

    A:(x,c,s) -> (omega x,c,s(1-x)/c),
    B:(x,c,s) -> (x,omega c,s),
    C:(x,c,s) -> (x,c,omega s).

The norm identity and the determinant product show that they preserve
(2.2). Direct substitution proves

    A^n=B^n=C^n=1, C central, AB=C^(-1)BA.              (2.3)

They give a free transitive action on every geometric fibre: A and B
choose the first two roots, and C chooses the last. Therefore T_n is
a torsor for the finite Heisenberg group H_n, not just an unspecified
scalar normalization line. The extra central root records the failure
of the first two root changes to commute on the normalized intertwiner.

For comparison with the standard cyclic dilogarithm convention, let
q=omega^((n+1)/2), so q^2=omega and q^n=1, and set

    p^-=1/c, p^+=-x/(q c).

Then (p^-)^n+(p^+)^n=1 and

    p^-+q^(2j+1)p^+=(1-omega^j x)/c.

Thus d_j is exactly the spectral cyclic-dilogarithm definition, with
its determinant root retained. This is a reparameterization, not a new
local quantum function. The normalization cover, viewed over t, has
the explicit Heisenberg structure (2.3).

If U0 e_j=omega^j e_j and P0 e_j=e_(j+1), then

    D U0 D^(-1)=U0,
    D P0 D^(-1)=P0(1-x U0)/c.                           (2.4)

The commutant of U0,P0 consists of scalars: commuting with U0 forces a
matrix to be diagonal, and commuting with P0 makes its diagonal constant.
Consequently this intertwiner is unique up to scalar. Determinant one
reduces the ambiguity to mu_n. A mu_n-valued algebraic function on an
irreducible parameter component is constant, since its n-th power is one.
This is the precise rigidity statement available for comparing two
intertwiners of the same automorphism.

It does not prove that two arbitrary products implement that same
automorphism, nor that every projective scalar cocycle is trivial.
Those are separate coherence statements.

## 3. The face contraction is an exact finite Fourier evaluation

Let X be the ideal compactification of a globally branched knot exterior.
Its single ideal vertex and H_1(X;Z)=0 are the topological inputs.
Let r be the number of tetrahedra, and use the existing face selectors

    D_f=X_0-X_1+X_2, R_f=X_2-X_3, Epsilon=diag(epsilon).

Work over R=Z/nZ. The following argument also works for even n;
oddness is needed for the Weyl normalization in Section 5.
Define the finite groups and maps

    V=ker D_f,
    T(v)=Epsilon R_f v, U(v)=X_0 v,
    K=ker(T:V->R^r), H=T(V),
    W={w in H : (U k).w=0 in R for every k in K}.        (3.1)

For w in W choose any v with Tv=w and put

    q_W(w)=-(Uv).w in R.                               (3.2)

This is independent of the lift: changing v by k changes it by
-(Uk).w, which vanishes by definition. Its polarization is bilinear,
so q_W is a quadratic function on the finite abelian group W.

Use self-dual Haar measure n^(-1/2) times counting measure on R.
Its delta function at zero has value sqrt(n). For an arbitrary
function F:R^r->C define the charged-kernel-style contraction

    Z_n(F)=n^(-r/2) sum_(v in V)
                         omega^(-(Uv).Tv) F(Tv).        (3.3)

All signs and local spectral factors can be included in F. This is
the full face measure and all r independent delta factors, not a
bare unnormalized sum.

**Theorem.** For every such knot triangulation, including singular
face matrices and every composite n,

    |V|=n^r, |W|=n^r/|K|^2,
    Z_n(F)=|W|^(-1/2) sum_(w in W) omega^(q_W(w))F(w).   (3.4)

There is no limiting operation or choice of inverse face matrix.

**Proof of the topological input over R.** The local cocycle lemma
of `automatic_face_regularity.md` uses only addition and sign changes,
so it holds over R. The universal coefficient theorem gives
H^1(X;R)=Hom(H_1(X;Z),R)=0; with one ideal vertex its edge cocycles
themselves vanish. Thus D_f^T has trivial kernel over R. Perfect finite
character duality implies D_f is surjective, and |V|=n^r.

For k in K, define a character of V/K by

    kappa(k)([v])=omega^(-(Uk).Tv).

This is well-defined. If it is trivial, R_f^T Epsilon Uk annihilates
ker D_f and hence belongs to im D_f^T. Choose a with
D_f^T a+R_f^T Epsilon Uk=0. Locally write b=X_0k,c=X_2k.
The equations D_fk=R_fk=0 give face values (b,b+c,c,c), and the last
equation gives the paired position values
(a,-a,a+epsilon*b,-epsilon*b). They are exactly the same local ideal
edge cocycle. It vanishes, so k=0. Therefore kappa is injective.

Dualizing this injection gives a surjection V/K -> K^vee. Its kernel
is identified by T with W. Hence |W|=|V|/|K|^2.

Finally sum (3.3) over each coset v+K. Its coefficient is

    omega^(-(Uv).Tv) sum_(k in K) omega^(-(Uk).Tv).

Character orthogonality makes this zero outside W and |K| times
the displayed phase on W. Since n^(-r/2)|K|=|W|^(-1/2), (3.4)
follows, including its exact measure. QED.

This formulation survives primes dividing the integer face torsion.
W need not be a free R-module; its cardinality and quadratic function
are the invariant data. A rational nullspace dimension cannot replace
these data at such a prime.

## 4. The period is algebraic, with its normalization specified

When F is a product of local cyclic-dilogarithm entries, its coefficients
are algebraic functions on products of the torsors T_n. Formula (3.4)
is then a finite algebraic matrix coefficient on that parameter space.
Specializing an algebraic decorated holonomy gives an algebraic number,
with every determinant root and Fourier factor retained.

This is an exact finite period in the representation-theoretic sense.
It does not yet identify it with the continuous Faddeev state. The
local bridge and the additional dilogarithm period are given in
`rational_quantum_dilogarithm_torsor.md`.

## 5. Edge reduction gives one irreducible boundary module

Here is the invariant version of the face/edge linear algebra. Let
Lambda=R^(2r) with its standard alternating form. The r-1 independent
edge rows span a primitive isotropic submodule E_ed. Their primitivity
for odd n has a uniform proof. A dependence among all r edge rows
says that in each tetrahedron the three opposite-pair sums of edge
values are equal. Since 2 is invertible, such values are uniquely
lambda_ij=a_i+a_j. A face's three edge values recover its three a_i,
so the a_i agree across glued faces. There is one ideal vertex;
the dependence is therefore the constant edge assignment. Deleting
one row removes it. The same argument modulo every prime divisor of
n gives a unit minor locally, hence a split injection over R.

Isotropy is the local cusp-intersection cancellation already proved
in `preferred_longitude_cochains.md`. The full meridian/longitude
pairing is -2, a unit in R. Therefore

    E_ed^perp/E_ed is a free symplectic R-module of rank two, (5.1)

with its generators supplied by the marked peripheral curves. It
does not depend on the projection rank of a face matrix.

In the r-fold clock/shift module of dimension n^r use Weyl operators

    W(a,b)=omega^(-a.b/2) X^a Y^b,
    W(v)W(w)=omega^(Omega(v,w)/2)W(v+w).

For an edge character chi define the exact projector

    Pi_chi=|E_ed|^(-1) sum_(e in E_ed) chi(e)^(-1)W(e).

All nonidentity Weyl monomials have trace zero, so

    rank Pi_chi=n^r/|E_ed|=n.                           (5.2)

The boundary Weyl operators act on H_chi=im Pi_chi. For a class
v in E_ed^perp/E_ed, their trace on H_chi is zero unless v=0.
Their n^2 matrices are therefore trace-orthogonal and span End(H_chi).
This proves irreducibility and scalar commutant directly.

More generally, start with the split local cyclic algebras A_(t_j)
from Section 1 over the gluing function field. The classical gluing
equations make the commuting edge operators have n-th powers one.
Their projector gives the same rank-n boundary module, now with the
actual peripheral central characters. After a central-root extension
the trace argument above applies, and descends the dimension and
irreducibility assertions. Thus the interior gives a splitting of the
boundary cyclic algebra on its gluing field.

This is a uniform quantum Hamiltonian reduction. Singular face
projections are alternate presentations of the same reduction, rather
than additional species of quantum states.

### 5.1 Reduction of the torsor itself

On a nondegenerate gluing chart pull back one T_n for each classical
tetrahedral coordinate t_j. Push out their r central mu_n groups by
multiplication, with the recorded orientation convention. The product
cover becomes a torsor P for the Heisenberg extension of Lambda.
In Weyl coordinates this group has law

    (v,z)(w,z')=(v+w,zz'*omega^(Omega(v,w)/2)).

Choosing the inverse central generator matches (2.3); orthogonals and
the reduction are unchanged. All fixed signs in edge central
characters are incorporated before the next step.

For an edge monomial product_j t_j^a_j(1-t_j)^b_j=1, its root
eta=product_j x_j^a_j c_j^b_j is mu_n-valued. These roots give a
moment map P -> E_ed^vee. In root coordinates the edge vector is
e=(b,-a); under a deck vector v,

    eta_e(p.v)=eta_e(p)*omega^(Omega(e,v)).

For a prescribed character chi its fibre P_chi is a torsor for the
preimage H(E_ed^perp). The Weyl lift of E_ed is central in that
subgroup by isotropy. Its quotient is a torsor for

    H(E_ed^perp)/E_ed = H(E_ed^perp/E_ed).               (5.3)

This is the Heisenberg group of one boundary pair. Indeed on each
geometric fibre, primitivity makes Lambda -> E_ed^vee surjective
with kernel E_ed^perp. Each moment fibre is nonempty and transitive
with that stabilizer; quotienting its free E_ed action proves (5.3).
These finite etale constructions descend.

Thus a boundary H_n-torsor is constructed on every gluing chart,
without a proper-face hypothesis or an angle limit. Identifying its
period section on the intrinsic decorated character space remains
the global task; a quotient group alone does not identify the section.

The later [pointed tetrahedron gluing theorem](pointed_tetrahedron_gluing.md)
extends the edge-lattice step to all levels for S^3 link exteriors.
Its integral argument includes the missing prime 2 and proves
primitivity without a global branching. With the full Weyl phases
retained, the saturated boundary reduction has dimension N^c
at every N for c cusps. The marked unhalved peripheral rows are
a separate issue: their pairing -2 can give an index-two lattice,
whose algebra has two sectors at even levels. The earlier odd-n
identification with the full marked boundary algebra is therefore
not extended by silently inverting 2. The subsequent
[integral half-longitude proof](integral_half_longitude.md)
now identifies the saturation for a knot as the marked meridian
and half of its preferred longitude. A mod-two dual-face cocycle
and nullhomology of the longitude give this integral result
before N is chosen. The Weyl lift then has TY=q^2 YT; its square
retains the full edge character. Matching the actual central
longitude, source and selected period still requires comparison.

## 6. The torsor that still has to be globalized

For two presentations over an identified decorated-character function
field, with matched peripheral lifts, let H_X,H_Y be these irreducible
boundary modules. Their module-intertwiner space

    I_XY=Hom_(A_boundary)(H_X,H_Y)

is one-dimensional. Its invertible part is a G_m-torsor; a specified
identification of determinant lines reduces it to a mu_n-torsor.
Hilbert 90 handles descent of a specified multiplicative cocycle at
the function-field level. It neither chooses a canonical section nor
trivializes an arbitrary mu_n or degree-two obstruction.

The local module has a canonical vacuum, the unit killed by X+Y-1,
as proved in `pointed_steinberg_recoupling.md`. Tensoring these units
and applying the edge projector gives an algebraic candidate

    J_X=Pi_chi(1 tensor ... tensor 1) in H_X.

It can vanish on a locus; irreducibility of its ambient module has
not removed that possibility. A face contraction such as (3.4) is
a scalar period. Matching its boundary cut and frames to this projected
vector is an additional comparison, not an already proved consequence
of the scalar formula.

The relevant object is therefore the pointed splitting module
(H_X,[J_X]), together with its normalization line.
An unpointed intertwiner exists uniformly; proving that it takes
[J_X] to [J_Y] is the actual state-invariance assertion. Calling the
unpointed intertwiner line a torsor does not discharge that assertion.

The intended intrinsic object is the pointed boundary splitting module
with the reduced Heisenberg/dilogarithm period torsor. Its global
definition must identify the gluing charts of decorated flat local
systems and verify one universal quantum five-term coherence. A list
of individually certified knot triangulations cannot substitute for
that statement.

## 7. What rigidity can prove, and the remaining volume assertion

Once two normalized constructions are sections of the same pointed
intertwiner line and implement the same quantum automorphism, their
ratio is mu_n-valued and constant on each irreducible lifted parameter
component. One normalization fixes their exact equality there; descent
must still respect the deck transformations (2.3). This is the useful
algebraic rigidity mechanism.

The classical dilogarithm regulator is a value of the corresponding
period torsor, rather than an asymptotic definition of hyperbolic volume.
The requested conjecture still needs a uniform comparison of the
normalized quantum period with that classical regulator. Fixed-level
Zariski rigidity alone supplies no comparison between different n:
the covers T_n and their period vectors vary with n. The theory should
replace repeated saddle computations by this single compatibility
theorem; at present that theorem has not been proved.

The next proof obligations are consequently structural:

1. Construct the pointed period object on the intrinsic decorated
   character space and prove its universal five-term descent.
2. Match its normalization and cycle with the existing Faddeev state,
   using the exact local rational-parameter bridge.
3. Prove compatibility of its normalized size with the dilogarithm
   regulator on the complete geometric class, uniformly in the class
   of knots requested by the user.

These preserve the full objective. The finite reductions and torsor
identification above are tools toward it, not a redefinition of success.

The subsequent pointed recoupling, period-descent and frame-transport
notes now prove local selected-vector coherence and full projective
matrix covariance on the stated root covers. In particular
`projective_frame_period_torsor.md` supplies the operator comparison,
determinant normalization and identity anchor needed to apply the
rigidity mechanism of this section. Actual vector transport is essential:
the unit in an endpoint frame is generally not taken to the new unit.
The intrinsic equivariant knot period, its literature cycle and the
regulator comparison across levels are still outstanding.
