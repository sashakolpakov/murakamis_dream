# Actual ordinary-color q-jets: one-volume growth and a macroscopic tame source

28 October 2026. The ordinary-color VALUES are polynomial at q_N, but
their q-normal derivatives need not be. For the actual figure-eight
state, the first derivative at color N-1 has the sharp volume exponent,
with an explicit positive formula and leading constant. Nevertheless
EVERY fixed-order q-jet, uniformly over all ordinary colors, has at most
that ONE-volume exponent, not two volumes.

A separate positive-plat argument gives a genuinely broad source
filtration: every fixed q-jet is polynomial for colors
k(j-1)+1<=N in a fixed k-bridge presentation. This includes the entire
figure-eight half-orbit and its midpoint. It permits restarting the
actual fixed-budget pointed recurrence at a macroscopic color, with
polynomial data and no input from the complete value.

## 1. The actual whole-source cyclotomic polynomial

Use the independently proved ordinary-color identity

    C_j(q)=sum_(k=0)^(j-1) T_(j,k)(q),
    T_(j,k)=product_(r=1)^k
                    (q^(2j)+q^(-2j)-q^(2r)-q^(-2r)). (1)

Its reduced unknot normalization, crossing Cartan phases and zero
framing are the original ones. At roots (1) is the actual Newton
state of the pointed Green theorem; for fixed j the generic Laurent
identity follows from the independently identified ordinary quotient
at infinitely many levels. Thus (1) is not fitted to K_N.

Put q_N=exp(pi i/N), Q=q_N^2, F_k=(Q;Q)_k and

    J(s)=integral_0^s log(2sin(pi t))dt,
    gamma=max J=J(5/6), Delta=2gamma=Vol(4_1)/(2pi).

All q-derivatives below keep the integer color j FIXED. They are not
meridian derivatives or derivatives along a changing root level.

## 2. A sharp exact first jet at the top ordinary color

Write D_q=q d/dq. For every N>=3,

    (D_q C_(N-1))(q_N)
       =-2N(Q-Q^-1) sum_(k=1)^(N-2)
                         |F_(k-1) F_(k+1)|/|F_2|.     (2)

Every summand is POSITIVE real before the displayed common phase.
Indeed all nonconstant T_(N-1,k) contain the root-zero factor r=1.
Its derivative is -2N(Q-Q^-1). Every remaining factor is

    Q+Q^-1-Q^r-Q^-r
       =4sin(pi(r+1)/N)sin(pi(r-1)/N)>0,
                    2<=r<=N-2.

Multiplication gives precisely the factorial quotient in (2), with
the k=1 empty product equal to one. This is a derivative of the
COMPLETE original ordinary state, rather than an individual large
summand. Its value C_(N-1)(q_N)=1 does not control this jet.

The exact leading asymptotic, through ALL integer levels, is

    (D_q C_(N-1))(q_N)
        =-i N^(7/2)/(pi 3^(1/4))
                         exp(N Delta)(1+o(1)).        (3)

Proof. Uniformly on compact 0<s<1 the elementary factorial estimate is

    |F_k|=sqrt(2Nsin(pi k/N)) exp(NJ(k/N))(1+O(1/N)),

and its all-index version has logarithmic error O(log N). Also
|F_2|=8pi^2/N^2 (1+O(N^-2)). Thus the summand in (2), at s=k/N,
is

    [N^3 sin(pi s)/(4pi^2)] exp(2NJ(s))(1+O(1/N)).

The exponent has its unique global maximum at s=5/6 and second
derivative -2pi sqrt(3). Endpoint-uniform estimates discard its
complement exponentially. Rescale k=5N/6+sqrt(N)xi. The lattice
Gaussian sum has integral 3^-1/4, with arbitrary fractional part of
5N/6. Since sin(5pi/6)=1/2, its sum is

    N^(7/2)/(8pi^2 3^(1/4)) exp(NDelta)(1+o(1)).

Finally -2N(Q-Q^-1)=-8pi i(1+O(N^-2)). This proves (3).
At N=2 the only ordinary color is trivial and the first jet is zero.

## 3. Uniform ONE-volume upper bound for every fixed q-jet

For every fixed nonnegative integer r there are constants A,C_r
independent of N and j such that

    |[t^r] C_j(q_N(1+t))|
                   <=C_r N^(A+4r) exp(NDelta), 1<=j<N. (4)

The same assertion holds for logarithmic derivatives D_q^r, with a
different fixed C_r. It controls the ENTIRE fixed-order ordinary jet
vector, up to polynomial dimension factors. In particular fixed jets
do not accumulate a two-volume rate in this example.

Here is a direct all-color proof, including activated root zeros.
For each factor in (1), at q_N,

    f_(j,r)=-4sin(pi(j+r)/N)sin(pi(j-r)/N).

For r<j<N it is zero only when j+r=N, and there is at most ONE
such factor in a product. Every nonzero factor has magnitude at
least 16/N^2. Every fixed-order derivative of a factor is bounded
by C_r N^r. Repeated Leibniz differentiation therefore costs at
most C_r N^(4r) times the product of all NONZERO root factors:
there are at most N^r choices of differentiated factors, at most
r removed nonzero factors, and derivative powers cost N^r.
An undifferentiated zero simply makes that term zero.

It remains to bound these root products, not to assume them tame.
If k<min(j,N-j), their exact magnitude is

    |T_(j,k)(q_N)|
        =|F_(j+k)|/[|1-Q^j| |F_(j-k-1)|].             (5)

Its logarithm is at most N(max J-min J)+O(log N)=NDelta+O(log N).
If j>N/2 and k>=m=N-j, the zero at r=m is removed; the remaining
absolute product is EXACTLY

    |F_(k+m) F_(k-m)|/[|1-Q^m| |1-Q^(2m)|].          (6)

All factorial indices are in 0,...,N-1 and 2m<N. Since each J is
at most gamma and the two denominators are bounded below by 4/N,
(6) has the same exponential upper bound. Equations (5)--(6), the
all-index factorial estimate and the additional sum over k prove (4).
This proof does not rely on cancellations or an ordinary-jet bound
which is being inferred from the desired volume theorem.

## 4. A broad polynomial window, including the midpoint

The independent positive-plat/source proof in
[the macroscopic normal-jet window](ordinary_color_macroscopic_normal_jet_window.md)
gives, for ANY fixed knot with a k-bridge plat and every fixed r,

    |[t^r]C_j(q_N(1+t))|<=C_(K,k,r) N^(c_(K,k,r))
                     whenever k(j-1)+1<=N.           (7)

The inclusive endpoint is important. Its elementary inputs are:

* The actual endpoint-zero TL path space for the 2k(j-1)-strand
  cable has maximum height k(j-1). On the one-sided arc
  theta in [pi/(2N),pi/N), all required sine weights are positive.
* Actual colored cups have squared norm [j]^k, and the reduced
  original closure divides by exactly [j], giving the generic-arc
  bound |C_j(exp(i theta))|<=[j]_theta^(k-1).
* The actual zero-framed finite cut is Laurent in q^(1/2) of degree
  O_K(j^2). Clearing its denominator after a tangent-half-angle
  substitution makes an ordinary polynomial on an interval of
  length comparable to 1/N; the clearing factor varies by O_K(1).
  Elementary Chebyshev coefficient/derivative bounds give polynomial
  fixed derivatives, including at the one-sided endpoint.

The proof takes the invariant polynomial to the endpoint, rather
than differentiating a singular path basis or a zero quantum
dimension. For k>=2 the relevant ordinary [j] is nonzero.

For the figure-eight, k=2. Thus every fixed q-jet is polynomial
uniformly through j=floor((N+1)/2). In particular the midpoint has
NO positive exponential jet rate. No matching positive lower rate
is claimed there: a particular derivative may vanish. On the other
hand (3) proves sharp one-volume growth near the far endpoint.
The polynomial source filtration therefore separates actual tame
half-orbit data from exponentially large far normal response.

## 5. Restart the ACTUAL pointed system without using C_N

Assume k>=2; the one-bridge unknot is already identically one. Let an
actual all-level annihilator have order d and pole budget B
as in the pointed Gram theorem. Define

    J_N=1+floor((N-1)/k),
    j0=J_N-d+1.

For large N, j0 is beyond the fixed exceptional starting colors.
Prescribe the actual B-jets of C_(j0),...,C_(j0+d-1), all inside
the polynomial window (7), and impose the SAME all-level recurrence
through color N. This produces an exact tail pointed system with
polynomial source supported in its initial d blocks.

The original valuation proof still makes its constant values unique:
the sum of leading-coefficient zero orders over this TAIL is no
larger than the original uniform budget B. Subtraction of any two
solutions with zero prescribed initial jets therefore leaves every
constant coefficient zero. Nothing in that induction requires a
starting color fixed independently of N; the bounded source was the
missing quantitative input, now supplied by (7).

After the same jet scaling the tail bulk symbol and all normal
resonance data are unchanged. Its starting coordinate tends to 1/k,
rather than zero. This is an actual source-preserving improvement,
not a definition using an unknown target value. A tail Green/transfer
estimate still needs its singular-step and spectral control. In
particular a general sharp Vol conclusion does not follow merely
from this restart, nor from the figure-eight calculation (3)--(4).

[Audit](../experiments/audit_actual_figure_eight_ordinary_normal_jets.py):
actual cyclotomic Taylor jets, all-color product identities, the
positive endpoint formula and leading constant, and midpoint/tail
growth diagnostics. Finite checks supplement the all-level proofs.
