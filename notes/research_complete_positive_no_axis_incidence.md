# Complete positive triangulations have no shape-axis tetrahedra

Private research note, 17 November 2026.

Complete cusp holonomy supplies globally defined squared determinant
coordinates on the unoriented edges. They rule out equality of any two
opposite-pair edge-label multisets in a positive tetrahedron. Consequently
the zero-block character bootstrap cannot start at any level \(N\ge3\).
This is a limitation of that test, not vanishing of the original pointed
projection. A local rank-one tetrahedron, if present, is necessarily
mixed and regular.

## 1. Geometric setting and incidence

Let \(M\) be an oriented complete finite-volume hyperbolic three-manifold
with torus cusps, equipped with a finite geometric ideal triangulation.
Every tetrahedron has its geometric orientation and strictly positive
dihedral angles. The developing map and complete holonomy are fixed.
Local edges and vertices may have repeated global labels. No assumption
of a global branching or of a lift of the holonomy to
\(\mathrm{SL}_2(\mathbb C)\) is made.

For one ordered tetrahedron write
\[
 A=\{[01],[23]\},\qquad B=\{[02],[13]\},\qquad
 C=\{[03],[12]\},
 \tag{1}
\]
as multisets of global unoriented edge labels. Denote their multiplicity
vectors by \(a,b,c\). For a global edge \(e\), the source's local edge
row is
\[
 \beta(e)_t=\epsilon_t(a_e-c_e,b_e-c_e).
 \tag{2}
\]
Its shape-axis cases are \(A=C\), \(B=C\), or \(A=B\). Equivalently,
the whole local image of the edge lattice lies respectively on one of
the three lines with first coordinate zero, second coordinate zero,
or equal coordinates. Equation (2) uses the original shape axes.

**Theorem 1.** In this complete positive setting, the three multisets
in (1) are pairwise different. This holds for any number of complete
cusps.

## 2. Squared determinants and the proof

The group \(\mathrm{PSL}_2(\mathbb C)\) acts on
\[
 \mathcal V=(\mathbb C^2\setminus\{0\})/\{\pm1\}.
 \tag{3}
\]
Indeed the two determinant-one lifts of a projective transformation
differ by sign and therefore induce the same action on (3).

For each cusp choose a lift of its ideal vertex. Its peripheral
stabilizer is conjugate to a group of translations
\(z\mapsto z+b\). The matrices
\[
 \begin{pmatrix}1&b\\0&1\end{pmatrix}
 \tag{4}
\]
fix \((1,0)\), and their negatives fix its class in (3). Conjugating
back gives a nonzero vector class fixed by the entire stabilizer.
Choose one such class at each cusp and extend by the holonomy action
to all lifted ideal vertices. This is well-defined: two deck elements
giving the same lifted cusp vertex differ by its stabilizer, which
fixes the chosen vector class. The resulting decoration is equivariant.

If a lifted edge has decorated endpoints \(v_i,v_j\), set
\[
 d_e=\det(v_i,v_j)^2.
 \tag{5}
\]
Changing representatives by signs, reversing the edge, or applying
any deck transformation leaves (5) unchanged. In the last case either
determinant-one lift preserves the determinant before squaring.
Thus \(d_e\) is a single complex number attached to the global
unoriented edge. It is nonzero because an incident positive geometric
tetrahedron has distinct developed ideal vertices.

Use the cross-ratio convention
\[
 z=\frac{\det(v_0,v_2)\det(v_1,v_3)}
          {\det(v_0,v_3)\det(v_1,v_2)},\qquad
 z'=\frac1{1-z},\qquad z''=\frac{z-1}{z}.
 \tag{6}
\]
It is the convention \(r(\infty,0,1,z)=z\) of the crossing source.
Put
\[
 D_A=d_{[01]}d_{[23]},\quad
 D_B=d_{[02]}d_{[13]},\quad
 D_C=d_{[03]}d_{[12]}.
 \tag{7}
\]
Then
\[
 z^2=\frac{D_B}{D_C},\qquad
 (z')^2=\frac{D_C}{D_A},\qquad
 (z'')^2=\frac{D_A}{D_B}.
 \tag{8}
\]
For a direct sign check take
\[
 v_0=(1,0),\quad v_1=(0,1),\quad
 v_2=(1,1),\quad v_3=(z,1).
 \tag{9}
\]
The unsquared opposite-pair determinant products are \(1-z,-z,-1\);
this proves all three formulas in (8). Arbitrary changes of the four
vector scales multiply the three products by the same factor, so the
calculation proves (8) for the original decoration as well.

If two of the multisets \(A,B,C\) coincide, their products in (7)
coincide. One of the three shapes in (8) then has square one, so it is
real. All three shapes of a positively ordered ideal tetrahedron have
positive imaginary part. This contradiction proves Theorem 1.

Completeness is essential to this argument. For incomplete peripheral
holonomy, a cusp eigenvector can have eigenvalue different from
\(\pm1\). Its class in (3) then need not be fixed by the peripheral
stabilizer, and (5) need not descend to a global edge coordinate.
The theorem is not asserted for arbitrary positive incomplete shapes.

## 3. The remaining rank-one incidence is regular

Here rank refers to the rational rank of the full local edge image in
(2), not a modular rank or the restriction of a partially projected
state.

**Theorem 2.** If that local rank is one, then, after permuting the
three opposite pairs, there are two distinct global edges \(e,f\) with
\[
 A=\{e,e\},\qquad B=\{f,f\},\qquad C=\{e,f\}.
 \tag{10}
\]
The tetrahedron is regular, with all dihedral angles \(\pi/3\).
If the face-dual graph is connected and its number \(T\) of tetrahedra
exceeds two, the two-label sets of distinct rank-one tetrahedra are
disjoint. Under these same connectedness and \(T>2\) hypotheses,
at most \(\lfloor T/2\rfloor\) tetrahedra have local rank one, and at
least \(\lceil T/2\rceil\) have local rank two.

**Proof.** The multiplicity vectors \(a,b,c\) are distinct by Theorem 1,
are nonnegative integral vectors of coordinate sum two, and are
collinear by rank one. On their affine integer line write them as
\(v+k u\), with \(u\) primitive integral and three distinct integer
values of \(k\). The spread of these values is at least two. Some
coordinate of \(u\) is a nonzero integer; that coordinate can vary
by at most two in the simplex of coordinate sum two. Therefore the
spread is exactly two, and that coordinate changes from zero to two.
At the endpoint where it is two, all other coordinates vanish.
Since \(\sum u_i=0\), another coordinate changes in the opposite
direction and gives the other endpoint. The three vectors are
\(2\mathbf e_e,\mathbf e_e+\mathbf e_f,2\mathbf e_f\).
This proves (10). Rank zero would already force \(A=B=C\), so it
cannot occur.

Choose a cyclic positive shape ordering with the mixed pair as \(C\).
In (7), (10) gives
\[
 D_A=d_e^2,\qquad D_B=d_f^2,\qquad D_C=d_ed_f.
 \tag{11}
\]
Consequently \(z^2=(z')^2=d_f/d_e\), hence
\[
 [z(1-z)]^2=1.
 \tag{12}
\]
The choice \(z(1-z)=-1\) has only real roots, being
\(z^2-z-1=0\). The choice \(z(1-z)=1\) has upper-half-plane root
\(z=e^{i\pi/3}\). Thus positivity forces regularity.

Each of the two global edge labels in (10) occurs three times and
receives total angle \(\pi\) from this tetrahedron. If two distinct
rank-one tetrahedra share one label, their contributions exhaust the
\(2\pi\) angle around that edge. No other tetrahedron is incident to
it, because all its dihedral contributions would be positive.
Every face of either tetrahedron contains the shared label: a face
contains one local edge from each opposite pair and therefore includes
both labels in (10). Its paired face must consequently belong to one
of those two tetrahedra. They form a whole face-dual connected
component. Connectedness gives precisely two tetrahedra. This proves
the disjointness assertion.

Finally the number of global edges is \(T\). To verify the count,
truncate the \(c\) torus cusps to obtain a compact manifold
\(\overline M\). Doubling shows \(\chi(\overline M)=0\), since its
boundary and its closed oriented three-dimensional double both have
Euler characteristic zero. Coning each boundary torus raises Euler
characteristic by one, so the ideal-vertex compactification has
\(\chi=c\). Its cell count is \(c-E+2T-T\), hence \(E=T\).
Each rank-one tetrahedron uses two global edge labels disjoint from
those of every other rank-one tetrahedron. If there are \(m\) such
tetrahedra, \(2m\le E=T\). Rank zero is excluded, so the remaining
tetrahedra have rank two. \(\square\)

## 4. Consequence for the exact character bootstrap

Use the original pointed tensor, commuting edge operators, and
primitive integral edge lattice \(E\) wherever the bootstrap source
applies, in particular for an \(S^3\) link exterior. Let \(Q\) be a
primitive \(N\)-th root, \(G=\operatorname{Hom}(E,\mathbb Z/N)\), and
let \(\alpha_t,\beta_t\in G\) be the exact shifts of \(X_t,Y_t\).
The original source convention gives, on every genuine edge row \(e\),
\[
 \alpha_t(e)=c_e-b_e,\qquad
 \beta_t(e)=c_e-a_e,\qquad
 (\alpha_t-\beta_t)(e)=a_e-b_e\pmod N.
 \tag{13}
\]
Weyl scalar units and the specified compatible edge characters do
not change these commutators.

Starting at \(H_0=0\), the exact zero-block bootstrap can enlarge
the invariant subgroup only when one of
\[
 \alpha_t\in H,\qquad \beta_t\in H,\qquad
 \alpha_t-\beta_t\in H
 \tag{14}
\]
holds. At \(H=0\), each condition in (14) says that two opposite-pair
multisets have equal multiplicities modulo \(N\). Actual edge rows
generate \(E\), so (13) tests the entire character.
Every multiplicity difference lies in \([-2,2]\). For \(N\ge3\),
vanishing modulo \(N\) is therefore ordinary integer vanishing.
Theorem 1 excludes all three possibilities at every tetrahedron.
Thus
\[
 H_\infty=0\qquad(N\ge3).
 \tag{15}
\]
For edge rank \(r\ge2\), this cannot contain the nontrivial kernel of
evaluation at a primitive genuine edge, so the bootstrap's
single-edge completion criterion cannot apply. For rank one that
kernel is already zero; the existing single-edge result is unaffected.
At \(N=2\) the parity coincidences in (13) remain possible, and (15)
is not asserted.

The same obstruction excludes a final fresh shape-axis factor in
an integral edge-basis elimination: if all earlier basis rows vanish
on that tetrahedron and the last row has shape-axis direction, the
whole local image lies on that axis, contrary to Theorem 1.
Every new complete positive geometric triangulation, including any
obtained by positive geometric moves, satisfies the same obstruction.
Changing the original local polarization is not covered by this
argument and would require an actual pointed source adapter.

These statements neither make a joint projected block zero nor prove
it nonzero. They give no regulator asymptotic, no norm lower bound,
and no identification of the candidate pointed tensor with the
original quantum invariant.

## 5. Sources and coverage

The direct algebraic sources, read completely and checked at the
following pins, are:

1. [Pointed tetrahedron modules and all-level edge reduction](pointed_tetrahedron_gluing.md),
   SHA256
   \(\texttt{ba91c4be463e38add42b2f8ebc53c3cd3a7e96e97ac4247330dc325e7f6b3a7c}\).
   This fixes (2), the shape axes, original pointed tensor, and exact
   edge operators.
2. [Joint pointed nonvanishing by character-subgroup propagation](research_joint_edge_character_bootstrap.md),
   SHA256
   \(\texttt{09f8f96a582e15488e8758c33ce4693da7937c438fde5e72b935262916c9e9ca}\).
   Its exact commutators and subgroup rule supply (13)--(15).

The cross-ratio convention agrees with equation (1.5) of
[The actual crossing sum and the complete Bloch fundamental class](crossing_fundamental_cycle.md),
SHA256
\(\texttt{0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f}\).
That complete text was also read; its global comparison theorem is not
a premise here. Equations (3)--(12) have self-contained proofs above.

Equivariant cusp decorations and determinant coordinates are standard;
see, for coverage, Goerner--Zickert,
[Triangulation Independent Ptolemy Varieties, Section 3.1 and Figure 2](https://math.umd.edu/~zickert/Triangulation%20independent%20Ptolemy%20varieties.pdf).
No proof from that paper is imported, and no novelty is claimed for
decoration or cross-ratio theory. No normal-surface realization theorem
or global \(\mathrm{SL}_2\) lifting theorem is used.
