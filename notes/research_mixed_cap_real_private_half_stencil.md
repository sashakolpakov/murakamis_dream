# The real-private cap half-stencil: one paid switch and two endpoint tests

Research deduction, 7 November 2026. The complete early-taper source
now has a real-private profile envelope. On that profile the cap half
with fixed outgoing height is strictly positive for both own types.
For the switch that changes outgoing height, its minimum over the
private real coordinate occurs at one of the two original cuts.
Both resulting own-three signs and the own-four left-cut sign
are also positive. The own-four right-cut sign, with the actual
height correlation retained, remains open. No numerical evaluation
or new certificate is used.

## 1. Source and exact half-stencil

Use the original cap phases and allocations in
[the alias-payment note](research_mixed_cap_alias_half_and_private_payment.md),
and the complete literal source envelope from
[the early-taper real-row theorem](research_mixed_cap_early_taper_real_rows.md).
For \(e\in[.27,.49]\) real, put
\[
\begin{split}
 p_\alpha(e,z)&=g'(e+z)-(1+\alpha/2)g'(z),\qquad \alpha=0,1,\\
 H_\chi(e,z;c)&=\Re\left[(1+i\chi c/.12)
                         \{p_\alpha(e,z)+3i/2\}\right].
\end{split}                                                   \tag{1}
\]
Take
\[
 .1\le x=\Re z\le.22,\qquad -.108\le h=\Im z\le.021.
                                                               \tag{2}
\]
For an actual moving minimum, \(h=c(x-.1)/.12\), with any
additional inherited cutoff retained as prescribed. The first
lemma is valid even on the larger independent rectangle (2).
The second lemma retains arbitrary fixed \(z,c\), and therefore
does not enlarge an actual taper when it is applied.

## 2. Strict positivity of the fixed-height switch

**Lemma 1.** On (2), throughout the complete private interval,
\[
 H_0(e,z;c)>\begin{cases}21/242,&\alpha=0,\\1/132,&\alpha=1.
                    \end{cases}                         \tag{3}
\]

*Proof.* Let \(r=e^{2\pi h}\). The fixed bounds imply
\[
                       \frac12<r<\frac{23}{20}.          \tag{4}
\]
For the upper bound use \(2\pi h\le.042\pi<33/250\) and
\[
 e^u\le1+u+\frac{u^2}{2(1-u/3)}\quad(0\le u<3);
\]
its value at \(33/250\) is less than \(23/20\).
For the lower bound, \(.216\pi<594/875<56/81<\log2\),
where the last inequality is the first two positive terms of
\(\log2=2\sum_{j\ge0}(1/3)^{2j+1}/(2j+1)\).

The real-argument ranges give
\[
 \cos2\pi(e+x)<-\frac6{25},\qquad
 \cos2\pi x>\frac9{50}.                                \tag{5}
\]
For the first bound the maximum cosine on \([.37,.71]\)
is attained at an endpoint. At \(.37\) it is less than
\(-1/2\); at \(.71\) it equals \(-\sin(.08\pi)<-6/25\).
The sine lower polynomial at \(1/4<.08\pi\) proves this
last bound. Similarly \(\cos(.44\pi)=\sin(.06\pi)>9/50\),
using the sine lower polynomial at \(3/16<.06\pi\).

Set
\[
 A=|1-re^{-2\pi i(e+x)}|^2,\qquad
 B=|1-re^{-2\pi ix}|^2,\qquad T=1+r^2.
\]
Then
\[
 A>T+\frac{12}{25}r,\qquad
 0<B<T-\frac9{25}r<2.                                  \tag{6}
\]
The final bound follows from monotonicity of the quadratic for
\(r>1/2\) and its value \(3817/2000<2\) at \(23/20\).

For own type four, expand the exact lower comparison:
\[
\begin{split}
 \frac{(T+12r/25)^2-(T-9r/25)^3}{r}
 ={}&\frac{51}{25}-\frac{724}{625}r
       +\frac{49479}{15625}r^2-\frac{1493}{625}r^3\\
   &+\frac{27}{25}r^4-r^5>\frac12.
\end{split}                                                   \tag{7}
\]
Indeed the quadratic/cubic terms are bounded below by
\((26221/62500)r^2>0\), and the fourth/fifth terms by
\(-(7/100)(23/20)^4\). The remaining lower bound is
\[
 \frac{51}{25}-\frac{724}{625}\frac{23}{20}
             -\frac7{100}\left(\frac{23}{20}\right)^4
              =\frac{9366553}{16000000}>\frac12.
\]
Thus \(A^2-B^3>r/2>1/4\). Since \(B^3<8\),
\(A^2/B^3>33/32\), and
\[
 H_0=\Re p_1=\frac14\log(A^2/B^3)
             >\frac14\log(33/32)>\frac1{132}.
\]

For own type three it is preferable not to subtract an allocation
from the preceding estimate: the sign of \(\log B\) varies.
Directly, (5)--(6) imply
\(A-B>(21/25)r>21/50\), so \(A/B>121/100\). Therefore
\[
 H_0=\Re p_0=\frac12\log(A/B)
           >\frac12\log(121/100)>\frac{21}{242}.
\]
Both final logarithm bounds use \(\log(1+u)>u/(1+u)\).
\(\square\)

The negative complex-private alias example does not contradict
(3): the numerator and denominator there had different radii.
Here their common radius is preserved exactly.

## 3. The moving-height switch has no interior private minimum

**Lemma 2.** Fix any \(z=x+ih\) with \(.1\le x\le.22\)
and any real \(c\). For either flag,
\[
 \min_{.27\le e\le.49}H_1(e,z;c)
           =\min\{H_1(.27,z;c),H_1(.49,z;c)\}.           \tag{8}
\]
In particular the statement holds with the exact original relation
between \(h,c,x\); no independent broadening is needed.

*Proof.* Put \(a=-c/.12\), \(r=e^{2\pi h}>0\),
and \(\theta=2\pi(e+x)\). All terms in (1) except
\(g'(e+z)\) are independent of \(e\). The exact derivative is
\[
 \partial_eH_1
    =\frac{2\pi r}{|1-re^{-i\theta}|^2}
           \{\sin\theta+a(\cos\theta-r)\}.             \tag{9}
\]
Throughout this interval \(\cos\theta<0\).
At any zero of the numerator \(N(\theta)\),
\[
 a=\frac{\sin\theta}{r-\cos\theta},\qquad
 N'(\theta)=\frac{r\cos\theta-1}{r-\cos\theta}<0.
                                                               \tag{10}
\]
Every critical point is therefore a strict positive-to-negative
derivative crossing, hence a maximum. There can be at most one
such crossing; a second would require an intervening crossing of
the opposite direction. Otherwise the function is monotone.
In either case its minimum occurs at an endpoint, proving (8).
This argument covers positive as well as negative original heights.
\(\square\)

## 4. Three of the four remaining endpoint signs

Now retain the actual unselected sign and height relations
\[
 -.108\le c\le.021,\qquad h=\rho c,
 \quad 0\le\rho\le1,
\]
where the minimum-level contour in particular uses
\(\rho=(x-.1)/.12\). The own-four case has \(c\le0\).

**Proposition 3.** For own type three, throughout these domains,
\[
                         H_1(e,z;c)>\frac1{20}
                             \qquad(.27\le e\le.49).
                                                               \tag{11}
\]
For own type four with \(c\le0\),
\[
                         H_1(.27,z;c)>\frac1{132}.       \tag{12}
\]

*Proof at the left private cut.* At \(e=.27\), the numerator
angle belongs to \([.74\pi,.98\pi]\), and the denominator
angle to \([.2\pi,.44\pi]\). In addition to (5),
\[
 \cos(2\pi(e+x))<-\frac{17}{25},\quad
 \sin(2\pi(e+x))<\frac{37}{50},\quad
 \sin(2\pi x)>\frac{29}{50}.                            \tag{13}
\]
The cosine lower polynomial through degree six and sine upper
polynomial through degree five at \(143/175>.26\pi\)
give the first two constants. The sine lower polynomial at
\(157/250<.2\pi\) gives the third.
Since \(r+r^{-1}<5/2\) throughout (4),
\[
 \frac BA<\frac{5/2-9/25}{5/2+34/25}
                    =\frac{107}{193}.
\]
It follows that, for either flag,
\[
 \frac{d}{dr}\Im p_\alpha
 =\frac{\sin(2\pi(e+x))}{A}
       -(1+\alpha/2)\frac{\sin(2\pi x)}B<0,             \tag{14}
\]
because \((37/29)(107/193)<1\).
At \(r=1\), the original arguments give exactly
\[
 \Im p_0=-.27\pi,\qquad
 \Im p_1=\pi(.5x-.52)\ge-.47\pi>-3/2.                \tag{15}
\]
If \(c\le0\), then \(a=-c/.12\ge0\) and \(r\le1\),
so (14)--(15) imply \(\Im p_\alpha+3/2>0\).
Consequently \(H_1=H_0+a(\Im p_\alpha+3/2)>H_0\)
when \(a>0\), and the nonstrict version holds when \(a=0\).
Lemma 1 proves (12) and the required own-three left endpoint.

For own three with \(c\ge0\), \(-7/40\le a\le0\)
and \(1\le r<23/20\). Now (14) gives \(\Im p_0<0\).
Moreover \(r+r^{-1}\le929/460\), so (13) improves the
modulus ratio to
\[
 \frac AB>\frac{929/460+34/25}{929/460-9/25}
                =\frac{7773}{3817}>2.
\]
Thus \(H_0>\tfrac12\log2>1/3\), while
\(a(\Im p_0+3/2)\ge-21/80\). This gives
\(H_1>17/240>1/20\) at the left cut.

*Own three at the right private cut.* At \(e=.49\), the
numerator sine is negative and the denominator sine positive.
Thus (14) is strictly negative for every \(r>0\), and
\(\Im p_0=-.49\pi\) at \(r=1\).
If \(c\ge0\), then \(r\ge1\), \(a\le0\), and
\(\Im p_0+3/2<0\); the correction to \(H_0\) is
nonnegative. If \(c\le0\), then \(r\le1\), \(0\le a\le.9\),
and
\[
 a(\Im p_0+3/2)\ge a(3/2-.49\pi)>-\frac9{250}.
\]
Therefore Lemma 1 yields
\[
 H_1>\frac{21}{242}-\frac9{250}>\frac1{20}.
\]
Apply Lemma 2 to the two own-three endpoints to obtain (11).
\(\square\)

The sole remaining cap-side inequality is own four at \(e=.49\),
with \(c\in[-.108,-.020]\) and the actual relation
\(r=\exp\{2\pi c(x-.1)/.12\}\) (and any prescribed
additional cutoff treated explicitly). Independent ranges for
\(r\) and \(c\) cannot replace this correlation.

The shared center switch must still remain identical in the cap
and ordinary halves, and their imaginary gauges must cancel before
interpreting these statements as transport of the full action.
The ordinary neighbor's actual reference-height domain and the
retained middle compensation remain compulsory. In particular the
older ordinary stencil certificates have narrower height inputs
than some attached first coordinates; those certificates are not
silently enlarged by Proposition 3. No complete compensated
boundary sign is asserted.
