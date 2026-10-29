# A positive supported Racah factorial, its metric and retained partner current

29 October 2026. This is an independent finite FACTORIAL theorem. It
does not assume that a proposed four-port source coefficient is a
Racah sum. On the full folded supported chamber it proves a common
phase, a positive root normalization, a uniform positive Laplace
principle, and polynomial relative bounds for every fixed generic-q
normal jet. Complementary high partners have the same positive value
core but an additional explicitly retained normal current.

Connecting these formulas to the actual source requires its separate
typed coefficient identity. A positive root value is not by itself a
bound on a complete Hermite recoupling operator.

## 1. Seven factorials, with a root unit at every denominator

Fix N>=3, D=N-1, M=floor(D/2), q=exp(pi i/N), and six INTEGER
folded spins 0<=a,b,c,d,e,f<=M. Define four faces and three quads

    F=(a+b+e, c+d+e, a+d+f, b+c+f),
    Q=(a+b+c+d, a+c+e+f, b+d+e+f).              (1)

Assume every F_i>=D. Every face is an ordinary triangle: its two
smaller entries sum to at least D minus its largest, which is at
least its largest because D>=2M. Moreover EVERY face deficit
F_i-2ell lies in [0,D]. Every difference Q_k-F_i is one such
deficit of a complementary face. Therefore

    z_-=max F_i <= z_+=min Q_k,
    D<=z_-<=z_+<=4M<=2D,
    0<=z-F_i<=D, 0<=Q_k-z<=D.                   (2)

Use the GENUINE generic symmetric factorial [n]!_zeta, with
[u]_zeta=(zeta^u-zeta^-u)/(zeta-zeta^-1). Set

    S(zeta)=sum_(z=z_-)^(z_+) (-1)^z [z+1]!
                  /[product_i [z-F_i]! product_k[Q_k-z]!]. (3)

No negative factorial is assigned a value: the displayed interval
is the true finite range. By (2), every denominator is a unit at q.
The numerator contains EXACTLY ONE factor [N]. Factoring it BEFORE
specialization defines the analytic function

    G(zeta)=(-1)^D S(zeta)/[N]_zeta.              (4)

Let s_r=product_(u=1)^r 2sin(pi u/N), s_0=1. The exact positive
root value is

    R_N:=G(q)=N sum_z s_(z-D)
                    /[product_i s_(z-F_i) product_k s_(Q_k-z)]>0. (5)

Indeed the signs of [N+1],...,[z+1] multiply to (-1)^(z+1-N).
Together with (-1)^(D+z) this is +1. Also s_D=N. The powers of
2sin(pi/N) cancel, since

    sum_i(z-F_i)+sum_k(Q_k-z)=z,
    sum_i F_i=sum_k Q_k=2(a+b+c+d+e+f).

Thus (5) is a finite exact identity, including boundary faces F_i=D,
collapsed z intervals, both level parities and composite levels.

## 2. The exact positive face metric

For a face (x,y,z) of sum F, define the generic squared triangle
factor and its regular normalization by

    Delta_F^2=[F-2x]![F-2y]![F-2z]!/[F+1]!,
    D_F(zeta)=(-1)^(F-D)[N]_zeta Delta_F^2.

It is analytic and nonzero at q, with positive root value

    d_F=D_F(q)
           =s_(F-2x)s_(F-2y)s_(F-2z)/(N s_(F-D))>0. (6)

The natural positive normalized scalar is

    W_N=R_N sqrt(product_faces d_F).              (7)

This metric is not optional in a geometric interpretation. The
branch-independent generic squared identity is EXACTLY

    [N]^2 S(zeta)^2 product_faces Delta_F^2
                      =G(zeta)^2 product_faces D_F(zeta). (8)

The root of its right side is W_N^2>0. There is no residual sign,
because sum_faces(F-D)=2(a+b+c+d+e+f)-4D is even. Equation(8)
defines a finite factorial normalization; it is not a claim that an
as-yet-unproved physical recoupling matrix is unitary in this metric.

The ordered physical Clebsch norms, source gamma factors and any
intermediate quantum dimensions must still be matched by an actual
coefficient theorem. A quantum dimension can vanish at the odd simple
endpoint. It is not canceled by evaluating (7) alone; its generic
source limit must be retained before interpreting this as a physical Gram.

## 3. A uniform positive action on the ENTIRE folded chamber

Put L(t)=integral_0^t log(2sin(pi u))du on [0,1], continuously at
both endpoints. Write x=(a,b,c,d,e,f)/N, D_N=D/N, and use the
same linear forms F_i(x),Q_k(x). On

    I_N=[max_i F_i(x),min_k Q_k(x)]

define

    A_N(x,Z)=L(Z-D_N)-sum_i L(Z-F_i(x))
                                -sum_k L(Q_k(x)-Z),
    V_N(x,Z)=A_N(x,Z)
       +(1/2)sum_faces[sum_(ell in face)L(F(x)-2x_ell)
                                           -L(F(x)-D_N)].       (9)

Uniformly over ALL allowed integral labels,

    log R_N=N max_(Z in I_N) A_N(x,Z)+O(log N),
    log W_N=N max_(Z in I_N) V_N(x,Z)+O(log N).   (10)

Proof. Every factorial index is in [0,D], so the uniform elementary
sine-factorial estimate log s_r=N L(r/N)+O(log N) applies to every
term, including endpoints. There are at most 2N positive terms.
Their maximum gives the upper bound and one term gives the lower.
The modulus of continuity of L is O(epsilon log(1/epsilon)); rounding
Z to a feasible integral index changes N times the action by at most
O(log N). All constants are independent of the labels. The same
estimate applied to the four explicit factors (6) proves the second
line. Thus no cancellation or selected complex saddle is required.

For any convergent scaled-label sequence, (10) yields the corresponding
max-action limit, with D_N replaced by 1. This is an action theorem;
identification with an actual geometric tetrahedron is a separate task.

Two calibrations expose the metric's role. At all six scaled labels
1/3, the bare action maximum is 3v3/pi, whereas the face metric adds
-2v3/pi and the normalized maximum is v3/pi. At all six labels 1/2,
the metric action is zero and the normalized maximum is v8/pi.
Here v3=3Lambda(pi/3), v8=8Lambda(pi/4). The maxima occur respectively
at Z=7/6 and Z=7/4, by direct differentiation of (9).

The independently proved
[local hyperideal geometry theorem](actual_four_port_hyperideal_angle_volume.md)
now identifies this normalized maximum with actual truncated-tetrahedron
volume. Its exact Casimir angle coordinates are a_ell=(ell+1/2)/N.
Using Z=(z+7/4)/N shifts the numerator factorial argument by 3/(4N),
each denominator argument by 1/(4N), and every face-metric argument by
1/(2N). The same uniform endpoint modulus gives the SHARP scalar bound

    log W_N=(N/pi)Vol_ext(T(a_ell))+O(log N)        (10a)

on the entire supported chamber, with a universal error constant.
Vol_ext denotes the continuous boundary-volume extension when an odd
simple channel has zero dihedral angle. This is a local scalar energy
calibration, not a proof that a source graph supplies the corresponding
cell gluing or a completed Hermite metric.

## 4. Polynomial relative generic normal jets, not just root values

Take zeta=q exp(t), with ALL integer labels fixed, and cancel the
single displayed [N] in each term of (3). This is the actual generic
factorial germ, not a formal root recurrence continued off the root.
There is a universal c>0 such that on

    |t|<=r_N=c/[N^2(1+log N)]                     (11)

the functions G and each D_F are holomorphic and nonzero, and their
ratios to their positive root values differ from one by less than
1/4. The canonical analytic square roots of D_F, positive at t=0,
therefore define H(t)=G(t) product_F sqrt(D_F(t)), with H(0)=W_N.
Shrinking the SAME universal c if necessary gives |H/H(0)-1|<1/4.

Here is a uniform proof. After cancellation, all factors zeta-zeta^-1
cancel too, by the factorial degree equality used in section1. Every
remaining factor is zeta^u-zeta^-u, 1<=u<2N, u!=N. At t=0 its
absolute value is at least 4 dist(u,N Z)/N. For |t|<=N^-2, its
derivative has absolute value at most 30N. Thus each unit factor's
logarithmic change is bounded by
15N^2|t|/dist(u,N Z) when that relative change is small. Across a
summand there are at most eighteen copies of the harmonic sum
sum_(k=1)^N 1/k; the four face factors have the same fixed bound.
Consequently each product ratio has logarithmic change at most
C N^2(1+log N)|t|, with universal C. Choosing, for example, a
sufficiently small c<=10^-6 makes every summand stay in a small
common sector around its POSITIVE value in (5). A positive weighted
sum stays in that sector as well. This proves (11), including the
nonzero lower bound and analytic square roots.

Cauchy's inequality now gives, for every fixed k>=0 and F=G or H,

    |F^(k)(0)|/k! <=2 r_N^-k F(0),
    |(1/F)^(k)(0)|/k! <=2 r_N^-k/F(0).           (12)

Thus finite normal jets and inverse scalar jets have polynomial
relative cost UNIFORMLY throughout this folded supported chamber.
This scalar assertion does not estimate a change of physical frame.
Together with (10a), it bounds squared fixed normal jets by a polynomial
times exp[(2N/pi)Vol_ext(T(a_ell))], with all joint labels still shared.

## 5. Complementary partners: positive value core and a real missing current

Now replace ANY subset of the six folded labels ell by D-ell.
At each face, its new deficits are old deficits, their complements
D-old_deficit, the old excess F-D, or its complement D-(F-D).
They all lie in [0,D]. Its new sum lies in [D,2D]. Therefore (2)'s
denominator-unit assertion survives at EVERY one of the up to 64
partner assignments, and the new z range is nonempty with z_-<=2D.

Also the sum of its six labels is at most 4D, because every new face
has sum at most 2D. Hence z_+<=8D/3<3N-1. The generic sum still
contains [N] in every term, but some terms now contain [2N] too.
The EXACT decomposition is

    (-1)^D S(zeta)/[N]_zeta=C(zeta)+[2N]_zeta T(zeta), (13)

where C sums the TRUE terms z<=2D after deleting the numerator [N],
and T sums the terms z>=2N-1 after deleting BOTH [N] and [2N].
All their denominators are units. At q the nonempty core is exactly
the positive expression (5), with z truncated at 2D. The positive
metric (6) and squared identity (8) apply at every partner value too.
The core C has the same polynomial scalar-jet bound as section4.

The term [2N]T is NOT zero as a generic normal. In particular

    ((-1)^D S/[N])'(0)=C'(0)+(4N/(q-q^-1))T(0).   (14)

Writing z=2N-1+k, its retained root value is explicitly

    T(0)=-2sin(pi/N)N^2 sum_k (-1)^k s_k
              /[product_i s_(2N-1+k-F_i)
                         product_j s_(Q_j-2N+1-k)]. (15)

Every index in (15) is physical. The alternating sum must remain
coherent. Its absolute-value envelope is not a substitute for it.
For example N=4, partner labels (2,2,2,2,2,1) arise by five flips
from the supported folded labels (1,1,1,1,1,1). Their faces are
(6,6,5,5), quads (8,7,7). Core z=6 gives C(0)=sqrt(2), while
the single tail term z=7 gives T(0)=-1. The EXTRA first normal in
(14) is exactly 8sqrt(2)i. Deleting the tail loses actual data.

Accordingly (12) is a theorem for the complete LOW-fold scalar germ
and for partner value cores. It is NOT asserted for the full partner
germ without a further coherent estimate for T. Nor are the partner
columns deleted from a physical Hermite cluster. This is the remaining
normal interface for using the positive factorial in a full recoupling
energy argument.

A separate, UNPROVED research lead is preserved by the
[64-partner value diagnostic](../experiments/diagnose_supported_racah_partner_value_reflection.py)
and its [recorded root images](../experiments/supported_racah_partner_value_reflection_diagnostic_results.json).
For three specified folded tuples per level when distinct, every one
of the 64 complement bit patterns was checked at N=3,...,10: 1408
comparisons showed no failure of W_squared invariance. These are exact
finite cyclotomic-root images, not a uniform complex identity proof.
No symmetry of generic germs, bound on the [2N] current, completed
physical Gram or volume theorem is inferred from that observation.

## 6. An exact valuation interface to the separately proved physical kernel

The preceding factorial theorem has not used a source identity. One
can now APPLY the independently proved
[actual inverse four-port theorem](actual_general_four_port_single_racah_kernel.md),
equations (23),(24). Put its external highest weights
(A,B,C,D_ext)=(2a,2b,2c,2d), E=2e and G=2f. It states

    L_(G,E)=chi_E X_E/(b_G J_n S0 V_n) *S,
    p=min(a+d,b+c), q=max(a+d,b+c), s=p+q,
    n=p-f, t0=q-p,
    V_n=zeta^n (Q^(-p-f-1);Q)_n
                  /[F_n(Q^(t0+1);Q)_n(Q^(-s-1);Q)_n]. (16)

Throughout the fully supported folded chamber, chi_E X_E, b_G and
J_n are root units, while S0 has exactly one [N] zero. This follows
directly from the source product formulas: all their physical
factorial indices are <=D, whereas the numerator of S0 is [s+1]!
with D<=s<=2D. For X_E at its endpoint, its numerator index is <=A
when that endpoint is H, and <=B when it is A. Hence no endpoint
root zero has been hidden in that assertion.

Both f faces imply p+f>=D and q+f>=D. The sole possible numerator
zero of V_n is at index k=p+f-D. It is INSIDE 0,...,n-1 exactly
when 2f<D. Its denominator has no root zero: t0+n=q-f<=D, and
the first potential zero in (Q^(-s-1);Q)_n has index s-D>=n.
Consequently the actual inverse coefficient has exact order

    ord_q L_(G,E)=-1 if 2f<D,
    ord_q L_(G,E)= 0 if 2f=D.                    (17)

Its leading coefficient is nonzero by the positive finite sum (5).
Thus a positive root factorial does NOT turn the uncompleted physical
coefficient matrix into a finite positive operator: paired output
channels have genuine simple poles and must be combined with their
partners in a regular Hermite frame.

The same bookkeeping in the actual ordered invariant norm

    N_E=n_(ab)^e n_(cd)^e [2e+1]

gives order two for paired e and order one for odd simple e. These
are source-frame orders, not optional quantum-dimension factors.
Equations (16),(17) supply an explicit local interface for matching
the positive metric (6) to a completed physical recoupling energy;
they do not complete that matching or bound the partner current (15).

Audit: [true root factorials, partner ranges and retained Taylor coefficients](../experiments/audit_actual_supported_racah_common_phase_and_normal_metric.py).
The common phase, metric, uniform action and jet arguments above are
independent of the proposed actual four-port source identity.

Independent internal review: the global audit agent completed a full
analytical read of sections1–6 and a fresh primary replay. The harmonic
unit-factor estimate and inverse jets, exact high-partner current,
N=4 nonzero normal, source pole orders and norm orders all passed.
The replay checked eight exhaustive folded levels, 1202 supported
tuples, 686 partner metrics, the retained-current fixture and six
metric-action calibrations. That verdict does not include a full
partner-jet bound or a positive completed physical recoupling Gram.
