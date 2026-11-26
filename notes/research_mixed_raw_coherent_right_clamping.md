# Upper-taper clamping with one raw right edge

Research theorem, 5 November 2026. This note retains the raw right-edge label throughout;
no comparison with a complex saddle of that edge is used.

Use the typed polygons \(\Omega_3,\Omega_4\), unselected coefficient
bands \(K_3=[-.03,.02]\), \(K_4=[-.057,0]\), and original coherent
phases \(\phi_{\eta,\epsilon}\) of the
[coherent clamping theorem](research_mixed_unselected_right_clamping.md).
Set
\[
 t\in[.45,.5],\quad k\in K_{3+\alpha},\quad
 R(t)=400(.5-t)^2,\quad z=t+ikR(t),\quad q=1+ikR'(t).
 \tag{1}
\]
The other coherent argument \(a\) ranges independently over its full
typed polygon, including selected neighboring heights. The raw right
argument is fixed at \(.5\), after the complete right-angle and row
reductions. It retains its original type \(\beta\).

Let \(d=1\) when \(z\) is the first argument of the raw edge,
and \(d=0\) otherwise. Its own factorial indicator is
\(\epsilon=\beta\) if \(d=1\), and \(\epsilon=\alpha\)
if \(d=0\). The raw row maximum is unique, with
\(1/5<u_*<2/5\), by the
[complete bracket theorem](research_mixed_right_boundary_row_bracket.md).
Its original stationarity equation is
\[
 T(u,z)=\Re\{g'(u+.5)+g'(u+z)-(2+\epsilon)g'(u)
             +2\pi i[d z+(1-d)/2]\}=0,
 \qquad T_u\le-2\pi.
 \tag{2}
\]
The allocated raw marginal at this row is
\[
 K(z,u)=g'(z+u)-(1+\alpha/2)g'(z)+2\pi i d u.
 \tag{3}
\]
These are the actual signed-height formulas; no unsmoothed-radius
convention is extended from one height sheet to the other.

Write \(G=\partial_2\phi_{\eta,\alpha}(a,z)\) if \(d=1\),
and \(G=\partial_1\phi_{\alpha,\eta}(z,a)\) otherwise. 
**Theorem 1.** On every domain above,
\[
                    D=\Re\{q[G+K(z,u_*)]\}<-1/20.\tag{4}
\]
It is the derivative of the sum of one coherent allocated rate and
one maximized raw allocated rate. Only real-row stationarity is used
in differentiating the maximum. All selected-neighbor corrections
are fixed during this motion. The center is unselected; for a
four-type center its nonpositive height makes the factorial weight
branch govern up to \(.5\) from the left. At the endpoint the
statement uses the continuous upper rate, with the original Fourier
upper bound retained. It does not assert a relative nonzero finite
weight at that endpoint.

## Exact reduction and checker

For fixed \(t,k\), only \(G\) depends on \(a\), holomorphically
on a neighborhood of the whole typed polygon. The original root and
complete coherent packet on these products are supplied by the
closed-cotangent, interface, right-guard and right-square inputs
listed in the coherent clamping note. The harmonic maximum principle
therefore reduces \(a\) to its six boundary edges. There are exactly
\(2^4\cdot6=96\) families, indexed by \((d,\alpha,\beta,\eta)\)
and the edge. Each has three real parameters: edge position, \(t\),
and \(k\). This reduction does not use harmonicity in \(t,k\).

For a real parameter differential, the exact formulas are
\[
 \begin{split}
 dz&=q\,dt+iR\,dk,&dq&=i(800k\,dt+R'\,dk),\\
 K_z&=g''(z+u)-(1+\alpha/2)g''(z),&K_u&=g''(z+u)+2\pi i d,\\
 du_*&=-\Re(K_u\,dz)/T_u,&
 dD&=\Re\{dq(G+K)+q(dG+K_zdz+K_u du_*)\}.
 \end{split}\tag{5}
\]
Here \(dG\) is the corresponding row of the original complex Schur
Hessian. In particular the response of the real maximizing row is
not a complex critical-point Schur complement.

The checker encloses the coherent root by the existing original-log
whole-cell affine Newton self-map, and separately encloses its exact
midpoint root. For the raw row, sign-validated midpoint bisection gives
a trial \(u_0\); on the whole cell,
\[
 |u_*(z)-u_0|\le |T(u_0,z)|/(2\pi).\tag{6}
\]
An uncertain sign does not remove either possible zero. The full-box
formula (5) gives a mean-value upper bound about the midpoint. The
minimum of that bound and direct interval evaluation is valid. A
strictly signed full derivative permits a maximizing-face reduction;
otherwise exact rational bisection retains both children. Saved mode
rechecks every root, derivative, signed reduction and leaf, exhausting
the complete tree without new complex-root proposals.

The complete 96-family outward cover verifies (4). Integration along fixed \(a,k\) yields
an upper-rate loss \((t-.45)/20\) upon clamping to \(.45\).
On the actual hybrid graph all slow and fast left cutoffs are one on
this motion, so neighboring heights stay fixed and the attenuated
coefficient \(k\) remains constant. The two incident edges remain
one coherent edge and one raw edge. The original complete raw source
bound and coherent packet give this rate comparison with an arbitrary
single finite-source tolerance; no lower bound for the raw finite
kernel is inferred.

Selected moving centers are excluded. No result for an opposite
extended half stencil, all minimum-flow cases, a whole contour
integral, or finite-sum noncancellation follows from this local criterion.

    python3 experiments/certify_mixed_raw_coherent_right_clamping.py
