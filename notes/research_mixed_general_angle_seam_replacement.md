# Isolated zero collars with arbitrary neighboring half-period angles

Research proof, 5 November 2026. An isolated variable near zero can now be
replaced by its geometric reference without restricting its neighbors to
small neighborhoods of special angles. The comparison includes the change
in every adjoining noncollar block. It uses the original source profiles,
real concavity, and argument bounds for the original conditional root.
No new critical-point parameter cover is needed.

## 1. Statement and the comparison to be proved

Fix a cyclic word of three- and four-crossing blocks. Let its type indicators
be \(\epsilon_j\in\{0,1\}\), its Fourier selections be
\(0\le\sigma_j\le\epsilon_j\), and its actual critical reference be
\(r=(r_j)\). Write \(\phi_{\eta\epsilon}(a,b)\) for the allocated
conditional phase, with its original logarithms, chirp and factorial
halfweights. The real part of the total reference action is
\[
 M=\Re\sum_j\phi_{\epsilon_{j-1},\epsilon_j}(r_{j-1},r_j).
 \tag{1}
\]
The established reference rectangles are
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                         \tag{2}
\]

Use the original periodic hybrid contour, with fixed
\(0<\rho\le1/1000\). Let \(S\) be a nonempty independent set of
positions: no physical edge has both endpoints in \(S\). Consider the
region
\[
 x_s\in[0,\rho]\ (s\in S),\qquad
 x_j\in[\rho,1/2]\ (j\notin S),\qquad
 x_{s-1},x_{s+1}\in[1/10,1/2]\ (s\in S).             \tag{3}
\]
The last intervals are the entire indicated intervals, not small
neighborhoods of their endpoints. Coordinates not adjacent to \(S\)
may lie below \(1/10\).

**Theorem 1.** For every fixed word and \(\rho\), the original selected
integrals over (3), summed over every permitted selection, satisfy
\[
 \left|\text{contribution of (3)}\right|
       \le C N^A e^{N(M-|S|/500)}.                  \tag{4}
\]
The constants are independent of the integer level \(N\), and both
parities are included. Shared neighbors, two-cycles and three-cycles are
allowed. A one-cycle has no nonempty independent set.

This is a theorem about a part of the original integration domain. It
does not cover adjacent collar coordinates, noncollar neighbors below
\(1/10\), or angles beyond the half-period. It does not by itself
establish the volume conjecture for a new knot family.

For the proof, replace every \(x_s\) by \(\Re r_s\) and set
\(\sigma_s=0\). Recompute all hybrid heights and denote the resulting
targets by \(z_j^\#\). This is a pointwise comparison, not a substitution
in the integral. The repaired real coordinates all belong to
\([\rho,1/2]\). The
[half-period phase theorem](research_mixed_deep_low_half_region.md)
therefore bounds their total coherent rate by \(M\).

## 2. The two incident blocks and the neighboring edge errors

Around one position \(s\in S\), write the three types as
\((\alpha,\beta,\gamma)\), the neighboring real coordinates as
\(a,c\), and \(t=\Re r_s\). Thus
\[
 a,c\in[.1,.5],\qquad
 t\in I_\beta,\qquad I_0=[.30,.39],\quad I_1=[.27,.33]. \tag{5}
\]
For a neighboring coordinate, denote its physical height by \(p\)
and its repaired height by \(h\). These symbols denote real heights,
not angles or cotangents. Replacing the collar removes one argument
from a minimum of cutoffs. Hence \(p\) and \(h\) have the same sign,
and \(|p|\le|h|\).

The selected coherent edge rate is
\[
 e_{\eta\epsilon}(z,w)=\Re\phi_{\eta\epsilon}(z,w)
       +\frac{\sigma_z}{2}\chi(z)+\frac{\sigma_w}{2}\chi(w),
 \qquad \chi(z)=\max\{\Re g(z),-2\pi\Im z\},
 \tag{6}
\]
where \(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\).
Every maximum in (6) is retained. Put
\(\theta_x=\pi(1/2-x)\), and write \(u_+=\max(u,0)\).
The [acute gradient theorem](research_mixed_acute_gradient_height_transfer.md)
gives the following upper costs for lowering the repaired pair to its
all-real value:
\[
 \begin{split}
 P_L(x,h)&=\frac\pi2 h_+-\frac{\alpha\theta_x}{2}h+\pi\sigma_L h,\\
 P_R(x,h)&=\frac\pi2(-h)_+-\frac{\gamma\theta_x}{2}h+\pi\sigma_R h.
 \end{split}                                                    \tag{7}
\]
The unselected middle height lies between \(-.03\) and \(.02\)
for type three, and between \(-.057\) and zero for type four. Its
cost is therefore at most
\[
 T_0(t)=.015\pi,\qquad T_1(t)=.057\pi(1-t).        \tag{8}
\]
Using the full height range in (8) enlarges the bound; it removes the
middle minimum of cutoffs altogether.

There can also be a change in an edge joining this neighbor to another
noncollar coordinate. Write \(d=h-p\). Its physical rate minus its
repaired rate is bounded by
\[
 \begin{split}
 Q_L(x,h,p)&=\left(\pi\sigma_L-\frac{\alpha\theta_x}{2}\right)d
                                    +\frac\pi2(-d)_+,\\
 Q_R(x,h,p)&=\left(\pi\sigma_R-\frac{\gamma\theta_x}{2}\right)d
                                    +\frac\pi2 d_+ .
 \end{split}                                                    \tag{9}
\]
The other endpoint may already be complex. To prove (9), first hold
that endpoint fixed. Convexity in the changed height gives
\[
 e(p)-e(h)\le(1-\tau)\{e(0)-e(h)\},\qquad p=\tau h,\quad0\le\tau\le1.
 \tag{10}
\]
At height zero the branch \(-2\pi\Im z\) attains the own selected
maximum. Its supporting line bounds the braces in (10) by
\((\Im\phi_{a\text{ or }b}+\pi\sigma)h\).
The own-real, other-complex argument bounds in the acute theorem then
give (9), with the sign of \(d\) retained. At \(h=0\) the assertion
is immediate. This reasoning uses convexity of the full selected rate;
it is not a lower estimate for the modulus of a finite kernel.

Every fee in (9) is nonnegative on the allowed height bands. For
unselected type three, the left fee vanishes when \(h\ge0\), and
the right fee vanishes when \(h\le0\). Unselected type-four heights
are nonpositive; selected heights are nonnegative. Substituting these
signs into (9) proves the remaining assertions. Consequently an absent
noncollar edge causes no problem: its reserved fee may be discarded.

## 3. A finite expression containing every permitted height

Let
\[
 L_b(x)=\min\{1,\max\{0,(x-.1)/(b-.1)\}\},\qquad
 R(x)=\begin{cases}1&x\le.45,\\400(.5-x)^2&x\ge.45.\end{cases}
 \tag{11}
\]
The row uses \(b=.22\) when unselected and \(b=.12\) when selected.
If its height coefficient is \(c_0\), every actual pair \((p,h)\)
lies in the triangle with vertices
\[
              (0,0),\quad(0,H),\quad(H,H),
                    \qquad H=c_0 R(x)L_b(x).                  \tag{12}
\]
This contains all inner-neighbor cutoffs and all collar attenuations,
even when one noncollar coordinate is adjacent to two collar coordinates.
An unselected type-three row uses the two possibilities
\(c_0=-.03,.02\); an unselected type-four row uses \(c_0=-.057\);
a selected row uses \(c_0=.014\). The zero vertex and convexity
include every intervening reference height.

Use the exact rational source profiles
\(A_{\beta\alpha}(p)\) and \(B_\gamma(p)\) from the
[height-dependent source theorem](research_mixed_height_resolved_seam_sources.md).
On each fixed selection band these profiles are convex piecewise affine
functions. The full expression consisting of the source profile, (7),
and (9) is convex in \((p,h)\). It is therefore enough to take its
maximum at the vertices (12). Define
\[
 \begin{split}
 E_L(x)&=\max_{(p,h)}
  \{A_{\beta\alpha}(p)-A_{\beta\alpha}(0)+P_L(x,h)+Q_L(x,h,p)\},\\
 E_R(x)&=\max_{(p,h)}
  \{B_\gamma(p)-B_\gamma(0)+P_R(x,h)+Q_R(x,h,p)\},
 \end{split}                                                    \tag{13}
\]
where the maxima are over the listed vertices and height coefficients.
There is no optimization over unknown boundary data in (13).

The source collar cost is included in
\[
 U_{\alpha\beta\gamma}
 =A_{\beta\alpha}(0)+B_\gamma(0)+2\Delta_{.001}+\beta\nu_{.001},
 \quad \nu_\rho=-J(\rho),\quad\Delta_\rho=\rho\log2-J(\rho),
 \quad J(x)=\int_0^x\log(2\sin\pi u)\,du.                      \tag{14}
\]
This bounds every \(\rho\le.001\). The earlier
[real connector theorem](research_mixed_low_endpoint_connector_lower.md)
certifies all 64 corner values of
\[
 f_{\alpha\beta}(a,t)+f_{\beta\gamma}(t,c)-U_{\alpha\beta\gamma},
                         \qquad f=\Re\phi\text{ on real arguments}.
 \tag{15}
\]
Joint real concavity bounds (15) below by the trilinear interpolation
of any certified lower corner values. Denote that interpolation by
\(\mathcal I_{\alpha\beta\gamma}(a,t,c)\).

**Lemma 2.** On the whole box (5), for every permitted endpoint selection,
\[
 -\mathcal I_{\alpha\beta\gamma}(a,t,c)
       +E_L(a)+E_R(c)+T_\beta(t)\le-3/1000.          \tag{16}
\]
Thus the complete raw collar-pair ceiling, plus both neighboring-edge
fees, lies at least \(3/1000\) below the repaired coherent pair.

## 4. Exact verification of the elementary inequality

Here are the reductions underlying the finite verification of (16).
They are part of the proof, not sampling assumptions.

First, the expression is affine in \(t\), since (13) is independent
of \(t\), (8) is affine, and the interpolation in (15) is affine in
each variable separately. It suffices to use the two endpoints of
\(I_\beta\). There are 36 choices of types, permitted selections,
and this middle endpoint.

Next divide each outer interval at
\[
                     .1,\quad .12,\quad .22,\quad .45,\quad .5.
 \tag{17}
\]
On each piece, \(R L_b\) is a polynomial of degree at most two.
Every convex source profile is the maximum of the affine extensions
of its segments on the relevant fixed selection band. Substituting
these extensions into (13) represents each side as the maximum of
finitely many polynomials of degree at most three. This avoids any
division at irrational preimages of source knots.

All coefficients may be bounded rationally. Each corner value used in
\(\mathcal I\) is rounded downward and checked against its original
outward interval. Each cost multiplying \(\pi\) in (7)--(9), after
combination at a permitted height vertex, is nonnegative. Replacing
\(\pi\) by the verified upper bound \(355/113\) therefore enlarges
the entire cost. The source profiles already have rational coefficients.

For a rectangle, put every side polynomial into its degree-three
Bernstein form. If their coefficients are \(l_{ik}\) and \(r_{jl}\),
and the degree-\((3,3)\) coefficients of the interpolated margin are
\(m_{kl}\), then every polynomial branch has coefficients at most
\[
                   \max_i l_{ik}+\max_j r_{jl}+T_\beta-m_{kl}.
 \tag{18}
\]
The Bernstein basis is nonnegative and sums to one, so an upper bound
\(-3/1000\) for every coefficient proves (16) throughout the rectangle.
All \(36\cdot16=576\) initial rectangles pass this test without
subdivision. The largest certified coefficient is less than
\(-.00331311\), leaving strict slack above the claimed loss \(.003\).
The saved certificate records every rectangle. The replay checks its
coverage and recomputes (18) with exact rational arithmetic; its coverage
validator also supports complete quadtree subdivisions.

No new critical roots, logarithmic lifts, or dilogarithm values enter
this step. The only phase values are the earlier original-log corner
certificates. The separate acute-gradient theorem supplies the analytic
inequalities needed to reach this elementary expression.

## 5. Assembly on the original cyclic product

The two incident edges of distinct positions in \(S\) are disjoint,
because \(S\) is independent. Allocate the original Fourier
halfweights to these edges once. The original raw-pair bounds give (14)
with the actual endpoint height profiles; Lemma 2 replaces each pair
by its repaired coherent pair, subtracting \(3/1000\) and the two
nonnegative fees (9).

Only noncollar vertices adjacent to \(S\) can change height. A vertex
with one collar neighbor has one remaining noncollar-edge incidence;
its corresponding fee is included in that collar's comparison. A vertex
with two collar neighbors has no remaining noncollar edge, and both
reserved fees are harmless. If a noncollar edge has both endpoints
changed, telescope its rate difference by changing one endpoint and then
the other. Equation (9) is uniform in the other complex target, so its
two endpoint fees bound this difference. This uses the edge once.

If the other noncollar endpoint is below \(.1\), the relevant cutoff
is zero both before and after the replacement, so there is no change
to bound. All nonzero changes take place in the already admitted typed
complex polygons. The original finite-source upper bounds continue to
apply: real deep-low edges use the real half-endpoint packet, and
nonlow edges use the established complex products.

After summing, the neighboring-edge differences consume at most their
reserved fees. Thus, before the arbitrarily small finite-source
tolerances, the original product rate is at most
\[
             \sum_j e_j(z_{j-1}^\#,z_j^\#)-3|S|/1000
                         \le M-3|S|/1000.                    \tag{19}
\]
Choose the sum of all finite-source tolerances at most \(1/1000\).
For \(|S|\ge1\), the remaining loss is at least \(|S|/500\).
The fixed contour Jacobians, polynomial factors and finitely many
selections are absorbed into \(CN^A\). Integration proves (4).
For a two-cycle, the two physical edges remain distinct and its one
noncollar vertex has no remaining edge. For a three-cycle, the single
remaining edge receives precisely the two telescoped corrections.
These cases require no asymptotic change of normalization.

## Reproduction

Run the exact certificate with

```sh
python3 experiments/check_mixed_general_angle_seam_replacement.py
```

To replay the saved partition without changing its record, use

```sh
python3 experiments/check_mixed_general_angle_seam_replacement.py \
  --input repro/results/research-mixed-general-angle-seam-replacement.json \
  --output /tmp/mixed-general-angle-seam-replacement-review.json
```

The preliminary floating grid is archived separately under
`repro/diagnostics/2026-11-05-seam-elementary-envelope/`; it is not used
as a certificate or as the justification for (16).
