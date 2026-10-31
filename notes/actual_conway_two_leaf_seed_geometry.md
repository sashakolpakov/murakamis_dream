# Two-leaf seeds in the actual complete Conway geometry

31 October 2026. Internally reviewed geometric extension and dependency
audit. Keep the original retained crossing-circle leaf \(h\), its literal
turns and identity stacks. Allow seeds \(A_s=h^s\) for every fixed \(s\ge2\)
and the grammar
\[
E::=A_s\mid T(E)\mid EE.
\]
Consider the actual cylindrical closure \(C(FG)\), where both \(F\) and
\(G\) are expressions in this grammar. Isolated \(C(A_2)\) is excluded.

The strict complete source optimizer builds the actual complete
finite-volume right-angled two-ball link metric. Every fixed retained
half-twist partner has the same complete volume. The marked deformed
representation and its actual filled-volume action also extend. The old
restriction \(s\ge3\) is unnecessary for these geometric statements.

This note does not assert a universal mixed-color or alias gap. The
[two-leaf source theorem](actual_conway_two_leaf_seed_source.md) treats
the finite source, rounding and packet separately; the
[algebraic leaf certificate](actual_conway_algebraic_leaf_alias_certificate.md)
supplies an additional sufficient alias condition. A full quantum limit
requires those analytic hypotheses.

## 1. The exact new strict base

For every prescribed seed output \(b\in(0,1)\), choose
\[
\frac b2<a<\min\left(b,\frac12\right).
\]
Take both leaves of \(A_2=hh\) equal to \(a\). The single retained product
\((a,a)\mapsto b\) has
\[
p=q=b-a>0,\qquad r=2a-b>0,\qquad w=1-2a>0.
\tag{1}
\]
Both leaf atoms and all three product atoms are strict. This is an
existence state of the original wire polytope; it imposes no equal-label
restriction on the finite source sum.

The [old seed extension](actual_conway_arbitrary_width_seeds.md), from
\(A_{s-1}\) to \(A_s\), now starts at \(s=2\). Choose a last leaf
\(0<c<\min(b/2,1-b,1/4)\), set \(t=b-c/2\), use a strict \(A_{s-1}\)
state at \(t\), and attach \((t,c)\mapsto b\). At a macro product choose
both child outputs in \((b/2,\min(b,1/2))\); at a turn use the child
output \(1-b\). Every proper expression therefore has a strict state at
every \(b\in(0,1)\). For \(C(FG)\), delete only the forced final gate,
whose two input loads sum to \(1\), and choose both child outputs to be
\(1/2\). This gives a strict reduced state.

The [complete boundary barrier](actual_positive_conway_hyperbolic_volume.md),
§2, now applies without change. Every proper endpoint wire propagates
to a leaf endpoint or a product with a nonvertex-flat atom
\((0,a,1-a)\). Any saturated retained product inequality similarly
exposes such an atom. Its positive infinite directional derivative
toward the strict state cannot be canceled by any other atom, whose
derivative is finite or positive infinite. Every maximizing leaf and
retained prism is consequently strict.

The retained tetrahedron angle maps recover all leaf and product wires;
turns recover their wires, and the deleted final gate adds no free
direction. Strict concavity gives a unique maximizer and a negative
definite reduced Hessian. Fixed proper-output profiles are real analytic
on \((0,1)\). None of this argument uses a third leaf once (1) is supplied.

## 2. Exact \(A_2\) ports and the unchanged macro inequalities

Use the original port variables \(B=\cot(\pi b)\), \(X,Y>0\), with
\(X^2+Y^2-B^2=1\). A leaf of complete label \(a\) has
\(B=X=\cot(\pi a)>0\) and \(Y=1\). The actual stationary product laws are
\[
B_{\mathrm{out}}=\frac{B_1B_2+X^2-1}{B_1+B_2},
\qquad
Y_{\mathrm{out}}=\frac{Y_1Y_2}{B_1+B_2},
\qquad B_1+B_2>0.
\tag{2}
\]
At the unique optimized \(A_2\) state, the two leaves have the same
\(X\), directly by the stationary input equations. Therefore
\[
B=X-\frac1{2X},\qquad Y=\frac1{2X},\qquad X>0,
\qquad B+Y=X>0,\qquad X-B=\frac1{2X}>0.
\tag{3}
\]
In particular \(-Y<B<X\). Moreover \(B(X)\) is strictly increasing
from \(-\infty\) to \(+\infty\), so for every \(b\in(0,1)\) its
selected solution is the unique positive
\[
X=\frac{B+\sqrt{B^2+2}}2.
\tag{4}
\]
This agrees with strictness; no branch is inferred from a squared
equation alone.

For all \(s\ge2\), the original Chebyshev recurrence gives
\(B_s=T_s(X)/U_{s-1}(X)\), \(Y_s=1/U_{s-1}(X)\), and the same strict
inequality \(-Y_s<B_s<X\). Its proof can start at (3). Equivalently,
when \(X=\cos\alpha<1\), put \(h_0=\sin\alpha\) and use
\(B_s=h_0\cot(s\alpha)\), \(Y_s=h_0\csc(s\alpha)\), with the positive
denominators selecting \(0<s\alpha<\pi\). The hyperbolic \(X>1\)
branch and the \(X=1\) limit have the same inequalities.

The [macro preservation proof](actual_conway_strict_leaf_quarter_bound.md)
uses only this inequality. The literal turn
\((B,X,Y)\mapsto(-B,Y,X)\) preserves it. At a product with \(X<1\),
put \(h_0=\sqrt{1-X^2}\), \(\alpha=\arccos X\), and write the child
ports as
\((B_i,Y_i)=(h_0\cot u_i,h_0\csc u_i)\).
Their inequalities give \(u_i>\alpha\); the positive denominator in
(2) gives \(u_1+u_2<\pi\). The output has angle \(u_1+u_2\), hence
again \(-Y_{\mathrm{out}}<B_{\mathrm{out}}<X\).

For \(X\ge1\), the same inequality places each child \(B_i\) between
\(\sqrt{X^2-1}\) and \(X\). Thus \(0<X-B_i<1\), and
\[
B_{\mathrm{out}}-X
=\frac{(X-B_1)(X-B_2)-1}{B_1+B_2}<0.
\]
The output \(B\) is positive, supplying its lower inequality. All
steps include the \(A_2\) base without a new hypothesis.

At the closed root, the actual ordered port matching gives
\((B,X,Y)\) and \((-B,X,Y)\). Applying \(-Y<B<X\) to both yields
\(|B|<\min(X,Y)\). The hyperboloid identity implies \(X<1\), \(Y<1\).
These bounds propagate down each macro product: its common \(X<1\)
stays fixed; writing its child angles \(u,v\) as above,
\(Y_{\mathrm{out}}<1\) gives \(u+v<\pi-\alpha\). Since \(u,v>\alpha\),
each child has \(\alpha<u,v<\pi-\alpha\), hence \(Y_{\mathrm{child}}<1\).
Turns exchange \(X,Y\). Stop at a seed, not at its individual leaves,
whose \(Y\) is \(1\).

For a proper seed \(A_s\), \(Y_s<1\) implies
\(\sin(s\alpha)>\sin\alpha\), consequently \((s+1)\alpha<\pi\). Thus
\[
\cos\frac{\pi}{s+1}<X<1,\qquad
\frac14<a<
\frac1\pi\arctan\!\left(\sec\frac{\pi}{s+1}\right)
\le\frac{\arctan2}{\pi}.
\tag{5}
\]
For \(A_2\), this is precisely \(1/2<X<1\) and
\(1/4<a<\arctan(2)/\pi\). The upper endpoint differs materially
from the old \(\arctan(\sqrt2)/\pi\) mixed-source bound.

## 3. The complete geometric inputs

The existing geometric proof can now be read with \(A_2\) as its base,
without changing a local cell, ordered face map or cut.

- The leaf pyramid requires only \(0<a<1/2\). Its two shaded
  triangles, right apex edges and ordered base quadrilateral are unchanged.
- The [ideal multiplication prism](actual_newton_ideal_prism_and_associativity.md)
  requires exactly \(p,q,r,w>0\). Its three ideal tetrahedra, face
  metrics and dihedral-angle formulas use only these strict variables.
  There is no seed-width parameter in the local theorem.
- The ordered stack maps remain
  \(F:(C_0,C_1,C_2,C_3)\mapsto(v_0,v_1,P,\infty)\) and
  \(G:(C_0,C_1,C_2,C_3)\mapsto(\infty,P,v_2,v_3)\).
  Stationarity matches the full ordered quadrilateral metrics.
  A turn rotates this actual frame.
- Convex attachment uses the same angle sums \(\pi/2\) or \(\pi\)
  on input CAP edges and strict output angles \(\pi b,\pi(1-b)\).
  The first \(A_2\) product already has the completed port pattern
  PORT, WHITE, SHADED, WHITE. Products and turns preserve it.
  Supported-face gluing prevents accidental vertex identifications
  outside the common face; the cell adjacency is a tree.
- Both root children in \(C(FG)\) are completed cells, including
  \(A_2\) and turned \(A_2\). The actual closed map
  \(C_j\mapsto C_{3-j}\) preserves the ordered metric and FREE/CAP
  pairs. Both opposite angle pairs sum to \(\pi\), so the common
  face disappears as a flat white seam. The result is the same
  convex ideal right-angled polyhedron, with every nonflat edge in
  an original leaf bowtie.
- The [literal projection-ball cut](actual_conway_bowtie_projection_cut.md)
  uses only the original leaf boxes, segment pairings, turns and
  stacks. Its ribbon induction gives exactly the shaded triangles,
  white facial walks and cyclic orders of the metric construction.
  It does not count at least three leaves in an open seed.
  The existing caveat remains: an auxiliary open quadrilateral
  port is not itself half of a physical four-punctured tangle boundary.
- Every finite edge has the same pointwise four-step return and
  four right angles. Canonical rectangular cusp links give equal
  opposite shaded sides. Scaling them to length \(1\) makes every
  shaded-triangle and copied-white gluing preserve horospheres.
  The reversible cut identifies their compact links with cusp
  tori. Completeness and finite volume follow.

If \(V_E\) is the original source-selected sum of leaf and prism
volumes, the actual pure augmented exterior \(Y_E\) therefore satisfies
\[
\operatorname{Vol}(Y_E)=2\max V_E.
\tag{6}
\]
This identifies the geometric variational value. The finite quantum
source requires its separate positivity and rounding argument.

The algebraic shape and rational Bloch-chain comparison also uses
only these local pyramids and prisms, their five-term relations, the
common algebraic coordinate field, and this degree-one closed
fundamental chain. It introduces no further \(s\ge3\) hypothesis.

## 4. Complete retained half-twist partners

The [complete half-twist partner](actual_conway_half_twist_partner_geometry.md)
changes the original shaded-disk pairings across the two projection
copies. Its three exact edge words are identities for
\(E=e^{2\pi i a}\) throughout \(0<a<1/2\). They do not require
\(a\le\arctan(\sqrt2)/\pi\) or a seed of length \(3\).
Every edge belongs to one original leaf bowtie, so arbitrary fixed
signs select one of the already checked pure or odd edge words.
The canonical triangle decorations are preserved by the changed
vertex bijections. Hence every fixed sign pattern \(\epsilon\) has
an actual complete finite-volume metric with
\[
\operatorname{Vol}(Y_E^\epsilon)
=\operatorname{Vol}(Y_E)=2\max V_E.
\tag{7}
\]
The primitive meridian and longitude paths and their rectangle-area
checks are local and remain nonsingular for \(0<a<1/2\).

This is a complete geometric statement. The old whole mixed-color
supporting-plane estimate need not hold throughout (5); a complete
metric alone does not identify the independently long filled quantum
asymptotic.

## 5. The two exclusions and the source interface

Isolated \(C(A_2)=C(hh)\) has forced last inputs \(x+y=1\), with
both leaves at most \(1/2\). Thus \(x=y=1/2\). Both leaf cells and
the last gate are flat, so there is no strict reduced assignment.
It is excluded here. Its flat source alone does not establish a
topological nonhyperbolicity statement.

There is also a genuine finite-level change. For even \(N=2m\),
the leaf Newton support ends at \(M=m-1\). The \(A_2\) coefficient
at the top degree \(d=2m-1\) is absent, because a product has
output at most \(2M=d-1\). The old assertion that every robust
seed has every coefficient positive for every \(N\ge3\) cannot
be quoted with \(A_2\) substituted. For odd \(N\), \(2M=d\).
These endpoint facts do not obstruct a fixed strict interior
optimizer, but the source theorem must round on the actual
support. That audit is separate from (6)–(7).

The complete geometric argument has no remaining use of \(s\ge3\).
That restriction did supply the old mixed alias interval. Every
expression, turn, sign pattern and diagram is fixed; this note
claims no uniform estimate over unbounded trees.

## 6. The deformed representation and primitive filling action

The marked geometric interfaces also extend. Retain all original
free wires \(y\), delete only the forced-flat final gate, and use
the original pure mixed-core action
\[
\begin{aligned}
f_0(y,t)&=\sum_i g(x_i(y),t_i)+\sum_{\mathrm{products}}m,\\
g(x,t)&=J(2x)-2J(x)-J(x-t)-J(x+t),\\
J(a)&=\int_0^a\operatorname{Log}(2\sin(\pi u))\,du.
\end{aligned}
\tag{8}
\]
The logarithmic sheets continue from the strict complete chamber.
Section 1 supplies the same invertible complete wire Hessian.
Thus the free-wire equations have one holomorphic critical branch
near independent \(t=0\), with separately even critical action
\(\phi_0(t)\). Every complete leaf in (5) lies in the original
strict high branch \(1/4<x<1/2\).

For a retained half-twist \(\epsilon\in\{0,+1,-1\}\), the original
[selected-source shear](actual_odd_conway_complex_color_packet.md) is
\[
\begin{aligned}
v&=g_t(x,t),&
\chi&=t-\frac{\epsilon v}{2\pi i},\\
f_\epsilon(x,\chi)&=g(x,t)-\frac{\epsilon v^2}{4\pi i},&
df_\epsilon&=g_x\,dx+v\,d\chi.
\end{aligned}
\tag{9}
\]
At \(t=0\), the change of variables has derivative
\(1-\epsilon i\cot(\pi x)\), nonzero for every \(0<x<1/2\).
The source-branch verification uses \(x>1/4\) to select its simple
root and fixes the additive constant by continuation to \(x=1/2\).
It has no upper cutoff \(\arctan(\sqrt2)/\pi\). Consequently (5)
supplies every local branch assumption, including for \(A_2\).
This does not establish a global alias bound.

For explicit geometric data, set \(E=e^{2\pi i x}\), \(T=e^{2\pi i t}\),
and
\[
Z=\frac{1+E}{1+T},\qquad
R=\frac{T(1+E)^2}{E(1+T)^2},\qquad
Z^2-(1+E)Z+ER=0.
\tag{10}
\]
Use the original ordered port \((0,\infty,1,R)\), first-ball flag
\(Z\), and second-ball flag \(Z/E\). The same four white/completion
matrices \(W_0,\ldots,W_3\) from the
[pure marked theorem](actual_conway_marked_peripheral_deformation.md)
apply. Its nine prism identities and turn/closure identities are
rational identities in independent local angle phases; they contain
no seed width. They propagate one Möbius map on each original white
face through every \(A_2\) product. Nonplanar deformed white pieces
are not assumed to be reflection planes.

At pure leaves keep the original within-copy shaded map \(S\).
At odd leaves retain the original cross-copy maps \(A,B\). Their
three pointwise edge words
\[
W_0^{-1}BW_2^{-1}A,\qquad
W_2^{-1}BW_0^{-1}A,\qquad
W_1^{-1}BW_3^{-1}A
\]
are identities for independent \(E,R\), not only at completeness.
The same closed bowtie quotient gives the actual group presentation.
These matrices therefore define a representation of the actual
signed augmented-link exterior in a bounded framed neighborhood of
its complete holonomy. Matching a port cross ratio alone is not
being used to infer a group or physical tangle boundary.

The main meridian still crosses its two original white sectors,
whose \(W\) maps have the same derivative at the corner. It is
parabolic and remains nonidentity near the complete anchor; its
whole peripheral commutant remains parabolic. At an auxiliary flag,
the original disk longitude has multiplier \(Q^2\), where
\[
\rho=\frac{Z}{1+E-Z},\qquad Q=\frac{E-Z}{Z-1}.
\]
The pure meridian multiplier is \(\rho\); the two primitive signed
collar paths have multipliers \(\rho Q\) and \(\rho/Q\).
Their complete translations and two-rectangle area give the same
original primitive marking. The physical \(R^\epsilon\) sign is
fixed by the original local threading calibration. The
[signed marked theorem](actual_odd_conway_marked_peripheral_deformation.md)
therefore gives, with the same small logarithms,
\[
U_i=-2\pi i\chi_i,\qquad
V_i=-2\partial_i\phi_\epsilon(\chi),\qquad
U_i=U_i^{\mathrm{pure}}-\frac{\epsilon_i V_i}{2}.
\tag{11}
\]
This half-longitude shear compares the actual signed cusp lattices;
it does not assert that half a longitude is primitive in either
one. The physical filled crossing power is exactly \(\epsilon_i-2p_i\).

The selected primitive \(G_\epsilon=2\pi i\phi_\epsilon\) retains
its local quadratic correction \(-\epsilon_iV_i^2/8\), with
\(dG=\tfrac12\sum_i V_i\,dU_i\). Its complete value is the actual
signed volume (7), on the same oriented family. The original
fundamental-chain differential gives the absolute identity
\[
\operatorname{Vol}(\rho_\chi)
=\operatorname{Im}G_\epsilon
-\frac12\sum_i\operatorname{Re}U_i\,\operatorname{Im}V_i.
\tag{12}
\]
There is no added integration constant, framing character or
unrelated representation component.

For any fixed filled auxiliary subset and independently sufficiently
long fixed signed integers \(p_i\), the selected-action saddle
\[
\partial_i\phi_\epsilon+
\frac{\pi i}{p_i}(\chi_i-1)=0
\]
is exactly \(U_i+p_iV_i=-2\pi i\). The complete auxiliary Hessian
is nonsingular: \(\cot(\pi x_i)>0\) and
\(1-\epsilon_i i\cot(\pi x_i)\ne0\). Thus the small saddle exists
for all sufficiently small independent \(1/p_i\). Unfilled cusps
remain parabolic by separate evenness.

The [marked geometric completion theorem](general_source_regulator_hyperbolic_equality.md)
identifies this bounded framed branch with the smooth complete
holonomy of the actual signed filled topology. At that saddle,
(12) becomes
\[
\operatorname{Vol}(Y_E^\epsilon(p))
=2\pi\operatorname{Re}\!\left[
\phi_\epsilon(\chi_*)+
\frac{\pi i}{2}\sum_{i\ \mathrm{filled}}
\frac{(\chi_i-1)^2}{p_i}
\right].
\tag{13}
\]
When every auxiliary circle is filled and the fixed parity pattern
has one main component, this is the actual knot complement volume.
Partial fillings retain the corresponding augmented-link cusps.
In hidden pure variables the equation has \(p_i-\epsilon_i/2\);
replacing it by ordinary rational filling of the pure partner
would change the primitive angle and marking. No such replacement
is made here.

The geometric input to the
[original whole-period theorem](general_original_source_long_filling_transfer.md)
therefore extends throughout the stated \(s\ge2\), \(C(FG)\) grammar.
A full invariant equality follows only when its actual finite
packet, rounding and whole-source complement estimates are also
supplied. A separately proved condition such as
\(\cot(\pi x_i)\ge2/3\) at every complete leaf can supply the new
alias estimate; it is not automatic from (5).

## Dependencies and internal review

The proof extends the local cells, ordered maps and primitive
markings of the linked original notes. In particular, the
[signed long-filling theorem](actual_odd_conway_long_filling_volume.md)
keeps geometry, the finite complex packet, and the whole-source
gap as distinct inputs. No previous theorem file is changed.

Author analytical audit: complete. The source-transport reviewer
independently read §§1–6 and passed the strict base, port propagation,
completed-cell geometry, source branch and primitive filled-volume
interfaces. The coherent-source reviewer independently passed the
deformed and marked interface in §6. The primary reviewer independently
passed §§1–6, including the local shear, original primitive marking
and absolute volume normalization, with the invariant limit conditional
on the separate source estimates. These are internal proof reviews,
not external peer review. No numerical test is used to infer this
uniform geometric extension or a quantum asymptotic.
