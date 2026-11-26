# Manuscript and guide claim audit

This is a read-only audit of the public checkout at the HEAD recorded in the adjacent JSON manifest. It checks the statements, dependencies and distinctions between established full-invariant results and narrower results. It is not a new proof verification of every inherited technical lemma. No public file was changed and no manuscript or guide build was run.

## Concrete clarifications

1. `manuscript/sections/N-uniform-filling-bound.tex`, lines 50–56 as read: the new variable \(\mathcal D\) in the product-grid estimate should explicitly have degree at most \(d=N-1\) in each variable. This hypothesis was stated for \(S\) in the preceding paragraph, but is not literally repeated when \(\mathcal D\) is introduced. The proof and the actual application \(\mathcal D=S_{\mathrm{full}}-S_{\mathrm{CROSS}}\) satisfy the hypothesis. This is a theorem-statement clarification, not a defect of the source argument. Root has accepted this correction.

2. `book/chapters/algebraic.md`, lines 233–241 as read: qualify the regulator identity \(\operatorname{Vol}(Y)=\sum_jD(z_j)\) by requiring that the shapes realize the specified oriented hyperbolic triangulation and its required peripheral completion. Algebraic nondegenerate gluing solutions alone determine a regulator/representation volume, not necessarily the volume of the original complete manifold. Suggested lead: “When these shapes realize the specified oriented hyperbolic triangulation, with the required peripheral completion, its volume is …”. This prevents the explanation from skipping the geometric identification that the rest of the guide carefully retains.

No further mathematical correction was found in the bounded scope below.

## Scope checked

- `main.tex`, the introduction and reproduction chapter: fixed diagrams and powers precede the level limit; both parities and composite levels; original knot/component test; the recursive grammar, summed condition, local condition and directed condition remain separate sufficient theorems; the planar terminal decoration can change the knot.
- The introduction’s completed-results table, manuscript README and `repro/PROOF_INPUTS.md`: Appendix N is a finite functional theorem requiring a separate source estimate for a new volume class; Appendix O is the all-CROSS contribution, not the full invariant. The PDF expressly retains named established technical inputs and is not described as repeating every external companion proof.
- The geometric-characteristic chapter and selected parts of H/M: the first-charge anchor and noncentral semisimple auxiliary condition remain; full longitude identity is distinguished from its derivative; the operator implication begins with an existing fixed nonzero all-level annihilator, retains the reduced/full meridian factor, and concludes one selected factor, not a full A-polynomial or recurrence ideal.
- Appendix O’s opening, assumptions, exact source normalization and geometric statement: actual Morse source, original matching/mark/framing, simple sphere, supplied or constructively obtained geometric certificate, original filling curves and knot parity qualification are retained. No complete positive full-source endpoint theorem or flat-plat assumption is silently substituted for the Morse CROSS input.
- Guide `results.md`, `frontier.md`, `manuscript.md` and methods scope paragraphs: decorated planar conclusions are not transferred to unchanged cores; the missing full-minus-CROSS estimate remains explicit; finite Hermite norms are not called exponential source bounds; the new private finite-cover/Morse extension and private all-even bipyramid family are not promoted.
- The methods additions on mixed Hermite bounds and genuine sector covers: the actual source retains its spectral multidegree; product-grid vanishing removes only the no-derivative tensor; the Cartesian branch sum of maxima retains shared face weights and the original degree targets; protected zeros are not replaced; the scope remains the published certified marked plats. The forty-branch example is the published separation result, not a universal feasibility assertion.

## Algebraic chapter and illustration

Read all 361 lines of the new algebraic chapter and the SVG source; rendered the SVG in Chromium and inspected `/private/tmp/md-bipyramid-move-browser-review.png`.

- The quantum-factorial phase is exact. At \(N=6\), the values \(S_6(1)=1\), \(S_6(2)=\sqrt3\), \(S_6(4)=6\), \(B_{2,6}=1/27\), \(B_{3,6}=1/216\) and ratio eight are correct. The stated ratio asymptotic \(B_{2,N}/B_{3,N}\sim N\) matches the full calculation in the linked comparison note. It is not presented as an exact Pachner identity.
- The Hilbert-90 convention is consistent: \(a=b/\sigma(b)\) and \(\sigma(y)=ay\) imply \(\sigma(by)=by\). The cited Milne Corollary 5.24 uses precisely this quotient. No growth bound is inferred from existence of the gauge. The actual finite polynomial’s dilogarithm asymptotic is copied with the source sign and \(h_N=2\pi i/N\).
- The two Koszul differentials compose to zero. Over \(\mathbb Q[x]\), \((x,x)\) has \(H_1\simeq R/(x)\), while the single nonzerodivisor \(x^2\) has no higher homology. The translation matrix reduction to \(\operatorname{diag}(1,\dots,1,1-H)\) needs no division. The regular-sequence implication agrees with Stacks 062F; the note does not infer failure of exactness from singularity alone.
- The fixed-polynomial versus level-dependent \(q^N-1\) distinction, two-step Heisenberg product, finite Dyson formula, and marked boundary-cover monomials are correct. The cover paragraph distinguishes total cover degree from boundary-torus degree and does not infer quantum descent from volume multiplication.
- The figure has the same five vertices and six boundary triangles on both sides. Its left tetrahedra are \(PABC,QABC\), with internal face \(ABC\); its right tetrahedra are \(PQAB,PQBC,PQCA\), with internal edge \(PQ\). The Chromium rendering is legible and has no mathematical labeling error. A preliminary MuPDF SVG raster ignored CSS and filled outlines black; that is not the actual browser rendering and is not reported as a source defect.

Primary reference checks were limited to the cited statements: Milne, Fields and Galois Theory v4.22, Corollary 5.24; Stacks 0621 and 062F. They were read through the web tool. No literature theorem is used to strengthen the repository claims.

## Private research preserved separately

The finite genuine-sector-cover theorem is frozen in `/private/tmp/md-matched-simple-sphere-finite-sector-cover-volume.md`, SHA256 `db7e4a4659c30dda81d73192442789cfa71e397cc1a743238af98288b33ff6ea`; its manifest records the proof inputs. It is not published by this audit.

The rational certificate review is `/private/tmp/md-cyclic-rational-constants-independent-read.md`, SHA256 `63ecc778140f30e84cbbf0bca7f2e02f6b42327fca1685c8084d487ee667451a`. The verifier was run once independently; its output byte-matches the root result. Its mathematical interval operations were checked. The only remaining implementation issue before portability is the absolute import path to the old interval engine; the engine hash is recorded in that review. No numerical samples were treated as a proof of a general diagram theorem.
