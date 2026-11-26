# The residual Jacobian and Gaussian determinant of the Conway minimum

21 November 2026. Research note; previous finals and public manuscripts
remain unchanged.

The normalized source minimum has a uniformly bounded real Hessian,
but its number of variables grows with the quantum level. Bounding
its Gaussian determinant by a power of the Hessian condition number
would therefore introduce an artificial exponential factor. The tree
structure and the Hilbert--Schmidt normalization remove that loss.
The determinant below stays within universal constants of one.

This controls a Gaussian normalization, not the value of the minimum.
No simultaneous limit in quantum level and temperature, or comparison
with hyperbolic volume, is claimed.

## 1. Actual normalized data and residual coordinates

Use the actual complete Conway compiler of the
[convex source theorem](research_convex_normalized_conway_source.md).
There are \(s\) proper vertices. At level \(N\), each proper packet
lies in the full complex Newton space \(H_N\), including its confluent
normal directions. Put \(D=Ns\) and identify their direct sum with
\(\mathbb C^D\).

Every prescribed leaf, linear gate, bilinear gate and original closing
row has been divided by its stated budget
\(16\max(1,\|T_v\|_{\rm HS})\). Thus its Hilbert--Schmidt norm, and
therefore its operator norm, is at most \(\sigma=1/16\).
Write \(\Phi_v\) for these local maps, and \(c\) for the row on the
whole direct sum which is the normalized original closing row at
the top packet and zero elsewhere. Define
\[
 G_v(x)=\Phi_v((x_j)_{j\text{ child of }v})-x_v,\qquad
 E(x)=\|G(x)\|^2+|cx|^2.                                  \tag{1}
\]
The feasible set is the product \(\mathcal D\) of the proper unit
balls. All scalar source budgets are retained; if \(a\) is the exact
normalized recursion, then
\[
 G(a)=0,\qquad \|a_v\|\le\sigma,\qquad
                 k=ca=K_N/B_{\rm tot},\quad |k|\le\sigma^2. \tag{2}
\]
The cited theorem proves that \(E\) has a unique interior minimizer
\(x_*\) on \(\mathcal D\), and \(I\le D_{\mathbb R}^2E\le3I\)
there. Set \(r_*=G(x_*)\). Evaluating at \(a\) gives
\[
                    \|r_*\|^2\le E(x_*)\le|k|^2\le\sigma^4.
                                                                 \tag{3}
\]
Real inner products mean \(\operatorname{Re}(u^*v)\), and real
Lebesgue measure is used throughout.

Order children before parents. Then
\[
 T(x)=DG(x)=-I+A(x),\qquad A(x)^s=0,\qquad
                    \det_{\mathbb C}T(x)=(-1)^D.          \tag{4}
\]
In fact \(G\) is a polynomial automorphism of \(\mathbb C^D\):
given \(r\), its inverse is obtained successively from
\(x_v=\Phi_v((x_j)_j)-r_v\). Consequently its real Jacobian is
exactly one everywhere.

There is no lower minimum hidden outside the feasible balls.
If \(x\notin\mathcal D\), choose a violating vertex all of whose
children are in their unit balls. Then
\(\|\Phi_v\|\le\sigma\) and \(\|x_v\|>1\), so
\[
                       E(x)\ge\|G_v(x)\|^2>(1-\sigma)^2.
                                                                 \tag{5}
\]
This exceeds (3). Since a polynomial automorphism is proper
(its continuous polynomial inverse takes compact sets to compact
sets), \(E\) is coercive. Thus \(x_*\) is also its unique global
minimum on the entire real coordinate space.

## 2. A determinant bound independent of the number of variables

Let
\[
 T_*=DG(x_*),\qquad d_*=c(I-A(x_*))^{-1},\qquad
                         H_*=D_{\mathbb R}^2E(x_*).
                                                                 \tag{6}
\]
The row \(d_*\) is the actual closing row transported backwards
through the linearized tree. Since each child derivative has norm
at most \(\sigma\), each parent has at most two children, and each
child belongs to one parent,
\[
 \|A(x_*)\|\le\sqrt2\sigma\le\tfrac18,\qquad
 \|T_*^{-1}\|\le\tfrac87,\qquad \|d_*\|\le\tfrac1{14}.    \tag{7}
\]

**Theorem.** The real Gaussian determinant satisfies
\[
 \boxed{\quad
 (1+\|d_*\|^2)^2(1-4\sigma^2\|r_*\|^2)
       \le\det_{\mathbb R}(H_*/2)
       \le(1+\|d_*\|^2)^2 .
 \quad}                                                       \tag{8}
\]
In particular, with \(\gamma=197/196\),
\[
             1-2^{-22}\le\det_{\mathbb R}(H_*/2)\le\gamma^2.
                                                                 \tag{9}
\]
These constants do not depend on the level, the tree size or its
fixed crossing powers after the original budgets are retained.

**Proof.** Only bilinear gates contribute to the residual curvature.
At a product vertex \(v\), write the normalized gate coefficients
as \(B_{v,kij}\), and define a complex matrix
\[
                  (C_v)_{ij}=\sum_k\overline{(r_*)_{v,k}}
                                                    B_{v,kij}.
 \]
Cauchy--Schwarz and the normalized Hilbert--Schmidt budget give
\(\|C_v\|_{\rm F}\le\sigma\|(r_*)_v\|\), where
\(\|\cdot\|_{\rm F}\) is matrix Frobenius norm.

Let \(C_0\) be the complex symmetric matrix with blocks \(C_v\)
between the left and right child variables and \(C_v^T\) in the
reverse positions, with every other block zero. Distinct parents
have disjoint sibling pairs. Therefore
\[
                         \|C_0\|_{\rm F}^2
                       \le2\sigma^2\|r_*\|^2.                 \tag{10}
\]
The exact half-Hessian quadratic form is
\[
 \tfrac12H_*[h,h]
       =\|T_*h\|^2+|ch|^2+\operatorname{Re}(h^TC_0h).
                                                                 \tag{11}
\]
Make the complex-linear change \(u=T_*h\).
Its real determinant is one by (4). Put
\(\lambda=cT_*^{-1}=-d_*\), and \(H_0=I+\lambda^*\lambda\)
as a complex Hermitian matrix. The first two terms of (11)
become \(u^*H_0u\). Since this is a rank-one update,
\[
        \det_{\mathbb R}H_0=(1+\|\lambda\|^2)^2.          \tag{12}
\]
The further complex-linear change \(v=H_0^{1/2}u\) leaves the
curvature in the form \(\operatorname{Re}(v^TC_1v)\), where
\[
 C_1=H_0^{-T/2}T_*^{-T}C_0T_*^{-1}H_0^{-1/2}.
 \]
As \(\|H_0^{-1/2}\|\le1\), (7) and (10) imply
\[
 \|C_1\|_{\rm F}^2
    \le(8/7)^4\,2\sigma^2\|r_*\|^2
                         \le4\sigma^2\|r_*\|^2.             \tag{13}
\]

For completeness, the real symmetric matrix representing
\(\operatorname{Re}(v^TC_1v)\), in real and imaginary coordinates,
is
\[
 \mathcal C=
 \begin{pmatrix}
  \operatorname{Re}C_1&-\operatorname{Im}C_1\\
  -\operatorname{Im}C_1&-\operatorname{Re}C_1
 \end{pmatrix}.
 \]
It anticommutes with multiplication by \(i\). Its eigenvalues
therefore occur as \(t_j,-t_j\), \(1\le j\le D\), including zeros,
and
\(\sum_jt_j^2=\|C_1\|_{\rm F}^2\).
In view of (3) and (13), every \(t_j^2<1\).
Taking the determinants in (11)--(12) gives the exact identity
\[
 \det_{\mathbb R}(H_*/2)
        =(1+\|d_*\|^2)^2\prod_{j=1}^D(1-t_j^2).         \tag{14}
\]
For \(0\le b_j\le1\), induction gives
\(1-\sum_jb_j\le\prod_j(1-b_j)\le1\).
Apply this with \(b_j=t_j^2\) and use (13). This proves (8).
Finally \(4\sigma^2\|r_*\|^2\le4\sigma^6=2^{-22}\), and
\((1+\|d_*\|^2)^2\le(1+1/196)^2=\gamma^2\).
This proves (9). \(\square\)

The Hilbert--Schmidt normalization is substantive in this argument.
An operator-norm bound on each bilinear gate alone would not give
(10) without a dimension factor.

## 3. The exact integral and its Gaussian normalization

For a real inverse temperature \(\tau>0\), define the normalized
positive integral on the whole coordinate space
\[
 Z_N(\tau)=\left(\frac{\tau}{\pi}\right)^D
                          \int_{\mathbb C^D}e^{-\tau E(x)}\,dx.
                                                                 \tag{15}
\]
The change of variables \(r=G(x)\), with its exact Jacobian one,
gives
\[
 \boxed{\quad
 Z_N(\tau)=
   \mathbb E_{\,r\sim\mathcal N_{\mathbb C}(0,\tau^{-1}I)}
       \exp\{-\tau|cG^{-1}(r)|^2\},\qquad 0<Z_N(\tau)\le1 .
 \quad}                                                        \tag{16}
\]
Here the complex Gaussian has density
\((\tau/\pi)^D e^{-\tau\|r\|^2}\).
The inverse \(G^{-1}\) is the actual polynomial recursion from
Section 1. The scalar \(cG^{-1}(0)\) is the original normalized
source \(k\); it is not replaced by an unsigned model.

The quadratic approximation has the exact integral
\[
 \left(\frac{\tau}{\pi}\right)^D
 \int e^{-\tau\{E(x_*)+\tfrac12H_*[h,h]\}}\,dh
       =\frac{e^{-\tau E(x_*)}}
                        {\sqrt{\det_{\mathbb R}(H_*/2)}}.
                                                                 \tag{17}
\]
By (9), its prefactor lies in
\[
              \left[\frac{196}{197},\,
                                  (1-2^{-22})^{-1/2}\right].
                                                                 \tag{18}
\]
In particular the logarithm of this prefactor is uniformly bounded,
despite the growing number of coordinates.

For each **fixed** \(N\), the same is the usual large-\(\tau\)
prefactor of (15):
\[
 Z_N(\tau)=
   \frac{e^{-\tau E(x_*)}}{\sqrt{\det_{\mathbb R}(H_*/2)}}
                                      (1+o_N(1)),
                      \qquad \tau\longrightarrow\infty.        \tag{19}
\]
Indeed the unique global minimum is interior and nondegenerate.
Taylor expansion and \(h=\tau^{-1/2}u\) give (19) locally, dominated
by a fixed positive quadratic form. On the complement of a fixed
neighborhood there is a positive energy gap, by coercivity and
uniqueness. Its integral is negligible: integrability of \(e^{-E}\)
follows directly from the change of variables in (16), and
\(e^{-\tau E}\le e^{-(\tau-1)(E(x_*)+\delta)}e^{-E}\)
on a region with gap \(\delta>0\).

No uniform error bound for (19) when \(N\) also varies has been
proved here. In particular neither a polynomial temperature nor
an exponentially increasing temperature is substituted into it.
The theorem removes a spurious determinant factor from the local
Gaussian normalization; it does not determine \(E(x_*)\).
Its source-compatible geometric rate, and a nonzero geometric lower
certificate after arbitrary fixed short fillings, remain necessary.

## Complete direct source

The following complete matching text was read. It supplies the actual
compiler, its Hilbert--Schmidt budgets, the marked closing row, and the
interior source minimum. The polynomial change of variables and the
dimension-independent determinant estimate are proved above.

| Source | SHA-256 |
|---|---|
| [Normalized convex Conway source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical experiment, build, git operation,
previous-final edit or public-document change was performed.
