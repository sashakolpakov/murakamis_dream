# A full spectral-strip gap for an original cap and its whole CROSS star

31 October 2026. **Internally reviewed analytical research theorem, unpublished.**
Root and an independent geometry reviewer completed full proof/source reviews.
The cap varies
in a small COMPLEX disk about +2; every neighboring CROSS spectrum may
range over the ENTIRE real fold, with a sufficiently thin fixed complex
strip. This is a relative weighted star theorem, not an absolute Phi_D
bound. The original face targets and both parity cutoffs remain unchanged.

## 1. Original source and theorem

Let F=(u,A,v,C) be an original marked cap, with u=v=0 and A,C ordinary.
Include EVERY other original A-incident port in a product of k genuine
CROSS coupons. The valence k is fixed with the original diagram but
otherwise arbitrary. Remove the fixed common raw signs and write

\[
\begin{aligned}
P_N^{\boldsymbol\delta}(A,Y)&=\prod_eP_{e,\mathrm{CROSS}}(A,Y;\sigma(\delta_e)),\\
\sigma(\delta)&=-2\cos(2\pi\delta),\\
P_N^0(A,Y)&=P_N^{\boldsymbol\delta}(A,Y)\big|_{\boldsymbol\delta=0}.
\end{aligned}\tag{1}
\]

The endpoint product has nonnegative coefficients at both parities.
All shared variables remain identified. The actual finite CROSS degree
projections are unchanged as the spectra vary.

Fix positive ordinary radii, protected variables exactly zero, with
L_A=L_C. Write P_N^+(a)=P_N^0(a,L_Y). The actual endpoint weighted
action has the locally uniform real limit

\[
\frac1N\log P_N^+(L_Ce^t)\longrightarrow F(t),\qquad
F\text{ differentiable at }0,\qquad0<\nu:=F'(0)<\frac12.\tag{2}
\]

The derivative condition is the substantive scalar hypothesis. At a
classified stationary cap with only CROSS neighbors it follows from
the SAME original demand: L_A=L_C and
F'(0)=sum_(e!=F) q_(e,A)=1-q_(F,A)=nu in (0,1/2).

Put d=N-1 and M=floor(N/2)-1. For cap spectrum sigma the ORIGINAL
projected polynomial and the extracted star are

\[
\begin{aligned}
H_{F,\mathrm{cap}}(A,C;\sigma)&=\sum_{j=0}^M(-1)^jb_j(\sigma)A^{d-j}C^j,\\
B_N(Y;\sigma,\boldsymbol\delta)&=[A^d]H_{F,\mathrm{cap}}P_N^{\boldsymbol\delta}.
\end{aligned}\tag{3}
\]

**Theorem.** There are fixed epsilon_*>0, h_*>0, eta>0 and N_0 such that

\[
\sup_{\substack{|\sigma-2|\le\varepsilon_*\,,\ |\operatorname{Im}\delta_e|\le h_*\\
\operatorname{Re}\delta_e\in\mathbb R\,,\ |Y_f|=L_f}}
|B_N(Y;\sigma,\boldsymbol\delta)|
\le e^{-\eta N}P_N^+(L_C),\qquad N\ge N_0.\tag{4}
\]

Both parities and every remaining face phase are included. This
extracts exactly the original A^d against the WHOLE neighboring
product; it is not a shifted demand or an independent allocation at
each neighbor.

## 2. Root-safe cap factors and the exact global CROSS majorant

Set theta=pi/N and

\[
\begin{aligned}
c_j&=2\cos((2j+1)\theta),&s_j&=2\sin(j\theta),\\
B_j&=\prod_{r=1}^js_r^2,&b_j(\sigma)&=B_j\prod_{r=j+1}^d(\sigma-c_r),\\
U_j&=b_j(2),&\gamma_j&=2-c_j>0.
\end{aligned}
\]

These are the full original unused-row products, also at repeated
spectral roots. They satisfy the polynomial relation

\[
(\sigma-c_{j+1})b_{j+1}(\sigma)=s_{j+1}^2b_j(\sigma).\tag{5}
\]

For j<=M, the explicit increasing-sine ratios give
U_j<=U_0=csc^2(theta/2)<=C N^2. Since product gamma_j=4 and
chi_N(z)=2T_N(z/2)+2, for |sigma-2|<=epsilon_s,

\[
|b_j(\sigma)|\le U_j\prod_{r>j}\left(1+\frac{\varepsilon_s}{\gamma_r}\right)
\le CN^2e^{N\kappa_s},\qquad
\kappa_s=\operatorname{arcosh}(1+\varepsilon_s/2).\tag{6}
\]

There is no division by b_j, chi_N, or a varying spectral factor.
This polynomial estimate is used near every endpoint or sampled
zero outside the strict row interval below.

The original cofactor interpolation theorem supplies the stronger,
GLOBAL coefficientwise CROSS bound, on any fixed strip |Im delta|<=T,

\[
|P_{e,\mathrm{CROSS}}(\sigma(\delta))|_{\mathrm{coeff}}
\le C_T\log^2(N+1)e^{2\pi d|\operatorname{Im}\delta|}
P_{e,\mathrm{CROSS}}(-2).\tag{7}
\]

This is equation (27) of [the original cofactor factorization](actual_cross_cofactor_factorization.md),
section 8, not an inferred coefficient lower asymptotic. Its nodal
positivity covers ALL j,a<=J: for j<=a it is the direct positive
original recurrence; for j>a it is the retained physical tail adapter.
Thus the plain coefficient majorant includes j=J-1 at all nodes.
Its central coefficientwise comparisons use (x+y)^2>=2xy, with the
original forced outer units retained.

Taking products in (7), even when face variables are shared, yields

\[
|P_N^{\boldsymbol\delta}|_{\mathrm{coeff}}
\le Q_N\exp\!\left(2\pi d\sum_e|\operatorname{Im}\delta_e|\right)P_N^0.\tag{8}
\]

where Q_N is a fixed polynomial upper bound in N on a fixed strip.
For later rate estimates put

\[
\omega=\kappa_s+2\pi\sum_e|\operatorname{Im}\delta_e|.\tag{9}
\]

## 3. Actual MAIN-edge angular loss on the whole neighbor fold

The triangle on the opposite side of original MAIN edge AC from
(u,A,C) belongs to a different port in P_N^delta. It contains the two
supported positive variables A,C. Fix phi_0 in (0,pi/8) and a small
radial interval |t|<=T_0. The reviewed cofactor angular theorem gives
gamma>0 and a FIXED strip height h_0>0 such that

\[
\begin{aligned}
|P_N^{\boldsymbol\delta}(Ce^{t+i\phi},Y)|
&\le CN^K\exp\!\left(2\pi d\sum_e|\operatorname{Im}\delta_e|-\gamma N\right)P_N^+(L_Ce^t),\\
\phi_0\le|\phi|\le\pi,\quad |t|&\le T_0,\quad |\operatorname{Im}\delta_e|\le h_0,
\quad\operatorname{Re}\delta_e\in\mathbb R,\quad |Y_f|=L_f.
\end{aligned}\tag{10}
\]

Here C on the left is the actual complex face value. Thus A and C
have precisely the stated phase difference regardless of other
face phases. No phase is assigned to a protected zero.

To verify (10) against the actual source, put u=-4sin^2(pi delta).
At even N=2m the central formula is

\[
\begin{gathered}
s_m^2(x+y)D_bD_c+s_ms_{m-1}xy(D_bE_c+E_bD_c),\\
D_b=R_{m-1}(b;u),\qquad E_b=(a_{m-1}+u)R_{m-2}(b;u).
\end{gathered}
\]

At odd N=2m+1 it is

\[
G_bG_c+u s_ms_{m+1}xyD_bD_c,\qquad
G_b=R_m(b;u),\quad D_b=R_{m-1}(b;u).\tag{11}
\]

The skipped-central odd term is retained. Every central summand has
a cofactor on the actual AC side, at index J or J-1. On that side
the actual angular theorem gives C N^K exp(-gamma N)R_j(positive;0),
uniformly on the entire real fold and its fixed thin strip. The
J-1 case includes the theorem's omitted-node extra-factor/division
argument and its polynomial cost; no logarithmic angular prefactor
is being claimed. On the other side apply the exact coefficient
interpolation/Bernstein bound.

The remaining central factors are bounded on that strip. At positive
radii use, at even levels,
D_b(0)>=s_(m-1)^2(x+y)R_(m-2)(b;0) and (x+y)^2>=2xy;
at odd levels use
G_b(0)>=s_m^2(x+y)D_b(0) and
G_b(0)G_c(0)>=2s_m^4 xyD_b(0)D_c(0).
These compare every central term to the actual positive endpoint
kernel without division by a small diagonal or central zero.
This proves (10); the other star ports use (7).
Shrinking the strip later preserves all these fixed constants.

## 4. Total-degree tails and fixed choices of radii

Choose delta_j>0 such that

\[
0<\nu-2\delta_j<\nu+2\delta_j<\frac12,\qquad
l=\lceil N(\nu-\delta_j)\rceil,\quad r=\lfloor N(\nu+\delta_j)\rfloor.
\]

For sufficiently large N, 0<l<=r<r+1<=M. Differentiability in (2)
gives fixed t_-<0<t_+, as small as desired, and beta>0 with

\[
\begin{aligned}
F(t_-)-(\nu-\delta_j)t_-&\le F(0)-\beta,\\
F(t_+)-(\nu+\delta_j)t_+&\le F(0)-\beta.
\end{aligned}\tag{12}
\]

Choose them also within (-T_0,T_0), and so small that

\[
F(t)-vt\le F(0)+\gamma/4,
\]

for t between 0 and either chosen radius, and
v in {nu-delta_j,nu+delta_j}. Continuity gives this extra condition.
The integer rounding of l/N and (r+1)/N costs only O(1) in logarithms.

Write P_N^delta=sum_j p_j^delta(Y)A^j. Formula (3) gives the exact
total-degree split j<l, l<=j<=r, and j>r, all with j<=M. Positivity
of P_N^0, (6),(8), and the two Chernoff radii show that the exterior
parts have bound

\[
\left|\sum_{\substack{0\le j\le M\\j<l\ \mathrm{or}\ j>r}}
(-1)^jb_j(\sigma)C^jp_j^{\boldsymbol\delta}(Y)\right|
\le\operatorname{poly}(N)e^{N(F(0)-\beta+\omega+o(1))}.\tag{13}
\]

For example, the lower positive tail is bounded by
exp(-(l-1)t_-)P_N^+(L_C exp(t_-)); the upper one by
exp(-(r+1)t_+)P_N^+(L_C exp(t_+)). No individual neighbor A allocation
is restricted. Endpoint or zero spectral rows are controlled by (6),
not by solving a divided recurrence there.

## 5. An exact finite analytic antidifference on the interior rows

Put h=1/N. For a complex log-radius zeta set

\[
\begin{aligned}
w_j(\zeta)&=(-1)^jb_j(\sigma)e^{-j\zeta},\\
a_N(t,\zeta,\sigma)&=-e^{-\zeta}
\frac{4\sin^2(\pi(t+h))}{\sigma-2\cos(2\pi(t+3h/2))}.
\end{aligned}\tag{14}
\]

Then w_(j+1)=a_N(j/N)w_j EXACTLY by (5). On a fixed complex tube
about the strict row interval and a fixed rectangle
|Re zeta|<T_1, |Im zeta|<2phi_0 with T_1>T_0, the denominator stays
away from zero for sigma in a sufficiently small complex disk about 2.
At sigma=2, a_N converges uniformly there to -exp(-zeta). After
shrinking these fixed neighborhoods if necessary, a_N-1 has a
uniformly bounded analytic inverse. The original b_j can still be
zero; it is never divided out. All divisions in this construction are
confined to the stated bulk interval, where both the denominator in
(14) and a_N-1 are uniformly nonzero.

Here is the finite construction, including its error. Put

\[
\begin{aligned}
K_N&=(a_N-1)^{-1},\\
(\mathcal F_hH)(t)&=-\frac{a_N(t)}{a_N(t)-1}\,[H(t+h)-H(t)],\\
H_N&=\sum_{q=0}^{m_N-1}\mathcal F_h^qK_N.
\end{aligned}\tag{15}
\]

Let rho be the row-tube radius, K a uniform bound on
|a_N/(a_N-1)|, and K_0 a uniform bound on |K_N| on the larger tube
and fixed parameter rectangle. Choose

\[
m_N=\left\lfloor\frac{\rho N}{8(K+1)}\right\rfloor\ge1.
\]

Use m_N nested tubes from radius rho to rho/2. Cauchy's derivative
bound makes each forward difference cost at most 2h/s, with
s=rho/(2m_N), so each F_h costs at most
4Khm_N/rho<=1/2. All literal shifts stay in the preceding tube.
The finite geometric identity now gives

\[
\begin{aligned}
a_N(t)H_N(t+h)-H_N(t)&=1-e_N(t),\\
e_N(t)&=(a_N(t)-1)\mathcal F_h^{m_N}K_N(t),\\
|H_N|&\le2K_0,\qquad |e_N|\le Ce^{-cN}.
\end{aligned}\tag{16}
\]

All functions are analytic in zeta and sigma on the fixed parameter
rectangle; the bounds are uniform. This constructs an exact finite
antidifference, not an asymptotic solution for a discrete coefficient.

Consequently the ORIGINAL window kernel satisfies EXACTLY

\[
\sum_{j=l}^rw_j
=w_{r+1}H_N((r+1)/N)-w_lH_N(l/N)
+\sum_{j=l}^re_N(j/N)w_j.\tag{17}
\]

BOTH endpoint terms remain. Each w_j retains the full b_j unused-row
product, including every common sampled zero.

## 6. Exact A contour and both radial side currents

The actual window coefficient is

\[
\frac1{2\pi}\int_{-\pi}^{\pi}
P_N^{\boldsymbol\delta}(Ce^{i\phi},Y)
\sum_{j=l}^rw_j(i\phi)\,d\phi.\tag{18}
\]

This is a literal coefficient contour, not a finite grid. No alias
or bound on the total degree of P_N relative to N is needed.

For |phi|>=phi_0, (10) and (6) give rate at most
F(0)+omega-gamma. For |phi|<=phi_0, insert (17).
The residual contributes at most

\[
\operatorname{poly}(N)e^{N(F(0)+\omega-c+o(1))}.\tag{19}
\]

by (6),(8). No analytic interpolation of p_j has been used.

Consider separately the boundary terms j=l and j=r+1. Apart from
the actual scalar (-1)^j b_j(sigma), their integrand is

\[
W_j(\zeta)=P_N^{\boldsymbol\delta}(Ce^\zeta,Y)
e^{-j\zeta}H_N(j/N;\zeta,\sigma).
\]

It is holomorphic on the small rectangle of (14)-(16). Deform the
segment zeta=i[-phi_0,phi_0] to Re zeta=t_- for j=l, and to
Re zeta=t_+ for j=r+1. The exact contour identity retains BOTH joining
segments, at Im zeta=+phi_0 and Im zeta=-phi_0.

On the shifted vertical segment, bounded H_N, (6),(8),(12) give rate
at most F(0)+omega-beta. On either joining segment, the actual
A/C phase difference is exactly +/-phi_0, so (10) applies.
The small-radius choice after (12) bounds the rate there by

\[
F(0)+\omega-3\gamma/4.\tag{20}
\]

Thus BOTH endpoint terms have a strict rate improvement, and both
original radial currents have been controlled, not discarded.
All bounds are uniform in the other face phases.

## 7. Closing the fixed spectral neighborhoods

The row interval, angular threshold, radii and positive losses
beta,gamma,c were fixed using the endpoint profile before the final
spectral neighborhoods were chosen. Take epsilon_* within the initial
cap disk, and h_* within the initial CROSS strip, such that

\[
\operatorname{arcosh}(1+\varepsilon_*/2)+2\pi k h_*
<\frac14\min\{\beta,\gamma/2,c\}.\tag{21}
\]

All these numbers are fixed before N tends to infinity. Equations
(13),(18)-(20) give a uniform upper rate strictly below F(0).
Since log P_N^+(L_C)=NF(0)+o(N), reducing the gap once more proves
the actual finite comparison (4) at all sufficiently large levels.

This includes arbitrary real parts of every CROSS fold parameter.
No cap moment sequence at a varied spectrum, unknown degree
interpolation, or finite-order adiabatic extrapolation has entered.
The finite high-order construction (15)-(17) supplies the stated
exponential residual, and all source cutoff endpoints remain.

## 8. Exterior attachment and precise remaining scope

As the whole A-star was included, the unchanged exterior G_N has no
A incidence. For the remaining original target monomial Y^t, (4)
and Cauchy give

\[
\big|[Y^{\mathbf t}]B_N(Y;\sigma,\boldsymbol\delta)G_N(Y)\big|
\le e^{-\eta N}P_N^+(L_C)
\frac{\sup_{|Y_f|=L_f}|G_N(Y)|}{\prod_fL_f^{t_f}}.\tag{22}
\]

Here ordinary t_f=d and protected exponents zero are unchanged.
Boundary variables may be shared arbitrarily. All raw source scalar
signs are fixed unit factors; there is no new N normalization.

This is a genuine spectral-neighborhood RELATIVE star improvement.
Its displayed weighted star/exterior envelope is not generally known
to be at most exp(N Phi_D). The hypothesis that every other A-incident
port is CROSS also remains explicit. Consequently no universal cap
elimination, full source gap, or volume theorem is inferred.

## 9. A shorter fixed-spectrum proof using only finite positive moments

At the fixed spectra cap +2 and all neighbors -2, there is a separate
proof of the relative star gap that avoids analytic antidifferencing.
It uses the [exact positive cap-moment law](research_flat_cap_positive_moment_form.md),
not its disproved squared-norm strengthening. Put

\[
P_N^0(A,Y)=\sum_{j\ge0}p_{N,j}(Y)A^j,\qquad
R_N(x;Y)=\sum_{j=0}^Mp_{N,j}(Y)(-Cx)^j.
\]

There is a positive random variable \(X_N\) with

\[
\mathbb E X_N^j=U_j/U_0\quad(0\le j\le d),\qquad
B_N(Y;2,0)=U_0\mathbb E R_N(X_N;Y).\tag{23}
\]

Its support is unbounded. Only the displayed finite moments are used.
The original full sine products give \(B_d=N^2\) and
\(\prod_{r=0}^d\gamma_r=4\), hence \(U_d=N^2\) at both parities. Thus

\[
m_d:=\mathbb E X_N^d=N^2\sin^2\!\frac{\pi}{2N}
\le\frac{\pi^2}{4},\qquad U_0\le CN^2.\tag{24}
\]

Fix a small \(\delta_0>0\). The actual AC-cofactor angular theorem at
phase difference \(\pi\) gives constants \(C_0,K,\gamma>0\) with

\[
|P_N^0(-Cx,Y)|\le C_0N^Ke^{-\gamma N}P_N^+(L_Cx),
\quad 1-\delta_0\le x\le1+\delta_0,\quad |Y_f|=L_f.
\]

The central formulas (11) retain every term at both parities; the
ordinary AC variables are supported in one actual triangle. This
bound is therefore uniform in every other face phase.

Choose \(0<\delta<\delta_0\) and \(R>1+\delta\). Split the expectation
in (23) into the lower, middle and upper ranges separated by
\(1-\delta\) and \(1+\delta\). In the lower range, positivity of the
endpoint product gives
\( |R_N(x;Y)|\le P_N^+(L_C(1-\delta))\).
In the upper range the TRUE total cap cutoff gives

\[
|R_N(x;Y)|\le x^M P_N^+(L_C),\qquad
\mathbb E\!\left[X_N^M\mathbf1_{X_N\ge1+\delta}\right]
\le(1+\delta)^{-(d-M)}m_d.
\]

On the bounded middle range, use the finite identity
\(R_N(x;Y)=P_N^0(-Cx,Y)-\sum_{j>M}p_{N,j}(Y)(-Cx)^j\).
Its first term has the angular gap. The second has the finite Chernoff
bound \((x/R)^{M+1}P_N^+(L_CR)\). The full product is evaluated only
on this bounded interval: neither its higher powers nor its square
is integrated against the moment law. Combining the three ranges gives

\[
\begin{aligned}
\sup_{|Y_f|=L_f}|B_N(Y;2,0)|\le U_0\bigg[&P_N^+(L_C(1-\delta))\\
&+m_d(1+\delta)^{-(d-M)}P_N^+(L_C)\\
&+C_0N^Ke^{-\gamma N}P_N^+(L_C(1+\delta))\\
&+\left(\frac{1+\delta}{R}\right)^{M+1}P_N^+(L_CR)\bigg].
\end{aligned}\tag{25}
\]

This is an explicit finite inequality for the actual positive star
values; no individual neighbor A allocation is made.
Let \(F_0=F(0)\). Choose \(t>0\) with \(F(t)-F_0<t/2\), set \(R=e^t\),
and then take \(\delta>0\) small enough that all four deficits are positive:

\[
\begin{aligned}
\eta_1&=F_0-F(\log(1-\delta)),\\
\eta_2&=\tfrac12\log(1+\delta),\\
\eta_3&=\gamma-F(\log(1+\delta))+F_0,\\
\eta_4&=\tfrac12(t-\log(1+\delta))-F(t)+F_0.
\end{aligned}\tag{26}
\]

The first uses \(F'(0)>0\); the fourth uses \(F'(0)<1/2\) with the
radius \(t\) fixed first. Continuity gives the third. At even levels
\(d-M=M+1=N/2\); at odd levels these quantities are \((N+1)/2\) and
\((N-1)/2\). The bounded offsets, (24), and the endpoint weighted limit
therefore turn (25) into a strict exponential gap relative to the
actual \(P_N^+(L_C)\).

This proof does not extend the positive moment sequence to a varying
cap spectrum. Sections 2–7 provide that separate analytic extension.
The fixed-spectrum argument also does not supply a coefficientwise
comparison with the paired endpoint reference: it is the same
weighted, phase-uniform star estimate as the main theorem.

## Inputs and internal reviews

The original cap factors follow from the exact polynomial tail formula
in the [all-demand source proof](research_cap_cross_all_demand_subexponential_contraction.md)
and its [original-demand dictionary](research_two_port_main_cap_original_demand_convolution.md).
The all-strip coefficientwise bound is the
[original cofactor factorization](actual_cross_cofactor_factorization.md),
section 8, equations (22)–(27). The
[global cofactor angular theorem](actual_cross_cofactor_global_angular_gap.md),
sections 1–4, supplies the fixed strip and the polynomial omitted-node
cost. The [mixed CROSS/window note](research_mixed_cross_window_cycle_packing.md),
sections 1–2, also records the exact central comparisons and support.

The finite normal form is the
[analytic switching theorem](research_analytic_switching_suppression.md),
sections 1–3; its forward version is proved explicitly in (15)–(17).
The endpoint action comes from the
[even closed half-block theorem](actual_fejer_half_block_entropy.md),
section 5, and the [odd raw factorization and coefficient theorem](actual_fejer_odd_regularized_full_numerator.md),
sections 1–3. The stationary interpretation uses the
[full-fiber common-weight classification](research_full_fiber_sharp_stationary_classification.md).
The [incidence and assembly note](research_cap_cross_incidence_and_disjoint_assembly.md)
explains why the present whole-star operation is different from attaching
a two-port estimate to an exterior carrying A.

Root and the independent geometry reviewer read the full source and
analytic proof in sections 1–8 and reported PASS. They checked the
exact cap recurrence, original global coefficient majorant, both parity
central factors, all-fold angular input, finite antidifference and nested
tubes, total-degree tails, both window endpoints and both contour joining
currents, and the order of choosing fixed losses and spectral neighborhoods.
The only requested wording clarification names both nonzero bulk
denominators; no mathematical correction was required.

The endpoint moment argument in section 9 separately has full root,
coherent and geometry analytical/source reviews. Its last finite moment,
total cutoff, bounded-only use of the full product and all four deficits
were independently checked. These are internal reviews, not external
peer review. Preservation changes mathematical formatting and working
relative links. No numerical audit or new runtime evidence is needed or
claimed for these analytical arguments.
