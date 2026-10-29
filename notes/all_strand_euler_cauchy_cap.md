# An exact Euler/Cauchy source formula for arbitrary braid index

27 October 2026. The original pivotal source of an arbitrary braid can
be expressed as a sum of the universal two-leg Euler coefficient
functionals. This is not a restriction to two-strand knots: the ENTIRE
actual braid word is retained, including all transitions between the
tail summands. Its diagonal blocks are extracted only after that word
has been multiplied. The formula works at every original root and
retains the full external peripheral and framing line.

This extends [the two-leg cap theorem](actual_euler_cap_cauchy_boundary.md)
using [the actual flat Borel fusion](actual_borel_regular_fusion_and_divided_cap_period.md).
It provides an exact finite source transform, not yet a geometric
relative-period map or a volume estimate.

## 1. Decompose the closed tail, keeping the first source untouched

Fix Q of exact order N>=2 in characteristic zero and put

    F_a=(Q;Q)_a, 0<=a<N.

On b physical strands use the actual nilpotent balanced Borel heads

    K_i e_a=x_i Q^(-a)e_a,
    F_i e_a=(1-Q^(a+1))e_(a+1), a<N-1,
    F_i e_(N-1)=0.

The original closed braid has the same marked color x on every
strand. Unequal x_i below are allowed for the algebraic source formula;
they do not assert that the same-color braid operator can be assigned
arbitrary new colors. In the application x_i=x=-M/q at the fixed
actual root q^2=Q.

For the closed tail T=V_2 tensor ... tensor V_b define

    K_T=product K_i,
    f_T=F_2+K_2^-1 F_3+...+K_2^-1...K_(b-1)^-1 F_b,
    Y=product_(i=2)^b x_i.

If b=2 this tail is already one N-dimensional head, of color y=x_2.
For b>=3 the proved regular fusion identifies T with

    A_0 tensor R^(N^(b-3)),
    A_0=<H,f | H^N=1, Hf=Q^-1 fH, f^N=0>.

Let t index its N^(b-3) copies and let j=0,...,N-1 index the right
idempotent in f^a e_j. For lambda=(t,j), use the NORMALIZED basis

    w_(lambda,a)=f_T^a(e_0 tensor e_(j-sum(t) mod N) tensor e_t)/F_a.

The explicit triangular fusion theorem proves that these are a basis
of the actual physical tail. No change to the first head, its input
e_0 or its output row ell=ones^t occurs. Direct application of K_T,f_T
gives

    K_T w_(lambda,a)=y_lambda Q^-a w_(lambda,a),
    f_T w_(lambda,a)=(1-Q^(a+1))w_(lambda,a+1),
    y_lambda=Y Q^-j,                               (1)

with the last arrow zero. Thus

    T=direct_sum_lambda W_(y_lambda),
    number of lambda=N^(b-2).                     (2)

All basis denominators F_a are nonzero actual root units. Formula (2)
is a decomposition for the Borel action; it does not presume a
decomposition for the full quantum-group action or diagonalize the
braid word.

## 2. Why the original pivotal closure splits exactly

Let S_T be the just specified tail basis change. The original product
of its pivotal operators is EXACTLY

    G_T=product_(i=2)^b K_i^(1-N)=K_T^(1-N).

Consequently its conjugate under S_T is block diagonal, with blocks
K_(y_lambda)^(1-N). This is why the original weighted partial trace,
rather than an invented trace, splits over these heads.

Let W be the COMPLETED actual braid operator, including all its
original local crossing lines. Form

    W'=(I tensor S_T^-1) W (I tensor S_T),
    W_(lambda,mu):V_1 tensor W_mu -> V_1 tensor W_lambda.

The full word must be formed before taking W_(lambda,lambda).
Off-diagonal transitions between tail heads during its multiplication
contribute to those diagonal blocks. Discarding them earlier changes
the invariant.

The actual word intertwines total K and F. Those total operators are
block diagonal in (2), so every DIAGONAL block W_(lambda,lambda)
commutes with their action on V_1 tensor W_lambda. Write C_lambda
for the actual two-leg fusion. It identifies that tensor product with
the free regular left A_0 module. Therefore uniquely

    C_lambda^-1 W_(lambda,lambda) C_lambda=R_(a_lambda), (3)

where R_a denotes RIGHT multiplication by a in A_0. For example
a_lambda is computed by applying the left side to the algebra unit.
The matrix C_lambda depends on x_1, not on y_lambda: in
f=F_1+K_1^-1 F_2, the second K root enters only the normalized
total weight, not its lowering arrows.

Let chi_W be the original external line, including full d_N(M) and
zero-framing factors, if they are not already included in W. Basis
invariance of partial trace gives the exact original source identity

    P_W=chi_W sum_lambda Lambda_(x_1,y_lambda)(a_lambda). (4)

It retains the original first input e_0 and all-ones output ell.
It is valid even if some or all selected values vanish. No period
has been divided out to choose a preferred source frame.

## 3. The unequal-color cap has the same universal kernel

For two Borel heads of roots x_1 and y, the same literal physical-cap
calculation as in the equal-color theorem gives

    Lambda_(x_1,y)(f^a e_k)
       =y^(1-N) x_1^-a Q^-(k+a) F_(k+a)/F_k,
                                      if k+a<N,
       =0,                            if k+a>=N.    (5)

The second pivot supplies y^(1-N)Q^-(k+a); all a lowering arrows
forced onto its leg supply x_1^-a F_(k+a)/F_k. Relative to the
equal-root formula, this changes every cap value by the SAME factor
(y/x_1)^(1-N). Thus the already proved Euler formula applies with

    z=x_1 f,
    u(z)=sum_(a=0)^(N-1) z^a/F_a,
    v(z)=u(z)^-1 in A_0,
    J_Q(z)=1/[(1-z)(1-Qz)],
    rho_0=[f^(N-1)e_0],
    gamma_lambda=N(x_1 y_lambda)^(1-N)Q.

In particular (4) becomes the all-level theorem

    P_W=chi_W sum_lambda gamma_lambda
                rho_0[ v(Q^2 z) a_lambda u(z) ]
       =chi_W sum_lambda gamma_lambda
                rho_0[ J_Q(z) u(z)^-1 a_lambda u(z) ]. (6)

Every inverse is an honest finite polynomial in the nilpotent z.
The factor Q^2 in the first line is essential, even at an original
root. Both lines are exact source identities and include ALL original
word factors; neither is a formal geometric saddle formula.

For the original same-color b-strand word, gamma_lambda simplifies to

    gamma_(t,j)=N x^(b(1-N)) Q^(1-j).               (7)

At |x|=1 this factor has modulus N. This observation gives no bound
for the transformed word coefficients a_lambda, their Euler conjugates
or cancellation between lambda terms. The fusion and Euler maps have
not been proved uniformly well conditioned in the required norm.

The variable f in the coefficient algebra acts by LEFT multiplication
when it represents the physical TOTAL F. The a_lambda and their Euler
conjugation in (6) belong to the RIGHT coefficient algebra. Conjugating
the physical word by u(physical total F) would instead do nothing,
since that word commutes with total F. Retaining this distinction is
necessary in any subsequent physical/geometric symbol comparison.

## 4. The coefficient source is exactly a two-point divided difference

There is an exact polynomial-evaluation form of (6). First reduce the
Euler-conjugated word in the canonical free basis of A_0:

    b_lambda=u(z)^-1 a_lambda u(z)
             =sum_(k,j=0)^(N-1) b_(lambda,k,j) f^k e_j,
    B_lambda(Z)=sum_(k=0)^(N-1) b_(lambda,k,0) x_1^-k Z^k.

Then the ORIGINAL period is exactly

    P_W=chi_W x_1^(N-1)/(1-Q)
             sum_lambda gamma_lambda
                     [B_lambda(1)-B_lambda(Q^-1)].    (8)

Indeed the power series coefficients of J_Q(Z) below degree N are

    [Z^m]J_Q(Z)=(1-Q^(m+1))/(1-Q).

For the term b_(k,0), the top coefficient uses m=N-1-k, so its factor
is x_1^(N-1-k)(1-Q^-k)/(1-Q). Summing gives (8), with its sign,
normalization and actual root branches fixed. No limiting argument
or contour deformation is involved.

The canonical reduction BEFORE the two evaluations is essential.
Evaluation Z=1 is not a homomorphism from the nilpotent algebra
Z^N=0 to the coefficient field. In particular a lift changed by
Z^(N+1), which is zero in that algebra, would change the displayed
two-point difference if evaluated without first reducing it. Thus (8)
is an exact LINEAR source period of the normal form; it is not a
regular scalar-clock specialization of the root representation.

At the complex root, |1/(1-Q)|=O(N). Every explicit scalar in this
conversion has at most polynomial size on the unit-color arc for
fixed braid index. This does not bound B_lambda at its two arguments:
their coefficients are the full N-dependent transformed word, and
their differences and sum can cancel. Formula (8) supplies no
unproved nonvanishing or rigidity assumption.

There is a precise quantitative form for the ORIGINAL complete
reduced invariant. Put Q_N=exp(2pi*i/N), x_N=-exp(-pi*i/N).
For b>=3 label the heads lambda=(t,j) as in (1); for b=2 there
is one head and take j=0. Define, without dividing by any invariant,

    S_N=sum_lambda Q_N^-j
                 [B_lambda(1)-B_lambda(Q_N^-1)].     (9)

For the actual complete word every retained external crossing/framing
factor, apart from d_N, has modulus one, and |d_N(1)|=1/N.
Removing d_N to return from the full ADO period to the ORIGINAL
reduced Kashaev period gives the EXACT modulus identity

    |Kashaev_N(K)|=N/|1-Q_N| * |S_N|.               (10)

One can equivalently keep the corresponding unit phase from
chi_W, x_N and Q_N rather than pass to absolute values. It is
fixed by the original word; it has not been chosen to normalize
a new solution. Formula (10) also holds when either side vanishes.
Since N/|1-Q_N|=O(N^2), the original volume conjecture is equivalent
to the definite estimate

    (2pi/N) log|S_N| -> Vol(S^3 minus K).            (11)

Equation (11) is UNPROVED in general. It is a critical-path metric
for this exact source representation, not a derived limit theorem.
In particular (9) keeps all N-dependence of the actual transformed
word and all possible endpoint/tail cancellation. No estimate for
it follows from the polynomial size of the factors in (10).

## 5. Scope on the critical path

Formula (6) reaches arbitrary braid index and in particular actual
hyperbolic-knot words. It supplies the original finite cap with a
universal rational kernel after a specified word transform, so there
is no need to guess a double-pole weight or restrict this source
calculation to a two-strand family.

It does not identify z with the second-cut Fourier momentum p. It
does not identify the nilpotent fixed-root Borel center with the
classical geometric representation germ. It does not identify a
selected nonzero geometric cycle, prove subexponential coefficients,
or control the remaining sectors. It also does not supply a moving-q
normal extension merely by keeping M at a fixed original root.

The [exact Fourier localization](universal_resonant_fourier_source_completion.md)
places the original complete value at the resonant row. The next
critical comparison can now be posed with the ACTUAL all-strand
coefficient source (6), instead of a hypothetical unsourced density.
The [exact fusion-clock equation](actual_fusion_right_euler_clock.md)
specifies a polynomial relation of its right Euler argument to
physical clocks, with its nilpotent denominator retained.
One still needs a source-compatible geometric period transform of
that expression and the sharp regulator norm. Gates C--E remain open.

## 6. Exact and independent verification

The [original-matrix audit](../experiments/audit_all_strand_cauchy_cap.py)
and its [saved results](../experiments/all_strand_cauchy_cap_results.json)
pass on 18 signed-word cases of braid indices 2,3,4 and levels 2--5,
with 60 diagonal tail-head blocks. They independently evaluate the
original physical pivotal cap, (6) and the exact two-point formula
(8), retaining the actual
half-Cartan, framing and complete modified-dimension factors.

A separate agent reran those checks and checked the unequal-color
cap (5) on 203 basis elements at levels 2--8 and six unequal-color
tail decompositions. The theorem rests on the basis and trace proof
above; these tests check its conventions and implementation.
