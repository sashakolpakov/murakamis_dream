# The low geometric endpoint of the right closing path

Private phase deduction, 9 November 2026. A piecewise real cubic
barrier and the original secant primitive put the geometric action
at \(2\pi/3-i/1000\) below the actual closing action. Convexity
in the outgoing height joins this point to the decreasing
hyperbola. This does not estimate the finite inner source.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation or frozen-source edit is used.

## 1. Three real cubic barriers

Use the original branch \(c=p+iq=\cos(t_*(u)/2)\) and action
\(S=S_3(0,u)\) from the taller strip and the
[wider continuation](research_mixed_symmetric_closing_wider_phase_hyperbola.md).
For real \(u=\beta\in[0,2\pi/3]\), the real cubic equation gives
\[
 \cos(\beta/2)
   =p\{4p^2-12(q-1/3)^2-5/3\}
   \le p(4p^2-5/3).
 \tag{1}
\]
The last function increases for \(p\ge3/4\), as holds on this
original branch. Consequently
\[
 \begin{array}{c|c|c}
 \text{real interval}&\text{strict lower bound for }p
                    &p_0(4p_0^2-5/3)\\ \hline
 [0,2\pi/3]&19/25&22933/46875<1/2\\
 [0,\pi/2]&319/400&33585277/48000000<7/10<1/\sqrt2\\
 [0,1]&41/50&78638/93750<7/8<\cos(1/2).
 \end{array}
 \tag{2}
\]
All comparisons are at the displayed rational barriers; no
new root is selected. The last cosine inequality follows
from \(\cos x>1-x^2/2\) for \(0<x<\pi\).

Define the original real first-edge loss
\[
 L(a)=\frac1\pi\int_0^a
                       \operatorname{arsinh}(\tan(x/2))\,dx .
 \tag{3}
\]
For real \(\beta\), the real part of the principal outgoing
return is at least
\[
 \Re\operatorname{arsinh}(c\tan(\beta/2))
 \ge\operatorname{arsinh}(p\tan(\beta/2))
 \ge p\,\operatorname{arsinh}(\tan(\beta/2)).
 \tag{4}
\]
For the first inequality write the return as \(r+i\nu\):
its real argument equals \(\sinh r\cos\nu\le\sinh r\).
The second inequality is concavity of \(\operatorname{arsinh}\)
on the positive real line, with its value zero at the origin
and \(0<p<1\).

Since \(S'=-\operatorname{arsinh}(c\tan(u/2))/\pi\), (2)--(4)
give the complete normalized real-action loss
\[
 \begin{split}
 M_3-\Re S(2\pi/3)
 &>\frac{19}{25}L(2\pi/3)
            +\frac3{80}L(\pi/2)+\frac9{400}L(1)\\
 &>\frac{19}{25}L(2\pi/3)+\frac1{25}L(\pi/2).
 \end{split}
 \tag{5}
\]
The second step uses \(9L(1)>L(\pi/2)\).
Indeed \(L(1)>1/(4\pi)>7/88\), while
\[
 L(\pi/2)\le\sqrt2\,\pi/16<55/196,
 \tag{6}
\]
by \((\operatorname{arsinh}\tan(x/2))'=\tfrac12\sec(x/2)\)
and \(\sec(x/2)\le\sqrt2\) on that interval.
These two bounds imply the claimed strict comparison.

## 2. An exact unevaluated lower bound for the loss

The positive secant series gives
\[
 L(a)\ge\frac{a^2}{4\pi}
             +\frac{a^4}{192\pi}+\frac{a^6}{4608\pi}.
 \tag{7}
\]
This follows by integrating
\(\sec(x/2)\ge1+x^2/8+5x^4/384\) twice with the
normalization in (3).
Retain all three terms for \(a=2\pi/3\), and the first
two for \(a=\pi/2\). The last line of (5) exceeds
\[
 \frac{313\pi}{3600}
       +\frac{19\pi^3}{24300}
       +\frac{\pi^3}{76800}
       +\frac{19\pi^5}{1312200}>\frac3{10}.
 \tag{8}
\]
For a fully rational check, \(\pi>25/8\) implies
\(\pi^3>61/2\) and \(\pi^5>295\). The witnesses are
\(15625>15616\) and \(9765625>9666560\).
The four terms in (8) then exceed respectively
\[
 \frac{2717}{10000},\qquad
 \frac{119}{5000},\qquad
 \frac{39}{100000},\qquad
 \frac{427}{100000}.
 \tag{9}
\]
Their sum is \(30016/100000>3/10\).
For the comparisons in (9), the exact integer witnesses are
\[
 \begin{gathered}
 3130000>3129984,\qquad
 5795000>5783400,\qquad
 6100000>5990400,\qquad
 560500000>560309400 .
 \end{gathered}
 \tag{10}
\]

The adopted original complete-action upper bound is
\(M_3<1339/705\). Thus (5)--(10) give
\[
                  \Re S(2\pi/3)<451/282<8/5.
 \tag{11}
\]
The stronger constant \(451/282\) is retained below.

## 3. Convexity and the complete low-height phase comparison

Keep \(f=\operatorname{arsinh}(c\tan(u/2))\),
\(\Xi=2S+iu^2/\pi-iu\) and the derivative decomposition
from the wider continuation:
\[
 f'=L_0+E_0,\quad
 L_0=\frac{c}{2C\sqrt D},\quad
 |E_0/L_0|<39/200,\quad C=\cos(u/2).
 \tag{12}
\]
Here \(D=c^2+C^2-c^2C^2\) has positive real and imaginary parts,
\(|D-1|<18/25<\sqrt3/2\). Hence
\(0<\arg\sqrt D<\pi/6\).
On the entire wider rectangle,
\[
 0\le\arg C<7\sqrt3/20<49/80<5/8<\pi/5,\qquad
                   0<\arg c<\arctan(7/15)<\pi/6.
 \tag{13}
\]
Therefore
\[
 -11\pi/30<\arg L_0<\pi/6,\qquad
 \Re L_0>\tfrac14|L_0|.
 \tag{14}
\]
For the latter, \(11\pi/30<5\pi/12\) and
\(\cos(5\pi/12)=(\sqrt6-\sqrt2)/4>1/4\);
the other endpoint has the larger cosine.
Equations (12)--(14) imply
\[
 \Re f'>\frac{11}{200}|L_0|>0,\qquad
 \frac{\partial^2}{\partial K^2}\Re\Xi(\beta-iK)
                              =\frac{2}{\pi}\Re f'>0 .
 \tag{15}
\]

Let \(K_\ell=1/1000\). Since the return remains principal,
\(|\Im f|<\pi/2\), so changing the outgoing height from
zero to \(K_\ell\) changes \(2\Re S\) by at most \(K_\ell\).
At real angle \(2\pi/3\), the exact outer crossing and trace
charge contribute \(K_\ell/3\). Hence
\[
 \Re\Xi(2\pi/3-iK_\ell)
 <\frac{451}{141}+\frac1{750}<\frac{16}{5}
                                      <M_g-\frac1{100}.
 \tag{16}
\]
The middle inequality follows because
\(16/5-451/141=1/705>1/750\).
The last inequality is the adopted consequence
\(M_g>321/100\) of the horizontal maximum and taller action
floor.

The already proved hyperbola ends at \(2\pi/3-3iK_g/4\),
with phase below \(M_g-d^2/(8\pi)\),
where \(d=\pi/2-\beta_g>0\).
Convexity (15) therefore pays the whole upward vertical
\[
 2\pi/3-3iK_g/4\ \longrightarrow\ 2\pi/3-i/1000
 \tag{17}
\]
at geometric rate at most
\[
                 M_g-\min\{d^2/(8\pi),1/100\}.
 \tag{18}
\]
The original logarithmic lift and action constant are used
throughout. Equations (16)--(18) are only phase estimates.
They do not supply a finite inner bound at rate \(S(u)\),
an edge packet at outgoing height below \(1/10\), or the
remaining low/far outer source. Those estimates are separate.

## Frozen source bindings

- Original taller cubic and action:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Original wider cubic, derivative and decreasing hyperbola:
  e9eadfc87f49741345f33ac73f717a4e1698ccaca5c3ffb824d48bd0444a8cbb.
- Complete normalized action upper bound:
  8435798f58bbf1a11319a6abb4b61a91c092647f230b4e2f3b48769329ee20b2.
- Actual horizontal maximum:
  f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
