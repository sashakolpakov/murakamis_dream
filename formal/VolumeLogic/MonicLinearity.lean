import VolumeLogic.MonicRemainder

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-- Scalar multiplication of the actual ascending coefficient list. -/
def polyScale (c : R) : List R → List R
  | [] => []
  | a::f => (c*a)::polyScale c f

@[simp]
theorem coefficient_polyScale (c : R) (f : List R) (n : Nat) :
    coefficient (polyScale c f) n = c * coefficient f n := by
  induction f generalizing n with
  | nil => simp [polyScale, coefficient]; grind
  | cons a f ih =>
    cases n with
    | zero => rfl
    | succ n => exact ih n

theorem horner_zero_of_coefficients_zero (f : List R) (z : R)
    (h : ∀ n, coefficient f n = 0) : horner f z = 0 := by
  induction f with
  | nil => rfl
  | cons a f ih =>
    have ha : a = 0 := h 0
    have hf : ∀ n, coefficient f n = 0 := fun n => h (n+1)
    simp only [horner]
    rw [ha, ih hf]
    grind

/-- Coefficient equality, including arbitrary zero padding, preserves evaluation. -/
theorem horner_congr {f g : List R} (h : CoeffEq f g) (z : R) :
    horner f z = horner g z := by
  induction f generalizing g with
  | nil =>
    have hg : ∀ n, coefficient g n = 0 := fun n => (h n).symm
    exact (horner_zero_of_coefficients_zero g z hg).symm
  | cons a f ih =>
    cases g with
    | nil =>
      have hf : ∀ n, coefficient (a::f) n = 0 := fun n => h n
      exact horner_zero_of_coefficients_zero (a::f) z hf
    | cons b g =>
      have hab : a = b := h 0
      have hfg : CoeffEq f g := fun n => h (n+1)
      simp only [horner]
      rw [hab, ih hfg]

@[simp]
theorem horner_polyAdd (f g : List R) (z : R) :
    horner (polyAdd f g) z = horner f z + horner g z := by
  induction f generalizing g with
  | nil => simp [polyAdd, horner]; grind
  | cons a f ih =>
    cases g with
    | nil => simp [polyAdd, horner]; grind
    | cons b g =>
      simp only [polyAdd, horner]
      rw [ih]
      grind

@[simp]
theorem horner_polyScale (c : R) (f : List R) (z : R) :
    horner (polyScale c f) z = c * horner f z := by
  induction f with
  | nil => simp [polyScale, horner]; grind
  | cons a f ih =>
    simp only [polyScale, horner]
    rw [ih]
    grind

theorem coefficient_drop (f : List R) (k n : Nat) :
    coefficient (f.drop k) n = coefficient f (k+n) := by
  induction k generalizing f with
  | zero => simp
  | succ k ih =>
    cases f with
    | nil => simp [coefficient]
    | cons a f => simpa [List.drop, coefficient, Nat.succ_add] using ih f

theorem coeffEq_drop {f g : List R} (h : CoeffEq f g) (k : Nat) :
    CoeffEq (f.drop k) (g.drop k) := by
  intro n
  rw [coefficient_drop, coefficient_drop, h (k+n)]

/-- Each synthetic-quotient coefficient is an evaluation of the actual tail.
This identity also covers empty lists and trailing zero coefficients. -/
theorem coefficient_synthetic (r : R) (f : List R) (n : Nat) :
    coefficient (synthetic r f) n = horner (f.drop (n+1)) r := by
  induction f generalizing n with
  | nil => simp [synthetic, coefficient, horner]
  | cons a f ih =>
    cases f with
    | nil => simp [synthetic, coefficient, horner]
    | cons b f =>
      cases n with
      | zero => rfl
      | succ n => simpa only [synthetic, coefficient, List.drop_succ_cons] using ih n

theorem synthetic_congr (r : R) {f g : List R} (h : CoeffEq f g) :
    CoeffEq (synthetic r f) (synthetic r g) := by
  intro n
  rw [coefficient_synthetic, coefficient_synthetic]
  exact horner_congr (coeffEq_drop h (n+1)) r

theorem synthetic_polyAdd (r : R) (f g : List R) :
    CoeffEq (synthetic r (polyAdd f g))
      (polyAdd (synthetic r f) (synthetic r g)) := by
  intro n
  rw [coefficient_synthetic, coefficient_polyAdd,
    coefficient_synthetic, coefficient_synthetic]
  have hd : CoeffEq ((polyAdd f g).drop (n+1))
      (polyAdd (f.drop (n+1)) (g.drop (n+1))) := by
    intro k
    simp only [coefficient_drop, coefficient_polyAdd]
  rw [horner_congr hd r, horner_polyAdd]

theorem synthetic_polyScale (r c : R) (f : List R) :
    CoeffEq (synthetic r (polyScale c f)) (polyScale c (synthetic r f)) := by
  intro n
  rw [coefficient_synthetic, coefficient_polyScale, coefficient_synthetic]
  have hd : CoeffEq ((polyScale c f).drop (n+1))
      (polyScale c (f.drop (n+1))) := by
    intro k
    simp only [coefficient_drop, coefficient_polyScale]
  rw [horner_congr hd r, horner_polyScale]

/-- Newton reconstruction is independent of every coefficient-equivalent
representation. Its fixed output length makes this literal list equality. -/
theorem monicRemainder_congr (roots : List R) {f g : List R} (h : CoeffEq f g) :
    monicRemainder roots f = monicRemainder roots g := by
  induction roots generalizing f g with
  | nil => rfl
  | cons r roots ih =>
    simp only [monicRemainder]
    rw [horner_congr h r, ih (synthetic_congr r h)]

/-- Addition is proved for the constructed remainder, coefficient by coefficient. -/
theorem monicRemainder_polyAdd (roots f g : List R) :
    CoeffEq (monicRemainder roots (polyAdd f g))
      (polyAdd (monicRemainder roots f) (monicRemainder roots g)) := by
  induction roots generalizing f g with
  | nil => exact coeffEq_refl []
  | cons r roots ih =>
    have hc := monicRemainder_congr roots (synthetic_polyAdd r f g)
    have hi := ih (synthetic r f) (synthetic r g)
    intro n
    cases n with
    | zero =>
      simp only [monicRemainder, coefficient_polyAdd,
        coefficient_addConstant_zero, coefficient_timesLinear_zero, horner_polyAdd]
      rw [hc]
      have h := hi 0
      simp only [coefficient_polyAdd] at h
      rw [h]
      grind
    | succ n =>
      simp only [monicRemainder, coefficient_polyAdd,
        coefficient_addConstant_succ, coefficient_timesLinear_succ]
      rw [hc]
      have h0 := hi n
      have h1 := hi (n+1)
      simp only [coefficient_polyAdd] at h0 h1
      rw [h0, h1]
      grind

theorem monicRemainder_polyScale (roots : List R) (c : R) (f : List R) :
    CoeffEq (monicRemainder roots (polyScale c f))
      (polyScale c (monicRemainder roots f)) := by
  induction roots generalizing f with
  | nil => exact coeffEq_refl []
  | cons r roots ih =>
    have hc := monicRemainder_congr roots (synthetic_polyScale r c f)
    have hi := ih (synthetic r f)
    intro n
    cases n with
    | zero =>
      simp only [monicRemainder, coefficient_polyScale,
        coefficient_addConstant_zero, coefficient_timesLinear_zero, horner_polyScale]
      rw [hc]
      have h := hi 0
      simp only [coefficient_polyScale] at h
      rw [h]
      grind
    | succ n =>
      simp only [monicRemainder, coefficient_polyScale,
        coefficient_addConstant_succ, coefficient_timesLinear_succ]
      rw [hc]
      have h0 := hi n
      have h1 := hi (n+1)
      simp only [coefficient_polyScale] at h0 h1
      rw [h0, h1]
      grind

theorem newtonFunctional_congr (roots : List R) {f g : List R} (h : CoeffEq f g) :
    newtonFunctional roots f = newtonFunctional roots g := by
  rw [← top_coefficient_is_newton, ← top_coefficient_is_newton,
    monicRemainder_congr roots h]

theorem newtonFunctional_polyAdd (roots f g : List R) :
    newtonFunctional roots (polyAdd f g) =
      newtonFunctional roots f + newtonFunctional roots g := by
  have h := monicRemainder_polyAdd roots f g (roots.length-1)
  simpa only [coefficient_polyAdd, top_coefficient_is_newton] using h

theorem newtonFunctional_polyScale (roots : List R) (c : R) (f : List R) :
    newtonFunctional roots (polyScale c f) = c * newtonFunctional roots f := by
  have h := monicRemainder_polyScale roots c f (roots.length-1)
  simpa only [coefficient_polyScale, top_coefficient_is_newton] using h

/-- Adding an actual constructed monic multiple leaves the remainder unchanged
coefficientwise. No quotient relation is assumed as a substitute for division. -/
theorem monicRemainder_add_multiple (roots f q : List R) :
    CoeffEq (monicRemainder roots (polyAdd f (monicMultiple roots q)))
      (monicRemainder roots f) := by
  have ha := monicRemainder_polyAdd roots f (monicMultiple roots q)
  have hz := monicRemainder_annihilates_multiple roots q
  intro n
  have h := ha n
  have h0 := hz n
  simp only [coefficient_polyAdd, coefficient] at h h0
  rw [h0] at h
  grind

/-- The constructed functional descends under formal monic congruence,
including noncanonical input lists and repeated roots. -/
theorem newtonFunctional_quotient_invariant (roots f g q : List R)
    (h : CoeffEq f (polyAdd g (monicMultiple roots q))) :
    newtonFunctional roots f = newtonFunctional roots g := by
  rw [newtonFunctional_congr roots h, newtonFunctional_polyAdd,
    newtonFunctional_annihilates_multiple]
  grind

theorem monicRemainder_quotient_invariant (roots f g q : List R)
    (h : CoeffEq f (polyAdd g (monicMultiple roots q))) :
    CoeffEq (monicRemainder roots f) (monicRemainder roots g) := by
  rw [monicRemainder_congr roots h]
  exact monicRemainder_add_multiple roots g q

theorem coefficient_replicate_zero (k n : Nat) :
    coefficient (List.replicate k (0 : R)) n = 0 := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    cases n with
    | zero => rfl
    | succ n => exact ih n

/-- Appending any number of actual zero entries preserves every coefficient. -/
theorem coeffEq_append_zeros (f : List R) (k : Nat) :
    CoeffEq (f ++ List.replicate k (0 : R)) f := by
  induction f with
  | nil => intro n; exact coefficient_replicate_zero k n
  | cons a f ih =>
    intro n
    cases n with
    | zero => rfl
    | succ n => exact ih n

theorem monicRemainder_append_zeros (roots f : List R) (k : Nat) :
    monicRemainder roots (f ++ List.replicate k (0 : R)) =
      monicRemainder roots f :=
  monicRemainder_congr roots (coeffEq_append_zeros f k)

theorem newtonFunctional_append_zeros (roots f : List R) (k : Nat) :
    newtonFunctional roots (f ++ List.replicate k (0 : R)) =
      newtonFunctional roots f :=
  newtonFunctional_congr roots (coeffEq_append_zeros f k)

end VolumeLogic
