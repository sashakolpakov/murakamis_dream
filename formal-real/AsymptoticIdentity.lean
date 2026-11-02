import Mathlib.Analysis.Asymptotics.Lemmas
import Mathlib.Analysis.Complex.Basic
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.RingTheory.PowerSeries.Basic

noncomputable section
open Filter Asymptotics
open scoped Topology

namespace VolumeLogic.AsymptoticIdentity

variable {ι : Type*} {l : Filter ι} [NeBot l]

/-- A coefficient cannot have the order of the next power of a nonzero scale
which tends to zero. No positivity or real-valued scale is assumed. -/
theorem coefficient_zero_of_next_order {h : ι → ℂ} {c : ℂ} (m : ℕ)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (ho : (fun n => c * h n ^ m) =O[l] (fun n => h n ^ (m+1))) : c = 0 := by
  have hs : (fun n => h n ^ (m+1)) =o[l] (fun n => h n ^ m) :=
    (isLittleO_pow_pow (Nat.lt_succ_self m)).comp_tendsto ht
  have hq := (ho.trans_isLittleO hs).tendsto_div_nhds_zero
  have he : (fun n => (c * h n ^ m) / h n ^ m) =ᶠ[l] (fun _ => c) := by
    filter_upwards [hn] with n hne
    simp [hne]
  exact tendsto_nhds_unique tendsto_const_nhds (hq.congr' he)

/-- Actual asymptotic estimates through every order determine the coefficients
of an eventually zero function. The remainder is one order smaller than the
last coefficient being recovered. -/
theorem coefficients_zero_of_all_orders {F h : ι → ℂ} (c : ℕ → ℂ)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ᶠ n in l, F n = 0)
    (ho : ∀ m : ℕ,
      (fun n => F n - ∑ i ∈ Finset.range (m+1), c i * h n ^ i)
        =O[l] (fun n => h n ^ (m+1))) : ∀ m, c m = 0 := by
  intro m
  induction m using Nat.strong_induction_on with
  | h m ih =>
    have hp (n : ι) : (∑ i ∈ Finset.range (m+1), c i * h n ^ i) =
        c m * h n ^ m := by
      rw [Finset.sum_range_succ]
      have hzsum : (∑ i ∈ Finset.range m, c i * h n ^ i) = 0 := by
        apply Finset.sum_eq_zero
        intro i hi
        simp [ih i (Finset.mem_range.mp hi)]
      simp [hzsum]
    have hm : (fun n => -(c m * h n ^ m)) =O[l] (fun n => h n ^ (m+1)) := by
      apply (ho m).congr'
      · filter_upwards [hz] with n hzero
        simp [hzero, hp]
      · exact Filter.EventuallyEq.rfl
    apply coefficient_zero_of_next_order m ht hn
    simpa using hm.neg_left

/-- If the coefficients are polynomials in a parameter, their vanishing on
an infinite parameter set makes them zero polynomials. The asymptotic
constants and thresholds may depend on the parameter and the order. -/
theorem coefficient_polynomials_zero {F : ℂ → ι → ℂ} {h : ι → ℂ}
    (p : ℕ → Polynomial ℂ) {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ s ∈ D, ∀ᶠ n in l, F s n = 0)
    (ho : ∀ s ∈ D, ∀ m : ℕ,
      (fun n => F s n - ∑ i ∈ Finset.range (m+1), (p i).eval s * h n ^ i)
        =O[l] (fun n => h n ^ (m+1))) : ∀ m, p m = 0 := by
  intro m
  apply Polynomial.eq_zero_of_infinite_isRoot
  apply hD.mono
  intro s hs
  exact coefficients_zero_of_all_orders (fun i => (p i).eval s) ht hn (hz s hs)
    (ho s hs) m

theorem formal_series_zero {F : ℂ → ι → ℂ} {h : ι → ℂ}
    (P : PowerSeries (Polynomial ℂ)) {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ s ∈ D, ∀ᶠ n in l, F s n = 0)
    (ho : ∀ s ∈ D, ∀ m : ℕ,
      (fun n => F s n - ∑ i ∈ Finset.range (m+1),
        (PowerSeries.coeff i P).eval s * h n ^ i)
        =O[l] (fun n => h n ^ (m+1))) : P = 0 := by
  apply PowerSeries.ext
  intro m
  simpa using coefficient_polynomials_zero (fun i => PowerSeries.coeff i P)
    hD ht hn hz ho m

end VolumeLogic.AsymptoticIdentity
