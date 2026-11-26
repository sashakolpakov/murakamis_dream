# What is fixed in a strict Conway filling family?

18 November 2026. Expository research note. This note spells out the
definitions and quantifiers in the frozen statements. It proves no new
volume identity and changes none of those statements.

The phrase “fix an admissible strict Conway tangle construction, its
crossing circles, and a half-twist pattern giving one knot” means:
choose one finite recipe for assembling two-strand boxes; keep a separate
label and crossing disk at every elementary box; check a finite
strictness test; and choose the local even/odd strand connections so
that the closed main strands form one circle. The integers subsequently
varied add full twists inside those same disks. They do not change the
recipe or its component pairing.

## 1. Ordered four-endpoint tangles

A box is a three-ball containing a tangle whose four boundary endpoints
are fixed and ordered. In the rectangular drawing they are
\[
 0=\text{bottom left},\qquad 1=\text{bottom right},\qquad
 2=\text{top right},\qquad 3=\text{top left}.
\]
The box may also contain closed components. Those components must be
retained when boxes are assembled. Boundary order matters: an abstract
isomorphism of tangles that changes the attaching points is not the
specified operation.

The literal operations, in the conventions of [G, §1], are as follows.

* **Product \(FG\).** Place \(F\) below \(G\), join \(F_2\) to \(G_1\)
  and \(F_3\) to \(G_0\), and keep the exposed tuple
  \((F_0,F_1,G_2,G_3)\). This is an ordered stack.
* **Turn \(T(F)\).** Rotate the entire box clockwise through a quarter
  turn, carrying its strands, disks, framings and marks. The new ordered
  tuple is \((F_1,F_2,F_3,F_0)\).
* **Cylindrical closure \(C(F)\).** Join endpoints \(0\) to \(3\) and
  \(1\) to \(2\) by the prescribed empty outside arcs.

Products can be reparenthesized by rescaling their stack collars.
Their factors cannot simply be exchanged. Likewise, the physical
half-turn \(T^2\) must not be erased merely because the corresponding
operator on a particular finite source algebra squares to the identity.
The distinctions between physical moves and algebraic source identities
are explicit in [C, §4]. In particular, there is no rule
\(T(FG)=T(F)T(G)\).

Write \(R^n\) for the standard two-strand braid with \(n\in\mathbb Z\)
signed half twists; \(R^0\) is the two through strands. The elementary
filled leaf is
\[
                         h_i(n_i)=T(R^{n_i}).
\tag{1}
\]
An expression is a finite rooted construction tree built from these
leaves, products and turns, and closed as \(C(FG)\). There are
\(H\ge2\) separately labeled leaf occurrences. Each occurs once and
has its own parameter \(n_i\). Two leaves with the same numerical
twist are still two different boxes.

This is a presentation of a Conway algebraic, or arborescent, tangle.
It is not a claim that every presentation of every arborescent knot is
strict, or that every hyperbolic knot has this presentation.

## 2. Crossing circles and the retained half twists

Before filling a leaf, keep an auxiliary unknot \(c_i\) surrounding its
two strands. It bounds the original crossing disk, punctured twice by
the main strands. The disks lie in the separate leaf boxes and retain
their original local framings. Turns move these disks along with their
boxes.

At leaf \(i\), retain
\[
                           \epsilon_i\in\{0,1,-1\}
\]
half twists: none, one positive, or one negative. Remove the other
full twists but keep \(c_i\). After stacking and closing, this gives an
augmented link with \(H\) labeled auxiliary components and its main
components. Denote its exterior by \(Y_\tau^\epsilon\).

On the boundary torus of \(c_i\), \(\mu_i\) is the meridian of that
auxiliary component. The disk longitude \(\lambda_i\) is its push-off
in the original crossing-disk framing. They are a primitive ordered
integral basis. They are not the meridian and preferred longitude of
the final main knot.

Use the orientations of [G, §1] and [M, §§6–7]. Filling the slope
\[
                            \mu_i+p_i\lambda_i,\qquad p_i\in\mathbb Z,
\tag{2}
\]
removes the crossing circle and inserts \(p_i\) full disk turns with
the convention
\[
                         n_i=\epsilon_i-2p_i.
\tag{3}
\]
Thus one positive unit of this surgery coordinate subtracts two
positive braid half twists. Equation (3) fixes the sign convention;
one must not replace it by \(\epsilon_i+2p_i\) while retaining the
same oriented peripheral basis. At \(p_i=0\), meridional filling
restores just the retained \(\epsilon_i\) crossing.

The surgery is performed in the original disk neighborhood. Its ambient
manifold remains \(S^3\). The main cusp is not filled. If only some
crossing circles are filled, the others remain actual components of
the link exterior.

Both \(+1\) and \(-1\) give odd endpoint pairing, but their signed
half-twist markings are retained. A comparison of those two parents
also changes the description of the primitive meridian; it is not an
instruction to forget the sign.

## 3. Strictness: a finite real-variable test

Strictness is a condition on the construction tree before choosing the
large integer twists. Its variables are normalized source-state or
angle variables, not the integers \(n_i\), the surgery coefficients
\(p_i\), or the quantum level \(N\).

Assign a real output variable to every open subexpression. Require:
\[
\begin{aligned}
 &0<a_i<\tfrac12 &&\text{at every elementary leaf},\\
 &y=1-x &&\text{across a turn},\\
 &\max(x,y)<z<x+y<1 &&\text{at every retained product}.
\end{aligned}
\tag{4}
\]
At the final cylindrical root \(C(FG)\), remove its forced last
product and require only that the two outputs be \(b\) and \(1-b\).
Do not impose the strict product inequality on that removed gate.
The construction is **strict** when these conditions have a solution.

The exact compiler in [C, §2] replaces this feasibility problem by
four possible open-output sets:
\[
 L=(0,\tfrac12),\qquad H=(\tfrac12,1),\qquad
 A=(0,1),\qquad \varnothing.
\]
Here \(H\) as a type label is unrelated to the number \(H\) of leaves.
A leaf has type \(L\). A turn exchanges \(L,H\), preserves \(A\),
and preserves emptiness. The product table is

| Lower / upper type | \(L\) | \(H\) | \(A\) |
|---|---|---|---|
| \(L\) | \(A\) | \(H\) | \(A\) |
| \(H\) | \(H\) | \(\varnothing\) | \(H\) |
| \(A\) | \(A\) | \(H\) | \(A\) |

An empty child makes its ancestors empty. The table is symmetric as a
feasibility statement; this does not make the physical product
commutative. At closure the permitted pairs are
\[
                         AA,\quad AL,\quad AH,\quad LH
\tag{5}
\]
and their reversals. This is exactly the condition that the two open
output sets contain complementary points.

For example, two \(L\) inputs can produce any \(z\in(0,1)\):
choose equal inputs \(a\) with
\(z/2<a<\min(z,1/2)\). Two \(H\) inputs cannot satisfy \(x+y<1\).
These illustrate why the type test concerns genuine open intervals,
rather than nonnegative boundary states.

The geometric meaning is substantial. For a strict construction, the
frozen marked-geometry theorem constructs the complete augmented-link
metric from the original ideal cells. The strict state places the
variational problem in its interior; the proved optimizer is unique
and nondegenerate. The original disks and primitive cusp markings
survive this construction [G, §1; M, §§1–7].

Strictness alone does not say that an arbitrary short filling is
hyperbolic or satisfies the volume identity. Conversely, failure of
the strict test for one presentation is not a counterexample to that
identity, nor an assertion that its finite invariant vanishes.

## 4. The separate knot test, and a checked example

Ignore over/under information just for the purpose of following
components. The three possible pairings of four terminals are
\[
 I=(03)(12),\qquad U=(01)(23),\qquad X=(02)(13).
\]
An even leaf \(T(R^{2k})\) has pairing \(U\); an odd leaf
\(T(R^{2k+1})\) has pairing \(X\). A turn exchanges \(I,U\) and fixes
\(X\). Products use the actual attachment convention of §1:

| Lower / upper pairing | \(I\) | \(U\) | \(X\) |
|---|---|---|---|
| \(I\) | \(I\) | \(U\) | \(X\) |
| \(U\) | \(U\) | \(U\), plus an internal circle | \(U\) |
| \(X\) | \(X\) | \(U\) | \(I\) |

Every internal circle is recorded and kept. At the end, cylindrical
closure adds the pairing \(I\): an output \(U\) or \(X\) gives one
main component, whereas an output \(I\) gives two. An internal circle
can never reconnect to an endpoint later. This is the full knot test,
as used in [M, §7] and [V, §1].

Here is a small actual admissible construction:
\[
 \tau=C\bigl((h_1h_2)(h_3h_4)\bigr),\qquad
                 \epsilon=(0,1,1,1).
\tag{6}
\]
Both retained products have type \(LL\to A\); the closing pair is
\(AA\). More explicitly, take every \(a_i=3/10\) and both retained
outputs \(1/2\). Then \(3/10<1/2<3/5<1\), and the two closing
outputs are complementary. This is a feasible strict state, not a
claim about the maximizing state.

For the component check, the lower child has pairing \(U\cdot X=U\);
the upper child has \(X\cdot X=I\); their product has \(U\cdot I=U\).
No \(U\cdot U\) product occurs, so no internal circle is created.
Closing \(U\) by \(I\) traces the single cycle
\[
                            0\longrightarrow1\longrightarrow2
                              \longrightarrow3\longrightarrow0.
\]
Thus (6) gives one main knot for every integer tuple
\[
                   (n_1,n_2,n_3,n_4)
                   =(-2p_1,1-2p_2,1-2p_3,1-2p_4).
\]
Hyperbolicity and the volume conclusion are guaranteed by the cited
theorem only in its stated long regime. Changing the example to four
odd leaves gives \(I\cdot I=I\), hence two main components. Strictness
and the knot test really are different tests.

## 5. What “admissible” adds

In this discussion, “admissible” is shorthand for a specified bundle
of data and checked hypotheses; it is not a further universal
topological adjective. The bundle consists of:

1. A fixed finite literal expression with \(H\ge2\), the ordered
   attachments of §1, and distinct labeled leaf occurrences.
2. The original crossing circles, their disjoint leaf neighborhoods,
   crossing disks, peripheral bases, and signed half-twist markings.
3. A successful strictness test (4), equivalently the recursive table.
4. A half-twist pattern whose complete component traversal gives one
   main component, including the internal-circle check.

For the scalar invariant one also fixes its single reduced cut and
framing convention. The frozen statement uses unknot value one and
the specified correction from blackboard to zero framing [V, §1].
These normalization data do not add a new topological restriction on
the knot.

There is no extra requirement that both closing children be completed
boxes: the current strict theorem allows bare or turned elementary
closing children. The older completed-root grammar remains the scope
of a separate signed local expansion, as [V, §1] explicitly explains.
The general strict theorem uses the pure source and imposes no
strict-quarter leaf bound or signed-packet prerequisite.
Nor does admissibility mean “already known to satisfy the desired
volume identity”; the combinatorial tests precede that theorem.

## 6. The order of quantifiers in the frozen result

Fix the data in §5. The frozen theorem [V, Theorem 1.1] supplies a
finite threshold \(P_0=P_0(\tau,\epsilon)\) such that, for every
**fixed** integer tuple \(\mathbf p\) satisfying
\[
                              |p_i|>P_0\quad\text{for all }i,
\tag{7}
\]
the resulting knot is hyperbolic and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{\epsilon,\mathbf p})|
           =\operatorname{Vol}(S^3\setminus K_{\epsilon,\mathbf p}).
\tag{8}
\]
The limit runs through all sufficiently large integer levels, not
only a prime or odd subsequence. The precise source theorem also
gives a nonzero leading asymptotic, with its framing phases retained.

The logical order is
\[
 \boxed{\ \text{fix the construction and pattern}\ ;\
   \text{choose a long fixed tuple}\ ;\ N\longrightarrow\infty.\ }
\tag{9}
\]
“Independently long” means no constraint on relative signs or ratios
of the coordinates. It does not allow \(\mathbf p\) or the construction
tree to grow with \(N\). A maximum over the finitely many retained
patterns gives a single threshold for one fixed construction if
desired; no threshold uniform over all constructions is asserted.

Since \(n_i=\epsilon_i-2p_i\), the same condition can be stated using
large absolute physical crossing powers, with a correspondingly
adjusted bound and the fixed parity pattern.

The geometric theorem also permits filling a subset of crossing
circles by long slopes while leaving the others unfilled [G, §1].
That is a theorem near the complete augmented parent. It is not the
assertion that one may first perform arbitrary short fillings and
then invoke the same theorem on the new exterior.

## 7. The stronger arbitrary-partial-filling target

Fix a proper subset \(I\subsetneq\{1,\ldots,H\}\) and any fixed
integers \(a_i\), \(i\in I\), with no longness condition. Fill those
circles first and keep the entire resulting source and its remaining
boundary data. The target is a bound
\[
                            B(\tau,\epsilon,I,\mathbf a)
\]
such that (8) holds for every fixed completion with
\[
 p_i=a_i\ (i\in I),\qquad |p_j|>B(\tau,\epsilon,I,\mathbf a)
       \ (j\notin I),
\tag{10}
\]
whenever the final filled knot is hyperbolic. The threshold may depend
on the already fixed short fillings. The statement must remain
applicable after further partial fillings; when no free coordinate
remains, the iteration stops.

The intermediate exterior need not itself be hyperbolic. Discarding
such an intermediate would change the target unless its relevant
hyperbolic descendants were separately controlled [P, §§3–4, 8].

Condition (7) misses infinitely many assignments when \(H\ge2\):
one coordinate can stay short while another becomes arbitrarily large.
Those are untreated assignments, not counterexamples. Distinct
assignments can also represent the same knot. Thus “all coordinates
long,” “finitely many exceptional assignments for one template,” and
“finitely many exceptional knot types” are different assertions.

Recent general local source results concerning amplitudes, critical
schemes, transverse normal forms or exact current identities do not
change these quantifiers by themselves. To prove (10), they must be
assembled into a theorem for the entire actual partially filled
source, retaining its closing functional and boundary terms and
proving the geometric contribution is nonzero. This note makes no
such additional assembly claim.

## 8. Complete direct texts and author review

The direct texts used here are listed below. The two paper main files
are used for their explicit definitions and theorem statements; this
expository note does not reprove their imported analytic or geometric
theorems. Each listed file was read completely, including the older
scope qualifications, and its SHA256 was renewed after review.

* **G:** [Marked geometry, main file](../papers/strict-conway-geometry/main.tex),
  SHA256 d2cd70531797177de1c73264bcec8e0a38c00668878ab97f8c9499a50d80ca3f.
* **C:** [Exact source composition with single-leaf attachments](actual_conway_single_leaf_source_composition.md),
  SHA256 ba0d23a5e929f375018481e3f9d037e5ed5abe31694f0614af5cb879e0fef022.
* **M:** [General masked marked filling](actual_conway_general_mask_marked_filling.md),
  SHA256 881a265fd9356e6c531ca5db49f337aff3928fac0fe6113a1a03acde39b16ec3.
* **V:** [Conway asymptotics, main file](../papers/conway-asymptotics/main.tex),
  SHA256 98d34dcfe31f89e5c7c7f904da93f375386e9a94a113972fb0a8e78e08b0ca7b.
* **P:** [Finite exceptions and partial fillings](research_finite_exceptions_under_partial_fillings.md),
  SHA256 b9c7a1021de618c1f44ab4b645f98068bd5188f93e51928c1d5de5a55870c566.

The example (6) was checked by the displayed endpoint traversal and
strict-state inequalities on paper. No mathematical program, numerical
experiment, or change to a frozen source was used.
