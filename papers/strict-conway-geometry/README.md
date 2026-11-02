# Marked geometry of strict Conway compositions

This classical paper constructs the complete exterior and independently
long primitive signed fillings of a fixed literal strict Conway
expression. It proves the individual-edge mask induction and the
original closed-link identification; it does not apply the completed-root
global metric theorem to the enlarged syntax.

## Statements

- **sm:complete**: complete metric of the original augmented link,
  primitive crossing-circle bases and absolute volume \(2\pi F_0\).
- **sm:mask-invariant**: all four output-edge bits, including asymmetric
  high-type outputs, convex attachment and terminal accounting.
- **sm:knot-choice**: a literal pure/odd choice with one main component.
- **sm:marked-deformation**: the actual original group, positive retained
  chain, parabolic main cusps and exact auxiliary similarity logarithms.
- **sm:fillings**: original peripheral group, parabolic unfilled cusps,
  independently long signed primitive fillings, and the absolute
  critical-action formula.

The fixed presentation must have a strict state after deleting only its
forced closing gate and retaining the complementary root relation.
Arbitrary bare or turned closing children are allowed when this condition
holds. Slopes refer to the original crossing disks. A knot-complement
conclusion additionally requires all auxiliaries to be filled and the
actual main pairing to have one component. The paper claims no quantum
asymptotic, global character-variety uniqueness, or moving main-meridian
longitude theorem.

## Local constructions proved in this paper

Section 2 constructs the ideal leaf pyramid and multiplication prism
from their vertices and supporting planes, computes their volumes by
positive tetrahedra, and proves the ordered cross-ratio matching.
Sections 5 and 7–8 derive the primitive collar translations, common
prism maps, actual and auxiliary white transitions, full group words,
and deformed peripheral multipliers. In particular:

- `sm:local-cells`, `sm:leaf`, `sm:prism-P`, `sm:prism-angles`,
  `sm:prism-volume`: the local cells, support, angles and volumes;
- `sm:kappa`, `sm:input-kappa`, `sm:output-kappa`: whole ordered
  quadrilateral matching, including its shear;
- `sm:world-matrices`, `sm:world-table`, `sm:prism-maps`: all twelve
  prism transitions in one coordinate system;
- `sm:peripheral-words`, `sm:translations`,
  `sm:multiplier-calculation`: the original primitive basis and its
  complete translations and deformed multipliers.

The earlier completed-root papers **Pyramids, prisms, and complete
geometry of Conway closures** and **Marked deformations and long
fillings of Conway closures** remain historical references. Neither
their local proofs nor their narrower global theorems are prerequisites
of the present proof.

## Exact imports

- **Stationary profiles of strict Newton trees**:
  Lemma 2.2 (st:types), Theorem 3.3 (st:positive-action),
  Lemma 4.1 (st:port-product) and Proposition 4.2 (st:port-types).
  Only the nonmetric strict optimizer, Hessian and profile identities are
  used. The local core quantum asymptotic is not imported.
- The classical ideal-tetrahedron volume formula, with its flat limit,
  is stated explicitly in `sm:tetra` and referenced to Milnor,
  *Hyperbolic geometry: the first 150 years*. All subsequent cell
  volumes are computed here from that normalization.
- **Circle patterns and primitive fillings of augmented links**:
  Proposition 6.1 for near-complete primitive metric completion;
  equation (7.3) and Section 7.3 for the similarity-log differential and
  the same-boundary-chain comparison. All topological, flag, positivity,
  primitive-log and unfilled-cusp premises are verified here.

The primitive ratio is \(\tau=2ic/(1-\epsilon ic)\). Accordingly
\(\Phi_{\chi_i\chi_j}(0)=\pi i\tau_i\delta_{ij}\) and
\(DV(0)=-2\pi i\,\mathrm{diag}(\tau_i)\). This convention avoids the
half-ratio ambiguity in the older general-mask note.

## Build and finite reproduction

From this directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex

From the repository root, with SymPy installed in the chosen Python
environment:

    python -I papers/strict-conway-geometry/check.py --output /tmp/strict-conway-geometry.json

The exact checker covers the finite mask-state closure, original
endpoint-pairing table, an independent chord-line solution for the
prism vertex, all twelve common prism maps and the two actual white
triangle maps, projective edge/turn/closing words and their scalar
returns, primitive collar translations, auxiliary flags and
multipliers, and Hessian/signed-period/boundary-term algebra.
Negative controls change an asymmetric mask, an ordered face map, a
closing order, a component count, an odd meridian and the primitive
factor of two. The JSON output pins the paper and its actual companion
inputs and is written only if they remain unchanged. An optimized
Python invocation is rejected and any stale output is removed first.
These calculations do not establish variational existence, topology,
convexity, completeness, analytic uniformity or a volume theorem.
