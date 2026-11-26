# The marked geometric action for nearby boundary colors

Research theorem, 6 November 2026. For every fixed positive path whose
crossing powers are three or four, the stationary action of the original
source agrees with the marked geometric action on a neighborhood of both
complete boundary colors. The constant is the one already determined at
completeness. This discharges the additional geometric premise in the
[mixed-source stability reduction](research_mixed_open_source_stability_reduction.md).
The estimates for the whole finite source in that reduction remain open.

The proof continues the actual filling equations and their original
logarithms. Equality at one boundary color is used only to fix a constant
after the boundary derivatives have been proved equal.

## 1. The two actions and the statement

Fix a path with selected vertices numbered \(1,\ldots,m\), where
\(m\ge1\), and powers \(n_j\in\{3,4\}\). Each selected vertex
has two original incidences. The two outside ends are distinct; their
angles are \(\theta_L,\theta_R\), and their ordinary colors are
\[
 w_L=-2\cos\theta_L,\qquad w_R=-2\cos\theta_R.
 \tag{1}
\]
For use inside a marked circle tree, retain the original incidence
orders, half-twist carriers, disk longitudes and integral parameters
\(n_j=\eta_j-2p_j\). No diagram reduction changes those parameters.

Let \(\mathcal F_m(z;\boldsymbol\theta)\) be the actual source
action in the [boundary-response note](research_mixed_open_word_boundary_response.md).
Here \(z\) comprises the \(2m\) leg coordinates and the two
endpoint wire coordinates. At each end its color-dependent contribution,
including the endpoint chirp, is
\[
 F(e,x;\theta)=
 -J(1/2-x+\theta/(2\pi))-J(1/2-x-\theta/(2\pi))
 -3J(x)-J(e-x)+i\pi ex.
 \tag{2}
\]
The primitive satisfies \(J'(u)=\Log(2\sin\pi u)\), with the
original branch and normalization. All other terms of the source action
are unchanged. Let
\[
 \mathcal W_m(\boldsymbol\theta)
   =\mathcal F_m(z(\boldsymbol\theta);\boldsymbol\theta)
 \tag{3}
\]
be its stationary action through the already localized complete point.
The source Hessian theorem proves existence and uniqueness of this
holomorphic critical branch near zero.

Write \(t_0=\theta_L\), \(t_{m+1}=\theta_R\), and define the
geometric action before eliminating the selected angles by
\[
 \mathcal A_m(\mathbf t;\boldsymbol\theta)
 =\sum_{j=0}^{m}\psi(t_j,t_{j+1})
   +\sum_{j=1}^{m}\left(\frac{in_jt_j^2}{4\pi}-it_j\right).
 \tag{4}
\]
The edge primitive \(\psi\) has its original complete constant and
derivatives \(\psi_t=-r_t/\pi\), where \(r_t\) is the original
meridian increment. The selected stationary equations are exactly
\[
 \sum_{e\ni j}r_{j,e}=\frac{in_j}{2}t_j-\pi i.
 \tag{5}
\]
Let \(m_3\) be the number of powers equal to three, and let
\(i\gamma\), \(\gamma\in\mathbb R\), be the fixed type-three
constant of the [absolute calibration](research_mixed_geometric_action_calibration.md).

**Theorem 1.** For every fixed path there is a complex bidisk about
\(\boldsymbol\theta=0\) on which the original marked geometric
solution \(\mathbf t(\boldsymbol\theta)\) and its inverse leg
coordinates are holomorphic, the inverse coordinates equal
\(z(\boldsymbol\theta)\), and
\[
 \boxed{\quad
 \mathcal W_m(\boldsymbol\theta)
 =\mathcal A_m(\mathbf t(\boldsymbol\theta);\boldsymbol\theta)
                         +i m_3\gamma.
 \quad}
 \tag{6}
\]
The equality includes the full complex constant and all boundary
derivatives. Both sides descend to holomorphic functions of the ordinary
colors in (1). The original positive cells, face identifications and
selected primitive filling periods persist on this neighborhood. The
outside auxiliary cusps are permitted to become incomplete; they have
their prescribed outside angles. Main cusps remain complete.

## 2. Continue the original geometric solution

At zero outside angles, the
[source-geometric identification](research_mixed_geometric_source_identification.md)
gives the same positive complete-ended point for the two constructions.
At each original edge the
[positive-edge Hessian theorem](research_positive_edge_global_monotonicity.md)
gives \(-\Re\psi''\succ0\). Sum these forms and restrict the
outside angles to be fixed. Every selected vertex has an incident edge,
so
\[
 -\Re\mathcal A_{m,\mathbf t\mathbf t}\succ0.
 \tag{7}
\]
The crossing terms have purely imaginary constant Hessian. A complex
symmetric matrix with strictly positive Hermitian real part is
invertible: if it killed a nonzero vector, pairing with its conjugate
would contradict positivity. The holomorphic implicit-function theorem
therefore gives \(\mathbf t(\boldsymbol\theta)\) solving the
full equations (5), with their fixed charge one, near zero.

All original shapes are strictly positive at the center, all face-map
denominators are nonzero, and every selected core has positive length.
These are open conditions for the fixed finite collection of cells.
Shrink the bidisk so that they persist. The original gluing and
peripheral identities are the same rational identities used by
[marked completion](research_positive_point_marked_completion.md).
Their logarithmic lifts are continued from the center. In particular
the original primitive slopes remain fixed by (5), rather than merely
having exponentiated multiplier one. The local tube completion of that
note applies to each selected core. This gives the marked deformation
germ; it does not assert completeness at a nonzero outside angle.

On every edge put
\[
 a=\tan(t/2),\quad b=\tan(u/2),\quad
 q^2=1+a^2+b^2,\qquad
 x=\pi^{-1}\arctan(1/q).
 \tag{8}
\]
Choose the same square-root and inverse-tangent branches as at the
complete-ended geometric point. These functions are regular locally.
The original stationary-wire identity is
\[
 b(x,t)+b(x,u)=\psi(t,u),\qquad
 \partial_x\{b(x,t)+b(x,u)\}=0,
 \tag{9}
\]
at this wire, where
\[
 b(x,t)=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x).
 \tag{10}
\]
The identities in (9) are proved as holomorphic identities, with
their complete constants, in Section 5 of
[the unsummed phase note](research_unsummed_network_phase_coercivity.md).
Thus they apply on a neighborhood, including both outside edges.

## 3. The deformed geometry solves the original source equations

At a selected vertex let its angle be \(t\), its wires be \(x,y\),
and set
\[
 X=e^{2\pi ix},\quad Y=e^{2\pi iy},\qquad
 U=\frac{1-X}{1+X(1+2\cos t)},\quad
 V=\frac{1-Y}{1+Y(1+2\cos t)}.
 \tag{11}
\]
The inverse legs are \(s=i\Log U/(2\pi)\) and
\(v=i\Log V/(2\pi)\), with their original logarithms continued
from the identified point. Every denominator and logarithm argument
is nonzero there, so all these functions are regular on a smaller
bidisk. This step needs no global choice of a new logarithmic branch.

Let \(\epsilon=n-3\) and use the original incidence primitive
\[
 \ell_s(x)=2\pi isx-
 \frac{\operatorname{Li}_2(XU)-\operatorname{Li}_2(X)}{2\pi i}
 -\pi ix,
 \qquad g(s)=J(s)+\frac{i\pi}{2}(s-s^2).
 \tag{12}
\]
The unsummed vertex action is
\[
 \mathcal V_n=g(s+v)-\epsilon\{g(s)+g(v)\}
                              +\ell_s(x)+\ell_v(y).
 \tag{13}
\]
The factorization in the
[unit-period elimination](research_mixed_unit_period_leg_elimination.md)
is an algebraic identity, independent of the outside angles. Applying
it to (5) and (11) gives
\[
 X(1-UV)=(1-U)^\epsilon(1-XU),\qquad
 Y(1-UV)=(1-V)^\epsilon(1-YV).
 \tag{14}
\]
Consequently \(\exp(\partial_s\mathcal V_n)=
\exp(\partial_v\mathcal V_n)=1\). The derivatives are
holomorphic on the connected small bidisk. They are zero at its center
by the [original logarithmic-lift theorem](research_mixed_geometric_source_log_lifts.md).
A continuous function with values in \(2\pi i\mathbb Z\) is
constant, so both derivatives are exactly zero throughout the bidisk.
The proof keeps the selected charge equal to one throughout.

The same argument fixes the wire derivatives. The algebraic identity
\[
 \exp(\partial_x\ell_s)=
 \frac{XU-1}{U(1-X)}=
 -\frac{X^2+2X\cos t+1}{(X-1)^2}
 =\exp(\partial_x b(x,t))
 \tag{15}
\]
holds by (11). Their difference is zero at the center by the absolute
calibration, and hence remains zero. At an internal edge, the two
incidence derivatives consequently sum to zero by (9). At an outside
edge, the selected incidence derivative plus \(b_x(x,\theta)\)
also sums to zero.

These are also the equations of the contracted source. To check the
normalization at an outside edge before differentiating, the already
calibrated endpoint identity extends immediately to
\[
 F(e,x;\theta)-\frac{i\pi}{2}(e-e^2)
                       =\ell_e(x)+b(x,\theta).
 \tag{16}
\]
Indeed both sides change from their value at \(\theta=0\) by
exactly \(b(x,\theta)-b(x,0)\); the zero-color identity is
[the endpoint calibration](research_mixed_endpoint_action_calibration.md),
Theorem 1.

At an internal edge, the contraction is unchanged. Its expression is
\(G(s,v)=J(s+v)-2J(s)-2J(v)-i\pi(s+v-(s+v)^2)/2\).
For the stationary wire, its leg derivatives equal those of
\(\ell_s(x)+\ell_v(x)\): these are the rational identities
(17)--(18) of the absolute calibration with their continued zero
logarithmic lifts. They remain valid on the local germ just as in
(15). The wire derivative is zero, so differentiating through its
elimination adds no term. The source's quadratic chirps telescope
by the same polynomial identity as at zero outside angles.

Thus the inverse geometry in (11), together with the two endpoint
wires, solves every actual equation
\(\mathcal F_{m,z}=0\). It agrees with the localized source point
at the center. Local uniqueness of the source critical branch proves
that these inverse coordinates are precisely
\(z(\boldsymbol\theta)\). No assertion that the charge family
covers an open set of independent leg coordinates is needed.

## 4. Boundary derivatives determine the full action germ

Since the source is stationary in its internal variables, its only
explicit dependence on \(\theta_L\) gives
\[
 \partial_{\theta_L}\mathcal W_m
   =b_t(x_0,\theta_L).
 \tag{17}
\]
Here \(x_0\) is the original left outside wire at the common
critical point. Similarly the right derivative is
\(b_t(x_m,\theta_R)\).

The geometric envelope has the derivatives
\[
 \frac{d}{d\theta_L}
   \mathcal A_m(\mathbf t(\boldsymbol\theta);\boldsymbol\theta)
 =\psi_1(\theta_L,t_1)=b_t(x_0,\theta_L),
 \tag{18}
\]
and likewise at the right end. The selected-angle derivatives vanish
by (5); the last equality is the stationary-wire identity (9),
differentiated with its zero wire derivative. Equations (17)--(18)
prove that the difference in (6) is constant on the bidisk.
The complete-point calibration, equation (23) of its note, fixes this
constant as \(i m_3\gamma\). This proves (6).

The source action is separately even in the two outside angles, by
(2) and local uniqueness. It therefore descends to (1), since
\(w+2=\theta^2+O(\theta^4)\) is a local analytic coordinate
in \(\theta^2\). Equality (6) gives the same descent for the
stationary geometric action. In particular the ordinary-color
derivatives really are derivatives of the marked geometric action,
including its changes away from completeness.

There is an explicit peripheral form of these derivatives. The original
edge primitive satisfies \(\psi_1=-r_1/\pi\), so
\[
 \partial_{\theta_L}\mathcal W_m
    =-\frac1\pi\operatorname{arsinh}
       \{\tan(\theta_L/2)\cos(t_1(\boldsymbol\theta)/2)\},
 \tag{19}
\]
with the original branch; at the right end replace \(t_1\) by
\(t_m\). At zero outside angles, differentiation of (19) gives
\[
 \begin{split}
 \mathcal W_{m,\theta_L\theta_L}(0)
      &=-\frac{\cos(t_1(0)/2)}{2\pi},\\
 \mathcal W_{m,\theta_R\theta_R}(0)
      &=-\frac{\cos(t_m(0)/2)}{2\pi},\qquad
 \mathcal W_{m,\theta_L\theta_R}(0)=0.
 \end{split}
 \tag{20}
\]
The derivative of the selected angle contributes no term here because
it is multiplied by \(\tan(\theta_L/2)=0\), or by its right
counterpart. At a complete outside edge, (8) gives
\(\tan(\pi x_0)=\cos(t_1(0)/2)\), with the branches fixed
at completeness. Thus (20) agrees exactly with the earlier source
formula in terms of \(\tan(\pi u_L)\); its ordinary-color
derivative is \(-\cos(t_1(0)/2)/(4\pi)\). This checks the
factor of two from \(w+2=\theta^2+O(\theta^4)\) without
changing the meridian or longitude normalization.

## 5. Volume normalization and the remaining analytic problem

For nearby outside angles, the original cell-volume formula is
\[
 V_{\rm cells}(\boldsymbol\theta)
 =2\pi\Re\mathcal W_m(\boldsymbol\theta)
 -2\Im\theta_L\,\Im r_{0,\{0,1\}}
 -2\Im\theta_R\,\Im r_{m+1,\{m,m+1\}}.
 \tag{21}
\]
This is the [positive-edge volume identity](research_positive_edge_volume_identity.md),
equation (24), with (6). In particular the correction vanishes at
complete outside colors, and also at real outside angles on this
local branch. For general complex angles the correction must be kept.
Edges outside this selected path that remain complete contribute their
unchanged original complete volumes when the component is assembled in
a tree. Edges incident to a deformed outside vertex instead contribute
their own continued edge actions and the volume corrections in (21).

The same calculation retains the peripheral normalization explicitly.
For an outside end \(b\) with original carrier \(\eta_b\), let
\(U_b,V_b\) denote the continued logarithms of the original
meridian and disk-longitude multipliers. If this path supplies its sole
incident edge, equation (15) of the marked-completion note gives
\[
 U_b=-2\pi\partial_{\theta_b}\mathcal W_m-i\eta_b\theta_b,
 \qquad V_b=2i\theta_b.
 \tag{22}
\]
At a shared outside vertex, first sum the derivatives of every incident
component and every remaining edge; subtract the carrier term just
once. Thus the source action determines the actual marked peripheral
periods on the germ. The multipliers \(e^{U_b},e^{V_b}\) here are
affine holonomy multipliers; identifying them with eigenvalue variables
in a chosen \(SL_2\) convention requires its corresponding square
roots. Neither the carrier term nor that convention can be discarded.

The local nonzero source coefficient and the geometric germ are now
both available for every fixed positive three/four path. To use it
in the long-filling theorem, two analytic conclusions in the
mixed-source stability reduction still have to be proved for the
**entire** original polynomial:

1. The complementary contour and Fourier terms are exponentially
   smaller on a fixed complex ordinary-color neighborhood.
2. Outside a small real boundary-color neighborhood, the whole source
   has a strict gap below this same geometric action.

Once these hold, the strip argument and component assembly of that
reduction apply without a further geometric-germ assumption. Uniform
reversal of all signs follows by the original conjugation symmetry,
with the continued marking; arbitrary mixtures of small positive and
negative powers do not follow from this theorem. The local identity
does not establish either missing analytic estimate, nor the
finite-exception theorem.
