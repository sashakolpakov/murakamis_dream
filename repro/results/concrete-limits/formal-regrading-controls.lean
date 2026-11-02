import FormalRegradingRing

namespace VolumeLogic.RegradingControls
open PowerSeries MvPowerSeries FormalShift FormalRegradingRing

/-- The h factor in the image of u cannot be discarded. -/
theorem omitted_h_factor :
    regrading (MvPowerSeries.X 1 : MvPowerSeries (Fin 2) ℚ) ≠
      PowerSeries.C Polynomial.X := by
  intro he
  have hc := congrArg
    (fun F : PowerSeries (Polynomial ℚ) => Polynomial.coeff (PowerSeries.coeff 0 F) 1) he
  rw [regrading_coeff] at hc
  norm_num at hc

/-- Every fixed finite jet misses a nonzero actual formal series. -/
theorem finite_jet_misses_term (L : ℕ) :
    (∀ n, n ≤ L → PowerSeries.coeff n
      (regrading (MvPowerSeries.X 0 ^ (L+1) : MvPowerSeries (Fin 2) ℚ)) = 0) ∧
    (MvPowerSeries.X 0 ^ (L+1) : MvPowerSeries (Fin 2) ℚ) ≠ 0 := by
  constructor
  · intro n hn
    rw [map_pow, regrading_h, PowerSeries.coeff_X_pow, if_neg (by omega)]
  · intro he
    have hc := congrArg (MvPowerSeries.coeff (Finsupp.single 0 (L+1))) he
    norm_num [MvPowerSeries.coeff_X_pow] at hc

/-- Specializing s to a single value destroys injectivity, even at all h orders. -/
theorem fixed_s_loses_information :
    (MvPowerSeries.X 1 - MvPowerSeries.X 0 : MvPowerSeries (Fin 2) ℚ) ≠ 0 ∧
    PowerSeries.map (Polynomial.evalRingHom (1 : ℚ))
      (regrading (MvPowerSeries.X 1 - MvPowerSeries.X 0 : MvPowerSeries (Fin 2) ℚ)) = 0 := by
  constructor
  · intro he
    have hc := congrArg (MvPowerSeries.coeff (index 0 1)) he
    have hi : Finsupp.single (1 : Fin 2) (1 : ℕ) ≠ Finsupp.single (0 : Fin 2) 1 := by
      intro hs
      have hv := congrArg (fun f : Fin 2 →₀ ℕ => f 1) hs
      norm_num at hv
    norm_num [MvPowerSeries.coeff_X, index, hi] at hc
  · rw [map_sub, regrading_u, regrading_h, map_sub, map_mul]
    simp

end VolumeLogic.RegradingControls
#print axioms VolumeLogic.RegradingControls.omitted_h_factor
#print axioms VolumeLogic.RegradingControls.finite_jet_misses_term
#print axioms VolumeLogic.RegradingControls.fixed_s_loses_information
