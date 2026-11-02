import FormalShift
import Mathlib.RingTheory.PowerSeries.Exp

/-!
# Formal exponential projection

`exponential B` composes Mathlib's factorial power series with B. The theorems
establish the zero-constant admissibility hypothesis explicitly; the raw
function is not interpreted as an exponential on inadmissible arguments.

Over any commutative Q-algebra the actual h=0 algebra homomorphism commutes
with this construction. Applied to FormalShift's logarithmic difference,
it gives exp(j*S'(u)); for natural j this equals (exp S'(u))^j. No analytic
expansion, Laurent regrading, physical operator or longitude identification
is inferred here. The parameter S corresponds to the paper's regraded
principal action mathcalS, not its unrescaled stationary action.
-/
noncomputable section
namespace VolumeLogic.FormalExp
open PowerSeries MvPowerSeries
open VolumeLogic.FormalShift
variable {R : Type*} [CommRing R] [Algebra ℚ R]

/-- The exponential series composed with a possibly multivariate argument.
All theorems below explicitly establish admissibility of the argument. -/
def exponential {σ : Type*} (B : MvPowerSeries σ R) : MvPowerSeries σ R :=
  (PowerSeries.exp R).subst B

theorem exponential_coeff {σ : Type*} (B : MvPowerSeries σ R)
    (hB : MvPowerSeries.constantCoeff B = 0) (e : σ →₀ ℕ) :
    MvPowerSeries.coeff e (exponential B) =
      finsum (fun n : ℕ => algebraMap ℚ R (1 / (n.factorial : ℚ)) *
        MvPowerSeries.coeff e (B ^ n)) := by
  simp [exponential, PowerSeries.coeff_subst
    (PowerSeries.HasSubst.of_constantCoeff_zero hB), PowerSeries.coeff_exp]

theorem exponential_coeff_finite {σ : Type*} (B : MvPowerSeries σ R)
    (hB : MvPowerSeries.constantCoeff B = 0) (e : σ →₀ ℕ) :
    (fun n : ℕ => algebraMap ℚ R (1 / (n.factorial : ℚ)) *
      MvPowerSeries.coeff e (B ^ n)).HasFiniteSupport := by
  simpa using PowerSeries.coeff_subst_finite
    (PowerSeries.HasSubst.of_constantCoeff_zero hB) (PowerSeries.exp R) e

omit [Algebra ℚ R] in
theorem atHZero_constant (B : MvPowerSeries (Fin 2) R) :
    PowerSeries.constantCoeff (atHZero B) = MvPowerSeries.constantCoeff B := by
  simp [atHZero, bc, index, MvPowerSeries.coeff_zero_eq_constantCoeff]

theorem exponential_constant {σ : Type*} (B : MvPowerSeries σ R)
    (hB : MvPowerSeries.constantCoeff B = 0) :
    MvPowerSeries.constantCoeff (exponential B) = 1 := by
  rw [exponential, PowerSeries.constantCoeff_subst
    (PowerSeries.HasSubst.of_constantCoeff_zero hB)]
  rw [finsum_eq_single _ 0]
  · simp
  · intro n hn
    simp [map_pow, hB, zero_pow hn]

theorem exponential_isUnit {σ : Type*} (B : MvPowerSeries σ R)
    (hB : MvPowerSeries.constantCoeff B = 0) : IsUnit (exponential B) := by
  apply MvPowerSeries.isUnit_iff_constantCoeff.mpr
  rw [exponential_constant B hB]
  exact isUnit_one

theorem exponential_zero {σ : Type*} :
    exponential (0 : MvPowerSeries σ R) = 1 := by
  simp [exponential, PowerSeries.subst_zero_eq_C_constantCoeff]

omit [Algebra ℚ R] in
/-- Evaluation h=0, as an actual bundled algebra homomorphism. -/
def hZeroHom : MvPowerSeries (Fin 2) R →ₐ[R] PowerSeries R :=
  MvPowerSeries.substAlgHom zeroVariables_hasSubst

omit [Algebra ℚ R] in
theorem hZeroHom_apply (B : MvPowerSeries (Fin 2) R) :
    hZeroHom B = atHZero B := by
  rw [hZeroHom, MvPowerSeries.substAlgHom_apply, ← atHZero_eq_subst]

/-- Evaluation h=0 commutes with the actual formal exponential. -/
theorem atHZero_exponential (B : MvPowerSeries (Fin 2) R)
    (hB : MvPowerSeries.constantCoeff B = 0) :
    atHZero (exponential B) = exponential (atHZero B) := by
  simp only [exponential, atHZero_eq_subst, PowerSeries.subst_def]
  rw [MvPowerSeries.subst_comp_subst_apply
    (PowerSeries.HasSubst.const (PowerSeries.HasSubst.of_constantCoeff_zero hB))
    zeroVariables_hasSubst]

omit [Algebra ℚ R] in
/-- The full regular amplitude has no leading exponential factor. -/
theorem regularDifference_atHZero (A : MvPowerSeries (Fin 2) R) (j : R) :
    atHZero (shiftRegular A j - A) = 0 := by
  rw [atHZero_eq_subst, MvPowerSeries.subst_sub zeroVariables_hasSubst,
    ← atHZero_eq_subst, ← atHZero_eq_subst, shiftRegular_atHZero, sub_self]

omit [Algebra ℚ R] in
theorem regularDifference_origin (A : MvPowerSeries (Fin 2) R) (j : R) :
    MvPowerSeries.constantCoeff (shiftRegular A j - A) = 0 := by
  have h := congrArg (PowerSeries.coeff 0) (regularDifference_atHZero A j)
  simpa [atHZero, bc, index, MvPowerSeries.coeff_zero_eq_constantCoeff] using h

theorem regular_exponential_atHZero (A : MvPowerSeries (Fin 2) R) (j : R) :
    atHZero (exponential (shiftRegular A j - A)) = 1 := by
  rw [atHZero_exponential _ (regularDifference_origin A j),
    regularDifference_atHZero, exponential_zero]

theorem exponential_linear_coeff (c : R) (n : ℕ) :
    PowerSeries.coeff n (exponential (c • (PowerSeries.X : PowerSeries R))) =
      c ^ n * algebraMap ℚ R (1 / (n.factorial : ℚ)) := by
  rw [exponential, ← PowerSeries.rescale_eq_subst]
  simp [PowerSeries.coeff_rescale]

/-- The formal version of the leading shift ratio after logarithmic regrading. -/
theorem logarithmic_exponential_atHZero (S : PowerSeries R)
    (A : MvPowerSeries (Fin 2) R) (j : R)
    (hS : PowerSeries.coeff 1 S = 0) :
    atHZero (exponential (logarithmicShift S A j)) =
      exponential (j • PowerSeries.derivative R S) := by
  rw [atHZero_exponential _ (logarithmicShift_origin S A j hS),
    logarithmicShift_atHZero]

theorem logarithmic_exponential_amplitude_independent (S : PowerSeries R)
    (A A' : MvPowerSeries (Fin 2) R) (j : R)
    (hS : PowerSeries.coeff 1 S = 0) :
    atHZero (exponential (logarithmicShift S A j)) =
      atHZero (exponential (logarithmicShift S A' j)) := by
  rw [logarithmic_exponential_atHZero S A j hS,
    logarithmic_exponential_atHZero S A' j hS]

theorem logarithmic_exponential_isUnit (S : PowerSeries R)
    (A : MvPowerSeries (Fin 2) R) (j : R)
    (hS : PowerSeries.coeff 1 S = 0) :
    IsUnit (exponential (logarithmicShift S A j)) :=
  exponential_isUnit _ (logarithmicShift_origin S A j hS)

/-- The natural-shift functional equation is inherited from the actual
factorial exponential series, then transported by admissible substitution. -/
theorem exponential_nat_smul {σ : Type*} (B : MvPowerSeries σ R)
    (hB : MvPowerSeries.constantCoeff B = 0) (n : ℕ) :
    exponential ((n : R) • B) = exponential B ^ n := by
  have hb := PowerSeries.HasSubst.of_constantCoeff_zero hB
  rw [exponential, exponential, ← PowerSeries.subst_pow hb,
    PowerSeries.exp_pow_eq_rescale_exp, PowerSeries.rescale_eq_subst]
  rw [PowerSeries.subst_comp_subst_apply
    (PowerSeries.HasSubst.of_constantCoeff_zero' (by simp)) hb]
  rw [PowerSeries.subst_smul hb, PowerSeries.subst_X hb]

theorem logarithmic_exponential_atHZero_nat (S : PowerSeries R)
    (A : MvPowerSeries (Fin 2) R) (n : ℕ)
    (hS : PowerSeries.coeff 1 S = 0) :
    atHZero (exponential (logarithmicShift S A (n : R))) =
      exponential (PowerSeries.derivative R S) ^ n := by
  rw [logarithmic_exponential_atHZero S A (n : R) hS]
  apply exponential_nat_smul
  change PowerSeries.constantCoeff (PowerSeries.derivative R S) = 0
  rw [← PowerSeries.coeff_zero_eq_constantCoeff, PowerSeries.coeff_derivative]
  simp [hS]

end VolumeLogic.FormalExp
