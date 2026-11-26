# Exact crossing filters for the ordinary mark: recovery and an arithmetic obstruction

Research deduction, 7 November 2026. At odd squarefree levels the
ordinary Casimir mark is an explicit polynomial in the original crossing,
with coefficient absolute sum one. It expresses the ordinary observation
using positive crossing powers that grow with the level. At infinitely
many other odd levels, two distinct physical nodes have the same crossing
eigenvalue, so no function of that crossing can isolate the ordinary
mark. Neither statement supplies an ordinary closure theorem from the
proved cyclic three/four asymptotics. No numerical evaluation is used.

## 1. Original eigenvalues and the complete mark

Keep the full Newton algebra, including the first normals at its double
roots,
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 A_n=JM^n,\qquad v=v(-2).
 \tag{1}
\]
Here \(M\) is multiplication by the original crossing \(R\),
and \(C\) is multiplication by \(z\). The original crossing
eigenvalues, with their physical-node indexing, are
\[
 \lambda_j=R(c_j)=\kappa_N(-1)^j
       \exp\!\left(\frac{\pi i j(j+1)}N\right),\qquad
 c_j=2\cos\frac{(2j+1)\pi}N,\qquad 0\le j<N.
 \tag{2}
\]
At a double node the full local multiplication block is
\[
 M_j=\lambda_j(1+\alpha_j\varepsilon),\qquad
 \varepsilon^2=0,\qquad
 \alpha_j=\frac{i(N-1-2j)}{4\sin((2j+1)\pi/N)}\ne0.
 \tag{3}
\]
These are the original value and normal formulas in
[arbitrary-power compilation, Section 6](research_arbitrary_power_source_compilation.md).
No diagonalizable quotient of (1) is used.

Suppose first that \(N\) is odd. Put
\(h=(N-1)/2\) and \(\rho_N=\lambda_h=R(-2)\).
The node \(c_h=-2\) is simple; the other distinct physical nodes
are double and may be indexed by \(0\le j<h\). For any integer
\(d\) with \(-h\le d\le h\), the signs in (2) give
\[
 \frac{\lambda_{h-d}}{\rho_N}
 =(-1)^{-d}\exp\!\left(\frac{\pi i(-dN+d^2)}N\right)
 =\exp\!\left(\frac{\pi i d^2}N\right).
 \tag{4}
\]
In particular every ratio is a \(2N\)-th root of unity.

The [ordinary Casimir-mark theorem](research_mixed_ordinary_boundary_casimir_mark.md),
equations (5)--(8), identifies the primitive complete-node idempotent as
\[
 \pi_N(z)=\frac{2T_N(z/2)+2}{N^2(z+2)},\qquad
 \Pi_N:=\pi_N(C)=Jvv^T,
 \qquad
 v^TWv=\rho_N^{-3}\operatorname{tr}(\Pi_NWA_3).
 \tag{5}
\]
The polynomial \(\pi_N\) equals one at the simple complete node
and vanishes in value and first normal at every other physical node.
Equation (5) holds for every matrix \(W\), in particular every
original three/four word. Its scalar has modulus one and no omitted
power of \(N\).

## 2. A coefficient-controlled exact filter at odd squarefree levels

**Proposition 1.** Let \(N\ge3\) be odd and squarefree, and set
\[
 L=2N,\qquad p_L(z)=\frac1L\sum_{a=0}^{L-1}z^a.
\]
Then on the full original algebra
\[
                 \boxed{\quad \Pi_N=p_L(M/\rho_N)^2.\quad}
 \tag{6}
\]

*Proof.* If a ratio in (4) equals one, then \(2N\mid d^2\),
in particular \(N\mid d^2\). Squarefreeness implies
\(N\mid d\). Since \(|d|\le(N-1)/2\), necessarily
\(d=0\). Thus the complete eigenvalue occurs only at its simple
physical node. Every other ratio is a nontrivial \(L\)-th root of
unity, where \(p_L\) has a zero. Squaring gives a double zero,
so the filter vanishes on the entire local algebra (3), including
its first normal. At the complete simple node it has value one.
The physical local-factor decomposition of (1) therefore identifies
it with \(\Pi_N\). \(\square\)

Write
\[
 p_L(z)^2=\sum_{a=0}^{2L-2}c_{a,L}z^a,\qquad
 c_{a,L}=\begin{cases}
 (a+1)/L^2,&0\le a<L,\\
 (2L-1-a)/L^2,&L\le a\le2L-2.
 \end{cases}
 \tag{7}
\]
These coefficients are nonnegative and sum to one. Combining (5)--(7)
and cycling each trace gives the exact ordinary observation
\[
 \boxed{\quad
 v^TWv=\sum_{a=0}^{4N-2}c_{a,2N}\rho_N^{-a-3}
                  \operatorname{tr}(WA_{a+3}).\quad}
 \tag{8}
\]
Indeed
\(\operatorname{tr}(M^aWA_3)
 =\operatorname{tr}(WA_3M^a)=\operatorname{tr}(WA_{a+3})\).
The coefficient absolute sum in (8) is exactly one. This assertion
does not bound the matrix norm of the filter: \(M\) is not unitary
in a positive metric on the full algebra, and \(\Pi_N=Jvv^T\)
is not an orthogonal projection.

The completions in (8) have one original positive crossing power
\(3\le a+3\le4N+1\); they are not asserted to be words whose
letters all lie in \(\{3,4\}\). The new
[spectral-rate theorem](research_mixed_word_spectral_radius.md)
controls repetitions of each fixed three/four word, not these
level-dependent crossing powers or the coherent sum in (8).
The full-normal period relation of arbitrary-power compilation,
equation (22), has a nilpotent correction and a period growing with
\(N\); it does not turn (8) into finitely many fixed-word estimates.
Thus the exact coefficient cost is controlled, but the required
marked-source estimate and noncancellation are not supplied.

## 3. A repeated-eigenvalue obstruction in the actual source

**Proposition 2.** For every odd prime \(p\ge5\), at level
\(N=p^2\) the complete idempotent \(\Pi_N\) is not a function
of the crossing \(M\). In particular it is not a polynomial,
a holomorphic functional-calculus expression, or a fixed-level
matrix-norm limit of such expressions.

*Proof.* Set \(d=2p\) and \(j=h-2p\). Since
\(p^2-4p-1\ge0\) for \(p\ge5\), one has
\(0\le j<h\). This is a noncomplete double node. Equation (4)
gives
\[
               \lambda_j/\rho_N
                  =\exp(\pi i\,4p^2/p^2)=1.
 \tag{9}
\]
The crossing retains a nonzero normal there: explicitly (3) gives
\(\alpha_j=ip/\sin(4\pi/p)\ne0\).

For a function \(f\) holomorphic near the spectrum, its action
on this double local factor and on the complete simple factor is
respectively
\[
 f(M_j)=f(\rho_N)+\rho_N\alpha_j f'(\rho_N)\varepsilon,
 \qquad f(M_h)=f(\rho_N).
 \tag{10}
\]
But \(\Pi_N\) has value zero on the first factor and one on
the second. These incompatible value requirements already rule out
\(f(M)=\Pi_N\), irrespective of the derivative in (10).
Retaining more derivative data cannot separate identical eigenvalues.

At fixed \(N\), physical-node value extraction is a continuous
linear functional on the finite-dimensional multiplication algebra.
Every \(f(M)\) has equal extracted values at these two nodes,
and every matrix-norm limit retains that equality. Equivalently,
the finite-dimensional algebra \(\mathbb C[M]\) is closed and
contains the holomorphic functional calculus. This also rules out
limits of filters with unbounded degree at that fixed level.
In the maximum of the two physical value errors, every such filter
has error at least \(1/2\). No level-uniform Euclidean norm bound
is inferred from this physical-coordinate observation. \(\square\)

For example, the squared average in (6), if used at a level from
Proposition 2, acts on the extra block as
\(1+(L-1)\alpha_j\varepsilon\), not as zero. Discarding that
block or its normal would change the original source.

At even levels the separate obstruction is already exact:
\(-2\) is not a physical root, and the ordinary observation is the
forced two-resolvent expression (15) of the Casimir-mark theorem.
That theorem's nonzero commutator (16) rules out a single Casimir
mark representing the observation for every matrix \(W\), hence
also a mark that is merely a function of \(M=R(C)\).
Neither the odd simple-node identity nor (6) extends to that case.

These statements prevent one all-level ordinary-mark construction
by functional calculus of the single crossing. They do not exclude
a noncommuting three/four-word completion, a parameter deformation
that introduces new operators, or a source-specific residual estimate
for selected \(W\). They also do not show that the ordinary
coefficient vanishes. The original signed boundary functional,
all physical normals and the outstanding open-source comparison
remain unchanged.
