# Analytic transport through a regular modulus crossing

28 October 2026. This gives a local marked-action upper bound for a
holomorphic recurrence at a modulus crossing where its eigenvalues are
DISTINCT and nonzero. The proof constructs an exponentially accurate
diagonal form by elementary matrix identities and Cauchy estimates.
It needs no exact solution, source overlap, formal WKB summation theorem
or pointwise dominance assumption.

The sufficient condition compares a COMPUTABLE analytic remainder
barrier with the width of the marked classical actions. It always holds
on a sufficiently short regular crossing window. Extending it over a
whole knot orbit still requires a global action-barrier comparison;
mere single-valued calibration of an action does not prove that.
Actual real ramification and singular leading coefficients are outside
this local theorem.

## 1. Explicit analytic data

Write epsilon=1/N and x_(j+1)=x_j+epsilon on a fixed real interval I.
Let U_R denote its complex stadium of radius R. Suppose T_N and T_0
are holomorphic on U_(2R), uniformly bounded, and

    ||T_N-T_0||_(U_(2R))<=C_0 epsilon.             (1)

Assume T_0 has a supplied holomorphic eigenbasis V_0 there:

    V_0^(-1)T_0V_0=D_0=diag(lambda_1,...,lambda_d),
    ||V_0||,||V_0^(-1)||<=K,
    |lambda_i|>=m>0, |lambda_i-lambda_k|>=delta>0. (2)

These are bounds on specified coefficient functions. For a classical
companion, V_0 has columns (1,lambda_i,...,lambda_i^(d-1))^t, so all
data are directly checkable on its normalized spectral branches.
An actual recurrence as in
[the whole-source spectral theorem](actual_macroscopic_a_spectral_upper_bound.md)
satisfies (1) on any such regular fixed domain, uniformly on its small
complex-q source circle. An unverified classical polynomial alone
does not supply that actual quantum premise.

After the exact change by V_0, put

    B_N(z)=V_0(z+epsilon)^(-1)T_N(z)V_0(z).

Cauchy's estimate gives B_N=D_0+O(epsilon) on U_R. Initially set
D=diag B_N, R_N=B_N-D. The diagonal gap is at least 3delta/4 for
large N and ||R_N||<=C epsilon. All constants below are uniform.

## 2. Exponentially accurate diagonalization, with its proof

There are explicitly bounded constants sigma>0,C and holomorphic
V_N,D_N,R_N on U_(R/2), with D_N diagonal, such that EXACTLY

    V_N(z+epsilon)^(-1)T_N(z)V_N(z)=D_N(z)+R_N(z),
    ||V_N-V_0||+||V_N^(-1)-V_0^(-1)||<=C epsilon,
    ||D_N-D_0||<=C epsilon, ||R_N||<=C exp(-sigma N). (3)

The shifted identity is asserted where both z and z+epsilon belong
to that neighborhood; this includes every real step across I. The
one-dimensional case has no off-diagonal part and is immediate.

Here is a constructive proof with quantitative constants. Maintain
||D||<=M and diagonal gap g=delta/2; take M larger than twice the
initial diagonal bound. If R is off diagonal with norm eta, solve

    [D,X]=-R, diag X=0,
    X_(ik)=-R_(ik)/(D_(ii)-D_(kk)), ||X||<=a eta,
    a=d/g.

On a stadium narrowed by Delta>=2epsilon, Cauchy gives
||X(z+epsilon)-X(z)||<=2a eta epsilon/Delta. With X^+=X(z+epsilon),

    (I+X^+)^(-1)(D+R)(I+X)=D+F,
    F=(I+X^+)^(-1)[(X-X^+)D+R X].                (4)

This is an exact identity. If a eta<=1/2, its new off-diagonal norm
is bounded by

    eta_new <=[8Ma epsilon/Delta+4a eta] eta.      (5)

Its diagonal change is O(eta^2). To see the latter without losing a
derivative, (X-X^+)D is off diagonal. Its contribution to diag F
therefore requires the extra factor (I+X^+)^(-1)-I=O(eta).
The other term RX already has size O(eta^2).

Choose a fixed

    c<=min(R/8,R/(128Ma)), p=floor(cN),
    Delta=R/(2p).

For sufficiently large N the starting eta is at most 1/(32a).
Equation (5) then decreases eta at least by a factor 1/2 at EVERY
step. The accumulated diagonal change is O(sum eta^2)=O(epsilon^2),
so the stated bound M and gap g persist. The p domain losses total
R/2 and Delta>=4epsilon, so all exact shifts are legitimate.

The basis is the product of I+X at each step. Since
sum ||X||<=2a eta_0=O(epsilon), it and its inverse are I+O(epsilon).
The final off-diagonal is O(epsilon*2^(-p)). For example one may use

    sigma=(c log 2)/2.                            (6)

All bounds are derived from (1)--(2), not an unknown solution.
They are conservative, not optimal conversion exponents. The same
construction is holomorphic in additional parameters wherever those
uniform premises hold, including the actual tiny complex-q circle.

## 3. A checkable action-width criterion

Normalize the real marked actions at the left endpoint a of I:

    A_i(x)=integral_a^x log|lambda_i(t)| dt,
    W=max_(x in I)[max_i A_i(x)-min_i A_i(x)].      (7)

Suppose W<sigma. Then the EXACT product P_N of T_N across I satisfies

    limsup (1/N)log||P_N||<=max_i A_i(b),           (8)

where b is its right endpoint. Every specified input and output with
subexponential norms has the same upper bound. This is a product bound,
not merely a prediction from formal critical points.

Proof. Let d_(i,j) be the diagonal entries of the actual D_N(x_j),
and put G_0=I, G_(j+1)=D_N(x_j)G_j, all diagonal. Uniformly in j,

    log |(G_j)_(ii)|=N A_i(x_j)+O(1),              (9)

by (3), nonvanishing in (2), and the ordinary uniform Riemann estimate.
The remaining EXACT recurrence after G_j has factors

    I+E_j, E_j=G_(j+1)^(-1)R_N(x_j)G_j.

Equations (3), (7), and (9) give
||E_j||<=C exp[-N(sigma-W)]. There are O(N) steps, so their product
is I+O(N exp[-N(sigma-W)]). Consequently

    P_N=V_N(b) G_n [I+O(N exp[-N(sigma-W)])] V_N(a)^(-1).

This proves (8) and gives an exponentially small relative matrix
remainder after the explicitly marked diagonal propagation.
The exponential anisotropy of G_j is RETAINED and estimated by W;
it is not asserted to be a tame positive full-space metric.

In fact the same proof pins down the WHOLE singular-value vector.
Let A_(1)(b)>=...>=A_(d)(b) be the sorted endpoint actions. Under
the stated barrier, bounded invertible endpoint frames and the
I+o(1) middle factor give, for every k,

    log sigma_k(P_N)=N A_(k)(b)+O(1).            (9a)

Use the elementary singular-value inequalities for multiplication
by a bounded invertible matrix on both sides of the diagonal G_n.
Thus all partial sums satisfy the corresponding asymptotic
log-majorization, and every fixed continuous convex function of
the normalized log singular values has the endpoint-action limit.
This conditional pinching is stronger than a convexity estimate.
It does not make the barrier follow from Karamata, and does not
prove a nonzero overlap for the selected scalar source.

For finite N there is a more flexible certificate: construct (3)
and the diagonal G_j, compute bounds e_j>=||G_(j+1)^(-1)R_NG_j||,
and use

    ||P_N||<=||V_N(b)|| ||V_N(a)^(-1)||
                   max_i |(G_n)_(ii)| product_j(1+e_j). (10)

Proving sum_j e_j=o(N) suffices. These quantities use only the
explicitly constructed local diagonalizers and scalar diagonal
products, not the unknown exact vector solution or its final scalar.

## 4. A distinct-root modulus crossing is locally harmless

For two branches suppose |lambda_1(x_*)|=|lambda_2(x_*)|, while
the eigenvalues themselves stay separated as in (2). On
I=[x_*-ell,x_*+ell], let

    |d/dx log|lambda_1/lambda_2||<=L.

Then |A_1(x)-A_2(x)|<=L ell^2 throughout I. Thus L ell^2<sigma
is a sufficient condition for (8), even if the larger modulus
switches at x_*. The bound applies also to distinct REAL roots
of opposite sign. No positive real weights are introduced.

The analytic data may be fixed on a neighborhood of x_* first;
sigma is then independent of the shortened ell. Hence a sufficiently
short crossing window always meets this condition. For more than
two regular branches use W<=2ell max_(i,k) sup_I|log|lambda_i/lambda_k||.

All quantities are checkable from a specified classical curve and
actual analytic recurrence. For a simple root of F(x,L),
partial_x Log lambda=-F_x/(lambda F_L), which bounds L. A calibrated
Bloch/peripheral action may supply the A_i, but (7) still requires
the explicit quantitative width comparison.

This does not contradict the
[Gaussian conversion example](analytic_two_channel_conversion_counterexample.md).
On its whole interval the conversion has positive gain even though
the complete branch actions vanish. Its global width cannot satisfy
the sufficient barrier comparison. On a sufficiently short regular
window the theorem gives precisely the local estimate (8). An
exponentially small local conversion can still grow after a long
external propagation; it cannot be discarded in later gluing.

### A verified action-coordinate radius can replace the Euclidean one

The proof also works in a supplied univalent holomorphic coordinate
w=zeta(z). Assume the transformed matrices and basis obey (1)--(2)
on an action-plane neighborhood of radius R_w, and the EXACT shifted
coordinate map f_epsilon(w)=zeta(zeta^(-1)(w)+epsilon) is holomorphic
there with

    |f_epsilon(w)-w|<=V epsilon.

In (4) set X^+=X(f_epsilon(w)). Cauchy's estimate changes (5) only
by replacing epsilon/Delta with V epsilon/Delta. Hence one may use

    c<=min(R_w/(8V),R_w/(128MaV)), sigma=c log2/2. (11)

The actual sampled recurrence and the real actions (7) are unchanged;
no continuum substitution for a discrete step is made. This follows
from a verified analytic coordinate and shift map, not a formal
replacement of the independent variable.

At a distinct-root crossing, an appropriately marked
zeta(z)=integral Log(lambda_i/lambda_k) dz has nonzero derivative
unless that MARKED logarithm vanishes. It is therefore a valid local
coordinate on a sufficiently small domain. Its analytic inverse may
be bounded by excluding its actual action-plane critical values and
singularities. This gives a CHECKABLE action-domain version of the
remainder barrier. It does not identify the optimal barrier with
the nearest calibrated collision action, or show that a zero
regulator jump implies the global width inequality. Those stronger
connection statements are still unproved.

## 5. What finite gluing additionally requires

On overlapping regular domains with the SAME marked V_0 and the
same iteration (4), two truncation depths give compatible frames:
their ratio is I+O(exp[-min(sigma_1,sigma_2)N]) on a smaller overlap.
Indeed their factors are literally the same up to the smaller
depth; every additional X is already exponentially small there.
This proves an actual overlap statement without choosing an
unspecified exact WKB solution.

It does NOT justify resetting every local action to zero and then
freely splicing its best endpoint. In global action coordinates,
each off-diagonal error and overlap correction acquires its FULL
factor exp[N(A_k-A_i)]. A sufficient finite-gluing condition is a
strict positive margin between each domain's exponential remainder
barrier and those globally calibrated action differences, including
the overlap locations. More flexibly, one may verify the weighted
finite-N certificate (10) on the full assembled blocks.

Across genuine spectral ramification V_0 and its inverse need not
be bounded, so (1)--(6) no longer apply. Equality of absolutely
calibrated regulator values at a ramification point is useful
geometric information, but does not itself prove a quantum
connection estimate. An action-coordinate refinement controlling
that connection, rather than the conservative Euclidean sigma,
remains necessary for the proposed general endpoint theorem.

Thus the proved local result is (3)--(8), including regular
modulus crossings and an explicit analytic barrier. No general
two-bridge or whole-knot geometric bound is claimed until the
actual operator, boundary source and global conversion margins
are verified. The original-source Cauchy recovery remains exactly
that of the macroscopic spectral theorem.

[Audit](../experiments/audit_actual_local_analytic_transport.py)
checks the exact iterative identity, separated-root contraction,
bounded frame and weighted product reconstruction on analytic
model matrices. These are supplementary checks, not an actual
quantum-operator or global ramification calculation.
