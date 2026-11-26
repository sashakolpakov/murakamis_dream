# Main-meridian colors, exact typed turns, and the limitation of the present geometric cells

Private working note, 31 October 2026.

The finite-dimensional source can be varied in the main meridian without making a turn singular. The distinction is between the vector-space turn, which is regular, and presenting every coupon in a single moving Casimir algebra, which is incompatible with dual colors. This note gives the turn, its first variation, and a bound uniform in the level on a fixed microscopic color disk. It also identifies why the existing geometric Conway cells cannot acquire a nonparabolic main meridian simply by changing their parameter values.

The geometric normal period already constructed from the actual braid coefficients is an inherited input. No conclusion here identifies its remaining framing period with the full finite sum or proves a new asymptotic volume formula.

## 1. The two strand colors and their exact duality

Fix \(N\ge2\), and put
\[
d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad \rho=q-q^{-1}.
\]
Use the actual nilpotent basis
\[
Kv_a=xQ^{-a}v_a,\qquad Fv_a=v_{a+1},\qquad
Ev_a=e_a(x)v_{a-1},\qquad
e_a(x)=[a]\frac{xq^{1-a}-x^{-1}q^{a-1}}{\rho}.
\tag{1}
\]
The endpoint expressions vanish. The coproduct and antipode are
\[
\begin{aligned}
\Delta E&=E\otimes K+1\otimes E,&
\Delta F&=F\otimes1+K^{-1}\otimes F,\\
S(E)&=-EK^{-1},&S(F)&=-KF,&S(K)&=K^{-1}.
\end{aligned}
\tag{2}
\]
These are the conventions of [the intrinsic cut calculation](/Users/sasha/volume-conjecture/notes/intrinsic_cut_and_meridian_atlas.md).

Write \(M=e^u=q^s\). The paired highest weights \(d+s,d-s\) have roots
\[
x_+=-q^{-1}M,\qquad x_-=-q^{-1}M^{-1},
\qquad x_-=x_+^{-1}Q^{-1}.
\tag{3}
\]
An orientation reversal replaces \(V_+\) by \(V_-\). At \(M=1\) the two become the same complete-color module. All formal statements first fix \(N\); uniform statements will explicitly use a bounded microscopic displacement \(s\).

Let \(\varphi_a\) be the dual basis of \(V_x^*\) and \(y=x^{-1}Q^{-1}\). An explicit module isomorphism is
\[
J_x:V_y\longrightarrow V_x^*,\qquad
J_xw_a=c_a(x)\varphi_{d-a},\qquad
c_a(x)=(-x)^aQ^{a(a+1)/2}.
\tag{4}
\]
It is invertible for every \(x\ne0\), including ordinary-color resonances. Indeed, the dual action is
\[
K\varphi_a=x^{-1}Q^a\varphi_a,\quad
F\varphi_a=-xQ^{-a}\varphi_{a-1},\quad
E\varphi_a=-x^{-1}Q^{a+1}e_{a+1}(x)\varphi_{a+1}.
\tag{5}
\]
The \(K\) equation uses \(Q^d=Q^{-1}\); the \(F\) equation is precisely \(c_{a+1}=-xQ^{a+1}c_a\). The \(E\) equation then follows from the direct identity \(e_a(y)=e_{N-a}(x)\). No division by a vanishing matrix coefficient or eigenvalue difference occurs. In particular
\[
c_a(x_+(u))=c_a(x_+(0))e^{au}.
\tag{6}
\]

## 2. A regular typed turn, its bound, and its first variation

Write an arbitrary map \(A:V_x\otimes V_x\to V_x\otimes V_x\) as
\[
A(v_k\otimes v_l)=\sum_{i,j}A^{ij}_{kl}v_i\otimes v_j.
\]
Bending the first output down and the second input up gives
\[
\mathcal T(A):V_x^*\otimes V_x\longrightarrow V_x\otimes V_x^*,
\qquad
\mathcal T(A)(\varphi_i\otimes v_k)
=\sum_{j,l}A^{ij}_{kl}v_j\otimes\varphi_l.
\tag{7}
\]
To verify (7), insert \(\sum_l v_l\otimes\varphi_l\), apply \(A\) to the middle two factors, and evaluate the first two. These are actual duality morphisms, so intertwiners map to intertwiners. Using (4) on both dual factors gives the exact formula in nilpotent-module bases:
\[
\boxed{\quad
\mathcal T_x(A)^{\,jb}_{ak}
=\frac{c_a(x)}{c_b(x)}A^{\,d-a,j}_{k,d-b}.
\quad}
\tag{8}
\]
The domain is \(V_y\otimes V_x\), and the target is \(V_x\otimes V_y\). This is a typed Hom map, not an endomorphism of the equal-color tensor product.

For the Euclidean matrix-entry norm, equivalently Hilbert--Schmidt norm,
\[
e^{-\pi R}\|A\|_{\mathrm{HS}}
\le\|\mathcal T_{x_+}(A)\|_{\mathrm{HS}}
\le e^{\pi R}\|A\|_{\mathrm{HS}},
\qquad |s|\le R,\quad M=q^s.
\tag{9}
\]
The entry rearrangement is a permutation, and
\[
\left|\frac{c_a(x_+)}{c_b(x_+)}\right|
=|M|^{a-b}
=\exp\left(-\frac{\pi\operatorname{Im}s}{N}(a-b)\right).
\]
Since \(|a-b|\le N-1\), (9) follows, uniformly through \(s=1\).

There is an exact first-variation identity. If \(B(u)=\mathcal T_{x_+(u)}(A(u))\), then
\[
\dot B^{\,jb}_{ak}
=\mathcal T_{x_+(0)}(\dot A)^{\,jb}_{ak}
+(a-b)B(0)^{\,jb}_{ak}.
\tag{10}
\]
The second term is \(BD_{\mathrm{in}}-D_{\mathrm{out}}B\), where the two diagonal operators record \(a,b\). With respect to \(s\), its coefficient is \(\pi i(a-b)/N\), of modulus at most \(\pi\).

This controls the turn in physical matrix coordinates. It is not a bound in a spectral polynomial norm. A change from these coordinates to a Casimir interpolation basis can be badly conditioned, and products of matrices can still have exponentially large norm. Left bends and full rotations must retain their actual pivotal maps. No untyped scalar-algebra automorphism is asserted.

## 3. The constant opposite-color Casimir order and its actual cut

For roots \(x_1,x_2\), define
\[
\Omega=\rho^2F_{\mathrm{tot}}E_{\mathrm{tot}}
       +qK_{\mathrm{tot}}+q^{-1}K_{\mathrm{tot}}^{-1}.
\]
The exact two-color identity from the intrinsic cut calculation is
\[
\begin{aligned}
P_{x_1,x_2}(z)
&=\prod_{j=0}^{N-1}(z-c_j)
=T_N(z)+(x_1x_2)^N+(x_1x_2)^{-N},\\
c_j&=qx_1x_2Q^{-j}+q^{-1}(x_1x_2)^{-1}Q^j,
\qquad P_{x_1,x_2}(\Omega)=0,
\end{aligned}
\tag{11}
\]
where \(T_0=2,T_1=z,T_{r+1}=zT_r-T_{r-1}\). It is a polynomial matrix identity, so it holds on the resonant locus as well as at distinct eigenvalues.

For equal colors it becomes
\[
P_{\mathrm{same}}(z;M)=T_N(z)+M^{2N}+M^{-2N},
\qquad
c_j(M)=q^{-2j-1}M^2+q^{2j+1}M^{-2}.
\tag{12}
\]
This is the moving-node family of [the meridian Casimir source](/Users/sasha/volume-conjecture/notes/meridian_casimir_source.md). For the dual pair, \(x_+x_-=q^{-2}\), and instead
\[
\boxed{\quad P_{\mathrm{opp}}(z)=T_N(z)+2,\qquad
c_j=q^{-2j-1}+q^{2j+1}.\quad}
\tag{13}
\]
The nodes are constant.

Put \(R_0=\mathbb C[[u]]\), \(x=x_+(u)\), \(y=x_-(u)\). The actual partial pivotal trace, using \(g_y=K_y^{1-N}\), satisfies
\[
\operatorname{ptr}_{g_y}\Omega^r=0\ (0\le r<N-1),\qquad
\operatorname{ptr}_{g_y}\Omega^{N-1}=s_x I,
\tag{14}
\]
where
\[
s_x=(-1)^{N+1}NM^{1-N}\sum_{j=0}^{N-1}M^{2j}
=(-1)^{N+1}N\frac{\sinh Nu}{\sinh u},
\qquad s_x(0)=(-1)^{N+1}N^2.
\tag{15}
\]
Thus \(s_x\) is a unit. If a polynomial of degree \(r<N\) annihilated \(\Omega\), multiply it by \(z^{N-1-r}\) and apply (14). Its leading coefficient would vanish. The minimal polynomial is exactly (13).

In fact the entire opposite-color centralizer near completeness is
\[
\boxed{\quad
\operatorname{End}_{E,F,K;R_0}(V_x\otimes V_y)
=R_0[\Omega]\simeq R_0[z]/(T_N(z)+2).
\quad}
\tag{16}
\]
To prove this including its lattice, the special complete centralizer has dimension \(N\), by the base-change theorem in [integral projective cut duality](/Users/sasha/volume-conjecture/notes/integral_projective_cut_duality.md). The generic kernel dimension of the finite intertwining system cannot exceed this. Equation (14) gives \(N\) independent Casimir powers, so the generic dimension is exactly \(N\).

Their actual cut pairing has determinant
\[
\det\bigl(\operatorname{ptr}_{g_y}\Omega^{i+j}\bigr)_{0\le i,j<N}
=(-1)^{N(N-1)/2}s_x^N\in R_0^\times.
\tag{17}
\]
Entries before the anti-diagonal vanish, and anti-diagonal entries equal \(s_x\); reversing columns proves the determinant formula. An integral intertwiner lies in the fraction-field span of the powers. Its pairing with every power is integral, and (17) forces its coefficients to be integral. This proves (16) and base change.

Each repeated root of \(T_N+2\) therefore retains a nonzero nilpotent part: there is a size-two Jordan block at every repeated node. For odd \(N\), \(-2\) is the sole simple root. In contrast, (12) is generically separable over \(\mathbb C((u))\). The two generic algebras are not isomorphic as algebras. The typed linear turn (8) never asserts such an isomorphism.

The full modified cut has an especially simple form. With the prescribed phase
\[
d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},
\qquad \eta_N=i^{N+3},\qquad
c_N=Nq^{N(1-N)/2},
\]
one has
\[
d_N(M)s_x=c_N,\qquad
d_N(M)\operatorname{ptr}_{g_y}f(\Omega)
=c_N[z^{N-1}]\bigl(f\bmod(T_N+2)\bigr)I.
\tag{18}
\]
Thus the algebra and the full cut are constant; the actual coupon coefficients can still vary with \(M\). Equation (18) does not determine those coefficients or the invariant.

A formal neighborhood is not a uniform disk. The coefficient \(s_x\) vanishes at \(M=q^k\), \(1\le k<N\), whereas \(d_N(M)\) has a pole there. These points approach \(1\) as \(N\) grows. The perfect pairing is a statement over \(R_0\) for each \(N\), not a bounded inverse on a fixed complex \(M\)-disk. The physical turn (8) has no such singularity.

### An explicit polynomial coordinate map for the typed turn

There is also an exact finite coordinate map; its large-\(N\) bound is a separate problem. Let \(\check R_{y,x}:V_y\otimes V_x\to V_x\otimes V_y\) be the actual mixed checked braiding, with its original normalization retained. For \(f\) in the same-color Casimir order, put
\[
G_f=\check R_{y,x}^{-1}\mathcal T_x(f(\Omega_{x,x})).
\tag{18a}
\]
This is an endomorphism of \(V_y\otimes V_x\). By (16) it has a unique expression \(G_f=g_f(\Omega_{y,x})\), with \(\deg g_f<N\).

Its coefficients are explicit partial traces. Write \(P(z)=T_N(z)+2=\sum_{r=0}^N p_rz^r\), \(p_N=1\), and define
\[
q_j(z)=\sum_{r=j+1}^N p_rz^{r-j-1},\qquad 0\le j<N.
\]
For the functional \(\ell(a)=[z^{N-1}](a\bmod P)\), one has
\(\ell(z^i q_j)=\delta_{ij}\) for \(0\le i,j<N\). When \(i\le j\), this follows from degree and the leading coefficient. When \(i>j\), reduce
\[
z^iq_j=z^{i-j-1}\left(P-\sum_{r=0}^jp_rz^r\right);
\]
the resulting polynomial has degree at most \(i-1<N-1\). Therefore
\[
\boxed{\quad
g_f(z)=\sum_{j=0}^{N-1}
\frac{\operatorname{ptr}_{g_x}
\left(G_fq_j(\Omega_{y,x})\right)}{s_y}\,z^j.
\quad}
\tag{18b}
\]
The partial trace in (18b) is its scalar value on \(V_y\). Since \(s_y(0)\ne0\), this formula is regular over \(R_0\). It is an \(R_0\)-linear isomorphism between the two rank-\(N\) polynomial orders: currying is an isomorphism of the intertwiner spaces, and the mixed braiding is invertible. Reconstruction is
\(\mathcal T_x(f(\Omega_{x,x}))=\check R_{y,x}g_f(\Omega_{y,x})\).
The braiding here is a retained coordinate carrier; it is not an extra crossing inserted into the original tangle.

The formula is nonlinear in the color and linear in \(f\). After stripping the explicitly known common Cartan scalar, the finite mixed-braiding entries are Laurent expressions in the two roots, so the coordinate formula is rational in \(M\) near \(1\). If the unstripped convention includes a Gaussian scalar in \(u\), it must be restored; the displayed construction with the actual \(\check R\) is holomorphic over \(R_0\) regardless of this convention. It includes all nilpotent directions and keeps the pivot in the trace. Its first derivative is obtained by differentiating (18a)--(18b), including the mixed braiding, pivot and Casimir realizations, as well as the explicit term (10).

Thus an exact typed finite source adapter exists. What is not proved is that the coefficient map (18b), in the complete-source spectral norms, has a controlled large-\(N\) cost. The Hilbert--Schmidt estimate (9) alone does not bound this change of coordinates.

## 4. The exact obstruction in the existing geometric cells

In [the marked strict Conway construction](/Users/sasha/volume-conjecture/notes/actual_conway_general_mask_marked_filling.md), each leaf has white-face maps \(W_0,\ldots,W_3\), rational in two variables \(E,R\). At its main corner \(C_j\), the actual small main meridian is
\[
\mu_j=W_{j-1}^{-1}W_j
\quad\text{or its inverse}.
\tag{19}
\]
The two white maps have equal derivatives in local coordinates at the corner: \(E^{-1}\) at \(C_0,C_2\), and \(E\) at \(C_1,C_3\). Hence (19) has multiplier exactly one for every \(E,R\) in the domain. It remains nonidentity near completeness and therefore remains parabolic.

Consequently no change of the auxiliary colors, no holomorphic substitution \(E=E(u),R=R(u)\), and no simultaneous change of world frame can make these formulas realize the marked main multiplier \(M^2=e^{2u}\). A genuine extension must change the face maps or matching data. It cannot be obtained solely by changing values of the old parameters.

The marked multiplier is essential to this first-order statement. The trace squared of a meridian with eigenvalues \(e^{\pm u}\) is \(4\cosh^2u\), whose derivative at zero vanishes. A first-order unmarked trace test would miss the obstruction; the logarithmic marked multiplier has derivative \(2\).

## 5. The geometric germ that already exists, and the remaining comparison

For a fixed hyperbolic knot in the strict class, [the actual geometric normal-period calculation](/Users/sasha/volume-conjecture/notes/actual_geometric_normal_period.md) supplies a different route. It uses the original oriented braid coefficients and the positive marked gluing Jacobian. In its coordinates
\[
u=\operatorname{Log}M,\qquad U=2u,\qquad
V=2\operatorname{Log}L_{\mathrm{intr}},
\]
the unframed geometric germ is unramified over \(U\), and its cusp derivative is nonzero and nonreal. The actual coefficient critical scheme has two framing directions; its transverse Hessian is nondegenerate. Its formal normal period is nonzero and has the marked geometric connection after the specified gauge comparison.

These are inherited results, not consequences newly proved by the turn formula. One can also convert an oriented tangle into an oriented braid, preserving its exact finite contraction after retaining the actual dualities, pivot, and zero-framing correction. Equality of the finite contractions alone does not identify a selected normal stationary block under that conversion. It does not evaluate the remaining framing period or determine the coefficient of the geometric block in the complete finite sum.

Two concrete obligations remain for a Conway-based extension.

1. Express both color types, their typed turns, and the first variation (10) in coordinates with controlled large-\(N\) estimates. Equations (8)--(18) provide exact algebraic data, but no spectral-to-physical norm comparison.
2. Construct new marked white/shaded maps with main multiplier \(M^2\), or compare the typed tangle phase to the existing braid critical scheme, retaining the primitive longitude, framing directions, pivot, and absolute action constant. Equation (19) proves that mere reparametrization cannot suffice.

The new conclusions are the regular turn (8), its uniform microscopic bound (9), its exact derivative (10), and the full constant opposite-color order (16) with actual cut (18). They hold at every \(N\ge2\). They neither rule out a main-meridian extension nor select the finite quantum period from the already existing geometric normal block.

## 6. A precise geometric first-variation statement after auxiliary filling

The following calculation describes what a source comparison would have to recover. It uses the joint marked peripheral germ of the geometric representation; it does not claim that the old two-variable leaf cells already parametrize that germ. The joint germ and its parabolic slices are established in [the marked multicusp gluing theorem](/Users/sasha/volume-conjecture/notes/general_marked_multicusp_gluing_rigidity.md); the calculation here records the effect of retaining the auxiliary filling equations.

Let \(U_0,V_0\) be the centered squared-eigenvalue logs of the main meridian and preferred longitude. Write \(U_a,V_a\), \(1\le a\le r\), for the original auxiliary curves. On the joint geometric germ the primitive satisfies
\[
dG=\frac12\left(V_0\,dU_0+\sum_{a=1}^rV_a\,dU_a\right).
\tag{20}
\]
The required local existence and coordinates are supplied by the positive marked-gluing argument: choose independent edge rows and all meridian rows. They form a full-rank isotropic matrix \((A\ B)\). For positive shapes, the same polarized calculation as in the one-cusp geometric normal-period proof makes
\(A+B\operatorname{diag}((z_j-1)^{-1})\) invertible. The implicit-function theorem then gives the joint germ in the variables \(U_0,\ldots,U_r\). Three developed flags give the actual face maps, and the original fundamental chain fixes the imaginary constant in \(G\). Thus this step uses the full shape gluing model and its peripheral row identities, rather than reusing (19) with changed \(E,R\).

On its slice \(U_0=0\), the existing auxiliary construction has a nonidentity parabolic main meridian. Its commuting longitude has multiplier one too. Consequently
\[
V_0(0,U_1,\ldots,U_r)=0.
\tag{21}
\]
Closedness of (20) makes the matrix
\(\tau_{ij}=\partial V_i/\partial U_j\) symmetric. Differentiating (21) therefore gives
\[
\tau_{0a}=\tau_{a0}=0\qquad (U_0=0,\ a\ge1).
\tag{22}
\]
This is first-order isolation only. It does not assert that the main cusp shape is independent of the auxiliary filling.

Fix sufficiently long signed auxiliary slopes \(p_a\), with the primitive filling equations
\[
U_a+p_aV_a=-2\pi i.
\tag{23}
\]
The established long-filling implicit-function theorem makes their auxiliary Jacobian invertible near the filled point. Solving them as \(U_a=U_a(U_0)\), their derivative at \(U_0=0\) is
\[
(I+P\tau_{aa})U_a'(0)=-P\tau_{a0}=0,
\qquad P=\operatorname{diag}(p_1,\ldots,p_r).
\tag{24}
\]
Thus \(U_a'(0)=0\). No correction from the auxiliary response appears in the first main-cusp derivative. More generally, away from the main-parabolic slice the usual chain rule gives
\[
\frac{dV_0}{dU_0}
=\tau_{00}-\tau_{0a}(I+P\tau_{aa})^{-1}P\tau_{a0};
\]
the second term vanishes at the point considered in (24).

On the filling locus define
\[
G_p=G+\frac14\sum_a p_aV_a^2.
\tag{25}
\]
Because \(dU_a=-p_a\,dV_a\), equations (20) and (25) give exactly
\[
dG_p=\frac12V_0\,dU_0.
\tag{26}
\]
The regulator formula has the correct absolute filled normalization as well. Before filling it is
\[
\operatorname{Vol}(\rho)
=\operatorname{Im}G-\frac12\operatorname{Re}U_0\operatorname{Im}V_0
-\frac12\sum_a\operatorname{Re}U_a\operatorname{Im}V_a.
\]
Substituting \(\operatorname{Re}U_a=-p_a\operatorname{Re}V_a\) and (25) reduces this to
\[
\operatorname{Vol}(\rho)
=\operatorname{Im}G_p
-\frac12\operatorname{Re}U_0\operatorname{Im}V_0.
\tag{27}
\]
The primitive smooth auxiliary completions are the same ones used by the existing filling theorem. At \(U_0=0\) the main end is complete, so
\(\operatorname{Im}G_p(0)=\operatorname{Vol}(S^3\setminus K_p)\).

Let \(\tau_{K_p}\) be the marked cusp derivative of this filled knot, and write \(\widehat G_p(M)=G_p(2\operatorname{Log}M)\). Equations (21), (24), and (26) imply
\[
G_p(U_0)=G_p(0)+\frac{\tau_{K_p}}4U_0^2+O(U_0^3),
\qquad
\widehat G_p(e^u)=\widehat G_p(1)+\tau_{K_p}u^2+O(u^3),
\tag{28}
\]
where the second notation means that the primitive is expressed in \(M=e^u\), with \(U_0=2u\). The cusp derivative has positive imaginary part in the oriented complete convention.

The finite reduced state has the already established Weyl symmetry \(F_N(M)=F_N(M^{-1})\), so its first \(u\)-derivative at \(M=1\) vanishes too. This agreement of first derivatives is exact but does not compare the nontrivial quadratic coefficient in (28) with a derivative of the full finite source. In particular neither the typed turn nor the formal normal block proves a limit for that derivative or for the regular microscopic profile.

