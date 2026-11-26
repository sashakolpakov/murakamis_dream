# A sharper lower bound for the actual first-cap plane

Research deduction, 8 November 2026. The original bare first-cap
supporting plane at incoming real coordinate \(1/2\), and at the
actual negative incoming height of the ordinary-next family, is
strictly greater than \(7/8\). This is a bound on the already
calibrated source plane. It neither asserts a lower bound for an
absolute finite cap sum nor replaces the actual following action.

Only written analytic inequalities and one rational consequence of
an already printed scalar enclosure are used. No source, root,
primitive, or saved numerical computation is evaluated or replayed.

## 1. The same actual plane and source profile

Use the canonical ordinary-next references and source allocation of
[calibrated horizontal transport](research_mixed_next_calibrated_horizontal_transport.md),
Section 1. The first cap is the original type-three cap, and both
values of the subsequent type flag \(\beta\in\{0,1\}\) are allowed.
Write its actual attached incoming coordinate as
\[
 a_*=A+ih_a,\qquad -9/125<h_a<0,
\]
and its actual private endpoint coordinate as \(e_*\), with
\[
 h_e=\Im e_*\in[-11/200,1/25].
 \tag{1}
\]
The latter is the original endpoint rectangle; its height is not
replaced by a freely chosen critical height.

Let \(T_0\) be the original bare cap action, and let \(p_L\) be
the actual first conditional incoming marginal. Thus
\(T_0'(a_*)+p_L=0\). Retain exactly
\[
 B_*=\Re T_0(a_*)-\Re p_L(1/2-A)
                       -\frac{(1/2-A)^2}{2500000}.
 \tag{2}
\]
All normals, phase lifts and additive constants are those in
[complete upper-target cap support](research_mixed_cap_upper_target_completion.md).
Its equation (4), in the bare type-three case, gives
\[
 B_*\ \ge\
 \Re\Psi(7/20+ih_e,\,1/2+ih_a),
 \tag{3}
\]
where
\[
 \Psi(e,a)=S(e)+J(e+a)-J(a)-i\pi ae.
 \tag{4}
\]
Indeed \(7/20\) is in the same retained real private window
\([27/100,49/100]\), and (3) is the original main-profile
support inequality. No constituent bound is inferred from a
signed finite sum.

## 2. A lower supporting tangent in the two heights

At fixed real coordinates \((E,a_R)=(7/20,1/2)\), set
\[
 \Phi(H,h)=\Re\Psi(E+iH,1/2+ih).
\]
The joint negative real Hessian in
[upper-target extension, Lemma 1](research_mixed_cap_upper_target_extension.md)
is positive on the entire segment from \((H,h)=(0,0)\) to
\((h_e,h_a)\). Consequently \(\Phi\) is convex on this
segment and has its ordinary lower supporting tangent:
\[
 \Phi(h_e,h_a)\ge
 \Phi(0,0)-h_e\Im\Psi_e(E,1/2)
                         -h_a\Im\Psi_a(E,1/2).
 \tag{5}
\]
This use of height convexity is at incoming real coordinate
\(1/2\). It makes no assertion about the Hessian at a displaced
incoming real coordinate.

The original logarithmic derivatives give
\[
 \Im\Psi_a(E,1/2)=-\pi E=-\frac{7\pi}{20}.
 \tag{6}
\]
For the other derivative, the original endpoint branch and
equations (26)--(27) of
[the complete half-cap source](research_mixed_half_face_complete_cap_packet.md)
give
\[
 \Psi_e(E,1/2)
 =-J'(E-u_c(E))+i\pi u_c(E)+J'(E+1/2)-i\pi/2,
 \tag{7}
\]
with
\[
 17/100<\Re u_c(E)<28/100,\qquad \Im u_c(E)>0,\qquad
                     0<\Re(E-u_c(E))<1/2.
 \tag{8}
\]
The original sine logarithm at \(E-u_c(E)\) has argument
strictly between \(-\pi/2\) and zero. The logarithm at
\(E+1/2=17/20\) is real. It follows directly, on the
original zero lift, that
\[
 -\frac{33\pi}{100}<\Im\Psi_e(E,1/2)<\frac{28\pi}{100},
 \qquad |\Im\Psi_e(E,1/2)|<\frac\pi3.
 \tag{9}
\]
Thus no complex derivative is obtained by differentiating a
bound on the modulus.

The scalar display in Section 1, equation (2), of
[the half-cap action upper bound](research_mixed_half_face_cap_action_upper.md)
already records
\[
                    \lambda(7/20)=\Re S(7/20)>\frac{108}{125}.
 \tag{10}
\]
This is solely a rational consequence of that printed enclosure;
its saved replay is not rerun or otherwise evaluated here.
Also \(J(17/20)=-J(3/20)\), \(J(1/2)=0\), and
\[
 \begin{split}
 -J(3/20)
 &\ge-\int_0^{3/20}\log(2\pi s)\,ds\\
 &=\frac3{20}\left(1-\log\frac{3\pi}{10}\right)
 >\frac3{20},
 \end{split}
 \tag{11}
\]
since \(2\sin\pi s\le2\pi s\) and \(3\pi/10<1\).
Equations (4), (10) and (11) therefore imply
\[
                         \Phi(0,0)>\frac{507}{500}.
 \tag{12}
\]

## 3. The uniform rational floor

Combining (1), (5), (6), (9) and (12) yields
\[
 \begin{split}
 B_*
 &>\frac{507}{500}
       -\frac{11\pi}{600}-\frac{63\pi}{2500}\\
 &=\frac{507}{500}-\frac{653\pi}{15000}\\
 &>\frac{507}{500}-\frac{14366}{105000}
   =\frac{11513}{13125}
   >\boxed{\frac78}.
 \end{split}
 \tag{13}
\]
The penultimate comparison uses \(\pi<22/7\). The last has
the exact positive difference
\[
               \frac{11513}{13125}-\frac78
                         =\frac{229}{105000}>0.
 \tag{14}
\]
This floor is uniform on the same actual following family as
(2), including both next types. It does not enlarge that family
to independently varying reference coordinates.

The original complete cap upper estimate with plane \(B_*\),
its all-real ordinary-color scope, both level parities and fixed
ordinary derivatives are unchanged. Its local complex-color and
fixed-base mixed-derivative consequences are also unchanged.
The lower bound (13) concerns the complete-color phase used to
define and calibrate this common upper plane; it is not a
nonvanishing assertion for other ordinary colors.

In particular an independently proved upper rate strictly below
\(7/8\) for any complete or positive partial cap source may be
compared with the original plane \(B_*\), while retaining the
original conditional, Fourier and outgoing source allocation.
That additional cap estimate and the actual following-action
comparison must still be supplied in their own source domains.
