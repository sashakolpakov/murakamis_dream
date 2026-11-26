# The complete first polynomial on the unselected 444 right shoulder

Private written proof, 11 November 2026. The second coordinate retains
its actual negative height and moves from \(9/20\) to \(1/2\).
The first period is complete.
The third coordinate remains on its original unselected plateau.
Neither a second height connection nor a second real arc is included.

## 1. Literal source and action

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\). All references and primitive constants are the original
coupled ones. Put
\[
 P=[11/50,9/20],\quad H=1/100,\quad
 y=q+ic_2,\quad 9/20\le q\le1/2,\qquad z=b+ic_3,\ b\in P.
 \tag{1}
\]
The actual source bounds are
\[
 -.078<c_1<-.020,\quad
 -.102<c_2,c_3,h_2,h_3<-.001,\quad
 -.051<h_e<-.019,\quad a_2=\Re r_2\le.36.
 \tag{2}
\]
At \(m=4\) the third private index is ordinary and its following leg
is attached. No cap is substituted for it.

With \(\zeta=e^{-2\pi i/N}\), \(P_j=(\zeta;\zeta)_j\),
\(p_j(V)=(\zeta V;\zeta)_j\), retain
\[
\begin{split}
 U_N(w,X)&=\sum_{i<N}H_N(w,\zeta^{-i})p_i(X)/P_i^2,\\
 C_N(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 L_N(w;X,Y)&=U_N(w,X)d_N(X)C_N(X,Y),\\
 f_N(w,Y)&=N\operatorname{CT}_X[L_N(w;X,Y)(1+X^{-N})].
\end{split} \tag{3}
\]
Its exact root-filter identity is
\[
 f_N(w,Y)=\sum_{k=0}^{N-1}U_N(w,\zeta^k)C_N(\zeta^k,Y)/P_k.
 \tag{4}
\]
This is the single unnormalized physical sum. The \(X\)-band of
\(L_N\) is \([-N+1,2N-2]\), so only its coefficients at zero
and \(N\) enter (3). No additional \(1/N\) or factor two is present.

Use the original phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-i\pi(e-e^2)/2,\\
 Q(s;a,b)&=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,\\
 F_{123}&=\Psi(e,z_1)+Q(s_2;z_1,z_2)+Q(s_3;z_2,z_3)
                           -g(z_1)-g(z_2)-g(z_3)/2,\\
 \Lambda_{123}(z)&=\Re F_{123,*}
                 +\Re\{\partial_{z_3}F_{123,*}(z-r_3)\}.
\end{split} \tag{5}
\]
Every star belongs to the same actual word. In particular both
shared marginal cancellations are the original stationary equations.
At every first point \(a=x+ih\), the full first-weight ceiling is
\[
 W_\sigma(a)=\max\{-\Re g(a),\,2\pi h_+\}-2\pi\sigma h .
\]
The old-face comparisons below retain both entries of this maximum.
At the second target in (1), the full unselected weight has ceiling
\(-\Re g(y)\), since \(c_2<0\) and \(q\le1/2\). No polynomial
weight is replaced by one of its summands or divided out.

**Theorem 1.** On a sufficiently small fixed ordinary-color
disk about \(-2\), at both parities,
\[
 |f_N(w,Y)d_N(Y)C_N(Y,Z)|\,|d_N(Z)|^{1/2}
 \le C N^A e^{N\{\Lambda_{123}(z)-10^{-12}\}},
 \quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
 \tag{6}
\]
Fixed color derivatives obey the same bound on smaller disks with
polynomial costs. The second coordinate is unselected; there is no
\(Y^{-N}\) in (6).

## 2. The old-face profile anchors

Let \(q_0=9/20\), \(y_0=q_0+ic_2\), and
\(\kappa=1/2500000\). Both complete first coefficient paths are
\[
 0\longrightarrow .1\longrightarrow .1+ih_\sigma
 \longrightarrow .45+ih_\sigma
 \longrightarrow .5+ih_\sigma\longrightarrow .5
 \longrightarrow7/8\longrightarrow1,
 \qquad h_0=c_1,\quad h_1=H.                                    \tag{7}
\]
First consider the pieces up to the real half point. On each piece
retain its original complete cap envelope: the five private profiles
at heights \(h_e,0,0,-.055,.04\), with cuts \(.27,.49\) and penalties
\(0,0,0,.11\pi,.08\pi\), and its separate true-end ceiling.
No cap profile depends on \(q\).

At \(q=q_0\), these profiles paired with the first ordinary main
at height \(h_2\), its real left cut \(1/8\), its real half rate,
or its last carrier, have their original allocated two-factor
bound \(\Lambda_{12}(q_0)\). The following table records the
profile implications, rather than merely a finite-sum bound.

| First portion | Original profile calibration |
|---|---|
| Unselected \(P+ic_1\) | Complete first-cap plane and ordinary main/left/half/last supporting planes, with original half allocations |
| Negative \([.1,.22]+ic_1\) | Joint central source, Sections 2--3, for every main point; joint low/half source (23) for both real cuts; first-four/four last calibration (36) for the separate last profile |
| Negative join at \(.1\) | Negative-height face, Sections 4--5: each common raw profile is paid at both endpoints before convex interpolation |
| Selected \([.1,.45]+iH\) | Complete selected early source, equations (11)--(13) and Sections 3--6, and the selected plateau full-product comparisons |
| Positive join at \(.1\) | Zero-height face and positive convex envelope: the same cap/main/cut/half profiles at the two heights |
| Real \(0<x\le.1\) | Real-first-interval equations (8)--(9), (21)--(23), for the full raw profile envelope |
| Either \(.45\)-to-\(.5\) horizontal | Unselected and selected right-half proofs, before finite summation |
| Both half-face joins | The fixed-profile convex construction described below |

All entries are uniform for the original outgoing \(q_0\in P\);
none changes an actual reference height. The selected true ends keep
their original larger reserve. The negative true-end ceiling is used
on the negative left pieces. On the half-face joins one may use the
larger common constant
\[
 E_*=\frac35+2\pi H+\frac{\log4}{100}<69/100.                       \tag{8}
\]
This is a comparison with a formal ceiling, never division by a
finite cap value.

For precision, the raw half-face construction in Section 3 of
[the early-second selected right connection](research_mixed_complete44_first_selected_early_second_right_connection.md)
is repeated with \(y_0=.45+ic_2\), rather than its displayed
\(.22+ic_2\). Its two endpoint inputs are genuinely uniform on
the whole \(P\): equations (10)--(12), (24) of the unselected
right-half proof bound every fixed main point by its allocated
plane; Sections 2--5 of the selected right-half proof bound every
same main/cut profile. The constant (8) fits the negative cap plane
because its bare plane is \(>149/200\). The exact second derivatives
on the half face are
\[
 \partial_h^2\Re\Psi(e,.5+ih)=-\pi\Re\cot\pi(e+.5+ih)>0,\qquad
 \partial_h^2\Re Q(s;.5+ih,y_0)
                       =-\pi\Re\cot\pi(s+.5+ih)>0.               \tag{9}
\]
Their signs and every first-weight rate at the half face are
independent of \(y_0\). Real low rows and a fixed collar below one
half have the same convexity. At nonpositive first height the high
block reduces to its half and last rates; the last rate is \(-2\pi h\),
so adding it to each convex cap profile still gives a convex
function. Its negative endpoint is paid by the old last comparison,
and its zero endpoint is below the paid half rate. At nonnegative
height the zero-drift theorem reduces the high block to the half
rate alone. Thus the old raw comparisons
hold on both half-face joins, including the real half point. This
does not replace a fixed-height main bound by a critical-action bound.

The right cut \(r_0<1/2\) may be chosen arbitrarily sufficiently
close to one half, before \(N\), and its distance from one half may
then be decreased finitely many times. The raw half-rate comparison pays its entire fixed physical
collar by continuity. The real-half main interval can extend down
to \(3/40\): its portion below \(1/8\) increases to that endpoint
by the exact force comparison in the negative-shoulder source.

Attach any next ordinary main, left, half or last profile at
\((y_0,z)\), with its original incoming and outgoing halfweights.
The complete ordinary-source theorem compares each individually to
its supporting plane. Its incoming tangent cancels that of
\(\Lambda_{12}\), and its incoming quadratic supplies
\[
 \gamma_*:=\kappa(q_0-a_2)^2
       \ge\kappa(9/100)^2>\kappa/1000>10^{-10}.                   \tag{10}
\]
Thus every old-face product just listed is below
\(\Lambda_{123}(z)-\gamma_*\), even if its additional first-path
gap is dropped. The outgoing allocation is exactly
\(-\Re g(z)/2\). The two halves at \(y_0\) give
\(-\Re g(y_0)\), the full second weight.

## 3. Main-index barriers and a decreasing joint profile

Put \(R=e^{2\pi c_2}\). The actual heights give
\[
 13/25<R<1,\qquad 1/2<\rho_j=e^{2\pi h_j}<1,\qquad
 T_3=e^{-2\pi h_3}<2.                                           \tag{11}
\]
For the sharper first inequality, the positive logarithm series gives
\[
 \log(25/13)>12/19+144/6859>619/950>561/875>51\pi/250.
\]
Here \(7200>6859\) and the middle cross-product difference is \(8675\).

Every first main maximum on (7), before the real half point, can
be restricted to \(s_R\ge1/6\), even on its real segment approaching
zero. Its exact private force has squared modulus
\[
 \frac{|T_a-\rho_2e^{-2\pi i(x+s_R)}|^2
              |1-R\rho_2e^{-2\pi i(q+s_R)}|^2}
             {|1-\rho_2e^{-2\pi is_R}|^6},
 \qquad T_a=e^{-2\pi\Im a}.                                    \tag{12}
\]
For \(s_R\le1/6\), the own squared denominator is at most one.
For \(s_R\ge\ell(q):=23/40-q\), the outgoing shifted angle is
at least \(23/40>1/2\), so its numerator is greater than one.
If the first height is nonpositive, \(T_a\ge1\), and its folded
numerator is at least the own denominator: \(x+s_R\le1-s_R\)
for \(x\le1/2\), while increasing \(T_a\ge1\) increases the modulus.
This also covers \(x=0\), by equality in the first comparison.

For the positive first height \(0\le h\le H\), used only at
\(x\ge.1\), \(T_a>15/16\). If the first shifted cosine is
nonnegative, then
\[
 \cos(2\pi s_R)-\cos(2\pi(s_R+x))
 =2\sin(\pi x)\sin(\pi(2s_R+x))>3/10 .
 \tag{13}
\]
Here \(3/40\le s_R\le1/6\), \(.1\le x\le.5\), and in the
cosine-nonnegative case the second sine is greater than \(1/2\);
the first is greater than \(3/10\).
If the shifted cosine is negative, the corresponding difference
with \(T_a\) is at least \(\cos(2\pi s_R)\ge1/2\).
Consequently the first squared numerator minus the own squared
denominator exceeds \(-31/256+3/10>0\).
Thus (12) is greater than one on the entire interval being removed.

The third main similarly increases through \(1/8\le t_R\le1/5\).
Its incoming folded numerator square is at least
\(1+\rho_3^2+3\rho_3/5\). Write
\(D_s=1+\rho_3^2-3\rho_3/5\). Its outgoing numerator square is
greater than \(1+\rho_3^2/4+\rho_3/2>D_s\).
For \(\rho_3\le3/4\), \(D_s^2<(89/80)^2<5/4\), whereas
the incoming square is at least \(31/20\).
For \(\rho_3\ge3/4\), use \(D_s\le1+2\rho_3/5\);
the incoming square exceeds \(D_s^2\) by at least
\((21/25)\rho_3^2-\rho_3/5>0\).
The exact squared force is therefore greater than one.
All these inequalities retain the incoming chirps.

For the paired main profiles, including the full unselected second
weight, the shared real derivative is
\[
 \partial_q\Re\{Q(s;a,y)+Q(t;y,z)-g(y)\}
       =\log\frac{N_sN_t}{D^3},
 \quad
 N_s=|1-R\rho_2e^{-2\pi i(q+s_R)}|,\quad
 N_t=|T_3-Re^{-2\pi i(q+t_R)}|,\quad
 D=|1-Re^{-2\pi iq}|.
 \tag{14}
\]
On the clipped intervals \(s_R\ge1/6,t_R\ge1/5\),
\[
 N_s^2\le A=R^2+\tfrac32R+1,\quad
 N_t^2\le B=R^2+\tfrac{12}{5}R+4,\quad
 D^2\ge D_0=R^2+\tfrac{19}{10}R+1 .
 \tag{15}
\]
The angular bounds are \(\cos2\pi(q+s_R)\ge-3/4\),
\(\cos2\pi(q+t_R)\ge-3/5\), and
\(\cos2\pi q\le-19/20\). The squared moduli are convex in
\(\rho_2\in[0,1]\) and \(T_3\in[1,2]\).
Their exact difference is
\[
\begin{split}
 D_0^3-AB={}&R^6+\tfrac{57}{10}R^5+\tfrac{1283}{100}R^4
       +\tfrac{14359}{1000}R^3+\tfrac{523}{100}R^2
       -\tfrac{27}{10}R-3=:P(R).
\end{split} \tag{16}
\]
One has \(P(1/2)=-63/250\), \(P'(1/2)=21683/1000>21\),
and \(P'\) increases on \([1/2,1]\). Hence
\(P(13/25)>-63/250+21/50=21/125>0\).
The paired main rate decreases. Integrate before taking the maximum;
no differentiability of a maximizing branch is required.

## 4. Moving the first low cut and paying every endpoint rate

The first left cut is now \(\ell(q)=23/40-q\in[3/40,1/8]\).
For a real first private index the derivative along this moving cut,
paired with a fixed next main or real cut, is exactly
\[
 \frac d{dq}\{E_2(\ell(q);a,y)+Q(t;y,z)-g(y)\}
 =\log\frac{(2\sin\pi\ell)^3N_t}{N_{\rm in}D^3},
 \quad
 N_{\rm in}=|e^{-2\pi\Im a}-e^{-2\pi i(x+\ell)}|.
 \tag{17}
\]
The outgoing first numerator cancels before taking any bound.
For nonpositive first height, \(N_{\rm in}\ge2\sin\pi\ell\).
For positive height, on its path \(x\ge.1\),
\(N_{\rm in}>1/2\). Also
\[
 (2\sin\pi\ell)^2<3/5,\quad
 2\sin\pi\ell<4/5,\quad N_t\le3,\quad D^3>27/8.
 \tag{18}
\]
For the last inequality,
\(D^2\ge D_0>D_0(13/25)=2823/1250
 =9/4+21/2500\).
Thus (17) is negative in either case; for the positive case its
ratio is less than \(3072/3375\). Paired with the third last rate,
omit \(N_t\) and one denominator power, which is still decreasing.
Every low physical row increases to this moving cut by the same
literal ratio: for positive first height its folded first numerator
is \(>1/2\). Throughout \(0\le t\le\ell(q)\), one has
\(q+t\in[.45,.625]\), so its outgoing numerator square is
greater than \(1+1/4+7/10=39/20>16/9\).
The numerator product is therefore \(>2/3\), whereas the own
denominator cube is \(<(4/5)^3<2/3\).
For nonpositive height cancel the first numerator against one own
factor, leaving \(1/(2\sin\pi\ell)^2>1\).

The third real left cut stays at \(1/8\). For it and the third
half profile, \(N_t\le1+R\); for a first clipped main or real
cut \(N_s\le1+R\). Since \(D>3/2\) and
\[
 (3/2)D_0-(1+R)^2=\tfrac12R^2+\tfrac{17}{20}R+\tfrac12>0,
\]
these paired rates decrease. For a third last carrier the derivative
is \(\log(N_s/D^2)<0\).

For the first half rate, \(N_s=|1+Re^{-2\pi iq}|<3/5\), while
every third main has \(N_t<3\). Hence its paired rate also strictly
decreases. Uniform continuity extends this assertion to a fixed
physical collar \(r_0\le s_R\le1/2\), after decreasing its width.
The first high-row theorem for nonpositive outgoing height now applies
on the full angular square: for \(-.078\le\Im a\le0\), its two
rates are the first half and last. For nonnegative first height its
drift is zero, so only the half rate is needed.
The continuous integrated formulas extend both comparisons to
\(x=1/2\) or \(q=1/2\). Their zero-safe product proof is uniform
there as well; no strict logarithmic summand inequality is required
at a real numerator zero.

It remains to pay the first last carrier at negative first height.
At the old face \(q_0\), uniformly on \(.1\le x\le.5\),
\[
 E_2(1/8;a,y_0)-E_2(1;a,y_0)>\frac{107}{12000}.
 \tag{19}
\]
Indeed its incoming numerator integral is greater than
\(-11/160\): minimize the radius to use
\(\sin(\pi/5)>7/12\), and
\(\log(12/7)<11/20\). The latter follows from
\[
 e^{11/20}>1+11/20+121/800+1331/48000
                =82991/48000>12/7 .
\]
The outgoing numerator integral is \(>1/24\):
its cosine is below \(-7/8\), its radius is \(>1/2\), so its
modulus exceeds \(7/5\), and \(\log(7/5)>1/3\).
The sine bound \(2\sin\pi v\le2\pi v\) gives
\(-J(1/8)\ge\{1-\log(\pi/4)\}/8>31/200\):
indeed \(\pi<22/7\) and the positive atanh series imply
\(\log(4/\pi)>\log(14/11)>6/25\).
Thus \(-3J(1/8)>93/200\).
The remaining chirp and last difference is greater than
\(-429/1000\), since \((7/8)2\pi(.078)<429/1000\).
Their sum is exactly \(107/12000\).

The first last carrier is constant in \(q\). Its pair with a third
main and the second weight has derivative \(\log(N_t/D^2)\).
In fact \(N_t/D^2<9/8\): the polynomial
\[
 81D_0^2-64B
 =81R^4+\tfrac{1539}{5}R^3+\tfrac{39041}{100}R^2
                  +\tfrac{771}{5}R-175
\]
increases for \(R\ge1/2\) and is \(1081/25>0\) there.
Its total possible cost over length \(1/20\) is less than \(1/160\).
Equation (19) leaves
\[
                 107/12000-1/160=1/375>0.                       \tag{20}
\]
Thus use the already calibrated old first-left-cut profile for
this branch. No lower bound for a finite row has been used.
Third real cuts or last carriers have still smaller costs.

The third high block reduces to its own half and last rates by the
original transformed-upper-row Lemma 1 on
\([.22,.5]^2,\ |\Im y|,|\Im z|\le.108\).
It is not an application of the narrower first-depth theorem at
depth \(.102\). This pays every first/third physical endpoint
combination with the same raw gap (10).

## 5. The enlarged first ordinary contour

The first central block has moving left cut \(\ell(q)\), fixed
right cut \(r_0<1/2\), and original main height \(h_2\).
We give the additional all-height check needed for its joins and
sampling terms. Put
\[
 C(s)=\Re\cot\pi s,\qquad A=\cosh(2\pi\eta),\qquad s=u+i\eta.
\]
Throughout the following estimates \(u\ge\ell(q)\) is retained;
the containing interval \(u\ge3/40\) is not used to drop that
coupled lower-cut condition.
The outgoing shifted cotangent is negative because
\(q+u\ge23/40>1/2\).

For \(.1\le x\le.5\), \(-.078\le h\le.01\),
\(3/40\le u\le1/8\), and \(|\eta|\le.102\),
\[
 3C(s)>\frac{27}{11},\qquad C(s+a)<2 .
 \tag{21}
\]
Use \(\sin2\pi u>9/20,\ \cos2\pi u>7/10\),
\(\cosh(.204\pi)<5/4\), and
\(\cot(7\pi/40)<2\). If the shifted cotangent is nonpositive,
no upper estimate is needed.
For explicit witnesses, \(\sin(3\pi/20)>
15/32-(15/32)^3/6>9/20\), \(\sqrt2/2>7/10\), and
\(\tan(7\pi/40)>21/40>1/2\).
The positive-series estimate
\(\cosh t\le1+t^2/[2(1-t^2/12)]\), with \(t<13/20\),
gives \(\cosh(.204\pi)<1+1014/4631<5/4\).
For \(\eta\ge.102\), the following lower bound keeps the
negative first height:
\[
 \cosh2\pi(\eta+h)
 \ge\frac{61}{100}A+\frac{39}{160A}.                             \tag{22}
\]
Indeed minimize at \(h=-.078\), use
\(e^{-.156\pi}>61/100\), \(\sinh(.156\pi)>39/80\), and
\(A-\sqrt{A^2-1}\ge1/(2A)\).
The exponential witness is
\(\log(100/61)>2(39/161+(39/161)^3/3)>.156\pi\).

On this lower private interval, if \(C(s+a)>0\),
\[
 3C(s)-C(s+y)>
       \frac{27/20}{A-7/10}+\frac{9/20}{A+1},\qquad
 C(s+a)<\frac1{(61/100)A+39/(160A)-23/50}.                       \tag{23}
\]
For the outgoing term use \(q+u\in[.575,.625]\),
\(-\sin2\pi(q+u)>9/20\), and \(0\le\eta+c_2\le\eta\).
After clearing positive denominators, the difference in (23) has
numerator
\[
 \frac{1960A^2-9933A+13253}{20000}
                         +\frac{8073}{32000A}>0.
 \tag{24}
\]
The quadratic discriminant is \(-5239031<0\).

For \(1/8\le u\le1/4\) and \(\eta\ge.102\), \(A>6/5\), and
\[
 3C(s)-C(s+y)>\frac{21/10}{A}+\frac{9/20}{A+1},\qquad
 C(s+a)<\frac1{(61/100)A-1/5}
 \tag{25}
\]
whenever the latter is positive. Here \(u+x\ge.225\).
The bound \(A>6/5\) follows from
\(\cosh(.204\pi)>1+(51/80)^2/2>6/5\).
The cleared difference is
\[
 \frac{1111}{2000}A^2-\frac{229}{1000}A-\frac{21}{50}>0:
\]
it is \(5256/50000>0\) at \(A=6/5\), and increases thereafter.
For \(u\ge1/4\), a positive incoming shifted sine is no larger
than the own sine, and its cosine is below \(-1/2\). Hence
\[
 \frac{C(s+a)}{C(s)}
       \le\frac{A+1}{(61/100)A+1/2}<3 .
 \tag{26}
\]
For \(u\ge1/8,|\eta|\le.102\), use instead
\(C(s)>\tfrac12\cot\pi u\) and
\(C(s+a)\le\cot\pi(u+x)<\cot\pi u\).
At \(u=1/2\) use its limit and the strictly negative shifted term.
Together these prove \(\Re Q_{ss}<0\) for every \(\eta\ge h_2\).

For real \(0\le x<.1\), \(h=0\), the same-height incoming denominator
is at least the own denominator whenever its cotangent is positive.
For \(u\le1/4\) its sine ratio is at most
\(1/\sin2\pi u<20/9<3\); for \(u\ge1/4\) it is at most one.
The outgoing cotangent is negative. Thus the same curvature holds
at every height also on this real first interval.

The original imaginary derivative \(I=\Im Q_s\) decreases with
private height throughout \(\eta\ge h_2\), and its upper-height limit is
\(-\pi-2\pi q+2\pi u\ge-37\pi/20\). Thus \(I>-37\pi/20\)
on this whole interval, including the segment from \(h_2\) to zero
used in the upper-horizontal comparison. Below zero the elementary strip argument bounds
give \(I<\pi\), even if the first shifted radius exceeds one:
if \(u+x<1/2\), bound that argument by
\(\pi(1-2u-2x)\); otherwise it is nonpositive.
The outgoing argument is nonpositive and the own argument
nonnegative. The original \(2\pi x\) chirp is retained.

Choose lower and upper alias heights \(-1/5,4\).
Relative to the original main line they lose at least
\(\pi/5\) and \(4113\pi/10000\), respectively.
Every weighted vertical half decreases from its real cut.
Curvature on \(h_2\le\eta\le0\) pays both unweighted joins by
their main/cut endpoints. Those endpoints were paid in Sections 3--4.

The exact marked factorial interpolant is unchanged:
\[
 e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                     E_N(a)E_N(y)E_N(s)^3.                      \tag{27}
\]
For every fixed first \(x\ge\rho>0\), its real arguments remain
in compact subsets of \((0,1)\), with
\(a_R+r_0<1\) and \(q+r_0<1\).
The original split-cotangent formula has the \(+N\) main density,
two unweighted joins, two horizontal corrections and four weighted
vertical halves. Half-grid sides approximate the moving cut, with
uniform \(o(1)\) rate costs; all displaced rows are retained in
their adjacent physical groups. Sections 3--4 account for every
low, collar and high row through \(N-1\).

The third own-four source uses left cut \(1/8\), main height \(h_3\),
and a fixed right cut near one half. Its all-height curvature follows
directly: the incoming shifted cotangent is nonpositive. If the
outgoing one is positive, then \(t<.28\), and, with
\(A=\cosh2\pi\eta\),
\[
 3C(t+i\eta)>\frac{21/10}{A+1/5},\qquad
 C(t+z)<\frac1{A/2+1/2}.
 \tag{28}
\]
The first rational expression exceeds the second. Its imaginary
derivative therefore lies between the exact limits
\(-\pi-2\pi b+2\pi t\ge-33\pi/20\) and \(2\pi q\le\pi\).
The same lower/upper aliases \(-1/5,4\), all weighted sides and
both convex joins are paid by its main/real-cut endpoints.
Its low rows increase to \(1/8\); its high rows were treated above.
Thus both ordinary kernels are complete, not merely their main lines.

At first \(x=0\) apply the Laurent endpoint lemma to the whole product
after fixing a small interval radius and then a still smaller
\(\rho>0\). Its first band is
\([-(1+\sigma)N+1,(2-\sigma)N-2]\).
The old real-first linear improvement \((.1-x)/3\) permits any
sufficiently small continuation cost; the new transports did not
spend that improvement. No source constant is assumed uniform as
\(\rho\to0\). This finishes both first paths up to their real half point.

## 6. The real first interval from one half to seven eighths

The complete [negative-shoulder conditional source](research_mixed_four_unit_incoming_negative_shoulder_source.md)
applies on the entire new domain, including \(q=.5\), with the
original simple upper root and zero lift. It gives
\[
 |C_N(e^{-2\pi ia},Y)|
 \le\operatorname{poly}(N)e^{N\{\max(\Re\Theta(a,y),L(y),H(y))+\tau\}},
 \quad .5\le a\le7/8,                                         \tag{29}
\]
where
\[
 L(y)=E_{1/2}(\ell(q);y),\qquad H(y)=E_{1/2}(1/2;y).
 \tag{30}
\]
It retains every physical row, including the entire postwall middle,
both joins and all sampling corrections. Its action comparison is
\[
 \Re\Theta(a,y)\le\Re\Theta(.5,y)
 \le M(y):=\max_{1/8\le u\le r_0}\Re Q(u+ih_2;.5,y).             \tag{31}
\]
The cut can contain the whole compact critical family. The extra
interval below \(1/8\) is raised to that endpoint by its exact force.
The scalar \(M_1(0)<7/15\) in that source's postwall bound has
the separate written proof in
[the elementary one-numerator lemma](research_elementary_one_numerator_rate_bound.md);
its stronger ceiling is \(7/15-1/1000\).

Let \(\mathcal A(0)\) be the original real-half cap envelope,
including (8). Complete cap transport bounds the full cap and either
first Fourier weight by
\(\max\{\mathcal A(0),9/10\}\).
The original main trial in the selected-real-first proof gives
\(A_0(0)>181/200\), independently of \(q\). Thus this ceiling is
just \(\mathcal A(0)\).

The raw real-half comparisons in Section 2 pay each cap entry paired
with \(M(y_0),L(y_0)\), or \(H(y_0)\), and every next profile.
Sections 3--4 transport these: \(M\) clips to \(u\ge1/6\);
\(L\) uses the moving-cut derivative (17); \(H\) uses the strict
half-row inequality. Equations (29)--(31) therefore give the same
raw gap \(\gamma_*\) for this entire real first arc.

## 7. The final real first arc and the complete coefficient

For \(7/8\le a<1\), the coherent full-cap ceiling is \(223/240\).
The complete conditional bound \(7/15\) on this incoming arc is
valid for every outgoing \(|Y|\le1\), by the final-real source
proof before its geometric calibration. Hence the first pair,
including either full first weight of rate zero, has ceiling
\[
                         223/240+7/15=67/48.                   \tag{32}
\]
Compare it with the old real-half formal profile
\(A_0(0)+E_{1/2}(1/8;y_0)\).
The incoming half integral is \(>1/14\), because
\(2\cos(\pi/8)>9/5\) and \(\log(9/5)>4/7\).
The outgoing integral is \(>1/24\), as in (19).
Therefore
\[
 A_0(0)+E_{1/2}(1/8;y_0)
 >\frac{181}{200}+\frac{93}{200}+\frac1{14}+\frac1{24}
 >\frac{67}{48}+\frac1{16}.                                    \tag{33}
\]
The last difference after cancelling \(1/24\) is \(13/525>0\).
This is a lower trial for a calibrated action profile, not for a
finite sum.

Only the next profile and second weight need be moved in this
comparison; the positive ceiling (32) is independent of \(q\).
Their possible cost is \(<1/160\) by the same \(9/8\) bound as
in Section 4. Third real cuts and last profiles have smaller cost.
The reserve \(1/16\) in (33) pays it. The Laurent endpoint lemma
then fills the fixed collar at \(a=1\), with its prescribed small
cost, for the whole product and both first bands. No endpoint
factorial approximation is used.

Each path (7) is now paid with raw gap at least \(\gamma_*\).
The original exact integrand is entire in the additive first
coordinate, so
\[
 f_N(w,Y)=N\sum_{\sigma=0}^1\int_{\Gamma_\sigma}
       U_N(w,X)d_N(X)X^{-\sigma N}C_N(X,Y)\,da                  \tag{34}
\]
with the indicated two oriented paths from zero to one.
Multiplying by the complete \(d_N(Y)C_N(Y,Z)\) and its outgoing
halfweight before taking moduli preserves this identity.
The \(N\,da\) density, finite lengths and every internal residue
density contribute only their original polynomial factors.
Choose all source, collar and ordinary-color allowances with sum
less than \(\gamma_*-10^{-12}\). This proves (6).

The old cap profile bounds and the exact complete-coefficient
symbols have their stated fixed ordinary-color neighborhoods.
Intersect these finitely many neighborhoods, reserving the same
arbitrarily small rate allowance for their color dependence.
The new ordinary comparisons are color independent. Cauchy's
formula on a smaller fixed disk supplies every fixed color jet.
At a zero of any color-independent multiplier the upper bound
holds directly; no Fourier factor or outgoing halfweight is
divided out.

The exact subsequent restricted integral has density \(+N\,dy\)
on \([9/20,1/2]+ic_2\), and obeys the same exponential bound
with polynomial cost. All first Fourier alternatives are consumed
once in (34); the full second weight and outgoing halfweight each
occur once. The second coordinate has not changed height or
completed a period. No nonzero whole-transfer, whole-word or knot
conclusion is asserted.

## Direct source versions

The complete author proof and every directly used source implication
were read, and all thirty source bindings were checked. Independent
review is required before adoption.

| Direct source | Implication used | SHA-256 |
|---|---|---|
| research_mixed_complete44_second_early_full_first_period.md | Sections 1–2: exact coefficient filter, action and first-path normalization | 2c2e9953e47bccf58206972f49cbadb011dab21ca966921643d50b55a1e3d0b4 |
| research_mixed_complete44_second_early_central_four.md | Sections 1–2: actual 444 reference roles and shared halfweight calibration | e5be8082613eac6887d3aca857703e4ac5b511c430f35ca91fa388c71a924f45 |
| research_mixed_first_cap_plateau_completion.md | Section 2: each complete cap profile and genuine end below the original plane | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_three_row_source_assembly.md | Sections 1–2: actual ordinary domains and individual main/left/half/last planes | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_first_four_four_true_last_row_calibration.md | Sections 1, 3–7: first-four/four last carrier and its full early calibration | 52c149d8500e88c6e4e3fdf1c9e699baf376dfaac8b96d3461dc81f9d1725e0d |
| research_mixed_early_joint_central_source.md | Sections 2–3: pointwise early main and true-end transport | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_joint_low_tail.md | Section 3, equation (23): each early cap × real-cut/half profile | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_first_four_four_negative_height_face.md | Sections 2–5: common negative-join raw envelope and both endpoint calibrations | f50598305505a5dde4537fc15d6ed114b8e3a01eb87d69cff5ac36e0829b40a3 |
| research_mixed_selected_four_four_early_complete_source.md | Sections 2–6: all selected early main/cut/half/last profiles | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_selected_four_four_full_product.md | Sections 2–3: all selected plateau cap/ordinary profile pairs | 4fadefa2aa2ab731da1c1557aeec77113e2bbd5d491c7fd104011b24766a248d |
| research_mixed_selected_four_four_zero_height_face.md | Proposition 2: raw zero-face Cartesian profile calibration | fe99fcefe1618991471f083febcf4c6043418a4387d76be1ae2015542734810f |
| research_mixed_first_positive_join_convex_envelope.md | Sections 2–4: common positive-join convex envelope | b1f18bb5a79ff958654190c960c933ac7839f1da3fc86635f6222a1ea58cb774 |
| research_mixed_four_four_real_first_interval.md | Sections 2–5: complete real-first envelope and preserved linear endpoint reserve | b848eb005f99d57259662ef3a864b207e093b6ebfaf4c34c2dbcc1e9727d58fc |
| research_mixed_initial44_right_half_interval.md | Equations (10)–(12), (17)–(18), (24): fixed main planes and joint physical transport | 309d6869f7438a9ed0a407c43666198ce1a039db7545c404a5e97f4ba2538c9c |
| research_mixed_selected44_right_half_interval.md | Sections 2–6: selected right-half raw profiles and finite inventory | 50d7d9daaf5e33f45749b7c5ca9e2dba4fd0dca2298986d337cb58e35979ebc1 |
| research_mixed_complete44_first_selected_early_second_right_connection.md | Section 3: common fixed-profile half-face construction and larger end ceiling | 4a0ec064b1f408351088e386e3cba2c4bdf2ee852f2c3027687394fa0626ea58 |
| research_mixed_complete44_two_early_angles_high_rows.md | Theorem 1 and its finite proof: nonpositive-height high rows on the full angular square | b088d7b6e388f65f3a96e9176f810cfd0936cb31f425e47fcd9808c6dcb81c8d |
| research_mixed_all_angle_high_row_sign_class.md | Theorem 2 and Corollary 3: zero-drift high rows and zero-safe finite endpoints | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_transformed_upper_rows.md | Lemma 1: next own-four high rows through real incoming angle one half | bdfc604c945926f257278a15c1383df228cf5238754fada7bbfd278b6aedd603 |
| research_mixed_four_unit_incoming_negative_shoulder_source.md | Theorem 1 and equations (7)–(8), (40)–(41): complete negative-output unit source and fixed-height comparison | 32ab90d92081f4741a48f295efe7b3af202ad29ca863e5e25a75b4109e26962f |
| research_elementary_one_numerator_rate_bound.md | Entire lemma: written scalar M1(0) bound used by the unit-source postwall estimate | f2376d1732f241ef3214a413259615b56de935a7fde7ae17370e95f72dac4289 |
| research_mixed_initial44_complete_real_cap_transport.md | Theorem 1: complete cap transport with its unreplaced real-half envelope | dd8d313e1e23240943421b6fbb340f28de769f46d2c0f98f3a4a749be20d4420 |
| research_mixed_complete44_second_selected_real_first_arc.md | Sections 2–3, equation (29): the original real-half cap-main lower trial | f9a9a53a68faf11293f8463e713afdb951ffd5cddcf18e8f1dee4d09ff5fb37c |
| research_mixed_initial44_far_right_physical_envelope.md | Sections 2–3: coherent complete-cap ceiling on the far real arc | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_complete44_second_far_real_arc.md | Section 3, equation (21): complete conditional 7/15 ceiling for every outgoing disk point | 922a114d355f134aae94065d2c8996ac26d670f6dd5439f20285c7c7b627dd2e |
| research_mixed_four_four_real_first_endpoint.md | Lemma 1: arbitrarily small-cost homogeneous Laurent endpoint continuation | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |
| research_mixed_fourier_weight_continuation.md | Sections 1, 5: exact diagonal polynomial and both absolute Fourier alternatives | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| exact_factorial_interpolation_and_complex_contours.md | Sections 4–5: original finite-height factorial symbols and marked residue identity | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_horizontal_asymmetric_contour.md | Section 4: exact +N mode, both joins and all six sampling currents | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_conditional_contour_allowance.md | Section 2: zero-safe finite bounds for every physical row | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

Only written inequalities and source/identity checks were used.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.
