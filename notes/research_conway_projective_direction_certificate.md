# A projective-line source certificate and scalar amplitude refinement

22 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

Suppose one supplies a complex line in the full packet space at every
proper vertex of the normalized Conway tree. Orthogonally projecting
each gate output onto its supplied line gives an explicit trial:
its closing is a product of local complex overlaps, and its residual
norm is a sum of local directional leakages. A source-relative bound
then needs no minimization.

There is an optional refinement. All scalar packet phases can be
optimized by one tree pass, and the amplitudes solve a strongly
convex real quartic with one scalar variable per proper vertex.
The remaining full-gradient certificate is entirely transverse.
Neither construction supplies the directions, their required
relative error, or their geometric rate.

## 1. The original source and supplied directions

Use the complete normalized source of the
[convex source theorem](research_convex_normalized_conway_source.md).
Let \(V\) be its proper vertices, \(v_0\) its top proper vertex,
and \(s=|V|\). Each packet belongs to the full Newton space
\(H_N\cong\mathbb C^N\), retaining the value and first-derivative
coordinates at its repeated roots.
The maps \(\Phi_v\) are prescribed constants at leaves, complex
linear at turns, and complex bilinear at products. The original
normalized closing is \(L\), and
\[
 E(x)=\sum_{v\in V}\|\Phi_v((x_c)_c)-x_v\|^2
                           +|Lx_{v_0}|^2,\qquad
 \mathcal D=\prod_{v\in V}\{\|x_v\|\le1\}.
 \tag{1}
\]
Put \(e_*=\min_{\mathcal D}E\), \(\sigma=1/16\), and
\(\gamma=197/196\). The known budget \(B=B_{\rm tot}\) is unchanged.
The complete source theorem gives
\[
 \begin{gathered}
 \|\Phi_v\|,\|L\|\le\sigma,\qquad
 I\le D_{\mathbb R}^2E\le3I,\qquad
 x-\tfrac12\nabla E(x)\in\tfrac{33}{256}\mathcal D,\\
 B^2e_*\le |K_N|^2\le\gamma B^2e_* .
 \end{gathered}
 \tag{2}
\]
Write \(G(x)=(\Phi_v((x_c)_c)-x_v)_v\).
The true normalized recursion field \(a^{\rm ex}\) satisfies
\(G(a^{\rm ex})=0\), \(La^{\rm ex}_{v_0}=K_N/B\), and
\(\|a^{\rm ex}_v\|\le\sigma\).
All gradients use the real inner product
\(\operatorname{Re}\sum_v h_v^*k_v\), represented by complex
packet columns.

Choose arbitrary unit vectors \(u_v\in H_N\). Their lines are the
supplied projective directions; choosing them is still a problem
in the full \(N\)-dimensional spaces. For each proper vertex define
\[
\kappa_v=\|\Phi_v((u_c)_c)\|,\qquad
c_v=u_v^*\Phi_v((u_c)_c),\qquad a_v=|c_v|,\qquad
 \beta=|Lu_{v_0}|^2.
 \tag{3}
\]
At a leaf the expression inside \(\Phi_v\) is its prescribed
constant. Then \(0\le a_v\le\kappa_v\le\sigma\) and
\(0\le\beta\le\sigma^2\). These numbers use actual local tensors
and supplied directions, without the unknown closed scalar.

## 2. An explicit product certificate without minimization

Put \(\Pi_v=u_vu_v^*\), and evaluate the projected forward recursion
\[
 \widetilde a_v
       =\Pi_v\Phi_v((\widetilde a_c)_c)=\alpha_vu_v,
 \qquad
 \alpha_v=c_v\prod_{c\text{ child of }v}\alpha_c .
 \tag{4}
\]
Empty products are one. Consequently
\[
 k_\parallel=L\widetilde a_{v_0}
               =(Lu_{v_0})\prod_{v\in V}c_v,\qquad
 A_v:=|\alpha_v|=a_v\prod_c A_c .
 \tag{5}
\]
These formulas retain the actual complex phases and original closing.
They do not require a choice of arguments or division by any overlap.
Changing the unit representative of a supplied line leaves the
projected field and \(k_\parallel\) unchanged.

Every projected packet has norm at most \(\sigma\), by forward
induction. Its residual is exactly transverse:
\[
 G_v(\widetilde a)
   =(I-\Pi_v)\Phi_v((\widetilde a_c)_c),\qquad
 H_0:=\|G(\widetilde a)\|^2
      =\sum_v(\kappa_v^2-a_v^2)\prod_c A_c^2.
 \tag{6}
\]
Thus the full trial value is \(|k_\parallel|^2+H_0\).

The residual-to-source comparison improves slightly on this small
packet set. The true field \(a^{\rm ex}\) and \(\widetilde a\)
both have every packet norm at most \(\sigma\). On their segment
write \(DG=-I+\mathscr A\). A unary derivative block has norm at
most \(\sigma\); either derivative block at a binary gate has
norm at most \(\sigma^2\). Each child occurs in only one parent.
The squared norm of a binary row is bounded by \(2\sigma^4\)
times the sum of its child squared norms. Hence
\(\|\mathscr A\|\le\sigma\). Integrating along the segment gives
\[
 \|G(\widetilde a)\|
     \ge(1-\sigma)\|\widetilde a-a^{\rm ex}\|,\qquad
 \boxed{\quad
       |K_N/B-k_\parallel|\le\frac{\sqrt{H_0}}{15}.
       \quad}
 \tag{7}
\]
The last step uses \(\|L\|\le1/16\), not a substituted norm closing.
In particular, with \(S_0=|k_\parallel|\),
\[
 \boxed{\quad
 B(S_0-\sqrt{H_0}/15)_+
       \le |K_N|\le B(S_0+\sqrt{H_0}/15).
 \quad}
 \tag{8}
\]
This includes zero overlaps and zero projected outputs.
For example \(H_0\le S_0^2\) implies
\[
 \frac{196}{225}B^2S_0^2\le |K_N|^2
                   \le\frac{256}{225}B^2S_0^2 .
 \tag{9}
\]
When \(S_0=H_0=0\), (8) forces \(K_N=0\).
A positive-rate lower bound follows if the explicit product has
that rate and its relative leakage satisfies a suitable bound in
(8). No such geometric estimate is established here.

## 3. All scalar packet phases align on a tree

For each vertex put
\(z_v=u_v^*\Phi_v((u_c)_c)\). Choose phases recursively by
\[
 \theta_v=\sum_{c\text{ child of }v}\theta_c+\arg z_v,
 \qquad \widehat u_v=e^{i\theta_v}u_v.
\tag{10}
\]
The empty sum at a leaf is zero. If \(z_v=0\), choose its argument
arbitrarily. Complex multilinearity gives, in every case,
\[
        \widehat u_v^*\Phi_v((\widehat u_c)_c)=a_v\ge0.
\tag{11}
\]
There is one parent for each proper packet, so this recursive
choice creates no conflicting phase condition. A closing term
\(|Lx_{v_0}|^2\) is unchanged by its packet's scalar phase.

Let \(0\le r_v\le1\), and define
\[
 p_v(r)=\prod_{c\text{ child of }v}r_c,\qquad
 x_v(r)=r_v\widehat u_v,
\tag{12}
\]
with empty product one. Equations (3), (10)--(11) prove
\[
 \boxed{\quad
 F_u(r):=E(x(r))
 =\sum_{v\in V}
   \bigl[r_v^2+\kappa_v^2p_v(r)^2-2a_vr_vp_v(r)\bigr]
                                      +\beta r_{v_0}^2 .
 \quad}
\tag{13}
\]
This is the exact minimum over all scalar phases for these
directions and radii. Indeed every gate cross term is bounded
below by replacing its real inner product by its absolute value,
and (10) attains all those lower bounds simultaneously.
The phase choice is independent of the radii, including zero radii.

The scalar objective has the explicit nonnegative decomposition
\[
 F_u(r)=\sum_{v\in V}
 \left[(r_v-a_vp_v(r))^2+
              (\kappa_v^2-a_v^2)p_v(r)^2\right]
                                      +\beta r_{v_0}^2.
\tag{14}
\]
Its degree is at most four. Only scalar packet phases have been
removed; phases between coefficients inside each packet remain
in the directions and their actual tensor overlaps.

## 4. The scalar amplitude problem is uniformly convex

The map \(r\mapsto(r_v\widehat u_v)_v\) is a real linear isometry.
Consequently restriction of (2) proves
\[
                   I\le D^2F_u(r)\le3I
                         \qquad(0\le r_v\le1).
\tag{15}
\]
There is a unique minimizer \(r^u\) on this cube. This is a
problem in \(s\) real variables once the directions and the
coefficients (3) have been supplied; their construction and
full tensor evaluation have not become independent of \(N\).

No upper amplitude constraint is active. If \(r_v=1\), the
inward estimate (2), paired with \(\widehat u_v\), gives
\[
 \partial_{r_v}F_u(r)
 =\operatorname{Re}(\widehat u_v^*\nabla_v E(x(r)))
                   \ge2(1-33/256)>0.
\tag{16}
\]
This contradicts the necessary one-sided derivative condition
for a minimum at the upper endpoint.

At \(r_v=0\), formula (13) gives
\(\partial_{r_v}F_u(r)\le0\): the contribution of its own gate
is \(-2a_vp_v\); its proper parent's contribution, if present,
is also a nonpositive cross term, and the root contribution is
zero. A minimum at zero requires this derivative to be
nonnegative. It is therefore zero. Interior derivatives vanish
as well. Hence
\[
       \nabla F_u(r^u)=0,\qquad 0\le r_v^u\le33/256.
\tag{17}
\]
The last bound follows by pairing the full inward step in (2)
with \(\widehat u_v\) at this stationary radius field.

One possible scalar iteration is
\[
 r^{(j+1)}_v
   =\max\{0,r^{(j)}_v-\tfrac12\partial_{r_v}F_u(r^{(j)})\}.
\tag{18}
\]
The unprojected component is at most \(33/256\), by (2).
Thus this map stays in the cube. Averaging (15) along a segment
and using nonexpansiveness of the componentwise maximum shows
that it contracts distances by at most \(1/2\).
This is an additive convergence statement; relative accuracy
for an exponentially small value is not asserted.

## 5. Only transverse gradients remain

Write \(x^u=x(r^u)\), \(g_v=\nabla_vE(x^u)\), and
\(\Pi_v=u_vu_v^*=\widehat u_v\widehat u_v^*\).
The amplitude equations also remove the imaginary component
of the full gradient along these lines.

To check this even at zero amplitudes, let \(w\) be the proper
parent of \(v\), and put
\(p_{w\setminus v}=\prod_{c\ne v}r_c\) over its other children.
Direct differentiation of the original complex squares gives
\[
 \tfrac12\widehat u_v^*\nabla_vE(x(r))
 =r_v-a_vp_v+
 \begin{cases}
 r_v\kappa_w^2p_{w\setminus v}^2
                 -a_wr_wp_{w\setminus v},&w\text{ proper},\\
 \beta r_v,&v=v_0.
 \end{cases}
\tag{19}
\]
Each quantity on the right is real, by (11). This calculation
uses both the vertex's own residual and its parent's residual;
no adjoint contribution is omitted. It remains valid at a
zero overlap or a zero amplitude. Equations (17), (19) imply
\[
                  \widehat u_v^*g_v=0,\qquad
                  \|g\|^2=\sum_v\|(I-\Pi_v)g_v\|^2.
\tag{20}
\]

Set
\[
 q_u=F_u(r^u),\qquad
 \mathcal T_u=\sum_v\|(I-\Pi_v)g_v\|^2.
\]
The complete source theorem's quadratic gradient minorant
therefore gives the certified bounds
\[
 \boxed{\quad
 B^2\max\{0,q_u-\tfrac12\mathcal T_u\}
            \le |K_N|^2\le\gamma B^2q_u .
 \quad}
\tag{21}
\]
These use the original scalar closing, every source phase and
all full-Hermite coordinates. They require no division by \(K_N\).
If \(q_u=0\), the upper bound already implies \(K_N=0\).
If \(q_u>0\), a sufficient relative lower witness is
\(\mathcal T_u\le2(1-\eta_N)q_u\), with \(0<\eta_N\le1\).
If also \(\log\eta_N=o(N)\) and
\(\pi N^{-1}\log(B^2q_u)\to V>0\), (21) yields
\(2\pi N^{-1}\log|K_N|\to V\).
Neither estimate is proved for geometric directions here.

## 6. Scope and complete proof source

Minimizing \(q_u\) over all projective directions recovers \(e_*\)
exactly: every \(x(r)\) is feasible, while every feasible field
can be expressed by directions, radii and phases, whose phase
optimization cannot increase its energy. This observation does
not reduce the full direction problem to fixed dimension.

The explicit product certificate (8) needs neither that
direction minimization nor the scalar amplitude solve.
Its local complex overlaps and leakage sum suffice.
For the optional refinement, amplitudes and scalar phases
need no separate approximation: they are optimized in
the scalar convex problem (13). Its source certificate (21)
uses only transverse gradients.
This differs from deleting higher moments, linear-corridor
elimination, or replacing the original closing by a norm.
Formula (13) depends only on the supplied projective lines,
but an aligned representative need not be unique at zero overlaps.
Every choice allowed in (10) satisfies (21).

There is no assertion that minimization over directions remains
convex or has a new fixed-order semidefinite description.
No geometric direction field, transverse estimate, short-filling
lower bound, or new volume-conjecture class is constructed.
The supplied directions are full \(N\)-dimensional packet vectors,
including their tails and repeated-root derivative coordinates.
An interior Gaussian germ,
classical shape or matching mean character is not automatically
such a supplied vector with the required leakage estimate.

The sole complete proof source was read at the matching pin:

| Source | SHA-256 |
|---|---|
| [Complete normalized Conway source, 329 lines](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

Orthogonal tensor compression and estimates by sums of discarded
squared norms are established methods. Primary coverage includes
[Oseledets, Tensor-Train Decomposition, Theorem 2.2](https://users.math.msu.edu/users/iwenmark/Teaching/CMSE890/TENSOR_oseledets2011.pdf)
and [Grasedyck, Hierarchical Singular Value Decomposition of Tensors,
Definition 15, Lemma 16 and Theorem 17](https://webdoc.sub.gwdg.de/ebook/serien/e/MPI_Math_Nat/preprint2009_27.pdf).
Those statements were checked for coverage; no proof is imported.
No novelty is claimed for general orthogonal truncation.
The closing-specific comparison (7), together with the stated
phase and scalar-amplitude deductions, is proved here.

The projected product and leakage identities, phase alignment,
scalar amplitude reduction and transverse certificate are proved above.
Only written mathematics and text operations were used.
