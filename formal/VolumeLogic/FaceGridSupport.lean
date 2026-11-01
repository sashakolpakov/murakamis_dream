import Std

namespace VolumeLogic

/-!
The exponent argument used after root-grid character orthogonality.
An ordinary face selected by the grid has exponent congruent to N-1.
Nonnegative exponents and the total-degree bound then force the one
target monomial, including zero at both protected faces.

This module proves the support argument. It does not construct the
physical face grid, prove character orthogonality, or identify the
polynomial with the original marked tensor contraction.
-/

theorem residue_target_lower (N k : Nat) (h : k % N = N - 1) :
    N - 1 ≤ k := by
  have hm := Nat.mod_le k N
  omega

theorem list_sum_lower (d : Nat) (xs : List Nat)
    (h : ∀ x ∈ xs, d ≤ x) : xs.length * d ≤ xs.sum := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    have hx : d ≤ x := h x (by simp)
    have ht : ∀ y ∈ xs, d ≤ y := by
      intro y hy
      exact h y (by simp [hy])
    have hs := ih ht
    simp only [List.length_cons, List.sum_cons, Nat.add_mul, Nat.one_mul]
    omega

/-- A nonnegative total-degree budget exhausted by the ordinary targets
leaves no degree at either protected face. -/
theorem face_budget_saturation (d a b : Nat) (xs : List Nat)
    (lower : ∀ x ∈ xs, d ≤ x)
    (budget : a + b + xs.sum ≤ xs.length * d) :
    a = 0 ∧ b = 0 ∧ xs = List.replicate xs.length d := by
  have hs := list_sum_lower d xs lower
  have ha : a = 0 := by omega
  have hb : b = 0 := by omega
  refine ⟨ha, hb, ?_⟩
  have upper : xs.sum ≤ xs.length * d := by omega
  clear budget hs ha hb
  induction xs with
  | nil => simp
  | cons x xs ih =>
    have hx : d ≤ x := lower x (by simp)
    have ht : ∀ y ∈ xs, d ≤ y := by
      intro y hy
      exact lower y (by simp [hy])
    have hs := list_sum_lower d xs ht
    simp only [List.length_cons, List.sum_cons, Nat.add_mul, Nat.one_mul] at upper
    have heq : x = d := by omega
    have hu : xs.sum ≤ xs.length * d := by omega
    have tail := ih ht hu
    simp only [List.length_cons, List.replicate_succ]
    simpa only [heq] using congrArg (fun ys => d :: ys) tail

/-- After Fourier selection, the ordinary congruences and homogeneous
degree bound already force both protected exponents to vanish.
No separate congruence hypothesis at a protected face is needed. -/
theorem face_grid_unique_exponents (N a b : Nat) (xs : List Nat)
    (residues : ∀ x ∈ xs, x % N = N - 1)
    (budget : a + b + xs.sum ≤ xs.length * (N - 1)) :
    a = 0 ∧ b = 0 ∧ xs = List.replicate xs.length (N - 1) := by
  apply face_budget_saturation (N - 1) a b xs _ budget
  intro x hx
  exact residue_target_lower N x (residues x hx)

/-- If the numerator has less than the target total degree, every
monomial is rejected by at least one ordinary-face grid. -/
theorem face_grid_below_target (N a b : Nat) (xs : List Nat)
    (budget : a + b + xs.sum < xs.length * (N - 1)) :
    ¬ (∀ x ∈ xs, x % N = N - 1) := by
  intro residues
  have hs := list_sum_lower (N - 1) xs (by
    intro x hx
    exact residue_target_lower N x (residues x hx))
  omega

/-- The exact support selector after averaging every free face grid.
The exterior protected face is not averaged; its exponent is forced
to zero by the degree budget. -/
theorem face_grid_selection_iff (N a b : Nat) (xs : List Nat)
    (positive : 0 < N)
    (budget : a + b + xs.sum ≤ xs.length * (N - 1)) :
    (b % N = 0 ∧ ∀ x ∈ xs, x % N = N - 1) ↔
      (a = 0 ∧ b = 0 ∧ xs = List.replicate xs.length (N - 1)) := by
  constructor
  · intro h
    exact face_grid_unique_exponents N a b xs h.2 budget
  · rintro ⟨ha, hb, ht⟩
    refine ⟨by simp [hb], ?_⟩
    intro x hx
    rw [ht] at hx
    simp only [List.mem_replicate] at hx
    have heq : x = N - 1 := by omega
    rw [heq]
    exact Nat.mod_eq_of_lt (by omega)

end VolumeLogic
