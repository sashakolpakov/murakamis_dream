# Quantitative descent of the actual phase up to its boundary currents

28 October 2026. Saturation gives more than a bound at exact critical
points: on a slowly expanding regular window it gives a polynomial lower
bound for the gradient everywhere above the volume level. Normalized
gradient descent consequently costs only exp(o(N)) in that window. The
full quantum dilogarithm has a uniform symbol estimate on the same slowly
shrinking angular strips.

This is a quantitative REGULAR-REGION statement for the actual full
phase, at arbitrary fixed word width. It does not remove the original
relative boundary currents. Descent can reach a shape/coordinate boundary,
a logarithmic chart seam, or a quantum-pole exclusion before reaching the
volume sublevel. Such exit currents must be retained. A claim of the full
sharp knot bound still requires their estimate or exact cancellation.

## 1. The fixed phase and its algebraic critical equations

Use the full logarithmic coordinates of
[the marked critical-action calculation](actual_wall_critical_regulator.md),
including every Gaussian and cap coordinate. On a recorded local sheet,

    W(Z)=sum_a epsilon_a Li_2(A_a(Z))
              +Z^t C Z/2+i kappa^t Z+c,
    A_a(Z)=sigma_a exp(v_a^t Z),
    phi=Im W, R=sum_a epsilon_a D(A_a), rho=Re Z.

The actual signed monomial vectors v_a and quadratic form C have the
integral/rational structure specified there; any required fixed algebraic
coordinate cover is retained. Branches and their integer logarithmic marks
are matched. In particular c has real imaginary-free normalization, and
the exact off-critical identity is

    phi-R=rho^t Im(partial W).                         (1)

Write x_i=exp Z_i. In these actual coordinates the exponentiated full
critical equations are rational functions of the torus coordinates on
the fixed cover:

    H_i(x)=exp(partial_i W), H_i(x)=1.                 (2)

One can instead use a fixed nonsingular linear combination of the
derivatives if a coordinate cover requires it; all norm comparisons then
have fixed constants. It is necessary to use the original exponentiated
equations, not powers that introduce additional solution components.
Integer changes of the recorded flattening do not change (2).

Clear denominators to obtain f_i(x). Let D(x) contain the torus coordinate
factors, all cleared denominators, all singular graph factors, and the
shape exclusions. The regular critical locus is the zero locus of the
f_i in D!=0. Its JOINT shape-image closure Y in (P^1)^s is the saturated
closure of [the critical compactification](saturated_critical_regulator_compactification.md).
The already proved input is

    |R|<=V on Y, V=Vol(S^3 minus K).                    (3)

This is a statement about the actual full equations. Replacing them by
an anchor-only, constrained endpoint, or unsaturated cleared system is
not permitted in the following argument.

## 2. A finite saturation certificate separates high regulator values

Take finitely many multihomogeneous equations G_l for Y in the product
of projective lines. For their affine pullbacks g_l(x)=G_l(A(x),1),
the localized radical ideal condition gives finite certificates

    D^(k_l) g_l^(s_l)=sum_i h_(li)(x) f_i(x),           (4)

after clearing any additional fixed rational denominators. Here
k_l>=0 and s_l>=1 are fixed integers, and h_(li) are fixed polynomials.
The power s_l cannot in general be omitted: the original critical ideal
need not be radical. Formula (4) is an ordinary ideal-membership
certificate. Its existence follows by taking the radical in the
localized coordinate ring; it can also be produced and checked by
polynomial arithmetic for a specified word.

Normalize every G_l on unit homogeneous representatives, so |G_l|_norm
is a continuous function on the compact product (P^1)^s. For any fixed
eta>0 the compact set

    B_eta={shape tuples: R>=V+eta}

is disjoint from Y. Therefore either B_eta is empty, or

    max_l |G_l|_norm >= mu_eta>0 on B_eta.              (5)

This uses compactness and the defining equations only, not an effective
Lojasiewicz exponent or an assumption of isolated critical points.
At finite shapes the affine value |G_l(A,1)| is at least its normalized
value: the removed homogeneous normalization factor is a product of
positive powers of sqrt(1+|A_a|^2), each at least one.

## 3. Polynomial gradient lower bound on a mild regular window

Fix a finite analytic chart with its recorded logarithmic branches.
For L>=2 let Omega_L impose

    |x_i|, |x_i|^(-1)<=L,
    |d_a(x)|^(-1)<=L

for each individual excluded polynomial factor d_a of D. Further
fixed chart restrictions, including selected-strip or quantum-pole
exclusions, may be imposed. The upper bounds on all fixed polynomials
on Omega_L are powers of L. Also |rho|<=sqrt(dim Z) log L.

There are constants c_eta>0 and B<infinity, depending on the fixed
word, chart and eta but not L, such that

    phi>=V+eta, Z in Omega_L
             ==> ||partial W(Z)||>=c_eta L^(-B).      (6)

Proof. If ||partial W||>=eta/(2 sqrt(dim Z) log L), this already
implies (6), after increasing B and decreasing c_eta. Otherwise (1)
gives R>=V+eta/2, so (5) supplies a g_l of modulus at least mu_(eta/2).
For ||partial W||<=1, |exp(partial_i W)-1|<=e|partial_i W|.
Clearing its denominator thus gives

    |f_i(x)|<=C L^a ||partial W||.

The certificate (4), the denominator lower bounds and polynomial upper
bounds give

    mu_(eta/2)^(s_l)<=C L^b ||partial W||.

There are only finitely many certificates, so their largest exponent
and smallest positive constant give (6). The case ||partial W||>1
is immediate. If B_(eta/2) is empty, the first alternative is the only
one. This proves the claim uniformly even near nonisolated critical
components and their genuine saturated degenerations.

The same window gives a polynomial Hessian bound. Locally,

    partial^2 W=C+sum_a epsilon_a v_a v_a^t A_a/(1-A_a),
    ||partial^2 W||<=C L^a.                            (7)

Higher fixed derivatives have the same type of bound. These bounds do
not depend on the choice of an integer logarithmic mark, which changes
only the linear part of W.

Taking L=N^epsilon in (6)--(7) proves a quantitative exclusion of
high-action approximate critical points in this window. The point is
the exponent B*epsilon, which can be made smaller than any fixed
positive number by choosing epsilon sufficiently small. This is
stronger than merely excluding a convergent high-action critical
sequence on a fixed compact set.

## 4. Subexponential cost of regular descent

Regard the logarithmic chart as a real Euclidean domain. Holomorphy
gives ||grad phi||=||partial W||. On phi>=V+eta use the vector field

    X=-grad phi/||grad phi||^2.                         (8)

Then d phi(X)=-1 exactly. Equations (6)--(7) imply, for another fixed B,

    ||X||+||DX||<=C_eta L^B.                           (9)

Extend it smoothly in a slightly larger regular chart as needed, with
a cutoff which is one on the region being used; before a chart exit
this does not change the flow. A cutoff over an inverse-power collar
still has derivative bounded by a fixed power of L.

Suppose the initial chain has mass exp(o(N)) and initial action at
most O(log^2 N), as holds for bounded branches and logarithmic radii
O(log N). Up to its first exit or its arrival at phi=V+eta, the
available flow time is T_N=O(log^2 N). The usual variational equation,

    d(D F_t)/dt=DX(F_t) D F_t,

and direct integration of its norm imply

    ||D F_t||<=exp(C_eta L^B T_N).                     (10)

For L=N^epsilon, choose epsilon>0 so that B*epsilon<1. Every fixed
dimensional fixed-time flow image, and the entire time-parametrized
sweep before exit, then have mass exp(o(N)). The sweep gains only the
additional factor T_N(1+sup||X||). No polynomial bound on this mass is
needed for the exponential-rate problem.

At the TARGET ACTION level the hitting-time map is also controlled:
the time is exactly phi(Z)-V-eta, whose derivative has a polynomial
bound in the recorded window. An arbitrary excluded-factor boundary
is different. Its first-hit time can have an unbounded derivative at
a grazing contact. Formula (10) must not be asserted for that first-hit
map without an additional argument. A regular collar level chosen by
coarea on the sweep controls the exit current; all such currents and
any original chain boundary must remain in the period identity.

More precisely, the
[independent coarea construction](quantitative_regular_phase_descent_coarea_audit.md)
uses H(u,z)=F_(u tau(z))(z), where tau=(phi(z)-V-eta)_+, and the
running maximum m(u,z)=max_(v<=u) rho(H(v,z)) of a Lipschitz nested-window
exhaustion. Coarea on the PARAMETER cylinder selects a legal level
r in (1,2) such that its entire slice, pushed forward with multiplicity,
has mass exp(o(N)). If the initial chain and its boundary have that
mass bound, the exact period identity is

    integral_C omega = integral_C_low omega
                           +integral_E_r omega-integral_B_r omega. (10a)

Here B_r is the original-boundary sweep and E_r is the COMPLETE
exit-associated slice. The latter can contain grazing curtains which
have returned to the interior after touching the collar. It must not
be relabeled as a current supported entirely on the collar hypersurface.
All three currents have controlled mass; only C_low has the proved
low-action support. The running maximum handles re-entry without a
first-hit-time derivative or discarded curtain.

Thus this statement bounds interior transport and its action-level
endpoint. It is not a license to omit a boundary current or to cross
an actual quantum pole. The latter is an excluded exit even if the
classical shape is algebraically regular there.

## 5. The full quantum symbol on shrinking strips

The defining-integral proof in
[the literature-state audit](literature_state_volume.md#21-a-uniform-complex-remainder-on-an-entire-horizontal-strip)
can be made quantitative in the strip width. For 0<b<=1 and
|Im z|<=pi-delta, 0<delta<=1,

    log Phi_b(z/(2 pi b))
       =Li_2(-exp z)/(2 pi i b^2)+R_b(z),
    |R_b(z)|<=C b^2 (delta^(-1)+log(2/delta)).          (11)

The constant is independent of Re z. Here are the bounds in that
integral argument. With c=-b^2/24 and

    K_b(t)=[1/sinh(b^2 t)-1/(b^2 t)]/(4t sinh t),
    H_b(t)=K_b(t)-c exp(-t)/t,

one has |H_b(t)|<=C b^2 for 0<t<=1 and
|H_b(t)|<=C b^2 exp(-t) for t>=1. Consequently its weighted L1 norm
with weight exp((1-delta/pi)t) is at most C b^2/delta.
The remaining explicit arctan(z/pi) is bounded by C log(2/delta)
on this strip, uniformly in Re z. Inserting these in the exact
remainder integral proves (11).

For the ACTUAL full function Psi_epsilon, substitute b^2=1/N and
its recorded half-step shift. Taylor's formula uses
|exp z/(1-exp z)|<=C/delta on the smaller angular strip. Hence, for
2pi/N<=delta<=1 and
delta<=epsilon Im z<=2pi-delta,

    log Psi_epsilon(z)
      =Li_2(exp z)/(epsilon*2pi*i/N)
           +(1/2)Log(1-exp z)+O(1/(N delta)).          (12)

All logarithms are the same selected-strip continuations as in the
exact definition. For the derivative estimate use a disk of radius
delta/4. At the threshold delta=2pi/N one must return to (11), rather
than reapply (12) with an inadmissibly smaller delta: throughout that
disk the shifted Phi argument has strip margin at least
3delta/4-pi/N>=delta/4. Its remainder and the half-step Taylor remainder
are therefore still O(1/(N delta)) throughout the disk. Cauchy's
formula gives, for every fixed k,

    |partial_z^k remainder|<=C_k/(N delta^(k+1)).      (13)

In particular delta=N^(-epsilon), with epsilon small, is allowed.
A fixed product of these full functions, original monomial factors,
Gaussian factors and rational source amplitudes has the actual W as
its leading phase with subexponential amplitude on this window.
This last assertion applies only where its rational denominators and
selected logarithmic strips are retained. It does not analytically
continue a finite cyclic atom across a Stokes boundary, and does not
drop the full-function moment ray corrections.

## 6. Consequence and exact remaining task

The final LOW-ACTION CHAIN obtained from an original scalar cycle by
the controlled transport above, with the stated initial mass bound,
has contribution bounded by

    exp(N(V+eta)/(2pi)+o(N)).                          (14)

This follows from (10), (12) and the triangle inequality on that final
chain. The exact Stokes identity expresses the original initial period
as its low-action contribution PLUS the retained exit-associated and
original-boundary sweep contributions. Even if every interior point
of an initial chain reaches the target level, its own boundary sweep
cannot be omitted. Estimate (14) by itself is not an estimate for that
initial chain's complete period. It requires no assertion that the
selected geometric saddle has nonzero coefficient, and is uniform
over all fixed knot words to which the actual phase construction applies.

The original period itself also contains the exit/boundary currents
created or retained in that transport. Equation (14) becomes the
desired whole-source bound ONLY after those currents have been
controlled at the same rate. The entire all-transfer-endpoint corner
has a separate subexponential estimate in
[the total-transfer packet theorem](actual_total_transfer_endpoint_packets.md).
Mixed endpoint/bulk currents, simultaneous coordinate/shape exits,
and source seams are not thereby estimated. They remain the concrete
obstruction, rather than an unquantified cost of regular interior
gradient descent.

The shrinking-strip calculation, including both signs and the exact
half-step normalization, has a separate
[independent integral audit](shrinking_strip_full_psi_independent_audit.md).
It corrected the displayed Hessian sign and supplied the derivative
argument at the smallest permitted strip width; both are incorporated
above. No computational sample is used to prove (6), (10) or (12).
