# A vertexwise criterion for positive geometric fillings

The global sum used to control the finite quantum source is not needed
for geometric completion. For an ordered all-circle tree, the nonlinear
charge equations admit a contraction whose norm is independent of the
number of vertices. This gives a sufficient condition at each vertex,
including vertices with zero or small crossing power and large degree.
The conclusion below concerns the actual hyperbolic metric and its
marked volume and cusp. It makes no new assertion about dominance in
the finite quantum sum.

## 1. Statement

Use the original ordered all-circle construction and its actual
octahedral decomposition. There are at least two circle vertices.
Every graph edge is an original physical quarter-turn, and each vertex
carries an original crossing circle. Keep the original cyclic orders,
disk frames, retained half twists \(\epsilon_v\in\{0,\pm1\}\), and
primitive auxiliary curves \((\mu_v,\lambda_v)\).
Fix the integers \(p_v\) and the physical powers
\(n_v=\epsilon_v-2p_v\). Write \(d_v\ge1\) for the graph degree.
Assume the original component test gives the required knot, when a
knot-complement conclusion is desired.

The following condition suffices for positive geometric completion:
\[
                 \sqrt{d_v^2+n_v^2}\ \ge630
                    \qquad\text{for every vertex }v.
\tag{1}
\]
There is a unique solution in the closed polydisk
\(|\tau_v|\le10^{-2}\) of
\[
 \Psi_v(\boldsymbol\tau)+\frac{i n_v}{2\pi}\tau_v=ic,
 \qquad
 \Psi(\boldsymbol\tau)=\sum_{vw}\psi(\tau_v,\tau_w),
 \qquad 0\le c\le1.
\tag{2}
\]
The solution continues holomorphically in \(c\) on a neighborhood of
the closed unit disk, is zero at \(c=0\), and satisfies
\[
 \operatorname{Im}\tau_v(c)<0\quad(0<c\le1),\qquad
 |\tau_v(c)|
 \le\frac{2\pi c}
          {\sqrt{d_v^2+n_v^2}-d_v/39000}.
\tag{3}
\]
The denominator is positive. The original primitive periods obey
\[
 U_v=-2\pi\Psi_v-i\epsilon_v\tau_v,\qquad
 V_v=2i\tau_v,\qquad U_v+p_vV_v=-2\pi ic.
\tag{4}
\]
The cells consequently complete to cone solid tori of angle \(2\pi c\)
for \(c>0\), and to smooth solid tori at \(c=1\). The main knot cusp
remains unfilled and complete. In particular the endpoint is a
complete finite-volume hyperbolic metric on the actual filled knot
complement.

The constants in (1) are deliberately tied to the already established
radius \(10^{-2}\) of the positive octahedral chart. The substantial
difference from the earlier condition is that there is no sum over
vertices. The number and relative sizes of the degrees and powers
are unrestricted.

The geometric inputs are the [ordered octahedral decomposition](actual_all_circle_octahedral_decomposition.md),
the [positive angular charts](actual_all_circle_angular_octahedra.md), and
the [primitive filling completion](actual_all_circle_geometric_completion.md). Their conclusions about
the actual ordered topology, positive tetrahedra, primitive periods,
and completion are used below. No source comparison diagram is used.

## 2. Exact derivatives of the nonlinear error

On the branches through zero define
\[
 F(t,u)=2\operatorname{arsinh}\!
          \left(\tan(t/2)\cos(u/2)\right),\qquad
 E(t,u)=F(t,u)-t.
\tag{5}
\]
The edge action satisfies \(-2\pi\psi_t=F\). Put
\[
 Q(t,u)=\sqrt{1-\sin^2(t/2)\sin^2(u/2)},\qquad Q(0,0)=1.
\tag{6}
\]
Differentiation gives exactly
\[
 F_t=\frac{\cos(u/2)}{\cos(t/2)Q(t,u)},\qquad
 F_u=-\frac{\sin(t/2)\sin(u/2)}{Q(t,u)}.
\tag{7}
\]
Indeed \(1+\tan^2(t/2)\cos^2(u/2)=Q^2/\cos^2(t/2)\);
the square roots agree at zero and hence throughout the small
connected chart. This fixes the branches in (7).

For \(|t|,|u|\le10^{-2}\), let
\[
 a=\frac1{79000},\qquad b=\frac1{199},\qquad
 \omega=b^4,\qquad \delta=\frac1{39000}.
\tag{8}
\]
The elementary series bounds with \(r=1/200\) give
\[
 |\sin(t/2)|\le\frac{r}{1-r^2/6}<b,\qquad
 |\cos(t/2)-1|
       \le\frac{r^2}{2(1-r^2/12)}<a,
\tag{9}
\]
and the same for \(u\). Thus
\(|Q|^{-1}\le(1-\omega)^{-1}\) and
\(|Q-1|\le\omega\). To see the latter estimate, use
\((Q-1)(Q+1)=-\sin^2(t/2)\sin^2(u/2)\); the branch has
\(\operatorname{Re}Q>0\), so \(|Q+1|\ge1\).
Equation (7) now yields
\[
 \begin{split}
 |E_t|&\le
       \frac{2a/(1-a)+\omega}{1-\omega}<\delta,\\
 |E_u|&\le\frac{b^2}{1-\omega}<\delta.
 \end{split}
\tag{10}
\]
Both final inequalities are rational comparisons. In particular,
\(E(0,u)=0\), and
\[
 E(t,u)=tH(t,u),\qquad
 H(t,u)=\int_0^1 E_t(\lambda t,u)\,d\lambda,\qquad
 |H(t,u)|\le\delta.
\tag{11}
\]
The function \(H\) is holomorphic also at \(t=0\). No division by a
possibly vanishing unknown is needed to define it.

## 3. A contraction independent of the size of the tree

Write \(L_v=\sqrt{d_v^2+n_v^2}=|d_v-in_v|\).
Multiplying (2) by \(-2\pi\) and using (5) gives
\[
 (d_v-in_v)\tau_v+
       \sum_{w\sim v}E(\tau_v,\tau_w)=-2\pi ic.
\tag{12}
\]
Define the fixed-point map
\[
 \mathcal T_{c,v}(\boldsymbol\tau)=
       -\frac{2\pi ic}{d_v-in_v}
       -\frac{\sum_{w\sim v}E(\tau_v,\tau_w)}{d_v-in_v}.
\tag{13}
\]
On the closed polydisk of radius \(\rho=10^{-2}\), (11) and
\(d_v/L_v\le1\) give, uniformly for complex \(|c|\le1\),
\[
 |\mathcal T_{c,v}|
       \le\frac{2\pi}{630}+\delta\rho<\rho.
\tag{14}
\]
For example the last strict inequality already follows from
\(\pi<22/7\). The total row derivative is at most
\[
 \frac{d_v\delta+d_v\delta}{L_v}\le2\delta<1.
\tag{15}
\]
Hence (13) is a strict contraction in the ordinary maximum norm,
with a constant independent of the graph size. It has exactly one
fixed point in the polydisk. Iteration from zero converges uniformly
in \(c\), so the fixed point is holomorphic for \(|c|<1\).
The strict margin in (14) allows \(|c|\le1+\varepsilon\) for some
positive \(\varepsilon\), proving the stated neighborhood assertion.
The selected value at \(c=0\) is zero.

The sign needed for geometric completion is not inferred from
smallness. Equation (11) rewrites (12) as
\[
 A_v(\boldsymbol\tau)\tau_v=-2\pi ic,\qquad
 A_v=d_v-in_v+\sum_{w\sim v}H(\tau_v,\tau_w).
\tag{16}
\]
For real \(c>0\),
\[
 \operatorname{Re}A_v\ge(1-\delta)d_v>0,\qquad
 \operatorname{Im}\tau_v
       =-\frac{2\pi c\,\operatorname{Re}A_v}{|A_v|^2}<0.
\tag{17}
\]
Moreover \(|A_v|\ge L_v-\delta d_v\), which proves (3).
Every \(\tau_v\) is nonzero for \(c>0\).

This argument allows arbitrary signs of \(n_v\), and \(n_v=0\).
It makes no assumption that neighboring powers are comparable.
The same sign proof works even when a large degree makes the total
meridian logarithm in (4) close to \(-2\pi i\).

## 4. Actual metric and absolute volume

The octahedral chart depends only on the parameters at the ends of
one physical edge. Conditions (3) and (14) keep every such pair in
its proved positive disk. The actual ordered disk seams match
their full complex ratios, including the single prescribed odd seam.
The original cut proof retains every primitive meridian and longitude.
Thus the geometric completion theorem applies to the path just
constructed, rather than to an unrelated solution of exponentiated
gluing equations.

In particular, the actual logarithmic periods start at zero as
\(c\downarrow0\): in a fixed complete peripheral frame the second
fixed point escapes to infinity, and the increments of
\(\log(z-q_v)\) along the fixed generator paths tend to zero.
Their differences from (4) are continuous integers times \(2\pi i\),
and hence vanish along the whole path. The slope in (4) makes one
full primitive turn at \(c=1\). This is the winding information
that exponentiated filling equations alone would not supply.

Let
\[
 \mathcal C(c)=\operatorname*{stat}_{\boldsymbol\tau}
 \left[\Psi+\frac{i}{4\pi}\sum_vn_v\tau_v^2
                         -ic\sum_v\tau_v\right].
\tag{18}
\]
The same actual fundamental chain and primitive period calibration
as in the completion theorem give
\[
             \operatorname{Vol}_c=2\pi\operatorname{Re}\mathcal C(c),
 \qquad
 \frac{d}{dc}\operatorname{Vol}_c
                      =2\pi\sum_v\operatorname{Im}\tau_v(c).
\tag{19}
\]
The complete anchor is the volume of two regular octahedra per
tree edge. Every complementary primitive \(\lambda_v\) represents
the core, of length \(\ell_v=-2\operatorname{Im}\tau_v\).
The estimates above give the explicit bounds
\[
 \frac{4\pi c(1-\delta)d_v}{(L_v+\delta d_v)^2}
 \le\ell_v(c)\le
 \frac{4\pi c(1+\delta)d_v}{(L_v-\delta d_v)^2}.
\tag{20}
\]
If \(S=\sum_vd_v/L_v^2\), integration yields
\[
 \frac{2\pi^2(1-\delta)}{(1+\delta)^2}S
 \le\operatorname{Vol}_0-\operatorname{Vol}_1\le
 \frac{2\pi^2(1+\delta)}{(1-\delta)^2}S.
\tag{21}
\]
Here \(S\) is a useful bound on the volume change, not a hypothesis
for existence or completion.

When the main component is a knot, the independently geometric
preferred-cusp continuation also applies. With the original
oriented writhe \(w_{\mathbf n}\), it gives
\[
 \tau_K=-w_{\mathbf n}-\sum_vn_v+
       2i\sum_{vw}
       \sqrt{1+\tan^2(\tau_v(1)/2)+\tan^2(\tau_w(1)/2)}.
\tag{22}
\]
Its proof uses the actual marked representation and preferred
longitude. Equation (22) is not inferred from a quantum correction.

## 5. A finite criterion with different radii at different vertices

One can keep the local graph data instead of using the common
threshold (1). Choose radii \(0<r_v\le10^{-2}\). Set
\[
 s_v=\sinh(r_v/2),\qquad a_v=\cosh(r_v/2)-1,\qquad
 \omega_{vw}=s_v^2s_w^2.
\tag{23}
\]
The same derivative calculation gives
\[
 \begin{split}
 \alpha_{vw}
 &=\frac{a_v+a_w}{(1-a_v)\sqrt{1-\omega_{vw}}}
          +\frac1{\sqrt{1-\omega_{vw}}}-1,\\
 \beta_{vw}
 &=\frac{s_vs_w}{\sqrt{1-\omega_{vw}}},
 \end{split}
\tag{24}
\]
as bounds for \(|E_t|\) and \(|E_u|\) on the corresponding
bidisk. Put \(h_v=\sum_{w\sim v}\alpha_{vw}\).
The following finite inequalities suffice:
\[
 \begin{split}
 &2\pi+h_vr_v<L_vr_v,\qquad h_v<d_v,\\
 &\max_v\left[
       \frac{h_v}{L_v}
       +\sum_{w\sim v}\frac{\beta_{vw}r_w}{L_vr_v}\right]<1.
 \end{split}
\tag{25}
\]
The first line makes (13) preserve the product of the vertex disks
and gives the sign in (17). The second is a contraction bound in
the weighted norm \(\max_v|\tau_v|/r_v\).
The proof of Sections 3--4 applies unchanged, with
\[
 |\tau_v(c)|\le\frac{2\pi c}{L_v-h_v}.
\tag{26}
\]
This is a finite numerical certificate in the integer degrees and
powers and the chosen positive radii. All quantities can be bounded
by rational Taylor enclosures; it does not assume the existence of
a saddle or a geometric representation.

More generally, the second line of (25) can be replaced by a
positive-vector certificate for the derivative matrix with diagonal
entries \(h_v/L_v\) and off-diagonal entries \(\beta_{vw}/L_v\).
If a positive vector \(q\) and a number \(\kappa<1\) satisfy
\(Mq\le\kappa q\), contraction holds in the \(q\)-weighted norm.
The invariant polydisk is still supplied separately by the first
line of (25). Thus choosing the contraction norm does not change
the geometric parameter region.

## 6. What this extends, and what remains separate

The global condition \(S\le2^{-25}\) implies (1), but the converse
fails on arbitrarily large trees. For instance on paths with powers
chosen from \(630,631\), every degree is at most two and (1) holds,
whereas \(S\) grows linearly with the number of vertices.
Choose the original parity pattern by the finite knot-component
test when a knot is required. The vertexwise criterion also permits
a zero power at any vertex of degree at least \(630\), together
with other powers satisfying their own local inequalities.

These examples concern the arithmetic hypotheses and the supplied
actual diagram. They do not assert an unrestricted classification
of small-slope fillings. The explicit positive radius is a sufficient
chart, not the maximal positivity domain of the octahedra.

The earlier quantum proof discards some parts of the source with a
fixed absolute loss and then compares that loss with the total
change of the critical action. The total change in (21) can grow
with the size of a tree satisfying (1). Consequently this geometric
theorem alone does not supply the earlier source dominance or a
new volume-conjecture conclusion. The [local subtree argument](actual_all_circle_local_message_volume.md)
provides such a quantum comparison under the stronger condition
\(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\). The geometric condition
\(L_v\ge630\) alone does not prove that quantum conclusion.
