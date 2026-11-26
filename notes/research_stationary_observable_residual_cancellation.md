# Estimating a boundary derivative using the stationary equations

Research deduction, 6 November 2026.

The terminal comparison needs a bound for the boundary derivative of an
action at its critical point. An enclosure of each critical coordinate
separately can lose information: the coordinates satisfy the same system
of stationary equations. Those equations may be subtracted from the
observable before estimating its error. The resulting function has the
same value on the critical set, and can have much smaller first
derivatives in the uncertain coordinates.

This note proves that elementary implication. It does not supply new
numerical signs, a finite-source estimate, or a volume theorem. Its
intended application uses the existing terminal reference families and
saved bounds for their original logarithms. It does not assert a new
principle of asymptotic rigidity.

## 1. An exact identity with an approximate reference point

Let \(z\in\mathbb C^d\), \(b\in\mathbb C\), and write
\(x=(z,b)\). Let \(F(x)\in\mathbb C^d\) and \(P(x)\in\mathbb C\)
be holomorphic on a domain containing all line segments used below.
The actual reference family satisfies

\[
 F(z(b),b)=0.
 \tag{1}
\]

Choose a coordinate \(a=z_k\). Suppose the existing enclosure has the
form

\[
 b=b^0+\delta,\qquad
 z=z^0+u\delta+\zeta,\qquad
 |\delta|\le r,\quad |\zeta_j|\le\eta_j.
 \tag{2}
\]

The stored point \(x^0=(z^0,b^0)\) need not satisfy (1). Put
\(U=(u,1)\), and let \(E_j\) be the coordinate vector for \(z_j\)
in \(\mathbb C^{d+1}\). In particular
\(h=x-x^0=U\delta+\sum_j E_j\zeta_j\).

For any fixed complex row \(w\in\mathbb C^{1\times d}\) and scalar
\(\lambda\in\mathbb C\), define

\[
 R(x)=P(x)-wF(x)-\lambda(a-a^0).
 \tag{3}
\]

Taylor's formula along the segment \(x^0+th\), with real
\(0\le t\le1\), gives the exact identity on (1):

\[
\begin{split}
 P(x)={}&P(x^0)-wF(x^0)+\lambda(a-a^0)
       +DR(x^0)U\,\delta
       +\sum_j DR(x^0)E_j\,\zeta_j\\
 &+\int_0^1(1-t)D^2R(x^0+th)[h,h]\,dt.
\end{split}
\tag{4}
\]

All derivatives here are complex derivatives and all matrix products
are ordinary products, without conjugation. The term \(-wF(x^0)\)
must be retained. Replacing the approximate stored point by a critical
point without paying its residual would invalidate (4).

Suppose an interval for
\(\Im(P(x^0)-wF(x^0))\) has midpoint \(p_0\) and radius
\(\rho_0\). If

\[
 |DR(x^0)U|\le\mu,\qquad
 |DR(x^0)E_j|\le\mu_j,
\]

and the last integral in (4) has modulus at most \(B\), then

\[
 \left|\Im P(x)-p_0-\Im\{\lambda(a-a^0)\}\right|
 \le \rho_0+r\mu+\sum_j\eta_j\mu_j+B.
 \tag{5}
\]

This is a bound for the same actual reference family as (2). It does
not restrict the independent target coordinates in a subsequent phase
comparison. Once (5) is certified, the exact quadratic maximum in
[the source-cell comparison](research_mixed_terminal_source_cell_joined_plane.md),
Section 2, applies without any change to its original cells.

## 2. Eliminating the first-order coordinate errors

There is an exact choice of \(w,\lambda\) that makes all the first
derivatives in (4) vanish whenever the following nonsingularity
conditions hold at \(x^0\). Let

\[
 H=D_zF(x^0),\qquad f=D_bF(x^0),\qquad
 v=-H^{-1}f,
 \tag{6}
\]

and suppose \(H\) is invertible and \(v_k\ne0\). Here \(v\)
is defined by (6); it is not silently identified with an approximate
stored predictor \(u\). Set

\[
 \lambda=\frac{P_b(x^0)+P_z(x^0)v}{v_k},\qquad
 w=(P_z(x^0)-\lambda e_k^{\mathsf T})H^{-1}.
 \tag{7}
\]

Then \(R_z(x^0)=0\) directly. Also

\[
 w f=-(P_z-\lambda e_k^{\mathsf T})v
     =-P_zv+\lambda v_k=P_b,
\]

so \(R_b(x^0)=0\). Thus \(DR(x^0)=0\), and both
first-order error terms in (4) disappear. This argument is valid
whether or not \(F(x^0)=0\).

Equivalently, the map \(x\mapsto(F(x),a)\) has invertible
derivative at \(x^0\). The nonzero entry \(v_k\) is the precise
condition that \(a\) can serve as a local coordinate on any zero
level of \(F\) meeting that inverse chart. If \(F(x^0)\ne0\),
the inverse-function theorem alone does not assert that the chart
meets \(F=0\). The actual family in (1)--(2) is a separate premise
of the error estimate. No global inverse or new finite-source identity
is asserted.

For a rigorous saved-data calculation one need not compute the exact
complex values in (7). One may choose exact Gaussian rational
\(w,\lambda\), then enclose the residual derivatives in (5) using
the saved analytic intervals. The estimate remains valid for every
such choice. A proposed inverse or a small numerical residual is not
itself a certificate; the interval bounds \(\mu,\mu_j\) must still
be proved. No choice is prescribed or numerically tested in this note.

## 3. Combining logarithmic terms before bounding the remainder

The intended stationary equations and observable are affine functions
plus linear combinations of the same original logarithmic primitives.
More generally, suppose

\[
 F(x)=F_{\rm aff}(x)+\sum_\ell c_\ell j(\ell_\ell(x)),\qquad
 P(x)=P_{\rm aff}(x)+\sum_\ell d_\ell j(\ell_\ell(x)),
 \tag{8}
\]

where \(c_\ell\in\mathbb C^d\), \(d_\ell\in\mathbb C\),
each \(\ell_\ell\) is affine, and the indicated branches of \(j\)
are holomorphic on the entire segment images. Zero coefficients may
be inserted to put both formulas on the same list of arguments.

Write \(L_\ell=D\ell_\ell\), and suppose saved bounds give
\(|j''|\le m_\ell\) on these images. Then a valid value of \(B\)
in (5) is

\[
 B=\frac12\sum_\ell |d_\ell-wc_\ell|\,m_\ell
       \left(r|L_\ell U|
                   +\sum_j\eta_j|L_\ell E_j|\right)^2.
 \tag{9}
\]

Indeed the affine terms, including \(-\lambda(a-a^0)\), have
zero second derivative. Each remaining term contributes
\((d_\ell-wc_\ell)j''(\ell_\ell(x))\,(L_\ell h)^2\)
to the integrand in (4). Its modulus has the bound in (9), and
\(\int_0^1(1-t)\,dt=1/2\). The coefficients must be combined
before taking absolute values to obtain this particular bound.
Evaluating \(P\) and \(wF\) separately gives a valid but potentially
larger bound.

For the original notation \(g'(z)=j(z)+i\pi(1/2-z)\),
one has \(g'''=j''\). Thus the already saved full primitive
curvature bounds are of the order required in (9). Their original
argument domains and logarithmic lifts still have to be checked for
each use; the identity alone does not enlarge those domains.

## 4. The two existing terminal representations

At an actual coupled terminal reference the shared stationary equation
is

\[
 f_a=g'(a+s)+g'(a+t)-3g'(a)+2\pi it=0.
 \tag{10}
\]

Consequently the two expressions

\[
 P_O=\tfrac32g'(a)-g'(a+s),\qquad
 P_T=g'(a+t)-\tfrac32g'(a)+2\pi it
 \tag{11}
\]

represent the same boundary derivative, since \(P_T-P_O=f_a\).
This identity is already present in the original terminal action and
height-derivative formulas; see
[the height-sign proof](research_mixed_terminal_height_tangent_sign.md)
and [the plane allocation](research_mixed_terminal_reserved_plane_transfer.md).
It is one particular subtraction of a stationary equation.

The two expressions generally differ at the stored approximate point.
Any Taylor estimate must use the chosen expression's own constant,
derivative and remainder. The whole-affine terminal representation
can be estimated using the smaller posterior error of \(t\), while
(3)--(9) also permit combinations of several stationary equations.
Whether either choice pays the five remaining phase comparisons is a
separate quantitative question. No computation or successful sign is
asserted here, and no frozen comparison record is changed.
