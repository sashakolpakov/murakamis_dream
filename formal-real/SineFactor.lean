import UniformProfile
import ActualGauge
import Mathlib.Analysis.Calculus.DSlope
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Complex
import Mathlib.Analysis.Normed.Group.Bounded

noncomputable section
open Filter
open scoped Topology
namespace VolumeLogic.SineFactor

/-- The complex sine quotient with its removable value at the origin. -/
def sinc (z : ℂ) : ℂ := if z = 0 then 1 else Complex.sin z / z

@[simp]
theorem sinc_zero : sinc 0 = 1 := by simp [sinc]

theorem sinc_of_ne_zero {z : ℂ} (hz : z ≠ 0) : sinc z = Complex.sin z / z := by
  simp [sinc, hz]

theorem sinc_eq_dslope : sinc = dslope Complex.sin 0 := by
  ext z
  simp [sinc, dslope, Function.update_apply, slope, div_eq_inv_mul]

theorem continuous_sinc : Continuous sinc := by
  apply continuous_iff_continuousAt.mpr
  intro z
  rw [sinc_eq_dslope]
  by_cases hz : z = 0
  · subst z
    apply continuousAt_dslope_same.mpr
    fun_prop
  · rw [continuousAt_dslope_of_ne hz]
    fun_prop

/-- The normalized limiting factor, with value one at s=0. -/
def limitingFactor (s : ℂ) : ℂ := sinc (Real.pi * s)

/-- On the denominator chart this is the original H_N with its removable
value at s=0. Every fixed compact lies in that chart for large N. -/
def factor (N : ℕ) (s : ℂ) : ℂ :=
  limitingFactor s / sinc (Real.pi * s / N)

@[simp]
theorem factor_zero (N : ℕ) : factor N 0 = 1 := by
  simp [factor, limitingFactor]

theorem continuous_limitingFactor : Continuous limitingFactor :=
  continuous_sinc.comp (by fun_prop)

theorem factor_eq_literal (N : ℕ) (s : ℂ) (hN : (N : ℂ) ≠ 0) (hs : s ≠ 0) :
    factor N s = ActualGauge.sineNormalization N s := by
  have hp : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  have hps := mul_ne_zero hp hs
  rw [factor, limitingFactor, sinc_of_ne_zero hps,
    sinc_of_ne_zero (div_ne_zero hps hN), ActualGauge.sineNormalization]
  field_simp

/-- The assigned value at zero is a continuous removable extension. -/
theorem continuousAt_factor_zero (N : ℕ) : ContinuousAt (factor N) 0 := by
  unfold factor
  apply continuous_limitingFactor.continuousAt.div
  · apply continuous_sinc.continuousAt.comp
    fun_prop
  · simp

/-- The original literal quotient tends to one at its punctured origin. -/
theorem literal_tendsto_zero (N : ℕ) (hN : (N : ℂ) ≠ 0) :
    Tendsto (ActualGauge.sineNormalization N) (𝓝[≠] (0 : ℂ)) (𝓝 1) := by
  have ht : Tendsto (factor N) (𝓝[≠] (0 : ℂ)) (𝓝 (factor N 0)) :=
    (continuousAt_factor_zero N).tendsto.mono_left nhdsWithin_le_nhds
  rw [factor_zero] at ht
  apply ht.congr'
  filter_upwards [self_mem_nhdsWithin] with s hs
  exact factor_eq_literal N s hN hs

/-- Uniformly small arguments stay in one continuity neighborhood of zero. -/
theorem uniform_scaled_continuous {K : Set ℂ} (hK : Bornology.IsBounded K)
    (g : ℂ → ℂ) (hg : ContinuousAt g 0) (a : ℂ) :
    TendstoUniformlyOn (fun N : ℕ => fun s => g (a*s/N))
      (fun _ => g 0) atTop K := by
  obtain ⟨R,hR,hbound⟩ := hK.exists_pos_norm_le
  apply Metric.tendstoUniformlyOn_iff.mpr
  intro ε hε
  obtain ⟨δ,hδ,hgδ⟩ := Metric.continuousAt_iff.mp hg ε hε
  have ht : Tendsto (fun N : ℕ => ‖a‖*R/(N : ℝ)) atTop (𝓝 0) :=
    VolumeLogic.RealModel.real_rateLimit_iff.mp
      (VolumeLogic.RealModel.constant_div_nat_rate (‖a‖*R))
  have hsmall : ∀ᶠ N : ℕ in atTop, ‖a‖*R/(N : ℝ) < δ :=
    ht.eventually (gt_mem_nhds hδ)
  filter_upwards [hsmall] with N hN
  intro s hs
  rw [dist_comm]
  apply hgδ
  rw [dist_zero_right, norm_div, norm_mul, Complex.norm_natCast]
  exact lt_of_le_of_lt
    (div_le_div_of_nonneg_right
      (mul_le_mul_of_nonneg_left (hbound s hs) (norm_nonneg a)) (Nat.cast_nonneg N)) hN

/-- The scaled denominator converges uniformly to one on every bounded set. -/
theorem denominator_tendsto {K : Set ℂ} (hK : Bornology.IsBounded K) :
    TendstoUniformlyOn (fun N : ℕ => fun s => sinc (Real.pi*s/N))
      (fun _ => (1 : ℂ)) atTop K := by
  simpa using uniform_scaled_continuous hK sinc continuous_sinc.continuousAt (Real.pi : ℂ)

/-- A single eventual threshold makes every scaled denominator nonzero. -/
theorem denominator_bounds {K : Set ℂ} (hK : Bornology.IsBounded K) :
    ∀ᶠ N : ℕ in atTop, ∀ s ∈ K,
      (1 : ℝ)/2 ≤ ‖sinc (Real.pi*s/N)‖ ∧ ‖sinc (Real.pi*s/N)‖ ≤ 3/2 := by
  convert UniformProfile.moving_factor_bounds (c := 1) (C := 1)
    (by norm_num) (denominator_tendsto hK) (fun _ _ => by norm_num) using 1
  norm_num

/-- The actual removable factor converges uniformly on every complex compact. -/
theorem factor_tendsto {K : Set ℂ} (hK : IsCompact K) :
    TendstoUniformlyOn factor limitingFactor atTop K := by
  obtain ⟨B,hB,hbound⟩ := (hK.image continuous_limitingFactor).isBounded.exists_pos_norm_le
  apply Metric.tendstoUniformlyOn_iff.mpr
  intro ε hε
  have hclose := Metric.tendstoUniformlyOn_iff.mp (denominator_tendsto hK.isBounded)
    (ε/(2*B)) (by positivity)
  filter_upwards [denominator_bounds hK.isBounded,hclose] with N hN heN
  intro s hs
  let d := sinc (Real.pi*s/N)
  have hdnorm : (1 : ℝ)/2 ≤ ‖d‖ := (hN s hs).1
  have hdpos : 0 < ‖d‖ := lt_of_lt_of_le (by norm_num) hdnorm
  have hd : d ≠ 0 := norm_pos_iff.mp hdpos
  have ha : ‖limitingFactor s‖ ≤ B := hbound _ (Set.mem_image_of_mem limitingFactor hs)
  have he : ‖1-d‖ < ε/(2*B) := by simpa [dist_eq_norm] using heN s hs
  have hid : factor N s - limitingFactor s = limitingFactor s * (1-d) / d := by
    change limitingFactor s / d - limitingFactor s = _
    field_simp
  have hb : ‖factor N s - limitingFactor s‖ ≤ 2*B*‖1-d‖ := by
    rw [hid, norm_div, norm_mul]
    apply (div_le_iff₀ hdpos).mpr
    have hn : 0 ≤ ‖1-d‖ := norm_nonneg _
    have hmul := mul_le_mul_of_nonneg_right hdnorm (mul_nonneg hB.le hn)
    have hnum := mul_le_mul_of_nonneg_right ha hn
    nlinarith
  rw [dist_comm, dist_eq_norm]
  apply lt_of_le_of_lt hb
  simpa only [mul_comm] using (lt_div_iff₀ (by positivity : 0 < 2*B)).mp he

/-- The only zeros of the limiting factor are the nonzero integers. -/
theorem limiting_zero_iff (s : ℂ) :
    limitingFactor s = 0 ↔ ∃ k : ℤ, k ≠ 0 ∧ s = (k : ℂ) := by
  have hp : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  constructor
  · intro hz
    have hs : s ≠ 0 := by intro hs; simp [hs, limitingFactor] at hz
    rw [limitingFactor, sinc_of_ne_zero (mul_ne_zero hp hs)] at hz
    have hsin : Complex.sin (Real.pi*s) = 0 :=
      (div_eq_zero_iff.mp hz).resolve_right (mul_ne_zero hp hs)
    obtain ⟨k,hk⟩ := Complex.sin_eq_zero_iff.mp hsin
    have hsk : s = (k : ℂ) := by
      apply mul_left_cancel₀ hp
      calc
        (Real.pi : ℂ)*s = k*Real.pi := hk
        _ = Real.pi*k := by ring
    refine ⟨k,?_,hsk⟩
    intro hk0
    exact hs (by simpa [hk0] using hsk)
  · rintro ⟨k,hk,rfl⟩
    have hkC : (k : ℂ) ≠ 0 := by exact_mod_cast hk
    rw [limitingFactor, sinc_of_ne_zero (mul_ne_zero hp hkC)]
    have hsin : Complex.sin ((Real.pi : ℂ)*k) = 0 := by
      rw [mul_comm]
      exact Complex.sin_int_mul_pi k
    rw [hsin, zero_div]

theorem limiting_ne_zero_of_avoids (s : ℂ)
    (hs : ∀ k : ℤ, k ≠ 0 → s ≠ (k : ℂ)) : limitingFactor s ≠ 0 := by
  intro hz
  obtain ⟨k,hk,hsk⟩ := (limiting_zero_iff s).mp hz
  exact hs k hk hsk

/-- The disks used in the tree-profile papers avoid every limiting zero. -/
theorem limiting_ne_zero_of_norm_lt_one (s : ℂ) (hs : ‖s‖ < 1) :
    limitingFactor s ≠ 0 := by
  apply limiting_ne_zero_of_avoids
  intro k hk he
  have hnorm : (1 : ℝ) ≤ ‖(k : ℂ)‖ := by
    rw [Complex.norm_intCast]
    exact_mod_cast Int.one_le_abs hk
  rw [he] at hs
  linarith

/-- The actual moving H_N has one positive lower bound on any compact
avoiding the nonzero integers, not merely a separate pointwise bound. -/
theorem compact_factor_bounds {K : Set ℂ} (hK : IsCompact K)
    (havoid : ∀ s ∈ K, ∀ k : ℤ, k ≠ 0 → s ≠ (k : ℂ)) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧
      ∀ᶠ N : ℕ in atTop, ∀ s ∈ K, c ≤ ‖factor N s‖ ∧ ‖factor N s‖ ≤ C := by
  exact UniformProfile.compact_moving_factor_bounds hK
    continuous_limitingFactor.continuousOn
    (fun s hs => limiting_ne_zero_of_avoids s (havoid s hs)) (factor_tendsto hK)

theorem disk_factor_bounds (R : ℝ) (hR : R < 1) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧
      ∀ᶠ N : ℕ in atTop, ∀ s ∈ Metric.closedBall (0 : ℂ) R,
        c ≤ ‖factor N s‖ ∧ ‖factor N s‖ ≤ C := by
  apply UniformProfile.compact_moving_factor_bounds (isCompact_closedBall 0 R)
    continuous_limitingFactor.continuousOn ?_ (factor_tendsto (isCompact_closedBall 0 R))
  intro s hs
  exact limiting_ne_zero_of_norm_lt_one s
    (lt_of_le_of_lt (by simpa [Metric.mem_closedBall, dist_zero_right] using hs) hR)

/-- The literal removable factor discharges the H_N limit and nonvanishing
premises in the compact profile-to-volume implication. The actual source,
A_N limit, error estimates, base rate and geometric calibration remain inputs. -/
theorem compact_sine_volume_transfer
    {K : Set ℂ} {F A error : ℕ → ℂ → ℂ} {base : ℕ → ℂ}
    {a : ℂ → ℂ} {rate volume C1 C2 : ℝ}
    (hK : IsCompact K) (ha : ContinuousOn a K)
    (hane : ∀ s ∈ K, a s ≠ 0)
    (havoid : ∀ s ∈ K, ∀ k : ℤ, k ≠ 0 → s ≠ (k : ℂ))
    (hAlim : TendstoUniformlyOn A a atTop K)
    (hbase : ∀ᶠ N in atTop, base N ≠ 0)
    (hrate : Tendsto (fun N => Real.log ‖base N‖/(N : ℝ)) atTop (𝓝 rate))
    (hprofile : ∀ᶠ N in atTop, ∀ s ∈ K,
      F N s = (A N s * factor N s) * base N * (1+error N s))
    (herror : ∀ᶠ N in atTop, ∀ s ∈ K,
      ‖error N s‖ ≤ C1/(N : ℝ)+C2/(N : ℝ)^2)
    (hvol : 2*Real.pi*rate = volume) :
    (∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0) ∧
      TendstoUniformlyOn (fun N s => 2*Real.pi*Real.log ‖F N s‖/(N : ℝ))
        (fun _ => volume) atTop K := by
  exact UniformProfile.compact_microscopic_volume_transfer hK ha
    continuous_limitingFactor.continuousOn hane
    (fun s hs => limiting_ne_zero_of_avoids s (havoid s hs))
    hAlim (factor_tendsto hK) hbase hrate hprofile herror hvol

/-- The exact fixed quadratic scalar in the two circle-tree profiles.
For a fixed diagram and fixed powers, its coefficient c is independent of N. -/
def quadraticPhase (c : ℂ) (N : ℕ) (s : ℂ) : ℂ :=
  Complex.exp (c*s^2/N)

/-- This is the printed q_N^((-w-sum n_v)s²/2), using the paper's explicit
convention q_N^a=exp(pi*i*a/N). The writhe and sum of powers are fixed. -/
theorem quadraticPhase_eq_diagram_scalar (w t : ℤ) (N : ℕ) (s : ℂ) :
    quadraticPhase ((Real.pi : ℂ)*Complex.I*(-(w : ℂ)-(t : ℂ))/2) N s =
      Complex.exp (((Real.pi : ℂ)*Complex.I/N)*((-(w : ℂ)-(t : ℂ))*s^2/2)) := by
  unfold quadraticPhase
  congr 1
  ring

theorem quadraticPhase_ne_zero (c : ℂ) (N : ℕ) (s : ℂ) :
    quadraticPhase c N s ≠ 0 := Complex.exp_ne_zero _

/-- The actual phase tends uniformly to one on every complex compact.
No unit-modulus assertion is made for complex parameters. -/
theorem quadraticPhase_tendsto (c : ℂ) {K : Set ℂ} (hK : IsCompact K) :
    TendstoUniformlyOn (quadraticPhase c) (fun _ => (1 : ℂ)) atTop K := by
  have hsq : Continuous (fun s : ℂ => s^2) := by fun_prop
  have ht := uniform_scaled_continuous (hK.image hsq).isBounded
    Complex.exp (by fun_prop) c
  apply Metric.tendstoUniformlyOn_iff.mpr
  intro ε hε
  have he := Metric.tendstoUniformlyOn_iff.mp ht ε hε
  filter_upwards [he] with N hN
  intro s hs
  simpa [quadraticPhase] using hN (s^2) (Set.mem_image_of_mem (fun z : ℂ => z^2) hs)

/-- Both explicit factors of the circle-tree profiles are now supplied.
Only the source profile and its error, base invariant rate and absolute
geometric calibration remain as substantive application inputs. -/
theorem compact_quadratic_sine_volume_transfer
    (c : ℂ) {K : Set ℂ} {F error : ℕ → ℂ → ℂ} {base : ℕ → ℂ}
    {rate volume C1 C2 : ℝ}
    (hK : IsCompact K)
    (havoid : ∀ s ∈ K, ∀ k : ℤ, k ≠ 0 → s ≠ (k : ℂ))
    (hbase : ∀ᶠ N in atTop, base N ≠ 0)
    (hrate : Tendsto (fun N => Real.log ‖base N‖/(N : ℝ)) atTop (𝓝 rate))
    (hprofile : ∀ᶠ N in atTop, ∀ s ∈ K,
      F N s = (quadraticPhase c N s * factor N s) * base N * (1+error N s))
    (herror : ∀ᶠ N in atTop, ∀ s ∈ K,
      ‖error N s‖ ≤ C1/(N : ℝ)+C2/(N : ℝ)^2)
    (hvol : 2*Real.pi*rate = volume) :
    (∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0) ∧
      TendstoUniformlyOn (fun N s => 2*Real.pi*Real.log ‖F N s‖/(N : ℝ))
        (fun _ => volume) atTop K := by
  exact compact_sine_volume_transfer (a := fun _ => 1) hK continuousOn_const
    (fun _ _ => one_ne_zero) havoid (quadraticPhase_tendsto c hK)
    hbase hrate hprofile herror hvol

end VolumeLogic.SineFactor
