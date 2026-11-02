import TriangleMinimizer
import Mathlib.Analysis.Calculus.LocalExtr.Basic

/-!
Euler equations for the literal supported triangle entropy supremum.
The corner loads are the actual arctangent maximizer on regular rows and
one half at the active corner on singleton rows. Repeated destinations are
summed before the free-coordinate equations are imposed. Grounding leaves
the root demand arbitrary. Hall feasibility and geometric incidence are
not supplied by these theorems.
-/
namespace VolumeLogic.TriangleBalance
open scoped BigOperators
open Set
open TriangleLoads TrianglePotential TriangleMinimizer

/-- The explicit maximizing corner loads on every nonempty fixed support. -/
noncomputable def supportedLoad (a q : Fin 3 → ℝ) (i : Fin 3) : ℝ := by
  classical
  exact if Regular a then load a q i else if 0 < a i then 1/2 else 0

theorem supportedLoad_regular (a q : Fin 3 → ℝ) (hr : Regular a) :
    supportedLoad a q = load a q := by
  classical
  funext i
  simp [supportedLoad, hr]

theorem not_regular_singleton (a : Fin 3 → ℝ) (active : Fin 3)
    (hz : ∀ i, i ≠ active → a i = 0) : ¬ Regular a := by
  rintro ⟨i,j,hij,hi,hj⟩
  have hia : i = active := by
    by_contra hn
    rw [hz i hn] at hi
    exact lt_irrefl _ hi
  have hja : j = active := by
    by_contra hn
    rw [hz j hn] at hj
    exact lt_irrefl _ hj
  exact hij (hia.trans hja.symm)

theorem supportedLoad_singleton (a q : Fin 3 → ℝ) (active : Fin 3)
    (hp : 0 < a active) (hz : ∀ i, i ≠ active → a i = 0) :
    supportedLoad a q = singletonLoad active q := by
  classical
  funext i
  have hr := not_regular_singleton a active hz
  by_cases hi : i = active
  · subst i
    simp [supportedLoad, hr, hp, singletonLoad]
  · simp [supportedLoad, hr, hz i hi, singletonLoad, hi]

theorem supportedLoad_feasible (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) : Feasible a (supportedLoad a q) := by
  classical
  by_cases hr : Regular a
  · rw [supportedLoad_regular a q hr]
    exact loads_feasible a q ha (regular_radicand a q ha hr)
  · obtain ⟨i,hi⟩ := hne
    rw [supportedLoad_singleton a q i hi (nonregular_singleton a ha hr i hi)]
    exact singleton_feasible a q i hi

theorem potential_eq_supportedLoad (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) : potential a q = objective a q (supportedLoad a q) := by
  classical
  by_cases hr : Regular a
  · rw [supportedLoad_regular a q hr]
    exact potential_eq_loads a q ha (regular_radicand a q ha hr)
  · obtain ⟨i,hi⟩ := hne
    have hz := nonregular_singleton a ha hr i hi
    rw [supportedLoad_singleton a q i hi hz, potential_singleton a q i hi hz,
      objective_singleton a q i hi]

/-- Derived from the attained actual supremum, not an assumed gradient. -/
theorem potential_supporting (a q p : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) :
    potential a q + ∑ i, supportedLoad a q i * (p i-q i) ≤ potential a p := by
  obtain ⟨_,_,_,hb⟩ := potential_attained a p ha hne
  have hf := supportedLoad_feasible a q ha hne
  have hu := hb (supportedLoad a q) hf
  have he := objective_difference a p q (supportedLoad a q) hf
  rw [← potential_eq_supportedLoad a q ha hne] at he
  linarith

theorem potential_path_derivative (a q h : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) (u : ℝ) :
    HasDerivAt (fun v : ℝ => potential a (fun j => q j + v * h j))
      (∑ i, h i * supportedLoad a (fun j => q j + u * h j) i) u := by
  classical
  by_cases hr : Regular a
  · rw [supportedLoad_regular a _ hr]
    exact potential_path_hasDerivAt a q h ha (regular_radicand a q ha hr) u
  · obtain ⟨i,hi⟩ := hne
    have hz := nonregular_singleton a ha hr i hi
    rw [supportedLoad_singleton a _ i hi hz]
    simpa [singletonLoad, div_eq_mul_inv] using potential_singleton_hasDerivAt a q h i hi hz u

variable {T V : Type*}

/-- Actual corner loads are added at their original vertex destinations. -/
noncomputable def vertexLoad [Fintype T] (c : T → Fin 3 → V)
    (a : T → Fin 3 → ℝ) (q : V → ℝ) : V → ℝ :=
  column c (fun t => supportedLoad (a t) (fun i => q (c t i)))

noncomputable def residual [Fintype T] (c : T → Fin 3 → V)
    (a : T → Fin 3 → ℝ) (d q : V → ℝ) (v : V) : ℝ := vertexLoad c a q v-d v

/-- Finite incidence summation retains every repeated destination. -/
theorem column_pairing [Fintype T] [Fintype V] (c : T → Fin 3 → V)
    (β : T → Fin 3 → ℝ) (h : V → ℝ) :
    (∑ v, column c β v * h v) = ∑ t, ∑ i, β t i * h (c t i) := by
  classical
  simp only [column, Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t _
  simp only [aggregate, Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  simp

/-- Each supported triangle still has total load one half after incidence
aggregation, even when several of its corners have the same destination. -/
theorem sum_vertexLoad [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) :
    (∑ v, vertexLoad c a q v) = (Fintype.card T : ℝ) / 2 := by
  have he := column_pairing c (fun t => supportedLoad (a t) (fun i => q (c t i)))
    (fun _ => 1)
  simp only [mul_one] at he
  unfold vertexLoad
  rw [he]
  have hm : ∀ t, (∑ i, supportedLoad (a t) (fun j => q (c t j)) i) = 1/2 :=
    fun t => (supportedLoad_feasible (a t) _ (ha t) (hne t)).2.1
  simp only [hm, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  ring

theorem sum_residual [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) :
    (∑ v, residual c a d q v) = (Fintype.card T : ℝ) / 2 - ∑ v, d v := by
  simp only [residual, Finset.sum_sub_distrib, sum_vertexLoad c a q ha hne]

/-- The grounded root equation is not silently added to the free equations.
Its remaining residual is exactly the total mass discrepancy. -/
theorem root_residual [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) (root : V)
    (hb : ∀ v, v ≠ root → vertexLoad c a q v = d v) :
    residual c a d q root = (Fintype.card T : ℝ) / 2 - ∑ v, d v := by
  classical
  have he : (∑ v, residual c a d q v) = residual c a d q root := by
    apply Finset.sum_eq_single root
    · intro v _ hv
      simp [residual, hb v hv]
    · simp
  rw [← he]
  exact sum_residual c a d q ha hne

theorem root_balance_iff_total [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) (root : V)
    (hb : ∀ v, v ≠ root → vertexLoad c a q v = d v) :
    vertexLoad c a q root = d root ↔ (∑ v, d v) = (Fintype.card T : ℝ) / 2 := by
  have he := root_residual c a d q ha hne root hb
  unfold residual at he
  constructor <;> intro hh <;> linarith

/-- Every actual directional derivative is the residual-load pairing. -/
theorem summedPotential_path_derivative [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q h : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) (u : ℝ) :
    HasDerivAt (fun v : ℝ => summedPotential c a d (fun j => q j+v*h j))
      (∑ v, residual c a d (fun j => q j+u*h j) v * h v) u := by
  have hp := HasDerivAt.fun_sum (u := Finset.univ) (fun t _ =>
    potential_path_derivative (a t) (fun i => q (c t i)) (fun i => h (c t i))
      (ha t) (hne t) u)
  have hd := HasDerivAt.fun_sum (u := Finset.univ) (fun v _ =>
    (((hasDerivAt_id u).mul_const (h v)).const_add (q v)).const_mul (d v))
  have he : (∑ v, residual c a d (fun j => q j+u*h j) v * h v) =
      (∑ t, ∑ i, h (c t i) * supportedLoad (a t)
        (fun j => q (c t j)+u*h (c t j)) i) - ∑ v, d v * h v := by
    simp only [residual, sub_mul, Finset.sum_sub_distrib, vertexLoad]
    rw [column_pairing]
    congr 1
    apply Finset.sum_congr rfl
    intro t _
    apply Finset.sum_congr rfl
    intro i _
    exact mul_comm _ _
  rw [he]
  convert! hp.sub hd using 1
  simp only [one_mul]

/-- Each coordinate derivative is exactly its aggregate load minus demand. -/
theorem coordinate_derivative [Fintype T] [Fintype V] [DecidableEq V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) (v : V) :
    HasDerivAt (fun u : ℝ => summedPotential c a d (q + u • Pi.single v 1))
      (residual c a d q v) 0 := by
  convert! summedPotential_path_derivative c a d q (Pi.single v 1) ha hne 0 using 1
  simp [Pi.single_apply, mul_ite]

/-- A grounded global minimum satisfies every free-coordinate balance. -/
theorem minimizer_balance [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) (root : V)
    (hq : q root = 0)
    (hm : ∀ p : V → ℝ, p root = 0 → summedPotential c a d q ≤ summedPotential c a d p) :
    ∀ v, v ≠ root → vertexLoad c a q v = d v := by
  classical
  intro v hv
  have hg : ∀ u : ℝ, summedPotential c a d (q + (0 : ℝ) • Pi.single v 1) ≤
      summedPotential c a d (q + u • Pi.single v 1) := by
    intro u
    simpa using hm (q + u • Pi.single v 1) (by simp [hq, Ne.symm hv])
  have hl : IsLocalMin (fun u : ℝ => summedPotential c a d (q+u • Pi.single v 1)) 0 :=
    Filter.Eventually.of_forall hg
  exact sub_eq_zero.mp (hl.hasDerivAt_eq_zero (coordinate_derivative c a d q ha hne v))

/-- Supporting inequalities add on the same shared vertex variables. -/
theorem summedPotential_supporting [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q p : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) :
    summedPotential c a d q + ∑ v, residual c a d q v * (p v-q v) ≤
      summedPotential c a d p := by
  have h := Finset.sum_le_sum (s := Finset.univ) (fun t _ =>
    potential_supporting (a t) (fun i => q (c t i)) (fun i => p (c t i)) (ha t) (hne t))
  have he := column_pairing c (fun t => supportedLoad (a t) (fun i => q (c t i)))
    (fun v => p v-q v)
  simp only [summedPotential, residual, vertexLoad]
  rw [Finset.sum_add_distrib] at h
  simp only [sub_mul, Finset.sum_sub_distrib]
  rw [he]
  have hd : (∑ v, d v * p v) = (∑ v, d v * q v) + ∑ v, d v * (p v-q v) := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro v _
    ring
  linarith

/-- Free balance suffices for a global grounded minimum, without a table. -/
theorem balance_minimizer [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) (root : V)
    (hq : q root = 0) (hb : ∀ v, v ≠ root → vertexLoad c a q v = d v) :
    ∀ p : V → ℝ, p root = 0 → summedPotential c a d q ≤ summedPotential c a d p := by
  intro p hp
  have hs : (∑ v, residual c a d q v * (p v-q v)) = 0 := by
    apply Finset.sum_eq_zero
    intro v _
    by_cases hv : v = root
    · subst v
      simp [hq,hp]
    · simp [residual,hb v hv]
  have he := summedPotential_supporting c a d q p ha hne
  simpa [hs] using he

theorem grounded_minimizer_iff_balance [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (d q : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i) (root : V)
    (hq : q root = 0) :
    (∀ p : V → ℝ, p root = 0 → summedPotential c a d q ≤ summedPotential c a d p) ↔
      ∀ v, v ≠ root → vertexLoad c a q v = d v :=
  ⟨minimizer_balance c a d q ha hne root hq, balance_minimizer c a d q ha hne root hq⟩

/-- The actual Euler system has exactly one grounded solution. -/
theorem exists_unique_balance [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ) (d : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hp : ∀ t i, 0 < a t i → 0 < β t i)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0)
    (hm : ∀ t, (∑ i, β t i) = 1/2)
    (hc : TransportCoercivity.connected (support c a)) (root : V)
    (hd : ∀ v, v ≠ root → d v = column c β v) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ v, v ≠ root → vertexLoad c a q v = d v := by
  have hne := table_support_nonempty a β hz hm
  obtain ⟨q,⟨hq,hmin⟩,hu⟩ := exists_unique_prescribed_minimizer c a β d ha hp hz hm hc root hd
  refine ⟨q, ⟨hq, minimizer_balance c a d q ha hne root hq hmin⟩, ?_⟩
  intro p hp
  exact hu p ⟨hp.1, balance_minimizer c a d p ha hne root hp.1 hp.2⟩

end VolumeLogic.TriangleBalance
