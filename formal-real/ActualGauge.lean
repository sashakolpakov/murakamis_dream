import FormalGauge
import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Complex

/-! Exact scalar gauge algebra for an actual finite recurrence.  The finite
coefficient family is constructed before any asymptotic expansion. -/
noncomputable section
namespace VolumeLogic.ActualGauge

variable {R : Type*} [CommRing R]

def denominator (r : ℕ) (f : ℕ → R) : R :=
  ∏ k ∈ Finset.Icc 1 r, f k

def punctured (r j : ℕ) (f : ℕ → R) : R :=
  ∏ k ∈ (Finset.Icc 1 r).erase j, f k

def clearedCoefficient (r : ℕ) (a f : ℕ → R) (j : ℕ) : R :=
  if j = 0 then denominator r f * a 0
  else (-1)^j * f 0 * punctured r j f * a j

theorem denominator_clearing (r : ℕ) (a f : ℕ → R)
    (j : ℕ) (hjr : j ≤ r) :
    f j * clearedCoefficient r a f j =
      denominator r f * (-1)^j * f 0 * a j := by
  by_cases hj : j = 0
  · subst j
    simp [clearedCoefficient, mul_left_comm, mul_assoc]
  · have hp : f j * punctured r j f = denominator r f :=
      Finset.mul_prod_erase (Finset.Icc 1 r) f
        (Finset.mem_Icc.mpr ⟨by omega, hjr⟩)
    rw [clearedCoefficient, if_neg hj, ← hp]
    ring

/-- The scalar construction is precisely the existing formal coefficient
construction when its coefficient ring is the bivariate series ring. -/
theorem formal_coefficient_eq {A : Type*} [CommRing A] [Algebra ℚ A]
    (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) A) (j : ℕ) :
    FormalGauge.clearedCoefficient r a j =
      clearedCoefficient r a (FormalGauge.shiftedMeridian (R := A)) j := rfl

/-- Any coefficient-ring homomorphism transports the constructed finite
products, including the special zeroth coefficient. -/
theorem map_clearedCoefficient {S : Type*} [CommRing S] (φ : R →+* S)
    (r : ℕ) (a f : ℕ → R) (j : ℕ) :
    φ (clearedCoefficient r a f j) =
      clearedCoefficient r (fun k => φ (a k)) (fun k => φ (f k)) j := by
  by_cases hj : j = 0
  · simp [clearedCoefficient, hj, denominator, map_prod]
  · simp [clearedCoefficient, hj, punctured, map_prod]

section Field
variable {K : Type*} [Field K]

/-- A multiplied gauge identity is enough. No inverse of the unshifted
meridian factor f(0) is required. -/
theorem coefficient_times_normalization (r : ℕ) (a f H : ℕ → K)
    (j : ℕ) (hjr : j ≤ r)
    (hn : ∀ j, 1 ≤ j → j ≤ r → f j ≠ 0)
    (hg : ∀ j, 1 ≤ j → j ≤ r → H j * f j = (-1)^j * H 0 * f 0) :
    clearedCoefficient r a f j * H 0 = denominator r f * a j * H j := by
  by_cases hj : j = 0
  · subst j
    simp [clearedCoefficient, mul_assoc]
  · have hpos : 1 ≤ j := by omega
    apply mul_left_cancel₀ (hn j hpos hjr)
    calc
      f j * (clearedCoefficient r a f j * H 0) =
          (f j * clearedCoefficient r a f j) * H 0 := by ring
      _ = (denominator r f * (-1)^j * f 0 * a j) * H 0 := by
        rw [denominator_clearing r a f j hjr]
      _ = denominator r f * a j * ((-1)^j * H 0 * f 0) := by ring
      _ = denominator r f * a j * (H j * f j) := by rw [hg j hpos hjr]
      _ = f j * (denominator r f * a j * H j) := by ring

/-- The exact original recurrence implies the constructed cleared equation.
The only cancellations are the actual nonzero normalization factors. -/
theorem cleared_equation_of_recurrence (r : ℕ) (a f F H Z : ℕ → K)
    (scale : K) (hs : scale ≠ 0) (hH : H 0 ≠ 0) (hZ : Z 0 ≠ 0)
    (hn : ∀ j, 1 ≤ j → j ≤ r → f j ≠ 0)
    (hg : ∀ j, 1 ≤ j → j ≤ r → H j * f j = (-1)^j * H 0 * f 0)
    (hF : ∀ j ≤ r, F j = scale * H j * Z j)
    (he : ∑ j ∈ Finset.range (r+1), a j * F j = 0) :
    ∑ j ∈ Finset.range (r+1), clearedCoefficient r a f j * (Z j / Z 0) = 0 := by
  apply mul_left_cancel₀ (mul_ne_zero (mul_ne_zero hs hH) hZ)
  rw [mul_zero, Finset.mul_sum]
  have hh : ∑ j ∈ Finset.range (r+1),
      (scale * H 0 * Z 0) * (clearedCoefficient r a f j * (Z j / Z 0)) =
      denominator r f * ∑ j ∈ Finset.range (r+1), a j * F j := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j hj
    have hjr : j ≤ r := by have := Finset.mem_range.mp hj; omega
    rw [hF j hjr]
    have hc := coefficient_times_normalization r a f H j hjr hn hg
    calc
      (scale * H 0 * Z 0) * (clearedCoefficient r a f j * (Z j / Z 0)) =
          scale * (clearedCoefficient r a f j * H 0) * Z j := by
        field_simp
      _ = scale * (denominator r f * a j * H j) * Z j := by rw [hc]
      _ = denominator r f * (a j * (scale * H j * Z j)) := by ring
  rw [hh, he, mul_zero]

/-- The familiar quotient form implies the multiplied gauge used above. -/
theorem cleared_equation_of_ratio (r : ℕ) (a f F H Z : ℕ → K)
    (scale : K) (hs : scale ≠ 0) (hH : H 0 ≠ 0) (hZ : Z 0 ≠ 0)
    (hn : ∀ j, 1 ≤ j → j ≤ r → f j ≠ 0)
    (hg : ∀ j, 1 ≤ j → j ≤ r → H j / H 0 = (-1)^j * f 0 / f j)
    (hF : ∀ j ≤ r, F j = scale * H j * Z j)
    (he : ∑ j ∈ Finset.range (r+1), a j * F j = 0) :
    ∑ j ∈ Finset.range (r+1), clearedCoefficient r a f j * (Z j / Z 0) = 0 := by
  apply cleared_equation_of_recurrence r a f F H Z scale hs hH hZ hn ?_ hF he
  intro j hpos hjr
  have h := (div_eq_div_iff hH (hn j hpos hjr)).mp (hg j hpos hjr)
  calc
    _ = (-1)^j * f 0 * H 0 := h
    _ = _ := by ring

end Field

/-- The literal normalization away from its removable singularities. -/
def sineNormalization (N : ℕ) (s : ℂ) : ℂ :=
  Complex.sin (Real.pi * s) / ((N : ℂ) * Complex.sin (Real.pi * s / N))

/-- The actual meridian divisor for q=exp(pi*i/N), at the shifted parameter. -/
def sineMeridian (N : ℕ) (s : ℂ) (j : ℕ) : ℂ :=
  2 * Complex.I * Complex.sin (Real.pi * (s+j) / N)

theorem sineMeridian_eq_exp (N : ℕ) (s : ℂ) (j : ℕ) :
    sineMeridian N s j =
      Complex.exp ((Real.pi * (s+j) / N) * Complex.I) -
      Complex.exp (-((Real.pi * (s+j) / N) * Complex.I)) := by
  rw [sineMeridian, neg_mul_eq_neg_mul, ← Complex.cos_add_sin_I,
    ← Complex.cos_sub_sin_I]
  ring

/-- The actual root and meridian used in the microscopic substitution. -/
def levelRoot (N : ℕ) : ℂ := Complex.exp ((Real.pi / N) * Complex.I)

def meridianValue (N : ℕ) (s : ℂ) : ℂ :=
  Complex.exp ((Real.pi * s / N) * Complex.I)

theorem levelRoot_power (N : ℕ) (hN : (N : ℂ) ≠ 0) :
    levelRoot N ^ N = -1 := by
  rw [levelRoot, ← Complex.exp_nat_mul]
  have harg : (N : ℂ) * ((Real.pi / N) * Complex.I) = Real.pi * Complex.I := by
    field_simp
  rw [harg, Complex.exp_pi_mul_I]

theorem meridianValue_shift (N : ℕ) (s : ℂ) (j : ℕ) :
    meridianValue N (s+j) = levelRoot N ^ j * meridianValue N s := by
  rw [meridianValue, levelRoot, meridianValue, ← Complex.exp_nat_mul, ← Complex.exp_add]
  congr 1
  ring

theorem sineMeridian_eq_root_shift (N : ℕ) (s : ℂ) (j : ℕ) :
    sineMeridian N s j = levelRoot N ^ j * meridianValue N s -
      (levelRoot N ^ j * meridianValue N s)⁻¹ := by
  rw [sineMeridian_eq_exp, Complex.exp_neg, ← meridianValue_shift]
  rfl

/-- Integer shifts change the numerator by exactly the retained parity sign. -/
theorem numerator_shift (s : ℂ) (j : ℕ) :
    Complex.sin (Real.pi * (s+j)) = (-1)^j * Complex.sin (Real.pi * s) := by
  have h := Complex.sin_antiperiodic.add_nat_mul_eq j (x := Real.pi * s)
  have he : (Real.pi : ℂ) * (s+j) = Real.pi * s + j * Real.pi := by ring
  rw [he]
  exact h

/-- The exact physical sine quotient satisfies the multiplied gauge. The
assumptions exclude only the denominators actually used in this chart. -/
theorem sine_gauge (N : ℕ) (s : ℂ) (j : ℕ) (hN : (N : ℂ) ≠ 0)
    (h0 : Complex.sin (Real.pi * s / N) ≠ 0)
    (hj : Complex.sin (Real.pi * (s+j) / N) ≠ 0) :
    sineNormalization N (s+j) * sineMeridian N s j =
      (-1)^j * sineNormalization N s * sineMeridian N s 0 := by
  simp only [sineNormalization, sineMeridian, Nat.cast_zero, add_zero]
  rw [numerator_shift]
  field_simp

/-- No shifted sine denominator vanishes off the real axis. This is the
chart used for the actual finite recurrence before taking asymptotics. -/
theorem shifted_sine_ne_zero (N : ℕ) (s : ℂ) (j : ℕ)
    (hN : (N : ℂ) ≠ 0) (hs : s.im ≠ 0) :
    Complex.sin (Real.pi * (s+j) / N) ≠ 0 := by
  intro hz
  obtain ⟨k, hk⟩ := Complex.sin_eq_zero_iff.mp hz
  have he := (div_eq_iff hN).mp hk
  have hi := congrArg Complex.im he
  simp only [Complex.mul_im, Complex.add_re, Complex.add_im,
    Complex.ofReal_re, Complex.ofReal_im, Complex.natCast_re,
    Complex.natCast_im, Complex.intCast_re, Complex.intCast_im,
    add_zero, zero_mul, mul_zero] at hi
  exact hs ((mul_eq_zero.mp hi).resolve_left Real.pi_ne_zero)

/-- The original finite recurrence, with the literal sine normalization,
produces the exact cleared equation on every nonreal parameter. -/
theorem sine_cleared_equation (N r : ℕ) (s : ℂ) (a F Z : ℕ → ℂ)
    (scale : ℂ) (hN : (N : ℂ) ≠ 0) (hs : s.im ≠ 0)
    (hscale : scale ≠ 0) (hZ : Z 0 ≠ 0)
    (hF : ∀ j ≤ r, F j = scale * sineNormalization N (s+j) * Z j)
    (he : ∑ j ∈ Finset.range (r+1), a j * F j = 0) :
    ∑ j ∈ Finset.range (r+1),
      clearedCoefficient r a (sineMeridian N s) j * (Z j / Z 0) = 0 := by
  have hd (j : ℕ) := shifted_sine_ne_zero N s j hN hs
  have hsin : Complex.sin (Real.pi * s) ≠ 0 := by
    simpa using shifted_sine_ne_zero 1 s 0 (by norm_num) hs
  have hden : Complex.sin (Real.pi * s / N) ≠ 0 := by simpa using hd 0
  have hH : sineNormalization N (s+(0 : ℕ)) ≠ 0 := by
    simpa [sineNormalization] using div_ne_zero hsin (mul_ne_zero hN hden)
  apply cleared_equation_of_recurrence r a (sineMeridian N s) F
    (fun j => sineNormalization N (s+j)) Z scale hscale hH hZ ?_ ?_ hF he
  · intro j _ _
    exact mul_ne_zero (mul_ne_zero (by norm_num) Complex.I_ne_zero) (hd j)
  · intro j _ _
    simpa only [Nat.cast_zero, add_zero] using sine_gauge N s j hN hden (hd j)

end VolumeLogic.ActualGauge
