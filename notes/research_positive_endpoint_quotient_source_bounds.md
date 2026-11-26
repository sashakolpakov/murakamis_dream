# Positive-endpoint division preserves the joint turn norm and source profile

Private written proof, 16 November 2026.

Ordinary division at a fixed number of points within \(O(N^{-2})\)
of \(+2\) has polynomial cost in the joint norm of a canonical
polynomial and its first original turn. For original microscopic
endpoint products, the resulting quotient sources also preserve
the physical-color upper profile after any fixed signed \(V_n\).
The forcing is propagated from its actual row, so this conclusion
does not spend the terminal integral twice.

All divisions below are ordinary polynomial divisions before the
specified turn. No physical nonunit is inverted. The theorem does
not concern negative-endpoint division or arbitrary multiplication
after a received turn.

## 1. An unconditional polynomial joint-norm bound

Use the original algebra and operators
\[
 q=e^{\pi i/N},\quad D=N-1,\quad \eta=(-1)^D,\quad
 c_j=2\cos((2j+1)\pi/N),\quad P_N(C)=2T_N(C/2)+2,
\]
\[
 \mathcal A_N=\mathbb C[C]/(P_N),\quad
 e_j(C)=S_j^{-2}\prod_{a<j}(c_a-C),\quad
 S_j=\prod_{a=1}^j2\sin(a\pi/N),
\]
\[
 Te_j=e_{D-j},\quad J=TCT,\quad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\quad
 K_N(w,C)=\sum_{j=0}^D e_j(w)e_j(C).
 \tag{1}
\]
Here multiplication by \(C\) is reduced in the full quotient,
while every input polynomial has its specified canonical
representative of degree at most \(D\). Write
\[
 \|f\|=\sup_{C\in[-2,2]}|f(C)|,\qquad
                       \mathfrak B_N(f)=\|f\|+\|Tf\|.
 \tag{2}
\]

Fix \(s\ge0\) and \(B<\infty\). Let
\[
 a_{\ell,N}=2+\beta_\ell/N^2,\qquad |\beta_\ell|\le B,
                       \qquad 1\le\ell\le s,
 \tag{3}
\]
with arbitrary complex parameters, including collisions. Define
ordinary polynomials recursively by
\[
 f_0=f,\qquad
 f_\ell(C)=\frac{f_{\ell-1}(C)-f_{\ell-1}(a_{\ell,N})}
                              {C-a_{\ell,N}}.
 \tag{4}
\]
Every removable value in (4) has its ordinary polynomial meaning.
These polynomials remain canonical. Their final member is the
ordinary quotient of \(f\) by \(\prod_{\ell=1}^s(C-a_{\ell,N})\).

**Theorem 1.** There are constants \(C,p\), depending only on
\(s,B\), such that for every level and every canonical \(f\),
\[
 \boxed{\quad
       \max_{0\le\ell\le s}\mathfrak B_N(f_\ell)
                           \le CN^p\mathfrak B_N(f).
 \quad}                                                    \tag{5}
\]
Replacing each real norm by
\(\|g\|+N^{-2}\|g'\|\) gives an equivalent assertion. Thus
all original first normals are included. The constants are
uniform for all complex roots in (3); no separation of roots
or confluent interpolation inverse is used.

### Proof

First, for \(|a-2|\le B/N^2\), ordinary polynomial estimates give
\[
 |f(a)|+\left\|\frac{f(C)-f(a)}{C-a}\right\|
                                      \le C_B N^{p_B}\|f\|.
 \tag{6}
\]
To check uniformity also outside the real interval, put the disk
\(|a-2|\le B/N^2\) and \([-2,2]\) inside a Bernstein ellipse
with parameter \(e^{b_B/N}\), enlarged by a fixed factor in
\(b_B\). The ellipse is convex. The Chebyshev coefficient bound
and the finite formulas for the derivative of \(T_k(C/2)\),
\(k\le D\), bound \(f\) and \(f'\) there by a polynomial
times \(\|f\|\). Integrating \(f'\) on the segment from \(a\)
to \(C\) proves (6). This also proves the assertion at coincident
points and for repeated divisions.

For a single division put \(Q=(f-f(a))/(C-a)\), \(Y=TQ\).
The exact coherent equation is
\[
                    (J-a)Y=Tf-f(a)e_D.                    \tag{7}
\]
Both sides are classes in the original full algebra; all first
normals of the reset term remain. We use the existing unconditional
graph-norm estimate for the original \(J\): for every canonical
\(Y\), uniformly when \(|a-c_0|\le\Lambda/N^2\),
\[
 \|Y\|\le C_\Lambda N^{p_\Lambda}
       \bigl(\|(J-a)Y\|+|Y(c_0)|+|Y'(c_0)|\bigr).
 \tag{8}
\]
This is the full-normal estimate in the finite-band operator
source, equation (29). Its proof uses the balanced forward state
\((Y(c_j),(j+1)\Delta Y(c_j))\), with step norm
\(1+C_\Lambda/(j+1)\), the differentiated equation with its
original forcing, and full-Hermite reconstruction. It applies
to arbitrary polynomial forcing and to complex \(a\), not only
to endpoint kernels. Since \(2-c_0=O(N^{-2})\), its parameter
condition holds uniformly in (3).

The two actual anchors are
\[
 Y(c_0)=\phi_N(Q),\qquad
 Y'(c_0)=\phi_N(Q_{0,N}Q),\qquad
 Q_{0,N}(C)=\partial_wK_N(c_0,C).
 \tag{9}
\]
The fixed-row source bound gives \(\|Q_{0,N}\|\le N^{O(1)}\).
The original full-normal trace estimate
\(|\phi_N(uv)|\le CN^5\|u\|\|v\|\), and (6), bound both
anchors by a polynomial times \(\|f\|\). The radical bound
\(\|e_D\|\le\sqrt{N-1}\) bounds the reset in (7).
Equations (6)--(9) consequently give
\[
 \|Q\|+\|TQ\|\le C_BN^{p_B}\bigl(\|f\|+\|Tf\|\bigr).
 \tag{10}
\]
Iterating (10) a fixed number of times proves (5). Markov's
inequality for degree at most \(D\) proves the equivalent
first-normal norm statement. No source has been separated
before the exact identity (7), and no quotient relation was
divided by \(C-a\). \(\square\)

For a holomorphic parameter family the bound is uniform on
larger compact parameter sets. Cauchy's formula therefore
preserves its exponential rate after any fixed parameter
derivatives. Differentiation in \(a_\ell\) costs a factor
\(N^2\) for each derivative in \(\beta_\ell\).

## 2. Original product sources and their actual prefix bounds

Retain the signed operators
\[
 V_n=\kappa^nTR^{-n}T,\quad \kappa=q^{D^2/2},\qquad
 D_n=V_nCV_{-n},\qquad V_n1=1.
 \tag{11}
\]
The last equality follows from
\(Te_0=e_D\), \(R^{-n}e_D=\kappa^{-n}e_D\), and \(Te_D=1\).
No turn is moved through ordinary multiplication.

Fix \(r\ge1\), \(A<\infty\), and an integer \(n\). The input
\(P_0\) can be either
\[
 \operatorname{can}\prod_{i=1}^rK_N(w_i,C),\qquad
 w_i=2\cosh(\alpha_i/N),\quad |\alpha_i|\le A,
 \tag{12}
\]
or any original canonical channel of its six-state tensor module,
with or without its specified gauge. These are the actual products
of \((f_i,\mathcal Df_i,\mathcal Sf_i,
\mathcal S\mathcal Df_i,P_N,1)\), optionally multiplied by the
specified fixed \((C-2)\)-gauge. They are not arbitrary received
coupons. The ungauged extension is proved at the end of §3 by
exact forced recovery, not by division of a quotient identity.
Form \(P_\ell\) from \(P_0\) by (4), and put
\[
 F_\ell=V_nP_\ell,\quad J_N=\lfloor(N-1)/2\rfloor,\quad
 c_N(u)=2\cos(2\pi u+\pi/N).
 \tag{13}
\]

Let \(L_n(u)\ge0\) be the original maximal terminal logarithmic
shift modulus, and define
\[
 \mathcal J_n(u)=\int_0^uL_n(v)\,dv,\quad
 \mathcal I_n=\mathcal J_n(1/2),\qquad L_0=0.
 \tag{14}
\]
The function is integrable, is unchanged under \(n\mapsto-n\),
and vanishes for \(n=\pm1\).

**Theorem 2.** Uniformly on the bounded complex parameters in
(3),(12), for every \(0\le\ell\le s\),
\[
 \boxed{\quad
 \limsup_{N\to\infty}\max_{0\le j\le J_N}
 \left\{\frac1N\log\left(1+
   \sup_{\boldsymbol\alpha,\boldsymbol\beta}
    [|F_\ell(c_j)|+|\dot F_{\ell,j}|]\right)
                         -\mathcal J_n(j/N)\right\}\le0,
 \quad}                                                    \tag{15}
\]
where \(\dot F_{\ell,j}=\partial_uF_\ell(c_N(u))|_{u=j/N}\).
At double physical nodes this also bounds the first spectral
normal. At the odd simple node only its value is required.
Furthermore
\[
 \limsup_{N\to\infty}N^{-1}
       \log\left(1+\sup_{\boldsymbol\alpha,\boldsymbol\beta}
                               \|F_\ell\|\right)\le\mathcal I_n.
 \tag{16}
\]
Fixed derivatives in the endpoint and division parameters retain
(15); fixed spectral derivatives retain (16). No higher spectral
derivative profile between physical rows is asserted.

We first treat the product itself and the gauged channels, and
justify their source profile \(\ell=0\) from the actual equations.
The first-turn theorem gives
\[
 \|P_0\|\le N^{O(1)},\qquad \|TP_0\|\le e^{o(N)}
 \tag{17}
\]
simultaneously for these gauged channels and the product, uniformly
on bounded complex parameter sets. Its signed initialization argument gives
subexponential fixed-row values and normals for \(V_nP_0\).
The original product recurrence, including its gauged channels
and forced recovery, has compact propagator
\[
 \|\mathcal T_{j_2,j_1}\|
 \le C_\epsilon N^{p_\epsilon}
       \exp\left\{N\int_{j_1/N}^{j_2/N}L_n(u)\,du
                          +C_\epsilon N^{1-1/(66r)}\right\}.
 \tag{18}
\]
Its endpoint strips, including every prefix, cost
\(\exp\{CN\epsilon\log(e/\epsilon)+O(\log N)\}\),
with \(C\) independent of \(\epsilon\). These are the original
coupled value/normal estimates, with the source and recovery
windows of their actual sizes.

Stop (18) at the row producing the desired channel value and
normal. Fixed shifts of its window endpoints cost
\(O_\epsilon(1)\) in the exponent on a compact interval.
The left strip and its subexponential initial data therefore give
\[
 N^{-1}\log(1+|F_0(c_j)|+|\dot F_{0,j}|)
 \le \mathcal J_n(j/N)+C\epsilon\log(e/\epsilon)+o_\epsilon(1)
 \tag{19}
\]
through the compact interval. The same endpoint estimates cover
the first strip. On the last strip, the whole upper bound is
\(\mathcal I_n+o(1)\), and its excess over \(\mathcal J_n(j/N)\)
is at most \(\int_{1/2-\epsilon}^{1/2}L_n\), up to the vanishing
endpoint loss. Sending \(N\) to infinity before \(\epsilon\)
to zero proves (15) for \(\ell=0\). This uses the actual prefix
estimate, not an inference of a color profile from a whole norm.
For \(n=0\), all inputs have polynomial norm and the assertion
is immediate. The same stopping argument covers \(n=\pm1\),
where \(L_n=0\).

## 3. Signed forced recovery of each quotient

For the product and gauged starting channels, Theorem 1 and (17)
imply simultaneously
\[
 \|P_\ell\|\le N^{O(1)},\qquad
                         \|TP_\ell\|\le e^{o(N)}.
 \tag{20}
\]
For every fixed initial row \(j\), the original identities are
\[
 \begin{split}
 F_\ell(c_j)&=\kappa^n\phi_N(R^{-n}(TP_\ell)F_{j,N}),\\
 F_\ell'(c_j)&=\kappa^n\phi_N(R^{-n}(TP_\ell)Q_{j,N}),
 \end{split}
 \quad
 F_{j,N}(C)=K_N(c_j,C),\quad
 Q_{j,N}(C)=\partial_wK_N(c_j,C).
 \tag{21}
\]
The two fixed-row coupons have polynomial norm. The original
crossing has unit-modulus physical values and polynomial first
normals. The coherent trace and Hermite estimates applied to
(21) therefore give subexponential initial values and normals
for every fixed window, uniformly in all parameters. This is
actual source initialization, not arbitrary recurrence data.

Conjugating the ordinary division identity by \(V_n\) gives
\[
 \boxed{\quad
 (D_n-a_{\ell,N})F_\ell
                   =F_{\ell-1}-P_{\ell-1}(a_{\ell,N})1.
 \quad}                                                    \tag{22}
\]
The scalar evaluation on the right is polynomially bounded by
(6),(20). All residuals and normals of (22) remain in the full
algebra. In particular (22) is not solved by an inverse of
\(D_n-a_{\ell,N}\).

For \(n=\sigma m\ne0\), \(m=|n|\), the exact extreme coefficients
of its ordinary physical lift are unchanged by subtracting \(a\):
\[
 b_+(j)=q^{-\sigma(2j+m+1)}\prod_{h=0}^{m-1}A(j+h),\qquad
 b_-(j)=q^{\sigma(2j-m+1)}\prod_{h=0}^{m-1}B(j-h),
 \tag{23}
\]
with
\[
 A(t)=\frac{s_{t+1}^4}{s_{2t+1}s_{2t+2}},\quad
 B(t)=\frac{s_t^4}{s_{2t}s_{2t+1}},\quad s_t=2\sin(\pi t/N).
\]
Use the genuine length-\(2m\) window from \(j-m\) through
\(j+m-1\), and its first-\(u\)-normal window. The leading
coefficient \(b_+(j)\) is nonzero on every forward row used
below. The normal equation is obtained by differentiating the
ordinary residual before evaluation. Since
\[
                         P_N(c_N(u))=4\sin^2(\pi Nu),
 \tag{24}
\]
its value and first derivative vanish at the grid. Thus the
exact homogeneous value/normal matrix is
\[
 \begin{pmatrix}\mathsf A_N&0\\\mathsf A_N'&\mathsf A_N\end{pmatrix},
 \tag{25}
\]
with forcing formed from both the value and normal of the
right side of (22), including the derivative of \(b_+^{-1}\).

On a fixed buffered compact interval, its scalar principal
companion has precisely the terminal roots of \(x_n-2\),
each double. The complex perturbation \(a_{\ell,N}-2=O(N^{-2})\)
does not change this limit and is uniform without separation
among the different \(a_\ell\). Confluent frames at the separated
terminal roots, scaling each double chain by
\(\operatorname{diag}(1,N^{-1/2})\), and grading the independent
normal block by \(N\), give the homogeneous bound
\[
 \|\mathcal U_{j,k}\|
 \le C_\epsilon N^{p_\epsilon}
  \exp\left\{N\int_{k/N}^{j/N}L_n(u)\,du+C_\epsilon\sqrt N\right\}.
 \tag{26}
\]
Indeed the finite coefficients and frame changes are \(O(N^{-1})\)
perturbations, whose scaled cost is \(O(N^{-1/2})\); the bounded
normal coupling gains the same factor after the grade change.
This is the two-chain instance of the actual product transfer
estimate. All signs in (23) are retained before bounding.

Suppose (15) has been proved for \(F_{\ell-1}\). On the compact
interval, the forcing packet at row \(k\) is bounded by
\(N^{O(1)}\exp\{N\mathcal J_n(k/N)+o(N)\}\), uniformly.
Variation of constants with (26) gives the exponent
\[
 \mathcal J_n(k/N)+\int_{k/N}^{j/N}L_n(u)\,du
                                      =\mathcal J_n(j/N).
 \tag{27}
\]
There are at most \(N\) forcing packets. Their sum, the fixed
window shifts, and the polynomial factors add only \(o(N)\)
on a fixed compact interval. Thus no second copy of
\(\mathcal I_n\) appears. This argument keeps the original
signed forcing; the triangle inequality is applied only after
the exact recovery equation.

For completeness the endpoint bounds and final output are as
follows. Start at center \(j=m\), whose window uses only fixed
rows \(0,\ldots,2m-1\), initialized by (21). Continue through
\(j=J_N-m\), producing the last physical row \(J_N\).
Every coefficient evaluation in the ordered extremes and
remaining finite-band terms lies between \(j-m+1\) and
\(j+m-1\). With
\(d_j=\min(j-m+1,J_N-m-j+1)\), normalized coefficients,
first derivatives, and forcing selectors are bounded by
\(C(N/d_j)^b\). This follows from the sine-distance bounds
\(|A|+|B|\le C(N/d_j)^2\), \(|A^{-1}|\le C(N/d_j)^4\)
and the fixed ordered formula for \(D_n\). The bounded complex
\(a_\ell\) changes only a middle coefficient. There is no
standalone \(N^b\) cost per row.

Products along any prefix of an endpoint strip of length
\(\epsilon N+O(1)\) cost at most
\(\exp\{CN\epsilon\log(e/\epsilon)+O(\log N)\}\).
On the left, all forcing exponents are at most
\(\mathcal J_n(\epsilon+O(1/N))\). Together with (21), this
initializes (26) at that same profile plus the endpoint loss.
On the right, the forcing is at most \(\mathcal I_n+o(1)\),
so propagation from the last compact row gives the whole
budget \(\mathcal I_n\) plus the endpoint loss. Its excess
over the required right-end profile is bounded by the tail
integral of \(L_n\). The last step uses coefficients at most
\(J_N-1\), so there is no singular next row. It includes
the odd simple value and every even last-row normal.

Take \(N\to\infty\) and then \(\epsilon\downarrow0\).
Equations (26),(27) and these endpoint bounds prove (15)
for \(F_\ell\). Induction proves it for every fixed number
of divisions. Full-Hermite reconstruction yields (16).
At double nodes \(|c_N'(j/N)|\ge c/N\), so conversion of
the scaled angular normal to the first spectral normal costs
only a polynomial factor. No spectral normal is introduced
at the odd simple node.

It remains to justify the ungauged starting channels promised
in §2. Let \(Z_N\) be one such ordinary tensor channel and let
\(a\ge0\) be its fixed gauge exponent. Put
\[
 p_b=\operatorname{can}((C-2)^b Z_N),\qquad 0\le b\le a.
 \tag{28}
\]
Every \(p_b\) has polynomial real norm by the ordinary channel
bounds and full-Hermite reconstruction. The final \(p_a\) is
the known gauged channel. Exactly in the full algebra,
\[
 (J-2)Tp_b=Tp_{b+1},\qquad
                 (D_n-2)V_np_b=V_np_{b+1},\quad b<a.
 \tag{29}
\]
The actual anchors of \(Tp_b\) are polynomial by (9) with
\(Q\) replaced by \(p_b\). Descending induction using (8)
therefore gives \(\|Tp_b\|\le e^{o(N)}\) for every \(b\),
starting from the first-turn bound for \(p_a\). This also
supplies (21) for every \(V_np_b\). For \(n=0\), the polynomial
input bounds already give the claim. Otherwise apply the signed forced
recovery argument (23)--(27) to the second equation of (29),
now with \(a_{\ell,N}=2\) and without a scalar reset. Starting
from the proved prefix profile of \(V_np_a\), descending
induction gives that same profile for \(V_np_0\). Ordinary
divisions (4) can then be applied to \(p_0\) by the already
proved argument. This proves all of Theorem 2. In particular
no claim that dividing \(\operatorname{can}((C-2)^aZ_N)\)
ordinarily recovers \(\operatorname{can}Z_N\) was needed;
the possible \(P_N\) aliases remain in (28),(29).

Uniformity on larger complex parameter sets and Cauchy's
formula prove the parameter-derivative assertions. The maps
\(\alpha_i^2\mapsto N^2(w_i-2)\) have uniformly regular
inverses on bounded smaller domains, so fixed derivatives
in \(w_i\), as well as in \(a_\ell\), cost only polynomial
powers of \(N\). Markov gives the whole-norm assertion for
fixed higher spectral derivatives, but is not used to claim
the smaller physical profile for them.

## 4. Scope and direct sources

The profile (14) is the previously calibrated terminal profile:
for \(|n|\ge2\),
\(\mathcal J_n(u)=\operatorname{Re}S_{|n|}(\pi-2\pi u)\)
with the original branch and endpoint normalization. This
identification does not turn (15) into a bound on a complex
boundary contour or on a subsequent closed graph trace.

Theorem 1 is unconditional for the joint input norm. Theorem 2
uses the original product or stated tensor-channel source before the
divisions, its first-turn estimate, and its actual signed prefix
system. It does not allow arbitrary received transformed factors
to be inserted into that class. If a source-exact parameter row
can be cleared using only roots in (3), its ordinary quotient
packets acquire these budgets; the construction and rank of
that row are separate algebraic obligations. No negative root
is removed or treated by this theorem.

A targeted coverage search found the graph-norm estimate (8),
the original product first-turn theorem, and the existing
physical-prefix argument, but no stated ordinary-division closure.
The new assertions are (5) and the forced quotient-prefix
consequence (15), with their original source initialization.

The following complete direct sources were read at unchanged
pins, with their used implications and hashes checked:

* [Original finite-band operators and graph norm](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb.
* [Original first-turn initialization](research_first_turn_endpoint_product_initialization.md),
  SHA256 7d0871a7dcde94c1cc73f98495b9521a61478729ddd52c51570ffa95f1901105.
* [Actual signed product transfer](research_turned_endpoint_product_characteristic_upper_bound.md),
  SHA256 5e594fa40c1ab70b72a0c1b85748182e33850675a45ed6ea42f2c20349831b2a.
* [Physical rows, radicals, and microscopic input bounds](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.
* [Physical-color profile and action normalization](research_filled_leaf_physical_color_profile.md),
  SHA256 8d9d8feea838832950fbe85f049d33111224ffd3d12e37067c16cd2dc4e3fae9.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted notes and public manuscripts are unchanged.
