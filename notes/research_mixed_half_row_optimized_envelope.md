# An optimized envelope for the half-row certificate

Research method, 5 November 2026. This note gives a different rigorous
whole-cell upper test for the
[half-row certificate design](research_mixed_half_row_support.md).
It keeps the original phase, both halfweights, both conditional
orientations and the same ordinary reference faces. It proves an
analytic acceptance rule, not a uniform negative sign. No checker,
saved tree or partial record is changed here.

## 1. The target maximum and a stronger curvature bound

Use the original notation
\[
\begin{split}
 F(v;a,b)={}&g(v+a)+g(v+b)-(2+\epsilon)g(v)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi iav,\\
 \phi(Z)&=F(s_*;Z),\qquad Z=(a,b)=U+iH,\qquad
 I=[11/50,9/20],\quad \kappa=1/2500000,\\
 D(Z,X)&=\Re F(1/2;X+iH)-\Re\phi(Z)
       -\Re\phi'(Z)\cdot(X-U)+\kappa\|X-U\|^2,\\
 V(Z)&=\max_{X\in I^2}D(Z,X).
\end{split}
\tag{1}
\]
The critical value and all its derivatives use the original
zero-lift branch. The admitted ordinary references and their
holomorphic local neighborhoods are those of the existing design.
The height bounds used below are \(|H_i|\le3/25\).

The two target coordinates in \(D\) separate exactly. In particular
their mixed second derivative vanishes. The chirp at the fixed real
index is independent of the target real coordinate, but remains in
the value and in derivatives with respect to the reference height.

For \(f(x)=\Re\{g(x+1/2+ih)-\lambda g(x+ih)\}\),
\(x\in I\), \(|h|\le3/25\) and \(\lambda\ge1\), the exact
half-period identity gives
\[
 -f''(x)=
 \frac{2\pi sC}{s^2+C^2-1}
       +(\lambda-1)\pi\Re\cot\pi(x+ih),
 \quad s=\sin(2\pi x),\quad C=\cosh(2\pi h).
\tag{2}
\]
The existing outer-strip bounds give \(3/10<s\le1\) and
\(1\le C<4/3\). The extra cotangent is nonnegative.
For fixed \(s\), the first fraction without \(2\pi\) decreases
with \(C\), since its derivative has numerator
\(s(s^2-C^2-1)<0\). At \(C=4/3\) it is
\(12s/(9s^2+7)\); its only interior critical point is a maximum.
Its endpoint values on \([3/10,1]\) are \(360/781\) and
\(3/4\). Thus, using \(\pi>157/50\),
\[
 -f''(x)>\frac{720\pi}{781}>\frac{14}{5},
 \qquad D_{X_iX_i}<-c,
 \qquad c=\frac{14}{5}-2\kappa>0.
\tag{3}
\]
This is uniform on the full auxiliary height range, not only the
smaller actual-height range. The separable target function has a
unique maximizer \(X^*(Z)\in I^2\).

## 2. An enclosure of every clipped optimizer

Fix a reference parameter cell and one rational trial
\(\widehat X\in I^2\). Suppose outward intervals
\([\underline\beta_i,\overline\beta_i]\) enclose
\(D_{X_i}(Z,\widehat X)\) throughout that cell. Then every
optimizer in the cell lies in the following product of intervals:
\[
 \mathcal X_i=I\cap
 \left[\widehat X_i-\frac{[-\underline\beta_i]_+}{c},
       \widehat X_i+\frac{[\overline\beta_i]_+}{c}\right],
 \qquad [r]_+=\max(r,0).
\tag{4}
\]

To prove this, fix a reference and one coordinate. If
\(x^*>\widehat x\), the derivative at \(x^*\) is zero at an
interior maximum or nonnegative at the upper endpoint. Since the
derivative decreases at rate at least \(c\),
\(D_x(\widehat x)\ge c(x^*-\widehat x)\).
If \(x^*<\widehat x\), the derivative at \(x^*\) is zero or
nonpositive at the lower endpoint, giving
\(D_x(\widehat x)\le-c(\widehat x-x^*)\).
Equality of the two points requires no sign condition. These
inequalities prove (4), including trials and optimizers on either
endpoint.

This coordinatewise argument uses separability. A general jointly
strongly concave function would not justify (4) merely from its
gradient at one target point. Here the original half-row expression
in (1) has precisely the required separation.

## 3. Differentiating the maximum, including clipping transitions

The unique optimizer is continuous in the reference. Indeed, any
convergent subsequence of maximizers along converging references
has, by compactness of \(I^2\) and continuity of \(D\), a limit
maximizing the limiting target function. Uniqueness identifies that
limit and proves continuity of the entire sequence.

On the admitted reference domain, \(V\) is continuously
differentiable, with the same conclusion on sufficiently small
local neighborhoods where the original phase and strict target
curvature persist. This includes points where a maximizing
coordinate enters or leaves an endpoint of \(I\).
For a small reference displacement \(e\), write
\(X_0=X^*(Z)\) and \(X_e=X^*(Z+e)\). The elementary sandwich is
\[
 D(Z+e,X_0)-D(Z,X_0)
 \le V(Z+e)-V(Z)
 \le D(Z+e,X_e)-D(Z,X_e).
\tag{5}
\]
First-order expansion in the reference is uniform for targets in
the compact square. Since \(X_e\to X_0\), both bounds in (5)
equal \(D_Z(Z,X_0)e+o(\|e\|)\). This proves differentiability;
continuity of \(D_Z\) and \(X^*\) proves continuity of the
derivative. No derivative of the possibly nondifferentiable
optimizer is required. On a closed parameter face the same formula
holds by restriction, with one-sided parameter limits at its ends.

More explicitly, put
\[
 P=\phi'(Z),\qquad H_\phi=\phi''(Z),\qquad
 d=X^*(Z)-U,\qquad
 P_c=F_X(1/2;X^*(Z)+iH).
\tag{6}
\]
The reference partial derivatives of \(D\), holding its target
fixed, are the unchanged identities
\[
 D_U=-\Re(H_\phi d)-2\kappa d,
 \qquad D_H=\Im(P-P_c+H_\phi d).
\tag{7}
\]
For any real parameter \(\xi_j\) of the ordinary reference face,
the envelope derivative is therefore
\[
 V_{\xi_j}
 =D_U\cdot\Re Z_{\xi_j}
              +D_H\cdot\Im Z_{\xi_j},
 \quad\text{evaluated at }X=X^*(Z).
\tag{8}
\]
The derivative of \(X^*\) contributes no term. The original
coupled-root response still supplies \(Z_{\xi_j}\), and the same
complex Schur complement supplies \(H_\phi\). In particular the
first-argument chirp, the own denominator power and the two
different outer allocations remain in (6)--(8).

## 4. A whole-cell acceptance rule

Let the exact parameter box be centered at \(\xi^0\), with
halfwidths \(h_j\), and let \(Z_0=Z(\xi^0)\). Obtain an
outward upper bound \(M_0\ge V(Z_0)\) from the tiny original-log
midpoint root disk. One permitted construction uses the same
rational trial \(\widehat X\): enclose the *midpoint* target
slopes by \([\underline\beta_i^0,\overline\beta_i^0]\), then set
\[
\begin{split}
 G_i^0=\max\Bigl\{&0,
  \max_{0\le t\le9/20-\widehat X_i}
         (\overline\beta_i^0t-ct^2/2),\\
 &\max_{0\le t\le\widehat X_i-11/50}
         (-\underline\beta_i^0t-ct^2/2)\Bigr\},\\
 M_0&=\overline{D(Z_0,\widehat X)}+G_1^0+G_2^0.
\end{split}
\tag{9}
\]
Each scalar maximum is evaluated exactly by clipping its stationary
point to the indicated interval. Any rational trial is valid;
proximity to the midpoint optimizer affects only efficiency.

Independently enclose the *whole-cell* slopes at the trial and use
(4) to construct \(\mathcal X=\mathcal X_1\times\mathcal X_2\).
Evaluate (6)--(8) over the original whole-cell reference/root
enclosures and \(X\in\mathcal X\). If the resulting outward
intervals are \(\mathcal G_j\), then
\[
 V(Z(\xi))\le M_0+
                  \sum_j h_j\sup|\mathcal G_j|
             \qquad\text{throughout the parameter box}.
\tag{10}
\]
For the proof, integrate the continuously differentiable envelope
along the straight parameter segment from \(\xi^0\) to \(\xi\).
Every intermediate optimizer lies in (4). Enlarging correlated
quantities to interval enclosures is conservative, so (8) is bounded
by the stated intervals along this segment.

There is no whole-cell quadratic target gain to add to (10).
The target maximum is already taken at each point of the integrated
envelope; only the midpoint upper estimate (9) contains such a gain.
For example, a strict outward bound
\[
             M_0+\sum_j h_j\sup|\mathcal G_j|<-1/2000
\tag{11}
\]
would accept this cell for one conditional orientation and all
targets. Both orientations still require their own test.

## 5. Scope of a future implementation

The interval optimizer boxes need not shrink to the exact optimizer
and need not track clipping transitions. The original branch,
whole-cell root validation, correlated responses, ordinary-face
coverage, complete tree reconstruction and saved replay remain
necessary. A floating optimization may propose a rational trial,
but it does not enter acceptance except through that rational value.

Equations (3)--(11) are an alternative analytic acceptance rule.
They do not establish that any previously unfinished cell passes,
that the complete reference family has a negative deficit, or that
the finite open source has a nonzero dominant contribution. The
existing partial certificate and its original proof and checker
remain unchanged.
