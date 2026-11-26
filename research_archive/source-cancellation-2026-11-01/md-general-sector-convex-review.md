# General complementary-source convex criteria: exact scope and a protected-singleton barrier

1 November 2026. Private proof/status work only; no release, manuscript or guide file is changed. The subject is the original shared targets and local coefficient envelopes, not a new invariant or a volume counterexample.

## 1. What the sufficient results require

Appendix P proves full long-filling volume equality under weak balance, or its quantified positive-defect extension, on an original matched simple sphere. It does not assert that every marked sphere meets that geometric condition.

Appendix Q assumes an unabridged finite certificate for every locally allowed noncentral C/L/R string of each input. Its protected triangular sum transfers those hypotheses; it does not manufacture them for arbitrary inputs. It retains the original face targets, including the single duplicated-target correction.

The older general_actual_sector_cover_filling_volume.md explicitly fixes an original certified simple-white **plat**. Its final universal question is restricted to that class. The 54-region obstruction is an original matched-sphere **Morse** source with a verified knot-producing parity pattern. Its certificate does not supply a flat-plat realization of that same marked incidence. It therefore refutes universal extension to arbitrary matched simple spheres, without settling the narrower flat-plat question.

Likewise, general_endpoint_conditioned_source_energy.md, §1, fixes a certified flat plat. Its sufficient inequalities remain valid within their hypotheses. An unqualified assertion that their universal extension to all matched spheres is “open” needs correction: that larger extension is false by the argument below.

The 17-region separation certificate obstructs a coarse anchor with unrestricted spectator labels, while forty branches certify the genuine strings of that same source. The 54-region certificate instead obstructs one already fixed genuine string with central spectators. Splitting only C/L/R labels cannot subdivide that singleton further.

## 2. The original score and exact targets

Write \(d=N-1\). Every local incidence vector has total degree \(d\); each ordinary face has shared target \(d\), and the two protected faces have target zero. Limiting normalized loads therefore sum to one at each region and ordinary face. Every repeated occurrence retains its original global face label.

For \(0\le a\le1/2\), set
\[
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},
 \qquad \Lambda(t)=-\int_0^t\log|2\sin u|\,du.
\]
Thus \(f(0)=f(1/2)=0\) and \(f(1/2-a)=f(a)\). A half-degree triangle has load sum \(1/2\), entropy \(C(\alpha)=\sum_i f(\alpha_i)\), and potential
\[
 Q_t(\ell)=\max_{\alpha\ge0,\ \sum\alpha_i=1/2}
           \left(C(\alpha)+\sum_{i\in t}\alpha_i\ell_i\right).
\]
Protected corners are deleted; \(\ell_i=\log L_i\) is only defined at ordinary positive weights.

Let \(h\) denote positive endpoint coefficient entropy and \(g\) the proved upper rate of \(|a_N|^2/p_N\), in shared-energy (15). On central loads both are \(h_C\), the maximum of the two triangle entropies over their permitted outer split. On a left load, let \(h_{\rm env}\) be the perspective envelope and
\[
                    h_{\rm sharp}=\min\{h_{\rm env},(h+g)/2\}.
\]
These are bounds on the same original feasible flow, not the exponent of its signed global sum.

## 3. Exact score identity on every protected-singleton sector

Suppose one chosen region is left, with quartet \((x,b,z,y)\), where \(b,y\) are protected and \(x,z\) ordinary. Every other region is central. The retained triangle at the chosen side is the singleton \(x\).

Let \(\mathcal P_{\rm cap}\) be the closed feasible load polytope for this string, with the original face targets. Its cap load is
\[
                 q_{\rm cap}=(u,0,1-u,0),\qquad 0\le u\le1/2.
\]
Here \(q_{\rm cap}\) denotes normalized loads, not logarithmic weights.

**Protected-singleton identity.** On the entire cap interval,
\[
 k^*(q_{\rm cap})=0,\quad h(q_{\rm cap})=-2f(u),\quad
 g(q_{\rm cap})=2f(u),\quad
 h_{\rm env}(q_{\rm cap})=h_{\rm sharp}(q_{\rm cap})=0.
 \tag{1}
\]
Indeed, actual_protected_outer_spectral_energy.md §2(4) with \(\mu=0,\nu=u\) gives \(k^*=f(0)+f(u)-f(u)=0\) and \(h=-2f(u)\), including the closed endpoints and both parities. Its (5), equivalently shared-energy (15), gives \(g=C(u,1/2-u,0)=2f(u)\). The envelope perspective has mass \(2u\) and normalized singleton row \((1/2,0,0)\), of entropy zero. Continuity gives the same value at \(u=0\).

Let \(\mathcal C_{\rm cap}\) be the old envelope capacity for this fixed string. If \(\mathcal P_{\rm cap}\ne\varnothing\), then
\[
 \boxed{\displaystyle
 \max_{\mathcal P_{\rm cap}}\sum_e h_{\rm sharp}(q_e)
 =\frac12\max_{\mathcal P_{\rm cap}}\sum_e(h(q_e)+g(q_e))
 =\mathcal C_{\rm cap}.}
 \tag{2}
\]
For the last equality the exact cap envelope is
\[
 A_{\rm cap}(\ell)=\max\{\ell_z,(\ell_x+\ell_z)/2\}
      =\max_{0\le u\le1/2}\{u\ell_x+(1-u)\ell_z\}.
 \tag{3}
\]
It has zero entropy at every allowed cap load. The existing perspective network contains precisely this interval and two ordinary half-rows at each spectator. Optimizing the two-row outer split gives \(h_C\) at that spectator. No mixtures of distinct genuine spectator labels have been added.

No capacity minimizer is required. Before imposing face equations, the product \(K\) of row simplices and the cap interval is compact convex; its entropy \(E\) is continuous concave and its face-load map \(B\) is linear. The set
\[
                    \{(Bz,t):z\in K,\ t\le E(z)\}
\]
is a closed convex hypograph. Separate \((\mathbf1,a)\), for any \(a>\max_{Bz=\mathbf1}E(z)\), from this set. The coefficient of its last coordinate is nonnegative, and is strictly positive because \(\mathbf1\) is a feasible load. Division by it supplies logarithmic weights whose dual value is below \(a\); weak duality gives the reverse inequality. If the target is infeasible, separating it from the compact load polytope instead gives capacity \(-\infty\).

Thus the energy refinement supplies **no improvement anywhere on this whole class of protected-singleton strings**. Equation (2) is not asserted for general one-sided strings.

## 4. The public R54 flow defeats both universal score inequalities

Use the certified 54-region source with protected faces \(29,50\), left at \(32=(0,50,16,29)\), and central elsewhere. Set
\[
          \lambda=\frac{548219162717}{10^{12}},\qquad u=\lambda/2.
\]
Keep its 106 central triangle rows exactly. At each spectator aggregate the two half-rows into its four-incidence load. Each middle then has load at most \(1/2\), so the spectator is central. The exact original face equations, singleton-obstruction (12), make these aggregates and \((u,0,1-u,0)\) one feasible flow in \(\mathcal P_{\rm cap}\).

At each spectator \(h_C\), being the maximum over outer splits, is at least the entropy of those two certified rows. By (1) the cap contributes zero to both half-scores. Therefore this same flow satisfies
\[
 \sum_eh_{\rm sharp}(q_e)\ge E_{\rm dual}>\Phi+\frac15,\qquad
 \sum_e(h(q_e)+g(q_e))\ge2E_{\rm dual}>2\Phi+\frac25.
 \tag{4}
\]
The inequalities use the public outward-rounded rational certificate:
\[
 E_{\rm dual}>67.8938190642,\qquad
 \Phi\le P(L^{\rm up})<67.6882466366,\qquad
 E_{\rm dual}-P(L^{\rm up})>0.2055724276>1/5.
\]
Here \(2\pi\Phi\) is the actual complete augmented volume. Its upper bound comes from the separate positive-radius witness, not from the upper endpoint of a feasible entropy interval.

Consequently the universal extensions of shared-energy (19) and (23) to every matched simple-sphere Morse diagram are false. Their conditional implications are unaffected. This argument needs no signed-source lower bound, no full-positive endpoint theorem on arbitrary Morse sources, and no numerical optimizer.

The chosen actual string cannot be omitted as identically zero: the public obstruction note §3 proves shared support at every sufficiently large even level. The previously frozen private md-excursion-weighted-r54-absolute-array-obstruction.md separately strengthens the obstruction to an actual mixed-spectrum absolute-array sum. It also proves
\[
 \inf_{w_a>0}\left(\sum_aw_a\right)^{1/2}
                 \left(\sum_a|A_a|^2/w_a\right)^{1/2}
                         =\sum_a|A_a|.
\]
This is pointwise even for \(N\)- and spectrum-dependent weights. For nonzero entries choose \(w_a=|A_a|\); send weights of zero entries to zero. If all entries vanish, both sides vanish. This excludes all positive diagonal references on that unchanged array partition once the absolute-sum lower applies, but says nothing about coherent regrouping or nondiagonal phase correlations. The earlier proof is not newly promoted or extended to odd levels here.

## 5. A nearby legal mark kills this singleton, without solving the source problem

The same certificate has the nonmatching edge \(29\!-\!16\), incident to triangles \((16,0,29)\) and \((29,44,16)\). The first belongs to region 32, matched across \(0\!-\!29\); the second belongs to region 35, matched across \(29\!-\!44\). Thus \(29\!-\!16\) is an actual MAIN edge.

Choose this reduced mark without changing any crossing coupon or physical twist. The protected variables become \(L_{29}=L_{16}=0\). Every left monomial of region 32 has \(L_{16}\)-degree greater than \(\lfloor d/2\rfloor\), hence positive. The old obstructing string is now exactly zero for every \(N\ge2\).

The exact MAIN-mark transport theorem applies to the **full** original polynomial source, with transported turns and the original coupon frames. It does not transport this sector, its capacity or the old rational flow. No claim follows that the new mark satisfies weak balance or all sector certificates. The original knot-producing parity pattern is unchanged; choosing another cut on that same knot is permitted. No assertion is made that this new edge is reached by one local physical slide through region 32.

This gives a concrete remaining test: certify or obstruct the surviving genuine strings at the new mark. The existing fixed-mark obstruction does not refute a theorem allowing a successful mark to be selected. Full-invariant mark independence does not transfer a sector estimate without rechecking its changed targets.

## 6. Publication-safe status correction

Suggested replacement for an unqualified statement that the universal combined-score inequality is open:

> The joint and combined energy bounds are sufficient criteria on the stated class of certified flat plats. Their extension as universal inequalities for arbitrary matched simple-sphere Morse diagrams is false. On the certified 54-region source, the protected left load \((u,0,1-u,0)\) has endpoint entropy \(h=-2f(u)\), relative-energy rate \(g=2f(u)\), and envelope \(h_{\rm env}=0\). Its refined local score is therefore zero, while the same feasible central spectator rows have total entropy greater than the complete geometric rate by more than \(1/5\). This defeats the universal score comparison on that fixed source and mark, not the conditional theorem or volume equality. The narrower flat-plat question and the possibility of changing the reduction mark are not settled by this example; a proof for the general source must retain additional coherent cancellation or establish a different comparison.

Exact published inputs:

- actual_protected_outer_spectral_energy.md, §2(4)–(5): the three sharp protected local rates, including closed boundaries and both parities.
- general_endpoint_conditioned_source_energy.md, §1 for flat-plat scope; §5(15),(19) and §6(20)–(23) for the scores.
- actual_fejer_full_kernel_entropy_identity_reduction.md, §1(1): the central outer-split maximum.
- actual_singleton_sector_envelope_obstruction.md, §§2–5, especially (5),(10)–(13),(18): original incidence, one exact feasible flow and certified constants; §3 also proves nonzero support.
- research_fixed_sector_fractional_forest_reduction.md, §1: the existing perspective network. Half-integral vertices do not justify replacing a concave entropy maximum by pure atoms.
- research_arbitrary_main_edge_mark_transport.md, §§4–8: exact full-source transport, expressly not sectorwise transport.

Potential wording locations, not edited: book/chapters/frontier.md around line 722 calls the universal shared inequality “the missing statement” without repeating the flat-plat restriction; results.md around line 917 calls the global comparison unresolved. The source note itself explicitly states the narrower scope at its opening and should retain it.

## 7. Source record

The following hashes record exact versions read, not a fresh audit of every imported theorem. No numerical search, spectral sampling or new filling calculation was used.

Read checkout HEAD: f2076a1bb61e9ee9e8f05d3beaf49ed7dbb73e5a.

| Source | SHA256 |
|---|---|
| manuscript/sections/P-weak-balance.tex | 2fa93c0a481941f1075feef21a1fc05915457abc2c3d1a125b9508ab130130aa |
| manuscript/sections/Q-protected-triangular-sums.tex | 7b9336b24b0088760aa73db35e584fd089c62ee9f699a6a11e7c5d02cdced195 |
| notes/general_actual_sector_cover_filling_volume.md | e84ad4e28eaa65bd3114656cb332c93846aaf5d929612cba9f8a47e651fe7d57 |
| notes/actual_complete_source_cauchy_capacity_gap.md | 2e18048aa34b126700848e2c40cb9c1c596b775c1941cad922e102e60b0ff293 |
| notes/actual_shared_radius_certificate_separation.md | d6e5179aed8badce246171b578f65bbb97a88c00ac5955f627f0327e2932e59b |
| notes/research_fixed_sector_fractional_forest_reduction.md | 1f19fe3924bd113b2669a99a8f3c42550216c0da11156d43f2f2a1a90a708f69 |
| notes/general_endpoint_conditioned_source_energy.md | 7c1baebe8fa2efc2dc3183e08c27d97f65b04ffa2b6e4a183913a39a416959eb |
| notes/actual_protected_outer_spectral_energy.md | 39d14d5bcbe4e3087223ddf77579e25cc217f3229a013d913fedae144efebd4b |
| notes/actual_fejer_full_kernel_entropy_identity_reduction.md | 7cdfbf7f4ca19cdaf476431693e00de3707c574681f081fe93fe46e8197a1f74 |
| notes/actual_singleton_sector_envelope_obstruction.md | 77828c96533bc72db0d7f524b7ecb51f363777ce1c60b2a57b107f6b0f1a7493 |
| notes/research_arbitrary_main_edge_mark_transport.md | 7a7c9efdca1e9f7907dc5baf5dfe8ba12e2345ee5f2df2ed94240e95ee69112a |
| experiments/actual_singleton_sector_obstruction_certificate.json | 324173b25db8fbe36a89ac65617663c44d1385772c1e29e394bbb6b478a11022 |
| experiments/actual_singleton_sector_obstruction_results.json | 696b22ca2cfcce38dea9e0e73ea833afb36116feaf61dce54c91532d696baebf |
| book/chapters/frontier.md | 9bf5afb921b67e7d52d2d02b6b6e03488fe3e80164512ad407ba72d9824e3003 |
| book/chapters/results.md | 991bddc4a4d96df9d6f261dae7104a55f70f1a383ebf49d6edc3cbec5a021a1c |

Previously frozen absolute-array proof SHA256: 5a466b68ab92541698bbcc37a50de93b701777a10531887397a48542cb847129.

The exact public incidence gives face indices 62 and 75 for edge 16–29; that pair is absent from matching_faces. The old edge 29–50 and alternatives 0–50 and 0–16 are also nonmatching. This is a finite incidence check, not a capacity or asymptotic computation.
