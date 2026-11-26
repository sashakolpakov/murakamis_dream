# A source-controlled positive path through the wider inner saddle

Private written finite-source deduction, 9 November 2026. The positive
first-angle contour can be routed through the original selected
saddle and then toward the right face, with the geometric sector
never exceeding its stationary action. The complete endpoint sector
is paid on every part of this contour at height at most \(7/10\).
The part above that height is retained as an explicit unpaid
maximum.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation or frozen-source edit is used.

## 1. Original family and two Hessian signs

Use the wider branch and the outer hyperbola
\[
 u=\beta-iK,\quad K=\frac{\pi K_g}{2\beta},\quad
 \pi/2\le\beta\le2\pi/3,\qquad
 t_*(u)=a_*-iH_*,\quad s(u)=\Re S_3(0,u).
 \tag{1}
\]
The wider cubic proof retains the original charge and gives
\[
 0<a_*<2\pi/3,\qquad1/10<H_*<1,\qquad a_*>1.
 \tag{2}
\]
For the last assertion,
\(\cos(a_*/2)=\Re c/\cosh(H_*/2)<7/8<\cos(1/2)\).
The whole family (1) is compact, with \(K>17/40\).

For any positive first angle in
\[
 t=a-iH,\qquad0\le a\le2\pi/3,\quad1/10\le H\le1,
 \tag{3}
\]
put \(c_t=\cos(t/2)\), \(C=\cos(u/2)\),
\(A=c_t^2,B=C^2,D=A+B-AB\).
The original phase and its derivatives are
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it,
 \quad
 \Phi_{tt}=-\frac1{2\pi}
       \left\{\frac1{c_t}+\frac C{c_t\sqrt D}\right\}
                                    +\frac{3i}{2\pi}.
 \tag{4}
\]
The positive wider-edge source calibrates this same branch,
including \(a=0\) by outgoing strictness.

There is a useful stronger ratio estimate. Since
\[
 |\cos u|^2=\cos^2\beta+\sinh^2K
       <1/4+69/100=47/50<1,
 \tag{5}
\]
one has \(\Re B-|B|^2>0\). Here the already proved
\(\cosh K<13/10\) gives \(\sinh^2K<69/100\).
Also \(\Re A>0\),
\(\Im A\ge0,\Im B>0\). The exact identity
\[
 |D|^2-|B|^2
 =2\{\Re A(\Re B-|B|^2)+\Im A\,\Im B\}
                         +|A|^2|1-B|^2>0
 \tag{6}
\]
implies
\[
            \left|\frac C{c_t\sqrt D}\right|
                  <\frac1{\sqrt{|A|}}\le2.
 \tag{7}
\]
Here \(|A|=(\cosh H+\cos a)/2\ge1/4\).

The wider source has \(\Re D>0\), and
\[
 0\le\arg c_t<\pi/4,\quad0<\arg C<\pi/4,\quad
                         |\arg\sqrt D|<\pi/4 .
 \tag{8}
\]
Thus \(C/(c_t\sqrt D)\) has positive real part.
The original secant comparison on (3) gives
\(\Re(1/c_t)>7/8\).
For completeness, writing \(x=\cos(a/2)\in[1/2,1]\)
and \(s=\sinh(H/2)\), the real secant is
\(x\cosh(H/2)/(x^2+s^2)\).
It has only a maximum in the interior of the \(x\)-interval.
At \(x=1\) its value exceeds \(7/8\); at \(x=1/2\)
it exceeds \(98/109>7/8\), using \(s^2<15/49\).
Also \(\Im(1/c_t)\le0\).
Equations (4),(7)--(8) therefore prove uniformly
\[
                 \Re\Phi_{tt}<-1/(4\pi),\qquad
                 \Im\Phi_{tt}>1/(2\pi).
 \tag{9}
\]

## 2. A positive path that stays in the source rectangle

Write \(h_0=7/10\), \(A_0=2\pi/3\).
We define a left-to-right path \(\gamma_+(u)\) from
\(-i\max\{H_*,h_0\}\), through \(t_*(u)\), to the right
face \(A_0-iH_R\).

If \(H_*\ge h_0\), first follow the horizontal
\([0,a_*]-iH_*\). Then follow
\[
 t=t_*+(1+i)\sigma,\qquad
 0\le\sigma\le\sigma_R:=
                    \min\{H_*-h_0,A_0-a_*\}.
 \tag{10}
\]
If this diagonal reaches \(h_0\) before the right face,
continue horizontally to \(A_0-ih_0\).
Otherwise stop at the right face. In this case
\[
                  H_R=\max\{h_0,H_*+a_*-A_0\}.
 \tag{11}
\]
No assertion that the diagonal always reaches \(h_0\) is needed.

If \(H_*<h_0\), put \(\sigma_L=H_*-h_0<0\).
First follow the horizontal from \(-ih_0\) to
\(t_*+(1+i)\sigma_L\). Then follow the diagonal
with \(\sigma_L\le\sigma\le0\) to \(t_*\), and finally
the horizontal to \(A_0-iH_*\). Its left joining angle
is positive, since \(a_*>1\) and \(h_0-H_*<3/5\).
Here \(H_R=H_*\).
Both constructions stay entirely in (3).

The geometric rate \(R(t)=\Re\Phi(t,u)\) satisfies
\[
                         R(t)\le s(u)
                              \qquad(t\in\gamma_+(u)).
 \tag{12}
\]
Indeed on the critical-height horizontal,
integration of the first inequality in (9) gives
\[
 R(a-iH_*)\le s(u)-(a-a_*)^2/(8\pi).
 \tag{13}
\]
On the diagonal through the critical point,
\[
 \frac{d^2}{d\sigma^2}R(t_*+(1+i)\sigma)
            =-2\Im\Phi_{tt}<-1/\pi,\qquad R'(0)=0,
 \tag{14}
\]
so \(R\le s-\sigma^2/(2\pi)\).
Moreover
\[
 \frac d{d\sigma}\Re\Phi_t(t_*+(1+i)\sigma)
                  =\Re\Phi_{tt}-\Im\Phi_{tt}<-3/(4\pi).
 \tag{15}
\]
After a positive diagonal displacement its horizontal derivative
is negative; the following horizontal therefore decreases by
(9). After a negative displacement its horizontal derivative
is positive; the horizontal to its left lies below its value
at the joining point, again by (9).
This proves (12) in both cases.

There is a uniform strict geometric gap on portions a fixed
distance from \(t_*(u)\). This follows directly from
(13)--(15) on each of the finitely many pieces and compactness;
the two definitions agree when \(H_*=h_0\).
No finite Gaussian approximation is needed for this upper bound.

## 3. What the complete finite source proves on this path

Retain the exact two-short-edge current
\[
 \begin{gathered}
 g_N^{<<}(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)e^{3iNt^2/(4\pi)},\\
 W_N(t)=\frac{e^{-iNt}}{(1-(-1)^{N-1}e^{-iNt})^2},\qquad
 I_{+,N}(u)=-\frac{N^2C_{N,3}}{\pi i}
                              \int_{\gamma_+(u)}g_N^{<<}W_N\,dt .
 \end{gathered}
 \tag{16}
\]
Every edge row, both physical endpoint groups, all caps and both
aliases in its pointwise edge estimates remain. The first-short
slit theorem is eligible because \(\Re(-2\cos t)<2\) on (3).
The positive wider-edge theorem applies to the second factor;
its extension at \(a=0\) is the same outgoing-strictness
argument as in the signed source.

Define the literal endpoint rate
\[
 E(a,H;u)=\Re\psi(a-iH,0)+(H+K)/2+3aH/(2\pi)-H
 \tag{17}
\]
and, with the maximum over an empty set omitted, put
\[
 E_{\rm high}(u)=
     \max_{\substack{a-iH\in\gamma_+(u)\\H\ge h_0}}E(a,H;u).
 \tag{18}
\]
On all parts with \(H\le h_0\),
\[
                       E(a,H;u)<123/100+K/2.
 \tag{19}
\]
To check the uniformity in \(H\), the proof of the
endpoint-budget theorem gives
\[
 E(a,H;u)\le
 2b_2+\frac{H^2}{4\pi}-\frac{4a^2}{17\pi}
                   +\frac{3aH}{2\pi}-\frac H2+\frac K2.
 \tag{20}
\]
Its right side is convex in \(H\in[0,h_0]\).
At \(H=0\) it is at most \(2b_2+K/2<7/6+K/2\);
at \(H=h_0\) the proved bound is (19).
This proves (19) throughout the interval.

Combining (12),(17)--(19) with the complete pointwise source
and the full multiplier in (16) gives, for each fixed \(\tau>0\),
\[
 |I_{+,N}(u)|\le C_\tau\left[
      e^{N(s(u)+\tau)}
     +e^{N(123/100+K/2+\tau)}
     +e^{N(E_{\rm high}(u)+\tau)}\right].
 \tag{21}
\]
An empty high part contributes no last term.
This is also a bound for the sum of the absolute integrals.
All paths have bounded length and heights uniformly separated
from zero, so their original \(N^2C_{N,3}\), sine and full
double-pole denominator contribute only the stated rate and
polynomial factors.

On the outer hyperbola, the first term of (21) has the strict
attached geometric gap proved in the wider-phase theorem.
The second term has the endpoint gap proved in the
right endpoint-budget theorem. The last term has not been
bounded here. In particular the sufficient remaining inequality
on this positive path is
\[
             2E_{\rm high}(u)+(2\beta/\pi-1)K<M_g
 \tag{22}
\]
with a uniform margin.
No endpoint maximum is replaced by a geometric critical value.

The path also stops on the right face at height \(H_R\).
The further vertical/low/far first-angle currents still need
their source and attached comparisons. Thus (21) is a concrete
positive-current reduction, not a full inner packet or a bound
for the whole right outer connector.

## Frozen source bindings

- Wider cubic, original phase and hyperbola action comparison:
  e9eadfc87f49741345f33ac73f717a4e1698ccaca5c3ffb824d48bd0444a8cbb.
- Complete wider positive edge:
  f3f9cdca2307f100a5766638ae91e329be5c7f372ac9b303ede0a28c9953e22f.
- Signed-source boundary extension and original trace factor:
  dea764c87b923f51be906688369da2fed794d376cb11469522f98983559d63c8.
- First-short slit theorem:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Exact original cubic current and secant comparison:
  7ba93b34b12765ebdfec7853ffc1e7e77bc370e07770c9088f59e538785af908.
- Fixed-depth endpoint comparison:
  f6dafa452dab15d307b7d2aad771b66409356ecf20aa441da38c01f45315c6b3.
