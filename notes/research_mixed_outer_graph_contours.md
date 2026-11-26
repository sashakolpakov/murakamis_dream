# Exact periodic graph contours for the mixed outer source

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note implements a single periodic contour that preserves the proved
central conditional domain and reaches height zero on the right
half-period. It keeps every finite kernel, Fourier weight and selected
alias. The transition-source estimates remain a separate obligation.

## 1. Exact deformation of every alias term

Use the global Laurent kernels and polynomial weight from the
[exact torus identity](research_mixed_conditional_torus_composition.md).
After expanding the product of the factors \(1+X_j^{-N}\), fix any
alias subset \(S\) of the four-type variables. Its integrand
\(F_{N,S}(X_1,\ldots,X_m)\) is a Laurent polynomial on
\((\mathbb C^\times)^m\). In particular the apparent denominators
in interpolation expressions for \(d_N\) are removable.

Let \(h_j:\mathbb R/\mathbb Z\to\mathbb R\) be continuous and
piecewise continuously differentiable, with bounded derivatives on
their pieces. Put
\[
 z_j(x)=x+i h_j(x),\qquad X_j(x)=e^{-2\pi i z_j(x)}.
 \tag{1}
\]
Then the exact constant-term integral is
\[
 \operatorname{CT}F_{N,S}
  =\int_{[0,1]^m}F_{N,S}(X_1(x_1),\ldots,X_m(x_m))
                 \prod_{j=1}^m(1+i h'_j(x_j))\,d\mathbf x .
 \tag{2}
\]
The normalization \(\kappa^{m+k}N^{m+k}\) of the original torus
identity is unchanged. Thus the graph deformation applies separately
to every alias subset before any absolute estimate.

For one variable, \(X(x)\) winds clockwise once. The pullback
\(dX/(2\pi iX)=-dz\), together with this reversed orientation,
gives the plus sign in (2). Equivalently, the integral of
\(e^{-2\pi i\ell z}dz\) is one for \(\ell=0\) and zero for every
nonzero integer \(\ell\), by its entire periodic primitive.
Expand the finite Laurent polynomial and apply this statement
successively to prove (2).

There are no additional vertical boundary pieces. More explicitly,
the homotopy from a constant height \(c_j\) to \(h_j\),
\[
 h_{j,\theta}(x)=(1-\theta)c_j+\theta h_j(x),
                  \qquad 0\le\theta\le1,
 \tag{3}
\]
is periodic; the two vertical sides of a fundamental strip cancel.
Corners between smooth pieces cancel internally. This argument uses
the original finite Laurent polynomial, not a factorial approximation
across a branch cut. It also applies to the exact open-word
integrands, whole ordinary boundary polynomials and all fixed ordinary
derivatives in the torus note. It supplies no new bound on those
boundary polynomials.

## 2. A concrete central-preserving taper

Define the periodic, continuous, piecewise quadratic function
\[
 \chi(x)=
 \begin{cases}
 16x^2,&0\le x\le1/4,\\
 1,&1/4\le x\le2/5,\\
 100(1/2-x)^2,&2/5\le x\le1/2,\\
 0,&1/2\le x\le1 .
 \end{cases}
 \tag{4}
\]
For an unselected variable let \(c_j\) be its actual critical height.
For a selected four-type alias set \(c_j=7/500=.014\).
The proved geometric ranges give \(|c_j|\le57/1000\).
Take
\[
                         h_j(x)=c_j\chi(x).
 \tag{5}
\]
This retains the original or selected constant height on
\([1/4,2/5]\), equals zero on the whole right half-period, and
joins periodically at height zero at the seam. It is not necessary
to smooth its two derivative corners to use (2).
Moreover \(|\chi'|\le20\), so
\[
 |1+i h'_j|
 \le\sqrt{1+(57/50)^2}<38/25 .
 \tag{6}
\]
For each fixed word, the entire graph Jacobian is therefore bounded
independently of \(N\); it introduces no exponential rate.

The whole right-half source reduction
[proved separately](research_mixed_right_half_source_reduction.md)
applies to the zero-height portion of (5), with the actual
Fourier polynomial and selected aliases retained. Its supporting-plane
comparison is not a premise or conclusion of this note.

## 3. The left taper preserves the pair-Hessian condition

For \(z=x+ih\), \(0<x<1/2\), the elementary identity
\[
 |\Im\cot(\pi z)|<1
       \quad\Longleftrightarrow\quad
       \cos(2\pi x)<e^{-2\pi|h|}
 \tag{7}
\]
follows from
\(\Im\cot(\pi z)=-\sinh(2\pi h)/
[\cosh(2\pi h)-\cos(2\pi x)]\).
For \(0<x<1/4\), integration of \(\tan t\ge t\) gives
\[
 -\frac{\log\cos(2\pi x)}{2\pi}\ge\pi x^2,
 \qquad |h_j(x)|\le\frac{114}{125}x^2<\pi x^2.
 \tag{8}
\]
For \(1/4\le x<1/2\), (7) holds at every finite height.
Thus every graph point with \(0<x<1/2\) satisfies (7).

In particular let \(s,a\) have real parts in \((0,1/2)\) and
satisfy (7), and use the original pair phase
\(V(s,a)=g(s+a)-g(s)-g(a)\). Writing
\(\cot\pi s=u+iv,\ \cot\pi a=p+iq\), we have \(u,p>0\)
and \(|v|,|q|<1\). Its exact negative real Hessian obeys
\[
 \det(-\Re V''/\pi)
  =\frac{(u+p)^2-(pv-uq)^2}
          {(u+p)^2+(v+q)^2}>0 .
 \tag{9}
\]
Both diagonal entries are positive as well: a positive determinant
forces \(\Re\cot\pi(s+a)<up/(u+p)<\min(u,p)\).
Consequently this pair form is positive definite. This includes
the actual critical internal legs paired with any left-half graph
point, using their proved type-three and type-four rectangles.
It is a pointwise ambient Hessian assertion.

It is **not** concavity of the phase restricted to the curved graph.
Already in one variable, for a holomorphic phase \(\Phi\),
\[
 \frac{d^2}{dx^2}\Re\Phi(x+i h(x))
  =\Re\{\Phi''(x+i h)(1+i h')^2
                         +i h''\Phi'(x+i h)\}.
 \tag{10}
\]
The extra terms have no sign supplied by (9).

## 4. What the contour does and does not finish

The whole central source and its alias estimates apply unchanged on
\([1/4,2/5]^m\). The exact outer source is now represented on one
closed periodic graph, with no added endpoint integral. Nevertheless
the strips \(0<x<1/4\) and \(2/5<x<1/2\) contain full original
conditional kernels at parameter values outside that central source
theorem. Neither (9) nor continuity proves the required uniform
source bounds across those strips. Taking absolute values of every
internal summand can also lose the calibrated geometric rate.

A valid next comparison must keep the actual complex supporting
planes, the true \(d_N\) envelope (including its forcing branch),
and every selected factor \(X_j^{-N}\) throughout those transitions.
The periodic graph removes a contour-boundary issue; it does not
remove the exterior cancellation issue. No global mixed-word
asymptotic or new ordinary-boundary estimate is claimed.

## 5. Reproduction

Run

    python3 experiments/check_mixed_outer_graph_contours.py

The checker verifies the exact taper matching, derivative and Jacobian
budgets, the pair determinant algebra, the graph-chain-rule identity
and the Fourier primitive normalization. The analytic integration and
strict pair argument are the proofs above; the checker is not a
numerical contour-dominance certificate.
