import UniformProfile

namespace VolumeLogic.UniformProfile.Controls
open Filter
open scoped Topology

/-- Pointwise convergence at each parameter does not give the shared
threshold required by the theorem. -/
theorem spikes_pointwise (s : ℕ) :
    Tendsto (fun N : ℕ => if N=s then (-1 : ℂ) else 0) atTop (𝓝 0) := by
  apply tendsto_const_nhds.congr'
  filter_upwards [eventually_gt_atTop s] with N hN
  simp [ne_of_gt hN]

theorem spikes_destroy_common_nonvanishing :
    ¬ (∀ᶠ N in atTop, ∀ s : ℕ,
      (1 : ℂ)+(if N=s then (-1 : ℂ) else 0) ≠ 0) := by
  intro h
  obtain ⟨N,hN⟩ := eventually_atTop.mp h
  have hn := hN N le_rfl N
  simp at hn

theorem inverse_locations_injective : Function.Injective
    (fun N : ℕ => (1 : ℝ)/((N : ℝ)+1)) := by
  intro i j hij
  simp only [one_div,inv_inj] at hij
  exact Nat.cast_injective (add_right_cancel hij)

/-- The failure of pointwise convergence persists on the actual compact
real interval [0,1], not merely on an unbounded parameter space. -/
theorem compact_spikes_pointwise (s : ℝ) :
    Tendsto (fun N : ℕ => if (1 : ℝ)/((N : ℝ)+1)=s then (-1 : ℂ) else 0)
      atTop (𝓝 0) := by
  by_cases he : ∃ k : ℕ, (1 : ℝ)/((k : ℝ)+1)=s
  · obtain ⟨k,hk⟩ := he
    apply tendsto_const_nhds.congr'
    filter_upwards [eventually_gt_atTop k] with N hN
    have hne : (1 : ℝ)/((N : ℝ)+1) ≠ s := by
      intro h
      have := inverse_locations_injective (h.trans hk.symm)
      omega
    simp only [if_neg hne]
  · have hne : ∀ N : ℕ, (1 : ℝ)/((N : ℝ)+1) ≠ s := by simpa using he
    simpa only [if_neg (hne _)] using
      (tendsto_const_nhds : Tendsto (fun _ : ℕ => (0 : ℂ)) atTop (𝓝 0))

theorem compact_spikes_have_zero_every_level (N : ℕ) :
    ∃ s ∈ Set.Icc (0 : ℝ) 1,
      (1 : ℂ)+(if (1 : ℝ)/((N : ℝ)+1)=s then (-1 : ℂ) else 0) = 0 := by
  refine ⟨1/((N : ℝ)+1),⟨by positivity,?_⟩,by simp⟩
  apply (div_le_one (by positivity)).mpr
  have : (0 : ℝ) ≤ (N : ℝ) := Nat.cast_nonneg N
  linarith

/-- The error threshold cannot be enlarged to include error -1. -/
theorem relative_error_one_can_cancel :
    ‖(-1 : ℂ)‖ = 1 ∧ (1 : ℂ)*(1 : ℂ)*(1+(-1)) = 0 := by norm_num

/-- With no positive factor bound a nonzero base and zero relative error
can still produce an identically zero family. -/
theorem zero_factor_can_cancel :
    (1 : ℂ) ≠ 0 ∧ ‖(0 : ℂ)‖ = 0 ∧ (0 : ℂ)*1*(1+0) = 0 := by norm_num

/-- Uncontrolled exponential growth of the factor changes the rate.
Actual complex exponential and real logarithm are used. -/
theorem unbounded_factor_changes_rate (N : ℕ) (hN : 0 < N) :
    Real.log ‖Complex.exp (N : ℂ)‖/(N : ℝ) = 1 := by
  simp only [Complex.norm_exp, Complex.natCast_re, Real.log_exp]
  exact div_self (Nat.cast_ne_zero.mpr (Nat.ne_of_gt hN))

end VolumeLogic.UniformProfile.Controls

#print axioms VolumeLogic.UniformProfile.Controls.spikes_pointwise
#print axioms VolumeLogic.UniformProfile.Controls.spikes_destroy_common_nonvanishing
#print axioms VolumeLogic.UniformProfile.Controls.inverse_locations_injective
#print axioms VolumeLogic.UniformProfile.Controls.compact_spikes_pointwise
#print axioms VolumeLogic.UniformProfile.Controls.compact_spikes_have_zero_every_level
#print axioms VolumeLogic.UniformProfile.Controls.relative_error_one_can_cancel
#print axioms VolumeLogic.UniformProfile.Controls.zero_factor_can_cancel
#print axioms VolumeLogic.UniformProfile.Controls.unbounded_factor_changes_rate
