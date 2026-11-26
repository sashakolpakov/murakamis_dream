# A proposed certificate for the mixed terminal Newton faces

Research design, 5 November 2026. This note proves a finite-dimensional
upper-certificate rule for the eight mixed zero-mode face families.
It does not assert that those inequalities have passed. The reference
parameters are the whole two original input disks, covered by the
already saved endpoint witnesses. No word samples, new reference
domain, or proposed moving target root enter the rule.

## 1. The eight families and their exact defect

Retain the original reduced phase \(\mathcal T(a;t,u)\) and the
joint Hessian theorem from
[the joint zero-mode proof](research_mixed_terminal_three_joint_zero_mode.md).
For a reference \(a_*=A+iH\) in either original input disk, let
\(t_*(a_*)\), \(u_*(a_*)\) be the selected type-three endpoint
coordinates. Their original action is \(\mathcal P(a_*)\), with
the exact calibration and derivatives of
[the critical-curve theorem](research_mixed_terminal_three_critical_curve.md).
The full saved witnesses lie in the type-three rectangles of
[the exact endpoint-image extraction](research_mixed_open_word_endpoint_rectangles.md):
\(\Re t_*\in(.278,.391)\), \(\Im t_*\in(-.072,.021)\),
\(\Re u_*\in(.218,.242)\), \(\Im u_*\in(.049,.077)\).
Thus the critical-curve chart applies to each complete root enclosure,
not merely to its displayed midpoint.
Put \(\kappa=1/2500000\).

Use \(I_a=[.22,.45]\), \(I_t=[.15,.50]\), \(I_u=[.10,.40]\).
The eight families, for each external type, are:
\[
\begin{array}{c|c|c|c}
\text{family}&t&u&\text{free real targets}\\ \hline
t\text{ flattened}&c_t&z+i\Im u_*&(y,z)\in I_a\times I_u\\
u\text{ flattened}&x+i\Im t_*&c_u&(y,x)\in I_a\times I_t\\
\text{both flattened}&c_t&c_u&y\in I_a
\end{array}
\tag{1}
\]
where \(c_t\in\{.15,.50\}\), \(c_u\in\{.10,.40\}\), and
the first target argument is always \(a=y+iH\).
Thus there are two, two and four families respectively. The last four
must not be omitted as if the two one-coordinate flattenings included
the real-real corners.

For any family let \(X\) denote its one or two free real targets,
with first coordinate \(y\). Define its bare deficit
\[
 G(a_*;X)=\Re\mathcal T(y+iH;t,u)-\Re\mathcal P(a_*)
 -\Re\mathcal P'(a_*)(y-A)+\kappa(y-A)^2.
\tag{2}
\]
A strict negative upper bound for (2) controls the corresponding
family in equation (17) of the zero-mode proof.

It suffices to bound this bare deficit. With the external halfweight
\(-\nu g/2\), the allocated deficit differs by
\[
 -\frac{\nu}{2}
 \{\Re g(y+iH)-\Re g(a_*)-\Re g'(a_*)(y-A)\}\le0,
\tag{3}
\]
because \(y\mapsto\Re g(y+iH)\) is convex on \(I_a\).
The actual finite Fourier interpretation at \(\nu=1\) still uses
the actual negative reference height; (3) does not authorize a new
positive-height Fourier branch on the auxiliary input disk.

## 2. Strong concavity and boundary target maximizers

Every free-target principal Hessian of (2) satisfies
\[
                  G_{XX}''\preceq-\mu I,\qquad \mu=3/100.
\tag{4}
\]
Indeed Lemma 1a of the joint theorem gives \(\pi/100\), while the positive
quadratic in (2) costs at most \(2\kappa\) in its first coordinate.
The rational inequality \((157/50)/100-2\kappa>3/100\) proves (4).
The same theorem applies on the flattened faces, since all their
heights lie in the original box.

Here is the reusable box rule. Let \(X^0\) be any fixed point of the
free-target box \(Q=\prod_j[L_j,U_j]\). Suppose on a reference
parameter set one has
\[
 G(a_*;X^0)\le v,\qquad
 \partial_{X_j}G(a_*;X^0)\in[g_j^-,g_j^+].
\tag{5}
\]
For each coordinate put
\[
\begin{split}
h_j^-&=\operatorname{clip}(g_j^-/\mu,\ L_j-X_j^0,\ 0),\\
h_j^+&=\operatorname{clip}(g_j^+/\mu,\ 0,\ U_j-X_j^0),\\
C_j&=\max\{g_j^-h_j^--\mu(h_j^-)^2/2,\
             g_j^+h_j^+-\mu(h_j^+)^2/2\}.
\end{split}
\tag{6}
\]
Then the whole parameter set and target box satisfy
\[
                         G(a_*;X)\le v+\sum_j C_j .
\tag{7}
\]
Here \(\operatorname{clip}(s,l,r)=\min(r,\max(l,s))\).

*Proof.* Strong concavity bounds \(G(X^0+h)\) by
\(G(X^0)+\nabla G(X^0)\cdot h-\mu\|h\|^2/2\).
When \(h_j\le0\) the greatest admissible linear term is \(g_j^-h_j\);
when \(h_j\ge0\) it is \(g_j^+h_j\).
Each concave quadratic is maximized at the clipped point in (6).
Taking the larger of the two values and then summing proves (7).
Both half-intervals contain zero, so each \(C_j\ge0\). \(\square\)

In particular an outward gradient at an endpoint can have zero
correction. Replacing (6) by an unconstrained squared-gradient penalty
would needlessly lose this boundary information. A rational trial
near a proposed constrained maximizer is useful, but its proposal
does not determine acceptance.

## 3. Reference variation with the tangents cancelled

A direct interval subtraction of the two actions in (2) can be
replaced by an exact mean-value calculation. Fix the rational target
\(X^0\), put \(d=y-A\), and use indicators
\(\sigma_t,\sigma_u\in\{0,1\}\) for whether each target retains
the corresponding reference height. They are \((0,1)\), \((1,0)\)
and \((0,0)\) in the three rows of (1).
All derivatives of \(\mathcal T\) below are at its face target.
Primes of \(t_*,u_*,\mathcal P\) are holomorphic derivatives at
the reference \(a_*\). Exact differentiation gives
\[
\begin{split}
G_A={}&-\sigma_t\Im\mathcal T_t\,\Im t_*'
       -\sigma_u\Im\mathcal T_u\,\Im u_*'
       -d\,\Re\mathcal P''-2\kappa d,\\
G_H={}&\Im(\mathcal P'-\mathcal T_a)
       -\sigma_t\Im\mathcal T_t\,\Re t_*'
       -\sigma_u\Im\mathcal T_u\,\Re u_*'
       +d\,\Im\mathcal P''.
\end{split}
\tag{8}
\]
The reference action and its linear tangent cancel before taking
interval absolute values. The needed terminal derivatives are
\[
\begin{split}
\mathcal P'&=g'(a_*+t_*)-g'(a_*)+2\pi it_*,\\
\mathcal P''&=g''(a_*+t_*)(1+t_*')
                           -g''(a_*)+2\pi it_*'.
\end{split}
\tag{9}
\]
The fixed-target gradient is
\[
 G_y=\Re\mathcal T_a-\Re\mathcal P'+2\kappa d;
 \quad G_z=\Re\mathcal T_u\ \text{on a flattened-}t\text{ face};
 \quad G_x=\Re\mathcal T_t\ \text{on a flattened-}u\text{ face}.
\tag{10}
\]

The original three-variable endpoint Jacobian computes the responses:
if \(z_*=(e_*,t_*,u_*)\) and \(f(z_*,a_*)=0\), then
\[
                         z_*'=-f_z^{-1}f_a .
\tag{11}
\]
It must be enclosed on the same original root box, including its
complex dependence. Independent bounds for uncoupled \(t,u\) do not
replace (11).

For a saved parameter rectangle centered at \(a_0\), a validated
point enclosure gives \(G(a_0;X^0)\). Enclose (8) throughout the
whole rectangle. Its two halfwidths times the corresponding absolute
derivative bounds then give a valid \(v\) in (5). The target-gradient
intervals in (5) are evaluated on that same whole rectangle.
This proves a complete whole-reference-cell, whole-target-box
acceptance rule without a target grid.

## 4. Root enclosure, exact partitions and bounded validation

The [original endpoint record](../repro/results/research-mixed-open-word-critical-localization.json)
and its [saved replay](../repro/results/research-mixed-open-word-critical-localization-replay.json)
cover each input disk by exact Cartesian
rectangles, not only boundary circles. Its own-three families have
1,645 and 1,702 accepted leaves. The proposed check retains these
unchanged trees, their exclusions and all original rational root
witnesses. It does not need a new reference-boundary minimum principle.

For each retained leaf and all eight families, the intended strict
acceptance is
\[
                         v+\sum_j C_j<-1/2000.
\tag{12}
\]
A floating constrained target optimization may propose rational
\(X^0\); all acceptance uses outward versions of (5)--(12).
There is no complex-root proposal. At a parameter point or child
rectangle \(A_0\), a tighter enclosure follows from the *same* saved
center, inverse and contraction matrix: if
\(b=\sup_{a\in A_0}|Yf(z_0,a)|_\infty\) and
\(\|I-Yf_z\|_\infty\le q<1\) on the original box, then
\(\|z_*(a)-z_0\|_\infty\le b/(1-q)\) throughout \(A_0\).
Intersect this bound with the original radius. This is a consequence
of the existing validated self-map, not a new root search.

The implementation may tighten a resulting rectangular enclosure
\(Z\) further. With its center \(m\), the same original inverse
\(Y\) gives the interval image
\[
 z_*(a)\in m-Yf(m,A_0)
       +\{I-Yf_z(Z,A_0)\}(Z-m).
\tag{13}
\]
Intersecting (13) with \(Z\) preserves the already proved root,
by the integral mean-value identity on the convex rectangle. No
existence test at a new proposed center is being substituted for the
original self-map. Five such interval-image intersections are used
for a whole parameter cell, and twelve for its midpoint. The
responses (11) use the same inverse and an eight-term Neumann
enclosure with the rigorous remaining geometric-series tail.

The driver is
[certify_mixed_terminal_three_mixed_faces.py](../experiments/certify_mixed_terminal_three_mixed_faces.py).
It first reconstructs all four old trees in their original right-first
LIFO order, including all 233 excluded boxes. The two own-three
families give exactly 3,347 reference leaves and 26,776 ordered jobs,
one for each leaf and face. The original trees and witnesses are
immutable. Within one such leaf, an unsuccessful source upper bound
may split a reference parameter rectangle at an exact rational
midpoint. The selected axis is recorded, so replay reconstructs the
literal partition rather than guessing the refinement order. Boxes
are omitted only when their exact minimum squared normalized radius
is greater than one. There is no target grid and no new complex-root
search. Target-coordinate optimization only proposes a rational
trial for (5)--(7).

An author attempt has explicit caps of at most 600,000 additional
tree nodes, 600 seconds of the numerical author loop, and added
depth at most 45 (the default is 20). No automatic budget enlargement
or restart is performed. The active box remains on the pending
frontier throughout fallible arithmetic. A signal-masked commit
either records its accepted leaf or replaces it by its two children;
checkpoint publication is atomic. An arithmetic or inherited-input
failure stops the attempt with that box unresolved, rather than
accepting it or silently changing the original root data.

Each resume reads an immutable prior incomplete record and writes a
distinct output path. It checks proof, driver, complete input-tree
and inherited dependency hashes, reconstructs every recorded prefix,
validates every saved rational target against its exact face box,
and verifies the exact pending frontier. Accepted prefixes and their
targets are retained unchanged. The author does not repeat their
arithmetic. A final saved replay does repeat every original root
enclosure and every accepted source inequality, using the exact stored
partition and targets with no root proposals, target proposals or
subdivision. Both modes recheck all bound files before publishing
their final result. A partial attempt remains explicitly incomplete;
only an exhaustive author record and its successful saved replay
establish (12) for all families. The calculation has not yet been run.

The earlier narrower design, with \(I_t=[.20,.45]\) and
\(\mu=17/100\), was reviewed but never executed. Its proof and
driver are preserved in the
[pre-author archive](../repro/diagnostics/2026-11-05-terminal-three-narrow-preauthor/manifest.json).
The current design uses the analytically enlarged rectangle and its
weaker common curvature throughout; no narrow-face acceptance is
imported into this new scope.

A complete pass would control exactly the mixed zero-mode faces
listed in (1), including their inward half-grid perturbations by
the uniform continuity estimate already proved in the zero-mode note.
One-index and two-index aliases, the remaining real triangular
complement, and the full coherent terminal polynomial would still
need their own arguments.

