# Exact star–triangle reduction with its retained degree defect

28 October 2026. The balanced root-of-unity star–triangle identity in
[the general source fusion theorem](actual_general_flow_fusion.md) has
an exact extension to stars below balance. It factors off the same
cyclotomic pair constraints and retains a polynomial whose degree is
exactly the balance defect. Its normalized coefficient norm has the
explicit bound (e+1)^5 binom(N+e,e)^6, so EVERY sublinear defect
e=o(N) has only subexponential cost. No claim is made that the
original knot state has defects in this range, or that contracting its
remaining polynomial cannot cancel the geometric contribution.

## 1. Polynomial factorization, including an unbalanced star

Fix a primitive Nth root Q, put d=N-1, and write

    B_L(X,Z)=product_(r=0)^(L-1)(X-Q^r Z).

Let 0<=L_i<=d, S=L_1+L_2+L_3, and suppose

    S<=2d,                 L_i+L_j>=d for every i!=j.       (1)

Define

    e=2d-S,       k_i=d-L_i,       a_i=k_i-e.

Then a_i>=0, sum k_i=d+e, sum a_i=d-2e. In particular
0<=e<=d/2. The actual charged contraction is

    F_L(X_1,X_2,X_3)=[Z^d] product_i B_(L_i)(X_i,Z).

There is an EXACT homogeneous polynomial R_L of degree e such that

    F_L=Delta_L R_L,                                      (2)

    Delta_L=
       product_(r<a_3)(X_1-Q^(k_2+1+r) X_2)
      *product_(r<a_1)(X_2-Q^(k_3+1+r) X_3)
      *product_(r<a_2)(X_3-Q^(k_1+1+r) X_1).               (3)

This holds in the ordinary polynomial ring, BEFORE nilpotent source
reduction. Arbitrary nonzero coefficients in front of Z are allowed
by substituting X_i -> X_i/b_i and multiplying by product b_i^L_i.
One can subsequently identify neighbor variables as required by the
actual graph.

Proof. Set X_i=Q^p X_j with

    N-L_j <= p <= L_i.

The two incident products have, as roots in Z, intervals with exponents
[p-L_i+1,p] and [-L_j+1,0]. The conditions on p make these intervals
overlap or touch, and their union contains at least N consecutive
integers. Their product is divisible by X_j^N-Z^N, up to a nonzero
scalar. The remaining product has Z-degree S-N<=d-1. Therefore its
product with X_j^N-Z^N has ZERO Z^d coefficient: the constant term
would need degree d in the remainder, while the Z^N term is already
too large. Thus every linear factor displayed in (3) divides F_L.
They are pairwise nonassociate factors in the three-variable polynomial
ring. Their total degree is d-2e. Since F_L has degree S-d=d-e,
the quotient has degree e. The nonzero coefficient below also proves
that F_L and R_L are not identically zero. This argument uses only
the full cyclotomic product and polynomial divisibility.

## 2. A nonzero marked coefficient fixes the normalization

Put T(n)=n(n-1)/2 and use the Gaussian binomial with base Q. The
coefficient of X_2^e in R_L is exactly

    c_L=(-1)^(d-a_3)
        Q^[T(L_1)+T(k_1)-(k_2+1)a_3-T(a_3)]
        {L_3 choose k_1}_Q.                              (4)

In particular c_L!=0: L_3=k_1+a_2<=d and 0<=k_1<=L_3.

To prove (4), set X_1=0. The first block contributes
(-1)^L_1 Q^T(L_1) Z^L_1. To get the largest X_2 exponent in the
remaining Z^k_1 coefficient, take no Z from the second block and
k_1 powers from the third. The resulting coefficient is
(-1)^d Q^[T(L_1)+T(k_1)] {L_3 choose k_1}_Q at
X_2^(a_1+a_3+e) X_3^a_2. The corresponding leading coefficient
of Delta_L is (-1)^a_3 Q^[(k_2+1)a_3+T(a_3)]. Division gives (4).

At e=0 the quotient is the single scalar c_L, recovering the
balanced star–triangle theorem, with all phases retained. At e>0,
replacing R_L by this one coefficient is NOT an exact source identity.

## 3. Growing defect jets have an explicit uniform exponential scale

For EVERY admissible e, not just a fixed degree, the coefficient norm
satisfies the explicit uniform estimate

    |c_L| <= ||R_L||_1 <= (e+1)^5 (2N)^(4e) |c_L|.       (5)

The norm is the sum of the ordinary complex coefficient moduli,
not the value after contraction against an exterior knot source.
This already covers e_N log N=o(N). The refinement (5a) below
extends the conclusion to EVERY e_N=o(N).

Here is a direct proof that does not hide constants growing with e.
Set a=X_1/X_3, b=X_3/X_2. If c_D is the unit-modulus leading
coefficient of Delta_L, then

    Delta_L=c_D X_2^(a_1+a_3) X_3^a_2 D(a,b),

where D is a product of a_2 factors (1-unit*a), a_1 factors
(1-unit*b), and a_3 factors (1-unit*a*b). The quotient R_L/X_2^e
has monomials a^u b^(u+w), u+w<=e. All needed a and b exponents
therefore lie between zero and e.

Also F_L/(c_D X_2^(d-e) b^a_2) is an ORDINARY polynomial in a,b:
in each monomial of F_L the X_2 degree is at most L_2, and
d-e-L_2=a_2. Its coefficient at a^i b^j, for i,j<=e, comes from
the original three Z indices

    L_1-i,           j,           k_1-j+i.

The first two binomials have moduli <=N^i and <=N^j. The third
differs from {L_3 choose k_1}_Q by |i-j| adjacent-index steps.
Each ratio or its reciprocal along valid indices has modulus <=N:
all its nonzero factors satisfy 4/N<=|1-Q^r|<=2. Thus these
coefficients of F_L, after dividing by c_D, are bounded by

    |c_L| N^(i+j+|i-j|) <= |c_L| N^(2e).

Invalid indices give zero; no vanishing factorial is inverted.
The same bound holds for any complex primitive Nth root, since its
nonzero factors are a permutation of the standard ones.

Expand 1/D formally at (0,0). Its coefficient of a^u b^v is a
sum over at most e+1 choices t for the number of factors of type ab.
Each term is bounded by a product of three complete homogeneous
coefficients of lengths <=d and degrees u-t,v-t,t. Their elementary
counting bounds give, for u,v<=e,

    |[a^u b^v](1/D)| <= (e+1)(2N)^(u+v).

Convolving with the needed rectangle of F_L uses at most (e+1)^2
terms. There are at most (e+1)^2 coefficients of R_L. Combining
these bounds proves the upper estimate (5); (4) gives its lower
estimate. This proof permits e to grow with N throughout.

The counting can be sharpened uniformly, including e=0. Put
B=binom(N+e,e). Then

    ||R_L||_1/|c_L| <= (e+1)^5 B^6
                 <= (e+1)^5 (2 exp(1) N/e)^(6e), e>=1. (5a)

The first bound applies also at e=0, when B=1 and R_L=c_L.

Indeed the kth smallest modulus among the N-1 nonzero root factors
is at least 2k/N: distance min(j,N-j) occurs at most twice and
2 sin(pi*j/N)>=4 min(j,N-j)/N. Therefore the product of ANY r
distinct such factors is at least (2/N)^r r!, at every primitive
root. A Gaussian-binomial index shift of r steps has numerator
bounded by 2^r and r distinct denominator factors, so its ratio
is at most N^r/r!, in either direction when the indices are valid.

The first two binomials in the rectangle have moduli at most their
ordinary binomial coefficients: their elementary-symmetric expansion
is a sum of binom(L,i) unit terms. These counts are <=B for i<=e
and L<=d. For the third relative ratio, r<=e gives

    N^r/r! <= N^e/e! <= B.

Thus every rectangle coefficient is bounded by |c_L|B^3. Each
complete homogeneous coefficient of degree r<=e and length <=d
is a sum of at most binom(d+r-1,r)<=B unit terms. The three groups
in 1/D therefore give (e+1)B^3. The convolution and quotient-support
counts each contribute at most (e+1)^2, proving (5a). Finally
B<= [exp(1)(N+e)/e]^e<= [2 exp(1)N/e]^e for e>=1.
No constant in these bounds depends on e.

Consequently log(||R_L||_1/|c_L|)=o(N) for every e=o(N), since
e log(N/e)=o(N). This includes all sublinear windows, not just a
fixed normal depth or an O(sqrt N) window. At e=0, R_L=c_L exactly.

For the ACTUAL standard root Q=exp(2*pi*i/N), the exact modulus
of (4) is N/(|F_(k_1) F_(k_2-e) F_(k_3)|). The uniform endpoint
factorial estimate and (5a) consequently give, for e>=1,

    log ||R_L||_1 = (N/pi) sum_i Lambda(pi*k_i/N)
                         +O(e log(N/e)+e+log N).          (6)

The replacement of F_(k_2-e) by F_(k_2) obeys the same error bound:
the intervening e factors have product between (2/N)^e e! and
2^e. At e=0 the error in (6) is simply O(log N).

Here Lambda(theta)=-integral_0^theta log|2 sin u| du. The last
formula uses the uniform endpoint-aware factorial estimate already
proved for the original state, together with reflection about N.
In particular if e=o(N) and k_i/N -> t_i>0, then sum t_i=1.
The corresponding limiting ideal tetrahedron has angles pi*t_i, and

    lim (2pi/N) log ||R_L||_1 = 2 Vol(tetrahedron).       (7)

The factor TWO is essential. A single extracted scalar must not be
counted as one tetrahedron in the volume-conjecture normalization.
The entire transformed source, including its new triangle factors,
is what preserves the knot period.

## 4. What this permits in the proposed leading/jet reduction

Equations (2)-(5) are a precise, source-compatible local meaning of
"a geometric factor with a controlled quantum correction."
The correction is retained as a homogeneous polynomial; it is not
erased by an unsupported assertion of nilpotence or rigidity.

### The degree defect is the exact angular source-phase frequency

There is an analytic interpretation on the original unit-radius anchor
torus. Let a charged product, including all its explicit constant
normalizers, be

    P(X)=gamma product_f (alpha_f X_(i_f)-beta_f X_(j_f)),
    |alpha_f|=|beta_f|=1, X_a=exp(i theta_a).

Let S_a count the incident linear factors at anchor a, counting a
self-loop twice. The source density is P(X) product_a X_a^(-d).
On fixed real argument lifts, the elementary identity

    exp(i A)-exp(i B)=2i exp(i(A+B)/2) sin((A-B)/2)

gives EXACTLY

    P(exp(i theta)) product_a exp(-i*d*theta_a)
       =C exp[(i/2)sum_a (S_a-2d)theta_a] A(theta),       (8)

where C is an explicit theta-independent nonzero scalar and A(theta)
is the real product of the displayed sine factors. A(theta) may change
sign; this is not a positivity assertion. In particular, away from
its zero set the angular phase derivative equals

    partial_(theta_a) Arg(source density)=(S_a-2d)/2.    (9)

Equation (8) is global on the lifted angles. Its sine signs account
for the apparent phase jumps and the periodicity of the original
integer-degree density. Self-loops satisfy the same formula because
their common anchor contributes one full theta_a phase.

Thus the additive fusion defect S_a-2d is precisely the source's
angular frequency, not only a formal incidence count. A full-block
contraction adds the two endpoint defects at the identified anchor;
a balanced star--triangle move removes a zero-frequency direction
and preserves every outer defect. These are the exact incidence
identities proved in the general fusion note. Removing an explicit
self-loop monomial reduces both S_a and 2d by the same amount, when
the remaining source charge is written correctly.

For the below-balance central star here, S=2d-e, so this exact central
frequency is -e/2. The retained degree-e polynomial and (5) quantify
its actual cost, including every growing e=o(N) by (5a).
A defect of order N is a macroscopic source phase. Its bound in (5)
is not subexponential. At nonunit anchor radii,
the real part of each logarithmic factor derivative need not be 1/2;
(8)-(9) are not an exclusion theorem for complex critical points on
deformed contours.

There are two necessary limitations for the actual conjecture.
First, the original clocks range across O(N), so a balance defect
need not satisfy e=o(N); (5a) then gives no subexponential
comparison. Second, a nonzero polynomial with a large norm can
pair to zero with the exterior source. Equations (5)-(7) do not give
a scalar lower bound after that pairing. A global theorem controlling
defects and preserving the geometric contribution remains necessary.

The coefficient identities are independently audited in
[the defect-jet audit](../experiments/audit_charged_star_triangle_defect_jets.py).
The separate exact source fusion note gives the full-length reproducing
kernel and the consequent contraction of the original closure adapters.
No new broad-class volume theorem is asserted here.
