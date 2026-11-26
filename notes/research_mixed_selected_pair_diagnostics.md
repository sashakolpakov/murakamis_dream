# Selected right-transition pairs: preserved diagnostic route

Research diagnostics, 4 November 2026. This note records an unfinished
route. The numerical experiments below do not establish a universal
selected-pair bound and are not included among theorem certificates.
The proved analytic input is the
[diagonal-height reference extension](research_mixed_selected_height_reference_extension.md),
including its target-curvature corollary.

Take the ordered pair of original allocated phases
\(F(z)=\phi_{\alpha\beta}(z_0,z_1)+
\phi_{\beta\gamma}(z_1,z_2)\). For
\(p,q\in[.22,.45]\), \(t\in[.45,.5]\), and
\(\tau=20(.5-t)\), use the selected targets and branch corrections
in equations (9)--(11) of that extension note. In particular the
middle Fourier allocation has weight one, every true forcing branch
is retained, and the two exterior costs are
\[
 (1-\tau)^2q_j(\Im z_j)^2\quad(\sigma_j=0),\qquad
 (1-\tau)q_j(\Im z_j)^2-\tau/100\quad(\sigma_j=1),
\]
with \(q_0=7.55\), \(q_2=5.5\). These costs require the farther
exterior plateau coordinates to remain at their prescribed heights.

The floating script
`/tmp/diagnose_selected_paired_right_transition.py` tested all five-vertex
type words having a selectable leg in the middle triple, every allowed
nonempty selection and true Fourier branch, and all external typed
rectangle corners. It optimized the three real targets numerically.
Its output `/tmp/selected-paired-right-transition-diagnostic.json`
contains 14,336 optimizations. All observed defects were negative;
the largest was approximately \(-.02446708\). This is only a corner
diagnostic with numerical optimization. It does not control the
reference boundary edges or establish completeness of target extrema.

The private outward pilot `/tmp/pilot_selected_pair_outward.py`
then covered the boundary product containing that worst observed
case: ordered word \((4,4,3,4,4)\), left middle leg selected,
branch \(f=(0,0,0)\), a type-four bottom external edge and a
type-three top external edge. It retained the complete
\(t\in[.45,.5]\) interval and both neighboring plateau target
intervals. The pilot used rational supporting points, exact real
concavity, original logarithmic Newton roots and full-cell derivative
bounds. At 256 bits it passed 24 cells, with an outward defect upper
bound below \(-.0174440\); its output is
`/tmp/selected-pair-outward-pilot.json`.

That pilot covers one boundary product and one selection/branch only.
Its private implementation has not undergone the full independent
review and provenance workflow required of a final source certificate.
A universal proof still needs the complete distinguished-boundary
cover, each allowed selection and branch, the generalized reference
barrier, and the exact finite-source and exterior-block assembly.
Overlapping transition stars require additional bookkeeping.
