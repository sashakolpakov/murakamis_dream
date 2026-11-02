import Mathlib.Analysis.Normed.Module.FiniteDimension
import Mathlib.Topology.Order.Compact
import Mathlib.Topology.Order.Lattice
import Mathlib.Algebra.Order.GroupWithZero.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Coercivity of a finite supported transport potential. Row supports and positive
corner loads are actual finite data; demands are their column sums. Connectivity
uses finite co-occurrence paths. No uniform recession margin is assumed.
Hall feasibility, geometric support and the triangle vertex bound remain written.
-/
namespace VolumeLogic.TransportCoercivity
open Set
open scoped BigOperators
variable {V T : Type*} [Fintype V] [Fintype T]

/-- Supply of one row of the actual supported table. -/
noncomputable def rowMass (S : T → Finset V) (α : T → V → ℝ) (t : T) : ℝ :=
  ∑ i ∈ S t, α t i

/-- Demands are column sums, including boundary columns. -/
noncomputable def demand (S : T → Finset V) (α : T → V → ℝ) (i : V) : ℝ := by
  classical
  exact ∑ t, if i ∈ S t then α t i else 0

/-- Every row support must be nonempty. -/
noncomputable def rowMax (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (h : V → ℝ) (t : T) : ℝ := (S t).sup' (hne t) h

/-- The actual maximum-minus-linear recession with its constructed demands. -/
noncomputable def recession (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (h : V → ℝ) : ℝ :=
  (∑ t, rowMass S α t * rowMax S hne h t) - ∑ i, demand S α i * h i

/-- A graph step joins two supported corners in the same actual row. -/
def rowStep (S : T → Finset V) (u v : V) : Prop :=
  ∃ t, u ∈ S t ∧ v ∈ S t

/-- Connectivity means finite paths of row co-occurrences. -/
def connected (S : T → Finset V) : Prop :=
  ∀ u v, Relation.ReflTransGen (rowStep S) u v

theorem sum_demand (S : T → Finset V) (α : T → V → ℝ) (h : V → ℝ) :
    (∑ i, demand S α i * h i) = ∑ t, ∑ i ∈ S t, α t i * h i := by
  classical
  simp only [demand, Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t _
  simp [ite_mul]

/-- Feasibility rewrites the recession as a sum of supported gaps. -/
theorem recession_eq_gaps (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (h : V → ℝ) :
    recession S hne α h =
      ∑ t, ∑ i ∈ S t, α t i * (rowMax S hne h t - h i) := by
  rw [recession, sum_demand, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro t _
  simp only [rowMass, Finset.sum_mul, ← Finset.sum_sub_distrib, mul_sub]

theorem recession_nonneg (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 ≤ α t i) (h : V → ℝ) :
    0 ≤ recession S hne α h := by
  rw [recession_eq_gaps]
  apply Finset.sum_nonneg
  intro t _
  apply Finset.sum_nonneg
  intro i hi
  exact mul_nonneg (hα t i hi) (sub_nonneg.mpr (Finset.le_sup' h hi))

/-- Zero recession forces every supported value to its row maximum. -/
theorem recession_zero_iff (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i) (h : V → ℝ) :
    recession S hne α h = 0 ↔
      ∀ t i, i ∈ S t → h i = rowMax S hne h t := by
  have hp : ∀ t i, i ∈ S t → 0 ≤ α t i * (rowMax S hne h t - h i) :=
    fun t i hi => mul_nonneg (hα t i hi).le (sub_nonneg.mpr (Finset.le_sup' h hi))
  rw [recession_eq_gaps, Finset.sum_eq_zero_iff_of_nonneg
    (fun t _ => Finset.sum_nonneg (fun i hi => hp t i hi))]
  constructor
  · intro hz t i hi
    have hr := (Finset.sum_eq_zero_iff_of_nonneg (fun i hi => hp t i hi)).mp
      (hz t (Finset.mem_univ t))
    have hd := (mul_eq_zero.mp (hr i hi)).resolve_left (ne_of_gt (hα t i hi))
    exact (sub_eq_zero.mp hd).symm
  · intro he t _
    apply Finset.sum_eq_zero
    intro i hi
    rw [he t i hi, sub_self, mul_zero]

/-- Equality propagates along a finite co-occurrence path. -/
theorem equal_of_row_path (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (h : V → ℝ) (hz : recession S hne α h = 0)
    {u v : V} (path : Relation.ReflTransGen (rowStep S) u v) : h u = h v := by
  have he := (recession_zero_iff S hne α hα h).mp hz
  induction path with
  | refl => rfl
  | tail _ step ih =>
    obtain ⟨t, hu, hv⟩ := step
    exact ih.trans ((he t _ hu).trans (he t _ hv).symm)

theorem recession_zero (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) : recession S hne α (0 : V → ℝ) = 0 := by
  simp [recession, rowMax]

/-- Grounding removes the constant zero direction, even for one vertex. -/
theorem grounded_recession_pos (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : connected S) (root : V) (h : V → ℝ)
    (ground : h root = 0) (nonzero : h ≠ 0) : 0 < recession S hne α h := by
  have hn := recession_nonneg S hne α (fun t i hi => (hα t i hi).le) h
  apply lt_of_le_of_ne hn
  intro hz
  apply nonzero
  funext i
  exact (equal_of_row_path S hne α hα h hz.symm (hc i root)).trans ground

/-- Finite maxima and sums make the actual recession continuous. -/
theorem continuous_recession (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) : Continuous (recession S hne α) := by
  unfold recession
  apply Continuous.sub
  · apply continuous_finsetSum
    intro t _
    exact continuous_const.mul (Continuous.finset_sup'_apply (hne t)
      (fun i _ => continuous_apply i))
  · apply continuous_finsetSum
    intro i _
    exact continuous_const.mul (continuous_apply i)

/-- Positive homogeneity uses the same support and table. -/
theorem recession_smul (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (h : V → ℝ) {c : ℝ} (hc : 0 ≤ c) :
    recession S hne α (c • h) = c * recession S hne α h := by
  have hm : ∀ t, rowMax S hne (c • h) t = c * rowMax S hne h t := by
    intro t
    exact (Finset.mul₀_sup' hc h (S t) (hne t)).symm
  simp only [recession, hm, Pi.smul_apply, smul_eq_mul]
  simp_rw [mul_sub, Finset.mul_sum]
  congr 1 <;> apply Finset.sum_congr rfl <;> intro i _ <;> ring

/-- The grounded unit sphere is compact, and its strict positive minimum gives
a uniform bound. `exists_forall_le'` also covers the empty sphere: in that case
it selects any positive constant. Thus this statement includes a one-vertex
graph, whose only grounded direction is zero. -/
theorem grounded_recession_coercive
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : connected S) (root : V) :
    ∃ c : ℝ, 0 < c ∧ ∀ h : V → ℝ, h root = 0 →
      c * ‖h‖ ≤ recession S hne α h := by
  let U : Set (V → ℝ) := {h | h root = 0} ∩ Metric.sphere 0 1
  have hU : IsCompact U :=
    (isCompact_sphere (0 : V → ℝ) 1).inter_left
      (isClosed_eq (continuous_apply root) continuous_const)
  have hpos : ∀ h ∈ U, 0 < recession S hne α h := by
    intro h hh
    apply grounded_recession_pos S hne α hα hc root h hh.1
    intro hz
    have hs := hh.2
    simp [hz] at hs
  obtain ⟨c, hcpos, hmin⟩ := hU.exists_forall_le'
    (continuous_recession S hne α).continuousOn hpos
  refine ⟨c, hcpos, ?_⟩
  intro h ground
  by_cases hz : h = 0
  · simp [hz, recession_zero]
  have hn : 0 < ‖h‖ := norm_pos_iff.mpr hz
  have hu : ‖h‖⁻¹ • h ∈ U := by
    constructor
    · simp [ground]
    · rw [Metric.mem_sphere, dist_zero_right]
      rw [norm_smul_of_nonneg (inv_nonneg.mpr hn.le)]
      exact inv_mul_cancel₀ hn.ne'
  have hl := mul_le_mul_of_nonneg_left (hmin _ hu) hn.le
  rw [recession_smul S hne α h (inv_nonneg.mpr hn.le)] at hl
  have cancel : ‖h‖ * (‖h‖⁻¹ * recession S hne α h) =
      recession S hne α h := by
    rw [← mul_assoc, mul_inv_cancel₀ hn.ne', one_mul]
  rw [cancel, mul_comm ‖h‖ c] at hl
  exact hl

/-- The potential uses the actual demands computed from the same corner table. -/
noncomputable def potential (S : T → Finset V) (α : T → V → ℝ)
    (Q : T → (V → ℝ) → ℝ) (h : V → ℝ) : ℝ :=
  (∑ t, Q t h) - ∑ i, demand S α i * h i

/-- Local vertex lower bounds give the exact global recession lower bound;
fixed boundary offsets may be included in the row constants `C`. -/
theorem recession_sub_le_potential
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, rowMass S α t * rowMax S hne h t - C t ≤ Q t h)
    (h : V → ℝ) :
    recession S hne α h - ∑ t, C t ≤ potential S α Q h := by
  have hs := Finset.sum_le_sum (s := Finset.univ) (fun t _ => hQ t h)
  simp only [Finset.sum_sub_distrib] at hs
  unfold recession potential
  linarith

/-- A genuine uniform coercive lower bound for the actual potential. -/
theorem grounded_potential_coercive
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : connected S) (root : V)
    (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, rowMass S α t * rowMax S hne h t - C t ≤ Q t h) :
    ∃ c : ℝ, 0 < c ∧ ∀ h : V → ℝ, h root = 0 →
      c * ‖h‖ - ∑ t, C t ≤ potential S α Q h := by
  obtain ⟨c, hcp, hcr⟩ := grounded_recession_coercive S hne α hα hc root
  refine ⟨c, hcp, ?_⟩
  intro h ground
  have hr := hcr h ground
  have hpot := recession_sub_le_potential S hne α Q C hQ h
  linarith

theorem continuous_potential (S : T → Finset V) (α : T → V → ℝ)
    (Q : T → (V → ℝ) → ℝ) (hQ : ∀ t, Continuous (Q t)) :
    Continuous (potential S α Q) := by
  unfold potential
  apply Continuous.sub
  · exact continuous_finsetSum _ (fun t _ => hQ t)
  · exact continuous_finsetSum _
      (fun i _ => continuous_const.mul (continuous_apply i))

/-- Every grounded sublevel of the constructed potential is bounded. -/
theorem grounded_sublevel_bounded
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : connected S) (root : V)
    (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, rowMass S α t * rowMax S hne h t - C t ≤ Q t h)
    (M : ℝ) :
    Bornology.IsBounded {h : V → ℝ | h root = 0 ∧ potential S α Q h ≤ M} := by
  obtain ⟨c, hcp, hcr⟩ := grounded_potential_coercive S hne α hα hc root Q C hQ
  rw [Metric.isBounded_iff_subset_closedBall (0 : V → ℝ)]
  refine ⟨(M + ∑ t, C t) / c, ?_⟩
  intro h hh
  rw [Metric.mem_closedBall, dist_zero_right]
  apply (le_div_iff₀ hcp).mpr
  have hr := hcr h hh.1
  linarith [hh.2]

/-- A continuous potential has compact grounded sublevels. -/
theorem grounded_sublevel_compact
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : connected S) (root : V)
    (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, rowMass S α t * rowMax S hne h t - C t ≤ Q t h)
    (hcont : ∀ t, Continuous (Q t)) (M : ℝ) :
    IsCompact {h : V → ℝ | h root = 0 ∧ potential S α Q h ≤ M} := by
  apply Metric.isCompact_of_isClosed_isBounded
  · exact (isClosed_eq (continuous_apply root) continuous_const).inter
      (isClosed_le (continuous_potential S α Q hcont) continuous_const)
  · exact grounded_sublevel_bounded S hne α hα hc root Q C hQ M

/-- The finite transport lower bound supplies an actual grounded minimizer;
neither a minimizer nor a uniform recession margin is assumed. -/
theorem exists_grounded_minimizer
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : connected S) (root : V)
    (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, rowMass S α t * rowMax S hne h t - C t ≤ Q t h)
    (hcont : ∀ t, Continuous (Q t)) :
    ∃ h : V → ℝ, h root = 0 ∧
      ∀ k : V → ℝ, k root = 0 → potential S α Q h ≤ potential S α Q k := by
  let K : Set (V → ℝ) := {h | h root = 0 ∧ potential S α Q h ≤ potential S α Q 0}
  have hk : IsCompact K :=
    grounded_sublevel_compact S hne α hα hc root Q C hQ hcont _
  have h0 : (0 : V → ℝ) ∈ K := ⟨rfl, le_rfl⟩
  obtain ⟨h, hh, hm⟩ := hk.exists_isMinOn ⟨0, h0⟩
    (continuous_potential S α Q hcont).continuousOn
  refine ⟨h, hh.1, ?_⟩
  intro k ground
  by_cases hle : potential S α Q k ≤ potential S α Q 0
  · exact hm ⟨ground, hle⟩
  · exact hh.2.trans (le_of_not_ge hle)

end VolumeLogic.TransportCoercivity
