# Boundary energy of a connected Conway block

21 November 2026. A connected collection of short pieces can be removed
from the normalized Conway energy while retaining its exact full boundary
map. This note proves a pointwise comparison, before the remaining
boundary packets are optimized. The comparison factor is uniform in the
level, the block size, and the chosen fixed filling coefficients.

The boundary map itself remains coherent and marked. The theorem does
not replace it by an operator norm or prove that its geometric closing
coefficient is nonzero.

## 1. A block with clamped input and output packets

Use the complete boundary spaces, original markings and normalized local
maps of the
[convex source theorem](research_convex_normalized_conway_source.md).
Thus every leaf and linear or bilinear map has norm at most
\(\sigma=1/16\). The per-vertex budgets and their original product
\(B_{\rm tot}\) are retained. In particular a normalized product is
the actual full Newton multiplication divided by its known local budget.
All budgets are held fixed while boundary packets vary. No repeated-root
derivative is discarded.

Let \(\Omega\) be a nonempty connected set of vertices in the rooted
compiler tree. It has one top vertex \(\omega\), with one outgoing
boundary leg. Every child leg entering \(\Omega\) from below is a cut
input leg. Write its clamped packet as \(u_j\), and assume
\(\|u_j\|\le1\). Inputs may also be prescribed normalized leaf packets.

Clamp the top output to a packet \(y\), with \(\|y\|\le1\), in the
top output Hilbert space. All other packets \(z_v\), for
\(v\in\Omega\setminus\{\omega\}\), are internal variables in their
unit balls. In each local recursion put \(x_\omega=y\), \(x_v=z_v\)
at internal vertices, and use \(u_j\) at cut inputs. Define
\[
 S_\Omega(z;u,y)
    =\sum_{v\in\Omega}\|\Phi_v((x_c)_c)-x_v\|^2,\qquad
 C_\Omega(u,y)=\min_{\|z_v\|\le1}S_\Omega(z;u,y).        \tag{1}
\]
When there are no internal variables, this is the displayed local
squared residual itself.

The block may contain the physical closing root. In that case its
normalized local map is the original row \(L\), its output space is
\(\mathbb C\), and its clamped output is \(y=0\). The root residual
is then \(|Lx_{v_0}|^2\), exactly as in the original energy.
For the estimates below one can also let this scalar \(y\) vary over
its unit disk.

Let \(F_\Omega(u)\) be the exact normalized composite obtained by
performing the recursions inside \(\Omega\). It retains every original
phase and all cut boundary coordinates. Since the cut inputs have norm
at most one, every exact internal packet and \(F_\Omega(u)\) have
norm at most \(\sigma\).

## 2. Internal elimination and the output Hessian

**Theorem.** For each fixed clamped input \(u\), the internal minimum in
(1) exists uniquely and is interior. The boundary value is smooth in
the real and imaginary output coordinates, with
\[
             \frac{63}{32}I\le D_y^2C_\Omega(u,y)\le2I. \tag{2}
\]
Consequently, with \(c=63/64\),
\[
 \boxed{\quad
 c\|y-F_\Omega(u)\|^2\le C_\Omega(u,y)
                          \le\|y-F_\Omega(u)\|^2.
 \quad}                                                \tag{3}
\]
All constants are independent of \(N\), the number of block vertices,
and the filling coefficients after the stated budgets are retained.

**Proof.** First let every vertex output in \(\Omega\), including the
top output, vary in its unit ball, while the cut inputs remain fixed.
The residual Jacobian is \(-I+A\). Each child block has norm at most
\(\sigma\), each row has at most two such blocks, and each child appears
in at most one parent row. Hence \(\|A\|\le\sqrt2\sigma\le1/8\).
The half-Hessian residual-curvature term is bounded in absolute value by
\(\sigma(1+\sigma)\) times the squared variation norm: at a product
it is
\[
 2\operatorname{Re}\langle\mathcal R_v,
                                      \Phi_v(\xi_L,\xi_R)\rangle,
\]
and distinct parents have disjoint sibling pairs. This gives
\[
                     I\le D^2S_\Omega\le3I             \tag{4}
\]
on these balls, by the same bounds
\(2[(7/8)^2-1/8]>1\) and \(2[(9/8)^2+1/8]<3\).
Clamping \(y\) retains (4) on the internal variables.

At an internal vertex the half-gradient step for those variables is
\[
 z_v-\tfrac12(\nabla_z S_\Omega)_v
       =\Phi_v-(D_v\Phi_{\operatorname{parent}(v)})^*
                                     \mathcal R_{\operatorname{parent}(v)}.
\]
Every internal vertex has its parent in \(\Omega\). This step has
component norm at most
\(\sigma+\sigma(1+\sigma)=33/256<1\), including when that parent
is the clamped top. By (4) it is a contraction with factor \(1/2\).
Its unique fixed point is the unique internal minimizer and is interior.
The statement is immediate if there are no internal variables.

At this interior minimum the internal Hessian block \(H_{zz}\) is
positive definite, with \(H_{zz}\ge I\). The real implicit function
theorem applied to \(\nabla_zS_\Omega=0\) therefore gives a smooth
minimizer as the parameters \((u,y)\) vary. The interior margin also
gives a local extension at points where an input or output is on its
unit sphere. Differentiating the stationary equations gives
\[
 D_y^2C_\Omega
                  =H_{yy}-H_{yz}H_{zz}^{-1}H_{zy}.     \tag{5}
\]
The top variable appears only as minus its identity in the top residual,
so \(H_{yy}=2I\). Moreover
\[
 H_{yz}=-2D_z\Phi_\omega,\qquad
 \|H_{yz}\|\le2\sqrt2\sigma.
\]
Only the internal children of the top occur in this row. There are at
most two, and their derivative blocks have norm at most \(\sigma\).
Thus \(\|H_{yz}\|^2\le8\sigma^2=1/32\). Formula (5) and
\(H_{zz}^{-1}\le I\) prove (2). With no internal variables,
the Hessian is exactly \(2I\).

At \(y=F_\Omega(u)\), the exact recursion gives zero cost. The first
output derivative is therefore zero there. The segment from this point
to any allowed \(y\) stays in the unit ball. Integrating (2) twice
along that segment proves (3). \(\square\)

The output derivative has the concrete boundary-flux formula
\[
 \nabla_y C_\Omega(u,y)
      =2\{y-\Phi_\omega(z_*(u,y),u)\}.                 \tag{6}
\]
Its half differs from \(y-F_\Omega(u)\) by at most
\(\|y-F_\Omega(u)\|/64\), by integrating (2) once.
Only output convexity, with the inputs clamped, has been asserted.

Joint convexity in the cut inputs is false. For example, the actual
Newton algebra has \(M(b_0,b_0)=b_0\). A single product vertex on the
real input lines \(u_1=\alpha b_0\), \(u_2=\beta b_0\), with fixed
output \(y=t b_0\), has energy
\[
                           |a\alpha\beta-t|^2,
 \qquad a=1/b_\omega>0,\quad 0<t\le1.
\]
At \(\alpha=\beta=0\) its real input Hessian has off-diagonal entries
\(-2at\) and zero diagonal entries. It is indefinite.

## 3. Exact linear corridors

When the clamped block is a chain of normalized linear maps \(A_i\),
the boundary energy has an explicit formula. This includes turns and
multiplication by a fixed retained packet, with every full Newton
coordinate present. Suppose
\[
 x_0=u,\quad x_L=y,\qquad
 S=\sum_{i=1}^L\|x_i-A_ix_{i-1}\|^2,\qquad \|A_i\|\le\sigma.
\]
Put
\[
 P_i=A_LA_{L-1}\cdots A_{i+1},\quad P_L=I,\qquad
 W=\sum_{i=1}^LP_iP_i^*.
\]
Then
\[
 C(u,y)=\langle y-A_L\cdots A_1u,\,
                         W^{-1}(y-A_L\cdots A_1u)\rangle.       \tag{7}
\]
Indeed the errors \(r_i=x_i-A_ix_{i-1}\) satisfy
\(y-A_L\cdots A_1u=\sum_iP_ir_i\). The map on the right is
surjective because \(P_L=I\). Its least-norm solution is
\(r_i=P_i^*W^{-1}(y-A_L\cdots A_1u)\), as follows by orthogonality
to its kernel. This proves (7) without ball constraints. The internal
minimum with balls is interior by the preceding theorem. It satisfies
the same strictly convex quadratic stationary equations, so it is also
the unconstrained minimum and (7) is valid with the original balls.

In particular
\[
                  I\le W\le\frac{256}{255}I,\qquad
                  \frac{255}{256}I\le W^{-1}\le I.     \tag{8}
\]
These follow from \(\|P_i\|\le\sigma^{L-i}\) and a geometric series.
No inverse of an individual \(A_i\) is used; the maps can be singular.
The metric estimate concerns the residual from the exact transported
center. It is not a lower bound on the norm of that center.

## 4. Several short blocks in the original source

Choose any collection of pairwise vertex-disjoint connected blocks.
Retain every block output and every cut input as boundary variables,
except for the physical root output, which is fixed at zero if present.
Eliminate all other variables inside the blocks. Original local terms
outside the blocks remain in a nonnegative function \(A\).
For fixed remaining boundary packets, exact elimination gives
\[
                    E_{\rm red}=A+\sum_jC_{\Omega_j}(u_j,y_j).
\]
There is no remaining coupling through an eliminated variable: a vertex
outside a connected block can see only that block's retained top output.
Define the compressed residual energy
\[
                    E_{\rm comp}
                       =A+\sum_j\|y_j-F_{\Omega_j}(u_j)\|^2.     \tag{9}
\]
Each composite map uses the same normalized gates as before. In
particular \(B_{\rm tot}\) is unchanged; no new budget is silently
assigned to a fused map.

Equation (3), together with \(A\ge0\), gives the pointwise inequalities
\[
                       cE_{\rm comp}\le E_{\rm red}\le E_{\rm comp}.
\]
Taking minima over all remaining unit-ball variables proves
\[
             c\min E_{\rm comp}\le\min E_N\le\min E_{\rm comp}.  \tag{10}
\]
The factor \(c\) occurs once, independently of the number of blocks,
because the energies add. No joint input convexity or convexity of
\(E_{\rm comp}\) is used in this argument.

Let \(\gamma=197/196\) be the source constant from the convex theorem.
Its original scalar comparison and (10) imply
\[
 \boxed{\quad
 cB_{\rm tot}^2\min E_{\rm comp}\le|K_N|^2
                      \le\gamma B_{\rm tot}^2\min E_{\rm comp}.
 \quad}                                                        \tag{11}
\]
Thus absorbing any such collection of fixed short pieces preserves the
original exponential rate with a constant loss independent of their
number. This is a boundary comparison before the final minimization,
not a replacement of the marked invariant by a norm of individual pieces.

## 5. What this removes, and what remains

The internal energy of an arbitrary connected short block is comparable
to its exact boundary residual with uniform constants. This removes
an internal metric or assembly loss as a separate exponential obstacle.
The fixed filling coefficients can enter the known per-gate budgets and
the exact composite maps; all of those factors remain in (11).

What remains is the asymptotic behavior of the compressed source with
those actual coherent maps. The estimates do not supply a subexponential
bound on an inverse map. Neither (3) nor (11) establishes the map's value
on a geometric boundary field or a nonzero marked closing coefficient. A geometric lower
certificate for the remaining boundary problem is still required for
the finite-exception volume theorem.

## Complete direct source

The sole direct proof source was read in full at the matching pin:

| Source | SHA-256 |
|---|---|
| [Unweighted convex Conway source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

The clamped boundary problem, Schur estimate, corridor formula and
assembly inequalities are proved above. Only written mathematics and
text operations were used. No mathematical program, test, build,
numerical iteration, git operation or previous-final edit was performed.
