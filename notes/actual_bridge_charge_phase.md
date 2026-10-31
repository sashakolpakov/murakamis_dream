# Exact charged bridge phase and a further original-source selection rule

28 October 2026. After exact signed overbridge elimination, all
quadratic interior-clock phases telescope. The COMPLETE bridge is
one charge-d cyclic beta product with explicit linear weights.
This gives its full marked complex action. Positive absolute
entropy does not automatically make that action stationary.

An actual post-elimination 5_2 source fiber has nonzero phase flux
at its unique conditional absolute maximum. More constructively,
its remaining finite Fourier sum vanishes EXACTLY on that entire
high-entropy clock region. The vanishing is a new complementary
charge constraint, not a discarded small term or a counterexample
to the volume conjecture.

## 1. Exact normalization and complete phase telescoping

Use the original signed bridge theorem and its full normalizers in
[the source-preserving unwinding note](actual_signed_overbridge_unwinding.md).
Put d=N-1, q=exp(pi*i/N), Q=q^2, x=-q^(-1). A bridge has
m encounters, signs sigma_j, monotone clocks h_1>=...>=h_m,
and original port parameters a_j,b_j with a_j b_j=Q^2 x.
Let u_j be the spectator output, z6 for a positive encounter
and z7 for a negative one. The signed table gives EXACTLY

    c_j=kappa^(sigma_j)/N *a_j^(-h_j)
                             q^(-h_j^2+(1+sigma_j)h_j). (1)

For a positive encounter u_j=Q^(-h_j)/(x a_j); for a
negative one u_j=Qx/a_j. Substituting either in the proved
original c_j gives (1), including every sign and half-step.

Combining all c_j, link monomials and Gaussian phases, the
complete non-Pochhammer/non-binomial prefactor is

    kappa^w/N *Zin^(-h_1)
       *product_(j<m) a_j^(-(h_j-h_(j+1))) *a_m^(-h_m)
       *(-1)^(sum_(j=2)^m h_j)
       *q^(-h_1^2+h_1+sum_j sigma_j h_j),
    w=sum_j sigma_j.                                   (2)

All interior quadratic clocks have cancelled, not been
dropped by taking absolute values.

Define NONNEGATIVE integer charges

    n_0=d-h_1, n_j=h_j-h_(j+1) (1<=j<m), n_m=h_m,
    sum_(r=0)^m n_r=d,
    w_r=sum_(j=1)^r sigma_j.

Put

    t_0=1, t_r=(-1)^r q^(2+w_r)/(Zin a_r), 1<=r<=m,
    z_0=b_1/Zin,
    z_r=a_r b_(r+1)Q^(-1)=x^(-1)a_r/a_(r+1), 1<=r<m,
    z_m=a_m Zout.

Then the ENTIRE original conditioned bridge coefficient is

    B_gamma=kappa^w product_(r=0)^m
                      [(z_r;Q)_(n_r)/F_(n_r) *t_r^(n_r)],
    F_n=(Q;Q)_n.                                      (3)

This identity includes every original N factor. To prove it,
the telescoping q-binomial product is
F_(h_1)/[F_(h_m)product F_(h_j-h_(j+1))]. Reflect

    F_(h_1)F_(d-h_1)=N(-1)^(h_1)q^(h_1(h_1+1)).

Its N cancels the 1/N in (2), its quadratic cancels
-h_1^2, and its sign combines into (-1)^(sum_j h_j).
Finally sum_j h_j=sum_(r>=1)r n_r and
sum_j sigma_j h_j=sum_(r>=1)w_r n_r. This proves (3).

The exact parameters obey

    z_(r-1)t_(r-1)=Q^(epsilon_r)t_r,
    epsilon_r=(1-sigma_r)/2,
    z_m t_m=Tend=(-1)^m q^(2+w) Zout/Zin.               (4)

These are source identities, not an imposed balancing condition.

## 2. The full leading COMPLEX bridge action

Write T_r=n_r/N, U_r=exp(2pi*i*T_r). The exact charge is
sum T_r=1-1/N; its leading equation is sum T_r=1. On a
fixed nondegenerate logarithmic cell the marked complex action is

    W_gamma=sum_r [Li_2(z_r)-Li_2(z_r U_r)
                        -Li_2(1)+Li_2(U_r)
                        +Log U_r Log t_r].             (5)

The full coefficient has exp[N W_gamma/(2pi*i)] times its
specified subexponential density, with kappa^w still EXACTLY
outside. If one expands the original complete kappa as well,
its leading action is the known real constant -pi^2 w.
It changes no stationarity equation. The q^(2+w_r) factors
in (3) remain in the exact source and its finite-level phase;
they affect (5) at subleading order for fixed word length.

Branches in (5) mean the continuation of each actual finite
Pochhammer arc. Equivalently define its leading logarithm by
integrating Log(1-z exp(2pi*i*t)) along that arc; do not give
the endpoint dilogarithms unrelated principal branches.
The factorial starting at 1 has its usual integrable endpoint.

The full differential, before imposing actual spectator-flow
dependencies, is

    dW=sum_r {
       Log[t_r(1-z_r U_r)/(1-U_r)] dLog U_r
       +Log[(1-z_r U_r)/(1-z_r)] dLog z_r
       +Log U_r dLog t_r }.                            (6)

Thus the Gaussian/monomial source has not disappeared from the
action. It is now the explicit Log U Log t coupling.

If the bridge parameters a_r are independent while its
charges vary, constrained charge criticality requires

    t_r(1-z_r U_r)/(1-U_r)=Lambda,
    U_r=(Lambda-t_r)/(Lambda-z_r t_r).

At leading order (4) gives z_r t_r=t_(r+1). Hence
product U_r=(Lambda-1)/(Lambda-Tend). The charge equation
product U_r=1 therefore requires Tend=1 for a finite
regular interior critical point. Generic endpoint data
do not satisfy it. This is a conditional phase-flux test,
not a global knot critical equation: the actual anchored
flow makes some a_r depend on other charges and supplies
the extra terms in (6).

There is an exact finite counterpart. If the a_r really
are held independent during summation over all charges,
write U_z(v)=sum_(n=0)^d (z;Q)_n v^n/F_n. Then

    sum_(sum n=d) B_gamma
       =kappa^w [v^d] U_Tend(v)
                           product_(sigma_r=-1)(1-t_r v)^(-1). (7)

Proof: modulo v^N the finite quantum binomial theorem is
U_z(v)=P(zv)/P(v), with the original finite Euler P.
Using P(Qv)=P(v)/(1-v), equations (4) telescope the product.
This independent-parameter sum must not be applied to a
whole knot while ignoring the actual spectator-flow dependencies.

## 3. Real angular entropy and phase, with every sheet retained

On the original fixed-central grids, |z_r| and |t_r| differ
from one by O(1/N). Write their leading arguments as
z_r=exp(2pi*i*alpha_r), t_r=exp(2pi*i*tau_r).
Let J(s)=-D(exp(2pi*i*s))/(2pi), periodic, and let

    chi(s)=({s}^2-{s})/2.

The leading logarithmic modulus per N and phase per N are

    E_gamma=sum_r [J(alpha_r+T_r)-J(alpha_r)-J(T_r)],
    Theta_gamma/pi=sum_r
         [chi(alpha_r+T_r)-chi(alpha_r)-chi(T_r)+2T_r tau_r]. (8)

The phase includes the c_j monomials and original Gaussian
phases through tau_r. The omitted kappa phase is label-independent
and specified above. Equation (8) is a piecewise quadratic real
phase on every actual support cell, not a positive weight.
At the usual nonzero radial grid regularization the errors are
O(log N) in log magnitude; on endpoint-free cells the neighbor
phase derivatives converge with O(1/N) error.

On a positive arc 0<alpha_r<alpha_r+T_r<1, (8) reduces to

    Theta_gamma=pi sum_r T_r(alpha_r+2tau_r).

Choosing the actual lifted relation alpha_r=tau_(r+1)-tau_r
there gives Theta_gamma=pi sum_r T_r(tau_r+tau_(r+1)).
Its internal phase derivative is pi(T_(r-1)+T_r), strictly
positive when the adjacent charges are positive. A real
absolute optimizer is therefore not automatically a complex
stationary point. The corresponding absolute entropy is
the sum of twice the ideal tetrahedron volumes with angles
pi*T_r, pi*alpha_r, pi*(1-alpha_r-T_r). These form a genuine
positive concave angle chart, but the retained phase remains.

## 4. A new complementary-charge rule for an actual remaining wire

Consider an actual under-output followed by a reduced
overbridge-input on the SAME ordinary wire. Suppose its
full dependence is

    g(Z)=Z^(r-H)(aZ;Q)_(d-r)(b/Z;Q)_(d-H), ab=Q,
                                      0<=r,H<=d.        (9)

Then the exact remaining constant term is

    CT g=(-1)^(d-r) a^(H-r)
       *Q^[(d-r)(d-r-1)/2-H(d-H)]
       *[r choose d-H]_Q.                             (10)

In particular it is ZERO unless r+H>=d. No geometric
norm is divided out in (10). This is a new source-support
selection in addition to overbridge monotonicity.

Here is an elementary proof, without assuming a q-Chu theorem.
Put t=aZ, L=d-r, K=d-H. Reflect the second product:

    (Q/t;Q)_K=(-1)^K Q^(K(K+1)/2)t^(-K)
                                      (tQ^(H+1);Q)_K.

Thus CT g is a^(H-r)(-1)^K Q^(K(K+1)/2) times
[t^L](t;Q)_L(tQ^(H+1);Q)_K. If r+H<d, the product
is (1-t^N) times a polynomial of degree<L, so this
coefficient vanishes. If r+H>=d it is

    (1-t^N)/(tQ^L;Q)_(H-L+1).

Finite q-Pascal gives its t^L coefficient
Q^(L^2)[H choose L]_Q. Root factorial reflection turns
the result into (10); the parity factor is exactly
Q^(N(N-1)/2)=(-1)^(N-1), also at even N.

For r+H<=d-1 the stronger root-circle identity is

    g(Z)=(-1)^(d-H)a^(-(d-H))Q^((d-H)(d-H+1)/2)
        *Z^(r-d)(1-(aZ)^N)
        *(Q^(H+1)aZ;Q)_(d-1-r-H).                     (11)

On the original grid the norm 1-(aZ)^N is a fixed
nonzero scalar. Its remaining Fourier powers lie from
r-d through -H-1, entirely negative and strictly above
-N. Thus the original N-point SUM, not merely a formal
constant term, is exactly zero in this region.

## 5. Whole original post-reduction sanity check: 5_2

Use the independently identified original word
[1,1,1,2,-1,2] and its actual averaged cut and two
pivots in the [post-bridge source audit](../experiments/audit_bridge_reduced_absolute_envelope.py).
Its overpaths are [0],[1],[2,3],[4],[5]; wire 8 has
already been eliminated in the genuine two-crossing bridge.
Keep the audit's rational labels, but change label6/N
from 9/10 to 89/100. Then the underclock of crossing1
is r/N=1/100, while the first reduced overbridge clock
is H/N=59/100 and the second is 35/100.
The nontrivial bridge inequality is strict.

The remaining wire5 occurs only in the under-output
of crossing1 and the input of that reduced bridge.
Their actual parameters satisfy ab=Q: a=Q^(r+1)/z3
and b=z6/x, while z6=x z3 Q^(-r). Every other
crossing, reduced bridge factor and original boundary
coupon is independent of wire5. Thus (9)--(11) apply
to the ENTIRE remaining source, with its full scalar.

The label5/N=1/10 lies at the unique conditional global
absolute maximum in this fiber. Indeed its one remaining
Pochhammer has asymptotic length 1-r/N-H/N=2/5;
the two endpoints are conjugate there. Yet its phase
flux under label5 -> label5+1 tends to

    pi(1+r/N-H/N)=21pi/50 !=0 modulo 2pi.               (12)

The complete reduced entropy at this supported source
point is 2.546436873747266..., much larger than the
geometric knot-volume rate. This does not refute the
volume conjecture: (11) shows its conditional source
sum is EXACTLY ZERO. The large real envelope is removed
by a further source constraint, not by a norm estimate.

For a direct phase calculation on this cell, the whole
source's leading phase obeys

    (1/pi) partial_(label5/N) Theta
        =xi3-2xi6+xi7+1=21/50.

The original cap/pivot factor is nonzero and independent
of wire5; common kappa/framing phases are retained and
cancel from this neighbor ratio. The audit compares the
whole actual finite-source ratio with (9), not a newly
chosen co-source or a pre-elimination summand.

The lesson is constructive. Exact bridge reduction gives
a positive entropy chart, but no automatic real saddle.
One must also perform or control the remaining anchor
contractions. Equation (10) proves one actual new
complementary-charge selection; its condition ab=Q is
typed and must be checked before applying it elsewhere.
No claim that all remaining seams have this form is made.

The [audit](../experiments/audit_actual_bridge_charge_phase.py)
checks the exact charged identity, its optional independent-parameter
height sum, the complementary seam for every clock, and the
whole original post-bridge phase/source fiber.
