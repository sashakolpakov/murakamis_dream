import Std

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R]

/-- A table of coefficients of h^a u^b. No analytic convergence is assumed. -/
abbrev BivariateCoefficients (R : Type u) := Nat → Nat → R

/-- The coefficients of B(h, hs), indexed by powers of h and s. -/
def regrade (B : BivariateCoefficients R) (n b : Nat) : R :=
  if b ≤ n then B (n - b) b else 0

/-- Reading the diagonal which originally held the coefficient of h^a u^b. -/
def recoverRegrading (D : BivariateCoefficients R) (a b : Nat) : R :=
  D (a + b) b

theorem regrade_coefficient_recovery (B : BivariateCoefficients R) (a b : Nat) :
    regrade B (a + b) b = B a b := by
  simp [regrade]

theorem recover_regrade (B : BivariateCoefficients R) :
    recoverRegrading (regrade B) = B := by
  funext a b
  exact regrade_coefficient_recovery B a b

theorem regrade_injective (B C : BivariateCoefficients R)
    (h : regrade B = regrade C) : B = C := by
  have hh := congrArg recoverRegrading h
  simpa only [recover_regrade] using hh

theorem regrade_zero :
    regrade (fun _ _ => (0 : R)) = (fun _ _ => 0) := by
  funext n b
  simp [regrade]

theorem regrade_zero_iff (B : BivariateCoefficients R) :
    regrade B = (fun _ _ => 0) ↔ B = (fun _ _ => 0) := by
  constructor
  · intro h
    apply regrade_injective B (fun _ _ => 0)
    simpa only [regrade_zero] using h
  · intro h
    rw [h, regrade_zero]

theorem regrade_add (B C : BivariateCoefficients R) :
    regrade (fun a b => B a b + C a b) =
      (fun n b => regrade B n b + regrade C n b) := by
  funext n b
  simp only [regrade]
  split <;> grind

theorem regrade_scalar (c : R) (B : BivariateCoefficients R) :
    regrade (fun a b => c * B a b) =
      (fun n b => c * regrade B n b) := by
  funext n b
  simp only [regrade]
  split <;> grind

theorem regrade_above_diagonal (B : BivariateCoefficients R) (n b : Nat)
    (h : n < b) : regrade B n b = 0 := by
  simp [regrade, Nat.not_le.mpr h]

/-- Every coefficient table supported in b ≤ n has a unique preimage. -/
theorem regrade_recover (D : BivariateCoefficients R)
    (support : ∀ n b, n < b → D n b = 0) :
    regrade (recoverRegrading D) = D := by
  funext n b
  by_cases h : b ≤ n
  · simp [regrade, recoverRegrading, h, Nat.sub_add_cancel h]
  · simp [regrade, h, support n b (Nat.lt_of_not_ge h)]

/-- Seeing orders at most L in h recovers exactly a+b ≤ L, not all of B. -/
theorem regrade_finite_order_iff (B C : BivariateCoefficients R) (L : Nat) :
    (∀ n b, n ≤ L → regrade B n b = regrade C n b) ↔
    (∀ a b, a + b ≤ L → B a b = C a b) := by
  constructor
  · intro h a b hab
    simpa only [regrade_coefficient_recovery] using h (a + b) b hab
  · intro h n b hn
    by_cases hb : b ≤ n
    · have hab : n - b + b ≤ L := by omega
      simpa [regrade, hb] using h (n - b) b hab
    · simp [regrade, hb]

/-- The formal monomial h^(L+1) is invisible in every order at most L. -/
def hiddenRegradingTerm (L : Nat) (a b : Nat) : R :=
  if a = L + 1 ∧ b = 0 then 1 else 0

theorem hidden_regrading_term_truncates (L n b : Nat) (hn : n ≤ L) :
    regrade (hiddenRegradingTerm (R := R) L) n b = 0 := by
  by_cases hb : b ≤ n
  · have impossible : ¬(n - b = L + 1 ∧ b = 0) := by omega
    simp [regrade, hiddenRegradingTerm, hb, impossible]
  · simp [regrade, hb]

theorem hidden_regrading_term_nonzero (L : Nat) (h10 : (1 : R) ≠ 0) :
    hiddenRegradingTerm (R := R) L ≠ (fun _ _ => 0) := by
  intro h
  have hval := congrFun (congrFun h (L + 1)) 0
  exact h10 (by simpa [hiddenRegradingTerm] using hval)

end VolumeLogic
