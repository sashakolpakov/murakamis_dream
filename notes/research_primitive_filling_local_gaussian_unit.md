# The local primitive-filling coefficient is an algebraic unit

Private written proof, 15 November 2026.

The original circle-tree source determines a particularly simple divisor
for its local primitive-charge Gaussian coefficient. On its regular
marked chart, that coefficient has no zero except a selected zero-angle
factor. This rules out all-order cancellation *inside that local Morse
block*. It does not identify the coefficient with which the original
finite source selects the block.

## 1. The original boundary source and the local chart

Let \(\mathcal T=(V,E)\) be an original ordered circle tree with at
least one edge, and let \(\varnothing\ne S\subseteq V\) be a set of
filled vertices. Write \(k=|S|\), let \(E_S\) contain every edge with
at least one endpoint in \(S\), and put \(m=|E_S|\). The set need
not be connected. For \(v\in S\), let \(d_v\) be its original
tree degree. For \(w\notin S\), put
\(d_S(w)=\#\{vw\in E:v\in S\}\).

Retain every original signed crossing power \(n_v\), including its
carrier. At complete main color and levels \(N\ge3\), define
\[
 K_N(t,u)=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u),
 \qquad \mathcal D_{n,N}f=\phi_N(R^nf).
 \tag{1}
\]
The exact boundary polynomial of the filled region is
\[
 Z_{S,N}(\mathbf u)=
 \left(\prod_{v\in S}\mathcal D_{n_v,N}^{(v)}\right)
 \prod_{e=vw\in E_S}K_N(t_v,t_w),
 \qquad t_w=u_w\quad(w\notin S).
 \tag{2}
\]
The raw product is reduced only by the actual vertex traces. In
particular (2) includes their first Hermite normals. It follows
directly by leaving the outside vertex factors open in the original
finite contraction \(\mathrm{cta:exact\text{-}source}\).

Use tangent and edge coordinates
\[
 a_v=\tan(t_v/2),\qquad q_e^2=1+a_v^2+a_w^2.
 \tag{3}
\]
Choose the component and continued logarithms marked at
\(a=0,q_e=1\). The regular open conditions used below are
\[
 1+a_v^2\ne0\quad(v\in V),\qquad
 q_e(q_e^2+1)\ne0\quad(e\in E_S).
 \tag{4}
\]
On the complete-parameter slice \(a_{V\setminus S}=0\), this is
the incident-edge restriction of the regular cover in
[the partial-boundary component note](research_partial_boundary_edge_cover_component.md).
One may instead fix regular outside angles and retain the same local
marked formulas. No arbitrary representation is asserted to admit
these coordinates.

Let \(\psi(t_v,t_w)\) be the original continued edge action and set
\[
 \begin{aligned}
 \Psi(\mathbf t,\mathbf u)&=\sum_{e\in E_S}\psi(t_v,t_w),\\
 F(\mathbf t,\mathbf u)&=\Psi(\mathbf t,\mathbf u)
       +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2-i\sum_{v\in S}t_v,\\
 r_{v,e}&=\frac12\log\frac{q_e+a_v}{q_e-a_v},\qquad
 \mathcal P_v=\sum_{e\ni v}r_{v,e}-\frac{i n_v}{2}t_v,\qquad
 J=\left(\frac{\partial\mathcal P_v}{\partial t_w}\right)_{v,w\in S}.
 \end{aligned}
 \tag{5}
\]
The logarithms are continued, not replaced by principal values at
the endpoint. The derivative identity \(\psi_{t_v}=-r_{v,e}/\pi\)
gives
\[
 F_{t_v}=-\frac{\mathcal P_v+\pi i}{\pi},\qquad
                         -F_{\mathbf t\mathbf t}=J/\pi.
 \tag{6}
\]
Thus the primitive filling equations are exactly the stationary
equations \(\mathcal P_v=-\pi i\). The selected Jacobian is the
actual primitive-period Jacobian, with the outside angles fixed.

## 2. Simplifying the original edge half-density

The canonical factorial interpolation of the original Newton sum has
wire phase \(B_e(x;t,u)=b(x,t)+b(x,u)\). Its branch at completeness
has \(x_*=1/4\). The original stationary equation is
\[
 \cos(2\pi x_*)=\frac{1-\cos t\cos u}{2+\cos t+\cos u}
                         =\frac{q_e^2-1}{q_e^2+1}.
 \tag{7}
\]
Consequently \(\cot(\pi x_*)=q_e\) on the marked logarithmic
lift. Write \(a=\tan(t/2)\), \(b=\tan(u/2)\), and \(q=q_e\).
Then
\[
 \sin^2(\pi x_*)=\frac1{1+q^2},\qquad
 -B_{e,xx}(x_*;t,u)
     =\frac{2\pi q(1+q^2)^2}{(1+a^2)(1+b^2)}.
 \tag{8}
\]
For the second equality, substitute (7) into the original formula
\[
 B_{e,xx}=-2\pi\sum_{\xi=t,u}
       \left\{\frac{\sin(2\pi x)}{\cos(2\pi x)+\cos\xi}
                                      +\cot(\pi x)\right\}.
\]
The two fractions become \(q(1+a^2)/(1+b^2)\) and its endpoint
interchange. Their sum with \(2q\) is
\(q(1+q^2)^2/((1+a^2)(1+b^2))\).

All quantities in (8) are nonzero on (4). The original sine factors
in the factorial interpolation are also nonzero there: at the saddle
their possible additional zeros are \(q\pm a=0\) or
\(q\pm b=0\), whereas
\((q-a)(q+a)=1+b^2\) and \((q-b)(q+b)=1+a^2\).
Thus its local formal Gaussian coefficients continue on the marked
logarithmic and half-density covers. This is continuation of formal
coefficients; it is not an extension of a finite-sum asymptotic domain.

The original leading edge coefficient is
\[
 \alpha_e=
 \frac{\sqrt{2\pi}}
      {4\sin^2(\pi x_*)\sqrt{-B_{e,xx}(x_*;t,u)}}.
\]
Its square therefore simplifies exactly to
\[
                \boxed{\alpha_e^2=
                     \frac{(1+a_v^2)(1+a_w^2)}{16q_e}.}
 \tag{9}
\]
The marked square root has \(\alpha_e(0,0)=1/4\). In particular
the edge coefficient is a unit on (4), without a positivity premise.

## 3. The full Hermite trace fixes the primitive-charge prefactor

Put \(\mathfrak q_N=e^{\pi i/N}\), \(\eta=(-1)^{N-1}\), and
\(C_{N,n}=\mathfrak q_N^{n(N-1)^2/4}\). The exact complete trace
for an arbitrary-degree even polynomial \(f(t)\) is
\[
 \mathcal D_{n,N}f=\eta C_{N,n}\sum_{j=0}^{N-1}g'(\tau_j),
 \quad g(t)=\sin t\,f(t)e^{inNt^2/(4\pi)},
 \quad \tau_j=\frac{\pi(N-1-2j)}N.
 \tag{10}
\]
After pairing the upper and lower horizontal sides, its exact lower
contour contribution is
\[
 -\frac{N^2C_{N,n}}{\pi i}
    \int g(t)W_N(t)\,dt,
 \qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}
       =\sum_{\ell\ge1}\ell\eta^{\ell-1}e^{-i\ell Nt}.
 \tag{11}
\]
The exact vertical endpoint current is retained separately in the
source identity. Formula (11) has unit coefficient for charge one
at both parities. It is the double-pole kernel of the full Hermite
trace, not an ordinary value-sampling trace.

Apply (11) in every selected variable of (2), and take the charge-one
term in each horizontal kernel. For its *local formal Gaussian
block* at a specified stationary point \(\mathbf t_*\), the wire
factors contribute \(N^{-3m/2}\prod_e\alpha_e\), and the angle
Gaussian contributes \((2\pi/N)^{k/2}/\sqrt{\det(-F'')}\).
Including all trace factors gives
\[
 \mathfrak G_{S,N}=
 \left(\prod_{v\in S}C_{N,n_v}\right)
 N^{3(k-m)/2}e^{NF(\mathbf t_*,\mathbf u)}
             \left(A_0+N^{-1}A_1+\cdots\right),
 \tag{12}
\]
where
\[
 A_0=\left(-\frac1{\pi i}\right)^k(2\pi)^{k/2}
       \frac{\prod_{e\in E_S}\alpha_e\,
                         \prod_{v\in S}\sin t_{*,v}}
            {\sqrt{\det[-F''(\mathbf t_*,\mathbf u)]}}.
 \tag{13}
\]
The square roots include the continued local contour orientation.
Equation (12) defines the local formal block; it is deliberately not
an asserted asymptotic expansion of \(Z_{S,N}\). When \(S\) is
connected with \(b\) boundary edges, \(m=k-1+b\), so the power
in (12) is \(-3(b-1)/2\), agreeing with the original boundary
source normalization.

The finite turn scalars and the final writhe factor remain those of
\(\mathrm{cta:exact\text{-}source}\). At complete main color the
edge factors \(H_N/W_j\), \(H_N\), and turn scalars equal one;
the remaining writhe and displayed \(C_{N,n_v}\) factors are nonzero
phases. None is absorbed by division by an unknown invariant.

## 4. The explicit local coefficient theorem

**Theorem.** Suppose a point on (4), with the retained logarithmic
marks, satisfies \(\mathcal P_v=-\pi i\) for all \(v\in S\),
\(\det J\ne0\), and \(a_v\ne0\) for every selected vertex.
The original local primitive-charge block (12) has nonzero leading
coefficient. More precisely,
\[
 \boxed{
 A_0^2=\frac{(-8)^k}{16^m}\,
 \frac{
  \displaystyle\prod_{v\in S}a_v^2(1+a_v^2)^{d_v-2}
  \displaystyle\prod_{w\notin S}(1+a_w^2)^{d_S(w)}
 }{
  \displaystyle\left(\prod_{e\in E_S}q_e\right)\det J
 }.}
 \tag{14}
\]
The square is a rational unit on that regular primitive critical
chart. The coefficient itself is a unit on its retained half-density
cover. No restriction on the sizes or signs of the fixed \(n_v\)
is required for this local statement.

**Proof.** Square (13), use (6), and retain the complex signs:
\[
 \left(-\frac1{\pi i}\right)^{2k}(2\pi)^k\pi^k=(-2)^k.
\]
Now substitute (9) and
\(\sin^2t_v=4a_v^2/(1+a_v^2)^2\). Each incident edge supplies
one factor \(1+a_v^2\) at its endpoint. The selected exponent is
therefore \(d_v-2\), and the outside exponent is \(d_S(w)\).
This gives (14). All its numerator and denominator factors are units
under the stated hypotheses, including when \(d_v=1\). \(\square\)

On a supplied positive geometric filling with the original core
condition \(\operatorname{Im}t_v<0\), the selected zero-angle
exclusion follows automatically. The theorem does not establish
that an arbitrary hyperbolic short filling admits this chart, a
positive decomposition, or the nonsingular Jacobian condition.

## 5. Formal exactness and the remaining source map

For clarity, at an isolated holomorphic Morse point the complete
local stationary series detects formal twisted exactness. Choose
local Morse coordinates with phase \(F_*-\sum y_i^2/2\), put
\(h=N^{-1}\), and include the coordinate Jacobian in a top density
\(f(y,h)\,dy\). The normalized Gaussian functional is
\[
 \mathcal E(f)=
   \left.\exp\left(\frac h2\sum_i\partial_{y_i}^2\right)
                       f(y,h)\right|_{y=0}.
 \tag{15}
\]
It is well defined coefficientwise for holomorphic germs formal in
\(h\). Integration by parts gives
\(\mathcal E((h\partial_{y_i}-y_i)b)=0\). Conversely, split the
constant coefficient of \(f\) as its value at zero plus
\(\sum_i y_i b_i\). Replacing \(y_i b_i\) by
\(h\partial_{y_i}b_i\) modulo these currents and repeating in
successive powers of \(h\) gives
\[
 \ker\mathcal E=
      \sum_i(h\partial_{y_i}-y_i)\mathcal O_y[[h]].
 \tag{16}
\]
Thus the local top twisted de Rham quotient is the rank-one
\(\mathbb C[[h]]\) module detected by (15). This statement is
formal; it asserts neither convergence of the current primitives
nor an equality of analytic global relative periods.

By (14), the local density in (12) has a nonzero class in this
quotient, already at leading order. Odd-moment cancellation cannot
annihilate its entire Gaussian series. The source's zero-charge
sector illustrates why the trace still matters: (10) is a total
derivative, so its zero Fourier mode has zero local stationary
series to every order. The factor \(\ell\) in (11) records exactly
this cancellation. A positive edge amplitude before taking the
trace does not remove it.

Finally, neither (14) nor (16) makes the original finite source a
faithful pairing on this local quotient. The selected source still
contains the wire lattice modes, all endpoint currents, the other
angular charges, the prescribed exterior, and its actual closing.
No source-compatible map identifying its geometric contribution
with (12) has been proved here. All-order vanishing of a *selected
scalar* therefore cannot be used to infer that this already nonzero
local class is exact. That inference would first need the missing
comparison with the original relative cycle. The explicit divisor
(14) separates the local question from that remaining comparison.

## Pinned sources and directly used statements

All derivations above are written algebra and formal Gaussian
reduction. No mathematical code or numerical experiment was used.

* `papers/circle-tree-volume/finite-bounds.tex`, SHA256
  `e4cf66544703af6d9a78208deae971c4d9f4367ba4b2ad660694ee489ef67ea1`:
  the full original vertex contraction, Newton pairing, physical
  turn factors, reduced cut, and final framing normalization.
* `papers/circle-tree-volume/edge-packet.tex`, SHA256
  `53eb6dbfbda3ca639db35911ed50947c29655840337f9d1f1ce909d435013dbb`:
  the canonical factorial interpolation, original wire stationary
  equation and curvature, calibrated edge action, and normalized
  leading edge coefficient. Its finite-sum domain is not enlarged.
* `notes/research_exact_complete_trace_contour.md`, SHA256
  `a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8`:
  the all-degree derivative trace, both-parity double-pole kernel,
  exact paired horizontal prefactor and retained endpoint current.
* `notes/research_partial_boundary_edge_cover_component.md`, SHA256
  `f3fdc37ee25b537680a96747ff40a746054b44ecb3bdd09f5fe246f5d29e762d`:
  the marked component and regular edge coordinates, literal
  peripheral multipliers, continued logarithmic primitive equations,
  and their rational selected Jacobian. Its limitations on inclusion,
  logarithmic continuation and cycle survival are retained here.
