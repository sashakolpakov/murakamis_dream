# The actual marked framing density from Casimir-source Ward currents

30 October 2026. local source theorem. This concerns the leading
LOCAL density of the actual complete-color augmented-plat source after
transverse Gaussian elimination. It retains the original mark, all finite
offsets and the actual magnetic top-form. The invariant ordered-flag
form alone is not its density: the marked cut supplies a meromorphic
factor. No coefficient of this local density in the original global
period is asserted.

## 1. Exact white Ward identities on the specified complex-head source

Write Q=zeta^2, d=N-1, m=d-a, B=Q^(-N), and use the actual LARGE
polynomial H=H_m^B(U,V) of the
[generic white-source theorem](actual_generic_boundary_gauge_and_source.md).
With A0=Q^d=1/(BQ), it satisfies the two exact identities

    (1-U)H(U/Q,V)+U(1-V)H(U,V/Q)
                                =(1-UV Q^(-m))H(U,V),       (1)

    A0(U-A0)H(QU,V)+U(V-A0)H(U,QV)
                                =(Q^m UV-A0^2)H(U,V).       (2)

They are polynomial identities in independent complex U,V and generic
Q,B, before root specialization. Thus the actual raising and lowering
intertwiner equations continue to the selected complex head chart;
they are not inferred from agreement on a finite root grid.

Here is an elementary finite proof. Put

    P_j(X)=product_(r=0)^(j-1)(X-Q^r),
    N_b=V^b P_b(U)P_(m-b)(V), H=sum_(b=0)^m c_b N_b.

Each N_b individually satisfies (1), by canceling the endpoint factors
in P_j(X/Q). For (2), subtract its right side and apply the resulting
operator L to one N_b. With M_b=V^b P_b(U)P_(m-1-b)(V), direct
factor cancellation gives

    L N_b=-UV { Q^b(A0-Q^(m-b-1))(Q^(m-b)-1) M_b
                  +A0(A0-Q^(b-1))(Q^b-1) M_(b-1) }.     (3)

The out-of-range endpoint terms have their displayed zero coefficient.
The ACTUAL finite coefficients obey

    c_(b+1)/c_b
       =-B Q^(b+1)(1-Q^(m-b))(1-BQ^(m-b))
                       /[(1-Q^(b+1))(1-BQ^(b+1))].     (4)

Substituting A0=1/(BQ) into (3) makes the coefficient of each M_b
zero by (4). This proves (2) and its endpoints, with every generic
coefficient retained.

To check the source convention, the actual white is

    W_a(i,j;r)=(-1)^m zeta^[-dr+di-m(m-1)]
                         H(Q^i,Q^j)/F_m, i+j=m+r.

The original coproduct F equation is

    (1-Q^i)W(i-1,j;r-1)
       +zeta^(-d)Q^i(1-Q^j)W(i,j-1;r-1)
                                  =(1-Q^r)W(i,j;r),

which is (1). The original Ecal equation gives (2) after multiplying
by UV and its fixed monomial. No small/large root collision is used.
The K equation is the literal affine degree constraint.

The specified cups and inverse caps obey their exact unit-step Ward
equations by the moving-factorial recurrence, with the highest weight
fixed. For example p_L(x)/p_L(x-1) is

    -zeta^(L-2x)(1-Q^x)/(1-Q^(L-x+1)).                   (5)

This makes the two terms in Delta(F)p_L cancel identically. Reversing
the literal cap and using the same recurrence proves its dual equation.
These identities are meromorphic; neither an endpoint pole nor its
normal is deleted. The actual signed circle factors, fixed label weights
and generic scalar adapters are independent of magnetic heads.

## 2. The actual half-index symbols, and their first transport

This section uses the PHYSICAL semiclassical parameter

    h=Log Q=2pi i/N,

not the distinct generic epsilon derivative at one fixed root. Set
A=Q^(u+1/2), q=Log A, and for a fixed highest-weight-L head put
M_L=zeta^(L+1). The row action of its original balanced generators is

    K=M_L/A,
    F=(1-A/zeta)T_-,
    Ecal=(M_L^(-1)-M_L zeta^(-1)/A)T_+,
    T_+ f(q)=f(q+h), T_- f(q)=f(q-h).                    (6)

In the Weyl convention
Op_W[a(q) exp(sp)]f(q)=a(q+sh/2)f(q+sh), their EXACT symbols are

    K=M_L/A, F=(1-A)exp(-p),
    Ecal=(M_L^(-1)-M_L/A)exp(p).                        (7)

Thus there is no order-h subprincipal term in these symbols. At a
complete physical head M_L=-1. Different-head products in the original
coproduct have the same property. A right matrix action uses the
transposed shift; direct substitution gives the same symbol with p
reversed. This retains the input/output operator ordering.

All half-index shifts and the exact parameters
M_L=exp[h(L+1)/2] are kept in the action and amplitude. In particular
L/(2N) and (L+1)/(2N) are not identified near the fold. At each finite
N, change the already proved selected packet to the half-index variables
exactly. Reexpanding it retains the order-one exponential from the
shift of its action, as well as the amplitude and coordinate Jacobian.
The fixed-derivative estimates for that packet justify this operation;
one does not replace it by its limiting phase before making the change.
The finite affine offsets and their characters are exactly those already retained in the
[complete local marked-density theorem](actual_augmented_plat_local_marked_density.md).

The total K equation is an affine head constraint, so a trivalent
tensor is initially supported on that constraint rather than an
ordinary function of three unconstrained positions. Before the next
calculation, take a primitive linear Fourier transform in one constrained
head. Equivalently eliminate the same primitive affine equation with
its full coarea half-density. The retained mixed position/momentum
coordinates then give an ordinary local generating family. The
Fourier normalization is kept as a base scalar and its Jacobian is
kept in the density. This step does not apply an ordinary WKB formula
to a delta-supported tensor or discard the K constraint.

The first transport implication can be proved directly. Suppose
P_h=sum_v a_v(q,h)T^v has Weyl symbol H(q,p)+O(h^2), and
P_h[exp(S/h)(b+O(h))]=0 on a regular local Lagrangian chart. Expanding
the actual shifted amplitude to first order gives, on H(q,S_q)=0,

    V dot partial_q b+(1/2)div_q(V)b=0,
    V=partial_p H(q,S_q).                               (8)

Indeed each term contributes a_v exp(v dot S_q) v dot partial b;
its remaining first correction is half the derivative of that same
coefficient along v, including v^t S_qq v. Their sum is precisely
half the displayed divergence. This is transport of the genuine
Lagrangian half-density, rather than invariance of S alone. Primitive
linear Fourier/constraint coordinates carry the same formula, by the
ordinary Gaussian change of variables with its Jacobian retained.

There is a useful normalization check. On the Hom correspondence
P_out=P_in=P=[k,e;kf,*], the three principal constraint fields are

    X_K=(k/2)A_h, X_E=k A_f,
    X_F=A_e-(f/2)A_h,                                  (9)

where A_xi is actual simultaneous conjugation. In invariant group
volume their divergences are 0,-e,f. Since X_E Log k=-e and
X_F Log k=f, (8) gives k^(-1/2) times invariant half-density,
not bare invariant half-density. Turning the input into an outgoing
leg by the ACTUAL channel cup removes this adapter. For completeness,
in the half-index coordinate u=(r+1/2)/N and lambda=(L+1)/N,
the root cup is

    exp(pi i r) q0^(-r) G_N(r)G_N(L-r)/G_N(L).

The uniform interior sine-factorial expansion makes each numerator
G_N(Nu-1/2)=sqrt(N)exp[N J(u)](1+O(N^-1)). Therefore its variable
amplitude is exp(-pi i u), namely sqrt(K) times a fixed-color scalar.
The exact denominator G_N(L), also near the folded endpoint, stays in
that scalar. This checks the required modular half-density factor
without dropping an endpoint normalization.

Equivalently the all-output vertex (W tensor I)p_(2a) is annihilated
by its original total K-1,Ecal,F. On P_total=I, their fields are
A_h/2,A_f,A_e, so its leading half-density is invariant. Ordinary
caps have the dual property. This supplies a local check of the
assembly below; it is not an assumption that every scalar kernel is
a graph with nonzero mixed input/output Hessian. The latter would be
false for the rank-one complete-circle kernel.

## 3. Actual scalar currents for an arbitrary fixed plat

Keep the original Morse word, all complete-circle sectors, its cups,
caps and the original exposed physical cut. Expand each sector as the
literal W/pi network, or use its proved scalar-one exceptional packet
with its restoring character. Equations (1)--(5) give its actual
intertwiner identities in the independent complex heads. The retained
cyclic turns and categorical duals use their original order. The
exceptional numerator and its restored integer characters obey the same
unit-step identities: an integer-affine exp(2pi i head) character is
unchanged by every such shift.

Compose the original Hopf-adjoint insertions through this network.
There is an explicit finite scalar-current construction. Move each
inserted K,Ecal,F through the next vertex using the displayed local
identity; pair the two insertions on each contracted wire with its
actual cup or cap. Keep every resulting multiplication coefficient.
For a shifted factor c and an insertion j the reindexing is exactly

    j T^v c-(T^(-v)j)c
                         =(T^v-I)[(T^(-v)j)c].          (10)

Thus each unmatched internal term is a specified integral difference
current, with its insertion shifted in the OPPOSITE direction.
Use the original saturated affine head lattice to express these
translations in a primitive free basis. The local degree equations
ensure that the matched current has zero remaining constraint defect.
No independent edge maximization or cyclic wrapping is involved.

Ordinary pivotal contractions cancel the matched Hopf insertions.
The only cut terms are the literal dual rows of the original mark,
computed in the next section. This is the same finite Green-product
construction as in the [ordered Gaussian-current calculation](residual_gaussian_ward_currents.md),
but here its local inputs are the independent-head Casimir identities
(1),(2), not a braid mixed-Hessian model. The construction is an
algorithm on the actual word and works at every fixed width and both
level parities. It retains finite endpoint currents on an original
finite domain. In the local regular meromorphic chart it is the
corresponding interior current identity; no claim identifying that
completion with the whole cyclotomic source is needed below.

The principal vector of a local insertion is obtained by differentiating
its ACTUAL symbol with respect to p: expansion of a shifted amplitude
gives sum_v h_v exp(v dot p)v. Equations (7)--(9) therefore identify
the local variations as the actual conjugation fields on its trivalent
correspondence. Their propagation through the original shared heads
agrees with the explicit incidence/momentum inverse of the
[critical-scheme theorem](actual_augmented_plat_critical_scheme.md).
On the regular complete geometric germ they are tangent to that exact
critical scheme. The two cut-compensated combinations below are its
two actual framing fields. This uses the source critical-scheme inverse,
not merely constancy of the critical action.

## 4. The actual marked co-source, including its sign

Use the original balanced cut e_ab=1/N. The one-cut array is diagonal
term by term after the other actual caps, by total-degree conservation.
For Phi(C)=Tr(eC), the exact dual Hopf rows are

    e_K=K^(-1)eK-e,
    e_E=K^(-1)e Ecal-Ecal K^(-1)e,
    e_F=eF-KF e K^(-1).                                (11)

At complete color, with A=Q^a in the original integer-index convention,
their diagonals are

    (e_K)_aa=0,
    (e_E)_aa=q0(1-Q)A/N,
    (e_F)_aa=(1-Q)A/N.                                (12)

These follow by two neighboring matrix entries, with the actual zero
end arrows retained. The original scalar summand already contains 1/N.
Consequently the boundary coefficients for

    W1=2(ad_K-I)+2ad_Ecal, W2=ad_F+ad_Ecal

are b1=2q0(1-Q)A and b2=(1+q0)(1-Q)A. Both satisfy

    b_i/h -> -2 A.                                     (13)

The half-index replacement changes A only by 1+O(h), so not this
leading co-source. This is a ROOT physical semiclassical statement;
it does not identify any generic epsilon-normal of a bare marked row.

Normalize the cut momentum to one as in the actual critical-scheme
slice, and use

    F(r,s)=[[r,1-r],[s,-s]],
    mu=F^(-1)[[1,1],[0,1]]F,
    A_cut=(1+s)^(-1).

The two actual fields, with the same conjugation convention, are

    xi1=-2(1-r)partial_r+2s partial_s,
    xi2=(2r-1)partial_r+2s partial_s.                   (14)

Their determinant is -2s, a unit on this chart. Their difference is
partial_r. The exact residual difference current has boundary row
(1-q0)(1-Q)A/N, so its divided leading co-source is zero.

The ordinary-cap comparison also exposes the marked insertion
directly. At the exposed pair, with SECOND physical index x, its exact
mark/cap ratio is N^(-1)q0^(-d^2)Q^(d x). Since d=N-1,

    Q^(d x)=exp(2pi i x) exp(-2pi i x/N).                (15)

The first factor is the retained integer character. On complementary
integer indices a+x=d, the second is Q times the first integer clock
Q^a (or its corresponding fixed half-index scalar). Up to that retained
fixed-color scalar its leading factor is A_cut. Thus the marked source has a
genuine A_cut insertion, not a constant Haar normalization. Equation
(12) computes its differential covariance from the actual source.

## 5. Gaussian elimination transports the divergence and its Jacobian

Use the selected ordinary packets and the joint deficient packet at
the proved regular geometric frame. The complete marked-density theorem
gives their nonzero relative product amplitude with its original magnetic
top-form. The positive-certificate critical scheme gives exactly two
magnetic null directions; all transverse magnetic Hessians are units.
Keep two actual free magnetic coordinates chi which are etale on this
framing orbit, and call the remaining coordinates u. One chi can be
chosen to include the actual cut head. Keep every original finite offset,
Poisson character and constant phase in this same branch.

Contract only u by its local geometric Gaussian. This defines the
leading two-form Omega_src: its coefficient is the actual product
amplitude divided by the marked square root of det(-F_uu), with the
full chi/u Jacobian and original magnetic top-form retained. The new
local packet theorem makes this form NONZERO. This construction does
not choose a component of the original global integration cycle.

For clarity, the effect on a current can be checked without an invariance
guess. A term j(chi,u,h)T_chi^gamma T_u^beta in the exact current has
Gaussian image obtained by replacing its insertion by

    E_(chi+h gamma)[T_u^(-beta)j]

and then shifting the external Gaussian block by h gamma. The insertion
is translated oppositely, exactly as in (10). This is the substitution
u_new=u+h beta with the local critical point recentered. Equivalently
one proves the required leading identity by Gaussian integration by
parts. Normal total currents have zero formal Gaussian integral; an
external current has leading coefficient xi_i^chi times the Gaussian
density. Its external divergence differentiates that WHOLE density,
including the inverse Hessian determinant and coordinate Jacobian.
No separately averaged product of insertions is substituted.

The source packets are holomorphic on a common smaller chart with
relative O(h) errors and fixed-derivative bounds. These justify the
first transport expansion of the actual continued factors; unknown
higher amplitude coefficients cancel from the leading current because
its principal characteristic vanishes. A local descending normal
Gaussian cycle gives the same leading computation. Its small outer
boundary is exponentially below the critical value. None of these
local operations moves the original finite-head cycle across a source
divisor.

Combining this calculation, the actual principal fields (14) and the
explicit boundary rows (13) gives

    Lie_(xi_i) Omega_src-2 A_cut Omega_src=0, i=1,2.      (16)

This is the missing subprincipal transport statement. It was obtained
from (1)--(13) and the original product amplitude, not inferred from
invariance of the stationary action or from the old braid determinant.

## 6. The resulting orbit form and its scope

Put

    Omega_cut=-dr wedge ds/[s(1+s)].                     (17)

Direct differentiation gives Lie_(xi_i)Omega_cut=2 A_cut Omega_cut.
Divide (16) by this nonzero form. Both independent vector fields kill
the ratio, so on a connected geometric framing chart

    Omega_src=c_D Omega_cut, c_D!=0,                    (18)

where c_D is independent of the framing point. It retains the original
source's base-only normalization, phases, parity convention and chosen
Gaussian square roots. The theorem does not choose or erase these data.
The local channel Gaussian multiplies c_D by its nonzero cusp-shape
factor, since the cusp shapes and its marked Hessian are frame-invariant.
Thus the actual local folded sum at either parity has the same orbit
form, with its own retained nonzero constant.

In the ordered-flag convention Pi=g^(-1)E11 g, with image v and
kernel w, let Omega=dv wedge dw/(v-w)^2. For g=F^(-1),

    Pi=[[r,r(1-r)/s],[s,1-r]],
    w=(r-1)/s, 1/(v-w)=s,
    Omega=dr wedge ds/s.

Consequently the ACTUAL marked answer is

    Omega_src=-c_D A_cut Omega.                         (19)

The insertion at 1+s=0, the omitted s=0 chart, and all source-chart
divisors remain. No nonconstant additional local factor survives the
two proved Ward equations, but this says nothing about residues at
the excluded boundaries or contributions from other WKB sectors.

In particular, formal Gaussian current transport is not an invertible
map on all fixed-root carry sectors: at h=2pi i/N the Bernoulli adapter
for exp(hD)-1 vanishes on a literal A^N character. These source sectors,
normal directions and original cotangent weights are not removed by
(18). The selected global framing period, its boundary/current map,
and its coefficient in the original finite cycle remain separate.

There is a concrete residual-fiber consequence. Since
A_cut=(1+s)^(-1), the same proved density is

    Omega_src=(c_D/s) dr wedge dLog A_cut.              (20)

Relative to the displayed base form dLog A_cut, its differential on
a fixed affine framing fiber is c_D dr/s=c_D d(r/s). It is exact.
Thus a specified first-cut localization in A_cut, with its actual base
coefficient retained, does not by itself produce a nonzero closed
period of this residual leading form. Its contribution requires the
original relative boundary/current coefficient or other retained
source weight. Equation (20) neither chooses a centralizer section
nor discards the original cotangent, character or divisor terms.

## 7. Finite source checks

The [focused exact audit](../experiments/audit_actual_augmented_plat_framing_density_source_ward.py)
and [results](../experiments/actual_augmented_plat_framing_density_source_ward_results.json)
check 14 termwise F identities, 14 E telescopes and 10 adjacent
coefficient cancellations; 300 original H four-jet identities with
1,200 retained coefficients; 570 actual cup four-jet ratios; and
308 truncated complete cut-row diagonals. Symbolic checks also retain
the exact Weyl half-steps, root cup phase, three modular divergences,
two cut-field covariances, flag Jacobian and marked finite clock offset.
A variable Gaussian and a coordinate change separately check the
transverse determinant derivative and full top-form Jacobian. The
general finite-current construction and its Gaussian transport are
proved analytically in §§3--5, not inferred from these checks.

The conclusion is the local framing form (18)–(19). Its global cycle coefficient and boundary currents remain unproved; no global period statement follows.