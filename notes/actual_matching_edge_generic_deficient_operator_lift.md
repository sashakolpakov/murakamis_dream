# A specified generic exceptional-operator lift at nonreal deficient degree

30 October 2026. Independently reviewed. The original generic
exceptional polynomial has a source-preserving meromorphic lift to a
nonreal deficient-degree neighborhood. It uses the actual LARGE-channel
white numerators and an explicitly chosen moving-period factorial.
Every fixed genuine q derivative has subexponential relative cost in
shrinking folded-channel windows. At maximal folded channels the cost
is polynomial, at both parities.

The root value of this generic lift is exp(-2pi i v) times the earlier
phase-canceled entire kernel, where v is the target input row. This
integer character is one on the source lattice but is retained off it.
Negative channel-row poles are genuine divisors of the generic lift.
Neither a nonzero leading normal amplitude nor a nonzero transported
global cycle is asserted.

## 1. Which generic operator and which source germ

Fix N>=3, d=N-1, 0<=a<=floor(d/2), m=d-a, s=d-2a, and
zeta=q0 exp(epsilon), q0=exp(pi i/N), Q=zeta^2. All complex
powers use this Log zeta and the specified logarithmic row lifts.
Use the ORIGINAL generic identity

    p_a(Omega)=D_a/(rho_a beta_N) B^(-1) R^(-1) S_(2a),
    S_(2a)=W_a p_(2a) W_a^T,                             (1)

proved in the [actual exceptional polynomial theorem](actual_matching_edge_geometric_target_polynomial.md).
Here B is the actual nested cup bend and R the actual cyclic turn.
In particular this is not the regular complete-circle lift
W_a pi_a with a fixed root dual scalar. Its coefficient

    c_a(zeta):=D_a/(rho_a beta_N)
      =(-1)^a N^2 zeta^(a^2-2d^2)
          [2a]! [m]! / product_(j=1,j!=N)^(d+a+1)[j]     (2)

has the factor [N] canceled as an EXACT generic quotient. The actual
completed operator is E_a=D_a^(-1)p_a(Omega); dividing our lift below
by the same moving D_a gives that very generic germ and its jets.
All factors remaining in (2), D_a, and their inverses are root units.

For an original low-degree matrix entry put

    0<=u,v<=t<=d, h=v-u, ell=t-v,
    sigma=d-h, r=a-h.

The polynomial bandwidth gives zero identically in zeta when |h|>a.
On the SUPPORTED grid |h|<=a, inverse bending and the original turn
give the exact generic tensor entry

    [p_a(J_t)]_(u,v)
      =c_a W_a(d-v,u;r) p_(2a)(r)
              W_a(t-u,d-t+v;2a-r)
        /[(-1)^d zeta^(-d+2v) pV(v) pV(ell)].            (3)

All positions and cup orientations in (3) are literal. They are the
same ones used in the original physical-operator audit; no scalar
symbol is substituted for an operator.

## 2. Put both actual white factors in the same deficient chart

The [boundary/source theorem](actual_generic_boundary_gauge_and_source.md)
gives a finite continuation of the original white map:

    mathscr W_a(zeta;sigma,i)
       =(-1)^m zeta^[-d(sigma-m)+di-m(m-1)]
          H_m^B(Q^i,Q^(sigma-i))/F_m,
    B=Q^(-N), F_m=(Q;Q)_m.                              (4)

This is the actual LARGE generic numerator H_m. It agrees with every
physical white coefficient in both total-degree halves, not just its
root value.

The high factor in (3) can be reduced before any interpolation. For
the original Chevalley maps J_L|i>=zeta^[-(L+1)i]|L-i> and
S=P(J_d tensor J_d), the generic intertwiner identity is

    S W_a=kappa W_a J_(2a).

Its scalar is fixed without a square-root convention: at middle
channel row a the physical total is d, and S acts by zeta^(-Nd)
on that entire degree block. The column is nonzero, so

    kappa=zeta^[-Nd+a(2a+1)].

Consequently the EXACT generic reversal is

    W_a(d-j,d-i;2a-r)=zeta^[s(a-r)] W_a(i,j;r).           (5)

For (3), its second white factor is therefore
zeta^(s h) mathscr W_a(zeta;sigma,ell), and its first is
mathscr W_a(zeta;sigma,sigma-u). Both actual numerators have the
same complex total sigma. Equation (5) is proved on the finite source;
the displayed right side now specifies the continued high factor.
No off-grid conclusion is inferred merely from physical jet bounds.

## 3. The factorial lift and its original support

Let

    P=pi i/Log zeta,
    G_P(z)=(2pi/P)^z Gamma(z+1)
       * product_(k>=1) Gamma(Pk+z+1)
                      /[Gamma(Pk-z)(Pk)^(2z+1)],
    Fhat_P(z)=exp[(Log zeta)z(z+1)/2-pi i z/2] G_P(z).    (6)

The [moving-period factorial lemma](actual_moving_period_factorial_normals.md)
proves local convergence, meromorphic continuation, and

    Fhat_P(z+1)=(1-zeta^(2z+2))Fhat_P(z),
    Fhat_P(0)=1, Fhat_P(n)=(Q;Q)_n                       (7)

for every nonnegative integer n at which the finite product is
regular. In particular (7) agrees with every supported generic
factorial in (3), with highest weights d and 2a FIXED. They are
not replaced by P-1 as zeta varies.

Define the specified meromorphic cups by

    mathscr p_L(zeta;x)
      =exp(pi i x) zeta^[x(L-x-1)]
                       Fhat_P(x)Fhat_P(L-x)/F_L,
    mathscr pV(zeta;x)=N zeta^(-d^2) mathscr p_d(zeta;x). (8)

The factor exp(pi i x) specifies the original (-1)^x mark. Equations
(2), (4), (6), and (8) define the full local lift

    mathscr K_a(zeta;t,u,v)
       =c_a zeta^(s h)
          mathscr W_a(zeta;sigma,sigma-u)
          mathscr W_a(zeta;sigma,ell) mathscr p_(2a)(zeta;r)
          /[(-1)^d zeta^(-d+2v)
                     mathscr pV(zeta;v) mathscr pV(zeta;ell)]. (9)

For every original SUPPORTED physical entry this equals (3) for
generic zeta, hence matches all its genuine q jets. The lift of the
completed operator is mathscr E_a=D_a^(-1) mathscr K_a.

The original finite sum may discard the identically zero entries
|h|>a before its residue cycle is introduced. Small product circles
around its remaining original lattice points then evaluate this
same generic source exactly, with its other tensors and exposed
mark retained. Formula (9) is not claimed to match zero entries
on forbidden generic lattice slices: it is MEROMORPHIC there,
and its poles are part of any subsequent cycle transport.

In particular Fhat_P(r) has a pole at each negative integer r=-k,
k>=1. When 2a+k>=N, its complementary factor has a root zero at
P=N, and the root pole may cancel. This root cancellation does not
remove the generic divisor or its normal residue. The construction
does not differentiate a reflection with d=P-1.

## 4. The exact root character

Put beta_a=s_(2a)/s_a^2 and

    V_a(h)=product_(j=a+1)^m 2sin(pi(h+j)/N),
    z1=q0^(2u-sigma), z2=q0^(sigma-2ell),
    c=cos(pi h/N).

The previous entire ROOT kernel is

    K_ent=beta_a^2/N * V_a(h) R_a(z1;c)R_a(z2;c).

The specified generic lift has the exact meromorphic root identity

    mathscr K_a(q0;t,u,v)=exp(-2pi i v) K_ent.             (10)

Here is a phase certificate. The exact root reflection of (6) gives

    mathscr pV(q0;x)=N q0^(-d^2+dx),
    mathscr p_(2a)(q0;a-h)
       =N q0^[2a(a-h)-s h]/[F_(2a)(q0)V_a(h)].           (11)

The actual large/small root collision and Gaussian normalization give

    H_m^1=P_s(T)q0^(a sigma+a^2) beta_a R_a,
    P_s(T)=(-i)^s q0^[s((d-3)/2-h)] V_a(h),
    c_a(q0)=N^2 q0^(a^2-2d^2) beta_a,
    F_(2a)(q0) F_m(q0)^2
       =(-1)^d q0^[a(2a+1)+m(m+1)] N^2 beta_a.           (12)

Insert (11),(12) in (9). The nonconstant surviving exponent is
q0^(-2Nv)=exp(-2pi i v). The remaining integer sign is
(-1)^s q0^[(3a-m)N]=1. This proves (10) and fixes its character;
matching the physical grid alone would not have fixed it.

In the original circle coordinates R=sigma-u, S=ell, the normalized
entire circle coefficient in the
[regulator normalization](actual_matching_edge_deficient_packet_regulator.md)
satisfies

    C_a(sigma;R,S)
       =k_a N q0^[d(ell-u)] exp(2pi i v)
                                      mathscr K_a(q0;t,u,v). (13)

Thus the character of this specified generic lift cancels the
character from restoring the actual physical turn. The absolute
circle normalization is the one already fixed in that theorem.
The bare canceled-root K_ent and the root of (9) are different
off-grid functions, although they agree on the original lattice.

## 5. Full local generic-normal upper bound

Take a fixed compact neighborhood on which BOTH numerator arguments
in (9) belong to the joint deficient corridor, with all marked scaled
coordinates bounded. Require also

    |Im(sigma/N)|>=b>0,
    0<Re(v/N)<1, 0<Re(ell/N)<1                         (14)

with fixed margins. At a sufficiently small nonreal perturbation of
the actual deficient geometric frame these conditions hold. The two
channel-cup arguments r/N and (2a-r)/N then stay in fixed compact
sets with imaginary part bounded away from zero. The physical-cup
arguments remain in their canonical interior strips.

This perturbation exists in the actual common frame, not just in
formal source coordinates. In its disk chart the proved real frame
has z-w=-1+i d0 and prefix trace A2=-1-2/(z-w), with d0=1/sqrt(3).
Shift the real part of its global flag w0 by a small real e; the
actual white reflection then changes z-w to -1-e+i d0. At e=0,

    partial_e Log A2=-2/(1+d0^2),
    partial_e Sigma=i/[pi(1+d0^2)] !=0.

Thus a sufficiently small fixed nonzero e makes the normalized
degree nonreal. All the previous strict exterior, regular-chart,
ordinary-complement and numerator-corridor conditions persist by
openness. After choosing this frame, take its sufficiently small
compact neighborhood so that the lower bound in (14) is fixed.

For s=d-2a satisfying 0<=s<=eta N, with eta sufficiently small,
the root lift is nonzero on this compact and every fixed k>=0 obeys

    |partial_epsilon^k mathscr E_a|_0
       <=C_k N^(10k)(C N^20)^(2s) |mathscr E_a(q0)|.      (15)

The same estimate holds for mathscr K_a. In particular it has
subexponential relative cost when s log N=o(N), and polynomial
relative cost for bounded s, including both maximal folded parities.
It makes no claim at a fixed nonzero scaled separation s/N.

To prove (15), use the actual LARGE-numerator estimates of the
boundary/source theorem separately for the two specified whites.
On |epsilon|<=cN^(-10), each has ratio at most (C N^20)^s to
its nonzero root value. The moving-period lemma bounds each cup
and its inverse relative to its root value on this disk. For the
negative and above-N channel arguments it uses a fixed O(N)
integer shift into the canonical strip, whose sine factors avoid
zero because of (14). The fixed original factorials F_d,F_(2a)
and the scalar (2), D_a and their inverses have the usual harmonic
root-unit bound. Their relative variations are bounded on this
same disk. Every remaining monomial has exponent O(N^2) and hence
bounded relative variation there. Thus (9) is holomorphic in epsilon
throughout the disk and has the stated ratio bound on its boundary.
Cauchy's formula gives (15) for the LITERAL generic operator germ.

The nonreal-degree requirement in (14) is substantive. A claim
covering a real negative-integer channel row would cross the divisors
described in section 3 and is not a consequence of this theorem.
Likewise, (15) is an upper bound, not a relative asymptotic formula
with a nonzero leading normal coefficient. The original global cycle,
its crossed residues, complementary-source estimates and its selected
stationary coefficient remain necessary for a volume theorem.

Focused audit: [original generic operator, root character and full
normal lift](../experiments/audit_actual_matching_edge_generic_deficient_operator_lift.py),
with [saved results](../experiments/actual_matching_edge_generic_deficient_operator_lift_results.json).
Exact arithmetic passed 492 actual high-adapter four-jets and 608
original exceptional-polynomial four-jets, retaining 528 entries with
nonzero higher coefficients and the moving face scalar. The actual
nonreal-frame derivative was also checked symbolically. At 95 digits,
eight independent Barnes-product root-character checks, four literal
supported generic completed entries, twelve full generic normal checks,
and sixteen nonreal-deficient full-operator circle checks passed. The
largest root-character relative error was below 1.2e-94; the largest
literal generic/normal error was below 1.6e-91. Uniformity and all-fixed-
jet conclusions come from the proof, not these finite samples.

Primary-agent full analytical review: PASS. It checked the literal
generic p/E provenance, two large numerators, high reversal scalar,
root character and restored normalization, supported initial cycle,
and full relative upper bound with its nonreal-degree requirement.
An independent geometric/source review also checked the restoring
turn and the sign of the explicit actual-frame variation. Neither
review supplies a nonzero global period coefficient.

Independent full analytical review and fresh redirected audit: PASS. The
review independently checked the literal generic p/E germ and moving face
scalar, high reversal, every root-character phase, actual nonreal-frame
variation, retained meromorphic divisors and all-normal upper bound. The
replay reproduced every count and error bound above. It supplies no
nonzero leading normal amplitude or global cycle contribution.
