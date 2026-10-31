# The actual signed color packet through the quarter-index boundary

31 October 2026. Internally reviewed local source theorem. This extends the LOCAL original
mixed-color coefficient theorem across $x=1/4$. The selected branch has a
source-fixed nonzero amplitude on a fixed joint complex neighborhood, with
an exponentially small relative error on the physical Newton grid. Both
transport channels and every conversion error are retained in the proof.
No global alias estimate, full filled-volume theorem, or arbitrary-syntax
geometric theorem is inferred here.

The exact inputs are the [selected mixed-inner source](actual_pretzel_mixed_inner_source_wkb.md), §§1–6;
the [analytic diagonalization lemma](actual_local_analytic_transport_action_barrier.md), §§1–3;
the [complete-color crossing proof](actual_complete_circle_boundary_packet.md), §§2–3; and
the [signed Conway packet](actual_odd_conway_complex_color_packet.md), §§1–5. The last complete-color
crossing proof is used as a template, not as a mixed-color identification:
the literal mixed finite sum and its recurrence are printed below.

## 1. Literal source, parameters, and result

Put $d=N-1$, $M=\lfloor d/2\rfloor$, $q=e^{\pi i/N}$, $Q=q^2$,
$\kappa=q^{d^2/2}$, $F_j=(Q;Q)_j$, and $t=h/N$. For a physical integer
$r>|\operatorname{Re}h|$ define the specified continuation
of the original finite source by

\[
\begin{aligned}
A_{h,r}&=\sum_{v=r}^{M}
 \frac{Q^{-vr}F_{2v}}{F_v\widehat F_N(v-h)\widehat F_N(v+h)F_{v-r}},\\
D_{h,r}&=\frac{Q^{-r^2}F_{2r}}
 {F_r\widehat F_N(r-h)\widehat F_N(r+h)},&
U_{h,r}&=\frac{A_{h,r}}{D_{h,r}}.
\end{aligned}\tag{1}
\]

Here $\widehat F_N$ is exactly the [marked factorial completion](exact_factorial_interpolation_and_complex_contours.md) of the original
source, not an independently selected solution. At physical integer
$h\ge0$ with $h\le r$, (1) is the actual low-core coefficient normalization.
For r in a fixed neighborhood of N/4, all shifted factorial arguments
remain in regular compact substrips after choosing a small fixed complex
t disk. In particular (1) is holomorphic and even in t. Its terminal
source is $U_{h,M}=1$.

Write $\varepsilon=1/N$, $x=r/N$, $Y=e^{2\pi i x}$, $H=e^{2\pi i t}$, and

\[
\operatorname{den}(x)=(1-QY/H)(1-QYH).
\]

The exact recurrence, including the terminal wall, is

\[
\begin{aligned}
U_r&=p(x,t,\varepsilon)U_{r+1}+q_c(x,t,\varepsilon)U_{r+2},\\
p&=-\frac{Q^{-2}Y^{-1}[(H+H^{-1})Q^3Y^2+Q+1]}
 {\operatorname{den}(x)},\\
q_c&=-\frac{Q^{-4}Y^{-2}(1-Q^2Y)(1-Q^3Y^2)(1+Q^2Y)}
 {\operatorname{den}(x)\operatorname{den}(x+\varepsilon)},\\
q_c((M-1)/N,t,1/N)&=0,&
U_{M-1}&=p((M-1)/N,t,1/N).
\end{aligned}\tag{2}
\]

The wall zero is literal at both parities and for every complex t in
this corridor. No $D_{h,M+1}$ is divided out. The exact Ward telescoping
proof of (2) continues to this factorial completion because its lower
endpoint is $v=r$. Thus the parameter extension in this note is attached
to the original source itself.

Set $p_0=p(x,t,0)$ and $q_0=q_c(x,t,0)$. Let $\mu_s,\mu_f$ be the two
analytic roots of $\mu^2-p_0\mu-q_0=0$, labeled
at $t=0$ by

\[
\mu_s(x,0)=-Y^{-1},\qquad
\mu_f(x,0)=Y^{-1}\cot^2(\pi x).\tag{3}
\]

The selected logarithm is continued from $\operatorname{Log}\mu_s(1/2,t)=0$. Define

\[
\begin{aligned}
S(x,t)&=\int_x^{1/2}\operatorname{Log}\mu_s(u,t)\,du,\\
\nu&=\frac{p_1+q_1/\mu_s-q_0(\partial_x\mu_s)/\mu_s^2}
 {1+q_0/\mu_s^2},\\
C(x,t)&=\sqrt{\mu_s(x,t)}\exp\!\left[
 \int_x^{1/2}\frac{\nu(u,t)}{\mu_s(u,t)}\,du\right].
\end{aligned}\tag{4}
\]

$p_1,q_1$ are the $\varepsilon$ derivatives of the exact rational functions
(2) at zero. All marks in (4) continue the established high-index ones.

**Local quarter theorem.** There exist fixed $h_0,t_0,a_0,c>0$ and,
for every sufficiently large N of either parity, a zero-free holomorphic
function $I_N(x,t)$ on

\[
|\operatorname{Re}x-1/4|<h_0,\qquad
|\operatorname{Im}x|<a_0,\qquad |t|<t_0,
\]

such that, uniformly for physical $r/N$ in the smaller real interval and
all complex $|t|<t_0$,

\[
\begin{aligned}
U_{Nt,r}&=I_N(r/N,t)[1+O(e^{-cN})],\\
I_N(x,t)&=C(x,t)e^{NS(x,t)}[1+O(N^{-1})].
\end{aligned}\tag{5}
\]

The second estimate is uniform holomorphically on a fixed smaller joint
domain. The constants and domains are independent of N. The first is a
relative source-grid assertion and the second a complex asymptotic of
the explicit interpolant; they are different estimates.

## 2. Uniform analytic diagonalization before choosing the crossing width

Set $X_r=(U_r,U_{r+1})^{\mathsf T}$ and
$T_N=\begin{pmatrix}p&q_c\\1&0\end{pmatrix}$. The exact direction
is $X_r=T_N(x_r,t)X_{r+1}$, from high index to low index.

First choose a fixed regular complex neighborhood of $x_0=1/4$ and a
fixed sufficiently small t disk. At $(x_0,0)$, the roots in (3) are $i,-i$.
On the closure of a small enough neighborhood they remain distinct,
nonzero and bounded, with a bounded analytic eigenframe $V_0$ whose
columns are $(\mu_s,1)^{\mathsf T}$ and $(\mu_f,1)^{\mathsf T}$. All denominators in (2) are
bounded away from zero. The exact rational $T_N$ equals $T_0+O(1/N)$
uniformly there, including all t in the chosen disk.

Apply the proved analytic diagonalization lemma with reversed shift
direction. Its matrix commutator construction is holomorphic in the
additional parameter t and uses only uniform coefficient, inverse-frame,
nonzero-root and eigenvalue-gap bounds. It supplies a COMPUTABLE fixed
$\sigma>0$, bounded holomorphic $V_N,V_N^{-1}$, and diagonal $D_N$ such that

\[
\begin{aligned}
V_N(x,t)^{-1}T_N(x,t)V_N(x+\varepsilon,t)&=D_N(x,t)+R_N(x,t),\\
V_N&=V_0+O(\varepsilon),\\
D_N&=\operatorname{diag}(\mu_s,\mu_f)+O(\varepsilon),\\
\|R_N\|&\le C e^{-\sigma N}.
\end{aligned}\tag{6}
\]

Each diagonal entry is nonzero. Its first component in the selected
column is also nonzero. These assertions hold on a fixed smaller
complex neighborhood. All bounds are uniform in the small t disk.
The diagonalization is performed BEFORE shortening the crossing window;
$\sigma$ therefore does not shrink with that subsequently chosen window.

The lemma's construction can be taken even in t: its initial rational
coefficients, labeled roots, and every commutator correction are even.
No ratio of physical source values, and no putative already-selected
solution, is used to construct $V_N$ or $D_N$.

## 3. A negative cumulative competitor action survives complex colors

Choose $\delta>0$ small and set $h=\delta/4$. Here this width $h$ is
distinct from the color index in (1). Let the high anchor be the actual
integer $b_N=\lceil N(x_0+2\delta)\rceil$ and $x_b=b_N/N$. We work
with targets $|x-x_0|\le h$. The entire interval $[x_0-h,x_b]$ lies in the regular domain.

At $t=0$, the relative log modulus is

\[
f(x)=\log|\mu_f/\mu_s|=2\log\cot(\pi x),\qquad
f(x_0)=0,\qquad f'(x)=-\frac{4\pi}{\sin(2\pi x)}.\tag{7}
\]

Shorten $\delta$ so $-8\pi\le f'\le-4\pi$. If $x\le x_0$, the
possible positive contribution from $x$ to $x_0$ is at most $4\pi h^2$,
whereas the negative contribution from $x_0$ to $x_0+2\delta$ is at most
$-8\pi\delta^2$. If $x\ge x_0$, integrate directly from $x$ to
$x_0+2\delta$. Consequently,
uniformly in the whole target interval,

\[
\int_x^{x_b}\log\left|\frac{\mu_f(u,0)}{\mu_s(u,0)}\right|du
\le-7\pi\delta^2+O(N^{-1}).\tag{8}
\]

All partial relative actions along the anchor-to-target interval have
absolute value at most $C_0\delta^2+O(N^{-1})$, for a fixed explicit
coefficient bound $C_0$; for example $C_0=40\pi$ suffices here.

On the fixed regular domain an analytic logarithm of $\mu_f/\mu_s$ exists.
Its even parameter dependence gives

\[
\left|\operatorname{Log}(\mu_f/\mu_s)(x,t)
-\operatorname{Log}(\mu_f/\mu_s)(x,0)\right|
\le C_1|t|^2.\tag{9}
\]

This is a complex-parameter estimate; taking real parts controls actual
moduli for every complex $t$. Choose $\delta$ first with
$C_0\delta^2<\sigma/8$. Then choose $t_0$ smaller so
$3C_1\delta t_0^2<\pi\delta^2$. Equations
(8)–(9), ordinary uniform Riemann estimates, and $D_N=\mu+O(1/N)$ give

\[
\begin{aligned}
|G_f(r)/G_s(r)|&\le C e^{-6\pi\delta^2N},\\
\max_{\mathrm{partial}}\left|\log|G_f/G_s|\right|
&\le N\sigma/4+O(1).
\end{aligned}\tag{10}
\]

for target r and along the full propagation interval, respectively.
Here $G_i(r)=\prod_{j=r}^{b_N-1}d_i(x_j,t)$ and $G_i(b_N)=1$.
The two statements have different domains: the strict negative bound
is for targets near quarter; the width bound covers ALL partial products.
The $O(1)$ rounding and diagonal-correction costs are uniform.

Thus the fast branch may locally exceed the selected branch below
quarter, but its ACCUMULATED action from the actual high anchor is
still strictly smaller on this sufficiently short target interval.
This is the extra information not supplied by eigenvalue separation.

## 4. Exact source anchor, both channels, and all conversion errors

At $x_b$, the established high-index theorem applies uniformly for all
complex $|t|<t_0$, since $x_b$ is a fixed positive distance above quarter.
It gives the actual source vector and the ratio to its next coordinate.
In the frame (6), write

\[
V_N(x_b,t)^{-1}X_{b_N}
=\begin{pmatrix}a_{s,N}(t)\\a_{f,N}(t)\end{pmatrix}.
\]

Its exact entries are defined by the original finite sums (1). The high
theorem and $V_N=V_0+O(1/N)$ imply

\[
\begin{aligned}
a_{s,N}(t)&=\frac{C(x_b,t)}{\mu_s(x_b,t)}
 e^{NS(x_b,t)}[1+O(N^{-1})],\\
|a_{f,N}/a_{s,N}|&\le C/N.
\end{aligned}\tag{11}
\]

In particular $a_{s,N}$ is holomorphic and zero-free after shrinking the
fixed disk, uniformly for large N. Neither coefficient is set to zero.
The uniform relative form in (11), not a bound at $t=0$ alone, is used.

For completeness the exact interaction calculation is as follows.
Write $Y_r=V_N(x_r,t)^{-1}X_r$ and
$G_r=\operatorname{diag}(G_s(r),G_f(r))$. Then

\[
G_r^{-1}Y_r=(I+E_r)G_{r+1}^{-1}Y_{r+1},\qquad
E_r=G_r^{-1}R_N(x_r,t)G_{r+1}.
\]

By the partial width bound (10),

\[
\|E_r\|\le C e^{-3\sigma N/4},\qquad
\prod_r(I+E_r)=I+O(Ne^{-3\sigma N/4}).\tag{12}
\]

The $1/d_i$ factors are uniformly bounded. Factoring $a_{s,N}$ and using
(10)–(12) in the first component gives, on the target grid,

\[
U_r=a_{s,N}(t)[V_N(x_r,t)]_{1,s}G_s(r)
[1+O(e^{-c_1N})].\tag{13}
\]

The direct fast source component is bounded by $N^{-1}$ times its strict
negative relative action; its converted contributions are bounded by
(12) with the full calibrated action width. Formula (13) therefore
does not discard a Stokes multiplier, reset any action, or suppose that
an $O(1/N)$ local error remains small under an uncontrolled long product.

## 5. Exponentially accurate interpolation of the selected product

Let $l_N(x,t)=\operatorname{Log}d_s(x,t)$ on the fixed regular tube, with the mark
continuing $\operatorname{Log}\mu_s$. The functions $l_N$ and all their Cauchy derivative
bounds are uniform in $N,t$ on a slightly smaller fixed tube.
For physical $r\le b_N$ let $E_N^s(x,t)$ be the optimally truncated analytic
Euler–Maclaurin expression for

\[
\sum_{j=r}^{b_N-1}l_N(j/N,t):
\]

\[
\begin{aligned}
E_N^s(x,t)&=N\int_x^{x_b}l_N(u,t)\,du
 +\frac{l_N(x,t)-l_N(x_b,t)}2\\
&\quad+\sum_{k=1}^{K}\frac{B_{2k}}{(2k)!}N^{1-2k}
 \left[\partial_x^{2k-1}l_N(x_b,t)-\partial_x^{2k-1}l_N(x,t)\right].
\end{aligned}\tag{14}
\]

Choose $K=\lfloor c_2N\rfloor$ with a sufficiently small fixed $c_2>0$.
On the fixed tube, Cauchy gives $|l_N^{(k)}|\le Bk!a^{-k}$. The usual
analytic remainder bound $CN[K/(\pi aN)]^{2K}$ is therefore exponentially small,
uniformly for the physical grid and complex t. This gives

\[
I_N(x,t)=a_{s,N}(t)[V_N(x,t)]_{1,s}e^{E_N^s(x,t)}.\tag{15}
\]

All three factors are holomorphic and zero-free on the fixed smaller
domain. The anchor is an explicitly known finite source coefficient,
not an unknown closed invariant. Equations (13)–(15) prove the first
assertion of (5). There is no need to interpolate or estimate a moving
support cutoff: r and the anchor remain physical integers and the
factorial continuation in t was already fixed in (1).

## 6. The leading action and amplitude are the original selected ones

The selected vector from (6), propagated only with $d_s$, satisfies the
original scalar recurrence up to an exponentially small holomorphic
relative defect. One can see this from both rows of the exact matrix
identity (6), since its first component and $d_s$ are nonzero. Its scalar
one-step ratio is

\[
v_{s,N}(x,t)=d_s(x,t)
\frac{[V_N(x,t)]_{1,s}}{[V_N(x+\varepsilon,t)]_{1,s}}.
\]

It satisfies $v_{s,N}=\mu_s+O(\varepsilon)$, with corresponding derivative bounds,
and its Riccati residual is exponentially small. Expanding that residual
to first order yields

\[
v_{s,N}=\mu_s+\varepsilon\nu+O(\varepsilon^2).\tag{16}
\]

with EXACTLY $\nu$ from (4). The denominator
$1+q_0/\mu_s^2=1-\mu_f/\mu_s$ is bounded away from zero, even at quarter;
there it equals two at $t=0$. To justify the expansion without a formal
series assumption, Cauchy bounds give derivatives of $v_{s,N}-\mu_s$ of
order $O(\varepsilon)$; substituting $v_{s,N}=\mu_s+O(\varepsilon)$ in the exact
Riccati defect then solves its first-order coefficient with $O(\varepsilon^2)$
remainder by this nonzero denominator.

The eigenvector ratios telescope. Euler–Maclaurin applied to (16)
therefore gives the selected first component between x and $x_b$ as

\[
\sqrt{\frac{\mu_s(x,t)}{\mu_s(x_b,t)}}
\exp\!\left[N\int_x^{x_b}\operatorname{Log}\mu_s(u,t)\,du
 +\int_x^{x_b}\frac{\nu(u,t)}{\mu_s(u,t)}\,du\right]
[1+O(N^{-1})].\tag{17}
\]

This is a holomorphic estimate, not an extrapolation from its real grid
values. Explicitly, writing $v_1=[V_N]_{1,s}=\mu_s+O(\varepsilon)$, Cauchy
also gives $v_1'=\mu_s'+O(\varepsilon)$, and (16) implies

\[
d_s=\mu_s+\varepsilon(\nu+\partial_x\mu_s)+O(\varepsilon^2).
\]

Insert this expansion directly into (14). The additional integral of
$\mu_s'/\mu_s$ is $\operatorname{Log}\mu_s(x_b)-\operatorname{Log}\mu_s(x)$;
together with the half-endpoint term and $v_1(x)/v_1(x_b)$, it gives the
square root in (17). The remaining
Bernoulli terms and integrated $O(\varepsilon^2)$ error are uniformly $O(1/N)$
on the smaller complex tube. Thus no uniqueness principle on a finite
grid is being used to obtain complex uniformity.

At the anchor, $a_{s,N}[V_N]_{1,s}$ equals
$C(x_b,t)e^{NS(x_b,t)}[1+O(N^{-1})]$ by (11). Multiplying (17) proves
the second assertion of (5), with the original C and S in (4), uniformly
holomorphically on a smaller fixed tube. The endpoint normalization at
$1/2$ and BOTH parity marks came from the high-source theorem; no new
connection or endpoint constant appears at quarter.

At $t=0$ this recovers, on both sides of quarter,

\[
S(x,0)=i\pi(1/2-x)^2,\qquad
C(x,0)=\sqrt{\sin(\pi x)}e^{-3\pi i(1/2-x)/2}.\tag{18}
\]

The exponential grid residual and the inverse-N leading expansion
remain separate throughout this proof.

## 7. Original signed Conway coefficients and the local wire packet

Keep the exact finite coefficients $d_N^\epsilon(r,t)$, the removed phase
$e^{-i\epsilon\pi d/4}$, and the continuous chirp of
[signed Conway packet](actual_odd_conway_complex_color_packet.md), §§1–3. For the negative sign,
replace only its high-source interpolation $e^{E_N}$ by $I_N$ in (15).
Here $\epsilon\in\{0,1,-1\}$ is the physical half-twist sign, distinct
from the step size $\varepsilon=1/N$:

\[
\begin{aligned}
A_N^{\mathrm{hol}}(x,t)&=
 \frac{N^2G_N(2Nx)}{G_N(Nx)^2G_N(N(x-t))G_N(N(x+t))},\\
P_N(x)&=\frac{\kappa^{-1}e^{i\pi d/4}}
 {e^{-i\pi Nx+i\pi Nx(Nx+1)/N}},\\
I_N^-(x,t)&=A_N^{\mathrm{hol}}(x,t)P_N(x)I_N(x,t).
\end{aligned}\tag{19}
\]

These are the SAME canonical factorial and chirp marks. Their exact
source identity uses
$q^{h^2}D_{h,r}/D_{0,r}=G_N(r)^2/[G_N(r-h)G_N(r+h)]$;
hence no quadratic color factor is lost.
At physical r, (19) agrees with the normalized literal negative core
coefficient up to the relative exponential residual in (5).
For the positive sign use its Schwarz reflection in x,t; for the pure
sign use $A_N^{\mathrm{hol}}$ itself. All are even holomorphic in t.

The leading formulas are unchanged:

\[
\begin{aligned}
I_N^\epsilon(x,t)&=N^{1/2}b_\epsilon(x,t)
 e^{Nf_\epsilon(x,t)}[1+O(N^{-1})],\\
f_0(x,t)&=g(x,t),\\
f_-(x,t)&=g(x,t)+S(x,t)-S(x,0),\\
f_+(x,t)&=\overline{f_-(\overline x,\overline t)}.
\end{aligned}\tag{20}
\]

where $g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t)$. The old explicit $b_\epsilon$
are nonzero and analytically extend through $x=1/4$. In particular

\[
\begin{aligned}
\frac{b_\epsilon(x,0)}{b_0(x,0)}
&=\sqrt{\sin(\pi x)}e^{-i\epsilon\pi x/2},
&&\epsilon\in\{-1,1\},\\
\partial_t^2 f_\epsilon(x,0)
&=-\frac{2\pi\cot(\pi x)}{1-\epsilon i\cot(\pi x)},
&&\epsilon\in\{0,-1,1\}.
\end{aligned}\tag{21}
\]

The implicit shear identity for $f_\epsilon$ continues across quarter by
the identity theorem on the common connected neighborhood. Its derivative
$1-\epsilon i\cot(\pi x)$ remains nonzero there. This is identification of
the already selected source action, not an inference from its Hessian.

Consequently the existing finite tensor-cotangent/local Gaussian proof
extends to any FIXED strict wire window whose leaf coordinates lie in
the union of this quarter neighborhood and the previously proved high
intervals, provided its original pure wire Hessian is negative definite
and its primitive lattice and support are retained. Bound the exponential
coefficient residuals absolutely before the complex wire saddle, then
shrink the fixed color polydisk so they remain below the selected action.
The exact finite window still has $N^{3/2}$ amplitude, all original affine
offsets, the external $\eta_N$ phase and the diagonal color Hessian (21).
The shifted critical wire stays in the fixed interpolation tubes.

This conditional LOCAL consequence applies to the strict quarter leaves
of the test family $C(hT(h^s))$ once its already identified strict lattice
window is supplied. It is not by itself a whole-source or filling claim.

## 8. Scope, parameter order, and remaining obligations

The order of constants is essential: fix the rational analytic recurrence
domain and its uniform diagonalization barrier; choose a much shorter
anchor-to-target interval; retain its negative cumulative relative action;
then choose a small complex-color disk. Choose the EM tube and truncation
on fixed domains. Finally let N tend to infinity through both parities.
All target and color radii are fixed positive numbers, not shrinking with N.

Neither root separation nor an $O(1/N)$ local transport approximation would
prove (5). Equations (8)–(13) explicitly control the actual other source
channel and exponentially small mode conversions with their accumulated
actions. The extension only crosses a short regular modulus boundary; it
does not continue the selected branch arbitrarily far below quarter.

No omitted low-core indices, alias sectors, physical-color complements,
root-leaf geometry or global boundary currents have been set to zero.
Global source gaps and the actual marked peripheral geometry remain the
separate hypotheses of the long-filling transfer theorem. This note gives
a local analytical input that was previously unavailable, with its exact
source normalization preserved.

## Internal review and preservation

The primary agent and geometry agent independently completed full analytical
and source reviews of §§1–8. They checked the literal factorial continuation,
both terminal parities, the source anchor and both channels, the uniform
complex-parameter action barrier, interaction-picture errors, holomorphic
Euler–Maclaurin interpolation, first-order Riccati correction and endpoint
normalization, and the signed chirp/shear/local-window consequence. Neither
review infers a global source gap or a new volume theorem. These are internal
research reviews, not external peer review. No numerical calibration is used
as an asymptotic proof, and no new runtime audit is needed for this analytic
extension. The native mathematical presentation and relative links are
validated separately.
