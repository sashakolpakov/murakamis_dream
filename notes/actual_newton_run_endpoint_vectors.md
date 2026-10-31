# Finite Gaussian boundary data for arbitrary repeated twist/turn runs

29 October 2026. For every fixed integer m, the actual source of
(T_2 P_rev)^m has explicit first AND last fixed-rank endpoint vectors.
They reduce to original signed-twist sources with fixed Newton
insertions. Each such source has a finite algebraic Gaussian leading
coefficient, so testing a candidate recurrence's boundary projection
does not require an unknown knot invariant or an unspecified solution.
No interior branch-survival theorem for all m is asserted.

## 1. Universal exact source endpoint identities

Use the full original Newton algebra/metric, Bhat_h=B_h/s_h^2,
T=T_1,P=P_rev,R=kappa r. The actual Cartan identities give

    kappa^2(-q)^d=1,
    theta=kappa^3(-q)^d=kappa.

Thus the [coherent modular reduction](actual_newton_coherent_turn_reduction.md)
simplifies, for every integer m, to

    v_m:=(T^2P)^m1=kappa^m T P T^(1-m)1.                 (1)

For a polynomial f, its Newton endpoint coefficient satisfies
alpha_(d-j)(f)=phi(f Bhat_j). Lower triangularity of T therefore gives

    (v_m)_h=kappa^m sum_(j=0)^h
                  T_(h,j) phi(R^(1-m) Bhat_j).            (2)

There is an equally explicit right endpoint formula. Define

    E_h=sum_(r=0)^h nu_h^(-1)nu_(h-r)(-q)^(-(h-r))
                                     [h choose r]_Q Bhat_r.

Then, on the FULL algebra and with every confluent normal retained,

    mathscrR(R Bhat_h)=R^(-1)E_h,
    (v_m)_(d-h)=kappa^m phi(R^(-m)E_h).                  (3)

Proof. TPT=kappa PT^(-1)P implies
PT=kappa T^(-1)PT^(-1)P. Apply this to e_h. The middle vector
PT^(-1)e_(d-h) is supported on indices0,...,h. The actual reflected
inverse kernel gives

    kappa (T^(-1))_(d-r,d-h)
       =nu_h^(-1)nu_(h-r)(-q)^(-(h-r))[h choose r]_Q.

This proves (3)'s first equality. The Frobenius identity
phi(mathscrR(f)g)=phi(f mathscrR(g)) then proves its second.
It is a full operator/source calculation, not a claim about eigenlines.

In particular

    (v_m)_0=kappa^(m+1)phi(R^(1-m)),
    (v_m)_d=kappa^m phi(R^(-m)).                          (4)

For fixed endpoint rank h, all sums in(2)--(3) have at most h+1
terms, with explicit coefficients. There is no inverse Clebsch minor.

## 2. Fixed endpoint insertions still have a finite Gaussian certificate

Keep a(s)=(1-2s)sin(2pi s), epsilon=k mod2, and
s_l=(2l-epsilon)/(2k), as in
[the actual twist endpoint theorem](actual_twist_endpoint_gaussian_certificate.md).
For every FIXED k>0 and FIXED h>=0, set

    G_(k,h)(N)=sum_(0<s_l<1)(-1)^l a(s_l)sin(pi s_l)^(2h)
                         exp[-i pi N(l-epsilon/2)^2/k].    (5)

This is algebraic and periodic in N modulo8k. With C_(N,k) exactly
the phase in that theorem, the original source obeys

    phi(r^k Bhat_h)
       = C_(N,k) N^(3/2+2h)/(pi^(2h)(h!)^2) G_(k,h)(N)
                                              +O_(k,h)(N^(1+2h)). (6)

For odd k the error is O_(k,h)(N^(1/2+2h)). Negative k follows
by coefficient conjugation. The statements concern fixed h<N as
N tends to infinity; h may not be sent to a fraction of N here.

An own proof retains the full source derivative. Its exact folded form is

    phi(r^k Bhat_h)=(-1)^(d+1)/2 sum_j nu_j^k {
       Bhat_h(c_j)[c_j-(k/2)(d-2j)A_j]+A_j^2 Bhat_h'(c_j)}. (7)

Uniformly with all fixed-order s derivatives,

    Bhat_h(2cos(2pi s))
      =N^(2h)sin(pi s)^(2h)/(pi^(2h)(h!)^2)+O_h(N^(2h-2)).

This follows directly from its h factors and
s_h^2=(2pi/N)^(2h)(h!)^2[1+O_h(N^(-2))]. Insert this into(7)
and apply the proved half-grid Gaussian argument to the leading a(s)
term. The remaining source terms have no extra N factor and are
O(N^(1/2+2h)), except the possible even-k endpoint contributions
already bounded by O(N^(1+2h)). This proves (6), including normals.

For each specified k,h, nonvanishing of(5) is a FINITE cyclotomic
test; a zero leading coefficient is not silently discarded. For k3,

    G_(3,h)=4^(-h)G_(3,0),

and for k4,

    G_(4,h)=2^(-h)G_(4,0).

Both are nonzero on every N residue class. For k5 the two paired
weights are

    a_1 sin(pi/10)^(2h), a_2 sin(3pi/10)^(2h).

At h0 the first is larger; at every integer h>=1 the second is
larger: a_2/a_1=cos(pi/5)>1/2 and
sin(3pi/10)/sin(pi/10)=(3+sqrt5)/2>2. Their strict difference gives a uniform triangle lower bound
exactly as in the scalar theorem. Thus fixed endpoint insertions for
powers3,4,5 all have nonzero leading terms, with no parity restriction.

The exceptional powers have exact fixed-root boundary data instead:

    phi(Bhat_h)=delta_(h,d),
    phi(r Bhat_h)=(-q)^(d-h),
    phi(r^2 Bhat_h)=(-q)^(d-h)F_(d-h).                   (8)

Negative powers are their conjugates. These follow from the literal
r and r^2 source columns and the full Frobenius pairing. Thus the
vanishing leading Gaussians at k0,1,2 leave no unknown endpoint data.

## 3. Every fixed twist power has nonzero resolved Gaussian boundary modes

There is a stronger UNIVERSAL vector statement even when the scalar
Gaussian sum cancels. Fix any k>=3, put epsilon=k mod2 and
rho=floor((k-1)/2), and define

    s_j=(2j-epsilon)/(2k), t_j=sin(pi s_j)^2,
                      1<=j<=rho, 0<t_1<...<t_rho<1,
    w_j(N)=2(-1)^j(1-2s_j)sin(2pi s_j)
                       exp[-i pi N(j-epsilon/2)^2/k].    (9)

Then, for EVERY integer N,

    G_(k,h)(N)=sum_(j=1)^rho t_j^h w_j(N).               (10)

To prove it, pair the stationary index j with k+epsilon-j. Their
positions are s and1-s, their a values and sin(pi s)^(2h) agree,
and their (-1) signs agree. Their quadratic phase difference is
pi N(k+epsilon-2j), an even integer multiple of pi. The remaining
middle position s=1/2 has a=0. Thus every pair adds, proving(10).
Moreover

    |w_j(N)|=2(1-2s_j)sin(2pi s_j)>0                    (11)

independently of N or any coprimality condition.

Let V_(h,j)=t_j^h, 0<=h<rho. This fixed Vandermonde is invertible:
its determinant is product_(i<j)(t_j-t_i)!=0. Form from the ACTUAL
source entries the normalized vector

    b_(h,N)=pi^(2h)(h!)^2
        phi(r^k Bhat_h)/(C_(N,k)N^(3/2+2h)).

Equation(6) is uniform over this fixed finite vector. Consequently

    V^(-1)b_N=(w_j(N))_j+O_k(N^(-1/2)),                 (12)

with O_k(1/N) error for odd k. Every individual resolved coefficient
therefore has a uniform positive lower bound for all sufficiently
large N. Negative powers give its conjugate statement.

One may use an EXACT algebraic normalization at every root instead:

    btilde_(h,N)=s_h^2 phi(r^k Bhat_h)
                                 /(4^h C_(N,k)N^(3/2)). (12a)

Since s_h^2/4^h=pi^(2h)(h!)^2 N^(-2h)[1+O_h(N^(-2))],
the same conclusion(12) holds with btilde. All its finite-level
normalizing factors, and the Vandermonde entries, are algebraic.

The normalizations and V inverse are explicit, depend on k, and have
only polynomial cost in N. They do not use an unknown knot invariant.
Thus scalar residue-class cancellations do NOT leave unknown source
incidence if one retains the full fixed-rank endpoint vector. These
are resolved GAUSSIAN endpoint modes. Identifying them with a chosen
interior Ward branch requires the exact boundary-to-Ward projection
and a propagation estimate on the domain in question. Neither follows
from the names or from nonzero individual entries; a finite endpoint
projection alone does not control subsequent mode conversion.

## 4. What this gives a finite-depth source criterion

For any fixed m and any proposed finite-rank Ward recurrence for v_m,
(2)--(7) specify its endpoint vectors by finitely many exact Gaussians
and known N powers/phases. A dominant-eigenprojection test can therefore
be made against actual source data. It must retain a possible linear
combination/cancellation between those finite coefficients; nonzero
individual entries do not imply a nonzero projection.

The repeated run is modularly PARABOLIC and conjugate to one twist.
Its unbounded count of displayed turns is not a new general bridge
family. The reusable result here is the actual finite boundary-data
formula; it is not counted as completion of the broad source problem.

The next m4 vector and its exact rank-three inhomogeneous Ward are
already displayed in the endpoint theorem. Its forward source has an
interior modulus switch; distinct roots alone cannot select one branch.
The data here remove an unknown boundary value from that problem,
rather than asserting that the remaining conversion or global source
gap has been solved.

All statements are ROOT-VALUE identities in the actual original source.
Bhat insertions encode endpoint coordinates and full Casimir Hermite
normals. They are not Taylor derivatives in q of an arbitrary generic
turn family. No recorded Newton clock is promoted to a peripheral
deformation or an additional actual knot coupon without its own proof.

Audit: [full original endpoint matrices and finite Gaussian data](../experiments/audit_actual_twist_endpoint_gaussian_certificate.py).
Its modal-residue checks use exact primitive cyclotomic-root images
in finite fields, with the prime and image recorded in the results.
They supplement the all-k pairing/Vandermonde proof above; a successful
specialization is not itself a proof of an identity over the complex
cyclotomic field.

The finite audit checks original source families, coefficient identities, Gaussian profiles and cyclotomic modal residue vectors. These checks supplement the universal pairing proof; they do not extrapolate it from the tested twist powers.