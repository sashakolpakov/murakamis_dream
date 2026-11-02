import WeightedGraph
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

/-!
The actual finite weighted graph Laplacian with one coordinate grounded.
The reduced matrix is the principal submatrix obtained by deleting that
coordinate. Its invertibility is derived from nonnegative weights and finite
paths in their positive support, not assumed as a matrix hypothesis.

The identification of a geometric Hessian with this matrix remains a written
input. No nonlinear implicit-function or uniform inverse bound is asserted.
-/

namespace VolumeLogic.GroundedLaplacian
open scoped BigOperators Classical

variable {V E : Type*}

/-- Extend a vector on the free vertices by the prescribed zero at the root. -/
noncomputable def extend (root : V) (f : {v : V // v ≠ root} → ℝ) : V → ℝ :=
  fun v => if h : v = root then 0 else f ⟨v, h⟩

theorem extend_root (root : V) (f : {v : V // v ≠ root} → ℝ) :
    extend root f root = 0 := by
  classical
  simp [extend]

theorem extend_free (root : V) (f : {v : V // v ≠ root} → ℝ)
    (v : {v : V // v ≠ root}) : extend root f v = f v := by
  classical
  simp [extend, v.property]

theorem extend_injective (root : V) : Function.Injective (extend root) := by
  intro f g h
  funext v
  simpa only [extend_free] using congrFun h v

theorem extend_zero (root : V) : extend root 0 = 0 := by
  classical
  funext v
  simp [extend]

theorem extend_restrict (root : V) (f : V → ℝ) (hf : f root = 0) :
    extend root (fun v => f v) = f := by
  classical
  funext v
  by_cases hv : v = root
  · subst v
    simp [extend_root, hf]
  · simp [extend, hv]

/-- Deleting the root does not change a finite sum whose root term is zero. -/
theorem sum_free [Fintype V] (root : V) (f : V → ℝ) (hf : f root = 0) :
    (∑ v : {v : V // v ≠ root}, f v) = ∑ v, f v := by
  classical
  have h := Fintype.sum_subtype_add_sum_subtype (fun v : V => v ≠ root) f
  have hz : (∑ v : {v : V // ¬ v ≠ root}, f v) = 0 := by
    apply Finset.sum_eq_zero
    intro v _
    have hv : (v : V) = root := not_ne_iff.mp v.property
    simpa [hv] using hf
  simpa only [hz, add_zero] using h

/-- The principal submatrix of the actual `Bᵀ W B` graph Laplacian. -/
noncomputable def reducedMatrix [Fintype E]
    (src dst : E → V) (w : E → ℝ) (root : V) :
    Matrix {v : V // v ≠ root} {v : V // v ≠ root} ℝ :=
  fun u v => WeightedGraph.laplacian src dst w u v

theorem reducedMatrix_symm [Fintype E]
    (src dst : E → V) (w : E → ℝ) (root : V)
    (u v : {v : V // v ≠ root}) :
    reducedMatrix src dst w root u v = reducedMatrix src dst w root v u :=
  WeightedGraph.laplacian_symm src dst w u v

/-- Multiplication by the reduced matrix, as an actual real linear map. -/
noncomputable def reducedOperator [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (root : V) :
    ({v : V // v ≠ root} → ℝ) →ₗ[ℝ] ({v : V // v ≠ root} → ℝ) := by
  classical
  exact (reducedMatrix src dst w root).mulVecLin

theorem reducedOperator_apply [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (root : V)
    (f : {v : V // v ≠ root} → ℝ) (u : {v : V // v ≠ root}) :
    reducedOperator src dst w root f u =
      ∑ v, WeightedGraph.laplacian src dst w u v * extend root f v := by
  classical
  change (∑ v : {v : V // v ≠ root},
    WeightedGraph.laplacian src dst w u v * f v) = _
  rw [← sum_free root (fun v =>
    WeightedGraph.laplacian src dst w u v * extend root f v)]
  · simp only [extend_free]
  · simp only [extend_root, mul_zero]

/-- The reduced bilinear form is exactly the original edge form after zero
extension; no boundary term is discarded from a nonzero coordinate. -/
theorem reduced_bilinear [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (root : V)
    (f g : {v : V // v ≠ root} → ℝ) :
    (∑ u, f u * reducedOperator src dst w root g u) =
      WeightedGraph.form src dst w (extend root f) (extend root g) := by
  classical
  rw [← WeightedGraph.laplacian_form]
  rw [← sum_free root (fun u => ∑ v,
    extend root f u * WeightedGraph.laplacian src dst w u v * extend root g v)]
  · apply Finset.sum_congr rfl
    intro u _
    rw [reducedOperator_apply, Finset.mul_sum]
    simp only [extend_free, mul_assoc]
  · simp only [extend_root, zero_mul, Finset.sum_const_zero]

theorem reduced_quadratic [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (root : V)
    (f : {v : V // v ≠ root} → ℝ) :
    (∑ u, f u * reducedOperator src dst w root f u) =
      WeightedGraph.energy src dst w (extend root f) := by
  rw [reduced_bilinear, WeightedGraph.energy_eq_form_self]

/-- Strict positivity comes from the actual connected positive support. -/
theorem reduced_quadratic_pos [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V)
    (f : {v : V // v ≠ root} → ℝ) (hf : f ≠ 0) :
    0 < ∑ u, f u * reducedOperator src dst w root f u := by
  rw [reduced_quadratic]
  apply WeightedGraph.grounded_energy_pos src dst w hw hc root _ (extend_root root f)
  intro h
  exact hf (extend_injective root (h.trans (extend_zero root).symm))

theorem reducedOperator_eq_zero_iff [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V)
    (f : {v : V // v ≠ root} → ℝ) :
    reducedOperator src dst w root f = 0 ↔ f = 0 := by
  constructor
  · intro h
    by_contra hf
    have hp := reduced_quadratic_pos src dst w hw hc root f hf
    simp [h] at hp
  · intro h
    simp [h]

theorem reducedOperator_injective [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V) :
    Function.Injective (reducedOperator src dst w root) := by
  intro f g h
  have hz : reducedOperator src dst w root (f - g) = 0 := by
    rw [map_sub, h, sub_self]
  exact sub_eq_zero.mp ((reducedOperator_eq_zero_iff src dst w hw hc root _).mp hz)

/-- Finite dimensionality turns the proved injectivity into bijectivity. -/
theorem reducedOperator_bijective [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V) :
    Function.Bijective (reducedOperator src dst w root) := by
  classical
  have hi := reducedOperator_injective src dst w hw hc root
  exact ⟨hi, LinearMap.injective_iff_surjective.mp hi⟩

/-- The inverse is constructed only after nondegeneracy has been proved. -/
noncomputable def reducedEquiv [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V) :
    ({v : V // v ≠ root} → ℝ) ≃ₗ[ℝ] ({v : V // v ≠ root} → ℝ) :=
  LinearEquiv.ofBijective (reducedOperator src dst w root)
    (reducedOperator_bijective src dst w hw hc root)

theorem reducedEquiv_apply [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V)
    (f : {v : V // v ≠ root} → ℝ) :
    reducedEquiv src dst w hw hc root f = reducedOperator src dst w root f := rfl

theorem exists_unique_reduced_solution [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V)
    (b : {v : V // v ≠ root} → ℝ) :
    ∃! f, reducedOperator src dst w root f = b := by
  let e := reducedEquiv src dst w hw hc root
  refine ⟨e.symm b, e.apply_symm_apply b, ?_⟩
  intro f hf
  exact (reducedOperator_injective src dst w hw hc root)
    (hf.trans (e.apply_symm_apply b).symm)

/-- The determinant is nonzero, including the empty reduced matrix. -/
theorem reducedMatrix_det_ne_zero [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V) :
    (reducedMatrix src dst w root).det ≠ 0 := by
  have hi : Function.Injective (reducedMatrix src dst w root).mulVec :=
    reducedOperator_injective src dst w hw hc root
  exact isUnit_iff_ne_zero.mp
    ((Matrix.isUnit_iff_isUnit_det _).mp
      (Matrix.mulVec_injective_iff_isUnit.mp hi))

/-- Solve the original vertex equations at every free vertex, with one
grounding condition. The equation at the root is deliberately not imposed:
it records the reaction to grounding. -/
theorem exists_unique_grounded_solution [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V) (b : V → ℝ) :
    ∃! f : V → ℝ, f root = 0 ∧ ∀ u, u ≠ root →
      (∑ v, WeightedGraph.laplacian src dst w u v * f v) = b u := by
  obtain ⟨g, hg, hu⟩ := exists_unique_reduced_solution src dst w hw hc root
    (fun v => b v)
  refine ⟨extend root g, ⟨extend_root root g, ?_⟩, ?_⟩
  · intro u hroot
    simpa only [reducedOperator_apply] using congrFun hg ⟨u, hroot⟩
  · intro f hf
    have hr : reducedOperator src dst w root (fun v => f v) =
        (fun v : {v : V // v ≠ root} => b v) := by
      funext u
      rw [reducedOperator_apply, extend_restrict root f hf.1]
      exact hf.2 u u.property
    calc
      f = extend root (fun v => f v) := (extend_restrict root f hf.1).symm
      _ = extend root g := congrArg (extend root) (hu _ hr)

end VolumeLogic.GroundedLaplacian
