import VolumeLogic.RateComparison

namespace VolumeLogic
open Lean.Grind
universe u

/-- A set of integer levels, retained in every eventual assertion. -/
abbrev LevelScope := Nat → Prop

def physicalLevels : LevelScope := fun N => 2 ≤ N
def evenLevels : LevelScope := fun N => 2 ≤ N ∧ N % 2 = 0
def oddLevels : LevelScope := fun N => 2 ≤ N ∧ N % 2 = 1

/-- The threshold may depend on all previously fixed data. -/
def EventuallyOn (s : LevelScope) (P : Nat → Prop) : Prop :=
  ∃ N₀, ∀ N, N₀ ≤ N → s N → P N

theorem eventuallyOn_of_forall {s : LevelScope} {P : Nat → Prop}
    (h : ∀ N, s N → P N) : EventuallyOn s P :=
  ⟨0, fun N _ hs => h N hs⟩

theorem eventuallyOn_mono {s : LevelScope} {P Q : Nat → Prop}
    (h : EventuallyOn s P) (imp : ∀ N, s N → P N → Q N) :
    EventuallyOn s Q := by
  obtain ⟨N₀, h⟩ := h
  exact ⟨N₀, fun N hn hs => imp N hs (h N hn hs)⟩

theorem eventuallyOn_and {s : LevelScope} {P Q : Nat → Prop}
    (hp : EventuallyOn s P) (hq : EventuallyOn s Q) :
    EventuallyOn s (fun N => P N ∧ Q N) := by
  obtain ⟨a, ha⟩ := hp
  obtain ⟨b, hb⟩ := hq
  exact ⟨a+b, fun N hn hs => ⟨ha N (by omega) hs, hb N (by omega) hs⟩⟩

theorem eventuallyOn_restrict {s t : LevelScope} {P : Nat → Prop}
    (h : EventuallyOn s P) (sub : ∀ N, t N → s N) : EventuallyOn t P := by
  obtain ⟨a, ha⟩ := h
  exact ⟨a, fun N hn ht => ha N hn (sub N ht)⟩

theorem eventuallyOn_finite {I : Type u} {s : LevelScope}
    (indices : List I) (P : I → Nat → Prop)
    (h : ∀ i ∈ indices, EventuallyOn s (P i)) :
    EventuallyOn s (fun N => ∀ i ∈ indices, P i N) := by
  induction indices with
  | nil => exact eventuallyOn_of_forall (by simp)
  | cons i rest ih =>
    have hi := h i (by simp)
    have hr := ih (fun j hj => h j (by simp [hj]))
    exact eventuallyOn_mono (eventuallyOn_and hi hr) (by simp_all)

/-- Both parity proofs are needed to recover an all-level assertion. -/
theorem eventuallyOn_both_parities {P : Nat → Prop}
    (he : EventuallyOn evenLevels P) (ho : EventuallyOn oddLevels P) :
    EventuallyOn physicalLevels P := by
  obtain ⟨a, ha⟩ := he
  obtain ⟨b, hb⟩ := ho
  refine ⟨a+b, fun N hn hs => ?_⟩
  by_cases h : N % 2 = 0
  · exact ha N (by omega) ⟨hs, h⟩
  · exact hb N (by omega) ⟨hs, by omega⟩

/-- Every signed power is long; signs are not tied to one another. -/
def LongEnough {I : Type u} (T : Nat) (p : I → Int) : Prop :=
  ∀ i, T < (p i).natAbs

theorem longEnough_mono {I : Type u} {a b : Nat} {p : I → Int}
    (h : LongEnough b p) (hab : a ≤ b) : LongEnough a p := by
  intro i
  have := h i
  omega

/-- Combine finitely many thresholds before fixing the power tuple. Nothing
here permits the powers or the diagram to vary with the asymptotic level. -/
theorem fixed_filling_finite_threshold {I J : Type u} (indices : List J)
    (P : J → (I → Int) → Prop)
    (h : ∀ j ∈ indices, ∃ T, ∀ p, LongEnough T p → P j p) :
    ∃ T, ∀ p, LongEnough T p → ∀ j ∈ indices, P j p := by
  induction indices with
  | nil => exact ⟨0, by simp⟩
  | cons j rest ih =>
    obtain ⟨a, ha⟩ := h j (by simp)
    obtain ⟨b, hb⟩ := ih (fun k hk => h k (by simp [hk]))
    refine ⟨a+b, fun p hp k hk => ?_⟩
    have hpa := longEnough_mono hp (show a ≤ a+b by omega)
    have hpb := longEnough_mono hp (show b ≤ a+b by omega)
    simp only [List.mem_cons] at hk
    rcases hk with hkj | hkr
    · exact hkj ▸ ha p hpa
    · exact hb p hpb k hkr

section Rates
variable {R : Type u} [Field R] [LE R] [LT R]
  [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-- Epsilon definition, with the level scope and sequence explicit. -/
def RateLimit (s : LevelScope) (f : Nat → R) (a : R) : Prop :=
  ∀ ε, 0 < ε → EventuallyOn s (fun N => a-ε < f N ∧ f N < a+ε)

theorem positive_quarter (ε : R) (h : 0 < ε) :
    0 < ε/4 ∧ 4*(ε/4) = ε := by
  have hn : (4 : R) ≠ 0 := by grind
  have he := Field.div_mul_cancel (x := ε) hn
  constructor <;> grind

theorem rateLimit_const (s : LevelScope) (a : R) :
    RateLimit s (fun _ => a) a := by
  intro ε hε
  exact eventuallyOn_of_forall (by intros; constructor <;> grind)

theorem rateLimit_congr {s : LevelScope} {f g : Nat → R} {a : R}
    (hf : RateLimit s f a) (eq : EventuallyOn s (fun N => f N = g N)) :
    RateLimit s g a := by
  intro ε hε
  exact eventuallyOn_mono (eventuallyOn_and (hf ε hε) eq) (by intros; grind)

theorem rateLimit_add {s : LevelScope} {f g : Nat → R} {a b : R}
    (hf : RateLimit s f a) (hg : RateLimit s g b) :
    RateLimit s (fun N => f N+g N) (a+b) := by
  intro ε hε
  have hq := positive_quarter ε hε
  apply eventuallyOn_mono (eventuallyOn_and (hf (ε/4) hq.1) (hg (ε/4) hq.1))
  intro N _ h
  constructor <;> grind

omit [LE R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R] in
theorem rateLimit_restrict {s t : LevelScope} {f : Nat → R} {a : R}
    (h : RateLimit s f a) (sub : ∀ N, t N → s N) : RateLimit t f a := by
  intro ε hε
  exact eventuallyOn_restrict (h ε hε) sub

omit [LE R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R] in
theorem rateLimit_both_parities {f : Nat → R} {a : R}
    (he : RateLimit evenLevels f a) (ho : RateLimit oddLevels f a) :
    RateLimit physicalLevels f a := by
  intro ε hε
  exact eventuallyOn_both_parities (he ε hε) (ho ε hε)

/-- A shrinking additive corridor preserves the rate. -/
theorem rateLimit_squeeze_error {s : LevelScope} {f g e : Nat → R} {a : R}
    (hf : RateLimit s f a) (he : RateLimit s e 0)
    (bounds : EventuallyOn s (fun N => f N-e N ≤ g N ∧ g N ≤ f N+e N)) :
    RateLimit s g a := by
  intro ε hε
  have hq := positive_quarter ε hε
  apply eventuallyOn_mono
    (eventuallyOn_and (eventuallyOn_and (hf (ε/4) hq.1) (he (ε/4) hq.1)) bounds)
  intro N _ h
  constructor <;> grind

theorem rateLimit_scale_nonnegative {s : LevelScope} {f : Nat → R} {a : R}
    (c : R) (hc : 0 ≤ c) (hf : RateLimit s f a) :
    RateLimit s (fun N => c*f N) (c*a) := by
  intro ε hε
  have hd : 0 < 4*(c+1) := by grind
  have hdn : 4*(c+1) ≠ 0 := by grind
  have he := Field.div_mul_cancel (x := ε) hdn
  have hδ : 0 < ε/(4*(c+1)) := by
    by_cases hp : 0 < ε/(4*(c+1))
    · exact hp
    · have hn : 0 ≤ -(ε/(4*(c+1))) := by grind
      have hm := OrderedRing.mul_nonneg hn (show 0 ≤ 4*(c+1) by grind)
      grind
  apply eventuallyOn_mono (hf (ε/(4*(c+1))) hδ)
  intro N _ h
  have hl := OrderedRing.mul_nonneg hc
    (show 0 ≤ f N-(a-ε/(4*(c+1))) by grind)
  have hu := OrderedRing.mul_nonneg hc
    (show 0 ≤ a+ε/(4*(c+1))-f N by grind)
  constructor <;> grind

end Rates
end VolumeLogic
