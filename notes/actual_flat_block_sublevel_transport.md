# Exact unit-mass transport for phase-flat charged block cores

28 October 2026. An additional constructive case of the fixed-clock mass
problem covers UNBALANCED biconnected cores with any fixed number of anchors.
The hypothesis is the flatness of their actual positive-binomial block
connection, not balance of their individual binary-factor incidences.
It is checked from the original block metadata. No finite source is changed.

The conclusion is stronger than existence of a semialgebraic replacement:
one constant-radius source torus has normalized logarithmic mass ONE. There
is also an explicit polynomial lower bound relative to its positive capacity.
This is a fixed-clock theorem. Flatness is not automatic on surviving knot
sources, and this note supplies no general full-clock volume estimate.

## 1. Original blocks and a precise phase test

Let Q=exp(2pi*i/N), q=exp(pi*i/N), and take the actual residual block source

    P(X)=gamma product_e product_(r=0)^(L_e-1)
                      (alpha_e X_(u_e)-Q^r beta_e X_(v_e)),
    f(X)=P(X)/product_i X_i^(a_i),
    1<=L_e<=N-1, |alpha_e|=|beta_e|=1, sum_i a_i=sum_e L_e=M.

All extracted original normalizers and clock factors remain outside or in
gamma as previously specified. Loops and tight cuts are treated by their
exact source rules before taking this residual connected core. Assume its
strict Hall inequalities: for every nonempty proper vertex set I,

    0<a(I)-m_I<C_I.                                      (1)

The block coefficient identity from
[the actual phase calculation](anchor_phase_cycles_and_exact_fusion.md) is

    product_r(alpha X_u-Q^r beta X_v)
       =alpha^L sum_(j=0)^L c_(L,j) w_e^j X_u^(L-j)X_v^j,
    c_(L,j)=|[L choose j]_Q|>0,
    w_e=-(beta_e/alpha_e)q^(L_e-1).                       (2)

Assume there are unit phases eta_i such that w_e=eta_v/eta_u on every
edge. Equivalently every oriented block-cycle holonomy is one. This is a
finite spanning-tree test, including every parallel edge and original
closure block. For actual root phases it is exact integer arithmetic
modulo 2N, rather than a numerical small-phase test.

Substitution X_i=eta_i^(-1)Y_i transforms the ENTIRE polynomial to

    P(eta^(-1)Y)=Gamma P_+(Y),
    P_+(Y)=product_e sum_j c_(L_e,j)Y_u^(L_e-j)Y_v^j,
    Gamma=gamma product_e alpha_e^(L_e)eta_u^(-L_e).

Consequently the original coefficient has the exact pointing

    [X^a]P=Gamma product_i eta_i^(a_i) [Y^a]P_+.          (3)

The factors in (3) are known source factors; they are not chosen from
the unknown period. Their modulus is |gamma|.

## 2. An actual regular critical point and a unit-mass sublevel torus

Set

    G(rho)=log P_+(exp rho)-sum_i a_i rho_i.

For each block use its normalized positive weights proportional to
c_(L,j) exp((L-j)rho_u+j rho_v). Differentiation gives

    Hess G=sum_e Var_e(j)(e_v-e_u)(e_v-e_u)^t.             (4)

Every variance is strictly positive. Connectivity therefore makes G
strictly convex modulo the common scale. It is coercive on that quotient.
To see this without a capacity theorem, order the rho_i and write their
successive gaps as g_j, with high vertex sets I_j. Choosing the larger
endpoint of every block gives an endpoint monomial of coefficient at
least one, and hence

    G(rho)>=sum_j [C_(I_j)-(a(I_j)-m_(I_j))]g_j
             >=max rho-min rho.                        (5)

The last inequality uses the integral strict Hall condition (1).
Adding the constant log|gamma| would restore the outside scalar.
Thus a unique minimizer rho_* exists modulo scale. Its positive value

    Cap=|gamma| exp G(rho_*)

is an ACTUAL regular complex critical modulus of f at
X_i=eta_i^(-1)exp(rho_*,i). Holomorphic differentiation agrees with
the real logarithmic derivative there, and every block is nonzero
because its transformed coefficients and arguments are positive.
The existing radial cut theorem in addition bounds its radius ratios
by (M-1)^(k-1).

On the shifted source torus X_i=eta_i^(-1)exp(rho_*,i+i theta_i),
the triangle inequality in (2) gives |f(X)|<=Cap. This torus is
homologous to the original coefficient torus in (C*)^k/C*, by ordinary
finite changes of radii and angles; its normalized absolute logarithmic
top-form mass is exactly one. Therefore

    |[X^a]P|<=Cap<=Mcrit(f).                              (6)

This bypasses the unknown complexity of interior gradient transport
for this entire class, including its unbalanced biconnected members.
It does not assert that Cap is the largest of all complex critical moduli.

## 3. A source-exact polynomial lower bound

Let B be the number of nonempty blocks. At rho_*, choose independent
integer random variables J_e with probabilities

    p_e(j)=c_(L_e,j)exp((L_e-j)rho_u+j rho_v)/Z_e.

The mean endpoint assignment is a, by criticality. Expanding P_+ gives
the EXACT identity

    |[X^a]P|/Cap=Prob(endpoint degrees equal a).           (7)

The sequences p_e are log-concave. Indeed their successive ratios,
apart from a positive tilt, are

    sin(pi(L-j)/N)/sin(pi(j+1)/N).

These decrease because the sum of the two relevant cotangents is
sin(pi(L+1)/N) divided by positive sine factors. For L=N-1 the
ratios are constant, so the same conclusion holds.

Extend log p_e affinely between integers, obtaining a concave function
phi_e. If mu_e=E J_e, Jensen and the entropy bound give

    phi_e(mu_e)>=sum_j p_e(j)log p_e(j)>=-log(L_e+1).    (8)

There is an integral endpoint flow j_e with the SAME required degrees
and with sum_e phi_e(j_e)>=sum_e phi_e(mu_e). Here is an elementary
rounding proof. Confine each coordinate to [floor mu_e,ceil mu_e];
every phi_e is affine on this box. The nonintegral edges of a feasible
flow have no degree-one vertex, since the required incidence imbalance
is integral. They therefore contain an undirected cycle. Move in both
directions along that cycle until an edge becomes integral. The current
flow is a convex combination of the two endpoints, so at least one
endpoint does not decrease the affine objective. Repeat; an integral
feasible flow is reached after at most B steps. This is the usual
network-flow rounding proved here with its source degrees retained.

The probability of that ONE integral flow, using (8), is at least
product_e(L_e+1)^(-1). Equation (7) now proves

    Cap/product_e(L_e+1) <= |[X^a]P| <= Cap.              (9)

For a fixed original diagram B is bounded independently of N, so
the lower factor is polynomial in N. This is actual selected-coefficient
noncancellation in a fixed sector, not a conclusion from a nonzero
ambient module or a guessed local saddle.

## 4. What must still be checked for a whole knot

The phase test must hold for the ACTUAL surviving block graph, after
every proposed exact fusion, with all original closure and clock factors.
The existing nonzero 6_3 family has a macroscopic curved bulk cycle, so
the test is not automatic for alternating diagrams or arbitrary widths.
No arbitrary-width hyperbolic-knot class satisfying it in every sector
has been established here. An original full clock sum may also cancel
between the known phases in (3) and its retained W_h.

There is a finite way to certify UNIFORM anchor flatness, if a diagram
class supplies the needed identities. For the original metadata each
block gain is q^(b_e N+c_e+sum_j a_ej h_j), with integer coefficients.
On a stratum where the nonempty blocks and chosen source fusions are
fixed, spanning-tree propagation makes each cycle exponent an affine
integer function of (N,h). Uniform flatness is exactly its vanishing
modulo 2N on that stratum's integer clock lattice. Check its values
on one lattice point and on generators of the difference lattice.
The constants and linear coefficients are explicit, so this avoids
an all-level numerical extrapolation. The unit-block-preserving source
fusions used here only multiply or divide unit gains and impose affine charge/length
equalities; their finite anchor-decreasing order gives finitely many
such strata for a fixed diagram. This is a certification procedure,
not a proof that the test succeeds on any new knot class.

Including the clocks as extra coefficient variables would require an
exact nonnegative-coefficient, phase-flat presentation of their FULL
feedback and factorial weights. The anchor Ward equations alone do not
provide this: their critical points are not critical in h. Equations
(6)--(9) therefore cannot be assigned the knot regulator bound without
that missing joint comparison, and no nonflat sectors are discarded.

For the general nonflat mass problem, semialgebraic complexity of one
sublevel set still does not control the particular transported source
class. Effective local trivializations over a polynomial number of
base intervals cannot simply be composed while retaining polynomial
degree or multiplicity. This note avoids that issue only by constructing
the constant-radius torus above.

A bare quotient by the critical ideal is not an alternative finite-source
argument. Already for f=z+z^(-1), its critical derivative z-z^(-1)
has CT[z(z-z^(-1))]=-1. Thus the original coefficient functional does
not annihilate the critical ideal. A toric-residue comparison must
retain the differential source or construct its exact adapter, not
replace this functional by evaluation on critical points.

The hypothesis L_e<=N-1 is essential: a length-N Fermat block has missing interior coefficients, so strict Hall alone would not imply the lower bound (9). The theorem does not extend to a full-clock or knot-class statement.

[Audit](../experiments/audit_actual_flat_block_sublevel_transport.py):
root-Pochhammer phases, unbalanced strict-Hall examples, convex critical
points, original complex coefficients and the polynomial probability
bound. These computations supplement the uniform proof above; no knot
class or full-clock volume theorem is inferred from the examples.
