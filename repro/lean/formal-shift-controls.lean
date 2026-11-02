import FormalShift

open PowerSeries MvPowerSeries
open VolumeLogic.FormalShift
namespace VolumeLogic.FormalShiftControls

/-- The shift factor j is necessary: S=u^2 and j=2 give 4u, not 2u. -/
theorem shift_factor_required :
    atHZero (logarithmicShift (PowerSeries.X ^ 2 : PowerSeries ℚ) 0 2) ≠
      PowerSeries.derivative ℚ (PowerSeries.X ^ 2) := by
  intro h
  have hc := congrArg (PowerSeries.coeff 1) h
  rw [logarithmicShift_atHZero] at hc
  norm_num [PowerSeries.coeff_derivative, PowerSeries.coeff_X_pow, map_ofNat] at hc

/-- A negative shift has its signed derivative, without an absolute value. -/
theorem negative_shift :
    PowerSeries.coeff 1
      (atHZero (logarithmicShift (PowerSeries.X ^ 2 : PowerSeries ℚ) 0 (-2))) = -4 := by
  rw [logarithmicShift_atHZero]
  norm_num [PowerSeries.coeff_derivative, PowerSeries.coeff_X_pow, map_ofNat]

/-- Even S(0)=S'(0)=0 does not make S/h regular. Subtracting the shifted
and unshifted actions before division is indispensable. -/
theorem principal_pole_required : ¬ ∃ F : MvPowerSeries (Fin 2) ℚ,
    MvPowerSeries.X 0 * F = MvPowerSeries.X 1 ^ 2 := by
  rintro ⟨F, h⟩
  have hc := congrArg (MvPowerSeries.coeff (index 0 2)) h
  have hn : ¬ Finsupp.single (0 : Fin 2) 1 ≤ index 0 2 := by
    intro hh
    have := hh 0
    norm_num [index] at this
  rw [MvPowerSeries.X, MvPowerSeries.coeff_monomial_mul, if_neg hn] at hc
  norm_num [MvPowerSeries.coeff_X_pow, index] at hc

/-- If S has a linear term, the logarithmic shift has nonzero constant term. -/
theorem origin_condition_required :
    MvPowerSeries.constantCoeff
      (logarithmicShift (PowerSeries.X : PowerSeries ℚ) 0 1) = 1 := by
  have h := congrArg (PowerSeries.coeff 0)
    (logarithmicShift_atHZero (PowerSeries.X : PowerSeries ℚ) 0 1)
  simpa [atHZero, bc, index, PowerSeries.coeff_derivative,
    MvPowerSeries.coeff_zero_eq_constantCoeff] using h

/-- Regular amplitudes disappear only from the h^0 coefficient, not from
higher orders: shifting A=u by 2 adds 2h. -/
theorem regular_shift_retained :
    bc (shiftRegular (MvPowerSeries.X 1 : MvPowerSeries (Fin 2) ℚ) 2 -
      MvPowerSeries.X 1) 1 0 = 2 := by
  rw [shiftRegular, MvPowerSeries.subst_X (shiftVariables_hasSubst 2)]
  simp [shiftVariables, shiftArgument, bc, index, MvPowerSeries.coeff_X]

end VolumeLogic.FormalShiftControls
#print axioms VolumeLogic.FormalShiftControls.shift_factor_required
#print axioms VolumeLogic.FormalShiftControls.negative_shift
#print axioms VolumeLogic.FormalShiftControls.principal_pole_required
#print axioms VolumeLogic.FormalShiftControls.origin_condition_required
#print axioms VolumeLogic.FormalShiftControls.regular_shift_retained
