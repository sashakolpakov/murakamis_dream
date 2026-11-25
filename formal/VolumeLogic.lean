import VolumeLogic.FiniteSupport
import VolumeLogic.FiniteAlgebra
import VolumeLogic.RateComparison
import VolumeLogic.ProtectedSum
import VolumeLogic.MonicRemainder
import VolumeLogic.MonicLinearity
import VolumeLogic.MonicUniqueness
import VolumeLogic.MonicProduct
import VolumeLogic.TriangularBoundary
import VolumeLogic.FaceGridSupport
import VolumeLogic.ResolventFunctional
import VolumeLogic.SourceAssembly

/-!
Finite coefficient and support lemmas used by the active volume reference:
canonical confluent remainders and resolvents, the actual face-grid degree
selector, coherent sector assembly, and the scalar protected/boundary
comparisons. The concrete complex rate argument is in the Mathlib project.
-/
