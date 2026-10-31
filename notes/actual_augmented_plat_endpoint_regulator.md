# The actual augmented-plat endpoint action has its diagram regulator

30 October 2026. At the complete channel endpoint, the fully normalized
q-Hahn coupon phase has the SAME Bloch–Wigner regulator as its original
crossing-circle diagram, for every retained half twist. This is an
absolute comparison: an exact rational wedge calculation gives a constant
regulator difference, and a connected real chart proves that constant is
zero. It is not an inference from matching peripheral derivatives.

Consequently any regular, correctly marked geometric critical point of
the assembled endpoint phase has critical rate equal to the volume of the
actual augmented link. Existence of such a point on the source's required
logarithmic sheet, a contributing cycle, and a nonzero controlled amplitude
are separate questions. This note does not prove a source asymptotic.

## 1. The complete normalized endpoint symbol

Use the original phase Theta_epsilon from
[the local character calculation](actual_augmented_plat_local_critical_character_map.md),
equation (1), with its inverse-measure factor H, both q-Hahn columns,
and the retained half twist epsilon in {0,+1,-1}. Write

    T=exp(2pi i tau), U=exp(2pi i u), V=exp(2pi i v),
    Z=exp(2pi i alpha), W=exp(2pi i beta).

At xi=1/2, J=exp(2pi i xi)=-1 and J0(1/2)=0. Adding H to the two
column factorial actions cancels the terms J0(tau-1/2). The remaining
factorial part is

    J0(u)+J0(tau-u)+J0(v)+J0(tau-v)
      -2[J0(alpha)+J0(1/2-alpha)+J0(beta)+J0(1/2-beta)]
      -J0(u-alpha)-J0(tau-u-1/2+alpha)
      -J0(v-beta)-J0(tau-v-1/2+beta).                 (1)

The retained polynomial phase is

    pi i [(u+v)/2+(tau-1/2)(alpha+beta)
                                +tau+3(epsilon-1)/4]. (2)

On the original factorial branch,

    2pi i J0(s)=-Li2(exp(2pi i s))
                       +pi^2(s^2-s)+Li2(1).          (3)

One verifies (3) by differentiation from 0<s<1 and the common value at
s=0, then analytically continues with the recorded logarithmic marks.
Thus the Bloch symbol of 2pi i Theta_epsilon is

    B_H=B(U,Z)+B(V,W),
    B(X,z)=-[X]-[T/X]+2[z]+2[-1/z]+[X/z]+[-Tz/X].     (4)

The half-twist term in (2) contributes a REAL constant to 2pi i Theta,
so it contributes no regulator. It does still change the actual auxiliary
meridian needed to realize the same main-input/main-output relation.
Neither that change nor the coefficient 2 in (4) may be discarded.

## 2. A rational chart for the endpoint critical correspondence

Both actual internal q-Hahn equations at J=-1 are rationally
parameterized by

    Z=(a-1)/(a+1), U=T(a-1)^2/(Ta^2+1),
    W=(b-1)/(b+1), V=T(b-1)^2/(Tb^2+1).              (5)

Indeed a=(1+Z)/(1-Z), and direct substitution gives the quadratic
P(U,Z)=0 of the local character calculation; the same holds for V,W.
Every regular endpoint root is represented by this chart away from the
listed denominators. The chart has coordinates (T,a,b) in a nonempty
Zariski-open subset of C^3. A common nonzero magnetic scale can be fixed
at one: it simultaneously conjugates the head matrices and does not
change any crossing symbol below.

For clarity all reconstructions use the actual physical head matrices

    K=-1/X, F=S(1-X), E=(X^-1-1)/S,
    Lminus=[[1,0],[-KF,K]],
    G=[[K,E],[FK,FE+K^-1]].                           (6)

Put

    Y(X,z)=-(1-X)(Tz+X)/[(X-z)(T-X)],
    D=ZW(T-U)(T-V)/[(TZ+U)(TW+V)].                   (7)

In the low physical degree chart the input heads (X,S) are

    (V,Y(V,W)), (T/V,1),

and the output heads are

    (U,1/[D Y(U,Z)]), (T/U,1/D).                     (8)

Let A=G1, B=Lminus1^-1 G2 Lminus1, P=BA, H=P+I.
Then H is nonzero nilpotent and the endpoint transport is

    C=I+cH, c=(2Tab-Ta-Tb+a+b-2)
                        /[2(T+1)(a-1)(b-1)].       (9)

This follows either by multiplying the explicit matrices or by
c=Tr([H,A]A_out)/32. In particular C A C^-1=A_out. The full ordered
product P, including its Borel frame, is preserved.

For the HIGH physical degree chart one must use the actual affine
index adapter, rather than substitute the physical pair product into
(4). Its input and output heads are respectively

    (V/T,Y(V,W)), (1/V,1),
    (U/T,D Y(V,W)), (1/U,D Y(U,Z)Y(V,W)).             (10)

The low variables in (4),(5),(7) remain unchanged. The exact finite
high-block identification has no extra phase or scalar. Formula (6)
with (10), followed by c=Tr([H,A]A_out)/32, gives exactly the same coefficient (9) in the high physical
chart. The executable certificate checks it independently with
the same original crossing rule below.

## 3. Reconstruct the actual auxiliary meridian and every crossing

The positive Hurwitz half twist on a trace -2 pair is simultaneous
conjugation by P^-1-I. At P=-I+H its projective normalization is
I+H/2. Therefore the raw, trace -2 auxiliary meridian for the original
coupon R^epsilon L_N is

    C_aux,raw=-[I+(epsilon/2-c)H].                    (11)

This sign is its actual complete raw lift; the corresponding physical
meridian has trace +2. The literal threading word [2,1,1,2] transports
the main pair by C_aux^-1 and closes the auxiliary because it commutes
with P. Composing its main half twist gives total conjugator I+cH.
This uses the
[proved original peripheral word](actual_mixed_crossing_circle_preferred_longitude.md),
not an assigned auxiliary longitude.

To recover the actual THIRD Gauss head from (11), let
L=Lminus2 Lminus1 and set G3=L C_aux,raw L^-1. Its coordinates are

    K3=(G3)11, E3=(G3)12, F3=(G3)21/K3.              (12)

Now execute chronological adjacent crossings [2,1,1,2], and then the
signed main crossing R^epsilon if epsilon is nonzero. All maps here
are rational. For two input heads (k,e,f),(l,g,h), the original positive
crossing, with d=1-eh, is

    (ld, [dg+e(dl-l^-1)]/k, kh/d),
    (k/d, e/(ld), l[df+h(d/k-k)]).                    (13)

With physical clocks A0=-1/k, B0=-1/l its five-dilog symbol is

    [B0]+[1/d]+[1/A0]-[B0/d]-[1/(dA0)].             (14)

The original negative crossing has c0=1-(B0/A0)gf and outputs

    (lc0, kg, f+h/k-f/(l^2c0)),
    (k/c0, le+g-k^2g/c0, f/l),                       (15)

with symbol

    [A0]+[c0]+[1/B0]-[A0c0]-[c0/B0].                (16)

Call the sum of these FOUR or FIVE actual symbols B_disk,epsilon.
Direct rational substitution checks all nine final Gauss coordinates:
the first two heads are exactly (8) or (10), and the auxiliary head is
exactly (12) again. Thus this is the actual original closed circle, not
an abstract centralizer with a missing closing/pivot convention.

The closing pivot is a monomial; its complete leading contribution and
the main marked cup/cap phases are included in (2) and the global source
characters. They contribute no extra dilogarithm symbol. A monomial can
still change an action value off stationarity; section 5 treats that
point explicitly.

## 4. Exact wedge identity and absolute real normalization

With delta[z]=z wedge (1-z), the following identity holds over the
rational function field Q(T,a,b), for BOTH physical degree charts and
all epsilon in {0,+1,-1}:

    delta(B_H-B_disk,epsilon)=0.                      (17)

Here is a finite algebraic certificate for (17), including its procedure
so no fitted regulator or floating point identity is involved. Use (5)
in (4); construct B_disk by (6)--(16); factor every argument and its
complement into irreducible polynomials over Q. For an argument z write
v_z for its integer exponent vector, retaining positive rational prime
factors as well as polynomial factors. Then expand

    sum_(coefficient n, argument z) n
                                  (v_z v_(1-z)^t-v_(1-z) v_z^t). (18)

The matrices from (4) and (14),(16) are identical. Only the torsion sign
-1 is removed in this rational exterior square; factors such as 2 are
kept. The accompanying audit performs precisely (18), symbolically,
and records every rational argument and the empty difference matrix.
It also independently checks (9)--(13) and the complete auxiliary closure.
Thus (17) is an identity of rational functions, not evidence from a finite
sample of shapes. One compact form of the COMMON wedge, useful for checking
the expansion without comparing two large symbol lists, is as follows. Put

    A_r=2Tr-T+1, B_r=Tr-r+2, F_r=Tr^2+1.

Then BOTH sides expand to

    2 T wedge (T+1)
      +sum_(r=a,b) [ A_r wedge T - A_r wedge F_r
          +2 A_r wedge (r-1) + B_r wedge F_r
          -2 B_r wedge (r-1) + F_r wedge r
          +2 r wedge (r-1) ].                        (18a)

There are exactly fifteen nonzero coefficients in this polynomial-factor
basis. In particular the mixed factors involving both a and b from the
actual four-crossing diagram cancel; this is a global identity for the
whole coupon, not equality of independent crossing maxima.

For any Bloch symbol B the differential of its Bloch–Wigner regulator
factors through delta B:

    dD(z)=log|z| dArg(1-z)-log|1-z| dArg z.

Therefore (17) makes D(B_H-B_disk,epsilon) constant on its regular
complex parameter chart. This chart is connected: it is obtained from
C^3 by deleting finitely many proper polynomial hypersurfaces, and two
generic points can be joined by complex lines avoiding their finitely
many excluded intersection points. Every rational expression has real
coefficients, so the chart contains a generic real point. At that point
every argument is real and every Bloch–Wigner value is zero. Consequently

    D(B_H)=D(B_disk,epsilon).                         (19)

This is the required ABSOLUTE regulator identity. Wedge equality alone
would not prove it. Nor does (19) claim equality of integral Bloch classes,
flattenings, or complex periods: rational wedge zero can retain information
not measured by D. Changes of logarithmic sheet must continue to carry
the original integer marks in the action.

## 5. Assemble the actual diagram and the critical action

Apply (19) at every original twist-region coupon. The actual disk words
and retained half crossings, with the actual outside wires and caps, form
the original augmented-link diagram. The crossing-block proof in
[the marked fundamental-cycle calculation](crossing_fundamental_cycle.md),
sections 2--4, is componentwise: its local octahedral balls, arc-strip face
identifications, and degree-one cusp truncation apply to this multi-component
diagram as well. No step joins different components or replaces their
preferred peripheral paths. The knot-only shortcut H2(M)=0 is NOT used:
for a compact connected oriented link exterior H3(M)=0, so the exact
sequence makes H3(M,partial M) -> H2(partial M) injective. The displayed
degree-one cycle on EACH oriented cusp is precisely the boundary of the
relative fundamental class, and hence fixes the relative class uniquely.
Accidental developed crossing degeneracies can be avoided by adding their
finitely many divisors to the generic frame exclusions, or handled by the
continuous extension D(0)=D(1)=D(infinity)=0. Thus at the complete geometric representation

    sum_regions D(B_H)=Vol(actual augmented link).    (20)

One can use an actual positive gluing certificate to supply that geometric
representation; (20) does not assume convexity of a particular source
polytope or independently maximize individual regions.

To pass from a Bloch symbol to the original action value, keep the full
stationarity condition. In logarithmic variables z=rho+i theta the
assembled action G=2pi i phi has the form

    G=sum n_j Li2(exp(a_j dot z+i pi nu_j))
                         +(1/2)z^t C z+i k dot z+c0,

with real a_j,nu_j,C,k and Im c0=0, and C symmetric. This follows directly
from (1)--(3), the original monomial cup/cap phases, and the retained
integer logarithmic characters. For matching branches the exact identity is

    Im G-sum n_j D(exp(a_j dot z+i pi nu_j))
                                  =rho dot Im(gradient G). (21)

It follows by expanding Im Li2, the real quadratic, and the imaginary
linear term; the full proof is in the repo's
[wall regulator calculation](actual_wall_critical_regulator.md), section 3.
At a FULL stationary point on the recorded marked sheet the right side
vanishes. If the channel is held at its endpoint rather than varied, its
logarithm is log J=i pi modulo 2pi i and has rho_J=0, so its unsolved
normal derivative contributes nothing to (21). All remaining free magnetic
and internal variables still require their actual stationary equations.
A constrained endpoint extremum in some other complex variable is not
enough.

Therefore, whenever the complete geometric character is realized by a
regular correctly marked full critical point of this actual endpoint phase,

    2pi Re phi(0)=Im G(0)=Vol(actual augmented link).  (22)

The original exterior framing factors of unit modulus add real constants
to G and preserve (22). Equation (22) fixes the complete-volume ANCHOR
needed alongside the proved primitive differential

    dG=(1/2) sum_i V_i dU_i.

It does not prove a global lift to the required source sheet, a quantum
cycle coefficient, a nonzero leading amplitude, a bound on competing or
singular regions, or a mixed-color complex corridor. In particular no
source limit or general long-filling theorem follows from (22) alone.

Audit: [exact six-chart regulator comparison](../experiments/audit_actual_augmented_plat_endpoint_regulator.py),
[recorded results](../experiments/actual_augmented_plat_endpoint_regulator_results.json).

The endpoint regulator retains the stated sheet, cycle, amplitude and source-asymptotic limitations.