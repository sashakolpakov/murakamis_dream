# Isolated zero-power vertices and a larger positive angular chart

1 November 2026. Private geometric result. The assertion concerns
the actual metric and its primitive filling periods. It makes no
claim about dominance in the finite quantum sum.

## 1. The partial filling

Fix the original ordered all-circle tree and its labeled octahedral
decomposition. Choose an independent set \(Z\) of vertices: no edge
has both endpoints in \(Z\). Suppose each \(v\in Z\) has degree
\(D_v\ge3\), and set its physical power to zero, with
\(\epsilon_v=p_v=0\). Initially leave every other auxiliary circle
unfilled.

For \(0\le c\le1\), define
\[
 \varphi_v=\frac{\pi c}{D_v},\qquad
 \alpha_v=\operatorname{artanh}(\sin\varphi_v),\qquad
 \tau_v=-2i\alpha_v\quad(v\in Z),\qquad
 \tau_w=0\quad(w\notin Z).
 \tag{1}
\]
Every nonzero endpoint in an edge block therefore has a zero
parameter at its other endpoint. The edge response is
\[
 F(t,u)=-2\pi\psi_t(t,u)
       =2\operatorname{arsinh}(\tan(t/2)\cos(u/2)).
 \tag{2}
\]
On the branches continued from zero,
\[
 F(-2i\alpha,0)
 =-2i\arcsin(\tanh\alpha)=-2i\varphi.
 \tag{3}
\]
Thus \(\Psi_v=ic\) at a vertex in \(Z\), exactly the charge
equation for its zero power. At an unfilled vertex \(w\), separate
evenness in the first angular variable gives \(\Psi_w=0\).
Consequently \(U_w=V_w=0\) there.

## 2. All eight tetrahedra remain positive

Write
\[
 S=\tanh\alpha=\sin\varphi,\qquad
 C=\operatorname{sech}\alpha=\cos\varphi>0.
 \tag{4}
\]
In the exact two-ended chart with parameters \((-2i\alpha,0)\),
the wire and disk parameters become
\[
 k=C^{-1},\quad
 E=\frac{C+i}{C-i},\quad
 H_0=\frac{C+iS}{C-iS},\quad H_1=1,\quad
 R=\frac1{1+C^2}.
 \tag{5}
\]
The two apices in the first copy, and those in the second copy, are
\[
 A_+=\frac{C-iS}{C-i},\quad B_+=\frac1{1+iC},
 \qquad
 A_-=\frac{C-iS}{C+i},\quad B_-=\frac1{1-iC}.
 \tag{6}
\]
These are substitutions into the actual cross-copy chart
\(C_R\circ T_{1-R}\); using the quarter-turn alone would not give
these apices.

Substitution of (5)--(6) in the four oriented tetrahedral cross
ratios gives, in the first copy,
\[
 S+iC,\qquad \frac{iC}{1-S}=ie^\alpha,\qquad
 -S+iC,\qquad \frac{iC}{1+S}=ie^{-\alpha}.
 \tag{7}
\]
In the second copy the first and third entries are exchanged and
the other two are unchanged. The second-copy tetrahedra use their
prescribed reversed vertex order. Equations (7) can also be checked
as rational identities by putting
\(S=2r/(1+r^2)\), \(C=(1-r^2)/(1+r^2)\).

All eight shapes have positive imaginary part whenever
\(0\le\varphi<\pi/2\). Here
\(\varphi\le\pi/3\), so
\[
 C\ge\frac12,\qquad
 e^{-\alpha}\ge2-\sqrt3,\qquad
 \Im z_j\ge2-\sqrt3>0.
 \tag{8}
\]
This is a uniform positive margin for the whole closed path.
The nonzero angular parameter can reach
\(2\operatorname{artanh}(\sqrt3/2)\), well outside the small
radius \(10^{-2}\) used by the vertexwise criterion.

## 3. Actual gluing and primitive completion

The ordered page decomposition and all its three-point face maps
are unchanged. The local maps are rational in the displayed
parameters, and (5)--(8) encounter neither a degenerate tetrahedron
nor a zero denominator. The disk-side shape ratios agree on the
same continued branches. Thus the cells glue in the original
marked exterior along the whole path.

At each \(v\in Z\), the original periods are
\[
 U_v=-2\pi\Psi_v=-2\pi ic,\qquad
 V_v=2i\tau_v=4\alpha_v>0.
 \tag{9}
\]
The original small-charge limit fixes these as actual logarithmic
periods, not only as eigenvalue logarithms modulo \(2\pi i\).
Indeed the second fixed point escapes the fixed developed
generator paths as \(c\downarrow0\); their logarithmic increments
tend to zero. Their continuous integral differences from (9)
therefore vanish along the path. The same argument used in the
positive completion theorem gives a cone angle \(2\pi c\) at this
core and a smooth solid torus at \(c=1\).

The remaining auxiliary cusps have zero periods and remain complete.
The main cusp is also complete. The endpoint is therefore the
actual partially filled finite-volume hyperbolic exterior, with all
vertices in \(Z\) filled on their original meridian slopes.

## 4. Independently long fillings at every other vertex

For this fixed tree and fixed independent set \(Z\), the partial
path persists when the other powers are independently sufficiently
large in absolute value. Put \(r_w=1/n_w\), \(w\notin Z\), and
write the equations as
\[
 \Psi_v(\boldsymbol\tau)=ic\quad(v\in Z),
 \qquad
 r_w\Psi_w(\boldsymbol\tau)+\frac{i}{2\pi}\tau_w=icr_w
       \quad(w\notin Z).
 \tag{10}
\]
At \(\mathbf r=0\), (1) solves this system. Every mixed derivative
joining \(Z\) to its complement vanishes, since
\(\psi_{tu}\) has the factor \(\sin(t/2)\sin(u/2)\).
The Jacobian of (10) is block diagonal, with entries
\[
 -\frac{D_v\cos\varphi_v}{2\pi}\quad(v\in Z),
 \qquad \frac{i}{2\pi}\quad(w\notin Z).
 \tag{11}
\]
They are uniformly nonzero on \(0\le c\le1\). The holomorphic
implicit function theorem, followed over this compact interval,
therefore gives one positive reciprocal-polydisk in all the
\(r_w\). The selected solution is holomorphic there and along a
neighborhood of the charge interval. By (8) and continuity all
tetrahedra remain positive after shrinking this polydisk.

The required lower-half-plane sign for the formerly unfilled
vertices needs an additional argument. Define the holomorphic
quotient
\[
 B_v(\boldsymbol\tau)=
 \sum_{w\sim v}\frac{F(\tau_v,\tau_w)}{\tau_v},
 \tag{12}
\]
using its removable value at \(\tau_v=0\). At a vertex in \(Z\),
its base value is \(D_v\varphi_v/\alpha_v\ge D_v/2\).
At every other vertex it is
\(\sum_{w\sim v}\cosh\alpha_w\), with \(\alpha_w=0\) off \(Z\);
this lies in \([d_v,2d_v]\). These inequalities also hold at
\(c=0\) by their limits.

After one more uniform shrinking, \(\Re B_v>0\) for every vertex
and every real \(c\in[0,1]\). For real powers, (10) implies
\[
 \tau_v=-\frac{2\pi ic}{B_v-in_v},
 \qquad
 \Im\tau_v=-\frac{2\pi c\,\Re B_v}{|B_v-in_v|^2}<0
       \quad(c>0).
 \tag{13}
\]
Thus the full path has positive core lengths. Its original
peripheral periods satisfy
\(U_v+p_vV_v=-2\pi ic\), including at the zero-power vertices.
All auxiliary fillings are smooth at \(c=1\).

There is consequently a finite threshold \(B(\mathcal T,Z)\)
such that every independently chosen signed integer tuple with
\(n_v=0\) on \(Z\) and \(|n_w|>B(\mathcal T,Z)\) elsewhere gives
this geometric completion. The original parity and knot-component
test is still required for a knot-complement statement. No ratio
between the nonzero powers is restricted.

## 5. Scope

The marked action is calibrated by the same primitive-period and
Schläfli argument along this positive path. This gives an actual
geometric target, but no finite-source lower bound or volume-limit
claim has been established here.

A zero box can sometimes be deleted or interpreted as an unmarked
product junction in an earlier presentation. The metric result is
therefore not claimed to produce new knot types. Its precise
content is an explicit positive cell path, outside the small-angle
chart, and its persistence under independent long fillings at the
other vertices.
