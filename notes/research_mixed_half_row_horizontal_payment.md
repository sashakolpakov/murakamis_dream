# Quantitative payment of the half-row vertical cost

Research deduction, 5 November 2026. A stronger joint horizontal
Hessian bound gives an explicit sufficient half-row comparison even
when the vertical sign condition fails. The comparison retains the
original reference and its two marginals. It does not assert that
every actual coupled reference satisfies the new sufficient condition.

## 1. A stronger joint bound on the actual index range

Use the original allocated phase
\[
 F(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi ias,
 \qquad \eta,\epsilon\in\{0,1\},
 \tag{1}
\]
with the primitive and original lifts of the
[half-row vertical comparison](research_mixed_half_row_vertical_comparison.md).
Consider the fixed complex product
\[
 \begin{split}
 \mathcal S_1&=[23/100,1/2]+i[-27/250,17/250],\\
 \mathcal P&=[11/50,9/20]+i[-3/25,3/25].
 \end{split}
 \tag{2}
\]
Every individual and shifted argument stays in the original regular
strip. Unlike a moving-root assertion, the following estimate concerns
the uneliminated phase on this explicit product.

**Lemma 1.** On (2),
\[
                         -\Re F''\succ\frac1{10}I_3.
 \tag{3}
\]

Put \(V(s,a)=g(s+a)-g(s)-g(a)\), and write
\(u=\Re\cot\pi s\), \(p=\Re\cot\pi a\),
\(C=\Re\cot\pi(s+a)\). Its negative real Hessian is
\[
 -\Re V''=\pi
       \begin{pmatrix}u-C&-C\\-C&p-C\end{pmatrix}.
 \tag{4}
\]
We prove the stronger pair estimate
\(-\Re V''\succ(\pi/28)I_2\). The same argument then
applies to \(V(s,b)\).

First suppose \(C>0\). Then
\(\Re s+\Re a<1/2\), so both real coordinates belong to
\([.22,.28]\). On this range the sine in the real cotangent
formula exceeds \(49/50\), its cosine exceeds \(-1/5\),
and \(\cosh(2\pi\Im s),\cosh(2\pi\Im a)<4/3\).
Consequently
\[
 u,p>\frac{49/50}{4/3+1/5}=\frac{147}{230}>\frac35,
 \qquad
 C\le\cot(.45\pi)=\tan(.05\pi)<\frac16.
 \tag{5}
\]
The matrix in (4) is a positive diagonal matrix minus
\(C(1,1)^T(1,1)\). Its least eigenvalue is therefore greater
than \(3/5-1/3=4/15>1/28\).

Next suppose \(C\le0\) and \(\Re s\le2/5\).
Here \(\sin(2\pi\Re s)>9/16\) and
\(\cosh(2\pi\Im s)-\cos(2\pi\Re s)<9/4\),
so \(u>1/4\). The old outer cotangent estimate gives
\(p>9/70>1/8\). The negative shift contributes a positive
semidefinite rank-one matrix, so (4) is greater than
\((\pi/8)I_2\).

Finally suppose \(2/5\le\Re s\le1/2\). Then \(u\ge0\),
the shifted real part belongs to \([.62,.95]\), and its
absolute height is at most \(.228\). Hence
\[
 -C>
 \frac{3/10}{9/4+1}=\frac6{65}>\frac1{12},
 \qquad p>\frac18.
 \tag{6}
\]
Thus the matrix in (4) is bounded below by
\[
 K_0=\begin{pmatrix}1/12&1/12\\1/12&1/12+1/8\end{pmatrix}.
 \tag{7}
\]
Its determinant is \(1/96\) and its trace is \(7/24\).
It is positive definite, and its least eigenvalue is strictly greater
than determinant divided by trace, namely \(1/28\). This proves
the pair estimate in every case, including \(\Re s=1/2\).

For completeness, the scalar bounds used here require no new
parameter check. The bounds
\(\cosh(.216\pi)<5/4\), \(\cosh(.24\pi)<4/3\), and
\(p>9/70\) are retained from the
[fixed-contour proof](research_mixed_horizontal_zero_mode_support.md).
On \([.22,.28]\),
\(\sin(2\pi x)\ge\cos(.06\pi)>49/50\) and
\(\cos(2\pi x)>-1/5\), using \(.06\pi<1/5\).
Also
\[
 \tan(\pi/20)
 <\frac{11/70}{1-(11/70)^2/2}
 =\frac{1540}{9679}<\frac16.
 \tag{8}
\]
On \([.23,.4]\), the smallest sine is \(\sin(\pi/5)\);
\(\sin(.6)>.6-.6^3/6>9/16\) proves the asserted lower
bound. On \([.62,.95]\), the smallest absolute sine is
\(\sin(\pi/10)>3/10\), for example by the cubic sine bound
at \(157/500<\pi/10\). Finally \(.456\pi<36/25\), and
the positive hyperbolic series gives
\[
 \cosh t\le1+\frac{t^2}{2}
       +\frac{t^4}{24(1-t^2/30)}<\frac94,
                    \qquad t=36/25.
 \tag{9}
\]
The geometric tail bound uses the successive even-power ratio at
most \(t^2/30\) after the fourth-power term.

Now decompose (1) as
\[
 F=V(s,a)+V(s,b)-\epsilon g(s)
             -\frac\eta2g(a)-\frac\epsilon2g(b)+2\pi ias.
 \tag{10}
\]
The two pair estimates give the lower matrix
\((\pi/28)\operatorname{diag}(2,1,1)\). The additional own
terms have nonnegative negative-real Hessian on (2), and the chirp
has zero real Hessian. Since \(\pi/28>1/10\), (3) follows.

## 2. The exact vertical cost with a quadratic credit

Fix an actual original reference \((s_0,a_0,b_0)\) covered by
(2), with \(F_s(s_0;a_0,b_0)=0\). The actual conditional
indices have real part at least \(.23\). For ordinary vertices this
follows from the original two-leg maps in
[the all-word localization theorem, Section 3](research_mixed_open_word_critical_localization.md#3-all-lengths-including-one-and-two),
whose typed disks lie in the
[box \(Q=[.23,.45]+i[-.12,.12]\)](research_mixed_open_word_hessian.md).
For terminal attached indices, the
[saved endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give real ranges \((.278,.391)\) for type three and
\((.246,.350)\) for type four, including the separate length-one
values where applicable. The upper half-index extension is used
only along the comparison segment.
Retain the notation \(M,p_a,p_b,d_a,d_b,y_0\) and the old
supporting plane \(B\) from the vertical comparison. Put
\[
 d_s=1/2-\Re s_0>0,\qquad
 D=d_s^2+d_a^2+d_b^2,\qquad
 \Theta_0=\Im F_s(1/2;a,b).
 \tag{11}
\]
The outer targets are still \(a=x+i\Im a_0\),
\(b=z+i\Im b_0\) with \(x,z\in[.22,.45]\).
Their heights have not been independently replaced.

By Lemma 1 and the original index equation,
\[
 \Re F(1/2+iy_0;a,b)
 \le M+p_ad_a+p_bd_b-\frac D{20}.
 \tag{12}
\]
For \(H(y)=\Re F(1/2+iy;a,b)\), the exact derivative at zero
is \(H'(0)=-\Theta_0\). Moreover
\[
 \begin{split}
 H''(y)
 &=-\Re F_{ss}(1/2+iy;a,b)\\
 &=\pi\Re\tan\pi(a+iy)+\pi\Re\tan\pi(b+iy)
 >\frac\pi6
 \end{split}
 \tag{13}
\]
throughout the segment joining zero to \(y_0\).
Indeed \(\Re\cot\pi(1/2+iy)=0\), while each shifted
cotangent is less than \(-1/12\) by (6). This also shows
directly why the vertical cost is independent of the own flag
\(\epsilon\).

The strong convexity inequality based at zero, valid for either sign
of \(y_0\), gives
\[
 H(y_0)\ge H(0)-y_0\Theta_0+\frac\pi{12}y_0^2.
 \tag{14}
\]
Combining (12)--(14) yields the following universal quantitative
comparison on this fixed-height family:
\[
 \boxed{\quad
 \mathcal R_\epsilon(1/2;a,b)
 \le M+p_ad_a+p_bd_b-\frac D{20}
       +y_0\Theta_0-\frac\pi{12}y_0^2.
 \quad}
 \tag{15}
\]
At \(y_0=0\), both vertical terms vanish. For nonzero \(y_0\)
the vertical inequality is strict; no distinction between the two
height signs or a new logarithmic branch is needed.

## 3. An explicit paid region beyond the sign test

Retain \(\mu=1/1250000\) in the original plane
\(B=M+p_ad_a+p_bd_b-\mu(d_a^2+d_b^2)/2\). Equation (15)
implies the exact sufficient condition
\[
 y_0\Theta_0-\frac\pi{12}y_0^2
 \le \frac{d_s^2}{20}
       +\left(\frac1{20}-\frac\mu2\right)(d_a^2+d_b^2)
 \quad\Longrightarrow\quad
 \mathcal R_\epsilon(1/2;a,b)\le B.
 \tag{16}
\]
A convenient stricter condition retaining an explicit reserve is
\[
 y_0\Theta_0-\frac\pi{12}y_0^2
       +\frac\mu2(d_a^2+d_b^2)\le\frac D{40}
 \quad\Longrightarrow\quad
 \mathcal R_\epsilon(1/2;a,b)\le B-\frac D{40}.
 \tag{17}
\]
These include the old sign region \(y_0\Theta_0\le0\).
They also include the explicit bad-sign band
\[
                 0<y_0\Theta_0\le\frac\pi{12}y_0^2,
 \tag{18}
\]
as well as additional positive vertical costs paid by the real
displacements in (16) or (17).

Everything in these conditions is evaluated at the same original
reference and the stated targets. In particular the lifted angle is
the explicit elementary quantity
\[
 \Theta_0=2\pi x
 +\arg(1+e^{2\pi\Im a_0-2\pi ix})
 +\arg(1+e^{2\pi\Im b_0-2\pi iz}),
 \qquad -2\pi z<\Theta_0<2\pi x.
 \tag{19}
\]
The [vertical comparison](research_mixed_half_row_vertical_comparison.md)
identifies its sign with the quadratic numerator \(q\); (15)
retains its magnitude instead of discarding the bad-sign region.

No uniform satisfaction of (16) over all coupled references and all
horizontal targets is claimed. The calibrated left and revived-last
rows also remain separate. The complete-contour theorem retains
every original row and current; this deduction supplies a stronger
half-row input on the explicit region above, with no new source
interpolation, root proposal, parameter cover, or transverse
derivative assertion.
