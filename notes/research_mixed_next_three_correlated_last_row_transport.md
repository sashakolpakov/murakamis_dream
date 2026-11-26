# Last-row transport from two correlated geometric height bounds

Research deduction, 8 November 2026. Two explicit inequalities for
the actual neighboring heights suffice to extend the first-main
by next-last comparison beyond the excluded radius range.
The proof below establishes that implication. Verification of
these two inequalities on the original geometric family is a
separate requirement; no new family coverage is asserted here.

## 1. The source and the two required height inequalities

Keep the original ordinary \(343\) reference and the notation of
[the upper-end theorem](research_mixed_next_own_three_upper_end_last_reduction.md).
Write
\[
\begin{gathered}
a=x+ih_a,\qquad y=q+ih_y,\qquad z=u+ih_z,\\
x,u\in[11/50,9/20],\qquad 0\le q\le11/50,\\
-.072<h_a<0,\quad -.102<h_s,h_y<-.001,\quad
-.065<h_z<.068,\\
R=e^{2\pi h_y},\qquad r_s=e^{2\pi h_s}.
\end{gathered}
\tag{1}
\]
The first conditional factor is the original own-four kernel
\(C_{1,N}(X,Y)\), and the next factor is the original own-three
kernel \(C_{0,N}(Y,Z)\), where \(X=e^{-2\pi ia}\),
\(Y=e^{-2\pi iy}\), and \(Z=e^{-2\pi iz}\).
The height \(h_s\) is that of the actual first private index,
namely the leg \(p=s_2\) in the seven-variable geometric system.
These heights are held fixed while the real shared coordinate
\(q\) moves. They are not independent replacements for the
geometric reference.

The additional inequalities required here are
\[
                R\le\frac{41}{50},\qquad
                r_s\ge\frac45 R.
\tag{2}
\]
They are equivalent to
\[
\frac{\log(41/50)}{2\pi}-\Im y_*\ge0,\qquad
\Im p_*-\Im y_*-\frac{\log(4/5)}{2\pi}\ge0.
\tag{3}
\]
Both left sides in (3) are harmonic functions of the original
external parameter \(b=s_4\). Thus the boundary-certificate
method used for the radius exclusion can test them on the
whole actual family. This note does not perform that test.
The earlier condition \(|Y_*|\le7/10\) is not used.

## 2. A positive derivative on the full shared interval

The exact next-last rate, including its outgoing carrier, is
\[
                    L_0=-\log R+2\pi(h_z)_+.
\tag{4}
\]
For the clipped first main index
\(s=s_R+ih_s\), \(1/6\le s_R\le5/12\), define
\[
\mathcal A(s;q)
  =B_U(x)+\Re Q_1(s;a,y)+L_0-\Re g(y).
\tag{5}
\]
Here \(B_U\), \(Q_1\), \(g\), and the reference bound
\(\Lambda_{123}(z)\) retain exactly the original normalization
of the upper-end theorem. In particular (5) includes the
entire shared-weight allocation. Its exact derivative is
\[
\partial_q\mathcal A
=\log|1-Rr_s e^{-2\pi i(q+s_R)}|
                  -2\log|1-Re^{-2\pi iq}|.
\tag{6}
\]
Put
\[
D=|1-Re^{-2\pi iq}|^2,\qquad
U=|1-Rr_s e^{-2\pi i(q+s_R)}|^2.
\]
Thus \(\partial_q\mathcal A=\tfrac12\log(U/D^2)\).

For \(0\le q\le1/10\), the original trigonometric bounds give
\(D\le9/20\) and \(U\ge3/4\), hence a positive derivative.
On the two other intervals the same bounds, before replacing
\(r_s\) by an independent lower endpoint, give
\[
\begin{array}{c|c|c}
q&D\text{ upper bound}&U\text{ lower bound}\\ \hline
[1/10,1/5]&1+R^2-3R/5&
                  1+(Rr_s)^2+Rr_s/5\\
[1/5,11/50]&1+R^2-9R/25&
                  1+(Rr_s)^2+13Rr_s/10.
\end{array}
\tag{7}
\]
These are the inequalities underlying equation (17) of
the upper-end theorem. Their cosine bounds use the whole
clipped index interval. Since both rightmost expressions
increase with \(r_s>0\), (2) yields
\[
                  U-D^2\ge R p_i(R),
\tag{8}
\]
on the respective intervals, with
\[
\begin{split}
p_1(R)&=-\frac9{25}R^3+\frac65R^2-\frac{11}5R+\frac65,\\
p_2(R)&=-\frac9{25}R^3+\frac{18}{25}R^2
                              -\frac{681}{625}R+\frac{18}{25}.
\end{split}
\tag{9}
\]
On \(0\le R\le1\), \(p_1'\) is increasing and
\(p_1'(1)=-22/25<0\), so \(p_1\) is decreasing. Also
\[
       p_2'(R)=-\frac{27}{25}(R-2/3)^2-\frac{381}{625}<0.
\]
The endpoint values are the exact rational numbers
\[
 p_1(41/50)=\frac{13711}{3125000},\qquad
 p_2(41/50)=\frac{350511}{3125000}.
\tag{10}
\]
Both are positive. The original height bound gives \(R>13/25\);
therefore (8)--(10) imply
\[
 U-D^2>\frac{178243}{78125000}>\frac1{500}.
\tag{11}
\]
For \(q\le11/50\), \(\cos(2\pi q)>0\), so \(D<2\).
Consequently, on \(q\ge1/10\),
\[
 \partial_q\mathcal A
 >\frac12\log(1+1/2000)
 >\frac1{4002}>\frac1{5000}.
\tag{12}
\]
The middle inequality follows from
\(\log(1+t)>t/(1+t)\) for \(t>0\).
The bounds for \(q\le1/10\) give a stronger reserve.
Thus (12) holds on the entire shared interval.

## 3. Transport of the original calibration

At \(q_0=11/50\), the original typed own-three last-row
certificate bounds
\(L_0-\Re g(y)/2\) strictly below its own supporting plane.
It applies at every original ordinary reference in the stated
family, without a radius restriction of \(7/10\).
The first-main and cap planes and the matched shared marginals
give exactly the calibration in equation (14) of the upper-end
theorem:
\[
                 \mathcal A(s;q_0)
                    <\Lambda_{123}(z)-10^{-10}.
\tag{13}
\]
The explicit reserve comes from the retained first quadratic
term and \(\Re y_*>.24\). No numerical margin is extracted
from the strict next-last comparison itself.

The first-main clippings to \([1/6,5/12]\) are valid at
every current \(q\); the next-last rate is independent of
that first index. Equation (12) now transports (13) to
every \(0\le q\le q_0\), under (2).

The other first profiles use their original comparisons.
The real low cut at \(1/8\) has positive transport derivative
on the entire radius range. The first real half is bounded
by its negative-height half profile, then clipped and
transported as above. The double-last profile already has
its all-radius reserve \(109/2000\).
These are precisely the alternatives retained in Section 3
of the upper-end theorem. No bound on a coherent sum is
used as a bound on one of its summands.

## 4. Complete first factor attached to the next upper end

For \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(W)=(rW;r)_j\), set
\[
\mathcal U_{0,N}^{\rm end}
   =\sum_{\lceil N(1-q)\rceil\le j<N}
      \left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|.
\tag{14}
\]
Empty sums are zero. The all-radius upper-end argument
already proves that the literal row rates in (14) are at
most \(L_0\). Its finite form is uniform, retains numerator
zeros, includes both parities, and permits arbitrary subsets.

The complete first-source reduction uses exactly the original
low physical rows, both horizontal aliases, all weighted side
pieces, both unweighted joins, and the positive upper rows.
Every alternative keeps \(L_0\) attached. The profile
comparisons in Section 3 therefore replace the restricted
transport step in Section 4 of the upper-end theorem,
without changing that finite decomposition.

Choosing its finite-product tolerances inside (13) gives
\[
 |U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)|
             \mathcal U_{0,N}^{\rm end}
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}}.
\tag{15}
\]
This is conditional on the actual-reference inequalities (2).
It applies on (1), to all real ordinary colors and both
parities. The central first integral retains its original
\(+N\,da\) measure. For the corresponding holomorphic
expressions with fixed base labels and frozen index sets,
the original polynomial-continuation argument gives all
fixed normalized local derivatives with deficit \(10^{-12}\).

Only the next upper end \(v=1-j/N\le q\) is covered by this
argument. The positive interior upper rows, noncentral first
incoming paths, and the remaining signed Fourier contours
are not concluded from (15). In particular (15) is not a
whole-transfer asymptotic or a volume identity.
