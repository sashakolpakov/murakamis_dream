# Actual prefix signs at the right-angled framing boundary

30 October 2026. For the original
right-angled matching-polyhedron cut, the limiting clock signs are
determined by the OUTWARD face normals with their actual source lifts.
In particular every 222 pair has two negative limiting clocks, every
022/220 finite clock is negative, and every 202 total is positive.
There is no independent choice of signs or local framing.

The input is the labeled geometric certificate and the actual
white-reflection prefix dictionary. The statement is not asserted
for an arbitrary routed crossing that lacks that dictionary. It does
not compute the coefficient of a global selected period.

## 1. Keep the actual reflection lifts

Fix the original exposed first physical head, with positive marked
meridian J=[[1,1],[0,1]]. Its ideal fixed point p is infinity. The
exterior reference white face F_ref contains p. Indeed the first
head is the product of the two adjacent white reflections, and p is
their common ideal vertex. The exterior spine is the recorded one in
[the actual cut proof](actual_right_angled_selected_framing_obstruction.md),
section 3, not a newly chosen basing path.

For an outward UNIT spacelike face normal n write

    M(n)=[[n0+n3,n1-i n2],[n1+i n2,n0-n3]],
    H_f=adj M(n_f)=[[a_f,b_f],[bar b_f,d_f]],
    J_f=[[0,-1],[1,0]] bar H_f
                       =[[-b_f,-d_f],[a_f,bar b_f]].     (1)

The anti-linear map J_f followed by conjugation is its plane
reflection. The ACTUAL trace-minus-two prefix lift is

    Q_f=J_f bar J_ref.                                  (2)

Consecutive products telescope with these signs; this is precisely
the lift fixed by the original source dictionary. Multiplying
individual Q_f by arbitrary minus signs would change the clock signs
below and is not allowed.

The marked ideal vertex lies in the inward halfspace of every face.
For its null lift p=(1/2,0,0,1/2), this inequality is

    <n_f,p>=-(n0-n3)/2=-a_f/2<=0.

Consequently

    a_f>=0; a_f=0 iff p is on F_f,
    a_f>0 for every nonincident white face.              (3)

Strictness is exactly the nonincident supporting inequality in the
positive labeled certificate. Since a_ref=0 and det H_ref=-1,
|b_ref|=1. Multiplying the recorded matrices now gives

    (Q_f)21=-a_f bar b_ref.                              (4)

Thus all NONZERO lower-left prefix entries have the SAME phase
and a strictly positive real coefficient. This is an equality of
the actual SL2 lifts, not a projective sign convention inferred
after computing a ratio.

## 2. The boundary table with its real signs

In the common frame F(r,s)=[[r,1-r],[s,-s]], let L_f=Tr(Q_f Pi),
Pi=F E11 F^-1. For a nonincident face the leading term is

    L_f=(a_f bar b_ref/s)r^2(1+O(1/r)).                  (5)

For incident faces it is constant, by the actual cusp-stabilizer
calculation in the
[source boundary theorem](actual_q_hahn_resonant_hard_edge.md).
Fix s away from these finitely many constant-prefix zeros.

At an original circle, label the consecutive incoming white faces
F_0,F_1,F_2 as in that source theorem; the output has its own
middle face and the SAME outer faces. Put

    X=-L_0/L_1, Y=-L_1/L_2, T=XY=L_0/L_2.              (6)

With 0 denoting an incident/constant face and 2 a nonincident/
quadratic face, (4)--(6) prove the following limits:

| Pattern | Forced finite boundary data |
| --- | --- |
| 222 | X_infinity=-a_0/a_1<0, Y_infinity=-a_1/a_2<0 |
| 022 | Y_infinity=-a_1/a_2<0 |
| 220 | X_infinity=-a_0/a_1<0 |
| 202 | T_infinity=a_0/a_2>0 |

The a_i in this table are the positive coefficients in H_f, NOT
the complex prefix diagonals L_i. In 002 and 200 the finite ratios
of constant prefixes retain their actual dependence on s; the
paired Bessel packets already keep that dependence. The two outer
faces cannot both contain this marked MAIN cusp: their common ideal
vertex is the distinct auxiliary cusp of the disk. Thus 000/020 do
not occur in these original complete-circle boxes.

The same proof holds with every retained half twist. Its shaded
pairings and primitive auxiliary marking change, but the exact
outside white-reflection prefix loops (2) do not. It also proves the
signs for every original white interval and cup/cap adjacency to
which the same dictionary applies. It does not authorize an arbitrary
routed band to be assigned these original face labels.

### One main component gives every 200/002 Bessel calibration

Suppose the fixed retained-half-twist diagram has ONE main component;
the auxiliary crossing circles are still present. This is the relevant
connectivity hypothesis when subsequent independent full twists produce
a knot. Full twists do not change that connectivity. Every original
based physical puncture is then a conjugate of the marked primitive
main meridian or its inverse. In the recorded trace-minus-two lift it
has the form -g J^epsilon g^-1, epsilon=+1 or -1, with g an ACTUAL
element of the complete holonomy group.

In a 200 box both Q_1 and Q_2 fix infinity, so the actual second
puncture B=Q_2 Q_1^-1 does also. Its unique parabolic fixed point
implies g(infinity)=infinity. The complete torus-cusp stabilizer acts
by translations on its horospheres; hence g commutes with J. One can
also see the absence of another multiplier directly: a dilation would
make conjugates of J accumulate at the identity, while a nontrivial
unit-modulus rotation would give a fixed axis in hyperbolic space.
Discreteness and the free complete deck action exclude both. Therefore

    B=-J^epsilon in every original 200 box.

Likewise Q_0,Q_1 fix infinity in a 002 box, so its actual first
puncture is A=-J^epsilon. This is primitive meridian conjugacy, with
no added longitude, cusp translation or independent local basing.
It can fail when there is more than one main component.

The orientation does not change the Bessel parameter. For 200 write
Q_1=e[[1,z0],[0,1]], e=+1 or -1. Since Tr A=Tr B=Tr(BA)=-2,
B=-J^epsilon forces A_21=4epsilon. At r=N rho the actual raw clocks
give

    U_raw/N^2 -> -4epsilon rho^2/[s(1+z0 s)],
    V_raw -> (1+z0 s)/(1+(z0+epsilon)s).

Their actual white arguments remain q^-1 times these clocks. Substituting
these limits in the proved 200 Bessel parameter cancels epsilon and gives

    K=s^2 sin^2(pi mu)/(4pi^2 rho^2),   mu=m/N.

For 002 write Q_0=e[[1,z0],[0,1]]. Now A=-J^epsilon forces B_21=4epsilon,
and

    U_raw -> (1+z0 s)/(1+(z0+epsilon)s),
    N^2 V_raw -> s(1+(z0+epsilon)s)/(4epsilon rho^2).

The proved 002 parameter gives the SAME K. All constant-prefix zeros
remain excluded as above. Thus the original 200/002 Bessel theorems
cover every such original box in this one-main-component class,
including either orientation and every fixed retained-half-twist pattern.
At the literal Fourier scaling rho=1/(2pi i j), fixed j!=0, the limit
is I_0(2j s sin(pi mu)); it is nonzero when Re s!=0. This is a local
root-numerator conclusion, with exact normalizations retained in the
source theorem. It does not add a generic normal or a global period claim.

There is also a nonzero local choice compatible with the actual
[off-node source family](actual_braided_residual_framing_current.md),
section 5. Take rho in a positive real compact and
s=exp(-2pi i alpha)-1 with alpha in a compact subset of (0,1/2),
still avoiding the finitely many excluded constant-prefix zeros.
The packet is J_0(s sin(pi mu)/(pi rho)), with a nonreal argument,
and is therefore nonzero. For completeness, if J_0(z)=0, its radial
equation (t f')'=-z^2 t f for f(t)=J_0(zt), integrated against bar f,
gives z^2 integral_0^1 t|f|^2=integral_0^1 t|f'|^2>0; hence z is real.
On the same positive-rho compact the exact source family's limiting
factor rho(1-exp(-1/rho))exp(t_coh/rho) is nonzero as well. This is
compatibility of local parameter choices: the coherent variable t_coh
is not identified with alpha, and the unknown whole-source coefficient
or a selected cycle is not determined.

## 3. Actual half-index and factorial consequences

Retain physical head i=N x-1/2, with X=exp(2pi i x), exactly as in
the source boundary theorem. The actual white argument is q^-1 X,
not X. A negative finite limiting clock has a logarithmic lift with
Re x=1/2; a pair of them has canonical total Re(x+y)=1. This is a
boundary of the earlier strict physical packet, not a point claimed
to lie in one of its fixed compact subsets.

In particular the 222 finite head clocks stay away from X=0,1 and
infinity. The finite clocks of 022/220 do also. The remaining head
in 022/220 has imaginary part of order N log N; its actual factorial
normals have the separately proved
[logarithmic-escape control](actual_moving_period_factorial_logarithmic_escape.md)
when their stated argument hypotheses hold. Auxiliary rows still
come from i+j=(d-a)+r0 with the ACTUAL discrete a. They are not
assigned the universal physical-head -1/2 offset.

For 202 the total is on a positive compact ray for a fixed diagram
and boundary chart, so the whole-polynomial relative packet in the
source boundary theorem applies without changing the reference cusp.
For 220 the actual qU approaches a strictly negative ray, exactly the
domain of the complementary determinant packet; 022 is transported
by the ACTUAL generic reciprocity with its scalar and marks retained.

There is also a useful exact finite matrix consequence for the 222
LIMITING clocks, separate from an asymptotic statement. The original
small-channel determinant identity in the
[complementary source theorem](actual_q_hahn_complementary_hard_edge.md) is

    H_a^1(U,V)/V^a=[2a choose a]_Q
          det[I-(qU/2)H_--(q^-1/(2V))H_+].               (7)

The Hermitian matrices H_-,H_+ are positive definite for every actual
a<=floor((N-1)/2), including the fold. At the physical half-index
arguments U=q^-1 X_infinity, V=q^-1 Y_infinity, (7) contains

    I+|X_infinity|H_-/2+H_+/(2|Y_infinity|)>=I.          (8)

Thus this exact limiting-argument determinant is strictly positive.
For the large m=d-a the original forced partner product remains.
No generic derivative is obtained by differentiating that root
collision identity. Nor does (8) by itself replace the actual
r=N rho arguments by their limits: their O(1/N) perturbation can
change a determinant of size O(N) by an order-one factor.

The boundary dictionary supplies honest geometric domains for the
actual numerators and factors. It does not prove a full 222 packet,
erase finite offsets or characters, or supply the original relative
framing-cycle coefficient.

Focused audit: [actual signed cuboctahedral prefixes](../experiments/audit_actual_right_angled_resonant_prefix_signs.py),
with [saved results](../experiments/actual_right_angled_resonant_prefix_signs_results.json).
The labeled ideal right-angled cuboctahedron, cube matching in one
coordinate and marked main edge in another supply all six permissible
patterns. The audit retains the actual SL2 lifts and their trace-minus-two
heads; it checks 168 support inequalities, 24 right angles, six prefix
matrices, 16 ordered disk triples and two half-index identities.
Eight additional exact symbolic cases retain both primitive orientations,
both prefix lifts and both 200/002 endpoint formulas.

No generic partner differentiation, boundary asymptotic or global period is inferred.

The resonant-prefix calculation gives local nonzero packets and off-node information, not a whole-period estimate.