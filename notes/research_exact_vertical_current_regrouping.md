# Regrouping the original vertical currents before taking a modulus

Research deduction, 7 November 2026. Moving the zero-frequency
integral to its original negative saddle height changes the exact
vertical coefficient. Combining that change with the cotangent
current gives an exponential penalty below the saddle height. This
is an identity of the original finite source, not a new contour or
a sign estimate for its remaining profiles.

## 1. The finite one-index identity

Let \(N\ge2\), let \(a,b\) be half-grid endpoints, and let
\(F\) be holomorphic on a neighborhood of
\([a,b]+i[h_-,h_+]\). Assume
\[
                     h_-<h_0<0<h_+.
 \tag{1}
\]
Write \(\Delta F(y)=F(b+iy)-F(a+iy)\). The lower-base
residue formula, equation (6) of
[the exact mixed contour identity](research_mixed_pair_full_period_contour.md),
applies with these possibly asymmetric top and bottom heights:
\[
\begin{split}
 \sum_{a<j/N<b}F(j/N)
 ={}&N\int_a^b\frac{F(x+ih_-)}{1-e^{-2\pi iN(x+ih_-)}}\,dx\\
 &+N\int_a^b F(x+ih_+)
       \frac{e^{2\pi iN(x+ih_+)}}{1-e^{2\pi iN(x+ih_+)}}\,dx\\
 &+iN\int_{h_-}^{h_+}
                \frac{\Delta F(y)}{1+e^{2\pi Ny}}\,dy.
\end{split}
 \tag{2}
\]
Indeed the same rectangular residue calculation uses only the
half-grid condition at the two vertical sides; it does not require
\(h_+=-h_-\).

Split the first denominator into its constant term and its full
lower alias. Cauchy's theorem, with the original orientations,
gives
\[
 \int_a^b F(x+ih_-)\,dx
 =\int_a^b F(x+ih_0)\,dx
                  -i\int_{h_-}^{h_0}\Delta F(y)\,dy.
 \tag{3}
\]
Consequently (2) is exactly
\[
\begin{split}
 \sum_{a<j/N<b}F(j/N)
 ={}&N\int_a^bF(x+ih_0)\,dx\\
 &+N\int_a^bF(x+ih_-)
       \frac{e^{-2\pi iN(x+ih_-)}}{1-e^{-2\pi iN(x+ih_-)}}\,dx\\
 &+N\int_a^bF(x+ih_+)
       \frac{e^{2\pi iN(x+ih_+)}}{1-e^{2\pi iN(x+ih_+)}}\,dx\\
 &+iN\int_{h_-}^{h_+}w_{N,h_0}(y)\Delta F(y)\,dy,
\end{split}
 \tag{4}
\]
where the value at \(y=h_0\) is immaterial and
\[
 w_{N,h_0}(y)=\frac1{1+e^{2\pi Ny}}
                      -\boldsymbol1_{\{y<h_0\}}.
 \tag{5}
\]
In particular the negative sign of the lower piece is retained.
The subtraction in (5) occurs before a modulus is taken; bounding
the two terms separately would lose its decay.

## 2. The resulting vertical penalties

The elementary bounds following directly from (5) are
\[
 |w_{N,h_0}(y)|\le
 \begin{cases}
 e^{2\pi Ny},&h_-\le y<h_0,\\
 1,&h_0<y\le0,\\
 e^{-2\pi Ny},&0\le y\le h_+.
 \end{cases}
 \tag{6}
\]
Thus the rate debit on either vertical side may be taken to be
\[
 \ell_{h_0}(y)=
 \begin{cases}
 2\pi|y|,&y<h_0,\\
 0,&h_0\le y\le0,\\
 2\pi y,&y\ge0.
 \end{cases}
 \tag{7}
\]
At the cut \(h_0\), use the larger containing upper from either
closed piece when taking a supremum. There is no assertion of a
positive debit along the segment from the saddle height to zero.
The two horizontal aliases retain their usual debits
\(2\pi|h_-|\) and \(2\pi h_+\): their denominators are bounded
away from zero for all sufficiently large \(N\).

The identity holds with arbitrary additional holomorphic parameters.
It can therefore be applied successively in each index, before any
modulus is taken. Tensoring (4) retains every horizontal, vertical
and corner contribution and every original scalar. In a rate bound,
each vertical coordinate contributes its own (7). Fixed derivatives
in the other parameters commute with the finite identity.

## 3. Scope for the original paired Fourier source

The regular rectangles and fixed negative main heights in
[the paired-period criterion](research_mixed_paired_fourier_period_criterion.md)
satisfy (1). Its regularity lemma permits (4) for both original
index variables of either vertex, uniformly on the full shared-wire
period. In its equations (8)--(9), one may therefore replace the
zero debit assigned to an entire vertical side by the piecewise
debit (7), splitting the side at \(h_0\) and zero when needed.
This improves a containing bound without changing the original
finite source, its Fourier prefactors, its log lifts, or the exact
polynomial periodicity.

The physical triangular complement in that criterion is unchanged.
No complementary-period sign follows from (7) alone, and no
control of a whole paired kernel or of an actual cap message is
asserted here. In particular the real-height endpoints and the
segment \([h_0,0]\) still require their own comparison.
