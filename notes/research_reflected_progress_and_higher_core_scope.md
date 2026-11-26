# Reflected closures and the remaining connected-core obligation

Research scope note, 3 November 2026. The target still counts original
integer assignments of every fixed admissible template, restricted to
those giving hyperbolic knots. The manuscripts remain frozen.

The [reflected theorem](research_reflected_even_kashaev_volume_theorem.md)
proves the original volume identity for the closed pairs
\((-2k,2k)\), \(k\ge2\), and their mirrors, through all integer
levels. In particular it resolves every original four-path assignment
\((m,0,-2k-m,2k)\). These are actual infinite parameter fibers, not
exceptions identified by knot type. The
[fixed insertion theorem](research_even_reflected_casimir_insertions.md)
additionally retains arbitrary fixed Casimir polynomials at the two
boxes.

Neither result estimates the pair with another unfilled boundary.
A complete edge coupon has degree depending on the level and an
exponential phase; it is not a fixed polynomial insertion. In the
attached pair the original degrees become \((1,2)\), so the internal
primitive equation also gains the return of its extra edge.
The closed stationary action cannot simply be reused.

## 1. What complete two-circle coverage would and would not imply

The existing [two-circle theorem](research_two_circle_finite_exceptions.md)
already leaves only finitely many original pairs untreated. Proving
the remaining hyperbolic pairs would remove all exceptions in that
family. Every assignment carried to such a pair by an exact marked
reduction would then be covered, even if the reduction has infinite
fibers. In particular this would settle the entire four-path stratum
\[
 K_4(a,0,b,c)\simeq C(R^{a+b}T(R^c))
\]
whenever its closure is hyperbolic. Fixed unit reductions and further
zero padding give other precisely reducible strata. Their rotations,
carriers and framing factors still have to be transported.

There is no exact reduction of every rational chain to this family.
The following elementary obstruction persists even after closing,
so it is stronger than failure of a particular marked collar form.

**Proposition 1.** For every integer \(a\ge2\), the rational knot
\[
       K_3(a,-3,-3)=C\bigl(R^aT(R^{-3}T(R^{-3}))\bigr)
       \tag{1}
\]
is not isotopic to any two-circle closure \(C(R^uT(R^v))\),
even if mirrors are allowed.

**Proof.** Use the original fraction convention: \(R^n\) adds \(n\),
\(T\) sends a fraction to its negative reciprocal, and the through
tangle has fraction zero. These conventions, including the
cylindrical closing frame, are fixed in the
[marked rational-corridor calculation](research_rational_corridor_compression.md).
The fraction in (1) is
\[
                  a+\frac38=\frac{8a+3}{8}.
                  \tag{2}
\]
Put \(p=8a+3\ge19\). It is odd, so the closure has one component.
The numerator of a two-circle fraction is \(uv-1\), and its
denominator is \(v\), with no common factor. Equality of the
two-bridge knots forces \(|uv-1|=p\). Allowing a mirror and both
Schubert denominator equivalences, the denominator of (1) has class
\[
              \{\pm8,\ \pm8^{-1}\}\pmod p
                  =\{\pm8,\ \pm(3a+1)\}\pmod p,
                  \tag{3}
\]
because \(8(3a+1)=3p-1\).
We use precisely Schubert's classification as proved in
[Kauffman--Lambropoulou, Theorem 2](https://arxiv.org/html/math/0212011#S1).

Neither numerator nor denominator class here is that of the unknot
or an integral two-strand closure. Thus a candidate two-circle
presentation cannot have \(u\) or \(v\) in \(\{0,\pm1\}\);
equivalently this follows directly from the original cap and unit
reductions. Hence \(|u|,|v|\ge2\), and
\[
 |uv|\in\{p-1,p+1\},\qquad
             2\le |v|\le\frac{p+1}{2}.
             \tag{4}
\]
The only magnitudes in the range (4) representing (3) are
\(8\) and \(3a+1\): their complementary representatives exceed
\((p+1)/2\). But \(8\) divides neither \(p-1=8a+2\) nor
\(p+1=8a+4\), and
\[
                 2<\frac{8a+2}{3a+1}
                    <\frac{8a+4}{3a+1}<3
                    \qquad(a\ge2).
                    \tag{5}
\]
Thus \(3a+1\) divides neither number either, contradicting (4).
\(\square\)

This proposition is a topological nonreduction statement. Any
application to the volume target retains the condition that the
displayed knot is hyperbolic; no hyperbolicity theorem is imported
here. For example \(a=2\) gives denominator classes
\(\{7,8,11,12\}\) modulo \(19\), none obtainable from the factors
of \(18\) or \(20\).

The corresponding prepared pendant source is
\(T(R^{-3}T(R^{-3}))\), of fraction \(3/8\). It fails the
one-terminal compression test \(p\equiv\pm1\pmod q\).
Its two-boundary extension has matrix with diagonal entries \(3,3\)
and lower-left entry \(8\), so also fails the one-vertex corridor
test. Its original selected degrees are \((1,2)\), rather than
the degrees \((1,1)\) of a closed two-circle pair.
This is a concrete minimal outstanding boundary problem.

The general definite normal form preserves arbitrary attachments
but leaves an arbitrarily long chain of magnitudes at least two.
The two complementary uniform-sign forms do not eliminate that
chain. Nor can a filled primitive core be used as an unchanged
ideal-pants cuff: its holonomy is loxodromic. The exact qualifications
are recorded in Sections 5--6 of the corridor calculation. A scalar
closed theorem therefore does not replace these open tensors.

## 2. The exact counted-set gain from a future component theorem

Here is a logical implication, not an established analytic
hypothesis. It generalizes the existing independent-set deduction.

Let \(G=(V,E)\) be a finite connected graph, \(d=|V|\), and
\(1\le s<d\). Fix allowed integer values at each vertex and a
domain \(\mathcal D\) of complete assignments. Suppose that for
every proper partial assignment \((I,\mathbf a)\) whose induced
components in \(G[I]\) have at most \(s\) vertices, there is a
finite threshold \(B(I,\mathbf a)\) such that the desired property
holds whenever those coordinates are fixed and every remaining
coordinate has magnitude greater than \(B(I,\mathbf a)\).
The hypothesis includes simultaneous assembly of all those
components; individual component statements alone are not enough.

**Proposition 2.** Under this hypothesis, the untreated set in
\(\mathcal D\) is contained in finitely many slices fixing the
values of \(s+1\) vertices spanning a connected subgraph. In a box
of radius \(H\), it has cardinality \(O(H^{d-s-1})\).

**Proof.** Begin with the empty partial assignment. At an eligible
node, an untreated completion must have a free coordinate of
magnitude at most the node's threshold. Branch over the finitely
many choices of that coordinate and its value. Continue if every
new induced component has at most \(s\) vertices. Otherwise choose
a connected set of exactly \(s+1\) vertices inside a component
that exceeds \(s\), record their already fixed values, and stop
the branch. Such a connected set exists by growing a tree inside
that component.

The tree of choices has depth at most \(d\) and finite branching.
Since \(G\) is connected and \(d>s\), a branch cannot reach all
coordinates while its components still have size at most \(s\).
Every untreated assignment therefore reaches one of finitely many
recorded slices. Each slice fixes \(s+1\) original coordinates
and contains at most \((2H+1)^{d-s-1}\) points in the box.
For fixed carriers \(n_v=\eta_v-2p_v\), fixing a power fixes exactly
one original surgery coefficient, so the same count holds in
surgery coordinates. \(\square\)

The proved isolated-vertex assembly is the case \(s=1\), on its
domain \(d_v+|n_v|>2\). It yields the current
\(O(H^{d-2})\) bound. Joint boundary coverage and assembly for
every adjacent pair would give \(s=2\), hence \(O(H^{d-3})\);
in particular it would give cofiniteness for three-vertex paths
on that domain. Closed two-circle coverage does not establish
this premise. Larger templates still require larger connected
components or a theorem stable under their actual composition.

Degenerate reductions remain a separate obligation. The
[strict-padding argument](research_finite_exceptions_under_partial_fillings.md#8-a-consequence-of-counting-assignments-strict-padding)
shows why a fixed unresolved higher core cannot be left behind
when infinitely many original assignments collapse to it.
The goal has not been weakened to a statement about knot types.

## 3. Primary coverage and the next source theorem

Jun Murakami's
[double-twist preprint, version 3](https://arxiv.org/html/2501.00225v3)
states coverage of all hyperbolic double-twist knots in its
introduction and Theorem 1, with the small parameter cases referred
to earlier work in Section 3.5. The supplied version also explicitly
assumes odd levels \(N\ge3\) at the start of Section 1. This scope
check does not audit its proof or infer an extension to even levels.
Our reflected argument independently keeps all integer levels.
No novelty claim follows from this comparison.

The most direct reusable next step is a full boundary theorem for
an actual adjacent short pair, then prepared-word stability beyond
it. The attached reflected pair is a natural test of the new source
concentration machinery; the pair \((-3,-3)\) is a minimal
uniform-sign test with known positive geometric structure.
Both require a nonzero original contribution, all repeated-root
normals, a fixed holomorphic boundary domain and control of the
whole boundary period. Fixed Casimir moments alone provide none
of the needed estimates for level-dependent coupons.

For arbitrary rational words, the
[exact two-color forced system](research_rational_word_local_source_system.md)
retains the genuine turns, forcing and full boundary vector.
Its middle-cut rank obstruction excludes an exact fixed-memory
causal replacement for arbitrary input. It still permits estimates
for prepared word states. Proving such estimates while retaining
coherent sums is a route to the required boundary theorem;
another central characteristic identity or a closed positive norm
does not supply it by itself. Branching Conway pieces would then
still require their own multiboundary assembly.
