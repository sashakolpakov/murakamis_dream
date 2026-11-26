# Boundary responses with a first block of type three

Research implementation specification, 6 November 2026. This is the
first-flag-zero version of the
[original response specification](research_mixed_second_selected_external_response.md).
It uses the original canonical reference for flags \((0,1,\beta)\),
\(\beta\in\{0,1\}\), and implements the changed incoming marginal
proved in the
[first-three extension](research_mixed_second_selected_first_three_extension.md).
No reference, derivative enclosure, scalar sign or numerical response
bound is established by this specification.

## 1. Original response coefficients

Write
\[
 q=(e,\xi,a,u,z,v,b),\qquad c=s_4^*,\qquad
 f^{(0,\beta)}(q_*(c);c)=0,\qquad k(w)=\pi\cot(\pi w).
 \tag{1}
\]
The original seven-gradient system and its uniform residual theorem are
those of [residual localization](research_mixed_prefix_residual_localization.md),
with first flag zero. In particular the changed gradient rows are
\[
 f_e=-j(e-\xi)+j(e+a)+i\pi(\xi-a),\qquad
 f_a=j(e+a)+j(a+u)-2j(a)+i\pi(u-e),
 \quad j=J'.
 \tag{2}
\]
If \(H=f_q\), the changed diagonal entries are
\[
 H_{ee}=-k(e-\xi)+k(e+a),\qquad
 H_{aa}=k(e+a)+k(a+u)-2k(a).
 \tag{3}
\]
All other entries have the forms in the original response specification.
The forcing and derivative equation remain
\[
 f_c=e_b\{k(b+c)+i\pi\},\qquad Hq_*'+f_c=0.
 \tag{4}
\]
The caller must supply a certified derivative of this first-type-three
reference. The module neither evaluates (2) nor inverts \(H\).

The allocated phase has no incoming halfweight:
\[
 F_0=Q_1(u;a,z)+Q_\beta(v;z,b)-g(z)-\frac{\beta}{2}g(b).
 \tag{5}
\]
Its incoming and outgoing marginals are
\[
 p_L=g'(a+u)-g'(a)+2\pi iu,\qquad
 p_R=g'(v+b)-(1+\beta/2)g'(b).
 \tag{6}
\]
Since \(g''=k-i\pi\), differentiating along this same reference gives
\[
 \begin{aligned}
 L_a&=k(a+u)-k(a),& L_u&=k(a+u)+i\pi,\\
 R_v&=k(v+b)-i\pi,&
 R_b&=k(v+b)-(1+\beta/2)k(b)+i\pi\beta/2,\\
 p_L'&=L_a a'+L_u u',&
 p_R'&=R_v v'+R_b b',\\
 \mathcal B_0&=|p_L'a'|+|p_R'b'|.
 \end{aligned}
 \tag{7}
\]
Thus the former \(3k(a)/2\) coefficient becomes \(k(a)\), and
the former \(i\pi a'/2\) term disappears. The incoming chirp
and outgoing \(\beta/2\) halfweight remain. There is no conjugation
in the two holomorphic products in (7). Their moduli also bound
the signed responses with conjugated coordinate derivatives in the
Laplacian identity.

## 2. Domains and conditional input contract

The endpoint theorem gives the strict necessary ranges
\[
 \begin{aligned}
 e&\in(.376,.438)+i(-.019,.037),\\
 \xi&\in(.218,.242)+i(.049,.077),\\
 a&\in(.278,.391)+i(-.072,.021),\qquad a\in P_3,\\
 P_3&=\{|w-(.35-.01i)|\le.083\},\qquad
 P_4=\{|w-(.30-.052i)|\le.060\}.
 \end{aligned}
 \tag{8}
\]
The attached coordinate \(a\) is not assigned the ordinary
type-three height interval. The remaining necessary ranges are
\[
 \begin{aligned}
 u,z&\in P_4\cap([.24,.36]+i[-.102,-.001]),\\
 v,b&\in
 \begin{cases}
 P_3\cap([.267,.433]+i[-.065,.068]),&\beta=0,\\
 P_4\cap([.24,.36]+i[-.102,-.001]),&\beta=1.
 \end{cases}
 \end{aligned}
 \tag{9}
\]
For an external chart rectangle \(C\), the certified reference and its
derivative are required only for actual parameters in \(C\cap K_j\),
where
\[
 \begin{aligned}
 K_3&=P_3\cap\{-.072\le\Im c\le.068,\ \Re c-3\Im c\le.608\},\\
 K_4&=P_4\cap\{-.108\le\Im c\le-.001\}.
 \end{aligned}
 \tag{10}
\]
The external leg is attached at word length four and ordinary at greater
lengths. Its canonical existence and zero original logarithmic lifts
come from the reference theorem, not from a response calculation.

The common product required of the full supplied coordinate boxes is
\[
 E\times U\times Q^5,\quad
 E=[.33,.47]+i[-.09,.08],\quad
 U=[.21,.25]+i[.01,.10],\quad
 Q=[.23,.45]+i[-.12,.12].
 \tag{11}
\]
The module also requires the strict whole-box height conditions
\[
 \begin{gathered}
 -.078<\Im a<.021,\qquad -.102<\Im u<-.001,\\
 (\Im v,\Im b)\in
 \begin{cases}(-.065,.068)^2,&\beta=0,\\
 (-.102,-.001)^2,&\beta=1.
 \end{cases}
 \end{gathered}
 \tag{12}
\]
The incoming interval in (12) is the unchanged boundary-extension
condition; it is consistent with the stronger necessary lower bound
in (8). The full original target-product and concavity premises remain
those of the stationary boundary-extension theorem.

Necessary endpoint, typed-disk and external-domain tests are recorded
for inspection, using the closed enclosures of the strict ranges.
They are not a complete admissibility test and are not used to clip
the supplied boxes. The caller retains the original common-reference,
pair-sum and regularity obligations. In particular a residual provider
must validate its full raw affine image and connecting segments before
any independently justified pointwise root enclosure is used here.

## 3. Outward implementation and provenance

The new
[provider](../experiments/mixed_second_selected_first_three_external_response.py)
exports the same evaluate_response(coordinates, qprime, beta, *, pi=None)
API and the alias evaluate. The coordinate inventory is exactly
e,xi,a,u,z,v,b,c; the derivative inventory is exactly the first seven,
all differentiated with respect to the same complex \(c\).
All entries are supplied outward complex balls. An optional pi is a
certified enclosure of \(\pi\).

As in the frozen provider, the four cotangent arguments are
\(a,a+u,b,v+b\). Their whole real intervals must lie in \((0,1)\).
The provider evaluates \(\pi\cos(\pi w)/\sin(\pi w)\) only after a
Cartesian separation of the sine from zero. It records every argument,
sine, cosine, cotangent, coefficient, marginal derivative and product.
A failed regularity or finiteness check is inconclusive.

If the directed modulus intervals are \([l_L,h_L]\) and
\([l_R,h_R]\), the output stores the exact rational bounds
\[
 \max(0,l_L)+\max(0,l_R)\le\mathcal B_0\le h_L+h_R.
 \tag{13}
\]
Status enclosed requires a finite bound and both full-box conditions
(11)--(12). The output always identifies alpha=0 and leaves
canonical_existence_certified_here and qprime_certified_here false.
No coordinate clipping, root proposal, inverse evaluation or scalar
budget call occurs. The calculation uses four sine calls, four cosine
calls and two complex moduli, with at most one pi enclosure.

The exported PINNED map binds this specification, the first-three
extension theorem and the frozen mechanical source. A calling driver
must verify these hashes before and after its run and bind the new
provider's own bytes. The module performs no numerical work on import.
All first-type-four providers, records and response bounds remain
unchanged; none supplies a numerical value for \(\mathcal B_0\).

## 4. What a completed boundary calculation would imply

For each fixed \((\beta,j)\), a complete boundary cover must establish
both original scalar alternatives \(D_\nu\le-\gamma_i\), all required
whole-image domains and heights, and a bound \(\mathcal B_0\le B_i\).
With independent extrema over the entire boundary, put
\[
 \gamma=\min_i\gamma_i,\qquad B_*=\max_iB_i,\qquad
 \eta_j=\gamma-\frac{r_j^2}{2}B_*,
 \quad r_3=.083,\quad r_4=.060.
 \tag{14}
\]
The stationary extension theorem gives \(D_\nu\le-\eta_j\) throughout
\(K_j\) if \(\eta_j>0\). Boundary height conditions extend by harmonic
maximum and minimum principles. Every clipping segment and junction is
included in the boundary coverage. The disk-loss coefficients are
\(6889/2000000\) and \(9/5000\), respectively.

This applies the maximum principle to the original phase defect with
its two complex affine tangents. It makes no subharmonicity assertion
about a scalar majorant and does not substitute cellwise compensated
gaps for the independent global extrema in (14). No boundary sign,
interior sign, finite-source gap or completed parameter cover is claimed
by the provider or this specification.
