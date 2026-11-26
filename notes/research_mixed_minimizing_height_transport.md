# Minimizing-height transport on a common source box

Research proof, 4 November 2026. This gives a canonical constrained
height graph on a common complex source box, its exact transport law,
and two obstructions to extending that conclusion to shrinking height
fibers. The complete finite-source hypotheses are kept explicit.

## 1. A common-box theorem, including constrained faces

Let \(X\subset\mathbb R^m\) be a compact convex box and let
\(Y=\prod_j[\ell_j,u_j]\) be a compact height box with nonempty
interior. Let \(\Phi\) be holomorphic on a neighborhood of
\(X+iY\), with its already specified logarithmic lift. Write
\[
 U(x,h)=\Re\Phi(x+ih),\qquad \Phi''=-A+iB,
 \qquad A\ge aI>0,\quad \|B\|\le b
 \tag{1}
\]
throughout this common product. Here \(A,B\) are real symmetric
matrices; the constants are uniform on the product.

**Theorem 1.** There is a unique constrained minimizer
\[
 h(x)=\operatorname*{argmin}_{h\in Y}U(x,h),\qquad
                         v(x)=U(x,h(x)).
 \tag{2}
\]
The map \(h\) is Lipschitz with constant at most \(b/a\).
The function \(v\) is continuously differentiable with Lipschitz
gradient and is strongly concave with constant \(a\). If
\(z_*=x_*+ih_*\in X+iY\) is an original critical point,
\(\Phi'(z_*)=0\), then \(h(x_*)=h_*\) and
\[
                v(x)\le\Re\Phi(z_*)-\frac a2|x-x_*|^2.
 \tag{3}
\]
The assertion does not require every minimizer to lie in the
interior of the height box.

The Cauchy--Riemann identities, with signs retained, are
\[
 U_x=\Re\Phi',\quad U_h=-\Im\Phi',\quad
 U_{xx}=-A,\quad U_{hh}=A,\quad U_{hx}=U_{xh}=-B.
 \tag{4}
\]
Compactness and strict height convexity give existence and uniqueness
in (2). The two minimizing variational inequalities, combined with
\(U_{hh}\ge aI\), give
\(a|h(x)-h(x')|\le b|x-x'|\). The unique-minimizer envelope
identity gives \(v_x=U_x(x,h(x))\); together with (4) and the
Lipschitz bound, this proves the stated gradient regularity.

For fixed \(h\), the function \(U(\cdot,h)\) is strongly concave.
The common feasible set is essential in the following argument:
\[
 \begin{split}
 v(tx+(1-t)x')
 &=\min_{h\in Y}U(tx+(1-t)x',h)\\
 &\ge t v(x)+(1-t)v(x')
                +\frac a2t(1-t)|x-x'|^2.
 \end{split}
 \tag{5}
\]
At the original critical point, height convexity identifies its
height with the minimizer, and \(v_x(x_*)=0\). This proves (3).

On an open region where a fixed set \(F\) of height coordinates
is free and all other coordinates are fixed at box endpoints,
the implicit equations are \(\Im\Phi'_F=0\). Consequently
\[
 (Dh)_F=A_{FF}^{-1}B_{F,*},\qquad (Dh)_{F^c}=0,
 \qquad
 v''=-A-B_{*,F}A_{FF}^{-1}B_{F,*}.
 \tag{6}
\]
For a wholly interior minimizer this is exactly
\[
             Dh=A^{-1}B,\qquad
             v''=-(A+B A^{-1}B).
 \tag{7}
\]
No differentiability of the active set across its changes is needed
for (5). In particular (7) is not used on a constrained face.

## 2. Usable existence tests for an interior transported graph

The constrained graph always exists under (1). It is interior
throughout a real subbox if the height-gradient component is
strictly negative on each lower height face and strictly positive
on each corresponding upper face, uniformly over the other
coordinates. These face inequalities rule out every constrained
minimizer on the boundary and are direct derivative tests.

There is also a residual test that does not require all box faces.
If the Euclidean height ball \(\overline B(h_0,r)\) lies inside
\(Y\) and
\[
                    |\Im\Phi'(x+ih_0)|<ar,
 \tag{8}
\]
then its height-gradient points strictly outward on the ball
boundary. The minimum on that ball is interior and hence is the
unique minimizer on \(Y\). At a known interior root \((x_0,h_0)\),
the sufficient condition \(b|x-x_0|<ar\) follows from (4).
Thus a compact source neighborhood, its height margin and two
explicit derivative bounds give a quantitative transport radius.
Continuing (7) is valid only while such a common source region and
an interior-height condition remain available.

## 3. Literal finite-source bounds and an exact periodic contour

Suppose additionally that the original finite Laurent density has
the uniform upper bound
\[
       |\mathcal F_N(e^{-2\pi iz})|
                  \le C N^q e^{N\Re\Phi(z)},\qquad z\in X+iY.
 \tag{9}
\]
This must come from the complete finite kernels and actual Fourier
weights. Root holomorphy is not a substitute. Then its value on the
minimizing graph has the literal bound
\[
 |\mathcal F_N(e^{-2\pi i(x+ih(x))})|
 \le C N^q
     e^{N(\Re\Phi(z_*)-a|x-x_*|^2/2)}.
 \tag{10}
\]
Where a source theorem supplies only a uniform additional rate
\(\delta\), that same \(\delta\) must be retained in (9)--(10).

For a compact patch lying inside a real fundamental cube, extend
the Lipschitz function \(h\) to a slightly larger cube, multiply
by a fixed Lipschitz cutoff equal to one near \(X\), and periodize
the resulting function with support away from the cube's boundary.
This gives a periodic Lipschitz graph \(H\) agreeing with \(h\)
on the patch. The exact
[coupled contour identity](research_mixed_coupled_outer_graph.md)
then reads
\[
 \operatorname{CT}\mathcal F_N
 =\int_{\mathbb T^m}\mathcal F_N(e^{-2\pi i(x+iH(x))})
                                      \det(I+iDH(x))\,dx.
 \tag{11}
\]
For completeness, the identity for a Lipschitz graph follows by
periodic smoothing: the derivatives converge in every finite
\(L^p\), uniformly bounded, so each Jacobian minor converges in
\(L^1\). Apply the closed holomorphic-form identity to the smooth
graphs and take the limit for each fixed finite Laurent polynomial.
No added current or determinant-nonvanishing assumption appears.
On the optimized patch,
\[
                  |\det(I+iDh)|\le(1+(b/a)^2)^{m/2}
 \tag{12}
\]
almost everywhere. The extension has its own finite bound, independent
of \(N\). Equation (10) says nothing about that extension region.

If \(h_*\) is interior and the original density has a nonzero local
packet, the minimizing graph is smooth near the critical point and
preserves its original Gaussian coefficient. Indeed, put
\(T=I+iA_*^{-1}B_*\). It is invertible, since \(A_*^{-1}B_*\)
is similar to a real symmetric matrix. Exactly
\[
 \Phi''_*T=-(A_*+B_*A_*^{-1}B_*),\qquad
 \det(-T^T\Phi''_*T)=\det(T)^2\det(-\Phi''_*).
 \tag{13}
\]
The graph Jacobian cancels the transformed Gaussian determinant,
with the branch fixed by the local oriented deformation. All original
scalar carriers and powers of \(N\) therefore remain unchanged.

This is already applicable on the proved unselected plateau product:
take \(X=[.22,.45]^m\), type-three heights \([-.03,.02]\), and
type-four heights \([-.057,0]\). The
[full reset theorem](research_mixed_full_height_reset.md)
gives positive allocated Hessians on every block and the actual
whole conditional packets. Summing the original edge incidences
gives (1) for the total phase, including lengths one and two.
On the compact four-type height product,
\(\nu=-\Re g>0\), so the
[Fourier comparison](research_mixed_fourier_weight_continuation.md)
is relative and (9) has no rate tolerance. If needed, a sufficiently
small enlargement of this compact box preserves the strict source,
curvature and relative-weight inequalities and places the fixed
geometric height in its interior. Thus the theorem gives an actual
optimized plateau contour, with the original \(N^0\) coefficient.
It does not enlarge the existing source box into the left transition.

The [complex stability theorem](research_mixed_real_packet_complex_stability.md)
also gives common small source boxes over every real compact bounded
away from zero. These yield (9) whenever the actual Fourier branches
agree with the chosen phase. They need not contain the original
geometric heights; without that inclusion, (3) does not compare their
minimum to the original geometric action.

## 4. Convex shrinking tubes do not suffice

Even a convex complex tube, strict real accretivity and an interior
geometric critical point do not imply concavity of the minimum over
variable fibers. Take
\[
 \Phi(z)=-(z-1)^2-3iz,\qquad
 0\le x\le2,\quad -2x\le h\le0.
 \tag{14}
\]
Here \(A=2\), \(B=0\), and the critical point is
\(z_*=1-3i/2\), interior to the tube. The height minimizer is
\(h(x)=-2x\) for \(0\le x<3/4\), so
\[
 v(x)=3x^2-4x-1,
 \qquad v''(x)=6>0,
 \qquad v(0)=-1>\Re\Phi(z_*)=-9/4.
 \tag{15}
\]
Thus (5) cannot be reused with an \(x\)-dependent feasible set,
even if its total domain is convex. Active sloping faces require
their own tilted-Hessian or boundary-action comparison.

## 5. An original type-four height-transport obstruction

The issue is present in the original phase, not only in (14).
For the homogeneous type-four block define
\[
 \Psi(z)=\phi_{11}(z,z),\qquad
 P_0=2+i/2,\qquad
 z_0=\frac1{2\pi i}\Log\frac{P_0+i}{P_0-i}=x_0+ih_0.
 \tag{16}
\]
The boundary value has \(\Im\cot\pi z_0=1/2\), with
\[
 .14<x_0<.15,\qquad -.031<h_0<-.030.
 \tag{17}
\]
At this fixed real coordinate the open global cotangent fiber is
\((-w(x_0),w(x_0))\), where
\[
 w(x)=\frac1{2\pi}
 \log\left(\sqrt{\cos^2(2\pi x)+3}-\cos(2\pi x)\right),
 \qquad h_0=-w(x_0).
 \tag{18}
\]
Indeed \(|\Im\cot\pi(x+ih)|<1/2\) is equivalent, for
\(t=e^{2\pi|h|}\ge1\), to
\(t^2+2\cos(2\pi x)t-3<0\).

The original selected inner cotangent at the boundary is the root
near \(.46276746+.41841397i\) of the exact rational polynomial
\[
 F(S)=S^3+(4+2i)S^2+(11/4+6i)S+2-23i/4.
 \tag{19}
\]
A rational Rouché disk of radius \(10^{-4}\) about
\(46277/100000+i\,41841/100000\) contains exactly one root.
It lies strictly in \(\Re S>0,\ |\Im S|<1\). For parameters
\(P=Q=2+i(1/2-\varepsilon)\) sufficiently near the boundary,
the nearby root is the unique global selected root. Its limit
therefore fixes the original logarithmic lift at (19).

Writing \(s_0=\Log((S+i)/(S-i))/(2\pi i)\), the literal outer
derivative is
\[
 \Psi'(z_0)=2g'(s_0+z_0)+2\pi i s_0-3g'(z_0),
 \qquad
                    -\Im\Psi'(z_0)>1/2.
 \tag{20}
\]
The checker encloses this on the whole Rouché disk, not at a
floating root. All arguments remain in their original regular strips.
The certified derivative is approximately \(.57015\).

Throughout the open fiber (18), the
[global cotangent theorem](research_mixed_global_cotangent_roots.md)
gives the original root and positive allocated Schur form. Hence
\(\partial_h^2\Re\Psi(x_0+ih)>0\). Continuity from (20) implies
\(\partial_h\Re\Psi>1/2\) throughout that entire fiber.
There is no interior solution of the minimizing-height equation
there: its infimum is approached at the lower boundary. This also
rules out an interior height-stationary point on any homogeneous
four-type cycle with every real coordinate equal to \(x_0\).
Indeed strict height convexity gives uniqueness, so cyclic symmetry
would force all its heights to be equal, contradicting (20).

This is an obstruction to transporting an unconstrained minimizing
height inside the stated global cotangent domain. It is not a failure
of the finite conditional asymptotic, not an outer-integral lower
bound obstruction, and not a claim that a different contributing
contour cannot work. The common-box theorem remains valid; extension
through shrinking transition fibers needs new active-face and source
estimates.

## 6. Reproduction

    python3 experiments/check_mixed_minimizing_height_transport.py --precision 256

The checker verifies exact transport/completion identities, the
variable-fiber example, the original rational cubic and a strict
Rouché enclosure, and outward bounds for the derivative in (20).
The compact minimization and finite-contour arguments are the
analytic proof above; no word sampling is used.
