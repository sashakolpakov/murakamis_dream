# A high-index cardinal deletion in both complete Fourier sectors

Research deduction, 7 November 2026. The last one percent of the
second physical indices can be removed separately from either complete
Fourier coefficient in the next attachment \(34\to343,344\).
The proof bounds the complete prefix at those nodes, interpolates the
deleted values on the whole unit disk, and then estimates the original
\(d_N C_{\beta,N}\) on the entire coefficient circle. It applies both
before and after the existing first-coordinate deletion.

This is stronger than combining the two coefficients on this narrower
set. It does not upgrade the wider \(b\ge11N/12\) deletion to separate
coefficients, and does not identify any sampled interval with a contour
arc. No numerical evaluation is used.

## 1. The exact projections and sectors

Put
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad S_j=|P_j|,\quad p_j(Y)=(rY;r)_j.
 \tag{1}
\]
Use the complete original sources
\[
 \begin{split}
 U_{0,N}(w,X)&=\sum_{\ell=0}^{D}
                    H_N(w,r^{-\ell})p_\ell(X)/P_\ell,\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{D}
           \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
                 \qquad\beta=0,1,\\
 F_N(w,Y)&=N\operatorname{CT}_X
                   [U_{0,N}(w,X)C_{1,N}(X,Y)].
 \end{split}
 \tag{2}
\]
The exact first root sum is
\[
 F_N(w,Y)=\sum_{a=0}^{D}
                  U_{0,N}(w,r^a)C_{1,N}(r^a,Y).
 \tag{3}
\]
Its normalization and all coherent coefficients are those of the
[next-attachment identity](research_mixed_three_four_next_conditional_attachment.md).

Let \(d_N\) be the degree-\(D\) polynomial satisfying
\(d_N(r^b)=P_b^{-1}\). For a degree-\(D\) polynomial \(E\), write
\[
 \mathcal S_{\sigma,\beta}[E](w,Z)
     =N[Y^{\sigma N}]
           \{E(w,Y)d_N(Y)C_{\beta,N}(Y,Z)\},
                  \qquad \sigma=0,1.
 \tag{4}
\]
These are exactly the functionals of
[cardinal sector separation](research_mixed_next_cardinal_sector_separation.md),
Section 1. Their sum is
\[
 \mathcal S_{0,\beta}[E]+\mathcal S_{1,\beta}[E]
       =\sum_{b=0}^{D}\frac{E(w,r^b)}{P_b}
                                      C_{\beta,N}(r^b,Z).
 \tag{5}
\]
The Laurent band is \([-D,2D]\); thus no third sampled frequency
or extra Gram factor occurs in (4)--(5).

Set
\[
 B_N=\lceil99N/100\rceil,\qquad
 I_N\subset\{B_N,\ldots,D\},\qquad
 \Pi_I E(Y)=\sum_{b\in I_N}E(r^b)\mathfrak l_b(Y),
 \quad
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu.
 \tag{6}
\]
The set \(I_N\) is arbitrary; an empty set is allowed. In particular
the estimates below are uniform over all subsets of this final band.
On \(|Y|\le1\), one has \(|\mathfrak l_b(Y)|\le1\).

For the first-coordinate deletion retain precisely
\[
 \begin{split}
 A_N&=\lceil23N/24\rceil,\\
 R_N^a(w,Y)&=\sum_{a=A_N}^{D}
                       U_{0,N}(w,r^a)C_{1,N}(r^a,Y),\\
 F_N^{<}&=F_N-R_N^a.
 \end{split}
 \tag{7}
\]
These are the complete polynomials of
[the first-coordinate sector theorem](research_mixed_three_four_next_sectorwise_first_end.md),
not restrictions of a continuous contour.

## 2. The complete high-node prefix on the unit disk

Let
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 \rho(v)=(1+v)\log(1+v)-v\log v,\quad \rho(0)=0,
 \quad b_1=433/500.
 \tag{8}
\]
For \(n=D-b\), the exact incoming support and complementary
binomial inequality give
\[
 \begin{split}
 F_N(w,r^b)
    &=N\sum_{j=0}^{n}
           \frac{P_{b+j}}{P_bP_j^3}T_{j,N}(w),\\
 T_{j,N}(w)&=\operatorname{CT}_X
                    [X^{-j}p_j(X)U_{0,N}(w,X)],\\
 \frac{S_{b+j}}{S_bS_j}&\le\binom nj,\qquad
 |T_{j,N}(w)|
    \le C_\tau N^{A_\tau}
           e^{N(b_1+\tau)}\binom{N+j}{j}.
 \end{split}
 \tag{9}
\]
These are equations (5)--(10) of
[the binomial end bound](research_mixed_three_four_next_binomial_end_bound.md),
with its coherent seam source. In particular the \(H_N\) coefficients
inside \(T_{j,N}\) remain complete; no absolute bound on their
individual Newton summands is used.

For \(b\in I_N\), put \(v=1-b/N\le1/100\). Since
\(j/N<v<1/6\), \(J\) decreases and \(\rho\) increases on the
required interval. The uniform sine-factorial estimate, including
the true endpoints, and the ordinary binomial theorem imply
\[
 |F_N(w,r^b)|\le C_\tau N^{A_\tau}
    \exp N\{b_1+\rho(v)-2J(v)+v\log2+\tau\}.
 \tag{10}
\]
This holds for every real ordinary color \(w\in[-2,2]\), and,
for every chosen \(\tau>0\), on a sufficiently small fixed complex
disk about \(w=-2\).

The following elementary witnesses give a uniform small rate.
First,
\[
 (1+v)\log(1+v)\le v+v^2/2.
 \tag{11}
\]
Indeed the difference of the right side and the left side has
derivative \(v-\log(1+v)\ge0\) and vanishes at zero.
The right side of
\(\rho(v)\le v+v^2/2-v\log v\) increases on the present interval.
Also
\[
 e^5>\sum_{j=0}^{6}\frac{5^j}{j!}
       =\frac{81445}{720}>100,\qquad
 e^3>\sum_{j=0}^{5}\frac{3^j}{j!}
       =\frac{92}{5}>\frac{50}{3}.
 \tag{12}
\]
Thus \(\log100<5\), \(\log(50/3)<3\), and
\[
 \rho(v)<\frac{1201}{20000},\qquad
 -J(v)\le v\{1-\log(6v)\}
       \le\frac{1+\log(50/3)}{100}<\frac1{25}.
 \tag{13}
\]
The sine chord \(2\sin\pi u\ge6u\) on \([0,1/6]\) proves the
second inequality, with its continuous value at zero.
Finally \(v\log2<7/1000\), using the existing elementary
\(\log2<7/10\). Hence the limiting rate in (10) is less than
\[
 \frac{433}{500}+\frac{1201}{20000}
                     +\frac2{25}+\frac7{1000}
              =\frac{20261}{20000}=:B_{\rm hi}.
 \tag{14}
\]
Summing at most \(N\) cardinal polynomials yields
\[
 \sup_{|Y|\le1}|\Pi_I F_N(w,Y)|
       \le C_\tau N^{A_\tau}e^{N(B_{\rm hi}+\tau)}.
 \tag{15}
\]
Every added off-grid row is included by this polynomial estimate.

The first-coordinate theorem, equation (14), separately gives
\[
 \sup_{|Y|\le1}|R_N^a(w,Y)|
       \le C_\tau N^{A_\tau}e^{N(371/720+\tau)}.
 \tag{16}
\]
Cardinal projection costs at most another factor \(N\), so the same
rate holds for \(\Pi_I R_N^a\). Consequently (15) also holds with
\(F_N\) replaced by \(F_N^{<}\), using the exact subtraction
\(\Pi_I F_N^{<}=\Pi_I F_N-\Pi_I R_N^a\).

## 3. The whole \(d_N C_\beta\) on the coefficient circle

Put \(c_{\rm b}=-2J(1/6)<1/3\). The original uniform factorial
estimate gives \(-J(t)\le c_{\rm b}/2\) for \(0\le t\le1\).
The finite \(q\)-binomial formula, with unit-modulus coefficients,
therefore gives
\[
 \frac{|p_j(Y)|}{S_j}
   \le\sum_{k=0}^{j}\frac1{S_kS_{j-k}}
   \le C N^A e^{Nc_{\rm b}},\qquad |Y|=1,\quad j<N.
 \tag{17}
\]
This is the whole-index bound in
[global transform ends, Section 2](research_mixed_three_four_global_transform_ends.md).
All its denominator indices are below \(N\). The exact cardinal
formula, including the polynomial forcing in \(d_N\), gives
\[
 d_N(Y)=\sum_{b=0}^{D}P_b^{-1}\mathfrak l_b(Y),\qquad
 \sup_{|Y|=1}|d_N(Y)|
          \le C N^A e^{Nc_{\rm b}/2}.
 \tag{18}
\]

The output disks here are
\[
 \beta=0:\quad |Z|\le R_0:=e^{17\pi/125},
 \qquad
 \beta=1:\quad |Z|\le1.
 \tag{19}
\]
They contain every actual ordinary and terminal output of its type.
For a next three this follows from the ordinary height bound
\(\Im z<17/250\) and terminal private height bound
\(\Im z<37/1000\); for a next four both heights are strictly
negative. These are precisely the domains of
[the low-index kernel margin](research_mixed_next_low_index_kernel_margin.md),
Section 2.

The same note proves the full outgoing-row bounds
\[
 \sum_{j=0}^{D}\frac{|p_j(Z)|}{S_j^{1+\beta}}
       \le C_\tau N^{A_\tau}e^{N(m_\beta+\tau)},
 \qquad
 m_0=\frac{1271}{2500},\quad m_1=\frac7{15}.
 \tag{20}
\]
This follows there from the centered-arc numerator profile on the
entire disk, not from a terminating outgoing support.
On the circle \(|Y|=1\), the factor \(Y^{-j}\) has modulus one.
Combining (17)--(20) in the complete sum (2) proves
\[
 \sup_{\substack{|Y|=1\\Z\ {\rm in}\ (19)}}
       |d_N(Y)C_{\beta,N}(Y,Z)|
       \le C_\tau N^{A_\tau}
                    e^{N(1/2+m_\beta+\tau)}.
 \tag{21}
\]
Both numerator products, all rows \(0\le j<N\), and all zeros
are retained. There is no reciprocal-factorial substitution for
\(d_N(Y)\) on this circle.

## 4. Separate complete-sector bounds, including the overlap

The coefficient formula in (4) on \(|Y|=1\) has a multiplier of
modulus one for either \(\sigma\). Thus (15) and (21) bound
each sector of \(\Pi_I F_N\) and \(\Pi_I F_N^{<}\).
Since \(m_1<m_0\), their common limiting rate is less than
\[
 B_{\rm hi}+\frac12+\frac{1271}{2500}
     =\frac{40429}{20000}
     =\frac{203}{100}-\frac{171}{20000}.
 \tag{22}
\]
Choose the aggregate finite and complex-color allowances smaller
than \(171/20000\). The factor \(N\) in (4) and all finite
cardinal sums cost only polynomial powers.

**Theorem 1.** Uniformly for the disks (19), both level parities,
all real ordinary colors and a sufficiently small fixed complex
color disk about \(-2\),
\[
 \begin{split}
 |\mathcal S_{\sigma,\beta}[\Pi_I F_N](w,Z)|
       &\le C N^A e^{203N/100},\\
 |\mathcal S_{\sigma,\beta}[\Pi_I F_N^{<}](w,Z)|
       &\le C N^A e^{203N/100},
            \qquad \sigma=0,1.
 \end{split}
 \tag{23}
\]
The constants are independent of the subset \(I_N\) in (6).

For clarity, the overlap in the second line is itself controlled:
\[
 |\mathcal S_{\sigma,\beta}[\Pi_I R_N^a]|
 \le C_\tau N^{A_\tau}
       e^{N\{371/720+1/2+m_\beta+\tau\}}.
 \tag{24}
\]
This follows from (16) and (21); the same rate bounds
\(\mathcal S_{\sigma,\beta}[R_N^a]\).
In particular \(371/720< B_{\rm hi}\), so (24) is covered by
the rate in (23). No estimate of an arbitrary truncated coherent
first-index sum is inferred from a bound for that full sum.

Define the twice-filtered polynomial
\[
 F_N^{\sharp}=(I-\Pi_I)(F_N-R_N^a).
 \tag{25}
\]
The exact correction identity is
\[
 F_N-F_N^\sharp
       =R_N^a+\Pi_I F_N-\Pi_I R_N^a.
 \tag{26}
\]
Every term on the right has a separate bound in (23)--(24).
Therefore each original full Fourier coefficient changes by at
most \(C N^A e^{203N/100}\) under (25). At physical nodes, (25)
is exactly the first-root truncation \(a<A_N\) with the second
indices \(b\in I_N\) deleted. Its full contour meaning remains
the degree-\(D\) polynomial (25), not a cropped incoming arc.

There is no omitted divided-difference correction in this argument.
In the notation of the exact sector-separation note, set
\[
 Q_I(Y)=\sum_{b\in I_N}F_N(w,r^b)
        \frac{r^b}{N}\frac{d_N(Y)-P_b^{-1}}{Y-r^b}.
 \tag{27}
\]
Then the two exact errors are respectively
\[
 \begin{split}
 \mathcal S_{1,\beta}[\Pi_I F_N]
       &=N\operatorname{CT}_Y[Q_I(Y)C_{\beta,N}(Y,Z)],\\
 \mathcal S_{0,\beta}[\Pi_I F_N]
       &=\sum_{b\in I_N}\frac{F_N(w,r^b)}{P_b}
                         C_{\beta,N}(r^b,Z)
           -N\operatorname{CT}_Y[Q_I(Y)C_{\beta,N}(Y,Z)].
 \end{split}
 \tag{28}
\]
Both complete expressions in (28) are bounded by (23), because
the whole circle estimate precedes coefficient extraction.
The proof does not discard \(Q_I\) on the grounds that its two
copies cancel in the sum. The identical formulas and bounds hold
with \(F_N^{<}\) in place of \(F_N\).

## 5. Actual action comparison, derivatives, and the local source

The original next conditional action is denoted
\(\mathcal P_\beta^+(w,z)\), with \(Z=e^{-2\pi iz}\).
The kernel-margin theorem, equation (23), proves
\[
 \begin{array}{c|c}
 \text{reference family}&\Re\mathcal P_\beta^+(-2,z)\\ \hline
 \text{ordinary next three}&>2+\chi\\
 \text{terminal next three}&>52/25+\chi\\
 \text{ordinary next four}&>199/100+2\chi\\
 \text{terminal next four}&>41/20+2\chi
 \end{array}
 \qquad \chi=\frac{117}{800\pi}>\frac{819}{17600}>\frac1{25}.
 \tag{29}
\]
These are the matched ordinary conditional images and terminal
graphs of the original local next-source theorem. In particular
their common action floor is strictly greater than \(51/25\);
no independent product of containing rectangles replaces those
reference families.

Choose fixed smaller neighborhoods of these compact families,
inside (19), and a small complete-color disk, on which
\[
                  \Re\mathcal P_\beta^+(w,z)>51/25.
 \tag{30}
\]
The difference between \(51/25\) and \(203/100\) is \(1/100\).
For any one of the sector errors in (23), (24), or (26), denoted
\(\mathcal E_{\sigma,\beta,N}\), Cauchy's formula on smaller
neighborhoods therefore gives
\[
 \left|\partial_w^j\partial_z^k
       \left[e^{-N\mathcal P_\beta^+(w,z)}
          \mathcal E_{\sigma,\beta,N}(w,e^{-2\pi iz})\right]\right|
       \le C_{j,k}e^{-N/200}
 \tag{31}
\]
for every fixed pair of derivative orders. Polynomial prefactors
are absorbed by the weaker exponent. Real ordinary-color
derivatives also retain the absolute bounds (23): apply Markov
to the complete \(T_{j,N}(w)\) in (9) and the complete first-cap
polynomials in (16), before the positive sums and interpolation.
For output derivatives, use Cauchy on smaller disks; alternatively
their degree \(D\) permits a radius enlargement of order \(N^{-1}\)
at polynomial cost. These operations retain the original ordinary
normal data and both level parities.

The same deletion preserves the proved local prefix asymptotic.
At every actual matching input \(y=q_{34}(s_3)\), the completed
following-prefix theorem has
\[
 |e^{-2\pi iy}|<1,\qquad
                  \Re\mathcal P_{34}(-2,y)>7/4.
 \tag{32}
\]
By (15)--(16) and (26), the whole unit-disk correction has rate
at most \(B_{\rm hi}+\tau<11/10\), with a fixed sufficiently
small tolerance. On fixed smaller matching neighborhoods keep
\(\Re\mathcal P_{34}(w,y)>3/2\). The normalized correction and
all fixed mixed derivatives are then \(O(e^{-N/4})\).
Consequently
\[
 F_N^\sharp(w,e^{-2\pi iy})
   =N^{-3/2}\mathcal A_{34}(w,y)e^{N\mathcal P_{34}(w,y)}
                            (1+O_{\rm hol}(N^{-1})),
 \tag{33}
\]
with the same nonzero coefficient and absolute action. The same
statement holds for \((I-\Pi_I)F_N\).
Substitution into the actual local next integral preserves its
nonzero \(N^{-2-\beta/2}\) coefficient and its fixed derivatives.
Its full \(d_N C_{\beta,N}\) factors remain present.

All estimates use the conditional normalization (2)--(5).
The later ordinary outgoing observation retains the original
matrix and scalar adapters of the next-attachment identity.
This theorem does not replace those adapters by point evaluation.

For \(I_N=\{B_N,\ldots,D\}\), (23) pays a nonempty final band
in each whole Fourier coefficient for all sufficiently large \(N\).
The broader \(b\ge\lceil11N/12\rceil\) and low-\(b\) deletions
remain proved for their combined sampled sum, with the separate
selected-plateau correction theorem applying on its stated contour.
No separate suppression of either entire broader correction is
inferred here. The complete remaining middle coefficient and its
prescribed closing observation are still separate obligations.
