# Reduction of the incoming corner to one displaced vertical segment

Research deduction, 8 November 2026. The complete selected source is
now bounded against its original following geometric action on the
horizontal segment at its actual negative incoming height. The
stronger real-arc cap bound also pays the real interval starting
at \(13/20\). An exact finite contour deformation therefore replaces
the old half-face corner and its earlier real interval by one vertical
segment at \(13/20\), plus contributions with a proved exponential gap.

This is a reduction of a specified remaining contour obligation. It
does not estimate the new vertical segment, establish a complete
selected coefficient, or enlarge the proved knot family. No numerical
evaluation or new reference calibration is used.

## 1. The original finite integrand and paths

Keep the actual canonical reference, both ordinary conditional
indices, and the original outgoing affine action
\(\Lambda_{123}(z)\) of
[calibrated horizontal transport](research_mixed_next_calibrated_horizontal_transport.md),
Sections 1 and 4. In particular
\[
 -9/125<h_a<0,\qquad
 y=\xi+i/100,\quad z=\zeta+i\Im z_*,
 \qquad \xi,\zeta\in[11/50,9/20],\qquad \beta\in\{0,1\}.
 \tag{1}
\]
The external parameter remains the actual \(s_4^*\in K_3\cup K_4\).
Set \(X(a)=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\).
Define the literal integrand
\[
 f_N(a)=
 U_{0,N}(w,X(a))C_{1,N}(X(a),Y)
 d_N(Y)Y^{-N}C_{\beta,N}(Y,Z),
 \qquad
 \omega_\beta(Z)=|d_N(Z)|^{\beta/2}.
 \tag{2}
\]
For \(\beta=0\), the last quantity is identically one, also at
zeros of \(d_N\). It is an external modulus factor; no branch of
a square root is inserted in \(f_N\).

Every sum in (2) is the complete original finite sum. As a function
of \(a\), the integrand is entire and one-periodic: the dependence
on \(X\) is a finite Laurent polynomial, and \(X(a)\) is a nonzero
entire exponential. No asymptotic expression is needed for this
holomorphy statement.

Write
\[
 A=\frac12+ih_a,\qquad
 B=\frac{13}{20}+ih_a,\qquad
 b=\frac{13}{20},\qquad c=\frac7{10}.
 \tag{3}
\]
The portion of the original contour under discussion is the
oriented chain \(A\to1/2\to c\), with density \(+N\,da\).
Its two adjacent vertical pieces, if originally split at the
pair height, concatenate with their original orientations.
This is the chain identified in
[the local corner cancellation theorem](research_mixed_half_face_local_corner_cancellation.md),
Section 1.

## 2. The real interval from \(13/20\) is paid

The [complete log-two cap bound](research_mixed_cap_uniform_log_two_bound.md)
gives the upper rate
\[
 M_{\rm half}-\log2\,(a-1/2),\qquad M_{\rm half}<203/200
 \tag{4}
\]
for the whole cap on the real interval \([1/2,7/10]\), at \(w=-2\)
and on sufficiently small fixed complex neighborhoods with an
arbitrarily small extra rate.

The complete conditional bound, both selected-weight alternatives,
and the actual correlated marginal in
[the final real-interval comparison](research_mixed_next_far_incoming_arc_comparison.md),
Sections 2--3, hold throughout that same incoming interval.
Its restriction \(a\ge69/100\) was used only to lower-bound the
combined incoming decrease. Replacing its old cap decrease by
(4), the combined decrease is at least
\[
 L(a)=\log2\,d+\frac6{37}d+\frac{15}{16}d^2,
 \qquad d=a-\frac12.
 \tag{5}
\]
For \(a\ge13/20\), one has \(d\ge3/20\). All coefficients are
positive, and \(\log2>2/3\). Hence
\[
 L(a)>
 \frac1{10}+\frac9{370}+\frac{27}{1280}
 >\frac1{10}+\frac3{125}+\frac{21}{1000}
 =\frac{29}{200}.
 \tag{6}
\]
The strict rational comparisons use \(1125>1110\) and
\(27000>26880\), respectively.

The largest following cost in the cited proof, before subtracting
the incoming decrease, is
\[
 C_0=
 \frac{203}{200}+\frac{35}{48}+\frac{147}{5000}
 +\frac{17}{1000}+\frac7{250}+\frac3{25}
 =\frac{58157}{30000}.
 \tag{7}
\]
The other marginal sign and the other selected-weight alternative
have smaller costs there. The actual allocated reference obeys
\(A_*>9/5\) and
\[
 A_*+p(\xi-\Re y_*)+B_3(\xi,\zeta)\le\Lambda_{123}(z).
 \tag{8}
\]
All symbols in (8) are the unchanged reference quantities of that
proof; no terminal reference or independent box is substituted.
Combining (6)--(8),
\[
 C_0-L(a)<\frac{53807}{30000}
          =\frac95-\frac{193}{30000}.
 \tag{9}
\]
Thus the complete original density has a raw following-action gap
greater than \(193/30000\) throughout \(b\le a\le c\).
Allocating all finite-source and neighborhood tolerances within
this reserve proves, for all sufficiently large \(N\),
\[
 \omega_\beta(Z)|f_N(a)|
 \le C N^D e^{N(\Lambda_{123}(z)-1/400)}
       \qquad (b\le a\le c).
 \tag{10}
\]
The two level parities and both values of \(\beta\) are included.
The ordinary color scope here is complete color and its small
complex neighborhood; the new real cap contour has not been
promoted to all real ordinary colors. The original incoming
normalization \(+N\) and integration over this fixed interval
add only a polynomial factor.

## 3. An exact identity with only one unpaid segment

Put
\[
 \begin{split}
 I_N&=N\left(\int_A^{1/2}f_N(a)\,da+
                         \int_{1/2}^{c}f_N(a)\,da\right),\\
 V_N&=N\int_B^b f_N(a)\,da,\\
 E_N&=N\int_A^B f_N(a)\,da+
                         N\int_b^c f_N(a)\,da .
 \end{split}
 \tag{11}
\]
Then the finite identity
\[
                         I_N=V_N+E_N
 \tag{12}
\]
holds exactly at every level. Indeed Cauchy's theorem on the
rectangle with vertices \(A,B,b,1/2\) gives
\[
 \int_A^{1/2}f_N+\int_{1/2}^b f_N
                         =\int_A^B f_N+\int_B^b f_N .
 \tag{13}
\]
There are no enclosed poles, omitted residues, or replaced
endpoint amplitudes. Multiplication by the remaining factors
in (2) is already part of this identity, and the differential
has its original complex orientation.

[Calibrated horizontal transport](research_mixed_next_calibrated_horizontal_transport.md),
Theorem 3, bounds the first term of \(E_N\), with finite rate loss
\(1/800\), at the actual height \(h_a\).
Equation (10) bounds its second term. Consequently, at complete
ordinary color and on a sufficiently small fixed complex
neighborhood,
\[
 \boxed{\qquad
 \omega_\beta(Z)|E_N|
 \le C N^D e^{N(\Lambda_{123}(z)-1/1000)} .
 \qquad}
 \tag{14}
\]
The slightly smaller gap allows a common neighborhood and total
tolerance. All outgoing coordinates retain their complete
selected intervals; both third-factor types and both parities
are included. At each reference base, keep the endpoints and paths
fixed before taking complex neighborhoods and derivatives.
Fixed derivatives then have their inherited polynomial costs,
with the outside modulus factor used only for allocation.
No modulus is differentiated or divided out.

## 4. The precise remaining comparison

The only term of this particular contour union not bounded in
(14) is the original finite integral
\[
 V_N=N\int_{13/20+ih_a}^{13/20} f_N(a)\,da .
 \tag{15}
\]
A uniform strict bound for (15) against the same
\(\Lambda_{123}(z)\) would complete the bound for this union.
It may be proved by a bound on its full density or by controlling
cancellation within the vertical integral. No lower estimate or
positivity of its summands is assumed.

The newly proved cap packet near the earlier real interval does
not by itself give such a bound: the width of its complex
neighborhood has not been shown to reach every \(h_a\).
The cap-only upper bound on the full depth rectangle also does
not supply (15), because it has a different scalar ceiling and
the conditional action increases as the incoming height decreases.
Finally, the horizontal proof transports fixed contour profiles
through a numerator wall; it does not establish their convexity
under changes of height after that crossing.

Equation (12) removes the artificial half-face corner by exact
finite holomorphy while recording the replacement segment
explicitly. Other pieces of a complete selected contraction and
stability under arbitrary short partial fillings retain their
own proof obligations. No new knot-family or finite-exceptions
conclusion is asserted.
