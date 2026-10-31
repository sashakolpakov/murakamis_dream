# Intrinsic probe geometry for unflagged Conway components

31 October 2026. geometric and classical-action theorem.
It supplies the exact parameter range and absolute pressure used by the
separate [full-normal coefficient-cone bound](actual_conway_unflagged_core_probe_bound.md).
The classical probe does not insert a physical circle into the invariant.
No signed coefficient estimate follows from the geometry alone.

The inputs are the original [strict-mask complete geometry](actual_conway_general_strict_mask_geometry.md),
the [marked quarter-bound theorem](actual_conway_general_mask_marked_filling.md),
the [rigid-spine action identity](actual_conway_rigid_spine_and_flagged_tree_geometry.md),
and the [exact reduced-hub source](actual_conway_reduced_hub_source_normal_form.md).
The appendix proves a separate universal pressure gap for an unturned
product hub, with an explicit constant greater than \(1/10\).

## 1. The component and its effective leaves

Root a strict reduced Frobenius hub tree at a flagged original leaf.
A maximal connected component of unflagged hubs has a unique parent edge.
Orient that edge toward its parent. Its outgoing source is
\[
                         Q=T(A),
\]
where \(A=FG\) is an unturned product with at least two branches. Inside
the component there are only products and turns of \(A\)-type subtrees.
Each boundary satellite from a flagged descendant is an \(L\)-type
module; each ordinary original leaf is also \(L\).

The exact positive profile of such a boundary module is
\(f_{L_i}=g+c_i\), with its absolute constant fixed by the [rigid-spine theorem](actual_conway_rigid_spine_and_flagged_tree_geometry.md). Replacing that profile by an effective bare \(g\)-leaf changes
the whole component action only by the sum of those constants:
\[
 f_A(z)=f_{A^{\mathrm{skel}}}(z)+\sum_i c_i.
 \tag{1}
\]
The skeleton is a completed expression in effective \(L\) leaves:
\(LL,T(A),AA,LA,AL\). No quantum coupon is replaced by \(h\).

Define the intrinsic probe
\[
 \Omega_Q=\max_{0\le a\le1/2}
           \bigl[g(a)+f_Q(a)\bigr]
          =\max_{0\le a\le1/2}
           \bigl[g(a)+f_A(1-a)\bigr].
 \tag{2}
\]
This is the positive action of the strict literal closure
\(C(hA)\), with a bare probe leaf. The root is \(L/A\), so the established
[strict-state/barrier theorem](actual_conway_general_strict_mask_geometry.md) gives a unique strict optimizer. The probe
equation says \(X_Q=1\); since \(Q=T(A)\), equivalently \(Y_A=1\).
In the port of the unturned \(A\), root complementarity gives
\[
                (B_A,X_A,Y_A)=(-x,x,1),\qquad 0<x<1.
 \tag{3}
\]
The strict upper bound follows from the \(A\) inequality \(B_A>-Y_A\).
The probe leaf has cotangent \(x\).

The parent flagged spine evaluates precisely this same intrinsic state:
its \(H\)-product has common \(X_Q=1\). Thus (2) is the actual component
state selected by the original complete source, not a freely imposed
boundary value.

## 2. Every effective leaf is in the closed proper range

At the last product \(A=FG\), the strict source equations and the input
type inequalities imply
\[
 Y_A^2=(B_F-B_A)(B_G-B_A)\le(X_A-B_A)^2.
\]
At (3), this is \(1\le4x^2\), hence
\[
                              \frac12\le x<1.
 \tag{4}
\]
Thus even the artificial closing probe leaf has the required range.

All descendant \(A\) ports are strictly proper. At the root product,
common \(X=x<1\); if a child has type \(A\), its cotangent obeys
\(B_i<X\), while positivity of \(B_i+B_j\) and \(B_j\le X\) gives
\(B_i>-X\). Consequently
\[
       Y_i^2=1+B_i^2-X^2<1,\qquad X_i=X<1.
\]
A turn swaps these two strict bounds. The same argument propagates
through every product. The root \(A\) alone may have \(Y_A=1\).

For any effective \(L\) input of a retained product, its port is
\((X,X,1)\). If the other input is \((B,X,Y)\), the output bound
\(Y_o\le1\) gives
\[
 1+B^2-X^2\le(B+X)^2,\qquad
 1\le2X(B+X)\le4X^2.
 \tag{5}
\]
Hence every effective leaf has \(X\ge1/2\). With an \(A\) neighbor the
last inequality is strict. If the two children are \(L,L\) and the
parent is a proper descendant, \(Y_o<1\) makes the first inequality
strict. The inherited \(X<1\) gives the upper bound.

Equality \(X=1/2\) can therefore occur only when the root \(A\) itself
has two effective \(L\) children. This is exactly the isolated effective
three-leaf closure \(C(hhh)\); all three effective leaves then have
\(X=1/2\). Otherwise every effective leaf, including the probe, has
\[
                              \frac12<X<1.
 \tag{6}
\]
These claims concern effective component leaves. Physical leaves inside
their decorated satellites may be at quarter index or have smaller
cotangents, as the rigid-spine law already describes.

## 3. Relation to the already certified local parameter domains

The [two-leaf block certificate](actual_conway_uniform_two_leaf_block_alias_gap.md) covers \(1/2\le X\le1\), including its
exact lower endpoint. The [single-leaf attachment comparison](actual_conway_single_leaf_alias_composition.md) covers
proper child ports and the closed slope square used for the bad range
\(1/2\le X\le2/3\); the older single-leaf bound covers \(X\ge2/3\).

The only new possible parent boundary is the root \(A\) with \(Y_A=1\).
For a root single attachment \(A=LF\), write \(X=x\). Equations (3),(5)
give the other child's cotangent and height exactly:
\[
 B_F=\frac1{2x}-x,\qquad Y_F=\frac1{2x}.
\]
In the bad range \(1/2\le x\le2/3\), the child and parent slopes are
\[
 \mu=f_F'=2\log(2x^2),\qquad
 \lambda=f_A'=2\log x.
 \tag{7}
\]
Both belong to the original closed square
\([-2\log2,0]^2\). The child is proper; equality \(x=1/2\) cannot occur
for an \(A\) child, but its limiting value is already in the certificate.
For a root \(LL\) block the endpoint \(x=1/2\) is in the original
two-leaf block interval.

There is also an exact source regrouping of the positive probe.
Because \(A=FG\) is unturned, \(C(h(FG))\) can be regrouped in the full
Frobenius scalar. If either \(F\) or \(G\) is type \(A\), group \(h\)
with the other branch, leaving two completed root children. If both are
effective \(L\) leaves, it is the [isolated effective three-leaf closure](actual_conway_isolated_three_leaf_long_twist_volume.md).
This is an algebraic source regrouping and a parameter check, not a
topology or arbitrary colored-module replacement theorem.

Thus there is no missing geometric parameter range at this probe.
Whether a proposed signed coefficient adapter actually has these
effective \(g+c_i\) source envelopes remains a separate obligation.

## 4. Absolute constants and the original root action

Equation (1) gives the exact identity
\[
 \Omega_Q
   =F_{\mathrm{probe}}(A^{\mathrm{skel}})+\sum_i c_i.
 \tag{8}
\]
No scalar constant is normalized away. Each \(c_i\) is itself the sum
of its satellite pressures from the rigid-spine theorem.

For completeness, close the whole original reduced tree at a flagged
leaf \(h_0\), with satellites \(Q_j\) of type \(L\) or \(A\). Its original
Frobenius scalar is
\(\phi((Th_0)\prod_jQ_j)\), equivalently \(C(h_0T(\prod_jQ_j))\).
The associated \(H\)-profile has
\[
        f_H(z)=g(1-z)+\sum_j\Omega_{Q_j}.
\]
At the original coefficient-one closing endpoint \(z=1\), \(g(0)=0\).
Continuity of the original optimized action therefore yields
\[
                          F_0=\sum_j\Omega_{Q_j}.
 \tag{9}
\]
Alternatively the same equality follows directly by using the original
complementary root relation in the positive profile convolution.

Substituting (8) and the exact rigid constants recursively into (9)
is a finite accounting identity on the original tree. It retains
exactly the original complete action. The bare probe appearing in
\(F_{\mathrm{probe}}\) is an intrinsic classical dual used to determine
a constant; it is not an extra physical auxiliary color, and it does
not add an uncharged \(2G_0\) to the quantum source.

## 5. Scope of the probe

Equations (1)–(9) concern the original positive profiles and their
complete selected states. The effective leaves carry their exact
additive constants. Their signed coupons and independent physical colors
are retained by the separate coefficient-cone theorem.

The old block and attachment certificates therefore have no missing
geometric parameter range at this probe. Whether a proposed coefficient
comparison belongs to the required cone is a source obligation; the
profile identity does not prove it. The complete action accounting
does not add an artificial \(2G_0\), a crossing circle or a filling slope.

## Appendix. A universal dual-pressure gap for an unturned product

### A.1. The exact product hypothesis

Let \(A=FG\) be an actual unturned product, with both children of strict
type \(L\) or \(A\). Either child may have its own internal turns. The
product has strict output interval \((0,1)\). Let \(f_A(z)\) be its
original positive optimized action, extended continuously to the closed
output interval. The established [strict-state/barrier theorem](actual_conway_general_strict_mask_geometry.md) gives a
unique strict optimizer and an analytic strictly concave profile on
\((0,1)\).

At that optimizer put
\[
 B=\cot(\pi z),\qquad
 B_i=\cot(\pi x_i),\qquad
 \kappa_A=e^{-f_A'(z)},\qquad
 X^2=\frac{1+B^2}{1+\kappa_A},\qquad Y^2=\kappa_A X^2.
 \tag{A1}
\]
The source equations give a common positive \(X\) for both inputs and
the output:
\[
 X^2+Y^2-B^2=1,\qquad
 B(B_1+B_2)=B_1B_2+X^2-1,\qquad B_1+B_2>0.
 \tag{A2}
\]
Strict gate support \(z>x_i\) and the exact child type inequalities give
\[
                       B<B_i\le X.
 \tag{A3}
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
 \tag{A4}
\]
where
\[
 g(a)=J(2a)-4J(a),\quad
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\quad
 G_0=g(1/4)=\frac{2G}{\pi}
 \tag{A5}
\]
and \(G\) is Catalan's constant. The associated strict closed roots
supply interior maximizers. The first probe has \(X_A=1\); the second
has \(Y_A=1\), since the turn exchanges \(X,Y\). Closed endpoints are
included in (A4) only to make compactness explicit.

### A.2. Derivative domination by the two-leaf product

Rearranging (A2) gives the exact identity
\[
 Y^2=(B_1-B)(B_2-B)\le(X-B)^2.
 \tag{A6}
\]
All factors are positive by (A3), so there is no sign or squared-branch
ambiguity. Using \(Y^2=1+B^2-X^2\), (A6) becomes
\[
 1\le2X(X-B),\qquad
 X\ge X_2(B):=\frac{B+\sqrt{B^2+2}}2.
 \tag{A7}
\]
If either child has type \(A\), the inequalities are strict.

For the actual two-leaf product \(hh\), both inputs have
\((B_i,X,Y_i)=(X,X,1)\), so
\[
 B=X_2-\frac1{2X_2},\qquad
 Y_2=\frac1{2X_2},\qquad
 f_{hh}'(z)=\log(4X_2^4)=2\log(2X_2^2).
 \tag{A8}
\]
For any fixed \(B\), the function
\[
 x\longmapsto\log\frac{x^2}{1+B^2-x^2}
\]
is strictly increasing on \(0<x<\sqrt{1+B^2}\). Equations (A1) and (A7)
therefore give the whole-output inequality
\[
                    f_A'(z)\ge f_{hh}'(z),
                    \qquad 0<z<1.
 \tag{A9}
\]
It is strict everywhere if either child has type \(A\). If both children
are \(L\), their profiles are \(g\) plus constants, and equality in (A9)
is exact, with those constants added to \(f_{hh}\).

At \(z=1/2\), \(B=0\) and \(X_2=1/\sqrt2\), so \(f_A'(1/2)\ge0\).
Strict concavity of \(f_A\) implies
\[
             \max_{0\le z\le1/2}f_A(z)=f_A(1/2).
 \tag{A10}
\]
The continuous endpoint values do not add a new maximizer above this
value.

### A.3. An explicit uniform gap greater than \(1/10\)

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
one has \(X_2(B)>1/\sqrt3\). Thus (A8)–(A9) imply
\[
 f_A(7/12)-f_A(1/2)
 \ge -\frac16\log(3/2).
 \tag{A11}
\]
The original leaf \(g\) is concave on \([0,1/2]\), with
\(g(1/2)=0\). Its chord from \(1/4\) to \(1/2\) yields
\[
                          g(5/12)\ge G_0/3.
 \tag{A12}
\]
Evaluating (A4) at \(a=5/12\) and using (A10)–(A12) proves
\[
 \boxed{\quad
 \Omega_{TA}-\max_{0\le z\le1/2}f_A(z)
 \ge \frac{G_0}{3}-\frac16\log(3/2)
 >\frac1{10}.
 \quad}
 \tag{A13}
\]
The last inequality is elementary and requires no numerical evaluation.
The alternating Catalan series gives \(G>1-1/9=8/9\);
the classical bound \(\pi<22/7\) therefore gives \(G_0>56/99\).
Also \(\log(3/2)<1/2\). Hence the middle expression in (A13) is
strictly larger than
\[
 \frac{56}{297}-\frac1{12}=\frac{125}{1188}>\frac1{10}.
\]
This constant is independent of the product syntax, its size and all
additive rigid-profile constants. No compact family or lower bound on
its intrinsic satellite curvature is required.

### A.4. Reflection and pressure comparison

The exact two-leaf root satisfies
\[
 X_2(B)X_2(-B)=\frac12.
\]
Equation (A8) consequently gives
\(f_{hh}'(1-z)=-f_{hh}'(z)\). The difference
\(f_{hh}(z)-f_{hh}(1-z)\) has zero derivative and vanishes at \(1/2\);
therefore \(f_{hh}\) is symmetric under \(z\mapsto1-z\).

Integrating (A9) from \(1-z\) to \(z\) proves
\[
 f_A(z)\ge f_A(1-z)\quad (1/2\le z\le1),\qquad
                         \Omega_{TA}\ge\Omega_A.
 \tag{A14}
\]
For \(1/2<z<1\), the first inequality is strict if either child is type
\(A\). The maximizing probe for \(\Omega_A\) is strictly in \((0,1/2)\),
so the pressure inequality is then strict too. With two \(L\) children,
both profiles differ from the symmetric \(hh\) profile only by a
constant, so \(\Omega_{TA}=\Omega_A\).

The unturned product condition is essential to the proof. Applying an
outer turn reverses the output derivative, and does not preserve (A9)
or the claimed orientation of (A14). This note makes no corresponding
claim for an arbitrary type-\(A\) expression with a top turn.

### A.5. Exact scope for the pending signed estimate

The result proves the requested classical inequality for the high
Newton-index part of a candidate unflagged-turn estimate, if that part
has already been bounded by the original lower-half profile. It does
not itself establish that quantum coefficient bound or replace the
original signed coefficient by its positive profile. The separate
[coefficient-cone theorem](actual_conway_unflagged_core_probe_bound.md)
supplies its own exact finite adapter.

The low Newton part uses a separate source-exact alias or spectral
estimate; it is not inferred from this pressure inequality. Likewise (A14) does not allow the exponential norm of an
arbitrary turn to be charged to a new physical leaf. There is no new
source-circle insertion, isotopy, geometric volume replacement, or
full mixed-hub theorem here.

## scope

This is an analytical proof, with no numerical test or inferred
topological re-rooting. The signed coefficient bound, local packet,
primitive filling calibration and eventual invariant limit remain
separately named inputs.
