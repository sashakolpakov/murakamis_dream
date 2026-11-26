# Reversal and a coherently summed terminal boundary

Research deduction, 5 November 2026. Physical reversal gives a right-cap
version of the fixed-reference prefix estimate, but in the opposite
retained leg family. It does not reverse the arguments of an individual
conditional kernel in the existing integral. A second exact identity
sums the whole terminal coordinate in that existing integral. The result
is one explicit negative-band boundary polynomial. A supporting-plane
upper bound for this polynomial would remove the terminal-coordinate
restriction from an all-plateau first-collar sector. That source bound is
not proved here.

## 1. The two exact one-cap charts

Use the notation of the
[exact conditional composition](research_mixed_conditional_torus_composition.md):
\(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and
\[
 C_{\epsilon,N}(X,Y)=\sum_{j<N}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}}.
 \tag{1}
\]
Write \(\mathcal U_{\epsilon,N}(w,X)\) and
\(\mathcal H_N(w,Y)\) for its whole ordinary-color polynomials,
and \(W_{\epsilon,N}(X)=\{d_N(X)(1+X^{-N})\}^{\epsilon}\).
For a word \(n_j=3+\epsilon_j\), put \(k_4=\sum_j\epsilon_j\)
and \(\mathcal Z_N=v(w_L)^TA_{n_1}\cdots A_{n_m}v(w_R)\).
The original chart is
\[
 \mathcal Z_N=\kappa^{m+k_4}N^{m+k_4}
 \oint \mathcal U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^m C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal H_N(w_R,X_m^{-1})
 \prod_{j=1}^m W_{\epsilon_j,N}(X_j)
 \prod_{j=1}^m\frac{dX_j}{2\pi iX_j}.
 \tag{2}
\]
Here \(X_j=e^{-2\pi it_j}\): the other ordinary leg family
\(s_j\) has been summed. All circles are counterclockwise,
with arbitrary positive radii.

The original matrices \(A_n\), and the matrices \(B_n,\Gamma\)
in the [unsummed contraction](research_mixed_wire_exact_contraction.md),
are symmetric. Transposition therefore gives
\[
 \mathcal Z_N(n_1,\ldots,n_m;w_L,w_R)
 =\mathcal Z_N(n_m,\ldots,n_1;w_R,w_L).
 \tag{3}
\]
In the full index sum this exchanges
\((s_j,t_j)\) with \((t_{m+1-j},s_{m+1-j})\), including the
two private endpoint legs. The triangular supports and ordinary
boundary rows are unchanged. Applying (2) to the reversed word gives
the equally exact chart
\[
 \mathcal Z_N=\kappa^{m+k_4}N^{m+k_4}
 \oint \mathcal H_N(w_L,Y_1^{-1})
 \prod_{j=1}^{m-1}C_{\epsilon_j,N}(Y_{j+1},Y_j)
 \mathcal U_{\epsilon_m,N}(w_R,Y_m)
 \prod_{j=1}^m W_{\epsilon_j,N}(Y_j)
 \prod_{j=1}^m\frac{dY_j}{2\pi iY_j}.
 \tag{4}
\]
Now \(Y_j=e^{-2\pi is_j}\). This is an identity for the whole
ordinary-color polynomial, hence for every fixed ordinary jet and
both level parities. It uses no conjugation.

There is no pointwise substitution \(X_j=Y_{m+1-j}\) turning
(2) into (4). For example, at \(N=3\), direct substitution in
(1) gives
\[
 C_{0,3}(1,r)=2+r,\qquad C_{0,3}(r,1)=2+r^2.
 \tag{5}
\]
The factors are different. Physical matrix symmetry is not symmetry
of this chirped conditional kernel.

## 2. A reflected full-plateau suffix estimate

Apply the [ending-three prefix theorem](research_mixed_first_collar_fixed_reference_completion.md)
and the [ending-four extension](research_mixed_four_enlarged_contour_transport.md)
to the reversed word. Original critical-point uniqueness identifies
its retained reference with \(s_j^*\) in (4). Thus no cyclic
reference or narrower endpoint height range is imported.

Here is the resulting precise allocation. Let \(m\ge4\) and
\(2\le\ell\le m-2\). The right cap coordinate is a real collar
coordinate \(y_m\in[0,\rho]\), the next coordinate has real part
\(y_{m-1}\in I_{3+\epsilon_{m-1}}\), where
\[
 I_3=[.267,.433],\qquad I_4=[.24,.363].
 \tag{6}
\]
Coordinates \(\ell,\ldots,m-2\) are independent unselected
plateau coordinates, with real parts in \(P=[.22,.45]\) and
heights \(\Im s_j^*\). At \(m-1\) use exactly the physical
attenuation path of the corresponding prefix theorem; both selections
are allowed when this type is four. Selection at \(m\) is also
allowed. Set \(d_j=y_j-\Re s_j^*\). The literal suffix is
\[
\begin{split}
 \mathcal R^{\rm cap}_{\ell,N}={}&
 \left|\mathcal U_{\epsilon_m,N}(w_R,Y_m)
          \prod_{j=\ell}^{m-1}C_{\epsilon_j,N}(Y_{j+1},Y_j)\right|\,
 |d_N(Y_m)^{\epsilon_m}Y_m^{-N\sigma_m}|\\
 &\quad\cdot
 |d_N(Y_{m-1})^{\epsilon_{m-1}}Y_{m-1}^{-N\sigma_{m-1}}|
 \prod_{j=\ell+1}^{m-2}|d_N(Y_j)|^{\epsilon_j}
 |d_N(Y_\ell)|^{\epsilon_\ell/2}.
\end{split}
 \tag{7}
\]
The conventions on empty products apply. Let \(\widehat M_\ell\)
be its reference action, and let \(\widehat P_{\ell,b}\) be the
second marginal of its last allocated conditional phase, whose
arguments are \((s_{\ell+1},s_\ell)\). Let
\(\widehat D_j\) be the two-row excess of the reversed ordinary
factor at vertex \(j\). The existing prefix results imply
\[
\begin{split}
 \frac1N\log\mathcal R^{\rm cap}_{\ell,N}
 \le{}&\widehat M_\ell+\Re\widehat P_{\ell,b}d_\ell
       -\delta_{\epsilon_m,\epsilon_{m-1}}
       +\sum_{j=\ell}^{m-2}\widehat D_j+\tau\\
 &-\kappa_*\left(d_{m-1}^2+
            2\sum_{j=\ell+1}^{m-2}d_j^2+d_\ell^2\right)
       +O_m(\log N/N),
 \qquad \kappa_*=1/2500000,
\end{split}
 \tag{8}
\]
where \(\delta_{00}=3/100\), \(\delta_{10}=3/125\), and
\(\delta_{01}=\delta_{11}=4/125\). All internal tangents
cancel; the displayed cut tangent cancels the adjacent phase in the
reversed chart. Source tolerances sum to the one prescribed \(\tau\).
If all \(\widehat D_j=0\), then \(\tau<1/250\) leaves a
common finite loss \(1/50\), with a smaller polynomial prefactor
absorbed for large \(N\). Ordinary colors and fixed jets have the
same fixed-neighborhood scope as the cited prefix results.

This proves a right-cap suffix estimate, but its active collar is
on \(s_m\). It does not estimate an arbitrary region of the
\(t_m\) integral in (2). In particular one cannot combine its
bound with an original-chart prefix bound by multiplying two
pointwise inequalities on different retained variables. The
[exact two-cap chart](research_mixed_two_cap_torus_composition.md)
instead contains its explicit Gram bridge; its separate regular
packet cannot be imported, in view of the
[proved forcing obstruction](research_mixed_gram_forced_transport.md).

## 3. Sum the original terminal coordinate before estimating it

There is a different exact reduction which stays in chart (2).
Define the negative-band Laurent polynomial
\[
 \mathcal V_{\epsilon,N}(w,X)
 :=\sum_{i=0}^{N-1}
       \frac{X^{-i}p_i(X)}{P_i^{1+\epsilon}}
                   \mathcal U_{\epsilon,N}(w,r^i).
 \tag{9}
\]
Its band in \(X\) is contained in \([-N+1,0]\).

**Proposition 1.** For every \(X\ne0\) and every ordinary color,
\[
\begin{split}
 \mathcal V_{\epsilon,N}(w,X)
 &=\sum_{j<N}
    C_{\epsilon,N}(X,r^j)
           \frac{\mathcal H_N(w,r^{-j})}{P_j^\epsilon}\\
 &=N\oint C_{\epsilon,N}(X,Y)\mathcal H_N(w,Y^{-1})
             W_{\epsilon,N}(Y)\frac{dY}{2\pi iY}.
\end{split}
 \tag{10}
\]
The circle in the last line may have any positive radius.

*Proof.* At \(X=r^a\), the exact identities (17)--(18) of the
conditional composition give
\[
\begin{split}
 \sum_j C_{\epsilon,N}(r^a,r^j)
              \frac{\mathcal H_N(w,r^{-j})}{P_j^\epsilon}
 &=P_a\sum_i\Gamma_{ai}
           \frac{(B_{3+\epsilon}b(w))_i}
                {\kappa^{1+\epsilon}N^\epsilon}\\
 &=P_a\sum_i\Gamma_{ai}P_i^{1-\epsilon}
                        \mathcal U_{\epsilon,N}(w,r^i).
\end{split}
 \tag{11}
\]
Here \(b_j(w)=\mathcal H_N(w,r^{-j})/P_j\), and the second
line uses symmetry of \(B_{3+\epsilon}\), not of \(C\).
The original Gram entry gives
\[
 P_a\Gamma_{ai}P_i^{1-\epsilon}
       =\frac{r^{-ai}p_i(r^a)}{P_i^{1+\epsilon}}.
 \tag{12}
\]
This includes its triangular zero when \(a+i\ge N\), so proves
the first equality in (10) at every node. Both sides have band
\([-N+1,0]\); equality at the \(N\) nodes proves the Laurent
identity. For the second equality, the unweighted band in \(Y\)
is \([-N+1,N-1]\). Multiplication by \(d_N(Y)\) at type
four introduces only the possible additional frequency \(+N\).
The factor \(1+Y^{-N}\) is exactly its root-average correction.
This proves the normalization \(N\) and both equalities. \(\square\)

Consequently, for \(m\ge2\), (2) equals
\[
\begin{split}
 \mathcal Z_N={}&\kappa^{m+k_4}N^{m+k_4-1}
 \oint \mathcal U_{\epsilon_1,N}(w_L,X_1)
       \prod_{j=2}^{m-1}C_{\epsilon_j,N}(X_{j-1},X_j)\\
 &\qquad\cdot\mathcal V_{\epsilon_m,N}(w_R,X_{m-1})
       \prod_{j=1}^{m-1}W_{\epsilon_j,N}(X_j)
       \prod_{j=1}^{m-1}\frac{dX_j}{2\pi iX_j}.
\end{split}
 \tag{13}
\]
For \(m=2\) the conditional product is empty. Every terminal
row, its full diagonal weight, its selected Fourier alternative,
and its ordinary-color dependence have been summed in (9).
The remaining variables have the same bands and the same aliases as
before. All identities differentiate in either color. A one-vertex
word remains the separate original one-cap formula; (13) does not
apply to it.

In particular (13) has no standalone Gram factor to estimate.
It does not assert that the Gram forcing vanishes: the entire forced
transform is inside \(\mathcal V\). Taking absolute values in
(9) would discard precisely the new terminal cancellation being kept.

## 4. One concrete remaining source inequality

Here is a sufficient next estimate for (13). It is not a consequence
of the ordinary row bounds. Let \(a_*=t_{m-1}^*\),
\(\nu=\epsilon_{m-1}\), \(\epsilon=\epsilon_m\), and let
\(P_\epsilon(a)\) be the original optimized terminal action in
the [terminal supporting-plane theorem](research_terminal_supporting_plane.md).
This action includes the full terminal diagonal weight, but not the
neighbor's allocated halfweight. Put
\[
 \Pi_{\epsilon,\nu}(a)=P_\epsilon(a)-\frac\nu2 g(a).
 \tag{14}
\]
For \(a=y+i\Im a_*\), \(y\in P\), seek the finite bound
\[
\begin{split}
 \frac1N\log\left(
  |\mathcal V_{\epsilon,N}(w_R,e^{-2\pi ia})|
  |d_N(e^{-2\pi ia})|^{\nu/2}\right)
 \le{}&\Re\Pi_{\epsilon,\nu}(a_*)
  +\Re\Pi'_{\epsilon,\nu}(a_*)(y-\Re a_*)\\
 &-\kappa_*(y-\Re a_*)^2+\tau+O(\log N/N).
\end{split}
 \tag{15}
\]
Its requested scope is a fixed ordinary-color neighborhood and a
zero-safe complex thickening, uniformly on the actual reference
families. The halfweight is only a modulus allocation; a holomorphic
formulation squares the displayed product. No holomorphic square root
of a finite Fourier polynomial is required.

To see concretely what (15) would settle, assume the ordinary excesses
vanish and take the first-collar prefix through \(h=m-1\),
\(m\ge4\), with the target and selection conditions of the two
prefix theorems. Its cut has exactly the other neighbor halfweight.
At the reference, the two actions add to the full open action and
\[
       P_{m-1,b}+\Pi'_{\epsilon,\nu}(a_*)=0.
 \tag{16}
\]
Thus (15) and the prefix estimate cancel their last tangent and give
a strict first-collar bound for (13) on the entire independent
unselected plateau suffix, with the displayed quadratic losses and
one total source tolerance. There is no terminal-coordinate condition:
that coordinate was summed exactly in (10). For example a total
tolerance less than \(1/250\) leaves the common loss \(1/50\).
There is no fixed per-edge loss proportional to word length.

The existing concavity of \(P_\epsilon\) controls its phase on
admitted horizontal input slices. It does not prove (15) for the whole
finite polynomial \(\mathcal V\), and neither does the local
terminal Gaussian packet. In the original chart, the terminal lower
half with a moving neighboring plateau target is one concrete sector
not supplied by the ordinary row theorem. The exact seam itself is
not an additional obstruction: the literal factors at terminal angle
zero and one coincide, and the existing right-sector result includes
angle one on its admitted neighboring domain. Formula (15) instead
asks for the cancellation of the complete terminal coordinate.

This deduction supplies an exact boundary source and a sufficient
calibrated estimate. It proves no sign for (15), no global ordinary
closure asymptotic, and no stability theorem for arbitrary short
partial fillings.

## 5. A physical cap profile and a limitation of its triangle bound

The constants \(b_0=.808,b_1=.866\) in the
[refined cap source bound](research_mixed_cap_seam_source_bounds.md)
apply at outgoing \(X=1\) and a small fixed outgoing collar.
They do not bound \(\mathcal U_{\epsilon,N}(w,r^i)\) uniformly
over all physical outgoing indices in (9). Ordinary-color uniformity
near \(-2\) does not enlarge that outgoing domain.

A legitimate global physical-index profile follows instead from
the coherent endpoint coefficient. Write \(S(e)=F(e,u_c(e))\),
\(\lambda(e)=\Re S(e)\), and \(h(e)=J(e)+\lambda(e)\) on
the real period. The
[whole-circle endpoint bound](research_mixed_endpoint_polynomial_collar.md)
and the compact real-index packet give, with one arbitrary prescribed
tolerance, the uniform rate \(h(s)\) for
\(\mathcal H_N(w,r^{-j})\), \(s=j/N\). Indeed \(h\) extends
continuously to zero at both endpoints, where the polynomial
endpoint theorem supplies the bound; the interior is a compact
packet. The color neighborhood is chosen once for this decomposition.

At \(X=r^i\), every private row with \(i+j\ge N\) vanishes
exactly. The resulting cap profile is
\[
 \mathfrak U_\epsilon(t)
 =\max_{0\le s\le1-t}
       \{\lambda(s)+J(s+t)-J(t)-\epsilon J(s)\},
       \qquad 0\le t\le1.
 \tag{17}
\]
The endpoints have their continuous values. Uniform sine-product
upper estimates and the exact support prove
\[
 |\mathcal U_{\epsilon,N}(w,r^i)|
 \le C_\eta N^{A_\eta}
       \exp N\{\mathfrak U_\epsilon(i/N)+\eta\}.
 \tag{18}
\]
Both parities and fixed ordinary derivatives are retained. This
uses the coherent inner endpoint function, but takes a triangle
bound over the private cap index.

For \(a=x+ih\) define the zero-safe full product rate
\[
 I_a(t)=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv .
 \tag{19}
\]
Every row of (9), including revived rows at complex \(a\), is
then bounded by the one-dimensional profile
\[
 \mathfrak A_\epsilon(a)
 =\max_{0\le t\le1}
   \{\mathfrak U_\epsilon(t)+I_a(t)
                -(1+\epsilon)J(t)-2\pi ht\}.
 \tag{20}
\]
Thus (20), plus the original neighboring Fourier halfweight,
is a valid triangle upper rate for \(\mathcal V\). It is not a
sharp enough baseline comparison for all terminal types.

**Proposition 2.** At every actual terminal type-four reference
with \(m\ge2\), (20) satisfies
\[
       \mathfrak A_1(a_*)>
                \Re P_1(a_*)+\frac{\pi}{20000}.
 \tag{21}
\]
This is a failure of this positive majorant to establish (15),
not a lower bound for the coherent polynomial \(\mathcal V\).

*Proof.* Eliminate only the standalone endpoint auxiliary
\(u=u_c(e)\) in the original terminal action, leaving
\[
\begin{split}
 Z_\epsilon(a,e,t)={}&
 S(e)+g(t+a)+g(t+e)-(2+\epsilon)g(t)+2\pi iat\\
 &-g(a)-(1+\epsilon)g(e)+J(e).
\end{split}
 \tag{22}
\]
At the original endpoint solution,
\(Z_e=Z_t=0\) and \(Z_\epsilon(a_*,e_*,t_*)=P_\epsilon(a_*)\).
Hold \(a=a_*\) fixed and flatten both remaining imaginary parts:
\[
 e(v)=\Re e_*+i(1-v)\Im e_*,
 \qquad t(v)=\Re t_*+i(1-v)\Im t_*,
 \quad 0\le v\le1.
 \tag{23}
\]
The [actual endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
put a type-four \(e_*\) in
\((.333,.363)+i(-.051,-.019)\) and \(t_*\) in
\((.246,.350)+i(-.108,-.020)\). Therefore the whole
\(e\)-segment is in
\(E_{\rm cap}=[.27,.49]+i[-.055,.04]\), and the whole
\(t\)-segment and \(a_*\) are in
\(Q=[.23,.45]+i[-.12,.12]\).

The endpoint branch along (23) is not inferred from the terminal
map at \(a_*\). The
[full endpoint-rectangle packet](research_mixed_endpoint_cap_rectangle.md)
constructs the original standalone \(u_c(e)\) throughout
\(E_{\rm cap}\). The explicit Schur calculation in
[cap contour Lemma 1](research_mixed_cap_outer_contour_reduction.md#3-curvature-and-the-lower-real-half)
then gives \(-\Re S''(e)>0\) on this entire segment.
All its inequalities use the original \(F_u=0\) branch.

Up to a purely imaginary quadratic polynomial with real coefficients,
(22) equals
\[
 S(e)+W(e,t)+V(t,a)-\epsilon[J(e)+J(t)],
 \quad W(e,t)=J(e+t)-J(t),\quad
 V(t,a)=J(t+a)-J(t)-J(a).
 \tag{24}
\]
On (23), \(1/2<\Re(e+t)<1\). The exact estimates (5) and
(10) of the [open Hessian proof](research_mixed_open_word_hessian.md)
give \(-\Re W''\ge(\pi/8)\,dt^2\) and
\(-\Re V''\ge(\pi/8)(dt^2+da^2)\).
The extra type-four diagonal terms are positive. Consequently
\[
 -\Re Z_{1,(e,t)(e,t)}''\ge(\pi/4)\,dt^2 .
 \tag{25}
\]
For \(f(v)=\Re Z_1(a_*,e(v),t(v))\), original stationarity
gives \(f'(0)=0\), and (25) gives
\(f''(v)\ge(\pi/4)(\Im t_*)^2\). Hence
\[
 f(1)-f(0)\ge\frac\pi8(\Im t_*)^2>\frac{\pi}{20000}.
 \tag{26}
\]
Put \(s=\Re e_*\), \(t=\Re t_*\). They obey \(s+t<1\),
so are an admissible trial in (17)--(20). On this trial
\(\Re[g(a_*+t)-g(a_*)]=I_{a_*}(t)\); all arguments
remain in the original regular strip. Substitution shows that its
rate is exactly \(f(1)\). Thus
\(\mathfrak A_1(a_*)\ge f(1)\), proving (21).
\(\square\)

Adding the usual Fourier halfweight majorant cannot remove this
excess: its rate is at least
\(-(\nu/2)\Re g(a_*)\), the value included in (14).
This explains why the seam constants cannot simply be replaced by
the positive profile (17) to finish (15).

A more precise route remains concrete. If a coherent physical cap
upper profile \(u_\epsilon(t)\), with uniform fixed-color scope,
is established on \(0\le t\le1\), then an outer triangle bound
alone would prove (15) provided
\[
\begin{split}
 &\max_{0\le t\le1}
  \{u_\epsilon(t)+I_a(t)-(1+\epsilon)J(t)-2\pi ht\}\\
 &\quad+\frac{\nu}{2}
       \max\{-\Re g(a),\,2\pi\max(h,0)\}\\
 &\le
 \Re\Pi_{\epsilon,\nu}(a_*)+
 \Re\Pi'_{\epsilon,\nu}(a_*)(y-\Re a_*)
                  -\kappa_*(y-\Re a_*)^2 .
\end{split}
 \tag{27}
\]
The displayed Fourier maximum is the
[original absolute continuation bound](research_mixed_fourier_weight_continuation.md#5-a-criterion-for-relative-exponential-accuracy);
it is not replaced by its relative branch outside the proved domain.
Equation (27) retains a one-dimensional outer optimization and the
actual boundary tangent. Proposition 2 excludes only the substitution
\(u_\epsilon=\mathfrak U_\epsilon\) as a universal baseline proof
for type four. A sharper coherent \(u_\epsilon\), or cancellation
within (9) itself, remains a distinct source estimate.
