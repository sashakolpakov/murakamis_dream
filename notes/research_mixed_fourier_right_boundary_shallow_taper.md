# A paid shallow taper for the complete Fourier right boundary

Research deduction, 7 November 2026. The complete Fourier-cap
supporting plane pays the compensated right boundary on its entire
unselected plateau. It also pays a fixed shallow enlargement of the
physical suffix, with the actual hybrid taper heights and their
neighbor dependence. The original relative pinning fee is included.

The width is positive and fixed before taking the level to infinity.
No new source evaluation or quantified taper-width certificate is used.

## 1. The literal right component and its coherent extension

Use an actual Fourier-ended word and the notation of
[Fourier-ended boundary windows](research_mixed_fourier_ended_boundary_windows.md),
equations (11)--(18). The last vertex has type four, the last retained
coordinate is \(h=m-1\), and the physical right boundary starts at
the safe cut \(q\). Fix an admissible right good block and its triple
pin. Write \(\ell\) for the last pinned coordinate and \(v\) for the
outer Dirichlet coordinate of that block. Thus
\(\ell<v<q\), and every coordinate at or before the pin is kept at
its prescribed baseline when forming the right compact component.
All selections in this note are zero.

Put
\[
 P=[11/50,9/20],\qquad r_j=a_j+ic_j,\qquad
 \kappa_*=\frac1{2500000},\qquad
 a_d=1000(99/101)^{704}<\frac1{1296}.
 \tag{1}
\]
The output is fixed at \(y=x_0\). The exact right modulus is
\[
 R_N^{\rm F}
 =|V_N^{\rm F}(x_0,X_h)|
       \prod_{j=q+1}^{h}|C_{\epsilon_j,N}(X_{j-1},X_j)|
       |d_N(X_q)|^{\epsilon_q/2}
       \prod_{j=q+1}^{h}|d_N(X_j)|^{\epsilon_j},
 \quad X_j=e^{-2\pi iz_j}.
 \tag{2}
\]
The final vertex's selected alternative is already inside \(V_N^{\rm F}\).
No surviving retained coordinate is selected in (2).
In particular the factor at \(h\) has one half assigned to the
adjacent ordinary block and the other half to the Fourier cap.
At the safe cut \(q\) only the displayed half belongs to this
boundary product.

The compensated quantity is exactly
\[
 \mathcal C_{R,N}^{\rm F}
 =B_{R,N}^{\rm F}-D_R+a_d(x_v-a_v)^2.
 \tag{3}
\]
The protected closing terms cancel by the reflected identity (16a)
of [finite boundary windows](research_mixed_open_finite_boundary_windows.md):
\[
 B_{R,N}^{\rm F}-D_R
 =N^{-1}\log R_N^{\rm F}-M_R^{\rm F}
  +\sum_{j=\ell+1}^{q}
       \Re\{\phi_j(z_{j-1},z_j)-\phi_j(r_{j-1},r_j)\}.
 \tag{4}
\]
Here \(z_\ell=r_\ell\). The sum is the original safe coherent
extension, with its original allocated phases. Its cut marginal
cancels the literal suffix marginal; all internal complex marginals
cancel by the actual critical equations. No cyclic reference or
independent terminal action is substituted.

Suppose first that all free real coordinates belong to \(P\), at
their reference heights. Each complete ordinary factor has its
original supporting plane with coefficient \(\kappa_*\). The
[complete Fourier-cap plane](research_mixed_fourier_right_cap_full_plateau_plane.md),
Theorem 1, supplies precisely the missing terminal half allocation,
with the same coefficient and its original complex action and real
incoming marginal. Thus these planes apply to the entire product
(2), including all its rows and Fourier-polynomial zeros.

The fee in (3) is paid by a coherent extension edge. Precisely, if
the right block starts at \(g\), then
\(v=g+2d+5\), and edge \(j=g+2d+5\) is between the last pin and the
literal suffix. The protected last triple gives \(j\le q-3\).
Section 4 of
[contracted boundary collars](research_mixed_contracted_boundary_collar_completion.md)
proves that this edge has negative real Hessian at least \(I/5\);
its tangent defect supplies \(1/10\) of each endpoint's squared
displacement. In particular
\[
                   \frac1{10}-a_d>\kappa_*.
 \tag{5}
\]
Retain the remaining edge and complete-source quadratics as well.
For every aggregate source tolerance \(\tau>0\), (4) then gives
\[
 \mathcal C_{R,N}^{\rm F}
 \le-\kappa_*\sum_{j=\ell+1}^{h}(x_j-a_j)^2
                    +\tau+O(\log N/N)
       \qquad(\mathbf x\in P^{h-\ell}).
 \tag{6}
\]
This is the compensated bound, not a sign for \(B_{R,N}^{\rm F}\)
alone. Its constants are uniform on each compact admissible
bounded-width reference family. The finite-window reduction has
only finitely many such type and pin-position families.

Every reference real part in this ordinary suffix has distance
strictly greater than
\[
                            r_0=17/1000
 \tag{7}
\]
from \(\partial P\): the inherited whole-input ordinary images have
real ranges \((.267,.433)\) for type three and \((.24,.36)\) for
type four. Fourier-ended window inheritance uses these same maps
with its actual exterior leg. It does not require a repeated
reference or the narrower cyclic rectangles.

## 2. Continue the complete finite suffix

The square of (2) is the modulus of the holomorphic Laurent
polynomial
\[
 \mathcal P_N=
       V_N^{\rm F}(x_0,X_h)^2
       \prod_{j=q+1}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)^2
       d_N(X_q)^{\epsilon_q}
       \prod_{j=q+1}^{h}d_N(X_j)^{2\epsilon_j}.
 \tag{8}
\]
Thus \(|\mathcal P_N|=(R_N^{\rm F})^2\), also at every zero.
There is no holomorphic halfpower and no division by \(d_N\).
The exact incoming band of \(V_N^{\rm F}\) is
\([-N+1,0]\). Each conditional factor has bands
\([-N+1,0]\) and \([0,N-1]\), while \(\deg d_N<N\).
Consequently every separate exponent in (8) has absolute value
at most \(4N\).

Sum the continuous ordinary and Fourier-cap supporting planes
used in (6), before adding the coherent extension. This is a
continuous horizontal upper rate for \(R_N^{\rm F}\) on the full
suffix plateau. Apply
[horizontal complex extension](research_mixed_horizontal_complex_extension.md),
Theorem 1, to (8), with twice that rate. For each \(\zeta>0\)
there is a fixed complex neighborhood width \(\delta>0\) in which
the rate for \(R_N^{\rm F}\) increases by at most \(\zeta\), with
a polynomial prefactor and an arbitrarily small final source
tolerance. The estimate is uniform in the retained cut coordinate,
the original compact reference family, and the level.
It includes both real endpoints of every plateau interval.

This uses the complete finite suffix, not separate continuation
of its individual physical rows. Its coefficients may depend on
the level; only the proved rate and the exact linear degree bound
enter the extension theorem.

## 3. The actual shallow taper, with the cut protected

For a fixed sufficiently small \(\varepsilon>0\), allow
\[
 \begin{split}
 x_j&\in P &&(\ell<j\le q+1),\\
 x_j&\in[.22-\varepsilon,.45+\varepsilon]
                                      &&(q+2\le j\le h).
 \end{split}
 \tag{9}
\]
All selections remain zero. Thus the last incoming coordinate \(h\)
may taper whenever \(h\ge q+2\), as in the physical windows of
the boundary reduction. Define \(\bar x_j=\operatorname{clamp}_P x_j\).

On this range the exact unselected hybrid height is
\[
 h_j(\mathbf x)=c_jR(x_j)
       \min_{k\in\{j-1,j,j+1\}}L(x_k),\qquad
 L(x)=\min\{1,(x-.1)/.12\},
 \tag{10}
\]
with a missing right neighbor assigned value one.
Here \(R=1\) up to \(.45\), and
\(R(x)=400(.5-x)^2\) just above \(.45\).
The near-zero seam repair is not encountered.
The minimum uses the original row convention.

For \(0<\varepsilon<.01\), the exact cutoff bounds are
\[
 1-R(x_j)\le40\varepsilon,\qquad
 1-\min L\le(25/3)\varepsilon .
 \tag{11}
\]
Since \(|c_j|<.12\), they imply
\[
 |h_j(\mathbf x)-c_j|<\frac{29}{5}\varepsilon,\qquad
 |x_j+ih_j(\mathbf x)-(\bar x_j+ic_j)|<7\varepsilon.
 \tag{12}
\]
They allow several lower and upper crossings simultaneously.
The cut height \(h_q=c_q\) and every height in the coherent
extension stay fixed, since \(q-1,q,q+1\) remain in \(P\).
The height at \(q+1\) may change; it belongs to the literal
polynomial (8). The symbols defining the synthetic compact
component, through \(q+1\), are unchanged. Thus its residual
\(D_R\), the closing terms after their cancellation in (4),
and the fee in (3) are the same as at the clamped comparison
point. No coherent phase is continued into an unproved taper
domain.

Choose \(\zeta<\kappa_*r_0^2/4\), then choose a fixed
\(\varepsilon>0\) so that \(7\varepsilon<\delta\) from Section 2.
If some coordinate in (9) is outside \(P\), its clamped value
is in \(\partial P\), hence
\[
             \sum_{j=\ell+1}^{h}(\bar x_j-a_j)^2>r_0^2.
 \tag{13}
\]
Apply the polynomial estimate only to \(R_N^{\rm F}\) in (4).
The coherent extension and fee agree at the actual and clamped
points, so (6), (12)--(13) pay the continuation loss. If all
coordinates lie in \(P\), use (6) directly and spend no fixed
loss near the reference. We obtain the following bound:
\[
 \boxed{\quad
 \mathcal C_{R,N}^{\rm F}
 \le-\frac{\kappa_*}{2}
       \sum_{j=\ell+1}^{h}(\bar x_j-a_j)^2
          +\tau+O(\log N/N)
              \quad\hbox{throughout (9).}\quad}
 \tag{14}
\]
Both level parities are retained. For the nonplateau part of (9),
one smaller total tolerance and sufficiently large \(N\) give
the positive finite exponential reserve
\[
                   \frac{\kappa_*r_0^2}{4}
                       =\frac{289}{10^{13}}.
 \tag{15}
\]
The width and the sufficiently large level may be chosen uniformly
over the fixed finite family of admissible boundary types and pin
positions. No value of that width is inferred from finite samples.

## 4. Consequence for the actual compensated boundary

Equation (14) bounds an actual part of the right supremum in
Fourier-ended boundary windows, equation (18). It includes the
complete Fourier right cap, simultaneous shallow physical tapers,
their changed neighboring heights, the original synthetic
completion and its relative pinning fee. Together with the
[paid left shallow taper](research_mixed_left_boundary_shallow_taper.md),
it pays both outer brackets on the corresponding unselected
boundary sectors; the retained middle occupation loss in that
equation is unchanged.

The output remains \(x_0\). The conclusion does not change an
incoming height to the selected positive height, cover a deep
taper or the full incoming period, or move the protected cut
strip. Those configurations are still part of the finite boundary
problem. No ordinary closing functional or arbitrary-message
Fourier norm is replaced by the present estimate.
