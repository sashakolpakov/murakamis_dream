# A finite algebraic dominant-root certificate for the actual backward cubic

29 October 2026. This is an exact spectral input for the next original
Newton source packet in
[the endpoint theorem](actual_twist_endpoint_gaussian_certificate.md).
It proves a strict dominant-mode gap on every closed subinterval of
0<=u<pi/2 for its actual backward principal cubic. It does not infer
the original source projection from two scalar endpoint sizes, nor
claim a whole-word asymptotic without the exact backward source/current.

## 1. The cubic and the assertion

Put Z=exp(-2iu) and

    f_Z(lambda)=lambda^3+(5Z-3)lambda^2
          +(3-7Z+3Z^2)(1-Z)lambda-(1-Z)^5.              (1)

There is a continuous root mu(u), beginning at mu(0)=-2, which is
the UNIQUE root of largest modulus for 0<=u<pi/2. It is nonzero and
simple there. Consequently for every fixed u_0<pi/2 there are constants

    min_(0<=u<=u0)|mu(u)|>0,
    max_(0<=u<=u0,max other roots lambda)|lambda/mu(u)|<1. (2)

The small roots may collide at u=0, but the isolated dominant line
remains regular there. At u=pi/2 the largest moduli do tie; no strict
gap at that endpoint is asserted.

The discriminant is exactly

    disc f_Z=-Z^6(Z-1)^2(27Z^2-54Z+23).                 (3)

The two zeros of its last factor are positive real numbers different
from1. Thus all three roots are distinct on 0<u<=pi/2. Distinctness
alone would not prove(2): the FORWARD cubic of this same source has an
interior dominant-modulus switch. We instead exclude dominant ties
by the finite real-algebraic calculation below.

## 2. An exact test for a pair of equal moduli

For p(lambda)=lambda^3+a lambda^2+b lambda+c, c!=0, form the cubic

    T(t)=[a^3 c(t+2)-a^2 b^2-a b c(t^2+5t+4)
                          +b^3(t+2)+c^2(t+1)^3]/c^2.   (4)

Its three roots, counted with multiplicity, are

    lambda_i/lambda_j+lambda_j/lambda_i, i<j.

Indeed a direct resultant identity is

    Res_lambda(p(lambda),w^3 p(lambda/w))
                      =c^3(w-1)^3 w^3 T(w+w^-1).        (5)

Two nonzero distinct roots have equal modulus only if their root of
T is REAL in[-2,2]. Conversely a real t in[-2,2] gives a unit-modulus
ratio, by solving w+w^-1=t. This is an exact test, including an opposite
root pair t=-2.

Specialize(4) to a=5Z-3, b=(3-7Z+3Z^2)(1-Z), c=-(1-Z)^5.
On the open lower unit semicircle put v=Z+Z^-1=2cos(2u), so -2<v<2.
Write R=R_2/2 and

    R_2=2(v-2)^4 t^3
       +(-3v^4+39v^3-166v^2+292v-184)t^2
       +(15v^4-72v^3+141v^2-181v+134)t
       -7v^4+62v^3-87v^2-132v+220,

    I=(9v^3-57v^2+120v-84)t^2
       +(-9v^3+120v^2-373v+339)t
       +9v^3-66v^2+235v-288.

Exact expansion gives

    (T_Z+T_(Z^-1))/2=R/(v-2)^4,
    (T_Z-T_(Z^-1))/(Z-Z^-1)=I/(v-2)^4.                 (6)

For real t, an equal-modulus pair must therefore satisfy R=I=0.
Their resultant and linear subresultant are

    Res_t(R,I)=(v-2)^4 P(v),
    S_1=(v-2)^4[A(v)t+C(v)],                            (7)

where

    P=19683v^13-275562v^12+1388745v^11-1804275v^10
      -10052343v^9+44382411v^8-41161510v^7-136024030v^6
      +409871548v^5-286814789v^4-449999851v^3
      +1045577541v^2-804786993v+230409954,

    A=486v^6-3807v^5+8973v^4+4038v^3
                                      -51728v^2+82608v-43461,
    C=-243v^6+3240v^5-12492v^4+6666v^3
                                      +61295v^2-138366v+89982.

The audit verifies the displayed polynomial identities by exact symbolic arithmetic. No fitted spectral curve or floating-point root count is used.

## 3. Only one interior parameter can have an equal-modulus pair

Exact Sturm counts show P has precisely TWO roots in(-2,2), one in
each of the rational intervals

    J_-=[-1761026772/10^9,-1761026771/10^9],
    J_+=[ 1314531712/10^9, 1314531713/10^9].             (8)

Horner evaluation with rational interval arithmetic proves A!=0 on
both intervals. On J_-, 1<-C/A<2; on J_+, 4<-C/A<5.
The latter root cannot give an equal-modulus pair because t must
belong to[-2,2]. All possible interior ties are therefore at the single
root v_* in J_-. Approximate values, used ONLY as labels, are

    v_*=-1.761026771989515...,
    t_*=1.479926424410411...,
    u_eq/pi=.421400986116556... .

## 4. That possible tie involves only the two smaller roots

For v in J_-, the corresponding lower-unit-circle Z lies in the exact
rectangle

    Re Z in J_-/2,
    -474021285/10^9 < Im Z < -474021281/10^9.             (9)

The imaginary bounds follow by squaring their positive absolute values
against 1-v^2/4. Use the following rational centers and radius r=1/1000:

    z_1=(1168965+2383072 i)/10^6,
    z_2=(2467958+ 977085 i)/10^6,
    z_3=(3765644- 990050 i)/10^6.                        (10)

For every Z in(9), exact rectangular arithmetic gives, for each center,

    |f_Z(z_j)|<1/50000, |f'_Z(z_j)|>1,
    |3z_j+(5Z-3)|<20.

On |lambda-z_j|=r the Taylor remainder is consequently bounded by

    1/50000+20r^2+r^3 < r < |f'_Z(z_j)|r.

Rouche's theorem isolates exactly one root in each disk. The disks are
pairwise disjoint, so they exhaust all three roots. Their centers
satisfy the exact rational inequalities

    |z_1|,|z_2|<3-r,  |z_3|>3+r.

Thus the first two roots have modulus<3 and the third modulus>3.
In particular a tie at v_* cannot be a tie for the largest modulus.

At u=0 the isolated root -2 is strictly larger than the two zero roots.
By(3) it continues without an eigenvalue collision. Dominance could
be lost only at an equal-modulus pair, and sections2--4 have excluded
every possible dominant tie in the open half-circle. This proves(1)--(2).

## 5. What the actual source still has to supply

This certificate is a usable piece of a source-selection proof rather
than a replacement for it. For the literal backward recurrence, retain
its three-component initial vector and all inhomogeneous currents.
On a prefix where its exact evolution is the homogeneous companion
of(1) plus a uniform smooth O(1/N) matrix error, suppose its actual
initial vector is a nonzero polynomial-scale multiple of the dominant
vector plus a relative error epsilon_N=o(1). This allows the actual
O(N^(-1/2)) initial error, not only O(1/N). Then(2) proves dominant
transport on every strict half-prefix by the following direct iteration.

Choose a smooth dominant/complement frame, divide each step by mu,
and obtain a scalar block1+O(1/N) coupled by O(1/N) to a uniformly
stable two-dimensional block B(u). For any fixed strict prefix its
powers are uniformly exponentially bounded: the two-by-two
Cayley--Hamilton formula bounds them by C(m+1)r^m for some r<1,
including coincident fast eigenvalues. Hence

    H(u)=sum_(m>=0) (B(u)^m)^* B(u)^m

converges with bounded first derivative, I<=H<=C I, and
H-B^*HB=I. Thus the B norm contracts by at most sqrt(1-1/C)<1.
The moving-frame/moving-H error per step is O(1/N).

Write a_i,b_i for the scalar and complementary components after
dividing out the accumulated mu factors. For a fixed sigma<1, a
direct induction in these block equations gives

    ||b_i||/|a_i| <= C[sigma^i epsilon_N+1/N],
    a_i/a_(i-1)=1+O(1/N).

The induction starts because a_0 is nonzero and epsilon_N tends to0;
the stable block absorbs its O(1/N) errors for all sufficiently large N.
Every scalar ratio is then nonzero, and its product is bounded above
and below by fixed positive constants. The total scalar coupling from
the initial transient is at most C epsilon_N/N, since sum sigma^i
is bounded. Summed logarithms have O(1) error relative to the dominant
primitive. The double FAST root at0 causes no problem: only the
dominant projection must be smooth, and its complementary block is
uniformly stable there.

The hypotheses in that last paragraph concern the ACTUAL vector source.
Two scalar endpoint magnitudes do not establish them. The exact
Q^2 delta_(i,1) forcing and the second reset D_2=0 of the forward Ward
equation cannot be deleted when deriving this backward vector. In
particular an interior inhomogeneous current must either be retained
as an additional state with its own estimate, or bounded directly;
the spectral result(2) does not make it harmless. Regularity of the
cubic or nonzero Gaussian endpoint
values alone is not being called a whole-source theorem.

Audit: [exact ratio identities, Sturm intervals and three rational root disks](../experiments/audit_actual_backward_cubic_dominant_source_certificate.py).
It uses exact rational arithmetic throughout, with no sampled
eigenvalue plot or numerical integral in its proof.
