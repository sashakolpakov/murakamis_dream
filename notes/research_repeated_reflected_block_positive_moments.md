# Positive moments of repeated original reflected crossing blocks

Research deduction, 8 November 2026. No numerical evaluation is used.

A particular mixed positive crossing list has a positive operator in
the original coefficient space. Its actual capped scalar is a positive
spectral moment, so it cannot vanish at any level. The operator is the
Gram matrix of a complete crossing power, rather than the one-crossing
Gram matrix used for homogeneous threes. This supplies explicit lower
bounds from the already proved reflected source. It does not determine
the geometric rate of the longer capped words.

## 1. Exact block, source and closing scalar

Use the full original Newton algebra at an integer level \(N\ge2\),
with crossing matrix \(M=M_N\), reversal \(J=J_N\), coordinate vectors
\(\mathbf e_j\), \(D=N-1\), and
\[
 q=e^{\pi i/N},\qquad \kappa=q^{D^2/2},\qquad
 A_n=JM^n,\qquad \phi(v)=\mathbf e_D^T v.
 \tag{1}
\]
All adjoints below use the original Euclidean Hermitian norm. The
[positive-cycle source](research_positive_three_crossing_cycle.md),
equations (1)--(6), proves the exact full-matrix identities
\[
 M^{-1}=\overline M,\qquad M^T=JMJ,\qquad
 MJM=\kappa JM^{-1}J,
 \qquad MA_nM^{-1}=\kappa M^*M^{n-2}.
 \tag{2}
\]
In particular these identities retain the first normal at every
repeated physical root. They are not distinct-node identities.

Fix integers \(r,m\ge1\), independently of \(N\), and set
\[
 W_r=A_2^{r-1}A_{r+2},\qquad
 K_r=(M^r)^*M^r>0,\qquad
 Z_{r,m,N}=\phi\!\left[JW_r^mM^{-1}\mathbf e_0\right].
 \tag{3}
\]
Despite its convenient last factor, the word in (3) has only positive
crossing powers after multiplication. Its ordered crossing list is
\[
 \underbrace{(2,\ldots,2,r+2),\ldots,(2,\ldots,2,r+2)}_{m
 \text{ blocks}},
 \quad\text{with the last }r+2\text{ replaced by }r+1.
 \tag{4}
\]
Each block contains \(r-1\) twos. Successive entries in (4) are
separated by the literal original turn \(J\), with the original
input \(\mathbf e_0\) and closing row \(\phi\). For instance
\(Z_{2,2,N}=\phi(M^2JM^4JM^2JM^3\mathbf e_0)\).

**Theorem 1.** At every integer level,
\[
 MW_rM^{-1}=\kappa^rK_r,
 \qquad
 \boxed{\quad Z_{r,m,N}=\kappa^{rm-1}\mu_{r,m,N},\qquad
 \mu_{r,m,N}:=\mathbf e_0^*K_r^m\mathbf e_0>0 .\quad}
 \tag{5}
\]

*Proof.* By (2), the transformed twos are \(\kappa M^*\),
and the transformed last factor is \(\kappa M^*M^r\). Hence
their product is exactly \(\kappa^r(M^*)^rM^r\). Taking its
\(m\)-th power in (3) gives
\[
 Z_{r,m,N}=\kappa^{rm}\mathbf e_0^T M^{-1}K_r^m\mathbf e_0.
\]
The first row of \(M^{-1}\) is
\(\kappa^{-1}\mathbf e_0^T\), proving (5). Strict positivity
uses invertibility of the full \(M\). No phase or component of the
source has been replaced before the pairing. \(\square\)

The [all-run two-block identity](research_mixed_two_adjacent_merged_source.md),
equation (14h), also gives
\[
 W_r=\kappa^rM^{-1}JM^{-r}JM^{r+1},\qquad
 K_r=JM^{-r}JM^r.
 \tag{6}
\]
Thus the same scalar is a repeated reflected word:
\[
 Z_{r,m,N}=\kappa^{rm-1}
 \phi\!\left[M^{-r}JM^r(JM^{-r}JM^r)^{m-1}\mathbf e_0\right].
 \tag{7}
\]
For \(m=1\) this is exactly the previously studied reflected source.
For \(r=1\), (5) is the homogeneous-three moment theorem. For
\(r,m>1\), (5) concerns a repeated mixed block, not either of those
special cases. The earlier positive-cycle Section 6 instead varies
the caps around powers of \(M^*M\); here the cap stays \(\mathbf e_0\)
and the positive operator is \((M^r)^*M^r\).

## 2. Finite bounds with the actual cap retained

Write \(L_{r,N}=\|M^r\|_2^2\) and
\(\mu_{r,0,N}=1\). The positive spectral measure of \(K_r\) at
the actual \(\mathbf e_0\) gives, exactly,
\[
 \mu_{r,1,N}=\|M^r\mathbf e_0\|_2^2,
 \qquad
 \mu_{r,j,N}^2\le\mu_{r,j-1,N}\mu_{r,j+1,N}\quad(j\ge1),
 \tag{8}
\]
and for every \(m\ge1\),
\[
 \boxed{\quad
 \|M^r\mathbf e_0\|_2^{2m}
 \le |Z_{r,m,N}|
 \le L_{r,N}^{m-1}\|M^r\mathbf e_0\|_2^2.
 \quad}
 \tag{9}
\]
Indeed diagonalize \(K_r\) with positive eigenvalues \(\lambda_j\)
and weights \(w_j=|\langle u_j,\mathbf e_0\rangle|^2\), whose sum
is one. Cauchy--Schwarz gives (8), and Jensen's inequality for
\(\lambda^m\) gives the lower bound in (9). The upper bound is
\(\lambda^m\le L_{r,N}^{m-1}\lambda\). These finite inequalities
are valid even when the cap has exponentially small overlap with
the top eigenspace. No top-mode approximation is being used.

For specified actual caps \(f,g\), the same positive form obeys
\[
 |f^*K_r^m g|^2\le(f^*K_r^m f)(g^*K_r^m g).
 \tag{10}
\]
Equation (10) supplies no lower bound when the caps differ. The
noncancellation statement (5) uses the exact matching cap, not a
freely selected observation at an interior color.

## 3. A geometric lower rate for the even-power input

Let \(r=2k\), \(k\ge2\), and let
\(\mathcal K_k=C(R^{-2k}T(R^{2k}))\) be the original reflected
knot of the
[reflected volume theorem](research_reflected_even_kashaev_volume_theorem.md).
Put
\[
 \chi_k=\frac{\operatorname{Vol}(S^3\setminus\mathcal K_k)}{4\pi}.
 \tag{11}
\]
That theorem, with the literal reduced closing normalization, proves
\(\|M^{2k}\mathbf e_0\|_2^2=e^{2N\chi_k+o(N)}\). Also let
\[
 J_0(x)=\int_0^x\log(2\sin\pi t)\,dt,
 \qquad c=2J_0(5/6)>0.
 \tag{12}
\]
The [one-crossing operator theorem](research_one_crossing_gaussian_window.md),
Theorem 2, gives \(\log\|M\|_2=Nc+o(N)\). Consequently (9) gives
\[
 2m\chi_k
 \le \liminf_N N^{-1}\log|Z_{2k,m,N}|
 \le \limsup_N N^{-1}\log|Z_{2k,m,N}|
 \le 2\chi_k+4k(m-1)c.
 \tag{13}
\]
The lower bound transports an independently proved original source
rate through any fixed number of these positive blocks. It is not
asserted equal to the volume rate of the longer word.

For \(r=2\), the exact column
\(|(M^2\mathbf e_0)_j|=\prod_{\nu=1}^j2\sin(\pi\nu/N)\),
and its established Laplace estimate, give the first-moment rate
\(c\). Section 4 improves the operator upper rate in this case to
\(b_2=-4J_0(1/4)\), so
\[
 mc\le\liminf_N N^{-1}\log|Z_{2,m,N}|
 \le\limsup_N N^{-1}\log|Z_{2,m,N}|
 \le c+2(m-1)b_2.
 \tag{14}
\]
All these assertions use the full sequence of integer levels and
both parities. Conjugating the complete word gives the mirror
statements with the same moduli.

## 4. Cyclic moments and a sharp two-crossing operator rate

The original complete cardinal contraction in the positive-cycle
note, equations (3), (8)--(9), identifies the cycle of \(rm\) degree-two
vertices with the ordered list consisting of \(m\) copies of
\((2,\ldots,2,r+2)\). Its integral has one factor \(+N\) for each
internal circle, and is exactly
\[
 \operatorname{Tr}(W_r^m)=\kappa^{rm}\operatorname{Tr}(K_r^m).
 \tag{15}
\]
The cardinal pairing is bilinear; positivity follows only after
the exact similarity (5). At each level,
\[
 L_{r,N}^m\le\kappa^{-rm}\operatorname{Tr}(W_r^m)
                        \le N L_{r,N}^m.
 \tag{16}
\]
Thus its logarithmic rate, when known, is \(2m\) times the original
operator-norm rate of \(M^r\). The polynomial factor \(N\) makes this
claim independent of a cap overlap.

For \(r=2\) that norm rate has a direct complete proof. Write
\(S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N)\). The
[exact two-crossing coefficient formula](research_degree_two_power_two_formula.md),
equation (1), gives
\[
 |(JM^2)_{ij}|=
 \frac{N S_{i+j}}{S_i^2S_j^2}\quad(i+j<N),
 \qquad (JM^2)_{ij}=0\quad(i+j\ge N).
 \tag{17}
\]
No boundary coefficient or normal is removed. The endpoint-uniform
factorial estimate shows that the logarithm in (17) is, uniformly
over its entire triangle,
\[
 N E_2(i/N,j/N)+O(\log N),\qquad
 E_2(x,y)=J_0(x+y)-2J_0(x)-2J_0(y).
 \tag{18}
\]
On the strict triangle a stationary point must satisfy
\[
 2\sin\pi(x+y)=(2\sin\pi x)^2=(2\sin\pi y)^2.
 \tag{19}
\]
Since \(x+y<1\), the equality of sines forces \(x=y\), and
(19) then gives \(x=y=1/4\). This is the unique interior
stationary point. No boundary point maximizes \(E_2\): on an open
coordinate edge its inward derivative is \(+\infty\); on
\(x+y=1\) the value is zero; the three corners also have value
zero; and \(E_2(1/4,1/4)=-4J_0(1/4)>0\). Continuity on the
closed triangle therefore proves the unique global maximum
\[
 \max E_2=b_2=-4J_0(1/4)=\frac{2G_{\mathrm{Cat}}}{\pi}.
 \tag{20}
\]
The last sine-integral identity is recorded in
[original Newton transport](research_corner_newton_source_transport.md),
Section 5: \(J_0(1/4)=-G_{\mathrm{Cat}}/(2\pi)\).
Rounding \((N/4,N/4)\) supplies a permitted matrix
entry for all sufficiently large levels. The largest entry is
bounded above by the operator norm and bounds that norm from above
after multiplication by \(N\). Equations (17)--(20), with the
unitary reversal \(J\), prove
\[
 \lim_N N^{-1}\log\|M^2\|_2=b_2,
 \qquad
 \boxed{\quad
 \lim_N N^{-1}\log|\operatorname{Tr}((A_2A_4)^m)|
                  =2mb_2=\frac{4mG_{\mathrm{Cat}}}{\pi}.
 \quad}
 \tag{21}
\]
This is an actual cyclic tensor contraction with its original
measure and scalar. The volume-scaled number is \(8mG_{\mathrm{Cat}}\).
No identification of that cycle with a specified knot, link,
fully augmented manifold or cover is made. In particular (21)
is not a volume-conjecture assertion for the capped words (4).

## 5. The capped diagrams and the limitation of the rate estimate

In the original negative continued-fraction convention used by the
positive-cycle note, Section 4, an entry \(n\) has matrix
\(T_n=\left(\begin{smallmatrix}n&-1\\1&0\end{smallmatrix}\right)\).
The block and the final one-unit decrement in (4) give exactly
\[
 B_r=T_2^{r-1}T_{r+2}
 =\begin{pmatrix}r^2+r+1&-r\\r^2&1-r\end{pmatrix},\qquad
 \binom{p_m}{q_m}=B_r^m\binom11.
 \tag{22}
\]
For the final decrement use
\(T_{r+1}=T_{r+2}\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)\).
Since \(\det B_r=1\) and \(\operatorname{Tr}B_r=r^2+2\),
\[
 p_0=1,\quad p_1=r^2+1,\quad
 p_m=(r^2+2)p_{m-1}-p_{m-2},
 \qquad q_1=r^2-r+1.
 \tag{23}
\]
The fraction is reduced because the matrix is integral unimodular.
For even \(r\), all \(p_m\) are odd. The original closure is then
a knot, also seen without a fraction convention: every crossing
power in (4) is even except the last \(r+1\); that last odd block
has the diagonal endpoint pairing, which every intervening even
block and quarter-turn preserves. Its union with the outside vertical
pairing has one component. This component statement is independent
of the quantum level and does not remove either level parity.

At \(m=1\), (22) gives \((r^2+1)/(r^2-r+1)\), consistent with
the reflected description (7). At \(r=m=2\), it gives \(29/17\).
The numerator 29 is neither an equal reflected-pair numerator
\(s^2+1\) nor one of the homogeneous-three numerators
\(F_{2j+1}\) from the positive-cycle note (the consecutive relevant
values are 13 and 34). Thus this repeated mixed list does not
reduce as a whole to either of those previously analyzed lists.
Other identifications and overlap with any existing filling theorem
are not being excluded by this observation.

The finite noncancellation (5) and lower rates (13)--(14) are the new
conclusions for these specified actual closures. A geometric
identification of the limiting capped rate would require a matching
upper rate and an original volume calculation; neither follows from
positivity or from a Casson--Rivin variational lower bound alone.
There is no claim here about arbitrary mixed lists, unequal caps,
ordinary boundary colors, a completed third short attachment, or
the general finite-exceptions goal.
