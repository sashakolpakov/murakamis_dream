# A narrower real strip for the actual Fourier outgoing leg

Research deduction, 7 November 2026. The correlated last ordinary
four equation forces its outgoing leg into the strict strip
\(1/4<\Re q_*<1/3\). The proof uses only the original parameter
bounds and the typed own-leg constraints. It performs no root,
source or numerical evaluation.

## 1. The actual equation and elementary parameter bounds

Use the actual family of the
[correlated endpoint theorem](research_mixed_fourier_right_cap_correlated_endpoint.md):
\[
 a\in K_3\cup K_4,\quad s_*,q_*\in O_4,\quad
 Y=\rho e^{i\phi}=e^{2\pi ix_0},\quad
 S=e^{-2\pi is_*},\quad Q=e^{-2\pi iq_*}.
 \tag{1}
\]
The incoming type may be either three or four. This is the last
ordinary four family; a private first-cap leg is not substituted
for \(s_*\).

Write
\[
 Q=R(\cos\theta-i\sin\theta),\quad
 \theta=2\pi\Re q_*,\quad R=e^{2\pi\Im q_*},\quad
 \alpha=1-\frac{\cos\phi}{\rho},\quad d=\frac{\sin\phi}{\rho}.
 \tag{2}
\]
The original typed filters give
\[
 0<R<1,\quad .48\pi\le\theta\le.72\pi,\quad
 |S|<1,\quad \Im S<-2/5.
 \tag{3}
\]
The last strict bound is the analytic own-leg inequality in
Section 2 of the
[annulus protocol](research_mixed_fourier_right_cap_annulus_protocol.md),
derived before its saved-data test.

The [allocation-curvature proof](research_mixed_fourier_allocation_curvature.md)
gives \(121/200<\rho<123/200\).
The original angle interval also implies
\[
 \frac25<\cos\phi<\frac{41}{100},\qquad
 \frac9{10}<\sin\phi<\frac{457}{500}.
 \tag{4}
\]
Here are exact elementary witnesses for the sharpened upper bounds.
From \(157/50<\pi<22/7\) and
\(.18299<\Re x_0<.18301\),
\[
             \frac{1149}{1000}<\phi<\frac{1151}{1000}.
 \tag{5}
\]
Cosine is decreasing and sine increasing on this interval.
Their alternating Taylor bounds give the rational comparisons
\[
 \begin{split}
 1-\frac{t^2}{2}+\frac{t^4}{24}
       -\frac{t^6}{720}+\frac{t^8}{40320}
       &<\frac{41}{100},\qquad t=\frac{1149}{1000},\\
 u-\frac{u^3}{6}+\frac{u^5}{120}
       &<\frac{457}{500},\qquad u=\frac{1151}{1000}.
 \end{split}
 \tag{6}
\]
Thus
\[
 \frac{39}{121}<\alpha<\frac{43}{123},\qquad
 \frac{60}{41}<d<\frac{914}{605}.
 \tag{7}
\]
All comparisons concern the full original parameter enclosure.

## 2. The two strict real barriers

The exact outgoing equation gives
\[
 S=1+Y^{-1}-Q-\frac{Y^{-1}-1}{Q}.
 \tag{8}
\]
Since \(Y^{-1}-1=-\alpha-id\), taking imaginary parts yields
\[
 \Im S=-d+R\sin\theta+
                  \frac{\alpha\sin\theta+d\cos\theta}{R}.
 \tag{9}
\]

**Theorem.** Every reference (1) satisfies
\[
                         \frac14<\Re q_*<\frac13.
 \tag{10}
\]

*Proof of the lower barrier.* Suppose \(\theta\le\pi/2\).
Then \(\cos\theta\ge0\), and the lower end of (3) gives
\(\sin\theta\ge\cos(\pi/50)>99/100\).
The arithmetic-geometric mean inequality in (9) implies
\[
 \Im S\ge-d+2\sin\theta\sqrt{\alpha}
 >-\frac{914}{605}+\frac{99\sqrt{39}}{550}>-\frac25.
 \tag{11}
\]
For the last comparison, both sides of
\(1089\sqrt{39}>6720\) are positive and
\[
 39\cdot1089^2=46250919>45158400=6720^2.
 \tag{12}
\]
This contradicts (3), proving \(\theta>\pi/2\).

*Proof of the upper barrier.* Suppose \(\theta\ge2\pi/3\).
Throughout the remaining old range in (3),
\(\sin\theta\le\sqrt3/2<7/8\) and
\(\cos\theta\le-1/2\). In particular (7) gives
\[
 \alpha\sin\theta+d\cos\theta
 <\frac{43}{123}\frac78-\frac{30}{41}<0.
 \tag{13}
\]
Since \(R<1\), the positive term \(R\sin\theta\)
is at most \(\sin\theta\), while division by \(R\) makes
the negative numerator in (13) smaller. Hence (9) implies
\[
 \begin{split}
 \Im S
 &<(1+\alpha)\sin\theta-d(1-\cos\theta)\\
 &<\frac{166}{123}\frac78-\frac{60}{41}\frac32
   =-\frac{499}{492}<-1.
 \end{split}
 \tag{14}
\]
This contradicts \(|S|<1\). Thus \(\theta<2\pi/3\),
which proves (10). \(\square\)

The same calculation retains useful correlation with the height.
On the whole actual family, (3) and (9) imply
\[
 \begin{split}
 R^2\sin\theta-(d-2/5)R
                +\alpha\sin\theta+d\cos\theta&<0,\\
 R^2\sin\theta-(d-1)R
                +\alpha\sin\theta+d\cos\theta&>0.
 \end{split}
 \tag{15}
\]
These are necessary joint radial/angular inequalities; they do not
replace the original typed filters or assert that arbitrary points
between their boundaries are realized.

## 3. Consequence for the completed critical-height source

For the original plane of the
[completed bare inner-source theorem](research_mixed_fourier_right_cap_bare_inner_completion.md),
write
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                         -\kappa(x-\Re a_*)^2,
 \qquad \kappa=1/2500000.
\]
The two outgoing plateau edges on their negative critical-height
line consequently have the sharper uniform losses
\[
 \begin{split}
 \mathcal L_\eta(x,11/50)&<
                     B_\eta(x)-\frac{9\kappa}{10000},\\
 \mathcal L_\eta(x,9/20)&<
                     B_\eta(x)-\frac{49\kappa}{3600}.
 \end{split}
 \tag{16}
\]
This follows from the exact distances
\(1/4-11/50=3/100\) and \(9/20-1/3=7/60\).
It strengthens a bound for the entire coherent inner factor, with
the same finite prefactors and normalization, on that height line.

The real physical outgoing faces have height zero. Their change
in the action from the negative critical-height line is not
discarded or bounded by (16). Thus this result does not pay the
remaining real-height faces or physical wedge of the
[outer-contour theorem](research_mixed_fourier_right_cap_outer_contour.md).
