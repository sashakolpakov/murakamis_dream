# Appendix O to Appendix P: bounded geometric implication audit

This is a read-only audit of the geometry interface, not a certification
of every analytic proof in the manuscript. It checks the hypotheses
needed to pass from the central source action to the marked filling and
its metric volume, and the use of that conclusion in Appendix P.
No numerical constants or Fourier-tail estimates were recomputed.

The exact snapshots, a section-level implication graph, symbolic
normalization checks, and internal-reference checks are stored in
\(\texttt{weak-balance-geometry-snapshot.json}\). Its reproducible
checker is \(\texttt{check_weak_balance_geometry.py}\).
The checker uses exact symbolic algebra and a graph acyclicity check;
it is not a proof assistant.

No concrete missing hypothesis or circular inference was found in this
bounded interface read. The conclusion relies on the local geometric
and finite-source theorems listed below. The audit does not replace
their proofs.

## 1. Exact input and output types

The input to the geometric part of Appendix O is:

1. A finite simple triangulated oriented sphere with at least four
   vertices; a perfect matching of the cubic dual; a nonmatching marked
   edge; and the actual cyclic frame of every matched quadrilateral.
2. The inverse-cut diagram in \(S^3\), or an existing diagram whose
   labeled cut is this data. The local disk maps and their original
   twice-punctured disk collars are retained.
3. A fixed retained half-twist vector
   \(\epsilon_e\in\{-1,0,1\}\). The original terminal graph determines
   the number of main components; a knot conclusion requires it to be
   connected.
4. Integers \(p_e\), fixed before the quantum level, with
   \(n_e=\epsilon_e-2p_e\) independently sufficiently long. The
   threshold depends on the complete fixed diagram and frames.

The general Morse source identity alone allows more combinatorics,
but the current geometry theorem uses the simple-sphere input above.
There is no transfer to an arbitrary tensor graph, a non-simple
cellulation, or an arbitrary auxiliary representation.

The geometric output is a complete finite-volume metric on the
original auxiliary filling, with every main cusp complete. The knot
case is the original \(S^3\setminus K_{\boldsymbol p}\). The analytic
output in Appendix O is only the nonzero all-central contribution.
Appendix P adds the separate weak-balance or quantified remainder
hypothesis to conclude the full-invariant limit.

In particular, neither “central” nor “geometric contribution” means
that its finite coefficient is a separate topological invariant.

## 2. Section-level dependency map

The following are the substantive arrows. The JSON records 19 nodes
and their exact dependencies.

| Conclusion | Required input and location |
|---|---|
| Original augmented diagram, basis and parity | O, \(\texttt{mcg:sec-1}\)–\(\texttt{mcg:sec-2}\); \(\texttt{research_matched_sphere_morse_source.md}\), §§1–4 |
| Positive right-angled cut certificate | Initial simple-sphere construction in \(\texttt{actual_balanced_terminal_fan_volume.md}\), §2, before any fan |
| Complete augmented metric | Original white/shaded pairings and rectangular links in O, \(\texttt{mcg:sec-2}\); matching-geometry proof |
| Exact finite source with its mark | O, \(\texttt{mcg:sec-3}\); general Morse compiler, §§5–6 |
| Complete action and stationarity | Original determinant calibration and actual facet coning in \(\texttt{actual_original_boundary_stationary_character.md}\), near equations (11)–(13) |
| One analytic pattern and source saddle | O, \(\texttt{mcg:sec-4}\); marked circle-pattern Jacobian proof |
| Actual framed group representation | O, \(\texttt{mcg:sec-5}\); full primitive collar and local Morse relations |
| Corrected representation-volume action | O, \(\texttt{mcg:sec-6}\); fixed fundamental-chain peripheral differential and the complete anchor |
| Smooth primitive filling | O, \(\texttt{mcg:sec-7}\); nearby framed metric-completion theorem, §§1–6 |
| Nonzero central period | O analytic part, H1/H2 and all-charge analysis; this is a separate analytic theorem |
| Full invariant under weak balance | P's shared-torus remainder, N's exact Hermite norm, then the central asymptotic and filled metric from O |

There is an apparent note-level cross-reference between L and O:
L's later full-volume discussion refers to O, while O refers to the
balanced-fan note. At the level actually used in the proofs, the
arrows are acyclic. O uses the initial packing construction and exact
finite Morse source, not L's full-volume conclusion or its bound on
one-sided sectors. P does not feed into any geometric premise of O.

The positive marked-gluing rigidity theorem is not being used as a
substitute for a metric-completion theorem. The latter is separately
constructed in O. Likewise, an agreement of cusp Hessians is not the
basis for the action identification: the exact peripheral one-form is
retained.

## 3. Complete geometry and absolute normalization

The inverse construction retains the physical pairing
\((0,1),(2,3)\), distinct from the shaded grouping
\((1,2),(3,0)\), in its stated local numbering. Odd half twists use
\((0,2),(1,3)\) with their signed paths. This agrees with the cited
inverse-cut construction. The complement is therefore determined
before its source or metric is studied.

The simple-sphere certificate-removal argument has separate ingredients:
strict finite Hall feasibility; exclusion of boundary entropy maxima;
an interior multiplier solution; injectivity of the developed center
triangles; and disjoint supporting circles/halfspaces. Strict
feasibility alone is not asserted to prove interiority. These steps
are contained in the cited initial construction, not deduced from the
later volume limit. Their role in this audit is to establish the
complete positive geometric anchor.

At that anchor, the original coefficient uses two protected zero
curvatures and ordinary target \(d=N-1\) on each remaining face.
The source triangle has load sum \(1/2\), and
\[
 \partial_{\log w_f}Q_t=\frac{\theta_{tf}}{2\pi},
 \qquad
 \sum_{t\ni f}\theta_{tf}=2\pi.
\]
Consequently
\[
 P(q)=\sum_tQ_t(q)-\sum_{\text{ordinary }f}q_f,\qquad
 \nabla P(q^*)=0,\qquad P(q^*)=\Phi.
\]
The determinant normalization is fixed by its one-corner limit
\(Q(w,0,0)=\frac12\log w\), not by a freely chosen entropy constant.
Coning the actual facets of the actual polyhedron gives
\[
 2\pi\Phi=2\operatorname{Vol}(Q)=\operatorname{Vol}(Y_D).
\]
Thus P's \(Q\), ordinary targets, and \(2\pi\) convention agree with O.
The equality concerns the central complete action. It is not a
previously assumed full-source volume theorem.

The marked normalization is essential. A different positive radius
vector may be used later for Cauchy's inequality, but stationarity
and \(P(q^*)=\Phi\) in P are asserted only for the actual complete
packing.

## 4. Group relations and primitive peripheral variables

The common circle pattern is solved on a fixed small polydisk, with
the two marked lines normalized once and the last horizontal
translation removed. Its complete Jacobian proof uses the positive
ordinary-face Hessian, the two circles tangent to both lines, and
connected triangle adjacency. It does not assume a source-to-group
identification to prove its own rank.

The reflection-prefix construction satisfies the same-wire and cup/cap
relations with variable Morse headcount. The inserted \(F,G,F\) pair
cancels because \(\mathcal R_F^-\mathcal R_F^+=I\).
The full collar maps conjugate both ordered puncture generators,
not just their product or traces. This supplies every local relation
in the recorded Morse van Kampen presentation; there is no separately
assigned monodromy around a graph cycle.

Write \(P\) for the ordered disk longitude, with selected eigenvalue
\(J=-e^{-2\pi i\delta}\). The even collar \(C\) has eigenvalues
\(R_0,1\), and its complete limit retains the nontrivial parabolic
divided difference. The source equations do not replace \(C\) by the
identity at \(R_0=1\).

For all three retained signs, the meridian
\[
 \mathsf M=mR_0(J^{-1}-1)^{-\epsilon}
               C^{-1}(P^{-1}-I)^\epsilon
\]
has eigenvalues
\[
                    m,\qquad mR_0(-J)^\epsilon.
\]
Therefore
\[
 \det\mathsf M=m^2R_0(-J)^\epsilon=1,\quad
 U=-\operatorname{Log}R_0-\epsilon\operatorname{Log}(-J),\quad
 V=2\operatorname{Log}(-J)=-4\pi i\delta .
\]
These identities were rechecked symbolically for
\(\epsilon=-1,0,1\). The half-twist factor is a unit near completeness.
The logarithms are centered germs in the selected common frame.
Their meaning is the original primitive disk basis, not an arbitrary
pair of spectral eigenvalues.

Every main meridian stays noncentral parabolic. Its commuting main
longitude therefore has multiplier one. This verifies the unfilled
cusp hypothesis needed later.

## 5. Action, filling, and actual metric volume

With
\[
 A_\epsilon=A_0+\pi i\sum_e\epsilon_e\delta_e^2,
\]
the exact derivative is
\[
 dA_\epsilon=\sum_eU_e\,d\delta_e,\qquad
 d(2\pi iA_\epsilon)=-\frac12\sum_e U_e\,dV_e.
\]
The fixed fundamental-chain representation volume uses squared
similarity logs and satisfies
\[
 d\operatorname{Vol}(\rho)
 =\frac12\sum_e\left(\operatorname{Re}V_e\,d\operatorname{Im}U_e
             -\operatorname{Re}U_e\,d\operatorname{Im}V_e\right).
\]
The complete anchor then fixes the real constant:
\[
 2\pi\operatorname{Re}A_\epsilon
 =\operatorname{Vol}(\rho)
       -\frac12\sum_e\operatorname{Im}U_e\,\operatorname{Re}V_e.
\]
The checker verifies the differential identity, including its factor
\(1/2\). This is an imported fundamental-chain theorem applied to an
actual representation, not to a formal stationary algebraic solution.

The unit-charge phase is
\[
 S_{\boldsymbol1}
 =A_\epsilon-2\pi i\sum_ep_e\delta_e^2+2\pi i\sum_e\delta_e .
\]
Its critical equations give the unwrapped identity
\(U_e+p_eV_e=-2\pi i\). For \(\delta=a+ib\), direct real algebra gives
\[
 \operatorname{Re}(-2\pi ip\delta^2+2\pi i\delta)
   =4\pi pab-2\pi b
   =\frac{\operatorname{Im}U\,\operatorname{Re}V}{4\pi}.
\]
Thus \(2\pi\operatorname{Re}S_{\boldsymbol1}=\operatorname{Vol}(\rho)\).
This is not yet the filled-metric conclusion.

For that conclusion, the following additional hypotheses are checked
in O:

- The matrices and chosen flags converge to the complete framed
  representation as every \(|n_e|\) tends to infinity.
- The actual critical-point formula has
  \(\operatorname{Im}\delta_e>0\), for either sign of \(n_e\).
  Thus \(\operatorname{Re}V_e>0\) and the auxiliary longitude has
  nonunit modulus.
- The second common fixed point escapes every compact developed
  generator path. The actual logarithmic generator increments tend
  to zero, so they equal the prescribed small \(U,V\), without hidden
  \(2\pi i\) multiples, before multiplication by \(p_e\).
- The logarithmic link is a nonsingular compact flat torus with a
  rank-two period lattice. The primitive filling slope has period
  exactly \(-2\pi i\); a complementary primitive period has nonzero
  real part.

The equivariant compact-core and cusp-tail constructions then produce
a smooth solid torus with this exact meridian and complete unfilled
main cusps. The checker independently verifies the tube-coordinate
metric. This excludes the possibility of a nontrivial parabolic
filling word which only has eigenvalue one.

Finally the same finite boundary triangulation is used in the
axis-valued filling comparison. The conical boundary homotopy has
vanishing limiting volume, and the added axis-valued tetrahedra have
zero volume. Hence the representation volume above equals the
constructed filled metric volume. Surgery in the original
twice-punctured disk collar inserts \(-2p_e\) crossings, so this is the
original \(S^3\) filling, with the original knot-parity qualification.

The general completion theorem does not supply a representation for
arbitrary short slopes. Existence here comes from the independent
reciprocal-slope implicit-function argument.

## 6. What Appendix P adds

P assumes the actual complete weak-balance inequalities. Its
power-flattened weights are one common Cauchy radius vector and need
not be another circle packing. It derives a strict real-cube bound
for the entire difference between full and central sources.

The finite Hermite norm from N then transfers that source bound to
the original fixed twist insertion. Its factor
\(\prod_e(1+|n_e|/2)\) has zero exponential rate because the powers
are fixed. Repeated-node derivatives and the odd simple node are
part of that finite functional; no semisimple replacement is used.

O supplies a nonzero central asymptotic at both parities and
\[
 \operatorname{Re}S_{\boldsymbol1}
 =\Phi-O_D\left(\sum_en_e^{-2}\right).
\]
Increase the diagram-dependent twist threshold until this drop is
smaller than the already fixed remainder gap. Only then can P infer
that the full invariant has the same rate. The framing/component
characters have modulus one at complete color; the stated
\(i^{N+3}/N\) normalization also has zero exponential rate.
Neither is silently absorbed as an unknown real action.

The result is restricted to weak balance or P's quantified extension,
an original knot parity, and fixed independently long powers.
It says nothing universal about unchanged simple spheres that fail
those criteria.

## 7. Audit limits and exact checks

The file map fixes hashes for O, P, N, L and fifteen supporting notes.
The executable checks establish:

- acyclicity of the recorded 19-node implication map;
- the three signed meridian eigenvalue identities;
- the boundary-action differential and real filling correction;
- the tube-coordinate metric;
- all 99 O internal references and all 24 P internal references have
  unique targets in the manuscript sources.

Acyclicity of this selected graph is a bookkeeping check, not an
automated proof that every imported theorem is true. The analytic
H1/H2 construction, all-charge currents, and weak-balance constants
were treated as their stated established inputs; they were not
reproved here. The fundamental-chain peripheral differential and
its coisotropic pairing are nontrivial geometric dependencies,
explicitly retained above. Standard finite Hall transport,
holomorphic implicit-function, and complete-local-isometry covering
arguments are also used.

Within this stated scope, no unproved filling or full-invariant
assumption was found hidden in the geometric interface.

