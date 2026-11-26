import RealTransfer
import CoefficientGram
import StationaryElimination
import FourierHermite
import ConwayAssembly

/-!
Expected-type contracts for the analysis modules.

Each example spells out the mathematical proposition used in the reference.
The examples verify the interface to the selected proof roots, not the
written knot identities, contour arguments, differentiations, or geometry.
The full symbol dictionary and the boundary of each correspondence are in
`formal/correspondence/analysis.json`.
-/

set_option autoImplicit false
noncomputable section
open Filter
open scoped BigOperators InnerProductSpace ComplexConjugate

namespace VolumeLogic.AnalysisContracts

section ScalarTransfer

-- manuscript-contract: VolumeLogic.RealModel.complex_packet_volume_transfer
example {K u aN SN E : ℕ → ℂ} {a S : ℂ} {b V ρ : ℝ}
    (identity : ∀ᶠ N in atTop,
      K N = u N * ((((N : ℝ) ^ ρ : ℝ) : ℂ) *
        (aN N * Complex.exp ((N : ℂ) * SN N)) + E N))
    (phase : ∀ᶠ N in atTop, ‖u N‖ = 1)
    (amplitude : Tendsto aN atTop (nhds a)) (nonzero : a ≠ 0)
    (action : Tendsto SN atTop (nhds S))
    (error : ∀ ε > 0, ∀ᶠ N in atTop,
      ‖E N‖ ≤ Real.exp ((N : ℝ) * (b + ε)))
    (gap : b < S.re) (volume_identity : 2 * Real.pi * S.re = V) :
    (∀ᶠ N in atTop, K N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖K N‖ / (N : ℝ)) atTop (nhds S.re) ∧
      Tendsto (fun N => 2 * Real.pi * Real.log ‖K N‖ / (N : ℝ))
        atTop (nhds V) := by
  exact RealModel.complex_packet_volume_transfer ρ identity phase amplitude nonzero
    action ⟨Eventually.of_forall (fun _ => norm_nonneg _), error⟩ gap volume_identity

-- manuscript-contract: VolumeLogic.RealModel.upperRate_norm_of_cost
example {E : ℕ → ℂ} {B C : ℕ → ℝ} {b : ℝ}
    (B_nonnegative : ∀ᶠ N in atTop, 0 ≤ B N)
    (C_nonnegative : ∀ᶠ N in atTop, 0 ≤ C N)
    (B_rate : ∀ ε > 0, ∀ᶠ N in atTop,
      B N ≤ Real.exp ((N : ℝ) * (b + ε)))
    (C_rate : ∀ ε > 0, ∀ᶠ N in atTop,
      C N ≤ Real.exp ((N : ℝ) * ε))
    (bound : ∀ᶠ N in atTop, ‖E N‖ ≤ C N * B N) :
    (∀ᶠ N in atTop, 0 ≤ ‖E N‖) ∧
      ∀ ε > 0, ∀ᶠ N in atTop,
        ‖E N‖ ≤ Real.exp ((N : ℝ) * (b + ε)) := by
  exact RealModel.upperRate_norm_of_cost ⟨B_nonnegative, B_rate⟩
    ⟨C_nonnegative, by simpa only [zero_add] using C_rate⟩ bound

-- manuscript-contract: VolumeLogic.RealModel.upperRate_of_polynomial_bound
example {C : ℕ → ℝ} {C₀ m : ℝ} (prefactor : 0 ≤ C₀)
    (polynomial_bound : ∀ᶠ N in atTop,
      0 ≤ C N ∧ C N ≤ C₀ * (N : ℝ) ^ m) :
    (∀ᶠ N in atTop, 0 ≤ C N) ∧
      ∀ ε > 0, ∀ᶠ N in atTop, C N ≤ Real.exp ((N : ℝ) * ε) := by
  simpa only [RealModel.UpperRate, zero_add] using
    RealModel.upperRate_of_polynomial_bound prefactor polynomial_bound

end ScalarTransfer

section CoefficientPairing
variable {ι κ η E F G : Type*}
variable [Fintype ι] [Fintype κ] [Fintype η]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
variable [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
variable [NormedAddCommGroup G] [InnerProductSpace ℂ G] [CompleteSpace G]

-- manuscript-contract: VolumeLogic.CoefficientGram.quadratic_eq_norm_sq
example (v : ι → E) (c : EuclideanSpace ℂ ι) :
    ⟪c, CoefficientGram.gram (CoefficientGram.synthesis v) c⟫_ℂ =
      (‖∑ i, c i • v i‖ : ℂ) ^ 2 := by
  simpa only [CoefficientGram.synthesis_apply] using
    CoefficientGram.quadratic_eq_norm_sq (CoefficientGram.synthesis v) c

-- manuscript-contract: VolumeLogic.CoefficientGram.ker_gram
example (B : EuclideanSpace ℂ ι →L[ℂ] E) :
    (B.adjoint ∘L B).ker = B.ker := by
  exact CoefficientGram.ker_gram B

-- manuscript-contract: VolumeLogic.CoefficientGram.coordinate_change
example (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (S : EuclideanSpace ℂ κ →L[ℂ] EuclideanSpace ℂ ι) :
    (B ∘L S).adjoint ∘L (B ∘L S) =
      S.adjoint ∘L (B.adjoint ∘L B) ∘L S := by
  exact CoefficientGram.coordinate_change B S

-- manuscript-contract: VolumeLogic.CoefficientGram.closing_bound
example (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (ℓ : E →L[ℂ] ℂ) (c : EuclideanSpace ℂ ι) :
    ‖ℓ (B c)‖ ≤ ‖ℓ‖ * Real.sqrt (Complex.re ⟪c, (B.adjoint ∘L B) c⟫_ℂ) := by
  exact CoefficientGram.closing_bound B ℓ c

-- manuscript-contract: VolumeLogic.CoefficientGram.corridor_comp
example (T₁ : E →L[ℂ] F) (T₂ : F →L[ℂ] G)
    (B₀ : EuclideanSpace ℂ ι →L[ℂ] E)
    (B₁ : EuclideanSpace ℂ κ →L[ℂ] F)
    (B₂ : EuclideanSpace ℂ η →L[ℂ] G)
    (A₁ : EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ κ)
    (A₂ : EuclideanSpace ℂ κ →L[ℂ] EuclideanSpace ℂ η)
    (first_piece : T₁ ∘L B₀ = B₁ ∘L A₁)
    (second_piece : T₂ ∘L B₁ = B₂ ∘L A₂) :
    (T₂ ∘L T₁) ∘L B₀ = B₂ ∘L (A₂ ∘L A₁) := by
  exact CoefficientGram.corridor_comp T₁ T₂ B₀ B₁ B₂ A₁ A₂ first_piece second_piece

-- manuscript-contract: VolumeLogic.CoefficientGram.corridor_preserves_zero
example (T : E →L[ℂ] F)
    (B₀ : EuclideanSpace ℂ ι →L[ℂ] E)
    (B₁ : EuclideanSpace ℂ κ →L[ℂ] F)
    (A : EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ κ)
    (coordinate_identity : T ∘L B₀ = B₁ ∘L A)
    (c : EuclideanSpace ℂ ι) (physically_zero : B₀ c = 0) :
    B₁ (A c) = 0 := by
  exact CoefficientGram.corridor_preserves_zero T B₀ B₁ A coordinate_identity c
    physically_zero

end CoefficientPairing

section StationaryBlocks
variable {ι τ : Type*} [Fintype ι] [DecidableEq ι]

-- manuscript-contract: VolumeLogic.StationaryElimination.solve_linearized
example {A : Matrix ι ι ℂ} {B Y : Matrix ι τ ℂ}
    (internal_nondegenerate : IsUnit A.det) (differentiated_stationarity : A * Y + B = 0) :
    Y = -(A⁻¹ * B) := by
  exact StationaryElimination.solve_linearized internal_nondegenerate
    differentiated_stationarity

-- manuscript-contract: VolumeLogic.StationaryElimination.effective_hessian
example {A : Matrix ι ι ℂ} {B Y : Matrix ι τ ℂ}
    (D : Matrix τ ι ℂ) (C : Matrix τ τ ℂ)
    (internal_nondegenerate : IsUnit A.det) (differentiated_stationarity : A * Y + B = 0)
    (mixed_symmetry : D = B.transpose) :
    C + D * Y = C - D * A⁻¹ * B := by
  subst D
  exact StationaryElimination.effective_hessian C internal_nondegenerate
    differentiated_stationarity

-- manuscript-contract: VolumeLogic.StationaryElimination.schur_zero_mixed
example (A : Matrix ι ι ℂ) (C : Matrix τ τ ℂ) :
    C - (0 : Matrix ι τ ℂ).transpose * A⁻¹ * (0 : Matrix ι τ ℂ) = C := by
  exact StationaryElimination.schur_zero_mixed A C

end StationaryBlocks

section ShiftedFourier

-- manuscript-contract: VolumeLogic.FourierHermite.shiftedDFT_eq_sum
example {N : ℕ} (level : 2 ≤ N) (α : ℝ) (f : Fin N → ℂ) (a : Fin N) :
    letI : NeZero N := ⟨by omega⟩
    FourierHermite.shiftedDFT α f a = (N : ℂ)⁻¹ * ∑ k : Fin N,
      Complex.exp (((-2 * Real.pi * ((k.val : ℝ) + α) * (a.val : ℝ) /
        (N : ℝ) : ℝ) : ℂ) * Complex.I) * f k := by
  letI : NeZero N := ⟨by omega⟩
  exact FourierHermite.shiftedDFT_eq_sum α f a

-- manuscript-contract: VolumeLogic.FourierHermite.shifted_reconstruction
example {N : ℕ} (level : 2 ≤ N) (α : ℝ) (f : Fin N → ℂ) (k : Fin N) :
    letI : NeZero N := ⟨by omega⟩
    (∑ a : Fin N, FourierHermite.shiftedDFT α f a *
      Complex.exp (((2 * Real.pi * ((k.val : ℝ) + α) * (a.val : ℝ) /
        (N : ℝ) : ℝ) : ℂ) * Complex.I)) = f k := by
  letI : NeZero N := ⟨by omega⟩
  exact FourierHermite.shifted_reconstruction α f k

-- manuscript-contract: VolumeLogic.FourierHermite.shifted_parseval
example {N : ℕ} (level : 2 ≤ N) (α : ℝ) (f : Fin N → ℂ) :
    letI : NeZero N := ⟨by omega⟩
    (∑ a : Fin N, ‖FourierHermite.shiftedDFT α f a‖ ^ 2) =
      (∑ k : Fin N, ‖f k‖ ^ 2) / (N : ℝ) := by
  letI : NeZero N := ⟨by omega⟩
  exact FourierHermite.shifted_parseval α f

-- manuscript-contract: VolumeLogic.FourierHermite.centered_variance
example {N : ℕ} (_level : 2 ≤ N) :
    (∑ k : Fin N, ((k.val : ℝ) - ((N : ℝ) - 1) / 2) ^ 2) =
      (N : ℝ) * ((N : ℝ) ^ 2 - 1) / 12 := by
  exact FourierHermite.centered_variance N

-- manuscript-contract: VolumeLogic.FourierHermite.hermite_coefficient_mass
example {N : ℕ} (level : 2 ≤ N) (α : ℝ) (n : ℤ)
    (h : Fin N → ℂ) (unit_values : ∀ k, ‖h k‖ = 1) :
    letI : NeZero N := ⟨by omega⟩
    (∑ j, ‖FourierHermite.circleCoefficients
      (FourierHermite.hermiteCoefficients (FourierHermite.shiftedDFT α h)
        (FourierHermite.shiftedDFT α
          (fun k => (((n : ℝ) * ((k.val : ℝ) - ((N : ℝ) - 1) / 2) : ℝ) : ℂ) * h k))) j‖) ≤
      2 * Real.sqrt N * (1 + |(n : ℝ)| / Real.sqrt 12) := by
  letI : NeZero N := ⟨by omega⟩
  exact FourierHermite.hermite_coefficient_mass level α n h unit_values

-- manuscript-contract: VolumeLogic.FourierHermite.crossing_coefficient_mass
example {N : ℕ} (level : 3 ≤ N) (n : ℤ) :
    letI : NeZero N := ⟨by omega⟩
    (∑ j, ‖FourierHermite.crossingCoefficients (N := N) n j‖) ≤
      2 * Real.sqrt N * (1 + |(n : ℝ)| / Real.sqrt 12) := by
  letI : NeZero N := ⟨by omega⟩
  exact FourierHermite.crossing_coefficient_mass (by omega : 2 ≤ N) n

end ShiftedFourier

section ConwayContraction

-- manuscript-contract: VolumeLogic.ConwayAssembly.fullColorContraction_norm_le
example {N r : ℕ} (β : Fin r → Fin N → ℂ)
    (D : (Fin r → Fin N) → ℂ) (B : ℝ) (source_bound : ∀ j, ‖D j‖ ≤ B) :
    ‖∑ j : Fin r → Fin N, (∏ ℓ, β ℓ (j ℓ)) * D j‖ ≤
      B * ∏ ℓ, ∑ k, ‖β ℓ k‖ := by
  simpa only [ConwayAssembly.fullColorContraction, mul_comm B] using
    ConwayAssembly.fullColorContraction_norm_le β D B source_bound

-- manuscript-contract: VolumeLogic.ConwayAssembly.conway_packet_volume_limit
example {r : ℕ} {K u aN : ℕ → ℂ}
    (β : (N : ℕ) → Fin r → Fin N → ℂ)
    (D : (N : ℕ) → (Fin r → Fin N) → ℂ)
    (n : Fin r → ℤ) (B : ℕ → ℝ) {a S : ℂ} {b V : ℝ}
    (coefficient_identity : ∀ (N : ℕ) [NeZero N], 3 ≤ N → ∀ ℓ,
      β N ℓ = FourierHermite.crossingCoefficients (n ℓ))
    (source_identity : ∀ᶠ N in atTop,
      K N = u N * ((((N : ℝ) ^ (3 / 2 : ℝ) : ℝ) : ℂ) *
        (aN N * Complex.exp ((N : ℂ) * S)) +
          ∑ j : Fin r → Fin N, (∏ ℓ, β N ℓ (j ℓ)) * D N j))
    (source_bound : ∀ᶠ N in atTop, ∀ j, ‖D N j‖ ≤ B N)
    (B_nonnegative : ∀ᶠ N in atTop, 0 ≤ B N)
    (source_rate : ∀ ε > 0, ∀ᶠ N in atTop,
      B N ≤ Real.exp ((N : ℝ) * (b + ε)))
    (phase : ∀ᶠ N in atTop, ‖u N‖ = 1)
    (amplitude : Tendsto aN atTop (nhds a)) (nonzero : a ≠ 0)
    (gap : b < S.re) (volume_identity : 2 * Real.pi * S.re = V) :
    (∀ᶠ N in atTop, K N ≠ 0) ∧
      Tendsto (fun N => Real.log ‖K N‖ / (N : ℝ)) atTop (nhds S.re) ∧
      Tendsto (fun N => 2 * Real.pi * Real.log ‖K N‖ / (N : ℝ))
        atTop (nhds V) := by
  exact ConwayAssembly.conway_packet_volume_limit β D n B (3 / 2) coefficient_identity
    source_identity source_bound ⟨B_nonnegative, source_rate⟩ phase amplitude nonzero
    tendsto_const_nhds gap volume_identity

end ConwayContraction
end VolumeLogic.AnalysisContracts
