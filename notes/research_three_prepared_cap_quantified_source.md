# The original prepared cap on a specified Fourier disk

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This quantifies the output domain of the full first attachment. It uses
the original finite cap and restores the deleted corner after contraction.
The resulting source packet is uniform on the genuine complex disk of
radius \(1/200\). A whole outgoing-period estimate adequate for arbitrary
further attachment remains a separate requirement.

## 1. Statement and certified critical branch

Put
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\quad Y_h=\Im x_h,\quad
 {\cal D}=\{y:|y-x_h|\le1/200\},\quad
 {\cal Q}=\{y:|\Re(y-x_h)|,|\Im(y-x_h)|\le1/200\}.
 \tag{1}
\]
Use the original matrices \(A=JM^3\), the original Newton evaluation
vector \(v(w)\), and the full half-band cardinal vector \(h(y)\).
The prepared source is
\[
                 {\cal B}_N(y,u)=v(-2\cos u)^TA^2h(y).
 \tag{2}
\]
The phase \(\Theta_{\rm eff}(y,u)\) and amplitude \({\cal A}(y,u)\)
are the actual branches of
[the full first-attachment theorem](research_three_cap_central_source.md),
continued by the original stationary equations.

**Theorem 1.** On a neighborhood of \({\cal D}\times\{0\}\),
the original finite source (2) satisfies uniformly
\[
 {\cal B}_N(y,u)=C_{N,3}\kappa N^{-1}{\cal A}(y,u)
       e^{N\Theta_{\rm eff}(y,u)}(1+O(N^{-1})),
                         \qquad {\cal A}(y,u)\ne0.
 \tag{3}
\]
This includes both level parities and all fixed ordinary outside
derivatives in \(w=-2\cos u\). The normalized remainder is holomorphic.
The conclusion concerns the true disk \({\cal D}\), not the entire
coordinate square \({\cal Q}\).

We use the actual critical branch certified in
[the analytic phase theorem](research_three_phase_graph_transform.md).
Its 4,096 output cells cover \({\cal Q}\) exactly and retain the original
lifted phase. Their outward enclosures imply the following deliberately
rounded bounds, in the order wire, cap angle, first index, second index:
\[
 \begin{array}{c|c|c}
 &\Re&\Im\\ \hline
 x_c&(.176,.179)&(.09,.12)\\
 \tau_c&(3/2,31/20)&(-1,-97/100)\\
 s_c&(.31,.39)&(-1/125,1/125)\\
 t_c&(.31,.39)&(-17/1000,3/250).
 \end{array}
 \tag{4}
\]
The tighter cells give \(\Re\tau_c<1.538<\pi/2\) and
\(-\Im\tau_c<.983<1.07\). Thus the original complete-edge local
packet applies uniformly near these cap critical points. Its
factorial arguments and all retained index arguments remain regular.

The same phase certificate proves \(|\Theta_{\rm eff,yy}|<14\) on
\({\cal Q}\). At the center,
\(\Re\Theta_{\rm eff}>1.9113\) and
\(|\Theta_{\rm eff,y}|<.08\). Hence on the true disk,
\[
 \Re\Theta_{\rm eff}(y,0)>
 1.9113-.08(.005)-7(.005)^2
                         =1.910725>1.9107.
 \tag{5}
\]
Only (5) uses the restriction from the square to the disk.

## 2. The exterior, joins and real finite remainders

For this proof delete the larger corner
\(L_{40}=\lfloor N/40\rfloor\), writing
\(\widetilde A_{40}=A-E_{40}\).
The exact retained source is
\[
 {\cal C}^{(40)}_N(y,u)
 =N\int_{-1/8+iY_h}^{7/8+iY_h}
       W_N(x,u)\widetilde V_N^{(40)}(x,y)\,dx
 =v(-2\cos u)^TA\widetilde A_{40}h(y).
 \tag{6}
\]
This changes no summand in the central index square.
Restore the removed corner only after estimating this full integral.

The original exterior-cap argument permits the sharper bound
\[
 |W_N(\xi+iY_h,0)|\le\operatorname{poly}(N)e^{1.264N},
 \quad
 \xi\in[-1/8,.14]\cup[.20,7/8].
 \tag{7}
\]
It uses the same exact reflected trace and all physical omissions as
[the established exterior proof](research_three_cap_wire_complement.md).
The separate
[sharper author certificate](../experiments/certify_three_prepared_cap_exterior.py)
proves all 26 original domains at threshold \(158/125\);
the [independent reflection replay](../experiments/replay_three_prepared_cap_exterior.py)
checks their complete rational cover at higher precision.
No original cap term or first normal has been dropped.

The [symmetric-height retained bound](research_three_vertex_symmetric_height_bound.md)
is termwise on the whole real index set. It gives rate below \(.6466\)
when the input wire stays at \(Y_h\) and \(|\Im(y-x_h)|\le.005\),
uniformly for every real outgoing phase. Thus the exterior part in
(6) has rate below \(1.9106\), strictly below (5).

For the central input interval use fixed rational initial heights
\[
 h_0=.10135869,\quad H_0=.97895510,\quad
 \sigma_0=.00300831,\quad \theta_0=-.00629803 .
 \tag{8}
\]
The wire moves from height \(Y_h\) to \(h_0\) at real endpoints
\(.14,.20\). The actual cap bounds \(1.261,1.2638\) on these joins
are Proposition 2 of the exterior proof. The
[conditional retained join bound](research_three_prepared_cap_join_vertex.md)
is below \(.6469\), uniformly on \({\cal Q}\). The two join products
therefore have rate below \(1.9107\).

On the central wire, the original cap proof is uniform on the narrow
wire/trace-height intervals containing (8). Its whole cap and positive
bottom each have rate at most \(1.265\). The
[real-index complementary theorem](research_three_prepared_cap_real_complement.md)
bounds the L40 sum outside \(B^2\), \(B=[1/4,9/20]\), by \(.6455\).
Discard it before any index deformation, at product rate below \(1.9105\).

Next retain only the positive cap bottom \(0\le\Re\tau\le9/5\)
at depth \(H_0\). Every other original angular integral, folded
vertical and physical tail has rate below \(1.26\), and the radical
has a still smaller rate. Proposition 2 of the symmetric-height note
bounds every retained real-index subset by \(.6485\) at the two
heights now present. Their product is below \(1.9085\).
This order keeps the actual finite source: no bound on a sum is
reused for a subset after its cancellations have been removed.

## 3. Anisotropic index contours and supporting planes

The original index rectangles used for the constant-cotangent extraction
are now
\[
 {\cal R}_s=B+i[-1/125,1/125],\qquad
 {\cal R}_t=B+i[-17/1000,3/250].
 \tag{9}
\]
They contain the whole certified critical-index range (4), with strict
margin. Put their real sides at half-grid cuts within \(O(N^{-1})\)
of the endpoints of \(B\).

Keep the unsummed original phase
\[
 {\cal G}(x,\tau,s,t;y)=
 b(x,\tau)+\Psi(\tau)+\frac{3i\tau^2}{4\pi}-i\tau
                      +F(s,t;x,y)-\pi i(x+y).
 \tag{10}
\]
Its real-coordinate box is
\[
 {\cal R}=[.14,.20]\times[0,1.8]\times B\times B,\qquad
 \Re y\in[97/600,103/600].
 \tag{11}
\]
The [joint Hessian theorem](research_three_vertex_joint_concavity.md)
applies throughout all heights under consideration. In particular,
\[
 -\Re d^2{\cal G}\succeq
 (3/4+\pi/5)\,dx^2+\frac1{20\pi}\,d\tau^2
                  +\frac34(ds^2+dt^2)
 \tag{12}
\]
on horizontal variations of the four input variables.
The full five-variable real Hessian, including \(\Re y\), is also
strictly negative. This follows directly by adding the cap form to
the positive incidence decomposition of the retained phase.
The assertions hold on the closed real boxes by continuity.

Holomorphy consequently makes the phase convex in any joint imaginary
direction while the real coordinates are fixed. This fact supplies
a finite global certificate without a sampled maximization.
For a concave real function \(f\) on a real rectangle, any exact
point \(z_0\) in it gives the supporting bound
\[
 f(z)\le f(z_0)+\nabla f(z_0)\cdot(z-z_0)
 \le f(z_0)+
 \sum_j\max\{\partial_j f(z_0)(a_j-z_{0j}),
             \partial_j f(z_0)(b_j-z_{0j})\}.
 \tag{13}
\]
All terms on the final right side are evaluated outward.
Numerical optimization is used only to propose the rational \(z_0\);
it is not an acceptance test.

At input wire/trace heights \(h_0,-H_0\), the certificate proves:

* If \(s\) or \(t\) has real part at an end of \(B\), then
  \(\Re{\cal G}<1.9107\) throughout the other real coordinates
  and all imaginary heights in (9), for every \(y\in{\cal Q}\).
* On the four products of horizontal sides of (9),
  \(\Re{\cal G}<1.95\) throughout the real box.

For the first assertion, convexity in
\((\Im s,\Im t,\Im y)\) reduces to its eight corners.
There are four possible real index faces, hence 32 supporting
planes. Each includes the full range of the other real index;
two-vertical-side products are therefore retained as well.
The second assertion has eight supporting planes, including the
two output heights. The certified worst side bound is less than
\(1.908\); the rounded \(1.9107\) threshold leaves a fixed margin.

The exact cotangent formulas recover the original central finite sum.
Vertical half-grid cotangents are bounded. Every nonconstant horizontal
factor costs at least
\[
 2\pi\min(1/125,17/1000,3/250)=2\pi/125
 \tag{14}
\]
in exponential rate. Thus all alias products have rate below
\(1.95-2\pi/125<1.9107\). The four constant products combine with
the exact positive coefficient \(N^2\). Their already bounded
vertical currents permit moving both index heights to
\(\sigma_0,\theta_0\). No pole, corner product or reflection term
is discarded.

## 4. Translating the entire principal cycle

The remaining principal four-dimensional rectangle has initial
imaginary coordinates
\[
                (h_0,-H_0,\sigma_0,\theta_0).
 \tag{15}
\]
For each fixed \(y\in{\cal D}\), translate them simultaneously and
linearly to the four actual critical heights from the phase certificate.
All intermediate coordinates lie inside the joint concavity chamber.
The homotopy is a compact prism. Its eight real faces retain every
connecting current in the holomorphic Stokes formula; its Jacobians
are uniformly bounded.

At the initial heights, every real face of \({\cal R}\) has
\(\Re{\cal G}<1.9107\), uniformly on \({\cal Q}\). This is the
remaining set of sixteen supporting planes: eight input faces and
two output heights. Their largest certified upper bound is below
\(1.909\). They use (13) in every nonfixed real coordinate, including
the outgoing real phase.

At the critical heights, the four input first derivatives vanish.
Integrating (12) from the critical point therefore bounds the whole
rectangle by its actual critical value. The coarse coordinate ranges
in (4) give distances greater than \(.021\) from the wire faces,
\(.06\) from the index faces, and \(1/4\) from the nearer trace face.
Consequently every real face has a uniform gap greater than \(1/4000\).
For example the three lower bounds are
\[
 \frac{27}{40}(.021)^2>\frac1{4000},\qquad
 \frac38(.06)^2>\frac1{4000},\qquad
 \frac7{880}(1/4)^2>\frac1{4000}.
 \tag{16}
\]
Here \(\pi>3\) and \(\pi<22/7\) were used in (12).
The independent current replayer checks these coordinate conditions
against every one of the 4,096 saved critical enclosures, as well as
their exact output-grid coverage.

For each fixed real face point, \(\Re{\cal G}\) is convex along
the simultaneous imaginary-height translation. Its maximum is
therefore at one of these two endpoint height planes. By (5),
\[
 \max_{\text{every homotopy face}}\Re{\cal G}
       <\Re\Theta_{\rm eff}(y,0)-\frac1{50000},
                         \qquad y\in{\cal D}.
 \tag{17}
\]
Thus Stokes moves the whole principal cycle to the actual critical
heights without an uncontrolled interpolation region. Its orientation
and leading coefficient remain unchanged.

The factorial and index symbols are uniform on this chamber.
For the full central trace range one uses only the actual low
complete-kernel polynomial upper bound with exponent \(\Re\Psi\).
Its nonzero packet is used solely near the cap critical angle,
where the certified compact ranges are strictly inside its proved
domain. The exponentially small nonconstant trace denominators
remain harmless throughout the height translation.

On the final height plane, (12) gives a strict gap outside a fixed
critical neighborhood. The holomorphic Gaussian theorem there
supplies the unique nonzero local coefficient. The original measure,
trace scalar and the \(+N^2\) index residue factor give \(N^{-1}\),
exactly as in the previously proved first attachment.

This coefficient can be written as the analytic continuation of
the old product expression for \({\cal A}\). Equivalently it is the
nonzero four-variable Gaussian coefficient of (10). The latter
description is used to prove the source assertion on this disk:
no separate cap or retained packet is assumed at every moving
intermediate wire. The two coefficient formulas agree near \(x_h\)
and hence as holomorphic functions on the connected critical branch.

All finite discarded regions have now been controlled: exterior
wire, wire joins, real index complement, original angular/physical/
radical remainders, index sides, cotangent aliases, homotopy faces,
and the final principal complement. Each has a uniform strict gap
on the true disk. This proves (3) for the exact retained source (6).

## 5. Original corner, normals and reproduction

The [L40 Fourier corner-transfer theorem](research_three_chain_fourier_corner_transfer.md#4-a-larger-deleted-corner-for-a-larger-source-domain)
restores the original source (2). Its actual contracted error has
rate below \(1.715\) on the base Fourier-height line. The same theorem
adds at most \(\pi|\Im(y-x_h)|\), so its rate on the outgoing square
is below \(1.715+\pi/200<1.731\), with the original ordinary outside
derivatives. A sufficiently small complex outside neighborhood keeps
it below \(7/4\). This is far below (5).
The transfer therefore preserves the same nonzero coefficient.

Every complement estimate is strict on a compact parameter set.
The actual critical branch is holomorphic and remains in the open
factorial chart. Thus a sufficiently small ordinary outside-color
neighborhood and an open neighborhood of the closed disk preserve
all estimates. Evenness in the outside angle descends the analytic
remainder to the color \(w=-2\cos u\); Cauchy estimates retain each
fixed ordinary derivative without division by \(\sin u\).
This completes Theorem 1. \(\square\)

The [56-plane author](../experiments/certify_three_prepared_central_currents.py)
and [record](../repro/results/research-three-prepared-central-currents.json)
store every exact domain, rational supporting point, outward bound
and dependency hash. Its
[independent replayer](../experiments/replay_three_prepared_central_currents.py)
uses the negative-frequency retained primitive, a reflected cap
primitive, and real logarithmic gradients, with no optimizer.
It verifies all 56 domains and all 4,096 critical-coordinate cells.
The [replay record](../repro/results/research-three-prepared-central-currents-replay.json)
retains the resulting provenance.

The sharper exterior [author record](../repro/results/research-three-prepared-cap-exterior.json)
and [independent replay](../repro/results/research-three-prepared-cap-exterior-replay.json)
retain all 26 exact domains. The conditional join and real-index
complement have their separate source proofs and independent covers
linked above.

The coordinate square is used to over-cover errors and to certify the
analytic critical branch. The lower action comparison is asserted
only on the true complex disk. Theorem 1 supplies a quantified
original prepared input for a further attachment. It does not by
itself identify or bound the complementary outgoing period in that
next attachment.
