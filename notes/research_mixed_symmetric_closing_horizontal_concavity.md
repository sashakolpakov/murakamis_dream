# Horizontal concavity of the actual symmetric closing phase

Private written phase and source deduction, 9 November 2026. The
original symmetric closing phase has a strictly negative real second
derivative on the taller positive rectangle. Its actual geometric
point is therefore the unique horizontal maximum there, with a
quantitative quadratic gap. A weaker curvature bound holds on the
whole symmetric phase rectangle. The complete inner-source theorem
then pays the positive horizontal portions separated from that point.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, or frozen-source edit is used.

## 1. Original phase and statement

Keep the original cubic branch and stationary action of the
[taller strip theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md):
\[
 \begin{gathered}
 \mathcal V=\{u:|\Re u|\le\pi/2,\ |\Im u|\le7/10\},\qquad
 \mathcal V_+=\{a-ih:0\le a\le\pi/2,\ 0\le h\le7/10\},\\
 c(u)=\cos(t_*(u)/2),\quad C(u)=\cos(u/2),\qquad
 4c^3-4ic^2-3c+i=C,\\
 f(u)=\operatorname{arsinh}\{c(u)\tan(u/2)\},\qquad
 S'(u)=-f(u)/\pi,\qquad S(0)=S_3(0,0).
 \end{gathered}
 \tag{1}
\]
The return is the original principal return, holomorphic on a
neighborhood of \(\mathcal V\). The closing phase is exactly that
of the [original symmetric trace](research_mixed_symmetric_343_closing_trace_and_domain.md):
\[
                        \Xi(u)=2S(u)+iu^2/\pi-iu .
 \tag{2}
\]
Its additive constant has not been changed.

The actual positive geometric point is
\[
 u_g=\beta_g-iK_g,\qquad
 0<\beta_g<\pi/2,\qquad17/30<K_g<7/10
 \tag{3}
\]
by the [strict height localization](research_mixed_symmetric_closing_height_below_seven_tenths.md).
That theorem retains the unsquared middle equation
\[
                       f(u_g)=i(u_g-\pi/2).
 \tag{4}
\]
In particular \(\Xi'(u_g)=0\).

**Theorem.** With exactly these branches,
\[
 \begin{array}{ll}
 \Re f'(u)>56/425>1/8,
       &\Re\Xi''(u)<-1/(4\pi),\qquad u\in\mathcal V_+,\\[2mm]
 \Re f'(u)>16/425>1/32,
       &\Re\Xi''(u)<-1/(16\pi),\qquad u\in\mathcal V .
 \end{array}
 \tag{5}
\]
Consequently, writing \(\Xi_g=\Re\Xi(u_g)\),
\[
 \Re\Xi(a-iK_g)
 \le\Xi_g-\frac{(a-\beta_g)^2}{8\pi}
                          \qquad(0\le a\le\pi/2),
 \tag{6}
\]
and
\[
 \Re\Xi(a-iK_g)
 \le\Xi_g-\frac{(a-\beta_g)^2}{32\pi}
                          \qquad(-\pi/2\le a\le\pi/2).
 \tag{7}
\]
Equality in either estimate is possible only at \(a=\beta_g\).
The actual closing Hessian is nonzero, with
\[
                         |\Xi''(u_g)|>1/(4\pi).
 \tag{8}
\]
In particular the two ends of the positive horizontal have
gaps at least
\[
             \beta_g^2/(8\pi),\qquad
                         (\pi/2-\beta_g)^2/(8\pi),
 \tag{9}
\]
respectively. These are positive constants for this fixed
original geometric point.

## 2. Exact implicit derivative and its branch

Put
\[
 \Delta=12c^2-8ic-3,\qquad
 D_0=c^2+C^2-c^2C^2.
 \tag{10}
\]
Differentiating the cubic in (1), without changing its root,
gives
\[
                     c'(u)=-\frac{\sin(u/2)}{2\Delta}.
 \tag{11}
\]
The taller-strip guards are, throughout \(\mathcal V\),
\[
 c=p+iq,\quad p>3/4,\quad1/6<q<1/3,\quad
 |c|<1,\quad0<\Re t_*<\pi/2,\quad0<-\Im t_*<1 .
 \tag{12}
\]
It follows that
\[
 \Re\Delta=12p^2-12q^2+8q-3>19/4,\qquad
                            0<\arg c<4/9 .
 \tag{13}
\]
For the first bound, \(8q-12q^2>1\) on the stated
open interval. For the second use \(q/p<4/9\) and
\(\arctan x<x\).

The same phase guards give
\[
 |C|\le\cosh(7/20)<17/16,\qquad
 |\arg C|<7/20 .
 \tag{14}
\]
Here the modulus bound uses
\(|C|^2=(\cos(\Re u)+\cosh(\Im u))/2\), not merely the
rectangle for its real and imaginary parts. The argument
bound follows from
\[
 |\tan(\arg C)|
   =|\tan(\Re u/2)\tanh(\Im u/2)|
                  \le\tanh(7/20)<7/20 .
 \tag{15}
\]
In addition,
\[
 |1-c^2|<4/5,\qquad |1-C^2|<13/20,\qquad
                         |1-D_0|<13/25 .
 \tag{16}
\]
For the first inequality,
\[
 |1-c^2|
 =\{\cosh(-\Im t_*)-\cos(\Re t_*)\}/2
 <\tfrac12\cosh1<4/5 .
 \tag{17}
\]
The positive series gives
\(\cosh1\le3/2+(1/24)/(1-1/30)=179/116<8/5\).
For the second inequality in (16), use
\(\cos(\Re u)\ge0\) and
\(\cosh(7/10)<13/10\), as proved by the positive-series
witness in the height-localization note. The third is the
identity \(1-D_0=(1-c^2)(1-C^2)\).

Take the principal square root of \(D_0\). Equation (16) shows
\[
 |\arg\sqrt{D_0}|<1/3,\qquad |\sqrt{D_0}|<5/4 .
 \tag{18}
\]
Indeed \(\sin(2/3)>2/3-(2/3)^3/6=50/81>13/25\), so the disk
in (16) has arguments of modulus less than \(2/3\). Also
\(|D_0|<38/25<25/16\), where the last comparison is \(608<625\).

The original return obeys
\[
                           \cosh f=\sqrt{D_0}/C .
 \tag{19}
\]
Its square is the algebraic identity following from (1).
At \(u=0\), \(C=1,D_0=1,f=0\), so the sign in (19) is
positive. Both sides are holomorphic and nonzero on the
connected phase rectangle and its fixed neighborhood:
the original cut-safe return is supplied by the taller-strip
theorem, and (16) keeps \(D_0\) away from zero. Analytic
continuation therefore proves (19) without a new square-root
or logarithmic choice.

Using (11),(19), the derivative has the exact two-term form
\[
 f'(u)=L(u)+E(u),\qquad
 L=\frac{c}{2C\sqrt{D_0}},\qquad
 E=-\frac{1-C^2}{2\Delta\sqrt{D_0}},\qquad
 \frac E L=-\frac{C(1-C^2)}{c\Delta}.
 \tag{20}
\]
This expression includes the motion of the original inner critical
point. Keeping only the first term would not be the derivative of
the stationary inner action.

## 3. Uniform real-part bounds

Equations (12)--(18) give
\[
 |L|>\frac{3/4}{2(17/16)(5/4)}
                    =\frac{24}{85},\qquad
 \left|\frac E L\right|
 <\frac{(17/16)(13/20)}{(3/4)(19/4)}
                    =\frac{221}{1140}<\frac15 .
 \tag{21}
\]
For \(u\in\mathcal V_+\), the half-cosine \(C\) is in the
closed first quadrant. Thus
\[
             -41/60<\arg L<7/9 .
 \tag{22}
\]
Both endpoints are strictly between \(-\pi/4\) and
\(\pi/4\). For the larger positive endpoint use
\(7/9<25/32<\pi/4\), where \(224<225\) and \(\pi>25/8\).
The negative endpoint has smaller absolute value.
Consequently
\[
 \Re f'\ge\Re L-|E|
    >|L|\left(\frac23-\frac15\right)
    >\frac{24}{85}\frac7{15}
                 =\frac{56}{425}>\frac18 .
 \tag{23}
\]
Here \(\cos(\pi/4)>2/3\), and the final comparison is \(448>425\).

On the full symmetric rectangle, retain both signs of \(\arg C\).
Then
\[
              -41/60<\arg L<203/180 .
 \tag{24}
\]
This interval lies strictly inside \((-3\pi/8,3\pi/8)\):
the larger upper endpoint is less than \(75/64<3\pi/8\),
since \(12992<13500\). Moreover
\(\cos(3\pi/8)=\tfrac12\sqrt{2-\sqrt2}>1/3\);
for example \(\sqrt2<3/2\) gives
\(\cos(3\pi/8)>1/(2\sqrt2)>1/3\).
Equations (21),(24) therefore yield
\[
 \Re f'>
 |L|\left(\frac13-\frac15\right)
 >\frac{24}{85}\frac2{15}
                 =\frac{16}{425}>\frac1{32}.
 \tag{25}
\]
The last comparison is \(512>425\).

Finally
\[
                   \Xi''(u)=-2f'(u)/\pi+2i/\pi .
 \tag{26}
\]
Equations (23),(25) prove all curvature bounds in (5).
Integrating them twice on the horizontal line through the
actual stationary point, using (4), proves (6)--(9).
No positivity of an unspecified effective Hessian has been
assumed; its real part is controlled directly by (20).

## 4. A finite consequence on the covered positive horizontal

This section only uses a contour already inside the proved
inner-source domain. Let
\[
 Q_N(u)=\phi_N\!\left[
 R_N^3\mathcal K_N(-2,x)\mathcal K_N(x,-2\cos u)\right],
 \quad
 W_N(u)=\frac{e^{-iNu}}{(1-(-1)^{N-1}e^{-iNu})^2}.
 \tag{27}
\]
Both edges and the full Hermite trace in \(Q_N\) are retained.
The [complete inner theorem](research_mixed_symmetric_closing_complete_inner_asymptotic.md)
gives the uniform upper bound
\[
             |Q_N(u)|\le C N^{-3/2}e^{N\Re S(u)}
                                      \qquad(u\in\mathcal V_+).
 \tag{28}
\]
For the exact outer phase multiplier,
\[
 \left|e^{iN(a-iK_g)^2/\pi}W_N(a-iK_g)\right|
 \le
 \frac{\exp\{N(2aK_g/\pi-K_g)\}}
                   {(1-e^{-NK_g})^2}.
 \tag{29}
\]
Thus for any fixed \(d>0\), the absolute integral over the
portion \(0\le a\le\pi/2\), \(|a-\beta_g|\ge d\), of the
original integrand
\[
 \sin u\,Q_N(u)^2e^{iNu^2/\pi}W_N(u)\,du
 \tag{30}
\]
has, even after its original \(N^2/\pi\) prefactor, the bound
\[
 C N^A\exp\left\{N\left(\Xi_g-\frac{d^2}{8\pi}\right)\right\}.
 \tag{31}
\]
The unit crossing scalar has no effect on this upper bound.
Equation (29) retains the whole sampling denominator; no
Fourier alias has been discarded. Both level parities are
covered. This proves an actual remote-current bound on the
covered positive segment, rather than applying a phase
inequality to an unlicensed source.

The corresponding negative-half phase inequality (7) is not,
by itself, a bound for the finite source on that half. The
complete inner theorem used in (28) has the positive lower
domain. Connections to the original outer sampling contour,
negative or reflected source regions, far samples and their
normals, endpoint currents, and the nonzero full closing
coefficient remain distinct obligations. No estimate beyond
\(|\Re u|\le\pi/2\) is asserted here.

## Frozen source bindings

- Full taller cubic/action and original logarithmic return:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Actual geometric point inside the taller rectangle:
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
- Original symmetric closing trace and phase normalization:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Complete finite inner source, both full edges and both parities:
  4e6d58951cff746a5daf6b3efcf3df917233e64d773d936a232dbc6bb870c96c.
