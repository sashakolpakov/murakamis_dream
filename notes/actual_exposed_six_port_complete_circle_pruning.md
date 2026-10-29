# Complete-circle pruning through an exposed six-head source

29 October 2026. The actual saturated six-head source kills an
unsaturated triple at an EXPOSED marked white vertex, before the
unrestricted mark acts. The same argument kills unsaturated boundary
triples in the typed three-port graph substitution. This is a whole
source cancellation with all complete-circle normals retained. No
bare mark is moved through a nested cap.

## 1. The actual support theorem being used

Let O be the local ring of analytic functions at zeta=q=exp(pi i/N)
and K its fraction field. For the generic balanced highest-weight-d
physical module V_d(zeta), d=N-1, put

    Lambda_6=Inv_K(V_d(zeta)^tensor6) intersect V_d(O)^tensor6,
    S_N=Lambda_6/(zeta-q)Lambda_6.

This is the ACTUAL saturated original-source specialization, not the
span of one cup seed and not the whole enlarged root invariant space.
The [proved six-port source support](actual_six_port_three_circle_support.md)
states that on S_N the product of the three disjoint complete-circle
sectors obeys

    (L_a tensor L_b tensor L_c) S_N=0
                               whenever a+b+c<d.   (1)

Each L_j is the full root sector of L_N, including its nilpotent
first normal on a paired cluster. The source theorem proves (1) by
clearing the absent generic joint corner. No root semisimplification
or deletion of a derivative projector is involved.

## 2. A literal six-head ordinary removal

Take the ordered NC/Morse graph and exposed white vertex v of the
[corrected first-normal theorem](actual_nc_morse_graph_first_normal_source_reduction.md).
Its three edge slots are in increasing order. Omit ALL THREE cap arcs
of that white vertex. All other white cap arcs are ordinary. Because
the outer arc of v is exposed, these remaining caps can be removed
in their actual innermost Morse order without closing or passing over
any of the six retained physical heads. The last six heads are exactly
the three ordered consecutive pairs at v.

Also temporarily omit the three pair coupons incident to v. Define
Y(zeta) to be the remaining physical six-head column, with the original
cup source and every other edge coupon present in its chosen regular
generic Hopf lift. Every cup, cap removal and internal edge map is a
regular generic Hopf map. Thus

    Y(zeta) in Lambda_6,
    Y(q) in S_N.                                   (2)

The generic lifts may be analytic full-cluster Casimir polynomials,
or the explicitly regular h0 W(zeta)pi(zeta) lifts with the correct
root value. They must not be singular individual generic projectors.
Membership (2) uses only their regularity and covariance. Actual
integer H=0 is preserved by the source, coupons and cap removals.

The omitted three coupons touch NONE of the other removed cap heads.
They can therefore be applied LAST to the retained six heads as an
exact index contraction. This is a commutation of maps on disjoint
indices, not a braid or a tensor flip. For their original exponents,
the observed physical column is

    Y_obs=(R^(e1)L_a tensor R^(e2)L_b
                                  tensor R^(e3)L_c)Y(q). (3)

The R powers preserve each paired source and are invertible, so (1)
gives Y_obs=0 when a+b+c<d. Only AFTER this equality are the three
remaining arcs closed by two ordinary caps and the original full m.
Consequently their marked source is zero, without invoking any local
invariant property of m or replacing it by an ordinary covector.

The conclusion holds for every internal channel assignment, with all
its phases and normals. It proves that an exposed marked-white
unsaturated term in the first-normal formula cancels COHERENTLY:

    [product_(other vertices)s_v(0)]
                    s_mark'(0) Xi_Gamma(0)=0.       (4)

If another source factor is zero the same conclusion already follows
directly or by the multiple-zero rule. A local s_mark' can be nonzero;
(4) is a whole-source compatibility relation, not its local deletion.

Together with the existing black and ordinary-white zero statements,
the complete exposed NC graph source can be summed using ONLY labels
with J_v>=d at EVERY vertex, including the marked one.

## 3. The unsupported three-port seam is zero before its exterior

For the typed graph substitution in
[the three-port sewing theorem](actual_nc_three_port_source_sewing.md),
B has an outer white block on slots (0,k,E_B-1). Omit its three caps
and its three incident pair coupons. This is exactly the ordinary
removal above, giving a physical Y_B(q) in S_N. In the new graph its
three boundary coupons occur ONCE each on the merged edges; all
other maps lie in B or in A's exterior. Their product annihilates
Y_B(q) when the shared triple has sum <d. Hence the entire B source
column is zero before pairing with ANY exterior supplied by A.

Thus the unsupported triangular seam term is zero as an actual
source, not a zero divided by a marked theta scalar. The exact whole
raw gluing rule is

    Z_new=sum_(a+b+c>=d)
             Z_A(a,b,c) Z_B(a,b,c)/Z_theta(a,b,c).   (5)

The complete coherent interior sums are taken inside each Z_A,Z_B;
the three shared boundary labels are summed once and stay correlated.
Z_theta is the proved strictly positive all-channel marked expression.
There is no omitted unsaturated correction in THIS typed complete-
circle operation. An ordinary open coefficient may have nonzero
higher normals there, but the original fixed first-normal source is
zero by (1)--(3).

## 4. What is not annihilated

An unsupported open S_N cell can carry a nonzero marked functional.
Equation (1) kills its TOP COMPLETE-CIRCLE observation, not the cell
or its lower moments. The correlated boundary torsor is unchanged.
Nor does this argument apply to a bare mark at a nested cap: omitting
that vertex can leave enclosing cap annuli across the retained heads,
so the same untransported six-head array need not satisfy (2).

The assumption of COMPLETE circle color is essential. Replacing
L_N by a different ordinary auxiliary color gives different spectral
values and normals; its product is not the top product in (1).
No auxiliary-color corridor or filling-current pruning is asserted.

The [focused sewing audit](../experiments/audit_actual_nc_three_port_source_sewing.py)
constructs the actual physical Y before boundary circles, checks its
ordinary six-head Ward equations and extracted divided-power kernel,
then verifies its full observed zero on an unsaturated boundary.
The all-N proof is the regular-source membership and the already
proved all-N source support (1), not extrapolation from those levels.

Independent internal review: root read the complete typed argument
against the source-support theorem and confirmed the cap-removal
order, exact saturated-lattice membership, regular lifts and disjoint
coupon commutation. The focused audit passes nineteen sewings and
five actual six-head ordinary/divided-current and pruning families;
the nested-cap countercurrent is explicitly retained. This is a
source theorem, not a norm estimate or a general graph-volume claim.

The global audit agent subsequently read the full pruning and whole
three-port sewing proofs and freshly replayed those physical tests,
including the nonzero source before the unsupported circle product
and the nested-cap countercurrent: PASS. No further correction was
required after the exposed-pointing hypothesis was made explicit.
