import Std

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R] [LE R] [LT R]
  [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-- Appendix P after the entropy and Hessian estimates, with all terms doubled.
The analytic estimates producing h, energy and defect are separate inputs. -/
theorem doubled_flattening_gain (t h energy defect : R)
    (ht : 0 ≤ t) (hsmall : t*energy ≤ h) :
    t*h - 2*(1-t)*defect ≤
      2*t*h - 2*(1-t)*defect - t*t*energy := by
  have hp : 0 ≤ h-t*energy := by grind
  have hprod := OrderedRing.mul_nonneg ht hp
  grind

theorem strict_weak_balance_gain (t h energy : R)
    (ht : 0 < t) (hh : 0 < h) (hsmall : t*energy ≤ h) :
    0 < 2*t*h-t*t*energy := by
  have ht0 : 0 ≤ t := by grind
  have gain := doubled_flattening_gain t h energy 0 ht0 hsmall
  have positive := OrderedRing.mul_pos ht hh
  grind

def total : List R → R
  | [] => 0
  | x :: xs => x + total xs

theorem total_nonnegative (xs : List R) (positive : ∀ x ∈ xs, 0 ≤ x) :
    0 ≤ total xs := by
  induction xs with
  | nil => simp [total]
  | cons x xs ih =>
    have hx := positive x (by simp)
    have hxs : ∀ y ∈ xs, 0 ≤ y := by
      intro y hy
      exact positive y (by simp [hy])
    have hi := ih hxs
    simp only [total]
    grind

/-- Additional nonnegative losses preserve a specified sector margin.
Strict positivity of that margin is imposed by the next theorem. -/
theorem nonempty_sector_gap (phi cost gap chosen : R) (others : List R)
    (hchosen : cost+gap ≤ chosen) (hothers : ∀ x ∈ others, 0 ≤ x) :
    phi+cost-(chosen+total others) ≤ phi-gap := by
  have hsum := total_nonnegative others hothers
  grind

theorem sector_strictly_below (phi cost gap chosen : R) (others : List R)
    (hgap : 0 < gap) (hchosen : cost+gap ≤ chosen)
    (hothers : ∀ x ∈ others, 0 ≤ x) :
    phi+cost-(chosen+total others) < phi := by
  have h := nonempty_sector_gap phi cost gap chosen others hchosen hothers
  grind

/-- The source gap must exceed the action drop caused by filling. -/
theorem filled_rate_gap (phi sourceGap actionDrop filledRate : R)
    (comparison : 2*actionDrop < sourceGap)
    (calibration : phi-actionDrop ≤ filledRate) :
    2*(phi-sourceGap) < 2*filledRate-sourceGap := by
  grind

theorem filled_remainder_strictly_below (phi sourceGap actionDrop filledRate : R)
    (hgap : 0 < sourceGap) (comparison : 2*actionDrop < sourceGap)
    (calibration : phi-actionDrop ≤ filledRate) :
    phi-sourceGap < filledRate := by
  have h := filled_rate_gap phi sourceGap actionDrop filledRate comparison calibration
  grind

end VolumeLogic
