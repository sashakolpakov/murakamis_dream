# An exact Newton quotient for the complete selected next coefficient

Research deduction, 8 November 2026. The high monomial part of the
next transfer can be expressed in the original Newton basis with an
explicit finite coefficient bound. A terminating binomial identity
and summation by parts remove the three independent factorial
denominators that occur in its direct expansion. The actual prefix
coefficients remain coherent.

This is a finite source identity and upper bound, not suppression of
the selected sector. Its remaining contraction is displayed in
Section 5. No numerical evaluation or change to a frozen source is
used.

## 1. The actual prefix coefficients and the quotient

Put
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad S_j=|P_j|,\quad
 p_j(Y)=(rY;r)_j,\quad f_j(Y)=p_j(Y)/P_j .
 \tag{1}
\]
All factorial denominators below have indices less than \(N\).
For products \(p_j\) only, indices above \(D\) are allowed.
Keep the literal original source
\[
\begin{split}
 U_N(w,X)&=\sum_{\ell=0}^D H_N(w,r^{-\ell})f_\ell(X),\\
 C_{\beta,N}(X,Z)&=\sum_{j=0}^D
      X^{-j}f_j(X)f_j(Z)/P_j^\beta,\qquad \beta=0,1,\\
 F_N(w,Y)&=F_{34,N}(w,Y)
            =N\operatorname{CT}_X[U_N(w,X)C_{1,N}(X,Y)].
\end{split}
\tag{2}
\]
These are exactly the sources of
[the next attachment](research_mixed_three_four_next_conditional_attachment.md).
Define their actual Newton coefficients by
\[
\begin{split}
 T_{i,N}(w)&=\operatorname{CT}_X[X^{-i}p_i(X)U_N(w,X)],\\
 a_{i,N}(w)&=\frac{N T_{i,N}(w)}{P_i^2},\qquad
                    F_N(w,Y)=\sum_{i=0}^D a_{i,N}(w)f_i(Y).
\end{split}
\tag{3}
\]
In particular these coefficients are not the physical-node
coefficients of the lowered \(33\) word.

On the unit circle the exact reciprocal identity is
\[
          \overline{f_i(X)}=X^{-i}f_i(X).
 \tag{4}
\]
It follows by conjugating each factor and its denominator in (1).
The Laurent band of \(X^{-i}p_i(X)U_N(w,X)\) is contained in
\([-i,D]\subset(-N,N)\). Exact root averaging therefore gives
\[
 \boxed{\quad
 a_{i,N}(w)=\frac1{P_i}
       \sum_{b=0}^{D-i}U_N(w,r^b)\overline{f_i(r^b)} .
 \quad}
 \tag{5}
\]
The upper limit is the literal zero \(p_i(r^b)=0\) for \(i+b\ge N\).
Every retained cap value in (5) is complete. There is no
positivity assumption on it or on \(a_{i,N}\).

The original Fourier polynomial has the entire identity
\[
             d_N(Y)=\frac1N\sum_{\ell=0}^D f_\ell(Y),
 \tag{6}
\]
proved in [the first-node theorem, Lemma 1](research_mixed_next_three_first_physical_node.md).
In particular its forcing is retained. For \(0\le i<N\), let
\[
 f_i(Y)d_N(Y)=(Y^N-1)Q_i(Y)+R_i(Y),\qquad \deg R_i<N
 \tag{7}
\]
be ordinary polynomial division. Then \(Q_0=0\), and
\(\deg Q_i\le i-1\) for \(i\ge1\).

## 2. Finite Newton multiplication and its wrapped part

The finite product identity needed here is
\[
 \boxed{\quad
 p_i(Y)p_\ell(Y)=r^{-i\ell}
 \sum_{k=0}^{\min(i,\ell)}
 \frac{(-1)^k r^{k(k-1)/2}P_iP_\ell}
      {P_kP_{i-k}P_{\ell-k}}p_{i+\ell-k}(Y).
 \quad}
 \tag{8}
\]
It holds for every \(0\le i,\ell<N\), including when a product
index on the right reaches or exceeds \(N\).

For a direct proof, the assertion at \(\ell=0\) is immediate.
Multiplication by \(1-r^{\ell+1}Y\) uses
\[
 p_s(Y)(1-r^{\ell+1}Y)
     =r^{\ell-s}p_{s+1}(Y)+(1-r^{\ell-s})p_s(Y).
 \tag{9}
\]
If \(c_{i,\ell,k}\) denotes the coefficient in (8), extended by
zero outside its range, the required recurrence is
\[
 c_{i,\ell+1,k}
   =r^{k-i}c_{i,\ell,k}
        +(1-r^{k-1-i})c_{i,\ell,k-1}.
 \tag{10}
\]
For interior indices, divide by the proposed left coefficient.
The two ratios are respectively
\[
 \frac{r^k(1-r^{\ell+1-k})}{1-r^{\ell+1}},
 \qquad
 \frac{1-r^k}{1-r^{\ell+1}},
\]
whose sum is one. The endpoint cases follow from the same
recurrence; the potential \(k=i+1\) term has factor
\(1-r^0=0\). This induction never divides by \(P_N\).

At the present root of unity,
\[
           p_{N+m}(Y)=(1-Y^N)p_m(Y)\qquad(0\le m<N).
 \tag{11}
\]
Consequently the quotient of \(f_i f_\ell\) by \(Y^N-1\) is zero
if \(i+\ell<N\), and otherwise equals
\[
 -r^{-i\ell}\sum_{k=0}^{i+\ell-N}
 \frac{(-1)^k r^{k(k-1)/2}p_{i+\ell-N-k}(Y)}
      {P_kP_{i-k}P_{\ell-k}} .
 \tag{12}
\]
The terms of (8) with product index below \(N\) have no quotient.
Every term of (12) has degree below \(N\), so there is no further
division.

Insert (12) in (6)--(7), and put \(m=i+\ell-N-k\).
For \(0\le m<i\), the remaining range is
\(0\le k\le i-m-1\), with \(\ell=N+m+k-i\). Thus
\[
 Q_i(Y)=\sum_{m=0}^{i-1}q_{i,m}p_m(Y),
 \tag{13}
\]
where the exact coefficient is
\[
 \boxed{\quad
 q_{i,m}
  =-\frac{r^{i(i-m)}}{N P_iP_{N+m-i}}
           \sum_{k=0}^{i-m-1}\frac{(r^{-i};r)_k}{P_k}.
 \quad}
 \tag{14}
\]
Here the elementary identity
\[
 (r^{-i};r)_k
     =(-1)^kr^{-ik+k(k-1)/2}\frac{P_i}{P_{i-k}}
\]
accounts for every phase. For example, (14) gives
\(Q_1=-r/(N^2P_1)\), agreeing with the leading coefficient of
\(f_1d_N\). This is an algebraic normalization check, not a
finite-level evaluation used to justify the identity.

## 3. A uniform bound for the truncated binomial sum

For \(1\le i<N\), write
\[
 z_i=-e^{\pi i(i+1)/N},\qquad
 A_{i,k}=\frac{S_i}{S_kS_{i-k}}>0\quad(0\le k\le i).
 \tag{15}
\]
Conjugation of the factors shows exactly that
\[
           \frac{(r^{-i};r)_k}{P_k}=z_i^k A_{i,k}.
 \tag{16}
\]
One can also check the phase from the consecutive ratio
\[
 \frac{1-r^{k-i}}{1-r^{k+1}}
   =z_i\,\frac{\sin\{\pi(i-k)/N\}}{\sin\{\pi(k+1)/N\}}.
\]
The magnitudes \(A_{i,k}\) are symmetric under \(k\mapsto i-k\)
and are nondecreasing up to the middle and nonincreasing
afterward. For \(i\le N-2\), this follows from the strict
decrease of
\(\sin\{\pi(i-k)/N\}/\sin\{\pi(k+1)/N\}\) as a real function
of \(k\); its derivative has the sign of
\(-\sin\{\pi(i+1)/N\}<0\).

For a nonnegative monotone sequence with maximum \(A\),
summation by parts gives
\[
       \left|\sum_{k=u}^v z^k A_k\right|
                   \le\frac{2A}{|1-z|},\qquad |z|=1,\ z\ne1.
 \tag{17}
\]
Indeed multiply by \(1-z\); the two endpoint terms and the
total variation have sum at most \(2A\).

The complete finite binomial theorem also gives
\[
 \sum_{k=0}^{i}\frac{(r^{-i};r)_k}{P_k}
                  =(r^{-i};r)_i,\qquad
                       |(r^{-i};r)_i|=S_i.
 \tag{18}
\]
For \(i\le N-2\),
\[
 |1-z_i|
  =2\sin\frac{\pi(N-i-1)}{2N}\ge\frac2N .
 \tag{19}
\]
If \(n\) is on the increasing side, apply (17) to \(0\le k\le n\).
If it is on the decreasing side, subtract the tail \(n<k\le i\)
from (18) and apply (17) to that tail. Symmetry covers the
two equal central values when \(i\) is odd. In either case,
\[
 \left|\sum_{k=0}^{n}\frac{(r^{-i};r)_k}{P_k}\right|
                  \le S_i+N\,\frac{S_i}{S_nS_{i-n}},
               \qquad 0\le n\le i .
 \tag{20}
\]

The index \(i=D\) must be treated separately: \(z_D=1\),
so (19) does not apply. In this case
\((r^{-D};r)_k/P_k=1\), the partial sum is \(n+1\le N=S_D\),
and (20) still holds. This includes \(N=2\). No endpoint is
removed by a nonresonance assertion.

## 4. Reflection cancels the interior factorials

Let \(n=i-m-1\). The exact complementary factorial identity is
\[
 P_{D-n}=\frac{N}{\nu_nP_n},
       \qquad \nu_n=(-1)^n r^{-n(n+1)/2},\quad |\nu_n|=1.
 \tag{21}
\]
It is the original identity in
[the lowered-word observation, equation (14)](research_mixed_next_lowered_word_dual_observation.md).
Here \(N+m-i=D-n\), so (14) becomes
\[
 q_{i,m}
   =-\frac{\nu_n r^{i(i-m)}P_n}{N^2P_i}
           \sum_{k=0}^{n}\frac{(r^{-i};r)_k}{P_k}.
 \tag{22}
\]
Equations (20)--(22) prove the finite bound
\[
 \boxed{\qquad
 |q_{i,m}|
       \le\frac{S_{i-m-1}}{N^2}
                    +\frac1{N S_{m+1}},
       \qquad 1\le i<N,\quad0\le m<i .
 \qquad}
 \tag{23}
\]
For \(i=D\), the direct endpoint calculation gives the stronger
first term alone. Every denominator in (23) is nonzero.
The bound is uniform at both parities and at every level.

For comparison, bounding each summand of (12) independently
would retain three factorial denominators. Equation (23)
uses the constant phase and the complete finite sum before
taking absolute values. It does not assert positivity of the
original quotient or its Newton coefficients.

## 5. The actual selected contraction remains specified

For any polynomial \(F\) of degree at most \(D\), polynomial
division gives
\[
 Fd_N=(Y^N-1)Q_F+R_F,\qquad \deg R_F<N.
\]
Since \(C_{\beta,N}\) has incoming band \([-D,0]\),
both \(R_FC_{\beta,N}\) and \(Q_FC_{\beta,N}\) have highest
degree less than \(N\). Therefore the exact selected functional is
\[
 N[Y^N](Fd_NC_{\beta,N})
                       =N\operatorname{CT}_Y[Q_FC_{\beta,N}].
 \tag{24}
\]
This is the quotient mechanism already present in
[cardinal sector separation](research_mixed_next_cardinal_sector_separation.md);
the new formulas above specify it in the actual Newton expansion.
For (3),
\[
 \boxed{\quad
 N[Y^N](F_Nd_NC_{\beta,N})
   =N\sum_{i=1}^D a_{i,N}(w)
        \sum_{m=0}^{i-1}q_{i,m}\,
               \operatorname{CT}_Y[p_m(Y)C_{\beta,N}(Y,Z)] .
 \quad}
 \tag{25}
\]
The outer \(N\) in (25) is the original extraction factor.
The next ordinary row retains the separate scalar
\(\kappa_N^{4+\beta}N^{1+\beta}P_b^{1-\beta}\) at a physical
output, exactly as in the next-attachment theorem.

There is a complementary exact form of the wrap restriction.
By (4), each product \(f_if_\ell f_k\) is self-reciprocal
with degree \(i+\ell+k\). Hence (3) and (6) imply
\[
\begin{split}
 N[Y^N](F_Nd_NC_{\beta,N})
   =\sum_{\substack{0\le i,\ell,k<N\\i+\ell\ge N}}
    a_{i,N}(w)\frac{f_k(Z)}{P_k^\beta}\,
       \overline{[Y^{\,i+\ell-N}](f_i f_\ell f_k)}.
\end{split}
\tag{26}
\]
The conjugation in (26) concerns only the constant finite basis
coefficients, not \(w\), \(Z\), or \(a_{i,N}(w)\).
This is a restriction on two Newton indices. It is not a
deletion of physical input nodes or an identification of Newton
degree with the selected monomial degree.

Equations (5), (23), and (25) retain an actual complete-source
contraction to estimate. They do not yet bound it below the
ordinary or terminal next action: the correlated coherent
coefficients \(a_{i,N}\) and the full outgoing constant-term
observations in (25) remain. Taking their independent positive
majorants is an additional step requiring its own action
comparison. Neither a single seam value of the prefix nor a
bound for high physical Newton nodes supplies that comparison.

All formulas are polynomial identities in the original ordinary
color and outgoing variable, with all original normal data and
both parities retained. Fixed derivatives in those variables
commute with every finite operation. No full selected-sector
suppression, complete next-source asymptotic, or knot-family
conclusion is inferred here.
