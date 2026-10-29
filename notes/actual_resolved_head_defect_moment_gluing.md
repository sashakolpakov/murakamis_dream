# A single resolved head defect is forced to match; multiple defects retain charge

28 October 2026. For a FULL finite canonical trace configuration of the
original braid source, one isolated noncentral head-endpoint mismatch
cannot survive: preservation of the actual lower (or upper) Borel moment
forces its missing normal match. This gives a regulator bound for that
specified class of restricted critical configurations. It is not an
exact deletion of the quantum endpoint current or a bound on its entire
period.

For several mismatches the same calculation gives an exact weighted
linear conservation law. There are genuine cycle charges. An explicit
closed defective Hurwitz configuration shows that independent
flag-stabilizer rescalings cannot in general be replaced by common
crossing frames. That example has action zero and is not an
excess-volume counterexample.

## 1. The original matrices and the endpoint relation

Use the classical limits of the ORIGINAL physical matrices in
[bounded quantum meridian transport](actual_bounded_quantum_meridian_transport.md):

    L_-(K,f)=[[1,0],[-K f,K]], L_+(K,e)=[[K,e],[0,1]],
    G=L_-^(-1)L_+=[[K,e],[fK,fe+K^(-1)]].             (1)

The parabolic leaf is fe+K+K^(-1)=-2, so G has determinant one and
trace -2. At a resolved lower endpoint write B=1-s and

    K=-B^(-1), f=tau, e=s^2/[B tau].                 (2)

Then s=0, tau!=0 gives

    G(tau)=[[-1,0],[-tau,-1]].                       (3)

The two sides of the physical head source may have tau_L!=tau_R.
This is an actual source possibility, not merely a bad coordinate:
the [resolved head calculation](actual_resolved_head_face_geometry.md)
and the [endpoint factorial chart](actual_endpoint_head_factorial_chart.md)
retain its finite window K_R(tau_L/tau_R), which is not supported
only at ratio one. The normal clock is the same on both sides; the
missing normal derivative is the logarithmic tau ratio.

The actual crossing canonical graph preserves BOTH Borel products.
For b heads put

    M_-=L_(-,b)...L_(-,1)
       =[[1,0],[-K_total F_total,K_total]],
    F_total=sum_j (K_1...K_(j-1))^(-1) f_j.           (4)

This is the leading canonical consequence of the literal original
Hopf intertwining, with no scalar or framing normalization changed.
The upper product similarly retains E_total and K_total. Both signs
of a genuine crossing preserve these moment matrices.

## 2. Precise one-defect theorem, including the original source premise

Consider an ORIGINAL one-component closed braid, with its justified
whole-word averaged trace source

    chi_N/N Tr[(I tensor g tensor ... tensor g)W_N]. (5)

Suppose a FULL restricted critical configuration has all the following
properties:

1. It lifts to a finite canonical composition of the genuine resolved
   local crossing graphs, in their actual order and with their actual
   tags. There is no other transfer face or auxiliary relation replacing
   a genuine local graph. A tangential critical point in an arbitrary
   cleared chart is not being assumed to have this property.
2. Every ordinary wire matches its full phase point. There is exactly
   ONE nonmatching wire, with the lower endpoint relation (2)--(3):
   K_L=K_R=-1, e_L=e_R=0, f_L=tau_L and f_R=tau_R, both finite and
   nonzero. The upper version is obtained by exchanging e and f.
3. The trace is taken at a regular cut away from that defect. Its full
   leading canonical closing is the identity. All original pivotal and
   marked factors remain. Any original source face that replaces this
   identity by a different relation must instead be counted as another
   defect; it is not silently ignored.

Then

    tau_L=tau_R.                                    (6)

### Proof

At a head j the difference of its two lower factors is

    Delta L_(-,j)=-K_j(tau_R-tau_L) E_21.

Every genuine crossing preserves M_-. Every other wire matches.
The regular trace fixed-point condition identifies the initial and
final physical phase points, so their M_- matrices are equal. Therefore

    0=M_-,final-M_-,initial
       =L_(-,b)...L_(-,j+1) Delta L_(-,j)
                                  L_(-,j-1)...L_(-,1). (7)

All left and right factors are invertible. Thus Delta L_(-,j)=0 and
(6) follows. This argument uses a complete canonical fixed point,
not a separate Ward equation for an arbitrarily restricted operator.

Here is why (5) provides the stated regular closing. In the original
physical index basis it is a diagonal trace pairing, hence identifies
the two clock variables and their exponentiated conjugate positions
at a full regular stationary point. The actual pivot is
g_a=x^(1-N)Q^(-a): its logarithm is order one in a/N, not order N.
It and the factor 1/N are retained amplitudes and introduce no new
leading canonical graph at a finite regular cut. The external chi_N
and the common Cartan lines do not alter that closing. The cardinal
source's exact integer modes shift logarithmic positions by integer
turns and leave these multiplicative matching relations unchanged.
Matched factorial frame changes cancel across the trace; replacing
only one side would not be the original source.

Consequently (7)'s top/bottom equality is supplied by the FULL original
stationary trace closing under property 3. It has NOT been inferred
from the operator equation [F_total,W_N]=0 after inserting a projector.
Indeed [F_total,P_R] is generally nonzero. This theorem does not set
that finite quantum rank-one current to zero.

## 3. Regulator consequence and its limits

After (6), every wire and crossing is on the genuine graph, so the
configuration is an honest parabolic knot representation. Apply the
representation-independent marked fundamental-cycle calibration in
[the actual regulator theorem, Section 5](actual_wall_critical_regulator.md#5-the-marked-fundamental-cycle-comparison-extends-beyond-faithfulness).
It uses generic auxiliary flags and sends forced repeated developed
vertices to zero in the normalized alternating complex. Finite shape
limits at 0,1,infinity contribute zero by continuity of D; one does
not have to deform an abelian knot representation through irreducible
representations to use this chain identity.

The omitted normal is the physical Log B=0 normal. Its contraction
with the real logarithmic coordinates in the phase-defect identity
is zero. After the restored match, all original integer logarithmic
marks are retained exactly as in the full critical calibration.
The actual representation-volume bound consequently gives

    |Im W_critical| <= Vol(S^3 minus K).              (8)

On a joint regular framed critical closure this also follows directly
from [the saturated compactification](saturated_critical_regulator_compactification.md).
No assertion that an arbitrary endpoint tuple lies in that closure
is used as a substitute for the restored physical matching above.

This conclusion concerns the one-defect configurations with the
three explicit properties above. The assertion that an arbitrary
restricted source face lifts to that finite composition remains a
separate check. In particular no escaping conjugating frame,
uncontrolled Bruhat denominator, second source defect or non-genuine
transfer relation is covered by the word "finite."

Nor does (8) bound the whole endpoint period, its transport mass or
its normal neighborhood. The exact beta normal-jet calculation shows
why evaluating a collision fiber is not enough for such a claim.

## 4. The exact multiple-defect boundary-to-interior charge equation

For several lower-branch head jumps the argument is still exact, but
its conclusion is a conservation law. Across a defect on head j,
lower triangular multiplication gives

    Delta M_- = -(K_j...K_b) Delta tau_j E_21,
    Delta F_total=omega_j Delta tau_j,
    omega_j=(K_1...K_(j-1))^(-1).                    (9)

The weights are evaluated at the actual time slice of that defect.
They depend only on the physical clocks, not on the tau jumps.
Crossings preserve F_total between defects; the defects do not change
K_total. For a closed canonical trace the exact necessary equation is

    sum_defects omega_j Delta tau_j=0.               (10)

With prescribed boundary moment difference b, the right side becomes
b. All weights are nonzero and rational in the actual finite clocks.
If r such jumps are treated as independent boundary data, this map
has an (r-1)-dimensional complex kernel when r>=2. The upper moment
does not eliminate these f-branch charges: e=0 on both sides, so its
jump is zero. Upper-branch defects have the analogous upper equation.

Thus (10) is a genuine exact forced Borel transport equation, but it
has retained homogeneous charges. It is not a coercive inverse for
all jumps. The rest of the nonlinear closed Hurwitz equations can
impose additional conditions; they must be proved, not replaced by
uniqueness of a proposed geometric solution.

### A stable forced transport with its kernel retained

Although (10) cannot remove the homogeneous charge, its forced part
does have a controlled inverse. Write A=(omega_1,...,omega_r).
In the Euclidean norm on these actual scalar tau-jump coordinates,

    Delta tau=A^* b/||A||_2^2 + h, A h=0,
    ||A^+||=1/||A||_2, ||I-A^+A||=1.               (10a)

If every physical clock in the relevant slices lies in
N^(-epsilon)<=|K_h|<=N^epsilon, then

    ||A^+|| <= N^((b_heads-1)epsilon)/sqrt(r).       (10b)

Here b_heads is the braid width, distinguished from the boundary
datum b. This is polynomial in N for a fixed word and fixed epsilon.
It does not normalize the unknown knot period or suppose h is small.

There is also a fully rational, holomorphic version, useful for the
frame torsor. Choose one defect p; its weight is always a unit. Keep
the other r-1 charges rho_j unchanged and set

    Delta tau_j=rho_j (j!=p),
    Delta tau_p=omega_p^(-1)
                               [b-sum_(j!=p)omega_j rho_j]. (10c)

All coefficients are rational in the actual finite clocks. Their
norms on that window are at most C_word N^(2(b_heads-1)epsilon).
Thus boundary data propagate stably AFTER the homogeneous charges
are supplied. This is a quantitative forced Borel flow, rather than
an inference that rigidity kills its kernel. The metric is explicitly
the scalar charge metric; no bound in an unmatched quantum fusion
frame is being asserted.
The weights here are the PRESCRIBED ACTUAL clock trajectory. Solving
(10c) does not assert that arbitrary rho_j leave later clocks unchanged
under the nonlinear R maps, or solve all of their fixed-point equations.
That feedback must remain in any use as an interior construction.

## 5. A closed free-charge example and a common-frame obstruction

There is an explicit family where these charges are real geometric
data of the defective canonical composition. Set on every head

    K_j=-1, e_j=0, f_j!=0, z_j=(-1)^(j-1) f_j.

All based meridians are then

    H_j=-I-z_j E_21.                                (11)

Direct substitution in the ORIGINAL based Hurwitz law shows that
BOTH crossing signs simply SWAP adjacent z_i,z_(i+1). Equivalently
their unbased f map is (f_i,f_(i+1))->(-f_(i+1),-f_i). This preserves
the lower Borel product exactly, as it must.

For any one-component braid the underlying permutation is a single
cycle. Choose two distinct nonzero numbers a,b and let the initial
z tuple equal b except at one position, where it is a. Its final
tuple differs at precisely two positions. Closing the other heads
honestly and allowing two endpoint jumps closes the entire finite
defective configuration. Their z charges are +(a-b) and -(a-b), so
(10) holds. Both jumps may be nonzero, while every crossing remains
on the genuine resolved graph. The window K_R evaluated at a/b or
b/a is not identically zero; for a/b=2 both are nonzero at every
finite R. This does not assert a nonzero integrated knot contribution.

These jumps cannot always be absorbed by common crossing frames.
For example use the actual one-component word (1,-2,1,-2) and the
initial tuple (a,b,b), a!=b, a,b!=0. At its first crossing the two
noncentral commuting nilpotents have the relation

    (H_2+I)=(b/a)(H_1+I).                           (12)

The ratio b/a is invariant under ANY COMMON SL2 conjugation of this
crossing. Commutation is likewise invariant. If all crossings of an
honest one-component Wirtinger representation have commuting incident
meridians, the under meridian is unchanged at every crossing; following
the knot makes every meridian the SAME matrix. Its crossing ratios
must therefore all be one. Equation (12) cannot become that honest
configuration by common crossing frames and matching wire frames.
Independent head rescalings would change (12), but those are precisely
the unproved extra covariance; they are not gauge equivalence of the
original local crossing configuration.

There is also a simple peripheral restriction. A diagonal stabilizer
conjugates U(tau)=I+tau E_21 by tau->d^(-2)tau. An actual peripheral
holonomy must centralize its noncentral meridian, forcing d^2=1.
Thus an arbitrary residual diagonal scale cannot be dismissed as
allowed longitude holonomy.

This free-charge example lies on the ALL-clock/all-transfer endpoint
stratum; its regulator is zero and that full endpoint packet already
has a subexponential operator bound. It is not a counterexample to
the volume upper bound. It does show that Borel conservation and
common-frame freedom alone do not remove multiple defect charges.

## 6. What is now proved

One finite, isolated head defect is restored at a genuine full trace
critical point, with the original source premise made explicit. Its
critical regulator is bounded by the knot volume. Several defects
satisfy the exact rational charge equation (10); there is no automatic
coercivity or common-frame removal. A general boundary estimate still
needs the complete multi-defect source or an additional controlled
transport of its homogeneous charges. No quantum endpoint current,
unknown knot period, or exponential normal contribution is divided out.

[Audit](../experiments/audit_actual_resolved_head_defect_moment_gluing.py):
original signed quantum Borel intertwining, exact triangular jump
weights, original trace-pivot scale and the closed free-charge example.
