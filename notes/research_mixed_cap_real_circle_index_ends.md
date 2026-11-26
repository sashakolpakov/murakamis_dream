# Extreme private indices on the whole real incoming circle

Research lemma, 7 November 2026. The extreme private-index rows of
either original cap have rate less than \(3/5\), uniformly on the
whole unit circle and for every real ordinary color. This provides
an elementary estimate when an outgoing angle approaches zero.
No numerical evaluation is used.

## 1. Exact products and the complete endpoint coefficient

Use \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(S_j=|P_j|\), and \(p_j(X)=(rX;r)_j\). The caps are
\[
 U_{\alpha,N}(w,X)=
  \sum_{j=0}^{N-1}\frac{H_N(w,r^{-j})p_j(X)}
                         {P_j^{1+\alpha}},\qquad \alpha=0,1.
                                                               \tag{1}
\]
The coefficient \(H_N\) is the complete Newton polynomial defined
in [the original source](research_mixed_three_four_ordinary_pair_target.md).
We use its literal finite expansion only for these extreme rows.

The existing
[Newton polynomial bound](research_mixed_newton_color_tubes.md)
and its scalar bound in
[the seam majorants](research_mixed_endpoint_seam_majorants.md)
give
\[
 \sum_{\ell=0}^{N-1}|e_\ell(w)|
       \le C N^B e^{Nb_2},\qquad
 b_2<73/125<3/5,\qquad -2\le w\le2.                     \tag{2}
\]
On a sufficiently small fixed complex neighborhood of \(-2\),
the same estimate holds with any prescribed additional positive
rate tolerance. Both level parities are included, including
vanished complete-color Newton factors.

## 2. The high-index product has a uniform finite bound

For \(j=N-1-m\), the finite binomial identity gives
\[
 \frac{p_j(X)}{P_j}
  =\sum_{\ell=0}^j
   \frac{(-1)^\ell r^{\ell(\ell+1)/2}X^\ell}
        {P_\ell P_{j-\ell}}.                            \tag{3}
\]
The reflection identity \(S_{N-1-k}=N/S_k\) implies
\[
 \frac1{S_\ell S_{j-\ell}}
   =\frac{S_{m+\ell}}{N S_\ell}\le\frac{2^m}{N}.
\]
All indices here are between zero and \(N-1\). Thus, without
dividing by any outgoing-angle factor,
\[
                    \frac{|p_j(X)|}{S_j}\le2^m
                              \qquad(|X|=1).            \tag{4}
\]
This includes \(X=1\) and every root at which the numerator
vanishes.

The complete endpoint coefficient obeys the exact bound
\[
 |H_N(w,r^{-j})|
  \le \frac{2^m}{S_m}\sum_{\ell=0}^{j}|e_\ell(w)| .
                                                               \tag{5}
\]
To verify it, its \(\ell\)-th physical Newton term has modulus
\[
 |e_\ell(w)|\,\frac{S_j}{S_\ell S_{j-\ell}}
 = |e_\ell(w)|\,\frac{S_{m+\ell}}{S_mS_\ell}
 \le |e_\ell(w)|\,\frac{2^m}{S_m}.
\]
Terms with \(\ell>j\) vanish exactly.

Combining (4)--(5), the absolute cap row is bounded by
\[
 \begin{cases}
 \displaystyle \frac{4^m}{S_m}\sum_\ell|e_\ell(w)|,
                                      &\alpha=0,\\[6pt]
 \displaystyle \frac{4^m}{N}\sum_\ell|e_\ell(w)|,
                                      &\alpha=1.
 \end{cases}                                                   \tag{6}
\]
For the second line use \(S_j=N/S_m\).
Write \(J(t)=\int_0^t\log(2\sin\pi s)\,ds\).
If \(m/N\le\delta<1/6\), the uniform sine-product bound
\(\log S_m=NJ(m/N)+O(\log N)\) shows that the two rates in
(6) are at most
\[
             b_2+\delta\log4-J(\delta)+\epsilon.         \tag{7}
\]
Here \(J\) is decreasing on \([0,\delta]\), and \(\epsilon\)
is needed only when allowing a complex color neighborhood.
The additional term tends to zero with \(\delta\).

## 3. Low private indices and the finite conclusion

For \(j/N=s\le\delta\), the exact complete endpoint bound is
\[
 |H_N(w,r^{-j})|
 \le\sum_{\ell=0}^{j}|e_\ell(w)|
                   \frac{S_j}{S_\ell S_{j-\ell}}.
                                                               \tag{8}
\]
For these Newton indices \(u=\ell/N\le s<1/2\), their
real-color upper entropy is at most the complete-color
function \(V_0(u)\), which is continuous with \(V_0(0)=0\).
The elementary \(|p_j(X)|\le2^j\) for \(|X|=1\)
therefore bounds the rate of each summand in (8), after the
cap factors are included, by
\[
 V_0(u)-J(u)-J(s-u)-\alpha J(s)+s\log2+\epsilon,
               \qquad 0\le u\le s\le\delta.             \tag{9}
\]
Its supremum tends to zero as \(\delta\downarrow0\).
This proves the uniform low-index assertion directly, without
extrapolating a compact-index asymptotic.

**Proposition.** There is a fixed \(\delta>0\) such that
\[
 \sum_{\substack{0\le j<N\\j/N\le\delta\
                    \mathrm{or}\ j/N\ge1-\delta}}
 \frac{|H_N(w,r^{-j})|\,|p_j(X)|}{S_j^{1+\alpha}}
          \le C N^B e^{3N/5},\qquad |X|=1,\quad\alpha=0,1.
                                                               \tag{10}
\]
It holds for every real color \(w\in[-2,2]\), and on a
sufficiently small fixed complex neighborhood of \(-2\).
Every fixed ordinary-color derivative has the corresponding
positive-row estimate.

Indeed choose \(\delta<1/6\) so the extra term in (7) is
less than \(1/125\), and the supremum of (9) without
\(\epsilon\) is less than \(1/2\). Since
\(73/125+1/125<3/5\), a small fixed total tolerance leaves
the asserted exponent. There are at most \(N^2\) terms in
the displayed absolute estimates, so their count changes only
the polynomial factor. The real-color derivative assertion
follows by applying Markov's inequality to the complete
polynomial \(H_N(w,r^{-j})\) in each row. Complex derivatives
follow by Cauchy's formula on a smaller fixed disk.

The endpoint layers in (10) are chosen before the limit in \(N\).
The proposition bounds only those layers. It does not bound the
central private rows or assert phase alignment of their sum.
For small complex color disks, the separate
[endpoint polynomial localization theorem](research_mixed_endpoint_polynomial_collar.md)
already gives a stronger coherent description near the endpoint.
The present elementary proof additionally keeps the whole real
color interval and every real incoming angle in its stated scope.
