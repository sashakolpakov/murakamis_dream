# Complete endpoint continuation to private real part 11/50

Research deduction, 8 November 2026. The complete endpoint source
extends through the additional strip with real part in
\([11/50,9/40]\), below the auxiliary-real curve and at depth
at most \(3/50\). The right-cut comparison uses an integrated
directional estimate. A pointwise bound that discards the
correlation between the auxiliary slope and reciprocal depth
is not used.

This is a theorem for the original full endpoint finite sum.
It proves no comparison for an outer-cap path or following
contraction. No numerical evaluation or frozen-source edit is used.

## 1. Source and statement

Keep the original finite function, phases and normalizations of
[the \(9/40\) endpoint extension](research_mixed_endpoint_below_curve_nine_fortieths.md):
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi el}e_l(w)}{S_lG_N(Ne-l)},\qquad
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\qquad
 S(e)=F(e,u_c(e)).
 \tag{1}
\]
Let \(\eta_0(E)\) be the depth of the original auxiliary-real
curve \(p=1-2t^2+2it\), with \(e=\Log p/(2\pi i)\), and set
\[
 \mathcal W_{11/50}=
 \{E-i\eta:11/50\le E\le9/40,\quad
                         \eta_0(E)\le\eta\le3/50\}.
 \tag{2}
\]

**Theorem.** On a fixed complex neighborhood of
\(\mathcal W_{11/50}\times\{-2\}\),
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                  (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.
 \tag{3}
\]
The action and nonzero coefficient have their original branches
and constants. Both level parities, every revived row, and all
fixed normalized mixed ordinary-color/index derivatives are
included. Combining (3) with the preceding below-curve theorems,
the above-curve source and the earlier rectangle supplies the
complete endpoint packet near
\([11/50,49/100]+i[-3/50,0]\), at ordinary color near \(-2\).
It does not assert an outer-phase bound.

## 2. Explicit original-root bounds

Put
\[
 p=Re^{2\pi iE},\qquad s=\cos2\pi E,\qquad c=Rs,\qquad
 \sqrt{1-2p}=A-iB,\qquad
 \tan\pi u_c=A/2-i(B-1)/2 .
 \tag{4}
\]
These are the same original branches continued from the
auxiliary-real curve; in particular \(A>0\), \(B\ge1\).
Here
\[
 \frac3{20}<s<\frac{33}{175},\qquad
 R_0(E)>5/4,\qquad R<35/24,\qquad c<11/40 .
 \tag{5}
\]
For the lower sine bound use
\(\sin(\pi/20)>\sin(5/32)>3/20\), from its cubic lower
polynomial. For the upper one use
\(s\le\sin(3\pi/50)<33/175\).
The curve radius solves
\((1-s^2)R_0^2+2sR_0-2=0\); at \(R=5/4\) the left side
is at most \(-53/2450<0\).
The upper radius is the unchanged logarithmic witness
\(\log(35/24)>3\pi/25\) from the western theorem.

The exact formulas
\[
 A^2=\frac{\sqrt{1-4c+4R^2}+1-2c}{2},\qquad
 B^2=\frac{\sqrt{1-4c+4R^2}-1+2c}{2}
 \tag{6}
\]
give
\[
                 A<53/40,\qquad 1\le B<111/100.
 \tag{7}
\]
For the first, retain \(c>3R/20\). The resulting upper
bound for \(A^2\) increases with \(R>1\): differentiating
gives the positive comparison
\((2R-3/20)/\sqrt{(2R-3/20)^2+1-(3/20)^2}>3/20\).
At \(R=35/24\), its radical is
\(\sqrt{1243}/12<147/50\), and hence
\[
                 A^2<1401/800<(53/40)^2.
\]
For \(B\), its square increases in both \(c\) and \(R\).
At their upper bounds its radical is
\(\sqrt{6053/720}<29/10\), so
\[
                 B^2<49/40<(111/100)^2.
\]

Write \(u_c=\xi+ih_c\) and \(\tan\pi u_c=x-iy\).
Then
\[
 0\le y<11/200,\qquad x^2>29/80+y+y^2.
 \tag{8}
\]
The original arctangent has real part in \((0,\pi/4)\).
Its double-angle formula gives
\(\tan(2\pi\xi)<12/5<\tan(3\pi/8)\), by (7);
the first inequality follows by substituting
\(A=53/40\), \(B-1=11/100\).
Also \(x^2>29/80>1/3\).
On its vertical arctangent segment,
\(\Re(1/(1+z^2))<1/(109/80+y)\).
Consequently
\[
 \boxed{\quad
 \frac16<\xi<\frac3{16},\qquad
 0\le-h_c<
 \frac{y}{\pi(109/80+y)}
 \le\frac{22}{567\pi}<\frac1{80}.
 \quad}
 \tag{9}
\]
The last rational comparison uses \(\pi>25/8\).
Since \(R>5/4\), \(\pi\eta>1/9\), and therefore
\[
 \pi(\eta+h_c)>
       \frac19-\frac{22}{567}
       =\frac{41}{567}>\frac1{14}.
 \tag{10}
\]
This preserves \(0<\Re u_c<E\), \(\Im(e-u_c)<0\), the
original primitive chamber and the zero logarithmic lift.
The negative real Hessian remains positive there, so the
critical point is simple.

## 3. The slope-depth correlation

The right cut is
\[
 b(E)=E-\delta,\qquad \delta=1/1000,\qquad
 \Delta=b(E)-\xi>63/2000,\qquad
 m=\frac{-h_c}{\Delta}<\frac25 .
 \tag{11}
\]
We need a bound for \(m\coth(\pi\eta)\), not the product
of independent bounds for its two factors.

Fix \(E\), so \(s\) in (4) is fixed, and differentiate with
respect to \(R\). With
\(D=(2R-s)^2+1-s^2\), equation (6) gives
\[
 B_R=\frac{(2R-s)/\sqrt D+s}{2B}>\frac49,\qquad y_R>\frac29 .
 \tag{12}
\]
Indeed \(2R-s>23/10\), so its ratio to \(\sqrt D\) exceeds
\(23/26\). The right side of (12) is then bounded below by
\[
 \frac{23/26+3/20}{111/50}>\frac49 .
\]
This derivative computation uses the actual root at fixed \(E\).

For \(y>0\), define
\[
 Y(R)=\frac{y}{109/80+y}\frac{R+1}{R-1}.
\]
On the entire radial interval \(R_0(E)<R\le35/24\),
\[
 \frac{Y'}Y
 =\frac{(109/80)y_R}{y(109/80+y)}
                   -\frac2{R^2-1}
 >\frac{545}{567}\frac{400}{99}-\frac{32}{9}
 =\frac{18416}{56133}>0 .
 \tag{13}
\]
The value at \(y=0\) follows by continuity.
At \(R=35/24\) the bound \(y\le11/200\) still holds,
including if this endpoint is outside the smaller chosen
radial subinterval. Thus \(Y(R)\le118/567\).
Using (9), (11), and
\(\coth(\pi\eta)=(R+1)/(R-1)\), we obtain
\[
 m\coth(\pi\eta)
 <\frac{236000}{35721\pi}<\frac{17}{8}.
 \tag{14}
\]
For the last comparison \(\pi>25/8\) gives
\(1888000/893025<17/8\).
This does not assume any monotonicity of \(\xi\).

## 4. Integrated right-cut comparison

Put \(A_0=2\tan\pi u+3\cot\pi u\).
On the right segment from \(u_c\) to \(b(E)\),
\[
             \Re A_0>26/5,\qquad
             |\Im A_0|<(9/100)\Re A_0 .
 \tag{15}
\]
Here is a complete set of elementary witnesses.
Equation (9) gives
\[
 \sinh(2\pi|h_c|)
 <\frac{74844}{963499}<\frac{171}{2200};
\]
the first fraction is \(t/(1-t^2/6)\) at \(t=44/567\).
Also \(\sin(2\pi\Re u)\ge\sqrt3/2>19/22\).
The tangent and cotangent imaginary-to-real ratios are
therefore less than \(9/100\).
Since \(\Re u\le b(E)\le28/125\),
\(\pi\Re u<88/125\). The usual alternating sine/cosine
polynomials at \(88/125\) give
\[
 \cos(88/125)>381/500,\qquad
 \sin(88/125)<81/125,\qquad
 \cot(\pi\Re u)>127/108>47/40 .
\]
The first inequality can use the cosine polynomial through
degree six, and the second the sine polynomial through degree
five; these are rational strict inequalities.
Furthermore
\(\sinh(\pi|\Im u|)<171/4400\) and
\(\sin(\pi\Re u)\ge1/2\). Thus
\[
 \Re\cot\pi u>
       \frac{47}{40}\frac{140}{141}=\frac76,
\]
using \((171/2200)^2<1/140\).
The product of the real tangent and cotangent exceeds
\(10000/10081\). Minimizing
\(2(10000/10081)/v+3v\) over \(v\ge7/6\) gives
\[
 \Re A_0>
     \frac{120000}{70567}+\frac72>\frac{26}{5}.
\]
The last strict comparison is \(1200000>1199639\).
This proves (15).

We strengthen the correlated cotangent lemma of the
\(9/40\) theorem by retaining its integrated positive remainder.
Along this segment, put
\[
 d=E-\Re u,\qquad
 y_{\rm rec}=\eta-m(d-\delta)>0 .
\]
Then
\(\delta\le d\le E-\xi<7/120<3/50\),
\(0\le m<2/5\), and \(y_{\rm rec}\le\eta\).
With \(C_0=\coth(\pi\eta)\), define exactly
\[
 Q(d)=(1-m^2)\sin2\pi d+
 2mC_0(\cosh2\pi y_{\rm rec}-\cos2\pi d)
                  -2m\sinh2\pi y_{\rm rec}.
\]
As in that lemma, \(Q(\delta)\ge0\), and
\[
 \frac{Q'(d)}{2\pi}\ge
        (1-m^2)\cos2\pi d-2m^2>\frac25 .
 \tag{16}
\]
Indeed \(2\pi d<3\pi/25<66/175\), whose square is less
than \(1/7\); hence \(\cos2\pi d>13/14\), giving the
stronger lower bound \(161/350>2/5\).

The positive cotangent denominator satisfies
\[
 \cosh2\pi y_{\rm rec}-\cos2\pi d
 <1+\frac6{83}-\frac{13}{14}
 =\frac{167}{1162}<\frac3{20}.
 \tag{17}
\]
For the hyperbolic bound use
\(\cosh z-1\le(z^2/2)/(1-z^2/12)\) when \(z^2<1/7\).
Dividing the integrated (16) by (17) yields
\[
 \Re\{(1+im)^2\cot\pi(d-iy_{\rm rec})\}
 >-2m\coth(\pi\eta)+\frac{16\pi}{3}(d-\delta)
 \tag{18}
\]
when \(d>\delta\); the non-strict endpoint version suffices.

Parameterize the straight critical-to-cut segment by
\(u(s)=u_c+s\Delta(1+im)\), \(0\le s\le1\).
Then \(d-\delta=(1-s)\Delta\).
The exact Hessian is
\(F_{uu}=-\pi(A_0+\cot\pi(e-u))\).
Equations (14)--(15) imply
\[
 \Re\{A_0(1+im)^2\}>\frac{2496}{625},\qquad
                  -2m\coth(\pi\eta)>-\frac{17}{4}.
\]
After integration with the actual Taylor weight \(1-s\),
(18) consequently gives
\[
\begin{split}
 &\int_0^1(1-s)
     \Re\{(A_0+\cot\pi(e-u(s)))(1+im)^2\}\,ds\\
 &\hspace{12mm}>
       -\frac{641}{5000}+\frac{16\pi\Delta}{9}
       >-\frac{641}{5000}+\frac7{40}
       =\frac{117}{2500}>0.
\end{split}
 \tag{19}
\]
The second comparison uses \(\Delta>63/2000\) and \(\pi>25/8\).
Taylor's exact second-order integral from \(F_u(e,u_c)=0\)
therefore proves
\[
             \Re F(e,b(E))<\Re S(e)
 \tag{20}
\]
with a uniform positive gap. No pointwise positivity of the
whole directional form is asserted or needed.

For completeness the other cut stays \(a_L=1/20\).
Along its segment, (10) gives
\(\Im\cot\pi(e-u)<15\).
The same tangent/cotangent formulas give
\(\Re A_0>4\) and
\(|\Im A_0|<(4/15)\Re A_0\), since
\(\sin2\pi\Re u>3/10\).
Thus, writing \(F_{uu}=-A_*+iB_*\),
\[
 |B_*|<(241/60)A_*,\qquad
 \frac{|\Delta\Im u|}{|\Delta\Re u|}<\frac3{28}.
\]
The left cone bracket exceeds
\[
          1-\frac9{784}-\frac{241}{280}
                            =\frac{501}{3920}>0.
 \tag{21}
\]
This proves the other real-cut gap
\(\Re F(e,a_L)<\Re S(e)\).
Compactness gives common positive lower bounds for both gaps.

## 5. All original real tails and the absolute action floor

For lower rows \(x\le1/20\),
\(E-x\ge17/100>1/6\), so the original lower force is
still greater than \(27\).

For \(x\ge b(E)\ge219/1000\), \(\pi x>17/25\).
The positive tangent polynomial through degree five gives
\[
 \tan(\pi x)>
 \frac{17}{25}+\frac{(17/25)^3}{3}
                    +\frac{2(17/25)^5}{15}>\frac45.
\]
The last numerator comparison, with common denominator
\(146484375\), is \(117802214>117187500\).
The sine and cosine polynomials at \(17/25\) give
\[
 \sin\pi E>5/8,\qquad \cos\pi E<4/5 .
\]
Keep the unchanged height bounds
\(\sinh\pi\eta<1/5\) and \(e^{\pi\eta}<5/4\).

In the exact force formula (9) of
[the original bridge real-tail theorem](research_mixed_endpoint_bridge_real_tails.md),
the postwall real-angle maximum is less than
\[
 \frac{4(4/5)^3}{27(5/8)^2}<\frac15.
\]
Before the wall use its width \(1/1000\) and
\(\sin\pi x>3/5\), giving the same bound.
The height contribution is at most
\[
 \frac15\frac{25}{16}\frac{\sqrt{41}}4
                  <\frac{65}{128},
\]
since \(\sqrt{41}<13/2\).
Every real row from \(b(E)\) to one half therefore has
\[
                  e^{R_x}<
 \frac54\left(\frac15+\frac{65}{128}\right)
                           =\frac{453}{512}<\frac9{10}.
 \tag{22}
\]
All revived rows past the private endpoint are included.

On the real interval \([11/50,7/20]\), the exact original
curvature formula similarly gives
\[
 0<-\lambda''(E)
 <\pi\left(\frac54+\frac2{(5/8)(7/5)}\right)
 =\frac{99\pi}{28}<\frac{23}{2}.
\]
The square-root lower bound follows as before from
\(\cos2\pi E<1/4\).
Use only the printed saved consequences
\(\lambda(7/20)>108/125\) and
\(|\lambda'(7/20)|<1/200\), with the original source
identified in
[the bridge phase-floor theorem](research_mixed_endpoint_bridge_phase_floor.md).
The actual displacement is at most \(13/100\), so
\[
 \lambda(E)>
 \frac{108}{125}-\frac1{200}\frac{13}{100}
          -\frac{23}{4}\left(\frac{13}{100}\right)^2
 =\frac{30647}{40000}>\frac{1511}{2000}.
 \tag{23}
\]
No saved primitive is recomputed or replayed.

The above-curve theorem preserves the original chamber up
to the real-auxiliary curve. Equations (9)--(10) preserve it
below the curve and give \(\Im(e-u_c)<0\).
Thus
\[
 \partial_\eta\Re S=
       -\Arg\sin\pi(e-u_c)+\pi\Re u_c>0,
\]
and the lower bound (23) persists on (2).
The reflected upper auxiliary half uses only \(E>1/6\);
its complete ceiling remains \(67/105\), strictly below
this own action. Together with (20)--(22), this pays every
omitted physical or revived row, with the original carrier
and zero-safe factorial inequalities.

## 6. Finite contour completion and derivatives

Use the original half-grid cuts
\[
 a_N=(\lceil Na_L\rceil-1/2)/N,\qquad
 b_N=(\lceil Nb(E)\rceil-1/2)/N .
\]
All retained primitive real parts are regular, with
\(0<\Re u<E\) and reciprocal real separation
\(E-\Re u\ge1/1000+O(N^{-1})\).
The exact retained row has its original nonzero \(N^{-2}\)
symbol, not a new interpolation.

For \(h_c=-H<0\), the original signed-height reflection
pays the opposite upper horizontal alias by
\(\pi(1+2E)H\); the main-side alias loses \(2\pi H\).
Horizontal concavity, vertical convexity and the two real
cut gaps control both weighted horizontal currents, all
four vertical sign-halves and both unweighted joins.
At zero auxiliary height use the original fixed small
symmetric rectangle with \(|\Im F_u|<\pi\).
A slight enlargement keeps the saddle interior, and a
finite cover preserves uniform gaps.

The exact residue density is \(+N\).
Combining the \(N^{-2}\) row and interior \(N^{-1/2}\)
Gaussian therefore gives precisely \(N^{-3/2}\), with the
original nonzero coefficient in (3).
Every Newton and reciprocal zero, both parities and all
off-grid revived rows remain in the zero-safe discarded
source estimates.
They preserve their strict gaps on a fixed small
ordinary-color disk; fixed-base contours and integer cuts
then give the local holomorphic expansion. A finite cover
and Cauchy's formula give all stated normalized mixed jets.
No moving cutoff is differentiated.

Finally, the preceding below-curve strips and the
above-curve source cover the complementary depths and
real parts through \(49/100\), with identical original
actions and coefficients on overlaps. This proves the
rectangle consequence following (3). All outer contour
comparisons remain separate.

