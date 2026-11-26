# Independent check of the preferred main-longitude calculation

1 November 2026. Read-only mathematical check of
`/private/tmp/md-general-conway-preferred-main-longitude-translation.md`,
final input SHA256 `def6e731a84429d678e14801c4a278936b818b02be4abc31933dc810dce13ab1`.
No repository source was edited.

## 1. Oriented affine addition

The local arc multiplier is \(-d_jd_k\), with \(d_j=(-1)^j\), because an inward arc has oriented meridian \(d_j\) times the local unit and an outward arc has \(-d_k\) times that unit. The displacement \(-d_k\beta\) is unchanged when both traversal and meridian orientation reverse. A joining segment has displacement \(d_k\beta\); multiplying arc, join and arc gives exactly the three-term sum in equation (10).

For a change of endpoint frame \(u'_j=\alpha_j u_j+\beta_j\), \(\alpha_j=d_j/d'_j\), direct affine substitution gives one term \(-d'_j\beta_j\) at each exposed endpoint. This proves (11), including the odd routes with multiplier minus one. The explicit global rule \(\alpha_b\kappa=\alpha_a\), with contribution \(\alpha_b\beta\), is consistent with it. The final open-chart qualification is necessary and correct: this calculation transports boundary charts with virtual completions until the original closed mask theorem supplies every actual white transition.

## 2. Rational identities

I constructed the Möbius frames from equation (6) and the normalized three-point map of each world quadrilateral, independently of the printed translation tables. Exact rational simplification checks all four unit meridians, all four odd routes, all four turn rebasing maps, all four closing maps, all six product maps, and the product/turn/closure potential identities. This is 69 scalar checks, using the independent symbols \(E,R,a,b,c\).

The private executable is
`/private/tmp/md-ledger-peer-geometric-cocycle-check.py`,
SHA256 `a582447e4e032b6acce5c9c56e57c2702e4c87601936d5c66c5760444ffbf9b2`.
Its result is
`/private/tmp/md-ledger-peer-geometric-cocycle-check-results.json`,
SHA256 `0c3f41dc22046c34756398df61c8250b42deca10b2eb932f74904c30ed506ae5`.
These checks establish matrix identities only; the actual path and homology arguments were read separately.

The product potential \(P=(E+R)/(E-1)\) cancels every unturned product correction. A turn contributes \(-2i\cot(\pi b)\), and the closed root cancels the two remaining boundary potentials. A pure turned leaf has \(I=2i\cot(\pi x)\), while an odd leaf has \(I=2i\cot(\pi x)-\epsilon\). Thus the covariant labels give precisely the physical-turn-edge sum, without an artificial contribution from a binary product resolution.

## 3. Actual words and preferred framing

The original `notes/actual_conway_general_mask_marked_filling.md`, Section 6, explicitly identifies \(A^{-1}W_0\) with physical \(R^{-1}\) and \(W_0^{-1}B\) with physical \(R\). It fixes those signs by the actual threading calculation, independently of the new longitude proof.

The old edge words therefore give the rows of (32) as identities of paths. Abelianizing the positive row gives
\[
 -t_0t_1\mu_K+(t_0-t_1)\mu_{\mathrm{aux}};
\]
the negative row gives
\[
 t_0t_1\mu_K+(t_0-t_1)\mu_{\mathrm{aux}}.
\]
Undoing the actual turn sends parallel positive-braid strands to \(t_0=-t_1\); consequently these main-meridian coefficients are exactly the actual oriented writhe contributions. The pure row has no main-meridian coefficient. Since all outside strips are crossing free, the total path has self-framing \(w_\epsilon\). Its underlying component follows every actual main segment once, so it is a single longitude traversal, rather than an unspecified multiple. Subtracting \(w_\epsilon\mu_K\) therefore gives the preferred augmented main longitude.

For the disjoint original crossing-circle disks, \([\lambda_i]=\ell_i[\mu_K]\). The primitive filling kills \(\mu_i+p_i\lambda_i\), whence the image of the augmented main longitude has homology \(-\sum_i p_i\ell_i^2\mu_K\). Adding \(\sum_i p_i\ell_i^2\) main meridians is therefore the correct preferred-longitude correction, with the positive sign in (40). This uses the actual auxiliary slope convention and leaves the main cusp unfilled.

## 4. Agreement with the independently calculated quantum scalar

The geometric proof gives
\[
 \tau_{\mathrm{main}}
 =2i\sum_e\cot(\pi x_e^{\mathrm{fill}})
       -\sum_i\epsilon_i-w_\epsilon+\sum_i p_i\ell_i^2.
\]
Since \(\ell_i^2=2(1+o_i)\), \(w_\epsilon=\sum_i o_i\epsilon_i\), and \(n_i=\epsilon_i-2p_i\), its integer equals
\[
 -w_{\mathbf{n}}-\sum_i n_i=-2\sum_{\mathrm{parallel}}n_i.
\]
This is exactly the scalar exponent in the separate quantum ledger. Neither proof uses the conclusion of the other. The geometric result itself requires only the actual strict marked geometry and filling branch, not the narrower analytic component-path condition needed for the currently established moving-meridian packet.

No correction is required. The correspondence identifies the first scalar-plus-edge correction in the proved microscopic profile with the actual preferred cusp shape for its covered class. It does not identify a classical factor of a quantum annihilator.
