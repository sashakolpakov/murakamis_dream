import Mathlib.Analysis.Fourier.ZMod
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Shifted Fourier arrays and the full filling coefficient bound

The Fourier transform uses the actual counting arrays, with the factor
`1 / N` and the phase of the shifted root grid explicit.  Parseval is
proved from Mathlib's finite Fourier inversion, not assumed as a norm
axiom.  The Hermite reconstruction keeps the exceptional coefficient at
zero and omits its normal datum.  Its final two-place shift is truncated,
rather than taken modulo the level.

These are the coefficient estimates of the volume manuscript's exact
operations chapter and Conway filling proof.  They do not construct a
crossing matrix or infer nonvanishing of a closing from a norm bound.
-/

noncomputable section
open scoped BigOperators ComplexConjugate
open Finset

namespace VolumeLogic.FourierHermite

private theorem dft_pairing {N : ℕ} [NeZero N] (f g : ZMod N → ℂ) :
    (∑ k, conj (ZMod.dft f k) * ZMod.dft g k) =
      (N : ℂ) * ∑ j, conj (f j) * g j := by
  classical
  calc
    (∑ k, conj (ZMod.dft f k) * ZMod.dft g k) =
        ∑ k, ∑ j, conj (f j) *
          (ZMod.stdAddChar (j * k) * ZMod.dft g k) := by
      apply sum_congr rfl
      intro k _
      rw [ZMod.dft_apply, map_sum, sum_mul]
      apply sum_congr rfl
      intro j _
      simp only [smul_eq_mul, map_mul]
      rw [← AddChar.map_neg_eq_conj, neg_neg]
      ring
    _ = ∑ j, conj (f j) * ZMod.dft (ZMod.dft g) (-j) := by
      rw [sum_comm]
      apply sum_congr rfl
      intro j _
      rw [ZMod.dft_apply, mul_sum]
      apply sum_congr rfl
      intro k _
      simp only [smul_eq_mul, mul_neg, neg_neg]
      rw [mul_comm k j]
    _ = (N : ℂ) * ∑ j, conj (f j) * g j := by
      simp only [ZMod.dft_dft, neg_neg, smul_eq_mul]
      rw [mul_sum]
      apply sum_congr rfl
      intro j _
      ring

private theorem dft_energy {N : ℕ} [NeZero N] (f : ZMod N → ℂ) :
    (∑ k, ‖ZMod.dft f k‖ ^ 2) = (N : ℝ) * ∑ j, ‖f j‖ ^ 2 := by
  have h := congrArg Complex.re (dft_pairing f f)
  simpa only [Complex.conj_mul', ← Complex.ofReal_pow, ← Complex.ofReal_sum,
    ← Complex.ofReal_natCast, ← Complex.ofReal_mul, Complex.ofReal_re] using h

/-- The output phase for the root grid `(k + α) / N`. -/
def shiftPhase (N : ℕ) (α : ℝ) (a : Fin N) : ℂ :=
  Complex.exp (((-2 * Real.pi * α * (a.val : ℝ) / (N : ℝ) : ℝ) : ℂ) * Complex.I)

@[simp] theorem norm_shiftPhase (N : ℕ) (α : ℝ) (a : Fin N) :
    ‖shiftPhase N α a‖ = 1 := by
  exact Complex.norm_exp_ofReal_mul_I _

/-- The normalized DFT on the actual finite array.  `α = 1/2` is the
midpoint grid used by the filling functional. -/
def shiftedDFT {N : ℕ} [NeZero N] (α : ℝ) (f : Fin N → ℂ) (a : Fin N) : ℂ :=
  shiftPhase N α a * ((N : ℂ)⁻¹ *
    ZMod.dft (f ∘ (ZMod.finEquiv N).symm) (ZMod.finEquiv N a))

private theorem finEquiv_eq_cast {N : ℕ} [NeZero N] (j : Fin N) :
    ZMod.finEquiv N j = (j.val : ZMod N) := by
  apply ZMod.val_injective N
  rw [ZMod.val_cast_of_lt j.isLt]
  cases N with
  | zero => exact Fin.elim0 j
  | succ N => rfl

private theorem character_fin {N : ℕ} [NeZero N] (j a : Fin N) :
    ZMod.stdAddChar (-(ZMod.finEquiv N j * ZMod.finEquiv N a)) =
      Complex.exp (((-2 * Real.pi * (j.val : ℝ) * (a.val : ℝ) /
        (N : ℝ) : ℝ) : ℂ) * Complex.I) := by
  rw [finEquiv_eq_cast, finEquiv_eq_cast]
  let m : ℤ := -((j.val : ℤ) * (a.val : ℤ))
  have he : -((j.val : ZMod N) * (a.val : ZMod N)) = (m : ZMod N) := by
    dsimp [m]
    push_cast
    rfl
  calc
    _ = Complex.exp (2 * Real.pi * Complex.I *
        (m : ℂ) / (N : ℂ)) :=
      (congrArg (fun z : ZMod N => ZMod.stdAddChar z) he).trans
        (ZMod.stdAddChar_coe (N := N) m)
    _ = _ := by
      congr 1
      dsimp [m]
      push_cast
      ring

/-- The bundled definition is exactly the manuscript's sum on the
shifted root grid, with no change of coefficients or normalization. -/
theorem shiftedDFT_eq_sum {N : ℕ} [NeZero N] (α : ℝ)
    (f : Fin N → ℂ) (a : Fin N) :
    shiftedDFT α f a = (N : ℂ)⁻¹ * ∑ k : Fin N,
      Complex.exp (((-2 * Real.pi * ((k.val : ℝ) + α) * (a.val : ℝ) /
        (N : ℝ) : ℝ) : ℂ) * Complex.I) * f k := by
  classical
  have hd : ZMod.dft (f ∘ (ZMod.finEquiv N).symm) (ZMod.finEquiv N a) =
      ∑ k : Fin N, ZMod.stdAddChar
        (-(ZMod.finEquiv N k * ZMod.finEquiv N a)) * f k := by
    rw [ZMod.dft_apply]
    simpa [smul_eq_mul] using
      (Equiv.sum_comp (ZMod.finEquiv N).toEquiv (fun k : ZMod N =>
        ZMod.stdAddChar (-(k * ZMod.finEquiv N a)) *
          f ((ZMod.finEquiv N).symm k))).symm
  rw [shiftedDFT, hd]
  simp only [mul_sum]
  apply sum_congr rfl
  intro k _
  rw [character_fin, shiftPhase]
  have he :
      Complex.exp (((-2 * Real.pi * α * (a.val : ℝ) / (N : ℝ) : ℝ) : ℂ) * Complex.I) *
        Complex.exp (((-2 * Real.pi * (k.val : ℝ) * (a.val : ℝ) /
          (N : ℝ) : ℝ) : ℂ) * Complex.I) =
      Complex.exp (((-2 * Real.pi * ((k.val : ℝ) + α) * (a.val : ℝ) /
        (N : ℝ) : ℝ) : ℂ) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  calc
    _ = (N : ℂ)⁻¹ *
        (Complex.exp (((-2 * Real.pi * α * (a.val : ℝ) / (N : ℝ) : ℝ) : ℂ) * Complex.I) *
          Complex.exp (((-2 * Real.pi * (k.val : ℝ) * (a.val : ℝ) /
            (N : ℝ) : ℝ) : ℂ) * Complex.I)) * f k := by ring
    _ = _ := by rw [he]; ring

/-- Exact reconstruction on the same shifted grid. The positive phase
undoes the coefficient phase, including a nonintegral grid shift. -/
theorem shifted_reconstruction {N : ℕ} [NeZero N] (α : ℝ)
    (f : Fin N → ℂ) (k : Fin N) :
    (∑ a : Fin N, shiftedDFT α f a *
      Complex.exp (((2 * Real.pi * ((k.val : ℝ) + α) * (a.val : ℝ) /
        (N : ℝ) : ℝ) : ℂ) * Complex.I)) = f k := by
  classical
  let g : ZMod N → ℂ := f ∘ (ZMod.finEquiv N).symm
  have hinv := (ZMod.dft : (ZMod N → ℂ) ≃ₗ[ℂ] (ZMod N → ℂ)).symm_apply_apply g
  have hinvk := congrFun hinv (ZMod.finEquiv N k)
  rw [ZMod.invDFT_apply] at hinvk
  have hphase (a : Fin N) :
      Complex.exp (((2 * Real.pi * ((k.val : ℝ) + α) * (a.val : ℝ) /
        (N : ℝ) : ℝ) : ℂ) * Complex.I) * shiftPhase N α a =
        ZMod.stdAddChar (ZMod.finEquiv N a * ZMod.finEquiv N k) := by
    have hcast : ZMod.finEquiv N a * ZMod.finEquiv N k =
        (((a.val : ℤ) * (k.val : ℤ) : ℤ) : ZMod N) := by
      rw [finEquiv_eq_cast, finEquiv_eq_cast]
      push_cast
      rfl
    rw [shiftPhase, ← Complex.exp_add, hcast, ZMod.stdAddChar_coe]
    congr 1
    push_cast
    ring
  have hs :
      (∑ a : Fin N, ZMod.stdAddChar (ZMod.finEquiv N a * ZMod.finEquiv N k) *
        ZMod.dft g (ZMod.finEquiv N a)) =
      ∑ a : ZMod N, ZMod.stdAddChar (a * ZMod.finEquiv N k) * ZMod.dft g a :=
    Equiv.sum_comp (ZMod.finEquiv N).toEquiv (fun a : ZMod N =>
      ZMod.stdAddChar (a * ZMod.finEquiv N k) * ZMod.dft g a)
  calc
    _ = (N : ℂ)⁻¹ * ∑ a : Fin N,
        ZMod.stdAddChar (ZMod.finEquiv N a * ZMod.finEquiv N k) *
          ZMod.dft g (ZMod.finEquiv N a) := by
      rw [mul_sum]
      apply sum_congr rfl
      intro a _
      rw [shiftedDFT]
      change _ = (N : ℂ)⁻¹ * (_ * ZMod.dft g (ZMod.finEquiv N a))
      rw [← hphase]
      ring
    _ = _ := by rw [hs]; simpa [g, smul_eq_mul] using hinvk

/-- Parseval with the coefficient normalization `1 / N`. -/
theorem shifted_parseval {N : ℕ} [NeZero N] (α : ℝ) (f : Fin N → ℂ) :
    (∑ a, ‖shiftedDFT α f a‖ ^ 2) =
      (∑ k, ‖f k‖ ^ 2) / (N : ℝ) := by
  classical
  have hN : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (NeZero.ne N)
  have hd := dft_energy (f ∘ (ZMod.finEquiv N).symm)
  have hs (v : ZMod N → ℝ) :
      (∑ a : Fin N, v (ZMod.finEquiv N a)) = ∑ k : ZMod N, v k :=
    Equiv.sum_comp (ZMod.finEquiv N).toEquiv v
  have hf : (∑ k : ZMod N, ‖f ((ZMod.finEquiv N).symm k)‖ ^ 2) =
      ∑ a : Fin N, ‖f a‖ ^ 2 := by
    simpa using
      (hs (fun k => ‖f ((ZMod.finEquiv N).symm k)‖ ^ 2)).symm
  simp only [shiftedDFT, norm_mul, norm_shiftPhase, one_mul, norm_inv,
    Complex.norm_natCast, mul_pow]
  rw [← mul_sum, hs (fun k => ‖ZMod.dft (f ∘ (ZMod.finEquiv N).symm) k‖ ^ 2), hd]
  change (N : ℝ)⁻¹ ^ 2 * ((N : ℝ) *
    (∑ k : ZMod N, ‖f ((ZMod.finEquiv N).symm k)‖ ^ 2)) = _
  rw [hf]
  field_simp

private theorem sum_indices (N : ℕ) :
    (∑ k : Fin N, (k.val : ℝ)) = (N : ℝ) * ((N : ℝ) - 1) / 2 := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Fin.sum_univ_castSucc]
    simpa only [Fin.val_castSucc, Fin.val_last, ih, Nat.cast_add, Nat.cast_one] using
      (show (N : ℝ) * ((N : ℝ) - 1) / 2 + (N : ℝ) =
        ((N : ℝ) + 1) * (((N : ℝ) + 1) - 1) / 2 by ring)

private theorem sum_squared_indices (N : ℕ) :
    (∑ k : Fin N, (k.val : ℝ) ^ 2) =
      (N : ℝ) * ((N : ℝ) - 1) * (2 * (N : ℝ) - 1) / 6 := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Fin.sum_univ_castSucc]
    simpa only [Fin.val_castSucc, Fin.val_last, ih, Nat.cast_add, Nat.cast_one] using
      (show (N : ℝ) * ((N : ℝ) - 1) * (2 * (N : ℝ) - 1) / 6 + (N : ℝ) ^ 2 =
        ((N : ℝ) + 1) * (((N : ℝ) + 1) - 1) * (2 * ((N : ℝ) + 1) - 1) / 6 by ring)

/-- The exact centered variance used by the normal data. -/
theorem centered_variance (N : ℕ) :
    (∑ k : Fin N, ((k.val : ℝ) - ((N : ℝ) - 1) / 2) ^ 2) =
      (N : ℝ) * ((N : ℝ) ^ 2 - 1) / 12 := by
  calc
    _ = (∑ k : Fin N, (k.val : ℝ) ^ 2) -
        ((N : ℝ) - 1) * (∑ k : Fin N, (k.val : ℝ)) +
        (N : ℝ) * (((N : ℝ) - 1) / 2) ^ 2 := by
      simp_rw [sub_sq]
      simp only [sum_add_distrib, sum_sub_distrib, ← sum_mul, ← mul_sum,
        sum_const, card_univ, Fintype.card_fin, nsmul_eq_mul]
      ring
    _ = _ := by rw [sum_indices, sum_squared_indices]; ring

/-- The normal data for the full integer crossing power. -/
def normalData {N : ℕ} (n : ℤ) (h : Fin N → ℂ) (k : Fin N) : ℂ :=
  (((n : ℝ) * ((k.val : ℝ) - ((N : ℝ) - 1) / 2) : ℝ) : ℂ) * h k

/-- The zeroth reconstructed coefficient is `H₀`.  Only the Fourier
normal coefficient `D₀` is omitted here; all physical normal data
`d_k`, including `d_0`, were transformed before this reconstruction. -/
def hermiteCoefficients {N : ℕ} (H D : Fin N → ℂ) (a : Fin N) : ℂ :=
  if a.val = 0 then H a
  else (((N : ℂ) - (a.val : ℂ)) * H a + D a) / (N : ℂ)

private def shiftedIndex {N : ℕ} (i : Fin N) : Fin N :=
  if h : i.val + 2 < N then ⟨i.val + 2, h⟩ else i

/-- Shift by two places with zero outside the array, as required by
`a_N = a_(N+1) = 0`. This is not a cyclic shift. -/
def shiftTwo {N : ℕ} (a : Fin N → ℂ) (j : Fin N) : ℂ :=
  if j.val + 2 < N then a (shiftedIndex j) else 0

/-- Coefficients in the ordinary-circle basis. -/
def circleCoefficients {N : ℕ} (a : Fin N → ℂ) (j : Fin N) : ℂ :=
  (-1 : ℂ) ^ j.val * (a j - shiftTwo a j)

private def vec {N : ℕ} (a : Fin N → ℂ) : EuclideanSpace ℂ (Fin N) :=
  WithLp.toLp 2 a

private theorem vec_norm_sq {N : ℕ} (a : Fin N → ℂ) :
    ‖vec a‖ ^ 2 = ∑ j, ‖a j‖ ^ 2 := by
  exact EuclideanSpace.norm_sq_eq (vec a)

private theorem vec_norm_le_of_pointwise {N : ℕ} (a b : Fin N → ℂ)
    (hab : ∀ j, ‖a j‖ ≤ ‖b j‖) : ‖vec a‖ ≤ ‖vec b‖ := by
  have he : ‖vec a‖ ^ 2 ≤ ‖vec b‖ ^ 2 := by
    rw [vec_norm_sq, vec_norm_sq]
    apply sum_le_sum
    intro j _
    exact pow_le_pow_left₀ (norm_nonneg _) (hab j) 2
  exact (sq_le_sq₀ (norm_nonneg _) (norm_nonneg _)).mp he

private theorem vec_norm_shiftTwo_le {N : ℕ} (a : Fin N → ℂ) :
    ‖vec (shiftTwo a)‖ ≤ ‖vec a‖ := by
  classical
  let s : Finset (Fin N) := univ.filter (fun i => i.val + 2 < N)
  have hinj : Set.InjOn (@shiftedIndex N) s := by
    intro i hi j hj hij
    have hi' : i.val + 2 < N := (mem_filter.mp hi).2
    have hj' : j.val + 2 < N := (mem_filter.mp hj).2
    have hv := congrArg Fin.val hij
    simp only [shiftedIndex, dif_pos hi', dif_pos hj'] at hv
    exact Fin.ext (by omega)
  have he : (∑ j, ‖shiftTwo a j‖ ^ 2) = ∑ j ∈ s, ‖a (shiftedIndex j)‖ ^ 2 := by
    rw [show s = univ.filter (fun i => i.val + 2 < N) from rfl, sum_filter]
    apply sum_congr rfl
    intro j _
    by_cases hj : j.val + 2 < N <;> simp [shiftTwo, hj]
  have hle : (∑ j ∈ s, ‖a (shiftedIndex j)‖ ^ 2) ≤ ∑ j, ‖a j‖ ^ 2 := by
    rw [← sum_image (f := fun j => ‖a j‖ ^ 2) hinj]
    exact sum_le_sum_of_subset_of_nonneg (subset_univ _)
      (by intro j _ _; positivity)
  have hn : ‖vec (shiftTwo a)‖ ^ 2 ≤ ‖vec a‖ ^ 2 := by
    simpa only [vec_norm_sq, he] using hle
  exact (sq_le_sq₀ (norm_nonneg _) (norm_nonneg _)).mp hn

private theorem circle_norm_le {N : ℕ} (a : Fin N → ℂ) :
    ‖vec (circleCoefficients a)‖ ≤ 2 * ‖vec a‖ := by
  have he : ‖vec (circleCoefficients a)‖ = ‖vec (a - shiftTwo a)‖ := by
    apply (sq_eq_sq₀ (norm_nonneg _) (norm_nonneg _)).mp
    simp only [vec_norm_sq, circleCoefficients, norm_mul, norm_pow, norm_neg,
      norm_one, one_pow, one_mul, Pi.sub_apply]
  rw [he]
  calc
    ‖vec (a - shiftTwo a)‖ ≤ ‖vec a‖ + ‖vec (shiftTwo a)‖ :=
      norm_sub_le (vec a) (vec (shiftTwo a))
    _ ≤ 2 * ‖vec a‖ := by linarith [vec_norm_shiftTwo_le a]

private theorem sum_norm_le_sqrt_card {N : ℕ} (a : Fin N → ℂ) :
    (∑ j, ‖a j‖) ≤ Real.sqrt N * ‖vec a‖ := by
  have hs := sum_mul_sq_le_sq_mul_sq (univ : Finset (Fin N))
    (fun j => ‖a j‖) (fun _ => (1 : ℝ))
  have hr : (Real.sqrt N * ‖vec a‖) ^ 2 =
      (∑ j, ‖a j‖ ^ 2) * (N : ℝ) := by
    rw [mul_pow, Real.sq_sqrt (Nat.cast_nonneg _), vec_norm_sq]
    ring
  apply (sq_le_sq₀ (by positivity) (by positivity)).mp
  rw [hr]
  simpa using hs

private def valuePart {N : ℕ} (H : Fin N → ℂ) (a : Fin N) : ℂ :=
  ((((N : ℝ) - (a.val : ℝ)) / (N : ℝ) : ℝ) : ℂ) * H a

private def normalPart {N : ℕ} (D : Fin N → ℂ) (a : Fin N) : ℂ :=
  if a.val = 0 then 0 else (N : ℂ)⁻¹ * D a

private theorem hermite_decomposition {N : ℕ} [NeZero N] (H D : Fin N → ℂ) :
    hermiteCoefficients H D = valuePart H + normalPart D := by
  funext a
  have hn : (N : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr (NeZero.ne N)
  simp only [hermiteCoefficients, valuePart, normalPart, Pi.add_apply,
    Complex.ofReal_div, Complex.ofReal_sub, Complex.ofReal_natCast]
  by_cases ha : a.val = 0
  · simp [ha, hn]
  · simp only [ha, if_false]
    field_simp

private theorem valuePart_norm_le {N : ℕ} [NeZero N] (H : Fin N → ℂ) :
    ‖vec (valuePart H)‖ ≤ ‖vec H‖ := by
  apply vec_norm_le_of_pointwise
  intro a
  have hn : (0 : ℝ) < N := by exact_mod_cast NeZero.pos N
  have hi : (a.val : ℝ) ≤ N := by exact_mod_cast a.isLt.le
  have h0 : 0 ≤ ((N : ℝ) - a.val) / N := div_nonneg (sub_nonneg.mpr hi) hn.le
  have h1 : ((N : ℝ) - a.val) / N ≤ 1 := by
    rw [div_le_one hn]
    exact sub_le_self _ (Nat.cast_nonneg _)
  simp only [valuePart, norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg h0]
  exact mul_le_of_le_one_left (norm_nonneg _) h1

private theorem normalPart_norm_le {N : ℕ} [NeZero N] (D : Fin N → ℂ) :
    ‖vec (normalPart D)‖ ≤ ‖vec D‖ / (N : ℝ) := by
  have hle : ‖vec (normalPart D)‖ ≤
      ‖vec (fun a => (N : ℂ)⁻¹ * D a)‖ := by
    apply vec_norm_le_of_pointwise
    intro a
    by_cases ha : a.val = 0
    · simp only [normalPart, ha, if_true, norm_zero]
      positivity
    · simp [normalPart, ha]
  calc
    ‖vec (normalPart D)‖ ≤ ‖(N : ℂ)⁻¹ • vec D‖ := hle
    _ = ‖vec D‖ / (N : ℝ) := by
      rw [norm_smul, norm_inv, Complex.norm_natCast]
      ring

private theorem hermite_norm_le {N : ℕ} [NeZero N] (H D : Fin N → ℂ) :
    ‖vec (hermiteCoefficients H D)‖ ≤ ‖vec H‖ + ‖vec D‖ / (N : ℝ) := by
  rw [hermite_decomposition]
  exact (norm_add_le (vec (valuePart H)) (vec (normalPart D))).trans
    (add_le_add (valuePart_norm_le H) (normalPart_norm_le D))

/-- Parseval for the unit value data, with every shifted-grid phase kept. -/
theorem value_energy {N : ℕ} [NeZero N] (α : ℝ) (h : Fin N → ℂ)
    (hh : ∀ k, ‖h k‖ = 1) :
    (∑ a, ‖shiftedDFT α h a‖ ^ 2) = 1 := by
  rw [shifted_parseval]
  simp only [hh, one_pow, sum_const, card_univ, Fintype.card_fin,
    nsmul_eq_mul, mul_one]
  exact div_self (Nat.cast_ne_zero.mpr (NeZero.ne N))

/-- The exact normal-data energy, including the finite `N² - 1` correction. -/
theorem normal_energy {N : ℕ} [NeZero N] (α : ℝ) (n : ℤ)
    (h : Fin N → ℂ) (hh : ∀ k, ‖h k‖ = 1) :
    (∑ a, ‖shiftedDFT α (normalData n h) a‖ ^ 2) =
      (n : ℝ) ^ 2 * ((N : ℝ) ^ 2 - 1) / 12 := by
  rw [shifted_parseval]
  have he : (∑ k, ‖normalData n h k‖ ^ 2) =
      (n : ℝ) ^ 2 *
        ∑ k : Fin N, ((k.val : ℝ) - ((N : ℝ) - 1) / 2) ^ 2 := by
    simp only [normalData, norm_mul, hh, mul_one, Complex.norm_real,
      Real.norm_eq_abs, sq_abs, mul_pow, mul_sum]
  rw [he, centered_variance]
  have hn : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (NeZero.ne N)
  field_simp

private theorem transformed_normal_norm_le {N : ℕ} [NeZero N]
    (hN : (0 : ℝ) < N) (α : ℝ) (n : ℤ) (h : Fin N → ℂ)
    (hh : ∀ k, ‖h k‖ = 1) :
    ‖vec (shiftedDFT α (normalData n h))‖ / (N : ℝ) ≤
      |(n : ℝ)| / Real.sqrt 12 := by
  apply (div_le_iff₀ hN).mpr
  apply (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp
  rw [vec_norm_sq, normal_energy α n h hh, mul_pow, div_pow,
    Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 12), sq_abs]
  nlinarith [sq_nonneg (n : ℝ)]

/-- The complete value/normal reconstruction followed by the truncated
ordinary-circle conversion. -/
def fillingCoefficients {N : ℕ} [NeZero N] (α : ℝ) (n : ℤ)
    (h : Fin N → ℂ) : Fin N → ℂ :=
  circleCoefficients (hermiteCoefficients
    (shiftedDFT α h) (shiftedDFT α (normalData n h)))

/-- The actual finite-array bound used by the Conway filling proof.
The exceptional Fourier coefficient uses `H₀`, and both out-of-range
values of the shift are zero. -/
theorem hermite_coefficient_mass {N : ℕ} [NeZero N] (hN : 2 ≤ N)
    (α : ℝ) (n : ℤ) (h : Fin N → ℂ) (hh : ∀ k, ‖h k‖ = 1) :
    (∑ j, ‖fillingCoefficients α n h j‖) ≤
      2 * Real.sqrt N * (1 + |(n : ℝ)| / Real.sqrt 12) := by
  have hn : (0 : ℝ) < N := by exact_mod_cast (lt_of_lt_of_le (by decide : 0 < 2) hN)
  have hv : ‖vec (shiftedDFT α h)‖ = 1 := by
    have he : ‖vec (shiftedDFT α h)‖ ^ 2 = 1 := by
      rw [vec_norm_sq, value_energy α h hh]
    nlinarith [norm_nonneg (vec (shiftedDFT α h))]
  have ha : ‖vec (hermiteCoefficients
      (shiftedDFT α h) (shiftedDFT α (normalData n h)))‖ ≤
      1 + |(n : ℝ)| / Real.sqrt 12 := by
    exact (hermite_norm_le _ _).trans (by
      rw [hv]
      exact add_le_add_right (transformed_normal_norm_le hn α n h hh) 1)
  calc
    (∑ j, ‖fillingCoefficients α n h j‖) ≤
        Real.sqrt N * ‖vec (fillingCoefficients α n h)‖ := sum_norm_le_sqrt_card _
    _ ≤ Real.sqrt N * (2 * ‖vec (hermiteCoefficients
        (shiftedDFT α h) (shiftedDFT α (normalData n h)))‖) :=
      mul_le_mul_of_nonneg_left (circle_norm_le _) (Real.sqrt_nonneg _)
    _ ≤ Real.sqrt N * (2 * (1 + |(n : ℝ)| / Real.sqrt 12)) :=
      mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left ha (by norm_num))
        (Real.sqrt_nonneg _)
    _ = _ := by ring

/-- The normalized physical value data `(-1)^(n k) q^(n k(k+1))`,
with the fixed exponential lift of every integral power. -/
def crossingValues (N : ℕ) (n : ℤ) (k : Fin N) : ℂ :=
  (-1 : ℂ) ^ (n * (k.val : ℤ)) *
    Complex.exp (((Real.pi * (n : ℝ) * (k.val : ℝ) * ((k.val : ℝ) + 1) /
      (N : ℝ) : ℝ) : ℂ) * Complex.I)

@[simp] theorem norm_crossingValues (N : ℕ) (n : ℤ) (k : Fin N) :
    ‖crossingValues N n k‖ = 1 := by
  rw [crossingValues, norm_mul, norm_zpow]
  simp only [norm_neg, norm_one, one_zpow, one_mul]
  exact Complex.norm_exp_ofReal_mul_I _

/-- The actual midpoint-grid coefficient array for a fixed signed power. -/
def crossingCoefficients {N : ℕ} [NeZero N] (n : ℤ) : Fin N → ℂ :=
  fillingCoefficients (1 / 2) n (crossingValues N n)

/-- The coefficient cost for the explicit physical value and normal arrays. -/
theorem crossing_coefficient_mass {N : ℕ} [NeZero N] (hN : 2 ≤ N) (n : ℤ) :
    (∑ j, ‖crossingCoefficients (N := N) n j‖) ≤
      2 * Real.sqrt N * (1 + |(n : ℝ)| / Real.sqrt 12) := by
  exact hermite_coefficient_mass hN (1 / 2) n (crossingValues N n)
    (norm_crossingValues N n)

end VolumeLogic.FourierHermite
