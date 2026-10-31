# The actual complete circle as a positive face polynomial

30 October 2026. The complete ROOT
circle, with its original weight and literal W/pi cup normalization,
has an exact homogeneous polynomial factorization in its four face
diagonals. For EVERY original folded channel that polynomial has nonnegative
coefficients. Its local zeros enforce the original unwrapped channel
support on a modular physical-head grid. Both level parities are included.

This is local source algebra. The global face-grid measure, marked
coefficient, stationary angle balance and original relative period
are separate statements.

## 1. Exact local variables, lifts and scalar

Put N>=3, d=N-1, q=exp(pi i/N), Q=q^2, and keep an actual integer
0<=a<=floor(d/2). Write m=d-a, s=d-2a and

    beta_a=S_(2a)/S_a^2, S_j=product_(r=1)^j 2sin(pi r/N),
    k_a=1 if s=0, otherwise k_a=2.

Let x,b,c,y be the outer, incoming-middle, outgoing-middle and final
face diagonals, respectively. Choose their logarithms and use the
literal centered physical heads

    S=d/2+N(Log x-Log b)/(2pi i),
    R=d/2+N(Log x-Log c)/(2pi i),
    sigma=d+N(Log x-Log y)/(2pi i).                    (1)

The other physical heads are sigma-S and sigma-R. The auxiliary row
is r=sigma-m, with its actual complement 2a-r. Thus

    Q^S=-q^-1 x/b, Q^(sigma-S)=-q^-1 b/y,
    Q^R=-q^-1 x/c, Q^(sigma-R)=-q^-1 c/y.

The physical half-index and the auxiliary finite color are not confused.
Define, using the original Hermitian matrices H_-,H_+,

    D_a(x,z,y)=det[z I+(x/2)H_-+(y/2)H_+],
    Ptilde_s(x,y)=product_(j=a+1)^(d-a)(x-Q^j y).       (2)

The empty determinants and products are one. Then the full coefficient
of the specified regular root complete-circle source is EXACTLY

    h0_a W_a pi_a
      =k_a beta_a^2
         D_a(x,b,y) D_a(x,c,y) Ptilde_s(x,y)/(bc)^(d/2). (3)

This is the fixed-root Hopf lift from the
[original source envelope](actual_original_network_resonant_source_envelope.md),
not a newly chosen off-grid continuation of a canceled exceptional
kernel. A retained half twist multiplies (3) by its original fixed
scalar omega_a^epsilon. Every power in (3) uses the logarithms in (1).

If one adds literal N-lifts to R,S,sigma, the multiplier is
(-1)^[d(n_R+n_S)]. The degree lift n_sigma cancels. It is identically
one at odd N; at even N it must be retained or canceled by a proved
global source-character calculation. Formula (3) makes no independent
wrapping of an out-of-basis head.

## 2. Proof from the literal large white and cups

At the root the actual white and dual are

    W_a(i,j;r)=(-1)^m q^[-dr+di-m(m-1)] H_m^1(Q^i,Q^j)/F_m,
    i+j=m+r, F_m=(Q;Q)_m,
    pi_a(r;i,j)=gamma_a^-1 p_(2a)(2a-r)
       W_a(d-j,d-i;2a-r)/[pV(d-j)pV(d-i)].

Here gamma_a=q^(2-a^2)/N^2 is FIXED, h0_a=k_a N beta_a,
pV(z)=N q^(-d^2+dz), and no paired norm pi_a W_a is inverted.
The exact Chevalley factor is
W_a(d-j,d-i;2a-r)=q^[s(a-r)]W_a(i,j;r).

Let T=Q^sigma and P_s(T)=product_(j=a)^(m-1)(T-Q^j).
The exact root reflection of the SPECIFIED factorial section gives

    p_(2a)(d+a-sigma)
          =F_s q^[2m(d+a)] T^-a/P_s(T).                (4)

Indeed p_(d-s)(z)=F_s exp(pi i z)q^[(s-1)z]
/product_(j=1)^s(1-Q^(z+j)); substitute z=d+a-sigma and retain
exp(pi i z)=q^(Nz) literally. This proves (4) before canceling its
possible poles. The root identities H_m=H_a P_s and

    H_a(U,V)=V^a K_a det[I-(qU/2)H_--(q^-1/(2V))H_+],
    K_a=q^(a^2) beta_a,

are source-exact finite polynomial identities.

For comparison with the previously normalized entire circle C_a,
substitution in the preceding literal W/pi expression gives the same
head factor q^[d(R+S-2sigma)]/P_s(T) as in C_a. Its remaining
scalar ratio is one: use

    F_j=(-i)^j q^[j(j+1)/2] S_j, S_(d-j)=N/S_j.

The ratio reduces to q^[-2N(-2N+a+3)]=1. This proves h0_a W_a pi_a=C_a
as the specified meromorphic root functions, not just at physical nodes.
It does not identify their moving-q germs with a different generic lift.

Now use the exact original normalized coefficient

    C_a=k_a V_a(d-sigma) q^[d(R+S-sigma)-2a^2]
                  H_a(U_o,V_o)H_a(U_i,V_i)/T^a,
    V_a(h)=product_(j=a+1)^m 2sin(pi(h+j)/N).

On the logarithms (1), direct factorization gives

    V_a(d-sigma)=Ptilde_s(x,y)/(xy)^(s/2),
    H_a(-q^-1 x/z,-q^-1 z/y)=(-q^-1)^a K_a y^-a D_a(x,z,y),
    q^[d(R+S-sigma)]=(xy/(bc))^(d/2).                 (5)

For the first identity, the scalar in the sine product is
i^s q^[-sum_(j=a+1)^m j]=i^s q^(-sN/2)=1.
The remaining powers of xy cancel because d=2a+s, and
K_a^2 q^(-2a^2)=beta_a^2. This proves (3) with its exact scalar.
The same formulas show that additional N-lifts contribute
(-1)^[d(n_R+n_S)+(s-d)n_sigma]=(-1)^[d(n_R+n_S)], since s-d=-2a.

## 3. Coefficient positivity and homogeneity

D_a is homogeneous of degree a in x,z,y and has NONNEGATIVE REAL
coefficients. This follows directly from the actual positive matrices,
without assuming their entries are real. Factor H_-=B_-B_-* and
H_+=B_+B_+*, and apply Cauchy--Binet to the rectangular matrix

    [sqrt(z) I, sqrt(x/2) B_-, sqrt(y/2) B_+].

Its determinant expansion is a sum of squared absolute minors times
the indicated monomials, hence has the claimed coefficients. Since all
three source matrices I,H_-,H_+ are positive definite, every homogeneous
monomial of degree a in the three variables in fact has positive
coefficient: subtract a sufficiently small positive multiple of I
from each matrix, then select the three identity parts in the same
Cauchy--Binet expansion. This is a coefficient statement for each
fixed N,a; no uniform lower coefficient bound is claimed.

More strongly, the retained forced product has the exact positive
expansion for EVERY original folded label:

    Ptilde_s(x,y)=sum_(j=0)^s [S_s/(S_j S_(s-j))] x^(s-j)y^j. (7)

To prove it, multiply its finite linear factors, or induct on their
number, to obtain the coefficient
(-1)^j Q^[(a+1)j+j(j-1)/2] [s choose j]_Q.
The exact finite Gaussian coefficient is
[s choose j]_Q=q^[j(s-j)] S_s/(S_j S_(s-j)).
The remaining q exponent is
j[2a+2+j-1+s-j]=j(2a+1+s)=jN.
Its factor q^(jN)=(-1)^j cancels the displayed sign. This proves
(7), whose coefficients are strictly positive because s<N. It also
retains both maximal-fold parities: Ptilde=1 at odd simple fold and
Ptilde=x+y at even maximal fold. No quarter-channel restriction is needed.

The numerator in (3) is consequently a homogeneous polynomial of
degree 2a+s=d with nonnegative coefficients in the four face variables.
The monomial denominator and all finite logarithmic carries are still
part of the source. Evaluating some face variables at complex values
does not preserve positivity of the resulting specialized coefficients.

## 4. Local modular support retains one forced zero

Take physical heads i,j in {0,...,d}, sigma=i+j. In the original white
the unwrapped auxiliary row is r=sigma-m, so its actual allowed range
is 0<=r<=2a, equivalently

    m<=sigma<=d+a.                                    (6)

At U=Q^i,V=Q^j, every Newton summand of H_a has factors forcing
k<=i and a-k<=j. Therefore H_a(Q^i,Q^j)=0 if sigma<a.
Exact root complementation sends the pair to (d-j,d-i), proving
the same vanishing if sigma>2d-a.

The complete circle retains ONE factor P_s(Q^sigma) after (4)
cancels one of the two factors from its large numerators. Hence:

* If sigma<m, either sigma<a and the small numerator vanishes,
  or a<=sigma<m and the retained P_s vanishes.
* If sigma>d+a, either sigma>2d-a and the complementary small
  numerator vanishes, or sigma-N belongs to [a,m-1] and P_s vanishes.

These are zeros of the canceled entire root coefficient, not an
assignment of a value to an unexplained 0 times infinity. Thus a
modular auxiliary residue outside its original support is killed
locally even though its individual continued channel cup may have
a pole.

If both physical pairs of a circle survive and their totals agree
modulo N, both totals lie in the SAME interval (6), containing only
2a+1<=N integers. They therefore agree exactly. The auxiliary row is
then the original unwrapped row. The complementary physical cup
also adds no modular states: i+j congruent to d modulo N with
0<=i,j<=d forces i+j=d, since d-N<0 and d+N>2d.

This local check supplies the missing support input for a possible
global face-grid transformation. The global primitive measure,
even-level coset and carry phases, original marked-cap monomial and
coefficient-extraction identity still require their own proof.

Focused audit: [literal circle, coefficients and support](../experiments/audit_actual_complete_circle_positive_face_polynomial.py),
with [saved results](../experiments/actual_complete_circle_positive_face_polynomial_results.json).
At 85 digits it checks 94 literal LARGE-white/dual/cup circle identities
and 22 retained N-lift characters, with maximum source error below
4.6e-83. Independent continuant expansions check 79 original D polynomials
and their 823 strictly positive coefficients; 522 forced-product
coefficients check the all-label sine-binomial formula. Exact finite-field
checks retain 6910 forbidden physical-pair zeros, 28211 circle zeros for
unequal totals congruent modulo N, 5274 supported unwrapped pairs and
150 original physical-cup modular support identities. Three symbolic
calculations check the phase, outer degree and centered mark exponents.
No numerical global source transformation is asserted by this audit.

The local modular support uses the one forced factor that remains after the cup cancellation.

The global face grid, marked coefficient and exponential rate are separate from this local source statement.