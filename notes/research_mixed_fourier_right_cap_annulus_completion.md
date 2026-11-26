# The actual Fourier endpoint belongs to the ordinary type-three source domain

Research theorem, 7 November 2026. The sole fixed rational crossing test
passed. For every incoming leg in \(K_3\cup K_4\), the auxiliary leg
of the original correlated own-four Fourier endpoint belongs strictly
to \(K_3\). This settles its reference-domain obligation. It does not
assert the false independent-disk inclusion or a whole right-cap bound.

## 1. The completed fixed record

The [annulus protocol](research_mixed_fourier_right_cap_annulus_protocol.md)
and its [standard-library checker](../experiments/check_mixed_fourier_right_cap_annulus.py)
were fully reviewed and frozen before the single execution.
The immutable compressed
[result](../repro/results/research-mixed-fourier-right-cap-annulus.json.gz)
has SHA-256

    af2a3d9875b281db1327bb0b114515018ae1aa518dcb394767c1e91fea9b967a

The checker and protocol hashes are respectively

    39337ada17af9122286050c4bcc9b04edc4707983072ce8ee56d1bbda01f316d
    3069c8412a7a9b58e0c55597462d437394be15030ebf239f77e81f198b8d2e90

All eight quarter-circle charts and all 512 closed cells completed.
Each cell has a strict exclusion witness. The record retains all
9,728 prescribed polynomial upper bounds and all 145,920
degree-fourteen Bernstein coefficient intervals, including the filters
that were not needed for the first exclusion. All 33 elementary
rational preflight witnesses passed. There were no unexcluded cells,
errors, refinements, alternate choices, retries, analytic evaluations,
root solves, gain evaluations or source replays.

All 27 input bindings were unchanged before and after. The sole
analytic bound input was the full saved \(K\) enclosure from the
[original boundary-map record](../repro/results/research-mixed-fourier-boundary-update.json),
SHA-256

    5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514

It retains the entire original certified algebraic root square,
rather than its center. Its \(K\)-field canonical hash is
\(00f030c9a079403c2811e9b1c0dcca898ca8d912f4c11c0e338b3cc655a89591\);
the original root-certificate canonical hash is
\(f04e925c094ba2f2c6723d3321cb58ac4988255b52e3408c2895b662bcf1cf8f\).
Read-only inspection of the saved final summary and source associations
confirmed these identities, the complete inventory, and all 27 current
file hashes. That inspection did not replay the polynomial arithmetic.

## 2. The correlated containment theorem

Keep the original compact domains
\[
 \begin{split}
 P_3&=\{|z-(.35-.01i)|\le.083\},&
 P_4&=\{|z-(.30-.052i)|\le.060\},\\
 K_3&=P_3\cap\{-.072\le\Im z\le.068,\ 
                       \Re z-3\Im z\le.608\},&
 K_4&=P_4\cap\{-.108\le\Im z\le-.001\}.
 \end{split}
 \tag{1}
\]
For each \(a\in\mathcal K=K_3\cup K_4\), let
\((s(a),q(a))\in O_4^2\) be the unique original-log critical
pair of \(Q_1(s;a,q)+\ell_q(x_0)\), as in the
[correlated endpoint theorem](research_mixed_fourier_right_cap_correlated_endpoint.md).
Set \(Y=K=e^{2\pi ix_0}\) and
\[
 \beta_K(q)=-\frac1{2\pi i}
  \operatorname{Log}
  \frac{1-Ke^{-2\pi iq}}{K+(1-2K)e^{-2\pi iq}} .
 \tag{2}
\]
This is the already calibrated lower-half-plane logarithm branch.
No new logarithm or exponentiated critical branch is selected.

**Theorem 1.** Uniformly on the whole actual correlated family,
\[
 \frac23<
 \left|e^{-2\pi i\beta_K(q(a))}\right|
 <\frac32,\qquad
 |\Im\beta_K(q(a))|<\frac{13}{200},\qquad
 \beta_K(q(a))\in\operatorname{int}K_3 .
 \tag{3}
\]
The incoming leg keeps its original type: the assertion covers
both \(a\in K_3\) and \(a\in K_4\).

*Proof.* Write \(A=e^{-2\pi ia}\), \(S=e^{-2\pi is(a)}\),
\(Q=e^{-2\pi iq(a)}\), and \(B=e^{-2\pi i\beta_K(q(a))}\).
The original equations give
\[
 B=\frac{1-YQ}{Y+(1-2Y)Q},\qquad
 S=1+Y^{-1}-Q-\frac{Y^{-1}-1}{Q},\qquad
 A=\frac{1-SQ}{S(1-SQ)+(1-S)^3}.
 \tag{4}
\]
All denominators are nonzero on the actual family, by the original
filtered equations. The protocol proves nineteen strict necessary
polynomial inequalities at every possible crossing of either circle
\(|B|=2/3\) or \(|B|=3/2\). Clearing denominators is legitimate
there and introduces no extra actual crossing.

The eight exact charts cover both entire circles, including every
shared endpoint. On each of their 64 fixed closed cells, the saved
Bernstein bound makes at least one necessary polynomial strictly
negative throughout the cell. Its nonnegative Bernstein basis and
partition of unity prove this for the whole cell, not just its
endpoints. Thus neither circle intersects the actual family.

The sets \(K_3,K_4\) are convex and share \(.325-.031i\);
their union is connected. Original existence, zero lifts and
uniqueness make \(a\mapsto B(a)\) continuous on that union.
At the calibrated alternating input \(a=z_3^*\), the output is
\(s=q=z_4^*\) and \(\beta_K(q)=z_3^*\). Its original
height lies between \(-.03\) and \(.015\), so the elementary
exponential bounds in the protocol put this anchor strictly between
the two circles. Connectedness and absence of crossings establish
the first assertion of (3).

Since \(|B|=e^{2\pi\Im\beta_K(q)}\), and the protocol's
fixed elementary witness proves \(e^{.13\pi}>3/2\), the
annulus implies \(|\Im\beta_K(q)|<.065\). The earlier
[whole-disk boundary inclusion](research_mixed_fourier_boundary_critical_existence.md),
equation (5), also gives
\[
       |\beta_K(q)-(.35-.01i)|<.082<.083 .
 \tag{5}
\]
Together these put the auxiliary leg inside the ordinary
type-three disk and strictly inside both height bounds of \(K_3\).
The slanted side follows from the proved \(O_3\subset K_3\)
comparison in
[typed envelopes](research_mixed_typed_last_row_envelopes.md),
equations (5)--(6); that comparison has strict room throughout
the closed ordinary height strip. Hence the final inclusion in
(3) is strict. \(\square\)

Compactness gives positive uniform separation from every boundary
of \(K_3\). The original critical branch and (2) continue
holomorphically near this compact family. Consequently, after a
fixed sufficiently small change of the outgoing Fourier parameter
from \(x_0\), the same auxiliary legs still lie in
\(\operatorname{int}K_3\). This is a local parameter-neighborhood
consequence, not an assertion on a whole Fourier period.

## 3. Source consequence and remaining estimates

For an actual last ordinary vertex of type four, its exterior pair
\((a,\beta_K(q(a)))\) now belongs to the correct
\(K_{3+\eta}\times K_3\) source product. The original coupled
equations and zero-lift identities identify the reference with the
one in the completed ordinary conditional-source comparisons.
Those comparisons may therefore be invoked with their original
target domains, physical heights, incoming marginal and two
halfweight allocations.

This does not remove the outgoing halfweight from those theorems.
Removing it at rate level adds the \(g(q)/2\) Bregman term, and
no finite \(d_N\) factor may be divided out. Independently, the
[bare inner-contour deduction](research_mixed_fourier_right_cap_bare_inner_contour.md)
pays the bare main sheet and the inner aliases directly and
isolates three real-row comparisons. Their signs and the outgoing
\(q\)-source's physical tails, aliases and joins remain separate
obligations.

Finally, the earlier
[independent-disk failure](research_mixed_fourier_boundary_saved_domain_result.md)
is unchanged: \(\beta_K(D_4)\subset K_3\) is false on that
larger independent domain. The theorem above proves containment
only after retaining the exact original coupled relations (4).
It proves no whole right-cap sign, global boundary contraction,
ordinary-knot noncancellation, or cofinite assignment theorem.
