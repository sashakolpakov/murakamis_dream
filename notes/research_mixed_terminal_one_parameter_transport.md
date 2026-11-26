# One-parameter transport of the original terminal main comparison

Research deduction, 6 November 2026. A canonical ordinary-plus-terminal
suffix has one complex external parameter. Its original gradient has
rank-one parameter forcing, and its sole boundary response is a scalar
Schur complement. This gives a boundary-only main-profile criterion on
eight full-disk semicircle charts, or eighteen clipped-disk charts,
rather than a product of two boundary families. Centered value and
force formulas below involve only three reference coordinates and no
terminal private action. No new inequality is evaluated here.

## 1. Original reference and its rank-one response

Fix the incoming type flag \(\beta\in\{0,1\}\), terminal flag
\(\epsilon\in\{0,1\}\), and preceding ordinary flag one.
Use the five original, unscaled logarithmic equations
\(f(q;b)=0\) of
[the canonical suffix theorem](research_mixed_terminal_horizontal_envelope_diagnostic.md),
equations (1)--(5), with
\[
 q=(e,\xi,t,a,s),\qquad
 q_*(b)\in E\times U\times Q^3,\qquad
 \mu=6\pi/49.
 \tag{1}
\]
That theorem supplies existence, uniqueness, original zero lifts and
holomorphy near each closed original input disk
\[
 D_3=\{|b-(.35-.01i)|\le.09\},\qquad
 D_4=\{|b-(.30-.052i)|\le.064\}.
 \tag{2}
\]
It does not assert that every such input is realized by a finite word.
The original Jacobian \(\mathcal H=\partial_qf\) is complex symmetric
and satisfies \(-\Re\mathcal H\succ\mu I\).

Only its last gradient row depends on the external parameter:
\[
 f_s=j(a+s)+j(s+b)-3j(s)+i\pi[b-a+s-1/2],
 \qquad j(z)=\Log(2\sin\pi z).
 \tag{3}
\]
Set \(k(z)=g''(z)=\pi\cot(\pi z)-i\pi\), and put
\(L=j'(s+b)+i\pi=k(s+b)+2\pi i\). Differentiating the
original equations, not their exponentiated polynomial replacements,
gives
\[
 q_*'(b)=-L\mathcal H^{-1}{\bf e}_s.
 \tag{4}
\]
Here \({\bf e}_s\) is the fifth coordinate vector. In particular
only one inverse column is needed for all five responses.

The incoming allocated marginal of the original two-factor phase is
\[
 p(b)=g'(b+s_*)-(1+\beta/2)g'(b)+2\pi i s_*.
 \tag{5}
\]
The coefficient \(1+\beta/2\) retains the incoming modulus
halfweight; the last term retains the incoming chirp. Equations
(4)--(5) imply the exact scalar identity
\[
 p'(b)=k(b+s_*)-(1+\beta/2)k(b)
                         -L^2(\mathcal H^{-1})_{ss}.
 \tag{6}
\]
No conjugation occurs in this Schur expression. In negative-exponential
shape coordinates \(Z=\exp[-2\pi i(s_*+b)]\),
\(L=2\pi i/(1-Z)\); all Jacobian entries are likewise elementary
rational expressions in the original shapes and \(\pi\).
This avoids a high-degree endpoint-elimination map and does not choose
a new critical branch.

For example, coercivity alone gives the valid, possibly coarse bounds
\[
 \|q_*'\|_2\le |L|/\mu,\qquad
 |p'|\le |k(b+s_*)-(1+\beta/2)k(b)|+|L|^2/\mu.
 \tag{7}
\]
A tighter certified inverse column may replace these bounds. A
numerical inverse proposal is not by itself an inverse certificate.

The same existence theorem permits a fixed-center or affine residual
transport without any inverse certificate. For prescribed exact
\(q^0,\tau\), use \(q^{\rm aff}(b)=q^0+\tau(b-b^0)\).
If its entire raw image lies in the common convex domain, then
\[
 \|q^{\rm aff}(b)-q_*(b)\|_2
                   \le\|f(q^{\rm aff}(b);b)\|_2/\mu.
 \tag{8}
\]
An interval residual must use the whole external box and whole affine
image before intersecting necessary actual-root rectangles. Existence
is required only for the actual parameter points in the typed disk.
The original logarithms and the straight segments used in a Taylor
residual must all remain in their regular strips.

## 2. The sole boundary correction

Project the canonical family to
\(r(b)=(b,s_*,a_*,t_*,v_*)\), where \(v_*\) is \(\xi_*\)
for \(\epsilon=0\) and \(e_*\) for \(\epsilon=1\).
With precisely the phases of
[the joint-main budget](research_mixed_terminal_joint_main_budget.md), set
\[
 F(r)=Q_1(s;b,a)+\Phi_\epsilon(a;t,v)-g(a)-\frac\beta2g(b).
 \tag{9}
\]
Its stationary value is the original \(M_*\), including the absolute
private-action constant. The original equations and elimination
identities give \(F_s=F_a=F_t=F_v=0\) on the family, and
\(F_b=p\). Thus \(b\), which is also the external parameter,
is its only boundary coordinate.

For a fixed real main target \(x=(x_b,x_s,x_a,x_t,x_v)\), put
\[
 \Lambda=\operatorname{diag}(1,1,0,1,1),\qquad
 w=x+i\Lambda\Im r+iH{\bf e}_a,\quad H=1/100,
 \qquad \Psi_\nu=F+(1-\nu)g(a)+2\pi i\nu a.
 \tag{10}
\]
The original defect is
\[
 D_\nu(b;x)=\Re\{\Psi_\nu(w)-F(r)-p(b)(w_b-b)\}.
 \tag{11}
\]
This retains the complete selected weight and the incoming affine
marginal. The target products are the original ones in the joint-main
budget: \(b_R\in P\), \(s_R\in[.125,.5]\),
\(a_R\in I_\nu\), \(t_R\in[.15,.5]\), and the whole private
interval; \(I_1=P=[.22,.45]\), \(I_0=[.4,.45]\).

The original ordinary Hessian bound applies to both outer heights in
\([-.12,.12]\), and the full terminal Hessian applies to its main
products. Hence their sum, with the nonnegative own-weight curvature,
proves target concavity also when the incoming parameter ranges over
the full disks (2). This phase statement does not enlarge a separate
finite-source right-tail theorem. The reference images lie in a convex
containing product of the same Hessian domains, so \(-\Re F''\succeq0\)
on all reference-to-anchor segments.

Fix a certified anchor \(b^0\) in the parameter domain, with its
original canonical marginal \(p^0\). Then
\[
 C_0(b)=\frac12\Re\{[p(b)-p^0]\overline{b-b^0}\}\le0,
 \qquad \Delta_b(D_\nu-C_0)\ge0.
 \tag{12}
\]
These are the
[signed boundary-compensation identities](research_stationary_reference_signed_boundary_compensation.md)
with a single boundary coordinate of coefficient one. They require
neither \(q_*'\) nor \(p'\) to evaluate the correction. For a convex
parameter domain, (6) also gives the exact representation
\[
 C_0(b)=\frac{|b-b^0|^2}{2}
       \int_0^1\Re p'(b^0+t(b-b^0))\,dt.
 \tag{13}
\]
Its sign follows either from the concave reference segment or from
the reduced boundary-energy identity. Nonpositivity does not remove
the adverse boundary term \(-C_0\).

**Theorem 1.** Let \(K\) be a disk or clipped disk inside one of (2),
and assume the stated full reference and target domains on a
neighborhood of its closure. If a boundary estimate, uniform in all
allowed targets, satisfies
\[
 D_\nu(b;x)\le d_\nu(b),\qquad
 d_\nu(b)-C_0(b)<-\delta\quad(b\in\partial K,\ \nu=0,1),
 \tag{14}
\]
then \(D_\nu< -\delta\) throughout \(K\), with the same targets.

Indeed apply the maximum principle to the original function
\(D_\nu-C_0\) at each fixed target, and then use \(C_0\le0\)
in the interior. Neither the optimized budget nor a numerical upper
enclosure is asserted to be subharmonic.

For all four type pairs, full disks need eight rational semicircle
charts: two per \((\beta,\epsilon)\). For the existing \(K_3,K_4\),
the [nine arc-and-chord charts](research_mixed_second_selected_external_boundary_charts.md)
give eighteen cases after the two terminal types are included. All
clipping segments and junctions remain required. These counts concern
one boundary parameter, not the number of subdivision cells or profile
inequalities a future certificate may require.

There are two distinct sufficient routes. A direct uniform bound for
\(d_\nu\) on **every** \(b\in K\) needs no compensation. A
boundary-only bound needs (14), or a separate response-loss estimate.
The implication from a bare negative boundary budget to a uniform
interior budget is not justified.

## 3. A private-action-free centered value and force transport

The three-cost criterion in
[the joint-main curvature theorem](research_mixed_terminal_joint_main_curvature_budget.md)
uses only \((s,a,t)\) after the true stationary equations have been
imposed. Here are full-box differential formulas for its scalar data.
They do not impose stationarity on a Cartesian enclosure or its center.

Write \(a=A+ic\), \(\Delta=H-c\), \(d=i\Delta\),
\(\bar a=A+iH\), and for \(z=s+a,t+a,a\) define
\[
 L_z=g'(z+d)-g'(z),\qquad
 E_z=L_z-dk(z),\qquad K_z=k(z+d)-k(z).
 \tag{15}
\]
Let \(\mathcal B_g(z;d)=g(z+d)-g(z)-dg'(z)\). The literal
data of that criterion are
\[
\begin{split}
 T_\nu={}&\Re\{\mathcal B_g(s+a;d)+\mathcal B_g(t+a;d)
                       -3\mathcal B_g(a;d)\}
          +(1-\nu)\Re g(\bar a)-2\pi\nu H,\\
 A_s={}&\Re L_{s+a},\qquad A_t=\Re L_{t+a}-2\pi\Delta,\\
 A_{a,\nu}={}&\Re\{L_{s+a}+L_{t+a}-3L_a
                                      +(1-\nu)g'(\bar a)\}.
\end{split}
 \tag{16}
\]
They have no dependence on \(b\) or the private variable except
through the correlated reference coordinates \(s,a,t\).

For arbitrary variations of these three complex coordinates,
\(\mathrm dd=-i\,\mathrm dc\), and direct differentiation gives
\[
 \mathrm d\mathcal B_g(z;d)=E_z\,\mathrm dz+L_z\,\mathrm dd,
 \qquad
 \mathrm dL_z=K_z\,\mathrm dz+k(z+d)\,\mathrm dd.
 \tag{17}
\]
In particular the six real partial derivatives of the trial value are
\[
\begin{array}{c|cc}
 &\partial_{\Re}&\partial_{\Im}\\ \hline
 s&\Re E_{s+a}&-\Im E_{s+a}\\
 t&\Re E_{t+a}&-\Im E_{t+a}\\
 a&\Re(E_{s+a}+E_{t+a}-3E_a)+(1-\nu)\Re g'(\bar a)
   &\Delta\Re\{k(s+a)+k(t+a)-3k(a)\}.
\end{array}
 \tag{18}
\]
For the force differentials, use (17) in (16), retaining
\(\mathrm dA_t=\Re\mathrm dL_{t+a}+2\pi\mathrm dc\) and
the extra term \((1-\nu)\Re[k(\bar a)\mathrm dA]\) in
\(\mathrm dA_{a,\nu}\). All arguments and their connecting
segments must lie in the original regular strips. The residual
logarithmic increment \(E_z\) is second order in \(d\);
its exact form preserves this cancellation before interval bounds.

Equations (17)--(18) give a centered mean-value enclosure from one
literal midpoint evaluation and full-box logarithm/cotangent bounds.
Alternatively substitute \(\mathrm ds=s_*'(b)\mathrm db\),
\(\mathrm da=a_*'(b)\mathrm db\),
\(\mathrm dt=t_*'(b)\mathrm db\) from (4). This yields only
two real parameter derivatives while preserving the common dependence.
The latter version needs a certified inverse-column enclosure; it
cannot use derivatives of independently clipped coordinate images.

The off-stationary distinction is explicit. At the lifted trial
\(r+i\Delta{\bf e}_a\), the literal defect for an arbitrary regular
reference vector is
\[
 D_\nu^{\rm lift}(r)=T_\nu(r)-\Delta\Im F_a(r),
 \qquad
 \nabla_xD_\nu^{\rm lift}
  =(0,\Re F_s+A_s,\Re F_a+A_{a,\nu},\Re F_t+A_t,\Re F_v).
 \tag{19}
\]
Thus \(T_\nu\) and the three forces are the true value and force
data on the canonical family, while (19) retains every missing
residual at a nonstationary center. Enclosing the explicitly defined
functions (16) on a full box is legitimate; identifying them with the
literal off-stationary defect without (19) is not.

## 4. A concrete scalar criterion and a fixed-target alternative

For \(g_h(x)=\Re g(x+ih)\), define
\[
 \Gamma_{I,m}(A;x_*,h)=\sup_{x\in I}
 \{A(x-x_*)-m[g_h(x)-g_h(x_*)-g_h'(x_*)(x-x_*)]\}.
 \tag{20}
\]
On intervals inside \((0,.5]\), this is a single clipped convex
conjugate. It has an explicit scalar optimizer: put
\(r_h=e^{2\pi h}\), \(\ell=A/m+g_h'(x_*)\), and solve
\[
 g_h'(x)=\ell,\qquad
 \cos(2\pi x)=\frac{1+r_h^2-e^{2\ell}}{2r_h}.
 \tag{21}
\]
If \(\ell\) is outside the derivative range of \(I\), use the
corresponding endpoint; otherwise use the unique interior inverse.
Intervals crossing a clipping transition require a containing
enclosure. This is not an unconstrained numerical optimization, and
the gain is not truncated at zero when \(x_*\notin I\).

Under exactly the height and optimizer-restriction hypotheses of
the curvature theorem, an eligible boundary budget in (14) is
\[
\begin{split}
 d_\nu={}&T_\nu
 +\Gamma_{[.22,.5],1}(A_s;\Re s_*,\Im s_*)\\
 &+\Gamma_{I_\nu,\nu+1/2}(A_{a,\nu};\Re a_*,H)
 +\Gamma_{[.18,.5],1}(A_t;\Re t_*,\Im t_*).
\end{split}
 \tag{22}
\]
The original incoming force is zero because the full marginal (5)
was subtracted. No independent maximization of a boundary halfweight
has been inserted.

The curvature theorem's incoming-height condition
\(-.078\le\Im b\le.021\) is narrower than either full disk and
does not cover all of \(K_3\cup K_4\). Its three-gain formula and
\(s\ge.22\) restriction therefore cannot silently be used on all
those boundaries. On a region where these hypotheses hold throughout,
(22) and (14) are a one-parameter sufficient uniform criterion.
Elsewhere the full-domain main concavity from Section 2 still permits
an ordinary fixed-target tangent certificate on the unshortened index
intervals. Different valid boundary majorants may be combined, but
each must bound the same original defect and retain the same \(C_0\).

For such a fixed target, all off-stationary derivatives also stay
simple. Put \(\delta_b=x_b-\Re b\),
\(K=k(b+s)-(1+\beta/2)k(b)\), and
\(L=k(b+s)+2\pi i\). On any full regular reference box,
\[
 \nabla_XD_x
  =\Re(-K\delta_b,-F_s-L\delta_b,-F_a,-F_t,-F_v),
 \tag{23}
\]
\[
 \nabla_YD_x
  =-\Im(\Psi_b-F_b-K\delta_b,
        \Psi_s-F_s-L\delta_b,-F_a,\Psi_t-F_t,\Psi_v-F_v).
 \tag{24}
\]
These follow by differentiating the literal (11) with the marginal
defined as \(F_b\) on the whole box. They are the one-boundary
specialization of the
[centered difference-of-actions identities](research_mixed_third_selected_recentered_defect.md).
Terms \(F_s,F_a,F_t,F_v\) may vanish only on the canonical family.
After a centered trial enclosure, horizontal concavity bounds the
entire target box by its exact affine support. One then subtracts
\(C_0^-\), just as in (14).

The resulting certificate needs only the original one-parameter family,
one boundary marginal and either three scalar costs or a fixed-target
support bound. It proves no new sign, no estimate for the other
terminal profile labels, no nonplateau contour bound and no nonzero
coefficient of the complete invariant. Those remain separate from
this reduction.
