
import TriangleBalance

open scoped BigOperators
open VolumeLogic
open TriangleBalance TriangleMinimizer TrianglePotential TriangleLoads
namespace VolumeLogic.TriangleBalanceControls

-- Wrong half-mass normalization is rejected by an actual supported row.
theorem half_mass : ¬ ((∑ v : Unit,
    vertexLoad (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
      (fun _ => 0) v) = 1) := by
  have he := sum_vertexLoad (fun (_ : Unit) (_ : Fin 3) => ())
    (fun _ => ![1,0,0]) (fun _ => 0)
    (by intro t i; fin_cases i <;> norm_num)
    (by intro t; exact ⟨0, by norm_num⟩)
  norm_num at he
  simp only [Fintype.sum_unique]
  rw [he]
  norm_num

-- Repeated active destinations keep both corner loads, not one of them.
theorem repeated_destination : vertexLoad (fun (_ : Unit) (_ : Fin 3) => (1 : Fin 2))
    (fun _ => ![1,1,0]) (fun _ => 0) 1 = 1/2 := by
  have he := sum_vertexLoad (fun (_ : Unit) (_ : Fin 3) => (1 : Fin 2))
    (fun _ => ![1,1,0]) (fun _ => 0)
    (by intro t i; fin_cases i <;> norm_num)
    (by intro t; exact ⟨0, by norm_num⟩)
  simpa [Fin.sum_univ_two, vertexLoad, column, aggregate] using he

-- The one-vertex grounded problem has a minimum but no zero root residual
-- when the chosen root demand is zero.
theorem arbitrary_root :
    (∀ p : Unit → ℝ, p () = 0 →
      summedPotential (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
        (fun _ => 0) (fun _ => 0) ≤
      summedPotential (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
        (fun _ => 0) p) ∧
    residual (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
      (fun _ => 0) (fun _ => 0) () ≠ 0 := by
  constructor
  · intro p hp
    have he : p = fun _ => (0 : ℝ) := by funext v; cases v; exact hp
    rw [he]
  · have he := root_residual (fun (_ : Unit) (_ : Fin 3) => ())
      (fun _ => ![1,0,0]) (fun _ => 0) (fun _ => 0)
      (by intro t i; fin_cases i <;> norm_num)
      (by intro t; exact ⟨0, by norm_num⟩) ()
      (by intro v hv; cases v; exact False.elim (hv rfl))
    norm_num at he
    rw [he]
    norm_num

-- Without connected support, a free unused vertex admits distinct solutions.
theorem disconnected_support : ∃ q p : Fin 2 → ℝ, q ≠ p ∧ q 0 = 0 ∧ p 0 = 0 ∧
    (∀ v, v ≠ 0 → vertexLoad (fun (_ : Unit) (_ : Fin 3) => (0 : Fin 2))
      (fun _ => ![1,0,0]) q v = 0) ∧
    (∀ v, v ≠ 0 → vertexLoad (fun (_ : Unit) (_ : Fin 3) => (0 : Fin 2))
      (fun _ => ![1,0,0]) p v = 0) := by
  refine ⟨![0,0], ![0,1], ?_, by norm_num, by norm_num, ?_, ?_⟩
  · intro he
    have hh := congrFun he 1
    norm_num at hh
  all_goals
    intro v hv
    fin_cases v
    · exact False.elim (hv rfl)
    · simp [vertexLoad, column, aggregate]

end VolumeLogic.TriangleBalanceControls
#print axioms VolumeLogic.TriangleBalanceControls.half_mass
#print axioms VolumeLogic.TriangleBalanceControls.repeated_destination
#print axioms VolumeLogic.TriangleBalanceControls.arbitrary_root
#print axioms VolumeLogic.TriangleBalanceControls.disconnected_support
