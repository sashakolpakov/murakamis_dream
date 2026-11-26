# The original conditional branch on the selected left corner

Private research proof, 8 November 2026. The selected type-four
conditional branch extends across the part of the positive radial
seam where \(\Re Y>1\). Its original action still decreases when the
incoming coordinate moves rightward or upward. Explicit radius and
real-index guards put this branch inside the already proved curvature
strip. These are phase statements, not a finite-source deformation.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Domain and original sheet

Keep
\[
a=x-i\eta,\quad \frac12\le x\le\frac7{10},\quad
0\le\eta\le\frac9{125},\qquad
y=q+\frac i{100},\quad 0\le q\le\frac{11}{50},
\quad X=e^{-2\pi ia},\quad Y=e^{-2\pi iy}.
\tag{1}
\]
Write \(\rho=|X|\), \(R=|Y|=e^{\pi/50}\). The original elementary
bounds in [the selected incoming corner](research_mixed_next_selected_incoming_corner_union.md),
Section 2, and
[the selected right horizontal](research_mixed_next_three_selected_left_incoming_right_horizontal.md)
give
\[
\frac58<\rho\le1,\quad \Re X<-\frac5{26},\quad \Im X\ge0,\quad
\rho^2(3-2\Re X)>1,\qquad 1<R<\frac{16}{15}.
\tag{2}
\]
For the real-part inequality use
\(\cos\Arg X\le\cos(3\pi/5)<-4/13\).

Retain the original primitive and chirp
\[
Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\qquad
g'(z)=\Log(1-e^{-2\pi iz}).
\tag{3}
\]
The critical equation in \(v=e^{2\pi it}\) is
\[
v(v-X)(v-Y)=X(v-1)^3,
\quad
(1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0.
\tag{4}
\]
At \(q=11/50\), \(\Im Y<0,\Re Y<1\), so
[the algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md)
identifies its original simple zero-lift root and multiplier
\[
0<\arg v<\arg X,\qquad
w=\frac{v-X}{1-X},\qquad \Im w>0,\quad |w|<1.
\tag{5}
\]
The following proof continues this particular root. It does not
assert that every upper-half-plane root of the cubic is selected.

**Theorem.** On the full closed domain (1), this root is simple and
obeys
\[
Q_t(t_*;a,y)=0,\qquad
\frac2{25}<\Re t_*<1-x,\qquad
\frac12<|e^{2\pi it_*}|<2,\qquad
\Theta_a=\Log w,\quad \Im w>0,\quad |w|<1,
\tag{6}
\]
where \(t_*=\Log v/(2\pi i)\) and
\(\Theta(a,y)=Q(t_*;a,y)\). In particular
\[
\partial_x\Re\Theta<0,\qquad
\partial_{\Im a}\Re\Theta<0.
\tag{7}
\]
At \(q=0\), \(g(y)\) and its derivative mean their specified
limits from \(q>0\). Since \(Y=R>1\ne1\), this is a regular local
logarithmic determination with \(\Arg(1-Y)=\pi\). No assertion
about a finite factorial symbol on the seam is included.

## 2. The enlarged incoming-ray and multiplier exclusions

First, the incoming-ray exclusion is stronger than its former use
on \(\Re Y<1\). Set \(v=sX\), \(s>0\), and use equation (12) of
the algebraic transport theorem. For \(s>1\), its imaginary-part
numerator is positive by (2), contradicting \(\Im Y\le0\) when
\(\Im X>0\). For \(0<s<1\), its real-part numerator is less than
\(s^3-s^2-2s\). Division by the negative denominator \(s(s-1)\)
therefore gives
\[
\Re Y-1>s+\frac2{1-s}>2.
\tag{8}
\]
This is impossible because \(\Re Y\le R<16/15\). For negative-real
\(X\), its positive ray is outside the upper half-plane. Thus an
upper selected root cannot cross the incoming numerator ray.

Here is the new real-multiplier exclusion. Suppose an upper prewall
root has real \(w\). The identity \(v=w+(1-w)X\) gives \(w<1\).
Neither zero nor one is possible. If \(w<0\), then
\(\Im(v/X)=w\Im(X^{-1})>0\), contrary to
\(0<\arg v<\arg X\). At negative-real \(X\), the upper-root
property already gives \(\Im w>0\). We may therefore assume
\[
0<w<1,\quad A=\Re v,\quad r=|v|^2,\quad d=1-A.
\]
Exactly as in equations (16)--(18) of the algebraic theorem,
\[
A<w,\quad r\le1-2wd,\quad
Y=2-\frac1v+\frac{(v-1)^2}{w},\quad
\frac{\Im Y}{\Im v}=\frac1r-\frac{2d}{w}\le0.
\tag{9}
\]
Consequently
\[
\frac{w}{2d}\le r\le1-2wd,\qquad
w\le\frac{2d}{1+4d^2}\le\frac12 .
\]
Equality \(w=1/2\) would require \(A=1/2=w\), so \(w<1/2\).
The sharper actual real part in (2) gives
\[
A=w+(1-w)\Re X<\frac{31w-5}{26}<\frac{21}{52}.
\tag{10}
\]

If \(A\le0\), equations (9) imply \(r\le1\), and the real part
of the displayed formula for \(Y\) is at least two. Suppose \(A>0\).
For fixed \(A,w\), the function
\[
\Re Y-1=1-\frac A r+\frac{A^2+d^2-r}{w}
\tag{11}
\]
is concave in \(r>0\). Its minimum on the interval in (9) is
therefore at an endpoint. Put \(b=1-2A>5/26\). At the lower
endpoint it equals
\[
\frac{b}{1+b}+\frac{b^2}{w}>\frac5{31}.
\tag{12}
\]
At the upper endpoint it is
\[
f(w)=1+2d-\frac{A}{1-2dw}-\frac{2Ad}{w}.
\]
For \(A\le w\le1/2\), the denominator \(1-2dw\) is at least
\(A>0\), and
\[
f''(w)=-\frac{8Ad^2}{(1-2dw)^3}-\frac{4Ad}{w^3}<0.
\]
Its endpoint values are
\[
f(A)=\frac{db}{A^2+d^2}\ge db,\qquad
f(1/2)=2db,\qquad
db>\frac{31}{52}\frac5{26}=\frac{155}{1352}.
\tag{13}
\]
Here \(A^2+d^2\le1\) for \(0<A<1\).
Both (12) and (13) exceed \(1/15\). Thus every putative real
multiplier requires
\[
\Re Y>1+\frac{155}{1352}>\frac{16}{15},
\tag{14}
\]
contrary to (2).

Finally the unit-multiplier exclusion from equations (20)--(22) of
the algebraic theorem remains valid without \(\Re Y<1\).
Indeed write \(X=A_0+iB_0\), \(w=c_0+is_0\),
\(|w|=1,s_0>0\), and \(d_0=2(1-c_0)>0\). Then
\[
P=|v|^2=1+(|X|^2-A_0)d_0+2B_0s_0>1,
\quad Y=v+d_0X(1-X)(1-v^{-1}).
\]
With \(X(1-X)=C_0+iD_0\),
\[
D_0=B_0(1-2A_0)\ge0,\quad
P+d_0C_0=1+2B_0s_0+2B_0^2d_0>0.
\]
For \(v=r_0+it_0,t_0>0\),
\[
\Im Y=\frac{t_0}{P}(P+d_0C_0)
       +\frac{d_0D_0}{P}(P-r_0)>0,
\tag{15}
\]
again impossible.

## 3. Continuation, simplicity, and the original action

Continue (5) by decreasing \(q\) at each fixed \(X\). Use all
four strict conditions in (5) together, so the exclusions are not
circular. An incoming-ray exit is excluded by (8), a real-\(w\)
exit by (9)--(14), and a unit-\(w\) exit by (15).

A real root would satisfy
\[
Y=v-\frac{X(v-1)^3}{v(v-X)},\qquad
\Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.
\tag{16}
\]
For \(\Im X>0,q>0\), this excludes \(v<1\). For \(v>1\),
\[
|v-X|^2-|1-X|^2=(v-1)(v+1-2\Re X)>0,
\]
so it is outside \(|w|<1\). At \(q=0,\Im X>0\), (16)
excludes every real root since \(v=0,1,X\) are impossible.
For negative-real \(X\) and \(q>0\), (16) is real and cannot
equal the nonreal \(Y\).

It remains to check the corner \(X=-\rho,Y=R\).
Its real cubic is
\[
(1+\rho)v^3-(2\rho+R)v^2+\rho(3-R)v-\rho.
\tag{17}
\]
One quarter of its derivative discriminant equals
\[
R^2+(7\rho+3\rho^2)R-5\rho^2-9\rho
\le-\frac{7541}{14400}<0 .
\tag{18}
\]
For a written endpoint check, this expression increases in \(R\);
at \(R=16/15\) it decreases in \(\rho\ge5/8\), since both
coefficients \(3R-5\) and \(7R-9\) are negative. At \(\rho=5/8\)
its value is
\(256/225+71/12-125/64-45/8=-7541/14400\).
Thus (17) is strictly increasing and has one real root and a
simple conjugate pair. Its real root is greater than one, because
the value at one is \((1+\rho)(1-R)<0\); it is again outside
\(|w|<1\). No real-axis exit is possible.

There is no escape to infinity: \(|w|<1\) implies
\(|v|\le |X|+|1-X|<3\). The count in the invariant open region
defined by (5), with multiplicities, stays one. A multiple selected
root would contribute at least two to that count. Hence the branch
exists and is simple on the entire closed domain. Uniqueness in
this region makes its local continuations agree.

By the prewall condition, the shifted arguments \(a+t,y+t\) and
the index \(t\) remain in their original real strips. The logarithmic
equation is an integer multiple of \(2\pi i\), so continuity from
\(q=11/50\) fixes it to zero. Likewise
\[
e^{\Theta_a}=\frac{v-X}{1-X}=w,\qquad \Theta_a=\Log w
\tag{19}
\]
retains its original lift, since \(w\) stays in the open upper
unit half-disk. This proves the action signs (7), including
their continuous seam limits.

## 4. The strict radius bounds

The full semicircle calculation in
[the inward-seam root annulus](research_mixed_conditional_corner_root_annulus.md),
Section 2, extends to the present \(1<R<16/15\). We give the
changed endpoint bounds explicitly. Suppose \(v=r+it_0\),
\(|v|=1/2,t_0>0\), and set
\[
L=v^2-2v+3-v^{-1},\quad X=\frac{v(v-Y)}{L-Y},\quad
C(r)=2r^2-\frac{166r}{25}+\frac{11}{4}.
\]
For \(-1/2<r\le2/5\), its original expansion gives
\[
\Delta:=|L-Y|^2-\frac{16}{25}|v-Y|^2
\ge |L|^2-\frac4{25}+\frac9{25}R^2-2C(r)R.
\tag{20}
\]
The omitted \(-\Im Y\) coefficient is positive, and
\(C(r)\ge207/500\). The right side decreases in \(R\le16/15\),
since its derivative is at most
\(18(16/15)/25-414/500=-3/50<0\).
At \(R=16/15\) it is
\[
F(r)=-32r^3+\frac{596}{15}r^2-\frac{6313}{375}r
                         +\frac{88363}{30000}.
\tag{21}
\]
Here \(F''(r)\ge8/3>0\) for \(r\le2/5\), and
\[
F'(2/5)=-51/125<0,\qquad F(2/5)=5209/10000>0.
\]
Thus \(\Delta>0\), which would give \(|X|<5/8\).

For \(2/5\le r<1/2\), the same original real-part expansion is
bounded below by
\[
f(r,R)=rR^2+(6r^2-13r/4-1/4)R
                         -16r^3+6r^2+5r/2-11/16.
\tag{22}
\]
Its second \(r\)-derivative \(12R-96r+12\) is negative throughout
this enlarged range. Its endpoint values remain
\[
f(1/2,R)=\tfrac12(R-\tfrac14)(R-\tfrac12)>0,\qquad
f(2/5,R)=\tfrac25R^2-\tfrac{59}{100}R+\tfrac{497}{2000}>0.
\]
The last quadratic has discriminant \(-99/2000\).
Hence \(\Re X>0\), the other contradiction. This proves the
semicircle exclusion.

At \(X=-\rho,Y=R\), let \(r_0>1\) be the real root of (17).
Equation (16) gives \(R>r_0\). Vieta therefore gives
\[
|v_{\rm upper}|^2=\frac{\rho}{(1+\rho)r_0}
 >\frac{5}{13}\frac{15}{16}=\frac{75}{208}>\frac14.
\tag{23}
\]
Connected continuation and (20)--(22) preserve \(|v|>1/2\).
For the upper bound, if \(|v|\ge2\), the three original logarithms
in \(Q_t\) have radii at most \(1/2,4/7,1/2\), with the last
occurring three times. The original bound
\(\arcsin(4/7)<\pi/5\), recorded in
[the negative-height branch, equation (17)](research_mixed_conditional_negative_height_branch.md),
gives
\(\Im Q_t>\pi-2\pi/3-\pi/5>0\), a contradiction.
Thus \(1/2<|v|<2\).

## 5. The lower real-index guard

Suppose \(u=\Re t_*\le2/25\), and put
\[
\theta=2\pi u,\quad U=e^{2\pi\Im t_*}\in(1/2,2),\quad
T=e^{2\pi\eta}\in[1,8/5),\quad D=|1-Ue^{-i\theta}|^2 .
\]
The exact folded force is
\[
|e^{Q_t}|^2=
\frac{|T-Ue^{-2\pi i(x+u)}|^2
      |1-RUe^{-2\pi i(q+u)}|^2}{D^3}.
\tag{24}
\]
The elementary witnesses in
[the original angle guard, equations (5)--(8)](research_mixed_conditional_corner_root_angle.md)
give
\[
\cos\theta>6/7,\quad
\cos 2\pi(x+u)<1/5,\quad
\theta\le2\pi(q+u)\le3\pi/5 .
\tag{25}
\]

If \(U\le1\), the invariant \(|w|<1\) gives
\[
1-U^2-2U\Re X(\cos\theta-U)-2U\Im X\sin\theta<0.
\tag{26}
\]
If \(U\le\cos\theta\), the middle term is nonnegative, so
\(1-U<2U\sin\theta/(1+U)\le\sin\theta\).
If \(U>\cos\theta\), instead
\(1-U<1-\cos\theta<\sin\theta\).
Consequently
\[
D<\frac{27}{13}\sin^2\theta,\qquad D<\frac{11}{28}.
\tag{27}
\]
The latter follows from convexity in \(U\in[1/2,1]\) and
\(\cos\theta>6/7\). Radial minimization at the outgoing angle
in (25) gives an outgoing squared modulus at least \(\sin^2\theta\).
The incoming squared modulus exceeds one. Thus
\[
|e^{Q_t}|^2>\frac{10192}{3267}>1,
\tag{28}
\]
contrary to the zero lift.

If \(U\ge1\), angular monotonicity and \(R\ge1\) give
\[
|1-RUe^{-2\pi i(q+u)}|\ge |1-Ue^{-i\theta}|.
\]
Also
\[
\frac DU<U+U^{-1}-12/7\le11/14,\qquad
\frac{|T-Ue^{-2\pi i(x+u)}|^2}{U^2}>
1+U^{-2}-\frac2{5U}\ge\frac{21}{20}.
\]
The last function increases in \(U^{-1}\in[1/2,1]\).
Substitution in (24) gives
\[
|e^{Q_t}|^2>\frac{21}{20}\left(\frac{14}{11}\right)^2
=\frac{1029}{605}>1 .
\tag{29}
\]
This proves the real-index assertion in (6).

## 6. Curvature and the actual left-end calibration

The outgoing cotangent inequality of
[prewall curvature, Theorem 1](research_mixed_next_lower_left_corner_prewall_curvature.md)
applies after replacing its private height by \(-\sigma\) and
its inward height by \(1/100\). The cotangent real part is even
in its height. Therefore, on
\(2/25\le t_R<1-x,\ |\sigma|\le\log2/(2\pi)\),
\[
K(t_R+q,\sigma+1/100)
 <(3-1/540000)K(t_R,\sigma),
\quad
-\Re Q_{tt}>\frac{\pi}{540000}K(t_R,\sigma)>0.
\tag{30}
\]
The incoming cotangent is negative because its real coordinate is
between one half and one. This substitution concerns the proved
cotangent inequality only; it does not import its inward finite source.

The same maximum-of-convex-profiles argument as Section 5 of that
note now gives, at \(a_L=1/2+ih_a\),
\[
\Re\Theta(a_L,y)\le
\max_{2/25\le v\le1/2}\widehat R(v,h_s;a_L,y).
\tag{31}
\]
Here \(\widehat R\) is the original continuous numerator-period
upper rate, and \(|h_s|<\log2/(2\pi)\).
Its incoming wall has the same upward height-derivative jump;
no eliminated-action convexity is asserted.

In particular equation (20) of the selected right-horizontal theorem
pays (31), with the original cap plane \(B_*=B_U(1/2)\),
against every fixed next main, real-cut, last, or upper physical
profile, and each of the two selected weight alternatives:
\[
B_*+\Re\Theta(a_L,y)+\varphi+W_\nu(y)
 <\Lambda_{123}(z)-1/100 .
\tag{32}
\]
The same critical-action inequality holds on the rightward-bottom
and upward-right replacement path by (7) and the already proved
cap bounds there. Equations (31)--(32) are profile comparisons.
They do not bound the literal conditional kernel without its
physical rows, aliases, and unweighted connecting sides.

All strict critical separations are uniform by compactness.
The unresolved finite-corner task is to prove the complete
canonical middle reduction and deformation at this positive shared
height, retaining its postwall upper rate and both connectors.
Nothing here removes those obligations, the original filter,
or any remaining signed Fourier integral.
