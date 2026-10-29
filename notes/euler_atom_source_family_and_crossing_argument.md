# Euler-factor source families and the literal crossing argument

27 October 2026. Multiplying the actual primitive gauge period by one
Euler factor gives an exactly solvable inverse-factor family. At the
resonant shifts a=Q^r it transfers the selected local period from the
Gaussian point 2 to the boundary point 0. This is a real source effect
of an N-dependent unit, rather than an inference from its classical
symbol. A further forward Euler factor has a nonreal formal critical
pair; its selected asymptotic is not proved here.

The Euler polynomial is literally the one in the original R-matrix.
Its ARGUMENT must also be retained: the physical R atom and the right
source variable are different operators. We prove this distinction,
and give the exact literal signed crossing coefficients in the actual
two-leg Borel fusion. No family below is substituted for the original
knot invariant.

## 1. The actual atom and its right-source argument are distinct

Fix q=exp(pi*i/N), Q=q^2, rho=q-q^-1, N>=2. Write

    F_k=(Q;Q)_k,
    u_N(z)=sum_(k=0)^(N-1) z^k/F_k,
    v_N(z)=sum_(k=0)^(N-1) (-1)^k Q^(k(k-1)/2)z^k/F_k.

In the normalized actual unchecked crossing the nilpotent factor is

    Theta=v_N(X), X=q rho^2 E_1 F_2,
    Theta^-1=u_N(X).                              (1)

This follows coefficient by coefficient from the original coefficient
q^(k(k-1)/2)rho^k/[k]_q!, since

    [k]_q!=q^(-k(k-1)/2)F_k/(1-Q)^k,
    rho(1-Q)=-q rho^2.

It agrees with [the existing actual-atom proof](controlled_cyclic_euler_source.md).
Every Cartan, flip, framing and peripheral line remains its original
factor. Formula (1) does not replace that whole crossing by one scalar
Euler function.

The [actual source gauge](actual_source_fourier_twisted_traces.md)
instead uses z=xf in the RIGHT coefficient algebra of Borel fusion.
On the physical two-leg regular module its right operator has rank
N(N-1). At the complete color, both E_1 and F_2 have rank N-1,
so the physical X in (1) has rank (N-1)^2. Hence these two
nilpotent operators cannot be similar for any N>=2. Their Euler
units minus identity have the same respective ranks, because their
linear coefficients are units and the remaining factor is invertible.

Thus u_N(a z) below is an explicit actual-source COUPON using the
same Euler polynomial as the literal inverse R atom. It cannot be
called a complete crossing insertion by equating its argument with
X. A whole crossing comparison has to carry its actual fusion,
weight-diagonal factor and finite-path support as well.

## 2. Exact signed crossing coefficients in the actual Borel fusion

In the actual two-leg fusion C, with z_(a,k)=f^a e_k, remove only
the recorded common Cartan scalar kappa from the positive crossing.
Its unique RIGHT coefficient is exactly

    a_+=sum_(a,k>=0,a+k<N)
       (-1)^k x^(-a-2k) Q^(k(k-1)/2) f^a e_k/F_a. (2)

The inverse crossing, with scalar kappa^-1 recorded, has coefficient

    a_-=sum_(a,k>=0,a+k<N)
       (-1)^k x^(a+2k) Q^(-k(k-1)/2-ka) f^a e_k/F_a. (3)

Here x is the actual same-color highest K eigenvalue and M=-qx;
the formulas hold at fixed root for generic M and at completeness.
They are not obtained by a numerical fit at M=1.

For a direct proof of (2), the actual positive crossing sends
e_0 tensor e_j to x^-j e_j tensor e_0. The fusion kernel is

    C_(u,v;a,k)=x^(u-a) F_a F_v/[F_(a-u)F_k],
    0<=u<=a, v=k+a-u<N.

It preserves the unwrapped total degree a+k=u+v. Fixing that
degree j, solve its triangular system for the right coefficient.
The finite Euler inverse convolution gives

    F_a [f^a e_k]a_+=(-1)^k x^(-a-2k)Q^(k(k-1)/2),
    a+k=j<N,

and there are no coefficients with a+k>=N. This proves (2).
The nonwrapped paths form a triangular subalgebra. Its diagonal
weights are d_k=(-1)^k x^-2k Q^(k(k-1)/2); inversion of its
Euler factor gives (3). It also follows by direct multiplication
of (2) and (3) in the full actual coefficient algebra.

The completed expression u_N(x^-1 f) D(H), D e_k=d_k e_k,
has the same coefficients as (2) on nonwrapped paths. Its wrapped
terms require their own source comparison; they may not be erased
from a general inserted word simply because one two-leg cap kills
them. At M=1 its Euler argument is

    x^-1 f=x^-2 z=Q z.                             (4)

Thus the actual crossing's right Euler profile is related to the
resonant a=Q case below, rather than an unmarked replacement of
its argument by z. The diagonal D and the source-supported finite
path information remain essential for the whole crossing.

## 3. The full inverse-factor family has a retained norm source

Let

    g_N(z)=v_N(z)v_N(Qz) modulo z^N,
    w^-_(N,a)(z)=g_N(z)u_N(a z) modulo z^N,
    J^-_N(a)=[z^(N-1)]w^-_(N,a)(z).                (5)

All use their canonical degree-<N representatives. The exact
parameter polynomial is

    J^-_N(a)=(1/N)sum_(k=0)^(N-1)
                            product_(r=0)^(k-1)(a-Q^r). (6)

To prove (6), the finite q-binomial coefficient identity gives

    [z^k]v_N(z)u_N(a z)
          =a^k(a^-1;Q)_k/F_k
          =product_(r=0)^(k-1)(a-Q^r)/F_k.

It is polynomial at a=0 as well. The reflected coefficient of
v_N(Qz) at degree N-1-k is F_k/N. Convolution cancels the
remaining factorial and yields (6).

Writing P_k(a)=product_(r=0)^(k-1)(a-Q^r), the identity
P_k(Qa)=Q^k(a-Q^-1)P_(k-1)(a) and
P_(k+1)(a)=(a-Q^k)P_k(a) yield the exact parameter transport

    J^-_N(Qa)=(Qa-1)(a-1)J^-_N(a)
                              +(Qa/N)(2-a^N).      (7)

The complete norm P_N(a)=a^N-1 enters its derivation. The
source 2-a^N cannot be replaced by its value at a marked point
before transporting the parameter.

The entire canonical wave in (5), before setting z^N=0, obeys

    (1-z)(1-Qz)w^-_(N,a)(Qz)-(1-a z)w^-_(N,a)(z)
           =[(a^N-2)/N]z^N+J^-_N(a)z^(N+1).     (8)

All lower coefficients follow from nilpotent Euler cancellation.
For the degree-N coefficient, use the ordinary polynomial identities
u_N(aQz)=(1-a z)u_N(a z)+a^N z^N/N and the full gauge Ward
equation. Their source gives (a^N-2)/N. Truncating a product's
degree-N tail does not change that coefficient because Q^N-1=0.
The degree-N+1 coefficient is the displayed top period. This
proves (8) without treating evaluation as a nilpotent character.

For moments j_m=[z^(N-1)]z^m w^-_(N,a), (8) implies exactly

    j_(m+2)=(1+Q-aQ^(m+2))j_(m+1)
                                +(Q^(m+2)-Q)j_m,
    j_0=J^-_N(a),
    j_1=(1+Q-aQ)J^-_N(a)+Q(a^N-2)/N.            (9)

The generic cleared classical source support is
z(z+a-2)=0. That polynomial alone does not select its branch.

## 4. A proved source branch transfer at resonant inverse atoms

For fixed r>=0 and N>r, take a=Q^r. Exact Euler transport gives

    w^-_(N,Q^r)(z)=v_N(Qz)(z;Q)_r modulo z^N.     (10)

For a fixed polynomial P, the BASE period on v_N(Qz) is

    L_N(P)=[z^(N-1)]P(z)v_N(Qz)
           =(1/N)sum_m [z^m]P(z) F_m,            (11)

once N exceeds its degree. Since F_0=1 and F_m=O_m(N^-m)
for every fixed m>=1, (10)-(11) prove

    J^-_N(Q^r)=N^-1[1+O_r(N^-1)],
    [z^(N-1)]P(z)w^-_(N,Q^r)(z)/J^-_N(Q^r)
                               -> P(0),          (12)

with error O_(P,r)(1/N). Its original period is nonzero for all
sufficiently large N and has zero exponential rate. In particular

    J^-_N(1)=1/N, J^-_N(Q)=Q/N                  (13)

exactly. Before adding this inverse factor, the gauge period is
c_N~omega_N/sqrt(N), and its fixed polynomial observables select
2. After the factor the Gaussian leading component disappears
and the evaluated boundary source selects 0. The actual finite
period has not vanished; its leading source class has changed.

At a=1 this can also be seen from the minimal Ward equation:
w^-=v_N(Qz), so

    (1-Qz)w^-(Qz)-w^-(z)=-z^N/N.

Its classical source support is only z=0. The extra root z=1
of the generic cleared polynomial z(z+a-2) at a=1 comes from
an unremoved factor 1-z. It cannot be used as a selected
critical point. Source saturation is necessary at the resonant
atom, even though the multiplying Euler polynomial is a unit
in the nilpotent algebra.

Thus fixed-degree source selection cannot simply be extended to
all Euler units. This is an exact family of source probes built
from the actual atom polynomial. It is not a statement that a
literal complete R crossing, including D(H), always destroys a
Gaussian branch.

## 5. Adding a forward factor gives a different critical problem

For completeness define the other actual-polynomial source probe

    w^+_(N,a)=g_N(z)v_N(a z) modulo z^N,
    J^+_N(a)=[z^(N-1)]w^+_(N,a),
    b^+_N(a)=[z^(N-2)]w^+_(N,a).

Its full unreduced Ward equation is

    (1-z)(1-Qz)(1-a z)w^+_(N,a)(Qz)-w^+_(N,a)(z)
      =-[(2+a^N)/N]z^N
       +[(1+a+aQ^-1)J^+_N(a)-aQ^-1 b^+_N(a)]z^(N+1)
       -aJ^+_N(a)z^(N+2).                       (14)

The degree-N source follows by multiplying the exact Euler and
gauge Ward equations; it retains 2+a^N. The remaining two
coefficients are read from the cubic factor and the top two
canonical coefficients. This is an exact recursion/source
statement, not an assertion about which critical class survives.

At a=1 its classical equation is (1-z)^3=1. Besides the
boundary root zero it has the two nonreal points

    z_+=3/2+i sqrt(3)/2, z_-=conjugate(z_+).

On the marked upper branch, the coefficient action
S_+(z)=3Li_2(z)-2pi*i Log z is stationary at z_+, since
Log(1-z_+)=-2pi*i/3. Its imaginary part is exactly

    Im S_+(z_+)=3D(z_+)=2D(exp(pi*i/3)).           (15)

For example the cross-ratio triangle has angles pi/6,pi/6,
2pi/3, so D(z_+)=2Lambda(pi/6)-Lambda(pi/3)=2Lambda(pi/3).
The elementary duplication identity gives (15). This is the
same positive regulator number calibrated for the original
figure-eight source in [its independent Bloch calculation](figure_eight_bloch_specialization.md).

No selected asymptotic for J^+_N(1) is proved here. Numerical
rate samples are saved as diagnostics only. Neither a nonreal
formal critical point nor the equality of the regulator number
in (15) identifies this universal source probe with a knot
invariant or supplies its nonzero thimble coefficient.

## 6. Verification and critical-path consequence

The [exact audit](../experiments/audit_euler_atom_source_family.py)
and [saved results](../experiments/euler_atom_source_family_results.json)
pass 23 levels, 115 parameter cases, both unreduced Ward families,
the exact parameter transport and resonant fixed-observable
selection formulas. Twelve literal crossing tests at complete
and generic meridians verify (1)-(3) directly from the original
color matrices and actual fusion. The rank mismatch of the two
atom arguments is checked at every complete test.

The inverse-family result gives a real source-branch transfer
and identifies the exact resonant saturation that any full-word
theorem must handle. The signed crossing formulas specify what
is additionally needed to pass from the Euler function family
to a literal crossing. Nothing here replaces the original state
by a positive model, asserts new move invariance, or proves the
general volume conjecture.
