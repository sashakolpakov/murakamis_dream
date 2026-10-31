# The original cross-central Green kernel has a selected spectral action

30 October 2026. The exact exceptional
operator period now has a source-selected leading Green-kernel action
when its two physical rows lie strictly on opposite sides of the
midpoint. The actual characteristic denominator, all phases and both
level parities are retained. On the anti-diagonal the original Green
entry is strictly negative for every real spectral parameter below -2.
Every fixed genuine generic-q jet costs only a polynomial relative
to that root Green entry on the strict fixed compacts below.

This is an integrand theorem. It neither deforms the fixed contour
nor proves that its geometric critical point contributes.

## 1. Exact original phases and the anti-diagonal sign

Use the original root matrix J_t of
[the continuant operator period](actual_matching_edge_continuant_operator_period.md),
with 0<=t<=d=N-1. Let 0<=u<=v<=t, q=exp(pi i/N), theta=pi/N, and

    Delta_m(z)=det(J_[m]-zI),
    D_t(z)=det(J_t-zI)
          =product_(h=0)^t [2cos((2h+1)theta)-z].

The original upper and lower entries agree AT THE ROOT and equal

    U_r=-a_r exp[i(2r+1-t)theta],
    a_r=4sin((t-r)theta)sin((r+1)theta)>0.           (1)

The root reversal is J_t reversed=conjugate(J_t). Thus the trailing
determinant of size t-v is conjugate(Delta_(t-v)(conjugate z)).
Substitution in the exact Green formula gives

    (zI-J_t)^-1_(u,v)
       =-exp[i theta(v-u)(u+v-t)]
          *product_(r=u)^(v-1) a_r
          *Delta_u(z) conjugate(Delta_(t-v)(conjugate z))/D_t(z).
                                                               (2)

The single minus sign is important. The upper product has sign
(-1)^(v-u), the two zI-J continuants have signs (-1)^u and
(-1)^(t-v), and the full characteristic determinant has sign
(-1)^(t+1). Their ratio is -1, independent of every label and
level parity. Also
sum_(r=u)^(v-1)(2r+1-t)=(v-u)(u+v-t) exactly.

For a real z<-2 the denominator D_t(z) is positive. If u+v=t,
the phase in (2) is one and its two prefix lengths agree. Hence

    (zI-J_t)^-1_(u,t-u)
       =-product_(r=u)^(t-u-1) a_r *|Delta_u(z)|^2/D_t(z)<0,
                         0<=u<=floor(t/2).         (3)

Strictness is exact, not asymptotic. For u=0 the empty determinant
is one. For u>0, the already proved positive imaginary part of
the physical half-prefix implies Delta_u(z)!=0 for every real z;
its proof needs only u<=floor(t/2), not a complete-channel
assumption. See the explicit extension in the
[physical generic-jet theorem](actual_q_hahn_physical_generic_jet_bound.md).
Equation (3) is the sign of the original matrix entry. It does not
replace the surrounding state or mark by a positive functional.

## 2. A fully normalized leading Green action

Take actual integer sequences with

    t/N->tau, u/N->nu, v/N->omega,
    0<nu<tau/2<omega<tau<1.                        (4)

Uniformity is on compact subsets of this strict real domain.
The row indices remain physical integers. They are not analytically
continued to complex magnetic coordinates.

Use the selected prefix action proved in
[the original off-spectrum prefix theorem](actual_casimir_off_spectrum_prefix_action.md):

    A_tau(s)=-4 exp[i pi(2s-tau)]
                         sin(pi(tau-s))sin(pi s),
    w=2-z,
    S_(tau,b)(z)=integral_0^b
       Log[(w+2A_tau(s)+sqrt(w(w+4A_tau(s))))/2] ds.  (5)

The logarithm and square root are selected at negative real spectral
infinity. Write S^#_(tau,b)(z)=conjugate(S_(tau,b)(conjugate z)),
which is a holomorphic function on the conjugate prefix domain.

Define beta_1=pi(1-tau+2nu), beta_2=pi(1-tau+2(tau-omega)).
Both lie strictly between zero and pi. Let U be the component
containing the real interval z<-2 of

    {Re[exp(-i beta_1/2)(2-z)]>0}
     intersect {Re[exp(+i beta_2/2)(2-z)]>0}
     minus [-2,2].                                (6)

In particular U contains a complex neighborhood of every compact
real interval below -2. Every compact subset of U is in the two
finite prefix domains for all sufficiently large N. Their actual
determinants are nonzero there, as is D_t.

Use (2) to mark the logarithm of minus the Green entry: retain its
literal phase theta(v-u)(u+v-t), the positive logarithms of a_r,
the two selected prefix logarithms, and the denominator product
logarithms continued from their positive values at z<-2. Then

    N^-1 Log[-(zI-J_t)^-1_(u,v)] -> G_(tau,nu,omega)(z),

    G_(tau,nu,omega)(z)
      =i pi(omega-nu)(nu+omega-tau)
       +integral_nu^omega log[4sin(pi(tau-s))sin(pi s)] ds
       +S_(tau,nu)(z)+S^#_(tau,tau-omega)(z)
       -integral_0^tau Log[2cos(2pi s)-z] ds.        (7)

Convergence is locally uniform on U, with every fixed z derivative.
The proof uses the actual identity (2): each prefix limit is (5),
the middle positive product has a smooth Riemann-sum limit on the
strict interval in (4), and the EXACT denominator product has the
last integral in (7). All its roots remain in [-2,2], so on a
compact of U that Riemann sum and its spectral derivatives converge
uniformly. No unknown function of z can be added to (7).

The normalized logarithm is an accumulated source phase, not the
principal argument of the scalar Green entry. On the anti-diagonal
omega=tau-nu, (7) is real for z<-2, in agreement with the exact
negative sign (3).

## 3. The genuine generic-q Green normals have relative polynomial bounds

Keep a fixed compact of the parameter and spectral domain (4),(6),
and now use the original generic matrix J_t(q exp(h)), including
its distinct upper and lower entries. Write R_uv(h,z) for its
Green entry. For all sufficiently large N there are constants c,C>0, independent of N and the
physical integer labels in this compact, such that

    |R_uv(h,z)/R_uv(0,z)|<=C,
    |R_uv(0,z)/R_uv(h,z)|<=C,
                         |h|<=c N^-2.             (8)

In particular the generic entry is nonzero on this disk and

    |partial_h^r R_uv(0,z)|
          <=C_r N^(2r)|R_uv(0,z)|                 (9)

for every fixed r. The inverse Green entry has the corresponding
relative bound. These are upper bounds; no nonzero asymptotic
amplitude for a particular normal is inferred.

Here is a proof retaining the source factors. Each original
generic entry in the physical tridiagonal block has h derivative
O(N) for |h|<=c/N^2. Its finitely many exponent factors have size
O(N), and their moduli are bounded on that disk. Fixed bandwidth
therefore gives an operator-norm perturbation O(N|h|) in either
prefix. At the root, the two prefix inverses on the chosen compact
are uniformly bounded by the proved strict-half-prefix theorem
and its conjugate. Thus their relative determinant factors are
det(I+E), with ||E||<=C N|h|. For N large this is less than 1/2,
and the trace logarithm gives

    |Log det(I+E)|<=C N^2 |h|.

This bounds BOTH determinant ratios. The trailing generic prefix
is perturbed as its own actual matrix; the root reflection is used
only to establish its initial inverse bound, never differentiated.

All intervening upper entries in the Green product are uniformly
bounded away from zero at the root: the strict support has u/N>0
and v/N<tau, and both sine factors in (1) have fixed margins on
that interval. Their individual logarithmic variations are O(N|h|),
so their product and its inverse have the same exp[O(N^2|h|)]
relative control. Finally the EXACT generic denominator is
product_(m=0)^t[lambda_m(q exp(h))-z]. The spectral compact has
positive distance from [-2,2]; each moving node varies by
O(N|h|), so this denominator and its inverse satisfy the same
relative bound. Combining these facts in the original generic
Green formula proves (8). Cauchy's inequality on that very disk
proves (9), retaining all numerator and spectral-node derivatives.

## 4. The original scalar integrand and its remaining contour problem

Let a/N->alpha in (0,1/2]. The actual Casimir polynomial has the
selected logarithmic limit Psi_alpha(z) from
[the source root-location theorem](actual_matching_edge_racah_root_location.md).
At the root the original face factor is D_a(q)=1. Thus, on the
common domain just specified, the ACTUAL spectral integrand in
the completed-operator formula has leading action

    Psi_alpha(z)+G_(tau,nu,omega)(z).              (10)

In particular its spectral stationarity equation is explicitly

    Psi_alpha'(z)+G_(tau,nu,omega)'(z)=0,

    G'(z)=-integral_0^nu
             [w(w+4A_tau(s))]^-1/2 ds
           -integral_0^(tau-omega)
             [w(w+4conjugate(A_tau(s)))]^-1/2 ds
           +integral_0^tau [2cos(2pi s)-z]^-1 ds.  (11)

The roots in (11) are those of (5) and its conjugate continuation,
not newly chosen square roots. The denominator term is essential;
it is fixed by the original finite characteristic polynomial.

Equation (10) is an action for the real-physical-row INTEGRAND, not
an asymptotic for the contour integral or for its surrounding
coherent contraction. A deformation of the original fixed contour
still has to retain every actual spectral pole and normal. Targets
in (-2,2), midpoint prefixes, complex physical rows and relative
amplitude expansions are outside the theorem here. The normal
bound (9) does not assert that an individual normal has that action.
Neither (3) nor (7) implies dominance of the real off-spectrum ray.

There is also an explicit endpoint issue for a closed contour. A
fixed contour enclosing the spectral interval can cross the scalar's
limiting cut [2,infinity). A contour staying in that scalar slit may
instead need an N-dependent closing segment approaching 2, between
the largest Casimir node and the smallest scalar zero. Fixed-compact
limits (7),(10), or the fixed-compact normal bound (9), do not
control such a segment.

Audit: [actual Green phases, strict anti-diagonal signs and selected logarithms](../experiments/audit_actual_matching_edge_cross_central_green_action.py).

The theorem bounds the stated integrand and normals. It does not select a contour or prove a geometric contribution to the full source.