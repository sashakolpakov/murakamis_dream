# Relative homology and compact periods in a positive gluing chart

Research proof, 23 November 2026.

A supplied positive critical point determines the entire ordinary
relative homology of its positive logarithmic chart above a sufficiently
high sublevel. There is one compact Legendre disk, and its coefficient
in any finite relative cycle is an explicit angle-projection degree.
For a holomorphic growing period this gives its full leading term,
including the retained density and this integer coefficient.

This is a statement about finite chains in one fixed marked chart.
It does not provide such a representative for an original quantum
source, or identify its cut, lip or infinite boundary currents.

## 1. The marked potential and its radial minimum

Let \(t\geq1\), \(\Theta=(0,\pi)^t\), and write
\[
 X=\{x=\rho+i\theta:\rho\in\mathbb R^t,\ \theta\in\Theta\},
 \qquad P=P^{\mathsf T}\in M_t(\mathbb R),\qquad u=a+ib.
 \tag{1}
\]
Use the principal upper-half-plane branches in
\[
 S(x)=\sum_j\operatorname{Li}_2(e^{x_j})
             +\tfrac12x^{\mathsf T}Px-u^{\mathsf T}x,
 \quad v(x)=-\operatorname{Log}(1-e^x),\quad h=\Im S.
 \tag{2}
\]
Thus \(S_x=v(x)+Px-u\). Suppose a positive critical point
\(x_*=\rho_*+i\theta_*\in X\) is supplied. The fixed affine target,
quad choices and all logarithmic windings are part of (2). In the
gluing application [G] supplies exactly this potential after positive
quad selection. No existence assertion is implicit in this hypothesis.

Put
\[
 \beta(\theta)=b-P\theta,\qquad
 \gamma(\theta)=\pi\mathbf1-\theta-\beta(\theta),\qquad
 \mathcal P=\{\theta\in\Theta:\beta>0,\ \gamma>0\}.
 \tag{3}
\]
This is a convex open polytope. At the critical point
\(\beta_* =\Im v(x_*)\), and
\(\gamma_* =\pi\mathbf1-\theta_*-\Im v(x_*)\); both are positive.
Indeed \(z\) and \(z/(1-z)\) are in the upper half-plane, so the
three indicated arguments are the angles of their positive triangle.
In particular \(\theta_*\in\mathcal P\).

Direct differentiation gives
\[
 \begin{split}
 h(\rho,\theta)
   &=\sum_j\Im\operatorname{Li}_2(e^{\rho_j+i\theta_j})
                          -\rho^{\mathsf T}\beta-a^{\mathsf T}\theta,\\
 D&=\operatorname{diag}_j\Im v'(x_j)>0,\qquad
 \Im v'(x_j)=\frac{\Im(e^{x_j})}{|1-e^{x_j}|^2},\\
 h_{\rho\rho}&=D,\qquad h_{\theta\theta}=-D.
 \end{split}                                                   \tag{4}
\]
For fixed \(\theta\in\mathcal P\), the derivative
\(h_{\rho_j}=\Im v(x_j)-\beta_j\) increases from \(-\beta_j\)
to \(\gamma_j\) as \(\rho_j\) runs from \(-\infty\) to
\(+\infty\). Consequently its unique global radial minimum is
\[
 \rho_{L,j}(\theta)=\log\frac{\sin\beta_j(\theta)}
                                      {\sin\gamma_j(\theta)},
 \qquad x_L(\theta)=\rho_L(\theta)+i\theta.
 \tag{5}
\]
The formula follows from the sine rule, or by substitution in
\(\operatorname{Arg}(1-e^{x_j})=-\beta_j\). It is smooth on
\(\mathcal P\), and \(\rho_L(\theta_*)=\rho_*\).

For \(z_j=e^{x_{L,j}}\), the Bloch--Wigner identity yields
\[
 H(\theta):=h(x_L(\theta))
     =\sum_j D_{\mathrm{BW}}(z_j)-a^{\mathsf T}\theta.
 \tag{6}
\]
The real peripheral tilt in (6) is retained. The sum is a calibrated
hyperbolic volume only in an application supplying that calibration;
neither an imaginary additive constant nor this tilt is discarded.

For completeness, let \(S_{xx}=K+iD\), with \(K=K^{\mathsf T}\)
real. The real Hessian and its radial Schur complement are
\[
 \operatorname{Hess}h=\begin{pmatrix}D&K\\K&-D\end{pmatrix},\quad
 \rho'_L=-D^{-1}K,\quad H''=-D-KD^{-1}K<0,\quad
 J_L:=x'_L=-D^{-1}K+iI=-D^{-1}\overline{S_{xx}}.
 \tag{7}
\]
These formulas are the Legendre calculation of [L], equally valid
for complex \(u\). The matrix \(J_L\) is invertible: a complex
symmetric matrix with positive imaginary part has trivial kernel.
Thus \(H\) is strictly concave, with its unique maximum
\(h_*:=H(\theta_*)=h(x_*)\).

## 2. A cutoff retracts the whole pair

Define the fixed-radius height \(f(\theta)=h(\rho_*,\theta)\).
It is strictly concave on all of \(\Theta\), stationary at
\(\theta_*\), and extends continuously to \([0,\pi]^t\).
Here the dilogarithms have their upper-side boundary values; their
values remain continuous even when a boundary shape equals \(1\).
Every other point of this closed cube has strictly smaller height.
To see the boundary assertion, restrict to a segment from
\(\theta_*\): its derivative starts at zero and is strictly
decreasing at every interior point. Its endpoint limit is therefore
strictly smaller than its value at the center.

Choose levels
\[
 c_0<c<h_*,\qquad \{\theta\in\Theta:f(\theta)\geq c_0\}
                                      \Subset\mathcal P.
 \tag{8}
\]
Such levels exist by compactness of the closed cube and
\(\theta_*\in\mathcal P\). Choose a smooth cutoff \(0\leq\chi\leq1\)
depending only on \(f\), equal to zero for \(f\leq c_0\) and to
one for \(f\geq c\). Set
\[
 \rho_0(\theta)=\rho_*+\chi(\theta)(\rho_L(\theta)-\rho_*),\quad
 A_c=\{x\in X:h(x)\leq c\},\quad
 R_s(\rho,\theta)=((1-s)\rho+s\rho_0(\theta),\theta).
 \tag{9}
\]
Outside \(\mathcal P\) define \(\rho_0=\rho_*\). This is a smooth
global definition because the support of \(\chi\) is compact in
\(\mathcal P\). The maps \(R_s\) strongly retract \(X\) onto its
graph; we now verify that they preserve \(A_c\).

If \(f(\theta)\geq c\), the target \(\rho_0=\rho_L\) is the
global radial minimum. If \(f(\theta)<c\), radial convexity and
\(H(\theta)\leq f(\theta)\) show
\(h(\rho_0,\theta)\leq f(\theta)<c\); outside \(\mathcal P\)
this is the definition of \(\rho_0\). Thus a starting point of
\(A_c\) always has its target in \(A_c\). Radial convexity proves
the same for the whole joining segment. This proves a strong
deformation retraction of pairs, not just of two reference chains.

Moreover,
\[
 h(\rho_0(\theta),\theta)>c
       \quad\Longleftrightarrow\quad
 \theta\in\Omega_c:=\{\theta\in\mathcal P:H(\theta)>c\}.
 \tag{10}
\]
Indeed a high graph point must have \(f\geq c\), hence lies on the
Legendre graph; conversely \(H>c\) implies \(f>c\) and \(\chi=1\).
The graph pair is therefore \((\Theta,\Theta\setminus\Omega_c)\).
Notice also that (9) preserves every sublevel \(h\leq d\) for
\(d\geq c\). It need not decrease height monotonically below \(c\).

Strict concavity makes \(\Omega_c\) convex and nonempty. Since
\(H\leq f\), its closure lies compactly inside \(\mathcal P\).
It is exactly \(K_c=\{H\geq c\}\): every level point can be
approached along its segment to \(\theta_*\) from higher values.
On \(H=c\), the gradient is nonzero, since the only stationary
point is \(\theta_*\). Thus \(K_c\) is a smooth convex closed
\(t\)-ball, and \(\partial K_c=\{H=c\}\).

Clamp each ray from \(\theta_*\) to its intersection with
\(\partial K_c\), leaving points of \(K_c\) fixed. Linear
interpolation of the radial distance gives a strong deformation
of \((\Theta,\Theta\setminus\Omega_c)\) onto
\((K_c,\partial K_c)\). It stays in \(\Theta\) by convexity;
a point outside \(\Omega_c\) remains outside until it reaches
\(\partial K_c\). The radial intersection depends continuously
and smoothly on direction, since \(K_c\) is smooth and contains
\(\theta_*\) in its interior.

Combining this clamp with (9) proves
\[
 (X,A_c)\simeq (K_c,\partial K_c),\qquad
 H_j(X,A_c;\mathbb Z)=
 \begin{cases}\mathbb Z,&j=t,\\0,&j\ne t.\end{cases}
 \tag{11}
\]
The compact disk \(\Gamma_c=x_L(K_c)\), with its standard
\(\theta\)-orientation, is a generator, and its boundary has
height exactly \(c\). All homology here uses ordinary finite
singular chains. In particular no noncompact end is filled by
this calculation.

## 3. Its coefficient is an angle-projection degree

For every \(\rho\), radial minimality at \(\theta_*\) gives
\(h(\rho,\theta_*)\geq h_*>c\). Hence angle projection is a map
of pairs
\[
 \pi:(X,A_c)\longrightarrow
             (\Theta,\Theta\setminus\{\theta_*\}),\qquad
 \pi(\rho+i\theta)=\theta.
 \tag{12}
\]
It sends \([\Gamma_c]\) to the positive local fundamental class
at \(\theta_*\). Both groups in degree \(t\) are \(\mathbb Z\),
so \(\pi_*\) is an isomorphism. Consequently every finite relative
cycle \(\Gamma\) has the exact coefficient formula
\[
 [\Gamma]=k[\Gamma_c],\qquad
 k=\deg_{\theta_*}(\pi\Gamma)\in\mathbb Z.
 \tag{13}
\]
This degree means the induced local relative homology class.
For smooth transverse chains it is the signed count of intersections
with \(\{\theta=\theta_*\}\), counting the sign of the angle
projection on each oriented chain. This convention fixes the
intersection orientation without an additional ambient sign.

Since \(X\) is contractible and \(t\geq1\), every compact closed
\(t\)-cycle in \(X\) has zero class in (11). A nonzero generator
therefore needs a relative boundary in \(A_c\), or separately
controlled ends followed by a justified truncation. An entire compact
closed quantum cycle cannot simply be placed in this unpunctured
chart and assigned degree one.

## 4. The resulting compact-period formula

Let \(\Gamma\) be a finite piecewise-smooth relative \(t\)-cycle
in \((X,A_c)\). The retractions above and finite-chain homology
in the ball give compact piecewise-smooth chains \(B,R\) with
\[
 \Gamma-k\Gamma_c=\partial B+R,\qquad
 \operatorname{supp}R\subset A_c.
 \tag{14}
\]
One can triangulate the compact homotopies and the ball filling to
obtain these chains. The clamp is smooth on either side of its
boundary, so this needs only piecewise-smooth chains. Equivalently
use smooth approximation relative to the regular level \(h=c\).

Suppose, on a neighborhood of these compact chains, the actual forms
are holomorphic top forms
\[
 \omega_N=N^\mu e^{NS(x)/(2\pi i)}a_N(x)\,dx_1\cdots dx_t.
 \tag{15}
\]
Assume \(a_N\) is polynomially bounded on that neighborhood,
and \(a_N=a_0+O(N^{-1})\) uniformly holomorphically near \(x_*\),
where \(a_0(x_*)\ne0\). Holomorphic top forms are closed. Stokes
and (14) give the exact identity and the bound
\[
 \int_\Gamma\omega_N
      =k\int_{\Gamma_c}\omega_N+\int_R\omega_N,
 \qquad \left|\int_R\omega_N\right|
                   \leq N^C e^{Nc/(2\pi)}.
 \tag{16}
\]
The constant includes the finite volume of \(R\). No independent
bound on a noncompact homotopy or on its ends is used.

Write \(\varphi(\theta)=S(x_L(\theta))/(2\pi i)\). At the center
\(\varphi'=0\) and
\[
 \mathcal H=-\varphi''(\theta_*),\qquad
 \Re\mathcal H=-H''(\theta_*)/(2\pi)>0,\qquad
 C_*=(2\pi)^{t/2}
       \frac{a_0(x_*)\det J_L(\theta_*)}{\sqrt{\det\mathcal H}}\ne0.
 \tag{17}
\]
The square root is the Gaussian branch on matrices with positive
real part; the orientation is the stated \(\theta\)-orientation.
Strict concavity gives a fixed height gap outside every small
neighborhood of \(\theta_*\) in \(K_c\). Taylor expansion there,
Gaussian rescaling and the positive real Hessian in (17) give
\[
 \int_\Gamma\omega_N
   =k\,C_* N^{\mu-t/2}e^{NS(x_*)/(2\pi i)}(1+O(N^{-1}))
                      +O(N^C e^{Nc/(2\pi)}).
 \tag{18}
\]
The local estimate uses the uniform holomorphic expansion of the
amplitude; its derivative bounds follow on a smaller neighborhood
by Cauchy estimates. Odd Gaussian terms integrate to zero, and
the remaining Taylor error is \(O(N^{-1})\). The complement is
exponentially smaller by the fixed height gap. Thus if \(k\ne0\)
the period has its retained nonzero leading constant. If \(k=0\),
(16) instead gives the lower sublevel bound directly.

## 5. What this does and does not assemble

[L] constructs the Legendre chain and controlled homotopies of
specified reference chains. Here the cutoff controls the whole
positive-chart pair and computes the coefficient of every finite
relative chain by (13); (18) then assembles its compact period.
The argument works for the tilted height in (6), without assuming
purely imaginary peripheral targets or using a descent flow.

It does not show that an original Kashaev cycle, with its actual
amplitude and closing row, has a representative satisfying these
hypotheses. Quantum divisors, cut banks, finite flat faces and
noncompact ends may supply additional chains outside this pair.
Their actual marks and boundary currents must be retained. Different
logarithmic windings give different potentials, not additional
classes silently identified by (11). No source degree, scalar
lower bound for a knot, or finite-exception theorem follows without
the corresponding original-source construction.

## Complete direct sources

- [L] [Global Legendre contour](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/general_legendre_rivin_contour.md), 421 lines, SHA-256 `b51be11036b05fbccd586c2d0a4505559631870357cf128dd256dcc87e26970b`: the off-critical Legendre identity, Hessian and local period calculation. The whole-pair and projection-degree arguments are supplied above.
- [G] [Positive gluing gradient bound](research_positive_gluing_gradient_escape_bound.md), 226 lines, SHA-256 `60de078745893f5f3bb2b9491a974cc31cfe99bf54000d99f77672c374d5c779`: the actual marked potential and positive quad convention. Its gradient-flow conclusion is not a premise of (9)--(18).
