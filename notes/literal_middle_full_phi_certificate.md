# A literal middle five-point operator identity with its complete finite source

28 October 2026. This realizes the middle classical certificate

    +partial(a,b,p,p_1,s_M)

from [the crossing fundamental cycle](crossing_fundamental_cycle.md)
as an exact finite relative operator identity inside the original
crossing factorization. Its developed arguments are the five
cross-ratios of that **specific** configuration, with the required
quad/orientation changes. The X face is a strict cut of a cyclic
unit; its full projector correction is explicit. The original
cup selects a nonzero top marked full-Phi value.

This is an identity with marked full-Phi and nilpotent Euler
operators, including their factorial face frames and circle/radial
sources. It does not assert that each factor separately is an
already assigned positive charged tetrahedron in a regular
geometric face frame. That further face/Fourier assignment, the
other two certificates, and the global selected cycle remain
separate work.

## 1. Fixed actual coordinates and the original crossing factor

Use complete original heads with

    Q=exp(2pi*i/N), d=N-1, x=-q^(-1), lambda=x^(-1)=Qx,
    S_1^N=mu, S_2^N=x^N mu,
    Z=Z_1, X=x S_2S_1^(-1), XZ=QZX, X^N=Z^N=1.

The literal five flags were calculated in
[the middle-configuration note](actual_middle_five_point_wall_factorization.md).
With every right flag tag retained, an explicit bounded
homogeneous frame sends them to

    (a,b,p,p_1,s_M)=(0,1-X,infinity,(1-Z,1)^t,1). (1)

The fourth entry is a homogeneous column; no inverse of 1-Z
is taken. Put

    P(A)=sum_(h=0)^d (-1)^hQ^(h(h-1)/2)A^h/F_h,
    F_h=(Q;Q)_h,
    n=e_1S_2=(Q-Z^(-1))X, P=P(n),
    n_-= -e_1Z_2S_2.

The exact original uncheck crossing is

    R_0=D P(n_-)P.                               (2)

D is the original Cartan diagonal. Its common scalar line
kappa, framing and peripheral factors remain external and
identical throughout. The checked crossing is flip R_0
with that same line; none of these factors is reset.

## 2. The fifth clock is an actual quantum cross-ratio

Define

    H=P^(-1)ZP=Z(1-n)=Z+(1-QZ)X.                (3)

The finite Euler recurrence proves the middle equality.
Thus H is invertible, H^N=1 and nH=QHn, without taking
any singular reciprocal of 1-Z. Its commutative symbol is

    H_cl=X+Z-XZ,

the H appearing in the five cross-ratios of (1).

Let Psi be the full literature function with the exact
normalization in
[the modular moment theorem](actual_modular_dilog_circle_and_boundary_source.md).
Retain

    phi_N=sqrt(N) exp{i pi[1/4-(N+N^(-1))/12]}.

The elementary marked root evaluation, independently
proved in [the marked-flag note](actual_marked_full_phi_flag_pentagon.md),
gives

    F_Z=marked Psi(QZ)
        =phi_N diag_j[1/F_j], 0<=j<N.           (4)

The argument at clock index j is on logarithmic lift
2pi*i*(j+1)/N. Thus j=d uses the regular TOP value,
not the zero on the bottom lift. The finite missing arrow
of n lies at input j=0. The exact conjugation is

    F_Z n F_Z^(-1)=n(1-Z).                      (5)

Transport the **entire** clock mark, rather than choosing
a new one, by

    F_H=P^(-1)F_ZP.                              (6)

It is the marked full-Phi function of QH in this transported
integer frame. Equations (3), (5), and commutation of P with
n give

    F_H n F_H^(-1)=n(1-H).                      (7)

All matrices in (3)--(7) are invertible where claimed at
the physical root. The inverse of 1-H is not used.

## 3. The exact two-to-three word and the original R

Since n and -nH Q-commute and share nilpotent degree,
the finite ordered binomial theorem proves

    F_H P=P P(-nH)F_H.

Equivalently the literal two-to-three sequence is

    P(n)F_H^(-1)=F_H^(-1)P(n)P(-nH).            (8)

Multiplying by the displayed interface F_H gives an exact
refactorization of the original crossing, including every
exterior operator:

    R_0=D P(n_-) F_H^(-1)P(n)P(-nH)F_H.         (9)

The final F_H is a retained face/source adapter; deleting
it would change the original period. In a network one can
use (8) on that specified subword or (9) as a full crossing
replacement with its adapter. These are not definitions
of a new invariant.

## 4. All five developed arguments and the exact X-wall

Use the actual preceding factors to transport each argument
to the common input frame. The two arguments on the left
of (8) are n and the negative clock Z, since PHP^(-1)=Z.
The three on the right are the negative clock H and

    u=F_H^(-1)nF_H,
    w=-F_H^(-1)P nH P^(-1)F_H
      =-F_H^(-1)nZF_H.                           (10)

These are explicit finite matrices, and they simplify to

    K=X(1-E_0(Z)),
    u_Z=-Z^(-1)K,
    u=P^(-1)u_ZP,
    w=QK=QX(1-E_0(Z)).                          (11)

Here E_0 is the original first-clock zero-index projector.
It is the required finite source wall, not an omitted
exceptional case.

For a proof, F_Z^(-1)nF_Z=u_Z follows from consecutive
factorial ratios. Also

    n=u_Z+QK, u_Z(QK)=Q(QK)u_Z,
    P(n)=P(u_Z)P(QK).                            (12)

Every term of degree >=N vanishes because K is a strict
cut shift. Conjugation by P(u_Z) sends QK to
QK(1-u_Z)^(-1). Substitution of (6) into w in (10)
then gives

    w=P^(-1)[-u_Z Z(1-u_Z)^(-1)]P
      =P^(-1)[QK(1-u_Z)^(-1)]P=QK,

proving the last identity of (11) at all levels.

The corresponding exact ordered quad relation is

    r=wH^(-1)=-u(1-Q^(-1)u)^(-1), r^N=0.        (13)

The inverses in (12)--(13) exist because u is nilpotent.
They are not inverses of a clock determinant with a
nontrivial kernel.

Classically, away from the boundary divisors, (10)--(13)
become

    u_cl=n_cl/(1-H_cl)=-X/[Z(1-X)],
    w_cl=X,
    r_cl=X/H_cl,
    u_cl=r_cl/(r_cl-1).

Thus u is the negative-quad coordinate of the tetrahedron
with cross-ratio X/H, while w is the precisely cut X
tetrahedron. The developed signed list of (8) is therefore

    left:  [n_cl]-[Z],
    right: -[H_cl]-[X/H_cl]+[X].                 (14)

This is exactly the middle certificate of (1), since
n_cl=-X(1-Z)/Z is the positive-quad coordinate of its
omitted-a tetrahedron. It is not a five-point relation
for freely chosen unrelated flags.

Statement (14) identifies the rational geometric arguments
and their quantum cuts. It does not discard the nonlinear
factorial frames in assigning a positive tetrahedral
kernel or its complete phase. Those frames remain in
(4), (6), and the period construction below.

## 5. The complete original source is nonzero and polynomial

Keep the actual cup and full marker

    p=N sum_(a=0)^d x^(a-d)|a,d-a>,
    m|a,b>=x^b/N^2, mp=1.

Then exactly

    P(n)p=N|d,0>,
    Hp=Q^(-1)p,
    F_Hp=(phi_N/N)p.                            (15)

To prove the first identity, the coefficient of |u,d-u>
is N x^(u-d) times

    sum_(h=0)^(d-u) Q^(-h(u+1))
                  {u+h choose h}_Q
             ={N choose u+1}_(Q^(-1)).

The equality is the finite Gaussian hockey-stick identity.
At the primitive root it is zero for u<d and one for
u=d. The remaining identities in (15) follow from (3),
(4), and (6). In particular the actual cup selects the
TOP marked QH argument, with value phi_N/N.

Consequently both sides of (8) have the exact source value

    mP(n)F_H^(-1)p=phi_N^(-1).                  (16)

This is nonzero and has modulus N^(-1/2). In (9) the
retained final adapter has factor phi_N/N on the cup.
The full checked original crossing therefore has exactly
its old source value, including kappa and all original
framing/peripheral lines. The scalar has not been reset
to one in (8).

The complete cut correction is known at every order,
not just to first order:

    w^a=Q^a X^a(1-sum_(j=0)^(a-1)E_j(Z)),
    mw^ap=1-a/N, 0<=a<N.                        (17)

These formulas follow from the strict shift and the
original uniform marked clock distribution. Thus the
projector correction can be of order one at bulk a;
it is not legitimate to remove it because an individual
endpoint weight is 1/N.

At an interior position of a longer word one must keep
F_H as an operator and every projector of (17). The
scalar simplification (15) applies to this actual input
cup. The earlier counterexamples to untransported
interior cut relocation are unaffected.

## 6. Full-Phi/Fourier frames and all radial components

Every operator in (8)--(9) has an explicit fixed-complexity
full-Phi/Gaussian relative-period realization. Let

    T=J_(minus,1) tensor S_2,
    D_n|j>=lambda^j(-1)^jQ^(j(j-1)/2)|j>,
    H_n|j>=D_n(j)|j>/F_j.

Then the exact frames are

    n=H_n T H_n^(-1),
    u_Z=D_n T D_n^(-1),
    w=lambda T,
    H_n=phi_N^(-1)D_nF_Z.                       (18)

D_n is a unitary linear/quadratic Gaussian at unit
marks. T is the literal strict compression of a unit
shift; its missing Fourier/Hardy endpoint is exactly
the projector in (11), not a new boundary convention.
For unit S_2 all these cores have norm at most one.
Their inverses as Euler operators use the opposite
root/orientation, retaining its phase.

For each Euler polynomial in a contractive core use
the exact circle-minus-radial operator

    P_epsilon(T)=B_epsilon(T)-E_epsilon(T)

of the modular-circle theorem. For diagonal frames use

    (F_Z)_j=phi_N(-1)^jQ^(-j(j-1)/2)
                         [B_+(j)-E_+(j)],
    (F_Z^(-1))_j=(N/phi_N)Q^(-j-1)
                         [B_+(d-j)-E_+(d-j)].    (19)

All phases and the factors phi_N,N are retained. For
example P(-nH)=P^(-1)P(-nZ)P, and
-nZ=H_n(-TZ)H_n^(-1), another contractive core.
Equations (6), (18), and (19) therefore expand the full
word (9) into finitely many explicit Phi/Gaussian
integrals and their original coefficient cycles.

Every bracket in (19), and every transfer bracket, is
kept as B-E in its original order. Expanding their
product includes ALL circle/radial components with
their signs; no individual component is identified
with the whole original scalar. The radial kernel
alone has the proven harmonic or diagonal polynomial
bound, while other full-Phi factors can still give
an exponential period. No global domination estimate
is inferred from those local bounds.

The exact operator identity also transports every
actual Ward current: apply the ordinary typed product
rule to (8) or (9). In particular, the X-wall is
QXE_0=QE_dX, whose original current is explicitly

    [F_tot,E_dX]=(Q^(-1)-1)mu^(-1)
                              |d><0| tensor S_2^2.

It remains in (11), (17), and (19). The other current
terms are finite commutators of the displayed P,
F_Z and their inverses; differentiating the exact
operator word gives their equal full sum. This is
not a claim of sectorwise Ward vanishing.

## 7. Scope and exact audit

This provides the literal middle five-point relative
operator sequence, its original R embedding, its
marked full-Phi clocks, every strict projector moment,
and the nonzero original cup coefficient. It is an
actual finite identity at every N, including even N,
with no hypothetical source replacement.

To obtain a complete positive geometric tensor
presentation one must still assign these framed
operators to the proper oriented geometric face
kernels and transport the actual relative cycle.
The other two classical certificates are not declared
proved by (8). A local operator equality does not
give a global geometric intersection degree.

Run

    python3 experiments/audit_literal_middle_full_phi_certificate.py

The exact prime-field audit checks 27 complete/wrap
families through N=10: (8), the entire original R
word (9), the cut identities and every moment (17),
and the original source (15)--(16). The common
phi_N power is retained symbolically in those
homogeneous tests; its phase and modulus were
independently checked in the marked-full-Phi audit.
