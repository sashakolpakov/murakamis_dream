import FormalExp
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Tactic.Ring

/-! Actual finite-product gauge construction. No denominator is
inverted: the clearing identity is a multiplied identity in formal series. -/
noncomputable section
namespace VolumeLogic.FormalGauge
open PowerSeries MvPowerSeries
open FormalShift FormalExp
variable {R : Type*} [CommRing R] [Algebra ℚ R]

/-- The original meridian divisor at the j-th shifted argument. -/
def shiftedMeridian (j : ℕ) : MvPowerSeries (Fin 2) R :=
  exponential (shiftArgument (j : R)) - exponential (-shiftArgument (j : R))

def meridian : PowerSeries R :=
  exponential (PowerSeries.X : PowerSeries R) - exponential (-PowerSeries.X)

def denominator (r : ℕ) : MvPowerSeries (Fin 2) R :=
  ∏ k ∈ Finset.Icc 1 r, shiftedMeridian k

def punctured (r j : ℕ) : MvPowerSeries (Fin 2) R :=
  ∏ k ∈ (Finset.Icc 1 r).erase j, shiftedMeridian k

/-- The zeroth coefficient retains the full denominator product. Every
positive shift replaces only its own denominator by the original f_0. -/
def clearedCoefficient (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) R)
    (j : ℕ) : MvPowerSeries (Fin 2) R :=
  if j = 0 then denominator r * a 0
  else (-1)^j * shiftedMeridian 0 * punctured r j * a j

omit [Algebra ℚ R] in
theorem project_shiftArgument (j : R) :
    hZeroHom (shiftArgument j) = (PowerSeries.X : PowerSeries R) := by
  rw [hZeroHom_apply, atHZero_eq_subst, shiftArgument,
    MvPowerSeries.subst_add zeroVariables_hasSubst,
    MvPowerSeries.subst_mul zeroVariables_hasSubst,
    MvPowerSeries.subst_X zeroVariables_hasSubst,
    MvPowerSeries.subst_X zeroVariables_hasSubst]
  simp [zeroVariables]

theorem project_shiftedMeridian (j : ℕ) :
    hZeroHom (shiftedMeridian (R := R) j) = meridian := by
  have harg : MvPowerSeries.constantCoeff (shiftArgument (j : R)) = 0 := by
    simp [shiftArgument]
  have hneg : MvPowerSeries.constantCoeff (-shiftArgument (j : R)) = 0 := by
    simp [harg]
  rw [shiftedMeridian, map_sub, hZeroHom_apply, atHZero_exponential _ harg,
    ← hZeroHom_apply, project_shiftArgument, hZeroHom_apply,
    atHZero_exponential _ hneg, ← hZeroHom_apply, map_neg, project_shiftArgument]
  rfl

theorem shiftedMeridian_constant (j : ℕ) :
    MvPowerSeries.constantCoeff (shiftedMeridian (R := R) j) = 0 := by
  have hp : MvPowerSeries.constantCoeff (shiftArgument (j : R)) = 0 := by
    simp [shiftArgument]
  have hn : MvPowerSeries.constantCoeff (-shiftArgument (j : R)) = 0 := by
    simp [hp]
  rw [shiftedMeridian, map_sub, exponential_constant _ hp,
    exponential_constant _ hn, sub_self]

theorem meridian_constant : PowerSeries.constantCoeff (meridian (R := R)) = 0 := by
  rw [← project_shiftedMeridian 0, hZeroHom_apply, atHZero_constant,
    shiftedMeridian_constant]

theorem project_denominator (r : ℕ) :
    hZeroHom (denominator (R := R) r) = meridian ^ r := by
  simp [denominator, map_prod, project_shiftedMeridian]

theorem shifted_mul_punctured (r j : ℕ) (hpos : 1 ≤ j) (hjr : j ≤ r) :
    shiftedMeridian (R := R) j * punctured r j = denominator r := by
  exact Finset.mul_prod_erase (Finset.Icc 1 r) shiftedMeridian
    (Finset.mem_Icc.mpr ⟨hpos, hjr⟩)

/-- Actual denominator clearing, also at the unshifted coefficient j=0. -/
theorem denominator_clearing (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) R)
    (j : ℕ) (hjr : j ≤ r) :
    shiftedMeridian j * clearedCoefficient r a j =
      denominator r * (-1)^j * shiftedMeridian 0 * a j := by
  by_cases hj : j = 0
  · subst j
    simp [clearedCoefficient, mul_left_comm, mul_assoc]
  · have hp := shifted_mul_punctured (R := R) r j (by omega) hjr
    rw [clearedCoefficient, if_neg hj, ← hp]
    ring

theorem project_punctured (r j : ℕ) (hpos : 1 ≤ j) (hjr : j ≤ r) :
    hZeroHom (punctured (R := R) r j) = meridian ^ (r-1) := by
  have hm : j ∈ Finset.Icc 1 r := Finset.mem_Icc.mpr ⟨hpos, hjr⟩
  simp [punctured, map_prod, project_shiftedMeridian,
    Finset.card_erase_of_mem hm]

/-- The exact coefficient normalization required by the classical assembler.
No gauge factor is cancelled from the coefficient family. -/
theorem project_clearedCoefficient (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) R)
    (j : ℕ) (hjr : j ≤ r) :
    hZeroHom (clearedCoefficient r a j) =
      meridian ^ r * ((-1)^j * hZeroHom (a j)) := by
  by_cases hj : j = 0
  · subst j
    simp [clearedCoefficient, project_denominator]
  · have hpos : 1 ≤ j := by omega
    have hr : 1 ≤ r := by omega
    have hp : meridian (R := R) * meridian ^ (r-1) = meridian ^ r := by
      rw [← pow_succ', Nat.sub_add_cancel hr]
    simp only [clearedCoefficient, if_neg hj, map_mul, map_pow, map_neg, map_one,
      project_shiftedMeridian, project_punctured r j hpos hjr]
    rw [← hp]
    ring

/-- The same statement in FormalShift's coefficient-projection notation. -/
theorem atHZero_clearedCoefficient (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) R)
    (j : ℕ) (hjr : j ≤ r) :
    atHZero (clearedCoefficient r a j) =
      meridian ^ r * ((-1)^j * atHZero (a j)) := by
  simpa only [hZeroHom_apply] using project_clearedCoefficient r a j hjr

end VolumeLogic.FormalGauge
