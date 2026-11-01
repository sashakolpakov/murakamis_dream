import VolumeLogic.MonicUniqueness

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-- Multiplication of the actual ascending coefficient lists. -/
def polyMul : List R → List R → List R
  | [], _ => []
  | a::f, g => polyAdd (polyScale a g) (0::polyMul f g)

theorem polyAdd_congr {f f' g g' : List R}
    (hf : CoeffEq f f') (hg : CoeffEq g g') :
    CoeffEq (polyAdd f g) (polyAdd f' g') := by
  intro n
  simp only [coefficient_polyAdd]
  rw [hf n, hg n]

theorem polyScale_congr (c : R) {f g : List R} (h : CoeffEq f g) :
    CoeffEq (polyScale c f) (polyScale c g) := by
  intro n
  simp only [coefficient_polyScale]
  rw [h n]

theorem shift_congr {f g : List R} (h : CoeffEq f g) :
    CoeffEq ((0 : R)::f) (0::g) := by
  intro n
  cases n with
  | zero => rfl
  | succ n => exact h n

theorem polyMul_zero_right (f : List R) : CoeffEq (polyMul f []) [] := by
  induction f with
  | nil => exact coeffEq_refl []
  | cons a f ih =>
    intro n
    cases n with
    | zero => simp [polyMul, coefficient, polyScale]; grind
    | succ n =>
      have h := ih n
      simp only [polyMul, polyScale, coefficient_polyAdd, coefficient] at *
      grind

theorem polyMul_congr_right (f : List R) {g g' : List R}
    (h : CoeffEq g g') : CoeffEq (polyMul f g) (polyMul f g') := by
  induction f with
  | nil => exact coeffEq_refl []
  | cons a f ih => exact polyAdd_congr (polyScale_congr a h) (shift_congr ih)

/-- The same convolution can be expanded in its second coefficient list. -/
theorem polyMul_cons_right (f : List R) (b : R) (g : List R) :
    CoeffEq (polyMul f (b::g)) (polyAdd (polyScale b f) (0::polyMul f g)) := by
  induction f with
  | nil => intro n; cases n <;> simp [polyMul, polyScale, polyAdd, coefficient]
  | cons a f ih =>
    intro n
    cases n with
    | zero => simp [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]; grind
    | succ n =>
      have h := ih n
      simp only [coefficient_polyAdd, coefficient_polyScale] at h
      simp only [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]
      rw [h]
      grind

theorem polyMul_comm (f g : List R) : CoeffEq (polyMul f g) (polyMul g f) := by
  induction f with
  | nil => exact coeffEq_symm (polyMul_zero_right g)
  | cons a f ih =>
    exact coeffEq_trans (polyAdd_congr (coeffEq_refl _) (shift_congr ih))
      (coeffEq_symm (polyMul_cons_right g a f))

theorem polyMul_congr_left {f f' : List R} (h : CoeffEq f f') (g : List R) :
    CoeffEq (polyMul f g) (polyMul f' g) :=
  coeffEq_trans (polyMul_comm f g)
    (coeffEq_trans (polyMul_congr_right g h) (polyMul_comm g f'))

theorem polyMul_congr {f f' g g' : List R}
    (hf : CoeffEq f f') (hg : CoeffEq g g') :
    CoeffEq (polyMul f g) (polyMul f' g') :=
  coeffEq_trans (polyMul_congr_left hf g) (polyMul_congr_right f' hg)

theorem polyMul_add_right (f g h : List R) :
    CoeffEq (polyMul f (polyAdd g h)) (polyAdd (polyMul f g) (polyMul f h)) := by
  induction f with
  | nil => exact coeffEq_refl []
  | cons a f ih =>
    intro n
    cases n with
    | zero =>
      simp only [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]
      grind
    | succ n =>
      have hi := ih n
      simp only [coefficient_polyAdd] at hi
      simp only [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]
      rw [hi]
      grind

theorem polyMul_add_left (f g h : List R) :
    CoeffEq (polyMul (polyAdd f g) h) (polyAdd (polyMul f h) (polyMul g h)) :=
  coeffEq_trans (polyMul_comm _ _)
    (coeffEq_trans (polyMul_add_right _ _ _)
      (polyAdd_congr (polyMul_comm _ _) (polyMul_comm _ _)))

theorem polyMul_scale_right (f : List R) (c : R) (g : List R) :
    CoeffEq (polyMul f (polyScale c g)) (polyScale c (polyMul f g)) := by
  induction f with
  | nil => exact coeffEq_refl []
  | cons a f ih =>
    intro n
    cases n with
    | zero =>
      simp only [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]
      grind
    | succ n =>
      have hi := ih n
      simp only [coefficient_polyScale] at hi
      simp only [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]
      rw [hi]
      grind

theorem polyMul_scale_left (c : R) (f g : List R) :
    CoeffEq (polyMul (polyScale c f) g) (polyScale c (polyMul f g)) :=
  coeffEq_trans (polyMul_comm _ _)
    (coeffEq_trans (polyMul_scale_right _ _ _)
      (polyScale_congr c (polyMul_comm _ _)))

theorem polyMul_shift_left (f g : List R) :
    CoeffEq (polyMul (0::f) g) (0::polyMul f g) := by
  intro n
  simp only [polyMul, coefficient_polyAdd, coefficient_polyScale]
  grind

theorem polyMul_assoc (f g h : List R) :
    CoeffEq (polyMul (polyMul f g) h) (polyMul f (polyMul g h)) := by
  induction f with
  | nil => exact coeffEq_refl []
  | cons a f ih =>
    exact coeffEq_trans (polyMul_add_left (polyScale a g) (0::polyMul f g) h)
      (polyAdd_congr (polyMul_scale_left a g h)
        (coeffEq_trans (polyMul_shift_left (polyMul f g) h) (shift_congr ih)))

theorem timesLinear_as_add (r : R) (f : List R) :
    CoeffEq (timesLinear r f) (polyAdd (polyScale (-r) f) (0::f)) := by
  intro n
  cases n with
  | zero =>
    simp only [coefficient_timesLinear_zero, coefficient_polyAdd,
      coefficient_polyScale, coefficient]
    grind
  | succ n =>
    simp only [coefficient_timesLinear_succ, coefficient_polyAdd,
      coefficient_polyScale, coefficient]
    grind

theorem polyMul_timesLinear_left (r : R) (f g : List R) :
    CoeffEq (polyMul (timesLinear r f) g) (timesLinear r (polyMul f g)) :=
  coeffEq_trans (polyMul_congr_left (timesLinear_as_add r f) g)
    (coeffEq_trans (polyMul_add_left _ _ _)
      (coeffEq_trans
        (polyAdd_congr (polyMul_scale_left (-r) f g) (polyMul_shift_left f g))
        (coeffEq_symm (timesLinear_as_add r (polyMul f g)))))

/-- The explicitly generated monic ideal is closed under actual multiplication. -/
theorem polyMul_monicMultiple_left (roots f g : List R) :
    CoeffEq (polyMul (monicMultiple roots f) g)
      (monicMultiple roots (polyMul f g)) := by
  induction roots with
  | nil => exact coeffEq_refl _
  | cons r roots ih =>
    exact coeffEq_trans (polyMul_timesLinear_left r (monicMultiple roots f) g)
      (timesLinear_congr r ih)

/-- Reducing the first factor before multiplication preserves the actual
canonical remainder. No hypothesis that multiplication respects a quotient
has been assumed: its monic multiple is constructed in the proof. -/
theorem monicRemainder_mul_reduce_left (roots f g : List R) :
    monicRemainder roots (polyMul f g) =
      monicRemainder roots (polyMul (monicRemainder roots f) g) := by
  have hd : CoeffEq (polyMul f g)
      (polyAdd (polyMul (monicRemainder roots f) g)
        (monicMultiple roots (polyMul (monicQuotient roots f) g))) := by
    have hp := polyMul_congr_left (monic_division_identity roots f) g
    have ha := polyMul_add_left
      (monicMultiple roots (monicQuotient roots f)) (monicRemainder roots f) g
    have hm := polyMul_monicMultiple_left roots (monicQuotient roots f) g
    intro n
    have h := (hp n).trans (ha n)
    simp only [coefficient_polyAdd] at h ⊢
    rw [hm n] at h
    grind
  apply list_eq_of_coeffEq_of_length_eq
  · exact monicRemainder_quotient_invariant roots _ _ _ hd
  · simp only [monicRemainder_length]

theorem monicRemainder_mul_reduce_right (roots f g : List R) :
    monicRemainder roots (polyMul f g) =
      monicRemainder roots (polyMul f (monicRemainder roots g)) := by
  rw [monicRemainder_congr roots (polyMul_comm f g),
    monicRemainder_mul_reduce_left,
    monicRemainder_congr roots (polyMul_comm (monicRemainder roots g) f)]

theorem monicRemainder_mul_reduce_both (roots f g : List R) :
    monicRemainder roots (polyMul f g) =
      monicRemainder roots
        (polyMul (monicRemainder roots f) (monicRemainder roots g)) := by
  rw [monicRemainder_mul_reduce_left roots f g,
    monicRemainder_mul_reduce_right roots (monicRemainder roots f) g]

theorem newtonFunctional_mul_reduce_both (roots f g : List R) :
    newtonFunctional roots (polyMul f g) =
      newtonFunctional roots
        (polyMul (monicRemainder roots f) (monicRemainder roots g)) := by
  rw [← top_coefficient_is_newton, ← top_coefficient_is_newton,
    monicRemainder_mul_reduce_both]

/-- Actual multiplication followed by the constructed monic remainder. -/
def quotientProduct (roots f g : List R) : List R :=
  monicRemainder roots (polyMul f g)

theorem quotientProduct_length (roots f g : List R) :
    (quotientProduct roots f g).length = roots.length :=
  monicRemainder_length roots _

theorem quotientProduct_congr (roots : List R) {f f' g g' : List R}
    (hf : CoeffEq f f') (hg : CoeffEq g g') :
    quotientProduct roots f g = quotientProduct roots f' g' :=
  monicRemainder_congr roots (polyMul_congr hf hg)

theorem quotientProduct_comm (roots f g : List R) :
    quotientProduct roots f g = quotientProduct roots g f :=
  monicRemainder_congr roots (polyMul_comm f g)

/-- Canonical multiplication is associative even for repeated roots. -/
theorem quotientProduct_assoc (roots f g h : List R) :
    quotientProduct roots (quotientProduct roots f g) h =
      quotientProduct roots f (quotientProduct roots g h) := by
  simp only [quotientProduct]
  rw [← monicRemainder_mul_reduce_left, ← monicRemainder_mul_reduce_right]
  exact monicRemainder_congr roots (polyMul_assoc f g h)

theorem polyMul_one_left (f : List R) : CoeffEq (polyMul [1] f) f := by
  intro n
  cases n with
  | zero =>
    simp only [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]
    grind
  | succ n =>
    simp only [polyMul, coefficient_polyAdd, coefficient_polyScale, coefficient]
    grind

theorem quotientProduct_one_left (roots f : List R) :
    quotientProduct roots [1] f = monicRemainder roots f :=
  monicRemainder_congr roots (polyMul_one_left f)

theorem quotientProduct_one_right (roots f : List R) :
    quotientProduct roots f [1] = monicRemainder roots f := by
  rw [quotientProduct_comm, quotientProduct_one_left]

/-- Ordinary multiplication of a finite list of polynomial factors. -/
def polyProduct : List (List R) → List R
  | [] => [1]
  | f::fs => polyMul f (polyProduct fs)

/-- The same product reduced after every operation, with the same modulus. -/
def canonicalProduct (roots : List R) : List (List R) → List R
  | [] => monicRemainder roots [1]
  | f::fs => quotientProduct roots f (canonicalProduct roots fs)

theorem monicRemainder_product (roots : List R) (fs : List (List R)) :
    monicRemainder roots (polyProduct fs) = canonicalProduct roots fs := by
  induction fs with
  | nil => rfl
  | cons f fs ih =>
    simp only [polyProduct, canonicalProduct, quotientProduct]
    rw [monicRemainder_mul_reduce_right, ih]

/-- The full Newton functional can be evaluated after reducing at each
intermediate multiplication, with no bound on the initial product degree. -/
theorem newtonFunctional_product (roots : List R) (fs : List (List R)) :
    newtonFunctional roots (polyProduct fs) =
      coefficient (canonicalProduct roots fs) (roots.length-1) := by
  rw [← top_coefficient_is_newton, monicRemainder_product]

@[simp]
theorem horner_polyMul (f g : List R) (z : R) :
    horner (polyMul f g) z = horner f z * horner g z := by
  induction f with
  | nil => simp only [polyMul, horner]; grind
  | cons a f ih =>
    simp only [polyMul, horner_polyAdd, horner_polyScale, horner]
    rw [ih]
    grind

theorem formalDerivativeValue_polyAdd (f g : List R) (z : R) :
    formalDerivativeValue (polyAdd f g) z =
      formalDerivativeValue f z + formalDerivativeValue g z := by
  induction f generalizing g with
  | nil => simp only [polyAdd, formalDerivativeValue]; grind
  | cons a f ih =>
    cases g with
    | nil => simp only [polyAdd, formalDerivativeValue]; grind
    | cons b g =>
      simp only [polyAdd, formalDerivativeValue, horner_polyAdd]
      rw [ih]
      grind

theorem formalDerivativeValue_polyScale (c : R) (f : List R) (z : R) :
    formalDerivativeValue (polyScale c f) z = c * formalDerivativeValue f z := by
  induction f with
  | nil => simp only [polyScale, formalDerivativeValue]; grind
  | cons a f ih =>
    simp only [polyScale, formalDerivativeValue, horner_polyScale]
    rw [ih]
    grind

/-- The first normal of the constructed product satisfies the algebraic
Leibniz rule. No analytic derivative or equality of sampled values is used. -/
theorem formalDerivativeValue_polyMul (f g : List R) (z : R) :
    formalDerivativeValue (polyMul f g) z =
      formalDerivativeValue f z * horner g z +
        horner f z * formalDerivativeValue g z := by
  induction f with
  | nil => simp only [polyMul, formalDerivativeValue, horner]; grind
  | cons a f ih =>
    simp only [polyMul, formalDerivativeValue_polyAdd,
      formalDerivativeValue_polyScale, formalDerivativeValue, horner, horner_polyMul]
    rw [ih]
    grind

/-- The exact product remainder at a double spectral node. Both first-normal
contributions remain, including when either factor vanishes at that node. -/
theorem double_root_product_remainder (r : R) (f g : List R) :
    monicRemainder [r,r] (polyMul f g) =
      [horner f r * horner g r - r *
        (formalDerivativeValue f r * horner g r +
          horner f r * formalDerivativeValue g r),
       formalDerivativeValue f r * horner g r +
          horner f r * formalDerivativeValue g r] := by
  rw [double_root_remainder, horner_polyMul, formalDerivativeValue_polyMul]

theorem newtonFunctional_double_root_product (r : R) (f g : List R) :
    newtonFunctional [r,r] (polyMul f g) =
      formalDerivativeValue f r * horner g r +
        horner f r * formalDerivativeValue g r := by
  rw [← top_coefficient_is_newton, double_root_product_remainder]
  rfl

theorem formalDerivativeValue_addConstant (a : R) (f : List R) (z : R) :
    formalDerivativeValue (addConstant a f) z = formalDerivativeValue f z := by
  cases f <;> simp only [addConstant, formalDerivativeValue, horner] <;> grind

theorem formalDerivativeValue_timesLinear (r : R) (f : List R) (z : R) :
    formalDerivativeValue (timesLinear r f) z =
      horner f z + (z-r)*formalDerivativeValue f z := by
  induction f with
  | nil => simp only [timesLinear, formalDerivativeValue, horner]; grind
  | cons a f ih =>
    simp only [timesLinear, formalDerivativeValue, horner_addConstant,
      formalDerivativeValue_addConstant, horner_timesLinear, horner]
    rw [ih]
    grind

/-- The constructed remainder retains the value at its first listed root. -/
theorem monicRemainder_head_value (r : R) (roots f : List R) :
    horner (monicRemainder (r::roots) f) r = horner f r := by
  simp only [monicRemainder, horner_addConstant, horner_timesLinear]
  grind

/-- If a node occurs twice, its first normal is retained even when the
modulus has further roots. Root permutation invariance permits these two
occurrences to be placed first without any distinctness assumption. -/
theorem monicRemainder_double_head_derivative (r : R) (roots f : List R) :
    formalDerivativeValue (monicRemainder (r::r::roots) f) r =
      formalDerivativeValue f r := by
  change formalDerivativeValue
    (addConstant (horner f r)
      (timesLinear r (monicRemainder (r::roots) (synthetic r f)))) r = _
  rw [formalDerivativeValue_addConstant, formalDerivativeValue_timesLinear,
    monicRemainder_head_value, synthetic_horner, diagonal_divided_difference]
  grind

theorem quotientProduct_double_head_value (r : R) (roots f g : List R) :
    horner (quotientProduct (r::r::roots) f g) r = horner f r * horner g r := by
  simp only [quotientProduct, monicRemainder_head_value, horner_polyMul]

theorem quotientProduct_double_head_derivative (r : R) (roots f g : List R) :
    formalDerivativeValue (quotientProduct (r::r::roots) f g) r =
      formalDerivativeValue f r * horner g r +
        horner f r * formalDerivativeValue g r := by
  simp only [quotientProduct, monicRemainder_double_head_derivative,
    formalDerivativeValue_polyMul]

end VolumeLogic
