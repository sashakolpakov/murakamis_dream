import VolumeLogic.FiniteAlgebra

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-- Coefficient lookup; trailing zero coefficients do not change a polynomial. -/
def coefficient : List R → Nat → R
  | [], _ => 0
  | a :: _, 0 => a
  | _ :: rest, n+1 => coefficient rest n

/-- Equality of formal coefficient arrays, not equality merely of their values. -/
def CoeffEq (a b : List R) : Prop := ∀ n, coefficient a n = coefficient b n

/-- Add a constant coefficient. -/
def addConstant (a : R) : List R → List R
  | [] => [a]
  | b :: rest => (a+b) :: rest

/-- Exact multiplication by X-r, with one harmless trailing zero for the zero list. -/
def timesLinear (r : R) : List R → List R
  | [] => [0]
  | a :: rest => (-r*a) :: addConstant a (timesLinear r rest)

/-- Synthetic quotient of f(X)-f(r) by X-r, using no division in the ring. -/
def synthetic (r : R) : List R → List R
  | [] => []
  | [_] => []
  | _ :: b :: rest => horner (b :: rest) r :: synthetic r (b :: rest)

@[simp]
theorem coefficient_addConstant_zero (a : R) (f : List R) :
    coefficient (addConstant a f) 0 = a + coefficient f 0 := by
  cases f <;> simp [coefficient, addConstant] <;> grind

@[simp]
theorem coefficient_addConstant_succ (a : R) (f : List R) (n : Nat) :
    coefficient (addConstant a f) (n+1) = coefficient f (n+1) := by
  cases f <;> simp [coefficient, addConstant]

@[simp]
theorem coefficient_timesLinear_zero (r : R) (f : List R) :
    coefficient (timesLinear r f) 0 = -r * coefficient f 0 := by
  cases f <;> simp [timesLinear, coefficient] <;> grind

@[simp]
theorem coefficient_timesLinear_succ (r : R) (f : List R) (n : Nat) :
    coefficient (timesLinear r f) (n+1) =
      coefficient f n - r * coefficient f (n+1) := by
  induction f generalizing n with
  | nil => simp [timesLinear, coefficient]; grind
  | cons a rest ih =>
    cases n with
    | zero => simp [timesLinear, coefficient]; grind
    | succ n =>
      simp only [timesLinear, coefficient, coefficient_addConstant_succ]
      have h := ih n
      grind

@[simp]
theorem horner_addConstant (a : R) (f : List R) (z : R) :
    horner (addConstant a f) z = a + horner f z := by
  cases f <;> simp [addConstant, horner] <;> grind

@[simp]
theorem horner_timesLinear (r : R) (f : List R) (z : R) :
    horner (timesLinear r f) z = (z-r)*horner f z := by
  induction f with
  | nil => simp [timesLinear, horner]; grind
  | cons a rest ih =>
    simp only [timesLinear, horner, horner_addConstant]
    grind

/-- A literal list identity for the synthetic-division reconstruction. -/
theorem synthetic_reconstruct_nonempty (r a : R) (rest : List R) :
    addConstant (horner (a::rest) r) (timesLinear r (synthetic r (a::rest))) = a::rest := by
  induction rest generalizing a with
  | nil => simp [synthetic, timesLinear, addConstant, horner]; grind
  | cons b rest ih =>
    simp only [synthetic, timesLinear, addConstant, horner]
    have h := ih b
    simp only [horner] at h
    congr 1
    · grind

/-- The identity holds coefficientwise also for the empty representation of zero. -/
theorem synthetic_reconstruct (r : R) (f : List R) :
    CoeffEq (addConstant (horner f r) (timesLinear r (synthetic r f))) f := by
  cases f with
  | nil => intro n; cases n <;> simp [synthetic, timesLinear, addConstant, horner, coefficient] <;> grind
  | cons a rest => rw [synthetic_reconstruct_nonempty]; intro n; rfl

/-- The polynomial quotient evaluates to the division-free divided difference. -/
theorem synthetic_horner (r z : R) (f : List R) :
    horner (synthetic r f) z = dividedDifference f r z := by
  induction f with
  | nil => rfl
  | cons a rest ih =>
    cases rest with
    | nil => simp [synthetic, dividedDifference, horner]; grind
    | cons b rest =>
      simp only [synthetic, horner, dividedDifference] at *
      grind


/-- Formal polynomial addition, with ascending coefficients. -/
def polyAdd : List R → List R → List R
  | [], g => g
  | f, [] => f
  | a::f, b::g => (a+b)::polyAdd f g

@[simp]
theorem coefficient_polyAdd (f g : List R) (n : Nat) :
    coefficient (polyAdd f g) n = coefficient f n + coefficient g n := by
  induction f generalizing g n with
  | nil => simp [polyAdd, coefficient]; grind
  | cons a f ih =>
    cases g with
    | nil => simp [polyAdd, coefficient]; grind
    | cons b g =>
      cases n with
      | zero => rfl
      | succ n => exact ih g n

theorem coeffEq_refl (f : List R) : CoeffEq f f := fun _ => rfl

theorem coeffEq_symm {f g : List R} (h : CoeffEq f g) : CoeffEq g f :=
  fun n => (h n).symm

theorem coeffEq_trans {f g h : List R} (a : CoeffEq f g) (b : CoeffEq g h) :
    CoeffEq f h := fun n => (a n).trans (b n)

theorem timesLinear_congr (r : R) {f g : List R} (h : CoeffEq f g) :
    CoeffEq (timesLinear r f) (timesLinear r g) := by
  intro n
  cases n with
  | zero => simp only [coefficient_timesLinear_zero]; rw [h 0]
  | succ n => simp only [coefficient_timesLinear_succ]; rw [h n, h (n+1)]

theorem addConstant_congr (a : R) {f g : List R} (h : CoeffEq f g) :
    CoeffEq (addConstant a f) (addConstant a g) := by
  intro n
  cases n with
  | zero => simp only [coefficient_addConstant_zero]; rw [h 0]
  | succ n => simp only [coefficient_addConstant_succ]; exact h (n+1)

/-- Polynomial multiplication by a split monic polynomial.
Repeated entries are allowed; no distinctness or nonzero differences are assumed. -/
def monicMultiple : List R → List R → List R
  | [], f => f
  | r::roots, f => timesLinear r (monicMultiple roots f)

/-- Successive synthetic division gives the ordinary quotient by the monic product. -/
def monicQuotient : List R → List R → List R
  | [], f => f
  | r::roots, f => monicQuotient roots (synthetic r f)

/-- Newton reconstruction of the remainder, still in ordinary monomial coefficients. -/
def monicRemainder : List R → List R → List R
  | [], _ => []
  | r::roots, f => addConstant (horner f r)
      (timesLinear r (monicRemainder roots (synthetic r f)))

/-- Exact formal-coefficient Euclidean division, over any commutative ring.
The multiplier is the explicit monic polynomial ∏(X-r), not an assumed quotient relation. -/
theorem monic_division_identity (roots f : List R) :
    CoeffEq f (polyAdd (monicMultiple roots (monicQuotient roots f))
      (monicRemainder roots f)) := by
  induction roots generalizing f with
  | nil => intro n; simp [monicMultiple, monicQuotient, monicRemainder, coefficient]; grind
  | cons r roots ih =>
    have hs := synthetic_reconstruct r f
    have hq := ih (synthetic r f)
    have ht := addConstant_congr (horner f r) (timesLinear_congr r hq)
    intro n
    have h := (hs n).symm.trans (ht n)
    cases n with
    | zero =>
      simp only [coefficient_addConstant_zero, coefficient_timesLinear_zero,
        coefficient_polyAdd] at h
      simp only [monicMultiple, monicQuotient, monicRemainder,
        coefficient_polyAdd, coefficient_addConstant_zero, coefficient_timesLinear_zero]
      grind
    | succ n =>
      simp only [coefficient_addConstant_succ, coefficient_timesLinear_succ,
        coefficient_polyAdd] at h
      simp only [monicMultiple, monicQuotient, monicRemainder,
        coefficient_polyAdd, coefficient_addConstant_succ, coefficient_timesLinear_succ]
      grind

@[simp]
theorem timesLinear_length (r : R) (f : List R) :
    (timesLinear r f).length = f.length+1 := by
  induction f with
  | nil => rfl
  | cons a f ih =>
    simp only [timesLinear, List.length_cons]
    cases h : timesLinear r f with
    | nil => simp [h] at ih
    | cons b rest => simp [addConstant]; simp [h] at ih; omega

@[simp]
theorem monicRemainder_length (roots f : List R) :
    (monicRemainder roots f).length = roots.length := by
  induction roots generalizing f with
  | nil => rfl
  | cons r roots ih =>
    simp only [monicRemainder, List.length_cons]
    have hl := timesLinear_length r (monicRemainder roots (synthetic r f))
    cases h : timesLinear r (monicRemainder roots (synthetic r f)) with
    | nil => simp [h] at hl
    | cons a rest =>
      simp [addConstant]
      have hi := ih (synthetic r f)
      simp [h] at hl
      omega

theorem coefficient_eq_zero_of_length_le (f : List R) (n : Nat)
    (h : f.length ≤ n) : coefficient f n = 0 := by
  induction f generalizing n with
  | nil => rfl
  | cons a f ih =>
    cases n with
    | zero => simp at h
    | succ n => exact ih n (by simpa using h)

/-- The remainder has degree strictly below the degree of the monic product. -/
theorem monic_remainder_degree_bound (roots f : List R) (n : Nat)
    (h : roots.length ≤ n) : coefficient (monicRemainder roots f) n = 0 := by
  apply coefficient_eq_zero_of_length_le
  simpa only [monicRemainder_length] using h

/-- Iterated divided difference with repeated nodes retained by synthetic division. -/
def newtonFunctional : List R → List R → R
  | [], _ => 0
  | [r], f => horner f r
  | r::s::roots, f => newtonFunctional (s::roots) (synthetic r f)

/-- The top coefficient of the explicit monic remainder is its confluent Newton functional. -/
theorem top_coefficient_is_newton (roots f : List R) :
    coefficient (monicRemainder roots f) (roots.length-1) = newtonFunctional roots f := by
  induction roots generalizing f with
  | nil => rfl
  | cons r roots ih =>
    cases roots with
    | nil => simp [monicRemainder, timesLinear, addConstant, coefficient, newtonFunctional]; grind
    | cons s roots =>
      change coefficient (addConstant (horner f r)
        (timesLinear r (monicRemainder (s::roots) (synthetic r f))))
        (roots.length+1+1-1) = newtonFunctional (s::roots) (synthetic r f)
      have he : roots.length+1+1-1 = roots.length+1 := by omega
      rw [he, coefficient_addConstant_succ, coefficient_timesLinear_succ]
      have hz := monic_remainder_degree_bound (s::roots) (synthetic r f)
        (roots.length+1) (by simp)
      have hi := ih (synthetic r f)
      simp only [List.length_cons] at hi
      have hn : roots.length+1-1 = roots.length := by omega
      rw [hn] at hi
      rw [hz, hi]
      grind

/-- For two nodes the top trace is precisely the previously defined divided difference.
This theorem includes coincident nodes. -/
theorem two_node_top_coefficient (r s : R) (f : List R) :
    coefficient (monicRemainder [r,s] f) 1 = dividedDifference f r s := by
  have h := top_coefficient_is_newton [r,s] f
  simpa only [List.length_cons, List.length_nil, newtonFunctional, synthetic_horner] using h


/-- The modulus itself, with a literal leading coefficient one. -/
def monicPolynomial (roots : List R) : List R := monicMultiple roots [1]

@[simp]
theorem monicMultiple_length (roots f : List R) :
    (monicMultiple roots f).length = roots.length+f.length := by
  induction roots with
  | nil => simp [monicMultiple]
  | cons r roots ih => simp only [monicMultiple, timesLinear_length, List.length_cons]; omega

theorem monicPolynomial_monic (roots : List R) :
    coefficient (monicPolynomial roots) roots.length = 1 := by
  induction roots with
  | nil => rfl
  | cons r roots ih =>
    change coefficient (timesLinear r (monicMultiple roots [1])) (roots.length+1) = 1
    rw [coefficient_timesLinear_succ]
    have hz := coefficient_eq_zero_of_length_le (monicMultiple roots [1])
      (roots.length+1) (by simp)
    change coefficient (monicMultiple roots [1]) roots.length = 1 at ih
    rw [hz, ih]
    grind

@[simp]
theorem synthetic_length (r : R) (f : List R) :
    (synthetic r f).length = f.length-1 := by
  induction f with
  | nil => rfl
  | cons a f ih =>
    cases f with
    | nil => rfl
    | cons b f => simp only [synthetic, List.length_cons] at *; omega

@[simp]
theorem monicQuotient_length (roots f : List R) :
    (monicQuotient roots f).length = f.length-roots.length := by
  induction roots generalizing f with
  | nil => simp [monicQuotient]
  | cons r roots ih => simp only [monicQuotient, ih, synthetic_length, List.length_cons]; omega

theorem monicMultiple_zero (roots : List R) : CoeffEq (monicMultiple roots ([] : List R)) [] := by
  induction roots with
  | nil => exact coeffEq_refl []
  | cons r roots ih =>
    intro n
    cases n with
    | zero =>
      simp only [monicMultiple, coefficient_timesLinear_zero, coefficient]
      have h := ih 0
      simp only [coefficient] at h
      rw [h]; grind
    | succ n =>
      simp only [monicMultiple, coefficient_timesLinear_succ, coefficient]
      have h0 := ih n
      have h1 := ih (n+1)
      simp only [coefficient] at h0 h1
      rw [h0, h1]; grind

/-- Inputs already below the modulus degree are unchanged, coefficient by coefficient. -/
theorem monicRemainder_of_degree_lt (roots f : List R) (h : f.length ≤ roots.length) :
    CoeffEq (monicRemainder roots f) f := by
  have hl := monicQuotient_length roots f
  have hq : monicQuotient roots f = [] := by
    cases hq : monicQuotient roots f with
    | nil => rfl
    | cons a rest => simp [hq] at hl; omega
  have hd := monic_division_identity roots f
  rw [hq] at hd
  have hz := monicMultiple_zero (R:=R) roots
  intro n
  have hd' := hd n
  have hz' := hz n
  simp only [coefficient_polyAdd, coefficient] at hd' hz'
  grind

/-- Normalization of the trace on every polynomial of degree less than the modulus. -/
theorem newtonFunctional_of_degree_lt (roots f : List R) (h : f.length ≤ roots.length) :
    newtonFunctional roots f = coefficient f (roots.length-1) := by
  rw [← top_coefficient_is_newton]
  exact monicRemainder_of_degree_lt roots f h (roots.length-1)

@[simp]
theorem synthetic_addConstant (r a : R) (f : List R) :
    synthetic r (addConstant a f) = synthetic r f := by
  cases f with
  | nil => rfl
  | cons b rest => cases rest <;> rfl

theorem synthetic_cons (r a : R) (f : List R) (h : f ≠ []) :
    synthetic r (a::f) = horner f r :: synthetic r f := by
  cases f with
  | nil => exact False.elim (h rfl)
  | cons b rest => rfl

@[simp]
theorem synthetic_timesLinear (r : R) (f : List R) :
    synthetic r (timesLinear r f) = f := by
  induction f with
  | nil => rfl
  | cons a f ih =>
    rw [timesLinear, synthetic_cons r (-r*a) (addConstant a (timesLinear r f))]
    · rw [horner_addConstant, horner_timesLinear, synthetic_addConstant, ih]
      congr 1
      grind
    · cases timesLinear r f <;> simp [addConstant]

/-- Monic multiples have zero remainder, including at repeated roots. -/
theorem monicRemainder_annihilates_multiple (roots q : List R) :
    CoeffEq (monicRemainder roots (monicMultiple roots q)) [] := by
  induction roots generalizing q with
  | nil => exact coeffEq_refl []
  | cons r roots ih =>
    have ht := timesLinear_congr r (ih q)
    have ha := addConstant_congr ((r-r)*horner (monicMultiple roots q) r) ht
    intro n
    simp only [monicRemainder, monicMultiple, horner_timesLinear, synthetic_timesLinear]
    have h := ha n
    cases n with
    | zero =>
      simp only [coefficient_addConstant_zero, timesLinear, coefficient] at h ⊢
      grind
    | succ n =>
      simp only [coefficient_addConstant_succ, timesLinear, coefficient] at h ⊢
      grind

/-- The top-coefficient functional kills the ideal generated by the monic modulus. -/
theorem newtonFunctional_annihilates_multiple (roots q : List R) :
    newtonFunctional roots (monicMultiple roots q) = 0 := by
  rw [← top_coefficient_is_newton]
  exact monicRemainder_annihilates_multiple roots q (roots.length-1)

/-- Formal differentiation of a Horner polynomial, evaluated at z.
This is an algebraic derivative; no topology or analytic differentiability is assumed. -/
def formalDerivativeValue : List R → R → R
  | [], _ => 0
  | _::rest, z => horner rest z + z*formalDerivativeValue rest z

theorem diagonal_divided_difference (f : List R) (z : R) :
    dividedDifference f z z = formalDerivativeValue f z := by
  induction f with
  | nil => rfl
  | cons a rest ih => simp only [dividedDifference, formalDerivativeValue]; rw [ih]

/-- The double-root trace really differentiates; coincident roots are not discarded. -/
theorem double_root_top_coefficient (r : R) (f : List R) :
    coefficient (monicRemainder [r,r] f) 1 = formalDerivativeValue f r := by
  rw [two_node_top_coefficient, diagonal_divided_difference]

/-- The full linear remainder modulo (X-r)^2, with its constant and first-normal term. -/
theorem double_root_remainder (r : R) (f : List R) :
    monicRemainder [r,r] f =
      [horner f r - r*formalDerivativeValue f r, formalDerivativeValue f r] := by
  have h := synthetic_horner r r f
  rw [diagonal_divided_difference] at h
  simp only [monicRemainder, timesLinear, addConstant]
  rw [h]
  congr 1
  · grind
  · congr 1
    grind


end VolumeLogic
