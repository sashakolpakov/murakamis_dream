# The actual coefficient model has a nonzero geometric normal period

Research note, 26 October 2026. This derives the first transport
amplitude from the original crossing coefficients and proves a uniform
Morse--Bott statement at the complete hyperbolic representation. After
transverse formal contraction, the resulting actual-coefficient normal
connection is formally gauge equivalent to the marked geometric one.

This is a comparison of local normal stationary blocks. It is not a
construction of the selected global finite-state cycle, an identification
of its quantum-A annihilator ideal, or a volume-conjecture proof.

## 1. The actual state and its independent flow variables

Keep the original reduced state F_N(M), q_N=exp(pi*i/N), Q=q_N^2,
x=-M/q_N and Y=M^2. Use exactly the factorial boundary frame of
[the marked critical-correspondence proof](marked_braid_holonomy.md).
Its cut vector is constant and its covector is the normalized average.
The reduced period is still F_N(M); the factor 1/N is retained.

Take a b-strand knot braid with m crossings, read in the actual
operator-action order. Start with integer positions a_0,...,a_(b-1)
and one transfer k_t for each crossing. The position update is

    (a,b) -> (b+k,a-k) for a positive crossing,
    (a,b) -> (b-k,a+k) for a negative crossing.

Closing strands 1,...,b-1 gives b-1 independent integral equations.
Their matrix on the initial positions is a cofactor of P-I for the
braid permutation P. Because the closure is a knot, P is one cycle;
this cofactor has determinant +1 or -1. Thus all positions except
a_0 are solved integrally in terms of a_0 and all m transfers.
The total-index conservation gives the remaining closure as well.
There are exactly

    d=m+1                                           (1.1)

independent phase variables, on an integral flow lattice with no
unrecorded determinant. This counts variables of the actual cut sum,
not a substituted geometric state.

## 2. The principal amplitudes retain the color half-step

Write H=Log Q, A=Q^a, B=Q^b, C=Q^k. The balanced positive
crossing has exact variable product

    P_Q(QB)P_Q(QC)P_Q(Y/A)
       /[P_Q(QBC)P_Q(YC/A)P_Q(Q)],                  (2.1)

with the already proved Gaussian factor. The negative product
replaces B by A and Y/A by Y/B, with its different Gaussian.
The cancellation Qx^2=Y is important in (2.1): the last two
variable arguments are not Q-shifted arguments.

For the existing compact product,

    Log P_Q(z)=Li_2(z)/H+(1/2)Log(1-z)+O(H),
    Log P_Q(Qz)=Li_2(z)/H-(1/2)Log(1-z)+O(H).

Every higher variable coefficient is rational in z. Also
Log x=Log M+pi*i-H/2 on the specified sheet. Its contribution
to the Gaussian amplitude is sqrt(AB) positively and
sqrt(C/(AB)) negatively. Therefore the squared variable
principal amplitudes of the actual coefficients are

    a_(+,0)^2=AB (1-BC)(1-Y/A)
                      /[(1-B)(1-C)(1-YC/A)],
    a_(-,0)^2=C/(AB) (1-AC)(1-Y/B)
                      /[(1-A)(1-C)(1-YC/B)].        (2.2)

All five shape arguments are nonzero and different from one
on the established geometric chart, so these are units there.
Their square-root covers and original phases are retained.

This includes the exact local transport. For example the three
positive internal shift ratios are

    R_a=BC/x * (1-Y/(QA))/(1-YC/(QA)),
    R_b=A/(Cx) * (1-QBC)/(1-QB),
    R_k=-A/(QBCx) * (1-QBC)(1-YC/A)/(1-QC).         (2.3)

The negative ratios are

    R_a=x/B * (1-QAC)/(1-QA),
    R_b=x/A * (1-Y/(QB))/(1-YC/(QB)),
    R_k=1/x * (1-QAC)(1-YC/B)/(1-QC).              (2.4)

They follow by cancelling finite factors; no asymptotic knot
identity is used. If S is the actual local leading action,
each equation verifies

    [H]Log R_i=(1/2)S_(ii)+partial_i Log a_0.        (2.5)

For the actual meridian half-step M->exp(H/2)M, its ratios are

    R_M^+=(ABC)^(-1/2)(1-YC/A)/(1-Y/A),
    R_M^-=(AB/C)^(1/2)(1-YC/B)/(1-Y/B).             (2.6)

They have zero first H correction and satisfy
S_(uu)/8+partial_u Log a_0/2=0. The half-step and its original
square-root character are therefore checked independently.

The closed pivot and zero-framing factors contribute principal
amplitude M^(b-1-w)/product_(j=1)^(b-1) A_j, where w is the
writhe and A_j are initial closed positions. Their leading
phases and base-only constants remain the ones in the
[actual action calculation](quantum_longitude_and_regulator_action.md).
Thus the complete variable amplitude is nonzero on the chart.
Neither the fixed P_Q(Q)^(-m) nor the boundary normalization
1/N has been evaluated separately at a root or discarded.

## 3. The geometric critical scheme is smooth with two framing directions

The actual crossing calculation gives an isomorphism of open
critical schemes with framed augmented knot representations,
with its inverse meridian eigenflag fixed to the cut flag 1.
Its formulas and inverses have unit denominators on the chosen
chart, so this includes Artin rings, not just complex points.
The framing group is B_1=Stab_(PGL_2)(1), of dimension two.
The geometric representation is irreducible and its projective
centralizer is trivial; the framing torsor is explicitly split
by three developed flags, as already constructed in that note.

Here is why the unframed geometric germ is smooth with meridian
as coordinate, without importing a deformation-rigidity proof.
Use the positive triangulation and invertible marked gluing
Jacobian in [the geometric rigidity note](geometric_rigidity_and_cyclic_source.md).
The development construction identifies its germ with the
augmented representation quotient. This identification also
works over Artin rings: three distinct vertex flags give the
unique face transformation; their differences stay units.
The product around an edge fixes its two distinct endpoints
and has multiplier the edge shape product, hence is identity
when that product is one. The dual two-skeleton therefore
constructs a flat representation. Conversely a representation
and peripheral flag give the developed cross-ratios. Normalizing
one ordered triple makes these two constructions inverse.
The fixed SL2 lift is retained on its etale sign cover.

The marked gluing germ is etale over the meridian. Consequently
the actual framed critical germ at fixed M is a smooth open
part of its two-dimensional B_1 torsor. The actual inverse cut
flag can be compared by (U,V)->(-U,-V); both peripheral signs
are changed together, preserving the regulator differential.

It follows that the Hessian of the flattened actual phase has

    kernel=T(B_1), rank=d-2=m-1.                   (3.1)

Indeed the local gradient ideal is the logarithm of the
exponentiated critical equations. Its Jacobian is the Hessian,
and smoothness of this very critical scheme gives rank d-2.
This is a Morse--Bott assertion for the actual coefficient
phase. Alternatingness is not required; the positive geometric
input is the already audited one for hyperbolic knot exteriors.

## 4. A nonzero transverse formal block of the actual coefficients

Choose two actual position/transfer coordinates chi whose
differential on the framing torsor is invertible. Their level
set is an algebraic transverse slice. Restriction of the
symmetric Hessian to the remaining d-2 coordinate directions
is nondegenerate, because those directions complement its
radical. Let this restriction be H_perp.

Formal Gaussian contraction on the slice now yields a nonzero
normal block, with variable leading term

    A_(perp,0)=a_(beta,0)/sqrt(det(-H_perp)),         (4.1)

up to the retained coordinate half-density. The numerator is
a unit by Section 2 and the denominator is a unit by (3.1).
Subtract the full constant and quadratic phase before Wick
contraction; all remaining vertices have degree at least three.
At each formal H order there are finitely many contractions.
All coefficients are algebraic functions of the critical
representation and framing, regular at the complete chart.

Before selecting a framing section, the result is a formal
two-form density on B_1. If r,s are coordinates on that torsor,
then its squared leading coefficient is

    a_(beta,0)^2 det(partial chi/partial(r,s))^2
                                      /det(-H_perp). (4.2)

This formula changes correctly under a different transverse
coordinate choice. It does not perform the remaining framing
period. Replacing that period by evaluation at an arbitrary
framing section would change the selected global construction.

## 5. Formal normal difference transport agrees with the geometric line

Let K be a common algebraic function field for the geometric
gluing branch and its rational framing section, adjoining the
recorded half-density roots. The actual normal block has form

    Z_act^perp=C_beta(H) exp(S_act/H)
                      A_act(M)(1+sum_(j>=1)H^j A_j(M)). (5.1)

C_beta(H) denotes its recorded base-only normalization line,
including the fixed product and cut-average constants and powers
of H. If a constant Li_2(1) is moved from the phase into this
line, that move is recorded on both sides. No value of an
individual compact factor at a root is assigned.

All variable amplitudes in (5.1) belong to K, and A_act is a
unit on the complete chart. The positive triangulation's
dual local formal period in the geometric rigidity note has
the same property. Its leading action satisfies the same
preferred-longitude differential as S_act, and both complete
imaginary values equal Vol(M). Their leading difference is
therefore an M-constant real phase, retained in the comparison
line. Use epsilon=H=2h, h=Log q, throughout.

After retaining those base-only lines, the ratio of the two
normal amplitudes is an explicitly recursively computable

    g(M,h) in K[[h]]^times.                        (5.2)

It is their quotient of formal Gaussian series. The leading
term is the ratio of the algebraic unit amplitudes; every
higher coefficient follows by finite division in K. Thus,
for their actual meridian-step ratios with sigma(M)=exp(h)M,

    a_act^perp=a_geo * sigma(g)/g.                 (5.3)

Equivalently their formal period connections differ by
h dLog g, with all leading longitude and lift characters
matched. This proves a formal normal-connection comparison
to all orders. It is not merely a comparison of leading
dilogarithmic symbols.

The full ADO factor d_N(M), including its root-central
difference constant, remains the original one. It is not
absorbed into the coefficientwise formal unit (5.2). Its
local nodal density comparison is the separate exact result
of the preceding note.

## 6. What this does and does not select

The normal block comes from the actual coefficient model and
has nonzero principal amplitude. The remaining framing density
and its boundary source have not been paired with the actual
finite cut cycle. Equation (5.3) consequently does not identify
the quantum-A module of the selected finite sum, its root
monodromy eigenline, or its complete value with this normal block.

In particular no conclusion about a geometric factor of the
minimal summed operator follows just from the nonzero normal
block: taking the remaining relative period can kill a class.
The whole selected root source and its lattice still have to
be transported, including all polar intersections and caps.
Nor are the formal series assumed to converge or to control
their selected value along h=pi*i/N. The volume-norm theorem
is still required for the original F_N(1).

There is a concrete check against a tempting simplification.
The raw normal framing density is not automatically a constant
Haar form. At the figure-eight algebraic critical point over
F_97 with Riley root 36, frames (r,s)=(2,3),(3,2) give squared
two-form coefficients 92 and 77. Multiplication by s^2 gives
52 and 17, and multiplication by s^4 gives 80 and 68. Thus
neither dr ds/s nor dr ds/s^2 is the raw coefficient density
up to a frame-independent multiplier. A global framing
comparison needs its specified quantum adapters and boundary
source, not an assumed group-volume factor.

There is also an exact characteristic-zero calculation on the
full framing chart. Put t=(1-sqrt(-3))/2 and tau_cusp=2-4t. The
squared coefficient of dr ds in the same normal two-form is

    f_perp(r,s)^2=-tau_cusp/[6 s^2(s+1)^2].         (6.1)

The [full two-variable audit](../experiments/audit_full_framing_density.py)
retains both framing derivatives and checks the two Hessian
null vectors in Q(sqrt(-3))(s,r). Exact polynomial arithmetic
proves independence of r on this figure-eight chart.
[Results](../experiments/full_framing_density_results.json).

The [regular meridian centralizer](regular_meridian_centralizer.md)
now explains the additional (s+1) divisor. Its invariant
two-form adapted to the actual cut coordinate is
Omega_cut=-dr wedge ds/[s(s+1)], so (6.1) says exactly
Omega_perp^2=(-tau_cusp/6)Omega_cut^2. Contracting the latter
with its centralizer vector s partial_r gives dlog A_cut,
A_cut=1/(1+s). This identifies the geometric quotient form;
it does not yet prove that the original finite source and
its selected cut implement this contraction. Neither the
formula for every knot nor that period comparison is assumed.

The subsequent [actual cut-residue/density calculation](actual_cut_residue_and_principal_density.md)
now derives the logarithmic cut co-source directly from the
original finite average. Both original crossing amplitudes
have a mixed-Hessian/momentum-coboundary factorization;
the momentum factors cancel on every critical closure and
leave the original pivot. The corrected ambient phase
volume is invariant under the regular-meridian centralizer.
A linearized fixed-point complex supplies an invariant
torsion under a stated rigidity hypothesis. Identifying
that determinant line with this normal Gaussian density
and transporting the selected internal source remain work.

## 7. Precisely where the ideal triangulation theorem enters

The positive triangulation theorem supplies more than a numerical
expression for volume. Its geometric shapes produce the marked
Bloch representative beta_T, with D(beta_T)=Vol(M); Section 3
uses positivity to prove an invertible marked gluing Jacobian.
Development then transports this rigidity to the actual critical
scheme. Sections 4--5 consequently construct a nonzero transverse
formal block from the original crossing coefficients and compare
its connection with the geometric regulator line.

These implications use the ideal triangulation theorem at the
geometric realization and rigidity step. They do not assert that
the theorem supplies a quantum source, a selected relative period,
or a quantum comparison along arbitrary changes of triangulation.
In particular, the algebraically split framing torsor does not
fix a pairing of (4.2) with the original cut cycle. Selecting an
ordinary algebraic frame and selecting a horizontal pointed
relative period are different operations.

This gives a precise route for the next theorem. Transport the
actual relative source, its integral lattice, and its full cut
through a tetrahedral presentation to the positive triangulation.
Retain the marked meridian, longitude lift, and peripheral factors
throughout. The selected resulting relative class must pair
nontrivially with the normal block above. The required comparison
concerns this class and its period, rather than just the critical
equations or the existence of an unpointed module isomorphism.
Control of that selected period's regulator norm across levels
is additional to the local formal comparison.

## 8. An exact obstruction for a proposed source comparison

When the two proposed source objects admit specified equal-rank
affine presentations over the same difference field (F,sigma),
write them as

    sigma(v)=C_K v+c_K,
    sigma(w)=C_T w+c_T.                            (8.1)

This is a conditional comparison criterion; neither the existence
of a global geometric inhomogeneous factor for every knot nor a
selected triangulation source is assumed to have been proved.

A change w=Gv+t with G invertible intertwines (8.1) exactly when

    sigma(G) C_K=C_T G,
    (sigma-C_T)t=c_T-sigma(G)c_K.                  (8.2)

The first equation compares the homogeneous connections. Once it
is solved, the remaining obstruction is the explicit additive class

    [c_T-sigma(G)c_K] in F^d/(sigma-C_T)F^d.        (8.3)

Indeed, with H_aug=[G t;0 1] and U_i=[C_i c_i;0 1], the identity
sigma(H_aug)U_K=U_T H_aug is exactly the two equations (8.2).
Thus this obstruction concerns the horizontal affine extension,
not the existence of points on its underlying affine space.

The geometric gluing germ does not determine (8.3). For an
elementary demonstration take F=C(q,M), sigma(M)=qM and C=1.
The sources c=0 and c=1 have the same homogeneous connection,
but are inequivalent: sigma(t)-t=1 has no rational solution.
Expand any t in C(q)((M)); the constant Laurent coefficient of
sigma(t)-t is zero, whereas that of 1 is one. This proves the
claim without a growth argument. It does not model a hyperbolic
knot; it isolates the additional datum any comparison must retain.

Even a solution of (8.2) over a completed field is only a formal
extension comparison. To identify actual selected periods one
must also transport the source-one section p, the meridian lattice
Lambda, and the augmented cut functional lambda:

    p_T=H_aug p_K, Lambda_T=H_aug Lambda_K,
    lambda_T H_aug=lambda_K.                      (8.4)

Whenever these identities hold in the actual whole-germ period
realization, they give lambda_T(p_T)=lambda_K(p_K), including at
a marked specialization where the common lattice makes the period
regular. Equation (5.3) solves only the homogeneous formal normal
comparison; it does not establish (8.2)--(8.4) for the actual
relative source. Finite-cover descent alone cannot fill this gap,
as the trace argument in the [affine-source note](affine_quantum_a_period.md)
shows. This is the explicit source-compatible comparison for which
the positive ideal triangulation supplies the geometric target.

### When the source comparison also determines the period

There is a useful conditional reduction at a root. Work over a
coefficient field E with sigma of finite order n; for the actual
M coordinate and q_N this can be n=2N. Suppose both specified
source extensions in (8.1) have nonresonant cyclic monodromy,
det(I-H_K)det(I-H_T)!=0. Their rational horizontal source-one
sections are unique, by the cyclic descent proof in
[the affine-source note](affine_quantum_a_period.md):

    v_K=(I-H_K)^(-1)s_K, v_T=(I-H_T)^(-1)s_T.

Iterating the actual affine comparison (8.2) around the orbit gives

    G H_K=H_T G,
    s_T=G s_K+(I-H_T)t.

Substitution therefore proves exactly v_T=G v_K+t. Thus an
independent choice of rational horizontal section is unnecessary
under these hypotheses. When the specified selected sections belong
to this rational solution space and the cut and lattice are also
transported, their scalar periods agree, including a common regular
complete specialization. Nonresonance may fail at the complete
point: the equality is first an equality of rational whole germs,
then is evaluated on the specified common lattice.

This is not a proof of those hypotheses for the actual geometric
source. In a resonant block homogeneous rational sections remain,
and the original pointing must still be supplied. Nor does a
separately chosen root-level affine gauge control the comparison
across levels: a nonresonant extension always has a rootwise
rational splitting. A fixed generic comparison, or another proved
uniform realization with its normalization, is still required.
The triangulation theorem supplies the geometric chart on which
to seek that comparison; it does not construct the gauge or prove
the selected period's regulator norm.

The subsequent [common period-space construction](common_frobenius_regulator_period_space.md)
now records this geometric action line together with the actual
Frobenius and Tate marks over one logarithmic Heisenberg connection.
Its phase and norm identities are exact. A source-cohomology
retraction shows why that enlargement alone cannot split an
existing generic source. It does not prove (8.2)--(8.4) for the
actual knot period or control the selected realization of the
formal amplitude (5.2).

The subsequent [actual cut-wall source calculation](cut_wall_and_cyclic_source.md)
now identifies a local part of this comparison. The normalized
actual cut has consecutive wall factors p,sigma(p); its regularized
dual presentation and the geometric cyclic lattice have the same
point source. An explicit regular formal unit calibrates the
geometric collision to the actual wall, including its residue.
The full ADO common frame is retained. This is a comparison of
local presentations over S, not a solution of (8.2)--(8.4) for the
actual global source and selected knot section.

## 9. Exact checks and coverage

[The audit](../experiments/audit_actual_normal_stationary_period.py)
verifies all six exact internal first-transport identities
and both meridian half-step identities symbolically from
(2.3)--(2.6). Twenty-four independent geometric charts use
both algebraic Riley roots over F_97,F_193,F_601 and four
different regular frames per root. The Hessian is constructed
from the actual phase, while its null vectors are differentiated
from independent representation matrices. Each five-variable
Hessian has rank three and precisely the two framing null
directions. Every selected transverse determinant and actual
principal amplitude is nonzero. The meridian deformation
tangent satisfies the mixed Hessian equation, and the reduced
second derivative is twice the independently computed marked
longitude derivative. These are validations of the uniform
scheme and Gaussian arguments, not volume experiments.
The additional univariate function-field certificate proves (6.1)
and checks both framing null vectors before the stated restriction.
[Results](../experiments/actual_normal_stationary_period_results.json).

Critical-point existence and optimistic-limit potentials have
the coverage already recorded in the marked-braid note. Formal
stationary phase and formal difference connections likewise
have existing coverage in the earlier comparison notes. No
published proof is assumed here and no novelty claim is made.
The result added here is the particular normal-block comparison
in the original coefficient conventions, with the actual
subprincipal color, pivot and half-step factors retained.

The subsequent [uniform density theorem](quantum_source_bridge_extension.md)
now gives the intrinsic variable principal coefficient for arbitrary
knot braids: its parity-normalized square is -T_beta Omega_cut^2/2.
The Gaussian kernel and self-dual cokernel are explicitly matched
to the endpoint cut complex. Thus the determinant identification
is no longer limited to the two prototype knots. Its base-only
quantum normalization and selected global period remain unproved.

Reproduce the finite and symbolic first-transport diagnostics with:

    python3 experiments/audit_actual_normal_stationary_period.py
