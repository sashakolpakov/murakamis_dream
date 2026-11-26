# Coherent deletion of the highest conditional rows

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The last rows of a canonical conditional kernel can be large away from
the physical grid. In the original finite operator, however, an entire
short block of those rows has small exponential norm. The proof keeps
the conditional sum coherent before applying a norm estimate. It applies
to both vertex types at every level, including all original normal data.
It is a local operator estimate; comparison with a whole observed word
still requires bounds for the surrounding factors.

## 1. The exact original block

Use the matrices of the
[exact mixed contraction](research_mixed_wire_exact_contraction.md).
Write \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\),
\(P_j=(r;r)_j=\delta_j S_j\), and
\(S_j=\prod_{h=1}^j2\sin(\pi h/N)>0\). The matrix changing the
original Newton coordinates is denoted here by \(\mathsf S\):
\[
 \mathsf S_{j\ell}=
 \frac{\delta_j^{-1}q^{j\ell}}{S_\ell S_{j-\ell}}
 \quad(0\le\ell\le j),\qquad
 \Gamma=\mathsf S\mathsf S^T,\qquad
 A_n=\mathsf S^TB_n\mathsf S.
 \tag{1}
\]
The entries outside the indicated triangle are zero. Transposes in
these exact identities are bilinear, not Hermitian adjoints.
For \(\epsilon=0,1\), the original vertex matrix is
\[
 (B_{3+\epsilon})_{ij}
 =\kappa^{1+\epsilon}N^\epsilon
       \frac{P_{i+j}}{(P_iP_j)^\epsilon}\,
                      1_{\{i+j<N\}},\qquad |\kappa|=1.
 \tag{2}
\]

For \(0\le L\le\lfloor N/2\rfloor\), let \(\Pi_L\) be the diagonal
projection onto indices \(D-L,\ldots,D\), and put
\[
 E_{\epsilon,L}=\mathsf S^T\Pi_L B_{3+\epsilon}\mathsf S,
 \qquad
 \mathsf S E_{\epsilon,L}\mathsf S^{-1}
                         =\Gamma\Pi_L B_{3+\epsilon}.
 \tag{3}
\]
Thus (3) is precisely the contribution of conditional indices
\(i=D-k\), \(0\le k\le L\), in the original conditional product
\(\Gamma B_{3+\epsilon}\). It is not an arbitrary coordinate
truncation of the original matrix. Both adjacent triangle supports
force its two physical outer indices to be at most \(L\).
Its rank is therefore at most \(L+1\).

The deletion is one-sided in the conditional index and need not be a
symmetric operator. Formula (3) specifies exactly which original
summands are retained. In particular it does not replace either
repeated-root algebra by its value-only quotient.

## 2. The final row has polynomial norm

Let \(u_j=(-q^{-1})^j\) and let \(e_0\) be the first coordinate vector.
The sine reflection identity \(S_{D-j}=N/S_j\), together with
\(\delta_D=1\), gives
\[
 \mathsf S_{D,\ell}=\frac{u_\ell}{N},\qquad
 \mathsf S_{0,\ell}=1_{\{\ell=0\}},\qquad
 (B_{3+\epsilon})_{D,0}=\kappa^{1+\epsilon}N.
 \tag{4}
\]
All other entries in that row of \(B\) vanish. Consequently
\[
 E_{\epsilon,0}=\kappa^{1+\epsilon}u e_0^T,\qquad
                         \|E_{\epsilon,0}\|_2=\sqrt N.
 \tag{5}
\]
This is an identity in the original coordinates. The endpoint
vectors are \(u\) and \(e_0\); they are not identified with the
ordinary complete evaluation vector \(v(-2)\).

## 3. A uniform bound for the whole highest-row block

**Theorem 1.** At every level \(N\ge2\), for both vertex types and
every \(1\le L\le\lfloor N/2\rfloor\),
\[
 \|E_{\epsilon,L}\|_2
 \le \sqrt N\sum_{k=0}^L\frac{(2N)^k}{k!}
 \le 2\sqrt N\left(\frac{2eN}{L}\right)^L.
 \tag{6}
\]
In particular, for \(0<\eta\le1/2\) and \(L=\lfloor\eta N\rfloor\),
including \(L=0\),
\[
 \|E_{\epsilon,L}\|_2
       \le 2\sqrt N\exp\{N\sigma(\eta)\},\qquad
                 \sigma(\eta)=\eta\log(2e/\eta)\longrightarrow0.
 \tag{7}
\]

*Proof.* Denote row \(j\) of \(\mathsf S\) by \(\mathsf s_j\).
Sine reflection gives, for \(\ell\le D-k\),
\[
 |\mathsf S_{D-k,\ell}|
   =\frac{S_{k+\ell}}{N S_\ell}\le\frac{2^k}{N},
 \qquad
                    \|\mathsf s_{D-k}\|_2\le\frac{2^k}{\sqrt N}.
 \tag{8}
\]
For \(b\le L\le N/2\), concavity of sine gives
\(2\sin(\pi h/N)\ge4h/N\) for \(h\le b\). Hence
\[
 \|\mathsf s_b\|_2\le\|\mathsf s_b\|_1
  \le\sum_{\ell=0}^b
       \frac{(N/4)^b}{\ell!(b-\ell)!}
  =\frac{(N/2)^b}{b!}.
 \tag{9}
\]
The exact support and moduli in (2) are
\[
 |(B_{3+\epsilon})_{D-k,b}|
   =N\,\frac{S_k^\epsilon}
                   {S_b^\epsilon S_{k-b}}\quad(0\le b\le k).
 \tag{10}
\]
For a three-vertex, (8)--(10) bound its \(k\)-th row contribution by
\[
 \frac{2^k}{\sqrt N}\,
 N\sum_{b=0}^k
     \frac{(N/4)^{k-b}}{(k-b)!}\frac{(N/2)^b}{b!}
            =\sqrt N\,\frac{(3N/2)^k}{k!}.
 \tag{11}
\]
For a four-vertex, monotonicity of \(\sin x/x\) gives
\(S_k/(S_bS_{k-b})\le {k\choose b}\).
The sequence \((N/2)^b/b!\) is nondecreasing for \(b\le k\le N/2\).
Thus the corresponding contribution is at most
\[
 \frac{2^k}{\sqrt N}\,
 N\sum_{b=0}^k {k\choose b}\frac{(N/2)^b}{b!}
              \le\sqrt N\,\frac{(2N)^k}{k!}.
 \tag{12}
\]
Here a rank-one matrix \(\mathsf s_{D-k}^T\mathsf s_b\) has norm
\(\|\mathsf s_{D-k}\|_2\|\mathsf s_b\|_2\), also for complex rows.
Summing proves the first inequality in (6). Successive terms read
backward have ratio at most \(L/(2N)\le1/4\), so the sum is at most
\((4/3)(2N)^L/L!\). Finally \(L!\ge(L/e)^L\).
For (7), \(x\log(2eN/x)\) increases on \(0<x\le N/2\);
use \(L\le\eta N\), and use (5) when \(L=0\).
\(\square\)

## 4. What the block estimate does and does not control

For any fixed word, define
\(\widetilde A_v=A_{3+\epsilon_v}-E_{\epsilon_v,L}\).
There is the exact noncommuting telescope
\[
 A_1\cdots A_m-\widetilde A_1\cdots\widetilde A_m
   =\sum_{v=1}^m
       \widetilde A_1\cdots\widetilde A_{v-1}\,
       E_{\epsilon_v,L}\,A_{v+1}\cdots A_m.
 \tag{13}
\]
The original boundary scalar follows by multiplying this identity
by its actual boundary vectors. All ordinary boundary derivatives
follow by differentiating those finite vectors. For arbitrary vectors
\(x,y\), its error is bounded by
\[
 \sum_{v=1}^m
 \|(\widetilde A_1\cdots\widetilde A_{v-1})^T x\|_2\,
 \|E_{\epsilon_v,L}\|_2\,
 \|A_{v+1}\cdots A_m y\|_2 .
 \tag{14}
\]
The remaining factors in (14) cannot be replaced by their eigenvalue
gaps or by positivity in an unrelated metric. In particular (7)
does not prove that this error is below the geometric rate of every
mixed word. It provides a small exponential cost for the inserted
block; a useful observed-word bound must still control its surrounding
vectors.

The estimate explains why a large off-grid last-row value need not
force a large original-source contribution: its whole physical
operator has the exact form (5). It does not assert cancellation of
all outer Fourier aliases, a lower bound for the retained source,
or a volume theorem for an arbitrary matrix word.

## 5. Reproduction

Run:

    python3 experiments/check_mixed_coherent_endpoint_deletion.py

The exact checks retain the original crossing matrices, both vertex
types, every indicated cutoff, the final-row scalar, the reflected
row moduli, both support constraints, and noncommuting word telescopes.
The all-level norm estimate follows from (8)--(12); it is not inferred
from numerical matrix norms.
