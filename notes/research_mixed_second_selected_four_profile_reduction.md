# Four remaining estimates for the second selected coordinate

Research theorem, 6 November 2026.

When only the second of the first two retained coordinates is selected,
the complete local finite sum now requires four upper-rate comparisons
instead of thirty-two. The first ordinary factor contributes only its
main-contour profile. The second contributes either its main contour
or its real half row. Each has the two original Fourier alternatives.
The uniform signs of these four comparisons remain open.

The same pointwise comparisons reduce the problem with both first
coordinates selected from 128 terms to 24. They do not yet give a
negative bound for either complete local sum.

## 1. Source, heights, and profile notation

Fix a positive word of length \(m\ge4\) in block types three and four,
with first three flags \((\alpha,1,\beta)\),
\(\alpha,\beta\in\{0,1\}\). Use the literal kernels, original
critical reference, and profiles of
[the second-selection reduction](research_mixed_second_selected_plateau_reduction.md).
Select the second coordinate at height
\[
 H_2=1/100,\qquad z_2=x_2+iH_2,\qquad x_1,x_2,x_3\in P=[.22,.45].
 \tag{1}
\]
Initially position 1 is unselected, so \(z_1=x_1+ic_1\);
position 3 is also unselected, with \(z_3=x_3+ic_3\).
All ordinary indices keep their original contour heights.

For factor \(j=2,3\), \(R_0^j\) is its bare main-contour maximum,
\(R_L^j\) its left real-cut value, \(R_R^j\) its real half-row
value, and \(R_1^j\) its full periodic last-row rate. The relevant
finite product is
\[
 \mathcal B_{23,N}
 =|C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)d_N(X_2)X_2^{-N}|
                     |d_N(X_1)|^{\alpha/2}|d_N(X_3)|^{\beta/2}.
 \tag{2}
\]
Keep its original two-boundary affine term \(\Lambda_{23}\).
The two full selected-weight rates are
\[
 W_2^{\mathrm{fac}}=-\Re g(z_2)-2\pi H_2,\qquad
 W_2^{\mathrm{force}}=0.
 \tag{3}
\]
No Fourier factor or boundary derivative is absorbed into a new
normalization.

## 2. Completed pointwise comparisons

The following comparisons hold independently of the real target
of the other factor.

| Profile being removed | Dominating profile | Strict gap | Proof |
|---|---|---|---|
| \(R_1^2\) | \(R_0^2\) | \(1/50\) | [Outgoing-selected last row](research_mixed_selected_outgoing_four_last_row_domination.md) |
| \(R_L^2\) | \(R_0^2\) | \(1/100\) | [Left cut of factor 2](research_mixed_second_selected_left_cut_domination.md) |
| \(R_R^2\) | \(R_0^2\) | \(1/30\) | [Half row of factor 2](research_mixed_second_selected_left_half_row_domination.md) |
| \(R_L^3\), \(\beta=0\) | \(R_0^3\) | \(1/125\) | [Incoming-selected type-three left cut](research_mixed_selected_three_left_rows.md) |
| \(R_L^3\), \(\beta=1\) | \(R_0^3\) | \(1/1000\) | [Left cut of factor 3, type four](research_mixed_second_selected_outgoing_four_left_cut.md) |

The first three use the fixed trial \(s=.3+i\Im s_2^*\).
Their containing domains include both possible attached first types:
\[
 -.078<c_1<.021,\qquad -.102<\Im s_2^*<-.001.
 \tag{4}
\]
The last-row comparison even permits the larger incoming interval
\([-.108,.068]\).
For factor 3, both its index and outgoing coordinate have ordinary
type-three heights in \((-.065,.068)\), or ordinary type-four heights
in \((-.102,-.001)\). These are exactly the respective hypotheses
of the last two comparisons. The type-three proof permits
\(0\le H_2\le7/625\), so it includes (1).

The new fixed-grid certificates are complete:

| Comparison | Whole-interval checks | Smallest saved lower bound |
|---|---:|---:|
| [Factor 2 last row](../repro/results/research-mixed-selected-outgoing-four-last-row-domination.json) | 128 | \(>0.0245897>1/50\) |
| [Factor 2 left cut](../repro/results/research-mixed-second-selected-left-cut-domination.json) | 128 | \(>0.0163984>1/100\) |
| [Factor 2 half row](../repro/results/research-mixed-second-selected-left-half-row-domination.json) | 32 | \(>0.0368288>1/30\) |
| [Factor 3 type-four left cut](../repro/results/research-mixed-second-selected-outgoing-four-left-cut.json) | 128 | \(>0.0018714>1/1000\) |

The displayed decimals are conservative summaries. Acceptance uses
the exact rational directed endpoints in each record. The proofs
first reduce the real targets and one height analytically, then
bound each whole remaining height interval by an outward midpoint
value and a proved Lipschitz correction. These are complete interval
bounds, not a grid of unqualified samples. Their scripts use the
original primitive and keep the asymmetric chirp.

The outgoing last-row comparison is different: it bounds a joint
profile by the original action rather than by another profile.
The [exact height-transport theorem](research_mixed_second_selected_outgoing_last_rows.md)
gives, for either \(\nu\),
\[
 R_0^2+R_1^3-\frac\alpha2\Re g(z_1)
                 -\frac\beta2\Re g(z_3)+W_2^\nu
 <\Lambda_{23}-\frac1{400}.
 \tag{5}
\]
It also retains a negative quadratic remainder, which may be
discarded for the present upper bound.

## 3. The complete finite product with position 1 unselected

Define the four-term defect
\[
 D_4=
 \max_{\substack{j\in\{0,R\}\\
          \nu\in\{\mathrm{fac},\mathrm{force}\}}}
 \left\{
 R_0^2+R_j^3-\frac\alpha2\Re g(z_1)-\frac\beta2\Re g(z_3)
                       +W_2^\nu-\Lambda_{23}\right\}.
 \tag{6}
\]

**Theorem 1.** For every \(\tau>0\), the entire finite product (2)
satisfies
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
      \exp N\{\Lambda_{23}+\max(-1/400,D_4)+\tau\}.
 \tag{7}
\]
The assertion includes both level parities and every finite row
and contour contribution of the original reduction.

*Proof.* Start with its thirty-two profiles. Each comparison in
the first three rows of the table replaces the indicated profile
of factor 2 by \(R_0^2\), leaving all other terms unchanged.
Only eight profiles remain. Equation (5) bounds the two with
right profile 1. The relevant last row of the table replaces the
two with right profile \(L\) by those with right profile 0.
The other four are precisely (6). Applying the original finite-current
bound with one total tolerance gives (7). \(\square\)

This is still an upper-bound reduction. A strict negative bound
for (6) must cover both main/main alternatives and both main/half-row
alternatives. The theorem does not assert that any of those four
functions is negative. In particular it does not yet add position 2
to the completed first-selection plateau theorem.

## 4. Both first coordinates selected

Now let \(\alpha=1\), select both first coordinates, and put
\(H_1=H_2=1/100\). The exact finite product is
\[
 \mathcal B_{123,N}
 =|U_{1,N}(w,X_1)C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)
                    d_N(X_1)X_1^{-N}d_N(X_2)X_2^{-N}|
                                  |d_N(X_3)|^{\beta/2}.
 \tag{8}
\]
Keep its original affine term \(\Lambda_{123}\).
The cap's main and left-cut profiles are \(A_0,A_L\); the existing
cap comparisons have already removed its other profiles. For
\(i=1,2\), set
\[
 W_i^{\mathrm{fac}}=-\Re g(z_i)-2\pi H_i,\qquad
 W_i^{\mathrm{force}}=0.
 \tag{9}
\]

The incoming height \(H_1=.01\) is inside the containing domains
of all three left-factor comparisons in Section 2. They therefore
still dominate \(R_1^2,R_L^2,R_R^2\) by \(R_0^2\).
The right-factor left-cut comparison is also unchanged.
No unselected joint supporting plane is used in these pointwise
replacements.

Consequently define
\[
 D_{24}=
 \max_{\substack{a\in\{0,L\},\ j\in\{0,R,1\}\\
                 \nu_1,\nu_2\in\{\mathrm{fac},\mathrm{force}\}}}
 \left\{A_a+R_0^2+R_j^3-\frac\beta2\Re g(z_3)
             +W_1^{\nu_1}+W_2^{\nu_2}-\Lambda_{123}\right\}.
 \tag{10}
\]

**Theorem 2.** For every \(\tau>0\),
\[
 \mathcal B_{123,N}\le C_\tau N^{A_\tau}
                       e^{N(\Lambda_{123}+D_{24}+\tau)}.
 \tag{11}
\]

*Proof.* Apply the same pointwise replacements in the 128-term
bound of Proposition 2 of the original reduction. Removing the
three non-main profiles of factor 2 leaves 32 terms. Removing the
right left-cut profile leaves \(2\cdot3\cdot2\cdot2=24\) terms,
exactly (10). All other factors and rates are common in each
replacement. The original complete finite-current estimate gives
(11). \(\square\)

Unlike (5), the last right profile is not paid here. Its old
height-transport proof kept the first coordinate at its reference
height, which is not the present situation. Hence right profile 1
remains explicitly in (10). All twenty-four signs remain open.

## 5. What the next comparison must prove

The [central budget](research_mixed_second_selected_central_budget.md)
and [index barriers](research_mixed_second_selected_horizontal_concavity.md)
give the exact coupled optimization for the two main/main terms
in (6). The
[reference curve](research_mixed_second_selected_reference_curve.md)
expresses their data through one original endpoint parameter,
with the original logarithmic lifts and both boundary derivatives.

The first
[prescribed diagnostic](../repro/results/research-mixed-second-selected-central-budget-diagnostic.json)
was inconclusive before evaluating any scalar budget: direct
interval propagation through the nested rational maps could not
certify that the first transferred shape was nonzero. It made two reference
calls and zero primitive or conjugate evaluations. It provides no
evidence for or against the central signs and excludes no reference.
A tighter correlated rational enclosure is needed before that
diagnostic can assess the proposed estimate.

The two main/half-row terms in (6) and the twenty-four terms in (10)
remain additional local comparisons. Even a proof of all of them
would leave the other boundary positions, nonplateau contributions,
whole-source boundary-color estimates, and arbitrary short partial
fillings required by the finite-exception objective.
