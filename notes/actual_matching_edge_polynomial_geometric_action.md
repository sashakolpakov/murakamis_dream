# The selected scalar polynomial generates the actual recoupled transport

30 October 2026. At the complete original
channel, the canonical leading action of the actual target Casimir
polynomial has exactly the derivative required by the ACTUAL inverse
cyclic four-port turn. Its additive scalar constant is fixed by a
positive finite-source anchor. This is a classical marked-transport
comparison with an actual scalar asymptotic, not an asymptotic theorem
for the polynomial operator acting in the surrounding contraction.

The exact finite operator and all its original generic normals remain
those in [the geometric target polynomial theorem](actual_matching_edge_geometric_target_polynomial.md).
The actual selected scalar branch comes from the
[root-location and slit-domain theorem](actual_matching_edge_racah_root_location.md),
not from choosing a solution of a formal characteristic equation.

## 1. Follow the actual inverse turn

Use the original trace-minus-two incoming meridians

    A=-[[1,1],[0,1]], B=-[[1,0],[-4,1]],
    P=BA, H=P+I, C=I+bH,
    Aout=C A C^-1, Bout=C B C^-1.

The proved physical bend has tuple
`(Aout,Bout,B^-1,A^-1)`. Its target pairs the middle objects. To write
the target as an ordinary two-head operator one applies the INVERSE
of the original pivotal turn R. Its based tuple, up to one common
conjugacy, is

    (Bout,B^-1,A^-1,Aout),
    (Ain_target,Bin_target)=(Aout^-1,A),
    (Aout_target,Bout_target)=(Bout,B^-1).             (1)

Here is a direct basepath check of the cyclic order. If L_i are the
four original local lower Borel factors, their total product is I
for the invariant tensor. Rotating their local order from (1,2,3,4)
to (2,3,4,1) rotates their four based meridians and conjugates all of
them by L_1. Thus it has precisely the common-conjugacy effect just
stated. The finite pivotal clock in R is still present in the operator
identity; it gives no extra leading magnetic-momentum factor, since
its ratio under one physical index shift is q^-2 -> 1. Its actual
constant phase is NOT removed from the finite source.

The target ordered product is

    T=B^-1 Bout=A Aout^-1,
    Tr T=2+16b^2.                                    (2)

Set alpha=8b^2-4b+1. Direct calculation gives the genuine target
conjugator

    D=T-alpha I,
    D A D^-1=B^-1,
    D Aout^-1 D^-1=Bout,
    [D,T]=0, det D=-64b^4.                           (3)

In particular (3) retains WHICH ordered meridian is sent to which;
it is stronger than matching the target trace alone.

## 2. The physical rectangle determines its eigenratio

For the certified complete geometry the actual primitive marking gives
`b=-i/(2c)`, independently of the retained half-twist sign. Suppose
first `0<c<=1`, and write

    c=sech eta, eta>=0,
    Tr T=-2cosh(2eta),
    J=-exp(-2eta)=exp(2pi i xi),
    xi=1/2+i eta/pi.                                 (4)

This specifies the target eigenflag. On the two T-eigenlines the
conjugator D has eigenvalues J-alpha and J^-1-alpha. Its selected
eigenratio is therefore

    R_target=(J-alpha)/(J^-1-alpha)
       =(1+i sinh eta)/(1-i sinh eta)
       =exp(2i atan(sinh eta)).                      (5)

The opposite eigenflag inverts (5). Both (3) and the chosen expression
in (5) extend through eta=0. In the normalization that gives eigenvalue
one on the other flag, the parabolic limit is

    D_normalized=I+(i/2)(T+I) at eta=0.              (6)

This coefficient is a target transport parameter; it is not an
independently introduced crossing-circle cusp shape. In particular
there is no reason to assign it the orientation inequality of an
original auxiliary cusp.

## 3. The actual scalar source fixes the generating derivative

Let a_N/N->1/2 in the original folded range. The root-location theorem
proves local uniform convergence of the actual canonical logarithms

    N^-1 Log p_(a_N)(z) -> Psi_(1/2)(z)
                 on C minus [2,infinity).

Define the scalar action along the actual target trace by

    F(eta)=Psi_(1/2)(-2cosh(2eta)).                   (7)

For eta real and nonnegative, the positive finite-product proof gives

    F(eta)=max_(0<=v<=1/2)
       integral_0^v log[cos^2(pi s)
               *(cosh^2 eta-sin^2(pi s))/sin^4(pi s)] ds.

Its unique maximum is `v=atan(cosh eta)/pi`, the actual rectangle
parameter. Differentiation at the maximum gives an elementary exact
formula. In c=sech eta coordinates,

    dF/dc=-2/c * integral_0^(atan(1/c)/pi)
                                      ds/(1-c^2 sin^2(pi s))
          =-2 arccos c/(pi c sqrt(1-c^2)).

Using `dc/deta=-c tanh eta` proves

    F'(eta)=2 atan(sinh eta)/pi.                    (8)

The limit at eta=0 is zero. Its additive constant is fixed by the
ACTUAL positive source evaluation at z=-2:

    F(0)=4 integral_0^(1/4) log cot(pi s) ds
        =4 Catalan/pi=v8/pi.                        (9)

Thus no arbitrary period constant or logarithm winding was selected:

    F(eta)=v8/pi+(2/pi) integral_0^eta atan(sinh r) dr. (10)

These formulas hold holomorphically on `|Im eta|<pi/2`, with the branch
continued from eta=0. Indeed `-2cosh(2eta)` avoids [2,infinity) on that
strip. The analytic arctangent in (8) is its continuation from zero;
its derivative is `1/cosh eta`, with no pole inside the strip. The
identity theorem extends the real calculation. One must not substitute
a pointwise principal inverse trigonometric value after leaving the
real axis.

Because `xi=1/2+i eta/pi`, equation (8) is precisely

    partial_xi Psi_(1/2)(J+J^-1)
                       =-2i atan(sinh eta),
    exp[-partial_xi Psi_(1/2)(J+J^-1)]=R_target.       (11)

The sign in (11) is the actual spectral-multiplier sign. Let Theta be
the original fully normalized algebraic two-column generating phase.
We use it here as the already proved classical character relation,
not as a new asymptotic for a column at the complex target color.
Its algebraic critical-character map says
`exp(partial_xi Theta)=R_target`. Multiplication by the scalar source
polynomial adds `Psi_(1/2)(J+J^-1)` to that phase. Target-channel
stationarity is therefore

    exp(partial_xi[Theta+Psi])=1,

exactly (11). It is NOT `R_target=exp(partial_xi Psi)`. This calculation
uses the original inverse turn (1), the physical ordered matrices (3),
and the canonical scalar branch (7).

## 4. General input color gives the actual four-parabolic character relation

The same comparison holds for EVERY fixed real INPUT parameter
`0<alpha<=1/2`, not only the complete input alpha=1/2. Keep it distinct
from the TARGET parameter `xi=1/2+i eta/pi`. Put

    lambda_input=2cos(2pi alpha), s=sin(pi alpha),
    z=J+J^-1=-2cosh(2eta),
    F_alpha(eta)=Psi_alpha(z).

Here Psi_alpha is again the actual selected scalar limit proved by the
finite polynomial root theorem. For eta>0 its positive variational
formula has unique maximum satisfying

    sin^2(pi v_*)=s^2 cosh^2 eta/(s^2+cosh^2 eta).

Differentiate its original integral at that maximum. With
`t=tan(pi v)`, the integral of
`1/(cosh^2 eta-sin^2(pi v))` is elementary. It gives

    partial_eta F_alpha
      =(2/pi) atan[s sinh eta/sqrt(1+(1-s^2)sinh^2 eta)]
      =(2/pi) asin(s tanh eta).                       (12)

Both inverse functions in (12) are continued from zero; for positive
real eta their values lie in `(0,pi alpha)`. For example the equivalence
follows by squaring the tangent and using `1+sinh^2 eta=cosh^2 eta`.
Thus the selected scalar multiplier gives the eigenratio

    R_alpha=exp[-partial_xi Psi_alpha(J+J^-1)]
           =exp[2i asin(s tanh eta)],
    R_alpha+R_alpha^-1
        =2-(2-lambda_input)(z+2)/(z-2).              (13)

This is precisely the ACTUAL four-parabolic trace equation in the
inverse-turn convention (1), as can be proved without importing a
character-variety formula. Diagonalize the target product
`T=diag(J,J^-1)` and write its second incoming meridian as

    B_t=[[b11,b12],[b21,b22]],
    Tr B_t=Tr(B_t^-1 T)=-2, det B_t=1.

The two trace equations give

    b11=-2J/(J+1), b22=-2/(J+1),
    b12 b21=-(J-1)^2/(J+1)^2.                       (14)

For a target centralizer with eigenratio R, take `D=diag(R,1)`.
The original input product is, BY THE ACTUAL INVERSE TURN,
`(D B_t D^-1)^-1 B_t`. Therefore

    lambda_input=Tr(D B_t^-1 D^-1 B_t)
       =2-[(J-1)^2/(J+1)^2](2-R-R^-1).             (15)

Since `(J-1)^2/(J+1)^2=(z-2)/(z+2)`, equations (13) and (15)
are identical. This proves the generating relation for general input
trace, not just the number of its roots. At alpha=1/2 the explicit
physical collar computation (3)--(5) fixes WHICH of the two inverse
eigenratio branches is the marked one. Continuing that branch in alpha
gives (13); no new arbitrary sign is selected at each input value.

The expressions extend on `|Im eta|<pi/2` using the same scalar slit
branch. The parabolic target eta=0 has the finite normalized limit

    D_normalized=I+(i s/2)(T+I).

Its source trace is `2+16(i s/2)^2=lambda_input`, as it must be.
This is a classical parabolic limit, not a substitute for an actual
generic-q normal. For the analytic rectangle parameter c>1 one may take
`eta=i arccos(1/c)` inside the same strip; the continued marking agrees
with the real physical target in the preceding theorem. This statement
does not assert that any finite real-color contour can be moved there
without poles or without additional contributions.

The additive value of each general-input scalar action is already
fixed by its actual positive finite-source limit at any z<-2, followed
by the slit-domain continuation. No additive period is inferred from
(13) alone. Equation (9) is the explicit complete-input anchor.

## 5. What has and has not been compared

The target trace, the ordered target conjugator, its selected eigenratio,
and the entire scalar generating derivative now agree with the actual
recoupled geometry. The scalar action has its finite-source anchor (9).
The original generic identity remains `D_a^-1 p_a(Omega)` before every
normal extraction; at root `D_a=1`, and its fixed scalar generic jets
have the already proved polynomial relative bound on compact real
targets below -2. No generic normal is replaced by a root derivative.

Equation (11) is a comparison at the actual classical critical point.
The algebraic ordinary-column character map is valid on its regular
complex channel chart, but the existing ordinary-column ASYMPTOTIC
theorem keeps that channel real and discrete. This note does not extend
that theorem to (4). Nor does scalar convergence in (7) establish the
action of the degree-O(N) polynomial p_a(Omega) on the complementary
selected boundary state. Establishing that action, its actual phase,
and its contribution to the original finite source remains necessary.

In particular (9) is a scalar anchor, not a new proof that an assembled
marked critical action equals the complement volume. Any such assembly
must also retain the pivotal clock, original row and half-twist factors,
native measures, shared wires, and the full physical normal already
specified by the exact source identities.

Audit: [actual inverse turn, ordered transport and scalar generating action](../experiments/audit_actual_matching_edge_polynomial_geometric_action.py).
It proves four symbolic ordered-matrix identities, all four cyclic
prefix identities, the exact eigenratio and parabolic normalization,
and the rational Cayley identity fixing the sign. Five further symbolic
identities check the generic target pair and its original-input trace
relation. At 90 digits it checks
three independent action integrals, twelve actual source-polynomial
actions and first derivatives, four endpoint second derivatives,
and twelve general-input scalar derivatives and character equations,
at both level parities. No operator or network asymptotic is tested.


The action uses the stated analytic c>1 continuation without claiming that it is realized by a complete geometric rectangle. No polynomial-operator substitution or source-cycle contribution follows.