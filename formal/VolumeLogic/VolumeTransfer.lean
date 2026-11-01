import VolumeLogic.LevelLimits
import VolumeLogic.SourceAssembly

namespace VolumeLogic
open Lean.Grind
universe u v w

/-!
The final contribution-to-invariant implication. `Magnitude` and `LogScale`
are explicit elementary analytic interfaces: complex modulus, and log(x)/N
on positive x in the application. They do not assume a volume limit or a
noncancellation theorem. The exact sequence, normalization, remainder,
level scope and fixed geometric action are parameters of the conclusions.
Saddle estimates, the physical invariant identity, and the geometric
action-volume equality are separate written inputs.
-/

variable {C : Type u} {R : Type v} [CommRing C] [Field R] [LE R] [LT R]
  [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]
attribute [local instance] Semiring.natCast Ring.intCast

structure Magnitude (C : Type u) (R : Type v) [CommRing C] [Field R] [LE R] where
  value : C → R
  nonneg : ∀ z, 0 ≤ value z
  eq_zero_iff : ∀ z, value z = 0 ↔ z = 0
  mul : ∀ z w, value (z*w) = value z * value w
  add_le : ∀ z w, value (z+w) ≤ value z + value w
  neg : ∀ z, value (-z) = value z

structure LogScale (R : Type v) [Field R] [LE R] [LT R] where
  value : Nat → R → R
  monotone : ∀ N x y, 0 < x → x ≤ y → value N x ≤ value N y
  product : ∀ N x y, 0 < x → 0 < y → value N (x*y) = value N x + value N y
  constant_limit : ∀ c, 0 < c → RateLimit physicalLevels (fun N => value N c) 0

def magnitudeRate (mag : Magnitude C R) (log : LogScale R) (f : Nat → C) : Nat → R :=
  fun N => log.value N (mag.value (f N))

/-- The arbitrary value of log at zero is never used to claim a finite rate. -/
def HasRate (s : LevelScope) (mag : Magnitude C R) (log : LogScale R)
    (f : Nat → C) (a : R) : Prop :=
  EventuallyOn s (fun N => f N ≠ 0) ∧ RateLimit s (magnitudeRate mag log f) a

/-- This is the epsilon form of a limsup bound, including zero remainders. -/
def HasUpperRate (s : LevelScope) (mag : Magnitude C R) (log : LogScale R)
    (f : Nat → C) (b : R) : Prop :=
  ∀ ε, 0 < ε → EventuallyOn s (fun N => f N = 0 ∨ magnitudeRate mag log f N ≤ b+ε)

theorem magnitude_positive (mag : Magnitude C R) {z : C} (hz : z ≠ 0) :
    0 < mag.value z := by
  have h := mag.nonneg z
  have hne : mag.value z ≠ 0 := fun h0 => hz ((mag.eq_zero_iff z).mp h0)
  grind

omit [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R] in
theorem magnitude_reverse_add (mag : Magnitude C R) (z w : C) :
    mag.value z ≤ mag.value (z+w)+mag.value w := by
  have h := mag.add_le (z+w) (-w)
  have heq : z+w+(-w) = z := by grind
  rw [heq, mag.neg] at h
  exact h

theorem logScale_lt_reflects (log : LogScale R) (N : Nat) {x y : R}
    (hy : 0 < y) (h : log.value N x < log.value N y) : x < y := by
  by_cases hxy : x < y
  · exact hxy
  · have hyx : y ≤ x := by grind
    have hm := log.monotone N y x hy hyx
    grind

theorem hasRate_congr {s : LevelScope} (mag : Magnitude C R) (log : LogScale R)
    {f g : Nat → C} {a : R} (h : HasRate s mag log f a)
    (eq : EventuallyOn s (fun N => f N = g N)) : HasRate s mag log g a := by
  constructor
  · exact eventuallyOn_mono (eventuallyOn_and h.1 eq) (by intros; grind)
  · apply rateLimit_congr h.2
    exact eventuallyOn_mono eq (by intros; simp_all [magnitudeRate])

theorem hasRate_mul {s : LevelScope} (mag : Magnitude C R) (log : LogScale R)
    {f g : Nat → C} {a b : R} (hf : HasRate s mag log f a)
    (hg : HasRate s mag log g b) :
    HasRate s mag log (fun N => f N*g N) (a+b) := by
  have hn := eventuallyOn_and hf.1 hg.1
  constructor
  · apply eventuallyOn_mono hn
    intro N _ h
    have hp := OrderedRing.mul_pos (magnitude_positive mag h.1) (magnitude_positive mag h.2)
    have hm := mag.mul (f N) (g N)
    intro hz
    have h0 := (mag.eq_zero_iff (f N*g N)).mpr hz
    grind
  · apply rateLimit_congr (rateLimit_add hf.2 hg.2)
    apply eventuallyOn_mono hn
    intro N _ h
    have he := log.product N (mag.value (f N)) (mag.value (g N))
      (magnitude_positive mag h.1) (magnitude_positive mag h.2)
    simp only [magnitudeRate, mag.mul]
    exact he.symm

/-- A strict rate gap yields actual modulus domination; it is not supplied
as a hypothesis. The normalization has not yet been discarded. -/
theorem strict_remainder_eventually_small {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N)
    (mag : Magnitude C R) (log : LogScale R)
    {G E : Nat → C} {a b : R}
    (leading : HasRate s mag log G a) (remainder : HasUpperRate s mag log E b)
    (gap : b < a) :
    EventuallyOn s (fun N => 2*mag.value (E N) < mag.value (G N)) := by
  have hδ := positive_quarter (a-b) (show 0 < a-b by grind)
  have two : (0 : R) < 2 := by grind
  have ht := rateLimit_restrict (log.constant_limit 2 two) physical
  apply eventuallyOn_mono (eventuallyOn_and leading.1
    (eventuallyOn_and (leading.2 ((a-b)/4) hδ.1)
      (eventuallyOn_and (remainder ((a-b)/4) hδ.1) (ht ((a-b)/4) hδ.1))))
  intro N _ h
  have hg := magnitude_positive mag h.1
  by_cases he0 : E N = 0
  · have hz := (mag.eq_zero_iff (E N)).mpr he0
    grind
  · have he : magnitudeRate mag log E N ≤ b+(a-b)/4 := by grind
    have hep := magnitude_positive mag he0
    have hprod := log.product N 2 (mag.value (E N)) two hep
    have hrate : log.value N (2*mag.value (E N)) < log.value N (mag.value (G N)) := by
      simp only [magnitudeRate] at he h
      grind
    exact logScale_lt_reflects log N hg hrate

/-- Triangle and reverse triangle give the corridor used in the limit. -/
theorem small_remainder_corridor (mag : Magnitude C R) (log : LogScale R)
    (N : Nat) (G E : C) (hg : G ≠ 0) (small : 2*mag.value E < mag.value G) :
    G+E ≠ 0 ∧
    (log.value N (mag.value G)-log.value N 2 ≤ log.value N (mag.value (G+E)) ∧
     log.value N (mag.value (G+E)) ≤ log.value N (mag.value G)+log.value N 2) := by
  have gp := magnitude_positive mag hg
  have ep := mag.nonneg E
  have rev := magnitude_reverse_add mag G E
  have tri := mag.add_le G E
  have sp : 0 < mag.value (G+E) := by grind
  have snz : G+E ≠ 0 := by
    intro h
    have hz := (mag.eq_zero_iff (G+E)).mpr h
    grind
  have two : (0 : R) < 2 := by grind
  have lower : mag.value G ≤ 2*mag.value (G+E) := by grind
  have upper : mag.value (G+E) ≤ 2*mag.value G := by grind
  have hl := log.monotone N _ _ gp lower
  have hu := log.monotone N _ _ sp upper
  have pl := log.product N 2 (mag.value (G+E)) two sp
  have pu := log.product N 2 (mag.value G) two gp
  exact ⟨snz, by constructor <;> grind⟩

theorem hasRate_add_smaller {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N)
    (mag : Magnitude C R) (log : LogScale R)
    {G E : Nat → C} {a b : R}
    (leading : HasRate s mag log G a) (remainder : HasUpperRate s mag log E b)
    (gap : b < a) : HasRate s mag log (fun N => G N+E N) a := by
  have hs := strict_remainder_eventually_small physical mag log leading remainder gap
  have hc := eventuallyOn_mono (eventuallyOn_and leading.1 hs)
    (fun N _ h => small_remainder_corridor mag log N (G N) (E N) h.1 h.2)
  constructor
  · exact eventuallyOn_mono hc (by intros; grind)
  · have two : (0 : R) < 2 := by grind
    exact rateLimit_squeeze_error leading.2
      (rateLimit_restrict (log.constant_limit 2 two) physical)
      (eventuallyOn_mono hc (by intros; simpa [magnitudeRate] using And.right ‹_›))

/-- The exact invariant, including its original scalar, has the selected
rate. The complete remainder is mandatory; a central-sector bound alone
cannot provide the `remainder` argument. -/
theorem invariant_rate_transfer {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N)
    (mag : Magnitude C R) (log : LogScale R)
    {K u G E : Nat → C} {a b : R}
    (exactSource : EventuallyOn s (fun N => K N = u N*(G N+E N)))
    (normalization : HasRate s mag log u 0)
    (leading : HasRate s mag log G a) (remainder : HasUpperRate s mag log E b)
    (gap : b < a) : HasRate s mag log K a := by
  have hsum := hasRate_add_smaller physical mag log leading remainder gap
  have hprod := hasRate_mul mag log normalization hsum
  have heq := eventuallyOn_mono exactSource (by intros; exact Eq.symm ‹_›)
  have h := hasRate_congr mag log hprod heq
  have hz : (0 : R)+a = a := by grind
  rw [hz] at h
  exact h

/-- The previously proved scalar action-drop lemma supplies the strict
comparison required by the analytic transfer. -/
theorem invariant_rate_of_source_gap {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N)
    (mag : Magnitude C R) (log : LogScale R)
    {K u G E : Nat → C} {a phi gamma drop : R}
    (exactSource : EventuallyOn s (fun N => K N = u N*(G N+E N)))
    (normalization : HasRate s mag log u 0) (leading : HasRate s mag log G a)
    (remainder : HasUpperRate s mag log E (phi-gamma))
    (hgamma : 0 < gamma) (smallDrop : 2*drop < gamma)
    (calibration : phi-drop ≤ a) : HasRate s mag log K a := by
  exact invariant_rate_transfer physical mag log exactSource normalization leading remainder
    (filled_remainder_strictly_below phi gamma drop a hgamma smallDrop calibration)

/-- A source supremum or another nonnegative budget; this is not a claim
that every polynomial satisfies an analytic source estimate. -/
def BudgetUpperRate (s : LevelScope) (log : LogScale R) (B : Nat → R) (b : R) : Prop :=
  ∀ ε, 0 < ε → EventuallyOn s (fun N => B N = 0 ∨ log.value N (B N) ≤ b+ε)

omit [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R] in
theorem budgetUpper_zero (s : LevelScope) (log : LogScale R) (b : R) :
    BudgetUpperRate s log (fun _ => 0) b := by
  intro ε _
  exact eventuallyOn_of_forall (by intros; exact Or.inl rfl)

theorem budgetUpper_const {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N) (log : LogScale R)
    (c : R) (hc : 0 ≤ c) : BudgetUpperRate s log (fun _ => c) 0 := by
  by_cases hz : c = 0
  · subst c
    exact budgetUpper_zero s log 0
  · have hp : 0 < c := by grind
    intro ε hε
    have hr := rateLimit_restrict (log.constant_limit c hp) physical
    exact eventuallyOn_mono (hr ε hε) (by intros; right; grind)

/-- A finite sum of positive majorants with a common upper rate still has
that rate. No estimate is claimed for a number of terms growing with N. -/
theorem budgetUpper_add {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N) (log : LogScale R)
    {B D : Nat → R} {b : R}
    (bn : ∀ N, s N → 0 ≤ B N) (dn : ∀ N, s N → 0 ≤ D N)
    (hb : BudgetUpperRate s log B b) (hd : BudgetUpperRate s log D b) :
    BudgetUpperRate s log (fun N => B N+D N) b := by
  intro ε hε
  have hq := positive_quarter ε hε
  have two : (0 : R) < 2 := by grind
  have ht := rateLimit_restrict (log.constant_limit 2 two) physical
  apply eventuallyOn_mono
    (eventuallyOn_and (eventuallyOn_and (hb (ε/4) hq.1) (hd (ε/4) hq.1))
      (ht (ε/4) hq.1))
  intro N hN h
  have b0 := bn N hN
  have d0 := dn N hN
  by_cases hz : B N+D N = 0
  · exact Or.inl hz
  · have sp : 0 < B N+D N := by grind
    right
    by_cases hbd : B N ≤ D N
    · have dp : 0 < D N := by grind
      have hu : log.value N (D N) ≤ b+ε/4 := by grind
      have comp := log.monotone N (B N+D N) (2*D N) sp (by grind)
      have prod := log.product N 2 (D N) two dp
      grind
    · have bp : 0 < B N := by grind
      have hu : log.value N (B N) ≤ b+ε/4 := by grind
      have comp := log.monotone N (B N+D N) (2*B N) sp (by grind)
      have prod := log.product N 2 (B N) two bp
      grind

theorem budgetUpper_mul {s : LevelScope} (log : LogScale R)
    {B D : Nat → R} {b d : R}
    (bn : ∀ N, s N → 0 ≤ B N) (dn : ∀ N, s N → 0 ≤ D N)
    (hb : BudgetUpperRate s log B b) (hd : BudgetUpperRate s log D d) :
    BudgetUpperRate s log (fun N => B N*D N) (b+d) := by
  intro ε hε
  have hq := positive_quarter ε hε
  apply eventuallyOn_mono (eventuallyOn_and (hb (ε/4) hq.1) (hd (ε/4) hq.1))
  intro N hN h
  have b0 := bn N hN
  have d0 := dn N hN
  by_cases bz : B N = 0
  · left
    change B N*D N = 0
    rw [bz]
    grind
  · by_cases dz : D N = 0
    · left
      change B N*D N = 0
      rw [dz]
      grind
    · have bp : 0 < B N := by grind
      have dp : 0 < D N := by grind
      have prod := log.product N (B N) (D N) bp dp
      right
      grind

theorem sector_sum_nonnegative {I : Type w} (indices : List I) (weight : I → R)
    (h : ∀ i ∈ indices, 0 ≤ weight i) : 0 ≤ sectorSum indices weight := by
  induction indices with
  | nil => simp only [sectorSum]; exact Std.le_refl _
  | cons i rest ih =>
    have hi := h i (by simp)
    have hr := ih (fun j hj => h j (by simp [hj]))
    simp only [sectorSum]
    grind

theorem budgetUpper_finite_sum {I : Type w} {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N) (log : LogScale R)
    (indices : List I) (weight : I → Nat → R) (b : R)
    (nonneg : ∀ i ∈ indices, ∀ N, s N → 0 ≤ weight i N)
    (bounds : ∀ i ∈ indices, BudgetUpperRate s log (weight i) b) :
    BudgetUpperRate s log (fun N => sectorSum indices (fun i => weight i N)) b := by
  induction indices with
  | nil => exact budgetUpper_zero s log b
  | cons i rest ih =>
    have ht := ih (fun j hj => nonneg j (by simp [hj]))
      (fun j hj => bounds j (by simp [hj]))
    have hn : ∀ N, s N → 0 ≤ sectorSum rest (fun j => weight j N) := by
      intro N hN
      exact sector_sum_nonnegative rest _ (fun j hj => nonneg j (by simp [hj]) N hN)
    exact budgetUpper_add physical log (nonneg i (by simp)) hn (bounds i (by simp)) ht

/-- Finite polynomial or other subexponential prefactors, still carrying
their actual sector indices, do not consume the common strict gap. -/
theorem finite_weighted_envelope_upperRate {I : Type w} {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N) (log : LogScale R)
    (indices : List I) (weight : I → Nat → R) (envelope : Nat → R) (b : R)
    (nonneg : ∀ i ∈ indices, ∀ N, s N → 0 ≤ weight i N)
    (envelope_nonnegative : ∀ N, s N → 0 ≤ envelope N)
    (weights : ∀ i ∈ indices, BudgetUpperRate s log (weight i) 0)
    (bound : BudgetUpperRate s log envelope b) :
    BudgetUpperRate s log
      (fun N => sectorSum indices (fun i => weight i N)*envelope N) b := by
  have hn : ∀ N, s N → 0 ≤ sectorSum indices (fun i => weight i N) := by
    intro N hN
    exact sector_sum_nonnegative indices _ (fun i hi => nonneg i hi N hN)
  have h := budgetUpper_mul log hn envelope_nonnegative
    (budgetUpper_finite_sum physical log indices weight 0 nonneg weights) bound
  have hz : (0 : R)+b = b := by grind
  rw [hz] at h
  exact h

/-- A fixed filling cost does not change an upper exponential rate. The
bound must apply to the actual complete remainder, on its admissible
canonical degree class. The cost may depend on the fixed signed fillings. -/
theorem filling_bound_preserves_upperRate {s : LevelScope}
    (physical : ∀ N, s N → physicalLevels N)
    (mag : Magnitude C R) (log : LogScale R)
    {E : Nat → C} {B : Nat → R} {b : R} (cost : R) (hcost : 0 < cost)
    (nonneg : ∀ N, s N → 0 ≤ B N)
    (bound : EventuallyOn s (fun N => mag.value (E N) ≤ cost*B N))
    (source : BudgetUpperRate s log B b) : HasUpperRate s mag log E b := by
  intro ε hε
  have hq := positive_quarter ε hε
  have hc := rateLimit_restrict (log.constant_limit cost hcost) physical
  apply eventuallyOn_mono
    (eventuallyOn_and bound (eventuallyOn_and (source (ε/4) hq.1) (hc (ε/4) hq.1)))
  intro N hN h
  by_cases he : E N = 0
  · exact Or.inl he
  · have hp := magnitude_positive mag he
    have bn := nonneg N hN
    have bp : 0 < B N := by
      by_cases hz : B N = 0
      · have heq : cost*B N = 0 := by rw [hz]; grind
        grind
      · grind
    have hb : log.value N (B N) ≤ b+ε/4 := by grind
    have hm := log.monotone N (mag.value (E N)) (cost*B N) hp h.1
    have prod := log.product N cost (B N) hcost bp
    right
    simp only [magnitudeRate]
    grind

/-- Construct the leading term from its actual nonzero amplitude and
carrier. In applications the carrier is exp(N A); its modulus rate is
Re(A). A relative 1+O(1/N) correction remains in the amplitude. -/
theorem leading_rate_from_amplitude {s : LevelScope}
    (mag : Magnitude C R) (log : LogScale R)
    {amplitude carrier G : Nat → C} {a : R}
    (amp : HasRate s mag log amplitude 0)
    (carrier_nonzero : EventuallyOn s (fun N => carrier N ≠ 0))
    (carrier_rate : EventuallyOn s (fun N => magnitudeRate mag log carrier N = a))
    (definition : EventuallyOn s (fun N => G N = amplitude N*carrier N)) :
    HasRate s mag log G a := by
  have hc : HasRate s mag log carrier a := by
    refine ⟨carrier_nonzero, ?_⟩
    apply rateLimit_congr (rateLimit_const s a)
    exact eventuallyOn_mono carrier_rate (by intros; exact Eq.symm ‹_›)
  have hm := hasRate_mul mag log amp hc
  have he := eventuallyOn_mono definition (by intros; exact Eq.symm ‹_›)
  have hr := hasRate_congr mag log hm he
  have hz : (0 : R)+a = a := by grind
  rw [hz] at hr
  exact hr

omit [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R] in
theorem hasRate_both_parities (mag : Magnitude C R) (log : LogScale R)
    {f : Nat → C} {a : R}
    (he : HasRate evenLevels mag log f a) (ho : HasRate oddLevels mag log f a) :
    HasRate physicalLevels mag log f a :=
  ⟨eventuallyOn_both_parities he.1 ho.1, rateLimit_both_parities he.2 ho.2⟩

/-- Geometry supplies this scalar equality for the same fixed knot and
action. The conclusion is the scaled epsilon limit, not an abstract label
called `VolumeConjecture`. -/
theorem calibrated_volume_rate {s : LevelScope} (mag : Magnitude C R)
    (log : LogScale R) {K : Nat → C} {a volume : R}
    (scale : R) (hscale : 0 ≤ scale) (rate : HasRate s mag log K a)
    (geometry : scale*a = volume) :
    EventuallyOn s (fun N => K N ≠ 0) ∧
    RateLimit s (fun N => scale*magnitudeRate mag log K N) volume := by
  constructor
  · exact rate.1
  · rw [← geometry]
    exact rateLimit_scale_nonnegative scale hscale rate.2

/-- Typed semantic data. The filling type may depend on the diagram, and
every sequence and volume is indexed by that same diagram and fixed
filling. This prevents an assembly from silently changing the invariant. -/
structure InvariantFamily (Diagram : Type w) (Filling : Diagram → Type w)
    (C : Type u) (R : Type v) where
  invariant : (D : Diagram) → Filling D → Nat → C
  volume : (D : Diagram) → Filling D → R

/-- The full conditional implication for a fixed member of a family. The
analytic estimates and geometric identification are premises, while
noncancellation, normalization restoration and the final limit are proved. -/
theorem fixed_filling_volume_transfer {Diagram : Type w} {Filling : Diagram → Type w}
    (family : InvariantFamily Diagram Filling C R) (D : Diagram) (p : Filling D)
    {s : LevelScope} (physical : ∀ N, s N → physicalLevels N)
    (mag : Magnitude C R) (log : LogScale R)
    {u G E : Nat → C} {a phi gamma drop : R}
    (exactSource : EventuallyOn s (fun N => family.invariant D p N = u N*(G N+E N)))
    (normalization : HasRate s mag log u 0) (leading : HasRate s mag log G a)
    (remainder : HasUpperRate s mag log E (phi-gamma))
    (hgamma : 0 < gamma) (smallDrop : 2*drop < gamma)
    (calibration : phi-drop ≤ a) (scale : R) (hscale : 0 ≤ scale)
    (geometry : scale*a = family.volume D p) :
    EventuallyOn s (fun N => family.invariant D p N ≠ 0) ∧
    RateLimit s (fun N => scale*magnitudeRate mag log (family.invariant D p) N)
      (family.volume D p) := by
  exact calibrated_volume_rate mag log scale hscale
    (invariant_rate_of_source_gap physical mag log exactSource normalization leading remainder
      hgamma smallDrop calibration) geometry

/-- Connect the actual finite sector contraction to the rate theorem.
The index list is the entire remainder, with multiplicities. The source
budget includes all weights and its analytic estimate remains explicit.
No operator bound is assumed outside the supplied admissible degree class. -/
theorem finite_source_rate_transfer {A I : Type w} [CommRing A]
    {s : LevelScope} (physical : ∀ N, s N → physicalLevels N)
    (mag : Magnitude C R) (log : LogScale R)
    (indices : List I) (full central : Nat → A) (term : Nat → I → A)
    (fill : Nat → A → C) (sourceSize : Nat → A → R)
    (admissible : Nat → A → Prop) (weight : Nat → I → R) (envelope : Nat → R)
    (cost : R) (hcost : 0 < cost) {K u : Nat → C} {a phi gamma drop : R}
    (source : ∀ N, s N → full N = central N + sectorSum indices (term N))
    (fill_zero : ∀ N, s N → fill N 0 = 0)
    (fill_add : ∀ N, s N → ∀ x y, fill N (x+y) = fill N x+fill N y)
    (sector_admissible : ∀ N, s N → ∀ i ∈ indices, admissible N (term N i))
    (operator_bound : ∀ N, s N → ∀ x, admissible N x →
      mag.value (fill N x) ≤ cost*sourceSize N x)
    (sector_bound : ∀ N, s N → ∀ i ∈ indices,
      sourceSize N (term N i) ≤ weight N i*envelope N)
    (budget_nonnegative : ∀ N, s N → 0 ≤ sectorSum indices (weight N)*envelope N)
    (budget : BudgetUpperRate s log
      (fun N => sectorSum indices (weight N)*envelope N) (phi-gamma))
    (exactInvariant : EventuallyOn s (fun N => K N = u N*fill N (full N)))
    (normalization : HasRate s mag log u 0)
    (leading : HasRate s mag log (fun N => fill N (central N)) a)
    (hgamma : 0 < gamma) (smallDrop : 2*drop < gamma) (calibration : phi-drop ≤ a) :
    HasRate s mag log K a := by
  let E : Nat → C := fun N => fill N (full N)-fill N (central N)
  have pointwise : EventuallyOn s (fun N => mag.value (E N) ≤
      cost*(sectorSum indices (weight N)*envelope N)) := by
    apply eventuallyOn_of_forall
    intro N hN
    have hz : mag.value 0 = 0 := (mag.eq_zero_iff 0).mpr rfl
    have h := finite_sector_filling_bound indices (term N) (full N) (central N)
      (fill N) (sourceSize N) mag.value (admissible N) (weight N) cost (envelope N)
      (source N hN) (fill_zero N hN) (fill_add N hN) hz mag.add_le
      (show 0 ≤ cost by grind) (sector_admissible N hN)
      (operator_bound N hN) (sector_bound N hN)
    change mag.value (fill N (full N)-fill N (central N)) ≤ _
    grind
  have upper := filling_bound_preserves_upperRate physical mag log cost hcost
    budget_nonnegative pointwise budget
  have exactSource : EventuallyOn s (fun N =>
      K N = u N*(fill N (central N)+E N)) := by
    apply eventuallyOn_mono exactInvariant
    intro N _ h
    dsimp [E]
    grind
  exact invariant_rate_of_source_gap physical mag log exactSource normalization leading upper
    hgamma smallDrop calibration

/-- The threshold is selected after the diagram, gap and admissibility
test, and before the fixed signed tuple. Analytic, action-drop and metric
thresholds may differ; their sum is a constructed common threshold.
There is no assertion uniform in a growing diagram or N-dependent tuple. -/
theorem long_filling_volume_transfer {Diagram I : Type w}
    (family : InvariantFamily Diagram (fun _ => I → Int) C R) (D : Diagram)
    (admissible : (I → Int) → Prop) (mag : Magnitude C R) (log : LogScale R)
    (u G E : (I → Int) → Nat → C) (action drop : (I → Int) → R)
    (phi gamma scale : R) (hgamma : 0 < gamma) (hscale : 0 ≤ scale)
    (exactSource : ∀ p, admissible p → EventuallyOn physicalLevels
      (fun N => family.invariant D p N = u p N*(G p N+E p N)))
    (normalization : ∀ p, admissible p → HasRate physicalLevels mag log (u p) 0)
    (remainder : ∀ p, admissible p → HasUpperRate physicalLevels mag log (E p) (phi-gamma))
    (calibration : ∀ p, admissible p → phi-drop p ≤ action p)
    (analytic : ∃ T, ∀ p, admissible p → LongEnough T p →
      HasRate physicalLevels mag log (G p) (action p))
    (smallDrop : ∃ T, ∀ p, admissible p → LongEnough T p → 2*drop p < gamma)
    (geometry : ∃ T, ∀ p, admissible p → LongEnough T p →
      scale*action p = family.volume D p) :
    ∃ T, ∀ p, admissible p → LongEnough T p →
      EventuallyOn physicalLevels (fun N => family.invariant D p N ≠ 0) ∧
      RateLimit physicalLevels
        (fun N => scale*magnitudeRate mag log (family.invariant D p) N) (family.volume D p) := by
  obtain ⟨ta, ha⟩ := analytic
  obtain ⟨td, hd⟩ := smallDrop
  obtain ⟨tg, hg⟩ := geometry
  refine ⟨ta+td+tg, fun p hp hl => ?_⟩
  have hla := longEnough_mono hl (show ta ≤ ta+td+tg by omega)
  have hld := longEnough_mono hl (show td ≤ ta+td+tg by omega)
  have hlg := longEnough_mono hl (show tg ≤ ta+td+tg by omega)
  exact fixed_filling_volume_transfer family D p (fun _ h => h) mag log
    (exactSource p hp) (normalization p hp) (ha p hp hla) (remainder p hp)
    hgamma (hd p hp hld) (calibration p hp) scale hscale (hg p hp hlg)

end VolumeLogic
