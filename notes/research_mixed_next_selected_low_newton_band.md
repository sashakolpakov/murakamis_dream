# A complete selected-coefficient bound for the first Newton band

Research deduction, 8 November 2026. The exact wrapped quotient
bounds the contribution of every actual prefix Newton row
\(i\le\lfloor N/25\rfloor\) to the complete selected next
coefficient. Both next letters, both parities, and all actual
ordinary and terminal output families are covered. The first
cap coefficient remains coherent, and the outgoing conditional
kernel retains every row.

This is a deletion of a specified Newton band in the selected
coefficient. It is not a physical-node deletion, a pointwise bound
for the same partial prefix, or a bound for the other Fourier
coefficient. No numerical evaluation or frozen-source edit is used.

## 1. The actual finite source

Put \(D=N-1\), \(r=e^{-2\pi i/N}\),
\(P_j=(r;r)_j\), \(S_j=|P_j|\), and
\(p_j(Y)=(rY;r)_j\), \(f_j(Y)=p_j(Y)/P_j\).
Retain the original functions
\[
\begin{split}
 U_N(w,X)&=\sum_{\ell=0}^{D}H_N(w,r^{-\ell})f_\ell(X),\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{D}
       Y^{-j}f_j(Y)f_j(Z)/P_j^\beta,\qquad\beta=0,1,\\
 F_N(w,Y)&=F_{34,N}(w,Y)
       =N\operatorname{CT}_X[U_N(w,X)C_{1,N}(X,Y)].
\end{split}
\tag{1}
\]
The actual Newton expansion, with its original normalization, is
\[
 T_{i,N}(w)=\operatorname{CT}_X[X^{-i}p_i(X)U_N(w,X)],
 \qquad a_{i,N}(w)=\frac{N T_{i,N}(w)}{P_i^2},
 \qquad F_N(w,Y)=\sum_{i=0}^{D}a_{i,N}(w)f_i(Y).
\tag{2}
\]
These are the coefficients in
[the wrapped-quotient theorem, Section 1](research_mixed_next_selected_wrap_quotient.md).
They are not the high physical-node coefficients of a lowered word.

Set
\[
 \delta=\frac1{25},\qquad n_N=\lfloor\delta N\rfloor,
 \qquad F_N^{\mathrm{lo}}(w,Y)=
                 \sum_{i=0}^{n_N}a_{i,N}(w)f_i(Y).
\tag{3}
\]
The complete selected observation of this polynomial is
\[
 \mathcal S_{1,\beta}[F_N^{\mathrm{lo}}](w,Z)
       =N[Y^N]\{F_N^{\mathrm{lo}}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)\}.
\tag{4}
\]
In particular (4) retains the entire forced polynomial \(d_N\).

## 2. The coherent incoming bound and the exact quotient

Write
\[
 J(t)=\int_0^t\log(2\sin\pi s)\,ds,
 \qquad \rho(t)=(1+t)\log(1+t)-t\log t,
 \qquad b_1=\frac{433}{500}.
\tag{5}
\]
The complete cap coefficient bound in
[the binomial end theorem, equation (6)](research_mixed_three_four_next_binomial_end_bound.md)
gives, for every \(\tau>0\),
\[
 |T_{i,N}(w)|\le C_\tau N^{B_\tau}
              e^{N(b_1+\tau)}\binom{N+i}{i}
       \le C_\tau N^{B_\tau}e^{N\{b_1+\rho(i/N)+\tau\}}.
\tag{6}
\]
This holds for every real ordinary color \(w\in[-2,2]\), and
on a sufficiently small fixed complex disk about \(-2\).
To recall why the cap stays coherent, expand only the outer
numerators in (2). Their unit-modulus roots give
\[
 |[X^i](p_i(X)p_\ell(X))|\le\binom{i+\ell}{i}
                                      \le\binom{N+i}{i}.
\]
The original sum \(\sum_\ell |H_N(w,r^{-\ell})|/S_\ell\)
has rate \(b_1\). No expansion of any \(H_N\) is used.

The uniform sine-factorial estimate is
\(\log S_i=NJ(i/N)+O(\log N)\), including both endpoints.
Since \(\rho\) increases and \(J\) decreases on
\([0,\delta]\), equations (2) and (6) imply
\[
 \max_{i\le n_N}|a_{i,N}(w)|
   \le C_\tau N^{B_\tau}
       e^{N\{b_1+\rho(\delta)-2J(\delta)+\tau\}}.
\tag{7}
\]

For the exact Euclidean quotient
\[
 f_i(Y)d_N(Y)=(Y^N-1)Q_i(Y)+R_i(Y),\qquad\deg R_i<N,
\tag{8}
\]
the wrapped-quotient theorem proves \(Q_0=0\) and
\[
 Q_i(Y)=\sum_{m=0}^{i-1}q_{i,m}p_m(Y),\qquad
 |q_{i,m}|\le\frac{S_{i-m-1}}{N^2}
                       +\frac1{N S_{m+1}}.
\tag{9}
\]
This bound already includes the terminating binomial cancellation,
the resonant last row, and both level parities. It never divides
by \(P_N\).

Here \(m+1\le i\le n_N\). All factors in
\(S_{i-m-1}\) are at most one because \(\delta<1/6\).
The uniform factorial bound also gives
\(S_{m+1}^{-1}\le CN^B e^{-NJ(\delta)}\).
On \(|Y|=1\), the literal numerator satisfies
\(|p_m(Y)|\le2^m\le e^{N\delta\log2}\).
Thus the full finite quotient in (8) obeys
\[
 \max_{1\le i\le n_N}\sup_{|Y|=1}|Q_i(Y)|
       \le CN^B e^{N\{-J(\delta)+\delta\log2\}}.
\tag{10}
\]
For levels with \(n_N=0\), (4) is identically zero. No
asymptotic index is required to cover these levels.

## 3. Keep every outgoing observation

Put \(c_{\rm b}=-2J(1/6)<13/40\),
\(L(t)=-2J((1-t)/2)\), and
\[
 M_\beta(C)=\max_{0\le t\le1}
                 \{L(t)-(1+\beta)J(t)+Ct\}.
\tag{11}
\]
The full unit-circle binomial estimate and complete output-disk
bound, as recorded in
[the seam theorem, equations (11)--(16)](research_mixed_next_complete_source_seam_collar.md),
give
\[
 \sup_{|Y|=1,\ |Z|\le T}|C_{\beta,N}(Y,Z)|
  \le C_\tau N^{B_\tau}
            e^{N\{c_{\rm b}+M_\beta(\log_+T)+\tau\}}.
\tag{12}
\]
Indeed \(|f_j(Y)|\le C_\tau N^{B_\tau}e^{N(c_{\rm b}+\tau)}\),
and the remaining sum is exactly
\(\sum_j|p_j(Z)|/S_j^{1+\beta}\). The incoming chirp has
unit modulus. There is no physical termination assumption in (12).

The incoming Laurent band of \(C_\beta\) is \([-D,0]\).
Consequently the exact quotient identity gives
\[
 \mathcal S_{1,\beta}[F_N^{\mathrm{lo}}]
       =N\sum_{i=1}^{n_N}a_{i,N}(w)
                         \operatorname{CT}_Y[Q_i(Y)C_{\beta,N}(Y,Z)].
\tag{13}
\]
The outside \(N\) is the original selected extraction factor.
Equations (7), (10), and (12), with the finite sum in (13), prove
\[
 \boxed{\quad
 |\mathcal S_{1,\beta}[F_N^{\mathrm{lo}}](w,Z)|
 \le C_\tau N^{B_\tau}
 e^{N\{b_1+\rho(\delta)-3J(\delta)+\delta\log2
                   +c_{\rm b}+M_\beta(\log_+T)+\tau\}} .
 \quad}
\tag{14}
\]
Every outgoing constant-term observation in (13) is included.
This estimate requires no positivity of \(a_{i,N}\), \(Q_i\),
or the original source.

## 4. Written rational comparisons at \(\delta=1/25\)

Use \(\log2<7/10\), \(\log2>2/3\), and
\(\log3>13/12\), proved by the elementary series witnesses in
[the next-four pair theorem](research_mixed_next_four_real_pair_action_floor.md).
Also \(\log25<13/4\). For an explicit witness for the latter,
the first six positive exponential terms give
\[
 e^{13/8}>\sum_{k=0}^{5}\frac{(13/8)^k}{k!}
      =\frac{19839493}{3932160}>5;
 \qquad 19839493-5\cdot3932160=178693>0.
\tag{15}
\]
Squaring proves the logarithmic bound.

The inequality \((1+t)\log(1+t)\le t+t^2/2\) follows by
differentiation. The sine chord \(2\sin\pi t\ge6t\) on
\([0,1/6]\) gives \(-J(\delta)\le\delta\{1-\log(6\delta)\}\).
Since \(\log6>7/4\), we obtain
\[
 \rho(\delta)<\frac{17}{100}+\frac1{1250},\qquad
 -3J(\delta)<\frac3{10},\qquad
 \delta\log2<\frac7{250}.
\tag{16}
\]
In particular
\[
              \rho(\delta)-3J(\delta)+\delta\log2
                                  <\frac{1247}{2500}.
\tag{17}
\]

At the actual output references, the complete disk bounds are
\(M_1(0)<7/15\), \(M_0(0)=c_{\rm b}<13/40\), and
\(M_0(17\pi/125)<1271/2500\), as in
[the upper radial theorem, equation (19)](research_mixed_next_upper_radial_seam.md).
The stronger original action floors are those of the
[next-three](research_mixed_next_three_real_pair_action_floor.md)
and [next-four](research_mixed_next_four_real_pair_action_floor.md)
pair theorems. Substituting (17) in (14) gives:
\[
\begin{array}{c|c|c|c}
 \text{actual reference}&\text{source ceiling}&
       \Re\mathcal P_\beta^+(-2,z_*)\text{ floor}&
       \text{floor minus ceiling}\\ \hline
 \text{ordinary three},\ h_z\le0&5037/2500&419/200&401/5000\\
 \text{ordinary three},\ h_z\ge0&10991/5000&441/200&17/2500\\
 \text{terminal three}&10991/5000&89/40&67/2500\\
 \text{ordinary four}&32347/15000&109/50&353/15000\\
 \text{terminal four}&32347/15000&56/25&1253/15000
\end{array}
\tag{18}
\]
The source ceilings are strict before the arbitrary tolerance.
The smallest displayed reserve is \(17/2500\). The sign
conditions refer only to the actual ordinary-three reference;
both closed sign subfamilies have a strict reserve at height zero.

**Theorem.** On every actual ordinary or terminal next-three or
next-four family, the selected observation (4) is exponentially
smaller than the unchanged next action. It holds for both parities
and all real ordinary colors, normalized against the complete-color
action. On fixed sufficiently small complex complete-color and
actual-output neighborhoods, every fixed normalized mixed derivative
satisfies
\[
 \partial^\alpha\left[
 e^{-N\mathcal P_\beta^+(w,z)}
 \mathcal S_{1,\beta}[F_N^{\mathrm{lo}}](w,e^{-2\pi iz})\right]
                         =O_\alpha(e^{-N/1000}).
\tag{19}
\]

Choose the total source tolerance and the fixed neighborhood
variation inside the reserve in (18). The original complex-color
coefficient bounds and small enlargements of the output disks
then prove a value bound with a margin larger than \(1/1000\).
Cauchy's formula proves (19) on smaller neighborhoods. For all
real ordinary colors, Markov's inequality gives each fixed ordinary
derivative with polynomial cost. The retained index set in (3)
does not depend on any differentiated parameter.

The exact selected coefficient therefore reduces to the Newton
range \(i>\lfloor N/25\rfloor\), with the error (19). The next
physical row still has its separate original scalar
\(\kappa_N^{4+\beta}N^{1+\beta}P_b^{1-\beta}\); none is
introduced or removed by (13). This deletion does not alter the
old cardinal filter, prove a pointwise partial-prefix estimate,
or suppress the unselected coefficient. The coherent remaining
Newton contraction, and hence complete selected-sector suppression,
remain open.
