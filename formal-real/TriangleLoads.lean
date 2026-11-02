import WeightedGraph
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
Actual derivatives of the three arctangent loads of an exponential triangle.
Nonnegative corner coefficients and a positive radicand include both a fully
positive triangle and a triangle with exactly one zero corner. The resulting
Jacobian is identified with the explicit three-edge graph form.

Identifying these loads with the gradient of the entropy-envelope potential,
and identifying the geometric incidence data, remain written inputs.
-/

namespace VolumeLogic.TriangleLoads
open scoped BigOperators

/-- The actual corner weights in logarithmic coordinates. -/
noncomputable def weights (a q : Fin 3 → ℝ) (i : Fin 3) : ℝ :=
  a i * Real.exp (q i)

noncomputable def radicand (w : Fin 3 → ℝ) : ℝ :=
  w 0 * w 1 + w 1 * w 2 + w 2 * w 0

noncomputable def triangleD (w : Fin 3 → ℝ) : ℝ := Real.sqrt (radicand w)

/-- This arctangent formula is used only when the radicand is positive. -/
noncomputable def load (a q : Fin 3 → ℝ) (i : Fin 3) : ℝ :=
  Real.arctan (weights a q i / triangleD (weights a q)) / Real.pi

/-- The off-diagonal conductance; diagonal entries are immaterial because
they are multiplied by a zero endpoint difference. -/
noncomputable def conductance (w : Fin 3 → ℝ) (i j : Fin 3) : ℝ :=
  w i * w j / (2 * Real.pi * triangleD w * (w i + w j))

noncomputable def jacobianAction (w h : Fin 3 → ℝ) (i : Fin 3) : ℝ :=
  ∑ j, conductance w i j * (h i - h j)

noncomputable def radicandRate (w h : Fin 3 → ℝ) : ℝ :=
  w 0 * w 1 * (h 0 + h 1) + w 1 * w 2 * (h 1 + h 2) +
    w 2 * w 0 * (h 2 + h 0)

/-- Edge labels 0,1,2 represent the unordered corner pairs 01,02,12. -/
def edgeSrc : Fin 3 → Fin 3 := ![0, 0, 1]

def edgeDst : Fin 3 → Fin 3 := ![1, 2, 2]

theorem weights_nonneg (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i) :
    ∀ i, 0 ≤ weights a q i := by
  intro i
  exact mul_nonneg (ha i) (le_of_lt (Real.exp_pos _))

theorem weights_pos_iff (a q : Fin 3 → ℝ) (i : Fin 3) :
    0 < weights a q i ↔ 0 < a i := by
  exact mul_pos_iff_of_pos_right (Real.exp_pos _)

theorem weights_hasDerivAt (a q h : Fin 3 → ℝ) (i : Fin 3) :
    HasDerivAt (fun t : ℝ => weights a (fun j => q j + t * h j) i)
      (weights a q i * h i) 0 := by
  have hl : HasDerivAt (fun t : ℝ => q i + t * h i) (h i) 0 := by
    simpa using ((hasDerivAt_id (0 : ℝ)).mul_const (h i)).const_add (q i)
  simpa [weights, mul_assoc] using hl.exp.const_mul (a i)

theorem radicand_pos_of_positive_pair (w : Fin 3 → ℝ) (hw : ∀ i, 0 ≤ w i)
    (i j : Fin 3) (hij : i ≠ j) (hi : 0 < w i) (hj : 0 < w j) :
    0 < radicand w := by
  fin_cases i <;> fin_cases j <;> simp_all [radicand] <;>
    nlinarith [mul_nonneg (hw 0) (hw 1), mul_nonneg (hw 1) (hw 2),
      mul_nonneg (hw 2) (hw 0), mul_pos hi hj]

/-- A positive triangle radicand excludes two simultaneous zero corners. -/
theorem pair_sum_pos (w : Fin 3 → ℝ) (hw : ∀ i, 0 ≤ w i)
    (hs : 0 < radicand w) (i j : Fin 3) (hij : i ≠ j) :
    0 < w i + w j := by
  by_contra hn
  have hi : w i = 0 := by linarith [hw i, hw j]
  have hj : w j = 0 := by linarith [hw i, hw j]
  fin_cases i <;> fin_cases j <;> simp_all [radicand]

theorem triangleD_pos (w : Fin 3 → ℝ) (hs : 0 < radicand w) :
    0 < triangleD w := Real.sqrt_pos.mpr hs

theorem triangleD_sq (w : Fin 3 → ℝ) (hs : 0 < radicand w) :
    triangleD w ^ 2 = radicand w := Real.sq_sqrt (le_of_lt hs)

theorem conductance_symm (w : Fin 3 → ℝ) (i j : Fin 3) :
    conductance w i j = conductance w j i := by
  simp only [conductance, mul_comm (w i), add_comm (w i)]

theorem conductance_nonneg (w : Fin 3 → ℝ) (hw : ∀ i, 0 ≤ w i)
    (i j : Fin 3) : 0 ≤ conductance w i j := by
  unfold conductance triangleD
  exact div_nonneg (mul_nonneg (hw i) (hw j))
    (mul_nonneg (mul_nonneg (mul_nonneg (by norm_num) (le_of_lt Real.pi_pos))
      (Real.sqrt_nonneg _)) (add_nonneg (hw i) (hw j)))

theorem conductance_pos (w : Fin 3 → ℝ) (hs : 0 < radicand w)
    (i j : Fin 3) (hi : 0 < w i) (hj : 0 < w j) :
    0 < conductance w i j := by
  unfold conductance
  exact div_pos (mul_pos hi hj)
    (mul_pos (mul_pos (mul_pos (by norm_num) Real.pi_pos)
      (triangleD_pos w hs)) (add_pos hi hj))

/-- The rational simplification behind the derivative, proved independently
of any entropy or Hessian interpretation. -/
theorem derivative_algebra (x y z D h k l : ℝ)
    (hD : 0 < D) (hDs : D ^ 2 = x * y + y * z + z * x)
    (hxy : x + y ≠ 0) (hxz : x + z ≠ 0) :
    (1 / (1 + (x / D) ^ 2) *
      ((x * h * D - x *
        ((x * y * (h + k) + y * z * (k + l) + z * x * (l + h)) /
          (2 * D))) / D ^ 2)) / Real.pi =
      x * y / (2 * Real.pi * D * (x + y)) * (h - k) +
      x * z / (2 * Real.pi * D * (x + z)) * (h - l) := by
  have hd : D ≠ 0 := ne_of_gt hD
  have hp : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  have hden : D ^ 2 + x ^ 2 ≠ 0 := ne_of_gt (by positivity)
  have hf : D ^ 2 + x ^ 2 = (x + y) * (x + z) := by nlinarith [hDs]
  have hr :
      (1 / (1 + (x / D) ^ 2) *
        ((x * h * D - x *
          ((x * y * (h + k) + y * z * (k + l) + z * x * (l + h)) /
            (2 * D))) / D ^ 2)) / Real.pi =
      x * (2 * D ^ 2 * h -
        (x * y * (h + k) + y * z * (k + l) + z * x * (l + h))) /
        (2 * Real.pi * D * (D ^ 2 + x ^ 2)) := by
    field_simp
  rw [hr, hf, hDs]
  field_simp
  ring

theorem radicand_hasDerivAt (a q h : Fin 3 → ℝ) :
    HasDerivAt (fun t : ℝ => radicand (weights a (fun j => q j + t * h j)))
      (radicandRate (weights a q) h) 0 := by
  have h0 := weights_hasDerivAt a q h 0
  have h1 := weights_hasDerivAt a q h 1
  have h2 := weights_hasDerivAt a q h 2
  have hd := ((h0.mul h1).add (h1.mul h2)).add (h2.mul h0)
  simp only [zero_mul, add_zero] at hd
  have hr :
      (weights a q 0 * h 0 * weights a q 1 + weights a q 0 * (weights a q 1 * h 1)) +
      (weights a q 1 * h 1 * weights a q 2 + weights a q 1 * (weights a q 2 * h 2)) +
      (weights a q 2 * h 2 * weights a q 0 + weights a q 2 * (weights a q 0 * h 0)) =
      radicandRate (weights a q) h := by
    unfold radicandRate
    ring
  rw [hr] at hd
  exact hd

theorem triangleD_hasDerivAt (a q h : Fin 3 → ℝ)
    (hs : 0 < radicand (weights a q)) :
    HasDerivAt (fun t : ℝ => triangleD (weights a (fun j => q j + t * h j)))
      (radicandRate (weights a q) h / (2 * triangleD (weights a q))) 0 := by
  have hzero : radicand (weights a (fun j => q j + 0 * h j)) ≠ 0 := by
    simpa using ne_of_gt hs
  simpa only [triangleD, zero_mul, add_zero] using
    (radicand_hasDerivAt a q h).sqrt hzero

theorem derivative_algebra_vector (w h : Fin 3 → ℝ) (hw : ∀ i, 0 ≤ w i)
    (hs : 0 < radicand w) (i : Fin 3) :
    (1 / (1 + (w i / triangleD w) ^ 2) *
      ((w i * h i * triangleD w -
        w i * (radicandRate w h / (2 * triangleD w))) / triangleD w ^ 2)) /
      Real.pi = jacobianAction w h i := by
  have hd := triangleD_pos w hs
  have hds := triangleD_sq w hs
  have hp01 := ne_of_gt (pair_sum_pos w hw hs 0 1 (by decide))
  have hp02 := ne_of_gt (pair_sum_pos w hw hs 0 2 (by decide))
  have hp12 := ne_of_gt (pair_sum_pos w hw hs 1 2 (by decide))
  have hi : i = 0 ∨ i = 1 ∨ i = 2 := by fin_cases i <;> simp
  rcases hi with rfl | rfl | rfl
  · simpa only [jacobianAction, Fin.sum_univ_three, sub_self, mul_zero,
      zero_add, conductance, radicandRate] using
      derivative_algebra (w 0) (w 1) (w 2) (triangleD w) (h 0) (h 1) (h 2)
        hd hds hp01 hp02
  · have hds' : triangleD w ^ 2 = w 1 * w 0 + w 0 * w 2 + w 2 * w 1 := by
      rw [hds]
      unfold radicand
      ring
    have hp10 : w 1 + w 0 ≠ 0 := by simpa only [add_comm] using hp01
    convert derivative_algebra (w 1) (w 0) (w 2) (triangleD w) (h 1) (h 0) (h 2)
      hd hds' hp10 hp12 using 1 <;>
      simp only [jacobianAction, Fin.sum_univ_three, sub_self, mul_zero,
        add_zero, conductance, radicandRate]; ring
  · have hds' : triangleD w ^ 2 = w 2 * w 0 + w 0 * w 1 + w 1 * w 2 := by
      rw [hds]
      unfold radicand
      ring
    have hp20 : w 2 + w 0 ≠ 0 := by simpa only [add_comm] using hp02
    have hp21 : w 2 + w 1 ≠ 0 := by simpa only [add_comm] using hp12
    convert derivative_algebra (w 2) (w 0) (w 1) (triangleD w) (h 2) (h 0) (h 1)
      hd hds' hp20 hp21 using 1 <;>
      simp only [jacobianAction, Fin.sum_univ_three, sub_self, mul_zero,
        add_zero, conductance, radicandRate]; ring

/-- The derivative of the actual load formula along an arbitrary logarithmic
direction. The identity is derived by the exponential/square-root/arctangent
chain rules, including at a zero corner. -/
theorem load_hasDerivAt (a q h : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hs : 0 < radicand (weights a q)) (i : Fin 3) :
    HasDerivAt (fun t : ℝ => load a (fun j => q j + t * h j) i)
      (jacobianAction (weights a q) h i) 0 := by
  have hden : triangleD (weights a (fun j => q j + 0 * h j)) ≠ 0 := by
    simpa using ne_of_gt (triangleD_pos (weights a q) hs)
  have hc := (((weights_hasDerivAt a q h i).div
    (triangleD_hasDerivAt a q h hs) hden).arctan).div_const Real.pi
  simp only [Pi.div_apply, zero_mul, add_zero] at hc
  rw [derivative_algebra_vector (weights a q) h (weights_nonneg a q ha) hs i] at hc
  exact hc

theorem jacobianAction_single_off_diagonal (w : Fin 3 → ℝ)
    (i j : Fin 3) (hij : i ≠ j) :
    jacobianAction w (Pi.single j 1) i = -conductance w i j := by
  classical
  simp [jacobianAction, Pi.single_apply, hij, eq_comm]

/-- In particular the off-diagonal entry is the derivative of an actual
coordinate variation, not an assumed Hessian entry. -/
theorem load_off_diagonal_hasDerivAt (a q : Fin 3 → ℝ)
    (ha : ∀ i, 0 ≤ a i) (hs : 0 < radicand (weights a q))
    (i j : Fin 3) (hij : i ≠ j) :
    HasDerivAt (fun t : ℝ => load a
      (fun k => q k + t * (Pi.single j 1 : Fin 3 → ℝ) k) i)
      (-conductance (weights a q) i j) 0 := by
  simpa only [jacobianAction_single_off_diagonal (weights a q) i j hij] using
    load_hasDerivAt a q (Pi.single j 1) ha hs i

theorem jacobianAction_constant (w : Fin 3 → ℝ) (c : ℝ) :
    jacobianAction w (fun _ => c) = 0 := by
  funext i
  simp [jacobianAction]

/-- The full bilinear pairing is the graph form on the three actual corner
pairs. Each unordered pair is counted once. -/
theorem jacobian_pairing (w h k : Fin 3 → ℝ) :
    (∑ i, h i * jacobianAction w k i) =
      WeightedGraph.form edgeSrc edgeDst
        (fun e => conductance w (edgeSrc e) (edgeDst e)) h k := by
  simp [jacobianAction, Fin.sum_univ_three, WeightedGraph.form, edgeSrc, edgeDst]
  rw [conductance_symm w 1 0, conductance_symm w 2 0, conductance_symm w 2 1]
  ring

theorem jacobian_energy (w h : Fin 3 → ℝ) :
    (∑ i, h i * jacobianAction w h i) =
      WeightedGraph.energy edgeSrc edgeDst
        (fun e => conductance w (edgeSrc e) (edgeDst e)) h := by
  rw [jacobian_pairing, WeightedGraph.energy_eq_form_self]

/-- Pairing the derivative of the actual loads with the direction gives
the actual graph energy, with the same factor 1/(2*pi). -/
theorem load_pairing_hasDerivAt (a q h : Fin 3 → ℝ)
    (ha : ∀ i, 0 ≤ a i) (hs : 0 < radicand (weights a q)) :
    HasDerivAt
      (fun t : ℝ => ∑ i, h i * load a (fun j => q j + t * h j) i)
      (WeightedGraph.energy edgeSrc edgeDst
        (fun e => conductance (weights a q) (edgeSrc e) (edgeDst e)) h) 0 := by
  have hd := HasDerivAt.fun_sum (u := Finset.univ)
    (fun i _ => (load_hasDerivAt a q h ha hs i).const_mul (h i))
  rw [jacobian_energy] at hd
  exact hd

/-- For a finite collection of triangles, all corners are evaluated at the
same vertex function. The resulting edge type is the actual product of
triangle labels with the three local pair labels, so parallel edges and
coincident corner labels are preserved. -/
theorem sum_load_pairing_hasDerivAt {T V : Type*} [Fintype T]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (q h : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, 0 < radicand (weights (a t) (fun i => q (corners t i)))) :
    HasDerivAt
      (fun u : ℝ => ∑ t, ∑ i, h (corners t i) *
        load (a t) (fun j => q (corners t j) + u * h (corners t j)) i)
      (WeightedGraph.energy
        (fun e : T × Fin 3 => corners e.1 (edgeSrc e.2))
        (fun e : T × Fin 3 => corners e.1 (edgeDst e.2))
        (fun e : T × Fin 3 => conductance
          (weights (a e.1) (fun i => q (corners e.1 i))) (edgeSrc e.2) (edgeDst e.2)) h) 0 := by
  have hd := HasDerivAt.fun_sum (u := Finset.univ)
    (fun t _ => load_pairing_hasDerivAt (a t) (fun i => q (corners t i))
      (fun i => h (corners t i)) (ha t) (hs t))
  simpa only [WeightedGraph.energy, Fintype.sum_prod_type] using hd

/-- A zero corner stays identically zero in logarithmic coordinates. This
does not replace a positive-radicand triangle by a singleton. -/
theorem load_zero_corner (a q : Fin 3 → ℝ) (i : Fin 3) (hi : a i = 0) :
    load a q i = 0 := by
  simp [load, weights, hi]

/-- A singleton is defined separately: its sole supported corner receives
mass one half. The arctangent formula is not evaluated at D=0 to define it. -/
noncomputable def singletonLoad (active : Fin 3) (_q : Fin 3 → ℝ) (i : Fin 3) : ℝ :=
  if i = active then 1 / 2 else 0

theorem singletonLoad_hasDerivAt (active : Fin 3) (q h : Fin 3 → ℝ) (i : Fin 3) :
    HasDerivAt (fun t : ℝ => singletonLoad active (fun j => q j + t * h j) i) 0 0 :=
  hasDerivAt_const 0 _

end VolumeLogic.TriangleLoads
