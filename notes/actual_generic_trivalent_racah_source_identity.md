# The actual generic trivalent source is the normalized single Racah sum

29 October 2026. This proves the previously missing GENERIC finite
identity, with the normalization determined by the original nested
cups and genuine ordered duals. It includes both low channels and
their high fold partners before root specialization. The proof uses
an actual mixed-highest Casimir matrix, two universal rational
certificates, the literal coefficient COLUMN obtained by bending,
and our own finite polynomial/Sears calculation. No quoted quantum
6j evaluation is a premise.

This is a finite identity and preserves the normal tails. A tame
boundary-conditioning or general graph asymptotic estimate is not
claimed solely from this formula.

## 1. Statement with the actual source normalization

Let N>=2, d=N-1, zeta generic, Q=zeta^2, F_n=(Q;Q)_n, and

    [n]! = zeta^[-n(n-1)/2] F_n/(1-Q)^n.

For every ordinary triangle 0<=a,b,c<=d put J=a+b+c and
r=b+c-a, r1=a+b-c, r2=a+c-b. Let B_abc be the ACTUAL analytic
factorial source sum defined in (8) of
[the generic six-head theorem](actual_generic_six_head_tetrahedral_source.md).
It is not defined through the formula to be proved here. Then

    B_abc=(-1)^J zeta^D [a]![b]![c]!/[J+1]! *S_abc,
    D=a^2-b^2+c^2-ab-ac+bc-cd,                     (1)

where the SINGLE terminating sum is

    S_abc=sum_z (-1)^z [z+1]!
       /([z-J]! product_(j=a,b,c)[z-d-j]!
          [d+a+b-z]![d+a+c-z]![d+b+c-z]!),
    max(J,d+a,d+b,d+c)<=z
                       <=min(d+a+b,d+a+c,d+b+c).  (2)

Every factorial index in its true range is nonnegative. Equations
(1),(2) are generic rational identities, so all root-zero factors
and all generic normals must be retained when specializing them.

## 2. An actual finite highest-source space

First take a>=b, put h=a-b, and let

    C={h,h+1,...,min(a+b,d)}, D0=d+h,
    V=ker(Ecal_12^(2a+1)) in (V_d tensor V_d)_(degree D0).

The generic physical Clebsch columns from the six-head theorem give
a basis

    v_c=W_c[a+c-b], c in C.

Indeed the generic physical pair decomposes into its distinct
Casimir eigenspaces with highest weights 2c; in degree D0, precisely
these descendants are killed by Ecal_12^(2a+1). Their highest lift
to Hom(Q_b,V_d tensor V_d tensor Q_a) is

    H(w)=sum_(u=0)^(2a) alpha_u Ecal_12^u w tensor |u>,
    alpha_u=(-1)^u zeta^[u(4a+1)]Q^[-u(u-1)/2]
                                      F_(2a-u)/F_(2a).

The direct E equation proves this formula, and extracting the third
color zero is its inverse. Thus no full ambient space is silently
identified with the actual highest source.

Let A=Omega_12 and B be Omega_23 transported to this highest chart.
In physical prefix coordinates |s,D0-s>, h<=s<=d, direct extraction
of third colors zero and one gives

    B_ss=zeta^(-d+2b+1)Q^s+zeta^(d-2b-1)Q^(-s),
    B_(s-1,s)=-zeta^(2a-1)Q^(s-D0)
                       (1-Q^(d+1-s))(1-Q^(D0-s+1)). (3)

All other entries vanish. The diagonal FE contribution from third
color zero cancels the corresponding term from third color one.
This is the actual right-pair Casimir, whose physical V_d-channel
eigenvalue is

    H0=zeta^N+zeta^(-N).

The first physical component of each v_c has a closed finite Chu
evaluation:

    phi_c=v_c(h,d)
       =zeta^[-dc+2(d-c)h]
                         F_(d-h)/[F_(d-c)F_(c-h)]. (4)

For clarity, (4) is obtained directly from the physical coproduct
sum for W_c[c+h](h,d). After extracting zeta^(-dc)F_h/F_c,
the remaining sum is

    sum_u(-1)^u Q^[u(u-1)/2]
                        F_(d-u)/[F_u F_(d-c-u)F_(h-u)].

The finite second Chu identity, already proved by finite binomial
expansion in the six-head note, evaluates it to
Q^((d-c)h)F_c F_(d-h)/[F_(d-c)F_h F_(c-h)]. Thus (4) is not an
assumed endpoint value. Put f_c=v_c/phi_c; every f_c has first
physical component one.

## 3. A universal, uniquely determined three-diagonal matrix

Write lambda_c=zeta^(2c+1)+zeta^(-2c-1), delta=zeta+zeta^(-1),
rho=zeta-zeta^(-1), and

    alpha=H0^2+lambda_a lambda_b,
    beta=gamma=H0(lambda_a+lambda_b).

The independently proved, generic
[quantum Fricke identities](actual_adjacent_twist_character_and_source.md)
apply to the actual adjacent Casimirs in this highest-source module.
Eliminating their third generator gives

    A^2B-(Q+Q^-1)ABA+BA^2+rho^2 delta^2 B
                                      =rho^2(delta beta-gamma A),
    B^2A-(Q+Q^-1)BAB+AB^2+rho^2 delta^2 A
                                      =rho^2(delta alpha-gamma B). (5)

These are universal cleared Hopf-algebra equalities, not a recurrence
deduced from a guessed Racah sum. In the A-eigenbasis f_c, the first
identity forces B to be tridiagonal: its off-diagonal coefficient
can be nonzero only when the two indices differ by one. Its diagonal
is

    b_c=H0(lambda_a+lambda_b)/(delta+lambda_c).     (6)

For c>0 this follows by canceling the nonzero generic factor
delta-lambda_c. The channel c=0 occurs only when h=0 and a=b;
there that factor is identically zero and requires a separate ACTUAL
source calculation. Here f_0=p_d is the canonical physical cup. Its
genuine retraction is the canonical cap ell_d, up to the same scalar
on numerator and denominator, so

    b_0=(ell_d B p_d)/(ell_d p_d).

Put S1=sum_(s=0)^d Q^(-s), S2=sum_(s=0)^d Q^(-2s). Using (3) and
P_d(s)/P_d(d-s)=(-1)^d zeta^d Q^(-s), the diagonal and upper
off-diagonal terms give EXACTLY

    ell_d p_d=(-1)^d zeta^d S1,
    ell_d B p_d=(-1)^d{
       zeta^(2a+1)(1+Q^N)S1
        +[zeta^(2d-2a-1)-zeta^(2a+1)Q^N]S2}.

The finite geometric ratio S2/S1=(1+Q^(-N))/(1+Q^(-1)) reduces
this to b_0=H0 lambda_a/delta=beta/(2delta), exactly (6). This
supplies the exceptional endpoint without continuing in an integer
channel. Write

    B f_c=p_c f_(c+1)+b_c f_c+m_c f_(c-1).

Here m_h=0 and p_maxC=0. The two remaining coefficients are

    kappa0=zeta^N Q^b,
    p_c=-kappa0^-1 Q^(c-h)
       (1-Q^(c+h+1))(1-Q^(a+b-c))(1-Q^(d-c))
                      /[(1-Q^(2c+1))(1+Q^(c+1))],
    m_c=-kappa0^-1 Q^c
       (1-Q^(c-h))(1-Q^(N+c))(1-Q^(a+b+c+1))
                      /[(1+Q^c)(1-Q^(2c+1))].     (7)

Here is a uniform proof of (7), rather than interpolation of matrix
data. Since f_c has first physical component one, (3) and the first
row of the physical A give a prescribed row-sum

    p_c+b_c+m_c=S_c.

To state this and its certificate without long monomial powers, use
INDEPENDENT formal variables q,t,H,V,Y and set

    Q=q^2, t=zeta^N, H=Q^h, V=Q^b, Y=Q^c,
    lambda(Y)=qY+q^(-1)Y^(-1),
    A00=q/t^2(1-H)(1-t^2/H)
           +qH/t^2(1-t^2/Q)(1-Q)+q/H+H/q,
    B00=QHV/t+t/(QHV),
    S(Y)=B00-(tV/q)(lambda(Y)-A00).                (8)

The coefficient of the first off-diagonal in B divided by that in
A is exactly -tV/q; hence (8) is the first-row equation for EVERY
c. Substituting (6),(7) in p+b+m-S gives the IDENTICALLY ZERO
rational function of q,t,H,V,Y.

The diagonal of the second identity in (5) fixes products
P_c=p_c m_(c+1) by the first-order recursion

    [2lambda_c-(Q+Q^-1)lambda_(c+1)]P_c
      +[2lambda_c-(Q+Q^-1)lambda_(c-1)]P_(c-1)
       =rho^2[delta alpha-gamma b_c-delta^2 lambda_c
                                             +lambda_c b_c^2]. (9)

Its forward coefficient is nonzero generic, and P_(h-1)=0.
Substitution of (7) in (9) is a SECOND identically zero rational
function in those five independent variables. The accompanying
symbolic certificate clears each denominator and verifies zero.

These two identities determine the actual coefficients uniquely:
at h, m_h=0 and the row-sum gives p_h; then (9) fixes P_h, so
m_(h+1)=P_h/p_h, and the next row-sum fixes p_(h+1). Continue.
All interior proposed p_c are nonzero generic; their only physical
endpoint zeros are c=a+b or c=d. Thus induction proves (7) at
every channel, including the endpoint, without an undetermined sign.
If b=0 the space has one dimension and the statement is immediate.

## 4. The source is a coefficient COLUMN, with literal bend normalization

Use the actual generic maps

    T=(I_V tensor W_(V,Qa)^V)W_b,
    L_c=(W_c tensor I_Qa)W_(Qc,Qa)^Qb.

The right map T has Omega_23 eigenvalue H0 on ALL input colors,
since its positions23 factor through the actual V_d. Its left-basis
expansion is

    T=sum_c R_Hom(c) L_c,
    R_Hom(c)=J_c B_abc,
    J_c=(-1)^(d+c) zeta^ER
       F_r1 F_r2 F_(d-a)F_(d-c)F_(2c+1)
                            /[F_a F_d F_(d+c+1)],
    ER=-2a^2-5c^2+2ac+2bc+ad+3dc-c+d.            (10)

The full source-independent map proof, using only cups and Clebsch
maps, is in
[the literal generic tetrahedral bend](actual_generic_tetrahedral_source_as_recoupling.md).
In brief, bend the b output of
(DW_a tensor DW_b tensor DW_c)(p16 p23 p45). The resulting map is
simultaneously a known multiple of W_(Qc,Qa)^Qb and
(DW_c tensor I)(I tensor Wtilde_a)W_b. The latter bent Wtilde_a
is its actual first-entry-one mixed Clebsch map times its explicitly
computed cup scalar. Composing DW_c W_c=n_c then proves (10).
It is a map identity before scalar extraction, not a scalar fit.

The third-color-zero coefficient of L_c is nu_c v_c, where

    nu_c=(-1)^r2 zeta^[r2(2c-4a+r2-1)]
                                      F_(2a)F_r/(F_r1 F_(2c)).

Thus in the f_c basis the RIGHT coordinate column of T is

    y_c=J_c nu_c phi_c B_abc.                     (11)

This is not the inverse coefficient obtained by applying a left
eigenrow to v_c. Confusing them changes the transpose and invalidates
the recurrence.

Define a nonzero generic gauge by

    K_c=(-1)^(d+b+c) zeta^P
       F_a F_(N+a)F_(2b)F_(d-a+b)
       /[F_(J+1)F_(a-b)F_r F_b F_(d-a)F_r1F_(d-c)],
    P=2a^2-b^2+3c^2-2ac+2bc-d(a+b+2c+1)+b+c,
    g_c=B_abc/K_c, sigma_c=J_c nu_c phi_c K_c.      (12)

All factorial indices here are nonnegative on C. From the explicit
products, its successive ratio is

    sigma_(c+1)/sigma_c
      =-Q^(c-h)(1-Q^(c+h+1))(1-Q^(2c+3))
          *(1-Q^(a+b-c))(1-Q^(d-c))
       /[(1-Q^(2c+1))(1-Q^(N+c+1))
          *(1-Q^(J+2))(1-Q^(c-h+1))].             (13)

Successive ratios are used only when both indices belong to C;
outside C the corresponding term is its actual endpoint zero.

There is an exact source endpoint: at c=h the source Euler formula
has r=0 and directly gives B_abh=K_h. Hence g_h=1. No unknown
endpoint residue or source coefficient is supplied as an assumption.

## 5. The exact finite eigenproblem is our own AW polynomial operator

Put X=Q^N. For c in C define

    u_c=(1-Q^(h+c+1))(1-Q^(c+1))
              *(1-Q^(c-a-b))(1-X^-1Q^(c+1))
                            /[(1-Q^(2c+1))(1-Q^(2c+2))],
    v_c=(1-Q^(h-c))(1-Q^(-c))
              *(1-Q^(-a-b-c-1))(1-X^-1Q^(-c))
                            /[(1-Q^(-2c-1))(1-Q^(-2c))],
    Lambda_b=(Q^-b-1)(1-X^-1Q^-b).                (14)

At c=0 the second formula has its removable value after canceling
(1-Q^(-c))/(1-Q^(-2c))=1/(1+Q^(-c)). Direct rational substitution
of (7),(13) gives

    b_c=H0-kappa0(Lambda_b+u_c+v_c),
    p_c=kappa0 v_(c+1) sigma_(c+1)/sigma_c,
    m_c=kappa0 u_(c-1) sigma_(c-1)/sigma_c.         (15)

These are also checked identically over the five-variable rational
field. Since y is the coefficient COLUMN, its Casimir equation is

    H0 y_c=p_(c-1)y_(c-1)+b_c y_c+m_(c+1)y_(c+1).

Equations (11),(15) therefore give the exact source recurrence

    u_c(g_(c+1)-g_c)+v_c(g_(c-1)-g_c)
                                           =Lambda_b g_c. (16)

Equivalently the gauged physical matrix is
H0 I+kappa0(L_AW-Lambda_b I), with L_AW the difference operator on
the left of (16). Its physical Casimir eigenvalue is H0, NOT lambda_b.
The latter is the affine difference-operator eigenvalue only.

Our independently proved
[finite symmetric polynomial operator](finite_balanced_sears_operator_proof.md)
applies with base Q and parameters

    A0=zeta Q^(a-b), B0=zeta,
    C0=zeta^(-1)Q^(-a-b), D0=zeta/X,
    z_c=zeta Q^c, degree n=b.

Its forward/backward coefficients are exactly (14). Thus the finite
polynomial calculation in that note proves that

    G_c=4phi3(Q^-b,X^-1Q^-b,Q^(a-b-c),Q^(a-b+c+1);
                 Q^(a-b+1),Q^-2b,X^-1Q^(a-b+1);Q,Q) (17)

satisfies (16). The sum has length b; no denominator reaches zero
in its generic physical range, since d>=a>=b. At c=h one numerator
is one, so G_h=1. Also v_h=0, u_maxC=0, and every interior u_c is
nonzero generic. Consequently the scalar three-term recurrence with
its ACTUAL endpoint g_h=1 determines all its values uniquely.
It follows that

    B_abc=K_c G_c, for a>=b, c in C.              (18)

This is the decisive source-selection step. It is a finite exact
recurrence argument; no semiclassical branch or noncancellation
assumption is made.

## 6. Own Sears conversion gives the single sum

First suppose a=max(a,b,c) and d>=b+c. Write z=d+a+k in (2).
The factorial ratios give the balanced finite long series

    H=4phi3(Q^-r,Q^(N+a+1),Q^-b,Q^-c;
                   Q^(N-b-c),Q^(a-b+1),Q^(a-c+1);Q,Q).

Its prefactor is the k=0 term of (1). Apply our OWN finite Sears
identity, taking termination length b, retained parameter Q^-r,
d_S=Q^(a-b+1), e_S=Q^(a-c+1). Extending the sum to length b
is legitimate since Q^-r already kills all k>r. It gives

    H=(Q^(b+1),X^-1Q^(a-b+1);Q)_b
                 /(Q^(a-c+1),X^-1Q^(c+1);Q)_b *G_c.

Here the k=0 prefactor of (1) is explicitly

    R0=(-1)^(d+b+c) zeta^D [a]![N+a]!
       /([J+1]![d-b-c]![a-b]![a-c]![r]!).

Reverse the two negative-start Pochhammers in the Sears factor.
That factor becomes

    Q^[b(h-c)] F_(2b)F_(d-h)F_(a-c)F_(d-b-c)
       /[F_b F_(d-a)F_r1 F_(d-c)].

All four latter factorials cancel those in R0 as displayed in (12).
For the phase, converting R0 to F factorials gives exponent

    D-T(a)-T(N+a)+T(J+1)+T(d-b-c)+T(h)+T(a-c)+T(r),

where T(n)=n(n-1)/2. Adding 2b(h-c) gives exactly P in (12).
Thus their product is K_c with its full sign and phase, not merely
its square. Equation (18) proves (1) in this region.

To remove the temporary size restriction, fix ordinary a=max(a,b,c).
The independently proved
[generic source polynomial reduction](generic_trivalent_bilinear_racah_port.md),
section3a, normalizes the ACTUAL B to R_SRC(X), degree at most r,
after the explicit factor (XQ^-a)_(2a+1). The proposed single sum
normalizes to the explicit R_TGT(X) of that same degree. Their
normalizations and constants were derived by finite products there.
For every real 0<zeta<1, the preceding argument proves equality at
ALL X=Q^(d+1), d>=b+c. These are infinitely many distinct points.
Thus the two finite polynomials agree identically. Their rational
coefficients in Q then agree generically as well.

Substitute X=Q^(d+1) for ANY physical d>=a. If a term would have
d-b-c+k<0, its finite product
(XQ^(-b-c+k);Q)_(J+1) contains 1-Q^0 and is EXACTLY zero.
This restores precisely the correct lower limit z>=J. Therefore
the same identity covers d<b+c and every high-partner range.
No nonzero factorial is assigned to a negative index.

Finally remove the ordering restriction by genuine cyclic duality.
For the canonical physical cup,

    P_d(d-u)/P_d(u)=(-1)^d zeta^(-d+2u).

Cycling the three consecutive physical PAIRS in p16 p23 p45 gives
exactly the inverse K on the moved pair. Intertwining transports it
to the moved ordinary object. Hence

    U_bca(r_b,r_c,r_a)=K_a^(-1)(r_a)U_abc(r_a,r_b,r_c).

The ordinary Theta coefficient needed to extract the new canonical
corner is computed by its finite two-term E recursion, first along
third color zero to second color 2b, then keeping that second color
maximal. It is

    Theta_abc(0,2b,r2)
      =zeta^Et F_(2b)F_r2/(F_r1F_(2c)),
    Et=-2(a^2-ab-a+bc-c^2).

Substituting the ACTUAL source-corner prefactors (9) of the generic
six-head theorem cancels every factorial and sign, leaving

    B_bca=zeta^[D(b,c,a)-D(a,b,c)]B_abc.           (19)

Every triple can be cyclically rotated so its largest label is first.
The factorial prefactor and the finite sum in (1),(2) are symmetric.
Thus (19) proves (1) for ALL ordered ordinary triangles.

## 7. Root normals, scope and audit

There is also a useful EXACT closed-trace corollary. With the original
ordinary closure T_abc from (11) of the generic six-head theorem,

    T_abc=(-1)^d product_(j=a,b,c)[2j+1]
       *[r]![r1]![r2]!/[J+1]!
       *product_(j=a,b,c)([j]!^2[d-j]!/[N+j]!)
       *S_abc^2.                                 (20)

This is a square of the generic scalar, not a Hermitian absolute
square. It keeps the genuine ordinary dimensions. To verify all
normalization factors directly, insert (1) for B_abc and B_cba in
that source trace and replace F_n by
zeta^[n(n-1)/2](1-Q)^n[n]!. The powers of 1-Q cancel. Writing
T(n)=n(n-1)/2, the remaining exponent is the identically zero
polynomial

    E+D(a,b,c)+D(c,b,a)+T(r)+T(r1)+T(r2)+T(J+1)
             +sum_(j=a,b,c)[T(d-j)-T(N+j)+2j]=0,

where E is the actual trace exponent in the six-head theorem. This
also proves (20) without importing a tetrahedral trace normalization.

Equations (1),(2) now give a single factorial sum for each generic
branch in the full <=8-branch marked cluster formula. This identity
holds before specialization, so it retains the derivative tails
that are lost by imposing Q^N=1 first. For low-fold principal-root
labels, one can extract the known single [N] factor and recover the
proved positive root partition. High partners and terms crossing N
retain their actual zero orders; they must be combined as prescribed
by the generic cluster formula before a marked normal is taken.

The proof has NOT yet established a polynomial bound for every
lower marked moment divided by the positive top moment. Such a
bound requires estimates for the explicit factorial sums and their
bounded normals; it does not follow merely from (1).

Audit: [universal symbolic recurrence and literal source checks](../experiments/audit_actual_generic_trivalent_racah_source_identity.py).
The two Fricke/boundary rational certificates and the transpose/AW
gauge certificates have identically zero cleared numerators in five
independent parameters. The supplementary original-matrix audit
passes eleven generic families, 489 all-vector Jacobi recurrences,
full highest-source column/endpoint checks, and cyclic source
covariance. These are exact checks supporting the uniform proof,
not an inference from numerical polynomial fitting.

Independent internal review: both the global audit agent and the
crossing/source agent completed full analytical reads and fresh replays,
including the exceptional c=0 actual cup projection, literal source-column
bend and transpose, generic high-partner continuation, cyclic source
phase and closed-trace exponent cancellation. No conditioning or
asymptotic conclusion was included in either verdict.
