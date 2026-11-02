import Mathlib.RingTheory.PowerSeries.Derivative
import Mathlib.RingTheory.MvPowerSeries.Rename
import Mathlib.Tactic.FinCases

/-!
# The logarithmic shift of a filtered meridian expansion

Variables 0 and 1 are h and u. The actual formal substitution S(u+jh)
has an exactly divisible difference S(u+jh)-S(u). After division by h,
its constant h coefficient is j*S'(u). An arbitrary regular bivariate
amplitude A(h,u) contributes zero to this coefficient under the same shift.

This optional Mathlib module does not enlarge the Std-only FormalRegrading
library. It does not construct the formal exponential, identify S or A with
an analytic source expansion, or assert an equation for a physical operator.
-/

noncomputable section
namespace VolumeLogic.FormalShift
open PowerSeries MvPowerSeries
variable {R : Type*} [CommRing R]

def index (a b : ℕ) : Fin 2 →₀ ℕ :=
  Finsupp.single 0 a + Finsupp.single 1 b

@[simp]
theorem index_zero (a b : ℕ) : index a b 0 = a := by simp [index]
@[simp]
theorem index_one (a b : ℕ) : index a b 1 = b := by simp [index]

def bc (F : MvPowerSeries (Fin 2) R) (a b : ℕ) : R := MvPowerSeries.coeff (index a b) F

def shiftArgument (j : R) : MvPowerSeries (Fin 2) R :=
  MvPowerSeries.X 1 + MvPowerSeries.C j * MvPowerSeries.X 0

theorem argument_hasSubst (j : R) : PowerSeries.HasSubst (shiftArgument j) :=
  PowerSeries.HasSubst.of_constantCoeff_zero (by simp [shiftArgument])

def shiftPrincipal (S : PowerSeries R) (j : R) : MvPowerSeries (Fin 2) R :=
  S.subst (shiftArgument j)

-- The same substitution obtained by rescaling h after the ordinary binomial sum.
theorem shiftPrincipal_rescale (S : PowerSeries R) (j : R) :
    shiftPrincipal S j =
      MvPowerSeries.rescale ![j, 1] (S.subst (MvPowerSeries.X 0 + MvPowerSeries.X 1)) := by
  rw [MvPowerSeries.rescale_eq_subst]
  rw [PowerSeries.subst_def]
  rw [MvPowerSeries.subst_comp_subst_apply
    (MvPowerSeries.hasSubst_of_constantCoeff_zero (fun _ => by simp))
    (MvPowerSeries.HasSubst.smul_X ![j, 1])]
  unfold shiftPrincipal
  rw [PowerSeries.subst_def]
  congr 1
  funext i
  simp [shiftArgument, MvPowerSeries.subst_add,
    MvPowerSeries.HasSubst.smul_X, MvPowerSeries.subst_X]
  rw [MvPowerSeries.smul_eq_C_mul, add_comm]

theorem shiftPrincipal_coeff (S : PowerSeries R) (j : R) (a b : ℕ) :
    bc (shiftPrincipal S j) a b =
      j ^ a * ((a + b).choose a : R) * PowerSeries.coeff (a + b) S := by
  rw [shiftPrincipal_rescale]
  unfold bc
  rw [MvPowerSeries.coeff_rescale, PowerSeries.coeff_subst_X_zero_add_X_one]
  simp [index, mul_assoc]

@[simp]
theorem bc_sub (F G : MvPowerSeries (Fin 2) R) (a b : ℕ) :
    bc (F-G) a b = bc F a b - bc G a b := by simp [bc]

-- Division by h is a literal coefficient shift, valid when the h^0 coefficient vanishes.
def divideH (F : MvPowerSeries (Fin 2) R) : MvPowerSeries (Fin 2) R := fun e =>
  MvPowerSeries.coeff (e + Finsupp.single 0 1) F

@[simp]
theorem divideH_coeff (F : MvPowerSeries (Fin 2) R) (a b : ℕ) :
    bc (divideH F) a b = bc F (a+1) b := by
  change MvPowerSeries.coeff (index a b + Finsupp.single 0 1) F = _
  have hi : index a b + Finsupp.single 0 1 = index (a+1) b := by
    ext i
    fin_cases i <;> simp [index]
  rw [hi]
  rfl

def principalDifference (S : PowerSeries R) (j : R) : MvPowerSeries (Fin 2) R :=
  shiftPrincipal S j - shiftPrincipal S 0

@[simp]
theorem principalDifference_zero (S : PowerSeries R) (j : R) (b : ℕ) :
    bc (principalDifference S j) 0 b = 0 := by
  simp [principalDifference, shiftPrincipal_coeff]

theorem principalDifference_first (S : PowerSeries R) (j : R) (b : ℕ) :
    bc (divideH (principalDifference S j)) 0 b =
      j * PowerSeries.coeff b (PowerSeries.derivative R S) := by
  rw [divideH_coeff]
  simp [principalDifference, shiftPrincipal_coeff,
    PowerSeries.coeff_derivative, Nat.add_comm, mul_assoc, mul_comm]

theorem principalDifference_division (S : PowerSeries R) (j : R) :
    MvPowerSeries.X 0 * divideH (principalDifference S j) =
      principalDifference S j := by
  apply MvPowerSeries.ext
  intro e
  have he : e = index (e 0) (e 1) := by
    ext i
    fin_cases i <;> simp [index]
  rw [he]
  generalize e 0 = a
  generalize e 1 = b
  cases a with
  | zero =>
    have hn : ¬ Finsupp.single (0 : Fin 2) 1 ≤ index 0 b := by
      intro hh
      have := hh 0
      simp [index] at this
    rw [MvPowerSeries.X, MvPowerSeries.coeff_monomial_mul, if_neg hn]
    exact (principalDifference_zero S j b).symm
  | succ a =>
    have hi : index (a+1) b = Finsupp.single 0 1 + index a b := by
      ext i
      fin_cases i <;> simp [index, Nat.add_comm]
    rw [hi, MvPowerSeries.X, MvPowerSeries.coeff_add_monomial_mul, one_mul]
    change bc (divideH (principalDifference S j)) a b = _
    rw [divideH_coeff]
    simp only [bc, hi]

/-- The literal coefficient of h^0, retaining the whole formal u series. -/
def atHZero (F : MvPowerSeries (Fin 2) R) : PowerSeries R := PowerSeries.mk (bc F 0)

theorem principalDifference_symbol (S : PowerSeries R) (j : R) :
    atHZero (divideH (principalDifference S j)) =
      j • PowerSeries.derivative R S := by
  apply PowerSeries.ext
  intro b
  simpa [atHZero] using principalDifference_first S j b

-- Joint-origin vanishing supplies the zero-constant condition for a later
-- formal-exponential construction over a suitable rational algebra.
theorem principalDifference_origin (S : PowerSeries R) (j : R)
    (hS : PowerSeries.coeff 1 S = 0) :
    MvPowerSeries.constantCoeff (divideH (principalDifference S j)) = 0 := by
  have h := principalDifference_first S j 0
  simpa [bc, index, PowerSeries.coeff_derivative, hS,
    MvPowerSeries.coeff_zero_eq_constantCoeff] using h


/-- The actual substitution h=0, u=X. -/
def zeroVariables : Fin 2 → PowerSeries R := ![0, PowerSeries.X]

theorem zeroVariables_hasSubst : MvPowerSeries.HasSubst (zeroVariables (R := R)) :=
  MvPowerSeries.hasSubst_of_constantCoeff_zero (fun i => by
    fin_cases i <;> simp [zeroVariables, PowerSeries.X])

theorem atHZero_eq_subst (F : MvPowerSeries (Fin 2) R) :
    atHZero F = MvPowerSeries.subst zeroVariables F := by
  apply PowerSeries.ext
  intro b
  rw [atHZero, PowerSeries.coeff_mk]
  change bc F 0 b = MvPowerSeries.coeff (Finsupp.single () b)
    (MvPowerSeries.subst zeroVariables F)
  rw [MvPowerSeries.coeff_subst zeroVariables_hasSubst]
  symm
  rw [finsum_eq_single _ (index 0 b)]
  · simp [Finsupp.prod_fintype, zeroVariables, index, bc]
  · intro e he
    rw [Finsupp.prod_fintype _ _ (fun _ => by simp)]
    simp only [Fin.prod_univ_two, zeroVariables, Matrix.cons_val_zero,
      Matrix.cons_val_one]
    by_cases h0 : e 0 = 0
    · have h1 : e 1 ≠ b := by
        intro hh
        apply he
        ext i
        fin_cases i <;> simp [index, h0, hh]
      simp [h0, PowerSeries.coeff_X_pow, Ne.symm h1]
    · simp [zero_pow h0]

/-- A regular two-variable logarithmic amplitude after s -> s+j. -/
def shiftVariables (j : R) : Fin 2 → MvPowerSeries (Fin 2) R :=
  ![MvPowerSeries.X 0, shiftArgument j]

theorem shiftVariables_hasSubst (j : R) : MvPowerSeries.HasSubst (shiftVariables j) :=
  MvPowerSeries.hasSubst_of_constantCoeff_zero (fun i => by
    fin_cases i <;> simp [shiftVariables, shiftArgument])

def shiftRegular (A : MvPowerSeries (Fin 2) R) (j : R) : MvPowerSeries (Fin 2) R :=
  MvPowerSeries.subst (shiftVariables j) A

theorem shiftRegular_atHZero (A : MvPowerSeries (Fin 2) R) (j : R) :
    atHZero (shiftRegular A j) = atHZero A := by
  simp only [atHZero_eq_subst, shiftRegular]
  rw [MvPowerSeries.subst_comp_subst_apply (shiftVariables_hasSubst j)
    zeroVariables_hasSubst]
  congr 1
  funext i
  fin_cases i
  · change MvPowerSeries.subst zeroVariables (MvPowerSeries.X 0) = 0
    rw [MvPowerSeries.subst_X zeroVariables_hasSubst]
    rfl
  · change MvPowerSeries.subst zeroVariables (shiftArgument j) = PowerSeries.X
    rw [shiftArgument, MvPowerSeries.subst_add zeroVariables_hasSubst,
      MvPowerSeries.subst_mul zeroVariables_hasSubst,
      MvPowerSeries.subst_X zeroVariables_hasSubst,
      MvPowerSeries.subst_X zeroVariables_hasSubst]
    simp [zeroVariables]

/-- The full logarithmic shift, including all regular-amplitude coefficients. -/
def logarithmicShift (S : PowerSeries R) (A : MvPowerSeries (Fin 2) R) (j : R) : MvPowerSeries (Fin 2) R :=
  divideH (principalDifference S j) + shiftRegular A j - A

theorem logarithmicShift_atHZero (S : PowerSeries R) (A : MvPowerSeries (Fin 2) R) (j : R) :
    atHZero (logarithmicShift S A j) = j • PowerSeries.derivative R S := by
  unfold logarithmicShift
  simp only [atHZero_eq_subst]
  rw [MvPowerSeries.subst_sub zeroVariables_hasSubst,
    MvPowerSeries.subst_add zeroVariables_hasSubst]
  rw [← atHZero_eq_subst, ← atHZero_eq_subst, ← atHZero_eq_subst,
    shiftRegular_atHZero, add_sub_cancel_right, principalDifference_symbol]

/-- No joint constant term remains when the principal action has no linear
term. This supplies the zero-constant condition for a later formal
exponential over a suitable rational algebra. -/
theorem logarithmicShift_origin (S : PowerSeries R)
    (A : MvPowerSeries (Fin 2) R) (j : R)
    (hS : PowerSeries.coeff 1 S = 0) :
    MvPowerSeries.constantCoeff (logarithmicShift S A j) = 0 := by
  have h := congrArg (PowerSeries.coeff 0) (logarithmicShift_atHZero S A j)
  simpa [atHZero, bc, index, PowerSeries.coeff_derivative, hS,
    MvPowerSeries.coeff_zero_eq_constantCoeff] using h

end VolumeLogic.FormalShift
