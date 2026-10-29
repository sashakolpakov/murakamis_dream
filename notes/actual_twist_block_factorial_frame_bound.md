# A factorial-frame bound for complete original twist blocks

28 October 2026. An explicit normalized **physical** Borel fusion and its
exact inverse improve the uniform twist-block estimate. For absolute
constants C,A, every N>=2 and every integer ell satisfy

    ||B_N^ell||_op <= C N^A(1+|ell|) exp(12 gamma_* N),
    gamma_*=-integral_0^(1/6)log(2sin(pi t))dt.           (1)

The same holds for HS norm with one additional factor N. Here B_N is
either actual complete crossing with its original Cartan/root framing
line; those complete scalar factors have modulus one. No arbitrary
condition number is removed. Every fusion metric cost is bounded in
the original balanced flat norm, and the common Cartan is kept on the
meridian continuation used in the proof.

In volume units 24pi gamma_*=12v_3, where v_3 is the regular ideal
tetrahedron volume. The preceding independently checked bound
2pi log(7+5sqrt(2)) in
[the convex block note](actual_convex_gauge_block_energy.md) remains
valid; (1) is a sharper result, with a separate explicit-frame audit.
Neither bound is the sharp knot-volume theorem.

The later [joint projector-profile theorem](actual_twist_block_projector_barrier.md)
improves 12v_3 further to 4v_3+2v_8 by maximizing the coupled projector
interval profile. It uses the exact physical frames and source
continuation established here; the coarser proof below is unchanged.

The subsequent [joint projector estimate](actual_twist_block_projector_barrier.md)
sharpens the volume constant further to 4v_3+2v_8. It uses the SAME
physical frames, source and meridian-circle argument below, but
maximizes the complete projector factorial profile together. The
independent bound (1) and its proof remain valid.

## 1. The actual normalized fusion and inverse

Fix q=exp(pi i/N), Q=q^2, d=N-1, F_a=(Q;Q)_a. Continue the original
meridian M near one and set x=-M/q, Y=M^2. On each balanced physical
head use the literal matrices

    K|a>=x Q^(-a)|a>,
    F|a>=(1-Q^(a+1))|a+1>,
    Ecal|a>=(M Q^(-a)-M^(-1))|a-1>, Ecal=rho^2 E.

Missing endpoint arrows are zero. This is the original nilpotent
N-color meridian family; it is not a generic cyclic representation.
The total lowering operator is

    f=F_1+K_1^(-1)F_2, f^N=0.

For total integer degree T, set I_T=[max(0,T-d),min(T,d)]. The actual
free Borel fusion columns are f^a|0,T-a>. Normalize each by its
nonzero physical factorial F_a. In the basis |u,T-u> this gives

    C_T(u,a)=x^(u-a) F_(T-u)/[F_(a-u)F_(T-a)], u<=a,
    C_T(u,a)=0 otherwise.                             (2)

These are triangular matrices with diagonal one. Expanding f^a by
the finite Q-binomial theorem proves (2) directly. Their exact inverses
are

    C_T^(-1)(u,a)=(-1)^(a-u)Q^((a-u)(a-u-1)/2) C_T(u,a). (3)

Indeed (2) factors as
diag_u(x^u F_(T-u)) times the upper Euler-Toeplitz matrix
(1/F_(a-u)) times its inverse diagonal. The inverse Euler coefficients
are (-1)^h Q^(h(h-1)/2)/F_h. This proves (3) for arbitrary nonzero M,
not only at the complete root. In particular both matrices have the
SAME entrywise moduli. All normalized factorials and powers of M in
these physical frames are retained.

## 2. The sharp elementary factorial cost of this frame

Write

    J(s)=integral_0^s log(2sin(pi t))dt.

The already proved endpoint-uniform factorial estimate gives
log|F_a|=N J(a/N)+O(log N) uniformly in 0<=a<N. On the triangle
u,v>=0, u+v<=1,

    max [J(u+v)-J(u)-J(v)]=2gamma_*.                   (4)

To check (4), fix s=u+v. The expression is strictly concave in u:
its second derivative is
-pi sin(pi s)/[sin(pi u)sin(pi(s-u))]<0.
The maximum has u=v=s/2. Its derivative in s is
log(2cos(pi s/2)), so s=2/3 is the unique maximum. Its value is
-3J(1/3)=-2J(1/6)=2gamma_*; the last identity follows by integrating
the sine doubling formula and using J(1-s)=-J(s).

Every entry of (2) is a Q-binomial coefficient times x^(u-a).
Equations (2)--(4) therefore prove, uniformly on |M-1|<=1/(8N^3),

    ||C_T||, ||C_T^(-1)|| <= C_0 N^A0 exp(2gamma_*N).   (5)

The factor |x|^(u-a) is uniformly bounded there, and converting max
entry to norm costs at most N. The bound is uniform in the integer
degree T. Thus the full physical fusion condition number costs
exp(4gamma_*N+O(log N)). It has not been declared subexponential.

## 3. A literal bidiagonal Casimir in this normalized frame

Use the actual normalized tensor Casimir

    Omega=F_tot Ecal_tot+qK_tot+q^(-1)K_tot^(-1),
    Ecal_tot=Ecal_1K_2+Ecal_2, K_tot=K_1K_2.

It commutes with f. Direct application to the seed vector gives

    Omega|0,j>=c_j(Y)|0,j>
                 +(M Q^(-j)-M^(-1)) f|0,j-1>,
    c_j(Y)=q^(-1)Y Q^(-j)+qY^(-1)Q^j.                 (6)

For example the first physical offdiagonal term before rewriting is
(M Q^(-j)-M^(-1))(1-Q)|1,j-1>. Subtracting that same multiple of
f|0,j-1> leaves the Cartan diagonal c_j(Y); this verifies (6) without
inverting an endpoint coefficient.

Commuting Omega through f^a and retaining the normalizer F_a gives

    C_T^(-1) Omega C_T |a,j>
       =c_j(Y)|a,j>+b_j(M)|a+1,j-1>,
    j=T-a,
    b_j(M)=(M Q^(-j)-M^(-1))(1-Q^(T-j+1)).             (7)

Targets outside the physical basis are omitted. In particular when
j=0 the formal coefficient M-M^(-1) need not vanish away from
completeness; |a+1,-1> is absent by the original endpoint convention.
At a=d the displayed factor 1-Q^N genuinely vanishes. Thus
(7) is an actual finite bidiagonal matrix, denoted H_T(M), valid
also at the complete collisions. It uses no cyclic head completion.

The actual generic-meridian crossing polynomial, derived from its
finite highest-weight matrix in
[the meridian Casimir note](meridian_casimir_source.md#1-the-fixed-operator-and-its-generic-meridian-spectrum),
has eigenvalue

    lambda_j(Y)=nu_j Y^(-j),
    nu_j=(-1)^j q^(j(j+1)), |nu_j|=1.                  (8)

This is the original crossing with the explicit common Cartan scalar
recorded separately. Equations (2),(7),(8) identify its complete
degree block by similarity, rather than merely comparing its spectrum.

The finite-matrix verification of (8) is short. At total degree j write
a highest vector h_j=sum_(a=0)^j beta_a |a,j-a>, beta_0=1.
Its actual Ecal equation gives

    beta_(a+1)/beta_a
      =-e_(j-a)/[e_(a+1)xQ^(-(j-a-1))],
    e_a=M Q^(-a)-M^(-1).

For generic M these denominators are nonzero. Multiplying cancels
the e factors and gives beta_j=(-1)^j x^(-j)Q^(j(j-1)/2).
The coefficient of |0,j> in the checked R h_j comes only from the
zero-transfer term on |j,0>, so its eigenvalue is beta_j x^(-j),
which is exactly (8). The N descendants of each h_j are nonzero
generically by the elementary E F^r recurrence; f^N=0. Distinct
c_j(Y) make these N summands independent and their dimensions total
N^2. The defining finite R commutes with the actual total generators,
so this computes the whole generic crossing, not just selected entries.

## 4. Explicit interval projectors with only one possible collision

Fix nonnegative physical degrees r<=s from the j-interval of H_T.
For generic M its c_j(Y) are distinct. The j-to-k bidiagonal spectral
projector E_k has entry, from column s to row r,

    (E_k)_(r,s)=
       product_(l=r+1)^s b_l(M)
          /product_(l=r,l!=k)^s [c_k(Y)-c_l(Y)]
                                  if r<=k<=s,
    (E_k)_(r,s)=0 otherwise.                         (9)

One proof expands the triangular resolvent:
[(z-H_T)^(-1)]_(r,s)=product b_l/product_(l=r)^s(z-c_l),
then takes the residue at c_k. This proves the full matrix formula,
including intervals touching a physical endpoint.

The exact factorization of each difference is

    c_k(Y)-c_l(Y)
      =qY^(-1)(Q^k-Q^l)[1-Y^2 Q^(-(k+l+1))].          (10)

The first product of differences in (10), for l in [r,s], l!=k,
has absolute value exactly |F_(k-r)F_(s-k)|. Its reciprocal is at
most exp(2gamma_*N+O(log N)).
The additional common factor |qY^(-1)|^(s-r) is not exactly one
on the later meridian circle, but its logarithm is O(N delta)
there and it is uniformly bounded above and below.

For the second product the integers k+l+1 form an interval of length
at most N, inside [1,2N-1], with the entry l=k omitted. There is at
most ONE zero at M=1: k+l+1=N. If this is the omitted entry, there
is no zero. This explicitly includes the simple self-paired node
when N is odd and the near-endpoint nodes when N is even.

After removing this possible zero and the omitted entry, the root
product is a circular interval product of 1-Q^m. It is a ratio of
factorials, or two such ratios when the interval crosses N. Its
leading logarithm is the difference of two endpoint values of J;
J(1)=0 accounts for the crossing. Hence that product AND its reciprocal
are at most exp(2gamma_*N+O(log N)). Omitting one additional nonzero
factor changes the bound only by O(log N), since

    4/N <= |1-Q^m| <=2, 1<=m<N.

This is a whole-product estimate; multiplying N separate polynomial
bounds is not used.

## 5. The shrinking meridian circle retains all normalizers

For any integer ell choose

    delta=1/[8N^3(1+|ell|)], M=1+delta exp(i theta).    (11)

All c_j(Y) are distinct on this circle: the other solutions of
M^4=Q^m are a distance of order 1/N from one, while delta is smaller.
For a nonzero root factor the relative change in its logarithm is
O(delta/|1-Q^m|). Summing around a full interval costs at most

    O(delta N(1+log N))=O(1),

because |1-Q^m|>=4min(m,N-m)/N. Thus the noncolliding product bound
in Section 4 remains uniform on (11); there is no N^O(N) loss.
The possible zero factor has magnitude
|1-M^4| >=3delta, since |M^3+M^2+M+1|>=3 on this small circle.
Its reciprocal costs at most C N^3(1+|ell|).

The numerator of (9) has two interval products. At M=1 their moduli are

    |F_s/F_r|,
    |F_(T-r)/F_(T-s)|,

where all indices lie in [0,d]. Each has leading exponent at most
2gamma_*N. Neither numerator interval contains a root-zero factor.
The same harmonic-sum comparison preserves those bounds on (11).
The factors M^(-1) in the first numerator product and qY^(-1)
in each denominator difference contribute only exp(O(N delta))
over the complete intervals; they are retained on both sides.
Combining them with BOTH denominator products proves, for all entries
and degrees,

    |(E_k)_(r,s)|
        <= C_1 N^A1(1+|ell|) exp(8gamma_*N).            (12)

The eigenvalue powers in (8) are uniformly bounded on (11):
|M^(-2j ell)| <= exp(4N|ell|delta) <2.
Summing the at most N projectors and converting max entry to operator
norm costs only a further polynomial. Combining with (5) gives

    ||B_N(M)^ell||
        <= C_2 N^A2(1+|ell|) exp(12gamma_*N)             (13)

on the entire circle, in the ORIGINAL physical metric.

The full original common Cartan has not disappeared. On the retained
branch alpha=d+Log M/Log q it is

    kappa(M)=q^(alpha^2/2),
    kappa(M)/kappa(1)
       =M^d exp[(Log M)^2/(2Log q)].                   (14)

Its ell-th power has modulus bounded by
exp(2N|ell|delta+C N|ell|delta^2), uniformly less than a fixed constant.
Thus (13) holds for the unstripped crossing too, with its SAME original
Cartan. The original framing scalars at M=1 have modulus one. There
is no color-dependent factor chosen from a knot period here.

Finally every actual signed crossing power is holomorphic near M=1:
the finite defining R and its inverse have only the constant nonzero
factorials F_a and powers of nonzero M as denominators. The apparent
spectral poles in (9) cancel in the full matrix. Cauchy's formula at
the center of (11), with the full matrix and Cartan retained, bounds
its norm by the maximum norm on that circle. This proves (1). The
circle integral introduces no extra delta^(-1) factor, since dM and
the Cauchy denominator have the same radius.

## 6. Source-preserving whole-word consequence and scope

The bound concerns a coherently contracted actual twist block before
any absolute values. It can replace that block inside any original
braid or plat, of arbitrary width, without changing a cap, pivot,
modified-dimension factor, marked source or framing line. Therefore
the preceding block-energy argument, on consecutive repeated-generator
blocks of the specified original braid word, improves to

    limsup_N (2pi/N)log|P_N|
       <=sum_twist blocks min(|ell|v_8,12v_3).          (15)

The original reduced Kashaev scalar has the same bound. Blocks and
width are fixed while N tends to infinity. The estimate is uniform
in ell as stated in (1), but the whole-word asymptotic uses a fixed
braid word. The strict comparison 12v_3<4v_8 makes every consecutive
repeated-generator block of length at least four improve its
separate-crossing bound. No tangle conversion of an arbitrary unoriented
diagram twist region is asserted. This is still a
coarse repeated-generator-block upper bound, not an estimate by Vol(S^3-K), a
nonzero selected geometric coefficient or the volume conjecture.

The strict constant comparison needs no numerical volume premise.
For G=sum_(n>=0)(-1)^n/(2n+1)^2, G>8/9. The elementary Fourier series
of the sine integral gives

    v_3=(3sqrt(3)/4)sum_(k>=0)
                [(3k+1)^(-2)-(3k+2)^(-2)].

The decreasing positive summand bounds its tail from k=1 by its
first value plus its integral, so that sum is at most
3/4+9/400+1/60. Together with sqrt(3)<7/4 this gives v_3<10/9.
Since v_8=4G>32/9, one obtains 3v_3<10/3<32/9<v_8,
which proves 12v_3<4v_8 rigorously.

Explicitly, this whole-source bound also holds at ODD braid width.
For the original b-strand complete cut, retain the unitary pivot g
and the original unit zero-framing correction in W. The exact cut
identity is C=Tr_env[W(I tensor g^(tensor(b-1)))]=K_N I. Therefore

    |K_N| <= N^(b-1)||W||_op
      <= N^(b-1) product_t min(||B_sign(t)||_op^|ell_t|,
             C N^A(1+|ell_t|)exp(12gamma_*N)).          (16)

The first inequality follows directly by summing the N^(b-1)
environment diagonal matrix elements and applying the operator norm.
No positivity premise for the pivotal trace is required. The full
ADO state differs at completeness by its retained root phase/N.
Thus (16) includes all original source factors in modulus and gives
(15) for either parity of braid width, without relying only on the
even-plat notation of the gauge construction.

## 7. Independent actual-matrix audit

    python3 experiments/audit_actual_twist_block_factorial_frame.py

The audit evaluates the generic-meridian R directly from the finite
E^h tensor F^h sum, independently of the spectral reconstruction.
It checks the normalized physical fusion, its explicit Euler inverse,
the bidiagonal Casimir intertwining, every interval-projector entry,
the difference factorization and the one-collision count, all physical
degree endpoints, signed powers and the full Cartan continuation.
Fresh result: **PASS**, 240 signed meridian/degree families through
N=9, including both level parities.
[Saved results](../experiments/actual_twist_block_factorial_frame_results.json).

The new bound's exponential constants come from the uniform analytic
product proof, not extrapolation of those finite tests. The previous
Hermite norm theorem is left intact as an independent coarser bound.
