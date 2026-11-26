# Exact coupled cap sources and their regular meridian boundary relation

28 October 2026. Every terminal pair source can be peeled by exact
coefficients before taking a critical-point limit. The resulting source
is a coupled geometric polynomial, including at the original marked
cap. An exact interval identity retains its complete numerator and gives
a regular complex Lagrangian on which the actual framed meridians are
inverse. This supplies the classical cap equation missing from treating
the two terminal monomials as independent saddle variables.
The retained interval endpoints are disjoint from every regular
noncentral geometric critical branch for a one-component knot.

It does not compute the intersection of the original interval/torus
cycle with a hyperbolic thimble. In particular, a generic geometric clock
is complex, while the initial interval parameter is real.

The [audit](../experiments/audit_actual_coupled_caps_interval_source.py)
and [results](../experiments/actual_coupled_caps_interval_source_results.json)
check the literal duality matrices, all fused boundary coefficients,
whole original four-head words, interval identities on their logarithmic
charts, and the actual framed meridian product.

## 1. Physical pair sources, with their original normalization

Put

    N>=2, d=N-1, Q=exp(2*pi*i/N), F_a=(Q;Q)_a,
    y=x^(-1)Q^(-1), K_i=x_i B_i^(-1).

Use the existing balanced factorial basis and the actual oriented dual
in [the pivotal-duality proof](relative_pivotal_duality.md). On the
physical basis vector indexed by (a,b), the cup and ordinary right cap are

    cup_x(a,b)=N x^(a-d) delta_(a+b,d),
    cap_x(a,b)=N^(-1) y^a delta_(a+b,d).             (1)

The original averaged marked right cap, before any Ward-corner
replacement, is

    mark_x(a,b)=x^b/N^2,       0<=a,b<N.            (2)

Here is a direct normalization check. In the original unbalanced basis,
J_x e_b=c_b e_(d-b)^*, c_b=(-x)^b Q^(b(b+1)/2), and the pivot is
g_a=x^(-d)Q^(-a). The balanced reflection identity is

    F_b F_(d-b)=N(-1)^b Q^(b(b+1)/2).

Thus the balanced cup is F_a F_b/c_b on a+b=d; the ordinary cap is
c_b g_a/(F_a F_b). These give (1). Writing D_F=diag(F_a), the actual
averaged defect is D_F^(-1)g^(-1)e D_F, e_(a,b)=1/N. Its cap row is
(D_F^(-1)g^(-1)e D_F)^t g J_x before balancing, which gives (2)
at EVERY pair (a,b), not just on the invariant fiber.

For a k-pair plat, the cup degree is k d. Each ordinary cap forces degree
d on its pair. The actual word and every Gaussian dilation sector
preserve total integer degree. Consequently, after the k-1 ordinary
caps, (2) is paired only with the marked fiber a+b=d. On that fiber it is

    mark_x(a,d-a)=x^(d-a)/N^2.                     (3)

This restriction uses degree, not a Ward identity applied separately to
a Gaussian sector. Finite head support and all external scalar lines are
retained. If one first uses the already assembled Ward corner, reversing
that corner after decomposing into Gaussian sectors is not justified;
start from (2) instead.

Let K_N(r)=sum_(a=0)^(N-1) r^a. With the coefficient-source convention
that a row at (a,b) contributes z_1^(-a)z_2^(-b), the exact coupled kernels
are

    Cup_x(z_1,z_2)=N x^(-d) z_2^d K_N(x z_1/z_2),
    Cap_x(z_1,z_2)=N^(-1) z_2^(-d) K_N(Q^(-1)z_2/(x z_1)),
    Mark_x(z_1,z_2)=x^d N^(-2) z_2^(-d) K_N(z_2/(x z_1)).       (4)

The last line is precisely (2) on its forced degree fiber. Its
normalization is different from the ordinary cap. The phase Q^(-1) in
the ordinary cap is retained.

## 2. Exact terminal-factor peeling

These kernels can also be recovered by peeling the terminal factors in
[the all-Hardy residue graph](actual_hardy_forest_residue_reduction.md).
For the actual inverse fusion

    C_x^(-1)=F_2 F_1^(-1) V_- F_2^(-1),

the ordinary fused row is N^(-1)<0,d|. The terminal F_2 extracts
F_d=N, while the first-head reciprocal factorial at output 0 extracts 1.
The remaining exact coefficient is

    [b^d] U_N(b/z_2) V_N(b/(x z_1))
       =z_2^(-d) (t;Q)_d/N
       =z_2^(-d) K_N(Q^(-1)t)/N,  t=z_2/(x z_1).       (5)

Only the first N jets of U_N,V_N occur. The first equality is the finite
q-binomial theorem; the second follows from
(t;Q)_d=(1-t^N)/(1-Q^(-1)t). Both numerator and denominator are retained,
with the ratio extended as its polynomial.

For completeness, the fused original marked row m_x=mark_x C_x on the
same degree fiber has

    m_x(r,d-r)=x^(d-r)(-1)^r Q^(-r(r+1)/2) F_r^2/N^2.      (6)

Indeed the explicit fusion coefficient gives
sum_(a=0)^r F_(d-a)/F_(r-a)=N, by the finite q-binomial theorem and the
reflection identity. This yields (6). Peeling its adjacent complete
inverse fusion gives m_x C_x^(-1)=mark_x, not a new selected row.
There is no division by the knot value and no requirement that it be
nonzero.

Equations (4)--(6) eliminate all terminal monomial/factorial caps and
their redundant fusion-frame variables by exact coefficients. They do
not discard a terminal source endpoint: that information is in K_N.

## 3. Replace K_N by its exact interval source

On a chosen logarithmic chart write L=Log r and put

    A(r)=Log r/(r-1),
    K_N(r)=N A(r) integral_0^1 exp(N s Log r) ds.        (7)

This is an exact elementary integral, since its right side is
(r^N-1)/(r-1). On the sheet L=0 at r=1, A extends analytically with
A(1)=1 and is nonzero nearby. The two interval endpoints remain present;
(7) does not replace their difference by one exponential.

On a different logarithmic sheet at r=1 the individual factors in (7)
have a compensating pole and zero. The combined function is still the
polynomial K_N, but the factors must not be continued separately through
that point. On any compact logarithmic chart avoiding those points,
the interval integrand is bounded and ordinary Fubini applies. A full
angular circuit is treated as a lifted cut chart with its matched ends.

Substituting (7) into (4) gives the exact boundary kernels

    Cup_x=N^2 x^(-d) z_2^d A(r_cup) integral_0^1 exp(Ns Log r_cup)ds,
    Cap_x=z_2^(-d) A(r_cap) integral_0^1 exp(Ns Log r_cap)ds,
    Mark_x=x^d/N z_2^(-d) A(t) integral_0^1 exp(Ns Log t)ds,

    r_cup=x z_1/z_2, r_cap=Q^(-1)t, t=z_2/(x z_1).       (8)

In particular the original marked normalization is x^d/N after
introducing its one interval, not 1. These formulas can be inserted in
the original whole physical word. They are exact scalar source
identities, including with its continuous Gaussian variables.

Concretely, if W_beta is the original physical word on 2k heads, its
original selected scalar is the pairing of W_beta with k copies of (1)
as input, k-1 ordinary cap rows, and the one row (2), times the unchanged
external scalar line chi_beta,N. Equations (3)--(8) replace only those
sources. Each of the 2k turns contributes one interval coordinate,
independently of N. The boundary fusion frames can all be removed; the
unshortened all-Hardy graph now has 6m+2k complex coordinates for m
crossings, together with its m real Gaussian coordinates and the 2k
interval coordinates. This count is before any further coefficient
or residue simplification. The source numerator is encoded by the
retained ends of these intervals, not deleted.

For a source-compatible initial cycle one may ensure that every boundary
ratio has modulus different from 1. Initial cup radii can be chosen
freely. At a terminal touched head the last active factorial is positive:
its output radius can be enlarged arbitrarily while keeping its reflected
cyclic argument small. If it is the first head of its last crossing, the
only subsequent transfer lowers that head and increasing this radius
also makes the transfer argument smaller. The second-head terminal
factorial has no subsequent transfer. Thus the final radius of each
touched head can be enlarged independently; for each terminal pair
choose a sufficiently large common scale giving |t|=1/2. An untouched
head has its free source radius. This preserves the previous small-atom
chamber and gives fixed positive separation of the boundary ratios from
1. The logarithmic radius bounds remain C(1+sum|xi|), so the original
Gaussian domination still applies. Initial cup ratios can be perturbed
off 1 if an untouched pair fixes their reciprocal ratio.

## 4. The regular complex boundary relation

Let h=2*pi*i/N and define a clock by B=exp(p), where p is the
logarithmic semiclassical momentum. In (8), stationarity in the interval
interior requires Log t=0 at leading order (or Log r_cup=0 for the cup).
The resulting paired relation is

    z_2=x z_1,   B_1=exp(2*pi*i*s),   B_2=B_1^(-1).        (9)

The cup and covector orientations give opposite source momenta and the
same physical constraint. For the ordinary cap Log r_cap=Log t-h;
its extra factor exp(-2*pi*i*s) is nonzero and is kept in the amplitude.
At the exact position t=1 its already-integrated kernel has
K_N(Q^(-1))=0, and the ordinary cap--cup bubble remains exactly zero.
The nonzero density asserted below is the JOINT (head,s) density before
integrating s, not a claim that this integrated kernel is nonzero at
t=1. The original marked bubble is instead one. Both normalizations
are checked by the audit. Integrating out s can produce cancellation
and must not be mistaken for a proof of selected noncancellation.
The exact degree d=N-1 gives the affine constraint

    D+1=N,

and the leading clock lifts in (9) have p_1+p_2=2*pi*i. It is not a
zero-charge constraint produced by forgetting the half-step.
At finite N the source monomial has p_1+p_2=h d and hence
B_1 B_2=Q^d=Q^(-1); together with the actual dual color xy=Q^(-1)
this gives K_tot=1 exactly. The principal constraints (9) are its
Q-to-1 limit. No exact finite clock identity B_1 B_2=1 is asserted.

For fixed x the set (9), with z_1 nonzero and B_1 nonzero and different
from 1, is nonempty, regular, and Lagrangian: dlog B_2=-dlog B_1 and
dlog z_2=dlog z_1 cancel the two symplectic terms. The factor A has value
1 on its selected local sheet at the stationary relation. Interval
orientation is +1. Thus the local source density there is nonzero,
with its original scalar and Gaussian determinant still retained.
This statement is about a boundary relation and local density, not a
computed geometric-thimble multiplicity.

## 5. These are the actual inverse peripheral meridians

Use the commuting principal symbols of the actual balanced generators:

    K_i=x_i/B_i,
    f_i=(1-B_i)z_i,
    e_i=z_i^(-1)(x_i^(-1)-x_i/B_i),
    x_1=x, x_2=x^(-1).

On (9), direct substitution gives

    K_tot=K_1 K_2=1,
    f_tot=f_1+K_1^(-1)f_2=0,
    e_tot=e_1 K_2+e_2=0.                            (10)

At completeness x=-1, (9) reads z_2=-z_1. These are exactly the
classical equations of the actual dual pair, not equations of a newly
assigned boundary invariant.

To check the based meridians, retain the actual Gauss convention

    L_(+,i)=[[K_i,e_i],[0,1]],
    L_(-,i)=[[1,0],[-K_i f_i,K_i]],
    G_i=L_(-,i)^(-1)L_(+,i),
    H_1=G_1, H_2=L_(-,1)^(-1)G_2 L_(-,1).

Then the exact classical matrix multiplication is

    H_2 H_1=(L_(-,2)L_(-,1))^(-1)(L_(+,2)L_(+,1))=I.    (11)

The last equality follows from (10): both triangular products are I.
Raw G_2 G_1 is generally NOT the correct based product. These H_i are
the same framed meridians whose exact quantum Hurwitz transport was
proved in [the actual shared-flag note](actual_shared_quantum_flags_and_charged_exchange.md).
Thus the boundary branch in (9) is compatible with an actual knot
representation's oriented cup/meridian relation.
Conversely, H_2 H_1=I makes the upper triangular product
L_(+,2)L_(+,1) equal the lower triangular product L_(-,2)L_(-,1).
Their diagonal and off-diagonal entries force exactly (10). On the
regular locus B_1 different from 1, K_tot=1 gives B_2=B_1^(-1), and
f_tot=(1-B_1)(z_1-z_2/x)=0 gives z_2=x z_1. Thus (9) is precisely
the regular physical cap locus, not only a sufficient special family.

At x=-1, this chart covers the Zariski-open part of the nontrivial
trace -2 parabolic class with G_(11) different from 0,-1. Explicitly
B=-1/G_(11), z=(-G_(11)-1)/G_(12). The determinant and trace equations
force G_(12)G_(21)=-(G_(11)+1)^2, so z is nonzero there.
For finitely many nontrivial parabolic meridians, a simultaneous generic
SL(2,C) conjugation avoids all these finitely many proper closed
conditions: each is proper on a parabolic conjugacy class, and SL(2,C)
is irreducible. Hence a supplied geometric knot representation with
inverse meridians at its paired turns has a simultaneous regular
boundary chart. At each turn the second physical factor is recovered
by (10)--(11), giving B_2=B_1^(-1), z_2=-z_1.
In a list of adjacent paired turns the preceding paired triangular
products are I by (10), so the first meridian of the next pair is in
the same based frame; a separate independent frame per cap is not
being assumed. This is a classical simultaneous framing statement.
It does not supply a quantum cycle map implementing that conjugation.

This does not assert that every INTERNAL factorization chart of the
word is regular in that frame. Further five-term/relative-chart
transport may still be needed there.
For example, substituting the regular physical cap into the inverse
fusion chart gives K=V, A=UK=1 and J=V/K=1. This intrinsic terminal
auxiliary degeneration is why adjacent boundary factors were peeled
by coefficients rather than declared regular independent saddles.

There is also an exact agreement with the literal five-flag source
mark. Put R=x z_1/z_2 and X=x z_2/z_1, as in the
[marked full-Phi flag calculation](actual_marked_full_phi_flag_pentagon.md).
At the complete root x^2=Q^(-1), so X=Q^(-1)/R. The source branch R=1
therefore has precisely the mark X=Q^(-1). In the original finite typed
source, the independently proved equality is X cup=Q^(-1)cup. This
marking match does not impose X^N=1 on the unwrapped scalar coordinate;
the latter remains a variable until an actual source/cycle map supplies
that specialization.

## 6. Complex cap clocks have an exact endpoint-fixed source deformation

Initially s is the real interval [0,1]. Its interior clocks lie on the
unit circle. A generic geometric B is any nonzero complex value; its
logarithm gives a complex s modulo integers. No claim is needed that a
single frame puts every B on the unit circle.

There is instead an exact source-preserving deformation. For fixed Log r,
the function exp(Ns Log r) is ENTIRE in s. Consequently, for any compact
piecewise smooth path gamma from 0 to 1,

    integral_gamma exp(Ns Log r) ds
       =integral_0^1 exp(Ns Log r) ds.                  (12)

This follows from its entire primitive, also at Log r=0. Given a regular
geometric clock B, choose any s_g=Log B/(2*pi*i) and an endpoint-fixed
path through s_g. Equation (12) proves exact equality of the original
source pointwise in every other variable. It holds for all caps
simultaneously by taking the product paths. The endpoints are unchanged;
there are no residues or omitted source corrections in this s-only
deformation. One may prescribe a nonzero local tangent at s_g as well.

If useful, a single generic classical frame can also avoid the positive
real ray for all the finitely many B. Each B is a nonconstant holomorphic
function of that frame; its positive-ray inverse image has empty
interior by the open mapping theorem. On this additional dense open
real-analytic choice, use 0<Arg B<2*pi, giving 0<Re s_g<1. This is not
required for (12), but places the desired complex point directly above
the interior of the initial interval strip.

On a fixed compact path family, |s| is bounded. The additional absolute
factor is at most exp(CN|Log r|); the initial radius estimates make this
at most exp(C'N(1+sum|xi|)). Thus the original Gaussian majorant still
justifies the joint path deformation and Fubini. The marked logarithmic
charts in r, including their matched angular ends, remain as in Section 3;
entireness in s is not a license to discard those data.

Therefore the theorem removes the spurious separate-terminal-monomial
critical equations and supplies a regular actual meridian boundary
Lagrangian with nonzero density. The boundary interval paths can be
deformed through its desired complex clocks exactly. This does not yet
prove that the bulk head-variable cycle reaches the same geometric
branch with nonzero whole-cycle intersection, or
that its endpoint/alias contributions have smaller exponential rate.

## 7. A regular interval endpoint cannot carry a noncentral knot representation

At either retained interval endpoint s=0 or 1, the principal source
clocks are B_1=B_2=1. Stationarity in s is not imposed at an endpoint,
so this does NOT require z_2=x z_1. Nevertheless, at x=-1 the actual
classical generators have e_i=f_i=0, K_i=-1 for every finite nonzero
z_i. Hence each physical G_i=-I, and the framed H_i is also -I.

Suppose a complete stationary solution is in regular charts where the
actual Hurwitz laws and paired boundary equations define a representation
of a ONE-component knot group. All its oriented meridians are conjugate,
up to inversion. If one is -I, every meridian is -I; since meridians
generate the knot group, the induced PSL(2,C) representation is trivial.
Thus no noncentral geometric representation occurs at a regular source
interval endpoint.

In particular, choose a regular geometric critical point and small
coordinate neighborhoods of its finitely many interval coordinates
s_g. Each s_g is different from 0 and 1, since its meridian is not
central. The neighborhoods can be chosen with positive separation
from both endpoints. Every endpoint stratum has empty intersection
with this neighborhood of the geometric critical branch. Thus the
localized geometric stationary germ, including its Gaussian block,
has no contribution from a cap interval endpoint. This removes an
endpoint cancellation of THAT local block; it does not compute the
original whole-cycle coefficient of that block.

This is a source-support exclusion on the regular representation locus.
It is not an estimate for endpoint periods on singular norm divisors,
escaping flags, or extra integer phase aliases. Those are precisely the
cases where a regular representation argument alone supplies no bound.

## 8. Uniform regular-geometric exclusion of physical cutoff walls

The same argument applies to fixed signed endpoint-clock projectors
in the actual five-term/flag moves, including the explicit E_0(Z)
in [the marked full-Phi flag calculation](actual_marked_full_phi_flag_pentagon.md).
The clock here must be a PHYSICAL actual head clock, or an explicitly
tracked exact Hurwitz conjugate of one; arbitrary fusion-relative
clocks are not covered.

For Z^N=1 define its original spectral projector

    E_j(Z)=N^(-1)sum_(r=0)^(N-1) Q^(-jr)Z^r.

Exactly, (Z-Q^j)E_j=0. Let j range over a fixed finite set of signed
integers as N grows, so the top index d is j=-1. Their principal
characteristic wall is B=1. At complete color the corresponding
actual physical meridian is G=-I, as proved above. A regular actual
Hurwitz solution for a one-component knot on ANY such wall therefore
has trivial induced PSL(2,C) representation.

This gives a uniform LOCAL statement near a compact regular geometric
critical branch. There are only finitely many tracked clocks, and
their B values differ from 1. Choose delta>0 such that |B-1|>=delta
throughout a sufficiently small compact neighborhood. For all large N,
|B-Q^j|>=delta/2 for every one of the finitely many signed j.

More explicitly, suppose a wall component admits a regular formal WKB
expansion exp(S/h)(a_0+h a_1+...), h=2*pi*i/N. A physical clock acts
with leading multiplier B=exp(partial_(log z) S). Its annihilating
relation (Z-exp(jh))f=0 first gives (B-1)a_0=0. Since B-1 is invertible
on this neighborhood, a_0=0. At each subsequent order the lower
coefficients already vanish, leaving (B-1)a_r=0; hence EVERY a_r=0.
Exact Hurwitz conjugation transports both the annihilating equation
and this regular symbol argument. A bounded fixed number of clock
shifts only changes the finite signed set of j.

Thus physical endpoint-projector corrections have zero regular formal
geometric block in these charts. They cannot cancel a nonzero
localized geometric Gaussian block there. This is neither an analytic
bound on the full root-level correction nor a proof that such a
Gaussian block is selected by the original whole cycle.

Two limitations are essential. First, a bulk index j_N/N tending to
a nonzero angle has principal B=exp(2*pi*i*lim j_N/N), not 1, and is
not excluded. Second, relative fusion clocks A=J=1 can occur on a
REGULAR physical cap, as the explicit inverse-fusion calculation in
Section 5 shows. A projector in such a relative clock must not be
called a physical meridian cutoff without its actual clock map.

No finite Ore localization is being performed. Inverting all the
shifted factors 1-Q^r Z at fixed N would invert their product
1-Z^N=0 and destroy the whole finite module. Formal regular-geometric
exclusion at bounded signed shifts does not authorize this globally
invalid operation, or deleting any original finite source/projector.

## 9. Finite physical-projector stationary strata have action zero

There is also a critical-VALUE statement, including the missing normal
equation of an endpoint projector. It applies to a network of actual
canonical crossing relations, the original inverse-meridian turns,
and finitely many explicitly tracked PHYSICAL signed-endpoint
projectors. Require finite nonzero physical position coordinates.
At every crossing the shape tuple must be regular, or a genuine joint
limit of its regular actual rational graph; an arbitrary cleared
auxiliary chart is not sufficient. Stationarity is imposed in all
remaining phase directions. The following argument does not assume
stationarity in a projector's fixed clock normal.

First, a general finite unit-wall calculation extends the action
identity. Write the full leading phase, with all original logarithmic
marks retained, in the form

    W(Z)=sum_j epsilon_j Li_2(exp(a_j.Z+i phi_j))
                      +Z^t C Z/2+i kappa.Z+c,

where C is real symmetric, a_j,phi_j,kappa are real and Im c=0.
Restrict it to a stratum of linear logarithmic constraints

    A Z=i theta_0, A and theta_0 real.                 (15)

Thus A Re Z=0. Dilog terms identically equal to Li_2(1) on the
stratum are real constants, with their consistent integer marks,
and are omitted from its derivative. If this restricted finite phase
is stationary, the gradient of its remaining expression is conormal
to (15). Its contraction with Re Z consequently vanishes. The
off-critical defect identity from
[the actual regulator calculation](actual_wall_critical_regulator.md)
therefore gives EXACTLY

    Im W=sum_j epsilon_j D(exp(a_j.Z+i phi_j)).        (16)

This also covers dependent linear unit-wall constraints, after using
a basis of their conormal space. It avoids assigning a finite value
to a singular normal derivative: remove the constant Li_2(1) terms
before differentiating on the stratum. Equivalently their possible
normal limits are bounded by rho log|rho|, which tends to zero.
All Gaussian/cap variables and pure-imaginary integer logarithmic
terms remain in this calculation. An unrelated constrained maximum
of the real part of W does not satisfy this stationarity hypothesis.

Next the original physical projector kernel is, in the actual
position frames,

    (F_out E_j F_in^(-1))(zout,zin)
                         =N^(-1)(zout/zin)^j.         (17)

For a bounded signed index choose its representative j_N in [0,d].
Its leading clock lift h j_N, h=2pi*i/N, is either 0 or 2pi*i;
the latter integer logarithmic phase in (17) is retained. In either
case its characteristic correspondence is

    B_in=B_out=1, positions zin,zout arbitrary.       (18)

Thus a projector can allow a position/flag jump. It does NOT permit
a physical MERIDIAN jump: at B=1 the original finite-chart formulas
give K=-1,e=f=0 and G=-I, independently of that position. Based
conjugation preserves -I. All the other crossing, wire and turn
relations therefore glue physical meridian matrices through this
projector just as through an ordinary wire. They define a
representation of the SAME one-component knot group, even though
the auxiliary position need not be periodic at that wire.

One meridian is -I by (18); every knot meridian is conjugate to it,
up to inversion. Hence ALL meridians are -I. In these finite charts
every physical clock equals one. The original direct five-symbol
crossing regulator is consequently zero at EACH crossing: its
arguments are A=B=C_plus=C_minus=1. The nine-symbol value has the
same limit whenever the specified joint actual graph limit exists.
Cups, caps, Gaussians and the retained projector marks add no Bloch
terms. Equation (16) proves

    Im W=0                                             (19)

for every such stationary physical-projector stratum.

This extends the local geometric exclusion of Section 8 to a value
bound for finite physical-wall stationary blocks, despite their
omitted clock-normal equations. It is not an analytic bound on the
sum or mass of those blocks. Auxiliary fusion clocks, escaping
positions, arbitrary cleared-graph branches and bulk indices j_N/N
not tending to 0 or 1 remain excluded. Nor does (19) apply to an
unidentified TRANSFER-index endpoint: its zero-transfer Cartan-flip
branch need not force any physical meridian to be central. Those
boundaries require their own exact source grouping.
