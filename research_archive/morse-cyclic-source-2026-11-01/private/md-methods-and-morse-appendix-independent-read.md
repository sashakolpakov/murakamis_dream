# Methods chapter and Morse appendix: independent bounded read

1 November 2026. Read-only check of the root-authored methods chapter and Appendix O in the publication checkout. This records mathematical scope and conversion fidelity, not a fresh proof of every cited theorem.

## Methods chapter

The following points agree with their actual source formulas.

- The decomposition into a specified contribution and a remainder is correctly distinguished from invariance of either piece. The stated subexponential, nonzero prefactor plus a fixed exponential remainder gap gives the displayed logarithmic limit.
- The shared face coefficient retains a single target for each ordinary face and the two protected zero faces. The degree accounting agrees with the original homogeneous source. The flat presentation is only an illustration; the Morse adapter is separately linked.
- The full-Hermite insertion bound is exactly the published supremum bound, with fixed signed powers. It does not bound the remaining shared polynomial.
- The positive-sum maximum argument includes polynomial state count, uniform logarithmic error, and approximation of the maximizing support at every sufficiently large level.
- The sine-factorial integral, Lobachevsky normalization, and ideal-tetrahedron volume formula have the correct signs. Volume is strictly concave on the positive angle domain. The text separates existence of an interior critical point from identifying the intended manifold.
- Weighted Cauchy and the dual Gram cost are correctly normalized, including the common boundary measure. The absence of a lower overlap bound is explicit.
- The unitary finite Fourier normalization and Parseval identity are correct. Against ordinary_color_plancherel_bound_audit.md §4, the actual energy is \(E_N=|K_N|^2+R_N^{\mathrm{ord}}\), with \(1\le R_N^{\mathrm{ord}}\le C N^B\). The lower bound uses the trivial color \(C_1=1\). A positive energy exponent \(\lambda\) gives Kashaev rate \(\pi\lambda\), as written.
- Convex majorization and the positive-measure Tauberian theorem are correctly separated. The Tauberian conclusion is cumulative, and the example with alternating level behavior does not claim to be a knot example.
- The quantum commutation relation in the illustrative convention is correct. Pointing, classical factor divisibility, full ideals, and selected periods are distinguished.
- The coverage table does not promote the projected cube or unresolved general signed remainder to a full volume theorem.

Corrections sent to root:

1. “Unchanged general matched sphere” should retain “simple” and the stated Morse/marked geometry.
2. The regulator paragraph's stronger criterion needs its actual bistochastic hypothesis and surrounding action/endpoint assumptions. A safe concise wording is: “One crucial input in a stronger sufficient criterion is a bistochastic positive transport that fixes the regulator observable.” Positivity and fixing a scalar mean are insufficient.
3. For arbitrary complex shape \(z\ne0,1\), the Bloch–Wigner value is signed volume. Say “signed volume,” or restrict to \(\operatorname{Im}z>0\) when stating positive volume.
4. Useful notation completion: explicitly set \(c_0=K_N\), \(c_j=C_j(q_N)\), \(1\le j<N\), with \(C_j\) the original reduced zero-framed ordinary color. This makes clear that the energy is not an arbitrary Fourier norm and explains \(R_N^{\mathrm{ord}}\ge1\).

A minor optional precision is to say \(N\ge3\) at the source-identity application, as in the exact source theorem; the abstract finite polynomial norm remains valid at \(N=2\). This does not affect any asymptotic assertion.

The native MathML rendering completed without warnings. There were no control bytes; inline and display delimiters were balanced. A naïve Markdown link regex incorrectly detects the coefficient example as a link, but it is inside a display and the native parser renders it as mathematics.

## Appendix O

An independent extraction and comparison, removing only equation tags, native labels, and whitespace, gives:

| Unit | Display formulas | Inline formulas | Comparison |
|---|---:|---:|---|
| Analytic Morse period | 28 | 119 | All unchanged |
| Original complement and geometric contribution | 39 | 165 | All unchanged |

The displays also agree with the previously frozen private analytic and geometric proofs. The comparison was performed independently of the converter's own counts.

I literally read the raw phase and normalization, H1/H2 statements, odd central normal, primitive lattice, the outer-cube/cutoff/inner-cube choice, whole-domain endpoint currents, independent signed charge comparison, original disk-framed equation, nonunit longitude modulus, same-chain filling-volume comparison, and the final full-source limitation.

The original phase \(q^{d^2\sum n_e/4}\), parity cancellation, \((-2i)^R\), level power \(N^{R+1/2}\), and both determinant branches remain unchanged. The two distinct cube radii remain distinct. The primitive equation is still \(U+pV=-2\pi i\), with the main cusps unfilled. The argument claims a nonzero all-CROSS period and does not suppress LEFT/RIGHT without an additional argument.

One inherited reference ambiguity was found in geometry §9 after (31): it said the H1/H2 estimates held “for the exact coefficient (5),” where (5) is the full numerator. I requested “for the all-CROSS projection of the exact coefficient (5).” Root has applied this in both the source note and Appendix O. No displayed formula was changed.

At the last read, Appendix O SHA256 was
878e61c2d2b40a4f22f0ace29935ca632d191db6e0d183c67456286141ebc956.
The analytic public note SHA256 was
6ef1f3c2271df37017b448428869b6c4470db3c0d163f52bfaa735966d9d44ed.
The corrected geometric public note SHA256 was
36018844b8e14207ae30ed65180b5f87d62028f0bf12aa2db63f06374ec12654.

The methods chapter was still being edited by root for literature and the reported precisions. The inspected snapshot SHA256 was
c3623bc4f8f629dc15f92af7f39e3fad3a4271bf2f220d0bfa3948c439e8af7e.
No public or workspace file was edited by this reader.
