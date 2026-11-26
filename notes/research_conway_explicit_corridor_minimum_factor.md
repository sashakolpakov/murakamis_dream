# An explicit corridor factor for the quartic Conway minimum

Research proof, 23 November 2026.

The original quartic minimum differs from an explicit multiple of the
original squared source by an exponentially small relative error. The
factor uses only the known closing row and the turns above the highest
product. No unknown internal response appears in it. This does not
evaluate the minimum or establish its geometric rate.

## 1. The original minimum and the known factor

Use the full normalized Conway compiler of [C], with its prescribed
leaves, products, turns and original closing. At every level \(N\ge2\),
all packets belong to the full Newton space, including its Hermite
directions. Put

\[
 \sigma=\frac1{16},\qquad
 E(x)=\sum_v\|\Phi_v(x_{\rm children})-x_v\|^2
                                      +|Lx_{\rm top}|^2,
 \qquad e_* =\min_{\|x_v\|\le1}E(x).
 \tag{1}
\]

The actual normalized forward field is \(a\), and

\[
 \|a_v\|\le\sigma,\qquad
 k=La_{\rm top}=K_N/B_{\rm tot},\qquad
 L=\chi\lambda_\varepsilon/b_\rho,
 \quad \varepsilon\in\{0,N-1\}.
 \tag{2}
\]

Every physical budget remains the original

\[
 b_v=16\max(1,\|T_v\|_{\rm HS}),
 \qquad \Phi_v=M/b_v\ \text{or }J/b_v.
 \tag{3}
\]

Suppose first that the tree has a product. Starting at the closing,
let \(v_*\) be the highest product. Its output is followed by turns
with normalized maps \(A_1,\ldots,A_m\), ordered upward. Thus the
proper corridor consists of the output of \(v_*\) and those \(m\)
turn outputs. Set

\[
 P_i=A_m\cdots A_{i+1}\quad(0\le i\le m),
 \quad P_m=I,\quad b_i=LP_i,
 \quad C=1+\nu_{\rm corr},\quad
 \nu_{\rm corr}=\sum_{i=0}^m\|b_i\|^2.
 \tag{4}
\]

The \(b_i\) in (4) are rows, distinct from the vertex budgets \(b_v\).
All terms in (4) are known physical data. If the turn budgets in
upward order are \(\beta_1,\ldots,\beta_m\), then explicitly

\[
 \nu_{\rm corr}
   =\frac{|\chi|^2}{b_\rho^2}
           \sum_{i=0}^m\prod_{j=i+1}^m\beta_j^{-2},
 \qquad 1\le C\le\frac{256}{255}.
 \tag{5}
\]

The bound follows from \(\|L\|\le\sigma\) and
\(\|A_j\|\le\sigma\). Empty products have value one.

Write

\[
 \eta=\frac{\chi}{b_\rho\prod_{j=1}^m\beta_j},
 \qquad \zeta=\frac{|\eta|}{b_{v_*}}.
 \tag{6}
\]

The endpoint identities of [G] give, with no conjugation in the
bilinear form,

\[
 LP_0\Phi_{v_*}(u,w)=u^{\mathsf T}Bw,
 \qquad B=\frac{\eta}{b_{v_*}}J
       \ \text{or }\frac{\eta}{b_{v_*}}e_0e_0^{\mathsf T},
 \qquad \|B\|=\zeta.
 \tag{7}
\]

This includes both original endpoint closings and every parity of
the turn corridor. In particular, the true field satisfies
\(|k|\le\sigma^2\zeta\).

**Theorem.** With the known \(C,\zeta\) above,

\[
 \boxed{\quad
 \left(1-\frac{\zeta^2}{82C}\right)\frac{|k|^2}{C}
          \ \le e_*\le\frac{|k|^2}{C}.
 \quad}
 \tag{8}
\]

Equivalently, preserving the original budget and scalar,

\[
 C B_{\rm tot}^2 e_*\le |K_N|^2
       \le\frac{C B_{\rm tot}^2 e_*}
                       {1-\zeta^2/(82C)}.
 \tag{9}
\]

These inequalities include \(K_N=0\). If there is no product, put
\(\zeta=0\), define the corridor to be the whole proper chain and define \(C\) by (4)
for that chain. Then

\[
                          e_*=|k|^2/C
 \tag{10}
\]

exactly. If \(\chi=0\), both sides of (8)--(10) vanish.

In particular the explicitly rescaled minimum
\(\widetilde Q_N=C B_{\rm tot}^2e_*\) satisfies

\[
 \left(1-\frac{\zeta^2}{82C}\right)|K_N|^2
                         \le\widetilde Q_N\le|K_N|^2.
 \tag{10a}
\]

The variational presentation and its budgets depend on the chosen
compiler. Equation (10a) compares that presentation to the unchanged
original source; it does not assert that the minimum is itself a
topological invariant.

## 2. Exact elimination of the final linear corridor

Keep every packet below \(v_*\) as a variable \(u\). For fixed feasible
\(u\), put \(f=\Phi_{v_*}(u_L,u_R)\). Write \(y_0\) for the output
of \(v_*\), and \(y_1,\ldots,y_m\) for the turn outputs. The part of
(1) involving these variables is exactly

\[
 \|y_0-f\|^2+\sum_{i=1}^m\|y_i-A_i y_{i-1}\|^2
                                                    +|Ly_m|^2.
 \tag{11}
\]

Set \(r_0=y_0-f\) and \(r_i=y_i-A_i y_{i-1}\). Then

\[
 Ly_m=s+\sum_{i=0}^m b_i r_i,\qquad s=LP_0f.
 \tag{12}
\]

The unconstrained least-squares minimum and its residuals are

\[
 \min_r\left\{\sum_i\|r_i\|^2+
                      \left|s+\sum_i b_i r_i\right|^2\right\}
       =\frac{|s|^2}{C},\qquad r_i=-b_i^*s/C.
 \tag{13}
\]

For example, substitution gives the value in (13), and the
stationary equations are \(r_i+b_i^*(s+\sum_jb_jr_j)=0\).
The positive identity term makes that stationary point unique.

The original corridor ball constraints do not alter this minimum.
Indeed, with feasible \(u\) fixed, (11) is a strictly positive
quadratic in the corridor packets. Its half-gradient step is the
corresponding component of the full step of [C]. That step maps
every corridor packet ball into its \(33/256\) ball and contracts
by at most \(1/2\). Its fixed point is therefore feasible, interior
and stationary for the unconstrained quadratic. It is the unique
minimum in (13).

Consequently exact partial minimization of (1) gives

\[
 F(u)=R(u)+|g(u)|^2,\qquad
 g(u)=\frac{u_L^{\mathsf T}Bu_R}{\sqrt C},
 \qquad \min F=e_*.
 \tag{14}
\]

Here \(R\ge0\) is the sum of the unchanged residuals below the
corridor. For the corresponding part \(u_a\) of the true field,

\[
 R(u_a)=0,\qquad DR(u_a)=0,\qquad
 g(u_a)=k/\sqrt C,\qquad F(u_a)=|k|^2/C.
 \tag{15}
\]

All omitted coefficients have been eliminated, rather than projected
to semisimple values. Formula (13) is the familiar root-corridor
least-squares formula; the quantitative improvement below concerns
how much further internal minimization can lower (15).

## 3. Further minimization has an exponentially small relative effect

The more explicit Hessian estimate proved in [C] is

\[
                         D^2E\succeq\frac{41}{32}I.
 \tag{16}
\]

The partial minimum \(F\) inherits the same lower bound. To see this,
its eliminated quadratic minimizer is smooth in \(u\), and its Hessian
is the Schur complement of the full Hessian at that minimizer.
For every variation \(h\),

\[
 D^2F(u)[h,h]
    =\min_j D^2E(u,y_*(u))[(h,j),(h,j)]
                         \ge\frac{41}{32}\|h\|^2.
 \tag{17}
\]

The smooth formula extends to the closed feasible balls. Thus the
strong-convexity minorant, minimized over all real variations, gives

\[
 e_*\ge F(u_a)-\frac{16}{41}\|\nabla F(u_a)\|^2.
 \tag{18}
\]

Only the two immediate inputs of \(v_*\) occur in \(g\). At the true
field both have norm at most \(\sigma\). Therefore, in the original
coefficient metric,

\[
 \|Dg(u_a)\|^2
     \le\frac{\|B\|^2}{C}
                (\|(u_a)_L\|^2+\|(u_a)_R\|^2)
     \le\frac{2\sigma^2\zeta^2}{C}.
 \tag{19}
\]

The derivatives and gradients in (16)--(19) are real derivatives for
\(\operatorname{Re}\sum x_v^*y_v\). A complex-linear scalar row has
the same operator norm in these real coordinates. Using (15),

\[
 \|\nabla F(u_a)\|^2
   =\|2(Dg(u_a))^*g(u_a)\|^2
   \le\frac{8\sigma^2\zeta^2}{C}F(u_a).
 \tag{20}
\]

Substituting into (18), and using \(\sigma^2=1/256\), proves

\[
 e_*\ge\left(1-\frac{128\sigma^2\zeta^2}{41C}\right)F(u_a)
       =\left(1-\frac{\zeta^2}{82C}\right)F(u_a).
 \tag{21}
\]

The competitor \(u_a\) gives the reverse inequality \(e_*\le F(u_a)\).
This proves (8). If \(k=0\), (15) directly gives \(e_*=0\), so no
division by \(k\) is needed. With no product there is no remaining
variable \(u\), and (13) gives (10).

Finally, [G] gives the all-level estimate and its large-level rate

\[
 \zeta\le\frac1{256\max(1,\|M\|_{\rm HS})},\qquad
 \zeta\le\exp\left\{-\frac{2G_{\rm Cat}}\pi N+O(\log N)\right\}.
 \tag{22}
\]

Here \(G_{\rm Cat}=\int_0^{\pi/4}\log(\cot t)\,dt\). Thus the
relative loss in (8) is at most

\[
 \frac{\zeta^2}{82C}
       \le\exp\left\{-\frac{4G_{\rm Cat}}\pi N+O(\log N)\right\}.
 \tag{23}
\]

## 4. Prescribed leaves and smaller quartics

Suppose the feasible set for (14) is further restricted to a set
containing \(u_a\), and let \(e_{\rm cl}\) be its minimum. Then
the same comparison holds:

\[
 \left(1-\frac{\zeta^2}{82C}\right)\frac{|k|^2}{C}
           \le e_*\le e_{\rm cl}\le\frac{|k|^2}{C}.
 \tag{24}
\]

Indeed restriction gives the middle inequality, and the feasible
competitor \(u_a\) gives the last one. Exact elimination of any remaining
linear variables preserves that restricted minimum.

This includes the prescribed-leaf restriction in [B]: the fixed inputs
are the known leaf packets transported through their turn corridors,
and the true field obeys those restrictions. Eliminating the final
corridor at the same time is feasible, because none of its packets is
one of those fixed inputs. Thus (24) applies to the smaller quartic
on the connections between binary products, with its original budgets.
No unknown binary output is fixed in making this restriction.

Consequently \(C B_{\rm tot}^2e_{\rm cl}\) also obeys (10a). This
asserts the stated comparison, rather than equality between the
unrestricted and restricted numerical minima.

## 5. What has and has not been reduced

The leading comparison factor \(C\) is an explicit finite sum of
known corridor budgets. It requires neither the full forward field
nor its backward response. All other internal optimization can
change the corresponding value only by the relative amount in (8).
The proof may use the true field as a competitor without inserting
that unknown field into the definition of \(C\), \(E\), or the
original source.

This improves the fixed constant source comparison of [C] and removes
the unknown response coefficient from the leading comparison in [S].
It does not turn evaluation of \(e_*\) into a scalar secular equation.
The coherent value or a positive geometric lower witness for that
minimum is still required. The original marking, scalar \(\chi\),
budget product, and every physical Hermite direction remain present.
No finite-exception theorem or new filling class follows.

The literal product/turn tree and its original endpoint closing are
essential. General precomposed unary maps or shared descendants need
their own estimates; none is silently treated as a unitary turn.

## Complete inputs and comparison

The following four complete matching texts were read. The exact
corridor calculation is written in full above; [C] supplies its
inactive balls and Hessian bound, and [G] supplies the endpoint
contraction and quantitative rate. The complete binary-skeleton note
[B] supplies the prescribed-leaf restriction used in Section 4 and
already gives the exact corridor elimination. The complete scalar-response
note [S] was read for coverage; it retains an internal response in its
leading scalar comparison. The new assertion here is the explicit
exponentially small relative loss in (8) and (24).

- [C] [Normalized original source](research_convex_normalized_conway_source.md), SHA-256 `6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c`.
- [G] [Global closing curvature](research_conway_global_closing_curvature.md), SHA-256 `863f170da9a9017aa8b83b1ace44ee3e2c851f57c806c77678b3699e3f2f305f`.
- [B] [Binary-skeleton quartic](research_conway_binary_skeleton_quartic.md), SHA-256 `294220039d913fd349b867f9705670215c3ca98f581461c6f406db0dac20c7a3`.
- [S] [Scalar cap response](research_conway_scalar_cap_response.md), SHA-256 `6b9b73ae429713bdff63120a9841c06d2311d249f058f3da6b1f4e89dbfaecfb`.

Only written mathematics and text/hash operations were used. No earlier
final, manuscript or public document was edited.
