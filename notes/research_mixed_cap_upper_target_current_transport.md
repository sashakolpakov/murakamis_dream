# Calibrated transport of the first-cap cuts and aliases

Research deduction, 7 November 2026. At the original outgoing
height, four of the eight cap-current families decrease relative
to their original reference plane throughout the upper target
interval. Their completed plateau margins therefore extend
without new calculations. The other four families have explicit
fixed transport costs, which can be compared with their immutable
saved source reserves. No saved-reserve comparison is executed
here, and no height-taper or whole-cap theorem is asserted.

## 1. Original profiles, reference and derivative

Use the phases, source and enlarged regular product of the
[upper-target extension](research_mixed_cap_upper_target_extension.md).
Fix an actual cap reference
\[
 e_*=b+ih_*,\qquad z_*=a+ic,\qquad
 p=L_\alpha'(z_*),\qquad \kappa=1/2500000.
 \tag{1}
\]
The original endpoint image rectangles are
\[
 \begin{array}{c|cc}
 \alpha& e_*&z_*\\ \hline
 0&(.376,.438)+i(-.019,.037)&(.278,.391)+i(-.072,.021)\\
 1&(.333,.363)+i(-.051,-.019)&(.246,.350)+i(-.108,-.020).
 \end{array}
 \tag{2}
\]
They are the exact original image bounds used by the
[completed cap certificate](research_mixed_first_cap_coupled_plateau_certificate.md).
All its actual-reference exclusions and length cases remain
unchanged; only the outgoing integration target is varied here.

For a real cut \(e=.27\) or \(e=.49\), or an alias
\(e=x+i\eta\) with \(x\in[.27,.49]\) and
\(\eta=-.055,.04\), define the calibrated defect
\[
 \begin{split}
 D_{\alpha,e}(y)={}&
 \Re\Xi_\alpha(e,y+ic)-\Re L_\alpha(z_*)
       -\Re p\,(y-a)+\kappa(y-a)^2-\mathfrak p_e,\\
 \mathfrak p_e={}&0\quad\hbox{for cuts},\qquad
       \mathfrak p_e=2\pi|\eta|\quad\hbox{for aliases}.
 \end{split}
 \tag{3}
\]
Thus this is exactly the defect certified on \([.22,.45]\),
including its small quadratic allowance. The real cuts retain
height zero. Put \(r=e^{2\pi c}\), \(R=e^{2\pi\eta}\).
The original \(g'\) identity gives
\[
 \begin{split}
 D_{\alpha,e}'(y)
   ={}&\log|1-Rr e^{-2\pi i(x+y)}|
       -(1+\alpha/2)\log|1-r e^{-2\pi iy}|
                      -\Re p+2\kappa(y-a),\\
 \Re p={}&
 \log|1-e^{-2\pi i(e_*+z_*)}|
       -(1+\alpha/2)\log|1-e^{-2\pi iz_*}|.
 \end{split}
 \tag{4}
\]
In sine notation the first line's uncalibrated slope is
\[
 \log\left|\frac{\sin\pi(e+y+ic)}{\sin\pi(y+ic)}\right|
       +\pi\eta-\frac\alpha2
            \{\log|2\sin\pi(y+ic)|+\pi c\}.
 \tag{5}
\]
In particular the alias term \(+\pi\eta\) is retained. The
same radius \(r\) occurs in the target and reference in (4).
It will not be replaced by independent extrema in the own-four
comparison.

## 2. The own-four correlated slope comparison

For \(\alpha=1\), (2) implies
\[
 \frac12<r<\frac9{10},\qquad
 e^{2\pi h_*}>\frac{18}{25},\qquad
 -\cos(2\pi(b+a))>\frac{23}{100},\qquad
 -\cos(2\pi a)<\frac{59}{100},
 \tag{6}
\]
Here \(b+a\in(.579,.713)\). The cosine bounds follow from
\(\sin(.074\pi)>.23\) and
\(\cos(.3\pi)<.59\). For example
\(.23236-(.233)^3/6>.23\), and the fourth-degree
upper cosine polynomial at \(471/500<.3\pi\) is less
than \(.59\). The radius assertions follow from the elementary
exponential bounds already used in the original image proofs;
one may also use
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)}
 \quad(0\le x<3)
 \tag{7}
\]
at \(x=.321>.102\pi\) for \(e^{2\pi h_*}>18/25\).
The old \(e^{.216\pi}<2\) gives \(r>1/2\);
\(e^{.04\pi}>10/9\) gives \(r<9/10\).

Write \(q=1+r^2\), and introduce four positive polynomials
\[
 N=1+\frac{324}{625}r^2+\frac{207}{625}r,\quad
 T=q+\frac{19}{50}r,\quad
 V=q+\frac{59}{50}r,\quad
 D=q+\frac{19}{10}r .
 \tag{8}
\]
For the reference, (6) gives
\[
             \Re p>\frac12\log N-\frac34\log V.
 \tag{9}
\]
For \(y\in[.45,.5]\), every \(x\in[.27,.49]\)
satisfies \(.72\le x+y\le.99\), so
\(-\cos(2\pi(x+y))\le\sin(.06\pi)<19/100\).
Also \(-\cos(2\pi y)\ge\cos(.1\pi)>19/20\).
Thus at either real cut, and also at every lower-alias point
where \(R<1\), the uncalibrated slope in (4) is at most
\[
                         P_0(r)=\frac12\log T-\frac34\log D.
 \tag{10}
\]
For the lower alias this uses
\(1+(Rr)^2+(19/50)Rr\le T\), so does not lose its height.

The following exact polynomial proves a uniform separation:
\[
 \begin{split}
 \mathcal E(r)&=2ND^2-TV(D+V),\\
 \frac{\mathcal E(r)}r
 &=\frac1{125000}\bigl(
 257800+384040r+184354r^2\\
 &\hspace{25mm}-171004r^3-199720r^4-120400r^5\bigr)\\
 &\ge\frac{257800+384040r-306770r^2}{125000}
 \ge\frac{1289}{625}\qquad(0\le r\le1).
 \end{split}
 \tag{11}
\]
The last polynomial is concave, and its two endpoint values
are \(257800/125000\) and \(335070/125000\).
Since \(r>1/2\), \(\mathcal E(r)>1\).
Moreover \(T<9/4\) and \(D<4\).

Put \(v=V/D\in(0,1)\). Dividing (11) by \(2TD^2\)
and using \((1+v)/2\ge\sqrt v\) gives
\[
 \frac NT>\frac{v(1+v)}2+\frac1{72}
          \ge v^{3/2}+\frac1{72}.
 \tag{12}
\]
It follows from (9)--(10) that
\[
       \Re p-P_0(r)>
       \frac12\log\frac{73}{72}>\frac1{146}.
 \tag{13}
\]
This is the correlated marginal comparison; no independent
constant lower bound for \(p\) is needed.

Since \(2\kappa(y-a)<\kappa\), equations (4) and (13)
prove, for the two real cuts and the lower alias,
\[
                   D_{1,e}'(y)<-\frac1{200}.
 \tag{14}
\]
The inequalities are uniform in the free alias coordinate \(x\),
so they also transport its supremum.

For the upper alias put \(R=e^{.08\pi}>1\).
The reference height satisfies \(r<R^{-1/2}\). At any angle
\(\theta\),
\[
 \begin{split}
 R^2|1-r e^{i\theta}|^2-|1-Rr e^{i\theta}|^2
  &=(R-1)(R+1-2Rr\cos\theta)\\
  &\ge(R-1)(R+1-2\sqrt R)\ge0.
 \end{split}
 \tag{15}
\]
Consequently its uncalibrated slope is at most
\(P_0(r)+\log R\). Equations (13) and (4) now imply
\[
       D_{1,e}'(y)<.08\pi,\qquad
       D_{1,e}(y)\le D_{1,e}(.45)+\frac{\pi}{250}.
 \tag{16}
\]
This transport cost already includes the \(\kappa\) term.

## 3. Own-three slopes and fixed transport costs

For \(\alpha=0\), the actual rectangles (2) imply
\[
          \frac35<r<\frac87,\qquad \Re p>-1.
 \tag{17}
\]
To verify the first claim, use
\(.144\pi<.46\), \(e^{.46}<5/3\), and
\(e^{.042\pi}<e^{33/250}<8/7\), all obtained from (7).
For the second, \(b+a\in(.654,.829)\) implies
\[
 |1-e^{-2\pi i(e_*+z_*)}|
   \ge|\sin(2\pi(b+a))|>\sin(.3\pi)>\frac45.
 \tag{18}
\]
The denominator in (4) is less than \(1+r<15/7\).
Thus \(\Re p>\log(28/75)>-1\), since
\(e>65/24>75/28\).

At the right cut \(e=.49\), one has
\(\cos(2\pi(e+y))\ge\cos(.12\pi)>9/10\). Using
\(r+r^{-1}\le34/15\) on \([3/5,6/5]\), the squared
modulus ratio in its slope obeys
\[
 \frac{|1-r e^{-2\pi i(.49+y)}|^2}
      {|1-r e^{-2\pi iy}|^2}
 \le\frac{1+r^2-(9/5)r}{1+r^2+(19/10)r}
 \le\frac{14}{125}<e^{-21/10}.
 \tag{19}
\]
For the last comparison, \(e<11/4\) and
\(e^{1/10}<10/9\) give
\(e^{21/10}<605/72<125/14\). Thus its uncalibrated
slope is less than \(-21/20\), and (17) yields
\[
                        D_{0,.49}'(y)<-\frac1{25}.
 \tag{20}
\]

For the left cut and lower alias, the same numerator bound
as in (10), now with denominator exponent one, gives
\[
 \frac{|1-Rr e^{-2\pi i(x+y)}|^2}
      {|1-r e^{-2\pi iy}|^2}
 \le\frac{1+r^2+(19/50)r}{1+r^2+(19/10)r}
 \le\frac{397}{625}<e^{-21/50}.
 \tag{21}
\]
The exponential comparison follows from (7) at \(21/50\).
It follows that the uncalibrated slope is less than
\(-21/100\). Including (17) and the quadratic term gives
\[
              D_{0,e}'(y)<\frac45,\qquad
              D_{0,e}(y)\le D_{0,e}(.45)+\frac1{25}.
 \tag{22}
\]
For the upper alias \(R=e^{.08\pi}<13/10\). The numerator
is at most \(M=1+R^2r^2+(19/50)Rr\), whereas the
denominator is at least \(D=1+r^2+(19/10)r<9/2\).
Direct rational bounds give
\[
 D-M\ge r\left(\frac{19}{10}-\frac{19}{50}\frac{13}{10}
                      -\frac{69}{100}\frac87\right)
       >\frac13.
 \tag{23}
\]
Hence \(M/D<25/27\), and the uncalibrated slope is less
than \(\frac12\log(25/27)<-1/27\). Therefore
\[
                  D_{0,e}'(y)<1,\qquad
                  D_{0,e}(y)\le D_{0,e}(.45)+\frac1{20}.
 \tag{24}
\]
All the elementary exponential witnesses above use (7).
For \(e<11/4\), for example,
\(\sum_{k\ge4}1/k!<(1/24)/(1-1/5)=5/96\) suffices.
The sine and cosine bounds in (18)--(21) follow from
\(\sin(3\pi/10)=(1+\sqrt5)/4>4/5\),
\(\cos(.1\pi)>19/20\), and the second-degree lower
cosine bound at \(.12\pi\). Thus no evaluated logarithm
or newly sampled parameter is an input to these inequalities.

## 4. What already extends, and the four fixed saved comparisons

The source-defect derivative bounds apply to each alias coordinate
before taking its supremum. They therefore yield the following
transport table for the exact old calibrated current profiles:
\[
 \begin{array}{c|cccc}
 \alpha&\text{left cut}&\text{right cut}&\text{lower alias}
                                      &\text{upper alias}\\ \hline
 0&1/25&0&1/25&1/20\\
 1&0&0&0&\pi/250 .
 \end{array}
 \tag{25}
\]
Each entry is an upper cost in extending from \(y=.45\)
to any \(y\in[.45,.5]\), at the same original height \(c\).
Zero entries have a strictly decreasing defect. Consequently the
old completed margin \(1/200000\) for the own-three right cut
and the own-four left cut, right cut and lower alias is preserved
on the entire enlarged interval. This is an unconditional
current comparison on the already certified actual-reference sets.

The other four entries are fixed sufficient tests against saved
reserves. The completed 320-bit cap replay stores for every original
reference job a conservative maximum of its accepted leaf uppers.
For the corresponding family, add exactly the cost in (25),
using the outward rational \(\pi/250<11/875\) in the last
entry. Strict negativity of every such sum would prove that
family on the upper interval without a new source, root or
derivative evaluation. An all-excluded job is accounted for only
through its already audited actual-reference exclusion proof.
No charged sign is asserted before this fixed extraction is
reviewed and executed. A positive upper would remain inconclusive.

This proof neither moves the outgoing height nor compares an
unrelated reference. The complete finite cap would additionally
need its extreme-row ceiling and every retained Fourier
alternative allocated on the enlarged domain. In particular
these current extensions do not by themselves control a
height-taper graph or settle the contracted finite-boundary sign.
