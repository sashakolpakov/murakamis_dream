# A frozen center with a right vertex at distance two

Research certificate formulation, 5 November 2026. This note treats the
non-early half of a moving minimum whose opposite neighbor is early.
The complete sign assertion requires a passed record for all 240 domains
below. An incomplete bounded construction proves no full-family sign.
The already verified, unfrozen 400-domain theorem remains unchanged.

## 1. Actual heights and the compensated half

Use the original allocated phase, logarithmic lift and derivative
conventions of the [distance-two theorem](research_mixed_distance_two_right_halves.md).
Let the moving center have real coordinate \(t\in[.12,.22]\),
its non-early neighbor real coordinate \(y\in[t,.5]\), and the
next vertex on that side be right, already fixed at \(.5\). Its
opposite neighbor belongs to \([.1,.12]\). Write
\[
 \rho(t)=(t-.1)/.12,\qquad
 R(y)=\begin{cases}1,&y\le.45,\\400(.5-y)^2,&y\ge.45.\end{cases}
 \tag{1}
\]
The center's actual height \(h\) is fixed during this minimum
movement. The [one-early argument](research_mixed_one_early_neighbor_transport.md)
gives the containing intervals
\[
 J_{U_3}=[-1/200,1/300],\qquad
 J_{U_4}=[-19/2000,0],\qquad J_{S_4}=[0,7/500].
 \tag{2}
\]
Its real velocity is one and its height velocity is zero. Releasing
\(h\) independently of the early coordinate is legitimate for this
half; the old early-half inequality keeps any correlation it needs.

Put \(H=7/500\). The targets and neighbor height velocity are
\[
 z_c=t+ih,\qquad
 z_n=\begin{cases}y+ic_nR(y)\rho(t),&n\text{ unselected},\\
                  y+iHR(y),&n\text{ selected},\end{cases}
 \qquad b_n=\begin{cases}c_nR(y)/.12,&n\text{ unselected},\\
                         0,&n\text{ selected}.\end{cases}
 \tag{3}
\]
For an unselected neighbor \(\xi\in\{0,1\}\); for a selected
neighbor \(\xi=0\). The switch describes the conservative
minimum-height derivative, not the neighbor's actual height.

The neighbor coefficient uses the same actual cyclic geometric
conditioning as the 400-domain theorem: the middle interval of its
known type triple, the first-coordinate interval of the following
triple (hull over an unknown last type), the global typed intervals,
\([-.056,-.048]\) when its own and next types are four, and upper
bound \(-.053\) when its preceding type is also four. The checker
reconstructs these intersections from the original integer table.
No center reference coefficient is needed in (2).

Let \(G_c,G_n\) be the center and neighbor partials of their
coherent edge, in the actual cyclic order. With the original raw
optimizer \(u_*\), put
\[
 K=g'(z_n+u_*)-(1+\alpha_n/2)g'(z_n)+2\pi i d u_*,\qquad
 O_\xi=\Re\{G_c+i\xi b_n(G_n+K)\}.
 \tag{4}
\]
For the examined right half \(c\to n\to R\), use
\(\phi_{\alpha_c\alpha_n}(z_c,z_n)\), \(d=1\), and raw
own type \(\epsilon=\alpha_R\). For the examined left half
\(R\to n\to c\), use \(\phi_{\alpha_n\alpha_c}(z_n,z_c)\),
\(d=0\), and \(\epsilon=\alpha_n\). The center partial is
respectively the first and second partial; the neighbor partial is
the other one.

The required compensation is precisely the one paired with the
old early half. Define
\[
 a_c(h)=
 \begin{cases}
 0,&\alpha_c=0,\\
 -1/5,&\alpha_c=1\text{ and the examined side is right},\\
 4|h|-53/1000,&\alpha_c=1\text{ and the examined side is left}.
 \end{cases}
 \qquad \mathcal D=O_\xi+a_c(h).
 \tag{5}
\]
These adjustments apply regardless of selection. On the two
closed type-four bands, \(|h|=-h\) for \(U_4\) and \(|h|=h\)
for \(S_4\). Their common value at zero agrees. In particular the
left compensation has derivative \(-4\) or \(+4\) in the actual
height parameter. The old imaginary gauge has zero real contribution
because the center height velocity vanishes. The unfrozen selected
\(\pm.1\) adjustment is not substituted for (5).

**Certificate implication.** A complete passed cover proves
\(\mathcal D>0\) throughout this local family. Adding the unchanged
early-half inequality from the one-early theorem cancels (5), and
proves the conservative local derivative is positive in this
configuration. This does not assert positivity of every mixed local
pattern or a full cyclic asymptotic.

## 2. Source and true selected derivatives

All targets in (2)--(3) lie in the completed early cap, plateau and
right-triangle source union: at \(t=.12\), the type-three cap
already contains \([- .005,1/300]\), the unselected type-four
cap contains \([-.0095,0]\), and the enlarged selected cap
contains \([0,H]\); containment persists as \(t\) increases.
The original holomorphic packets and zero lift are those of the
[cap](research_mixed_early_selected_source_cap.md),
[interface](research_mixed_left_right_interface_source.md) and
[right-square](research_mixed_unselected_right_taper_products.md)
theorems. Derivatives therefore refer to those original phases.

For the selected center the true correction is
\(\max\{\Re g(t+ih),-2\pi h\}\). The strict strip inequality
\(-\Re g(t+ih)-2\pi h>3/40\), for
\(t\in[.12,.22]\), \(h\in[0,H]\), is the one proved in
[the early selected transport argument](research_mixed_early_selected_transport.md).
The correction equals \(-2\pi h\), which is constant during
this movement. A selected neighbor has zero height velocity and
fixed real coordinate, so either true branch has zero derivative.
An unselected neighbor retains the full factorial derivative in
(4). Thus (4) omits no moving Fourier contribution. It is a statement
about the derivative of the complete upper rate, not a lower bound
for a finite kernel.

## 3. Whole-box derivatives and saved witnesses

The row equation, its unique root in \((1/5,2/5)\), and the bound
\(T_u\le-2\pi\) are exactly those of the
[algebraic row theorem](research_mixed_algebraic_right_row.md) and
[real row derivative theorem](research_mixed_raw_row_stationarity.md).
For any rational trial \(u_0\) in that bracket,
\[
 |u_*-u_0|\le |T(u_0,z_n)|/(2\pi),\qquad
 (u_*)_p=-\Re\{M(z_n)_p\}/T_u,
 \quad M=g''(z_n+u_*)+2\pi i d.
 \tag{6}
\]
With \(K_z=g''(z_n+u_*)-(1+\alpha_n/2)g''(z_n)\), the exact
parameter derivative of (5) is
\[
\begin{split}
 \mathcal D_p=\Re\big[&H_{cc}(z_c)_p+H_{cn}(z_n)_p
       +v_p(G_n+K)\\
 &+v\{H_{nc}(z_c)_p+H_{nn}(z_n)_p
             +K_z(z_n)_p+M(u_*)_p\}\big]+(a_c)_p,
 \qquad v=i\xi b_n .
\end{split}                                                     \tag{7}
\]
Here \(H\) is the original coherent Schur Hessian. The height
parameter in (2) changes across the certificate box, so its derivative
must be included in (7), despite its zero physical height velocity.
Derivatives of \(R(y)\) occur in both the neighbor target and
\(b_n\).

The original logarithmic affine disk self-map encloses the complex
root separately on the full box and at its midpoint. Its radius
must be rational and strictly positive, at most \(1/20\). A
stored rational row trial is checked through (6), independently at
the full box and midpoint. Nonfinite Schur or row quantities force
rejection. Acceptance takes the greater of the direct interval
lower endpoint and the midpoint enclosure minus all full-box
first-derivative radii.

## 4. Complete family, accounting and verification

The four-type window contains the early position, center, neighbor
and right position in their cyclic order. Both orientations and
all permitted center/neighbor selections are retained. The exact
maps from \([0,1]^4\) are
\[
\begin{split}
 t&=.12+.10v_0,\quad h=\ell_h+(h_h-\ell_h)v_2,\quad
 c_n=\ell_n+(h_n-\ell_n)v_3,\\
 y&=t+(.45-t)v_1\quad\text{or}\quad y=.45+.05v_1.
\end{split}                                                     \tag{8}
\]
For a selected neighbor the last parameter is unused, its coefficient
is zero and its actual target height remains \(HR(y)\).
There are three center states, five combined neighbor state/switch
choices, four choices of the two outer types and two orientations.
Consequently each real piece has \(3\cdot5\cdot4\cdot2=120\)
domains, and the complete family has 240.

Every binary split retains both closed rational children. A
monotonic node may retain one endpoint only after a strict derivative
sign is proved on its entire box with that node's original root
witness. A leaf requires a strictly positive outward lower bound.
Replay reconstructs all 240 initial cubes, consumes every saved
split/monotonic/leaf node, verifies every witness and row trial, and
checks every count and dependency before and after. The already
passed 400-domain author and saved replay are also bound unchanged;
their old positive cells are not reused as acceptance of any new cell.

Construction stops after 200,000 total visits or 120 seconds and
records an incomplete result if necessary. A replay has no such
cap: every prescribed cell must be checked. No incomplete record
establishes the certificate implication.

Repeated cyclic incidences impose additional equalities inside these
independently enlarged domains. A two-cycle cannot have one early
and one distinct non-early incidence. In a three-cycle, an early
outer incidence can freeze the neighbor as well; that case is not
represented as active merely by this note. The asserted application
requires (3), and includes both conservative switches when it is
active. No assumption of distinct vertices is used to turn a missing
case into a proved one.

    python3 experiments/certify_mixed_frozen_center_distance_two_right_halves.py --precision 256
    python3 experiments/certify_mixed_frozen_center_distance_two_right_halves.py --precision 384 --input repro/results/research-mixed-frozen-center-distance-two-right-halves.json --output repro/results/research-mixed-frozen-center-distance-two-right-halves-replay.json
