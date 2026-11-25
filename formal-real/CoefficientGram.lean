import Mathlib.Analysis.InnerProductSpace.Adjoint

set_option autoImplicit false

/-!
The actual coefficient pairing in manuscript Proposition
`prop:coefficient-gram`. Finite coefficient vectors use
`EuclideanSpace ℂ ι`, whose norm is the l² norm, rather than the sup norm
on an unadorned function space. The synthesis map retains arbitrary,
possibly dependent spanning vectors.

The Gram operator is the actual Hilbert-space adjoint product. Its
nullspace is exactly the nullspace of synthesis. Coordinate changes
and composition of exact linear corridors keep these maps, their
pairings, and physically zero directions. The closing estimate is
only an upper bound; none of these facts proves a scalar lower bound.
-/

namespace VolumeLogic.CoefficientGram

open scoped InnerProductSpace ComplexConjugate BigOperators

variable {ι κ η E F G : Type*}
variable [Fintype ι] [Fintype κ] [Fintype η]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E]
variable [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
variable [NormedAddCommGroup G] [InnerProductSpace ℂ G] [CompleteSpace G]

/-- The finite coefficient map `c ↦ ∑ i, c i • v i`, with the l² domain. -/
noncomputable def synthesis (v : ι → E) : EuclideanSpace ℂ ι →L[ℂ] E :=
  ∑ i, (EuclideanSpace.proj i).smulRight (v i)

theorem synthesis_apply (v : ι → E) (c : EuclideanSpace ℂ ι) :
    synthesis v c = ∑ i, c i • v i := by
  simp [synthesis]

variable [CompleteSpace E]

/-- The transported pairing is `B† B`, with no orthonormality assumption. -/
noncomputable def gram (B : EuclideanSpace ℂ ι →L[ℂ] E) :
    EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ ι :=
  B.adjoint ∘L B

theorem inner_pullback (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (c d : EuclideanSpace ℂ ι) :
    ⟪B c, B d⟫_ℂ = ⟪c, gram B d⟫_ℂ :=
  (ContinuousLinearMap.adjoint_inner_right B c (B d)).symm

/-- The complex quadratic value itself is the real squared physical norm. -/
theorem quadratic_eq_norm_sq (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (c : EuclideanSpace ℂ ι) :
    ⟪c, gram B c⟫_ℂ = (‖B c‖ : ℂ) ^ 2 := by
  rw [← inner_pullback]
  exact inner_self_eq_norm_sq_to_K (𝕜 := ℂ) (B c)

theorem norm_sq_pullback (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (c : EuclideanSpace ℂ ι) :
    ‖B c‖ ^ 2 = Complex.re ⟪c, gram B c⟫_ℂ :=
  ContinuousLinearMap.apply_norm_sq_eq_inner_adjoint_right B c

theorem norm_pullback (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (c : EuclideanSpace ℂ ι) :
    ‖B c‖ = Real.sqrt (Complex.re ⟪c, gram B c⟫_ℂ) :=
  ContinuousLinearMap.apply_norm_eq_sqrt_inner_adjoint_right B c

theorem quadratic_nonneg (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (c : EuclideanSpace ℂ ι) :
    0 ≤ Complex.re ⟪c, gram B c⟫_ℂ := by
  rw [← norm_sq_pullback]
  exact sq_nonneg _

/-- Thus the transported form has no null directions beyond physically zero vectors. -/
theorem ker_gram (B : EuclideanSpace ℂ ι →L[ℂ] E) :
    (gram B).ker = B.ker :=
  ContinuousLinearMap.ker_adjoint_comp_self B

theorem quadratic_pos_iff (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (c : EuclideanSpace ℂ ι) :
    0 < Complex.re ⟪c, gram B c⟫_ℂ ↔ B c ≠ 0 := by
  rw [← inner_pullback]
  exact re_inner_self_pos (𝕜 := ℂ) (x := B c)

/-- The pairing is independent of representatives modulo the synthesis kernel. -/
theorem pairing_descends (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (c d u v : EuclideanSpace ℂ ι) (hu : B u = 0) (hv : B v = 0) :
    ⟪c + u, gram B (d + v)⟫_ℂ = ⟪c, gram B d⟫_ℂ := by
  rw [← inner_pullback, ← inner_pullback]
  simp [map_add, hu, hv]

/-- In the standard coefficient basis, the entries are the usual Gram entries. -/
theorem synthesis_gram_entry [DecidableEq ι] (v : ι → E) (i j : ι) :
    ⟪EuclideanSpace.single i (1 : ℂ),
      gram (synthesis v) (EuclideanSpace.single j (1 : ℂ))⟫_ℂ =
      ⟪v i, v j⟫_ℂ := by
  rw [← inner_pullback]
  simp [synthesis_apply, PiLp.single_apply]

/-- Substitution `c = S d` transports the entire Gram, including cross terms. -/
theorem coordinate_change (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (S : EuclideanSpace ℂ κ →L[ℂ] EuclideanSpace ℂ ι) :
    gram (B ∘L S) = S.adjoint ∘L gram B ∘L S := by
  simp only [gram, ContinuousLinearMap.adjoint_comp, ContinuousLinearMap.comp_assoc]

/-- The original closing row must still be applied after synthesis. -/
theorem closing_bound (B : EuclideanSpace ℂ ι →L[ℂ] E)
    (ℓ : E →L[ℂ] ℂ) (c : EuclideanSpace ℂ ι) :
    ‖ℓ (B c)‖ ≤ ‖ℓ‖ * Real.sqrt (Complex.re ⟪c, gram B c⟫_ℂ) := by
  rw [← norm_pullback]
  exact ℓ.le_opNorm (B c)

omit [Fintype ι] [Fintype κ] [Fintype η]
  [CompleteSpace E] [CompleteSpace F] [CompleteSpace G] in
/-- Exact coordinate relations are closed under composition of linear corridors. -/
theorem corridor_comp
    (T₁ : E →L[ℂ] F) (T₂ : F →L[ℂ] G)
    (B₀ : EuclideanSpace ℂ ι →L[ℂ] E)
    (B₁ : EuclideanSpace ℂ κ →L[ℂ] F)
    (B₂ : EuclideanSpace ℂ η →L[ℂ] G)
    (A₁ : EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ κ)
    (A₂ : EuclideanSpace ℂ κ →L[ℂ] EuclideanSpace ℂ η)
    (h₁ : T₁ ∘L B₀ = B₁ ∘L A₁) (h₂ : T₂ ∘L B₁ = B₂ ∘L A₂) :
    (T₂ ∘L T₁) ∘L B₀ = B₂ ∘L (A₂ ∘L A₁) := by
  rw [ContinuousLinearMap.comp_assoc, h₁, ← ContinuousLinearMap.comp_assoc,
    h₂, ContinuousLinearMap.comp_assoc]

omit [Fintype ι] [Fintype κ] [CompleteSpace E] [CompleteSpace F] in
/-- A physically zero incoming coefficient direction remains zero after a corridor. -/
theorem corridor_preserves_zero
    (T : E →L[ℂ] F) (B₀ : EuclideanSpace ℂ ι →L[ℂ] E)
    (B₁ : EuclideanSpace ℂ κ →L[ℂ] F)
    (A : EuclideanSpace ℂ ι →L[ℂ] EuclideanSpace ℂ κ)
    (h : T ∘L B₀ = B₁ ∘L A) (c : EuclideanSpace ℂ ι)
    (hc : B₀ c = 0) : B₁ (A c) = 0 := by
  have h' := congrArg (fun f => f c) h
  simpa only [ContinuousLinearMap.comp_apply, hc, map_zero] using h'.symm

end VolumeLogic.CoefficientGram
