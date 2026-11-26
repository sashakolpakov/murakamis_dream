# Uniform terminal alias endpoint comparison

Research completion, 6 November 2026.

All sixteen penalized terminal alias endpoint labels now satisfy the
joint comparison on the actual canonical \(K_4\) families, with a common
raw gap greater than \(1/20\). Both terminal types and both complete
selected-weight alternatives use the same height \(H=1/100\).
Vertical alias sides still require their zero-height endpoint comparisons.

## 1. Completed extraction and exact recombination

The fixed [uniform alias extraction](research_mixed_terminal_uniform_alias_reserves.md)
completed once. Its [result](../repro/results/research-mixed-terminal-uniform-alias-reserves.json)
has SHA256
142f424a414174fc8ee8ba0fd4ee69b6c8c6ffd5c954bbba9211771536b9bd87.
All 48 family maxima are finite, with no unresolved family or changed
input. The four original image covers contain \(72,49,45,25\) closed
source cells. All twelve source families and all sixteen compiled alias
labels are retained in each case.

The debit remains exactly \(41/1000\). In the notation of the extraction,

\[
 \rho_{\beta,\epsilon,k}
      =-U_{\beta,\epsilon,k}-41/1000.
 \tag{1}
\]

No smaller debit or different contour was substituted after seeing the
saved bounds.

For \(\beta=1\), combine these reserves with the completed
[joined-plane estimate](research_mixed_terminal_uniform_joined_plane.md).
Its [immutable result](../repro/results/research-mixed-terminal-uniform-joined-plane.json)
has SHA256
4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88.
The two records use the identical refined canonical cases. Exact
saved-data recombination gives the following conservative rational table:

| Terminal flag \(\epsilon\) | Allocated reserve \(\min_k\rho_{1,\epsilon,k}\) exceeds | Plane ceiling \(\max_\nu E_{\epsilon,\nu}^+\) is below | Joint gap exceeds |
|---:|---:|---:|---:|
| 0 | \(334925/10^6\) | \(61645/10^6\) | \(273280/10^6\) |
| 1 | \(122269/10^6\) | \(70840/10^6\) | \(51429/10^6\) |

Both last-column fractions are strictly greater than \(1/20\).
The exact unrounded lower bounds are approximately \(0.2732813196\)
and \(0.05143076038\), respectively; the rational comparisons prove
the statement.

The separate [recombination record](../repro/results/research-mixed-terminal-uniform-alias-comparison.json),
SHA256
2bb8973f00571490a8ecb3d219f104ecc7be2ec025918363d95cec830653e4e2,
checks all 532 inherited current bindings before and after. It verifies
the case and cover associations, all 2,292 stored outward-display
decodings, 48 family maxima, 64 label mappings, 48 plane-vertex sums,
and the 64 resulting endpoint comparisons. The original analytic
inequalities and scalar-gain certificates are inherited from their
bound proofs and results; they are not analytically replayed here.

## 2. Joint endpoint theorem and its scope

Use the canonical family \(q_*(b)\) of the extraction, with incoming
type four, ordinary type four, terminal type \(3+\epsilon\), and

\[
 b\in K_4,\qquad \epsilon\in\{0,1\},\qquad H=1/100.
 \tag{2}
\]

Let \(\sigma\) be any of the sixteen labels having at least one
alias coordinate in extraction equation (3), and let
\(\nu\in\{0,1\}\) denote the original complete selected-weight
alternative. Keep all original independent real targets, index heights,
alias penalties, incoming modulus halfweight and complex marginal.
Then the original joint defect satisfies

\[
             \sup D_{1,\epsilon,\nu,\sigma}<-1/20.
 \tag{3}
\]

Indeed the [exact plane allocation](research_mixed_terminal_reserved_plane_transfer.md)
gives

\[
 D_{1,\epsilon,\nu,\sigma}
       <E_{\epsilon,\nu}^+-\rho_{1,\epsilon,k(\sigma)}.
 \tag{4}
\]

The table proves (3). The two half-allocations use the same complete
Fourier alternative and the same height. No summand is removed, and
the source-specific reserve is not compared with a plane from another
canonical family.

The [canonical source-domain theorem](research_mixed_terminal_canonical_source_domain.md)
supplies the original terminal-four oriented and inverse-leg conditions
throughout (2). In particular it includes the actual word suffixes of
length at least three in its stated type scope. The independent image
rectangles are only covering devices; this proof does not declare all
their points source-feasible or extend the source theorem to all of
the auxiliary disk \(D_4\).

Equation (3) concerns the penalized endpoint labels. A vertical alias
side also has a zero-height endpoint, represented by a nonalias real-cut
profile. Its bound is still needed before height convexity controls the
whole side. Thus this completion supplies a uniform part of the terminal
alphabet, not a complete terminal-kernel, full-source, or knot theorem.
