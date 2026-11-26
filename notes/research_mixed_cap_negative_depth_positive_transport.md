# A complete cap upper bound on a negative-height incoming strip

Research deduction, 8 November 2026. A quantitative angular decrease
of the literal incoming numerator pays the complete cap on
\[
             14/25\le x\le33/50,\qquad -9/125\le h\le0.
\]
The depth is the full actual incoming depth, not a small complex
neighborhood of the real axis. The proof bounds the original sum
of complete endpoint coefficients times its exact finite products.
It includes the private rows beyond the moving real numerator wall.

No negative-height cap critical-point enclosure or relative packet
is required. The interval \(1/2\le x<14/25\), a comparison with the
following affine action, and a whole incoming contour deformation
remain separate. No numerical evaluation or frozen-source edit is used.

## 1. The literal source and existing physical coefficient bounds

Keep
\[
\begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\quad X=e^{-2\pi i(x+ih)},\\
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
                 H_N(w,r^{-j})\,p_j(X)/P_j,\qquad
 R=|X|=e^{2\pi h}.
\end{gathered}
\tag{1}
\]
Each \(H_N\) is the complete original endpoint polynomial,
with its ordinary normal and all Newton rows retained.

Write \(J(e)=\int_0^e\log(2\sin\pi s)\,ds\),
\(\lambda(e)=\Re S(e)\), and
\[
 I_{x,R}(e)=\int_0^e\log|1-Re^{-2\pi i(x+s)}|\,ds .
\tag{2}
\]
The complete physical coefficient and zero-safe product bounds in
[all-real complementary completion, Section 2](research_mixed_three_four_complementary_real_colors.md)
give the rate
\[
                         \lambda(e)+I_{x,R}(e)
\tag{3}
\]
on every compact physical private-index interval. They hold uniformly
for real ordinary colors \(w\in[-2,2]\) and for \(R\) in a compact
positive interval. In particular they are not a positive bound on
the separate Newton terms inside \(H_N\).

The two true private ends have the separate full-disk positive
bound in that source, equation (6), with rate \(3/5\). Thus (3)
is never extrapolated to zero or one. The same source and the
[exact radial comparison](research_mixed_three_four_far_half_cap_radial_extension.md),
equation (9), supply
\[
\begin{split}
 I_{x,R}(e)&\le -J(1/2-e),&&0\le e\le1/2,\\
 I_{x,R}(e)&\le J(e),&&1/2\le e\le1,
\end{split}
\quad
             1/2\le x\le1,\quad0<R\le1.
\tag{4}
\]
These are continuous integral bounds through all numerator zeros.

Set
\[
 B_0=\frac{1549}{1500},\qquad b_0=\frac{101}{125},\qquad
 \widehat M=\frac{203}{200}-\frac{1303}{7680000}.
\tag{5}
\]
The accepted physical coefficient bounds imply
\[
 \lambda(e)-J(1/2-e)<B_0\quad(0<e<1/2),\qquad
 \lambda(e)+J(e)<b_0\quad(1/2\le e<1).
\tag{6}
\]
The half-face critical action satisfies \(M_{\rm half}<\widehat M\),
by [the complete cap action bound](research_mixed_half_face_cap_action_upper.md).

A sharper sourcewise bound is available on the lower private sector.
Put \(c_L=27/100\) and
\[
 \phi(e)=\lambda(e)-J(1/2-e),\qquad L=\phi(c_L).
\tag{7}
\]
Equations (14) and the following curvature argument in
[the real-arc complete cap bound](research_mixed_real_arc_complete_cap_upper.md)
prove
\[
              \phi(e)\le L<M_{\rm half}\qquad(0<e\le c_L).
\tag{8}
\]
The argument is the original real-cut cone at \(c_L\), followed by
strict real concavity and \(\phi'(c_L)>0\). It bounds the full
physical coefficient rate, not a term recovered by subtraction
from a signed cap estimate. All real ordinary colors are covered
by the coefficient source already used in (3).

## 2. A uniform angular derivative for the entire middle private band

For the actual depth,
\[
 R\ge e^{-18\pi/125}>\frac58.
\tag{9}
\]
Indeed
\(\log(8/5)>6/13>18\pi/125\), by the positive logarithm
series or its first inverse-hyperbolic-tangent term and
\(\pi<22/7\). The last rational comparison is \(5250>5148\).

**Lemma 1.** For
\[
 \frac58\le R\le1,\quad
 0\le d\le\frac4{25},\quad
 \frac{27}{100}\le e\le\frac12,
\]
one has, at every nonsingular endpoint,
\[
 \partial_x I_{x,R}(e)\big|_{x=1/2+d}
 \le\frac12\log\frac{89}{169}<-\frac{40}{129}.
\tag{10}
\]
The corresponding integrated inequality holds through the singular
endpoints at \(R=1\).

*Proof.* Define
\[
 f_R(s)=\log|1+Re^{-2\pi is}|,\qquad A=1+R^2.
\]
The exact derivative of (2) is
\[
 \partial_x I_{x,R}(e)=f_R(d+e)-f_R(d).
\tag{11}
\]
For fixed \(d\), the squared numerator
\(A+2R\cos(2\pi(d+e))\) attains its maximum over
\(c_L\le e\le1/2\) at one of the two ends. This follows
because the angle interval lies inside \((0,2\pi)\) and
the only interior turning point of its cosine there is
its minimum at \(d+e=1/2\).

First take \(e=c_L\). More generally, for \(0<q<1/2\),
the function
\[
                         f_R(d+q)-f_R(d)
\]
on \(0\le d\le1/2-q\) has no interior maximum. For \(R<1\),
the sign of its derivative is the opposite of the sign of
\[
             A\cos(2\pi d+\pi q)+2R\cos(\pi q).
\tag{12}
\]
This expression strictly decreases with \(d\), so the derivative
can change only from negative to positive. The larger endpoint
value is the one at zero, since
\[
 (1-R)^2(1+R)^2
 \le (A-2R\cos2\pi q)(A+2R\cos2\pi q).
\tag{13}
\]
The difference on the right is \(4R^2\sin^2(2\pi q)\).
The argument extends to \(R=1\) by a limit; values at zeros
are interpreted as minus infinity. As \(4/25<1/2-c_L\),
we obtain
\[
 \exp\{2[f_R(d+c_L)-f_R(d)]\}
 \le\frac{A+2R\cos(2\pi c_L)}{(1+R)^2}
 <\frac{A}{(1+R)^2}
 \le\frac{89}{169}.
\tag{14}
\]
Here \(\cos(2\pi c_L)<0\), and
\(R/(1+R)^2\) increases on \([5/8,1]\).

For the other endpoint \(e=1/2\),
\[
 \exp\{2[f_R(d+1/2)-f_R(d)]\}
 =\frac{A-2R\cos2\pi d}{A+2R\cos2\pi d}
 \le\frac{A-R}{A+R}\le\frac{49}{129}<\frac{89}{169}.
\tag{15}
\]
Indeed \(2\pi d\le8\pi/25<\pi/3\), so its cosine exceeds
\(1/2\), while \(R/A\ge40/89\). Equations (14)--(15)
prove the first inequality of (10). Finally
\[
 \log\frac{169}{89}>
       2\frac{169-89}{169+89}=\frac{80}{129}
\]
proves the second.

For \(R=1\), the integral (2) is continuous and absolutely
continuous in \(x\), with the displayed integrable logarithmic
derivative away from its isolated singularities. Alternatively,
integrate for \(R<1\) and then take \(R\uparrow1\).
Both methods retain the numerator zeros and prove the same
integrated inequality. \(\square\)

Integrating (10) from \(x=1/2\) and using the radial bound
at that endpoint gives the complete middle-row estimate
\[
 I_{x,R}(e)\le
       -J(1/2-e)-\frac{40}{129}(x-1/2),
\quad
 \frac12\le x\le\frac{33}{50},\quad c_L\le e\le\frac12.
\tag{16}
\]
There is no condition \(x+e<1\) in (10) or (16).
Thus rows beyond the real numerator wall have not been discarded.

## 3. The complete finite cap and an explicit full-depth strip

**Theorem 2.** For every \(\tau>0\), both parities and all sufficiently
large \(N\),
\[
 \sup_{-2\le w\le2}|U_{0,N}(w,e^{-2\pi i(x+ih)})|
 \le C_\tau N^{B_\tau}
     \exp N\{\mathcal B(x)+\tau\},
\tag{17}
\]
uniformly on
\[
                    \frac12\le x\le\frac{33}{50},
                    \qquad-\frac9{125}\le h\le0,
\]
where the explicit source envelope is
\[
 \mathcal B(x)=
 \max\left\{L,\ B_0-\frac{40}{129}(x-1/2),\ b_0,\ \frac35\right\}.
\tag{18}
\]
The constant \(L\) is the original real-cut value in (7);
its already proved inequality \(L<M_{\rm half}<\widehat M\)
is sufficient here. No new evaluation of it is used.

In particular there is a fixed \(\gamma>0\) such that
\[
 \sup_{-2\le w\le2}|U_{0,N}(w,e^{-2\pi i(x+ih)})|
 \le C_\tau N^{B_\tau}e^{N(\widehat M-\gamma+\tau)}
\tag{19}
\]
throughout
\[
                  \frac{14}{25}\le x\le\frac{33}{50},
                  \qquad-\frac9{125}\le h\le0.
\tag{20}
\]

*Proof.* Separate the two true private ends by the fixed small
endpoint widths from the source of (3). Their entire positive
contribution has rate \(3/5\), uniformly on the closed incoming
unit disk.

On the remaining compact physical indices, retain three groups:
\(e\le c_L\), \(c_L\le e\le1/2\), and \(e\ge1/2\).
Their respective rates are bounded by \(L\), by
\(B_0-(40/129)(x-1/2)\), and by \(b_0\), using
(3)--(8) and (16). Taking a maximum and summing the original
rows adds only a polynomial factor. This proves (17).
Any harmless overlap at an integer cut may be assigned to
either adjacent group.

At \(x\ge14/25\), the middle rate is at most
\[
 B_0-\frac4{215}.
\]
It has a definite reserve below the cap ceiling:
\[
 \widehat M-\left(B_0-\frac4{215}\right)
 =\frac{121}{129000}-\frac{1303}{7680000}>\frac1{1500}.
\tag{21}
\]
For the last comparison, after subtracting \(1/1500\)
the first fraction becomes \(7/25800\); the remaining
cross-product comparison is \(53760000>33617400\).
The other rates in (18) are strictly below \(\widehat M\)
by (5), (8). Choose \(\gamma\) smaller than their positive
minimum reserve and \(1/1500\). This proves (19). \(\square\)

Every term of (1) was bounded using its whole coherent \(H_N\).
No contour was introduced and no weighted or unweighted cap
current has been omitted: the proof directly bounds the complete
finite physical sum, including all revived off-grid numerator rows
and both true ends. It does not transfer a signed sum estimate
through a diagonal row multiplier.

## 4. Ordinary derivatives and exact limitations

The all-real-color proof supplies fixed ordinary-color derivatives
with only polynomial losses by Markov's inequality, applied to
the complete polynomial before taking a uniform supremum.
For a prescribed extra tolerance, the original zero-safe
complex-color estimates give a sufficiently small fixed complex
neighborhood of complete color, with Cauchy bounds for fixed
ordinary derivatives.

The same estimates persist, with an arbitrarily small additional
rate, on sufficiently small complex neighborhoods of the compact
incoming strip: the exact finite factors and uniform product upper
rates are continuous in the incoming parameter, including at
numerator zeros. Any excursions past the closed index boundaries
are handled by the existing compact-index coefficient bounds;
the true-end estimates remain uniform on a slightly enlarged
incoming disk. Hold the physical index groups fixed before taking
fixed mixed derivatives. Cauchy on radius \(1/N\) then gives
polynomial derivative costs. No derivative of a modulus or of an
index cutoff is taken.

The rectangle (20) has the entire required negative depth.
Its earlier part \(1/2\le x<14/25\) has the upper envelope (18),
but is not claimed to have the smaller ceiling (19).
Neither statement supplies a nonzero cap packet, bounds its actual
negative-height critical action, or establishes the full following
weighted-source comparison. Those require their original
conditional factors, Fourier alternatives, correlated affine
reference and remaining incoming contour pieces.

