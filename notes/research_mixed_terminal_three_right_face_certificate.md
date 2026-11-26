# A certificate for the raw half-transform face

Research design, 5 November 2026. The original right-triangle reduction
leaves one phase family to check: the transform index is exactly \(1/2\),
the Newton index is real, and the external real target ranges over the
plateau. This note specifies its full-reference, full-target certificate.
No numerical author or saved replay has yet been run for this new family.
All completed mixed-face and alias files remain unchanged.

## 1. The exact face and its source role

Use the phase \(\mathcal T\), original logarithmic branches and full
finite normalization of
[the joint terminal source](research_mixed_terminal_three_joint_zero_mode.md).
Put
\[
 I_a=[11/50,9/20],\qquad I_u=[1/10,2/5],\qquad
 \kappa=1/2500000,\qquad \mu=3/100 .
 \tag{1}
\]
For an original own-three endpoint reference \(a_*=A+iH\), let
\((e_*,t_*,u_*)\) be its saved original-log root. The reference
action and derivative are
\[
 P(a_*)=\mathcal T(a_*;t_*,u_*),\qquad p(a_*)=P'(a_*).
 \tag{2}
\]
Their calibration is the
[critical-curve identity](research_mixed_terminal_three_critical_curve.md).
The full endpoint image rectangles, including their implicit
responses, remain those of the original map.

There is exactly one new family:
\[
 a=y+iH,\qquad t=1/2,\qquad u=z,\qquad
                  (y,z)\in I_a\times I_u .
 \tag{3}
\]
Both index heights are zero. There is no residue-alias penalty.
Its bare supporting-plane deficit is
\[
 G(a_*;y,z)=
 \Re\mathcal T(y+iH;1/2,z)-\Re P(a_*)
            -\Re p(a_*)(y-A)+\kappa(y-A)^2 .
 \tag{4}
\]
The target is the strict bound \(G<-1/2000\), over both full
original input disks \(D_3,D_4\), rather than just their boundaries
or actual word samples.

For the actual external type-four halfweight, the allocated deficit
is (4) plus
\[
 -\tfrac12\{\Re g(y+iH)-\Re g(A+iH)
                       -\Re g'(A+iH)(y-A)\}\le0.
 \tag{5}
\]
Thus the bare comparison suffices. Its finite-source interpretation
uses the actual negative type-four reference height, as in the
[completed zero-mode theorem](research_mixed_terminal_three_zero_mode_completion.md).
The auxiliary positive-height part of \(D_4\) introduces no new
physical Fourier branch.

The [right-triangle theorem](research_mixed_terminal_three_right_triangle.md)
reduces its entire original positive row-rate maximum to (3),
using the Newton maximum at \(t=1/2\) and monotonicity thereafter.
Consequently a complete certificate for (4) would discharge that
remaining raw-face comparison. No root at the target (3), and no
unproved moving-root containment, is needed.

## 2. The complete target square

The enlarged joint Hessian theorem gives
\[
 -\Re\mathcal T''\succ(\pi/100)I_3
 \quad\Longrightarrow\quad
                    G_{(y,z)}''\preceq-\mu I_2 ,
 \tag{6}
\]
since \(\pi/100-2\kappa>3/100\).
It applies at \(t=1/2\): the positive-block proof of the
Hessian floor explicitly allows \(\Re\cot(\pi t)=0\).
All shifted arguments in (3) are still in the original regular
primitive strips.

For any fixed rational trial \(X^0=(y^0,z^0)\) in the target box,
suppose a whole reference rectangle satisfies
\(G(a_*;X^0)\le v\) and
\(\partial_jG(a_*;X^0)\in[g_j^-,g_j^+]\).
For its coordinate interval \([\ell_j,r_j]\), set
\[
\begin{split}
 h_j^-&=\operatorname{clip}(g_j^-/\mu,\ell_j-X_j^0,0),\\
 h_j^+&=\operatorname{clip}(g_j^+/\mu,0,r_j-X_j^0),\\
 C_j&=\max\{g_j^-h_j^--\mu(h_j^-)^2/2,\
                 g_j^+h_j^+-\mu(h_j^+)^2/2\}.
\end{split}
\tag{7}
\]
Here \(\operatorname{clip}(s,l,r)=\min(r,\max(l,s))\).
Strong concavity yields the full-box upper bound
\[
                  G(a_*;y,z)\le v+C_1+C_2 .
 \tag{8}
\]
This is the already proved clipped rule in
[the mixed-face certificate](research_mixed_terminal_three_mixed_face_certificate.md).
No target grid or assumption about an interior optimizer is made.
A floating coordinate ascent may only propose the rational trial;
its values do not determine acceptance.

## 3. Reference derivatives and original root enclosures

Keep the trial fixed and write \(d=y^0-A\).
Both target index heights stay zero as the reference varies.
The reference action and its linear tangent cancel exactly:
\[
 G_A=-d\,\Re P''-2\kappa d,\qquad
 G_H=\Im(P'-\mathcal T_a)+d\,\Im P'' .
 \tag{9}
\]
There are no target-height response terms. The target derivatives are
\[
 G_y=\Re\mathcal T_a-\Re P'+2\kappa d,\qquad
 G_z=\Re\mathcal T_u .
 \tag{10}
\]
The reference derivatives still use the original coupled root:
\[
\begin{split}
 P'&=g'(a_*+t_*)-g'(a_*)+2\pi i t_*,\\
 P''&=g''(a_*+t_*)(1+t_*')-g''(a_*)+2\pi i t_*',\\
 (e_*',t_*',u_*')^T&=-f_z^{-1}f_a .
\end{split}
\tag{11}
\]
Every phase partial in (9)--(10) is evaluated at the face target,
and every reference derivative in (11) at its actual original branch.

The point value at a parameter-cell center, plus physical real and
imaginary halfwidths times whole-cell bounds for \(|G_A|,|G_H|\),
gives \(v\) in (8). Whole-cell target gradients give (7).
This uses fixed-trial differentiation, not a derivative of an
optimizing target.

## 4. Exact coverage and immutable validation

The new driver is
[certify_mixed_terminal_three_right_face.py](../experiments/certify_mixed_terminal_three_right_face.py).
It is a separate adaptation of the completed mixed-face driver.
All original root tests, Taylor-image tightening, Neumann response
enclosures, reference partition rules and protected checkpoint
logic are retained.

The original four input trees are reconstructed in their exact
right-first order, including all 233 original excluded boxes.
The two own-three families contribute 1,645 and 1,702 accepted
root leaves. One face per leaf gives exactly 3,347 new jobs.
Each original witness first proves its full-leaf unexponentiated
root and the endpoint-image inclusions. Tightening uses only that
same saved center and inverse \(Y\): the inherited \(b/(1-q)\)
bound followed by five interval Taylor-image intersections on
the cell and twelve at its midpoint. Eight Neumann terms and the
outward remaining geometric-series tail enclose (11).
There is no new complex-root proposal.

Strict acceptance is
\[
                        v+C_1+C_2<-1/2000.
 \tag{12}
\]
An unsuccessful author cell may split at an exact rational midpoint.
Only a strict exact outside-disk test may exclude a child. The
pending box remains on the frontier during all fallible arithmetic;
a signal-masked commit records its accepted trial or its two
children. An arithmetic or inherited-root failure leaves it unresolved.

Each author attempt is limited to 600,000 additional nodes and
600 seconds of its numerical loop, with added depth at most 45
(default 20). A resume reads an immutable incomplete record and
writes a different path. It verifies all current bindings, the
single-family metadata, every accepted prefix and rational trial,
and the exact reconstructed pending frontier before continuing.
It never repeats accepted-prefix arithmetic in author mode.
The final saved replay revalidates every root and accepted face
using the stored tree and rational trial, with both root and target
proposals disabled and no subdivision.

The completed mixed-face and alias author/replay pairs are bound,
including their input hashes and exact saved-tree/trial equality.
The original root author/replay, endpoint-image extraction, both
Hessian scalar records, critical-curve identification, zero-mode
completion, alias reduction and right-triangle proof are also bound.
All bound files are rechecked before final publication.

No numerical execution has yet occurred for this new family.
Only an exhaustive author record and independent saved replay
establish the uniform sign in (12). The resulting finite right-sector
bound then follows from the cited original-source reduction with
its stated common tolerance and ordinary-color scope; it is not
an independent assertion about arbitrary fillings.
