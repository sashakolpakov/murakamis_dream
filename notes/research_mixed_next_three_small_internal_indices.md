# Small internal indices with the full outgoing observation

Private research deduction, 8 November 2026. This note bounds a
specified part of the original physical-node sum. It keeps the
signed terminal trace intact, then estimates its attached outgoing
rows in absolute value. Every outgoing index is allowed. The result
removes the small internal indices from the remaining coupled
cancellation problem; it does not bound that whole problem.

## 1. Original summands and statement

Use the conventions of
[the paired-right identity, equations (17)--(18)](research_mixed_next_right_paired_terminal_insertion.md):
\[
\begin{gathered}
 D=N-1,\qquad q=e^{\pi i/N},\qquad r=q^{-2},\qquad
 \kappa=q^{D^2/2},\\
 P_a=(r;r)_a,\qquad
 S_a=|P_a|=\prod_{\nu=1}^a2\sin(\pi\nu/N),\qquad
 p_k(Z)=(rZ;r)_k,\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_a(t)=S_a^{-2}\prod_{h<a}(c_h-t),\\
 K_N^{\rm ord}(s,t)=\sum_{a=0}^{D}e_a(s)e_a(t),\\
 \mathcal K_{3,N}(w,c_j)
 =\phi_N^{(t)}[\mathcal R_N(t)^3
                      K_N^{\rm ord}(w,t)K_N^{\rm ord}(c_j,t)] .
\end{gathered}                                                    \tag{1}
\]
The functional \(\phi_N\) is the original full physical trace,
including its first normal at every double node. In particular
\(\mathcal K_{3,N}\) is already a signed finite sum.

For \(b\ge\lceil N/2\rceil\), put \(n=D-b\). Then
\(0\le n<\lfloor N/2\rfloor\), and the original high-index
coefficient is exactly
\[
 \ell_b(w)=\sum_{j=0}^{n}b_{nj}\mathcal R_N(c_j)^3
                                  \mathcal K_{3,N}(w,c_j),
 \qquad
 b_{nj}=(-1)^{n+j}
       \frac{2\sin((2j+1)\pi/N)S_n^2}{S_{n-j}S_{n+j+1}} .
                                                               \tag{2}
\]
The [radical contraction theorem](research_high_newton_radical_contraction.md)
proves \(|b_{nj}|\le2\). Its crossing values have modulus one.

Write the exact outgoing row as
\[
 R_{b,k}(Z)=\frac{r^{-bk}p_k(r^b)p_k(Z)}{P_k^2},
 \qquad 0\le k\le n .
                                                               \tag{3}
\]
Rows above \(n\) vanish. Thus an original expanded summand is
\[
 T_{b,j,k}(w,Z)=
 \frac{(-q)^b}{\kappa^2N}
 b_{nj}\mathcal R_N(c_j)^3\mathcal K_{3,N}(w,c_j)R_{b,k}(Z).
                                                               \tag{4}
\]
No absolute value has yet been taken inside the terminal trace.

**Theorem.** Uniformly for \(w\in[-2,2]\), \(|Z|\le8/7\), both
level parities, and every subset
\[
 \mathcal E_N\subset
 \left\{(b,j,k):
 \lceil N/2\rceil\le b\le D,\quad
 0\le j\le\min(D-b,\lfloor N/64\rfloor),\quad
 0\le k\le D-b\right\},
\]
one has
\[
 \boxed{\quad
 \sum_{(b,j,k)\in\mathcal E_N}|T_{b,j,k}(w,Z)|
 \le CN^A\exp N\left(\frac{419}{200}-\frac1{32}\right).
 \quad}                                                        \tag{5}
\]
The constants do not depend on the chosen subset. This is a bound
for the expanded original source after the coherent terminal
trace, not for the individual summands inside that trace.

## 2. A bound for every outgoing row

The exact factorial reflection in
[the outgoing budget, equation (2)](research_mixed_next_physical_three_outgoing_attachment_budget.md)
gives
\[
 |R_{b,k}(Z)|=\frac{S_n}{S_{n-k}S_k^2}|p_k(Z)|.
                                                               \tag{6}
\]
Every factor in \(S_n/S_{n-k}\) is at most two, and
\(|p_k(Z)|\le(15/7)^k\). Concavity of sine on \([0,\pi/2]\)
gives \(2\sin(\pi a/N)\ge4a/N\) for \(a\le N/2\).
Consequently, for \(1\le k\le n<N/2\),
\[
 S_k\ge(4/N)^k k!\ge(4k/(eN))^k,
 \qquad
 |R_{b,k}(Z)|\le
       \left(\frac{15e^2N^2}{56k^2}\right)^k .
                                                               \tag{7}
\]
The elementary factorial inequality follows by integrating
\(\log x\) from \(1\) to \(k\).

Set \(t=k/N\). The exponent in (7) is
\[
 f(t)=t\{2+\log(15/56)-2\log t\},\qquad f(0)=0.
\]
Since
\[
 f'(t)=\log\frac{15}{56t^2}\ge\log(15/14)>0
                     \quad(0<t\le1/2),
\]
every row is bounded at rate
\[
 f(1/2)=1+\tfrac12\log(15/14)
       <1+\frac1{28}=\frac{29}{28}.
                                                               \tag{8}
\]
Here \(\log(1+x)<x\) for \(x>0\). The row \(k=0\) equals one.
Thus for every retained physical node,
\[
 \sum_{k=0}^{n}|R_{b,k}(Z)|
                  \le N e^{29N/28}.
                                                               \tag{9}
\]
This deliberately elementary upper bound retains all outgoing
rows, including the endpoints and any zeros of \(p_k(Z)\).

## 3. The terminal trace at small internal indices

For \(j\le N/64\), physical termination gives
\[
 K_N^{\rm ord}(c_j,t)=\sum_{a=0}^j e_a(c_j)e_a(t).
\]
The exact product and decreasing \(\sin x/x\), as in
[terminal insertion, equations (7)--(10)](research_mixed_next_high_coefficients_terminal_insertion.md),
give
\[
 0\le e_a(c_j)\le\binom ja\binom{j+a}{a},
 \qquad
 \sum_{a=0}^j e_a(c_j)\le6^j.
                                                               \tag{10}
\]
For clarity, the first sine product can be reordered to pair the
indices \(j-a+1,\ldots,j\) with \(1,\ldots,a\); the second pairs
\(j+1,\ldots,j+a\) with the same denominator indices.
Every numerator index is below \(N\). Each comparison therefore
uses the decreasing function \(\sin x/x\) on \((0,\pi)\).
For the final sum use
\(\binom{j+a}{a}\le2^{j+a}\) and the binomial theorem.

On the strip \(|\Im\theta|\le\log2\), every numerator factor of
\(e_a(-2\cos\theta)\) has modulus at most \(9/2\).
Also \(S_a\ge S_j\) for \(a\le j\le N/64\), since the
intervening sine factors are at most one. It follows that
\[
 \|K_N^{\rm ord}(c_j,\cdot)\|_{\rm strip}
 :=\sup_{\substack{-\pi\le\Re\theta\le\pi\\
                         |\Im\theta|\le\log2}}
       |K_N^{\rm ord}(c_j,-2\cos\theta)|
 \le\frac{27^j}{S_j^2}.
                                                               \tag{11}
\]
For \(j\ge1\), the same sine chord as in (7) bounds the last
quantity by
\[
 \exp N h(j/N),\qquad
 h(x)=x\{\log27+2-2\log(4x)\}.
\]
This function increases for \(0<x\le1/64\).
Using the elementary logarithmic inequalities
\(\log3<11/10\) and \(\log2<7/10\), proved in the cited
terminal-insertion note and
[the small outgoing-index proof](research_mixed_next_three_small_outgoing_indices.md),
we obtain
\[
 h(1/64)=\frac{\log27+2+2\log16}{64}
       <\frac{109}{640}.
                                                               \tag{12}
\]
For \(j=0\) the inserted polynomial is one, so (12)'s bound
holds there too.

We now use the full operator estimate, rather than estimating
the physical trace term by term. The
[paired-right insertion theorem, equation (24)](research_mixed_next_right_paired_terminal_insertion.md)
states that, for every degree-at-most-\(N\) polynomial \(I\),
\[
 |\phi_N[\mathcal R_N^3K_N^{\rm ord}(w,\cdot)I]|
 \le C_\tau N^{A_\tau}
      e^{N(M_{\rm term}+\tau)}\|I\|_{\rm strip},
 \qquad M_{\rm term}<17/20 .
                                                               \tag{13}
\]
It includes all original trace contours and normal derivatives,
and is uniform for real ordinary \(w\). The polynomial in (11)
has degree at most \(j\), so all its hypotheses hold.
Combining (11)--(13) gives
\[
 |\mathcal K_{3,N}(w,c_j)|
 \le C_\tau N^{A_\tau}
       e^{N(17/20+109/640+\tau)}
       \quad (j\le\lfloor N/64\rfloor).
                                                               \tag{14}
\]
This step is where the established signed terminal estimate is
used; no assertion of positive trace weights is needed.

## 4. Attachment and the remaining indices

Multiply (14) by the whole positive outgoing estimate (9),
use \(|b_{nj}|\le2\), and sum over the at most \(N^2\) choices
of \(b,j\). The exact scalar in (4) has modulus \(1/N\).
These factors cost only a power of \(N\). The resulting rate
before \(\tau\) is
\[
 \frac{17}{20}+\frac{109}{640}+\frac{29}{28}
       =\frac{9211}{4480},\qquad
 \frac{419}{200}-\frac{9211}{4480}
       =\frac{873}{22400}>\frac1{32}.
                                                               \tag{15}
\]
For example, choose \(\tau=1/400\), which is smaller than
the reserve
\[
 \frac{873}{22400}-\frac1{32}=\frac{173}{22400}.
\]
This proves (5), including arbitrary subsets of the expanded
indices.

At the actual complete next-three references for words beginning
\(343\) of length at least five,
[the action floor](research_mixed_next_three_real_pair_action_floor.md)
is \(M_*=\Re\mathcal P_0^+(-2,z_*)>419/200\).
Thus (5) is exponentially smaller than the selected contribution
at those references. It does not determine that contribution's
coefficient in the full invariant.

After first removing the already bounded physical bands and the
small outgoing rows, (5) may be applied to the remaining triples.
This disjoint order avoids any double counting. It leaves only
\[
\begin{gathered}
 \lfloor N(1/2+\delta)\rfloor+1
       \le b<\lceil5N/6\rceil,\qquad n=N-1-b,\\
 \lfloor N/64\rfloor<j\le n,\qquad
 \lfloor N/4096\rfloor<k\le n ,
\end{gathered}                                                    \tag{16}
\]
where \(\delta\) is the fixed positive width in
[the physical continuation lemma](research_mixed_next_three_physical_half_band_from_vertical.md).
All original phases in these triples remain. The previously
estimated filter correction remains a whole separate term:
there is no claim that its internal pieces satisfy (5).

No bound for (16), lower bound for the full transfer, or extension
to arbitrary short partial fillings is proved in this note.
No mathematical numerical evaluation has been used.

