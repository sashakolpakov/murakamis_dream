import WeightedGraph
import Flattening
import TransportCoercivity
import GroundedConvexity
import GroundedLaplacian
import TriangleLoads
import TrianglePotential
import TriangleMinimizer
import TriangleBalance
import HallRecession
import TriangleHall

/-!
Expected propositions for the variational steps in Appendices P and R.
Each anonymous example spells out the mathematical hypotheses and conclusion
independently of the declaration type. The correspondence file records which
are complete identities and which are components of a written application.
-/

namespace VolumeLogic.VariationalContracts
open scoped BigOperators Classical
open Set
variable {V E T : Type*}

section WeightedGraphContracts
open WeightedGraph

-- manuscript-contract: VolumeLogic.WeightedGraph.energy_eq_zero_iff_constant
example [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : connected src dst w) (f : V → ℝ) :
    (∑ e, w e * (f (src e) - f (dst e)) ^ 2) = 0 ↔ ∀ u v, f u = f v := by
  simpa only [WeightedGraph.energy] using
    VolumeLogic.WeightedGraph.energy_eq_zero_iff_constant src dst w hw hc f

-- manuscript-contract: VolumeLogic.WeightedGraph.grounded_laplacian_pos
example [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : connected src dst w) (root : V) (f : V → ℝ)
    (ground : f root = 0) (nonzero : f ≠ 0) :
    0 < ∑ u, ∑ v, f u * laplacian src dst w u v * f v := by
  exact VolumeLogic.WeightedGraph.grounded_laplacian_pos src dst w hw hc root f ground nonzero

end WeightedGraphContracts

section FlatteningContracts
open Flattening

-- manuscript-contract: VolumeLogic.Flattening.stationary_quadratic_cost
example {g dg ddg : ℝ → ℝ} {t E : ℝ}
    (ht : 0 ≤ t)
    (hg : ∀ x ∈ Icc 0 t, HasDerivAt g (dg x) x)
    (hdg : ∀ x ∈ Icc 0 t, HasDerivAt dg (ddg x) x)
    (hzero : dg 0 = 0)
    (hlower : ∀ x ∈ Icc 0 t, 0 ≤ ddg x)
    (hupper : ∀ x ∈ Icc 0 t, ddg x ≤ E) :
    0 ≤ g t - g 0 ∧ g t - g 0 ≤ E * t ^ 2 / 2 := by
  exact VolumeLogic.Flattening.stationary_quadratic_cost ht hg hdg hzero hlower hupper

-- manuscript-contract: VolumeLogic.Flattening.weak_balance_sector_gap
example {g dg ddg Qk Qo : ℝ → ℝ}
    {dk dover t z E : ℝ} (others : List ℝ)
    (ht : 0 < t) (ht1 : t ≤ 1)
    (hg : ∀ x ∈ Icc 0 t, HasDerivAt g (dg x) x)
    (hdg : ∀ x ∈ Icc 0 t, HasDerivAt dg (ddg x) x)
    (hzero : dg 0 = 0)
    (hlower : ∀ x ∈ Icc 0 t, 0 ≤ ddg x)
    (hupper : ∀ x ∈ Icc 0 t, ddg x ≤ E)
    (hck : ConvexOn ℝ (Icc 0 1) Qk) (hco : ConvexOn ℝ (Icc 0 1) Qo)
    (hdk : HasDerivAt Qk dk 1) (hdo : HasDerivAt Qo dover 1)
    (hentropy : 0 ≤ Qk 1 - dk) (hpure : z / 2 ≤ Qo 1)
    (hover : 0 < Qo 1 - dover) (hbalance : z ≤ Qk 1 + Qo 1)
    (hsmall : t * E ≤ Qo 1 - dover)
    (hothers : ∀ x ∈ others, 0 ≤ x) :
    g t - (Qk (1 - t) + Qo (1 - t) -
      max ((1 - t) * z) (Qk (1 - t) + (1 - t) * z / 2) +
      VolumeLogic.total others) < g 0 := by
  exact VolumeLogic.Flattening.weak_balance_sector_gap others ht ht1 hg hdg hzero hlower hupper hck hco hdk hdo hentropy hpure hover hbalance hsmall hothers

end FlatteningContracts

section TransportCoercivityContracts
open TransportCoercivity
variable [Fintype V] [Fintype T]

-- manuscript-contract: VolumeLogic.TransportCoercivity.exists_grounded_minimizer
example
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : connected S) (root : V)
    (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, rowMass S α t * rowMax S hne h t - C t ≤ Q t h)
    (hcont : ∀ t, Continuous (Q t)) :
    ∃ h : V → ℝ, h root = 0 ∧
      ∀ k : V → ℝ, k root = 0 → potential S α Q h ≤ potential S α Q k := by
  exact VolumeLogic.TransportCoercivity.exists_grounded_minimizer S hne α hα hc root Q C hQ hcont

end TransportCoercivityContracts

section GroundedConvexityContracts
open GroundedConvexity

-- manuscript-contract: VolumeLogic.GroundedConvexity.exists_unique_grounded_minimizer
example [Fintype V] [Fintype T] [Fintype E]
    (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (α : T → V → ℝ) (hα : ∀ t i, i ∈ S t → 0 < α t i)
    (hc : TransportCoercivity.connected S) (root : V)
    (Q : T → (V → ℝ) → ℝ) (C : T → ℝ)
    (hQ : ∀ t h, TransportCoercivity.rowMass S α t *
      TransportCoercivity.rowMax S hne h t - C t ≤ Q t h)
    (hcont : ∀ t, Continuous (Q t))
    (src dst : E → V) (w : (V → ℝ) → E → ℝ)
    (dg : (V → ℝ) → (V → ℝ) → ℝ → ℝ)
    (hfirst : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Icc (0 : ℝ) 1,
      HasDerivAt (segmentValue (TransportCoercivity.potential S α Q) x y) (dg x y t) t)
    (hsecond : ∀ x ∈ grounded root, ∀ y ∈ grounded root, ∀ t ∈ Ioo (0 : ℝ) 1,
      HasDerivAt (dg x y)
        (WeightedGraph.energy src dst (w (segment x y t)) (y - x)) t)
    (hw : ∀ z ∈ grounded root, ∀ e, 0 ≤ w z e)
    (hconn : ∀ z ∈ grounded root, WeightedGraph.connected src dst (w z)) :
    ∃! x : V → ℝ, x root = 0 ∧ ∀ y : V → ℝ, y root = 0 →
      TransportCoercivity.potential S α Q x ≤ TransportCoercivity.potential S α Q y := by
  exact VolumeLogic.GroundedConvexity.exists_unique_grounded_minimizer S hne α hα hc root Q C hQ hcont src dst w dg hfirst hsecond hw hconn

end GroundedConvexityContracts

section GroundedLaplacianContracts
open GroundedLaplacian

-- manuscript-contract: VolumeLogic.GroundedLaplacian.reducedMatrix_det_ne_zero
example [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V) :
    (reducedMatrix src dst w root).det ≠ 0 := by
  exact VolumeLogic.GroundedLaplacian.reducedMatrix_det_ne_zero src dst w hw hc root

-- manuscript-contract: VolumeLogic.GroundedLaplacian.exists_unique_grounded_solution
example [Fintype V] [Fintype E]
    (src dst : E → V) (w : E → ℝ) (hw : ∀ e, 0 ≤ w e)
    (hc : WeightedGraph.connected src dst w) (root : V) (b : V → ℝ) :
    ∃! f : V → ℝ, f root = 0 ∧ ∀ u, u ≠ root →
      (∑ v, WeightedGraph.laplacian src dst w u v * f v) = b u := by
  exact VolumeLogic.GroundedLaplacian.exists_unique_grounded_solution src dst w hw hc root b

end GroundedLaplacianContracts

section TriangleLoadsContracts
open TriangleLoads

-- manuscript-contract: VolumeLogic.TriangleLoads.jacobian_energy
example (w h : Fin 3 → ℝ) :
    (∑ i, h i * jacobianAction w h i) =
      ∑ e : Fin 3,
        (w (edgeSrc e) * w (edgeDst e) /
          (2 * Real.pi * triangleD w * (w (edgeSrc e) + w (edgeDst e)))) *
          (h (edgeSrc e) - h (edgeDst e)) ^ 2 := by
  simpa only [WeightedGraph.energy, conductance] using
    VolumeLogic.TriangleLoads.jacobian_energy w h

-- manuscript-contract: VolumeLogic.TriangleLoads.sum_load_pairing_hasDerivAt
example {T V : Type*} [Fintype T]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (q h : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, 0 < radicand (weights (a t) (fun i => q (corners t i)))) :
    HasDerivAt
      (fun u : ℝ => ∑ t, ∑ i, h (corners t i) *
        load (a t) (fun j => q (corners t j) + u * h (corners t j)) i)
      (WeightedGraph.energy
        (fun e : T × Fin 3 => corners e.1 (edgeSrc e.2))
        (fun e : T × Fin 3 => corners e.1 (edgeDst e.2))
        (fun e : T × Fin 3 => conductance
          (weights (a e.1) (fun i => q (corners e.1 i))) (edgeSrc e.2) (edgeDst e.2)) h) 0 := by
  exact VolumeLogic.TriangleLoads.sum_load_pairing_hasDerivAt corners a q h ha hs

-- manuscript-contract: VolumeLogic.TriangleLoads.singletonLoad_hasDerivAt
example (active : Fin 3) (q h : Fin 3 → ℝ) (i : Fin 3) :
    HasDerivAt (fun t : ℝ => singletonLoad active (fun j => q j + t * h j) i) 0 0 := by
  exact VolumeLogic.TriangleLoads.singletonLoad_hasDerivAt active q h i

end TriangleLoadsContracts

section TrianglePotentialContracts
open TriangleLoads TrianglePotential

-- manuscript-contract: VolumeLogic.TrianglePotential.summedPotential_mixed_hasDerivAt
example {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q h : V → ℝ)
    (regular : T → Prop) [DecidablePred regular] (active : T → Fin 3)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, regular t → 0 < radicand (weights (a t) (fun i => q (corners t i))))
    (hsingle : ∀ t, ¬ regular t → 0 < a t (active t) ∧
      ∀ i, i ≠ active t → a t i = 0) (u : ℝ) :
    HasDerivAt (fun v : ℝ => summedPotential corners a demand (fun j => q j + v * h j))
      ((∑ t, if regular t then
        ∑ i, h (corners t i) * load (a t)
          (fun j => q (corners t j) + u * h (corners t j)) i
        else h (corners t (active t)) / 2) - ∑ v, demand v * h v) u := by
  exact VolumeLogic.TrianglePotential.summedPotential_mixed_hasDerivAt corners a demand q h regular active ha hs hsingle u

-- manuscript-contract: VolumeLogic.TrianglePotential.summedPotential_mixed_second_at
example {T V : Type*} [Fintype T] [Fintype V]
    (corners : T → Fin 3 → V) (a : T → Fin 3 → ℝ) (demand q h : V → ℝ)
    (regular : T → Prop) [DecidablePred regular] (active : T → Fin 3)
    (ha : ∀ t i, 0 ≤ a t i)
    (hs : ∀ t, regular t → 0 < radicand (weights (a t) (fun i => q (corners t i))))
    (hsingle : ∀ t, ¬ regular t → 0 < a t (active t) ∧
      ∀ i, i ≠ active t → a t i = 0) (u : ℝ) :
    HasDerivAt
      (fun v : ℝ => deriv
        (fun z : ℝ => summedPotential corners a demand (fun j => q j + z * h j)) v)
      (WeightedGraph.energy
        (fun e : T × Fin 3 => corners e.1 (edgeSrc e.2))
        (fun e : T × Fin 3 => corners e.1 (edgeDst e.2))
        (fun e : T × Fin 3 => if regular e.1 then conductance
          (weights (a e.1) (fun i => q (corners e.1 i) + u * h (corners e.1 i)))
          (edgeSrc e.2) (edgeDst e.2) else 0) h) u := by
  exact VolumeLogic.TrianglePotential.summedPotential_mixed_second_at corners a demand q h regular active ha hs hsingle u

end TrianglePotentialContracts

section TriangleMinimizerContracts
open TriangleLoads TrianglePotential TriangleMinimizer

-- manuscript-contract: VolumeLogic.TriangleMinimizer.exists_unique_prescribed_minimizer
example [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ) (δ : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hp : ∀ t i, 0 < a t i → 0 < β t i)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0)
    (hm : ∀ t, (∑ i, β t i) = 1/2)
    (hc : TransportCoercivity.connected (support c a)) (root : V)
    (hd : ∀ v, v ≠ root → δ v = column c β v) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ p : V → ℝ, p root = 0 →
      summedPotential c a δ q ≤ summedPotential c a δ p := by
  exact VolumeLogic.TriangleMinimizer.exists_unique_prescribed_minimizer c a β δ ha hp hz hm hc root hd

end TriangleMinimizerContracts

section TriangleBalanceContracts
open TriangleLoads TrianglePotential TriangleMinimizer TriangleBalance

-- manuscript-contract: VolumeLogic.TriangleBalance.exists_unique_balance
example [Fintype T] [Fintype V]
    (c : T → Fin 3 → V) (a β : T → Fin 3 → ℝ) (d : V → ℝ)
    (ha : ∀ t i, 0 ≤ a t i)
    (hp : ∀ t i, 0 < a t i → 0 < β t i)
    (hz : ∀ t i, ¬ 0 < a t i → β t i = 0)
    (hm : ∀ t, (∑ i, β t i) = 1/2)
    (hc : TransportCoercivity.connected (support c a)) (root : V)
    (hd : ∀ v, v ≠ root → d v = column c β v) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ v, v ≠ root → vertexLoad c a q v = d v := by
  exact VolumeLogic.TriangleBalance.exists_unique_balance c a β d ha hp hz hm hc root hd

end TriangleBalanceContracts

section HallRecessionContracts
open TransportCoercivity HallRecession
variable [Fintype V] [Fintype T]

-- manuscript-contract: VolumeLogic.HallRecession.connected_of_strict_cuts
example (S : T → Finset V) (hne : ∀ t, (S t).Nonempty)
    (d : V → ℝ) (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A) :
    connected S := by
  exact VolumeLogic.HallRecession.connected_of_strict_cuts S hne d hm hc

-- manuscript-contract: VolumeLogic.HallRecession.exists_grounded_minimizer
example (S : T → Finset V)
    (hne : ∀ t, (S t).Nonempty) (d : V → ℝ)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ → 0 < deficit S d A)
    (root : V) (P : (V → ℝ) → ℝ) (hP : Continuous P) (C : ℝ)
    (hbound : ∀ q, recession S hne d q-C ≤ P q) :
    ∃ q : V → ℝ, q root = 0 ∧ ∀ p : V → ℝ, p root = 0 → P q ≤ P p := by
  exact VolumeLogic.HallRecession.exists_grounded_minimizer S hne d hm hc root P hP C hbound

end HallRecessionContracts

section TriangleHallContracts
open TriangleLoads TrianglePotential TriangleMinimizer TriangleBalance TriangleHall
variable [Fintype V] [Fintype T]

-- manuscript-contract: VolumeLogic.TriangleHall.exists_unique_balance
example (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ →
      0 < HallRecession.deficit (support c a) d A) (root : V) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ v, vertexLoad c a q v = d v := by
  exact VolumeLogic.TriangleHall.exists_unique_balance c a d ha hne hm hc root

-- manuscript-contract: VolumeLogic.TriangleHall.exists_unique_minimizer
example (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (d : V → ℝ) (ha : ∀ t i, 0 ≤ a t i) (hne : ∀ t, ∃ i, 0 < a t i)
    (hm : (∑ v, d v) = (Fintype.card T : ℝ)/2)
    (hc : ∀ A : Finset V, A.Nonempty → A ≠ Finset.univ →
      0 < HallRecession.deficit (support c a) d A) (root : V) :
    ∃! q : V → ℝ, q root = 0 ∧ ∀ p : V → ℝ, p root = 0 →
      summedPotential c a d q ≤ summedPotential c a d p := by
  exact VolumeLogic.TriangleHall.exists_unique_minimizer c a d ha hne hm hc root

end TriangleHallContracts

/- The fixed-boundary dictionary uses one destination for three prescribed
boundary corners, while retaining a separate coefficient at each corner. -/
example (c : T → Fin 3 → V) (a : T → Fin 3 → ℝ)
    (root : V) (q : V → ℝ) (hq : q root = 0) (t : T)
    (hboundary : ∀ i, c t i = root) :
    (fun i => TriangleLoads.weights (a t) (fun j => q (c t j)) i) = a t := by
  funext i
  exact TriangleMinimizer.pooled_boundary_weight c a root q hq t i (hboundary i)

/- Half-mass is the source of the normalization under a common log scale.
This is checked for the actual supported supremum, including singletons. -/
example (a q : Fin 3 → ℝ) (ha : ∀ i, 0 ≤ a i)
    (hne : ∃ i, 0 < a i) (c : ℝ) :
    TrianglePotential.potential a (fun i => q i + c) =
      TrianglePotential.potential a q + c / 2 := by
  have shift : ∀ α, TrianglePotential.Feasible a α →
      TrianglePotential.objective a (fun i => q i + c) α =
        TrianglePotential.objective a q α + c / 2 := by
    intro α hα
    have hd := TriangleMinimizer.objective_difference a (fun i => q i + c) q α hα
    simp only [add_sub_cancel_left, ← Finset.sum_mul, hα.2.1] at hd
    linarith
  obtain ⟨α, hα, heα, hmaxα⟩ :=
    TriangleMinimizer.potential_attained a q ha hne
  obtain ⟨β, hβ, heβ, hmaxβ⟩ :=
    TriangleMinimizer.potential_attained a (fun i => q i + c) ha hne
  have hupper := hmaxα β hβ
  have hlower := hmaxβ α hα
  rw [shift β hβ] at heβ
  rw [shift α hα, ← heα] at hlower
  linarith

end VolumeLogic.VariationalContracts
