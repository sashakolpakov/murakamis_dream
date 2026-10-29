# A generic all-port single Racah kernel with actual Clebsch normalization

29 October 2026. This proves a SINGLE terminating balanced 4phi3
formula for every entry of the genuine inverse four-port recoupling
matrix. All external nonnegative INTEGER highest weights are allowed,
including half-integral spins and their actual cyclic-turn sign.
The normalizer comes from a true boundary entry and a leading
coefficient, not a quoted 6j evaluation or polynomial norm formula.

The independent source is the actual two-sum/all-entry construction in
[the ordinary four-port theorem](actual_ordinary_four_port_recoupling_kernel.md).
All high channels and generic normal tails are retained. Root sign
coherence, positive recoupling and sharp graph energy are not inferred.

## 1. Highest-weight notation and actual bases

Use generic zeta, Q=zeta^2 and F_n=(Q;Q)_n. On the ordinary module
V_A of INTEGER highest weight A>=0 use the original balanced
generators and canonical cup:

    P_A(u)=(-1)^u zeta^[u(A-u-1)] F_u F_(A-u)/F_A,
    p_A(u,A-u)=P_A(u), ell_A=p_A^(-1),
    F|u>=(1-Q^(u+1))|u+1>,
    Ecal|u>=zeta^(-A-1)(1-Q^(A+1-u))|u-1>,
    K|u>=zeta^A Q^(-u).

Take external highest weights A,B,C,D with even total. The allowed
intermediate highest weights are

    E=max(|A-B|,|C-D|),...,min(A+B,C+D), step2,
    G=max(|B-C|,|D-A|),...,min(B+C,D+A), step2.     (1)

Assume these equal-cardinality ranges nonempty. Every W_AB^E has
its first highest component one. Put m=(A+B-E)/2. Its actual
highest coefficients are

    h_AB^E(s)=(-1)^s zeta^[s(A-2B+2m-s-1)]
             F_(B-m+s)F_(A-s)/(F_(B-m)F_A),       (2)

and W_AB^E[r]=Delta(F)^r h/F_r, with the canceled physical
coproduct entries proved in the independent source theorem.

Define FULL invariant columns in the SAME external A,B,C,D order:

    S_E=(W_AB^E tensor W_CD^E)p_E,
    T_G(u,v,w,z)=(-1)^A zeta^(A-2u)
           [(W_BC^G tensor W_DA^G)p_G](v,w,z,u).  (3)

The factor (-1)^A K_A is the ACTUAL last-to-first pivotal turn:
ell_A^T p_A=(-1)^A K_A^(-1). It reduces to the older K_A for
integer spins but its sign matters when A is odd. Scaled physical
cups have reciprocal evaluations and retain this same snake.

We prove S_E=sum_G L_(G,E)T_G on EVERY external color. These
are inverse coefficients, not the specialized six-head source column.

## 2. Explicit product normalizers from actual boundary entries

Set

    H=(A+B+C-D)/2, L=min(A,H), Gmax=min(A+D,B+C),
    n=(Gmax-G)/2, U=(C+E-D)/2, V=(D-C+E)/2,
    m=(A+B-E)/2,
    chi_E=(-1)^U zeta^[U(E-U-1)-CV]
                         F_U F_D/(F_((C+D-E)/2) F_E). (4)

The unique outer-color contribution in the true S column gives

    S_E(i,H-i,0,D)=chi_E W_AB^E[U](i,H-i).         (5)

Its LAST physical Clebsch entry X_E has a product evaluation:

    if L=H:
      X_E=F_H h_AB^E(m)/(F_m F_U);
    otherwise L=A, put k=E-U:
      X_E=(-1)^m zeta^[-AB+2Am-m^2-m+k(E-B)]
                              F_(m+k)/(F_m F_k).  (6)

The first is the unique coproduct term with second color zero.
For the second the proved lowest endpoint is
W_AB^E[E](A,B-m)=(-1)^m zeta^[-AB+2Am-m^2-m].
Apply Ecal^(E-U). To finish with first color A every lowering
must act on the second object. Its coefficient divided by the
target coefficient zeta^[-(E-U)(E+1)]F_(E-U) gives (6).
Thus no magnetic sum is hidden in X_E.

For G put i0=(A+G-D)/2, m_bc=(B+C-G)/2,
m_da=(D+A-G)/2. The first nonzero T-chart entry is

    b_G=(-1)^A zeta^(A-2i0) h_BC^G(m_bc)
           *(-1)^m_da zeta^[-AD+2D m_da-m_da(m_da+1)]. (7)

Indeed T_G(i,H-i,0,D)=0 for i>i0, and its value at i0 is (7).
It retains the canonical cup, the W_DA lowest endpoint and the
odd-A cyclic sign. Every b_G is a nonzero generic product.

Define also

    J_n=zeta^[-n(B+1)] F_L F_(B-H+L)
                  /[F_(L-n)F_(B-H+L-n)], J_0=1.   (8)

This is the product of n lower off-diagonals of the ACTUAL first
pair Casimir on physical prefix degree H:

    Omega_AB(i,i-1)=zeta^(-B-1)
                         (1-Q^i)(1-Q^(B-H+i)).    (9)

All factorial indices in (4),(6),(7),(8) are nonnegative on their
physical ranges. The formulas are source entries, not fitted gauges.

## 3. The single terminating balanced Racah formula

If A+D<=B+C choose differences C-D,B-A; otherwise choose
D-C,A-B. Their maximum is E_min=max(|A-B|,|C-D|).
Call the larger s1=E_min and the other s2. Define

    alpha=zeta^(1+s1), beta=zeta^(1+s2),
    gamma=zeta^(-1-C-D), delta=zeta^(-1-A-B),
    P=alpha beta gamma delta=Q^(-Gmax),
    z_E=zeta^(E+1), K=zeta^(Gmax+1).              (10)

At equality this gives the same unordered parameter set. The first
parameter alpha is fixed to specify the polynomial normalization.
Put

    C_n=alpha^n(PQ^(n-1);Q)_n
                     /(alpha beta,alpha gamma,alpha delta;Q)_n,

    G_n(E)=sum_(k=0)^n
       (Q^-n,PQ^(n-1),alpha z_E,alpha/z_E;Q)_k Q^k
         /(Q,alpha beta,alpha gamma,alpha delta;Q)_k. (11)

Listed Pochhammers are multiplied. This is ONE finite sum, possibly
terminated earlier by another numerator. All generic denominators
are units in the physical length: alpha beta has positive exponent
of Q, while alpha gamma and alpha delta first reach zero AFTER n.
The leading coefficient C_n is nonzero generic.

Then the exact all-entry source coefficient is

    L_(G,E)=chi_E X_E/(b_G J_n C_n) *G_n(E),
    S_E=sum_(G in (1)) L_(G,E)T_G.                (12)

No 6j formula, norm or orthogonality measure is an input.

## 4. The uniquely fixed actual Jacobi operator

The actual fourth-leg bend identifies an invariant column with a
highest-weight-D three-object column. Its third-color-zero chart
w(i)=Psi(i,H-i,0,D), max(0,H-B)<=i<=L, is injective by the
original highest equation and ordinary F descendants. The actual
middle Casimir Bmid in that chart is the upper-bidiagonal matrix

    (Bmid)_ii=zeta^(D-A+1)Q^i+zeta^(-D+A-1)Q^(-i),
    (Bmid)_(i-1,i)=-zeta^(B+C-A-1)Q^(i-H)
                       *(1-Q^(A+1-i))(1-Q^(H-i+1)). (13)

This is the independently derived physical color0/color1 extraction.
Let Amid=Omega_AB. The S_E and T_G have respective eigenvalues
lambda_E=zeta^(E+1)+zeta^(-E-1), lambda_G.

Put lambda(W)=zeta^(W+1)+zeta^(-W-1),
Delta=zeta+zeta^(-1), rho=zeta-zeta^(-1), and central values

    a0=lambda(A)lambda(B)+lambda(C)lambda(D),
    b0=lambda(B)lambda(C)+lambda(A)lambda(D),
    c0=lambda(A)lambda(C)+lambda(B)lambda(D).

The original generic cleared Fricke identities force Bmid to be
three-diagonal in the S basis. Write its action as
Bmid S_E=p_E S_(E+2)+d_E S_E+m_E S_(E-2). The first relation gives

    d_E=(Delta b0-c0 lambda_E)/(Delta^2-lambda_E^2). (14)

The E=0 exception means A=B,C=D and is fixed by the ACTUAL cup
projection rather than cancellation of 0/0. With
S1=sum_(i=0)^A Q^-i and S2=sum_(i=0)^A Q^(-2i), (13) gives

    ell_A p_A=(-1)^A zeta^A S1,
    ell_A Bmid p_A=(-1)^A{
       zeta^(C+1)(1+Q^(A+1))S1
       +[zeta^(2A-C-1)-zeta^(C+1)Q^(A+1)]S2}.

The finite ratio S2/S1=(1+Q^(-A-1))/(1+Q^-1) gives
d_0=lambda(A)lambda(C)/Delta, the value of (14) after imposing
A=B,C=D and canceling. A=0 is immediate in one dimension.

The diagonal of the second Fricke relation fixes the products
P_E=p_E m_(E+2), with P_(E_min-2)=0, by

    [2lambda_E-(Q+Q^-1)lambda_(E+2)]P_E
      +[2lambda_E-(Q+Q^-1)lambda_(E-2)]P_(E-2)
       =rho^2[Delta a0-c0 d_E-Delta^2 lambda_E
                                             +lambda_E d_E^2]. (15)

The forward coefficient is nonzero generic.

There is a known ACTUAL LEFT eigenrow fixing the remaining gauge.
At G=Gmax one has i0=L, so this physical eigenrow is simply the
last chart coordinate. Hence

    ell_0(E)=L_(Gmax,E)=chi_E X_E/b_(Gmax)!=0.     (16)

This is a genuine source row, not a prescribed spectral weight.
Set u_E=p_E ell_0(E+2)/ell_0(E) and
v_E=m_E ell_0(E-2)/ell_0(E). Their sum is lambda_Gmax-d_E,
and their successive products are still P_E. Starting from
v_Emin=0, the sum and (15) determine them uniquely whenever the
proposed interior u is nonzero. The exact result is

    u_E=K U(z_E), v_E=K U(z_E^-1),
    U(z)=product_(t=alpha,beta,gamma,delta)(1-tz)
                                        /[(1-z^2)(1-Qz^2)],
    d_E=K+K^-1-K[U(z_E)+U(z_E^-1)].              (17)

To prove this uniformly, use independent formal variables
zeta,Q^a,Q^b,Q^c,Q^d,Q^e, with A=2a,...,E=2e.
For the first branch K=zeta Q^(a+d), both (14),(17) and the
product recurrence (15) have IDENTICALLY ZERO cleared rational
numerators. The attached audit supplies these two exact six-variable
symbolic certificates. The second branch follows by a<->b,c<->d,
which preserves a0,b0,c0. Parameter permutation preserves U.
After canceled endpoint factors are evaluated, U(z_E) is nonzero
on every interior channel and vanishes at the upper endpoint;
U(z_E^-1) vanishes at the lower endpoint. The uniqueness therefore
proves (17) for the ACTUAL operator, with no unfixed sign.

## 5. Leading coefficients supply the true source normalization

Let ell_G(i0)=1 be the physical LEFT eigenrow of (13), zero below
i0 and satisfying the elementary one-step equation above i0.
The independent two-sum source identity is

    L_(G,E)=ell_G(w_E)/b_G,
    w_E(i)=S_E(i,H-i,0,D).                        (18)

Divide by (16). Equation (17) gives the actual finite problem

    U(z_E)[g(E+2)-g(E)]+U(z_E^-1)[g(E-2)-g(E)]
                    =(Q^-n-1)(1-PQ^(n-1))g(E).   (19)

Indeed lambda_G=lambda_Gmax+K(Q^-n-1)(1-PQ^(n-1)).
This is the exact affine eigenvalue conversion, not a replacement
of the physical Casimir.

Our OWN [finite symmetric polynomial calculation](finite_balanced_sears_operator_proof.md)
proves that G_n solves (19), with leading coefficient C_n in
lambda_E=z_E+z_E^-1. Its degree is n and its generic leading
coefficient is nonzero. The finite grid has distinct Casimir nodes,
and its forward coefficient is nonzero until the last slot, so
the actual source row is proportional to G_n. Its multiplier still
needs determining.

For that multiplier, the physical Amid is irreducible tridiagonal.
Starting from its last row yields

    w_E(i)/w_E(L)=a polynomial in lambda_E
       of degree L-i with leading coefficient
           1/product_(t=i+1)^L Amid(t,t-1).       (20)

Formula (9) evaluates its denominator. In (18) only i>=i0=L-n
occurs and ell_G(i0)=1. Thus

    L_(G,E)/ell_0(E)
       has degree n and leading coefficient
                         b_(Gmax)/(b_G J_n).      (21)

Since n is less than the number of channel nodes, this polynomial
leading coefficient fixes the proportionality even on the finite
grid. Comparing (21) with C_n proves EXACTLY (12), on every color.

## 6. Exact conversion to the seven-factorial sum, including its phase

Put [r]!=zeta^[-r(r-1)/2]F_r/(1-Q)^r and s=(A+B+C+D)/2.
The tetrahedral incidence is the FOUR faces and THREE opposite sums

    t=( (A+B+E)/2, (C+D+E)/2,
        (B+C+G)/2, (D+A+G)/2 ),
    u=( s, (A+C+E+G)/2, (B+D+E+G)/2 ).

Define the literal seven-factorial finite sum

    S=sum_(z=max t)^(min u) (-1)^z [z+1]!
                           /(product_i[z-t_i]! product_j[u_j-z]!). (22)

All its true factorial indices are nonnegative. Choose the effective
quadruple (A',B',C',D')=(A,B,C,D) when A+D<=B+C, and
(B,A,D,C) otherwise. This latter permutation leaves (22) exactly
unchanged: it exchanges its last two faces and its last two opposite
sums. Set

    t0=s-Gmax,
    R1=(C+D-E)/2, R2=(A+B-E)/2,
    R3=(A'-B'+E)/2, R4=(D'-C'+E)/2,
    S0=(-1)^s [s+1]!/([R1]![R2]![t0]![R3]![R4]!),
    Mstar=(Gmax+G)/2+1,
    V_n=zeta^n (Q^-Mstar;Q)_n
                 /[F_n(Q^(t0+1);Q)_n(Q^(-s-1);Q)_n]. (23)

Every factor in S0 and V_n is nonzero generic. The EXACT source
normalization of the seven-factorial convention is

    S=S0 (V_n/C_n)G_n(E),
    L_(G,E)=chi_E X_E/(b_G J_n S0 V_n) *S.        (24)

This includes all signs and powers of zeta. In particular the
coefficient is not merely equated to a positive square or to an
unnormalized named 6j symbol.

Here is an own finite proof of (24). Write a=A'/2,b=B'/2,c=C'/2,
d=D'/2, e=E/2, f=G/2. Then fmax=a+d, n=fmax-f and
t0=b+c-a-d. At f=fmax the z range in (22) is the SINGLE z=s,
which is precisely S0. For general n write z=s-k. Dividing by S0
gives the finite falling-product identity

    S/S0=sum_(k=0)^n (-1)^k
       [R1]_k^down [R2]_k^down
       [R3]_(n-k)^down [R4]_(n-k)^down
       /([s+1]_k^down [t0+1]_(n-k)^up [k]![n-k]!). (25)

The products have their evident consecutive quantum integers. If
a formal term lies outside the true range of (22), one falling
product contains [0], and that term is EXACTLY zero. No nonzero
factorial is assigned to a negative index.

For generic formal z_E, factor the k=0 term of (25). Its residual
balanced series is

    4phi3(Q^-n,Q^-R1,Q^-R2,Q^(-t0-n);
              Q^(-s-1),Q^(R3-n+1),Q^(R4-n+1);Q,Q). (26)

Apply the OWN finite Sears identity, retaining Q^-R1 and taking
d_S=Q^(-s-1), e_S=Q^(R3-n+1). The resulting series is exactly
the same finite symmetric eigenpolynomial as (11), but with FIRST
parameter gamma=zeta^(-1-C-D). In particular its numerator pair
is Q^-R1 and Q^(-c-d-e-1), and its denominator parameters are
Q^-D', Q^(-(s-B')), Q^(-s-1).

After multiplying the k=0 term and canceling the two E-dependent
Sears denominator products, its scalar is

    D_n=(-1)^n zeta^[n(B'-A'+n+1)]
       (Q^(s-B'-n+1),Q^-D';Q)_n
                          /[F_n(Q^(t0+1);Q)_n]. (27)

These cancellations are performed as rational identities in formal
z_E BEFORE specializing a channel. Thus the identity still holds
when a k=0 factorial representation would have a negative index:
the falling-product polynomial (25) has no such division.

The OWN symmetric-polynomial proof makes the normalized degree-n
eigenpolynomial independent of its first parameter. Its leading
coefficient when gamma is first is

    C_n^gamma=gamma^n(PQ^(n-1);Q)_n
                    /(gamma alpha,gamma beta,gamma delta;Q)_n.

Reverse the finite product (Q^(s-B'-n+1);Q)_n in (27). The factors
Q^-D' and Q^(-(s-B')) cancel those of C_n^gamma. All signs cancel,
the remaining zeta monomial is zeta^n, and

    D_n C_n^gamma=V_n.                            (28)

Consequently D_n times the gamma-first polynomial equals
(V_n/C_n)G_n(E), proving (24). This is a finite product/Sears proof;
no generic factorial interpolation or quoted tetrahedral theorem
is required. The rational identity for formal z_E specializes to
every physical E using (25).

## 7. Exact source relation to a face-normalized scalar metric

The actual prefactor in (24) SEPARATES the two intermediate labels:

    a_E^src=chi_E X_E/S0(E),
    b_G^src=1/(b_G J_n V_n),
    L_(G,E)=b_G^src a_E^src S.                    (29)

Thus source columns rescaled as S_E/a_E^src and b_G^src T_G
have coefficient EXACTLY the seven-factorial sum (22). No phase
has been omitted in this row/column gauge.

For an admissible highest-weight triple define its usual finite
factorial expression, without assuming any 6j interpretation,

    D(U,V,W)=[(U+V-W)/2]![(U+W-V)/2]![(V+W-U)/2]!
                                      /[((U+V+W)/2)+1]!,
    D_E=D(A,B,E)D(C,D,E),
    D_G=D(B,C,G)D(D,A,G).

The coefficient sqrt(D_E D_G)S is therefore an explicit diagonal
gauge of the actual source: use sqrt(D_E)S_E/a_E^src and
b_G^src T_G/sqrt(D_G) as its two generic bases. Square-root
branches can be fixed positive at real 0<zeta<1, where every
factorial is positive. The squared identity is branch-independent.
For ANY separately fixed level N it says exactly

    [N]^2 D_E D_G L_(G,E)^2/(a_E^src b_G^src)^2
                           =[N]^2 D_E D_G S^2.    (30)

In particular (30) identifies the source with this convention of
the normalized scalar metric BEFORE a root normal is taken. If the
four face sums are in the saturated low-fold chamber, the familiar
root-zero factors in (30) are the actual generic ones. High partners
and [2N] tails remain in the same equality.

Principal-root positivity of the scalar convention must keep its
spin phase. For INTEGER spins (all six highest weights even), the
supported theorem gives the positive once-power factorial square.
For admissible half-integral spins the branch-free generic identity
(30) still holds, but the positive sine-factorial square differs by
the sign (-1)^(A+B+C+D+E+G). This is the parity of the four face
zero-removal signs. No positive-square assertion for arbitrary
half-spin data is silently included in (30).

These are diagonal gauges of a SCALAR recoupling matrix. They may
have zeros or poles at the root; paired confluence and original
boundary costs still require their own estimates. They neither
make the physical root operator positive nor identify this scalar
metric with the full marked magnetic/tensor energy. Also a_E^src
depends on its four external objects; it has not been asserted to
be a single universal per-edge metric throughout a graph.

## 8. Generic normals and scope

The theorem and (24) are rational BEFORE root specialization. High
intermediate channels, high partners and every normal of the original
maps remain present. Individual source factors may have zeros or
poles at a root, and extra terminations can have derivative tails.
The GENERIC finite sum and original source maps must be combined
before taking a fixed marked normal. In particular second-orbit
zeros such as [2N] in (22) are retained in (24); they cannot be
deleted when comparing first normals.

There is a useful explicit finite normal budget. If the EXTERNAL
highest weights A,B,C,D are all <N, while intermediate E,G retain
their ENTIRE ranges (1), then every denominator of G_n in (11)
is a root unit. Indeed alpha beta=Q^(t0+1), and the last exponent
t0+n is one of the ordinary physical coupling deficits, hence <N.
The other two exponents start at -m_cd or -m_ab for the minimal E,
with n<=m_cd,m_ab<N; their products end before exponent zero.
The factor F_n is a unit too.

The numerator of C_n has at most one simple root zero: its negative
exponents have magnitude <2N and length <N. The actual chi_E has
at most one pole, from F_E on a high channel E>=N, whereas X_E,
b_G and J_n are physical products with indices <N. Consequently

    pole_order L_(G,E)<=2.                       (31)

The full invariant T_G has at most one pole from its canonical
p_G, so each term L_(G,E)T_G has pole order at most THREE. To
check this complete physical identity through its first normal,
retain Taylor orders zero through FOUR after multiplying by the
cube of a local root parameter. This is a uniform finite normal
budget, not a bound on coefficient magnitudes. For unfolded high
EXTERNAL partners with highest weights >=N use the generic formula
itself and retain its explicit zero factors; (31) is not asserted
for that different range.

The identity supplies finite actual all-port coefficients for graph
contractions and meromorphic jets. It does not make a recoupling
positive, unitary, polynomially conditioned or sharply controlled
under cycle sewing.

Audit: [uniform certificates and independent literal source tensors](../experiments/audit_actual_general_four_port_single_racah_kernel.py).
Fresh replay passes two universal Fricke/AW identities, 381 generic
all-port external families and 1125 single-sum source entries,
including half-integral spins with the true (-1)^A cyclic sign.
Eight root zero-order families check all 40,820 channel entries,
including 14,332 retained high-channel entries, with the certified
inverse pole bound two and full-term first-normal budget four.
Finite tests supplement the displayed uniform proof; they are not
a polynomial-fitting argument.

Independent internal review: root completed a full analytical read
and fresh primary replay of the actual source theorem, seven-factorial
conversion and scalar metric gauge. The crossing/source agent also
completed a full independent analytical read and fresh primary replay,
then separately checked (25)--(28), the surviving zeta^n phase and
the added finite pole/first-normal budget (31). All 1125 source
entries were checked in both one-sum conventions. No energy or
full-root positivity conclusion was included in either verdict.
