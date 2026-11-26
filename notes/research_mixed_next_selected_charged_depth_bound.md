# A sharper depth bound on the original selected charged curve

Private phase deduction, 9 November 2026. The selected curve throughout
the full charge interval satisfies \(-\Im u_\delta<2/5\). This improves
the containing depth used in its physical endpoint-sector rate. It is
not a finite-source estimate or a proof that this sector is below the
selected inner action.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Source and statement

Keep the original curve, cubic branch, and logarithmic equation from
[the full-interval theorem](research_mixed_next_selected_charged_curve_full_interval.md)
and [the actual right-edge guards](research_mixed_next_selected_right_edge_cut_guards.md):
\[
\begin{gathered}
u_\delta=\beta-iK,\qquad 0\le\delta\le1/2,\qquad
0<\beta<4/3,\quad0<K<1/2\quad(\delta>0),\\
c=\cos(t_*(u_\delta)/2)=p+iq,\qquad
f=\operatorname{arsinh}\{c\tan(u_\delta/2)\}
                       =i(3u_\delta/2-\pi\delta).
\end{gathered}
\tag{1}
\]
At zero charge, \(u_0=0\). All returns in (1) are principal on
the adopted original sheet.

**Theorem.** On this entire selected curve,
\[
                              0\le K<2/5.
\tag{2}
\]
The already proved guards also yield the auxiliary bound
\[
                       3/4<p<8/9,\qquad 1/4<q<1/3.
\tag{3}
\]

To prove (3), put \(C=\cos(u_\delta/2)\), \(x=2p\), and \(b=2q\).
The right-edge guard proves \(|\cos u_\delta|\le1\), and hence
\(|C|^2=|(1+\cos u_\delta)/2|\le1\), so \(\Re C\le1\).
The original cubic has the exact real equation
\[
             2\Re C=x(x^2-3b^2+4b-3).
\tag{4}
\]
The same guard proves \(1/2<b<2/3\), while \(x>3/2\).
As \(3b^2-4b\) decreases on this interval, (4) gives
\[
 x^2=\frac{2\Re C}{x}+3b^2-4b+3
                       <\frac43-\frac54+3=\frac{37}{12}.
\tag{5}
\]
Thus \(p^2<37/48<64/81\), proving the upper bound in (3).
The other three bounds are the original cubic and actual-sheet guards.

## 2. The original critical equation at a hypothetical larger depth

Suppose \(K\ge2/5\), and write
\[
w=c\tan(u_\delta/2),\qquad f=X+i\nu .
\]
The denominator \(D=\cos\beta+\cosh K\) is positive, and
\[
\Re w=\frac{p\sin\beta+q\sinh K}{D}>0,\qquad
\Im w=\frac{q\sin\beta-p\sinh K}{D}.
\tag{6}
\]
Using (3), \(\sinh K\ge K\), and the earlier
\(\cos\beta>7/30\), we get
\[
                    \Im w<
 \frac{1/3-(3/4)(2/5)}{1+7/30}=\frac1{37}.
\tag{7}
\]
This is only an upper bound; no unjustified absolute-value estimate
is assigned to a possibly negative imaginary part.

For the principal return, \(-\pi/2<\nu<\pi/2\) and
\(\Im w=\cosh X\sin\nu\). If \(\Im w<0\), then \(\nu<0\).
Otherwise
\[
 \nu\le\arcsin(1/37)
 \le\frac{1/37}{\sqrt{1-1/37^2}}<\frac1{36}.
\]
The imaginary part of the exact equation (1) consequently gives
\[
 \beta<\frac{\pi}{3}+\frac1{54}<\frac{16}{15}.
\tag{8}
\]
For the last strict comparison use \(\pi<22/7\):
\(22/21+1/54=403/378<16/15\).

The following written bounds will be used repeatedly:
\[
 \sinh K<\frac{12}{23},\qquad
 \cosh K\ge\frac{27}{25},\qquad
 \sin\beta<\frac9{10},\qquad
 \cos\beta>\frac{23}{50}.
\tag{9}
\]
The first follows from
\(\sinh K\le K/(1-K^2/6)\) and \(K<1/2\); the second
from \(K\ge2/5\). For the trigonometric bounds put \(a=16/15\).
The alternating sine series and \(a^3>6/5,\ a^5<3/2\) give
\[
 \sin a<a-\frac15+\frac1{80}=\frac{211}{240}<\frac9{10}.
\]
The alternating cosine series, \(a^4>1,\ a^6<6\), give
\[
 \cos a>1-\frac{128}{225}+\frac1{24}-\frac1{120}
             =\frac{209}{450}>\frac{23}{50}.
\]
Monotonicity on \(0<\beta<a<\pi/2\) proves the last two bounds.

## 3. Excluding the negative-imaginary alternative quantitatively

First, under the standing hypothesis \(K\ge2/5\), one must have
\[
                                 \beta>1.
\tag{10}
\]
If instead \(\beta\le1\), use \(\sin\beta<6/7\) and
\(\cos\beta>1/2\). The sine bound follows, for example, from
\(\sin1<1-1/6+1/120=101/120<6/7\).
Equations (3),(6),(9) imply
\[
\Re w<
 \frac{16/21+4/23}{79/50}
       =\frac{22600}{38157}<\frac35,
\qquad
\Im w>-\frac{32/69}{79/50}
       =-\frac{1600}{5451}>-\frac3{10}.
\tag{11}
\]
Together with (7), this gives \(|\Im w|<3/10\). Since
\(\Im w=\cosh X\sin\nu\), one has
\[
 \cos\nu\ge\sqrt{1-(\Im w)^2}>\frac{19}{20}.
\]
But \(\Re w=\sinh X\cos\nu\), so
\[
 \sinh X<\frac{12}{19}<\frac{159}{250}
                    <\sinh(3/5).
\tag{12}
\]
The last inequality is the first two positive hyperbolic-sine
series terms, \(\sinh(3/5)>3/5+(3/5)^3/6=159/250\).
Thus \(X<3/5\), contrary to the real part of (1),
\(X=3K/2\ge3/5\). This proves (10).

Now the imaginary part of (1), (10), \(\delta\le1/2\), and
\(\pi<22/7\) give
\[
 \nu=\frac{3\beta}{2}-\pi\delta>
             \frac32-\frac{\pi}{2}>-\frac1{14}.
\]
Combining this with the upper bound \(\nu<1/36\) proves
\(|\nu|<1/14\). Therefore the real part of the critical equation
forces
\[
\Re w=\sinh(3K/2)\cos\nu
 >\frac{159}{250}\left(1-\frac1{392}\right)
 =\frac{159\cdot391}{250\cdot392}>\frac{19}{30}.
\tag{13}
\]
The last rational inequality is
\(1\,865\,070>1\,862\,000\) after clearing the positive
denominators.

On the other hand (3),(6),(9) give
\[
 \Re w<
 \frac{(8/9)(9/10)+(1/3)(12/23)}
      {23/50+27/25}
 =\frac{1120}{1771}<\frac{19}{30},
\tag{14}
\]
where the last comparison is \(33\,600<33\,649\).
This contradicts (13), and proves (2).

## 4. Source scope

The deduction retains the original selected \(u_\delta\), the
original cubic \(c\), and the unexponentiated return in (1).
It excludes a larger depth on that actual curve, rather than
excluding unrelated algebraic roots.

In the complete right-edge upper envelope this improves the physical
endpoint rate to
\[
                    e=(H+K)/2<H/2+1/5.
\]
No comparison of its full attached inner rate with
\(\Re S_3(0,u_\delta)\), no common taper, and no new finite packet
are proved by this inequality alone.

## Frozen source bindings

- Full selected charged curve:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Actual sheet and original cubic guards:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Complete finite right-edge upper envelope:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
