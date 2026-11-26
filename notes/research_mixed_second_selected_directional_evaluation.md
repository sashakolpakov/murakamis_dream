# Evaluating the directional central estimate

Research implementation specification, 6 November 2026.
The [directional estimate](research_mixed_second_selected_directional_budget.md)
reduces the two central rate comparisons to three scalar gains.
This note describes their outward evaluation from a previously enclosed
reference. It does not select a new reference, solve critical equations,
or assert that either comparison is negative.

## 1. Input and retained dependence

An input consists of the seven original shapes and coordinates
\((e,a,u,z,v,b,c)\), enclosed on one common endpoint-parameter cell,
with first flag one and outgoing flag \(\beta\in\{0,1\}\).
It must come from the original two-transfer reference map, with its
regularity, logarithmic branches and necessary geometric conditions.
A containing coordinate rectangle may have been intersected with those
proved conditions. The derivatives of the reference map are not used here.

The evaluator reconstructs the exact trial quantities
\(A,B,C,\ell,D_\nu,T_\nu\) from the central-budget formulas at
\(H=1/100\). Every operation uses outward balls. The vertical change is
evaluated with the original primitive, including its asymmetric chirp;
it is not replaced by the separate coarse height estimate.
The input intervals may lose correlations, but still contain the values
at every actual reference in the cell.
In particular the radial multiplier is evaluated as
\(\lambda=\exp(2\pi(H-\Im z_*))\), using the exact identity
\(|Z|=\exp(2\pi\Im z_*)\). This avoids dividing by an unnecessarily
wide radial enclosure of the same complex shape.

## 2. The three upper bounds

For the left-index gain, use the node-conjugate evaluator in
[the original scalar specification](research_mixed_second_selected_central_evaluation.md),
with coefficient \(m=1\), force \(A\), the actual center \(u_{*,R}\),
and target interval \([.22,.5]\).
This gives precisely \(\mathcal U(A)\): the directional theorem proves
\(A>0\), so the maximizer cannot lie below the actual center.
The implementation requires its interval enclosure to certify this sign;
an unresolved sign is inconclusive.

For the right-index gain, use the valid quadratic lower curvatures
\[
 \mu_0=2\pi/5,\qquad \mu_1=71\pi/80.
\]
Let \(d=\ell-B>0\), \(q_0=.2,\ q_1=.22\). If the saved enclosures give
upper bounds \(d_+\) and \(v_+\), and a positive rational lower bound
\(\underline\mu_\beta\le\mu_\beta\), then
\[
 \mathcal R_\beta(d)\le
 d_+t-\frac{\underline\mu_\beta}{2}t^2,\qquad
 t=\min\{d_+/\underline\mu_\beta,\ v_+-q_\beta\}.
\]
The right side is computed in exact rational arithmetic. Enlarging the
displacement interval, increasing the nonnegative force and decreasing
the curvature each preserves this upper bound. This uses the quadratic
replacement for type four, not an unvalidated solution of its scalar
critical equation. Again an unresolved positivity test for \(d\) is
inconclusive.

For the selected-coordinate gain use the same node-conjugate evaluator,
with coefficient \(m=1+\nu\), force \(D_\nu\), actual real center
\(\Re z_*\), and final height \(H\). Its target interval is
\[
 [.22,.45]\quad(\nu=1),\qquad [.4,.45]\quad(\nu=0).
\]
The forced interval does not contain the actual center. The routine must
evaluate its signed objective at the clipped maximizing target; it must
not add the unavailable center or replace a negative gain by zero.
The original node routine has this behavior when its exact-zero
shortcut is disabled.

Each branch is bounded by the outward sum
\[
 T_\nu+\mathcal U(A)+\overline{\mathcal R_\beta}(d)
                         +\mathcal Z_\nu(D_\nu).
\]
Acceptance requires both upper endpoints to be strictly negative. The
smaller of their two exact negatives is recorded as the proved cell
margin; comparison with the candidate margin \(1/2000\) is recorded
separately. On a completed finite cover the minimum of all positive
cell margins supplies a uniform margin. A prescribed larger margin is
not a prerequisite for this deduction. The branch-domain reduction justifies this maximum of
two restricted estimates; taking a minimum of the two branches would
not be valid.

## 3. Implementation and interpretation

The [evaluation module](../experiments/evaluate_mixed_second_selected_directional_budget.py)
performs no work on import. Its caller supplies the reviewed primitive
and node-conjugate provider after checking their frozen inputs. It records
the raw logarithmic increments, exact vertical cost, each scalar gain,
the rational right-index bound, the target intervals, and the branch
upper endpoints. One reference requires three node-conjugate calls:
one common left-index gain and one selected-coordinate gain per branch.
There is no flow search, nonconvex edge conjugate or parameter derivative.

A positive upper bound is a failure of this sufficient estimate, not a
counterexample to the source inequality. An inconclusive calculation
does not exclude a reference. A successful cell establishes only the
central estimate on that cell; a uniform theorem still requires a
complete covering argument. The outgoing type-three half-row comparison
and the simultaneous-selection problem remain separate.
