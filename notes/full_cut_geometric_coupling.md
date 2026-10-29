# The actual cut has a nonzero universal radial symbol

28 October 2026. The radial integrals in the ORIGINAL all-inverse
cut cycle can be evaluated asymptotically, uniformly for bulk cut
labels and every actual coefficient order. Their leading symbol
is an explicit Gamma quotient and never vanishes. Their remaining
exponential weight is exactly an original quantum factorial, with
a fixed Gaussian phase and a universal N^(-3/2) normalization.

This removes exponential radial cancellation at the coefficient
level. It does not remove cancellation in the final angular and
head-source contraction. In particular it is not a new positive
invariant or a proof of a knot-volume lower bound.

## 1. The source and the radial moment being evaluated

Use the exact [all-inverse cut cycle](actual_cyclic_dilog_hankel_cycle.md).
For epsilon=+1 or -1, Q=exp(2 pi i/N), 1<=j<N and u=j/N, its
j-th cut has

    h_(epsilon,j)(r)=(r-1)^(-u)
        product_(k!=j, 1<=k<N)
                    (1-r Q^[epsilon(k-j)])^(-k/N), r>1,
    g_(epsilon,j)(r)=(r-1)^u h_(epsilon,j)(r).

The non-endpoint logarithms have their specified radial marks.
Define its ORIGINAL, jump-weighted coefficient moment by

    R_(epsilon,N)(j,a)=sin(pi u)/pi
        * integral_1^infinity h_(epsilon,j)(r)r^(-a-1)dr,
                                                   a>=0. (1)

The actual coefficient formula is

    c_(epsilon,a)=sum_(j=1)^(N-1)
                         Q^(epsilon j a) R_(epsilon,N)(j,a). (2)

The entire head source and all original Gaussian/pivotal factors
remain in the ordered network. Thus (1) is an actual contraction
within that exact representation, not a chosen substitute period.

## 2. Exact complex endpoint, including its phase

Put

    F_(epsilon,j)=(Q^epsilon;Q^epsilon)_j,
    C_(epsilon,N)=exp[-epsilon pi i (N-1)(N-2)/(12N)].

Then the exact endpoint value is

    g_(epsilon,j)(1)
        =C_(epsilon,N) F_(-epsilon,j)/N^(u+1/2).   (3)

The modulus was already computed in the cut-cycle note. Here its
phase is also explicit. For epsilon=+1 and k!=j,

    arg(1-Q^(k-j))
       =pi(k-j)/N-(pi/2)sign(k-j).

Summing with the coefficient -k/N gives

    arg g_(+,j)(1)
      =-pi(N-1)(N-2)/(12N)+pi j(N-1-j)/(2N).

The j-dependent term is exactly the product phase of
F_(-,j). All factors in this calculation have the specified
radial logarithms; no branch is reset after the sum. Conjugation
proves epsilon=-1. Thus (3) retains the actual unit-modulus
global line as well as the factorial modulus.

## 3. The universal scaled radial profile

Write

    q(u)=log(2 sin(pi u))/(2 pi).

For every compact U contained in (0,1), uniformly for j/N in U
and bounded real s>=0,

    g_(epsilon,j)(exp(s/N))/g_(epsilon,j)(1)
      -> exp[-s/4+i epsilon q(u)s]
             [sinh(s/2)/(s/2)]^(-u).              (4)

The value of the last bracket at s=0 is one. In particular this
profile is nonzero, and its phase is the explicit linear phase
epsilon q(u)s. The radial profile is real positive precisely
when q(u)=0, namely u=1/6 or 5/6.

### Proof directly from the weighted finite root sum

It is enough to take epsilon=+1. Put r=exp(s/N). Differentiate
the marked logarithm of the ratio in (4):

    partial_s log[g_j(r)/g_j(1)]
       =-(1/N)sum_(k!=j) (k/N)
                 r Q^(k-j)/(r Q^(k-j)-1).         (5)

First adjoin the k=0 term, whose TOTAL weight k/N is zero.
In the following split both sums therefore run over
0<=k<N, k!=j; their introduced k=0 contributions cancel.
Set y_k=(k-j)/N, so k/N=u+y_k. The constant-u part of (5) is
EXACTLY

    -u [e^s/(e^s-1)
              -e^(s/N)/(N(e^(s/N)-1))].          (6)

This follows from the logarithmic derivative of
product_(l=0)^(N-1)(rQ^l-1), subtracting its l=0 term.
Both apparent s=0 singularities cancel. Uniformly for bounded
s, (6) tends to

    -u[e^s/(e^s-1)-1/s].

The y_k part converges uniformly to

    -integral_(-u)^(1-u) y e^(2 pi i y)/(e^(2 pi i y)-1)dy
       =-1/4+u/2+i q(u).                          (7)

The apparent singularity at y=0 is removable in the limiting
integrand. A direct uniform Riemann-sum justification is available:
away from zero it is ordinary smooth convergence; near zero the
difference between its r>1 and r=1 values is bounded by
C(r-1)/(|y|+r-1). The resulting summed error is O_U((1+S)log N/N)
on 0<=s<=S, with the single omitted grid point contributing
O(1/N). There are no other singularities because u stays in U.

To evaluate (7), use

    e^(2 pi i y)/(e^(2 pi i y)-1)
                              =1/2-(i/2)cot(pi y),
    integral_(-u)^(1-u) y cot(pi y)dy
                              =log(2 sin(pi u))/pi.

The latter follows by integration by parts; the integral of
log|sin(pi y)| over this length-one interval is -log 2.
Combining (6)--(7), the limiting logarithmic derivative is

    -1/4+i q(u)-u[(1/2)coth(s/2)-1/s].

Integration from zero proves (4), uniformly as stated.
The epsilon=-1 result is its conjugate.

## 4. A uniform nonvanishing Gamma symbol for the actual radial integral

For u in (0,1) and v>=0 define

    alpha_(epsilon)(u,v)=v+1/4+u/2-i epsilon q(u),
    K_(epsilon)(u,v)=Gamma(alpha_(epsilon)(u,v)) /
         [Gamma(u) Gamma(alpha_(epsilon)(u,v)+1-u)]. (8)

For every compact U contained in (0,1) and every finite V,
uniformly for j/N in U and 0<=a/N<=V,

    R_(epsilon,N)(j,a)
      =C_(epsilon,N) N^(-3/2) F_(-epsilon,j)
                       [K_(epsilon)(u,a/N)+o_(U,V)(1)]. (9)

There is no zero or pole of K on this domain: the two nonconstant
Gamma arguments have strictly positive real parts, and Gamma has
no zeros. Consequently |K| is bounded above and away from zero
on every such compact domain. Formula (9) can equivalently be
written with the nonzero leading term times 1+o(1).

There is a stronger sign statement. Put x=v+1/4+u/2>0. Expanding
(1-exp(-s))^(-u) in its positive binomial series inside (11) gives
the absolutely convergent Stieltjes expansion

    K_(epsilon)(u,v)=sin(pi u)/pi
          * sum_(k>=0) (u)_k/[k! (x+k-i epsilon q(u))]. (8a)

Every summand has positive real part, so

    Re K_(epsilon)(u,v)
        >=sin(pi u)/pi * x/[x^2+q(u)^2]>0,        (8b)
    sign Im K_(epsilon)=sign(epsilon q(u)),
    |Im K_(epsilon)|<=(|q(u)|/x) Re K_(epsilon).  (8c)

At q(u)=0 the imaginary part is zero. In particular the radial
symbol is STRICTLY ACCRETIVE, with an explicit positive uniform
lower bound on every bulk compact u interval and bounded v
interval. This sign follows from the original cut integral after
its specified endpoint phase has been factored out; it is not a
positivity claim about the unnormalized whole knot state.

For its proof change variables r=exp(s/N) in (1). After division
by g_j(1) N^(u-1), the integral is exactly

    sin(pi u)/pi * integral_0^infinity
      [N(exp(s/N)-1)]^(-u) [g_j(exp(s/N))/g_j(1)]
                                         exp[-(a/N)s]ds. (10)

The exact radial envelope proved for the original cycle gives

    |g_j(exp(s/N))/g_j(1)|<=exp[-(C_j/N)s],
    C_j=(N-1)/4-u/2.

For all sufficiently large N, C_j/N>=1/8, uniformly in j.
Also N(exp(s/N)-1)>=s. Thus (10) is dominated by an integrable
function independent of j,a,N when u is restricted to U. The
local convergence (4) is uniform, so uniform dominated convergence
applies, including all actual orders 0<=a<N.

The limiting integral is

    sin(pi u)/pi * integral_0^infinity
       [2sinh(s/2)]^(-u)
                      exp[-(v+1/4-i epsilon q(u))s]ds
      =sin(pi u)/pi * B(alpha_(epsilon)(u,v),1-u)
      =K_(epsilon)(u,v).                          (11)

In the beta integral put x=exp(-s); the last equality is the
Gamma reflection identity. Combining with the EXACT endpoint
(3) proves (9). In particular the factors N^(u-1) and
N^(-u-1/2) cancel to the universal N^(-3/2).

## 5. The resulting actual angular source and its limitation

Consider the exact full all-inverse word with s=9m cut variables,
and restrict its angular labels j_l/N to compact subintervals of
(0,1). Expand the ORIGINAL rational source into its finitely many
coefficient orders a_l>=0. Its exact radial integration is the
product of the moments (1). Formula (9) therefore supplies

    product_l [C_(epsilon_l,N) N^(-3/2)
                F_(-epsilon_l,j_l)
                K_(epsilon_l)(j_l/N,a_l/N)]       (12)

as its uniform leading coefficient kernel, with relative o(1)
in each coefficient. All head bounds, Fourier characters,
Gaussian matrices and the pivotal source remain in that array.

The multipliers K form a smooth, nonzero coefficient symbol. On
each bulk coefficient box the diagonal multiplication by their
product and its inverse have bounded norms in coefficient-space
ell^p for every p. This is a statement BEFORE the final linear
source contraction; it makes no claim about the physical fusion
metric or a lower bound after cancellation. The uniform error is
controlled by the corresponding absolute weighted coefficient
sum. It need not be small RELATIVE to the selected scalar.

More explicitly let J_N=diag(0,...,N-1) on the power-coefficient
space of one actual atom, with its ordinary orthonormal degree
basis. Define the NORMALIZED EXACT radial multiplier

    T_(epsilon,N,j)=diag_(0<=a<N)
        [R_(epsilon,N)(j,a) /
              (C_(epsilon,N) N^(-3/2) F_(-epsilon,j))]. (12a)

For bulk j/N in U, (9) is precisely the uniform operator-norm
statement

    ||T_(epsilon,N,j)-K_(epsilon)(u,J_N/N)|| -> 0. (12b)

Let gamma_(U)>0 be the minimum of the explicit right side in
(8b) for u in U, 0<=v<=1. For all sufficiently large N,

    Re T_(epsilon,N,j) >= (gamma_(U)/2) I,
    ||T_(epsilon,N,j)^(-1)|| <=2/gamma_(U),        (12c)

uniformly in these labels. Its norm is also uniformly bounded,
so its condition number is bounded. Equivalently every coefficient
vector f obeys

    Re <f,T_(epsilon,N,j)f>
                            >=(gamma_(U)/2)||f||^2.

The factorial and Gaussian endpoint line in (12a) remains its
explicit original factor. A general pivotal source is not this
positive quadratic pairing. Tensoring several such factors also
does not automatically keep their arguments in a common positive
half-plane. Thus (12c) is an actual radial coefficient estimate,
not the missing final scalar lower bound.

In a separately justified Laplace comparison on a real bulk chain,
with a strictly nondegenerate maximum of the real exponent and a
nonzero source amplitude, this uniform symbol changes the local
leading amplitude by the explicit nonzero Gamma factors. No such
chain for the whole knot is constructed here. In particular (9)
alone does not justify a deformation to complex angular labels or
termwise replacement after an uncontrolled oscillatory contraction.
Proving that the actual angular source selects the geometric point
is still necessary.

This can already be seen for one coefficient in (2). The leading
angular phase of its factorial and Fourier character is

    Phi_(epsilon)(u,v)
       =J(u)+(epsilon pi i/2)(u-u^2)+epsilon 2 pi i u v.

Its stationary equation is

    [1-exp(-epsilon 2 pi i u)] exp(epsilon 2 pi i v)=1. (13)

Thus the familiar complementary shape relation emerges directly
from the actual cut. For arbitrary real v its critical u is
complex; the real angular grid does not automatically pass through
it. When u=5/6, v=1/6, the endpoint absolute-envelope maximum is
a stationary point and K is positive. Those special values do
not give a general knot argument: the whole network couples all
v through its original heads and phases.

The bulk radial theorem therefore removes one concrete possible
source of exponential cancellation and supplies an actual,
nonvanishing amplitude for the next angular comparison. It does
not justify replacing (12) by its absolute value, deleting K,
ignoring the nonbulk labels, or inferring that the selected
geometric contribution cannot cancel with the rest of the word.

[Profile, endpoint-phase and moment audit](../experiments/audit_full_cut_geometric_coupling.py)
and [saved diagnostics](../experiments/full_cut_geometric_coupling_results.json).
