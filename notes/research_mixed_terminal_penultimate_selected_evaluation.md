# Fixed saved-vertex test for the penultimate selection

Unexecuted protocol, 6 November 2026. This test changes the scalar
majorant for the shared ordinary index when only the penultimate
retained coordinate is selected. It uses the complete, unchanged
reference projection and the already evaluated force vertices.
No new reference, parameter cell, primitive, cotangent, optimizer,
square root or cubic gain is evaluated.

The full source reduction is supplied separately by the
[penultimate-selection criterion](research_mixed_terminal_penultimate_selected_criterion.md).
Its source and contour conclusions are pinned
before this protocol can be executed. The scalar argument below
does not by itself replace any nonmain source row.

## 1. A rational upper retaining the negative-displacement cubic cost

Retain the original shared-index height \(h_s\), real reference
\(S=\Re s_*\), and target interval \(I=[.22,.5]\). For a case
whose certified coordinate interval satisfies
\[
 .24\le s_-\le S\le s_+\le.36,\qquad |h_s|<.061,
 \tag{1}
\]
put
\[
 m=19(.5-s_+)>0,\qquad D=s_+-.22>0.
 \tag{2}
\]
The [scalar curvature bound](research_mixed_terminal_cubic_cost_and_response_bounds.md),
equations (1)--(2), gives
\(2g_{h_s}''(x)\ge19(.5-x)\) on \([.22,.5]\).
For the exact cost
\[
 \phi_s(x)=2\{g_{h_s}(x)-g_{h_s}(S)-g_{h_s}'(S)(x-S)\},
 \quad
 G_s(q)=\sup_{x\in I}\{q(x-S)-\phi_s(x)\},
 \tag{3}
\]
and actual force \(q=-A\), \(A\ge0\), a maximum may be taken at
\(x\le S\): targets to its right have nonpositive objective, and
the center is allowed with objective zero. Write \(d=S-x\).
Then \(0\le d\le D\), and every point of the segment from \(x\)
to \(S\) has curvature at least \(m\). Hence
\[
 G_s(-A)\le\max_{0\le d\le D}\{Ad-md^2/2\}
 =Q_+(A):=
 \begin{cases}
 A^2/(2m),&0\le A\le mD,\\
 AD-mD^2/2,&A\ge mD.
 \end{cases}
 \tag{4}
\]
Equality at \(A=mD\) is assigned to the first branch in the
fixed implementation; the two formulas agree there.

For artificial endpoints of containing intervals define
\[
                  Q(A)=Q_+(\max(0,A)),\qquad A\in\mathbb R.
 \tag{5}
\]
This function is convex and nondecreasing: it is the supremum
of the affine functions \(Ad-md^2/2\), \(0\le d\le D\).
Equation (4) is used only for actual \(A\ge0\).
No bound \(G_s(-A)\le0\) is asserted at artificial \(A<0\).

The stronger cubic term can be retained with a fixed rational
bracket. Twice integrating the same curvature inequality gives
\[
 \phi_s(S-d)\ge \frac{m d^2}{2}+\frac{19d^3}{6},
 \qquad
 G_s(-A)\le F(A):=
 \sup_{0\le d\le D}\{Ad-md^2/2-19d^3/6\}
 \quad(A\ge0).
 \tag{5a}
\]
Define this same supremum for all real \(A\); it is convex,
nondecreasing, and zero for \(A\le0\). For \(A>0\), put
\[
 d_{\rm hi}=\min(D,A/m),\qquad
 d_{\rm lo}=\min\left(D,\frac{A}{m+19d_{\rm hi}/2}\right),\qquad
 R(A)=Q(A)-\frac{19d_{\rm lo}^3}{6}.
 \tag{5b}
\]
For \(A\le0\) set both displacements and \(R(A)\) to zero.
Then
\[
                 0\le F(A)\le R(A)\le Q(A).
 \tag{5c}
\]
Indeed, an interior maximizer \(d_*\) solves
\(A=md_*+19d_*^2/2\). Thus \(d_*\le d_{\rm hi}\), and
\(A\le(m+19d_{\rm hi}/2)d_*\), giving \(d_{\rm lo}\le d_*\).
If the maximum is attained at \(D\), then
\(A\ge mD+19D^2/2\); both clipped bounds equal \(D\).
At the maximizer the quadratic part is at most \(Q(A)\), and
the cubic debit is at least \(19d_{\rm lo}^3/6\), proving (5c).
This is one prescribed upper/lower bracket, without an iteration
or a square root. No convexity of the rational function \(R\)
is required.

## 2. The same force variables and their vertices

Use exactly the variables and complete selected-weight alternatives
of the [two-lift evaluation](research_mixed_terminal_two_selected_lift_budget_protocol.md).
The selected penultimate node is \(b\), with \(H=.01\),
\(\Delta_b=H-\Im b_*\), and \(\kappa=\pi\Delta_b\).
Let \(I_b,I_{rb},I_{sb}\) be its three saved normalized imaginary
cotangent means, and let \(V_+\ge0\) be the saved positive upper
for the weighted real combination. The unchanged forces are
\[
 \begin{split}
 A_r&=\kappa(1-I_{rb}),\\
 A_{b,1}&=\kappa(3I_b-I_{rb}-I_{sb}-1),\\
 A&=-u=\kappa(1+I_{sb}).
 \end{split}
 \tag{6}
\]
On the actual family \(A>0\), by the original segment domain
and \(|\Im\cot|<1\) in the
[shared-index proof](research_mixed_terminal_shared_index_gain_cancellation.md).
Containing endpoint combinations need not have that sign.

Let \(B_+\) be the saved upper real endpoint for the center of
\(b\), and \(q_e\) the same saved endpoint logarithm as before.
The two trial bounds and selected forces are
\[
 \begin{array}{c|c|c}
 \mu & \text{trial upper} & \text{selected force}\\ \hline
 1 & \kappa^2V_+/\pi_- -2\pi_-H & A_{b,1}\\
 0 & \kappa^2V_+/\pi_-
       -(.5-B_+)(q_e+q_{1/2,-})/2 & A_{b,1}+q_e .
 \end{array}
 \tag{7}
\]
The forced target remains \([.4,.45]\), while the factorial
target remains \(P=[.22,.45]\). All centers are retained, including
centers outside the forced interval. The same \(q_e\) is used in
both forced entries of (7).

Use the already prescribed uncertain-center cubic majorants
\(\mathcal G_r,\mathcal G_{b,\mu}\), with coefficients \(88/5\)
and \((\mu+1)49/5\). Before rounding they are convex functions
of their forces. The new vertex objective is
\[
 \mathcal F_\mu
 =\text{trial upper in (7)}
   +\mathcal G_r(A_r)+\mathcal G_{b,\mu}(A_{b,\mu})+F(A).
 \tag{8}
\]
It is separately convex in \(\kappa,I_b,I_{rb},I_{sb}\), and
also in \(q_e\) for the forced branch. Each force is separately
affine, \(F\) and the two exact cubic maxima are convex, and
the remaining quadratic has nonnegative coefficient.
Successive endpoint maxima therefore bound (8) using the
same sixteen factorial and thirty-two forced vertices per case.
No convexity property of a rounded gain output is used.

At a saved vertex let \(U_{\rm old}\) be its exact stored total
and \(d_{\rm old}\) its stored linear shared debit. Its new upper is
\[
                    U_{\rm new}=U_{\rm old}-d_{\rm old}+R(A).
 \tag{9}
\]
This subtraction removes a known additive term. It is not a
subtraction of a gain upper as a lower credit. The original
\(r,b\) gain certificates and their exact forces are unchanged.
The saved auxiliary mean for \(s+a\) is not used in (8).
The value \(R(A)\) replaces \(F(A)\) only after the vertex
reduction; it is not asserted to be separately convex.

## 3. Fixed input and computation inventory

The new standalone stdlib-only checker is
[check_mixed_terminal_penultimate_selected_budgets.py](../experiments/check_mixed_terminal_penultimate_selected_budgets.py).
Its prescribed output is
repro/results/research-mixed-terminal-penultimate-selected-budgets.json.
It requires the unchanged records:

* the original two-lift evaluation, SHA256
  55d8252d1a34bb6ad514cdc77c43376c7b4cbc42fd76617b9b21ef1868c8024d;
* its complete saved arithmetic audit, SHA256
  126b39c133170b668ab4e5ffe955a7064dd892521830a7c5b9c8e947226944be;
* the original harmonic reference projection, SHA256
  98a1e6d33c58074fffface6b3da93cbd4d842f5006a2d2f032c94a73ee81c198.

The checker pins those records, their reviewed producers and proofs,
the source criterion, and this protocol. It verifies every inherited
input binding before and after the computation, including its own
hash. Pending pins block execution.

There are exactly two cases, two branches per case, ninety-six
original vertices and ninety-six rational evaluations of (4)--(5c).
All 192 existing cubic certificates are associated by their exact
saved hashes and forces; they are neither regenerated nor optimized.
The independent saved audit supplies their complete root/candidate
verification. The new record retains the old vertex totals, old
debits, the exact rational \(A,m,D,mD\), the branch of (4)--(5),
the quadratic maximizing displacement, the single bracket
\([d_{\rm lo},d_{\rm hi}]\), \(Q(A)\), its cubic debit, \(R(A)\),
and the new total. The exact optimizer of \(F\) is not evaluated.
Direct recombination from the four unchanged trial/gain
summands must agree with (9).

The complete binary vertex inventory and original branch maxima
are checked against the saved audit. Positive new bounds are retained.
Each new branch maximum and its attaining flags are recorded,
together with all original bounds. Nothing is removed because its
sign is unfavorable.

## 4. Failure handling and mathematical scope

Failure of (1), any association, a missing vertex, or any input hash
produces a failed fresh record with the completed rows and exact
reason. It triggers no replacement constant, new sample, split,
gain, analytic call or retry. A nonnegative new budget is an
inconclusive sign test, not an arithmetic failure or counterexample.

The source criterion gives the complete profile upper
\[
 P^+=\max\{-1/400,\max_{\epsilon,\mu,v}U_{\rm new}\}.
 \tag{10}
\]
If \(P^+<0\), the raw local gap is \(-P^+\); one aggregate
finite-source tolerance gives half that gap. Both exact quantities
are recorded only when all four branch maxima and all source
premises have passed. Otherwise the finite upper is retained with
no sign conclusion. The criterion preserves both original boundary
marginals and unselected outer halfweights.
Even a successful local comparison does not prove a whole-word
noncancellation estimate or the finite-exceptions objective.
