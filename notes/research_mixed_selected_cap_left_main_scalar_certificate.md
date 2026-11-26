# A bounded certificate for the two cap-left/main scalar bounds

Research construction, 6 November 2026. The new
[driver](../experiments/certify_mixed_cap_left_main_budget.py) applies
the already reviewed
[diagnostic evaluator](../experiments/diagnose_mixed_cap_left_main_budget.py)
to the full original auxiliary rectangle. It adds coverage and
stopping logic without changing the two scalar functions, reference
filters, centered primitive, or gain arithmetic. This note asserts
no execution or completed uniform sign.

## 1. Conditional conclusion and the precise tests

Keep the actual first-four/next-three open critical references with
\(m\ge3\), all later types in \(\{3,4\}\), the original outgoing
tangent, and \(H=7/625\). Use the definitions and corrected trial
action of the
[cap-left/main majorant theorem](research_mixed_selected_cap_left_main_majorant.md).
For \(\nu=0,1\), the tested upper bound is
\[
 \mathcal J_\nu=
 \mathcal L_\nu+
 \Gamma_{2\pi\delta_*}(-d;\ .2-\Re s_*,0)
 +\Gamma_{\mu_\nu}(\beta_\nu;\ .22-\Re z_*,.45-\Re z_*),
 \quad
 \delta_*=\min\{\Re\cot\pi s_*,15/53\},\quad
 \mu_\nu=(23+18\nu)\pi/120.
 \tag{1}
\]
The diagnostic uses lower enclosures for the positive curvatures,
which can only increase this upper bound. It retains \(d\ge0\),
the actual difference \(S(.27)-S(e_*)\), and the exact incoming
chirp. The outgoing trial gradient is identically zero after
subtracting the original outgoing marginal.

**Conditional conclusion.** A complete successful record proves,
for both full Fourier alternatives and every \(y,v\in P=[.22,.45]\),
\[
 A_L(y)+B_0(y,v)+W_\nu(y)
                  <M+\ell_b(v)-1/2000,\qquad \nu=0,1.
 \tag{2}
\]
Indeed the majorant theorem bounds the supremum of the left side
minus \(M+\ell_b\) by \(\mathcal J_\nu\). Both tests must
pass strictly below \(-1/2000\) on every retained reference cell.
No independent maximization of reference actions, increments or
slopes is used.

## 2. Original reference family and branches

The cover starts at exactly
\[
 \Re u\in[217/1000,234/1000],\qquad
 \Im u\in[27/1000,45/1000],\qquad U=e^{2\pi i u}.
 \tag{3}
\]
It calls the unchanged reference function from the
[frozen half-row driver](../experiments/certify_mixed_selected_half_row_budget.py).
That function uses the original rational maps, coordinate rectangles,
nonprivate reduced disks, coupled sums
\(\Re(z_*+s_*)\in[.589,.77]\) and
\(\Re(s_*+b_*)\in[.635,.77]\), and the next external
\(K_3\cup K_4\) condition of the first-four/next-three central proof.
The next external leg may be attached, including \(m=3\).
The later types therefore remain unrestricted within \(\{3,4\}\).
An exclusion requires a whole interval contradiction to a necessary
reference condition. Nonfinite or inconclusive intervals are retained.
The same proved coordinate-range intersections are performed after
the necessary filters.

The exact primitive is
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi i w})-\pi^2/6}{2\pi i},
 \qquad g'(w)=\Log(1-e^{-2\pi i w}).
 \tag{4}
\]
Every argument must be enclosed in \(0<\Re w<1\). The
[centered enclosure proof](research_mixed_centered_primitive_enclosure.md)
then permits
\[
 g(W)\subseteq g(w_0)+g'(W)(W-w_0),
 \tag{5}
\]
where \(w_0\) is the exact dyadic center and its value is enclosed
by the original primitive in (4). The rectangle and its connecting
segments stay inside the original regular strip, so there is no new
logarithmic or dilogarithmic branch choice.

The same centered primitive is used inside the unchanged phase
helpers. The actual private action uses the auxiliary \(u\) itself;
the fixed left-cut action uses the original canonical radical and
arctangent formula at \(.27\). No critical root is proposed or
solved. The cap action difference in the corrected equation (23)
is formed before taking the real bound. Its ordinary height change
uses exactly \(z_H^*-z_*=i(H-\Im z_*)\), preserving the chirp
without a spurious independent real displacement.

## 3. Exact gain bounds and strict acceptance

For each reference box the evaluator takes the exact rational lower
endpoint of \(\pi\), and a rational lower bound
\[
 \delta_{\rm lo}=
 \max\{1/5,\min(\inf\Re\cot\pi s_*,15/53)\}.
 \tag{6}
\]
The proved fixed-height directional estimate makes
\(2\pi_{\rm lo}\delta_{\rm lo}\) a valid lower curvature for
the negative index displacement. With
\(d_{\rm up}\ge d\ge0\) and
\(L_{\rm up}\ge\Re s_*-.2\), it computes
\[
 t=\min\{L_{\rm up},d_{\rm up}/(2\pi_{\rm lo}\delta_{\rm lo})\},
 \qquad
 G_s=d_{\rm up}t-\pi_{\rm lo}\delta_{\rm lo}t^2.
 \tag{7}
\]
This is exact rational arithmetic. Positive index displacement has
nonpositive linear contribution and needs no gain.

The incoming curvature lower bound is
\((23+18\nu)\pi_{\rm lo}/120\). The unchanged exact rational
two-sided clipped-gain helper bounds both possible incoming
displacement directions, including endpoint maxima. The outgoing
gain remains zero. The driver accepts a cell only when the rational
serialized upper endpoint of each final majorant is strictly below
\(-1/2000\). Thus displayed ball-rounding cannot hide a failed
comparison.

## 4. Coverage, stopping, and scope

The single proposed attempt uses 160-bit arithmetic, at most 8,000
visits, and maximum depth 20. It bisects the two auxiliary axes
alternately, real first. Only the new diagnostic evaluator is called;
neither frozen half-row inspect nor any earlier cover is replayed.

The attempt stops immediately at its first inconclusive depth-20
leaf, retaining that leaf's component diagnostics and the complete
unvisited frontier. It also stops at the visit cap. Accepted and
excluded leaves, together with unresolved leaves and pending boxes,
must have prefix-free binary addresses and exact dyadic mass one.
Only a complete partition consisting of accepted or necessarily
excluded leaves permits proved status.

The record saves both rational accepted upper endpoints, all trial
components and gains, every pending box, and the bound script and
proof hashes. All inherited frozen dependencies, the diagnostic
record, the new driver, and this note are checked before and after
the run. The output path must be fresh; there is no automatic retry,
continuation, precision increase, or additional subdivision budget.

A partial record establishes no uniform sign. Even a complete
record would prove precisely (2), with its complementary half-row
comparisons supplied separately. It would not by itself prove the
global open-source comparison or the cofinite hyperbolic
filling-volume theorem.
