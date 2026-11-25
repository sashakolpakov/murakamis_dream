# Shared face estimates and triangular gluing for planar link diagrams

[Read the PDF](../../docs/papers/planar-certificates.pdf) · [TeX source](main.tex)

This paper gives sufficient source estimates for an unchanged augmented
planar diagram. The input is a fixed simple triangulation of the sphere,
a pairing of adjacent triangles, a nonmatching marked edge and the original
crossing-disk frames. The two endpoints of the mark have weight zero;
every other face has one positive weight shared by all its occurrences.

A noncentral sector is a choice of a left, central or right local term at
each crossing region, with at least one noncentral term. An unabridged
certificate covers every locally allowed sector, including a sector whose
final shared coefficient happens to vanish. It assigns one common face
weight vector to each sector or finite group of sectors, with a strict
rate gap below the augmented volume divided by twice pi. It does not
choose different radii for different occurrences of the same face.

## Results

- **Theorem 1.1:** a finite unabridged certificate implies the whole
  knot-invariant volume limit after independently sufficiently long fixed
  signed primitive fillings. The final strand pairing must be one knot.
- **Definition 3.1:** the exact certificate data and their full-sector scope.
- **Theorem 4.3:** weak balance of the complete packing, including the stated
  quantified defect variant, produces such a certificate by a common
  change of weights.
- **Theorem 5.3:** an oriented triangular gluing preserves unabridged
  certificates, with the original joining-face coefficient target.
- **Theorem 6.1:** an explicit seventeen-region example and its repeated
  tetrahedral attachments satisfy the certificate criterion while failing
  weak balance at the fixed mark.

The fixed diagram and fillings do not grow with the quantum level. The
criterion is not asserted for every matched sphere. The example separates
two sufficient tests at its specified mark; it does not exclude another
presentation or mark of the same knot from passing weak balance.

## Numbered companion inputs

Propositions 2.1–2.3 collect the imported facts. **Finite spectral
evaluation and uniform filling bounds**, Theorem 1.1, Proposition 4.1,
Theorem 9.1, Corollary 9.2 and Theorem 10.1, supplies the physical source,
full repeated-root filling norm and reduced normalization. **Spectral
bounds and asymptotics of Casimir sources**, Theorems 1.1 and 8.1 and its
central-filling application, gives the local envelopes and nonzero central
expansion. **Oscillatory filling sums with independently long twists**,
Theorem 1.1, evaluates that whole signed period. **Circle patterns and
primitive fillings of augmented links**, Proposition 2.1, Theorem 1.1 and
Corollary 8.1, provides the complete metric and primitive absolute volume
comparison. The present paper proves the complementary-source estimate
and its transport; the central contribution alone would not suffice.

## Build and exact certificates

From the repository root:

~~~sh
python3 tools/build_papers.py --no-publish planar-certificates
.venv/bin/python -I papers/planar-certificates/check.py --output /tmp/planar-certificates-check
~~~

The checker freshly verifies the two fixed rational interval certificates,
the complete forty-branch cover and nine oriented attachment stages. It
pins the exact data and implementations. These finite computations support
the named certificate example; the continuum estimates, arbitrary-iteration
gluing theorem and volume implication have written proofs.
