import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Complex.Basic

set_option autoImplicit false

/-!
The algebraic step in the stationary-Hessian formula of manuscript
Proposition `prop:stationary-schur`. Here `A` is the internal Hessian,
`B` the internal/external block, and `Y` the derivative of an already
supplied stationary family. Invertibility solves `A * Y + B = 0`;
substitution gives the Schur complement.

These are identities for actual complex matrices. The holomorphic
implicit-function theorem, differentiation of stationarity, and the
chain rule supplying these blocks remain written inputs. No existence
of a stationary family, positivity, or geometric-volume claim is made.
-/

namespace VolumeLogic.StationaryElimination

variable {ι τ : Type*} [Fintype ι] [DecidableEq ι]

/-- The bilinear complex Hessian uses transpose, not conjugate transpose. -/
noncomputable def schur (A : Matrix ι ι ℂ) (B : Matrix ι τ ℂ)
    (C : Matrix τ τ ℂ) : Matrix τ τ ℂ :=
  C - B.transpose * A⁻¹ * B

/-- Solve the linearized stationarity equation with the actual matrix inverse. -/
theorem solve_linearized {A : Matrix ι ι ℂ} {B Y : Matrix ι τ ℂ}
    (hA : IsUnit A.det) (h : A * Y + B = 0) :
    Y = -(A⁻¹ * B) := by
  have hAY : A * Y = -B := eq_neg_iff_add_eq_zero.mpr h
  calc
    Y = A⁻¹ * (A * Y) := (Matrix.nonsing_inv_mul_cancel_left A Y hA).symm
    _ = A⁻¹ * (-B) := by rw [hAY]
    _ = -(A⁻¹ * B) := Matrix.mul_neg _ _

/-- The solution is both necessary and sufficient; no extra solution is selected. -/
theorem linearized_iff {A : Matrix ι ι ℂ} {B Y : Matrix ι τ ℂ}
    (hA : IsUnit A.det) :
    A * Y + B = 0 ↔ Y = -(A⁻¹ * B) := by
  constructor
  · exact solve_linearized hA
  · rintro rfl
    rw [Matrix.mul_neg, Matrix.mul_nonsing_inv_cancel_left A B hA]
    exact neg_add_cancel B

/-- Substitution into the external derivative block before using Hessian symmetry. -/
theorem effective_block {A : Matrix ι ι ℂ} {B Y : Matrix ι τ ℂ}
    (D : Matrix τ ι ℂ) (C : Matrix τ τ ℂ)
    (hA : IsUnit A.det) (h : A * Y + B = 0) :
    C + D * Y = C - D * A⁻¹ * B := by
  rw [solve_linearized hA h, Matrix.mul_neg]
  simp only [sub_eq_add_neg, Matrix.mul_assoc]

/-- With symmetric Hessian blocks, the effective Hessian is the Schur complement. -/
theorem effective_hessian {A : Matrix ι ι ℂ} {B Y : Matrix ι τ ℂ}
    (C : Matrix τ τ ℂ) (hA : IsUnit A.det) (h : A * Y + B = 0) :
    C + B.transpose * Y = schur A B C :=
  effective_block B.transpose C hA h

/-- A vanishing mixed block leaves the external Hessian unchanged. -/
theorem schur_zero_mixed (A : Matrix ι ι ℂ) (C : Matrix τ τ ℂ) :
    schur A (0 : Matrix ι τ ℂ) C = C := by
  simp [schur]

end VolumeLogic.StationaryElimination
