# Small outgoing indices in the complete right observation

Private research deduction, 8 November 2026. The signed inner-kernel
estimate controls a fixed small interval of outgoing summation
indices, even after the original outgoing factor is attached.
The bound is uniform over the entire upper half of the retained
physical nodes. It follows from finite products; no mathematical
numerical evaluation is used.

## 1. The original summand and the part being estimated

Keep the original notation
\[
D=N-1,\quad r=e^{-2\pi i/N},\quad q=e^{\pi i/N},\quad
\kappa=q^{D^2/2},\qquad
P_j=(r;r)_j,\quad p_j(Z)=(rZ;r)_j,\quad
S_j=|P_j|=\prod_{a=1}^j2\sin(\pi a/N).
\tag{1}
\]
The actual outgoing variable lies in
\[
Z=\rho e^{-2\pi iu},\qquad
3/10\le u\le39/100,\qquad 4/5<\rho<8/7.
\tag{2}
\]
For the upper physical node \(Y=r^b\), with
\(\lceil N/2\rceil\le b\le D\), set \(n=D-b\).
The original next conditional factor terminates exactly at \(k=n\):
\[
C_{0,N}(r^b,Z)
 =\sum_{k=0}^{n}\frac{r^{-bk}p_k(r^b)p_k(Z)}{P_k^2}.
\tag{3}
\]
There is no substitution of a positive model for this complex sum.

Let \(\ell_b(w)\) be the original coefficient of the first source,
defined by the exact identity
\[
\frac{F_{34,N}(w,r^b)}{P_b}
       =\frac{(-q)^b}{\kappa^2N}\ell_b(w).
\tag{4}
\]
The [complete Fourier kernel theorem](research_mixed_next_physical_three_kernel_fourier_bound.md)
proves
\[
|\ell_b(w)|\le CN^A
 \exp N\left(\frac{419}{200}-\frac1{125}\right),
\qquad -2\le w\le2 ,
\tag{5}
\]
uniformly over these nodes and both level parities.
This is a bound for the coherent coefficient after its internal
sum, not a bound for the absolute values of its internal summands.

Put \(K_N=\lfloor N/4096\rfloor\), and define the literal low-index
part of (3):
\[
C_{0,N}^{\mathrm{low}}(r^b,Z)
 =\sum_{k=0}^{\min(n,K_N)}
       \frac{r^{-bk}p_k(r^b)p_k(Z)}{P_k^2}.
\tag{6}
\]
For any set \(B_N\subseteq\{\lceil N/2\rceil,\ldots,D\}\), let
\[
T_N^{\mathrm{low}}(w,Z;B_N)
 =\frac1{\kappa^2N}\sum_{b\in B_N}
          (-q)^b\ell_b(w)C_{0,N}^{\mathrm{low}}(r^b,Z).
\tag{7}
\]
In particular \(B_N\) can be the unresolved middle band
\(\lceil N/2\rceil\le b<\lceil5N/6\rceil\), or any subset of it.

**Proposition.** For all sufficiently large levels of both parities,
uniformly in (2), in \(-2\le w\le2\), and in the choice of \(B_N\),
\[
|T_N^{\mathrm{low}}(w,Z;B_N)|
 \le C'N^{A'}\exp N\left(\frac{419}{200}-\frac3{1000}\right).
\tag{8}
\]
The same bound holds if the low-index interval in each individual
summand is replaced by an arbitrary subset. This assertion concerns
the original unfiltered-prefix part of the observation. The
pre-existing filter correction is retained separately.

## 2. A direct finite-product estimate

For \(0\le k\le n\), factorial reflection gives exactly
\[
\left|\frac{r^{-bk}p_k(r^b)p_k(Z)}{P_k^2}\right|
 =\frac{S_n}{S_{n-k}S_k^2}|p_k(Z)|.
\tag{9}
\]
Indeed \(p_k(r^b)=P_{b+k}/P_b\), and
\(S_jS_{D-j}=N\). Thus the two reflection factors \(N\)
cancel. This also proves the original normalization in (9)
at both parities.

Each factor in \(S_n/S_{n-k}\) is at most two, while (2) gives
\[
\frac{S_n}{S_{n-k}}\le2^k,\qquad
|p_k(Z)|\le(1+|Z|)^k\le(15/7)^k .
\tag{10}
\]
For \(k\le N/2\), concavity of sine on \([0,\pi/2]\) gives
\(2\sin(\pi a/N)\ge4a/N\), hence
\[
S_k\ge(4/N)^k k!.
\tag{11}
\]
For \(k\ge1\), monotonicity of \(\log x\) gives
\[
\log k!\ge\int_1^k\log x\,dx
       =k\log k-k+1\ge k\log k-k.
\]
Combining (9)--(11), with \(t=k/N>0\), bounds each row by
\[
\exp N\left[t\left\{2+\log(30/7)-2\log(4t)\right\}\right]
 \le \exp\{N f(t)\},\qquad
f(t)=t\{4-2\log(4t)\}.
\tag{12}
\]
Here \(\log(30/7)<2\), since
\(e^2>1+2+2=5>30/7\).

The function \(f\), extended by \(f(0)=0\), increases on
\([0,1/4096]\), because \(f'(t)=2-2\log(4t)>0\).
At the right endpoint,
\[
f(1/4096)
 =\frac{4+20\log2}{4096}
 <\frac{18}{4096}<\frac1{200}.
\tag{13}
\]
For an explicit elementary witness to \(\log2<7/10\), use
\[
e^{7/10}>1+\frac7{10}+\frac{49}{200}+\frac{343}{6000}
       =\frac{12013}{6000}>2.
\]
The final rational comparison in (13) is \(3600<4096\).
The zero row of (6) equals one and obeys the same estimate.
There are at most \(N\) rows, so
\[
\sum_{k=0}^{\min(n,K_N)}
\left|\frac{r^{-bk}p_k(r^b)p_k(Z)}{P_k^2}\right|
       \le N e^{N/200}.
\tag{14}
\]
No asymptotic approximation, nonzero-symbol assumption, or
outgoing-angle restriction was needed for this bound. In particular
it is uniform at the exact integer cut and all numerator zeros.

## 3. Attachment and what remains

Insert (14) and the signed coefficient bound (5) into (7).
The factors \((-q)^b\) and \(\kappa\) have modulus one.
The number of retained \(b\)-indices is at most \(N\), and the
normalizing factor remains exactly \(1/N\). All resulting costs
outside the exponent are polynomial. Since
\[
\frac1{125}-\frac1{200}=\frac3{1000},
\]
this proves (8). Every restriction to a subset in the proposition
is legitimate because (14) is a positive upper bound.

For the unfiltered physical observation, (6) is an exact partition
of the existing outgoing rows. Once (8) is removed, its middle
part involves only
\[
\lceil N/2\rceil\le b<\lceil5N/6\rceil,\qquad
\lfloor N/4096\rfloor<k\le D-b .
\tag{15}
\]
These remaining rows must still be estimated with the original
phases and coefficient \(\ell_b\). The small-index proof does not
bound their sum, or assert that cancellation in one remaining
index is sufficient.

The old filter correction and the vertical and horizontal
boundary terms of
[the exact paired-right identity](research_mixed_next_right_paired_terminal_insertion.md)
are unchanged. A bound for that complete correction is not
split into bounds for its outgoing rows. Equation (8) therefore
supplies one complete attached sub-sum, not a whole-transfer
estimate or a lower bound for the Kashaev invariant.
