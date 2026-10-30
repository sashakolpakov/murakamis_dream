# The current general frontier

The target is a theorem at **every fixed bridge width**, with independently long signed twists. The general volume equality remains open. Exact source formulas, the marked geometric action, and much of the local analysis are now available; the unresolved step is the global quantum period.

## The class and the order of quantifiers

Fix an essential $2k$-strand plat diagram $D$, $k\geq2$, with a hyperbolic augmented exterior $Y_D$ and its actual primitive cusp markings. The [general target](../../notes/general_augmented_plat_long_twist_target.md) asks for a threshold $T(D)$ such that

$$\min_i |m_i|>T(D)\quad\Longrightarrow\quad
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K_{D,\mathbf m})|
=\operatorname{Vol}(S^3\setminus K_{D,\mathbf m}).$$

The diagram and every signed twist number $m_i$ are fixed **before** the quantum level $N$ tends to infinity. The prescribed parity pattern must give a knot. Hyperbolicity of a knot does not automatically certify every chosen augmentation.

Under the actual positive marked gluing certificate, the [geometric filling theorem](../../notes/general_augmented_plat_long_filling_quantifiers.md) already supplies a geometric threshold, including independently long partial fillings. It is the quantum threshold in the displayed implication that remains unproved for general plats.

## What is established on this path

| Step | Current conclusion | Remaining limitation |
| --- | --- | --- |
| Original finite source | Exact all-color formulas at arbitrary fixed width; shared Kirchhoff flows, Fourier charges and all required normals retained | An exact formula alone does not estimate its coherent sum |
| Ordinary local factors | Selected action and nonzero amplitude on full physical complex compacts; a global Legendre chart for that selected action | The channel remains a genuine discrete color; normal bounds have their stated domains |
| Actual geometry | A positive marked certificate gives the complete geometry, its nearby stationary branch and the absolute hyperbolic-volume anchor | Existence of the geometric critical point does not prove quantum contribution |
| Exceptional matching edge | Exact Casimir polynomial, selected scalar action, original resolvent period, and controlled Green kernels on strict physical support | The surrounding coherent state and a contributing contour remain to be controlled |
| Endpoint and normals | Polynomial bounds at the closing point $z=2$, with genuine generic derivatives | A shrinking endpoint neighborhood does not control the entire connecting contour |
| General long fillings | A conditional source-to-filling theorem with the correct independent-slope quantifiers | Its general complex packet, nonzero density germ and whole-source gap still need proof |

The [selected-factor theorem](../../notes/actual_augmented_plat_selected_factor_localization.md) is useful here: for the certified right-angled cut, exactly two physical-support failures can be placed at the ends of one chosen crossing-circle edge. Every other ordinary factor is on the selected physical packet. An all-central selected common frame **cannot exist**; moving all factors into that domain is therefore not an available shortcut.

## The exceptional edge now has an exact algebraic description

Its completed operator is the original normalized polynomial

$$E_a=D_a^{-1}p_a(\Omega).$$

This is a generic identity before root specialization, so it retains the colliding channels and their true normal derivatives. The [source polynomial theorem](../../notes/actual_matching_edge_geometric_target_polynomial.md) also fixes which geometric target is required: $z=\operatorname{Tr}(B_{\rm in}^{-1}B_{\rm out})=2-4/c^2$, with the actual primitive rectangle ratio $c$.

The [marked-word bound](../../notes/actual_matching_circle_rectangle_bound.md) proves $0<c\leq1$ for every circle in the certified complete class, including retained half twists. Otherwise that actual holonomy word would be elliptic in a freely acting complete-manifold group. Thus the actual target is at most $-2$; equality is a genuine parabolic case.

Every zero of $p_a$ is above $2$. Its canonical logarithm selects a scalar action on the slit plane, without inventing a complex finite color. The [generating-action theorem](../../notes/actual_matching_edge_polynomial_geometric_action.md) proves the general local character relation

$$R+R^{-1}=2-(2-\lambda_{\rm in})\frac{z+2}{z-2},$$

with the branch and additive scalar normalization fixed by the original source. This is a general local A-structure result. It is not yet the global knot quantum A-operator or its selected period.

![The exact polynomial-resolvent period, the geometric target and spectral endpoint, and the remaining global contribution problem.](../figures/exceptional-period.png)

The [exact operator period](../../notes/actual_matching_edge_continuant_operator_period.md) keeps the distinction explicit:

$$p_a(\Omega)=\frac{1}{2\pi i}\oint_\Gamma p_a(z)(zI-\Omega)^{-1}\,dz.$$

Its Green entries have original forward and backward continuants and the full characteristic denominator. Their [selected action and generic-normal bounds](../../notes/actual_matching_edge_cross_central_green_action.md) hold when the two actual physical rows are strictly on opposite sides of the midpoint on the stated common spectral domain, which includes every fixed compact real interval below $-2$. On the anti-diagonal, the Green entry is exactly negative for real $z<-2$. Neither this sign nor the scalar action proves that the geometric saddle contributes to the contour.

The endpoint $2$ also has separate [polynomial](../../notes/actual_matching_edge_polynomial_endpoint_control.md) and [full resolvent](../../notes/actual_casimir_endpoint_resolvent_bound.md) estimates. They control the original derivatives through a shrinking neighborhood, including both level parities. The connecting contour still needs an estimate. This closing point $+2$ is distinct from the possible geometric target $-2$, which is outside the current off-spectrum Green theorem.

## How far this is from the general conjecture

**The main gap remains a substantial global theorem.** There are three concrete tasks:

1. Put the exceptional-edge integral and the actual surrounding state on compatible domains, retaining their shared physical variables, marks and phases.
2. Prove that the geometric critical point contributes with a nonzero controlled coefficient to the original finite source. A classical character relation or a scalar polynomial evaluation does not establish this.
3. Control the remaining physical regions and aliases uniformly in the auxiliary colors, so the general long-filling transfer applies.

The Fourier route is still useful. Its exact positive partition gives a weighted-Cauchy upper bound with all flow and charge constraints retained. Its radial optimizer cannot simply be declared geometric: the [radial-frame obstruction](../../notes/actual_positive_fourier_radial_geometric_obstruction.md) prevents assembling all strict ordinary radial saddles into the certified complete representation. No numerical rate gap follows from that obstruction.

Likewise, taking independent local projector maxima pays a genuine exponential boundary cost. The computed folded rate is $5v_3/\pi$ at both parities. The joint contraction must account for that cost rather than discard it as a normalization.

## Existing equality results and preserved alternatives

The [results chapter](results.md) states the internally reviewed equality theorems for the specified pretzel, belt-stack and signed robust Conway families. The latter permit arbitrary fixed branching and seed widths within their grammar, with independently sufficiently long fixed signed fillings. They do not exhaust arbitrary plats. The minimal isolated $C(h^3)$ mixed-color filling case and arbitrary short fillings remain outside the stated general filling theorem.

The [source-divisor transfer](../../notes/general_long_filling_source_divisor.md) can tolerate a leading density that vanishes at completeness if its analytic germ is nonzero. With the other hypotheses supplied, it gives equality outside an analytic exceptional divisor and density one of long slopes in signed boxes; a monomial times a unit gives all independently long slopes. This is still conditional for general plats.

The cube, Fourier, Karamata-inspired estimates, positive sewing and pointed torsor approaches remain in the [research library](../library.html). Their detailed arguments and failed intermediate estimates are preserved in the technical archive. This chapter records the current dependencies rather than requiring the reader to traverse every historical note.
