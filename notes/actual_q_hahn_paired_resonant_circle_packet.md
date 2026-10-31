# A source-normalized paired resonant circle packet

30 October 2026. The incoming200 and
outgoing220 packets combine into the FULL original root circle
coefficient with its measure, turn character and finite clock corrections.
The actual generic220 numerator also has polynomial-cost fixed quantum
jets near the fold. With the specified moving-period cup lift, this
bounds genuine normals of the literal exceptional operator on the same
paired chart. A nonzero normal amplitude or global period coefficient
does not follow.

## 1. Keep both roots, the measure and the original character

Put d=N-1, a<=floor(d/2), m=d-a, s=m-a, q=exp(pi i/N), Q=q^2.
Use the normalized original circle coordinates (sigma;R,S), and put

    U_o=Q^R, V_o=Q^(sigma-R),
    U_i=Q^S, V_i=Q^(sigma-S), T=U_o V_o=U_i V_i,
    P_s(T)=product_(j=a)^(m-1)(T-Q^j),
    beta_a=s_(2a)/s_a^2, K_a=[2a choose a]_Q=q^(a^2)beta_a.

The logarithms of all four heads are the literal source lifts. The
[regulator normalization](actual_matching_edge_deficient_packet_regulator.md)
gives the exact full circle coefficient C_a. Substituting the original
normalization H_a=T^(a/2)K_a R_a and the actual root partner identity
H_m=P_s(T)H_a gives

    C_a(sigma;R,S)
      =k_a V_a(d-sigma) q^[d(R+S-sigma)-2a^2]
           H_m^1(U_o,V_o) H_m^1(U_i,V_i)
                         /[T^a P_s(T)^2].                 (1)

Here V_a(h)=product_(j=a+1)^m 2sin(pi(h+j)/N) and k_a is the
original multiplicity, including k_a=1 when 2a=d. Equation (1)
is used where its displayed denominator is nonzero; the original
coefficient has its previously proved removable continuation elsewhere.
It is an identity of the actual circle coefficient, not of its scalar
spectral symbol.

The h0_a-normalized literal turned W pi coefficient is
exp(-2pi i R)C_a. The
specified generic exceptional lift has the inverse root character
already recorded in its source theorem. These characters must either
be retained or canceled by that EXACT restoration. The retained half
twist multiplies C_a by its original kappa^epsilon nu_a^epsilon.
No cup, turn, fold multiplicity or channel unit is absorbed into an
unspecified constant in (1).

## 2. A relative full root packet

Assume m/N lies in a fixed compact subset of (0,1),

    U_i=N^2 kappa_i,  V_i in a fixed compact subset of C*,
    qU_o in a fixed compact subset of Re z<0.

Then V_o=T/U_o=N^2 kappa_o, with kappa_o bounded and bounded away
from zero. These hypotheses hold in a fixed sufficiently large-N
paired200/220 chart from the actual collar calculation in the
[complementary theorem](actual_q_hahn_complementary_hard_edge.md).
Set

    Z_i=(-1)^m Q^[m(m+1)/2] T^m
                      product_(j<m)(1-Q^j/U_i),
    K_i=sin^2(pi m/N)(V_i-1)/(pi^2 kappa_i V_i),
    M_o=I-(qU_o/2)H_-,
    A_N=k_a V_a(d-sigma) q^[d(R+S-sigma)-2a^2]
          Z_i V_o^m U_o^s K_a det M_o/[T^a P_s(T)^2].   (2)

Every factor in A_N is exact at the actual finite N and actual
finite-r frame. In particular det M_o has NOT been replaced by
its limiting-clock determinant: an O(1/N) change in qU_o can have
an order-one effect. The incoming whole-polynomial Bessel theorem
and the uniform relative220 determinant theorem imply

    C_a/A_N=J_0(2sqrt(K_i))+O(N^-1).                   (3)

The entire series sum_l (-K_i)^l/(l!)^2 defines this Bessel notation.
The error is uniform and absolute. On a compact where that series
is bounded away from zero, (3) is relative and C_a is nonzero for
large N. All factors in (2) are nonzero in this chart: |T| is
comparable to N^2, P_s and V_a have the same zeros there, and the
matrix M_o is uniformly accretive.

For the actual first-slot resonant chart r=1/(1-Q^-j)-b0 s_frame,
with fixed j!=0 and a first-cut clock A=exp(2pi i alpha),
0<alpha<1, the incoming limit is the proved
I_0(2j s_frame sin(pi m/N)), s_frame=A^-1-1. Its nonvanishing
for Re s_frame<0 was proved from the elementary radial ODE in the
[root boundary theorem](actual_q_hahn_resonant_hard_edge.md).
Thus this paired circle has a nonzero ROOT packet at those frames,
through both folded parities. The j=0 boundary and other prefix
patterns are not included in this statement.

There is also a nonzero off-node version: take r=N rho with rho
in a positive real compact and alpha in a compact subset of (0,1/2).
The actual geometric Bessel argument is
s_frame sin(pi m/N)/(pi rho), which is nonreal. The elementary radial
energy argument in the
[signed-prefix theorem](actual_right_angled_resonant_prefix_signs.md)
shows that J_0 has only real zeros. Thus (3) is relative on this
paired chart too. The original off-node source functional retains its
separate, nonzero limiting factor rho(1-exp(-1/rho))exp(t_coh/rho);
this does not identify t_coh with alpha or determine its unknown
whole-source coefficient.

## 3. Genuine generic220 control by a scaled original recurrence

Keep the heads sigma,R fixed with size O(N log N), put
q=q0 exp(epsilon), and use their actual powers U_o(q),V_o(q).
Let q0 U_o(q0), V_o(q0)/N^2 obey the preceding compact hypotheses.
For s=d-2a with 0<=s<=eta N, eta sufficiently small, the actual
LARGE generic numerator satisfies

    |H_m^B(U_o(q),V_o(q))/H_m^1(U_o(q0),V_o(q0))|
        <=C(C N^20)^s,  |epsilon|<=c N^-10.             (4)

For s=0 the right side is C. For s>0 the proof first bounds the
boundary circle and then uses holomorphy. Consequently every fixed k
has the corresponding Cauchy bound with the extra factor C_k N^(10k).
This is an upper bound for the original B=Q^-N deformation. It
does not differentiate the root collision in (1).

Here are the source and uniform estimates. Use the all-degree generic
monic recurrence R_(n+1)=(z+alpha_n)R_n+beta_n R_(n-1) proved in
the [paired-normal theorem](actual_q_hahn_near_fold_complex_partner_bound.md).
Its variables are b=q^sigma, z=b/U_o, so |b| and |z| are comparable
to N. Set G_n=R_n/z^n. Exactly,

    G_(n+1)=(1+alpha_n/z)G_n+(beta_n/z^2)G_(n-1),
    H_n^B(U_o,V_o)=V_o^n K_n G_n.                       (5)

For n<=a, all required spectral differences are at least cN^-2
on a small polynomial disk. The recurrence's original coefficient
b_n is O(N), b_n'=O(N^2 log N); its d_n is O(1), d_n'=O(N).
Using the original quotient formulas gives conservative bounds

    u_n=O(N^3), u_n'=O(N^6 log N),
    v_n=O(N^6), v_n'=O(N^9 log N),
    (alpha_n/z)'=O(N^5 log N),
    (beta_n/z^2)'=O(N^7 log N).                        (6)

These follow by the quotient rule with the ACTUAL spectral factors
(1-Q)B^-1Q^-n(1-B^2Q^(2n)) and their two-step analogues. Every
marked exponent remains O(N log N), and z'/z=O(N log N).

At the root the determinant for G_a is exactly

    M=I-(q0 U_o/2)H_--(q0^-1/(2V_o))H_+.

The proved H_+<=2H_-+8I shows Re M>=cI uniformly for large N.
Freeze its upper entries; their absolute values are bounded below,
since they are at least sqrt(B_n)(|q0 U_o|/2-|1/V_o|/2).
Set the corresponding generic lower entries to -beta_n/(z^2 upper_n)
and the diagonals to 1+alpha_n/z. This is the determinant in (5).
By (6) its operator perturbation is O(N^7 log N |epsilon|).
On |epsilon|<=cN^-10, the determinant ratio and its inverse are
bounded, as is the inverse matrix. Its final cofactor gives

    |G_(a-1)/G_a|<=C.                                  (7)

The actual scalar K_a has logarithmic derivative O(N^3); V_o^a
has logarithmic derivative O(N^2 log N). Thus H_a has bounded
two-sided relative variation on that disk.

On the boundary |epsilon|=cN^-10, each folded resonant spectral
difference is at least c|epsilon|; all others remain at least
cN^-2. Since b_n=O(N) and |z| is comparable to N, the scaled
recurrence coefficients in (5) are at most C|epsilon|^-1 and
C|epsilon|^-2. Propagating s rows from (7) therefore costs at
most (CN^20)^s. The exact scalar ratio K_m/K_a has 2s numerator
and 2s denominator factors; its denominator indices stay near N/2,
so it costs only C^s. Finally

    |V_o(q)^s/P_s(T(q0))|<=C^s.

This last estimate is why no artificial N^(2s) loss occurs: |T(q0)|
and |V_o(q0)| are both comparable to N^2, and the root partner
product is retained. It proves (4) on the circle. The original
finite H_m sum is holomorphic inside it, since m<N and all its
generic factorial denominators stay away from zero. The maximum
principle and Cauchy's formula apply to that full H_m, not to the
potentially singular monic R_m factors.

## 4. Restore the specified generic operator factors

For the paired chart also require the stated logarithmic-factorial
conditions for the actual cup arguments. Namely each canonical
physical argument lies in an interior real strip with imaginary
part O(N log N), or is an exterior argument with scaled imaginary
part bounded away from zero and bounded real part. Fixed original
integer factorials, including d=N-1, retain their fixed endpoints.
All marked heads are O(N log N).

This hypothesis is concrete for the paired reference box. With its
actual middle prefix Q1=e[[1,z0],[0,1]], the finite incoming second
clock is (1+z0 s_frame)/(1+(z0+1)s_frame), while the finite outgoing
first clock tends to -c^2. Choose a fixed first-cut compact on which
the former has an interior physical logarithmic lift. Such a choice
exists: for small positive alpha, s_frame=exp(-2pi i alpha)-1 and
that ratio is 1+2pi i alpha+O(alpha^2), independently of fixed z0.
When z0=0 it is exactly the first-cut A. The other physical and
channel-cup heads escape logarithmically with nonzero imaginary part.
Exclude the stated factorial divisors and retain every affine offset.

Use EXACTLY mathscr K_a and mathscr E_a=D_a^-1 mathscr K_a in
the [generic exceptional lift](actual_matching_edge_generic_deficient_operator_lift.md),
equation (9), including its original moving scalar c_a. Its two
white numerators are the incoming200 and outgoing220 factors above.
On the N^-10 disk, the genuine200 theorem bounds the first factor
relative to its nonzero root value; (4) bounds the second. The
[logarithmic-factorial theorem](actual_moving_period_factorial_logarithmic_escape.md)
bounds every cup factor and inverse relatively on its larger disk.
The fixed factorials, D_a and c_a are root units with polynomial
logarithmic derivatives. All retained monomial exponents have size
O(N^2 log^2 N). Therefore

    |partial_epsilon^k mathscr E_a|_0
      <=C_k N^(10k)(CN^20)^s |mathscr E_a(q0)|,           (8)

and the same holds for mathscr K_a. For s log N=o(N) this is a
subexponential relative cost, and for bounded s it is polynomial.
The root value and its physical turn are those used in (1)--(3).

This uses the literal generic exceptional polynomial germ. It does
not identify it with a generic W pi lift whose dual was fixed only
at the root. Equation (8) does not give a nonzero leading normal
amplitude. The local nonzero circle packet (3), even together with
(8), does not evaluate the original coupled band cycles or determine
the global relative framing coefficient.

Focused audit: [paired source, determinant and genuine normal checks](../experiments/audit_actual_q_hahn_paired_resonant_circle_packet.py),
with [saved results](../experiments/actual_q_hahn_paired_resonant_circle_packet_results.json).
The 140-digit run checks 24 exact full-circle normalizations against
the original white/channel-cup/physical-cap contraction, 24 retained
turn characters, two independent root Barnes-factorial contractions,
eight actual paired-frame root packets through both folded parities,
32 original scaled generic determinant identities and 32 independent
cofactor identities, 32 genuine large220 circle ratios, and 16 genuine
first/second numerator normals. The source error was below 4.2e-135.
The packet and disk samples are diagnostics, not proofs of the uniform
estimates. The full generic operator bound is the stated exact
factor-by-factor consequence; no full leading normal amplitude is
claimed by those finite tests.

The result is a nonzero local root-circle packet and the stated upper bound on genuine generic operator normals, with the marked source germ retained. It does not determine a leading normal amplitude or global relative-cycle coefficient.