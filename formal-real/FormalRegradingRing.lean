import FormalShift
import VolumeLogic.FormalRegrading
import Mathlib.Algebra.Ring.GrindInstances

/-! The actual map R[[h,u]] -> R[s][[h]], h |-> h,
u |-> h*s. No coefficient recovery or injectivity is assumed. -/

noncomputable section
namespace VolumeLogic.FormalRegradingRing
open PowerSeries MvPowerSeries FormalShift
variable {R : Type*} [_root_.CommRing R]

/-- The target has polynomial coefficients in s and formal variable h. -/
def targetVariables : Fin 2 → PowerSeries (Polynomial R) :=
  ![PowerSeries.X, PowerSeries.C Polynomial.X * PowerSeries.X]

theorem targetVariables_hasSubst : MvPowerSeries.HasSubst (targetVariables (R := R)) :=
  MvPowerSeries.hasSubst_of_constantCoeff_zero (fun i => by
    fin_cases i <;> simp [targetVariables, PowerSeries.X])

/-- Actual admissible power-series substitution, with its algebra structure. -/
def regrading : MvPowerSeries (Fin 2) R →ₐ[R] PowerSeries (Polynomial R) :=
  MvPowerSeries.substAlgHom targetVariables_hasSubst

theorem regrading_add (F G : MvPowerSeries (Fin 2) R) :
    regrading (F+G) = regrading F + regrading G := map_add regrading F G

theorem regrading_mul (F G : MvPowerSeries (Fin 2) R) :
    regrading (F*G) = regrading F * regrading G := map_mul regrading F G

/-- Each monomial has one possible h degree and one possible s degree. -/
theorem monomial_image (e : Fin 2 →₀ ℕ) :
    e.prod (fun i k => (targetVariables (R := R) i)^k) =
      PowerSeries.C (Polynomial.X ^ e 1) * PowerSeries.X ^ (e 0 + e 1) := by
  rw [Finsupp.prod_fintype _ _ (fun _ => by simp)]
  simp only [Fin.prod_univ_two, targetVariables, Matrix.cons_val_zero, Matrix.cons_val_one,
    mul_pow, ← map_pow]
  rw [pow_add]
  exact mul_left_comm _ _ _

theorem monomial_image_coeff (e : Fin 2 →₀ ℕ) (n b : ℕ) :
    Polynomial.coeff
      (PowerSeries.coeff n (e.prod (fun i k => (targetVariables (R := R) i)^k))) b =
      if n = e 0 + e 1 ∧ b = e 1 then 1 else 0 := by
  rw [monomial_image, PowerSeries.coeff_C_mul_X_pow]
  split <;> simp_all [Polynomial.coeff_X_pow]

/-- The full coefficient formula, including the unsupported triangular region. -/
theorem regrading_coeff (F : MvPowerSeries (Fin 2) R) (n b : ℕ) :
    Polynomial.coeff (PowerSeries.coeff n (regrading F)) b =
      if b ≤ n then bc F (n-b) b else 0 := by
  rw [regrading, MvPowerSeries.substAlgHom_apply]
  change Polynomial.coeff
    (MvPowerSeries.coeff (Finsupp.single () n)
      (MvPowerSeries.subst (S := Polynomial R) (targetVariables (R := R)) F)) b = _
  rw [MvPowerSeries.coeff_subst targetVariables_hasSubst]
  change (Polynomial.lcoeff R b).toAddMonoidHom _ = _
  rw [(Polynomial.lcoeff R b).toAddMonoidHom.map_finsum
    (MvPowerSeries.coeff_subst_finite targetVariables_hasSubst F (Finsupp.single () n))]
  simp only [LinearMap.toAddMonoidHom_coe, map_smul, Polynomial.lcoeff_apply,
    PowerSeries.coeff_coeToMvPowerSeries, monomial_image_coeff, smul_eq_mul]
  by_cases hb : b ≤ n
  · rw [if_pos hb]
    rw [finsum_eq_single _ (index (n-b) b)]
    · simp [bc, Nat.sub_add_cancel hb]
    · intro e he
      have hn : ¬ (n = e 0 + e 1 ∧ b = e 1) := by
        rintro ⟨hn, hb'⟩
        apply he
        ext i
        fin_cases i <;> simp [index, hb', hn]
      simp [hn]
  · rw [if_neg hb]
    apply finsum_eq_zero_of_forall_eq_zero
    intro e
    have hn : ¬ (n = e 0 + e 1 ∧ b = e 1) := by omega
    simp [hn]


/-- Each source coefficient is recovered at one literal coefficient of the
actual polynomial-coefficient target. -/
theorem coefficient_recovery (F : MvPowerSeries (Fin 2) R) (a b : ℕ) :
    Polynomial.coeff (PowerSeries.coeff (a+b) (regrading F)) b = bc F a b := by
  rw [regrading_coeff]
  simp

/-- This identifies the actual substitution with the old Std coefficient table. -/
theorem std_table_compatibility (F : MvPowerSeries (Fin 2) R) :
    (fun n b => Polynomial.coeff (PowerSeries.coeff n (regrading F)) b) =
      VolumeLogic.regrade (bc F) := by
  funext n b
  exact regrading_coeff F n b

theorem regrading_injective : Function.Injective (regrading (R := R)) := by
  intro F G h
  apply MvPowerSeries.ext
  intro e
  have he : e = index (e 0) (e 1) := by
    ext i
    fin_cases i <;> simp [index]
  have hc := congrArg
    (fun P => Polynomial.coeff (PowerSeries.coeff (e 0 + e 1) P) (e 1)) h
  rw [coefficient_recovery, coefficient_recovery] at hc
  simpa only [bc, ← he] using hc

theorem regrading_zero_iff (F : MvPowerSeries (Fin 2) R) :
    regrading F = 0 ↔ F = 0 := by
  constructor
  · intro h
    apply regrading_injective
    simpa using h
  · intro h
    simp [h]

theorem finite_order_iff (F G : MvPowerSeries (Fin 2) R) (L : ℕ) :
    (∀ n, n ≤ L → PowerSeries.coeff n (regrading F) = PowerSeries.coeff n (regrading G)) ↔
      (∀ a b, a+b ≤ L → bc F a b = bc G a b) := by
  constructor
  · intro h a b hab
    have hc := congrArg (fun p : Polynomial R => p.coeff b) (h (a+b) hab)
    simpa only [coefficient_recovery] using hc
  · intro h n hn
    apply Polynomial.ext
    intro b
    rw [regrading_coeff, regrading_coeff]
    split
    · exact h (n-b) b (by omega)
    · rfl

theorem coefficient_degree (F : MvPowerSeries (Fin 2) R) (n : ℕ) :
    (PowerSeries.coeff n (regrading F)).natDegree ≤ n := by
  apply Polynomial.natDegree_le_iff_coeff_eq_zero.mpr
  intro b hb
  rw [regrading_coeff, if_neg (by omega)]

theorem regrading_h : regrading (MvPowerSeries.X 0 : MvPowerSeries (Fin 2) R) =
    PowerSeries.X := by
  rw [regrading, MvPowerSeries.substAlgHom_X]
  rfl

theorem regrading_u : regrading (MvPowerSeries.X 1 : MvPowerSeries (Fin 2) R) =
    PowerSeries.C Polynomial.X * PowerSeries.X := by
  rw [regrading, MvPowerSeries.substAlgHom_X]
  rfl

end VolumeLogic.FormalRegradingRing
