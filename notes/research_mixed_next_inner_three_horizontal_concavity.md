# Full-box horizontal concavity of the original inner three-phase

Private phase theorem, 8 November 2026. The original reduced inner
phase is horizontally strictly concave on the entire independent
two-angle box used by the shortened-edge endpoint theorem. The
bound is quantitative and does not require the free-edge condition
\(|\cos(t/2)|<1\). It gives fixed horizontal cuts on both sides of
the actual critical family and a critical-height minimax identity.

This note proves statements about the original calibrated phase.
It does not extend a finite kernel packet throughout that box or
bound the angular endpoint connectors. No mathematical numerical
evaluation or frozen-source edit is used.

## 1. Original branch on the independent box

Let
\[
 t=a-iH,\quad u=b-iK,\qquad
 0\le a,b\le\pi/2,\quad0\le H\le1,\quad0\le K\le1/2.
\tag{1}
\]
The [shortened-edge endpoint theorem, Lemma 1](research_mixed_next_shortened_edge_endpoint_gap.md)
constructs the original holomorphic edge phase on a fixed
complex neighborhood of this entire box:
\[
\begin{split}
 \psi_t(t,u)
   &=-\pi^{-1}\operatorname{arsinh}
                         \{\tan(t/2)\cos(u/2)\},\\
 \psi(0,0)&=-8J(1/4).
\end{split}
\tag{2}
\]
The inverse hyperbolic sine is the principal return calibrated
to the original germ. Its proof checks both cuts, the closed
derivative form and the additive constant; no new phase is
defined by a stationary equation here.

Keep exactly
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it.
\tag{3}
\]
For actual
\[
 \mathcal U_+=\{b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},
\]
the [cubic continuation theorem](research_mixed_next_inner_three_cubic_continuation.md)
gives the original critical point
\[
 t_*(u)=a_*(u)-iH_*(u),\quad
 0<a_*(u)<\pi/2,\quad0<H_*(u)<1,\quad
 \Phi_t(t_*(u),u)=0 .
\tag{4}
\]
Its calibrated stationary action is
\[
                       S_3(0,u)=\Phi(t_*(u),u).
\tag{5}
\]
The family is compact, and every strict guard in (4) has
a uniform margin. The first edge is symmetric, so (3)
is the same phase as \(\psi(0,t)+\psi(t,u)\) plus the
original charge-one crossing term.

## 2. A positive-real Hessian decomposition

Put
\[
 c=\cos(t/2),\qquad C=\cos(u/2),\qquad
 A=c^2,\quad B=C^2,\qquad D=A+B-AB.
\tag{6}
\]
The following bounds hold throughout (1), including its boundary:
\[
\begin{split}
 |1-A|&=|\sin(t/2)|^2
        =\frac{\cosh H-\cos a}{2}<\frac45,\\
 |1-B|&=|\sin(u/2)|^2
        =\frac{\cosh K-\cos b}{2}<\frac47.
\end{split}
\tag{7}
\]
We used the written elementary bounds
\(\cosh1<8/5\) and \(\cosh(1/2)<8/7\), recorded with
their series witnesses in
[the upper terminal-region theorem, Sections 1 and 3](research_mixed_next_shortened_edge_upper_terminal_regions.md).
Since \(D=1-(1-A)(1-B)\), this proves
\[
                   \Re D>1-\frac{16}{35}=\frac{19}{35}.
\tag{8}
\]
In particular the principal square root \(\sqrt D\) is
holomorphic and nonzero on a fixed neighborhood of the box.

Both half-cosines lie strictly in the right half-plane, with
\[
        0\le\arg c<\pi/4,\qquad0\le\arg C<\pi/4,
              \qquad-\pi/4<\arg\sqrt D<\pi/4 .
\tag{9}
\]
For example
\[
 \frac{\Im c}{\Re c}
       =\tan(a/2)\tanh(H/2)<1,
\]
and the same formula applies to \(C\). Thus the exact product
argument in the second ratio below satisfies
\[
          -\pi/2<\arg\frac{C}{c\sqrt D}<\pi/2 .
\tag{10}
\]
There is no winding adjustment in this range.

Differentiating the original phase, with the square roots fixed
as in (2), gives
\[
 \boxed{\qquad
 \Phi_{tt}(t,u)
   =-\frac1{2\pi}\left\{\frac1c+\frac{C}{c\sqrt D}\right\}
                               +\frac{3i}{2\pi}.
 \qquad}
\tag{11}
\]
For clarity, the branch in this formula is the original one:
\[
 c\sqrt{1+C^2\tan^2(t/2)}
\]
is the nonzero holomorphic return from the derivative of the
principal inverse hyperbolic sine in (2). Its square is \(D\).
It equals the principal \(\sqrt D\) at \((t,u)=(0,0)\);
connectedness and (8) identify them on the whole box.
For \(u=0\), the corresponding derivative is \(1/(2c)\).
This proves (11), not merely its square.

The second ratio in (11) has strictly positive real part by
(10). The first ratio has an elementary quantitative bound:
\[
 |c|\le\cosh(H/2)<8/7,\qquad
 \Re(1/c)=\frac{\cos(\arg c)}{|c|}
           >\frac{7}{8\sqrt2}>\frac12.
\tag{12}
\]
The last strict inequality is equivalent to \(49>32\).
The crossing term in (11) is purely imaginary. Consequently
\[
 \boxed{\qquad
               \Re\Phi_{tt}(t,u)<-\frac1{4\pi}
                       \quad\hbox{throughout (1).}
 \qquad}
\tag{13}
\]
No condition on \(|A|\) or on the location of a finite-source
wire contour was used.

## 3. Actual horizontal action losses and fixed cuts

Fix \(u\in\mathcal U_+\), and write \(H_*=H_*(u)\),
\(a_*=a_*(u)\), and \(s(u)=\Re S_3(0,u)\).
On the whole fixed-height horizontal,
\[
 f_u(a)=\Re\Phi(a-iH_*,u),\qquad0\le a\le\pi/2,
\]
equations (4),(13) give \(f_u'(a_*)=0\) and
\(f_u''<-1/(4\pi)\). Integrating on either side of the
critical point yields
\[
 \boxed{\qquad
 \Re\Phi(a-iH_*,u)
       \le s(u)-\frac{(a-a_*)^2}{8\pi},
                      \qquad0\le a\le\pi/2 .
 \qquad}
\tag{14}
\]
The selected critical point is the unique maximum along
this entire horizontal. In particular the right-face comparison
available to a separate endpoint estimate is
\[
 s(u)\ge
 \Re\Phi(\pi/2-iH_*,u)
                     +\frac{(\pi/2-a_*)^2}{8\pi}.
\tag{15}
\]
All phase constants and the charge \(-it\) remain unchanged.

There are fixed cuts strictly bracketing the entire critical
family. One choice, requiring no evaluation of that family, is
\[
 a_L=\tfrac12\min_{\mathcal U_+}a_*(u),\qquad
 a_R=\tfrac12\{\pi/2+\max_{\mathcal U_+}a_*(u)\}.
\tag{16}
\]
Compactness and (4) give
\[
 0<a_L<\min a_*\le\max a_*<a_R<\pi/2 .
\tag{17}
\]
With the fixed positive number
\[
 \epsilon_{\rm hor}
     =\frac1{8\pi}
            \min\{a_L^2,(\pi/2-a_R)^2\},
\tag{18}
\]
equation (14) pays the two full horizontal outer pieces:
\[
 \Re\Phi(a-iH_*,u)\le s(u)-\epsilon_{\rm hor}
       \quad\left(0\le a\le a_L
                  \ \hbox{or}\ a_R\le a\le\pi/2\right).
\tag{19}
\]
Any \(O(N^{-1})\) displacement of these cuts has the same
phase gap with a slightly smaller constant. This statement
concerns the phase evaluated there, not an unproved finite
kernel symbol on those pieces.

## 4. The critical height is the minimax height

For fixed \(u\), let
\[
 U_u(a,H)=\Re\Phi(a-iH,u),\qquad
 M_u(H)=\max_{0\le a\le\pi/2}U_u(a,H).
\tag{20}
\]
Holomorphy and (13) imply
\[
                  \partial_H^2U_u=-\Re\Phi_{tt}>
                                    \frac1{4\pi}.
\tag{21}
\]
At \((a_*,H_*)\), both real first derivatives vanish by (4).
Keeping \(a=a_*\) and integrating (21) therefore gives
\[
 U_u(a_*,H)\ge s(u)+\frac{(H-H_*)^2}{8\pi}.
\tag{22}
\]
Together with (14), this proves the calibrated minimax statement
\[
 \boxed{\quad
 M_u(H_*)=s(u)=\min_{0\le H\le1}M_u(H),\qquad
 M_u(H)\ge s(u)+\frac{(H-H_*)^2}{8\pi}.
 \quad}
\tag{23}
\]
The maximizing coordinate at \(H_*\), and the minimizing
height in (23), are both unique. No assertion about the
maximizing coordinate at other heights is required.

## 5. Finite-source scope

The [complete shortened-edge packet](research_mixed_next_shortened_edge_upper_continuation.md)
now supplies the second edge on a fixed independent complex
neighborhood of the actual graph (4). The first edge has its
full packet there by the original free-pair theorem. These
facts license a local angular Gaussian; they do not automatically
license replacing the finite kernels by their phases on every
point used in (14) or (19).

In particular this note does not pay a connector from a
horizontal endpoint to its real sampling height. Vertical
convexity in (21) makes such a connector depend on both
endpoint values; the real value need not have a strict loss.
Nor are the negative-angular portion of the complete inner
trace, its odd central pole, its omitted derivative samples,
or its complete endpoint current estimated here.

The exact complete trace remains the one in
[the outer-fold and inner-source theorem](research_mixed_next_outer_fold_and_inner_source_lift.md).
Any full angular contour must retain that source and its
Fourier denominator. Equations (14)--(23) are rigorous original
phase comparisons for such a construction, not a full inner
trace or outer-transfer asymptotic.
