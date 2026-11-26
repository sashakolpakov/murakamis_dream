# The physical Ward kernel: Christoffel–Darboux action and full normals

Private written proof, 17 November 2026.

The finite Christoffel kernel in the positive Ward remainder has a
factorization with a positive second-kind correction. This determines
its exponential action uniformly over the whole physical input
interval, including the endpoint approaching \(2\). The Ward-to-
canonical unit has the difference of two calibrated complete-edge
actions. Original normal rows have polynomial relative upper bounds.
A reverse-parameter orthogonality identity supplies a stronger real
normal structure. No lower bound after arbitrary composition follows.

## 1. Pinned source, domains and normalization

Use \(N\ge2\), \(D=N-1\), \(m=\lfloor N/2\rfloor\), \(d=m-1\),
\(\theta=\pi/N\), \(\eta=(-1)^D\), and
\[
 c_j=2\cos((2j+1)\theta),\quad
 P_N(C)=2T_N(C/2)+2,\quad
 \Omega=\mathbb C\setminus[2,\infty),\quad I_N=[-2,c_0].
 \tag{1}
\]
Let \(F_j(C)=K_N(c_j,C)\) be the original physical rows. The
double indices are \(0\le j\le d\), with
\[
 h_j=\{4\sin\theta\sin((2j+1)\theta)\}^{-1}.
 \tag{2}
\]
At odd levels the extra simple row is \(F_*=K_N(-2,\cdot)\).
The pinned positive Ward theorem supplies the positive measure
\[
 d\mu(x)=\frac{N^2\rho_N(x)}{P_N(x)}\,dx,\quad
 \rho_N(x)=\frac{N}{4\pi\sin\theta}
       \tanh\!\left(\frac N2\operatorname{arcosh}(x/2)\right),\quad x>2,
\]
\[
 \int F_jF_k\,d\mu=h_j\delta_{jk}.
 \tag{3}
\]
All double rows have degree \(j\), simple roots in \((2,\infty)\),
and are positive below \(2\). Define, for real \(c<2\),
\[
 L_c(C)=\eta\sum_{j=0}^d F_j(c)F_j(C)/h_j,\qquad
 K_c=\sum_{j=0}^d F_j(c)^2/h_j,
\]
\[
 V_c(C)=\int\frac{L_c(x)^2(x-c)}{x-C}\,d\mu(x),\qquad
 J_c(C)=\int L_c(x)\frac{x-c}{x-C}\,d\mu(x),\qquad
 U_c(C)=\eta J_c(C).
 \tag{4}
\]
Integrals are over \((2,\infty)\). The identities \(V_c=L_cJ_c\)
and \(J_C(C)=\eta\) are exact. \(J_c(C)\) is polynomial in complex
\(c\) and holomorphic in \(C\in\Omega\); \(V_c\) uses a bilinear
square under complex continuation. For real \(c<2\), \(V_c,L_c,U_c\)
are zero-free on \(\Omega\), with \(V_c>0\), \(\eta L_c>0\) and
\(U_c>0\) on the real slit complement.

The original input \(A_c=K_N(c,\cdot)\) and its specified Ward
representative satisfy, for every complex \(c\),
\[
 TA_c(C)=\frac{\eta[P_N(C)-P_N(c)]}{N^2(C-c)},\qquad
 \widehat H_{A_c}(C)=\frac{P_N(C)J_c(C)-\eta P_N(c)}{N^2(C-c)}.
 \tag{5}
\]
Both diagonal singularities are removable. Only at a physical node
\(c\) does the term \(P_N(c)\) disappear, giving
\(\widehat H_{A_c}/TA_c=U_c\). These are the original full-jet
representatives: no odd simple normal or off-grid canonical equality
is introduced.

## 2. Exact Christoffel–Darboux factorization at both parities

For \(N\ge4\), so \(d\ge1\), use the actual Jacobi coefficients
\[
 a_r=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\quad
 b_r=\frac{s_r^4}{s_{2r}s_{2r+1}},\quad
 s_r=2\sin(r\theta),\qquad b_0=0.
 \tag{6}
\]
The recurrence
\[
 CF_r=(c_0+a_r+b_r)F_r-a_rF_{r+1}-b_rF_{r-1}
 \tag{7}
\]
is used only for \(0\le r<d\), with the \(b_0F_{-1}\) term absent.
The coefficient \(b_d\) is finite
and positive. No \(a_d\), which is singular at even levels, is used.
Detailed balance is \(a_{r-1}/h_{r-1}=b_r/h_r\).

Put \(R_d(C)=F_{d-1}(C)/F_d(C)\). Then exactly
\[
 \boxed{\quad
 L_c(C)=\frac{\eta F_d(c)F_d(C)}{h_d}\,B_c(C),\qquad
 B_c(C)=1+b_d\frac{R_d(C)-R_d(c)}{C-c}.
 \quad}
 \tag{8}
\]
The quotient is interpreted by its derivative at \(C=c\).
Indeed subtract (7) at \(C,c\), multiply by the opposite row and
sum with weights \(h_r^{-1}\) through \(r=d-1\). The interior terms
cancel by balance, leaving
\[
 (C-c)\sum_{r<d}\frac{F_r(C)F_r(c)}{h_r}
 =\frac{a_{d-1}}{h_{d-1}}F_d(C)F_d(c)
                         [R_d(C)-R_d(c)].
\]
Add the \(d\)-th term and use balance once more to obtain (8).

Let \(\mathcal J_d\) be the original symmetric \(d\)-row Jacobi
matrix. Its determinant is
\(\det(\mathcal J_d-CI)=(\prod_{r<d}a_r)F_d(C)\), so its spectrum
lies in \((2,\infty)\). Its last cofactor
gives
\[
 R_d(C)=a_{d-1}\langle e_{d-1},(\mathcal J_d-C)^{-1}e_{d-1}\rangle
       =\int\frac{d\sigma_d(x)}{x-C},\qquad
 \sigma_d>0,\quad \sigma_d((2,\infty))=a_{d-1}.
 \tag{9}
\]
Consequently
\[
 B_c(C)=1+b_d\int\frac{d\sigma_d(x)}{(x-c)(x-C)}.
 \tag{10}
\]
For every real \(c<2\), this is one plus a positive Cauchy transform.
In particular it is zero-free on \(\Omega\), positive below \(2\),
and has its principal logarithm there.

Fix \(K\Subset\Omega\). Uniformly in \(c\in I_N\), \(C\in K\),
\[
                  a_K\le |B_c(C)|\le b_K N^6.
 \tag{11}
\]
To see the upper bound, (6) gives \(a_{d-1},b_d\le N^2\), since
every nonzero \(s_r\ge4/N\). Also
\(x-c\ge2-c_0\ge4/N^2\), and \(x-C\) stays a fixed distance from
zero. For the lower bound, rotate by
\(\exp(i\arg(2-C)/2)\). The constant \(1\) and every integrand in
(10) lie in the same sector of width \(|\arg(2-C)|<\pi\);
their rotated real parts dominate their moduli by a positive
constant uniform on \(K\). This also shows
\[
 |\partial_c B_c(C)|/|B_c(C)|\le C_K/(2-c).
 \tag{12}
\]
Indeed an additional derivative only inserts another factor
\((x-c)^{-1}\), and the same cone estimate controls the absolute
integral by \(|B_c|\).

At the real diagonal,
\[
 K_c=\frac{F_d(c)^2}{h_d}[1+b_dR_d'(c)],\qquad
               1\le1+b_dR_d'(c)\le C N^8,\quad c\in I_N.
 \tag{13}
\]
Moreover \(h_d\) is bounded above and below by constant multiples
of \(N^2\). These statements also follow directly from (6),(9).
For \(N=2,3\), \(d=0\): \(L_c=\eta/h_0\), \(K_c=1/h_0\).
Those finite exceptional levels require no Jacobi quotient.

## 3. Uniform calibrated action, including \(c\to2\)

Use the original profile
\[
 \Psi_x(C)=\int_0^x
  2\operatorname{arsinh}\!\left(\frac{\sqrt{2-C}}2\cot(\pi s)\right)ds,
 \qquad \Psi(C)=\Psi_{1/2}(C).
 \tag{14}
\]
The square root has positive real part and the inverse hyperbolic
sine is principal. The logarithms below are normalized to be real
on \(C<2\). The pinned all-row theorem proves
\(\log F_j(C)=N\Psi_{j/N}(C)+o(N)\) uniformly on compact slit sets,
and with error \(O(\log N)\) on compact subsets of \(\Re C<2\).
It includes both endpoint rows and fixed output derivatives.

**Theorem 1.** Uniformly for \(c\in I_N\) and \(C\in K\Subset\Omega\),
\[
 \begin{split}
 \log K_c&=2N\Psi(c)+O(\log N),\\
 \Log(\eta L_c(C))&=N[\Psi(c)+\Psi(C)]+o_K(N),\\
 \Log U_c(C)&=N[\Psi(c)-\Psi(C)]+o_K(N).
 \end{split}
 \tag{15}
\]
For \(K\Subset\{\Re C<2\}\), both \(o_K(N)\) errors are
\(O_K(\log N)\). The output-logarithm errors have the same estimates
after every fixed number of \(C\)-derivatives on smaller compact sets.

**Proof.** First determine the real input factor without applying
a fixed half-plane margin at \(c_0\to2\). The last double node is
\(c_d=-2+O(N^{-2})\). Exact symmetry gives, for every physical
index \(l\), including the odd simple row,
\[
 F_d(c_l)=F_l(c_d),\qquad
 \log F_d(c_l)=N\Psi_{l/N}(-2)+O(\log N).
 \tag{16}
\]
Here the all-row theorem is applied on a fixed negative compact;
changing \(c_d\) to \(-2\) costs only \(O(N^{-1})\), uniformly in \(l\).

The precise classical normalization in (16) is
\[
 \Psi_x(-2)=\Psi(2\cos(2\pi x)),\qquad 0\le x\le1/2.
 \tag{17}
\]
For an explicit verification put \(a=\sin(\pi x)\), \(0<x<1/2\).
The derivative with respect to \(a\) of the right side of (17) is
\[
 \frac2\pi\int_0^1\frac{dy}{\sqrt{a^2+(1-a^2)y^2}}
 =\frac{2}{\pi\sqrt{1-a^2}}
       \operatorname{arsinh}\!\left(\frac{\sqrt{1-a^2}}a\right).
\]
Multiplication by \(da/dx=\pi\cos(\pi x)\) gives
\(2\operatorname{arsinh}(\cot(\pi x))=2\log\cot(\pi x/2)\).
This is also the derivative of the left side, directly from (14).
Both sides tend to zero at \(x=0\); continuity gives both endpoints.
Thus
\[
 \partial_x\Psi_x(-2)=2\log\cot(\pi x/2).
 \tag{18}
\]
An interval of length \(1/N\) therefore changes \(N\Psi_x(-2)\)
by at most \(O(\log N)\), including at \(x=0\). The centered
physical point \(c_l=2\cos(2\pi(l+1/2)/N)\) differs by just this
half-step from (17). Thus (16) gives
\[
                  \log F_d(c_l)=N\Psi(c_l)+O(\log N).
 \tag{19}
\]
For every real \(c\in I_N\), bracket \(c\) between successive
physical nodes. Both \(F_d(c)>0\) and \(\Psi(c)\) decrease with \(c\):
the former follows from its cut roots, and the latter from (14).
The adjacent phase changes are controlled by (18).
At even levels add the lower endpoint \(-2\) as an anchor;
its estimate follows directly from the all-row theorem at \(-2\).
This proves (19) uniformly on the entire interval \(I_N\).

The \(d\)-th row profile at the output gives
\[
 \Log F_d(C)=N\Psi(C)+o_K(N),
 \tag{20}
\]
with the stronger half-plane remainder. Replacing \(d/N\) by
\(1/2\) costs \(O_K(N^{-1})\), since the integrand in (14)
vanishes linearly there. Equations (8),(11) and (13) now prove
the first two statements in (15): \(\Log B_c=O_K(\log N)\),
including its bounded principal argument.

The proof of the preceding positive-remainder theorem in fact gives,
for all real \(c\in I_N\), not only the physical nodes,
\[
 a_K(2-c)\le |V_c(C)|/K_c\le b_K.
 \tag{21}
\]
It uses the same positive-cone estimate on the integral in (4).
As \(2-c\ge4/N^2\), the principal logarithm of \(V_c/K_c\)
is \(O_K(\log N)\); its imaginary part is bounded by \(\pi\).
Since \(U_c=V_c/(\eta L_c)\), the third statement follows.
Use the same estimates on a slightly larger compact set and
Cauchy's formula for the derivative assertion. \(\square\)

On the calibrated angular branch \(C=-2\cos t\),
\(\Psi(C)=\psi(t,0)\), including the original complete constant.
Thus (15) is a difference of complete-end source actions for \(U\),
not the two-free-color edge action \(\psi(t,u)\). For nonphysical
input \(c\), (5) still retains its separate \(P_N(c)\) term.

## 4. Full original normal rows on a complex output compact

**Theorem 2.** For \(C\in K\Subset\Omega\), \(c\in I_N\),
\[
 \left|\frac{\partial_cU_c(C)}{U_c(C)}\right|\le C_KN^5.
 \tag{22}
\]
For each physical double node \(c=c_j\), the exact original normal
representative consequently has the division-free bound
\[
 \widehat H_{G_j}(C)=
 \frac{\eta}{N^2}\frac{P_N(C)}{(C-c_j)^2}
       [U_{c_j}(C)+(C-c_j)\partial_cU_c(C)|_{c_j}],
\]
\[
 |\widehat H_{G_j}(C)|
 \le C_KN^5\,\left|\frac{P_N(C)}{N^2(C-c_j)^2}\right|
                     |U_{c_j}(C)|.
 \tag{23}
\]
The polynomial quotient in (23) includes its removable value at
\(C=c_j\); no division by a vanishing canonical row is required.

**Proof.** Write \(g=2-c\). The cut roots of the rows give
\[
 |F_j'(c)|\le jF_j(c)/g,\qquad
 \|\partial_cL_c\|_{L^2(\mu)}\le d\sqrt{K_c}/g.
 \tag{24}
\]
Differentiating the convergent integral for \(V_c\) in (4), and
using Cauchy–Schwarz and the bounded ratios
\((x-c)/(x-C)\), yields
\[
 |\partial_cV_c(C)|\le C_KK_c(1+d/g).
 \tag{25}
\]
Together with (21), this gives
\(|\partial_cV_c/V_c|\le C_K(g^{-1}+dg^{-2})\).
The factorization (8) and (12) give
\[
 |\partial_cL_c/L_c|
       \le d/g+C_K/g.
 \tag{26}
\]
Since \(g\ge4/N^2\), subtraction of these logarithmic derivatives
proves (22). At \(N=2,3\), \(L_c\) is constant and the same integral
argument gives the assertion.

Finally differentiate the exact full-source formula (5).
At a double \(c_j\), both \(P_N(c_j)\) and \(P_N'(c_j)\) vanish.
This gives the equality in (23), while
\(TG_j=\eta P_N/[N^2(C-c_j)^2]\). Boundedness of \(C-c_j\)
and (22) prove its inequality. All output values and first normals
are retained by the pinned Ward representative. There is no
\(G_*\) at the odd simple node. \(\square\)

There is no general lower bound here for
\(U_c+(C-c)\partial_cU_c\). Fixed output derivatives can be retained
by applying these holomorphic estimates on buffered output domains;
this does not remove cancellation in that bracket.

## 5. Reverse-parameter orthogonality and real normal structure

Fix a real output \(C<2\). Then \(c\mapsto J_c(C)\) has degree
exactly \(m\) and is orthogonal to every polynomial \(p(c)\) of
degree at most \(m-1\) for the positive measure
\[
                         d\tau_C(c)=\frac{d\mu(c)}{c-C}.
 \tag{27}
\]
Indeed, let \(S_j(C)=\int F_j(x)/(x-C)\,d\mu(x)\) and
\(H_c(C)=\int L_c(x)/(x-C)\,d\mu(x)\). The identity
\[
 J_c(C)=\eta+(C-c)H_c(C),\qquad
 H_c(C)=\eta\sum_{j=0}^d F_j(c)S_j(C)/h_j
 \tag{28}
\]
and orthogonal expansion of \(p\) give
\[
 \int J_c(C)\frac{p(c)}{c-C}\,d\mu(c)
 =\eta\int\frac{p(c)}{c-C}\,d\mu(c)
                      -\int H_c(C)p(c)\,d\mu(c)=0.
 \tag{29}
\]
All exchanges are finite polynomial expansions. The measure
\(\tau_C\) has tail \(x^{-N-1}\), so its moments through degree
\(N-1\) are finite; the largest degree in (29) is \(2m-1\).
The leading coefficient of \(J\) is
\(-\eta\,\mathrm{lc}(F_d)S_d(C)/h_d\ne0\). For this nonvanishing,
orthogonality applied to
\((F_d(x)-F_d(C))/(x-C)\) gives
\[
 F_d(C)S_d(C)=\int F_d(x)^2/(x-C)\,d\mu(x)>0.
 \tag{30}
\]
This includes \(d=0\). The elementary sign-change argument applied
to (29) proves that all \(m\) roots \(r_\nu(C)\) are simple and
lie in \((2,\infty)\). Normalization \(J_C(C)=\eta\) now gives
\[
 U_c(C)=\prod_{\nu=1}^{m}\frac{r_\nu(C)-c}{r_\nu(C)-C},\qquad
 \partial_c\log U_c(C)=-\sum_{\nu=1}^m\frac1{r_\nu(C)-c}
                         \quad(c<2).
 \tag{31}
\]
More generally, for complex \(c\notin[2,\infty)\) and fixed
nonnegative integer \(r\),
\[
 |\partial_c^rJ_c(C)/J_c(C)|
 \le (m)_r\,\operatorname{dist}(c,[2,\infty))^{-r},
 \tag{32}
\]
where \((m)_r=m(m-1)\cdots(m-r+1)\) and the derivative is zero
for \(r>m\). This follows by differentiating the finite root product.
At physical inputs the bound is \(O(N^{3r})\).

For a double physical input \(c_j\), (23) consequently has real ratio
\[
 \frac{\widehat H_{G_j}(C)}{TG_j(C)}
 =U_{c_j}(C)
    \left[1-(C-c_j)\sum_{\nu=1}^m\frac1{r_\nu(C)-c_j}\right].
 \tag{33}
\]
This equality is interpreted by removable continuation at physical
output zeros. For real \(C\le c_j\) it is positive and at least
\(U_{c_j}(C)\); at \(C=c_j\) it equals one. For general real
\(C<2\), only the absolute upper factor
\(1+|C-c_j|m/(2-c_j)\) is inferred. The root statement in this
section requires real \(C\); it is not a complex-output positivity
claim or a composition theorem.

## 6. Scope and complete direct sources

The factorization exposes an actual source action and retains its
full normal channels. It does not make the output-dependent unit
commute with the original turn, remove the free-input \(P_N(c)\)
term in (5), or prove noncancellation under an arbitrary closing.
The earlier positive-remainder note remains unchanged.

More precisely, write \(\widehat T A=\widehat H_A\) and
\(\widehat B(c,C)=\widehat H_{K_N(c,\cdot)}(C)\). The original
Frobenius trace is \(\phi(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f\).
Newton normalization gives \(\phi(e_i e_j)=\delta_{i+j,D}\):
below degree \(D\) this is zero, at degree \(D\) use
\(S_iS_j=N\), and above degree \(D\) the product is divisible by
\(P_N\), with its repeated roots. Expanding the kernel therefore gives
\[
 \widehat T A(C)=\phi_c[\widehat B(c,C)(TA)(c)],\qquad
 \phi_c[\widehat B(c,C)A(c)]=(\widehat T\circ T)A(C).
 \tag{34}
\]
Thus \(\widehat B\) is the Frobenius kernel of Ward regularization
of the identity. The action difference in (15) is a calibrated
ratio for its physical sections, not a polynomial-cost gauge
equivalence of the original turn. The actual \(TA\) jets and the
free-color diagonal term in (5) remain in (34); no phase telescoping
through arbitrary tangle composition is asserted.

All three complete direct texts were read and their used implications
checked:

* research_physical_rows_positive_ward_remainder.md,
  SHA256 a426c1e131f6b4948cd901d7615923d97e37b654db7bd6af25fb6fd56b1365dc:
  exact source family, positive Christoffel remainder, all physical
  nodes, entire parameter formula, full normal derivative.
* research_physical_jacobi_charge_boundary.md,
  SHA256 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583:
  original finite recurrence, detailed balance, Jacobi matrix and
  determinant normalization, exact ordinary-row endpoint range.
* research_mixed_next_first_short_edge_slit_plane_bound.md,
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b:
  uniform all-row logarithmic profile and its complete source action,
  slit continuation and stronger half-plane error.

Only written mathematics, source reads and metadata hashes were used.
No programs, numerical tests, builds or frozen/public edits were made.
