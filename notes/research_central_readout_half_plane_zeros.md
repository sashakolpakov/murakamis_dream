# Zeros of the original central readout inside the positive Jacobi domain

Research note, 3 November 2026. The original physical kernel rows
are zero-free in \(\Re w<c_0\), and their Jacobi problem is uniformly
accretive away from the boundary of that half-plane. This property
does not extend to their original central trace. The distinction
holds at every level, for each fixed signed integer power, and is
not an arbitrary-vector counterexample.

## 1. The original polynomial and its top two coefficients

Use the original Newton algebra and trace, with
\[
 q=e^{\pi i/N},\quad D=N-1,\quad
 c_j=2\cos((2j+1)\pi/N),\quad s_j=2\sin(j\pi/N),
 \quad S_j=\prod_{r=1}^j s_r .
 \tag{1}
\]
Thus \(S_D=N\), \(c_D=c_0\), and
\[
 e_j(w)=\frac{\prod_{r=0}^{j-1}(c_r-w)}{S_j^2},
 \qquad
 \mathcal H_{n,N}(w)=\phi_N[R^nK_N(\,\cdot\,,w)] .
 \tag{2}
\]
The symbol \(\mathcal H\) here has the ordinary free spectral
variable \(w\), rather than the outside angle used in some terminal
packet notes. It includes every original value and first normal.

Let \(M\) be the original crossing matrix and
\(\alpha=M^n\mathbf e_0\). The Frobenius identity
\(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\) gives
\[
                 \mathcal H_{n,N}(w)
                      =\sum_{j=0}^D\alpha_{D-j}e_j(w).
 \tag{3}
\]
This is the actual central observation, not the positive norm of
the physical row vector. For \(N\ge3\), the upper-left crossing block is
\[
 \kappa^{-1}M\big|_{\{0,1\}}=
             \begin{pmatrix}1&0\\-q&-q^2\end{pmatrix},
 \qquad 1+q^2=q c_0\ne0.
 \tag{4}
\]
Taking every signed integer power of this invertible triangular
block yields
\[
 \alpha_0=\kappa^n,\qquad
 \frac{\alpha_1}{\kappa^n}
       =-\frac{1-(-q^2)^n}{c_0}.
 \tag{5}
\]
The formula includes \(n=0\); for negative powers it follows
from the same divided difference of the two distinct eigenvalues.

**Theorem 1.** For every \(N\ge3\) and every integer \(n\), the
polynomial \(\mathcal H_{n,N}\) has degree \(D=N-1\).
If its zeros, with multiplicity, are \(\zeta_1,\ldots,\zeta_D\), then
\[
 \sum_{\ell=1}^D\zeta_\ell
   =-c_0-\frac{s_1^2}{c_0}\bigl[1-(-q^2)^n\bigr],
 \qquad
 \sum_{\ell=1}^D\Re\zeta_\ell\le-c_0<0.
 \tag{6}
\]
In particular at least one actual zero satisfies
\[
               \Re\zeta_\ell\le-\frac{c_0}{N-1}<0.
 \tag{7}
\]

*Proof.* Only the final two terms in (3) contribute to the two
highest polynomial coefficients. The leading coefficient is
\(\kappa^n(-1)^D/N^2\), which is nonzero. The sum of the
Newton nodes in \(e_D\) is
\(\sum_{r=0}^{D-1}c_r=-c_0\), because the sum over all \(N\)
nodes is zero. Also \(S_D/S_{D-1}=s_D=s_1\).
Vieta's formula therefore gives
\[
       \sum_\ell\zeta_\ell=-c_0+s_1^2\alpha_1/\alpha_0.
 \tag{8}
\]
Substitution of (5) proves the identity. The number
\((-q^2)^n\) has modulus one for every signed integer \(n\),
so \(1-\Re(-q^2)^n\ge0\). This proves (6) and (7). \(\square\)

At the zero in (7), every physical row
\(F_j(w)=K_N(c_j,w)\) remains nonzero, by
[the positive Jacobi theorem](research_physical_jacobi_charge_boundary.md).
Its ordinary Jacobi truncations satisfy
\[
 \Re(\mathcal J_j-\zeta_\ell I)
       \ge(c_0-\Re\zeta_\ell)I\ge c_0 I\ge I.
 \tag{9}
\]
Thus their resolvent norms are at most one, their endpoint
transmission is nonzero, and the original physical source pin
\((R^nK)(c_0,\zeta_\ell)=\kappa^n\) remains fixed and nonzero.
Nevertheless the original central observation is exactly zero.
The obstruction persists for arbitrarily large levels with any
one fixed power \(n\ge3\).

## 2. The lower half-plane does not restore general nonvanishing

Actual positive geometric colors lie in the lower half-plane.
There is no general lower-half-plane stability statement for
the central polynomial either. A small exact original example
suffices to distinguish that claim from geometric-locus control.

At \(N=4,n=3\), direct multiplication of the original crossing
matrix and (3) gives
\[
 -16\kappa^{-3}\mathcal H_{3,4}(w)=p(w)
 =w^3+\sqrt2(2-i)w^2+(30-8i)w+\sqrt2(-76+98i).
 \tag{10}
\]
This polynomial has exactly one zero in
\[
 \left|w-\frac{-4293-4916i}{1000}\right|<\frac1{500}.
 \tag{11}
\]
In particular that zero has both negative real and negative
imaginary parts and lies strictly in \(\Re w<c_0=\sqrt2\).

Here is a rational certificate for (11), without a numerical
root assertion. Write \(z=(-4293-4916i)/1000\), \(r=1/500\).
Using
\[
 \frac{141421356237}{10^{11}}
       <\sqrt2<
 \frac{141421356238}{10^{11}},
 \tag{12}
\]
complex \(L^1\) upper bounds and a maximum-component lower
bound give
\[
 \begin{aligned}
 |p(z)|&\le\frac{7540696563473}{156250000000000},\\
 |p'(z)|&\ge\frac{643497938473027}{6250000000000},\\
 |3z+\sqrt2(2-i)|
       &\le\frac{1310639321883}{50000000000}.
 \end{aligned}
 \tag{13}
\]
The resulting Rouché margin is
\[
 r|p'(z)|-|p(z)|
       -r^2|3z+\sqrt2(2-i)|-r^3
 \ge\frac{393885057898477}{2500000000000000}>0.
 \tag{14}
\]
Taylor's formula is exact for this cubic. On \(|w-z|=r\),
the linear term therefore dominates the constant, quadratic
and cubic terms together. Rouché's theorem gives precisely
one zero inside the disk.

## 3. Scope of the obstruction

Equations (6)--(9) rule out a universal overlap lower bound
deduced solely from the positive Jacobi problem, its accretive
resolvent, its nonzero endpoint forcing, or the positive-real
physical-row ratios. They also rule out a zero-free or
strictly positive-real central readout on that entire half-plane,
even after multiplication by a nonvanishing scalar gauge.
The example (10)--(14) excludes the unrestricted lower-half-plane
version.

Neither result places a zero on the actual geometric boundary
locus. The zeros in (7) may depend on the level and may leave
every fixed compact set; the explicit disk (11) is outside the
proved geometric color region. Thus this is not a counterexample
to the terminal packet near the complete point, to the proved
internal \(3,3\) packet, or to a future source-specific theorem
on a smaller geometric domain. It identifies an actual scalar
observation which positivity of the larger state does not control.

The [focused checker](../experiments/check_central_readout_half_plane_zeros.py)
constructs the central polynomial from the bottom row of the
literal original \(M^n\), independently of the first-column
calculation (4)--(5). It checks the leading coefficient, the
Vieta identity and (10) at both level parities and signed powers.
It also checks (12)--(14) with exact rational arithmetic.
The [saved record](../repro/results/research-central-readout-half-plane-zeros.json)
is a normalization and arithmetic check; the all-level statement
is proved above.
