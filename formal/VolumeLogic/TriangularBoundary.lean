import VolumeLogic.ProtectedSum

namespace VolumeLogic
open Lean.Grind
universe u
variable {R : Type u} [CommRing R] [LE R] [LT R]
  [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]
attribute [local instance] Semiring.natCast Ring.intCast

/-!
Triangular insertion with three possibly positive boundary weights.
All costs and complete actions are doubled. `t` is twice the removed
triangle potential, `b` is the logarithm of the common boundary weight,
and `qa,qc` are twice the retained triangle potentials. Thus `t-b` is
the undoubled boundary correction Delta. The duplicate target is 2*b,
which must not be replaced by 2*t.

The three local rates and their sector map are the actual scalar maxima
constructed in ProtectedSum. No disk packing, source envelope, or
volume identification is proved by this module.
-/

theorem boundary_left_with_defect (t c qa defect : R)
    (h : t ≤ qa+defect) (hd : 0 ≤ defect) :
    protectedMax (2*c) (qa+c) ≤
      protectedMax (2*c) (t+c)+(qa+t)-2*t+defect := by
  have h1 := protectedMax_ge_left (2*c) (t+c)
  have h2 := protectedMax_ge_right (2*c) (t+c)
  apply protectedMax_le <;> grind

theorem boundary_right_with_defect (a t qc defect : R)
    (h : t ≤ qc+defect) (hd : 0 ≤ defect) :
    protectedMax (2*a) (qc+a) ≤
      (t+qc)+protectedMax (2*a) (t+a)-2*t+defect := by
  have h1 := protectedMax_ge_left (2*a) (t+a)
  have h2 := protectedMax_ge_right (2*a) (t+a)
  apply protectedMax_le <;> grind

/-- The simplex-vertex lower bounds permit a loss of at most Delta/2
in undoubled rates, without comparing either middle weight to the boundary. -/
theorem boundary_bridge_with_defect (s : ProtectedSector)
    (a b c t qa qc : R) (ht : b ≤ t) (ha : b ≤ qa) (hc : b ≤ qc) :
    protectedBridgeRate s a t c qa qc ≤
      protectedFirstRate s t c qc+protectedSecondRate s a t qa-2*t+(t-b) := by
  have hd : 0 ≤ t-b := by grind
  cases s with
  | central =>
    simp only [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide, Bool.false_eq_true, ↓reduceIte]
    grind
  | left =>
    have h : t ≤ qa+(t-b) := by grind
    simpa [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide] using boundary_left_with_defect t c qa (t-b) h hd
  | right =>
    have h : t ≤ qc+(t-b) := by grind
    simpa [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide] using boundary_right_with_defect a t qc (t-b) h hd

/-- A wholly central inserted block excludes the right output label.
Only the left retained triangle needs the conditional packing comparison. -/
theorem boundary_bridge_central_block (s : ProtectedSector)
    (a t c qa qc : R) (inactive : protectedSecondSide s = false)
    (ha : t ≤ qa) :
    protectedBridgeRate s a t c qa qc ≤
      protectedFirstRate s t c qc+protectedSecondRate s a t qa-2*t := by
  cases s with
  | central =>
    simp only [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide, Bool.false_eq_true, ↓reduceIte]
    grind
  | left =>
    simpa [protectedBridgeRate, protectedFirstRate, protectedSecondRate,
      protectedFirstSide, protectedSecondSide] using protected_sum_left t c qa ha
  | right => simp [protectedSecondSide] at inactive

/-- The ordinary target is counted once, even when all three boundary
vertices were ordinary in the core. -/
theorem boundary_total_with_defect (s : ProtectedSector)
    (a b c t qa qc rest1 rest2 target1 target2 : R)
    (ht : b ≤ t) (ha : b ≤ qa) (hc : b ≤ qc) :
    rest1+rest2+protectedBridgeRate s a t c qa qc-(target1+target2-2*b) ≤
      (rest1+protectedFirstRate s t c qc-target1)+
      (rest2+protectedSecondRate s a t qa-target2)-(t-b) := by
  have h := boundary_bridge_with_defect s a b c t qa qc ht ha hc
  grind

theorem boundary_total_central_block (s : ProtectedSector)
    (a b c t qa qc rest1 rest2 target1 target2 : R)
    (inactive : protectedSecondSide s = false) (ha : t ≤ qa) :
    rest1+rest2+protectedBridgeRate s a t c qa qc-(target1+target2-2*b) ≤
      (rest1+protectedFirstRate s t c qc-target1)+
      (rest2+protectedSecondRate s a t qa-target2)-2*(t-b) := by
  have h := boundary_bridge_central_block s a t c qa qc inactive ha
  grind

omit [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R]
  [OrderedRing R] in
/-- The complete conditional block action contains the exact correction. -/
theorem boundary_conditional_action_cancels (core block t b : R) :
    core+(block+2*(t-b))-2*(t-b) = core+block := by
  grind

/-- A noncentral block's absolute certificate absorbs the full bridge
defect, leaving an additional nonnegative Delta/2 margin. -/
theorem boundary_noncentral_block_margin
    (cost cost1 cost2 phi1 phi2 gap t b : R)
    (join : cost ≤ cost1+cost2-(t-b))
    (core : cost1 ≤ phi1) (block : cost2 ≤ phi2-gap) :
    cost ≤ phi1+phi2-gap-(t-b) := by
  grind

/-- The final scalar closure splits on the whole inserted block string.
A central root label alone does not imply that the block is central. -/
theorem boundary_certified_rate (s : ProtectedSector)
    (outsideFirst outsideSecond : Bool)
    (a b c t qa qc rest1 rest2 target1 target2 phi1 phi2 gap1 gap2 : R)
    (ht : b ≤ t) (ha : b ≤ qa) (hc : b ≤ qc)
    (coreUpper : rest1+protectedFirstRate s t c qc-target1 ≤ phi1)
    (coreCertificate : (outsideFirst || protectedFirstSide s) = true →
      rest1+protectedFirstRate s t c qc-target1 ≤ phi1-gap1)
    (blockCertificate : (outsideSecond || protectedSecondSide s) = true →
      rest2+protectedSecondRate s a t qa-target2 ≤ phi2-gap2)
    (centralBlock : (outsideSecond || protectedSecondSide s) = false →
      rest2+protectedSecondRate s a t qa-target2 ≤ phi2+2*(t-b))
    (centralTriangle : (outsideSecond || protectedSecondSide s) = false → t ≤ qa)
    (noncentral : outsideFirst = true ∨ outsideSecond = true ∨ s ≠ .central) :
    rest1+rest2+protectedBridgeRate s a t c qa qc-(target1+target2-2*b) ≤
      phi1+phi2-protectedMin gap1 gap2 := by
  have min1 := protectedMin_le_left gap1 gap2
  have min2 := protectedMin_le_right gap1 gap2
  have active := protected_sector_map_noncentral s outsideFirst outsideSecond noncentral
  by_cases hb : (outsideSecond || protectedSecondSide s) = true
  · have block := blockCertificate hb
    have join := boundary_total_with_defect s a b c t qa qc rest1 rest2 target1 target2 ht ha hc
    grind
  · have hfalse : (outsideSecond || protectedSecondSide s) = false := by
      cases h : (outsideSecond || protectedSecondSide s) <;> simp_all
    have hsecond : protectedSecondSide s = false := by
      cases outsideSecond <;> cases h : protectedSecondSide s <;> simp_all
    have hfirst : (outsideFirst || protectedFirstSide s) = true := by grind
    have block := centralBlock hfalse
    have core := coreCertificate hfirst
    have join := boundary_total_central_block s a b c t qa qc rest1 rest2 target1 target2
      hsecond (centralTriangle hfalse)
    grind

end VolumeLogic
