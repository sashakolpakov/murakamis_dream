# Complete-color critical values and the additive filling condition

Research note, 6 November 2026.

For the fully expanded original signed-crossing source of a fixed knot,
the regular full critical-value comparison is already global. It is not
restricted to positive shapes. A collapsed filling phase has a different
remaining identification problem. At a unit longitude, its scalar
eigenvalue equation can lose the additive part of the actual peripheral
matrix. The original q-Hahn coupon below gives an exact example of this
loss, with regular simple internal roots.

No statement here asserts that this coupon is a stationary point of a
closed knot source, or that it contributes to a finite quantum period.

## 1. The global result which is already available

Fix a finite signed diagram of a hyperbolic knot \(K\), including its
original closure and peripheral marking. Arbitrary fixed signed powers
may be expanded into their literal signed crossings, by
[the exact compiler, Section 1](research_arbitrary_power_source_compilation.md).
This step preserves the finite source, including its normal data.

For its full-Psi source, retain every Gaussian, coupled cap and integer
logarithmic mark. At any finite regular **full** critical point, the
[rational crossing and wall calculation](actual_wall_critical_regulator.md)
and [coupled-cap relation](actual_coupled_caps_interval_source.md) give
the actual Wirtinger representation of \(\pi_1(S^3\setminus K)\).
Complete color makes its meridian unipotent. A noncentral meridian has
unipotent peripheral centralizer; a central knot meridian makes the
whole PSL representation trivial by normal generation. Thus the
representation is boundary-parabolic in either case.

With \(W\) the original action in \(\exp(NW/(2\pi i))\), the exact
identity is
\[
 \Im W-\sum_j\epsilon_jD(z_j)
       =\Re Z\cdot\Im\nabla W.
 \tag{1}
\]
Consistent changes of logarithmic sheet retain their explicit integer
marks. Full stationarity and the marked fundamental-cycle calculation
therefore give
\[
 \Re\frac{W}{2\pi i}
   =\frac{\operatorname{Vol}(\rho)}{2\pi}
   \le \frac{\operatorname{Vol}(S^3\setminus K)}{2\pi}.
 \tag{2}
\]
Neither negative developed tetrahedra nor nonprincipal marked sheets
invalidate (1)--(2). The
[saturated critical compactification](saturated_critical_regulator_compactification.md)
already proves that the regulator takes finitely many values and
extends with those values to the joint shape closure of genuine regular
critical points. There is no new compactness assertion here.

These statements apply to the regular full critical scheme of the
specified source. They do not identify every constrained endpoint,
escaping approximate critical configuration, or saddle of another
interpolation with that scheme. The full source also retains its ray
and cut currents:
[full-Psi cycle, Section 7](actual_full_psi_scalar_flow_cycle.md).
Even a regular physical cap can force an intermediate fusion chart
to degenerate; the coefficient peeling in the
[cap construction, Section 5](actual_coupled_caps_interval_source.md)
is part of the source and cannot be replaced by a fictitious independent
regular fusion saddle.

## 2. The exact additive equation at a parabolic filling longitude

Use the original endpoint coupon of
[the endpoint regulator, Sections 2--3](actual_augmented_plat_endpoint_regulator.md).
Let its ordered main-pair product be
\[
 P=-I+H,\qquad H\ne0,\qquad H^2=0.
 \tag{3}
\]
Its actual main-pair transport is \(C=I+cH\). For retained half twist
\(\epsilon\in\{0,1,-1\}\), its physical auxiliary meridian is, in PSL,
\[
 C_{\rm aux}=I+(\epsilon/2-c)H.
 \tag{4}
\]
The primitive disk longitude is \(P\). These are literal matrices of the
original threading word; they are not chosen solely by eigenvalue.

For any integer \(p\), including negative integers,
\[
 P^p=(-1)^p(I-pH),\qquad
 C_{\rm aux}P^p\sim I+(\epsilon/2-c-p)H.
 \tag{5}
\]
Consequently this peripheral pair kills the primitive filling slope if
and only if
\[
                         c=\epsilon/2-p.
 \tag{6}
\]
Every matrix in (5) has unit projective eigenvalue, regardless of (6).
Thus the scalar filling multiplier equation omits exactly one additive
condition at this noncentral parabolic longitude. This is a matrix-level
statement, independent of a choice of logarithmic sheet.

## 3. An explicit regular original coupon violating the missing equation

In the endpoint's rational chart take
\[
 T=2,\qquad a=2,\qquad b=3.
 \tag{7}
\]
The actual two q-Hahn roots and magnetic exponentials are
\[
 Z=\frac13,\quad W=\frac12,\quad
 U=\frac29,\quad V=\frac8{19}.
 \tag{8}
\]
At \(J=-1\), the internal equation from the original normalized phase
reduces to
\[
 {\cal P}(X,Y)
   =\{X(T+1)-4T\}Y^2+2X(T-1)Y+X(T+1)=0.
 \tag{9}
\]
Both pairs in (8) solve (9). Their \(Y\) derivatives are respectively
\(-40/9\) and \(-112/19\), so these are simple roots. All factorial
arguments of the endpoint symbol are different from \(0,1,\infty\);
for example its two six-shape lists are
\[
 \left(\frac29,9,\frac13,-3,\frac23,-3\right),\qquad
 \left(\frac8{19},\frac{19}4,\frac12,-2,\frac{16}{19},-\frac{19}8\right).
 \tag{10}
\]
The displayed denominators of the original rational head map are
nonzero. Its incoming momentum ratio is \(Y(V,W)=33/5\), its outgoing
ratio is \(Y(U,Z)=7/2\), and its normalization is \(D=10/27\).
In particular the original total entries are
\[
 F_{\rm tot}=\frac{27}{5},\qquad E_{\rm tot}=-\frac56,\qquad
 P=\begin{pmatrix}1/2&-5/6\\27/10&-5/2\end{pmatrix}.
 \tag{11}
\]
Thus \(H=P+I\) is nonzero and square-zero. The actual endpoint
transport coefficient is
\[
 c=\frac{2Tab-Ta-Tb+a+b-2}
          {2(T+1)(a-1)(b-1)}=\frac{17}{12}.
 \tag{12}
\]
The apparent division by \(J-J^{-1}\) is not used: the removable
endpoint transport is the regular \(I+cH\) of (12).

The actual channel eigenratio obeys \(R_0=1\), and hence
\(R_\epsilon=R_0(-J)^\epsilon=1\), as an identity on this endpoint
root chart. Nevertheless,
\[
 \epsilon/2-\frac{17}{12}-p
       =\frac{6\epsilon-17-12p}{12}\ne0
       \qquad(p\in\mathbb Z).
 \tag{13}
\]
For every integer \(p\), (5) is therefore a nontrivial unipotent in
PSL. All scalar eigenvalue filling equations hold, but the primitive
filling relation fails.

This example concerns the internal-root and peripheral part of an
actual coupon. It does not impose the remaining magnetic equations of
a closed word or assert their solvability. Its role is to rule out a
local implication needed by an overbroad global argument.

## 4. Consequence for short-filling continuation

The signed circle-tree action comparison in
[the positive-edge volume identity, Section 9](research_positive_edge_volume_identity.md)
correctly assumes a nonunit selected longitude when deducing the
filled-group relation from its eigenvalue equation. Equations (3)--(13)
exhibit the missing datum when that assumption fails. A global extension
must either retain the actual matrix filling equation, prove the
additive condition (6) from the remaining original equations, or show
that the offending source strata do not contribute. Equality of two
finite source formulas alone does not identify their stationary schemes.

There is a separate parameter obstruction. At intermediate cone charge
\(0<\lambda<1\), the equation
\(U+pV=-2\pi i\lambda\) generally does not kill the primitive slope.
The representation is then of the unfilled exterior, not of the final
integer-filled knot. Its complete-parent volume bound does not compare
it with the smaller geometric cone action. This limitation, including
the original relative-cycle requirements, is already stated in
[dominant saddle transport, Section 7](research_dominant_saddle_transport.md).

Thus regular critical-value control for the direct closed source is
already available for arbitrary fixed signed powers. It does not supply
global short-filling continuation, a nonzero coefficient on the
maximal-action class, or cancellation of the remaining source ends.
No new source asymptotic or finite-exception theorem follows here.
