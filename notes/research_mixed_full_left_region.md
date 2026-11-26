# The complete left integration region

Research theorem, 4 November 2026. All local derivative certificates
and their separate replays are complete. The argument below combines
them with the established finite-source and plateau estimates.

This note proves their consequence for the original finite cyclic sum. In particular, the conclusion is a
statement about a specified integration region, not yet a statement
about the full knot invariant.

## 1. The restricted integral

Fix a cyclic word of length \(m\ge1\) in the original three- and
four-crossing blocks. Its geometric critical point is \(r\), its
allocated phase is \(\Phi\), and its critical rate is
\[
                          M=\Re\Phi(r).
\]
All original normalization factors, Fourier polynomials, rows and
integer-level parities are retained. Define
\[
 Q=[.1,.45]^m,\qquad Y=[.12,.45]^m,\qquad P=[.22,.45].
                                                               \tag{1}
\]
For a subset \(S\) of the type-four positions, let
\(\mathcal I_{N,S}(D)\) be its original selected Laurent integral
over the real parameter set \(D\), on the
[earlier selected contour](research_mixed_early_selected_transport.md).
Thus each subset uses the exact contour prescribed for that subset.
Write
\[
                \mathcal Z_N(D)=\sum_S\mathcal I_{N,S}(D).
                                                               \tag{2}
\]
The sum has finitely many terms because the word is fixed before
\(N\) tends to infinity. Restricting its parameter set does not
produce a topological invariant; (2) is notation for part of the
exact contour formula.

Let \(\mu>0\) be a lower bound for the negative real Hessian on
the unselected plateau, as in the
[minimum-level transport argument](research_mixed_minimum_level_transport.md),
equation (11). The four possible local block types and compactness
allow the same positive \(\mu\) at every fixed cycle length.
No numerical value for it is needed below.

## 2. Assembly from the local inequalities

The two formerly pending local inputs are now established:

1. All 192 unselected half inequalities hold on their complete
   domains, including the separate verification of their saved cover.
2. All 175 charts in the
   [one-early-neighbor comparison](research_mixed_one_early_neighbor_transport.md)
   satisfy their positive half inequalities.

Together with the completed 78 constant-selected and 50
frozen-neighbor domains, these supply every local inequality used below.
The proof does not insert an additional saddle-point or positivity
assumption.

**Theorem 1.** Put
\[
                   \delta=\min\{1/2000,\mu/1600\}>0.
\]
There are constants \(C,A\), depending on the fixed word, such that
\[
 \left|\mathcal Z_N(Q)-\mathcal I_{N,\varnothing}(P^m)\right|
                \le C N^A e^{N(M-\delta)}                  \tag{3}
\]
at all sufficiently large integer levels. In particular, the
restricted sum \(\mathcal Z_N(Q)\) has the same nonzero geometric
leading coefficient, exponential action, unit factor and level power
as the original unselected central integral. That level power is
\(N^0\) for this cyclic source.

**Proof.** First consider \(Y\). With no selected positions, the
192 half inequalities imply nondecrease of the phase when all current
minimum coordinates are raised together to .22. If the initial point
lies outside \(P^m\), at least one endpoint coordinate equals .22,
while every geometric real coordinate is at least .27. The plateau
Hessian bound therefore gives phase loss \(\mu/800\). The complete
source theorem, with a fixed tolerance smaller than \(\mu/(1600m)\),
gives
\[
 |\mathcal I_{N,\varnothing}(Y\setminus P^m)|
                       \le C_0N^{A_0}e^{N(M-\mu/1600)}.
                                                               \tag{4}
\]

For a nonempty selection, the selected heights on \(Y\) are
constant. The 192 unselected and 78 selected half inequalities give
the local derivative condition in the earlier selected contour
argument. Its full Fourier correction is constant along the path
below .22. At the plateau endpoint, at least one selected block has
the established strict loss. Consequently
\[
 |\mathcal I_{N,S}(Y)|
                       \le C_SN^{A_S}e^{N(M-1/200)}
                       \qquad(S\ne\varnothing).             \tag{5}
\]
This includes the selected terms on \(P^m\) itself.

It remains to consider points in \(Q\setminus Y\). Up to boundary
sets of measure zero, they are partitioned by the nonempty set
\(B\) of positions in \([.1,.12]\). Keep those coordinates fixed.
Also keep fixed every non-early position whose two neighbors belong
to \(B\); both its incident blocks already have the direct early
estimate. Raise the minimum of the other coordinates to .22.

A moving center has either no early neighbor or exactly one. The
192, 78 and 50 domain calculations handle the first case. The second
local input handles the second case. Their inequalities retain every affected
height derivative, and the fixed-early transport argument therefore
makes the full selected rate nondecreasing along this path.

At its endpoint, every moving position is on the plateau. The fixed
isolated positions have only early incident blocks, even if their
own real coordinates are below .22. The early/plateau incidence
argument consequently applies without change: each reset cost is
paid once, and at least one early block supplies a positive loss.
The complete source estimate yields, for every selection and every
nonempty \(B\),
\[
 |\mathcal I_{N,S}(\text{region with early set }B)|
                         \le C_{S,B}N^{A_{S,B}}e^{N(M-1/2000)}.
                                                               \tag{6}
\]
The proof is precisely the conditional proposition in the
[fixed-early transport note](research_mixed_frozen_early_transport.md),
whose local hypothesis has now been supplied by the stated inputs.

All contours in (4)--(6) lie in the established enlarged cap and
plateau source products. Their Jacobians have the fixed bound
\((38/25)^m\). There are finitely many selections and early sets;
their constants and polynomial powers can therefore be absorbed in
\(C N^A\). The boundaries of the partition have measure zero and
do not change these integrals. Summing (4)--(6) proves (3).

The central unselected integral has its previously proved nonzero
asymptotic. An error with the strict exponential loss in (3) cannot
cancel its leading coefficient. This proves the last assertion.
\(\square\)

## 3. What is still outside this conclusion

The proof uses no positivity of the original summands and no claim
that a nonzero local coefficient automatically survives a further
summation. Its lower-bound consequence comes from retaining that
coefficient and estimating every other part of the specified region.

Coordinates below .1, coordinates above .45, and configurations mixing
those coordinates with the left transition are outside (3). The
separate low/plateau/right theorem controls another collection of
regions, but the mixed configurations between the two collections
must still be bounded. Nor does a cyclic result retain the external
variables needed to insert the short tangle into an arbitrary partial
filling. Thus (3) does not prove the full-period theorem or the
finite-exception theorem.
