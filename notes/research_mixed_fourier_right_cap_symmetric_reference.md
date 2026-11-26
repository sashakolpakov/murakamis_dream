# An exact symmetric reference for the Fourier right cap

Research deduction, 7 November 2026. A simple symmetric solution of
the right-cap critical equations is exactly the already certified
alternating three/four reference. Its input, both ordinary legs,
logarithmic lifts, and source allocation are therefore admitted
without a new critical-point calculation.

The final section specifies one physical-face comparison at this
reference. It is not evaluated here, and no sign for that comparison
is claimed.

## 1. Exact identification with the original algebraic reference

Let \(\alpha\) be the original upper-half-plane root of
\[
 p(\alpha)=4\alpha^4-6\alpha^3+4\alpha^2-2\alpha+1=0,
 \tag{1}
\]
with the certified disk and marking in
[the three/four interface theorem](research_three_four_source_interface.md).
Retain
\[
 Y=(1+2\alpha-4\alpha^2)^{-1},\qquad
 U=1-2\alpha,\qquad c=Y^{-1}-1.
 \tag{2}
\]
The original reference notes define
\[
 z_3=-\frac{\Log U}{2\pi i},\qquad
 z_4=\frac{\Log(2Y/(1-Y))}{2\pi i}.
 \tag{3}
\]
The first logarithm is the original lower-left-quadrant mark;
the second is its specified upper-half-plane mark from the
[power-four packet](research_power_four_source_packet.md).
Since \(c/2\) lies in the lower-left quadrant,
\(\Log(2Y/(1-Y))=-\Log(c/2)\), with no added logarithmic period.

Define the proposed symmetric exponents
\[
 S_*=Q_*=\frac c2=\alpha U,\qquad
 A_*=\frac{1+S_*}{1-S_*+2S_*^2}.
 \tag{4}
\]
Then
\[
                         A_*=U.
 \tag{5}
\]
Indeed, with \(S_*=\alpha U\),
\[
 U(1-S_*+2S_*^2)-(1+S_*)
 =-\alpha(U^4-U^3+U^2+U+2)
 =-4\alpha p(\alpha)=0.
 \tag{6}
\]
Here \(U\ne0\) and \(|S_*|<1\), so (6) also proves that
the displayed denominator in (4) is nonzero.
Consequently the decoded variables are exactly
\[
                         a_*=z_3,\qquad s_*=q_*=z_4.
 \tag{7}
\]

The two original exponentiated critical equations are
\[
 (1-A_*S_*)(1-S_*Q_*)=A_*(1-S_*)^3,\qquad
 Q_*^2-(2+c-S_*)Q_*+c=0.
 \tag{8}
\]
The first follows directly from (4). At \(S_*=c/2\), the second
polynomial factors as
\[
             \zeta^2-(2+c/2)\zeta+c
                         =(\zeta-c/2)(\zeta-2).
 \tag{9}
\]
Thus \(Q_*\) is precisely the unique unit-disk root; the other
root is exactly 2. No independently chosen quadratic branch enters.
The auxiliary Fourier leg also agrees exactly:
\[
 \frac{1-YQ_*}{Y+(1-2Y)Q_*}
   =\frac{Y(1+Y)}{1-3Y+4Y^2}=A_*=U.
 \tag{10}
\]

## 2. Typed eligibility and the original zero logarithmic lifts

The old power-four source theorem explicitly certifies
\[
 .284<\Re z_4<.285,\qquad -.043<\Im z_4<-.042.
 \tag{11}
\]
The saved original power-three author record
[research-three-vertex-mixed-reference.json](../repro/results/research-three-vertex-mixed-reference.json),
SHA-256
be27579fe6329c85d9617d00a7299ef67d75d1342ad7b0af5b589838c82650f2,
contains the outward critical-index enclosure
\[
 [\,0.35358333296974490681658610\ \mathord\pm 4.98\,10^{-27}\,]
 +i[\, -0.01678382500516450003846251\
                                      \mathord\pm8.89\,10^{-27}\,].
 \tag{12}
\]
In particular
\[
                    z_3\in(.353,.354)+i(-.017,-.016).
 \tag{13}
\]
The record's writer SHA-256 is
a01c4b94fd9452f7c17693b58dbd23692a2c6cc4fb1d5eb963cea057ebbe142e;
its source is the original algebraic reference record
9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd.
Read-only inspection verified the unchanged writer and all seven
bound dependencies. No enclosure was reevaluated or replayed.

Use exactly the original typed domains
\[
 \begin{split}
 K_3={}&\{|a-(.35-.01i)|\le.083,\quad
             -.072\le\Im a\le.068,\quad
                         \Re a-3\Im a\le.608\},\\
 O_4={}&\{|z-(.30-.052i)|\le.060,\quad
                             -.102\le\Im z\le-.001\}.
 \end{split}
 \tag{14}
\]
Equations (11)--(13) place \(a_*\) strictly inside \(K_3\),
and \(s_*,q_*\) strictly inside \(O_4\).
For example the squared disk distances are respectively less than
\[
 .004^2+.007^2=.000065<.083^2,\qquad
 .016^2+.010^2=.000356<.060^2.
 \]
The slanted type-three side has
\(\Re a_*-3\Im a_*<.354+.051=.405<.608\).

The filtered-image zero-lift theorem in
[the correlated endpoint note](research_mixed_fourier_right_cap_correlated_endpoint.md),
Section 3, now applies to (8) with all its original hypotheses.
It proves that the unexponentiated derivatives of
\[
 F_0(s,a,q)=g(s+a)+g(s+q)-3g(s)-g(a)-g(q)
                                  +2\pi ias+\ell_q(x_0)
 \tag{15}
\]
vanish in \(s,q\) at (7). Thus this is the original canonical
last-four branch for the admitted incoming type-three leg \(a_*\).
It is the same calibrated alternating anchor already used in the
annulus proof, not a new family obtained by selecting polynomial roots.

This statement concerns the complete canonical source domain.
It does not assert that the last incoming leg of a specified finite
prefix equals the periodic value \(z_3\).

## 3. A fixed physical-face diagnostic, still unevaluated

Let \(u=\Re z_4\), \(d=11/50\), and retain the actual incoming
height by taking \(a=a_*=z_3\). The point
\[
                         (s,q)=(u,d)
 \tag{16}
\]
belongs to the lower outgoing face of the exact low-index rectangle.
Every factorial argument of (15) is in its original regular strip,
and the original physical cardinal phase is regular since \(|Y|<1\).
The incoming target has no displacement from its reference, so its
original supporting plane is exactly
\(B_0(\Re a_*)=\Re F_0(z_4,z_3,z_4)\).

The one fixed comparison is
\[
 \mathfrak D=\Re\{F_0(u,z_3,d)-F_0(z_4,z_3,z_4)\}.
 \tag{17}
\]
Equivalently, before taking the real part its exact expression is
\[
 \begin{split}
 &g(z_3+u)-g(z_3+z_4)+g(u+d)-g(2z_4)
          -3g(u)+4g(z_4)-g(d)\\
 &\hspace{20mm}
       +2\pi iz_3(u-z_4)+\ell_d(x_0)-\ell_{z_4}(x_0).
 \end{split}
 \tag{18}
\]
The incoming \(g(z_3)\) cancels exactly; no favorable action constant
or tangent correction is substituted. This is the unselected
type-three incoming allocation, so no outgoing halfweight or
additional Fourier factor is present.

A positive value of (17) would disprove the uniform raw four-face
criterion on its stated canonical domain. It would not contradict
the actual coherently summed right cap or the already paid high-index
group. No sign of (17), or bound for the full low-index source, is
asserted in this note.
