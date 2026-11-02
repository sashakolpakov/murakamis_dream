import FormalExp
import Mathlib.Tactic.NormNum

open PowerSeries MvPowerSeries
open VolumeLogic.FormalShift VolumeLogic.FormalExp
namespace VolumeLogic.FormalExpControls

/-- The projected argument need not vanish as a whole u-series. -/
theorem retained_u_exponential :
    atHZero (exponential (MvPowerSeries.X 1 : MvPowerSeries (Fin 2) ℚ)) =
      PowerSeries.exp ℚ := by
  rw [atHZero_exponential _ (by simp), atHZero_eq_subst,
    MvPowerSeries.subst_X zeroVariables_hasSubst]
  change exponential (PowerSeries.X : PowerSeries ℚ) = _
  simp [exponential]

/-- A nonzero logarithmic series supported in positive h degree contributes
exactly one to the projected factor, but its full exponential is not one. -/
theorem h_exponential_projection :
    atHZero (exponential (MvPowerSeries.X 0 : MvPowerSeries (Fin 2) ℚ)) = 1 := by
  rw [atHZero_exponential _ (by simp), atHZero_eq_subst,
    MvPowerSeries.subst_X zeroVariables_hasSubst]
  exact exponential_zero

theorem h_exponential_nonconstant :
    bc (exponential (MvPowerSeries.X 0 : MvPowerSeries (Fin 2) ℚ)) 1 0 = 1 := by
  rw [bc, exponential, PowerSeries.coeff_subst_single]
  simp [index, PowerSeries.coeff_exp]

/-- Negative shifts cannot be replaced by their absolute values. -/
theorem negative_linear_coefficient :
    PowerSeries.coeff 1 (exponential ((-2 : ℚ) • (PowerSeries.X : PowerSeries ℚ))) = -2 := by
  rw [exponential_linear_coeff]
  norm_num

/-- Exponentiation is not just the constant-plus-linear truncation. -/
theorem quadratic_coefficient_retained :
    PowerSeries.coeff 2 (exponential ((2 : ℚ) • (PowerSeries.X : PowerSeries ℚ))) = 2 := by
  rw [exponential_linear_coeff]
  norm_num

/-- A nonzero scalar constant does not satisfy the formal substitution
condition over Q; no value of an inadmissible composition is interpreted. -/
theorem nonzero_origin_inadmissible :
    ¬ PowerSeries.HasSubst (1 : MvPowerSeries (Fin 2) ℚ) := by
  simp [PowerSeries.HasSubst]

/-- The full logarithmic shift with a linear principal action really hits
that excluded boundary. -/
theorem linear_action_inadmissible :
    ¬ PowerSeries.HasSubst
      (logarithmicShift (PowerSeries.X : PowerSeries ℚ) 0 1) := by
  have h := congrArg (PowerSeries.coeff 0)
    (logarithmicShift_atHZero (PowerSeries.X : PowerSeries ℚ) 0 1)
  have hc : MvPowerSeries.constantCoeff
      (logarithmicShift (PowerSeries.X : PowerSeries ℚ) 0 1) = 1 := by
    simpa [atHZero, bc, index, PowerSeries.coeff_derivative,
      MvPowerSeries.coeff_zero_eq_constantCoeff] using h
  simp [PowerSeries.HasSubst, hc]

end VolumeLogic.FormalExpControls
#print axioms VolumeLogic.FormalExpControls.retained_u_exponential
#print axioms VolumeLogic.FormalExpControls.h_exponential_projection
#print axioms VolumeLogic.FormalExpControls.h_exponential_nonconstant
#print axioms VolumeLogic.FormalExpControls.negative_linear_coefficient
#print axioms VolumeLogic.FormalExpControls.quadratic_coefficient_retained
#print axioms VolumeLogic.FormalExpControls.nonzero_origin_inadmissible
#print axioms VolumeLogic.FormalExpControls.linear_action_inadmissible
