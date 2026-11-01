# Bounded audit of the geometric step in Appendix M

## Scope and conclusion

This report reads Appendix M §7 and its adjoining phase/nondegenerate-Hessian statements, together with `actual_all_circle_geometric_characteristic.md` §§5–10. It also checks the ordered representation interfaces that those sections use (§§2.2–2.3, 4, 8), the relevant written positive-gluing statements, and the newly inserted same-chain paragraph in Appendix F. It does not certify the entire manuscript, replay all symbolic scripts, or reprove the all-order analytic estimates and recurrence algebra covered by the separate all-orders record.

The exact peripheral and framing argument has no additional defect identified in this bounded read. There was, however, an indirect geometric input that should not be hidden: the existing filled-meridian-germ citation went through a positive triangulation of the *filled* manifold. The replacement now included in Appendix I proves the needed local rigidity instead on the original positive augmented triangulation at the filled endpoint. It therefore removes that particular existence import for the covered all-circle family. Appendix M now cites that direct proof. The published statement explicitly concerns the decorated projective representation germ modulo conjugation; determinant-one signs are retained separately.

Source hashes and the finite implication graph are in [directed-geometry-snapshot.json](directed-geometry-snapshot.json). Line locations below refer to that snapshot.

## 1. What the previous rigidity citation actually supplied

At M lines 301–312 and characteristic lines 1203–1219, the required conclusion is precise: modulo conjugation, the decorated representation germ of the complete filled one-cusped knot is smooth of dimension one, and the prescribed main eigenvalue M is a local coordinate, retaining the source M^-1 eigenflag. This identifies an explicitly reconstructed source branch through complete holonomy with the geometric meridian germ.

The old citation chain was:

1. `actual_geometric_normal_period.md` §3, lines 124–141, invokes a positive complete ideal triangulation and its invertible marked Jacobian.
2. `geometric_rigidity_and_cyclic_source.md` §1, lines 14–47, supplies the written polarization proof conditional on such a triangulation.
3. `ge_geometric_triangulation_audit.md` §3 supplies existence by Ge's subdivision argument, conditional on the classical Epstein–Penner decomposition theorem.

The local marked rank, polarization, and decorated representation inverse have written proofs in `general_marked_multicusp_gluing_rigidity.md` §§2–3. The current bounded review read those arguments, but did **not** independently audit Ge's paper or prove Epstein–Penner. A general positive filled triangulation is not constructed by Appendix F: F constructs positive ideal cells of the original *augmented* exterior and completes its auxiliary ends. It would therefore have been inaccurate to call the old citation chain wholly internal to F or wholly checked here.

Without the cited local-uniqueness theorem, the source equations and ordered matrices still reconstruct actual filled-group representations through complete holonomy, and the preferred boundary-word identity still holds on those representations. What the old route had not independently justified at that point was uniqueness/equality with the unramified geometric meridian germ. The word identity is not itself deduced from the rigidity import.

## 2. Replacement on the retained augmented triangulation

The proof is included in Appendix I, “Local rigidity on the retained augmented triangulation,” and in Section 5 of [the geometric-characteristic note](../../notes/actual_all_circle_geometric_characteristic.md). Appendix M refers to this subsection directly.

All hypotheses are already supplied for this family:

- F lines 367, 480–497 retain distinct positive tetrahedra, full face returns and angle 2pi at the original augmented edges, including odd seams.
- F lines 501–556 give a nonunit auxiliary longitude multiplier and the primitive logarithmic period.
- F lines 556–558 identify the c=1 metric with the original smooth filled knot exterior; the main cusp remains complete.
- The original triangulation has only ideal vertices and torus links; its combinatorial edge/peripheral row identities are unchanged by incomplete auxiliary holonomy.

Let t be the number of tetrahedra and c the number of torus cusps. At this endpoint, use the positive quad derivative T_j=z_j/(1-z_j), with Im T_j>0. Append to t-c independent edge rows the main meridian and one slope mu_v+p_v lambda_v per auxiliary torus. Their classes are primitive and independent in the peripheral symplectic quotient. They form a rank-t real Lagrangian system (A B). Its Jacobian A+B diag(T_j) is invertible by polarization. The dependent affine logarithmic constants are compatible because the actual endpoint satisfies every edge equation; their compatibility does not require zero auxiliary logarithms.

The shape/representation inverse uses the actual dual two-skeleton and distinct developed triples. It applies at this incomplete point and over local Artin rings because all denominators remain units. Faithfulness of the augmented representation is not needed. For a nearby filled representation, its pullback to the augmented group has unique selected auxiliary eigenflags because the retained auxiliary longitudes have distinct eigenvalues. The main flag retains its exact prescribed eigenvalue.

The same eigenvalue splitting proves group descent over Artin rings. A longitude eigenvalue difference is a unit. A local slope representative can be normalized to identity at the residue point; its scalar commutator has square one and residue one, hence is one also over Artin rings. This does not reset a retained SL2 group-lift sign. The commuting slope is diagonal, so eigenvalue ratio one makes it scalar, hence identity in PGL2. Conversely a filled representation satisfies these slope constraints on the retained -2pi i branch. Fixing all auxiliary slope coordinates leaves the one-dimensional filled germ, with main coordinate a nonzero signed multiple of log M. On the declared source M^-1 line the ordered eigenvalue-ratio logarithm is -2 log M.

Thus the source's already proved implicit branch lands in exactly this germ and agrees with it by its prescribed M coordinate. This removes the Ge/filled-positive-triangulation import from this step only. It does not remove or validate other uses of that theorem elsewhere in the repository.

## 3. Exact source-to-representation equations

M equations (5)–(6) retain the actual physical-turn variables, the first-charge term and the framing scalar. Their conversion to the geometric equations is exact, rather than a comparison of second derivatives. Put X=exp(2pi i x), Q=exp(i tau), m=M^2. Directly from the original b integral and the insertion K,

    exp(b_x) = -(X+Q)(X+Q^-1)/(X-1)^2,
    exp(K_x) = (X-1)^2/[(1-Xm)(1-X/m)].

The two incident b factors and one K factor therefore give precisely characteristic (T1)/(R1). The independent identity

    -2pi b_tau = log[(Q+X)/(1+QX)]

follows by differentiating in x and comparing at x=0, then continuing the retained logs. Since K has no tau dependence, stationarity retains

    sum log rho = i n tau - 2pi i,
    U+pV = -2pi i,   V=2i tau,   n=epsilon-2p.

The scalar (pi i a(D)/2)t^2 does not alter these internal equations. Its explicit t derivative gives M^{a(D)} in the main longitude.

The source Hessian used to produce this implicit branch is a separate analytic assertion: the wire Hessians are invertible and successive conditional angular Schur complements are invertible. M lines 277–280 state that determinant argument. It must not be substituted for geometric representation rigidity; the replacement above supplies the latter independently.

## 4. Why these are actual marked group representations

The necessary imported local construction is stronger than matching a character polynomial:

- Native equations N5–N9 give full white/shaded face returns.
- N11–N16 determine the same source wire from both primitive auxiliary meridians, including cancellation before the Q=1 limit.
- The ordered page construction uses the original cyclic disk seams and physical turns. No open tangle commutativity or arbitrary pants permutation is used.
- S14b specifies both ordered puncture generators, their inversions at the turned endpoint, and the disk product P=ba. The Hurwitz intertwiner satisfies both generator conjugacies, not just peripheral trace matching.
- The opposite-eigenflag qualification is retained. The resulting representation is decorated by each actual positive main meridian's M^-1 flag; a native inverse loop gets the corresponding opposite selection. The old pure flags are not transported blindly through an odd seam.

These facts supply the actual original augmented group. At the selected smooth endpoint, Im tau<0 gives Q^2 != 1. It is this condition, together with full peripheral commutation, that turns similarity-one slope data into the filled-group relation. An exponentiated equation at Q=±1 would not suffice, and no such inference is made in the checked statements.

## 5. The preferred longitude is not inferred from its cusp derivative

The following distinct ingredients in characteristic §§6–10 were read:

1. Boundary Stokes gives the actual peripheral isotropy form, with the factor 1/2 because U is a ratio logarithm and log Q a single eigenvalue logarithm. The edge differential then kills the auxiliary derivatives of the squared discrepancy R=L^2/product f_e^2.
2. Independent prime squareclasses give geometric integrality of the generic source fiber over C(M), even after algebraic closure of that base. The constants argument gives R in C(M).
3. At every M0 != 0 a nonempty generic auxiliary open set gives simple edge roots, regular invertible character matrices and a regular finite atlas of ordered intertwiners. The chosen roots and minors extend to local sections through M0; isolated good points would not have been enough.
4. At M=±i the special fibers split, but their generic roots are simple. Strict matrix commutation continued from nonzero trace excludes the unwanted projective eigenline exchange. At M=±1 the main meridian is noncentral and the selected eigenvalue ratio remains a unit without division by M-M^-1.
5. Thus R has no zero or pole on C*, so R=cM^k. Only at this stage does the independent parabolic face-word cusp formula determine the exponent. It is not being used to guess a general rational factor.
6. Original surgery homology gives lambda_fill=lambda_aug mu_K^{sum p_v ell_v^2}, with ell_v=0,±2. The physical writhe convention then gives a(D)=-w(D)-sum n_v.
7. The once-bordered Seifert-surface frame calculation fixes the negative determinant-one lift at the actual complete filled knot. It is independent of the desired source formula. The even linking numbers ensure compatibility with pulling the lift back through the augmented exterior.

The generic algebra lemma allows simple graphs, but the actual geometric assembly here remains a finite literal tree with the stated main-knot test. This audit does not extend it to cyclic tensor graphs or unrelated diagrams.

The earlier parabolic face-word cusp calculation remains an imported written proof. This turn checked its statement, near-complete comparison, retained-wire Legendre interface and absence of reliance on the later full longitude identity, but did not replay every rational face-map identity in that earlier note. Likewise the topological edge/peripheral intersection identities remain named mathematical inputs; finite script checks are not substitutes for their proofs.

## 6. Normalizations in M §7

The conventions are mutually compatible:

- M=exp(pi i t) and the source uses the M^-1 eigenflag; L_geom is recorded on the M line, equivalently the inverse on that source line.
- exp(K_t)=(M^2-X)/(1-M^2 X).
- With S(t) the stationary source phase and mathcal S(u)=pi i[S(u/(pi i))-S(0)], differentiation gives -exp(mathcal S'(u))=L_geom(exp u).
- The constant negative lift is retained by log[-L_geom]. Its derivative at u=0 is the preferred cusp translation ratio.
- The chain rule gives S''(0)=pi i tau_K, not 2pi i tau_K. Together with the stated evenness and exact scalar, the resulting first correction is pi i tau_K s^2/(2N).

The audit did not reprove all-order existence or translated-chart bounds. It checked the geometric interpretation and these factors conditional on the analytic statements covered by the separate all-orders record.

## 7. Revised Appendix F same-chain comparison

The insertion at F lines 593–637 addresses the previously omitted explanation. It uses the same oriented tetrahedral chain and the same finite boundary triangulation. In a common fixed-point frame, the conical map and the axis-valued comparison transform by the same peripheral complex multiplier/modulus. The displayed homotopy is therefore equivariant. On a compact fundamental cross section its horizontal derivatives are bounded, height is comparable to Y and vertical derivatives are O(Y), giving boundary homotopy volume O(Y^-2).

For a fixed 0<c<=1 it compares the metric off the axis with the representation chain. It explicitly does not infer smooth filling or group descent for c<1. At c=1 the primitive filling slope has real period zero and one full imaginary turn, so the same triangulation extends by axis-valued vertices with zero added volume. Main cusp truncation is unchanged. Consequently Vol(rho)=Vol_c uses an actual chain comparison, not equality of differentials alone.

No hidden developing-map injectivity is needed for that volume-chain identity. The separate smooth-completion argument at F lines 556–558 supplies the geometric holonomy of the original knot at c=1. The c=0 limit is kept separate, where the fixed-point description degenerates but the positive tetrahedral volume sum gives the complete constant.

## 8. Integration and limits

The new subsection replaces the previous generic filled-germ citation
in characteristic Section 5 and Appendix I. M.7 now cites it directly.
The proof defines the symplectic form and its polarization explicitly,
and keeps the main eigencharacter, quotient by conjugation, and
projective-versus-determinant-one distinction visible.

This review did not replay every symbolic identity or formally verify
local analytic geometry. The initial reading snapshots and dependencies
are recorded separately from the integrated text. The proof uses the
original augmented triangulation and its positive endpoint; it asserts
no existence theorem for arbitrary filled triangulations and no broader
volume class.
