import Std

namespace VolumeLogic

/-- A path with total outside degree at most N-1 belongs to the central,
left, or right support. The two one-sided supports cannot overlap. -/
theorem three_supports (N i t : Nat) (support : i + t ≤ N - 1) :
    ((i ≤ (N-1)/2 ∧ t ≤ (N-1)/2) ∨ (N-1)/2 < t ∨ (N-1)/2 < i) ∧
    ¬ ((N-1)/2 < i ∧ (N-1)/2 < t) := by
  omega

/-- On a left endpoint the strict cutoff is floor(N/2), at both parities. -/
theorem left_endpoint_cutoff (N j : Nat) (hN : 2 ≤ N) (hj : j < N) :
    ((N-1)/2 < N-1-j ↔ j < N/2) := by
  omega

theorem central_endpoint_even (m i j : Nat) (hm : 1 ≤ m) (hj : j < 2*m) :
    (i ≤ (2*m-1)/2 ∧ 2*m-1-j ≤ (2*m-1)/2) ↔ (i < m ∧ m ≤ j) := by
  omega

/-- The middle row at odd level belongs to the central support. -/
theorem central_endpoint_odd (m i j : Nat) (hj : j ≤ 2*m) :
    (i ≤ (2*m)/2 ∧ 2*m-j ≤ (2*m)/2) ↔ (i ≤ m ∧ m ≤ j) := by
  omega

/-- The sine-Cauchy moment matrix only uses moments strictly below N-1. -/
theorem protected_moment_degree (N i j : Nat) (hN : 2 ≤ N)
    (hi : i ≤ N/2-1) (hj : j ≤ N/2-1) : i+j ≤ N-2 := by
  omega

end VolumeLogic
