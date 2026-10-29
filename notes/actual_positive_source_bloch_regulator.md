# A rational Bloch regulator for every positive-source volume maximum

**Later geometric result, 29 October 2026:** for every retained
cylindrical robust Conway factor, the
[actual cell realization](actual_positive_conway_hyperbolic_volume.md)
now identifies the source class with the geometric rational Bloch
class over a common number field, and its regulator with the actual
complete complement volume. The abstract rational-angle theorem below
continues to apply more broadly and does not itself supply a manifold.

29 October 2026. The algebraic volume period of every robust positive
Conway source is the regulator of an actual rational Bloch cycle. The
cycle is obtained by subtracting the complex-conjugate shape symbols.
Its boundary vanishes by the source's full constrained stationarity
equations. This is stronger than a formal sum of algebraic
dilogarithms, but does not identify the cycle with the marked
fundamental class of a link complement.

The argument applies to EVERY rational affine ideal-angle volume
problem in the
[algebraic maximum theorem](positive_source_algebraic_volume_period.md),
including boundary maxima and nonunique optimizers. It uses that
theorem's quotient by the exact flat Hessian kernel; it does not assume
that an optimizer is isolated in the original wire coordinates.

## 1. The rational Bloch group and regulator convention

Let K be a number field with its specified complex embedding, stable
under complex conjugation. Write U_K=K^times tensor_Z Q, additively,
and write ell(a) for the image of a nonzero field element in U_K.
Thus ell(ab)=ell(a)+ell(b); roots of unity have image zero.

Let P(K)_Q be the Q-vector space on symbols [z], z in K minus {0,1},
modulo the five-term relations

    [x]-[y]+[y/x]
      -[(1-x^-1)/(1-y^-1)]+[(1-x)/(1-y)]=0,          (1)

where the displayed arguments are defined and different from 0 and 1.
Use the boundary convention

    delta[z]=ell(z) wedge ell(1-z),
    B(K)_Q=ker(delta:P(K)_Q -> exterior^2 U_K).      (2)

This is the rational Bloch group, not an assertion of an integral
lift or of a particular K_3 lattice. The five-term relation has zero
boundary by direct expansion. In fact put

    X=ell(x), Y=ell(y), A=ell(1-x), B=ell(1-y),
    C=ell(x-y).

The five pairs ell(z),ell(1-z) in (1) are

    (X,A), (Y,B), (Y-X,C-X),
    (Y+A-X-B,C-X-B), (A-B,C-B).

Their signed wedge sum is identically zero in the free exterior
algebra on X,Y,A,B,C. Thus (2) is well defined without requiring
algebraic independence of the displayed field elements.

Let D(z) be the Bloch-Wigner dilogarithm, normalized so that a positive
ideal tetrahedron of shape z has hyperbolic volume D(z). Then
D(bar z)=-D(z). The same five-term relation holds for D, so

    R_K:P(K)_Q -> R,        R_K([z])=D(z)            (3)

is a well-defined regulator component for the specified embedding.
For completeness, the five-term identity follows from

    dD(z)=log|z| d arg(1-z)-log|1-z| d arg(z).

Applying this alternating bilinear differential to the preceding
zero wedge sum shows that the five-term D expression is locally
constant in x,y. The complex domain with x,y different from 0,1 and
from each other is connected. Letting y tend to x, all three ratio
arguments tend to 1, where D has continuous value zero; the first
two terms cancel. The constant is therefore zero. This also fixes
the sign convention and normalization in (3).

## 2. The algebraic data selected by the source maximum

Use the notation of the algebraic maximum theorem. The compact
rational polytope carries positive rational weights w_j and rational
affine ideal-angle triples alpha_j. Let F be its smallest face
containing all maxima. On F discard the atoms which are identically
flat, and call the remaining set I. Those positive atoms have the
SAME angle triples at every maximum.

After removing their common rational flat kernel, choose rational
coordinates y_l in which the positive angles read

    alpha_jr=a_jr+sum_l b_jrl y_l,   a_jr,b_jrl in Q.

The proved algebraicity theorem supplies an optimum y_* for which
the phases, sine values and positive shapes are algebraic. More
explicitly choose a positive integer B clearing the b denominators,
and put

    u_l=exp(pi i y_*l/B),
    t_jr=exp(pi i alpha_jr),
    s_jr=2sin(pi alpha_jr)>0.

Then

    t_jr=eta_jr product_l u_l^(B b_jrl),
    eta_jr=exp(pi i a_jr),                           (4)

where eta_jr is a root of unity. Choose K to contain these finitely
many algebraic numbers and their conjugates. It is a finite number
field stable under the given complex conjugation. No assertion that
K is the trace field of a manifold is being made.

All positive angles are interior in their simplices at a relative-
interior maximizer of F. Constrained stationarity in EVERY quotient
tangent y_l gives

    sum_(j in I,r) w_j b_jrl log s_jr=0.             (5)

For an integer C clearing the rational exponents, (5) gives the
exact algebraic relation

    product_(j,r) s_jr^(C w_j b_jrl)=1.             (6)

There is no winding ambiguity here: the s_jr are positive real
numbers, and (6) is derived from the selected real maximum. Its
image in U_K, divided by the nonzero rational C, is

    sum_(j,r) w_j b_jrl ell(s_jr)=0.                (7)

Equations (4) and (7), not merely the algebraicity of the shapes,
are the reason the regulator has a Bloch-cycle lift.

## 3. The antisymmetric shape boundary

For a positive angle triple (a,b,c), a+b+c=1, set

    t_a=exp(pi i a), s_a=2sin(pi a), and cyclically,
    z=t_a s_b/s_c.

The Euclidean angle sine rule, or an elementary sine identity, gives

    1-z=t_b^-1 s_a/s_c.                            (8)

For the elementary check multiply (8) by sin(pi c): it says
sin(pi c)=exp(pi i a)sin(pi b)+exp(-pi i b)sin(pi a).
The imaginary parts cancel and the real part is sin(pi(a+b)),
which equals sin(pi c). In particular Im z>0 and z has the prescribed
ordered ideal angles.

Write T_r=ell(t_r), S_r=ell(s_r). Since s_r is positive real,
conjugation fixes S_r and sends T_r to -T_r. Also

    T_a+T_b+T_c=ell(-1)=0 in U_K.

Using (8) to expand both shape boundaries therefore gives the exact
identity

    delta([z]-[bar z])
        =2(T_a wedge S_a+T_b wedge S_b+T_c wedge S_c). (9)

For clarity, the individual unsymmetrized expansion is

    delta[z]=-T_a wedge T_b
      +T_a wedge(S_a-S_c)+T_b wedge(S_b-S_c)
      +S_b wedge S_a-S_b wedge S_c-S_c wedge S_a.

The phase-phase and sine-sine terms are unchanged by conjugation;
only the two middle phase-sine terms change sign. Their difference
is (9). Thus the proof does not assume that the unsymmetrized sum of
positive shape symbols already has zero boundary.

## 4. Stationarity kills the complete rational boundary

Define the source class

    beta=(1/2) sum_(j in I) w_j([z_j]-[bar z_j])
                    in P(K)_Q.                     (10)

By (4), after torsion has been removed,

    T_jr=B sum_l b_jrl U_l,     U_l=ell(u_l).

Equations (9) and (7) now give

    delta beta
      =sum_(j,r) w_j T_jr wedge S_jr
      =B sum_l U_l wedge (sum_(j,r) w_j b_jrl S_jr)
      =0.                                         (11)

Hence beta is in B(K)_Q. It is anti-invariant under complex
conjugation and its regulator is EXACTLY

    R_K(beta)=sum_(j in I) w_j D(z_j)=max_P V.        (12)

There is no undetermined additive multiple of a volume constant in
(12): the symbols use their actual positive shapes and the regulator
uses actual ideal-tetrahedron volume. If there are no positive atoms,
beta=0 and the maximum is zero. If there are no quotient tangent
variables, (4) makes every T_jr zero and the same proof works directly.

This construction includes rational weights and affine constants of
arbitrary denominators. Passing to Q coefficients removes the roots
of unity in (4), the factor ell(-1) in (9), and the cleared exponent
in (6). The argument does NOT remove that torsion integrally. No
integral K-theory, integral Bloch boundary, or integral peripheral
normalization is asserted.

The ordered positive triples are uniquely selected by the maximum,
even when some original wire coordinates are free. Thus (10) does
not depend on choosing values for those flat coordinates. It is
unchanged as a displayed symbol expression by a rational change of
quotient coordinates; the coordinates are used to prove (11), not
to define its shapes.

There is also an elementary descent which removes the auxiliary
phase field. Put

    F_shape=Q(z_j,bar z_j : j in I) subset K.

The displayed expression beta already belongs to P(F_shape)_Q.
The inclusion F_shape^times -> K^times is injective; tensoring with
Q preserves that injection. Exterior squares of vector spaces
preserve injections as well (extend a basis of the smaller space
to a basis of the larger one). Thus

    exterior^2 U_(F_shape) -> exterior^2 U_K

is injective. The image of delta beta is zero by (11), so its
boundary was zero over F_shape itself. Consequently beta belongs
to B(F_shape)_Q. This descent uses neither a presumed injection
of Bloch groups nor a Galois or Hilbert-90 theorem. The phase
coordinates merely provide a finite algebraic field in which the
boundary calculation is transparent. For an empty atom list the
class is zero over Q.

## 5. The full original quantum limit is a Bloch regulator

For EVERY fixed robust actual positive Conway expression E, the
[whole-source variational theorem](actual_positive_conway_variational_limit.md)
and the algebraic maximum theorem yield, along all levels and both
parities,

    lim_(N -> infinity) (2pi/N)log Z_(E,N)
        =2 max_(P_E) V_E
        =R_(F_shape)(B_E),
    B_E=sum_(j in I_E)([z_j]-[bar z_j]) in B(F_shape)_Q. (13)

The weights here are all one and B_E=2 beta. Although its displayed
symbol expression has integer coefficients, its proved zero-boundary
statement is rational; possible integral torsion has not been checked.
Z_(E,N) is the entire original source, with all colors and repeated-root
normal directions retained. The class is selected by that exact
source's positive variational problem, not by choosing an arbitrary
branch of an A-polynomial.

The [cap-sum reduction](actual_conway_cap_sum_reduction.md) is compatible
with this construction. At a cap-closed product, the maximizing
polytope is a Cartesian product, its final gate is flat, and the
positive atom list is the union of the two lists. Thus, in a common
number field, B_(cap FG)=B_(cap F)+B_(cap G). This agrees with the
literal componentwise connected sum and exact source multiplication.
It also shows why a nonzero Bloch regulator alone cannot certify a
single complete hyperbolic complement.

## 6. The remaining geometric question is now more precise

We have an actual source-selected RATIONAL BLOCH CLASS, and its
regulator is the full quantum limit in (13). What is still missing
for a broad hyperbolic-knot theorem is a proof that this regulator
is the volume of the actual complement, for example by identifying
the class with its marked geometric Bloch class or by supplying a
source-compatible complete gluing certificate with the same volume.

The vanishing in (11) is algebraic and global, but it is not a face
pairing, an edge winding count, a cusp completeness equation, or a
fundamental-class degree computation. It also does not identify K
with a trace field, construct a generic-meridian A-torsor, or show
that a formal source cycle is the preferred geometric representation.
Those statements must not be inferred from the word "Bloch".

Audit: [formal wedge and stationarity certificates](../experiments/audit_actual_positive_source_bloch_regulator.py)
and [results](../experiments/actual_positive_source_bloch_regulator_results.json).
The identities are uniform symbolic exterior-algebra calculations;
finite numerical volumes are not used in their proof.

Independent internal review: the primary agent read the full proof,
independently expanded the conjugate-shape boundary and stationarity
factorization, checked the five-term differential normalization and
rational field scope, and replayed the symbolic audit successfully.
The additional descent to the conjugation-stable shape field was
checked separately: it uses exterior-square injectivity, not an
unproved assertion that Bloch groups inject under field extension.
The review leaves the marked manifold-class comparison open.
