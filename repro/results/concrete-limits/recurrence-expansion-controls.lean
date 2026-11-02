import RecurrenceGaugeExpansion

noncomputable section
open Filter Asymptotics
open scoped Topology
open VolumeLogic.RecurrenceExpansion
namespace VolumeLogic.RecurrenceExpansionControls

/-- Multiplication retains the quadratic cross term, even when each input is linear. -/
theorem retained_cross_term : PowerSeries.coeff 2
    (((1 : PowerSeries ℂ) + PowerSeries.X) * (1 - PowerSeries.X)) = -1 := by
  have he : ((1 : PowerSeries ℂ) + PowerSeries.X) * (1 - PowerSeries.X) =
      1 - PowerSeries.X^2 := by ring
  rw [he]
  simp

/-- The product theorem applies to literal complex functions, not only coefficient tables. -/
theorem literal_product_expansion {ι : Type*} {l : Filter ι} {h : ι → ℂ} (ht : Tendsto h l (𝓝 0)) :
    HasExpansion l h (fun n => (1 + h n) * (1 - h n))
      (((1 : PowerSeries ℂ) + PowerSeries.X) * (1 - PowerSeries.X)) := by
  have hp := hasExpansion_polynomial (l := l) (h := h)
    ((1 : Polynomial ℂ) + Polynomial.X) ht
  have hq := hasExpansion_polynomial (l := l) (h := h)
    ((1 : Polynomial ℂ) - Polynomial.X) ht
  simpa using hp.mul hq ht

/-- The actual sum may cancel although its individual factors are nonzero. -/
theorem cancelling_sum {ι : Type*} {l : Filter ι} {h : ι → ℂ} :
    HasExpansion l h (fun n => (1 + h n) + (-1 - h n)) (0 : PowerSeries ℂ) := by
  have he : (fun n => (1 + h n) + (-1 - h n)) = (fun _ : ι => (0 : ℂ)) := by
    funext n
    ring
  rw [he]
  simpa using (hasExpansion_const (l := l) (h := h) 0)

/-- A zero scale hides the nonzero series X at every order. The nonzero-scale
hypothesis in the characteristic implication cannot be removed. -/
theorem zero_scale_hides_series : HasExpansion (Filter.atTop : Filter ℕ) (fun _ => (0 : ℂ))
    (fun _ => (0 : ℂ)) (PowerSeries.X : PowerSeries ℂ) := by
  intro m
  have he : ((PowerSeries.X : PowerSeries ℂ).trunc (m+1)).eval 0 = 0 := by
    rw [← Polynomial.coeff_zero_eq_eval_zero, PowerSeries.coeff_trunc]
    simp
  simp only [he, sub_zero]
  exact isBigO_zero _ _

/-- The series in the preceding control is indeed nonzero. -/
theorem hidden_series_nonzero : (PowerSeries.X : PowerSeries ℂ) ≠ 0 := by
  exact PowerSeries.X_ne_zero

/-- Without a scale tending to zero, an eventually zero function can even
admit the nonzero constant series. Bounded remainder alone cannot recover it. -/
theorem nonvanishing_scale_hides_constant : HasExpansion (Filter.atTop : Filter ℕ) (fun _ => (1 : ℂ))
    (fun _ => (0 : ℂ)) (1 : PowerSeries ℂ) := by
  intro m
  simpa using (isBigO_const_one ℂ (-1 : ℂ) (Filter.atTop : Filter ℕ))

end VolumeLogic.RecurrenceExpansionControls

#print axioms VolumeLogic.RecurrenceExpansionControls.retained_cross_term
#print axioms VolumeLogic.RecurrenceExpansionControls.literal_product_expansion
#print axioms VolumeLogic.RecurrenceExpansionControls.cancelling_sum
#print axioms VolumeLogic.RecurrenceExpansionControls.zero_scale_hides_series
#print axioms VolumeLogic.RecurrenceExpansionControls.hidden_series_nonzero
#print axioms VolumeLogic.RecurrenceExpansionControls.nonvanishing_scale_hides_constant
