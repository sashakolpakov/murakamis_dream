# A first-coordinate end bound for each next Fourier sector

Research deduction, 7 November 2026. In the exact attachment
\(34\to343,344\), the first sampled indices
\(a\ge\lceil23N/24\rceil\) may be removed separately from each
of the two complete Fourier coefficients. The proof first bounds
their entire polynomial in the second variable on its unit disk,
then retains the exact reciprocal-factorial polynomial and the
whole next conditional kernel. It also gives a positive bound for
the corresponding double root rectangle. No partial root sum is
identified with a contour arc.

## 1. Exact source and the first-coordinate polynomial

Put
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad q=e^{\pi i/N},\quad
 P_j=(r;r)_j,\quad S_j=|P_j|,\quad p_j(Y)=(rY;r)_j.
 \tag{1}
\]
All factorial denominators below have indices between zero and
\(D\). The literal kernels and prefix are
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{\ell=0}^{D}
                  \frac{H_N(w,r^{-\ell})}{P_\ell}p_\ell(X),\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{D}
             \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
                      \qquad \beta=0,1,\\
 F_N(w,Y)&=N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)]
          =\sum_{a=0}^{D}U_{0,N}(w,r^a)C_{1,N}(r^a,Y).
\end{split}                                                    \tag{2}
\]
The last equality uses the exact \(X\)-band \([-D,D]\);
there is no nonzero multiple of \(N\) in that band.
Thus no scalar is lost when replacing the first constant term
by the first root sum. These are the sources in
[the next-attachment identity, equations (2)--(5)](research_mixed_three_four_next_conditional_attachment.md).

Let \(d_N\) be the unique polynomial of degree at most \(D\)
with \(d_N(r^b)=1/P_b\). For \(\sigma=0,1\), define
\[
 \mathcal S_{\sigma,\beta,N}(w,Z)
   =N[Y^{\sigma N}]
           \{F_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z)\}.
 \tag{3}
\]
Their sum is the exact next conditional source
\(\mathcal F_{\beta,N}\). Its \(Y\)-band before coefficient
extraction is \([-D,2D]\), so the two sectors in (3) are
precisely the two terms of the original root average.

Set
\[
\begin{split}
 L_N&=\lceil23N/24\rceil,\\
 R_N(w,Y)&=\sum_{a=L_N}^{D}
                  U_{0,N}(w,r^a)C_{1,N}(r^a,Y),\\
 F_N^{<}(w,Y)&=\sum_{a=0}^{L_N-1}
                  U_{0,N}(w,r^a)C_{1,N}(r^a,Y).
\end{split}                                                    \tag{4}
\]
Empty sums have their usual value zero. Both functions are entire
polynomials of degree at most \(D\) in \(Y\), and
\(F_N=F_N^{<}+R_N\) exactly.

## 2. A positive bound on the entire unit disk

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 \log S_j=NJ(j/N)+O(\log N).
 \tag{5}
\]
The error in (5) is uniform through both true endpoint indices.
Reflection gives \(S_bS_{D-b}=N\) and \(J(1-v)=-J(v)\).
For \(n=D-a\) and \(0\le j\le n\),
\[
 \frac{S_{a+j}}{S_aS_j}
   =\frac{S_n}{S_{n-j}S_j}\le\binom nj .
 \tag{6}
\]
Indeed \(\sin t/t\) decreases on \((0,\pi)\), so each factor
in the sine-product quotient is bounded by the corresponding
factor of the ordinary binomial coefficient. This is the exact
complementary binomial inequality in
[the final incoming-row bound, Section 1](research_mixed_three_four_next_binomial_end_bound.md).

The original terminating first-cap formula is
\[
 U_{0,N}(w,r^a)=\frac{N}{P_a^2}
       \sum_{\ell=0}^{n}(-q)^{-\ell}e_\ell(w)
                                     \frac{P_{a+\ell}}{P_\ell^2}.
 \tag{7}
\]
Its scalar and phases are those in
[physical far-half bounds, equation (7)](research_mixed_three_four_physical_far_half.md).
Put \(v=1-a/N\le1/24\). On the exact support
\(u=\ell/N<v\), the original zero-safe Newton estimate gives
\[
 |e_\ell(w)|\le C_\tau N^A e^{N\{V_0(u)+\tau\}},\qquad
 V_0(u)=-2J(1/2-u)-2J(u)\le2u\log2-2J(u).
 \tag{8}
\]
It holds on a sufficiently small fixed complex color disk about
\(-2\), for every prescribed \(\tau>0\). It also holds for all
real ordinary colors \(w\in[-2,2]\), because
\(V_\theta(u)\le V_0(u)\) on \(u\le1/2\), as used in
[physical middle reduction, Section 1](research_mixed_three_four_physical_middle_reduction.md).
This use of (7) keeps the entire terminating Newton sum.

The function \(J\) decreases on \([0,1/6]\). Equations
(5)--(8), followed by the binomial theorem, therefore give
\[
\begin{split}
 |U_{0,N}(w,r^a)|
 &\le \frac{N}{S_a}\sum_{\ell=0}^{n}
                      \binom n\ell\frac{|e_\ell(w)|}{S_\ell}\\
 &\le C_\tau N^A
             e^{N\{-2J(v)+v\log5+\tau\}}.
\end{split}                                                    \tag{9}
\]
Here \(|e_\ell|/S_\ell\) is bounded by
\(C_\tau N^A4^\ell e^{N(-3J(v)+\tau)}\), and
\(\sum_\ell\binom n\ell4^\ell=5^n\). The reciprocal \(S_a\)
contributes the favorable rate \(J(v)\).

For every complex \(|Y|\le1\), the first conditional factor
still terminates because its incoming argument is physical:
\[
 C_{1,N}(r^a,Y)
   =\sum_{j=0}^{n}
      \frac{r^{-aj}P_{a+j}}{P_aP_j^3}p_j(Y).
 \tag{10}
\]
All outgoing rows in this formula are retained. The uniform
inequality \(|p_j(Y)|\le2^j\), not a second physical support
restriction, and (6) prove
\[
 |C_{1,N}(r^a,Y)|
 \le C N^A e^{-2NJ(v)}\sum_{j=0}^{n}\binom nj2^j
 \le C N^A e^{N\{-2J(v)+v\log3\}}.
 \tag{11}
\]
Thus the entire product in (4), termwise in \(a\), has rate
\(-4J(v)+v\log15+\tau\) on the closed unit disk.

For \(0\le v\le1/24\), the sine chord
\(2\sin\pi u\ge6u\) on \([0,1/6]\) gives
\[
 -J(v)\le v(1-\log(6v))
 \le\frac{1+\log4}{24}<\frac1{10}.
 \tag{12}
\]
Use \(\log2<7/10\), \(\log3<11/10\), and
\(\log5<5/3\), with the finite positive exponential witnesses
for the first and third recorded in the binomial end proof.
For the second, the explicit local witness is
\[
 e^{11/10}>
       \sum_{j=0}^{5}\frac{(11/10)^j}{j!}
       =\frac{36015101}{12000000}>3.
 \tag{12a}
\]
In particular
\[
 -4J(v)+v\log15
       <\frac25+\frac{83}{720}
       =\frac{371}{720}.
 \tag{13}
\]
Summing the at most \(N\) first indices gives the positive bound
\[
 \boxed{\quad
 \sum_{a=L_N}^{D}
    |U_{0,N}(w,r^a)C_{1,N}(r^a,Y)|
 \le C_\tau N^A e^{N(371/720+\tau)},\qquad |Y|\le1.
 \quad}                                                       \tag{14}
\]
The strict reserve in the later comparison will pay the single
prescribed tolerance. Formula (14) includes every numerator zero
and both level parities.

## 3. The exact Fourier polynomial and conditional factor on a circle

Put
\[
 c_{\rm b}=-2J(1/6)<1/3,\qquad |J(t)|\le c_{\rm b}/2.
 \tag{15}
\]
The finite \(q\)-binomial formula, with all phases of modulus one,
implies
\[
 \frac{|p_j(W)|}{S_j}
 \le \sum_{k=0}^{j}\frac{|W|^k}{S_kS_{j-k}}
 \le C N^A e^{N\{c_{\rm b}+\log_+|W|\}},
                   \qquad 0\le j<N.
 \tag{16}
\]
This is the whole-index estimate of
[global transform ends, Section 2](research_mixed_three_four_global_transform_ends.md).

The exact interpolation formula for \(d_N\) can be written without
any apparent denominators:
\[
 d_N(Y)=\frac1N\sum_{b=0}^{D}\frac1{P_b}
                       \sum_{k=0}^{D}(Yr^{-b})^k.
 \tag{17}
\]
It is precisely the polynomial of
[Fourier-weight continuation, equation (2)](research_mixed_fourier_weight_continuation.md).
On \(|Y|=1\), (5), (15), and (17) give
\[
 |d_N(Y)|\le\sum_{b=0}^{D}S_b^{-1}
             \le C N^A e^{Nc_{\rm b}/2}.
 \tag{18}
\]
No reciprocal-factorial replacement or deletion of its forcing
is made.

Apply (16) to both numerator quotients in each row of
\(C_{\beta,N}(Y,Z)\). The remaining denominator is \(S_j^\beta\);
the incoming chirp has modulus one on this circle. Hence
\[
 |C_{\beta,N}(Y,Z)|
 \le C N^A
       e^{N\{(2+\beta/2)c_{\rm b}+\log_+|Z|\}},
                         \qquad |Y|=1.
 \tag{19}
\]
Every finite index remains in the positive sum proving (19).
Combining (18)--(19) gives rate
\((5+\beta)c_{\rm b}/2+\log_+|Z|\).

Use the two type-dependent closed output disks
\[
 \beta=0:\ |Z|\le e^{3\pi/20},
 \qquad
 \beta=1:\ |Z|\le1.
 \tag{20}
\]
Every actual ordinary and terminal next output lies strictly
inside its corresponding disk, by the original ordinary heights
and private endpoint rectangles cited in
[the first physical-end theorem, equation (8)](research_mixed_three_four_next_first_physical_end.md).
For \(\beta=0\) the last rate is less than
\[
 \frac56+\frac{3\pi}{20}<\frac{137}{105};
 \tag{21}
\]
for \(\beta=1\) it is less than one.

## 4. Each complete sector and the positive root rectangle

Define the two first-end coefficient errors
\[
 \mathcal E_{\sigma,\beta,N}^{a}(w,Z)
  =N[Y^{\sigma N}]
       \{R_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z)\},
                         \qquad \sigma=0,1.
 \tag{22}
\]
Cauchy's coefficient formula on \(|Y|=1\) is valid for this
finite Laurent polynomial and has multiplier of modulus one for
either coefficient. Thus (14), (18)--(21) imply an upper rate
strictly below
\[
 \frac{371}{720}+\frac{137}{105}
       =\frac{9173}{5040}
       =\frac{11}{6}-\frac{67}{5040}.
 \tag{23}
\]
The \(\beta=1\) rate is smaller. Choose the total tolerance
in (14) below the reserve in (23).

**Theorem 1.** On (20), for both parities and all sufficiently
large levels,
\[
 |\mathcal E_{\sigma,\beta,N}^{a}(w,Z)|
          \le C N^A e^{11N/6},\qquad \sigma=0,1.
 \tag{24}
\]
This holds for all real ordinary colors and on a sufficiently
small fixed complex color disk about \(-2\).
In particular each original sector (3) differs by the error (22)
from the same complete coefficient with \(F_N\) replaced by
the exact polynomial \(F_N^{<}\).

There is also a positive double-root conclusion. Let
\[
 A_{a,b,N}(w,Z)=U_{0,N}(w,r^a)C_{1,N}(r^a,r^b)
                              \frac{C_{\beta,N}(r^b,Z)}{P_b}.
 \tag{25}
\]
At each physical \(Y=r^b\), use (14), (19), and the direct
bound \(S_b^{-1}\le C N^A e^{Nc_{\rm b}/2}\). Summing all
\(b\) incurs only a polynomial factor. The same budget (23) proves
\[
 \boxed{\qquad
 \sum_{a=L_N}^{D}\sum_{b=0}^{D}|A_{a,b,N}(w,Z)|
                  \le C N^A e^{11N/6}.
 \qquad}                                                       \tag{26}
\]
Thus every subset of this first-end rectangle has the same
positive bound. Assertion (26) is proved before summing signs;
it is not inferred from the coefficient estimates (24).

Fixed ordinary derivatives in these bounds cost powers of \(N\).
For real colors apply Markov's inequality to each complete
first-cap polynomial before the positive sums in (14) and (26).
For complex colors and output derivatives use Cauchy's formula
on smaller disks. The exact output polynomials have degree at most
\(D\); all actual outputs are strictly interior to (20).

The original next-action comparison gives
\(\Re\mathcal P_\beta^+(-2,z)>15/8\) on the compact ordinary
and terminal families. Choose fixed neighborhoods inside (20)
on which
\[
                     \Re\mathcal P_\beta^+(w,z)>89/48.
 \tag{27}
\]
The difference between \(89/48\) and \(11/6\) is \(1/48\).
After shrinking the neighborhoods, Cauchy's formula therefore gives
for every fixed pair of orders
\[
 \left|\partial_w^j\partial_z^k
  \left[e^{-N\mathcal P_\beta^+(w,z)}
      \mathcal E_{\sigma,\beta,N}^{a}(w,e^{-2\pi iz})\right]\right|
 \le C_{j,k}N^{A_{j,k}}e^{-N/96}.
 \tag{28}
\]
The same conclusion holds for the sum over any fixed subset in
(26). For all real ordinary colors the absolute estimates are
instead compared with the complete-color action; no continuation
of that action through the entire real color interval is asserted.

## 5. Combining with the second-coordinate end bound

Set \(M_N=\lceil11N/12\rceil\) and retain the exact core
\[
 \mathcal C_{\beta,N}^{(24,12)}
    =\sum_{0\le a<L_N}\sum_{0\le b<M_N}A_{a,b,N}.
 \tag{29}
\]
Let \(\mathcal R^a=\sum_{a\ge L_N,b}A_{a,b,N}\), and let
\(\mathcal E^b=\sum_{b\ge M_N}F_N(w,r^b)C_{\beta,N}(r^b,Z)/P_b\)
be the coherent second-end sum in
[the binomial final-row theorem](research_mixed_three_four_next_binomial_end_bound.md).
Then
\[
 \mathcal F_{\beta,N}
  =\mathcal C_{\beta,N}^{(24,12)}
      +\mathcal R^a+\mathcal E^b
      -\sum_{a=L_N}^{D}\sum_{b=M_N}^{D}A_{a,b,N}.
 \tag{30}
\]
The intersection is controlled termwise by (26), while
\(\mathcal E^b\) has the already proved rate \(9/5<11/6\).
The coherent first-coordinate sum in that second-end theorem
has not been restricted by subtracting moduli. Equations
(26)--(30) give the normalized bound (28), with its left side
replaced by the corresponding derivative of
\[
 e^{-N\mathcal P_\beta^+(w,z)}
       \{\mathcal F_{\beta,N}
                        -\mathcal C_{\beta,N}^{(24,12)}\}.
 \tag{31}
\]
The positive real-color and fixed-derivative versions remain valid.

The first deletion (22) is valid separately for either complete
Fourier coefficient because it was proved on an entire coefficient
circle. The second deletion in (30) still concerns their combined
physical sampling identity. Neither deletion removes a real interval
from a continuous contour. In particular a later representation of
(29) must retain its own sampling kernels, side currents and aliases.
The estimates do not yet control the remaining parts of either
complete Fourier contour or prove a whole next-prefix asymptotic.

## 6. The truncated polynomial keeps the geometric contribution

The deletion also respects the already proved local source, rather
than merely its geometric phase. On every actual following family
\(y=q_{34}(c)\), the output belongs to \(O_4\), so
\[
 |e^{-2\pi iy}|<1,\qquad
                  \Re\mathcal P_{34}(-2,y)>7/4.
 \tag{32}
\]
These are the actual image and action conclusions used by
[the complete following-prefix theorem](research_mixed_three_four_following_complete_prefix.md).
On fixed smaller neighborhoods of their compact families, retain
\(|e^{-2\pi iy}|<1\) and
\(\Re\mathcal P_{34}(w,y)>13/8\).
The difference
\[
             \frac{13}{8}-\frac{371}{720}
                         =\frac{799}{720}>1
 \tag{33}
\]
and (14), with a smaller total tolerance, show that
\(e^{-N\mathcal P_{34}}R_N\) and all its fixed mixed derivatives
are bounded by a polynomial times \(e^{-N}\) on still smaller
neighborhoods.

Consequently the exact truncated polynomial has the same nonzero
asymptotic expansion as the full prefix:
\[
 F_N^{<}(w,e^{-2\pi iy})
   =N^{-3/2}\mathcal A_{34}(w,y)e^{N\mathcal P_{34}(w,y)}
                           (1+O_{\rm hol}(N^{-1})).
 \tag{34}
\]
Both the absolute action and the original coefficient
\(\mathcal A_{34}\ne0\) are unchanged. This applies at all
ordinary and terminal matching references of
[the next local-source theorem](research_mixed_three_four_next_local_source.md),
since its required input is exactly \(y=q_{34}(s_3)\).
Replacing \(F_N\) by \(F_N^{<}\) in that theorem's actual local
unwrapped integral therefore retains its
\(N^{-2-\beta/2}\) leading term and every fixed derivative.
The whole \(d_N C_{\beta,N}\) factors are still present.

Thus the first-coordinate deletion preserves the known local
geometric contribution and has a separately paid error in each
whole Fourier coefficient. The remaining coefficient of
\(F_N^{<}d_NC_{\beta,N}\) still needs its nonlocal contour bounds.
