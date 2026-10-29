# Positive multiplication in the actual full Newton source algebra

29 October 2026. The actual two-head source algebra has an explicit
NONNEGATIVE multiplication table in the same full Newton basis in which
the genuine quarter-turn reverses coordinates. This includes every
paired first normal, both level parities and composite levels. It is
not a positive model substituted for the original source.

Let N>=2, d=N-1, q=exp(pi i/N), Q=q^2, and

    c_j=q^(2j+1)+q^(-2j-1),
    s_r=product_(u=1)^r 2sin(pi u/N), s_0=1,
    B_r(z)=product_(j=0)^(r-1)(c_j-z),
    Bhat_r=B_r/s_r^2, 0<=r<=d.

The physical algebra is H_N=C[z]/P_N with
P_N=2T_N(z/2)+2. The
[actual Newton turn theorem](actual_newton_turn_positive_gram.md)
identifies this with the full original Hopf commutant and proves

    Rturn Bhat_r=Bhat_(d-r),
    phi(Bhat_i Bhat_j)=delta_(i+j,d),
    original cup-mark closure(f)=f(c_0)=alpha_0,
    phi(f)=alpha_d, if f=sum_r alpha_r Bhat_r.        (1)

The turn in (1) is the actual root operator with its original cups and
caps. Its simple root formula is NOT an arbitrary generic-q continuation.

## 1. Uniform multiplication theorem

If i+j<N, then in the ACTUAL algebra

    Bhat_i Bhat_j=sum_(k=max(i,j))^(i+j) mu_(i,j,k) Bhat_k,

    mu_(i,j,k)=s_(i+j)s_k
       /[s_i s_j s_(k-i)s_(k-j)s_(i+j-k)] > 0.       (2)

If i+j>=N, their product is ZERO in H_N, including all root normals.
Every denominator in (2) has index less than N. The formula is symmetric
in i,j and its unit cases are exact.

Here is an own generic finite proof. For generic zeta define
[u]=(zeta^u-zeta^(-u))/(zeta-zeta^(-1)), [u]!=product_[1,u],
t=-(zeta-zeta^(-1))^2, and use the same generic nodes and B polynomials.
Then

    B_i B_j=sum_(k=max(i,j))^(i+j) A_(i,j,k) B_k,
    A_(i,j,k)=t^(i+j-k) [i]![j]![i+j]!
       /([k]![k-i]![k-j]![i+j-k]!).                 (3)

By symmetry take i<=j. Starting at i=0, multiply by c_i-z and use

    (c_i-z)B_k=B_(k+1)+(c_i-c_k)B_k,
    c_i-c_k=t[k+i+1][k-i].                          (4)

The coefficient recurrence is
A_(i+1,j,k)=A_(i,j,k-1)+(c_i-c_k)A_(i,j,k).
After division by the nonzero interior factorial factors in (3), this
is exactly the elementary identity

    [i+1][i+j+1]=[k][k-j]+[k+i+1][i+j+1-k].         (5)

Expand the four powers of zeta on each side to verify (5). At the
lower and upper endpoints the same recurrence follows by its zero
factors or its leading coefficient 1. This proves (3) as a finite
rational identity, without a summation formula or a fit to samples.

At the principal root and i+j<N, [u]!=s_u/(2sin(pi/N))^u.
The powers of 2sin cancel t, and multiplication by
s_k^2/(s_i^2s_j^2) converts (3) precisely to (2).

For i+j>=N, c_(d-u)=c_u implies the polynomial identity

    B_N/B_j=B_(N-j).

Since i>=N-j, B_i B_j is divisible by B_N=(-1)^N P_N.
This is divisibility WITH MULTIPLICITIES, not equality only at distinct
nodes. Hence the zero assertion holds on the full physical source.

## 2. A positive cone preserved by genuine operations

Let C_N consist of all sum alpha_r Bhat_r with alpha_r real and >=0.
Equations (1),(2) prove that C_N is preserved by:

* actual serial multiplication of two-head boxes;
* the genuine quarter-turn;
* sums and multiplication by nonnegative real scalars.

Both actual closures in (1) are nonnegative on this cone. Thus any
specified physical two-head circuit built from cone-valued coupons
by these operations has an exact positive finite contraction. There
is no cancellation of positive terms and no lost normal coefficient.
Associativity is inherited from the actual polynomial/operator algebra.
No separate move normalization or conjectural topological invariance
has been imposed on a new state sum.

This does NOT say that a crossing R^e is cone-valued, that an arbitrary
multiport graph reduces to this alphabet, or that every such circuit
is hyperbolic. A proposed application must supply its actual ordered
two-head decomposition and preserve its original marking.

The nonzero test is also finite. A multiplication gate permits precisely

    i+j<N, max(i,j)<=k<=i+j.                        (6)

A turn replaces r by d-r. A closure fixes r=0 or r=d. Therefore a
whole typed circuit with strictly positive allowed input coordinates
is nonzero if and only if at least one internal label assignment
satisfies (6) and its turn/closure constraints. This is an exact finite
support certificate, not a claim that topology alone ensures it.

## 3. The original complete circle belongs to this cone at every level

For the actual complete circle use

    L_N(z)=(-1)^d U_d(z/2)=(-1)^d P_N'(z)/N.

The original Frobenius functional is
phi(f)=(-1)^d N^2[z^d](f mod P_N). Consequently

    phi(L_N f)=N Tr(m_f)=N sum_(j=0)^d f(c_j),       (7)

where m_f is multiplication by f in H_N. To prove the trace identity,
first take a monic polynomial with distinct roots and apply its exact
Lagrange interpolation to P' f mod P. Its leading coefficient is the
sum of f at those roots. Both sides are polynomial expressions in the
coefficients of P and f, so equality extends to repeated roots by
clearing the interpolation denominators. The trace counts algebraic
multiplicity and does not omit the paired blocks.

By (1), the r-th Newton coefficient of L_N is phi(L_N Bhat_(d-r)).
Put M=floor(d/2), v=d-r, and let k_l be 2 on a paired node and 1
on the odd simple node. Formula (7) gives the explicit coefficients

    lambda_r=0, r<d-M,
    lambda_r=N sum_(l=v)^M k_l
                s_(l+v)/[s_(l-v)s_v^2]>0, r>=d-M. (8)

Indeed Bhat_v(c_l)=0 for l<v, while for v<=l<=M the factorization

    c_t-c_l=4sin((l+t+1)pi/N)sin((l-t)pi/N)

gives Bhat_v(c_l)=s_(l+v)/(s_(l-v)s_v^2). For v>M the polynomial
already vanishes at every root, so its trace is zero. This proves
(8) with all multiplicities, including N=2 and both parities.

Thus complete-circle/turn/multiplication circuits give a genuine
all-level positive family inside the ORIGINAL source theory.
Their exact zeros remain important: for even N the support in (8)
starts at N/2, so L_N^2=0 by (2). Positivity does not hide that zero.

The same statement holds for EACH complete-circle sector. Let E_j
be the full Hermite cluster projector and L_j=L_N E_j. Formula (7)
with f replaced by E_j f gives phi(L_j f)=N k_j f(c_j). Thus, with
the original paired multiplicity k_j retained,

    Rturn(L_j)/(N k_j)=h_j
       =sum_(v=0)^j s_(j+v)/[s_(j-v)s_v^2] Bhat_v. (8a)

Every coefficient is strictly positive and every other coefficient is
zero. This applies to both parities, including paired nilpotent sectors;
it does not replace L_j by a projector. No derivative of f is missing:
the derivative in L_j is precisely the full Frobenius/trace identity
that produced (8a).

## 4. Odd simple projector and the primitive cube period

At N=2m+1, the simple Steinberg node is c_m=-2. Its genuine spectral
projector is

    E_St=B_m^2/N^2=Bhat_m^2,                        (9)

because B_m(c_m)=N and s_m^2=N; it has the required DOUBLE zero at
every paired node. Apply (2) and the actual turn to obtain

    h=Rturn(E_St)=sum_(v=0)^m beta(m,v)^2 Bhat_v,
    beta(m,v)=s_m/[s_v s_(m-v)]>0.                 (10)

All coefficients in (10) are positive; this proof uses the complete
polynomial projector rather than interpolation at simple values.
Write h^2=sum a_k Bhat_k. Formula (2) gives

    a_k=sum_(0<=i,j<=m, max(i,j)<=k<=i+j)
                     beta(m,i)^2 beta(m,j)^2 mu_(i,j,k)>0
                                              for EVERY 0<=k<=d. (11)

For nonemptiness choose i+j=k with i,j<=m. Therefore

    phi(h^4)=sum_(k=0)^d a_k a_(d-k)>0.             (12)

No identity Rturn(h^2)=h^2 is needed for (12). In particular a
root observation of that identity is not being continued generically.
The separate primitive-cube calculation must still prove its actual
normalization and the asymptotic/geometric interpretation of this
period. Equation (12) supplies its cancellation-free positive form.

More generally every h^p, p>=2, has positive coefficients at ALL
indices 0,...,d: h has a positive constant term and (11) starts the
induction. In particular phi(h^p)>0 for every such p. This is an exact
period statement, not an automatic topological or volume identification
for each power.

Audit: [generic finite products and full root-algebra verification](../experiments/audit_actual_positive_newton_multiplication.py).
The uniform proofs above establish positivity; finite tests independently
check the formulas, the actual repeated-root quotient and complete-circle
coefficients. They are not a general graph volume theorem.

Independent analytical review by the global audit agent checked the
generic induction, root normalization, repeated-root divisibility,
trace identity, circle support and odd projector/positive period.
