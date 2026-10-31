# The full real native cost throughout every shrinking fold window

30 October 2026. Let j_N/N tend to 1/2,
with 0<=j_N<=floor((N-1)/2). The FULL physical completed projector
and, when paired, its actual nilpotent have exponential norm rate
5v3/pi. No restriction such as (N-1-2j_N)log N=o(N) is needed here.

This concerns real integer physical degrees and magnetic indices,
their Euclidean operator norms, and fixed generic-q jets. It does
not extend the complex-normal corridor, supply a confluent complex
amplitude, or estimate a marked whole-network contraction.

## 1. Statement and the exact source interfaces

Put d=N-1, j=j_N, l=d-j and s=l-j. If j<l, let Q_j and M_j be
the ACTUAL completed target pair in the
[native projector theorem](actual_matching_edge_native_projector_energy.md).
If j=l, retain the ordinary isolated midpoint projector Pi_j.
Then, for every sequence j/N->1/2,

    N^-1 log ||Q_j||op ->5v3/pi,
    N^-1 log ||M_j||op ->5v3/pi                       (1)

on its paired subsequence, and the same limit holds for Pi_j on
its simple subsequence. All statements remain true for the
Hilbert--Schmidt norm. Every FIXED generic-q jet of these operators
has upper exponential rate at most 5v3/pi; equality is not asserted
for a derivative that can vanish.

We prove the paired claim; the isolated midpoint is already covered
by the [full folded profile](actual_matching_edge_magnetic_energy_profile.md).
Here s/N->0, while s itself can tend to infinity at any sublinear
rate. All original physical degrees are retained.

For complete degrees l<=t<=d, the exact Parseval comparison is

    N/(j+1) Z_(t,j) <= E_(t,j) <=N Z_(t,j),
    Z_(t,j)=|fhat_j(t/2)|^2/|sigma_(t,j)|.            (2)

The exact center source and double CD measure give

    Z_(t,j)=A_(N,t,j) R_j(1;c_t)^2,
    A_(N,t,j)=a_j^2/N *s_(2j)^2/s_j^4
                             *s_(t-j)/s_(t-l),
    c_t=-cos(pi(t+1)/N), a_j=|1-q^(4j+2)|.          (3)

All factorial indices lie in 0,...,d. The monic determinant R_j
is the original source determinant, not an auxiliary positive
replacement. It is increasing at z=1 for real c>=0. In (3),
c_t ranges from cos(pi j/N) to 1, so this monotonicity applies.

Let J(x)=integral_0^x log(2sin(pi y))dy on [0,1]. Its continuity,
J(0)=J(1/2)=J(1)=0, and the uniform factorial estimate give

    sup_(l<=t<=d) |N^-1 log A_(N,t,j)| ->0.          (4)

Indeed the factorial part divided by N is

    2J(2j/N)-4J(j/N)
          +J((t-j)/N)-J((t-l)/N)+O(log N/N).

The first two terms tend to zero. The last two arguments differ
by s/N->0, uniformly over t, so their difference tends to zero
by uniform continuity. The remaining a_j and N factors have
logarithms O(log N), since a_j>=4/N at a nonself-paired node.
Thus (2)--(4), at the endpoint and throughout the complete range,
prove

    max_(l<=t<=d) E_(t,j)=R_j(1;1)^2 exp(o(N)).       (5)

This is a maximum over one genuine physical degree. It does not
maximize independently over degrees of adjacent network coupons.

## 2. The actual endpoint selects the same cubic limit

Put u=floor(d/2), v=d-u and w_N=q^j. At t=d the positive coefficient
polynomial appearing in the original physical column is

    P_N(w)=sum_(a=0)^j beta(j,a)beta(u,a)beta(v,j-a) w^a,
    C_j(d,u)=q^((d-j)u) P_N(w_N).                    (6)

The denominator beta(d,j) is exactly one. The finite negative-root
theorem applies to this original polynomial. Uniform factorial
estimates and j/N,u/N,v/N->1/2 give uniformly over the whole support

    N^-1 log[beta(j,a)beta(u,a)beta(v,j-a)]
      =-3[J(a/N)+J(1/2-a/N)]+o(1).                 (7)

Replacing j/N by 1/2 uses only uniform continuity of J, including
both endpoints. There is no assumed bound on s log N here.

For every positive real w, (7) gives the same strict real Laplace
action as in the full folded theorem. Its selected saddle is
alpha(w)=pi^-1 arctan(w^(1/3)). The actual negative-root product
bound makes N^-1 Log(P_N(w)/P_N(1)) a normal family on the slit
plane. Uniqueness from the positive real axis therefore gives
the same holomorphic action for this whole sequence of actual
polynomials. In particular at w_N->i,

    N^-1 log |C_j(d,u)| ->5v3/(2pi).                (8)

This is the selected complex rate, not a conclusion from comparing
positive coefficients at w=i. The exact constant was computed from
alpha(i)=1/4+i log(3)/(4pi) and D(i/sqrt(3))=5v3/6 in the preceding
theorem.

At degree d the magnetic polynomial has all j roots negative real.
If u differs from d/2 by one half, its root-product formula gives

    cos(pi/(2N))^j <= |C_j(d,u)|/|fhat_j(d/2)| <=1;  (9)

if d is even the ratio is one. Finally the exact center scalar is

    |fhat_j(d/2)|=R_j(1;1) s_(2j)/s_j^3.           (10)

Its normalized logarithm tends to zero, since J(2j/N)-3J(j/N)->0.
Equations (8)--(10) prove

    N^-1 log R_j(1;1)^2 ->5v3/pi.                  (11)

## 3. The incomplete band is smaller, using its own actual formula

It remains to control j<=t<l, where the completed pair contains
only its simple physical branch. The complete-range Fourier
factorization is NOT assumed in this band. Instead start with the
original generic finite column. Its highest-vector factor at the
root is exactly

    F_(N-j+a-1) F_(N-a-1)/(F_(N-j-1)F_(N-1))
                           =Q^(a(a-j)) [j choose a]_Q.            (12)

This follows by complementing each factor
1-Q^(N-r)=-Q^(-r)(1-Q^r). Every denominator index is below N;
(12) is valid for ALL 0<=j<=t< N, not just complete channels.
Since [n choose k]_Q=q^(k(n-k)) beta(n,k), substitution into
the original divided-descendant sum gives the exact identity

    C_j(t,u)=q^((d-j)u) sum_a E(t,j,u,a) q^(a(t+j-d)),
    E=beta(j,a)beta(u,a)beta(t-u,j-a)/beta(t,j),
    max(0,u-t+j)<=a<=min(j,u).                      (13)

To check its phase directly, the Gaussian-binomial phases,
divided-descendant powers and root highest ratio leave
a(t+j-1)-ju before the factor
(-1)^a x^(-2a). Combining that factor with x^u and q^N=-1 gives
precisely (13). Thus its real positive envelope is an authorized
bound for this ACTUAL root source outside the complete chamber.

Set r=t-j<s=o(N). Every allowed a satisfies 0<=u-a<=r. Uniform
factorial estimates, j/N,t/N->1/2, and that inequality imply

    N^-1 log E(t,j,u,a)
       =-J(x)-J(1/2-x)+o(1),                       (14)

uniformly throughout the incomplete band and its full support.
Here x can be chosen as min(u/N,1/2). The possible excess of u/N
above 1/2 is o(1), so this harmless clipping and all arguments
of J are justified by its uniform continuity. In detail the
beta(j,a) term supplies the displayed profile, while beta(u,a),
beta(t-u,j-a), and the denominator beta(t,j) each have normalized
logarithm tending uniformly to zero because their complementary
indices are at most r.

There are at most N summands in (13). A triangle bound therefore
gives the uniform upper estimate from (14). This step is used only
in the collapsing boundary band and claims no selected oscillatory
rate for an interior column. The simple CD measure there is

    |sigma_(t,j)|=s_(t-j)s_(t+j+1)/(s_t^2 a_j).

Its normalized logarithm tends uniformly to zero: its three
factorial arguments tend respectively to 0,1,1/2. Summing the
squared column bound over at most N magnetic indices yields

    max_(j<=t<l) E_(t,j)
       <=exp[N(v8/(2pi)+o(1))].                    (15)

The smaller constant comes from the strict maximum at x=1/4 of
-2J(x)-2J(1/2-x). This estimate retains endpoints and all source
phases until the explicitly stated upper-bound step.

## 4. Assemble the real operator and retain the scope

The exact generic high adapter duplicates the same physical low
blocks. On each complete block M_j has norm E_(t,j); it is zero
on the incomplete band. Hence (5),(11) give its full operator
and Hilbert--Schmidt rate in (1). On a complete block
M_j=(J_t-c_j)Q_j, with uniformly bounded J_t-c_j, providing the
matching lower bound for Q_j. The native projector theorem gives
its upper bound by a polynomial times the maximum or square sum
of ALL energies. Equations (11),(15), and v8/(2pi)<5v3/pi prove
the other claim in (1). Fixed generic-q derivatives add only the
uniform polynomial factors already proved there.

Thus every shrinking SCALED fold window has the same explicit
real boundary cost, even when s log N is not o(N). The stronger
width here comes from positivity and real physical norms, not
from a larger joint complex domain for paired normal currents.
No fixed nonzero scaled-width assertion or whole-source volume
conjecture follows from this corollary.

Audit: [original incomplete-band formula and shrinking-fold source](../experiments/audit_actual_matching_edge_shrinking_fold_native_energy.py).

The indices remain real and physical. This result does not enlarge the complex-normal corridor or assert a whole-source limit.

The continuity, root-product and operator arguments prove the shrinking real-window bounds. Finite samples check their conventions, not their uniformity.