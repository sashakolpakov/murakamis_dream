import RecurrenceGaugeExpansion
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecificLimits.Basic

noncomputable section
open Filter Asymptotics
open scoped Topology
namespace VolumeLogic.RecurrenceExpansion
open FormalShift FormalExp FormalRegradingRing

def parameterVariables (s : ℂ) : Fin 2 → PowerSeries ℂ :=
  ![PowerSeries.X, PowerSeries.C s * PowerSeries.X]

theorem parameterVariables_hasSubst (s : ℂ) :
    MvPowerSeries.HasSubst (parameterVariables s) :=
  MvPowerSeries.hasSubst_of_constantCoeff_zero (fun i => by
    fin_cases i <;> simp [parameterVariables, PowerSeries.X])

theorem microscopic_eq_subst (s : ℂ) (B : MvPowerSeries (Fin 2) ℂ) :
    microscopic s B = MvPowerSeries.subst (parameterVariables s) B := by
  letI : Algebra (Polynomial ℂ) ℂ := (Polynomial.evalRingHom s).toAlgebra
  letI : IsScalarTower ℂ (Polynomial ℂ) ℂ :=
    IsScalarTower.of_algebraMap_eq (fun x => by
      change x = (Polynomial.evalRingHom s) (Polynomial.C x)
      simp)
  change PowerSeries.map (algebraMap (Polynomial ℂ) ℂ) (regrading B) = _
  rw [PowerSeries.map_algebraMap_eq_subst_X, regrading,
    MvPowerSeries.substAlgHom_apply, PowerSeries.subst_def]
  rw [MvPowerSeries.subst_comp_subst_apply targetVariables_hasSubst
    (PowerSeries.HasSubst.const (PowerSeries.HasSubst.of_constantCoeff_zero
      (show PowerSeries.constantCoeff (PowerSeries.X : PowerSeries ℂ) = 0 by simp)))]
  congr 1
  funext i
  change PowerSeries.subst (PowerSeries.X : PowerSeries ℂ) (targetVariables i) = _
  rw [← PowerSeries.map_algebraMap_eq_subst_X]
  have hx : algebraMap (Polynomial ℂ) ℂ Polynomial.X = s := by
    change (Polynomial.evalRingHom s) Polynomial.X = s
    simp
  fin_cases i <;> simp [targetVariables, parameterVariables, hx]

/-- Regrading followed by parameter evaluation commutes with the actual
formal factorial exponential on admissible arguments. -/
theorem microscopic_exponential (s : ℂ) (B : MvPowerSeries (Fin 2) ℂ)
    (hB : MvPowerSeries.constantCoeff B = 0) :
    microscopic s (exponential B) = exponential (microscopic s B) := by
  simp only [microscopic_eq_subst, exponential, PowerSeries.subst_def]
  rw [MvPowerSeries.subst_comp_subst_apply
    (PowerSeries.HasSubst.const (PowerSeries.HasSubst.of_constantCoeff_zero hB))
    (parameterVariables_hasSubst s)]

theorem microscopic_shiftArgument (s j : ℂ) :
    microscopic s (shiftArgument j) = (s+j) • (PowerSeries.X : PowerSeries ℂ) := by
  rw [microscopic_eq_subst, shiftArgument,
    MvPowerSeries.subst_add (parameterVariables_hasSubst s),
    MvPowerSeries.subst_mul (parameterVariables_hasSubst s),
    MvPowerSeries.subst_X (parameterVariables_hasSubst s),
    MvPowerSeries.subst_X (parameterVariables_hasSubst s), MvPowerSeries.subst_C]
  simp [parameterVariables, PowerSeries.smul_eq_C_mul, add_mul, PowerSeries.C_apply]

theorem microscopic_shiftedMeridian (s : ℂ) (j : ℕ) :
    microscopic s (FormalGauge.shiftedMeridian j) =
      exponential ((s+j) • (PowerSeries.X : PowerSeries ℂ)) -
      exponential ((-(s+j)) • (PowerSeries.X : PowerSeries ℂ)) := by
  have hp : MvPowerSeries.constantCoeff (shiftArgument (j : ℂ)) = 0 := by
    simp [shiftArgument]
  have hn : MvPowerSeries.constantCoeff (-shiftArgument (j : ℂ)) = 0 := by
    simp [hp]
  rw [FormalGauge.shiftedMeridian, map_sub, microscopic_exponential s _ hp,
    microscopic_exponential s _ hn, map_neg, microscopic_shiftArgument]
  simp only [neg_smul]


variable {ι : Type*} {l : Filter ι} {h : ι → ℂ}

/-- The elementary analytic exponential has its actual factorial formal
series at every order, for any complex scale tending to zero. -/
theorem hasExpansion_exp_linear (z : ℂ) (ht : Tendsto h l (𝓝 0)) :
    HasExpansion l h (fun n => Complex.exp (z * h n))
      (FormalExp.exponential (z • (PowerSeries.X : PowerSeries ℂ))) := by
  intro m
  have hz : Tendsto (fun n => z * h n) l (𝓝 0) := by
    simpa using tendsto_const_nhds.mul ht
  have ho := (Complex.exp_sub_sum_range_isBigO_pow (m+1)).comp_tendsto hz
  have hb : (fun n => (z * h n)^(m+1)) =O[l] (fun n => h n^(m+1)) := by
    simpa only [mul_pow] using
      (isBigO_const_mul_self (z^(m+1)) (fun n => h n^(m+1)) l)
  have hh := ho.trans hb
  simpa [trunc_eval, FormalExp.exponential_linear_coeff, div_eq_mul_inv,
    Function.comp_def, mul_pow, mul_assoc, mul_left_comm, mul_comm] using hh

theorem HasExpansion.sub {f g : ι → ℂ} {P Q : PowerSeries ℂ}
    (hf : HasExpansion l h f P) (hg : HasExpansion l h g Q) :
    HasExpansion l h (fun n => f n - g n) (P-Q) := by
  intro m
  have hh := (hf m).sub (hg m)
  simp only [map_sub, Polynomial.eval_sub]
  apply hh.congr_left
  intro n
  ring

/-- The elementary meridian divisor has the difference of the two full
exponential series, including every odd term and every vanished even term. -/
theorem hasExpansion_meridian_linear (z : ℂ) (ht : Tendsto h l (𝓝 0)) :
    HasExpansion l h (fun n => Complex.exp (z*h n) - Complex.exp (-z*h n))
      (FormalExp.exponential (z • (PowerSeries.X : PowerSeries ℂ)) -
        FormalExp.exponential ((-z) • (PowerSeries.X : PowerSeries ℂ))) :=
  (hasExpansion_exp_linear z ht).sub (hasExpansion_exp_linear (-z) ht)


/-- The actual microscopic parameter at the Nth root, h=pi*i/N. -/
def levelScale (N : ℕ) : ℂ := (Real.pi : ℂ) * Complex.I / N

theorem levelScale_tendsto (N : ι → ℕ) (hN : Tendsto N l atTop) :
    Tendsto (fun n => levelScale (N n)) l (𝓝 0) := by
  have hh := (tendsto_inv_atTop_nhds_zero_nat (𝕜 := ℂ)).comp hN
  simpa [levelScale, div_eq_mul_inv] using
    tendsto_const_nhds.mul hh

theorem levelScale_eventually_ne_zero (N : ι → ℕ) (hN : Tendsto N l atTop) :
    ∀ᶠ n in l, levelScale (N n) ≠ 0 := by
  filter_upwards [hN.eventually (eventually_ge_atTop 1)] with n hn
  apply div_ne_zero
  · exact mul_ne_zero (by exact_mod_cast Real.pi_ne_zero) Complex.I_ne_zero
  · exact_mod_cast (show N n ≠ 0 by omega)

/-- The exact sine divisor has the elementary exponential expansion on the
physical root-of-unity scale, without a separate meridian-factor estimate. -/
theorem sineMeridian_linear_expansion (N : ι → ℕ) (hN : Tendsto N l atTop)
    (s : ℂ) (j : ℕ) :
    HasExpansion l (fun n => levelScale (N n))
      (fun n => ActualGauge.sineMeridian (N n) s j)
      (FormalExp.exponential ((s+j) • (PowerSeries.X : PowerSeries ℂ)) -
        FormalExp.exponential ((-(s+j)) • (PowerSeries.X : PowerSeries ℂ))) := by
  have he : (fun n => ActualGauge.sineMeridian (N n) s j) =
      (fun n => Complex.exp ((s+j)*levelScale (N n)) -
        Complex.exp (-(s+j)*levelScale (N n))) := by
    funext n
    rw [ActualGauge.sineMeridian_eq_exp]
    congr 1 <;> congr 1 <;> dsimp [levelScale] <;> ring
  rw [he]
  exact hasExpansion_meridian_linear (s+j) (levelScale_tendsto N hN)

/-- The literal root-of-unity meridian factor matches the specialized formal
factor, with its expansion proved rather than supplied as an application input. -/
theorem sineMeridian_expansion (N : ι → ℕ) (hN : Tendsto N l atTop)
    (s : ℂ) (j : ℕ) :
    HasExpansion l (fun n => levelScale (N n))
      (fun n => ActualGauge.sineMeridian (N n) s j)
      (microscopic s (FormalGauge.shiftedMeridian j)) := by
  rw [microscopic_shiftedMeridian]
  exact sineMeridian_linear_expansion N hN s j

/-- The finite recurrence at actual roots, on any cofinal sequence of levels,
forces the classical identity. The meridian-factor expansion, exact sine
gauge, cleared coefficient expansion and whole finite expansion are proved.
The two analytic premises left are the original coefficient expansions and
the actual source-ratio expansions; the original recurrence is still an input. -/
theorem characteristic_at_roots [NeBot l]
    (r : ℕ) (a : ℕ → MvPowerSeries (Fin 2) ℂ)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (N : ι → ℕ) (hN : Tendsto N l atTop)
    (c F Z : ℂ → ℕ → ι → ℂ) (scale : ℂ → ι → ℂ)
    {D : Set ℂ} (hD : D.Infinite) (hDnr : ∀ s ∈ D, s.im ≠ 0)
    (hs : ∀ s ∈ D, ∀ᶠ n in l, scale s n ≠ 0)
    (hZ : ∀ s ∈ D, ∀ᶠ n in l, Z s 0 n ≠ 0)
    (hF : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j ≤ r, F s j n = scale s n * ActualGauge.sineNormalization (N n) (s+j) * Z s j n)
    (he : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1), c s j n * F s j n = 0)
    (hc : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l (fun n => levelScale (N n))
      (c s j) (microscopic s (a j)))
    (hv : ∀ s ∈ D, ∀ j ≤ r, HasExpansion l (fun n => levelScale (N n))
      (fun n => Z s j n / Z s 0 n)
      (microscopic s (FormalExp.exponential (FormalShift.logarithmicShift S A (j : ℂ))))) :
    (FormalCharacteristic.classicalPolynomial r (fun j => FormalShift.atHZero (a j))).eval
      (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  apply characteristic_of_sine_recurrence r a S A hS N c F Z scale hD hDnr
    (levelScale_tendsto N hN) (levelScale_eventually_ne_zero N hN) ?_
    hs hZ hF he hc ?_ hv
  · filter_upwards [hN.eventually (eventually_ge_atTop 1)] with n hn
    exact_mod_cast (show N n ≠ 0 by omega)
  · intro s _ j _
    exact sineMeridian_expansion N hN s j

end VolumeLogic.RecurrenceExpansion
