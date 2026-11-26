# The actual complete-ended source at the homogeneous wire

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The original one-vertex source with a complete ordinary outside color
has a nonzero packet near the homogeneous internal Fourier wire.
Its phase gradient there is nonzero. Thus a complete cap is not a
homogeneous Fourier endpoint. The result supplies an actual boundary
input for a subsequent local composition; it does not control the
remaining wire periods of a long open chain.

## 1. Source, saddle, and statement

Use the literal source of
[the mixed-vertex theorem](research_internal_pair_three_mixed_packet.md):
\[
 W_N(x,u)=\phi_N\!\left[R^3\mathbf B_N(x)K_N(\cdot,u)\right],
 \qquad C_{N,3}=\exp\{3\pi i(N-1)^2/(4N)\}.
 \tag{1}
\]
Here \(\mathbf B_N\) is the exact half-band cardinal interpolation
in the original quotient, including its physical first normals.
Its factorial representative is
\[
 B_N(x,t)=\frac{N}{
 G_N(N(1/2-x+t/(2\pi))-1/2)
 G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{2}
\]
It agrees with those jets, not necessarily with the canonical ordinary
polynomial at every off-grid spectral color. Its regular-strip phase is
\[
 b(x,t)=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),
 \quad J'(z)=\Log(2\sin\pi z),\quad J(0)=0.
 \tag{3}
\]
Put
\[
 x_h={1\over6}+{i\log2\over2\pi},\quad
 q_h=\cot(\pi x_h)={2\over\sqrt3}-i,\quad T={41\over20},
 \quad \Psi(t)=\psi(t,0).
 \tag{4}
\]
All branches below continue from their regular strips. In particular
\(\Psi(t)=-4J(1/4+t/(4\pi))-4J(1/4-t/(4\pi))\).
The relevant one-angle phase is
\[
 F(x,t;u)=b(x,t)+\psi(t,u)+{3it^2\over4\pi}-it.
 \tag{5}
\]
At \((x,u)=(x_h,0)\), its stationary equation is
\[
 3t+2i\left\{\operatorname{asinh}(\tan(t/2))
      +\operatorname{atanh}(\tan(t/2)/q_h)\right\}=2\pi.
 \tag{6}
\]
There is exactly one zero \(t_h\) of (6) in the disk
\[
 \left|t-\left({1567043151\over10^9}
                   -i{992123761\over10^9}\right)\right|<10^{-8}.
 \tag{7}
\]
The small disk and the inequalities used below are proved by the
outward scalar certificate linked in Section 5. No asymptotic is
deduced from a finite-level numerical sample.

**Theorem 1.** On a fixed complex neighborhood of \((x_h,0)\),
the critical point \(t_c(x,u)\) continues holomorphically, and
\[
 \begin{split}
 W_N(x,u)&=C_{N,3}N^{-1}A(x,u)e^{NS(x,u)}(1+O(N^{-1})),\\
 S(x,u)&=F(x,t_c(x,u);u),\\
 A(x,u)&={i\sqrt{2\pi}\over2\pi}
   {\sin t_c\,a_e(t_c,u)\over
              \sin(\pi x)\sqrt{-F_{tt}(x,t_c;u)}}\ne0.
 \end{split}
 \tag{8}
\]
Here \(a_e\) is the original full-edge amplitude, and the Gaussian
root has positive real part at the central point. The theorem holds
at both parities along all sufficiently large levels. The normalized
error is holomorphic with all fixed parameter derivatives. Evenness
in \(u\) gives the same assertion in the ordinary outside color
\(\zeta=-2\cos u\), including its derivatives at \(-2\).

## 2. The finite source outside the selected angle

Set \(H=-\Im t_h\), \(Y=\Im x_h\), \(M=\Re F(x_h,t_h;0)\).
The certificate proves
\[
 \begin{gathered}
 0<\Re t_h<\pi/2,\qquad \log2<H<107/100,\qquad
 |\cos(t_h/2)|<1,\qquad \Re F_{tt}(x_h,t_h;0)<-1/3,\\
 T<2\pi/3,\qquad -2\cos T\cosh H<3/2,\qquad
 (-\cos T)\cosh H<1,\\
 M-\Re b(x_h,0)>3/5,\qquad
 M-\Re F(x_h,T;0)>1/50,\qquad
 M-\Re F(x_h,T-iH;0)>1/25.
 \end{gathered}
 \tag{9}
\]
Every inequality has a strict reserve. In particular the entire
rectangle \(|\Re t|\le T,\ -H\le\Im t\le0\) maps to a
compact subset of \(\Re(-2\cos t)<2\), and all arguments in
(2) have their real parts strictly inside the regular factorial strip.

First remove the original radical indices from the outside edge,
writing \(K_N=L_N+(K_N-L_N)\), where
\(L_N=\sum_{j=0}^{\lfloor(N-1)/2\rfloor}e_j e_j\).
The radical polynomials have polynomial real-interval norms; hence
their kernel and all fixed real ordinary derivatives have polynomial
bounds by Markov's inequality. They vanish in value at every physical
node. In the full Hermite trace of their product with \(R^3B_N\),
only their first normals can contribute at double nodes; the odd
simple node contributes zero. Original crossing jets cost only powers
of \(N\). The global real-angle factorial estimate bounds the actual
jets of \(B_N\) by a polynomial times \(e^{N\Re b(x_h,0)}\).
Thus the whole removed trace has that rate, below \(M\) by (9).
All fixed outside derivatives are retained. A small complex outside
height costs at most \(e^{N|\Im u|}\), preserving the gap.

Next discard the original physical trace rows with
\(|t|\ge T_N\), where \(T_N\to T\) is a parity-appropriate
midpoint cut. The [real outer-angle bound](research_terminal_real_angle_tail.md)
and the original physical-normal estimates give the kernel rate
\(\Psi(T)\) there, including every required first normal.
The global factorial estimate gives rate \(\Re b(x_h,T)\)
for the other factor: its real-angle derivative is negative on
\(0<t<\pi\), since
\[
 \partial_t\Re b(x,t)={1\over2\pi}
 \log{ |\cos(\pi x+t/2)|\over|\cos(\pi x-t/2)|}<0.
 \tag{10}
\]
The continued upper bound remains valid when a shifted factorial
crosses its real wall. Consequently these discarded actual rows have
rate at most \(\Re F(x_h,T;0)<M-1/50\). Polynomial normal costs
and the \(O(1/N)\) midpoint change preserve a fixed gap.

On the remaining complex rectangle the literal low kernel satisfies
\[
 |\partial_\zeta^k L_N(-2\cos t,\zeta)|_{\zeta=-2\cos u}
 \le C_kN^{a_k}e^{N\{\Re\Psi(t)+|\Im u|\}}.
 \tag{11}
\]
This is [the physical-row interpolation bound](research_free_boundary_half_charge_observation.md),
Lemma 1, on the compact half-plane set just verified, using the
actual last-row Riccati normalization. It is not continuation of a
relative error known only at \(u=0\). At odd levels the complete
last row is literal; the even low complete kernel is supplied by
[its alternating interpolation theorem](research_even_complete_low_kernel.md).
Locally at \(t_h\), the first line of (9) permits the stronger
[full free-edge packet](research_pair_free_boundary_kernel.md),
Theorem 1, with its nonzero \(a_e\). The low kernel has the same
packet. Thus a sharp coefficient is needed only near the saddle,
while (11) controls all the other complex contour pieces.

## 3. The complete angular contour comparison

For positive angles \(0\le\tau\le T\) on the horizontal line
\(t=\tau-iH\), put \(a=1/6\),
\(s=1/2-t/(2\pi)=b+iS\), \(S=H/(2\pi)\).
Then \(a<b\le1/2\), \(S>Y\),
\(a>\alpha(Y)\), and \(b>\alpha(S)\), where
\(\alpha(v)=(2\pi)^{-1}\arccos(\operatorname{sech}(2\pi v))\).
The first height inequality follows from (9); the two alpha tests
are respectively \(\tfrac12\cosh(\log2)<1\) and the last
inequality on the second line of (9). The
[mixed-phase Hessian theorem](research_mixed_wire_phase_concavity.md)
therefore gives strict angular concavity, including \(\tau=0\)
by continuity. Its unique maximum is \(\Re t_h\), since (6)
is the actual zero-lift critical equation. Outside every fixed
saddle neighborhood the positive horizontal contour has a strict gap.

The negative horizontal part is also strictly smaller. For any
\(0\le\tau\le T\), define
\(g(h)=\Re b(x_h,-\tau-ih)-\Re b(x_h,\tau-ih)\).
All individual cosine arguments have real parts in
\((-\pi/2,\pi/2)\); each cosine has positive real part.
The individual logarithms in
\[
 b_t(x,t)={\log\cos(\pi x+t/2)-\log\cos(\pi x-t/2)\over2\pi}
 \tag{12}
\]
are therefore their continued right-half-plane logarithms.
Each \(\Im b_t\) lies strictly between \(-1/2\) and \(1/2\).
Since \(g(0)=0\), integration gives \(|g(h)|<h\) for \(h>0\).
The complete-edge real parts at opposite real angles agree, whereas
the crossing gives a difference \(-3\tau h/\pi\). Hence
\[
 \Re F(x_h,-\tau-ih;0)
 <\Re F(x_h,\tau-ih;0)+(1-3\tau/\pi)h.
 \tag{13}
\]
For \(\tau\ge\pi/3\), (13) and positive-angle concavity prove
a strict gap below \(M\). On \([-\pi/3,0]\) at height \(H\),
both tangent terms have nonnegative real part and \(\Re\sec(t/2)>0\),
so
\[
 -\Re F_{tt}=
 {\Re\tan(\pi x_h+t/2)+\Re\tan(\pi x_h-t/2)
                          +2\Re\sec(t/2)\over4\pi}>0.
 \tag{14}
\]
At \(\tau=0\), the logarithmic cosine modulus has vertical
derivative of absolute value less than one, because
\(\cos(2\pi\Re x_h)=1/2>0\). Thus
\(\Re b_t(x_h,-iH)\ge-Y\), and
\(\partial_\tau\Re F(x_h,-iH;0)\ge3H/(2\pi)-Y>0\).
Concavity makes the phase increasing on that negative interval;
its maximum there is at zero, strictly below the interior positive
maximum. This controls the whole negative horizontal contour.

It remains to retain the vertical endpoint currents. At \(\tau=T\)
and \(0\le h\le H\), write \(s=b+ih/(2\pi)\) with fixed
\(b=1/2-T/(2\pi)>a\), and put
\(u=\Re\cot\pi(s+x_h), v=\Re\cot\pi(s-x_h),
 d=\Re\csc\pi s\). One has \(v,d>0\).
The second line of (9) ensures \(b>\alpha(h/(2\pi))\).
Increasing the real argument from \(b\) to \(a+b\), and then
the height from \(h/(2\pi)\) to \(h/(2\pi)+Y\), gives
\(u<\Re\cot\pi s<d\). Consequently
\(-\Re F_{tt}=(v+2d-u)/(4\pi)>0\) on that side.
The real phase \(h\mapsto\Re F(x_h,T-ih;0)\) is convex,
so its maximum is at \(h=0\) or \(h=H\); both are below
\(M\) by (9). Equation (13) also controls the negative endpoint
at every positive height. All endpoint comparisons persist for
the actual midpoint cuts and nearby parameters.

## 4. Exact trace normalization and local coefficient

Apply the original even full-Hermite residue formula to
\(B_N(x,t)L_N(t,u)\). Its lower horizontal contribution is
\[
 {iN^2 C_{N,3}\over\pi}
 \int_{-T_N-iH}^{T_N-iH}
 {\sin t\,B_N(x,t)L_N(t,u)e^{3iNt^2/(4\pi)}e^{-iNt}
      \over(1-\eta e^{-iNt})^2}\,dt,
 \qquad \eta=(-1)^{N-1}.
 \tag{15}
\]
The two folded vertical endpoint currents are retained, as in the
[exact complete trace formula](research_exact_complete_trace_contour.md).
On a midpoint vertical side their denominator is
\((1+e^{-Nh})^2\), so their exponential weight is at most
\(e^{-Nh}\); Section 3 bounds exactly the phase including this
weight. No periodicity of the Gaussian representative is assumed.
The odd simple node and all even and odd double-node normals are
part of this original residue identity.

On the horizontal side the rational factor is
\(e^{-iNt}(1+O(e^{-NH}))\). Thus all companion trace modes
have a strict gap. Every nonlocal part of (15), both endpoints,
and the physical omissions in Section 2 are strictly below the
saddle. Near \(t_h\), use
\(B_N=e^{Nb}/(2N\sin\pi x)(1+O(N^{-1}))\) and the actual
edge packet \(L_N=N^{-3/2}a_e e^{N\psi}(1+O(N^{-1}))\).
The one-dimensional Gaussian then gives (8):
\(N^2N^{-1}N^{-3/2}N^{-1/2}=N^{-1}\), with the indicated
factor \(i\sqrt{2\pi}/(2\pi)\).

The strictly negative real Hessian, nonzero local amplitude, and
all strict global gaps persist for a small fixed complex change of
\(x\) and the ordinary outside color. The implicit-function theorem
and a local holomorphic deformation through the perturbed saddle
give the uniform statement, while (11) retains the complementary
source bounds. Cauchy's formula gives the derivative assertions.

## 5. Gradient, scope, and reproduction

At the homogeneous wire this complete-ended phase is not stationary
in the wire variable. Its exact derivative formulas are
\[
 \begin{split}
 S_x&=\log\cos(\pi x+t_c/2)+\log\cos(\pi x-t_c/2)
                                      -2\log\sin(\pi x),\\
 S_{xx}&=b_{xx}-{b_{xt}^2\over F_{tt}},\\
 b_{xx}&=-\pi\{\tan(\pi x+t_c/2)+\tan(\pi x-t_c/2)
                                               +2\cot(\pi x)\},\\
 b_{xt}&=\tfrac12\{\tan(\pi x-t_c/2)-\tan(\pi x+t_c/2)\}.
 \end{split}
 \tag{16}
\]
The certificate encloses
\(S_x(x_h,0)\simeq0.08113094-0.36386323i\) and
\(S_{xx}(x_h,0)\simeq-10.99607573+7.70214454i\).
The quantities are derivatives of the actual source phase in (8).
They are not set to zero by replacing the complete cap with the
homogeneous Fourier endpoint.

Run `python3 experiments/check_homogeneous_wire_complete_cap.py`.
The [record](../repro/results/research-homogeneous-wire-complete-cap.json)
contains the outward Rouché disk and the finite list of scalar gaps,
as well as source-dependency hashes. The analytic contour estimates
are the proof above, not an inference from parameter sampling.
The theorem gives one genuine boundary input near the homogeneous
wire. Propagation across a retained vertex still requires a justified
critical point in a common chart; controlling the complementary wire
integrals of an arbitrary open chain remains separate.

## 6. A quantified directed domain for the same actual cap

The fixed neighborhood in Theorem 1 can be extended in the direction
of the expected attachment displacement. Define the compact
parallelogram
\[
 \mathcal C=\left\{x={1\over6}+r+
 i\left({\log2\over2\pi}-{4r\over5}+s\right):
 0\le r\le{13\over1000},\quad
 -{3\over2000}\le s\le{1\over1000}\right\}.
 \tag{17}
\]
**Corollary 2.** The actual source packet (8) holds uniformly on a
complex neighborhood of \(\mathcal C\), with a fixed small ordinary
outside-color neighborhood, both parities, and all fixed ordinary
derivatives. Its selected critical point is the unique zero of (6),
with \(q_h\) there replaced by \(q(x)=\cot(\pi x)\), in the
common rectangle
\[
 {38\over25}<\Re t_c<{63\over40},\qquad
 {97\over100}<-\Im t_c<1.
 \tag{18}
\]
This is a quantitative domain for the cap input. No assertion that a
subsequent composed-wire saddle lies in \(\mathcal C\) is included.

*Proof.* Use the real midpoint cut tending to
\(T(x)=\pi-2\pi\Re x-1/50\). Its regular factorial margin is
exactly \(1/(100\pi)\), independently of \(x\). The
[directed-domain certificate](../experiments/certify_homogeneous_wire_cap_corridor.py)
and its [record](../repro/results/research-homogeneous-wire-cap-corridor.json)
cover (17) by 580 closed rational parameter boxes. An exact rational
vertical sweep verifies multiplicity-one coverage away from shared
faces. Every box proves the following strict properties:

- the period zero has a uniform Rouché disk strictly inside (18);
- the actual logarithms in the period are regular throughout (18),
  with \(\Re f_t>0\) on that whole common rectangle;
- at the zero, \(\Re t_c<\pi/2\),
  \(2\pi\Im x< H=-\Im t_c<107/100\),
  \(|\cos(t_c/2)|<1\), and \(-\Re F_{tt}>1/4\);
- \(\pi/2<T(x)<2\pi/3\), all contour colors obey
  \(\Re(-2\cos t)<7/4\), and both alpha conditions used in
  Section 3 hold;
- the radical omission has gap greater than \(1/2\), and both
  \(t=T(x)\) and \(t=T(x)-iH\) have gap greater than \(1/1000\)
  below \(\Re F(x,t_c;0)\).

Here \(f(t,x)\) denotes the left side of the period equation minus
\(2\pi\). The certificate chooses only the centers of its Rouché
circles numerically, then rounds them to explicit rational numbers.
All accepted inequalities use outward ball arithmetic. The exact
parameter derivative used to control the residual is
\[
 f_x(t,x)=\frac{2\pi i z(1+q^2)}{(q-z)(q+z)},
       \qquad z=\tan(t/2),\quad q=\cot(\pi x).
 \tag{19}
\]
For each parameter box, the mean-value bound from (19), followed by
the analytic Taylor bound in \(t\), proves the Rouché inequality
uniformly on the box. The positive real part of \(f_t\) on the
common convex rectangle proves univalence there by integration along
line segments. Thus the local zeros on overlapping boxes are the
same branch, and continue the zero from (7).

The critical phase is enclosed without inserting a first-order
error from a loose root box. If its circle has center \(c\) and
radius \(R\), then \(F_t=if/(2\pi)\) gives the rigorous bound
\[
 |F(x,t_c;0)-F(x,c;0)|
 \le {R\over2\pi}|f(c,x)|
       +{R^2\over4\pi}\sup_{|t-c|\le R}|f_t(t,x)|.
 \tag{20}
\]
The certified endpoint gaps use this bound, not sampled phase values.

All analytic comparisons of Sections 2--4 now hold uniformly on
(17). In particular \(\Re x\ge1/6\) preserves the nonnegative
tangent real parts on \([-\pi/3,0]\), while
\(\Re x<1/4\) preserves the cosine-modulus derivative bound at
zero. The chosen cut keeps every cosine in (12) in its right
half-plane. The same strict concavity and height convexity therefore
control the entire positive and negative horizontal intervals and
both original vertical currents. The low-kernel half-plane bound is
uniform by compactness; the selected angles stay in a fixed compact
subset of the actual free-edge packet domain.

Each strict inequality persists on a neighborhood of its parameter
box. A finite cover gives a common neighborhood of \(\mathcal C\)
and a common small ordinary outside-color disk. Although \(T(x)\)
is expressed using \(\Re x\), holomorphy is not being inferred from
that contour choice: near each fixed parameter one can hold its cut
fixed because the gaps are strict. The original source, selected
phase, and normalized packet then agree on overlaps. This proves
the asserted uniform holomorphic packet and its derivatives.
\(\square\)

Reproduce the continuum certificate with
`python3 experiments/certify_homogeneous_wire_cap_corridor.py`.
Its scope is the one-cap source on (17). It supplies neither a
global open-chain estimate nor an enclosure of every geometric
attachment wire in that parallelogram.
