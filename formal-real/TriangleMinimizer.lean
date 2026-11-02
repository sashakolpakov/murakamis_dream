import TrianglePotential
import GroundedConvexity

/-!
The actual supported triangle potential has a unique grounded minimum from
an explicitly positive half-mass corner table and actual row paths. Fixed
boundary offsets stay in the corner coefficients; coincident vertices are
aggregated only in the transport table. Hall existence and the geometric
incidence/development remain application inputs.
-/
namespace VolumeLogic.TriangleMinimizer
open scoped BigOperators
open Set
open TriangleLoads TrianglePotential

/-- A regular row has at least two distinct positive corner coefficients. -/
def Regular (a : Fin 3 → ℝ) : Prop :=
  ∃ i j, i ≠ j ∧ 0 < a i ∧ 0 < a j

theorem regular_radicand (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hr : Regular a) : 0 < radicand (weights a q) := by
  obtain ⟨i,j,hij,hi,hj⟩ := hr
  exact radicand_pos_of_positive_pair _ (weights_nonneg a q ha) i j hij
    ((weights_pos_iff a q i).mpr hi) ((weights_pos_iff a q j).mpr hj)

theorem nonregular_singleton (a : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hr : ¬ Regular a) (i : Fin 3) (hi : 0 < a i) :
    ∀ j, j ≠ i → a j = 0 := by
  intro j hji
  have hn : ¬ 0 < a j := fun hj => hr ⟨i,j,Ne.symm hji,hi,hj⟩
  exact le_antisymm (le_of_not_gt hn) (ha j)

/-- The existing explicit maximizer also supplies a bounded attained
supremum uniformly across the two fixed-support cases. -/
theorem potential_attained (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) :
    ∃ α, Feasible a α ∧ potential a q = objective a q α ∧
      ∀ β, Feasible a β → objective a q β ≤ potential a q := by
  by_cases hr : Regular a
  · have hs := regular_radicand a q ha hr
    refine ⟨load a q, loads_feasible a q ha hs, potential_eq_loads a q ha hs, ?_⟩
    intro β hβ
    rw [potential_eq_loads a q ha hs]
    exact objective_le_loads a q β ha hs hβ
  · obtain ⟨i,hi⟩ := hne
    have hz := nonregular_singleton a ha hr i hi
    refine ⟨singletonLoad i q, singleton_feasible a q i hi, ?_, ?_⟩
    · rw [potential_singleton a q i hi hz, objective_singleton a q i hi]
    · intro β hβ
      rw [feasible_singleton_unique a q β i hz hβ, objective_singleton a q i hi,
        potential_singleton a q i hi hz]

theorem potential_vertex_lower (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (i : Fin 3) (hi : 0 < a i) :
    (Real.log (a i) + q i) / 2 ≤ potential a q := by
  obtain ⟨α,_,_,hb⟩ := potential_attained a q ha ⟨i,hi⟩
  simpa only [objective_singleton a q i hi] using
    hb (singletonLoad i q) (singleton_feasible a q i hi)

theorem objective_difference (a q p α : Fin 3 → ℝ) (hf : Feasible a α) :
    objective a q α - objective a p α = ∑ i, α i * (q i - p i) := by
  rw [objective, objective, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  by_cases hi : a i = 0
  · simp [hf.2.2 i hi]
  · simp only [logWeight, if_neg hi]
    ring

theorem objective_difference_le (a q p α : Fin 3 → ℝ) (hf : Feasible a α) :
    objective a q α - objective a p α ≤ ‖q-p‖ / 2 := by
  rw [objective_difference a q p α hf]
  calc
    (∑ i, α i * (q i-p i)) ≤ ∑ i, α i * ‖q-p‖ := by
      apply Finset.sum_le_sum
      intro i _
      apply mul_le_mul_of_nonneg_left _ (hf.1 i)
      have hi := norm_le_pi_norm (q-p) i
      rw [Real.norm_eq_abs, Pi.sub_apply] at hi
      exact (le_abs_self _).trans hi
    _ = ‖q-p‖ / 2 := by rw [← Finset.sum_mul, hf.2.1]; ring

/-- Multivariate fixed-support continuity is proved via the actual maximum,
not inferred from the existence of derivatives along individual lines. -/
theorem potential_lipschitz (a : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) : LipschitzWith (1/2) (potential a) := by
  apply LipschitzWith.of_dist_le_mul
  intro q p
  have oneSide : ∀ q p, potential a q - potential a p ≤ ‖q-p‖ / 2 := by
    intro q p
    obtain ⟨α,hα,heq,_⟩ := potential_attained a q ha hne
    obtain ⟨_,_,_,hb⟩ := potential_attained a p ha hne
    have hl := objective_difference_le a q p α hα
    have hu := hb α hα
    rw [heq]
    linarith
  have hp := oneSide q p
  have hq := oneSide p q
  rw [norm_sub_rev] at hq
  rw [Real.dist_eq, dist_eq_norm]
  norm_num only [NNReal.coe_div, NNReal.coe_one, NNReal.coe_ofNat]
  rw [abs_sub_le_iff]
  constructor <;> nlinarith

theorem potential_continuous (a : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) : Continuous (potential a) :=
  (potential_lipschitz a ha hne).continuous

variable {T V : Type*}

/-- Active corners are retained before their vertex images are taken. -/
noncomputable def support (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (t : T) : Finset V := by
  classical
  exact (Finset.univ.filter (fun i => 0 < a t i)).image (c t)

/-- Only the corner table is aggregated at coincident vertex destinations. -/
noncomputable def aggregate (c : T → Fin 3 → V) (β : T → Fin 3 → ℝ)
    (t : T) (v : V) : ℝ := by
  classical
  exact ∑ i, if c t i = v then β t i else 0

noncomputable def column [Fintype T] (c : T → Fin 3 → V) (β : T → Fin 3 → ℝ)
    (v : V) : ℝ := ∑ t, aggregate c β t v

/-- An explicit harmless bound for all fixed corner offsets in one row. -/
noncomputable def offsetCost (a : T → Fin 3 → ℝ) (t : T) : ℝ :=
  (∑ i, if 0 < a t i then |Real.log (a t i)| else 0) / 2

theorem mem_support (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (t : T) (v : V) :
    v ∈ support c a t ↔ ∃ i, 0 < a t i ∧ c t i = v := by
  classical
  simp [support]

theorem support_nonempty (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (hne : ∀ t, ∃ i, 0 < a t i) (t : T) : (support c a t).Nonempty := by
  obtain ⟨i,hi⟩ := hne t
  exact ⟨c t i, (mem_support c a t _).mpr ⟨i,hi,rfl⟩⟩

theorem aggregate_nonneg (c : T → Fin 3 → V) (β : T → Fin 3 → ℝ)
    (hβ : ∀ t i, 0 ≤ β t i) (t : T) (v : V) : 0 ≤ aggregate c β t v := by
  classical
  apply Finset.sum_nonneg
  intro i _
  split_ifs <;> simp_all

theorem aggregate_positive (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ)
    (hn : ∀ t i, 0 ≤ β t i) (hp : ∀ t i, 0 < a t i → 0 < β t i)
    (t : T) (v : V) (hv : v ∈ support c a t) : 0 < aggregate c β t v := by
  classical
  obtain ⟨i,hi,hc⟩ := (mem_support c a t v).mp hv
  have hl : β t i ≤ aggregate c β t v := by
    unfold aggregate
    convert! Finset.single_le_sum
      (s := Finset.univ) (f := fun j => if c t j = v then β t j else 0)
      (fun j _ => by split_ifs <;> simp_all) (Finset.mem_univ i) using 1
    simp only [hc, ite_true]
  exact (hp t i hi).trans_le hl

theorem aggregate_zero_outside (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0) (t : T) (v : V)
    (hv : v ∉ support c a t) : aggregate c β t v = 0 := by
  classical
  apply Finset.sum_eq_zero
  intro i _
  by_cases hc : c t i = v
  · have hi : ¬ 0 < a t i := fun hi => hv ((mem_support c a t v).mpr ⟨i,hi,hc⟩)
    simp [hc, hz t i hi]
  · simp [hc]

theorem table_nonneg (a β : T → Fin 3 → ℝ)
    (hp : ∀ t i, 0 < a t i → 0 < β t i)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0) : ∀ t i, 0 ≤ β t i := by
  intro t i
  by_cases hi : 0 < a t i
  · exact (hp t i hi).le
  · rw [hz t i hi]

theorem table_support_nonempty (a β : T → Fin 3 → ℝ)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0)
    (hm : ∀ t, (∑ i, β t i) = 1/2) : ∀ t, ∃ i, 0 < a t i := by
  intro t
  by_contra hn
  have hall : ∀ i, β t i = 0 := fun i => hz t i (fun hi => hn ⟨i,hi⟩)
  have hh := hm t
  simp only [hall, Finset.sum_const_zero] at hh
  norm_num at hh

theorem aggregate_sum [Fintype V] (c : T → Fin 3 → V) (β : T → Fin 3 → ℝ) (t : T) :
    (∑ v, aggregate c β t v) = ∑ i, β t i := by
  classical
  unfold aggregate
  rw [Finset.sum_comm]
  simp

theorem aggregate_rowMass [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0) (t : T) :
    TransportCoercivity.rowMass (support c a) (aggregate c β) t = ∑ i, β t i := by
  classical
  calc
    TransportCoercivity.rowMass (support c a) (aggregate c β) t =
        ∑ v, aggregate c β t v := by
      apply Finset.sum_subset (Finset.subset_univ _)
      intro v _ hv
      exact aggregate_zero_outside c a β hz t v hv
    _ = ∑ i, β t i := aggregate_sum c β t

theorem aggregate_demand [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0) :
    TransportCoercivity.demand (support c a) (aggregate c β) = column c β := by
  classical
  funext v
  unfold TransportCoercivity.demand column
  apply Finset.sum_congr rfl
  intro t _
  by_cases hv : v ∈ support c a t
  · simp [hv]
  · simp [hv, aggregate_zero_outside c a β hz t v hv]

theorem transport_potential_eq [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0) :
    TransportCoercivity.potential (support c a) (aggregate c β)
      (fun t q => potential (a t) (fun i => q (c t i))) =
    summedPotential c a (column c β) := by
  funext q
  simp only [TransportCoercivity.potential, aggregate_demand c a β hz, summedPotential]

/-- Fixed offsets remain in separate corner coefficients even if several
corners share a vertex. The bound is for the original row supremum. -/
theorem row_vertex_lower [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0)
    (hm : ∀ t, (∑ i, β t i) = 1/2) (t : T) (q : V → ℝ) :
    TransportCoercivity.rowMass (support c a) (aggregate c β) t *
      TransportCoercivity.rowMax (support c a) (support_nonempty c a hne) q t -
      offsetCost a t ≤ potential (a t) (fun i => q (c t i)) := by
  classical
  obtain ⟨v,hv,hmax⟩ := Finset.exists_mem_eq_sup' (support_nonempty c a hne t) q
  obtain ⟨i,hi,hc⟩ := (mem_support c a t v).mp hv
  have hl := potential_vertex_lower (a t) (fun i => q (c t i)) (ha t) i hi
  have hb : |Real.log (a t i)| ≤ ∑ j, if 0 < a t j then |Real.log (a t j)| else 0 := by
    simpa only [if_pos hi] using Finset.single_le_sum
      (s := Finset.univ) (f := fun j => if 0 < a t j then |Real.log (a t j)| else 0)
      (fun j _ => by split_ifs <;> positivity) (Finset.mem_univ i)
  rw [aggregate_rowMass c a β hz, hm]
  change 1/2 * (support c a t).sup' _ q - offsetCost a t ≤ _
  rw [hmax, ← hc]
  unfold offsetCost
  linarith [neg_abs_le (Real.log (a t i))]

/-- Three pair labels contain every unordered pair of distinct corners. -/
theorem corner_pair_covered (i j : Fin 3) (hij : i ≠ j) :
    ∃ e : Fin 3, (edgeSrc e = i ∧ edgeDst e = j) ∨
      (edgeSrc e = j ∧ edgeDst e = i) := by
  fin_cases i <;> fin_cases j <;> simp_all [edgeSrc, edgeDst]
  all_goals decide

noncomputable def edgeWeight (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (q : V → ℝ) (e : T × Fin 3) : ℝ := by
  classical
  exact if Regular (a e.1) then conductance
    (weights (a e.1) (fun i => q (c e.1 i))) (edgeSrc e.2) (edgeDst e.2) else 0

theorem edgeWeight_nonneg (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (q : V → ℝ) (e : T × Fin 3) :
    0 ≤ edgeWeight c a q e := by
  classical
  unfold edgeWeight
  split_ifs
  · exact conductance_nonneg _ (weights_nonneg _ _ (ha e.1)) _ _
  · exact le_rfl

theorem row_step_positive_path (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (q : V → ℝ) {u v : V}
    (hstep : TransportCoercivity.rowStep (support c a) u v) :
    Relation.ReflTransGen (WeightedGraph.positiveStep
      (fun e : T × Fin 3 => c e.1 (edgeSrc e.2))
      (fun e : T × Fin 3 => c e.1 (edgeDst e.2)) (edgeWeight c a q)) u v := by
  classical
  by_cases huv : u = v
  · subst v
    exact Relation.ReflTransGen.refl
  obtain ⟨t,hu,hv⟩ := hstep
  obtain ⟨i,hi,hci⟩ := (mem_support c a t u).mp hu
  obtain ⟨j,hj,hcj⟩ := (mem_support c a t v).mp hv
  have hij : i ≠ j := by rintro rfl; exact huv (hci.symm.trans hcj)
  have hr : Regular (a t) := ⟨i,j,hij,hi,hj⟩
  obtain ⟨e,he | he⟩ := corner_pair_covered i j hij
  · apply Relation.ReflTransGen.single
    refine ⟨(t,e), ?_, Or.inl ?_⟩
    · simp only [edgeWeight, if_pos hr, he.1, he.2]
      exact conductance_pos _ (regular_radicand _ _ (ha t) hr) i j
        ((weights_pos_iff _ _ i).mpr hi) ((weights_pos_iff _ _ j).mpr hj)
    · simpa only [he.1, he.2] using And.intro hci hcj
  · apply Relation.ReflTransGen.single
    refine ⟨(t,e), ?_, Or.inr ?_⟩
    · simp only [edgeWeight, if_pos hr, he.1, he.2]
      exact conductance_pos _ (regular_radicand _ _ (ha t) hr) j i
        ((weights_pos_iff _ _ j).mpr hj) ((weights_pos_iff _ _ i).mpr hi)
    · simpa only [he.1, he.2] using And.intro hcj hci

theorem conductance_connected_of_rows (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hc : TransportCoercivity.connected (support c a))
    (q : V → ℝ) : WeightedGraph.connected
      (fun e : T × Fin 3 => c e.1 (edgeSrc e.2))
      (fun e : T × Fin 3 => c e.1 (edgeDst e.2)) (edgeWeight c a q) := by
  intro u v
  have hp := hc u v
  induction hp with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih => exact ih.trans (row_step_positive_path c a ha q hstep)

/-- Reparametrization of the original common-vertex affine path. -/
theorem affine_eq_segment (x y : V → ℝ) (u : ℝ) :
    (fun j => x j + u * (y-x) j) = GroundedConvexity.segment x y u := by
  funext j
  simp only [GroundedConvexity.segment, Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
  ring

/-- The actual first derivative on every segment, not an assumed gradient. -/
theorem summedPotential_segment_hasDerivAt [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (x y : V → ℝ) (u : ℝ) :
    HasDerivAt (GroundedConvexity.segmentValue (summedPotential c a d) x y)
      (deriv (GroundedConvexity.segmentValue (summedPotential c a d) x y) u) u := by
  classical
  let active : T → Fin 3 := fun t => Classical.choose (hne t)
  have hp : ∀ t, 0 < a t (active t) := fun t => Classical.choose_spec (hne t)
  have hd := summedPotential_mixed_hasDerivAt c a d x (y-x)
    (fun t => Regular (a t)) active ha
    (fun t hr => regular_radicand _ _ (ha t) hr)
    (fun t hr => ⟨hp t, nonregular_singleton (a t) (ha t) hr (active t) (hp t)⟩) u
  have heq : (fun v : ℝ => summedPotential c a d (fun j => x j + v * (y-x) j)) =
      GroundedConvexity.segmentValue (summedPotential c a d) x y := by
    funext v
    rw [affine_eq_segment]
    rfl
  rw [heq] at hd
  exact hd.differentiableAt.hasDerivAt

/-- The true second derivative has the same fixed support conductance graph,
including zero Hessian rows for actual singleton triangles. -/
theorem summedPotential_segment_second [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (x y : V → ℝ) (u : ℝ) :
    HasDerivAt (deriv (GroundedConvexity.segmentValue (summedPotential c a d) x y))
      (WeightedGraph.energy
        (fun e : T × Fin 3 => c e.1 (edgeSrc e.2))
        (fun e : T × Fin 3 => c e.1 (edgeDst e.2))
        (edgeWeight c a (GroundedConvexity.segment x y u)) (y-x)) u := by
  classical
  let active : T → Fin 3 := fun t => Classical.choose (hne t)
  have hp : ∀ t, 0 < a t (active t) := fun t => Classical.choose_spec (hne t)
  have hd := summedPotential_mixed_second_at c a d x (y-x)
    (fun t => Regular (a t)) active ha
    (fun t hr => regular_radicand _ _ (ha t) hr)
    (fun t hr => ⟨hp t, nonregular_singleton (a t) (ha t) hr (active t) (hp t)⟩) u
  have heq : (fun v : ℝ => summedPotential c a d (fun j => x j + v * (y-x) j)) =
      GroundedConvexity.segmentValue (summedPotential c a d) x y := by
    funext v
    rw [affine_eq_segment]
    rfl
  rw [heq] at hd
  convert! hd using 1
  congr 1
  funext e
  unfold edgeWeight
  congr 1
  congr 1
  congr 1
  funext i
  have he := congrFun (affine_eq_segment x y u) (c e.1 i)
  exact he.symm

/-- A strictly positive supported half-mass corner table and actual row
paths suffice for a unique grounded minimum of the explicit triangle sum.
No coercivity, strict convexity, gradient or Hessian is supplied as a premise. -/
theorem exists_unique_triangle_minimizer [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hp : ∀ t i, 0 < a t i → 0 < β t i)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0)
    (hm : ∀ t, (∑ i, β t i) = 1/2)
    (hc : TransportCoercivity.connected (support c a)) (root : V) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ p : V → ℝ, p root = 0 →
      summedPotential c a (column c β) q ≤ summedPotential c a (column c β) p := by
  classical
  have hne := table_support_nonempty a β hz hm
  have heq := transport_potential_eq c a β hz
  have hcont : ∀ t, Continuous (fun q : V → ℝ => potential (a t) (fun i => q (c t i))) := by
    intro t
    exact (potential_continuous (a t) (ha t) (hne t)).comp
      (continuous_pi (fun i => continuous_apply (c t i)))
  have result := GroundedConvexity.exists_unique_grounded_minimizer
    (support c a) (support_nonempty c a hne) (aggregate c β)
    (aggregate_positive c a β (table_nonneg a β hp hz) hp) hc root
    (fun t q => potential (a t) (fun i => q (c t i))) (offsetCost a)
    (row_vertex_lower c a β ha hne hz hm) hcont
    (fun e : T × Fin 3 => c e.1 (edgeSrc e.2))
    (fun e : T × Fin 3 => c e.1 (edgeDst e.2)) (edgeWeight c a)
    (fun x y => deriv (GroundedConvexity.segmentValue (summedPotential c a (column c β)) x y))
    (fun x _ y _ u _ => by
      rw [heq]
      exact summedPotential_segment_hasDerivAt c a (column c β) ha hne x y u)
    (fun x _ y _ u _ => summedPotential_segment_second c a (column c β) ha hne x y u)
    (fun q _ e => edgeWeight_nonneg c a ha q e)
    (fun q _ => conductance_connected_of_rows c a ha hc q)
  simpa only [heq] using result

/-- A boundary corner retains its prescribed coefficient when all boundary
corners are mapped to one grounded root. Distinct coefficients are not merged. -/
theorem pooled_boundary_weight (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (root : V) (q : V → ℝ) (hq : q root = 0) (t : T) (i : Fin 3)
    (hc : c t i = root) : weights (a t) (fun j => q (c t j)) i = a t i := by
  simp [weights, hc, hq]

/-- The only demand discrepancy allowed by grounding is retained exactly. -/
theorem root_demand_difference [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (δ d q : V → ℝ) (root : V)
    (hd : ∀ v, v ≠ root → δ v = d v) :
    summedPotential c a δ q - summedPotential c a d q = (d root-δ root) * q root := by
  classical
  calc
    summedPotential c a δ q - summedPotential c a d q =
        ∑ v, (d v-δ v) * q v := by
      simp only [summedPotential, sub_mul, Finset.sum_sub_distrib]
      ring
    _ = (d root-δ root) * q root := by
      apply Finset.sum_eq_single root
      · intro v _ hv
        rw [hd v hv]
        simp
      · simp

theorem grounded_demand_eq [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (δ d q : V → ℝ) (root : V)
    (hd : ∀ v, v ≠ root → δ v = d v) (hq : q root = 0) :
    summedPotential c a δ q = summedPotential c a d q := by
  have he := root_demand_difference c a δ d q root hd
  rw [hq, mul_zero] at he
  exact sub_eq_zero.mp he

/-- The original free-vertex demands suffice: no artificial boundary target
is imposed, because the table's actual root-demand term vanishes upon grounding. -/
theorem exists_unique_prescribed_minimizer [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ) (δ : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hp : ∀ t i, 0 < a t i → 0 < β t i)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0)
    (hm : ∀ t, (∑ i, β t i) = 1/2)
    (hc : TransportCoercivity.connected (support c a)) (root : V)
    (hd : ∀ v, v ≠ root → δ v = column c β v) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ p : V → ℝ, p root = 0 →
      summedPotential c a δ q ≤ summedPotential c a δ p := by
  obtain ⟨q,⟨hq,hmin⟩,hunique⟩ := exists_unique_triangle_minimizer c a β ha hp hz hm hc root
  refine ⟨q, ⟨hq, ?_⟩, ?_⟩
  · intro p hp
    rw [grounded_demand_eq c a δ (column c β) q root hd hq,
      grounded_demand_eq c a δ (column c β) p root hd hp]
    exact hmin p hp
  · intro p hp
    apply hunique
    refine ⟨hp.1, ?_⟩
    intro r hr
    rw [← grounded_demand_eq c a δ (column c β) p root hd hp.1,
      ← grounded_demand_eq c a δ (column c β) r root hd hr]
    exact hp.2 r hr

end VolumeLogic.TriangleMinimizer
