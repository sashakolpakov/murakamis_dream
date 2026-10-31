# Exact Bell weights and a source-balanced positive Gram

29 October 2026. The phase-ratio coefficient of the original conjugate
source has one positive angle-energy profile, rather than its square.
Its radius factors and normalization are explicit. A second result
constructs a canonical positive Gram for the ACTUAL right/left Fermat
frames: both source costs reduce to a rational chord sum, polynomial
away from the normalized central divisor. With the original cap
normalizers retained, the cost is O(1+|epsilon|logN) uniformly at
every cap index. This supplies a quantitative special-inner-product
input, not a bound on the interior original word.

## 1. Exact magnitude on the Fermat fiber

Use sigma=-1 and the actual normalized P,L and Bell basis of
[the source-exact reflection theorem](phase_ratio_double_and_fermat_source.md).
Let u^N+v^N=1 and assume the factors below are nonzero. Define

    t=v/barv, a=baru/u,
    A_j=|1-t Q^(-j)|,
    B_j=|1-a Q^j|,
    C_j=|1-at Q^j|.

The two original source equations give BOTH recurrences

    |c_(s,r+1)|/|c_(s,r)|=A_r/(|u| C_(s-r)),
    |c_(s,r)|/|c_(s-1,r)|=|v| C_(s-r)/B_s.        (1)

For n in Z define Cprod(0)=1 and
Cprod(n)/Cprod(n-1)=C_n, using reciprocal products for n<0.
Put

    f_(s,r)=|u|^(-r)|v|^s
          [product_(j=0)^(r-1) A_j] Cprod(s-r)
                             /[product_(j=1)^s B_j],
                  0<=s,r<N.                     (2)

Empty products equal one. Starting at (0,0), (1) proves

    |c_(s,r)|=kappa_N f_(s,r),
    kappa_N=||P||_2^2/[sum_(s,r) f_(s,r)^2]^(1/2).              (3)

This determines the normalization by a specified positive finite
sum, with no unknown knot period. Indeed the Bell transform is
unitary and its input is P tensor barP, so sum|c|^2=||P||^4.
The all-nonzero theorem on the open positive-central fiber justifies
normalizing at (0,0). Other nonsingular root marks have the same
formula with their actual chord factors, not principal arguments
silently substituted.

On the PRINCIPAL positive-central component, kappa_N=c_(0,0)>0
also fixes the scalar phase. The defining sum for c_(0,0) is real
by pairing a with -a. It never vanishes on this connected component
by (1), and as U=u^N tends to zero in the upper half-plane the
principal roots give P_a->1 and c_(0,0)->sqrtN. Hence its sign is
positive everywhere there. A different root mark must keep its own
phase; this argument does not silently identify those marks.

If the actual column is Gamma P, multiply c and kappa_N by
|Gamma|^2. No Gamma, inverse-frame normalization or cap residue
factor has been removed. The radii |u|,|v| in (2) may depend
arbitrarily on N. Formula (3) remains exact and does not declare
kappa_N or those radius factors subexponential.

## 2. Three shifted positive factorials, and both chambers

For a Frobenius center U=u^N in the upper half-plane, take the
principal marked roots and write

    alpha=Arg(U)/pi, beta=-Arg(1-U)/pi,
    gamma=alpha+beta,
    0<alpha,beta,gamma<1.

Define the positive shifted factorial

    T_N(L;delta)=product_(j=1)^L 2sin[pi(j+delta)/N],
    -1<delta<0, 0<=L<=N.

Every displayed sine is positive. Set

    A_full=|1-t^N|, C_full=|1-(at)^N|.

Reflection of the numerator arcs in (2) gives the exact formulas

    r>s:
    |c_(s,r)|=kappa_N A_full |u|^(-r)|v|^s
       /[T_N(N-r;-beta) T_N(s;-alpha)
                                T_N(r-s;gamma-1)],              (4)

    r<=s:
    |c_(s,r)|=kappa_N A_full C_full |u|^(-r)|v|^s
       /[T_N(N-r;-beta) T_N(s;-alpha)
                                T_N(N-s+r;gamma-1)].            (5)

Proof. A_j=2sin[pi(j+beta)/N], B_j=2sin[pi(j-alpha)/N].
For r>s the reciprocal negative-index Cprod gives the factors
2sin[pi(j+gamma-1)/N], j=1,...,r-s. Replace the A numerator
by its complete product divided by the remaining arc, and reflect
that arc. This proves (4). For r<=s also complement the positive
C numerator by its complete product; the same reflection proves (5).

The three lengths sum to N in (4), and their shifts sum to -1.
On the STRICT chamber 0<s<r<N all three shifted endpoints are
positive and sum to d=N-1. Thus (4) has ONE angle-energy weight,
not a square-root amplitude weight and not its square. In (5) the
lengths sum to 2N and the shifted endpoints sum to 2N-1. Boundary
rows, including s=0, retain their literal empty products; a negative
formal shifted endpoint is not declared a geometric angle. The
full half-phase/sign accounting is in the reflection theorem and
is not replaced by choosing the favorable chamber.

For shifts in a fixed compact subset of (-1,0), lengths at most
N-1, these T_N factors differ from the unshifted s_N factors
by polynomial factors: separate the first factor and integrate
the logarithmic derivative, bounded by the harmonic sums at the
two root endpoints. If a shift approaches a divisor, retain its
explicit factor. If L=N, T_N(N;delta)=|1-exp(2pi i delta)|,
not the forbidden zero s_N(N). No uniform polynomial comparison
through arbitrary exponentially close divisors is inferred.

In particular, U fixed and u=U^(1/N) is only one parameter regime.
A fixed semiclassical radius |u|!=1 has an exponentially varying
Frobenius center. Equations (2)--(5) retain that regime rather than
identifying it with the fixed-center estimate.

## 3. An explicit non-diagonal Bell Cauchy metric

For the full positive array f in (2), give an exterior array b the
norm squared sum f_(s,r)|b_(s,r)|^2. Its original source functional
sum c_(s,r)b_(s,r) has exact Riesz norm squared

    sum |c_(s,r)|^2/f_(s,r)=kappa_N^2 sum f_(s,r).                (6)

Thus an explicit positive Gram exists in the Bell space; in the
original doubled head coordinates it is a conjugate of diag(f)
and is generally nondiagonal. It retains ALL sectors. The phase
choice b=barc/|c| attains the corresponding weighted Cauchy bound,
so (6) is a sharp local all-exterior statement.

The coefficient c already belongs to a DOUBLED amplitude. Squaring
its contraction again proves a fourth-power statement, not the
desired |K|^2 estimate. Direct triangle comparison instead reads

    |sum c b|<=kappa_N sum f |b|.                 (7)

If the actual remaining contraction has |b| bounded polynomially
and the actual edge projector is diagonal in this SAME joint basis,
(4)--(7) supply a one-power positive partition comparison. Those
conditions on the remaining original contraction are not proved
here. Introducing a dephasing or discarding (5) does not establish
them. Normalization (6) is also explicit rather than assumed tame.

## 4. A stronger Gram balances the actual source AND co-source

There is a useful quantitative alternative which does not require
the Fermat equation. For the literal P,L in either orientation,
when u^N!=1 and v!=0, finite cancellation gives

    L_a P_a=(1-u)/(1-u Q_s^a).

Define

    H_a=|L_a|/|P_a|>0,
    U_a=(L_aP_a)/|L_aP_a|.

Then EXACTLY

    L=P^* H U, U unitary diagonal,
    P^*H P=L H^(-1)L^*
       =S_N(u):=|1-u|sum_(a=0)^d 1/|1-u Q_s^a|.                (8)

This is a prescribed positive inner product, constructed from
the known cyclic source frames, not from a knot value. For every
specified exterior A,

    |L A P|<=S_N(u)||A||_H.                      (9)

The phase U in (8) is compulsory; no positive pivotal trace is
claimed. If the actual rows/columns are Gamma_L L,Gamma_R P,
their balanced source norm squared is |Gamma_L Gamma_R|S_N.
The Gamma product is part of (9), even when exponential.

There is an elementary radius-uniform estimate

    S_N(u)<=2N^2 max(1,|u|^N)/|1-u^N|.            (10)

Indeed (1-u^N)/(1-uQ_s^a)=sum_(k=0)^d(uQ_s^a)^k.
Its absolute value is at most N max(1,|u|^d). Sum over a and
use |1-u|<=1+|u|. This proves (10) for arbitrary N-dependent
radii. A polynomial lower bound on the NORMALIZED central
separation |1-u^N|/max(1,|u|^N) makes this source cost polynomial.
It is not a lower bound on that separation when a source pole
approaches the contour.

On the doubled head, use H tensor H. The original doubled source
and co-source both have norm squared S_N^2. In the unitary Bell
basis its Gram is explicitly Bell^*(H tensor H)Bell, generally
NONDIAGONAL. Formula (4) of the reflection theorem preserves the
magnitudes of P,L, so this H is invariant under the source
antiinvolution, and its compulsory co-source clock is unitary
for H as well. No small-root or fixed-radius argument is needed.

The phase-ratio observables are unitary in the flat cyclic metric;
they need not be unitary for H. Nor is a diagonal H at one quad
chart automatically the diagonal metric at the next chart.
Transporting this Gram and retaining its off-diagonal terms is
essential. A flat diagonal edge projector need not be contractive
in the transported source metric.

The [selected corner-sector theorem](phase_ratio_corner_sector_metric.md)
proves a precise boundary exception: the doubled metric is scalar on
the actual corner's clock-sum sector for real cap parameters, and has
polynomial condition number there throughout the complex cap disk.
Orthogonal projectors restricted to that sector therefore have a tame
norm. This does not discard the other regularized-cap sectors or prove
that an interior crossing preserves the selected sector.

## 5. Polynomial cost at EVERY actual normalized cap

In the literal cap orientation Q_s=Q, put epsilon=v^N,

    u=Q^(-j)(1-epsilon)^(1/N), |epsilon|<=rho=1/16.

For j>=1 use the original normalized frames

    Phat_j=v^(N-j)P/alpha_j,
    Lhat_j=v^j L/beta_j,
    alpha_j beta_j=N(1-Q^(-j)).

For j=0 use P,L without those factors. Let Hhat_j be their
balanced positive metric as in (8). Their source norm squared is

    Shat_j=|epsilon| |1-u|/[N|1-Q^(-j)|]
                       sum_a1/|1-uQ^a|, j>=1,
    Shat_0=S_N(u).                               (11)

Uniformly in N,j, and the marked punctured epsilon disk,

    Shat_j<=C[1+|epsilon|(1+log N)],
    lim_(epsilon->0)Shat_j=1.                    (12)

Proof. Write delta=(1-epsilon)^(1/N). The marked logarithm gives
|delta-1|<=2|epsilon|/N. The resonant denominator is bounded
below by |epsilon|/[N(1+rho)] from
epsilon=(1-delta)sum_(k=0)^d delta^k. Every other denominator
|1-delta Q^k| is at least 3min(k,N-k)/N. Their reciprocal sum
is O(N(1+logN)). For j>=1, |1-u|/|1-Q^(-j)|<=2, giving (12).
For j=0 the resonant term in S_N is exactly one and the others
have the same bound. The resonant term tends to one in every
case and the other terms vanish. This proof keeps the actual
alpha_j,beta_j, whose separate sizes need not be polynomial.

Independent input/output caps may use different Hhat metrics.
Their original matrix element is bounded by the geometric mean
of these source costs times the operator norm from Hhat_in to
Hhat_out. Tensor products preserve this statement. The actual
corner source is obtained by Cauchy evaluation of Phat,Lhat at
zero; on |v|=rho^(1/N), each normalized dv/v circle has mass one.
Thus these cap source factors cost only polynomially in the
original whole residue presentation. The INTERIOR word norm
between those metrics, and all additional retained scalar lines,
remain to be bounded. This does not turn (12) into a knot-volume
bound by itself.

## 6. Off-Fermat/current packets are not erased

Let Delta=1-u^N-v^N and F_d=product_(a=1)^d(1-uQ^(-a)).
The normalized column satisfies B P=Delta e_0/F_d even off the
Fermat curve. Its exact Bell equations acquire

    c_sr-u c_(s,r+1)-vQ^(-r)c_(s-1,r)=h_s,
    c_sr-baruQ^s c_(s,r+1)-barv c_(s-1,r)=k_sr,
    h_s=(Delta/F_d)barP_s/sqrtN,
    k_sr=(barDelta/barF_d)Q^(-rs)P_s/sqrtN.

Consequently the recurrence behind (1) is replaced by

    [u-t baru Q^(s-r)]c_(s,r+1)
       =[1-tQ^(-r)]c_sr-h_s+tQ^(-r)k_sr.          (13)

Variation of constants retains the finite sum of both displayed
sources, with the actual cyclic closure determinant. Resonant
closure does not select a free homogeneous coefficient. Thus
(2)--(5) are exact Fermat-source formulas; extending them to a
complete inhomogeneous beta packet requires the currents (13),
not setting their central Delta to zero. The positive metric
(8)--(10) itself remains exact off the Fermat locus.

[Audit](../experiments/audit_phase_ratio_bell_weights.py): pointwise
shifted-factorial profiles and Parseval normalization, varying
radii/centers, source-balanced metrics and actual cap constants,
and the full off-Fermat source corrections.
