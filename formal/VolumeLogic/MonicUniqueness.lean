import VolumeLogic.MonicLinearity

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-- Coefficient equality determines a list once its length is fixed. -/
theorem list_eq_of_coeffEq_of_length_eq {f g : List R}
    (h : CoeffEq f g) (hl : f.length = g.length) : f = g := by
  induction f generalizing g with
  | nil => cases g <;> simp_all
  | cons a f ih =>
    cases g with
    | nil => simp at hl
    | cons b g =>
      have hab : a = b := h 0
      have hfg : CoeffEq f g := fun n => h (n+1)
      have hlen : f.length = g.length := by simpa using hl
      rw [hab, ih hfg hlen]

/-- Truncation leaves every coefficient below its cutoff unchanged. -/
theorem coefficient_take_of_lt (f : List R) (k n : Nat) (h : n < k) :
    coefficient (f.take k) n = coefficient f n := by
  induction k generalizing f n with
  | zero => omega
  | succ k ih =>
    cases f with
    | nil => simp [coefficient]
    | cons a f =>
      cases n with
      | zero => rfl
      | succ n => exact ih f n (by omega)

/-- A degree hypothesis is coefficientwise; it imposes no list-padding convention. -/
theorem coeffEq_take_of_degree_lt (f : List R) (k : Nat)
    (hdegree : ∀ n, k ≤ n → coefficient f n = 0) : CoeffEq (f.take k) f := by
  intro n
  by_cases h : n < k
  · exact coefficient_take_of_lt f k n h
  · rw [hdegree n (by omega)]
    apply coefficient_eq_zero_of_length_le
    have ht := List.length_take_le k f
    omega

theorem monicRemainder_of_coeff_degree_lt (roots f : List R)
    (hdegree : ∀ n, roots.length ≤ n → coefficient f n = 0) :
    CoeffEq (monicRemainder roots f) f := by
  have ht := coeffEq_take_of_degree_lt f roots.length hdegree
  rw [← monicRemainder_congr roots ht]
  exact coeffEq_trans
    (monicRemainder_of_degree_lt roots (f.take roots.length)
      (List.length_take_le roots.length f)) ht

/-- A small-degree representative of a monic congruence class is its remainder. -/
theorem monicRemainder_unique (roots f q r : List R)
    (hdegree : r.length ≤ roots.length)
    (hdivision : CoeffEq f (polyAdd r (monicMultiple roots q))) :
    CoeffEq (monicRemainder roots f) r := by
  exact coeffEq_trans
    (monicRemainder_quotient_invariant roots f r q hdivision)
    (monicRemainder_of_degree_lt roots r hdegree)

/-- The same uniqueness theorem permits arbitrary trailing zero coefficients. -/
theorem monicRemainder_unique_padded (roots f q r : List R)
    (hdegree : ∀ n, roots.length ≤ n → coefficient r n = 0)
    (hdivision : CoeffEq f (polyAdd r (monicMultiple roots q))) :
    CoeffEq (monicRemainder roots f) r := by
  exact coeffEq_trans
    (monicRemainder_quotient_invariant roots f r q hdivision)
    (monicRemainder_of_coeff_degree_lt roots r hdegree)

/-- Two reconstructions of the same input have the same small-degree remainder. -/
theorem monic_remainder_unique_between (roots f q₁ q₂ r₁ r₂ : List R)
    (hd₁ : r₁.length ≤ roots.length) (hd₂ : r₂.length ≤ roots.length)
    (h₁ : CoeffEq f (polyAdd r₁ (monicMultiple roots q₁)))
    (h₂ : CoeffEq f (polyAdd r₂ (monicMultiple roots q₂))) :
    CoeffEq r₁ r₂ := by
  exact coeffEq_trans (coeffEq_symm (monicRemainder_unique roots f q₁ r₁ hd₁ h₁))
    (monicRemainder_unique roots f q₂ r₂ hd₂ h₂)

/-- The coefficient functional can be computed from any such reconstruction. -/
theorem newtonFunctional_from_remainder (roots f q r : List R)
    (hdegree : r.length ≤ roots.length)
    (hdivision : CoeffEq f (polyAdd r (monicMultiple roots q))) :
    newtonFunctional roots f = coefficient r (roots.length-1) := by
  rw [← top_coefficient_is_newton]
  exact monicRemainder_unique roots f q r hdegree hdivision (roots.length-1)

theorem monicRemainder_idempotent (roots f : List R) :
    monicRemainder roots (monicRemainder roots f) = monicRemainder roots f := by
  apply list_eq_of_coeffEq_of_length_eq
  · exact monicRemainder_of_degree_lt roots (monicRemainder roots f)
      (by simp)
  · simp only [monicRemainder_length]

theorem monicMultiple_congr (roots : List R) {f g : List R} (h : CoeffEq f g) :
    CoeffEq (monicMultiple roots f) (monicMultiple roots g) := by
  induction roots with
  | nil => exact h
  | cons r roots ih => exact timesLinear_congr r ih

/-- Commuting two linear factors is a formal coefficient identity over a ring;
it does not require distinct roots or division by their difference. -/
theorem timesLinear_commute (r s : R) (f : List R) :
    CoeffEq (timesLinear r (timesLinear s f)) (timesLinear s (timesLinear r f)) := by
  intro n
  cases n with
  | zero => simp only [coefficient_timesLinear_zero]; grind
  | succ n =>
    cases n with
    | zero => simp only [coefficient_timesLinear_succ, coefficient_timesLinear_zero]; grind
    | succ n => simp only [coefficient_timesLinear_succ]; grind

/-- The actual modulus multiplication depends on the multiset of roots. -/
theorem monicMultiple_permutation {roots other : List R} (h : roots.Perm other)
    (f : List R) : CoeffEq (monicMultiple roots f) (monicMultiple other f) := by
  induction h with
  | nil => exact coeffEq_refl f
  | cons r h ih => exact timesLinear_congr r ih
  | swap r s roots => exact timesLinear_commute s r (monicMultiple roots f)
  | trans h₁ h₂ ih₁ ih₂ => exact coeffEq_trans ih₁ ih₂

/-- Newton's ordered construction gives the same monomial remainder in every
order, including all permutations of a list with repeated spectral nodes. -/
theorem monicRemainder_permutation {roots other : List R} (h : roots.Perm other)
    (f : List R) : monicRemainder roots f = monicRemainder other f := by
  have hlen := h.length_eq
  have hd : CoeffEq f (polyAdd (monicRemainder other f)
      (monicMultiple roots (monicQuotient other f))) := by
    intro n
    have hd := monic_division_identity other f n
    have hm := monicMultiple_permutation h (monicQuotient other f) n
    simp only [coefficient_polyAdd] at hd ⊢
    rw [hm]
    grind
  apply list_eq_of_coeffEq_of_length_eq
  · exact monicRemainder_unique roots f (monicQuotient other f)
      (monicRemainder other f) (by simp only [monicRemainder_length]; omega) hd
  · simp only [monicRemainder_length]; exact h.length_eq

/-- Consequently the confluent divided-difference functional is symmetric.
Repeated-node derivatives are retained rather than removed by cancellation. -/
theorem newtonFunctional_permutation {roots other : List R} (h : roots.Perm other)
    (f : List R) : newtonFunctional roots f = newtonFunctional other f := by
  rw [← top_coefficient_is_newton, ← top_coefficient_is_newton,
    monicRemainder_permutation h, h.length_eq]

/-- An exact identification criterion for a candidate coefficient functional.
The hypotheses must be established for that candidate on all polynomials;
agreement at sampled nodes or finitely many levels is not a substitute. -/
theorem newtonFunctional_characterization (roots : List R) (F : List R → R)
    (hcongr : ∀ a b, CoeffEq a b → F a = F b)
    (hadd : ∀ a b, F (polyAdd a b) = F a + F b)
    (hkill : ∀ q, F (monicMultiple roots q) = 0)
    (hnorm : ∀ r, r.length ≤ roots.length → F r = coefficient r (roots.length-1))
    (f : List R) : F f = newtonFunctional roots f := by
  rw [hcongr f _ (monic_division_identity roots f), hadd, hkill,
    hnorm (monicRemainder roots f) (by simp), top_coefficient_is_newton]
  grind

end VolumeLogic
