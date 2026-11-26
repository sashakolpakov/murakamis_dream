# Physical flow faces at a geometric framing endpoint

Private written proof, 18 November 2026.

The compatible endpoint lifts do not give a relative strict physical
fiber. At a separated row endpoint, setting all clock-one wires at
the lower boundary and all clock-one transfers to zero forces further
wire and transfer occupations to zero. Those additional edges have
nonunit geometric clocks. At a column endpoint the same statement
holds for the upper-wire lift, using hole flows.

This is a restriction on these particular physical lifts. A clock-one
wire placed at the opposite finite endpoint has a different support
equation. Its hard unit-shift projector is not removed by choosing a
different principal logarithm. Such sectors, long-transfer sectors,
and their interface currents remain possible sources of the missing
geometric comparison.

We first give exact necessary and sufficient directed-graph criteria
for a macroscopic cut fiber. We then apply the actual signed crossing
formulas to show the extra zero edges at the compatible lifts. The
argument neither assumes that the cut has a surviving directed cycle
nor asserts that it does not. The complete directs are R, M, S and L.

## 1. The original nonnegative circulation

Use R's expanded graph \(\Gamma\). A crossing is split into donor
and receiver visits, joined by its directed transfer edge. The wire
edges form the single directed knot cycle. Write
\[
 d=N-1,\qquad \partial=\text{incoming-minus-outgoing incidence}.
 \tag{1}
\]
The cut wire and the transfer edges are primitive chord coordinates.
If \(a_e\) denotes a wire occupation or a transfer occupation, the
literal support is precisely
\[
 \partial a=0,\qquad 0\le a_e\le d\quad\text{on wires},\qquad
                    a_e\ge0\quad\text{on transfers}.
 \tag{2}
\]
Indeed at a donor \(a_{\rm in}=a_{\rm out}+n\), and at a receiver
\(a_{\rm out}=a_{\rm in}+n\). The input/output bounds imply \(n\le d\).
Thus one may also impose \(a_e\le d\) on every edge without changing
the support. No upper index is replaced by \(N\), and no cyclic
occupation extension is used.

Let \(I\) be any set of edges not containing the cut, and let
\[
                         H=\Gamma\setminus I.
 \tag{3}
\]
Denote by \(\mathcal C(H)\) the set of edges that lie on at least
one directed cycle of \(H\). A directed loop counts as a cycle.
This is a finite combinatorial object determined by the actual
oriented graph and the specified edge set.

Every nonnegative real circulation is a sum of nonnegative multiples
of simple directed cycles. Here is an elementary proof. Starting
from any positive edge, conservation supplies a positive outgoing
edge at each successive vertex. A repeated vertex gives a directed
cycle. Remove the minimum flow on that cycle. At least one positive
edge disappears and no edge becomes negative. Repeating terminates
after finitely many removals, because the number of positive edges
strictly decreases. If the original flow is integral, every removed
weight is integral.

For each edge outside \(\mathcal C(H)\), every simple directed cycle
of \(\Gamma\) containing it meets \(I\). Comparing its coefficient
in this decomposition with the total weight on \(I\) gives
\[
                  a_e\le\sum_{i\in I}a_i
                         \qquad(e\notin\mathcal C(H)).
 \tag{4}
\]
A simple cycle uses an edge at most once; each cycle counted on
the left is counted at least once on the right. This proves the
constant one in (4), independently of \(N\) or the flow.

There is a direct finite cut certificate as well. If a retained
edge \(e:u\to v\) lies on no directed cycle of \(H\), let \(W\)
be the vertices reachable from \(v\) in \(H\). Then \(u\notin W\),
and every edge leaving \(W\) in the full graph belongs to \(I\).
Summing conservation on \(W\), and retaining the nonnegative
incoming edge \(e\), gives the sharper bound
\[
                 a_e\le\sum_{i\in I\cap\delta^+W}a_i.
 \tag{4a}
\]
Thus failure of the cut-cycle test has an explicit collection of
original endpoint edges that bounds the cut occupation.

In particular, when \(a_I=0\), every physical flow is supported
on \(\mathcal C(H)\). If \(a_i=O(N^\alpha)\) on \(I\), for a fixed
number of edges and \(0\le\alpha<1\), every additional edge outside
that cycle set also has flow \(O(N^\alpha)\).

## 2. Macroscopic cut flow and the maximal relative interior

Fix a real fraction \(0<\vartheta<1\). There are supported integral
states with \(a_I=0\) and
\[
                    a_{\rm cut}=\lfloor\vartheta d\rfloor
 \tag{5}
\]
for all sufficiently large \(N\) if and only if the cut edge lies
on a directed cycle of \(H\).

Necessity follows from (4). For sufficiency, choose a simple directed
cycle \(C\) through the cut and put \(\lfloor\vartheta d\rfloor\)
units on its edges, zero elsewhere. It satisfies every conservation
row and every capacity. This is an actual finite support state,
not merely a solution of the complex matching equations.

The same criterion remains necessary if \(a_I=o(N)\) and
\(a_{\rm cut}/d\to\vartheta\): otherwise (4) contradicts (5)'s
macroscopic limit.

There is also an exact description of the possible strict fiber.
Assume the cut belongs to \(\mathcal C(H)\). Choose a directed cycle
through every edge of \(\mathcal C(H)\), and let \(B\) be the sum
of their integral incidence vectors. Thus \(B_e\ge1\) on that
cycle set and \(B_e=0\) elsewhere. Fix a cut cycle \(C\), and choose
a sufficiently small positive constant \(\epsilon\). The real flow
\[
 x=(\vartheta-\epsilon B_{\rm cut}){\bf1}_C+\epsilon B
 \tag{6}
\]
has cut value \(\vartheta\), is strictly positive on every edge of
\(\mathcal C(H)\), and is strictly less than one there. For example,
choose \(\epsilon B_{\rm cut}<\vartheta/2\) and
\(\epsilon\max_e B_e<(1-\vartheta)/2\).
It has a positive capacity margin depending only on this graph
and \(\vartheta\).

An integral version keeps the exact cut value in (5). Put
\[
 b_N=\lfloor\epsilon d\rfloor,\qquad
 t_N=\lfloor\vartheta d\rfloor-b_NB_{\rm cut},\qquad
 a^{(N)}=t_N{\bf1}_C+b_NB.
 \tag{7}
\]
For large \(N\), \(t_N>0\). Equation (7) has all its nonzero edge
values between \(\delta d\) and \((1-\delta)d\), for some fixed
\(\delta>0\), while every edge outside \(\mathcal C(H)\) is zero.
All flows are integral and satisfy the original support.

Consequently a cut fiber with a margin on every edge outside \(I\)
exists exactly when every edge of \(H\) lies on a directed cycle.
When this fails but the cut survives, (7) supplies an interior only
of the smaller face supported on \(\mathcal C(H)\). An integral
port splitting or an undirected cycle does not prove either
directed criterion.

## 3. Column endpoints use a different directed graph

Let \(\gamma\) be the knot circulation: one on wire edges and zero
on transfer edges. It obeys \(\partial\gamma=0\). Define hole
occupations by
\[
 \bar a_e=d-a_e\quad\text{on wires},\qquad
 \bar a_e=a_e\quad\text{on transfers},
 \tag{8}
\]
and reverse every transfer edge while keeping the wire directions.
Call this directed graph \(\bar\Gamma\). Then
\[
                       \bar\partial\bar a=0.
 \tag{9}
\]
In the original orientations this is just
\(\partial(d\gamma-a)=0\); reversing the negative transfer
coefficients gives (8)--(9). All hole capacities remain between
zero and \(d\).

Thus every assertion (3)--(7) applies to \(\bar\Gamma\), with
the cut value \(d-a_{\rm cut}\). In particular the upper-wire
assignment \(a_i=d\) on unit wires, together with zero unit
transfers, is a zero-flow assignment on \(I\) in this hole graph.
The row and column criteria are not obtained by ignoring the
orientation of a signed transfer.

## 4. The actual signed geometric zero rules

Fix S's separated finite framing endpoint with every prefix minor
nonzero and the cut clock different from one. Let \(I\) consist of
all wire clocks equal to one and all transfer clocks equal to one
at this point. It contains at least one wire but omits the cut.

For a row endpoint all physical \(f\)'s are units, and a wire is in
\(I\) exactly when its physical \(e\) is zero. For a column endpoint
all physical \(e\)'s are units, and a wire is in \(I\) exactly when
its physical \(f\) is zero. These statements use the complete
Casimir and the noncentrality of every meridian; S also proves
that the two endpoint types do not mix at this chosen parameter.

We record the needed crossing formulas from M, in its actual
operator order. At a positive crossing, with
\(D=1-e_1f_2\),
\[
 e'_2=\frac{e_1}{K_2D},\qquad
 f'_1=\frac{K_1f_2}{D},\qquad C_+=D^{-1}.
 \tag{10}
\]
The donor is input \(1\), continued to output \(2\); the receiver
is input \(2\), continued to output \(1\). At a negative crossing,
with \(C=1-(K_1/K_2)e_2f_1\),
\[
 e'_1=K_1e_2,\qquad f'_2=f_1/K_2,\qquad C_-=C.
 \tag{11}
\]
The donor is input \(2\), continued to output \(1\); the receiver
is input \(1\), continued to output \(2\). All denominators here
are units on the stated full prefix chart.

At a row endpoint, (10)--(11) show that donor \(e\)-zero status
is preserved along its wire. Moreover,
\[
 \text{transfer}\in I
       \quad\Longleftrightarrow\quad e_{\rm donor}=0,
 \tag{12}
\]
because the recipient's \(f\) is a unit. At such a zero transfer,
the receiver formulas reduce respectively to
\[
                e'_1=e_2/K_1,\qquad e'_2=K_2e_1.
 \tag{13}
\]
Hence its \(e\)-zero status cannot change there either.

For a column endpoint, the recipient \(f\)-zero status is preserved
by (10)--(11), and
\[
 \text{transfer}\in I
       \quad\Longleftrightarrow\quad f_{\rm recipient}=0.
 \tag{14}
\]
When this holds, the other \(f\)-entry reduces respectively to
\[
                 f'_2=K_2f_1,\qquad f'_1=f_2/K_1.
 \tag{15}
\]
These are exactly the row-type rules on \(\bar\Gamma\): the
original recipient is the donor of the reversed hole transfer.
No assumption about signs or positivity of the complex
holonomy entries is used.

## 5. A forced additional wall at the compatible lifts

First take a row endpoint and impose its compatible physical lift
\[
                a_i=0\quad(i\in I).
 \tag{16}
\]
This means lower wire endpoints and small zero transfers, not
an arbitrary choice of lifts of the clock-one values.

Follow the single oriented knot wire cycle and mark a wire by one
when its \(e\) is zero. This periodic indicator is nonempty and
not identically one, since the cut is not marked. It therefore
has a transition from zero to one: a nonzero incoming wire is
followed by a zero outgoing wire at some visit. By (12)--(13)
this visit must be a receiver, and its transfer is not in \(I\).
Thus it has
\[
  e_{\rm in}\notin I,\qquad e_{\rm tr}\notin I,\qquad
                         e_{\rm out}\in I .
 \tag{17}
\]
The letters \(e_{\rm in},e_{\rm tr},e_{\rm out}\) in (17) denote
graph edges, not physical nilpotent entries.

The exact support row at this receiver is
\[
                   a_{\rm out}=a_{\rm in}+a_{\rm tr}.
 \tag{18}
\]
Nonnegativity and (16) force
\[
                         a_{\rm in}=a_{\rm tr}=0.
 \tag{19}
\]
Both are additional zero edges outside \(I\). In \(H\), the
receiver is a sink: its only outgoing edge was removed.
Its two retained incoming edges cannot lie on a directed cycle.
This proves failure of the strict-fiber criterion in Section 2.

The same conclusion is quantitative before imposing exact zeros:
\[
                    a_{\rm in},a_{\rm tr}\le a_{\rm out}.
 \tag{20}
\]
If the compatible endpoint edges have width \(O(\sqrt N)\),
these extra edges also have width \(O(\sqrt N)\). They cannot
remain at a fixed macroscopic interior fraction.

For a column endpoint impose the compatible physical lift
\[
 a_i=d\text{ on unit wires},\qquad
 a_i=0\text{ on unit transfers}.
 \tag{21}
\]
Use \(\bar\Gamma\) and the \(f\)-zero indicator. Equations
(14)--(15) give a hole-receiver birth exactly as above.
Its outgoing hole wire belongs to \(I\), while its incoming
hole wire and reversed transfer do not. Consequently
\[
       \bar a_{\rm in},\bar a_{\rm tr}\le\bar a_{\rm out},
 \tag{22}
\]
and both additional hole flows are zero under (21).
Again the complementary graph has retained edges that cannot
lie on a directed cycle. Thus no compatible row or column
endpoint in this setting has a relative strict fiber with
every non-\(I\) edge in a capacity interior.

The statement does not decide whether the cut lies in the
smaller cycle set. If it does, (7) gives macroscopic physical
states on a more degenerate face. If it does not, (4) bounds
the cut itself by the total compatible endpoint width.

## 6. The geometric point is outside that face's complex closure

Normalize flows by the head capacity and consider the limiting
real physical face defined by (16). Every one of its points
satisfies the additional linear equations (19). Its complex
algebraic closure therefore satisfies those same equations.

On the geometric logarithmic chart, the two extra edges in
(17) have clocks different from one, by their definition as
non-\(I\) edges. Their normalized logarithmic coordinates are
nonzero for every logarithm lift: a zero coordinate would
exponentiate to one. L supplies compatible principal logs
with \(I\)-values zero and the chosen cut log preserved.
The geometric point in that affine flow space consequently
fails (19). It is outside the complex algebraic closure of
the actual compatible row face, even when the real cut
fraction is allowed to vary before taking the closure.

For the column lift use normalized hole coordinates. A unit
wire has principal occupation one and hole coordinate zero.
A non-\(I\) wire cannot have hole coordinate zero, since
that would again give clock one; a non-\(I\) transfer cannot
have zero logarithmic coordinate. L's compatible upper-wire
logs therefore violate the additional equations from (22).
The same closure exclusion holds for that compatible column
face. The exact finite offset \(d=N-1\) changes its principal
reference by \(O(N^{-1})\); it cannot change the nonzero
limiting values on these additional geometric edges.

This identifies a concrete gap in a proposed fiberwise
continuation: complexifying the real compatible endpoint
face alone does not reach the geometric endpoint chart.
An integral splitting of the full flow lattice includes
directions absent from that nonnegative face. It is not a
source contour in those missing directions.

## 7. Opposite endpoint lifts and the retained source problem

The restriction to (16) or (21) is essential. At the row
receiver in (17), one may instead put the clock-one output
wire at its upper physical value \(d\). Its support equation is
\[
                         a_{\rm in}+a_{\rm tr}=d.
 \tag{23}
\]
It permits positive macroscopic incoming occupations.
It has not become (18) with zero right-hand side merely
because a principal logarithm of the output clock was
chosen near zero. The unit \(F\)-shift at that upper head
has a hard cutoff. Its path mask and all normal rows remain.
The analogous opposite assignment for a column endpoint
has the unit \(E\)-shift at a lower head. Long-transfer lifts
can likewise change the physical face.

Equation (23) is only a local support possibility; it does
not prove compatibility of all other faces of the whole
braid. Arbitrary mixed endpoint assignments retain their
full integral and nonnegative-flow constraints. No such
assignment is discarded or identified by logarithmic repair.

Thus the compatible smooth-gauge packet cannot be placed on
its apparent real endpoint face by an integral-coordinate
argument alone. Wrong-facing projector sectors, further
boundary layers, and long-transfer or relative-current
terms may be needed for a whole-source comparison. This
proof does not establish which of them occurs or contributes.
It proves no contour deformation, geometric period, action
gap for those currents, or nonzero scalar coefficient.

## Complete proof-source pins

* R: notes/research_actual_oblique_geometric_contour_decomposition.md,
  SHA256 9180de472bafb38c479d3e1aafac6c75c388d668371892f54219de658728034c.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* S: notes/research_soft_cut_separates_regular_endpoint_types.md,
  SHA256 935f6d97b9ca3a068412b33075610d17e0a571f68f2bc2925eac70c0480a2555.
* L: notes/research_regular_endpoint_logarithms_and_slit_chart.md,
  SHA256 dc340b9beef5dcdc2a01a35030515cc36cf5e6a6babad66b3fce03351817dc7b.

All four complete sources were read nontruncated in this active
sequence; the complete unchanged L read is retained from the
immediately preceding joint-packet proof. Every used implication
was checked. Only written mathematics and text/hash operations
were used. Frozen and public files were not changed.
