# Absolute cap-star comparison: exact constrained capacity and its missing budget

31 October 2026. **Internally reviewed analytical research theorem.**
Unpublished. The original ordinary targets are one, the original protected
MAIN pair is u,v, and Phi_D is the complete capacity in the original
normalization Vol(Y_D)/(2pi). No general absolute cap bound is asserted.

The main conclusions are exact variational reductions. They explain
why the reviewed leaf and spectral-star results do not yet prove an
absolute cap-only gap. Section 5 gives a literal obstruction to the
stronger inference from LOCAL star hypotheses alone; it is explicitly
not a common-stationary counterexample.

## 1. The exact one-cap residual capacity

Name one original cap F=(u,A,v,C), with triangles uAC,uvC and matching
edge uC. Its original cap degrees are q_A=1-s,q_C=s, with 0<=s<=1/2;
u,v remain zero. Every OTHER port in this section is CROSS.

Delete only F. Let R(s) be the maximum remaining complete-triangle
entropy with residual targets

\[
r_A=s,\qquad r_C=1-s,\qquad r_f=1\ (f\text{ other ordinary}),\qquad r_u=r_v=0.\tag{1}
\]

Put R(s)=-infinity when this fiber is empty. On its compact effective
domain R is concave and upper semicontinuous, by the compact concave
triangle-flow problem. The exact original cap-sector maximum is

\[
M_{\mathrm{cap}}=\max_{0\le s\le1/2}R(s).\tag{2}
\]

The ORIGINAL complete capacity has a different interval and a local
entropy term. In the complete row F, its first triangle has loads
(0,t,1/2-t) and its second is the pure-C half-row. Hence q_A=t,
q_C=1-t, 0<=t<=1/2, and its entropy is 2f(t). Restoring its ORIGINAL
targets in (1) therefore gives

\[
\Phi_D=\max_{1/2\le s\le1}\{R(s)+2f(s-\tfrac12)\}.\tag{3}
\]

We used f(1-s)=f(s-1/2) on this interval. There is no change of mark,
vertex, source pairing or target in (2)-(3). In particular concavity
of R alone does not compare these two maxima: they use opposite halves
of its effective domain. No reflection symmetry R(s)=R(1-s) is known
for an arbitrary prescribed exterior.

At an actual finite-common-weight cap-only stationary point with
0<nu<1/2, the cap equation is L_A=L_C. The remaining CROSS allocations
attain their local triangle Legendre formulas at these SAME weights.
For every feasible s', their dual affine upper differs from its value
at nu by (s'-nu)log(L_C/L_A)=0. Consequently

\[
R(\nu)=\max_{0\le s\le1}R(s)=M_{\mathrm{cap}}.\tag{4}
\]

This needs neither differentiability of R nor a separate local
maximality assumption for a Green row: all remaining rows are complete
concave triangle rows. It does not assert existence of such a
stationary point, and does not classify arbitrary boundary maxima of
the cap-restricted sector.

## 2. The cap-forest quotient preserves every target exactly

Now allow the at most two residual caps of classified positive-value
data. Their ordinary incidence edges form a forest, as proved in
[the cap-component theorem](research_cap_star_cut_and_cross_stellar_reduction.md), section 2. Let p
be the number of caps, and relax EACH cap row from its prescribed
overloaded orientation to ANY nonnegative split of unit supply between
its two ordinary vertices. Its entropy is still zero. All other ports
remain CROSS. Call this relaxed maximum M_rel.

For a tree component with n vertices and n-1 cap edges, deleting those
edges leaves total residual target n-(n-1)=1. Every nonnegative residual
vector (r_a) on that component with sum r_a=1 is realizable by the
relaxed cap rows. To see this, first let r be concentrated at one root.
Give each edge's full unit to the vertex farther from that root; every
nonroot vertex receives one and the root receives zero. Take the convex
combination of these allocations with coefficients r_a. The restored
cap load at vertex a is exactly 1-r_a.

Thus deleting the relaxed cap rows and merging each component is an
EXACT identification of the classical flow problem. Every merged
target is one; unmerged ordinary targets remain one; protected targets
remain zero. This is a flow quotient only, not a triangulated-sphere
edge contraction or an identity coupon. The true cap orientations
impose additional inequalities and are NOT silently discarded from
the definition of M_cap.

Write the original complete weighted potential as

\[
\begin{aligned}
F_D(L)&=\sum_{t\text{ original triangle}}Q_t(L)-\sum_{a\text{ ordinary}}\log L_a,\\
\Phi_D&=\inf_{L>0}F_D(L),\qquad C_0=2f(\tfrac14)=\frac{v_{\mathrm{oct}}}{2\pi}.
\end{aligned}\tag{5}
\]

Let E_cap be the linear subspace of log weights constant on every
cap-tree component. Each cap's two ordinary weights then equal a
common B, and its COMPLETE weighted value is exactly

\[
Q(0,B,B)+Q(0,0,B)=C_0+\log B.\tag{6}
\]

In a component with n vertices and n-1 caps, the n target logs and
n-1 cap logs leave exactly one target log. Compact concave duality for
the remaining CROSS rows therefore gives the exact relaxed identity

\[
\begin{aligned}
M_{\mathrm{rel}}&=\inf_{\log L\in E_{\mathrm{cap}}}F_D(L)-pC_0
=\Phi_D+\Delta_{\mathrm{cap}}-pC_0,\\
\Delta_{\mathrm{cap}}&:=\inf_{\log L\in E_{\mathrm{cap}}}F_D(L)-\Phi_D\ge0.
\end{aligned}\tag{7}
\]

The relaxed fiber is nonempty: start with an original feasible complete
flow, remove the cap rows, and merge their components. Each cap has
unit ordinary supply, so the same component totals are one. This
also verifies the normalization in (7). Compact hypograph separation
proves the dual equality even if a boundary multiplier is not attained.

For the actual closed cap sector one only has M_cap<=M_rel. However,
at classified cap-only stationary data with all cap splits strict and
finite common ordinary weights, equality DOES hold. The cap equations
place these weights in E_cap, the complete rows attain Q, and the
original demands cancel all logarithms. The actual feasible flow
attains the dual value in (7), hence

\[
M_{\mathrm{cap}}=M_{\mathrm{rel}}=\Phi_D+\Delta_{\mathrm{cap}}-pC_0.\tag{8}
\]

This is an exact identification of the classical stationary envelope,
not a claim that Delta_cap<=p C0. The latter inequality is the missing
unsigned absolute comparison in this formulation.

## 3. What the new leaf/star mechanism proves, and what it still needs

If there are no Green ports, a nontrivial maximal-weight cap component
has a nonroot leaf whose other incident ports are all CROSS. The
reviewed star theorem therefore applies at ANY cap-child valence,
with 0<nu<1/2 from the original demand. This removes the earlier
degree-two limitation for a RELATIVE star improvement.

At the common stationary weights in (8), its weighted block envelope
touches the original sharp block action. Indeed the CROSS neighbors
supply nu to the internal A face, while the cap supplies nu to boundary
C. Their log-weight discrepancy is nu(log L_A-log L_C)=0. With the
unchanged exterior included, the full weighted envelope is precisely
the value in (8), not an unrelated independently optimized number.

The star theorem gives some eta>0 below that envelope. Other cap rows
at their equal ordinary weights have polynomial weighted size at +2,
and only an arbitrarily small extra exponential cost on a sufficiently
small complex +2 disk. Other CROSS rows have the reviewed global-real
coefficientwise endpoint majorant and its thin-strip continuation.
Thus, when using these common stationary weights and retaining the
whole internal A^d contraction, the relevant source bound has rate
at most

\[
\Phi_D+\Delta_{\mathrm{cap}}-pC_0-\eta.\tag{9}
\]

after reducing eta to absorb those small strip costs. Shared boundary
variables and original ordinary targets are retained by the ONE final
Cauchy extraction. A second cap does not involve this leaf A, so it
belongs legitimately to the unchanged exterior.

Formula (9) is an absolute gap below Phi_D IF

\[
\Delta_{\mathrm{cap}}-pC_0<\eta.\tag{10}
\]

In particular the nonstrict variational inequality Delta_cap<=p C0
would suffice, because the star gives a strict positive eta. But no
current theorem compares eta to Delta_cap-p C0 in general. The leaf
mechanism alone therefore has NOT closed cap-only high maxima.

For localizations around a stationary datum inside a larger source,
one must use the genuine boundary coefficients of the contracted star
and exterior-array fibers. Cutting individual internal cap indices
would destroy the sum controlled by the theorem. The [original block-contraction theorem](research_original_block_contraction_and_cap_budget.md)
gives that precise localization interface.

These statements make no claim about a full filling period: an
absolute fixed-strip gap on the entire relevant source complement is
still required before the existing whole-period theorem applies.

## 4. The tempting exterior packing contact is not present

Deleting F removes BOTH triangles uAC,uvC and their common MATCHING
edge uC. The remaining positive CROSS disk has boundary u-A-C-v-u.
It gives contacts uA,AC,Cv and the marked parallel-line edge uv. It
does NOT give a contact uC. Consequently L_A=L_C does not force A
to touch v by copying C's radius: the assertion that C already touches
both lines has used a missing cap contact.

There is a direct boundary-coordinate check. Suppose a positive exterior
disk development has the prescribed boundary fan loads nu and 1-nu.
Put theta=2pi nu, equal circle radius r, centers A=(0,0), C=(2r,0),
and n=(cos theta,sin theta). Let the two lines be

\[
u:\ n\cdot z=r,\qquad v:\ n\cdot z=2r\cos\theta-r.\tag{11}
\]

They are parallel; A touches u, C touches v, and A,C are tangent. The
counterclockwise fan from the AC ray at A to its u ray has angle theta.
At C the fan from its v ray to the CA ray has angle 2pi-theta. Thus
the normalized exterior loads are exactly nu,1-nu. The line separation
is

\[
H=2r(1-\cos\theta)=4r\sin^2(\pi\nu),\tag{12}
\]

not the extra-contact value 2r. For 1/4<nu<1/2 both entire disks fit
between the two lines, and neither has the other line contact. Their
distance to that other line is r-2r cos theta>r. At nu=1/4 the extra
contacts first occur.

This is a literal local boundary configuration, not a claim that every
such boundary has an embedded finite interior CROSS packing, or that
an arbitrary stationary disk develops injectively. It is enough to
identify the missing step in the proposed immediate extra-contact
contradiction. A global disk theorem could impose further restrictions;
none is inferred here from the unfilled cap triangle.

## 5. A literal warning: local star hypotheses do not bound its exterior

The following fixed matched sphere proves that LOCAL star hypotheses
alone cannot bound the full weighted envelope by Phi_D. Start with the
five-vertex simple sphere having ports

\[
(u,A,v,C),\qquad(A,u,C,Z),\qquad(v,C,u,Z).
\]

Stellar-subdivide the last port's triangle vCZ by a new ordinary W,
retaining its vZ pairing and pairing the other new triangles across
CW. The resulting FOUR original ports are

\[
F=(u,A,v,C),\quad E=(A,u,C,Z),\quad
G'=(v,u,W,Z),\quad G''=(C,v,Z,W).\tag{13}
\]

Their eight triangles are uAC,uvC,uAZ,ACZ,uvZ,vWZ,vCW,CZW. Each edge
is in two triangles, the sphere is simple, and the displayed paired
edges uC,AZ,vZ,CW are distinct. Deleting them leaves a simple bipartite
MAIN quadrangulation with four distinct vertices per port. The
general Morse realization therefore supplies actual sources for
this recorded incidence; no flat-plat word or knot equivalence is
asserted. Mark the ORIGINAL MAIN pair u,v.

Use F as cap, all other ports CROSS, and choose ordinary weights

\[
L_A=L_C=1,\qquad L_Z=4,\qquad L_W=W>0.
\]

The entire A-star consists of E. Its endpoint A-load is exactly

\[
\nu=\frac1\pi\left(\arctan\frac12+\arctan\frac13\right)=\frac14.\tag{14}
\]

The last equality uses the positive tangent-addition branch. In
particular the local star hypotheses and its positive loss constants
do NOT depend on W. Let X_E=Q(1,0,4)+Q(1,1,4), a fixed finite number.
The original full weighted cap-only envelope, including every target,
is

\[
\mathcal E(W)=X_E-\tfrac12\log4+Q(0,W,4)+Q(1,0,W)+Q(1,4,W)-\log W.
\]

Each of the last three triangle potentials admits its pure-W
half-load. Hence

\[
\mathcal E(W)\ge\tfrac12\log W+X_E-\tfrac12\log4\longrightarrow+\infty.\tag{15}
\]

The actual complete capacity Phi_D of this fixed finite sphere is
finite. Thus an arbitrarily large excess of this weighted envelope
over Phi_D is compatible with all LOCAL star hypotheses and a fixed
positive relative loss.

The exterior is NOT stationary in this example. It is therefore NOT
a counterexample to Delta_cap<=p C0, to the cap-only maximum inequality,
or to the volume conjecture. At W tending to infinity its original W
demand plainly fails the stationarity equation. The example only
rules out promoting a local relative estimate to an absolute theorem
without using the global demands/stationarity or a genuine positive
reference comparison. Equations (1)-(10), rather than this warning,
are the main reduced absolute problem.

## Dependencies and review status

The [whole CROSS-star spectral theorem](research_cap_cross_shared_star_spectral_gap.md)
supplies the genuine relative loss and fixed spectral neighborhoods.
The [cap-component and stellar theorem](research_cap_star_cut_and_cross_stellar_reduction.md)
supplies the forest and leaf selection, and the exact refinement used
in section 5. The [full-fiber stationary classification](research_full_fiber_sharp_stationary_classification.md)
supplies the original finite common weights and strict residual caps.
The [triangle entropy normalization](actual_triangle_entropy_algebraic_balance.md)
and [complete-capacity duality](actual_smoothed_source_capacity_blocks.md)
fix the constants and the compact concave optimization convention.
The [matched-sphere Morse construction](research_matched_sphere_morse_source.md)
supplies actual sources for (13); it does not identify them with another
filled knot. The cap flow quotient in section 2 is classical only and
does not change any quantum tensor.

Root and coherent_partner_currents independently reviewed sections 1–5
in full, analytically and against the original source scope: PASS.
They checked the complementary R(s) intervals, forest target realization,
exact dual constant, stationary attainment, relative spectral-star budget,
missing contact and oriented fan coordinates, and the literal four-port
nonstationary envelope example. These are internal reviews, not external
peer review. Preservation changes formatting and supplies durable links.

No numerical audit or scan is needed or claimed. There is no constructed
bad common-stationary maximum, coefficient lower-rate assertion, new
finite-source rewiring, or general prescribed-diagram volume theorem.
