# Original one-cap pressure: global real continuation and an algebraic boundary response

31 October 2026. **analytical research theorem.**
Unpublished. The original source boundary curve has an atom-free,
log-algebraic pressure-root density and an exact selected logarithmic
period equal to the original **drilled** hyperbolic volume. No filled
quantum limit or ordinary knot A-polynomial identification is asserted.
The original simple matched sphere, protected MAIN edge uv and cap
F=(u,A,v,C) remain fixed. Every other original port is CROSS. Assume a
strict finite positive one-cap stationary exterior, with all ordinary
incidences positive, L_A=L_C and 0<nu<1/2. The [one-cap geometric double](research_one_cap_geometric_double.md) gives
the stronger nu>1/4, but that stronger inequality is not needed below.
Work on the ODD-level original binary polynomial P_N(A,C), with every
other ordinary face extracted to its original demand d=N-1.

Inputs are the local complex pressure theorem, its root-measure
reconstruction, the original half-triangle potential and compact flow
duality. No signed coefficient lower asymptotic is assumed. This note
does not prove chi_D >= M_cap-Phi_D.

## 1. The positive-real gluing branch exists for every finite boundary ratio

Put A=exp(z), C=1; let I be the other ordinary faces, with weights exp(w_i).
For the original exterior triangles define

\[
\mathcal F(z,w)=\sum_tQ_t(L)-\sum_{i\in I}w_i.\tag{1}
\]

Each supported half-triangle has supply 1/2. Its entropy is continuous
and bounded on its closed supported simplex; its weighted potential is
the maximum of entropy plus its load/log-weight pairing. On positive
weights Q_t is real analytic. A pure supported corner contributes a
linear term and no Hessian; every other supported triangle has Hessian
kernel precisely common scaling of its supported coordinates.

The graph joining ordinary vertices that share an exterior triangle is
connected. Deleting the cap triangles removes only the ordinary edge
AC from those triangles, and the triangle on the other side of AC
remains in the exterior. Thus no edge of the connected ordinary graph
is lost. The grounded Hessian in the I variables is positive definite
at EVERY finite positive weight assignment, not only at z=0.

Here is the required global coercivity. Extend a vector v in R^I by
v_A=v_C=0. Write alpha^0 for the actual strict exterior allocation at
the given stationary point. Its I demands are one. The recession
function in the extracted directions is

\[
\begin{aligned}
\operatorname{rec}(v)
 &=\sum_t\frac12\max_{f\in\operatorname{supp}t}v_f-\sum_{i\in I}v_i\\
 &=\sum_t\left[\frac12\max_{f\in\operatorname{supp}t}v_f
     -\sum_{f\in\operatorname{supp}t}\alpha^0_{t,f}v_f\right].
\end{aligned}\tag{2}
\]

Every summand is nonnegative. Equality requires all supported v_f in
each nonmonomial triangle to be equal, since all its supported alpha^0
are strictly positive. Connectedness and the two fixed anchors force
v=0. Hence rec(v)>=c||v|| for some c>0, by compactness of the unit
sphere. The pure-vertex choices in each local potential give

\[
\mathcal F(z,w)\ge c\lVert w\rVert-C(1+|z|).\tag{3}
\]

uniformly for z in compact real intervals. This also covers the empty
I case with its empty minimization convention. Entropy boundedness is
enough here; no global coefficient asymptotic is being invoked.

Consequently (1) has one finite minimizer w(z) for every real z. Its
grounded Hessian is invertible, so the implicit-function theorem makes
w(z) and

\[
F_{\mathrm{cl}}(z)=\min_w\mathcal F(z,w).\tag{4}
\]

real analytic on the WHOLE real line. This is actual positive gluing
with the original I demands. It is not an assertion that its planar
developing map remains embedded for all z.

Let mu_D be the probability measure reconstructed from the local
pressure germ in [the original pressure/root-measure theorem](research_cap_root_measure_from_classical_pressure.md).
The function

\[
F_\mu(z)=M_{\mathrm{cap}}+\int_{[0,1]}
 \log(1-p+pe^z)\,d\mu_D(p).\tag{5}
\]

is real analytic on all R (locally the denominator is uniformly away
from zero). The local theorem says F_cl=F_mu near zero.
The identity theorem for real analytic functions therefore gives

\[
F_{\mathrm{cl}}(z)=F_\mu(z)\qquad(z\in\mathbb R).\tag{6}
\]

This continuation uses coercivity and the finite positive gluing
system, not a remote every-degree coefficient limit or an assumed
global complex saddle.

## 2. The exact residual interval is [0,1]

Let R(s) retain precisely the original residual targets A:s, C:1-s,
all I demands one and both protected demands zero. Its full feasible
interval is [0,1]. To see the endpoint assertion, multiply the
transportation problem by two: each exterior triangle supplies one,
each I face demands two, and A,C together demand two. This is an
ordinary bipartite network-flow polytope with integral supplies and
demands (one may route both A,C into a common final sink). Integral
vertices attain the linear minimum and maximum of the A load. In the
original normalization these two extrema lie in {0,1/2,1}.

The strict cap exterior realizes s=nu<1/2. The original complete
packing realizes a residual s>1/2: the restored cap's uAC triangle
has A load alpha_A in (0,1/2), so its exterior A demand is
1-alpha_A in (1/2,1). Thus the two extrema are 0 and 1. Convexity
supplies every intervening value. This uses the literal half-supply
network and the original complete packing, not a new mark or source.

Compact concave duality now gives, including both endpoints,

\[
\begin{aligned}
F_{\mathrm{cl}}(z)&=\max_{0\le s\le1}\{R(s)+sz\},\\
R(s)&=\inf_{z\in\mathbb R}\{F_{\mathrm{cl}}(z)-sz\}.
\end{aligned}\tag{7}
\]

The second formula follows also by closed concave biconjugacy; R is
upper semicontinuous and concave on its compact feasible interval.
In particular R(s)=M_cap-I_mu(s), where I_mu is the Legendre transform
of the normalized integral in (5).

The limiting derivatives of (7) as z tends to minus/plus infinity
are 0 and 1. Differentiating (5) and using dominated convergence gives

\[
\begin{aligned}
\mu_D(\{1\})&=\lim_{z\to-\infty}F_{\mathrm{cl}}'(z)=0,\\
1-\mu_D(\{0\})&=\lim_{z\to+\infty}F_{\mathrm{cl}}'(z)=1.
\end{aligned}\tag{8}
\]

Thus neither endpoint carries a root atom. This is stronger than
merely knowing the stationary mean nu or the finite polynomial's
nonzero endpoint coefficients.

## 3. The selected circle-star equations give an algebraic boundary phase

Write w=exp(z)>0 and m_D(w)=F_cl'(log w). For each nonmonomial
exterior triangle t on supported positive weights a,b,c put

\[
\begin{gathered}
T_t^2=ab+ac+bc,\qquad T_t>0,\\
Z_{t,f}=\frac{T_t+iL_f}{T_t-iL_f}
       =\exp(2\pi i\alpha_{t,f}).
\end{gathered}\tag{9}
\]

The same formula applies with exactly two positive weights. A pure
supported corner has alpha=1/2 and is represented separately by the
constant factor -1; a zero corner contributes 1. No zero T is divided
out. The exact extracted-face equations are

\[
\prod_{t\ni f}Z_{t,f}=1\qquad(f\in I).\tag{10}
\]

The branch is specified by the original load equations sum_t alpha=1,
the positive T_t, and the actual stationary weights at w=1. The
algebraic equations alone need not specify those integer lifts.

After denominators are cleared, (9)-(10), L_A=w, L_C=1 form a finite
polynomial system with Gaussian-rational coefficients. The Jacobian
in the extracted log weights of (10) is a nonzero diagonal factor
times the grounded Hessian. The nonmonomial T equations have nonzero
T derivatives. Hence the selected branch is a regular algebraic curve
over the w line. Its weight coordinates and its boundary product

\[
B_D(w)=\prod_{t\ni A}Z_{t,A}
        =\exp(2\pi i m_D(w)).\tag{11}
\]

are algebraic functions of w. Equivalently there is a nonzero
source-boundary eliminant

\[
\mathcal A_D(w,B_D(w))=0.\tag{12}
\]

It may be obtained by saturating by the nonzero denominators and
Jacobian and selecting the regular component carrying the positive
branch. Eliminating a higher-dimensional extraneous component without
this selection is not the asserted construction. Gaussian-rational
polynomial equations suffice; taking Galois conjugates if needed
gives an eliminant over their ground field.

This is an algebraic boundary ANGLE response of the original source
disk. It is NOT identified here with the ordinary knot A-polynomial,
nor with a primitive meridian/longitude pair of the drilled group.
That additional peripheral dictionary has not been proved. The phase
B alone forgets an integer; the actual lift m is fixed by its positive
continuation and the endpoint values 0 and 1 from (8).

## 4. The root measure is absolutely continuous with a log-algebraic density

Push mu_D forward by r=(1-p)/p to a probability measure sigma_D on
(0,infty); (8) removes the endpoint masses. For w off the negative
real axis the pressure derivative has the actual Stieltjes form

\[
m_D(w)=\int_{(0,\infty)}\frac{w}{w+r}\,d\sigma_D(r).\tag{13}
\]

This holomorphic function continues the positive-real m from (11).
For Im w>0 it has strictly positive imaginary part, since
Im[w/(w+r)]=r Im(w)/|w+r|^2. Thus

\[
B_D(w)=\exp(2\pi i m_D(w)),\qquad 0<|B_D(w)|<1.\tag{14}
\]

in the upper half-plane. The algebraic relation (12), valid near the
positive axis, holds throughout that half-plane by holomorphic
continuation. It fixes one selected algebraic branch there. On the
positive axis |B|=1; the reflected branch obeys
B(conj w)=1/conj(B(w)). No branch is reset on the negative axis.

There can be no atom at any finite r0>0. If an atom has mass a>0,
then at w=-r0+i y, y>0,

\[
\operatorname{Im}m_D(-r_0+iy)\ge\frac{ar_0}{y},\qquad
 |B_D(-r_0+iy)|\le\exp\!\left(-\frac{2\pi ar_0}{y}\right).\tag{15}
\]

A nonzero algebraic branch near a finite point has a Puiseux leading
term c(w+r0)^beta and hence a power-law lower bound along this ray.
It cannot satisfy (15). This contradiction excludes every interior
atom, without assuming any smooth limiting density in advance.

Away from a finite set of algebraic branch, zero and pole points on
the negative axis, the upper branch B is analytic and nonzero in a
neighborhood. There one can choose Log B and write
m=Log B/(2pi i)+an integer, with the SAME continued integer lift.
Stieltjes inversion applied to m(w)/w gives the real-analytic density

\[
\frac{d\sigma_D(r)}{dr}
 =\frac{\operatorname{Im}m_D(-r+i0)}{\pi r}
 =-\frac{\log|B_D(-r+i0)|}{2\pi^2r}.\tag{16}
\]

Explicitly, -Im[m(x+i y)/(x+i y)]/pi is the convolution of sigma_D
with y/[pi((x+r)^2+y^2)]. Integrate it over a compact negative interval
and let y decrease to0. The elementary Poisson approximate-identity
limit gives that interval's measure; the analytic boundary values
there give exactly (16). Endpoint atoms have already been excluded.

There is no singular continuous part: outside that finite set the
measure has (16), while a measure supported on the remaining finite
set is atomic and has already been excluded. Returning to p yields

\[
\frac{d\mu_D(p)}{dp}
 =-\frac{\log\left|B_D\!\left(-\frac{1-p}{p}+i0\right)\right|}
          {2\pi^2p(1-p)},\qquad 0<p<1.\tag{17}
\]

The density is nonnegative, integrates to one, and is piecewise real
analytic. At an interior exceptional point it has at worst a logarithmic
singularity: a Puiseux zero of B becomes a multiple of log|r-r0| in
(16). A boundary pole is incompatible with (14).

For completeness, at r=0 and infinity, (8) gives m->0 and m->1,
respectively, so B tends to the nonzero value1. Its nonconstant
algebraic Puiseux expansion gives m=O(w^a) at0 and m-1=O(w^-b) at
infinity for some a,b>0 on the selected branches. Consequently the
endpoint density bounds are O(p^(b-1)) and O((1-p)^(a-1)). In particular
both logarithmic endpoint moments are finite. These assertions concern
the actual fixed disk; they give no uniform exponent over varying
diagrams.

## 5. The same algebraic branch determines the exact missing comparison

Let f_D(w)=int log(1-p+p w) dmu_D(p), continued from positive w.
Then f_D(1)=0, and on the slit plane

\[
df_D=m_D(w)\frac{dw}{w}
 =\left[\frac{\operatorname{Log}B_D(w)}{2\pi i}
       +\text{the retained integer}\right]\frac{dw}{w}.\tag{18}
\]

Thus the original pressure difference is a logarithmic integral on
the selected algebraic boundary curve. Its normalization is fixed
at w=1, not by an arbitrary integration constant. Calling (18) the
volume of a knot representation would need a separate group and
relative-chain proof.

Put q(z)=Q(0,exp(z),1). Its original normalization is

\[
\begin{gathered}
q(z)=\frac2\pi\operatorname{Ti}_2(e^{z/2}),\qquad
q'(z)=\frac{\arctan(e^{z/2})}{\pi},\\
\operatorname{Ti}_2(x)=\int_0^x\frac{\arctan t}{t}\,dt.
\end{gathered}\tag{19}
\]

Restoring the two original cap triangles and their two target logs
gives the exact full-capacity formula

\[
\Phi_D-M_{\mathrm{cap}}
 =\inf_{z\in\mathbb R}\{f_D(e^z)+q(z)-z\}.\tag{20}
\]

It is equivalent to the original R(s)+2f(s-1/2) formula, by (7), and
does not replace either face target.

There is an exact algebraic critical-point and absolute-value statement
here, beyond an unspecified minimization. Put

\[
B_{\mathrm{cap}}(w)=\frac{1+i\sqrt w}{1-i\sqrt w},\qquad
 a_{\mathrm{cap}}(w)=\frac{\arctan\sqrt w}{\pi}.\tag{20a}
\]

The derivative of the potential in (20) with respect to log w is
m_D(w)+a_cap(w)-1. It is strictly increasing: the first derivative
has positive Bernoulli variance and the cap derivative is strictly
positive. Its limits are -1 and 1/2 by (8). Therefore there is exactly
one positive critical point w_*, and w_*>1 because
m_D(1)+a_cap(1)-1=nu-3/4<0. At this point

\[
B_D(w_*)B_{\mathrm{cap}}(w_*)=1,\qquad
 m_D(w_*)+a_{\mathrm{cap}}(w_*)=1.\tag{20b}
\]

The second equality is the retained lift: the sum lies in (0,3/2)
for positive w, so the only possible integer at a solution is1.
The selected positive solution is algebraic, since (12),(20a) are
algebraic and the critical point is isolated (the derivative is
strictly positive). Its finite exterior weights restore the original
complete A and C demands; every other original demand was already
imposed. Thus it is the original complete circle packing.

With C0=q(0)=2G/pi, where q's argument here is the log weight z and
G is Catalan's constant, the exact relative logarithmic period is

\[
\Phi_D=M_{\mathrm{cap}}+C_0
 +\int_1^{w_*}\bigl[m_D(w)+a_{\mathrm{cap}}(w)-1\bigr]\frac{dw}{w}.
\tag{20c}
\]

Equivalently the integrand is Log_lift(B_D B_cap)/(2pi i), with lift
2pi i[m_D+a_cap-1], not independently reset principal logarithms.
The value is the original drilled hyperbolic volume divided by2pi
by the already proved complete packing/capacity theorem. This is an
absolute geometric consequence of that theorem and the specified
constant M_cap+C0; it does not require a new representation-volume
identification of (18), identify a knot A-polynomial, or prove a
filled quantum limit.

For r>0 let U(r)=Re f_D(-r+i0). The finite original two negative-axis
suprema correspond, in precisely the degree-one normalization, to

\[
-\chi_D=\sup_{r>0}\{U(r)-\max(0,\log r)\}.\tag{21}
\]

with the continuous limiting values at r=0,infinity included. The
endpoint power and interior logarithmic bounds after (17) justify
these finite limits; the original supremum-rate theorem already
handles them without needing this additional regularity.

Equations (18)-(21) put the proposed universal comparison on ONE
selected, source-normalized algebraic boundary branch:

\[
\sup_{r>0}\{\operatorname{Re}f_D(-r+i0)-\log_+r\}
 \le\inf_{z\in\mathbb R}\{f_D(e^z)+q(z)-z\}.\tag{22}
\]

This note does not prove (22). It proves that the previously arbitrary
root measure is constrained by the actual finite circle-star system,
has no atoms, and is reconstructed by (17). The known one-cap original
chain only bounds the right-hand deficit by W(nu)/pi minus its fixed
peripheral gap. It does not identify the logarithmic curve integral
on the left with that representation volume or pay that deficit.

In particular no global embedding of the positive exterior for all
real z, no analytic continuation of an individual complex saddle
through every branch point, no knot A-polynomial identification, and
no signed original coefficient lower rate is used or asserted.

## Inputs

The [original effective-response theorem](research_global_cap_effective_response_criterion.md),
sections 1–3, supplies the local complex pressure germ and the grounded
ordinary graph. The [pressure/root-measure theorem](research_cap_root_measure_from_classical_pressure.md),
sections 1–2 and 6, supplies the same original odd-level measure and the
exact negative-axis supremum rates. The
[constrained cap capacity](research_cap_constrained_capacity_budget.md),
sections 1–2, retains the original targets and compact concave duality.
The [triangle entropy theorem](actual_triangle_entropy_algebraic_balance.md)
fixes the half-supply normalization and local Legendre potentials.
The [complete packing capacity](actual_smoothed_source_capacity_blocks.md)
identifies the selected complete value with the original drilled volume.
The [one-cap original chain budget](research_one_cap_original_chain_volume_budget.md)
supplies the still separate geometric upper bound discussed after (22).

Preservation changes mathematical formatting and supplies durable links.
No numerical audit, signed coefficient lower asymptotic, arbitrary complex
saddle continuation, knot A-polynomial identification, or general filled
volume theorem is claimed. Inequality (22) remains open.
