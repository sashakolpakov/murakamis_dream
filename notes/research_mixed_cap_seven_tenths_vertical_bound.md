# A complete cap bound on the vertical line at seven tenths

Research deduction, 8 November 2026. The complete original cap has
exponential upper rate \(3907/4500<7/8\) throughout the incoming
vertical segment with real part \(7/10\) and height between
\(-9/125\) and zero. The proof estimates its physical rows, keeping
each entire endpoint coefficient coherent. A curvature estimate for
that coefficient compensates for the positive part of the incoming
product.

No cap critical point or contour deformation is needed for this upper
bound. Every physical row, both true index ends, both level parities
and all real ordinary colors are retained. No numerical evaluation
or change to a frozen proof is used.

## 1. The original finite sum and its row rates

Keep
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
                 H_N(w,r^{-j})\,p_j(X)/P_j,\\
 a=7/10-i\eta,\qquad 0\le\eta\le9/125,\qquad
 X=e^{-2\pi ia},\qquad R=|X|=e^{-2\pi\eta}.
 \end{gathered}
 \tag{1}
\]
The coefficient \(H_N\) is the whole original endpoint polynomial,
including all its Newton terms and ordinary normal. The existing
depth bound gives
\[
                              5/8<R\le1.
 \tag{2}
\]
Indeed \(\log(8/5)>6/13>18\pi/125\), using
\(\pi<22/7\).

Let \(J\) be the original sine primitive, let
\(\lambda(e)=\Re S(e)\) be the original complete-color endpoint
action at a real physical private index, and put
\[
 h(e)=\lambda(e)+J(e),\qquad
 f_R(s)=\log|1-Re^{-2\pi is}|,\qquad
 I_R(e)=\int_{7/10}^{7/10+e} f_R(s)\,ds .
 \tag{3}
\]
At \(R=1\) the integrals are understood through the integrable
logarithmic zeros.

On every compact physical private interval \(e=j/N\in I\Subset(0,1)\),
the original coefficient and zero-safe product bounds supply
\[
 \left|H_N(w,r^{-j})p_j(X)/P_j\right|
 \le C_\tau N^{B_\tau}
       e^{N\{\lambda(e)+I_R(e)+\tau\}},
                    \qquad -2\le w\le2.
 \tag{4}
\]
This is precisely the compact-index source in Section 2 of
[all-real complementary completion](research_mixed_three_four_complementary_real_colors.md).
Its true-end bound, equation (6), separately gives a fixed sufficiently
small \(\delta_0>0\) such that
\[
 \sum_{\substack{0\le j<N\\ j/N\le\delta_0\ {\rm or}\ j/N\ge1-\delta_0}}
       |H_N(w,r^{-j})p_j(X)/P_j|
 \le C N^B e^{3N/5}
                    \qquad(|X|\le1,\ -2\le w\le2).
 \tag{5}
\]
Thus no compact endpoint asymptotic will be extended to zero or one.

## 2. Three elementary bounds for the incoming integral

First consider \(7/10\le s\le5/6\).
Here \(\cos(2\pi s)\le1/2<R\), so
\(1+R^2-2R\cos(2\pi s)\) increases with \(R\).
Consequently
\[
 f_R(s)\le f_1(s)=\log(2\sin\pi s).
 \tag{6}
\]
The latter function is nonnegative on this interval and concave,
with value \(\tfrac12\log2\) and derivative \(-\pi\) at \(s=3/4\).
Its tangent gives
\[
 \begin{split}
 \int_{7/10}^{5/6} f_1(s)\,ds
 &\le \frac2{15}\left(\frac12\log2-\frac{\pi}{60}\right)\\
 &<\frac2{15}\left(\frac7{20}-\frac5{96}\right)
   =\frac{143}{3600}<\frac1{25}.
 \end{split}
 \tag{7}
\]
Only \(\log2<7/10\) and \(\pi>25/8\) are used.
On \(5/6\le s\le9/10\), one has \(\cos(2\pi s)\ge1/2\), hence
\[
 |1-Re^{-2\pi is}|^2\le1+R^2-R\le1,\qquad f_R(s)\le0.
 \tag{8}
\]
Since the upper comparison in (6) is nonnegative, (7)--(8)
also bound every shorter integral beginning at \(7/10\).

Next, for \(9/10\le s\le11/10\),
\(\cos(2\pi s)\ge\cos(\pi/5)>4/5\).
The squared modulus is convex in \(R\), so its maximum on
\([5/8,1]\) is at an endpoint. At those endpoints its upper
bounds are respectively
\[
 1+\frac{25}{64}-\frac54\frac45=\frac{25}{64}<\frac25,
                  \qquad 2-\frac85=\frac25.
 \tag{9}
\]
The cosine inequality is strict, and therefore
\[
 f_R(s)<\frac12\log(2/5)<-\frac25.
 \tag{10}
\]
For the last step, the elementary inequality
\(\log(5/2)>2((5/2)-1)/((5/2)+1)=6/7>4/5\) suffices.

Finally, for \(11/10\le s\le6/5\),
\(\cos(2\pi s)\ge\cos(2\pi/5)>3/10\).
The same convexity in \(R\) bounds the two endpoint squares by
\[
 1+\frac{25}{64}-\frac54\frac3{10}=\frac{65}{64}
                       <\frac{36}{25},
 \qquad
 2-\frac35=\frac75<\frac{36}{25}.
 \tag{11}
\]
Thus \(f_R(s)<\log(6/5)<1/5\) on this last interval.
Equations (7)--(11) prove the following bounds, all uniform in \(R\):
\[
 I_R(e)\le
 \begin{cases}
   1/25,&0\le e\le1/5,\\
   1/25-(2/5)(e-1/5),&1/5\le e\le2/5,\\
   -1/50,&2/5\le e\le1/2.
 \end{cases}
 \tag{12}
\]
For the third bound, the integral through \(11/10\) is at most
\(1/25-(2/5)(1/5)=-1/25\), and its remaining length is at most
\(1/10\), at rate at most \(1/5\).
All bounds include the case \(R=1\), by direct integration or
continuity through its zeros.

## 3. Curvature of the complete coefficient

The exact calculation in Section 2 of
[the coherent far-arc cap estimate](research_mixed_next_coherent_cap_far_arc.md)
proves
\[
                            -h''(e)>18/5
                         \qquad(0<e<1/2).
 \tag{13}
\]
Since \(J''(e)=\pi\cot\pi e>0\) there and
\(\lambda=h-J\), it follows that \(-\lambda''(e)>18/5\).
Taylor's formula about \(e_0=7/20\) therefore gives
\[
 \lambda(e)\le\lambda(e_0)+\lambda'(e_0)(e-e_0)
                              -\frac95(e-e_0)^2.
 \tag{14}
\]
The already established scalar consequences in
[the cap seam source bound](research_mixed_cap_seam_source_bounds.md),
equation (7), are
\[
 \lambda'(e_0)<0,\qquad
 \lambda(e_0)-e_0\lambda'(e_0)<433/500 .
 \tag{15}
\]
For \(e>0\), (14)--(15) imply the useful uniform bound
\[
                 \lambda(e)<\frac{433}{500}
                                      -\frac95(e-7/20)^2.
 \tag{16}
\]
These are direct written deductions from the existing source
inequalities. No scalar value, derivative or saved result is
evaluated again.

For \(0<e\le1/5\), combine (12) and (16):
\[
 \lambda(e)+I_R(e)
 <\frac{433}{500}+\frac1{25}
                     -\frac95\left(\frac3{20}\right)^2
 =\frac{1731}{2000}<\frac{3907}{4500}.
 \tag{17}
\]
For \(1/5\le e\le2/5\), put \(u=e-7/20\). The same bounds give
\[
 \begin{split}
 \lambda(e)+I_R(e)
 &<\frac{433}{500}-\frac1{50}-\frac25u-\frac95u^2\\
 &\le\frac{433}{500}-\frac1{50}+\frac1{45}
   =\frac{3907}{4500}.
 \end{split}
 \tag{18}
\]
The second line is the exact maximum of the displayed real quadratic.
For \(2/5\le e<1/2\), the cruder bound
\(\lambda(e)<433/500\), together with (12), gives a rate
less than \(423/500<3907/4500\).

For the upper physical half use the existing radial comparison:
\[
 I_R(e)\le J(e),\qquad
 \lambda(e)+I_R(e)\le h(e)\le h(1/2)<101/125,
                       \qquad 1/2\le e<1.
 \tag{19}
\]
The first inequality is equation (9) of
[the far-half radial cap theorem](research_mixed_three_four_far_half_cap_radial_extension.md);
the monotonicity of \(h\) above one half is equation (5) of the
cap seam source bound. This completes the estimate of every compact
physical private index.

## 4. Complete finite-source conclusion

**Theorem.** For every prescribed \(\tau>0\), all sufficiently
large \(N\), both level parities, and uniformly for
\(0\le\eta\le9/125\),
\[
 \boxed{\quad
 \sup_{-2\le w\le2}
 |U_{0,N}(w,e^{-2\pi i(7/10-i\eta)})|
 \le C_\tau N^{B_\tau}
       e^{N(3907/4500+\tau)}.
 \quad}
 \tag{20}
\]
Indeed (17)--(19) bound all compact rows in (4), and the two true
ends have the smaller rate \(3/5\) by (5).
There are only \(N\) physical rows, so summing their positive
upper bounds adds only a polynomial factor. Every \(H_N\) remains
its complete coherent coefficient.

Fixed ordinary-color derivatives follow from the complete
all-real polynomial bound by Markov's inequality. The existing
complex-color coefficient bounds give a sufficiently small fixed
neighborhood of complete color for any prescribed extra tolerance.
The zero-safe integral rates are jointly continuous in the incoming
parameter, including numerator zeros. At each base point retain
the same physical index groups, extend their bounds to a small
fixed neighborhood, and use Cauchy's formula on radius \(1/N\).
This gives fixed incoming and mixed derivatives with polynomial
costs and an arbitrarily small extra rate. The true ends retain
their original slightly enlarged disk estimates.

The strict scalar reserve relevant to the actual following
calibration is
\[
                  \frac78-\frac{3907}{4500}=\frac{61}{9000}>0.
 \tag{21}
\]
In particular the newly proved actual cap-plane floor \(B_*>7/8\)
would place (20) below that unchanged plane. Applying it to the
selected source still requires the original conditional factor,
its height and horizontal comparisons, the third factor and both
selected-weight alternatives. Those factors are not part of the
cap theorem (20), and no knot-family statement is inferred from
this bound alone.
