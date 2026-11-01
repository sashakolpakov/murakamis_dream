import VolumeLogic.RateComparison
import Mathlib.Analysis.Convex.Deriv
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
One-variable calculus behind Appendix P's shared-weight flattening.
Derivative hypotheses below concern actual real functions. Neither the
quadratic action cost nor the supporting-tangent gain is assumed.
Identifying these functions with geometric triangle potentials, their
Hessians and their stationary complete point remains a written input.
-/

namespace VolumeLogic.Flattening
open Set

/-- Convexity follows from the actual nonnegative second derivative on
the interval. Endpoint differentiability is a convenient stronger
hypothesis than the interior-only mean-value theorem requires. -/
theorem convex_on_Icc_of_second_nonneg {g dg ddg : ℝ → ℝ} {a b : ℝ}
    (hg : ∀ x ∈ Icc a b, HasDerivAt g (dg x) x)
    (hdg : ∀ x ∈ Icc a b, HasDerivAt dg (ddg x) x)
    (hddg : ∀ x ∈ Icc a b, 0 ≤ ddg x) :
    ConvexOn ℝ (Icc a b) g := by
  apply convexOn_of_hasDerivWithinAt2_nonneg (convex_Icc a b)
    (fun x hx => (hg x hx).continuousAt.continuousWithinAt)
    (fun x hx => (hg x (interior_subset hx)).hasDerivWithinAt)
    (fun x hx => (hdg x (interior_subset hx)).hasDerivWithinAt)
  exact fun x hx => hddg x (interior_subset hx)

/-- The supporting line at a stationary left endpoint is horizontal. -/
theorem stationary_convex_lower {g : ℝ → ℝ} {t : ℝ}
    (ht : 0 ≤ t) (hc : ConvexOn ℝ (Icc 0 t) g)
    (hg0 : HasDerivAt g 0 0) : 0 ≤ g t - g 0 := by
  rcases eq_or_lt_of_le ht with hzero | hpos
  · subst t
    simp
  · have hs := hc.le_slope_of_hasDerivAt
      (show (0 : ℝ) ∈ Icc 0 t from ⟨le_rfl, ht⟩)
      (show t ∈ Icc 0 t from ⟨ht, le_rfl⟩) hpos hg0
    rw [slope_def_field, sub_zero] at hs
    simpa using (le_div_iff₀ hpos).mp hs

/-- A stationary function with second derivative between zero and E
has action cost between zero and E*t^2/2. The upper bound is obtained
from convexity of E*x^2/2-g(x), not assumed as a Taylor estimate. -/
theorem stationary_quadratic_cost {g dg ddg : ℝ → ℝ} {t E : ℝ}
    (ht : 0 ≤ t)
    (hg : ∀ x ∈ Icc 0 t, HasDerivAt g (dg x) x)
    (hdg : ∀ x ∈ Icc 0 t, HasDerivAt dg (ddg x) x)
    (hzero : dg 0 = 0)
    (hlower : ∀ x ∈ Icc 0 t, 0 ≤ ddg x)
    (hupper : ∀ x ∈ Icc 0 t, ddg x ≤ E) :
    0 ≤ g t - g 0 ∧ g t - g 0 ≤ E * t ^ 2 / 2 := by
  have h0 : HasDerivAt g 0 0 := by
    simpa only [hzero] using hg 0 ⟨le_rfl, ht⟩
  have lower := stationary_convex_lower ht
    (convex_on_Icc_of_second_nonneg hg hdg hlower) h0
  let f : ℝ → ℝ := fun x => E * x ^ 2 / 2 - g x
  let df : ℝ → ℝ := fun x => E * x - dg x
  let ddf : ℝ → ℝ := fun x => E - ddg x
  have hf : ∀ x ∈ Icc 0 t, HasDerivAt f (df x) x := by
    intro x hx
    convert ((((hasDerivAt_id x).mul (hasDerivAt_id x)).const_mul E).div_const 2).sub (hg x hx)
      using 1 <;> first | rfl | (funext y; dsimp [f]; ring) | (dsimp [df]; ring)
  have hdf : ∀ x ∈ Icc 0 t, HasDerivAt df (ddf x) x := by
    intro x hx
    convert ((hasDerivAt_id x).const_mul E).sub (hdg x hx) using 1 <;>
      first | rfl | (dsimp [ddf]; ring)
  have hf0 : HasDerivAt f 0 0 := by
    simpa [df, hzero] using hf 0 ⟨le_rfl, ht⟩
  have upper := stationary_convex_lower ht
    (convex_on_Icc_of_second_nonneg hf hdf
      (fun x hx => sub_nonneg.mpr (hupper x hx))) hf0
  dsimp [f] at upper
  constructor
  · exact lower
  · nlinarith

/-- The common logarithmic-weight path; the same parameter changes every
ordinary coordinate. Protected coordinates are not part of this index set. -/
def weightPath {ι : Type*} (P : (ι → ℝ) → ℝ) (q : ι → ℝ) (t : ℝ) : ℝ :=
  P (fun i => (1 - t) * q i)

/-- Application of the calculus estimate to the actual shared path.
The directional derivative and Hessian hypotheses remain explicit. -/
theorem weight_path_cost {ι : Type*} (P : (ι → ℝ) → ℝ) (q : ι → ℝ)
    {dg ddg : ℝ → ℝ} {t E : ℝ} (ht : 0 ≤ t)
    (hg : ∀ x ∈ Icc 0 t, HasDerivAt (weightPath P q) (dg x) x)
    (hdg : ∀ x ∈ Icc 0 t, HasDerivAt dg (ddg x) x)
    (hzero : dg 0 = 0)
    (hlower : ∀ x ∈ Icc 0 t, 0 ≤ ddg x)
    (hupper : ∀ x ∈ Icc 0 t, ddg x ≤ E) :
    0 ≤ P (fun i => (1 - t) * q i) - P q ∧
      P (fun i => (1 - t) * q i) - P q ≤ E * t ^ 2 / 2 := by
  simpa [weightPath] using stationary_quadratic_cost ht hg hdg hzero hlower hupper

/-- Supporting-tangent inequality at the complete scale beta=1.
The quantity Q(1)-dQ is the entropy intercept in the application. -/
theorem convex_support_at_one {Q : ℝ → ℝ} {dQ β : ℝ}
    (hβ : β ∈ Icc (0 : ℝ) 1) (hc : ConvexOn ℝ (Icc 0 1) Q)
    (hd : HasDerivAt Q dQ 1) :
    β * Q 1 + (1 - β) * (Q 1 - dQ) ≤ Q β := by
  rcases eq_or_lt_of_le hβ.2 with heq | hlt
  · subst β
    simp
  · have hs := hc.slope_le_of_hasDerivAt hβ
      (show (1 : ℝ) ∈ Icc 0 1 from ⟨zero_le_one, le_rfl⟩) hlt hd
    rw [slope_def_field] at hs
    have hmul := (div_le_iff₀ (sub_pos.mpr hlt)).mp hs
    nlinarith

/-- The preceding estimate in the actual flattening parameter t=1-beta. -/
theorem convex_flattening_gain {Q : ℝ → ℝ} {dQ t : ℝ}
    (ht : t ∈ Icc (0 : ℝ) 1) (hc : ConvexOn ℝ (Icc 0 1) Q)
    (hd : HasDerivAt Q dQ 1) :
    (1 - t) * Q 1 + t * (Q 1 - dQ) ≤ Q (1 - t) := by
  have hβ : 1 - t ∈ Icc (0 : ℝ) 1 := ⟨by linarith [ht.2], by linarith [ht.1]⟩
  simpa only [sub_sub_cancel] using convex_support_at_one hβ hc hd

/-- The actual two branches of a surviving one-sided local envelope.
`Qk` is the retained triangle and `Qo` the overloaded triangle. The defect
is constructed as max(0,z-Qk(1)-Qo(1)), rather than supplied as a loss
bound. The pure-corner and entropy hypotheses are written source inputs. -/
theorem side_loss_from_convexity {Qk Qo : ℝ → ℝ} {dk dover t z : ℝ}
    (ht : t ∈ Icc (0 : ℝ) 1)
    (hck : ConvexOn ℝ (Icc 0 1) Qk) (hco : ConvexOn ℝ (Icc 0 1) Qo)
    (hdk : HasDerivAt Qk dk 1) (hdo : HasDerivAt Qo dover 1)
    (hentropy : 0 ≤ Qk 1 - dk) (hpure : z / 2 ≤ Qo 1) :
    t * (Qo 1 - dover) - (1 - t) * max 0 (z - (Qk 1 + Qo 1)) ≤
      Qk (1 - t) + Qo (1 - t) -
        max ((1 - t) * z) (Qk (1 - t) + (1 - t) * z / 2) := by
  have hk := convex_flattening_gain ht hck hdk
  have ho := convex_flattening_gain ht hco hdo
  have hβ : 0 ≤ 1 - t := sub_nonneg.mpr ht.2
  have hke := mul_nonneg ht.1 hentropy
  have hsum : (1 - t) * (Qk 1 + Qo 1) + t * (Qo 1 - dover) ≤
      Qk (1 - t) + Qo (1 - t) := by nlinarith
  have hdef := mul_le_mul_of_nonneg_left
    (le_max_right (0 : ℝ) (z - (Qk 1 + Qo 1))) hβ
  have hdef0 := mul_nonneg hβ (le_max_left (0 : ℝ) (z - (Qk 1 + Qo 1)))
  have hpure0 := mul_nonneg hβ (sub_nonneg.mpr hpure)
  have hfirst : t * (Qo 1 - dover) - (1 - t) * max 0 (z - (Qk 1 + Qo 1)) ≤
      Qk (1 - t) + Qo (1 - t) - (1 - t) * z := by nlinarith
  have hsecond : t * (Qo 1 - dover) - (1 - t) * max 0 (z - (Qk 1 + Qo 1)) ≤
      Qo (1 - t) - (1 - t) * z / 2 := by nlinarith
  have hmax : max ((1 - t) * z) (Qk (1 - t) + (1 - t) * z / 2) ≤
      Qk (1 - t) + Qo (1 - t) -
        (t * (Qo 1 - dover) - (1 - t) * max 0 (z - (Qk 1 + Qo 1))) :=
    max_le (by linarith) (by linarith)
  linarith

/-- The calculus cost and the two-branch convex gain imply a strict
rate margin. Additional actual nonnegative local losses can be kept in
the same finite sector via the existing Std-only sum theorem. -/
theorem flattening_sector_gap {g dg ddg Qk Qo : ℝ → ℝ}
    {dk dover t z E : ℝ} (others : List ℝ)
    (ht : t ∈ Icc (0 : ℝ) 1)
    (hg : ∀ x ∈ Icc 0 t, HasDerivAt g (dg x) x)
    (hdg : ∀ x ∈ Icc 0 t, HasDerivAt dg (ddg x) x)
    (hzero : dg 0 = 0)
    (hlower : ∀ x ∈ Icc 0 t, 0 ≤ ddg x)
    (hupper : ∀ x ∈ Icc 0 t, ddg x ≤ E)
    (hck : ConvexOn ℝ (Icc 0 1) Qk) (hco : ConvexOn ℝ (Icc 0 1) Qo)
    (hdk : HasDerivAt Qk dk 1) (hdo : HasDerivAt Qo dover 1)
    (hentropy : 0 ≤ Qk 1 - dk) (hpure : z / 2 ≤ Qo 1)
    (hothers : ∀ x ∈ others, 0 ≤ x)
    (hmargin : E * t ^ 2 / 2 <
      t * (Qo 1 - dover) - (1 - t) * max 0 (z - (Qk 1 + Qo 1))) :
    g t - (Qk (1 - t) + Qo (1 - t) -
      max ((1 - t) * z) (Qk (1 - t) + (1 - t) * z / 2) +
      VolumeLogic.total others) < g 0 := by
  have hcost := (stationary_quadratic_cost ht.1 hg hdg hzero hlower hupper).2
  have hloss := side_loss_from_convexity ht hck hco hdk hdo hentropy hpure
  have hsum := VolumeLogic.total_nonnegative others hothers
  linarith

/-- Under zero defect the existing strict scalar criterion is now joined
to the derived calculus bounds, rather than to assumed cost/gain bounds. -/
theorem weak_balance_sector_gap {g dg ddg Qk Qo : ℝ → ℝ}
    {dk dover t z E : ℝ} (others : List ℝ)
    (ht : 0 < t) (ht1 : t ≤ 1)
    (hg : ∀ x ∈ Icc 0 t, HasDerivAt g (dg x) x)
    (hdg : ∀ x ∈ Icc 0 t, HasDerivAt dg (ddg x) x)
    (hzero : dg 0 = 0)
    (hlower : ∀ x ∈ Icc 0 t, 0 ≤ ddg x)
    (hupper : ∀ x ∈ Icc 0 t, ddg x ≤ E)
    (hck : ConvexOn ℝ (Icc 0 1) Qk) (hco : ConvexOn ℝ (Icc 0 1) Qo)
    (hdk : HasDerivAt Qk dk 1) (hdo : HasDerivAt Qo dover 1)
    (hentropy : 0 ≤ Qk 1 - dk) (hpure : z / 2 ≤ Qo 1)
    (hover : 0 < Qo 1 - dover) (hbalance : z ≤ Qk 1 + Qo 1)
    (hsmall : t * E ≤ Qo 1 - dover)
    (hothers : ∀ x ∈ others, 0 ≤ x) :
    g t - (Qk (1 - t) + Qo (1 - t) -
      max ((1 - t) * z) (Qk (1 - t) + (1 - t) * z / 2) +
      VolumeLogic.total others) < g 0 := by
  have hgain := VolumeLogic.strict_weak_balance_gain t (Qo 1 - dover) E ht hover hsmall
  apply flattening_sector_gap others ⟨ht.le, ht1⟩ hg hdg hzero hlower hupper
    hck hco hdk hdo hentropy hpure hothers
  rw [max_eq_left (sub_nonpos.mpr hbalance)]
  nlinarith

end VolumeLogic.Flattening
