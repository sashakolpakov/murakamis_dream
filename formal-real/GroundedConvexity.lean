import WeightedGraph
import TransportCoercivity
import Mathlib.Analysis.Convex.Deriv
import Mathlib.Tactic.Linarith

/-!
Strict convexity and uniqueness for an actual grounded real potential.
The second derivative along a segment is identified with the constructed
weighted graph energy. Strict positivity follows from finite positive-edge
paths, rather than from an assumed positive-definite Hessian or strict
convexity. Existence is supplied by the actual supported transport potential.

Geometric differentiation, conductance signs and connected support, and the
feasible positive transport table remain written inputs. The derivative
hypotheses are weaker than C2 regularity: actual first and second derivatives
on the indicated segments suffice; continuity of the Hessian is not needed.
-/

namespace VolumeLogic.GroundedConvexity
open Set

variable {V E T : Type*}

/-- The coordinate space with one fixed zero coordinate. -/
def grounded (root : V) : Set (V → ℝ) := {x | x root = 0}

/-- The actual affine segment, with the same parameter on every coordinate. -/
def segment (x y : V → ℝ) (t : ℝ) : V → ℝ := (1 - t) • x + t • y

/-- The restriction of the actual potential to that segment. -/
def segmentValue (P : (V → ℝ) → ℝ) (x y : V → ℝ) (t : ℝ) : ℝ :=
  P (segment x y t)

theorem convex_grounded (root : V) : Convex ℝ (grounded root) := by
  intro x hx y hy a b _ _ _
  change a * x root + b * y root = 0
  simp only [show x root = 0 from hx, show y root = 0 from hy, mul_zero, add_zero]

theorem segment_grounded (root : V) (x y : V → ℝ)
    (hx : x ∈ grounded root) (hy : y ∈ grounded root) (t : ℝ) :
    segment x y t ∈ grounded root := by
  change (1 - t) * x root + t * y root = 0
  simp only [show x root = 0 from hx, show y root = 0 from hy, mul_zero, add_zero]

/-- Actual derivative data imply strict convexity on the closed interval.
First derivatives at the endpoints ensure the required continuity there. -/
theorem strictConvexOn_Icc_of_second_pos {g dg ddg : ℝ → ℝ} {a b : ℝ}
    (hg : ∀ t ∈ Icc a b, HasDerivAt g (dg t) t)
    (hdg : ∀ t ∈ Ioo a b, HasDerivAt dg (ddg t) t)
    (hpos : ∀ t ∈ Ioo a b, 0 < ddg t) :
    StrictConvexOn ℝ (Icc a b) g := by
  have heq : (interior (Icc a b)).EqOn (deriv g) dg :=
    deriv_eqOn isOpen_interior (fun t ht =>
      (hg t (interior_subset ht)).hasDerivWithinAt)
  apply strictConvexOn_of_deriv2_pos (convex_Icc a b)
    (fun t ht => (hg t ht).continuousAt.continuousWithinAt)
  intro t ht
  have hi : t ∈ Ioo a b := by simpa only [interior_Icc] using ht
  have hd : HasDerivWithinAt (deriv g) (ddg t) (interior (Icc a b)) t :=
    (hdg t hi).hasDerivWithinAt.congr heq (heq ht)
  simpa only [Function.iterate_succ_apply, Function.iterate_zero_apply] using
    (show 0 < deriv (deriv g) t from by
      rw [hd.hasDerivAt (isOpen_interior.mem_nhds ht) |>.deriv]
      exact hpos t hi)

/-- Along distinct grounded endpoints, the actual graph-valued second
derivative is strictly positive. Weights may depend on the point, and zero
edges are allowed, provided their positive support remains connected. -/
theorem segment_strictConvexOn [Fintype E]
    (P : (V → ℝ) → ℝ) (src dst : E → V)
    (w : (V → ℝ) → E → ℝ) (root : V)
    (x y : V → ℝ) (hx : x ∈ grounded root) (hy : y ∈ grounded root)
    (hxy : x ≠ y) (dg : ℝ → ℝ)
    (hfirst : ∀ t ∈ Icc (0 : ℝ) 1, HasDerivAt (segmentValue P x y) (dg t) t)
    (hsecond : ∀ t ∈ Ioo (0 : ℝ) 1,
      HasDerivAt dg (WeightedGraph.energy src dst (w (segment x y t)) (y - x)) t)
    (hw : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ e, 0 ≤ w (segment x y t) e)
    (hconn : ∀ t ∈ Ioo (0 : ℝ) 1,
      WeightedGraph.connected src dst (w (segment x y t))) :
    StrictConvexOn ℝ (Icc (0 : ℝ) 1) (segmentValue P x y) := by
  apply strictConvexOn_Icc_of_second_pos hfirst hsecond
  intro t ht
  apply WeightedGraph.grounded_energy_pos src dst (w (segment x y t))
    (hw t ht) (hconn t ht) root (y - x)
  · change y root - x root = 0
    simp only [show x root = 0 from hx, show y root = 0 from hy, sub_self]
  · exact sub_ne_zero.mpr (Ne.symm hxy)

/-- The strict Jensen inequality is derived for every distinct grounded
segment, with its actual common coordinate interpolation. -/
theorem segment_strict_jensen [Fintype E]
    (P : (V → ℝ) → ℝ) (src dst : E → V)
    (w : (V → ℝ) → E → ℝ) (root : V)
    (x y : V → ℝ) (hx : x ∈ grounded root) (hy : y ∈ grounded root)
    (hxy : x ≠ y) (dg : ℝ → ℝ)
    (hfirst : ∀ t ∈ Icc (0 : ℝ) 1, HasDerivAt (segmentValue P x y) (dg t) t)
    (hsecond : ∀ t ∈ Ioo (0 : ℝ) 1,
      HasDerivAt dg (WeightedGraph.energy src dst (w (segment x y t)) (y - x)) t)
    (hw : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ e, 0 ≤ w (segment x y t) e)
    (hconn : ∀ t ∈ Ioo (0 : ℝ) 1,
      WeightedGraph.connected src dst (w (segment x y t)))
    {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    P (segment x y t) < (1 - t) * P x + t * P y := by
  have hc := segment_strictConvexOn P src dst w root x y hx hy hxy dg
    hfirst hsecond hw hconn
  have h := hc.2 (show (0 : ℝ) ∈ Icc (0 : ℝ) 1 from ⟨le_rfl, zero_le_one⟩)
    (show (1 : ℝ) ∈ Icc (0 : ℝ) 1 from ⟨zero_le_one, le_rfl⟩)
    zero_ne_one (sub_pos.mpr ht.2) ht.1 (sub_add_cancel 1 t)
  simpa [segmentValue, segment] using h

/-- A C2 potential with the stated graph Hessian is strictly convex on the
grounded space. The explicit segment derivative data are sufficient even
without a separate continuity assumption on the Hessian. -/
theorem strictConvexOn_grounded [Fintype E]
    (P : (V → ℝ) → ℝ) (src dst : E → V)
    (w : (V → ℝ) → E → ℝ) (root : V)
    (dg : (V → ℝ) → (V → ℝ) → ℝ → ℝ)
    (hfirst : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Icc (0 : ℝ) 1,
      HasDerivAt (segmentValue P x y) (dg x y t) t)
    (hsecond : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Ioo (0 : ℝ) 1,
      HasDerivAt (dg x y)
        (WeightedGraph.energy src dst (w (segment x y t)) (y - x)) t)
    (hw : ∀ z ∈ grounded root, ∀ e, 0 ≤ w z e)
    (hconn : ∀ z ∈ grounded root, WeightedGraph.connected src dst (w z)) :
    StrictConvexOn ℝ (grounded root) P := by
  refine ⟨convex_grounded root, ?_⟩
  intro x hx y hy hxy a b ha hb hab
  have ht : b ∈ Ioo (0 : ℝ) 1 := ⟨hb, by linarith⟩
  have hs := segment_strict_jensen P src dst w root x y hx hy hxy (dg x y)
    (hfirst x hx y hy) (hsecond x hx y hy)
    (fun t _ => hw _ (segment_grounded root x y hx hy t))
    (fun t _ => hconn _ (segment_grounded root x y hx hy t)) ht
  have heq : 1 - b = a := by linarith
  simpa only [segment, heq, smul_eq_mul] using hs

/-- Two actual grounded global minimizers coincide. Strict convexity is
derived from the derivative/graph data in the theorem, not supplied. -/
theorem grounded_minimizer_eq [Fintype E]
    (P : (V → ℝ) → ℝ) (src dst : E → V)
    (w : (V → ℝ) → E → ℝ) (root : V)
    (dg : (V → ℝ) → (V → ℝ) → ℝ → ℝ)
    (hfirst : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Icc (0 : ℝ) 1,
      HasDerivAt (segmentValue P x y) (dg x y t) t)
    (hsecond : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Ioo (0 : ℝ) 1,
      HasDerivAt (dg x y)
        (WeightedGraph.energy src dst (w (segment x y t)) (y - x)) t)
    (hw : ∀ z ∈ grounded root, ∀ e, 0 ≤ w z e)
    (hconn : ∀ z ∈ grounded root, WeightedGraph.connected src dst (w z))
    {x y : V → ℝ} (hx : x ∈ grounded root) (hy : y ∈ grounded root)
    (hminx : ∀ z ∈ grounded root, P x ≤ P z)
    (hminy : ∀ z ∈ grounded root, P y ≤ P z) : x = y :=
  (strictConvexOn_grounded P src dst w root dg hfirst hsecond hw hconn).eq_of_isMinOn
    hminx hminy hx hy

/-- The constructed supported transport potential has exactly one grounded
minimum. Table feasibility, vertex lower bounds and continuity produce
existence; actual graph-valued segment derivatives produce uniqueness.
No relation between the two support presentations is silently imposed. -/
theorem exists_unique_grounded_minimizer [Fintype V] [Fintype T] [Fintype E]
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : TransportCoercivity.connected S) (root : V)
    (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, TransportCoercivity.rowMass S α t *
      TransportCoercivity.rowMax S hne h t - C t ≤ Q t h)
    (hcont : ∀ t, Continuous (Q t))
    (src dst : E → V) (w : (V → ℝ) → E → ℝ)
    (dg : (V → ℝ) → (V → ℝ) → ℝ → ℝ)
    (hfirst : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Icc (0 : ℝ) 1,
      HasDerivAt (segmentValue (TransportCoercivity.potential S α Q) x y) (dg x y t) t)
    (hsecond : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Ioo (0 : ℝ) 1,
      HasDerivAt (dg x y)
        (WeightedGraph.energy src dst (w (segment x y t)) (y - x)) t)
    (hw : ∀ z ∈ grounded root, ∀ e, 0 ≤ w z e)
    (hconn : ∀ z ∈ grounded root, WeightedGraph.connected src dst (w z)) :
    ∃! x : V → ℝ, x root = 0 ∧ ∀ y : V → ℝ, y root = 0 →
      TransportCoercivity.potential S α Q x ≤ TransportCoercivity.potential S α Q y := by
  obtain ⟨x, hx, hm⟩ := TransportCoercivity.exists_grounded_minimizer
    S hne α hα hc root Q C hQ hcont
  refine ⟨x, ⟨hx, hm⟩, ?_⟩
  intro y hy
  exact grounded_minimizer_eq (TransportCoercivity.potential S α Q) src dst w root dg
    hfirst hsecond hw hconn hy.1 hx hy.2 hm

end VolumeLogic.GroundedConvexity
