# An exact signed principal-compression expansion of the odd lower cofactor

This note gives an all-level alternative to fitting a constant adjugate matrix. The original odd lower cofactor at the complete endpoint is a signed sum of positive principal determinants multiplied by monomials. Its total absolute polynomial mass is at most a linear factor in the level times the original positive endpoint cofactor, coefficient by coefficient. The estimate therefore survives multiplication by positive spectator polynomials and the original shared coefficient extraction.

This is not a construction of a face-independent matrix \(W_N\) with \(D/N=\operatorname{Tr}(W_N\operatorname{adj}M)\). The principal determinants below have different sizes and complementary monomial factors. Their rank deficits range over the whole available interval. This alone does not propagate cap cancellation to a neighborhood of the other spectra or prove a full-source or filling estimate.

## 1. Exact original source

Fix \(N=2m+1\ge3\), and put
\[
 \theta=\frac\pi N,\qquad s_j=2\sin(j\theta),\qquad
 a_j=4\cos^2((j+\tfrac12)\theta),\quad A=x+y,\quad P=xy.
 \tag{1}
\]
The face variables are the original outer variables \(x,y\) and middle variable \(b\); \(u=-\sigma-2\). The row-replacement polynomials of the original cofactor identity are
\[
 \begin{split}
 R_0(b;u)&=1,\\
 R_j(b;u)&=b^j\prod_{r<j}(a_r+u)+s_j^2 A R_{j-1}(b;u)
       +s_js_{j-1}(a_{j-1}+u)P R_{j-2}(b;u),
 \end{split} \tag{2}
\]
where the last summand is absent at \(j=1\). Write
\[
 G_b(u)=R_m(b;u),\qquad D_b(u)=R_{m-1}(b;u).
 \tag{3}
\]
The full central numerator remains
\[
 P_C(u)=G_b(u)G_c(u)+u s_m^2xyD_b(u)D_c(u).
 \tag{4}
\]
Its first derivative at zero retains the skipping current \(s_m^2xyD_b(0)D_c(0)\), as well as the two differentiated visited-central terms.

For \(0\le a\le m\), define
\[
 M_a=bI_a+\frac x2H_-^{[a]}+\frac y2H_+^{[a]},
 \qquad Q_a=\det M_a,\qquad Q_0=1.                 \tag{5}
\]
The matrices are leading principal submatrices of the same level-\(N\) positive endpoint matrices. Their entries are
\[
 (H_\pm)_{j,j}=\frac1{\cos(j\theta)\cos((j+1)\theta)},\qquad
 (H_\pm)_{j-1,j}=\sqrt{B_j}\,[\sin(j\theta)\pm i\cos(j\theta)],
\]
\[
 B_j=\frac{\sin^2(j\theta)}{\cos^2(j\theta)
                   \sin((2j-1)\theta)\sin((2j+1)\theta)}.
 \tag{6}
\]
They are positive definite for \(a\le m\). The exact source determinant theorem gives \(G_b(0)=NQ_m\). Cauchy–Binet gives nonnegative coefficients for every \(Q_a\), and the positive imaginary part of its matrix pencil proves real stability. No level is changed when \(a\) changes.

The source definitions and determinant identities are from 'actual_cross_cofactor_factorization.md', 'actual_q_hahn_joint_accretive_determinant.md', sections 2–4, and 'actual_complete_circle_positive_face_polynomial.md'. Write \(F\preceq G\) when \(G-F\) has nonnegative coefficients in the original variables \(b,x,y\).

## 2. Physical-node factorization and a positive tail

Index the nonzero nodes by \(k=1,\ldots,m\), and set
\[
 a=m-k,\qquad u_k=-4\sin^2(k\theta)=-a_a.
 \tag{7}
\]
The original spectral value is \(\sigma_k=-2\cos(2k\theta)\). At this node the \(a\)-th triangular diagonal vanishes, and
\[
 R_a(b;u_k)=S_{2a}Q_a(b,x,y),\qquad
 S_{2a}=\prod_{r=1}^{2a}s_r=\prod_{r<a}(a_r-a_a)>0.
 \tag{8}
\]
The empty products and determinant are one. To verify the normalization, use the actual polynomial Casimir
\[
 \mathcal L=\mathcal D(b^2+Ab+P)\mathcal D,\qquad
 \mathcal D b^j=s_jb^{j-1},\qquad \lambda_j=s_js_{j+1}.
\]
The row-replacement equation makes \(R_a\) its degree-\(a\) eigenpolynomial with eigenvalue \(\lambda_a\). Its leading coefficient is the product in (8). The differences \(\lambda_a-\lambda_r=s_{a-r}s_{a+r+1}>0\) prove uniqueness and the product identity. The exact q-Hahn three-term determinant identity identifies the monic eigenpolynomial with (5).

For \(a\le j\le m\), put \(n=j-a\). Then
\[
 R_j(b;u_k)=S_{2a}Q_a(b,x,y)K_{a,j}(x,y),\qquad K_{a,a}=1,
 \tag{9}
\]
because every inhomogeneous prefix after row \(a\) in (2) has a zero factor. The tail recurrence is
\[
 K_{a,j}=s_j^2A K_{a,j-1}
       +s_js_{j-1}(a_{j-1}-a_a)P K_{a,j-2}.
 \tag{10}
\]
The second coefficient vanishes at \(j=a+1\) and is negative afterward. Positivity must therefore be established without replacing these signs by absolute values.

Normalize \(k_n=K_{a,a+n}/\prod_{r=a+1}^{a+n}s_r^2\). Then \(k_0=1,k_1=x+y\), and
\[
 k_n=(x+y)k_{n-1}-\beta_nxyk_{n-2},\qquad
 \beta_n=\frac{s_{n-1}s_{2a+n}}{s_{a+n}s_{a+n-1}}
       =1-\frac{s_as_{a+1}}{s_{a+n}s_{a+n-1}}.
 \tag{11}
\]
The sine product subtraction identity gives the last equality. Since \(a+n\le m\), positivity and monotonicity of the relevant sines give \(0\le\beta_n\le1\).

Put \(h_n=k_n-xk_{n-1}\), with \(h_1=y\). Equation (11) gives
\[
 h_n=yh_{n-1}+(1-\beta_n)xyk_{n-2},\qquad
 k_n=xk_{n-1}+h_n.                                    \tag{12}
\]
Induction proves nonnegative coefficients for \(h_n,k_n\). Returning to (11) also proves
\[
                  0\preceq k_n\preceq(x+y)^n.          \tag{13}
\]
Thus the nodal factorization is a positive monomial sum times a principal determinant, despite the negative two-step term of (10).

## 3. Coefficientwise endpoint comparison

For prefix rows \(r<a\), \(0\le a_r-a_a\le a_r\). The positive path expansion of (2) up to row \(a\) therefore gives
\[
                  0\preceq R_a(b;u_k)\preceq R_a(b;0).
 \tag{14}
\]
Equation (13) bounds the nodal continuation by the monomer extension
\[
 R_j(b;u_k)\preceq R_a(b;0)\prod_{r=a+1}^{j}s_r^2(x+y).
\]
The endpoint recurrence contains that extension and has only nonnegative additional terms. Consequently
\[
 \boxed{\quad0\preceq R_j(b;u_k)\preceq R_j(b;0),
                  \qquad a\le j\le m.\quad}            \tag{15}
\]
This uses the original face variables coefficient by coefficient. Protected zeros may be specialized afterward. It does not substitute independent corner maximizations for shared targets.

## 4. Exact endpoint interpolation with bounded weights

The degree of \(D_b(u)\) in \(u\) is at most \(m-1\). Let
\[
 A_N(u)=\prod_{k=1}^m(u+4\sin^2(k\theta)).
\]
The finite sine identity is
\[
 A_N(-4\sin^2t)=\frac{\sin Nt}{\sin t},\qquad A_N(0)=N.
 \tag{16}
\]
Both sides are degree-\(m\) polynomials in \(-4\sin^2t\), with the same roots and leading coefficient. Differentiating at \(t=k\theta\) gives
\[
 A_N'(u_k)=-\frac{N(-1)^k}{8\sin^2(k\theta)\cos(k\theta)}.
\]
Thus the cardinal coefficient at zero is \(2(-1)^{k+1}\cos(k\theta)\), and exact interpolation gives
\[
 \boxed{\quad D_b(0)=\sum_{k=1}^m
       2(-1)^{k+1}\cos(k\theta)D_b(u_k).\quad}           \tag{17}
\]
The sum of absolute weights is exactly
\[
 C_N=2\sum_{k=1}^m\cos(k\theta)
                  =\csc(\theta/2)-1\le2m=N-1.         \tag{18}
\]
This interpolates the actual degree-\(m-1\) cofactor. It does not infer the full numerator's normal derivatives from value-only node data.

Combining (9), (13), and (17) gives at most \(m(m+1)/2\) signed stable atoms. Each node \(k\) contributes nonnegative scalar multiples of
\[
               x^r y^{k-1-r}Q_{m-k}(b,x,y),
                         \qquad0\le r\le k-1,          \tag{19}
\]
with sign \((-1)^{k+1}\). Every atom has the correct degree \(m-1\). It is a positive principal determinant multiplied by one-dimensional coordinate pencils.

Let \(\mathfrak A_N\) be their total absolute polynomial mass. It is exactly
\[
 \mathfrak A_N=\sum_{k=1}^m2\cos(k\theta)D_b(u_k).
\]
The coefficientwise triangle inequality and (15) give
\[
 \boxed{\quad D_b(0)\preceq\mathfrak A_N
                       \preceq C_ND_b(0).\quad}        \tag{20}
\]
Dividing every polynomial by \(N\) gives the same statement for \(D/N\). This controls absolute polynomial mass, not merely scalar interpolation weights.

## 5. Shared extraction and the skipping current

For any nonnegative-coefficient polynomial \(F\) in the original shared variables, and any original target multi-index \(\tau\),
\[
 \sum_{\text{signed atoms }T}|[L^\tau]FT|
    =[L^\tau]F\mathfrak A_N
    \le C_N[L^\tau]FD_b(0).                            \tag{21}
\]
Face identifications and protected specializations may be made first. The spectators need not have disjoint variables. For signed spectators one may replace \(F\) by its coefficientwise absolute polynomial, but that operation need not preserve the desired coherent cap bound.

The skipping current in (4) has a similar exact mass estimate. The endpoint recurrence gives \(G_b(0)\succeq s_m^2(x+y)D_b(0)\), and likewise at \(c\). Since \((x+y)^2\succeq2xy\),
\[
 s_m^2xy\,\mathfrak A_N(b)\mathfrak A_N(c)
 \preceq\frac{C_N^2}{2s_m^2}G_b(0)G_c(0)
 \preceq\frac{(N-1)^2}{6}G_b(0)G_c(0).                 \tag{22}
\]
Here \(s_m^2=4\cos^2(\theta/2)\ge3\). The factor \(2\), rather than \(4\), is the coefficientwise justification. Equation (22) survives the same shared extraction. It retains the skipping current but does not account for the other two terms of \(P_C'(0)\), which need their own exact interpolation.

## 6. Precise limitation and finite checks

The exact signed expansion has polynomial mass and uses the original source throughout. It is consistent with nonstability of \(D\), because its coefficients have both signs. It does not construct a constant Hermitian \(W_N\), bound such a matrix's singular values, or represent a neighboring spectrum by a small-rank perturbation of one endpoint pencil.

The principal rank at node \(k\) is \(m-k\), and the forced monomial degree is \(k-1\). Thus the expansion spans the entire rank-deficit range. Equation (20) does not concentrate its mass at bounded or sublinear deficit. A far-node spectral loss must be compared to the actual cap/exterior budget after shared extraction; it cannot simply be discarded relative to an unrelated central endpoint. Protected monomial cases can have many coincident nodal pieces whose signed cancellations matter.

The executable companion 'md-odd-nodal-signed-compression-exact.py' was run at \(N=3,5,7,9,11\) over exact cyclotomic fields. It constructs the original recurrence, independently constructs principal determinants by their tridiagonal recursion, evaluates cardinal weights from their full node products, and compares every coefficient of the reconstructed \(D\). These bounded checks support the finite algebra only. The inequalities above have direct all-level proofs and are not inferred from samples. No invariant or volume conclusion is claimed.
