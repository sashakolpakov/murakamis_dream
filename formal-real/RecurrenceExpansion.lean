import FormalCharacteristic
import Mathlib.RingTheory.PowerSeries.Trunc
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Topology.Algebra.Polynomial

noncomputable section
open Filter Asymptotics
open scoped Topology
namespace VolumeLogic.RecurrenceExpansion

variable {ι : Type*} {l : Filter ι} {h : ι → ℂ}

/-- Every finite truncation approximates the actual function with the next
power as remainder. No convergence of the formal series is asserted. -/
def HasExpansion (l : Filter ι) (h f : ι → ℂ) (P : PowerSeries ℂ) : Prop :=
  ∀ m : ℕ, (fun n => f n - (P.trunc (m+1)).eval (h n))
    =O[l] (fun n => h n ^ (m+1))

theorem polynomial_bounded (P : Polynomial ℂ) (ht : Tendsto h l (𝓝 0)) :
    (fun n => P.eval (h n)) =O[l] (fun _ => (1 : ℂ)) :=
  (P.continuous.tendsto 0 |>.comp ht).isBigO_one ℂ

theorem eval_isBigO_of_X_pow_dvd (P : Polynomial ℂ) (m : ℕ)
    (ht : Tendsto h l (𝓝 0)) (hd : Polynomial.X ^ m ∣ P) :
    (fun n => P.eval (h n)) =O[l] (fun n => h n ^ m) := by
  obtain ⟨Q, rfl⟩ := hd
  simpa using (isBigO_refl (fun n => h n ^ m) l).mul (polynomial_bounded Q ht)

theorem trunc_product_remainder (P Q : PowerSeries ℂ) (m : ℕ)
    (ht : Tendsto h l (𝓝 0)) :
    (fun n => (P.trunc (m+1)).eval (h n) * (Q.trunc (m+1)).eval (h n) -
      ((P*Q).trunc (m+1)).eval (h n)) =O[l] (fun n => h n ^ (m+1)) := by
  have hd : Polynomial.X ^ (m+1) ∣
      P.trunc (m+1) * Q.trunc (m+1) - (P*Q).trunc (m+1) := by
    rw [Polynomial.X_pow_dvd_iff]
    intro d hd
    rw [Polynomial.coeff_sub, PowerSeries.coeff_trunc, if_pos hd]
    have hc := PowerSeries.coeff_mul_eq_coeff_trunc_mul_trunc P Q hd
    apply sub_eq_zero.mpr
    simpa only [← Polynomial.coe_mul, Polynomial.coeff_coe] using hc.symm
  simpa using eval_isBigO_of_X_pow_dvd _ (m+1) ht hd

/-- A polynomial evaluated on the scale has its literal finite coefficient
series as an asymptotic expansion, with no missing Cauchy coefficients. -/
theorem hasExpansion_polynomial (P : Polynomial ℂ)
    (ht : Tendsto h l (𝓝 0)) :
    HasExpansion l h (fun n => P.eval (h n)) (P : PowerSeries ℂ) := by
  intro m
  have hd : Polynomial.X ^ (m+1) ∣ P - (P : PowerSeries ℂ).trunc (m+1) := by
    rw [Polynomial.X_pow_dvd_iff]
    intro d hd
    simp [Polynomial.coeff_sub, PowerSeries.coeff_trunc, hd, Polynomial.coeff_coe]
  simpa using eval_isBigO_of_X_pow_dvd _ (m+1) ht hd

theorem HasExpansion.bounded {f : ι → ℂ} {P : PowerSeries ℂ}
    (hf : HasExpansion l h f P) (ht : Tendsto h l (𝓝 0)) :
    f =O[l] (fun _ => (1 : ℂ)) := by
  have hb : (fun n => h n ^ (0+1)) =O[l] (fun _ => (1 : ℂ)) := by
    simpa only [Nat.zero_add, pow_one] using ht.isBigO_one ℂ
  have hr := (hf 0).trans hb
  have hp := polynomial_bounded (P.trunc 1) ht
  simpa using hr.add hp

theorem HasExpansion.mul {f g : ι → ℂ} {P Q : PowerSeries ℂ}
    (hf : HasExpansion l h f P) (hg : HasExpansion l h g Q)
    (ht : Tendsto h l (𝓝 0)) :
    HasExpansion l h (fun n => f n * g n) (P*Q) := by
  intro m
  have ha : (fun n => (f n - (P.trunc (m+1)).eval (h n)) * g n)
      =O[l] (fun n => h n ^ (m+1)) := by
    simpa only [mul_one] using (hf m).mul (hg.bounded ht)
  have hb : (fun n => (P.trunc (m+1)).eval (h n) *
      (g n - (Q.trunc (m+1)).eval (h n))) =O[l] (fun n => h n ^ (m+1)) := by
    simpa only [one_mul] using (polynomial_bounded (P.trunc (m+1)) ht).mul (hg m)
  have hc := trunc_product_remainder P Q m ht
  have hh := (ha.add hb).add hc
  apply hh.congr_left
  intro n
  dsimp
  ring

theorem HasExpansion.sum {κ : Type*} (s : Finset κ)
    {f : κ → ι → ℂ} {P : κ → PowerSeries ℂ}
    (hf : ∀ j ∈ s, HasExpansion l h (f j) (P j)) :
    HasExpansion l h (fun n => ∑ j ∈ s, f j n) (∑ j ∈ s, P j) := by
  intro m
  have hh := IsBigO.sum (s := s) (fun j hj => hf j hj m)
  simpa [Finset.sum_sub_distrib, map_sum, Polynomial.eval_finsetSum] using hh


theorem hasExpansion_const (c : ℂ) :
    HasExpansion l h (fun _ => c) (PowerSeries.C c) := by
  intro m
  simpa using (isBigO_zero (fun n => h n ^ (m+1)) l)

theorem HasExpansion.prod {κ : Type*} (s : Finset κ)
    {f : κ → ι → ℂ} {P : κ → PowerSeries ℂ}
    (hf : ∀ j ∈ s, HasExpansion l h (f j) (P j))
    (ht : Tendsto h l (𝓝 0)) :
    HasExpansion l h (fun n => ∏ j ∈ s, f j n) (∏ j ∈ s, P j) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using (hasExpansion_const (l := l) (h := h) 1)
  | @insert j s hj ih =>
      have hjf := hf j (Finset.mem_insert_self j s)
      have hs := ih (fun k hk => hf k (Finset.mem_insert_of_mem hk))
      simpa [Finset.prod_insert hj] using hjf.mul hs ht

/-- Evaluate the polynomial parameter after the actual regrading map. -/
def microscopic (s : ℂ) : MvPowerSeries (Fin 2) ℂ →+* PowerSeries ℂ :=
  (PowerSeries.map (Polynomial.evalRingHom s)).comp
    FormalRegradingRing.regrading.toRingHom

theorem microscopic_coeff (s : ℂ) (B : MvPowerSeries (Fin 2) ℂ) (m : ℕ) :
    PowerSeries.coeff m (microscopic s B) =
      (PowerSeries.coeff m (FormalRegradingRing.regrading B)).eval s := by
  simp [microscopic, PowerSeries.coeff_map]

theorem trunc_eval (P : PowerSeries ℂ) (m : ℕ) (z : ℂ) :
    (P.trunc (m+1)).eval z =
      ∑ i ∈ Finset.range (m+1), PowerSeries.coeff i P * z^i := by
  simp [PowerSeries.trunc_apply, Polynomial.eval_finsetSum]

/-- Assemble the whole finite equation from its individual coefficient and
shift-ratio expansions. This is genuine multiplication of asymptotic series;
the next-order tail of the truncated Cauchy product was proved above. -/
theorem finite_equation_expansion (r : ℕ)
    (a b : ℕ → MvPowerSeries (Fin 2) ℂ) (s : ℂ)
    (c v : ℕ → ι → ℂ) (ht : Tendsto h l (𝓝 0))
    (hc : ∀ j ≤ r, HasExpansion l h (c j) (microscopic s (a j)))
    (hv : ∀ j ≤ r, HasExpansion l h (v j) (microscopic s (b j))) :
    HasExpansion l h (fun n => ∑ j ∈ Finset.range (r+1), c j n * v j n)
      (microscopic s (∑ j ∈ Finset.range (r+1), a j * b j)) := by
  simp only [map_sum, map_mul]
  apply HasExpansion.sum
  intro j hj
  have hjr : j ≤ r := by have := Finset.mem_range.mp hj; omega
  exact (hc j hjr).mul (hv j hjr) ht

theorem characteristic_of_factor_expansions [NeBot l]
    (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (c v : ℂ → ℕ → ι → ℂ) {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1), c s j n * v s j n = 0)
    (hc : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (c s j)
      (microscopic s (FormalGauge.clearedCoefficient r a j)))
    (hv : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (v s j)
      (microscopic s (FormalExp.exponential (FormalShift.logarithmicShift S A (j : ℂ))))) :
    (FormalCharacteristic.classicalPolynomial r (fun j => FormalShift.atHZero (a j))).eval
      (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  apply FormalCharacteristic.gauged_classical_identity_from_all_orders r a S A hS
    hD ht hn hz
  intro s hs m
  have he := finite_equation_expansion r (FormalGauge.clearedCoefficient r a)
    (fun j => FormalExp.exponential (FormalShift.logarithmicShift S A (j : ℂ)))
    s (c s) (v s) ht (hc s hs) (hv s hs) m
  simpa only [trunc_eval, microscopic_coeff, FormalCharacteristic.shiftedEquation] using he

end VolumeLogic.RecurrenceExpansion
