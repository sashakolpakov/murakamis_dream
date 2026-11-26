# A source-sensitive polar bound for Conway correction errors

Private written proof, 23 November 2026.

The backward closing row in the normalized Conway recursion determines
a positive seminorm for each bilinear error term. This gives a
computable error disk which is never worse than the earlier local
full-norm disk. At the original cylindrical closing it removes an
exponentially large multiplication cost. Every genuine turn changes
the transported carrier explicitly; no boundary direction is removed
permanently, and no positive lower rate is inferred.

## 1. The original normalized recursion and Frobenius carriers

Fix \(N\ge2\), and use the complete normalized source of [C] and [R].
The actual Newton space is
\[
 H_N=\mathbb C[X]/(P_N),\quad P_N=2T_N(X/2)+2,\quad d=N-1,\quad
 q=e^{\pi i/N},\quad c_j=q^{2j+1}+q^{-2j-1},
\]
\[
 s_r=\prod_{a=1}^r2\sin(\pi a/N),\qquad
 e_r(X)=s_r^{-2}\prod_{j<r}(c_j-X),\qquad e_0=1.
 \tag{1}
\]
Empty products are one. Coefficient vectors have the Euclidean
Hermitian norm. With \(J e_r=e_{d-r}\), [F] gives the actual
quarter-turn and original Frobenius functional:
\[
 J=J^*=J^{-1},\qquad
 \phi(f)=f_d=(-1)^dN^2[X^d]\operatorname{rem}_{P_N}f,
 \qquad \phi(fg)=f^{\mathsf T}Jg.
 \tag{2}
\]
Thus the full values and first normals at double roots, and the odd
simple-root value, remain in this algebra. The two original closing
rows are \(\lambda_d=\phi\) and \(\lambda_0(f)=f(c_0)\).

Let \(b_v\) be the recorded normalization budget of each original
tensor. At a product the normalized map is
\(\Phi_v(u,w)=uw/b_v\); at a turn it is \(Ju/b_v\).
All normalized tensor norms are at most \(\sigma=1/16\).
Keep the original normalized closing \(L\), budget product
\(B_{\rm tot}\), and true packets \(a\):
\[
 a_v=\Phi_v((a_c)_c),\qquad
 k:=K_N/B_{\rm tot}=La_{\rm top},\qquad \|a_v\|\le\sigma.
 \tag{3}
\]
All original framing or other prescribed scalars stay in these data.
Any separately recorded exterior scalar multiplies the final disk.

For a feasible trial \(x\), set
\[
 e=a-x,\quad r_v=\Phi_v((x_c)_c)-x_v,\quad
 A=D\Phi(x),\quad z=Lx_{\rm top},\quad
 d=c(I-A)^{-1},
 \tag{4}
\]
where \(c\) is \(L\) on the top packet and zero elsewhere.
The matrix \(A\) is strictly triangular, so the displayed inverse
of \(I-A\) is a finite sum. These are the source-preserving rows of [R].
At each proper vertex define the full algebra carrier
\[
                         h_v=Jd_v^{\mathsf T}.
 \tag{5}
\]
There is no conjugation in (5): (2) gives
\(d_v(f)=\phi(h_vf)\). The backward recursion becomes
\[
 \begin{split}
 h_c&=h_vx_{c'}/b_v
       &&\text{at a product, with sibling }c',\\
 h_c&=Jh_v/b_v&&\text{at a genuine turn}.
 \end{split}
 \tag{6}
\]
The product rule follows from associativity inside \(\phi\).
For the turn, \(d_c=d_vJ/b_v\) and (5) give the second rule.
It uses the literal turn, not an algebra automorphism. Hence these
carriers retain every later return through the specified exterior.

## 2. A sharp polar estimate at a product

Write \(M_h\) for multiplication by \(h\) in the full algebra.
At a product define
\[
 B_v=JM_{h_v}/b_v,\qquad
 S_v=(B_v^*B_v)^{1/2}=|M_{h_v}|/b_v\succeq0.
 \tag{7}
\]
These are known matrices once \(x\) and its backward rows are known.
Commutativity and (2) imply
\[
 u^{\mathsf T}B_vw=d_v\Phi_v(u,w),\qquad
                            B_v^{\mathsf T}=B_v.
 \tag{8}
\]
For every \(u,w\in H_N\),
\[
 \boxed{\quad
 |d_v\Phi_v(u,w)|
       \le (u^*S_vu)^{1/2}(w^*S_vw)^{1/2}.
 \quad}
 \tag{9}
\]
Here is a finite-dimensional proof including the complex conjugations.
For any matrix \(B\), singular-value decomposition gives
\[
 |\langle f,Bg\rangle|
       \le\langle f,|B^*|f\rangle^{1/2}
                             \langle g,|B|g\rangle^{1/2}.
\]
If \(B^{\mathsf T}=B\), then
\(|B^*|=|B|^{\mathsf T}\). Apply this with \(f=\bar u\),
\(g=w\); its first quadratic form is \(u^*|B|u\).
This proves (9), also when the matrices are singular. Singular
vectors show that its constant one is sharp whenever \(B_v\ne0\).
No claim of a Loewner-smallest majorizing metric is made.

Let
\(\beta_v=\sup_{\|u\|=\|w\|=1}\|\Phi_v(u,w)\|\)
be the bilinear operator norm. It is at most the normalized full
tensor norm, hence at most \(\sigma\). From (8),
\[
 \|S_v\|=\|B_v\|\le\|d_v\|\beta_v,\qquad
                         \ker S_v=\operatorname{Ann}(h_v).
 \tag{10}
\]
The first equality and bound use decomposable inputs \(u\otimes w\).
They do not identify a bilinear norm with the norm of a row on the
whole tensor product. The kernel statement is the exact equality
\(\ker M_{h_v}=\{u:h_vu=0\}\), including nilpotent directions.
It concerns this particular contraction, not a quotient which can
be transported unchanged through another turn.

These Grams also assemble on the literal tree. Each packet is a child
of at most one product, so distinct sibling pairs are disjoint.
Let \(\mathcal B\) have blocks
\(\left(\begin{smallmatrix}0&B_v\\B_v&0\end{smallmatrix}\right)\)
on those pairs and zero on unused packets. Then
\[
 \sum_{v\ {\rm product}}e_L^{\mathsf T}B_ve_R
       =\tfrac12e^{\mathsf T}\mathcal Be,\qquad
 |\mathcal B|=\mathcal S
       =\bigoplus_{v\ {\rm product}}(S_v\oplus S_v)\oplus0,
 \qquad
 \left|\tfrac12e^{\mathsf T}\mathcal Be\right|
                                    \le\tfrac12e^*\mathcal Se.
 \tag{10a}
\]
This is a positive majorant for the error at the fixed trial field.
It makes no positivity assertion for the original complex source.

## 3. A computable disk for the original scalar

The exact error identity in [R] is
\[
 (I-A)e=r+Q(e),\qquad
 k=z+dr+\sum_{v\ {\rm product}}d_v\Phi_v(e_L,e_R),
 \tag{11}
\]
where \(Q_v(e)=\Phi_v(e_L,e_R)\) at products and zero otherwise.
Only the last sum requires an estimate. Compute the known correction
and nonnegative scalar majorants upward through the actual tree:
\[
 \delta=(I-A)^{-1}r,\qquad
 \Delta_v=\|r_v\|+\sigma\sum_{c}\Delta_c,
 \tag{12}
\]
\[
 \omega_v=\sum_c\|A_{vc}\|\omega_c+
       \mathbf1_{v\ {\rm product}}\beta_v\Delta_L\Delta_R.
 \tag{13}
\]
Empty sums are zero. The argument in [R], equations (16)–(18) gives
\(\|e_v\|\le\Delta_v\): at a product use the ordered difference
\(\Phi(e_L,a_R)+\Phi(x_L,e_R)\), with the true and trial packets
in their prescribed balls. Subtracting \(\delta\) from (11)
gives
\((I-A)(e-\delta)=Q(e)\). Its triangular equations and (13)
therefore prove
\[
                   \|e_v-\delta_v\|\le\omega_v.
 \tag{14}
\]
Thus both majorants are explicit finite calculations, with no unknown
closed invariant used as input.

At a product put \(s_v=\|S_v\|\), and, for either child \(c\), set
\[
 t_{vc}=\min\left\{\sqrt{s_v}\,\Delta_c,
      (\delta_c^*S_v\delta_c)^{1/2}
                                  +\sqrt{s_v}\,\omega_c\right\},
 \qquad R_{\rm pol}(x)=\sum_{v\ {\rm product}}t_{vL}t_{vR}.
 \tag{15}
\]
Triangle inequality for the seminorm \(\|S_v^{1/2}\cdot\|\),
(12), and (14) bound \(\|S_v^{1/2}e_c\|\) by \(t_{vc}\).
Equations (9)--(11) consequently give
\[
 |k-(z+dr)|\le R_{\rm pol}(x)
 \le\sum_{v\ {\rm product}}
                    \|d_v\|\beta_v\Delta_L\Delta_R
                         =R_{\rm loc}(x).
 \tag{16}
\]
The last expression is the earlier local radius of [R], with its
actual local bilinear norms. For evaluation, \(\beta_v\) may everywhere
be replaced by its recorded full tensor upper bound; no bilinear
maximization is required, and the same comparison remains valid.

Keep also [R]'s global quadratic radius. The fully computable result is
\[
 \widehat k=z+dr,\qquad
 R(x)=\min\{R_{\rm pol}(x),\ \|r\|^2/343\},
 \tag{17}
\]
\[
 \boxed{\quad
 B_{\rm tot}(|\widehat k|-R)_+
       \le |K_N|\le B_{\rm tot}(|\widehat k|+R).
 \quad}
 \tag{18}
\]
It is never a worse disk than the earlier minimum of the local and
global radii. Vanishing carriers and singular polar matrices require
no inversion or exceptional case. The center remains the original
coherent correction, before taking an absolute value.

## 4. An exponential saving at the actual cylindrical closing

Suppose the top proper gate is a product with budget \(b_v\), and
the original normalized closing is \(L=\chi\phi/b_\rho\).
The prescribed scalar \(\chi\) and its actual closing budget
\(b_\rho\) are retained. Then
\[
 h_v=\chi/b_\rho,\qquad
 B_v=\frac{\chi}{b_\rho b_v}J,\qquad
 S_v=\frac{|\chi|}{b_\rho b_v}I.
 \tag{19}
\]
Thus the top contribution to (16) is at most
\(|\chi|\Delta_L\Delta_R/(b_\rho b_v)\).
The old local bound instead charges
\(|\chi|\|M\|_{\rm bil}\Delta_L\Delta_R/(b_\rho b_v)\),
where \(M\) is actual multiplication. This is a bilinear saving:
\(|\phi(uw)|\le\|u\|\|w\|\), whereas the full tensor row
\(\phi M\) has Euclidean norm \(\sqrt N\).

The difference is exponential. For \(k=\lfloor N/4\rfloor\) and
all sufficiently large levels, the exact formula in [M], equation (2) gives
\[
 \|M\|_{\rm bil}\ge\mu_{k,k,2k}
                         =s_{2k}^{\,2}/s_k^{\,4},\qquad
 \log\mu_{k,k,2k}=\frac{2G_{\rm Cat}}\pi N+O(\log N).
 \tag{20}
\]
For completeness, let \(J_0(x)=\int_0^x\log(2\sin\pi t)dt\).
Subtracting \(\log t\) leaves a smooth function on every interval
\([0,b]\), \(b<1\); its Riemann-sum error is bounded. Integral
comparison for \(\sum\log(a/N)\) gives
\(\log s_n=NJ_0(n/N)+O(\log N)\) in the ranges used here.
The elementary sine double-angle identity gives
\(J_0(1/2)=0\) and \(J_0(1/4)=-G_{\rm Cat}/(2\pi)\), where
\(G_{\rm Cat}=\int_0^{\pi/4}\log(\cot t)dt\).
Indeed the integrals of \(\log(2\sin t)\) and
\(\log(2\cos t)\) on \([0,\pi/4]\) sum to zero; the cosine
integral minus the sine integral is \(G_{\rm Cat}\).
These facts prove (20), with the rounding
of \(k\) changing only the stated error.

The same normalization budgets occur on both sides of this comparison.
Restoring \(B_{\rm tot}\) preserves the ratio. The saving comes from
composing multiplication with the original closing before estimating
it. Other products can still control the radius of a larger expression.

## 5. Turns, marked caps, and scope

For the other original closure \(L=\chi\lambda_0/b_\rho\), (2)
gives \(h_v=\chi e_d/b_\rho\). Since
\(M_{e_d}u=u_0e_d\), its polar matrix at a product is
\[
              S_v=\frac{|\chi|}{b_\rho b_v}
                                      |e_0\rangle\langle e_0|.
 \tag{21}
\]
Only the two value errors at \(c_0\) enter that contraction.
But the next genuine turn sends this carrier to a scalar multiple
of \(1\), by (6), and the full-rank matrix (19) returns. Thus neither
normal directions nor a future return have been discarded.

The matrices and radii above apply to arbitrary feasible trial fields,
all levels and both parities, with the literal original closing.
They do not reduce the physical dimension, assert positivity of the
complex error, or supply an asymptotic estimate for \(\widehat k\).
A lower bound still needs that corrected center to exceed its proved
radius at the desired rate. No volume identity or finite-exception
theorem is inferred. The new quantitative assertions are the
source-sensitive no-worse disk (15)--(18) and the exponential local
saving (19)--(20), rather than a claim of novelty for polar
decomposition or adjoint-weighted error estimation.

## Complete sources

All four complete proof texts were read at matching versions:

| Label | Complete source | SHA256 |
|---|---|---|
| R | notes/research_conway_source_visible_residual_transport.md | 0d344301b0df65246551cf81498eff84582f796a03271b201f8fbba6c7742007 |
| F | notes/research_conway_full_boundary_quotient_gram.md | debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077 |
| M | notes/actual_positive_newton_multiplication.md | 543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb |
| C | notes/research_convex_normalized_conway_source.md | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

The complete comparison text
notes/research_conway_orthogonal_linear_elimination.md, SHA256
aa53b79685296193d5bf7fc66e53f3a3fbe03fc72a36481fb3aee23afe2ae113,
retains an inverse boundary Gram after eliminating linear residuals;
it does not give the polar product disk above. Only written
mathematics and source-text/hash operations were used. No mathematical
program, test, build, git operation or earlier-final edit was made.

[R]: research_conway_source_visible_residual_transport.md
[M]: https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_positive_newton_multiplication.md
