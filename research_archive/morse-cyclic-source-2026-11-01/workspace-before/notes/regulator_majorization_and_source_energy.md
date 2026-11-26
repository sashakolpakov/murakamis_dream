# Majorization, exact regulator conservation, and pointed energy

28 October 2026. Majorization gives a sharp general product inequality,
but by itself it pays the pointwise singular-value envelope. There is a
stronger, useful strict-convexity statement: a bistochastic mixing map
which fixes the regulator observable can mix only equal-regulator
channels. That property makes the exponential action weights telescope
and gives an endpoint bound for the original source energy. The actual
quantum connection has not been proved to possess this property.

## 1. The general log-majorization inequality

For invertible d by d matrices A_j let s_1>=...>=s_d be their singular
values and P=A_(m-1)...A_0. For every 1<=r<=d,

    sum_(i<=r)log s_i(P)
       <=sum_j sum_(i<=r)log s_i(A_j).             (1)

Indeed the product of the top r singular values is the operator norm
of the r-th exterior power. Apply the elementary product-norm bound
there. At r=d equality holds, by multiplicativity of the determinant.
Thus log s(P) is majorized by the decreasing vector with entries
sum_j log s_i(A_j).

For completeness, the convex-function implication needs no imported
inequality. The partial-sum inequalities imply

    sum_i (u_i-t)_+ <=sum_i (v_i-t)_+

for every t, because each side is the maximum over r of its top-r
sum minus rt. Every convex piecewise linear function is a linear
function plus a positive combination of these hinge functions.
Approximation proves sum f(u_i)<=sum f(v_i) for every convex f.
Taking f(t)=exp(pt), p>0, yields the corresponding Schatten bound.

This is sharp with only the individual singular spectra specified:
positive diagonal matrices whose decreasing singular directions are
aligned attain equality. It cannot be generally improved by changing
the convex function.

On a regular slowly varying recurrence with a tame supplied
instantaneous eigenbasis, the transformed steps are
diag(lambda_i(x_j))+O(1/N). For eigenvalues bounded away from zero,
their singular logarithms are the decreasing log|lambda_i|+O(1/N).
Consequently (1) yields the integral of the POINTWISE sorted root
moduli. It does not yield the maximum complete marked-branch action.
For r=1 this is the safe classical spectral envelope already proved
for the actual source. All exterior-power refinements retain the
same limitation at r=1.

The actual source costs are not part of a singular-spectrum list:

    |ell^*P s|<=||ell|| ||s|| s_1(P).

In the actual macroscopic theorem, s is the entire ordinary-color
packet on the denominator-avoiding complex circle and has proved
polynomial norm. That fact makes (1) an original-source upper bound;
it does not supply a new branch-selection inequality.

## 2. Strict convexity gives a stronger exact rigidity

Let C be a nonnegative doubly stochastic matrix and r a real vector.
One has the EXACT variance identity

    sum_(i,k) C_(ik)(r_i-r_k)^2
                      =2 r dot (r-Cr).            (2)

The two quadratic terms on expansion use the row and column sums.
In particular, if Cr=r, every term on the left vanishes:

    C_(ik)>0 => r_i=r_k.                           (3)

This is also the equality case of strict convexity of t^2 under
doubly stochastic averaging. Merely preserving the TOTAL mean of r
does not give (3); every doubly stochastic matrix preserves that mean.

There is a noncommutative version directly suited to an energy.
Let Phi(X)=sum_a K_a X K_a^* be a bistochastic Kraus channel:

    sum_a K_a^*K_a=I, sum_a K_aK_a^*=I.

For a Hermitian regulator observable R,

    sum_a ||R K_a-K_a R||_HS^2
            =2 Tr[R(R-Phi(R))]
            =2 Tr[R(R-Phi^*(R))].                 (4)

Expansion proves this identity: the two square terms each give
Tr R^2, and the cross term is Tr[R Phi(R)]. Thus if either the
Schroedinger or Heisenberg channel fixes R, EVERY Kraus operator
commutes with R and with exp(tR). In an eigenbasis of R, all mixing
is inside equal-regulator blocks. This is substantially stronger
than conservation of one scalar mean in one selected state.

For reference, a bistochastic channel also majorizes the eigenvalues
of every positive input. For a rank-r projection Q,
Tr[Q Phi(rho)]=Tr[Phi^*(Q)rho], where 0<=Phi^*(Q)<=I and
Tr Phi^*(Q)=r. Diagonalizing rho bounds this trace by the sum of its
top r eigenvalues; maximize over Q. This proves the usual convex
energy inequalities directly. The NEW information required for (3)
or (4) is the fixed regulator observable, not bistochasticity alone.

## 3. Exact telescoping with the original source retained

Here is a concrete sufficient condition for endpoint control. It is
an algebraic transport theorem, not a claim about an unverified knot
connection. Let r_j be specified real diagonal action vectors and

    G_j=diag(exp(N r_(i,j))).

Suppose the diagonal propagation is

    D_j=G_(j+1) A_j G_j^(-1),
    A_j diagonal, ||A_j||<=exp(epsilon_j),
    sum_j epsilon_j=o(N).                         (5)

Unitary diagonal phases may be included in A_j. Suppose the ACTUAL
energy evolution is

    rho_(j+1)=D_j Phi_j(rho_j)D_j^*,              (6)

where Phi_j is bistochastic and fixes diag(r_j) as in (4). These are
conditions on specified local connection maps; no unknown terminal
product or Kashaev value enters their definition. They imply

    Tr[G_m^(-1)rho_m G_m^(-1)]
       <=exp(2sum_j epsilon_j)
                        Tr[G_0^(-1)rho_0 G_0^(-1)].             (7)

Proof. By (4) each K_(a,j) commutes with G_j. Write
rhohat_j=G_j^(-1)rho_j G_j^(-1). Then EXACTLY

    rhohat_(j+1)=A_j Phi_j(rhohat_j) A_j^*.

Take the trace, use positivity and trace preservation, and iterate.
This is the desired partial-sum telescoping: all intermediate action
potentials cancel, including at equal-regulator mixing events.

For a genuine amplitude recurrence the special case is one UNITARY
Kraus operator U_j. If [U_j,diag(r_j)]=0 and A_j=I, the whole
product is exactly

    P=G_m (U_(m-1)...U_0)G_0^(-1).                (8)

If the zero anchor gives G_0=I, the singular values of P are EXACTLY
the endpoint exp(N r_(i,m)), up to ordering. Thus every top-r
log-majorization bound telescopes to an endpoint sum, not an
integral of separately sorted local increments.

For the original pure input rho_0=s s^* and output ell, (7) gives

    ell^*rho_m ell <=exp(2sum epsilon_j)
           ||G_m ell||^2 ||G_0^(-1)s||^2.         (9)

When the actual evolution is coherent, rho_m=P s s^*P^*, its left
side is exactly |ell^*P s|^2. No replacement of that evolution by an
artificial mixture is implicit in (9).

The general positive-output energy has the same bound with its
specified output Gram matrix in place of ell ell^*. All actual
external factors and original source normalizations remain outside
this estimate unchanged. In particular a zero regulator anchor,
polynomial original source and co-source norms, and
r_(i,m)<=Vol(K)/(2pi) give the sharp desired UPPER rate. No nonzero
overlap or lower rate follows.

Introducing an artificial dephasing or a Kraus average does NOT
establish premise (6). For the original coherent scalar one must
prove its amplitude evolution or its exact selected Plancherel
energy has that positive channel representation. Nor does regulator
invariance under finite character-cover monodromy over a FIXED normalized
peripheral point, or equality at a ramification point, imply invariance
under the quantum connection. A meridian loop which
ends on a different longitude sheet can have a different regulator.

A bounded number of subexponentially bounded connection matrices
supported only in equal-action blocks also suffices in (8), with
a subexponential norm factor; more generally their summed logarithmic
norm cost must be o(N). They need not be unitary. Genuine
representation ramification supplies equality of the calibrated
values on a colliding block. Proving that the actual quantum
connection has only those blocks, with that bound, remains the
analytic/source requirement.

## 4. Approximate conservation needs the right accuracy

Formula (4) gives a quantitative diagnostic. If
||Phi^*(R)-R||_HS<=eta and ||R||_HS<=B, then

    sum_a ||[R,K_a]||_HS^2<=2B eta.               (10)

Across a pair of regulator eigenvalues separated by g, the total
squared Kraus mass is at most 2B eta/g^2. Hence polynomial
approximate conservation gives only polynomial off-block suppression.
After conjugation by exp(NR), a transition from r_k to r_i carries
exp[N(r_k-r_i)]. A polynomial error need not survive that factor.
For example a bound from (10) alone would need eta exponentially
smaller than exp[-2N(r_k-r_i)] for an upward weighted transition.
The fixed point property or an actual action barrier is essential.

The independently proved Gaussian model makes this quantitative:
its off-diagonal coupling can be 1/N, its complete marked branch
actions are zero, but its selected growth is
a/4-theta^2/(4a)>0. Discarding coherent phases costs still more.
If W_N(theta)=b_N sum_(k=0)^(N-1)
exp[a k(N-k)/N+i k theta], exact finite Fourier orthogonality gives

    (1/N)sum_(ell=0)^(N-1)|W_N(2pi ell/N)|^2
       =b_N^2 sum_(k=0)^(N-1)exp[2a k(N-k)/N].   (11)

The square-root energy rate is a/4, exactly the scalar envelope,
whereas fixed theta in (0,min(a,pi)) has the smaller coherent rate.
Thus a positive phase-averaged energy can destroy the conversion
penalty that one is trying to use. Equation (11) is a phase-variable
example, NOT the actual root-color Plancherel energy: that actual
identity retains its special ordinary-color polynomial remainder.

## 5. The knot-specific test suggested by majorization

The useful test is stronger than convex ordering of root moduli:
construct the ACTUAL connection on a calibrated representation
packet and prove that its positive energy map is bistochastic and
fixes the regulator observable, or prove directly that its entries
are confined to equal-calibrated-action blocks with subexponential
cost. The exact rigidity (2)--(4) then supplies the missing
no-upward-action mixing statement and the source estimate (7)--(9).

The [complex representation-path theorem](complex_peripheral_action_and_conversion_bound.md)
already supplies calibrated equality at genuine normalized
ramification and an absolute endpoint volume bound. The
[two-bridge midpoint theorem](two_bridge_midpoint_regulator_anchor.md)
supplies the zero anchor on every genuine component of that class.
The finite quantum connection, its possible nodal jumps, and its
exact selected energy are still to be identified and bounded.
General log-majorization or Karamata does not manufacture those
facts from eigenvalues alone.

[Audit](../experiments/audit_regulator_majorization.py): exterior-power
partial sums, the bistochastic variance identity, regulator-fixed
quantum channels, exact pointed action telescoping, and the finite
Gaussian phase-Plancherel distinction.

Coverage only: product log-majorization is established matrix theory;
see [Gowda, Some log and weak majorization inequalities](https://userpages.umbc.edu/~gowda/papers/trGOW20-02.pdf).
The exterior-power, convexity, channel and source calculations used
here are proved above independently.
