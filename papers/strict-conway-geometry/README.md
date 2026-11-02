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

## Exact imports

- **Stationary profiles of strict Newton trees**:
  Lemma 2.2 (st:types), Theorem 3.3 (st:positive-action),
  Lemma 4.1 (st:port-product) and Proposition 4.2 (st:port-types).
  Only the nonmetric strict optimizer, Hessian and profile identities are
  used. The local core quantum asymptotic is not imported.
- **Pyramids, prisms, and complete geometry of Conway closures**:
  Section 2 for local ideal cells and volume normalization;
  equations (3.2)–(3.3) for ordered face metrics;
  equations (5.5)–(5.8) for rational local maps;
  Section 7 for the local collar words and area calculation.
  Its global completed-root Theorem 1.2 is not used.
- **Marked deformations and long fillings of Conway closures**:
  Sections 2–4 for local mixed-leaf shear, rational maps and peripheral
  multipliers. The new paper supplies its own global strict-mask group
  assembly before using these local identities.
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
endpoint-pairing table, projective edge/turn/closing words, auxiliary
flags and multipliers, and Hessian/signed-period/boundary-term algebra.
Negative controls change an asymmetric mask, a closing order, a
component count and the primitive factor of two. The JSON output pins
all input sources and is written only if they remain unchanged.
These calculations do not establish variational existence, topology,
convexity, completeness, analytic uniformity or a volume theorem.
