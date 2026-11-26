# A coherent cap bound on a larger final incoming arc

Research deduction, 7 November 2026. Retaining the private-index
dependence of the complete endpoint coefficient extends the paid real
first-coordinate arc from \([13/16,1]\) to \([7/10,1]\). The estimate
uses the whole original cap and conditional polynomial, including
rows that do not terminate between physical roots. It introduces no
new contour or unweighted connecting segment.

The remaining real main integral is consequently restricted to
\([1/2,7/10]\). Its initial vertical connector remains separate.
No numerical evaluation or certificate replay is used.

## 1. The complete finite source and its private-row rate

Use the original factors
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
             H_N(w,r^{-j})\,\frac{p_j(X)}{P_j},\\
 C_{1,N}(X,Y)&=\sum_{k=0}^{N-1}
             \frac{X^{-k}p_k(X)p_k(Y)}{P_k^3},\\
 r&=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 p_j(X)=(rX;r)_j,\qquad S_j=|P_j|.
\end{split}                                                    \tag{1}
\]
Each \(H_N\) is its complete coherent endpoint polynomial.
Let \(J\) be the continuous one-periodic primitive of
\(\log(2|\sin\pi e|)\), normalized by \(J(0)=0\). Write
\[
 \lambda(e)=\Re S(e),\qquad h(e)=\lambda(e)+J(e),\qquad
 b_0=\frac{101}{125}.
                                                               \tag{2}
\]
Here \(S\) is the original endpoint action. The real-index source
bounds in
[the complementary real-color theorem, Section 2](research_mixed_three_four_complementary_real_colors.md)
give, on every compact private interval in \((0,1)\),
\[
 |H_N(w,r^{-j})|
 \le C_\tau N^{B_\tau}e^{N\{h(j/N)+\tau\}},
                 \qquad -2\le w\le2.
                                                               \tag{3}
\]
They also hold on a sufficiently small fixed disk about \(-2\),
with an arbitrary prescribed extra tolerance. The two true private
ends are bounded separately, on the whole disk \(|X|\le1\), by
\[
 \sum_{\substack{j/N\le\delta_0\\\text{or }j/N\ge1-\delta_0}}
  |H_N(w,r^{-j})|\,|p_j(X)|/S_j
                         \le C N^B e^{3N/5}.
                                                               \tag{4}
\]
The endpoint width is fixed and sufficiently small. Equation (4)
is the zero-safe finite-product bound from the same source; it does
not extrapolate the compact asymptotic (3) to an endpoint.

For real \(a=1-v\), define
\[
 B_v(e)=J(e-v)+J(v)-J(e),\qquad
 A(v)=J(v)-2J(v/2),\qquad 0\le v\le\tfrac12.
                                                               \tag{5}
\]
The zero-safe numerator estimate and the uniform sine-factorial
estimate give the complete compact cap-row rate
\[
 h(e)+B_v(e)=\lambda(e)+J(a+e)-J(a).
                                                               \tag{6}
\]
Thus the dependence on \(e\) is retained before maximizing.
The source statements (3)--(6) are uniform through numerator zeros.

## 2. A quantitative curvature bound for the coherent endpoint

The exact real endpoint curvature in
[the early real-row theorem, Lemma 1](research_mixed_cap_early_taper_real_rows.md)
implies
\[
 -h''(e)=\frac{2\pi}{\sin\pi e}
              \Re\frac1{\sqrt{2-e^{-2\pi ie}}},
                   \qquad 0<e<\tfrac12.
                                                               \tag{7}
\]
The square root is its original branch with positive real part.
Set
\[
 s=\sin\pi e,\qquad R=\sqrt{1+8s^2},\qquad 1<R<3.
\]
Since
\[
 |2-e^{-2\pi ie}|=R,\qquad
 \left(\Re\sqrt{2-e^{-2\pi ie}}\right)^2
                          =\frac{(R+1)(R+3)}8,
\]
one obtains
\[
 \frac1s\Re\frac1{\sqrt{2-e^{-2\pi ie}}}
             =\frac1R\sqrt{\frac{R+3}{R-1}}
             >\frac1{\sqrt3}.
                                                               \tag{8}
\]
The squared comparison is equivalent to
\((R-3)(R^2+2R+3)<0\).
Moreover \(\pi/\sqrt3>9/5\): it follows from
\(\pi>25/8\) and \(15625>15552\). Therefore
\[
                         -h''(e)>\frac{18}{5}.
                                                               \tag{9}
\]
The original seam identities give \(h'(1/2)=0\) and
\(h(1/2)<b_0\). Integrating (9) to that endpoint proves
\[
 h(e)\le b_0-\frac95(1/2-e)^2
                         \qquad(0\le e\le1/2).
                                                               \tag{10}
\]
The limiting endpoint values are continuous. On the full interval,
the original monotonicity and reflection identity give
\[
                         h(e)\le b_0\qquad(0\le e\le1).
                                                               \tag{11}
\]
These are bounds for the action of the complete endpoint coefficient,
not for the entropy of its separate Newton summands.

## 3. The incoming angle and private index have a joint loss

The quotient calculation in
[the final-arc theorem, Lemma 1](research_mixed_next_selected_final_first_arc.md)
gives
\[
 B_v(e)\le A(v),\qquad 0\le A(v)\le v\log2 .
                                                               \tag{12}
\]
The stronger sign on the wrapped range, proved in
[the end-range theorem, Section 2](research_mixed_next_selected_first_wall_rows.md),
is
\[
                         B_v(e)\le0\qquad(v\le e\le1).
                                                               \tag{13}
\]
It follows either from its two endpoint values \(B_v(v)=B_v(1)=0\)
and its unique interior minimum, or directly by differentiating
the sine quotient. All these statements extend through the
integrable singularities by continuity.

On the prewall interval \(0<e<v\), the stronger curvature is
\[
\begin{split}
 B_v''(e)
  &=-\pi\{\cot\pi e+\cot\pi(v-e)\}\\
  &\le-2\pi\cot(\pi v/2).
\end{split}                                                    \tag{14}
\]
Indeed
\(\sin\pi e\sin\pi(v-e)\le\sin^2(\pi v/2)\).
The midpoint has value \(A(v)\) and derivative zero, so
\[
 B_v(e)\le A(v)-d_v(e-v/2)^2,\qquad
 d_v=\pi\cot(\pi v/2).
                                                               \tag{15}
\]
Suppose now \(0<v\le3/10\). With \(z=3\pi/20\),
\(\sin z<z\), \(\cos z>1-z^2/2\), and \(\pi<22/7\) yield
\[
 d_v\ge\pi\cot(3\pi/20)
 >\frac{20}{3}\left(1-\frac{9\pi^2}{800}\right)
 >\frac{8711}{1470}>\frac{59}{10}.
                                                               \tag{16}
\]
Combining (10) and (15), and completing the two squares, gives
\[
\begin{split}
 h(e)+B_v(e)
 &\le b_0+A(v)
       -\frac{(9/5)d_v}{9/5+d_v}(1/2-v/2)^2\\
 &\le b_0+A(v)-\mathcal L,\qquad
 \mathcal L=\frac{531}{385}\left(\frac7{20}\right)^2
            =\frac{26019}{154000},
                    \qquad 0\le e\le v\le3/10 .
\end{split}                                                    \tag{17}
\]
For \(v=0\) the prewall interval is empty. On its complement,
(11) and (13) give the smaller cap ceiling \(b_0\).
The physical endpoint ceiling \(3/5\) in (4) is also smaller.
Consequently the entire cap, with every original private row, obeys
\[
 |U_{0,N}(w,e^{-2\pi i(1-v)})|
 \le C_\tau N^{B_\tau}
   e^{N\{\max(b_0,b_0+A(v)-\mathcal L)+\tau\}},
                     \qquad 0\le v\le3/10 .
                                                               \tag{18}
\]
This is uniform for all real ordinary colors and on sufficiently
small fixed complete-color disks. To prove it, apply (3) and the
zero-safe product bound only on the compact private rows, sum their
positive upper bounds after (17), and use (4) at both true ends.
The at most \(N\) rows cost only a polynomial factor.

## 4. The whole conditional source on the disk

The complete centered-arc numerator bound gives
\[
 |p_k(Y)|\le C_\tau N^{B_\tau}e^{N\{L(k/N)+\tau\}},
 \quad |Y|\le1,\qquad L(t)=-2J((1-t)/2).
                                                               \tag{19}
\]
Together with (12) and the original
\(\max_{[0,1]}(L-2J)<7/15\), it proves
\[
 \sup_{|Y|\le1}|C_{1,N}(e^{-2\pi i(1-v)},Y)|
       \le C_\tau N^{B_\tau}e^{N\{A(v)+7/15+\tau\}} .
                                                               \tag{20}
\]
The incoming chirp has modulus one. Every conditional index,
including both true ends and all revived rows, is retained.

Since \(A(v)\le(3/10)\log2<21/100\), the two rates resulting
from (18)--(20) satisfy
\[
\begin{split}
 b_0+A(v)+7/15
   &<\frac{2227}{1500}<\frac{153}{100},\\
 b_0+2A(v)+7/15-\mathcal L
   &<\frac{77}{50}-\frac{6601}{462000}
    =\frac{153}{100}-\frac{1981}{462000}.
\end{split}                                                    \tag{21}
\]
All comparisons are exact rational inequalities using
\(\log2<7/10\). Allocate the finitely many source and color
tolerances inside the smaller reserve in (21).

**Theorem 1.** At both level parities,
\[
 \sup_{\substack{7/10\le a\le1,\ |Y|\le1\\-2\le w\le2}}
 |U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)|
                     \le C N^B e^{153N/100}.
                                                               \tag{22}
\]
The same ceiling holds on a sufficiently small fixed disk about
\(w=-2\). Every fixed real ordinary derivative has polynomial cost:
apply Markov to each complete \(H_N\) with its own rate before the
positive private sum. Fixed derivatives on smaller complex color
disks follow by Cauchy. No Newton summand within \(H_N\) has been
replaced by an absolute estimate.

## 5. The original selected-next comparison and the remaining arc

Use precisely the ordinary-next family, action and marginals of
[the filtered selected-plateau theorem](research_mixed_next_filtered_selected_plateau.md),
equations (3)--(8). Thus the first three flags are \((0,1,\beta)\),
\(\beta=0,1\), the next vertex is ordinary, and
\[
 y=x+i/100,\quad x\in P=[.22,.45],\qquad
 z=u+i\Im z_*,\quad u\in P,\qquad
 Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
                                                               \tag{23}
\]
The product in (22) is a polynomial of degree at most \(D=N-1\)
in \(Y\). As proved in Section 3 of
[the final-arc theorem](research_mixed_next_selected_final_first_arc.md),
the full selected-plane comparison applies to any such polynomial
with disk ceiling \(77/50\). It retains both alternatives of the
exact \(d_N(Y)\) weight, the original incoming marginal and the
whole ordinary third factor.

Here the stronger ceiling \(153/100=77/50-1/100\) gives
\[
\begin{split}
 &|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                       |d_N(Z)|^{\beta/2}\\
 &\hspace{12mm}\le C_\tau N^{B_\tau}
             e^{N\{\Lambda_{123}(z)-3/250+\tau\}},
       \qquad X=e^{-2\pi ia},\quad 7/10\le a\le1 .
\end{split}                                                    \tag{24}
\]
For \(\beta=0\), no outgoing halfweight is inserted.
The raw comparison follows by subtracting \(1/100\) from the
previous raw rate, whose gap was greater than \(1/500\).
After all remaining finite tolerances and polynomial factors,
one may retain the conservative gap \(1/200\).

In particular the actual prefix contribution
\[
 F_{34,N}^{\,\ge7/10}(w,Y)
   =N\int_{7/10}^{1}
       U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da
                                                               \tag{25}
\]
satisfies the same selected estimate. Its insertion into the
selected \(y\) integral retains both original factors \(N\).
Bounded path lengths change only polynomial prefactors.
Keep the paths fixed at a base reference for outside-parameter
derivatives. The strict reserves, the original holomorphic
source bounds and Cauchy's formula give the same local normalized
fixed mixed derivatives with loss \(1/400\), using the outgoing
weight only in its original nonzero reference neighborhood.
No division through a weight zero on the whole plateau is used.

The real-main reduction in
[the conditional alias theorem](research_mixed_next_far_half_conditional_aliases.md)
differs from the complete conditional source only by already paid
physical ends and decaying currents. Thus (24) also pays its
remaining real main contribution on \([7/10,13/16]\), with the
smaller inherited error gap if necessary. This conclusion is obtained
on the original real segment; it creates no unweighted main-path
connectors. The still-unestimated first-coordinate pieces are the
real main integral on \([1/2,7/10]\) and its initial vertical join.
The theorem does not estimate a full Fourier coefficient, an
arbitrary physical-index subset, or a terminal-third reference.
