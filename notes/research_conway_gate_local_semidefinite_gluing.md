# Convex gate energies and semidefinite gluing along the Conway tree

21 November 2026. Research note; earlier finals and public manuscripts
remain unchanged.

A fixed quadratic redistribution makes every gate energy jointly
strongly convex. The redistributed terms still sum to the original
source energy. This gives an exact semidefinite formulation using one
matrix block per gate and only the first moments of shared boundary
packets. Equivalently, affine boundary forces suffice for exact dual
assembly.

A connected short component has a jointly convex shifted boundary
energy with an exact semidefinite epigraph. Its original complex
coefficients and every boundary coordinate remain present. These
statements do not construct certificates at the hyperbolic volume rate.

## 1. The actual source and a quadratic redistribution

Use the normalized actual compiler of the
[convex source theorem](research_convex_normalized_conway_source.md).
Fix a level \(N\ge2\). Each proper vertex \(v\) carries the full
packet \(x_v\in H_N\),
with \(2N\) real coordinates, including the repeated-root directions.
A local map \(\Phi_v\) is a prescribed leaf, a linear turn, or the
original bilinear Newton product. Its recorded Hilbert--Schmidt
normalization gives norm at most \(\sigma=1/16\). The closing
root \(\rho\) has one child \(v_0\) and retains the original
normalized closing row \(L\).

Write
\[
 C_v=\{v\}\cup\{w:w\text{ is a child of }v\}
       \quad(v\ne\rho),\qquad C_\rho=\{v_0\}.                 \tag{1}
\]
These sets, called bags below, contain all real and imaginary
coordinates of their listed packets. Every proper bag has at most
\(6N\) real variables. Put
\[
 g_w=1-\|x_w\|^2,\qquad
 E_v=\|\Phi_v((x_w)_w)-x_v\|^2,\qquad
 E_\rho=|Lx_{v_0}|^2,\qquad E=\sum_vE_v.                       \tag{2}
\]
The original feasible set is the product of unit balls \(g_w\ge0\).
Its minimum \(e_*\) is attained at a unique interior field \(a_*\),
and the original marked source satisfies
\[
 B_{\rm tot}^2e_*\le |K_N|^2
                    \le\frac{197}{196}B_{\rm tot}^2e_* .        \tag{3}
\]
The known budget product \(B_{\rm tot}\) is unchanged here.

Fix \(t=1/4\). Define
\[
 V_v=E_v-t\|x_v\|^2+t\sum_{w\text{ child of }v}\|x_w\|^2
                      \quad(v\ne\rho),\qquad
 V_\rho=E_\rho+t\|x_{v_0}\|^2.                                \tag{4}
\]
Every proper variable occurs once with each sign, so
\[
                                \sum_vV_v=E.                  \tag{5}
\]
The \(V_v\) need not be nonnegative. For a prescribed leaf packet
\(b\), its minimum is
\(-t\|b\|^2/(1-t)\), attained at \(x=b/(1-t)\).
Thus all local constants must be retained when lower bounds are
assembled.

A proper bag and its parent bag intersect exactly in the one packet
\(x_v\). That packet occurs in these two bags and nowhere else.
This follows directly from a literal tree with distinct child
occurrences. No identification of boundary variables is suppressed.

## 2. A local Hessian certificate

For a bag \(C\), let \(Q_2(C)\) consist of
\[
 q=s_0+\sum_{w\in C}g_ws_w,                                    \tag{6}
\]
where \(s_0\) is a sum of squares of real polynomials of degree at
most two on \(C\), and each \(s_w\) is a sum of squares of
degree-at-most-one polynomials on \(C\). Absolute squares of
complex polynomials mean the sum of their real and imaginary squares.

Set \(\mu=31/128\).

**Lemma.** Every \(V_v\) is jointly \(\mu\)-strongly convex on its
bag's product of unit balls. More precisely, its real Hessian has a
certificate
\[
 h^{\mathsf T}(D^2V_v(x)-\mu I)h
   =\sum_\nu|W_{v\nu}(x)h|^2+
                  \sum_{w\in C_v}g_w(x)h^{\mathsf T}A_{vw}h,   \tag{7}
\]
where the matrices \(W_{v\nu}\) are affine in the local variables
and the matrices \(A_{vw}\) are constant positive semidefinite.
All terms use only \(C_v\).

**Proof.** We use the local square completions (6)--(8) in the
[degree-four certificate proof](research_conway_degree_four_semidefinite_certificate.md).
Their tensor coefficient bounds use the Hilbert--Schmidt norm and
are unchanged by reshuffling complex indices.

At a product write the output as \(x_0\), the inputs as \(x_1,x_2\),
and the normalized bilinear map as \(B\). Its half-Hessian is
\[
\begin{split}
 \tfrac12D^2V_v[h,h]={}&
 (1-t)\|h_0\|^2+t(\|h_1\|^2+\|h_2\|^2)\\
 &-2\operatorname{Re}\langle h_0,
                     B(h_1,x_2)+B(x_1,h_2)\rangle\\
 &+\|B(h_1,x_2)+B(x_1,h_2)\|^2\\
 &+2\operatorname{Re}\langle B(x_1,x_2),B(h_1,h_2)\rangle
             -2\operatorname{Re}\langle x_0,B(h_1,h_2)\rangle .
\end{split}                                                     \tag{8}
\]
The two derivative cross terms consume constant allowances
\(2\sigma\|h_0\|^2+\sigma(\|h_1\|^2+\|h_2\|^2)\).
The last two curvature terms consume, respectively,
\(\sigma^2(\|h_1\|^2+\|h_2\|^2)\) and
\(\sigma(\|h_1\|^2+\|h_2\|^2)\).
In each case the exact remainder is a sum of squares plus the
original ball constraints times constant positive semidefinite
quadratic forms in \(h\), by the cited local identities.
The already positive squared norm in (8) is retained. Consequently
\[
 \tfrac12D^2V_v[h,h]\ \ge\
  (1-t-2\sigma)\|h_0\|^2+
                 (t-2\sigma-\sigma^2)(\|h_1\|^2+\|h_2\|^2)
 =\frac58\|h_0\|^2+\frac{31}{256}(\|h_1\|^2+\|h_2\|^2),       \tag{9}
\]
with exactly that polynomial certificate for the difference.

At a turn, the same linear square completion gives coefficients
\(1-t-\sigma=11/16\) at the output and \(t-\sigma=3/16\)
at its child in the half-Hessian. A leaf has half-Hessian
\((1-t)I\). The root has half-Hessian at least \(tI\).
All exceed \(\mu I/2\). The unused constant diagonal forms are
sums of squares. This proves (7), including its local support.
\(\square\)

The conclusion is joint convexity in the actual full packet variables.
It is not joint convexity of the unshifted squared residual at a
product gate.

For any feasible local center \(b\), integrating (7) along
\(b+\theta(x-b)\), \(0\le\theta\le1\), gives
\[
 V_v(x)-V_v(b)-\nabla V_v(b)\cdot(x-b)
                     -\frac\mu2\|x-b\|^2\in Q_2(C_v).          \tag{10}
\]
Indeed each square integrates to a positive semidefinite Gram form
of degree at most four. For a ball term use
\[
 g_w(b+\theta(x-b))
  =(1-\theta)g_w(b)+\theta g_w(x)
                    +\theta(1-\theta)\|x_w-b_w\|^2.
\]
Its three integrated pieces are a sum of squares, a ball times a
quadratic sum of squares, and a degree-four sum of squares.
This is the same elementary degree-preserving integration as in
the direct certificate proof. The center can be on the boundary:
\(g_w(b)\ge0\) suffices.

## 3. Local semidefinite moments and only first-moment matching

At each bag introduce a real linear functional \(\mathcal L_v\)
on its polynomials of degree at most four. Impose
\[
 \mathcal L_v(1)=1,\quad
 \mathcal L_v(f^2)\ge0\quad(\deg f\le2),\quad
 \mathcal L_v(g_wf^2)\ge0
                 \quad(w\in C_v,\ \deg f\le1).                  \tag{11}
\]
These are the usual moment and localizing matrix conditions.
On an edge to a proper vertex \(v\), match only
\[
                    \mathcal L_v(x_v)
                  =\mathcal L_{\operatorname{parent}(v)}(x_v)
                            \quad\text{in }\mathbb R^{2N}.      \tag{12}
\]
No higher shared moment is required.

For each local functional its mean \(m_v=\mathcal L_v(x_{C_v})\)
lies in the bag's product of balls. In fact positivity gives
\(\|\mathcal L_v(x_w)\|^2\le\mathcal L_v(\|x_w\|^2)\le1\).
Apply (10) at this feasible mean. The linear term has zero value,
so
\[
 \mathcal L_v(V_v)\ge V_v(m_v)
           +\frac\mu2\mathcal L_v(\|x_{C_v}-m_v\|^2)
                                   \ge V_v(m_v).               \tag{13}
\]
This is a direct Jensen inequality for these truncated moments;
no representing measure is assumed.

By (12), the local means form one feasible global packet field \(m\).
Equations (5) and (13) therefore prove the exact formulation
\[
 \boxed{\quad
 e_*=\min_{\{\mathcal L_v\}\text{ satisfying }(11),(12)}
                                          \sum_v\mathcal L_v(V_v).
 \quad}                                                        \tag{14}
\]
The lower bound follows from
\(\sum_v\mathcal L_v(V_v)\ge\sum_vV_v(m)=E(m)\ge e_*\).
Evaluation at the restrictions of \(a_*\) is feasible and gives
equality. Thus the minimum is attained. Any optimal family has
the correct global first moments and zero second-moment deviations
in every bag, by (13) and uniqueness of the source minimizer.
Higher moment uniqueness is not needed.

The objective in (14) uses the redistributed \(V_v\). Its quadratic
shifts need not cancel across arbitrary local functionals, since
their second moments are not matched. Identity (5) is applied to the
consistent mean field in the lower-bound proof. Replacing that objective
by \(\sum_v\mathcal L_v(E_v)\) under first-moment matching alone is
not part of the theorem.

The largest moment or free Gram block has size at most
\[
                              \binom{6N+2}{2},                  \tag{15}
\]
and each localizing block has size at most \(6N+1\).
There are linearly many blocks in the number of gates.
The separator conditions are just \(2N\) real equalities per edge.
These are size bounds for this representation, not claims about
exact-arithmetic running time or relative precision.

## 4. Affine boundary forces give an exact dual

For each proper vertex choose a real force
\(p_v\in\mathbb R^{2N}\) on its full boundary packet, and let
\[
 \begin{split}
 F_v(x;p)&=V_v(x)-p_v\cdot x_v
                         +\sum_{w\text{ child of }v}p_w\cdot x_w,
                                      &&v\ne\rho,\\
 F_\rho(x;p)&=V_\rho(x)+p_{v_0}\cdot x_{v_0}.
 \end{split}                                                    \tag{16}
\]
Their sum is still exactly \(E\). Introduce one real constant
\(\alpha_v\) per bag and impose the local conditions
\[
                         F_v(\,\cdot\,;p)-\alpha_v\in Q_2(C_v).
                                                                 \tag{17}
\]
Any such forces, constants and Gram matrices give the source lower bound
\[
                         |K_N|^2\ge B_{\rm tot}^2\sum_v\alpha_v .
                                                                 \tag{18}
\]
The constants can be negative and must be summed with their signs.

The maximum of \(\sum_v\alpha_v\) under (17) is \(e_*\),
and is attained. To prove the nontrivial direction, use global
stationarity at the actual interior minimizer and choose
\[
                   p_v=\partial_{x_v}V_v(a_*)                 \tag{19}
\]
at each proper vertex, with real derivatives. The global stationary
equation at a child says
\(\partial_{x_w}V_v(a_*)+p_w=0\); at the top it gives the analogous
root equation. Thus every force-adjusted \(F_v\) has zero gradient
at \(a_*|_{C_v}\). Put
\(\alpha_v=F_v(a_*|_{C_v};p)\).
Certificate (10) proves (17), and the forces cancel to give
\(\sum_v\alpha_v=E(a_*)=e_*\).

For fixed forces, even the local best constant in (17) is exact.
Indeed let \(b\) minimize the jointly strongly convex \(F_v\)
on the bag balls. In an interior packet its gradient block is zero.
At a boundary packet it is \(-2\beta_wb_w\) for some
\(\beta_w\ge0\): tangent derivatives vanish, and the inward derivative
is nonnegative. These statements follow by varying one packet at a
time. Also \(\beta_wg_w(b)=0\). Hence
\[
 \nabla F_v(b)\cdot(x-b)
        =\sum_w\beta_wg_w(x)+\sum_w\beta_w\|x_w-b_w\|^2.        \tag{20}
\]
Combining (20) with (10) proves
\(F_v-\min F_v\in Q_2(C_v)\).
Thus the local semidefinite minimizations for specified forces do not
use the global minimizer. It is used in (19) only to prove that the
global dual attains the exact value.

## 5. Exact convex boundary energy for a connected short component

Let \(\Omega\) be a nonempty connected set of proper gate vertices.
It has a top output \(y\) and one packet \(u_j\) at every child
edge entering from outside. Clamp these boundary packets in their
unit balls, and minimize over the other outputs in \(\Omega\).
Let \(C_\Omega(u,y)\) be the minimum of the unshifted residual sum
\(\sum_{v\in\Omega}E_v\). All these are the original normalized
gates with their original budgets.

The redistributed boundary value is
\[
 \boxed{\quad
 \widetilde C_\Omega(u,y)
       =C_\Omega(u,y)+t\sum_j\|u_j\|^2-t\|y\|^2
       =\min_{\rm internal}\sum_{v\in\Omega}V_v .
 \quad}                                                        \tag{21}
\]
The equality follows by cancellation of internal quadratic terms.
Every variable of this block occurs in at least one of its bags.
Consequently \(\sum_{v\in\Omega}V_v\) is jointly
\(\mu\)-strongly convex in all its boundary and internal variables.
Partial minimization preserves the same modulus on the joint boundary:
interpolate the two internal minimizers along with their boundary
data, apply the strong-convexity inequality, and drop the nonnegative
squared internal displacement. Thus
\(\widetilde C_\Omega\) is jointly \(\mu\)-strongly convex on
its product of boundary balls.

This boundary function has an exact semidefinite epigraph.
Use one local functional per bag in \(\Omega\), satisfying
(11) and first-moment matching on internal edges. Prescribe the
boundary first moments to be \(u,y\), and impose
\[
                              s\ge\sum_{v\in\Omega}\mathcal L_v(V_v).
                                                                 \tag{22}
\]
For any such list, (13) gives a feasible mean field with cost at least
\(\widetilde C_\Omega(u,y)\). Conversely evaluation at the unique
internal minimizer realizes equality in that bound, and (22) allows
every larger \(s\). Therefore the projection onto \((u,y,s)\)
is exactly
\[
             \{(u,y,s):\text{boundary packets in their balls},
                                   \ s\ge\widetilde C_\Omega(u,y)\}.
                                                                 \tag{23}
\]
This is a linear projection of an affine semidefinite feasible set,
with moment order still equal to two.

One may replace any collection of disjoint connected short components
by these convex boundary functions, leaving all shared boundary packets
and uncovered gates. Exact partial minimization preserves \(e_*\).
The quadratic boundary redistributions cancel when components are
assembled. There is no additional comparison factor and no assertion
that the unshifted \(C_\Omega\) is jointly convex.

A block containing the closing root is handled by the same construction,
with its scalar output fixed and only the incoming cut packets left
as boundary variables. The root term is \(V_\rho\); there is no
negative outgoing quadratic term. The same local Jensen and epigraph
proof applies.

## 6. The remaining geometric lower bound

All gate conditions in (17) use known local tensors, affine forces
and finite positive semidefinite matrices. They can be checked without
an unknown invariant. Fixed short pieces can be retained through
their exact convex boundary relation (23). These are source-preserving
algebraic gluing rules for arbitrarily large fixed Conway trees.

No Casson--Rivin construction of the forces or Gram matrices has been
proved. For the proposed volume identity one still needs feasible
certificates whose positive total \(\sum_v\alpha_v\), after restoring
\(B_{\rm tot}^2\), has the hyperbolic volume rate, and a matching upper
bound. Real angle balance has not been shown to imply these
full-coordinate quantum inequalities.

## Sources and coverage

Both complete matching proof sources were read:

| Source | SHA-256 |
|---|---|
| [Degree-four source certificate](research_conway_degree_four_semidefinite_certificate.md) | 8b706c7e08aa124ce5d80c2401511a3be67a09b1878b0adfd4ec989514cf44db |
| [Normalized original source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

Sparse sum-of-squares programs and the running-intersection condition
are established techniques; see the primary records of
[Waki--Kim--Kojima--Muramatsu](https://epubs.siam.org/doi/abs/10.1137/050623802)
and [Lasserre](https://epubs.siam.org/doi/abs/10.1137/05064504X).
Those coverage records were checked. Their proofs are not used here.
The specific assertion proved above is exactness at degree four with
first-moment gluing for the redistributed physical tree energy.
No novelty is claimed for sparse semidefinite methods themselves.

Only written mathematics, coverage lookup and text/hash operations were
used. No mathematical program, test, numerical optimization, build,
git operation or previous-final edit was performed.

