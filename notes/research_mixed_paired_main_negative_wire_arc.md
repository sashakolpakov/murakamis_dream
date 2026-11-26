# The main paired current on the negative wire arc

Research deduction, 7 November 2026. The main-main comparison for
the original paired Fourier kernel extends to the whole negative
part of its fixed shared-wire lift. The proof first restricts two
maximizing index coordinates using the original gradients, then
proves monotonicity in the shared wire. No analytic evaluation,
new root or parameter subdivision is used.

Use the phases, fixed original index heights and profile notation of
[the paired-period criterion](research_mixed_paired_fourier_period_criterion.md).
Write \(x_0=\xi+iY\), \(K=e^{2\pi ix_0}\), and
\[
 z=w+iY,\qquad \xi-\tfrac12\le w\le0,\qquad
 \rho=|K|,\quad R_3=e^{2\pi h_{3,0}},\quad R_4=e^{2\pi h_{4,0}}.
 \tag{1}
\]
The four index coordinates are \(u,v\) for type three and \(p,q\)
for type four. Their real cores are unchanged:
\[
 u_R,v_R\in[1/4,9/20],\qquad
 p_R,q_R\in[1/5,21/50].
 \tag{2}
\]
Only \(v,p\) meet the shared wire. Every index remains at its
original negative main height.

## 1. Elementary radius and angle bounds

The original certified reference enclosures give
\[
 \xi>181/1000,\quad \xi>9/50,\qquad
 \frac35<\rho<\frac58,\quad
 \frac89<R_3<\frac{10}{11},\quad
 \frac34<R_4<\frac45.
 \tag{3}
\]
These loose radius bounds follow from the already proved
\(.07871<Y<.07873\),
\(-.0169<h_{3,0}<-.0167\) and
\(-.0425<h_{4,0}<-.0423\), without evaluating a new exponential.
For clarity, use \(25/8<\pi<22/7\). Then
\(12/25<2\pi Y<1/2\);
\(e^{12/25}>8/5\) follows from its cubic positive Taylor sum,
and \(e^{1/2}<33/20<5/3\) from
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)},\qquad 0\le x<3.
 \tag{4}
\]
Likewise \(1/10<-2\pi h_{3,0}<1/9\), and
\(1/4<-2\pi h_{4,0}<2/7\).
Use \(e^{1/10}>11/10\), \(e^{1/9}<9/8\),
\(e^{1/4}>5/4\), and
\(e^{2/7}\le177/133<4/3\).
The bound at \(1/9\) follows from \(e^x<(1-x)^{-1}\);
the others follow from (4) or the first two positive terms.

The trigonometric bounds needed below are
\[
 \cos(13\pi/50)<7/10,\qquad
 \cos(9\pi/25)<9/20,\qquad
 \cos(2\pi/5)>3/10.
 \tag{5}
\]
For the first two, \(13\pi/50>13/16\) and
\(9\pi/25>9/8\), respectively, so
\(\cos x\le1-x^2/2+x^4/24\) at those lower arguments
proves the displayed upper bounds. The last follows from
\(\cos(2\pi/5)=(\sqrt5-1)/4\) and \(\sqrt5>11/5\).

## 2. Restricting the shared index maximizers

**Lemma 1.** For every wire in (1), the maximum defining the
main-main profile can be taken with
\[
                       v_R\le19/50,\qquad p_R\le19/50.
 \tag{6}
\]
This is a consequence of directional monotonicity on the whole
discarded index slices, not an additional source restriction.

*Proof.* Put \(U=e^{-2\pi iu}\), \(V=e^{-2\pi iv}\).
The original type-three derivative is
\[
 \Re(F_3)_v=\log\frac{|Z(1-UV)|}{|1-ZV|}.
 \tag{7}
\]
For \(v_R\ge19/50\), one has
\(63/100\le u_R+v_R\le9/10\).
Thus \(\cos(2\pi(u_R+v_R))>-7/10\), by (5), and
\[
 |Z(1-UV)|^2
 <\frac{25}{64}
       \left(1+\left(\frac{100}{121}\right)^2
                       +\frac75\frac{100}{121}\right)
 <\frac{259}{225}.
 \tag{8}
\]
On this same slice,
\[
 231/1000<1+w-v_R\le31/50.
 \tag{9}
\]
The cosine on that interval is less than \(1/8\):
at its left endpoint use
\(\cos(231\pi/500)=\sin(19\pi/500)<1/8\);
on its part beyond \(1/2\) the cosine is negative.
Since \(|ZV|>8/15\) and \(r^2-r/4\) is increasing there,
\[
 |1-ZV|^2>1+|ZV|^2-|ZV|/4
       >1+\frac{64}{225}-\frac2{15}=\frac{259}{225}.
 \tag{10}
\]
Equations (7)--(10) prove a strictly negative derivative.
Decreasing \(v_R\) to \(19/50\), whenever necessary, increases
the phase, for every other index in its original range.

For type four put \(P=e^{-2\pi ip}\), \(Q=e^{-2\pi iq}\).
The original derivative is
\[
 \Re(F_4)_p
      =\log\frac{|Z(1-PQ)|}{|1-P|\,|1-ZP|}.
 \tag{11}
\]
If \(p_R\ge19/50\), then \(\cos(2\pi p_R)<0\).
Also \(-3/4<w-p_R<-1/4\), so
\(\cos(2\pi(w-p_R))<0\). Hence
\[
 |Z(1-PQ)|^2
       <\frac{25}{64}(1+16/25)^2=\frac{1681}{1600},
 \qquad
 |1-P|^2|1-ZP|^2>1+R_4^2>\frac{25}{16}.
 \tag{12}
\]
The derivative in (11) is strictly negative too. This proves (6).
Both replacements are independent and preserve the full domain of
the two other indices. \(\square\)

## 3. Monotonicity of the coupled wire phase

**Lemma 2.** Suppose \(3/4<R<10/11\),
\(3/5<\rho<5/8\),
\(-16\pi/25\le\varphi\le0\), and
\(2\pi/5\le\vartheta\le19\pi/25\).
Then
\[
 |1-\rho R e^{i(\varphi-\vartheta)}|^2
                   -R^2|1-\rho e^{i\varphi}|^2>\frac6{121}.
 \tag{13}
\]

*Proof.* The difference is
\[
 1-R^2+2R\rho\{(R-\cos\vartheta)\cos\varphi
                                      -\sin\varphi\sin\vartheta\}.
 \tag{14}
\]
The braced expression is nonnegative for
\(-\pi/2\le\varphi\le0\), because \(R>\cos(2\pi/5)\).
For the remaining interval write \(a=-\varphi\). The expression
is \(R\cos a-\cos(a+\vartheta)\), where
\(\pi/2\le a\le16\pi/25\).
For fixed \(a\), the largest cosine over the stated
\(\vartheta\)-interval is at \(\vartheta=19\pi/25\).
Indeed its minimum, if interior, is at \(a+\vartheta=\pi\);
comparison of the two endpoint cosines uses
\(\sin(a+29\pi/50)<0\).
At that chosen endpoint,
\[
 \frac d{da}\{R\cos a-\cos(a+19\pi/25)\}
       =-R\sin a+\sin(a+19\pi/25)<0.
 \tag{15}
\]
Consequently the braced expression in (14) is bounded below by
\[
 -R\cos(9\pi/25)+\cos(2\pi/5)
       >-\frac{10}{11}\frac9{20}+\frac3{10}
       =-\frac6{55}.
 \tag{16}
\]
Insert this into (14) and use (3):
\[
 1-R^2-\frac{12R\rho}{55}
 >1-\left(\frac{10}{11}\right)^2
             -2\frac{10}{11}\frac58\frac6{55}
 =\frac6{121}.
 \tag{17}
\]
This proves the lemma. \(\square\)

**Theorem 3.** The main-main profile satisfies
\[
 \begin{split}
 &E_{3,00}(x_0,w+iY)+E_{4,00}(w+iY,x_0)\\
 &\quad\le E_{3,00}(x_0,iY)+E_{4,00}(iY,x_0)
       \le M_{34}-\frac{\mu}{2}\xi^2,
 \qquad \xi-\tfrac12\le w\le0,
 \end{split}
 \tag{18}
\]
where \(\mu>0\) is the same compact Hessian constant supplied by
Proposition 4 of the paired-period criterion.

*Proof.* After Lemma 1, both shared index real parts lie in
\([1/5,19/50]\). Put \(\varphi=2\pi w\), and let
\(\vartheta\) be \(2\pi\) times the corresponding index real part.
These variables meet Lemma 2, since \(\xi>9/50\).
For the same fixed remaining indices, the exact derivative of the
total real phase is
\[
 \begin{split}
 \partial_w\Re(\phi_3+\phi_4)
 &=-2\pi(h_{3,0}+h_{4,0})
       +\log\frac{|1-ZV|\,|1-ZP|}{|1-Z|^2}\\
 &=\log\frac{|1-ZV|}{R_3|1-Z|}
                 +\log\frac{|1-ZP|}{R_4|1-Z|}>0.
 \end{split}
 \tag{19}
\]
Lemma 2 proves each strict sign; the real logarithm needs no
additional lift. The derivative retains the original common-wire
chirp. Maximizing over the now fixed containing index domains
preserves monotonicity, so the first inequality in (18) follows.
At \(w=0\) enlarge those domains back to the original cores and
apply the already proved main-main estimate. This gives its second
inequality. \(\square\)

Together with Proposition 4, this controls the entire main-main
wire range \([\xi-1/2,1/5]\), apart from its intended local
stationary neighborhood where the nonzero packet is retained.
It does not establish the main-main comparison on the remaining
arc \((1/5,\xi+1/2]\), nor any nonmain or physical-tail product.
In particular it supplies no whole paired-period theorem yet.
All phases here use the same unwrapped wire lift as the criterion;
no periodic identification of individual index currents is made.
