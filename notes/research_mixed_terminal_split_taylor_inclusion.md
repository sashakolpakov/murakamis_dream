# Affine-path and error-path Taylor bounds for terminal inclusion

Research protocol, 6 November 2026. The correlated affine run made
all sixteen full-tube contraction bounds less than one, but the
type-three input cases failed its inclusion test. The following
stronger inclusion test uses the same sixteen tubes and already
saved primitive bounds. It changes neither the predictor nor the
candidate radii, and requires no analytic evaluation.

## 1. Separate the two connecting segments

Use the original gradient, eleven rank-one terms, exact \(q^0,B,u\),
parameter radius \(r\), and error radii \(\rho\) of
[the correlated affine theorem](research_mixed_terminal_correlated_affine_family_certificate.md).
For \(\delta=b-b_0\), write
\[
 q^{\rm aff}=q^0+u\delta,\qquad q=q^{\rm aff}+\zeta,\qquad
 |\delta|\le r,\quad |\zeta_i|\le\rho_i .
 \tag{1}
\]
For primitive \(\ell\), retain
\[
 h_{\ell i}=|\sigma_\ell(Bv_\ell)_i|,\quad
 a_\ell=r|\lambda_\ell|,\quad
 d_\ell=\sum_j|v_{\ell j}|\rho_j,\quad
 E^0_{ij}=|(I-BJ_0)_{ij}|.
 \tag{2}
\]
All these symbols denote exact values or outward upper bounds as
specified in the original certificate. Let \(m_\ell^{\rm aff}\)
bound \(|j''|\) on the affine argument disk of radius \(a_\ell\),
and \(m_\ell^{\rm full}\) bound it on the full disk of radius
\(a_\ell+d_\ell\). The saved strip guards ensure every segment
below is regular on the original logarithm branch.

First integrate \(J(q;b)-J_0\) along the affine parameter path.
The original chirp has constant Jacobian, so throughout that path
\[
 |(I-BJ(q^{\rm aff};b))_{ij}|
 \le A_{ij}:=E^0_{ij}
       +\sum_\ell h_{\ell i}m_\ell^{\rm aff}a_\ell|v_{\ell j}|.
 \tag{3}
\]
The original residual bound is unchanged:
\[
                     |Bf(q^{\rm aff};b)|\le R .
 \tag{4}
\]
Now Taylor expand each primitive in the **error** displacement
\(v_\ell^{\mathsf T}\zeta\), at this same \(q^{\rm aff}\) and
fixed \(b\). For the fixed-point map \(T_b(q)=q-Bf(q;b)\),
\[
 |T_b(q^{\rm aff}+\zeta)-q^{\rm aff}|_i
 \le R_i+(A\rho)_i+Q_i(\rho),\qquad
 Q_i(\rho)=\frac12\sum_\ell
                      h_{\ell i}m_\ell^{\rm full}d_\ell^2 .
 \tag{5}
\]
The factor \(1/2\) is the integral Taylor remainder factor
\(\int_0^1(1-t)\,dt\). No stationarity of the affine predictor is
assumed, and all its residual is retained in (4).

## 2. A stronger certificate on the same candidate tube

**Theorem 1.** Suppose the original full-tube strip and central
canonical-root containment conditions hold. Retain any previously
proved contraction matrix \(E\ge0\) on this tube with
\[
                 \max_i (E\rho)_i/\rho_i<1 .
 \tag{6}
\]
If
\[
                    R+A\rho+Q(\rho)<\rho ,
 \tag{7}
\]
then the original canonical family satisfies
\[
 |q_{*,i}(b)-q_i^0-u_i(b-b_0)|<\rho_i
                          \quad(|b-b_0|\le r).
 \tag{8}
\]

Indeed, (5) and (7) map the same closed error polydisk strictly
into itself. The old full-tube contraction estimate is unchanged.
Banach's theorem supplies the root, and the original central
enclosure, local implicit uniqueness, and connected-disk analytic
continuation identify it exactly as in the correlated theorem.
The same argument gives continuity on the closed disk boundary.
No statement that the old failed inclusion test had succeeded
is used.

With the ideal displayed majorants, the difference between the old
inclusion cost and (5) is exactly
\[
 \begin{split}
 (E^{\rm full}\rho)_i-(A\rho+Q(\rho))_i
   =\sum_\ell h_{\ell i}\left[
     (m_\ell^{\rm full}-m_\ell^{\rm aff})a_\ell d_\ell
                       +\frac12m_\ell^{\rm full}d_\ell^2\right].
 \end{split}
 \tag{9}
\]
The regular-strip curvature formula is nondecreasing with disk
radius, so the right side is nonnegative. The two savings have
different sources: the affine displacement uses its smaller disk,
and the remaining error displacement has a quadratic Taylor
remainder rather than a full derivative-times-distance bound.
Independent serialization and upward reconstruction may add a tiny
outward enlargement; acceptance always uses the reconstructed
strict inequality (7), never an inferred comparison from (9).

This also gives a structured route to unequal error radii:
for any proposed vector \(\rho\), the explicit monotone inclusion
map is \(R+A\rho+Q(\rho)\), with the full argument radii and strip
bounds checked at that same vector. A formal inverse majorant from
a different tube is not an enclosure or a substitute for (7).
The present protocol does not choose any new vector.

## 3. Fixed saved-only protocol

The immutable source is the
[correlated result](../repro/results/research-mixed-terminal-correlated-affine-family.json),
SHA256 51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1.
Its completed saved-data audit is
[the rational reconstruction record](../repro/results/research-mixed-terminal-correlated-affine-family-saved-audit.json),
SHA256 2638c47a2b0216f04bb4f31e4f6bdd86d9c2b17cdfd00ea880835dcf80d97959.
The four \((\beta,\epsilon)\) cases and the four original multipliers
\(1/4,1/2,1,2\) are retained in their original order.

The standalone standard-library checker
[check_mixed_terminal_split_taylor_inclusion.py](../experiments/check_mixed_terminal_split_taylor_inclusion.py)
verifies the source, audit, proof and helper identities, all inherited
hashes, exact case associations, and all sixteen complete candidate
records. It uses the audit's conservative reconstructed residual
vector \(R\) and contraction bounds. It rebuilds (3) from the saved
center cotangents, the saved certified interval for \(\pi\), exact
\(B\), and the original affine curvature witnesses. It computes
(5) using the corresponding full-tube witnesses from the **same**
candidate.

As in the completed audit, center intervals are recombined by exact
rational arithmetic and outward hulls. Moduli use exact integer
square roots; curvature uses the saved positive sine interval.
Outward dyadic rounding is allowed only upward. Every analytic
primitive and sine interval remains a pinned source-bound input.
There are no analytic imports or callbacks, proposals, roots,
optimizers, new input boxes, subdivisions, changed radii, or retries.

The output retains all sixteen new margins, the unchanged
contraction bounds, and all failed coordinates. It reports successes
only after checking (7). The fixed output path is
repro/results/research-mixed-terminal-split-taylor-inclusion.json.
No successful type-three result is assumed by this protocol.
Even a complete reference enclosure would still leave uniform
phase and finite-source comparisons, as well as nonzero amplitudes,
to their separate arguments.
