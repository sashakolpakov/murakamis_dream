# The actual finite-clock boundary determinant through the fold

30 October 2026. The original 222
boundary has two finite negative raw clocks, by the literal
[right-angled prefix sign theorem](actual_right_angled_resonant_prefix_signs.md).
At the ROOT this puts its actual white numerator in a positive
definite determinant, including the maximal folded channel. This
note proves a uniform relative perturbation formula which retains
the order-one transport term, and an explicit leading logarithmic
rate through the fold. The proof uses the finite determinant,
matrix traces and elementary sums, not a saddle selection assumption.

These are numerator results. Scalar phases, partner products and
all source normalization remain explicit. No genuine generic
quantum derivative, full source cycle, or volume equality follows.

## 1. The literal source and its negative raw clocks

Put N>=2, d=N-1, theta=pi/N, q=exp(i theta), Q=q^2 and
0<=a<=floor(d/2). Let H_a^1(U,V) be the root white polynomial in
the [resonant boundary theorem](actual_q_hahn_resonant_hard_edge.md).
Its exact determinant, proved in the
[complementary boundary theorem](actual_q_hahn_complementary_hard_edge.md), is

    H_a^1(U,V)=V^a K_a
       det[I-(qU/2)H_--(q^-1/(2V))H_+],
    K_a=[2a choose a]_Q.                                  (1)

The empty determinant for a=0 is one. The Hermitian positive
definite matrices H_-,H_+ have common diagonal

    d_n=1/[cos(n theta)cos((n+1)theta)],  0<=n<a,

and upper adjacent entries

    sqrt(B_n)[sin(n theta) -/+ i cos(n theta)], 1<=n<a,
    B_n=sin^2(n theta)/[cos^2(n theta)
                      sin((2n-1)theta)sin((2n+1)theta)].   (2)

Their positivity follows from the original exact Cholesky pivots;
it holds at both level parities and through the folded endpoint.

Use the ACTUAL half-index arguments

    U=q^-1 X, V=q^-1 Y, X<0, Y<0,
    alpha=-X/2>0, beta=-1/(2Y)>0.

Then the matrix in (1) is EXACTLY

    M=I+alpha H_-+beta H_+ > I.                           (3)

In particular its determinant is positive, while V^a and K_a
retain their original phases. This statement concerns the raw
clocks X,Y, not an independently rotated pair of physical heads.
The original 222 geometry supplies precisely these limiting signs.
The exact finite-r arguments differ from their limits, and are
handled next; they are not silently set equal to their limits.

## 2. Uniform relative transport, with its first correction retained

Change the coefficients in (3) to alpha(1+e_-), beta(1+e_+),
allowing complex e_-,e_+. Set eta=|e_-|+|e_+|<1 and

    E=M^(-1/2)[alpha e_- H_-+beta e_+ H_+]M^(-1/2).

Both alpha M^(-1/2)H_- M^(-1/2) and
beta M^(-1/2)H_+ M^(-1/2) are positive semidefinite, and
their sum is I-M^-1<I. Hence ||E||<=eta, with no dependence
on N,a, or a small eigenvalue of an individual H matrix.
The marked logarithm, zero when e_-=e_+=0, therefore satisfies

    Log(det(M+Delta M)/det M)=tr E+R,
    |R|<=a eta^2/[2(1-eta)],
    |Log(det(M+Delta M)/det M)|<=-a log(1-eta).          (4)

Indeed expand tr Log(I+E) in its absolutely convergent matrix
power series, use |tr E^j|<=a eta^j, and sum the terms j>=2.
This also proves nonvanishing and specifies the relative branch.

If X is changed to X(1+u) and Y to Y(1+v), the exact choices are

    e_-=u, e_+=(1+v)^(-1)-1.                            (5)

Thus O(N^-1) relative clock corrections give

    det(M+Delta M)/det M=exp(tr E)[1+O(N^-1)].          (6)

The trace need not tend to zero: it is an order-one source
transport term and must stay. Corrections O(log N/N) have at
most O(log N) logarithmic cost, with a nonzero relative factor.
The estimates are uniform through the fold. The factors V^a,
K_a and all other source factors remain outside this comparison
and are kept EXACTLY. These are clock perturbations at one root,
not the moving-Q or moving-B generic quantum derivatives.

## 3. The determinant's leading rate

Suppose a/N tends to xi in [0,1/2] and alpha,beta tend to positive
limits. The convergence below is uniform when alpha,beta stay
in compact subsets of the positive reals. For 0<=t<1/2 write

    c(t)=cos(pi t),
    D(t)=1+(alpha+beta)/c(t)^2,
    b(t)^2=[(alpha+beta)^2-4alpha beta c(t)^2]/[4c(t)^4],
    lambda_+(t)=[D(t)
        +sqrt(1+[2(alpha+beta)+4alpha beta]/c(t)^2)]/2.

The square root here is positive real. Then

    (1/N)log det M -> I(xi;alpha,beta),
    I(xi;alpha,beta)=integral_0^xi log lambda_+(t) dt.    (7)

The endpoint xi=1/2 is included. The improper integral converges
because log lambda_+(t)=O(1+|log(1/2-t)|). An a=0 subsequence
has empty determinant and rate zero.

Here is a proof from the actual finite matrices. The diagonal of
M is 1+(alpha+beta)d_n; the squared modulus of its upper entry is

    B_n[(alpha+beta)^2 sin^2(n theta)
                      +(alpha-beta)^2 cos^2(n theta)].   (8)

Away from t=1/2 these converge to D(t), b(t)^2. On each fixed
closed interval below 1/2, entries are uniformly bounded. The
few initial n, for which the B_n continuum approximation is not
uniform, do not affect the Riemann limit: after removing an
arbitrarily short initial interval convergence is uniform, while
all the removed entries have a common bound. Their contribution
to each fixed matrix trace moment is bounded by that interval's
length times a constant depending only on the moment.

For a fixed integer j, expand tr M^j into closed nearest-neighbor
walks of length j. Away from the two ends, each walk sees entries
whose variation over j indices tends uniformly to zero. The
constant-coefficient walk sum is the zeroth Fourier coefficient
of [D(t)+2b(t)cos(phi)]^j; complex offdiagonal phases cancel
because a closed walk traverses each edge equally in both
directions. Endpoint walks contribute O(j/N) to the normalized
trace. Consequently, for every polynomial P and xi<1/2,

    (1/N)tr P(M) -> integral_0^xi (1/(2pi))
                   integral_0^(2pi) P(D+2b cos phi) dphi dt. (9)

All eigenvalues of M lie in [1,C_xi] by (3) and the bounded row
sums. The limiting symbol lies in the same type of interval:
D-2b>=1. Approximate log on this interval by truncating

    log z=log R-sum_(j>=1)(1-z/R)^j/j, R>C_xi.

The tail converges uniformly geometrically since z>=1. Its trace
error divided by N is bounded by (a/N) times the uniform error.
Thus (9) holds for log as well. Finally

    D+2b cos phi=lambda_+ |1+(b/lambda_+)exp(i phi)|^2,

where b/lambda_+<1. Expanding the scalar logarithm in powers of
exp(i phi) shows that its second factor has mean logarithm zero.
This proves (7) below the fold, without invoking a limiting
matrix theorem.

To include the fold, cut off the last h<=delta N+O(1) indices.
Write M in these two principal blocks. Its Schur complement S
on the last block satisfies I<=S<=M_tail: the lower bound follows
by minimizing the quadratic form of M>=I over the first block.
The upper bound is the explicit positive Schur subtraction. Hence

    0<=log det M-log det M_bulk
       <=log det M_tail<=sum_tail log[1+(alpha+beta)d_n]. (10)

The last inequality follows, for example, from its Cholesky
pivots being no larger than its diagonal entries. With
j_n=N-2n-2>=1 at every allowed diagonal entry,

    d_n<=C N^2/j_n^2.

The j_n have step two. Integral comparison for the sum of log j
therefore bounds (10) by

    C h[1+log(N/max(1,h))]+O(log N).

After division by N this tends to zero as delta tends to zero.
The same integrable bound handles the tail of (7). This proves
the endpoint, including every sequence of actual folded colors.

For varying positive parameters, (4) bounds the normalized logarithmic
change by C(|Delta log alpha|+|Delta log beta|), uniformly in the
channel and N on positive compact sets. Thus the fixed-parameter
argument extends uniformly to compactly varying alpha,beta; the
integral in (7) has the same continuity by its integrable fold bound.

## 4. The original scalar and large partner

Let Lambda(x)=-integral_0^x log|2sin v| dv. The exact magnitude
of K_a is s_(2a)/s_a^2, where s_j=product_(r=1)^j 2sin(pi r/N).
Elementary Riemann sums, splitting off the integrable endpoint
logarithms, give

    (1/N)log|H_a^1(q^-1X,q^-1Y)|
      -> xi log|Y|+[2Lambda(pi xi)-Lambda(2pi xi)]/pi
                      +I(xi;alpha,beta).                (11)

Equation (1), not just (11), retains its complex scalar phase.
For the actual large channel m=d-a, keep the exact root identity

    H_m^1(U,V)=H_a^1(U,V)
                         product_(r=a)^(m-1)(UV-Q^r).    (12)

For xi bounded away from zero and XY in a positive compact, the
product in (12) is uniformly away from its factors' zeros. Its
additional logarithmic rate is

    integral_xi^(1-xi) log|XY-exp(2pi i t)| dt.          (13)

The finite q^-2 in UV=Q^-1 XY and the exact endpoints stay in
(12). At small colors, or under complex perturbations near any
forced divisor, use that exact product, not a claimed uniform
relative replacement of it. No derivative of (12) is used to
assert a generic quantum normal.

This is a boundary extension of the earlier strict physical-tube
theorem: the canonical raw negative clocks have limiting real
total degree one, which lies on that tube's boundary. Unlike the
whole rational column, the numerator determinant has no omitted
Delta_a(UV) denominator. This note estimates the numerator only.

The action in (7) has the original selected normalization. To check
this directly, rotate both raw clocks to X_delta=e^(-i delta)X and
Y_delta=e^(-i delta)Y, with fixed small delta>0. Their actual heads
lie in the earlier strict physical tube for all sufficiently large N.
The two determinant coefficients become alpha e^(-i delta) and
beta e^(i delta), so (4) bounds the difference of their normalized
marked logarithms from the negative-clock value by C delta,
uniformly in N and through the fold. The strict-tube theorem gives
the original selected action at each fixed delta. Taking N to
infinity and then delta to zero identifies its boundary value with
(7). The branch is transported by (4) from the positive determinant;
at X=Y=-1 this is the old real center, where the determinant is
positive, so the two branches agree there. Continuation through the
connected negative-clock quadrant retains that equality.
The exact factors V^a and K_a are still those of (1). No unrelated
solution of the characteristic equation or new additive constant
is being selected by the trace-walk calculation.
This comparison uses the strict-tube theorem for xi>0. At xi=0,
the present small-a/N trace bounds and scalar sums give rate zero;
the selected boundary value there follows by continuity, without
invoking the earlier fixed-positive-color packet at zero color.

It supplies one piece of the original boundary source, not its
global cycle coefficient or the full complementary-color gap.

Focused audit: [original numerator and determinant checks](../experiments/audit_actual_q_hahn_negative_clock_boundary.py),
with [saved results](../experiments/actual_q_hahn_negative_clock_boundary_results.json).
At 90-digit precision it compares 48 literal source numerators, 30
independent dense determinants and 48 large-partner identities. It
checks 36 retained trace corrections against the proved remainder
bound, six independent dense trace calculations and 42 positive
Schur-tail inequalities. The 36 leading-rate diagnostics supplement
the written proof; they are not its justification.

The conclusion concerns the root numerator. It does not establish generic-$q$ normal data or a global period.

The selected boundary calculation retains the original half offsets and the positive branch specified above.