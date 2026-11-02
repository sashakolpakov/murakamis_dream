import OperatorCoefficientAdapter

noncomputable section
namespace VolumeLogic.OperatorCoefficientAdapterControls
open Polynomial OperatorCoefficientAdapter OperatorNormalization LaurentExpansion

/-- A negative meridian exponent is retained exactly in the finite table. -/
theorem negative_meridian_exponent_retained :
    encode (Polynomial.monomial 2 (LaurentPolynomial.T (-3) : LaurentPolynomial ℂ)) (2,-3) = 1 := by
  change encode (Polynomial.monomial 2 (LaurentPolynomial.T (-3) : LaurentPolynomial ℂ))
    ((2 : ℕ), -3) = 1
  rw [encode_coefficient]
  simp

/-- q degree and shift degree occupy different indices; the transpose is essential. -/
theorem shift_degree_is_not_q_degree :
    operatorFamily (Polynomial.monomial 2
      (Polynomial.monomial 3 (LaurentPolynomial.T (-1) : LaurentPolynomial ℂ))) 3 (2,-1) = 1 ∧
    operatorFamily (Polynomial.monomial 2
      (Polynomial.monomial 3 (LaurentPolynomial.T (-1) : LaurentPolynomial ℂ))) 2 = 0 := by
  constructor
  · simp only [operatorFamily, shiftPolynomial, Polynomial.Bivariate.swap_monomial_monomial,
      Polynomial.coeff_monomial]
    change encode (Polynomial.monomial 2 (LaurentPolynomial.T (-1) : LaurentPolynomial ℂ))
      ((2 : ℕ), -1) = 1
    rw [encode_coefficient]
    simp
  · simp [operatorFamily, shiftPolynomial, Polynomial.Bivariate.swap_monomial_monomial,
      Polynomial.coeff_monomial, encode_zero]

/-- Injectivity of the finite encoding does not make the q=1 projection injective. -/
theorem classical_projection_can_vanish :
    encode (Polynomial.X - 1 : Polynomial (LaurentPolynomial ℂ)) ≠ 0 ∧
    classicalCoefficient (encode (Polynomial.X - 1 : Polynomial (LaurentPolynomial ℂ))) = 0 := by
  constructor
  · intro hh
    have hp := encode_injective (hh.trans encode_zero.symm)
    exact Polynomial.X_sub_C_ne_zero (1 : LaurentPolynomial ℂ) (by simpa using hp)
  · rw [classicalCoefficient_encode]
    simp

/-- A zero truncated family does not justify omitting the only L coefficient.
The final wrapper excludes this with its explicit degree bound. -/
theorem omitted_shift_invalidates_degree_bound :
    operatorFamily (Polynomial.C Polynomial.X : Polynomial (Polynomial (LaurentPolynomial ℂ))) 0 = 0 ∧
    ¬ (Polynomial.Bivariate.swap
      (OperatorNormalization.normalize
        (Polynomial.C Polynomial.X : Polynomial (Polynomial (LaurentPolynomial ℂ))))).natDegree ≤ 0 := by
  have hn : OperatorNormalization.normalize
      (Polynomial.C Polynomial.X : Polynomial (Polynomial (LaurentPolynomial ℂ))) =
      Polynomial.C Polynomial.X := by
    simp [OperatorNormalization.normalize, commonOrder]
  constructor
  · simp [operatorFamily, shiftPolynomial, Polynomial.Bivariate.swap_C, encode_zero]
  · rw [hn]
    simp [Polynomial.Bivariate.swap_C]

end VolumeLogic.OperatorCoefficientAdapterControls

#print axioms VolumeLogic.OperatorCoefficientAdapterControls.negative_meridian_exponent_retained
#print axioms VolumeLogic.OperatorCoefficientAdapterControls.shift_degree_is_not_q_degree
#print axioms VolumeLogic.OperatorCoefficientAdapterControls.classical_projection_can_vanish
#print axioms VolumeLogic.OperatorCoefficientAdapterControls.omitted_shift_invalidates_degree_bound
