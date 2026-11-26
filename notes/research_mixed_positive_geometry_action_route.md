# A route from positive path geometry to the mixed open-word action

Research assessment and analytic lemma, 5 November 2026. The positive
marked geometric solution exists for every open word in three and four.
The new critical localization concerns a different set of coordinates.
This note gives a larger injectivity chamber in which the two points
could be identified, and states the remaining range and branch
obligations. It does not assert that those obligations are satisfied.

## 1. A convex chamber using adjacent leg sums

Fix a word \(3+\epsilon_1,\ldots,3+\epsilon_m\), with
\(m\ge1\) and \(\epsilon_j\in\{0,1\}\). Use exactly the
original action \(\mathcal F_m\) in equation (1) of
[the open-word Hessian lemma](research_mixed_open_word_hessian.md).
Its legs are \(s_j,t_j\), its private legs are \(s_1,t_m\),
and its ordinary endpoint variables are \(u_L,u_R\). In particular
its endpoint term is
\[
 B(e,u)=-2J(1/2-u)-3J(u)-J(e-u),\qquad
                 J''(z)=\pi\cot\pi z.                    \tag{1}
\]

Define the open convex domain \(\mathcal C_m\) by
\[
\begin{split}
 &0<\Re s_j,\Re t_j<1/2 &&(1\le j\le m),\\
 &\Re(s_j+t_j)>1/2 &&(1\le j\le m),\\
 &\Re(t_j+s_{j+1})>1/2 &&(1\le j<m),\\
 &0<\Re u_L<\Re s_1,\qquad
   0<\Re u_R<\Re t_m.                                  \tag{2}
\end{split}
\]
There is no restriction on imaginary parts. Every argument of
\(J\) remains in its original strip \(0<\Re z<1\).

**Lemma 1.** Throughout \(\mathcal C_m\),
\(-\Re\mathcal F_m''\) is positive definite. The full
holomorphic gradient of \(\mathcal F_m\) is injective on
\(\mathcal C_m\). This is a strict pointwise assertion;
no uniform lower eigenvalue on this unbounded domain is claimed.

*Proof.* Write \(C(z)=\Re\cot\pi z\). For any finite height,
\[
 C(x+iy)=\frac{\sin(2\pi x)}
                    {\cosh(2\pi y)-\cos(2\pi x)}.        \tag{3}
\]
It is positive for \(0<x<1/2\) and negative for
\(1/2<x<1\). For
\(V(z,w)=J(z+w)-J(z)-J(w)\), the real quadratic form is
\[
 -\Re d^2V=\pi\{C(z)\,dz^2+C(w)\,dw^2
                              -C(z+w)(dz+dw)^2\}>0       \tag{4}
\]
on each ordinary pair in (2). At an endpoint vertex use instead
\(W(e,t)=J(e+t)-J(t)\), whose negative real Hessian is
\[
 -\Re d^2W=\pi\{-C(e+t)(de+dt)^2+C(t)\,dt^2\}.         \tag{5}
\]
It is positive definite under the same sum condition. No artificial
\(-J(e)\) has been inserted.

For an endpoint function (1),
\[
 -\Re d^2B=a\,du^2+b(de-du)^2,\quad
 a=\pi\Re(2\tan\pi u+3\cot\pi u)>0,\quad
 b=\pi C(e-u)>0.                                        \tag{6}
\]
Indeed \(0<\Re u<1/2\) and \(0<\Re(e-u)<1/2\).
Both real parts of tangent and cotangent are positive in the
first strip. Thus (6) is positive definite in \((e,u)\).

For \(m\ge2\), decompose the original action into the two
endpoint functions \(B\), the two endpoint vertices \(W\),
the internal vertex pairs \(V\), and all \(m-1\) shared
pairs \(V\). Add the original terms
\(-\epsilon_j[J(s_j)+J(t_j)]\) and the original purely
imaginary quadratic polynomial. The decomposition is exact: every
internal leg receives two copies of its negative own primitive,
while a private leg has none outside its endpoint function and
its type-four term. Equations (4)--(6) control every variable;
the type-four own terms are positive semidefinite. The imaginary
quadratic polynomial has zero Hermitian real part of its Hessian.
This proves the assertion also for \(m=2\), with its single
literal shared edge.

For \(m=1\), use the two functions \(B\) and the remaining
\(J(s_1+t_1)\), whose negative real Hessian is positive
semidefinite by (2). The two endpoint forms already control all
four variables. The same type-four observation applies.

For distinct points \(z,w\in\mathcal C_m\), integrate the
complex symmetric Hessian along their segment. Its Hermitian part
is its entrywise real part. Hence
\[
 \Re\bigl[(z-w)^*(-\nabla\mathcal F_m(z)
                         +\nabla\mathcal F_m(w))\bigr]>0. \tag{7}
\]
The gradients cannot coincide. \(\square\)

The quantitative localization domain in the cited Hessian theorem
is not asserted to be a subset of \(\mathcal C_m\). Membership
of its actual critical point requires the adjacent-sum inequalities
in (2), not merely the individual typed-disk bounds. Conversely,
membership in (2) requires none of those narrow height bounds.

## 2. The inverse from the already existing positive geometry

The [positive path theorem](research_positive_path_fractional_charge_cube.md)
supplies, at unit charges, the unique positive original solution
for every integer word \(n_j\ge3\). Write its angles as
\(\tau_j=a_j-iH_j\), with complete outside angles zero.
The exact equations are
\[
 \sum_{e\ni j}r_{j,e}
       =\frac{in_j}{2}\tau_j-\pi i,\qquad
 r_{j,e}=\operatorname{arsinh}
       \bigl(\tan(\tau_j/2)\cos(\tau_k/2)\bigr).        \tag{8}
\]
These retain the original logarithmic lifts. Positivity and the
core signs \(H_j>0\) are part of that theorem.

For an edge \(jk\), put
\[
 A=\cos^2(\tau_j/2),\quad B=\cos^2(\tau_k/2),\quad
 q^2=A^{-1}+B^{-1}-1,\quad
 x=\pi^{-1}\arctan(1/q),\quad X=e^{2\pi ix}.             \tag{9}
\]
The branches are the original positive ones. The
[wire-order theorem](research_positive_path_real_wire_order.md)
already proves \(0<\Re x<1/4\), \(\Im x>0\), and
\(\Re x<1/2-\Re\tau_j/(2\pi)\) at each active incidence.
It also proves \(|A|<1\) at an active endpoint. The cosine
phase bound puts \(A\) in the open upper-right quadrant;
a complete endpoint has \(A=1\).

The algebraic inverse for the leg at endpoint \(j\) is
\[
 U_{j,e}=\frac{1-X}{1+X+2X\cos\tau_j},
                  s_{j,e}=\frac{i}{2\pi}\Log U_{j,e}.     \tag{10}
\]
It is the inverse appearing in the calibrated type-three and
type-four vertex identities. Choosing its original logarithm and
verifying its image are part of the remaining comparison.

The rational function in (10) is finite and nonzero on the
positive path family. For completeness, \(X=(q+i)/(q-i)\),
so (10) becomes
\[
                   U_{j,e}=\frac{-i}{2qA+i(2A-1)}.        \tag{11}
\]
If its denominator vanished, squaring and using (9) would give
\(B=-4A^2\). At an active endpoint the latter has negative
imaginary part, whereas \(B\) has nonnegative imaginary part.
At a complete endpoint it equals \(-4\), also impossible.
The numerator is nonzero. This excludes a pole or zero; it does
not establish a desired argument range for the logarithm.

The proposed identification now has a precise remaining target:
prove that the inverse legs (10), with the complete outside wires
as \(u_L,u_R\), satisfy (2), and that (8) gives the original
zero gradient of \(\mathcal F_m\) in those logarithms. If
the localized source critical point also lies in (2), Lemma 1
identifies the two points. No new geometric existence theorem is
required for this route.

## 3. Why positivity and the coarse ranges do not suffice

There is an exact positive edge for which the adjacent-sum
inequality fails after (10). Set both endpoint angles to
\(\tau=2\pi/3\). Then
\[
 A=B=1/4,\qquad q=\sqrt7>\sqrt6
 =\sqrt{(\Re\tan(\tau/2))^2+(\Re\tan(\tau/2))^2}.
                                                               \tag{12}
\]
The strict inequality is exactly the
[eight-tetrahedron positivity criterion](research_positive_edge_global_monotonicity.md).
The original stationary wire and both inverse legs are
\[
 X=\frac34+\frac{i\sqrt7}{4},\qquad
 U=1-X=\frac14-\frac{i\sqrt7}{4},\qquad
 \Re(s_{j,e}+s_{k,e})=\frac{\arctan\sqrt7}{\pi}<\frac12.
                                                               \tag{13}
\]
Here the logarithm of \(U\) has argument in \((-\pi/2,0)\).
Also \(\Re x=\arctan(1/\sqrt7)/\pi<1/6\), which satisfies
the original real wire order at these angles.

Both positivity and the strict failure in (13) persist when both
angles are replaced by \(2\pi/3-i\delta\) for sufficiently
small \(\delta>0\). This perturbation has strict negative
angle heights, \(|\cos(\tau/2)|<1\), arbitrarily small
positive cosine phase, and the established coarse upper height
bound. Thus adding those qualitative conditions does not prove (2).

**This is not a unit-filling solution.** At \(\delta=0\),
each return is the positive real number
\(\operatorname{arsinh}(\sqrt3/2)\), whereas the real part
of (8) would require their sum to equal \(n_jH_j/2=0\).
The same mismatch persists for small \(\delta>0\) with a
fixed number of these incidences and \(n_j\in\{3,4\}\).
The example refutes an inference from positivity and coarse
ranges alone; it neither refutes the proposed unit-period lemma
nor concerns a finite-source cancellation estimate.

## 4. The remaining absolute action identification

Even after the range comparison, the original vertex identities
must be retained with their logarithmic lifts and constants. The
existing [all-three action calibration](research_three_chain_action_volume_calibration.md)
and [mixed-reference calibration](research_mixed_contracted_phase.md#5-absolute-action-under-the-exact-wire-contraction)
give them on their specified connected charts. One must prove that
the geometric inverses above lie on those calibrated continuations,
or establish an equivalent exact identity on a chart containing them.
Exponentiated stationary equations alone do not do this.

The ordinary endpoint identity is already complete:
\[
 S(e)-\frac{i\pi}{2}(e-e^2)
       =\ell_e(u_c(e))+b(u_c(e),0),                       \tag{14}
\]
with zero complex additive constant, by
[the endpoint action calibration](research_mixed_endpoint_action_calibration.md).
Its chart requirements still have to be checked for any geometric
inverse to which it is applied. The existing full-\(E\) and
\(E_{\mathrm{cap}}\) specializations cover the stated source
images without a new constant choice.

Once the original vertex and wire identities have been summed,
[the positive-edge volume identity](research_positive_edge_volume_identity.md#4-a-stationary-action-on-an-arbitrary-selected-region)
and [marked completion](research_positive_point_marked_completion.md)
apply to the existing solution (8). They retain the original
carriers \(\eta_j\), disk frames and primitive slopes
\(\mu_j+p_j\lambda_j\), where \(n_j=\eta_j-2p_j\).
The calibrated purely imaginary source constants and the literal
finite carrier scalars must remain in the action/amplitude accounting.

A fractional-charge path does not by itself supply the missing unit
vertex calibration: its angular linear term is \(-i\chi_j\tau_j\),
whereas the present source uses \(-i\tau_j\). The unit-period
image and original branch identification remain explicit unproved
obligations. No old critical roots or numerical covers were
reconstructed for this assessment.
