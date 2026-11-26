# Exact references for the two-selected terminal window

Research deduction, 6 November 2026. The existing five-variable
canonical terminal family determines the preceding own-four ordinary
vertex by two rational backward transfers. On explicitly filtered
parameters these recover the original zero logarithmic lifts, not
merely exponentiated critical equations. The resulting parameter set
is exactly the image of a unique seven-variable canonical window.
Every actual suffix of types \((3+\gamma,4,4,3+\epsilon)\) is included.
No new root, numerical enclosure, or selected-height sign is asserted.

## 1. Original domains and the already constructed family

Use the original primitive
\[
 g'(z)=\operatorname{Log}(1-e^{-2\pi iz}),\qquad
 g''(z)=\pi\cot(\pi z)-i\pi
 \tag{1}
\]
on its prescribed regular strip. Retain
\[
 \begin{split}
 D_3&=\{|z-(7/20-i/100)|\le9/100\},&
 P_3&=\{|z-(7/20-i/100)|\le83/1000\},\\
 D_4&=\{|z-(3/10-13i/250)|\le8/125\},&
 P_4&=\{|z-(3/10-13i/250)|\le3/50\},\\
 K_3&=P_3\cap\{-9/125\le\Im z\le17/250,\
                         \Re z-3\Im z\le76/125\},\\
 K_4&=P_4\cap\{-27/250\le\Im z\le-1/1000\},\\
 O_4&=P_4\cap\{-51/500\le\Im z\le-1/1000\}.
 \end{split}
 \tag{2}
\]
Thus \(O_4\subset K_4\subset\operatorname{int}D_4\). The distinction
is useful: \(O_4\) is a necessary ordinary-image domain, whereas
\(K_4\) also accommodates attached legs.

For each terminal flag \(\epsilon\in\{0,1\}\), let
\[
 q_\epsilon(b)=(e(b),\xi(b),t(b),a(b),s(b)),\qquad b\in D_4,
 \tag{3}
\]
be the original canonical suffix from
[the five-variable construction, Section 1](research_mixed_terminal_horizontal_envelope_diagnostic.md).
The endpoint has type \(3+\epsilon\), and its preceding ordinary
vertex has type four. The original five unscaled gradient equations
vanish, and the branch is holomorphic near the entire closed disk.
The [whole-disk enclosures](research_mixed_terminal_all_input_affine_enclosures.md)
and [posterior refinement](research_mixed_terminal_quadratic_residual_refinement.md)
refer to this same branch; they are not needed to establish its existence.

In particular the original ordinary map gives
\[
       a(b),s(b)\in\operatorname{int}P_4,\qquad
       -51/500<\Im a(b),\Im s(b)<-1/1000.
 \tag{4}
\]
These are full-bidisk image bounds, proved before the cyclic
specialization in
[critical height bounds, Section 1](research_mixed_cyclic_critical_height_bounds.md).
Their real parts lie strictly between \(.24\) and \(.36\).

Adjoin one more own-four ordinary vertex, with index \(r\), retained
leg \(b\), and external input \(c\) of type \(3+\gamma\).
The two additional original equations are
\[
 \begin{split}
 f_b&=g'(r+b)+g'(s+b)-3g'(b)+2\pi i s=0,\\
 f_r&=g'(r+c)+g'(r+b)-3g'(r)+2\pi i c=0.
 \end{split}
 \tag{5}
\]
The chirps in (5) fix the orientation. Neither equation depends on
\(\gamma\); that flag specifies the allowed external disk and its
allocated boundary weight.

## 2. Rational reconstruction and zero logarithmic lifts

Put \(B=e^{-2\pi ib}\), \(S=e^{-2\pi is(b)}\), and define
\[
 R(b)=\frac{1-SB-S(1-B)^3}{B(1-SB)},\qquad
 C(b)=\frac{1-RB}{R(1-RB)+(1-R)^3}.
 \tag{6}
\]
These are the exponent-three backward transfer from
[the original rational reference curve](research_mixed_second_selected_reference_curve.md),
now applied to the preceding ordinary vertex. They are rational in
\((S,B)\), not asserted to be rational functions of the coordinate \(b\).
Whenever their denominators are nonzero, they satisfy exactly
\[
 (1-RB)(1-SB)=S(1-B)^3,\qquad
 (1-RC)(1-RB)=C(1-R)^3.
 \tag{7}
\]
Conversely (7) uniquely determines \(R,C\) from \(S,B\) on this
regular locus.

Define \(\Omega_{\gamma,\epsilon}\) to consist of \(b\in O_4\)
such that the two denominators in (6) are nonzero,
\(\Im R<0,\Im C<0\), and the principal decodings
\[
          r(b)=-\frac{\operatorname{Log}R(b)}{2\pi i}\in O_4,
 \qquad   c(b)=-\frac{\operatorname{Log}C(b)}{2\pi i}
                                                       \in D_{3+\gamma}
 \tag{8}
\]
hold. Define its actual-input part by
\[
 \Omega^K_{\gamma,\epsilon}
       =\{b\in\Omega_{\gamma,\epsilon}:c(b)\in K_{3+\gamma}\}.
 \tag{9}
\]
The half-plane signs in (8) choose \(0<\Re r,\Re c<1/2\).
No logarithm is assigned to an excluded or branch-uncertain point.

**Lemma 1.** At every point of \(\Omega_{\gamma,\epsilon}\),
both equations (5) have their original zero logarithmic lift.

*Proof.* Equation (7) says that each exponential \(\exp f_b,\exp f_r\)
equals one. All original logarithms are regular on the stated
coordinate domains. It remains to bound their imaginary parts.

For \(z\in O_4\), write \(z=x+ih\). Since \(h<0\) and
\(.24\le x\le.36\),
\[
       0<\Im g'(z)<\pi(1/2-x)\le13\pi/50.
 \tag{10}
\]
This follows by increasing the radius in
\(1-\rho e^{-2\pi ix}\) from \(0<\rho<1\) to one; its argument
increases to \(\pi(1/2-x)\).
For \(r+b\) and \(s+b\), the real part is in \([.48,.72]\).
The cosine of twice its \(\pi\)-multiple is negative, so the
complex number inside the logarithm has positive real part.
Consequently each logarithm has imaginary part in
\((-\pi/2,\pi/2)\). It follows that
\[
       -13\pi/10<\Im f_b<43\pi/25,
 \tag{11}
\]
where the positive chirp contributes \(2\pi\Re s\in(.48\pi,.72\pi)\).
In particular \(-2\pi<\Im f_b<2\pi\).

For the other sum, \(r+c\) has real part in \([.476,.80]\)
and imaginary part below \(.079\). On this real interval
\(\cos(2\pi\Re(r+c))\le\cos(2\pi/5)<1/3\). Also
\[
 e^{2\pi\Im(r+c)}<e^{.16\pi}<2:
 \quad .16\pi<2/3<\log 2.
 \tag{12}
\]
Here \(\pi<22/7\) gives the first inequality, and
\(\log2=2\operatorname{atanh}(1/3)>2/3\) the second.
Thus the real part of \(1-e^{-2\pi i(r+c)}\) exceeds \(1/3\).
Its principal argument is again in \((-\pi/2,\pi/2)\).
As \(.236\le\Re c\le.44\), (10) gives
\[
       -327\pi/250<\Im f_r<47\pi/25.
 \tag{13}
\]
Both bounds lie strictly between \(-2\pi\) and \(2\pi\).
The only possible multiples of \(2\pi i\) for \(f_b,f_r\)
are therefore zero. This proves the original lifts, rather than
assuming that exponentiation preserved them. \(\square\)

## 3. Exact canonical image and actual suffix coverage

**Proposition 2.** For every \(c\in D_{3+\gamma}\), there is a
unique original seven-variable canonical reference
\[
       (e,\xi,t,a,s,b,r)\in E\times U\times Q^5
 \tag{14}
\]
solving the five equations of (3) and (5). Here
\(E=[.33,.47]+i[-.09,.08]\),
\(U=[.21,.25]+i[.01,.10]\), and
\(Q=[.23,.45]+i[-.12,.12]\).
Its \(b\)-coordinate is in the interior of \(O_4\).
The map \(c\mapsto b\) is holomorphic and injective on a neighborhood
of the closed disk after restricting to that canonical branch.
Its image of \(D_{3+\gamma}\) is exactly
\(\Omega_{\gamma,\epsilon}\); its image of \(K_{3+\gamma}\)
is exactly \(\Omega^K_{\gamma,\epsilon}\).

*Proof.* Use the established endpoint and ordinary maps to update
the disjoint groups
\[
 (e,\xi,t)=\operatorname{endpoint}_\epsilon(a),\qquad
 (s,a)=B_1(b,t),\qquad (r,b)=B_1(c,s),
 \tag{15}
\]
with the output order chosen by adjacency in (5).
The endpoint coordinates lie in their original endpoint rectangles
and typed disk, and every ordinary output lies in its typed disk.
Thus (15) is a continuous self-map of a compact convex product.
Brouwer gives a fixed point of the original logarithmic equations.
The construction is the reversed counterpart of
[the seven-variable prefix construction, Section 4](research_mixed_second_selected_reference_curve.md).

The seven-variable Jacobian is a principal submatrix of the
[original length-four Hessian](research_mixed_open_word_hessian.md),
with the first attached leg \(c\) held fixed. Inactive first-end
coordinates may be fixed anywhere in their original domains;
their contributions do not change this principal submatrix.
Its negative real part exceeds \((6\pi/49)I_7\) on (14).
Complex-gradient injectivity therefore gives uniqueness on that
whole convex product. The implicit function theorem and uniqueness
give a holomorphic branch near the closed input disk.

The full-bidisk image bounds apply to both ordinary vertices in
(15), giving \(r,b,s,a\in\operatorname{int}P_4\) and the strict
height bounds (4). The last five coordinates solve (3) for this
\(b\in D_4\), so uniqueness identifies them with \(q_\epsilon(b)\).
Exponentiating the two remaining zero-lift equations gives (7),
and solving them gives (6). All denominators are nonzero: the
original strip excludes \(1-SB=0\), and the second denominator
equals \((1-RB)/C\ne0\). The principal decodings are exactly
the original \(r,c\). Hence the canonical \(b\) lies in \(\Omega\).

Conversely, a point of \(\Omega\), together with (3) and (8),
solves all seven original equations by Lemma 1 and lies in (14).
Uniqueness identifies it with the canonical reference for its
own \(c\). Thus the two images are precisely those asserted.
If two inputs had the same \(b\), (3) and the unique formulas
(6) would give the same \(c\); the map is injective.
This argument concerns the filtered canonical branch, not the
global rational map in shape space. \(\square\)

There is no ramification on this image. Near any filtered point,
the identities (7) hold on a regular complex neighborhood.
The original logarithmic residuals are locally constant multiples
of \(2\pi i\), and Lemma 1 sets them to zero. Differentiating the
seven equations with respect to \(b\), even at a filter boundary,
shows that \(c'(b)=0\) would force every internal derivative to
vanish by the nonsingular seven-variable Hessian. This contradicts
the derivative of the coordinate \(b\) itself. Therefore
\[
                         c'(b)\ne0.
 \tag{16}
\]
In particular \(b(c)\) also has nonzero derivative. If necessary
one shrinks its neighborhood of the closed disk to preserve
injectivity; compactness, injectivity on the closed disk and
local invertibility justify this shrinking.

**Corollary 3.** Every actual positive open word of length \(m\ge4\)
whose final types are \((3+\gamma,4,4,3+\epsilon)\) has
its reference \(b=z_{m-2}\) in \(\Omega^K_{\gamma,\epsilon}\).
The other coordinates are reconstructed by (3), (6) and (8).

*Proof.* The original reference theorem and
[typed actual envelopes](research_mixed_typed_last_row_envelopes.md)
give \(c=z_{m-3}\in K_{3+\gamma}\). At \(m=4\), this is the
first endpoint's attached leg; for larger \(m\), it is ordinary.
The next two vertices are ordinary own-four vertices in either case.
Their equations and the final endpoint equations are precisely (15).
The original uniqueness theorem identifies the suffix with
Proposition 2's reference. No ordinary equation has been applied
to an endpoint vertex. \(\square\)

For terminal type four, \(b\in O_4\subset K_4\) also puts
the canonical \(a(b)\) in the original oriented, inverse-feasible
source domain by the
[canonical source-domain theorem](research_mixed_terminal_canonical_source_domain.md).
Thus this reconstruction preserves the terminal source eligibility
needed in the two-selected window. It does not declare all points
of an independent \(a\)-rectangle source-feasible.

## 4. Correlated transport without a new reference equation solve

All seven coordinates and the external input can now be treated as
functions of the same old parameter \(b\). For example put \(k=g''\),
and let primes denote derivatives with respect to that parameter.
Differentiating (5) on the original branch gives
\[
 \begin{split}
 r'={}&-\frac{k(r+b)+k(s+b)-3k(b)
                         +(k(s+b)+2\pi i)s'}{k(r+b)},\\
 c'={}&-\frac{\{k(r+c)+k(r+b)-3k(r)\}r'+k(r+b)}
                                      {k(r+c)+2\pi i}.
 \end{split}
 \tag{17}
\]
Neither denominator can vanish in the regular strip:
\(\cot(\pi z)\) never equals \(i\) or \(-i\) at a finite
regular point. Alternatively, (6) may be differentiated in
shape coordinates before principal decoding. These are exact
identities, not new interval derivative bounds.

The completed affine description
\(q_\epsilon(b)=q_0+u(b-b_0)+\zeta(b)\) consequently supplies
the old coordinates without a new root solve. Any future rigorous
evaluation of (6) must enclose its full rational images and separate
every denominator before decoding. Pointwise restrictions such as
(8) do not permit clipping an image before a whole-box derivative
bound. Nor does an affine predictor vector \(u\) equal the exact
derivative \(q_\epsilon'(b)\) merely because its value remainder
is small. The present result supplies the correct parameterization
and domains, not those further numerical estimates.

Finally the two shared-leg equations in (5) and (3) are exactly
the two stationary identities used in
[the joint two-selected window](research_mixed_terminal_two_selected_window.md),
equations (12)--(17). They cancel both linear height responses
when \(b,a\) move to the common selected height. All five real
forces and both vertical remainders in that criterion therefore
depend on this single correlated reference parameter. The shared
ordinary-index force still contains
\[
 \Re\{L_{\Delta_b}(s+b)+L_{\Delta_a}(s+a)\}
                                      -2\pi\Delta_b,
 \tag{18}
\]
with its original chirp. Reconstruction does not remove this term,
prove its sign, or allow the two complete selected weights to use
different contours.

A uniform joint budget on \(\Omega^K_{\gamma,\epsilon}\) would
cover every actual suffix in Corollary 3. The necessary remaining
quantitative premise is still the full joint main and nonmain
profile comparison with the five/four simultaneous costs of that
criterion. The old unselected-input terminal gap alone supplies
no such comparison. No selected-source gap, arbitrary finite-word
realization, whole-source asymptotic or knot-family theorem follows
from the reference reconstruction.
