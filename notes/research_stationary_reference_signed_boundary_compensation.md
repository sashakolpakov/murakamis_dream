# Retaining the sign of the boundary response

Research lemma, 6 November 2026. The existing boundary-extension
argument bounds the absolute size of a response term. There is also
an exact compensating function. Subtracting it makes the original
phase difference subharmonic, so the signed response can be kept
until the boundary estimate is taken. On a disk its correction at
the center is a Fourier inner product. This is a conditional estimate,
not a new noncancellation theorem for a quantum sum.

## 1. The original phase difference and its correction

Use the hypotheses and notation of
[stationary boundary extension](research_mixed_stationary_reference_boundary_extension.md),
with external parameter \(c\) in a bounded planar domain \(\Omega\).
Its boundary is assumed piecewise smooth, and all the functions below
are defined on neighborhoods of the closure. The clipped disks used
there satisfy this boundary hypothesis.

The reference \(r(c)\in\mathbb C^n\) is holomorphic. The reference
phase \(F\) is holomorphic near its image and has no additional
explicit dependence on \(c\). Write \(I\) for its internal coordinates
and \(B\) for its boundary coordinates. Throughout the neighborhood,
\[
 F_i(r(c))=0\quad(i\in I),\qquad p_j(c)=F_j(r(c))\quad(j\in B).
 \tag{1}
\]
The functions \(p_j\) are the original complex boundary derivatives.
They are not independently chosen supporting slopes.

For a fixed real target \(x\), fixed real height vector \(h\), and
constant diagonal matrix \(\Lambda=\operatorname{diag}(\lambda_j)\)
with \(\lambda_j\ge0\), put
\[
 w=x+ih+\tfrac12\Lambda(r-\bar r),\qquad
 D(c;x)=\Re\{\Psi(w)-F(r)-F'(r)\cdot(w-r)\}.
 \tag{2}
\]
Require the target phase \(\Psi\) to be holomorphic near the whole
target image and \(-\Re\Psi''(w)\succeq0\) throughout that image.
The previously proved exact identity is
\[
 \Delta D=A(c;x)+2\Re\sum_{j\in B}
                \lambda_jp_j'(c)\overline{r_j'(c)},\qquad
 A=-\Re\{(\Lambda r')^T\Psi''(w)\Lambda\bar r'\}\ge0.
 \tag{3}
\]
Here \(\Delta=\partial_{\Re c}^2+\partial_{\Im c}^2\). No target
optimization has been differentiated.

Define the real function
\[
 C(c)=\frac12\Re\sum_{j\in B}\lambda_jp_j(c)\overline{r_j(c)}.
 \tag{4}
\]
The product in (4) is generally not holomorphic. Its precise
Laplacian is what is needed:
\[
 \Delta C=2\Re\sum_{j\in B}
                  \lambda_jp_j'\overline{r_j'}.
 \tag{5}
\]
Indeed, for holomorphic \(p,r\), differentiating
\(\Re(p\bar r)=(p\bar r+\bar p r)/2\) gives
\(\Delta\Re(p\bar r)=4\Re(p'\bar r')\).

**Proposition 1.** Under these hypotheses, \(D-C\) is subharmonic.
Consequently
\[
 D(c;x)\le C(c)+\sup_{\zeta\in\partial\Omega}
                         \{D(\zeta;x)-C(\zeta)\}.
 \tag{6}
\]
If a proved boundary majorant \(d(\zeta)\) satisfies
\(D(\zeta;x)\le d(\zeta)\) for every allowed target, then
\[
 D(c;x)\le C(c)+\sup_{\partial\Omega}(d-C).
 \tag{7}
\]

*Proof.* Equations (3) and (5) give \(\Delta(D-C)=A\ge0\).
Apply the maximum principle to this original function for each fixed
target. The same target-independent majorant then proves (7).
The argument does not differentiate \(d\), a supremum, or a numerical
upper bound. \(\square\)

One may replace (4) by
\[
 C_{p^0,r^0}(c)=\frac12\Re\sum_{j\in B}\lambda_j
              (p_j(c)-p_j^0)\overline{(r_j(c)-r_j^0)}
 \tag{8}
\]
for arbitrary complex constants \(p_j^0,r_j^0\). The difference
between (4) and (8) is harmonic, so the same proof applies.
Taking these constants from one reference can reduce the size of the
quantities that have to be enclosed. It does not change their Laplacian.

There is a useful stronger conclusion when the reference phase is
concave as well as the target phase.

**Proposition 2.** Suppose \(\lambda_j=1\) at every boundary
coordinate. Choose a reference \(r^0=r(c_0)\) and \(p_j^0=F_j(r^0)\).
Assume that \(F\) is holomorphic on a convex neighborhood containing
all segments from \(r^0\) to \(r(c)\), and that
\(-\Re F''\succeq0\) throughout these segments. Then the centered
function (8) is nonpositive. In particular,
\[
 \sup_{c\in\overline\Omega,\ x}D(c;x)
 \le \sup_{\zeta\in\partial\Omega}
                  \{d(\zeta)-C_{p^0,r^0}(\zeta)\}.
 \tag{8a}
\]
A strict negative upper bound on the right proves a uniform phase
gap without any estimate of derivatives with respect to \(c\).

*Proof.* Set \(v=r(c)-r^0\). Both references satisfy the internal
stationary equations, so their gradient difference has zero internal
components. Since the boundary coefficients are one,
\[
 \begin{split}
 2C_{p^0,r^0}(c)
 &=\Re\{(F'(r(c))-F'(r^0))\cdot\bar v\}\\
 &=\int_0^1\Re\{(F''(r^0+tv)v)\cdot\bar v\}\,dt\\
 &=\int_0^1 v^*\Re F''(r^0+tv)v\,dt\le0.
 \end{split}
 \tag{8b}
\]
The last identity uses symmetry of the complex Hessian: its Hermitian
real part is its entrywise real part. Apply (7) with (8), then discard
the nonpositive interior term. \(\square\)

The boundary comparison in (8a) keeps the phase and its signed
compensation at the same boundary point. This is legitimate because
their difference is subharmonic. It is different from pairing unrelated
local phase gaps with the absolute derivative bounds in the earlier
barrier estimate. The full boundary must still be covered.

## 2. Harmonic measure expresses the signed cost exactly

For \(c\in\Omega\), let \(\omega_c\) be harmonic measure on
\(\partial\Omega\): integrating a continuous boundary function
against \(\omega_c\) gives its harmonic extension evaluated at \(c\).
The subharmonic comparison used in Proposition 1 also gives
\[
 D(c;x)\le
 \int_{\partial\Omega}D(\zeta;x)\,d\omega_c(\zeta)
       +C(c)-\int_{\partial\Omega}C(\zeta)\,d\omega_c(\zeta).
 \tag{9}
\]
Since each \(p_j\) and \(r_j\) is harmonic, their boundary averages
are \(p_j(c)\) and \(r_j(c)\). Expanding the products therefore yields
the exact identity
\[
 C(c)-\int C\,d\omega_c
 =-\frac12\Re\sum_{j\in B}\lambda_j
   \int_{\partial\Omega}
       (p_j(\zeta)-p_j(c))
       \overline{(r_j(\zeta)-r_j(c))}\,d\omega_c(\zeta).
 \tag{10}
\]
Thus the response correction is a signed covariance. It can help or
hurt the phase comparison. Its sign is not fixed by holomorphicity.

If \(D\le-\gamma\) on the whole boundary, (9)--(10) imply
\[
 D(c;x)\le-\gamma-\frac12\Re\sum_{j\in B}\lambda_j
   \int (p_j-p_j(c))\overline{(r_j-r_j(c))}\,d\omega_c.
 \tag{11}
\]
Cauchy--Schwarz gives the weaker, always valid upper bound
\[
 D(c;x)\le-\gamma+\frac12\sum_{j\in B}\lambda_j
  \left(\int|p_j-p_j(c)|^2\,d\omega_c\right)^{1/2}
  \left(\int|r_j-r_j(c)|^2\,d\omega_c\right)^{1/2}.
 \tag{12}
\]
Keeping the cross terms in (11) may be stronger than replacing them
by (12). Neither formula asserts a sign without an additional estimate.

For example, take one boundary coordinate, \(r(c)=c\), \(F(z)=-z^2/2\),
and \(\lambda=1\). Then \(p(c)=-c\). On a disk centered at zero,
the covariance at the center is \(-R^2\), so its contribution to the
upper bound is \(+R^2/2\). These functions are entire; choosing
\(\Psi=F\) satisfies the target-concavity hypothesis. Holomorphicity
and concavity alone therefore do not eliminate the response loss.

## 3. The disk formula and a finite Fourier certificate

Suppose now that \(\Omega=\{|c-c_0|<R\}\), and expand the holomorphic
boundary functions as
\[
 p_j(c_0+t)=\sum_{n\ge0}p_{j,n}t^n,\qquad
 r_j(c_0+t)=\sum_{n\ge0}r_{j,n}t^n.
 \tag{13}
\]
Their neighborhoods of holomorphicity contain a slightly larger disk,
so these series converge absolutely on the boundary. At \(c_0\),
harmonic measure is \(d\theta/(2\pi)\). Orthogonality of the functions
\(e^{in\theta}\) gives
\[
 \int (p_j-p_j(c_0))\overline{(r_j-r_j(c_0))}\,d\omega_{c_0}
       =\sum_{n\ge1}p_{j,n}\overline{r_{j,n}}R^{2n}.
 \tag{14}
\]
In particular, a complete boundary bound \(D\le-\gamma\) implies
\[
 D(c_0;x)\le-\gamma-\frac12\Re\sum_{j\in B}\lambda_j
                  \sum_{n\ge1}p_{j,n}\overline{r_{j,n}}R^{2n}.
 \tag{15}
\]
This is a Fourier inner product of the boundary derivatives and
boundary coordinates. It is not an identification with the Fourier
coefficients of Kashaev's invariant.

For an explicit tail bound, assume \(R<\rho\) and that the functions
are holomorphic on a neighborhood of \(|c-c_0|\le\rho\), with
\[
 |p_j(c)|\le M_{p,j},\qquad |r_j(c)|\le M_{r,j}
                 \quad(|c-c_0|=\rho).
 \tag{16}
\]
Cauchy's coefficient estimates, followed by a geometric series, give
\[
 \left|\sum_{n>m}p_{j,n}\overline{r_{j,n}}R^{2n}\right|
 \le M_{p,j}M_{r,j}
       \frac{(R/\rho)^{2(m+1)}}{1-(R/\rho)^2}.
 \tag{17}
\]
Thus finitely many certified coefficients and (16) would bound the
signed correction in (15). No such coefficient certificate is supplied
here. Formula (15) controls the center; other points require their
own harmonic-measure comparison or an additional uniform argument.
For a clipped disk the boundary includes its straight segments,
and its harmonic measure is not the uniform angular measure of the
containing circle. Formula (14) cannot be applied to that clipped
domain without changing the argument.

## 4. Several parameters and gluing

Under the hypotheses of the
[product-boundary theorem](research_mixed_stationary_reference_product_boundary_extension.md),
use (4) with the jointly holomorphic functions \(p_j(c),r_j(c)\).
For each parameter \(c_k\),
\[
 \Delta_k(D-C)=A_k\ge0.
 \tag{18}
\]
Iterating the one-variable maximum principle proves (6)--(7) with
the product of the full boundary curves in place of
\(\partial\Omega\). Iterating harmonic extension gives (9)--(12)
with the product harmonic measure. The holomorphic functions have
their interior values as their averages under this product measure,
which justifies the same covariance calculation.

For several clusters sharing the same reference coordinates, sum the
functions (4) before taking any upper bound. At a shared coordinate,
the contribution is
\[
 \frac{\lambda_j}{2}\Re\left\{
        \left(\sum_\ell p_j^{(\ell)}\right)\overline{r_j}\right\}.
 \tag{19}
\]
It vanishes identically if the original complex matching equation
\(\sum_\ell p_j^{(\ell)}=0\) holds throughout the parameter
neighborhood. The shared coordinate, target height and coefficient
\(\lambda_j\) must agree between clusters, just as in the previous
gluing theorem. Only external coordinates remain in the total
compensating function.

This lemma offers a signed alternative to the absolute response
barriers. It does not supply the boundary phase inequalities, joint
holomorphic reference families for arbitrary tangles, a contributing
cycle, or a nonzero leading coefficient for the entire original sum.
Those remain separate requirements for short-filling stability.

## 5. Application to the original second-position comparison

For the existing prefix family, the boundary coordinates are \(a,b\)
and both coefficients are one. The reference phase is
\[
 F=Q_1(u;a,z)+Q_\beta(v;z,b)
                  -g(z)-\frac\alpha2g(a)-\frac\beta2g(b),
 \qquad \alpha,\beta\in\{0,1\},
 \tag{20}
\]
with the original \(Q_\epsilon\) and \(g\) defined in the
[central comparison](research_mixed_second_selected_central_completion.md).
The original stationary equations give \(F_u=F_z=F_v=0\).

The rectangular coordinate ranges in the
[first-type-three extension](research_mixed_second_selected_first_three_extension.md)
and the corresponding first-type-four endpoint bounds form a convex
containing product for each fixed \((\alpha,\beta)\). Both ordinary
indices have real part between .24 and .433 and imaginary part between
-.102 and .068. The three outer coordinates have real part in
\([.22,.45]\) and imaginary part in \([-.12,.12]\). Thus the
[whole-pair Hessian estimate](research_mixed_horizontal_zero_mode_support.md)
applies separately to both \(Q\) terms throughout every connecting
segment. The remaining negative own terms in (20) have nonnegative
negative real Hessian, since all their real coordinates are below
\(1/2\). Hence \(-\Re F''\succeq0\) on this containing product.

For example, the exact parameter \(c_0=.32-.04i\) lies in both
\(K_3\) and \(K_4\). Its canonical reference supplies one possible
anchor \(r^0\). With the new or old original marginals as appropriate,
the compensation in Proposition 2 is
\[
 C_0(c)=\frac12\Re\{
       (p_L(c)-p_L(c_0))\overline{a(c)-a(c_0)}
      +(p_R(c)-p_R(c_0))\overline{b(c)-b(c_0)}\}\le0.
 \tag{21}
\]
The same formula applies to the central alternatives and to the formal
half-row extension, because both have the same unselected boundary
coordinates and original reference phase. Their target-concavity
hypotheses remain the separate ones already proved for those targets.

Consequently a complete-boundary estimate
\[
                     d_\nu(c)-C_0(c)\le-\delta
                     \quad(c\in\partial K_j,\ \nu=0,1)
 \tag{22}
\]
would prove the corresponding uniform comparison throughout \(K_j\).
It requires a certified anchor, original boundary marginal values,
and the whole boundary inequalities. It requires no new inverse-Jacobian
or boundary-derivative estimates. No anchor evaluation or estimate
(22) has been performed here, and the current numerical attempt retains
its original absolute-response protocol.
