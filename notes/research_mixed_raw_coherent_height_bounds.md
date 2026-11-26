# Imaginary marginal bounds beside one or two raw right edges

Research theorem, 5 November 2026. The analytic reduction
is the [raw/coherent height-comparison lemma](research_mixed_raw_coherent_height_comparison.md).
Its domains, logarithmic normalization, original coherent phases and
complete real-row envelopes are retained.

Write \(G_d(a,z)\) for the sum of the coherent center marginal and
the allocated raw marginal at its maximizing real row, with center
type four and orientation \(d\). Put
\[
 W=\operatorname{conv}\{.45-.057i,.5,.45+.014i\},\qquad
 z(t)=t+.28i(.5-t),\quad .45\le t\le.5.\tag{1}
\]
**Theorem 1.** The following inequalities hold:
\[
 \Im G_d(a,z)>-3/5\quad(a\in\Omega_{3+\eta},z\in W),\qquad
 \Im G_d(a,z)>-9/20\quad(a\in\Omega_{3+\eta},\Re a\ge.16,z\in W).
 \tag{2}
\]
For two raw right neighbors one has
\[
 \Im\{K_0(z,u_0)+K_1(z,u_1)\}>-9/20.\tag{3}
\]
The two optimizing real rows in (3) remain independent. The incoming
raw edge has own-factorial type one; the outgoing edge's own type is
its right neighbor's indicator \(\beta\in\{0,1\}\).

Height convexity makes each imaginary marginal nonincreasing in the
center height. Thus the top edge (1) suffices. For fixed \(z\), the
mixed marginal is harmonic in \(a\), so the boundary of the full or
clipped neighbor polygon suffices. For \(d=0\) the raw neighbor's
type does not enter the allocated center derivative or row optimizer;
for \(d=1\) both types are retained. There are consequently
\(3(6+6)=36\) full-polygon families and \(3(7+6)=39\) clipped
families, plus the two cases in (3). All 77 domains are retained.

The checker uses the original-logarithm affine Newton self-map for the
one coherent root and sign-validated real-row enclosures from
\(T_u\le-2\pi\). For a real parameter differential, its exact
marginal response is
\[
 dG=H_{ca}\,da+H_{cc}\,dz+K_z\,dz+K_u\,du_*,\quad
 du_*=-\Re(K_u\,dz)/T_u,\quad dz=(1-.28i)\,dt.\tag{4}
\]
The two-raw version sums the last two terms for each independent row.
Here \(H\) is the exact original complex Schur Hessian, whereas the
row response uses real stationarity only. The full-box derivatives
of \(-\Im G\), together with a separately certified midpoint value,
bound each rational rectangle. Direct interval evaluation is another
valid bound. Each saved monotonic reduction retains its maximizing
face and is rechecked; every split retains both children. A completed
saved tree is required for each of the 77 exact initial domains.

The complete outward cover proves (2)--(3) on all 77 families, with
910 accepted cells. Section 3 of the cited height-comparison lemma gives
its selected-to-unselected rate comparison, including both true
Fourier alternatives and their single source tolerance. Combined
with a separate unselected clamp it removes the selected height
before horizontal clamping. It does not make the selected contour
itself monotone. No full-period asymptotic or missing opposite-half
inequality is claimed.

    python3 experiments/certify_mixed_raw_coherent_height_bounds.py
