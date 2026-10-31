# Two-leaf Conway seeds: complete source, geometry, and the mixed-source hypothesis

31 October 2026. Complete-source extension and conditional mixed-source interface. The seed restriction can be
reduced to two leaves for the COMPLETE source and its literal geometry on
C(FG), with both children built from such seeds. The previous all-level,
all-output strict-support assertion cannot be retained. A geometry-certified
mixed-source statement follows under the explicit tangent condition below;
that condition is not automatic in the enlarged grammar. This note verifies the exact source and packet inputs for the existing
long-filling transfer under that certificate; it does not claim that every
two-leaf diagram passes it.

## 1. Exact grammar and the finite support issue

Use the unchanged physical leaf h=T(L_N), actual quarter-turn T, original
identity-wire stack, and marked cylindrical closure C. Allow finite expressions
E ::= A_s | T(E) | EE with s>=2, where A_s contains s distinct h coupons.
Fix a closed C(FG) with F,G from this grammar. All trees are fixed before N.
Put d=N-1 and M=floor(d/2).

The original complete leaf has strictly positive Newton coefficients at every
0<=r<=M. Exact positive multiplication shows

$$
\operatorname{supp}(A_2)=\{0,\ldots,2M\}.
$$

For a chosen k<=2M distribute k=i+j with i,j<=M and choose the upper product
output k; its coefficient is positive. No product output exceeds i+j. At odd
N, 2M=d. At even N, 2M=d-1, so the top coordinate is genuinely missing.
Actual turns may move this missing coordinate to the bottom. In particular,
the old proof by all-output support induction is unavailable.

The original complete-source identities, scalar normalization and nonnegative
Newton coefficients themselves remain exact. They do not require a robust
seed: see [original physical Conway source](actual_positive_complete_circle_conway_trees.md) §§1,3–4.

## 2. Strict classical states replace full finite support

At prescribed seed output b in (0,1), choose equal leaves

$$
\frac b2<a<\min\!\left(b,\frac12\right).
$$

Then the only gate of A_2 satisfies max(a,a)<b<2a<1 and each leaf is strictly
between 0 and 1/2. For A_s with s>2, the induction already given in
[arbitrary-width seed proof](actual_conway_arbitrary_width_seeds.md) §1 applies. At a macro-product choose
both child outputs in (b/2,min(b,1/2)); at a turn use 1-b. This constructs a
strict state for every open expression at every interior output.

For C(FG), delete ONLY its forced last gate, whose exact finite coefficient
is one and whose inputs obey i+j=d. Choose continuous child outputs 1/2,1/2.
Every remaining leaf and product inequality is strict. The boundary-barrier
argument of [original complete geometry](actual_positive_conway_hyperbolic_volume.md) §2 now applies without
change: a proper endpoint wire descends to a nonvertex-flat atom, and every
other gate equality exhibits one directly. A segment to this strict state
gives +infinity directional derivative at that atom, never a negative
infinite contribution elsewhere. The reduced maximum is interior and unique.
The retained tetrahedral angle maps recover all free wires, so its Hessian is
negative definite. Fixed interior-output profiles are real analytic.

Here is an every-level lattice proof that does NOT use full seed support.
Contract every chain of turns: a wire then equals a chosen unturned integer
coordinate or d minus it. Delete the forced final gate and express one root
child coordinate as d minus the other. The two children have disjoint trees;
these operations introduce no equation such as 2r=d. All remaining unturned
outputs are free integer coordinates. Round d times each coordinate of any
strict reduced real state to a nearest integer, then restore all eliminated
coordinates by those exact affine formulas. Each coordinate error is bounded
independently of d. Every nonforced inequality has fixed positive slack;
therefore every rounded state is valid for all sufficiently large d, at both
parities. In particular each leaf lies below M, even when 2M=d-1.

The finite state count is polynomial in N. The original uniform leaf/gate
factorial estimate is N times the same continuous action plus O(log N),
including d versus N offsets. Applying it to the rounded unique maximum gives
the lower limit; summing the uniform upper bound gives the upper limit. Thus

$$
\lim_{N\to\infty}\frac1N\log Z_{E,N}^{0}=\max_{P_E}A_E.
$$

for the whole original pure complete scalar, along all sufficiently large
levels. It is strictly positive at those levels. For an open output sequence
r_N/d->b in (0,1), use the analytic strict profile at b_N=r_N/d and round only
its other coordinates. The same argument proves its coefficient limit.
No finite-N full-support claim, or N=2 claim, is needed.

The isolated C(A_2) really lies outside this theorem. Its two leaves must sum
to d. At even N that is impossible because 2M=d-1, so the actual scalar is
zero. At odd N only both leaf labels M occur; the continuum state is
(1/2,1/2), all retained leaf volumes are zero. It has no strict complete metric
of the type used here. Isolated C(A_s),s>=3, has the existing separate strict
complete argument; this does not extend the mixed-color theorem for C(A_3).

## 3. Literal complete geometry and complete signed coupons

The companion [two-leaf seed geometry proof](actual_conway_two_leaf_seed_geometry.md)
checks the complete and deformed geometric interfaces in detail.

For an optimized A_2 let X=cot(pi a)>0. Its port is exactly

$$
\begin{aligned}
B_2&=X-\frac1{2X},\qquad Y_2=\frac1{2X},\\
B_2+Y_2&=X>0,\qquad X-B_2=\frac1{2X}>0.
\end{aligned}
$$

Hence -Y<B<X holds for this seed at every interior output. The macro-product
and turn preservation proof in [strict-quarter port theorem](actual_conway_strict_leaf_quarter_bound.md)
§§2–3 uses precisely this inequality. At a closed C(FG), the reflected root
ports give X,Y<1; those two inequalities propagate to every macro-seed port.
At an A_2 seed, Y=1/(2X)<1 therefore yields

$$
\frac12<X<1,\qquad \frac14<a<\frac{\arctan2}{\pi}.
$$

For s>=3 the old sharper width-dependent bound remains valid.

The geometric proof in [original complete geometry](actual_positive_conway_hyperbolic_volume.md) §§3–7
uses strict leaf/prism angles, exact ordered input maps, and the completed
child FREE/CAP pattern. A_2 already is a completed product; both closed root
children are completed. Thus its original convex gluing, right-angled closed
polyhedron, reversible bowtie cut and canonical cusp decoration apply. The
assembled complete hyperbolic metric is on the actual augmented complement,
with volume 2pi max A_E. This is not an identification from a formal tangle
fraction or from matching just a port modulus.

All leaf coordinates remain in a compact subinterval of (1/4,1/2) for each
fixed expression. Consequently the actual high-index complete odd-coupon
asymptotic and its concave plateau bound apply. Replacing g by g_tilde only
at the chosen odd leaves gives a concave majorant agreeing with the pure
action near its strict maximum; this maximum is still the unique global one.
The original primitive central lattice has 2H-3 free wires: H leaf outputs,
H-2 retained product outputs, and one root input relation. The strict lattice
construction above preserves that primitive lattice and every d=N-1 shift.
Thus the complete signed amplitude argument of
[original half-twist Newton transport](actual_odd_conway_newton_transport.md) §4 is inherited, including its nonzero
local amplitudes and original phase. The changed shaded gluings and complete
cusp/edge checks of [literal half-twist partner geometry](actual_conway_half_twist_partner_geometry.md) §§1–3 are
local to these same literal leaf disks. This establishes the COMPLETE signed
source/volume interface; it does not by itself supply a mixed-color gap.

The connectivity induction also survives: A_2 realizes {I,U} without internal
loops (both odd, or one pure and one odd). The existing turn/set-product table
therefore gives the same constructive one-main-component parity choice.

## 4. Exact additional hypothesis for the whole mixed-color estimate

Retain the original functions

$$
\begin{aligned}
J(t)&=\int_0^t\log(2\sin(\pi u))\,du,\\
g(a)&=J(2a)-4J(a),\qquad k(u)=-2J(u/2),\\
I(a)&=\min_{0\le u\le1}\bigl[g(a)+g'(a)(u-a)-k(u)\bigr].
\end{aligned}
$$

A sufficient condition on the ACTUAL complete optimizer is

$$
I(a_l)>0\qquad\text{for every leaf }l.\tag{H}
$$

This condition is finite, geometric and uses the original optimized leaf
labels. Since the expression is fixed, its minimum is a positive constant.
Under (H), every step of [whole mixed-source gap](actual_odd_conway_uniform_mixed_source_gap.md) §§4–5
applies on the unchanged expanded alias support: core tangents, gate tangents
and affine-wire cancellation give a loss for every nonempty alias subset;
the all-core concave majorant and local physical-color loss give the entire
complement gap. Both parity offsets and the polynomial state count are
unchanged. This proves the same two WHOLE mixed-source inequalities there,
conditional on (H), without requiring all finite Newton outputs to occur.
It is not yet a new assertion of the final filling theorem.

For a0=atan(sqrt2)/pi, the earlier theorem proves I>0 on [1/4,a0]. For a>=a0,
g'(a)<=-log2 and k'(u)>=-log2, so k(u)-g'(a)u is maximized at u=1. Hence

$$
I(a)=g(a)+(1-a)g'(a),\qquad
I'(a)=(1-a)g''(a)<0.\tag{A}
$$

In particular the universal A_2 upper bound atan2/pi is insufficient. The separately proved algebraic sufficient cutoff is X=cot(pi a)>=2/3:
its tangent margin is greater than 1/2500. Its exact proof and conditional
source transfer are in
[algebraic leaf alias certificate](actual_conway_algebraic_leaf_alias_certificate.md).
Thus this condition on every actual A_2 seed, with the old automatic
condition at all larger proper seeds, suffices for (H).

## 5. A strict A_2 tree where the inherited tangent fails

Consider the literal permitted tree

$$
E=C\bigl(A_2T(A_4)\bigr).
$$

where A_4 may itself be the product of two A_2 seeds. The following strict
stationary data are exact, not a numerical scan. At the first A_2 take leaf
cotangent X=1/sqrt3, so its common leaf label is a=1/3. Its port is

$$
(B,X,Y)=\left(-\frac1{2\sqrt3},\frac1{\sqrt3},\frac{\sqrt3}{2}\right).
$$

At A_4 take leaf cotangent X=sqrt3/2=cos(pi/6). Formula B_j=T_j(X)/U_(j-1)(X)
gives B_2=1/(2sqrt3), B_3=0, B_4=-1/(2sqrt3), and Y_4=1/sqrt3. Its turn
therefore has the port

$$
\left(\frac1{2\sqrt3},\frac1{\sqrt3},\frac{\sqrt3}{2}\right).
$$

These are exactly the reflected matching root ports. Every seed gate is
strict: its common-X product rule has positive denominators, the A_4 outputs
have the listed cotangents, and the leaf-to-output inequalities are strict.
For an elementary check, its common leaf a satisfies 1/4<a<1/3;
the first output b_2 lies between a and 2a, the second equals1/2 and lies
between b_2 and b_2+a, and the third b_4=1-b_2 lies between1/2 and1/2+a.
The A_2 gate also has a<b_4<2a. Thus this is a strict stationary state and,
by the uniqueness proved above, the actual complete optimizer.

At the first seed leaf a=1/3, g'(a)=-log3 and the alias endpoint u=1 gives

$$
g(1/3)+g'(1/3)(1-1/3)-k(1)
=g(1/3)-\frac23\log3<0.
$$

Indeed g(1/3)<=g(1/4)=2Catalan/pi<2/3 and log3>1. Therefore (H) fails for this
actual enlarged-grammar optimizer. This is only a failure of the leafwise
supporting-plane proof: it does NOT exhibit a whole-source alias maximum,
realize the local envelope sharply, or disprove a mixed-source/filling gap.
Other ports and shared constraints may compensate the local deficit.

## 6. Exact changed-source packet and marked-geometry interfaces

The following verifies the inherited hypotheses rather than using the name
of the grammar. Write H for the number of actual leaves and K=2H-3 for the
primitive wire dimension. Before closure there are H leaf outputs and H-1
product outputs; eliminate each turn by r_out=d-r_in, fix the root output,
and solve its input-sum equation integrally for a variable from one of its
disjoint child trees. This removes two variables, with coefficient +1 or -1.
There is no even-level index-two lattice. The remaining coordinates k lie in
Z^K and every physical wire is r_w=N ell_w(k/N)+delta_w, with ell_w integral
affine and the original fixed integer shifts delta_w. Equal optimized seed
labels impose no equation on this lattice.

Choose a small fixed rectangular wire box around the strict optimizer. All
leaves lie in one compact subinterval of (1/4,1/2), all retained gate factorial
arguments lie in (0,1), and these properties persist on a fixed complex tube.
For sufficiently small physical color deficits h_l<=delta N, EVERY integer
state in that box is admissible for every sufficiently large N of either
parity. In particular r_l+h_l<=M and r_l-h_l>=0. No seed boundary output is
used to define or complete this window.

The EXACT local coefficients remain those of
[exact changed-source complex packet](actual_odd_conway_complex_color_packet.md) (1)–(3):

$$
\begin{aligned}
A_N(v,t)&=\frac{N^2s_{2v}}{s_v^2G_N(v-Nt)G_N(v+Nt)},\\
d_N^0(r,t)&=A_N(r,t),\\
d_N^\epsilon(r,t)&=\kappa^\epsilon\sum_{v=r}^{M}
(-1)^v q^{\epsilon v(r+1)}\binom vr_q A_N(v,t),\qquad\epsilon=\pm1,\\
\ell_N^\epsilon(r,t)&=e^{-i\epsilon\pi d/4}d_N^\epsilon(r,t).
\end{aligned}
$$

Here $q=e^{\pi i/N}$, $\kappa=q^{d^2/2}$, and $s_j$ is the original sine factorial.
The Gaussian coefficient is $\binom vr_q=s_v/(s_rs_{v-r})$.
Thus each circle still contributes its original N^2 coefficient factor,
not an extra normalized loop. All Hermite/normal directions, Cartan phases,
physical signs and the unit eta_N=exp[(i pi d/4)sum epsilon_l] are unchanged.
The packet is the finite sum of products of these H coefficients and the
H-2 original retained Newton gate coefficients on that rectangle.

The exponentially accurate high-index interpolation in that note §3 is a
LOCAL coefficient theorem on any such compact high-index interval. Its exact
chirp, selected recurrence solution and relative exp(-sigma N) grid error do
not involve the seed width or require other output coefficients to be
nonzero. The canonical factorial marks likewise depend only on the actual
strict factorial arguments. Each leaf contributes N^(1/2); each retained
gate contributes N^(-3/2). Hence the interpolated summand has power
N^(H/2-3(H-2)/2)=N^(3-H). Its original offset amplitude is

$$
b_E=\left(\prod_l b_{\epsilon_l}\right)\left(\prod_g b_{\mu,g}\right)
\exp\!\left[\sum_l\delta_l\partial_x f_{\epsilon_l}
+\sum_g\nabla m(w_g)\mathbin{\cdot}\delta_{w_g}\right].
$$

Here $b_{\epsilon_l}$ and $b_{\mu,g}$ are the original local leaf and gate
amplitudes from the exact changed-source packet. The CHANGED local actions
$f_\epsilon$, not the pure colored ones, occur in the offset factor.
The full wire Hessian is negative definite at completeness. Analytic implicit
function theory therefore gives one nearby holomorphic critical point. The
finite tensor-cotangent proof retains all rectangle boundary currents and
all nonzero modes; its assumptions are this strict window, the local joint
interpolant, and its fixed exponential grid error. They have just been
verified. The same argument yields

$$
\begin{aligned}
C_N^\epsilon(t)&=N^{3/2}a_\epsilon(t)e^{N\Phi_\epsilon(t)}
\bigl(1+O(N^{-1})\bigr),\\
a_\epsilon(t)&=\frac{(2\pi)^{K/2}b_E(y_*(t),t)}
{\sqrt{\det[-F_{\epsilon,yy}(y_*(t),t)]}}.
\end{aligned}
$$

Indeed 3-H+K/2=3/2. At zero the amplitude is the positive pure one times
product_(epsilon_l!=0) sqrt(sin(pi a_l))exp(-i epsilon_l pi a_l/2), so it is
nonzero. The local action shear and separate evenness are unchanged; writing
c_l=cot(pi a_l)>0, the color Hessian is exactly

$$
\partial_{t_l}\partial_{t_m}\Phi_\epsilon(0)
=-\frac{2\pi c_l}{1-\epsilon_l i c_l}\,\delta_{lm}.
$$

Its real part is strictly negative. This establishes the exact finite
complex corridor packet at both parities, including its normalization,
nonzero amplitude and original shifts. No all-boundary finite support was
used in any step.

Under (H), section4 supplies the entire physical-color gap and all-alias gap.
The concave core majorant gives the outside-wire-window gap. Combining these
with the exact packet gives the original mixed source versus packet error
exp[N(F0-gamma)] on a fixed small physical corridor, uniformly at both
parities. Thus the two quantum hypotheses of
[original-source long-filling transfer](general_original_source_long_filling_transfer.md) §1 are satisfied, including
mu=3/2 and the displayed eta_N, for every fixed passing A_2-based expression.

Finally, the marked geometry uses no missing finite-support assertion:
[marked odd peripheral deformation](actual_odd_conway_marked_peripheral_deformation.md) §§3–6 uses the strict
complete geometric anchor, the same local selected action, rational ordered
white/prism/turn maps, and exact local shaded/peripheral words. These inputs
are identical at every cell of the enlarged tree. Its complete polygons are
nondegenerate by §3 here, and the same wire Hessian supplies the nearby branch.
The primitive paths therefore remain U_l=-2pi i t_l, V_l=-2 partial_l Phi,
and the same actual odd-link full-twist equation U_l+p_l V_l=-2pi i applies.
The absolute regulator is anchored at the actual complete volume proved
above. No rational filling of a different pure partner is substituted.

Accordingly this interface audit supplies all inputs for the existing
long-filling transfer on the subclass satisfying (H), in particular the
finite algebraic condition $X\ge2/3$ at each $A_2$ seed. Any resulting enlarged
filling statement must retain the original quantifiers: one fixed literal
diagram and sign pattern, any chosen auxiliary subset, independent integral
slopes sufficiently long for that fixed datum, then all N tending to infinity.
It must not assert that every A_2 diagram passes the extra condition. The
explicit example in §5 shows why such an assertion would be unsupported.

## Inputs and review scope

Existing workspace inputs are [original physical Conway source](actual_positive_complete_circle_conway_trees.md),
[whole-source variational limit](actual_positive_conway_variational_limit.md), [original complete geometry](actual_positive_conway_hyperbolic_volume.md),
[arbitrary-width seed proof](actual_conway_arbitrary_width_seeds.md), [strict-quarter port theorem](actual_conway_strict_leaf_quarter_bound.md),
[original half-twist Newton transport](actual_odd_conway_newton_transport.md), [whole mixed-source gap](actual_odd_conway_uniform_mixed_source_gap.md),
and [literal half-twist partner geometry](actual_conway_half_twist_partner_geometry.md). The new steps are the A_2
strict seed, explicit every-level interior rounding, source-interface audit,
and exact C(A_2 T(A_4)) tangent failure. No existing theorem file is changed.
Author proof complete. The coherent-source reviewer independently fully
read sections 1–6: PASS, including strict every-level rounding, primitive
lattice, original finite changed coefficients, integer offset amplitude,
nonzero packet and the conditional whole-source restoration. The geometric
reader independently fully read sections 1–6: PASS, including the exact
stationary example, primitive lattice, changed packet and signed primitive
filling interface. The primary agent independently fully read sections 1–6: PASS as an
extension conditional on the retained original coefficient, packet and
marked-geometry theorems and, for the mixed-source transfer, $\min_l I(a_l)>0$.
That review checked strict rounding, primitive lattice dimension, powers of
$N$, actual ports, the tangent counterexample and the transfer interfaces.
These are internal reviews, not external peer review. No runtime test is
used to infer the extension.
