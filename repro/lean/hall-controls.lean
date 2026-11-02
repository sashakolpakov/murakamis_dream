import TriangleHall

open scoped BigOperators
open VolumeLogic TriangleBalance TriangleMinimizer TriangleLoads
namespace VolumeLogic.HallControls

/-- A strict two-vertex cut gives the actual balance with one zero corner.
Two corners have the same destination; the active support is still retained. -/
theorem strict_cut_balance : ∃! q : Fin 2 → ℝ, q 0 = 0 ∧
    ∀ v, vertexLoad (fun (_ : Unit) => ![0,1,1])
      (fun _ => ![1,1,0]) q v = (![1/4,1/4] : Fin 2 → ℝ) v := by
  apply TriangleHall.exists_unique_balance
    (fun (_ : Unit) => ![0,1,1]) (fun _ => ![1,1,0]) ![1/4,1/4]
  · intro t i
    fin_cases i <;> norm_num
  · intro t
    exact ⟨0,by norm_num⟩
  · norm_num [Fin.sum_univ_two]
  · intro A hn hu
    fin_cases A <;>
      norm_num [HallRecession.deficit,HallRecession.capacity,HallRecession.rowCut,
        support,Fin.exists_fin_succ,Finset.sum_filter,Fin.sum_univ_succ] at *
    exact hu (by decide)

/-- Weak cuts can hold on a connected support while the demanded boundary
load is unattainable at every finite height. -/
theorem weak_cuts_no_balance :
    (∀ A : Finset (Fin 2), 0 ≤ HallRecession.deficit
      (fun (_ : Unit) => Finset.univ) (![0,1/2] : Fin 2 → ℝ) A) ∧
    ¬ ∃ q : Fin 2 → ℝ, ∀ v,
      vertexLoad (fun (_ : Unit) => ![0,1,1]) (fun _ => ![1,1,1]) q v =
        (![0,1/2] : Fin 2 → ℝ) v := by
  constructor
  · intro A
    fin_cases A <;>
      norm_num [HallRecession.deficit,HallRecession.capacity,HallRecession.rowCut,
        Fin.exists_fin_succ,Fin.sum_univ_succ]
  · rintro ⟨q,hq⟩
    have hp := TriangleHall.supportedLoad_positive ![1,1,1]
      (fun i => q ((![0,1,1] : Fin 3 → Fin 2) i))
      (by intro i; fin_cases i <;> norm_num) 0 (by norm_num)
    have he := hq 0
    simp only [vertexLoad,column,aggregate,Fintype.sum_unique,Fin.sum_univ_succ] at he
    norm_num at he
    have hlast : (![0,1,1] : Fin 3 → Fin 2) 2 ≠ 0 := by decide
    simp only [if_neg hlast,add_zero] at he
    linarith

/-- Strict proper cuts alone do not supply the missing total mass equation. -/
theorem incompatible_total :
    (∀ A : Finset (Fin 2), A.Nonempty → A ≠ Finset.univ →
      0 < HallRecession.deficit (fun (_ : Unit) => Finset.univ)
        (fun _ => 0) A) ∧
    ¬ ∃ q : Fin 2 → ℝ, ∀ v,
      vertexLoad (fun (_ : Unit) => ![0,1,1]) (fun _ => ![1,1,1]) q v = 0 := by
  constructor
  · intro A hn hu
    fin_cases A <;>
      norm_num [HallRecession.deficit,HallRecession.capacity,HallRecession.rowCut,
        Fin.exists_fin_succ,Fin.sum_univ_succ] at *
  · rintro ⟨q,hq⟩
    have he := sum_vertexLoad (fun (_ : Unit) => ![0,1,1])
      (fun _ => ![1,1,1]) q
      (by intro t i; fin_cases i <;> norm_num)
      (by intro t; exact ⟨0,by norm_num⟩)
    simp only [hq,Finset.sum_const_zero,Fintype.card_unique] at he
    norm_num at he

end VolumeLogic.HallControls
#print axioms VolumeLogic.HallControls.strict_cut_balance
#print axioms VolumeLogic.HallControls.weak_cuts_no_balance
#print axioms VolumeLogic.HallControls.incompatible_total
