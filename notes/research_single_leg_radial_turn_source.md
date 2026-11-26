# A nonzero geometric source along one radial leg and its turn

22 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

The original centered multiplication tensor has a uniformly growing
geometric contribution when two parameters have modulus one and the
third runs along a strict prism ray, including its zero endpoint.
An exact reciprocal identity gives the corresponding original scalar
observation after a genuine turn. The coefficient comes from the
initialized source, rather than a choice of a formal saddle solution.

These are statements about a universal three-boundary source. They do
not assert that arbitrary open outputs remain in this family, or that
an assembled knot period satisfies the volume identity.

## 1. The source and the result

Use the full algebra, centered basis and original Frobenius functional
of the [centered compiler](research_centered_fourier_conway_compiler.md).
Thus
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \kappa=q^{d^2/2},\qquad
 U_N(t)=\sum_{j=0}^d t^j f_j,
\]
Every power \(q^\alpha\) means \(e^{\pi i\alpha/N}\), including
half-integer exponents. In these conventions
\[
 \mathcal C_N(x,y,z)=\phi(U_N(x)U_N(y)U_N(z)),\qquad
 \phi(f_i f_j)=\delta_{ij},\qquad Jf_j=f_{d-j}.
 \tag{1}
\]
The positive coefficient norm makes the entire centered basis
orthonormal. All value and first-derivative coordinates at the repeated
Casimir roots remain in this space.

A strict prism shape means real numbers
\[
 a,b,c>0,\qquad a+b,a+c,b+c<1,\qquad a+b+c>1.
 \tag{2}
\]
For such a shape put
\[
 x_r=-r e^{-2\pi ia},\qquad y=-e^{-2\pi ib},\qquad
 z=-e^{-2\pi ic},\qquad 0\le r\le1.
 \tag{3}
\]
There is no requirement that the radial leg have the largest angle.
Use the source's calibrated branches
\[
 \begin{split}
 \Psi(x,y,z)={}&-\frac{\pi}{12}
 +\frac1{2\pi}\bigl[
 \operatorname{Li}_2(-x)+\operatorname{Li}_2(-y)
 +\operatorname{Li}_2(-z)+\operatorname{Li}_2(-xyz)\\
 &\hspace{27mm}
 -\operatorname{Li}_2(xy)-\operatorname{Li}_2(xz)
 -\operatorname{Li}_2(yz)\bigr],\\
 B(x,y,z)={}&[(1-xy)(1-xz)(1-yz)]^{-1/2}.
 \end{split}
 \tag{4}
\]
The dilogarithms start with their power series in the open unit disk
and take continuous limits at the displayed strict angular boundary.
The square root has the branch specified by the same source. None of
its three factors vanishes on (2)--(3). Set
\[
 h(r)=-\operatorname{Im}\Psi(x_r,y,z),\qquad
 J_0(t)=\int_0^t\log(2\sin\pi u)\,du\quad(0\le t\le1).
 \tag{5}
\]

**Theorem.** Uniformly for shapes in a fixed compact subset of (2)
and all \(0\le r\le1\),
\[
 \mathcal C_N(x_r,y,z)=
 \kappa e^{i\pi/4-\pi i/(2N)}B(x_r,y,z)
                   e^{iN\Psi(x_r,y,z)}(1+O(N^{-1})).
 \tag{6}
\]
The height is strictly increasing on \(0<r<1\), and
\[
 h(r)\ge h(0)=J_0(b+c)-J_0(b)-J_0(c)>0.
 \tag{7}
\]
Consequently the original source is nonzero for every sufficiently
large level, uniformly in this family. The statement includes both
parities, composite levels and level-dependent approaches to \(r=0\).
It concerns the actual finite polynomial in (1).

## 2. Positivity of the entire radial interval

For \(0<t<1\), differentiating the Fourier series of the
dilogarithm, or integrating its logarithmic derivative, gives
\[
 \operatorname{Im}\operatorname{Li}_2(e^{-2\pi it})
                                      =2\pi J_0(t).
\]
Formula (4) at \(x=0\) therefore gives the equality in (7).
To prove its strict sign, fix \(c\) and consider
\(g(b)=J_0(b+c)-J_0(b)-J_0(c)\) on \(0<b<1-c\).
The log-sine integral has \(J_0(1)=0\) and
\(J_0(1-t)=-J_0(t)\). Thus \(g\) is zero at both endpoints.
Moreover
\[
 g'(b)=\log\frac{\sin\pi(b+c)}{\sin\pi b}
\]
is positive before \(b=(1-c)/2\) and negative afterwards.
This proves \(g(b)>0\) throughout the open interval.

For monotonicity in \(r\), set
\[
 E=e^{-2\pi i(a+(b+c)/2)},\qquad
 s=2\cos\pi(b-c),\qquad t_0=2\cos\pi(b+c).
\]
The strict prism inequalities imply
\[
 \frac12<a+\frac{b+c}{2}<1,\qquad
 \operatorname{Im}E>0,\qquad
 s-t_0=4\sin\pi b\sin\pi c>0.
 \tag{8}
\]
Differentiating (4) along the ray gives
\[
 \frac{dh}{d\log r}=-\frac1{2\pi}\arg\mathcal R_r,
 \quad
 \mathcal R_r=
 \frac{(1-r e^{-2\pi i(a+b)})(1-r e^{-2\pi i(a+c)})}
      {(1-r e^{-2\pi ia})(1-r e^{-2\pi i(a+b+c)})}
 =\frac{1-rsE+r^2E^2}{1-rt_0E+r^2E^2}.
 \tag{9}
\]
Here the argument is continued from zero at \(r=0\); it is not a
new choice of logarithmic lift. Direct multiplication gives
\[
 \operatorname{Im}\mathcal R_r
 =-\frac{r(s-t_0)(1-r^2)\operatorname{Im}E}
             {|1-rt_0E+r^2E^2|^2}<0
                                      \qquad(0<r<1).
 \tag{10}
\]
Thus the continued argument stays in \((-\pi,0)\), proving
strict monotonicity. Continuity includes \(r=0,1\).
The lower bound in (7) is uniformly positive on shape compacts.

## 3. Taking the initialized source formula to the zero endpoint

The [full prism-source theorem](research_centered_tensor_full_prism_source_transport.md)
already proves (6) on every interval \(r_0\le r\le1\), provided
the height is nonnegative. Its exact canceled formula is
\[
 \mathcal C_N=\mathcal G_N
 -\frac{\kappa}{N}D_N(x)D_N(y)D_N(z)\mathcal I_N,
 \qquad D_N(t)=1-(-1)^d t^N.
 \tag{11}
\]
Here \(\mathcal G_N\) is the specified nonzero seven-factor
canonical Gamma quotient. We now check the constants as the one
radius tends to zero; the theorem's stated restriction \(r_0>0\)
is not silently dropped.

Permute the contour roles so that its first angle is largest, as in
the source proof. Its two remaining angles, say \(b',c'\), are
less than \(1/2\). Every use of the canonical factorial estimates
there is on a full vertical strip with real part in a fixed compact
subinterval of \((0,1)\). Those estimates, including the relative
error, are uniform for arbitrarily large imaginary parts. Sending
one radius to zero only sends some nonnegative heights to infinity.

Write \(\varrho_x,\varrho_y,\varrho_z\) for the permuted moduli,
and \(\ell_j=-\log\varrho_j/(2\pi)\). Before taking the limit
they are finite and nonnegative. On the vertical current parameter
\(Y\in\mathbb R\), the shifted arguments are
\[
 a_Y=1-b'+i(Y+\ell_y),\quad
 b_Y=1-c'+i(Y+\ell_z),\quad
 c_0=1-b'-c'+i(\ell_y+\ell_z).
\]
The possible amplitude denominators in its current estimate are
\(h_*(c_0),h_*(a_Y),h_*(b_Y)\), where
\(h_*(w)^2=i(1-e^{2\pi iw})\). Their angles are respectively
\(b'+c',b',c'\). For every \(v\ge0\) and \(0<\theta<1\),
\[
 |1-v e^{-2\pi i\theta}|\ge\sin(\pi\theta)(1+v).
 \tag{12}
\]
All reciprocal amplitude factors therefore stay bounded independently
of these heights. The current rate proof uses only that the moduli
are at most one: its comparison \(v_0\le\min(v_y,v_z)\) requires
no positive lower radius, since
\(v_y=\varrho_y e^{-2\pi Y}\),
\(v_z=\varrho_z e^{-2\pi Y}\) and
\(v_0=\varrho_y\varrho_z e^{-2\pi Y}\).
Its Cauchy factor also has the bound (12),
uniformly even when the Cauchy-leg radius is zero. Hence the same
integrable current majorant gives
\[
 |\mathcal I_N|\le C N\left[
       \int_{-\infty}^0 e^{\pi NY}\,dY+
       \int_0^\infty e^{-\pi NY/2}\,dY\right]\le C',
\]
and consequently
\[
 |\mathcal I_N|\le C,\qquad
 |\mathcal C_N-\mathcal G_N|\le C/N
                                      \qquad(0<r\le1),
 \tag{13}
\]
with constants independent of the lower radius.

The seven-factor quotient is symmetric in its angle/height linear
forms. Write \(\mathfrak F_N\) for the source's canonical factorial
\(F_N\), to distinguish it from the generating polynomial (1).
For the original radial leg its zero-radius limit is
\[
 \mathcal G_N(0,y,z)=\frac{\kappa}{\sqrt N}
 \frac{\mathfrak F_N(N(1-b)-1/2)
       \mathfrak F_N(N(1-c)-1/2)}
      {\mathfrak F_N(N(1-b-c))}\ne0.
 \tag{14}
\]
Indeed exactly two numerator and two denominator arguments tend
upwards to infinity. At fixed \(N\), their factorials tend to the
same nonzero canonical upper constant, and cancel in matching pairs.
The remaining three factors lie in the nonzero canonical strip.

Continuity of the original polynomial and this explicit limit extend
(13) to \(r=0\). The same full-strip estimates give
\[
 \mathcal G_N=
 \kappa e^{i\pi/4-\pi i/(2N)}B(x_r,y,z)
                     e^{iN\Psi(x_r,y,z)}(1+O(N^{-1}))
 \tag{15}
\]
uniformly down to that endpoint: all positive heights are allowed,
and the remaining amplitude factors stay bounded and nonzero.
This is a continuous radial assertion, not holomorphy of the Gamma
quotient at zero. The original source itself is polynomial.

The height bound (7) and the nonzero bounded amplitude make (13)
exponentially small relative to (15), uniformly on the family.
This proves (6).

It is essential to take the limit of (11). In the representation
using the radial leg as the Cauchy leg, setting that parameter equal
to zero in the uncanceled rectangle would lose the moving pole at
infinity. Its nonzero contribution is exactly the limit (14).
If the largest-angle permutation chooses another Cauchy leg, the
diverging shifts occur in the factorial weight instead; the uniform
estimates above cover that representation as well.

## 4. The original scalar observation after a turn

The compiler's full coefficient relation is
\(\overline{C_{ijk}}=C_{d-i,d-j,d-k}\). Reindexing its polynomial
gives the exact identity
\[
 \mathcal C_N(x,y,z)=(xyz)^d
       \overline{\mathcal C_N(1/\bar x,1/\bar y,1/\bar z)}.
 \tag{16}
\]
For \(|y|=|z|=1\), define the reciprocal polynomial
\[
 \mathcal T_N(t;y,z)=t^d\mathcal C_N(1/t,y,z)
             =\phi\bigl[J(U_N(y)U_N(z))U_N(t)\bigr].
 \tag{17}
\]
Both expressions have their polynomial interpretation at \(t=0\).
Equations (16)--(17) give
\[
 \mathcal T_N(t;y,z)=(yz)^d
                         \overline{\mathcal C_N(\bar t,y,z)}.
 \tag{18}
\]
Thus on the turned ray \(t_r=\overline{x_r}\), (6) yields
\[
 \mathcal T_N(t_r;y,z)=(yz)^d
 \overline{\kappa e^{i\pi/4-\pi i/(2N)}
       B(x_r,y,z)e^{iN\Psi(x_r,y,z)}}(1+O(N^{-1})).
 \tag{19}
\]
Its exponential rate is the same positive \(h(r)\). The carrier
\((yz)^d\) and all phases in (19) are retained. In particular the
turned coordinate is \(t_r=\bar x_r\); replacing it by \(x_r\)
would change the strict-prism angular condition.

For unit-normalized coherent inputs
\(u_N(t)=U_N(t)/\sqrt{Z_N(t)}\), with
\(Z_N(t)=\sum_{j=0}^d|t|^{2j}\), the actual scalar is
\[
 \phi\bigl[J(u_N(y)u_N(z))u_N(t)\bigr]
                =\frac{\mathcal T_N(t;y,z)}{N\sqrt{Z_N(t)}}.
 \tag{20}
\]
Here \(1\le Z_N(t_r)\le N\). The exact normalization is only
polynomial and does not change the positive exponential rate.

## 5. Scope and complete proof sources

This proves the presence and nonzero coefficient of the geometric
contribution in two specified original scalar observations, uniformly
along the full radial interval and at its signed-crossing endpoint.
It is not merely a forward norm maximum or a formal critical equation.
Reciprocity itself is already part of the tensor's exact algebra;
the additional estimate is the growing single-leg interval through
zero and its correctly oriented turned observation.

The result supplies neither the whole output after the next arbitrary
branching nor a compatible scalar observation for an arbitrary short
component. Its two unit parameters are a different regime from the
compact open bidisks in the cyclic vacuum-gap theorem. No uniform
vacuum gap at this unit boundary is inferred here. No new knot-volume
class or finite-exception theorem follows from (6) or (19) alone.

The complete direct proof texts are:

| Source | SHA-256 |
|---|---|
| [Initialized full prism source, 651 lines](research_centered_tensor_full_prism_source_transport.md) | eb43e287eca5933b70de3b6362a81f92d46bb2e121f0eb5716793c107adaef10 |
| [Full centered compiler, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

Both were read in full at the matching pins. The radial sign argument,
uniform endpoint extension and correctly marked turned observation
are proved above. Only written mathematics and text operations were
used. No earlier final or public manuscript was edited.
