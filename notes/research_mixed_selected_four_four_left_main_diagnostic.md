# One-box evaluation of the next-four left-cap/main-contour bounds

Research specification, 6 November 2026. This fixes one
[diagnostic](../experiments/diagnose_mixed_four_four_left_main_budget.py)
for the two scalar majorants in
[the next-four left-cap/main theorem](research_mixed_selected_four_four_left_main_majorant.md).
The diagnostic does not establish their signs on the full reference
family, evaluate a finite quantum source, solve a critical equation,
or repeat an earlier parameter cover.

## 1. Exact quantities and allocation

Keep \(H=1/100\), \(e_0=.27\), and the original next-four
reference \((e_*,s_*;z_*,b_*)\), with
\(z_H^*=\Re z_*+iH\). The tested expressions are precisely
\[
 \begin{split}
 \mathcal J_\nu^{(4)}
 &=\mathcal L_\nu+
   \Gamma_{\mu_s}(-d;.22-\Re s_*,0)
   +\Gamma_{\mu_\nu}(\beta_\nu;.22-\Re z_*,.45-\Re z_*),\\
 \mu_s&=\pi(39/80+a_*),\qquad
 a_*=\Re\cot\pi s_*>2/5,\qquad
 \mu_\nu=(23+18\nu)\pi/120,\quad \nu=0,1 .
 \end{split}
 \tag{1}
\]
The original outgoing marginal is
\(p=g'(s_*+b_*)-\tfrac32g'(b_*)\), and the outgoing
trial gradient after its affine subtraction is exactly zero.
The outgoing halfweight and extra index factorial cancel from
the trial value because their coordinates are unchanged there.
They have already contributed to the marginal and Hessian in (1);
they must not be dropped from that derivation.

Evaluate the relative trial value as
\[
 \begin{split}
 \Delta_{\rm cap}
   &=\Psi(e_0,z_H^*)-\Psi(e_*,z_*),\\
 \Delta_{\rm ord}
   &=g(s_*+z_H^*)-g(s_*+z_*)-g(z_H^*)+g(z_*)
                         +2\pi is_*(z_H^*-z_*),\\
 \mathcal L_\nu
   &=\Re(\Delta_{\rm cap}+\Delta_{\rm ord}+g(z_*))
                         -\nu\Re g(z_H^*)-2\nu\pi H .
 \end{split}
 \tag{2}
\]
In the chirp use the exact identity
\(z_H^*-z_*=i(H-\Im z_*)\), not the difference of two
independently enclosed real parts. The cap difference retains
the canonical \(S(.27)-S(e_*)\), its actual private height,
and both original cap chirps.

With \(S=e^{-2\pi is_*}\), \(Z=e^{-2\pi iz_*}\),
\(E_0=e^{-2\pi ie_0}\), and
\(\lambda=e^{2\pi H}/|Z|\), the two forces are
\[
 \begin{split}
 d&=\log\lambda-\log|1-\lambda SZ|+\log|1-SZ|>0,\\
 \beta_\nu&=\log|1-\lambda E_0Z|+\log|1-\lambda SZ|
                   -\log|S|-(2+\nu)\log|1-\lambda Z|.
 \end{split}
 \tag{3}
\]
All factors use the same rational endpoint parameter and its
necessary-reference enclosures.

## 2. Outward arithmetic and the original reference helper

Use the reusable reference helper and centered primitive in
[the next-four half-row diagnostic](../experiments/diagnose_mixed_four_four_half_row_budget.py),
with the domains, original maps and necessary filters of
[its evaluation specification](research_mixed_selected_four_four_half_row_evaluation.md).
Do not call its half-row inspection routine. The helper keeps the
own-four outgoing transfer and next-external \(K_3\cup K_4\)
condition, including attached external inputs at length three.
Strict whole-box violations alone exclude a box; a nonfinite
or unresolved regularity condition is inconclusive.

Only pointwise interval evaluation is used here. The coordinate
intersections in the helper are therefore legitimate necessary
enclosures of actual references. No derivative or mean-value
argument in the auxiliary parameter is applied to those clipped
coordinate images.

The primitive is the original \(g\) on \(0<\Re w<1\),
enclosed by
\[
 g(W)\subseteq g(w_0)+
       \Log(1-e^{-2\pi iW})(W-w_0).
 \tag{4}
\]
Its exact dyadic center value uses the original dilogarithm.
The [centered-primitive proof](research_mixed_centered_primitive_enclosure.md)
establishes (4) on the entire convex regular rectangle.
The actual private action uses the same auxiliary \(u_*\);
the fixed cut uses its original explicit canonical radical.

Let \(\pi_{\rm lo}\) be the exact rational lower endpoint
of the interval for \(\pi\), and put
\[
 a_{\rm lo}=\max\{2/5,\inf\Re\cot\pi s_*\},\qquad
 \underline\mu_s=\pi_{\rm lo}(39/80+a_{\rm lo}),\qquad
 \underline\mu_\nu=(23+18\nu)\pi_{\rm lo}/120.
 \tag{5}
\]
These are valid positive curvature lower bounds on every actual
reference in the box. For \(d_{\rm up}\ge d\ge0\) and
\(L_{\rm up}\ge\Re s_*-.22\), the index gain is bounded by
\[
 t=\min\{L_{\rm up},d_{\rm up}/\underline\mu_s\},
 \qquad
 G_s=d_{\rm up}t-\underline\mu_s t^2/2.
 \tag{6}
\]
All operations in (5)--(6) are exact rational arithmetic after
taking directed interval endpoints. Increasing the slope or
available displacement, or lowering the positive curvature,
only increases the maximum. The incoming gain uses the existing
two-sided clipped quadratic rule with \(\underline\mu_\nu\).
There is no outgoing gain.

## 3. Fixed input, output and execution limits

Use the same inherited accepted depth-18 box specified in the
next-four half-row evaluation note. It is the lexicographically
first deepest accepted leaf in
[the completed central record](../repro/results/research-mixed-next-four-adaptive-budget-attempt02.json):
\[
 \begin{gathered}
 \texttt{001111101111010111},\\
 \Re u\in[115337/512000,57677/256000],\qquad
 \Im u\in[8919/256000,279/8000].
 \end{gathered}
 \tag{7}
\]
Reconstruct it from the original root rectangle and alternating
dyadic splits, using saved addresses only. No accepted central
inequality is reevaluated. An accepted necessary-reference box
need not contain a realized word reference.

The proposed diagnostic has 160-bit precision, exactly one call
to the new two-scalar evaluator, and no subdivisions, alternate
boxes, continuations or automatic retry. It records both outward
scalar values against zero and \(-1/2000\), all trial components,
forces, curvature lower bounds and gains, and exact directed
rational endpoints. Failure of a sufficient majorant is not a
counterexample to the underlying source comparison.

Before and after evaluation, bind the actual map providers and
their inherited dependencies, completed central record, reference
helper and primitive bytes, their evaluation specification, the
next-four majorant, this note and the new driver. Require a fresh
output path. Implementation review and separate execution
authorization are required before the one diagnostic is run.
