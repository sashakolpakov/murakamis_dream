# Restoring the full physical middle band after both small-index removals

Private exact source reduction, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or change to a
frozen input is used.

The remaining transfer can be expressed with the original physical
middle endpoint and with both internal indices bounded below by
fixed fractions of the level. Restoring the previously paid
physical half-band costs only an exponentially small error. This
allows the exact endpoint amplitude of the coupled physical sum
to be retained; it does not bound the remaining coupled sum.

## 1. Original source and the new remainder

Use the actual base reference of
[the complete transfer reduction, Section 1](research_mixed_next_three_complete_transfer_middle_reduction.md):
an actual complete word in powers three and four beginning \(343\),
of length \(m\ge5\), with \(w=-2\), \(Z=Z_*\), and
\[
 \mathcal P_*=\mathcal P_0^+(-2,z_*),\qquad
 \mathcal M_*=\Re\mathcal P_*>419/200,\qquad |Z_*|<8/7.
 \tag{1}
\]
The transfer is the original
\[
 \mathcal T_0[F_N]
 =N[Y^0](F_Nd_NC_{0,N})+N[Y^N](F_Nd_NC_{0,N}).
 \tag{2}
\]
Retain its local geometric integral \(I_{{\rm geom},N}\), with
unchanged nonzero \(N^{-2}\) coefficient. Its algebraic packet
error is part of that integral and is not included in the
exponentially small error below.

Set
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\\
 M_N=\lceil N/2\rceil,\quad Q_N=\lceil5N/6\rceil,\quad
 J_N=\lfloor N/64\rfloor,\quad K_N=\lfloor N/4096\rfloor,\\
 S_a=\prod_{\nu=1}^a2\sin(\pi\nu/N),\quad
 P_a=(r;r)_a,\quad p_k(Z)=(rZ;r)_k,\\
 c_j=2\cos((2j+1)\pi/N).
\end{gathered}
 \tag{3}
\]
Here \(J_N,K_N\) are integer cutoffs, not the logarithmic action
or an ordinary kernel. Write that kernel as
\(K_N^{\rm ord}\).

For \(b\ge M_N\), put \(n=D-b\), and keep the exact expanded
summand from
[the small internal-index theorem, equations (2)--(4)](research_mixed_next_three_small_internal_indices.md):
\[
\begin{split}
 T_{b,j,k}
 &=\frac{(-q)^b}{\kappa^2N}
       b_{n,j}\mathcal R_N(c_j)^3
       \mathcal K_{3,N}(-2,c_j)
       \frac{r^{-bk}p_k(r^b)p_k(Z_*)}{P_k^2},\\
 b_{n,j}&=(-1)^{n+j}
          \frac{2\sin((2j+1)\pi/N)S_n^2}
               {S_{n-j}S_{n+j+1}},\\
 \mathcal R_N(c_j)&=\kappa(-1)^j q^{j(j+1)},\\
 \mathcal K_{3,N}(w,c_j)
 &=\phi_N^{(t)}
   [\mathcal R_N(t)^3K_N^{\rm ord}(w,t)K_N^{\rm ord}(c_j,t)] .
\end{split}
 \tag{4}
\]
The terminal trace in (4) is complete and signed, including
every repeated-root normal. Its internal summands have not been
replaced by absolute values.

Define
\[
 \boxed{\quad
 \mathscr R_N^{\rm both}
 =\sum_{b=M_N}^{Q_N-1}
       \ \sum_{j=J_N+1}^{D-b}
       \ \sum_{k=K_N+1}^{D-b}T_{b,j,k}.
 \quad}
 \tag{5}
\]
All ranges are literal integer ranges; empty ones are zero.

**Theorem.** There is a fixed \(\epsilon_{\rm both}>0\), specified
in Section 3, such that for all sufficiently large levels of both
parities,
\[
 \boxed{\quad
 \mathcal T_0[F_N](-2,Z_*)
   =I_{{\rm geom},N}+\mathscr R_N^{\rm both}
       +O(e^{N(\mathcal M_*-\epsilon_{\rm both})}).
 \quad}
 \tag{6}
\]
Thus the physical range in (5) is the old whole middle range,
rather than the shortened range after the physical half-band was
removed. Both small-index exclusions are retained. No suppression
or noncancellation assertion for (5) is made.

## 2. Exact restoration and the eligible subset estimates

Let \(\delta_{\rm ph}>0\) and
\(b_N^{\rm rem}=\lfloor N(1/2+\delta_{\rm ph})\rfloor+1\)
be precisely the width and cutoff in the complete transfer
reduction, equation (10). Let
\[
 \mathcal H_N=\{M_N,\ldots,b_N^{\rm rem}-1\},\qquad
 \mathcal I_N=\{b_N^{\rm rem},\ldots,Q_N-1\}.
 \tag{7}
\]
For sufficiently large \(N\), these disjoint sets partition
\(\{M_N,\ldots,Q_N-1\}\).

For any such physical set \(\mathcal B\), define four sums of
the exact summands (4):
\[
\begin{split}
 A(\mathcal B)&=\sum_{b\in\mathcal B}
                         \sum_{j=0}^{D-b}\sum_{k=0}^{D-b}T_{b,j,k},\\
 L_k(\mathcal B)&=\sum_{b\in\mathcal B}
          \sum_{j=0}^{D-b}\sum_{k=0}^{\min(K_N,D-b)}T_{b,j,k},\\
 L_jH_k(\mathcal B)&=\sum_{b\in\mathcal B}
          \sum_{j=0}^{\min(J_N,D-b)}
                          \sum_{k=K_N+1}^{D-b}T_{b,j,k},\\
 H_jH_k(\mathcal B)&=\sum_{b\in\mathcal B}
          \sum_{j=J_N+1}^{D-b}
                          \sum_{k=K_N+1}^{D-b}T_{b,j,k}.
\end{split}
 \tag{8}
\]
The exact partition is
\[
 H_jH_k(\mathcal B)
       =A(\mathcal B)-L_k(\mathcal B)-L_jH_k(\mathcal B).
 \tag{9}
\]
In particular the last term is low \(j\), high \(k\).
There is no subtraction of low \(j\), all \(k\) without an
overlap correction.

Each term on the right of (9), for \(\mathcal B=\mathcal H_N\),
has an adopted bound:
\[
\begin{array}{c|c|l}
\text{term}&\text{upper rate}&\text{source}\\ \hline
 A(\mathcal H_N)&\mathcal M_*-\gamma/2&
 \text{physical half-band, }\gamma=10^{-13}\\
 L_k(\mathcal H_N)&419/200-3/1000&
 \text{small outgoing indices}\\
 L_jH_k(\mathcal H_N)&419/200-1/32&
 \text{small internal indices}.
\end{array}
 \tag{10}
\]
Each bound allows a fixed polynomial prefactor.

The first line is
[physical continuation from the complete vertical, Section 4](research_mixed_next_three_physical_half_band_from_vertical.md),
or equation (27) of the complete transfer reduction. At each
physical node,
\[
 \sum_{j,k}T_{b,j,k}
   =\frac{F_N(-2,r^b)}{P_b}C_{0,N}(r^b,Z_*).
 \tag{11}
\]
Thus this bound controls the absolute sum over physical nodes
of the whole attached factor. It is not a bound for arbitrary
subsets of its internal \(j,k\) summands.

The second line is
[small outgoing indices, Proposition (8)](research_mixed_next_three_small_outgoing_indices.md).
It applies to every physical-node subset, retaining the
coherent sum over all \(j\), which is exactly \(\ell_b(-2)\).
We use precisely that scope in \(L_k(\mathcal H_N)\).

The third line is
[small internal indices, Theorem (5)](research_mixed_next_three_small_internal_indices.md).
That theorem bounds the sum of absolute values after the
complete signed terminal trace, for every subset of the
expanded triples with \(j\le J_N\), and every outgoing \(k\).
It therefore pays \(L_jH_k(\mathcal H_N)\), as well as
\(L_jH_k(\mathcal I_N)\). Its hypotheses include \(|Z_*|<8/7\)
from (1).

The previously adopted reduction is
\[
 \mathcal T_0[F_N]
   =I_{{\rm geom},N}
       +H_jH_k(\mathcal I_N)+L_jH_k(\mathcal I_N)
       +E_N^{\rm old},
 \quad
 E_N^{\rm old}=O(e^{N(\mathcal M_*-\epsilon_{\rm old})}),
 \tag{12}
\]
where \(\epsilon_{\rm old}>0\) is exactly the number in
equation (32) of the complete transfer reduction.
It follows from (9),(12) that
\[
\begin{split}
 \mathcal T_0[F_N]-I_{{\rm geom},N}-\mathscr R_N^{\rm both}
   =E_N^{\rm old}+L_jH_k(\mathcal I_N)
       -A(\mathcal H_N)+L_k(\mathcal H_N)
       +L_jH_k(\mathcal H_N).
\end{split}
 \tag{13}
\]
This displays the restoration sign explicitly. It also explains
why neither positivity of individual residues nor a bound for
arbitrary outgoing subbands of the physical half-band is needed.

## 3. Error budget and original filter scope

Take
\[
 \epsilon_{\rm both}
   =\frac14\min\{\epsilon_{\rm old},\gamma/2,3/1000,1/32\}>0.
 \tag{14}
\]
Equations (1),(10),(13) imply (6). The factor four leaves room
to absorb every fixed polynomial prefactor for sufficiently
large \(N\). No quantitative excess of
\(\mathcal M_*\) above \(419/200\) is spent.

All terms in (13) concern the already unfiltered original
coefficients. The old cardinal filter, its partial
first-coordinate deletion, both Fourier sectors, and every
oriented contour current have already been retained and
accounted for in \(E_N^{\rm old}\). None is split again by
\(j\) or \(k\), and no second filter correction is introduced.
The newly restored physical band is inside the old retained
node range; the old filter cutoffs themselves are unchanged.

## 4. The unchanged endpoint in the exact coupled amplitude

Put
\[
 L=\lfloor N/6\rfloor,\qquad U=\lfloor N/2\rfloor-1,\qquad
 m_{jk}=\max\{L,j,k\},
\]
\[
 W_{jk,N}
   =\sum_{n=m_{jk}}^U
       q^{-(k+1)n}
       \frac{S_n^3}{S_{n-j}S_{n+j+1}S_{n-k}} .
 \tag{15}
\]
The substitution \(n=D-b\) sends the restored physical range
\(M_N\le b<Q_N\) exactly to \(L\le n\le U\), at both parities.
The original phase cancellation and outgoing formula in
[coupled phases, equations (4)--(8)](research_mixed_next_middle_insertion_coupled_phases.md)
therefore give
\[
\boxed{\begin{split}
 \mathscr R_N^{\rm both}
 =\frac{\kappa(-q)^D}{N}
 \sum_{j=J_N+1}^U\sum_{k=K_N+1}^U
 &\frac{2\sin((2j+1)\pi/N)\,i^k
          q^{3j(j+1)+k(k-1)/2}}{S_k^2}\\
 &\qquad\cdot p_k(Z_*)\,W_{jk,N}\,
                       \mathcal K_{3,N}(-2,c_j).
\end{split}}
 \tag{16}
\]
All factorial indices in (15) are nonnegative and below \(N\),
including \(n+j+1\le2U+1<N\). The endpoints \(j\), \(k\), and
\(L\) are retained through their maximum, with no fictitious
zero at the fixed physical cutoff. The exact scalar in (16)
is inherited from (4), not a new normalization.

Consequently the endpoint identities and the all-\(j\),
\(k\ge\varepsilon N\) theorem of
[the physical endpoint packet](research_mixed_next_middle_physical_endpoint_packet.md)
apply to precisely this \(W\), with \(\varepsilon=1/4096\).
For example its exact final positive amplitude remains
\[
 a_U^{j,k}=
 \begin{cases}
 S_U/(2S_{U-k}),&N=2m,\ U=m-1,\\[2mm]
 S_U\,2\sin(\pi(m-j)/N)/
       \{4\cos^2(\pi/(2N))S_{U-k}\},&N=2m+1,\ U=m-1 .
 \end{cases}
 \tag{17}
\]
There is no new endpoint displaced by \(\delta_{\rm ph}N\).

One can equivalently retain the entire polynomial
\[
 \mathcal B_N^{\rm both}(t,Z)=
 \sum_{j=J_N+1}^U\sum_{k=K_N+1}^U
 \frac{2\sin((2j+1)\pi/N)\,i^k
       q^{3j(j+1)+k(k-1)/2}}{S_k^2}
 p_k(Z)W_{jk,N}K_N^{\rm ord}(c_j,t).
 \tag{18}
\]
It has degree at most \(U\) in each variable. Then exactly
\[
 \mathscr R_N^{\rm both}
  =\frac{\kappa(-q)^D}{N}
     \phi_N^{(t)}
       [\mathcal R_N(t)^3K_N^{\rm ord}(-2,t)
                                  \mathcal B_N^{\rm both}(t,Z_*)].
 \tag{19}
\]
This preserves both coupled index phases inside the complete
Hermite trace. It does not estimate that polynomial on a shifted
contour. In particular a relative \(O(N^{-1})\) approximation
of each \(W_{jk,N}\) cannot be discarded inside (16) without
a bound for its complete coupled error.

The result is a base-reference reduction only. It proves neither
new outside jets, a bound for (16), noncancellation of the full
transfer, nor a knot-family volume statement.

