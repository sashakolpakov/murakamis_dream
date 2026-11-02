import TriangleLoads
import Mathlib.Analysis.Convex.Deriv
import Mathlib.Analysis.SpecialFunctions.Integrals.LogTrigonometric
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.Calculus.Deriv.Shift

/-!
The actual Lobachevsky triangle entropy and its supported variational envelope.
The potential is defined by the same integral and constrained maximum as in
the written triangle-potential arguments, not by integrating an assumed
gradient field. Geometric incidence and packing identifications are separate.
-/

namespace VolumeLogic.TrianglePotential
open scoped BigOperators
open Set MeasureTheory Filter Interval
open TriangleLoads

noncomputable def lobachevsky (x : ℝ) : ℝ :=
  -(∫ u in (0 : ℝ)..x, Real.log |2 * Real.sin u|)

noncomputable def entropy (t : ℝ) : ℝ :=
  (lobachevsky (Real.pi * t) + lobachevsky (Real.pi / 2 - Real.pi * t)) /
    Real.pi

noncomputable def entropySlope (t : ℝ) : ℝ :=
  Real.log (Real.cos (Real.pi * t)) - Real.log (Real.sin (Real.pi * t))

theorem lobachevsky_eq_log_sin (x : ℝ) :
    lobachevsky x = -(∫ u in (0 : ℝ)..x, Real.log (Real.sin u)) - x * Real.log 2 := by
  have heq : (∫ u in (0 : ℝ)..x, Real.log |2 * Real.sin u|) =
      ∫ u in (0 : ℝ)..x, (Real.log 2 + Real.log (Real.sin u)) := by
    apply intervalIntegral.integral_congr_codiscreteWithin
    apply Filter.codiscreteWithin_mono (show Ι (0 : ℝ) x ⊆ univ by simp)
    have hs : Real.sin ⁻¹' ({0} : Set ℝ)ᶜ ∈ Filter.codiscrete ℝ := by
      apply Real.analyticOnNhd_sin.preimage_zero_mem_codiscrete (x := Real.pi / 2)
      simp
    filter_upwards [hs] with u hu
    simp only [mem_preimage, mem_compl_iff, mem_singleton_iff] at hu
    rw [Real.log_abs, Real.log_mul (by norm_num) hu]
  have hi : IntervalIntegrable (fun u : ℝ => Real.log (Real.sin u)) volume 0 x :=
    intervalIntegrable_log_sin
  rw [lobachevsky, heq, intervalIntegral.integral_add intervalIntegrable_const hi,
    intervalIntegral.integral_const]
  simp only [sub_zero, smul_eq_mul]
  ring

theorem lobachevsky_continuous : Continuous lobachevsky := by
  have h : Continuous (fun x : ℝ => ∫ u in (0 : ℝ)..x, Real.log (Real.sin u)) :=
    intervalIntegral.continuous_primitive (fun _ _ => intervalIntegrable_log_sin) 0
  rw [show lobachevsky = (fun x : ℝ => -(∫ u in (0 : ℝ)..x, Real.log (Real.sin u)) - x * Real.log 2) from funext lobachevsky_eq_log_sin]
  exact h.neg.sub (continuous_id.mul_const (Real.log 2))

theorem lobachevsky_hasDerivAt {x : ℝ} (hx : Real.sin x ≠ 0) :
    HasDerivAt lobachevsky (-Real.log (2 * Real.sin x)) x := by
  have hc : ContinuousAt (fun u : ℝ => Real.log (Real.sin u)) x :=
    (Real.continuousAt_log hx).comp Real.continuous_sin.continuousAt
  have hi := intervalIntegral.integral_hasDerivAt_right
    (f := fun u : ℝ => Real.log (Real.sin u))
    (a := 0) intervalIntegrable_log_sin
    ((Real.measurable_log.comp Real.continuous_sin.measurable).stronglyMeasurable.stronglyMeasurableAtFilter) hc
  convert! hi.neg.sub ((hasDerivAt_id x).mul_const (Real.log 2)) using 1
  · funext u
    exact lobachevsky_eq_log_sin u
  · rw [Real.log_mul (by norm_num) hx]
    ring

theorem lobachevsky_zero : lobachevsky 0 = 0 := by simp [lobachevsky]

theorem lobachevsky_half_pi : lobachevsky (Real.pi / 2) = 0 := by
  rw [lobachevsky_eq_log_sin, integral_log_sin_zero_pi_div_two]
  ring

theorem entropy_continuous : Continuous entropy := by
  exact ((lobachevsky_continuous.comp (continuous_const.mul continuous_id)).add
    (lobachevsky_continuous.comp
      (continuous_const.sub (continuous_const.mul continuous_id)))).div_const Real.pi

theorem entropy_zero : entropy 0 = 0 := by
  simp [entropy, lobachevsky_zero, lobachevsky_half_pi]

theorem entropy_half : entropy (1 / 2) = 0 := by
  norm_num [entropy, lobachevsky_zero, lobachevsky_half_pi, mul_one_div]

theorem entropy_hasDerivAt {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) (1 / 2)) :
    HasDerivAt entropy (entropySlope t) t := by
  have hp : 0 < Real.pi * t := mul_pos Real.pi_pos ht.1
  have hph : Real.pi * t < Real.pi / 2 := by nlinarith [Real.pi_pos, ht.2]
  have hs := Real.sin_pos_of_pos_of_lt_pi hp (by linarith [Real.pi_pos])
  have hc := Real.cos_pos_of_mem_Ioo (show Real.pi * t ∈ Ioo (-(Real.pi / 2)) (Real.pi / 2) by
    constructor <;> linarith [Real.pi_pos])
  have hsp : Real.sin (Real.pi / 2 - Real.pi * t) ≠ 0 := by
    rw [Real.sin_pi_div_two_sub]
    exact ne_of_gt hc
  have h1 := (lobachevsky_hasDerivAt (ne_of_gt hs)).comp t
    ((hasDerivAt_id t).const_mul Real.pi)
  have h2 := (lobachevsky_hasDerivAt hsp).comp t
    (((hasDerivAt_id t).const_mul Real.pi).const_sub (Real.pi / 2))
  convert! (h1.add h2).div_const Real.pi using 1
  · rw [Real.sin_pi_div_two_sub, Real.log_mul (by norm_num) (ne_of_gt hc),
      Real.log_mul (by norm_num) (ne_of_gt hs)]
    unfold entropySlope
    field_simp
    ring

theorem entropySlope_hasDerivAt {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) (1 / 2)) :
    HasDerivAt entropySlope
      ((-Real.sin (Real.pi * t) * Real.pi) / Real.cos (Real.pi * t) -
        (Real.cos (Real.pi * t) * Real.pi) / Real.sin (Real.pi * t)) t := by
  have hp : 0 < Real.pi * t := mul_pos Real.pi_pos ht.1
  have hph : Real.pi * t < Real.pi / 2 := by nlinarith [Real.pi_pos, ht.2]
  have hs := Real.sin_pos_of_pos_of_lt_pi hp (by linarith [Real.pi_pos])
  have hc := Real.cos_pos_of_mem_Ioo (show Real.pi * t ∈ Ioo (-(Real.pi / 2)) (Real.pi / 2) by
    constructor <;> linarith [Real.pi_pos])
  have hl := (hasDerivAt_id t).const_mul Real.pi
  convert! (hl.cos.log (ne_of_gt hc)).sub (hl.sin.log (ne_of_gt hs)) using 1
  simp

theorem entropy_concave : ConcaveOn ℝ (Icc (0 : ℝ) (1 / 2)) entropy := by
  apply concaveOn_of_hasDerivWithinAt2_nonpos (convex_Icc 0 (1 / 2))
    entropy_continuous.continuousOn
    (f' := entropySlope)
    (f'' := fun t => (-Real.sin (Real.pi * t) * Real.pi) / Real.cos (Real.pi * t) -
      (Real.cos (Real.pi * t) * Real.pi) / Real.sin (Real.pi * t))
  · intro t ht
    rw [interior_Icc] at ht
    exact (entropy_hasDerivAt ht).hasDerivWithinAt
  · intro t ht
    rw [interior_Icc] at ht
    exact (entropySlope_hasDerivAt ht).hasDerivWithinAt
  · intro t ht
    rw [interior_Icc] at ht
    have hp : 0 < Real.pi * t := mul_pos Real.pi_pos ht.1
    have hph : Real.pi * t < Real.pi / 2 := by nlinarith [Real.pi_pos, ht.2]
    have hs := Real.sin_pos_of_pos_of_lt_pi hp (by linarith [Real.pi_pos])
    have hc := Real.cos_pos_of_mem_Ioo (show Real.pi * t ∈ Ioo (-(Real.pi / 2)) (Real.pi / 2) by
      constructor <;> linarith [Real.pi_pos])
    have h1 : 0 ≤ Real.sin (Real.pi * t) * Real.pi / Real.cos (Real.pi * t) := by positivity
    have h2 : 0 ≤ Real.cos (Real.pi * t) * Real.pi / Real.sin (Real.pi * t) := by positivity
    rw [neg_mul, neg_div]
    linarith

/-- The supporting tangent is valid also when the competing load is an
endpoint. No differentiability of the entropy at the endpoints is assumed. -/
theorem entropy_tangent {a b : ℝ} (ha : a ∈ Ioo (0 : ℝ) (1 / 2))
    (hb : b ∈ Icc (0 : ℝ) (1 / 2)) :
    entropy b ≤ entropy a + entropySlope a * (b - a) := by
  rcases lt_trichotomy a b with hab | rfl | hba
  · have h := entropy_concave.slope_le_of_hasDerivAt
      ⟨ha.1.le, ha.2.le⟩ hb hab (entropy_hasDerivAt ha)
    rw [slope_def_field] at h
    have hh := (div_le_iff₀ (sub_pos.mpr hab)).mp h
    linarith
  · simp
  · have h := entropy_concave.le_slope_of_hasDerivAt hb
      ⟨ha.1.le, ha.2.le⟩ hba (entropy_hasDerivAt ha)
    rw [slope_def_field] at h
    have hh := (le_div_iff₀ (sub_pos.mpr hba)).mp h
    nlinarith

/-- The sum of the actual three arctangents is a half turn. This proof
includes a zero corner directly, not by a limiting argument. -/
theorem arctan_sum (x y z D : ℝ) (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z)
    (hD : 0 < D) (hDs : D ^ 2 = x * y + y * z + z * x) :
    Real.arctan (x / D) + Real.arctan (y / D) + Real.arctan (z / D) =
      Real.pi / 2 := by
  have hd : D ≠ 0 := ne_of_gt hD
  by_cases hz0 : z = 0
  · subst z
    have hxy : 0 < x * y := by nlinarith [sq_pos_of_pos hD]
    have hxp : 0 < x := by nlinarith
    have hyp : 0 < y := by nlinarith
    have hi : y / D = (x / D)⁻¹ := by
      field_simp
      nlinarith [hDs]
    rw [hi, Real.arctan_inv_of_pos (div_pos hxp hD)]
    simp
  · have hzp : 0 < z := lt_of_le_of_ne hz (Ne.symm hz0)
    have hp : 0 < x + y := by nlinarith [sq_pos_of_pos hD]
    have hprod : (x / D) * (y / D) < 1 := by
      rw [div_mul_div_comm, div_lt_one (mul_pos hD hD)]
      nlinarith [mul_pos hzp hp]
    have hid : (x / D + y / D) / (1 - x / D * (y / D)) = D / z := by
      have hden : D ^ 2 - x * y ≠ 0 := by nlinarith [mul_pos hzp hp]
      field_simp
      nlinarith [hDs]
    rw [Real.arctan_add hprod, hid]
    have hi : D / z = (z / D)⁻¹ := by simp [div_eq_mul_inv]
    rw [hi, Real.arctan_inv_of_pos (div_pos hzp hD)]
    ring

theorem loads_sum (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) :
    (∑ i, load a q i) = 1 / 2 := by
  have hw := weights_nonneg a q ha
  have h := arctan_sum (weights a q 0) (weights a q 1) (weights a q 2)
    (triangleD (weights a q)) (hw 0) (hw 1) (hw 2)
    (triangleD_pos _ hs) (triangleD_sq _ hs)
  simp only [load, Fin.sum_univ_three]
  rw [← add_div, ← add_div, h]
  field_simp

theorem load_mem_Ioo (a q : Fin 3 → ℝ) (i : Fin 3) (hi : 0 < a i)
    (hs : 0 < radicand (weights a q)) : load a q i ∈ Ioo (0 : ℝ) (1 / 2) := by
  have hp := (weights_pos_iff a q i).mpr hi
  have hd := triangleD_pos (weights a q) hs
  constructor
  · exact div_pos (Real.arctan_pos.mpr (div_pos hp hd)) Real.pi_pos
  · unfold load
    apply (div_lt_iff₀ Real.pi_pos).mpr
    convert! Real.arctan_lt_pi_div_two (weights a q i / triangleD (weights a q)) using 1
    ring

theorem load_nonneg (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) (i : Fin 3) : 0 ≤ load a q i := by
  rcases eq_or_lt_of_le (ha i) with hz | hp
  · simp [load_zero_corner a q i hz.symm]
  · exact (load_mem_Ioo a q i hp hs).1.le

noncomputable def logWeight (a q : Fin 3 → ℝ) (i : Fin 3) : ℝ :=
  if a i = 0 then 0 else Real.log (a i) + q i

/-- The zero-weight coordinates are explicitly excluded from the load simplex. -/
def Feasible (a α : Fin 3 → ℝ) : Prop :=
  (∀ i, 0 ≤ α i) ∧ (∑ i, α i) = 1 / 2 ∧ (∀ i, a i = 0 → α i = 0)

noncomputable def objective (a q α : Fin 3 → ℝ) : ℝ :=
  ∑ i, (entropy (α i) + α i * logWeight a q i)

/-- The actual supported finite variational envelope. Its theorems require
at least one positive corner, so the empty supported simplex is not used. -/
noncomputable def potential (a q : Fin 3 → ℝ) : ℝ :=
  sSup {v : ℝ | ∃ α, Feasible a α ∧ objective a q α = v}

theorem logWeight_eq_log (a q : Fin 3 → ℝ) (i : Fin 3) (hi : 0 < a i) :
    logWeight a q i = Real.log (weights a q i) := by
  simp [logWeight, ne_of_gt hi, weights, Real.log_mul (ne_of_gt hi) (Real.exp_ne_zero _)]

theorem loads_feasible (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) : Feasible a (load a q) := by
  exact ⟨load_nonneg a q ha hs, loads_sum a q ha hs, fun i hi => load_zero_corner a q i hi⟩

theorem feasible_mem_Icc (a α : Fin 3 → ℝ) (hf : Feasible a α) (i : Fin 3) :
    α i ∈ Icc (0 : ℝ) (1 / 2) := by
  refine ⟨hf.1 i, ?_⟩
  calc α i ≤ ∑ j, α j := Finset.single_le_sum (fun j _ => hf.1 j) (Finset.mem_univ i)
       _ = 1 / 2 := hf.2.1

theorem entropySlope_at_load (a q : Fin 3 → ℝ) (i : Fin 3) (hi : 0 < a i)
    (hs : 0 < radicand (weights a q)) :
    entropySlope (load a q i) + logWeight a q i = Real.log (triangleD (weights a q)) := by
  let w := weights a q i
  let D := triangleD (weights a q)
  have hw : 0 < w := (weights_pos_iff a q i).mpr hi
  have hd : 0 < D := triangleD_pos _ hs
  have hx : 0 < w / D := div_pos hw hd
  have hangle : Real.pi * load a q i = Real.arctan (w / D) := by
    dsimp [load, w, D]
    field_simp
  have hr : Real.cos (Real.arctan (w / D)) / Real.sin (Real.arctan (w / D)) = D / w := by
    rw [Real.cos_arctan, Real.sin_arctan]
    have hsq : Real.sqrt (1 + (w / D) ^ 2) ≠ 0 := by positivity
    field_simp
  unfold entropySlope
  rw [hangle, ← Real.log_div (ne_of_gt (Real.cos_arctan_pos _))
    (ne_of_gt (Real.sin_arctan_pos.mpr hx)), hr,
    Real.log_div (ne_of_gt hd) (ne_of_gt hw), logWeight_eq_log a q i hi]
  simp only [w, D, sub_add_cancel]

/-- Concavity plus the explicitly proved stationarity equations bounds every
feasible load, including those on the boundary of the simplex. -/
theorem objective_le_loads (a q α : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) (hf : Feasible a α) :
    objective a q α ≤ objective a q (load a q) := by
  have each : ∀ i, entropy (α i) + α i * logWeight a q i ≤
      entropy (load a q i) + load a q i * logWeight a q i +
        Real.log (triangleD (weights a q)) * (α i - load a q i) := by
    intro i
    by_cases hi : a i = 0
    · rw [hf.2.2 i hi, load_zero_corner a q i hi]
      simp
    · have hp : 0 < a i := lt_of_le_of_ne (ha i) (Ne.symm hi)
      have ht := entropy_tangent (load_mem_Ioo a q i hp hs) (feasible_mem_Icc a α hf i)
      have he := entropySlope_at_load a q i hp hs
      rw [← he]
      nlinarith
  have hsum := Finset.sum_le_sum (s := Finset.univ) (fun i _ => each i)
  simpa only [objective, Finset.sum_add_distrib, ← Finset.mul_sum,
    Finset.sum_sub_distrib, hf.2.1, loads_sum a q ha hs, sub_self, mul_zero, add_zero] using hsum

/-- The supremum is attained by the stated arctangent loads. This equality
is derived from the constrained maximum, not a definition of the potential. -/
theorem potential_eq_loads (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) :
    potential a q = objective a q (load a q) := by
  let S := {v : ℝ | ∃ α, Feasible a α ∧ objective a q α = v}
  have hm : objective a q (load a q) ∈ S := ⟨load a q, loads_feasible a q ha hs, rfl⟩
  have hb : ∀ v ∈ S, v ≤ objective a q (load a q) := by
    rintro v ⟨α, hf, rfl⟩
    exact objective_le_loads a q α ha hs hf
  exact le_antisymm (csSup_le ⟨_, hm⟩ hb) (le_csSup ⟨_, hb⟩ hm)

theorem sum_jacobianAction (w h : Fin 3 → ℝ) : (∑ i, jacobianAction w h i) = 0 := by
  have ht := jacobian_pairing w (fun _ => 1) h
  simpa [WeightedGraph.form] using ht

theorem jacobianAction_zero_corner (a q h : Fin 3 → ℝ) (i : Fin 3) (hi : a i = 0) :
    jacobianAction (weights a q) h i = 0 := by
  simp [jacobianAction, conductance, weights, hi]

theorem exists_positive_pair (w : Fin 3 → ℝ) (hw : ∀ i, 0 ≤ w i)
    (hs : 0 < radicand w) : ∃ i j : Fin 3, i ≠ j ∧ 0 < w i ∧ 0 < w j := by
  by_cases h0 : w 0 = 0
  · by_cases h1 : w 1 = 0
    · simp [radicand, h0, h1] at hs
    · by_cases h2 : w 2 = 0
      · simp [radicand, h0, h2] at hs
      · exact ⟨1, 2, by decide, lt_of_le_of_ne (hw 1) (Ne.symm h1),
          lt_of_le_of_ne (hw 2) (Ne.symm h2)⟩
  · by_cases h1 : w 1 = 0
    · by_cases h2 : w 2 = 0
      · simp [radicand, h1, h2] at hs
      · exact ⟨0, 2, by decide, lt_of_le_of_ne (hw 0) (Ne.symm h0),
          lt_of_le_of_ne (hw 2) (Ne.symm h2)⟩
    · exact ⟨0, 1, by decide, lt_of_le_of_ne (hw 0) (Ne.symm h0),
        lt_of_le_of_ne (hw 1) (Ne.symm h1)⟩

theorem radicand_pos_all_coordinates (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) (q' : Fin 3 → ℝ) :
    0 < radicand (weights a q') := by
  obtain ⟨i, j, hij, hi, hj⟩ := exists_positive_pair (weights a q) (weights_nonneg a q ha) hs
  exact radicand_pos_of_positive_pair _ (weights_nonneg a q' ha) i j hij
    ((weights_pos_iff a q' i).mpr ((weights_pos_iff a q i).mp hi))
    ((weights_pos_iff a q' j).mpr ((weights_pos_iff a q j).mp hj))

/-- Differentiation of the maximizing value cancels the load derivatives
by their common Lagrange multiplier and exact mass conservation. -/
theorem objective_loads_hasDerivAt (a q h : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) :
    HasDerivAt
      (fun t : ℝ => objective a (fun j => q j + t * h j)
        (load a (fun j => q j + t * h j)))
      (∑ i, h i * load a q i) 0 := by
  have each : ∀ i, HasDerivAt
      (fun t : ℝ => entropy (load a (fun j => q j + t * h j) i) +
        load a (fun j => q j + t * h j) i * logWeight a (fun j => q j + t * h j) i)
      (Real.log (triangleD (weights a q)) * jacobianAction (weights a q) h i +
        h i * load a q i) 0 := by
    intro i
    by_cases hi : a i = 0
    · simpa [load, weights, hi, entropy_zero,
        jacobianAction_zero_corner a q h i hi] using hasDerivAt_const (0 : ℝ) (0 : ℝ)
    · have hp : 0 < a i := lt_of_le_of_ne (ha i) (Ne.symm hi)
      have hl := load_hasDerivAt a q h ha hs i
      have he0 : HasDerivAt entropy (entropySlope (load a q i))
          (load a (fun j => q j + 0 * h j) i) := by
        simpa only [zero_mul, add_zero] using entropy_hasDerivAt (load_mem_Ioo a q i hp hs)
      have he := he0.comp 0 hl
      have hw : HasDerivAt (fun t : ℝ => logWeight a (fun j => q j + t * h j) i) (h i) 0 := by
        simpa [logWeight, hi] using
          (((hasDerivAt_id (0 : ℝ)).mul_const (h i)).const_add (q i)).const_add (Real.log (a i))
      have heq := entropySlope_at_load a q i hp hs
      convert! he.add (hl.mul hw) using 1
      simp only [zero_mul, add_zero]
      rw [← heq]
      ring
  have hsum := HasDerivAt.fun_sum (u := Finset.univ) (fun i _ => each i)
  simpa only [objective, Finset.sum_add_distrib, ← Finset.mul_sum,
    sum_jacobianAction, mul_zero, zero_add] using hsum

/-- The first derivative of the actual supported supremum is the explicit
arctangent load vector. It is not an assumed envelope differentiation law. -/
theorem potential_hasDerivAt (a q h : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) :
    HasDerivAt (fun t : ℝ => potential a (fun j => q j + t * h j))
      (∑ i, h i * load a q i) 0 := by
  have heq : (fun t : ℝ => potential a (fun j => q j + t * h j)) =
      (fun t : ℝ => objective a (fun j => q j + t * h j)
        (load a (fun j => q j + t * h j))) := by
    funext t
    exact potential_eq_loads a _ ha (radicand_pos_all_coordinates a q ha hs _)
  rw [heq]
  exact objective_loads_hasDerivAt a q h ha hs

/-- The same derivative at every point of a logarithmic affine path. -/
theorem potential_path_hasDerivAt (a q h : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) (t : ℝ) :
    HasDerivAt (fun u : ℝ => potential a (fun j => q j + u * h j))
      (∑ i, h i * load a (fun j => q j + t * h j) i) t := by
  have hd := potential_hasDerivAt a (fun j => q j + t * h j) h ha
    (radicand_pos_all_coordinates a q ha hs _)
  have hd' : HasDerivAt (fun u : ℝ => potential a
      (fun j => q j + t * h j + u * h j))
      (∑ i, h i * load a (fun j => q j + t * h j) i) (t - t) := by
    simpa only [sub_self] using hd
  convert! hd'.comp_sub_const t t using 1
  funext u
  congr 1
  funext j
  ring

/-- Differentiating the actual first derivative yields the previously
constructed graph energy, including a zero corner. -/
theorem potential_path_second_hasDerivAt (a q h : Fin 3 → ℝ)
    (ha : ∀ i, 0 ≤ a i) (hs : 0 < radicand (weights a q)) :
    HasDerivAt
      (fun t : ℝ => deriv (fun u : ℝ => potential a (fun j => q j + u * h j)) t)
      (WeightedGraph.energy edgeSrc edgeDst
        (fun e => conductance (weights a q) (edgeSrc e) (edgeDst e)) h) 0 := by
  have heq : (fun t : ℝ => deriv (fun u : ℝ => potential a (fun j => q j + u * h j)) t) =
      (fun t : ℝ => ∑ i, h i * load a (fun j => q j + t * h j) i) := by
    funext t
    exact (potential_path_hasDerivAt a q h ha hs t).deriv
  rw [heq]
  exact load_pairing_hasDerivAt a q h ha hs

theorem singleton_feasible (a q : Fin 3 → ℝ) (active : Fin 3) (hp : 0 < a active) :
    Feasible a (singletonLoad active q) := by
  refine ⟨?_, ?_, ?_⟩
  · intro i
    simp only [singletonLoad]
    split_ifs <;> norm_num
  · simp [singletonLoad]
  · intro i hi
    have hn : i ≠ active := by rintro rfl; linarith
    simp [singletonLoad, hn]

theorem feasible_singleton_unique (a q α : Fin 3 → ℝ) (active : Fin 3)
    (hz : ∀ i, i ≠ active → a i = 0) (hf : Feasible a α) :
    α = singletonLoad active q := by
  have hout : ∀ i, i ≠ active → α i = 0 := fun i hi => hf.2.2 i (hz i hi)
  have hsum : (∑ i, α i) = α active := by
    apply Finset.sum_eq_single active
    · intro i _ hi
      exact hout i hi
    · simp
  have hi : α active = 1 / 2 := by rw [← hsum]; exact hf.2.1
  funext i
  by_cases he : i = active
  · subst i
    simpa [singletonLoad] using hi
  · simp [singletonLoad, he, hout i he]

theorem objective_singleton (a q : Fin 3 → ℝ) (active : Fin 3) (hp : 0 < a active) :
    objective a q (singletonLoad active q) = (Real.log (a active) + q active) / 2 := by
  have ht : ∀ i, entropy (singletonLoad active q i) +
      singletonLoad active q i * logWeight a q i =
      if i = active then logWeight a q active / 2 else 0 := by
    intro i
    by_cases hi : i = active
    · subst i
      simp only [singletonLoad, ite_true]
      rw [entropy_half]
      ring
    · simp [singletonLoad, hi, entropy_zero]
  unfold objective
  simp_rw [ht]
  simp [logWeight, ne_of_gt hp]

/-- The two-zero boundary convention follows from the very same supported
supremum. It is not obtained by evaluating arctan at a zero denominator. -/
theorem potential_singleton (a q : Fin 3 → ℝ) (active : Fin 3)
    (hp : 0 < a active) (hz : ∀ i, i ≠ active → a i = 0) :
    potential a q = (Real.log (a active) + q active) / 2 := by
  have hm : ∃ α, Feasible a α ∧
      objective a q α = (Real.log (a active) + q active) / 2 :=
    ⟨singletonLoad active q, singleton_feasible a q active hp, objective_singleton a q active hp⟩
  have hb : ∀ v ∈ {v : ℝ | ∃ α, Feasible a α ∧ objective a q α = v},
      v ≤ (Real.log (a active) + q active) / 2 := by
    rintro v ⟨α, hf, rfl⟩
    rw [feasible_singleton_unique a q α active hz hf, objective_singleton a q active hp]
  exact le_antisymm (csSup_le ⟨_, hm⟩ hb) (le_csSup ⟨_, hb⟩ hm)

theorem potential_singleton_hasDerivAt (a q h : Fin 3 → ℝ) (active : Fin 3)
    (hp : 0 < a active) (hz : ∀ i, i ≠ active → a i = 0) (t : ℝ) :
    HasDerivAt (fun u : ℝ => potential a (fun j => q j + u * h j)) (h active / 2) t := by
  have heq : (fun u : ℝ => potential a (fun j => q j + u * h j)) =
      (fun u : ℝ => (Real.log (a active) + (q active + u * h active)) / 2) := by
    funext u
    exact potential_singleton a _ active hp hz
  rw [heq]
  convert! ((((hasDerivAt_id t).mul_const (h active)).const_add (q active)).const_add
      (Real.log (a active))).div_const 2 using 1
  simp only [one_mul]

theorem potential_singleton_second_hasDerivAt (a q h : Fin 3 → ℝ) (active : Fin 3)
    (hp : 0 < a active) (hz : ∀ i, i ≠ active → a i = 0) (t : ℝ) :
    HasDerivAt (fun u : ℝ => deriv
      (fun v : ℝ => potential a (fun j => q j + v * h j)) u) 0 t := by
  have heq : (fun u : ℝ => deriv
      (fun v : ℝ => potential a (fun j => q j + v * h j)) u) =
      (fun _ : ℝ => h active / 2) := by
    funext u
    exact (potential_singleton_hasDerivAt a q h active hp hz u).deriv
  rw [heq]
  exact hasDerivAt_const _ _

/-- Finite triangles share the same vertex variables, and the face-demand
linear term is retained. Repeated corner pairs remain parallel graph edges. -/
noncomputable def summedPotential {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q : V → ℝ) : ℝ :=
  (∑ t, potential (a t) (fun i => q (corners t i))) - ∑ v, demand v * q v

theorem summedPotential_path_hasDerivAt {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q h : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, 0 < radicand (weights (a t) (fun i => q (corners t i)))) (u : ℝ) :
    HasDerivAt (fun v : ℝ => summedPotential corners a demand (fun j => q j + v * h j))
      ((∑ t, ∑ i, h (corners t i) * load (a t)
        (fun j => q (corners t j) + u * h (corners t j)) i) - ∑ v, demand v * h v) u := by
  have hp := HasDerivAt.fun_sum (u := Finset.univ)
    (fun t _ => potential_path_hasDerivAt (a t) (fun i => q (corners t i))
      (fun i => h (corners t i)) (ha t) (hs t) u)
  have hd := HasDerivAt.fun_sum (u := Finset.univ)
    (fun j _ => (((hasDerivAt_id u).mul_const (h j)).const_add (q j)).const_mul (demand j))
  convert! hp.sub hd using 1
  simp only [one_mul]

/-- The Hessian along the actual shared path is the actual weighted graph
energy. Incidence, positive support and grounding are not inferred here. -/
theorem summedPotential_path_second_hasDerivAt {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q h : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, 0 < radicand (weights (a t) (fun i => q (corners t i)))) :
    HasDerivAt
      (fun u : ℝ => deriv
        (fun v : ℝ => summedPotential corners a demand (fun j => q j + v * h j)) u)
      (WeightedGraph.energy
        (fun e : T × Fin 3 => corners e.1 (edgeSrc e.2))
        (fun e : T × Fin 3 => corners e.1 (edgeDst e.2))
        (fun e : T × Fin 3 => conductance
          (weights (a e.1) (fun i => q (corners e.1 i))) (edgeSrc e.2) (edgeDst e.2)) h) 0 := by
  have heq : (fun u : ℝ => deriv
      (fun v : ℝ => summedPotential corners a demand (fun j => q j + v * h j)) u) =
      (fun u : ℝ => (∑ t, ∑ i, h (corners t i) * load (a t)
        (fun j => q (corners t j) + u * h (corners t j)) i) - ∑ v, demand v * h v) := by
    funext u
    exact (summedPotential_path_hasDerivAt corners a demand q h ha hs u).deriv
  rw [heq]
  exact (sum_load_pairing_hasDerivAt corners a q h ha hs).sub_const _

/-- Pointwise Hessian along the entire actual affine path. Thus the graph
energy can be used on every point of a grounded segment, not just at its origin. -/
theorem summedPotential_path_second_at {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q h : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, 0 < radicand (weights (a t) (fun i => q (corners t i)))) (u : ℝ) :
    HasDerivAt
      (fun v : ℝ => deriv
        (fun z : ℝ => summedPotential corners a demand (fun j => q j + z * h j)) v)
      (WeightedGraph.energy
        (fun e : T × Fin 3 => corners e.1 (edgeSrc e.2))
        (fun e : T × Fin 3 => corners e.1 (edgeDst e.2))
        (fun e : T × Fin 3 => conductance
          (weights (a e.1) (fun i => q (corners e.1 i) + u * h (corners e.1 i)))
          (edgeSrc e.2) (edgeDst e.2)) h) u := by
  have heq : (fun v : ℝ => deriv
      (fun z : ℝ => summedPotential corners a demand (fun j => q j + z * h j)) v) =
      (fun v : ℝ => (∑ t, ∑ i, h (corners t i) * load (a t)
        (fun j => q (corners t j) + v * h (corners t j)) i) - ∑ v, demand v * h v) := by
    funext v
    exact (summedPotential_path_hasDerivAt corners a demand q h ha hs v).deriv
  rw [heq]
  have hd := (sum_load_pairing_hasDerivAt corners a (fun j => q j + u * h j) h ha
    (fun t => radicand_pos_all_coordinates (a t) (fun i => q (corners t i))
      (ha t) (hs t) _)).sub_const (∑ v, demand v * h v)
  have hd' := hd
  rw [show (0 : ℝ) = u - u by ring] at hd'
  convert! hd'.comp_sub_const u u using 1
  funext v
  congr 1
  apply Finset.sum_congr rfl
  intro t _
  apply Finset.sum_congr rfl
  intro i _
  congr 2
  funext j
  ring

/-- The same shared potential may contain singleton rows. The partition and
sole active corners are explicit data, not conclusions about a geometric mesh. -/
theorem summedPotential_mixed_hasDerivAt {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q h : V → ℝ)
    (regular : T → Prop) [DecidablePred regular] (active : T → Fin 3)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, regular t → 0 < radicand (weights (a t) (fun i => q (corners t i))))
    (hsingle : ∀ t, ¬ regular t → 0 < a t (active t) ∧
      ∀ i, i ≠ active t → a t i = 0) (u : ℝ) :
    HasDerivAt (fun v : ℝ => summedPotential corners a demand (fun j => q j + v * h j))
      ((∑ t, if regular t then
        ∑ i, h (corners t i) * load (a t)
          (fun j => q (corners t j) + u * h (corners t j)) i
        else h (corners t (active t)) / 2) - ∑ v, demand v * h v) u := by
  have each : ∀ t, HasDerivAt
      (fun v : ℝ => potential (a t) (fun j => q (corners t j) + v * h (corners t j)))
      (if regular t then ∑ i, h (corners t i) * load (a t)
        (fun j => q (corners t j) + u * h (corners t j)) i
        else h (corners t (active t)) / 2) u := by
    intro t
    by_cases ht : regular t
    · simpa only [if_pos ht] using potential_path_hasDerivAt (a t)
        (fun i => q (corners t i)) (fun i => h (corners t i)) (ha t) (hs t ht) u
    · simpa only [if_neg ht] using potential_singleton_hasDerivAt (a t)
        (fun i => q (corners t i)) (fun i => h (corners t i)) (active t)
        (hsingle t ht).1 (hsingle t ht).2 u
  have hp := HasDerivAt.fun_sum (u := Finset.univ) (fun t _ => each t)
  have hd := HasDerivAt.fun_sum (u := Finset.univ)
    (fun j _ => (((hasDerivAt_id u).mul_const (h j)).const_add (q j)).const_mul (demand j))
  convert! hp.sub hd using 1
  simp only [one_mul]

/-- Actual second derivative of the original shared sum, with nonsingletons
and singleton affine rows together. Only the latter's graph weights are zero. -/
theorem summedPotential_mixed_second_at {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q h : V → ℝ)
    (regular : T → Prop) [DecidablePred regular] (active : T → Fin 3)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, regular t → 0 < radicand (weights (a t) (fun i => q (corners t i))))
    (hsingle : ∀ t, ¬ regular t → 0 < a t (active t) ∧
      ∀ i, i ≠ active t → a t i = 0) (u : ℝ) :
    HasDerivAt
      (fun v : ℝ => deriv
        (fun z : ℝ => summedPotential corners a demand (fun j => q j + z * h j)) v)
      (WeightedGraph.energy
        (fun e : T × Fin 3 => corners e.1 (edgeSrc e.2))
        (fun e : T × Fin 3 => corners e.1 (edgeDst e.2))
        (fun e : T × Fin 3 => if regular e.1 then conductance
          (weights (a e.1) (fun i => q (corners e.1 i) + u * h (corners e.1 i)))
          (edgeSrc e.2) (edgeDst e.2) else 0) h) u := by
  have heq : (fun v : ℝ => deriv
      (fun z : ℝ => summedPotential corners a demand (fun j => q j + z * h j)) v) =
      (fun v : ℝ => (∑ t, if regular t then ∑ i, h (corners t i) * load (a t)
        (fun j => q (corners t j) + v * h (corners t j)) i
        else h (corners t (active t)) / 2) - ∑ v, demand v * h v) := by
    funext v
    exact (summedPotential_mixed_hasDerivAt corners a demand q h regular active ha hs hsingle v).deriv
  rw [heq]
  have each : ∀ t, HasDerivAt
      (fun v : ℝ => if regular t then ∑ i, h (corners t i) * load (a t)
        (fun j => q (corners t j) + v * h (corners t j)) i
        else h (corners t (active t)) / 2)
      (if regular t then WeightedGraph.energy edgeSrc edgeDst
        (fun e => conductance
          (weights (a t) (fun i => q (corners t i) + u * h (corners t i)))
          (edgeSrc e) (edgeDst e)) (fun i => h (corners t i)) else 0) u := by
    intro t
    by_cases ht : regular t
    · simp only [if_pos ht]
      have hd := load_pairing_hasDerivAt (a t)
        (fun i => q (corners t i) + u * h (corners t i))
        (fun i => h (corners t i)) (ha t)
        (radicand_pos_all_coordinates (a t) (fun i => q (corners t i)) (ha t) (hs t ht) _)
      have hd' := hd
      rw [show (0 : ℝ) = u - u by ring] at hd'
      convert! hd'.comp_sub_const u u using 1
      funext v
      apply Finset.sum_congr rfl
      intro i _
      congr 2
      funext j
      ring
    · simp only [if_neg ht]
      exact hasDerivAt_const _ _
  have hd := (HasDerivAt.fun_sum (u := Finset.univ) (fun t _ => each t)).sub_const
    (∑ v, demand v * h v)
  convert! hd using 1
  simp only [WeightedGraph.energy, Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro t _
  by_cases ht : regular t <;> simp [ht]

end VolumeLogic.TrianglePotential
