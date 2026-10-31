# A complete geometric double of a one-cap stationary exterior

31 October 2026. **analytical research theorem.**
Unpublished. This concerns ONE residual cap
and complete CROSS rows at every other original port. The original MAIN
mark, face targets and matching are retained until the explicitly defined
doubling construction. No equality of the old and doubled quantum sources
or links, and no universal absolute cap-volume comparison, is asserted.

## 1. The actual disk and its double

Let T be the original simple matched triangulated sphere, with protected
MAIN edge uv and cap

\[
F=(u,A,v,C),\qquad (u,A,C),\ (u,v,C),\qquad
\text{matching edge }uC.
\]

Suppose first that a strict cap-only stationary datum exists: its cap
loads are (q_A,q_C)=(1-nu,nu), 0<nu<1/2, all ordinary incidences are
positive, the remaining ports are CROSS, and their common finite weights
satisfy L_A=L_C. The result in
[the cap-cut theorem](research_cap_star_cut_and_cross_stellar_reduction.md), section 1,
then proves that the opposite edge Av is absent. Delete the two triangles
of F and their shared edge uC. The remaining triangulated closed disk D
has boundary, in cyclic order,

\[
u,A,C,v.\tag{1}
\]

It has NEITHER boundary diagonal: Av was absent and uC has been removed.
All four boundary edges are MAIN. Therefore every remaining original
triangle pair lies wholly in D. Removing F has not cut any other port.

Take two labeled copies D_1,D_2, and identify their boundaries by

\[
u_1=v_2,\quad A_1=C_2,\quad C_1=A_2,\quad v_1=u_2.\tag{2}
\]

This reverses the boundary cyclic order, so the result T^dbl is a
triangulated sphere. It is SIMPLE. Indeed each copy embeds injectively;
an edge from one copy could duplicate an edge from the other only if
both endpoints were boundary vertices. In the disk all such edges are
the four boundary edges, because both diagonals are absent. Those four
edges are precisely the edges identified in the gluing. There is also
no triangle with all three vertices on the boundary: such a triangle
would contain a boundary diagonal. Thus the gluing creates neither a
duplicate triangle nor any repeated nonboundary edge.

The inherited triangle pairing is an actual matching: every port lies
in one copy and its four vertices remain distinct. The four glued edges
remain MAIN. In particular T^dbl has a simple MAIN quadrangulation and
admits the complete packing/angle-capacity theorem, with mark
uv. If T has R ports, T^dbl has 2(R-1) ports. This is a new matched
sphere, not a re-presentation of the old filled knot.

The same construction is defined without a stationary assumption for
ANY disk of this form with neither boundary diagonal. The stationary
assumption above is one exact original-source reason that Av is absent.

## 2. Exact capacity and the genuine complete optimizer

Let R(s) be the original residual capacity, as in
[the original constrained-capacity theorem](research_cap_constrained_capacity_budget.md), section 1: interior
ordinary targets are one, the boundary targets are A:s, C:1-s and
u:v:0. No targets are changed in this definition.

At the stationary datum the remaining CROSS allocations attain their
triangle Legendre optima at the original finite weights. Duplicate
these allocations into D_1 and D_2 using (2), and duplicate the weights.
They agree at the glued vertices because L_A=L_C and L_u=L_v=0.
Every interior demand is still one. At each of A,C the two boundary
contributions add to nu+(1-nu)=1. The protected demands stay zero.
Thus the duplicated flow is feasible for the COMPLETE problem on the
simple sphere T^dbl and attains its global Legendre upper bound.
Consequently

\[
\Phi(T^{\mathrm{dbl}})=2R(\nu)=2M_{\mathrm{cap}}.\tag{3}
\]

Here the last equality is the exact stationary dual-attainment theorem
for the original one-cap residual problem; it is not an asymptotic
coefficient or a source-limit assertion. The complete optimizer on the
double is positive at every ordinary incidence and unique. Its actual
circle packing therefore develops each copy of D injectively. This
supplies an embedded exterior in this construction; it is not an
assumption about an arbitrary signed Green development.

There is also a converse characterization of the relaxed residual
maximum. The double has an involution exchanging its two copies and
interchanging u with v and A with C. Uniqueness of the complete optimizer
and of its positive weights up to common scale makes the optimizer
invariant under this involution. The two A/C weights are equal. To see
that no scale is hidden, normalize the marked line separation; the
involution preserves that normalization, or apply it twice to the
positive proportionality factor to obtain factor one.

Restrict this complete optimizer to D_1. All its interior targets are
one. The boundary loads have the form s_*,1-s_*: the other copy exchanges
them and the doubled targets are one. The common equality L_A=L_C
means that its dual affine upper bound is independent of s. Hence

\[
R(s_*)=\max_{0\le s\le1}R(s)=\frac{\Phi(T^{\mathrm{dbl}})}2.\tag{4}
\]

Strict concavity in the actual triangle loads makes this residual
maximizer unique. For example, if two distinct residual load vectors
attained the same maximum, their midpoint would give a strict gain in
at least one nonconstant triangle row. The usual protected monomial
rows are fixed and cause no exception. Thus a strict original cap-only
stationary point, when it exists, is precisely this single residual
optimizer with s_*<1/2. If s_*>1/2, concavity instead places the maximum
over the original cap interval [0,1/2] at its endpoint; s_*=1/2 is the
terminal case, not a strict cap. Here 1/2 is indeed feasible. Completing
D by either missing diagonal gives a simple matched sphere with the same
mark. The original uC completion supplies a strictly feasible residual
load s>1/2, while the Av completion supplies one with s<1/2. Their convex
combination supplies s=1/2. These two completions are different sources,
not an asserted isotopy or a coefficient transport.

## 3. A new geometric restriction on the original cap split

In the genuine packing of T^dbl, normalize the marked u,v circles as
parallel lines, and let their positive separation be H. The finite
circles A,C have a common radius r, are tangent to each other, and
respectively touch u and v. They do NOT touch the other line, because
Av and uC are absent from the simple contact graph. Every ordinary disk
lies in the strip between u and v. Thus

\[
H>2r.\tag{5}
\]

This strict statement is justified by the complete simple-sphere
packing, not merely by the formal four boundary contacts.

For clarity, the fan-angle calculation is orientation-independent at
the required cosine level. Put the A center at 0, the C center at 2re,
where e is a unit vector. Let n be the unit normal from A toward its
line u. The boundary fan of D_1 at A has central angle theta=2pi s_*;
its two endpoint rays are n and e. Hence n dot e=cos(theta), irrespective
of which oriented arc realizes this fan. The two line equations are

\[
u:\ n\cdot z=r,\qquad v:\ n\cdot z=2r\cos\theta-r.
\]

Their separation is therefore

\[
H=2r\bigl(1-\cos(2\pi s_*)\bigr)=4r\sin^2(\pi s_*).\tag{6}
\]

Combining (5) and (6), with the ordinary fan loads between zero and one,
gives the genuine residual-disk restriction

\[
\frac14<s_*<\frac34.\tag{7}
\]

In particular EVERY strict one-cap-only stationary datum in the
original setting satisfies

\[
\frac14<\nu<\frac12.\tag{8}
\]

The nonstationary four-port example with local A-star mean nu=1/4 in
the earlier cap-budget note is therefore not a counterexample: it did
not satisfy the common stationary demands of the entire exterior.
Neither (7) nor this proof covers a disk with another cap left inside;
the rows duplicated here are all complete CROSS rows.

## 4. The remaining absolute inequality is now geometric, but unproved

Let C0=2f(1/4) and retain the original prescribed chart D_orig. At a
strict stationary one-cap datum, the earlier exact constrained dual is

\[
M_{\mathrm{cap}}=\Phi(D_{\mathrm{orig}})+\Delta_{\mathrm{cap}}-C_0.
\]

Together with (3) this yields

\[
\Delta_{\mathrm{cap}}\le C_0
\quad\Longleftrightarrow\quad
\Phi(T^{\mathrm{dbl}})\le2\Phi(D_{\mathrm{orig}}).\tag{9}
\]

Thus the missing unsigned cap comparison is a specific complete-volume
comparison between an original capped disk and its twisted double.
The construction proves both sides are genuine complete packing
capacities. It does NOT prove the inequality in (9). The graphs and
actual matched sources differ; there is no source equality, filling
identification, or admissible right-angled contraction implicit in the
gluing.

The exact residual formulas remain

\[
\begin{aligned}
M_{\mathrm{cap}}&=\max_{0\le s\le1/2}R(s),\\
\Phi(D_{\mathrm{orig}})&=\max_{1/2\le s\le1}
   \bigl[R(s)+2f(s-\tfrac12)\bigr].
\end{aligned}\tag{10}
\]

The new geometry restricts the unique unrestricted maximizer of R to
(1/4,3/4). A concavity statement and this location alone do not bound
how much R can decrease between s_* and 1/2; a quantitative boundary
deformation or a genuine capped-disk/double volume comparison is still
required. No abstract concave function is asserted to be realizable by
an actual positive triangulated disk.

If the geometric comparison in (9) is certified for a particular
one-cap configuration, the [signed spectral-star theorem](research_cap_cross_shared_star_spectral_gap.md)
supplies the further strict loss below Phi(D_orig). More strongly,
Phi(T^dbl)<2Phi(D_orig) already gives an unsigned cap-sector gap.
These are scoped consequences for that sector, not the full non-CROSS
remainder or a general prescribed-diagram filling theorem.

## Scope and dependencies

The only external mathematical inputs used here are the already
original cap cut, compact complete triangle duality, and the
simple matched-sphere packing/capacity theorem in this project. Relevant
durable sources are:

* [cap-star cuts](research_cap_star_cut_and_cross_stellar_reduction.md), section 1;
* [original cap capacity](research_cap_constrained_capacity_budget.md), sections 1-2;
* [simple-sphere complete capacity and packing](actual_smoothed_source_capacity_blocks.md), sections 1-5;
* [matched-sphere source realization](research_matched_sphere_morse_source.md), for the distinction
  between the newly constructed matched sphere and the old source.

The statement is limited to one cap with all remaining original ports CROSS. The doubled matched sphere is not identified with the original source, and no universal volume comparison is claimed.