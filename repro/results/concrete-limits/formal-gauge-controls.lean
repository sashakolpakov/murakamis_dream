import FormalGauge
import Mathlib.Tactic.NormNum

namespace VolumeLogic.FormalGaugeControls
open PowerSeries MvPowerSeries
open FormalShift FormalExp FormalGauge

/-- An order-zero operator acquires no spurious meridian factor. -/
theorem zero_order (a : ℕ → MvPowerSeries (Fin 2) ℚ) :
    clearedCoefficient 0 a 0 = a 0 := by
  simp [clearedCoefficient, denominator]

/-- At order two the positive shift removes its own denominator only. -/
theorem first_shift_replacement :
    clearedCoefficient 2 (fun _ => (1 : MvPowerSeries (Fin 2) ℚ)) 1 =
      -shiftedMeridian 0 * shiftedMeridian 2 := by
  have hi : Finset.Icc 1 2 = ({1,2} : Finset ℕ) := by decide
  simp [clearedCoefficient, punctured, hi]

/-- The first shift has the negative first-order meridian coefficient. -/
theorem first_shift_signed_linear :
    PowerSeries.coeff 1
      (hZeroHom (clearedCoefficient 1 (fun _ => (1 : MvPowerSeries (Fin 2) ℚ)) 1)) = -2 := by
  rw [project_clearedCoefficient 1 _ 1 le_rfl]
  have hp := exponential_linear_coeff (R := ℚ) 1 1
  have hn := exponential_linear_coeff (R := ℚ) (-1) 1
  simp only [one_smul] at hp
  simp only [neg_one_smul] at hn
  norm_num [meridian, hp, hn]

/-- Clearing is valid although none of the formal shifted denominators is a unit. -/
theorem shifted_denominator_not_unit (j : ℕ) :
    ¬ IsUnit (shiftedMeridian (R := ℚ) j) := by
  rw [MvPowerSeries.isUnit_iff_constantCoeff, shiftedMeridian_constant]
  simp

/-- The normalization theorem cannot be extended to indices beyond the order. -/
theorem outside_order_fails :
    hZeroHom (clearedCoefficient 0 (fun _ => (1 : MvPowerSeries (Fin 2) ℚ)) 1) ≠
      meridian ^ 0 * ((-1)^1 * hZeroHom (1 : MvPowerSeries (Fin 2) ℚ)) := by
  intro h
  have hc := congrArg PowerSeries.constantCoeff h
  simp [clearedCoefficient, punctured, project_shiftedMeridian,
    meridian_constant] at hc

end VolumeLogic.FormalGaugeControls
#print axioms VolumeLogic.FormalGaugeControls.zero_order
#print axioms VolumeLogic.FormalGaugeControls.first_shift_replacement
#print axioms VolumeLogic.FormalGaugeControls.first_shift_signed_linear
#print axioms VolumeLogic.FormalGaugeControls.shifted_denominator_not_unit
#print axioms VolumeLogic.FormalGaugeControls.outside_order_fails
