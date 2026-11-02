import SineFactor

noncomputable section
open Filter
open scoped Topology
namespace VolumeLogic.SineFactorControls
open SineFactor

/-- The removable value is one, whereas the unextended literal quotient
uses division by zero at the origin. They must not be interchanged there. -/
theorem origin_requires_removal (N : ℕ) :
    factor N 0 = 1 ∧ ActualGauge.sineNormalization N 0 = 0 := by
  simp [ActualGauge.sineNormalization]

/-- The limiting zero set excludes every nonzero integer, not the origin. -/
theorem nonzero_integer_limit (k : ℤ) (hk : k ≠ 0) :
    limitingFactor (k : ℂ) = 0 :=
  (limiting_zero_iff (k : ℂ)).mpr ⟨k,hk,rfl⟩

/-- Already on the genuine denominator chart at N=2, the boundary s=1
has a zero factor. The strict R<1 disk condition has mathematical content. -/
theorem boundary_one_is_zero : factor 2 1 = 0 := by
  rw [factor_eq_literal 2 1 (by norm_num) (by norm_num)]
  norm_num [ActualGauge.sineNormalization]

/-- Uniform convergence on the closed unit disk does not give a positive
uniform lower bound: the actual numerator zero at s=1 persists. -/
theorem no_positive_unit_disk_bound :
    ¬ ∃ c : ℝ, 0 < c ∧ ∀ᶠ N : ℕ in atTop,
      ∀ s ∈ Metric.closedBall (0 : ℂ) 1, c ≤ ‖factor N s‖ := by
  rintro ⟨c,hc,hbound⟩
  obtain ⟨N,hN⟩ := hbound.exists
  have h := hN 1 (by simp [Metric.mem_closedBall, dist_zero_right])
  have hz : limitingFactor 1 = 0 := by
    simpa using nonzero_integer_limit 1 (by norm_num)
  simp [factor,hz] at h
  linarith

/-- The fixed diagram scalar need not have unit modulus at a complex
parameter, even though its coefficient is purely imaginary. -/
theorem complex_phase_not_unit_modulus :
    ‖quadraticPhase ((Real.pi : ℂ)*Complex.I) 1 (1+Complex.I)‖ =
        Real.exp (-2*Real.pi) ∧
    ‖quadraticPhase ((Real.pi : ℂ)*Complex.I) 1 (1+Complex.I)‖ ≠ 1 := by
  have hsq : ((1 : ℂ)+Complex.I)^2 = 2*Complex.I := by
    calc
      _ = 1 + 2*Complex.I + Complex.I^2 := by ring
      _ = _ := by rw [Complex.I_sq]; ring
  have he : quadraticPhase ((Real.pi : ℂ)*Complex.I) 1 (1+Complex.I) =
      Complex.exp ((-2 : ℂ)*Real.pi) := by
    unfold quadraticPhase
    rw [hsq]
    congr 1
    calc
      _ = (2*(Real.pi : ℂ))*(Complex.I*Complex.I) := by ring
      _ = _ := by rw [Complex.I_mul_I]; ring
  rw [he, Complex.norm_exp]
  norm_num

end VolumeLogic.SineFactorControls

#print axioms VolumeLogic.SineFactorControls.origin_requires_removal
#print axioms VolumeLogic.SineFactorControls.nonzero_integer_limit
#print axioms VolumeLogic.SineFactorControls.boundary_one_is_zero
#print axioms VolumeLogic.SineFactorControls.no_positive_unit_disk_bound

#print axioms VolumeLogic.SineFactorControls.complex_phase_not_unit_modulus
