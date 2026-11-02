import AsymptoticIdentity

open Filter Asymptotics
open scoped Topology
namespace VolumeLogic.AsymptoticIdentityControls

/-- An identically zero scale loses every positive-degree coefficient,
even if expansions are supplied at every order. -/
theorem zero_scale_hides_linear :
    Tendsto (fun _ : ℕ => (0 : ℂ)) atTop (𝓝 0) ∧
    (∀ m : ℕ, (fun _ : ℕ => -(∑ i ∈ Finset.range (m+1),
      (if i = 1 then (1 : ℂ) else 0) * (0 : ℂ)^i))
      =O[atTop] (fun _ : ℕ => (0 : ℂ)^(m+1))) ∧
    (if (1 : ℕ) = 1 then (1 : ℂ) else 0) ≠ 0 := by
  refine ⟨tendsto_const_nhds, ?_, by simp⟩
  intro m
  have hs : (∑ i ∈ Finset.range (m+1),
      (if i = 1 then (1 : ℂ) else 0) * (0 : ℂ)^i) = 0 := by
    apply Finset.sum_eq_zero
    intro i _
    by_cases hi : i = 1 <;> simp [hi]
  simpa only [hs, neg_zero] using (isBigO_zero (fun _ : ℕ => (0 : ℂ)^(m+1)) atTop)

/-- At a single parameter value, the nonzero polynomial X is invisible,
regardless of the valid asymptotic scale used in the application. -/
theorem one_parameter_hides_polynomial (h : ℕ → ℂ) :
    (∀ m : ℕ, (fun n : ℕ => -(∑ i ∈ Finset.range (m+1),
      ((if i = 0 then Polynomial.X else 0 : Polynomial ℂ).eval 0) * h n^i))
      =O[atTop] (fun n : ℕ => h n^(m+1))) ∧
    (Polynomial.X : Polynomial ℂ) ≠ 0 := by
  constructor
  · intro m
    have hs (n : ℕ) : (∑ i ∈ Finset.range (m+1),
        ((if i = 0 then Polynomial.X else 0 : Polynomial ℂ).eval 0) * h n^i) = 0 := by
      apply Finset.sum_eq_zero
      intro i _
      by_cases hi : i = 0 <;> simp [hi]
    simpa only [hs, neg_zero] using (isBigO_zero (fun n : ℕ => h n^(m+1)) atTop)
  · exact Polynomial.X_ne_zero

/-- Any fixed finite number of next-order remainder estimates misses
the next coefficient, even for an otherwise valid nonzero scale. -/
theorem finite_order_hides_next_coefficient (h : ℕ → ℂ) (L : ℕ) :
    (∀ m ≤ L, (fun n : ℕ => -(∑ i ∈ Finset.range (m+1),
      (if i = L+1 then (1 : ℂ) else 0) * h n^i))
      =O[atTop] (fun n : ℕ => h n^(m+1))) ∧
    (if L+1 = L+1 then (1 : ℂ) else 0) ≠ 0 := by
  refine ⟨?_, by simp⟩
  intro m hm
  have hs (n : ℕ) : (∑ i ∈ Finset.range (m+1),
      (if i = L+1 then (1 : ℂ) else 0) * h n^i) = 0 := by
    apply Finset.sum_eq_zero
    intro i hi
    have hn : i ≠ L+1 := by have := Finset.mem_range.mp hi; omega
    simp [hn]
  simpa only [hs, neg_zero] using (isBigO_zero (fun n : ℕ => h n^(m+1)) atTop)

end VolumeLogic.AsymptoticIdentityControls
#print axioms VolumeLogic.AsymptoticIdentityControls.zero_scale_hides_linear
#print axioms VolumeLogic.AsymptoticIdentityControls.one_parameter_hides_polynomial
#print axioms VolumeLogic.AsymptoticIdentityControls.finite_order_hides_next_coefficient
