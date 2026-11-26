# A selected plateau leg next to a real height reset

Research note, 4 November 2026. This estimates a boundary block between
a reset plateau coordinate and a selected plateau coordinate. It uses
the whole original conditional source and both actual Fourier branches.

Let \(P=[11/50,9/20]\), \(H=7/500\), and use the original allocated
phase and reference plane
\[
 \begin{split}
 \phi_{\eta\epsilon}(a,b)
 &=Q_\epsilon(s_*(a,b);a,b)
             -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \Gamma_r(z)&=\phi(r)+\phi'(r)\cdot(z-r),\qquad
 r\in R_{3+\eta}\times R_{3+\epsilon},\\
 R_3&=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \end{split}                                                   \tag{1}
\]
All primitives, logarithmic lifts and finite functions are exactly
those of the [selected-source theorem](research_mixed_selected_right_taper_support.md).
Write \(\ell\) for the selected coordinate, numbered zero or one.
The four patterns \((\eta,\epsilon,\ell)\) are
\[
                  (0,1,1),\ (1,1,1),\ (1,0,0),\ (1,1,0).
                                                               \tag{2}
\]
The selected target has height \(H\); the other target is real.
Both target real parts belong to \(P\), independently of the reference.

For \(f=0,1\), put
\[
 \psi_f(z)=\phi(z)+\tfrac f2 g(z_\ell)
                            +\pi i(1-f)z_\ell.                \tag{3}
\]

**Theorem 1.** Uniformly in all references, targets and patterns
above, both branches satisfy
\[
                 \Re\{\psi_f(z)-\Gamma_r(z)\}<-1/100.
                                                               \tag{4}
\]
For the original full Laurent kernel and polynomial Fourier weights,
the allocated finite block obeys
\[
 |C_{\epsilon,N}(X,Y)|
 |d_N(X)X^{-N\sigma_a}|^{\eta/2}
 |d_N(Y)Y^{-N\sigma_b}|^{\epsilon/2}
 \le C N^A e^{N(\Re\Gamma_r(z)-1/200)}.                       \tag{5}
\]
Here the selected indicator at coordinate \(\ell\) is one.
If the real reset coordinate is type four, its indicator may be either
zero or one. Its selected factor has modulus one at the real target.
The estimate holds at both parities for all sufficiently large levels.

## Strong real concavity, used without the old taper comparison

The [full right-square source theorem](research_mixed_unselected_right_taper_products.md)
gives the original holomorphic root and the entire nonzero canonical
packet on a neighborhood of every target and reference product here.
Lemma 2 of the selected-source theorem proves, on larger independent
target boxes containing all the present targets,
\[
                         -\Re\psi_f''>\tfrac54 I.             \tag{6}
\]
Only this curvature result and the full source are used. Its separate
support comparison requiring a taper coordinate is not invoked.

For a fixed reference, define the real target defect
\(F_r(x)=\Re(\psi_f(x+i h)-\Gamma_r(x+i h))\), with fixed
heights \(h_\ell=H\) and \(h_{1-\ell}=0\).
At any point \(c\in P^2\), Taylor's theorem and (6) give
\[
 \max_{x\in P^2}F_r(x)
 \le F_r(c)+\sum_{j=0}^1
       \max_{v\in[11/50-c_j,9/20-c_j]}
                   \{G_jv-\tfrac58 v^2\},
 \quad G_j=\partial_{x_j}F_r(c).                              \tag{7}
\]
The scalar maxima retain both interval endpoints and the possible
interior critical point. An optimizer may propose \(c\), but the
certificate accepts only the outward right side of (7).

The target heights and real square are independent of the references.
At each fixed target, \(-\Gamma_r(z)\) is holomorphic on a neighborhood
of the whole reference product. The repeated maximum principle thus
reduces its real part to sixteen products of rectangle sides. The
four patterns and two Fourier branches require 128 two-real-parameter
reference products. Each reference product has an exact prefix-free
dyadic cover of total area one.

On a reference cell, the checker verifies an affine Newton self-map
for the original logarithmic root and a separate point root at the
cell center. At its rational target point it verifies another original
logarithmic Newton self-map. The mean-value bound uses the exact identity
\[
                  d_r\Gamma_r(z)=\phi''(r)(z-r)\,dr,           \tag{8}
\]
and the target gradient uses the entire reference-root enclosure.
Every cell checks the right side of (7) is strictly less than
\(-1/100\). No floating objective value is an acceptance test.
The saved-cover mode uses only rational witnesses and proposes neither
new roots nor new target points. This proves (4) on the full products.

## Actual Fourier weights and finite normalization

For the selected positive height the allocated Fourier upper rate is
\[
          \tfrac12\max\{-\Re g(z_\ell),2\pi H\}-\pi H.
                                                               \tag{9}
\]
Combining this with the original kernel phase gives precisely
\(\max_{f=0,1}\Re\psi_f\). The forcing branch is retained even
where it dominates the reciprocal-factorial branch. At the real
reset coordinate, \(-\Re g(x)>0\) throughout the compact interval
\(P\), so its original Fourier weight has the relative factorial
asymptotic. A selection there has modulus one.

The full right-square packet bounds the literal kernel with its
nonzero original coefficient, all finite rows and every conditional
cotangent current. Apply the actual Fourier upper bound with a
sufficiently small fixed tolerance and absorb it in the reserve
between \(1/100\) and \(1/200\). This proves (5), with all original
level powers included in the fixed polynomial. The half-powers are
real moduli; in cyclic products their two incidences recombine into
the original integer weights and selected factors.

The result is a comparison for the indicated plateau boundary block.
It alone does not estimate an entire selected low/plateau cluster,
transition region or full outer period.

## Reproduction

    python3 experiments/certify_mixed_selected_reset_plateau_support.py --precision 256

    python3 experiments/certify_mixed_selected_reset_plateau_support.py --precision 320 --input repro/results/research-mixed-selected-reset-plateau-support.json --output /tmp/research-mixed-selected-reset-plateau-support-review.json
