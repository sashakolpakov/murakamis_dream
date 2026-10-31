# Historical transform port and actual mixed highest chart

29 October 2026. This records the algebra and mixed highest-chart route
available BEFORE the general coefficient bridge was completed. The
general original-source formula is now proved in the
[all-channel positive scalar and regular-cube theorem](actual_trivalent_all_channel_positive_scalar_and_regular_cubes.md),
using the [complete finite Euler--Racah transform](finite_trivalent_euler_racah_transform.md).
An independent, shorter coefficient bridge is the
[finite square-linearization proof](actual_trivalent_square_linearization_bridge.md).
The former missing identity(4) below is therefore established by those
proofs. This historical derivation and its audit do not themselves
replace either proof, and the separate mixed chart in section3 still
requires its recorded bending normalizations before source use.

## 1. Exact long and short series for the candidate factorial object

Put N>=2,d=N-1,q=exp(pi i/N),Q=q^2,F_n=(Q;Q)_n,s_n=|F_n|.
Take a=max(a,b,c), 0<=a,b,c<=floor(d/2), J=a+b+c>=d. Write

    r=b+c-a, delta=J-d.

Then 0<=delta<=r<=min(b,c), and every factorial below has index<N.
Define the positive OBJECT, without identifying it with the source,

    R=N sum_(t=a)^(b+c)
       s_t/[prod_(j=a,b,c) s_(t-j) s_(d+t-J)
                         s_(a+b-t)s_(a+c-t)s_(b+c-t)].

Its first summand is

    R0=N s_a/[s_(a-b)s_(a-c)s_(a-delta)s_b s_c s_r].

Direct factorial ratios prove

    R=R0 H_long,
    H_long=4phi3(Q^-r,Q^(a+1),Q^-b,Q^-c;
                  Q^(a-b+1),Q^(a-c+1),Q^-b-c;Q,Q).    (1)

Here series have their usual FINITE meaning
sum_k product(numerator;Q)_k Q^k/[F_k product(denominator;Q)_k].
For a direct check, put t=a+k, convert each sine factorial using
s_n=i^n q^[-n(n+1)/2]F_n, and reverse the three descending factorials.
The variable powers combine to (-q^(d+3))^k=Q^k. The term k=0 is
exactly R0. Thus (1) is an own ratio calculation, not a 6j formula.

The root relation gives Q^(a-delta+1)=Q^-b-c. Accordingly the series
is balanced. Apply the independently PROVED finite Sears identity in
[the elementary symmetric-operator proof](finite_balanced_sears_operator_proof.md),
with kept parameter alpha=Q^-b, transformed parameters
beta=Q^(a+1),gamma=Q^-c and denominator choices
D=Q^-b-c,E=Q^(a-b+1). It gives EXACTLY

    H_long=S_pref H_short,
    S_pref=(Q^(a+1);Q)_r(Q^-2b;Q)_r
                       /[(Q^(a-b+1);Q)_r(Q^-b;Q)_r],
    H_short=4phi3(Q^-delta,Q^-r,Q^-b,Q^-b;
                        Q^-b-c,Q^-b-c,Q^-2b;Q,Q).    (2)

The Sears proof is a finite polynomial operator calculation; no
published summation or quantum 6j identity is a premise. At the root
the new parameter Q^(-J-1) is Q^-delta, so the second sum stops at
delta. Every denominator in the old and new TRUE summation ranges is
a unit. In particular Q^-b and Q^-2b never reach a zero before their
allowed lengths r<=b and delta<=b. No zero prefactor is canceled by
an unspecified continuation.

This short series is the paired-parameter Askey--Wilson polynomial
of degree delta at z=1 with elementary operator parameters
A=D=Q^-b,B=C=Q^-c, divided by its explicit leading normalization.
Indeed ABCD Q^(delta-1)=Q^-r. This is an identification of the
PROVED finite series(2), not a source identification by that name.

## 2. The former source gate, with its exact normalization

The actual scalar A_source already has an independent
[root-Fourier coefficient theorem](actual_trivalent_root_fourier_source_certificate.md).
Let C_delta be its REVERSED coefficient in that note's(7), WITHOUT
the outer phase Q^[b(b+1)-c(c-1)]. Explicitly

    c_e=[U^e](U;Q)_c^2,
    C_delta=[U^delta](UQ^-b;Q)_b^2
                  sum_e c_e F_(2c-e)/F_(2c-e-r) U^e. (3)

Only 0<=e<=delta matter, and all its factorials are physical units.
Set

    E=3a^2+b^2+c^2-2ab-2ac+2bc-2c-2,
    K_source=N q^[E+2b(b+1)-2c(c-1)]/(F_a F_b F_c F_r).

Then the already proved source formula is A_source=K_source C_delta.
Combining(1),(2) with exact sine-factorial reflection proves that the
proposed equality

    A_source=(-1)^(N+J)q^[2a^2-ab-ac+bc-J-3]
                         *s_a s_b s_c/(N s_delta)*R

is EQUIVALENT to the following coefficient identity, now proved by the
complete transform and independent square-linearization bridge above:

    C_delta=Q^[b(a+c-b)+c(2c+1)]
       *F_(2b)/F_(a+b-c)
       *F_a^2/[F_delta F_(a-delta)^2] *H_short.        (4)

The equivalence here was proved separately from(4). To check the
phase, first multiply R0 by s_a s_b s_c/(N s_delta), then the Sears
prefactor in(2). In F-factorials this leaves
F_a F_(b+c)F_(2b)/[F_delta F_(a-delta)F_r F_c F_(a+b-c)F_b]
times its stated root phase. Divide by K_source and use
F_(b+c)F_(a-delta)=N(-1)^(b+c)Q^[(b+c)(b+c+1)/2].
All signs combine to the Q power in(4); the extra factor Q^(d^2+d)
is one. Also

    F_a/F_(a-delta)=(Q^-b-c;Q)_delta

EXACTLY at this root. Thus (4) is a short, normalized Rodrigues-type
target for the paired operator polynomial in(2).

The coefficient theorem proves A_source=0 when J<d. Its leading
coefficient also proves nonzero entire saturation layers delta0 and1.
Those facts and the finite comparisons alone did not prove(4) at
arbitrary delta. The completed finite proofs now supply that step and
establish the all-order positive scalar. No broad graph asymptotic
or geometric conclusion follows merely from(1)--(4).

## 3. An actual mixed highest chart with a simple right channel

There is a separate direct source-operator route to the same type of
recoupling problem. Write Q_j for the genuine ordinary highest-weight
2j module in its divided-F balanced basis, with

    F|u>=(1-Q^(u+1))|u+1>,
    Ecal|u>=q^(-2j-1)(1-Q^(2j+1-u))|u-1>,
    K|u>=q^(2j)Q^-u|u>.

Study highest vectors of weight2b in V_N tensor V_N tensor Q_a.
Their left physical pair degree at third color0 is

    D0=d+a-b.

For a physical pair vector w of that degree, the exact highest lift is

    H_L(w)=sum_(u=0)^(2a) alpha_u Ecal_12^u w tensor |u>,
    alpha_u=(-1)^u q^[u(4a+1)] Q^[-u(u-1)/2]
                                         F_(2a-u)/F_(2a). (5)

The last highest-vector equation is Ecal_12^(2a+1)w=0. Every earlier
equation follows directly from the ratio of the actual Ecal_3 and K_3
coefficients. The right highest chart is similarly

    H_R(w')=sum_(v=0)^d (-x q^(-2b))^v/F_v
                                    |v> tensor Ecal_23^v w'. (6)

Extracting first color0 from(5) gives the rectangular anti-Pascal map

    J_mix[B,A]=alpha_(D0-B) x^A
         Q^[(B(B+1)-D0(D0+1))/2]
         F_(D0-B)F_(D0-A)/[F_(D0-B-A)F_B],            (7)

where A is a first-pair physical color, B a right-pair physical color,
and entries outside the true physical ranges or A+B>D0 are zero.
This follows by the same finite coproduct binomial as the original
complete anti-Pascal chart. It is not a square inverse frame on an
unrestricted pair space; no polynomial conditioning is asserted.

More simply, extracting third color0 after the ACTUAL Omega_23 gives
on the valid highest source the upper-bidiagonal operator

    B_mix e_A=-(Q^(A+b+1)+Q^(-A-b-1))e_A
       +q^(2b+1)(1-Q^A)(1-Q^(D0-A+1)) e_(A-1).      (8)

For a>=1 this equality holds even on the entire displayed w space:
only third colors0,1 can reach that extraction, and their F_2 E_2
terms cancel. If a=0, the same expression agrees on the genuine
highest-source kernel Ecal_12 w=0; the absent third color1 must not
be invented for arbitrary w.

The right intermediate V_N has eigenvalue-2. It is SIMPLE in(8), at
A*=d-b: its diagonal equals-2 only when Q^(A+b+1)=1. A normalized
left eigenrow has support A=A*+k and closed entries

    ell_k=(-q^-1)^k Q^[k(k+1)] [a choose k]_Q[b choose k]_Q,
    0<=k<=min(a,b).                                  (9)

Its first entry is one. The direct ratio of the bidiagonal equation
is -q^-1 Q^(2k)(1-Q^(a+1-k))(1-Q^(b+1-k))/(1-Q^k)^2,
which proves(9). Its modulus is beta(a,k)beta(b,k), with unit phase
(-1)^k q^[k(a+b+1)]. No collision or even-level derivative is being
silently treated as simple: this is a DIFFERENT, genuinely mixed
V_N tensor Q_a channel, whose -2 node is simple at both parities.

The left ordinary channel c is the actual vector
W^(c)_(a+c-b) in degree D0, and has a regular generic Clebsch lift.
Equations(5)--(9) provide an explicit finite overlap to its simple
right channel. Relating that overlap to the original triangular
corner requires all the bending and 3j normalization factors. Those
factors are not proved merely from the existence of this chart. The
separate completed coefficient proof of(4) does not supply an unstated
normalization for this alternative mixed-chart route.

Audit: [root long/short Racah algebra and literal mixed highest-chart extraction](../experiments/audit_actual_trivalent_general_finite_transform_port.py).
