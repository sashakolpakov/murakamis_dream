import HallRecession

/-!
Strict finite cut inequalities imply existence and uniqueness of the actual
supported triangle balance. No feasible table is an input: a minimizer of
the Lobachevsky envelope constructs the positive corner table. The theorem
retains singleton rows and repeated destinations. Geometric incidence and
verification of the cuts for a particular packing remain application work.
-/
namespace VolumeLogic.TriangleHall
open scoped BigOperators
open TriangleLoads TrianglePotential TriangleMinimizer TriangleBalance

theorem supportedLoad_positive (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (i : Fin 3) (hi : 0 < a i) : 0 < supportedLoad a q i := by
  classical
  by_cases hr : Regular a
  · rw [supportedLoad_regular a q hr]
    unfold load
    apply div_pos _ Real.pi_pos
    apply Real.arctan_pos.mpr
    exact div_pos ((weights_pos_iff a q i).mpr hi)
      (triangleD_pos _ (regular_radicand a q ha hr))
  · simp [supportedLoad,hr,hi]

theorem supportedLoad_zero (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) (i : Fin 3) (hi : ¬ 0 < a i) :
    supportedLoad a q i = 0 := by
  exact (supportedLoad_feasible a q ha hne).2.2 i
    (le_antisymm (le_of_not_gt hi) (ha i))

variable {T V : Type*} [Fintype T] [Fintype V]

/-- The row lower bound uses a canonical local feasible point solely to invoke
the established vertex estimate. It assumes no prescribed column sums. -/
theorem row_lower (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (t : T) (q : V → ℝ) :
    TransportCoercivity.rowMax (support c a) (support_nonempty c a hne) q t / 2 -
      offsetCost a t ≤ potential (a t) (fun i => q (c t i)) := by
  let β : T → Fin 3 → ℝ := fun t => supportedLoad (a t) 0
  have hz : ∀ t i, ¬ 0 < a t i → β t i = 0 :=
    fun t i hi => supportedLoad_zero (a t) 0 (ha t) (hne t) i hi
  have hm : ∀ t, (∑ i, β t i) = 1/2 :=
    fun t => (supportedLoad_feasible (a t) 0 (ha t) (hne t)).2.1
  have he := row_vertex_lower c a β ha hne hz hm t q
  rw [aggregate_rowMass c a β hz,hm] at he
  linarith

theorem continuous_summedPotential (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) :
    Continuous (summedPotential c a d) := by
  unfold summedPotential
  apply Continuous.sub
  · apply continuous_finsetSum
    intro t _
    apply (potential_continuous (a t) (ha t) (hne t)).comp
    exact continuous_pi (fun i => continuous_apply (c t i))
  · exact continuous_finsetSum _ (fun v _ => continuous_const.mul (continuous_apply v))

theorem recession_lower (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (q : V → ℝ) :
    HallRecession.recession (support c a) (support_nonempty c a hne) d q -
      ∑ t, offsetCost a t ≤ summedPotential c a d q := by
  have he := Finset.sum_le_sum (s := Finset.univ) (fun t _ => row_lower c a ha hne t q)
  rw [Finset.sum_sub_distrib,← Finset.sum_div] at he
  unfold HallRecession.recession summedPotential
  linarith

/-- All vertices, including the grounded root, have the prescribed load. The
root equation uses the explicit total half-mass compatibility. -/
theorem exists_balance (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ →
      0 < HallRecession.deficit (support c a) d A) (root : V) :
    ∃ q : V → ℝ, q root = 0 ∧ ∀ v, vertexLoad c a q v = d v := by
  obtain ⟨q,hq,hmin⟩ := HallRecession.exists_grounded_minimizer
    (support c a) (support_nonempty c a hne) d hm hc root
    (summedPotential c a d) (continuous_summedPotential c a d ha hne)
    (∑ t, offsetCost a t) (recession_lower c a d ha hne)
  have hb := minimizer_balance c a d q ha hne root hq hmin
  refine ⟨q,hq,?_⟩
  intro v
  by_cases hv : v = root
  · subst v
    exact (root_balance_iff_total c a d q ha hne root hb).mpr hm
  · exact hb v hv

/-- The table is a conclusion. Its positive entries are precisely the active
corners, and repeated corner destinations are summed only in the columns. -/
theorem exists_positive_table (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ →
      0 < HallRecession.deficit (support c a) d A) (root : V) :
    ∃ β : T → Fin 3 → ℝ,
      (∀ t i, 0 < a t i → 0 < β t i) ∧
      (∀ t i, ¬ 0 < a t i → β t i = 0) ∧
      (∀ t, (∑ i, β t i) = 1/2) ∧ column c β = d := by
  obtain ⟨q,_,hb⟩ := exists_balance c a d ha hne hm hc root
  refine ⟨fun t => supportedLoad (a t) (fun i => q (c t i)),?_,?_,?_,?_⟩
  · exact fun t i hi => supportedLoad_positive (a t) _ (ha t) i hi
  · exact fun t i hi => supportedLoad_zero (a t) _ (ha t) (hne t) i hi
  · exact fun t => (supportedLoad_feasible (a t) _ (ha t) (hne t)).2.1
  · exact funext hb

/-- The previously conditional uniqueness theorem now receives its positive
table and row connectivity from the finite cut hypotheses. -/
theorem exists_unique_balance (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ →
      0 < HallRecession.deficit (support c a) d A) (root : V) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ v, vertexLoad c a q v = d v := by
  obtain ⟨β,hp,hz,hrow,hd⟩ := exists_positive_table c a d ha hne hm hc root
  have hconn := HallRecession.connected_of_strict_cuts
    (support c a) (support_nonempty c a hne) d hm hc
  obtain ⟨q,⟨hq,hb⟩,hu⟩ := TriangleBalance.exists_unique_balance c a β d ha hp hz hrow
    hconn root (fun v _ => (congrFun hd v).symm)
  refine ⟨q,⟨hq,?_⟩,?_⟩
  · intro v
    by_cases hv : v = root
    · subst v
      exact (root_balance_iff_total c a d q ha hne root hb).mpr hm
    · exact hb v hv
  · intro p hpp
    exact hu p ⟨hpp.1,fun v _ => hpp.2 v⟩

theorem exists_unique_minimizer (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ →
      0 < HallRecession.deficit (support c a) d A) (root : V) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ p : V → ℝ, p root = 0 →
      summedPotential c a d q ≤ summedPotential c a d p := by
  obtain ⟨q,⟨hq,hb⟩,hu⟩ := exists_unique_balance c a d ha hne hm hc root
  refine ⟨q,⟨hq,balance_minimizer c a d q ha hne root hq (fun v _ => hb v)⟩,?_⟩
  intro p hp
  have hpb := minimizer_balance c a d p ha hne root hp.1 hp.2
  apply hu p
  refine ⟨hp.1,?_⟩
  intro v
  by_cases hv : v = root
  · subst v
    exact (root_balance_iff_total c a d p ha hne root hpb).mpr hm
  · exact hpb v hv

end VolumeLogic.TriangleHall
