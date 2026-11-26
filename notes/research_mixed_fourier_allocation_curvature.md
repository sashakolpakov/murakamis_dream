# Two real-row bounds survive the Fourier boundary allocation

Research deduction, 7 November 2026. The last ordinary block and the
Fourier boundary use different outgoing weights. Their actions differ
by one explicit holomorphic function. That function is concave along
most of the relevant horizontal interval, and its possible failure of
concavity near the left endpoint costs less than the existing strict
row gaps. Consequently the real cuts at \(1/8\) and \(1/2\) remain
strictly below the original Fourier boundary action.

All comparisons below are analytic. No root, source maximum or
numerical test is evaluated. The true last row and the outgoing
summation contour remain separate questions.

## 1. The action added at the boundary

Keep the fixed original Fourier parameter
\[
 y=x_0,\qquad Y=e^{2\pi i y}=\rho e^{i\phi},\qquad
 .18299<\Re y<.18301,\quad .07871<\Im y<.07873.
 \tag{1}
\]
The original primitive and cardinal action are
\[
 \begin{split}
 g(q)&=\frac{\operatorname{Li}_2(e^{-2\pi iq})-\pi^2/6}{2\pi i},\\
 \ell_q(y)&=2\pi iy(q-\tfrac12)
 -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})
                      -\operatorname{Li}_2(Y)}{2\pi i}.
 \end{split}
 \tag{2}
\]
Their branches and additive constants are those of the original
finite source. Define
\[
 H(q)=\tfrac12g(q)+\ell_q(y),\qquad
 h_H(x)=\Re H(x+ih),\qquad -.102\le h\le-.001.
 \tag{3}
\]
The subscript on \(h_H\) distinguishes this real function from its
fixed height \(h\). A prime on \(h_H\) means differentiation in \(x\).

Put
\[
 R=e^{2\pi h},\quad \theta=2\pi x,\quad \delta=\theta-\phi,\quad
 D_A=1+R^2-2R\cos\theta,\quad
 D_B=1+\rho^2R^2-2\rho R\cos\delta.
 \tag{4}
\]
Both denominators are positive. Direct differentiation of (2) gives
\[
 h_H''(x)
   =\frac{\pi R\sin\theta}{D_A}
       -\frac{2\pi\rho R\sin\delta}{D_B}
   =-\frac{\pi R E(\theta,R)}{D_A D_B},
 \qquad
 E=2\rho\sin\delta\,D_A-\sin\theta\,D_B.
 \tag{5}
\]
Here \(\sin\delta>0\) throughout \(x\in[.22,.45]\), because
\(0<x-\Re y<1/2\). In particular the cardinal term has negative
real second derivative on this whole interval.

We will use the elementary bounds
\[
 \frac{121}{200}<\rho<\frac{123}{200},\qquad
 \frac{21}{40}<R<1,\qquad
 \frac25<\cos\phi<\frac{21}{50},\qquad
 \frac9{10}<\sin\phi<\frac{921}{1000}.
 \tag{6}
\]
The last two follow from the original parameter interval, as proved
in the [half-plane branch theorem](research_mixed_fourier_endpoint_halfplane_branch.md).
For the first, \( .49<2\pi\Im y<.5\).
The power series bound
\[
 e^t<1+t+\frac{t^2}{2(1-t/3)}\qquad(0<t<3)
 \tag{7}
\]
follows by majorizing the successive terms starting with \(t^2/2\);
their ratios are at most \(t/3\), with a strict inequality after
the next term. Thus \(e^{1/2}<33/20\), and
\(\rho>20/33>121/200\). In the other direction,
\[
 e^{.49}>1+.49+\frac{(.49)^2}{2}+\frac{(.49)^3}{6}
                                      >\frac{200}{123}.
\]
For \(R\), the bound \(2\pi(.102)<321/500\) and (7) give
\[
 R^{-1}
  <\frac{821}{500}+\frac{103041}{393000}
  =\frac{249449}{131000}<\frac{40}{21}.
 \tag{8}
\]
The last comparison has integer difference
\(40\cdot131000-21\cdot249449=1571>0\).

## 2. Strict concavity from \(x=.24\) onwards

**Lemma 1.** For every height in (3),
\[
                 h_H''(x)<-\frac1{10000}
                    \qquad(.24\le x\le.45).
 \tag{9}
\]

*Proof.* First take \(\theta_0=.48\pi\) and
\(\delta_0=\theta_0-\phi\). The bounds \(157/50<\pi<22/7\)
and (1) imply
\[
 \frac{1789}{5000}<\delta_0<\frac{359}{1000}.
 \tag{10}
\]
The alternating Taylor bounds for sine and cosine yield
\[
 \sin\delta_0>\frac7{20},\qquad
 \cos\delta_0>\frac{117}{125}.
 \tag{11}
\]
For the first it is enough to use
\(t-t^3/6>7/20\) at \(t=1789/5000\).
For the second use
\(1-t^2/2+t^4/24-t^6/720>117/125\) at \(t=359/1000\).
Also
\[
 0<\cos\theta_0=\sin(.02\pi)<\frac{63}{1000},
                    \qquad \sin\theta_0>\frac{99}{100}.
 \tag{12}
\]
The sine lower bound follows already from the cosine upper bound.

At this one angle, apply (6), (11) and (12) to (5). Since \(D_A,D_B\)
are positive and \(\sin\theta_0\le1\), the resulting lower bound is
\[
 \begin{split}
 E(\theta_0,R)
 &>\frac{847}{2000}\left(1+R^2-\frac{63}{500}R\right)
          -1-\frac{15129}{40000}R^2
          +\frac{14157}{12500}R\\
 &=-\frac{1153}{2000}
       +\frac{1811}{40000}R^2+\frac{1079199}{1000000}R.
 \end{split}
 \tag{13}
\]
Both nonconstant coefficients are positive. At \(R=21/40\)
the last expression is
\[
                  \frac{818687}{320000000}>\frac1{400}.
 \tag{14}
\]
Thus (14) is a strict lower bound for the actual radii.

It remains to show that moving the angle to the right does not lose
this bound after division by its positive sine. Write
\[
 c=\cos\phi,\quad v=\sin\phi,\quad X=-\cot\theta.
\]
For \(\theta_0\le\theta\le.9\pi\), \(X>-8/125\), by (12).
An exact rearrangement of (5) gives
\[
 \frac{E(\theta,R)}{\sin\theta}
 =2\rho(c+vX)(1+R^2)-1-\rho^2R^2
       +2\rho R\,\frac{cX+v+2vX^2}{\sqrt{1+X^2}}.
 \tag{15}
\]
The derivative of the last fraction is
\[
       \frac{c+3vX+2vX^3}{(1+X^2)^{3/2}}.
 \tag{16}
\]
For \(X\ge0\) its numerator is positive. For
\(-8/125\le X\le0\), it exceeds
\[
 \frac25-3\frac{921}{1000}\frac8{125}
                 -2\frac{921}{1000}\left(\frac8{125}\right)^3>0.
 \tag{17}
\]
Every \(X\)-dependent term in (15) therefore increases with \(X\).
Since \(-\cot\theta\) increases with \(\theta\), (14) and
\(\sin\theta_0\le1\) give
\[
                       E(\theta,R)>\frac{\sin\theta}{400}.
 \tag{18}
\]
On this interval \(\sin\theta\ge\sin(.9\pi)>3/10\).
Also \(D_A<4\), \(D_B<(13/8)^2\), and \(\pi R>3/2\).
Substituting these inequalities in (5) gives
\[
 -h_H''(x)>
       \frac{(3/2)(3/10)}{400\cdot11}
       =\frac9{88000}>\frac1{10000}.
 \tag{19}
\]
This proves (9). \(\square\)

On the short remaining interval, the positive upper bound is enough.
For \(x\in[.22,.24]\),
\[
 \Re\cot\pi(x+ih)\le\cot\pi x\le\cot(.22\pi)<\frac32.
 \tag{20}
\]
The first inequality follows from
\(\Re\cot\pi(x+ih)=\sin(2\pi x)/
[\cosh(2\pi h)-\cos(2\pi x)]\).
For the last, \(.22\pi>2/3\) and
\(\tan t>t\) on \(0<t<\pi/2\). The cardinal curvature in (5)
is negative, so
\[
                         h_H''(x)<\frac{3\pi}{4}.
 \tag{21}
\]

## 3. A uniform bound for the difference from a tangent line

**Lemma 2.** Let \(x_*\in[.24,.45]\), keep the same height \(h\)
at \(x\) and \(x_*\), and put \(q_*=x_*+ih\). Then for every
\(x\in[.22,.45]\),
\[
 \Re\{H(x+ih)-H(q_*)-H'(q_*)(x-x_*)\}
                         <\frac{33}{70000}.
 \tag{22}
\]
For \(x\ge.24\), the left side is nonpositive.

*Proof.* The latter assertion is Lemma 1 integrated along the segment
between \(x\) and \(x_*\). If \(x<.24\), the exact Taylor remainder
with the integration direction reversed is
\[
 h_H(x)-h_H(x_*)-h_H'(x_*)(x-x_*)
       =\int_x^{x_*}(t-x)h_H''(t)\,dt .
 \tag{23}
\]
The part from \(.24\) to \(x_*\) is nonpositive. Equations
(21) and \(0\le.24-x\le1/50\) bound the rest by
\[
 \frac{3\pi}{8}(.24-x)^2
       \le\frac{3\pi}{20000}<\frac{33}{70000}.
 \tag{24}
\]
Here \(\pi<22/7\). \(\square\)

## 4. Transfer of the two existing strict row estimates

Use an actual last-four Fourier reference with incoming flag
\(\eta=0,1\). Its fixed coordinates are \((s_*,a_*,q_*)\) as
in [the bare inner-contour theorem](research_mixed_fourier_right_cap_bare_inner_contour.md).
The outgoing point belongs to \(O_4\), hence
\[
 .24<\Re q_*<.36,\qquad -.102\le\Im q_*\le-.001 .
 \tag{25}
\]
The [correlated domain theorem](research_mixed_fourier_right_cap_annulus_completion.md)
places the auxiliary exterior leg in the domain of the original
ordinary source estimates. The original logarithmic equations
identify their reference with \((s_*,a_*,q_*)\).

The ordinarily allocated phase is
\[
 F(s,a,q)=Q_1(s;a,q)-\tfrac\eta2g(a)-\tfrac12g(q).
 \tag{26}
\]
The bare Fourier phase is exactly \(\mathscr F=F+H(q)\).
At the actual reference,
\[
 \mathscr F_s=\mathscr F_q=0,\qquad
 F_q=-H'(q_*),\qquad \mathscr F_a=F_a.
 \tag{27}
\]
For horizontal targets \(a=x+i\Im a_*\), \(q=z+i\Im q_*\),
let \(\Delta x=x-\Re a_*\), \(\Delta z=z-\Re q_*\), and
retain the old curvature coefficient
\(\kappa=1/2500000\). The old and new supporting planes are
\[
 \begin{split}
 B_F&=\Re F_*+\Re F_a\,\Delta x+\Re F_q\,\Delta z
                          -\kappa(\Delta x^2+\Delta z^2),\\
 B_{\rm F}&=\Re\mathscr F_*+\Re\mathscr F_a\,\Delta x
                          -\kappa(\Delta x^2+\Delta z^2).
 \end{split}
 \tag{28}
\]
The new plane is \(\mathcal L_\eta\) in the bare inner-contour
theorem. No outgoing marginal occurs in it, because of (27).

At either real cut \(s=c\), \(c=1/8,1/2\), the original row
has its ordinary rate \(T_F(c;x,z)=\Re F(c,a,q)\).
The new rate is exactly
\(\mathcal T_\eta(c;x,z)=T_F(c;x,z)+\Re H(q)\).
Consequently
\[
 \mathcal T_\eta(c;x,z)-B_{\rm F}
   =T_F(c;x,z)-B_F
       +\Re\{H(q)-H(q_*)-H'(q_*)\Delta z\}.
 \tag{29}
\]
This is an identity of the original source rates. No finite
Fourier polynomial is divided out.

The [left-cut source theorem](research_mixed_four_left_cut_support.md),
Theorem 1, and the
[half-row source theorem](research_mixed_half_row_support_completion.md),
equation (3), each give
\[
                    T_F(c;x,z)-B_F<-\frac1{2000}
 \tag{30}
\]
on their complete original reference families and all horizontal
targets in \([.22,.45]^2\). Their hypotheses hold here by (25)
and the correlated domain theorem. Combining (22), (29) and (30)
proves
\[
 \boxed{\quad
   \mathcal T_\eta(c;x,z)
      <\mathcal L_\eta(x,z)-\frac1{35000},
          \qquad c=1/8,1/2 .
 \quad}
 \tag{31}
\]
The arithmetic is \(1/2000-33/70000=1/35000\).
This retains the stronger old \(\kappa\), so the same margin holds
against the weaker plane with coefficient \(\kappa/2\) in
equation (20) of the bare inner-contour theorem.

Thus two of its three real-row comparisons are settled, with
a uniform strict margin and the original source normalization.
The main sheet and inner aliases were already bounded there.
The real last row \(c=1\) is not covered by (30), and this
note claims no lower bound for the remaining outgoing finite sum.
