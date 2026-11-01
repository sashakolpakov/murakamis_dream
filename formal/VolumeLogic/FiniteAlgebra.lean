import Std

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-- Coefficients in ascending powers; the empty list represents zero. -/
def horner : List R → R → R
  | [], _ => 0
  | a :: rest, z => a + z * horner rest z

/-- A polynomial divided difference, defined without division by z-w. -/
def dividedDifference : List R → R → R → R
  | [], _, _ => 0
  | _ :: rest, z, w => horner rest z + w * dividedDifference rest z w

theorem divided_difference_identity (a : List R) (z w : R) :
    horner a z - horner a w = (z-w)*dividedDifference a z w := by
  induction a with
  | nil => simp [horner, dividedDifference]; grind
  | cons a rest ih =>
    simp only [horner, dividedDifference]
    grind

/-- This is the scalar polynomial identity behind the resolvent numerator.
It does not need distinct roots or an inverse of z-w. -/
theorem annihilating_root_identity (a : List R) (z w : R)
    (root : horner a w = 0) :
    (z-w)*dividedDifference a z w = horner a z := by
  have h := divided_difference_identity a z w
  grind

/-- Clear denominators in the double-root Hermite calculation.
P and Q stand for the value and nilpotent terms of the resolvent. -/
theorem double_root_jet_identity (h0 h1 f0 f1 p q v0 v1 : R)
    (value : v0 = h0*q) (derivative : v1 = h0*p+h1*q) :
    h0*h0*(f0*p+f1*q) = h0*f0*v1+(h0*f1-h1*f0)*v0 := by
  grind

def product : List R → R
  | [] => 1
  | x :: xs => x * product xs

/-- Sum of all products choosing the first or second entry at each position. -/
def allChoices : List (R × R) → R
  | [] => 1
  | (a,b) :: xs => a*allChoices xs + b*allChoices xs

/-- The same sum with the all-first choice omitted. -/
def nonemptySecondChoices : List (R × R) → R
  | [] => 0
  | (a,b) :: xs => a*nonemptySecondChoices xs + b*allChoices xs

theorem all_choices_product (xs : List (R × R)) :
    allChoices xs = product (xs.map (fun p => p.1+p.2)) := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    rcases x with ⟨a,b⟩
    simp only [allChoices, List.map_cons, product]
    grind

/-- Appendix N: only the term with no differentiated coordinate is removed
by vanishing on the joint node grid. -/
theorem tensor_grid_subtraction (xs : List (R × R)) :
    nonemptySecondChoices xs =
      product (xs.map (fun p => p.1+p.2)) - product (xs.map Prod.fst) := by
  induction xs with
  | nil => simp [nonemptySecondChoices, product]; grind
  | cons x xs ih =>
    rcases x with ⟨a,b⟩
    have hp := all_choices_product xs
    simp only [nonemptySecondChoices, List.map_cons, product]
    grind

/-- An ordered product difference expanded without dividing by a factor. -/
def productDifference : List (R × R) → R
  | [] => 0
  | (a,b) :: xs => (a-b)*product (xs.map Prod.fst) + b*productDifference xs

theorem product_difference_identity (xs : List (R × R)) :
    productDifference xs = product (xs.map Prod.fst)-product (xs.map Prod.snd) := by
  induction xs with
  | nil => simp [productDifference, product]; grind
  | cons x xs ih =>
    rcases x with ⟨a,b⟩
    simp only [productDifference, List.map_cons, product]
    grind

end VolumeLogic
