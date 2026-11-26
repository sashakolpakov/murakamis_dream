# Exact symmetry completion of the own-three left-cut certificate

Research deduction, 5 November 2026. The bounded original own-three
author run stopped at its 600-second cap after completing five of
six ordinary boundary faces. This note completes the remaining
equal-type face by exact input/root permutation and revalidation.
It does not enlarge the search budget, propose new roots or targets,
or repeat the source arithmetic on the five completed faces.
The original proof, certifier and partial record remain immutable.

## 1. Input and the exact symmetry

Use the original equations, allocations, target domain and strict
gap from the
[own-three support proof](research_mixed_three_left_cut_support.md).
The partial author record is
[research-mixed-three-left-cut-support-partial.json](../repro/results/research-mixed-three-left-cut-support-partial.json),
with SHA256
3fdd788cbd235d72bdba3499111e7901485c807e0f9bea3c80492fdd6a869778.
Its five completed cases and leaf counts are
\[
 \begin{array}{c|rrrrr}
 (\alpha,\beta,\mathrm{face})&(0,0,0)&(0,0,1)&(0,1,0)&(0,1,1)&(1,1,0)\\
 \hline
 L&77988&77988&45884&46577&25757 .
 \end{array}
 \tag{1}
\]
Each retained leaf passed both original conditional orientations
at 256 bits. The incomplete case is only \((1,1,1)\);
its partial tree remains in the immutable input but is not used
to fill the missing face.

Write \(z=(s,t)\), \(p=(A,C)\), and let
\(S=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).
The original unexponentiated equations \(E(z,p)=0\) obey
\[
                E(Sz,Sp)=S E(z,p).
 \tag{2}
\]
Both inputs of the remaining case have type four and the same
disk. At every common parameter triple \((\theta,\rho,\psi)\),
the circle-first and circle-second parametrizations therefore
satisfy
\[
                         p_1(\theta,\rho,\psi)
                              =S p_0(\theta,\rho,\psi).
 \tag{3}
\]
No parameter-axis reversal or reflection occurs. Their cube trees
can have the identical split axes, boxes and right-first order.
Uniqueness of the original zero-lift root gives \(z_1=Sz_0\).
The two conditional orientations simply exchange: their first
retained argument and following root remain in the same internal
order. Both first type flags equal one, so all allocated outer
terms and the chirp agree under this exchange.

## 2. Transport of every saved affine witness

For an original saved witness, write its affine center as
\(z_0+D(p-p_0)\), inverse matrix as \(Y\), and remainder
radii as \(r=(r_s,r_t)\). The transported witness is exactly
\[
 \widetilde z_0=Sz_0,\quad
 \widetilde Y=SYS,\quad
 \widetilde D=SDS,\quad
 \widetilde r=Sr .
 \tag{4}
\]
Thus both rows and columns of the inverse and affine matrices are
reversed; only reversing rows would be incorrect. The rational
complex entries themselves are unchanged.

The two saved rational target pairs are reversed as a list of
orientations. The two target coordinates inside each pair are
not reversed. Equations (2)--(3) show that the exact deficit in
the new orientation equals that in the opposite old orientation.
This includes the correlated reference Hessian and the asymmetric
first chirp.

The helper nevertheless verifies every transported leaf directly,
using the unchanged original own-three interval root self-map,
original-log midpoint test, response enclosure and complete target
gain test. It calls the original functions with own flag zero and
the actual circle-second parameters. It makes no root proposal,
target proposal or subdivision. This revalidation also checks
that finite-precision interval evaluation of (4) passes the
original strict \(1/2000\) acceptance threshold.

## 3. Coverage and provenance

The helper is
[complete_mixed_three_left_cut_symmetry.py](../experiments/complete_mixed_three_left_cut_symmetry.py).
Before arithmetic it pins the original partial input, original
proof and original certifier hashes, and checks all 24 inherited
dependencies. It reconstructs the complete right-first binary
tree of each of the five cases in (1), including its exact split
axis at every depth, exhausted stack, leaf count and maximum depth.
This is a structural check, not a replay of their old inequalities.

The new sixth tree is transported from the complete fifth tree.
Every original split is retained and every leaf is transformed
by (4). It therefore exhausts the same whole cube and has exactly
25,757 leaves and 51,513 nodes. Together the six faces have
\[
                  299951\ \hbox{leaves},\qquad
                  599896=2(299951)-6\ \hbox{nodes}.
 \tag{5}
\]
These counts accompany actual tree reconstruction and direct
acceptance of all transported leaves.

Only after this validation passes does the helper assemble
[research-mixed-three-left-cut-support.json](../repro/results/research-mixed-three-left-cut-support.json)
with status “passed”. It retains the original proof/certifier
hashes and the original 24-entry dependency dictionary exactly.
Additional symmetry-completion metadata binds this note, the helper
and the immutable partial input, records the permutation and
transport counts, and distinguishes the original bounded author
time from the new validation time. The five earlier face trees
are copied unchanged. The incomplete sixth prefix is discarded
from the assembled output, while remaining fully preserved in
the original partial record.

The unchanged original certifier can consequently replay the
assembled canonical record at higher precision across all six
faces, with no proposals or refinement. It rechecks every earlier
leaf as well as every transported leaf. No change to its acceptance
rule or to its input-domain definition is needed.

Upon complete acceptance, the six-face premise of the original
support proof is fulfilled, and its reference-boundary principle
gives the same uniform own-three left-row bound on the entire
reduced ordinary products. The distinction between formal
auxiliary allocations and actual physical Fourier heights remains
unchanged. Half rows, last rows, terminal endpoint graphs and
full-source noncancellation remain separate.
