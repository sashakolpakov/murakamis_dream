# Optional curvature improvements of the central evaluator

Research specification, 6 November 2026. This adds rigorous upper
bounds to the frozen three-gain evaluator without changing its
arithmetic, reference provider or Fourier domains. It performs no
parameter work on import. No evaluation is authorized by this note.

## 1. Interface and unchanged scope

The new module
[evaluate_mixed_second_selected_curvature_budget.py](../experiments/evaluate_mixed_second_selected_curvature_budget.py)
has three interfaces:

* The evaluation wrapper calls the frozen directional helper exactly
  once, then postprocesses its result.
* The postprocessing interface accepts an already saved result, its
  evaluator and the same reference shapes and coordinates. It reads
  their directed endpoints and makes no helper or primitive call.
* The rational postprocessor accepts these serialized endpoints
  directly and uses only exact fractions.

The caller must bind the new module, this specification, its four
pinned inputs, and the provider of the common-reference enclosures.
The wrapper verifies its four pinned inputs before and after its
single original helper call. The separate postprocessing interfaces
rely on the caller's binding checks.

The original result is retained verbatim. If it does not contain both
finite branch budgets, no extra branch is attempted and the result
stays arithmetically incomplete. A complete pair, whether negative or
positive, may be improved. Thus this wrapper does not justify further
reference refinement driven by a positive sufficient upper bound.

All results retain the original scope: actual stationary references
to which the [directional theorem](research_mixed_second_selected_directional_budget.md)
applies, with \(H=1/100\). A reference provider's retained status
does not prove existence, word realization or geometric feasibility.
The wrapper checks none of these and makes no such claim.
It does not enlarge the caller's reference cover.

## 2. Valid component upper bounds

Write the original branch bound as
\[
                   T_\nu+\mathcal U+\mathcal R_\beta+\mathcal Z_\nu,
                   \qquad \nu=0,1.
 \tag{1}
\]
Every candidate below bounds the indicated same component uniformly
on the supplied reference enclosure. Their minimum is therefore a
valid upper bound; they are not new terms to add to (1).

The original component upper endpoints are always candidates.
The [local-curvature lemma](research_mixed_second_selected_local_curvature_gains.md)
adds the following candidates when their exact rational guards hold:

* If \(5/16<u_{*,R}<63/200\), \(|h_u|<9/200\), and
  \(0<A<33/200\) hold throughout the enclosure, then
  \(\mathcal U\le2691/204800\).
* For \(\beta=0\), if \(1/3<v_{*,R}<3/8\) and
  \(|h_v|<1/50\), then
  \(\mathcal R_0\le\overline d^{\,2}/(2(471/265))\).
* If \(D_1<0\) throughout the enclosure and
  \(.22<x_*<.28\), then
  \(\mathcal Z_1\le\underline D_1^{\,2}/10\).

Every strict condition is checked using the appropriate directed
endpoint. The first and third proofs use only their displayed
one-variable costs, which are identical for both values of \(\beta\);
they therefore also apply when \(\beta=1\).
The forced selected gain is kept exactly as in the frozen result,
including its sign and the target interval \([.4,.45]\). It is
never replaced by its maximum with zero.

## 3. A generic type-three right-index curvature

There is a further rational improvement requiring no cotangent
evaluation. The negative-sign reference shape \(V=e^{-2\pi i v_*}\)
satisfies
\[
 \cot(\pi v_*)=i\frac{1+V}{1-V},\qquad
 \Re\cot(\pi v_*)=
             \frac{-2\Im V}{(1-\Re V)^2+(\Im V)^2}.
 \tag{2}
\]
Suppose its enclosing rectangle is
\([x_-,x_+]+i[y_-,y_+]\), with \(y_+<0\). Put
\[
 Q=\max\{(1-x_-)^2,(1-x_+)^2\}
                      +\max\{y_-^2,y_+^2\},\quad
 q_-=\frac{-2y_+}{Q},\quad
 \delta_-=\max\{1/5,\min(q_-,15/53)\}.
 \tag{3}
\]
Here \(Q>0\), and (2) implies \(\Re\cot(\pi v_*)\ge q_-\).
The original joint directional theorem proves
\(\delta_v=\min(\Re\cot(\pi v_*),15/53)>1/5\).
Consequently \(\delta_v\ge\delta_-\). These bounds refer to the
same original reference and fixed index height.

For \(\beta=0\), let \(\pi_-\) be the existing primitive's lower
endpoint for \(\pi\), and set
\[
 \mu_-=2\pi_-\delta_-,\qquad
 L_+=\overline v_R-1/5,\qquad
 t_0=\min(\overline d/\mu_-,L_+).
 \tag{4}
\]
The implementation checks \(L_+\ge0\); its other factors are
strictly positive. Enlarging the force and displacement range and
lowering the curvature in the original right-index gain gives
\[
               \mathcal R_0\le\overline d\,t_0-\mu_-t_0^2/2.
 \tag{5}
\]
This is an alternative bound for the same right gain. It adds no
additional Hessian cost to the left or selected-coordinate terms.
For \(\beta=1\), the frozen right gain is retained.

## 4. Vertical and final minima

Equation (12) of the
[central-budget proof](research_mixed_second_selected_central_budget.md)
gives
\[
 \mathcal V\le c_\beta(H-\underline h_z)^2,\qquad
                c_0=33/5,\quad c_1=429/70.
 \tag{6}
\]
These constants use \(\pi<22/7\) in the proved stationary
curvature bounds \(21\pi/10\) and \(39\pi/20\).
The implementation additionally checks the entire supplied real
intervals \(u_R,z_R\subseteq[.24,.36]\),
\(v_R\subseteq[.267,.433]\) for \(\beta=0\) or
\([.24,.36]\) for \(\beta=1\), and \(\overline h_z<H\).
The stationary-reference premise remains essential; (6) is not
asserted at arbitrary rational map values or noncritical points.

Take the minimum of (6) and the frozen vertical upper endpoint.
Combine it with the saved \(g_H(x_*)\) upper endpoint for \(\nu=0\),
or subtract \(\pi_-/50\) for \(\nu=1\). The minimum of this
trial bound and the original \(T_\nu\) upper endpoint is valid.
Add that trial minimum and exactly one upper bound for each of
\(\mathcal U,\mathcal R_\beta,\mathcal Z_\nu\).
Finally take the minimum with the original complete branch upper
endpoint. Thus every selected value is a minimum of valid upper
bounds on the same expression; no component is counted twice.

The result records each candidate, its exact rational witness and
the selected index. Its displayed degenerate rational budget
interval encloses the exact chosen upper majorant; it is explicitly
not an enclosure of the underlying phase value.
Acceptance requires both strict upper bounds below zero.
The minimum of their positive deficits is saved, and the
\(1/2000\) candidate comparisons are separate information.
No negative result by itself establishes that its reference
enclosure contains an admissible point.
