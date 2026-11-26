# The selected source on a final part of the real incoming interval

Research deduction, 8 November 2026. The decreasing upper bound for
the complete cap gives a strict comparison with the actual following
geometric action on the incoming interval \([69/100,7/10]\). The
comparison includes both alternatives of the selected Fourier weight
and both types of the next tangle. It uses the original finite sums
at complete ordinary color and on a small complex neighborhood.

This is a bound for a specified part of the selected source. It does
not estimate the vertical connector at incoming real part \(7/10\),
the earlier incoming interval, or the whole selected contraction.
No numerical evaluation, saved-data comparison, or change to a
frozen proof is used.

## 1. The exact density and its following reference

Use the ordinary-next canonical family and original normalizations
of [the full selected-plateau comparison](research_mixed_next_filtered_selected_plateau.md).
Its selected flags are \((0,1,\beta)\), where \(\beta\in\{0,1\}\).
Write its actual reference as
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3).
 \tag{1}
\]
Both internal indices \(s_*,t_*\) are ordinary indices. The
external parameter remains the same \(s_4^*\in K_3\cup K_4\);
no terminal reference or independent containing box replaces it.

Set
\[
\begin{gathered}
 P=[11/50,9/20],\qquad H=1/100,\qquad
 y=x+iH,\quad z=u+i\Im z_*,\quad x,u\in P,\\
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},
 \qquad 69/100\le a\le7/10 .
\end{gathered}
 \tag{2}
\]
Here \(a\) is the real incoming coordinate, distinct from \(a_*\).
The nonnegative density to be bounded is precisely
\[
 \mathscr D_N=
 |U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                         |d_N(Z)|^{\beta/2}.
 \tag{3}
\]
The functions \(U_{0,N}\) and \(C_{1,N}\) are the complete original
cap and conditional polynomials. The latter is
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
          \frac{X^{-j}(rX;r)_j(rY;r)_j}{(r;r)_j^3},
 \qquad r=e^{-2\pi i/N}.
\]
The other finite factors in (3) retain the definitions of the
selected-plateau theorem. In particular there is no incoming
Fourier halfweight; at \(\beta=0\) the last factor is one,
including at zeros of \(d_N(Z)\).

Let
\[
\begin{split}
 A_*&=\Re\{\mathcal P_{34}(-2,y_*)-\tfrac12 g(y_*)\},\\
 \alpha&=\Re y_*\in(6/25,9/25),\\
 p&=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\}.
\end{split}
 \tag{4}
\]
The original following affine action is denoted by
\(\Lambda_{123}(z)\), and the third-factor supporting plane by
\(B_3(x,u)\), exactly as in equations (8), (17)--(18) of the
selected-plateau theorem. The properties we use are
\[
 A_*+p(x-\alpha)+B_3(x,u)\le\Lambda_{123}(z),\qquad A_*>9/5.
 \tag{5}
\]
The stronger action inequality in
[the allocated-action theorem](research_mixed_next_allocated_action_floor.md)
proves the second assertion for this same canonical family.
All three quantities in (4) come from one actual reference.

## 2. Complete cap and conditional upper bounds

Put \(M_{\rm half}=\Re\mathcal T(1/2,-2)\), the original cap
critical action at the half face. The
[complete decreasing cap envelope](research_mixed_cap_uniform_departure_envelope.md)
proves
\[
 |U_{0,N}(-2,e^{-2\pi ia})|
 \le C_\tau N^{B_\tau}
   \exp N\{M_{\rm half}-\log(3/2)(a-1/2)+\tau\}.
 \tag{6}
\]
It includes every physical row, both horizontal remainders,
all four weighted vertical currents, and every main-path join.
Its scope includes small complex ordinary-color neighborhoods
with arbitrarily small additional rate. It is not an all-real-color
bound for this newly chosen main contour.
The original action bound gives \(M_{\rm half}<203/200\).

For the complete conditional factor use
[the conditional incoming-decrease theorem](research_mixed_real_arc_conditional_absolute_decrease.md).
Write
\[
 c=-J(1/4)<7/48,\qquad \delta=x-1/4,\qquad d=a-1/2.
\]
The bound on \(c\) is the written inequality
\(-4J(1/4)<7/12\), with its elementary witness in
[the low-index kernel margin](research_mixed_next_low_index_kernel_margin.md).
If \(\bar q_0(x)\) is the real optimized conditional action at
incoming coordinate \(1/2\), the conditional theorem gives
\[
 |C_{1,N}(X,Y)|
 \le \operatorname{poly}(N)
 \exp N\{\bar q_0(x)+13\pi/2500-\mathcal D(a)\},
 \quad
 \mathcal D(a)\ge\frac6{37}d+\frac{15}{16}d^2 .
 \tag{7}
\]
The two useful quadratic upper bounds from that same theorem are
\[
\begin{split}
 \bar q_0(x)
 &\le 5c+\tfrac12\log2\,\delta-\tfrac\pi3\delta^2,\\
 \bar q_0(x)-J(x)/2
 &\le \tfrac{11}{2}c+\tfrac14\log2\,\delta
                       -\tfrac{143\pi}{384}\delta^2 .
\end{split}
 \tag{8}
\]
These bound the whole conditional sum through its already proved
complete asymptotic, not merely an arbitrarily chosen row.
In particular all parity and numerator-wall contributions remain.

Maximizing each quadratic over the entire real line is an upper
bound for its maximum on \(P\). Since \(\log2<7/10\) and
\(\pi>25/8\), (8) implies
\[
 \bar q_0(x)<\frac{35}{48}+\frac{147}{5000},
 \qquad
 \bar q_0(x)-J(x)/2<\frac{77}{96}+\frac{49}{6400}.
 \tag{9}
\]
Indeed the respective quadratic gains are at most
\((7/20)^2/[4(25/24)]\) and \((7/40)^2/4\).
For the second bound we used \(143\pi/384>1\).

Combining the incoming decreases in (6) and (7), define
\[
 \mathcal L(a)=\log(3/2)d+\mathcal D(a).
\]
The elementary inequality \(\log(3/2)>2/5\) gives
\[
 \mathcal L(a)>
 \frac{104}{185}d+\frac{15}{16}d^2>\frac7{50}
                    \quad(69/100\le a\le7/10).
 \tag{10}
\]
For an explicit witness at \(d=19/100\), the two terms on the
right are \(494/4625>17/160\) and
\(1083/32000>27/800\); their sum exceeds \(7/50\).
At the far endpoint the stronger bound is
\[
 \mathcal L(7/10)>
 \frac2{25}+\frac6{185}+\frac3{80}
 =\frac{2219}{14800}>\frac{149}{1000}.
 \tag{11}
\]

## 3. The selected weights and the actual marginal

The complete third-factor comparison and Fourier-weight theorem,
as assembled in the selected-plateau proof, give
\[
\begin{split}
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)Y^{-N}|^{1/2}
                          |d_N(Z)|^{\beta/2}
 &\le C_\tau N^{D_\tau}e^{N\{B_3(x,u)+7/250+\tau\}},\\
 |d_N(Y)Y^{-N}|^{1/2}
 &\le C_\tau N^{D_\tau}e^{N\{H_0(x)+\tau\}},\\
 H_0(x)&=\max\{-J(x)/2-3\pi/400,0\}.
\end{split}
 \tag{12}
\]
Both alternatives of this maximum are retained. These statements
include the full third conditional polynomial and its remainders.
They do not divide by a Fourier polynomial at a zero.

We use two further bounds from the same proof, with the actual
correlated marginal (4):
\[
\begin{array}{ll}
 p\le0:& H_0(x)-p(x-\alpha)<3/25,\\[1mm]
 p\ge0:& p<3/5,\quad -p(x-\alpha)<21/250.
\end{array}
 \tag{13}
\]
The first is equation (25) and its preceding interval argument
there. For the second, its equation (28) gives
\(p<7/10-393/3062<3/5\), and \(\alpha-x<7/50\).
When \(x\ge\alpha\), the last expression is nonpositive,
so the same upper bound still holds.

Let \(\mathcal C(a,x)\) denote the resulting upper rate for (3)
after subtracting \(B_3(x,u)+p(x-\alpha)\), before the arbitrarily
small finite-source tolerance. Equations (6)--(13) bound it
without evaluating any reference action.

If \(p\le0\), use the first part of (9) and (13). Since
\(13\pi/2500<17/1000\), equations (10), (12) give
\[
\begin{split}
 \mathcal C(a,x)
 &<
 \frac{203}{200}+\frac{35}{48}+\frac{147}{5000}
 +\frac{17}{1000}+\frac7{250}+\frac3{25}-\frac7{50}\\
 &=\frac{53957}{30000}
 =\frac95-\frac{43}{30000}.
\end{split}
 \tag{14}
\]
The bound holds uniformly over the whole outgoing interval.

If \(p\ge0\), consider the two alternatives in \(H_0\).
For the zero alternative, replace \(3/25\) in (14) by
\(21/250\), which only decreases that bound.
For the factorial alternative, combine the second bound in (9)
with the exact height cost
\[
 13\pi/2500-3\pi/400=-23\pi/10000<-23/3200 .
\]
Equations (10)--(13) then give
\[
 \mathcal C(a,x)<
 \frac{203}{200}+\frac{77}{96}+\frac{49}{6400}
 -\frac{23}{3200}+\frac7{250}+\frac{21}{250}-\frac7{50}
 <\frac{1791}{1000}.
 \tag{15}
\]
For the last comparison use \(77/96<803/1000\),
\(49/6400<8/1000\), and \(23/3200>7/1000\).
This is again less than the ceiling in (14).

By (5), every case therefore lies strictly below the actual
following affine action by at least \(43/30000>1/1000\).
At \(a=7/10\), replace \(7/50\) by \(149/1000\) using (11).
The uniform margin improves by \(9/1000\), to
\[
             \frac{313}{30000}>\frac1{100}.
 \tag{16}
\]
No independent marginal or additive action constant has replaced
the original following reference.

## 4. Finite-source conclusion and limits of the result

**Theorem.** Uniformly on the canonical family (1)--(2),
for both values of \(\beta\), both integer parities, and all
sufficiently large \(N\), the exact density (3) satisfies
\[
 \mathscr D_N\le C N^B
         e^{N\{\Lambda_{123}(z)-1/2000\}}
                \qquad(69/100\le a\le7/10,\ w=-2).
 \tag{17}
\]
At the endpoint \(a=7/10\) it satisfies the stronger estimate
\[
 \mathscr D_N\le C N^B
         e^{N\{\Lambda_{123}(z)-1/200\}} .
 \tag{18}
\]
The constants may be chosen on a fixed sufficiently small complex
ordinary-color neighborhood of \(-2\), after reducing these gaps.
Fixed ordinary-color derivatives have polynomial costs, by the
same holomorphic bounds and Cauchy's formula.

To prove the finite statements, allocate the total tolerance from
(6), (12), and their common neighborhoods strictly inside the
reserves (14)--(16). All remaining prefactors are polynomial in
\(N\). Every factor is the original complete finite function, so
no conditional row, Fourier alternative, or contour remainder
needs to be supplied after taking this product. The real incoming
integration over this final interval, with its original density
\(+N\), likewise costs only a polynomial factor. The two independent
outgoing coordinates retain their whole selected intervals.

The bounds are stated for the weighted density. They do not
differentiate a modulus halfweight or divide by one at its zeros.
They make no all-real-ordinary-color claim beyond the scope of the
new cap envelope. In particular (17) alone is not a theorem for
an arbitrary subsequent tangle composition.

This pays the final real incoming interval and its endpoint in the
actual following-action comparison. The remaining incoming
connector and the earlier real interval still require a compatible
contour argument, with their common endpoint cancellation retained.
The full selected contraction and the finite-exceptions objective
remain open.
