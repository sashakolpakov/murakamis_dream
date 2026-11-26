# Unit leaves suffice for every fixed strict Conway tangle

21 November 2026. Research scope lemma. Earlier final notes and public
manuscripts remain unchanged.

Every fixed integer assignment in a strict Conway construction has an
exact strict presentation whose elementary powers are all \(+1\) or
\(-1\). This is a statement about the filled tangles, with their
ordered boundary points and original marked source. The number of new
leaves depends on the fixed powers being expanded.

One can also expand only the already fixed leaves of a partial filling.
The remaining free powers are then unchanged. Consequently, a general
partial-filling theorem for arbitrary fixed short powers can be reduced
to such a theorem for fixed unit powers in arbitrary positions. Neither
statement supplies that missing theorem or a volume lower bound.

## 1. Ordered tangles and the single-crossing identity

Use the literal conventions in the
[strict family definitions](research_strict_conway_family_definitions.md).
The endpoints of a box are ordered as bottom left, bottom right, top
right, top left. The product \(FG\) stacks \(F\) below \(G\), and
\(T\) rotates the entire box clockwise through a quarter turn, carrying
its strands, ribbons and marks. Put
\[
                       h(n)=T(R^n),\qquad n\in\mathbb Z,
 \tag{1}
\]
where \(R^n\) is the original signed two-strand braid.
The cylindrical closure and its empty outside arcs remain fixed.

For one crossing, the actual rotation gives
\[
                     h(\sigma)=T(R^\sigma)\simeq R^{-\sigma},
                     \qquad\sigma\in\{1,-1\}.
 \tag{2}
\]
This can be checked in the single-crossing ball itself. A quarter turn
interchanges the two projected diagonals. After the exposed endpoints
are relabelled by the prescribed tuple, the overpassing diagonal is
therefore the one in the inverse crossing. The strands and their planar
ribbons are precisely the inverse single-crossing diagram. No
Reidemeister-I curl is introduced, and no branch outside this ball is
rotated or discarded.

The full original Newton packet verifies (2), including its scalar.
Write \(d=N-1\), \(q=e^{\pi i/N}\), \(\kappa=q^{d^2/2}\), and use
the normalized Newton basis \(b_0,\ldots,b_d\). The
[actual Newton source theorem](actual_newton_turn_positive_gram.md)
gives
\[
 Jb_r=b_{d-r},\qquad
 R^\sigma=\kappa^\sigma\sum_{r=0}^d(-q)^{\sigma r}b_r.
 \tag{3}
\]
Here \(J\) is the genuine unscaled turn on the complete boundary
algebra, not an eigenvalue-only substitution. Since
\[
 \kappa^2(-q)^d=(-1)^dq^{d(d+1)}=1,
 \]
reversing the coefficients in (3) proves exactly
\[
                              JR^\sigma=R^{-\sigma}.
 \tag{4}
\]
There is no omitted power of \(N\) or unit phase. The identity holds
in the full quotient algebra and hence retains every repeated-root
normal. Physically (2) uses only a single crossing. It does not assert
that \(T^2F=F\) for an arbitrary attached tangle \(F\).

## 2. The expansion and its complete boundary data

For \(n=\sigma k\) with \(k\ge2\), replace one filled leaf by
\[
                 \mathcal U(n)=T\bigl(h(-\sigma)^k\bigr).
 \tag{5}
\]
The power in parentheses means an ordered stack of \(k\) distinct
leaf occurrences. By (2), each factor is the original crossing
\(R^\sigma\), so their concatenation is \(R^{\sigma k}\).
Thus \(\mathcal U(n)\simeq h(n)\) relative to the four outside
endpoints, with the ribbons carried.

For zero use
\[
                         \mathcal U(0)=T\bigl(h(1)h(-1)\bigr).
 \tag{6}
\]
The inner stack is \(R^{-1}R\), which cancels by the ordinary
Reidemeister-II isotopy to the through identity \(R^0\). Turning
that identity gives \(h(0)\), the cup-cap tangle. It is not replaced
by two through strands. Leaves of power \(1\) or \(-1\) are simply
left unchanged.

These replacements lie inside the original leaf ball. They preserve
the outside endpoint order and extend by the identity through every
attachment. Any marked point and ribbon inside the ball are carried
through the displayed isotopy. Consequently they preserve all main
and internal components, the specified reduced cut, and the final
preferred zero framing of a closed knot.

At every level their full open packets are equal as well. The packet
of (5) is
\[
                    J\bigl((JR^{-\sigma})^k\bigr)
                        =J\bigl((R^\sigma)^k\bigr)=JR^n,
 \tag{7}
\]
and the packet of (6) is
\[
                         J\bigl((JR)(JR^{-1})\bigr)=J1.
 \tag{8}
\]
Only actual multiplication and the full identity (4) are used. The
result is an identity before the remaining exterior is contracted.
Every subsequent original boundary observation, including all normal
directions, is therefore retained. No framing correction is inferred
from an unoriented sum of crossing powers; the original ribbons and
the exact scalars (3)--(4) provide the comparison.

## 3. Strictness survives the replacement

Recall the open-output sets for the strict angle test:
\[
             L=(0,1/2),\qquad H=(1/2,1),\qquad A=(0,1).
 \tag{9}
\]
Every elementary leaf has type \(L\). A turn preserves type \(A\).
The strict product table gives \(LL\to A\) and \(AL\to A\).
It follows by induction that an ordered stack of any \(k\ge2\)
elementary leaves has output set exactly \(A\); choose, for example,
left association. Its turn again has output set \(A\). Therefore every
replacement in (5) or (6) has output set
\[
                                  A\supset L.
 \tag{10}
\]

More explicitly, take any strict feasible state of the old expression.
Its output at the replaced leaf is some \(a\in L\). Because the new
subtree has the full output set \(A\), its own strict variables can
be chosen to have output exactly \(a\). Leave all the old variables
outside that leaf unchanged. Every old product inequality and every
old turn equation still holds, as does the complementary-output
condition at the cylindrical root. Do this independently in each
replaced leaf ball. This proves strictness without assuming that the
old optimizer remains an optimizer, or that its geometric metric is
unchanged by drilling a different auxiliary link.

**Proposition.** Every fixed filled strict Conway expression has a
strict expression with only unit leaves, the same full boundary
packet, and the same ordered marked filled tangle. The number of leaves
in this explicit expression is
\[
 H'=\sum_{i=1}^H u(n_i),\qquad
 u(n)=
 \begin{cases}
 2,&n=0,\\
 |n|,&n\ne0.
 \end{cases}
 \tag{11}
\]
In particular a strict knot remains the same knot, with the same
zero-framed reduced invariant at every level. Hyperbolicity, when
present, is a property of that unchanged filled knot.

## 4. A reduction of the partial-filling target to fixed unit powers

Fix a strict template and a proper subset of its original leaves whose
powers have already been assigned arbitrary integers. Expand only
these fixed leaves by (5)--(6). The result is one fixed enlarged
strict template, depending on those assigned integers. Every new
leaf is fixed at \(+1\) or \(-1\); every untouched free leaf keeps
exactly its original integer power, carrier and disk neighborhood.
The local isotopies avoid the latter neighborhoods. Hence every
completion of the free powers gives the same original marked filled
knot and source before and after expansion.
For each new leaf choose its retained carrier to equal its unit power;
its surgery coefficient is then zero. These new auxiliary circles are
filled, not left as unfilled components of the intermediate exterior.

It follows that the following two universal stability statements for
the strict class are equivalent:

1. After any fixed short partial assignment, every sufficiently long
   completion of the remaining powers that gives a hyperbolic knot
   satisfies the original volume identity.
2. The same assertion holds when every fixed power is \(+1\) or
   \(-1\), in arbitrary positions of an arbitrary fixed strict
   template.

The first includes the second. For the converse, apply the second to
the enlarged template just constructed and pull back its threshold.
The free powers are unchanged, so no sums of unbounded opposite
coordinates, affine fibers or loss of longness enter this step.
There is still at least one free leaf because the original partial
assignment was proper. The same argument applies successively after
further partial assignments.

This reduces the numerical alphabet of fixed fillings, not their
interactions. Unit leaves in an arbitrary connected component need
not remain terminal or have degree two after the existing reductions.
Such components can encode every fixed strict core by the proposition.
The general theorem for them remains unproved.

## 5. Scope and existing reductions

The number \(H'\) in (11) depends on the fixed powers. There is no
single enlarged template asserted for an unbounded family of integer
assignments, and no family is changed into long fillings merely by
this expansion. The auxiliary crossing circles of the enlarged
presentation are new labeled disks; their unfilled exterior is not
identified with the old augmented exterior. Only the displayed filled
tangles, and the free disk neighborhoods left untouched in Section 4,
are identified.

The exact terminal zero/unit operations, marked degree-two moves,
cap splitting and affine reduction fibers were already available.
This lemma adds a strict unit-only presentation and the corresponding
uniform reduction of the partial-filling target. It proves no new
analytic source estimate, nonzero geometric coefficient, or volume
identity. A finite-exception argument must still preserve the original
assignment fibers and settle the hyperbolic cores they retain.

## Complete proof sources

Both complete sources were read at the following matching versions.
Only their operation conventions, strict type test and actual complete
Newton source are used; their analytic volume statements are not proof
inputs here.

| Source | SHA-256 |
|---|---|
| [Strict Conway family definitions](research_strict_conway_family_definitions.md) | 55662159ccd65ae3183bc55b4f17b414d15a18b6970e3d54a725ba16247eeb1a |
| [Actual Newton turn and signed crossings](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
