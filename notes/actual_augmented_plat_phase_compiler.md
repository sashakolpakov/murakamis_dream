# An exact phase compiler for arbitrary fixed augmented plats

30 October 2026. Every fixed 2k-head plat made from the original
complete crossing-circle coupons R^epsilon L_N, epsilon in {0,+1,-1},
has an explicit finite factorial sum with its entire original phase.
There is no restriction on k>=2 or on the graph formed by its twist
regions. The physical q-Hahn sums simplify: their internal quadratic
phases cancel exactly, leaving a single linear Fourier phase. The
resulting internal critical equation is a quadratic polynomial.

This is a source-exact complete-color statement. It supplies an
explicit global phase and finite algebraic candidate equations. It
does not select their geometric branch, prove a global contour/gap,
or supply a mixed-color filling corridor. Thus it is an advance
toward a theorem for arbitrary fixed sufficiently twisted plats,
not that volume theorem itself. A proposed twist threshold T(D)
depends on the fixed skeleton D; it is distinct from quantum level N.

## 1. The phase of the actual physical Casimir column

Put d=N-1, q=exp(pi i/N), Q=q^2, x=q^d=-q^-1,
kappa=q^(d^2/2), and s_n=product_(r=1)^n 2sin(pi r/N).
For 0<=b<=a<=d write the POSITIVE sine binomial

    beta(a,b)=s_a/(s_b s_(a-b)).

Let t<=d be an actual low physical pair degree, j a Casimir index,
and 0<=u<=t. The actual canonical eigenvector of the physical pair
Casimir has first entry one and components f_u(c_j), with
c_j=q^(2j+1)+q^(-2j-1). Its already proved finite q-Hahn formula is

    f_u(c_j)=x^(t-j)/[t choose j]_Q
       sum_a (-1)^a x^[-(t-j-u+2a)]
         Q^[a(a-1)/2+a(t-j-u+a)]
         [j choose a]_Q [u choose a]_Q [t-u choose j-a]_Q,

    max(0,u-t+j)<=a<=min(j,u).                            (1)

All factorial indices are below N. In particular (1) describes the
original physical column, not an arbitrarily normalized eigenbasis.
The elementary marked identity

    [v choose w]_Q=q^[w(v-w)] beta(v,w)

turns (1) into the simpler exact formula

    f_u(c_j)=(-1)^u q^[-(j+1)u]
       sum_a (-1)^a q^[a(t+j+1)] E(t,j,u,a),

    E(t,j,u,a)=beta(j,a) beta(u,a) beta(t-u,j-a)/beta(t,j)>0.
                                                               (2)

Indeed the complete exponent of q inside (1) is

    -u+2a+a(a-1)+2a(t-j-u+a)
       +a(j-a)+a(u-a)+(j-a)(t-u-j+a)-j(t-j)
      =a(t+j+1)-(j+1)u.                                  (3)

The a^2 terms cancel. No factorial envelope or asymptotic estimate
is used in this cancellation.

On every channel that survives the COMPLETE circle, d-j<=t and
j<=floor(d/2). Put delta=t+j-d. Since (-1)^a=q^(-Na), (2) is

    f_u(c_j)=(-1)^u q^[-(j+1)u]
                         sum_a q^(delta a) E(t,j,u,a),
    0<=delta<=floor(d/2).                                 (4)

Thus the summation variable carries a positive-coefficient polynomial
at one specified Fourier argument q^delta. Its entire phase is
retained; positivity of its coefficients does not imply positivity
or a lower bound for that value.

## 2. Complete signed coupons in every original degree

Take an arbitrary physical pair degree S in 0,...,2d. Set

    t=min(S,2d-S), shift=max(0,S-d).

Use physical basis |shift+u,S-shift-u>, 0<=u<=t. The high block is
literally the low block under this index translation, for both the
Casimir and original signed crossing.

For every j with j<d-j<=t the full reflected-circle resolution has
positive coefficient

    h_(t,j)=2s_t^2/[s_(t-j)s_(t+j-d)].

If N is odd and j=d/2<=t, use the same formula WITHOUT the factor 2.
No other channel contributes. Let nu_j=(-1)^j q^[j(j+1)]. Then the
EXACT all-input kernel of B_epsilon=R^epsilon L_N is

    B_epsilon[u,v]=kappa^epsilon x^(-t)
          sum_j h_(t,j) nu_j^(epsilon-1) f_u(c_j) f_v(c_j).
                                                               (5)

This is bilinear in the two physical columns, not Hermitian. To
prove it, start with the actual positive reflected tensor
H=L_N P=sum_j h v_j v_j^*. Its normalized last component is
(v_j)_t=x^t nu_j, and literal reversal gives
P conjugate(v_j)=conjugate(x^t nu_j) v_j. Hence
L_N=H P has coefficient h x^-t nu_j^-1 times v_j v_j^T.
On this actual complete-circle image, R acts by kappa nu_j.
At a double root its normal correction annihilates L_N: the latter
is its derivative times the square-zero Jordan operator. At the
odd simple root the value calculation is immediate. This proves (5)
for both signs, all parities and all physical degree blocks.

Thus the normal directions responsible for L_N have been evaluated
exactly BEFORE the rank-one image is used. Formula (5) is not an
initial semisimple quotient, and it does not identify an arbitrary
generic-q germ with its root values.

Substitution of (4) makes each (j,a,b) contribution to (5) the
positive factorial weight h_(t,j) E(t,j,u,a) E(t,j,v,b) times

    kappa^epsilon (-1)^[t+(epsilon-1)j+u+v]
      q^[t+(epsilon-1)j(j+1)-(j+1)(u+v)+delta(a+b)].       (6)

Equation (6) is the complete physical coupon phase. In particular
the two internal summation variables have no individual square term.

## 3. Compile any fixed augmented 2k-plat

Fix the positions and order of the twist regions in a literal
2k-head plat. Augment every chosen region by its original auxiliary
circle and retain its prescribed parity epsilon. Use the original
bottom cups, ordinary top caps and ONE unrestricted marked top cap:

    p_ab=N x^-b delta_(a+b,d),
    ell_ab=x^a delta_(a+b,d)/N,
    m_ab=x^b/N^2.                                       (7)

The original exterior line chi_N, including framing, stays explicit.
All crossing-circle coupons and any remaining original crossings
preserve integer degree. Only after the k-1 ordinary top caps have
acted does total degree kd force the marked pair degree to d.
This is the permitted whole-source restriction; m is not replaced
locally in a separated degree-changing sector.

Expand every augmented coupon by (5), or further by (6). Sum every
actual physical wire index, channel j and internal q-Hahn index.
Unchanged identity wires identify their labels. The resulting finite
sum is EXACTLY chi_N times the original marked plat contraction.
There is no inverse Clebsch matrix, recoupling determinant, fitted
boundary vector, or division by a knot value in this construction.
The powers in (7) multiply to N^-1; all other powers, phases and
factorials are those in (5)--(6). Each kappa^epsilon is retained as
its explicit external unit phase, not reset to one.

For a fixed skeleton this is a finite union of rational affine
state polytopes. The low/high choices t=S or t=2d-S give finitely
many chambers. Every surviving channel and internal summation range
is an explicit linear inequality, such as

    d-j<=t, 2j<=d,
    max(0,u-t+j)<=a<=min(j,u).

All lattice offsets from d=N-1 and both parity endpoint weights are
kept in the exact formulas. The number of states is bounded by a
power of N depending on the fixed diagram. Augmentation removes the
large full-twist powers from the number of blocks; those fixed filling
parameters are not extra copies of a quantum-level dependent packet.

This also computes the physical coefficient tensor entering the
[marked multiport Chebyshev packet](actual_marked_multiport_chebyshev_source_packet.md).
That packet's correct C,...,C,H conjugation and final half-bandwidth
fold may be applied afterward. Neither its polynomial DCT cost nor
this exact compiler proves a sharp coherent energy bound.

## 4. An explicit global action and a local quadratic critical equation

Let J(z)=integral_0^z Log(2sin(pi w))dw with the marks continued
from positive factorial arguments. Put

    B(v,w)=J(v)-J(w)-J(v-w).

For scaled labels (tau,xi,upsilon,alpha)=(t,j,u,a)/N the real
factorial action of E is

    Ecal=B(xi,alpha)+B(upsilon,alpha)
              +B(tau-upsilon,xi-alpha)-B(tau,xi).          (8)

Its exact leading complex phase after (4) is

    Ecal+pi i[upsilon-xi*upsilon
                                  +(tau+xi-1)alpha].       (9)

The finite +1 terms and d=N-1 differences give specified order-one
amplitude/phase corrections; they are recovered from (4), not
discarded. For a whole coupon add two copies of (8), the h action

    2J(tau)-J(tau-xi)-J(tau+xi-1),                       (10)

and the exact polynomial phase read from (6). Include the source
characters from (7). Summing these functions over the original
network gives its explicit global candidate phase. Uniform factorial
errors are O_D(log N) even at endpoints; this alone bounds the
absolute term envelope, not the coherent sum from below.

There is a particularly simple algebraic equation for an INTERNAL
q-Hahn stationary variable. The derivative of (8) exponentiates to

    sin(pi(xi-alpha))^2 sin(pi(upsilon-alpha)) /
       [sin(pi alpha)^2 sin(pi(tau-upsilon-xi+alpha))].     (11)

The phase in (9) supplies exp(pi i(tau+xi-1)). Set

    T=exp(2pi i tau), Jc=exp(2pi i xi),
    U=exp(2pi i upsilon), Z=exp(2pi i alpha).

With the original logarithmic marks and away from the displayed pole
divisors, exp(partial_alpha Phi)=1 is exactly

    T(Jc-Z)^2(U-Z)+(Z-1)^2(TZ-U Jc)=0.                    (12)

Its cubic terms cancel. The remaining quadratic coefficients are

    A=T(2Jc+U-2)-U Jc,
    B=T(1-Jc^2-2Jc U)+2U Jc,
    C=U Jc(T Jc-1),
    A Z^2+B Z+C=0.                                      (13)

The degree is at most two on special parameter loci; no division by
A is made. Such degenerations and the specified pole divisors must
remain in any branch analysis.

The complete global stationarity equations likewise become explicit
rational Laurent equations after exponentiating the original wire
variables and clearing ONLY specified nonzero denominators. Thus
finite algebraic candidate-branch and Jacobian tests are available
at arbitrary fixed bridge width. Pole exclusions, logarithmic marks,
boundary sectors and the original finite cycle remain part of the
problem. A solution of (12) has not thereby been identified with a
geometric tetrahedron or an A-polynomial branch.

## 5. Why the real positive saddle criterion does not automatically apply

This exact phase also locates an obstruction. At a real strict
complete-image channel,

    0<tau+xi-1<1/2.

The factorial logarithmic derivative (11) is positive real, while
the derivative phase has argument strictly between 0 and pi/2.
Consequently an interior real alpha cannot solve the stationary
equation even after subtracting an integer Poisson frequency.
Equivalently, the representation before (4) has imaginary derivative
between 2pi and 5pi/2; its retained integer mark removes 2pi and
leaves exactly the phase in (9).

On the boundary delta=0 the finite q-Hahn sum in (4) IS positive,
but this is one channel boundary, not a theorem that the whole
augmented source concentrates there. The odd simple channel and
even endpoint pairs must also remain in any endpoint analysis.

Thus the real-concave version of the
[analytic sewing criterion](actual_six_port_analytic_sewing_criterion.md)
cannot be applied to this raw expanded phase by ignoring its Fourier
factor. One needs a source-preserving complex deformation, a selected
local resummation, or another exact period representation, followed
by a global boundary/gap and nonzero-period argument. The quadratic
(12) makes the local candidate branches explicit; it does not choose
their original-cycle coefficients. The mixed ordinary-circle colors
required by long Dehn filling need a separate extension as well.

Audit: [physical Casimir columns, full signed coupons and marked plats](../experiments/audit_actual_augmented_plat_phase_compiler.py).
The fresh audit passes N=2,...,10: 99 original degree blocks,
704 canonical-column entries, all three signed complete coupon
identities in every block, and eight literal marked plat contractions
at k=2,3,4. Its matrices are built independently from the original
coproduct and signed crossings, not from the q-Hahn formula being
checked. The symbolic phase cancellation and quadratic degree are
also checked exactly. These are source-identity checks, not numerical
evidence for an unproved all-plat volume limit.

The finite compiler does not supply a mixed-color packet or select a geometric cycle.