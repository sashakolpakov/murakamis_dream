# Boundary propagation at a geometric framing endpoint

Private written proof, 18 November 2026.

For the actual finite source, a geometric clock-one pattern cannot
be the entire set of thin physical boundary edges. Allow any mixture
of lower and upper lifts, including upper unit-transfer aliases.
If every clock-one edge lies within width \(\omega\) of a physical
endpoint and \((c+2)\omega<N-1\), then at least one edge whose
geometric clock is not one lies within that same width of an endpoint.

The proof is global on the single knot wire cycle. Long transfers
between clock-one wire runs cancel from its total flow budget.
They cannot drain the excess unless another boundary layer occurs.
This is an exact support statement, not a claim about cancellation
of complex amplitudes or about a geometric period.

The complete directs are F, the physical flow-face theorem, and M,
the actual signed crossing map. The earlier conditional long-transfer
necessity is not a proof premise: its proposed fully strict sector
is empty by the theorem proved here.

## 1. Actual support and arbitrary endpoint lifts

Use F's expanded directed graph for the fixed knot braid. Its wire
edges form a single directed cycle. Each of the \(c\) crossings
has a donor and a receiver visit, with its directed transfer edge
joining the donor to the receiver. Put
\[
                         d=N-1,\qquad N\ge2.
 \tag{1}
\]
The original nonnegative integer occupations obey
\[
 a_{\rm in}=a_{\rm out}+n
       \quad\text{at a donor},\qquad
 a_{\rm out}=a_{\rm in}+n
       \quad\text{at a receiver},\qquad 0\le a_e\le d.
 \tag{2}
\]
The last inequality applies to transfers as well: it follows
from the input/output wire capacities. These are F's exact
support equations in the primitive cut-and-transfer coordinates.

Fix a separated finite geometric endpoint with every retained
prefix minor nonzero and cut clock different from one. Let \(I\)
be all wire and transfer edges whose geometric clocks are one.
There is at least one \(I\)-wire, and the cut wire is not in \(I\).
At a row endpoint all physical \(f\)'s are units and \(I\)-wires
are precisely the \(e\)-zero wires. At a column endpoint all
physical \(e\)'s are units and \(I\)-wires are precisely the
\(f\)-zero wires. The complete-color and separation hypotheses
are those already checked in F.

For a physical index define its endpoint distance
\[
                           D_e=\min(a_e,d-a_e).
 \tag{3}
\]
We prove the following implication for every supported state:
\[
 \boxed{\quad
 (c+2)\omega<d,\qquad D_i\le\omega\quad(i\in I)
       \quad\Longrightarrow\quad
       D_e\le\omega\text{ for some }e\notin I .
 \quad}
 \tag{4}
\]
Here \(\omega\ge0\), and no common choice of the two endpoints
is imposed. A unit wire or transfer may separately occupy its
lower or upper band. In particular (4) retains the long
\(n\approx d\) aliases rather than replacing them by small
transfers. The threshold makes the two endpoint bands disjoint.

## 2. The exact zero-status rules at both crossing signs

At a row endpoint, F proves that donor \(e\)-zero status is
preserved for both signed crossings, and
\[
           \text{transfer}\in I
             \quad\Longleftrightarrow\quad e_{\rm donor}=0.
 \tag{5}
\]
Thus the donor of every \(I\)-transfer has both wire occurrences
in \(I\). At an \(I\)-transfer, its receiver's zero status is also
preserved. In M's conventions the receiver \(e\)-entry is multiplied
by \(K_1^{-1}\) positively and by \(K_2\) negatively.
These multipliers are units.

We need the converse at an internal receiver as well. Suppose its
input and output both have \(e=0\). Positively the input is head 2;
the complete Casimir gives \(K_2=-1\). With \(D=1-e_1f_2\), M's
full receiver formula reduces to
\[
                              e'_1=e_1^2f_2/K_1.
 \tag{6}
\]
Hence \(e'_1=0\) forces \(e_1=0\). Negatively the receiver input
is head 1, so \(e_1=0\) and \(K_1=-1\). With
\(C=1-(K_1/K_2)e_2f_1\), its formula becomes
\[
                        e'_2=-(K_1/K_2)e_2^2f_1/C.
 \tag{7}
\]
Again the other factors are units, and \(e'_2=0\) forces \(e_2=0\).
Thus every visit with both wire occurrences in \(I\) has its
transfer in \(I\), including receiver visits.

The column statement uses the actual hole graph from F:
wire directions are kept, transfer directions reversed, and
\[
                 \bar a=d-a\text{ on wires},\qquad
                 \bar n=n\text{ on transfers}.
 \tag{8}
\]
These are nonnegative supported flows with the same capacities.
The original recipient becomes the hole donor. Its \(f\)-zero
status is preserved, and a transfer is in \(I\) exactly when
that hole donor has \(f=0\). At a hole receiver with both incident
\(f\)'s zero, the full signed formulas give
\[
 \begin{array}{ll}
 f_1=0,\ K_1=-1:& f'_2=K_2e_1f_2^2\quad\text{(positive)},\\[1mm]
 f_2=0,\ K_2=-1:& f'_1=-(K_1/K_2)e_2f_1^2/C
                                             \quad\text{(negative)} .
 \end{array}
 \tag{9}
\]
The physical \(e\)'s and all denominators are units. These prove
exactly the row-type zero-status rules for the hole graph.

Equations (5)--(9) concern the geometric pattern \(I\).
They do not prescribe a small value for a physical \(I\)-transfer.
All its original lower and upper support alternatives remain.

## 3. The summed wire-run identity

First treat a row endpoint. Divide the nonempty proper set of
\(I\)-wires into its maximal consecutive runs on the oriented
knot wire cycle. Let there be \(s\ge1\) runs. Denote the first
wire value of run \(\ell\) by \(A_\ell\), and the last by \(B_\ell\).
A run of a single wire is allowed; then these are the same value.

A birth from a non-\(I\) wire to an \(I\)-wire cannot occur at a
donor by zero-status preservation. It is a receiver, and its
transfer is outside \(I\): an \(I\)-transfer would preserve the
receiver status too. The same statements hold for the death
from an \(I\)-wire to a non-\(I\) wire.

Assume for contradiction that every non-\(I\) edge has
\[
                              \omega<a_e<d-\omega.
 \tag{10}
\]
At the birth of each run, (2) gives
\[
                  A_\ell=a_{\rm in}+n_{\rm birth}>2\omega.
 \tag{11}
\]
Since \(A_\ell\) is in one of the two endpoint bands, it must
be upper: \(A_\ell\ge d-\omega\). At the death,
\[
                  B_\ell=a_{\rm out}-n_{\rm death}<d-2\omega.
 \tag{12}
\]
Its upper alternative is impossible, so \(B_\ell\le\omega\).
Consequently
\[
                \sum_{\ell=1}^s(A_\ell-B_\ell)
                                     \ge s(d-2\omega).
 \tag{13}
\]
This already excludes a one-wire run under (10); no exceptional
treatment of that case is needed below.

All visits strictly inside these runs have both wire occurrences
in \(I\), and Section 2 shows that every transfer at such a visit
belongs to \(I\). Telescoping (2) on all the runs gives
\[
 \sum_{\ell=1}^s(A_\ell-B_\ell)
       =\sum_{\text{internal donors}}n_i
                          -\sum_{\text{internal receivers}}n_i.
 \tag{14}
\]
Every \(I\)-transfer has its donor internal to a run, by (5).
Its receiver is either internal to an \(I\)-run or has both wire
occurrences outside \(I\), because that transfer preserves receiver
zero status. If its receiver is internal, its two contributions in
(14) cancel, including when both visits lie in the same run.

Let \(\mathcal E\) be the \(I\)-transfers whose receiver has both
wire occurrences outside \(I\). We obtain the exact global identity
\[
             \boxed{\displaystyle
               \sum_{\ell=1}^s(A_\ell-B_\ell)
                                      =\sum_{i\in\mathcal E}n_i .}
 \tag{15}
\]
Birth and death transfers are not omitted: they are the non-\(I\)
transfers already recorded in the endpoint values (11)--(12).
Equation (15) includes all internal \(I\)-transfers with their
actual physical sizes. It does not discard long aliases.

At the receiver of an edge in \(\mathcal E\), (10) and (2) give
\[
                        n_i=a_{\rm out}-a_{\rm in}<d-2\omega.
 \tag{16}
\]
Its upper unit-transfer alternative \(n_i\ge d-\omega\) is
therefore impossible, including when \(\omega=0\). Hence
\[
                     n_i\le\omega\quad(i\in\mathcal E),
                     \qquad |\mathcal E|\le c.
 \tag{17}
\]
Combining (13), (15) and (17) yields
\[
                    s(d-2\omega)\le c\omega.
 \tag{18}
\]
But \(s\ge1\) and \((c+2)\omega<d\) give
\(s(d-2\omega)\ge d-2\omega>c\omega\), a contradiction.
This proves (4) for row endpoints.

For a column endpoint use (8), the \(f\)-zero runs, and (9).
The endpoint distances (3) are unchanged by hole conversion,
as is the strict interior condition (10). Every step
(11)--(18) applies in the hole graph. Translating back proves
(4) for the original column source, with no endpoint reset.

## 4. Exact boundary covering and source scope

For any fixed \(\omega\) satisfying (4), the theorem is the exact
support inclusion
\[
 S_N\cap\bigcap_{i\in I}\{D_i\le\omega\}
       \ \subseteq\
             \bigcup_{e\notin I}\{D_e\le\omega\},
 \tag{19}
\]
where \(S_N\) is the original finite support. Fixing an order of
the non-\(I\) edges gives a disjoint finite partition by the first
additional edge with \(D_e\le\omega\). Its two lower/upper bands
and all earlier-edge exclusions stay in the corresponding mask.
There are at most \(3c\) choices of the additional edge in the
expanded graph.

Equation (19) is valid with arbitrary complex weights on the
original supported states. It uses positivity of occupation
indices, not positivity of their amplitudes. It supplies no
upper or lower bound for a signed sum. If an inserted current
changes matching or support by an affine shift, its exact
shifted constraints must be checked separately; it is not
silently put back into \(S_N\).

For \(\omega=0\), some additional nonunit-clock edge is exactly
at a finite endpoint. For \(\omega=C\sqrt N\), an additional
boundary layer has the same \(O(\sqrt N)\) width, for all large
\(N\). More generally this applies to every sublinear width.
Thus allowing mixed wire lifts and long unit transfers does not
produce a sector in which precisely the geometric unit edges
are near their endpoints and all other edges remain farther away.

A long \(I\)-transfer is still an actual finite matrix block.
Its value or its opposite-corner kernel is not contradicted by
(4). The identity (15) says why such blocks alone do not solve
source placement: those connecting two \(I\)-runs cancel in
the total support budget, while an escape to the strict
complement cannot be long. A physical state using long blocks
must therefore bring additional non-\(I\) edges to the boundary.

Those extra edges have nonunit geometric clocks. Their finite
boundary factors, analytic continuations and interface currents
must be retained in any comparison with the geometric chart.
Neither the lattice port map nor a local endpoint Gaussian
constructs that comparison. The theorem makes no assertion
about a deformation of the original relative cycle, a framing
period, a scalar normalization, or a nonzero geometric coefficient.

## Complete proof-source pins

* F: notes/research_geometric_endpoint_physical_flow_faces.md,
  SHA256 3d79e497da998f27e4beeb8d0914ddd4efbf6906fb7175e2ff83e464b6bf50c4.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.

Both complete sources were read nontruncated in the current
active author sequence and retained unchanged. Every signed
formula, support implication and source qualification used here
was checked. Only written mathematics and text/hash operations
were used. Frozen and public source texts were not changed.
