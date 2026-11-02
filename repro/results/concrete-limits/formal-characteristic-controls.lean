import FormalCharacteristic

noncomputable section
namespace VolumeLogic.FormalCharacteristicControls
open VolumeLogic.FormalCharacteristic VolumeLogic.FormalExp VolumeLogic.FormalShift

/-- The divisor vanishes at the complete meridian, although it is not the
zero series. Cancellation uses a domain, not invertibility at the origin. -/
theorem meridian_divisor_not_unit : ¬ IsUnit meridianDivisor := by
  intro h
  have hc := MvPowerSeries.isUnit_iff_constantCoeff.mp h
  have hx : MvPowerSeries.constantCoeff (PowerSeries.X : PowerSeries ℂ) = 0 := by
    change PowerSeries.constantCoeff (PowerSeries.X : PowerSeries ℂ) = 0
    simp
  have hnx : MvPowerSeries.constantCoeff (-PowerSeries.X : PowerSeries ℂ) = 0 := by
    rw [map_neg, hx, neg_zero]
  have hz : MvPowerSeries.constantCoeff meridianDivisor = 0 := by
    rw [meridianDivisor, map_sub, exponential_constant _ hx, exponential_constant _ hnx]
    simp
  rw [hz] at hc
  exact not_isUnit_zero hc

private theorem logarithmic_zero (j : ℂ) :
    logarithmicShift (0 : PowerSeries ℂ) 0 j = 0 := by
  have hp (k : ℂ) : PowerSeries.subst (shiftArgument k) (0 : PowerSeries ℂ) = 0 := by
    rw [← PowerSeries.coe_substAlgHom (argument_hasSubst k), map_zero]
  have ha : MvPowerSeries.subst (shiftVariables j) (0 : MvPowerSeries (Fin 2) ℂ) = 0 := by
    rw [← MvPowerSeries.coe_substAlgHom (shiftVariables_hasSubst j), map_zero]
  have hd : divideH (0 : MvPowerSeries (Fin 2) ℂ) = 0 := by
    ext e
    rfl
  simp only [logarithmicShift, principalDifference, shiftPrincipal, shiftRegular,
    hp, ha, sub_self, hd, add_zero]

/-- A two-term cleared equation can vanish while its unsigned classical
polynomial at +1 is nonzero. The inherited minus sign is necessary. -/
theorem negative_classical_argument_required :
    shiftedEquation 1
      (fun j => if j = 0 then MvPowerSeries.X 1 else -MvPowerSeries.X 1)
      (0 : PowerSeries ℂ) 0 = 0 ∧
    (classicalPolynomial 1 (fun _ => (1 : PowerSeries ℂ))).eval (-1) = 0 ∧
    (classicalPolynomial 1 (fun _ => (1 : PowerSeries ℂ))).eval 1 ≠ 0 := by
  constructor
  · simp [shiftedEquation, Finset.sum_range_succ, logarithmic_zero, exponential_zero]
  constructor
  · simp [classicalPolynomial, Finset.sum_range_succ]
  · intro he
    have hc := congrArg (PowerSeries.coeff 0) he
    norm_num [classicalPolynomial, Finset.sum_range_succ, map_ofNat] at hc

end VolumeLogic.FormalCharacteristicControls
#print axioms VolumeLogic.FormalCharacteristicControls.meridian_divisor_not_unit
#print axioms VolumeLogic.FormalCharacteristicControls.negative_classical_argument_required
