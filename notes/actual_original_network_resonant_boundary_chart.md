# One common resonant chart for the original certified network

30 October 2026. Independently reviewed. A fixed certified
right-angled augmented diagram with one main component admits ONE
original boundary chart in which all six permitted root-numerator
regimes hold simultaneously. The first-cut phase is small and positive,
and the boundary parameter rho is positive real. No independent local
conjugations, reference changes or optimized heads are used.

This is a statement about the original white numerators sampled from
the COMPLETE geometric representation. It is not a finite-channel
stationarity theorem, a generic-normal theorem, or a selected-period
calculation. The full source still retains its cups, measures, marks,
band sums and original support cycles.

## 1. Actual data and the common chart

Fix the labeled positive right-angled matching-polyhedron certificate,
the original exterior spine and white-prefix dictionary, and a fixed
retained-half-twist pattern for which the main strands form ONE
component. Auxiliary crossing circles remain present. The statement
applies to every original input and output white factor with that
dictionary; it does not label an arbitrarily routed extra band by an
original face. All constants below may depend on this fixed diagram.

Use its original exposed primitive meridian J=[[1,1],[0,1]], with
fixed point infinity, and its incident reference face F_ref. Retain
the actual reflection lifts of the
[signed-prefix theorem](actual_right_angled_resonant_prefix_signs.md):

    H_f=[[a_f,b_f],[bar b_f,d_f]], det H_f=-1,
    Q_f=J_f bar J_ref, (Q_f)21=-a_f bar b_ref,
    a_f>=0, with equality precisely at incident faces.       (1)

There is a useful further consequence of this ORIGINAL meridian
normalization. The other adjacent white face at its ideal vertex has
actual prefix -J^epsilon, epsilon=+1 or -1, according to the recorded
orientation. Its diagonal gives b_neighbor=-b_ref. Its upper-right
entry then gives

    b_ref(d_ref+d_neighbor)=epsilon.

Both d entries are real, and |b_ref|=1. Hence b_ref=+1 or -1. In
particular the common phase in (1) is REAL in this specified global
normalization. This does not choose new signs for individual lifts.

In the actual two-parameter frame F(r,s)=[[r,1-r],[s,-s]], put

    s=exp(-2pi i alpha)-1,  r=N rho,
    alpha>0 small, rho>0.

For each prefix Q_f=[[A,B],[C,D]], its diagonal is exactly

    L_f=Tr(Q_f F E11 F^-1)
       =-C r^2/s+(A-D+C/s)r+D+Bs.                         (2)

The complete cusp-stabilizer argument in the
[original boundary theorem](actual_q_hahn_resonant_hard_edge.md)
gives the following two alternatives:

    a_f=0:  Q_f=e_f[[1,z_f],[0,1]],
             L_f=e_f(1+z_f s), e_f=+1 or -1;
    a_f>0:  L_f=(a_f b_ref/s)r^2[1+O(1/r)].              (3)

There are finitely many such constants. Since s=-2pi i alpha+O(alpha^2),
every constant L_f tends to e_f as alpha tends to zero. Thus one
alpha_0>0 makes all constant prefixes nonzero for 0<alpha<alpha_0.
The frame is invertible since s is nonzero.

All subsequent uniform statements mean alpha in a fixed compact
subinterval of (0,alpha_0), rho in a fixed compact subset of (0,infinity),
and N sufficiently large depending on those compacts and the diagram.
The coefficients and errors in (3) are then uniform. No limit taking
alpha to zero together with N is asserted.

## 2. Simultaneous signs and canonical logarithmic lifts

At each original half disk use its ACTUAL ordered faces and clocks

    X=-L_0/L_1, Y=-L_1/L_2, T_raw=XY=L_0/L_2.          (4)

The input and output share their outer prefixes, but may have different
middle prefixes. The original auxiliary longitude and the marked main
cusp are distinct, so 000 and 020 are excluded by the signed-prefix
theorem. Keep every other possibility, independently at the two halves.

For transitions between a quadratic and a constant prefix, (3) gives

    X/N^2 -> -a_f b_ref rho^2/[s e_g(1+z_g s)]
                 for a quadratic-to-constant transition;
    N^2 X -> -e_f s(1+z_f s)/(a_g b_ref rho^2)
                 for a constant-to-quadratic transition.   (5)

Because b_ref and e_f are real signs, their leading imaginary parts
as alpha tends to zero are nonzero: of order alpha^-1 in the first
line and alpha in the second. Shrinking alpha_0 once therefore keeps
every one of these finitely many limiting coefficients off the real
axis, simultaneously. Finite-r corrections preserve this separation
for large N. In particular no escaping physical clock is on its
positive-ray logarithmic seam.

Ratios of two quadratic prefixes give the strict signs already proved
from positive face normals. Ratios of two constant prefixes in an
original 200 or 002 box have the primitive forms proved by the
one-main-component corollary: the corresponding puncture is -J^epsilon,
not an arbitrary cusp translation. Their finite clock is

    (1+z0 s)/(1+(z0+epsilon)s)
       =1+2pi i epsilon alpha+O(alpha^2).               (6)

It also avoids the positive-ray seam and the value one for sufficiently
small positive alpha. The resulting simultaneous table is

| Pattern | Limiting data and applicable root model |
| --- | --- |
| 200 | X/N^2 nonzero, Y finite nonzero; last-term Bessel packet |
| 002 | X finite nonzero, N^2 Y nonzero; first-term Bessel packet |
| 202 | X/N^2 and N^2 Y nonzero, T_raw positive; relative full-polynomial packet |
| 220 | X negative finite, Y/N^2 nonzero; complementary determinant packet |
| 022 | N^2 X nonzero, Y negative finite; its exact reciprocal packet |
| 222 | X,Y negative finite; positive determinant with retained trace correction |

The negative limits stay off the positive seam too. Hence every
physical head in these original factors has its canonical logarithmic lift
x=Log(X)/(2pi i) with 0<Re x<1. The original cup/cap inverse clocks
then have complementary canonical lifts. The physical finite index
is i=Nx-1/2, so its ACTUAL white argument is Q^i=q^-1 X, with
q=exp(pi i/N) and Q=q^2. Do not drop this half-index factor.

The input/output totals agree EXACTLY, not just modulo N. To see
the required carry, all original two-head canonical argument sums
lie in the SAME open interval (pi,3pi). For 222 and 202 they tend
to 2pi. For 220/022 one argument tends to pi and the other stays
strictly between zero and 2pi. For 200, the primitive formulas in
the signed-prefix corollary give an escaping argument
3pi/2+O(alpha) when epsilon=+1 and pi/2+O(alpha) when epsilon=-1.
The corresponding finite argument from (6) is O(alpha)>0 or
2pi-O(alpha), respectively. Their sums are therefore
3pi/2+O(alpha) and 5pi/2+O(alpha). The 002 formulas give the same
two alternatives. Shrink alpha_0 and then take N large so all these
statements have a uniform strict margin. The two halves have EXACTLY
the same product T_raw. Their complex logarithmic sums can differ
only by 2pi i times an integer, and their argument sums lie in an
interval of length 2pi; hence they are equal. This proves their
auxiliary matching rows agree after the physical half-index shift.
It does not assume independently reset local degree logarithms.
These are the PHYSICAL input/output rows of the matrix coefficient.
The underlying literal dual white instead has heads (d-j,d-i), total
2d-sigma and row 2a-r0. Its exact source reflection is retained:
with A0=Q^d, the numerator transforms by
H_m(A0/V,A0/U)=A0^m(UV)^(-m) H_m(U,V), and the full white by
W_a(d-j,d-i;2a-r0)=q^[(d-2a)(a-r0)] W_a(i,j;r0).
These are the recorded generic source identities, with their marked
affine heads. The dual white rows are not asserted to equal r0.

For 202, the two escaping limiting clocks are nonreal and have a
positive product. Their canonical arguments in (0,2pi) therefore add
to 2pi. At finite N their product lies near the positive ray, and
continuation gives the exact marked choice

    q^(sigma+1)=-sqrt_near_positive(T_raw),
    sigma=i_1+i_2,   Q^sigma=Q^-1 T_raw.               (7)

Here sqrt_near_positive is the branch positive on the limiting ray.
Equation (7) is forced by the two original head lifts; it is not a
freely chosen total square root. The same conclusion holds for 222,
whose limiting two canonical arguments are both pi.

There is NO exclusion of a 202/202 pair, of a rectangle with c=1,
or of T_raw tending to one. The argument is applied to both actual
middle prefixes and uses only the same finite set of original faces.

## 3. What the root-numerator packets now imply

At every matching edge retain its actual integer channel
0<=a<=floor((N-1)/2), put m=N-1-a, and define the auxiliary row
by the original equation i_1+i_2=(N-1-a)+r0. No universal physical
-1/2 offset is assigned to auxiliary heads. Thus all finite degree
constraints hold, but these samples of the complete parabolic
representation are NOT asserted to solve the deformed finite-a
stationary equations, especially when m/N is away from one half.

Suppose each actual m/N stays in a fixed compact subset of (0,1).
For the allowed folded channels this also keeps a/N away from zero
for large N. The same geometry identifies the actual factorial domains.
Every physical head i and d-i has real part divided by N in a fixed
compact subset of (0,1), and imaginary part divided by N of size
O(log N). Exactly,

    r0=a+N(x+y-1),  2a-r0=a-N(x+y-1).

For 202/222, x+y=1-i log(T_infinity)/(2pi)+O(1/N), so both
auxiliary real parts are a+O(1), in an interior factorial strip.
For mixed outer degrees, their imaginary parts have opposite signs
and absolute values divided by N equal to (log N)/pi+O(1), with
bounded real parts divided by N. They are nonreal exterior arguments.
The literal dual exchanges these auxiliary complements and reflects
physical heads by d; it preserves the stated margins. Fixed integer
factorials F_m,F_(2a),F_d have indices at most d. Thus these arguments
meet the hypotheses, including divisor avoidance, of the already
proved [logarithmic-factorial theorem](actual_moving_period_factorial_logarithmic_escape.md).
This identifies source-factor
domains; it does not replace a full regular-lift normal estimate.

The finite list of numerator parameter limits in the table lies in
the compact domains of the already proved root theorems:

* The [200/002 theorem](actual_q_hahn_resonant_hard_edge.md) has the
  same limiting Bessel parameter at every such box,
  K=s^2 sin^2(pi m/N)/(4pi^2 rho^2), independent of its primitive
  orientation. Choose alpha_0<1/2. The corresponding J_0 argument
  s sin(pi m/N)/(pi rho) is nonreal and its value is nonzero by the
  radial energy identity in the signed-prefix corollary. On the fixed
  parameter compacts these values are uniformly bounded away from zero.
* The same source theorem's 202 packet keeps its full small-channel
  polynomial and the exact large-partner product. Its total is near
  a positive compact, away from the negative polynomial-root ray.
  Since a/N is separated from zero, the forced partner factors stay
  uniformly away from their unit-arc zeros, even if T_raw tends to one.
* The [complementary packet](actual_q_hahn_complementary_hard_edge.md)
  applies to every 220 box. Its exact reciprocity, including the scalar
  and marked head lifts, transports every 022 box to that domain.
* The [negative-clock theorem](actual_q_hahn_negative_clock_boundary.md)
  applies to every 222 box. Its O(1/N) clock perturbations retain the
  order-one trace term; replacing the finite clocks by their limits
  without that correction is not asserted.

These models give nonzero root numerators for all sufficiently large N
and uniform relative errors O(1/N) after their stated exact scalar,
endpoint-product and trace normalizations. There are only finitely many
original factors. Their literal product therefore has the product of
these normalized root models with relative error 1+O_D(1/N). This is
only a finite product statement for these specified numerator values;
it does not estimate a sum over the original shared head variables.
Every model retains its actual finite clocks and total, as specified
in its source theorem. The limiting signs select its domain; they do
not license replacing a degree-O(N) polynomial by its limiting-argument
value.

The positive-rho chart is also compatible with the actual off-node
family in the [braided current theorem](actual_braided_residual_framing_current.md):
set p_N=1-1/(N rho+b0 s). Its known coherent boundary factor tends to
rho(1-exp(-1/rho))exp(t_coh/rho), which is nonzero. The coherent variable
t_coh is not identified with alpha, and the whole-source scalar multiplying
that factor remains unknown. No source-to-framing degree or nonzero
relative-cycle coefficient follows from the common numerator chart.

Focused audit: [actual simultaneous charts and source packets](../experiments/audit_actual_original_network_resonant_boundary_chart.py),
with [saved results](../experiments/actual_original_network_resonant_boundary_chart_results.json).
Two original main references of the signed ideal right-angled
cuboctahedron cover all six patterns and both primitive orientations.
Its cube matching retains the spherical ribbon order and has a literal
one-main-component parity witness (0,1,1,1). A supplemental actual
octahedral pair tests 202/202 and total one; that supplemental reference
is NOT asserted to be a main edge in the one-main-component class.
The audit keeps this distinction rather than assuming such pairs away.
At 100 digits it passes 288 exact paired-total checks, 1152 physical
head/cup checks, 3456 auxiliary-factorial domains, 320 marked square-root
checks, 576 simultaneous half-disk domains, 1152 finite-r clock checks,
and 288 literal root packets with 288 full dual numerator/white-turn
identities. The largest paired-total error is below 3e-101, the largest
dual identity error below 1.9e-91, and max N times packet relative error
is 0.01491. These are focused finite checks; the written proof supplies
the uniform existence and error claims.

Independent full analytical review: PASS. The coherent-source reader
checked the real reference coefficient, common small-phase seam exclusion,
primitive orientation signs, exact (pi,3pi) total-carry argument, physical
and auxiliary offsets, both marked total branches, every root-numerator
domain and the finite-product error. This review includes 202/202 and
c=1; it does not supply a generic bound, finite-color critical point or
global relative-cycle coefficient.

The primary reader independently passed the common-chart proof, including
the real reference normalization, simultaneous seams and exact total carry.
The source reader additionally checked the literal dual total, auxiliary
complement, generic reciprocal factor and full white-turn monomial, then
freshly replayed the complete focused audit: PASS. Both the geometric
factorial-domain classification and the distinction between the main
fixtures and the supplemental 202/202 pair are retained. No source sum,
generic normal amplitude or contributing cycle is inferred.
