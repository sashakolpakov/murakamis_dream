import RealTransfer
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Topology.MetricSpace.Pseudo.Basic
import Mathlib.Topology.Order.Compact

/-!
Uniform consequences of the written microscopic profile. No pointwise
convergence is substituted for a common threshold. The parameter set need
not be compact once its uniform profile bounds have been supplied.
-/
noncomputable section
open Filter
open scoped Topology

namespace VolumeLogic.UniformProfile

theorem norm_one_add_bounds {z : ℂ} (hz : ‖z‖ ≤ (1 : ℝ)/2) :
    (1 : ℝ)/2 ≤ ‖1+z‖ ∧ ‖1+z‖ ≤ 3/2 := by
  have hlow : (1 : ℝ) ≤ ‖1+z‖ + ‖z‖ := by
    simpa using norm_sub_le (1+z) z
  have hu := norm_add_le (1 : ℂ) z
  norm_num at hu
  constructor <;> linarith

/-- A bounded small relative error preserves uniform positive multiplicative
bounds. The actual level-dependent profile factor is retained. -/
theorem profile_norm_bounds {f factor base error : ℂ} {c C : ℝ}
    (_hc : 0 < c) (hfactor : c ≤ ‖factor‖ ∧ ‖factor‖ ≤ C)
    (herr : ‖error‖ ≤ (1 : ℝ)/2)
    (heq : f = factor * base * (1+error)) :
    (c/2)*‖base‖ ≤ ‖f‖ ∧ ‖f‖ ≤ (3*C/2)*‖base‖ := by
  obtain ⟨hl,hu⟩ := norm_one_add_bounds herr
  rw [heq, norm_mul, norm_mul]
  have hb := norm_nonneg base
  have hf := norm_nonneg factor
  constructor
  · nlinarith [mul_le_mul_of_nonneg_right hfactor.1 hb,
      mul_le_mul_of_nonneg_left hl (mul_nonneg hf hb)]
  · have hC : 0 ≤ C := le_trans hf hfactor.2
    nlinarith [mul_le_mul_of_nonneg_right hfactor.2 hb,
      mul_le_mul_of_nonneg_left hu (mul_nonneg hf hb)]

/-- Two fixed positive multiplicative bounds give an explicit O(1/N)
bound on the difference of actual logarithmic rates. -/
theorem log_rate_corridor {f base : ℂ} {l u : ℝ} {N : ℕ}
    (hl : 0 < l) (hu : 0 < u) (hb : base ≠ 0)
    (hbound : l*‖base‖ ≤ ‖f‖ ∧ ‖f‖ ≤ u*‖base‖) :
    f ≠ 0 ∧
      |Real.log ‖f‖/(N : ℝ) - Real.log ‖base‖/(N : ℝ)| ≤
        (|Real.log l|+|Real.log u|)/(N : ℝ) := by
  have hbp : 0 < ‖base‖ := norm_pos_iff.mpr hb
  have hfp : 0 < ‖f‖ := lt_of_lt_of_le (mul_pos hl hbp) hbound.1
  have hlo := Real.log_le_log (mul_pos hl hbp) hbound.1
  have hup := Real.log_le_log hfp hbound.2
  rw [Real.log_mul (ne_of_gt hl) (ne_of_gt hbp)] at hlo
  rw [Real.log_mul (ne_of_gt hu) (ne_of_gt hbp)] at hup
  have hab : |Real.log ‖f‖ - Real.log ‖base‖| ≤
      |Real.log l|+|Real.log u| := by
    apply abs_le.mpr
    constructor
    · have := neg_abs_le (Real.log l)
      have := abs_nonneg (Real.log u)
      linarith
    · have := le_abs_self (Real.log u)
      have := abs_nonneg (Real.log l)
      linarith
  refine ⟨norm_pos_iff.mp hfp, ?_⟩
  rw [← sub_div, abs_div]
  rw [show |(N : ℝ)| = (N : ℝ) from abs_of_nonneg (Nat.cast_nonneg N)]
  exact div_le_div_of_nonneg_right hab (Nat.cast_nonneg N)

/-- This is uniform in the parameter, with one eventual level threshold.
The only asymptotic input is the scalar base rate; the rate of the
parameter-dependent profile is derived from actual norm bounds. -/
theorem uniform_profile_rate {α : Type*} {K : Set α}
    {F factor error : ℕ → α → ℂ} {base : ℕ → ℂ}
    {c C rate : ℝ} (hc : 0 < c) (hC : 0 < C)
    (hbase : ∀ᶠ N in atTop, base N ≠ 0)
    (hrate : Tendsto (fun N => Real.log ‖base N‖/(N : ℝ)) atTop (𝓝 rate))
    (hprofile : ∀ᶠ N in atTop, ∀ s ∈ K,
      F N s = factor N s * base N * (1+error N s))
    (hfactor : ∀ᶠ N in atTop, ∀ s ∈ K,
      c ≤ ‖factor N s‖ ∧ ‖factor N s‖ ≤ C)
    (herror : ∀ᶠ N in atTop, ∀ s ∈ K, ‖error N s‖ ≤ (1 : ℝ)/2) :
    (∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0) ∧
      ∀ ε > 0, ∀ᶠ N in atTop, ∀ s ∈ K,
        |Real.log ‖F N s‖/(N : ℝ)-rate| < ε := by
  let B := |Real.log (c/2)|+|Real.log (3*C/2)|
  have hcorr : ∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0 ∧
      |Real.log ‖F N s‖/(N : ℝ)-Real.log ‖base N‖/(N : ℝ)| ≤ B/(N : ℝ) := by
    filter_upwards [hbase,hprofile,hfactor,herror]
      with N hb he hf hr
    intro s hs
    exact log_rate_corridor (by positivity) (by positivity) hb
      (profile_norm_bounds hc (hf s hs) (hr s hs) (he s hs))
  refine ⟨hcorr.mono (fun N h s hs => (h s hs).1), ?_⟩
  intro ε hε
  have hsmall : ∀ᶠ (N : ℕ) in atTop, |B/(N : ℝ)| < ε/2 := by
    have ht := VolumeLogic.RealModel.real_rateLimit_iff.mp
      (VolumeLogic.RealModel.constant_div_nat_rate B)
    simpa only [Real.dist_eq,sub_zero] using
      (Metric.tendsto_atTop.mp ht (ε/2) (by positivity) |> eventually_atTop.mpr)
  have hclose : ∀ᶠ N in atTop,
      |Real.log ‖base N‖/(N : ℝ)-rate| < ε/2 := by
    simpa only [Real.dist_eq] using
      (Metric.tendsto_atTop.mp hrate (ε/2) (by positivity) |> eventually_atTop.mpr)
  filter_upwards [hcorr,hsmall,hclose] with N hn hsmall hclose
  intro s hs
  have ht := abs_add_le
    (Real.log ‖F N s‖/(N : ℝ)-Real.log ‖base N‖/(N : ℝ))
    (Real.log ‖base N‖/(N : ℝ)-rate)
  have hb := le_abs_self (B/(N : ℝ))
  have h := (hn s hs).2
  have heq : (Real.log ‖F N s‖/(N : ℝ)-Real.log ‖base N‖/(N : ℝ))+
      (Real.log ‖base N‖/(N : ℝ)-rate) = Real.log ‖F N s‖/(N : ℝ)-rate := by ring
  rw [heq] at ht
  linarith

/-- The epsilon statement above is genuine uniform convergence on the set,
not a separate pointwise limit at each parameter. -/
theorem uniform_profile_tendsto {α : Type*} {K : Set α}
    {F factor error : ℕ → α → ℂ} {base : ℕ → ℂ}
    {c C rate : ℝ} (hc : 0 < c) (hC : 0 < C)
    (hbase : ∀ᶠ N in atTop, base N ≠ 0)
    (hrate : Tendsto (fun N => Real.log ‖base N‖/(N : ℝ)) atTop (𝓝 rate))
    (hprofile : ∀ᶠ N in atTop, ∀ s ∈ K,
      F N s = factor N s * base N * (1+error N s))
    (hfactor : ∀ᶠ N in atTop, ∀ s ∈ K,
      c ≤ ‖factor N s‖ ∧ ‖factor N s‖ ≤ C)
    (herror : TendstoUniformlyOn error (fun _ => 0) atTop K) :
    (∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0) ∧
      TendstoUniformlyOn (fun N s => Real.log ‖F N s‖/(N : ℝ))
        (fun _ => rate) atTop K := by
  have he : ∀ᶠ N in atTop, ∀ s ∈ K, ‖error N s‖ ≤ (1 : ℝ)/2 := by
    have h := Metric.tendstoUniformlyOn_iff.mp herror (1/2) (by norm_num)
    filter_upwards [h] with N hN
    intro s hs
    simpa [dist_eq_norm] using (hN s hs).le
  obtain ⟨hn,hr⟩ := uniform_profile_rate hc hC hbase hrate hprofile hfactor he
  refine ⟨hn,Metric.tendstoUniformlyOn_iff.mpr ?_⟩
  intro ε hε
  filter_upwards [hr ε hε] with N hN
  intro s hs
  simpa only [Real.dist_eq,abs_sub_comm] using hN s hs

/-- The actual varying H_N may be bounded through its uniform limit. No
replacement H_N=H is made in the profile identity. -/
theorem moving_factor_bounds {α : Type*} {K : Set α}
    {H : ℕ → α → ℂ} {h : α → ℂ} {c C : ℝ} (hc : 0 < c)
    (hlim : TendstoUniformlyOn H h atTop K)
    (hbound : ∀ s ∈ K, c ≤ ‖h s‖ ∧ ‖h s‖ ≤ C) :
    ∀ᶠ N in atTop, ∀ s ∈ K, c/2 ≤ ‖H N s‖ ∧ ‖H N s‖ ≤ C+c/2 := by
  have he := Metric.tendstoUniformlyOn_iff.mp hlim (c/2) (by positivity)
  filter_upwards [he] with N hN
  intro s hs
  have hdist : ‖h s-H N s‖ < c/2 := by simpa [dist_eq_norm] using hN s hs
  have hl := norm_le_norm_add_norm_sub (h s) (H N s)
  have hu := norm_le_norm_add_norm_sub (H N s) (h s)
  rw [norm_sub_rev] at hu
  obtain ⟨hlo,hup⟩ := hbound s hs
  constructor <;> linarith

/-- Compactness and actual nonvanishing of the continuous limiting factor
construct the positive lower and upper bounds, including an empty set. -/
theorem compact_nonvanishing_bounds {α : Type*} [TopologicalSpace α]
    {K : Set α} {h : α → ℂ} (hK : IsCompact K)
    (hh : ContinuousOn h K) (hne : ∀ s ∈ K, h s ≠ 0) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧ ∀ s ∈ K, c ≤ ‖h s‖ ∧ ‖h s‖ ≤ C := by
  by_cases hnon : K.Nonempty
  · obtain ⟨x,hx,hmin⟩ := hK.exists_isMinOn hnon hh.norm
    obtain ⟨y,hy,hmax⟩ := hK.exists_isMaxOn hnon hh.norm
    exact ⟨‖h x‖,‖h y‖,norm_pos_iff.mpr (hne x hx),norm_pos_iff.mpr (hne y hy),
      fun s hs => ⟨hmin hs,hmax hs⟩⟩
  · refine ⟨1,1,by norm_num,by norm_num,?_⟩
    intro s hs
    exact (hnon ⟨s,hs⟩).elim

/-- A uniformly convergent, level-dependent factor with a continuous
nonvanishing compact limit has uniform positive bounds at all large
levels. This theorem derives rather than assumes the common threshold. -/
theorem compact_moving_factor_bounds {α : Type*} [TopologicalSpace α]
    {K : Set α} {H : ℕ → α → ℂ} {h : α → ℂ} (hK : IsCompact K)
    (hh : ContinuousOn h K) (hne : ∀ s ∈ K, h s ≠ 0)
    (hlim : TendstoUniformlyOn H h atTop K) :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧
      ∀ᶠ N in atTop, ∀ s ∈ K, c ≤ ‖H N s‖ ∧ ‖H N s‖ ≤ C := by
  obtain ⟨c,C,hc,hC,hbound⟩ := compact_nonvanishing_bounds hK hh hne
  exact ⟨c/2,C+c/2,by positivity,by positivity,moving_factor_bounds hc hlim hbound⟩

/-- Separate bounded scalar and moving modified-dimension factors are kept
in the exact source profile. This covers complex parameters; neither
factor is presumed to have unit modulus. -/
theorem scalar_profile_transfer {α : Type*} {K : Set α}
    {F A H error : ℕ → α → ℂ} {base : ℕ → ℂ}
    {a b c C rate : ℝ} (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) (hC : 0 < C)
    (hbase : ∀ᶠ N in atTop, base N ≠ 0)
    (hrate : Tendsto (fun N => Real.log ‖base N‖/(N : ℝ)) atTop (𝓝 rate))
    (hprofile : ∀ᶠ N in atTop, ∀ s ∈ K,
      F N s = (A N s * H N s) * base N * (1+error N s))
    (hA : ∀ᶠ N in atTop, ∀ s ∈ K, a ≤ ‖A N s‖ ∧ ‖A N s‖ ≤ b)
    (hH : ∀ᶠ N in atTop, ∀ s ∈ K, c ≤ ‖H N s‖ ∧ ‖H N s‖ ≤ C)
    (herror : TendstoUniformlyOn error (fun _ => 0) atTop K) :
    (∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0) ∧
      TendstoUniformlyOn (fun N s => Real.log ‖F N s‖/(N : ℝ))
        (fun _ => rate) atTop K := by
  apply uniform_profile_tendsto (c := a*c) (C := b*C) (by positivity) (by positivity)
    hbase hrate hprofile ?_ herror
  filter_upwards [hA,hH] with N hAN hHN
  intro s hs
  obtain ⟨ha1,ha2⟩ := hAN s hs
  obtain ⟨hc1,hc2⟩ := hHN s hs
  rw [norm_mul]
  exact ⟨mul_le_mul ha1 hc1 hc.le (norm_nonneg _),
    mul_le_mul ha2 hc2 (norm_nonneg _) hb.le⟩

theorem uniform_vanishing_of_bound {α : Type*} {K : Set α}
    {error : ℕ → α → ℂ} {bound : ℕ → ℝ}
    (hb : Tendsto bound atTop (𝓝 0))
    (he : ∀ᶠ N in atTop, ∀ s ∈ K, ‖error N s‖ ≤ bound N) :
    TendstoUniformlyOn error (fun _ => 0) atTop K := by
  apply Metric.tendstoUniformlyOn_iff.mpr
  intro ε hε
  have hsmall : ∀ᶠ N in atTop, |bound N| < ε := by
    simpa only [Real.dist_eq,sub_zero] using
      (Metric.tendsto_atTop.mp hb ε hε |> eventually_atTop.mpr)
  filter_upwards [he,hsmall] with N hN hsmall
  intro s hs
  have h := lt_of_le_of_lt (hN s hs) (lt_of_le_of_lt (le_abs_self _) hsmall)
  simpa [dist_eq_norm] using h

/-- The first-order directed profile supplies a uniform error tending to
zero with one threshold, not a family of pointwise O-estimates. -/
theorem uniform_vanishing_of_inverse_level {α : Type*} {K : Set α}
    {error : ℕ → α → ℂ} (C : ℝ)
    (he : ∀ᶠ N in atTop, ∀ s ∈ K, ‖error N s‖ ≤ C/(N : ℝ)) :
    TendstoUniformlyOn error (fun _ => 0) atTop K := by
  exact uniform_vanishing_of_bound
    (VolumeLogic.RealModel.real_rateLimit_iff.mp
      (VolumeLogic.RealModel.constant_div_nat_rate C)) he

/-- The centered summed-tree expansion retains its O(1/N) coefficient and
O(1/N^2) error. Boundedness of that coefficient on the chosen compact
gives this concrete two-order norm bound. -/
theorem uniform_vanishing_of_two_orders {α : Type*} {K : Set α}
    {error : ℕ → α → ℂ} (C1 C2 : ℝ)
    (he : ∀ᶠ N in atTop, ∀ s ∈ K,
      ‖error N s‖ ≤ C1/(N : ℝ)+C2/(N : ℝ)^2) :
    TendstoUniformlyOn error (fun _ => 0) atTop K := by
  have h1 := VolumeLogic.RealModel.real_rateLimit_iff.mp
    (VolumeLogic.RealModel.constant_div_nat_rate C1)
  have h2 := VolumeLogic.RealModel.real_rateLimit_iff.mp
    (VolumeLogic.RealModel.constant_div_nat_rate C2)
  have hinv := VolumeLogic.RealModel.real_rateLimit_iff.mp
    (VolumeLogic.RealModel.constant_div_nat_rate 1)
  have hsq : Tendsto (fun N : ℕ => C2/(N : ℝ)^2) atTop (𝓝 0) := by
    convert h2.mul hinv using 1 <;> simp [pow_two,div_eq_mul_inv,mul_assoc]
  have ht : Tendsto (fun N : ℕ => C1/(N : ℝ)+C2/(N : ℝ)^2) atTop (𝓝 0) := by
    simpa using h1.add hsq
  exact uniform_vanishing_of_bound ht he

/-- Concrete cta:profile/dt:profile consequence. Both moving factors stay
in the exact equation. The 2*pi normalization is restored uniformly. -/
theorem microscopic_volume_transfer {α : Type*} {K : Set α}
    {F A H error : ℕ → α → ℂ} {base : ℕ → ℂ}
    {a b c C rate volume : ℝ} (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) (hC : 0 < C)
    (hbase : ∀ᶠ N in atTop, base N ≠ 0)
    (hrate : Tendsto (fun N => Real.log ‖base N‖/(N : ℝ)) atTop (𝓝 rate))
    (hprofile : ∀ᶠ N in atTop, ∀ s ∈ K,
      F N s = (A N s * H N s) * base N * (1+error N s))
    (hA : ∀ᶠ N in atTop, ∀ s ∈ K, a ≤ ‖A N s‖ ∧ ‖A N s‖ ≤ b)
    (hH : ∀ᶠ N in atTop, ∀ s ∈ K, c ≤ ‖H N s‖ ∧ ‖H N s‖ ≤ C)
    (herror : TendstoUniformlyOn error (fun _ => 0) atTop K)
    (hvol : 2*Real.pi*rate = volume) :
    (∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0) ∧
      TendstoUniformlyOn (fun N s => 2*Real.pi*Real.log ‖F N s‖/(N : ℝ))
        (fun _ => volume) atTop K := by
  obtain ⟨hn,hr⟩ := scalar_profile_transfer ha hb hc hC hbase hrate hprofile hA hH herror
  refine ⟨hn,Metric.tendstoUniformlyOn_iff.mpr ?_⟩
  intro ε hε
  have hp : 0 < 2*Real.pi := by positivity
  have he := Metric.tendstoUniformlyOn_iff.mp hr (ε/(2*Real.pi)) (by positivity)
  filter_upwards [he] with N hN
  intro s hs
  have h := hN s hs
  rw [Real.dist_eq,abs_sub_comm] at h
  rw [Real.dist_eq,← hvol]
  have heq : 2*Real.pi*rate-2*Real.pi*Real.log ‖F N s‖/(N : ℝ) =
      (2*Real.pi)*(rate-Real.log ‖F N s‖/(N : ℝ)) := by ring
  rw [heq,abs_mul,abs_of_pos hp,abs_sub_comm]
  simpa only [mul_comm] using (lt_div_iff₀ hp).mp h

/-- The compact microscopic interface used by both tree profile statements.
For the directed first-order profile take C2=0. For the centered summed
profile C1 bounds its explicit first coefficient and C2 its uniform
second-order remainder. All factors, including the moving H_N, remain
in the exact equality. Analytic proofs of those profile estimates and
of the displayed factor limits remain explicit inputs. -/
theorem compact_microscopic_volume_transfer {α : Type*} [TopologicalSpace α]
    {K : Set α} {F A H error : ℕ → α → ℂ} {base : ℕ → ℂ}
    {a h : α → ℂ} {rate volume C1 C2 : ℝ}
    (hK : IsCompact K) (ha : ContinuousOn a K) (hh : ContinuousOn h K)
    (hane : ∀ s ∈ K, a s ≠ 0) (hhne : ∀ s ∈ K, h s ≠ 0)
    (hAlim : TendstoUniformlyOn A a atTop K)
    (hHlim : TendstoUniformlyOn H h atTop K)
    (hbase : ∀ᶠ N in atTop, base N ≠ 0)
    (hrate : Tendsto (fun N => Real.log ‖base N‖/(N : ℝ)) atTop (𝓝 rate))
    (hprofile : ∀ᶠ N in atTop, ∀ s ∈ K,
      F N s = (A N s * H N s) * base N * (1+error N s))
    (herror : ∀ᶠ N in atTop, ∀ s ∈ K,
      ‖error N s‖ ≤ C1/(N : ℝ)+C2/(N : ℝ)^2)
    (hvol : 2*Real.pi*rate = volume) :
    (∀ᶠ N in atTop, ∀ s ∈ K, F N s ≠ 0) ∧
      TendstoUniformlyOn (fun N s => 2*Real.pi*Real.log ‖F N s‖/(N : ℝ))
        (fun _ => volume) atTop K := by
  obtain ⟨al,au,hal,hau,hA⟩ := compact_moving_factor_bounds hK ha hane hAlim
  obtain ⟨hl,hu,hhl,hhu,hH⟩ := compact_moving_factor_bounds hK hh hhne hHlim
  exact microscopic_volume_transfer hal hau hhl hhu hbase hrate hprofile hA hH
    (uniform_vanishing_of_two_orders C1 C2 herror) hvol

end VolumeLogic.UniformProfile
