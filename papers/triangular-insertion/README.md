# Triangular insertion and volume limits for augmented diagrams

[Read the PDF](../../docs/papers/triangular-insertion.pdf) · [TeX source](main.tex)

This paper inserts a diagram already controlled at a protected edge into
an ordinary triangular face of another diagram. The three boundary
curvatures are now positive. Two must be sufficiently small relative to
the third at every required core certificate witness and at the complete
packing. Smallness at the complete point alone is not the hypothesis.

The input diagrams carry unabridged certificates: every locally allowed
noncentral sector has a common face-weight witness with a strict source
gap. The insertion retains the old coefficient demands at the boundary
vertices. Its proof combines a fixed-boundary variational problem with
estimates for all assembled noncentral sectors.

## Results

- **Theorem 1.1:** any fixed finite collection of certified inputs can be
  inserted into sufficiently thin ordinary faces of an explicitly
  certified core. The assembled diagram has a full-source certificate.
  For a final knot-producing parity, independently sufficiently long
  fixed signed primitive fillings give the volume limit.
- **Theorem 2.3:** prescribed positive boundary curvatures determine a
  unique interior packing of the triangular disk. Its normalized action
  is the original boundary-triangle action plus the fixed disk constant.
- **Corollary 9.1:** for every even chain length at least 2^20, an explicit
  insertion of the seventeen-region block has a source gap at least 1/50
  and retains a weak-balance failure. The fixed filling threshold can
  depend on the entire assembled diagram.

The disk-action identity is a classical variational statement. It is not
an equality of finite spectral polynomials. The separate source argument
keeps shared face weights, newly allowed sectors and whole-block cases.
The number of inserted pieces and all filling powers remain fixed as the
level tends to infinity; the main knot cusp remains complete.

## Numbered companion inputs

**Proposition 2.2** lists the finite, analytic and geometric inputs.
**Finite spectral evaluation and uniform filling bounds**, Theorems 1.1,
9.1 and 10.1 and Corollary 9.2, supplies the original source, full filling
norm and invariant normalization. **Spectral bounds and asymptotics of
Casimir sources**, Theorems 1.1 and 8.1, gives the uniform sector rates
and central coefficient asymptotic. **Oscillatory filling sums with
independently long twists**, Theorem 1.1, handles the whole signed central
period. **Circle patterns and primitive fillings of augmented links**,
Proposition 2.1 and Theorem 1.1, supplies the original marked exterior,
primitive metric completion and absolute volume comparison.

The certificate definition, protected gluing and explicit seed are
**Shared face estimates and triangular gluing for planar link diagrams**,
Definition 3.1 and Theorems 5.3 and 6.1. The ordinary-boundary extension
and its complete complementary-source estimate are proved here.

## Build and exact certificate

From the repository root:

~~~sh
python3 tools/build_papers.py --no-publish triangular-insertion
.venv/bin/python -I repro/check_triangular_boundary_certificate.py --output /tmp/triangular-insertion-check
~~~

The certificate runner replays the exact incidence and demand tables,
restricted dual flow, forty old branches and five newly allowed anchors,
and verifies their interval rate inequalities. The all-length core
construction, packing existence and analytic volume limit retain their
written proofs. No knot invariant is evaluated by that runner.
