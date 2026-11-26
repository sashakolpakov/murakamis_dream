# Integral square coherence for actual auxiliary closure homotopies

Private written proof, 19 November 2026.

Two specified closure-probe homotopies give an integral second
relation before evaluating the source. The proof follows their
crossing walls and retains the resolved inter-probe crossings.
It does not cancel a potentially torsion parameter in a skein
module. A local cubical complex supplies all disjoint comparison
cells; the global construction here supplies the two-probe square.

The sole complete direct is C, the actual skein-corrected closure
source. It supplies the capped fundamental probes, the original
pointed evaluation, and the one-probe framing and source rows.
All chain definitions and the two-parameter construction are below.
No acyclicity, flatness, geometric nonzero class, or complete
derived comparison is claimed.

## 1. The free comparison complex and its actual source

Use C's marked parameters
\[
 A=q^{1/2}=e^{\pi i/(2N)},\quad q=e^{\pi i/N},\quad N\ge2,
 \qquad \delta=A-A^{-1},\qquad \theta=-A^3.
 \tag{1}
\]
For the chain definitions first regard \(A\) as a formal
Laurent variable and put \(R=\mathbb Z[A,A^{-1}]\).
Fix the original physical closed braid and its pointed cut.
All auxiliary ribbons below are disjoint from that core and
carry its actual fundamental color.

Let \(C_0\) be the free \(R\)-module on finite framed auxiliary
link diagrams in this fixed complement, up to ambient framed
isotopy fixing the physical core and its cut. The inherited
framing and all stages along the physical braid are part of
the datum. No skein relation has yet been imposed on \(C_0\).
In particular \(C_0\) has no \(\delta\)-torsion.

A crossing-comparison box has four fixed ribbon ends and the
three local replacements \(+\), \(-\), and
\[
                           s=I-e.
 \tag{2}
\]
The last is a linear combination of the two actual smoothings,
with the signs and ribbons of C's fundamental crossing identity.
An oriented one-box generator \(E(D)\) has boundary
\[
                  dE(D)=D_+-D_- -\delta D_s.
 \tag{3}
\]
Reversing its orientation reverses this boundary.
If a smoothing merges or splits components, that is the actual
new diagram. Component labels are not imposed after reconnection.

We also allow an even-framing comparison box on a fixed arc.
For any integer \(h\), define
\[
 p_h(A)=\frac{A^{6h}-1}{\delta}\in R,\qquad
 dT_h(D)=D^{(2h)}-D-\delta p_h(A)D.
 \tag{4}
\]
The notation \(D^{(2h)}\) retains \(2h\) ribbon twists on that arc.
For example \(p_1=A(1+A^2+A^4)\); the formula for negative \(h\)
is still Laurent polynomial. Only even repairs are written in
this form: \(\theta(1)=-1\) prevents replacing a single twist
by a \(\delta\)-multiple of an unframed diagram.

For \(k\ge1\), let \(C_k\) be free over \(R\) on framed staged
diagrams with \(k\) ordered, pairwise disjoint comparison boxes
of these two types. Each unresolved box is a formal relation
generator, not an additional evaluated operator. Quotient only
by framed isotopies that preserve the ordered local data.
Replacing box \(j\) by its boundary combination defines \(d_j\).
Set
\[
                     d=\sum_{j=1}^k(-1)^{k-j}d_j:C_k\longrightarrow C_{k-1}.
 \tag{5}
\]
Replacement is linear, so (2) and (4) also make sense when
another box has already produced a linear combination.

**Local complex.** One has \(d^2=0\) in every degree.

Indeed replacements in two disjoint boxes commute as
modifications of the framed diagram, including every reconnection.
In \(d^2\), the two orders of each pair occur with opposite
signs in (5). They therefore cancel term by term in the free
module. This argument does not require commuting matrix
operators at a common stage, nor a fixed number of components.
It is a statement about disjoint local replacements.

For a fixed level, C's actual decorated evaluation defines
\[
 {\rm Ev}_{N,\mu}:C_0\longrightarrow
       \{\hbox{original meridian source germs}\},\qquad M=e^\mu.
 \tag{6}
\]
The coefficient \(A\) is evaluated at (1). The local fundamental
identity \(\check R-\check R^{-1}=\delta(I-e)\) annihilates
(3), and the actual twist \(\theta=-A^3\) annihilates (4).
Thus \({\rm Ev}_{N,\mu}\circ d=0\) on \(C_1\).
It is an augmentation of this chain complex by the actual
source. Every fixed \(\mu\)-derivative is also an augmentation.
All core scalars, pivots, caps and auxiliary framings remain.
An outside normalization line is multiplied into every term
before differentiation.

The complex just defined is a free comparison complex. We do
not identify its homology with the full skein module or with
a character-ring resolution.

## 2. The integral local square

For two crossing boxes use \(D_{ab}\), where \(a,b\) can be
\(+,-,s\). Let \(E_1(b)\) mark the first box with the second
already replaced by \(b\), and define \(E_2(a)\) similarly.
The two-box generator has boundary
\[
 \boxed{\quad
 dD_{\square}
 =E_1(+)-E_1(-)-E_2(+)+E_2(-)
                   +\delta\bigl(E_2(s)-E_1(s)\bigr).
 \quad} \tag{7}
\]
This is (5) with \(k=2\), with its indicated orientation.
Its boundary is exactly zero in \(C_0\): expanding (3), the
four corner diagrams cancel, the single-resolution diagrams
cancel, and the two double-resolution terms are equal.
The same formula, with the corresponding local correction
in place of \(s\), applies to a crossing/repair or repair/repair
pair. It follows directly from (4)--(5).

For later use write
\[
 \begin{split}
 H_\square&=E_1(+)-E_1(-)-E_2(+)+E_2(-),\\
 K_\square&=E_2(s)-E_1(s),\\
 C_\square&=D_{s,+}-D_{s,-}-D_{+,s}+D_{-,s}.
 \end{split} \tag{8}
\]
Then direct expansion gives
\[
 dH_\square=-\delta C_\square,\qquad
 dK_\square=C_\square,\qquad
 dD_\square=H_\square+\delta K_\square.
 \tag{9}
\]
In the middle identity the double-resolution terms cancel
without dividing by \(\delta\).
This is the local second relation that will be assembled globally.

## 3. Two actual probe homotopies and their crossing walls

Choose two instances of C's closure relation, indexed \(1,2\).
For each one the two endpoint probes represent words
\(\beta(h_i)w\) and \(h_iw\), with the fixed negative based
probe convention. Their endpoints have zero self-framing.
Place the first and second endpoint probes in two ordered,
separate initial stages above the same physical braid.
There are four specified ordered corner links \(L_{00}\),
\(L_{10}\), \(L_{01}\), \(L_{11}\).

Choose based homotopies \(F_1(u,s)\) and \(F_2(v,t)\) in the
fixed physical complement, for \(0\le s,t\le1\).
Here \(u,v\) are circle parameters along the probes.
They are chosen relative to fixed small based arcs.
C proves existence and gives finite generic one-parameter
homotopies through immersed curves. Choose carried ribbon
fields along them, extending the specified initial ribbons.
For now keep the carried endpoint framings rather than
resetting them to zero. Their product family is
\[
                       L(s,t)=F_1(\,\cdot\,,s)\ \cup\
                                  F_2(\,\cdot\,,t).
 \tag{10}
\]
The entire compact family stays disjoint from the physical core.

After a relative perturbation the discriminant in the parameter
square has the following elementary form.

* Self-double events of \(F_1\) give vertical walls, and those
  of \(F_2\) give horizontal walls.
* Mutual collisions satisfy \(F_1(u,s)=F_2(v,t)\). Their locus
  has dimension \(4-3=1\). Parallel branch tangents impose two
  further conditions and can be avoided. The projection to the
  \((s,t)\)-square is then an immersion: a tangent with
  \(ds=dt=0\) would satisfy
  \(F_{1,u}\,du-F_{2,v}\,dv=0\), hence \(du=dv=0\).
* Intersections of two projected walls are isolated transverse
  intersections corresponding to two distinct double points.
  Their crossing balls are disjoint. A triple collision would
  involve three curve parameters and two family parameters,
  subject to six equalities, and is generically absent.

The factors in (10) remain immersions; their derivatives in
\(u\) or \(v\) never vanish. Ordinary tangencies of an immersed
wall to a horizontal or vertical coordinate line are harmless.
Choose the boundary to avoid wall vertices. Compactness and
transversality make the resulting wall graph finite, after
subdividing its smooth compact arcs if necessary.

Crossing signs coorient the walls. For a mutual wall the two
branches retain their two probe labels. For a self wall, swapping
the branches reverses both the separation vector and the
tangent cross product, so it does not change this coorientation.
Use the full inherited ribbons in every resolution. Local
crossing-ball charts may be chosen on finitely many wall
intervals, with their framed transition isotopies retained.
The two endpoint pairings defining the smoothings survive branch
interchange. On a closed wall, the carried ribbon data return
to the same data; no new zero-framing choice is made. Hence the
resolved diagram and relation generator close in their framed
isotopy classes. This excludes an unrecorded smoothing-band twist.

## 4. Assembly of the global second relation

Orient the boundary clockwise in the ordered coordinates \((s,t)\),
so its local coordinate model is \(H_\square\) in (8).
For each oriented
edge \(e\), collect its signed crossing events as a chain
\(H_e\in C_1\), and its signed smoothing combinations as
\(C_e\in C_0\). C's one-parameter construction, now with the
other probe present, gives
\[
                  dH_e=L_{\mathrm{end}(e)}
                         -L_{\mathrm{start}(e)}-\delta C_e.
 \tag{11}
\]
The crossing events include mutual crossings of the two probes.
They cannot be discarded as independent commuting loop factors.
Put
\[
                         H_\partial=\sum_{e\subset\partial[0,1]^2}H_e,
 \qquad C_\partial=\sum_{e\subset\partial[0,1]^2}C_e.
 \tag{12}
\]
The corner terms cancel, so \(dH_\partial=-\delta C_\partial\).
This alone would not permit division by \(\delta\) in a skein
quotient. The actual wall graph gives more.

Along a wall segment between vertices, the marked crossing
configuration varies by a framed isotopy. Thus the two endpoint
occurrences of that relation generator cancel with opposite
signs when wall segments are summed. The same holds for the
inherited smoothing combinations. Closed walls contribute no
endpoint. At a transverse wall vertex, identify its two disjoint
crossing balls with the local square of Section 2. Let
\(\varepsilon_p=\pm1\) record its orientation relative to (7).
The four incident wall segments contribute exactly
\(\varepsilon_p H_{\square,p}\). Therefore, after all segment
cancellations,
\[
 H_\partial=\sum_p\varepsilon_p H_{\square,p},\qquad
 C_\partial=\sum_p\varepsilon_p C_{\square,p}.
 \tag{13}
\]
These are equalities in the free framed-diagram modules.
They follow by following every oriented wall arc, not by
canceling a parameter in the evaluated source.

Define finite chains
\[
                 P=\sum_p\varepsilon_p D_{\square,p}\in C_2,
 \qquad K=\sum_p\varepsilon_p K_{\square,p}\in C_1.
 \tag{14}
\]
Equations (9) and (13) prove the global integral identities
\[
 \boxed{\qquad dP=H_\partial+\delta K,\qquad
                         dK=C_\partial. \qquad} \tag{15}
\]
Every double-resolved diagram is retained. In particular (15)
exhibits an actual second boundary with the prescribed
one-homotopy boundary chain as its leading term.
The divided curvature \(C_\partial\) is an explicit first
boundary, not merely an element whose \(\delta\)-multiple
vanishes in a quotient.

## 5. Restoring the specified zero-framed corners

The carried framing at the endpoint of homotopy \(i\) differs
from its specified endpoint framing by \(2h_i\) twists, by C's
one-probe parity calculation. Thus the four carried corners
are consistent, but need not be the four prescribed zero-framed
corners.

Choose the fixed based arcs and small repair balls disjoint
from both homotopies away from those arcs. This can be arranged
when choosing the based homotopies: the other compact
two-dimensional trace can avoid the basepoint and then a small
ball around it. Append the comparison generator (4) to each
one-probe path to perform its actual endpoint repair, with its
orientation chosen as needed.

The product square of the two extended paths decomposes into
the carried square, crossing/repair rectangles, and a
repair/repair rectangle. Their comparison boxes are disjoint
on the fixed based arcs. Add their two-box generators from
(5),(7) to \(P\), and their resolved-edge terms to \(K\).
Internal path edges cancel exactly. The remaining boundary
is now the four paths with the prescribed zero-framed corner
diagrams, and the identities (15) still hold.

This is an integral repair using
\(\theta^{2h_i}-1=\delta p_{h_i}(A)\).
It neither discards the factors \(A^{6h_i}\) nor uses an odd
twist as a small correction. All mutual probe crossings and
all inherited framings after smoothing remain in the chains.

Applying the actual augmentation to the second identity in
(15) gives, at every level and throughout the meridian germ,
\[
                       {\rm Ev}_{N,\mu}(C_\partial)=0.
 \tag{16}
\]
All fixed true \(\mu\)-jets satisfy the same equality. The
first identity in (15) supplies the integral chain-level
explanation of this source coherence. The fact that
\(\delta_N\ne0\) is not used to construct \(K\) or \(P\).

## 6. The endpoint-labelled Koszul row and its limits

For closure move \(i\), let \(\ell_i^+\) and \(\ell_i^-\)
denote its two bounded initial probe symbols, including the
minus trace from the left auxiliary pivot. Put
\[
                          f_i=\ell_i^+-\ell_i^-.
 \tag{17}
\]
C identifies \(f_i\), up to that retained common sign, with
the corresponding classical mixed closure trace.
At an ordered two-probe corner, the two initial contractions
are products of bounded intertwiner coupons. Their complete-root
principal expression is \(\ell_1^{\eta_1}\ell_2^{\eta_2}\);
no commutation of the actual coupons is being asserted.

There is a precise, limited endpoint-history interpretation of
(15). Before identifying any chain generators, take the free
module on the four edge-history occurrences
\(\mathbf h_{1,+},\mathbf h_{1,-},\mathbf h_{2,+},\mathbf h_{2,-}\).
Each occurrence denotes traversal in its increasing coordinate,
independently of the orientation of the square boundary.
There is an \(R\)-linear map sending it to that specified
positive-coordinate history chain. Distinct occurrences remain
distinct in this free bookkeeping module even if their images
reuse the same local generators in \(C_1\).

After the marked specialization \(A=1\), assign these four
occurrences the labels \(\ell_2^+e_1,\ell_2^-e_1,
\ell_1^+e_2,\ell_1^-e_2\), respectively. The labels take values
in two formal copies of the bounded classical endpoint-function
space. With the square orientation of (7), the boundary history
\(\mathbf h_{1,+}-\mathbf h_{1,-}-\mathbf h_{2,+}
+\mathbf h_{2,-}\) has label
\[
                  (\ell_2^+-\ell_2^-)e_1
                    -(\ell_1^+-\ell_1^-)e_2
                           =f_2e_1-f_1e_2.
 \tag{18}
\]
Its formal boundary under \(e_i\mapsto f_i\) is zero.
The history maps to \(H_\partial\), and (15) identifies
\(dP\) with that image modulo the displayed \(\delta K\).
The even repairs also contribute no additional label at \(A=1\).
Thus the specified boundary-history lift of the genuine
integral second relation has the first Koszul row as its label.

This label assignment is not asserted to descend through the
history map, or to define a module map from all staged chains
over the classical character ring.
The free comparison complex has many other generators and
may have additional homology. No identification of its entire
derived specialization with a closure Koszul complex follows.
Indeed the crossing-difference relations at \(\delta=0\)
only identify over- and under-crossings; the full specialized
skein trace/Fricke relations are not part of this presentation.
Moreover an isotopy in the closed complement may already use
the closure relations, so it need not induce a relation in the
free punctured-disk character ring.

The local complex (5) has disjoint comparison cubes in every
degree. The global wall proof here is only for two independent
one-probe homotopies. With three or more family parameters,
additional collision strata can occur; this proof does not
silently supply all their global higher coherences.
Nor does it prove \(\delta\)-flatness, survival of the empty
source class on a geometric factor, or a lower bound for the
original closed period. The new result is the integral
two-probe filling (15), its exact original-source augmentation
(16), and its limited leading-row identification (18).

## Complete proof-source pin

C: notes/research_skein_corrected_braid_closure_source.md,
SHA256 1e7586c23494f3ea91be0060f5b2cfed01155a569e6d1ac6c25682c5c446272f
(491 lines).

The complete matching C final was freshly read nontruncated in
the immediately preceding active author sequence and retained
unchanged. Only written mathematics and text/hash operations
were used. Frozen and public files were not changed.
