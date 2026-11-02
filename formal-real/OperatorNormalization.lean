import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.Bivariate
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.Ring
import Mathlib.RingTheory.PowerSeries.Exp
import Mathlib.RingTheory.PowerSeries.Order
import ActualGauge
import Mathlib.RingTheory.Localization.Integer
import Mathlib.RingTheory.Localization.FractionRing

/-! A finite operator is recorded as a polynomial in q with coefficients in
R[L]. The symbol L records shift degree; this commutative coefficient record
does not identify Ore multiplication with commutative multiplication. -/
noncomputable section
namespace VolumeLogic.OperatorNormalization
open Polynomial
variable {R : Type*} [CommRing R]

/-- A nonzero finite rational coefficient family has a common nonzero
denominator and a nonzero cleared family. This is algebraic clearing;
nonvanishing of that denominator on a chosen analytic chart is separate. -/
theorem exists_nonzero_cleared_family {B : Type*} [CommRing B] [IsDomain B]
    {K : Type*} [Field K] [Algebra B K] [IsFractionRing B K]
    {ι : Type*} [Finite ι] (a : ι → K) (ha : ∃ i, a i ≠ 0) :
    ∃ d : B, d ≠ 0 ∧ ∃ b : ι → B,
      (∀ i, algebraMap B K (b i) = algebraMap B K d * a i) ∧ ∃ i, b i ≠ 0 := by
  obtain ⟨d, hd⟩ := IsLocalization.exist_integer_multiples_of_finite (nonZeroDivisors B) a
  choose b hb using hd
  have hdn : (d : B) ≠ 0 := mem_nonZeroDivisors_iff_ne_zero.mp d.property
  refine ⟨d, hdn, b, ?_, ?_⟩
  · intro i
    simpa [Algebra.smul_def] using hb i
  · obtain ⟨i, hi⟩ := ha
    refine ⟨i, ?_⟩
    intro hh
    have hz := hb i
    have hmap : algebraMap B K (d : B) ≠ 0 := by
      intro hz
      apply hdn
      apply IsFractionRing.injective B K
      rw [hz, map_zero]
    simp only [hh, map_zero, Algebra.smul_def] at hz
    exact (mul_ne_zero hmap hi) hz.symm


/-- The maximal common q-1 multiplicity of the finite coefficient record. -/
def commonOrder (P : Polynomial (Polynomial R)) : ℕ := P.rootMultiplicity 1

/-- Actual monic division, rather than a normalized-symbol existence premise. -/
def normalize (P : Polynomial (Polynomial R)) : Polynomial (Polynomial R) :=
  P /ₘ (Polynomial.X - Polynomial.C 1)^commonOrder P

/-- The Laurent-in-M, polynomial-in-L classical coefficient record at q=1. -/
def classicalSymbol (P : Polynomial (Polynomial R)) : Polynomial R :=
  (normalize P).eval 1

theorem factorization (P : Polynomial (Polynomial R)) :
    P = (Polynomial.X - Polynomial.C 1)^commonOrder P * normalize P :=
  (Polynomial.pow_mul_divByMonic_rootMultiplicity_eq P 1).symm

theorem classicalSymbol_ne_zero {P : Polynomial (Polynomial R)} (hP : P ≠ 0) :
    classicalSymbol P ≠ 0 :=
  Polynomial.eval_divByMonic_pow_rootMultiplicity_ne_zero 1 hP

theorem maximal_common_order {P : Polynomial (Polynomial R)} (hP : P ≠ 0) :
    ¬ (Polynomial.X - Polynomial.C 1)^(commonOrder P+1) ∣ P :=
  Polynomial.pow_rootMultiplicity_not_dvd hP 1

theorem common_order_iff {P : Polynomial (Polynomial R)} (hP : P ≠ 0) (k : ℕ) :
    k ≤ commonOrder P ↔ (Polynomial.X - Polynomial.C 1)^k ∣ P :=
  Polynomial.le_rootMultiplicity_iff hP

theorem normalized_common_order_zero {P : Polynomial (Polynomial R)} (hP : P ≠ 0) :
    commonOrder (normalize P) = 0 :=
  Polynomial.rootMultiplicity_eq_zero (classicalSymbol_ne_zero hP)


/-- Coefficient evaluation in an arbitrary target ring. This is the actual
coefficient multiplying the jth shifted value at the specified q. -/
def actualCoefficient {K : Type*} [CommRing K] (φ : R →+* K)
    (q : K) (P : Polynomial (Polynomial R)) (j : ℕ) : K :=
  ((P.map (Polynomial.mapRingHom φ)).eval (Polynomial.C q)).coeff j

theorem coefficient_factorization {K : Type*} [CommRing K] (φ : R →+* K)
    (q : K) (P : Polynomial (Polynomial R)) (j : ℕ) :
    actualCoefficient φ q P j =
      (q-1)^commonOrder P * actualCoefficient φ q (normalize P) j := by
  have hp := congrArg (fun B : Polynomial (Polynomial R) =>
    ((B.map (Polynomial.mapRingHom φ)).eval (Polynomial.C q)).coeff j) (factorization P)
  simp only [Polynomial.map_mul, Polynomial.map_pow, Polynomial.map_sub,
    Polynomial.map_X, Polynomial.map_one, map_one, Polynomial.eval_mul,
    Polynomial.eval_pow, Polynomial.eval_sub, Polynomial.eval_X, Polynomial.eval_one] at hp
  have he : ((Polynomial.C q : Polynomial K) - 1)^commonOrder P =
      Polynomial.C ((q-1)^commonOrder P) := by simp
  rw [he, Polynomial.coeff_C_mul] at hp
  exact hp

theorem recurrence_factorization {K : Type*} [CommRing K] (φ : R →+* K)
    (q : K) (P : Polynomial (Polynomial R)) (s : Finset ℕ) (v : ℕ → K) :
    (∑ j ∈ s, actualCoefficient φ q P j * v j) =
      (q-1)^commonOrder P * ∑ j ∈ s, actualCoefficient φ q (normalize P) j * v j := by
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [coefficient_factorization φ q P j]
  ring

/-- Stripping the common factor preserves an actual recurrence wherever q≠1.
The target coefficient specialization need not be injective. -/
theorem recurrence_iff {K : Type*} [CommRing K] [NoZeroDivisors K]
    (φ : R →+* K) (q : K) (hq : q ≠ 1)
    (P : Polynomial (Polynomial R)) (s : Finset ℕ) (v : ℕ → K) :
    (∑ j ∈ s, actualCoefficient φ q P j * v j) = 0 ↔
      (∑ j ∈ s, actualCoefficient φ q (normalize P) j * v j) = 0 := by
  rw [recurrence_factorization, mul_eq_zero]
  simp [pow_ne_zero _ (sub_ne_zero.mpr hq)]

/-- Changing L to -L is an involution and cannot destroy a nonzero symbol. -/
theorem sign_substitution_ne_zero {P : Polynomial R} (hP : P ≠ 0) :
    P.comp (-Polynomial.X) ≠ 0 := by
  intro hh
  have he := congrArg (fun Q : Polynomial R => Q.comp (-Polynomial.X)) hh
  have hi : (-Polynomial.X : Polynomial R).comp (-Polynomial.X) = Polynomial.X := by simp
  rw [Polynomial.comp_assoc, hi, Polynomial.comp_X, Polynomial.zero_comp] at he
  exact hP he

/-- The complete meridian and sign gauge remains nonzero as a polynomial.
This assertion concerns the polynomial ring, not its evaluation at M=1. -/
theorem gauged_symbol_ne_zero [NoZeroDivisors R] {P : Polynomial (Polynomial R)}
    (hP : P ≠ 0) (f : R) (hf : f ≠ 0) (r : ℕ) :
    Polynomial.C (f^r) * (classicalSymbol P).comp (-Polynomial.X) ≠ 0 := by
  exact mul_ne_zero (Polynomial.C_ne_zero.mpr (pow_ne_zero r hf))
    (sign_substitution_ne_zero (classicalSymbol_ne_zero hP))

/-- The retained meridian factor in the actual Laurent coefficient ring. -/
def meridian : LaurentPolynomial ℂ := LaurentPolynomial.T 1 - LaurentPolynomial.T (-1)

theorem meridian_ne_zero : meridian ≠ 0 := by
  intro hh
  have hc := congrArg (fun P : LaurentPolynomial ℂ => P.coeff 1) hh
  norm_num [meridian, LaurentPolynomial.T_apply] at hc

theorem laurent_gauged_symbol_ne_zero {P : Polynomial (Polynomial (LaurentPolynomial ℂ))}
    (hP : P ≠ 0) (r : ℕ) :
    Polynomial.C (meridian^r) * (classicalSymbol P).comp (-Polynomial.X) ≠ 0 :=
  gauged_symbol_ne_zero hP meridian meridian_ne_zero r


/-- The finite root convention used by the source never equals one at a
positive level, so the normalization factor is cancellable there. -/
theorem levelRoot_ne_one (N : ℕ) (hN : (N : ℂ) ≠ 0) :
    ActualGauge.levelRoot N ≠ 1 := by
  intro hh
  have hp := ActualGauge.levelRoot_power N hN
  rw [hh, one_pow] at hp
  norm_num at hp

theorem recurrence_at_root_iff (φ : R →+* ℂ) (N : ℕ) (hN : (N : ℂ) ≠ 0)
    (P : Polynomial (Polynomial R)) (s : Finset ℕ) (v : ℕ → ℂ) :
    (∑ j ∈ s, actualCoefficient φ (ActualGauge.levelRoot N) P j * v j) = 0 ↔
      (∑ j ∈ s, actualCoefficient φ (ActualGauge.levelRoot N) (normalize P) j * v j) = 0 :=
  recurrence_iff φ _ (levelRoot_ne_one N hN) P s v

section Taylor
variable [Algebra ℚ R]

/-- The formal q=e^h substitution with L kept as a coefficient variable. -/
def qTaylor (P : Polynomial (Polynomial R)) : PowerSeries (Polynomial R) :=
  P.eval₂ PowerSeries.C (PowerSeries.exp (Polynomial R))

theorem qTaylor_constant (P : Polynomial (Polynomial R)) :
    PowerSeries.constantCoeff (qTaylor P) = P.eval 1 := by
  induction P using Polynomial.induction_on' with
  | add P Q hP hQ => simpa [qTaylor] using congrArg₂ (· + ·) hP hQ
  | monomial n a => simp [qTaylor]

/-- The actual unit in e^h-1=h*unit, including all higher coefficients. -/
def exponentialUnit : PowerSeries R :=
  PowerSeries.mk (fun n => algebraMap ℚ R (1 / ((n+1).factorial : ℚ)))

theorem exponentialUnit_constant :
    PowerSeries.constantCoeff (exponentialUnit (R := R)) = 1 := by
  simp [exponentialUnit]

theorem exp_sub_one_factorization :
    PowerSeries.exp R - 1 = PowerSeries.X * exponentialUnit (R := R) := by
  ext n
  rw [show PowerSeries.X * exponentialUnit (R := R) =
    PowerSeries.X^1 * exponentialUnit (R := R) by simp,
    PowerSeries.coeff_X_pow_mul']
  cases n with
  | zero => simp
  | succ n => simp [exponentialUnit]

theorem exponentialUnit_isUnit : IsUnit (exponentialUnit (R := R)) :=
  PowerSeries.isUnit_iff_constantCoeff.mpr (by rw [exponentialUnit_constant]; exact isUnit_one)

/-- Removing the common q-1 factor gives precisely the same leading symbol
after q=e^h, because the intervening factor has constant coefficient one. -/
theorem qTaylor_factorization (P : Polynomial (Polynomial R)) :
    qTaylor P = PowerSeries.X^commonOrder P *
      (exponentialUnit (R := Polynomial R)^commonOrder P * qTaylor (normalize P)) := by
  have hp := congrArg qTaylor (factorization P)
  unfold qTaylor at hp
  rw [Polynomial.eval₂_mul, Polynomial.eval₂_pow, Polynomial.eval₂_sub,
    Polynomial.eval₂_X, Polynomial.eval₂_C, map_one] at hp
  rw [exp_sub_one_factorization, mul_pow, mul_assoc] at hp
  exact hp

theorem qTaylor_leading_coefficient (P : Polynomial (Polynomial R)) :
    PowerSeries.coeff (commonOrder P) (qTaylor P) = classicalSymbol P := by
  rw [qTaylor_factorization, PowerSeries.coeff_X_pow_mul']
  simp [PowerSeries.coeff_zero_eq_constantCoeff, exponentialUnit_constant,
    qTaylor_constant, classicalSymbol]

theorem qTaylor_lower_coefficients (P : Polynomial (Polynomial R))
    (n : ℕ) (hn : n < commonOrder P) : PowerSeries.coeff n (qTaylor P) = 0 := by
  rw [qTaylor_factorization, PowerSeries.coeff_X_pow_mul']
  simp [hn]

theorem qTaylor_order {P : Polynomial (Polynomial R)} (hP : P ≠ 0) :
    (qTaylor P).order = commonOrder P := by
  rw [PowerSeries.order_eq_nat]
  constructor
  · rw [qTaylor_leading_coefficient]
    exact classicalSymbol_ne_zero hP
  · exact qTaylor_lower_coefficients P

end Taylor

end VolumeLogic.OperatorNormalization
