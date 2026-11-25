import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
The reference's final scalar implication, using actual complex norms,
real logarithms and ordinary all-integer limits.

A nonnegative upper rate is expressed by eventual exponential bounds.
It allows zeros and does not use Real.log's totalized value at zero.
The packet theorem proves eventual nonvanishing before taking its logarithmic
limit. Its hypotheses retain the finite action S_N and bound the entire
remainder of the same exact scalar. No source estimate, Gaussian coefficient,
Fourier contour or geometric calibration is asserted without a hypothesis.
-/

namespace VolumeLogic.RealModel
open Filter

/-- Upper exponential rate for an eventually nonnegative real sequence.
Zero values are allowed at arbitrarily many levels. -/
def UpperRate (B : ℕ → ℝ) (b : ℝ) : Prop :=
  (∀ᶠ N in atTop, 0 ≤ B N) ∧
    ∀ ε > 0, ∀ᶠ N in atTop, B N ≤ Real.exp ((N : ℝ) * (b + ε))

/-- Multiplying nonnegative budgets adds their upper rates, including zeros. -/
theorem UpperRate.mul {B C : ℕ → ℝ} {b c : ℝ}
    (hB : UpperRate B b) (hC : UpperRate C c) :
    UpperRate (fun N => B N * C N) (b + c) := by
  constructor
  · filter_upwards [hB.1, hC.1] with N hBN hCN
    exact mul_nonneg hBN hCN
  · intro ε hε
    filter_upwards [hB.2 (ε / 2) (by linarith),
      hC.2 (ε / 2) (by linarith), hC.1] with N hBN hCN hCpos
    calc
      B N * C N ≤ Real.exp ((N : ℝ) * (b + ε / 2)) *
          Real.exp ((N : ℝ) * (c + ε / 2)) :=
        mul_le_mul hBN hCN hCpos (Real.exp_nonneg _)
      _ = Real.exp ((N : ℝ) * (b + c + ε)) := by
        rw [← Real.exp_add]
        congr 1
        ring

/-- The actual filled remainder inherits a source bound after a
subexponential nonnegative cost. Neither budget is divided out. -/
theorem upperRate_norm_of_cost {E : ℕ → ℂ} {B C : ℕ → ℝ} {b : ℝ}
    (hB : UpperRate B b) (hC : UpperRate C 0)
    (bound : ∀ᶠ N in atTop, ‖E N‖ ≤ C N * B N) :
    UpperRate (fun N => ‖E N‖) b := by
  refine ⟨Eventually.of_forall (fun N => norm_nonneg _), ?_⟩
  intro ε hε
  have hprod := hC.mul hB
  filter_upwards [bound, hprod.2 ε hε] with N hN hprodN
  exact hN.trans (by simpa only [zero_add] using hprodN)

private theorem inv_nat_tendsto :
    Tendsto (fun N : ℕ => (N : ℝ)⁻¹) atTop (nhds 0) :=
  tendsto_inv_atTop_zero.comp tendsto_natCast_atTop_atTop

private theorem log_nat_div_tendsto :
    Tendsto (fun N : ℕ => Real.log (N : ℝ) / (N : ℝ)) atTop (nhds 0) := by
  have h : Tendsto (fun x : ℝ => Real.log x / x) atTop (nhds 0) := by
    simpa using Real.tendsto_pow_log_div_mul_add_atTop 1 0 1 one_ne_zero
  exact h.comp tendsto_natCast_atTop_atTop

/-- Any fixed real-power cost has upper rate zero. The exponent may be
negative and the prefactor may vanish. -/
theorem upperRate_of_polynomial_bound {C : ℕ → ℝ} {C₀ m : ℝ}
    (hC₀ : 0 ≤ C₀)
    (bound : ∀ᶠ N in atTop, 0 ≤ C N ∧ C N ≤ C₀ * (N : ℝ) ^ m) :
    UpperRate C 0 := by
  refine ⟨bound.mono fun _ h => h.1, ?_⟩
  intro ε hε
  by_cases hz : C₀ = 0
  · filter_upwards [bound] with N hN
    have hzero : C N ≤ 0 := by simpa [hz] using hN.2
    exact hzero.trans (Real.exp_nonneg _)
  · have hpos : 0 < C₀ := lt_of_le_of_ne hC₀ (Ne.symm hz)
    have hlim : Tendsto
        (fun N : ℕ => Real.log C₀ / (N : ℝ) +
          m * (Real.log (N : ℝ) / (N : ℝ))) atTop (nhds 0) := by
      simpa [div_eq_mul_inv] using
        (tendsto_const_nhds.mul inv_nat_tendsto).add
          (log_nat_div_tendsto.const_mul m)
    have hsmall := hlim.eventually (eventually_lt_nhds hε)
    filter_upwards [bound, hsmall, eventually_ge_atTop (1 : ℕ)] with N hN hs hNpos
    have hn : (0 : ℝ) < (N : ℝ) := Nat.cast_pos.mpr (by omega)
    have hp : 0 < C₀ * (N : ℝ) ^ m :=
      mul_pos hpos (Real.rpow_pos_of_pos hn _)
    apply hN.2.trans
    apply (Real.log_le_iff_le_exp hp).mp
    rw [Real.log_mul hz (ne_of_gt (Real.rpow_pos_of_pos hn _)),
      Real.log_rpow hn]
    have : Real.log C₀ + m * Real.log (N : ℝ) < (N : ℝ) * ε := by
      have hd := (div_lt_iff₀ hn).mp (show
          (Real.log C₀ + m * Real.log (N : ℝ)) / (N : ℝ) < ε by
        simpa [add_div, mul_div_assoc] using hs)
      linarith
    simpa only [zero_add] using this.le

private theorem packet_rate (ρ : ℝ) {amp S : ℕ → ℂ} {a A : ℂ}
    (hamp : Tendsto amp atTop (nhds a)) (ha : a ≠ 0)
    (hS : Tendsto S atTop (nhds A)) :
    let G := fun N : ℕ => (((N : ℝ) ^ ρ : ℝ) : ℂ) *
      (amp N * Complex.exp ((N : ℂ) * S N))
    (∀ᶠ N in atTop, G N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖G N‖ / (N : ℝ)) atTop (nhds A.re) := by
  dsimp only
  have haev := hamp.eventually (eventually_ne_nhds ha)
  have hnpos : ∀ᶠ N : ℕ in atTop, (0 : ℝ) < (N : ℝ) := by
    filter_upwards [eventually_ge_atTop (1 : ℕ)] with N hN
    exact Nat.cast_pos.mpr (by omega)
  have hlogamp : Tendsto (fun N => Real.log ‖amp N‖)
      atTop (nhds (Real.log ‖a‖)) :=
    (Real.continuousAt_log (norm_ne_zero_iff.mpr ha)).tendsto.comp hamp.norm
  have h₁ := log_nat_div_tendsto.const_mul ρ
  have h₂ := hlogamp.mul inv_nat_tendsto
  have h₃ := Complex.continuous_re.continuousAt.tendsto.comp hS
  constructor
  · filter_upwards [haev, hnpos] with N haN hn
    exact mul_ne_zero (Complex.ofReal_ne_zero.mpr
      (ne_of_gt (Real.rpow_pos_of_pos hn ρ)))
      (mul_ne_zero haN (Complex.exp_ne_zero _))
  · have hsum : Tendsto
        (fun N : ℕ => ρ * (Real.log (N : ℝ) / (N : ℝ)) +
          Real.log ‖amp N‖ * (N : ℝ)⁻¹ + (S N).re)
        atTop (nhds A.re) := by
      simpa using (h₁.add h₂).add h₃
    apply hsum.congr'
    filter_upwards [haev, hnpos] with N haN hn
    rw [norm_mul, norm_mul, Real.log_mul
      (by simpa using (ne_of_gt (Real.rpow_pos_of_pos hn ρ)))
      (mul_ne_zero (norm_ne_zero_iff.mpr haN)
        (norm_ne_zero_iff.mpr (Complex.exp_ne_zero _))),
      Real.log_mul (norm_ne_zero_iff.mpr haN)
        (norm_ne_zero_iff.mpr (Complex.exp_ne_zero _))]
    simp only [Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (Real.rpow_nonneg hn.le ρ),
      Real.log_rpow hn, Complex.norm_exp, Real.log_exp, Complex.mul_re,
      Complex.natCast_re, Complex.natCast_im, zero_mul, sub_zero]
    field_simp
    ring

private theorem remainder_div_tendsto {G E : ℕ → ℂ} {a b : ℝ}
    (hne : ∀ᶠ N in atTop, G N ≠ 0)
    (hlead : Tendsto (fun N => Real.log ‖G N‖ / (N : ℝ))
      atTop (nhds a))
    (herr : UpperRate (fun N => ‖E N‖) b) (gap : b < a) :
    Tendsto (fun N => E N / G N) atTop (nhds 0) := by
  let δ := (a - b) / 4
  have hδ : 0 < δ := by dsimp [δ]; linarith
  have hlow := hlead.eventually (eventually_gt_nhds (show a - δ < a by linarith))
  have hbound : ∀ᶠ N in atTop,
      ‖E N / G N‖ ≤ Real.exp ((N : ℝ) * (-2 * δ)) := by
    filter_upwards [hne, hlow, herr.2 δ hδ,
      eventually_ge_atTop (1 : ℕ)] with N hGN hLN hEN hNpos
    have hn : (0 : ℝ) < (N : ℝ) := Nat.cast_pos.mpr (by omega)
    have hg : 0 < ‖G N‖ := norm_pos_iff.mpr hGN
    have hexp : Real.exp ((N : ℝ) * (a - δ)) ≤ ‖G N‖ := by
      apply (Real.le_log_iff_exp_le hg).mp
      have hh := (lt_div_iff₀ hn).mp hLN
      nlinarith
    have hratio : ‖E N‖ / ‖G N‖ ≤
        Real.exp ((N : ℝ) * (b + δ)) /
          Real.exp ((N : ℝ) * (a - δ)) :=
      div_le_div₀ (Real.exp_nonneg _) hEN (Real.exp_pos _) hexp
    rw [norm_div]
    apply hratio.trans_eq
    rw [← Real.exp_sub]
    congr 1
    dsimp [δ]
    ring
  have hdecay : Tendsto (fun N : ℕ => Real.exp ((N : ℝ) * (-2 * δ)))
      atTop (nhds 0) :=
    Real.tendsto_exp_atBot.comp
      (tendsto_natCast_atTop_atTop.atTop_mul_const_of_neg (by linarith : -2 * δ < 0))
  apply tendsto_zero_iff_norm_tendsto_zero.mpr
  exact squeeze_zero' (Eventually.of_forall fun N => norm_nonneg _) hbound hdecay

/-- The reference's complete packet-to-volume implication.
The diagram and filling powers are fixed before N tends through all integers.
The action is S N, not its limit substituted inside the exponential.
A convergent relative correction belongs in amp; E is the entire smaller
remainder. Its strict rate bound supplies the scalar noncancellation. -/
theorem complex_packet_volume_transfer
    {K u amp S E : ℕ → ℂ} {a A : ℂ} {b volume : ℝ} (ρ : ℝ)
    (exactSource : ∀ᶠ N in atTop,
      K N = u N * ((((N : ℝ) ^ ρ : ℝ) : ℂ) *
        (amp N * Complex.exp ((N : ℂ) * S N)) + E N))
    (unit : ∀ᶠ N in atTop, ‖u N‖ = 1)
    (hamp : Tendsto amp atTop (nhds a)) (ha : a ≠ 0)
    (hS : Tendsto S atTop (nhds A))
    (remainder : UpperRate (fun N => ‖E N‖) b)
    (gap : b < A.re) (geometry : 2 * Real.pi * A.re = volume) :
    (∀ᶠ N in atTop, K N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖K N‖ / (N : ℝ)) atTop (nhds A.re) ∧
      Tendsto (fun N => 2 * Real.pi * Real.log ‖K N‖ / (N : ℝ))
        atTop (nhds volume) := by
  let G := fun N : ℕ => (((N : ℝ) ^ ρ : ℝ) : ℂ) *
    (amp N * Complex.exp ((N : ℂ) * S N))
  have hG := packet_rate ρ hamp ha hS
  change (∀ᶠ N in atTop, G N ≠ 0) ∧
    Tendsto (fun N => Real.log ‖G N‖ / (N : ℝ)) atTop (nhds A.re) at hG
  have hratio := remainder_div_tendsto hG.1 hG.2 remainder gap
  have hfactor : Tendsto (fun N => 1 + E N / G N) atTop (nhds (1 : ℂ)) := by
    simpa using tendsto_const_nhds.add hratio
  have hfne := hfactor.eventually (eventually_ne_nhds (one_ne_zero : (1 : ℂ) ≠ 0))
  have hfactorlog : Tendsto (fun N => Real.log ‖1 + E N / G N‖)
      atTop (nhds 0) := by
    simpa only [Function.comp_def, norm_one, Real.log_one] using
      (Real.continuousAt_log (by norm_num : ‖(1 : ℂ)‖ ≠ 0)).tendsto.comp
        hfactor.norm
  have hnorm : ∀ᶠ N in atTop, ‖K N‖ = ‖G N‖ * ‖1 + E N / G N‖ := by
    filter_upwards [exactSource, unit, hG.1] with N hK hu hGN
    have hsplit : G N + E N = G N * (1 + E N / G N) := by
      field_simp
    change K N = u N * (G N + E N) at hK
    rw [hK, norm_mul, hu, one_mul, hsplit, norm_mul]
  have hKne : ∀ᶠ N in atTop, K N ≠ 0 := by
    filter_upwards [hnorm, hG.1, hfne] with N hKN hGN hfN
    apply norm_ne_zero_iff.mp
    rw [hKN]
    exact mul_ne_zero (norm_ne_zero_iff.mpr hGN) (norm_ne_zero_iff.mpr hfN)
  have hrate : Tendsto (fun N => Real.log ‖K N‖ / (N : ℝ))
      atTop (nhds A.re) := by
    have hsmall := hfactorlog.mul inv_nat_tendsto
    have hsum : Tendsto
        (fun N => Real.log ‖G N‖ / (N : ℝ) +
          Real.log ‖1 + E N / G N‖ * (N : ℝ)⁻¹)
        atTop (nhds A.re) := by
      simpa using hG.2.add hsmall
    apply hsum.congr'
    filter_upwards [hnorm, hG.1, hfne] with N hKN hGN hfN
    rw [hKN, Real.log_mul (norm_ne_zero_iff.mpr hGN) (norm_ne_zero_iff.mpr hfN)]
    ring
  refine ⟨hKne, hrate, ?_⟩
  have hv := hrate.const_mul (2 * Real.pi)
  rw [geometry] at hv
  simpa only [mul_div_assoc] using hv

end VolumeLogic.RealModel
