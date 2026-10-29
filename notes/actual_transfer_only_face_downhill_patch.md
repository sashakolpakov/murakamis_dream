# Simultaneous lower-transfer faces with interior physical heads go downhill

28 October 2026. This gives a source-preserving boundary operation for an
arbitrary fixed one-component braid word. Several actual total transfers
may approach zero simultaneously. If every physical head factorial stays
in a regular interior strip, all those transfer normals have compatible
zero sides. The original scalar cardinal source can be continued from
its existing lower cotangent sides through their joint NEGATIVE collar,
with its exact currents retained. Every
outgoing selected-strip norm/cardinal phase is downhill at the stated
nested scale.

Head endpoints are excluded. This is a genuine class of removable exits,
not a sharp bound for the remaining whole knot period, nor a claim about
the number of repeated boundary visits during a global descent.

## 1. The original source has independent integer transfer coordinates

Use the original complete balanced crossing, with d=N-1. Its two signed
routings are

    (a,b) -> (b+sigma*k, a-sigma*k), sigma=+1 or -1.  (1)

All original kappa, Cartan, pivotal, framing and external factors are
retained. Before splitting states, use the justified whole original
averaged trace

    K_N=chi_N/N Tr[(I tensor g tensor ... tensor g) W_N]. (2)

For a one-component closure its integer closed paths have coordinates

    (t,k_1,...,k_m) in Z^(m+1),                         (3)

with counting Jacobian ONE. Here t is one arc's color. Follow the
oriented physical knot: each crossing's two visits change that color
by opposite multiples of k_j. Every intermediate arc label is therefore
an integer linear form

    ell_r=t+sum_j e_(rj) k_j, e_(rj) in {0,1,-1}.       (4)

Each k_j cancels after its second visit, so the path closes for EVERY
integer transfer vector, and conversely every closed path recovers its
unique t and transfers. An equivalent direct proof propagates symbolic
initial heads through (1). At the end their owners are permuted by a
single cycle P and acquire integral offsets d_r(k). Closure asks
A_r-A_(Pr)=d_r(k). Degree conservation gives sum_r d_r=0 identically,
so these equations solve integrally around that cycle, with one free
common color and no divisibility constraint.

The physical state polytope is exactly

    0<=k_j<=d, 0<=ell_r(t,k)<=d.                       (5)

For the average (2) it has strict real interior: take t=d/2 and every
k_j=eta d with eta<1/(4(m+1)). This is a domain assertion, not a
positivity or noncancellation assertion. A highest-cut t=0 presentation
can have forced faces. Its forced equalities must be removed before
using a free-coordinate interior statement; (2) is justified for the
whole original word, not separately after inserting a current.

This is the explicit knot lattice of
[the scalar cardinal completion](actual_scalar_cardinal_source_completion.md#explicit-knot-coordinates-dimension-and-forced-cut-faces).
It explains why the lower-transfer normals in the following theorem
are independent even after the ORIGINAL closure is imposed.

## 2. Exact singular factor and the regular-head hypotheses

For a positive crossing the original coefficient is

    r_+(a,b;k)=kappa x^(-a-b+k) Q^(b(a-k))
                 Fhat(b+k)Fhat(a)/[Fhat(k)Fhat(b)Fhat(a-k)],
    Q=exp(2pi*i/N), x=-exp(-pi*i/N).                   (6)

The negative one is precisely its balanced conjugate mirror, not a
replacement positive coefficient. Its denominator also contains the
negative-root Fhat_-(k). The exact full-function identity is

    1/Fhat_epsilon(k)=Psi_epsilon(epsilon*h*(k+1))/phi_epsilon,
    h=2pi*i/N, phi_-=conjugate(phi_+).                (7)

Thus the classical lower-transfer normal has the EXACT tag

    xi_j=(k_j+1)/N, u_j=epsilon_j*2pi*i*xi_j.          (8)

It is not legitimate to omit the +1 when locating finite zeros.

Fix a subset J of crossings. Put delta=N^(-alpha), 0<alpha<1, and
assume |xi_j|<=delta for j in J. Every physical head label appearing
in any crossing is assumed to stay in the interior strip

    eta <= Re(ell_r/N) <= 1-eta, eta=N^(-epsilon),
    |Im(ell_r/N)| <= C epsilon log N+C/N.             (9)

Other transfer factorial arguments are regular in their own marked
strips. In particular none of their full-function arguments approaches
one during this operation. More generally it is enough to assume the
regular part G of the original logarithmic action satisfies

    |partial_(xi_j) G| <= C_0+C_word epsilon log N     (10)

on the entire normal tube. Condition (9), the actual five-function
formula (6), and the fixed integer coefficients (4) imply (10).
Indeed every relevant derivative is a fixed combination of
Log(1-Q^ell) and Log(Q^ell), plus fixed lift constants. Interior angular
margin eta bounds the first by O(1+epsilon log N); (9) bounds the
second. The original Cartan Gaussian has the same bound. Constants
depend only on the fixed word and the prescribed tube constants.

If alpha>C_word' epsilon for a sufficiently large fixed word constant,
all heads stay in (9), with slightly weaker constants, when ANY subset
of the k_j is displaced by real distance at most 2N delta. This uses
the finite integer routing coefficients in (4). Thus this hypothesis
can be checked before the move; it is not an assumed unknown period
comparison. In what follows choose alpha so that

    alpha > (C_word+2) epsilon,                       (11)

enlarging C_word to cover those margin changes. Such alpha exists for
all sufficiently small fixed epsilon.

## 3. All retained marks have zero real variation in these normals

The [scalar cardinal source](actual_scalar_cardinal_source_completion.md)
uses fixed powers of

    w^+(s)=A_N(s)+B_N(s) exp(2pi*i*s),
    w^-(s)=B_N(s)+A_N(s) exp(-2pi*i*s).               (12)

Every mode of every window is an INTEGER character of the actual
linear labels (4). Along a real transfer displacement its modulus is
EXACTLY constant, even when the other variables are complex. Hence
these leading integer marks cannot change the downhill sign below.
Their coefficients have only polynomial normal bounds on the
fractional fixed-height edges used here: heads stay in (9), and a
transfer window's digamma poles are a fixed distance from those edges.
No assertion that the modes are harmless on arbitrary macroscopic
complex deformations is made.

Likewise the ORIGINAL full-Psi reset

    Psi_epsilon(u)=(1-exp(Nu))
                              Psi_epsilon(u+epsilon*2pi*i) (13)

retains TWO outgoing sectors. Their relative character exp(Nu), with
u from (8), also has exactly constant modulus along a real k_j shift.
All original norm factors 1-exp(Nu) remain; none is replaced by one.
Integer step shifts leave these characters themselves unchanged.

At outside physical integers the A_N,B_N packets have compensating
poles. Consequently (12) must remain a JOINT packet during the filling.
It is split only on regular outgoing edges. The ensuing statement
about each outgoing sector does not authorize independent pole
crossings for its separated terms.

## 4. Uniform simultaneous downhill at the nested scale

Write the original density's leading exponential as exp(N S), so its
height is Re S. On a continuous marked branch its singular transfer
part has the exact leading form

    S_sing=sum_(j in J) Li_2(exp(epsilon_j*2pi*i*xi_j))
                                      /(epsilon_j*2pi*i). (14)

All other leading terms are G in (10). Along xi_j -> xi_j-s_j with
s_j real and 0<=s_j<=2delta,

    partial_(s_j) Re S
       =log|1-exp(epsilon_j*2pi*i*(xi_j-s_j))|
                                     -Re partial_(xi_j)G
       <= -(alpha-C_word epsilon) log N+C.            (15)

This follows directly by differentiating Li_2. Its real logarithm is
single valued on the punctured normal disk. The exact holomorphic
completion below retains the zero if the path meets it.

Under (11), (15) is <=-c_word log N for all sufficiently large N.
The normals are independent coordinates, so they can be shifted in
any order; no positive circuit arises among them. After shifting each
one by 2delta, its signed full-Psi imaginary coordinate satisfies

    epsilon_j Im u_j' in [-6pi delta,-2pi delta].     (16)

Apply (13) at every outgoing factor and retain the complete 2^|J|
norm packet, together with every cardinal mode. The two-sector
selected-strip calculation in
[the shape-one patch](actual_isolated_shape_one_downhill_patch.md)
shows that the maximum outgoing sector height is at most the
continuously marked height followed in (15). Equivalently, the
branch on either side of the normal cut is the larger of the two
reset sectors; the other one has smaller height. Integer cardinal
characters do not change (15). Therefore EVERY outgoing sector obeys

    Re S_out <= Re S_in -2 c_word |J| delta log N.    (17)

The assertion is local in the stated regular-head tube. It makes no
claim about every sector of the entire original period away from it.

The full quantum factor, including its zeros, has the uniform normal
bound exp[O(N delta(1+|log delta|))+O(log N)]. The regular background
varies by O(N delta(1+epsilon log N)). Cardinal coefficients contribute
only a fixed polynomial factor on the stated edges. Thus the complete
fixed finite patch has additional mass exp(o(N)). These estimates use
alpha<1 and (11); they do not divide by the value of the knot period.

## 5. Exact cotangent filling and source sides

The finite-level reason this is an original-source operation is also
explicit. At a newly crossed integer k_j=-s, 1<=s<N,

    ord[1/Fhat_epsilon(k_j)]=1.

Every head factorial in (6) is nonzero and holomorphic on the interior
strip (9). The remaining transfer factors are regular, so the complete
summand has a zero at k_j=-s. Its full cardinal completion is
holomorphic there too, and has at least that zero. The cotangent pole
is therefore removable. At joint negative integers these statements
hold separately in every free k_j variable; the completed scalar
summand is holomorphic before taking any multivariate residue.

Consequently the old lower side Re k_j=-1/2 can be moved to
Re k_j=-R-1/2, with R=O(N delta)<N, at fixed positive upper/lower
heights, retaining both horizontal connecting pieces. No original
physical integer residue is removed and no new one is added. This
can be performed simultaneously in all j in J, because (3) is an
integer coordinate system. The iterated product-prism Stokes identity
retains every side and corner current with its induced orientation.
The statement is applied to a joint-chain piece on whose ENTIRE
sweep the head margin (9) holds. If the full source is first split
into this regular-head piece and head-endpoint pieces, the new
transverse cutting curtains are part of those side currents. They
are not dropped or declared lower-rate by the present theorem.
For a single translated patch, with sweep S and

    partial S=Gamma_out-Gamma_in-S_side,

the exact identity is

    integral_(Gamma_in) omega
       =sum_outgoing_sectors integral_(Gamma_out) omega_sector
                                      -integral_(S_side) omega. (18)

At outside integer poles the packet is kept combined, as required in
Section 3. Formula (18) does not drop the horizontal connectors or
the side currents of the other original logarithmic/radial factors.
Its residue-free form assumes the sweep stays in Re k_j<0, starting
at the original lower sides as just specified. A patch starting at
POSITIVE transfer coordinates can cross the original poles
k_j=0,1,...,O(N delta). Their original residue currents must then be
added with their orientations. They are not canceled by the windows,
which equal one on physical integers. The existing low-transfer
packet bound controls their operator cost but does not bound an
unrestricted exterior by the knot volume. No generic positive-side
residue deletion is part of this theorem.

A direct finite-step estimate provides an independent check on the
zero side. For k=nu-s on a fractional fixed-height edge,

    1/Fhat(k)=product_(r=0)^(s-1)(1-Q^(nu-r))/Fhat(nu).

For s=O(N delta), its modulus is at most

    N^C [C(s+1)/N]^s.                                (19)

The regular head and Cartan ratios cost at most N^(C_word epsilon*s+C).
All integer characters are invariant under those step shifts. Thus
the far negative edge has the suppressing factor
exp[-(alpha-C_word epsilon)s log N+O(s+log N)], in agreement with
(15). Near the start and on the retained horizontal connectors one
uses the complete bounded normal patch rather than asserts a uniform
strict gap from a face of zero displacement.

## 6. Boundary of the theorem

This supplies a simultaneous downward filling for lower-TRANSFER-only
outer cotangent faces with regular interior heads, in the ORIGINAL
complete closed source at arbitrary braid width. A failure of its
regular-head hypotheses routes
the analysis to a physical head endpoint, another transfer endpoint,
or an escaping/nonregular head chart. It cannot be blamed on an
arbitrary circuit of nine auxiliary atomic variables in this chart.
An interior normal cut may instead retain the original low-transfer
residue packet described above; that current is also not removed.

It does NOT assert that all physical face directions are downhill.
For example at the all-zero head AND transfer vertex, reverse any
strict interior flow. Since the factorial-degree imbalance at either
signed crossing is +k, its logarithmic modulus along that outward ray
has the leading positive increment -k t log t+O(t). Fixed cardinal
characters have unit modulus there. Thus Slater feasibility alone
does not give a downhill direction when head endpoints collide. That
increment is still o(1) at t=N^(-alpha); it is not an excess-volume
counterexample and does not affect (15), where heads are regular.

Global sharp upper bounds still require handling those other faces,
controlling repeated patch/flow visits and their aggregate source,
and retaining the original phase through any chart change. Neither
geometric survival nor the original volume limit is inferred here.

Reproducible free-coordinate, signed phase and exact-window checks:
[audit](../experiments/audit_actual_transfer_only_face_downhill.py).
