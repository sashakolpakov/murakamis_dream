import OperatorNormalization
import LaurentExpansion

noncomputable section
open Filter Asymptotics
open scoped Topology
namespace VolumeLogic.OperatorCoefficientAdapter
open Polynomial OperatorNormalization LaurentExpansion RecurrenceExpansion

/-- The two finite exponents in the polynomial-in-q, Laurent-in-M record. -/
def encode (p : Polynomial (LaurentPolynomial ℂ)) : Coefficient :=
  Finsupp.mapDomain (fun k : ℕ × ℤ => ((k.1 : ℤ), k.2))
    ((p.toFinsupp.coeff.mapRange AddMonoidAlgebra.coeff AddMonoidAlgebra.coeff_zero).uncurry)

theorem encode_coefficient (p : Polynomial (LaurentPolynomial ℂ)) (n : ℕ) (m : ℤ) :
    encode p ((n : ℤ),m) = (p.coeff n).coeff m := by
  have hi : Function.Injective (fun k : ℕ × ℤ => ((k.1 : ℤ), k.2)) := by
    intro x y he
    exact Prod.ext (Int.ofNat_inj.mp (congrArg (fun k : ℤ × ℤ => k.1) he))
      (congrArg (fun k : ℤ × ℤ => k.2) he)
  exact Finsupp.mapDomain_apply hi _ (n,m)

theorem encode_injective : Function.Injective encode := by
  intro p q he
  apply Polynomial.ext
  intro n
  apply LaurentPolynomial.ext
  intro m
  have hc := congrArg (fun a : Coefficient => a ((n : ℤ),m)) he
  simpa only [encode_coefficient] using hc

theorem encode_zero : encode 0 = 0 := by
  have hz : (0 : ℕ →₀ ℤ →₀ ℂ).uncurry = 0 := by ext; rfl
  simp [encode, hz]

/-- Every additive evaluation of the encoded table is the original double
finite sum. This is used for both numerical and formal classical evaluation. -/
theorem encode_sum {A : Type*} [AddCommMonoid A]
    (p : Polynomial (LaurentPolynomial ℂ)) (g : (ℤ × ℤ) → ℂ → A)
    (h0 : ∀ k, g k 0 = 0)
    (ha : ∀ k x y, g k (x+y) = g k x + g k y) :
    (encode p).sum g = p.sum (fun n a => a.coeff.sum (fun m c => g ((n : ℤ),m) c)) := by
  rw [encode, Finsupp.sum_mapDomain_index h0 ha,
    Finsupp.sum_uncurry_index, Finsupp.sum_mapRange_index (by intro n; simp)]
  rfl

theorem meridian_evaluation_sum (a : LaurentPolynomial ℂ) (M : ℂˣ) :
    LaurentPolynomial.eval₂ (RingHom.id ℂ) M a =
      a.coeff.sum (fun m c => c * (M : ℂ)^m) := by
  induction a using LaurentPolynomial.induction_on' with
  | add a b ha hb =>
      rw [map_add, ha, hb, AddMonoidAlgebra.coeff_add]
      exact (Finsupp.sum_add_index (by simp) (by intros; simp [add_mul])).symm
  | C_mul_T m c =>
      rw [LaurentPolynomial.eval₂_C_mul_T, ← LaurentPolynomial.single_eq_C_mul_T]
      rw [AddMonoidAlgebra.coeff_single, Finsupp.sum_single_index (by simp)]
      simp

/-- Numerical evaluation of the encoded coefficient agrees exactly with
polynomial evaluation followed by Laurent meridian evaluation. -/
theorem evaluate_encode (p : Polynomial (LaurentPolynomial ℂ)) (q : ℂ) (M : ℂˣ) :
    evaluate (encode p) q M = p.eval₂ (LaurentPolynomial.eval₂ (RingHom.id ℂ) M) q := by
  change (encode p).sum (fun k c => c * (q^k.1 * (M : ℂ)^k.2)) = _
  rw [encode_sum p _ (by simp) (by intros; simp [add_mul])]
  rw [Polynomial.eval₂_eq_sum]
  apply Finset.sum_congr rfl
  intro n _
  dsimp only
  rw [meridian_evaluation_sum, Finsupp.sum_mul]
  apply Finset.sum_congr rfl
  intro m _
  simp only [zpow_natCast]
  ring

/-- Transpose the q/L record, then take the actual coefficient of L^j. -/
def shiftPolynomial (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (j : ℕ) :
    Polynomial (LaurentPolynomial ℂ) := (Polynomial.Bivariate.swap P).coeff j

def operatorFamily (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (j : ℕ) :
    Coefficient := encode (shiftPolynomial P j)

theorem actualCoefficient_eq_shiftPolynomial {R K : Type*} [CommRing R] [CommRing K]
    (φ : R →+* K) (q : K) (P : Polynomial (Polynomial R)) (j : ℕ) :
    actualCoefficient φ q P j = ((Polynomial.Bivariate.swap P).coeff j).eval₂ φ q := by
  induction P using Polynomial.induction_on' with
  | add P Q hP hQ =>
      simpa [actualCoefficient] using congrArg₂ (· + ·) hP hQ
  | monomial n a =>
      simp only [actualCoefficient, Polynomial.map_monomial, Polynomial.eval_monomial,
        Polynomial.Bivariate.swap_monomial, Polynomial.coeff_mul_C, Polynomial.coeff_map]
      rw [← map_pow (Polynomial.C : K →+* Polynomial K), Polynomial.coeff_mul_C]
      simp

theorem actualCoefficient_eq_evaluate
    (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (q : ℂ) (M : ℂˣ) (j : ℕ) :
    actualCoefficient (LaurentPolynomial.eval₂ (RingHom.id ℂ) M) q P j =
      evaluate (operatorFamily P j) q M := by
  rw [operatorFamily, evaluate_encode, actualCoefficient_eq_shiftPolynomial]
  rfl


/-- The literal M=e^u expansion of a Laurent polynomial, as an additive map.
No injectivity of evaluation on a selected geometric germ is asserted. -/
def meridianSeries : LaurentPolynomial ℂ →+ PowerSeries ℂ where
  toFun a := a.coeff.sum (fun m c => PowerSeries.C c *
    FormalExp.exponential ((m : ℂ) • (PowerSeries.X : PowerSeries ℂ)))
  map_zero' := by simp
  map_add' a b := by
    rw [AddMonoidAlgebra.coeff_add]
    apply Finsupp.sum_add_index
    · intro _ _; simp
    · intro _ _ _ _; simp [add_mul]

theorem classicalCoefficient_encode (p : Polynomial (LaurentPolynomial ℂ)) :
    classicalCoefficient (encode p) = meridianSeries (p.eval 1) := by
  change (encode p).sum (fun k c => PowerSeries.C c *
    FormalExp.exponential ((k.2 : ℂ) • (PowerSeries.X : PowerSeries ℂ))) = _
  rw [encode_sum p _ (by simp) (by intros; simp [add_mul])]
  rw [Polynomial.eval_eq_sum]
  simp only [one_pow, mul_one, Polynomial.sum_def, map_sum]
  rfl

theorem classical_record_coefficient {R : Type*} [CommRing R]
    (P : Polynomial (Polynomial R)) (j : ℕ) :
    (P.eval 1).coeff j = ((Polynomial.Bivariate.swap P).coeff j).eval 1 := by
  have hh := actualCoefficient_eq_shiftPolynomial (RingHom.id R) 1 P j
  simpa [actualCoefficient] using hh

theorem classical_record_map {R : Type*} [CommRing R]
    (P : Polynomial (Polynomial R)) :
    P.eval 1 = (Polynomial.Bivariate.swap P).map (Polynomial.evalRingHom 1) := by
  ext j
  rw [Polynomial.coeff_map]
  exact classical_record_coefficient P j

theorem classicalCoefficient_normalized
    (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (j : ℕ) :
    classicalCoefficient (operatorFamily (OperatorNormalization.normalize P) j) =
      meridianSeries ((classicalSymbol P).coeff j) := by
  rw [operatorFamily, classicalCoefficient_encode]
  rw [classicalSymbol, classical_record_coefficient]
  rfl

/-- A polynomial in L with each Laurent meridian coefficient expanded at M=e^u. -/
def formalSymbol (p : Polynomial (LaurentPolynomial ℂ)) : Polynomial (PowerSeries ℂ) :=
  p.sum (fun j c => Polynomial.monomial j (meridianSeries c))

theorem formalSymbol_as_range (p : Polynomial (LaurentPolynomial ℂ)) (r : ℕ)
    (hr : p.natDegree ≤ r) :
    formalSymbol p = ∑ j ∈ Finset.range (r+1),
      Polynomial.monomial j (meridianSeries (p.coeff j)) := by
  apply Polynomial.sum_over_range'
  · intro j; simp
  · omega

theorem normalized_symbol_degree_bound
    (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (r : ℕ)
    (hr : (Polynomial.Bivariate.swap (OperatorNormalization.normalize P)).natDegree ≤ r) :
    (classicalSymbol P).natDegree ≤ r := by
  rw [classicalSymbol, classical_record_map]
  exact (Polynomial.natDegree_map_le).trans hr

theorem normalized_formalSymbol
    (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (r : ℕ)
    (hr : (Polynomial.Bivariate.swap (OperatorNormalization.normalize P)).natDegree ≤ r) :
    formalSymbol (classicalSymbol P) =
      FormalCharacteristic.classicalPolynomial r
        (fun j => classicalCoefficient (operatorFamily (OperatorNormalization.normalize P) j)) := by
  rw [formalSymbol_as_range _ r (normalized_symbol_degree_bound P r hr)]
  simp only [FormalCharacteristic.classicalPolynomial, classicalCoefficient_normalized]

theorem omitted_shift_coefficients_zero
    (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (r j : ℕ)
    (hr : (Polynomial.Bivariate.swap P).natDegree ≤ r) (hj : r < j) :
    operatorFamily P j = 0 := by
  have hc : (Polynomial.Bivariate.swap P).coeff j = 0 :=
    Polynomial.coeff_eq_zero_of_natDegree_lt (lt_of_le_of_lt hr hj)
  simp [operatorFamily, shiftPolynomial, hc, encode_zero]

/-- The root and logarithmic scale conventions agree exactly. -/
theorem levelRoot_eq_exp_scale (N : ℕ) :
    ActualGauge.levelRoot N = Complex.exp (levelScale N) := by
  unfold ActualGauge.levelRoot levelScale
  congr 1
  ring

def meridianUnit (N : ℕ) (s : ℂ) : ℂˣ :=
  Units.mk0 (Complex.exp (s*levelScale N)) (Complex.exp_ne_zero _)

theorem meridianValue_eq_unit (N : ℕ) (s : ℂ) :
    ActualGauge.meridianValue N s = (meridianUnit N s : ℂ) := by
  unfold ActualGauge.meridianValue meridianUnit levelScale
  simp only [Units.val_mk0]
  congr 1
  ring


/-- The normalized nonzero Laurent symbol of the supplied nested operator
vanishes on the selected formal characteristic. Every coefficient encoding,
root convention, common-factor cancellation and Laurent expansion is proved.
The original annihilating equation and source-ratio asymptotic remain inputs.
The explicit degree bound ensures no shift coefficient is omitted. -/
theorem normalized_characteristic_of_record {ι : Type*} {l : Filter ι} [NeBot l]
    (P : Polynomial (Polynomial (LaurentPolynomial ℂ))) (hP : P ≠ 0)
    (r : ℕ)
    (hr : (Polynomial.Bivariate.swap (OperatorNormalization.normalize P)).natDegree ≤ r)
    (S : PowerSeries ℂ) (A : MvPowerSeries (Fin 2) ℂ)
    (hS : PowerSeries.coeff 1 S = 0)
    (N : ι → ℕ) (hN : Tendsto N l atTop)
    (F Z : ℂ → ℕ → ι → ℂ) (scale : ℂ → ι → ℂ)
    {D : Set ℂ} (hD : D.Infinite) (hDnr : ∀ s ∈ D, s.im ≠ 0)
    (hs : ∀ s ∈ D, ∀ᶠ n in l, scale s n ≠ 0)
    (hZ : ∀ s ∈ D, ∀ᶠ n in l, Z s 0 n ≠ 0)
    (hF : ∀ s ∈ D, ∀ᶠ n in l,
      ∀ j ≤ r, F s j n = scale s n * ActualGauge.sineNormalization (N n) (s+j) * Z s j n)
    (he : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1), actualCoefficient
        (LaurentPolynomial.eval₂ (RingHom.id ℂ) (meridianUnit (N n) s))
        (ActualGauge.levelRoot (N n)) P j * F s j n = 0)
    (hv : ∀ s ∈ D, ∀ j ≤ r,
      HasExpansion l (fun n => levelScale (N n))
        (fun n => Z s j n / Z s 0 n)
        (microscopic s (FormalExp.exponential
          (FormalShift.logarithmicShift S A (j : ℂ))))) :
    classicalSymbol P ≠ 0 ∧
      (formalSymbol (classicalSymbol P)).eval
        (-FormalExp.exponential (PowerSeries.derivative ℂ S)) = 0 := by
  refine ⟨classicalSymbol_ne_zero hP, ?_⟩
  have hrec : ∀ s ∈ D, ∀ᶠ n in l,
      ∑ j ∈ Finset.range (r+1),
        evaluate (operatorFamily (OperatorNormalization.normalize P) j)
          (Complex.exp (levelScale (N n))) (Complex.exp (s*levelScale (N n))) * F s j n = 0 := by
    intro s hsd
    filter_upwards [he s hsd, hN.eventually (eventually_ge_atTop 1)] with n hen hn
    have hlev : (N n : ℂ) ≠ 0 := by exact_mod_cast (show N n ≠ 0 by omega)
    have hh := (recurrence_at_root_iff
      (LaurentPolynomial.eval₂ (RingHom.id ℂ) (meridianUnit (N n) s))
      (N n) hlev P (Finset.range (r+1)) (fun j => F s j n)).mp hen
    simpa only [actualCoefficient_eq_evaluate, levelRoot_eq_exp_scale,
      meridianUnit, Units.val_mk0] using hh
  have hh := LaurentExpansion.characteristic_of_laurent_recurrence r
    (operatorFamily (OperatorNormalization.normalize P)) S A hS N hN F Z scale
    hD hDnr hs hZ hF hrec hv
  rw [normalized_formalSymbol P r hr]
  exact hh

end VolumeLogic.OperatorCoefficientAdapter
