import MeridianExpansion

noncomputable section
namespace VolumeLogic.MeridianExpansionControls
open RecurrenceExpansion FormalExp

/-- The shift j survives in the first coefficient; replacing it by s loses data. -/
theorem linear_shift_retained (s : ℂ) (j : ℕ) :
    PowerSeries.coeff 1 (microscopic s (FormalGauge.shiftedMeridian j)) = 2*(s+j) := by
  rw [microscopic_shiftedMeridian, map_sub,
    exponential_linear_coeff, exponential_linear_coeff]
  norm_num
  ring

/-- The second coefficient vanishes by the exact difference of exponentials. -/
theorem even_coefficient_vanishes (s : ℂ) (j : ℕ) :
    PowerSeries.coeff 2 (microscopic s (FormalGauge.shiftedMeridian j)) = 0 := by
  rw [microscopic_shiftedMeridian, map_sub,
    exponential_linear_coeff, exponential_linear_coeff]
  norm_num
  ring

/-- The next odd coefficient is retained, so the meridian is not linearized. -/
theorem cubic_coefficient_retained (s : ℂ) (j : ℕ) :
    PowerSeries.coeff 3 (microscopic s (FormalGauge.shiftedMeridian j)) = (s+j)^3/3 := by
  rw [microscopic_shiftedMeridian, map_sub,
    exponential_linear_coeff, exponential_linear_coeff]
  norm_num
  ring

/-- At the real parameter s=-j the shifted divisor vanishes identically.
The nonreal chart used to clear actual denominators excludes this case. -/
theorem real_shift_zero (j : ℕ) :
    microscopic (-(j : ℂ)) (FormalGauge.shiftedMeridian j) = 0 := by
  rw [microscopic_shiftedMeridian]
  simp [FormalExp.exponential_zero]

end VolumeLogic.MeridianExpansionControls

#print axioms VolumeLogic.MeridianExpansionControls.linear_shift_retained
#print axioms VolumeLogic.MeridianExpansionControls.even_coefficient_vanishes
#print axioms VolumeLogic.MeridianExpansionControls.cubic_coefficient_retained
#print axioms VolumeLogic.MeridianExpansionControls.real_shift_zero
