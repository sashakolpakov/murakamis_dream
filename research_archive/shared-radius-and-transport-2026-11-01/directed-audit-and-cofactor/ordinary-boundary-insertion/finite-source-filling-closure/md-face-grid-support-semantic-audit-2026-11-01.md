# Bounded semantic audit of FaceGridSupport

Read-only audit of all six declarations in `formal/VolumeLogic/FaceGridSupport.lean`, compared with Appendix O, proposition `mcg:face-grid-selection`, and `research_matched_sphere_morse_source.md`, section 5. No compilation or public edit was performed in this audit; the parent has compiled the module.

**Conclusion:** no mathematical or application-scope correction is needed.

The actual application takes N at least 2, d=N−1, `a=m_u` for the exterior protected face, `b=m_v` for the other protected face, and `xs` for the R ordinary nonnegative exponents. The physical numerator has total degree R d. After division by the ordinary target monomial, each ordinary grid selects x congruent to d modulo N. The free protected-v grid selects b congruent to 0; there is no grid at the exterior-u face.

* `residue_target_lower` uses the actual nonnegative remainder to prove d≤x. Its slightly broader natural-number statement does not add a physical claim at N=0 or N=1.
* `list_sum_lower` sums these minima with multiplicity; it needs no distinctness of the exponent list.
* `face_budget_saturation` proves directly that a+b+sum(xs)≤length(xs)d, together with the ordinary minima, forces a=b=0 and every ordinary exponent d.
* `face_grid_unique_exponents` combines those constructed arithmetic steps. In particular, no exterior congruence is assumed, and the protected-v congruence is unnecessary in this forward implication because the degree budget already forces it.
* `face_grid_below_target` proves that a strictly lower total degree cannot survive all ordinary grids.
* `face_grid_selection_iff` restores the actual protected-v residue in the selector and proves both directions. The hypothesis N>0 is sufficient for the converse residue of d; the source uses N≥2.

For the translated physical grids L_f=xi_f omega^p_f, the surviving monomial has multiplier product(xi_f^(m_f−d)) xi_v^m_v=1. Thus neither the even coset nor arbitrary nonzero translations introduce a surviving extra character. This multiplier conclusion and finite character orthogonality are written applications, not additional Lean declarations.

The formalized object is the exponent support argument, not a polynomial grid evaluator. The original ribbon normalization, exact homogeneous source, equality between R coupons and R ordinary faces, primitive face-potential lattice, and finite root-of-unity character orthogonality remain explicit written inputs. The header, theorem comments, and Appendix O paragraph state this limit accurately. No topology, spectral normals, or asymptotic source bound is inferred from these six lemmas.

## Snapshot

* `formal/VolumeLogic/FaceGridSupport.lean`: `4baeeee58f794f7a610f880a5f465af13bb00beb6598f1041ac58fb9a74d8705`.
* `manuscript/sections/O-morse-geometric-contribution.tex`: `3d364e1aea83bb799665fe13f09be528b99626510b0d3025ddb87bf1d8f6f01f`.
* `notes/research_matched_sphere_morse_source.md`: `8fdfde4a0d83220f3709048f00cd9373cfbc9d14b05943e9f16f58ab50777f4f`.

The Appendix O snapshot here is later than the separately frozen analytic audit: the parent has inserted the face-grid proposition and is making the recorded simple-node wording correction. That does not retroactively change the earlier audit hash.
