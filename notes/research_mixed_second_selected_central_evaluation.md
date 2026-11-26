# Outward evaluation of the second-selection central budget

Research evaluation specification, 6 November 2026. This note proves
an outward evaluation procedure for the scalar conjugates in the
[central budget](research_mixed_second_selected_central_budget.md).
It proposes one inherited-box diagnostic after implementation review.
It contains no evaluated majorant, parameter cover, or uniform sign claim.

## 1. One correlated reference and the justified target restrictions

Keep the five original coordinates
\((a,u,z,v,b)=(r_1,s_2^*,r_2,s_3^*,r_3)\), first flag
\(\alpha\), and third flag \(\beta\). The second flag is one.
The [reference-curve deduction](research_mixed_second_selected_reference_curve.md)
expresses all five coordinates, the endpoint private leg and the next
external leg as rational functions of one endpoint parameter \(\xi\),
with \(W=e^{2\pi i\xi}\). Both transfers, the original logarithmic
lifts and the necessary coordinate/suffix conditions must be retained.
Five independent reference rectangles are not an alternative input.

Set \(H=1/100\) for the proposed diagnostic. The
[horizontal-concavity and barrier theorem](research_mixed_second_selected_horizontal_concavity.md)
proves that both branch maxima are unchanged on the tighter product
\[
 K'=P\times[.22,.5]\times P\times[q_\beta,.5]\times P,
 \qquad P=[.22,.45],\quad q_0=.2,\quad q_1=.22.
 \tag{1}
\]
The actual real center belongs strictly to every interval. The node
and edge conjugates in equations (23) and (29) of the central budget
may therefore be restricted to these new intervals. Their proofs
apply verbatim, and every restricted scalar conjugate is no larger
than its original counterpart. The two left edge-sum intervals now
start at \(.44\); the two right intervals start at \(.42\)
for \(\beta=0\), and \(.44\) for \(\beta=1\). All four
edge upper endpoints remain \(.95\).

The intended reference evaluator first propagates the original rational
shapes, then decodes the original coordinate logarithms. A forbidden
denominator, uncertain logarithm branch, nonfinite image, or unresolved
arithmetic comparison is inconclusive. Exclusion is permitted only by
a strict incompatibility with a proved necessary condition. For an
unknown next type, both typed alternatives must be excluded before
discarding the box. Equality and boundary-crossing boxes remain.
In particular the proposed stronger condition \(\Im z\le-.02\)
in the reference note is still open and is not a filter.

Necessary coordinate intersections may tighten pointwise enclosures.
Every value evaluated below is a pointwise function of that same
reference; no parameter derivative is taken through a clipped image.
If a future centered parameter-response method is added, it will
require separate bounds on the full untruncated rational image.

## 2. A branch-safe scalar conjugate calculation

Let a real scalar potential be \(m g_h(t)\), where
\(g_h(t)=\Re g(t+ih)\), \(m>0\), and the node target interval
is \([l,r]\subset(0,1/2]\). Its actual center is \(t_*\).
For a force \(p\), define
\[
 N_h(t)=1+\rho^2-2\rho\cos(2\pi t),\quad
 \rho=e^{2\pi h},\qquad
 C_m=\frac{1+\rho^2-N_h(t_*)e^{2p/m}}{2\rho}.
 \tag{2}
\]
All of \(p,h,t_*\) depend on the same reference. They may be
enclosed by outward intervals, but are not chosen as independent
optimizers. Define the continuous clipped angle function
\[
 T(c)=\begin{cases}
 1/2,&c\le-1,\\
 \displaystyle\frac1\pi\arctan\sqrt{\frac{1-c}{1+c}},&-1<c<1,\\
 0,&c\ge1.
 \end{cases}
 \tag{3}
\]
This is the clipped value of \(\arccos(c)/(2\pi)\),
with its two exterior regimes defined before any inverse cosine
could be called. The unique node maximizer is
\[
                       t_N=\operatorname{clip}(T(C_m),l,r).
 \tag{4}
\]
This formula remains valid when the formal cosine target lies outside
\([-1,1]\). It then selects the correct interval endpoint, rather
than treating the scalar problem as infeasible.

For the edge potential \(-g_h(t)\) on \([L,U]\), with
\(L<1/2<U=.95\), put
\[
 C_E=\frac{1+\rho^2-N_h(t_*)e^{-2p}}{2\rho},\qquad
 t_E=\operatorname{clip}(1-T(C_E),1/2,U).
 \tag{5}
\]
Its conjugate is the maximum of exactly two candidate values:
\[
 \chi^*(p)=\max\{p(L-t_*)-D_{-g_h}(L-t_*),
                         \ p(t_E-t_*)-D_{-g_h}(t_E-t_*)\}.
 \tag{6}
\]
Indeed its objective is convex on \([L,1/2]\), so that part
has its maximum at an endpoint. It is concave on \([1/2,U]\),
whose clipped critical point is (5). The second candidate includes
\(1/2\) when necessary. Thus (6) includes every possible maximum
without presuming that the edge Bregman cost is nonnegative.

For a general scalar potential \(m g_h\), allowing \(m=-1\)
for an edge, evaluate the candidate objective by the original formula
\[
 \mathcal A_m(p,t;t_*,h)=p(t-t_*)
 -m\{g_h(t)-g_h(t_*)-\log|1-e^{-2\pi i(t_*+ih)}|(t-t_*)\}.
 \tag{7}
\]
The original additive constant and derivative lift are retained.
At a node its conjugate is \(\mathcal A_m(p,t_N;t_*,h)\);
at an edge use \(m=-1\) in both candidates (6).

## 3. Why the interval version encloses every clipped branch

Suppose a whole reference box gives a finite outward interval
\([c_-,c_+]\) for either cosine expression in (2) or (5).
First clip its exact directed rational endpoints to \([-1,1]\).
Since \(T\) is decreasing,
\[
                T([c_-,c_+])
          \subseteq[T(c_+),T(c_-)]
 \tag{8}
\]
with directed enclosures at the two endpoints. Endpoints \(-1,1\)
have the exact values \(1/2,0\). For a rational interior endpoint
\(q\), form the positive rational number
\((1-q)/(1+q)\) before converting it to a ball. Its square root,
arctangent and division by a positive enclosure of \(\pi\)
give an outward endpoint value from (3). This avoids a rounded
inverse-cosine input accidentally crossing its branch cut. A failed
positivity or finiteness check returns inconclusive; it does not
delete the reference box.

The real interval clipping maps in (4)--(5) are monotone. Clip the
directed interval endpoints again to the indicated target interval,
and construct a containing ball. Even when a parameter box crosses
several endpoint/critical regimes, the resulting interval contains
the maximizing target for every admitted reference in that box.
There is no requirement that the whole box have a single regime.

Evaluate (7) on that entire containing interval, using outward
operations and the proved
[centered original primitive](research_mixed_centered_primitive_enclosure.md).
All node and edge target real parts remain strictly between zero
and one; their heights are fixed finite compact ranges. Hence each
primitive is evaluated on its original regular strip. The exact
shape at the center may be used for
\(N_h(t_*)=|1-e^{-2\pi i(t_*+ih)}|^2\) and its logarithmic
derivative; it must be the same height as the potential, including
height \(H\) for the selected node and the shifted incident edges.

The interval objective may lose correlation between the candidate
and its parameters, but its upper endpoint still contains the true
candidate value. Taking the larger directed upper endpoint for the
two edge candidates gives a valid upper bound for (6). Do not take
the smaller candidate merely because one possible stationary branch
is inconclusive. An inconclusive required candidate makes this
conjugate evaluation inconclusive.

Two exact zero-force simplifications are useful. A node whose force
is identically zero has conjugate zero, because its convex cost has
center in the target interval. A force interval merely containing
zero does not justify that replacement. For an edge whose actual
center satisfies \(1/2\le t_*\le U\),
\[
                    \chi^*(0)=\max\{0,-D_{-g_h}(L-t_*)\}.
 \tag{9}
\]
Its upper-branch critical point is exactly the actual center, with
value zero. In the reference family the outer sums \(a_*+u_*\)
and \(v_*+b_*\) both lie above one half and below \(.77\),
so (9) applies to the two zero-force outer edges in equation (29)
of the budget. This preserves their possible positive left-endpoint
cost; it does not set them to zero. The inner own-four sum is not
assumed above one half in the pattern \((3,4,3)\).

These arguments prove the outward evaluation rule independently of
the widths or signs of its eventual numerical outputs.

## 4. A finite trial family for both displayed budgets

Use the exact data \(A,B,C,\ell,G_H,D_\nu,T_\nu\)
from equations (6)--(9) of the central budget, with its exact vertical
cost. Keep the coarse vertical estimate separately as a diagnostic
component; do not replace the actual height by an independent floor.
Let
\[
 \Theta=\{0,1/4,1/2,3/4,1\},\qquad
 \mathcal R=\{0,1/4,1/2\},\qquad
 R_{\nu,\theta}=3C-\ell-(1-\theta)A-(1-\nu)G_H.
 \tag{10}
\]
For each of the fifteen predetermined choices \((\theta,\rho)\),
choose the four flows
\[
 \begin{split}
 w_1&=\rho(1-\theta)A,&w_2&=\theta A,\\
 w_3&=D_\nu-\theta A,&w_4&=\rho R_{\nu,\theta}.
 \end{split}
 \tag{11}
\]
Their node forces, in the order \((a,u,z,v,b)\), are exactly
\[
 (-\rho(1-\theta)A,\ (1-\rho)(1-\theta)A,\ 0,
                 (1-\rho)R_{\nu,\theta},\ -\rho R_{\nu,\theta}).
 \tag{12}
\]
In particular the selected-node force is identically zero; compute
that cancellation symbolically. The five trials with \(\rho=0\)
are precisely equation (29). The ten others test the stronger
four-flow bound (23), retaining additional outer-pair cost.
No sign restriction on any flow or on \(R_{\nu,\theta}\) is
required, and no numerical optimizer chooses these coefficients.

For each trial add its conjugate upper bounds to the exact-trial
upper bound \(T_\nu\). A finite minimum of valid upper bounds
is valid. The factorial and forced alternatives are tested separately;
both must be negative for a common central comparison. Report strict
negativity and, separately, the candidate margin \(1/2000\).
All decisions use exact rational directed endpoints, not printed
ball strings. Such a comparison would address only the main/main
term of the finite-source reduction.

## 5. One proposed inherited-reference diagnostic

After the reference and barrier proofs are frozen and the implementation
has passed independent static review, one prescribed diagnostic is a
useful width and implementation check. It must not begin a cover.

Use \(\alpha=1\), the original next-four auxiliary root rectangle,
and the saved complete central record
[adaptive attempt02](../repro/results/research-mixed-next-four-adaptive-budget-attempt02.json).
Select the lexicographically first accepted leaf of maximal accepted
depth, exactly as in the earlier one-box next-four diagnostics. Its
address and exact rectangle are
\[
 \begin{split}
 a_{18}&=001111101111010111,\\
 \xi&\in[115337/512000,57677/256000]
                   +i[8919/256000,279/8000].
 \end{split}
 \tag{13}
\]
Its selection uses saved metadata and exact dyadic reconstruction
only. It is not a certified word and no word realization is claimed.
The second-reference transfer now imposes the actual ordinary roles
required at length at least four.

Evaluate both \(\beta=0,1\) on this same box, each with its
own necessary reference filters. An excluded or inconclusive family
is reported as such; there is no alternate box. For each retained
family evaluate \(\nu=0,1\) with the fifteen trials (11), at
160-bit precision. Thus there are at most sixty predetermined trial
budgets on one auxiliary box, with no subdivision, precision retry,
continuation or sweep. The first-type-three chart remains unevaluated
by this diagnostic even though the formulas cover it.

The record must retain the following data:

* The exact inherited address and box, both type flags, every necessary
  exclusion or inconclusive reason, and the shared reference coordinates
  and shapes including the admitted next-external-type alternatives.
* The exact vertical cost, its separate coarse upper bound, both trial
  values \(T_\nu\), the logarithmic increments and forced gradient
  adjustment, with rational directed endpoints.
* Every trial flow and node force, each node conjugate, both edge
  candidate values or the justified exact-zero simplification, cosine
  intervals before clipping, candidate target enclosures, and final
  trial upper endpoints. Uncertain clipping regimes remain visible.
* The best upper endpoint for each Fourier alternative, strict-zero
  and candidate-margin flags, exact call counts, and all frozen input
  hashes checked before import and again after the call.

The frozen old reference/phase helpers may provide reviewed arithmetic,
but no earlier `inspect`, source main program, root solver, cover or
diagnostic main program is called. The new code and result use new
paths. The implementation must bind this specification, the central,
reference and barrier proofs, the original-primitive provider and its
proof, the inherited metadata record, and their necessary transitive
inputs. An unresolved branch or arithmetic failure is diagnostic
inconclusiveness, never a word exclusion or a successful budget.

A successful prescribed box would justify considering a separately
reviewed full-domain scalar plan; it would not establish a uniform
sign. A failed sufficient upper bound would first be analyzed through
the saved vertical, horizontal and edge-candidate components. It is
not an actual-source counterexample and does not authorize automatic
refinement. No diagnostic or parameter cover is executed by this note.
