import OperatorNormalization
import Mathlib.Algebra.Polynomial.RingDivision

noncomputable section
namespace VolumeLogic.OperatorNormalizationControls
open Polynomial OperatorNormalization

theorem pure_factor_normalizes_to_one (k : ℕ) :
    OperatorNormalization.normalize ((Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))^k) = 1 := by
  unfold OperatorNormalization.normalize commonOrder
  rw [Polynomial.rootMultiplicity_X_sub_C_pow]
  simpa only [mul_one] using Polynomial.mul_divByMonic_cancel_left
    (1 : Polynomial (Polynomial ℂ)) ((Polynomial.monic_X_sub_C 1).pow k)

/-- Direct specialization can erase an entire nonzero operator. -/
theorem raw_specialization_loses_operator :
    ((Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))^3).eval 1 = 0 ∧
    (Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))^3 ≠ 0 := by
  constructor
  · simp
  · exact pow_ne_zero 3 (Polynomial.X_sub_C_ne_zero 1)

/-- The leading h coefficient is recovered after stripping the full order. -/
theorem third_order_symbol_recovered :
    commonOrder ((Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))^3) = 3 ∧
    PowerSeries.coeff 3 (qTaylor ((Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))^3)) = 1 := by
  have ho : commonOrder ((Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))^3) = 3 := by
    exact Polynomial.rootMultiplicity_X_sub_C_pow 1 3
  refine ⟨ho, ?_⟩
  have hl := qTaylor_leading_coefficient
    ((Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))^3)
  rw [ho] at hl
  rw [hl, classicalSymbol, pure_factor_normalizes_to_one]
  simp

/-- A nonzero retained Laurent factor may vanish at the complete point. -/
theorem meridian_vanishes_only_after_evaluation :
    meridian ≠ 0 ∧ LaurentPolynomial.eval₂ (RingHom.id ℂ) (1 : ℂˣ) meridian = 0 := by
  constructor
  · exact meridian_ne_zero
  · simp [meridian, LaurentPolynomial.eval₂_T]

/-- Recurrence preservation really requires q≠1: the original coefficient
can vanish there while the normalized coefficient equals one. -/
theorem q_one_cancellation_is_invalid :
    actualCoefficient (RingHom.id ℂ) 1
      (Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ)) 0 = 0 ∧
    actualCoefficient (RingHom.id ℂ) 1
      (OperatorNormalization.normalize (Polynomial.X - Polynomial.C 1 : Polynomial (Polynomial ℂ))) 0 = 1 := by
  constructor
  · simp [actualCoefficient]
  · have hh := pure_factor_normalizes_to_one 1
    simp only [pow_one] at hh
    rw [hh]
    simp [actualCoefficient]

/-- The zero record is excluded from the nonzero-symbol theorem. -/
theorem zero_record_has_zero_symbol : classicalSymbol (0 : Polynomial (Polynomial ℂ)) = 0 := by
  simp [classicalSymbol, OperatorNormalization.normalize, commonOrder]

/-- The L↦-L change is nontrivial and changes evaluation. -/
theorem sign_change_is_retained :
    (((Polynomial.X + 1 : Polynomial ℂ).comp (-Polynomial.X)).eval 1) = 0 ∧
    (Polynomial.X + 1 : Polynomial ℂ).eval 1 = 2 := by
  norm_num

end VolumeLogic.OperatorNormalizationControls

#print axioms VolumeLogic.OperatorNormalizationControls.pure_factor_normalizes_to_one
#print axioms VolumeLogic.OperatorNormalizationControls.raw_specialization_loses_operator
#print axioms VolumeLogic.OperatorNormalizationControls.third_order_symbol_recovered
#print axioms VolumeLogic.OperatorNormalizationControls.meridian_vanishes_only_after_evaluation
#print axioms VolumeLogic.OperatorNormalizationControls.q_one_cancellation_is_invalid
#print axioms VolumeLogic.OperatorNormalizationControls.zero_record_has_zero_symbol
#print axioms VolumeLogic.OperatorNormalizationControls.sign_change_is_retained
