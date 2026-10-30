# A finite original-network source envelope at the resonant boundary

30 October 2026. Independently reviewed. Fix the labeled positive
right-angled matching-polyhedron certificate, actual cut and original
white-prefix dictionary of an augmented diagram with one main component.
On its single common boundary chart, the actual complete ROOT tensor
summand is nonzero.
Its specified regular complete-circle Hopf lift has fixed-quantum-jet
upper bounds of polynomial cost times (CN^C) to the sum of the channel
deficits. This includes all six original numerator types, both folded
parities, 202/202 pairs and c=1.

A positive triangulation alone does not supply the required polyhedron
and prefix data.

This is an UNCONTRACTED finite-network theorem. It retains the exact
first-normal identity for the original complete source, but supplies
no bound or noncancellation statement for its contracted finite sum or
relative period. The generic lift is the regular W pi lift already
proved for that identity, not the exceptional K/E germ and not the
entire moving-q germ of a complete crossing circle.

## 1. Specify the original generic tensor summand

Fix the original marked 2k-plat D with R complete-circle boxes and
retained half-twist signs epsilon_i. Put N>=3, d=N-1,
q0=exp(pi i/N), zeta=q0 exp(epsilon), Q=zeta^2. Fix actual folded
labels a_i, 0<=a_i<=floor(d/2), and write

    m_i=d-a_i, s_i=d-2a_i, S=sum_i s_i.

Use EXACTLY the regular Hopf lift from
[the full matching-graph source](general_matching_graph_full_normal_source.md),
sections 3--4. Its channel weights are held at their ORIGINAL root
values

    h0_a=k_a N s_(2a)/s_a^2,
    omega_a=q0^(d^2/2)(-1)^a q0^[a(a+1)],
    k_a=1 if 2a=d and k_a=2 otherwise,
    gamma_a=q0^(2-a^2)/N^2.                            (1)

They are all nonzero, including both maximal folded parities. In
particular h0_M=N at odd N and h0_M=2N/sin(pi/N) at even N.
Gamma_a is a FIXED root constant, not a generic norm to invert.

The original generic white has the specified finite continuation

    W_a(i,j;r)=(-1)^m zeta^[-dr+di-m(m-1)]
              H_m^(Q^-N)(Q^i,Q^j)/F_m,
    i+j=m+r, F_m=(Q;Q)_m.                              (2)

It is the actual LARGE source, m=d-a, in both physical degree halves.
For a fixed highest weight L<N define the original continued cup

    p_L(x)=exp(pi i x) zeta^[x(L-x-1)]
                    Fhat_P(x)Fhat_P(L-x)/F_L,
    pV(x)=N zeta^(-d^2)p_d(x), P=pi i/Log zeta.          (3)

Here Fhat_P is the specified moving-period Gamma product, agreeing
with the exact generic finite factorial at its admissible integer
arguments. The ordered cap is 1/p_L(L-x), with the same physical
scale when L=d. The complete-circle retraction is literally

    pi_a=gamma_a^-1 p_(2a)^T W_a^T
                           (ellV^T tensor ellV^T)P_rev. (4)

An explicit coefficient, useful for retaining every orientation, is

    pi_a(r;i,j)
      =gamma_a^-1 p_(2a)(2a-r)
            W_a(d-j,d-i;2a-r)/[pV(d-j)pV(d-i)].         (5)

The exact generic Chevalley identity also gives
W_a(d-j,d-i;2a-r)=zeta^[(d-2a)(a-r)]W_a(i,j;r).
Thus (5) retains the original channel cup, TWO physical inverse cups,
reversed tensor order and gamma_a. It divides by no paired root norm:
pi_a W_a=0 at a paired node is not a denominator in this theorem.

Expand every original coupon with (2),(4), and use the original physical
cups/caps and cyclic turns. Impose their literal integral affine head
constraints on an admissible stratum, with any primitive free-lattice
chart h=h0+A x. Let S_F(epsilon,h) be this ordinary CLOSED tensor
summand, including product_i h0_(a_i)omega_(a_i)^epsilon_i and an
ordinary cap at the exposed marked arc. At admissible integer heads
it is the actual finite summand of this specified regular Hopf lift.
No head is wrapped, and no support inequality is removed. Constant
forbidden strata retain their original zero value rather than being
assigned a meromorphic 0/0 continuation.

## 2. The one common geometric head assignment

Use the [original common boundary chart](actual_original_network_resonant_boundary_chart.md),
with r_frame=N rho, rho in a positive real compact, and
s_frame=exp(-2pi i alpha)-1, alpha in a fixed sufficiently small
positive compact. Every physical head has its ACTUAL canonical lift

    i=Nx-1/2, X=exp(2pi i x), 0<Re x<1.

The input/output two-head argument sums lie in the SAME interval
(pi,3pi), so their totals agree exactly, not just modulo N. Cups have
complementary lifts summing to d. Auxiliary heads are defined by
r0=i+j-(d-a), and both ends of each matching edge agree after the
recorded cup/dual reversal. Therefore h_N lies in the original
complex affine head chart. These are samples of the complete geometric
representation, not assertions of finite-a stationarity.

Require the shrinking-fold range S log N=o(N). For the estimates it
is enough first to assume each 0<=s_i<=eta N, for a sufficiently
small fixed eta. Then a_i/N stays in a fixed interior neighborhood
of one half and all the following margins are uniform.

Every physical i and d-i has real part divided by N in a fixed
compact subset of (0,1), with imaginary part divided by N of size
O(log N). For auxiliary heads put sigma=i+j. Exactly,

    r0=a+N(x+y-1),    2a-r0=a-N(x+y-1).                (6)

For 202/222, the canonical total gives
x+y=1-i Log(T_infinity)/(2pi)+O(1/N), T_infinity>0.
Both auxiliary real parts are consequently a+O(1), within an
interior factorial strip. For mixed outer degrees 200/220 and 002/022,
the two auxiliary arguments have opposite imaginary parts with
absolute value divided by N equal to (log N)/pi+O(1); their real
parts divided by N remain bounded. They lie in the nonreal exterior
factorial domain. Fixed integer offsets and all actual reversed
arguments preserve these margins. The only fixed integer factorials
are F_m,F_(2a),F_d and their original finite products, with indices<N.

Thus every factor and inverse in (2)--(5) satisfies the
[logarithmic-factorial theorem](actual_moving_period_factorial_logarithmic_escape.md).
The actual root and nearby generic factors avoid its poles and zeros.
This includes 202/202 and either folded parity; no physical-head
half-index offset is assigned to an auxiliary head.

## 3. Nonzero root product, with every exact factor retained

At the common chart every original white numerator has one of the six
proved boundary models. The source-normalized 200/002 Bessel factors
are nonzero: their common argument is
s_frame sin(pi m/N)/(pi rho), which is nonreal. The 202 whole polynomial
lies near its positive total ray, with its actual large-partner product
retained. The 220/022 determinant packets are nonzero on their actual
negative finite-clock rays. The 222 positive determinant retains its
finite clock perturbation and order-one trace correction. No202/202
pair or c=1 case is excluded.

Let B_v,N denote the exact scalar times normalized root model specified
by the applicable numerator theorem, evaluated at the ACTUAL finite
clocks. Keep every non-numerator factor of S_F(0,h_N) exactly, and
replace each H_m only by its B_v,N. Denote the resulting finite product
by B_F,N. Then

    S_F(0,h_N)=B_F,N[1+O_D(N^-1)],  B_F,N!=0.          (7)

In particular the uncontracted original root summand is nonzero for
large N. The original h0_a, gamma_a, omega_a, white monomials,
factorials, cups, pivotal clocks, half-index shifts and every integral
character remain in B_F,N. They are not normalized to modulus one.
Some have exponential or N log N size individually. Equation (7)
retains their exact joint product rather than bounding them separately.
The finite-clock determinant in 220 and the trace correction in 222
cannot be replaced by their limiting-clock values without their
specified order-one factors.

At the original exposed root mark, degree conservation after the other
caps forces complementary indices (d-x,x). The literal ratio of that
marked row to the ordinary cap is

    Xi_N(x)=N^-1 q0^(-d^2) Q0^(d x), Q0=q0^2.          (8)

Consequently the actual marked root summand on this same affine chart
is S_M(0,h_N)=Xi_N(x_N)S_F(0,h_N), and has the corresponding nonzero
packet Xi_N(x_N)B_F,N. The character in (8) is retained as written:
Q0^(dx)=exp(2pi i x)Q0^-x on a literal complex head, not merely Q0^-x.
No bare root mark is moved through a cap or promoted to a generic
covariant tensor.

For the chosen original first-cut chart its exposed physical clock is
A=(1+s_frame)^-1=exp(2pi i alpha), or the recorded complementary clock
according to the cap orientation. Thus x_N is real, equal to
N alpha-1/2 or N(1-alpha)-1/2, and

    |Xi_N(x_N)|=1/N.                                   (9)

This modulus statement is specific to that chosen real-alpha boundary
chart. It is not a claim that the marked character is harmless on an
arbitrary complex framing chart.

## 4. Every fixed generic jet of the specified lift

There are constants c_D,C_D and, for each fixed k, C_(D,k) such that
on |epsilon|<=c_D N^-10,

    |S_F(epsilon,h_N)/S_F(0,h_N)|
                     <=C_D(C_D N^40)^S,                (10)

and hence

    |partial_epsilon^k S_F(0,h_N)|
          <=C_(D,k) N^(10k)(C_D N^40)^S
                                       |S_F(0,h_N)|.   (11)

The derivative holds EVERY marked head h_N fixed. Its common geometric
construction is not rerun as epsilon varies.

Here is the proof from the actual factors. The genuine 200/002 theorem
gives bounded relative numerator variation on this smaller disk when
the nonzero Bessel factor is retained. The
[paired220 theorem](actual_q_hahn_paired_resonant_circle_packet.md)
gives cost C(CN^20)^s for 220; exact GENERIC reciprocity gives the same
for 022, including its marked complement and scalar. The
[positive-total theorem](actual_q_hahn_positive_total_boundary_normals.md)
gives that bound for 202/222, including possible zero single root edges.
Each matching edge has TWO original white numerators after (5) is
expanded. Their total cost is at most
C_D(C_D N^20)^(2 sum_i s_i)=C_D(C_D N^40)^S.

The factorial domain verification in section 2 gives bounded two-sided
relative variation for every cup factor, its inverse and fixed
factorial on the larger disk c/[N^2(1+log N)^2]. All monomial exponents
have size O_D(N^2(1+log N)^2), so their ratios are bounded on our
smaller disk. Gamma_a, h0_a and omega_a are the fixed root constants
of the specified lift and have relative ratio one. There are only
finitely many factors for fixed D. This proves (10) and its
holomorphy directly in the original regular factors. Cauchy's formula
proves (11).

Thus the cost is polynomial for bounded total deficit S, including
maximal folded channels at both level parities, and subexponential
whenever S log N=o(N). No fixed nonzero scaled channel-width estimate
is asserted. Nor is a nonzero leading normal amplitude inferred from
this relative UPPER bound.

## 5. The unchanged original first-normal identity and its limit

Let A_D,N be the original complete root source before its separately
recorded exterior framing line. On each label sector the specified
regular Hopf lift has ordinary closed value
F_a(epsilon)=D_N(epsilon)z_a(epsilon), with

    D_N(epsilon)=(-1)^d[N]_(q0 exp(epsilon)),
    nu_N=D_N'(0)=2N(-1)^N/(q0-q0^-1)!=0.

The exact source theorem therefore remains

    A_D,N=nu_N^-1 sum_a sum_(h in original support(a))
                                  partial_epsilon S_F(0,h). (12)

All sums in (12) are finite and retain their original affine constraints,
support, parity and mark. The full paired-circle first normal is already
contained in h0_a W_a pi_a at the root. No paired norm is inverted,
and no Hermite sector is removed. The regular lift need not be the
whole moving-q circle: any two regular generic Hopf lifts with the same
root coupon give the same marked scalar, because their closed difference
is D_N times a holomorphic open scalar vanishing at zero.

Combining (9),(11) with |nu_N|=N/sin(pi/N) gives the local bound

    |nu_N^-1 partial_epsilon S_F(0,h_N)|
       <=C_D N^9(C_D N^40)^S |S_M(0,h_N)|.              (13)

This retains the actual first-normal normalization and the actual mark
ratio. It is still a bound at the sampled complex head assignment.
Equation (12) is NOT evaluated by replacing its finite supported
summands by (13), moving their cycles to this chart, or identifying
the regular lift with the exceptional K/E germ. A contraction can
vanish although every local boundary factor in (7) is nonzero. The
original coherent band cycles, their boundary residues and the global
relative framing coefficient remain to be determined.

Focused audit: [literal regular source normalization and retained normals](../experiments/audit_actual_original_network_resonant_source_envelope.py),
with [saved results](../experiments/actual_original_network_resonant_source_envelope_results.json).
It compares (5) against 307 original categorical-dual coefficients and
their first jets, including 100 high-total coefficients. It retains
15 paired zero retractions and three simple retractions, checks 54
nonzero root scalars, six maximal-fold formulas and 33 actual mark/cap
ratios. All 307 tested coefficients detect the wrong first jet if the
fixed gamma_a is replaced by its tempting moving-q monomial. Two
original four-box plats, at opposite level parities, verify 32 retained
sector trace normals and both exhaustive full-color source sums. The
N=4 full source in that finite-field fixture is zero; no noncancellation
assertion is attached to the local envelope. Six symbolic checks retain
the affine offsets, reversed dual indices and marked character.

The common-chart, individual-packet and factorial bounds have their
separate focused audits. The finite-network inequalities here follow
by the displayed exact factorization and Cauchy's formula; they are
not a numerical estimate of a global period.

Independent full analytical review and fresh focused replay: PASS. The
source reader checked the literal reversed categorical dual (5), actual
LARGE white, fixed root gamma/h0/omega, both folded retraction types,
the retained physical trace normal and mark ratio, all six numerator
domains, and the two-large-factor deficit cost. The fresh replay
reproduced every reported coefficient, scalar, retraction, mark and
whole-source check, including the zero full-source fixture.

Independent geometric/source-domain review: PASS. The geometric reader
checked every physical and auxiliary moving-factorial argument, the exact
dual offsets, the real exposed first-cut head, the nonzero root product
with its finite-clock factors, and the N^9 normalization in (13).
Both reviews retain the specified regular-lift, uncontracted-product and
relative-upper-bound scope; neither asserts a global period coefficient.

Independent primary proof review: PASS. The primary reader checked the
literal complementary dual rows, fixed root weights, two-numerator
deficit cost, all moving-factorial domains, normalized mark and N^9
factor. The focused source replay is recorded separately; this proof
review supplies no global contraction or relative-cycle conclusion.
