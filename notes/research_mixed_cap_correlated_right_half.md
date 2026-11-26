# The remaining real-private right-cut half on the actual early taper

Research deduction, 7 November 2026. This closes the remaining cap-side
half-stencil from the
[real-private comparison](research_mixed_cap_real_private_half_stencil.md).
The radial variable is kept tied to the actual outgoing height slope.
All estimates below are analytic inequalities with explicit rational
witnesses; no functions or certificates are evaluated.

The conclusion is a cap-side transport inequality. It does not enlarge
the reference-height domains of the adjoining ordinary certificates,
or pay the separate true-index ceiling of the complete finite source.

## 1. The original correlated quantity

Write
\[
 .1\le x\le.22,\qquad d=x-.1,\qquad
 0\le a\le\frac9{10},\qquad z=x-iad,
 \quad r=e^{-2\pi ad}.
                                                               \tag{1}
\]
The original attached-four height is \(c=-.12a\). Thus (1)
contains its actual unselected early path, with the original
relation between height, slope and real coordinate. At the remaining
private endpoint \(e=.49\), set
\[
 p=g'(.49+z)-\frac32g'(z),\qquad
 H=\Re p+a(\Im p+3/2).
                                                               \tag{2}
\]
This is exactly \(H_1(.49,z;c)\) in the preceding note, including
its original imaginary gauge and outgoing halfweight allocation.

Define the following real functions:
\[
\begin{split}
 P_0(x)&=\log(2\cos\pi(x-.01))
                         -\frac32\log(2\sin\pi x),\\
 C(x)&=\frac32-\frac{37\pi}{50}+\frac{\pi x}{2},\\
 D(x)&=\frac12\tan\pi(x-.01)+\frac34\cot\pi x.
\end{split}                                                   \tag{3}
\]
These are the real part, shifted imaginary part and radial argument
coefficient at radius one, with the original logarithmic lifts.

## 2. Moving inward does not lower the real part

**Lemma 1.** Throughout (1),
\[
                            \Re p\ge P_0(x).             \tag{4}
\]
Equality holds when \(ad=0\); otherwise the inequality is strict.

*Proof.* Put \(t=2\pi ad\) and
\(\delta=\cosh t-1\). The exact modulus identity is
\[
\begin{split}
 \Re p-P_0(x)=\frac t4
 &+\frac12\log\left(1+
                 \frac\delta{1+\cos(2\pi(x-.01))}\right)\\
 &-\frac34\log\left(1+
                 \frac\delta{1-\cos(2\pi x)}\right).
\end{split}                                                   \tag{5}
\]
Let
\[
 H_*(x)=\frac3{8\sin^2\pi x}
                         -\frac1{4\cos^2\pi(x-.01)}>0.
                                                               \tag{6}
\]
The difference of the last two derivatives in (5), with its sign
reversed, decreases as \(\delta\) increases: its positive term
has coefficient \(3/4\) and the smaller denominator, whereas
the negative term has coefficient \(1/2\) and the larger one.
Integrating from zero gives
\[
                 \Re p-P_0(x)\ge t/4-H_*(x)(\cosh t-1).
                                                               \tag{7}
\]
Positivity in (6) follows already from
\(\sin^2\pi x<1/2<\cos^2\pi(x-.01)\).

Here is a rational bound that retains enough of both terms of (6).
For \(0<u<1\),
\[
 \sin u\ge u-u^3/6\ge\frac{u}{1+u^2/5},
 \qquad \sec^2 v\ge1+v^2.
\]
The second inequality follows from \(\tan v\ge v\) for
\(v\ge0\). Since \(\pi x<1\), these imply
\[
\begin{split}
 H_*(x)
 &\le\frac3{8\pi^2x^2}-\frac1{10}
           +\frac{3\pi^2x^2}{200}
           -\frac{\pi^2(x-.01)^2}{4}\\
 &<\widehat H(x):=
     \frac{15}{392x^2}-\frac9{100}-\frac94(x-.01)^2.
\end{split}                                                   \tag{8}
\]
For the last line use \(\pi^2>49/5\), \(\pi^2>9\),
and \(3\pi^2x^2/200<1/100\), all following from
\(157/50<\pi<22/7\) and \(x\le11/50\).
In particular \(\widehat H>0\).

The positive cosh series gives, for \(0\le t<\sqrt{12}\),
\[
                 \cosh t-1\le\frac{t^2}{2(1-t^2/12)}.
                                                               \tag{9}
\]
We have \(t\le(9\pi/5)d\le T:=40d/7\), with the latter
inequality strict when \(d>0\). It therefore suffices
to prove
\[
\begin{split}
 G(d)&:=1-T^2/12-2T\widehat H(x)\\
 &=1-\frac{150}{343}\frac d{x^2}
       +\frac{36}{35}d+\frac{180}{7}d(d+.09)^2
       -\frac{400}{147}d^2>0,
 \qquad x=d+.1.
\end{split}                                                   \tag{10}
\]
Three direct rational comparisons prove this on the whole interval:

* If \(0\le d\le1/20\), then \(d/x^2\le20/9\).
  Dropping the positive terms in (10) gives
  \(G\ge1-1000/1029-1/147=22/1029>0\).
* If \(1/20\le d\le7/100\), then
  \(d/x^2\le700/289\). The positive terms are at least
  \(9/175\) and \(63/2500\), while the last negative term
  is at least \(-1/75\). Thus
  \[
    G\ge\frac{55823}{52500}-\frac{105000}{99127}>0;
  \]
  the numerator after cross multiplication is \(21066521\).
* If \(7/100\le d\le3/25\), use \(d/x^2\le5/2\).
  The remaining polynomial in (10) is increasing: its derivative
  is greater than \(36/35-32/49=92/245>0\).
  At \(d=7/100\) the resulting lower bound is
  \[
    G\ge\frac{10357}{9375}-\frac{375}{343}>0,
  \]
  with positive cross-product numerator \(36826\).

For the first two bounds, \(d/(d+.1)^2\) increases up to
\(d=.1\); its global maximum is \(5/2\). These facts
follow by differentiation, or by completing the square.
Hence (10) is not a sampled check.

Equations (8)--(10) imply
\(2tH_*+t^2/12<1\) when \(t>0\), so
\(H_*(\cosh t-1)<t/4\). Now (7) proves (4), including
the exact equality at \(t=0\). \(\square\)

## 3. The argument improvement uses the same radius

**Lemma 2.** On (1),
\[
               \Im p+3/2\ge C(x)+(1-r)D(x).             \tag{11}
\]

*Proof.* The actual radius satisfies
\[
 \cos(2\pi x)\le e^{-2\pi^2x^2}
                         <e^{-(9\pi/5)d}\le r.
                                                               \tag{12}
\]
For the strict comparison use
\[
 \pi x^2-.9(x-.1)>3(x-.15)^2+.0225>0.
\]
The first inequality in (12) is
\(\log\cos u\le-u^2/2\), valid here because
\(0<2\pi x<\pi/2\).

At the numerator angle \(2\pi(.49+x)\), the sine and
cosine are both negative. Its squared modulus increases with
radius, so it is at most its radius-one value on \([r,1]\).
For the denominator, (12) implies the same comparison, since
\(1+v^2-2v\cos(2\pi x)\) increases for
\(v\ge r>\cos(2\pi x)\).
Integrating the exact argument derivatives with respect to radius
from \(r\) to one therefore yields
\[
 \Im p(r)-\Im p(1)
 \ge(1-r)\left\{
     \frac12\tan\pi(x-.01)+\frac34\cot\pi x\right\}.
\]
The original unit-radius arguments give
\(\Im p(1)=\pi(.5x-.74)\). This proves (11).
\(\square\)

## 4. One outgoing endpoint pays the complete interval

Combining (4) and (11), define the valid lower bound
\[
 H\ge L(x,a):=P_0(x)+aC(x)
                   +a(1-e^{-2\pi a(x-.1)})D(x).          \tag{13}
\]
The exact derivative relation
\(P_0'=-2\pi D\) is useful. Also \(D'<0\), since
\[
 D'=\pi\{\tfrac12\sec^2\pi(x-.01)
                           -\tfrac34\csc^2\pi x\}<0.
\]
The two squared trigonometric terms here lie on opposite sides
of \(1/2\). Finally
\[
 D(x)\ge D(.22)>\frac54.                                \tag{14}
\]
For an elementary witness, \(\tan(.21\pi)>3/4\)
follows from \(\tan u\ge u+u^3/3\) at
\(u=3297/5000<.21\pi\). Moreover
\(\cos(.22\pi)>3/4\), \(\sin(.22\pi)<16/25\)
give \(\cot(.22\pi)>75/64>7/6\).
The two terms in (14) therefore exceed \(3/8\) and \(7/8\).

For fixed \(0\le a\le.9\), differentiating (13) gives
\[
\begin{split}
 \partial_xL
 &=-2\pi D+a\pi/2+2\pi a^2e^{-2\pi ad}D
                 +a(1-e^{-2\pi ad})D'\\
 &\le-2\pi D(1-a^2)+a\pi/2
 <\frac\pi2(5a^2+a-5)\le-\frac\pi{40}.
\end{split}                                                   \tag{15}
\]
Thus only \(x=.22\) needs a scalar lower comparison.
At that endpoint,
\[
 P_0(.22)>\frac2{25},\qquad C(.22)>-\frac{12}{25}.
                                                               \tag{16}
\]
For the first inequality, the cosine lower polynomial through
degree six at \(33/50>.21\pi\) gives
\(\cos(.21\pi)>157/200\). The sine upper polynomial
through degree five at \(121/175>.22\pi\) gives
\(\sin(.22\pi)<16/25\). Consequently
\[
 P_0(.22)>\frac12\log\frac{616225}{524288}
   >\frac{91937}{1140513}>\frac2{25},
\]
using \(\log q>2(q-1)/(q+1)\) for \(q>1\).
The second bound in (16) follows from \(\pi<22/7\).

At \(x=.22\), one has
\((3/4)a<(6\pi/25)a<(19/25)a\) for \(a>0\).
The inequality \(1-e^{-t}\ge t/(1+t)\), together with
(14)--(16), therefore yields
\[
\begin{split}
 L(.22,a)
 &>\frac2{25}-\frac{12}{25}a
                         +\frac{15a^2/16}{1+19a/25}\\
 &=\frac{q(a)}{1+19a/25},\qquad
 q(a)=\frac2{25}-\frac{262}{625}a
                              +\frac{5727}{10000}a^2.
\end{split}                                                   \tag{17}
\]
The quadratic \(q-3/1000\) has positive leading coefficient
and discriminant exactly \(-8287/12500000<0\). Hence
\(q>3/1000\) on the real line. Since
\(1+19a/25\le421/250\) on the required interval,
\[
               H\ge L(.22,a)>\frac{3}{1684}>\frac1{600}.
                                                               \tag{18}
\]

**Theorem 3.** The original own-four cap half with the moving-height
switch satisfies \(H_1(.49,z;c)>1/600\) on the actual path (1).
Combining this with the already proved left-cut bound and the exact
private-endpoint minimum principle proves
\[
 H_1(e,z;c)>\frac1{600}\qquad(.27\le e\le.49).
                                                               \tag{19}
\]
The fixed-height switch was already strictly positive. Both cap-side
switches are thus paid for the real-private own-four profile, just
as they are for own three.

This theorem keeps the height derivative paired with its actual
radius. It is not a statement for independent \(r,a\) boxes,
nor for a path whose height has an unrelated additional cutoff.
If a prescribed fixed multiplier rescales both the height and its
derivative, it can instead be absorbed into the single parameter
\(a\) in (1); arbitrary mismatched replacements are not allowed.

In the full boundary argument the cap gauge must cancel the adjoining
ordinary gauge, using the same center switch. The ordinary factor's
actual first-attached height ranges, the separate finite true-index
ceiling, the middle energy and the relative pinning fee remain to be
controlled. The conclusion is a strict new cap-side transport bound,
not yet a complete compensated left-boundary sign.
