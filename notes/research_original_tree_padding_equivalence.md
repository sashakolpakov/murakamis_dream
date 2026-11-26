# Finite exceptions in the original tree grammar force zero exceptions

Research scope theorem, 4 November 2026. Frozen manuscripts are unchanged.

The original ordered circle-tree class already contains a padding
operation that repeats every filled knot on infinitely many original
integer assignments. No enlarged Conway closing grammar is needed.
Consequently a finite-exception theorem for every template in this
original class would prove the volume identity for every hyperbolic
knot represented by the class, with no exceptions. The same assertion
holds for its subclass of paths.

This note audits and extracts the logical consequence of the terminal
splitting in [the reduction-fiber note, Section 8](research_affine_reduction_fibers_and_core_obligation.md#8-a-terminal-splitting-inside-the-original-circle-tree-class).
It is not a new asymptotic or a claim that a failing knot exists.

## 1. The grammar and its required closure property

Use exactly the ordered construction in
[the circle-tree manuscript, Section 1](../papers/circle-tree-volume/main.tex).
A finite tree has at least one edge, one original crossing-circle
tangle at each vertex, and a terminal root. After filling its circles,
the recursive words have the form
\[
 W_v=\left(\prod_{w\in I_v^-}T(W_w)\right)R^{n_v}
                  \left(\prod_{w\in I_v^+}T(W_w)\right).
 \tag{1}
\]
The orders in both lists, physical turns, original disk frames,
orientations, reduced cut and prescribed cylindrical closure are
retained. There are no bare product junctions. Fix carriers
\(\eta_v\in\{-1,0,1\}\) and the original surgery coordinates
\[
                         n_v=\eta_v-2p_v,
                         \qquad p_v\in\mathbb Z.
 \tag{2}
\]
An admissible retained pattern has one main knot component and no
internal closed component. Full twists preserve this component test.
There is no condition excluding zero powers or inessential parameters
after filling, and assignments are not identified when they give the
same knot.

The needed closure property is concrete: replace a terminal vertex
by three consecutive crossing-circle vertices and propagate one
physical half-turn through the remaining ordered subtree. This
operation preserves (1), adds two circles, and takes paths to paths.
Here is the direct grammar check. Put \(\tau=T^2\). The spatial
rotation identities in
[the original collar proof](../papers/conway-reductions/moves.tex) are
\[
 \tau(FG)=\tau(G)\tau(F),\qquad
 \tau(TF)=T\tau(F),\qquad
 \tau(R^n)=R^n,\qquad \tau^2=1.
 \tag{3}
\]
Applying \(\tau\) to (1) exchanges its two child lists and reverses
each order, replacing every child by its half-turned child. Thus it
is another word of (1), with the same labelled vertices and signed
powers. All crossing disks and their frames move with the proper
rotation. It is not a mirror, and no exponent is negated. Before
filling, transport the original disk meridians and longitudes by
the same rotation; the coefficient in (2) is unchanged.

The equivalence below concerns a class closed under this operation.
Both the unrestricted original ordered circle-tree class and the
original path class have that property. A class with a fixed bound
on vertex number, a prohibition of zero fillings, or identified
parameter fibers need not have it; those are different targets.

## 2. One enlarged template and its exact zero slice

Let \(Q\) be an admissible marked template in the original class.
Expose its terminal root, using closed cyclicity if its only child
is initially on the other side. Write its evaluated closure as
\[
                       K_Q(s,\mathbf n)=C(R^sT(F_{\mathbf n})).
 \tag{4}
\]
The expression \(F_{\mathbf n}\) contains every other original
vertex exactly once. Define one enlarged template, independently of
the numerical assignments, by
\[
 P_Q(a,v,b,\mathbf n)=
 C\!\left(R^aT\!\left(R^vT\!\left(R^b
                         T(\tau F_{\mathbf n})\right)\right)\right).
 \tag{5}
\]
Its terminal chain has powers \(a,v,b\), and its remaining tree is
the half-turned old subtree. Each product still belongs to a vertex
with its own original crossing circle. By (3) this is an allowed
fixed ordered template, not a word chosen after evaluating its powers.

**Lemma 1.** For every integer assignment,
\[
                    P_Q(a,0,b,\mathbf n)
                           \simeq K_Q(a+b,\mathbf n).
 \tag{6}
\]
The isotopy is one of the actual closed main links, with all components,
orientations, marked cuts and supplied ribbons transported.

*Proof.* The zero power is the through identity before its adjacent
turns. Thus
\[
 \begin{split}
 P_Q(a,0,b,\mathbf n)
 &=C\!\left(R^a\tau(R^bT(\tau F_{\mathbf n}))\right)\\
 &=C\!\left(R^aT(F_{\mathbf n})R^b\right)\\
 &\simeq C\!\left(R^bR^aT(F_{\mathbf n})\right)
  =K_Q(a+b,\mathbf n).
 \end{split}
 \tag{7}
\]
The second line uses every order reversal in (3). The third is
closed cyclicity in the specified empty outside collar, followed
by concatenation of integral braids. It does not commute two open
tangles or erase a physical half-turn. The collar proof carries
all components and the reduced cut, and introduces no boundary
Dehn twist. These are ambient isotopies in the oriented three-sphere.
\(\square\)

In particular, the knot complements have equal volume whenever they
are hyperbolic. Transport the ribbon in (7) and then apply the
prescribed zero-framing correction. The original reduced Kashaev
invariants agree at every level. An uncorrected diagram may have a
framing factor; no equality of uncorrected diagrams is asserted.
Nor is (7) asserted to identify exteriors with different numbers of
*unfilled* auxiliary tori.

Give the new three vertices carriers
\[
                    (\eta_a,\eta_v,\eta_b)=(0,0,\eta_s),
 \tag{8}
\]
and transport the other old carriers with \(\tau\). If
\(s=\eta_s-2p_s\), the map
\[
 \iota:\quad ((p_s,\mathbf p),r)\longmapsto
             (p_a,p_v,p_b,\mathbf p)=(r,0,p_s-r,\mathbf p)
 \tag{9}
\]
is a bijection from the old integer assignment lattice times
\(\mathbb Z\) onto the entire slice \(p_v=0\) of the new lattice.
Its inverse is \(p_s=p_a+p_b\), \(r=p_a\). In particular
\[
             a=-2r,\quad v=0,\quad
             b=\eta_s-2(p_s-r),\quad a+b=s.
 \tag{10}
\]
All original parity restrictions are respected by fixed carriers;
\(r\) is unrestricted.

The enlarged retained pattern is admissible. At its retained
assignment, \(a=v=0,b=\eta_s\), (6) gives the old retained
knot. An internal closed component in a proper tangle could never
rejoin an endpoint and would leave an additional closed component,
so none is present. Every other assignment of the enlarged fixed
pattern has the same endpoint connections and internal component
count, because each change in (2) inserts a full twist. This proves
the actual knot test for one fixed enlarged template, not merely
for a collection of favorable parity choices.

## 3. Equivalence for the original tree and path classes

For a marked template \(Q\), let \(\mathcal F_Q\) denote the set
of its original integer assignments giving hyperbolic knots for
which the original Kashaev volume identity fails. Failure here
includes nonexistence of the proposed limit. This notation does
not assert that \(\mathcal F_Q\) is nonempty.

**Theorem 2.** For the original ordered circle-tree class, the
following statements are equivalent:

1. Every fixed admissible marked template has only finitely many
   assignments in \(\mathcal F_Q\).
2. Every hyperbolic knot represented by an admissible original
   template satisfies the original Kashaev volume identity at
   every integer assignment of its powers.

The same equivalence holds when both statements are restricted to
the original path class. More precisely, cofiniteness for the single
enlargement \(P_Q\) implies \(\mathcal F_Q=\varnothing\).

*Proof.* Lemma 1, the zero framing and the bijection (9) give the
exact equality of assignment sets
\[
       \iota^{-1}\bigl(\mathcal F_{P_Q}\cap\{p_v=0\}\bigr)
                          =\mathcal F_Q\times\mathbb Z.
 \tag{11}
\]
If the left side is finite, the right side is finite; hence
\(\mathcal F_Q\) is empty. Apply this to each \(Q\), using
the closure of the original grammar verified in Section 1.
The converse is immediate with no exceptions. The construction
preserves paths, proving the path assertion. \(\square\)

This does not assert that every hyperbolic knot has an original
circle-tree presentation. It concerns precisely the represented
class, with the same markings and assignment quantifiers as the
proposed finite-exception theorem. It also does not assert that
cofiniteness for \(Q\) itself implies no exceptions for \(Q\);
the needed premise is cofiniteness for its single enlargement.

**Corollary 3.** A universal long-remainder theorem for the partial
assignments of the enlarged templates would already imply statement
2, even if only its two-free-coordinate strata were used.

*Proof.* Fix any old assignment \((p_s,\mathbf p)\) giving a
hyperbolic knot. In (5), fix \(p_v=0\) and all old coordinates
\(\mathbf p\), leaving only \(p_a,p_b\) free. Along (9),
both \(|p_a|\) and \(|p_b|\) tend to infinity as \(|r|\) does,
while the knot remains exactly the fixed knot of \(Q\).
Any finite longness threshold on this partial-assignment stratum
therefore proves the identity for that knot. \(\square\)

## 4. Consequence for a finite branching proof

The existing degree-two zero move merges the two powers in (10).
Its output is indeed simpler, but its original assignment fiber
is \(\mathbb Z\). A proof cannot terminate this branch at an
untreated hyperbolic core and count that core as one exceptional
assignment. In contrast, the proved degree-two unit moves give
injective translations when their specified power is fixed.
The exact same-sign two-crossing reductions retain their stated
boundary twists and rotations; they supply no identity for a
general remaining short core.

Thus the new homogeneous-three source and boundary theorems give
genuine additional solved records. They do not alter (11).
A general finite branching closure must either prove the identities
of the hyperbolic cores occurring on infinite fibers, or supply a
source theorem that proves those identities through the long
remainder in Corollary 3. Leaving such cores untreated would assume
the missing conclusion. No numerical case or asymptotic estimate is
needed for this logical implication.
