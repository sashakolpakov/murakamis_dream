# Removing intermediate endpoint indices with the original end vectors retained

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The positive-similarity representation of a homogeneous three-crossing
chain permits a global deletion at every internal matrix join. Its
error is below the actual geometric action, uniformly in each fixed
chain length and on a fixed neighborhood of the complete outside
colors. The first and last matrix factors are retained: an omitted
internal index then has a small column factor on both sides. This
accounts for the exponential size of the actual boundary observations.

The result concerns intermediate Newton indices in the similarity
gauge. It is not a pointwise deletion of a Fourier-wire interval or
a bound for the full complement of the local Fourier saddle.

## 1. The actual source and an exact internal compression

Use the original matrices and full boundary vector
\[
 A=JM^3,\qquad H=M^*M,\qquad MAM^{-1}=\kappa H,\qquad
 v(z)=(e_0(z),\ldots,e_{N-1}(z))^T.
 \tag{1}
\]
These identities and the all-parity boundary-jet bounds are proved
in [the positive-cycle note](research_positive_three_crossing_cycle.md),
Sections 1 and 8. Put \(D=N-1\),
\[
 L=\lfloor N/50\rfloor,\quad
 P=\operatorname{diag}(\mathbf1_{L<j<D-L}),\quad Q=I-P.
 \tag{2}
\]
Let \(\widetilde A=A-E_L\) be the exact corner-deleted vertex
of [the traced-vertex theorem](research_traced_three_vertex_endpoint.md),
Section 7, and set
\[
 B=\kappa^{-1}M\widetilde A M^{-1}=H-D_N,
 \qquad D_N=\kappa^{-1}ME_LM^{-1}.
 \tag{3}
\]
For fixed \(m\ge2\), define the compressed source by
\[
 S^{\rm int}_{m,N}(z,w)
 =\kappa^m v(z)^TM^{-1}B(PB)^{m-1}Mv(w).
 \tag{4}
\]
Every original boundary polynomial and its ordinary derivatives
remain literal. Equivalently (4) inserts the exact matrix
\(\Pi=M^{-1}PM\) between successive retained vertices:
\(v(z)^T\widetilde A\Pi\widetilde A\cdots
\Pi\widetilde A v(w)\). No projection is applied to the
left or right end vector itself.

## 2. Endpoint columns of the original crossing

**Lemma 1.** With the Euclidean operator norm,
\[
 \|MQ\|\le CN^a e^{2N/25},\qquad
 \|BQ\|+\|QB\|\le CN^a e^{N(c+2/25)},\qquad
 \|B\|\le CN^a e^{2cN},
 \quad c=2\mathcal J(5/6).
 \tag{5}
\]

*Proof.* The original triangular entries have moduli
\(S_j/(S_kS_{j-k})\) for \(k\le j\). If \(k\le L\),
\[
 |M_{jk}|\le\frac{2^k}{S_k}
       \le\frac{(N/3)^k}{k!}
       \le\exp\left\{\frac N{50}
                             (1+\log(50/3))\right\}
       <e^{2N/25}.
 \tag{6}
\]
The first inequality bounds each factor in \(S_j/S_{j-k}\)
by two. For the second, \(\sin(\pi r/N)\ge3r/N\) on
\(0\le r/N\le1/50\). Indeed the sine Taylor lower bound,
\(25/8<\pi<22/7\), and
\[
 \frac{25}{8}\left(1-\frac{(22/7)^2}{6\cdot50^2}\right)-3
             =\frac{7229}{58800}>0
\]
prove it. Use \(k!\ge(k/e)^k\), and the increase of
\(k\log(eN/(3k))\) up to \(N/50\). The empty product
\(k=0\) is treated directly. Finally
\(\sum_{r=0}^5 3^r/r!-50/3=26/15>0\), so
\(\log(50/3)<3\).

If instead \(D-k\le L\), sine-factorial reflection gives
\[
 |M_{jk}|=\frac{S_{D-k}}{S_{D-j}S_{j-k}}
       \le {D-k\choose j-k}\le2^{D-k}\le2^L.
 \tag{7}
\]
The binomial estimate follows from the decrease of \(\sin x/x\)
on \((0,\pi)\), applied to each sine ratio. Matrix dimensions
contribute only powers of \(N\); (6)--(7) prove the first bound.

The original one-crossing theorem gives \(\|M\|\le Ce^{cN}\).
Since \(H\) is Hermitian,
\(\|HQ\|=\|QH\|\le\|M\|\|MQ\|\).
The already-proved corner estimate is
\(\|D_N\|\le CN^a e^{\sigma N}\),
\(\sigma=\log(100e)/50<3/25<c+2/25\).
Combining these estimates proves the second bound of (5).
The same comparison with \(\|H\|\le Ce^{2cN}\) proves
the third. None of these estimates asserts positivity of \(B\).
\(\square\)

## 3. A global source error below the geometric rate

**Theorem 2.** For every fixed \(m\ge2\) and fixed nonnegative
integers \(a,b\), the original full source
\(S_{m,N}(z,w)=v(z)^TA^mv(w)\) satisfies, at both parities,
\[
 \sup_{z,w\in[-2,2]}
 |\partial_z^a\partial_w^b(S_{m,N}-S^{\rm int}_{m,N})(z,w)|
 \le CN^A\exp N\{(2m-1)c+M_\infty+4/25\}.
 \tag{8}
\]
For complex boundary angles \(z=-2\cos(u+ih)\),
\(w=-2\cos(v+ik)\), add \(|h|+|k|\) to the exponent.
If \(M_m\) is the positive geometric action at the two complete
outside colors, the exponent in (8) is less than \(M_m-2/75\).
Thus a fixed complex neighborhood of those ordinary colors retains
a strict gap and every fixed ordinary derivative.

*Proof.* First compare the retained chain with (4). Telescoping
the insertions of \(P=I-Q\) gives the exact identity
\[
 B^m-B(PB)^{m-1}
 =\sum_{j=1}^{m-1} B(PB)^{j-1}Q B^{m-j}.
 \tag{9}
\]
Every summand contains a factor \(BQ\) and a factor \(QB\),
because \(Q^2=Q\), and at most \(m-2\) remaining factors
\(B\). Therefore (5) bounds its operator norm by
\[
 CN^A\exp N\{2(m-2)c+2(c+2/25)\}
          =CN^A e^{N\{(2m-2)c+4/25\}}.
 \tag{10}
\]
This is why both neighboring factors, including the first and
last matrix of the chain, are retained. A single end-vector
truncation would not give (10).

At physical double roots, actual inverse-crossing multiplication
preserves the full value and first-normal identities
\[
 (v^TM^{-1})^{(\nu)}(c_a)
 =\sum_{j=0}^{\nu}{\nu\choose j}
       (R^{-1})^{(\nu-j)}(c_a)v^{(j)}(c_a)^T,
       \quad \nu=0,1.
 \tag{11}
\]
At the odd simple root only the value is used. The original
full-Hermite estimates give
\[
 \|(v^TM^{-1})^{(\nu)}(c_a)\|
       \le CN^A e^{NM_\infty/2},\qquad
 \|Mv^{(\nu')}(c_b)\|
       \le CN^A e^{N(c+M_\infty/2)}.
 \tag{12}
\]
These are precisely the physical source estimates in Proposition 8
of the positive-cycle note, including the original normal forcing.
Multiplying (10) by (12) proves the rate in (8) for all required
physical mixed jets. Full Hermite interpolation has polynomial
interval norm and gives the same bound on the real square. Markov's
inequality supplies the fixed higher ordinary derivatives. Both
sources have degree at most \(N-1\) in each free color, so
Bernstein--Walsh gives the stated angular-height cost.

The original corner-removal error has rate
\((2m-1)c+M_\infty+3/25\), hence is smaller than (8).
Adding it restores the full original source. Finally Corollary 5
of the traced-vertex theorem proves
\[
 M_m>(2m-1)c+M_\infty+3/25+1/15,
 \qquad 3/25+1/15-4/25=2/75.
 \tag{13}
\]
This proves the gap. For a small ordinary-color bidisk, choose its
angular lifts with uniformly small heights; the cost tends to zero
as the bidisk shrinks, also at the ramified complete colors.
Apply the same argument to each fixed ordinary derivative.
\(\square\)

The theorem estimates the signed total of all omitted internal
similarity-index configurations, by an operator estimate valid for
the actual end observations. It does not replace those observations
by a positive spectral measure. The matrix \(\Pi\) is generally
oblique in the original coefficient norm, and no bound on its norm
was assumed. In a Fourier representation its insertion is an exact
additional finite kernel, not restriction to a real wire subinterval.

What remains is a sharp global analysis of the retained compact
index chain, or of the complementary Fourier cycle of its local
packet. Theorem 2 does not identify that compact-chain scalar with
its local Gaussian contribution and supplies no new nonzero
closing coefficient by itself.

## 4. Exact algebra reproduction

Run `python3 experiments/check_homogeneous_chain_internal_projection.py`.
The [checker](../experiments/check_homogeneous_chain_internal_projection.py)
and [record](../repro/results/research-homogeneous-chain-internal-projection.json)
verify the noncommutative telescope, the two adjacent small factors,
the literal similarity-source normalization and the rational budgets.
They do not estimate a quantum asymptotic by sampling finite levels.
