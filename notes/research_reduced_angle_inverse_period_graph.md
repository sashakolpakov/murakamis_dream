# The original inverse-period collar over a convex real-angle domain

Private written proof, 16 November 2026.

The compact inverse-period collar has a stronger description than its
star-shaped real-period parametrization: it is the graph of the
imaginary angles over a bounded convex domain of real angles. The
convex function defining that domain is obtained by minimizing the
original angle energy along its incidence fibers. This description
retains the original signed powers, charges and complete peripheral
branches. It also fixes the sign of a possible connector argument:
moving vertically away from this graph increases the real action.
Consequently the graph theorem does not itself complete the collar
to the original quantum integration class.

## 1. Original coordinates and the closed fiber problem

Fix a finite connected original ordered circle tree, a nonempty
selected set \(S\), and all edges incident to \(S\), counted once.
Let \(k=|S|\) and let \(m\) be the number of included edges.
Every selected vertex has positive degree. Outside angles are
complete: \(t_b=0\). Fix real powers \(n_v\) and positive real
charges \(c_v\). In an integral filling the original convention is
\(n_v=\eta_v-2p_v\); no carrier or slope is changed here.

Use the complete positive branches and write
\[
 t_v=s_v+i h_v,\qquad r_{v,e}=k_{v,e}+i g_{v,e},\qquad
 P_v(t)=\sum_{e\ni v}r_{v,e}-\frac{i n_v}{2}t_v.
 \tag{1}
\]
The affine angle coordinates consist of the selected \(s_v\) and
all endpoint incidence variables \(g_{v,e}\), with \(s_b=0\)
outside. Put
\[
 \rho_v=\sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v=-\pi c_v.
 \tag{2}
\]
The open positive polytope \(\mathcal P_c\) is defined by these
rows and the inequalities
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad
 |s_w|+2|g_{v,e}|<\pi\qquad(e=vw).
 \tag{3}
\]
Assume strict feasibility. Its compact closure is obtained by using
weak inequalities. Indeed a segment from any weak assignment to a
strict assignment is strict except at the weak endpoint. Interiors
and boundaries of \(\mathcal P_c\) are relative to the affine
space (2).

For one edge the original square coordinates are
\[
 \begin{aligned}
 A_P&=s_v/4-g_{w,e}/2,& A_Q&=s_v/4+g_{w,e}/2,\\
 y_P&=g_{v,e}/2+s_w/4,& y_Q&=g_{v,e}/2-s_w/4.
 \end{aligned}
 \tag{4}
\]
The pinned variational theorem supplies the continuous convex energy
\[
 \mathcal E=4\sum_e(E_{P,e}+E_{Q,e})
 \tag{5}
\]
on \(\overline{\mathcal P}_c\). Its Hessian is positive definite
on every nonzero affine tangent at an interior point. This follows
from the positive square Hessians and the injectivity of (4).
There is no outside imaginary-work term because the outside data
are complete. The exact edge differential is
\[
 4\,d(E_{P,e}+E_{Q,e})
 =k_{v,e}\,ds_v+k_{w,e}\,ds_w
       +h_{v,e}\,dg_{v,e}+h_{w,e}\,dg_{w,e}.
 \tag{6}
\]

Let \(\pi_s\) denote projection to the selected real angles and set
\[
 \overline D=\pi_s(\overline{\mathcal P}_c),\qquad
 e_c(s)=\min\{\mathcal E(s,g):(s,g)\in\overline{\mathcal P}_c\}.
 \tag{7}
\]
Every fiber is nonempty and compact for \(s\in\overline D\),
so the value in (7) is defined. At this stage the notation does not
assert uniqueness or interiority of a closed fiber minimizer.

The strict feasible real-angle base \(D=\pi_s(\mathcal P_c)\)
is explicitly
\[
 \boxed{\quad |s_v|<\pi,\qquad
 |n_vs_v-2\pi c_v|+
          \sum_{e=(v,w)}|s_w|<\pi d_v\quad(v\in S).\quad}
 \tag{8}
\]
Outside terms in the sum are zero; sums count incidences. This is
the fixed-real-angle form of the existing feasibility criterion.
For completeness, at fixed \(s\), each \(g_{v,e}\) independently
varies in the interval
\((-(\pi-|s_w|)/2,(\pi-|s_w|)/2)\). Their sum must equal
\((n_vs_v-2\pi c_v)/2\), giving (8). Outside incidences have
no sum constraint and can be chosen zero. Thus \(D\) is a
bounded convex open polytope, and \(\overline D\) is its closure.
The rows (2) are independent and their affine space projects
surjectively onto the selected \(s\): an arbitrary change of
\(s_v\) can be offset in one incidence at that vertex.

The function \(e_c\) is convex on \(\overline D\). Choose
minimizers in the two fibers and take their convex combination;
convexity of \(\mathcal E\) gives the convexity inequality for
(7). It is also lower semicontinuous: for any convergent sequence
of base points, a subsequence of their compact fiber minimizers
attaining the lower limit has a limiting feasible assignment.
No global strict-convexity assertion at boundary fibers is needed.

## 2. The regular fiber locus is exactly the positive period slice

Define
\[
 D_{\mathrm{reg}}=
 \{s\in D:\text{a minimizer in (7) lies in }\mathcal P_c\}.
 \tag{9}
\]

**Proposition 1.** The set \(D_{\mathrm{reg}}\) is open. Its
fiber minimizer \(z(s)=(s,g(s))\) is unique and real analytic.
Its endpoint imaginary angles match, giving a real analytic graph
\[
                         t(s)=s+i h(s).
 \tag{10}
\]
With \(u(s)=\nabla e_c(s)\), this graph satisfies the original
equations
\[
                         P(t(s))=u(s)-\pi i c.
 \tag{11}
\]
Conversely every positive solution of \(P(t)=u-\pi i c\)
occurs exactly once on (10). Thus \(\nabla e_c\) is a real
analytic diffeomorphism from \(D_{\mathrm{reg}}\) onto the
actual positive real-period image \(\Xi_c\). Neither of these
sets is assumed connected or convex.

**Proof.** An interior fiber critical point has positive Hessian
on the homogeneous fiber tangent. It is the unique global fiber
minimum, including against boundary points: its segment to any
distinct feasible point is interior before the endpoint, and has
strictly positive second derivative. The fiber stationarity equations
have invertible Hessian, so the implicit-function theorem supplies
an analytic interior critical point for all nearby \(s\). Its
uniqueness as a global minimum proves the first assertions.

Attach multipliers \(h_v\) to (2) while holding \(s\) fixed.
By (6), incidence stationarity is precisely
\[
 h_{v,e}=h_v\quad(v\in S),\qquad h_{b,e}=0\quad(b\notin S).
 \tag{12}
\]
The original square dictionary therefore reconstructs the matched
positive point (10). Along this fiber-minimum graph, (2) and (6)
give
\[
 de_c=\sum_{v\in S}\left(
            \sum_{e\ni v}k_{v,e}+\frac{n_v}{2}h_v\right)ds_v.
 \tag{13}
\]
Combining (13) with (2) gives (11).

Alternatively the ambient identity at this point is
\(d\mathcal E=u\cdot ds+\sum_v h_v\,d\rho_v\).
Consequently \(z(s)\) is the unique interior, hence global,
minimum of \(\mathcal E-u(s)\cdot s\) on
\(\overline{\mathcal P}_c\). This is the original tilted
problem defining \(\Xi_c\). Conversely its interior minimizer
minimizes its fixed-\(s\) fiber and satisfies (12), so it occurs
on (10). Uniqueness of the tilted minimum gives injectivity.
The period theorem supplies the analytic inverse \(u\mapsto t(u)\);
its real part is the inverse of \(\nabla e_c\). \(\square\)

There is also a direct differential formula. Write the complex
symmetric original Jacobian as
\[
                         J=\frac{\partial P}{\partial t}=A+iB,
                     \qquad A=A^{\mathsf T}>0,\qquad B=B^{\mathsf T}.
 \tag{14}
\]
Differentiating (11) in real \(s\) gives
\[
 \boxed{\quad
 h_s=-A^{-1}B,\qquad
 \nabla^2e_c=A+B A^{-1}B
                      =\bigl(\Re J^{-1}\bigr)^{-1}>0.
 \quad}
 \tag{15}
\]
Indeed the imaginary part of \((A+iB)(I+i h_s)=u_s\)
is \(B+A h_s=0\), and the real part gives the second formula.
The matrix \(h_s\) need not be symmetric; the graph assertion
does not identify \(h\) itself as the gradient of a function of
\(s\).

The reduced energy also has strict supporting inequalities between
any two distinct regular points, even if a segment between their
base points is not known to stay regular. Apply the strict supporting
inequality of \(\mathcal E\) at the first interior minimizer to
the second. The \(d\rho\) terms vanish, giving
\[
 e_c(s_2)>e_c(s_1)+\nabla e_c(s_1)\cdot(s_2-s_1)
                         \qquad(s_1\ne s_2\text{ in }D_{\rm reg}).
 \tag{16}
\]
In particular the gradient is strictly monotone between those points.
This does not replace the interior-minimizer requirement in (9)
by strict linear feasibility alone.

## 3. Exact convex projection of every low-energy collar

Assume now that the original charged positive solution at \(u=0\)
is supplied. Write its angle assignment as \(z_0\), its real
angles as \(s_0\), and \(E_0=\mathcal E(z_0)\). It is the unique
global minimum of \(\mathcal E\). Put
\[
 \Delta=\min_{\partial\mathcal P_c}\mathcal E-E_0>0,
 \qquad 0<\delta<\Delta,
 \qquad D_\delta=\{s\in\overline D:e_c(s)<E_0+\delta\}.
 \tag{17}
\]

**Theorem 2.** The set \(D_\delta\) is a bounded convex open
domain with smooth boundary. Its closure is compactly contained
in \(D_{\mathrm{reg}}\), and
\[
 \begin{aligned}
 \overline{D_\delta}
   &=\{s:e_c(s)\le E_0+\delta\}
     =\pi_s\{z:\mathcal E(z)\le E_0+\delta\},\\
 \nabla e_c(D_\delta)&=
       \Omega_\delta:=\{u:\mathcal E(z_u)<E_0+\delta\},\\
 \Gamma_\delta:=t(\Omega_\delta)
   &=\{s+i h(s):s\in D_\delta\}.
 \end{aligned}
 \tag{18}
\]
Here \(z_u\) is the unique closed tilted minimizer from the
original inverse-period theorem. Thus (18) is the exact real-angle
projection of that theorem's collar, with its same marking and
its same energy level, not a substitute contour.

**Proof.** The closed full sublevel
\(K_\delta=\{z:\mathcal E(z)\le E_0+\delta\}\)
is compact and lies in \(\mathcal P_c\). Whenever
\(e_c(s)\le E_0+\delta\), every fiber minimizer lies in
\(K_\delta\), so the fiber has its unique interior minimum.
Thus the weak reduced sublevel is exactly \(\pi_s(K_\delta)\),
is compact, and lies in the open set \(D_{\mathrm{reg}}\).
Likewise the strict sublevel is the projection of the strict
full sublevel. It is open by surjectivity of the affine projection,
or by Proposition 1, and is convex by convexity of \(e_c\).
It contains a neighborhood of \(s_0\).

Its closure is the weak sublevel. To approximate a weak-level
point, take its segment toward \(s_0\) and use convexity with
\(e_c(s_0)=E_0<E_0+\delta\). Lower semicontinuity gives the
opposite inclusion. On a neighborhood of the weak sublevel the
function is analytic and has positive definite Hessian (15).
Its gradient vanishes only at \(s_0\), by Proposition 1 and
uniqueness at \(u=0\). The level \(E_0+\delta\) is therefore
regular, proving smoothness of the boundary.

For \(s\in D_\delta\), Proposition 1 identifies its fiber
minimizer with \(z_{\nabla e_c(s)}\), proving one inclusion
in the second line of (18). Conversely any \(u\) in that line
has an interior minimizer in \(K_\delta\); its real-angle
projection lies in \(D_\delta\) and its gradient is \(u\).
The third line now follows from the same inverse correspondence.
\(\square\)

In these coordinates the original calibrated action is particularly
simple. Retain
\[
 \Phi_c(t)=\sum_{e=vw}\psi(t_v,t_w)
       +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
       -i\sum_{v\in S}c_vt_v,
 \qquad (\Phi_c)_t=-\frac{P+\pi i c}{\pi}.
 \tag{19}
\]
The exact edge energy identity gives, on the graph,
\[
 \Re\Phi_c(s+i h(s))=mM_\infty-\frac{e_c(s)}\pi,
                      \qquad M_\infty=\psi(0,0).
 \tag{20}
\]
This uses arbitrary fixed charges, as in the finite-period
compactness theorem, not only unit charge. The right side is
strictly concave on \(D_\delta\), has its unique maximum at
\(s_0\), and has exactly the boundary loss \(\delta/\pi\).
Compactness and (15) also give a constant \(\kappa_\delta>0\)
such that
\[
 \Re\Phi_c(t^0)-\Re\Phi_c(s+i h(s))
       \ge\frac{\kappa_\delta}{2\pi}|s-s_0|^2
                         \qquad(s\in\overline{D_\delta}).
 \tag{21}
\]
To see this, take the minimum eigenvalue of \(\nabla^2e_c\)
on the compact weak sublevel and integrate twice along the
segment from \(s_0\), which stays in that convex sublevel.
For a lower-half-plane center, sufficiently small \(\delta\)
keeps the entire closed graph in that half-plane, since the
full energy sublevels shrink to their unique minimizer. No
height sign is asserted on the whole regular locus.

## 4. The exact height cost of a vertical connector

Fix \(s\in D_{\mathrm{reg}}\). Suppose a real vector \(v\)
is such that the entire segment
\[
             t_r=s+i(h(s)+r v),\qquad 0\le r\le1,
 \tag{22}
\]
stays in the original positive domain with the fixed outside
data and continued original logarithms. This segment hypothesis
is additional: no global vertical convexity of that domain is used.
At its initial point (11) gives
\[
 \nabla_h\Re\Phi_c=\frac{\Im P+\pi c}{\pi}=0,
 \qquad
 \nabla_h^2\Re\Phi_c=\frac{\Re J}{\pi}>0.
 \tag{23}
\]
Twice integrating along (22) therefore gives the exact identity
\[
 \boxed{\quad
 \Re\Phi_c(t_1)-\Re\Phi_c(t_0)
   =\frac1\pi\int_0^1(1-r)
                   v^{\mathsf T}\Re J(t_r)v\,dr.
 \quad}
 \tag{24}
\]
The increase is strictly positive for \(v\ne0\). In particular
the graph is a strict minimum in the imaginary-angle directions,
despite being a strict maximum along its real-angle graph near
the geometric center.

On a compact positive neighborhood with \(\Re J\le\Lambda I\),
the cost in (24) is at most \(\Lambda|v|^2/(2\pi)\).
For a point on \(\partial D_\delta\), a connector segment
of this type consequently remains below the center's action by
at least
\[
                         \frac{\delta-\Lambda|v|^2/2}{\pi}
 \tag{25}
\]
when the numerator is positive. Such a common compact neighborhood
and a sufficiently small uniform displacement exist around the
closed graph. Formula (25) is a local budget for a short side
connector. It does not assert that the displacement needed to reach
the original endpoint faces or wire seams fits that budget, or that
such a displacement remains in a positive chart. Compactness of
finite real-period data does not change the sign in (24).

There is nevertheless a valid local comparison with the constant
geometric height \(h_0=h(s_0)\). On a sufficiently small compact
convex real-angle neighborhood \(Q\) of \(s_0\), the graph, the
constant-height slice and every segment between them stay positive.
On that slice
\(\nabla_s^2\Re\Phi_c(s+i h_0)=-\Re J/\pi<0\), and its
gradient vanishes at \(s_0\). Both endpoint chains therefore
have their unique maximum at \(s_0\). Vertical convexity bounds
the intervening prism by the larger endpoint action, giving a
strict uniform gap on \(\partial Q\). This is the original
period-coordinate application of the local Legendre-prism argument
already recorded in [the general contour note, Section 5](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/general_legendre_rivin_contour.md).
It is not a connection to the real-height rim or the full source
faces.

The real-height rim has a more definite limitation. Write
\(\mathcal E(s,0)\) for the ambient energy at zero incidence
angles; it need not satisfy the charged rows (2). At fixed
\(s\in(-\pi,\pi)^S\), all real original angles give positive
edges and real returns. Thus the zero-incidence assignment has
zero incidence gradient and is the strict minimum of the ambient
energy in its convex fixed-\(s\) incidence domain. The original
edge energy identity consequently gives
\[
 \begin{aligned}
 \Re\Phi_c(s)&=mM_\infty-\mathcal E(s,0)/\pi,\\
 \Re\Phi_c(s)-\Re\Phi_c(s+i h(s))
             &=\{e_c(s)-\mathcal E(s,0)\}/\pi\ge0.
 \end{aligned}
 \tag{26}
\]
Equality holds exactly when the graph's incidence assignment is
zero, equivalently when \(h(s)=0\). Equivalently, all rows satisfy
\(n_vs_v=2\pi c_v\): in that case the zero-incidence assignment
is feasible and is the fiber minimum. The reality assertions here
follow either directly from the square dictionary or from the
canonical real positive-edge formulas.

If \(h(s_0)\ne0\), (26) gives
\(\Re\Phi_c(s_0)>\Re\Phi_c(t^0)\). By continuity and the
shrinking of \(K_\delta\) to \(z_0\), every sufficiently small
projected collar has its entire real rim strictly above the target:
\[
 \Re\Phi_c(s)>\Re\Phi_c(t^0)
                      \qquad(s\in\overline{D_\delta}).
 \tag{27}
\]
Thus vertical sides all the way to \(h=0\) cannot be lower-action
connectors for such collars, even if those sides happen to stay
positive. This endpoint conclusion does not require their positivity.
It is the fixed-real-angle energy excess already underlying
[the physical-pressure theorem](research_charged_source_physical_pressure.md),
applied here to the actual collar projection. It concerns the
classical selected action, not the size of a signed trace remainder.

## 5. Exact remaining source task

The construction supplies the explicit convex real-angle domain (8),
its regular fiber-minimum locus, and the exact collar projection (18).
It proves neither that every strictly feasible real angle is regular
nor that the full inverse-period image has a prescribed topology.
The closed fiber problem and the closed tilted problem are different;
uniqueness of every tilted minimizer is not an assertion of uniqueness
of every boundary fiber minimizer.

For the original finite source, the relative boundary is still its
angular endpoint faces and wire seams, with the retained full Hermite
trace and free cardinal ends. The boundary of (18) is an interior
energy level, not one of those prescribed source faces. The exact
finite-period theorem also exhibits genuine trace poles on parts of
the positive inverse slice; it does not place those parts in the
component containing the center. Any deformation through such poles
requires its actual residue/current terms. Small detours and a local
action budget do not show that those terms have smaller complete
source rate.

Thus the result gives a canonical real-angle graph on which to try
the global contour construction and an exact test of one possible
connector's classical cost. It supplies no identification of the
whole original relative class, no bound for the remaining joint
factorial/wire source, and no nonzero quantum cycle coefficient.

## Direct sources and author readback

* [Original convex variation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_positive_filling_convex_variation.md),
  SHA256 `2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0`:
  square energies and differential, original affine incidence rows,
  strict feasibility, convex extension and interior uniqueness.
  Complete source text read in this sequence.
* [Original inverse-period descent](research_positive_period_inverse_descent.md),
  SHA256 `b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565`:
  exact tilted image, accretive Jacobian, calibrated action, and the
  existing bounded star-shaped collars. Complete text reread.
* [Finite real-period compactness](research_real_period_image_compactness.md),
  SHA256 `8ecdecc2c71e8a47a83fe60986ed618abaa926937920f376abebed779fb0c37e`:
  fixed-charge extension, bounded finite-period data and action
  calibration, and the precise original-source pole/relative-boundary
  limitations used in Section 5. Complete text reread.
* [General Legendre contour](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/general_legendre_rivin_contour.md),
  SHA256 b51be11036b05fbccd586c2d0a4505559631870357cf128dd256dcc87e26970b:
  coverage for the already known local convexity/prism argument;
  no source realization is imported from that different positive
  triangulation chart.
* [Physical charge pressure](research_charged_source_physical_pressure.md),
  SHA256 1e127c0842c0d6d5727a517cc66c39e73baa2846848c284d257c1ebe49679091:
  coverage for the same fixed-real-angle energy excess in (26).
  No positive-pressure estimate is identified with the original
  signed scalar.

Only written proofs, source-text reads and metadata hashes were used.
No mathematical program, numerical calculation, test or compilation
was run. Frozen notes, manuscripts and public documents were unchanged.
