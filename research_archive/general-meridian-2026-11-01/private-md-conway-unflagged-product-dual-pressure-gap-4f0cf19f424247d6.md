# A universal dual-pressure gap for an unturned Conway product hub

1 November 2026. NEW PRIVATE analytical proof. No frozen note, manuscript,
checkpoint or public file is changed. This concerns the original positive
optimized profiles and exact unsquared port equations. It does not itself
bound a signed quantum turn.

## 1. The exact product hypothesis

Let \(A=FG\) be an actual unturned product, with both children of strict
type \(L\) or \(A\). Either child may have its own internal turns. The
product has strict output interval \((0,1)\). Let \(f_A(z)\) be its
original positive optimized action, extended continuously to the closed
output interval. The established strict-state/barrier theorem gives a
unique strict optimizer and an analytic strictly concave profile on
\((0,1)\).

At that optimizer put
\[
 B=\cot(\pi z),\qquad
 B_i=\cot(\pi x_i),\qquad
 \kappa_A=e^{-f_A'(z)},\qquad
 X^2=\frac{1+B^2}{1+\kappa_A},\qquad Y^2=\kappa_A X^2.
 \tag{1}
\]
The source equations give a common positive \(X\) for both inputs and
the output:
\[
 X^2+Y^2-B^2=1,\qquad
 B(B_1+B_2)=B_1B_2+X^2-1,\qquad B_1+B_2>0.
 \tag{2}
\]
Strict gate support \(z>x_i\) and the exact child type inequalities give
\[
                       B<B_i\le X.
 \tag{3}
\]
Equality \(B_i=X\) holds for a child of type \(L\); it is strict for a
child of type \(A\). This hypothesis is automatically the local one at
an unflagged reduced product hub: its incoming branches have type \(L\)
or \(A\). A larger product can be associated at its last binary gate.
All constants internal to rigid children remain in the profiles.

Define the two intrinsic probe pressures
\[
 \Omega_A=\max_{0\le a\le1/2}\bigl[f_A(a)+g(a)\bigr],
 \qquad
 \Omega_{TA}=\max_{0\le a\le1/2}\bigl[f_A(1-a)+g(a)\bigr],
 \tag{4}
\]
where
\[
 g(a)=J(2a)-4J(a),\quad
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\quad
 G_0=g(1/4)=\frac{2G}{\pi}
 \tag{5}
\]
and \(G\) is Catalan's constant. The associated strict closed roots
supply interior maximizers. The first probe has \(X_A=1\); the second
has \(Y_A=1\), since the turn exchanges \(X,Y\). Closed endpoints are
included in (4) only to make compactness explicit.

## 2. Derivative domination by the two-leaf product

Rearranging (2) gives the exact identity
\[
 Y^2=(B_1-B)(B_2-B)\le(X-B)^2.
 \tag{6}
\]
All factors are positive by (3), so there is no sign or squared-branch
ambiguity. Using \(Y^2=1+B^2-X^2\), (6) becomes
\[
 1\le2X(X-B),\qquad
 X\ge X_2(B):=\frac{B+\sqrt{B^2+2}}2.
 \tag{7}
\]
If either child has type \(A\), the inequalities are strict.

For the actual two-leaf product \(hh\), both inputs have
\((B_i,X,Y_i)=(X,X,1)\), so
\[
 B=X_2-\frac1{2X_2},\qquad
 Y_2=\frac1{2X_2},\qquad
 f_{hh}'(z)=\log(4X_2^4)=2\log(2X_2^2).
 \tag{8}
\]
For any fixed \(B\), the function
\[
 x\longmapsto\log\frac{x^2}{1+B^2-x^2}
\]
is strictly increasing on \(0<x<\sqrt{1+B^2}\). Equations (1) and (7)
therefore give the whole-output inequality
\[
                    f_A'(z)\ge f_{hh}'(z),
                    \qquad 0<z<1.
 \tag{9}
\]
It is strict everywhere if either child has type \(A\). If both children
are \(L\), their profiles are \(g\) plus constants, and equality in (9)
is exact, with those constants added to \(f_{hh}\).

At \(z=1/2\), \(B=0\) and \(X_2=1/\sqrt2\), so \(f_A'(1/2)\ge0\).
Strict concavity of \(f_A\) implies
\[
             \max_{0\le z\le1/2}f_A(z)=f_A(1/2).
 \tag{10}
\]
The continuous endpoint values do not add a new maximizer above this
value.

## 3. An explicit uniform gap greater than \(1/10\)

Use the fixed upper-half probe \(z=7/12\), so its root leaf has
\(a=1-z=5/12\). On \(1/2\le z\le7/12\),
\[
 B\ge\cot(7\pi/12)=\sqrt3-2>-\frac1{2\sqrt3}.
\]
The final inequality is exactly \(7>4\sqrt3\), proved by \(49>48\).
Since \(X_2(B)\) is increasing and
\[
 \frac1{\sqrt3}-\frac{\sqrt3}{2}=-\frac1{2\sqrt3},
\]
one has \(X_2(B)>1/\sqrt3\). Thus (8)–(9) imply
\[
 f_A(7/12)-f_A(1/2)
 \ge -\frac16\log(3/2).
 \tag{11}
\]
The original leaf \(g\) is concave on \([0,1/2]\), with
\(g(1/2)=0\). Its chord from \(1/4\) to \(1/2\) yields
\[
                          g(5/12)\ge G_0/3.
 \tag{12}
\]
Evaluating (4) at \(a=5/12\) and using (10)–(12) proves
\[
 \boxed{\quad
 \Omega_{TA}-\max_{0\le z\le1/2}f_A(z)
 \ge \frac{G_0}{3}-\frac16\log(3/2)
 >\frac1{10}.
 \quad}
 \tag{13}
\]
The last inequality is elementary and requires no numerical evaluation.
The alternating Catalan series gives \(G>1-1/9=8/9\);
the classical bound \(\pi<22/7\) therefore gives \(G_0>56/99\).
Also \(\log(3/2)<1/2\). Hence the middle expression in (13) is
strictly larger than
\[
 \frac{56}{297}-\frac1{12}=\frac{125}{1188}>\frac1{10}.
\]
This constant is independent of the product syntax, its size and all
additive rigid-profile constants. No compact family or lower bound on
its intrinsic satellite curvature is required.

## 4. Reflection and pressure comparison

The exact two-leaf root satisfies
\[
 X_2(B)X_2(-B)=\frac12.
\]
Equation (8) consequently gives
\(f_{hh}'(1-z)=-f_{hh}'(z)\). The difference
\(f_{hh}(z)-f_{hh}(1-z)\) has zero derivative and vanishes at \(1/2\);
therefore \(f_{hh}\) is symmetric under \(z\mapsto1-z\).

Integrating (9) from \(1-z\) to \(z\) proves
\[
 f_A(z)\ge f_A(1-z)\quad (1/2\le z\le1),\qquad
                         \Omega_{TA}\ge\Omega_A.
 \tag{14}
\]
For \(1/2<z<1\), the first inequality is strict if either child is type
\(A\). The maximizing probe for \(\Omega_A\) is strictly in \((0,1/2)\),
so the pressure inequality is then strict too. With two \(L\) children,
both profiles differ from the symmetric \(hh\) profile only by a
constant, so \(\Omega_{TA}=\Omega_A\).

The unturned product condition is essential to the proof. Applying an
outer turn reverses the output derivative, and does not preserve (9)
or the claimed orientation of (14). This note makes no corresponding
claim for an arbitrary type-\(A\) expression with a top turn.

## 5. Exact scope for the pending signed estimate

The result proves the requested classical inequality for the high
Newton-index part of a candidate unflagged-turn estimate, if that part
has already been bounded by the original lower-half profile. It does
not establish that quantum coefficient bound or replace the original
signed coefficient by its positive profile.

The low Newton part still requires its source-exact alias or spectral
estimate. Likewise (14) does not allow the exponential norm of an
arbitrary turn to be charged to a new physical leaf. There is no new
source-circle insertion, isotopy, geometric volume replacement, or
full mixed-hub theorem here.

Inputs: notes/actual_conway_general_strict_mask_geometry.md §§1–2;
notes/actual_conway_general_mask_marked_filling.md §2;
notes/actual_conway_rigid_spine_and_flagged_tree_geometry.md §§2–4;
notes/actual_conway_reduced_hub_source_normal_form.md §§2–4.

Author proof complete. Independent review requested; no durable promotion.
