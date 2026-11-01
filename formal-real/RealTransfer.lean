import VolumeLogic.VolumeTransfer
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith

/-!
Concrete realization of the existing Std-only transfer theorem. The imported
VolumeLogic sources come from the separate Std-only ../formal package.
The elementary analytic interfaces are constructed below: complex norm and
Real.log(x)/N satisfy their required laws by Mathlib theorems.
The diagram-specific saddle, full remainder, exact source and geometric
calibration remain explicit inputs to the final transfer, as they should.
-/
namespace VolumeLogic.RealModel
open Filter

noncomputable def complexMagnitude : Magnitude ℂ ℝ where
  value := fun z => ‖z‖
  nonneg := norm_nonneg
  eq_zero_iff := fun _ => norm_eq_zero
  mul := norm_mul
  add_le := norm_add_le
  neg := norm_neg

/-- This elementary Archimedean estimate proves the interface's scalar limit;
it does not assume any theorem about knot asymptotics. -/
theorem constant_div_nat_rate (c : ℝ) :
    RateLimit physicalLevels (fun N => c / (N : ℝ)) 0 := by
  intro ε hε
  obtain ⟨N₀, hN₀⟩ := exists_nat_gt (|c| / ε)
  refine ⟨N₀ + 1, fun N hn hp => ?_⟩
  have hNp : (0 : ℝ) < (N : ℝ) := Nat.cast_pos.mpr (by
    change 2 ≤ N at hp
    omega)
  have hle : (N₀ : ℝ) ≤ (N : ℝ) := Nat.cast_le.mpr (by omega)
  have hf : |c| / ε < (N : ℝ) := lt_of_lt_of_le hN₀ hle
  have hsmall : |c / (N : ℝ)| < ε := by
    rw [abs_div, abs_of_pos hNp]
    apply (div_lt_iff₀ hNp).mpr
    simpa [mul_comm] using (div_lt_iff₀ hε).mp hf
  simpa only [zero_sub, zero_add] using abs_lt.mp hsmall

noncomputable def realLogScale : LogScale ℝ where
  value := fun N x => Real.log x / (N : ℝ)
  monotone := by
    intro N x y hx hxy
    exact div_le_div_of_nonneg_right (Real.log_le_log hx hxy) (Nat.cast_nonneg N)
  product := by
    intro N x y hx hy
    rw [Real.log_mul (ne_of_gt hx) (ne_of_gt hy), add_div]
  constant_limit := fun c _ => constant_div_nat_rate (Real.log c)

/-- Removing finitely many nonphysical initial levels is exactly ordinary
atTop eventuality; no prime-level or parity restriction is introduced. -/
theorem eventually_physical_iff {P : Nat → Prop} :
    EventuallyOn physicalLevels P ↔ ∀ᶠ N in atTop, P N := by
  constructor
  · rintro ⟨N₀, h⟩
    apply eventually_atTop.mpr
    refine ⟨N₀ + 2, fun N hn => h N (by omega) ?_⟩
    change 2 ≤ N
    omega
  · intro h
    obtain ⟨N₀, h⟩ := eventually_atTop.mp h
    exact ⟨N₀, fun N hn _ => h N hn⟩

/-- The custom epsilon interface is ordinary convergence in the real topology. -/
theorem real_rateLimit_iff {f : Nat → ℝ} {a : ℝ} :
    RateLimit physicalLevels f a ↔ Tendsto f atTop (nhds a) := by
  constructor
  · intro h
    apply Metric.tendsto_atTop.mpr
    intro ε hε
    obtain ⟨N₀, hN₀⟩ := h ε hε
    refine ⟨N₀ + 2, fun N hn => ?_⟩
    have hp : physicalLevels N := by change 2 ≤ N; omega
    have hb := hN₀ N (by omega) hp
    change a - ε < f N ∧ f N < a + ε at hb
    obtain ⟨hl, hu⟩ := hb
    rw [Real.dist_eq]
    apply abs_lt.mpr
    constructor <;> linarith
  · intro h ε hε
    obtain ⟨N₀, hN₀⟩ := Metric.tendsto_atTop.mp h ε hε
    refine ⟨N₀, fun N hn _ => ?_⟩
    have hb := hN₀ N hn
    rw [Real.dist_eq] at hb
    have ha := abs_lt.mp hb
    constructor <;> linarith

/-- Actual modulus/log rate, with eventual nonvanishing kept separate from
Real.log's totalized value at zero. -/
theorem complex_hasRate_iff {f : Nat → ℂ} {a : ℝ} :
    HasRate physicalLevels complexMagnitude realLogScale f a ↔
      (∀ᶠ N in atTop, f N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖f N‖ / (N : ℝ)) atTop (nhds a) := by
  change (EventuallyOn physicalLevels (fun N => f N ≠ 0) ∧
    RateLimit physicalLevels (fun N => Real.log ‖f N‖ / (N : ℝ)) a) ↔ _
  rw [eventually_physical_iff, real_rateLimit_iff]

theorem complex_hasUpperRate_iff {f : Nat → ℂ} {b : ℝ} :
    HasUpperRate physicalLevels complexMagnitude realLogScale f b ↔
      ∀ ε > 0, ∀ᶠ N in atTop,
        f N = 0 ∨ Real.log ‖f N‖ / (N : ℝ) ≤ b + ε := by
  simp only [HasUpperRate, eventually_physical_iff,
    magnitudeRate, complexMagnitude, realLogScale]

/-- A concrete instantiation of VolumeLogic.invariant_rate_transfer.
Every bound concerns the same exact complex sequence at all sufficiently
large integer levels. The remainder is the whole E, not a chosen sector. -/
theorem complex_invariant_rate_transfer
    {K u G E : Nat → ℂ} {a b : ℝ}
    (exactSource : ∀ᶠ N in atTop, K N = u N * (G N + E N))
    (normalization : (∀ᶠ N in atTop, u N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖u N‖ / (N : ℝ)) atTop (nhds 0))
    (leading : (∀ᶠ N in atTop, G N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖G N‖ / (N : ℝ)) atTop (nhds a))
    (remainder : ∀ ε > 0, ∀ᶠ N in atTop,
      E N = 0 ∨ Real.log ‖E N‖ / (N : ℝ) ≤ b + ε)
    (gap : b < a) :
    (∀ᶠ N in atTop, K N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖K N‖ / (N : ℝ)) atTop (nhds a) := by
  apply complex_hasRate_iff.mp
  exact invariant_rate_transfer (fun _ h => h) complexMagnitude realLogScale
    (eventually_physical_iff.mpr exactSource)
    (complex_hasRate_iff.mpr normalization) (complex_hasRate_iff.mpr leading)
    (complex_hasUpperRate_iff.mpr remainder) gap

/-- Unit framing characters supply normalization automatically. -/
theorem unit_norm_hasRate {u : Nat → ℂ}
    (unit : ∀ᶠ N in atTop, ‖u N‖ = 1) :
    HasRate physicalLevels complexMagnitude realLogScale u 0 := by
  apply complex_hasRate_iff.mpr
  constructor
  · filter_upwards [unit] with N hN
    intro hz
    simp [hz] at hN
  · apply tendsto_const_nhds.congr'
    filter_upwards [unit] with N hN
    simp [hN]

/-- Convergence to a nonzero actual complex amplitude proves its zero rate;
no abstract LogScale law is assumed here. -/
theorem amplitude_hasRate_of_tendsto {amp : Nat → ℂ} {a : ℂ}
    (hamp : Tendsto amp atTop (nhds a)) (ha : a ≠ 0) :
    HasRate physicalLevels complexMagnitude realLogScale amp 0 := by
  apply complex_hasRate_iff.mpr
  constructor
  · exact hamp.eventually (eventually_ne_nhds ha)
  · have hlog : Tendsto (fun N => Real.log ‖amp N‖) atTop (nhds (Real.log ‖a‖)) :=
      (Real.continuousAt_log (norm_ne_zero_iff.mpr ha)).tendsto.comp hamp.norm
    have hrec : Tendsto (fun N : Nat => (1 : ℝ) / (N : ℝ)) atTop (nhds 0) :=
      real_rateLimit_iff.mp (constant_div_nat_rate 1)
    simpa only [mul_zero, div_eq_mul_inv, one_mul] using hlog.mul hrec

/-- The finite critical action may vary with N; only its convergence is used.
The complex exponential is never zero and its actual modulus is exp(Re). -/
theorem exponential_action_hasRate {S : Nat → ℂ} {A : ℂ}
    (hS : Tendsto S atTop (nhds A)) :
    HasRate physicalLevels complexMagnitude realLogScale
      (fun N => Complex.exp ((N : ℂ) * S N)) A.re := by
  apply complex_hasRate_iff.mpr
  constructor
  · exact Filter.Eventually.of_forall (fun N => Complex.exp_ne_zero _)
  · have hre : Tendsto (fun N => (S N).re) atTop (nhds A.re) :=
      Complex.continuous_re.continuousAt.tendsto.comp hS
    apply hre.congr'
    filter_upwards [eventually_ge_atTop (1 : Nat)] with N hN
    have hn : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
    simp only [Complex.norm_exp, Real.log_exp, Complex.mul_re,
      Complex.natCast_re, Complex.natCast_im, zero_mul, sub_zero]
    exact (mul_div_cancel_left₀ (S N).re hn).symm

/-- The nonzero packet with convergent finite action has its actual modulus
rate. Relative corrections tending to 1 may be kept inside amp. -/
theorem gaussian_packet_hasRate {amp S : Nat → ℂ} {a A : ℂ}
    (hamp : Tendsto amp atTop (nhds a)) (ha : a ≠ 0)
    (hS : Tendsto S atTop (nhds A)) :
    HasRate physicalLevels complexMagnitude realLogScale
      (fun N => amp N * Complex.exp ((N : ℂ) * S N)) A.re := by
  have h := hasRate_mul complexMagnitude realLogScale
    (amplitude_hasRate_of_tendsto hamp ha) (exponential_action_hasRate hS)
  simpa only [zero_add] using h

/-- The volume normalization is an ordinary real limit. Geometry still
supplies the equality for the same exact sequence and action. -/
theorem complex_volume_transfer
    {K u G E : Nat → ℂ} {a b volume : ℝ}
    (exactSource : ∀ᶠ N in atTop, K N = u N * (G N + E N))
    (normalization : (∀ᶠ N in atTop, u N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖u N‖ / (N : ℝ)) atTop (nhds 0))
    (leading : (∀ᶠ N in atTop, G N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖G N‖ / (N : ℝ)) atTop (nhds a))
    (remainder : ∀ ε > 0, ∀ᶠ N in atTop,
      E N = 0 ∨ Real.log ‖E N‖ / (N : ℝ) ≤ b + ε)
    (gap : b < a) (geometry : 2 * Real.pi * a = volume) :
    (∀ᶠ N in atTop, K N ≠ 0) ∧
      Tendsto (fun N => 2 * Real.pi * Real.log ‖K N‖ / (N : ℝ))
        atTop (nhds volume) := by
  have h := complex_invariant_rate_transfer exactSource normalization leading remainder gap
  refine ⟨h.1, ?_⟩
  have ht := h.2.const_mul (2 * Real.pi)
  rw [geometry] at ht
  simpa only [mul_div_assoc] using ht


/-- Any fixed real power of the level is subexponential, including the
half-integral Gaussian powers in the actual period formulas. -/
theorem level_power_hasRate (k : ℝ) :
    HasRate physicalLevels complexMagnitude realLogScale
      (fun N => (((N : ℝ) ^ k : ℝ) : ℂ)) 0 := by
  apply complex_hasRate_iff.mpr
  have hp : ∀ᶠ N : Nat in atTop, (0 : ℝ) < (N : ℝ) := by
    filter_upwards [eventually_ge_atTop (1 : Nat)] with N hN
    exact Nat.cast_pos.mpr (by omega)
  constructor
  · filter_upwards [hp] with N hN
    apply norm_pos_iff.mp
    simp only [Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (Real.rpow_nonneg (le_of_lt hN) k)]
    exact Real.rpow_pos_of_pos hN k
  · have hb : Tendsto (fun x : ℝ => Real.log x / x) atTop (nhds 0) := by
      simpa using Real.tendsto_pow_log_div_mul_add_atTop 1 0 1 one_ne_zero
    have hn : Tendsto (fun N : Nat => Real.log (N : ℝ) / (N : ℝ)) atTop (nhds 0) :=
      hb.comp tendsto_natCast_atTop_atTop
    have hk : Tendsto (fun N : Nat => k * (Real.log (N : ℝ) / (N : ℝ)))
        atTop (nhds 0) := by simpa using hn.const_mul k
    apply hk.congr'
    filter_upwards [hp] with N hN
    simp only [Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (Real.rpow_nonneg (le_of_lt hN) k), Real.log_rpow hN,
      mul_div_assoc]

/-- A finite critical action, a convergent nonzero complex coefficient and
an explicit fixed level power produce the leading rate. The coefficient and
action limits here are all-level limits, not separate parity limits. -/
theorem powered_gaussian_packet_hasRate (k : ℝ) {amp S : Nat → ℂ} {a A : ℂ}
    (hamp : Tendsto amp atTop (nhds a)) (ha : a ≠ 0)
    (hS : Tendsto S atTop (nhds A)) :
    HasRate physicalLevels complexMagnitude realLogScale
      (fun N => (((N : ℝ) ^ k : ℝ) : ℂ) *
        (amp N * Complex.exp ((N : ℂ) * S N))) A.re := by
  have h := hasRate_mul complexMagnitude realLogScale (level_power_hasRate k)
    (gaussian_packet_hasRate hamp ha hS)
  simpa only [zero_add] using h

/-- The concrete packet-to-volume implication. The first-charge coefficient
and finite action have ordinary topological limits; all elementary norm,
logarithm, power and noncancellation steps are now proved, not assumptions.
The exact original source identity, whole-remainder bound and identification
of the limiting action with the same knot's volume remain explicit inputs. -/
theorem complex_packet_volume_transfer
    {K u amp S E : Nat → ℂ} {a A : ℂ} {b volume : ℝ} (k : ℝ)
    (exactSource : ∀ᶠ N in atTop,
      K N = u N * ((((N : ℝ) ^ k : ℝ) : ℂ) *
        (amp N * Complex.exp ((N : ℂ) * S N)) + E N))
    (unit : ∀ᶠ N in atTop, ‖u N‖ = 1)
    (hamp : Tendsto amp atTop (nhds a)) (ha : a ≠ 0)
    (hS : Tendsto S atTop (nhds A))
    (remainder : ∀ ε > 0, ∀ᶠ N in atTop,
      E N = 0 ∨ Real.log ‖E N‖ / (N : ℝ) ≤ b + ε)
    (gap : b < A.re) (geometry : 2 * Real.pi * A.re = volume) :
    (∀ᶠ N in atTop, K N ≠ 0) ∧
      Tendsto (fun N => 2 * Real.pi * Real.log ‖K N‖ / (N : ℝ))
        atTop (nhds volume) := by
  exact complex_volume_transfer exactSource
    (complex_hasRate_iff.mp (unit_norm_hasRate unit))
    (complex_hasRate_iff.mp (powered_gaussian_packet_hasRate k hamp ha hS))
    remainder gap geometry

end VolumeLogic.RealModel
