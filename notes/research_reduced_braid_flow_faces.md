# Strict physical flows and geometric endpoint faces of the reduced braid

Private written proof, 18 November 2026.

The actual reduced braid network always has strictly positive closed
physical flows for all sufficiently large levels. This follows from
knot routing through its full triangular \(S\)-junctions, including
when the remaining wire permutation has several cycles.

There is a different conclusion for its geometric clock-one pattern.
On the resolved all-\(f\)-unit chart with regular semisimple total
product, a nonempty clock-one pattern cannot be the only thin physical
boundary layer. If all its indices are within width \(\omega\) of
either endpoint and \((T+2)\omega<N-1\), some nonunit-clock edge
is within the same width of an endpoint. Here \(T\) counts the
actual transfer edges, including every branch of an \(S\)-junction.

Whole clock-one wire cycles are retained. They are not excluded by an
appeal to irreducibility. The proof uses the specific reduced knot
routing and the full \(S\)-junction equations. It supplies support
information, not a signed-current estimate or a geometric contribution.

The complete directs are G, the actual reduced correspondence, and C,
the original signed crossing flow rules. All additional routing,
circulation and endpoint arguments are proved below.

## 1. The exact reduced directed graph

Let a braid on \(m\ge2\) heads close to one knot, and put
\[
 r=m-1,\qquad d=N-1,\qquad N\ge2.
 \tag{1}
\]
For the finite matrices use \(q=e^{\pi i/N}\), \(Q=q^2\),
\(x=-M/q\), and \(f_k=\prod_{\ell=1}^k(1-Q^\ell)\), \(f_0=1\).
The quantum parameter is fixed; \(M\) is the common meridian.
Use G's actual reduced generators: an original \(R_i^{\pm1}\),
\(i\ge2\), is the physical checked crossing on the corresponding
remaining heads; an \(R_1\) is \(\kappa S_rD\), and its inverse
is \(\kappa^{-1}D^{-1}S_r^{-1}\). All scalar lines remain.
We keep the distinguished \(S_r\)-donor visit at every such
occurrence, even for \(r=1\), when \(S_1=I\).

The closed graph is the diagonal-path graph of the reduced matrix.
At a physical crossing follow its actual checked wire permutation.
For either sign its donor and recipient obey
\[
 a_{\rm in}=a_{\rm out}+n,\qquad
 b_{\rm out}=b_{\rm in}+n,\qquad
             0\le a_e\le d.
 \tag{2}
\]
The positive donor is the first input; the negative donor is the
second input. Thus both signs interchange their wire positions,
while retaining the stated directed transfer. Closing the remaining
output occupations to the same input occupations is exactly the
diagonal trace condition, not a new closure.

For an \(S_r\) or \(S_r^{-1}\) occurrence retain one donor junction
and its \(r-1\) recipient junctions. G's literal coefficient has
support
\[
 a_{\rm out}=a_{\rm in}-\sum_{j=2}^r n_j,\qquad
 b_{j,\rm out}=b_{j,\rm in}+n_j,\qquad
 n_j\ge0,\quad
 \sum_j n_j\le a_{\rm in},\quad b_{j,\rm in}+n_j\le d .
 \tag{3}
\]
The two signs have the same support. In G's notation their common
coefficient, up to the inverse's retained factor
\((-1)^{\sum n_j}Q^{(\sum n_j)(\sum n_j-1)/2}\), is
\[
 \prod_{j=2}^r
 x^{-(j-1)n_j}Q^{n_j\sum_{2\le i<j}b_{i,\rm in}}
       \frac{f_{b_{j,\rm in}+n_j}}{f_{b_{j,\rm in}}f_{n_j}} .
 \tag{4}
\]
Thus no intermediate transfer sum is being replaced by a fictitious
positive coefficient. Formula (4) is the exact matrix coefficient.
The diagonal \(D^{\pm1}\) changes no occupation.

Split crossings into their donor and recipient visits, and split an
\(S\)-junction into its donor and recipient visits with one directed
edge for each branch. The resulting finite directed graph is denoted
\(\Gamma\). Its wire edges form disjoint directed cycles; these are
the residual wire cycles. Every transfer goes from its donor visit
to its recipient visit. The conditions (2)--(3) are precisely
nonnegative integral circulation on \(\Gamma\), with capacity \(d\)
on every edge. A transfer's capacity follows already from its
incident wire capacities.

This graph retains the hard intermediate projectors as well. In a
physical crossing the donor decreases and the recipient increases
monotonically. In G's ordered factorization of \(S_r\), every partial
donor decrease is between zero and \(\sum_j n_j\), and each recipient
is raised only by its own \(n_j\). Therefore (2)--(3) imply all the
original intermediate bounds. No excursion is removed by replacing
a product of projected matrices with a projected product.

Write
\[
 T=(\text{number of physical crossing transfers})
          +(r-1)(\text{number of }S_r^{\pm1}\text{ occurrences}).
 \tag{5}
\]
Retain every occurrence, including inverse pairs if present.

## 2. Knot routing and a strict integral circulation

Every residual wire cycle contains an \(S\)-donor visit. To see this,
restore the removed first strand and replace each \(S/D\) occurrence
by its original \(R_1^{\pm1}\) wire crossing. The only change of
wire routing is the exchange of that removed strand with the donor
wire of the occurrence. A residual cycle avoiding every donor visit
is untouched by all these exchanges. It would remain a separate
closed component in the original braid, disjoint from the removed
strand. This contradicts the one-component closure.

The directed graph \(\Gamma\) is consequently strongly connected.
Within a residual cycle, every vertex reaches every other vertex by
following that directed cycle. If two residual cycles are distinct,
follow the first to one of its \(S\)-donor visits. At that occurrence
the second cycle occupies at least one recipient position: every
residual cycle meets every horizontal slice, and the donor belongs
to the first cycle. The corresponding \(S\)-branch is a directed
edge into the second cycle. This proves reachability in either
direction. For \(r=1\), the single wire cycle proves the assertion
without transfer edges.

There is an explicit positive integral circulation on this graph.
For each directed edge \(e\), choose a directed return path from its
target to its source and sum the edge-count circulations of all
these closed walks. Call the result \(v\). Then
\[
                  v_e\in\mathbb Z_{\ge1},\qquad \partial v=0.
 \tag{6}
\]
It depends only on the fixed finite graph. Put \(V=\max_e v_e\).
For \(d\ge4V\), the integer circulation
\[
              a_e=\left\lfloor\frac d{2V}\right\rfloor v_e
 \tag{7}
\]
satisfies
\[
                   \frac d{4V}\le a_e\le\frac d2
                          \quad\text{for every edge}.
 \tag{8}
\]
Equations (2)--(4) therefore give a genuine strict interior point
of the actual reduced finite path support at every sufficiently
large level. At the complete root the factors in (4), and the
literal supported crossing factors, are nonzero. This establishes
a supported path, not noncancellation of its matrix entry or source.

The result is stronger than connectedness of the undirected
incidence graph. It uses the donor position of each actual \(S\)
occurrence and the one-component original routing.

## 3. The geometric clock-one rules at a full \(S\)-junction

Now fix the resolved geometric reduced correspondence supplied by G.
Work at completeness \(x=-1\). Assume, as in its regular-total chart,
that every retained physical \(f\) and \(K\) is a unit at the stage
boundaries, all the displayed partial \(T_j\)'s below are units,
and
\[
                            K_\Sigma^2\ne1.
 \tag{9}
\]
For complete discrete faithful holonomy G supplies this chart after
its prescribed source-preserving presentation changes. No physical
integer state is inferred from that existence.

Let \(I\) be the set of graph wires whose geometric occupation
clock \(A\) is one and graph transfer edges whose geometric transfer
clock is one. Since \(f\) is a unit, use the regular identity
\[
                  p=(1-A)/f.
 \tag{10}
\]
Thus \(A=1\) is equivalent to \(p=0\) and to \(e=0\) on this
complete chart. It is the row-type zero pattern; no division by
\(p\) at its zero is made.

For an \(S_r\) occurrence G proves
\[
 z_j=(p_{\rm d}/x)K_2^{-1}\cdots K_{j-1}^{-1}f_j,\qquad
 T_j=1-\sum_{\ell\ge j}z_\ell,\qquad T_{r+1}=1,
 \tag{11}
\]
\[
 C_j=T_j/T_{j+1},\qquad
 A_{\rm d}'=A_{\rm d}/T_2,\quad p_{\rm d}'=p_{\rm d},
 \qquad A_j'=A_jC_j,\quad f_j'=f_j/T_{j+1}.
 \tag{12}
\]
Every partial denominator in (11)--(12) is retained. The hypotheses
make them units; they have not been canceled from a singular chart.
Consequently
\[
 C_j=1\ \Longleftrightarrow\ z_j=0\
 \Longleftrightarrow\ p_{\rm d}=0\
 \Longleftrightarrow\ A_{\rm d}=1.
 \tag{13}
\]
The donor's zero status is preserved by (10),(12), using its unit
input and output \(f\). If \(C_j=1\), the recipient's zero status
is preserved. Conversely, if both recipient clocks are one,
\(A_j=A_j'=1\) forces \(C_j=1\). These are statements at the
full junction; they do not assume unit factorial logarithms at
every intermediate donor position.

The inverse graph gives the same assertions for \(S_r^{-1}\).
Its physical transfers still have support (3). Reversing (12)
inverts the relevant clock ratios, which does not change whether
they are one. The diagonal \(D^{\pm1}\) fixes \(A\) and multiplies
\(p\) by a unit, so it preserves zero status.

For the two physical crossing signs, C proves the same rules from
the literal signed Gauss equations:

* donor wire zero status is preserved, and its transfer is in \(I\)
  exactly when the donor wires are in \(I\);
* a transfer in \(I\) preserves recipient zero status;
* if both recipient wires are in \(I\), its transfer is in \(I\).

The last implication uses C's actual complete Casimir and its
squared receiver formula, with the nonzero \(f\) and denominators
retained. Thus these rules hold at every vertex of \(\Gamma\).

## 4. The geometric pattern has an open wire run

Assume \(I\) is nonempty. The transfer rules imply that some wire
belongs to \(I\). We show that at least one residual wire cycle
contains both an \(I\)-wire and a non-\(I\)-wire.

Suppose instead that \(I\)-wires are a union of whole residual
cycles, and choose one such cycle. At every \(S\)-occurrence this
cycle occupies some head. If that head is the donor, the donor
is in \(I\). If it is a recipient, both its incident wires are
in \(I\), so (13) again forces the donor into \(I\).
Hence every \(S\)-donor visit is in \(I\).

Section 2 shows that every residual wire cycle visits an \(S\)
donor. Under the supposition that a cycle is wholly in or wholly
outside \(I\), every cycle is therefore wholly in \(I\). At any
horizontal slice all remaining occupation clocks then equal one.
But G's resolved level has
\[
                       K_\Sigma=xK_{\rm r}.
 \tag{14}
\]
As \(K_j=x/A_j\) and \(x=-1\), all these clocks being one gives
\(K_\Sigma=x^m\), hence \(K_\Sigma^2=1\), contradicting (9).
For \(r=1\) the same last contradiction applies directly.

It follows that there is an open maximal run of \(I\)-wires.
Whole \(I\)-cycles may coexist with it and remain in the proof
below. No claim that such whole cycles are individually forbidden
has been used.

## 5. Exact endpoint propagation, with all whole cycles retained

For every wire or transfer index define
\[
                         D_e=\min(a_e,d-a_e).
 \tag{15}
\]
Let \(\omega\ge0\) satisfy \((T+2)\omega<d\). We prove
\[
 \boxed{\quad
 I\ne\varnothing,\quad D_i\le\omega\ (i\in I)
 \quad\Longrightarrow\quad
          D_e\le\omega\text{ for at least one }e\notin I .
 \quad}
 \tag{16}
\]
Each index in \(I\) may independently use its lower or upper
endpoint band. In particular every long unit-transfer alias
remains in the hypothesis.

Assume for contradiction that every edge outside \(I\) is strictly
between \(\omega\) and \(d-\omega\). A birth or death of an
\(I\)-run cannot be a donor or a \(D\)-visit, since they preserve
zero status. It is a recipient with transfer outside \(I\).
At a birth, its incoming wire and transfer are both \(>\omega\);
therefore the first \(I\)-wire value \(A_\ell\) is \(>2\omega\).
Its endpoint-band condition forces \(A_\ell\ge d-\omega\).
At a death, the last \(I\)-wire value is
\(B_\ell=a_{\rm out}-n<d-2\omega\); its endpoint-band condition
therefore forces \(B_\ell\le\omega\).

There are \(s\ge1\) open runs by Section 4. Thus
\[
                    \sum_{\ell=1}^s(A_\ell-B_\ell)
                                     \ge s(d-2\omega).
 \tag{17}
\]
Telescope the exact flow equations on all open runs and on every
whole \(I\)-wire cycle. A full \(S\)-donor contributes
\(\sum_j n_j\), retaining every branch separately. At every
internal \(I\)-visit all its incident transfer edges are in \(I\).
Every \(I\)-transfer starts at an internal \(I\)-donor; its recipient
has either two \(I\)-wires or two non-\(I\)-wires.

Transfers of the first kind cancel in the total telescope, including
those between distinct runs or whole cycles. Whole cycles have no
endpoint term. If \(\mathcal E\) denotes the \(I\)-transfers ending
at two non-\(I\) recipient wires, the exact result is
\[
                  \sum_{\ell=1}^s(A_\ell-B_\ell)
                                     =\sum_{e\in\mathcal E} n_e .
 \tag{18}
\]
At such a recipient, \(n_e=a_{\rm out}-a_{\rm in}<d-2\omega\).
The upper alternative \(n_e\ge d-\omega\) is impossible.
Since \(e\in I\), it follows that \(n_e\le\omega\).
There are at most \(T\) such transfers. Equations (17)--(18) give
\[
                          s(d-2\omega)\le T\omega,
 \tag{19}
\]
contradicting \(s\ge1\) and \((T+2)\omega<d\). This proves (16).

Birth and death transfers have not been dropped; they determined
the endpoint values in (17). Nor were internal long transfers
estimated as small: they canceled exactly in (18). The proof also
applies at \(\omega=0\).

## 6. Source scope

Let \(S_N\) denote the actual reduced closed finite path support.
For \(I\ne\varnothing\) and \((T+2)\omega<d\), the conclusion
is the literal inclusion
\[
 S_N\cap\bigcap_{i\in I}\{D_i\le\omega\}
                \ \subseteq\
                   \bigcup_{e\notin I}\{D_e\le\omega\}.
 \tag{20}
\]
Ordering the non-\(I\) edges partitions the left side by the first
additional boundary edge, keeping its lower/upper choice and all
previous exclusions. No amplitude or current is deleted by this
partition. If \(I\) is empty, (16),(20) assert nothing; the strict
physical interior from Section 2 still exists.

The positive circulation construction and (20) have different
roles. The first proves nonempty physical support. The second
shows that the specified resolved geometric endpoint pattern
cannot be placed in isolation in that support. It does not put
the geometric point on an original Fourier or cotangent contour,
nor does it prove that the extra boundary terms cancel.

All statements concern the actual reduced root-\(q\) network with
its original scalar lines and Cartan-weighted meridian source.
Fixed-\(q\) meridian differentiation keeps these finite support
constraints. Quantum normals and inserted coupons may carry the
additional or affine rows specified in G's source; their supports
must be retained and checked separately. No full quantum-normal
identity is obtained by differentiating the root reduction.

In particular this theorem supplies neither an endpoint packet
nor a lower bound for a source contraction. The \(S\)-branch zero
in (11) is linear in \(p_{\rm d}=(1-A_{\rm d})/f_{\rm d}\);
it is not automatically the quadratic Casimir zero of an original
crossing Euler product. Their analytic transition estimates must
not be identified merely because both clocks tend to one.

## Complete direct-source pins

* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.
* C: notes/research_geometric_endpoint_boundary_propagation.md,
  SHA256 cda3efe3cf89267f9a3a351e1ad0d2a07f09c24ea3d10ee45fbb1d9ea11bb3c0.

Both complete directs were read nontruncated in this active author
sequence. Every used support, signed zero-status and resolved
chart implication was checked. Only written mathematics and
text/hash operations were used. Frozen and public files are unchanged.
