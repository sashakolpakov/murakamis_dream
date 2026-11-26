# Stationary-reference bounds from a product boundary

Research lemma, 6 November 2026. The stationary-reference extension
works with several complex external coordinates. Bounds on the
distinguished boundary of a product of clipped disks or rectangles
suffice, with an explicit sum of response costs. Matching internal
responses cancel separately in every parameter direction before
absolute values are taken. This is a conditional analytic theorem;
it supplies no new source comparison or numerical bound.

## 1. Jointly holomorphic references and coordinate responses

For \(1\le k\le d\), let \(K_k=\overline{\Omega_k}\) be a
closed disk, a convex clipped disk with nonempty interior, or a
closed rectangle. Put
\[
 K=\prod_{k=1}^dK_k,\qquad
 \partial_{\rm dist}K=\prod_{k=1}^d\partial\Omega_k.
 \tag{1}
\]
Thus every clipping segment is included. For rectangles, the factors
in the distinguished boundary are the entire perimeters, not just
their vertices.

Let \(r(c)\in\mathbb C^n\), \(c=(c_1,\ldots,c_d)\), be
jointly holomorphic on a neighborhood of \(K\). Let \(F\) be a
holomorphic reference phase on a neighborhood of \(r(K)\), with
fixed original branches and no additional explicit dependence on \(c\).
Partition the reference coordinates into internal indices \(I\) and
boundary indices \(B\). Assume on that neighborhood that
\[
 F_i(r(c))=0\quad(i\in I),\qquad
 p_j(c)=F_j(r(c))\quad(j\in B).
 \tag{2}
\]
All derivatives below are complex derivatives in the indicated
external parameter. With \(r_k=\partial_{c_k}r\), differentiation
of (2) gives
\[
 F''(r)r_k=(v_i^{(k)})_{i=1}^n,\qquad
 v_i^{(k)}=0\ (i\in I),\quad
 v_j^{(k)}=\partial_{c_k}p_j\ (j\in B).
 \tag{3}
\]

Fix a real target vector \(x\), a real height vector \(h\), and
a nonnegative real diagonal matrix
\(\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\).
They are independent of every parameter \(c_k\). Set
\[
 w=x+ih+\tfrac12\Lambda(r-\bar r),\qquad
 D(c;x)=\Re\{\Psi(w)-F(r)-F'(r)\cdot(w-r)\}.
 \tag{4}
\]
Require \(\Psi\) to be holomorphic on a neighborhood of the
entire target image, and
\(-\Re\Psi''(w)\succeq0\) on that entire image.
These requirements concern all of \(K\), not just (1).
They can hold uniformly for a fixed compact set of real targets
and a finite family of target phases; the proof then applies to
each target and phase separately.

Write \(\Delta_k=\partial_{\Re c_k}^2+\partial_{\Im c_k}^2\).
Holding the other parameters fixed, the exact
[one-parameter identity](research_mixed_stationary_reference_boundary_extension.md)
and (3) give
\[
 \begin{split}
 \Delta_kD
 &=-\Re\{(\Lambda r_k)^T\Psi''(w)\Lambda\bar r_k\}
     +2\Re\sum_{j\in B}
        \lambda_j(\partial_{c_k}p_j)
                      \overline{\partial_{c_k}r_j}\\
 &\ge-2B_k(c),\qquad
 B_k(c)=\sum_{j\in B}
       \lambda_j|(\partial_{c_k}p_j)(\partial_{c_k}r_j)|.
 \end{split}
 \tag{5}
\]
The first term is nonnegative because \(\Psi''\) is symmetric
and its real part is nonpositive. Each product inside \(B_k\)
is holomorphic in all the parameters. Consequently \(B_k\) is
continuous and separately subharmonic. The products in its signed
predecessor have a conjugate, but their moduli equal the moduli of
the holomorphic products displayed in (5).

## 2. The distinguished-boundary estimate

For a continuous separately subharmonic function \(f\) on a
neighborhood of \(K\), iterating the one-variable maximum principle
gives
\[
                     \sup_K f\le\sup_{\partial_{\rm dist}K}f.
 \tag{6}
\]
Indeed first fix \(c_2,\ldots,c_d\) and maximize in \(c_1\)
over its boundary, then do the same in \(c_2\), and continue.
Continuity on the compact product makes each supremum legitimate.
The same argument holds when the function is separately subharmonic
on the interior and continuous up to the full product boundary.

Suppose the following bounds hold on all of (1), uniformly over
the fixed targets:
\[
                 D\le-\gamma,\qquad B_k\le B_{0k}\quad(1\le k\le d),
 \qquad \gamma>0,\quad B_{0k}\ge0.
 \tag{7}
\]
By (6), each response bound extends throughout \(K\).
For a disk or clipped disk \(K_k\) contained in the disk centered
at \(c_{0k}\) with radius \(R_k\), take
\[
 q_k(c_k)=\frac{B_{0k}}2
           (R_k^2-|c_k-c_{0k}|^2),\qquad
 C_k=\frac{B_{0k}R_k^2}{2}.
 \tag{8}
\]
For a rectangle whose imaginary interval is \([y_k^-,y_k^+]\),
take instead
\[
 \begin{split}
 q_k(c_k)&=B_{0k}(\Im c_k-y_k^-)(y_k^+-\Im c_k),\\
 C_k&=B_{0k}(y_k^+-y_k^-)^2/4 .
 \end{split}
 \tag{9}
\]
The real width may replace the imaginary width by using the same
formula in \(\Re c_k\). A narrower containing strip also suffices
when its barrier is nonnegative throughout \(K_k\).
In every case \(0\le q_k\le C_k\) on \(K_k\) and
\(\Delta_kq_k=-2B_{0k}\).

**Theorem 1.** Under (2), (4) and (7), using any mixture of the
barriers (8)--(9),
\[
                  D(c;x)\le-\gamma+\sum_{k=1}^d C_k
                    \qquad(c\in K).
 \tag{10}
\]
In particular, for a product of clipped disks the loss is
\(\tfrac12\sum_k B_{0k}R_k^2\).

*Proof.* Put \(W=D-\sum_kq_k\). For each \(k\), all the
other barriers are constant in \(c_k\), so (5)--(7) imply
\[
                 \Delta_kW\ge-2B_k+2B_{0k}\ge0.
 \tag{11}
\]
Thus \(W\) is separately subharmonic on the full product.
On its distinguished boundary the nonnegative barriers give
\(W\le D\le-\gamma\). Equation (6) yields \(W\le-\gamma\)
throughout \(K\), proving (10). The proof is applied before taking
any target supremum. It never differentiates an optimizer, a clipped
conjugate or a numerical majorant. \(\square\)

There is no assertion that \(D\) itself is separately subharmonic.
The constants in (7) are independent global bounds over the same
distinguished boundary. A cellwise association of a favorable phase
gap with a smaller local response is not a substitute for them.
Nor does a cover of a diagonal parameter slice, or of one boundary
coordinate with all others fixed at reference centers, cover (1).

If target concavity requires bounds on the imaginary parts of
holomorphic reference coordinates, uniform strict bounds on (1)
extend by the same iterated maximum and minimum principles.
This is available only after joint holomorphic existence and the
other whole-product domain conditions have been established.

## 3. Internal gluing cancels each directional response

Consider finitely many clusters, each satisfying the preceding
holomorphic, stationary and target-curvature hypotheses over the
same parameter product. Their reference coordinates are restrictions
of one global \(r(c)\). Each occurrence of a shared coordinate has
the same real target, fixed height and coefficient \(\lambda_j\).
The cluster phases have no additional explicit parameter dependence.

Write \(p_j^{(\ell)}\) for the boundary marginal of cluster
\(\ell\). Count all occurrences with their original multiplicities.
For every glued internal coordinate \(j\in G\), require the full
complex matching equation on a neighborhood of \(K\):
\[
                 \sum_{\ell:\,j\in B_\ell}p_j^{(\ell)}(c)=0.
 \tag{12}
\]
The local phase allocations must already include their own terms and
Fourier weights so that (12) is the original stationary matching
equation. Set \(P_j=\sum_{\ell:\,j\in B_\ell}p_j^{(\ell)}\)
at each remaining external coordinate \(j\in E_{\rm out}\).

**Corollary 2.** For \(D_{\rm tot}=\sum_\ell D^{(\ell)}\),
\[
 \Delta_kD_{\rm tot}
   =\sum_\ell A_{\ell,k}
      +2\Re\sum_{j\in E_{\rm out}}
          \lambda_j(\partial_{c_k}P_j)
                  \overline{\partial_{c_k}r_j},
 \qquad A_{\ell,k}\ge0 .
 \tag{13}
\]
Thus Theorem 1 applies with
\[
 B_k^{\rm out}
   =\sum_{j\in E_{\rm out}}
       \lambda_j|(\partial_{c_k}P_j)(\partial_{c_k}r_j)|.
 \tag{14}
\]

For each \(k\), sum the exact first lines of (5). Differentiate
(12) in \(c_k\); the common multiplier
\(\lambda_j\overline{\partial_{c_k}r_j}\) makes that internal
response vanish. Only then take absolute values. The affine
tangent terms at glued coordinates already cancel in \(D_{\rm tot}\)
because their targets are shared. The nonnegative Hessian forms
remain nonnegative after pulling them back to the global coordinates.
This proves (13)--(14) with no loss at a matched internal interface.

The result is indexed by the external boundary, not by the count of
clusters. It does not bound the numerical sizes of the remaining
derivatives independently of that count or of the number of external
parameters. Matching at a single point, different height coefficients
on a shared coordinate, or hidden explicit parameter dependence does
not satisfy the corollary.

This provides a possible several-boundary comparison for branched
pieces whose original reference family and phase domains satisfy the
hypotheses. It does not construct such families, prove boundary signs,
transport the original source cycle, or establish a nonzero observed
coefficient. In particular no arbitrary-short-filling stability or
finite-exception theorem follows from this analytic lemma alone.
