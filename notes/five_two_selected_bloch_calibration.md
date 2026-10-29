# Exact Bloch and hyperbolic calibration of the selected five-crossing phase

28 October 2026. This identifies the critical value of the EXACT original
two-index source in [the finite transform](five_two_cyclotomic_transform_proof.md).
It does not infer a volume limit from the existence of that critical
point. Selection of the finite contour is separate.

## 1. The algebraic point and its logarithmic marks

Let rho be the positive real root of rho^3+rho^2-1=0, and put

    v=(1+rho)/2+i sqrt(1/rho-(1+rho)^2/4).

Then v is the upper nonreal root of v^3-v^2+1=0. In particular

    1-v=v^(-2), v^3=v^2-1, v^5=-(1+v).
    X=1/(1+v^2), Y=-v, Z=X/Y,
    x=1+Log(X)/(2pi i), y=1+Log(Y)/(2pi i).       (1)

The logarithms on the right are principal; X,Y lie in the lower
half-plane. Thus 1/2<Re y<Re x<1. Use the marked primitive

    J(z)=integral_0^z Log(2sin(pi t))dt,
    S(x,y)=3J(x)-J(y)-J(x-y)
                    +i pi(3x+2y-x^2-xy-y^2).                (2)

All three arguments have real part strictly between zero and one.
The stationary equations, with the actual marks, are

    3Log(1-X)-Log(1-Z)-2(2pi i x)-(2pi i y)+4pi i=0,
    -Log(1-Y)+Log(1-Z)-(2pi i x)+2pi i=0.                   (3)

Their exponentials are verified by reducing in Q[v]/(v^3-v^2+1):

    (1-X)^3=X^2 Y(1-Z),  1-Z=X(1-Y).                       (4)

There is no unnoticed integer in (3). For example rho is between
7548/10000 and 7549/10000 by direct polynomial signs and strict
monotonicity. Formula (1) then isolates v in the first quadrant
near .87744+.74486i, X near .38150-.41040i, and Z near
-.02193+.48634i. Principal arguments give

    Arg(1-X) in (.57,.61), Arg(1-Z) in (-.50,-.40),
    Im(2pi i x) in (5.44,5.50),
    Im(2pi i y) in (3.82,3.86).

The imaginary part of the first expression in (3) is therefore
between -.19 and .20; its real part is zero by (4), so the
integer multiple of 2pi i is zero. The second expression is
handled by 1-Z=X(1-Y): both Log(1-Z)-Log(1-Y) and principal
Log X have arguments in (-pi,0). This proves the marked
stationary equations exactly.

## 2. The critical action is its Bloch regulator

Write D for the Bloch--Wigner dilogarithm,

    D(z)=Im Li_2(z)+log|z| Arg(1-z).

With l_X=2pi i x and l_Y=2pi i y, direct differentiation and
evaluation at zero give

    2pi i S=Li_2(1)-3Li_2(X)+Li_2(Y)+Li_2(Z)
                     -l_X^2-l_X l_Y+2pi i(2l_X+l_Y).        (5)

All dilogarithms have the branches inherited from 0<Re z<1;
their arguments avoid [1,infinity). Set a=Re l_X, b=Re l_Y,
A=Im l_X, B=Im l_Y. The imaginary part of the polynomial
term in (5) is

    a(4pi-2A-B)+b(2pi-A).

Taking imaginary parts of (3) shows that this equals

    -3log|X| Arg(1-X)+log|Y| Arg(1-Y)
                                  +log|Z| Arg(1-Z).

Consequently, with no unrecorded additive constant,

    2pi Re S(x,y)=-3D(X)+D(Y)+D(Z).                         (6)

## 3. An explicit finite Bloch identity

The right side of (6) is exactly 3D(v). Here is a short proof
using only the six cross-ratio symmetries, duplication, and one
five-term relation.

First 1-v=v^-2 gives D(v^2)=D(v). Duplication
D(z^2)=2D(z)+2D(-z) gives

    D(-v)=-D(v)/2.
    D(-v^2)=D(X), since X=1/(1+v^2).
    D(v^4)=2D(v)+2D(X).                                    (7)

The same cubic equation gives the literal field identities

    -v^4=(-v-1)/(-v),
    A_0=v(1+v)/(1+v^2)=v^8/(v^8-1).                        (8)

Hence D(-v^4)=D(-v), D(A_0)=-D(v^8), and duplication once
more gives

    D(v^8)=2D(v^4)+2D(-v^4)=3D(v)+4D(X).                   (9)

The five-term identity in multiplicative form at (v,-v) is

    D(v)+D(-v)
      =D(-v^2)+D(v(1+v)/(1+v^2))
                          +D(-v(1-v)/(1+v^2))
      =D(X)-D(v^8)+D(Z),                                  (10)

because 1-v=v^-2. Substitution of (7)-(9) into (10) yields

    -3D(X)+D(-v)+D(Z)=3D(v).                               (11)

The regulator identities used here can be checked directly:
their exterior derivatives vanish using
dD=log|z| dArg(1-z)-log|1-z| dArg z, and their real degenerate
values fix the constants. Thus (11) is not a numerical rational
relation or a conclusion from the degree of the trace field.

## 4. Why 3D(v) is the hyperbolic volume of the marked complement

Use the explicitly paired three-tetrahedron p=0 odd family in
[the face and angle audit](twist_family_audit.md) and its
[independent topological and peripheral audit](twist_topology_and_peripherals.md).
That marked family is the 7/3 five-crossing knot complement.
Its positive symmetric angle coordinates are

    U=(A,B,C), V=(A,B,C), W=(B,C,A),
    A+3C=pi, A+B+C=pi.                                   (12)

The face audit proves that averaging into this symmetric locus
preserves all edge equations and does not decrease total volume.
The full volume is strictly concave. Thus an interior stationary
point of the one-dimensional symmetric volume is its full
maximum.

Put theta=Arg v. From 1-v=v^-2 and the stated branch one has

    C=theta, B=2theta, A=pi-3theta,

all positive. These are the three angles of the ideal shape v,
up to cyclic order. The Euclidean sine rule gives

    |v|=sin B/sin A, |1-v|=sin C/sin A.

The modulus relation |v|^2|1-v|=1 therefore says exactly

    sin^3 A=sin^2 B sin C.                                (13)

Equation (13) is the derivative-zero equation for

    3[Lambda(pi-3theta)+Lambda(2theta)+Lambda(theta)].

It is the interior maximum by strict concavity. The explicit
multiplier construction in Section 3.5 of the face audit glues
the cusp triangles isometrically, gives trivial edge dilation
and complete torus cusps, and hence supplies a complete
hyperbolic metric. Its three tetrahedra each have volume D(v).
The topological marking fixes the complement, and the positive
orientation fixes its volume sign. Therefore

    Vol(S^3 minus 5_2)=3D(v),
    Re S(x,y)=Vol(S^3 minus 5_2)/(2pi).                     (14)

This step uses the already audited classical face geometry;
it assumes no quantum state identity for that triangulation.

## 5. Scope

The selected algebraic point has the exact marked volume action.
This resolves the calibration of that point. The actual finite
source contour and the exclusion of all competing source pieces
still have to be established before (14) implies an asymptotic
statement for the original invariant.

[Exact field identities and marked-regulator diagnostic](../experiments/audit_five_two_selected_bloch_calibration.py).

