# Newton tangle formulas, terminal decorations and tree geometry

This record describes the proof reading and finite verification used to
extract three papers from the reference account. Its
[snapshot](tangle-tree-audit-snapshot.json) records the source versions,
review scopes and executed checks. The reference manuscript is unchanged.

The papers address different mathematical questions:

| Paper | Conclusion supplied here | Additional work needed for other conclusions |
| --- | --- | --- |
| [Newton coefficients and positive sources for Conway tangles](../papers/newton-tangles/main.tex) | Exact complete-meridian formulas and the positive source for the stated completed-root grammar, with an interior variational maximum. | Moving-meridian formulas, geometric development and the signed filling asymptotic. |
| [Balanced circle packings from terminal tangle decorations](../papers/terminal-decorations/main.tex) | A finite decoration construction giving strict balance; the volume consequence uses the numbered companion results. | The hypotheses and proofs of those imported finite, analytic and geometric theorems remain necessary. |
| [Positive octahedra and primitive fillings for trees of crossing circles](../papers/circle-tree-geometry/main.tex) | A positive hyperbolic filling and absolute volume formula when every vertex satisfies the stated degree-and-twist condition, or the variable-radius certificate. | An exact quantum kernel and estimates showing which contribution an invariant selects. |

## Newton algebra and the positive source

The detailed algebra reading covered Sections 3–6, including the physical
pair Casimir, its full polynomial commutant, quarter-turn, trace,
all-color auxiliary-circle expansions, crossings and half twists. The
rest of the paper was checked against the retained support and
variational arguments. The independent algebra reading did not repeat
the geometric or filling proofs from other papers.

Two substantive derivations were missing from the compressed source
presentation and are now explicit.

First, a residue calculation alone identifies two polynomial
functionals; it does not identify either one with the actual physical
partial trace. The new proof first computes that partial trace from the
generic pair decomposition, while keeping the polynomial fixed. It then
takes the root-of-unity limit, retaining paired derivatives. Only after
that calculation is the functional identified with the highest Newton
coefficient. The cup and cap equations also show that the physical turn
remains in the intertwiner algebra before its polynomial form is used.

Second, values at the spectral roots do not determine a polynomial
modulo a characteristic polynomial with repeated roots. The crossing
proof now constructs a triangular matrix commuting with generic Newton
multiplication. Its first column gives the Newton expansion. Regular
specialization and the paired divided difference recover the first
derivative at each double root, agreeing with the finite companion's
physical crossing formula. Index reversal then gives the half-twist
phases, including their signs.

The interval-support argument now caps each input index by the proposed
output before adding the available intervals. The proof uses the true
upper endpoint `min(u1,r)+min(u2,r)`, rather than claiming that every sum
up to `u1+u2` remains available after the caps. Primitive lattice rounding
supplies the eventual positivity used in the limit. It does not imply a
nonzero positive source at every small level.

The [finite matrix checker](../papers/newton-tangles/check.py) constructs
the physical representation matrices over suitable finite fields at
levels 2 through 9. It checks the pair characteristic identity, physical
turn and trace, all Newton products, high- and low-color expansions,
crossing values and derivatives, and both half-twist signs. It also
checks six cup/cap intertwiner identities at each level. Deliberately
dropping the repeated-root derivative or the turn phase fails. These
eight levels are finite checks of the written identities, not a proof
for every level or a proof of the variational theorem.

## Terminal decorations

The full paper was read, with a separate reading of Sections 3–4 on the
literal cut and local packing extension. No concrete defect was found
in those inspected arguments. The principal checks were:

- The stellar subdivision keeps the old matching edge, uses the cyclic
  face order correctly, and creates the specified new matched pair.
- An even stack of odd terminal pieces preserves the four-endpoint
  pairing and creates no closed internal main component. It need not
  preserve the isotopy type of the filled knot.
- The new tangent disk and the three outward shaded disks lie in the
  chosen empty interstice; the old disks stay fixed.
- The exact curvature recurrence is a square progression. The stated
  nearest-integer rule gives finite even counts with both normalized
  parameters at least four and difference at most one.
- The integral remainder bounds give the positive constant
  `3347/27720` for each retained pair. The added pairs satisfy their
  separate strict comparison. A single completed packing therefore
  supplies a common strict certificate for every noncentral sector.

The volume corollary imports the original invariant normalization,
the finite Hermite filling norm, the local spectral estimates, the
nonzero whole central contribution and the primitive geometric filling.
The decoration argument supplies the complementary strict gap. No
unrestricted source theorem is assumed.

The terminal checker replays exact polynomial and rational identities,
sixteen oriented patches and endpoint-pairing traversals. Its forty-nine
count examples supplement the written all-real counting argument. They
do not establish arbitrary iteration or an asymptotic invariant limit.

## Tree geometry

The proof reading covered the ordered tree cut, primitive peripheral
words, positive tetrahedron convention, contraction estimates, full
logarithmic periods, metric completion and absolute volume calculation.
A separate bounded reading concentrated on the topology, peripheral
matrices and imported regulator differential. No concrete mathematical
defect was found in that scope.

The common condition is `sqrt(d_v^2+n_v^2) >= 630` at every vertex. The
argument also supplies a certificate using different radii at different
vertices. The denominator estimate proves the sign of the imaginary
deformation parameter without dividing by a twist integer. Thus a
vertex with large degree and zero net twist is genuinely included.

The only specialized geometric import is the local peripheral-volume
differential in the marked-fillings paper, Section 7, equation (7.3).
The tree paper checks its primitive-basis orientation and positive-shape
convention explicitly. It does not import that companion's separate
long-filling existence theorem. The full periods are calibrated near
the complete cusp and continued; they are not reset to principal logs
after many page increments. The proof then constructs the cone tube,
the smooth filled endpoint and the absolute comparison with metric
volume on the same tetrahedral chain.

The symbolic checker verifies rational block identities and enclosures
and the four primitive peripheral multipliers. Those calculations do
not prove the topology, contraction theorem or metric completion. Nor
does the classical volume formula alone establish a quantum volume
limit. In particular, the moving-meridian tree kernel is still a
separate prerequisite for the summed and directed analytic estimates.

## Formal coercivity and publication checks

[TransportCoercivity.lean](../formal-real/TransportCoercivity.lean)
adds seven definitions and sixteen theorems. Its inputs are actual
positive supported table entries, their row and column sums, and finite
paths in the row-incidence graph. From connectedness and one fixed
coordinate, it proves a positive recession bound, a uniform norm
margin, compact sublevels and an attained minimum of the defined
potential. The uniform margin and minimizing point are derived, not
assumed.

The Hall inequalities constructing the geometric table, the prescribed
geometric margins, the triangle lower bound and the geometric support
identification remain written inputs. For a disk with three fixed
positive boundary values, the application combines the boundary columns
into the grounded coordinate and retains their logarithms in the row
constants. That substitution is not itself formalized. Neither
uniqueness nor the geometric development of the minimum is claimed by
this module.

The optional-package replay compiled all 83 declarations: 17 definitions
and 66 theorems. Its nine dependency pins were unchanged and all fourteen
negative controls were rejected. The publication reused that completed
execution after comparing all thirty recorded source hashes; it did
not infer success from a declaration count.

The consolidated paper runner completed ten groups, with fresh outputs
and unchanged recorded inputs. The three new PDFs have 18, 13 and 15
pages, respectively. Their native TikZ figures were rendered and read;
the build also checks unresolved references and overfull boxes. These
typesetting checks and finite replays supplement the written proofs.
They are not an end-to-end formal verification of the volume conjecture.
