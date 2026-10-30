# A positive tail-free Racah scalar at one actual matching edge

30 October 2026. This is a specialization of the actual generic four-port
coefficient theorem to the two halves of ONE crossing-circle matching
edge. Its four outside objects are all the original physical V_(N-1).
The scalar is positive after the retained single root zero is removed,
including every new high recoupling channel and both level parities.
All fixed generic scalar jets have polynomial relative cost. Each full
recoupled tensor term has at most one pole, so its first normal needs
Taylor order two after clearing that pole.

This theorem controls the explicitly stated scalar and Laurent budget.
It does not estimate the native boundary change-of-frame costs, the
completed Hermite operator, or the surrounding coherent contraction.

## 1. The full actual channel range is uniformly saturated

Put d=N-1, q=exp(pi i/N), and fix

    0<=a<=floor(d/2),
    (A,B,C,D)=(d,d,d,d), E=2a,
    G=2g, 0<=g<=d.                                      (1)

The G range in (1) is the ENTIRE generic four-port recoupling range.
No high partner is discarded. These are the four-port highest-weight
conventions of [the actual coefficient theorem](actual_general_four_port_single_racah_kernel.md).
The corresponding six spins are (d/2,d/2,d/2,d/2,a,g). Its faces and
opposite sums are

    F=(d+a,d+a,d+g,d+g),
    Q=(2d,d+a+g,d+a+g).                                 (2)

Every face is at least d, and all its triangle deficits are among
k,k,d-k for k=a or g. They lie in [0,d]. All four faces and three
opposite sums are INTEGERS, also when N is even and the four physical
spins d/2 are half-integral. Consequently the true Racah range is

    d+max(a,g)<=z<=min(2d,d+a+g),                        (3)

and all seven denominator factorial indices are in [0,d]. Every
numerator [z+1]! contains exactly one [N] and contains NO [2N].
Thus this special physical block is tail-free even when g>d/2.
This is not a claim that arbitrary high recoupling partners are tail-free.

For the genuine generic symmetric factorial at zeta define

    S_ag(zeta)=sum_(z in (3)) (-1)^z [z+1]! /
          ([z-d-a]!^2 [z-d-g]!^2 [2d-z]!
                              [d+a+g-z]!^2),
    G_ag(zeta)=(-1)^d S_ag(zeta)/[N]_zeta.               (4)

The division in (4) is performed in every original summand before
root specialization. It is an analytic germ at q, not a derivative
of a root-only replacement.

## 2. An exact positive squared-trinomial formula

Set s_k=product_(v=1)^k 2sin(pi v/N), s_0=1. The elementary identity
s_(d-k)=N/s_k gives the explicit root scalar

    R_N(a,g)=G_ag(q)
      =sum_(r=max(0,a-g))^(min(a,d-g))
            [s_(g+r)/(s_(g+r-a)s_r s_(a-r))]^2 >0.     (5)

To verify every factor, put k=z-d. The removed-numerator formula is

    N sum_k s_k /
       [s_(k-a)^2 s_(k-g)^2 s_(d-k) s_(a+g-k)^2].

Replace s_(d-k) by N/s_k and then set r=k-g. All indices in (5)
are between 0 and d. The signs of the factors [N+1],...,[z+1]
combine with (-1)^(d+z) to give +1. No half-spin phase was omitted:
A+B+C+D+E+G=4d+2a+2g is even.

The full high partner has the SAME root scalar:

    R_N(a,g)=R_N(a,d-g).                                (6)

This is termwise: replace g by d-g and r by a-r, and use
s_(d-k)=N/s_k in the numerator/first-denominator ratio. The actual
ranges in (5) are carried onto one another. Equation (6) is proved
at both parities and does not discard any generic normal.

The face metric is especially simple. For a face (d/2,d/2,k), put

    Delta_k^2=[k]!^2[d-k]!/[d+k+1]!,
    D_k(zeta)=(-1)^k [N]_zeta Delta_k^2.                 (7)

All D_k are analytic and nonzero at q, and

    D_k(q)=s_k s_(d-k)/N=1.                             (8)

There are two faces of each kind k=a,g. The generic normalized scalar
therefore has the single-valued form

    H_ag(zeta)=G_ag(zeta)D_a(zeta)D_g(zeta),
    H_ag(q)=R_N(a,g).                                   (9)

Its branch-independent identity is the exact actual scalar convention

    H_ag^2=[N]^2 S_ag^2 product_(four faces) Delta^2.    (10)

All powers and signs in (10) are the original ones. A scalar diagonal
gauge relating (10) to the physical recoupling matrix is still required;
root value 1 of the face factors alone does not make that matrix unitary.

## 3. Every fixed generic scalar jet has polynomial relative cost

There are universal c,C>0 such that, for ALL labels in (1), on

    zeta=q exp(t), |t|<=c/[N^2(1+log N)],               (11)

G_ag/G_ag(q), D_a, D_g and H_ag/H_ag(q) are holomorphic and remain
in a fixed small disk about 1. In particular they are nonzero.
For every fixed m>=0 this implies

    |partial_t^m G_ag(0)|+|partial_t^m H_ag(0)|
       <=C_m [N^2(1+log N)]^m R_N(a,g).                (12)

The same relative estimate holds for their inverses.

For clarity, the proof applies to the COMPLETE generic germ in (4).
After the one [N] factor is canceled, each summand and each face metric
is a quotient of factors zeta^u-zeta^(-u), 1<=u<2N, u!=N, with fixed
factorial multiplicities. Its logarithmic change on (11) is bounded
by C N^2(1+log N)|t|, using |sin(pi u/N)| bounded below by a constant
times dist(u,NZ)/N and the finite harmonic sum. At the root every
summand of G_ag is positive by (5). On a sufficiently small common
disk these summands remain in one narrow sector, so their sum has the
same uniform relative bound. Equations (7),(8) give it for D_a,D_g.
Cauchy's estimate proves (12). This is the direct supported-scalar
argument, with (2),(3) proving its hypotheses for the entire present
range, including half-integral physical spins and high g.

In particular no missing [2N]T normal survives here: such a numerator
factor is absent from every term before differentiation. The result
does not say that a normal equals the derivative of the positive
root expression (5); (4) remains the differentiated source.

## 4. The actual physical coefficient has only a simple pole

Let L_(2g,2a) be the actual inverse Racah coefficient, with its original
pivotal turn and first-highest-entry-one Clebsch bases. The exact source
formula is

    L_(2g,2a)=chi_E X_E/(b_G J_n S0 V_n) S_ag,
    n=d-g,
    S0=[2d+1]!/([d-a]!^2[a]!^2),
    V_n=zeta^n (Q^(-d-g-1);Q)_n /
                [(Q;Q)_n^2 (Q^(-2d-1);Q)_n],
    Q=zeta^2.                                          (13)

The four prefactors chi_E,X_E,b_G,J_n are root units. This follows
from their actual boundary product formulas: E=2a<N; their physical
endpoint factorial indices are all in [0,d]. No first-normal channel
norm is divided out.

S0 has exactly one root zero. The numerator of V_n has a single root
zero exactly when

    2g<d.                                              (14)

Indeed its negative exponents run from -(d+g+1) to -(2g+2), and the
only possible root multiple is -N. Its denominator factors are all
units: the negative product starts at -(2N-1) and has length d-g,
ending strictly before -N. The two (Q;Q)_n factors have n<N.
By the strict positivity in (5), S_ag has exactly one root zero.
Thus the ACTUAL coefficient orders are

    ord_q L_(2g,2a)=-1 for 2g<d,
    ord_q L_(2g,2a)= 0 for 2g>=d.                      (15)

This includes a=0 and all endpoints. It does not assert positivity
or regularity of the uncompleted physical coefficient matrix.

Let T_(2g) be the actual generic target invariant tensor. Its Clebsch
entries have the regular canceled physical coproduct formulas; the
only possible pole is the canonical intermediate cup, with denominator
(Q;Q)_(2g). Hence T_(2g) is regular for 2g<N and has at most a simple
pole for 2g>=N. These two ranges never overlap the pole range in (15).
Consequently

    pole_order [L_(2g,2a) T_(2g)] <=1                 (16)

for EVERY channel and level parity. The fixed source tensor S_(2a) is
regular, so the simple poles on the right of its exact recoupling
identity cancel in their full sum.

After multiplication by a local parameter t, each recoupled term is
holomorphic. Its contribution to the first normal of the regular
whole contraction is extracted from Taylor coefficient t^2. Thus
this special block has a uniform first-normal budget TWO, improving
the general all-port budget four. If a regular surrounding contraction
is present, it must be included when extracting that coefficient;
its derivatives are not discarded.

## 5. Relation to the geometric pair localization

The [prescribed-facet corollary](actual_right_angled_selected_framing_obstruction.md)
allows the two physical-support exceptions to be placed at the two
halves of any chosen crossing-circle matching edge. Their four outside
objects are then all V_d, so the present specialization applies regardless
of the ribbon order of the other matching edges. A physical MAIN edge
does not have that automatic property: its two channel legs can be
adjacent instead of opposite in the actual cyclic order.

The exact typed bend from the original W_a pi_a block to S_(2a), its
fixed gamma factor, and the unchanged physical mark belong to the
separate source interface. The normal must be extracted from the
complete generic contraction, with all channels in (1) retained.

Even after that interface, this is not a sharp completed block norm
or a bound on the full source. Its scalar gauge factors can carry
nontrivial boundary cost; the other local columns are not automatically
in the central domain; and a global selected cycle and coherent bound
remain necessary. The theorem makes the exceptional matching block
an explicit tail-free scalar/finite-jet problem, without declaring
those remaining tasks solved.

Audit: [exact matching-edge scalar, original recoupling and normal budget](../experiments/audit_actual_matching_edge_racah_positive_scalar.py).
It passes 21,772 support/phase/pole cases, ten independently reconstructed
generic source tensor families with all 47 recoupling coefficients,
529 retained root germs, 1,257 termwise partner checks, and 1,058 exact
face-unit jets. In 406 comparisons the partners have the same root value
but DIFFERENT generic first derivatives. The audit retains that distinction;
its finite cases test conventions, while the written harmonic-product
argument proves the uniform jet bound.

Independent source-transport review and fresh audit replay: PASS. The
reviewer independently specialized the actual boundary prefactors,
including the pure-phase highest endpoint, and checked every root-unit
and zero interval. The positive squared formula, half-integral physical
spin phase, face roots, full generic sector argument, disjoint coefficient
and target-cup poles, and Taylor-order-two budget all passed. The fresh
replay reproduced all reported exact counts, including the unequal
partner derivatives.

Root analytical review: PASS. The review separately checked a=0,
the actual scalar gauge convention, full generic fixed-jet bounds,
all boundary product units, and coefficient extraction with a regular
surrounding contraction. Neither review infers a native matrix norm
or a whole-source estimate from the face metric's root values.
