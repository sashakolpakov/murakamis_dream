# Conditional endpoint estimates uniform in the twist power

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The highest conditional rows admit an operator bound independent of
the signed crossing power. The reason is algebraic: every crossing
power commutes with the same lower bidiagonal coordinate
matrix, whose first quarter of diagonal entries are distinct.

This estimate concerns a specified part of the original operator.
Its contribution after closing an entire composition still depends
on the neighboring vectors.

## 1. A triangular commutator estimate

Fix \(N\ge2\), put \(D=N-1\), and let \(C\) be the original
matrix for multiplication by the boundary variable \(z\) in the Newton
basis:
\[
 C_{jj}=c_j=2\cos\frac{(2j+1)\pi}{N},\qquad
 C_{j,j-1}=-d_j=-4\sin^2\frac{\pi j}{N}.
 \tag{1}
\]
All other entries vanish. Put \(\gamma=\pi^2/4\).

**Lemma 1.** Suppose \(F\) is lower triangular, commutes with
\(C\), and satisfies \(|F_{jj}|\le1\). For
\(0\le l\le j\le\lfloor N/4\rfloor\),
\[
                     |F_{jl}|\le\gamma^{j-l}{j\choose l}.
 \tag{2}
\]

*Proof.* The diagonal case is the hypothesis. For \(l<j\),
the \((j,l)\) entry of \(CF=FC\) gives exactly
\[
 (c_j-c_l)F_{jl}
          =d_jF_{j-1,l}-d_{l+1}F_{j,l+1}.
 \tag{3}
\]
The identity
\[
 |c_j-c_l|
   =4\sin\frac{\pi(j+l+1)}N\sin\frac{\pi(j-l)}N
\]
has both sine arguments in \((0,\pi/2]\), because
\(j+l+1\le2j\le N/2\). Therefore
\[
 |c_j-c_l|\ge\frac{16(j-l)(j+l+1)}{N^2},\qquad
 d_a\le\frac{4\pi^2a^2}{N^2}.
 \tag{4}
\]
Induct on \(j-l\). Substitution in (3) reduces (2) to
\[
 j^2{j-1\choose l}+(l+1)^2{j\choose l+1}
            =(j-l)(j+l+1){j\choose l},
 \tag{5}
\]
which follows from the adjacent binomial identities.
\(\square\)

Let \(M\) denote the original crossing matrix, with the conventions
of the [three-crossing calculation](research_positive_three_crossing_cycle.md):
\[
 M_{jl}=\kappa(-1)^j q^{j(l+1)}
              \frac{S_j}{S_lS_{j-l}},\qquad
 q=e^{\pi i/N},\quad |\kappa|=1,\quad
 S_j=\prod_{a=1}^j2\sin\frac{\pi a}N.
 \tag{6}
\]
It is invertible and lower triangular, and commutes with \(C\)
because both are multiplication operators in the same finite
algebra. Every diagonal entry of \(M\) has modulus one.
Consequently Lemma 1 applies to \(F=M^p\) for every integer \(p\),
with the same bound (2). The power may depend on \(N\).
No diagonalizability of the full algebra is assumed; its repeated
roots and first normal directions remain present.

## 2. The exact endpoint block for every integer power

Use the basis-change matrix \(\mathsf S\) from the
[exact contraction](research_mixed_wire_exact_contraction.md):
\[
 \mathsf S_{jl}=\frac{\delta_j^{-1}q^{jl}}{S_lS_{j-l}}
       \quad(l\le j),\qquad
 \delta_j=\exp\left(\frac{\pi i j}{2}
                    -\frac{\pi i j(j+1)}{2N}\right).
 \tag{7}
\]
Its remaining entries are zero. Let \(J\) reverse the Newton
indices and define
\[
 A_n=JM^n,\qquad B_n=\mathsf S^{-T}A_n\mathsf S^{-1}
                         \quad(n\in\mathbb Z).
\]
For \(0\le L\le\lfloor N/4\rfloor\), let \(\Pi_L\) project onto
indices \(D-L,\ldots,D\). In the original coordinates set
\[
                 E_{n,L}=\mathsf S^T\Pi_LB_n\mathsf S.
 \tag{8}
\]
The known three-crossing formula gives
\[
 \begin{split}
 B_n&=B_3\mathsf S M^{n-3}\mathsf S^{-1},\\
 E_{n,L}&=E_{3,L}M^{n-3}.
 \end{split}
 \tag{9}
\]
The right multiplier in the first line is lower triangular, including
when \(n-3<0\). Since \(B_3\) vanishes when \(i+j\ge N\),
the same support condition holds for \(B_n\).
The known support of \(\Gamma=\mathsf S\mathsf S^T\) therefore
makes \(\Gamma\Pi_LB_n\) supported on \(0\le a,b\le L\).
Thus (8) retains both physical support conditions of the original
highest conditional rows. Its rank is at most \(L+1\).

For the final row alone, put \(u_j=(-q^{-1})^j\).
The exact three-crossing endpoint identity and the first row of
\(M^{n-3}\) yield
\[
 E_{n,0}=\kappa^{n-2}u e_0^T,\qquad
                         \|E_{n,0}\|_2=\sqrt N.
 \tag{10}
\]
These are literal Newton-coordinate vectors. Neither is substituted
for a complete ordinary-color boundary vector.

There is also an exact ordinary-color interpretation. Put
\(c_0=2\cos(\pi/N)\) and \(v(w)=(e_0(w),\ldots,e_D(w))^T\).
The Newton products give \(v(c_0)=e_0\), while the original identity
\(M^{-1}=\overline M\) gives \(u=\kappa M^{-1}v(c_0)\). Thus,
for every finite matrix \(W\),
\[
 E_{n,0}=\kappa^{n-1}M^{-1}v(c_0)v(c_0)^T,\qquad
 \operatorname{Tr}(WE_{n,0})
   =\kappa^{n-1}v(c_0)^TWM^{-1}v(c_0).
\]
This is the opposite physical boundary color \(c_0\to+2\), together
with an explicit inverse crossing; the complete ordinary color is
\(-2\). The identity alone supplies no bound for this observation
or its surrounding vectors.

## 3. A bound independent of the filling coefficient

**Theorem 2.** Put \(a=(3+\gamma)/2\). For every integer \(n\),
every \(N\ge2\), and \(1\le L\le\lfloor N/4\rfloor\),
\[
 \|E_{n,L}\|_2
       \le\sqrt N\sum_{k=0}^L\frac{(aN)^k}{k!}
       \le2\sqrt N\left(\frac{eaN}{L}\right)^L.
 \tag{11}
\]
Consequently, for \(0<\eta\le1/4\) and
\(L=\lfloor\eta N\rfloor\), including \(L=0\),
\[
 \sup_{n\in\mathbb Z}\|E_{n,L}\|_2
 \le2\sqrt N\,\exp\{N\sigma(\eta)\},\qquad
 \sigma(\eta)=\eta\log\frac{ea}{\eta}\longrightarrow0.
 \tag{12}
\]

*Proof.* Write \(\mathsf s_b\) for row \(b\) of \(\mathsf S\)
and put \(p=n-3\). For \(b\le L\), the sine lower bound gives
\[
 |\mathsf S_{bj}|\le\frac{(N/4)^b}{j!(b-j)!}.
\]
Lemma 1 and the binomial theorem imply
\[
 \begin{split}
 \|\mathsf s_bM^p\|_1
 &\le\sum_{j=0}^b|\mathsf S_{bj}|
                  \sum_{l=0}^j\gamma^{j-l}{j\choose l}\\
 &\le\frac{(N/4)^b}{b!}(2+\gamma)^b .
 \end{split}
 \tag{13}
\]
This is where dependence on \(p\) disappears.

The [endpoint deletion proof](research_mixed_coherent_endpoint_deletion.md)
gives the reflected high-row bound and exact vertex modulus
\[
 \|\mathsf s_{D-k}\|_2\le\frac{2^k}{\sqrt N},\qquad
 |(B_3)_{D-k,b}|=\frac{N}{S_{k-b}}
               \le N\frac{(N/4)^{k-b}}{(k-b)!}
                 \quad(0\le b\le k).
 \tag{14}
\]
Expand (9) into rank-one matrices. Equations (13)--(14) bound
the row \(D-k\) contribution by
\[
 \frac{2^k}{\sqrt N}N(N/4)^k
       \sum_{b=0}^k\frac{(2+\gamma)^b}{b!(k-b)!}
               =\sqrt N\,\frac{(aN)^k}{k!}.
\]
Summing proves the first inequality in (11). Consecutive terms
read backward have ratio at most \(L/(aN)\le1/(4a)<1/2\);
their sum is at most twice the last term. The inequality
\(L!\ge(L/e)^L\) proves the second bound.
Finally \(x\log(eaN/x)\) increases for \(0<x\le N/4\).
Use \(L\le\eta N\), and use (10) for \(L=0\), to obtain (12).
\(\square\)

## 4. Use in a whole composition

The exact ordered telescope in the endpoint deletion note applies
to arbitrary signed powers \(n_1,\ldots,n_m\), with
\(\widetilde A_v=A_{n_v}-E_{n_v,L}\).
For original boundary vectors \(x,y\), (12) bounds the difference
between the two observed products by
\[
 2\sqrt N e^{N\sigma(\eta)}
 \sum_{v=1}^m
  \|(\widetilde A_1\cdots\widetilde A_{v-1})^Tx\|_2
  \|A_{v+1}\cdots A_m y\|_2.
 \tag{15}
\]
The endpoint cost is uniform in every filling coefficient.
The surrounding norms remain necessary: this theorem does not
compare (15) with a hyperbolic volume rate or provide a lower
bound for the retained sum.

## 5. Reproduction

Run the focused checker with:

    python3 experiments/check_arbitrary_twist_conditional_endpoints.py

It verifies the commutator, binomial induction, original finite
matrices and endpoint normalizations. Uniformity in all integer
powers follows from Lemma 1, not from a finite list of powers.

