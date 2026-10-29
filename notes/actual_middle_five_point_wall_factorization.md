# The literal middle five-point configuration and its actual crossing factor

Research note, 28 October 2026. The middle five-point certificate in
[the classical crossing cycle, Section 3](crossing_fundamental_cycle.md)
is

    +partial(a,b,p,p_1,s_M), p_1=a p, s_M=a s_0.  (1)

This note puts those **actual shared quantum flags** in an explicit
canonical frame, identifies one of its tetrahedral arguments in an
exact factorization of the original crossing, and gives a corrected
finite reciprocal-coordinate transition with its original source.
The transition has an unavoidable spectral projector. Its omitted
term has a nonzero pairing in an actual one-crossing cup network.

This is not a full five-factor quantum realization of (1). It does
give a literal configuration, factor and correction against which
such a realization can be checked. In particular, scalar auxiliary
region flags cannot remove the determinant wall: a rank identity
below proves this for every generic choice of that flag.

## 1. A finite two-factor decomposition of the original crossing

Use the original balanced matrices from
[the shared quantum flags note](actual_shared_quantum_flags_and_charged_exchange.md).
Let P be the original finite Euler polynomial

    P(A)=sum_(h=0)^(N-1)(-1)^h Q^(h(h-1)/2)A^h/F_h,
    F_h=(Q;Q)_h, Q=exp(2pi*i/N).

The original uncheck crossing is R_0=D P(e_1 f_2), including its
original Cartan diagonal D. Its common scalar Cartan line kappa
remains external throughout; the full checked crossing is
kappa times flip R_0. Neither its framing nor its peripheral
normalization is changed.

Choose any cyclic completion S_2 of the actual raising shift.
Since f_2=(1-Z_2)S_2 is already the original nilpotent F_2,

    R_0=D P(-e_1 Z_2 S_2) P(e_1 S_2)             (2)

is an exact identity at every level N and every pair of nonzero
colors. Indeed put A=e_1S_2, B=-e_1Z_2S_2. Then BA=QAB,
so the finite binomial identity gives P(A+B)=P(B)P(A).
Every apparent product term of total degree >=N contains e_1^N
and vanishes. Thus no root specialization of separate infinite
compact products is involved. The cyclic wrap in S_2 cancels
in A+B and (2) is the original crossing, not a cyclic replacement.

The individual factors in (2) are nilpotent Euler kernels with
exact finite coefficients. They are not asserted to be single
nondegenerate basic matrix dilogarithms.

## 2. An exact canonical frame for the actual five flags

Now take complete colors x=-q^(-1), lambda=x^(-1)=Qx,
k=x^N=(-1)^(N-1), and the typed marks

    S_1^N=mu, S_2^N=k mu.

As in the shared-flag note let

    G_1=[[K,e],[fK,2lambda-QK]],
    a=(1,S_1)^t, b=(1,t_2)^t,
    t_2=f_1+K_1^(-1)S_2.

These are the fixed flags of the actual shared meridians H_1
and H_2. Choose the same Gauss auxiliary flags as the classical
calculation: p=(0,1)^t and s_0=(1,0)^t. Keep their images as
homogeneous columns:

    p_1=G_1p=(e_1,2lambda-QK_1)^t,
    s_M=G_1s_0=(K_1,f_1K_1)^t.                  (3)

No inverse of e_1 is used. Set

    Z=Z_1, Y=-ZS_1, X=x S_2S_1^(-1),
    L=[[Y,0],[-S_1,1]].                          (4)

All these frame factors are units, and

    XZ=QZX, X^N=Z^N=1.

The five original columns have the following exact form:

| Original flag F | Canonical column F_c | Retained right tag R_F in LF=F_c R_F |
| --- | --- | --- |
| a | (1,0)^t | Y |
| b | (1,1-X)^t | Y |
| p | (0,1)^t | 1 |
| p_1 | (1-Z,1)^t | lambda |
| s_M | (1,1)^t | YK_1 |

For example (t_2-S_1)Y^(-1)=1-X,
Y e_1=lambda(1-Z), and
(2lambda-QK_1)-S_1e_1=lambda. These prove the table
by multiplication. Thus it is the literal middle configuration
of (1), with every right normalization retained. A projective
coordinate such as (1-Z)^(-1) is not asserted to exist in the
finite module: its homogeneous column is what the table gives.

This frame is uniformly controlled at unit marks. If |mu|=1,
then S_1,Y,K_1 and lambda are unitary. The norm of L and
L^(-1) is the golden ratio (1+sqrt(5))/2; each right tag has
norm and inverse norm one. The frame neither diagonalizes all
five flags nor uses the generally exponential full coherent
Fermat basis. These assertions therefore do not contradict
the previously calculated exponential coherent-frame norms.

## 3. Its classical boundary and an actual tetrahedron factor

In the commutative limit the five flags of the table are

    (a,b,p,p_1,s_M)=(0,1-X,infinity,(1-Z)^(-1),1).

Put H=X+Z-XZ. In the exact cross-ratio convention of the
classical certificate, the omitted-vertex tetrahedra have

| Omitted vertex j | Cross-ratio r_j | Boundary sign |
| --- | --- | --- |
| a | H/[X(1-Z)] | + |
| b | 1/(1-Z) | - |
| p | X/H | + |
| p_1 | X | - |
| s_M | H | + |

This is a direct determinant computation on those five points,
so it is precisely the middle certificate (1). The first
tetrahedron has positive quad coordinate

    1/(1-r_0)=-X(1-Z)/Z.

But the last factor of the **original crossing** in (2) has
the exact argument

    n=e_1S_2=(Q-Z^(-1))X, n^N=0.                (5)

Its classical symbol is exactly -X(1-Z)/Z. Hence a genuine
tetrahedron of this specific certificate, not a freely chosen
auxiliary atom, occurs in (2). The tetrahedron omitting b has
positive quad coordinate Z. The boundary is equivalently

    [n_cl]-[Z]+[X/H]-[X]+[H]=0.                 (6)

Equation (6) is the classical statement. At the quantum level
neither X, Z, nor the homogeneous columns alone authorize
replacing the whole right factor in (2) by five uncorrected
cyclic dilogarithms.

## 4. Two explicit issues in a naive quantum lift

For the usual cyclic pentagon center pattern, a classical
parameterization of (6) is U=1-Z,V=X, with

    1-U+UV=H,
    -UV/(1-U)=n_cl,
    V/(1-U+UV)=X/H.

Its left centers are X and (1-X)(1-Z)=1-H. Applying the
ordinary complement relation gives exactly (6). But its
literal quantum candidates do **not** form a quantum torus:

    X(1-Z)-Q(1-Z)X=(1-Q)X !=0.                 (7)

Thus simply substituting the classical five-point coordinates
in the generic cyclic pentagon is false. A scalar root phase
or retained numerical multiplier does not remove (7). This
does not rule out a nonlinear quantum change of coordinates
with additional face factors; it locates the change that is
needed for this actual configuration.

The reciprocal coordinate also has a precise finite correction.
The would-be expression (1-QZ)^(-1)X cannot exist as a right
solution to (1-QZ)U=X, since 1-QZ has a kernel and X is a
unit. Let E_d be the Z=Q^(-1) spectral projector, and define
the finite group inverse

    H_Q(Z)|j>=1/(1-Q^(j+1))|j> (j<d),
    H_Q(Z)|d>=0,
    U=H_Q(Z)X.

Then exactly

    UZ=QZU, U^N=0,
    (1-QZ)U=X-E_dX.                              (8)

The projector in (8) is compulsory. It is not permission
to replace the generic reciprocal coordinate by U without
transporting the right-hand side as well.

## 5. An explicit corrected transition in the original crossing

There is a closed factorial gauge, rather than an unknown
similarity, connecting (5) to the regularized primitive (8):

    Gamma|j>=g_j|j>,
    g_j=(-1)^j Q^(-j(j-1)/2)F_j^2,
    Gamma n Gamma^(-1)=U.                       (9)

Here Gamma acts on the first actual head. To prove (9), use
X|j> proportional to |j-1> on the first head. For 1<=j<N,
the coefficient of n is Q(1-Q^(-j)) times that of X,
whereas the coefficient of U is 1/(1-Q^j) times that of X.
The required ratio is precisely

    g_j/g_(j-1)=-Q^(1-j)(1-Q^j)^2.

Both operators have zero arrow at j=0. This proves every
entry, including the wrap, independently of parity and mu.
Consequently the original crossing has the exact refactor

    R_0=D P(-e_1Z_2S_2) Gamma^(-1)P(U)Gamma.    (10)

Equations (8)--(10) give a corrected finite coordinate change
at a tetrahedron of the literal middle five-point configuration,
with every factor of the original R specified. They do not
yet give the entire five-factor quantum identity for (6).

Gamma is not a negligible unit. At complex roots,

    g_j=Q^j|F_j|^2.                              (11)

Its absolute weights are positive, but generally exponential
in N. For example the already proved factorial estimate in
[the coherent-frame note](actual_four_line_fermat_crossing_and_conditioning.md)
gives log||Gamma||=2gamma_*N+O(log N) and
log||Gamma^(-1)||=2gamma_*N+O(log N), with
gamma_*=Vol(4_1)/(4pi)>0. Thus the explicit frame contributes
at the scale being studied. It must stay in the period.

The same factorial square appears numerically in the existing
degree-d Rogers cap row: at completeness its entries satisfy
mu_r=x^(d+r)g_r/N^2. This does not cancel Gamma here. The
Rogers index belongs to the relative fusion frame, whereas
(9) acts on the original physical clock. A fusion comparison
must carry the actual matrix and all of its sources before
identifying those two diagonals.

## 6. Original source and the nonzero omitted wall

Keep the original complete cup and full marked cap

    p=N sum_(a=0)^d x^(a-d)|a,d-a>,
    m|a,b>=x^b/N^2, mp=1.

The unstripped common scalar line is kappa. The checked
crossing B with kappa external obeys Bp=p. Directly,

    Xp=Q^(-1)p,
    m E_d X Bp=Q^(-1)/N.                        (12)

For the full crossing the second value is
kappa Q^(-1)/N, with its same exterior framing and
peripheral factors. Thus (8)'s correction is visible in
an actual one-crossing source contraction, not only in an
arbitrary matrix entry.

The five-point canonical frame also has its literal right
source tags. At the a and b vertices put p'=Yp and
m'=mY^(-1). Then

    Xp'=p', m'p'=1, m'E_dXp'=1/N.               (13)

The Q phase in (12) has therefore not been discarded; (13)
is the correctly typed changed source. Under the further
factorial transition (9), use Gamma p and mGamma^(-1).
Their pairing is again one. Neither vector can be replaced
by the old vector individually in (10).

The cap still has its original affine charge
(J_1+J_2+1)p=Np. The corrected clock transition (8) has
not been identified with the internal integer edge winding
of a positive Pachner move. Its projector and source tags
are exactly part of what that identification must transport.

### Endpoint wall removal preserves every original knot exponent

There is an unconditional, quantitative boundary consequence.
Let C_N be the actual cut operator of any knot, with its
original exterior scalar normalization retained. Its Hopf
intertwining implies C_N=K_N I: commuting with the original
K forces a diagonal matrix, and commuting with the original
F, whose consecutive arrows are nonzero, makes all diagonal
entries equal. This argument holds at every N and at the
complete color, without an asymptotic or a Schur hypothesis.
Consequently

    m E_dX(C_N tensor I)p=Q^(-1)K_N/N,
    m(1-E_dX)(C_N tensor I)p=(1-Q^(-1)/N)K_N.    (15)

The scalar in the second line satisfies

    1/2 <= |1-Q^(-1)/N| <= 3/2  (N>=2).

Thus removal of this projector at the **marked endpoint**
preserves the limsup and liminf of N^(-1)log|K_N|; the
normalized logarithms change by at most (log 2)/N. This
removes this specific boundary normalization issue without
assuming a volume conjecture or a noncancellation statement.
The wall itself has exactly the same exponential rate as
K_N, with the polynomial factor 1/N, and cannot be declared
exponentially suppressed.

The boundary sewing algebra is equally explicit. For any
integers r,s and clock indices j,k,

    E_jX^r E_kX^s=delta_(j,k-r) E_jX^(r+s),
    m E_jX^r(C_N tensor I)p=Q^(-r)K_N/N.         (16)

Thus a fixed specified endpoint sewing word has an exact
finite coefficient multiplying the original scalar. A claim
that an **interior** five-point wall has moved to that
endpoint must still prove its current/source transport.
Equation (15) alone supplies neither that transport nor a
comparison with a separately selected geometric saddle.

## 7. A generic scalar auxiliary flag cannot remove this wall

The obstruction is not caused by choosing p=infinity. Let
P=(r,s)^t have scalar entries and ell_P=(-s,r). The original
complete meridian has the factorization

    G-lambda=(1,S)^t(K-lambda)(1,-S^(-1)).

Since ell_P P=0, it follows exactly that

    ell_P G P=(rS-s)(K-lambda)(r-S^(-1)s).       (17)

For a generic scalar flag both outer factors are units;
for example, r=1 and s^N!=mu. The middle factor has
rank N-1. Hence the determinant between P and GP is
singular of rank N-1 for **every** such generic scalar
auxiliary choice. Inverting it inside the original finite
module is impossible. This rules out repairing the naive
generic five-point field construction merely by moving a
scalar auxiliary flag.

This is a specific obstruction to that construction, not
to a relative quantum five-point period. A valid continuation
can retain a normal variable and the projector/source in
(8), or add a genuine quantum auxiliary module with its
originally specified reduction. It must then prove that
the resulting combined five-factor product gives (10)
with its typed source. Neither (7) nor (14) excludes that
possibility. No such complete product or geometric saddle
coefficient is asserted here.

## 8. The actual unwrapped-period coordinates match these flags

The [actual cyclic/Hardy graph](actual_cyclic_hardy_dilog_network.md)
uses S_i as multiplication by z_i and Z_i=B_i as the shift
f(z_i)->f(Qz_i). In that realization the same dictionary is
literal:

    X=x z_2/z_1, Z=B_1,
    n=(Q-B_1^(-1))X=q Ecal_1 z_2.               (18)

Here Ecal is the actual rho^2 E. Indeed at completeness
Ecal_1=z_1^(-1)(B_1^(-1)-1), and -xQ=q. All homogeneous
frame identities of Section 2 and (5) use only these Weyl
relations and the complete color. They therefore hold on
that actual graph as well, before selecting its root center.

The central powers must be distinguished. On the unwrapped
graph, X^N=x^N z_2^N/z_1^N is a variable central
multiplication operator. On the typed finite heads used in
Sections 2 and 6, S_2^N=k S_1^N gives X^N=1. That is a
source/period restriction, not an identity in the unwrapped
Laurent algebra. Equation (18) supplies the operator
dictionary but does not prove its source pushforward or
equate a central root value with a semiclassical shape.

## 9. Exact audit

Run

    python3 experiments/audit_actual_middle_five_point_wall.py

This checks 28 original-R factorizations (2), 21 typed
five-point frames and corrected factorial transitions,
and 21 generic scalar-flag rank obstructions, over exact
prime fields for N=2,...,8. It includes (12)--(13), both
wraps, the actual original coefficient evaluator, and the
full input cup. The all-level proofs above are finite
identities; these tests are independent diagnostics.
