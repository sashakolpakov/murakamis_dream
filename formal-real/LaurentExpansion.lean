import MeridianExpansion

/-!
Finite Laurent coefficients evaluated at the physical roots have their
actual formal expansion. Integer exponents may be negative. No coefficient
asymptotic is assumed, and no recurrence operator is constructed here.
-/
noncomputable section
open Filter Asymptotics
open scoped Topology
namespace VolumeLogic.LaurentExpansion
open RecurrenceExpansion

abbrev Coefficient := (ℤ × ℤ) →₀ ℂ

/-- Literal Laurent evaluation in q and M. -/
def evaluate (a : Coefficient) (q M : ℂ) : ℂ :=
  ∑ k ∈ a.support, a k * (q ^ k.1 * M ^ k.2)

/-- The logarithm of q^k M^m after q=exp(h), M=exp(u). -/
def monomialArgument (k : ℤ × ℤ) : MvPowerSeries (Fin 2) ℂ :=
  MvPowerSeries.C (k.1 : ℂ) * MvPowerSeries.X 0 +
  MvPowerSeries.C (k.2 : ℂ) * MvPowerSeries.X 1

/-- The complete bivariate Taylor series of the finite Laurent coefficient. -/
def formalCoefficient (a : Coefficient) : MvPowerSeries (Fin 2) ℂ :=
  ∑ k ∈ a.support, MvPowerSeries.C (a k) *
    FormalExp.exponential (monomialArgument k)

theorem monomialArgument_origin (k : ℤ × ℤ) :
    MvPowerSeries.constantCoeff (monomialArgument k) = 0 := by
  simp [monomialArgument]

theorem microscopic_constant (s c : ℂ) :
    microscopic s (MvPowerSeries.C c) = PowerSeries.C c := by
  rw [microscopic_eq_subst, MvPowerSeries.subst_C]
  rfl

theorem microscopic_monomialArgument (s : ℂ) (k : ℤ × ℤ) :
    microscopic s (monomialArgument k) =
      ((k.1 : ℂ) + (k.2 : ℂ) * s) • (PowerSeries.X : PowerSeries ℂ) := by
  rw [microscopic_eq_subst]
  simp only [monomialArgument,
    MvPowerSeries.subst_add (parameterVariables_hasSubst s),
    MvPowerSeries.subst_mul (parameterVariables_hasSubst s),
    MvPowerSeries.subst_C,
    MvPowerSeries.subst_X (parameterVariables_hasSubst s)]
  simp [parameterVariables, PowerSeries.smul_eq_C_mul, add_mul, mul_assoc]

theorem microscopic_formalCoefficient (s : ℂ) (a : Coefficient) :
    microscopic s (formalCoefficient a) =
      ∑ k ∈ a.support, PowerSeries.C (a k) * FormalExp.exponential
        (((k.1 : ℂ) + (k.2 : ℂ) * s) • (PowerSeries.X : PowerSeries ℂ)) := by
  simp only [formalCoefficient, map_sum, map_mul, microscopic_constant]
  congr 1
  funext k
  rw [microscopic_exponential s _ (monomialArgument_origin k),
    microscopic_monomialArgument]

theorem evaluate_exp (a : Coefficient) (h s : ℂ) :
    evaluate a (Complex.exp h) (Complex.exp (s*h)) =
      ∑ k ∈ a.support, a k * Complex.exp (((k.1 : ℂ)+(k.2 : ℂ)*s)*h) := by
  apply Finset.sum_congr rfl
  intro k _
  rw [← Complex.exp_int_mul, ← Complex.exp_int_mul, ← Complex.exp_add]
  congr 2
  ring

/-- The original q=1 Laurent symbol, expanded only in M=exp(u). -/
def classicalCoefficient (a : Coefficient) : PowerSeries ℂ :=
  ∑ k ∈ a.support, PowerSeries.C (a k) *
    FormalExp.exponential ((k.2 : ℂ) • (PowerSeries.X : PowerSeries ℂ))

theorem project_monomialArgument (k : ℤ × ℤ) :
    FormalShift.atHZero (monomialArgument k) =
      (k.2 : ℂ) • (PowerSeries.X : PowerSeries ℂ) := by
  rw [FormalShift.atHZero_eq_subst]
  simp only [monomialArgument,
    MvPowerSeries.subst_add FormalShift.zeroVariables_hasSubst,
    MvPowerSeries.subst_mul FormalShift.zeroVariables_hasSubst,
    MvPowerSeries.subst_C,
    MvPowerSeries.subst_X FormalShift.zeroVariables_hasSubst]
  simp [FormalShift.zeroVariables, PowerSeries.smul_eq_C_mul]

theorem project_formalCoefficient (a : Coefficient) :
    FormalShift.atHZero (formalCoefficient a) = classicalCoefficient a := by
  rw [← FormalExp.hZeroHom_apply]
  simp only [formalCoefficient, classicalCoefficient, map_sum, map_mul]
  apply Finset.sum_congr rfl
  intro k _
  have hc : FormalExp.hZeroHom (MvPowerSeries.C (a k)) = PowerSeries.C (a k) := by
    rw [FormalExp.hZeroHom_apply, FormalShift.atHZero_eq_subst,
      MvPowerSeries.subst_C]
    rfl
  rw [hc, FormalExp.hZeroHom_apply,
    FormalExp.atHZero_exponential _ (monomialArgument_origin k),
    project_monomialArgument]

theorem evaluate_single (k : ℤ × ℤ) (c q M : ℂ) :
    evaluate (Finsupp.single k c) q M = c * (q^k.1 * M^k.2) := by
  classical
  change (Finsupp.single k c).sum (fun j d => d * (q^j.1 * M^j.2)) = _
  simp

theorem microscopic_single (k : ℤ × ℤ) (c s : ℂ) :
    microscopic s (formalCoefficient (Finsupp.single k c)) =
      PowerSeries.C c * FormalExp.exponential
        (((k.1 : ℂ)+(k.2 : ℂ)*s) • (PowerSeries.X : PowerSeries ℂ)) := by
  classical
  rw [microscopic_formalCoefficient]
  change (Finsupp.single k c).sum (fun j d => PowerSeries.C d *
    FormalExp.exponential (((j.1 : ℂ)+(j.2 : ℂ)*s) •
      (PowerSeries.X : PowerSeries ℂ))) = _
  simp

theorem classicalCoefficient_add (a b : Coefficient) :
    classicalCoefficient (a+b) = classicalCoefficient a + classicalCoefficient b := by
  classical
  let g := fun (j : ℤ × ℤ) (d : ℂ) => PowerSeries.C d *
    FormalExp.exponential ((j.2 : ℂ) • (PowerSeries.X : PowerSeries ℂ))
  change (a+b).sum g = a.sum g + b.sum g
  apply Finsupp.sum_add_index
  · intro _ _
    simp [g]
  · intro _ _
    simp [g, add_mul]

theorem classicalCoefficient_single (k : ℤ × ℤ) (c : ℂ) :
    classicalCoefficient (Finsupp.single k c) =
      PowerSeries.C c * FormalExp.exponential
        ((k.2 : ℂ) • (PowerSeries.X : PowerSeries ℂ)) := by
  classical
  change (Finsupp.single k c).sum (fun j d => PowerSeries.C d *
    FormalExp.exponential ((j.2 : ℂ) • (PowerSeries.X : PowerSeries ℂ))) = _
  simp

variable {ι : Type*} {l : Filter ι} {h : ι → ℂ}

/-- Every coefficient estimate is proved from the finite Laurent support
and the elementary exponential remainder, at every asymptotic order. -/
theorem coefficient_expansion (a : Coefficient) (s : ℂ)
    (ht : Tendsto h l (𝓝 0)) :
    HasExpansion l h
      (fun n => evaluate a (Complex.exp (h n)) (Complex.exp (s*h n)))
      (microscopic s (formalCoefficient a)) := by
  simp only [microscopic_formalCoefficient, evaluate_exp]
  apply HasExpansion.sum
  intro k _
  exact (hasExpansion_const (a k)).mul
    (hasExpansion_exp_linear ((k.1 : ℂ)+(k.2 : ℂ)*s) ht) ht

theorem coefficient_expansion_at_roots (a : Coefficient) (s : ℂ)
    (N : ι → ℕ) (hN : Tendsto N l atTop) :
    HasExpansion l (fun n => levelScale (N n))
      (fun n => evaluate a (Complex.exp (levelScale (N n)))
        (Complex.exp (s*levelScale (N n))))
      (microscopic s (formalCoefficient a)) :=
  coefficient_expansion a s (levelScale_tendsto N hN)

/-- A finite Laurent recurrence needs no additional coefficient-expansion
hypothesis. The original recurrence, actual source normalization, eventual
nonvanishing and source-ratio asymptotics are still explicit inputs. -/
theorem characteristic_of_laurent_recurrence [NeBot l]
    (r : ℕ) (a : ℕ → Coefficient)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (N : ι → ℕ) (hN : Tendsto N l atTop)
    (F Z : ℂ → ℕ → ι → ℂ) (scale : ℂ → ι → ℂ)
    {D : Set ℂ} (hD : D.Infinite) (hDnr : ∀ s ∈ D, s.im ≠ 0)
    (hs : ∀ s ∈ D, ∀ᶠ n in l, scale s n ≠ 0)
    (hZ : ∀ s ∈ D, ∀ᶠ n in l, Z s 0 n ≠ 0)
    (hF : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j ≤ r, F s j n = scale s n *
        ActualGauge.sineNormalization (N n) (s+j) * Z s j n)
    (he : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1),
        evaluate (a j) (Complex.exp (levelScale (N n)))
          (Complex.exp (s*levelScale (N n))) * F s j n = 0)
    (hv : ∀ s ∈ D, ∀ j ≤ r,
      HasExpansion l (fun n => levelScale (N n))
        (fun n => Z s j n / Z s 0 n)
        (microscopic s (FormalExp.exponential
          (FormalShift.logarithmicShift S A (j : ℂ))))) :
    (FormalCharacteristic.classicalPolynomial r
      (fun j => classicalCoefficient (a j))).eval
        (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  have hh := characteristic_at_roots r (fun j => formalCoefficient (a j)) S A hS
    N hN (fun s j n => evaluate (a j) (Complex.exp (levelScale (N n)))
      (Complex.exp (s*levelScale (N n)))) F Z scale hD hDnr hs hZ hF he
      (fun s _ j _ => coefficient_expansion_at_roots (a j) s N hN) hv
  simpa only [project_formalCoefficient] using hh

end VolumeLogic.LaurentExpansion
