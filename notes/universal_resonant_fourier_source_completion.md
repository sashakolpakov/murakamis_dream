# Exact complete localization of the original first-slot Fourier source

Research theorem, 27 October 2026. At an actual root, the first-slot
cut in the [universal resonant presentation](universal_resonant_cut_and_actual_source.md)
has the exact ORIGINAL finite Fourier array

    J_(a,j)(1)=P_N(1) delta_(j,0)                     (1)

for EVERY physical first input a. This includes the original all-ones
output row, the original pivotal caps, twists and full peripheral
dimension line. No division by P_N and no nonvanishing assertion
are used. The result is a consequence of the actual Hopf rows,
rather than an approximation by the geometric principal density.
In fact the entire channel obeys L(X_j)=P_N X_j at completeness,
as proved below; this is stronger than the selected scalar rows.

Consequently the regular Fourier labels j!=0 have zero selected
finite value at completeness. A nonzero local geometric formal block
at those labels does not establish that it contributes to the original
period. The resonant value P_N remains to be evaluated. In particular,
(1) supplies neither its volume exponent nor a new scalar formula
independent of the original word.

## 1. The actual channel and its source

Fix N>=2, q=exp(pi*i/N), Q=q^2, and retain the original meridian M.
In the balanced head put

    B=diag(Q^a), K=x B^-1, x=-M/q,
    F_(a+1,a)=1-Q^(a+1),
    Ecal_(a-1,a)=M Q^(-a)-M^-1.                       (2)

All missing entries are zero. Ecal is the fixed scalar multiple
of E used in the actual balanced crossing conventions. Its
coproduct and antipode have the same form as those of E.

Cut a braid at its FIRST physical slot between two actual words
A and Bword; both words intertwine the true iterated coproduct.
The original second-cut coupon X defines the actual linear channel

    L(X)=d_N theta^(-w) ptr_g[ A (X tensor I) Bword ]. (3)

Here ptr_g closes every strand except the original first open strand
using g=K^(1-N), in the original order. The displayed external
factors may instead be recorded in their original external line;
the SAME convention must then be used for P_N and J throughout.
The universal presentation inserts a word P and its literal inverse,
so A Bword is exactly the original braid operator. It changes none
of the factors in (3), including their actual rational-map/lattice
specializations.

The [root scalar-closure proof](actual_one_index_fourier_source_and_ward_reduction.md),
Section 1, gives

    L(I)=P_N(M) I.                                   (4)

There is an elementary version of that proof: the cut commutes with
K and F; the distinct K eigenvalues make it diagonal, and its F
commutator makes successive diagonal entries equal because
1-Q^a!=0 for 0<a<N. Thus no generic irreducibility or division by
an unknown scalar period is needed. With the full line in (3),
P_N=d_N F_N; with that line recorded externally, P_N=F_N. At M=1,
F_N(1) is the fixed original Kashaev invariant.

Set ell=1^t, and use the actual root Fourier projectors

    X_j=V^-1 E_(j,j) V,
    (X_j)_(b,d)=Q^[j(d-b)]/N,
    V_(j,b)=Q^(jb), 0<=j<N.

The original one-index Fourier source is EXACTLY

    Y_j=L(X_j),  J_(a,j)=ell Y_j e_a.                 (5)

This follows by expanding the second-wire conjugation and retaining
the all-ones first output row. Since sum_j X_j=I, (4) gives

    sum_j J_(a,j)=P_N                                (6)

for every a. The 1/N in X_j is the Fourier inverse. There is no
additional exterior factor in (6).

## 2. Why the first-slot channel intertwines the actual Hopf adjoint

For the actual coproduct convention,

    Delta Ecal=Ecal tensor K+1 tensor Ecal,
    Delta F=F tensor 1+K^-1 tensor F,
    S(Ecal)=-Ecal K^-1, S(F)=-K F.

The induced action on an endomorphism is

    ad_K X=K X K^-1,
    ad_Ecal X=(Ecal X-X Ecal)K^-1,
    ad_F X=F X-K^-1 X K F.                           (7)

For the FIRST tensor factor, direct substitution in the coproduct
gives

    ad_h^(total)(X tensor I)=(ad_h X) tensor I,
                         h=K,Ecal,F.                (8)

For example the Ecal commutator is [Ecal,X] tensor K_other,
which becomes [Ecal,X]K^-1 tensor I after multiplying by the
total K^-1. For F the extra term cancels as

    K^-1 X tensor F_other
      -K^-1 X K K^-1 tensor F_other=0.

This verifies the position requirement. An arbitrary later-slot
embedding is not substituted for (8).

Multiplication on either side by an actual braid intertwiner
commutes with (7). The original pivotal partial trace is also an
adjoint intertwiner. One can check the latter directly, without
assuming scalarity: on the closed tensor factor write K_o,E_o,F_o
for its total generators and g_o for its original product pivot.
At the actual root,

    [g_o,K_o]=0,
    g_o E_o g_o^-1=K_o E_o K_o^-1,
    g_o F_o g_o^-1=K_o F_o K_o^-1.

Weighted partial-trace cyclicity cancels the closed-factor terms
in (7), using precisely these identities. The remaining terms
are ad_h of the partial trace. Equivalently these are the direct
evaluation/coevaluation identities checked in
[the closed-braid construction](closed_braid_period_line.md),
Section 2. Scalars d_N and theta^(-w) commute with this calculation.
Consequently

    L(ad_h X)=ad_h L(X), h=K,Ecal,F.                  (9)

Equations (8)--(9) apply to the literal cut of any word of the
specified equal original color, not only to an inverse-pair
example. The inverse-pair construction is what simultaneously
provides this first slot and the desired noncommuting geometric
meridian while preserving the original selected period.

Everything so far is an ACTUAL root identity. It makes no
off-root q scalarity or compressed auxiliary Hopf assertion.

## 3. Complete cyclic generator formulas

Let S be the cyclic raising shift S e_a=e_(a+1 mod N). The Fourier
projectors satisfy

    S X_j=X_j S=eta_j X_j, eta_j=Q^j,
    B^-1 X_j B=X_(j+1).                              (10)

All Fourier labels in this note are cyclic. At M=1 the missing
physical endpoints in (2) have zero coefficients. Therefore, as
exact finite matrices,

    F=S(I-QB), Ecal=S^-1(B^-1-I).                    (11)

There is no replacement of a nonzero endpoint by a cyclic arrow.
Substituting (10)--(11) into (7) gives

    ad_K X_j=X_(j+1),
    ad_Ecal X_j=x^-1 eta_j^-1
                         (Q^-1 X_(j+1)-X_j),
    ad_F X_j=eta_j X_j-eta_(j-1) X_(j-1).           (12)

For instance [S^-1(B^-1-I),X_j]B has its two X_j B terms
cancel; the remaining terms are
eta_j^-1(Q^-1 X_(j+1)-X_j). For the F row, the two S B terms
cancel by B X_j=X_(j-1)B. These prove all formulas in (12)
within the original finite balanced head.

The first row of (12) and (9) imply

    Y_(j+1)=B^-1 Y_j B.                              (13)

In particular their diagonal entries are independent of j. Summing
(13) and using (4) proves (Y_j)_(a,a)=P_N/N. This latter identity
also holds for generic M and will retain the full scalar period
in the endpoint equation below.

## 4. Highest-input localization, followed by all-input propagation

First take the actual input a=0. Since Ecal e_0=0 and
ell Ecal=ell(B^-1-I) at M=1, (13) gives

    ell (ad_Ecal Y_j)e_0
                  =x^-1[J_(0,j+1)-J_(0,j)].

Apply (9) to the Ecal row of (12) and compare the two expressions.
The resulting exact scalar recurrence is

    (eta_j-Q^-1)J_(0,j+1)
                       =(eta_j-1)J_(0,j).           (14)

At j=0 its right side is zero and 1-Q^-1 is a unit, so J_(0,1)=0.
For j=1,...,N-2 the coefficient eta_j-Q^-1 is nonzero, and
induction gives J_(0,j)=0 for every j!=0. Equation (6) then gives
J_(0,0)=P_N. This proof never divides by P_N and remains valid
when the original invariant vanishes.

For every physical input a, use (13), the F row of (12), and
F e_a=(1-Q^(a+1))e_(a+1). They give

    (1-eta_j)J_(a,j)
      =(Q^(a+1)-Q^-1 eta_j)J_(a,j-1)
                  +(1-Q^(a+1))J_(a+1,j-1).          (15)

At a=N-1 the last term is zero; it is not an added cyclic
physical-input column. The candidate P_N delta_(j,0), constant
in a, satisfies (15). Subtract it and call the difference D.
The result just proved is D_(0,j)=0 for all j. If D_(a,j)=0
for all j and a<N-1, (15) forces

    (1-Q^(a+1))D_(a+1,j-1)=0.

Every coefficient is a unit. Induction in a proves D=0, which is
the stated theorem (1). The proof also works at M=-1, since then
Ecal=-S^-1(B^-1-I); its extra common sign cancels in (14).

There is a useful full-matrix corollary. Define the Fourier rows
r_k=ell B^-k, which form a basis of the dual head. By (13),

    r_k Y_j=ell Y_(j+k) B^-k
           =P_N delta_(j+k,0) r_k.

Directly from (5), r_k X_j=delta_(j+k,0)r_k as well. Hence

    L(X_j)=P_N X_j,                                  (19)
    L(h(S))=P_N h(S)

for EVERY element h(S) of the finite cyclic-shift algebra. This
identity also uses no nonzero-period assumption. It concerns this
commutative subalgebra of coupons, not the full endomorphism
algebra or the generic-M channel.

## 5. The meridian endpoint and word data are retained off completeness

Keep the actual root Q but allow M to vary. Put

    kappa=M-M^-1, W=E_(N-1,0).

The exact finite Ecal matrix is

    Ecal=S^-1(MB^-1-M^-1 I)-kappa W.                 (16)

The last term subtracts the cyclic arrow at the original physical
endpoint. It is nonzero off completeness. The F row, K row,
(13), (15) and (Y_j)_(0,0)=P_N/N remain exact. Define the ACTUAL
inserted endpoint source

    R_j=ell L([W,X_j]B)e_0.                          (17)

Repeating the preceding Ecal calculation with (16) gives

    M(eta_j-Q^-1)J_(0,j+1)
      +(M-M^-1 eta_j)J_(0,j)
                 =kappa eta_j(P_N/N-R_j).           (18)

Indeed the cyclic part of ad_Ecal X_j is
x^-1 M eta_j^-1(Q^-1 X_(j+1)-X_j), while its missing-arrow
correction is -x^-1 kappa[W,X_j]B. On the output side,
ell Ecal=ell(MB^-1-M^-1 I)-kappa e_0^t. This proves (18),
including both its original scalar source and its actual inserted
endpoint source. Deleting (17) before differentiation would alter
the original meridian normal equation.

There is no universal generic-M profile determined by P_N alone
for all original words. The exact finite-field audit includes the
same first-slot inverse-pair cut on the one-positive-crossing
unknot and positive trefoil. At N=3, M=3 over F_157, their
highest rows divided by their respective NONZERO full periods are

    unknot:  [117,62,136],
    trefoil: [52,122,141].

Both sums are one modulo 157. The different rows disprove such a
universal rational identity across these original words; this is
not a separate claim about all hyperbolic knots or about a
particular complex asymptotic boundary profile. It records why
the whole word/source in (17)--(18) cannot be replaced by a
knot-independent cap simply because (1) holds on the complete
fiber.

## 6. Critical-path consequence and verification

On this actual source-preserving cut ALL of the selected complete
finite period is at j=0. Thus the nonzero geometric normal block
on a regular p!=1 chart is not yet a nonzero image of the final
selected scalar source: the complete finite rows at j!=0 vanish
exactly. Sampling their nonzero geometric principal coefficient
and summing it is not an evaluation of the actual finite array.

The remaining issue is a source-compatible geometric transform
of the resonant row and its whole endpoint/peripheral completion,
not proving that an unspecified regular Fourier row survives.
Its regulator exponent, subexponential coefficient and global
norm estimate are still unproved in general. The current theorem
does not close C, D or E of
[the critical-path audit](critical_path_to_original_volume_conjecture.md).

The [exact original-matrix audit](../experiments/audit_universal_resonant_fourier_source.py)
checks every matrix unit against all three Hopf-adjoint generators,
the generic-M endpoint equation (18), all-input equation (15),
complete delta localization and full matrix projector identity (19). Its
[saved results](../experiments/universal_resonant_fourier_source_results.json)
report PASS on 36 signed-word/cut cases at N=2,...,6, comprising
598 matrix input units and three generator checks per unit.
The full d_N, original pivots and twists are retained in every
case. These finite tests support the direct proof above; they
are not used as a proof for untested knots or as an asymptotic
estimate.
