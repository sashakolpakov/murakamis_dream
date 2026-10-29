# The full dilogarithm resolves the actual charged flag pentagon at the root

28 October 2026. The full modular dilogarithm has an actual finite
marked realization at the charged cup. Its values at the marked
clock spectrum are regular and invertible at the physical root.
They implement a mixed full-Phi/nilpotent pentagon with its
original source factor nonzero and of modulus sqrt(N).

The integer mark is fixed by an explicit operator preparing the
original cup, not by an arbitrary choice of a cyclic spectral
cut. This removes the singular norm-root factors in the earlier
[mixed cyclic/nilpotent pentagon](actual_shared_quantum_flags_and_charged_exchange.md).
It does not realize all three classical five-point certificates
inside the original crossing or choose its geometric period.

## 1. The exact full function and its marked unit-root values

Use the full literature function with the normalization proved in
[the rational evaluation](rational_quantum_dilogarithm_torsor.md)
and retained in
[the exact circle/boundary source](actual_modular_dilog_circle_and_boundary_source.md).
Write Q=exp(2pi*i/N), d=N-1, and

    Psi(z)=V_N(exp z)(1-exp(Nz))^((N+1)/(2N)+i z/(2pi))
                     exp[i Li_2(exp(Nz))/(2pi N)],
    V_N(t)=(1-t^N)^(d/(2N))
                    product_(ell=1)^d(1-Q^ell t)^(-ell/N). (1)

All marks are anchored at Re z=-infinity, as in those notes.
In particular

    Psi(z+2pi*i/N)=Psi(z)/(1-exp z).              (2)

For j=1,...,N the points z_j=2pi*i*j/N lie in the
interior or top boundary of the selected strip. They are
regular and nonzero, including j=N. The bottom point
z=0 is a zero and is deliberately a different mark.
Repeated use of (2) gives

    Psi(2pi*i*j/N)=phi_N/F_(j-1),
    F_a=(Q;Q)_a,
    phi_N=Psi(2pi*i/N)
      =sqrt(N) exp{i pi[1/4-(N+N^(-1))/12]}.       (3)

This fixes the scalar and phase, including even levels.
Here is a direct proof of the scalar. In (1) approach
z=log r+2pi*i/N with r increasing to one. Its central
zero cancels the ell=d factor. The resulting anchored
finite product is

    phi_N=N^(d/N) exp[i pi/(12N)]
                     product_(ell=1)^(N-2)
                          (1-Q^(ell+1))^(-ell/N). (4)

For 1<=a<N the anchored argument of 1-Q^a is
pi*a/N-pi/2. Summing the arguments in (4) gives the
phase in (3). For the modulus, either pair complementary
factors in (4), or use the exact radial identity

    |Psi(log r)|^2=(1-r)(1-r^N).

Equation (2) then yields
|Psi(log r+2pi*i/N)|^2=(1-r^N)/(1-r), which tends
to N. This proves (3) with no unspecified root phase.
The negative orientation is the conjugate-reflected
formula with the opposite phase.

## 2. The actual coupled flag oscillator has a fixed integer mark

Take the complete original heads, with x=-q^(-1),
lambda=x^(-1)=Qx, k=x^N=(-1)^(N-1), and typed
cyclic marks S_1^N=mu, S_2^N=k mu. In the notation
of [the actual shared flags](actual_shared_quantum_flags_and_charged_exchange.md),

    Delta=f_1+K_1^(-1)S_2-S_1,
    gamma=-e_2K_1,
    v=Z_2^(-1)+S_1e_2,

    Delta v=QvDelta, v^N=1, Delta^N=gamma^N=0,
    gamma Delta=lambda(Q^(-1)v-1).               (5)

Let E_j(v) be the v=Q^j spectral projectors, with
E_N=E_0. Then

    Delta E_1(v)=0.                              (6)

For example (5) makes Delta injective on every E_j
with j!=1. If Delta E_1 were nonzero, the remaining
N-1 injective arrows would contradict Delta^N=0.
There is a direct actual preparation of this cut. Put

    A=-S_1e_2Z_2, C=P(A),
    P(A)=sum_(h=0)^d (-1)^hQ^(h(h-1)/2)A^h/F_h. (7)

These use the actual finite e_2; A^N=0. Then

    v=C Z_2^(-1) C^(-1),
    Delta=C(K_1^(-1)J_(+,2))C^(-1),
    C gamma=gamma C.                             (8)

Here J_+ is the literal strict raising shift on the
second head. The first identity follows from the finite
Euler recurrence: A Z_2^(-1)=Q^(-1)Z_2^(-1)A, so
conjugation gives Z_2^(-1)(1-Q^(-1)A)=v. The third
follows by direct commutation of A with -e_2K_1.
For the second, both proposed raising operators obey
(5) with the same gamma and v. Their difference has
image in ker(gamma), and their clock covariance
therefore allows only the E_1 input. Both vanish on
that input, by (6) and the literal endpoint of J_+.
Thus their difference is zero.

For the original cup p of the preceding notes, exactly

    p=N x^(-d) C|0,d>.

Indeed the coefficient of |h,d-h> in C|0,d> is x^h,
by the ordinary factorial reflection. Consequently

    J_v=sum_(j=1)^N j E_j(v)=C(N-J_2)C^(-1),
    [J_v,Delta]=-Delta,
    J_v p=p,
    (J_v+J_1+J_2)p=Np.                           (9)

The actual cap and the actual integer source charge fix
this mark. Equation (9) is not an identification of J_v
with an arbitrary interior Pachner edge winding.

## 3. An invertible marked full-Phi matrix at the physical root

For t positive near one, with its indicated logarithm,
define

    F_v(t)=sum_(j=1)^N
                 Psi(Log t+2pi*i*j/N) E_j(v).    (10)

This is a marked evaluation, not a single-valued
cyclic functional calculus that identifies the top
and bottom logarithmic values at eigenvalue one.
All coefficients in (10) are holomorphic and nonzero
near t=1. Hence F_v(t) and its inverse are regular
there. The elementary shift (2), applied only to the
nonzero arrows Delta:E_j->E_(j-1), j>=2, gives

    F_v(t)Delta F_v(t)^(-1)
                        =Delta(1-Q^(-1)t v).     (11)

There is no exceptional wrap to check: (6) is the
actual missing arrow, not an arrow removed by hand.

At t=1, write F_v=F_v(1). Equations (3) and (8) give
the explicit original-head realization

    F_v=phi_N sum_(j=1)^N E_j(v)/F_(j-1)
       =phi_N C diag_b[1/F_(d-b)] C^(-1),
    F_v p=phi_N p.                               (12)

The phase and modulus of phi_N are those in (3).
In particular the selected source coefficient is
nonzero and polynomial in size at every N.

The relation to the old norm-one cyclic atom is exact.
Let nu^N=1-t^N and let C_t=V_N(tv) with its anchored
cyclic functional calculus. Then

    F_v(t)=B(t) nu^(-J_v) C_t,
    B(t)=(1-t^N)^((N+1)/(2N)+i Log t/(2pi))
                         exp[i Li_2(t^N)/(2pi N)]. (13)

Thus the full modular factor supplies an **integer
degree gauge**, rather than just a central scalar.
The apparent singular factors in (13) combine to the
regular marked matrix (10). Dropping nu^(-J_v) would
return the singular rescaled cyclic pentagon.

The preparation C itself has a contractive core at unit
marks. Let H_A act on the second head by
H_A|b>=lambda^(-b)|b>/F_b. Then

    A=H_A(S_1 tensor J_minus)H_A^(-1).

Both C=P(A) and C^(-1) are therefore factorial frames
around a literal norm-one nilpotent shift. Their Euler
factor and their inverse are the original full-Psi
relative moments at the appropriate orientation; their
diagonal factorial frames are reflected or ordinary
moments as in Section 5 below. Thus (12) has an exact
fixed-complexity full-Psi period presentation with the
same polynomial boundary-kernel types as the original
word. This is not a polynomial norm bound for C or F_v:
their exponential actions remain in the full functions.

## 4. The actual physical-root mixed pentagon and its source

For every scalar a, the finite Euler polynomial of the
original root satisfies

    F_v P(aDelta)
       =P(aDelta)P(-aQ^(-1)Delta v) F_v.         (14)

Indeed (11) conjugates the left Euler argument to
aDelta-aQ^(-1)Delta v. The two summands Q-commute.
The finite ordered binomial theorem gives their Euler
factorization; every term of total Delta-degree >=N
vanishes. This proves (14) independently of an assumed
published operator pentagon, at the physical root and
with the actual original endpoints.

Keep the full original marked cap m, with mp=1.
Because Delta p=0 and vp=Qp, both sides have exactly

    m F_v P(aDelta)p
      =m P(aDelta)P(-aQ^(-1)Delta v)F_vp
      =phi_N.                                   (15)

Every original common Cartan, framing and peripheral
line remains identical outside (15). The scalar phi_N
has not been reset to one. This is a physical-root
source-compatible mixed pentagon, with no free
auxiliary t and no singular norm-root specialization.

The nilpotent P factors can each be replaced by their
exact full-Psi circle/radial periods. Since their series
truncate, this is a finite linear replacement carrying
all relative boundary components. It does not yet
prove a homology pushforward between two unspecified
full-Faddeev face networks or identify their geometric
intersection coefficient.

## 5. The literal middle-five-point source gauges lie in the same class

The [literal middle configuration](actual_middle_five_point_wall_factorization.md)
requires the original argument n=e_1S_2, the corrected
reciprocal U, and its explicit diagonal Gamma. These
have a common **contractive** transfer, not an
uncontrolled nonnormal one. Put

    T=J_(minus,1) tensor S_2,
    H_n|j>=lambda^j c_j^+|j>,
    H_U|j>=lambda^j F_j|j>,
    c_j^+=(-1)^jQ^(j(j-1)/2)/F_j.

Then

    n=H_n T H_n^(-1), U=H_U T H_U^(-1),
    Gamma=H_U H_n^(-1),
    H_U=N lambda^(-d)Q^(-1) Rev H_n Rev,         (16)

where Rev|j>=|d-j>. Each identity follows from its
consecutive coefficient ratio and includes the strict
zero endpoint. For unit S_2, ||T||<=1.

Let c_a^- be the corresponding Euler coefficient at
Q^(-1). Finite factorial reflection gives

    Gamma_j=N^2 Q^j c_(d-j)^+ c_(d-j)^-,
    Gamma_j^(-1)=Q^(-j)c_j^+ c_j^-.              (17)

Each c_a^epsilon is exactly the one-full-Psi circle
minus radial source of the modular-circle theorem.
Thus both Gamma and its inverse are two-full-Psi
relative periods. At radius one their boundary kernels
are unit phase/power diagonals, with only the displayed
N^2 scalar. For reflected coefficients, the radial
power is t^j; for ordinary ones it is t^(N-j-1).
Each radial diagonal operator has norm at most 1/(2pi).
The Gaussian phases and the degree reversal in (16)
are explicit and retain their original roots.

This does not claim that Gamma has polynomial norm:
its exponential action is now carried by the full Psi
functions in its period, rather than hidden in a
discarded boundary frame. A component with one radial
factor and another circle factor can still have an
exponential period. No global dominance estimate
follows from the local radial bound alone.

## 6. Exact scope and the remaining geometric comparison

The full completion is compatible with an actual
charged cap mark and supplies (14) at the physical
root, where the norm-one cyclic version was singular.
The literal middle-five-point factorial transition
also has the exact full-Psi/source realization (16)--(17).
These are concrete local source bridges.

The three classical five-point certificates have
specific shared flags and face orders. Their complete
factor products have not yet been identified with the
mixed factors of (14) or with a proper full-Phi
tetrahedral pentagon before source extraction. In
particular, merely replacing a cyclic function by Psi
does not make the literal candidates 1-Z and X
Q-commute; their additive defect persists. The required
positive quad/Fourier change must carry its full
source and integer mark, with (16)--(17) giving an
explicit test for its boundary normalization.

Furthermore, ordinary Taylor projection is not natural
under arbitrary Laurent inversions: Psi-V begins in
t^N Log t, and multiplication by t^(-N) exposes a
nonvanishing logarithmic source. The circle/radial
formula is integrable for precisely a<N. A proposed
five-point move leaving that range must retain its
logarithmic/carry counterterms. Nothing in (14) requires
this invalid extension; its Delta grading is strictly
positive and nilpotent.

Thus the construction gives a genuine physical-root
mixed pentagon and nonzero original cap coefficient,
not yet the whole positive triangulation period or a
geometric lower bound.

## 7. Reproducible independent checks

Run

    python3 experiments/audit_actual_marked_full_phi_flag_pentagon.py

Exact prime-field checks cover 54 actual marked-root
pentagons through N=10, nine complete literal-five-point
moment gauges, and their original cups and integer marks.
The common phi_N scalar is retained symbolically in
those homogeneous identities. Independent complex
finite-product checks cover every marked unit-root
value (3) through N=20 at both orientations and verify
the exact phase and modulus. No volume statement is
used by these checks.
