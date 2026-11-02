import AsymptoticIdentity
import FormalRegradingRing
import FormalExp
import FormalGauge
import Mathlib.Tactic.Ring

/-! The analytic-to-formal characteristic implication. The estimates for the
actual finite recurrence and its coefficient normalization remain explicit
inputs; the formal shifts, regrading, projection and divisor cancellation
are constructed and proved. -/
noncomputable section
namespace VolumeLogic.FormalCharacteristic
open Filter Asymptotics
open scoped Topology
open FormalShift FormalExp FormalRegradingRing AsymptoticIdentity

def shiftedEquation (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ) :
    MvPowerSeries (Fin 2) ℂ :=
  ∑ j ∈ Finset.range (r+1), a j * exponential (logarithmicShift S A (j : ℂ))

def classicalPolynomial (r : ℕ) (b : ℕ → PowerSeries ℂ) :
    Polynomial (PowerSeries ℂ) :=
  ∑ j ∈ Finset.range (r+1), Polynomial.monomial j (b j)

/-- The retained reduced-to-full divisor, evaluated at M=exp(u). -/
def meridianDivisor : PowerSeries ℂ :=
  exponential (PowerSeries.X : PowerSeries ℂ) - exponential (-PowerSeries.X)

theorem meridianDivisor_linear : PowerSeries.coeff 1 meridianDivisor = 2 := by
  have hp := exponential_linear_coeff (R := ℂ) 1 1
  have hn := exponential_linear_coeff (R := ℂ) (-1) 1
  simp only [one_smul] at hp
  simp only [neg_one_smul] at hn
  norm_num [meridianDivisor, hp, hn]

theorem meridianDivisor_ne_zero : meridianDivisor ≠ 0 := by
  intro h
  have hc := meridianDivisor_linear
  rw [h] at hc
  norm_num at hc

theorem projected_shiftedEquation (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0) :
    atHZero (shiftedEquation r a S A) =
      ∑ j ∈ Finset.range (r+1), atHZero (a j) *
        exponential (PowerSeries.derivative ℂ S) ^ j := by
  rw [← hZeroHom_apply]
  simp only [shiftedEquation, map_sum, map_mul, hZeroHom_apply,
    logarithmic_exponential_atHZero_nat S A _ hS]

/-- The meridian factor is cancelled inside the proved identity. It is not
dropped from the finite operator as a normalization convention. -/
theorem classical_identity_of_shifted_zero (r : ℕ)
    (a : ℕ → MvPowerSeries (Fin 2) ℂ) (b : ℕ → PowerSeries ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (hc : ∀ j ≤ r, atHZero (a j) = meridianDivisor ^ r * ((-1) ^ j * b j))
    (hz : shiftedEquation r a S A = 0) :
    (classicalPolynomial r b).eval (-exponential (PowerSeries.derivative ℂ S)) = 0 := by
  have hp : (∑ j ∈ Finset.range (r+1), atHZero (a j) *
      exponential (PowerSeries.derivative ℂ S) ^ j) = 0 := by
    rw [← projected_shiftedEquation r a S A hS, hz, ← hZeroHom_apply, map_zero]
  have he : meridianDivisor ^ r *
      (classicalPolynomial r b).eval (-exponential (PowerSeries.derivative ℂ S)) = 0 := by
    calc
      _ = ∑ j ∈ Finset.range (r+1), atHZero (a j) *
          exponential (PowerSeries.derivative ℂ S) ^ j := by
        simp only [classicalPolynomial, Polynomial.eval_finsetSum,
          Polynomial.eval_monomial, Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j hj
        rw [hc j (by have := Finset.mem_range.mp hj; omega)]
        rw [neg_pow]
        ring
      _ = 0 := hp
  exact (mul_eq_zero.mp he).resolve_left (pow_ne_zero r meridianDivisor_ne_zero)

variable {ι : Type*} {l : Filter ι} [NeBot l]

/-- An actual all-orders expansion of the regraded equation, on infinitely
many parameters, recovers the whole bivariate formal identity. -/
theorem regraded_asymptotics_force_zero (B : MvPowerSeries (Fin 2) ℂ)
    {F : ℂ → ι → ℂ} {h : ι → ℂ} {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ s ∈ D, ∀ᶠ n in l, F s n = 0)
    (ho : ∀ s ∈ D, ∀ m : ℕ,
      (fun n => F s n - ∑ i ∈ Finset.range (m+1),
        (PowerSeries.coeff i (regrading B)).eval s * h n ^ i)
        =O[l] (fun n => h n ^ (m+1))) : B = 0 := by
  apply (regrading_zero_iff B).mp
  exact formal_series_zero (regrading B) hD ht hn hz ho

/-- The full conditional characteristic implication, retaining the exact
meridian divisor and sign. It assumes the written identification of the
finite equation's expansion with these formal coefficients. -/
theorem classical_identity_from_all_orders (r : ℕ)
    (a : ℕ → MvPowerSeries (Fin 2) ℂ) (b : ℕ → PowerSeries ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (hc : ∀ j ≤ r, atHZero (a j) = meridianDivisor ^ r * ((-1) ^ j * b j))
    {F : ℂ → ι → ℂ} {h : ι → ℂ} {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ s ∈ D, ∀ᶠ n in l, F s n = 0)
    (ho : ∀ s ∈ D, ∀ m : ℕ,
      (fun n => F s n - ∑ i ∈ Finset.range (m+1),
        (PowerSeries.coeff i (regrading (shiftedEquation r a S A))).eval s * h n ^ i)
        =O[l] (fun n => h n ^ (m+1))) :
    (classicalPolynomial r b).eval (-exponential (PowerSeries.derivative ℂ S)) = 0 := by
  apply classical_identity_of_shifted_zero r a b S A hS hc
  exact regraded_asymptotics_force_zero _ hD ht hn hz ho

/-- For the explicitly constructed gauge coefficients, the meridian factor
and sign are proved by FormalGauge rather than supplied as an extra premise. -/
theorem gauged_classical_identity_from_all_orders (r : ℕ)
    (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    {F : ℂ → ι → ℂ} {h : ι → ℂ} {D : Set ℂ} (hD : D.Infinite)
    (ht : Tendsto h l (𝓝 0)) (hn : ∀ᶠ n in l, h n ≠ 0)
    (hz : ∀ s ∈ D, ∀ᶠ n in l, F s n = 0)
    (ho : ∀ s ∈ D, ∀ m : ℕ,
      (fun n => F s n - ∑ i ∈ Finset.range (m+1),
        (PowerSeries.coeff i (regrading
          (shiftedEquation r (FormalGauge.clearedCoefficient r a) S A))).eval s * h n ^ i)
        =O[l] (fun n => h n ^ (m+1))) :
    (classicalPolynomial r (fun j => atHZero (a j))).eval
      (-exponential (PowerSeries.derivative ℂ S)) = 0 := by
  apply classical_identity_from_all_orders r (FormalGauge.clearedCoefficient r a)
    (fun j => atHZero (a j)) S A hS ?_ hD ht hn hz ho
  intro j hj
  simpa only [meridianDivisor, FormalGauge.meridian] using
    FormalGauge.atHZero_clearedCoefficient r a j hj

end VolumeLogic.FormalCharacteristic
