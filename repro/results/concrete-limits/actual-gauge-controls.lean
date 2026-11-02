import ActualGauge

open VolumeLogic.ActualGauge
namespace VolumeLogic.ActualGaugeControls

-- The zeroth coefficient retains D even when the unshifted meridian is zero.
theorem zeroth_coefficient_retains_denominator : clearedCoefficient 2 (fun _ => (1 : ℂ))
    (fun j => if j = 0 then 0 else if j = 1 then 2 else 3) 0 = 6 := by
  norm_num [clearedCoefficient, denominator, Finset.prod_Icc_succ_top]

-- At a positive shift the odd parity sign cannot be omitted.
theorem odd_shift_retains_sign : clearedCoefficient 1 (fun _ => (5 : ℂ))
    (fun j => if j = 0 then 2 else 3) 1 = -10 := by
  norm_num [clearedCoefficient, punctured]

-- A zero common H factor makes the original recurrence tautological while
-- the constructed normalized equation can still be nonzero.
theorem zero_normalization_cannot_cancel : (∑ j ∈ Finset.range 2, (if j = 0 then (1 : ℂ) else 0) * (0 : ℂ)) = 0 ∧
    (∑ j ∈ Finset.range 2,
      clearedCoefficient 1 (fun j => if j = 0 then (1 : ℂ) else 0)
        (fun _ => (1 : ℂ)) j * ((1 : ℂ) / 1)) ≠ 0 := by
  norm_num [clearedCoefficient, denominator, punctured, Finset.sum_range_succ]

-- The literal quotient has no assigned removable value at s=0. The
-- nonreal-chart theorem cannot be silently applied at the complete point.
theorem literal_quotient_is_not_removable_value : sineNormalization 3 0 = 0 ∧ sineNormalization 3 0 ≠ 1 := by
  norm_num [sineNormalization]


end VolumeLogic.ActualGaugeControls

#print axioms VolumeLogic.ActualGaugeControls.zeroth_coefficient_retains_denominator
#print axioms VolumeLogic.ActualGaugeControls.odd_shift_retains_sign
#print axioms VolumeLogic.ActualGaugeControls.zero_normalization_cannot_cancel
#print axioms VolumeLogic.ActualGaugeControls.literal_quotient_is_not_removable_value
