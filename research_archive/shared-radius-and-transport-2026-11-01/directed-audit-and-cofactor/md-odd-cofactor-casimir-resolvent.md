# The original odd lower cofactor as a forced Casimir polynomial

This is an exact finite reduction of the source cofactor. It does not establish a signed compression representation or a neighboring-spectrum bound.

Let \(N=2m+1\), \(\theta=\pi/N\),
\[
 s_j=2\sin(j\theta),\quad
 a_j=2+2\cos((2j+1)\theta),\quad A=x+y,\quad P=xy.
\]
The level remains \(N\). Define the polynomial operator
\[
 \mathcal D b^j=s_j b^{j-1},\qquad
 \mathcal L=\mathcal D\,(b^2+Ab+P)\,\mathcal D,
 \qquad \lambda_j=s_js_{j+1}.
 \tag{1}
\]
Multiplication by the quadratic is performed before the leftmost \(\mathcal D\). In particular
\[
 \mathcal L b^j
 =\lambda_j b^j+s_j^2A b^{j-1}
       +s_js_{j-1}P b^{j-2}.
 \tag{2}
\]
Absent negative powers have zero coefficient. The elementary cosine identity gives
\[
 \lambda_m=s_m^2,\qquad \lambda_m-\lambda_j=a_j.
 \tag{3}
\]
Thus the matrix of \(\lambda_m-\mathcal L\) in the monomial basis is exactly the original triangular Casimir block: diagonal \(a_j\), first lowering entry \(-s_j^2A\), and second lowering entry \(-s_js_{j-1}P\).

Let \(R_j(b;0)\) denote the literal last-row-replacement polynomials of `actual_cross_cofactor_factorization.md`, and set
\[
 G=R_m(b;0),\qquad D=R_{m-1}(b;0).
\]
The exact source identities are
\[
 \boxed{\quad
  (\lambda_m-\mathcal L)G=0,\qquad
  (\lambda_m-\mathcal L)\frac DN=b^{m-1}.
 \quad}
 \tag{4}
\]
Here is a direct proof of the normalization. On degrees at most \(m-1\), write \(T=\lambda_m-\mathcal L\). Its determinant is
\[
 \det T=\prod_{r=0}^{m-1}a_r=N.
 \tag{5}
\]
Indeed \(a_r=s_{m-r}^2\), and \(\prod_{j=1}^{m}s_j^2=N\) is the odd root-of-unity sine product. The last-row-replacement formula gives
\[
 D(b)=N(1,b,\ldots,b^{m-1})\,T^{-1}e_{m-1}.
\]
Applying \(T\) as a polynomial operator proves the second equation of (4). For the first, append the row and column of degree \(m\). Its diagonal is zero by (3), and the original monic eigenvector recursion determines the coefficients below degree \(m\). The last-row-replacement polynomial has leading coefficient \(\prod_{r<m}a_r=N\), hence is exactly this eigenpolynomial multiplied by \(N\). Equivalently, multiplying the triangular matrix by its adjugate proves the identity without division.

The coefficientwise proof is equally explicit. If \(h=\sum h_jb^j\), then
\[
 [b^j](\lambda_m-\mathcal L)h
 =a_jh_j-s_{j+1}^2A h_{j+1}
       -s_{j+2}s_{j+1}P h_{j+2}.
 \tag{6}
\]
The original path coefficients obey this recurrence. For \(D\), its top coefficient is \(N/a_{m-1}\), so the right side is \(N\) at \(j=m-1\) and zero below it. For \(G\), the top coefficient is \(N\), the diagonal at \(m\) is zero, and every row vanishes.

## The exact spectral expansion and its limitation

For each \(0\le n\le m\), let \(Q_n(b;x,y)\) be the unique monic polynomial of degree \(n\) satisfying
\(\mathcal LQ_n=\lambda_nQ_n\). This is the actual homogenized q-Hahn polynomial. Uniqueness follows from
\[
 \lambda_n-\lambda_j
 =4\sin((n-j)\theta)\sin((n+j+1)\theta)>0
 \quad(0\le j<n\le m).
 \tag{7}
\]
Expand the monomial in this triangular basis,
\[
 b^{m-1}=\sum_{n=0}^{m-1}c_n(x,y)Q_n(b;x,y).
\]
Then (4) gives the exact finite formula
\[
 \frac{D}{N}
 =\sum_{n=0}^{m-1}\frac{c_n(x,y)}{a_n}Q_n(b;x,y).
 \tag{8}
\]
Its smallest denominator is \(a_{m-1}=4\sin^2\theta\), of order \(N^{-2}\). This fact alone is **not** an operator-norm bound. The expansion coefficients and the norm of the triangular change of basis must also be controlled in the norm relevant to coherent extraction. The auxiliary q-Hahn moment functional depends on the face parameters; it cannot silently be treated as a fixed positive metric on all complex or negative face values.

The central positive determinant remains
\[
 G=N\det\left(bI+\frac x2H_-+\frac y2H_+\right).
 \tag{9}
\]
Consequently the unresolved task can be stated precisely: lift the inverse in (4) to a controlled constant-matrix operator on adjugates of the pencil in (9), or find another source-exact signed compression representation with a controlled norm. The proposed identity is
\[
 \frac DN=\operatorname{Tr}\left(W_N\operatorname{adj}
       \left(bI+\frac x2H_-+\frac y2H_+\right)\right).
 \tag{10}
\]
No such all-level formula for \(W_N\) has been proved here.

The one-level script `md-odd-adjugate-casimir-probe.py` checks a tempting but unsupported lift: the ordinary Hilbert–Schmidt Gram matrix of adjugate coefficients does not make the coefficient operator in (2) self-adjoint at \(N=7\). Its relative matrix defect is approximately \(0.237\). A second one-level nonlinear fit, `md-odd-adjugate-rank-two-probe.py`, did not find a rank-two representation at \(N=13\); this is not an impossibility proof. Both are diagnostics used to avoid assuming a simple metric or rank reduction. Neither supplies an analytic estimate.

The original deformed central numerator is still
\[
 G_b(u)G_c(u)+u s_m^2xyD_b(u)D_c(u).
\]
Its central-skipping term, all spectral normal derivatives, and the original shared face targets remain necessary. Equations (4)–(10) make no new one-cap, multi-cap, filling, or volume claim.
