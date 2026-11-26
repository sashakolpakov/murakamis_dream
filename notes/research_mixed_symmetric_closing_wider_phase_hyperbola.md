# The original wider cubic branch and a decreasing right hyperbola

Private phase deduction, 9 November 2026. The original selected
inner-three phase continues to the next real-angle interval.
On a specified outer hyperbola its original closing action
decreases strictly from an already gapped endpoint. This is a
phase theorem, not a finite-kernel continuation.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation or frozen-source edit is used.

## 1. Original branch on the wider outgoing rectangle

Let
\[
 \mathcal R=\{u=\beta-iK:\pi/2\le\beta\le2\pi/3,\quad0\le K\le7/10\},
 \qquad C=\cos(u/2).
 \tag{1}
\]
Start with the original cubic branch on the face \(\beta=\pi/2\)
of the adopted taller strip. Write
\[
 v=2c=x+ib,\qquad c=\cos(t_*(u)/2),\qquad
 v^3-2iv^2-3v+2i-2C=0 .
 \tag{2}
\]
The original cubic theorem gives the unique distinguished root
with \(\Re v>3/2\) on \(\Re C>1/2\). On (1),
\[
 \frac12\le\Re C<\frac45,\qquad
                  0\le2\Im C<\frac{21}{32}.
 \tag{3}
\]
Indeed \(\cosh(7/20)<17/16\),
\(\sinh(7/20)<3/8\), \(1/\sqrt2<3/4\), and
\(\sqrt3/2<7/8\) give the strict upper bounds
\(\Re C<51/64<4/5\) and \(2\Im C<21/32\).

The imaginary equation in (2) is
\[
 2\Im C=(3b-2)x^2-b^3+2b^2-3b+2 .
 \tag{4}
\]
At \(b=1/2\) its right side is
\(-x^2/2+7/8<-1/4\). At \(b=7/10\) it is
\(x^2/10+537/1000>381/500>21/32\).
Connected continuation of the original root therefore retains
\[
                         1/2<b<7/10.
 \tag{5}
\]
On the initial face this uses the taller bound \(1/3<b<2/3\):
the right side of (4) increases in \(b\) on that interval,
and is negative at \(b=1/2\), whereas \(2\Im C\ge0\).
Thus the original root starts between the two barriers.
Its real equation is
\[
 2\Re C=x(x^2-3b^2+4b-3).
 \tag{6}
\]
Since \(-3b^2+4b-3>-2\), \(x\ge7/4\) would imply
\(\Re C\ge119/128>4/5\). Thus \(x<7/4\).
There is no failure at the sole boundary point \(\Re C=1/2\):
at \(x=3/2\), the right side of (6) is at most \(7/8<1\),
because \(-3b^2+4b-3\le-5/3\). Hence the root remains
strictly to the right of \(x=3/2\) there as well.

In particular
\[
 3/2<x<7/4,\quad1/2<b<7/10,\quad
 |v|^2<1421/400<4,\qquad
 \Delta:=3v^2-4iv-3,\quad\Re\Delta>5.
 \tag{7}
\]
For the last estimate the minimum of
\(-3b^2+4b-3\) on \([1/2,7/10]\) is \(-7/4\).
The original root therefore extends holomorphically to a
neighborhood of the compact rectangle (1), including its
corner at \(\Re C=1/2\); the implicit charts agree with the
original branch on their overlap.

Use the original arccosine lift \(t_*=a_*-iH_*\). It has
\(a_*>0,H_*>0\). In fact
\[
                         1/10<H_*<1,\qquad a_*<2\pi/3.
 \tag{8}
\]
Here is a complete height check. If \(H_*\ge1\), put
\(s=\sinh^2(H_*/2)>(25/48)^2\). The exact cosine identity gives
\[
 x^2=4(1+s)-(1+s^{-1})b^2,
 \quad
 2\Re C=x\{1+4s+4b-(4+s^{-1})b^2\}.
 \tag{9}
\]
For fixed \(s\), both positive factors in the second expression
decrease in \(b\in[1/2,7/10]\); for fixed \(b\), both increase
in \(s\). Positivity follows from their values at
\(b=7/10,s=(25/48)^2\), as follows. The first identity there
gives
\[
 x^2>\frac{106479}{62500}+\frac{625}{576}>\frac{25}{9},
 \tag{10}
\]
where the second comparison is
\(106479\cdot192>325\cdot62500\), with difference \(131468\).
The brace is then greater than
\(25/9-167/100=997/900>1\).
For its monotonicity in \(b\), its derivative is
\(4-2(4+s^{-1})b\le-s^{-1}<0\).
Thus (9) would imply \(\Re C>5/6>4/5\), a contradiction.
Finally
\[
 \cos(a_*/2)=\frac{x}{2\cosh(H_*/2)}
                     >\frac{3/4}{8/7}=\frac{21}{32}>\frac12,
 \tag{11}
\]
which proves the angle bound in (8).
For the lower height, \(b=2\sin(a_*/2)\sinh(H_*/2)>1/2\)
implies \(\sinh(H_*/2)>1/4\). But
\(\sinh(1/20)\le(1/20)/(1-1/2400)<1/4\), so
\(H_*>1/10\).

## 2. The unsquared critical equation and the outgoing return

No polynomial root is substituted for an unverified logarithmic
critical point. Put \(T=\tan(t_*/2)\). It has positive real and
negative imaginary parts. Since \(C\) is in the closed first
quadrant with positive real part, both \(T\) and \(CT\) have
positive real parts. Their original principal inverse
hyperbolic sines stay off their cuts. The exponential identity
from the original cubic proof and connected continuation
from \(\beta=\pi/2\) retain the unsquared equation
\[
 \operatorname{arsinh}T+\operatorname{arsinh}(CT)
                            =i(3t_*/2-\pi).
 \tag{12}
\]
The cubic derivative and the principal coshes are nonzero,
so the same original Hessian identity proves
\(\Phi_{tt}(t_*,u)\ne0\).

The wider positive edge theorem identifies the same calibrated
primitive at these \(t_*,u\); no charge or complete constant
is changed. Define
\[
 S(u)=\psi(t_*,0)+\psi(t_*,u)+3it_*^2/(4\pi)-it_*,
 \qquad
 f(u)=\operatorname{arsinh}\{c(u)\tan(u/2)\}.
 \tag{13}
\]
The argument of \(f\) has positive real part, since \(c\)
is in the first quadrant and \(\tan(u/2)\) in the closed
lower right quadrant. Hence this is the original principal
return, and
\[
                              S'(u)=-f(u)/\pi.
 \tag{14}
\]
It continues the original action from the taller strip.

For the derivative calculation set \(A=c^2,B=C^2,D=A+B-AB\).
The bounds in (7) imply
\[
 \frac34<\Re c<\frac78,\qquad
 \frac14<\Im c<\frac7{20},\qquad |c|<1.
 \tag{15}
\]
Writing \(P=(\Re c)^2,Q=(\Im c)^2\), the function
\[
 |1-c^2|^2=1-2P+2Q+(P+Q)^2
 \tag{16}
\]
decreases in \(P\) and increases in \(Q\), since \(P+Q<1\).
At their bounding corner it equals \(23569/40000<16/25\).
Thus
\[
 |1-A|<4/5,\quad |1-B|<9/10,\quad
 |D-1|<18/25,\quad \Re D>7/25.
 \tag{17}
\]
Moreover \(0<\Re A<1\), \(0<\Re B\le1/2\),
\(\Im A>0,\Im B\ge0\); hence \(\Im D>0\).
The continued principal cosh is \(\sqrt D/C\).
Differentiating (2),(13) therefore gives the exact original
formula already used in the horizontal concavity theorem,
\[
 f'=L+E,\qquad
 L=\frac{c}{2C\sqrt D},\qquad
 E=-\frac{1-B}{2\Delta\sqrt D}.
 \tag{18}
\]
Since \(|C|^2<13/20<(13/16)^2\), (7),(15),(17) give
\[
                        |E/L|<39/200.
 \tag{19}
\]

## 3. Directional positivity on the right hyperbola

Keep the actual complete closing point
\(u_g=\beta_g-iK_g\), with \(0<\beta_g<\pi/2\) and
\(17/30<K_g<7/10\). Consider
\[
 u(\beta)=\beta-iK(\beta),\quad
 K(\beta)=\frac{\pi K_g}{2\beta},\quad
                    \pi/2\le\beta\le2\pi/3,
 \qquad r=\frac{K}{\beta}.
 \tag{20}
\]
This lies inside (1), and \(0<r<7/15\).
We prove
\[
                    \Re\{(1+ir)^2f'(u)\}>0 .
 \tag{21}
\]

First \(\arg c<\arctan(7/15)\). Also
\[
 \arg C
   =\arctan\{\tan(\beta/2)\tanh(K/2)\}
   <\arctan\{(\pi/\sqrt3)r\}
   <\arctan(2r)<2\arctan r.
 \tag{22}
\]
Here \(\tan(\beta/2)\le\sqrt3\), \(\beta\le2\pi/3\),
and \(\pi/\sqrt3<2\), the latter following for example from
\(\pi<22/7\) and \(\sqrt3>5/3\). Since
\(0<\arg\sqrt D<\pi/4\), the argument of the rotated leading
term lies in
\[
 -\pi/4<
 \arg\{(1+ir)^2L\}
 <3\arctan(7/15)<\pi/2 .
 \tag{23}
\]
Its cosine exceeds \(1/4\). At the larger positive endpoint,
\[
 \cos\{3\arctan(7/15)\}
       =\frac{1170}{274\sqrt{274}}
       >\frac{1170}{274\cdot17}>\frac14,
 \tag{24}
\]
where \(4680>4658\). The negative endpoint has cosine
\(1/\sqrt2>1/4\).
Combining (19),(23)--(24) proves the quantitative version
\[
 \Re\{(1+ir)^2 f'\}>
                   \frac{11}{200}|1+ir|^2|L|>0 .
 \tag{25}
\]

## 4. Strict decrease with the original closing normalization

Set
\[
 \Xi(u)=2S(u)+iu^2/\pi-iu,\qquad
 g(\beta)=\Re f(u)-r\Im f(u)-\pi r/2 .
 \tag{26}
\]
Since \(K'=-r\), \(r'=-2r/\beta\), direct differentiation gives
\[
 \frac d{d\beta}\Re\Xi(u(\beta))=-2g/\pi,\qquad
 g'=\Re\{(1+ir)^2 f'\}-r'(\Im f+\pi/2)>0.
 \tag{27}
\]
The second term is positive because \(f\) is the principal
return with \(\Im f>-\pi/2\).

The initial sign is fixed by the original source, not by
assuming that a continued action decreases. Put
\(u_0=\pi/2-iK_g\), and \(d=\pi/2-\beta_g>0\).
The adopted horizontal concavity gives
\[
 \Re f(u_0)-K_g>d/8,\qquad
 \Re\Xi(u_0)\le M_g-d^2/(8\pi),
             \quad M_g=\Re\Xi(u_g).
 \tag{28}
\]
At this initial point the taller cubic bounds have
\(\Re c>3/4,\Im c<1/3\). Hence
\[
 \Im\{c\tan(u_0/2)\}
   =\frac{\Im c-\Re c\,\sinh K_g}{\cosh K_g}<0,
 \tag{29}
\]
using \(K_g>17/30\) and
\((3/4)(17/30)=17/40>1/3\).
Thus \(\Im f(u_0)<0\) and \(g(\pi/2)>d/8\).
Equations (27)--(29) prove on the full path (20)
\[
 \boxed{\quad
 \Re\Xi(u(\beta))
 \le M_g-\frac{d^2}{8\pi}
              -\frac{d}{4\pi}(\beta-\pi/2).
 \quad}
 \tag{30}
\]

This identifies a strictly decreasing original geometric-action
path through the wider real-angle rectangle. It does not prove
a packet or an upper bound of rate \(S(u)\) for the full inner
kernel there. In particular the fixed-depth geometric maximum
in the separate endpoint-budget note has not been replaced by
the selected action (13). All remaining finite inner currents
and both edge-restoration errors still need their own estimates
before (30) can pay the full right outer connector.

## Frozen source bindings

- Distinguished cubic root, original unsquared equation and Hessian:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Taller strip, calibration and height series:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Wider positive finite edge and original critical-value continuation:
  f3f9cdca2307f100a5766638ae91e329be5c7f372ac9b303ede0a28c9953e22f.
- Original outgoing derivative and horizontal maximum:
  f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
- Actual geometric height localization:
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
