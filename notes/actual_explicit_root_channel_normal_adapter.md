# An explicit root-channel adapter for the first-normal defect

30 October 2026. The genuine first
quantum defect of the original off-node boundary functional is an
explicit function of TWO root-channel insertions. The adapter has
polynomial norm O(N^2) on the actual boundary scale. It retains the
full open root channel, not just its scalar closure z.

This is a finite-source identity at every N>=2 and arbitrary fixed
Morse width. It gives neither a bound for the root-channel norm nor
the coefficient of a geometric relative period.

## 1. The actual family and its divided descendants

Fix N>=2, d=N-1, q=q0 exp(epsilon), q0=exp(pi i/N), Q=q^2.
The highest weight d and the physical indices remain FIXED. Use

    F e_a=(1-Q^(a+1))e_(a+1), 0<=a<d, F e_d=0,
    K e_a=q^d Q^(-a)e_a,
    ad_F X=FX-K^-1 X K F, ad_K X=KXK^-1.              (1)

Let C_e be a holomorphic family of linear maps on End(V_d), commuting
with these ACTUAL generic adjoints, and suppose

    C_e(I)=z(e)I.                                     (2)

The original routed channel
C_e(X)=P_V[A U^-1(X tensor I)U B] satisfies these hypotheses with
the original generic pivot g=(-1)^d K, actual endpoints and all
peripheral factors; the [braided source/current theorem](actual_braided_residual_framing_current.md)
includes rectangular cuts and arbitrary fixed width. No bare root
mark is made covariant, and no routed U band is omitted here.
Only K and F covariance is needed in the proof below.

For 0<=s<=d put

    h_s(q)=(-1)^s Q^[s(s+1)/2] {d choose s}_Q,
    {d choose s}_Q=product_(j=1)^s (1-Q^(N-j))/(1-Q^j).

For -d<=n<=d let s0=max(-n,0), and define the n-th-band matrix

    V_n(q)_(s+n,s)=h_s(q)/h_s0(q)
       whenever 0<=s,s+n<=d; all other entries are zero.  (3)

All h_s(q0)=1, by 1-Q0^(N-j)=-Q0^(-j)(1-Q0^j).
Thus (3) is holomorphic near the root and V_n(q0)=T_n, the literal
unwrapped band sum sum_(r-s=n) E_rs. In particular V_-d=E_0d
and V_0=diag(h_0,...,h_d).

Here is the entire descendant calculation. The successive ratio is

    h_(s+1)/h_s=-Q^(s+1)(1-Q^(d-s))/(1-Q^(s+1)).

On a band with entries h_s, the coefficient of ad_F is

    (1-Q^(s+n+1))h_s-Q^n(1-Q^(s+1))h_(s+1)
                         =(1-Q^(N+n))h_s.             (4)

At either physical end the missing term is zero. Substitution of
the same ratio verifies (4) at the newly appearing left endpoint;
at the right endpoint h_(d+1)=0 is used only as that finite zero,
not as a new cyclic arrow. After normalizing (3), for -d<=n<d,

    ad_F V_n=c_n(q)V_(n+1),
    c_n=1-Q^n       if n<0,
    c_n=1-Q^(N+n)   if n>=0.                          (5)

In particular c_0=1-Q^N vanishes at the root. It is canceled
GENERICALLY, before taking root values. Equivalently, with
F_k=product_(j=1)^k(1-Q^j),

    (ad_F)^(d+n) E_0d
                  =F_(d+n) sum_s (h_s/h_d) E_(s+n,s).
                                                               (6)

For d+n>=N, (6) cancels the common factor in F_(d+n); it never
divides a specialized zero matrix by a root zero. This explains the
positive-band descendants without replacing the physical endpoint.

Generic ad_K has distinct eigenvalues on the different integer
bands. Its extreme band is one dimensional, so
C_e(E_0d)=lambda(e)E_0d, with lambda holomorphic. Covariance and
the nonzero generic factors (5) imply

    C_e(V_n)=lambda(e)V_n, -d<=n<=d.                  (7)

Analytic continuation gives (7) at the root too. Since V_0(q0)=I,
lambda(0)=z(0). Thus this proof also gives C_0(T_n)=z_0 T_n
directly from regular generic K/F covariance, without an off-root
cyclic shift or an assumed interpolation.

## 2. Two literal root insertions give the first-normal defect

Write C_1=partial_epsilon C_e|0, z_1=z'(0), and
mathcal A=C_0-z_0 Id_End. Define the explicit root diagonal

    H_0=0,
    H_s=2N sum_(j=1)^s 1/(1-Q0^j),
    H=diag(H_0,...,H_d).                              (8)

This is the genuine derivative h'_s(q0). Indeed differentiating
the product for h_s gives
s(s+1)+sum_j[2N/(1-Q0^j)-2j], leaving exactly (8).
In particular it keeps the derivative of Q^N; the root simplification
h_s(q0)=1 is not differentiated instead.

The derivative J_n=V'_n has entries H_s-H_s0 on its band.
Differentiating (7), and subtracting the derivative of (2) at n=0,
gives the EXACT identities

    eta I=mathcal A(H), eta=lambda'(0)-z_1,
    (C_1-z_1 Id_End)T_n
                   =eta T_n-mathcal A(J_n).           (9)

There is no unspecified scalar normal in eta: it equals any diagonal
entry of mathcal A(H), or Tr(mathcal A(H))/N.

For ANY unwrapped Toeplitz matrix X=sum_n x_n T_n, let
J(X)=sum_n x_n J_n. Since

    J(X)=XH-sum_n x_n H_max(-n,0) T_n

and mathcal A annihilates every T_n, (9) simplifies to

    (C_1-z_1 Id_End)X=eta X-mathcal A(XH).             (10)

In particular for X(p)_(r,s)=p^(r-s)/N, p!=0, the genuine defect
Delta_e(p)=C_e(X(p))-z(e)X(p) has

    Delta'_0(p)=eta X(p)-mathcal A(X(p)H),
    eta I=C_0(H)-z_0 H.                              (11)

Thus only the original ROOT insertions H and X(p)H are required,
in the SAME routed channel with its original closure. If p depends
on epsilon, the extra derivative is zero because the root defect
vanishes identically in p. No derivative of a root-only simplification
of an individual coupon has been used.

For the original coherent row e_t of trace one and its exact
b_N(t,p)=Tr[e_t X(p)], the retained scalar defect is therefore

    Tr[e_t Delta'_0(p)]
       =eta b_N(t,p)-Tr[e_t C_0(X(p)H)]
                                      +z_0 Tr[e_t X(p)H]. (12)

If b_N!=0 this may be divided by that SAME b_N. Equation (12)
does not evaluate either new root period from z. In particular it
does not introduce a second trace-one localization or remove U.

There is a useful exact check against the free pivotal channel
B_e(X)=D_e X-tau_e(X)I, tau_e(X)=Tr(g_e X), D_e=tau_e(I).
Swapping the sums in (8) gives

    sum_s Q0^(-s)H_s=-2N/(1-Q0^-1),
    tau_0(H)=-nu_N, nu_N=D'_0.

Equations (11) then give eta=nu_N and
Delta'_0(p)=nu_N[X(p)-I/N], retaining the physical trace-normal
sign. The actual N=2 odd-braid family in the current theorem shows
that these additional open data cannot generally be replaced by z.

## 3. The exact Plancherel bound

Center H by its scalar mean: tildeH_s=H_s-N^-1 sum_r H_r.
Both (9) and (10) are unchanged, since mathcal A(I)=mathcal A(X)=0.
Set

    R_N^2=N^-1 sum_s |tildeH_s|^2.

This variance has a finite exact Fourier formula. With
hat f_k=sum_s f_s Q0^(-ks), define the cyclic difference
b_s=H_s-H_(s-1 mod N). Then b_0=-N(N-1) and
b_s=2N/(1-Q0^s) for s>0. Pairing s with N-s gives
sum_(s>0)(1-Q0^s)^-1=(N-1)/2. The successive differences of
sum_(s>0)Q0^(-ks)/(1-Q0^s) are -1 for 1<=k<N, hence

    hat b_k=-2Nk,
    hat H_k=-2Nk/(1-Q0^-k), 1<=k<N,
    R_N^2=4 sum_(k=1)^(N-1) k^2/|1-Q0^k|^2.          (13)

These are the unnormalized Fourier transform and its Parseval factor
1/N^2; no extra N is suppressed. Also

    sum_(k=1)^(N-1) csc^2(pi k/N)=(N^2-1)/3.

For an elementary proof, logarithmically differentiate
P(x)=(x^N-1)/(x-1)=product_(k>0)(x-Q0^k) twice at x=1,
using P(1)=N, P'(1)=N(N-1)/2 and
P''(1)=N(N-1)(N-2)/3. Subtract the two resulting sums to get
sum |1-Q0^k|^-2=(N^2-1)/12. Therefore

    R_N^2<=N^2(N^2-1)/3, R_N<=N^2/sqrt(3).           (14)

Use Hilbert--Schmidt norm on matrices and its induced norm on
channels. If |log|p||<=A/N, then

    ||X(p)||_HS<=exp(A),
    ||X(p)tildeH||_HS<=exp(A)R_N,
    |eta|<=R_N ||mathcal A||_(HS->HS).

The second inequality follows entry by entry from |p^(r-s)|<=exp(A);
the third follows from eta I=mathcal A(tildeH). Consequently

    ||Delta'_0(p)||_HS
       <=2exp(A)R_N ||mathcal A||_(HS->HS)
       <=4exp(A)N^2/sqrt(3) ||C_0||_(HS->HS).         (15)

For the last inequality, C_0(I)=z_0 I gives |z_0|<=||C_0||.
The actual scale p_N=1-1/(N rho+c0), with rho in a fixed compact
of C* and c0 bounded, satisfies this hypothesis uniformly for large
N. Scalar pairing retains its actual factor ||e_t||_HS, and division
by b_N retains |b_N|^-1; neither is silently declared polynomial.
Most importantly, (15) is NOT a bound by |z_0|. The full channel
norm can contain large independent open-source contributions.

## 4. A canonical square-zero part of the root channel

Every such root channel preserves E_N=span{I,H}, and in the ordered
basis I,H its matrix is

    [[z_0,eta],[0,z_0]].                              (16)

For composition of two admissible channel families,

    z(CD)=z(C)z(D),
    eta(CD)=z(C)eta(D)+eta(C)z(D).                     (17)

Thus z+eta e, e^2=0, is an exact dual-number character of this
channel algebra. Where z!=0, eta/z is additive under composition.
This is literal finite linear algebra. Arbitrary braid coupons are
not thereby factored into these End(V_d) channels, and (17) implies
no global growth, transport or triangulation theorem.

The first-normal defect is therefore explicitly determined by the FULL
root channel, while (11)--(12) identify which additional root
insertions must be retained. The original finite support cycles,
their moving-period boundary terms and their relative geometric
coefficient remain outside this adapter.

The [focused audit](../experiments/audit_actual_explicit_root_channel_normal_adapter.py)
and [saved results](../experiments/actual_explicit_root_channel_normal_adapter_results.json)
pass 133 exact generic ladder entries and 54 raw divided-descendant
identities. Nineteen original braid, complete-circle and rectangular
sources give 2087 all-band first-normal defect comparisons, 2087
normalized-descendant jet entries, 801 off-node adapter entries,
57 coherent-period identities and 57 genuine moving-p checks. Twelve
actual channel compositions check (17). Exact finite-field tests give
496 Fourier modes, 31 Parseval identities and 62 pivotal free-channel
normal checks. Twenty boundary norm checks at 90 digits have maximum
relative Parseval error below 4.2e-90. These tests retain the actual
generic pivots; they do not infer the root-channel norm from z.

The estimate concerns the first-normal defect, not C_1 or z_1 separately. It retains the full-root-channel norm and the stated period scope.