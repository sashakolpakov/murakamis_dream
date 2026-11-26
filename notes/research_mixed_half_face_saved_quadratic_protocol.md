# A quadratic comparison using the frozen endpoint certificates

Analytic reduction and proposed protocol, 7 November 2026.
This calculation has not been executed. A standalone checker,
full static reviews, a frozen input manifest, and a root execution
instruction are required before evaluating any new certificate.

The earlier affine test completed and was inconclusive. Its
output and verdict remain unchanged. The present criterion uses
new proved curvature and a smaller outgoing-height allowance.
It requires only exact rational arithmetic on the lower
certificates already stored by that test. It does not repeat
any root, derivative, action, interval, or source calculation.

## 1. The new analytic inputs

The following results have written source proofs.

1. [Conditional curvature](research_mixed_half_face_conditional_curvature.md)
   replaces the two old affine upper costs by quadratic costs.
   With \(\delta=x-1/4\), their decreases are
   \(\mu_{\rm fac}\delta^2\) and \(\mu_{\rm force}\delta^2\), where
   \[
     \mu_{\rm fac}=\frac{143\pi}{384},\qquad
     \mu_{\rm force}=\frac{\pi}{3}.
   \]
2. [The conditional absolute bound](research_mixed_real_arc_conditional_absolute_decrease.md)
   reduces the outgoing-height allowance by
   \[
                 \Delta_H=\frac{12\pi H}{25},
                 \qquad H=1/100.
   \]
   On the whole real incoming interval it also supplies a
   nonnegative decrease \(\mathcal D(a)\), with \(\mathcal D(1/2)=0\).
3. [The complete cap upper bound](research_mixed_real_arc_complete_cap_upper.md)
   uses the same fixed cap ceiling
   \[
             \widehat M=\frac{203}{200}-\frac{1303}{7680000}
   \]
   throughout \(1/2\le a\le7/10\), with a strict uniform reserve.
   It estimates the entire finite cap, all real ordinary colors,
   and its stated local complex derivatives.

Consequently the two old upper costs \(\bar L_\sigma(x)\) of
[the affine protocol, equation (6)](research_mixed_half_face_saved_affine_protocol.md)
may be replaced, for the whole complementary real-arc density, by
\[
 \bar L_\sigma(x)-\mu_\sigma(x-1/4)^2-\Delta_H-\mathcal D(a).
 \tag{1}
\]
The old upper bound \(73/500\) for \(-J(1/4)\), all normalizations,
the third-factor allowance \(7/250\), both Fourier alternatives,
and the original halfweight allocation are unchanged.
For a uniform sufficient comparison we may drop
\(\mathcal D(a)\ge0\) and the additional positive cap reserve.

This is a different analytic inequality, rather than a change of
precision or a refinement of the old cells.

## 2. Meaning of the stored lower certificates

Retain the same five-variable following sheet, the same reduced
disks \(P_3,P_4\), and the same quantities \(A(c),p(c),q(c)\)
from the affine protocol. Its input \(c\) is the coordinate
\(s_3^*\) of the initial \(34\) half-chain; it is not the further
external coordinate \(s_4^*\).

For either alternative, define the old exact gap
\[
 g_\sigma(c,x)
   =A(c)+p(c)\{x-\Re q(c)\}-\bar L_\sigma(x).
 \tag{2}
\]
For each fixed \(c\), this is affine in \(x\).

The sole completed old result is

    repro/results/research-mixed-half-face-saved-affine-attempt01.json

with SHA256
533f8dd9663b920b541c2f7e3252d12153fb6d16dfe726c615da9d63148092c2.
Its manifest is

    repro/protocols/research-mixed-half-face-saved-affine.json

with SHA256
a71b93551de6fb5a8137988cef3cad860cbf3894c5f369babd3ab978c6ba0b04.
The [outcome record](research_mixed_half_face_saved_affine_outcome.md)
preserves its inconclusive verdict and complete inventory.

For a cell \(k\) on circle \(\nu\), let \(m_{\sigma,k,-}\)
and \(m_{\sigma,k,+}\) be the exact rational strings in the
field named exact_final_certificate_lower for the corresponding
left and right comparisons. Their meaning, proved by the old
protocol and checker, is
\[
 g_\sigma(c,x_\pm)\ge m_{\sigma,k,\pm}+b_\nu
 \quad(c\hbox{ in the whole boundary cell }k),
 \qquad b_\nu=\frac{B_\nu\rho_\nu^2}{2}.
 \tag{3}
\]
Here \(x_-=11/50,\ x_+=9/20\). The stored certificate already
subtracts the full-disk debit \(b_\nu\). It must not be
subtracted a second time.

Neither \(m_-\) nor \(m_+\) need be positive. Their validity as
lower bounds is independent of the old test's failure to make
them all positive.

## 3. A complete quadratic certificate

Put
\[
 d_-=-3/100,\qquad d_+=1/5,\qquad
 s_{\sigma,k}=
 \frac{m_{\sigma,k,+}-m_{\sigma,k,-}}{d_+-d_-}.
 \tag{4}
\]
Positive affine interpolation in \(x\) in (3) gives
\[
 g_\sigma(c,x)-b_\nu
   \ge m_{\sigma,k,-}+s_{\sigma,k}(\delta-d_-)
                 \qquad(d_-\le\delta\le d_+).
 \tag{5}
\]
This slope belongs to a lower chord; it is not an enclosure
of the true marginal \(p(c)\).

Use only the following fixed rational weakenings:
\[
 \underline\mu_{\rm fac}=\frac{3575}{3072},\qquad
 \underline\mu_{\rm force}=\frac{25}{24},\qquad
                         \underline\Delta=\frac3{200}.
 \tag{6}
\]
They follow from \(\pi>25/8\). Since \(\delta^2\ge0\), they
give lower bounds in the required direction. Define
\[
 \begin{split}
 P_{\sigma,k}(\delta)
   &=m_{\sigma,k,-}+s_{\sigma,k}(\delta-d_-)
       +\underline\mu_\sigma\delta^2+\underline\Delta,\\
 \delta_{\sigma,k}
   &=\max\{d_-,\min\{d_+,-s_{\sigma,k}/(2\underline\mu_\sigma)\}\},\\
 \gamma_{\sigma,k}&=P_{\sigma,k}(\delta_{\sigma,k}).
 \end{split}
 \tag{7}
\]
Everything in (7) is an exact rational operation on saved
rational lower bounds. The clipped point is the exact minimum
of this convex quadratic on the full interval.

**Proposition.** If every \(\gamma_{\sigma,k}>0\), over both
alternatives and every cell of both complete circles, then the
improved comparison holds uniformly for every \(x\in[11/50,9/20]\)
on both full reduced disks.

*Proof.* Let \(D_\sigma=-g_\sigma\) be the old deficit. Its
Laplacian in \(c\) has the already proved lower bound
\(\Delta_cD_\sigma\ge-2B_\nu\) on each disk. Subtracting
\(\mu_\sigma\delta^2+\Delta_H\), which is independent of \(c\),
does not change this Laplacian or any angular derivative.

Equations (5)--(7) say that on the whole boundary cell the
improved gap is at least \(b_\nu+\gamma_{\sigma,k}\).
The cells exhaust the boundary. Their finite positive minimum
\(\gamma\) therefore bounds the improved deficit above by
\(-b_\nu-\gamma\) on the entire boundary, for every fixed \(x\).
The same disk barrier as in the old protocol adds at most
\(b_\nu\) in the interior. Hence the improved deficit is at
most \(-\gamma\) throughout the disk. Both alternatives are
retained. \(\square\)

By (1) and the original third-factor plane, success would
give a strict bound below \(\Lambda_{123}\) for the complete
selected density on the real incoming arc \(1/2\le a\le7/10\).
Finite contour densities and bounded integration lengths cost
only powers of \(N\); the reserve absorbs the small tolerances.

This concerns the real arc. It does not estimate the original
incoming vertical connector or finish a complete \(343\),
\(344\), or arbitrary short-filling theorem.

## 4. Fixed inventory and permissible calculation

There are exactly 1,024 old cells: all 512 c3 cells, followed
by all 512 c4 cells, in their saved order. Each contains four
old comparisons in this order:

1. factorial_left, at \(11/50\);
2. factorial_right, at \(9/20\);
3. forcing_left, at \(11/50\);
4. forcing_right, at \(9/20\).

The new calculation consists of exactly two applications of
(7) per cell, first factorial, then forcing: 2,048 quadratic
minima in all. No cell or insufficient old endpoint is omitted.
The checker must retain both endpoint strings, the exact slope,
clipped minimizer, exact minimum, and sign for every comparison.

Its only mathematical inputs are the 4,096 stored rational
endpoint lower certificates and the fixed rational constants
(4), (6). In particular:

* no real or complex interval is decoded;
* no old midpoint, derivative, transport debit, inverse,
  product maximum, or disk debit is recomputed;
* no primitive, action, root, inclusion, Hessian, contour,
  or original finite quantum source is evaluated;
* no precision, subdivision, choice of constant, or alternate
  test depends on the outcome.

The fixed implementation may use Python's exact integer and
fraction arithmetic, JSON, file reads, and hashing. It must
not import the old checker or an interval or special-function
library.

## 5. Provenance, execution gate, and interpretation

Before execution, a new manifest must bind this protocol,
the standalone checker, the analytic inputs in Sections 1--2,
the old result and manifest, and every file binding of the
old manifest. It must include exact-hash root and independent
static reviews of the new protocol and checker. The old
dependency and failure records remain intact. Mutable progress
notes and the new output must not be mathematical input bindings.

The checker must verify the complete old inventory, its
completed status, and its verdict
complete_inventory_recorded_affine_test_inconclusive before
using its certificates. Missing entries, changed hashes,
invalid rational strings, or inconsistent labels block the
calculation. It must not repair them silently.

The sole proposed output is

    repro/results/research-mixed-half-face-saved-quadratic-attempt01.json

It is created exclusively and must never overwrite an existing
attempt. Root alone may execute it, once, after the stated
reviews and manifest are complete. There is no preliminary
numerical run, retry, refinement, or replay. All insufficient
or failed comparisons remain in the result. Success requires
every one of the 2,048 minima to be strictly positive; otherwise
the outcome is inconclusive.

No comparison has been performed in preparing this protocol.
The proposition's hypotheses have not been established, and
no real-arc gap is asserted. The old affine test remains a
completed, inconclusive calculation under its unchanged criterion.
