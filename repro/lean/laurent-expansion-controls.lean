import LaurentExpansion

noncomputable section
namespace VolumeLogic.LaurentExpansionControls
open LaurentExpansion RecurrenceExpansion

theorem negative_powers_are_evaluated :
    evaluate (Finsupp.single ((-2 : ℤ), (3 : ℤ)) (1 : ℂ)) 2 3 = 27/4 := by
  rw [evaluate_single]
  norm_num

theorem mixed_linear_coefficient (s : ℂ) :
    PowerSeries.coeff 1 (microscopic s
      (formalCoefficient (Finsupp.single ((-2 : ℤ), (3 : ℤ)) (1 : ℂ)))) =
        -2+3*s := by
  rw [microscopic_single]
  simp [FormalExp.exponential_linear_coeff]

theorem mixed_quadratic_coefficient (s : ℂ) :
    PowerSeries.coeff 2 (microscopic s
      (formalCoefficient (Finsupp.single ((-2 : ℤ), (3 : ℤ)) (1 : ℂ)))) =
        (-2+3*s)^2/2 := by
  rw [microscopic_single]
  norm_num [FormalExp.exponential_linear_coeff]
  ring

theorem nonzero_laurent_may_have_zero_classical_symbol :
    let a : Coefficient := Finsupp.single (1,0) 1 + Finsupp.single (0,0) (-1)
    a ≠ 0 ∧ classicalCoefficient a = 0 := by
  dsimp
  constructor
  · intro h
    have hh := congrArg (fun a : Coefficient => a (1,0)) h
    norm_num at hh
  · rw [classicalCoefficient_add, classicalCoefficient_single,
      classicalCoefficient_single]
    simp [FormalExp.exponential_zero]

end VolumeLogic.LaurentExpansionControls

#print axioms VolumeLogic.LaurentExpansionControls.negative_powers_are_evaluated
#print axioms VolumeLogic.LaurentExpansionControls.mixed_linear_coefficient
#print axioms VolumeLogic.LaurentExpansionControls.mixed_quadratic_coefficient
#print axioms VolumeLogic.LaurentExpansionControls.nonzero_laurent_may_have_zero_classical_symbol
