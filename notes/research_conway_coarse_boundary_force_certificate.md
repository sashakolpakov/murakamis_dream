# Boundary-force certificates after eliminating connected Conway components

21 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

A connected component of the normalized Conway tree can be eliminated
before boundary forces are chosen. Its shifted boundary cost has the same
uniform curvature bounds as a single gate. Consequently the force dual
and its mismatch error estimate can be written using only the packets
on edges between components. There is no additional comparison factor,
and no internal matching condition has to be checked again.

The eliminated cost retains the actual complex tensors. It can be
negative. These results reduce the boundary data required of a geometric
construction; they do not determine the signed cost at those data or its
hyperbolic-volume rate.

## 1. The source and an arbitrary connected partition

Use the full normalized compiler of the
[gate-local source theorem](research_conway_gate_local_semidefinite_gluing.md)
and the [boundary-force theorem](research_conway_boundary_force_mismatch_certificate.md).
Each proper vertex has a packet in the complex Newton space \(H_N\),
of dimension \(N\). We use real coordinates and the inner product
\(u\cdot v=\operatorname{Re}(u^*v)\). Every repeated-root coordinate
is retained.

Put \(\sigma=1/16\) and \(t=1/4\). Each prescribed leaf, linear map,
bilinear map \(\Phi_v\), and the original closing row \(L\), has
its recorded Hilbert--Schmidt norm at most \(\sigma\). On the product
of packet unit balls the original energy is
\[
 E(x)=\sum_{v\ne\rho}\|\Phi_v((x_c)_c)-x_v\|^2
                                      +|Lx_{v_0}|^2,
 \qquad e_*=\min E.                                      \tag{1}
\]
Here \(\rho\) is the closing root and \(v_0\) its one child.
The original marked scalar satisfies
\[
 B_{\rm tot}^2e_*\le |K_N|^2
          \le\gamma B_{\rm tot}^2e_*,\qquad \gamma=197/196. \tag{2}
\]
All original phases and the known budget product \(B_{\rm tot}\)
remain unchanged.

The redistributed potentials are
\[
 \begin{split}
 V_v&=\|\Phi_v-x_v\|^2-t\|x_v\|^2
                                  +t\sum_{c\text{ child}}\|x_c\|^2,
                                      &&v\ne\rho,\\
 V_\rho&=|Lx_{v_0}|^2+t\|x_{v_0}\|^2.
 \end{split}                                                \tag{3}
\]
They sum to \(E\) on consistent fields. The pointwise local Hessian
bounds proved in the boundary-force theorem are
\[
                 \mu I\le D^2V_v\le4I,\qquad \mu=45/128.   \tag{4}
\]

Partition all vertices, including \(\rho\), into nonempty connected
components \(\Omega\). A proper component has one top output packet
\(y\) and one input packet \(u_j\) for each child edge entering from
another component. Its boundary list is \(b_\Omega=(u,y)\).
The component containing \(\rho\) has just its entering input packets;
the physical scalar output remains fixed at zero. Every boundary
packet lies in its unit ball.

Define
\[
 W_\Omega(b)=\min_{\text{internal packet balls}}
                                  \sum_{v\in\Omega}V_v.  \tag{5}
\]
For a proper component, if \(C_\Omega(u,y)\) denotes its unshifted
residual minimum, internal quadratic terms cancel to give
\[
 W_\Omega(u,y)=C_\Omega(u,y)
                           +t\sum_j\|u_j\|^2-t\|y\|^2.   \tag{6}
\]
For the root component there is no negative outgoing term. Formula (5)
is used in both cases. In particular, the shifted costs need not be
nonnegative.

After this elimination each cut edge has two retained copies of its
packet: the child component's output and the parent component's input.
Let \(b\) list all these copies and define the consistency map
\[
                    (Bb)_v=b_{\mathrm{parent},v}
                                      -b_{\mathrm{child},v}. \tag{7}
\]
Different cut edges have disjoint copy coordinates. Therefore
\[
                                  BB^*=2I.               \tag{8}
\]
Exact partial minimization gives
\[
                  e_*=\min_{Bb=0}\sum_\Omega W_\Omega(b_\Omega),
                                                               \tag{9}
\]
with all boundary balls still imposed. This is an identity, without
the comparison loss of an approximate compressed residual.

## 2. Uniform curvature of the boundary cost

**Theorem 1.** Each \(W_\Omega\) is smooth on a neighborhood of its
closed boundary product of balls and, on that product,
\[
                      \mu I\le D^2W_\Omega\le4I.          \tag{10}
\]
The constants do not depend on the level, the component size, its
number of boundary legs, or its fixed short filling coefficients after
their original budgets have been retained.

**Proof.** The internal quadratic shifts in (3) cancel. For fixed
boundary data, the internal minimizer is therefore the same as for
the unshifted residual problem. The
[connected-block theorem](research_connected_conway_block_boundary_energy.md)
proves it is unique and interior, with every internal packet bounded
by \(33/256\). It includes a component containing the closing root,
whose scalar output is fixed at zero. Its half-gradient formula uses
only the original maps and their norm bound \(\sigma\).

Let \(z\) list internal variables and let
\(H=D^2\sum_{v\in\Omega}V_v\), evaluated at the minimizer.
Every variable occurs in at least one local bag. Thus (4) gives
\(H\ge\mu I\). The real implicit function theorem applies to
the internal stationary equations. The strict interior margin permits
a local extension when some clamped boundary packet is on its sphere.
Uniqueness makes these extensions agree. With no internal variables
this step is unnecessary.

Writing subscripts for the boundary and internal Hessian blocks,
\[
 D^2W_\Omega=H_{bb}-H_{bz}H_{zz}^{-1}H_{zb}.            \tag{11}
\]
For a boundary variation \(h\), set
\(q=-H_{zz}^{-1}H_{zb}h\). Then
\[
 h^{\mathsf T}D^2W_\Omega h
       =(q,h)^{\mathsf T}H(q,h)\ge\mu\|h\|^2.
\]
The same formula gives \(D^2W_\Omega\le H_{bb}\).
Each retained boundary packet occurs in exactly one bag inside this
component. Applying the upper bound (4) to a variation with all
internal coordinates zero consequently gives
\(h^{\mathsf T}H_{bb}h\le4\|h\|^2\). There is no component-size
factor: the boundary occurrences in different bags are disjoint.
This proves (10). \(\square\)

For clarity, the inverse-Hessian formula for a convex conjugate is
used below only where its maximizing packet is interior. Extending
\(W_\Omega\) by \(+\infty\) outside its boundary balls does not
give an unrestricted smooth inverse gradient on every possible force.

## 3. Forces only on the cut packets

Choose one real force \(p_v\in H_N\) on each cut edge and impose
\[
                       \|p_v\|\le1/3.                    \tag{12}
\]
For a proper component set
\[
 F_\Omega(b;p)=W_\Omega(b)-p_{\rm out}\cdot y
                                  +\sum_jp_j\cdot u_j.   \tag{13}
\]
For the root component keep only its input-force terms. Together these
affine terms are \(p\cdot Bb\).

Every \(F_\Omega\) has a unique interior boundary minimizer
\(b_\Omega(p)\). To check interiority without any assumption about
the compressed function, minimize the fine expression
\(\sum_{v\in\Omega}V_v\) with these boundary forces. At a packet of norm
one, the outward radial derivatives have the following lower bounds:
\[
 \begin{array}{c|c}
 \text{occurrence in the component}&\text{lower bound}\\ \hline
 \text{proper top output}&2(1-t)-2\sigma-1/3>0\\
 \text{cut input}&2t-2\sigma(1+\sigma)-1/3=13/384>0\\
 \text{internal output with a proper parent}
                 &2-2\sigma-2\sigma(1+\sigma)>0\\
 \text{internal output whose parent is the root}&2-2\sigma>0.
 \end{array}                                                \tag{14}
\]
The internal shifts cancel in the last two rows. At the root the
closing contribution to that radial derivative is \(2|Lx|^2\ge0\).
If the root component is the singleton root, its input bound improves
to \(2t-1/3=1/6\). The inequalities follow from
\(\|\Phi_v\|\le\sigma\), \(\|D_c\Phi_v\|\le\sigma\), and
\(\|\Phi_v-x_v\|\le1+\sigma\). Thus a boundary minimizer cannot
have a packet on its sphere. The same bounds persist on a neighborhood
of the closed force box. Theorem 1 now makes the boundary minimizers
smooth functions of these forces.

Define their signed total value and their cut mismatch by
\[
 d_{\mathcal P}(p)=\sum_\Omega F_\Omega(b_\Omega(p);p),
 \qquad m_{\mathcal P}(p)=B b(p).                         \tag{15}
\]
The symbol \(\mathcal P\) denotes the connected partition, not a
new polynomial. Individual minima in this sum can be negative.

Equivalently, with the boundary-ball convention for the conjugate,
\[
 W_\Omega^*(s)=\sup_{b_\Omega}
                         \{s\cdot b_\Omega-W_\Omega(b_\Omega)\},
 \qquad d_{\mathcal P}(p)
           =-\sum_\Omega W_\Omega^*(-(B^*p)_\Omega).     \tag{16}
\]
These conjugates use only the original connected components and their
full cut boundary packets. They do not insert an unknown global source
value as data.

**Theorem 2.** On (12),
\[
 \nabla d_{\mathcal P}=m_{\mathcal P},\qquad
             \tfrac12I\le-D^2d_{\mathcal P}\le\tfrac{256}{45}I,
                                                               \tag{17}
\]
and
\[
             \max_{p\text{ satisfying }(12)}d_{\mathcal P}(p)=e_*.
                                                               \tag{18}
\]
The maximum is attained in the interior of the force box.

**Proof.** Differentiate the independent stationary boundary equations.
Writing \(H_{\partial}\) for the block diagonal matrix with blocks
\(D^2W_\Omega(b_\Omega(p))\), the result is
\[
                  -D^2d_{\mathcal P}=BH_{\partial}^{-1}B^*.
\]
Equations (8) and (10) give (17). Weak duality gives
\(d_{\mathcal P}\le e_*\), since all forces cancel at a consistent
field in (9).

To prove attainment, let \(a_*\) be the original unique interior
minimizer of (1). Retain on the cut edges the fine optimal forces
\[
 p_v^*=\partial_{x_v}V_v(a_*)
                   =\tfrac32a_{*,v}-2\Phi_v((a_{*,c})_c). \tag{19}
\]
The boundary-force theorem proves
\(\|a_{*,v}\|\le33/256\) and hence
\(\|p_v^*\|\le163/512<1/3\).
For the corresponding fine forces on every edge, each adjusted gate
has zero gradient at \(a_*\). Summing those adjusted gates inside a
component cancels every internal force. Its unique block minimum is
therefore attained at the restriction of \(a_*\). Thus the retained
boundary copies agree, the signed values sum to \(e_*\), and (18)
holds. \(\square\)

## 4. A certificate involving only the boundary disagreement

At the minimizers in (15), average the two copies of each cut packet:
\[
                 \bar b=b(p)-\tfrac12B^*m_{\mathcal P}(p).
                                                               \tag{20}
\]
The copies now agree, remain in their unit balls, and obey
\(\|\bar b-b(p)\|^2=\|m_{\mathcal P}(p)\|^2/2\).
The adjusted boundary gradients vanish. Taylor's upper bound from
(10) therefore gives
\[
 e_*\le\sum_\Omega F_\Omega(\bar b_\Omega;p)
                \le d_{\mathcal P}(p)+\|m_{\mathcal P}(p)\|^2.
\]
The first inequality follows by assembling the exact internal
minimizers at the now-consistent boundary packets. Their shifts and
forces cancel. Consequently
\[
 \boxed{\quad d_{\mathcal P}(p)\le e_*
                \le d_{\mathcal P}(p)+\|m_{\mathcal P}(p)\|^2,\quad}
                                                               \tag{21}
\]
\[
 B_{\rm tot}^2\max(0,d_{\mathcal P}(p))\le |K_N|^2
       \le\gamma B_{\rm tot}^2
                  \{d_{\mathcal P}(p)+\|m_{\mathcal P}(p)\|^2\}.
                                                               \tag{22}
\]
These constants are the same as for single-gate forces. No mismatch
inside an eliminated component appears in (21).

If the entire tree is one component, its boundary is empty:
\(W=e_*\), \(d=e_*\), and \(m=0\). The matrix inequalities then
concern the zero-dimensional space. At the other extreme, singleton
components recover the fine boundary-force theorem, including the
singleton closing root. These limiting cases do not change the source.

## 5. A coherent-force normalization check

Take the root as a singleton and partition the proper vertices
arbitrarily. Let \(a\) be the exact forward normalized quantum field,
so \(a_v=\Phi_v((a_c)_c)\), and put \(k=La_{v_0}=K_N/B_{\rm tot}\).
Choose the cut forces \(p_v=-2t a_v\); they satisfy (12).
At these coherent fields all proper residuals vanish. In each proper
component the derivatives of its boundary norm shifts are exactly
canceled by these forces. Its minimizer is therefore its restriction
of \(a\), and its value is
\(t\|a_{\rm out}\|^2-t\sum_j\|a_{{\rm in},j}\|^2\).
Summing all proper components leaves \(t\|a_{v_0}\|^2\).

The remaining root minimum is the elementary quadratic problem
\[
 \min_x\{|Lx|^2+t\|x\|^2-2t\operatorname{Re}(a_{v_0}^*x)\}.
\]
Its minimizer is \(t(tI+L^*L)^{-1}a_{v_0}\), whose norm is at
most \(\|a_{v_0}\|\le\sigma\). The rank-one identity for the row
\(L\) gives the exact signed value
\[
                 d_{\mathcal P}(p)
                      =\frac{t}{t+\|L\|^2}|k|^2.          \tag{23}
\]
This check exhibits no new volume estimate. The exact coherent
boundary forces already contain the full forward quantum packets,
including the unknown scalar closing coefficient. It shows why
uniformly conditioned elimination does not by itself determine that
coefficient's rate.

## 6. What the compression changes

A fixed short connected component can now be eliminated once. To
apply (22), a geometric construction needs forces and packet
disagreements only on its actual cut legs, rather than trial fields,
forces, or matching estimates at every internal gate. All coordinates
of those cut packets, including the Hermite coordinates, are still
present. The functions \(W_\Omega\) can cease to be polynomials;
their original fine degree-four semidefinite lifts remain exact by the
gate-local theorem.

The missing input remains a positive signed \(d_{\mathcal P}\) at
the required hyperbolic-volume rate, with a subexponential relative
cost from the mismatch term. The sum in (15) must not be replaced by
the sum of its positive parts. From (17), force errors around the
maximizer satisfy
\[
 \tfrac14\|p-p^*\|^2\le e_*-d_{\mathcal P}(p)
                          \le\tfrac{128}{45}\|p-p^*\|^2.
\]
Thus an exponentially small normalized source still requires its
square-root scale of force accuracy for a positive lower certificate.
No Casson--Rivin construction of such full quantum boundary data is
proved here, and no new short-filling volume identity follows.

## Complete direct proof sources

All three complete matching sources were read before this note was
written:

| Source | SHA-256 |
|---|---|
| [Connected block boundary energy](research_connected_conway_block_boundary_energy.md) | 426b0eba0c7f4c502cf2b82052daf4d5a224ad8ec8419b3e2d8a624771f192ae |
| [Gate-local convex gluing](research_conway_gate_local_semidefinite_gluing.md) | 8b3241f9cc8a9e740aa4223345e39932f3a2096fcdab60f55458a6266857e8e9 |
| [Boundary forces and mismatch](research_conway_boundary_force_mismatch_certificate.md) | 73abcefd56c536e4d5ba93003b2f8515fe7380c6a290aec055603b54aa13f359 |

Only written mathematics and text/hash operations were used. No
mathematical program, numerical optimization, test, build, git operation,
or edit to a previous final was performed.
