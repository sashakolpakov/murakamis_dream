# A positive determinant period of the actual pointed quantum A-operator

Research note, 27 October 2026. This gives an exact finite algebraic
period on the actual A-operator side for every knot. It uses any
specified nonzero all-level annihilator and finitely many fixed
small-color jets. Its value is a positive ratio of polynomial
coefficients of two matrices of fixed bandwidth. Neither the operator's
root-level kernel rank nor a separate nonvanishing source-overlap
hypothesis is required for the identity.

The original Kashaev volume conjecture becomes a precise growth
statement for this ratio, equation (6.2). That growth statement is
not proved here. Positivity of Gram coefficients is not a substitute
for estimating their ratio or relating it to the marked regulator.

## 1. The actual operator, and a fixed amount of pointing

Use the actual reduced quantum periods from
[the all-level theorem](all_level_a_period.md). A nonzero actual
all-level meridian annihilator exists by the independent
[finite-cut proof](finite_sum_annihilator.md). Fix one, clear its
denominators, and write

    A=sum_(i=0)^d a_i(q,M) T^i, T M=q M T,
    a_i in Q[q^(+/-1),M^(+/-1)], a_d!=0.                (1.1)

The same argument works over a fixed coefficient number field.
All original normalization and meridian conventions are retained.
The finite small-color pointing gives the exact generic identities

    sum_i a_i(q,-q^j) C_(j+i)(q)=0, j>=1,
    C_N(q_N)=<K>_N, q_N=exp(pi i/N).                    (1.2)

Here C_j is the reduced j-dimensional highest-weight cut, with
unknot value one. No large-color Jones asymptotic is an input.
Equation (1.2) is the repo's own polynomial-rigidity consequence
of the actual root states and quotient colors.

Remove a common power of q-1 from the coefficients first, so
A_cl(M,L)=sum_i a_i(1,M)L^i is nonzero. This changes neither
the generic annihilation nor the original root periods.
Let A_q be the q-exponent span of a_d, D its M-exponent span,
and s its number of monomials. Choose a fixed j_*>=A_q+1 and put

    B=D(s-1).                                          (1.3)

For sufficiently large N, the total order of zeros at q_N in
a_d(q,-q^j), j_*<=j<=N-d, is at most B. Briefly, its root
specialization has at most D distinct zeros on that color orbit,
and any nonzero Laurent polynomial with s monomials has vanishing
order at most s-1. The latter is the Vandermonde argument in the
all-level note. The choice j_*>A_q prevents a coefficient from
vanishing identically on one of the color trajectories.

Only the jets through order B of C_(j_*),...,C_(j_*+d-1)
will be used. This is a fixed list, independent of N.
A smaller starting color is allowed when direct factorization
verifies that a_d(q,-q^j) is not identically zero for every
subsequent j; the bound A_q+1 is a sufficient uniform choice.

## 2. A finite banded system retains every singular step

Put t=q/q_N-1, n_c=N-j_*+1 and n=(B+1)n_c. For each color
j_*<=j<=N introduce its truncated jet

    y_j(t)=sum_(r=0)^B y_(j,r)t^r mod t^(B+1).

Define the square n by n matrix M_N by these equations:

* For the first d colors, prescribe their B-jets to be the actual
  fixed-color jets at q_N.
* For j_*<=j<=N-d, impose (1.2) modulo t^(B+1), with q=q_N(1+t).

Call the right side b_N. It is supported only in the first d
color blocks; its norm is bounded as N grows. These fixed Laurent
polynomials and their bounded-order jets are analytic near q=1.
The matrix has lower block bandwidth d and block size B+1. Its
initial diagonal blocks are I; each later diagonal block is
truncated multiplication by a_d(q,-q^j). A monomial q^a M^c
on the j-th trajectory contributes

    (-1)^c q_N^(a+cj) binom(a+cj,r)                   (2.1)

to its r-th jet. Thus every entry is O(N^B) and the matrix has
fixed bandwidth and size O(N). Negative exponents in (2.1)
use the ordinary generalized binomial coefficient.

Let R_N select the constant coefficient y_(j,0) from each block.
The actual color jets give a solution of

    M_N y=b_N.                                         (2.2)

Although higher jets in a truncated solution may not be unique,
every constant color value is unique. Indeed the difference of
two solutions has zero initial jets through order B. At a step
whose leading coefficient has zero order m, division in the
Laurent-series field lowers the known valuation by at most m.
Induction gives valuation at least

    B+1-sum_(previous steps)m >=1.

The argument can be performed on arbitrary polynomial lifts:
every recurrence error is divisible by t^(B+1), so the same
valuation induction applies. Consequently

    ker M_N subset ker R_N,
    R_N y=f_N=(C_(j_*)(q_N),...,C_N(q_N))^t              (2.3)

for every solution of (2.2). No division at the singular value
itself was used.

The nullity nu_N=dim ker M_N is at most B. In fact a leading
coefficient with order m has a multiplication block of nullity m
(the total budget ensures m<=B). A lower block triangular matrix
has rank at least the sum of the ranks of its diagonal blocks:
select invertible minors of each diagonal block and combine them.
Their combined minor is lower block triangular with nonzero
determinant. Summing the block nullities proves the assertion.

An exact per-level pole budget may replace B in this construction.
The theorem uses the uniform bound so its block size is fixed.

## 3. The pointed norm is a Gram coefficient ratio

For the fixed complex embedding at q_N let dagger be the ordinary
Hermitian transpose. Write

    P=M_N^dagger M_N, g=M_N^dagger b_N, beta=b_N^dagger b_N,
    Q_N(lambda)=det(P+lambda I),
    D_N(lambda,z)=det[ P+lambda I+z R_N^dagger R_N   g;
                       g^dagger                    beta ]. (3.1)

The variables lambda,z are ordinary commuting polynomial variables.
They have no relation to a peripheral longitude. In particular,
D_N here is not the root monodromy polynomial of the norm-torsor
note. Define

    G_N(A,j_*)=[lambda^nu_N z]D_N(lambda,z)
                         /[lambda^nu_N]Q_N(lambda).     (3.2)

**Exact pointed Gram theorem.** The denominator is positive and

    G_N(A,j_*)=||f_N||^2
              =sum_(j=j_*)^N |C_j(q_N)|^2.             (3.3)

For large N its numerator is positive too: any one of the fixed
initial colors tends to the unknot value 1 at q=1. Thus (3.2)
is a well-defined positive algebraic period, even at a level where
the complete Kashaev value might vanish.

Here is a direct proof which also explains the specified coefficient.
Use an orthonormal decomposition C^n=(ker M_N)^perp plus ker M_N.
On it P=diag(P_r,0), P_r positive definite. By (2.3), R_N is zero
on the kernel. Also g has no kernel component. Hence D_N has a
factor lambda^nu_N, and its remaining block has size r+1.
Let y_0 be the minimum-norm solution of (2.2). Then

    g=P_r y_0, beta=y_0^dagger P_r y_0.

At lambda=0 the Schur complement of P_r+z R_N^dagger R_N
is zero at z=0. Its derivative there is

    y_0^dagger R_N^dagger R_N y_0=||f_N||^2.

Therefore the coefficient in the numerator is det(P_r)||f_N||^2,
whereas the denominator coefficient is det(P_r). This proves
(3.3), without any special-fiber rank-one assumption or pseudoinverse
overlap estimate.

## 4. Both polynomial coefficient families are positive

Every coefficient of Q_N(lambda) and D_N(lambda,z) is nonnegative
real. For the latter form the rectangular matrix

    Z(lambda,z)=[ M_N                 b_N;
                 sqrt(z) R_N            0;
                 sqrt(lambda) I         0 ].             (4.1)

Its Gram matrix is exactly the bordered matrix in (3.1). The
Cauchy--Binet formula writes its determinant as a sum over row
sets of squared absolute determinants. In each summand the
chosen identity and R rows contribute a definite monomial in
lambda,z. Its coefficient is nonnegative. The same proof with
the last column and the R rows omitted applies to Q_N.

This is positivity of the displayed coefficient periods. It does
not assert that the original crossing coefficients are positive,
or that every complex minor has been estimated. It removes a
separate arbitrary choice of a source overlap from the statement:
the original overlap is already contained in the pointed border.

All data in (3.1) come from the specified actual A-operator and its
fixed small-color jets. No color near N is an input. Conjugation
of cyclotomic coefficients uses q_N->q_N^(-1), including the
conjugates of the actual initial jets.

These matrices still have fixed bandwidth. The matrix P has
bounded block bandwidth, and g is supported in the initial blocks:
because b_N is supported on the identity initial equations,
M_N^dagger b_N is just that same padded initial vector. Placing
the last row and column first keeps a bandwidth bounded in terms
of d and B, independently of N. The size is O(N), the nullity
is bounded, and all entries grow at most polynomially.

## 5. Independence of the operator presentation

If two actual all-level operators are used with a common sufficiently
large starting color j_*, their ratios (3.2) are identical, by (3.3).
Their orders, jet bounds, singular steps and matrix sizes can differ.
The equality is exact and retains their distinct lattice presentations.
Starting at two different fixed colors changes G_N only by finitely
many bounded small-color terms.

In particular the construction is not a largest-root prescription,
and it does not require an equality between the root-central
characteristic and the classical A-polynomial. Multiplying an
annihilator by a harmless or singular left factor changes its
finite jet system but leaves the exact ratio unchanged when the
same pointing and valid pole budget are used.

### A uniformly bounded jet lattice and its classical symbol

The polynomial growth in individual jet entries is removable
without changing the period. Set

    S_N=direct_sum_(j=j_*)^N diag(1,N^(-1),...,N^(-B)),
    M_tilde=S_N M_N S_N^(-1), b_tilde=S_N b_N.          (5.1)

Since R_N S_N^(-1)=R_N, the pointed Gram theorem applied to
these scaled data gives exactly the same G_N. This is a genuine
change of lattice and source, not an inference from invariance
of an unpointed norm. In the new matrix a jet coefficient of
order r is divided by N^r. Formula (2.1) shows that every entry,
the matrix operator norm, and the source norm are now bounded
uniformly in N. The bandwidth, size O(N), and nullity bound
are unchanged. The source border remains confined to a fixed
number of initial blocks.

This also identifies the bulk symbol of the positive determinant
problem directly from the actual A-operator. Write x=j/N,
M(x)=-exp(pi i x), delta_M=M partial_M, and let J be the
(B+1)-dimensional nilpotent subdiagonal shift. For fixed r,
the scaled coefficient in (2.1) tends uniformly to

    (-1)^c exp(pi i c x) (cx)^r/r!.

Thus the banded interior recurrence has block symbol, up to
the harmless scalar Fourier factor L^(-d),

    A_B(x,L)=sum_(i=0)^d sum_(r=0)^B
        x^r/r! [delta_M^r a_i(1,M)]_(M=M(x)) J^r L^i.
                                                        (5.2)

It is lower triangular in jet degree and satisfies

    det A_B(x,L)=A_cl(M(x),L)^(B+1).                  (5.3)

No additional classical curve is introduced by the jet repair.
For |L|=1 the Hermitian bulk Gram symbol is A_B^dagger A_B,
with determinant |A_cl(M(x),L)|^(2(B+1)). The initial equations
and source border are explicitly retained boundary terms.

These are statements about the chosen actual operator's symbol.
They do not assert that its classical polynomial has already
been identified with A_K, or estimate the small boundary singular
values of the finite matrices. Even a strictly positive bulk
Gram symbol need not bound those finite boundary singular values
away from zero; the growing-recurrence example below exhibits this.

### The actual quantum period is a positive regularized response

There is a canonical convex quadratic problem for these same scaled
data, with the original source retained. For real z>=0 put

    Phi_N(z)=min_y {||M_tilde y-b_tilde||^2+z||R_N y||^2}.
                                                        (5.4)

On the orthogonal complement of ker M_tilde its minimizer is unique.
If P_r,Q_r,g_r denote the restrictions of M_tilde^dagger M_tilde,
R_N^dagger R_N and M_tilde^dagger b_tilde, respectively, then

    Phi_N(z)=beta-g_r^dagger(P_r+z Q_r)^(-1)g_r,
    Phi_N(0)=0, Phi_N'(0)=G_N(A,j_*).                  (5.5)

The second identity follows from the proof of (3.3). Thus the
period is an ordinary derivative of an algebraic response function,
specified by finite matrices and a fixed source. The positive
gradient flow y'=-(P_r+zQ_r)y+g_r solves (5.4) for each fixed N;
its existence is not an assumption about a chosen knot state.

The source dependence can also be retained in a positive spectral
measure. Set H=P_r^(-1/2)Q_r P_r^(-1/2), u=P_r^(-1/2)g_r.
For its orthonormal eigenbasis H e_a=h_a e_a put
w_a=|e_a^dagger u|^2. Then exactly

    Phi_N(z)=sum_a w_a z h_a/(1+z h_a),
    G_N=sum_a w_a h_a, sum_a w_a=beta=O(1).             (5.6)

All h_a,w_a are nonnegative. The response is increasing and
concave in z. The weights record the original source and cannot
be dropped in favor of an extremal eigenvalue. Equations (5.4)--(5.6)
supply an actual quantum variational problem and its rigid algebraic
response for arbitrary knots. Relating this response to the geometric
angle-volume optimization and proving its exponential rate remain
the geometric part of the conjecture.

## 6. The desired A-polynomial/volume identity, with the original invariant

The independently proved positive ordinary-color bound in
[the regular-period note](regularized_kashaev_period.md#2-a-positive-trace-bounds-all-the-ordinary-colors)
gives |C_j(q_N)|=O_K(N^(b-1)) for 1<=j<N, where b is any fixed
knot-braid strand count. Therefore

    G_N(A,j_*)=|<K>_N|^2+O_K(N^(2b-1)),
    G_N(A,j_*)>=|<K>_N|^2.                             (6.1)

This is also the earlier positive cyclic trace norm H_N, with
its fixed small-color prefix removed:

    G_N(A,j_*)=N H_N-sum_(j=1)^(j_*-1)|C_j(q_N)|^2.

The new content relative to that norm formulation is the explicit
positive polynomial-coefficient ratio from the actual operator,
its uniformly bounded banded jet lattice and its response function.
No new knot state is being introduced.

For a hyperbolic knot with positive volume V, its original volume
conjecture is consequently equivalent to the polynomial-period identity

    lim_(N->infinity) (pi/N) log G_N(A,j_*)=V.           (6.2)

Equivalently the marked regulator norm of the existing torsor gives

    (2/N)log G_N(A,j_*)-log||P_hyp|| ->0,
    log||P_hyp||=2V/pi.                                (6.3)

The equivalence uses only the polynomial remainder in (6.1): a
positive exponential norm dominates that remainder in either direction.
It does not presume that <K>_N is eventually nonzero. If (6.2)
were proved, eventual nonvanishing would follow from (6.1).

This is a positive determinant-period formulation with the actual
quantum A-operator on the left, the original finite pointing retained,
and no restriction on bridge number or alternatingness. It is an
exact algebraic reduction of the required theorem, not a proof of
its exponential estimate. That estimate and its link with the
geometric A-curve's marked regulator are still necessary.

Fixed bandwidth and polynomial matrix entries alone do not imply a
polynomial bound on (3.2): a constant-coefficient recurrence y_j=c y_(j-1)
already has a determinant ratio growing as sum |c|^(2j). Small
singular values and the source border can encode an exponential
rate. No estimate of those determinants is inferred from their
construction or from positivity.

[Audit](../experiments/audit_pointed_a_gram_period.py).
[Results](../experiments/pointed_a_gram_period_results.json).

The subsequent [tempered leading-divisor theorem](tempered_a_growth_bound.md)
gives a one-sided exponential estimate for this period under its
explicit operator hypotheses. It proves the complete leading-germ
normalization and a direct matrix-product upper bound through
eigenvalue collisions. Its largest-root integral is not identified
with the selected volume; the source and sharp lower estimate remain.
