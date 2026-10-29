# An exponentially tame completion of the original source

28 October 2026. The known positive-integer-carry completion has a
source-preserving deformation which makes its ENTIRE overflow part
arbitrarily small exponentially, in the original balanced flat norm.
This is a quantitative result for every fixed signed braid or marked
plat, before taking absolute estimates. It removes one specified
family of source-zero completion branches; nilpotence alone had not
provided such an estimate.

The genuine degree-zero original word is unchanged. Its geometric
critical support, singular cycle boundaries and scalar exponential
estimate remain to be controlled. This theorem does not make those
remaining contributions small, and it is not a volume bound.

## 1. Keep the original crossing and its carry extension

Put d=N-1, Q=exp(2 pi i/N), x=-exp(-pi i/N). Let R_plus and
R_minus=R_plus^(-1) be the ORIGINAL complete balanced crossings,
including their common Cartan scalar. The independently proved
[Euler completion](actual_crossing_euler_completion_and_weight_source.md)
has

    R_tilde_plus=R_plus+Delta_plus,
    R_tilde_minus=R_minus+Delta_minus,
    Delta_minus=-R_minus Delta_plus R_minus.        (1)

Each Delta has total INTEGER degree change exactly +N, whereas
the original crossings preserve that degree. The literal completed
crossings are mutual inverses. On b heads the positive-carry ideal
has bth power zero.

For an arbitrary scalar z define

    R_(sigma,z)=R_sigma+z Delta_sigma.             (2)

The two signs in (2) remain literal inverses: locally
Delta_plus R_minus Delta_plus=0. For z=r^N, (2) is exactly

    R_(sigma,z)=r^D R_tilde_sigma r^(-D),          (3)

where D is local total integer head degree. This is an algebraic
identity, not an estimate in an ill-conditioned changed metric.
In particular the original degree-zero R_sigma in (2) is untouched.

For ANY signed word beta on b heads,

    W_z(beta)=W(beta)+sum_(l=1)^(b-1) z^l W_l,
    W_l has degree +lN.                           (4)

Thus the number of carry orders is bounded by braid width, not N
or word length. Its entire original pivotal first-cut matrix equals
that of W for EVERY z. Closing the other heads requires a first
input/output difference strictly between -N and N, which excludes
every positive carry. All original full dimension, peripheral,
framing and Cartan factors multiply the same matrices and remain.
The identity (4) also holds as the original root meridian family;
the quantitative norms below are stated at complete color.

The same exact source identity holds for the original marked plat.
For 2k heads, the cups have total input degree kd. The k-1 ordinary
caps fix degree (k-1)d and the FULL marked pair accepts degree from
0 to 2d. Hence the allowed total degree difference lies in [-d,d],
again excluding +lN. No cap or marked row is replaced here.

## 2. The factorized quantum atom is retained

In the relative algebra H^N=1, Hf=Q^(-1)fH, f^N=0, let e_j be
its original right idempotents and write

    f_z=f[1-(1-z)e_d].                            (5)

Its right multiplication is the old nilpotent shift except that
its wrapped step has weight z. The two-head fusion C preserves
integer degree. The original right-coefficient calculation gives

    R_(+,z)=C right[kappa U_x(f_z) D_x(H)] C^(-1),
    U_x(t)=sum_(a=0)^d x^(-a)t^a/F_a,
    D_x(H)=sum_(k=0)^d (-1)^k Q^(k(k-1)/2)x^(-2k)e_k. (6)

Indeed the coefficient of f^a e_k in U_x(f_z)D_x is its old
completed coefficient multiplied by 1 if a+k<N and by z otherwise.
There is at most one wrap. This proves (6), including the literal
inverse with the original reversed factor order. No positive model
or postulated tetrahedral weight is introduced.

Since f_z^N=0, any anchored analytic cyclic-dilog completion with
the same first N Euler coefficients acts identically on f_z. The
literature norm-one functions and every norm factor can therefore
be retained exactly as in the existing cyclic network theorem.
The boundary idempotent in (5) is NOT discarded: damping is a
controlled regularization of its carry, not a claim that the wall
or its full inserted Ward complex has vanished.

For 0<=z<=1, right multiplication by f_z is a weighted partial
permutation of norm at most one in the original relative monomial
basis. D_x and its inverse have norm one at complete color.

## 3. Uniform original-metric exponential bounds

Here are bounds with an explicit constant and no unspecified
factorial conditioning. For 0<=a<N,

    |F_a|<=2^N,
    1/|F_a|<=(N/2)^a/a!,
    sum_(a=0)^d 1/|F_a|<=exp(N/2).               (7)

To prove the middle inequality, sort any a distinct nonzero root
factors |1-Q^j|. The kth smallest is at least 2k/N: its distance
from a multiple of N occurs at most twice, and
2sin(pi s)>=4s for 0<=s<=1/2. Their product is at least
(2/N)^a a!. This applies to the actual initial root products.

For completeness, fix a total degree T in the actual fusion (1)
of the completion proof. Its block, with indices u<=a, factors as

    C_(u,a)=l_u M_(u,a) r_a,
    l_u=x^u F_(T-u),
    M_(u,a)=1/F_(a-u),
    r_a=x^(-a) F_a/F_(T-a).                       (8)

All indices lie in [0,d]. The triangular Toeplitz M is a finite
Euler function of a unit-norm shift. Its inverse has the same
coefficient magnitudes, by the finite Euler convolution. Equation
(7) therefore gives

    ||C||<=exp[(1+2log2)N],
    ||C^(-1)||<=exp[(3/2+log2)N].                 (9)

For example the three inverse factors in (8) have norms at most
2^N exp(N/2), exp(N/2), exp(N/2). These are bounds in the ORIGINAL
balanced physical and relative monomial metrics. They do not claim
that C is isometric.

The Euler factor and its inverse in (6) each have norm at most
exp(N/2). Put

    A=3+3log2.

Equations (6)--(9) imply

    ||R_tilde_sigma||<=exp(AN),
    ||R_sigma||<=exp(AN),
    ||Delta_sigma||<=2exp(AN).                    (10)

For the middle bound the original R is the block-diagonal
degree-zero part of its completion, an orthogonal degree pinching
of norm at most one. The same argument applies to the literal
negative inverse. The original complete kappa has modulus one
and is included throughout.

## 4. Entire overflow is arbitrarily small before an absolute bound

Let the fixed signed word have m crossings, and choose

    z_N=exp(-tau N), tau>=0.

Tensoring with untouched heads changes none of the local norms.
The ordinary product telescoping identity and (10) give

    ||W_(z_N)-W||
      <=2m 3^(m-1) exp[(mA-tau)N].                (11)

For any prescribed L>0 choose tau>=mA+L. The entire carry error
then has norm at most 2m3^(m-1)exp(-LN), while its original closed
source is EXACTLY zero by (4). This holds for both signs in the
same original flat metric, without changing that source to a
conjugated or exponentially conditioned boundary vector.

The trace norm of the original reduced first-cut functional is
at most N^(b-1), since every closed pivot is unitary. Original
finite cups/caps likewise have polynomial norms at complete
color. Thus (11) also bounds their absolute carry contributions
by a polynomial times exp(-LN), with the external source line
chi_N retained explicitly. This does not require taking absolute
values of the individually enormous unregularized carry paths.

The finite factor-path absolute envelope can also be controlled,
without relying on cancellation inside C or its inverse. For an
N^2-by-N^2 matrix T, its entrywise absolute matrix obeys
||abs(T)||<=||T||_HS<=N||T||. Right Euler monomial shifts are partial
permutations, so their entrywise absolute sum still has norm at
most exp(N/2). The Gaussian absolute matrix is the identity.
Consequently the nonnegative matrices summing all unwrapped or
wrapped local C/Euler/Gaussian/C^(-1) paths each have norm at most

    L_N=N^2 exp(AN).

Each wrapped path in (5)--(6) has exactly one factor z. In a word,
the sum of absolute weights of paths with at least one wrap is
therefore bounded in operator norm by

    m 2^(m-1) N^(2m) exp[(mA-tau)N].             (12)

The positive-carry degree restriction actually forbids those paths
from the plain original closed source term by term. Estimate (12)
also applies before that contraction, or after polynomially bounded
inserted coupons, when the simple closed-source degree exclusion is
unavailable. Thus the quantitative claim is not an inference from
source cancellation or an exchange of an infinite scalar expansion.
It concerns the specified finite factor expansion; an arbitrary
later scalar-contour rewriting must retain its own source identity.

There is also a controlled extension to the earlier coupon caveat.
Insert finitely many specified matrices whose original norms are
polynomial in N, including fixed products of normalized E,F,K
Ward coupons. Their completed-minus-original sourced products
obey the same telescoping estimate with those polynomial factors.
The equality is generally NOT exact for degree-lowering coupons;
the known N=2 example becomes z_N times its original nonzero
carry value. It is now smaller than any desired exponential rate
by increasing tau. No moving-q normal identity is inferred.

In particular let Q_in,Q_out be any of the specified physical
Hopf/Ward matrices, of polynomial norm, satisfying the exact actual
identity R_sigma Q_in=Q_out R_sigma. The deformed factor has

    ||R_(sigma,z_N) Q_in-Q_out R_(sigma,z_N)||
       <=2 exp[(A-tau)N] (||Q_in||+||Q_out||).     (13)

Thus the damping can preserve the entire fixed finite collection
of original Ward identities to an arbitrarily negative exponential
order, even when their individual degree-lowering coupons detect
the undamped carry. This is a norm statement on the original
source complex. It does not identify stationary branches of an
uncontrolled scalar factorization merely from those equations.

## 5. Exact scope for a global critical upper bound

This is a source-preserving analytic completion with a verified
absolute norm estimate for its entire source-zero overflow. Its
matrix kernels are finite Laurent polynomials of degree O(N) on
each local input/output pair, and (4) is polynomial in z of degree
at most b-1. It can be inserted into the existing fixed-variable
Euler/cyclic-dilog scalar networks; it introduces no hidden
N-rank co-source or unknown scalar normalization.

It does NOT prove that every stationary point of an arbitrary
scalar factorization is physical, or that a raw scalar cycle can
be replaced by its geometric contour. The idempotent (5), genuine
degree-zero kernel, clock feedback and source/cycle boundaries
remain. Excluding their nonphysical limiting stationary strata,
or showing their aggregate cancellation, is the remaining task.
In particular (11) is not an exponential estimate for W itself
or for its original knot scalar. It removes the additional
positive-N carry branches of this specified completion from that
problem, with an arbitrarily strong bound rather than a formal
source-null assertion alone.

## 6. Reproducible audit

    python3 experiments/audit_actual_exponentially_tame_carry_completion.py

The audit verifies (5)--(6), degree-gauge covariance, literal signed
inverses, and complete original one-cut/marked-plat sources for
several nontrivial signed words. It independently tests the fusion
factorization (8), the inverse Euler Toeplitz blocks, and the
claimed original-metric inequalities on complex matrices. The
all-level proof is (7)--(11), not a finite inference.
