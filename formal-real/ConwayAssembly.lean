import RealTransfer
import FourierHermite
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Positivity

/-!
The finite full-color contraction in the strict Conway filling proof.
The original closing identity is retained as a coherent sum. Triangle
inequalities are applied only after that identity, and the cost is derived
from the actual value/normal Fourier--Hermite coefficients.

The final theorem connects this bound to the reference's complex packet theorem.
The source envelope, nonzero packet coefficient, finite critical action and
geometric calibration remain the explicit written-mathematics inputs.
-/

namespace VolumeLogic.ConwayAssembly
open Filter
open scoped BigOperators
open VolumeLogic.RealModel

/-- The entire shared-color remainder after the original linear closing.
No absolute value or independent choice of a color is inserted in the sum. -/
def fullColorContraction {N r : ℕ}
    (β : Fin r → Fin N → ℂ) (D : (Fin r → Fin N) → ℂ) : ℂ :=
  ∑ j : Fin r → Fin N, (∏ ℓ, β ℓ (j ℓ)) * D j

/-- The finite contraction bound, before any exponential-rate argument.
The same source budget bounds every full color tuple. -/
theorem fullColorContraction_norm_le {N r : ℕ}
    (β : Fin r → Fin N → ℂ) (D : (Fin r → Fin N) → ℂ) (B : ℝ)
    (sourceBound : ∀ j, ‖D j‖ ≤ B) :
    ‖fullColorContraction β D‖ ≤ (∏ ℓ, ∑ k, ‖β ℓ k‖) * B := by
  classical
  unfold fullColorContraction
  calc
    ‖∑ j : Fin r → Fin N, (∏ ℓ, β ℓ (j ℓ)) * D j‖ ≤
        ∑ j : Fin r → Fin N, ‖(∏ ℓ, β ℓ (j ℓ)) * D j‖ :=
      norm_sum_le _ _
    _ ≤ ∑ j : Fin r → Fin N, (∏ ℓ, ‖β ℓ (j ℓ)‖) * B := by
      apply Finset.sum_le_sum
      intro j _
      rw [norm_mul, norm_prod]
      exact mul_le_mul_of_nonneg_left (sourceBound j)
        (Finset.prod_nonneg fun ℓ _ => norm_nonneg _)
    _ = (∏ ℓ, ∑ k, ‖β ℓ k‖) * B := by
      rw [← Finset.sum_mul]
      congr 1
      exact (Fintype.prod_sum (κ := fun _ : Fin r => Fin N)
        (fun ℓ k => ‖β ℓ k‖)).symm

private theorem upperRate_prod_zero {ι : Type*} (s : Finset ι)
    (f : ι → ℕ → ℝ)
    (hf : ∀ i ∈ s, UpperRate (f i) 0) :
    UpperRate (fun N => ∏ i ∈ s, f i N) 0 := by
  classical
  revert hf
  induction s using Finset.induction_on with
  | empty =>
    intro _
    simpa using upperRate_of_polynomial_bound (C := fun _ => (1 : ℝ))
      (C₀ := 1) (m := 0) (by norm_num)
      (Eventually.of_forall fun N => by simp)
  | @insert i s hi ih =>
    intro hf
    have hfirst := hf i (Finset.mem_insert_self i s)
    have hrest := ih (fun j hj => hf j (Finset.mem_insert_of_mem hj))
    simpa [Finset.prod_insert, hi] using hfirst.mul hrest

private theorem coefficient_cost_upperRate {r : ℕ}
    (β : (N : ℕ) → Fin r → Fin N → ℂ) (n : Fin r → ℤ)
    (coefficients : ∀ (N : ℕ) [NeZero N], 3 ≤ N → ∀ ℓ,
      β N ℓ = VolumeLogic.FourierHermite.crossingCoefficients (n ℓ)) :
    UpperRate (fun N => ∏ ℓ, ∑ k, ‖β N ℓ k‖) 0 := by
  have hmass : ∀ ℓ : Fin r, UpperRate (fun N => ∑ k, ‖β N ℓ k‖) 0 := by
    intro ℓ
    apply upperRate_of_polynomial_bound
      (C₀ := 2 * (1 + |(n ℓ : ℝ)| / Real.sqrt 12)) (m := 1 / 2)
    · positivity
    · filter_upwards [eventually_ge_atTop (3 : ℕ)] with N hN
      letI : NeZero N := ⟨by omega⟩
      refine ⟨Finset.sum_nonneg fun k _ => norm_nonneg _, ?_⟩
      rw [coefficients N hN ℓ]
      simpa [Real.sqrt_eq_rpow, mul_assoc, mul_left_comm, mul_comm] using
        VolumeLogic.FourierHermite.crossing_coefficient_mass (by omega : 2 ≤ N) (n ℓ)
  simpa using upperRate_prod_zero Finset.univ
    (fun ℓ N => ∑ k, ‖β N ℓ k‖) (fun ℓ _ => hmass ℓ)

/-- The actual strict Conway assembly step.

The source identity keeps the entire original color contraction and marked
closing. The powers n are one fixed integer tuple, and the coefficient
identity uses its actual finite Hermite coefficients. Their subexponential
product cost is proved here, rather than assumed for the filled error.
The source bound is uniform over the full shared-color array.

The packet and geometric inputs concern this same fixed diagram and
filling tuple. No saddle, Parseval identity, or full-source estimate is
replaced by positivity of a norm. -/
theorem conway_packet_volume_limit {r : ℕ}
    {K u amp S : ℕ → ℂ}
    (β : (N : ℕ) → Fin r → Fin N → ℂ)
    (D : (N : ℕ) → (Fin r → Fin N) → ℂ)
    (n : Fin r → ℤ) (B : ℕ → ℝ)
    {a A : ℂ} {b volume : ℝ} (ρ : ℝ)
    (coefficients : ∀ (N : ℕ) [NeZero N], 3 ≤ N → ∀ ℓ,
      β N ℓ = VolumeLogic.FourierHermite.crossingCoefficients (n ℓ))
    (sourceIdentity : ∀ᶠ N in atTop,
      K N = u N * ((((N : ℝ) ^ ρ : ℝ) : ℂ) *
        (amp N * Complex.exp ((N : ℂ) * S N)) +
          fullColorContraction (β N) (D N)))
    (sourceBound : ∀ᶠ N in atTop, ∀ j, ‖D N j‖ ≤ B N)
    (sourceRate : UpperRate B b)
    (unit : ∀ᶠ N in atTop, ‖u N‖ = 1)
    (hamp : Tendsto amp atTop (nhds a)) (ha : a ≠ 0)
    (hS : Tendsto S atTop (nhds A))
    (gap : b < A.re) (geometry : 2 * Real.pi * A.re = volume) :
    (∀ᶠ N in atTop, K N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖K N‖ / (N : ℝ)) atTop (nhds A.re) ∧
      Tendsto (fun N => 2 * Real.pi * Real.log ‖K N‖ / (N : ℝ))
        atTop (nhds volume) := by
  have hcost := coefficient_cost_upperRate β n coefficients
  have hbound : ∀ᶠ N in atTop,
      ‖fullColorContraction (β N) (D N)‖ ≤
        (∏ ℓ, ∑ k, ‖β N ℓ k‖) * B N := by
    filter_upwards [sourceBound] with N hN
    exact fullColorContraction_norm_le (β N) (D N) (B N) hN
  have hremainder := upperRate_norm_of_cost sourceRate hcost hbound
  exact complex_packet_volume_transfer ρ sourceIdentity unit
    hamp ha hS hremainder gap geometry

end VolumeLogic.ConwayAssembly
