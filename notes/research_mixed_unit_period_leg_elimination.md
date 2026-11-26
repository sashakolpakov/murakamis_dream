# Exact elimination of an original unit period into mixed leg equations

Research lemma, 5 November 2026. The actual positive unit filling equation
at a three- or four-vertex implies the corresponding algebraic source
relations after the inverse leg transformation. The argument excludes
all extraneous factors using the original positive geometry. It does
not infer the two source logarithmic lifts from their exponentials.

## 1. Original angles, returns and inverse legs

Take a degree-two selected vertex in the original positive path
solution, including its complete outside incidence if it is an end.
Let its angle be \(\tau\), its power be \(n\in\{3,4\}\),
and its two original stationary wires be \(x,y\). Write
\[
 Z=e^{i\tau},\qquad W=Z+Z^{-1}=2\cos\tau,
 \qquad X=e^{2\pi ix},\quad Y=e^{2\pi iy}.                \tag{1}
\]
The [positive path theorem](research_positive_path_fractional_charge_cube.md)
gives \(0<\Re\tau<\pi\), \(\Im\tau<0\), so
\(|Z|>1\) and in particular \(Z\notin\{0,1,-1\}\).
The [original wire-order theorem](research_positive_path_real_wire_order.md)
fixes both wire branches and the exact return identities
\[
 e^{2r_x}=\frac{X+Z}{1+XZ},\qquad
 e^{2r_y}=\frac{Y+Z}{1+YZ},\qquad
 r_x+r_y=\frac{in\tau}{2}-\pi i.                        \tag{2}
\]
All four factors in the two ratios are nonzero on the original
regular positive chart. The last equality is the full unit-period
equation, not an equation with an unspecified integer charge.

Define the algebraic inverse legs by
\[
 U=\frac{1-X}{1+X(1+W)},\qquad
 V=\frac{1-Y}{1+Y(1+W)}.                                \tag{3}
\]
The denominators and numerators are nonzero by Section 2 of
[the positive-geometry route assessment](research_mixed_positive_geometry_action_route.md).
That proof uses the original positive cosine quadrants and excludes
a denominator zero by the impossible relation \(B=-4A^2\).
Consequently (3) introduces no zero or pole on this family.

## 2. The exact factors and source relations

**Lemma 1.** At the original positive unit solution,
\[
 \boxed{\quad
 W=UV-U-V-1\quad(n=3),\qquad
 W=-U-V\quad(n=4).
 \quad}                                                 \tag{4}
\]
Put \(\epsilon=n-3\). The two exponentiated source equations
are exactly
\[
 X(1-UV)=(1-U)^\epsilon(1-XU),\qquad
 Y(1-UV)=(1-V)^\epsilon(1-YV).                           \tag{5}
\]

*Proof.* Exponentiating the already fixed last equation of (2)
gives
\[
 P_n:=Z^n(1+XZ)(1+YZ)-(X+Z)(Y+Z)=0.                     \tag{6}
\]
Let \(D_X=1+X(1+W)\). Directly from (3),
\[
 1+U(1+W)=\frac{2+W}{D_X}
       =\frac{(Z+1)^2}{ZD_X}\ne0,
 \qquad X=\frac{1-U}{1+U(1+W)},                         \tag{7}
\]
and likewise for \(V,Y\). Thus the substitution is reversible.
Set \(d_U=UZ^2+UZ+U+Z\), and define \(d_V\) similarly.
They are nonzero by (7). Substitution in (6) and clearing these
denominators gives the exact identities
\[
\begin{split}
 P_3&=\frac{-Z^2(Z-1)(Z+1)^2}
                 {d_Ud_V}
       [UVZ-UZ-VZ-Z^2-Z-1],\\
 P_4&=\frac{Z^2(Z-1)(Z+1)^3}
                 {d_Ud_V}
       [UZ+VZ+Z^2+1].                                   \tag{8}
\end{split}
\]
None of the displayed prefactors vanishes. Dividing the final
factor by \(Z\) proves (4). No root such as \(Z=1\) or
\(Z=-1\) has been substituted for the positive solution.

For type three, (7) and (4) give
\(X=(1+U-UV)^{-1}\). For type four they give
\(X=(1-U)/(1+U-U^2-UV)\). These are precisely (5), and
the second equation follows by transposition. The cancellation
in the first case is legitimate: \(U=1\) in (3) would force
\(W=-2\), hence \(Z=-1\), which was excluded.

There are no hidden zero logarithm arguments in (5). Indeed
\[
 1-XU=\frac{1+WX+X^2}{D_X}
      =\frac{(1+XZ)(X+Z)}{ZD_X}\ne0.                    \tag{9}
\]
The analogous formula applies to \(1-YV\). Also \(1-U\)
and \(1-V\) are nonzero by the preceding argument. Since
\(X,Y\ne0\), (5) now implies \(1-UV\ne0\).
This proves all stated algebraic assertions. \(\square\)

## 3. What remains for the original zero logarithmic lifts

Suppose that logarithms of \(U,V\) have been chosen so that
\(s=i\Log U/(2\pi)\), \(t=i\Log V/(2\pi)\) lie in a
regular source chart. Use the original primitives in
[the retained vertex action](research_mixed_contracted_phase.md#5-absolute-action-under-the-exact-wire-contraction):
\[
 \mathcal V_n(s,t;x,y)
  =g(s+t)-\epsilon\{g(s)+g(t)\}
                         +\ell_s(x)+\ell_t(y),\qquad
 g(z)=J(z)+i\pi(z-z^2)/2.                               \tag{10}
\]
Its two actual derivatives, with those same continued logarithms, are
\[
\begin{split}
 f_s&=\Log(1-UV)-\epsilon\Log(1-U)
                         +2\pi ix-\Log(1-XU),\\
 f_t&=\Log(1-UV)-\epsilon\Log(1-V)
                         +2\pi iy-\Log(1-YV).           \tag{11}
\end{split}
\]
Equations (5) prove only
\[
                  f_s=2\pi i k_s,\qquad
                  f_t=2\pi i k_t,\qquad k_s,k_t\in\mathbb Z.
                                                               \tag{12}
\]
They do not by themselves prove \(k_s=k_t=0\). In a connected
regular chart of these unit solutions the two integers are locally
constant. Thus either of the following additional inputs would
identify the original critical branch:

- a connected continuation within that chart to an already calibrated
  type-three or type-four point where both integers are zero; or
- direct bounds \(|\Im f_s|<2\pi\), \(|\Im f_t|<2\pi\)
  using the original logarithms throughout the proposed image.

For example, where the logarithms displayed in (11) are
principal, its imaginary part is exactly the corresponding sum of
their principal arguments and \(2\pi\Re x\) or
\(2\pi\Re y\). That supplies an explicit argument inequality
to check; it is not a new permission to reset the original logs.
The source chart inclusion and the required bound or continuation
have not been established here for all mixed open words.

The unit angular period in (2) is already fixed; this remaining
integer problem arises from changing to the retained source
coordinates. A fractional-charge path would change that period and
does not supply the missing unit-chart continuation. The absolute
vertex constants also remain those of the existing calibrated
identities, rather than being determined by (4) or (5).

This lemma supplies the exact algebraic part of the
[positive-geometry comparison route](research_mixed_positive_geometry_action_route.md).
It proves neither the pair-sum chamber inclusion, the missing zero
source lifts, nor an action-to-volume or finite-source conclusion.
The factorization (8) is an elementary polynomial identity and
requires no new root search or parameter cover.
