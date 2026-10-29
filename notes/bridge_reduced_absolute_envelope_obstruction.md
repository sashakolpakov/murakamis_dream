# The actual post-overbridge modulus envelope still exceeds knot volume

28 October 2026. Exact elimination of all overbridge interiors does NOT
make the remaining absolute-value optimization a geometric-volume
problem. There is a supported state of the newly reduced ORIGINAL 5_2
source with exponential modulus rate greater than 2.54. Its actual
geometric volume rate is less than 0.485. The original averaged cut,
both pivots and all bridge endpoint products are included.

This is a counterexample to a proposed absolute-envelope upper bound,
not to the invariant or the volume conjecture. It concerns the state
AFTER the proved simultaneous overbridge elimination. A subsequent
exact under-anchor/coefficient regrouping can create further
cancellations and is not contradicted by this calculation. In fact
the offending state's remaining wire-5 fiber has now been summed
EXACTLY to zero by the complementary-charge rule described below.

## 1. The actual continuous modulus on a monotone bridge cell

Let

    J(t)=integral_0^t log|2sin(pi u)| du,
    J(t+1)=J(t),
    P(t,l)=J(t+l)-J(t).                              (1)

For a bridge of m crossings let H1>=...>=Hm be its clocks divided by N,
let alpha_j=Arg(a_j)/(2pi) with any fixed lifted representatives,
and let theta_in,theta_out be its endpoint port phases divided by 2pi.
The exact source-preserving formula in
[the signed bridge theorem](actual_signed_overbridge_unwinding.md)
has limiting modulus action

    Gamma_B=J(H1)-J(Hm)-sum_j J(Delta_j)
       +P(1/2-alpha_1-theta_in,1-H1)
       +P(alpha_m+theta_out,Hm)
       +sum_j P(alpha_j-alpha_(j+1)+1/2,Delta_j),
    Delta_j=H_j-H_(j+1).                            (2)

Indeed the multinomial has action J(H1)-J(Hm)-sum J(Delta_j).
The signed original port identities give a_j b_j=Q^2 x, hence
b_j has limiting phase 1/2-alpha_j; the endpoint and link products
give the other terms of (2). The COMPLETE remaining monomial/scalar
prefactor has modulus between fixed constants times 1/N, as proved
in that note, so has no additional exponential action on the
original fixed-central grids. Its complex phase is retained.

For arguments whose central moduli stay away from one, the elementary
endpoint-aware product estimate gives

    log|(v_N;Q)_L|=N P(t,L/N)+O(log N),              (3)

when Arg(v_N)/(2pi)=t+O(1/N) and |v_N|=exp(gamma/N) with
fixed nonzero gamma. The estimate includes arcs ending at shape one:
split the logarithmic singularity from a smooth periodic part, or
compare its total variation after radial regularization at |gamma|/N.
Its Riemann-sum error is O(log N). Factorials have the same uniform
estimate. Exact root zeros, when present in another example, must
still be excluded by the actual polynomial support; (2) is not a
license to replace them by their continuous limits.

## 2. A genuine reduced state of the original 5_2 source

Use the actual three-braid word

    [1,1,1,2,-1,2],                                 (4)

identified independently with the same original 5_2 period in
[the whole-source proof](five_two_whole_source_reduction.md).
Use the regular propagated frames with initial c=(2,3,4), so their
central coordinates are (2,3s,4), s=(-1)^(N+1). Each crossing creates
two new wire variables, numbered consecutively after initial wires
0,1,2. Its port table is

| Crossing | Sign | Inputs | Outputs |
| --- | --- | --- | --- |
| 0 | + | 0,1 | 3,4 |
| 1 | + | 3,4 | 5,6 |
| 2 | + | 5,6 | 7,8 |
| 3 | + | 8,2 | 9,10 |
| 4 | - | 7,9 | 11,12 |
| 5 | + | 12,10 | 13,14 |

The EXACT overbridge paths are

    [0], [1], [2,3], [4], [5].                       (5)

Thus the original over-over variable 8 really has been summed out;
this is not a pre-elimination state or a word with only trivial
length-one bridges. Set the surviving labels to N/20 times

| Variable | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Label numerator | 13 | 8 | 11 | 18 | 3 | 2 | 18 | 6 | 4 | 16 | 13 | 19 | 4 | 10 |

Take the subsequence 20 divides N. The bridge clock lists are

    (1/2), (1/20), (3/5,7/20), (13/20), (3/5).       (6)

In particular the nontrivial monotonicity is STRICT. Its two spectator
under-strands have distinct original central parameters 3 and 4, so
the new link argument has central modulus 4/3 or its reciprocal,
not one. All original endpoint products likewise have central moduli
which are ratios of two distinct members of (2,3,4). Consequently
every product in this state is nonzero at every N in the subsequence.
No formal continuous state has been substituted for an actual support
point.

Substitution in (2), using J(1-t)=-J(t), gives exactly

    Gamma=-2J(3/20)-3J(1/5)-8J(1/4)
                         -2J(3/10)-2J(7/20)-2J(2/5)
       =2.5456403530804530135630814317531... .        (7)

## 3. The ORIGINAL boundary source is nonzero and has zero action

For the actual averaged first cut and two original closed pivots,
the boundary source in these normalized Fourier frames factors as

    C_0=K_N(z_(in,0))K_N(z_(out,0)^(-1))/N^2,

    C_i=x^(1-N)K_N(z_(in,i)/(Q z_(out,i)))/N, i=1,2,
    K_N(v)=(1-v^N)/(1-v).                           (8)

Here the comma in z_in,i denotes its head number. Formula (8) is
exactly F_0(e tensor g tensor g)F_final^(-1), with
e=ones/N and the ORIGINAL pivot g_a=x^(1-N)Q^(-a).
It is not a replacement trace or independent cap normalization.

The final braid permutation is a three-cycle. Each ordinary
geometric-series numerator in (8) is therefore 1-c_i/c_(pi(i))
with distinct positive c_i, so is nonzero. The two first-cut
numerators are nonzero because the relevant center moduli exceed
one. All denominators have modulus between a fixed constant times
1/N and a fixed constant. Thus the FULL boundary entry is nonzero
and bounded above and below by powers of N. It contributes zero
exponential action. This explicitly retains the phase and possible
cancellation of that source; no positivity is asserted.

The original framing, full Cartan scalar and optional full-state
modified dimension are label-independent unit or polynomial factors.
They also have zero action. Equations (2),(3),(7),(8) prove for this
COMPLETE reduced summand w_N that

    lim_(20|N) N^(-1) log|w_N|=Gamma.                (9)

## 4. The geometric rate is strictly smaller

The independently checked
[three-tetrahedron geometric calibration](five_two_selected_bloch_calibration.md)
gives Vol(5_2)=3D(v). Each positive ideal tetrahedron has volume at
most the regular tetrahedron value v3=D(exp(pi i/3)). The usual
angle-simplex concavity proof supplies that maximum directly.
Consequently

    Vol(5_2)/(2pi)<=3v3/(2pi)
       <0.485<2.54<Gamma.                           (10)

The actual value is approximately 0.45010961, but it is not needed
for this separation. The Arb audit rigorously encloses (7) and
the upper bound in (10), with a certified gap greater than 2.05.

The absolute sum of all remaining bridge/source states is at least
|w_N|. Its maximum over the actual monotone cells is therefore NOT
bounded by the hyperbolic volume rate. Exact overbridge unwinding
has not removed the need for further exponential cancellation.

This does not contradict the regular-critical-regulator theorem:
that theorem requires the FULL complex critical equations. A real
absolute maximum need not satisfy the missing phase equations.
Nor does this obstruct a later exact under-anchor/coefficient
reduction, which regroups the surviving states before any estimate.
It rules out the specific next step of identifying the present
absolute bridge envelope with Rivin's geometric maximum.

### The next exact cancellation is known for this witness

The [charged bridge phase calculation](actual_bridge_charge_phase.md)
proves an actual further wire identity: with
r=[label3-label6], H=[label6-label7], its wire-5 zero-frequency
coefficient is zero whenever r+H<d. In (7) these are r=0 and
H=3N/5, so the complete N-point wire sum is exactly zero at every
level in the chosen subsequence. The original caps are independent
of that wire and therefore retain the cancellation.

Thus the large individual summand is not being presented as an
uncontrolled global remainder. The next exact source projection
removes its whole fiber. The obstruction concerns taking absolute
values BEFORE that projection; the new phase-aware fusion is real
constructive progress beyond it.

[Audit and rigorous certificate](../experiments/audit_bridge_reduced_absolute_envelope.py)
and [saved results](../experiments/bridge_reduced_absolute_envelope_results.json).
