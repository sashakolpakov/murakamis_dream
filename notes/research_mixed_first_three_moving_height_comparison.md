# A paid moving-height comparison for the first type-three cap

Research deduction, 7 November 2026. After the analytic low-index
barrier, the complete first-type-three cap envelope and its adjoining
central or real-cut profile increase with slope greater than \(1/20\)
under the actual affine first-height change. The ordinary contour
height is fixed and nonpositive, and the next retained target is held
fixed. The cap's true-index alternative is included.

The statement covers the central contribution for every adjoining
type-four block, and the nonpositive-index-height subfamily of an
adjoining type-three block. Both real cuts are covered for either
adjoining type. The other high physical-tail profiles and the
neighboring-height contribution remain separate.

## 1. The reduced regular derivative

Use exactly the source, common parameter and allocations of the
[moving-height reduction](research_mixed_first_attached_moving_height_reduction.md).
Here the first cap has type three, so \(\alpha=0\), and
\[
 \begin{gathered}
 a=x+ih,\quad h=c(x-.1)/.12,\quad -.072<c<.021,\quad
             \lambda=-c/.12,\\
 .1\le x\le.22,\qquad e\in[.27,.49],\qquad
 s=v+i\eta,\quad \eta\in[-.108,0].
 \end{gathered}
 \tag{1}
\]
The fixed neighboring target retains the actual quadratic upper
cutoff and other hypotheses of the
[raised-index barrier](research_mixed_first_attached_index_barrier.md).
That theorem permits the central interval \(v\in[.22,.49]\),
with the physical lower cut at \(.22\).

For \(b\) fixed, the regular joint derivative is
\[
 \mathcal H_0
 =\Re\!\left[(1-i\lambda)
   \{g'(e+a)+g'(s+a)-2g'(a)+2\pi i s\}\right].
 \tag{2}
\]
The height reduction and endpoint-minimum arguments already proved
reduce its lower bound to \(\eta=0\),
\(e=.27,.49\), and \(v=.22,.49\). At \(v=.49\) the
uniform bound is \(43/500>1/20\). We therefore need only the
lower ordinary endpoint \(v=.22\).

## 2. A real-part lower bound when the first height is negative

Suppose \(c\le0\), so \(0\le\lambda<3/5\) and \(r=e^{2\pi h}\le1\).
One also has
\[
                              r>\frac35.
 \tag{3}
\]
Indeed \(2\pi|h|<.144\pi<1/2\), and the elementary bound
\[
 e^{1/2}\le1+\frac12+
                 \frac{(1/2)^2}{2(1-(1/2)/3)}
                =\frac{33}{20}<\frac53
 \tag{4}
\]
proves (3).

For a moment keep \(r\in[3/5,1]\) fixed while varying \(x\).
Put \(C=(r+r^{-1})/2\le17/15\). The real cotangent
\[
                 \frac{\sin(2\pi x)}{C-\cos(2\pi x)}
 \tag{5}
\]
has no interior minimum on \([.1,.22]\): its derivative has
the sign of \(C\cos(2\pi x)-1\), which decreases with \(x\).
At \(x=.1\), use \(\sin(.2\pi)>1/2\) and
\(\cos(.2\pi)>4/5\) to bound (5) below by \(3/2\).
At \(x=.22\), the old elementary bounds give
\[
 (5)>\frac{49/50}{17/15-9/50}
                         =\frac{147}{143}>1 .
 \tag{6}
\]
Hence \(\Re\cot\pi a>1\) at every intermediate \(x\).

Both shifted real arguments \(e+x\in[.37,.71]\) and
\(.22+x\in[.32,.44]\) have negative angular cosine.
Their real cotangents are strictly less than one: the denominator
in (5) is greater than one, and the numerator is at most one
(or is negative). Therefore, for fixed \(r,e\),
\[
 x\longmapsto
 \Re\{g'(e+a)+g'(.22+a)-2g'(a)\}
 \quad\hbox{is strictly decreasing on }[.1,.22].
 \tag{7}
\]
Only a real-part comparison is being integrated here. It does not
replace the actual relation between \(r,c,x\) in the moving derivative.

At the resulting endpoint \(x=.22\), the first numerator modulus
is minimized over \(e\in[.27,.49]\) at \(e=.49\).
For any fixed pair of angles with \(c_d>c_n\), direct differentiation
gives
\[
 \frac{d}{dr}
     \frac{1+r^2-2c_n r}{1+r^2-2c_d r}
       =\frac{2(c_d-c_n)(1-r^2)}
                    {(1+r^2-2c_d r)^2}\ge0 .
 \tag{8}
\]
Thus both numerator-to-denominator squared-modulus ratios in (7)
are bounded below by their values at \(r=3/5\).
Use
\[
 -\cos(1.42\pi)>\frac6{25},\qquad
 -\cos(.88\pi)>\frac{23}{25},\qquad
 \cos(.44\pi)>\frac9{50}.
 \tag{9}
\]
These are the existing sine/cosine witnesses in the raised-index and
cap half-stencil proofs. With \(r=3/5\), they give the three squared
moduli
\[
             A>\frac{206}{125},\qquad
             C_1>\frac{308}{125},\qquad
             B<\frac{143}{125}.
 \tag{10}
\]
Consequently the real part in (7), at every actual point under
consideration, is greater than
\[
 \frac12\log\frac{63448}{20449}
            >\frac12\log\frac{31}{10}
            >\frac{11023}{19680}.
 \tag{11}
\]
The first ratio comparison has cross-product difference \(561>0\).
For the last inequality use
\[
 \frac12\log(31/10)
  =\operatorname{atanh}(21/41)
  >\frac{21}{41}+\frac1{24}+\frac1{160}
  =\frac{11023}{19680};
 \tag{12}
\]
the last two terms are smaller than the cubic and quintic terms
of the positive atanh series, since \(21/41>1/2\).

## 3. The actual imaginary part pays the moving switch

The rotated-ratio argument from Proposition 2 of the moving-height
note applies to both shifts \(e\) and \(v=.22\). Indeed
\(0<\pi w<2\pi x+\pi w<\pi\) for \(w=e,.22\).
With the original lifts, it gives
\[
 \begin{array}{ll}
 r\le1:&\Im\{g'(w+a)-g'(a)\}\ge-\pi w,\\
 r\ge1:&\Im\{g'(w+a)-g'(a)\}\le-\pi w.
 \end{array}
 \tag{13}
\]
For \(c\le0\), the imaginary part of the braces in (2) is
therefore at least \(\pi(.22-e)\).
Since \(e\le.49\), \(\lambda<3/5\), and \(\pi<22/7\),
(11) implies
\[
 \mathcal H_0(e,.22,0;x,c)
  >\frac{11023}{19680}-\frac{891}{1750}
  >\frac1{20}.
 \tag{14}
\]
The final comparison is exact:
\[
 11023\cdot3500-1957\cdot19680=66740>0.
 \tag{15}
\]

If \(c\ge0\), then \(\lambda\le0\), \(r\ge1\).
Now (13) bounds the imaginary part of the braces in (2) above by
\(\pi(.22-e)<0\). Its product with \(\lambda\) is nonnegative.
The fixed-height joint bound gives its real part greater than
\(21/121\). Hence (14) holds in this case too, with additional
room. At \(c=0\) the conclusions agree.

Combining the two lower endpoints (14), the already paid upper
endpoint, and the exact \(\eta\) and private-coordinate reductions
proves the following uniform statement.

**Theorem 1.** Under (1) and the actual target hypotheses above,
\[
               \mathcal H_0(e,v,\eta;x,c)>\frac1{20}
 \quad\bigl(e\in[.27,.49],\ v\in[.22,.49],\
                                     -.108\le\eta\le0\bigr).
 \tag{16}
\]
No original conditional root is replaced, and no independent
large-height source packet is invoked.

## 4. Complete-envelope transport and its precise scope

The own-three true-end alternative has moving derivative greater
than \(21/242>1/20\), by Proposition 2 of the moving-height note.
Thus both alternatives of the complete cap envelope obey the same
strict lower slope when combined with the adjoining central profile
or either real cut \(.22,.49\).

For the central expression use the unchanged maximum \(B^0\) on
the raised index interval. For a cut use its fixed zero-height
ordinary index. Integration of each fixed private profile, followed
by its maximum, proves
\[
 \mathcal E(x_0)\le\mathcal E(x_1)-\frac{x_1-x_0}{20},
                    \qquad .1\le x_0<x_1\le.22 .
 \tag{17}
\]
Here \(h=c(x-.1)/.12\) changes as written, whereas \(b,\eta\)
and the ordinary-color parameter remain fixed. The cap angular
constant is chosen uniformly on this compact family; its angular
term is unchanged. There is no differentiability assumption on a
maximizing index, and the cap true-end exponent is not discarded.

The central statement covers every adjoining own-four factor,
whose original ordinary index height is negative. For an adjoining
own-three factor it covers only the nonpositive-index-height
subfamily. The real-cut comparisons have \(\eta=0\), so they apply
to both adjoining types. The first cap throughout has own type three.

Equation (17) is not yet the actual full minimum-neighbor move.
That move can also change \(b\)'s height; its two-incidence
contribution is exactly (23) of the moving-height note. The other
high physical-tail alternatives remain in the finite-source
envelope. Nor is the rate at the frozen-height comparison endpoint
identified with the calibrated boundary action. The protected
middle compensation and relative pinning fee retain their original
values and roles. No complete compensated boundary sign or
whole-source lower bound is inferred.
