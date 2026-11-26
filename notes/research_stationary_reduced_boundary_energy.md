# Stationary reduction and a compositional boundary energy

Research deduction, 6 November 2026. A negative Hermitian real part
survives complex stationary elimination. That Schur-complement fact
already appears in the [fixed-domain turn theorem](research_fixed_domain_long_power_turns.md)
and [edge-response calculation](research_edge_hessian_and_phase_response.md).
The additional conclusion here is an exact finite-difference boundary
energy law. Energies add under stationary gluing, including at a
branching vertex, and the original imaginary quadratic filling terms
contribute zero to this energy. It therefore supplies a compositional
version of the centered correction in
[signed boundary compensation](research_stationary_reference_signed_boundary_compensation.md).

The phase domains, original logarithmic lifts and stationary branches
remain hypotheses. Energy closure is an upper-bound mechanism; it
does not construct a contributing cycle or prove a nonzero observed
coefficient for arbitrary short tangles.

## 1. The exact reduced Hessian and its energy

Let \(F(q,b)\) be holomorphic in internal variables
\(q\in\mathbb C^k\) and boundary variables \(b\in\mathbb C^l\).
Suppose a specified holomorphic branch \(q=q(b)\), on a boundary
domain \(G\), obeys the original equations \(F_q=0\).
The internal Hessian block is assumed invertible along the branch.
Write
\[
 H=F''=\begin{pmatrix}H_{qq}&H_{qb}\\H_{bq}&H_{bb}\end{pmatrix},
 \quad \phi(b)=F(q(b),b),\quad p(b)=F_b(q(b),b),
 \quad Q=-\frac{H+H^*}{2}=-\Re H.
 \tag{1}
\]
Here \(H^*\) is the adjoint. The last equality uses complex symmetry
of a holomorphic Hessian; \(\Re H\) denotes entrywise real part.
No conjugate is introduced into the original stationary equations.

**Proposition 1.** Set
\[
 T=\begin{pmatrix}-H_{qq}^{-1}H_{qb}\\I\end{pmatrix},
 \qquad S=H_{bb}-H_{bq}H_{qq}^{-1}H_{qb}.
 \tag{2}
\]
Then \(\phi'=p\), \(\phi''=S\), and the following identity of
Hermitian forms is exact:
\[
                  -\Re S=T^*QT.
 \tag{3}
\]
Consequently \(Q\succeq0\) implies \(-\Re\phi''\succeq0\).
If \(Q\succeq\mu I\), then
\[
            -\Re\phi''\succeq\mu T^*T\succeq\mu I.
 \tag{4}
\]
More generally, a retained diagonal bound
\(Q\succeq\operatorname{diag}(0,W)\), \(W\succeq0\), gives
\(-\Re\phi''\succeq W\).

*Proof.* Differentiate \(F_q(q(b),b)=0\) and then differentiate
the original stationary value. This gives (2) and \(\phi'=F_b\).
The matrix identity \(HT=(0,S)^T\) implies \(T^*HT=S\).
Taking Hermitian parts proves (3), including (4) and the retained
diagonal assertion. In particular this is not elimination of
\(\Re H\) in place of the complex matrix \(H\). \(\square\)

Strict positivity of the internal block of \(Q\) is sufficient
for invertibility of \(H_{qq}\). Semidefiniteness alone is not.
When \(Q\succeq0\), (3) also identifies the reduced null space:
\(\xi\in\ker(-\Re S)\) if and only if \(T\xi\in\ker Q\).
Thus elimination preserves any genuine unremoved radical rather
than making it positive.

Define the boundary energy of two states in this branch by
\[
 \mathcal E_\phi(b_1,b_0)
   =-\Re\{[p(b_1)-p(b_0)]\cdot\overline{b_1-b_0}\}.
 \tag{5}
\]
The dot is the original bilinear coordinate pairing. If the boundary
segment \(b_t=b_0+t(b_1-b_0)\) stays in \(G\) and \(Q\succeq0\)
on its stationary graph, then, for \(\delta b=b_1-b_0\),
\[
 \mathcal E_\phi(b_1,b_0)
 =\int_0^1 (T(b_t)\delta b)^*Q(q(b_t),b_t)
                         (T(b_t)\delta b)\,dt\ge0.
 \tag{6}
\]
In particular (4) gives \(\mathcal E_\phi\ge\mu|\delta b|^2\).
This proves injectivity of \(p\) on a convex \(G\) in the strictly
coercive case; it does not prove existence of a stationary branch.

There is a useful alternative that requires no stationary graph along
the boundary segment. Put \(r_i=(q_i,b_i)\), where both endpoints
satisfy \(F_q(r_i)=0\). If the full straight segment between them
lies in a holomorphic domain with \(Q\succeq0\), then
\[
 \mathcal E_F(r_1,r_0)
 :=-\Re\{[F'(r_1)-F'(r_0)]\cdot\overline{r_1-r_0}\}
 =\mathcal E_\phi(b_1,b_0)
 =\int_0^1\delta r^*Q(r_0+t\delta r)\delta r\,dt\ge0.
 \tag{7}
\]
The middle equality only uses stationarity at the endpoints. The
interpolating full configurations need not be stationary. Formula
(7) remains valid when the two endpoints are given directly, without
first extending them to a common boundary graph.

## 2. Gluing, real incidence maps and signed filling quadratics

Consider finitely many phases \(F_v(x_v)\), in their specified
original coordinates and lifts. Let \(x\) collect all assembled
coordinates, and identify the local coordinates by
\(x_v=P_vx+a_v\), where each \(P_v\) is a constant real matrix
and \(a_v\) is a fixed complex vector. Real signed incidence matrices
include repeated ports and orientation reversals. Retain the full
assembled phase
\[
 \mathcal F(x)=\sum_v F_v(P_vx+a_v)
              +\frac i2x^TKx+\ell^Tx+c,
 \qquad K=K^T\in\mathbb R^{n\times n}.
 \tag{8}
\]
Every actual scalar, charge and primitive constant is retained in
(8). The form of (8) is a hypothesis about the original phase
presentation, not a replacement for a different quantum gluing rule.

For any two assembled states whose local connecting segments are
regular, direct subtraction of the gradients gives
\[
 \mathcal E_{\mathcal F}(x_1,x_0)
       =\sum_v\mathcal E_{F_v}(P_vx_1+a_v,P_vx_0+a_v).
 \tag{9}
\]
Indeed \(P_v\overline{\delta x}=\overline{P_v\delta x}\), and
\(\Re\{(iK\delta x)\cdot\overline{\delta x}\}=0\), because
\(\delta x^*K\delta x\) is real. The affine term has no gradient
difference. Equivalently, throughout a common domain,
\[
             -\Re\mathcal F''=\sum_vP_v^T(-\Re F_v'')P_v.
 \tag{10}
\]

**Theorem 2 (stationary boundary energy composes).** Split
\(x=(s,b)\) into newly internal and external variables. Suppose
two assembled states satisfy the exact original matching equations
\(\mathcal F_s=0\). Their exterior gradients are
\(p_i=\mathcal F_b(x_i)\). If every local segment in (9) has
\(-\Re F_v''\succeq0\), then
\[
 -\Re\{(p_1-p_0)\cdot\overline{b_1-b_0}\}
       =\sum_v\mathcal E_{F_v}(x_{v,1},x_{v,0})\ge0.
 \tag{11}
\]
No assumption that the whole connecting segment is stationary is
needed. The same law applies when a local phase \(F_v\) is already
a stationary reduction satisfying Proposition 1.

*Proof.* The internal components of the assembled gradient difference
vanish at the two endpoints. Apply (9) and then (7) locally.
Thus internal matching cancels before taking an absolute value or
an upper bound. There is no restriction to valence two. \(\square\)

If the assembled internal Hessian is invertible and a holomorphic
stationary branch is supplied, it can itself be eliminated using
Proposition 1. In a regular common branch, successive eliminations
give the same boundary primitive, gradient and energy as simultaneous
elimination: both evaluate exactly (8) at the same stationary state.
The Schur-complement formula consequently associates without an
additive curvature loss. This statement assumes all the intermediate
eliminations used are regular; it does not select a branch by formal
algebraic elimination.

For local bounds \(-\Re F_v''\succeq W_v\succeq0\), the full
retained lower bound is \(\sum_vP_v^TW_vP_v\), followed by (3).
It need not be positive definite. Injectivity of the assembled local
null relations is one sufficient condition. Bounds and stationary
domains can depend on the fixed graph and powers; no uniform estimate
as the number of clusters grows follows from (9).

## 3. A boundary-only certificate after any regular composition

Suppose a composed phase \(\mathcal F\) has a jointly holomorphic
stationary reference \(r(c)\), for \(c\) in a product of clipped
disks or rectangles. Its exterior coordinates are \(b(c)\), with
original exterior gradient \(p(c)\). Fix one anchor reference
\(r^0=r(c^0)\). The centered signed correction is exactly
\[
 C_0(c)=\frac12\Re\{[p(c)-p(c^0)]\cdot
                          \overline{b(c)-b(c^0)}\}
       =-\frac12\mathcal E_{\mathcal F}(r(c),r^0)\le0,
 \tag{12}
\]
provided either the graph hypothesis (6) or the local connecting-
segment hypotheses of Theorem 2 hold. Only exterior boundary data
are needed to evaluate the left side. The right side proves its sign
and records exactly how local energies compose.

Keep the original, possibly uneliminated target comparison
\[
 \begin{split}
 w&=X+ih+\tfrac12\Lambda(r-\bar r),\\
 D(c;X)&=\Re\{\Psi(w)-\mathcal F(r)
                        -\mathcal F'(r)\cdot(w-r)\}.
 \end{split}
 \tag{13}
\]
Here the target \(X\) and \(h\) are fixed while differentiating
in \(c\); \(\Lambda\) is constant diagonal, nonnegative, and
equals one on every exterior boundary coordinate. Assume the full
target image is regular and \(-\Re\Psi''\succeq0\) there.
All stationary equations and reference holomorphy hold on a
neighborhood of the entire parameter product. Then the
[signed-compensation identity](research_stationary_reference_signed_boundary_compensation.md)
gives, for each parameter direction,
\[
                         \Delta_k(D-C_0)\ge0.
 \tag{14}
\]
For a uniform boundary majorant \(D(\zeta;X)\le d(\zeta)\),
iteration of the one-variable maximum principle yields
\[
 \sup_{c,X}D(c;X)
 \le\sup_{\zeta\in\prod_k\partial K_k}
       \left\{d(\zeta)+\frac12
                   \mathcal E_{\mathcal F}(r(\zeta),r^0)\right\}.
 \tag{15}
\]
The distinguished boundary includes every clipping segment and its
junctions. The inequality keeps the phase and energy at the same
boundary point. It neither differentiates an optimized scalar
majorant nor bounds the energy by a separately maximized derivative.

Formula (15) is a compositional sufficient test: local reference
energy certificates establish (12), exact matching leaves only the
external energy, and a strict negative bound on the displayed
boundary expression proves the interior gap. Its right side still
requires a new boundary inequality. Nonnegative energy makes that
test more demanding than the bare boundary bound \(d<0\).
In particular (12) does not allow the positive boundary term in
(15) to be omitted.

If (13) is instead assembled as a sum of cluster defects, the
shared target coordinates, heights and coefficients must agree;
the original gluing terms in (8) must also be included. These are
the exact matching hypotheses of the earlier product-boundary
lemma. Eliminating a reference variable does not authorize replacing
the literal target source by its stationary value.

## 4. Two original phase classes to which the energy law applies

For the circle-tree edge phase on its original lift, the
[cone-chamber theorem](research_cone_chamber_accretivity.md) uses
\[
 \mathcal F(t)=\sum_{vw}\psi(t_v,t_w)
          +\frac i{4\pi}\sum_v n_vt_v^2-i\sum_v\lambda_vt_v,
 \qquad n_v,\lambda_v\in\mathbb R.
 \tag{16}
\]
On a specified convex chamber where its embedded edge Hessians
have positive negative real part, (9) gives the exact identity
\[
             \mathcal E_{\mathcal F}(t_1,t_0)
                       =\sum_{vw}\mathcal E_\psi(t_{vw,1},t_{vw,0}).
 \tag{17}
\]
Thus arbitrary fixed signed powers introduce no extra local energy
term. They do change the stationary references and may move them
outside the chamber. The chamber containment and original source
contour estimates are not consequences of (17). This includes
branching graphs wherever the original phase presentation (16)
and those domain conditions have been established.

For the current mixed-prefix reference, use the original phase
\[
 F_{\alpha\beta}(a,u,z,v,b)
 =Q_1(u;a,z)+Q_\beta(v;z,b)-g(z)
                         -\frac\alpha2g(a)-\frac\beta2g(b).
 \tag{18}
\]
The [whole-pair estimate](research_mixed_horizontal_zero_mode_support.md)
holds on \(\mathcal S\times\mathcal P^2\), where
\(\mathcal S=[.15,.49]+i[-.108,.068]\) and
\(\mathcal P=[.22,.45]+i[-.12,.12]\).
On the containing product \((u,v)\in\mathcal S^2\),
\((a,z,b)\in\mathcal P^3\), the two pair blocks and the
remaining nonnegative own terms give
\[
                  -\Re F_{\alpha\beta}''\succ\mu I_5,
                         \qquad \mu=1/1250000.
 \tag{19}
\]
The original stationary internal variables are \((u,z,v)\).
Their Hessian is invertible, so a local stationary graph over
\((a,b)\) exists near each actual reference. Wherever a common
such graph stays in this product, its reduced Hessian satisfies
(4). More directly, any two actual references in the product
satisfy (7), since the product is convex. With the original
allocated marginals \(p_L,p_R\), this gives the quantitative
version of (12):
\[
 -\Re\{\Delta p_L\overline{\Delta a}
              +\Delta p_R\overline{\Delta b}\}
                 \ge\mu\bigl(|\Delta a|^2+|\Delta b|^2\bigr).
 \tag{20}
\]
This comparison uses the actual reference family. It asserts no
global stationary graph on the independent \((a,b)\) rectangle.
Gluing compatible copies conserves their energies as in (11),
provided the original diagonal allocations are restored exactly
and each local reference segment remains in its stated domain.
No extra halfweight or missing chirp is introduced by this argument.

## 5. What composition does not preserve automatically

The real incidence condition in (8) is substantive. For a general
holomorphic coordinate map \(z=f(w)\),
\[
 (F\circ f)''=f'^TF''f'+\sum_jF_j f_j''.
 \tag{21}
\]
Neither term automatically preserves a nonpositive Hermitian real
part. Even \(F(z)=-z^2/2\), under \(z=iw\), becomes \(+w^2/2\).
The corresponding cotangent lift is canonical, so canonicality
alone does not preserve the energy condition. This is an obstruction
to an inference about arbitrary coordinate or tangle changes, not
a claim that this example is an original short filling. The
[coherent gluing tests](research_actual_coherent_gluing_hessian.md)
retain the additional polarization and port-budget conditions needed
for their different source presentation.

Also, zero twist energy is not a zero twist contribution to a
selected-height phase defect. For \(\theta(x)=ix^TKx/2\) and
\(w-r=d+ie\), with real \(d,e\), its exact Taylor defect is
\[
 \Re\{\theta(w)-\theta(r)-\theta'(r)\cdot(w-r)\}
                            =-d^TKe.
 \tag{22}
\]
This vanishes on a horizontal displacement, but can have either
sign when heights change. Thus the original filling and bilinear
chirps still have to be retained in the target inequalities in
(13)--(15), as in the present selected-boundary estimates.

Finally, local stationary elimination gives
\[
                       \det F''=\det H_{qq}\det\phi''.
 \tag{23}
\]
On a regular common branch this organizes the Gaussian determinants
without changing their original continuation. It does not choose
the square-root marks or give the actual source cycle a nonzero
intersection coefficient. A nonzero input amplitude and a justified
contributing local contour are still needed even for a nonzero local
Gaussian; the complete finite source additionally needs its endpoint,
alias, remainder and final observation estimates. The
[source-adapted observation criterion](research_source_adapted_observation_composition.md)
makes the last lower-bound requirement explicit.

The resulting closure statement is therefore for certified reference
domains, original reduced boundary data and signed upper comparisons.
It supplies no automatic domain, full finite-window estimate, or
nonzero marked scalar for arbitrary fixed short fillings.
