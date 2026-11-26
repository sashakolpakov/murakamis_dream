# A stronger summed-coordinate bound during the factorial reset

Research deduction, 6 November 2026. At a factorial maximizer with a
type-three next vertex, the two ordinary index coordinates obey a
stronger summed-real-part restriction throughout the negative and
positive first-height path. This is a bound on the original optimizing
points, not on every point of an independent product rectangle.

## 1. Original phase and scope

Use the four-variable phase \(\mathcal F(e,s,z,b)\) and the original
outgoing affine subtraction from the
[height-envelope proof](research_mixed_selected_boundary_height_envelope.md).
The adjacent vertex has type three, so its flag is \(\epsilon=0\).
It is the ordinary block adjoining the first selected type-four
coordinate of a mixed word of length at least three.
The private and ordinary heights remain their actual reference values,
and
\[
 c\le k:=\Im z\le7/500,\qquad c>-7/100,\qquad
 -13/200<\Im s,\Im b<17/250 .
 \tag{1}
\]
The actual negative reference bound and these ordinary height bounds
are the ones already used in Sections 8 and 12 of that proof.
In particular an attached-endpoint height interval is not substituted
for either ordinary coordinate.

The earlier whole-path factorial bound gives
\[
 .22\le\Re z<3/8,\qquad .2<\Re s\le.5,\qquad
 .22\le\Re b\le.45
 \tag{2}
\]
at every horizontal maximizer. Its proof precedes the stronger
positive-height bounds and does not require \(k\ge0\).
Section 12 also proves strict horizontal concavity on the restricted
box containing these maximizers.

**Proposition.** Every such factorial maximizer satisfies
\[
                         \Re(s+z)<41/50 .
 \tag{3}
\]
The fixed outgoing tangent affects only the real \(b\) derivative,
and the factorial subtraction \(-2\pi k\) is constant during
horizontal maximization. Neither changes the derivative used below.

## 2. The derivative on the proposed boundary

Put
\[
 S_0=e^{-2\pi i s},\quad Z=e^{-2\pi i z},\quad
 B=e^{-2\pi i b},\qquad r=|S_0|,\quad q=|Z|^{-1}.
 \tag{4}
\]
The original logarithmic phase, including \(2\pi izs\), gives
\[
 \exp(2\Re\mathcal F_s)
   =\frac{|1-S_0Z|^2\,|1-S_0B|^2}
          {|Z|^2\,|1-S_0|^4}.
 \tag{5}
\]
In particular the factor \(|Z|^{-2}\) is retained.

Suppose first that \(\Re(s+z)=41/50\). By (2),
\(\Re s\in(89/200,1/2]\). Throughout this boundary,
\[
 \begin{split}
 \cos(2\pi\Re(s+z))&>2/5,\\
 \cos(2\pi\Re(s+b))&>-3/5,\\
 \cos(2\pi\Re s)&<-47/50 .
 \end{split}
 \tag{6}
\]
For explicit witnesses, the first cosine is
\(\sin(7\pi/50)>\sin(7/16)>2/5\), by
\(\pi>25/8\) and the cubic sine lower bound.
For the second, \(\Re(s+b)\in(133/200,.95]\);
its cosine is bounded below by
\(-\sin(17\pi/100)>-\sin(\pi/5)>-3/5\).
The last trigonometric inequality follows from
\(\sin^2(\pi/5)=(5-\sqrt5)/8<9/25\).
For the third, \(\pi<22/7\) gives
\[
 \cos(11\pi/100)>
 1-\frac12(121/350)^2
 =\frac{47}{50}+\frac{59}{245000}.
 \tag{7}
\]

The height bounds in (1) imply
\[
          \frac{13}{20}<r<\frac85,\qquad
          0<q<\frac{39}{25},\qquad |B|<\frac85 .
 \tag{8}
\]
These require only elementary exponential bounds. For \(0<x<3\),
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)}.
 \tag{9}
\]
At \(x=41/100\) the right side is less than \(20/13\);
at \(x=11/25\) it is \(4971/3200<39/25<8/5\).
Use \(.13\pi<.41\), \(.14\pi<.44\), and
\(.136\pi<.44\) to obtain (8).

Equations (6)--(8) give
\[
 \begin{split}
 \frac{|1-S_0Z|^2}{|Z|^2}
   &<r^2-\frac{156}{125}r+\frac{1521}{625},\\
 |1-S_0B|^2&<1+\frac{64}{25}r^2+\frac{48}{25}r,\\
 |1-S_0|^2&>1+r^2+\frac{47}{25}r.
 \end{split}
 \tag{10}
\]
For the first inequality, bound the left side by
\(q^2+r^2-4qr/5\). This is convex in
\(q\in[0,39/25]\). The upper endpoint gives the larger value,
because \(1521/625-156r/125>0\) for \(r\le8/5\).
For the second, its polynomial upper bound is increasing in
\(|B|\ge0\), so \(|B|<8/5\) applies directly.

The squared denominator in (5) exceeds the product of the two
numerator bounds. Indeed their exact difference is
\[
 \begin{split}
 P(r)
 :={}&(1+r^2+47r/25)^2\\
 &-(r^2-156r/125+1521/625)
                         (1+64r^2/25+48r/25)\\
 ={}&-\frac{39}{25}r^4+\frac{15734}{3125}r^3
       +\frac{10946}{15625}r^2+\frac{5242}{15625}r
       -\frac{896}{625}>0
             \qquad(13/20\le r\le8/5).
 \end{split}
 \tag{11}
\]
To check the sign without a numerical enclosure, group the leading
terms of its derivative as
\[
 P'(r)=r^2\left(\frac{47202}{3125}-\frac{156}{25}r\right)
                +\frac{21892}{15625}r+\frac{5242}{15625}>0.
 \tag{12}
\]
At the left endpoint,
\(P(13/20)=18468121/100000000>9/50\).
Thus (5) is strictly less than one on the entire proposed boundary:
\(\Re\mathcal F_s<0\).

## 3. Exclusion of the larger sum

Suppose a horizontal maximizer had \(\Re(s+z)\ge41/50\).
Hold \(e,z,b\) and all heights fixed, and decrease \(\Re s\)
to \(41/50-\Re z\). This boundary point belongs to the original
real \(s\) interval: its real part is greater than \(89/200\)
and no greater than the hypothetical maximizing value, which is
at most \(1/2\).

The preceding calculation makes the real \(s\) derivative strictly
negative at that boundary. The already-proved conditional horizontal
concavity makes this derivative decrease further as \(\Re s\)
increases. A small decrease of \(\Re s\) would therefore increase
the original objective, including at equality. This contradicts
maximality and proves (3).

The new bound is available on the whole factorial height path,
including its negative portion. It improves an off-diagonal argument
restriction in the effective-curvature formula. It does not itself
prove the required \(6\pi\) curvature inequality, constrain the
forced branch without its own coordinate hypotheses, or estimate
any omitted finite-source current.

## 4. Signs of the two private response entries

The bound also places the two summed arguments in their cotangent
strips throughout this factorial path:
\[
 \left|\Im\cot\pi(s+z)\right|<1,\qquad
                  0<\Im\cot\pi(e+z)<1.
 \tag{13}
\]
Indeed, for real \(x,y\), the exact cotangent formula gives
\[
 |\Im\cot\pi(x+iy)|<1
       \quad\Longleftrightarrow\quad
              \cos(2\pi x)<e^{-2\pi|y|}.
 \tag{14}
\]
For \(s+z\), the proved restrictions give
\(.42<\Re(s+z)<.82\) and \(|\Im(s+z)|<.135\).
Its cosine is therefore at most \(\sin(.14\pi)\), and
\[
 \sin(.14\pi)
 <\frac{499148551}{1171875000}<\frac{213}{500}
 <\frac{427}{1000}<e^{-.27\pi}.
 \tag{15}
\]
The first rational number is the upper sine Taylor polynomial
\(x-x^3/6+x^5/120\) at \(x=11/25>.14\pi\).
For the last bound, \(.27\pi<17/20\) and
\[
 e^{17/20}
 \le1+\frac{17}{20}+\frac{(17/20)^2}{2}
       +\frac{(17/20)^3}{6}
       +\frac{(17/20)^4}{24(1-17/100)}
 =\frac{37287201}{15936000}<\frac{1000}{427}.
 \tag{16}
\]
The final cross-product difference is the positive integer
\(14365173\).

For \(e+z\), the actual private heights and the whole-path
factorial bounds give
\[
 .52<\Re(e+z)<.775,\qquad
                  -.121<\Im(e+z)<-.005.
 \tag{17}
\]
Its cosine is at most \(\sin(\pi/20)<1/5\), whereas
\(e^{-2\pi|\Im(e+z)|}>e^{-.8}>2/5\).
For example (9) at \(x=4/5\) bounds \(e^{.8}\) by
\(123/55<5/2\). Equation (14) applies; the negative height
in (17) makes its imaginary cotangent strictly positive.

Consequently the two private entries of the normalized imaginary
Hessian column in the height-envelope formula satisfy
\[
 q_e=1-\Im\cot\pi(e+z)\in(0,1),\qquad
 q_s=-1-\Im\cot\pi(s+z)\in(-2,0).
 \tag{18}
\]
These are pointwise signs and bounds along the original optimizing
path. They do not assert a sign for its full Schur determinant or
establish an invariant flow region.
