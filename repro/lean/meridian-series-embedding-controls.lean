import MeridianSeriesEmbedding

noncomputable section
namespace VolumeLogic.MeridianSeriesEmbeddingControls
open Polynomial OperatorCoefficientAdapter MeridianSeriesEmbedding

/-- A zero constant term does not make the meridian series zero. -/
theorem meridian_minus_one_has_nonzero_linear_term :
    meridianSeries (LaurentPolynomial.T 1 - 1 : LaurentPolynomial ℂ) ≠ 0 ∧
    PowerSeries.coeff 0 (meridianSeries (LaurentPolynomial.T 1 - 1 : LaurentPolynomial ℂ)) = 0 ∧
    PowerSeries.coeff 1 (meridianSeries (LaurentPolynomial.T 1 - 1 : LaurentPolynomial ℂ)) = 1 := by
  have hc : PowerSeries.coeff 1
      (meridianSeries (LaurentPolynomial.T 1 - 1 : LaurentPolynomial ℂ)) = 1 := by
    rw [map_sub, meridianSeries_one, map_sub, meridianSeries_T_coeff]
    norm_num
  refine ⟨?_, ?_, hc⟩
  · intro hz
    rw [hz, map_zero] at hc
    exact zero_ne_one hc
  · rw [map_sub, meridianSeries_one, map_sub, meridianSeries_T_coeff]
    norm_num

/-- Negative meridian powers become genuine inverses, with the expected sign. -/
theorem negative_power_is_inverse :
    meridianSeries (LaurentPolynomial.T (-1) : LaurentPolynomial ℂ) *
      meridianSeries (LaurentPolynomial.T 1 : LaurentPolynomial ℂ) = 1 ∧
    PowerSeries.coeff 1 (meridianSeries (LaurentPolynomial.T (-1) : LaurentPolynomial ℂ)) = -1 := by
  constructor
  · rw [← meridianSeries_mul]
    rw [← LaurentPolynomial.T_add]
    norm_num [meridianSeries_one]
  · rw [meridianSeries_T_coeff]
    norm_num

/-- No fixed number of initial coefficients suffices without a support bound. -/
theorem arbitrarily_long_zero_initial_jets (k : ℕ) :
    meridianSeries ((LaurentPolynomial.T 1 - 1)^k : LaurentPolynomial ℂ) ≠ 0 ∧
    ∀ n < k, PowerSeries.coeff n
      (meridianSeries ((LaurentPolynomial.T 1 - 1)^k : LaurentPolynomial ℂ)) = 0 := by
  have hpow : meridianSeries ((LaurentPolynomial.T 1 - 1)^k : LaurentPolynomial ℂ) =
      meridianSeries (LaurentPolynomial.T 1 - 1 : LaurentPolynomial ℂ)^k :=
    map_pow meridianRingHom _ k
  rw [hpow]
  refine ⟨pow_ne_zero k meridian_minus_one_has_nonzero_linear_term.1, ?_⟩
  intro n hn
  have hc : PowerSeries.constantCoeff
      (meridianSeries (LaurentPolynomial.T 1 - 1 : LaurentPolynomial ℂ)) = 0 := by
    simpa only [PowerSeries.coeff_zero_eq_constantCoeff] using
      meridian_minus_one_has_nonzero_linear_term.2.1
  have ho := PowerSeries.le_order_pow_of_constantCoeff_eq_zero k hc
  exact PowerSeries.coeff_of_lt_order n (lt_of_lt_of_le (by exact_mod_cast hn) ho)

/-- Coefficient embedding is faithful, but substitution of a selected L-series is not. -/
theorem selected_longitude_evaluation_has_kernel :
    formalSymbol (Polynomial.X + Polynomial.C (LaurentPolynomial.T 1) :
      Polynomial (LaurentPolynomial ℂ)) ≠ 0 ∧
    (formalSymbol (Polynomial.X + Polynomial.C (LaurentPolynomial.T 1) :
      Polynomial (LaurentPolynomial ℂ))).eval
      (-FormalExp.exponential ((1 : ℂ) • (PowerSeries.X : PowerSeries ℂ))) = 0 := by
  constructor
  · apply formalSymbol_ne_zero
    intro hz
    have hh := congrArg (fun p : Polynomial (LaurentPolynomial ℂ) => p.coeff 1) hz
    simp at hh
  · rw [formalSymbol_eq_map]
    simp [meridianRingHom_apply, meridianSeries_T]

end VolumeLogic.MeridianSeriesEmbeddingControls

#print axioms VolumeLogic.MeridianSeriesEmbeddingControls.meridian_minus_one_has_nonzero_linear_term
#print axioms VolumeLogic.MeridianSeriesEmbeddingControls.negative_power_is_inverse
#print axioms VolumeLogic.MeridianSeriesEmbeddingControls.arbitrarily_long_zero_initial_jets
#print axioms VolumeLogic.MeridianSeriesEmbeddingControls.selected_longitude_evaluation_has_kernel
