import VolumeLogic.RateComparison

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R] [LE R] [LT R]
  [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-!
Scalar source-rate logic for a protected triangular sum.

Every rate and target below is doubled.  `b` is the logarithm of the
joining radius; `qa` and `qc` are twice the two retained triangle rates.
The inequalities `b ≤ qa` and `b ≤ qc` are inputs, not formalized entropy
theorems.  The constructed sector map and all max branches are explicit.
No topology, analytic source envelope, spectral functional, or volume
identity is formalized in this module.
-/

noncomputable def protectedMax (x y : R) : R := by
  classical
  exact if x ≤ y then y else x

noncomputable def protectedMin (x y : R) : R := by
  classical
  exact if x ≤ y then x else y

omit [CommRing R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R]
  [OrderedRing R] in
theorem protectedMax_le (x y z : R) (hx : x ≤ z) (hy : y ≤ z) :
    protectedMax x y ≤ z := by
  unfold protectedMax
  split <;> grind

theorem protectedMax_ge_left (x y : R) : x ≤ protectedMax x y := by
  unfold protectedMax
  split <;> grind

theorem protectedMax_ge_right (x y : R) : y ≤ protectedMax x y := by
  unfold protectedMax
  split <;> grind

theorem protectedMin_le_left (x y : R) : protectedMin x y ≤ x := by
  unfold protectedMin
  split <;> grind

theorem protectedMin_le_right (x y : R) : protectedMin x y ≤ y := by
  unfold protectedMin
  split <;> grind

omit [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R] in
theorem protectedMin_positive (x y : R) (hx : 0 < x) (hy : 0 < y) :
    0 < protectedMin x y := by
  unfold protectedMin
  split <;> grind

omit [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R]
  [OrderedRing R] in
/-- The doubled complete bridge rates, with both singleton rows retained. -/
theorem protected_sum_central (b qa qc : R) :
    qa + qc = (b + qc) + (qa + b) - 2*b := by
  grind

/-- LEFT keeps the maximum of its pure and mixed branches. -/
theorem protected_sum_left (b c qa : R) (hqa : b ≤ qa) :
    protectedMax (2*c) (qa+c) ≤
      protectedMax (2*c) (b+c) + (qa+b) - 2*b := by
  have h1 := protectedMax_ge_left (2*c) (b+c)
  have h2 := protectedMax_ge_right (2*c) (b+c)
  apply protectedMax_le <;> grind

/-- RIGHT uses the reflected, separately recorded mixed branch. -/
theorem protected_sum_right (a b qc : R) (hqc : b ≤ qc) :
    protectedMax (2*a) (qc+a) ≤
      (b+qc) + protectedMax (2*a) (b+a) - 2*b := by
  have h1 := protectedMax_ge_left (2*a) (b+a)
  have h2 := protectedMax_ge_right (2*a) (b+a)
  apply protectedMax_le <;> grind

inductive ProtectedSector where
  | central
  | left
  | right
  deriving DecidableEq

def protectedFirstSide : ProtectedSector → Bool
  | .left => true
  | _ => false

def protectedSecondSide : ProtectedSector → Bool
  | .right => true
  | _ => false

noncomputable def protectedBridgeRate (s : ProtectedSector)
    (a _b c qa qc : R) : R :=
  match s with
  | .central => qa + qc
  | .left => protectedMax (2*c) (qa+c)
  | .right => protectedMax (2*a) (qc+a)

noncomputable def protectedFirstRate (s : ProtectedSector)
    (b c qc : R) : R :=
  if protectedFirstSide s then protectedMax (2*c) (b+c) else b+qc

noncomputable def protectedSecondRate (s : ProtectedSector)
    (a b qa : R) : R :=
  if protectedSecondSide s then protectedMax (2*a) (b+a) else qa+b

theorem protected_sum_bridge (s : ProtectedSector) (a b c qa qc : R)
    (hqa : b ≤ qa) (hqc : b ≤ qc) :
    protectedBridgeRate s a b c qa qc ≤
      protectedFirstRate s b c qc + protectedSecondRate s a b qa - 2*b := by
  cases s with
  | central =>
    simp only [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide, Bool.false_eq_true, ↓reduceIte]
    have h := protected_sum_central b qa qc
    grind
  | left =>
    simpa [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide] using protected_sum_left b c qa hqa
  | right =>
    simpa [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide] using protected_sum_right a b qc hqc

/-- Outside labels are retained; a noncentral output induces a noncentral input. -/
theorem protected_sector_map_noncentral (s : ProtectedSector)
    (outsideFirst outsideSecond : Bool)
    (h : outsideFirst = true ∨ outsideSecond = true ∨ s ≠ .central) :
    (outsideFirst || protectedFirstSide s) = true ∨
      (outsideSecond || protectedSecondSide s) = true := by
  cases s <;> cases outsideFirst <;> cases outsideSecond <;>
    simp_all [protectedFirstSide, protectedSecondSide]

omit [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R]
  [OrderedRing R] in
/-- The removed bridge contribution and duplicated target cancel exactly. -/
theorem protected_sum_target_cancellation (r1 r2 t1 t2 b : R) :
    (r1+r2-2*b) - (t1+t2-2*b) = (r1-t1)+(r2-t2) := by
  grind

theorem protected_sum_total_rate (s : ProtectedSector)
    (a b c qa qc rest1 rest2 target1 target2 : R)
    (hqa : b ≤ qa) (hqc : b ≤ qc) :
    rest1+rest2+protectedBridgeRate s a b c qa qc-(target1+target2-2*b) ≤
      (rest1+protectedFirstRate s b c qc-target1) +
      (rest2+protectedSecondRate s a b qa-target2) := by
  have h := protected_sum_bridge s a b c qa qc hqa hqc
  grind

omit [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R]
  [OrderedRing R] in
/-- Central costs add exactly, without taking separate local infima. -/
theorem protected_sum_central_total
    (b qa qc rest1 rest2 target1 target2 : R) :
    rest1+rest2+(qa+qc)-(target1+target2-2*b) =
      (rest1+(b+qc)-target1)+(rest2+(qa+b)-target2) := by
  grind

theorem protected_sum_common_gap (cost cost1 cost2 phi1 phi2 gap gap1 gap2 : R)
    (join : cost ≤ cost1+cost2)
    (upper1 : cost1 ≤ phi1) (upper2 : cost2 ≤ phi2)
    (chosen : cost1 ≤ phi1-gap1 ∨ cost2 ≤ phi2-gap2)
    (common1 : gap ≤ gap1) (common2 : gap ≤ gap2) :
    cost ≤ phi1+phi2-gap := by
  cases chosen <;> grind

theorem protected_sum_min_gap (cost cost1 cost2 phi1 phi2 gap1 gap2 : R)
    (join : cost ≤ cost1+cost2)
    (upper1 : cost1 ≤ phi1) (upper2 : cost2 ≤ phi2)
    (chosen : cost1 ≤ phi1-gap1 ∨ cost2 ≤ phi2-gap2) :
    cost ≤ phi1+phi2-protectedMin gap1 gap2 := by
  exact protected_sum_common_gap cost cost1 cost2 phi1 phi2
    (protectedMin gap1 gap2) gap1 gap2 join upper1 upper2 chosen
    (protectedMin_le_left gap1 gap2) (protectedMin_le_right gap1 gap2)

theorem protected_sum_strict_gap (cost cost1 cost2 phi1 phi2 gap1 gap2 : R)
    (join : cost ≤ cost1+cost2)
    (upper1 : cost1 ≤ phi1) (upper2 : cost2 ≤ phi2)
    (chosen : cost1 ≤ phi1-gap1 ∨ cost2 ≤ phi2-gap2)
    (positive1 : 0 < gap1) (positive2 : 0 < gap2) :
    cost < phi1+phi2 := by
  have hg := protectedMin_positive gap1 gap2 positive1 positive2
  have hb := protected_sum_min_gap cost cost1 cost2 phi1 phi2 gap1 gap2
    join upper1 upper2 chosen
  grind

/-- The sector map selects one of the two actual input certificate hypotheses. -/
theorem protected_sum_sector_gap (s : ProtectedSector)
    (outsideFirst outsideSecond : Bool)
    (cost cost1 cost2 phi1 phi2 gap1 gap2 : R)
    (join : cost ≤ cost1+cost2)
    (upper1 : cost1 ≤ phi1) (upper2 : cost2 ≤ phi2)
    (certificate1 : (outsideFirst || protectedFirstSide s) = true →
      cost1 ≤ phi1-gap1)
    (certificate2 : (outsideSecond || protectedSecondSide s) = true →
      cost2 ≤ phi2-gap2)
    (noncentral : outsideFirst = true ∨ outsideSecond = true ∨ s ≠ .central) :
    cost ≤ phi1+phi2-protectedMin gap1 gap2 := by
  have active := protected_sector_map_noncentral s outsideFirst outsideSecond noncentral
  have chosen : cost1 ≤ phi1-gap1 ∨ cost2 ≤ phi2-gap2 := by
    cases active with
    | inl h => exact Or.inl (certificate1 h)
    | inr h => exact Or.inr (certificate2 h)
  exact protected_sum_min_gap cost cost1 cost2 phi1 phi2 gap1 gap2
    join upper1 upper2 chosen

/-- The whole doubled-rate statement, with the local max rates and targets
substituted rather than an assumed final joined-rate inequality. -/
theorem protected_sum_certified_rate (s : ProtectedSector)
    (outsideFirst outsideSecond : Bool)
    (a b c qa qc rest1 rest2 target1 target2 phi1 phi2 gap1 gap2 : R)
    (hqa : b ≤ qa) (hqc : b ≤ qc)
    (upper1 : rest1+protectedFirstRate s b c qc-target1 ≤ phi1)
    (upper2 : rest2+protectedSecondRate s a b qa-target2 ≤ phi2)
    (certificate1 : (outsideFirst || protectedFirstSide s) = true →
      rest1+protectedFirstRate s b c qc-target1 ≤ phi1-gap1)
    (certificate2 : (outsideSecond || protectedSecondSide s) = true →
      rest2+protectedSecondRate s a b qa-target2 ≤ phi2-gap2)
    (noncentral : outsideFirst = true ∨ outsideSecond = true ∨ s ≠ .central)
    (positive1 : 0 < gap1) (positive2 : 0 < gap2) :
    rest1+rest2+protectedBridgeRate s a b c qa qc-(target1+target2-2*b) ≤
        phi1+phi2-protectedMin gap1 gap2 ∧
      rest1+rest2+protectedBridgeRate s a b c qa qc-(target1+target2-2*b) <
        phi1+phi2 := by
  have joined := protected_sum_total_rate s a b c qa qc rest1 rest2 target1 target2
    hqa hqc
  have bound := protected_sum_sector_gap s outsideFirst outsideSecond
    (rest1+rest2+protectedBridgeRate s a b c qa qc-(target1+target2-2*b))
    (rest1+protectedFirstRate s b c qc-target1)
    (rest2+protectedSecondRate s a b qa-target2)
    phi1 phi2 gap1 gap2 joined upper1 upper2 certificate1 certificate2 noncentral
  have positive := protectedMin_positive gap1 gap2 positive1 positive2
  constructor <;> grind

theorem protected_total_pair_bound (entries : List (R × R))
    (bounds : ∀ p ∈ entries, p.1 ≤ p.2) :
    total (entries.map Prod.fst) ≤ total (entries.map Prod.snd) := by
  induction entries with
  | nil => simp [total]
  | cons p ps ih =>
    have hp := bounds p (by simp)
    have hs : ∀ q ∈ ps, q.1 ≤ q.2 := by
      intro q hq
      exact bounds q (by simp [hq])
    have hi := ih hs
    simp only [List.map_cons, total]
    grind

/-- A common gap at one chosen block survives summing all upper-bounded blocks. -/
theorem protected_total_pair_gap (entries : List (R × R)) (gap : R)
    (bounds : ∀ p ∈ entries, p.1 ≤ p.2)
    (chosen : ∃ p ∈ entries, p.1 ≤ p.2-gap) :
    total (entries.map Prod.fst) ≤ total (entries.map Prod.snd)-gap := by
  induction entries with
  | nil => simp at chosen
  | cons p ps ih =>
    have hp := bounds p (by simp)
    have hs : ∀ q ∈ ps, q.1 ≤ q.2 := by
      intro q hq
      exact bounds q (by simp [hq])
    obtain ⟨q, hq, hgap⟩ := chosen
    have mem : q = p ∨ q ∈ ps := by simpa using hq
    cases mem with
    | inl heq =>
      subst q
      have hi := protected_total_pair_bound ps hs
      simp only [List.map_cons, total]
      grind
    | inr hmem =>
      have hi := ih hs ⟨q, hmem, hgap⟩
      simp only [List.map_cons, total]
      grind

/-- Finite assembly, conditional on iterated local comparisons giving `join`.
Each pair stores its actual input cost and complete action. -/
theorem protected_finite_assembly_gap (entries : List (R × R)) (cost gap : R)
    (join : cost ≤ total (entries.map Prod.fst))
    (bounds : ∀ p ∈ entries, p.1 ≤ p.2)
    (chosen : ∃ p ∈ entries, p.1 ≤ p.2-gap)
    (positive : 0 < gap) :
    cost ≤ total (entries.map Prod.snd)-gap ∧
      cost < total (entries.map Prod.snd) := by
  have h := protected_total_pair_gap entries gap bounds chosen
  constructor <;> grind

end VolumeLogic
