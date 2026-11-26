# First-cap plateau currents with the actual adjacent-four input restriction

Research design, 5 November 2026. The four-current comparison on the
whole auxiliary \(K_4\) domain of
[stage three](research_mixed_first_cap_typed_plateau_certificate.md)
is false: two original-root fixed-input tests have positive left-cut
deficit. They are not known to be actual word references. This stage
uses an already available, orientation-dependent ordinary-map image
bound to exclude those unused inputs. All earlier proofs, scripts and
incomplete records remain immutable. No author or saved replay of
this new stage has yet been executed.

## 1. The relevant leg, not a universal type-four real bound

Use the original ordinary two-leg map \((s,t)=B_\epsilon(a,b)\)
on the full typed input disks. The variables \(s,t\) are adjacent
to \(a,b\), respectively. The map satisfies the exact symmetry
\[
                     B_\epsilon(b,a)=(t,s),
 \tag{1}
\]
by its original zero-lift equations and uniqueness. This is a local
map identity, not an assertion that the chirped finite kernel is
symmetric.

The saved
[full-product affine image extraction](../repro/results/research-mixed-cyclic-block-images.json.gz)
has SHA256
`59081ba721017bdad0bce4a74693ef31066147d1c690a6c88f26a72a62aab696`.
It reuses the original complete four-real-parameter localization
cover. In the own/external type order, its oriented real bounds give
\[
 \begin{array}{c|c|c}
 \text{own / external types}&\text{output adjacent to type four}
                                    &\text{real lower bound}\\ \hline
 4/(3,4)&t&259/1000\\
 4/(4,4)&s,t&263/1000 .
 \end{array}
 \tag{2}
\]
The corresponding families contain 7,299 and 4,561 saved affine
witnesses. Both original input disks are covered, including their
interiors. No circle-boundary or cyclic-reference assumption is
needed for (2).

For direct exact verification, decode each saved binary address into
the original normalized four-dimensional parameter box. Let its
physical input halfwidths be \(\Delta x_j,\Delta y_j\), obtained
using input radii \(9/100,8/125\) according to type. Its validated
affine enclosure is
\[
 z_i=z_{0,i}+\sum_{j=1}^2D_{ij}(p_j-p_{0,j})+w_i,
                         \qquad |w_i|\le R_i.
 \tag{3}
\]
All stored centers, coefficients and radii are exact rationals.
Consequently the following is a rational lower bound, with no
floating rounding or new root evaluation:
\[
 \Re z_i\ge\Re z_{0,i}-R_i
       -\sum_{j=1}^2\left(
           |\Re D_{ij}|\Delta x_j+|\Im D_{ij}|\Delta y_j\right).
 \tag{4}
\]
The new driver checks (4) against (2) for all 7,299 relevant mixed
outputs and both outputs in all 4,561 same-type witnesses, a total
of 16,421 rational comparisons. Every saved address list must be
literally equal to the accepted list of the original complete source
cover. The extraction's source, extractor, original author and proof
hashes, together with the original independent localization replay,
are bound. The rounded display summaries are not the acceptance
test for this new extraction.

Now consider a first cap whose own type and next vertex type are
both four. Its external input is \(b=s_2\). For \(m\ge3\),
vertex 2 is ordinary, and this leg is adjacent to \(t_1\), an
attached leg of the first type-four endpoint. If the third vertex
is type three, the external types at vertex 2 are \((4,3)\);
(1) identifies \(s_2\) with the \(t\)-output of the stored
\((3,4)\) family. If the third vertex is type four, use either
output of the \((4,4)\) family. Thus
\[
          \Re s_2>259/1000\quad(m\ge3).
 \tag{5}
\]
At \(m=2\), \(s_2\) is the right endpoint's attached leg,
and both endpoint maps have own type four and neighbor type four.
For each of the 909 original witnesses in that typed family,
the real part of its attached center minus its validated radius
is an exact rational lower bound. Their exact minimum is
\[
 \min(\Re z_{0,\mathrm{attached}}-R)
       =\frac{13834284001670119}{50000000000000000}
       >\frac{69}{250}=.276.
 \tag{5a}
\]
The minimum occurs at original tree node 152. The new driver checks
every one of these rational comparisons against the original author
record, whose complete root trees and independent saved replay are
already bound. It stores the count, exact minimum and node; no root
is proposed or re-solved for this extraction. The reflected endpoint
construction gives the same assertion for either attached end.
In particular \(s_2\), not the private \(t_2\), has this bound.
Combining (5) and (5a), every actual reference in this particular
first-cap family satisfies \(\Re b>.259\) for every \(m\ge2\).

No universal real floor for arbitrary type-four legs is asserted.
In particular the output next to an external type-three leg is not
covered by (2). For all other first-cap type families, retain the
preceding input domains without this additional real restriction.

The same geometric conclusion applies to an actual type-four
terminal block with a type-four incoming leg \(a=t_{m-1}\).
For \(m\ge3\), that ordinary leg is adjacent to the terminal
attached type-four leg \(s_m\), so (2) gives \(\Re a>.259\).
For \(m=2\), the first attached leg \(t_1\) belongs to the
own-four/neighbor-four endpoint family, and (5a) gives \(\Re a>.276\).
This input-domain lemma is independent of any first-cap or terminal
finite-source comparison; either source proof may use it without
assuming that the other source certificate passes.

## 2. The precise new domain and the recorded obstruction

Keep the full original \(D_3\) for type-three inputs, and
\[
 K_4=\{|b-(.30-.052i)|\le.060\}
                         \cap\{-.108\le\Im b\le-.001\}
 \tag{6}
\]
for type-four inputs. **Only when own type and input type are both
four**, intersect (6) with \(\Re b\ge259/1000\).
Equations (2)--(5a), the ordinary image bounds and attached extraction
show that every actual word reference of length at least two remains
strictly in its admitted domain. The outgoing target is still the
entire plateau, and all four private cut/alias families are unchanged.

The [fixed-input record](../repro/results/research-mixed-first-cap-typed-cut-fixed-points.json)
uses own four, input four, the original root witness, private cut
\(e=.27\), and the same rational target
\(y=372948142107/10^{12}\). Its two normalized external inputs
are \(\xi=-15359/16384\), with \(\eta=0\) or \(1/1024\).
Their allocated deficits are positive, approximately
\(7.5270\cdot10^{-6}\) and \(1.9654\cdot10^{-6}\).
They lie inside (6), so merely weakening a positive requested gap
cannot establish the old \(K_4\) hypothesis. Both have
\(\Re b=61441/256000<.259\), and are outside the actual
oriented-input enclosure just proved. This excludes these inputs
from the required family; it does not by itself prove the remaining
current comparisons, nor give an actual-word counterexample.

## 3. Exact continuation and compulsory complete replay

The new driver is
[certify_mixed_first_cap_oriented_plateau.py](../experiments/certify_mixed_first_cap_oriented_plateau.py).
It bootstraps only the immutable
[stage-three attempt](../repro/results/research-mixed-first-cap-typed-plateau-attempt01.json),
SHA256
`d1321329fde521bd4100bd9d6195306acaf257cad6dac9eb9d0bc610abd1015f`.
That record is incomplete, with 19,732 completed jobs, a 578-node
active prefix for job 19,732, and five pending boxes. It contains no
arithmetic error. All these trees and the frontier are imported
verbatim; accepted source arithmetic is not repeated in author mode.

All three ancestor record/proof/script hashes and exact dependency
snapshots are checked. Their nested accepted prefixes must agree.
The gap \(1/200000\), \(\mu=3/200\), \(\kappa=1/2500000\),
target boxes, original-root helpers and source arithmetic are
unchanged from stage three. The numerical helper source is still
checked literally against the first-stage driver.

In original type-four normalized coordinates the additional real
condition is \(\xi\ge-41/64\). A new node `A` may discard a
box only if own and neighbor flags are both one and
\[
                            \sup\xi<-41/64.
 \tag{7}
\]
The earlier `X`, `H`, `R`, `U` exclusions retain their original
priority; `A` is used only if they all fail. Equality and crossing
boxes are kept. All other original jobs remain present. The same
protected active frontier, atomic checkpoints, bounded author and
immutable resume protocol apply, with default depth cap 30.

The final saved replay recomputes **every** accepted source leaf,
including all imported leaves, at its saved rational target, with
no proposals or refinement. The exact rational ordinary and
909-witness attached extractions are also checked. All five
exclusion kinds are validated separately,
all 21,032 jobs must be exhausted, and every current and ancestor
binding is rechecked before publication.

Only complete author and independent saved replay may establish the
four signs on this new domain. The unchanged full-source phase
reduction would then give the first-cap plateau supporting plane at
every actual reference for every fixed \(m\ge2\), with original
halfweights, rows, aliases, both parities and ordinary colors.
Until then the corresponding whole-plateau assembly must use this
repaired hypothesis, rather than the contradicted larger-domain one.
