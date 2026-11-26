# Complete endpoint continuation west to private real part 23/100

Research deduction, 8 November 2026. The below-curve endpoint packet
extends westward to \(E=23/100\), at the same depth \(3/50\).
The additional estimate keeps the real and imaginary parts of the
auxiliary root correlated. In particular the depth of \(e-u_c\)
increases below the auxiliary-real curve. This supplies the sharper
cotangent bound needed for both real cut comparisons.

This is a complete theorem for the original endpoint coefficient.
It does not estimate an outer-cap path. No numerical evaluation or
change to a frozen source is used.

## 1. Source, domain, and statement

Keep exactly
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\qquad
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu.
 \tag{1}
\]
All Newton polynomials, factorials, original logarithms and scalars
are those of [the specified endpoint source](research_complete_boundary_complex_index.md).
Write \(S(e)=F(e,u_c(e))\). Let \(\eta_0(E)\) be the depth of
the original [auxiliary-real curve](research_mixed_endpoint_auxiliary_real_curve.md),
so that
\[
 p_0=1-2t^2+2it,\quad E=\arg p_0/(2\pi),\quad
 \eta_0(E)=\log|p_0|/(2\pi).
 \tag{2}
\]

**Theorem.** On a fixed complex neighborhood of
\[
 \mathcal W\times\{-2\},\qquad
 \mathcal W=\{E-i\eta:23/100\le E\le6/25,\quad
                              \eta_0(E)\le\eta\le3/50\},
 \tag{3}
\]
the complete finite function (1) has
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                 (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.
 \tag{4}
\]
The action, coefficient and Gaussian square root are the original
ones. Both parities, all revived rows, and every fixed mixed
ordinary-color/index derivative of the normalized error are included.
Together with [the earlier below-curve corridor](research_mixed_endpoint_below_auxiliary_curve.md),
this covers its whole below-curve domain with left endpoint replaced
by \(23/100\); empty vertical sections retain their earlier convention.

## 2. Sharper correlated root bounds

Put
\[
 p=Re^{2\pi iE},\quad c=\Re p,\quad
 \sqrt{1-2p}=A-iB,\quad
 z=\tan\pi u_c=A/2-i(B-1)/2.
 \tag{5}
\]
Here \(A,B>0\), and \(B\ge1\) below the curve, as follows from
the exact square-root monotonicity proved in the earlier corridor.
The same original root and zero lift continue from (2).

The sharper radius estimate is
\[
 R<35/24,\qquad 3R/50<c<11/60.
 \tag{6}
\]
For the first, the first two positive logarithmic terms give
\[
 \log(35/24)>
       \frac{22}{59}+\frac{2662}{616137}>\frac{66}{175}
                       >\frac{3\pi}{25}\ge2\pi\eta.
\]
The middle comparison reduces to
\(27485150>27110028\).
For the upper bound for \(c\), use
\(\cos2\pi E\le\sin(\pi/25)<22/175\).
For the lower bound, \(E\le6/25\) gives
\(\cos2\pi E\ge\sin(\pi/50)>3/50\);
the last inequality follows from
\(\pi/50>1/16\) and
\(\sin(1/16)\ge1/16-(1/16)^3/6>3/50\).

The exact formulas
\[
 A^2=\frac{\sqrt{1-4c+4R^2}+1-2c}{2},\qquad
 B^2=\frac{\sqrt{1-4c+4R^2}-1+2c}{2}
 \tag{7}
\]
give the uniform bounds
\[
                    A<139/100,\qquad 1\le B<27/25.
 \tag{8}
\]
For \(B\), its square increases in \(c\) and \(R\). At the upper
bounds (6), the radical is less than
\(\sqrt{6317/720}<80/27\). Hence
\[
 B^2<629/540<729/625.
\]
For \(A\), its square decreases with \(c\), and its value on
\(c=3R/50\) increases with \(R>1\). The latter derivative sign
follows by the same squared comparison as the square-root
monotonicity, with \(c_0=3/50\). At \(R=35/24\), it follows that
\[
 A^2<
 \frac{\sqrt{6593/720}+33/40}{2}
 <\frac{771}{400}<\left(\frac{139}{100}\right)^2,
\]
using \(\sqrt{6593/720}<303/100\).
Also \(A^2=B^2+1-2c>49/30\).

Write \(u_c=\xi+ih_c\), and \(z=x-iy\) with \(y=(B-1)/2\).
Thus \(0\le y<1/25\), and
\[
 x^2=\frac{B^2+1-2c}{4}
                    >\frac{49}{120}+y+y^2.
 \tag{9}
\]
The real part of the original arctangent lies in \((0,\pi/4)\).
Its elementary double-angle formula, together with (8), gives
\[
 \tan(2\pi\xi)
   <\frac{4(139/100)}{4-(139/100)^2-(2/25)^2}
   =\frac{11120}{4123}<\frac{27}{10}
                         <\cot(11\pi/100).
 \tag{10}
\]
For the last comparison use
\[
 \cot q>\frac1q-\frac q2,\quad
 q=11\pi/100<121/350,\quad
 \frac{350}{121}-\frac{121}{700}
       =\frac{230359}{84700}>\frac{27}{10}.
\]
On the other hand, \(x^2>49/120>1/3\) gives
\(\xi>\arctan(1/\sqrt3)/\pi=1/6\).

On the vertical arctangent segment from \(x\) to \(x-iy\),
(9) gives
\[
 0<\Re\frac1{1+(x-iv)^2}
     \le\frac1{1+x^2-v^2}
     <\frac1{169/120+y}\qquad(0\le v\le y).
\]
Integrating, and using monotonicity of
\(y/(169/120+y)\), proves
\[
 \boxed{\quad
 \frac16<\xi<\frac{39}{200},\qquad
 0\le-h_c<\frac{24}{869\pi}<\frac9{1000}.
 \quad}
 \tag{11}
\]
The last strict comparison follows from \(\pi>25/8\).
In particular \(0<\xi<E\), all primitive real parts remain regular,
and the original critical point is simple.

We also have throughout (3)
\[
              R\ge R_0(E)>13/10,\qquad
                          \pi\eta>3/23.
 \tag{12}
\]
Indeed the increasing curve radius at \(E=23/100\) solves
\((1-c_0^2)R_0^2+2c_0R_0-2=0\), with
\(c_0=\sin(\pi/25)<22/175\).
The quadratic at \(R=13/10\), maximized at this upper \(c_0\),
is less than \(-30171/3062500<0\).
Now \(\log(13/10)>6/23\) proves (12).

## 3. The correlated depth of the reciprocal argument

The following estimate improves subtracting two independent height
bounds:
\[
             \eta+h_c(E-i\eta)\ge\eta_0(E).
 \tag{13}
\]
We prove it on each entire interval
\(\eta_0(E)\le\eta\le3/50\), retaining the original branch.
At a critical point put
\[
 A_0=2\tan\pi u_c+3\cot\pi u_c=a+ib,\qquad
 C=\cot\pi(e-u_c)=c_1+id.
\]
By (11), \(a>4\), \(a<2+3\sqrt3<8\), and
\[
                    0\le b<(2/25)a<16/25.
 \tag{14}
\]
Here \(\sinh(2\pi|h_c|)<1/15\),
\(\sin(2\pi\xi)>\sqrt3/2>6/7\), so the ratio of the imaginary
to real part of each tangent/cotangent is less than
\(7/90<2/25\). Positivity of \(b\) follows explicitly from
\[
 b=\sinh(2\pi|h_c|)
   \frac{\cosh(2\pi|h_c|)+5\cos(2\pi\xi)}
        {\cosh^2(2\pi|h_c|)-\cos^2(2\pi\xi)}\ge0.
\]
The elementary tangent/cotangent product bound gives \(a>4\);
the bounds \(a<8\) use their real-axis values.

From (11)--(12),
\[
 q=\pi(\eta+h_c)>
    \frac3{23}-\frac{24}{869}=\frac{2055}{19987},
                      \qquad q<1/5.
\]
Thus \(c_1>0\), and
\[
                0<d\le\coth q<1/q+q<10.
 \tag{15}
\]
This is only a coarse initial bound, obtained without (13).
Implicit differentiation of the original equation gives exactly
\[
                  u_c'(e)=\frac{C+i}{A_0+C},\qquad
       1-u_c'(e)=\frac{A_0-i}{A_0+C}.
 \tag{16}
\]
The numerator of the real part of the latter ratio is
\[
 a(a+c_1)+(b-1)(b+d)
     >16-(16/25+10)>0.
 \tag{17}
\]
Here \(0\le b<1\); the case \(h_c=0\) is included.
Consequently
\[
 \frac d{d\eta}(\eta+h_c)
             =1-\Re u_c'(e)>0.
\]
At the initial curve point \(h_c=0\). Integration proves (13).
This controls the actual root, not a freely chosen auxiliary height.

The sharper consequence is now
\[
 0<d\le\coth(\pi\eta_0(E))
       <\frac{23}{3}+\frac1{15}
       =\frac{116}{15}<\frac{31}{4}.
 \tag{18}
\]
We used \(q=\pi\eta_0>3/23\), \(q<1/5\), and
\(\coth q<1/q+q/3\).
The last elementary inequality follows by differentiating
\((1+q^2/3)\sinh q-q\cosh q\), whose derivative is
\((q/3)(q\cosh q-\sinh q)>0\).
On either straight segment from \(u_c\) to a real cut,
\(\eta+\Im u\ge\eta+h_c\), so (18) holds on the whole
segment as well.

## 4. Actual real-cut comparisons

Use the fixed-form cuts
\[
                         a_L=1/20,\qquad b(E)=E-1/1000.
 \tag{19}
\]
They enclose \(\xi\) by (11). On the left segment,
\(\sin(2\pi\Re u)>3/10\) and
\(\sinh(2\pi|\Im u|)<1/15\). The same elementary product
and ratio identities as in the earlier corridor imply
\[
 \Re A_0>4,\qquad |\Im A_0|<(\Re A_0)/4.
\]
Together with (18), these give, writing \(F_{uu}=-A_*+iB_*\),
\[
                   |B_*|<(9/4)A_*.
 \tag{20}
\]
The displacement slope is less than
\((9/1000)/(1/6-1/20)=27/350<1/12\).
The left cone bracket is therefore greater than \(89/144>0\).

On the right segment \(1/6\le\Re u\le6/25\). The tangent
and cotangent real parts, denoted \(a_1,a_2\), satisfy
\[
 a_1a_2>625/629,\qquad a_2>21/20.
 \tag{21}
\]
For the first inequality use the ratio bound \(2/25\) above.
For the second, \(\cot\pi\Re u>\cot(6\pi/25)>103/97\)
by \(\tan(\pi/100)>3/100\). Also
\(\sinh(\pi|\Im u|)<1/30\) and
\(\sin(\pi\Re u)\ge1/2\), so
\[
 \Re\cot\pi u>\frac{103}{97}\frac{225}{226}>21/20.
\]
The function \(2(625/629)/v+3v\) increases for \(v\ge21/20\).
Thus (21) gives
\[
 \Re A_0>25000/13209+63/20>5,\qquad
 |\Im A_0|<(2/25)\Re A_0.
\]
Together with (18),
\[
 |B_*|<(33/20)A_*,\qquad
 \frac{|\Delta\Im u|}{|\Delta\Re u|}
       <\frac{9/1000}{23/100-1/1000-39/200}=\frac9{34}.
 \tag{22}
\]
The right cone bracket is greater than
\[
          1-\frac{81}{1156}-\frac{33}{10}\frac9{34}
                              =\frac{163}{2890}>0.
 \tag{23}
\]
The exact second-order integral from the original critical point
therefore proves both real cut gaps
\[
           \Re F(e,a_L)<\Re S(e),\qquad
           \Re F(e,b(E))<\Re S(e).
 \tag{24}
\]
Their minimum on the compact domain (3) is strictly positive.

## 5. All omitted rows and the absolute action floor

We verify the small extension of the earlier real-tail proof rather
than using its former \(E\ge6/25\) statement outside its range.
For the lower rows \(x\le1/20\), \(E-x\ge9/50>1/6\);
the original force \(e^{R_x}\) is therefore still greater than \(27\).
For \(x\ge b(E)\), the old algebraic force bound applies with
\[
 \cot\pi x<6/5,\quad \sin\pi E>13/20,\quad
 \cos\pi E<4/5,\quad
 \sinh\pi\eta<1/5,\quad e^{\pi\eta}<5/4.
 \tag{25}
\]
Here \(x\ge229/1000\), so \(\pi x>23/32\), using
\(\pi>157/50\).
The original tangent lower polynomial gives the first inequality.
The sine and cosine polynomials at \(23/32\) give the next two.
The height bounds are unchanged.

In the force formula from
[the bridge real-tail proof, equation (9)](research_mixed_endpoint_bridge_real_tails.md),
the real-angle term for \(x\ge E\) is at most
\[
 \frac{4\cos^3\pi E}{27\sin^2\pi E}<\frac15.
\]
For \(b(E)\le x\le E\), use \(E-x\le1/1000\) and
\(\sin\pi x>3/5\); the same term is again less than \(1/5\).
The height term remains less than \(288/625\). Consequently
\[
                 e^{R_x(e,x)}
                  <\frac54\left(\frac15+\frac{288}{625}\right)
                  =\frac{413}{500}<1
                         \qquad(b(E)\le x<1/2).
 \tag{26}
\]
Thus every real row outside the cuts and below one half reduces
to its corresponding value in (24), including every revived row.

The reflected upper-half proof is unchanged: it uses only
\(E>1/6\), so its ceiling remains \(67/105\).
For completeness the original absolute phase floor also extends.
On the real interval from \(23/100\) to \(7/20\),
\[
 \cot\pi E<6/5,\quad \sin\pi E>13/20,\quad
                  |\sqrt{2-e^{-2\pi iE}}|>7/5.
\]
The last follows from \(\cos2\pi E<1/4\).
The exact original curvature identity therefore gives
\[
       0<-\lambda''(E)<(1546/455)\pi<11,\qquad
                          \lambda(E)=\Re S(E).
 \tag{27}
\]
Use precisely the already printed original scalar bounds
\(\lambda(7/20)>108/125\), \(|\lambda'(7/20)|<1/200\)
and their source identified in Section 4 of
[the bridge phase-floor theorem](research_mixed_endpoint_bridge_phase_floor.md).
No saved value is recomputed. Taylor's formula with
\(|E-7/20|<7/50\) gives \(\lambda(E)>1511/2000\).

The [above-curve theorem](research_mixed_endpoint_region_above_real_curve.md)
keeps the original primitive chamber and nonnegative auxiliary height
from \(\eta=0\) to \(\eta_0(E)\). Beyond it, (11)--(15) prove
the same chamber and \(\Im(e-u_c)<0\). On the whole radial interval,
\[
 \partial_\eta\Re S
      =-\Arg\sin\pi(e-u_c)+\pi\Re u_c>0.
 \tag{28}
\]
Hence \(\Re S(e)>1511/2000\) on (3). All upper-half rows
have a uniform action gap greater than \(1/10\).

## 6. Complete finite contour and scope

Use the half-grid cuts at
\[
 L_N=\lceil Na_L\rceil,\quad M_N=\lceil Nb(E)\rceil,\qquad
 a_N=(L_N-1/2)/N,\quad b_N=(M_N-1/2)/N .
 \tag{29}
\]
All omitted rows are paid by (24), (26), and the upper-half
comparison. These are bounds on literal finite summands, with
the original carrier, Newton factors and reciprocal zeros.
No physical-grid support is imposed at complex \(e\).

The retained regular strip has \(0<\Re u<E\) and
\(E-\Re u\ge1/1000\). Its original exact interpolation has
the nonzero \(N^{-2}\) symbol of the earlier corridor proof.
The critical height is nonpositive. For a nonzero height
\(-H=h_c\), the exact reflection gives the opposite upper
alias loss \(\pi(1+2E)H\), while the main-side alias loses
\(2\pi H\). Horizontal concavity gives the main maximum;
vertical convexity and the paid real cuts bound all four
weighted vertical half-sides and both unweighted joins.
At \(H=0\) use the original small symmetric finite rectangle
with \(|\Im F_u|<\pi\); the two aliases have a strict loss.
These are precisely the complete signed-height currents in
[the earlier corridor proof, Section 4](research_mixed_endpoint_below_auxiliary_curve.md),
now with every premise proved on (3).

The exact \(+N\) residue density and local Gaussian give
\(N^{-2}N N^{-1/2}=N^{-3/2}\), with the original nonzero
coefficient. The uniform zero-safe row estimates include both
parities and every Newton or reciprocal zero. They preserve
the discarded-source gaps on a fixed small ordinary-color disk.
Fix the base cuts and all contours before moving the parameters;
the simple critical chart and all strict currents persist.
A finite cover and Cauchy's formula prove (4) and every stated
normalized mixed derivative, without differentiating a cutoff.

This proves the endpoint source on the westward below-curve
corridor. Outer action comparisons, outer contour remainders,
and a full outer-cap or filled-source conclusion remain separate.
