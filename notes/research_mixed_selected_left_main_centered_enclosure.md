# Centering the whole left-cut/main-contour scalar bound

Research evaluation lemma, 6 November 2026. The two scalar tests in
[the left-cut/main-contour majorant](research_mixed_selected_cap_left_main_majorant.md)
can be enclosed as functions of one common complex reference
parameter. Differentiating the combined expression first cancels
the outgoing variation, the real trial gradients and, on the original
critical sheet, the private-action variation. This is a proof and
evaluation design; no scalar test, source, root or cover is run.

Throughout this note the index curvature is the fixed constant
\(\mu_s=2\pi/5\). The stronger varying curvature in the cited
majorant must not be substituted into the derivative below without
its additional derivative term.

## 1. A regular extension over one auxiliary box

Let \(\xi=u_*\) vary over a closed rectangular auxiliary box,
and put \(U=e^{2\pi i\xi}\). Use the original rational maps
\(E(U),Z(U),S(U),B(U)\), with their original logarithmic
coordinates \(e(\xi),z(\xi),s(\xi),b(\xi)\). On this box
require every map denominator to be nonzero, every coordinate
logarithm to have a fixed holomorphic branch, and every primitive
argument below to stay in \(0<\Re w<1\).
Also require
\[
 s_R:=\Re s>.2,\qquad a:=\Re z\in P=[.22,.45],
 \qquad z_H=a+iH,\quad H=7/625,
 \quad e_0=.27.
\tag{1}
\]
These conditions concern the entire auxiliary box, not merely a
coordinatewise intersection of its image with necessary reference
rectangles. They ensure that the straight parameter segments used
below are regular. They do not assert that every point is an actual
open-word reference.

To define a regular action off the actual reference set, retain the
explicit inner action
\[
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,
\tag{2}
\]
and the uneliminated original phase
\[
 \begin{split}
 \Phi(e,u,s,z,b)={}&F(e,u)+J(e+z)-J(z)-i\pi ez-g(e)\\
 &+Q(s;z,b)-g(z).
 \end{split}
\tag{3}
\]
The reference extension is evaluated at \(u=\xi\).
At every actual reference it is the original action, and its
\(e,u,s,z\) marginals vanish on the original zero lifts.
Away from that set no such vanishing is assumed.

Let \(\Psi_0(z)=\Psi(e_0,z)\), using the fixed canonical
action at the left cut. For \(\nu=0,1\) define
\[
 \mathcal L_\nu(\xi)=
 \Re\{\Psi_0(z_H)+Q(s;z_H,b)-\nu g(z_H)-\Phi(e,\xi,s,z,b)\}
                                  -2\nu\pi H.
\tag{4}
\]
At actual references this is exactly the trial action in the scalar
majorant, including \(S(.27)-S(e_*)\) and the actual private
height. The definition supplies an ordinary real differentiable
extension on the whole regular auxiliary box.

Write primes on reference coordinates for complex derivatives with
respect to \(\xi\). They can be formed directly from the
rational maps; for example
\[
 s'=-\frac{US_U}{S},\qquad
 z'=-\frac{UZ_U}{Z},\qquad
 e'=-\frac{UE_U}{E}.
\tag{5}
\]
These are exact rational derivatives, not derivatives of proposed
or numerically followed roots.

## 2. The cancellation before interval evaluation

Use the two complex target marginals
\[
 \begin{split}
 K_s={}&g'(s+z_H)-g'(s+z)+2\pi i(z_H-z),\\
 K_{z,\nu}={}&g'(e_0+z_H)+g'(s+z_H)
                    -(2+\nu)g'(z_H)+2\pi is,\\
 p_s={}&\Re K_s,\qquad \beta_\nu=\Re K_{z,\nu}.
 \end{split}
\tag{6}
\]
On the actual reference set, \(p_s=-d<0\) is the negative
index force already proved in the majorant. All logarithms in (6)
are the original regular-strip logarithms, not logarithms of a
quotient with a newly chosen lift.

Set
\[
 \mathcal R=\Phi_e e'+\Phi_z z'+\Phi_u,
\tag{7}
\]
where each partial is evaluated at \((e,\xi,s,z,b)\).
This residual is kept on an arbitrary regular auxiliary box.
It vanishes on a verified original zero-lift critical chart.

**Lemma 1.** For every real differential of the parameter,
\[
 d\mathcal L_\nu
    =\Re(K_s\,ds)+\beta_\nu\,da
                              -\Re(\mathcal R\,d\xi).
\tag{8}
\]

*Proof.* The outgoing derivative of the current trial is
\(Q_b(s;z_H,b)=g'(s+b)-g'(b)\), independent of the
incoming argument. It equals \(\Phi_b\) in (3), so the
entire \(db\) term cancels. The reference index derivative is
\(\Phi_s=Q_s(s;z,b)\). Its difference from the trial
index derivative is exactly \(K_s\), without any zero-lift
assumption. The trial incoming coordinate moves by the real
differential \(da\), giving \(\beta_\nu da\).
The remaining reference derivatives are precisely (7), with
\(du=d\xi\). This proves (8). \(\square\)

For explicit differentiation of the two real forces, put
\[
 R_1=g''(s+z_H),\quad R_0=g''(s+z),\quad
 R_e=g''(e_0+z_H),\quad R_z=g''(z_H),
\tag{9}
\]
and
\[
 \begin{split}
 \mathcal P&=(R_1-R_0)s'
                       +(\Re R_1-R_0-2\pi i)z',\\
 \mathcal Q_\nu&=(R_1+2\pi i)s'
                       +\Re\{R_e+R_1-(2+\nu)R_z\}\,z'.
 \end{split}
\tag{10}
\]
Then direct differentiation of (6), using \(da=\Re(z'd\xi)\),
gives
\[
               dp_s=\Re(\mathcal P\,d\xi),\qquad
               d\beta_\nu=\Re(\mathcal Q_\nu\,d\xi).
\tag{11}
\]
In particular the original chirp is retained by both occurrences
of \(2\pi i\) in (10).

## 3. The combined scalar derivative through clipping transitions

Keep \(\mu_s=2\pi/5\) fixed and let
\(\mu_\nu=(23+18\nu)\pi/120\). Define
\[
 \begin{split}
 \tau_s&=\operatorname{clip}(p_s/\mu_s,\ .2-s_R,\ 0),\\
 \tau_z&=\operatorname{clip}(\beta_\nu/\mu_\nu,
                                      \ .22-a,\ .45-a),\\
 \mathcal J_\nu&=\mathcal L_\nu+
       \Gamma_{\mu_s}(p_s;\ .2-s_R,\ 0)
       +\Gamma_{\mu_\nu}(\beta_\nu;\ .22-a,\ .45-a).
 \end{split}
\tag{12}
\]
At actual references this is exactly the proved scalar upper bound.
On the auxiliary box (12) is its specified extension, even if a
retained nonactual point happens to have \(p_s\ge0\).

**Lemma 2.** The extension (12) is continuously differentiable,
including at all target-clipping transitions. Its exact derivative is
\[
 d\mathcal J_\nu=\Re(\mathcal C_\nu\,d\xi),
\tag{13}
\]
where
\[
 \begin{split}
 \mathcal C_\nu={}&
  \{i\Im K_s+\mu_s\tau_s+(p_s)_+\}s'
   +\mu_\nu\tau_z z'\\
 &+\tau_s\mathcal P+\tau_z\mathcal Q_\nu-\mathcal R.
 \end{split}
\tag{14}
\]
On an actual reference chart the positive-part term and residual
vanish. Neither is silently deleted from an arbitrary auxiliary box.

*Proof.* The one-dimensional maximizer defining each quadratic gain
is unique and continuous. Differentiating its value is valid at
interior and clipped solutions; the formulas agree at transitions.
For the incoming gain the derivative is
\[
 \tau_z\,d\beta_\nu+(-\beta_\nu+\mu_\nu\tau_z)\,da.
\tag{15}
\]
For the index gain it is
\[
 \tau_s\,dp_s+
       \{-p_s+\mu_s\tau_s+(p_s)_+\}\,ds_R.
\tag{16}
\]
Indeed if \(p_s<0\), the upper displacement endpoint cannot
be its strict maximum and this is the usual centered-interval
formula. If \(p_s\ge0\), then \(\tau_s=0\), the gain
is identically zero, and the bracket in (16) is zero. The formulas
remain continuous at \(p_s=0\).

Add (15)--(16) to (8). The real trial contributions cancel, leaving
\[
 -\Im K_s\,d(\Im s)
 +(\mu_s\tau_s+(p_s)_+)\,ds_R
 +\mu_\nu\tau_z\,da
 +\tau_s\,dp_s+\tau_z\,d\beta_\nu
 -\Re(\mathcal R\,d\xi).
\tag{17}
\]
Equations (5), (11) turn this into (13)--(14). This proves the
claim across clipping transitions as well as within each branch.
\(\square\)

## 4. A centered enclosure and its exact limits

Let \(\xi_0\) be the exact rectangular center, and let
\(r_x,r_y\) be the two halfwidths. Suppose outward intervals
\(I_x,I_y\) contain \(\Re\mathcal C_\nu\) and
\(\Im\mathcal C_\nu\) throughout the whole box. Integrating
(13) along its straight segments proves
\[
 \mathcal J_\nu(\xi)\le
 \mathcal J_\nu(\xi_0)
      +r_x\max|I_x|+r_y\max|I_y|.
\tag{18}
\]
The center value may be enclosed from the literal original
primitives. The
[centered primitive lemma](research_mixed_centered_primitive_enclosure.md)
can be used for that evaluation, but (18) centers the combined
same-parameter expression before bounding its variation. No target
grid, proposed optimizer or differentiation of an approximate root
is involved.

For a valid implementation, the derivative enclosure must use the
unclipped rational-map images along these parameter segments.
Intersecting a coordinate enclosure with a necessary actual-reference
rectangle is legitimate for a pointwise source test, but does not
describe the holomorphic parameter segment in (18). Such an
intersection may not replace the images used to justify (13).
One can instead certify that the entire box image lies in the
desired ranges, or use its larger original image whenever all
regularity conditions remain valid.

Similarly, original zero lifts at actual points do not by themselves
authorize setting \(\mathcal R=0\) on an unverified auxiliary
box. Keeping (7) makes (18) valid without that inference. A separate
regular connected-chart argument may discharge those residuals,
but it must include the canonical inner action and all original
logarithmic lifts.

Finally, the optional stronger curvature
\(2\pi\min\{\Re\cot\pi s,15/53\}\) is not covered by
the fixed-curvature differentiation above. Its gain derivative has
the additional term
\(-\tau_s^2\,d\mu_s/2\); the minimum's switching set also
requires a piecewise or almost-everywhere derivative enclosure.
The fixed \(2\pi/5\) version avoids that extra requirement.

No uniform negative sign for (18), and no new complete finite-source
comparison, is asserted here. It is a correlated enclosure formula
for the two already proved sufficient scalar tests.
