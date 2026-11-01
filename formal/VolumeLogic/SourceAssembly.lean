import Std

namespace VolumeLogic
open Lean.Grind

/-!
Finite assembly of the original sector decomposition. The index list is
the entire list of retained noncentral sectors, with its original
multiplicities. Nothing in these statements replaces that list by one
selected term. The source identity, local estimates and the bound for
the actual filling functional are hypotheses; their analytic and
geometric proofs are not supplied by this module.
-/

universe u v w z

/-- A sum retaining the specified source indices and their multiplicities. -/
def sectorSum {I : Type u} {A : Type v} [CommRing A]
    (indices : List I) (term : I → A) : A :=
  match indices with
  | [] => 0
  | i :: rest => term i + sectorSum rest term

theorem filling_sector_sum {I : Type u} {A : Type v} {B : Type w}
    [CommRing A] [CommRing B] (indices : List I) (term : I → A)
    (fill : A → B) (zero : fill 0 = 0)
    (add : ∀ x y, fill (x + y) = fill x + fill y) :
    fill (sectorSum indices term) = sectorSum indices (fun i => fill (term i)) := by
  induction indices with
  | nil => exact zero
  | cons i rest ih =>
    simp only [sectorSum, add, ih]

/-- The exact whole remainder after filling, obtained from the full source
identity by additivity, before any absolute value is taken. -/
theorem filled_remainder_identity {I : Type u} {A : Type v} {B : Type w}
    [CommRing A] [CommRing B] (indices : List I) (term : I → A)
    (full central : A) (fill : A → B)
    (source : full = central + sectorSum indices term)
    (zero : fill 0 = 0)
    (add : ∀ x y, fill (x + y) = fill x + fill y) :
    fill full - fill central = sectorSum indices (fun i => fill (term i)) := by
  rw [source, add, filling_sector_sum indices term fill zero add]
  grind

section Bounds

variable {I : Type u} {A : Type v} {B : Type w} {R : Type z}
  [CommRing A] [CommRing B] [CommRing R] [LE R] [LT R]
  [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]

theorem magnitude_sector_sum (indices : List I) (term : I → B)
    (magnitude : B → R) (zero : magnitude 0 = 0)
    (triangle : ∀ x y, magnitude (x + y) ≤ magnitude x + magnitude y) :
    magnitude (sectorSum indices term) ≤
      sectorSum indices (fun i => magnitude (term i)) := by
  induction indices with
  | nil => simp only [sectorSum, zero]; exact Std.le_refl _
  | cons i rest ih =>
    have h := triangle (term i) (sectorSum rest term)
    simp only [sectorSum]
    grind

theorem sector_sum_mono (indices : List I) (a b : I → R)
    (bounds : ∀ i ∈ indices, a i ≤ b i) :
    sectorSum indices a ≤ sectorSum indices b := by
  induction indices with
  | nil => exact Std.le_refl _
  | cons i rest ih =>
    have hi := bounds i (by simp)
    have ht : ∀ j ∈ rest, a j ≤ b j := by
      intro j hj
      exact bounds j (by simp [hj])
    have h := ih ht
    simp only [sectorSum]
    grind

omit [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R] in
theorem sector_sum_common_factor (indices : List I) (weight : I → R) (c e : R) :
    sectorSum indices (fun i => c * (weight i * e)) =
      c * sectorSum indices weight * e := by
  induction indices with
  | nil => simp only [sectorSum]; grind
  | cons i rest ih => simp only [sectorSum, ih]; grind

/-- A uniform bound on every original sector, followed by the actual
operator-norm bound, controls the entire filled remainder. The common
factor e may be an exponential majorant and the weights may contain the
level-dependent polynomial prefactors. In the application, admissible
means degree at most N-1 in every spectral variable. The operator bound
is not assumed for arbitrary higher-degree polynomials. The rings here
are the scalar source polynomials and scalar filled values; there is no
commutation assertion for physical coupons at different crossings. -/
theorem finite_sector_filling_bound
    (indices : List I) (term : I → A) (full central : A)
    (fill : A → B) (sourceSize : A → R) (magnitude : B → R)
    (admissible : A → Prop)
    (weight : I → R) (operatorCost envelope : R)
    (source : full = central + sectorSum indices term)
    (fill_zero : fill 0 = 0)
    (fill_add : ∀ x y, fill (x + y) = fill x + fill y)
    (magnitude_zero : magnitude 0 = 0)
    (triangle : ∀ x y, magnitude (x + y) ≤ magnitude x + magnitude y)
    (cost_nonnegative : 0 ≤ operatorCost)
    (sector_admissible : ∀ i ∈ indices, admissible (term i))
    (operator_bound : ∀ x, admissible x →
      magnitude (fill x) ≤ operatorCost * sourceSize x)
    (sector_bound : ∀ i ∈ indices, sourceSize (term i) ≤ weight i * envelope) :
    magnitude (fill full - fill central) ≤
      operatorCost * sectorSum indices weight * envelope := by
  rw [filled_remainder_identity indices term full central fill source fill_zero fill_add]
  have hs := magnitude_sector_sum indices (fun i => fill (term i))
    magnitude magnitude_zero triangle
  have hb : ∀ i ∈ indices,
      magnitude (fill (term i)) ≤ operatorCost * (weight i * envelope) := by
    intro i hi
    have ho := operator_bound (term i) (sector_admissible i hi)
    have he := sector_bound i hi
    have hd : 0 ≤ weight i * envelope - sourceSize (term i) := by grind
    have hm := OrderedRing.mul_nonneg cost_nonnegative hd
    grind
  have hm := sector_sum_mono indices (fun i => magnitude (fill (term i)))
    (fun i => operatorCost * (weight i * envelope)) hb
  rw [sector_sum_common_factor] at hm
  grind

end Bounds

/-- The maximum is constructed from the full finite index list, rather
than an asserted common asymptotic threshold. -/
def sectorThreshold {I : Type u} (indices : List I) (threshold : I → Nat) : Nat :=
  match indices with
  | [] => 0
  | i :: rest => max (threshold i) (sectorThreshold rest threshold)

theorem sector_threshold_dominates {I : Type u} (indices : List I)
    (threshold : I → Nat) :
    ∀ i ∈ indices, threshold i ≤ sectorThreshold indices threshold := by
  induction indices with
  | nil => simp
  | cons i rest ih =>
    intro j hj
    simp only [List.mem_cons] at hj
    rcases hj with h | h
    · subst j
      simp only [sectorThreshold]
      exact Nat.le_max_left _ _
    · have ht := ih j h
      have hm := Nat.le_max_right (threshold i) (sectorThreshold rest threshold)
      simp only [sectorThreshold]
      omega

/-- Independent per-sector eventual estimates become simultaneous after
one explicit finite maximum. The level predicate can retain all levels,
one parity, or any other stated subsequence; it is never discarded. -/
theorem simultaneous_sector_threshold {I : Type u} (indices : List I)
    (threshold : I → Nat) (scope : Nat → Prop) (estimate : I → Nat → Prop)
    (individual : ∀ i ∈ indices, ∀ N, threshold i ≤ N → scope N → estimate i N) :
    ∀ N, sectorThreshold indices threshold ≤ N → scope N →
      ∀ i ∈ indices, estimate i N := by
  intro N hN hscope i hi
  have ht := sector_threshold_dominates indices threshold i hi
  exact individual i hi N (by omega) hscope

end VolumeLogic
