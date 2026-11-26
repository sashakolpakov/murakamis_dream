# The main-meridian operator interface after strict-tree volume equality

Private continuation inventory, 31 October 2026. This file is not a new
claim of an AJ theorem or a module comparison.

## 1. What is already available

The following are actual source theorems in the repository, independently
read in full for this inventory.

1. `notes/kashaev_ado_pointing.md` and `notes/root_orbit_pointing.md`
   identify the zero-framed reduced literature ADO family. Distinguish
   its raw unrolled variable x=q^alpha from the marked variable M=-qx.
   If f_N denotes the raw family, put F_N(M)=f_N(-q_N^(-1)M).
   Then F_N(-q_N^j)=C_j(q_N), 1<=j<=N, and F_N(1)=K_N.
   The complete raw point is x=-q_N^(-1), not x=1.
2. `notes/finite_sum_annihilator.md` gives a nonzero genuine all-level
   ADO annihilator by a generic finite cut-state lift, not by taking a
   ratio of invariant values. The filtered boundary count includes
   codimension strata; lowest internal exponential moments repair
   vanishing under summation; a central (q^N+1) factor is removed BEFORE
   root specialization. The localized actual ideal therefore has a
   monic minimum-order generator.
3. `notes/all_level_a_period.md` reconstructs K_N from ANY such fixed
   operator and finitely many fixed-color Laurent polynomials. Cross-level
   rigidity gives a generic recurrence; the whole q-germ of its ordered
   companion product is the actual period. The needed jet order is at
   most D(s-1), independent of N. This does not assume a simple root,
   semisimplicity, root-kernel rank one, or a regular forward orbit.
4. `notes/pointed_a_gram_period.md` realizes the same finite pointing as
   a positive ratio of coefficients of banded Gram determinants. Its
   exact value is sum_{j=j_*}^N |C_j(q_N)|^2. All ordinary j<N terms
   have polynomial size, so the ratio has the same exponential rate as
   |K_N|^2 whenever the complete volume is positive.
5. `notes/actual_conway_all_strict_tree_long_twist_volume.md` now proves
   the original K_N volume equality for every fixed strict literal tree
   with all independent fixed twist weights sufficiently long and its
   actual endpoint pairing a knot. Consequently the operator period and
   the positive Gram ratio have their desired volume limits in that
   class. No additional operator construction is needed for this
   corollary.

The durable corollary requested by the parent is
`notes/actual_conway_pointed_quantum_a_volume.md`. It must keep the
marked variable M throughout the fixed-color recurrence.

## 2. What is not supplied by the scalar theorem

The full meridian ADO state is

    N_N(M)=d_N(M)F_N(M),
    d_N(M)=i^(N+3) M^(N-1)/(1+M^2+...+M^(2N-2)).

Its complete whole germ is i^(N+3)K_N/N. The full/reduced Ore gauge
is T -> g(q,M)T, with

    g(q,M)=-q^(-1)(q^2 M^2-1)/(M^2-1).

The actual state, its source, the complete evaluation and this lattice
are fixed. An arbitrary levelwise norm-torsor section is not an
alternative permissible choice. In particular a rootwise ratio
F_N(q_N M)/F_N(M) constructs an equation FROM the already known state;
it is not the all-level operator supplied by finite elimination.

The existing long-filling saddle varies auxiliary crossing-circle
colors while the main meridian stays complete. Its complex color packet
cannot be relabeled as a main-meridian ADO WKB germ. Thus the scalar
limit at M=1 proves neither that an operator's classical symbol contains
the geometric main-meridian A-factor nor that its cyclic module is the
marked regulator module.

There is an exact reason to separate root-central and classical curves.
At q_N, the rational actual state is a quotient solution of the cyclic
module in C(M) with sigma(M)=q_N M. Since sigma^(2N)=1, the companion's
central monodromy has eigenvalue 1. That finite-level statement is not
the classical geometric longitude equation. The incompatibilities in
`notes/actual_meridian_companion_source_compatibility.md` rule out simply
identifying the actual source orbit with an arbitrary highest-weight
clock vector or dropping its first normal functional.

## 3. A precise sufficient missing theorem for the selected classical factor

Here is an elementary conditional lemma, independent of an AJ assertion.
Let P=sum_i a_i(q,M)T^i be an actual all-level annihilator. Clear
denominators, then remove the maximal common power of q-1, so

    P_cl(M,L)=sum_i a_i(1,M)L^i

is nonzero. Suppose a connected main-meridian complex neighborhood U
supports the actual family and a nonzero holomorphic function ell(M)
such that, for every shift in P,

    F_N(q_N^i M)/F_N(M) -> ell(M)^i

locally uniformly on U, with F_N nonzero there for all sufficiently
large N. Then

    P_cl(M,ell(M))=0 on U.

Proof: divide the exact all-level annihilation equation by F_N(M) and
take the limit term by term. The order is fixed, so this requires no
infinite-sum interchange. If (M,ell(M)) is independently identified
with an open smooth germ of the original irreducible geometric
meridian-longitude curve, that irreducible Laurent-polynomial factor
divides P_cl. Indeed the restriction of P_cl to that irreducible curve
vanishes on an analytic open set and hence identically.

A uniform nonzero WKB expansion

    F_N(e^u)=exp(N S(u)) [a(u)+O(N^(-1))], a(u)!=0,

on a fixed complex tube is sufficient for the ratio premise, with
ell(e^u)=exp(pi*i*S'(u)). More generally one needs actual control of
microscopic shift ratios of the amplitude; an o(N) bound on its log
modulus alone is insufficient. The relevant longitude must be calibrated
in the reduced convention above. Passing to full ADO introduces the
displayed rational/sign gauge, not an unrecorded normalization.

This identifies a minimal next analytic interface for *factor inclusion*:
prove the actual main-meridian shift-ratio germ and match its longitude
to the original preferred longitude. It is stronger than a complete
scalar limit and weaker than full equality of classical symbols,
multiplicities, or quantum modules.

## 4. The stronger torsor task

A module-level theorem would additionally identify the actual all-level
pointed cyclic module, or a specified quotient/subquotient carrying the
selected germ, with the quantum marked geometric module. It must retain
the fixed small-color source window, full modified-dimension lattice,
and normal at the completion divisor. A rootwise simple eigenline or
Hilbert-90 existence alone cannot make this comparison.

For covered knots the scalar norm equality is already a theorem:

    (4/N) log|operator period| -> 2 Vol/pi
                                 =log||P_hyp||.

The remaining task is the algebraic/geometric identification of the
selected module and characteristic factor, not existence of some
annihilator and not the selected complete-period volume rate.

## Audit record

Full analytical/source read completed for the finite annihilator,
all-level period, ADO pointing, quotient-color pointing and positive
Gram-period notes. The old generic state-integral/Andersen--Malusa
annihilator results concern a different state and are not used as an
identification of ADO. The literal strict-tree source theorem is the
only volume input. No runtime diagnostic, exterior proof, or knot scan
is used for the deductions above.


## Correction after the complete-meridian check, 31 October 2026

The sufficient ratio premise in Section 3 is impossible for the unchanged actual reduced state on a neighborhood containing M=1 in the positive-volume classes. Exact evenness and quotient-color pointing give F_N(q_N)=1, whereas F_N(1)=K_N grows exponentially. The new actual_ado_complete_meridian_zero_accumulation.md proves actual zeros within O(1/N), using the literal crossing degree bound. This does not refute the conditional algebraic lemma, but it excludes its proposed application to that state across completeness.

The canonical regular remainder from regularized_kashaev_period.md is the next object: subtract the ordinary-color interpolant and divide by the retained cyclotomic factor. Its scalar complete growth is known for the covered knots; a uniform main-meridian shift-ratio theorem and geometric longitude comparison remain unproved. The source must be retained in its affine equation.

The already existing peripheral_normal_period.md Section 2 also now applies unconditionally to every polynomial annihilator for the covered positive-volume knots: the operator has the boundary factor Y-1 on its right, equivalently every coefficient vanishes along its complete-color trajectory. The two-sign M version appears in the new zero note Section 7. This is an integral meridian-lattice statement; localization kills the delta quotient. It is not the geometric A-factor identification.
