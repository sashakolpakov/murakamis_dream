# A fixed domain test using the saved Fourier boundary enclosures

This test addresses one specific hypothesis needed by the right-boundary
source estimate. The boundary map \(\beta_K\) has already been proved
holomorphic on a neighborhood of \(D_4\), and its image is in the disk
of radius \(0.082\) about \(0.35-0.01i\). The complete ordinary source
estimates use the smaller set
\[
 K_3=\{|b-(.35-.01i)|\le.083\}
       \cap\{-.072\le\Im b\le.068,\quad \Re b-3\Im b\le.608\}.
\]
The disk inclusion does not by itself imply these three linear bounds.

The existing record
[Fourier boundary update](../repro/results/research-mixed-fourier-boundary-update.json),
with SHA256
5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514,
contains rational rectangular enclosures of \(\beta_K\) on all 512
closed boundary arcs of \(D_4\). They retain the full original
uncertainty in the algebraic parameter \(K\). The present test uses
those saved rectangles only. It does not evaluate a logarithm,
exponential, source, derivative, or new root.

## The mathematical implication

Let the saved rectangle on an arc be
\([r_-,r_+]+i[i_-,i_+]\). The three sufficient margins are
\[
 m_1=i_-+9/125,\qquad
 m_2=17/250-i_+,\qquad
 m_3=76/125-r_++3i_-.
\]
If all three margins are nonnegative on every arc, the harmonic
maximum and minimum principles extend the three bounds to all
of \(D_4\). Together with the already proved disk inclusion this
establishes \(\beta_K(D_4)\subset K_3\).

For a failed sufficient margin also retain
\[
 \widetilde m_1=i_++9/125,\qquad
 \widetilde m_2=17/250-i_-,\qquad
 \widetilde m_3=76/125-r_-+3i_+.
\]
If one of these upper margins is negative, every value on that
entire saved boundary arc violates the corresponding half-plane.
This disproves the proposed inclusion for the whole independent
disk \(D_4\). It does not disprove the inclusion of a narrower
family of actual terminal coordinates. Otherwise a failed lower
margin is recorded only as inconclusive.

## Fixed execution

The sole script is
[saved-domain recombination](../experiments/check_mixed_fourier_boundary_saved_domain.py).
Before execution its complete source and this argument must be
read by root and a peer. Their hashes are then fixed and passed
to the script. Root executes it once, writing the new exclusive file
repro/results/research-mixed-fourier-boundary-k3-saved-domain.json.

The inventory is fixed: all 512 arcs, all three lower and upper
margins per arc, and the saved conservative disk-radius bounds.
No arc is skipped after a failed margin. The script verifies the
original record hash, its success and coverage flags, and every
original source-file binding before and after the exact rational
arithmetic. It verifies its own and this protocol's frozen hashes.

The output reports containment, a certified boundary violation, or
an inconclusive enclosure. Every per-arc comparison is saved,
including failed comparisons. There are no optimizers, adaptive
subdivisions, retries, new precision choices, or analytic evaluations.
The chosen domain and its three half-planes are not changed after
viewing the outcome.

A successful result would settle only the displayed domain inclusion.
The original right-boundary finite polynomial still needs its
complete calibrated upper estimate.
