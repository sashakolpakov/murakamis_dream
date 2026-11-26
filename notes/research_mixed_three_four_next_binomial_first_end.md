# A wider first-coordinate deletion by complementary binomial bounds

Superseded draft, retained for derivation provenance. The independently
proved [sectorwise first-end theorem](research_mixed_three_four_next_sectorwise_first_end.md)
pays the larger first-coordinate range \(a\ge\lceil23N/24\rceil\),
separately in both complete Fourier sectors and in the positive
double-root sum. Its combined core and local-packet preservation
replace the weaker \(1/40\) conclusion below; this draft is not a
dependency or a separate completed milestone.

Research deduction, 7 November 2026. The exact complementary
binomial identity pays the last \(1/40\) of the first sampled
coordinate in the next attachment \(34\to343,344\), uniformly
over the entire second sampling period. Combined with the proved
last-\(1/12\) second-coordinate bound, the entire finite source
reduces to a smaller physical rectangle with an exponentially
small error at its original conditional action. No numerical
evaluation or partial-sum-to-arc identification is used.

## 1. The literal double root sum

Keep \(D=N-1\), \(r=e^{-2\pi i/N}\), \(q=e^{\pi i/N}\),
\(P_j=(r;r)_j\), \(S_j=|P_j|\), \(p_j(X)=(rX;r)_j\).
The exact source is
\[
 \mathcal F_{\beta,N}(w,Z)
   =\sum_{a,b=0}^{D} A_{a,b,N}(w,Z),\qquad
 A_{a,b,N}
   =U_{0,N}(w,r^a)C_{1,N}(r^a,r^b)
                          \frac{C_{\beta,N}(r^b,Z)}{P_b},
 \quad\beta=0,1.                                       \tag{1}
\]
As proved in
[the first physical-end theorem, Section 2](research_mixed_three_four_next_first_physical_end.md),
the first constant term has band \([-D,D]\), so its factor \(N\)
is replaced exactly by the first root sum. The second root sum
combines the two original Fourier coefficients and retains the
old-four weight \(1/P_b\). There is no further \(N\),
\(\kappa_N\), or Gram factor in (1).

For \(n=D-a\) and \(0\le j\le n\), the exact reflection and
sine comparison in
[the binomial second-end theorem, Section 1](research_mixed_three_four_next_binomial_end_bound.md)
give
\[
 \frac{S_{a+j}}{S_aS_j}
    =\frac{S_n}{S_{n-j}S_j}\le\binom nj .
                                                               \tag{2}
\]
Every factorial denominator remains nonzero.

## 2. The improved first-cap bound retains its exact termination

At the first sampled coordinate,
\[
 U_{0,N}(w,r^a)
  =\frac{N}{P_a^2}\sum_{\ell=0}^{n}
       (-q)^{-\ell}e_\ell(w)\frac{P_{a+\ell}}{P_\ell^2}.
                                                               \tag{3}
\]
This is the original terminating formula from
[physical far-half bounds](research_mixed_three_four_physical_far_half.md),
equation (7), including its scalar \(N\). Put
\[
                 v=1-a/N,\qquad u=\ell/N<v.
 \]
We use \(v\le1/40<1/6\). The uniform sine-product rate
\(\log S_j=NJ(j/N)+O(\log N)\) includes both endpoints,
and \(J(1-v)=-J(v)\).

On this short support the zero-safe Newton bound is
\[
 |e_\ell(w)|\le C_\tau N^A
    e^{N\{V_0(u)+\tau\}},\qquad
 V_0(u)=-2J(1/2-u)-2J(u)
                       \le2u\log2-2J(u).              \tag{4}
\]
It holds on a sufficiently small fixed complex color disk
about \(-2\). It also holds for every real color, because
the exact Newton entropy satisfies \(V_\theta(u)\le V_0(u)\)
for \(u\le1/2\), as used in
[physical middle reduction, Section 1](research_mixed_three_four_physical_middle_reduction.md).
No off-grid truncation or incomplete endpoint packet is invoked.

Taking absolute values of the exact short sum (3), and applying
(2), gives
\[
 |U_{0,N}(w,r^a)|
    \le \frac{N}{S_a}
        \sum_{\ell=0}^{n}\binom n\ell
                                  \frac{|e_\ell(w)|}{S_\ell}.
                                                               \tag{5}
\]
Since \(J\) decreases on \([0,v]\), (4) bounds the last quotient
by \(C_\tau N^A4^\ell e^{N\{-3J(v)+\tau\}}\).
The identity \(\sum_\ell\binom n\ell4^\ell=5^n\) and
the rate \(J(v)\) of \(S_a^{-1}\) consequently prove
\[
 |U_{0,N}(w,r^a)|
      \le C_\tau N^A
            e^{N\{-2J(v)+v\log5+\tau\}} .
                                                               \tag{6}
\]
This improves the older absolute physical-end estimate; it
does not replace a coherent cap bound elsewhere.

For every second physical index \(b\), the complete first
conditional factor has the exact support \(j\le n\):
\[
 C_{1,N}(r^a,r^b)
   =\sum_{j=0}^{n}
       \frac{r^{-aj}P_{a+j}}{P_aP_j^3}p_j(r^b).
                                                               \tag{7}
\]
Further zeros when \(j+b\ge N\) are retained. Since
\(|p_j(r^b)|\le2^j\), (2) and the same factorial rate give
\[
 |C_{1,N}(r^a,r^b)|
       \le C N^A e^{-2NJ(v)}
                     \sum_{j=0}^{n}\binom nj2^j
       \le C N^A e^{N\{-2J(v)+v\log3\}} .
                                                               \tag{8}
\]
Thus the entire first two-factor product, uniformly in every
physical \(b\), has upper rate
\[
                          -4J(v)+v\log15+\tau .
                                                               \tag{9}
\]

## 3. A uniform estimate for the entire second period

The complete weighted conditional estimate from
[the first physical-end theorem, equation (6)](research_mixed_three_four_next_first_physical_end.md)
is
\[
 \sum_{b=0}^{D}\frac{|C_{\beta,N}(r^b,Z)|}{S_b}
      \le C N^A e^{N\{1+\beta/6+\log_+|Z|\}} .
                                                               \tag{10}
\]
Retain exactly its original outgoing type domains:
\[
 \beta=0:\quad \Im z\le3/40;\qquad
 \beta=1:\quad \Im z\le0;\qquad Z=e^{-2\pi iz}.
                                                               \tag{11}
\]
On either corresponding closed disk in \(Z\), the rate in
(10) is less than \(103/70\). Every actual ordinary and
terminal output belongs strictly inside its appropriate
domain (11).

For \(v\le1/40\), the sine chord \(2\sin\pi t\ge6t\)
on \([0,1/6]\) gives
\[
 -J(v)\le v(1-\log(6v))
       \le\frac1{40}\left(1+\log\frac{20}{3}\right)
                                     <\frac3{40}.
                                                               \tag{12}
\]
The last comparison follows from
\(e^2>\sum_{j=0}^{4}2^j/j!=7>20/3\).
Moreover
\[
 \log5<\frac53,\qquad \log3<\frac{11}{10},\qquad
 \log15<\frac{83}{30}.                                  \tag{13}
\]
The first inequality has the finite witness
\(e^{5/3}>\sum_{j=0}^4(5/3)^j/j!=10009/1944>5\).
For the second,
\(e^{11/10}>\sum_{j=0}^5(11/10)^j/j!
=36015101/12000000>3\).
Combining (9)--(13), before the arbitrary tolerance, yields
\[
 -4J(v)+v\log15+\frac{103}{70}
    <\frac3{10}+\frac{83}{1200}+\frac{103}{70}
     =\frac{15461}{8400}<\frac{37}{20}.
                                                               \tag{14}
\]
The exact reserve is \(79/8400\).

Let \(L_N=\lceil39N/40\rceil\), and define
\[
 \mathcal R_{\beta,N}^{(40)}(w,Z)
      =\sum_{a=L_N}^{D}\sum_{b=0}^{D}A_{a,b,N}(w,Z).
                                                               \tag{15}
\]
Choosing the total color tolerance smaller than the reserve
in (14), then summing the first indices, proves
\[
 \sum_{a=L_N}^{D}\sum_{b=0}^{D}|A_{a,b,N}(w,Z)|
                    \le C N^A e^{37N/20}.             \tag{16}
\]
This holds at both parities, for all real ordinary colors,
and on a sufficiently small fixed complex disk about \(-2\),
throughout the corresponding output domain (11). Fixed real
ordinary derivatives follow by Markov's inequality applied
to each complete first-cap polynomial before summation;
complex color and output derivatives follow by Cauchy's
formula on smaller disks. All these are positive-row
estimates and preserve the true last row and every numerator
zero.

## 4. The combined reduced physical rectangle

Set \(M_N=\lceil11N/12\rceil\), and retain the exact core
\[
 \mathcal C_{\beta,N}^{(40,12)}(w,Z)
      =\sum_{0\le a<L_N}\sum_{0\le b<M_N}A_{a,b,N}(w,Z).
                                                               \tag{17}
\]
Let \(\mathcal E_{\beta,N}^{(12)}\) be the coherent
second-coordinate sector in the binomial second-end theorem.
Then the exact identity is
\[
 \mathcal F_{\beta,N}
   =\mathcal C_{\beta,N}^{(40,12)}
       +\mathcal R_{\beta,N}^{(40)}
       +\mathcal E_{\beta,N}^{(12)}
       -\sum_{a=L_N}^{D}\sum_{b=M_N}^{D}A_{a,b,N}.
                                                               \tag{18}
\]
The first-end estimate (16) pays its intersection term
termwise. The second-end estimate keeps the first-coordinate
sum coherent and has rate \(9/5<37/20\). It is not
restricted by subtracting moduli of parts of that coherent sum.

The independently proved original next action has
\(\Re\mathcal P_\beta^+(-2,z)>15/8\) on all the actual
ordinary and terminal reference families. By compactness,
choose common fixed neighborhoods on which (11) holds and
\[
                    \Re\mathcal P_\beta^+(w,z)>149/80 .
                                                               \tag{19}
\]
These are local ordinary-color neighborhoods; no action
continuation through all real colors is presumed.
Since \(149/80-37/20=1/80\), (16)--(19) and Cauchy's
formula give, for every fixed mixed order,
\[
 \left|\partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
   \{\mathcal F_{\beta,N}(w,e^{-2\pi iz})
       -\mathcal C_{\beta,N}^{(40,12)}(w,e^{-2\pi iz})\}
 \right]\right|
       \le C_{j,k}N^{A_{j,k}}e^{-N/160}.                \tag{20}
\]
For remote real ordinary colors the positive-row estimates
are instead compared with the complete-color action.

The entire next source therefore reduces, with its original
normalization and a calibrated error, to the physical indices
\(a<\lceil39N/40\rceil\), \(b<\lceil11N/12\rceil\).
Both Fourier coefficients remain combined. No partial
physical sum is equated with a contour rectangle, and any
later contour representation of (17) must retain its sampling
kernels, side currents and aliases. The nonzero full-source
contribution and its prescribed ordinary closing remain open.
