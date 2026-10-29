# Coverage check: normalized Racah factorials and hyperideal volume

29 October 2026. Coverage only: primary-source definitions and theorem
statements were checked. Their proofs are not inputs to our independent
[factorial/normal theorem](actual_supported_racah_common_phase_and_normal_metric.md)
or [local geometry theorem](actual_four_port_hyperideal_angle_volume.md).
The local 6j–hyperideal-volume relationship is established literature;
no novelty is claimed for recovering it here.

Our convention is zeta=exp(pi i/N), [u]=(zeta^u-zeta^-u)/(zeta-zeta^-1),
integer graph spins j<=floor((N-1)/2), and four face sums>=N-1.
W_N is the positive magnitude of the regularized face-normalized
scalar, with [N] removed before evaluation. Its exact Casimir angles
are pi-(2j+1)pi/N. The uniform result includes closed-chamber sequences
and O(log N) error for log W_N; its fixed normal jets are derivatives
in zeta=q exp(t), not merely coefficients in a large-N expansion.

## Closest prior statements

**Costantino (2007).** Definition3.2 gives the strict hyperbolic-type
conditions 1<face sum<2 and triangle deficits between0 and1.
Theorem3.9 gives a simple pole and the volume growth of the
regularized [n]6j coefficient. His [u] uses q^(u/2), so
q_paper=zeta^2 makes the quantum integers IDENTICAL to ours. The
D-block volume is twice the tetrahedron volume, matching our pi/N
normalization. This already covers the interior leading rate,
without an odd-level restriction; parity/composite levels alone
are not a new distinction. [Definitions3.1–3.2 and Theorem3.9](https://arxiv.org/html/math/0611399v4),
[published article](https://doi.org/10.2140/gt.2007.11.1831).

**Chen–Murakami (2023; preprint2017).** Theorems1–2 give the volume
limit when a tetrahedron has an ideal or ultra-ideal vertex and a
refined Gram-determinant prefactor for specified rational-angle
sequences. They take odd r, xi_r=exp(2pi i/r), q=xi_r^2 and
[u]=(q^(u/2)-q^(-u/2))/(q^(1/2)-q^(-1/2)). Their scaling is
spin/r=(pi-angle)/(4pi). Substituting r=2N would match our quantum
integer but violates their odd-r hypothesis. Their explicit halfshift
is also prior art. [Theorems1–2 and definition in§2](https://arxiv.org/html/1706.04887v3),
[journal DOI](https://doi.org/10.4310/JDG/1679503803).

**Belletti–Detcherry–Kalfagianni–Yang.** Theorem1.2 gives the sharp,
tuple-uniform v8+O(log r/r) upper capacity for r-admissible6j symbols;
AppendixTheoremA.1 states the ideal/hyperideal volume limit under
explicit face/deficit conditions. Their root is exp(2pi i/r), r odd,
with doubled integer colors. This is substantial overlapping coverage,
but a universal v8 bound is not the same statement as our label-dependent
two-sided closed-chamber volume estimate. Setting r=2N introduces
the [N] poles that their odd-root evaluation avoids.
[Theorem1.2,§2 and AppendixA](https://arxiv.org/html/1807.03327v2).

**Belletti–Yang (2025).** Theorem1.4 covers generalized hyperbolic
volume growth under a negative diagonal-cofactor hypothesis.
Theorem1.5 states a refined asymptotic along sequences with fixed
sides of the color wall and a limiting tetrahedron without ideal
vertices. The root remains exp(2pi i/r), r odd. Their§2 records
the earlier ideal/hyperideal cases as well. These results preclude
presenting the local volume mechanism as new.
[Theorems1.4–1.5 and§2.2](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/topo.70033),
[arXiv version](https://arxiv.org/abs/2308.13864).

**Costantino–Murakami (2013).** Their graph face model and6j symbols
use non-integral quantum-group representations and relate them to
truncated-tetrahedron volume. This is relevant background, not an
identified equality with our ordinary highest-weight Hermite source.
[Publisher abstract and primary paper](https://ems.press/journals/qt/articles/4181).

## What this bounded check establishes

The verified interior local volume claim is covered, most directly
by Costantino after the explicit root substitution. Our exact
all-chamber O(log N) estimate, scalar generic-normal/inverse-jet
bounds and retained [2N] partner current have more specific technical
statements; this bounded statement check neither proves they are
absent elsewhere nor supports a novelty claim. A refined large-level
asymptotic is not automatically a theorem about fixed-root generic-q
jets, and a lowest-nonzero Laurent coefficient is not an arbitrary
prescribed source normal.

None of these local statements supplies our literal marked-source
normalization, a positive completed recoupling Gram, or general graph
sewing/peripheral constraints. Turaev–Viro conclusions are not silently
substituted for original Kashaev invariants. The full-source problem
remains separate.
