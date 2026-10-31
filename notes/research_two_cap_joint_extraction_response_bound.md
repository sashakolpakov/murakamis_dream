# Actual two-cap extraction and an original-demand response certificate

31 October 2026. **exact-source and analytical research theorem.**
Unpublished. The response inequality below is a sufficient certificate;
its universal passage is not claimed.
The source is the original simple matched sphere with the original protected
MAIN pair u,v. There are two strict residual caps, all other coupons are
CROSS at their actual endpoint -2, and both caps are at +2. The geometric
classification has already proved that the two ordinary cap pairs are
disjoint. Label child/outer pairs (A,C) and (B,D). The finite common weights
satisfy L_A=L_C=a>0 and L_B=L_D=b>0. The exterior ordinary incidences are
positive. This note does NOT prove that the resulting certificate always
passes, and gives no varying-spectrum or filled-period theorem.

Inputs are the durable two-cap cylindrical-exterior theorem, the original
one-cap negative-axis reduction and cap moment form, the actual odd CROSS
determinant factorization, and the original positive determinant curvature.
The [two-cap geometry](research_two_cap_cylindrical_exterior_volume_budget.md)
and the [one-cap extraction](research_global_cap_negative_axis_and_mahler_bound.md)
retain the same source. There is no changed-diagram identification.

## 1. Four boundary variables and the two separate degree targets

Put d=N-1, M=floor(N/2)-1, H=M+1, and let I be the ordinary faces other
than A,C,B,D. Protected variables are set to zero first. Remove the fixed
common raw unit scalars and form the actual exterior polynomial

\[
\begin{aligned}
 E_N(L)&=\prod_{e\ \mathrm{not\ a\ cap}}P_{e,\mathrm{CROSS}}(-2;L),\\
 P_N(A,C,B,D)&=\left[\prod_{i\in I}L_i^d\right]E_N(L).
\end{aligned}
\]

There are R-2 exterior ports and R-4 extracted ordinary faces, so P_N is
homogeneous of degree 2d. Its coefficients are nonnegative at both
parities. The cap contractions impose MORE than this total degree:

\[
\begin{aligned}
 Q_N(A,C,B,D)&=[z^d]P_N(zA,zC,B,D)\\
 &=\sum_{0\le j,k\le d}p_{N,jk}A^jC^{d-j}B^kD^{d-k}.
\end{aligned}\tag{1}
\]

The second pair degree is d by total homogeneity. Neither the cylinder
construction nor the stationary classical pair loads makes the first
projection redundant at finite N. All cap formulas below apply to Q_N,
not to unprojected P_N.

With theta=pi/N and c_r=2cos((2r+1)theta), retain

\[
U_j=\left(\prod_{r=1}^{j}4\sin^2(r\theta)\right)
       \prod_{r=j+1}^{d}(2-c_r),\qquad 0\le j\le d.
\]

After the literal reflected cap relabeling if necessary, the actual
cap coefficient is (-1)^j U_j times child^(d-j) outer^j. Thus, up to ONE
fixed unit scalar, the original two-cap sector coefficient is exactly

\[
S_{LL}=\sum_{0\le j,k\le M}(-1)^{j+k}U_jU_kp_{N,jk}.\tag{2}
\]

Every original ordinary degree d is now imposed. No independent signs
are assigned to repeated face occurrences.

## 2. Completion has two mixed strips, not only a harmless double tail

Write S_** for the same sum over all 0<=j,k<=d, S_H* for j>=H and all k,
S_*H for all j and k>=H, and S_HH for both indices >=H. Then

\[
S_{LL}=S_{**}-S_{H*}-S_{*H}+S_{HH}.\tag{3}
\]

The exact cap moment law gives independent X,Y>0 with

\[
\begin{gathered}
 \mathbb E X^j=\mathbb E Y^j=\frac{U_j}{U_0}\quad(0\le j\le d),
 \qquad 0<U_j\le N^2,\\
 m_d=\mathbb E X^d=N^2\sin^2\frac{\pi}{2N}\le\frac{\pi^2}{4}.
\end{gathered}
\]

Consequently

\[
S_{**}=U_0^2\mathbb E Q_N(-X,1,-Y,1).\tag{4}
\]

This is absolutely integrable since Q_N has degree d in EACH pair.
Interchanging an unprojected P_N, which can have individual degree 2d,
with these moment integrals is not justified and is not done.

For v_-(t)=(-t,1), v_+(t)=(-1,t), define four actual suprema

\[
B_{\epsilon,\eta}=\sup_{0\le t,s\le1}
       |Q_N(v_\epsilon(t),v_\eta(s))|.
\]

Homogeneity and the four regions X<=1/X>=1, Y<=1/Y>=1 give

\[
|S_{**}|\le U_0^2\left[B_{--}+m_d(B_{+-}+B_{-+})+m_d^2B_{++}\right].\tag{5}
\]

Let R(s,t) be the original exterior complete-triangle capacity with
residual A,C loads s,1-s, B,D loads t,1-t, every i in I load one, and
u,v load zero. Empty fibers have value minus infinity. The original
complete capacity is exactly

\[
\Phi_D=\max_{s,t\in[1/2,1]}
       \left[R(s,t)+2f(s-\tfrac12)+2f(t-\tfrac12)\right].\tag{6}
\]

This fills the two original cap half-triangles and leaves every other
triangle and target unchanged. Therefore there is gamma_HH>0 with

\[
\max_{s,t\in[1/2,1]}R(s,t)\le\Phi_D-\gamma_{HH}.\tag{7}
\]

For an interior coordinate its added entropy is positive. At the four
remaining corners both added entropies vanish, but at least one original
ordinary cap incidence is zero; the unique positive complete optimizer
cannot occur there. Compactness and upper semicontinuity prove (7).
The proved CLOSED local coefficient upper and polynomial shared-array
count imply the corresponding uniform upper for p_(N,jk). Since U_j U_k
are polynomially bounded, for all sufficiently large levels

\[
|S_{HH}|\le e^{N(\Phi_D-\gamma_{HH}/2)}.\tag{8}
\]

The finite thresholds satisfy H/d>=1/2 at both parities. In contrast,
neither S_H* nor S_*H has this argument: its other residual coordinate
may be below 1/2. Dropping those mixed strips would be an actual error.
Sections 5-6 give separate original-demand bounds for them.

## 3. What stability survives, and the exact determinant inequality

On odd levels N=2m+1, every actual exterior CROSS coupon is

\[
\begin{gathered}
 N^2D_m(x,b,y)D_m(x,c,y),\\
 D_m(x,b,y)=\det\left[bI+\frac{x}{2}H_-+\frac{y}{2}H_+\right].
\end{gathered}\tag{9}
\]

with the original positive Hermitian H_-,H_+. Products, shared-variable
identifications, individual coefficient extractions and zero
specializations show that P_N is real stable or zero. We do NOT conclude
that Q_N is jointly real stable.

Two valid conditional statements remain. For fixed positive B,D,
P_N(A,C,zB,zD) is stable in A,C,z; its coefficient [z^d] is precisely
Q_N(A,C,B,D), so this binary homogeneous polynomial is stable or zero.
Also every individual row

\[
q_{N,j}(B,D)=[A^jC^{d-j}]P_N(A,C,B,D).
\]

is binary real stable or zero. These facts do not multiply conditional
negative-axis losses, and do not identify the full joint polynomial with
a product of Bernoulli factors.

Here is a different exact inequality which DOES retain the projection.
For each determinant t in (9), at arbitrary positive ordinary weights,
write its pencil as M_t=sum_f L_f K_tf>0 and set

\[
A_{tf}=M_t^{-1/2}L_fK_{tf}M_t^{-1/2},\qquad\sum_fA_{tf}=I.
\]

Protected zero terms are absent. For complex numbers |z_f|<=1, set
Z_t=sum_f z_f A_tf. The unital completely positive map from diagonal
scalars to sum_f z_f A_tf is contractive (equivalently insert the
isometry v -> (sqrt(A_tf)v)_f), so Z_t^*Z_t<=I. Therefore

\[
\begin{aligned}
 \log|\det Z_t|&\le-\frac12\operatorname{Tr}(I-Z_t^*Z_t)\\
 &=-\frac12\sum_f(1-|z_f|^2)\operatorname{Tr}A_{tf}
   -\frac12\sum_{f<g}|z_f-z_g|^2\operatorname{Tr}(A_{tf}A_{tg}).
\end{aligned}\tag{10}
\]

The inequality includes singular Z_t by continuity. All pair traces
are real and nonnegative. There is no commutativity assumption.

Define the normalized original loads and conductances

\[
\begin{gathered}
 r_{N,f}=\frac1N\sum_t\operatorname{Tr}A_{tf},\qquad
 g_{N,fg}=\frac1N\sum_t\operatorname{Tr}(A_{tf}A_{tg})\quad(f\ne g),\\
 H_N=\operatorname{Laplacian}(g_N)
       =\frac1N\operatorname{Hess}_{\log L}\log E_N(L).
\end{gathered}\tag{11}
\]

The scalar coupon factors N^2 remain in E_N and disappear only from
these derivatives. The factor N, rather than d, in (11) agrees with
the coefficient-rate normalization. The total loss in (10), divided
by N, is

\[
e_N(z)=\frac12\sum_fr_{N,f}(1-|z_f|^2)
       +\frac12\sum_{f<g}g_{N,fg}|z_f-z_g|^2.\tag{12}
\]

For each individual coordinate its quadratic coefficient is exactly
-sum_t Tr(A_tf^2)/(2N)<=0. Thus, when z_f is constrained to a fixed ray
and its modulus varies in [0,1], e_N is concave in that modulus. This
finite identity will justify radial endpoint minimization BEFORE any
Schur relaxation.

The exterior ordinary-pair graph is connected. Deleting the two cap
patches removes no ordinary edge from that graph: their only ordinary
edges AC and BD each have the opposite triangle still in the CROSS
exterior; the two pairs are disjoint. The original ordinary graph was
connected. Hence H_N has only the common scaling kernel. Its grounded
principal submatrices are positive definite. The actual determinant
derivative theorem gives r_N -> r and H_N -> H at fixed positive
weights, where H is the original complete-triangle conductance
Laplacian. No signed or projected coefficient limit is used here.

## 4. The four joint negative boxes have a finite response loss

Return to common cap weights A=C=a, B=D=b. Set

\[
F_N(L)=\frac1N\log E_N(L)
       -\frac dN\left[\sum_{i\in I}\log L_i+\log a+\log b\right].\tag{13}
\]

To bound B_(epsilon,eta), the exact coefficient contour for (1) has
the phases

\[
(z_A,z_C)=e^{i\theta}v_\epsilon(t),\qquad
 (z_B,z_D)=v_\eta(s),\qquad z_i=e^{i\theta_i}\quad(i\in I).\tag{14}
\]

The phase theta is the original PAIR-TOTAL projection [z^d]. Its
Fourier multiplier has modulus one. It cannot be fixed independently
or omitted. All measures are the original normalized torus measures.
The positive prefactor after dividing by a^d b^d is exp[N F_N(L)].

For fixed theta and theta_i, separate concavity from (12) shows that
the minimum over t,s occurs at their endpoints. Across all four boxes
this leaves the three real vectors per pair

\[
\mathcal V=\{(-1,1),(0,1),(-1,0)\}.
\]

For \(v,w\in\mathcal V\), all other moduli are one. Thus the radial part of (12)
is half the sum of r_(N,f) over zero boundary coordinates, and its
remaining part is half the ordinary complex Dirichlet energy.

Let boundary order be (A,C | B,D), and take the exact Schur complement

\[
K_N=H_{N,bb}-H_{N,bI}H_{N,II}^{-1}H_{N,Ib}.
\]

Relaxing the interior unit phases to arbitrary complex values lowers
the Dirichlet energy, with minimum z_b^* K_N z_b. Write its pair blocks
as K11,K12,K22. For z_b=(e^(i theta)v,w), the relative theta remains:

\[
z_b^*K_Nz_b=v^TK_{11}v+w^TK_{22}w
       +2\cos\theta\,v^TK_{12}w.
\]

Consequently define the exact finite positive loss

\[
\delta_{12,N}=\frac12\min_{v,w\in\mathcal V}
 \left\{\sum_{f:(v,w)_f=0}r_{N,f}
       +v^TK_{11}v+w^TK_{22}w-2|v^TK_{12}w|\right\}.\tag{15}
\]

There are nine expressions. Connectedness and positive boundary loads
make their minimum positive: if there is a zero coordinate its radial
cost is positive, while with no zero the pairwise opposite boundary
values cannot be one common constant. The same argument applies to
the limiting matrix, so delta_(12,N)->delta_12>0.

Equations (10)-(15) prove, uniformly over all four boxes,

\[
B_{\epsilon,\eta}\le e^{N(F_N(L)-\delta_{12,N})}.\tag{16}
\]

Here Q_N in the definition of B is at unweighted coordinates. Its
bihomogeneity is exactly what canceled a^d b^d. The interior and
pair-phase integrations introduce no exponential or polynomial loss.
At the genuine common stationary weights, F_N(L)->M_2. Hence

\[
\limsup_{N\ \mathrm{odd}}\frac1N\log|S_{**}|
       \le M_2-\delta_{12}.\tag{17}
\]

This is an explicit global simultaneous cancellation bound using the
original pair targets. It is not a claim that its loss pays the full
geometric budget.

## 5. Each mixed strip retains a one-pair loss and its high-degree cost

Fix j and write q_j(B,D) as in section 3. Its degree is d. Completion
of only the SECOND cap gives

\[
\sum_{k=0}^{d}(-1)^kU_kp_{N,jk}=U_0\mathbb E q_j(-Y,1).
\]

Its two negative-axis suprema can again be bounded directly by (10),
without appealing to binary roots. Use arbitrary positive weights

\[
A=ae^z,\qquad C=a,\qquad B=D=b,\qquad z\ge0.
\]

and retain all original I targets. Now A and C are individually
extracted, to j and d-j, so their two phases are independent unit
phases. Only B,D have the negative-axis boundary constraint. Let
kappa_(2,N)(L)>0 be the effective conductance between B,D in H_N,
eliminating ALL other ordinary vertices. The same radial endpoint
and Dirichlet argument gives

\[
\delta_{2,N}(L)=\min\left\{2\kappa_{2,N},
       \frac{r_{N,B}+\kappa_{2,N}}2,
       \frac{r_{N,D}+\kappa_{2,N}}2\right\}.\tag{18}
\]

Indeed the two-terminal Schur matrix is kappa[[1,-1],[-1,1]];
the opposite pair (-1,1) has half-energy 2kappa, and each one-zero
case adds its half-load to half-energy kappa/2. These are the exact
normalizations.

Use (13) with A=a exp(z) in the product E_N but keep its displayed
subtractions log a+log b. Cauchy extraction of A^j C^(d-j) gives
the ADDITIONAL factor exp(-zj). Both row negative-axis suprema obey

\[
B_{j,\pm}\le e^{N(F_N(L)-\delta_{2,N}(L))-zj}.\tag{19}
\]

This is uniform in every actual j, including zero row polynomials.
The original moments and U_j<=N^2 therefore prove

\[
|S_{H*}|\le\operatorname{poly}(N)
       e^{N(F_N(L)-\delta_{2,N}(L))-zH}.\tag{20}
\]

The polynomial is uniform on fixed positive weight compacts; one may
take the explicit factor (d+1)N^4(1+pi^2/4). No j-dependent saddle or
lower coefficient asymptotic is required. Since H/N->1/2,

\[
\limsup_{N\ \mathrm{odd}}\frac1N\log|S_{H*}|
       \le F(L)-\frac z2-\delta_2(L).\tag{21}
\]

The reflected statement for S_*H uses B=b exp(z), D=b, A=C=a, with
delta_1 the effective A,C response. The mixed sums retain their
original indices and signs throughout; taking their absolute values
does not discard their other cap's cancellation.

## 6. A finite classical sufficient criterion, with a local tilt improvement

The limiting positive functional in (13) is the original exterior
triangle potential

\[
F(L)=\sum_{t\ \mathrm{exterior}}Q_t(L)
       -\sum_{i\in I}\log L_i-\log a-\log b.\tag{22}
\]

At the stationary weights it is M_2. In fact the same weights give
R(s,t)<=F(L)=M_2 for every residual pair split: the two boundary
log-weight contributions are always log a+log b. Equality holds at
the actual (nu_1,nu_2) allocation. For the first mixed strip one
may choose ANY fixed positive weights with A/C=exp(z)>=1 and B=D;
then (21) is a valid upper bound. Thus one needs no global real
saddle continuation to state or verify the following certificate.

Choose two such weight systems L^(1),L^(2), with respective z_1,z_2>=0,
and compute their actual conductance matrices and loads. If

\[
\max\left\{M_2-\delta_{12},\
 F(L^{(1)})-\frac{z_1}{2}-\delta_2(L^{(1)}),\
 F(L^{(2)})-\frac{z_2}{2}-\delta_1(L^{(2)})\right\}<\Phi_D.\tag{23}
\]

then the original two-cap sector at the specified endpoint spectra
has a strict exponential gap below Phi_D along odd levels. This follows
from (3),(8),(17),(21), with only four terms. Replacing < by <= gives
the corresponding weak upper bound. No sector has been moved to a
different marked source.

There is a legitimate local optimization for these weights. Fix b=1,
write A=a exp(z), C=a, B=D=1, and minimize (22) in log a and log L_I.
At z=0 the common stationary weights solve these equations. Their
Hessian is the restriction of the connected original conductance
Laplacian, anchored at B,D, hence positive definite. The implicit
function theorem gives an analytic local family L^(1)(z) and F_1(z),
with

\[
F_1(0)=M_2,\qquad F_1'(0)=\nu_1<\frac12.\tag{24}
\]

The derivative is the original residual A load. Thus the high-degree
Chernoff part F_1(z)-z/2 itself strictly improves for small z>0.
The response delta_2(z) is continuous (a minimum of three smooth
expressions); its change must still be retained when checking (23).
The second mixed strip has the analogous family and derivative nu_2.
This local construction does not assume global saddle differentiability.

The geometric theorem supplies

\[
M_2-\Phi_D\le\frac{W(\nu_1)+W(\nu_2)}{\pi}-\frac{g_D}{2\pi}.
\]

One sufficient way to verify (23) is that all THREE explicit losses
M_2 minus its entries exceed this available budget. No such universal
comparison is claimed. In particular, a relative delta>0 alone does
not give an absolute Phi_D bound.

There is a simpler, possibly weaker, test requiring no tilt. At the
common stationary weights one has

\[
\delta_{12}\ge\max(\delta_1,\delta_2).
\]

For each state in (15), drop the other pair's nonnegative radial
cost and relax its boundary values as well as the interior values.
The resulting two-terminal minimum is exactly one of the three
expressions in (18), for the retained pair. This proves the claim
for either pair, before taking the minimum over states. Consequently

\[
\min(\delta_1,\delta_2)>M_2-\Phi_D.\tag{23a}
\]

alone implies the strict odd endpoint two-cap bound. At stationarity
the explicit two-terminal losses are

\[
\delta_i=\min\left\{2\kappa_i,\frac{\nu_i+\kappa_i}{2},
       \frac{1-\nu_i+\kappa_i}{2}\right\}.
\]

Condition (23) retains the potentially useful extra high-degree costs
and does not require (23a).

## 7. Scope and precise remaining issue

The exact extraction, moment completion and high-high tail statement
hold at both parities. The determinant response certificate is proved
for ODD N, where (9) is the actual endpoint source, not a positive
comparison substituted after signs. It controls actual globally
extracted coefficients, including the pair-total Fourier phase.

The new finite algebraic inequality (10) and nine-state response bound
do not require real stability of Q_N. Conditional binary stability is
recorded only where valid. All normalizations use N in the exponential
rate, d in the original finite degree targets, and actual odd matrices
of size m. The source constants remain in F_N. No independent phase
per occurrence, changed exterior target, omitted parity seam, or
divergent Mellin integral is introduced.

What remains is quantitative: prove that (23), a stronger exact joint
negative-axis criterion, or another cancellation estimate always pays
the summed original geometric budget for actual cylinder exteriors.
Neither the cylinder topology nor abstract stable-polynomial closure
establishes that inequality here. Even levels, spectral neighborhoods,
and whole filled periods are additional tasks.

## 8. A source-specific obstruction to restoring joint real stability

There is a stronger necessary condition than the abstract projection
counterexample. Any nonzero nonnegative polynomial Q which is
homogeneous of degree d in A,C and degree d in B,D, if jointly real
stable, MUST factor across the two pairs:

\[
Q(A,C,B,D)=Q_1(A,C)Q_2(B,D).\tag{25}
\]

Here is an elementary proof, including absent endpoint coefficients.
Put q(r,s)=Q(r,1,s,1) and Omega=C\(-infty,0]. Every r in Omega is a
ratio of two numbers in the upper half-plane, and the choices for r,s
are independent. Bihomogeneity and stability therefore imply that
q(r,s) never vanishes on Omega times Omega. Let l be its actual degree
in r. Its leading coefficient a(s) is nonzero at every positive s,
because its coefficients are nonnegative and not all zero. Near one
positive s_0, a(s) stays nonzero. For EVERY complex s in this small
disk, every root of the monic polynomial q(r,s)/a(s) lies on the
nonpositive real axis, since no root can be in Omega. Its coefficients
are consequently real. They are also holomorphic in s, so they are
constant. Hence q(r,s)=a(s)p(r) there, and polynomial identity extends
this to all r,s. Homogenizing to the specified degrees proves (25),
with possible monomial factors retained. Both factors have their
nonzero one-variable roots on the negative real axis. Conversely
products of these binary stable factors are jointly stable.

The actual exterior provides an exact classical test against (25).
Use relative log variables z,w and define the positive coefficient
pressure of the SAME Q_N by

\[
G(z,w)=\min_{\log a,\log L_I}
 \left\{\sum_tQ_t(ae^z,a,e^w,1,L_I)-\log a-\sum_{i\in I}\log L_i\right\}.\tag{26}
\]

The formula is needed only on one neighborhood of z=w=0. Its local
minimizer is finite and analytic by the same grounded-Hessian argument
as (24). The original coefficient contour extracts all I demands AND
the pair-total a degree d. Its only positive angular maximum is the
zero phase: A,C share the pair phase, B,D are anchored, and the
connected ordinary graph propagates equality of phases. All characters
are primitive incidence differences. Thus the already proved positive
determinant packet argument, with this literal identified phase,
gives a uniform local complex relative asymptotic and in particular

\[
\left.\frac1N\partial_z\partial_w\log Q_N(e^z,1,e^w,1)\right|_{(0,0)}
       \longrightarrow G_{zw}(0,0).\tag{27}
\]

This is a positive coefficient saddle, not a signed-sector lower.
The actual N^2 source factors and d targets are the same as in (13).

Let K be the four-terminal Schur matrix from section 4, at the actual
stationary weights. Write its off-diagonal entries as -g_fg^eff, with
g_fg^eff>=0, and put

\[
T=g_{AB}^{\mathrm{eff}}+g_{AD}^{\mathrm{eff}}
       +g_{CB}^{\mathrm{eff}}+g_{CD}^{\mathrm{eff}}>0.
\]

After eliminating I, the remaining extracted direction is
e_A+e_C. Taking this ONE further Schur complement gives exactly

\[
\begin{aligned}
 G_{zw}(0,0)&=K_{AB}
       -\frac{(K_{AA}+K_{AC})(K_{AB}+K_{CB})}{T}\\
 &=\frac{g_{AD}^{\mathrm{eff}}g_{BC}^{\mathrm{eff}}
             -g_{AB}^{\mathrm{eff}}g_{CD}^{\mathrm{eff}}}{T}.
\end{aligned}\tag{28}
\]

Therefore, if the explicit determinant in the numerator of (28) is
nonzero for the actual finite-common-weight exterior, its actual Q_N
fails joint real stability at every sufficiently large odd level.
Indeed (25) would make the mixed logarithmic derivative identically
zero, contradicting (27). This criterion refers to the original
gluing solution and its original conductances; it is not a freely
chosen polynomial counterexample.

No claim is made that (28) is always nonzero. A separating ordinary
circle tangent to both protected lines can couple the boundary through
a bottleneck; the cylinder theorem does not exclude that possibility.
Nor does zero in (28) prove factorization. The response bound in
sections 3-6 applies regardless of this diagnostic and never requires
restoring joint stability.

## Dependencies

- [Original two-cap geometry and summed volume budget](research_two_cap_cylindrical_exterior_volume_budget.md)
- [Original negative-axis extraction and strict one-cap tail](research_global_cap_negative_axis_and_mahler_bound.md)
- [Exact all-index cap moment form](research_flat_cap_positive_moment_form.md)
- [Actual endpoint CROSS factorization](actual_cross_cofactor_factorization.md)
- [Finite determinant curvature and positive matrices](actual_q_hahn_boundary_model_curvature.md)
- [Original conductance and coefficient-response normalization](research_global_cap_effective_response_criterion.md)
- [Closed endpoint coefficient entropy](actual_fejer_half_block_entropy.md)
- [Original positive coefficient saddle and torus measure](actual_positive_face_coefficient_saddle.md)

No numerical audit or asymptotic experiment is used as proof. Native
MathML rendering and dependency-link checks validate the document, not
its mathematical conclusions.
