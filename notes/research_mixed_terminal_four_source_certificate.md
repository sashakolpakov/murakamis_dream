# A unified certificate design for the type-four terminal source

Research design, 5 November 2026. This is one validation rule for the
eight flattened reduced faces, twelve reduced alias families, and one
raw half-transform face. A complete author record and an independent
saved replay would supply their signs and the complete type-four
terminal theorem through the already proved source reductions. No
author attempt or replay of this rule has been run. All twenty-one
signs remain unproved.

The new driver is
[certify_mixed_terminal_four_source.py](../experiments/certify_mixed_terminal_four_source.py).
Its exact-root, interval-tightening, clipped target gain, and saved-tree
mechanics adapt the completed type-three alias driver. Existing
proofs, scripts, source records and replay records remain unchanged.

## 1. Reference domains and the original phase

Let \(D_3,D_4\) be the two full original input disks of
[open localization](research_mixed_open_word_critical_localization.md).
The reference domain of this new design is explicitly
\[
 \mathcal D_3=D_3,
 \qquad \mathcal D_4=D_4\cap\{\Im a_*\ge-27/250\}.
 \tag{1}
\]
Since \(D_4\) has center \(.30-.052i\) and radius
\(.064\), its new lower cut is normalized coordinate
\(-7/8\). No conclusion on the removed part of \(D_4\)
is intended. The boundary \(\Im a_*=-.108\) is retained.

Every actual incoming nonprivate leg at the terminal vertex of an
open word of length at least two lies in these sets. For an ordinary
type-four leg, the full-input block image has height greater than
\(-.102\); the opposite attached type-four endpoint leg has
height greater than \(-.108\). These are respectively the full
map bounds in [the ordinary height theorem](research_mixed_cyclic_critical_height_bounds.md)
and [the exact endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md),
as assembled in [local factor coverage, Section 1](research_mixed_open_local_factor_coverage.md).
Thus the mask does not remove an actual terminal input, including
the two-endpoint case at length two. It is not a claim that every
point of either auxiliary reference set is realized by an open word.

For \(a_*=A+iH\) let \((e_*,t_*,u_*)\) be the original
own-type-four endpoint root. Its order is private, attached, Newton.
Always define the reference action by the full original expression
\[
 \begin{split}
 P(a_*)&=F_1(a_*;e_*,t_*,u_*),\\
 F_1(a;e,t,u)&=F(e,u)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)\\
 &\quad-i\pi e(1-e)/2+2\pi iat,\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu.
 \end{split}
 \tag{2}
\]
The original logarithmic lift, every mark, and both endpoint
factorials are those of [the exact triple source](research_mixed_terminal_four_joint_source.md).
The target reduced phase uses the already certified canonical branch
\[
 u_c(e)=\frac1\pi\arctan\frac{i+\sqrt{1-2e^{2\pi ie}}}{2},
 \qquad \Phi_1(a;e,t)=F_1(a;e,t,u_c(e)).
 \tag{3}
\]
The [endpoint-cap theorem](research_mixed_endpoint_cap_rectangle.md)
fixes this branch on \(E_{\rm cap}\). Evaluating (3) is not a
new critical-root proposal. The reference value in (2) continues to
use the inherited three-variable root, not a separate scalar solve.

Set
\[
 \begin{gathered}
 I_a=[.22,.45],\quad I_t=[.15,.50],\quad I_e=[.27,.49],
 \quad I_u=[.10,.269],\\
 \kappa=1/2500000,\qquad \mu=3/100,\qquad \delta=1/20000,\\
 B(a_*;y)=\Re P(a_*)+\Re P'(a_*)(y-A)-\kappa(y-A)^2.
 \end{gathered}
 \tag{4}
\]

## 2. Twenty-one literal families

In each family the external target is \(a=y+iH\), with
\(y\in I_a\). All listed free real variables range over
their entire intervals, including endpoints. Write
\(h_t=\Im t_*\), \(h_e=\Im e_*\).

| Families | Target coordinates | Penalty |
|---|---|---|
| Two flattened transform faces | \(t=.15,.50\) real; \(e=z+ih_e\), \(z\in I_e\) | zero |
| Two flattened private faces | \(e=.27,.49\) real; \(t=x+ih_t\), \(x\in I_t\) | zero |
| Four corners | both \(t,e\) real at their cuts | zero |
| Four transform single aliases | \(t=x\pm.12i\); \(e=z+i\sigma h_e\), \(\sigma=0,1\) | \(.24\pi\) |
| Four private single aliases | \(t=x+i\sigma h_t\); \(e=z-.055i\) or \(z+.04i\), \(\sigma=0,1\) | \(.11\pi\) or \(.08\pi\) |
| Four double aliases | \(t=x\pm.12i\); \(e=z-.055i\) or \(z+.04i\) | \(.35\pi\) or \(.32\pi\) |
| One raw half-transform face | \(t=.50\) real; \(e\in I_e,u\in I_u\) both real | zero |

For the first twenty families use \(\Psi=\Phi_1\); for the
last use \(\Psi=F_1\) without eliminating \(u\). The latter
includes the global raw half-face maximizer by
[the upper-triangle theorem](research_mixed_terminal_four_right_triangle.md).
The bare deficit to be certified is
\[
 D(a_*;X)=\Re\Psi-L-\Re P(a_*)
                    -\Re P'(a_*)(y-A)+\kappa(y-A)^2< -\delta.
 \tag{5}
\]
Here \(X\) denotes precisely the free real coordinates in that
row of the table, and \(L\) is its displayed penalty. An actual
height retained in an unaliased coordinate pays no penalty.

The [reduced-current theorem](research_mixed_terminal_four_reduced_currents.md)
proves \(-\Re\Phi_1''\succ(\pi/100)I_3\) on every
reduced target product in the table. The broad full Hessian gives
the same bound for the raw family at \(t=.5\). Therefore every
free-target principal Hessian of (5) satisfies
\[
                    D_{XX}''\preceq-\mu I,
       \qquad \pi/100-2\kappa>\mu.
 \tag{6}
\]
This includes constrained maxima at the target endpoints; no grid
of moving roots or target points is used to prove the upper bound.

## 3. Exact reference derivatives and a whole-target acceptance rule

For a fixed rational trial \(X^0\), set \(d=y-A\), and let
\(s_t,s_e\in\{0,1\}\) indicate the retained reference
heights. At most one flag is nonzero. Both are zero for the raw
half-face. The exact canceled reference derivatives are
\[
 \begin{split}
 D_A={}&-d\Re P''-2\kappa d
       -s_t\Im\Psi_t\Im t_*'-s_e\Im\Psi_e\Im e_*',\\
 D_H={}&\Im(P'-\Psi_a)+d\Im P''
       -s_t\Im\Psi_t\Re t_*'-s_e\Im\Psi_e\Re e_*'.
 \end{split}
 \tag{7}
\]
The penalties are fixed and have zero derivative. These expressions
differentiate the fixed trial, not an optimizing target. They keep
the complete complex responses of both possible retained heights.
The reference formulas are
\[
 \begin{split}
 P'&=g'(a_*+t_*)-g'(a_*)+2\pi it_*,\\
 P''&=g''(a_*+t_*)(1+t_*')-g''(a_*)+2\pi it_*',\\
 (e_*',t_*',u_*')^T&=-f_z^{-1}f_a,
 \qquad f_a=(0,\pi\cot\pi(t_*+a_*)+i\pi,0)^T.
 \end{split}
 \tag{8}
\]
The system \(f\) is the original unexponentiated own-four
endpoint system. In particular the driver passes own flag one in
every root, Jacobian, residual, and response call.

At the target, the partials in (7) come from
\[
 \begin{split}
 F_{1,a}&=g'(a+t)-g'(a)+2\pi it,\\
 F_{1,t}&=g'(a+t)+g'(e+t)-3g'(t)+2\pi ia,\\
 F_{1,e}&=F_e(e,u)+g'(e+t)-g'(e)-i\pi(1/2-e),\\
 F_{1,u}&=F_u(e,u).
 \end{split}
 \tag{9}
\]
For a reduced target insert \(u_c(e)\); its original equation
\(F_u=0\) removes the chain term in \(\Phi_{1,e}\).
For the raw family retain the literal real \(u\).
The free-target derivatives of (5) are respectively
\(\Re\Psi_a-\Re P'+2\kappa d\),
\(\Re\Psi_t\), \(\Re\Psi_e\), and
\(\Re\Psi_u\), keeping only the free coordinates in that family.

First intersect a reference rectangle with the mask (1). Let its
physical center be \(a_0\), halfwidths be \(r_A,r_H\),
and let \(v_0\) be an outward midpoint upper bound for (5).
Whole-rectangle enclosures of (7) give the fixed-trial bound
\[
             v=v_0+r_A\sup|D_A|+r_H\sup|D_H|.
 \tag{10}
\]
For each free target interval \([\ell_j,r_j]\), enclose the
target slope at \(X^0\) on that same whole reference rectangle
by \([\beta_j^-,\beta_j^+]\). Define
\[
 \begin{split}
 q_j^-&=\operatorname{clip}(\beta_j^-/\mu,\ell_j-X_j^0,0),\\
 q_j^+&=\operatorname{clip}(\beta_j^+/\mu,0,r_j-X_j^0),\\
 C_j&=\max\{\beta_j^-q_j^--\mu(q_j^-)^2/2,
                 \beta_j^+q_j^+-\mu(q_j^+)^2/2\}.
 \end{split}
 \tag{11}
\]
Strong concavity (6) proves
\[
                   D(a_*;X)\le v+\sum_j C_j
                   \quad\hbox{for all free targets }X.
 \tag{12}
\]
If an interval clipping comparison is undecidable, the driver may
use the larger unconstrained quadratic gain. Acceptance is solely
the strict outward inequality \(v+\sum C_j<-1/20000\).
Floating coordinate ascent proposes a rational trial only; exact
membership and (10)--(12) validate it. No floating decision establishes
a source sign, a root, or an exclusion.

## 4. Original roots, complete coverage, and resumable records

The original author and 320-bit replay have identical full input
trees. The driver reconstructs all 10,978 nodes, 5,258 accepted
root witnesses and 233 exact exclusions in their original right-first
order. It selects the 1,911 own-four leaves: 1,002 with type-three
external disk and 909 with type-four external disk. Pairing each
leaf with all twenty-one families gives exactly 40,131 ordered jobs.

All these jobs remain present despite the mask. Each new tree
partitions its original inherited reference rectangle, with every
split axis recorded explicitly. On a leaf the source rule uses the
exact intersection with normalized height \(\ge-7/8\) for
type-four inputs. An exclusion is allowed only if that intersection
is empty, or its exact minimum squared normalized radius is strictly
greater than one. A touching mask or circle boundary is retained.
Thus the record proves exactly (1), not the full old \(D_4\).

Before any acceptance on an inherited leaf, its saved rational
center, inverse \(Y\), and positive radius are revalidated by
the original own-four self-map test on the whole old rectangle.
Its complete private, attached and auxiliary image boxes are also
checked. No complex root is proposed. The same inverse gives an
initial tightened radius \(b/(1-q)\), followed by five interval
Taylor-image intersections on a parameter box and twelve at its
midpoint. The existing root is contained in every such intersection.
Eight Neumann terms and the outward remaining geometric tail
enclose (8). The canonical formula (3) is evaluated only for target
endpoint parameters on its already certified rectangle.

Author mode may subdivide only the reference rectangle after a
failed interval source bound. Its split score is the two contributions
in (10); this heuristic affects only the partition. Every attempt is
bounded by 600,000 additional committed nodes, 600 seconds of its
numerical loop, and added depth at most 45 (default 20). The active
box remains on the frontier throughout fallible arithmetic. Signal-
masked commits append either its acceptance, exclusion, or exact two
children. A depth limit, time limit, or arithmetic failure preserves
the unresolved frontier. Attempted and committed node counts are
recorded separately. There is no automatic restart or cap extension.

A checkpoint is published atomically. Resumes read an immutable
incomplete input and write a distinct new output; they retain every
completed tree and active prefix. The reconstructed exact frontier
must agree with the saved one. The proof, driver, family inventory,
reference mask, source records, replay records and recursive hash
bindings must all agree before continuation.

Saved replay accepts only a complete record. It disables root and
target proposals, revalidates the original witnesses, follows the
stored axes, uses precisely the saved rational trials, and checks
every accepted inequality anew. It neither refines nor searches.
The author time cap is not imposed on this exhaustive saved replay.
All bound files and the immutable input are checked again before
publication. A partial record is not a proof of the unvisited jobs.

The endpoint-cap author and its 320-bit replay are also bound with
identical saved trees. Their certified phase branch and full complex
packet are source inputs, not inferred from the new target tests.
The inherited endpoint-image record, the new source/current/exterior
proofs, and the saved elementary Hessian and end-tail constants are
bound independently of any proposed target coordinates.

## 5. The conditional source conclusion

A complete pass and saved replay would establish (5) on (1) for
all twenty-one families. The first twenty then control the retained
double rectangle, with its complete ordinary Newton sum and original
\(+N^2\) residue coefficient. The nonzero local term has power
\(N^{-2}\). The same twenty conditions control both entire
private tails by [the coherent private-tail theorem](research_mixed_terminal_four_private_tails.md).
They also control the remaining small transform indices by
[the left-strip theorem](research_mixed_terminal_four_left_strip.md).
The last comparison controls the complete upper transform triangle
by the already proved entropy reduction. The initial transform rows
are removed first as whole coherent sums by the existing end-tail
theorem. This is precisely the disjoint finite partition proved in
the left-strip note, including the even half-level row.

These implications retain the bare deficit throughout. An actual
unselected incoming type-four halfweight is added afterward by its
nonpositive convex Bregman remainder, using its actual negative
height. The positive-height part of the auxiliary domain (1) gives
no different finite Fourier branch. Neither a square root at a
Fourier zero nor division by a Fourier polynomial is used.

One total sufficiently small exponential tolerance pays finite
prefactors, half-grid shifts, and small ordinary-color perturbations;
Cauchy's formula gives the fixed ordinary derivatives on smaller
disks. A completed certificate would therefore prove the whole
type-four terminal packet and its independent horizontal supporting
plane on the stated actual-reference scope. It would not by itself
settle the remaining open-word contour sectors, ordinary closure,
branching, or arbitrary short fillings.

At present this is an unexecuted certificate design. The analytically
proved source reductions supply its sufficiency, not its twenty-one
numerical signs.
