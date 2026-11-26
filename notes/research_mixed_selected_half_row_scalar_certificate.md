# A bounded scalar certifier for the remaining half-row profiles

Research construction, 6 November 2026. The new
[driver](../experiments/certify_mixed_selected_half_row_budget.py)
implements the proved upper bounds in
[the half-row reduction](research_mixed_selected_four_three_half_row_majorant.md)
and [its branch-preserving evaluation specification](research_mixed_selected_half_row_evaluation_design.md).
No execution or completed sign theorem is asserted in this note.
Only a complete successful record would establish the conditional
conclusion below.

## 1. Four tested bounds

Keep the actual first-four/next-three references of length at least
three, the original outgoing affine term, and \(H=7/625\).
The four independently tested quantities are
\[
 \mathcal H^+_{0,1},\quad \mathcal H^+_{0,0},\quad
 \mathcal H_{.27,1},\quad \mathcal H_{.27,0}.
 \tag{1}
\]
Here the superscript \(+\) denotes the strengthened private
curvature \(28/5\) from the evaluation specification; the incoming
curvatures remain \(7,33/5\) for the main line and \(69/10,13/2\)
for the real left cut. The first index in each pair is the complete
factorial Fourier alternative and the second the forced alternative.
The original full Fourier factor is retained by taking their maximum.

The candidate common gap is
\[
                              \delta=1/2000.
 \tag{2}
\]
The pointwise right-cut comparison already gives
\(A_R<A_0-1/1250\). Therefore its two half-row comparisons need
not pass their own quadratic majorants: successful main-profile
tests imply those source comparisons directly.

**Conditional conclusion.** If the record covers the entire
auxiliary rectangle by necessary-reference exclusions and accepted
cells on which all four bounds (1) are strictly below \(-\delta\),
then every actual first-four/next-three reference satisfies
\[
 \begin{split}
 A_0(y)+B_R(y,v)+W_\nu(y)
     &<M+\ell_b(v)-1/2000,\\
 A_L(y)+B_R(y,v)+W_\nu(y)
     &<M+\ell_b(v)-1/2000
 \end{split}
 \qquad (y,v\in P,\ \nu=0,1).
 \tag{3}
\]
This follows directly from the scalar upper-bound theorem, with
no new critical point or free-target optimization. The \(A_LB_0\)
comparison remains separate, even if (3) is established.

## 2. Reference coverage and original branches

The auxiliary domain, rational maps, logarithmic coordinates and
necessary filters are exactly those of the already proved
first-four/next-three central scalar reduction:
\[
 \Re u\in[.217,.234],\qquad \Im u\in[.027,.045],
 \qquad U=e^{2\pi iu}.
 \tag{4}
\]
The driver imports the map and interval-enclosure helpers of the
original scalar driver, but never calls its old majorant evaluator.
The necessary coordinate rectangles, reduced disks, two pair-sum
intervals, and next-external \(K_3\cup K_4\) condition are copied
without tightening their domain. Every exclusion is strict.
An unseparated pole or logarithm causes subdivision, not exclusion.
After these tests, each coordinate enclosure is intersected with
its proved containing rectangle. This preserves every actual
reference in that cell and merely improves its enclosing interval.
It does not declare every retained auxiliary point geometric.

The phase primitive is the literal
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},
 \qquad J(w)=g(w)-\frac{i\pi}{2}w(1-w).
 \tag{5}
\]
Before every evaluation the whole argument enclosure must have
\(0<\Re w<1\). Formula (5) is then on the original regular
branch. Any nonfinite result is inconclusive. The reference cap
action uses the auxiliary \(u\) itself in the original explicit
action \(F(e_*,u)\). The only other private coordinate is the
fixed canonical \(u_c(.27)\), from the original square-root and
arctangent formula; its fixed regular-strip bounds are checked
before the cover. There is no root proposal or numerical root solver.

The main relative action cancels the reference cap action before
evaluation. The left-cut relative action is the difference of the
two original cap phases, exactly as in equation (13) of the
evaluation specification. The outgoing half-row maximum uses the
clipped \(\arccos\) formula, with its original reference slope.

## 3. Outward gains, acceptance and stopping

All transcendental operations use outward ball arithmetic. Every
quadratic gain is bounded by the two one-sided rules in the
evaluation specification. The directed slope and displacement
endpoints are converted to exact rational numbers, and the
one-sided maximizing displacement
\[
                       t=\min\{L,\max(0,\beta)/\mu\}
 \tag{6}
\]
and its value are then formed by rational arithmetic. This covers
clipping transitions without a target grid or a proposed optimizer.
Reference correlations are retained through the common box; using
containing slope/displacement intervals can only weaken a bound.

The driver records each of the four upper enclosures, its trial
value, incoming gradient, exact gain and acceptance flag. It also
records the private gradient/gain, outgoing maximizer enclosure,
outgoing value and reference coordinate enclosures. All finite
real endpoints have exact rational serialization, in addition to a
human-readable ball display.

The one authorized exploratory attempt is limited to \(160\)-bit
arithmetic, at most \(4000\) visited cells and depth at most \(20\).
It bisects the two auxiliary coordinates alternately. A leaf is
accepted only when all four enclosures are strictly below (2) with
negative sign. Every inconclusive depth-limit leaf and every
unvisited pending box is retained. A complete proof status requires
that no such leaf or box remains.

The final terminal addresses, including pending boxes, must be
prefix-free and have exact dyadic mass one. Source files and proof
dependencies are hash-bound before and after the attempt. The
output path must be fresh, and this driver has no automatic retry
or budget escalation. A partial cover proves none of (3) uniformly;
an unsuccessful upper bound is not an actual source counterexample.

Even a successful scalar record would settle precisely the two
half-row profiles in (3), plus their already dominated right-cut
and alias counterparts. It would leave the independent cap-left/
ordinary-main comparison and the broader open-source problem.
