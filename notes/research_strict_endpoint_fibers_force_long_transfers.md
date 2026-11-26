# A strict mixed endpoint fiber requires a long unit transfer

**Status, 18 November 2026:** superseded as a source-placement
criterion by
[the boundary-propagation theorem](research_geometric_endpoint_boundary_propagation.md).
That theorem proves that the strict-sector hypotheses (2)--(3)
below are empty. The conditional long-transfer implication remains
true, but has no occurrence content and must not be used as evidence
that the original source contains a contributing long block.
The proof is retained for the derivation history; no adoption of
this superseded note is requested.

Private written proof, 18 November 2026.

Allow arbitrary lower and upper assignments to the clock-one wires
of a separated geometric endpoint. If all other wires and transfers
stay macroscopically inside their capacities, the physical source
must contain a clock-one transfer near its upper value \(N-1\).
The corresponding Euler block runs between opposite head corners.
Thus mixed wire lifts do not restore a strict fiber using only the
small-transfer endpoint kernels.

This is a support theorem for actual finite states. It does not
assert that such strict states exist, that their analytic continuation
reaches the geometric point, or that their periods are nonzero.
Its proof directs are F, the physical flow-face theorem, and M,
the literal signed crossing map.

## 1. The finite sector and its quantitative hypotheses

Fix the endpoint and its expanded directed graph as in F. The knot
wire edges form one directed cycle; every crossing has one donor
and one receiver, joined by the transfer edge. Put
\[
 d=N-1,\qquad c=\text{number of crossings}.
 \tag{1}
\]
Let \(I\) consist of the geometric clock-one wire and transfer
edges. It contains a wire and omits the cut. At a row endpoint
all physical \(f\)'s are units and the \(I\)-wires are exactly
the \(e\)-zero wires. At a column endpoint all \(e\)'s are units
and the \(I\)-wires are exactly the \(f\)-zero wires.

Choose \(0<\eta<1/2\) and an endpoint width \(\omega\ge0\) such that
\[
             \omega<\min\{\eta d,\ d/(c+2)\}.
 \tag{2}
\]
Consider any supported integral state satisfying
\[
 \begin{split}
 &a_e\in[0,\omega]\cup[d-\omega,d] &&(e\in I),\\
 &a_e\in[\eta d,(1-\eta)d] &&(e\notin I).
 \end{split}
 \tag{3}
\]
The first line applies separately to wires and transfers. In
particular, mixed lower and upper wire assignments are allowed,
and no unit-transfer logarithm has been reset to a small physical
integer. The second line includes every non-\(I\) transfer.
All \(a_e\)'s are the original nonnegative integer occupations,
with wire and transfer capacities \(d\).

For any fixed \(\eta>0\), condition (2) holds for all large \(N\)
when \(\omega=o(N)\), including \(\omega=C\sqrt N\). If only
the endpoint clocks are specified asymptotically, an actual
physical sequence with \(Q^{a_e}\to1\), \(Q=e^{2\pi i/N}\),
has \(\min(a_e,d-a_e)=o(N)\); the difference between \(N\)
and \(d\) is one. Thus (3)'s width formulation records both
physical lifts of a clock-one limit.

The conclusion is that some transfer edge \(i\in I\) satisfies
\[
                              n_i\ge d-\omega.
 \tag{4}
\]
All four wire occurrences incident to this crossing belong to
\(I\). More precisely, in the literal donor/receiver order,
its input and output occupations have the form
\[
 (d-u,v)\longmapsto(w,d-z),\qquad
 n_i=d-u-w,\qquad
             u+w=v+z\le\omega,
 \tag{5}
\]
where \(u,v,w,z\) are nonnegative integers. For a negative
crossing these are the actual donor and receiver ports in
its reversed operator order, with its original flip and Cartan
factors still present.

## 2. Zero status at every interior visit of a unit-wire run

F already proves that donor \(e\)-zero status is preserved for
either signed crossing, and that at a row endpoint a transfer
belongs to \(I\) exactly when its donor \(e\) is zero.
Consequently a donor visit with both incident wires in \(I\)
has an \(I\)-transfer.

The receiver assertion also follows from the literal full map.
For a positive crossing, suppose its receiver input and output
both have \(e=0\). Its receiver input is head \(2\), so the
complete Casimir and the unit \(f_2\) give \(K_2=-1\).
M's formula, with \(D=1-e_1f_2\), reduces to
\[
                         e'_1=e_1^2f_2/K_1.
 \tag{6}
\]
The output being zero forces \(e_1=0\), since \(K_1,f_2\) are
units. Hence its transfer is in \(I\). For a negative crossing
the receiver input is head \(1\). Setting \(e_1=0\), \(K_1=-1\)
in M's formula with \(C=1-(K_1/K_2)e_2f_1\) gives
\[
                   e'_2=-(K_1/K_2)e_2^2f_1/C.
 \tag{7}
\]
Again the unit factors show that \(e'_2=0\) forces \(e_2=0\).
All denominators are units on the retained prefix chart.

Thus every interior visit along a consecutive run of \(I\)-wires
has a transfer in \(I\). This is a statement about its classical
clock; the physical transfer at that visit is still allowed to
be near \(d\). No finite support or full normal row is changed.

For a column endpoint use F's hole graph: keep wire directions
and reverse all transfer arrows. The original recipient becomes
the hole donor, whose \(f\)-zero status is preserved. At a
hole receiver with both \(f\)-entries zero, the corresponding
full signed formulas are
\[
 \begin{array}{ll}
 f_1=0,\ K_1=-1:
       & f'_2=K_2e_1f_2^2\quad\text{(positive)},\\[2mm]
 f_2=0,\ K_2=-1:
       & f'_1=-(K_1/K_2)e_2f_1^2/C
                                      \quad\text{(negative)} .
 \end{array}
 \tag{8}
\]
The physical \(e\)'s and the displayed denominators are units.
These equations prove the same interior-visit assertion for
the \(f\)-zero run in the hole graph.

## 3. A unit-wire run must lose almost one whole head

Consider a row endpoint. The periodic indicator of \(e\)-zero
wires on the single knot wire cycle is nonempty and proper.
Choose a transition from a non-\(I\) wire to an \(I\)-wire,
and follow the maximal consecutive run of \(I\)-wires to its
next non-\(I\) wire.

By F's signed zero rules, both the initial birth and terminal
death are receiver visits. Their transfers are outside \(I\):
a zero transfer would preserve the receiver zero status.
At the birth, conservation and (3) give
\[
 a_{\rm first}=a_{\rm in}+n_{\rm birth}\ge2\eta d.
 \tag{9}
\]
Since \(a_{\rm first}\) is within \(\omega\) of one endpoint
and \(\omega<\eta d\), it must be upper:
\[
                         a_{\rm first}\ge d-\omega.
 \tag{10}
\]
At the death,
\[
 a_{\rm last}=a_{\rm out}-n_{\rm death}
                    \le(1-2\eta)d.
 \tag{11}
\]
Its endpoint alternative cannot be upper under (2), so
\[
                              a_{\rm last}\le\omega.
 \tag{12}
\]

All visits strictly between these two ends have both wire
occurrences in \(I\), and hence all their transfers belong
to \(I\) by Section 2. Telescoping their exact occupation rows
along the run gives
\[
 a_{\rm last}-a_{\rm first}
       =\sum_{\rm internal\ receivers}n_i
                          -\sum_{\rm internal\ donors}n_i.
 \tag{13}
\]
Nonnegativity and (10)--(12) imply
\[
              \sum_{\rm internal\ donors}n_i\ge d-2\omega.
 \tag{14}
\]
There are at most \(c\) such donor visits. If all their transfers
were at the lower alternative \(n_i\le\omega\), then
\[
                         d-2\omega\le c\omega,
 \tag{15}
\]
contrary to (2). Therefore one of these \(I\)-transfers obeys
(4). If the run had no internal donor at all, (14) would
already contradict the existence of the state.

Even without the endpoint alternatives for \(I\)-transfers,
(14) forces a macroscopic \(I\)-transfer of size at least
\((d-2\omega)/c\). Their clock-one endpoint condition in (3)
is the additional input that places it specifically near \(d\).

For a column endpoint set hole occupations
\(\bar a=d-a\) on wires and \(\bar n=n\) on reversed transfers.
The bounds (3) are invariant under this change. The same
birth/run/death argument with the \(f\)-zero indicator proves
(14) for hole donors and hence (4) for the original transfer.
Nothing in this step replaces a physical upper index by a
lower index in the original source.

## 4. The forced block and the exact finite covering

Suppose (4) holds. At its original donor, write the input
as \(d-u\) and the output as \(w\). The exact support row gives
\[
                         u+w=d-n_i\le\omega.
 \tag{16}
\]
At its recipient write the input as \(v\) and the output as
\(d-z\). Then
\[
                         v+z=d-n_i\le\omega.
 \tag{17}
\]
This proves (5), with all finite offsets retained.
Every one of these four wires is within \(\omega\) of an
endpoint. Since \(\omega<\eta d\), none can be a non-\(I\)
wire under (3). Thus the forced long transfer occurs at
a crossing whose four wire occurrences have geometric
clock one, all of the same separated row or column type.

If the fixed geometric pattern has no crossing with all
four wires in \(I\), the sector (3) is therefore empty.
When it is nonempty, a finite exact covering is available:
order the \(I\)-transfer crossings as in the actual finite word
and partition (3)'s supported states by the first crossing
with \(n_i\ge d-\omega\). There are at most \(c\) pieces,
each carrying the block (5). The earlier-crossing inequalities
and all original physical/window bounds remain in its mask.
This is a partition of finite states, not an independent
replacement of the surrounding network by a model packet.

The same statement applies to the coupled interface states
only when their actual affine support inequalities satisfy
the hypotheses. A signed current can include states outside
(3); these are not silently added to the covering or estimated
by it.

## 5. What the necessity does and does not supply

The compatible lower-row or upper-column face from F already
forced extra small edges. The present theorem allows mixed
wire lifts and identifies a further necessary alternative:
to keep every non-\(I\) edge macroscopically interior, at least
one unit Euler block must traverse almost its entire finite
head. Its deficit is \(O(\omega)\), not a small transfer
about the same endpoint.

Thus a calculation retaining only the \(n=O(\sqrt N)\)
same-collar blocks cannot cover this strict physical sector
when \(\omega=O(\sqrt N)\). An exact long-block kernel must
retain its opposite head ports, full factorial normal
factors, flip, Cartan line, and the coupled masks just described.
The theorem determines the required sector but does not
evaluate its surrounding state.

There is no assertion that the whole original relative cycle
has nonzero pairing with any one of these pieces. Nor is a
power of \(N\) in a single block identified with a scalar
normalization or a framing period. Cancellations, other
physical faces, prefix-zero strata, infinity, and all
current boundaries remain separate source questions.

## Complete proof-source pins

* F: notes/research_geometric_endpoint_physical_flow_faces.md,
  SHA256 3d79e497da998f27e4beeb8d0914ddd4efbf6906fb7175e2ff83e464b6bf50c4.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.

Both complete proof sources were read nontruncated in the
immediately preceding active author sequence and retained
unchanged. The actual signed formulas and every used implication
were rechecked. Only written mathematics and text/hash operations
were used. Frozen and public files were unchanged.
