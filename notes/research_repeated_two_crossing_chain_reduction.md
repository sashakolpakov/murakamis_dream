# Exact reduction of a chain of two-crossing tangles

A string of degree-two vertices with the same power \(2\) or \(-2\)
can be replaced by one vertex. This is a marked tangle identity and an
identity in the full original quantum algebra. It does not require a
new asymptotic estimate. At a free boundary the quantum product must
still be reduced to its canonical representative of degree less than
\(N\). Equal quotient elements have equal canonical representatives,
but that representative need not equal the unreduced ordinary product
away from the physical spectral roots.

The reduction is useful for the finite-exception problem because it
removes arbitrarily long connected strings of short nonzero powers.
It does not reduce an arbitrary rational word to a single twist.

## 1. The original crossing and turn

Use the original crossing \(R\), physical quarter-turn \(T\), and
ordered tangle product of the
[marked degree-two moves](research_marked_degree_two_tangle_moves.md).
At level \(N\), put \(D=N-1\), \(q=e^{\pi i/N}\), and

\[
 \kappa=q^{D^2/2},\qquad q^a=\exp(\pi ia/N).
\]

Let \(M\) be multiplication by \(R\) in the original Newton basis,
and \(J\) its reversal matrix. The full algebra is
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\); its repeated roots
retain first derivatives. The already proved finite identities are

\[
 J^2=I,\qquad
 JM^\sigma J=\kappa^\sigma M^{-\sigma}JM^{-\sigma},
 \qquad JM^\sigma e_0=M^{-\sigma}e_0,
 \quad \sigma\in\{1,-1\}.                                      \tag{1}
\]

The first crossing identity is proved in the
[degree-two source reduction](research_degree_two_short_reductions.md).
For the last identity, reversal of the first column gives
\(\kappa(-q)^{D-j}\), whereas the inverse crossing has first
column \(\kappa^{-1}(-q^{-1})^j\). They agree because
\(\kappa^2(-q)^D=1\). Conjugation gives the negative sign.

## 2. The complete operator identity

**Proposition 1.** For every integer \(k\ge0\), both signs
\(\sigma\), and every level,

\[
 (JM^{2\sigma})^k
   =\kappa^{\sigma k}M^{-\sigma}JM^{-\sigma k}JM^\sigma,
                                                                    \tag{2}
\]
and consequently
\[
 (JM^{2\sigma})^kJ
   =\kappa^{\sigma(k+1)}
       M^{-\sigma}JM^{-\sigma(k+1)}JM^{-\sigma}.             \tag{3}
\]

**Proof.** Put \(C=M^{-\sigma}J\). Equation (1) gives
\(CM^{-\sigma}C^{-1}=\kappa^{-\sigma}JM^{2\sigma}\).
Taking the \(k\)-th power proves (2). Multiplication on the right
by \(J\), followed by (1), proves (3). These are matrix identities
on the entire algebra, not merely its semisimple quotient. \(\square\)

Let \(H_{p,N}=T(R^p)\) denote the original terminal element. A
pendant chain of \(k\ge1\) vertices, all with power \(2\sigma\),
has boundary element
\(F_{k,\sigma,N}=(JM^{2\sigma})^ke_0\). Thus

\[
 F_{k,\sigma,N}
   =\kappa^{\sigma k}R^{-\sigma}H_{-\sigma(k+1),N}
                   \quad\text{in }\mathcal A_N.                 \tag{4}
\]

If it is attached to a remaining vertex of power \(n\), with any
other spectator \(A\in\mathcal A_N\), then

\[
 \phi_N(R^nF_{k,\sigma,N}A)
   =\kappa^{\sigma k}
      \phi_N(R^{n-\sigma}H_{-\sigma(k+1),N}A).             \tag{5}
\]

No condition on the spectator is imposed. In particular it can be
the exact source of a large attached subtree. All unit scalars in
(2)--(5) are retained.

## 3. The marked tangle identities

Quantum equality alone does not identify the knot complements.
Here that identification follows from the actual boundary maps.

Label the four endpoints as in the marked degree-two note. On the
double-covering torus of the pillowcase, the physical turn and a
stack of \(n\) bottom crossings have affine lifts

\[
 \widetilde T(x,y)=(-y,x+1/2),\qquad
 A_n(x,y)=(x+ny+n/2,y).                                    \tag{6}
\]

These are the supported crossing and rotation mapping classes proved
there. Equality of their affine maps modulo the integer lattice and
the deck involution therefore gives the boundary isotopy; extending
it over a collar gives the tangle isotopy with all attached marks
carried.

Write \(I=R^0\) for the through tangle. The three half-lattice
translations correspond to the proper rotations
\(\rho,K,\tau\), respectively:

| Translation | Rotation | Endpoint permutation |
|---|---|---|
| \((1/2,0)\) | \(\rho\) | \((01)(23)\) |
| \((0,1/2)\) | \(K\) | \((03)(12)\) |
| \((1/2,1/2)\) | \(\tau=T^2\) | \((02)(13)\) |

Each preserves \(I\) as a tangle. It must nevertheless be retained
on an arbitrary spectator tangle.

**Proposition 2.** For any tangle \(F\), put
\(B_\sigma(F)=T(R^{2\sigma}F)\). Then

\[
 B_\sigma^k(TF)
 \simeq
 R^{-\sigma}T\left(
 R^{-\sigma(k+1)}T\left(R^{-\sigma}\rho_k(F)\right)\right),
                                                               \tag{7}
\]
where the actual proper rotation is

\[
 \rho_k=
 \begin{cases}
 \tau,&k\equiv0\pmod4,\\
 \rho,&k\equiv1\pmod4,\\
 \mathrm{id},&k\equiv2\pmod4,\\
 K,&k\equiv3\pmod4.
 \end{cases}                                                   \tag{8}
\]

For the pendant chain there is the simpler identity

\[
                     B_\sigma^k(I)
                \simeq R^{-\sigma}T(R^{-\sigma(k+1)}).
                                                               \tag{9}
\]

**Proof.** First ignore translations and work in
\(\mathrm{PSL}_2(\mathbb Z)\), writing \(S\) for the linear part
of \(\widetilde T\) and \(A_n\) for the linear shear. Direct
multiplication gives

\[
 (SA_{2\sigma})^k
    =A_{-\sigma}SA_{-\sigma k}S^{-1}A_\sigma.
                                                               \tag{10}
\]

The factor \(SA_{2\sigma}\) is conjugate to \(A_{-\sigma}\),
which proves (10) for all \(k\). To recover the full boundary maps,
include the translations in (6). The relative affine map

\[
 \left(A_{-\sigma}\widetilde T A_{-\sigma(k+1)}
           \widetilde T A_{-\sigma}\right)^{-1}
       (\widetilde T A_{2\sigma})^k\widetilde T
                                                               \tag{11}
\]

has linear part \(I\) or \(-I\). After the deck involution, its
translation modulo the lattice is, for \(k=0,1,2,3\pmod4\),
respectively \((1/2,1/2),(1/2,0),(0,0),(0,1/2)\), for both
crossing signs. This proves (7)--(8).

This finite residue-class calculation proves the formula for all
integers, not just four sample words. To see this directly, the
linear part of \(\widetilde T A_{2\sigma}\) is
\(\sigma(I+N_\sigma)\) with \(N_\sigma^2=0\). Its \(k\)-th
power and its accumulated affine translation are consequently
polynomials in \(k\) and \(\sigma^k\). Substituting \(k=4r+j\)
in (11), the difference from the listed half-translation has integer
polynomial coordinates in \(r\). The exact verification below
performs this calculation symbolically.

For (9), compare \((\widetilde T A_{2\sigma})^k\) with
\(A_{-\sigma}\widetilde T A_{-\sigma(k+1)}\). By (10) their
relative linear map is \(A_\sigma S A_\sigma\), up to the deck
involution. The remaining difference is a half-lattice translation.
Both operations preserve the through tangle: the first is the word
\(R^\sigma T(R^\sigma)\simeq R^\sigma R^{-\sigma}=I\),
and the second is a proper half-turn of \(I\). Thus the two maps
give isotopic images of \(I\), proving (9).

All these isotopies are relative to the four outside endpoints.
On a general spectator the rotation in (8) is carried, not erased.
The ribbon of a completed knot is transported; redrawing with
blackboard ribbons can produce the unit framing factors seen in
(2)--(5). \(\square\)

## 4. What this settles, and what it does not

In an ordered circle tree, a pendant chain of \(k\) powers
\(2\sigma\) can be replaced by one terminal power
\(-\sigma(k+1)\), while the power at its parent decreases by
\(\sigma\). Collecting the new outside \(R^{-\sigma}\) with
the parent power uses the original twist-sliding isotopy. Every
intervening branch receives its specified proper rotation, exactly
as in the degree-two marked moves. The operation identifies the
filled knot complements and their zero-framed invariants.

The replacement terminal has magnitude at least two, so the existing
terminal theorem applies. Therefore any collection of disjoint
pendant chains of this form can be fixed first, and independently
sufficiently long fixed powers at the remaining circles give the
volume identity. More generally, the identity applies whenever the
resulting marked diagram satisfies any already proved volume theorem,
including the recursive degree theorem. This adds low-degree strings
of arbitrary finite length without requiring a new boundary expansion
for every length.

For example, the pendant pair \((2,2)\) becomes a terminal power
\(-3\) and a shift by \(-1\) at its parent. Thus its long-remainder
volume conclusion also has an exact tangle-reduction proof. The
earlier joint boundary theorem proves more: it gives a complex
asymptotic for the original chain's canonical boundary polynomial.
That stronger statement does not follow from (4) alone: estimating
the canonical representative of a product requires another argument.
The [boundary multiplication theorem](research_boundary_crossing_packet_preservation.md)
now supplies it for every same-sign chain by estimating the canonical
product \(R^{-\sigma}H_{-\sigma(k+1),N}\).

An internal string can likewise be shortened by (7), with both
neighboring powers decreased by \(\sigma\), central power
\(-\sigma(k+1)\), and the rotation (8) carried on its downstream
branch. This is an exact simplification, not by itself an asymptotic
theorem for the new central power.

For a single internal chain with independently long powers at all
remaining vertices, there is a further consequence when \(k\ge31\).
The new vertex has degree two and power magnitude \(k+1\ge32\), so
\[
2^2+(k+1)^2\ge\max\{1024,128\cdot2\}.
\]
It satisfies the proved
[internal-vertex criterion](research_high_degree_short_internal_vertex.md);
the shifts of the neighboring powers do not affect their eventual
length. Thus the volume theorem also applies to this fixed-chain
family. The case \(k=1\) is covered by the separate degree-two
power-two theorem. Lengths \(2\le k\le30\) do not follow from these
criteria. An internal replacement is not a terminal, so the terminal
theorem cannot be used for those lengths.

Mixed-sign strings and arbitrary powers of magnitude at least three
are not covered by this single parabolic-word reduction. Nor may
infinite fibers of a later zero merger be counted as finite exceptions.
The general finite-exception theorem remains open.

## 5. Reproduction

The companion script checks (2)--(5) against the original full
crossing matrices and verifies (11) symbolically for \(k=4r+j\),
both signs, and every residue class \(j\). It also checks the
through-tangle stabilizer used in (9).

```sh
python3 experiments/check_repeated_two_crossing_chain_reduction.py \
  --precision 120 \
  --output repro/results/research-repeated-two-crossing-chain-reduction.json
```

The finite matrix comparisons check normalizations. The operator
proof and symbolic integer-parameter calculation establish the
identities for all levels and lengths; the proof of the isotopy also
uses the supported boundary-map realization in the cited marked
tangle note.
