# Resolved physical head faces: the original crossing and the missing wire equation

28 October 2026. A physical clock B tending to one need not make its
meridian central. The resolved chart f=(1-B)p finite contains a genuine
noncentral unipotent. The restricted positive crossing at input b=0,
including bulk transfer, is exactly the projection of the ORIGINAL
Hurwitz graph in this chart. Its action can have nonzero regulator.

This local resolution does not identify arbitrary restricted-face
critical points of the full word with knot representations. At a shared
head the two resolved parameters still have to agree. Fixing the head
face omits precisely that equation, and the complete sublinear head
packet has a generically nonzero off-diagonal reproducing kernel.
The packet and every normal coefficient must remain in the source.

## 1. Restricted stationary values, with the singular normal removed correctly

Write the actual marked phase in clock logarithms Z as

    W=sum_j epsilon_j Li2(A_j)+Z^t C Z/2+i kappa^t Z+c,
    A_j=exp(v_j.Z+i phi_j), C real symmetric, Im c=0.

On a physical face a set of integral real forms obeys

    a_f.Z=2pi i n_f, n_f integer.                     (1)

All its active shape-one terms have finite REAL Li2(1) values, with
their recorded flattenings. Restrict those terms to their constants
before differentiating. Call the resulting regular extension W_reg;
the original normal derivatives of W itself may be logarithmically
infinite. If the restricted phase is stationary in ALL complex tangent
directions, elementary linear algebra gives

    partial W_reg=sum_f lambda_f a_f.                 (2)

The active normals annihilate rho=Re Z. The same exact phase-defect
calculation as for the full action therefore gives

    Im W_face=sum_(j inactive) epsilon_j D(A_j).       (3)

Indeed the defect is rho.Im(partial W_reg), which vanishes by (1)--(2).
The omitted D(1) terms are zero. Integer mode marks from the cardinal
windows are retained; they only add integer multiples of the face
forms or of the other clock logarithms. They do not alter this proof.

Equation (3) is a regulator CALIBRATION, not a bound by knot volume.
Exponentiating (2) gives defect characters exp(lambda_f) in the regular-
part equations. It does not impose the missing full normal equations
or membership in the saturated original critical graph. In particular
one must not evaluate the original unsaturated rational equations at
their 0/0 shape-one factors.

## 2. A finite noncentral head chart

For one actual head use the physical Gauss coordinates

    K=-1/B, e=(B^-1-1)/p, f=(1-B)p.

Put s=1-B and tau=s p. Then

    K=-1/(1-s), e=s^2/[(1-s)tau], f=tau.              (4)

At s=0, tau!=0 this is a finite NONCENTRAL lower unipotent meridian.
It was absent from the finite-p centrality argument. The complementary
chart retains e finite and f tending to zero. The two branches obey
the exact physical equation

    e f=(1-B)^2/B.                                   (5)

Consequently two finite nonzero e- and f-parameters cannot describe
the same limiting head at B=1. Any change of chart or source adapter
must preserve (5); its small action alone does not justify deleting it.

The change is symplectic on the regular overlap. For the Liouville form,

    Log B dLog p - Log B dLog tau =d Li2(1-B).         (6)

This generating function tends to zero at B=1. Its normal derivative
is still needed when matching adjacent charts.

## 3. The actual b=0 crossing is locally the resolved Hurwitz graph

Use input clocks A,B, input positions p,r, and transfer U. The positive
physical outputs have clocks C=BU and E=A/U. The actual input fields are

    e1=(1-A)/(A p), f1=(1-A)p,
    e2=(1-B)/(B r), f2=(1-B)r.

The original Hurwitz graph has d=1-e1 f2, U=1/d. Let B tend to one in
the chart (4), keeping A,p,tau regular and e1!=0. For any regular bulk
U one can choose

    tau=(1-U^-1)/e1.                                 (7)

The limit is the ORIGINAL crossing graph, not a replacement map. Its
output clocks and positions are

    C=U, E=A/U,
    p_out1=p/(1-A),
    p_out2=(A-U)p/[U(1-A)].                          (8)

Substitution in all six original Gauss formulas proves these identities.
For example the output fields are

    e_out1=-A e1^2 tau, f_out1=-U tau/A,
    e_out2=-U e1,
    f_out2=-(1-A)p/U+tau(A/U-1/A).

They equal the physical fields of (8). The chart is regular for
A,U,A/U away from 0 and 1 and p,tau nonzero.

There is an independent generating-function check using the literal
physical coefficient, rather than assuming that a face belongs to
the graph. At b=0 the EXACT coefficient is

    r(a,0,k)=kappa x^(-a+k) F_a/F_(a-k).               (9)

Let u=Log A, v=Log U, x tending to -1 on its retained lift. Its leading
action, up to a real constant, is

    W_face=-Li2(A)+Li2(A/U)-i pi(u-v).                 (10)

The original output/input position terms are

    v Log p_out1+(u-v)Log p_out2-u Log p.

Stationarity in u and v gives EXACTLY (8). The omitted incoming second
position is replaced by (7), finite in tau and divergent in r=tau/s.
Thus every regular point of this restricted local canonical relation
lifts to the resolved ORIGINAL local graph. This is a useful positive
local theorem. It includes bulk k; such a face must not be declared
central merely because B=1.

The direct five-symbol regulator on this face is

    R_face=D(A/U)-D(A).                              (11)

It need not vanish. At a simultaneous opposite head degeneration
A=B=1, with e1 and f2 finite and e1 f2=1-U^-1, it becomes D(1/U).
These are limits of the genuine local crossing regulator. Their
nonzero values do not contradict the finite-p central theorem,
whose physical-position hypothesis has failed.

## 4. An exact mixed factorial gauge and its scope

Let D_j=F_j on the original head basis. Apply basis factor D^-1 to
input 1 and output 2, and D to input 2 and output 1. With c=b+k,
e=a-k, the transformed physical coefficient is exactly

    (F_e F_b)/(F_c F_a) r(a,b,k)
                 =kappa x^(-a-b+k) Q^(b(a-k))/F_k.    (12)

All physical supports remain. This displays explicitly how the e- and
f-type endpoint charts remove the local head-factorial singularities.
The clock phases are still present. The actual current differs from
the corresponding unweighted shift by its retained diagonal Q phase;
no cyclic wrap is identified with the nilpotent shift.

For a low packet 0<=j<=R=o(N), elementary sine bounds give

    |F_j| >=(4/N)^j j!,
    ||D|| ||D^-1|| <=exp[O(R log(eN/R))].             (13)

For large N every root factor in that packet has modulus below one,
so the smallest product is F_R and the displayed estimate follows
from R!>=(R/e)^R. Reflection gives the same type of bound at the high
packet, with its explicit N and unit phases. Thus the basis change
and its inverse cost exp(o(N)); it is legitimate source transport on
the WHOLE retained packet. Its adjoining wire/source factors remain.
The stronger uniform two-band statement, its globally invertible
truncated gauge, its band-interface arrows and mandatory cyclic
correction are proved in [the endpoint head chart](actual_endpoint_head_factorial_chart.md).

## 5. What still has to be matched across a resolved head

On a shared head the original identity gluing has the same B on the
two sides and p_left=p_right. Equation (4) then implies

    tau_left=tau_right.                              (14)

This condition is not restored merely by fixing s=0. For example the
wire generating term on the regular overlap is

    Log B [Log tau_left-Log tau_right].

At B=1 its VALUE is zero and all tangent derivatives in the tau's
are zero. Its omitted normal derivative is exactly the logarithm of
the ratio in (14). This gives an explicit explanation of why the
face-value identity (3) does not supply global representation gluing.

Retaining all coefficients in a low packet preserves the exact source,
but also retains its off-diagonal current. In the corresponding
monomial head frames the identity wire is the reproducing kernel

    K_R(xi/eta)=sum_(j=0)^R (xi/eta)^j,               (15)

in coefficient/constant-term normalization. The unitary finite Fourier
matrix kernel is K_R/N, as in the endpoint head chart; that polynomial
normalization does not change the exponential conclusion below.
Here xi,eta are the two resolved head coordinates. The adjacent factorial
gauges cancel; a known pivot only changes its specified ratio. The
kernel is polynomial and generically nonzero when xi!=eta. Its apparent
Hardy matching pole is removable because both terms in

    K_R(q)=[1-q^(R+1)]/[1-q]

have equal opposite residues at q=1. For example K_R(2)=2^(R+1)-1,
so even a fixed off-diagonal separation is not suppressed at rate
exp(-cN) when R=o(N). This is a statement about the actual retained
source packet, not an arbitrary inserted coupon. It does not prove
that the mismatch survives the exterior knot pairing.

Normal stationarity before restricting the face WOULD impose (14).
But a proof at exponential scale cannot infer that stationarity merely
from the source being exactly preserved or from the gauge norm being
subexponential. Endpoint and interface currents of the shrinking normal
packet must either be estimated coherently or included in an actual
resolved gluing theorem. Likewise an e/f wire must retain (5), not
replace its small generating action by a unit.

## 6. Consequence for the desired face bound

Local blowup resolves an important apparent obstruction: bulk transfer
at a physical head endpoint can lie on the genuine crossing graph
with finite noncentral meridians. The regulator and the tangent phase
agree there exactly. If ALL resolved wires also satisfy their original
matching equations and the full marked closure, these local graphs
assemble to an original boundary-parabolic knot representation and
the already proved representation-volume bound applies.

Arbitrary restricted-face stationarity supplies neither (14) nor its
e/f counterpart. Thus no blanket |R_face|<=Vol(K) theorem for every
cardinal-window physical-face critical point is proved by the local
resolution or tame basis change alone. The precise missing source
estimate is for the complete off-diagonal normal-packet currents,
with the original exterior phase retained. This is stronger and more
specific than the old finite-position centrality statement.

[Audit](../experiments/audit_actual_resolved_head_face_geometry.py):
all six rational Gauss output identities, the two tangent generating
equations, exact mixed gauge factors, endpoint packet norms, the
noncentral resolved input and the retained off-diagonal wire source.
