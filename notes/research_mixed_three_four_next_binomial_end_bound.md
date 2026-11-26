# A binomial bound for the final incoming rows

Research deduction, 7 November 2026. In the exact next attachment
\(34\to343,344\), the rows with second incoming index
\(b\ge\lceil11N/12\rceil\) have an exponential rate at most \(9/5\).
This is below the original geometric action on both the ordinary and
terminal reference families. The proof uses termination at a root of
unity and an elementary comparison of sine binomial coefficients with
ordinary binomial coefficients. It retains the coherent first-cap
coefficients and combines both Fourier sectors by the exact finite
sampling identity.

## 1. Reflection and a finite binomial inequality

Let
\[
 D=N-1,\qquad r=e^{-2\pi i/N},\qquad
 P_j=(r;r)_j,\qquad S_j=|P_j|,\qquad
 p_j(X)=(rX;r)_j,\qquad N\ge2.
 \tag{1}
\]
All factorial indices below lie between zero and \(D\), so their
denominators are nonzero. The complete sine product and reflection give
\[
 S_D=N,\qquad S_bS_{D-b}=N.
 \tag{2}
\]
For \(0\le b<N\), put \(n=D-b\). If \(0\le j\le n\), then
\[
 \frac{S_{b+j}}{S_bS_j}
   =\frac{S_n}{S_{n-j}S_j}
   =\prod_{\ell=1}^{j}
       \frac{\sin\{\pi(n-j+\ell)/N\}}{\sin(\pi\ell/N)}
   \le \binom nj.
 \tag{3}
\]
The empty product is one. To prove the inequality, the function
\(\sin t/t\) strictly decreases on \(0<t<\pi\): the derivative has
the sign of \(t\cos t-\sin t\), which decreases from zero because
its derivative is \(-t\sin t<0\). Since
\(n-j+\ell\ge\ell\), each factor in (3) is at most
\((n-j+\ell)/\ell\). Multiplication proves the claim.
The inequality is valid on the full range \(n<N\), although only
small \(n\) will be used.

## 2. The complete factors at a sampled incoming coordinate

Keep the original polynomials
\[
 \begin{split}
 U_{0,N}(w,X)
    &=\sum_{\ell=0}^{D}\frac{H_N(w,r^{-\ell})}{P_\ell}p_\ell(X),\\
 F_N(w,Y)
    &=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 C_{\beta,N}(Y,Z)
    &=\sum_{k=0}^{D}
       \frac{Y^{-k}p_k(Y)p_k(Z)}{P_k^{2+\beta}},
                     \qquad\beta\in\{0,1\}.
 \end{split}
 \tag{4}
\]
Here \(H_N\) is the complete original ordinary-boundary coefficient;
its internal sum has not been replaced by absolute values of Newton
terms. Define
\[
 T_{j,N}(w)=\operatorname{CT}_X[X^{-j}p_j(X)U_{0,N}(w,X)].
 \tag{5}
\]
The coherent seam estimate and its real-color extension, used in
[the earlier physical end bound](research_mixed_three_four_next_physical_end_sector.md),
equations (7)--(9), give
\[
 \begin{split}
 |T_{j,N}(w)|&\le
     C_\tau N^{A_\tau}e^{N(b_1+\tau)}\binom{N+j}{j},\\
 b_1&=433/500,\qquad
 \binom{N+j}{j}\le e^{N\rho(j/N)},\\
 \rho(t)&=(1+t)\log(1+t)-t\log t,\qquad \rho(0)=0.
 \end{split}
 \tag{6}
\]
For every \(\tau>0\), this holds for all real \(w\in[-2,2]\) and
on a sufficiently small fixed complex disk about \(-2\).

At \(Y=r^b\), both conditional factors terminate at \(n=D-b\).
Equations (3)--(5) give
\[
 \begin{split}
 |F_N(w,r^b)|
    &\le N\sum_{j=0}^{n}\binom nj\,S_j^{-2}|T_{j,N}(w)|,\\
 |C_{\beta,N}(r^b,Z)|
    &\le\sum_{k=0}^{n}\binom nk\,S_k^{-1-\beta}|p_k(Z)|.
 \end{split}
 \tag{7}
\]
These inequalities estimate complete finite factors. Any further
numerator zeros remain harmless, and \(|p_k(Z)|\le4^k\) for
\(|Z|\le3\).

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 \log S_j=NJ(j/N)+O(\log N).
 \tag{8}
\]
The error is uniform for every \(0\le j<N\). If
\[
             b\ge\lceil11N/12\rceil,\qquad v=1-b/N,
 \tag{9}
\]
then \(j/N,k/N\le n/N<v\le1/12\). On this interval \(J\)
decreases and \(\rho\) increases. Applying (6)--(8) and the
ordinary binomial theorem therefore yields
\[
 \begin{split}
 |F_N(w,r^b)|
   &\le C_\tau N^{A_\tau}
        e^{N\{b_1+\tau+\rho(v)-2J(v)\}}\,2^n,\\
 |C_{\beta,N}(r^b,Z)|
   &\le C N^A e^{-N(1+\beta)J(v)}\,5^n,\\
 S_b^{-1}&\le C N^A e^{NJ(v)}.
 \end{split}
 \tag{10}
\]
The last line uses \(J(1-v)=-J(v)\). Thus every weighted product
in the next transfer has rate at most
\[
 b_1+\tau+\rho(v)-(2+\beta)J(v)+v\log10.
 \tag{11}
\]
In particular the reciprocal factorial at the sampled coordinate has
not been dropped. It supplies the favorable \(+J(v)\) in (10).

## 3. An elementary strict comparison with \(9/5\)

For \(0\le u\le1/6\), concavity of sine gives
\(2\sin\pi u\ge6u\). Hence, for \(0\le v\le1/12\),
\[
 -J(v)\le v(1-\log(6v))
       \le\frac{1+\log2}{12}<\frac{17}{120}.
 \tag{12}
\]
Also
\[
 (1+v)\log(1+v)\le v+\frac{v^2}{2},
 \qquad
 \rho(v)\le v(1-\log v)+\frac{v^2}{2}
                 <\frac{85}{288}.
 \tag{13}
\]
For the first inequality, differentiate both sides and use
\(\log(1+v)\le v\); they agree at zero. The final bound uses
monotonicity and \(\log12<5/2\).

All logarithm comparisons needed here have elementary witnesses:
\[
 \begin{split}
 e^{7/10}
   &>1+\frac7{10}+\frac{49}{200}+\frac{343}{6000}>2,\\
 e^{5/3}
   &>\sum_{j=0}^{4}\frac{(5/3)^j}{j!}
       =\frac{10009}{1944}>5,\\
 e^{5/2}
   &>\sum_{j=0}^{6}\frac{(5/2)^j}{j!}
       =\frac{553405}{46080}>12.
 \end{split}
 \tag{14}
\]
In particular \(\log10<7/10+5/3=71/30\). Since \(2+\beta\le3\),
the rate in (11), before its arbitrary tolerance, satisfies
\[
 \begin{split}
 b_1+\rho(v)-(2+\beta)J(v)+v\log10
   &<\frac{433}{500}+\frac{85}{288}
                 +\frac{17}{40}+\frac{71}{360}\\
   &=\frac{64201}{36000}<\frac95.
 \end{split}
 \tag{15}
\]
The final reserve is \(599/36000\). Choosing \(\tau\) smaller
than this reserve and summing at most \(N\) rows proves the following.

**Theorem 1.** At every sufficiently large integer level, of either
parity,
\[
 \sum_{b=\lceil11N/12\rceil}^{D}
   \left|\frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z)\right|
      \le C N^A e^{9N/5},\qquad |Z|\le3,\quad\beta=0,1.
 \tag{16}
\]
The estimate holds uniformly for all real ordinary colors and on a
sufficiently small fixed complex disk about \(-2\).

Fixed ordinary-color derivatives obey the same bound with polynomial
cost. For real colors apply Markov's inequality to each complete
\(T_{j,N}\) before the positive sums in (7); for complex colors use
Cauchy's formula on smaller disks. Fixed output derivatives are allowed
on every smaller disk \(|Z|\le R_0<3\), by applying Cauchy's formula
to each complete conditional polynomial before summing. These
arguments preserve (16) as a sum of absolute values, rather than only
as a bound for its coherent total.

## 4. Comparison with the actual action and a reduced finite sum

Let \(\mathcal E_{\beta,N}^{(12)}\) be the sum inside (16) before
taking absolute values. The original action comparison in
[the physical end theorem](research_mixed_three_four_next_physical_end_sector.md),
Section 3, gives
\(\Re\mathcal P_\beta^+(-2,z)>15/8\) on all the actual ordinary
and terminal next reference families. Their outgoing values satisfy
\(|e^{-2\pi iz}|<3\). On common sufficiently small fixed
neighborhoods one has \(\Re\mathcal P_\beta^+(w,z)>29/16\).
Since \(29/16-9/5=1/80\), Theorem 1 and Cauchy's formula imply
\[
 \left|\partial_w^j\partial_z^k
   \left[e^{-N\mathcal P_\beta^+(w,z)}
       \mathcal E_{\beta,N}^{(12)}(w,e^{-2\pi iz})\right]\right|
       \le C_{j,k}N^{A_{j,k}}e^{-N/160}.
 \tag{17}
\]
The smaller displayed gap leaves room for a common choice of
neighborhoods. For remote real ordinary colors, (16) is instead
compared with the action at complete color; no continuation of that
action through the whole real color interval is asserted.

This estimate can be combined with the
[first-coordinate end rectangle](research_mixed_three_four_next_first_physical_end.md).
Denote the exact double-root summand by
\[
 A_{a,b,N}(w,Z)=
 U_{0,N}(w,r^a)C_{1,N}(r^a,r^b)
                       \frac{C_{\beta,N}(r^b,Z)}{P_b},
 \tag{18}
\]
and set \(L_N=\lceil99N/100\rceil\),
\(M_N=\lceil11N/12\rceil\). Define the remaining finite polynomial
\[
 \mathcal C_{\beta,N}^{(12)}(w,Z)
       =\sum_{0\le a<L_N}\sum_{0\le b<M_N}A_{a,b,N}(w,Z).
 \tag{19}
\]
The exact whole next transfer is
\[
 \mathcal F_{\beta,N}
   =\mathcal C_{\beta,N}^{(12)}
      +\mathcal R_{\beta,N}+\mathcal E_{\beta,N}^{(12)}
      -\sum_{a=L_N}^{D}\sum_{b=M_N}^{D}A_{a,b,N}.
 \tag{20}
\]
Here \(\mathcal R_{\beta,N}\) is the entire first-coordinate end
rectangle from that theorem. Its positive termwise estimate, of rate
\(7/4\), also bounds the intersection in (20). The bound for
\(\mathcal E_{\beta,N}^{(12)}\) keeps the first-coordinate sum
coherent; it is not asserted termwise in both indices.
On the common actual output neighborhoods, (17) consequently holds
with \(\mathcal E_{\beta,N}^{(12)}\) replaced by
\(\mathcal F_{\beta,N}-\mathcal C_{\beta,N}^{(12)}\).

Thus the complete next finite sum differs from (19) by an exponentially
smaller term at the original geometric action. Both Fourier
coefficients remain combined in this statement. The smaller physical
rectangle has not been replaced by a continuous rectangle or an
integral without sampling currents. Proving its nonzero geometric
contribution, and the full next-prefix asymptotic, remains necessary.

## 5. A sharper action floor from the actual coordinate ranges

The same source domains also give a stronger geometric comparison,
independently of the binomial estimate. It is useful when a competing
source rate is too large for the earlier floor \(15/8\).
At an actual next reference write \(y=t_2\), \(s=s_3\), and
\(z=t_3\), as in
[the local next-source theorem](research_mixed_three_four_next_local_source.md),
Section 2. For an ordinary third vertex both \(s,z\) are ordinary
legs. For a terminal third vertex, \(s\) is attached and \(z\)
is private. In both cases \(y\in O_4\) and
\(y=q_{34}(s)\).

The exact action identity and independent pair estimate in
[the physical end theorem](research_mixed_three_four_next_physical_end_sector.md),
equations (16)--(23), give
\[
 \Re\{\mathcal P_\beta^+(-2,z)-\mathcal P_{34}(-2,y)\}
  >\frac25+\pi\{h_s(x_z-x_y)+x_s(h_z-h_y)\},
 \qquad x_v=\Re v,\quad h_v=\Im v.
 \tag{21}
\]
All additive constants and the conditional normalization are unchanged.
The favorable terms \(-\Re g(y)-\beta\Re g(s)\) have merely been
dropped. The old prefix has \(\Re\mathcal P_{34}(-2,y)>7/4\).

The incoming bounds are \(x_y\in[.24,.36]\), \(h_y\le-.001\).
The ordinary image bounds and the
[private and attached endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give the following sufficient ranges. Every decimal is an exact
rational endpoint.

| Role and type of the next vertex | \(x_s\) | \(h_s\) | \(x_z\) | \(h_z\) |
|---|---|---|---|---|
| Ordinary three | \([.267,.433]\) | \([-.065,.068]\) | \([.267,.433]\) | \([-.065,.068]\) |
| Ordinary four | \([.24,.36]\) | \([-.102,-.001]\) | \([.24,.36]\) | \([-.102,-.001]\) |
| Terminal three | \([.278,.391]\) | \([-.072,.021]\) | \([.376,.438]\) | \([-.019,.037]\) |
| Terminal four | \([.246,.350]\) | \([-.108,-.020]\) | \([.333,.363]\) | \([-.051,-.019]\) |

Consequently the negative of the braces in (21) has the following
upper bounds:
\[
 \begin{array}{c|c|c}
 \text{next vertex}
   &\text{upper bound for the loss}
   &\text{lower bound for the action increment}\\ \hline
 \text{ordinary three}
   &.065\cdot.193+.433\cdot.064=40257/10^6
   &1/4\\
 \text{ordinary four}
   &.102\cdot.120+.36\cdot.101=48600/10^6
   &6/25\\
 \text{terminal three}
   &.072\cdot.198+.391\cdot.018=21294/10^6
   &33/100\\
 \text{terminal four}
   &.108\cdot.123+.350\cdot.050=30784/10^6
   &3/10
 \end{array}
 \tag{22}
\]
Each lower bound in the last column is strict. It follows by
subtracting \(22/7\) times the middle entry from \(2/5\).
For the first row, \(x_z-x_y\in[-.093,.193]\); the negative
product with \(h_s\) is bounded by \(.065\cdot.193\), which
exceeds \(.068\cdot.093\). In the second and fourth rows
\(h_s<0\), so only the positive endpoint of \(x_z-x_y\) can
lower that product. In the terminal-three row the entire difference
is positive. The second product uses the lower bound on \(h_z\)
and upper bound on \(h_y\) in every case.

It follows in particular that
\[
 \begin{array}{c|c}
 \text{next vertex}&\Re\mathcal P_\beta^+(-2,z)\\ \hline
 \text{ordinary three}&>2\\
 \text{ordinary four}&>199/100\\
 \text{terminal three}&>52/25\\
 \text{terminal four}&>41/20 .
 \end{array}
 \tag{23}
\]
Thus all the actual next reference families have the common strict
floor \(199/100\). Uniform compactness supplies smaller fixed
complex neighborhoods for any chosen lower floor below this value.
These are bounds on the same conditional action used throughout this
note. They neither prove a lower bound for the whole finite sum nor
change the two-sector distinction.
