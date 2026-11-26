# What the short-filling results imply about finite exceptions

Research scope note, updated 3 November 2026. The target continues to count
the original integer filling assignments. It has not been replaced by
a statement about distinct knot types, essential parameters, or density.
The manuscripts remain frozen.

The new boundary theorems allow many more partial fillings. They do
not yet prove that every fixed template has only finitely many
untreated assignments. There are two distinct issues already on
small paths: adjacent short vertices require a composition estimate
or a marked reduction to an already treated family,
and a zero vertex can give infinitely many assignments of the same
unresolved knot. The joint estimate is now proved for the pendant
pair of powers \(2,2\). An exact marked reduction now covers every
same-sign pendant chain of powers \(2\) or \(-2\), and boundary
multiplication gives its canonical boundary asymptotic. The mixed
pair \((2,-2)\) now also has a complete analytic boundary theorem
whose complete rate is the volume of the specified augmented
complement. Its original peripheral marking and geometric deformation
are now proved as well, giving the volume identity for every sufficiently
large fixed odd signed final twist in its literal closure.
Every isolated pair with \(d+|n|>2\) now has a complete boundary
theorem. The finite remainder of 6,369 pairs passed the common
interval certificate and a separate archive-coverage check.
Consequently arbitrary nonadjacent short fillings in that domain
can precede sufficiently long remaining fillings. Same-sign internal
\(2\)-crossing chains are also estimated at every fixed length.
The mixed pair and its mirror have now been proved eligible as
one-boundary pendant pieces in the hybrid tree theorem. Arbitrary
adjacent short assignments remain untreated.

## 1. Adjacent short vertices and the two-crossing reduction

Use the original crossing \(R\), physical quarter-turn \(T\), and
cylindrical closure \(C\). The three-vertex path has the expression

\[
 K_3(a,b,c)=C\bigl(R^aT(R^bT(R^c))\bigr).
 \tag{1}
\]

Fix \(a=b=2\), and let \(c\) vary through the odd integers. The
endpoint matching gives one component: an even integral braid has
the through pairing, an odd braid has the crossed pairing, and the
quarter-turn preserves the crossed pairing. Thus (1) has the crossed
pairing before cylindrical closure, which closes to one component.
As in the finite-exception target, restrict to assignments whose
resulting knot is hyperbolic. No assertion about hyperbolicity is
being inferred from the quantum expression below.

The fixed vertex \(a\) is an original leaf of power two. The fixed
vertex \(b\) has original degree two and power two. Each has its own
proved whole-boundary theorem. However, they are adjacent. If \(u\)
is the angle at the remaining vertex, their exact joint polynomial is

\[
 Z_N(u)=\mathcal D_{2,N}^{(t)}
          \bigl[H_{2,N}(t)K_N(t,u)\bigr],
 \qquad
 H_{2,N}(t)=\mathcal D_{2,N}^{(s)}K_N(s,t).
 \tag{2}
\]

Here \(K_N\) is the original complete edge polynomial and
\(\mathcal D_{n,N}f=\phi_N(R^nf)\) is the complete closing
functional, including its first derivatives at repeated roots.

Expression (2) is neither an original leaf polynomial nor the
degree-two singleton polynomial
\(\mathcal D_{2,N}[K_N(t,u)K_N(t,v)]\). Replacing the first
kernel by the already traced function \(H_{2,N}\) changes the
phase and its global estimates. The
[nonadjacent assembly](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_nonadjacent_short_fillings_and_long_remainder.md)
therefore does not apply. The
[connected-cluster criterion](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_connected_short_filling_clusters.md)
also does not apply: the selected original degrees are \(1,2\),
and both powers are \(2\).

The earlier [degree-two marked simplifications](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_marked_degree_two_tangle_moves.md)
concern powers \(0,\pm1\), so they do not remove this pair.
This is the smallest tree on which adjacent selected vertices can
leave an unfilled boundary. Separate singleton theorems alone do
not estimate (2).

A direct joint theorem for (2) is proved in
[the adjacent-pair boundary calculation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_adjacent_two_crossing_boundary_theorem.md).
It uses the exact double sum, its calibrated positive geometry,
the horizontal maximum, and a new full-period contour. The added
lattice terms outside the original triangle are exactly zero.
The lower first-variable contours consequently form complete circles;
their main integrals cancel after an explicit normalization, with
exponentially small errors. Combining the two vertical sides before
taking absolute values retains the peripheral multiplier and removes
the former diagonal-corner obstruction. The written endpoint bounds
and the interval certificate account for every remaining contour term.

There is now a second proof of the closed volume conclusion. The
[repeated-two-crossing reduction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_repeated_two_crossing_chain_reduction.md)
replaces the pendant pair by a terminal power \(-3\) and shifts its
parent power by \(-1\). The terminal theorem then applies when the
remaining power is sufficiently long. Thus a joint estimate of the
unreduced polynomial was not logically necessary for that closed
conclusion.

More generally, a pendant chain of \(k\) powers \(2\sigma\),
\(\sigma=\pm1\), becomes a terminal power \(-\sigma(k+1)\) and a
parent shift by \(-\sigma\), with the actual branch rotations
retained. The
[boundary multiplication theorem](research_boundary_crossing_packet_preservation.md)
also upgrades this quotient identity to a full asymptotic for the
canonical unreduced boundary polynomial. These arguments treat all
same-sign chains, but they do not validate an arbitrary iteration of
singleton theorems.

The mixed pair now has a separate
[complete analytic theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_two_crossing_boundary_theorem.md).
It estimates the original polynomial \(T(R^{-2}T(R^2))\) on a
fixed complex neighborhood, proves a nonzero leading coefficient,
and controls the whole boundary period. The proof accounts for all
terms in an exact contour identity; it does not infer this estimate
from the two singleton results. The
[positive ideal subdivision](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_two_crossing_positive_subdivision.md)
also proves its complete volume normalization, by exact gluing and
dilogarithm identities. The
[original word and collar proof](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_word_collar_representation.md)
now identifies the full marked geometric germ and proves the
volume theorem for its literal long odd final closure, of either
sign. The proof uses the exact original diagram meridian and
disk longitude, not just a comparison of complete cusp traces.
Other adjacent short powers still need a composition proof.

For comparison, neighboring zero-power vertices of original degrees
at least three are now covered by their
[joint Newton-coordinate theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_all_zero_subtree_newton_packet.md)
and [literal strict Conway geometry](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_zero_subtree_conway_geometry.md).
That proof treats the combined polynomial and applies to connected
sets of any size. The nonzero pair in (2) uses the separate
full-period argument just described.

## 2. An infinite fiber on a four-vertex path

For the four-vertex path, write

\[
 K_4(a,v,b,c)
   =C\bigl(R^aT(R^vT(R^bT(R^c)))\bigr).
 \tag{3}
\]

All powers refer to their original local crossing frames. Let
\(\tau=T^2\) be the actual physical half-turn. The
[ordered rotation and closure isotopies](../papers/conway-reductions/moves.tex)
give

\[
 \tau(FG)=\tau(G)\tau(F),\qquad
 \tau(TF)=T\tau(F),\qquad \tau(R^r)=R^r,
 \qquad C(FG)\simeq C(GF).
 \tag{4}
\]

In particular, the reversal of the product by \(\tau\) must be
retained. At \(v=0\), equations (3)--(4) give an ambient isotopy

\[
\begin{aligned}
 K_4(a,0,b,c)
  &=C\bigl(R^a\tau(R^bT(R^c))\bigr)\\
  &=C\bigl(R^aT(R^c)R^b\bigr)\\
  &\simeq C\bigl(R^{a+b}T(R^c)\bigr)
   =K_2(a+b,c).
\end{aligned}
 \tag{5}
\]

The first equality uses the through identity \(R^0\), before
applying the two turns. The last isotopy uses closed cyclicity and
then concatenation of integral braids. No open tangles have been
commuted, and no half-turn has been erased. These are the same
physical moves used in the
[marked degree-two zero reduction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_marked_degree_two_tangle_moves.md#4-a-zero-power-merges-two-twist-regions).

The isotopy carries the main knot, its marked arcs, orientations,
and any supplied ribbon. Consequently it identifies the filled knot
complements and their preferred meridian and longitude, after the
same orientation convention, and identifies the reduced zero-framed
Kashaev invariant. A raw diagram evaluation can retain a framing
factor of modulus one. Equation (5) is not a claimed homeomorphism
between exteriors having two unfilled auxiliary tori and an exterior
having only one: all the displayed powers are evaluated.

**Proposition.** Suppose the finite-assignment conclusion holds for
every fixed parity pattern of the four-vertex path (3). Then every
hyperbolic two-circle knot \(K_2(s,c)\), at every fixed pair of
integer powers \(s,c\), satisfies the original Kashaev volume
identity.

**Proof.** Fix such a hyperbolic knot and choose a parity
\(\epsilon\in\{0,1\}\). For every integer \(r\), take

\[
 (a,v,b,c)=(\epsilon+2r,\ 0,\ s-\epsilon-2r,\ c).
 \tag{6}
\]

This is one fixed parity pattern: the parities are
\(\epsilon,0,s-\epsilon,c\) modulo two. The carrier at the
zero vertex is \(0\). Choose the original other carriers with these
parities. Since \(n_j=\eta_j-2p_j\), every tuple (6) is an
allowed integer surgery assignment; as \(r\) increases by one,
the first surgery coefficient decreases by one and the third
increases by one. Thus the assignments are distinct.

Equation (5) identifies all of them with the same hyperbolic knot
\(K_2(s,c)\). In particular their fixed matching is a knot matching.
If that knot failed the volume identity, infinitely many assignments
of this one marked four-vertex template would fail it. This
contradicts the assumed finite-exception conclusion. Hence the knot
satisfies the identity. The fixed pair \(s,c\) was arbitrary. QED.

This proposition is an implication, not a proof of its conclusion.
The proved [two-circle result](research_two_circle_finite_exceptions.md)
leaves a finite set of pairs untreated. Any one hyperbolic pair in
that untreated set has infinitely many preimages in (6). It therefore
cannot be discarded as finitely many assignments of the larger path.
This gives a small explicit instance of the
[zero-cap padding issue](research_finite_exceptions_under_partial_fillings.md#8-a-consequence-of-counting-assignments-strict-padding).

The [reflected even knot theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_reflected_even_kashaev_volume_theorem.md)
now settles the pairs \((s,c)=(-2k,2k)\) for every integer
\(k\ge2\), and their mirrors. Therefore every assignment
\((m,0,-2k-m,2k)\) satisfies the original volume identity.
With fixed parity \(m=\epsilon+2r\), its original filling
coefficients are \((-r,0,k+\epsilon+r,-k)\). All of these
infinite fibers are covered. The argument does not extend the
same conclusion to an arbitrary unequal pair \((s,c)\).

## 3. What exact simplification can transfer safely

There is a useful elementary criterion. Suppose a fixed partial
assignment is transformed by proved marked isotopies into a family
with a cofinite theorem, and let \(f\) be the induced map from its
remaining original assignments to the new assignments. If every
fiber of \(f\) is finite, the inverse image of the finite untreated
set is finite. This transfers the cofinite conclusion without any
new source estimate. Alternatively, an infinite fiber is harmless
when the volume identity is already proved for its knot.

A fixed degree-two power \(\sigma=\pm1\) has precisely the first
behavior: it deletes that vertex and shifts both neighboring powers
by \(-\sigma\), with the prescribed physical rotations. On the
remaining parameter lattice the map is injective. A finite sequence
of such proved moves can therefore transfer the two-circle cofinite
theorem to a template with those extra powers already fixed.
It does not prove the theorem when those powers are also arbitrary
free parameters.

For example, on the three-vertex path, each fixed slice \(b=\pm1\)
reduces to \(K_2(a\mp1,c\mp1)\). A fixed endpoint power
\(a=\sigma\) reduces, by closed turn transfer, to
\(K_2(b-\sigma,c)\); the other endpoint is the same calculation
from the opposite root. Thus the union of these six fixed slices
has only finitely many untreated hyperbolic assignments. At a zero
power the cap rules or the degree-two zero move leave an integral
braid closure or an unknot, so there are no hyperbolic assignments
on those zero slices. Those particular reductions do not treat the
adjacent pair in Section 1; the separate two-crossing chain identity does.

A zero merger \((a,b)\mapsto a+b\) has infinite fibers when both
powers remain free. If one is already fixed, that particular merger
is injective on the other power; otherwise finite exceptions cannot
be pulled back without resolving the affected knots. The same test
must be applied to deleted parameters in a cap splitting. Merely
having finitely many resulting diagrams does not make the parameter
fibers finite.

## 4. Recommendation for the next theorem

The joint polynomial (2) is now controlled, as are the same-sign
chains described above. The next missing composition estimate
concerns general short connected regions, including mixed-sign
chains beyond the now treated pair. For that pair, both the full
boundary asymptotic and its original marked geometric identification
are proved, so the stated long-filling volume conclusion follows.
Multiplication and fixed boundary crossings preserve the
proved concentrated boundary asymptotics. Quarter-turns do not
preserve that class in general: \(T(H_p)=R^p\) for
\(H_p=T(R^p)\), and \(R^p\) has unit-modulus values throughout
the physical spectrum. The missing theorem must therefore use the
geometry of the actual compositions, or include intermediate sources
without strict concentration. More isolated estimates do not by
themselves establish such a theorem.

The new [fixed-domain turn theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_fixed_domain_long_power_turns.md)
does give a uniform composition result when the subsequent powers
are long. One threshold works for chains of arbitrary fixed length,
with either sign at each step and any initial terminal power of
magnitude at least two. It preserves the complete complex boundary
domain and global estimates. The proof therefore removes an actual
iteration problem, but does not establish the required stability
under arbitrary fixed short turns. A noninitial power can still
remain short in infinitely many assignments.

For the general target, the required statement is a boundary theorem
stable under the actual connected partially filled sources, together
with exact treatment of their degenerations. The finite-branching
lemma then applies to the original assignments. Zero mergers and cap
padding require additional care: the four-path proposition shows that
even an unresolved finite list of two-circle knots cannot simply be
left behind. Neither the independent-set assembly nor the current
high-degree connected-cluster theorem supplies this general result.
