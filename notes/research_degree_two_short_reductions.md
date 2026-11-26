# Exact source reductions at a vertex of degree two

Research note, 2 November 2026. A vertex with two neighbors can be
summed exactly when its crossing power is \(0\), \(1\), or
\(-1\). The identities below hold in the full finite pair
algebra, including the first normal derivatives at repeated spectral
roots. They simplify the source before any asymptotic estimate.
Their use to identify two marked knot complements additionally
requires the corresponding tangle or surgery move; that topological
identification is not proved here.

## 1. The algebra and the two-boundary polynomial

Fix a quantum level \(N\geq2\), and write

\[
D=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,
\qquad \kappa=q^{D^2/2},
\qquad S_k=\prod_{r=1}^k2\sin\frac{\pi r}{N},\quad S_0=1.
\]

All fractional powers of \(q\) use this exponential convention.
Let

\[
\mathcal A_N=\mathbb C[z]/(P_N(z)),
\qquad P_N(z)=2T_N(z/2)+2,
\]

where \(T_N\) is the usual Chebyshev polynomial. Its normalized
Newton basis is

\[
e_k(z)=S_k^{-2}\prod_{r=0}^{k-1}(c_r-z),
\qquad c_r=2\cos\frac{(2r+1)\pi}{N}.
\]

The original closing functional and crossing satisfy

\[
\phi(e_i e_j)=\delta_{i+j,D},
\qquad R=\kappa\sum_{k=0}^D(-q)^k e_k.
\tag{1}
\]

These are the conventions of the
[finite Newton calculus](../papers/newton-calculus/finite.tex).
Multiplication by \(R\) has matrix

\[
M_{ij}=
\begin{cases}
\displaystyle\kappa(-1)^i q^{i(j+1)}
             \frac{S_i}{S_jS_{i-j}},&i\geq j,\\
0,&i<j.
\end{cases}
\tag{2}
\]

The inverse is its coefficientwise complex conjugate. Let \(J\)
be the reversal matrix, \(J_{ij}=\delta_{i+j,D}\). In particular,
\(\phi(AB)=a^T Jb\) when \(a,b\) are the Newton coefficient
columns of \(A,B\). Multiplication is self-adjoint for this
bilinear form:

\[
M^T J=JM.
\tag{3}
\]

The edge element and the result of summing a degree-two vertex are

\[
\mathcal K=\sum_{i=0}^D e_i\otimes e_i,
\qquad
\mathcal J_n=
\sum_{i,j=0}^D\phi(R^n e_i e_j)e_i\otimes e_j
\quad\text{in }\mathcal A_N\otimes\mathcal A_N.
\tag{4}
\]

The coefficient matrix of \(\mathcal J_n\) is \(JM^n\).

**Proposition 1.** For every integer level \(N\geq2\),

\[
\mathcal J_0=\sum_{i=0}^D e_i\otimes e_{D-i},
\tag{5}
\]

\[
\mathcal J_{\sigma}
=\kappa^{\sigma}
 (R^{-\sigma}\otimes R^{-\sigma})\mathcal K,
\qquad \sigma\in\{1,-1\}.
\tag{6}
\]

The scalar \(\kappa^{\sigma}\) in (6) has modulus one and is
part of the exact identity. It is not suppressed.

## 2. An elementary finite summation

The required summation is a specialization of the standard
[second \(q\)-Chu–Vandermonde identity](https://dlmf.nist.gov/17.6.E3).
Here is a finite proof, followed by the check that specialization
at a root of unity is regular.

For a formal variable \(Q\), write

\[
{a\brack b}_Q
=\frac{(Q;Q)_a}{(Q;Q)_b(Q;Q)_{a-b}},
\qquad (z;Q)_r=\prod_{s=0}^{r-1}(1-zQ^s).
\]

The Gaussian coefficient is a polynomial in \(Q\), with value
zero when \(b>a\). For nonnegative integers \(i,j\),

\[
\sum_{k=0}^i
 (-1)^kQ^{k(k-1)/2+k(1-i)}
 {i\brack k}_Q{j+k\brack k}_Q
=(-1)^iQ^{i(i+1)/2}{j\brack i}_Q.
\tag{7}
\]

To prove it, put
\(a_{i,k}=(-1)^kQ^{k(k-1)/2+k(1-i)}{i\brack k}_Q\)
and define the rational function

\[
F_i(z)=\sum_{k=0}^i\frac{a_{i,k}}{(z;Q)_{k+1}}.
\]

The recurrence
\({i\brack k}_Q={i-1\brack k}_Q+
Q^{i-k}{i-1\brack k-1}_Q\) gives

\[
\begin{aligned}
F_i(z)
&=\sum_{k=0}^{i-1}Q^{-k}a_{i-1,k}
 \left(\frac1{(z;Q)_{k+1}}-
       \frac1{(z;Q)_{k+2}}\right)\\
&=-\frac{zQ}{1-z}F_{i-1}(Qz).
\end{aligned}
\]

Starting with \(F_0(z)=1/(1-z)\), induction yields

\[
F_i(z)=\frac{(-1)^iQ^{i(i+1)/2}z^i}{(z;Q)_{i+1}}.
\]

Finally, the elementary generating function

\[
\frac1{(z;Q)_{k+1}}
=\sum_{j\geq0}{j+k\brack k}_Qz^j
\]

follows by induction from the same Gaussian-binomial recurrence.
Taking its coefficient of \(z^j\) proves (7).

In the application, \(0\leq i,j<N\). Every displayed denominator
\((Q;Q)_k\) used to specialize (7) has \(k<N\), so it is
nonzero at \(Q=e^{2\pi i/N}\). If \(j+k\geq N\), the
polynomial \({j+k\brack k}_Q\) vanishes at that root: its
numerator \((Q^{j+1};Q)_k\) contains \(1-Q^N\), while its
denominator does not. Thus one can either sum to
\(\min(i,D-j)\) or retain the zero terms up to \(i\).
There is no division by a zero quantum factorial.

## 3. The exact matrix identity

We prove

\[
JMJ=\kappa M^{-1}JM^{-1}.
\tag{8}
\]

Using (2), its conjugate, and
\(S_{D-k}S_k=N\), the right side has entry

\[
\begin{aligned}
(\kappa M^{-1}JM^{-1})_{ij}
={}&\kappa^{-1}(-1)^{i+D}q^{-i-D(j+1)}\\
&\quad\times\sum_{k=0}^{\min(i,D-j)}
 (-1)^k q^{k(j+1-i)}
 \frac{S_iS_{k+j}}{S_k^2S_{i-k}S_j}.
\end{aligned}
\tag{9}
\]

The conversion

\[
\frac{S_a}{S_bS_{a-b}}=q^{-b(a-b)}{a\brack b}_Q
\]

turns the sum in (9) into the left side of (7). Therefore it
vanishes for \(i>j\), while for \(i\leq j\) it equals

\[
(-1)^i q^{i(j+1)}\frac{S_j}{S_iS_{j-i}}.
\tag{10}
\]

Substituting into (9) gives

\[
\kappa^{-1}(-1)^Dq^{ij-D(j+1)}
              \frac{S_j}{S_iS_{j-i}}
=\kappa q^{ij-Dj}\frac{S_j}{S_iS_{j-i}}.
\]

The equality uses
\(\kappa^2=q^{D^2}=(-1)^Dq^{-D}\).
The final expression is exactly
\(M_{D-i,D-j}=(JMJ)_{ij}\), by (2) and \(q^N=-1\).
This proves (8) at every level.

Multiplying (8) on the right by \(J\), and using (3) for
\(M^{-1}\), gives

\[
JM=\kappa M^{-1}(M^{-1})^T.
\tag{11}
\]

Multiplication of the two variables of \(\mathcal K\) by
\(R^{-1}\) transforms its coefficient matrix from the identity
to \(M^{-1}(M^{-1})^T\). Thus (11) proves (6) for
\(\sigma=1\). Complex conjugation proves it for
\(\sigma=-1\). Equation (5) follows immediately from (1).

## 4. What these identities permit in a full finite source

Suppose a degree-two vertex with neighbors \(v,w\) occurs in
the original circle-tree contraction. Its only dependence on these
two boundary algebras is \(\mathcal J_n\).

For \(n=\sigma=\pm1\), equation (6) removes that vertex and
replaces its two edges by one edge between \(v,w\). It multiplies
the remaining local factors by \(R^{-\sigma}\) at each neighbor
and contributes the scalar \(\kappa^{\sigma}\). In particular,
neighboring crossing powers \(n_v,n_w\) become

\[
n_v-\sigma,\qquad n_w-\sigma.
\tag{12}
\]

This is an exact identity in the full remaining contraction, even
when arbitrary additional boundary factors are attached at either
neighbor. The reduction may therefore be repeated at the algebraic
source level.

For \(n=0\), the tensor in (5) is the inverse of the pairing
matrix \(J\). It satisfies

\[
(\phi\otimes\phi)
\left[(A\otimes B)\mathcal J_0\right]=\phi(AB)
\qquad(A,B\in\mathcal A_N).
\tag{13}
\]

For example, if
\(A=\sum a_i e_i\), \(B=\sum b_j e_j\), the left side is
\(\sum_i a_{D-i}b_i=a^TJb\), which is the right side.
Thus after summing the two neighboring vertices, their local
factors can be merged into one algebra factor. Crossing powers
add, and all their other incident boundary factors remain. No
extra scalar occurs in (13).

Equations (6) and (13) are equalities in quotient algebras, not
pointwise identities between unreduced angular polynomials at
arbitrary real or complex angles. They preserve the values and
first normal derivatives at every double spectral root, and hence
every subsequent original trace. An unreduced product on the right
of (6) can have higher polynomial degree than the representative
on its left. It must not be substituted into a global pointwise
bound as if those representatives agreed everywhere.

## 5. The geometric question kept separate

The exact source reduction proves equality of the corresponding
closed finite contractions, up to the displayed unit scalar. It
does not by itself prove that the original and reduced diagrams
have homeomorphic complements, or identify their preferred
meridians and longitudes.

To transfer a volume theorem from a reduced marked diagram to the
original one, one must also establish the actual tangle isotopy or
primitive surgery move, including the changed neighboring carriers
and framing. Alternatively, one can compare the original marked
geometric actions directly. These are additional geometric tasks.
The algebraic equality does not replace them.

The subsequent
[marked tangle-move proof](research_marked_degree_two_tangle_moves.md)
supplies that topological comparison, with a physical half-turn
retained on the appropriate attached branch. It proves a
long-remainder volume theorem when an original degree-two power
is \(1\) or \(-1\). Its zero-power move merges neighboring
powers by their sum and retains the associated many-to-one
parameter issue. Neither conclusion follows from erasing that
half-turn in the present algebra.

The geometric branch for a degree-two zero filling degenerates at
unit charge, whereas the positive branch exists at powers
\(\pm1\); see
[the internal-vertex geometry note](research_isolated_internal_vertex_geometry.md).
The exact identities above explain why those exceptional small
sources can be treated algebraically without assuming that the
ordinary factorial bulk chart remains valid.

## 6. Reproduction

Run

```sh
python3 experiments/audit_degree_two_short_reductions.py
```

The script constructs (2) in the exact cyclotomic field generated
by \(e^{\pi i/(2N)}\). It checks the inverse, the reversal
identity (8), and the two-boundary identity (11), at every entry
for levels in its selected range. These checks verify exact
coefficients in the full algebra. The proof above establishes the
identity for all levels, rather than extrapolating from the finite
checks.
