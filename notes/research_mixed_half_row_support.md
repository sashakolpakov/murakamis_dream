# Ordinary-reference support at the real half row

Research certificate design, 5 November 2026. This acceptance scheme
tests the complete row at index \(1/2\) against the original
horizontal supporting plane. It retains both own types, both
conditional orientations, and every horizontal plateau target.
Only a complete twelve-face record with status “passed” proves
the uniform assertion below. The authorized bounded pilot has
no such scope.

## 1. Original references, allocations and the proposed comparison

Use the reduced disks
\[
 P_3=\{|z-(.35-.01i)|\le.083\},\qquad
 P_4=\{|z-(.30-.052i)|\le.060\}.
 \tag{1}
\]
For own flag \(\epsilon\in\{0,1\}\), external flags
\((\alpha,\beta)\in\{(0,0),(0,1),(1,1)\}\), and
\((A,C)\in P_{3+\alpha}\times P_{3+\beta}\), take the
original zero-lift two-leg root of
\[
 \begin{split}
 g'(s+t)+g'(s+A)-(2+\epsilon)g'(s)+2\pi iA&=0,\\
 g'(s+t)+g'(t+C)-(2+\epsilon)g'(t)+2\pi iC&=0.
 \end{split}
 \tag{2}
\]
Existence, uniqueness, holomorphy and the original parameter response
are supplied by the
[reduced-disk source theorem](research_mixed_reduced_disk_conditional_packets.md).
Its individual arguments lie in
\(Q=[.23,.45]+i[-.12,.12]\).

The two conditional orientations are
\[
 (s_*,a,b,\eta)=(s,A,t,\alpha)
                 \quad\hbox{and}\quad(t,C,s,\beta).
 \tag{3}
\]
In either orientation retain the complete allocated phase
\[
 \begin{split}
 F(v;a,b)={}&g(v+a)+g(v+b)-(2+\epsilon)g(v)
 -(1+\eta/2)g(a)-(1+\epsilon/2)g(b)+2\pi iav,\\
 \phi(a,b)&=F(s_*;a,b),\qquad Z=(a,b)=U+iH,\\
 I&=[11/50,9/20],\qquad \ell=1/2,\qquad \kappa=1/2500000,\\
 B_Z(X)&=\Re\phi(Z)+\Re\phi'(Z)\cdot(X-U)
                                -\kappa\|X-U\|^2,\\
 D(Z,X)&=\Re F(\ell;X+iH)-B_Z(X),\qquad X\in I^2.
 \end{split}
 \tag{4}
\]
The primitive, absolute constant and logarithmic lifts are those of
the original source. At this row the shifted real arguments lie
in \([.72,.95]\), so no numerator wall is crossed. Thus the first
term of \(D\) is exactly the complete allocated real-row rate,
including the asymmetric chirp and both outer halfweights.

**Certificate assertion.** A complete acceptance of all cases in
Sections 3--5 proves
\[
                             D(Z,X)<-1/2000
 \tag{5}
\]
on all six own/external reduced products, in both orientations and
for every \(X\in I^2\). No vertical sign condition at an optimizing
target is assumed. In particular the acceptance test also includes
the region not paid by the analytic half-row sign and energy criteria.

The allocations in (4) are formal phase functions on the full auxiliary
products. Their physical interpretation as unselected Fourier upper
rates is restricted to the actual negative type-four reference
heights. This distinction is unchanged by any complete acceptance
of (5).

## 2. Why the old matched gap applies at exactly one half

At matched targets \(X=U\), the allocated outer terms in the
critical phase and real row cancel. Section 2, equations (8)--(9)
of the reduced-disk source theorem bound the entire original right
real tail \([.49,1]\) on every distinguished input boundary:
the real cut and the complete revived endpoint each have gap
greater than \(1/1000\), and the original polynomial shape test
puts every intervening row below one of them. The row \(1/2\)
belongs to this interval.

Section 4 of that theorem then transfers each fixed-row entropy
gap to the whole reduced bidisk by two subharmonic maximum
principles. Consequently
\[
                         D(Z,U)<-1/1000
 \tag{6}
\]
on the full auxiliary product, including its full height range
\([-.12,.12]\). This uses the old complete real-tail theorem
at one fixed row. It does not extend the newer actual-height
right-tail endpoint theorem beyond its \(.108\) hypothesis,
and it does not infer an entropy gap from finite-sum cancellation.

The original critical phase also satisfies
\(-D_U^2\Re\phi\succ(\pi/8)I_2\), and the retained-variable
map \((A,C)\mapsto(A,t(A,C))\) is locally invertible because
\(t_C\ne0\). The same facts hold in the opposite orientation.
The [reference-boundary principle](research_mixed_horizontal_tail_reference_boundary.md)
therefore reduces (5) to the ordinary boundary
\[
 (\partial P_{3+\alpha}\times P_{3+\beta})
       \cup(P_{3+\alpha}\times\partial P_{3+\beta}).
 \tag{7}
\]
An interior maximizing reference would force \(X=U\), where
(6) has a larger reserve than the requested \(1/2000\).
There are twelve three-real-dimensional faces: two own types,
three unordered external type pairs, and two ordinary faces.
Both orientations are checked on every face. Swapping the two
inputs and the two original roots covers the exchanged ordered
type case; no equal-type face is omitted.

## 3. Strict concavity controls all real targets

For \(x\in I\), \(|h|\le3/25\), \(\lambda\ge1\), put
\(f(x)=\Re\{g(x+1/2+ih)-\lambda g(x+ih)\}\).
The chirp at this fixed index is constant in the target real part.
Writing \(\theta=2\pi x\) and \(K=\cosh(2\pi h)\),
the exact half-period cotangent identity gives
\[
 \begin{split}
 -f''(x)
 &=2\pi\Re\csc(2\pi(x+ih))
            +(\lambda-1)\pi\Re\cot\pi(x+ih)\\
 &\ge\frac{2\pi\sin\theta\,K}
              {\sin^2\theta+\sinh^2(2\pi h)}
 >\frac{27\pi}{80}>1.
 \end{split}
 \tag{8}
\]
Indeed \(\sin\theta>3/10\), \(1\le K<4/3\), and
\(\sinh^2(2\pi h)<7/9\), while the extra real cotangent is
nonnegative. These are the elementary outer-strip bounds already
used in the fixed-contour theorem. The last rational comparison
follows from \(\pi>3\).

The two target variables in (4) separate. The target Hessian of
\(D\) is therefore diagonal and bounded above by
\(-c_*I_2\), where \(c_*=1-2\kappa>0\).
For any rational trial \(\widehat X\in I^2\), an interval
\(\beta_i\) enclosing its target slope gives the complete gain
\[
 G_i=\max_{d\in[11/50-\widehat X_i,\,9/20-\widehat X_i]}
             \{\beta_i d-\tfrac12c_*d^2\}.
 \tag{9}
\]
The coefficient is maximized according to the sign of \(d\).
On each one-sided interval only zero, its clipped stationary point
and the endpoint are needed. A floating scalar optimizer proposes
the rational trial; (8)--(9), evaluated outward, decide acceptance
on the entire target square. There is no target grid.

## 4. Correlated reference derivatives and whole-cell acceptance

Parametrize each face by the full cube
\((\theta,\rho,\psi)\in[0,1]^3\). The circle input is
\(c+r e^{2\pi i\theta}\); the other input is
\(c+\rho r e^{2\pi i\psi}\). This covers its entire disk,
including its center, and includes all boundary points. Repeated
polar images are harmless.

The unchanged original affine-root certifier is called with the
current own flag \(\epsilon\) in every root equation, Jacobian,
nonlinear remainder, midpoint-lift and response calculation. Its
weighted Neumann enclosure supplies the response of both roots to
both external inputs. The exact polar derivatives supply the
response of the retained variables \(Z\) to the three real
parameters.

At fixed rational trial write \(P=\phi'(Z)\),
\(H_\phi=\phi''(Z)\), \(\delta=\widehat X-U\) and
\(P_c=F_X(1/2;\widehat X+iH)\). The cancellation-preserving
reference derivatives are exactly
\[
 D_U=(-\Re H_\phi-2\kappa I)\delta,\qquad
 D_H=\Im\{P-P_c+H_\phi\delta\}.
 \tag{10}
\]
The checker uses the original complex Schur complement
\[
 \begin{split}
 H_\phi&=F_{XX}-F_{Xs}F_{ss}^{-1}F_{sX},\\
 F_{ss}&=g''(s_*+a)+g''(s_*+b)-(2+\epsilon)g''(s_*),\\
 F_{sX}&=(g''(s_*+a)+2\pi i,\ g''(s_*+b)),\\
 F_{XX}&=\operatorname{diag}\bigl(
 g''(s_*+a)-(1+\eta/2)g''(a),
 g''(s_*+b)-(1+\epsilon/2)g''(b)\bigr).
 \end{split}
 \tag{11}
\]
Thus the asymmetric chirp, own denominator power and both outer
allocations vary correctly with the type case.

Let \(D_0\) be the direct interval phase deficit on the tiny
original-log midpoint root disk. For parameter halfwidths \(h_j\),
the whole-cell upper test is
\[
               D_0+\sum_{j=1}^3h_j\sup|D_{\xi_j}|+G_1+G_2
                                     <-1/2000.
 \tag{12}
\]
The reference derivatives follow from (10) by the real chain rule
with the full correlated root response. Both orientations must
pass (12) on every accepted leaf. No display-rounded value or
floating root or target proposal can accept a cell.

## 5. Bounded pilot, complete coverage and saved replay

The checker is
[certify_mixed_half_row_support.py](../experiments/certify_mixed_half_row_support.py).
It binds this proof, its own script, the current complete reduced-disk
author and saved replay, all their inherited dependencies, and the
analytic reference-boundary and target-optimization inputs.

The sole authorized pilot uses case
\((\epsilon,\alpha,\beta,\mathrm{face})=(0,1,1,0)\): own type
three, two external type-four inputs, first input on its circle,
second input in its disk. Both conditional orientations are tested.
Its caps are 511 visited nodes and 60 seconds. A completed pilot
would have status “pilot_complete”, never “passed”; an interrupted
pilot records its accepted leaves and every pending cell with
status “incomplete”. Neither establishes a universal sign.

A full run requires all twelve cases, but is not authorized merely
by completion of the pilot. Each exact root cube is bisected at
rational midpoints, cycling the three axes. The traversal appends
left then right and pops right first. Every accepted leaf stores
its rational original affine-root witness and both rational target
pairs. A complete case with \(L\) leaves has \(2L-1\) nodes;
the twelve-case total is \(2L_{\mathrm{total}}-12\).
Reconstructing the complete trees, rather than only these counts,
is required by the checker.

Saved replay uses the identical case list and tree traversal. It
revalidates every original root enclosure, midpoint lift, response,
target gain and strict bound (12). It may neither propose a root
or target nor refine a saved leaf. Proof, code, input and inherited
dependency hashes are checked again at completion.

Only a complete acceptance would prove (5) by (6)--(7). Its eventual
physical use would remove the half row from the corresponding
ordinary fixed-height complete-source maximum, keeping every
original contour current. It would not by itself settle the last
row, distinct terminal endpoint graphs, arbitrary neighboring-height
changes, or the full ordinary knot contraction. No full author run
or uniform theorem is claimed by this design or its bounded pilot.
