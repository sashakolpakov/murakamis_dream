# No interior high-tail maximum in a collar of the first minimum seam

Research deduction, 7 November 2026. At zero outgoing heights,
the complete adjoining physical high-tail rate decreases until
the first target's reflected position and is convex thereafter.
Its maximum is therefore at the old upper cut or at the true
last row. The same conclusion holds on a fixed open small-height
collar, with no numerical width chosen.

This is an actual physical-row comparison, independent of a
moving-root packet. It does not compare either surviving endpoint
with the calibrated boundary reference or pay the neighboring
height change.

## 1. Exact ratio and a general terminal convexity

Use the literal conditional source and the physical rate
\(\mathcal R_{\alpha\epsilon}(u;a,b)\) of equations (17)--(19)
of the
[complete adjoining envelope](research_mixed_first_attached_complete_contour_envelope.md).
Assume
\[
 .1\le x\le.22,\qquad x\le z\le.5,\qquad
                  a=x+ih_a,\quad b=z+ih_b .                  \tag{1}
\]
The incoming allocation \(\alpha\) is arbitrary and does not
enter the \(u\) derivative. Put \(w=-\cot\pi u\).
Away from numerator zeros the exact derivative obeys
\[
 \begin{split}
 e^{2\mathcal R'(u)}
 ={}&4^{-\epsilon}e^{2\pi(h_b-h_a)}
       |\sin\pi a|^2|\sin\pi b|^2\\
 &\quad{}\times
       |w-\cot\pi a|^2|w-\cot\pi b|^2(1+w^2)^\epsilon .
 \end{split}                                                  \tag{2}
\]
This is the original sine ratio, including its chirp and
height-dependent constant. It is not the ratio of a modified row.

For any finite heights and real parts in (1),
\[
 \Re\cot\pi a\le\cot\pi x,\qquad
 \Re\cot\pi b\le\cot\pi z\le\cot\pi x .                        \tag{3}
\]
Indeed the real cotangent is
\(\sin(2\pi x)/(\cosh(2\pi h)-\cos(2\pi x))\), with
nonnegative numerator on these intervals.
If \(u\ge1-x\), then \(w\ge\cot\pi x>0\).
Each factor on the second line of (2) is nondecreasing in \(w\);
the two squared-distance factors strictly increase beyond their
possible initial zero. Since \(w\) increases with \(u\),
\(\mathcal R'(u)\) increases on \((1-x,1)\).
Thus
\[
 \max_{1-x\le u\le1}\mathcal R(u)
       =\max\{\mathcal R(1-x),\mathcal R(1)\}.                 \tag{4}
\]
The rate is continuous at an initial numerator zero and at the
true last row. Its derivative may start at \(-\infty\);
this does not affect convexity or (4).

This reduction holds at arbitrary finite heights. In particular
any interior high-tail maximum still needing attention lies
strictly before \(1-x\).

## 2. Strict decrease on the real-height first segment

Suppose now \(h_a=h_b=0\).
For \(1/2\le u\le1-x\), put
\[
 y=1-u,\quad S=\sin\pi x,\quad C=\cos\pi x,\quad
 w=\cot\pi y,\quad k=C-Sw .
                                                               \tag{5}
\]
Then \(x\le y\le1/2\), \(0\le w\le C/S\), and \(k\ge0\).
At zero height the exact ratio is
\[
 e^{\mathcal R'(u)}
   =\frac{|\sin\pi(y-x)\sin\pi(y-z)|}
                   {2^\epsilon\sin^{2+\epsilon}\pi y}.
                                                               \tag{6}
\]
For fixed \(x,y\), the maximum of
\(|\sin\pi(y-z)|\) over \(x\le z\le.5\) is at one of
the two endpoints. The sine argument stays in \([-.5,.5]\),
where its absolute value increases with distance from zero.
Hence (6) is at most
\[
                 \frac{\max\{k^2,wk\}}
                              {(2\sin\pi y)^\epsilon}.        \tag{7}
\]

The elementary endpoint bounds imply
\[
 S>\frac3{10},\qquad C<\frac{24}{25},\qquad C+S<\frac32 .
                                                               \tag{8}
\]
For the first two use
\(\sin(\pi/10)=(\sqrt5-1)/4>3/10\) and
\(\cos^2(\pi/10)=(5+\sqrt5)/8<29/32<(24/25)^2\).
Monotonicity gives the bounds at larger \(x\).
The last bound follows from \(C^2+S^2=1\).

For \(\epsilon=0\),
\[
 k^2\le C^2<\frac{576}{625}<1,\qquad
 wk\le\frac{C^2}{4S}<\frac{96}{125}<1.                        \tag{9}
\]
Thus the type-three physical rate decreases throughout this
segment.

For \(\epsilon=1\), retain the extra factor
\(1/(2\sin\pi y)=\sqrt{1+w^2}/2\).
The first alternative in (7) obeys
\[
 \frac{\sqrt{1+w^2}}2(C-Sw)^2
       \le\frac{1+w}{2}(C-Sw)^2<\frac56.                      \tag{10}
\]
To see the strict upper bound, maximize the polynomial on
\(0\le w\le C/S\).
Its only possible nonzero interior maximum is at
\(w=(C-2S)/(3S)\), when that point is nonnegative,
with value \(2(C+S)^3/(27S)<5/6\).
Its endpoint values are \(C^2/2<1/2\) and zero.

For the second alternative use
\(\sqrt{1+w^2}\le w+1/(2w)\), for \(w>0\).
Then
\[
 \begin{split}
 \frac{\sqrt{1+w^2}}2w(C-Sw)
 &\le\frac12w^2(C-Sw)+\frac14(C-Sw)\\
 &\le\frac{2C^3}{27S^2}+\frac C4
 <\frac{4096}{5625}+\frac6{25}
 =\frac{5446}{5625}<1 .
 \end{split}                                                   \tag{11}
\]
The quadratic-times-linear term is maximized at \(2C/(3S)\).
At \(w=0\) the left side is zero, so the conclusion follows
by continuity. This proves strict decrease for type four too,
including all possible real numerator zeros.

The short interval \(49/100\le u\le1/2\) is simpler.
Both shifted real arguments are between \(.59\) and one,
and their sine moduli are at most \(\cos(.09\pi)\).
The own sine is at least \(\cos(.01\pi)\), and
\(2\sin\pi u>1\). Consequently
\[
 e^{\mathcal R'(u)}
 \le\left(\frac{\cos(.09\pi)}{\cos(.01\pi)}\right)^2<1.
                                                               \tag{12}
\]
Together, (9)--(12) prove
\[
 \mathcal R'(u)<0\quad(.49\le u\le1-x),\qquad
 \max_{.49\le u\le1}\mathcal R(u)
       =\max\{\mathcal R(.49),\mathcal R(1)\}
                       \quad(h_a=h_b=0).                     \tag{13}
\]
Integrated-logarithm zeros are retained: the rate is continuous
and strictly decreases through each such zero.

## 3. A uniform open collar, without a chosen numerical width

The set
\[
 \{(x,z,u):.1\le x\le.22,\ x\le z\le.5,\
                                      .49\le u\le1-x\}
                                                               \tag{14}
\]
is compact, and its unshifted sine denominator is bounded away
from zero. On it, equations (9)--(12) bound
\(e^{\mathcal R'(u)}\) by a fixed number strictly less than one.
The exact exponentiated ratio, obtained either from (2) or the
original sine identity, is a continuous function of
\((x,z,u,h_a,h_b)\), including at every numerator zero.

Uniform continuity therefore supplies a fixed
\(\delta>0\) for which
\[
 |h_a|,|h_b|<\delta
       \quad\Longrightarrow\quad
 \mathcal R'(u)<0\quad(.49\le u\le1-x).                        \tag{15}
\]
This assertion uses continuity of the exponentiated ratio, not
a false uniform continuity of its logarithm at zeros.
Apply (4) on the remaining segment, where it holds at all finite
heights. Equation (13), including its endpoint-only maximum,
therefore persists for all heights in (15).

In the actual first-minimum graph,
\[
 h_a=c_a(x-.1)/.12,\qquad
 h_b=c_bR(z)(x-.1)/.12 .
\]
The original coefficients and cutoff are uniformly bounded.
Thus a fixed positive interval \(x\in[.1,.1+\varepsilon]\)
satisfies (15), with the other actual source restrictions retained.
No numerical \(\delta\) or \(\varepsilon\), parameter subdivision,
new root proposal or source evaluation is used.

## 4. Finite-source consequence and remaining comparison

On this collar, the complete adjoining envelope may replace its
quartic/sextic list of high-tail critical values by the two
endpoints \(.49,1\). Its lower physical tail is already paid
by the raised cut \(.22\).
The complete literal finite factor therefore has the same
source upper bound with rates
\[
       \max\{B_{\alpha\epsilon}^{\,0},\
                  \mathcal R(.22),\
                  \mathcal R(.49),\
                  \mathcal R(1)\}.                            \tag{16}
\]
The old zero-safe finite-product argument pays the physical
sum from its whole continuous rate; (13)--(15) do not drop
finite rows or rely on nonvanishing. Polynomial prefactors,
arbitrarily small source tolerance, both level parities and
the original allocations are unchanged.

This is a simplification near the real first-minimum seam.
Away from that small-height collar, the full original list of
interior high-tail critical values remains.
Even in (16), a compensated source sign still needs the actual
coupled neighboring-height comparison and its calibrated endpoint
value. The original middle compensation and relative pinning fee
have not been replaced or paid by this tail reduction.

