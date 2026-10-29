# Complete-color divided Ward operators and the exact fusion ghost

Research theorem, 27 October 2026. At the complete integral color,
the first normal of a vanishing N-th quantum power gives a nonzero
divided Ward action. Its tensor fusion correction is one finite
unipotent exponential, with nilpotence bounded by strand number.
Ordinary closure kills this correction. A specified one-wrap,
relative cut-current test can detect it, but no identification of
that test with the selected global geometric class is asserted.

All formulas below are proved from finite matrices. In particular
no extension of a generic typical meridian color to a divided-power
quantum group is presumed.

## 1. The genuine complete integral color

Fix N>=2 and m=N-1. Initially q is generic, Q=q^2, rho=q-q^(-1).
On the ordinary integral Weyl color D_m(q) use the divided-F basis
v_a=F^(a)v_0, 0<=a<=m. Its literal matrices are

    K v_a=q^(m-2a)v_a,
    E v_a=[m-a+1]_q v_(a-1),
    F v_a=[a+1]_q v_(a+1),                      (1.1)

with arrows outside the range absent. For r>=0,

    E^(r)v_a={m-a+r choose r}_q v_(a-r),
    F^(r)v_a={a+r choose r}_q v_(a+r),            (1.2)

when the target exists, and zero otherwise. Braces denote symmetric
Gaussian polynomials. Formula (1.2) follows by multiplying adjacent
entries and dividing by [r]_q! over the generic field; its resulting
Gaussian polynomial is integral. Thus E^(N)=F^(N)=0 on each color
identically in q.

The finite generic-q R matrix of this actual color is

    R_uncheck=D sum_(r=0)^m
          q^(r(r-1)/2) rho^r E^r tensor F^r/[r]_q!,
    D=q^(H tensor H/2).                         (1.3)

It is regular near every prescribed q_N=exp(pi*i/N). Indeed its
r-th nilpotent coefficient can also be written
q^(r(r-1)/2)rho^r[r]_q! E^(r) tensor F^(r). The recorded Cartan
half-character remains on its chosen cover.

For completeness, its E intertwining does not need a literature
proof. From the matrices one gets

    [E,F^r]=[r]_q F^{r-1}
                 (q^(1-r)K-q^(r-1)K^(-1))/rho.

Likewise [E^r,F]=[r]_q E^{r-1}
(q^(r-1)K-q^(1-r)K^(-1))/rho; these are ordinary powers
in both commutator formulas and follow by induction from the
generator matrices.

Conjugating by D reduces the R intertwining equation to the
recursion c_(r+1)=c_r q^r rho/[r+1]_q for the coefficients of
E^r tensor F^r. This is exactly (1.3). The last unmatched term
has E^(m+1)=0. Consequently checked R commutes with Delta E
and Delta K. The F calculation uses the second displayed
commutator and the same coefficient recursion. It also commutes
with the iterated total actions on any tensor power. Inverses have
the same property. All identities are generic
q matrix identities before root specialization.

## 2. The tensor divided-power formula, including its order

On b tensor factors put

    C_E=Delta^(b-1)E=sum_(i=1)^b A_i,
    A_i=E_i K_(i+1)...K_b.

For i<j one has A_i A_j=Q A_j A_i. The ordinary q-multinomial
formula, proved by multiplying one additional factor, therefore
gives the following integral matrix formula:

    C_E^n/[n]_q!
      =sum_(n_1+...+n_b=n)
          q^(sum_(i<j)n_i n_j)
          tensor_i [E_i^(n_i)K_i^(n_1+...+n_(i-1))]. (2.1)

Terms with n_i>N-1 are zero. The order E^(n_i) before K powers
is part of the formula. On two factors this reads

    Delta E^(n)=sum_(r=0)^n q^(r(n-r))
                       E^(r) tensor E^(n-r)K^r.  (2.2)

Thus the tensor divided power is regular at q_N even when
[n]_q! vanishes. For b>=2 it is nonzero at n=N. For example
on v_(N-1) tensor v_1 only the r=N-1 term of (2.2) survives;
its output v_0 tensor v_0 has nonzero coefficient.

Every actual braid word commutes with (2.1): this holds generically
by commutation with C_E, and extends through the root because
both matrices are regular. This is a genuine complete-color root
Ward action invisible in the equality C_E(q_N)^N=0.

## 3. Exact first-normal normalization and the scaled matrix

Set Ecal=rho^2 E, C=rho^2 C_E. The polynomial matrix

    D_n(q)=C(q)^n/(Q;Q)_n

is regular near q_N for every n. Formula (2.1) proves this because

    D_n=rho^(2n)q^(-n(n-1)/2)(1-Q)^(-n) C_E^n/[n]_q!.

The entire divided matrix C_E^n/[n]_q! is interpreted by (2.1).
No zero factorial is separately evaluated.

In particular define

    J_b=[C(q)^N/(1-Q^N)]_(q=q_N).

Since (Q;Q)_(N-1)=N at the root,

    D_N(q_N)=J_b/N.                              (3.1)

The corresponding unscaled conversion is

    [C_E^N/(1-Q^N)]root
      =q_N^(-N(N-1)/2)N/(1-Q_N)^N
                          *[C_E^N/[N]_q!]root.  (3.2)

For Q=Q_N(1+epsilon), along the complete integral color,

    C(Q)^N=-N epsilon J_b+O(epsilon^2).           (3.3)

For q=q_N(1+h) the coefficient is -2N h J_b instead. These
are specified normalizations, not unnamed scalar multiples.

In the balanced basis used by the actual cut, at the root

    Ecal_(a,a+1)=Q_N^(-a-1)-1,
    K_aa=x Q_N^(-a), x=q_N^(N-1).

The unique mixed term on w_(N-1) tensor w_1 gives the useful
normalization check

    J_2(w_(N-1) tensor w_1)=-N q_N w_0 tensor w_0. (3.4)

It is nonzero at every level, including even and composite N.

## 4. The general-b fusion correction is one finite exponential

For any argument z define the positive-argument finite polynomial

    f_N(zX)=sum_(r=0)^(N-1) z^r X^r/(Q_N;Q_N)_r.

The actual negative factorial convention is obtained by z=-t.
Order the tensor factors as f_N(zA_b)...f_N(zA_1). The finite
q-multinomial identity before specializing gives exactly

    product_(i=b,...,1) f_N(zA_i)
        =sum_(n=0)^(b(N-1)) z^n D_n(q_N).        (4.1)

One way to see regularity on its right is its identical generic-q
ordered product on the left: each A_i^N=0 identically.

For 0<=r<N, Gaussian multiplication gives

    D_(kN) D_r={kN+r choose r}_Q D_(kN+r).

The scalar Gaussian tends to one, directly from its r product
factors. Thus D_(kN+r)=D_(kN)D_r at the root. Also

    D_N^k=k! D_(kN),                            (4.2)

because {kN choose N}_Q tends to k: all nonmultiple product
ratios tend to one, and the final ratio
(1-Q^(kN))/(1-Q^N) tends to k. Equivalently
(Q;Q)_(kN)/(1-Q^N)^k tends to N^k k!.

Combining these exact identities gives the full factorization

    product_(i=b,...,1) f_N(zA_i)
        =exp(z^N J_b/N) f_N(zC).                 (4.3)

The exponential is finite. For the literal negative series this
is exp((-t)^N J_b/N), so an odd-N sign is not suppressed.

Let position mean the ordinary integer sum a_1+...+a_b. Then
J_b lowers position by exactly N. Hence J_b^b=0, more precisely
its nilpotence index is at most floor(b(N-1)/N)+1. The defect
exp(z^N J_b/N)-I has only lowering degrees kN. Actual checked R
preserves position exactly, so its conjugates preserve this
bounded lowering filtration. The group generated using only such
positive lowering defects is unipotent, independently of N for
fixed b. No analogous claim for both raising directions is made.

## 5. Ordinary closure kills the ghost, while one normal wrap can pair

Let P lower total position by at least N, and let R_left,R_right
preserve total position. Weighted pivotal partial trace over all
but one strand kills R_left P R_right. Every closed-strand input
index equals its output index, so the remaining cut would have
to lower its index by at least N; its index range has only N values.
This is a term-by-term zero, independent of the diagonal pivotal
weights. Thus every positive term of (4.3) is invisible to ordinary
one-cut closure, including after actual braid transport.

A single missing edge W=E_(N-1,0) raises position by N-1. A
single such normal insertion can therefore leave a lowering-one
cut current from J_b. All higher powers J_b^k, k>=2, are still
killed by one-cut partial trace after one wrap. Pairing with a
specified cut cochain that raises one can then have degree zero.
This is a permission by degree, not a nonvanishing theorem for
an arbitrary global source.

There is a universal literal nonzero example. For b=2 let
W_tot=W tensor K+I tensor W and take the actual pivotal trace
over the second color. Then

    [ptr_2(J_2 W_tot)]_(0,1)=delta N x^(2-N),
    delta=(-1)^(N-1), x=q_N^(N-1).              (5.1)

Only the closed input index zero with its second-leg wrap
contributes. The coefficient follows from the unique mixed
divided term. It is nonzero for every N.

An even simpler formulation uses the true divided Hopf adjoint,
which is described next. Both are local normal-cochain tests,
not identification with the selected global relative class.

## 6. The true divided Hopf-adjoint Ward action and its SL2 block

On End(D_m(q)) put

    A_E(X)=ad_Ecal(X)=[Ecal,X]K^(-1),
    A_F(X)=ad_F(X)=F X-K^(-1)X K F.

These are generic-q Hopf actions on matrices. The correct divided
operators are

    J_E^ad=[A_E^N/(1-Q^N)]root,
    J_F^ad=[A_F^N/(1-Q^N)]root.                 (6.1)

They are not commutators with the individual divided matrix,
which is zero. For example write
A_E=U+V, U=L_Ecal R_(K^-1), V=-R_(Ecal K^-1).
Then UV=Q VU and U^N=V^N=0 identically. The same divided-binomial
calculation proves the regularity in (6.1). The F version uses
the inverse parameter Q^(-1).

Let W=E_(N-1,0) and U_0=sum_(a=0)^(N-2)E_(a,a+1). Directly
from these mixed terms, in the actual balanced root basis,

    J_E^ad(W)=-N U_0, J_E^ad(U_0)=0,
    J_F^ad(U_0)=N W, J_F^ad(W)=0.               (6.2)

For the first equation, the term with r=N-1-a left E actions
and s=a+1 right E actions is the only one contributing to
E_(a,a+1). Root product cancellation gives coefficient -N for
each a. Similarly

    J_F^ad(E_(a,a+1))=-N Q_N^(-a-1)W,

whose sum gives N W. Thus the two-dimensional span of W,U_0
is invariant, and -J_E^ad/N,J_F^ad/N are opposite standard
nilpotents generating SL2 on it. Both divided directions do
not generate a nilpotent group. The bounded unipotence in
Section 4 is specifically the one-direction relative defect.

The actual E-Ward cut primitive B=E_(1,0)/(Q_N^(-1)-1) satisfies

    [Ecal,B]=E_(0,0)-E_(1,1),
    Tr(B J_E^ad(W))=-N/(Q_N^(-1)-1)!=0.         (6.3)

This is a specified nonzero pairing of a divided normal current,
the actual missing edge, and a relative cut cochain. It does not
prove that the original global selected source has this class.

Ordinary pivotal partial trace with pivot K intertwines these
divided Hopf adjoints before specializing: it intertwines A_E,
A_F, their powers and scalar divisions, all by the actual Hopf
cap identities. Regularity then gives the root divided map.
At the complete root, the ADO pivot K^(1-N) differs on each
individual color by the scalar delta, so it has the same root
equivariance. This is the correct divided Ward naturality; replacing
it by ad_(J_b) would lose the mixed terms just computed.

## 7. The two normal directions and the actual auxiliary family

On the generic-M balanced auxiliary array the last raising formula
before root specialization is

    w(Q,M)=M Q^(-N)-M^(-1)
          =(Y-Z)/(M Z), Y=M^2, Z=Q^N.          (7.1)

It equals kappa=M-M^(-1) only on the root wall Z=1. The genuine
complete integral color is instead

    x=q^(N-1), M=-q^N, Y=Z,

and (7.1) vanishes identically on that path. At the root crossing
of the two walls,

    w=(Y-1)-(Z-1)+higher order.

For Q=Q_N(1+epsilon), fixed Y gives dw=-N epsilon; the integral
path has dlog Y=N epsilon and gives dw=0. Thus its normal
derivative is partial_epsilon+N partial_(log Y), not the prior
fixed-meridian q-normal derivative.

The precise failure of the generic auxiliary matrices to be a
genuine off-root Hopf module is visible without any deformation
theory. With actual truncated matrices one computes

    [Ecal,F]-rho(K-K^(-1))
       =-(1-Q^N) w(Q,M) E_(N-1,N-1).           (7.2)

It vanishes on either the root wall Z=1 or the complete integral
color wall Y=Z. This keeps the coupled boundary source explicitly;
it does not extend generic typical colors to the divided-power
theory by assumption.

The off-root boundary closure also has an adapter. On complete
integral color the genuine ordinary pivot is K. The auxiliary ADO
pivot is K^(1-N), with ratio

    K^(-N)v_a=q^(-Nm+2Na)v_a.

At q_N it is delta I. Its q-logarithmic first derivative is the
nonconstant diagonal N(2a-m), multiplied by delta. The ordinary
and ADO twists have ratio q^(-Nm); this too must be differentiated
if the closed q-normal sources are compared. For a zero-framed
b-strand knot of writhe ell, the exact routewise adapter is

    q^[Nm(ell-b+1)+2N sum_(closed legs) a_j].      (7.3)

It is one at the root by ell=b-1 modulo two, but its derivative
contains the recorded closed-position moment. Therefore equality
of root invariants does not identify their off-root source jets.

## 8. Scope

The complete integral-color divided Ward action, finite fusion
exponential, bounded positive lowering filtration, ordinary closure
cancellation, and explicit relative normal tests are proved here.
The true divided Hopf-adjoint diagram is also an exact actual
matrix construction.

The remaining source-survival theorem still requires a map from
the partially contracted actual geometric current module to this
marked relative cut module, preserving (7.1)--(7.3). The nonzero
local tests (5.1), (6.3) do not supply that map or its global
coefficient. No global cycle, Stokes, regulator norm, or volume
limit is inferred.

[Exact audit](../experiments/audit_complete_color_divided_ward.py).
[Results](../experiments/complete_color_divided_ward_results.json).
[Independent divided-bridge audit](divided_ward_bridge_independent_audit.md).
[Independent two-normal and pivotal-adapter audit](ward_source_localization_independent_audit.md).
