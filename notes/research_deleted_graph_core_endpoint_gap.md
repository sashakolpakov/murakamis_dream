# A deleted-graph core gives a uniform endpoint-angle gap

Private written proof, 17 November 2026.

The incidence-preserving completion test in [W] can fail because
the surviving angles are kept fixed. Here they are allowed to move.
An explicit contraction and restoration constructs a parent-unit
angle assignment whose surviving energy is no larger. This proves
a uniform strict gap for the whole closed endpoint-angle maximum
whenever all selected middle-edge endpoints lie in the relative
two-core of the deleted graph. Complete outside vertices are anchors
in this graph criterion.

In particular every pattern with no selected middle-incidence
count one is covered: counts two, three and all larger counts
are treated together.
The conclusion is a classical angle comparison, not a bound on a
quantum endpoint source.

## 1. The original angle problem and endpoint pattern

Use precisely the data of [W]. The finite graph has selected
vertices \(S\), complete outside vertices \(B\), and included
edges \(E\), each with a selected endpoint. Every selected vertex
has an original incidence. Parallel edges and loops are allowed;
a loop has two distinct incidences. The powers \(n_v\) are fixed
real signed numbers; integral powers are included.

For an oriented edge \(e=(v,w)\), the original square coordinates
are
\[
 A_P=s_v/4-g_{w,e}/2,\quad A_Q=s_v/4+g_{w,e}/2,\qquad
 y_P=g_{v,e}/2+s_w/4,\quad y_Q=g_{v,e}/2-s_w/4.
 \tag{1}
\]
At a loop the two incidence variables are distinct although
the two real vertex angles agree. Outside \(s_b=0\).
The closed angle inequalities are
\[
 |s_v|\le\pi,\qquad
 |s_v|+2|g_{w,e}|\le\pi,\qquad
 |s_w|+2|g_{v,e}|\le\pi.
 \tag{2}
\]
They express the two closed squares in (1). Write
\[
 \mathcal E(X)=4\sum_e(E_{P,e}+E_{Q,e}),\qquad
 \rho_v(X)=\sum_{e\ni v}g_{v,e}-n_vs_v/2,
 \qquad M_\infty=4G_{\rm Cat}/\pi.
 \tag{3}
\]
The square energy is continuous and convex on its closed square,
strictly convex in the interior, and invariant under simultaneous
negation of its two coordinates [S].

Assume a supplied positive parent solution \(X^*\) has the
original complex unit equations and their original branches.
Then [W] gives
\[
 \rho_v(X^*)=-\pi,\qquad
 d\mathcal E(X^*)=\sum_{v\in S}h_v^*\,d\rho_v,\qquad
 M_G=|E|M_\infty-\mathcal E(X^*)/\pi.
 \tag{4}
\]
Its ambient Bregman remainder is
\[
 D_*(X)=\mathcal E(X)-\mathcal E(X^*)
                       -d\mathcal E(X^*)(X-X^*).
 \tag{5}
\]
It is nonnegative on the closed angle body, and zero only at
\(X^*\). In the Euclidean vector of all square coordinates,
\[
 D_*(X)\ge\kappa\|X-X^*\|_2^2,\qquad
 \delta=\min_\nu(\pi/4-|X_\nu^*|)>0,\qquad
 \kappa=\frac{\delta}{\pi}\sin^2\delta.
 \tag{6}
\]
The original one-edge angle-volume is
\[
 V_e(X_e)=8G_{\rm Cat}-8(E_{P,e}+E_{Q,e})\ge0.
 \tag{7}
\]
It is strictly positive when both squares are interior.
All constants in (4)--(7) are those of [W].

Choose disjoint sets of deleted zero and middle edges
\(E_0,E_m\), with \(D=E_0\cup E_m\ne\varnothing\).
Let \(m_v\) count middle incidences at \(v\).
The closed boundary-angle fiber \(\mathcal B_D\) retains every
selected vertex, all surviving incidences, and
\[
 |s_v|\le\pi,\qquad
 \sum_{\substack{e\ni v\\e\notin D}}g_{v,e}-n_vs_v/2
                           =-\pi(1-m_v/2).
 \tag{8}
\]
It also retains (2) on surviving edges. Isolated vertices
keep both the angle bound and their empty-incidence row.
For \(X_B\in\mathcal B_D\), put
\[
 M_B(X_B)=(|E|-|D|)M_\infty-\mathcal E_B(X_B)/\pi.
 \tag{9}
\]
This is the original closed angle action from [W]. When a
regular positive critical realization of the displayed endpoint
phase is supplied, it is that phase's calibrated real action.
No critical realization is assumed below.

## 2. A combinatorial completion set

Let \(P\subset S\) be all selected endpoints of middle edges.
A completion set is a subset \(C\subset S\) such that
\[
 P\subset C,\qquad
 d_C(v):=\#\{D\text{-incidences at }v
              \text{ whose opposite end lies in }C\cup B\}
                                  \ge2\quad(v\in C).
 \tag{10}
\]
Counts include multiplicities and both incidences of a loop.
There is no degree requirement at an outside vertex. If
\(E_m=\varnothing\), the choice \(C=\varnothing\) is allowed.
The criterion depends only on the deleted graph, not on an
angle assignment or the powers.

**Theorem.** If a completion set exists, then every member of
\(\mathcal B_D\) satisfies
\[
                         M_B(X_B)\le M_G-\varepsilon_*,
 \tag{11}
\]
with the same parent-dependent constant for every such pattern:
\[
 \varepsilon_*=
 \min\left\{\frac{\kappa\delta^2}{4\pi},
                         \frac{V_\delta}{2\pi}\right\}>0.
 \tag{12}
\]
Here \(V_\delta\) is the minimum of the unnormalized
one-edge volume (7) over four square coordinates with
\(|X_\nu|\le\pi/4-\delta/2\). This is a positive minimum
on a compact interior set. The boundary fiber can be empty;
no assignment is asserted in that case. Otherwise it is
compact, so its entire angle maximum obeys (11).

### Energy decreases when a vertex block is centered

At a surviving selected vertex its block is
\[
               (s_v,(g_{v,e})_{e\notin D,\ e\ni v}).
 \tag{13}
\]
Negating one block preserves the surviving energy and
every weak edge inequality. If \(v\) is the first end
of a nonloop edge, the two square pairs in (1) become
\((-A_Q,-y_Q)\) and \((-A_P,-y_P)\). If it is the
second end, they are exchanged. For a loop at \(v\),
both square pairs are simultaneously negated. These
operations preserve the sum of square energies.

The midpoint of an assignment and this reflected assignment
sets exactly the chosen block to zero. Convexity therefore
shows that this centering cannot increase the energy.
It remains inside the weak angle body. Different vertex
blocks use distinct coordinates and their centerings commute.
An isolated block has no edge energy and causes no exception.

Center every block in \(C\), and denote the resulting
surviving assignment by \(Y_B\). Thus
\[
                         \mathcal E_B(Y_B)\le\mathcal E_B(X_B).
 \tag{14}
\]
Rows at vertices outside \(C\) have not changed. Rows in
\(C\) are temporarily zero. They need not be the boundary
rows (8); retaining those intermediate rows is not required
for the parent comparison.

### Explicit restoration of the parent rows

Retain the centered surviving coordinates and restore deleted
incidences as follows:
\[
 g_{v,e}=
 \begin{cases}
 -\pi/d_C(v),&
       v\in C,\ e\in D,\ \text{opposite end in }C\cup B,\\
 0,&\text{every other deleted incidence}.
 \end{cases}
 \tag{15}
\]
In particular every deleted outside incidence is zero.
Call the full resulting assignment \(X\).

Every nonzero incidence in (15) has an opposite real angle
zero: all selected angles in \(C\) were centered, and all
outside angles were already zero. Its magnitude is at most
\(\pi/2\) by (10). Hence its inequality in (2) holds.
At every zero incidence the inequality is just the retained
bound on the opposite angle. Surviving edges already obey
(2). This proves feasibility of all original weak squares,
including loops and edges crossing from \(C\) to \(S\setminus C\).

At \(v\in C\), the surviving incidences and real angle are
zero. Its \(d_C(v)\) restored usable incidences sum to
\(-\pi\), so its parent row is exactly \(\rho_v=-\pi\).
If \(v\in S\setminus C\), then \(m_v=0\) because \(P\subset C\).
Its surviving row in (8) was already the unit row and was
unchanged by centering. Its restored incidences are zero.
Thus it too has \(\rho_v=-\pi\). No row is imposed or
needed at an outside vertex. The construction restores
every selected parent row, including any isolated survivor.

### The exact comparison and uniform margin

Since \(X\) and \(X^*\) have the same rows, the affine
term in (5) vanishes. Adding and subtracting the centered
surviving energy gives the exact identity
\[
 \boxed{\quad
 M_G-M_B(X_B)=\frac{D_*(X)}{\pi}
    +\sum_{e\in D}\frac{V_e(X_e)}{2\pi}
    +\frac{\mathcal E_B(X_B)-\mathcal E_B(Y_B)}{\pi}.
 \quad}
 \tag{16}
\]
Indeed the volume sum is
\(|D|M_\infty-\mathcal E_D(X)/\pi\), and
\(\mathcal E(X)=\mathcal E_D(X)+\mathcal E_B(Y_B)\).
Substitution of (5),(9) proves (16) with all constants.

All three terms in (16) are nonnegative. If
\(\|X-X^*\|_2\ge\delta/2\), (6) gives the first
alternative in (12). Otherwise every square coordinate
has margin at least \(\delta/2\); any one edge of the
nonempty set \(D\) has volume at least \(V_\delta\),
giving the second alternative. This proves (11),(12).
Neither a sign for the powers nor a parent-height estimate
was used. \(\square\)

## 3. The relative two-core and concrete corollaries

There is a canonical finite way to test (10). Start with
the deleted graph \(D\), retaining all outside vertices
as anchors. Repeatedly remove a selected vertex of current
deleted degree zero or one, together with its incident
deleted edges. Never remove an outside vertex. Degrees
count loop incidences twice. Let \(C_*\) be the selected
vertices left when no such removal is possible.

This set is independent of the order of removals.
To prove it, let \(C\) be any selected set with the
degree property in (10), temporarily ignoring \(P\).
No first member of \(C\) can be removed: until that
event, all its incidences toward \(C\cup B\) are still
present and give degree at least two. Thus every such
\(C\) survives every removal sequence. The terminal
set itself has this degree property. It therefore
contains every other such set and is the unique largest
one. Every removal sequence has this same terminal set.
This proves both order independence and the equivalence
\[
        \text{a completion set exists}
                    \quad\Longleftrightarrow\quad P\subset C_*.
 \tag{17}
\]
The procedure is only a graph description; no computational
experiment or knot-by-knot test enters the theorem.

Several consequences retain the same constant (12).

* Every pure-zero pattern is covered by \(C=\varnothing\).
  Here no centering is needed and all deleted incidences
  are restored as zero, recovering the unchanged-row
  comparison in [W].
* If every selected \(m_v\) is zero or at least two,
  take \(C=P\). Every middle incidence at \(v\in C\)
  has its opposite end in \(C\cup B\), so
  \(d_C(v)\ge m_v\ge2\). This includes middle branching
  of degree three as well as cycles and paths whose
  selected endpoints have two incidences. Paths may
  end at complete outside vertices.
* Zero edges can provide the second usable incidence
  even at a selected middle-degree-one vertex. The full
  condition is (17), not the middle degree alone.
  Loops and parallel edges count literally in both tests.

The original assignment need not satisfy [W]'s
incidence-preserving capacity test. This proof moves
the surviving vertex blocks and explicitly pays their
energy change in (16). If a middle endpoint is removed
by the pruning procedure, this particular trial does
not apply. No reversed action inequality is inferred.

## 4. Source scope and direct sources

The parent may be any fixed original graph and signed-power
assignment with the stated positive unit solution. The
boundary assignments range over the whole closed angle
fiber, not only its geometric critical points. The result
does not establish positive parent geometry for an
arbitrary hyperbolic short filling. Nor is the trial
asserted to be a matched complex deformation or to
preserve boundary criticality during centering.

In particular this is not a quantum source deletion,
an estimate for all endpoint currents, or a selected-cycle
noncancellation theorem. The actual finite middle
polynomial, its other exponential, full normals, aliases,
angular closing and relative currents remain as in [W].
The graph criterion is sufficient for the stated
angle-action maximum; it assigns no zero rate or zero
source to an empty angle fiber.

Both complete direct texts were read in full and their
used implications checked:

* [W: Wire-endpoint angle action and uniform comparison constants](research_wire_endpoint_angle_comparison.md),
  SHA256 1c5abe425060f9d8f891bd72e260d912b2132b4c9ab270e813bd964551af7568.
* [S: Original block reflection and ambient convex energy](research_split_current_convex_action_gap.md),
  SHA256 8e42b3e549cebd45fa301ae3c41858ab2def475fa072985a49f5bc639ee204dc.

The complete edge-cut comparison, saturated-angle-face
energy and retained-boundary leaf profile were also read
for coverage. Their distinct vertex deletions and
infimal-projection criteria have not been enlarged.
Only written mathematics, source reads and hashes were
used. No mathematical program, numerical experiment,
test or build was run. Frozen notes and public papers
are unchanged.
