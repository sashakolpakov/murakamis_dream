# The original cap/CROSS contraction on a complex two-spectrum neighborhood

31 October 2026. Internally reviewed analytical theorem. Root and geometry
completed full independent analytical/source reviews; this is not external
peer review. Both polynomial spectral parameters, both actual projectors,
and the odd central transition are retained. This is an unpublished
research note, with the scope stated below.

## 1. The original coefficient and the claim

Keep the exact two-port incidence

\[
E=(A,0,C,Z),\qquad F=(0,A,0,C).
\]

with A incident only to these ports and its unchanged target A^d,
d=N−1. Write

\[
\begin{aligned}
\theta&=\pi/N,& c_j&=2\cos((2j+1)\theta),&s_j&=2\sin(j\theta),\\
a_j&=2+c_j,&\gamma_j&=2-c_j,&B_j&=\prod_{r=1}^j s_r^2,\\
M&=\lfloor N/2\rfloor-1,& H&=\lfloor d/2\rfloor,\\
J_n&=[\max(0,n-H),\min(M,n)]\cap\mathbb Z.
\end{aligned}
\]

The cap parameter is sigma, near +2; the E parameter is tau, near
−2. Define the genuine polynomial cap weights

\[
\begin{aligned}
g_j(\sigma)&=\sigma-c_j,\\
b_j(\sigma)&=B_j\prod_{r=j+1}^{d}g_r(\sigma),\\
\chi_N(\sigma)&=\prod_{r=0}^{d}g_r(\sigma).
\end{aligned}
\]

Let C_(j,h)(tau) be (−1)^d times the coefficient of
A^j C^h Z^(d−j−h) in the full original H_(V_N(tau))(A,0,C,Z).
Thus C_(j,h)(−2)=C_(j,h) is the old nonnegative raw endpoint
coefficient. Apply the actual CROSS cutoff h<=H and RIGHT cutoff
j<=M only in the final sum

\[
T_n(\sigma,\tau)=\sum_{j\in J_n}(-1)^j b_j(\sigma)C_{j,n-j}(\tau),
\qquad 0\le n\le N-2.\tag{1}
\]

The remaining original degrees are C^n Z^(d−n). The common raw
sign (−1)^d does not affect its modulus and has not been changed.
Let D_n^ref be the same fixed positive comparator in the reviewed
[all-demand theorem](research_cap_cross_all_demand_subexponential_contraction.md): even raw positive endpoint at both ports;
odd actual regularizer V_N(−2)−N^(−2)V_N'(−2) at both reference
ports. The numerator (1) is always RAW.

**Theorem.** There are epsilon_0>0 and omega(epsilon)->0 such that,
for 0<epsilon<=epsilon_0,

\[
\limsup_{N\to\infty}\frac1N\log
\max_{0\le n\le N-2}
\sup_{\substack{|\sigma-2|\le\varepsilon\\|\tau+2|\le\varepsilon}}
\frac{|T_n(\sigma,\tau)|}{D_n^{\mathrm{ref}}}
\le\omega(\varepsilon).\tag{2}
\]

Both disks are complex. Every spectral root is included, and the
level runs through both parities. In particular any two shrinking
radii tending to zero give a uniform subexponential comparison:
fix epsilon first, use eventual inclusion in its polydisk, then
let epsilon decrease to zero in (2).

This is a statement for the exact internal A^d contraction, not
for a larger star or a whole invariant. No polynomial factor or
spectral estimate for arbitrary incidence is asserted.

## 2. Polynomial source identities, including the odd transition

The general-coupon physical identity in sections 2–3 of the durable
[Newton source proof](research_cap_cross_low_demand_newton_contraction.md)
gives BEFORE projection

\[
\begin{aligned}
C_{j,h}(\tau)&=v(\tau)^T\widehat B_j(Z_N)e_{d-j-h},\\
v_r(\tau)&=(-1)^{d+r}B_r\prod_{l=r+1}^{d}(\tau-c_l).
\end{aligned}
\]

For clarity, its literal physical-index identity is

\[
Z(E,F,G)=\phi\bigl(G\mathscr R(F\mathscr R(E))\bigr)
=\alpha_E^T F(Z_N)P_{\mathrm{rev}}\alpha_G.
\]

for arbitrary polynomial coupons, before endpoint specialization.
Choose E=V_N(tau), F=Bhat_j, G=g_n=product_(r<n)(z−c_r), n=j+h.
The actual protected-face monomials are

\[
\begin{aligned}
H_{\widehat B_j}(0,A,0,C)&=A^{d-j}C^j,\\
H_{g_n}(0,C,0,Z)&=(-1)^n B_n C^{d-n}Z^n.
\end{aligned}
\]

The unchanged three face targets therefore give the raw scalar
(−1)^(d+n)B_n C_(j,h)(tau). On the Newton side it equals
(−1)^n B_n alpha_(V_N(tau))^T Bhat_j(Z_N)e_(d−n).
Cancelling B_n, with alpha_(V_N(tau),r)=(−1)^r B_r
product_(l>r)(tau−c_l), proves the displayed v(tau) formula with
exactly its (−1)^d sign. No extra N occurs. This is a general
physical polynomial identity, not endpoint interpolation.

The Newton relations (c_j−Z)Bhat_j=s_(j+1)^2 Bhat_(j+1),
Z_Ne_k=c_ke_k−s_(k+1)^2e_(k+1), and the literal row reflection
c_(d−n)=c_n, s_(d−n+1)=s_n then give for both spectra

\[
\begin{aligned}
g_n t_j(n)+s_n^2t_j(n-1)&=g_jt_j(n)-g_{j+1}t_{j+1}(n),\\
t_j(n)&=(-1)^j b_j(\sigma)C_{j,n-j}(\tau).
\end{aligned}\tag{3}
\]

These are polynomial identities, including when g_j or chi_N
vanishes. For n<=M the original cutoffs are redundant, so

\[
\begin{aligned}
g_nT_n+s_n^2T_{n-1}&=\chi_N(\sigma)C_{0,n}(\tau),&T_{-1}&=0,\\
C_{0,n}(\tau)&=\frac{N^2}{B_n}\prod_{r=0}^{n-1}(c_r-\tau).
\end{aligned}\tag{4}
\]

For n>H set L=n−H. Summing (3) over the actual moving range
J_n=[L,M] and retaining the adjacent-projector difference yields

\[
g_nT_n+s_n^2T_{n-1}
=(g_{L-1}-g_n)t_{L-1}(n)-g_{M+1}t_{M+1}(n).\tag{5}
\]

At even N=2m these currents contain C_(n−m,m)(tau) and
C_(m,n−m)(tau). At odd N=2m+1 they contain
C_(n−m−1,m+1)(tau) and C_(m,n−m)(tau). The first odd current
DOES NOT generally vanish when tau differs from −2.

There is one transition not covered by either n<=M or n>H:
at odd level n=H=m, J_n=J_(n−1)=[0,M]. Summing (3) there gives

\[
g_mT_m+s_m^2T_{m-1}
=\chi_N(\sigma)C_{0,m}(\tau)
+(-1)^M s_m^2 b_M(\sigma)C_{m,0}(\tau).\tag{6}
\]

Equations (4), (5), and (6) cover EVERY transition. No central
zero, lower-current term, or top coefficient is omitted.

## 3. Existing coefficientwise majorants at the fixed original root

Let kappa=arcosh(1+epsilon/2). The literal cap product gives

\[
|b_j(\sigma)|\le U_j e^{N\kappa},\qquad
|\chi_N(\sigma)|\le4e^{N\kappa},\qquad U_j=b_j(2).\tag{7}
\]

uniformly in its complex disk. For j<=M+1, U_j<=C N^2, including
the single current index above the cap cutoff. All divisions used
to prove (7) are by fixed gamma_r>0, never by varying g_r.

For E, use the EXISTING source-proved coefficientwise comparison in
[odd regularization](actual_fejer_odd_regularized_full_numerator.md),
section 4, equations (13)–(15), and its even comparison in section 5.
Denote the positive full reference coefficients by C_(j,h)^ref:
they are C_(j,h) at even level, and Cbar_(j,h) from the fixed-root
regularizer at odd level, including outside the CROSS cutoff.
Then for |tau+2|<=epsilon,

\[
|C_{j,h}(\tau)|\le Q_N(\varepsilon)C_{j,h}^{\mathrm{ref}},\qquad
Q_N(\varepsilon)\le(1+N^2\varepsilon)e^{N\kappa}.\tag{8}
\]

Here is why this comparison is root-safe. Each path has distinct
unused spectral factors. At even level all a_r>0, and the product
of their possible ratios is at most
product_r(1+epsilon/a_r)<=exp(N kappa). At odd level a_m=0 is
the sole central zero. A path retaining it is bounded by epsilon
times the product of its noncentral factors, which is paid by
N^2 epsilon times its positive derivative-reference term. Paths
without it are paid by the raw reference term. The noncentral
product is

\[
\prod_{r\ne m}\left(1+\frac{\varepsilon}{a_r}\right)
=\left[\frac{\sinh(N\kappa/2)}{N\sinh(\kappa/2)}\right]^2
\le e^{(N-1)\kappa}.
\]

This proves (8), and shows explicitly why no vanished a_m is
divided out. The comparison applies coefficientwise to the full
source, hence to either original projected part and both currents.

The same source results give uniform CLOSED coefficient entropy
for C^ref. On CROSS degrees it is the two-triangle maximum; on
the adjacent one-sided seam it is the same continuous full
endpoint entropy. These are actual coefficient upper/lower
theorems, not merely weighted capacities.

Two corner consequences will be used. Let q_L=(0,0,0,1) and
q_R=(1/2,0,1/2,0), in degree order (A,input middle,C,Z).
Their reference entropies are zero. There are nonnegative
e_L(eta),e_R(eta)->0 such that the original coefficients in
eta-neighborhoods of these corners obey the uniform upper rates
e_L(eta), e_R(eta). The precise fixed multiplicative enlargement
of the neighborhoods is immaterial and is included in these
definitions.

## 4. A complete comparator-rate lemma, including the high corner

The reviewed all-demand proof used the rate

\[
\begin{aligned}
J(u)&=f(u-\tfrac12)+\max_{u-1/2\le a\le1/2}
\{3f(a)+f(a-u+\tfrac12)\},\\
f(t)&=-\int_0^t\log\tan(\pi s)\,ds.
\end{aligned}\tag{9}
\]

We need the same actual coefficient estimate beyond its former
middle interval. In fact, uniformly for M<n<=N−2,

\[
\frac1N\log D_n^{\mathrm{ref}}=J(n/d)+o(1).\tag{10}
\]

and n=M has rate J(1/2)+o(1). This includes sequences tending
to n/d=1. Here is the finite-support lower check for that extension.

The existing positive convolution gives the continuous objective

\[
E(a,v;u)=2f(a)+f(v-a)+f(u-v)+f(u-a)-2f(v),
\qquad u-\tfrac12\le a\le v\le\tfrac12.\tag{11}
\]

Its derivative in v in the interior is

\[
\log\frac{\tan(\pi(u-v))\tan^2(\pi v)}{\tan(\pi(v-a))}\ge0.
\]

because u>=1/2, so tan(pi(u−v))>=cot(pi v), while
tan(pi(v−a))<=tan(pi v). Thus its closed maximum is v=1/2
and equals (9). All actual allocations have limiting data in
this compact domain. The closed coefficient upper, polynomial
number of terms, and continuity give a uniform upper for (10),
including its endpoints. A subsequence compactness argument
avoids imposing an interior-optimizer assumption at u=1.

For the LOWER, choose the actual cap index j=M, whose reference
weight is polynomial: V_M=N at even level and
V_M^o=1/[4cos^2(theta/2)] at odd level. At even level use the
exact lower block

\[
4(A+Z)R_M^*(0)R_M^*(C)\le P_{E,\mathrm{CROSS}}.
\]

with its genuine modified path numerators and original scalar
normalization, as in
[the closed half-block theorem](actual_fejer_half_block_entropy.md),
section 5. If one rewrites R_M^* using that theorem's determinant
D_M, its scalar C_front=N/[2sin(pi/N)] must multiply EACH factor;
it has not been removed here. Choose the forced Z unit. The actual first-triangle
A-degree then ranges over

\[
n-M\le k\le M\qquad(N\text{ even}).\tag{12}
\]

The two remaining triangle degrees are exactly M. At odd level
the true positive D_m convolution gives instead

\[
n-m\le k\le M\qquad(N\text{ odd}).\tag{13}
\]

with both triangle degrees m=N/2−1/2. The raw-to-regularized
CROSS comparison is by uniform positive factors. These are the
original integer intervals, not enlarged supports.

After dividing by d, the intervals (12), (13) are within O(1/d)
of [u−1/2,1/2] at both endpoints and are nonempty for every
n<=N−2. Clamp a maximizing a in (9) to the actual interval,
then round to an integer. The total change is O(1/d), even when
the interval is a singleton near n=N−2. The uniform CLOSED
triangle lower theorem and continuity therefore give the matching
lower rate J(u). The forced Z and the true R_M^* scalar have
remained in this lower estimate throughout. This proves (10).

As already proved for (9), J is continuous on [1/2,1], strictly
concave in the interior, with a unique peak u_* in (1/2,3/4).
It is increasing before the peak and decreasing afterwards.
Also, choosing a=u−1/2 gives

\[
J(u)\ge4f(u-\tfrac12)\ge0,\qquad J(1)=0.\tag{14}
\]

These properties and (10) do not depend on either varying spectrum.

## 5. Three row scales and the exact initial block

Fix small eta>0 and require epsilon<=c_0 eta^2, with c_0 a small
absolute constant. Set

\[
k=\lceil\eta N\rceil,\qquad b=\lfloor(\tfrac12-\eta)N\rfloor,
\qquad n_R=\lfloor(1-\eta)N\rfloor,\qquad a=k/N.
\]

For sufficiently large N, k<b<M<n_R<=N−2. Parameters epsilon
and eta remain fixed while N grows. The four relevant regions are:
the short initial block n<=k; the contour range k<=n<=b;
the central low strip b<n<=M; and the projected middle up to n_R.
The high corner n>=n_R is bounded directly.

For n<=k, every E reference coefficient in (1) approaches q_L.
Equations (7), (8), U_j<=CN^2, and the polynomial number of terms
give

\[
|T_n(\sigma,\tau)|\le\exp\{N[2\kappa+e_L(\eta)+o(1)]\}.\tag{15}
\]

uniformly on both disks and that initial range.

Let C_(0,n)^0=C_(0,n)(−2)>0. Its exact product implies, uniformly
through the full low range n<=M at both parities,

\[
\log C_{0,n}^{0}=2Nf(n/N)+O(\log N),\qquad
D_n^{\mathrm{ref}}\ge C_{0,n}^{0}/4,\qquad C_{0,n}^{0}\ge N^{-C}.\tag{16}
\]

For n<=b, no varying a-factor is close to a zero. Writing zeta=tau+2,

\[
\frac{C_{0,n}(\tau)}{C_{0,n}^{0}}=\prod_{r=0}^{n-1}\left(1-\frac{\zeta}{a_r}\right).
\]

The factors have |zeta/a_r|<=1/2. Since
sum_(r<n) a_r^(−1)<=CN/eta for n<=b, their logarithms give the
TWO-SIDED estimate

\[
e^{-CN\varepsilon/\eta}\le
\left|\frac{C_{0,n}(\tau)}{C_{0,n}^{0}}\right|
\le e^{CN\varepsilon/\eta}.\tag{17}
\]

This elementary lower is used only before b. No such nonvanishing
claim is made through the central rows.

## 6. Two exact Gamma products on the root-free contour range

For k<=n<=b both g_n(sigma) and c_n−tau stay uniformly away from
zero by c eta^2. Define

\[
Y_n=\frac{g_n(\sigma)T_n(\sigma,\tau)}{C_{0,n}(\tau)},\qquad
t_r(\sigma,\tau)=\frac{s_r^4}{(c_{r-1}-\tau)(\sigma-c_{r-1})}.
\]

Only n>k is solved in this normalization. The polynomial identity
(4) and its exact C_0 ratio yield

\[
Y_n=\chi_N(\sigma)-t_n(\sigma,\tau)Y_{n-1}.\tag{18}
\]

Put P_(k,n)=product_(r=k+1)^n t_r, A_(k,j)=P_(k,j)^(−1).
The solution retains the original starting source:

\[
Y_n=(-1)^{n-k}P_{k,n}Y_k
+\chi_N(\sigma)(-1)^nP_{k,n}\sum_{j=k+1}^{n}(-1)^jA_{k,j}.\tag{19}
\]

There is no reciprocal chi_N. Choose small complex delta,beta with

\[
\sigma=2\cos(2\pi\delta),\qquad \tau=-2\cos(2\pi\beta),
\qquad |\delta|,|\beta|\le\eta/8.
\]

The choice of signs does not matter because every expression is
even in each parameter. For t_r=(r−1/2)/N in the next display
(this local notation denotes a mesh point, not the recurrence
coefficient), the exact product ratio is

\[
\frac{A_{k,j}(\sigma,\tau)}{A_{k,j}(2,-2)}
=\prod_{r=k+1}^{j}
\frac{\sin(\pi(t_r+\delta))\sin(\pi(t_r-\delta))}{\sin^2(\pi t_r)}
\frac{\cos(\pi(t_r+\beta))\cos(\pi(t_r-\beta))}{\cos^2(\pi t_r)}.
\tag{20}
\]

Let s(t)=sin(pi t)/(pi t) and
L_delta(t)=log s(t+delta)+log s(t−delta)−2log s(t),
with the fixed analytic sinc logarithm. Define m=N/2, not necessarily
an integer. The two exact Gamma multipliers are

\[
\begin{aligned}
G_\delta(z,k)&=
\frac{\Gamma(z+\frac12+N\delta)\Gamma(z+\frac12-N\delta)\Gamma(k+\frac12)^2}
{\Gamma(k+\frac12+N\delta)\Gamma(k+\frac12-N\delta)\Gamma(z+\frac12)^2},\\
H_\beta(z,k)&=
\frac{\Gamma(m-k+\frac12+N\beta)\Gamma(m-k+\frac12-N\beta)\Gamma(m-z+\frac12)^2}
{\Gamma(m-z+\frac12+N\beta)\Gamma(m-z+\frac12-N\beta)\Gamma(m-k+\frac12)^2}.
\end{aligned}\tag{21}
\]

Equation (20) is exactly G_delta(j,k)H_beta(j,k) times the
exponential of the midpoint sum of

\[
L(t)=L_\delta(t)+L_\beta(\tfrac12-t).
\]

Both nearby endpoint zero pairs have therefore been removed from
the Euler–Maclaurin input and placed in EXACT Gamma factors.

Let Acal_N(z) be the explicit Gamma/smooth-product interpolant in
sections 2–3 of the durable
[endpoint contour proof](research_cap_cross_full_low_demand_subexponential_contraction.md),
with m=N/2 and the literal half-integer extension in
[the odd theorem](research_cap_cross_odd_low_demand_subexponential_extension.md).
For an analytic L, the midpoint expression used here is explicitly

\[
\mathcal E_{1/2,N}(L;u)=N\int_0^u L(t)\,dt
+\sum_{l=1}^{p-1}\frac{B_{2l}(1/2)}{(2l)!N^{2l-1}}
\bigl[L^{(2l-1)}(u)-L^{(2l-1)}(0)\bigr].
\]

with the analytic primitive and Bernoulli polynomials, radius
rho=1/5, and optimal truncation p=floor(pi rho N). Define

\[
I(z)=\frac{\mathcal A_N(z)}{\mathcal A_N(k)}G_\delta(z,k)H_\beta(z,k)
\exp\{\mathcal E_{1/2,N}(L;z/N)-\mathcal E_{1/2,N}(L;a)\}.
\tag{22}
\]

For each fixed contour height Y this is analytic and nonzero on

\[
k-\tfrac14\le\Re z\le b+\tfrac14,\qquad |\Im z|\le NY.
\]

Every shifted Gamma argument has real part >=eta N/2 for N large,
uniformly in both spectral disks. The sinc logarithms in L have
a common fixed-width zero-free neighborhood of radius rho around
the scaled rectangles, independently of eta sufficiently small.
Thus the same Bernoulli remainder estimate as in the cap-only
proof gives

\[
I(j)=A_{k,j}e^{e_{N,j}},\qquad |e_{N,j}|\le e^{-6N/5},\qquad k\le j\le b.\tag{23}
\]

The constants may depend on each fixed Y; they are uniform in
both spectral parameters. Adding the second smooth logarithm only
changes a finite prefactor, absorbed by 2pi/5>6/5.

## 7. The calibrated action and the contour estimate

The leading logarithm of G_delta is the difference of

\[
N\bigl[(u+\delta)\operatorname{Log}(u+\delta)+(u-\delta)\operatorname{Log}(u-\delta)-2u\operatorname{Log}u\bigr]
\]

between u=z/N and a. The leading logarithm of H_beta is the
NEGATIVE difference of the same expression with u replaced by
1/2−u and delta by beta. The exact normalization makes both
differences vanish at a. Stirling errors are O_(eta,Y)(log N),
uniformly in both disks; all arguments remain in the right
half-plane. The smooth midpoint terms have the corresponding
integrals with O_Y(N^(−1)) corrections.

Differentiating these leading expressions and adding the smooth
terms gives exactly

\[
\Psi'(u)=\operatorname{Log}\left(1+\frac{\sigma-2}{4\sin^2(\pi u)}\right)
+\operatorname{Log}\left(1-\frac{\tau+2}{4\cos^2(\pi u)}\right),
\qquad\Psi(a)=0.\tag{24}
\]

The small logarithms are the branches zero at the base spectra.
Exponentiating verifies the sine/cosine identities in (20), and
analytic continuation in the small delta,beta disks fixes the
branches. Normalization at a fixes the integration constant.
There is no unrecorded branch-dependent scalar.

For eta/2<=x<=1/2−eta/2, use

\[
\begin{aligned}
|\sin(\pi(x+iy))|^2&=\sin^2(\pi x)+\sinh^2(\pi y),\\
|\cos(\pi(x+iy))|^2&=\cos^2(\pi x)+\sinh^2(\pi y).
\end{aligned}
\]

Integrating first horizontally from a to x and then vertically,
the elementary integrals of 1/(x^2+y^2) and
1/((1/2−x)^2+y^2) prove

\[
|\Psi(x+iy)|\le C\varepsilon/\eta=:B.\tag{25}
\]

for ALL heights y. This bound is independent of the fixed Y used
in the interpolation. It applies on the full enlarged rectangle
for sufficiently large N.

The calibrated growth formula is consequently

\[
\begin{aligned}
\log|I(z)|&=N\Re[2f(z/N)-2f(a)+\Psi(z/N)]+O_{\eta,Y}(\log N),\\
\log|P_{k,n}|&=-2N[f(n/N)-f(a)]-N\Re\Psi(n/N)+O_\eta(\log N).
\end{aligned}\tag{26}
\]

Apply the exact alternating residue argument to (22). Enclose
the integers k,...,n by real sides k−1/4,n+1/4 and
imaginary sides ±NY, integrate pi I(z)csc(pi z), then subtract
the exact first term I(k)=1. After multiplication by P_(k,n),
the leading exponent is

\[
N[h(x,y)-2f(n/N)+2B],\qquad h(x,y)=\Re[2f(x+iy)]-\pi|y|.\tag{27}
\]

The endpoint estimates give h(x,y)<=2f(x), and on the
horizontal sides

\[
|h(x,Y)|\le\varepsilon_Y=\frac{2e^{-2\pi Y}}{\pi(1-e^{-4\pi Y})}\longrightarrow0.
\]

The left side costs
at most 2Nf(a)+2NB; the right side costs 2NB+O_eta(1); the
horizontal sides cost N(epsilon_Y+2B). Contour lengths and all
Gamma corrections are only polynomial in N for fixed eta,Y.

The error (23) remains negligible AFTER propagation and forcing:

\[
|\chi_NP_{k,n}|\sum_{j=k}^{n}|I(j)-A_{k,j}|
\le\exp\{N[2\max f-6/5+2B+\kappa]+O_\eta(\log N)\}.
\tag{28}
\]

Choose eta_0,c_0 small so that 2B+kappa<1/10. Since 2max f<1,
this is exponentially small. The parameter bounds in (17),
needed to convert back to the fixed comparator, add at most
C epsilon/eta to a rate; the same smallness choice leaves a
strict error margin after that conversion as well.

The initial value in (19), by (15), (17), and bounded g_k,
has rate at most 2kappa+e_L(eta)+C epsilon/eta. Its homogeneous
propagator in (26) costs at most 2f(a)+B. The forcing term is
bounded by the contour estimate just described. Fix epsilon,eta,Y,
let N grow, and only then let Y grow. Equations (17), (19),
and (26)–(28) prove the STRONG core estimate

\[
\begin{aligned}
\limsup_N\frac1N\log\max_{k\le n\le b}\sup_{\mathrm{disks}}
\frac{|T_n(\sigma,\tau)|}{C_{0,n}^{0}}&\le\Omega_{\mathrm{core}},\\
\Omega_{\mathrm{core}}&=2\kappa+e_L(\eta)+2f(\eta)+C\varepsilon/\eta.
\end{aligned}\tag{29}
\]

The stronger denominator C_(0,n)^0 is retained deliberately:
using only D_n^ref here would lose the small absolute boundary
rate needed for the next strip. No normalization is continued
past b.

## 8. Raw propagation across the central low strip

For b<n<=M use the polynomial recurrence (4) itself. The factor
g_n(sigma) stays uniformly close to 4. The old low ratio
s_n^2/gamma_n is at most one, and replacing gamma_n by g_n changes
its modulus by at most exp(C epsilon). Hence every raw forward
propagator across this strip costs at most exp(CN epsilon).
There is no division by c_(n−1)−tau or C_(0,n)(tau), which may
vanish on these rows.

For this step use the EXACT PREFIX PRODUCT in (4), not a replacement
of the raw C_0 coefficient by an unspecified reference coefficient.
For n<=M every a_r in that prefix is positive; at odd level the
central a_m=0 is outside it. Consequently

\[
|C_{0,n}(\tau)|\le C_{0,n}^{0}\prod_{r=0}^{n-1}\left(1+\frac{\varepsilon}{a_r}\right)
\le e^{N\kappa}C_{0,n}^{0}.\tag{29a}
\]

The last inequality uses the full positive product at even level,
and the noncentral product displayed in section 3 at odd level.
Thus it compares to the RAW C_(0,n)^0 exactly, with no need to
identify it with the odd regularized coefficient.

For b<=n<=M, equation (16) and f(1/2−v)=f(v) imply
log C_(0,n)^0<=2N f(eta)+o(N). Thus the forcing in (4) has
rate at most 2kappa+2f(eta). At the starting row b, the stronger
estimate (29) has absolute rate at most Omega_core+2f(eta).
Summing the O(N) raw recurrence terms yields

\[
|T_n(\sigma,\tau)|
\le\exp\{N[2\kappa+e_L(\eta)+4f(\eta)+C\varepsilon/\eta+o(1)]\},
\qquad b<n\le M.
\]

The fixed comparator has D_n^ref>=C_(0,n)^0/4>=N^(−C).
Combining this strip with (15), (16), and (29) gives the full-low
comparison

\[
\begin{aligned}
\limsup_N\frac1N\log\max_{n\le M}\sup_{\mathrm{disks}}
\frac{|T_n|}{D_n^{\mathrm{ref}}}&\le\Omega_{\mathrm{low}},\\
\Omega_{\mathrm{low}}&=2\kappa+e_L(\eta)+4f(\eta)+C\varepsilon/\eta.
\end{aligned}\tag{30}
\]

This is precisely where a raw recurrence is necessary: the nearby
tau roots in the central rows have NOT been divided out.

## 9. The high corner is bounded directly

For n>=n_R, the original range J_n forces BOTH j/d and
(n−j)/d to lie within O(eta)+O(1/N) of 1/2, while (d−n)/d
is O(eta). Thus every E reference degree approaches q_R.
Equations (7), (8), the polynomial bound for U_j, and the
definition of e_R give

\[
\max_{n\ge n_R}\sup_{\mathrm{disks}}|T_n|\le\exp\{N[2\kappa+e_R(\eta)+o(1)]\}.\tag{31}
\]

This is an absolute coefficient bound ONLY in this shrinking
corner. It does not discard cancellation in an interior region.
By the genuine comparator lower (10) and J>=0, D_n^ref>=exp(−o(N))
uniformly here. Consequently

\[
\limsup_N\frac1N\log\max_{n\ge n_R}\sup_{\mathrm{disks}}\frac{|T_n|}{D_n^{\mathrm{ref}}}\le2\kappa+e_R(\eta).\tag{32}
\]

No high-demand monotonicity for the varying E coefficients is
assumed; it would generally be unavailable.

## 10. Both projected currents on the remaining middle

For M<n<n_R use (5), except for the odd transition (6). The cap
current index is M+1, so its reference E coefficient tends to
the CROSS data with A-load 1/2. Its closed reference rate is
J(n/d), exactly as in the endpoint all-demand proof.

The lower current has h=H+1 at BOTH parities. Its normalized
data approach the original one-sided seam

\[
(q_x,q_b,q_c,q_y)=(t,0,\tfrac12,\tfrac12-t),\qquad t=n/d-\tfrac12.
\]

The full reference closed entropy there is 2f(t), and
2f(t)<=J(n/d) by (14). At odd level this uses the actual positive
derivative-reference coefficient for a path whose raw central
zero no longer vanishes; it does not reuse the former odd zero
simplification. Equations (7), (8) thus bound BOTH currents by

\[
\exp\{N[J(n/d)+2\kappa+o(1)]\}.\tag{33}
\]

At the odd transition n=m, the extra coefficient C_(0,m)(tau)
in (6) has reference corner rate zero, while chi_N has rate
at most kappa. Its total rate is at most 2kappa; the other
transition current has rate J(1/2)+2kappa. Thus (33) also
bounds the complete transition forcing. No missing odd index
is hidden in the generic moving-range formula.

On the interval M<=n<=n_R, the fixed s_n^2 and gamma_n have
lower bounds c eta^2. The endpoint raw forward and backward
products are bounded by a constant depending on eta: each
logarithmic step is O(1/(N eta)), so a product of at most N
steps has logarithm O(1/eta), not O(N). Perturbing gamma_n to
g_n(sigma) changes a logarithmic modulus by at most
C epsilon/eta^2 per step. Therefore EVERY raw propagator
over this interval is bounded by

\[
C_\eta\exp(CN\varepsilon/\eta^2).\tag{34}
\]

in either direction. Forcing denominators g_n or s_n^2 cost
only fixed eta-dependent constants. No tau factor is divided
out during this projected propagation.

The comparator J increases to its unique peak and decreases
after it. For eta small, n_R/d lies to the right of that peak.
Propagate from M up to the peak using (30), and backward from
n_R down to the peak using (32). Each encountered boundary or
forcing term has comparator rate no greater than the target
J in the chosen direction. There are O(N) such terms.
Equations (10), (33), and (34) prove the remaining ratio bound
with exponent at most

\[
\max\{\Omega_{\mathrm{low}},2\kappa+e_R(\eta)\}+C\varepsilon/\eta^2.
\]

For example all demands are bounded at rate

\[
\Omega(\varepsilon,\eta)=2\kappa+e_L(\eta)+e_R(\eta)+4f(\eta)+C\varepsilon/\eta^2.\tag{35}
\]

Integer rounding near the peak, b, or n_R costs o(1) by the
closed continuity already used in (10) and (16).

Choose eta=epsilon^(1/4) for sufficiently small epsilon. Then
epsilon<=c_0 eta^2, and every term of (35) tends to zero:

\[
\omega(\varepsilon)=2\operatorname{arcosh}(1+\varepsilon/2)
+e_L(\varepsilon^{1/4})+e_R(\varepsilon^{1/4})
+4f(\varepsilon^{1/4})+C\sqrt\varepsilon.\tag{36}
\]

This proves (2). A monotone upper envelope may be used if desired.

## Scope and review status

The proof uses the original general-coupon polynomial contiguity,
the already proved coefficientwise tau-neighborhood majorant,
two exact Gamma products on a root-free interior interval, raw
propagation through the central roots, BOTH original projected
currents, and a genuine high-corner coefficient bound. The actual
odd central transition (6) is explicit. All fixed spectral zeros
and Hermite data are retained; no quantum root is varied.

Root and geometry completed full independent analytical/source reviews
of this standalone proof. They checked the arbitrary-coupon sign and
normalization; both projected currents and the odd transition; both
exact Gamma products, their calibrated primitive and amplified
interpolation error; the strong raw-C0 core and central-prefix bound;
the actual singleton-compatible comparator lower supports; and both
propagation directions and order of limits. No numerical audit is
needed or claimed for this analytical continuation.

No whole-source, larger-star, filled-period, or general volume assertion
is made. The private cap-only derivation is historical background,
not an additional proof dependency of this standalone theorem.
