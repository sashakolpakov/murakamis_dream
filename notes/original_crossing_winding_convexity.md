# The original state has charged simplex amplitudes and a retained quadratic phase

28 October 2026. This is a statement about the original enhanced Kashaev
state, before a Fourier or Fermat change of basis. Each nonzero crossing
entry has four nonnegative factorial indices adding to N-1. Its absolute
action is concave on that charged simplex, strictly concave on each face
with at least three positive coordinates. The exact phases are quadratic
and remain indispensable: reversing a crossing leaves its entire support
and every absolute weight unchanged.

The original cut forces the state onto proper faces. In particular,
one must not assume an interior optimizer of the four-angle action is
accessible to the original source. The
[first-strand support reduction](original_source_cyclic_variation_peeling.md)
proves that the first head stays zero and gives the corresponding exact
q-Pascal boundary operator, including the two unit-modulus end crossings.
No broad volume-conjecture estimate follows from concavity alone.

## 1. Both actual crossings have the same charged support

Use Q=exp(2 pi i/N), s=exp(pi i/N),
F_j=product_(r=1)^j(1-Q^r), and the literature normalization proved in
[the crossing audit](kashaev_crossing_and_period_lattice.md).
Write B_+=P(R^o)^t and B_-=B_+^{-1}. For an entry with input (a,b)
and output (c,d), put

    u=[b-a-1], v=[a-c], t=[c-d], h=[d-b],             (1)

where brackets take values 0,...,N-1. Then exactly

    B_+[(c,d),(a,b)]
       =N Q^[1-(t+h)(u+h)]/(F_u conjugate(F_v) F_t conjugate(F_h))
                                                        (2)

when u+v+t+h=N-1, and it is zero otherwise. This follows by
substituting (i,j,k,l)=(a,b,d,c) into the original unbraided formula.
The two printed theta inequalities are equivalent to this sum condition:
the sum is congruent to -1 modulo N, and those inequalities bound it
strictly below 2N.

For the ACTUAL inverse, including the Q^{-1} correction to the printed
inverse, its factorial indices are (h,u,v,t). Its numerator is
N Q^[(u+v)(v+t)-1]. In particular the support is identical. Using the
sum in (1) gives the stronger entrywise identity

    B_-[(c,d),(a,b)]
       =Q^(c+d-a-b) conjugate(B_+[(c,d),(a,b)]).       (3)

Indeed the exponent left after division by conjugate(B_+) is
(u+v)(v+t)-(t+h)(u+h), congruent to h-v modulo N, and
h-v is congruent to c+d-a-b. Thus if Z e_j=Q^j e_j,

    B_-=(Z tensor Z) conjugate(B_+) (Z tensor Z)^{-1}. (4)

Conjugation in (3)-(4) is entrywise complex conjugation, not adjoint.
It does not make the original braid transfer positive or unitary.

The exact charged absolute weight is therefore, for either sign,

    |B_+[(c,d),(a,b)]|=|B_-[(c,d),(a,b)]|
                    =N/|F_u F_v F_t F_h|.             (5)

## 2. The uniform real action and its convex geometry

Let Lambda(0)=0 and Lambda'(theta)=-log(2 sin theta) on (0,pi).
The elementary uniform root-factorial estimate, including the two
endpoints, is

    log|F_j|=-(N/pi)Lambda(pi j/N)+O(log(N+1)),
                         0<=j<N.                     (6)

For clarity its uniformity does not require staying in the bulk.
Split log(2 sin pi x) into log x+log(1-x) plus a smooth function on
[0,1]. Stirling bounds for the two resulting factorial products and a
bounded Riemann-sum error for the smooth part prove (6), uniformly in j.

With alpha=(u,v,t,h)/N, (5)-(6) give

    (1/N)log|B_+|=H(alpha)+O(log(N+1)/N),
    H(alpha)=(1/pi)sum_(r=1)^4 Lambda(pi alpha_r),
    sum alpha_r=1-1/N.                               (7)

For a fixed whole word, the error remains O_word(log N), and its number
of state variables is fixed. Thus the absolute action of an actual state
is the sum of these local H, with the original support and cut constraints.
No scalar replacement state is needed to define this action.

Here is the strict-concavity statement, including the obtuse case.
For k>=3, theta_r>0 and sum theta_r=pi, the quadratic form

    sum_r cot(theta_r) w_r^2, sum_r w_r=0,             (8)

is positive definite. If every angle is at most pi/2, this is immediate;
at most one coefficient can be zero in this open simplex. Otherwise
exactly one angle, say theta_1, exceeds pi/2. Put
s_0=sum_(r>1)theta_r=pi-theta_1<pi/2. Cauchy--Schwarz gives

    sum_(r>1)cot(theta_r) w_r^2
       >= (sum_(r>1)w_r)^2 / sum_(r>1)tan(theta_r).

The addition formula for tan gives
sum_(r>1)tan(theta_r)<tan(s_0), since there are at least two positive
summands and their sum is below pi/2. This strictly dominates the negative
term -cot(s_0) w_1^2 whenever w_1 is nonzero. If w_1=0, the remaining
positive diagonal form is positive on every nonzero vector. This proves
(8). The same proof works when the angle sum is strictly below pi:
then cot(sum_(r>1)theta_r)>cot(pi-theta_1), strengthening the inequality.

Since the Hessian of sum Lambda is minus this cotangent form, H is
strictly concave on the open charged simplex. It extends continuously
as a concave function to its closure. On a face at limiting charge
sum alpha=1, the same assertion holds for its k>=3 active coordinates.
A two-coordinate face instead has zero action, because
Lambda(theta)+Lambda(pi-theta)=0. One-coordinate faces also have zero
action. Thus strictness on a forced source face must be checked, not
inferred from strictness in the unattained open four-coordinate simplex.

The value at the balanced point is
2 pi H(1/4,1/4,1/4,1/4)=8 Lambda(pi/4), the regular ideal octahedron
volume. This calibrates the local absolute envelope. It is not a claim
that its sum over a diagram equals the knot-complement volume.

## 3. Whole-word winding regions and their source faces

Fix the original arc colors divided by N and choose integer lifts of
the brackets in (1). The crossing indices are then affine functions of
these colors; their sum is exactly 1-1/N. Nonnegativity defines a convex
polytope for each choice of lifts. There are finitely many choices for
a fixed word, independently of N. The pivotal closures must be imposed
with their original shifts, not as unshifted equality of colors.

On a region with all four coordinates positive at every crossing,
the Hessian of the whole absolute action has kernel exactly the
variations which leave every crossing index fixed. At a crossing, this
requires all four incident arc variations to be equal. On a connected
projection these equalities propagate to a common translation of all
arc colors. Fixing the original cut color removes that translation.
Therefore the whole action is strictly concave on any such nonempty
region. It has at most one interior critical point; if one exists, it
is the unique maximum on that region's closure.

This assertion is deliberately not an existence claim. For the original
one-cut source, some four-coordinate interiors are inaccessible. On a
forced face, discard the zero-action one- and two-coordinate crossing
faces. The exact strictness criterion is injectivity, on the remaining
tangent space, of the combined corner maps at crossings with at least
three active coordinates. This is a finite linear-algebra calculation.
When it fails there are real flat directions, which need elimination
before applying an ordinary nondegenerate Laplace argument.

This gives a finite, source-dependent concavity problem. It does not
put a nonzero quantum coefficient on its maximizer, or equate an
absolute-state maximum with the geometric regulator.

## 4. The quadratic phase is part of the same original state

The exact factorial phase is

    F_j=|F_j| exp[pi i j(j+1)/(2N)-pi i j/2].          (9)

Write alpha_u,...,alpha_h for (1)/N, and define

    D(alpha)=alpha_u^2+alpha_t^2-alpha_v^2-alpha_h^2,
    L(alpha)=alpha_u+alpha_t-alpha_v-alpha_h,
    B(alpha)=-2pi(alpha_t+alpha_h)(alpha_u+alpha_h)
                          -(pi/2)D(alpha)+(pi/2)L(alpha).

Equations (2) and (9), without an asymptotic approximation, give

    B_+=|B_+| exp[i N B(alpha)-i(pi/2)L(alpha)+2pi i/N]. (10)

The negative crossing uses the complex conjugate of (10), multiplied
by the exact phase Q^(c+d-a-b) from (3). Thus on every fixed winding
region the leading phase of the WHOLE original state is a real quadratic
function of its arc colors, with crossing signs retained. The remaining
linear phases, pivotal scalars, and writhe factor remain explicit.

One may consequently define a phase homotopy by multiplying every
chosen exact phase angle of the whole summand by tau in [0,1]. At tau=0
this is the absolute sum of that original presentation; at tau=1 it is
the original invariant. Intermediate values are not claimed to be knot
invariants. Concavity supplies a possible initial real maximum on each
accessible face, but does not prove continuation of its integration
cycle or nonvanishing at tau=1.

There is a sharp reason that phase cannot be ignored. For a fixed braid
POSITION word, (3) implies that changing any crossing signs changes
neither its supported state set nor any absolute-state summand. The
enhancement mu=-s S is a unit-modulus cyclic shift, and the writhe
normalization also has modulus one, so the statement holds through the
original full closure. Yet crossing changes can change the knot or
unknot it. For example the position word (1,2,1,2) has the trefoil
closure with all signs positive and the figure-eight closure with
alternating signs. Their actual values differ, while their entire
absolute-state sum is identical. This is an exact finite-state
obstruction, not just a comparison of formal critical potentials.

The new concavity therefore cannot by itself settle source selection.
A reduced-alternating argument might additionally use its specified
phase and projection, but those are additional information. The desired
global theorem must carry (10) and the forced source faces all the way
to the geometric contour.

## 5. Independent finite checks

[The audit](../experiments/audit_original_crossing_winding_convexity.py)
checks (1)-(5) against the independently implemented original crossing
and its true inverse over finite fields, including even and composite
levels. Complex checks verify (9)-(10), the full original pivotal
contraction, the figure-eight normalization, and the equal absolute
sums of the two signed words above. The cotangent tests supplement,
and do not replace, the proof (8).
