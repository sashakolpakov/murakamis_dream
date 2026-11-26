# The contracted action on the positive three/four path

Research proof, 5 November 2026. The original contracted action, evaluated
at the inverse of the positive geometric solution, has real part equal
to the volume of its original cells divided by \(2\pi\). All logarithms
and additive constants are retained. This does not yet identify that
point with the independently localized source critical point, and does
not estimate the complete finite open-chain sum.

## 1. Two actions at a vertex

Consider the positive path charge family with powers \(n_v\in\{3,4\}\),
two incidences at each selected vertex, and complete outside vertices.
The two incidences include outside edges at an endpoint. Use the
original angle \(\tau\), wire coordinates \(x,y\), and inverse leg
coordinates \(s,t\) at one selected vertex. Set
\[
 X=e^{2\pi ix},\quad U=e^{-2\pi is},\qquad
 Y=e^{2\pi iy},\quad V=e^{-2\pi it},\qquad \epsilon=n-3.
 \tag{1}
\]
The primitives are those of the
[original logarithmic-lift theorem](research_mixed_geometric_source_log_lifts.md):
\[
\begin{split}
 J'(z)&=\Log(2\sin\pi z),\qquad
 \varphi(z)=\frac\pi2(z-z^2),\qquad g=J+i\varphi,\\
 \ell_s(x)&=2\pi isx-
 \frac{\operatorname{Li}_2(XU)-\operatorname{Li}_2(X)}{2\pi i}
 -\pi ix,\\
 b(x,\tau)&=-J(1/2-x+\tau/(2\pi))
             -J(1/2-x-\tau/(2\pi))-2J(x).
\end{split}                                                    \tag{2}
\]
Define the source and angular vertex actions by
\[
\begin{split}
 \mathcal V_n&=g(s+t)-\epsilon\{g(s)+g(t)\}
                          +\ell_s(x)+\ell_t(y),\\
 \mathcal B_n&=b(x,\tau)+b(y,\tau)
                         +\frac{in\tau^2}{4\pi}-i\tau.
\end{split}                                                    \tag{3}
\]
The linear term in \(\mathcal B_n\) is the unit-charge term.
It is not used as a stationary angular action when the own charge
is fractional.

The [wire-order theorem](research_positive_path_real_wire_order.md) keeps
the angular factorial arguments in \(0<\Re z<1\). The inverse-leg
and [wire-before-leg theorem](research_mixed_wire_before_inverse_leg.md)
give \(0<\Re x<\Re s<1/2\) and \(\Im x>0\) at an active edge,
with the regular complete limit \(x=1/4\). Thus \(XU\) stays below
the real axis. The dilogarithms in (2) have their original principal
cut-plane continuation, even if \(|XU|>1\). None of these statements
extends a finite-product asymptotic outside its proved domain.

## 2. The incidence derivatives agree throughout the charge family

The inverse leg has the exact expression
\[
 U=\frac{1-X}{1+X(1+2\cos\tau)}.
 \tag{4}
\]
Differentiation and substitution give
\[
\begin{split}
 e^{\partial_x\ell_s(x)}
 &=\frac{XU-1}{U(1-X)}
  =-\frac{X^2+2X\cos\tau+1}{(X-1)^2}\\
 &=\frac{\cos(\pi x-\tau/2)\cos(\pi x+\tau/2)}
          {\sin^2\pi x}
  =e^{\partial_x b(x,\tau)}.
\end{split}                                                    \tag{5}
\]
All derivatives are continuous on the original charge family, by the
regularity just established. Their difference belongs to
\(2\pi i\mathbb Z\). Simultaneously scale all charges to zero.
At that endpoint
\[
 x=1/4,\quad X=i,\quad \tau=0,\quad
 U=(-1-2i)/5,\qquad 1-XU=-U(1-X).
 \tag{6}
\]
Here \(\partial_x b=0\). The principal logarithms obey
\(\Log(1-XU)=\Log U+\Log(1-X)+\pi i\), so
\(\partial_x\ell_s=0\) as well. Consequently
\[
                  \partial_x\ell_s(x)=\partial_x b(x,\tau)
 \tag{7}
\]
on the entire family. This uses no unit-charge vertex equation.

Now keep the own charge equal to one and vary the other charges.
The logarithmic-lift theorem gives
\((\mathcal V_n)_s=(\mathcal V_n)_t=0\). The original return
equation gives
\[
 r_x+r_y=\frac{in\tau}{2}-\pi i,
 \qquad (\mathcal B_n)_\tau
      =-\frac{r_x+r_y}{\pi}+\frac{in\tau}{2\pi}-i=0.
 \tag{8}
\]
The chain rule and (7) therefore imply
\[
                      d(\mathcal V_n-\mathcal B_n)=0
 \tag{9}
\]
along each such fixed-own-charge path. No invertibility of a map from
charges to wires is required for this argument.

## 3. Fixing the two vertex constants

With the own charge fixed at one, scale every other charge to zero.
The two neighbors then have complete angle zero. The resulting isolated
vertex depends only on its own power: the positive charge theorem gives
the unique branch, and both returns and wires are equal. Equation (9)
reduces calibration at any vertex to this same isolated vertex.

For power three, use the middle vertex of the complete-ended all-three
chain of length three. Keep its charge one and increase the two end
charges from zero to one. Its final point belongs to the connected
chart of the [three-chain action calibration](research_three_chain_action_volume_calibration.md).
That result gives
\(\mathcal V_3-\mathcal B_3=i\gamma\), with the fixed real
constant \(\gamma\) specified there. Equation (9) transports this
value back to the isolated vertex and then to every type-three vertex
of the present family.

For power four, at the isolated vertex \(U=V=-\cos\tau\), by
the exact unit-period elimination. The original return is
\[
 r=i\tau-i\pi/2,\qquad
 \sinh r=\tan(\tau/2)=-i\cos\tau.
 \tag{10}
\]
Squaring the last equality and using \(\sin^2\tau+\cos^2\tau=1\)
gives
\[
 U^4-2U^3+1=(U-1)(U^3-U^2-U-1)=0.
 \tag{11}
\]
The proved lower-half-plane condition excludes \(U=1\). The real
cubic \(p(u)=u^3-u^2-u-1\) has only one real root \(r>1\): its
two critical values are \(p(-1/3)=-22/27\) and \(p(1)=-2\),
and \(p(2)=1\). Its other roots are the conjugate pair containing
\(U\). Their product is \(1/r\), so
\[
                         |U|^2=1/r<1.
 \tag{12}
\]
The source equation at the diagonal vertex simplifies to
\[
                X=Y=\frac1{1+2U},\qquad
                         \frac{2X}{1-X}=\frac1U.
 \tag{13}
\]
The geometric wire already has \(\Im X>0\), \(|X|<1\).
Equations (12)--(13) place it in the connected diagonal crescent
\[
 \{K:\Im K>0,\ |K|<1,\ |2K/(1-K)|>1\}
 \tag{14}
\]
used in the [power-four source calibration](research_power_four_source_packet.md#4-the-selected-coefficient-and-the-absolute-phase)
and its [cut-exclusion proof](research_exterior_crossing_phase.md#5-the-phase-constant-is-zero).
The selected angle there satisfies
\(2\cos\tau=1-X^{-1}=-2U\), so it is precisely our angle in
\(0<\Re\tau<\pi,\ \Im\tau<0\). Its index branch is also the
same, since \(s=\Log(1/U)/(2\pi i)\). The calibrated constant
on that crescent is zero. Equation (9) transports it to the full family.

**Theorem 1.** At each degree-two unit vertex of the positive path,
with the original branches and scalar conventions,
\[
 \boxed{\quad \mathcal V_3=\mathcal B_3+i\gamma,
                     \qquad \mathcal V_4=\mathcal B_4.\quad}
 \tag{15}
\]
In particular their real parts agree. The same \(\gamma\) is used
at every type-three vertex; it has not been reset by a branch choice.

## 4. The shared-wire contraction keeps its absolute constant

For the two inverse legs on a shared edge put
\[
 G(s,t)=J(s+t)-2J(s)-2J(t)-i\varphi(s+t).
 \tag{16}
\]
They satisfy \(0<\Re s,\Re t<1/2\); their sum therefore stays
in the regular strip, without needing a lower bound of \(1/2\).
The exact edge identities give
\[
 X=\frac{1-UV}{U+V-2UV},\quad
 \frac{X}{1-XU}=\frac{1-UV}{V(1-U)^2},\quad
 (1-XU)(1-XV)=UV(1-X)^2.
 \tag{17}
\]
The shared-wire logarithmic-lift theorem proves
\(\partial_x(\ell_s+\ell_t)=0\). Furthermore
\[
 G_s=\Log(1-UV)-2\Log(1-U)-\Log V,
 \qquad (\ell_s)_s=\Log X-\Log(1-XU).
 \tag{18}
\]
Their exponentials agree by (17), and likewise for the other leg.
At completeness \(U=V=(-1-2i)/5\), their actual values agree:
use \(1+U=2XU\), \(1-XU=(1-U)/2\), and their principal
arguments. Thus both derivative differences have zero lift along
simultaneous scaling of the charges. The chain rule now makes
\(G-\ell_s-\ell_t\) constant along this path.

The constant is zero, as follows by connecting its complete value
to the absolute [wire contraction calibration](research_mixed_contracted_phase.md#5-absolute-action-under-the-exact-wire-contraction).
That identity is already calibrated at \(U=V=e^{-2\pi i/3}\).
Join this point to \(U=V=(-1-2i)/5\) along
\[
 U(t)=-\frac12+\frac{3t}{10}
       +i\left[-\frac{\sqrt3}{2}
               +\left(\frac{\sqrt3}{2}-\frac25\right)t\right],
 \quad 0\le t\le1,
 \qquad X(t)=\frac{1+U(t)}{2U(t)}.
 \tag{19}
\]
Here \(U\) is strictly in the lower-left quadrant and \(XU\)
strictly in the lower-right quadrant. Writing \(R=|U|^2\), exact
calculation gives
\[
\begin{split}
 3R-2\Re U-1
  &=\frac35(1-t)\{5-(5-2\sqrt3)t\},\\
 R+\Re U
  &=\frac1{10}(1-t)\{5-(10-4\sqrt3)t\}.
\end{split}                                                    \tag{20}
\]
Both braces are positive on \([0,1]\). Thus \(X\) is in the
first-quadrant disk for \(t<1\) and ends at \(i\). All original
index arguments remain regular, \(XU\) avoids the dilogarithm cut,
and \(\arg X+\arg U=\arg(XU)\). The rational derivative
identities and their already fixed logarithmic lifts continue along
this path. They carry the zero constant to the complete point.
Continuity there is harmless: \(X=i\) is not a cut endpoint.
We conclude on every shared edge of the geometric charge family that
\[
                       G(s,t)=\ell_s(x)+\ell_t(x).
 \tag{21}
\]

## 5. The full contracted action evaluated at the geometric point

For a fixed open word of length \(m\ge1\), denote the geometric
inverse legs and outside wires by \(z_{\rm geom}\). At an endpoint,
the [ordinary endpoint calibration](research_mixed_endpoint_action_calibration.md)
gives, with its zero constant,
\[
 F(e,u)-i\varphi(e)=\ell_e(u)+b(u,0).
 \tag{22}
\]
Its hypotheses \(0<\Re u<\Re e<1/2\), \(\Im u>0\)
hold by the wire-before-leg theorem. Sum (21)--(22) with the original
vertex terms. The quadratic parts telescope exactly, using
\(\varphi(a+b)=\varphi(a)+\varphi(b)-\pi ab\). The result is
the original full contracted action \(\mathcal F_m\), including
both endpoint variables and all type-four own terms, with no new
constant.

Moreover \(z_{\rm geom}\) is a critical point of this contracted
action with its original logarithms. For each leg, (18) and its
transpose identify its derivative after contraction with the unsummed
vertex derivative, which is zero. At each endpoint, the derivative
in the outside wire is \(\partial_u\ell_e+\partial_u b(u,0)\).
By (7) this is the original positive geometric wire derivative,
also zero. These are pointwise derivative identities; they do not
require the geometric charge map to cover a neighborhood of all leg
coordinates.

Apply (15) at each vertex, and the original positive stationary-wire
identity \(b(x,\tau_v)+b(x,\tau_w)=\psi(\tau_v,\tau_w)\)
at every edge, including both complete outside edges. If \(m_3\)
is the number of type-three vertices and \(\tau_0=\tau_{m+1}=0\),
this proves the complex identity
\[
 \boxed{\quad
 \mathcal F_m(z_{\rm geom})
  =\sum_{j=0}^{m}\psi(\tau_j,\tau_{j+1})
      +\sum_{j=1}^{m}
           \left(\frac{in_j\tau_j^2}{4\pi}-i\tau_j\right)
      +i m_3\gamma.\quad}
 \tag{23}
\]
The [positive-edge volume identity](research_positive_edge_volume_identity.md#4-a-stationary-action-on-an-arbitrary-selected-region)
therefore gives
\[
                2\pi\Re\mathcal F_m(z_{\rm geom})
                             =V_{\rm cells}.
 \tag{24}
\]
When this path is a selected region in the original marked circle tree,
the [marked completion theorem](research_positive_point_marked_completion.md)
identifies these cells with that region of the partial filling; complete
edges outside the region contribute their original complete volumes.
The primitive coefficients remain \(n_j=\eta_j-2p_j\), and the
filled slopes remain \(\mu_j+p_j\lambda_j\).

Equation (24) is deliberately evaluated at \(z_{\rm geom}\).
Identifying it with the independently localized critical point of the
finite source remains a separate obligation. So do the complete
open-chain contour estimate, the other Fourier selections, and the
boundary estimates needed to attach this chain to a larger tangle.
No new knot class or finite-exception conclusion follows here alone.

The accompanying exact checker verifies the rational identities,
the isolated cubic, the two diagonal-path inequalities, and the
quadratic telescoping. The continuation and constant arguments are
the written proofs above; algebraic checks alone do not prove them.
