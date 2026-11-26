# Boundary forces and a local error certificate for the Conway source

21 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

The redistributed Conway gate energies admit a particularly simple
boundary-force dual. On an explicit ball of forces, every local problem
has an interior minimizer. The dual is uniformly well conditioned,
independently of the level and the size of the tree. Its value and the
disagreement of its local boundary packets give the two-sided estimate
\[
                     d(p)\le e_*\le d(p)+\|m(p)\|^2.
\]
Here \(e_*\) is the original normalized source minimum. The local
constants entering \(d(p)\) retain their signs. This estimate does not
make their sum positive or determine its hyperbolic volume rate.

## 1. The actual packet variables and local potentials

Use the complete normalized compiler in the
[convex source theorem](research_convex_normalized_conway_source.md)
and the quadratic redistribution in the
[gate-local gluing theorem](research_conway_gate_local_semidefinite_gluing.md).
There are \(s\) proper vertices. At level \(N\), each packet lies
in the full complex Newton space \(H_N\), of dimension \(N\), including
its repeated-root directions. All norms and derivatives below use real
coordinates on these complex packets, with inner product
\(\operatorname{Re}(u^*v)\).

The local map \(\Phi_v\) is a prescribed leaf, a linear turn, or the
original bilinear product, after its recorded Hilbert--Schmidt
normalization. Put \(\sigma=1/16\). Every local tensor and the original
normalized closing row \(L\) have norm at most \(\sigma\).
Each proper vertex has at most two distinct children, and each child
occurs in one parent. Write \(v_0\) for the top proper vertex and
\(\rho\) for the closing root.

For packet fields in the product of unit balls, set
\[
 E(x)=\sum_{v\ne\rho}\|\Phi_v((x_c)_c)-x_v\|^2
                                      +|Lx_{v_0}|^2,
 \qquad e_*=\min E.
 \tag{1}
\]
The original marked source and the known budget product satisfy
\[
 B_{\rm tot}^2e_*\le |K_N|^2
                   \le\gamma B_{\rm tot}^2e_*,
 \qquad\gamma=197/196.
 \tag{2}
\]
No ordinary-color sum or replacement closing functional is used.

Put \(t=1/4\) and define, on each gate's own packet variables,
\[
 \begin{split}
 V_v&=\|\Phi_v-x_v\|^2-t\|x_v\|^2
                                  +t\sum_{c\text{ child}}\|x_c\|^2,
                                     &&v\ne\rho,\\
 V_\rho&=|Lx_{v_0}|^2+t\|x_{v_0}\|^2.
 \end{split}
 \tag{3}
\]
Their sum on consistent packet fields is exactly \(E\). Local
potentials need not be nonnegative. All their constants must be kept.

For a bag \(C\), denote by \(Q_2(C)\) the expressions
\[
 s_0+\sum_{w\in C}(1-\|x_w\|^2)s_w,
 \tag{4}
\]
where \(s_0\) is a sum of squares of polynomials of degree at most two,
and every \(s_w\) is a sum of squares of degree-at-most-one polynomials.
Complex absolute squares mean sums of real and imaginary squares.
The complete local Hessian certificate proves, with
\(\mu_0=31/128\), that every feasible center \(b\) satisfies
\[
 V_v(x)-V_v(b)-\nabla V_v(b)\cdot(x-b)
                           -\frac{\mu_0}{2}\|x-b\|^2\in Q_2(C_v).
 \tag{5}
\]
This fixed-degree certificate will give explicit lower witnesses.

## 2. Uniform bounds for every local Hessian

We will also need the slightly stronger numerical bounds
\[
              \mu I\le D^2V_v\le4I,
              \qquad\mu=45/128,
 \tag{6}
\]
on each bag's product of unit balls. These are pointwise bounds;
the polynomial certificate used below remains (5).

At a proper gate let \(h_0\) vary its output, and let \(h_c\) vary
the inputs. Write \(A h_c=D\Phi_v h_c\). At a product,
\(\|A h_c\|^2\le2\sigma^2\sum_c\|h_c\|^2\). Its residual has
norm at most \(1+\sigma\), so the absolute value of the curvature term
in the half-Hessian is at most
\(\sigma(1+\sigma)\sum_c\|h_c\|^2\). Therefore
\[
 \begin{split}
 \tfrac12D^2V_v[h,h]
 &\ge\tfrac14\|h_0\|^2+
      \{t-2\sigma^2-\sigma(1+\sigma)\}\sum_c\|h_c\|^2\\
 &=\tfrac14\|h_0\|^2+\tfrac{45}{256}\sum_c\|h_c\|^2.
 \end{split}
 \tag{7}
\]
We used \(\|h_0-Ah_c\|^2\ge\|h_0\|^2/2-\|Ah_c\|^2\)
before subtracting \(t\|h_0\|^2\). The upper estimate follows from
\[
 \tfrac12D^2V_v[h,h]
 \le2\|h_0\|^2+
       \{t+4\sigma^2+\sigma(1+\sigma)\}\sum_c\|h_c\|^2
 \le2\|h\|^2.
 \tag{8}
\]
Turns have no residual curvature and satisfy the same bounds. A leaf
has Hessian \(2(1-t)I\); the root has Hessian
\(2tI+2L^*L\). They also satisfy (6). Affine forces do not alter any
of these Hessians.

## 3. A force ball on which all local minimizers are interior

Choose one real force \(p_v\) on each full packet and put
\[
 \begin{split}
 F_v(x;p)&=V_v(x)-p_v\cdot x_v
                              +\sum_{c\text{ child}}p_c\cdot x_c,
                                                &&v\ne\rho,\\
 F_\rho(x;p)&=V_\rho(x)+p_{v_0}\cdot x_{v_0}.
 \end{split}
 \tag{9}
\]
All real and imaginary coefficients remain present in these forces.
Restrict them to the product of balls
\[
                  \mathcal P=\{p:\|p_v\|\le1/3\text{ for every }v\}.
 \tag{10}
\]
Each \(F_v\) has a unique minimizer on its bag balls by (6). In fact
this minimizer is strictly interior for every \(p\in\mathcal P\).

To prove this, fix all packets but one and suppose that packet has norm
one. The derivative in its outward radial direction is positive in
each of the following cases:
\[
 \begin{array}{c|c}
 \text{packet occurrence}&\text{lower bound for its radial derivative}\\ \hline
 \text{proper output}&2(1-t)-2\sigma-1/3>0\\
 \text{proper input}&2t-1/3-2\sigma(1+\sigma)=13/384>0\\
 \text{root input}&2t-1/3=1/6>0.
 \end{array}
 \tag{11}
\]
For the input estimate, use \(\|D_c\Phi_v\|\le\sigma\) and
\(\|\Phi_v-x_v\|\le1+\sigma\). Moving that packet radially inward
would strictly decrease the local potential, contradicting minimality.
Thus the local gradients vanish at all the local minimizers.
The strict inequalities also hold on a neighborhood of the closed
force ball. The invertible Hessians in (6) consequently make the local
minimizers smooth functions of the forces there.

## 4. The exact dual and its conditioning

Temporarily give each bag its own copy of its packets. Every physical
packet then has exactly two copies: its own gate's output and its
parent's input, including the root input at the top. Let \(y\) denote
this list of copies. Define \(B\) by
\[
           (By)_v=y_{\operatorname{parent}(v),v}-y_{v,v}.
 \tag{12}
\]
The signs match (9), so the sum of the force-adjusted local potentials
is \(\sum_vV_v(y)+p\cdot By\). Different rows of \(B\) have disjoint
copy coordinates, and every row is the difference of two copies.
Hence
\[
                               BB^*=2I.
 \tag{13}
\]
There is no graph Laplacian in this equality.

For \(p\in\mathcal P\), let \(y_v(p)\) be the local minimizer of
\(F_v\), and define
\[
 d(p)=\sum_vF_v(y_v(p);p),\qquad m(p)=By(p).
 \tag{14}
\]
The number \(d(p)\) is a signed sum of local minima. Weak duality gives
\(d(p)\le e_*\), since the forces cancel on every consistent field.
Differentiation of the local stationary equations gives
\[
 \nabla d(p)=m(p),\qquad
 -D^2d(p)=B\,H_{\rm loc}(p)^{-1}B^*,
 \tag{15}
\]
where \(H_{\rm loc}\) is the block diagonal matrix of local Hessians.
Equations (6) and (13) imply
\[
                 \frac12 I\le -D^2d(p)\le\frac{256}{45}I.
 \tag{16}
\]
These constants do not depend on the level, the packet dimension, or
the number of gates.

The global source minimizer \(a_*\) satisfies
\(\|a_{*,v}\|\le33/256\), by the half-gradient self-map in the
convex source theorem. Define its forces by
\[
 p_v^*=\partial_{x_v}V_v(a_*)
                      =\tfrac32a_{*,v}-2\Phi_v((a_{*,c})_c).
 \tag{17}
\]
They obey
\[
               \|p_v^*\|\le\tfrac32\frac{33}{256}+2\sigma
                         =\frac{163}{512}<\frac13.
 \tag{18}
\]
Global stationarity makes every force-adjusted local gradient zero at
the corresponding restriction of \(a_*\). Thus its local minima
agree across every edge, \(m(p^*)=0\), and
\[
                      d(p^*)=e_*=\max_{p\in\mathcal P}d(p).
 \tag{19}
\]
The maximizer is unique by (16). This proves attainment inside a known
force ball, without knowing the source value or assuming it nonzero.

For example, projected gradient ascent
\[
 p^{j+1}=\operatorname{proj}_{\mathcal P}
                       \left(p^j+\frac{180}{557}m(p^j)\right)
 \tag{20}
\]
contracts distances to \(p^*\) by \(467/557\). Indeed the averaged
negative Hessian lies between the two constants in (16), so the
unprojected step has this contraction factor. Euclidean projection on
the product of force balls is nonexpansive, and \(p^*\) is a fixed point.
No iteration or numerical optimization has been run here.

## 5. The boundary mismatch is an upper error certificate

At the local minimizers, average each packet's two copies:
\[
                 \bar y=y(p)-\tfrac12B^*m(p).
 \tag{21}
\]
Both copies then equal their average, which is still in the unit ball.
Thus \(\bar y\) defines a feasible global field. Moreover
\[
                  \|\bar y-y(p)\|^2=\tfrac12\|m(p)\|^2.
 \tag{22}
\]
The gradients of the local \(F_v\) vanish at \(y_v(p)\). Apply the
upper Hessian bound \(4I\) along the segment to their averaged copies.
The forces cancel at \(\bar y\), so
\[
 E(\bar y)=\sum_vF_v(\bar y_v;p)
           \le d(p)+2\|\bar y-y(p)\|^2
           =d(p)+\|m(p)\|^2.
 \tag{23}
\]
Together with weak duality and (2), this proves
\[
 \boxed{\quad d(p)\le e_*\le d(p)+\|m(p)\|^2,\quad}
 \tag{24}
\]
\[
 \boxed{\quad
 B_{\rm tot}^2\max(0,d(p))\le|K_N|^2
       \le\gamma B_{\rm tot}^2\{d(p)+\|m(p)\|^2\}.
 \quad}
 \tag{25}
\]
All quantities in (25) come from independent local problems and their
full boundary packets. Neither equality of angles nor equality of
their mean charges replaces the packet mismatch in this formula.

## 6. Explicit degree-four witnesses, including approximate local solves

For exact local minimizers, (5) and stationarity give
\[
                    F_v(\cdot;p)-F_v(y_v(p);p)\in Q_2(C_v).
 \tag{26}
\]
Thus the lower number in (25) has a local degree-four certificate.
The original complex tensors enter its real polynomial coefficients;
their phases have not been discarded.

One can write feasible certificates without exact local minimization.
Take any force \(p\), and choose feasible trial copies \(b_v\) in
every bag. Put
\[
 q_v=\nabla F_v(b_v;p),\quad
 C=\sum_vF_v(b_v;p),\quad q=(q_v)_v,\quad m=Bb,
 \qquad A=C-\frac{64}{31}\|q\|^2.
 \tag{27}
\]
By completing a square in (5),
\[
 F_v(x;p)-\left(F_v(b_v;p)-\frac{\|q_v\|^2}{2\mu_0}\right)
                                                \in Q_2(C_v).
 \tag{28}
\]
Explicitly, the expression on the left is the sum of the certificate
in (5) and
\(\frac{\mu_0}{2}\|x-b_v+q_v/\mu_0\|^2\).
Its degree is at most four and it uses only the local bag.
The signed sum \(A\) is consequently a certified lower bound for
\(e_*\).

Averaging these trial copies again gives a feasible global field.
Taylor's upper estimate and Cauchy--Schwarz give
\[
 e_*\le U:=C+\frac1{\sqrt2}\|q\|\|m\|+\|m\|^2.
 \tag{29}
\]
Indeed the first-order term is at most
\(\|q\|\|\bar b-b\|=\|q\|\|m\|/\sqrt2\), and the quadratic term
is at most \(\|m\|^2\). In particular
\[
         B_{\rm tot}^2\max(0,A)\le |K_N|^2
                                      \le\gamma B_{\rm tot}^2U.
 \tag{30}
\]
The trials in this section need not be local minimizers, and this
certificate does not require the force restriction (10). The force
ball supplies the smooth, uniformly conditioned local problems in
Sections 3--5; the polynomial witness (28) is valid for arbitrary forces.

## 7. What a geometric force construction must establish

For a fixed completed knot, suppose forces \(p_N\in\mathcal P\) have
\(d_N=d(p_N)>0\), and suppose
\[
 \log\left(1+\frac{\|m(p_N)\|^2}{d_N}\right)=o(N),\qquad
 \frac\pi N\log(B_{{\rm tot},N}^2d_N)
                 \longrightarrow\operatorname{Vol}(S^3\setminus K).
 \tag{31}
\]
Then (25) proves the volume identity for the original marked source.
The fully explicit alternative is to use (27)--(30), require
\(A_N>0\), \(\log(U_N/A_N)=o(N)\), and give \(B_{{\rm tot},N}^2A_N\)
the stated volume rate. These are lower certificates using the actual
full-coordinate quantum boundary data, including their phases.

Uniform conditioning does not remove the required precision. Taylor's
formula around \(p^*\) and (16) show
\[
 \frac14\|p-p^*\|^2\le e_*-d(p)
                           \le\frac{128}{45}\|p-p^*\|^2.
 \tag{32}
\]
If the normalized \(e_*\) is exponentially small, a positive dual value
therefore requires force accuracy on its square-root scale. Local
convexity and a rapidly contracting iteration do not establish the
positive geometric rate in (31).

An arbitrary fixed short component may be kept through its exact
shifted boundary energy in the gate-local gluing theorem. The argument
above retains its original local gates, so the same constants and
degree-four witnesses apply without a separate estimate for every
short filling. What is still missing is a geometric construction of
these forces or trial copies with the positive signed sum and relative
error required by (31). No such construction or new volume theorem is
claimed here.

## Complete proof sources

Both complete matching sources were read before this proof was written:

| Source | SHA-256 |
|---|---|
| [Gate-local semidefinite gluing](research_conway_gate_local_semidefinite_gluing.md) | 8b3241f9cc8a9e740aa4223345e39932f3a2096fcdab60f55458a6266857e8e9 |
| [Complete normalized source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

The boundary-force method is convex dual decomposition; no novelty is
claimed for that general method. The local constants, the explicit
force ball, the mismatch certificate and the degree-four witnesses for
the complete marked Conway source are proved here. Only written
mathematics and text/hash operations were used. No mathematical program,
test, numerical optimization, build, git operation or earlier-final
edit was performed.
