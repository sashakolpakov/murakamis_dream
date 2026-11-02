import TriangleBalance
import Mathlib.Algebra.Order.Group.Finset

/-!
A direct finite-cut proof of the maximum-minus-linear recession bound.
No transport table is assumed: a height vector is reduced one positive
level at a time, and each level contributes its actual Hall deficit.
-/
namespace VolumeLogic.HallRecession
open scoped BigOperators
open TransportCoercivity
variable {T V : Type*} [Fintype T] [Fintype V]

noncomputable def positive (q : V → ℝ) : Finset V := by
  classical
  exact Finset.univ.filter (fun v => 0 < q v)

noncomputable def rowCut (S : T → Finset V) (A : Finset V) (t : T) : ℝ := by
  classical
  exact if ∃ v ∈ S t, v ∈ A then 1 else 0

noncomputable def capacity (S : T → Finset V) (A : Finset V) : ℝ :=
  (∑ t, rowCut S A t) / 2

noncomputable def deficit (S : T → Finset V) (d : V → ℝ) (A : Finset V) : ℝ :=
  capacity S A - ∑ v ∈ A, d v

noncomputable def recession (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d q : V → ℝ) : ℝ := (∑ t, rowMax S hne q t) / 2 - ∑ v, d v * q v

noncomputable def peel (q : V → ℝ) (a : ℝ) (v : V) : ℝ :=
  if 0 < q v then q v-a else 0

theorem mem_positive (q : V → ℝ) (v : V) : v ∈ positive q ↔ 0 < q v := by
  classical
  simp [positive]

omit [Fintype V] in
theorem peel_nonneg (q : V → ℝ) (a : ℝ)
    (ha : ∀ v, 0 < q v → a ≤ q v) : ∀ v, 0 ≤ peel q a v := by
  intro v
  unfold peel
  split_ifs with hv
  · exact sub_nonneg.mpr (ha v hv)
  · exact le_rfl

omit [Fintype V] in
theorem peel_split (q : V → ℝ) (a : ℝ) (hq : ∀ v, 0 ≤ q v) (v : V) :
    q v = peel q a v + if 0 < q v then a else 0 := by
  unfold peel
  split_ifs with hv
  · ring
  · have hz : q v = 0 := le_antisymm (le_of_not_gt hv) (hq v)
    simp [hz]

omit [Fintype T] in
theorem rowMax_peel (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (q : V → ℝ) (a : ℝ) (hq : ∀ v, 0 ≤ q v)
    (ha : ∀ v, 0 < q v → a ≤ q v) (t : T) :
    rowMax S hne q t = rowMax S hne (peel q a) t + a * rowCut S (positive q) t := by
  classical
  unfold rowCut
  by_cases hit : ∃ v ∈ S t, v ∈ positive q
  · rw [if_pos hit, mul_one]
    obtain ⟨v,hv,hm⟩ := Finset.exists_mem_eq_sup' (hne t) q
    have hpos : 0 < q v := by
      obtain ⟨u,hu,hup⟩ := hit
      have he := Finset.le_sup' q hu
      rw [hm] at he
      exact (mem_positive q u).mp hup |>.trans_le he
    have pe : rowMax S hne (peel q a) t = q v-a := by
      apply le_antisymm
      · apply Finset.sup'_le
        intro i hi
        by_cases hp : 0 < q i
        · simp only [peel, if_pos hp]
          have he := Finset.le_sup' q hi
          rw [hm] at he
          linarith
        · simp only [peel, if_neg hp]
          exact sub_nonneg.mpr (ha v hpos)
      · have he : peel q a v ≤ rowMax S hne (peel q a) t :=
          Finset.le_sup' (peel q a) hv
        rw [show peel q a v = q v-a from if_pos hpos] at he
        exact he
    change (S t).sup' (hne t) q = _
    rw [hm, pe]
    ring
  · rw [if_neg hit, mul_zero, add_zero]
    have hz : ∀ v ∈ S t, q v = 0 := by
      intro v hv
      have hn : ¬ 0 < q v := fun hp => hit ⟨v,hv,(mem_positive q v).mpr hp⟩
      exact le_antisymm (le_of_not_gt hn) (hq v)
    have e1 : rowMax S hne q t = 0 := by
      apply le_antisymm
      · exact Finset.sup'_le _ _ (fun v hv => (hz v hv).le)
      · obtain ⟨v,hv⟩ := hne t
        exact (hz v hv).symm.le.trans (Finset.le_sup' q hv)
    have e2 : rowMax S hne (peel q a) t = 0 := by
      apply le_antisymm
      · apply Finset.sup'_le
        intro v hv
        simp [peel, hz v hv]
      · obtain ⟨v,hv⟩ := hne t
        exact (peel_nonneg q a ha v).trans (Finset.le_sup' (peel q a) hv)
    rw [e1,e2]

theorem recession_peel (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d q : V → ℝ) (a : ℝ) (hq : ∀ v, 0 ≤ q v)
    (ha : ∀ v, 0 < q v → a ≤ q v) :
    recession S hne d q = recession S hne d (peel q a) + a * deficit S d (positive q) := by
  classical
  have e1 : (∑ t, rowMax S hne q t) =
      (∑ t, rowMax S hne (peel q a) t) + 2*a*capacity S (positive q) := by
    simp_rw [rowMax_peel S hne q a hq ha]
    rw [Finset.sum_add_distrib, ← Finset.mul_sum]
    unfold capacity
    ring
  have e2 : (∑ v, d v*q v) = (∑ v, d v*peel q a v) + a*(∑ v ∈ positive q, d v) := by
    conv_lhs => arg 2; ext v; rw [peel_split q a hq v, mul_add]
    rw [Finset.sum_add_distrib]
    congr 1
    simp only [positive, Finset.sum_filter, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro v _
    split_ifs <;> ring
  unfold recession deficit
  rw [e1,e2]
  ring

/-- Removing the least positive height removes at least one positive vertex. -/
theorem peel_card_lt (q : V → ℝ) (v : V) (hv : 0 < q v) :
    (positive (peel q (q v))).card < (positive q).card := by
  classical
  apply Finset.card_lt_card
  apply Finset.ssubset_iff_subset_ne.mpr
  constructor
  · intro i hi
    apply (mem_positive q i).mpr
    by_contra hn
    have he := (mem_positive (peel q (q v)) i).mp hi
    simp only [peel, if_neg hn] at he
    exact lt_irrefl _ he
  · intro he
    have hp : v ∈ positive (peel q (q v)) := he.symm ▸ (mem_positive q v).mpr hv
    have hh := (mem_positive (peel q (q v)) v).mp hp
    simp only [peel, if_pos hv, sub_self] at hh
    exact lt_irrefl _ hh

/-- All finite weak cut inequalities imply nonnegative recession on every
nonnegative height vector. The proof is induction on its positive support. -/
theorem nonneg_of_cuts (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) (hcut : ∀ A, 0 ≤ deficit S d A)
    (q : V → ℝ) (hq : ∀ v, 0 ≤ q v) : 0 ≤ recession S hne d q := by
  classical
  have aux : ∀ n : ℕ, ∀ q : V → ℝ, (positive q).card = n →
      (∀ v, 0 ≤ q v) → 0 ≤ recession S hne d q := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro q hn hq
      by_cases hp : (positive q).Nonempty
      · obtain ⟨v,hv,hmin⟩ := Finset.exists_mem_eq_inf' hp q
        have hvp := (mem_positive q v).mp hv
        have ha : ∀ i, 0 < q i → q v ≤ q i := by
          intro i hi
          have he := Finset.inf'_le q ((mem_positive q i).mpr hi)
          rw [hmin] at he
          exact he
        have hlt : (positive (peel q (q v))).card < n := by
          rw [← hn]
          exact peel_card_lt q v hvp
        have hr := ih _ hlt (peel q (q v)) rfl (peel_nonneg q (q v) ha)
        rw [recession_peel S hne d q (q v) hq ha]
        exact add_nonneg hr (mul_nonneg hvp.le (hcut _))
      · have hz : q = 0 := by
          funext v
          apply le_antisymm _ (hq v)
          apply le_of_not_gt
          intro hv
          exact hp ⟨v,(mem_positive q v).mpr hv⟩
        simp [hz,recession,rowMax]
  exact aux _ q rfl hq

theorem capacity_univ (S : T → Finset V) (hne : ∀ t, (S t).Nonempty) :
    capacity S Finset.univ = (Fintype.card T : ℝ)/2 := by
  classical
  have hh : ∀ t, ∃ v ∈ S t, v ∈ (Finset.univ : Finset V) := by
    intro t
    obtain ⟨v,hv⟩ := hne t
    exact ⟨v,hv,Finset.mem_univ v⟩
  have he : ∀ t, rowCut S Finset.univ t = 1 := fun t => if_pos (hh t)
  simp [capacity,he]

theorem weak_cuts_of_strict (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A) :
    ∀ A, 0 ≤ deficit S d A := by
  classical
  intro A
  by_cases he : A = ∅
  · subst A
    simp [deficit,capacity,rowCut]
  by_cases hu : A = Finset.univ
  · subst A
    rw [deficit,capacity_univ S hne,hm,sub_self]
  · exact (hc A (Finset.nonempty_iff_ne_empty.mpr he) hu).le

/-- A nonconstant nonnegative height vector has a genuinely positive cut
contribution when it vanishes at some vertex. -/
theorem positive_of_strict_cuts (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A)
    (q : V → ℝ) (hq : ∀ v, 0 ≤ q v) (hz : ∃ v, q v = 0) (hn : q ≠ 0) :
    0 < recession S hne d q := by
  classical
  have hp : (positive q).Nonempty := by
    by_contra he
    apply hn
    funext v
    apply le_antisymm _ (hq v)
    exact le_of_not_gt (fun hv => he ⟨v,(mem_positive q v).mpr hv⟩)
  have hu : positive q ≠ Finset.univ := by
    intro he
    obtain ⟨v,hv⟩ := hz
    have hpv : v ∈ positive q := he.symm ▸ Finset.mem_univ v
    have he := (mem_positive q v).mp hpv
    rw [hv] at he
    exact lt_irrefl _ he
  obtain ⟨v,hv,hmin⟩ := Finset.exists_mem_eq_inf' hp q
  have hvp := (mem_positive q v).mp hv
  have ha : ∀ i, 0 < q i → q v ≤ q i := by
    intro i hi
    have he := Finset.inf'_le q ((mem_positive q i).mpr hi)
    rw [hmin] at he
    exact he
  have hr := nonneg_of_cuts S hne d (weak_cuts_of_strict S hne d hm hc)
    (peel q (q v)) (peel_nonneg q (q v) ha)
  rw [recession_peel S hne d q (q v) hq ha]
  exact add_pos_of_nonneg_of_pos hr (mul_pos hvp (hc _ hp hu))

theorem recession_translate (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d q : V → ℝ) (b : ℝ) (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2) :
    recession S hne d (fun v => q v+b) = recession S hne d q := by
  have he : ∀ t, rowMax S hne (fun v => q v+b) t = rowMax S hne q t+b :=
    fun t => (Finset.sup'_add (S t) q b (hne t)).symm
  simp only [recession, he, Finset.sum_add_distrib, mul_add,
    Finset.sum_const, Finset.card_univ, nsmul_eq_mul, ← Finset.sum_mul, hm]
  ring

/-- Total mass compatibility removes the constant direction. Strict cuts then
give positivity on every nonzero grounded direction, of either sign. -/
theorem grounded_positive (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A)
    (root : V) (q : V → ℝ) (hg : q root = 0) (hn : q ≠ 0) :
    0 < recession S hne d q := by
  classical
  have hu : (Finset.univ : Finset V).Nonempty := ⟨root,Finset.mem_univ root⟩
  obtain ⟨v,_,hmin⟩ := Finset.exists_mem_eq_inf' hu q
  have hle : ∀ i, q v ≤ q i := by
    intro i
    have he := Finset.inf'_le q (Finset.mem_univ i)
    rw [hmin] at he
    exact he
  have hnn : (fun i => q i + -q v) ≠ 0 := by
    intro he
    have hr := congrFun he root
    simp only [hg, zero_add, Pi.zero_apply, neg_eq_zero] at hr
    apply hn
    funext i
    have hi := congrFun he i
    simpa [hr] using hi
  have hp := positive_of_strict_cuts S hne d hm hc (fun i => q i + -q v)
    (fun i => by linarith [hle i]) ⟨v,by ring⟩ hnn
  rwa [recession_translate S hne d q (-q v) hm] at hp

theorem continuous_recession (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) : Continuous (recession S hne d) := by
  unfold recession
  apply Continuous.sub
  · apply Continuous.div_const
    apply continuous_finsetSum
    intro t _
    exact Continuous.finset_sup'_apply (hne t) (fun i _ => continuous_apply i)
  · exact continuous_finsetSum _ (fun i _ => continuous_const.mul (continuous_apply i))

theorem recession_smul (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d q : V → ℝ) {b : ℝ} (hb : 0 ≤ b) :
    recession S hne d (b • q) = b * recession S hne d q := by
  have he : ∀ t, rowMax S hne (b • q) t = b * rowMax S hne q t :=
    fun t => (Finset.mul₀_sup' hb q (S t) (hne t)).symm
  simp only [recession, he, Pi.smul_apply, smul_eq_mul]
  simp_rw [← mul_assoc, mul_comm (d _) b, mul_assoc]
  rw [← Finset.mul_sum, ← Finset.mul_sum]
  ring

/-- Strict finite cuts yield a uniform grounded margin, without assuming a
supported transport table or any margin in advance. -/
theorem grounded_coercive (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A)
    (root : V) : ∃ b : ℝ, 0 < b ∧ ∀ q : V → ℝ, q root = 0 →
      b * ‖q‖ ≤ recession S hne d q := by
  let U : Set (V → ℝ) := {q | q root = 0} ∩ Metric.sphere 0 1
  have hU : IsCompact U := (isCompact_sphere (0 : V → ℝ) 1).inter_left
    (isClosed_eq (continuous_apply root) continuous_const)
  have hp : ∀ q ∈ U, 0 < recession S hne d q := by
    intro q hq
    apply grounded_positive S hne d hm hc root q hq.1
    intro hz
    have hs := hq.2
    simp [hz] at hs
  obtain ⟨b,hb,hmin⟩ := hU.exists_forall_le'
    (continuous_recession S hne d).continuousOn hp
  refine ⟨b,hb,?_⟩
  intro q hq
  by_cases hz : q = 0
  · simp [hz,recession,rowMax]
  have hn : 0 < ‖q‖ := norm_pos_iff.mpr hz
  have hu : ‖q‖⁻¹ • q ∈ U := by
    constructor
    · simp [hq]
    · rw [Metric.mem_sphere,dist_zero_right,norm_smul_of_nonneg (inv_nonneg.mpr hn.le)]
      exact inv_mul_cancel₀ hn.ne'
  have hl := mul_le_mul_of_nonneg_left (hmin _ hu) hn.le
  rw [recession_smul S hne d q (inv_nonneg.mpr hn.le)] at hl
  have he : ‖q‖ * (‖q‖⁻¹ * recession S hne d q) = recession S hne d q := by
    rw [← mul_assoc,mul_inv_cancel₀ hn.ne',one_mul]
  rwa [he,mul_comm ‖q‖ b] at hl

/-- A disconnected component and its complement would both have positive
deficit, although their supplies and demands add to the same total. -/
theorem connected_of_strict_cuts (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A) :
    connected S := by
  classical
  intro u v
  by_contra hv
  let A := Finset.univ.filter (fun w => Relation.ReflTransGen (rowStep S) u w)
  have hmem : ∀ w, w ∈ A ↔ Relation.ReflTransGen (rowStep S) u w := by
    intro w
    simp [A]
  have hu : u ∈ A := (hmem u).mpr Relation.ReflTransGen.refl
  have hvn : v ∉ A := fun h => hv ((hmem v).mp h)
  have hA : A ≠ Finset.univ := fun he => hvn (he.symm ▸ Finset.mem_univ v)
  have hAc : Aᶜ ≠ Finset.univ := by
    intro he
    have hh : u ∈ Aᶜ := he.symm ▸ Finset.mem_univ u
    exact (Finset.mem_compl.mp hh) hu
  have hrow : ∀ t, rowCut S A t + rowCut S Aᶜ t = 1 := by
    intro t
    by_cases hit : ∃ w ∈ S t, w ∈ A
    · obtain ⟨w,hw,hwA⟩ := hit
      have hall : ∀ z ∈ S t, z ∈ A := by
        intro z hz
        exact (hmem z).mpr (((hmem w).mp hwA).tail ⟨t,hw,hz⟩)
      have hn : ¬ ∃ z ∈ S t, z ∈ Aᶜ := by
        rintro ⟨z,hz,hzc⟩
        exact (Finset.mem_compl.mp hzc) (hall z hz)
      simp only [rowCut,if_pos (show ∃ w ∈ S t, w ∈ A from ⟨w,hw,hwA⟩),
        if_neg hn,add_zero]
    · have hitc : ∃ w ∈ S t, w ∈ Aᶜ := by
        obtain ⟨w,hw⟩ := hne t
        exact ⟨w,hw,Finset.mem_compl.mpr (fun hh => hit ⟨w,hw,hh⟩)⟩
      simp only [rowCut,if_neg hit,if_pos hitc,zero_add]
  have hcap : capacity S A + capacity S Aᶜ = (Fintype.card T : ℝ)/2 := by
    unfold capacity
    rw [← add_div, ← Finset.sum_add_distrib]
    simp [hrow]
  have hd : (∑ w ∈ A, d w) + (∑ w ∈ Aᶜ, d w) = (Fintype.card T : ℝ)/2 := by
    rw [Finset.sum_add_sum_compl,hm]
  have h1 := hc A ⟨u,hu⟩ hA
  have h2 := hc Aᶜ ⟨v,Finset.mem_compl.mpr hvn⟩ hAc
  unfold deficit at h1 h2
  linarith

/-- Any continuous potential with the actual recession lower bound has a
grounded global minimum. No transport table or minimizer is a premise. -/
theorem exists_grounded_minimizer (S : T → Finset V)
    (hne : ∀ t, (S t).Nonempty) (d : V → ℝ)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A)
    (root : V) (P : (V → ℝ) → ℝ) (hP : Continuous P) (C : ℝ)
    (hbound : ∀ q, recession S hne d q-C ≤ P q) :
    ∃ q : V → ℝ, q root = 0 ∧ ∀ p : V → ℝ, p root = 0 → P q ≤ P p := by
  obtain ⟨b,hb,hcoerc⟩ := grounded_coercive S hne d hm hc root
  let K : Set (V → ℝ) := {q | q root = 0 ∧ P q ≤ P 0}
  have hbounded : Bornology.IsBounded K := by
    rw [Metric.isBounded_iff_subset_closedBall (0 : V → ℝ)]
    refine ⟨(P 0+C)/b,?_⟩
    intro q hq
    rw [Metric.mem_closedBall,dist_zero_right]
    apply (le_div_iff₀ hb).mpr
    have hr := hcoerc q hq.1
    have hp := hbound q
    linarith [hq.2]
  have hcompact : IsCompact K := by
    apply Metric.isCompact_of_isClosed_isBounded _ hbounded
    exact (isClosed_eq (continuous_apply root) continuous_const).inter
      (isClosed_le hP continuous_const)
  obtain ⟨q,hq,hmin⟩ := hcompact.exists_isMinOn
    (show K.Nonempty from ⟨0,rfl,le_rfl⟩) hP.continuousOn
  refine ⟨q,hq.1,?_⟩
  intro p hp
  by_cases he : P p ≤ P 0
  · exact hmin ⟨hp,he⟩
  · exact hq.2.trans (le_of_not_ge he)

end VolumeLogic.HallRecession
