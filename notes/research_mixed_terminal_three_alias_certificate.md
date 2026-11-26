# A certificate design for the terminal three alias currents

Research design, 5 November 2026. This note gives an exact validation rule
for eight single-alias families and four double-alias families of the original
two-index terminal type-three source. No numerical author or replay has
been run for this design. A complete pass would supply the remaining
current comparisons for the central rectangular sub-sum. It would not
bound the rest of the original physical triangle.

The phase, original factorial interpolation and regular product are those of
[the joint zero-mode theorem](research_mixed_terminal_three_joint_zero_mode.md).
The exact current reduction and conditional rectangular packet are proved in
[the twelve-family alias reduction](research_mixed_terminal_three_alias_reduction.md).
The implementation is a separate adaptation of
[the completed mixed-face rule](research_mixed_terminal_three_mixed_face_certificate.md);
its proof, driver, author and saved replay remain unchanged and are
bound as inputs.

## 1. The twelve literal families

Put
\[
 I_a=[.22,.45],\qquad I_t=[.15,.50],\qquad I_u=[.10,.40],
 \quad h_0=3/25,\quad \kappa=1/2500000 .
 \tag{1}
\]
For a reference \(a_*=A+iH\) in either full original endpoint input
disk, let \((e_*,t_*,u_*)\) be its original own-three endpoint root.
Write
\[
 P(a_*)=\mathcal T(a_*;t_*,u_*),\qquad
 p(a_*)=P'(a_*).
 \tag{2}
\]
These are original logarithmic equalities from
[the critical-curve theorem](research_mixed_terminal_three_critical_curve.md).
All root enclosures used below satisfy the full image rectangles from
[the endpoint extraction](research_mixed_open_word_endpoint_rectangles.md).
No root at a new target is proposed or required.

For all twelve alias families all three real coordinates are free:
\[
 a=y+iH,\quad t=x+i h_t,\quad u=z+i h_u,\qquad
 (y,x,z)\in I_a\times I_t\times I_u,
 \tag{3}
\]
where the eight single-alias height pairs are
\[
 (\pm h_0,0),\quad(\pm h_0,\Im u_*),\quad
 (0,\pm h_0),\quad(\Im t_*,\pm h_0).
 \tag{4}
\]
The other index in each pair is a constant-mode current and has
height zero or its actual reference height. Only the aliased index
contributes a frequency penalty:
\[
             L_{\rm single}=2\pi h_0=6\pi/25 .
 \tag{5}
\]
The four double aliases have independent signs and penalty
\[
 (h_t,h_u)=(\pm h_0,\pm h_0),\qquad
                 L_{\rm double}=4\pi h_0=12\pi/25 .
\tag{6}
\]
Every real target endpoint is included. These families omit no
combination of alias signs, and do not add an alias penalty to an
unaliased retained reference height. The zero-height endpoints of
vertical alias sides are supplied by the already completed
mixed-face and corner comparisons, as explained in Section 4.

For any of these families define the unallocated deficit
\[
 G(a_*;X)=
 \Re\mathcal T(y+iH;t,u)-L-\Re P(a_*)
       -\Re p(a_*)(y-A)+\kappa(y-A)^2.
 \tag{7}
\]
The intended strict bound is \(G<-1/2000\).
With the external type-four halfweight, the allocated deficit is
no larger: its difference from (7) is
\[
 -\tfrac12\{\Re g(y+iH)-\Re g(A+iH)
                         -\Re g'(A+iH)(y-A)\}\le0 .
 \tag{8}
\]
This follows from horizontal convexity of \(\Re g\) on \(I_a\).
The actual finite Fourier allocation still uses the actual negative
type-four reference height. The auxiliary positive-height part of
the full input disk does not authorize a different Fourier branch.

## 2. Whole-target and whole-reference bounds

Lemma 1a of the joint theorem proves
\(-\Re\mathcal T''\succ(\pi/100)I_3\) on the entire product
used in (3)--(6), including every height in (4).
The constant penalties (5)--(6) have no derivative. Thus every free-target
principal Hessian of (7) satisfies
\[
 G_{XX}''\preceq-\mu I,\qquad \mu=3/100,
 \tag{9}
\]
since \((157/50)/100-2\kappa>3/100\).

Choose any fixed rational trial \(X^0\) in its exact target box
\(Q=\prod_j[\ell_j,r_j]\). On a whole reference rectangle enclose
\(G(a_*;X^0)\le v\) and
\(\partial_jG(a_*;X^0)\in[g_j^-,g_j^+]\). Put
\[
\begin{split}
 h_j^-&=\operatorname{clip}(g_j^-/\mu,\ell_j-X_j^0,0),\\
 h_j^+&=\operatorname{clip}(g_j^+/\mu,0,r_j-X_j^0),\\
 C_j&=\max\{g_j^-h_j^--\mu(h_j^-)^2/2,\
                  g_j^+h_j^+-\mu(h_j^+)^2/2\}.
\end{split}
\tag{10}
\]
Here \(\operatorname{clip}(s,l,r)=\min(r,\max(l,s))\).
Strong concavity gives the complete target bound
\[
              G(a_*;X)\le v+\sum_j C_j\quad(X\in Q).
 \tag{11}
\]
This includes a constrained maximizer at a target endpoint. The
implementation may return the unconstrained positive quadratic
bound when an interval comparison at the clipping threshold is
undecidable; that only enlarges (11).

For reference variation keep \(X^0\) fixed, and put \(d=y-A\).
Let \(\sigma_t,\sigma_u\in\{0,1\}\) indicate whether the target
retains that index's actual reference height. At most one is one;
both vanish in (6). The aliased heights and \(L\) are constant.
Direct differentiation of (7), with its reference tangent cancelled
before estimating, gives
\[
 \begin{split}
 G_A&=-d\,\Re P''-2\kappa d
       -\sigma_t\Im\mathcal T_t\,\Im t_*'
       -\sigma_u\Im\mathcal T_u\,\Im u_*',\\
 G_H&=\Im(P'-\mathcal T_a)+d\,\Im P''
       -\sigma_t\Im\mathcal T_t\,\Re t_*'
       -\sigma_u\Im\mathcal T_u\,\Re u_*'.
 \end{split}
 \tag{12}
\]
There is no derivative of an optimizing trial. Each retained
actual height contributes its full complex reference response.
The exact reference derivatives are
\[
\begin{split}
 P'&=g'(a_*+t_*)-g'(a_*)+2\pi i t_*,\\
 P''&=g''(a_*+t_*)(1+t_*')-g''(a_*)+2\pi i t_*',\\
 (e_*',t_*',u_*')^T&=-f_z^{-1}f_a .
\end{split}
\tag{13}
\]
The last line is the full original three-variable endpoint system,
not an independent scalar-root replacement.
The free-target gradient consists of
\[
 \Re\mathcal T_a-\Re P'+2\kappa d,\qquad
 \Re\mathcal T_t,\qquad \Re\mathcal T_u,
 \tag{14}
\]
in the order \(y,x,z\) for every family.

A point enclosure at the reference rectangle's center, plus its
two physical halfwidths times whole-rectangle bounds for
\(|G_A|,|G_H|\), gives \(v\). Whole-rectangle target derivatives
give the intervals in (10). These operations prove (11) throughout
the complete reference rectangle, without any boundary principle
or reference sampling.

## 3. Inherited roots, exact coverage and saved replay

The new driver is
[certify_mixed_terminal_three_aliases.py](../experiments/certify_mixed_terminal_three_aliases.py).
It retains the full original right-first input trees and their
3,347 own-three accepted leaves: 1,645 for the type-three external
disk and 1,702 for the type-four disk. Each leaf is paired with all
twelve families, giving exactly 40,164 ordered jobs.

The root validation, tightening and response computation are
unchanged from the reviewed mixed-face driver. The original saved
center, rational inverse \(Y\), positive radius and original
unexponentiated equation first prove the full-leaf root. The same
inverse then yields the \(b/(1-q)\) bound and five interval
Taylor-image intersections on a parameter rectangle, or twelve
at its midpoint. The response uses eight Neumann terms with the
outward remaining geometric-series tail. This preserves the
already identified original root; neither mode proposes a root.

A floating coordinate ascent may propose only a rational target
trial. Acceptance requires its exact membership in its target
box and the strict outward inequality
\[
                       v+\sum_j C_j<-1/2000 .
 \tag{15}
\]
If this fails, author mode may split the reference rectangle at
an exact rational midpoint, recording the axis. It may exclude a
child only when its exact minimum squared normalized radius is
strictly greater than one. A boundary point is never removed by
an uncertain membership test.

Each author attempt is capped at 600,000 additional nodes and
600 seconds of its numerical loop, with added depth at most 45
(default 20). Every unfinished box remains on the exact frontier
throughout fallible arithmetic. A signal-masked commit records
either its accepted leaf or its two children. Checkpoint
publication is atomic; a failed root check or arithmetic error
stops with that box unresolved.

Resumes read an immutable incomplete input and write a distinct
output. They verify all proof, driver, input and recursive dependency
hashes, all family definitions, every stored target and every tree
prefix/frontier before continuing. They retain accepted prefixes
unchanged. Final saved replay checks every accepted inequality
and original root, follows only stored partitions and rational
targets, and explicitly disables root and target proposals.
It makes no subdivisions. Both modes verify all bound files
again before publication.

The completed mixed-face author and its 320-bit replay are bound
with exact equality of their saved partitions and targets. Their
acceptances are not substituted for any of the twelve new families.
The earlier root record/replay, exact endpoint-image extraction,
joint Hessian proof and both scalar constant records are also
bound. No numerical run has yet been performed for this new rule.

## 4. Source consequence and its limit

The alias penalties in (5)--(6) are those of the original marked
residue kernels, not weights imposed on a different interpolant.
Write each one-index residue operation as its real constant-mode
integral \(I\) plus its alias remainder \(E\). Besides
\(I_t\otimes I_u\), the exact product contains
\(E_t\otimes I_u\), \(I_t\otimes E_u\), and
\(E_t\otimes E_u\).

In \(E_t\otimes I_u\), first deform the unaliased \(I_u\)
to its actual horizontal segment and its two vertical joins.
This is permitted by the original holomorphic interpolation on
the full product. An \(E_t\) horizontal segment has height
\(\pm h_0\). Height convexity in the unaliased \(u\) joins
reduces to heights zero and \(\Im u_*\), precisely the first
four families in (4).

An \(E_t\) vertical side is at a real \(t\)-cut. On each of
its upper and lower halves the rate minus the penalty
\(2\pi|\Im t|\) is convex in \(\Im t\), since the penalty
is linear there. Its endpoints are the same horizontal alias
families or height-zero \(t\). If \(u\) is on its shifted
horizontal segment, the latter is a completed flattened-\(t\)
face. If \(u\) is on a vertical join, convexity in its height
reduces further to that completed face or a completed real-real
corner. Thus no raw real \(t\)-cut with an independently free
unshifted \(u\) must be estimated.

Interchanging the two indices proves the same reduction for
\(I_t\otimes E_u\), giving the other four families in (4).
For \(E_t\otimes E_u\), the two horizontal segments give (6).
On a vertical side, endpoint convexity reduces to a double alias
or a single alias with the other height zero. If both sides are
vertical and both heights become zero, both real coordinates
are cuts, so the endpoint is a completed corner. These cases
exhaust the product currents with their exact original penalties.
No cancellation between different currents is used.

Consequently a complete author and saved replay satisfying (15) would bound
these alias currents below the same original supporting plane.
The [completed zero-mode theorem](research_mixed_terminal_three_zero_mode_completion.md)
supplies both the needed flattened faces/corners and the nonzero
coefficient for the entire constant-mode rectangle at the actual
reference. It also controls independent horizontal targets by
the same plane.
The exact alias reduction retains \(18+18+36=72\) deformed
current pieces; their finite multiplicity is paid only once.
Small fixed ordinary-color perturbations, inward half-grid cut
changes and fixed ordinary derivatives use one common arbitrarily
small tolerance through the inherited holomorphic symbols.

This is a design for a complete central rectangular packet.
It does not assert that (15) holds before the exhaustive checks,
does not replace the original \(+i\pi u\) lift, and does not control
the surviving real triangular complement outside
\(I_t\times I_u\).
