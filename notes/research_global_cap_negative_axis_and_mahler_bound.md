# The original one-cap coefficient reduces to two negative-axis suprema

31 October 2026. **exact-source and analytic reduction.**
Unpublished. The original
diagram, mark, and every ordinary degree target remain fixed. All noncap
coupons are at their actual CROSS endpoint sigma=-2; the cap is at +2.
No spectral-neighborhood, arbitrary-spectator, or unconditional absolute volume estimate
is asserted. The final two polynomial suprema are the remaining problem.

## 1. Extract the original exterior first

Use a simple matched source with protected MAIN faces u,v, cap
F=(u,A,v,C), and R-1 other original ports. At level N put
d=N-1 and M=floor(N/2)-1. Remove the fixed common raw unit signs from
each CROSS coupon. Define the genuine binary residual polynomial

\[
\begin{aligned}
P_N(A,C)&=\left[\prod_{\substack{f\ \mathrm{ordinary}\\f\ne A,C}}L_f^d\right]
 \prod_{e\ne F}P_{e,\mathrm{CROSS}}(-2;L),\\
P_N(A,C)&=\sum_{j=0}^{d}p_{N,j}A^jC^{d-j}.
\end{aligned}\tag{1}
\]

Protected variables are zero BEFORE this extraction. Every remaining
ordinary variable is extracted to its original d target. Homogeneity
gives degree d exactly: (R-1)d-(R-2)d=d. At both parities the actual
endpoint CROSS polynomials have nonnegative coefficients, so \(p_{N,j}\ge0\).
This is the entire exterior, not only the ports adjacent to A.

Set theta=pi/N and

\[
s_j=2\sin(j\theta),\qquad c_j=2\cos((2j+1)\theta),\qquad
U_j=\left(\prod_{r=1}^{j}s_r^2\right)\prod_{r=j+1}^{d}(2-c_r).
\]

The actual protected cap at +2 has all-index polynomial
sum_(j=0)^d (-1)^j U_j A^(d-j)C^j; its original RIGHT piece has
exactly j<=M. Thus the original cap/CROSS sector coefficient, up to
its fixed unit scalar, is

\[
S_N=\sum_{j=0}^{M}(-1)^jU_jp_{N,j}.\tag{2}
\]

Both original A^d and C^d demands have been imposed in (2). No sign
has been assigned independently to a face occurrence.

## 2. Complete the finite cap sum, with a strictly smaller omitted tail

Let R(s) be the original residual complete-triangle capacity with
A load s, C load 1-s, all other ordinary loads one, and the two original
protected loads zero. It is upper semicontinuous on its compact feasible
interval, with value minus infinity when the fiber is empty. The same
complete coefficient entropy gives

\[
\Phi_D=\max_{1/2\le s\le1}\bigl[R(s)+2f(s-\tfrac12)\bigr].\tag{3}
\]

There is a strict constant gamma_D>0, depending only on the fixed
diagram and mark, such that

\[
\max_{1/2\le s\le1}R(s)\le\Phi_D-\gamma_D.\tag{4}
\]

Indeed, if 1/2<s<1 and R(s) is finite, the added cap entropy in (3)
is strictly positive. At s=1/2 or s=1 it vanishes, but the cap's
complete half-triangle is a pure vertex. The original complete
optimizer is unique and positive on every ordinary incidence. Neither
endpoint can attain its value. Compactness and upper semicontinuity
now give (4). This uses the original complete-flow theorem, not any
full signed-source volume conclusion.

The proved uniform CLOSED local CROSS coefficient upper, followed by
the actual finite shared-array sum, implies

\[
\limsup_{N\to\infty}\frac1N\log p_{N,j_N}\le R(s)
\qquad\text{whenever }j_N/d\longrightarrow s.\tag{5}
\]

The number of local-degree arrays is polynomial because the diagram
is fixed. Their limits satisfy exactly the residual targets defining
R(s). This argument needs only the upper coefficient theorem; no
rounding or lower estimate is needed. It includes zero coefficients.

For all 0<=j<=d,

\[
\begin{aligned}
\frac{U_{j+1}}{U_j}&=\frac{\sin^2((j+1)\theta)}{\sin^2((j+3/2)\theta)}
 \quad(0\le j<d),\\
U_0&=\csc^2(\theta/2)\le N^2,\qquad U_d=N^2,\qquad 0<U_j\le N^2.
\end{aligned}\tag{6}
\]

The ratio crosses one only once, from below to above, so the maximum
is at an endpoint. Consequently the omitted actual tail satisfies

\[
|T_N|:=\left|\sum_{j=M+1}^{d}(-1)^jU_jp_{N,j}\right|
 \le e^{N(\Phi_D-\gamma_D/2)}.\tag{7}
\]

for all sufficiently large N. At odd N=2m+1, its smallest j=m gives
j/d=1/2 exactly; at even N=2m it gives m/(2m-1)>1/2. Thus no
parity seam is lost in the compact upper argument.

## 3. Exact positive moment reduction of the completed sum

The original positive cap moment law supplies X_N>0 with

\[
\mathbb E X_N^j=\frac{U_j}{U_0}\quad(0\le j\le d),\qquad
m_d:=\mathbb E X_N^d=N^2\sin^2\frac{\pi}{2N}\le\frac{\pi^2}{4}.\tag{8}
\]

Only these finite moments are used. In particular its unbounded
support is retained; no integration of degree greater than d occurs.
The completed finite sum is exactly

\[
S_N+T_N=U_0\mathbb E P_N(-X_N,1).\tag{9}
\]

Define two actual negative-axis suprema

\[
B_N^- =\sup_{0\le t\le1}|P_N(-t,1)|,\qquad
B_N^+ =\sup_{0\le t\le1}|P_N(-1,t)|.\tag{10}
\]

At t=0 these use the actual polynomial endpoint values. For X>=1,
homogeneity gives P_N(-X,1)=X^d P_N(-1,1/X). Split the expectation
at X=1 and use (8). The following FINITE inequality is therefore exact:

\[
|S_N|\le U_0\bigl[B_N^-+m_dB_N^+\bigr]+|T_N|.\tag{11}
\]

In particular

\[
\limsup_{N\to\infty}\frac1N\log|S_N|
\le\max\left\{\limsup_{N\to\infty}\frac1N\log\max(B_N^-,B_N^+),
\Phi_D-\frac{\gamma_D}{2}\right\}.\tag{12}
\]

The weak bound B_N^pm<=exp[N(Phi_D+o(1))] would prove the weak
absolute cap estimate at these fixed spectra. A strict bound for both
suprema would prove strict cap suppression. The exterior cannot be
replaced by its independent positive torus majorant in this reduction:
the coefficient extraction in (1) has already retained all its phases
and all original demands.

## 4. Genuine odd-level real stability

At odd N=2m+1 the actual sigma=-2 CROSS coupon is exactly

\[
N^2D_m(x,b,y)D_m(x,c,y),\qquad
D_m(x,b,y)=\det\left[bI+\frac{x}{2}H_-+\frac{y}{2}H_+\right].\tag{13}
\]

with the original positive-definite Hermitian H_-,H_+. If x,b,y
all have positive imaginary parts, the matrix's imaginary part is
positive definite. Its determinant is nonzero. Thus each factor is
real stable. Identifying shared face variables, multiplying, taking
the indicated derivatives for the ordinary coefficient extractions,
and specializing those variables and the two protected variables to
zero preserve real stability or give the zero polynomial. These
closure statements also follow directly from the one-variable
Gauss--Lucas/Hurwitz argument applied successively to the variables.

The actual P_N is nonzero whenever its original complete coefficient
is nonzero, as holds for every sufficiently large level under the
retained complete-source hypotheses. Hence P_N is a homogeneous binary
real-stable polynomial with nonnegative coefficients. Equivalently,
including possible roots at zero or infinity,

\[
P_N(A,C)=P_N(1,1)\prod_{r=1}^{d}
 \bigl[(1-\lambda_{N,r})C+\lambda_{N,r}A\bigr],
\qquad 0\le\lambda_{N,r}\le1.\tag{14}
\]

This applies to the original globally extracted polynomial, not to a
degree projection of an isolated coupon. We make no corresponding
even-level stability assertion here; the exact reduction (1)-(12)
holds at both parities.

## 5. The exact remaining negative-axis variational problem

For odd levels (14) turns (10) into

\[
\begin{aligned}
\log B_N^- -\log P_N(1,1)
 &=\max_{0\le t\le1}\sum_r\log|1-(1+t)\lambda_{N,r}|,\\
\log B_N^+ -\log P_N(1,1)
 &=\max_{0\le t\le1}\sum_r\log|t-(1+t)\lambda_{N,r}|.
\end{aligned}\tag{15}
\]

Zeros have logarithm minus infinity. These are genuine signed
boundary potentials, with the SAME root parameters for both branches.
There is no modulus replacement before the original face extraction.

A mean condition \(N^{-1}\sum_r\lambda_{N,r}\to\nu\) alone cannot bound these
potentials by a universal positive loss. Products approaching
A^(nu N) C^((1-nu)N) have that mean and almost no loss at t=1.
Such abstract examples are NOT asserted to arise from an original
stationary triangulated exterior. The original R(s), genuine circle
packing and fixed exterior targets are additional necessary data.

For a strict one-cap stationary exterior, the original-chain
theorem supplies M_cap-Phi_D<=W(nu)/pi-g/(2pi). A sufficient next
statement is a bound on both actual quantities in (15) that pays the
actual positive normalization's excess over Phi_D; the whole-star
phase gap alone does not quantify it. No such bound is proved here.
In particular neither real stability, nor the formal identity of the
mean with nu, is being used as a substitute for an original-disk
variational inequality.

## 6. A finite global variance budget at odd levels

The genuine factorization (14), unlike an arbitrary star majorant,
also supplies an explicit finite loss. Set

\[
\begin{aligned}
L_N&=-\sum_r\log\max(\lambda_{N,r},1-\lambda_{N,r}),\\
V_N&=\sum_r\lambda_{N,r}(1-\lambda_{N,r})
 =\left.\partial_z^2\log P_N(e^z,1)\right|_{z=0}.
\end{aligned}\tag{16}
\]

For every p,t in [0,1], the two affine functions in (15) attain
their largest absolute values at an endpoint of the t interval.
The endpoint values are 1-p, |1-2p| and p, all at most
max(p,1-p). Moreover

\[
-\log\max(p,1-p)\ge\min(p,1-p)\ge p(1-p).
\]

Thus the following inequalities are exact, with no asymptotic
coefficient or root-distribution assertion:

\[
\begin{aligned}
\max(B_N^-,B_N^+)&\le P_N(1,1)e^{-L_N}\le P_N(1,1)e^{-V_N},\\
|S_N|&\le N^2\left(1+\frac{\pi^2}{4}\right)P_N(1,1)e^{-L_N}+|T_N|.
\end{aligned}\tag{17}
\]

Equivalently the first term uses the genuine logarithmic Mahler measure

\[
\begin{aligned}
\operatorname{Mahler}(P_N)
 &=\exp\left[\frac1{2\pi}\int_0^{2\pi}\log|P_N(e^{i\theta},1)|\,d\theta\right]\\
 &=P_N(1,1)e^{-L_N}.
\end{aligned}\tag{17a}
\]

The equality follows factor by factor from the circle logarithmic
mean; roots on the circle are integrable. This is a property of the
exact globally extracted polynomial. It is not the Mahler measure
of separate local coupons or an exchange of a coefficient and a norm.

There is a simple additional sufficient condition. Let k_N be the
number of factors in (14) with \(\lambda_{N,r}\ge1/2\), counting all ties.
At a tied factor the two terms are equal, and here the A term is selected.
The original positive coefficient \(p_{N,k_N}\) contains
the product obtained by selecting the larger term from every factor.
Therefore

\[
\operatorname{Mahler}(P_N)\le p_{N,k_N}.\tag{17b}
\]

If liminf_(N odd) k_N/d>=1/2, (4)-(5) imply a strict gap for (17a)
and hence for the actual cap sector. This is a root-count condition
on the original extracted polynomial; it is not implied by its mean.

In a genuine strict one-cap stationary configuration, finite common
weights L_A=L_C give the SAME valid residual dual upper bound for
every s, and attain that bound at the stationary nu. Therefore
R(nu)=M_cap is its unrestricted maximum, including s>1/2. The same
upper coefficient argument (5), summed over j, gives

\[
\limsup_{N\to\infty}\frac1N\log P_N(1,1)\le M_{\mathrm{cap}}.\tag{18}
\]

No lower coefficient rate or convergence of the second derivative
is needed here. Consequently a sufficient, explicitly quantitative
condition for this fixed-spectrum odd subsequence is

\[
\liminf_{\substack{N\to\infty\\N\ \mathrm{odd}}}\frac{L_N}{N}
 >M_{\mathrm{cap}}-\Phi_D.\tag{19}
\]

The same sufficient condition with V_N in place of L_N is weaker
but uses only the finite positive residual variance. If either
liminf is at least M_cap-Phi_D, the weak absolute rate bound follows.
If it exceeds that value by delta>0, (7), (17), (18) give a strict
rate loss at least min(delta,gamma_D/2), after an arbitrarily small
limiting error. These are sufficient criteria, not conclusions about
all original exteriors.

The geometric W budget is one possible way to upper-bound the right
side of (19), but it has NOT been compared with L_N or V_N. In fact
the factorwise estimate itself has a definite limitation:

\[
\begin{aligned}
0\le L_N&\le2\log2\sum_r\lambda_{N,r},\\
0\le V_N&\le d\,\bar\lambda_N(1-\bar\lambda_N),\qquad
\bar\lambda_N=\frac1d\sum_r\lambda_{N,r}.
\end{aligned}\tag{20}
\]

For the first inequality, -log(1-p)<=2p log2 on 0<=p<=1/2
by convexity and the endpoint chord, while for p>=1/2 one has
-log p<=log2<=2p log2. The second is Jensen's inequality for
p(1-p). Thus this factorwise method cannot automatically pay a
larger proposed nu-only budget. Equation (15), which retains the
common optimizing t across ALL factors, is potentially sharper.

This section is a general exact-source extraction criterion. It does
not iterate a local cancellation estimate, claim a stationary phase
for the signed polynomial, or infer an inequality from the mean alone.

## Inputs and scope

Exact cap support and the all-index formula are in
[the original cap source interface](research_cap_cross_high_demand_signed_contraction.md),
section 6. The [positive cap moment law](research_flat_cap_positive_moment_form.md)
supplies the finite moments, including the last moment used here.
The [original residual capacity](research_cap_constrained_capacity_budget.md)
fixes every target and the complete-cap entropy in (3).
The closed CROSS coefficient uppers are in the
[even half-block theorem](actual_fejer_half_block_entropy.md) and the
[odd original-source theorem](actual_fejer_odd_regularized_full_numerator.md),
with the literal original shared-array dictionary. The
[odd determinant factorization](actual_cross_cofactor_factorization.md), section 3,
and [positive physical pencils](actual_q_hahn_boundary_model_curvature.md)
give (13). The [original one-cap chain budget](research_one_cap_original_chain_volume_budget.md)
provides the geometric sufficient comparison discussed after (19).

Common weights give the same upper bound for every boundary split and attain it at the stationary split $\nu$. This is a sufficient criterion, not a universal absolute-volume comparison.

This supplies no near-spectrum extension and no complete fixed-plat or
filled-period theorem. No numerical scan or source lower asymptotic is
used in (1)–(12). The inequality comparing the actual negative-axis or
Mahler growth with Phi remains open without a sufficient condition such
as (19) or the stated root-count test.
