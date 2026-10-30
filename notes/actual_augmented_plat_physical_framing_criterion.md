# A finite criterion for a physical magnetic framing

30 October 2026. This note reduces the simultaneous framing question for
the actual complete augmented-plat character to a strict semialgebraic
feasibility problem in one rank-one projector. It also treats the smaller
central domain used by the joint accretive determinant. The criterion
keeps every original prefix word and both actual degree adapters.

There is no assertion that this feasibility problem always has a solution.
The positive gluing certificate and the regular critical-scheme theorem
do not by themselves prove that assertion. In particular, a nonempty
real-open set of perfectly regular frames fails physical support at any
one essential crossing disk. The obstruction below explains why merely
avoiding algebraic divisors cannot settle the issue.

## 1. The common frame is a rank-one projector

Fix the actual marked geometric representation and its finite original
Morse word. For its prefix matrices Q use the same trace -2 main lifts
as in the [regular magnetic chart](actual_augmented_plat_regular_geometric_phase_chart.md).
A simultaneous projective frame g, modulo LEFT diagonal changes, is
equivalently

    Pi=g^(-1) E_11 g,  Pi^2=Pi, tr Pi=1, det Pi=0.       (1)

Indeed the two eigenspaces of Pi have distinct eigenvalues 1 and 0, so
every such projector is obtained this way; its stabilizer is precisely
the projective diagonal torus. This is the same two-dimensional complex
framing quotient as in the [actual critical scheme](actual_augmented_plat_critical_scheme.md).
Every needed prefix diagonal is the LINEAR function

    a_Q=tr(Q Pi)=(g Q g^(-1))_11.                        (2)

At an input of a crossing-circle coupon put

    Q_0=W, Q_1=A W, Q_2=P W, P=B A,
    a_i=tr(Q_i Pi).

For the output, replace A by the actual outgoing first meridian A';
Q_0 and Q_2 are unchanged. The original two physical wire phases are

    X_1=-a_0/a_1, X_2=-a_1/a_2, T=X_1 X_2=a_0/a_2.     (3)

We always impose the other finitely many regular-chart nonvanishings
from the cited chart theorem. No independent local change of frame is
permitted in (2).

## 2. Exact strict-support criterion

For a nonzero X off the positive real axis choose its wire logarithm by

    x=Log_(0,2pi)(X)/(2pi i),  0<Re x<1.                (4)

Write s=x_1+x_2. The actual low adapter is tau=s, u=x_1;
the high adapter is tau=2-s, u=1-x_2. At the complete channel the
strict local physical domain is

    1/2<Re tau<1,  0<Re u<Re tau.                       (5)

For three nonzero prefix diagonals, (4)--(5) hold if and only if

    Im(a_0 conjugate(a_2)) != 0,
    0 is not in the real convex hull of {a_0,a_1,a_2}.   (6)

Here the low or high adapter is determined, rather than freely chosen.
The second condition is equivalent to the existence of one open
half-plane through the origin containing all three numbers.

Proof. Rotate a_0 to the positive axis. Under the convex-hull condition
the three arguments have lifts

    arg a_0=0, arg a_2=delta in (-pi,pi), arg a_1=beta,
    max(0,beta,delta)-min(0,beta,delta)<pi.

The first condition in (6) says delta is neither 0 nor an endpoint.
The canonical physical arguments are consequently

    2pi Re x_1=pi-beta,
    2pi Re x_2=pi+beta-delta.                            (7)

Their sum is 2pi-delta. Thus delta>0 gives the low adapter,
delta<0 gives the high adapter, and

    Re tau=1-|delta|/(2pi) in (1/2,1).

Both inequalities for u follow from 0<Re x_i<1: in the low case
tau-u=x_2, and in the high case tau-u=1-x_1. Conversely (5) puts
the sum of the two wire arguments strictly between pi and 3pi and
away from 2pi. The inverse formulas (7) put the three prefix arguments
in an interval of width less than pi. This proves (6).

The input and output have the same a_0,a_2. Their prescribed adapter
therefore agrees. Their canonical sums agree in real part by (7) and
in imaginary part by X_1 X_2=T. Thus degree conservation holds as an
EXACT complex equality, not only after exponentiation.

At a cup or cap the first and last prefix words agree. The corresponding
condition is simply that a_1/a_0 is not a nonpositive real number; all
diagonals are nonzero. Then X_2=X_1^(-1) and their canonical logarithms
sum exactly to 1. Applying these tests at every event makes the chosen
wire logarithms solve the original affine incidence equations Bx=b
without any additional integer adjustment. Ordinary and marked cap
characters are still the distinct characters recorded in the source.

## 3. The central joint domain has an even simpler test

The central domain adds

    |2 Re u-Re tau|<1/2                                (8)

to (5). This is the leading open domain Re c>0, Re z>0 for

    c=-cos(pi tau), z=exp[pi i(tau-2u)].

The exact finite c has tau+1/N in place of tau; any compact subset
of (5),(8) satisfies its corresponding inequality for large N.
For BOTH actual adapters,

    tau-2u=x_2-x_1.                                    (9)

Consequently the central condition is adapter-independent. In physical
wire real parts it is the diamond

    |Re x_1-1/2|+|Re x_2-1/2|<1/2,
    Re(x_1+x_2) != 1.                                  (10)

An exact test using only the prefix diagonals is

    Im(a_0 conjugate(a_2)) != 0,
    |a_2| Re(a_1 conjugate(a_0))
      +|a_0| Re(a_1 conjugate(a_2)) > 0.                 (11)

Proof. In the argument lifts above, (8) is |2 beta-delta|<pi.
This says precisely that a_1 lies in the open half-plane centered at
the bisector of the MINOR angular interval from a_0 to a_2. The vector
a_0/|a_0|+a_2/|a_2| points along that bisector. Taking the scalar
product with a_1 gives (11). Conversely the resulting interval
delta/2-pi/2<beta<delta/2+pi/2, with |delta|<pi, puts all three
arguments in an interval of width less than pi. Thus (11) itself
implies (6), as well as (8).

This extra inequality is substantial: same-side disk flags, or merely
being in the larger physical strip (5), does not imply (11).

## 4. A finite semialgebraic feasibility problem

Equations (1),(2),(6) give a finite strict semialgebraic test for a
simultaneous physical magnetic frame. One can encode the convex-hull
test with one complex separator n_f per input/output triple:

    |n_f|^2=1, Re(n_f a_(f,i))>0 for i=0,1,2.

For the central domain there are no separator choices. Introduce
positive real r_(f,0),r_(f,2) with r_(f,i)^2=|a_(f,i)|^2 and require

    r_(f,2) Re(a_(f,1) conjugate(a_(f,0)))
      +r_(f,0) Re(a_(f,1) conjugate(a_(f,2))) > 0.        (12)

Also require the square of Im(a_(f,0) conjugate(a_(f,2))) to be
positive, impose the cup/cap tests, and retain every regular-chart
nonvanishing. All coefficients are algebraic when the actual marked
representation is algebraic. Only one projector Pi is shared by the
whole diagram. This formulation is suitable for an exact feasibility
or infeasibility certificate; it is not a collection of independent
local frame choices.

A strict feasible frame persists under sufficiently small changes of
the marked representation. The strict inequalities give a common
positive margin on the finite set of triples, and all denominators
remain nonzero. In particular it would persist for sufficiently long
fillings once obtained at completeness.

This persistence does not obtain the initial frame. Nor does (12)
make the pair totals real: their imaginary parts come from the moduli
of the prefix ratios. A theorem continuing only u at fixed real t,j
cannot be applied to these generally complex totals. Even a joint
domain requires comparing its selected internal roots with the actual
geometric roots, and subsequently controlling the contributing global
finite-source cycle.

### A finite family sharing one disk product is always feasible

There is a constructive positive result: all input/output triples from
any fixed finite family of transports sharing the SAME product P and
prefix W can be made central simultaneously. This does not couple
different disk products or different prefixes.

Normalize A,P as in (13), put H=P+I, and write its transported splits
as A_b=(I+bH)A(I-bH), with b in the given finite complex set. This
includes every complete centralizer transport and any retained finite
half-twist shifts. For a>0 put h=sqrt(2a+1) and take the projector

    L_a=[[1+a/2+i h/2, (a-1)/4+i h/2],
         [-a-1,       -a/2-i h/2]].                    (12a)

Direct multiplication gives

    L_a^2=L_a, tr L_a=1,
    tr(P L_a)=1, tr(A L_a)=a,
    tr([H,A] L_a)=-4i h,
    tr(A_b L_a)=a-4i b sqrt(2a+1)-8b^2.                (12b)

For the finite b-set the last expression is a+O(sqrt(a)), uniformly
as a tends to positive infinity. It therefore has positive real part
for every b once a is large enough. The central scalar inequality
in (11), with endpoints 1,1, is then strictly positive for every
triple. Only its T=1 seam remains. These finitely many scalar
inequalities hold on an open neighborhood of L_a in the complex
projector surface. The nonconstant function tr(P L) cannot be real
on any such open neighborhood. A sufficiently small perturbation
therefore removes the seam, and gives all the strict central tests.

For an arbitrary shared prefix W, recover the actual common projector
by

    Pi=W^(-1)L/tr(W^(-1)L).                             (12c)

It is rank-one of trace one, and its actual prefix diagonals are one
common nonzero scalar times tr(L),tr(A_b L),tr(P L). Thus the central
inequalities are unchanged. The additional trace in (12c) does not
vanish identically on the projector surface: otherwise
ell(W^(-1)v)=0 for every ell(v)=1, forcing W^(-1)=0. Hence its zero
set cannot contain the feasible open neighborhood. The perturbation
can simultaneously avoid this trace, the seam, and the finitely many
proper regular-chart divisors. This proves the assertion for W as
well, rather than assuming the W=I projector survives unchanged.

The construction is a precise favorable near-coincident-frame
mechanism at ONE auxiliary flag. It proves that each coupon's
incoming and outgoing central inequalities are locally compatible.
It leaves the genuinely simultaneous problem (12), with the actual
different products and prefixes of the full plat, unresolved.

## 5. A geometric necessary condition and an open obstruction

There is a useful uniform restriction on possible solutions. At one
essential complete disk normalize its distinct puncture flags so that

    A=-[[1,1],[0,1]], B=-[[1,0],[-4,1]],
    P=B A=[[1,1],[-4,-3]].                              (13)

This normalization follows directly from Tr A=Tr B=Tr P=-2.
The circle through the three parabolic flags is then the real circle.
Write Pi=v ell with ell(v)=1, put w=ker ell, and put z=Wv. These are
projective points; z is the right framing point transported by the
ACTUAL prefix W. If (6) holds, then

    z and w lie in the same open side of this circle.   (14)

In particular replacing z by v in this test would be incorrect.

Here is a direct proof. For real r=(r_0,r_1,r_2) set

    M(r)=r_0 I+r_1 A+r_2 P.

The matrices in this pencil are real-linearly independent and

    det M=2(r_0^2+r_1^2+r_2^2)-(r_0+r_1+r_2)^2.         (15)

Suppose z,w are in opposite open half-planes. The condition M(r)z=w
is two homogeneous real linear equations in three r's, so it has a
nonzero solution. M(r) cannot annihilate a nonreal z: its real and
imaginary vector parts are linearly independent, which would force
M=0. The real Möbius transformation identity

    Im M(z)=det(M) Im(z)/|M_21 z+M_22|^2

therefore gives det M<0. Normalize the sign so that sum r_i>0.
Equation (15) forces every r_i>0: if, for example, r_0<=0, then

    det M=(r_1-r_2)^2+r_0^2-2r_0(r_1+r_2)>=0,

because r_1+r_2>0. This is a contradiction. Now

    0=ell(M(r)Wv)=r_0 a_0+r_1 a_1+r_2 a_2.

This is a strictly positive convex relation after division by sum r_i,
contradicting (6).

If z is nonreal and w is on the real circle, the same argument gives
det M=0 and r_i>=0, still a nontrivial convex relation. If z is on
the real circle, solve instead M(r)z=0, again two real equations in
three unknowns. The same det=0 argument gives r_i>=0 and the same
relation for every w. The point at infinity is handled in homogeneous
coordinates, or by a real change of disk coordinates. Thus a good
triple must satisfy (14). This is a necessary condition, not a
converse.

The opposite-side choice is a nonempty REAL-OPEN condition on the
common framing quotient. It also allows v and w to be distinct, as
required for a projector. The common regular-frame locus is a complex
Zariski open dense subset by the cited chart theorem. It intersects
this real-open bad set: a nonzero holomorphic polynomial cannot vanish
on a real-open subset of this complex manifold. Hence EVERY such
complete character has common regular frames that fail physical
support already at this disk. This conclusion holds independently of
whether the representation has a positive gluing certificate.

For a small exact illustration use W=I, v=(i,1),
ell=(1,i)/(2i), so w=-i. Equations (13) give

    (a_0,a_1,a_2)=(1,-1+i/2,-1-5i/2),
    (1/2)a_0+(5/12)a_1+(1/12)a_2=0.                    (16)

The endpoint discriminant numerator is
a_0 a_1+a_1 a_2+a_0 a_2=1/4, and the leading-coefficient numerator
a_0+a_2+4a_1=-4-i/2; both are nonzero. Thus this support failure is
not just the local root-discriminant failure. Formula (16) is only
a local illustration; the preceding open-density argument deals with
all the other regular divisors of the actual finite diagram.

Near-coincident framing points do not evade (14). In the limit w=v,
each condition concerns v and Wv on its own developed disk circle.
The different prefixes W are fixed words of the representation, not
small perturbations of the identity. No simultaneous same-side or
central-domain conclusion follows just by taking w close to v.

## 6. What an ordinary fixed-total fiber estimate does and does not say

At fixed real discrete t,j, the proved magnetic corridor can be
multiplied over a fixed finite number of ORDINARY q-Hahn column
factors. Pull their magnetic u variables back by affine wire maps
preserving every such total. On a compact subset of the common
corridors, the relative errors multiply to 1+O(1/N), the leading
actions add, and the nonzero amplitudes multiply. An already evaluated
normal-derived coefficient depending only on these fixed t,j may
remain an EXACT scalar outside this product.

This elementary product statement estimates neither generic q/normal
derivatives of the columns nor the rank-two derivative terms of mixed
source kernels. It supplies no bound for fiber summation and does not
release t,j. It therefore does not establish an asymptotic for an
arbitrary full original-source summand containing those normal terms.

Audit: [exact projector, determinant, convexity and adapter checks](../experiments/audit_actual_augmented_plat_physical_framing_criterion.py).
The audit includes numerical argument comparisons only as regressions
of the explicit equivalences; it is not an existence search or a proof
of a favorable simultaneous frame for arbitrary augmented plats.

Independent analytical review: PASS. A second reader checked both
directions of the support and central-domain tests, the exact affine
degree lift and cap marks, the common-product constructive lemma and
its nonidentity-prefix normalization, the disk-side obstruction including
boundary flags, and the distinction between regular bad frames and
nonexistence of favorable frames. The initial audit was independently
replayed; the expanded audit adds 100 exact central-feasibility checks
for the constructive lemma. No global existence or cycle claim follows.
