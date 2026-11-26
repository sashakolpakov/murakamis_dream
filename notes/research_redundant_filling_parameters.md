# Redundant filling parameters and finite exceptional sets

Research note, 2 November 2026. The question in this note concerns
exceptions among the **original integer filling assignments** for a
fixed tangle template. Passing to a smaller parameter space is useful,
but does not change the set in which exceptions are being counted.

## 1. Exact reductions and their fibers

Let \(D\subseteq\mathbb Z^d\) be the filling assignments under
consideration that produce hyperbolic knots. For \(x\in D\), write

\[
K_x\subset S^3,
\qquad
\mathcal V(x):\quad
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_x)|
=\operatorname{Vol}(S^3\setminus K_x).
\]

Here \(K_N\) denotes the original, zero-framed Kashaev invariant, with
the conventions used in the manuscript. Let \(D'\) be a reduced
parameter set and let \(\pi:D\to D'\) be an exact reduction: the knot
and its framing are identified with the reduced knot, so that

\[
\mathcal V(x)\quad\Longleftrightarrow\quad
\mathcal V'(\pi(x)).
\]

Suppose a finite set \(E'\subset D'\) contains every reduced assignment
for which the volume identity has not yet been proved.

**Lemma.** Every unresolved original assignment belongs to

\[
\pi^{-1}(E')=\bigcup_{e\in E'}\pi^{-1}(e).
\]

Consequently, the unresolved original assignments form a finite set if
every fiber \(\pi^{-1}(e)\), for \(e\in E'\), is finite. If an unresolved
point \(e\in E'\) has an infinite fiber, this argument does not establish
the finite-exception conclusion. One must prove the volume identity for
that reduced point, or otherwise settle its whole fiber.

**Proof.** Outside \(\pi^{-1}(E')\), the reduced identity is known and
the exact reduction transports it back to the original knot. A finite
union of finite fibers is finite. Conversely, if the volume identity
failed at a reduced point with an infinite fiber, it would fail at
every point of that fiber. Even when no failure is known, leaving that
point unresolved leaves infinitely many original assignments
unresolved. \(\square\)

Thus the reduction need not be finite-to-one everywhere. The precise
requirement is to settle every reduced point whose fiber is infinite
before leaving a finite collection of unresolved points downstairs.

## 2. Why removing redundant parameters does not settle the question

A redundant filling parameter often leaves every integer in a fixed
parity class available without changing the knot. Its fiber is then
infinite. The same issue occurs with a reduction such as

\[
\pi:\mathbb Z^2\longrightarrow\mathbb Z,
\qquad
\pi(a,b)=a+b:
\qquad
\pi^{-1}(c)=\{(a,c-a):a\in\mathbb Z\}.
\]

Such reductions simplify the topology and the formulas. They do not
turn an unknown reduced knot into finitely many unknown original
assignments.

The closure identities in
[the Conway reductions paper](../papers/conway-reductions/closures.tex)
give an example within the strict Conway class. Write \(h(y)\) for an
integral twist tangle, \(T\) for the prescribed quarter-turn, and \(C\)
for cylindrical closure. Given a strict completed expression \(E\), the
padding construction has the exact knot identity

\[
C\bigl(h(0)[T(E)T(h(y))]\bigr)\simeq C(E)
\]

for every allowed integer \(y\). The zero-twist closure becomes a cap
closure; that closure separates the two factors, and the cap closure
of an integral braid is an unknot. The fixed half-turn in the closure
convention preserves the remaining closed knot.

The resulting family therefore contains infinitely many assignments
representing the same core \(C(E)\). A theorem with finitely many
exceptions for the reduced family is insufficient on this branch:
the particular core \(C(E)\) must satisfy the volume identity.

Arbitrary hyperbolic strict Conway cores can be padded this way.
Consequently, a theorem asserting finitely many exceptional
**assignments for every strict template** would imply the full volume
identity for every hyperbolic knot in the strict Conway class, at
arbitrary integer twist powers. The reverse implication is immediate.
This is a logical equivalence, not a counterexample to the proposed
theorem. It explains why a proof cannot leave exceptional collapsed
cores untreated.

## 3. A sufficient hypothesis for induction after partial filling

The following describes additional results that would make a reduction
and induction argument work. These results are requirements of the
strategy, not theorems currently proved in the repository.

For each partial-filling problem reached from a fixed input template,
assume there is a finite, marked decomposition into branches of the
following three kinds:

1. The branch has no hyperbolic final knot.
2. The branch has a hyperbolic parent exterior and an identified
   original open quantum source for which the complete long-filling
   theorem has been proved. In particular, the theorem applies when
   all remaining filling coefficients have sufficiently large
   absolute values, independently of their signs and relative sizes.
3. Exact knot and source identities reduce the branch to data of lower
   complexity. Every unresolved reduced case with an infinite fiber
   in the original parameter space must be proved separately; only
   finite fibers may remain exceptional.

Each record must retain its accumulated map from the original
assignments. This matters after more than one reduction: a parameter
discarded near the start can still make the fiber of a later terminal
case infinite.

For a branch of the second kind, the assignments outside the proved
long-filling region lie in finitely many subfamilies obtained by
fixing one remaining coefficient at a bounded integer value. Each
subfamily is a new partial-filling problem. The required classification
and source estimates must apply to these successors as well. The
hyperbolicity of the parent alone supplies neither the next source
formula nor its asymptotic estimates.

Assume that every operation strictly decreases a lexicographically
ordered pair of nonnegative integers: a reduction complexity followed
by the number of free effective filling coordinates. Together with
finite branching, this rules out an infinite path and gives a finite
reduction tree. Merely having finitely many structural descriptions is
insufficient if the procedure can cycle or repeatedly introduce new
free parameters.

At every unresolved terminal record, require that its fiber in the
original assignment space be finite. This includes a fully specified
filling reached through a succession of hyperbolic parents. Terminal
records whose volume identity is proved, and records with no
hyperbolic descendants, contribute no exceptions. The lemma then
shows that the union of all remaining exceptional assignments is
finite.

## 4. The induction input needed for a collapsed core

A nonhyperbolic partially filled exterior can simplify to a closed
hyperbolic knot complement while leaving a free nugatory filling
parameter. In that case, the required induction input is the volume
identity for that particular core. A statement allowing finitely many
exceptions for a smaller family leaves open the possibility that the
core is one of those exceptions. Its infinite fiber would then remain
unresolved in the original family.

The strategy can therefore reduce the analysis to hyperbolic short
parents and already solved collapsed cores only after the finite
reduction theorem and the relevant core proofs have been supplied.
The exact zero- and one-crossing identities provide useful reductions.
They do not classify every nonhyperbolic partial parent or prove the
volume identity for every hyperbolic core produced by those
reductions.

For this reason, a proof should maintain two lists: open parent
exteriors with the boundary estimates needed for further filling, and
closed knots for which the volume identity is proved. An infinite
fiber terminating at a closed core is settled by the second list.
Quotienting redundant parameters is useful bookkeeping, but does not
replace that proof.
