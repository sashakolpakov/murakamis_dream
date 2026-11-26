# A certified analytic input region for the twice-crossed conditional root

Research deduction, 7 November 2026. The exact cotangent criterion
proves existence of the original type-three conditional critical point
for every actual type-three incoming reference of the Fourier boundary.
The argument uses elementary rational bounds and retains the fixed
original Fourier parameter. No root or source is evaluated.

The same result covers a specified subdomain of type-four references.
The older conditioned \(44\) and \(444\) bounds do not, by themselves,
put the final incoming type-four leg in that subdomain. The distinction
between an interior ordinary window and the actual Fourier boundary is
retained below. No finite-source dominance is asserted.

## 1. The original parameter and a linear sufficient condition

Keep the original alternating output
\[
 y=x_0=\xi+i\upsilon,\qquad
 .18299<\xi<.18301,\qquad .07871<\upsilon<.07873,
 \tag{1}
\]
with the lift and parameter bounds of
[the Fourier allocation theorem](research_mixed_fourier_allocation_curvature.md).
For the actual additive incoming argument \(a\), write
\[
 P=\cot(\pi a)=p+i\alpha,\qquad
 Q=\cot(\pi y)=q+i\beta .
 \tag{2}
\]
These are the two arguments of the type-three polynomial in
[the full negative-crossing identity](research_mixed_fourier_negative_crossing_full_sources.md),
equation (14). In particular the second argument is \(y\), not
\(-y\), \(\bar y\), or an independently chosen ordinary external leg.

By [the exact root criterion](research_mixed_three_conditional_root_criterion.md),
the relevant real expression is
\[
 \mathcal B=p^2+q^2-(p+q)(\alpha q-\beta p).
 \tag{3}
\]
For \(p,q>0\), put \(t=p/q\). Then
\[
 \mathcal B>0
 \quad\Longleftrightarrow\quad
 \alpha<h_\beta(t),\qquad
 h_\beta(t)=(1+\beta)t-1+\frac2{1+t}.
 \tag{4}
\]
This function is strictly convex on \(t>0\).
Its tangent at \(t=2/3\) is
\[
 h_\beta(t)\ge\frac{17}{25}
                         +\left(\beta+\frac7{25}\right)t.
 \tag{5}
\]
Consequently a strict upper bound for
\(\alpha-(\beta+7/25)p/q\) below \(17/25\) is sufficient.
No sign of a conditional Hessian is needed for this implication.

We shall use the following bounds for the one fixed output:
\[
                 q>\frac{127}{100},\qquad
                        -\frac{73}{100}<\beta<0.
 \tag{6}
\]
Here are elementary witnesses, to make (6) independent of a new
cotangent evaluation. Put \(\phi=2\pi\xi\), \(T=2\pi\upsilon\).
Using \(157/50<\pi<22/7\), (1) gives
\[
 \frac{1149}{1000}<\phi<\frac{719}{625},\qquad
                     \frac{49}{100}<T<\frac{99}{200}.
 \tag{7}
\]
The alternating sine and cosine polynomials give
\[
 \sin\phi>\frac{114}{125},\qquad
           \frac{51}{125}<\cos\phi<\frac{41}{100}.
 \tag{8}
\]
For the first inequality use
\(z-z^3/6+z^5/120-z^7/5040\) at \(z=1149/1000\).
For the lower cosine bound use
\(1-z^2/2+z^4/24-z^6/720\) at \(z=719/625\);
for the upper bound use the same polynomial plus \(z^8/40320\)
at \(z=1149/1000\). These are strict rational comparisons
with the three constants in (8).

The positive series and their successive-term ratios give
\[
 \cosh T
 \le 1+\frac{T^2}{2(1-T^2/12)}
 <\frac{563}{500},\qquad
 \sinh T
 \le T+\frac{T^3}{6(1-T^2/20)}
 <\frac{129}{250}.
 \tag{9}
\]
For the strict comparisons substitute \(99/200\).
Also \(\cosh T>1+(49/100)^2/2=22401/20000\).
Since
\[
 q=\frac{\sin\phi}{\cosh T-\cos\phi},\qquad
 -\beta=\frac{\sinh T}{\cosh T-\cos\phi},
 \tag{10}
\]
we obtain
\[
 q>\frac{114/125}{563/500-51/125}
       =\frac{456}{359}>\frac{127}{100},\qquad
 -\beta<\frac{129/250}{22401/20000-41/100}
       =\frac{10320}{14201}<\frac{73}{100}.
 \tag{11}
\]
The denominator in (10) is positive and \(\sinh T>0\).
This proves (6).

## 2. A whole closed incoming rectangle

Define
\[
 \mathcal A=
 \left[\frac{267}{1000},\frac{433}{1000}\right]
       +i\left[-\frac9{125},\frac{17}{250}\right].
 \tag{12}
\]

**Theorem 1.** For every \(a\in\mathcal A\), the cotangents (2)
satisfy
\[
 p,q>0,\qquad |\alpha+\beta|<\frac{123}{100}<2,\qquad
                         \mathcal B>\frac1{400}.
 \tag{13}
\]
Hence the original type-three equation at inputs \((a,x_0)\)
has exactly one simple root in the right cotangent half-plane,
and that root has the original zero logarithmic lift. It is
holomorphic on a neighborhood of this closed parameter family.

*Proof.* For \(a=x+ih\), write \(\theta=2\pi x\) and
\(t=2\pi|h|\). On (12), \(\pi/2<\theta<\pi\), and
\[
 p=\frac{\sin\theta}{\cosh t-\cos\theta}>0,\qquad
 |\alpha|=\frac{\sinh t}{\cosh t-\cos\theta}.
 \tag{14}
\]
Replacing \(h\) by \(-|h|\) leaves \(p\) unchanged and can
only increase \(\alpha\). Thus it is enough to bound
\[
 L(\theta,t)=
 \frac{\sinh t+k\sin\theta}{\cosh t-\cos\theta},
 \qquad k=\frac{45}{127},\quad
             0\le t\le\frac{18\pi}{125}.
 \tag{15}
\]
Both terms in its numerator, after division by the denominator,
decrease with \(\theta\): their derivatives have numerators
\(-\sinh t\sin\theta\) and \(\cosh t\cos\theta-1\).
Moreover
\[
 \partial_t L=
 \frac{1-\cosh t\cos\theta-k\sinh t\sin\theta}
      {(\cosh t-\cos\theta)^2}>0.
 \tag{16}
\]
Indeed \(\cos\theta<0\) and the elementary bound below gives
\(\sinh t<2341/5000<1/2\), whereas \(k<1\).
The maximum of (15) is therefore at
\[
                     a_0=\frac{267}{1000}-\frac9{125}i.
 \tag{17}
\]
This is a containing-domain corner, not an independently selected
actual reference.

For completeness put
\(\delta=17\pi/500\) and \(t_0=18\pi/125\).
At (17), \(\sin\theta=\cos\delta\) and
\(\cos\theta=-\sin\delta\). The following elementary estimates suffice:
\[
 \cos\delta<\frac{1243}{1250},\qquad
 \cosh t_0+\sin\delta>\frac{121}{100},\qquad
                         \sinh t_0<\frac{2341}{5000}.
 \tag{18}
\]
Here
\[
 \frac{2669}{25000}<\delta<\frac{187}{1750},\qquad
 \frac{2826}{6250}<t_0<\frac{396}{875}.
 \tag{19}
\]
For the first inequality of (18), use
\[
 1-\frac{(2669/25000)^2}{2}
       +\frac{(187/1750)^4}{24}<\frac{1243}{1250}.
 \]
For the second, use
\[
 1+\frac{(2826/6250)^2}{2}
       +\frac{(2826/6250)^4}{24}
       +\frac{2669}{25000}-\frac{(187/1750)^3}{6}
                                      >\frac{121}{100}.
 \]
For the third, use the sinh upper function in (9) at \(396/875\):
\[
 \frac{396}{875}
 +\frac{(396/875)^3}{6[1-(396/875)^2/20]}
                                      <\frac{2341}{5000}.
 \]
All denominators are positive, and all three displayed comparisons
are rational.
Equations (14), (18) now give at (17)
\[
          p<\frac{411}{500},\qquad
                         \alpha<\frac{387}{1000}.
 \tag{20}
\]
For example their intermediate upper bounds are
\(2486/3025<411/500\) and
\(2341/6050<387/1000\).
Combining (15)--(20), throughout (12),
\[
 \alpha+\frac{45}{127}p
 <\frac{387}{1000}+\frac{45}{127}\frac{411}{500}
 =\frac{17}{25}-\frac{221}{127000}.
 \tag{21}
\]

From (6),
\[
       -\frac{\beta+7/25}{q}<\frac{45}{127}.
 \tag{22}
\]
If its numerator is nonpositive this is immediate; otherwise use
\(-\beta-7/25<45/100\) and \(q>127/100\).
Equations (5), (21)--(22) imply
\[
 h_\beta(p/q)-\alpha>\frac{221}{127000}.
 \]
The exact identity
\(\mathcal B=q(p+q)[h_\beta(p/q)-\alpha]\) then gives
\[
 \mathcal B>
 \frac{221}{127000}\left(\frac{127}{100}\right)^2
       =\frac{28067}{10000000}>\frac1{400}.
 \tag{23}
\]
Finally \(\cos\theta<0\), (14) and (18) imply
\(|\alpha|<1/2\); with (6) this gives the strip condition in
(13). The exact root theorem proves the stated existence,
uniqueness, simplicity and original lift. Compactness and the
strict inequalities give a neighborhood of the closed family.
\(\square\)

## 3. What the actual reference theorems supply

Every actual type-three incoming reference of the Fourier cap lies
in (12). An ordinary incoming leg belongs to
\[
 O_3=P_3\cap\{-.065\le\Im a\le.068\},
 \qquad P_3=\{|a-(.35-.01i)|\le.083\};
 \]
the real range of this disk is \([.267,.433]\).
The attached first-cap type-three leg instead has
real range \([.278,.391]\) and heights \([-.072,.021]\).
These are the two actual roles in
[the ordinary/attached domain theorem](research_mixed_actual_last_row_reference_domains.md),
and [Fourier-ended inheritance](research_mixed_fourier_ended_boundary_windows.md),
Section 2, identifies the same original maps at the Fourier end.
In particular the prepared word \(34\) uses the attached case.
Theorem 1 therefore proves the transformed original critical point
for every such actual type-three input, without replacing its
correlations by a new root or reference.

For type four, Theorem 1 applies whenever the actual incoming leg
has additionally been proved to lie in (12). This includes the
refined rectangle
\[
               (.27,.33)+i(-.057,-.02)
 \tag{24}
\]
and hence the more restrictive oriented \(44\) and \(444\)
subfamilies **where their original window hypotheses hold**.
Their bounds are
\[
 -.056<\Im t_j<-.048\quad(44),\qquad
 -.056<\Im t_j<-.053\quad(444),
 \tag{25}
\]
with \(t_j\) the first right leg in the ordered \(44\) pair
and the middle right leg in the \(444\) triple, respectively.
The orientation and image identification are those of
[open-window inheritance](research_mixed_open_word_window_inheritance.md),
Theorem 1.

These interior bounds do not automatically apply to the actual
last incoming leg \(t_{m-1}\). The \(44/444\) proofs use a
five-vertex ordinary window centered at that leg, with both
external inputs in the final rectangles. The Fourier-ended
theorem supplies the actual last exterior leg
\(\beta_K(t_m)\in D_3\), and subsequently \(K_3\), with its
original zero lift. It does not manufacture the extra ordinary
vertices needed by the centered five-window proof, nor does it
put that exterior leg in the smaller final rectangle.
Its stated conservative inheritance ranges remain the ones to use.

Thus (13) has not been established here for every actual
type-four terminal input. The remaining family retains
\[
 a=t_{m-1},\quad u=s_{m-1},\quad
 (s_m,t_m)\ \hbox{the original Fourier pair},
 \]
and all original equations, including
\[
 g'(u+a)+g'(s_m+a)-3g'(a)+2\pi i s_m=0.
 \tag{26}
\]
For a one-letter prefix \(4\) there is no such retained incoming
coordinate; for a first attached type-four leg the endpoint
equations, rather than an invented ordinary equation, must also
be retained. No assertion on an independent whole \(O_4\) box
is substituted for these correlations.

This deduction gives a critical point and its original lift only.
Even on (12), the finite \(C_{0,N}(X,Y^{-1})\) polynomial still
requires its own full endpoint, alias and contour comparisons
before that critical point can be promoted to a contributing
nonzero source packet. The incoming Fourier allocation and the
explicit scalar in the twice-crossed identity are unchanged.
