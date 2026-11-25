# Circle patterns and primitive fillings of augmented links

[Read the PDF](../../docs/papers/marked-fillings.pdf) ·
[TeX source](main.tex)

This paper constructs a hyperbolic metric and its volume from a marked
augmented link diagram. The input is a finite simple triangulated sphere,
a perfect matching of its dual, a marked nonmatching edge, and a retained
half-twist choice at every crossing circle. The matching specifies the
crossing-circle boxes and their ordered face pairings. The main components
are determined by following the strands through the matched boxes.

Theorem 1.1 proves the classical filling statement. Independently
sufficiently long signed fillings of the auxiliary cusps produce
the specified smooth hyperbolic exterior, and the real critical value of
the normalized action gives its absolute volume. The main cusps remain
complete. A knot-complement conclusion additionally requires that the
main strands form one component.

The auxiliary meridian and disk longitude are denoted by
$(\mu_e,\lambda_e)$. Filling $\mu_e+p_e\lambda_e$ restores crossing
power $n_e=\epsilon_e-2p_e$. All logarithmic periods are continued from
the complete structure; an exponentiated slope equation alone does not
fix their winding or prove smooth completion.

## Proof and reusable results

The proof has four parts:

1. Construct the complete circle packing by a strict angle optimization,
   prove that its developing map is globally well defined, and cut it
   along the marked edge to recover the link projection.
2. Deform the pattern and calculate the face isometries and peripheral
   holonomies. Their similarity logarithms are logarithms of the
   complex dilation multipliers, continued from the complete structure.
3. Solve the classical critical equations and prove the required sign
   for either sign of each independently long filling integer.
4. Complete the primitive cusp neighborhoods. Compare the oriented ideal
   cells with a fundamental chain of the resulting metric to determine
   the additive constant in the volume.

Proposition 6.1 gives the near-complete primitive metric completion used
by the strict Conway geometry paper. Section 7.1 computes how curves crossing the ideal faces pair with
variations of the dihedral angles and derives the peripheral differential, including its factor of two;
equation (7.3) is the volume differential. Section 7.3 proves the absolute
volume comparison. These are narrower reusable statements than the
main matched-sphere theorem, and their hypotheses are stated where used.

The paper uses the holomorphic implicit-function theorem, differential
forms and Stokes' theorem, and the classical ideal-tetrahedron volume
formula. It assumes no quantum asymptotic. Its final section explains
which additional source and noncancellation estimates are needed to
deduce a quantum volume limit.

## Build and finite checks

From the repository root:

~~~sh
python3 tools/build_papers.py marked-fillings
python3 -I papers/marked-fillings/check.py --output /tmp/marked-fillings-check.json
~~~

The checker requires SymPy. It verifies rational identities, normal-flow
signs, primitive words and boundary factors. It removes an old result
before checking and records the unchanged source hashes. The packing,
global topology, metric completion and volume comparison have written
proofs; they are not inferred from these finite calculations.
