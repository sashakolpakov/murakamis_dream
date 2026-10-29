# Exponential ordinary-color control and elimination of fast modes on a regular arc

28 October 2026. Two statements below are proved directly for the
original source. First, every fixed knot diagram has an exp(CN) bound
for ALL ordinary colors j<=cN on a fixed O(1/N) complex annulus around
q_N. Second, on a compact arc where the highest surviving classical
coefficient is nonzero, the higher quantum-order terms can be eliminated
using a slow-forward / fast-backward comparison. No eigenframe, lower
bound for the actual leading coefficient, or bound on an inverse braid
is used.

This weakens the order-survival hypothesis of the
[macroscopic spectral bound](actual_macroscopic_a_spectral_upper_bound.md)
on a regular arc. It does NOT yet remove it globally across zeros of the
highest surviving classical coefficient. That additional gluing problem,
including a zero at the selected endpoint, is stated explicitly below.

## 1. Actual ordinary colors are exponentially bounded on the full annulus

Fix an original zero-framed b-strand braid closure representing a knot,
and let C_j(q) be its ordinary reduced color-j scalar, with the original
half-Cartan, pivot K(q), and framing twist. For fixed c,S>0 there are
constants A,B, depending on the word,c,S, such that

    |C_j(exp((pi*i+s)/N))| <= j^B exp(Aj),
    1<=j<=cN, |s|<=S.                              (1)

In particular the right side is exp(CN). This includes j>=N and both
parities. It is a statement about the GENERIC ordinary Laurent
polynomial family, not a quotient-color assertion for a high ADO color.
There is no division by a vanishing quantum dimension in the proof.

Proof. Use the ordinary highest-weight basis with

    E v_a=[a]_q[j-a]_q v_(a-1), F v_a=v_(a+1),
    H v_a=(j-1-2a)v_a, 0<=a<j.

In the original positive R, the h-transfer coefficient before its
Cartan factor is

    q^(h(h-1)/2) rho^h/[h]! * [a]!/[a-h]!
                      * product_(r=0)^(h-1)[j-a+r], rho=q-q^-1.

Equivalently it is

    q^(h(h-1)/2-h(a-h)) [a choose h]_(q²)
              * product_(r=0)^(h-1)(q^(j-a+r)-q^(-j+a-r)).       (2)

This is an exact polynomial cancellation, valid also where a divided
factorial in the first expression vanishes. The inverse has the same
form, with the corresponding input/color and an altered q-monomial.
All those monomial exponents, including the Cartan weight product/2,
have absolute value at most Cj². Keep the marked half-root
q^(1/2)=exp((pi*i+s)/(2N)); no parity simplification is made.

In fact, in the Laurent coefficient norm in the marked half-root,
each entry in (2) has norm at most 4^j: the Gaussian coefficient has
coefficient sum binom(a,h)<=2^j, and each of the h binomial factors
has coefficient norm two. Monomials do not change this norm. The same
argument applies to the inverse crossing. If the fixed braid has ell
crossings, summing its at most j choices per crossing and its
j^(b-1) environmental trace indices gives the explicit coarse bound

    ||C_j||_(Laurent coefficient l1)
                  <=j^(ell+b-1) 4^(ell*j).         (2a)

Pivots, the full common Cartan line, and the zero-framing correction
are monomials and have coefficient norm one. This is a bound for the
original reduced cut, so no dimension denominator has been inserted.
Together with the directly proved degree O_word(j²), (2a) is an
alternative proof of (1).

Gaussian Pascal gives nonnegative integer coefficients, total
coefficient sum binom(a,h)<=2^a, and degree h(a-h)<=j²/4. Therefore

    |[a choose h]_(q²)| <= 2^j exp(S j²/(2N)).        (3)

Each factor in the product in (2) is at most 2exp(2Sj/N), while any
remaining q-monomial costs exp(CSj²/N). Since j<=cN, both crossing
signs consequently have every entry bounded by exp(A0 j). A checked
two-head matrix has at most j nonzero entries in any row or column,
so its original flat operator norm is at most j exp(A0 j).

A fixed braid word has norm at most j^B0 exp(A1 j). The ordinary pivot
has norm at most exp(Sj/N), and the zero-framing scalar has modulus
at most exp(C_word Sj²/N). The literal reduced cut is

    C_j(q)=theta_j^(-w)
       [Tr_env(W_j(q)(I tensor K(q)^(tensor(b-1))))]_(0,0).

Bounding that trace by j^(b-1) times the matrix norm proves (1).
This is the original cut definition. At exceptional q it follows by
the displayed integral matrix expressions/continuity, with no
replacement of the pivot or source.

## 2. The exact slow-forward / fast-backward system

Suppose the actual generic color family has a specified recurrence

    sum_(i=0)^d a_i(q,-q^j) C_(j+i)(q)=0,          (4)

with Laurent polynomial coefficients. Remove a common q-1 power. Let
m be the HIGHEST index for which a_m(1,M) is not identically zero;
assume 1<=m<d and put r=d-m. On a compact x interval I suppose

    |a_m(1,-exp(pi*i*x))| >= c0 >0.               (5)

All estimates below are uniform for q=q_N exp(s/N), |s|<=epsilon_N,
epsilon_N->0. In particular they apply at s=0. On I and fixed finitely
many neighboring mesh points, division by a_m is harmless. Put

    g_i(j)=a_i(q,-q^j)/a_m(q,-q^j), 0<=i<m,
    Y_j=(C_j,...,C_(j+m-1))^t,
    z_j=C_(j+m)+sum_(i<m)g_i(j)C_(j+i).            (6)

These are the original scalar values, not new independent solutions.
With A_j the m by m companion having last row -g_i(j),

    Y_(j+1)=A_j Y_j+e_m z_j.                     (7)

For i=m+t, iterating (7) a fixed t+1 steps expresses C_(j+i) as a
bounded row times Y_j plus a bounded linear combination of
z_j,...,z_(j+t). All those rows are uniformly bounded because d is
fixed and the g_i are bounded. For i>m,

    a_i(q,M)=(q-1)b_i(q,M),                       (8)

since its specialization at q=1 is identically zero. Thus its ratio to
a_m is O(1/N), uniformly on (5). Substituting these fixed forward
expansions into (4), and absorbing the resulting O(1/N) coefficient
of z_j, gives the EXACT relation

    z_j=c_j Y_j+sum_(l=1)^r b_(j,l) z_(j+l),
    ||c_j||+sum_l|b_(j,l)| <= C/N.               (9)

No approximation or factorization of a characteristic polynomial is
used to obtain (9). In particular, no division by a_d occurs. Equation
(9) is a backward-contracting fast system even if the original
d by d forward companion is unbounded or undefined at a particular q.

## 3. A two-boundary comparison with a macroscopic right buffer

Let A(x) be the classical m by m companion formed from
a_0(1,M),...,a_m(1,M), and rho(x) its spectral radius. Fix epsilon>0.
The positive Lyapunov metric from the spectral-bound note gives,
uniformly on I and for large N, a norm in which one step in (7) has
cost at most

    R_j=rho(j/N)+2epsilon.                        (10)

The metric and its inverse are bounded. Its variation on adjacent mesh
points is absorbed in the fixed epsilon. In particular R_j is bounded
above and below by positive constants, including when rho=0.

Let w_a=1 and w_(j+1)=R_j w_j. After dividing by w_j and using the
metric, (7),(9) imply scalar inequalities with one fixed constant C:

    U_(j+1)<=U_j+C Z_j,
    Z_j<=h C U_j+h C sum_(l=1)^r Z_(j+l), h=1/N,                 (11)

where U_j=||Y_j||/w_j and Z_j=|z_j|/w_j. Bounded ratios
w_(j+l)/w_j for l<=r have been included in C.

Take the equations for a<=j<B, specifying only U_a and the r terminal
values Z_B,...,Z_(B+r-1). Suppose the latter are at most exp(C1N).
This is available for the original source by (1); the weight w_j and
the bounded rows in (6) change that bound only by another exp(C2N).

Here is an elementary positive supersolution for this mixed boundary
problem. Choose kappa=2C and lambda=4C², increasing them slightly if
needed for strict inequalities. For sufficiently large N let

    eta=N^(-1/(2r)),
    U_j^slow=A exp(lambda h(j-a)),
    Z_j^slow=kappa h U_j^slow,
    Z_j^fast=B0 eta^(B-j),
    U_j^fast=4C eta Z_j^fast.                    (12)

Take A>=max(1,U_a) and B0>=max terminal Z_j. The sum of the slow and
fast packets is a strict supersolution of (11). For its fast Z-row,
the future contribution is at most

    h C r eta^-r=Cr/sqrt(N)->0.

For its slow Z-row the future contribution is O(h²) relative to
U_j^slow. The U-rows follow respectively from
exp(lambda h)-1> C kappa h and
4C>C+4C eta. These verify every inequality for large N.

For completeness, comparison needs no invertibility theorem. If an
actual component exceeded its supersolution, take the largest ratio
over the finite U,Z array. It cannot be on the specified boundaries.
At an interior component, (11) and the strict supersolution make the
ratio a strict subaverage of ratios no greater than that maximum,
a contradiction. Thus (12) bounds the original solution.

For a target T with B-T>=delta N, delta>0 fixed, the terminal term is

    <=exp(C2N) N^(-(B-T)/(2r))=exp(-Omega(N log N)).              (13)

The slow term costs exp(O(1)) beyond w_T and A. Therefore, if U_a
is polynomial, the ORIGINAL selected solution satisfies

    limsup (1/N)log||Y_T||
          <= integral_(lim a/N)^(lim T/N) log(rho(x)) dx,        (14)

interpreting the right side by epsilon-downward limiting if needed.
For the usual nonzero lower classical coefficient its logarithm is
integrable. All terminal fast data were retained and bounded; they
were not set to zero.

## 4. A genuine partial extension of the actual whole-source theorem

Suppose (4) is an actual all-level ordinary color recurrence, its
highest surviving classical index m>=1, and (5) holds on

    I=[1/k,1+delta]

for some fixed delta>0. Start with the m colors ending at the actual
positive macroscopic window J_N=1+floor((N-1)/k). These initial values
are polynomially bounded. Take T=N and B=floor((1+delta/2)N).
The ordinary-color exponential bound (1) supplies every terminal
value needed in (12), even though those colors are larger than N.
Consequently (14) gives

    limsup (1/N)log|K_N|
          <= integral_(1/k)^1 log rho_m(x) dx.                  (15)

This uses the finite roots of the HIGHEST SURVIVING CLASSICAL order,
even when d>m. It proves actual scalar control, not merely a formal
slow characteristic. At s=0 the exact color recurrence and (5) suffice;
there is no moving-q denominator to regularize and no inverse of the
actual leading coefficient. The complex-annulus version of the same
argument is also valid when the initial packet has its independently
proved polynomial complex bound.

## 5. The precise remaining exceptional-set problem

The condition (5) is essential in this proof. Near a zero of a_m(1,M),
the coefficients g_i and the small coefficients in (9) need not remain
bounded. The old d-order forward companion can still be polynomially
bounded on a suitable tiny q-circle, but multiplying that bound over
a fixed macroscopic buffer costs exp(O(N log N)), not exp(o(N)).
Conversely a shrinking buffer need not suppress the a priori exp(CN)
terminal data by (13). Thus those two estimates cannot simply be
combined to assert global elimination through a turning core.

This note proves neither that such exceptional cores necessarily add
growth for a knot, nor that they can be omitted. A compatible global
slow/fast transport or an additional source constraint at every core
is still needed to remove the classical-order-survival assumption
for an arbitrary annihilator. It also proves no geometric inequality
for the finite-root integral and no selected lower bound.

Reproduce the finite coefficient cancellations and exact defect-system
identity with

```sh
python3 experiments/audit_actual_regular_fast_color_elimination.py
```

The audit supplements the proofs above; it does not replace the
uniform barrier argument or claim an exceptional-core theorem.
