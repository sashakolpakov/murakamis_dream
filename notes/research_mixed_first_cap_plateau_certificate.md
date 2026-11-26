# A saved-root certificate for the four first-cap plateau currents

Research design, 5 November 2026. This note and its new driver specify
the remaining two real-cut and two horizontal-alias comparisons for
both first-cap types on the full outgoing plateau. All original
endpoint maps and their saved root witnesses are reused. No new
complex-root proposal is allowed. No author run or saved replay has
yet been executed; the sign remains unproved until both complete.
The scope is every endpoint of a word of length at least two, with
either neighboring type. The separate one-vertex roots are excluded.

## 1. Four complete phase families

Use the allocated original phase \(\Xi_\alpha(e,z)\), original
endpoint action \(S(e)\), and quadratic supporting plane from
[the full-plateau phase deduction](research_mixed_first_cap_plateau_phase.md).
Put
\[
 I_y=[11/50,9/20],\qquad I_e=[27/100,49/100],\qquad
 \kappa=1/2500000,\quad\mu=3/200,\quad\delta=1/20000.
 \tag{1}
\]
For an original external input \(b=\xi+i\eta\) in one of the
two original typed disks, let its endpoint map of own type
\(3+\alpha\) be \((e_*(b),z_*(b),u_*(b))\).
The outgoing reference is \(z_*(b)\), the **second** output of
that map; it is not the external input \(b\).
Write \(z_*=A+iH\), \(d=y-A\),
\(L(z)=\mathcal T_\alpha(z,-2)-\alpha g(z)/2\), and
\(p=L'(z_*)\).

The four families, including their complete target sets, are
\[
\begin{array}{c|c|c|c}
 \text{family}&e&z&\text{penalty}\\ \hline
 \text{left cut}&.27&y+iH&0\\
 \text{right cut}&.49&y+iH&0\\
 \text{lower alias}&x-.055i&y+iH&.11\pi\\
 \text{upper alias}&x+.04i&y+iH&.08\pi
\end{array}
\quad y\in I_y,\quad x\in I_e.
 \tag{2}
\]
Define their fixed-reference deficits by
\[
 G(b;X)=\Re\Xi_\alpha(e,z)-\Re L(z_*)
                    -\Re p\,d+\kappa d^2-\mathrm{penalty}.
 \tag{3}
\]
The cut target \(X\) is \((y)\); the alias target is \((y,x)\).
Every comparison is at the actual outgoing height \(H\).
The exact image extraction makes the own-four height negative
throughout the two entire map families. Thus its allocated outgoing
halfweight is the proved unselected physical one, even when the
external input disk has auxiliary positive heights.

The proposed strict acceptance is \(G<-\delta\) for all the
targets in (2), over all four complete endpoint-map domains. It is
a full outgoing target comparison, not a theorem on a grid of targets
or a collection of words. A complete pass gives exactly equation (14)
of the phase deduction. Its joint zero-mode bound, full real-tail
reduction and literal endpoint budget then supply the whole first-cap
upper plane with one prescribed finite-source tolerance.

## 2. Eliminate each target box by strict concavity

The proved joint Hessian floor \(\pi/200\) implies
\[
                  G_{XX}''\preceq-\mu I,
 \qquad \pi/200-2\kappa>3/200.
 \tag{4}
\]
Take any rational trial \(X^0\) in its target box. Suppose a whole
reference cell gives \(G(b;X^0)\le v\) and
\(\partial_jG(b;X^0)\in[g_j^-,g_j^+]\).
For a coordinate interval \([l_j,r_j]\), put
\[
\begin{split}
 h_j^-&=\operatorname{clip}(g_j^-/\mu,l_j-X_j^0,0),\\
 h_j^+&=\operatorname{clip}(g_j^+/\mu,0,r_j-X_j^0),\\
 C_j&=\max\{g_j^-h_j^--\mu(h_j^-)^2/2,
                 g_j^+h_j^+-\mu(h_j^+)^2/2\}.
\end{split}
 \tag{5}
\]
Strong concavity proves the whole-target upper
\[
                       G(b;X)\le v+\sum_j C_j.
 \tag{6}
\]
It includes boundary maxima and clipped transitions. The driver may
use floating coordinate ascent only to choose a rational trial.
Every acceptance uses (6) with outward arithmetic; no proposed
target value or proposed target root establishes an inequality.

The target endpoint coordinate is evaluated by the explicit canonical
formula
\[
 u_c(e)=\frac1\pi\arctan\frac{i+\sqrt{1-2e^{2\pi ie}}}{2}.
 \tag{7}
\]
The complete endpoint-rectangle theorem fixes its branch and original
zero logarithmic lift throughout the target rectangle. This is an
evaluation of an already proved algebraic branch, not a new root solve.

## 3. Canceled reference derivatives without dividing by the response

Write \(e'=de_*/db\), \(z'=dz_*/db\). At the original reference,
\[
\begin{split}
 p&=J'(e_*+z_*)-J'(z_*)-i\pi e_*-\tfrac\alpha2g'(z_*),\\
 p_b&=\pi\cot\pi(e_*+z_*)(e'+z')
       -\pi\cot\pi z_*\,z'-i\pi e'
       -\tfrac\alpha2 g''(z_*)z'.
\end{split}
 \tag{8}
\]
The reference value itself uses its saved original auxiliary root:
\(L(z_*)=F(e_*,u_*)+J(e_*+z_*)-J(z_*)-i\pi e_*z_*
-\alpha g(e_*)-\alpha g(z_*)/2\).
Its private and auxiliary marginals vanish. Differentiating (3)
at a **fixed** rational target, with \(\Xi_z\) evaluated at
that target, gives
\[
\begin{split}
 G_\xi&=\Im(p-\Xi_z)\Im z'-d\Re p_b
                                      -2\kappa d\Re z',\\
 G_\eta&=\Im(p-\Xi_z)\Re z'+d\Im p_b
                                      +2\kappa d\Im z'.
\end{split}
 \tag{9}
\]
These formulas differentiate the original external input, not the
outgoing coordinate as an independent reference. In particular there
is no division by \(z'\), and no second root response is required.
The target derivatives for (5) are
\[
 G_y=\Re\Xi_z-\Re p+2\kappa d,\qquad
                  G_x=\Re\Xi_e\quad\text{on aliases}.
 \tag{10}
\]
The fixed alias penalty has no reference derivative.

At a reference-cell midpoint, evaluate (3) on its validated root
enclosure. Add the two physical reference halfwidths times whole-cell
upper bounds for \(|G_\xi|\) and \(|G_\eta|\). This yields
\(v\) in (6), retaining the canceled forces in (9). All target
gradient bounds use the same whole cell. There is no derivative of
an optimizing target or an unproved exchange of optimization and
differentiation.

## 4. Original witnesses and complete reference coverage

The driver
[certify_mixed_first_cap_plateau.py](../experiments/certify_mixed_first_cap_plateau.py)
reconstructs the original four endpoint trees in their exact
right-first order. It retains both own flags in every root equation,
Jacobian and self-map test. The four families have respectively
1,645, 1,702, 1,002 and 909 original leaves, totaling 5,258.
All 10,978 original tree nodes and all 233 excluded boxes are checked
structurally; exclusion requires the original strict outside-disk test.
Four currents per leaf give exactly 21,032 jobs.

Each original witness first passes its unexponentiated interval
root test and exact typed output-rectangle inclusions. Let its saved
center and inverse be \(z_0,Y\), and let
\(q=\|I-Yf_z\|_\infty<1\) on the original box. For a parameter
subcell or its midpoint the inherited estimate
\(\|Yf(z_0,b)\|_\infty/(1-q)\) may tighten the old radius.
Five interval Taylor-image intersections are used on the parameter
cell and twelve at its midpoint. They contain the already proved
root and never change its branch. The response
\((e',z',u')=-f_z^{-1}f_b\) is enclosed by eight Neumann terms
with the outward geometric-series tail, as in the completed
terminal mixed-face certificate. No complex-root proposal is allowed.

The script accepts a leaf only when the whole-target outward upper
in (6) is strictly less than \(-1/20000\). Failure may subdivide
the reference rectangle, but never the target box; a failed original
root or nonfinite bound remains unresolved. The pending active box
is retained during all fallible arithmetic. Signal-masked commits
and atomic checkpoint replacement preserve its exact frontier.

Each author attempt has at most 600,000 additional nodes and 600
seconds in its numerical loop, with additional depth at most 45
(default 20). Resuming requires an immutable input and a different
output path. It verifies current hashes, family metadata, every
accepted prefix and trial, and the exact pending frontier. Accepted
prefix arithmetic is not rerun in author mode.

The final saved replay revalidates every original root and every
accepted current with its saved rational target. Both complex-root
and target proposals are forbidden, and no refinement is permitted.
All input, proof and script hashes are rechecked before publication.
The original root author/replay, exact endpoint-image extraction,
complete endpoint packet and complete cap source records are bound,
including their existing saved replays. This new certificate makes
no claim about the separate one-vertex source.

There is presently no numerical result for this design. Only a complete
author and an independent saved replay can establish its four signs.
The analytic phase/tail deductions remain valid independently of
whether this particular fixed contour achieves those signs.
