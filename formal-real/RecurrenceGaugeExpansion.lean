import RecurrenceExpansion
import ActualGauge

noncomputable section
open Filter Asymptotics
open scoped Topology
namespace VolumeLogic.RecurrenceExpansion

variable {ι : Type*} {l : Filter ι} {h : ι → ℂ}

/-- The asymptotic series of the cleared coefficient is derived from the
original coefficient and every retained meridian factor. The j=0 branch is
included; no factor is assumed to be a unit. -/
theorem clearedCoefficient_expansion (r : ℕ)
    (a f : ℕ → ι → ℂ) (P Q : ℕ → PowerSeries ℂ)
    (ht : Tendsto h l (𝓝 0))
    (ha : ∀ j ≤ r, HasExpansion l h (a j) (P j))
    (hf : ∀ j ≤ r, HasExpansion l h (f j) (Q j))
    (j : ℕ) (hj : j ≤ r) :
    HasExpansion l h
      (fun n => ActualGauge.clearedCoefficient r (fun k => a k n) (fun k => f k n) j)
      (ActualGauge.clearedCoefficient r P Q j) := by
  classical
  by_cases hj0 : j = 0
  · subst j
    have hp := HasExpansion.prod (Finset.Icc 1 r)
      (fun k hk => hf k (Finset.mem_Icc.mp hk).2) ht
    simpa [ActualGauge.clearedCoefficient, ActualGauge.denominator]
      using hp.mul (ha 0 (Nat.zero_le r)) ht
  · have hp := HasExpansion.prod ((Finset.Icc 1 r).erase j)
      (fun k hk => hf k (Finset.mem_Icc.mp (Finset.mem_of_mem_erase hk)).2) ht
    have hc := (((hasExpansion_const (l := l) (h := h) ((-1 : ℂ)^j)).mul
      (hf 0 (Nat.zero_le r)) ht).mul hp ht).mul (ha j hj) ht
    simpa [ActualGauge.clearedCoefficient, hj0, ActualGauge.punctured] using hc

/-- Constructing the scalar gauge and taking its expansion commute. This
removes any hypothesis about the expansion of an already-cleared family. -/
theorem characteristic_of_original_coefficient_expansions [NeBot l]
    (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (c f v : ℂ → ℕ → ι → ℂ) {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1),
        ActualGauge.clearedCoefficient r (fun k => c s k n) (fun k => f s k n) j *
          v s j n = 0)
    (hc : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (c s j) (microscopic s (a j)))
    (hf : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (f s j)
      (microscopic s (FormalGauge.shiftedMeridian j)))
    (hv : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (v s j)
      (microscopic s (FormalExp.exponential (FormalShift.logarithmicShift S A (j : ℂ))))) :
    (FormalCharacteristic.classicalPolynomial r (fun j => FormalShift.atHZero (a j))).eval
      (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  apply characteristic_of_factor_expansions r a S A hS
    (fun s j n => ActualGauge.clearedCoefficient r (fun k => c s k n) (fun k => f s k n) j)
    v hD ht hn hz ?_ hv
  intro s hs j hj
  have hh := clearedCoefficient_expansion r (c s) (f s)
    (fun k => microscopic s (a k))
    (fun k => microscopic s (FormalGauge.shiftedMeridian k))
    ht (hc s hs) (hf s hs) j hj
  rw [ActualGauge.formal_coefficient_eq, ActualGauge.map_clearedCoefficient]
  exact hh

/-- Starting with the actual finite recurrence, derive its cleared equation,
then its all-order expansion and classical identity. The analytic estimates
are separate per original coefficient, meridian factor and shift ratio. -/
theorem characteristic_of_actual_recurrence [NeBot l]
    (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (c f F H Z : ℂ → ℕ → ι → ℂ) (scale : ℂ → ι → ℂ)
    {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hs : ∀ s ∈ D, ∀ᶠ n in l, scale s n ≠ 0)
    (hH : ∀ s ∈ D, ∀ᶠ n in l, H s 0 n ≠ 0)
    (hZ : ∀ s ∈ D, ∀ᶠ n in l, Z s 0 n ≠ 0)
    (hfne : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j, 1 ≤ j → j ≤ r → f s j n ≠ 0)
    (hg : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j, 1 ≤ j → j ≤ r → H s j n * f s j n = (-1)^j * H s 0 n * f s 0 n)
    (hF : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j ≤ r, F s j n = scale s n * H s j n * Z s j n)
    (he : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1), c s j n * F s j n = 0)
    (hc : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (c s j) (microscopic s (a j)))
    (hf : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (f s j)
      (microscopic s (FormalGauge.shiftedMeridian j)))
    (hv : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (fun n => Z s j n / Z s 0 n)
      (microscopic s (FormalExp.exponential (FormalShift.logarithmicShift S A (j : ℂ))))) :
    (FormalCharacteristic.classicalPolynomial r (fun j => FormalShift.atHZero (a j))).eval
      (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  apply characteristic_of_original_coefficient_expansions r a S A hS c f
    (fun s j n => Z s j n / Z s 0 n) hD ht hn ?_ hc hf hv
  intro s hsd
  filter_upwards [hs s hsd, hH s hsd, hZ s hsd, hfne s hsd,
    hg s hsd, hF s hsd, he s hsd] with n hsn hHn hZn hfnen hgn hFn hen
  exact ActualGauge.cleared_equation_of_recurrence r
    (fun j => c s j n) (fun j => f s j n) (fun j => F s j n)
    (fun j => H s j n) (fun j => Z s j n) (scale s n)
    hsn hHn hZn hfnen hgn hFn hen

/-- For the literal sine normalization on a nonreal parameter set, its exact
integer-shift gauge and all shifted denominator exclusions are already proved.
Only the analytic coefficient/factor/ratio expansions remain hypotheses. -/
theorem characteristic_of_sine_recurrence [NeBot l]
    (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (N : ι → ℕ) (c F Z : ℂ → ℕ → ι → ℂ) (scale : ℂ → ι → ℂ)
    {D : Set ℂ} (hD : D.Infinite) (hDnr : ∀ s ∈ D, s.im ≠ 0)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hN : ∀ᶠ n in l, (N n : ℂ) ≠ 0)
    (hs : ∀ s ∈ D, ∀ᶠ n in l, scale s n ≠ 0)
    (hZ : ∀ s ∈ D, ∀ᶠ n in l, Z s 0 n ≠ 0)
    (hF : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j ≤ r, F s j n = scale s n * ActualGauge.sineNormalization (N n) (s+j) * Z s j n)
    (he : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1), c s j n * F s j n = 0)
    (hc : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (c s j) (microscopic s (a j)))
    (hf : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h
      (fun n => ActualGauge.sineMeridian (N n) s j)
      (microscopic s (FormalGauge.shiftedMeridian j)))
    (hv : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l h (fun n => Z s j n / Z s 0 n)
      (microscopic s (FormalExp.exponential (FormalShift.logarithmicShift S A (j : ℂ))))) :
    (FormalCharacteristic.classicalPolynomial r (fun j => FormalShift.atHZero (a j))).eval
      (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  apply characteristic_of_original_coefficient_expansions r a S A hS c
    (fun s j n => ActualGauge.sineMeridian (N n) s j)
    (fun s j n => Z s j n / Z s 0 n) hD ht hn ?_ hc hf hv
  intro s hsd
  filter_upwards [hN, hs s hsd, hZ s hsd, hF s hsd, he s hsd]
    with n hNn hsn hZn hFn hen
  exact ActualGauge.sine_cleared_equation (N n) r s
    (fun j => c s j n) (fun j => F s j n) (fun j => Z s j n)
    (scale s n) hNn (hDnr s hsd) hsn hZn hFn hen

end VolumeLogic.RecurrenceExpansion
