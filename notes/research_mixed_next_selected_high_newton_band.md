# The large Newton indices in the selected next coefficient

Research deduction, 8 November 2026. A fixed band of large Newton
indices in the complete three/four prefix contributes exponentially
less than the geometric next-three or next-four action. The proof
keeps a complementary factorial in the incoming coefficient until
it cancels the factorials in the exact quotient formula.

The indices here are the Newton indices in the prefix polynomial.
They are not physical color indices, and they are not the monomial
degree selected by Fourier extraction. The middle Newton indices
are not estimated. No numerical evaluation is used.

## 1. The complete source and the band being estimated

Use the exact notation of
[the selected quotient theorem](research_mixed_next_selected_wrap_quotient.md):
\[
 \begin{gathered}
 D=N-1,\quad r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad S_j=|P_j|,
 \quad p_j(Y)=(rY;r)_j,\quad f_j(Y)=p_j(Y)/P_j,\\
 U_N(w,X)=\sum_{e=0}^{D}H_N(w,r^{-e})f_e(X),\\
 C_{\beta,N}(Y,Z)=\sum_{j=0}^{D}
           Y^{-j}f_j(Y)f_j(Z)/P_j^\beta,\qquad\beta=0,1,\\
 F_N(w,Y)=F_{34,N}(w,Y)
       =N\operatorname{CT}_X[U_N(w,X)C_{1,N}(X,Y)]
       =\sum_{i=0}^{D}a_{i,N}(w)f_i(Y).
 \end{gathered}
 \tag{1}
\]
Every coefficient \(a_{i,N}\) is the complete original coefficient.
The quotient theorem proves
\[
 a_{i,N}(w)=\frac1{P_i}\sum_{b=0}^{D-i}
                    U_N(w,r^b)\overline{f_i(r^b)}
 \tag{2}
\]
and, for the original polynomial \(d_N\),
\[
 f_i d_N=(Y^N-1)Q_i+R_i,\qquad
 Q_i=\sum_{m=0}^{i-1}q_{i,m}p_m,\qquad \deg R_i<N,
 \tag{3}
\]
with the exact finite estimate
\[
 |q_{i,m}|\le
          \frac{S_{i-m-1}}{N^2}+\frac1{N S_{m+1}}.
 \tag{4}
\]
All denominator indices are below \(N\).

Fix
\[
              \delta=\frac1{16},\qquad n_N=\lfloor N/16\rfloor,
              \qquad I_N\subset\{D-n_N,\ldots,D\}.
 \tag{5}
\]
The subset \(I_N\) is arbitrary and depends only on the level.
For sufficiently large \(N\), every index in this range is positive.
Define its actual selected contribution by
\[
 \mathscr S^{I}_{\beta,N}(w,Z)
     =N[Y^N]\left[
        \left(\sum_{i\in I_N}a_{i,N}(w)f_i(Y)\right)
                     d_N(Y)C_{\beta,N}(Y,Z)\right].
 \tag{6}
\]
Since the incoming Laurent band of \(C_{\beta,N}\) is \([-D,0]\),
the exact division identity gives
\[
 \mathscr S^{I}_{\beta,N}
   =N\sum_{i\in I_N}\sum_{m=0}^{i-1}
       a_{i,N}(w)q_{i,m}
                  \operatorname{CT}_Y[p_m(Y)C_{\beta,N}(Y,Z)].
 \tag{7}
\]
The scalar \(N\) is the original Fourier-extraction factor.

## 2. Keep the complementary factorial in the incoming coefficient

Put \(n=D-i\). The exact reflection \(S_{D-n}=N/S_n\)
and the physical support in (2) give
\[
 |f_i(r^b)|=\frac{S_n}{S_bS_{n-b}}\le\binom nb,
                       \qquad 0\le b\le n.
 \tag{8}
\]
For the inequality, express the sine quotient as
\[
 \prod_{\nu=1}^{b}
  \frac{\sin\{\pi(n-b+\nu)/N\}}{\sin(\pi\nu/N)}
 \le\prod_{\nu=1}^{b}\frac{n-b+\nu}{\nu}.
 \tag{9}
\]
This uses decrease of \(\sin t/t\) on \((0,\pi)\).
Hence, writing \(U_n^{\max}(w)=\max_{0\le b\le n}|U_N(w,r^b)|\),
\[
                 |a_{i,N}(w)|\le
                       \frac{S_n}{N}\,2^n U_n^{\max}(w).
 \tag{10}
\]
The factor \(S_n\) in (10) will not be bounded separately.

We also need the lower sine-binomial inequality
\[
       S_nS_j\le S_{n+j}\qquad(n,j\ge0,\quad n+j\le D).
 \tag{11}
\]
For \(n>0\), the function of a real variable \(x\),
\[
 \sum_{\nu=1}^{n}\log(2\sin(\pi(x+\nu)/N))-\log S_n,
                       \qquad 0\le x\le D-n,
 \tag{12}
\]
is concave. Its values at both endpoints are zero: at the right
endpoint the factors are the reflection of the first \(n\)
factors. It is therefore nonnegative. Evaluating at integer
\(x=j\) proves (11); for \(n=0\) the assertion is equality.
No factorial with index \(N\) occurs.

For \(m<i\), reflection in the first term of (4) gives
\[
 S_{i-m-1}=\frac{N}{S_{n+m+1}},\qquad n+m+1\le D.
 \tag{13}
\]
Since \(n\le N/16\), every factor of \(S_n\) is less than
one, so \(S_n\le1\). Combining (4), (10), (11), and (13)
therefore proves the joint estimate
\[
 \begin{split}
 |a_{i,N}q_{i,m}|
 &\le \frac{2^nU_n^{\max}}{N^2}
       \left(\frac{S_n}{S_{n+m+1}}+
                            \frac{S_n}{S_{m+1}}\right)\\
 &\le\frac{2^{n+1}U_n^{\max}}{N^2S_{m+1}} .
 \end{split}
 \tag{14}
\]
This includes \(n=0\), namely the resonant last Newton row.
The quotient estimate (4) already treats that row separately.

## 3. Bounds for the remaining complete factors

Let
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 L(t)=-2J((1-t)/2),\qquad c_{\rm b}=-2J(1/6)<13/40,
 \qquad b_0=101/125 .
 \tag{15}
\]
The complete small-angle bound in
[the transformed initial-interval theorem, equations (7)--(12)](research_mixed_transformed_real_initial_interval.md)
is
\[
 |U_N(w,e^{-2\pi ix})|
  \le C_\tau N^{B_\tau}
       e^{N\{b_0+L(x)-J(x)+\tau\}},\qquad 0\le x\le1/10.
 \tag{16}
\]
It keeps every coherent \(H_N\), holds for all real ordinary
colors, and has the stated small complex complete-color version.
The function \(L(x)-J(x)\) increases on this interval, and
\(L(\delta)\le\delta\log2\). Thus, uniformly for \(n\le n_N\),
\[
 2^n U_n^{\max}(w)\le C_\tau N^{B_\tau}
   e^{N\{b_0+2\delta\log2-J(\delta)+\tau\}} .
 \tag{17}
\]

There is a simple rational bound on the extra cost. The sine
chord \(2\sin\pi t\ge6t\) for \(0\le t\le1/6\) gives
\[
 -J(1/16)\le\frac1{16}\{1+\log(8/3)\}<\frac18.
 \tag{18}
\]
Indeed \(e>1+1+1/2+1/6+1/24=65/24>8/3\).
Also \(\log2<7/10\), so
\[
                       2\delta\log2-J(\delta)<\frac{17}{80}.
 \tag{19}
\]

On the unit circle the complete binomial bound is
\[
 \frac{|p_m(Y)|}{S_m}\le C_\tau N^{B_\tau}
                  e^{N(c_{\rm b}+\tau)},\qquad 0\le m<N.
 \tag{20}
\]
It is equation (11) of
[the complete seam source theorem](research_mixed_next_complete_source_seam_collar.md).
For \(m\le i-1\le D-1\), the sine chord gives
\[
 |1-r^{m+1}|\ge\frac4N,\qquad
 \frac{|p_m(Y)|}{S_{m+1}}
       \le\frac N4 C_\tau N^{B_\tau}e^{N(c_{\rm b}+\tau)}.
 \tag{21}
\]

For any fixed output disk \(|Z|\le T\), the same full-index
bound for the incoming factor, followed by the disk numerator
bound for the outgoing factor, gives
\[
 \sup_{\substack{|Y|=1\\|Z|\le T}}|C_{\beta,N}(Y,Z)|
 \le C_\tau N^{B_\tau}
       e^{N\{c_{\rm b}+M_\beta(\log_+T)+\tau\}},
 \tag{22}
\]
where
\[
 M_\beta(C)=\max_{0\le t\le1}
                 \{L(t)-(1+\beta)J(t)+Ct\}.
 \tag{23}
\]
These are the whole-index estimates in
[the kernel-margin theorem](research_mixed_next_low_index_kernel_margin.md);
there is no physical support truncation in (20)--(22).

Insert (14), (17), (21), and (22) into (7), using its literal
unit-circle constant-term integral. At most \(N^2\) pairs of
indices occur, and all extraction and chord factors are
polynomial in \(N\). We obtain the bound
\[
 \boxed{\quad
 |\mathscr S^{I}_{\beta,N}(w,Z)|
 \le C_\tau N^{B_\tau}
  e^{N\{b_0+2c_{\rm b}+M_\beta(\log_+T)+17/80+\tau\}},
                      \qquad |Z|\le T .
 \quad}
 \tag{24}
\]
The same upper bound applies after replacing each term of (7)
by its absolute value. It is therefore uniform over all subsets
\(I_N\) in (5).

## 4. Comparison with the actual next action

Use the stronger original action bounds in the
[next-three pair theorem](research_mixed_next_three_real_pair_action_floor.md)
and [next-four pair theorem](research_mixed_next_four_real_pair_action_floor.md).
The output disks and their kernel constants are those in the
[upper radial theorem, equation (19)](research_mixed_next_upper_radial_seam.md).
Together they give the following comparisons:
\[
 \begin{array}{c|c|c}
 \text{actual reference}&
 \text{ceiling in (24), before }\tau&
 \text{strict action floor}\\ \hline
 \text{ordinary three, }h_z\le0&
 3991/2000&419/200\\
 \text{ordinary three, }h_z\ge0&
 21789/10000&441/200\\
 \text{terminal three}&21789/10000&89/40\\
 \text{ordinary four}&12823/6000&109/50\\
 \text{terminal four}&12823/6000&56/25
 \end{array}
 \tag{25}
\]
For the first row use \(M_0(0)=c_{\rm b}<13/40\);
for the next two use \(M_0(17\pi/125)<1271/2500\);
for the last two use \(M_1(0)<7/15\).
The smallest action-minus-ceiling difference in this table is
\(261/10000>1/40\).

**Theorem.** For every subset in (5), at both level parities,
the selected contribution (6) is exponentially smaller than
the original geometric next action on every stated reference
family. On fixed sufficiently small complex complete-color
and actual-output neighborhoods,
\[
 \partial_w^j\partial_z^k
 \left[e^{-N\mathcal P_\beta^+(w,z)}
       \mathscr S^{I}_{\beta,N}(w,e^{-2\pi iz})\right]
                       =O_{j,k}(e^{-N/200})
 \tag{26}
\]
for each fixed derivative order. The constants are uniform
over the subsets \(I_N\).

Choose the total source tolerance and the parameter-neighborhood
variation within the strict margin in (25). The finite estimates
then hold on slightly larger fixed neighborhoods; Cauchy's formula
gives (26), with the displayed smaller loss absorbing polynomial
factors. The two ordinary-three height subfamilies have strict
margins at height zero, so the local neighborhoods need not
preserve the sign condition at nearby parameter values.
For real ordinary colors the same positive source estimate uses
the complete-color action as its reference; Markov's inequality
applied before the positive sums gives fixed ordinary derivatives.

The theorem estimates only the selected coefficient of the
specified Newton band. It does not delete a band of physical
nodes, change the old cardinal filter, estimate the unselected
coefficient, or establish a full next-transfer asymptotic.
The original row-restoration scalar from the attachment identity
is unchanged. The remaining middle-index contraction still needs
an estimate that preserves its original coherent coefficients.
