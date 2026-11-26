# A source normal and a tangential error certificate

21 November 2026. Research note. Previous finals and public manuscripts
remain unchanged.

The normalized Conway source is a sum of squared recursion residuals
and one complex closing component. Its linearization therefore has a
one-dimensional complex normal. Projecting onto that normal gives a
computable scalar quantity. The error in its prediction of the minimum
is bounded by the tangential energy, with constants independent of the
level and the number of vertices.

The resulting radius vanishes at the minimizing field, even though
the recursion residual there need not vanish. This differs from the
earlier complex-source error disk, whose radius uses the full residual.
No geometric trial field or new volume identity is supplied below.

## 1. The original source and the lifted residual

Use the actual normalized compiler of the complete source theorem.
At level \(N\ge2\), let
\(\mathcal X=\bigoplus_{v=1}^s H_N\) be the direct sum of its
proper packet spaces. Each \(H_N\) is the full \(N\)-dimensional
Newton space, including the repeated-root normal directions. The
feasible set \(\mathcal D\subset\mathcal X\) is the product of
the unit balls.

Each prescribed leaf, linear gate, bilinear gate and original closing
row has been divided by its known budget
\(16\max(1,\|T_v\|_{\rm HS})\). Put \(\sigma=1/16\).
The resulting local maps \(\Phi_v\), and the normalized original
closing row \(L\), have norm at most \(\sigma\). Define
\[
 G_v(x)=\Phi_v((x_j)_{j\text{ child of }v})-x_v,\qquad
 cx=Lx_{v_0},\qquad
 E(x)=\|G(x)\|^2+|cx|^2 ,
 \tag{1}
\]
where \(v_0\) is the proper child of the closing root. The row
\(c\) is zero on all other packet slots.

Write \(B=B_{\rm tot}>0\) for the retained product of all local
budgets, and let \(K_N\) be the original reduced source. No phase,
marked cap, Cartan factor or peripheral line has been reset. If
\[
                     e_*=\min_{x\in\mathcal D}E(x),
 \qquad \gamma=\frac{197}{196},
\]
the complete source theorem gives
\[
             B^2e_*\le |K_N|^2\le\gamma B^2e_* .
 \tag{2}
\]
It also proves that \(E\) has a unique interior minimizer \(x_*\)
and real Hessian
\[
                           I\le D_{\mathbb R}^2E\le3I
                         \quad\hbox{on }\mathcal D.
 \tag{3}
\]
Real inner products are \(\operatorname{Re}(u^*v)\).

Fix any feasible trial field \(x\). All operators below are evaluated
at this field. Put
\[
 r=G(x),\quad z=cx,\quad DG(x)=-I+A,\quad
 S=I-A,\quad d=cS^{-1},\quad \nu=\|d\|^2 .
 \tag{4}
\]
The child-to-parent matrix \(A\) is strictly triangular. Its finite
inverse, backward source row and bounds are
\[
 S^{-1}=\sum_{j=0}^{s-1}A^j,\qquad
 \|A\|\le\frac18,\qquad \|S^{-1}\|\le\frac87,\qquad
 \|d\|\le\frac1{14}.
 \tag{5}
\]
Thus \(d\) is computable by the actual backward tree recursion.
It is not chosen using \(K_N\).

Introduce the lifted residual and its complex-linear derivative:
\[
 F(x)=(G(x),cx)\in\mathcal X\oplus\mathbb C,\qquad
 J=DF(x)=\binom{-S}{c}.
 \tag{6}
\]
All phases in the source correction
\[
                             w=z+dr
 \tag{7}
\]
are added before taking a norm.

## 2. The exact normal and tangential energies

Since \(S\) is invertible, \(J\) is injective. Its image has
complex codimension one in \(\mathcal X\oplus\mathbb C\).
Its orthogonal complement is spanned by
\[
                               \binom{d^*}{1},
\]
because \(-S^*d^*+c^*=0\). Let \(P_{\rm n}\) and
\(P_{\rm t}\) denote the orthogonal projections onto this normal
line and onto \(\operatorname{ran}J\), respectively. Define
\[
 \boxed{\quad
 \mathfrak n(x)=\|P_{\rm n}F(x)\|^2
       =\frac{|z+dr|^2}{1+\nu},\qquad
 \mathfrak t(x)=\|P_{\rm t}F(x)\|^2=E(x)-\mathfrak n(x).
 \quad}
 \tag{8}
\]
Both quantities are nonnegative. This is a projection in the
**lifted residual space**, not deletion of a physical boundary
channel: every Hermite direction still occurs in \(\mathcal X\).
In particular \(\mathfrak n(x)\) may be zero; orthogonality does
not prove that the coherent scalar (7) survives.

Write \(H_0=J^*J=S^*S+c^*c\). Equation (5) and
\(\|c\|\le1/16\) give
\[
               \frac{49}{64}I\le H_0\le\frac{325}{256}I.
 \tag{9}
\]
The full real gradient is \(\nabla E(x)=2J^*F(x)\). Since
\(J^*P_{\rm n}=0\),
\[
                  \|\nabla E(x)\|^2
                     \le \frac{325}{64}\mathfrak t(x).
 \tag{10}
\]
Moreover \(\mathfrak t(x)=0\) if and only if this gradient is
zero. By (3), that happens precisely at \(x=x_*\).

For comparison with the residual coordinates, stationarity is exactly
\[
                              r=d^*z .
 \tag{11}
\]
It follows that \(E(x_*)=\mathfrak n(x_*)=e_*\) and
\(\mathfrak t(x_*)=0\). The original closing is kept in this
identity; the entire residual \(r\) need not be zero at \(x_*\).

## 3. A feasible Gauss–Newton field

The Gauss–Newton displacement is the unique least-squares solution
\[
                 \delta=-H_0^{-1}J^*F(x).
 \tag{12}
\]
It satisfies
\[
 F(x)+J\delta=P_{\rm n}F(x),\qquad
 \|J\delta\|^2=\mathfrak t(x),\qquad
 \|\delta\|^2\le\frac{64}{49}\mathfrak t(x).
 \tag{13}
\]
In this source problem the field \(y=x+\delta\) is feasible
without a projection onto the balls.

To check this, first take the exact residual-Newton repair
\[
                         y_0=x+S^{-1}r .
 \tag{14}
\]
The earlier tree repair proof gives \(\|(y_0)_v\|\le1/14\)
for every packet. Indeed
\(Sy_0=\Phi(x)-A(x)x\), whose blocks have norm at most
\(\sigma\); upward solution of this equation bounds each packet
by \(\sigma/(1-2\sigma)=1/14\).
Its original closing is \(cy_0=w\), so
\[
                              |w|\le\frac1{224}.
 \tag{15}
\]
The explicit rank-one least-squares correction is
\[
                   y=y_0-S^{-1}d^*\frac{w}{1+\nu}.
 \tag{16}
\]
For verification, its linearized residual and closing are
\[
                  r-S\delta=d^*\frac{w}{1+\nu},
             \qquad z+c\delta=\frac{w}{1+\nu},
\]
which give precisely the normal component in (13).
Using (5) and (15), the correction in (16) has total norm at most
\[
                  \frac87\frac1{14}\frac1{224}
                                       =\frac1{2744}.
 \tag{17}
\]
Thus every packet of \(y\) has norm at most
\(1/14+1/2744=197/2744<1\). No unknown source value enters
the construction.

## 4. A two-sided certificate for the minimum

For any displacement \(h\), the bilinear tree gives the exact
expansion
\[
 F(x+h)=F(x)+Jh+(\mathcal Q(h),0),\qquad
                          \|\mathcal Q(h)\|\le\frac{\|h\|^2}{32}.
 \tag{18}
\]
Here \(\mathcal Q_v(h)=\Phi_v(h_L,h_R)\) at a binary
product and is zero elsewhere. Different sibling pairs are disjoint,
so the stated bound follows from
\(\sum_v\|h_L\|^2\|h_R\|^2\le\|h\|^4/4\).
There is no higher Taylor remainder.

**Theorem.** Every feasible trial field satisfies
\[
 \boxed{\quad
 \max\left\{0,\sqrt{\mathfrak n(x)}
                   -\frac{325}{2048}\mathfrak t(x)\right\}
 \ \le\sqrt{e_*}\ \le\
 \sqrt{\mathfrak n(x)}+\frac{2}{49}\mathfrak t(x).
 \quad}
 \tag{19}
\]
All constants are independent of \(N\), the tree size and the
fixed crossing powers after their original budgets are retained.

**Proof.** Strong monotonicity from (3), with
\(\nabla E(x_*)=0\), and (10) give
\[
              \|x_*-x\|^2\le\|\nabla E(x)\|^2
                           \le\frac{325}{64}\mathfrak t(x).
 \tag{20}
\]
Apply \(P_{\rm n}\) to (18) with \(h=x_*-x\). The linear
term disappears exactly. The reverse triangle inequality yields
\[
 \sqrt{e_*}=\|F(x_*)\|
   \ge\sqrt{\mathfrak n(x)}-\|\mathcal Q(x_*-x)\|
   \ge\sqrt{\mathfrak n(x)}-\frac{325}{2048}\mathfrak t(x).
\]
Clipping the right side at zero proves the lower bound.

For the upper bound, use the feasible field (16) in (18).
Equations (13) and (18) imply
\[
 \sqrt{e_*}\le\|F(y)\|
     \le\sqrt{\mathfrak n(x)}+\frac1{32}\|\delta\|^2
     \le\sqrt{\mathfrak n(x)}+\frac{2}{49}\mathfrak t(x).
\]
This proves (19). \(\square\)

The radius now uses the tangential energy, which vanishes at
stationarity. It is not the previous bound for the complex error
\(|K_N/B-w|\) in terms of \(\|r\|^2\). Equation (19) controls
the minimum and hence the magnitude of the original source through
(2); it does not identify its complex phase with \(w\).

## 5. An explicit original-source lower witness

Combining (2) and (19) gives
\[
 \boxed{\quad
 B\left[\sqrt{\mathfrak n}-\frac{325}{2048}\mathfrak t\right]_+
 \le |K_N|
 \le\sqrt\gamma B
            \left(\sqrt{\mathfrak n}+\frac{2}{49}\mathfrak t\right).
 \quad}
 \tag{21}
\]
Here \([u]_+=\max(0,u)\), and both energies are evaluated at
the chosen field. The only source-dependent scalar in them is the
computable coherent correction (7), not an assumed value of \(K_N\).

For a fixed construction, suppose feasible fields \(x_N\) satisfy
\(\mathfrak n(x_N)>0\) eventually and
\[
 \mathfrak t(x_N)\le a\sqrt{\mathfrak n(x_N)},\qquad
                         0\le a<\frac{2048}{325},
 \tag{22}
\]
with \(a\) independent of \(N\). If
\[
       \frac{2\pi}{N}\log\bigl(B_{\rm tot}
                        \sqrt{\mathfrak n(x_N)}\bigr)\longrightarrow V,
 \tag{23}
\]
then (21) proves
\[
                      \frac{2\pi}{N}\log|K_N|\longrightarrow V.
 \tag{24}
\]
More explicitly the ratio to the quantity inside the logarithm in
(23) lies between the positive constants
\(1-325a/2048\) and \(\sqrt\gamma(1+2a/49)\).
The discrepancy of the scaled logarithms is therefore \(O(N^{-1})\),
with these explicit constants.

A volume proof must still construct actual geometric fields satisfying
(22) and identify the rate (23). Angle stationarity alone does not
control \(\mathfrak t\), which contains the complete quantum
linearization. Fixed short subtrees may be contracted with their full
packets before applying the same argument, but no lower bound for
their geometric coupling is inferred here. No new filling case or
finite-exception theorem is claimed.

## Complete proof sources and coverage

Both complete proof texts were read at the matching pins below.
The first supplies the actual normalized compiler, source comparison
and interior minimum. The second supplies the original backward row,
exact bilinear remainder and feasible residual-Newton repair.

| Source | SHA-256 |
|---|---|
| [Normalized complete source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| [Source-visible residual transport](research_conway_source_visible_residual_transport.md) | 0d344301b0df65246551cf81498eff84582f796a03271b201f8fbba6c7742007 |

The complete scalar-cap response note was read at pin
6b9b73ae429713bdff63120a9841c06d2311d249f058f3da6b1f4e89dbfaecfb,
and the complete residual-Jacobian Gaussian note at pin
db22b86a97302926fed77385f82ff2284109e288ec3d03dd99538d3671c926b2,
for coverage. They respectively give a scalar nonlinear response and
a determinant bound at the exact minimum. Neither asserts the
trial-field tangential-energy radius (19). Orthogonal least squares
and Gauss–Newton correction are standard methods; no general novelty
is claimed for them.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical iteration, test, build, git operation
or earlier-final edit was performed.
