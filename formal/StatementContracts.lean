import VolumeLogic

/-!
Expected propositions for the finite manuscript arguments. Each anonymous
example states its binders and conclusion explicitly before applying the
selected declaration. The coefficient-list and ordered-ring dictionaries,
and the written inputs not formalized here, are recorded root by root in
`correspondence/finite.json`. These examples do not identify abstract bounds
with a quantum invariant or a geometric volume.
-/

namespace VolumeLogic.ManuscriptContracts
open Lean.Grind
universe u v w z
attribute [local instance] Semiring.natCast Ring.intCast

section NaturalSupports

-- manuscript-contract: VolumeLogic.three_supports
example (level left right : Nat) (degreeBudget : left + right ≤ level - 1) :
    ((left ≤ (level-1)/2 ∧ right ≤ (level-1)/2) ∨
      (level-1)/2 < right ∨ (level-1)/2 < left) ∧
      ¬ ((level-1)/2 < left ∧ (level-1)/2 < right) := by
  exact three_supports level left right degreeBudget

-- manuscript-contract: VolumeLogic.left_endpoint_cutoff
example (level endpoint : Nat) (levelAtLeastTwo : 2 ≤ level) (endpointInRange : endpoint < level) :
    ((level-1)/2 < level-1-endpoint ↔ endpoint < level/2) := by
  exact left_endpoint_cutoff level endpoint levelAtLeastTwo endpointInRange

-- manuscript-contract: VolumeLogic.central_endpoint_even
example (halfLevel first last : Nat) (positiveHalf : 1 ≤ halfLevel)
    (lastInRange : last < 2*halfLevel) :
    (first ≤ (2*halfLevel-1)/2 ∧ 2*halfLevel-1-last ≤ (2*halfLevel-1)/2) ↔
      (first < halfLevel ∧ halfLevel ≤ last) := by
  exact central_endpoint_even halfLevel first last positiveHalf lastInRange

-- manuscript-contract: VolumeLogic.central_endpoint_odd
example (halfDegree first last : Nat) (lastInRange : last ≤ 2*halfDegree) :
    (first ≤ (2*halfDegree)/2 ∧ 2*halfDegree-last ≤ (2*halfDegree)/2) ↔
      (first ≤ halfDegree ∧ halfDegree ≤ last) := by
  exact central_endpoint_odd halfDegree first last lastInRange

end NaturalSupports

section PolynomialAlgebra
variable {R : Type u} [CommRing R]

-- manuscript-contract: VolumeLogic.double_root_jet_identity
example (hValue hDerivative fValue fDerivative projection nilpotent numerator numeratorDerivative : R)
    (valueEquation : numerator = hValue*nilpotent)
    (derivativeEquation : numeratorDerivative = hValue*projection+hDerivative*nilpotent) :
    hValue*hValue*(fValue*projection+fDerivative*nilpotent) =
      hValue*fValue*numeratorDerivative+
        (hValue*fDerivative-hDerivative*fValue)*numerator := by
  exact double_root_jet_identity hValue hDerivative fValue fDerivative
    projection nilpotent numerator numeratorDerivative valueEquation derivativeEquation

-- manuscript-contract: VolumeLogic.tensor_grid_subtraction
example (coordinateCosts : List (R × R)) :
    nonemptySecondChoices coordinateCosts =
      product (coordinateCosts.map (fun entry => entry.1+entry.2)) -
        product (coordinateCosts.map (fun entry => entry.1)) := by
  exact tensor_grid_subtraction coordinateCosts

-- manuscript-contract: VolumeLogic.monic_division_identity
example (nodes coefficients : List R) (power : Nat) :
    coefficient coefficients power =
      coefficient (polyAdd
        (monicMultiple nodes (monicQuotient nodes coefficients))
        (monicRemainder nodes coefficients)) power := by
  exact monic_division_identity nodes coefficients power

-- manuscript-contract: VolumeLogic.monic_remainder_degree_bound
example (nodes coefficients : List R) (power : Nat) (aboveDegree : nodes.length ≤ power) :
    coefficient (monicRemainder nodes coefficients) power = 0 := by
  exact monic_remainder_degree_bound nodes coefficients power aboveDegree

-- manuscript-contract: VolumeLogic.top_coefficient_is_newton
example (nodes coefficients : List R) :
    coefficient (monicRemainder nodes coefficients) (nodes.length-1) =
      newtonFunctional nodes coefficients := by
  exact top_coefficient_is_newton nodes coefficients

-- manuscript-contract: VolumeLogic.double_root_remainder
example (node : R) (coefficients : List R) :
    monicRemainder [node,node] coefficients =
      [horner coefficients node - node*formalDerivativeValue coefficients node,
        formalDerivativeValue coefficients node] := by
  exact double_root_remainder node coefficients

-- manuscript-contract: VolumeLogic.monicRemainder_polyAdd
example (nodes first second : List R) (power : Nat) :
    coefficient (monicRemainder nodes (polyAdd first second)) power =
      coefficient (polyAdd (monicRemainder nodes first)
        (monicRemainder nodes second)) power := by
  exact monicRemainder_polyAdd nodes first second power

-- manuscript-contract: VolumeLogic.monicRemainder_polyScale
example (nodes coefficients : List R) (scalar : R) (power : Nat) :
    coefficient (monicRemainder nodes (polyScale scalar coefficients)) power =
      coefficient (polyScale scalar (monicRemainder nodes coefficients)) power := by
  exact monicRemainder_polyScale nodes scalar coefficients power

-- manuscript-contract: VolumeLogic.newtonFunctional_quotient_invariant
example (nodes first second quotient : List R)
    (sameClass : ∀ power, coefficient first power =
      coefficient (polyAdd second (monicMultiple nodes quotient)) power) :
    newtonFunctional nodes first = newtonFunctional nodes second := by
  exact newtonFunctional_quotient_invariant nodes first second quotient sameClass

-- manuscript-contract: VolumeLogic.monic_remainder_unique_between
example (nodes input firstQuotient secondQuotient firstRemainder secondRemainder : List R)
    (firstDegree : ∀ power, nodes.length ≤ power → coefficient firstRemainder power = 0)
    (secondDegree : ∀ power, nodes.length ≤ power → coefficient secondRemainder power = 0)
    (firstDivision : ∀ power, coefficient input power =
      coefficient (polyAdd firstRemainder (monicMultiple nodes firstQuotient)) power)
    (secondDivision : ∀ power, coefficient input power =
      coefficient (polyAdd secondRemainder (monicMultiple nodes secondQuotient)) power)
    (power : Nat) : coefficient firstRemainder power = coefficient secondRemainder power := by
  exact monic_remainder_unique_between nodes input firstQuotient secondQuotient
    firstRemainder secondRemainder firstDegree secondDegree firstDivision secondDivision power

-- manuscript-contract: VolumeLogic.monicRemainder_permutation
example (nodes reordered : List R) (sameMultiset : nodes.Perm reordered) (input : List R) :
    monicRemainder nodes input = monicRemainder reordered input := by
  exact monicRemainder_permutation sameMultiset input

-- manuscript-contract: VolumeLogic.newtonFunctional_characterization
example (nodes : List R) (candidate : List R → R)
    (coefficientInvariant : ∀ first second,
      (∀ power, coefficient first power = coefficient second power) →
        candidate first = candidate second)
    (additive : ∀ first second, candidate (polyAdd first second) = candidate first+candidate second)
    (killsMultiples : ∀ quotient, candidate (monicMultiple nodes quotient) = 0)
    (normalized : ∀ remainder,
      (∀ power, nodes.length ≤ power → coefficient remainder power = 0) →
        candidate remainder = coefficient remainder (nodes.length-1))
    (input : List R) : candidate input = newtonFunctional nodes input := by
  exact newtonFunctional_characterization nodes candidate coefficientInvariant
    additive killsMultiples normalized input

-- manuscript-contract: VolumeLogic.monicRemainder_mul_reduce_both
example (nodes first second : List R) :
    monicRemainder nodes (polyMul first second) =
      monicRemainder nodes (polyMul (monicRemainder nodes first)
        (monicRemainder nodes second)) := by
  exact monicRemainder_mul_reduce_both nodes first second

-- manuscript-contract: VolumeLogic.newtonFunctional_product
example (nodes : List R) (factors : List (List R)) :
    newtonFunctional nodes (polyProduct factors) =
      coefficient (canonicalProduct nodes factors) (nodes.length-1) := by
  exact newtonFunctional_product nodes factors

-- manuscript-contract: VolumeLogic.quotientProduct_assoc
example (nodes first second third : List R) :
    monicRemainder nodes (polyMul
      (monicRemainder nodes (polyMul first second)) third) =
      monicRemainder nodes (polyMul first
        (monicRemainder nodes (polyMul second third))) := by
  exact quotientProduct_assoc nodes first second third

-- manuscript-contract: VolumeLogic.quotientProduct_double_head_derivative
example (node : R) (otherNodes first second : List R) :
    formalDerivativeValue
      (monicRemainder (node::node::otherNodes) (polyMul first second)) node =
      formalDerivativeValue first node * horner second node +
        horner first node * formalDerivativeValue second node := by
  exact quotientProduct_double_head_derivative node otherNodes first second

-- manuscript-contract: VolumeLogic.polynomialResolvent_identity
example (nodes : List R) (element : R)
    (annihilated : horner (monicPolynomial nodes) element = 0) (power : Nat) :
    coefficient (timesLinear element (polynomialResolvent nodes element)) power =
      coefficient (monicPolynomial nodes) power := by
  exact polynomialResolvent_identity nodes element annihilated power

-- manuscript-contract: VolumeLogic.newtonFunctional_resolvent_reproduces
example (nodes coefficients : List R) (element : R) (positiveDegree : nodes ≠ [])
    (annihilated : horner (monicPolynomial nodes) element = 0) :
    newtonFunctional nodes (polyMul coefficients (polynomialResolvent nodes element)) =
      horner coefficients element := by
  exact newtonFunctional_resolvent_reproduces nodes coefficients element positiveDegree annihilated

end PolynomialAlgebra

-- manuscript-contract: VolumeLogic.face_grid_selection_iff
example (level exteriorExponent markedExponent : Nat) (ordinaryExponents : List Nat)
    (positiveLevel : 0 < level)
    (totalDegree : exteriorExponent+markedExponent+ordinaryExponents.sum ≤
      ordinaryExponents.length*(level-1)) :
    (markedExponent % level = 0 ∧
      ∀ exponent ∈ ordinaryExponents, exponent % level = level-1) ↔
      (exteriorExponent = 0 ∧ markedExponent = 0 ∧
        ordinaryExponents = List.replicate ordinaryExponents.length (level-1)) := by
  exact face_grid_selection_iff level exteriorExponent markedExponent
    ordinaryExponents positiveLevel totalDegree

section OrderedScalarComparisons
variable {R : Type u} [CommRing R] [LE R] [LT R]
  [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]

-- manuscript-contract: VolumeLogic.doubled_flattening_gain
example (flatten entropy energy defect : R) (nonnegative : 0 ≤ flatten)
    (small : flatten*energy ≤ entropy) :
    flatten*entropy-2*(1-flatten)*defect ≤
      2*flatten*entropy-2*(1-flatten)*defect-flatten*flatten*energy := by
  exact doubled_flattening_gain flatten entropy energy defect nonnegative small

-- manuscript-contract: VolumeLogic.strict_weak_balance_gain
example (flatten entropy energy : R) (positiveFlatten : 0 < flatten)
    (positiveEntropy : 0 < entropy) (small : flatten*energy ≤ entropy) :
    0 < 2*flatten*entropy-flatten*flatten*energy := by
  exact strict_weak_balance_gain flatten entropy energy positiveFlatten positiveEntropy small

-- manuscript-contract: VolumeLogic.nonempty_sector_gap
example (central actionCost gap selectedLoss : R) (additionalLosses : List R)
    (paysCost : actionCost+gap ≤ selectedLoss)
    (nonnegative : ∀ loss ∈ additionalLosses, 0 ≤ loss) :
    central+actionCost-(selectedLoss+total additionalLosses) ≤ central-gap := by
  exact nonempty_sector_gap central actionCost gap selectedLoss additionalLosses paysCost nonnegative

-- manuscript-contract: VolumeLogic.filled_remainder_strictly_below
example (complete sourceGap actionDrop filled : R) (positiveGap : 0 < sourceGap)
    (dropBelowGap : 2*actionDrop < sourceGap) (filledLower : complete-actionDrop ≤ filled) :
    complete-sourceGap < filled := by
  exact filled_remainder_strictly_below complete sourceGap actionDrop filled
    positiveGap dropBelowGap filledLower

-- manuscript-contract: VolumeLogic.protected_sum_certified_rate
example (sector : ProtectedSector) (firstOutside secondOutside : Bool)
    (a b c qa qc restFirst restSecond targetFirst targetSecond phiFirst phiSecond gapFirst gapSecond : R)
    (triangleFirst : b ≤ qa) (triangleSecond : b ≤ qc)
    (firstUpper : restFirst+protectedFirstRate sector b c qc-targetFirst ≤ phiFirst)
    (secondUpper : restSecond+protectedSecondRate sector a b qa-targetSecond ≤ phiSecond)
    (firstCertificate : (firstOutside || protectedFirstSide sector) = true →
      restFirst+protectedFirstRate sector b c qc-targetFirst ≤ phiFirst-gapFirst)
    (secondCertificate : (secondOutside || protectedSecondSide sector) = true →
      restSecond+protectedSecondRate sector a b qa-targetSecond ≤ phiSecond-gapSecond)
    (noncentral : firstOutside = true ∨ secondOutside = true ∨ sector ≠ .central)
    (positiveFirst : 0 < gapFirst) (positiveSecond : 0 < gapSecond) :
    restFirst+restSecond+protectedBridgeRate sector a b c qa qc-
      (targetFirst+targetSecond-2*b) ≤ phiFirst+phiSecond-protectedMin gapFirst gapSecond ∧
    restFirst+restSecond+protectedBridgeRate sector a b c qa qc-
      (targetFirst+targetSecond-2*b) < phiFirst+phiSecond := by
  exact protected_sum_certified_rate sector firstOutside secondOutside a b c qa qc
    restFirst restSecond targetFirst targetSecond phiFirst phiSecond gapFirst gapSecond
    triangleFirst triangleSecond firstUpper secondUpper firstCertificate secondCertificate
    noncentral positiveFirst positiveSecond

-- manuscript-contract: VolumeLogic.protected_sum_central_total
example (b qa qc restFirst restSecond targetFirst targetSecond : R) :
    restFirst+restSecond+(qa+qc)-(targetFirst+targetSecond-2*b) =
      (restFirst+(b+qc)-targetFirst)+(restSecond+(qa+b)-targetSecond) := by
  exact protected_sum_central_total b qa qc restFirst restSecond targetFirst targetSecond

-- manuscript-contract: VolumeLogic.protected_finite_assembly_gap
example (blockCostsAndActions : List (R × R)) (assembled gap : R)
    (assemblyBound : assembled ≤ total (blockCostsAndActions.map Prod.fst))
    (blockBounds : ∀ entry ∈ blockCostsAndActions, entry.1 ≤ entry.2)
    (activeBlock : ∃ entry ∈ blockCostsAndActions, entry.1 ≤ entry.2-gap)
    (positiveGap : 0 < gap) :
    assembled ≤ total (blockCostsAndActions.map Prod.snd)-gap ∧
      assembled < total (blockCostsAndActions.map Prod.snd) := by
  exact protected_finite_assembly_gap blockCostsAndActions assembled gap
    assemblyBound blockBounds activeBlock positiveGap

-- manuscript-contract: VolumeLogic.boundary_certified_rate
example (sector : ProtectedSector) (coreOutside blockOutside : Bool)
    (a b c t qa qc restCore restBlock targetCore targetBlock phiCore phiBlock gapCore gapBlock : R)
    (removedTriangle : b ≤ t) (firstTriangle : b ≤ qa) (secondTriangle : b ≤ qc)
    (coreUpper : restCore+protectedFirstRate sector t c qc-targetCore ≤ phiCore)
    (coreCertificate : (coreOutside || protectedFirstSide sector) = true →
      restCore+protectedFirstRate sector t c qc-targetCore ≤ phiCore-gapCore)
    (blockCertificate : (blockOutside || protectedSecondSide sector) = true →
      restBlock+protectedSecondRate sector a t qa-targetBlock ≤ phiBlock-gapBlock)
    (entireBlockCentral : (blockOutside || protectedSecondSide sector) = false →
      restBlock+protectedSecondRate sector a t qa-targetBlock ≤ phiBlock+2*(t-b))
    (conditionalPacking : (blockOutside || protectedSecondSide sector) = false → t ≤ qa)
    (noncentral : coreOutside = true ∨ blockOutside = true ∨ sector ≠ .central) :
    restCore+restBlock+protectedBridgeRate sector a t c qa qc-
      (targetCore+targetBlock-2*b) ≤ phiCore+phiBlock-protectedMin gapCore gapBlock := by
  exact boundary_certified_rate sector coreOutside blockOutside a b c t qa qc
    restCore restBlock targetCore targetBlock phiCore phiBlock gapCore gapBlock
    removedTriangle firstTriangle secondTriangle coreUpper coreCertificate blockCertificate
    entireBlockCentral conditionalPacking noncentral

-- manuscript-contract: VolumeLogic.boundary_conditional_action_cancels
example (core block twiceTriangle joiningLogWeight : R) :
    core+(block+2*(twiceTriangle-joiningLogWeight))-
      2*(twiceTriangle-joiningLogWeight) = core+block := by
  exact boundary_conditional_action_cancels core block twiceTriangle joiningLogWeight

-- manuscript-contract: VolumeLogic.boundary_total_central_block
example (sector : ProtectedSector)
    (a b c t qa qc restCore restBlock targetCore targetBlock : R)
    (blockRootInactive : protectedSecondSide sector = false)
    (conditionalTriangle : t ≤ qa) :
    restCore+restBlock+protectedBridgeRate sector a t c qa qc-
      (targetCore+targetBlock-2*b) ≤
      (restCore+protectedFirstRate sector t c qc-targetCore)+
      (restBlock+protectedSecondRate sector a t qa-targetBlock)-2*(t-b) := by
  exact boundary_total_central_block sector a b c t qa qc restCore restBlock
    targetCore targetBlock blockRootInactive conditionalTriangle

-- manuscript-contract: VolumeLogic.boundary_noncentral_block_margin
example (assembled coreCost blockCost phiCore phiBlock blockGap twiceTriangle joiningLogWeight : R)
    (join : assembled ≤ coreCost+blockCost-(twiceTriangle-joiningLogWeight))
    (coreBound : coreCost ≤ phiCore) (blockBound : blockCost ≤ phiBlock-blockGap) :
    assembled ≤ phiCore+phiBlock-blockGap-(twiceTriangle-joiningLogWeight) := by
  exact boundary_noncentral_block_margin assembled coreCost blockCost phiCore phiBlock
    blockGap twiceTriangle joiningLogWeight join coreBound blockBound

end OrderedScalarComparisons

section CoherentAssembly
variable {I : Type u} {A : Type v} {B : Type w}
  [CommRing A] [CommRing B]

-- manuscript-contract: VolumeLogic.filled_remainder_identity
example (allSectors : List I) (sector : I → A) (whole central : A) (fill : A → B)
    (completeDecomposition : whole = central+sectorSum allSectors sector)
    (zero : fill 0 = 0) (additive : ∀ x y, fill (x+y) = fill x+fill y) :
    fill whole-fill central = sectorSum allSectors (fun index => fill (sector index)) := by
  exact filled_remainder_identity allSectors sector whole central fill
    completeDecomposition zero additive

-- manuscript-contract: VolumeLogic.finite_sector_filling_bound
example {R : Type z} [CommRing R] [LE R] [LT R]
    [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]
    (allSectors : List I) (sector : I → A) (whole central : A)
    (fill : A → B) (polynomialSize : A → R) (absoluteValue : B → R)
    (degreeAdmissible : A → Prop) (weights : I → R) (operatorCost envelope : R)
    (completeDecomposition : whole = central+sectorSum allSectors sector)
    (fillZero : fill 0 = 0) (fillAdd : ∀ x y, fill (x+y) = fill x+fill y)
    (normZero : absoluteValue 0 = 0)
    (triangle : ∀ x y, absoluteValue (x+y) ≤ absoluteValue x+absoluteValue y)
    (nonnegativeCost : 0 ≤ operatorCost)
    (eachDegree : ∀ index ∈ allSectors, degreeAdmissible (sector index))
    (operatorBound : ∀ polynomial, degreeAdmissible polynomial →
      absoluteValue (fill polynomial) ≤ operatorCost*polynomialSize polynomial)
    (eachBound : ∀ index ∈ allSectors,
      polynomialSize (sector index) ≤ weights index*envelope) :
    absoluteValue (fill whole-fill central) ≤
      operatorCost*sectorSum allSectors weights*envelope := by
  exact finite_sector_filling_bound allSectors sector whole central fill polynomialSize
    absoluteValue degreeAdmissible weights operatorCost envelope completeDecomposition
    fillZero fillAdd normZero triangle nonnegativeCost eachDegree operatorBound eachBound

-- manuscript-contract: VolumeLogic.simultaneous_sector_threshold
example (allSectors : List I) (individualThreshold : I → Nat)
    (levelScope : Nat → Prop) (estimate : I → Nat → Prop)
    (individual : ∀ index ∈ allSectors, ∀ level,
      individualThreshold index ≤ level → levelScope level → estimate index level) :
    ∀ level, sectorThreshold allSectors individualThreshold ≤ level → levelScope level →
      ∀ index ∈ allSectors, estimate index level := by
  exact simultaneous_sector_threshold allSectors individualThreshold levelScope estimate individual

end CoherentAssembly
end VolumeLogic.ManuscriptContracts
