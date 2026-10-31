# Long filling from a spectral cover by original main-edge cuts

31 October 2026. Internally reviewed, unpublished sufficient theorem.
The conclusion is the original invariant's actual filled hyperbolic
volume. The sufficient covering condition below is not yet proved for
every eligible plat.

## 1. A full-source criterion that can change the cut

Fix an eligible original simple-white plat D at arbitrary fixed width
k>=2. Keep its ordered boxes, retained half twists, original peripheral
markings and a fixed endpoint permutation giving a knot. Write R for
its number of boxes and Phi=Vol(Y_D)/(2pi) for its drilled volume rate.
The actual twists n_e=epsilon_e-2p_e are fixed before the quantum level
N tends to infinity. Put d=N-1.

For every original MAIN edge m with adjacent faces a_m,b_m, define
the full polynomial coefficient

    S_(N,m)(delta)=[prod_(f!=a_m,b_m) L_f^d]
       prod_e H_(V_N(sigma_e))(L) |_(L_a_m=L_b_m=0),
    sigma_e=-2cos(2pi delta_e).

All ordered local polynomials and the R original spectral variables
are unchanged. The [all-MAIN marking theorem](research_arbitrary_main_edge_mark_transport.md)
gives S_(N,m)=S_N, the ORIGINAL full numerator, identically as a
polynomial in every spectrum. This is not an equality of projected
sectors. In particular a different choice of m at a different real
spectral point still bounds the same S_N.

In this Fourier formulation the local source contains V_N alone;
the retained half twists enter through n_e=epsilon_e-2p_e in the
original Fourier functional. They are not inserted into H a second time.

Let P_m be the compact original face-flow polytope for this coefficient:
each port has supply one, each unmarked face has target one, and the
two marked faces have target zero. For delta in the real torus
T^R=(R/Z)^R put

    B_m(delta)=max_(q in P_m) sum_e H_(|delta_e|_T)(q_e),
    B_*(delta)=min_(original MAIN edges m) B_m(delta).          (1)

Here |delta_e|_T is its distance to the nearest integer and H is the
original closed sharp local action from the
[uniform coefficient upper theorem](research_global_sharp_coefficient_limsup_majorant.md).
Every B_m, and hence B_*, is continuous. The flow polytopes are nonempty:
the actual packing at the adjacent marked pair supplies a complete
feasible flow. No new independent port radii occur in (1).

Choose a fixed a>0 so the closed real cube |delta|_infinity<=2a lies
inside the original full packet's strictly concave geometric chart.
Suppose

    max_(|delta|_T,infinity>=a) B_*(delta) < Phi.              (2)

Then there is T(D)<infinity such that, for EVERY independently signed
fixed integer vector p with min_e |p_e|>T(D),

    lim_(N->infinity) (2pi/N) log|K_N(K_D(p))|
                      =Vol(S^3 minus K_D(p)).                (3)

Both level parities and composite levels are included. There is no
slope-ratio restriction and no assertion of a threshold depending only
on k. A supplied 2k-plat gives bridge number at most k; exact minimal
bridge number needs its separate certificate.

The order in (2) matters. It is max_delta min_m B_m(delta), not
min_m max_delta B_m(delta). A single mark need not certify the whole
spectral complement. A finite cover by neighborhoods with different
marks is allowed, and all of them bound the same full numerator.

## 2. Uniform real bounds and a finite covering interpretation

The local coefficient theorem is uniform in the entire closed degree
and real spectral domain. For fixed D there are only polynomially many
integer incidence arrays. Applying the triangle inequality AFTER the
original face demands have been imposed gives, uniformly in delta,

    |S_N(delta)| <= exp{N[B_m(delta)+o(1)]}.                  (4)

The integer supplies and targets are d; rescaling by d gives P_m.
Replacing d/N by one changes the action uniformly by o(1), by its
proved closed-domain continuity. Protected exponents remain exactly
zero. Neither the local theorem nor this coefficient estimate uses a
flat-gap forest: it uses the unchanged local polynomials and actual
face incidence. There are finitely many original MAIN marks, so their
errors can be replaced by one uniform o(1). Equality of the full sources
then gives (4) with B_*.

By compactness, (2) is equivalent to the following finite-certificate
form: the closed spectral complement |delta|_T,infinity>=a has a finite
cover U_j, and for each j there are a MAIN edge m_j and gamma_j>0 with

    sup_(delta in U_j) B_(m_j)(delta) <= Phi-gamma_j.        (5)

For necessity choose a minimizing mark at each point, retain a strict
margin by continuity, and pass to a finite subcover. Sufficiency follows
by taking the smallest margin. The sets in (5) need not partition the
quantum sum or its Fourier integral. No derivatives of cutoffs or sharp
window boundary currents are introduced.

The [original full-source packet](general_full_spectral_numerator_geometric_packet.md)
already gives a nonzero relative asymptotic on the small geometric
complex chart, with the original action A_N, amplitude and primitive
face measure. Its limiting real action satisfies A_0(0)=Phi and has
negative definite Hessian there. After the fixed chart is shrunk,
strict concavity supplies a strict real gap on each compact annulus
eta<=|delta|_infinity<=a. The packet also bounds the entire small
real cube by exp{N[Phi+o(1)]}.

Together with (2),(4), this proves for every fixed eta>0 a gamma_eta>0
such that, at all sufficiently large N,

    sup_(real delta) |S_N(delta)| <= exp{N[Phi+o(1)]},
    sup_(|delta|_T,infinity>=eta) |S_N(delta)|
                                      <= exp{N[Phi-gamma_eta]}. (6)

Only the original full packet is used. A local packet at a newly
chosen cut, or an identification of its projected geometric action,
is unnecessary.

## 3. A real gap gives the needed complex strip

Here is a direct polynomial argument, so (6) is not mistaken for a
complex estimate. If F is a Laurent trigonometric polynomial of degree
at most d in each coordinate, and b(t) is a bounded upper bound for
log|F(t)| on the real torus, then

    log|F(x+iy)| <= 2pi d sum_j |y_j|
         + integral_(T^R) prod_j P_(|y_j|)(x_j-t_j) b(t) dt, (7)
    P_s(t)=sinh(2pi s)/(cosh(2pi s)-cos(2pi t)).

At s=0 the kernel means the point mass. It has total mass one. To prove
(7), write z=exp(2pi i delta_j). For y_j>=0, z^d F is a polynomial
holomorphic in the unit disk. The subharmonic inequality for its log
modulus bounds it by the Poisson integral of its boundary log modulus;
removing z^d costs exactly 2pi d y_j. For y_j<0 use z^(-1) instead.
Apply this one coordinate at a time, using the already bounded real
boundary data in the next coordinate. Zeros cause no problem: use the
subharmonic regularization log(|P|+epsilon) and let epsilon decrease.
This also proves the bound for an identically zero slice.

Apply (7) to S_N. Its separate polynomial degree in sigma is at most d,
so its Laurent degree in each exp(2pi i delta_j) is at most d. In (6)
use the real gap at eta/2 and the global upper bound Phi+epsilon.
If |x|_T,infinity>=eta, choose j with |x_j|_T>=eta. The Poisson mass
of |t_j|_T<eta/2 is at most C_eta |y_j| for |y_j|<=1: its circular
distance from x_j is at least eta/2, and the displayed kernel is
bounded there by C_eta |y_j|. Consequently, for |y_j|<=tau,

    N^(-1)log|S_N(x+iy)|
       <= Phi+epsilon-gamma_(eta/2)
                    +gamma_(eta/2) C_eta tau+2pi R tau.      (8)

First make epsilon small, then choose a sufficiently small fixed tau.
This gives a strict upper rate below Phi on the desired complex strip.
Fixed spectral derivatives have the same strict gap on a smaller
strip by Cauchy; use the real gap at eta/2 before shrinking so the
derivative circles stay in the covered region. Equation (8) is uniform
in N. It does not differentiate any spectral cover or change a mark
at a complex point.

## 4. Apply the whole-period argument to the full source

The proof of the [entire all-CROSS period theorem](general_all_cross_long_filling_volume.md)
uses precisely its two stated inputs: the relative packet H1 near zero
and the whole spectral strip gap H2 away from zero. All subsequent
estimates concern that entire polynomial and the ORIGINAL Fourier
functional. They also require separate evenness and period one, the
cosine polynomial degree bound, and the specified sine/Gaussian factors.
The full source S_N has all these properties.

Its H1 is the old full packet, including the raw sign (-1)^(dR), the
original powers of N and the same finite action A_N and determinant
H_N. Its H2 is (8). Apply that proof with S_N in place of its raw
all-CROSS coefficient. Endpoint values still vanish after the sine
factor is included, first endpoint derivatives match, and the second
derivative endpoint currents are retained in the three integrations by
parts. The infinite charge tail is handled on whole intervals; only
the same finite charge set is localized. Thus no new spectral-cycle
assumption or missing charge estimate is required.

The nonzero leading term is the old unit-charge packet, with the same
finite saddle, branch choices and all original framing/peripheral
factors. Its limiting critical value is the actual filled volume by the
[original marked action theorem](actual_cross_cofactor_marked_action.md).
In particular the right side of (3) is the FILLED knot's volume, not
Vol(Y_D). Enlarge the existing geometric and analytic long-filling
thresholds until their O_D(sum_e n_e^(-2)) loss is smaller than the
fixed complementary gaps. This choice works for all independently
signed fixed twists with sufficiently large minimum magnitude. This
proves (3).

## 5. A finite algebraic certificate at any original MAIN cut

There is also a directly checkable sufficient condition which does not
require solving (1). Choose ANY original MAIN edge m. Send its actual
packing contact to infinity; its two faces become the marked parallel
lines, and all other face curvatures L_f remain positive. This changes
the geometric normalization, not the ordered boxes or their peripheral
markings. The adjacent-mark construction in the
[absolute packing-capacity theorem](actual_smoothed_source_capacity_blocks.md)
gives the same complete rate Phi.

For each original ordered quartet (x,b,c,y) in this normalization, put
A=x+y. Suppose

    (A+b)(A+c) >= max(b^2,c^2) at EVERY port.               (9)

Then the full original long-filling conclusion (3) holds. More generally,
one may replace (9) by a finite cover of the actual non-CROSS sector
strings with shared positive radius witnesses, as in the
[finite-sector criterion](general_actual_sector_cover_filling_volume.md),
with these SAME two protected faces and all original face targets.

Here is the dependency check that extends those sufficient tests beyond
top marks. Their local CROSS/LEFT/RIGHT weighted estimates concern only
the unchanged ordered polynomials, including their protected-zero
specializations. The face coefficient is now exactly the same S_N by
the all-MAIN theorem. At the chosen complete packing, the endpoint cost
minus its ordinary targets is Phi by adjacent-mark capacity invariance.
The [triangle entropy inequality](actual_triangle_entropy_algebraic_balance.md)
turns (9) into strict local balance whenever a one-sided sector survives.
Protected overloaded middles give exactly zero sectors. Thus the proof
of the [balance criterion](general_complete_radius_balance_filling_volume.md),
or the finite-sector argument using its separate shared witnesses,
gives a uniform real gap for S_N-C_(N,m), where C_(N,m) is the newly
marked raw all-CROSS coefficient.

The [global CROSS spectral-gap proof](actual_global_cross_spectral_gap.md)
also applies to this coefficient: a MAIN pair cannot be the two
protected outer faces of a MATCHING port, each port has a nonmonomial
triangle, and the ordinary white graph remains connected. The last
fact follows from the simple triangulated sphere's connectivity after
deleting two vertices. These are precisely the zero-pattern and
connectivity inputs of its local estimates and common-phase sewing.
Its weighted endpoint exponent is again Phi. Consequently C_(N,m) has
a real gap away from zero, and hence so does S_N. The product-Poisson
argument supplies a complex strip if only real bounds have been used.

Now use the OLD full-source local packet and the full-period proof in
section 4. No projected-sector transport, new-cut regulator identity,
or rerouted flat-gap forest is required. This proves the claimed
any-MAIN version of the finite certificates. It does not assert that
(9) holds at some cut of every simple-white plat, or that changing the
cut strictly enlarges the underlying knot classes.

## 6. Scope of the remaining problem

The finite mark freedom removes the need to insist on one unfavorable
protected pair throughout an upper-bound argument. It does not assert
that (2), or any simpler balance certificate, always succeeds. A
uniform proof of that covering inequality for general eligible plats
would finish the stated long-twist conjecture through this theorem.
If its unsigned upper functional is too large, a cancellation-sensitive
bound for the same full source is still an alternative.

The exact local spectral maximization
[sum f(inputs)-f(sum inputs)](research_sharp_green_spectral_maximum.md)
can simplify conservative bounds on (1). One must keep the maxima over
the shared P_m and the order of the spectral/mark choices explicit.
Neither a minimum of separately optimized port bounds nor transport of
individual LEFT/CROSS/RIGHT contributions follows from the theorem.

## 7. Internal proof review

Root wrote and checked the argument. The geometry and cluster-source
reviewers independently read the complete proof, including the any-MAIN
certificate extension in section 5 and its cited source dependencies,
and reported PASS. They checked uniform finite-mark errors, the order
of minimum and maximum, the product-Poisson strip estimate, original
raw normalization, and the use of the old full-source packet in the
whole-domain charge argument. This is internal review, not external
peer review. The marking author separately checked the full-source
normalization and the certificate extension; the original half twists
occur exactly once, in the Fourier exponents. No numerical experiment
is used as a proof of the covering
inequality, whose universal validity remains open.
