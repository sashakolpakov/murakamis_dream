# The actual ordinary packet on the full strict physical tube

30 October 2026. A second exact Hermitian realization of the original
q-Hahn determinant puts its zeros in a sharp angular cone. It extends
the ordinary joint action and nonzero relative amplitude from the
central wedge to the FULL strict physical tube. Both magnetic
coordinates vary complexly; the channel remains an actual integer.

The finite source has a small upper-boundary correction, which is
necessary: an explicit one-channel counterexample is given below.
Every fixed compact in the full physical tube is covered for all
sufficiently large N. No contributing global cycle or coherent
whole-source estimate is asserted.

## 1. Exact source and a second determinant

Put theta=pi/N, q=exp(i theta), Q=q^2, d=N-1 and
1<=j<=floor(d/2). Write

    t=N tau, u=N nu, xi=j/N,
    z=exp[pi i(tau-2nu)], gamma=pi(tau+1/N).

The original joint source is exactly

    fhat_j(u,t-u)=x^u q^(jt) [2j choose j]_Q
                  R_j(z;-cos gamma)/Delta_j(Q^t),
    x=q^d, Delta_j(T)=product_(r=0)^(j-1)(T-Q^r).       (1)

All powers and scalar factors are those of
[the original joint amplitude theorem](actual_q_hahn_joint_complex_amplitude.md).
Let

    b_n=sin^2(n theta)/[cos^2(n theta)
                        sin((2n-1)theta)sin((2n+1)theta)].

The exact monic recurrence is

    R_0=1, R_1=z+c/cos(theta),
    R_(n+1)=[z+c/(cos(n theta)cos((n+1)theta))]R_n
                  +b_n[cos^2(n theta)-c^2]R_(n-1).     (2)

Define j-by-j real matrices A and K, indexed by 0,...,j-1:

    A_(n,n)=1/[cos(n theta)cos((n+1)theta)],
    A_(n-1,n)=A_(n,n-1)=sqrt(b_n)sin(n theta),
    K_(n-1,n)=sqrt(b_n)cos(n theta),
    K_(n,n-1)=-sqrt(b_n)cos(n theta), K_(n,n)=0.

Then the SAME polynomial has the second exact determinant

    R_j(z;-cos gamma)=det[zI-cos(gamma)A-sin(gamma)K].   (3)

Indeed the upper and lower adjacent entries of
J_gamma=cos(gamma)A+sin(gamma)K are
sqrt(b_n)sin(n theta+gamma) and sqrt(b_n)sin(n theta-gamma).
Their product is b_n[cos^2(gamma)-cos^2(n theta)],
so the continuant of zI-J_gamma is exactly (2).

The two Hermitian matrices

    H_+=A+iK,                   H_-=A-iK              (4)

are POSITIVE DEFINITE. Their adjacent entries have modulus sqrt(b_n)
and their diagonal equals that of the proved positive matrix D in
[the first determinant theorem](actual_q_hahn_joint_accretive_determinant.md).
A diagonal unitary phase gauge makes each of these tridiagonal
offdiagonals positive real. Thus each H_+ and H_- is unitarily
equivalent to D, including the maximal channel. Consequently

    J_gamma=(e^(i gamma)H_-+e^(-i gamma)H_+)/2.         (5)

This is a source-exact matrix identity, not an asymptotic model.

## 2. A sharp finite angular exclusion, and its necessary correction

For any eigenvector v of J_gamma with norm one, its eigenvalue is

    zeta=(h_-/2)e^(i gamma)+(h_+/2)e^(-i gamma),
    h_-=v*H_-v>0, h_+=v*H_+v>0.                     (6)

If pi/2<Re gamma<3pi/2, these two rays bound a left angular cone.
Put a_gamma=min(Re gamma,2pi-Re gamma). Every nonzero eigenvalue
satisfies |Arg zeta|>=a_gamma; the inequality is strict when the
two boundary rays are distinct. When Re gamma=pi all eigenvalues
are strictly negative real. Positive coefficients in (6) also
exclude a zero eigenvalue in this range.

Define the full physical tube

    P={ (tau,nu) in C^2:
                  1/2<Re tau<1, 0<Re nu<Re tau },

and its finite-level subdomain

    P_N={ (tau,nu) in P: Re tau<1-1/(2N) }.            (7)

For a physical point the principal argument of z in (1) is exactly
pi(Re tau-2Re nu), with absolute value <pi Re tau. On P_N,
a_gamma>pi Re tau. Therefore (3) is nonzero there. The factors
Delta_j(Q^t) are also nonzero: their zeros require tau=r/N modulo
an integer, 0<=r<j<N/2. All remaining factors in (1) are nonzero.
Thus the original finite source is holomorphic and nowhere zero
on P_N. The case j=0 is its explicit nonzero exponential.

The correction in (7) cannot simply be deleted for every finite N.
Already j=1 has its zero at

    z_N=cos[pi(tau+1/N)]/cos(pi/N).

Take tau_N=1-1/(4N)+i and delta=3pi/(4N). Then

    z_N=[-cos(delta)cosh(pi)+i sin(delta)sinh(pi)]/cos(pi/N),
    Arg z_N=pi-arctan[tan(delta)tanh(pi)]
                                <pi Re tau_N.         (8)

For the strict inequality, set a=pi/(4N):
tan(a)/tan(3a)<1/3<tanh(pi), valid for N>=3. Define
nu_N=[tau_N-Log(z_N)/(pi i)]/2 with the principal logarithm.
It satisfies 0<Re nu_N<Re tau_N, but (1) vanishes. The denominator
is nonzero. This is an exact finite-source counterexample on P.
These points approach the boundary of P as N grows and therefore
do not obstruct the fixed-compact theorem below.

## 3. Uniform inverse and logarithmic bounds on full physical compacts

Fix a compact K0 contained in P. For all large N, K0 lies in P_N
and gamma has real part between pi/2 and pi. Put

    M=zI-(e^(i gamma)H_-+e^(-i gamma)H_+)/2.

The three coefficients z, -e^(i gamma), -e^(-i gamma) lie in one
open half-plane through zero. To see this, write
a=Re gamma and psi=Arg z. The latter satisfies |psi|<a.
The other two arguments are pi-a and -(pi-a). Their angular
span together with psi is strictly less than pi. On a fixed
physical compact the span stays uniformly below pi, because
Re nu and Re(tau-nu) are bounded below and Re tau stays away
from 1/2 and 1. Their moduli also have positive lower and finite
upper bounds on K0. Rotate the half-plane by a phase beta. Locally,
and uniformly on a finite cover of K0, this gives

    Re(e^(-i beta)M)>=delta I+eta_- H_-+eta_+ H_+,
                    delta,eta_-,eta_+>=c_(K0)>0.      (9)

Hence ||M^(-1)||<=C_(K0). Conjugating M by H_+^(-1/2), or by
H_-^(-1/2), also gives

    |tr(M^(-1)H_+)|+|tr(M^(-1)H_-)|<=C_(K0)j.

Since partial_z M=I and
partial_gamma M=-(i/2)e^(i gamma)H_-+(i/2)e^(-i gamma)H_+,
both logarithmic derivatives of R_j with respect to z and gamma
are O_(K0)(j). No lower eigenvalue bound for D, H_+ or H_- is
used. The result is uniform through the folded channel.

The scalar factors in (1) have the same explicit O(N) logarithmic
derivative bounds as before. Thus the first derivatives of
N^(-1)Log fhat_j are uniformly bounded on full physical compacts.
Choose its scalar holomorphic logarithm on the convex P_N by
continuation from its already fixed central value. The exact real
center phase remains

    Im Log fhat_j(t/2,t/2)=pi[d(t-j)+j^2]/(2N).        (10)

The principal matrix logarithm of the old central realization is
not being asserted outside its domain. A central anchor bounds
the continued normalized scalar logarithm, and Cauchy estimates
give all its fixed derivatives on smaller physical compacts.

The normal-family argument now extends the ACTUAL selected leading
action throughout P. Any subsequential limit agrees on the central
open subset with the already proved Phi_xi, and hence everywhere
by the holomorphic identity theorem. This gives local uniform
convergence with all derivatives, uniformly for xi=j/N in compact
real subintervals of (0,1/2], always using its actual value.

## 4. The characteristic is simple on the entire tube

Set gamma0=pi tau, s=sin(pi xi), C=cos(pi xi), and

    W=1-2cos(gamma0)z+C^2 z^2,
    V=1-2cos(gamma0)z+z^2.                            (11)

Both are nonzero on P. This has a two-dimensional positive-cone
proof which includes C=0. Let u=(1,0)^T, v=(s,C)^T and

    B_gamma0=e^(i gamma0)u u*+e^(-i gamma0)v v*.

Its trace is 2cos(gamma0), its determinant is C^2, and

    det(I-z B_gamma0)=W.

Every nonzero eigenvalue is a NONNEGATIVE combination of the
same two left-cone rays, with at least one positive coefficient.
It therefore lies in the closed cone |Arg lambda|>=pi Re tau.
Reciprocation preserves that cone, so its reciprocal cannot be
the physical z, whose argument has smaller absolute value. This
proves the assertion for W. Taking s=0,C=1 proves it for V.

The full source characteristic from the exact Casimir shift is

    H=A(Y+Y^(-1))+D-(J+J^(-1))=0,
    A=(U-T)(1-U)/T, D=2U(1+T-U)/T,
    U=e^(2pi i nu), T=e^(2pi i tau), J=e^(2pi i xi).

Here A!=0 on P, and xi is bounded away from zero. Its two
solutions are

    Y_+=(s z+i sqrt(W))^2/V, Y_-=(s z-i sqrt(W))^2/V.   (12)

The square root is the holomorphic continuation from the selected
central branch on the simply connected P. It is NOT necessarily
the pointwise principal square root outside the central wedge.
The numerators in (12) are nonzero because W+s^2 z^2=V. The two
roots are distinct because s,z,W,V are nonzero. Thus H_a!=0 for
a=Log Y on the selected sheet throughout P, including xi=1/2.
The second source characteristic remains simple in Phi_tau:
its derivative is (1-T)exp(Phi_tau), which is nonzero. The leading
action in section 3 already supplies this actual holomorphic
logarithm, rather than selecting a new solution of that equation.

## 5. The actual nonzero amplitude, with its original normalization

The two finite source shifts (11),(12) of
[the original joint amplitude proof](actual_q_hahn_joint_complex_amplitude.md)
are rational identities for the SAME finite function (1). They
therefore hold on the enlarged domain. The proof's two derivative
bootstraps now apply on full physical compacts: the preceding
section supplies uniform characteristic simplicity, and section 3
supplies uniform Cauchy bounds on slightly larger compacts.

Explicitly let G_N=N^(-1)Log fhat, a=Phi_nu and b=Phi_tau.
The exact Casimir shift first gives partial_nu G_N-a=O(N^(-1));
Cauchy's formula gives the same bound for its derivatives. A
second substitution gives

    partial_nu G_N=a+N^(-1)r+O(N^(-2)).

The exact coproduct shift then gives, by the same two substitutions,

    partial_tau G_N=b+N^(-1)s1+O(N^(-2)).             (13)

Here r and s1 are EXACTLY the coefficients (16),(17) in that proof,
with its original integer offsets and actual xi=j/N. Their formulas
are holomorphic on P by the simplicity just proved. The errors
and their fixed derivatives are uniform on smaller compacts.

The one-form s1 d tau+r d nu is closed: equate the mixed derivatives
of the actual G_N in (13), use Cauchy bounds on the remainders,
and pass to admissible xi sequences. The coefficient functions
depend locally analytically on xi by the simple characteristic
and their already normalized central values. Thus closedness holds
at every real xi in the stated interval, including its folded end.

On the simply connected P this form defines a nonzero holomorphic
B_xi, normalized by the ALREADY PROVED central real-lattice amplitude.
Integrating (13) from a nearby genuine central sample along compact
paths gives

    fhat_j(Nnu,N(tau-nu))
       =N^(-1/2) B_(xi_N)(tau,nu)
              exp[N Phi_(xi_N)(tau,nu)](1+O(N^(-1)))   (14)

on every compact subset of P. Fixed derivatives of the relative
error have the same bound on smaller compacts. At the initial
sample Log fhat-N Phi+(1/2)log N-Log B is O(N^(-1)), and its
gradient has that same bound by (13). Thus no additive phase,
sample character, or normalization constant is introduced during
continuation. In the original overlap B is the exact coefficient
Acal(w_*)exp[pi i(alpha(w_*)-nu)] from the central proof. Both
level parities, arbitrary fixed complex magnetic displacements,
and the discrete folded limit are included.

## 6. The generic-normal bounds use the same enlarged corridor

The proved small-channel generic-normal and near-fold paired-normal
bounds also extend to any fixed compact K0 in P. There is one
necessary change in their matrix perturbation argument.

Use M in (9) as the root tridiagonal realization. For each adjacent
pair, freeze whichever of its two root entries has larger modulus,
and set the opposite generic entry so their product is -beta_n(q)
in the original generic recurrence. One must not always freeze
the upper entry: sin(gamma+n theta) can vanish at an integer degree.
The chosen entry is uniformly bounded below because sqrt(b_n)>=1/2
and

    |sin(gamma+n theta)|^2+|sin(gamma-n theta)|^2
      =2|sin gamma|^2 cos^2(n theta)
                         +2|cos gamma|^2 sin^2(n theta).

On fixed physical compacts, for all large N, both |sin gamma| and
|cos gamma| are bounded below. Therefore the larger adjacent entry
has a positive uniform lower bound. The diagonal is unchanged.
The old generic coefficient bounds give ||M(q)-M(q0)||=O(N^7|epsilon|),
and (9) supplies the bounded root inverse. All scalar factors and
their derivatives retain their former estimates.

It follows that the original small-channel N^8 fixed-jet bound
holds on K0. Its last inverse cofactor still equals R_(j-1)/R_j,
so the EXACT large-channel recurrence and scalar argument of
[the near-fold theorem](actual_q_hahn_near_fold_complex_partner_bound.md)
give the same paired bound

    |w_(j,l)/C_j|<=C_(K0)N^8(C_(K0)N^16)^(l-j)        (15)

when l-j<=eta_(K0)N. Thus its subexponential consequence for
(l-j)log N=o(N) holds on the full strict physical tube's fixed
compacts as well. The fixed positive scaled-channel limitation
and the distinction between an upper bound and an amplitude
remain unchanged.

## 7. Scope

The ordinary local packet now covers the full strict physical
domain, and its selected sheet is continued from the original
central source. Membership in that physical domain, matching the
geometric sheet, choosing a contributing original cycle, and
controlling the coherent contraction remain separate global tasks.
The finite boundary example (8) explains why the theorem is stated
on fixed compacts for sufficiently large N rather than by deleting
the exact finite correction everywhere.

Focused audit: [cone, literal source and full physical amplitudes](../experiments/audit_actual_q_hahn_full_physical_complex_packet.py),
with [saved results](../experiments/actual_q_hahn_full_physical_complex_packet_results.json).
The three formal cone identities and 242 exact actual-source
determinants passed. Six explicit finite-boundary counterexamples
were checked. Eight original generic adapters passed, including
four cases with a genuinely vanishing upper root entry. At 180
digits, 16 independent terminating-source comparisons and 16
amplitude calibrations strictly OUTSIDE the central wedge passed;
16 actual subprincipal gradient corrections also passed. The
largest N-scaled relative amplitude error was 1.184 and the largest
N-squared gradient remainder was 16.406. These are normalization
regressions; the cone and two-shift argument give the uniform result.

The theorem has fixed-compact, discrete-channel scope. It does not identify a global contributing cycle or give a coherent source estimate.

The finite-boundary caveat remains essential, including for the larger-entry generic adapter.