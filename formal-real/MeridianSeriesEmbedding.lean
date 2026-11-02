import OperatorCoefficientAdapter
import Mathlib.LinearAlgebra.Vandermonde

noncomputable section
namespace VolumeLogic.MeridianSeriesEmbedding
open Polynomial OperatorCoefficientAdapter OperatorNormalization RecurrenceExpansion
open Filter Asymptotics
open scoped Topology

/-- The finite Laurent basis is sent to the literal exponential series. -/
theorem meridianSeries_C_mul_T (c : ℂ) (m : ℤ) :
    meridianSeries (LaurentPolynomial.C c * LaurentPolynomial.T m) =
      PowerSeries.C c * FormalExp.exponential ((m : ℂ) • (PowerSeries.X : PowerSeries ℂ)) := by
  rw [← LaurentPolynomial.single_eq_C_mul_T]
  change (AddMonoidAlgebra.single m c : LaurentPolynomial ℂ).coeff.sum
    (fun m c => PowerSeries.C c * FormalExp.exponential ((m : ℂ) • (PowerSeries.X : PowerSeries ℂ))) = _
  rw [AddMonoidAlgebra.coeff_single, Finsupp.sum_single_index]
  simp

/-- Each signed Laurent monomial maps to its corresponding exponential. -/
theorem meridianSeries_T (m : ℤ) :
    meridianSeries (LaurentPolynomial.T m) =
      FormalExp.exponential ((m : ℂ) • (PowerSeries.X : PowerSeries ℂ)) := by
  have h := meridianSeries_C_mul_T 1 m
  simpa using h

/-- Multiplication of the actual factorial exponential series. -/
theorem exponential_linear_mul (a b : ℂ) :
    FormalExp.exponential (a • (PowerSeries.X : PowerSeries ℂ)) *
      FormalExp.exponential (b • (PowerSeries.X : PowerSeries ℂ)) =
      FormalExp.exponential ((a+b) • (PowerSeries.X : PowerSeries ℂ)) := by
  simp only [FormalExp.exponential, ← PowerSeries.rescale_eq_subst]
  exact PowerSeries.exp_mul_exp_eq_exp_add a b

theorem meridianSeries_one : meridianSeries 1 = 1 := by
  have h := meridianSeries_C_mul_T 1 0
  simpa [FormalExp.exponential_zero] using h

theorem meridianSeries_mul (p q : LaurentPolynomial ℂ) :
    meridianSeries (p*q) = meridianSeries p * meridianSeries q := by
  induction p using LaurentPolynomial.induction_on' with
  | add p₁ p₂ hp₁ hp₂ => simp [add_mul, hp₁, hp₂]
  | C_mul_T m c =>
    induction q using LaurentPolynomial.induction_on' with
    | add q₁ q₂ hq₁ hq₂ => simp [mul_add, hq₁, hq₂]
    | C_mul_T n d =>
      have hprod : LaurentPolynomial.C c * LaurentPolynomial.T m *
          (LaurentPolynomial.C d * LaurentPolynomial.T n) =
          LaurentPolynomial.C (c*d) * LaurentPolynomial.T (m+n) := by
        rw [map_mul, LaurentPolynomial.T_add]
        ring
      rw [hprod, meridianSeries_C_mul_T, meridianSeries_C_mul_T, meridianSeries_C_mul_T]
      simp only [Int.cast_add, map_mul]
      rw [show PowerSeries.C c * PowerSeries.C d *
          FormalExp.exponential (((m : ℂ)+(n : ℂ)) • (PowerSeries.X : PowerSeries ℂ)) =
          PowerSeries.C c * PowerSeries.C d *
          (FormalExp.exponential ((m : ℂ) • (PowerSeries.X : PowerSeries ℂ)) *
          FormalExp.exponential ((n : ℂ) • (PowerSeries.X : PowerSeries ℂ))) by
            rw [exponential_linear_mul]]
      ring

/-- The literal meridian substitution, as a ring homomorphism. -/
def meridianRingHom : LaurentPolynomial ℂ →+* PowerSeries ℂ :=
  { meridianSeries with map_one' := meridianSeries_one, map_mul' := meridianSeries_mul }

theorem meridianRingHom_apply (p : LaurentPolynomial ℂ) :
    meridianRingHom p = meridianSeries p := rfl

/-- Its coefficient formula retains every signed Laurent exponent. -/
theorem meridianSeries_coeff (p : LaurentPolynomial ℂ) (n : ℕ) :
    PowerSeries.coeff n (meridianSeries p) =
      p.coeff.sum (fun m c => c * (m : ℂ)^n) * (algebraMap ℚ ℂ (1/(n.factorial : ℚ))) := by
  change PowerSeries.coeff n (p.coeff.sum
    (fun m c => PowerSeries.C c * FormalExp.exponential ((m : ℂ) • (PowerSeries.X : PowerSeries ℂ)))) = _
  simp only [Finsupp.sum, map_sum, PowerSeries.coeff_C_mul,
    FormalExp.exponential_linear_coeff]
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro m _
  ring


/-- The coefficient formula for a single signed meridian monomial. -/
theorem meridianSeries_T_coeff (m : ℤ) (n : ℕ) :
    PowerSeries.coeff n (meridianSeries (LaurentPolynomial.T m : LaurentPolynomial ℂ)) =
      (m : ℂ)^n * algebraMap ℚ ℂ (1/(n.factorial : ℚ)) := by
  rw [meridianSeries_T, FormalExp.exponential_linear_coeff]

/-- A zero series coefficient forces the corresponding finite moment to vanish. -/
theorem moment_zero_of_coefficient_zero (p : LaurentPolynomial ℂ) (n : ℕ)
    (hn : PowerSeries.coeff n (meridianSeries p) = 0) :
    p.coeff.sum (fun m c => c * (m : ℂ)^n) = 0 := by
  rw [meridianSeries_coeff] at hn
  apply (mul_eq_zero.mp hn).resolve_right
  simp [Nat.factorial_ne_zero]

/-- If a Laurent polynomial has t supported exponents, vanishing of its first t
exponential coefficients forces it to be zero. The bound depends on its support. -/
theorem meridianSeries_eq_zero_of_initial_coefficients (p : LaurentPolynomial ℂ)
    (hp : ∀ n < p.coeff.support.card, PowerSeries.coeff n (meridianSeries p) = 0) :
    p = 0 := by
  classical
  let I := ↥p.coeff.support
  let e : Fin (Fintype.card I) ≃ I := (Fintype.equivFin I).symm
  let f : Fin (Fintype.card I) → ℂ := fun i => ((e i).val : ℂ)
  let v : Fin (Fintype.card I) → ℂ := fun i => p.coeff (e i).val
  have hf : Function.Injective f := by
    intro i j hij
    apply e.injective
    apply Subtype.ext
    change ((e i).val : ℂ) = ((e j).val : ℂ) at hij
    exact_mod_cast hij
  have hv : v = 0 := by
    apply Matrix.eq_zero_of_forall_pow_sum_mul_pow_eq_zero hf
    intro i
    change (∑ j, p.coeff (e j).val * ((e j).val : ℂ)^(i : ℕ)) = 0
    rw [e.sum_comp (fun j : I => p.coeff j.val * (j.val : ℂ)^(i : ℕ))]
    have hi : (i : ℕ) < p.coeff.support.card := by simpa [I] using i.isLt
    have hm := moment_zero_of_coefficient_zero p (i : ℕ) (hp (i : ℕ) hi)
    change (∑ m ∈ p.coeff.support, p.coeff m * (m : ℂ)^(i : ℕ)) = 0 at hm
    rw [← Finset.sum_attach p.coeff.support
      (fun m => p.coeff m * (m : ℂ)^(i : ℕ))] at hm
    exact hm
  apply LaurentPolynomial.ext
  intro m
  by_cases hm : m ∈ p.coeff.support
  · have hc := congrFun hv (e.symm ⟨m,hm⟩)
    simpa [v] using hc
  · exact Finsupp.notMem_support_iff.mp hm

/-- On a specified finite exponent set, its first |E| coefficients determine
 the Laurent polynomial. Unknown varying supports require a larger bound. -/
theorem equal_of_initial_coefficients_on_support (E : Finset ℤ)
    (p q : LaurentPolynomial ℂ) (hp : p.coeff.support ⊆ E) (hq : q.coeff.support ⊆ E)
    (he : ∀ n < E.card, PowerSeries.coeff n (meridianSeries p) =
      PowerSeries.coeff n (meridianSeries q)) : p = q := by
  have hs : (p-q).coeff.support ⊆ E := by
    rw [AddMonoidAlgebra.coeff_sub]
    exact Finsupp.support_sub.trans (Finset.union_subset hp hq)
  apply sub_eq_zero.mp
  apply meridianSeries_eq_zero_of_initial_coefficients
  intro n hn
  rw [map_sub, map_sub, he n (lt_of_lt_of_le hn (Finset.card_le_card hs)), sub_self]

/-- The finite Vandermonde criterion implies faithfulness of the complete series. -/
theorem meridianSeries_eq_zero_iff (p : LaurentPolynomial ℂ) :
    meridianSeries p = 0 ↔ p = 0 := by
  constructor
  · intro hp
    exact meridianSeries_eq_zero_of_initial_coefficients p (by simp [hp])
  · rintro rfl
    exact map_zero meridianSeries

theorem meridianSeries_injective : Function.Injective meridianSeries := by
  intro p q he
  have hh : meridianSeries (p-q) = 0 := by simp [he]
  exact sub_eq_zero.mp ((meridianSeries_eq_zero_iff _).mp hh)


/-- Constants are unchanged by the meridian substitution. -/
theorem meridianSeries_C (c : ℂ) :
    meridianSeries (LaurentPolynomial.C c) = PowerSeries.C c := by
  have h := meridianSeries_C_mul_T c 0
  simpa [FormalExp.exponential_zero] using h

/-- The same faithful substitution respects the complex coefficient algebra. -/
def meridianAlgHom : LaurentPolynomial ℂ →ₐ[ℂ] PowerSeries ℂ :=
  { meridianRingHom with commutes' := meridianSeries_C }

theorem meridianAlgHom_injective : Function.Injective meridianAlgHom :=
  meridianSeries_injective

/-- The earlier finite formal symbol is exactly coefficientwise polynomial mapping. -/
theorem formalSymbol_eq_map (p : Polynomial (LaurentPolynomial ℂ)) :
    formalSymbol p = p.map meridianRingHom := by
  have h := congrArg (Polynomial.map meridianRingHom) (Polynomial.sum_monomial_eq p)
  simpa only [formalSymbol, Polynomial.sum_def, Polynomial.map_sum, Polynomial.map_monomial, meridianRingHom_apply] using h

theorem formalSymbol_injective : Function.Injective formalSymbol := by
  intro p q he
  apply Polynomial.map_injective meridianRingHom meridianSeries_injective
  simpa only [← formalSymbol_eq_map] using he

theorem formalSymbol_ne_zero {p : Polynomial (LaurentPolynomial ℂ)} (hp : p ≠ 0) :
    formalSymbol p ≠ 0 := by
  rw [formalSymbol_eq_map]
  exact (Polynomial.map_ne_zero_iff meridianSeries_injective).mpr hp

/-- Common-factor normalization produces a nonzero formal classical symbol. -/
theorem normalized_formalSymbol_ne_zero
    {P : Polynomial (Polynomial (LaurentPolynomial ℂ))} (hP : P ≠ 0) :
    formalSymbol (OperatorNormalization.classicalSymbol P) ≠ 0 :=
  formalSymbol_ne_zero (OperatorNormalization.classicalSymbol_ne_zero hP)

/-- The actual recurrence yields a nonzero formal classical polynomial vanishing
on the selected characteristic. The analytic and source hypotheses are unchanged. -/
theorem normalized_characteristic_faithful {ι : Type*} {l : Filter ι} [NeBot l]
    (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (hP : P ≠ 0)
    (r : ℕ)
    (hr : (Polynomial.Bivariate.swap (OperatorNormalization.normalize P)).natDegree ≤ r)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (N : ι → ℕ) (hN : Tendsto N l atTop)
    (F Z : ℂ → ℕ → ι → ℂ) (scale : ℂ → ι → ℂ)
    {D : Set ℂ} (hD : D.Infinite) (hDnr : ∀ s ∈ D, s.im ≠ 0)
    (hs : ∀ s ∈ D, ∀ᶠ n in l, scale s n ≠ 0)
    (hZ : ∀ s ∈ D, ∀ᶠ n in l, Z s 0 n ≠ 0)
    (hF : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j ≤ r, F s j n = scale s n * ActualGauge.sineNormalization (N n) (s+j) * Z s j n)
    (he : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1), actualCoefficient
        (LaurentPolynomial.eval₂ (RingHom.id ℂ) (meridianUnit (N n) s))
        (ActualGauge.levelRoot (N n)) P j * F s j n = 0)
    (hv : ∀ s ∈ D, ∀ j ≤ r,
      HasExpansion l (fun n => levelScale (N n))
        (fun n => Z s j n / Z s 0 n)
        (microscopic s (FormalExp.exponential
          (FormalShift.logarithmicShift S A (j : ℂ))))) :
    classicalSymbol P ≠ 0 ∧
      formalSymbol (classicalSymbol P) ≠ 0 ∧
      (formalSymbol (classicalSymbol P)).eval
        (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  obtain ⟨hclassical, hvanish⟩ := normalized_characteristic_of_record
    P hP r hr S A hS N hN F Z scale hD hDnr hs hZ hF he hv
  exact ⟨hclassical, formalSymbol_ne_zero hclassical, hvanish⟩

end VolumeLogic.MeridianSeriesEmbedding
