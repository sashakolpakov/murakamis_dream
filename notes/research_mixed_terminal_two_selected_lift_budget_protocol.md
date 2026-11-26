# Fixed evaluation of the two added ordinary-lift budgets

Research evaluation protocol, 6 November 2026. This protocol is unrun.
It reuses the complete old reference banks and their exact harmonic
projection. There are two cases, one for each terminal type, with the
two external types combined by containing intervals. No root, backward
shape decoding, new parameter cell or source evaluation is introduced.

The purpose is to check the two inequalities in the
[composition theorem](research_mixed_terminal_two_selected_budget_composition.md),
using the linear shared debit of the
[cancellation theorem](research_mixed_terminal_shared_index_gain_cancellation.md).
A nonpositive result for both alternatives in both cases would
transfer the completed terminal profile gap. No sign is presumed.

## 1. Fixed source and argument inventory

The [reference-bank transfer](research_mixed_terminal_two_selected_reference_bank_transfer.md)
identifies the seven original suffix coordinates with the previously
certified prefix coordinates. Its standalone saved-data projection
must pass before this evaluation starts. The projection is
repro/results/research-mixed-terminal-two-selected-reference-projection.json.
It retains the 637 and 646 accepted old-\(\beta=1\) references,
respectively, all eighteen complete chart trees, all strict geometric
exclusions and every inherited association.

For each terminal flag \(\epsilon=0,1\), use the exact projected
coordinate component intervals for \(r,b,s,a\), and the sixteen
intervals \(J_j=[j/16,(j+1)/16]\). With \(H=1/100\), the
four prescribed arguments are
\[
\begin{array}{c|c}
\text{key}&\text{argument}\\ \hline
b&b+i\theta(H-\Im b)\\
rb&r+b+i\theta(H-\Im b)\\
sb&s+b+i\theta(H-\Im b)\\
sa&s+a+i\theta(H-\Im a).
\end{array}
\tag{1}
\]
The real sum is formed inside each old boundary cell before extrema
are taken. For example the \(rb\) imaginary part is
\(\Im r+(1-\theta)\Im b+\theta H\). For each fixed \(\theta\)
both components are scalar harmonic functions of the original
external coordinate. Their bounds extend through the complete
typed \(K\) domain. At a fixed reference each component is affine
in \(\theta\), so the hull of its two endpoint bounds covers
the whole slab. The same statement holds for all four rows in (1).

The full complex argument need not be holomorphic in the external
parameter. No such assertion, or maximum principle for a nonlinear
budget, is used. Union over the two external types is a containing
interval operation after the separate harmonic statements.

The evaluator checks the full coordinate guards
\[
 .24\le\Re(r,b,s,a)\le.36,\qquad
 -.102\le\Im(r,b,s,a)\le-.001 .
\tag{2}
\]
It also checks every argument rectangle is strictly inside
\(0<\Re z<1\). These are guards, not clipping instructions.
All calculations use the projected full rectangles. The actual
reference remains the canonical one; the interval midpoints
are never treated as stationary.

## 2. The integral data and forces

Evaluate \(\cot(\pi z)\) once on each of the
\(2\cdot16\cdot4=128\) rectangles in (1), at 256 bits.
Record its real and imaginary intervals as \(C_{\ell,j},I_{\ell,j}\).
The exact positive weights are
\[
       w_j=\frac1{16},\qquad
       v_j=\int_{J_j}(1-\theta)\,d\theta
                              =\frac{31-2j}{512}.
\tag{3}
\]
Define interval sums
\[
\begin{split}
 I_\ell&=\sum_{j=0}^{15}w_j I_{\ell,j},
                    &&\ell=b,rb,sb,sa,\\
 V&=\sum_{j=0}^{15}v_j(3C_{b,j}-C_{rb,j}-C_{sb,j}).
\end{split}
\tag{4}
\]
They enclose the normalized means for every actual reference.
The sums in (4) are exact rational operations on directed endpoints.

Let \(\Delta_b=H-\Im b\), \(\Delta_a=H-\Im a\),
\(\kappa=\pi\Delta_b\), and use an outward interval for
\(\kappa\). Original stationarity gives exactly
\[
\begin{split}
 W_b&=\pi\Delta_b^2 V_{\rm actual},\\
 A_r&=\kappa(1-I_{rb}^{\rm actual}),\\
 A_{b,1}&=\kappa(3I_b^{\rm actual}-I_{rb}^{\rm actual}
                                        -I_{sb}^{\rm actual}-1),\\
 -u&=\kappa(1+I_{sb}^{\rm actual}),\\
 v_s&=\pi\Delta_a(1-I_{sa}^{\rm actual}).
\end{split}
\tag{5}
\]
Here the superscript denotes the actual integral, as opposed to
its enclosing interval. In particular the original chirp in \(u\)
is retained.

Write \(\pi_-\) for the saved lower endpoint, let
\(V_+=\max(0,V^{\rm upper})\), and put
\[
\begin{split}
 \underline v&=\pi_-\,\Delta_a^{\rm lower}
                         \max(0,1-I_{sa}^{\rm upper}),\\
 d_s&=\frac12-(\Re s)^{\rm lower},\\
 \mathcal D(\kappa,I_{sb})&=
                 d_s\max\{0,\kappa(1+I_{sb})-2\underline v\}.
\end{split}
\tag{6}
\]
The whole \(sa\) segment has real part in \((.48,.72)\), so
\(v_s>0\). Thus \(\underline v\) is a valid lower bound even
if the interval for \(I_{sa}\) is too wide to prove positivity.
No interval endpoint of \(I_{sa}\) is asserted to be attained.
The cancellation theorem implies that (6) is an upper for the
positive shared-index debit. The projected bound for \(\Re s\)
and (2) justify its reflection argument.

At any allowed \(\kappa\),
\[
                         W_b\le \frac{\kappa^2V_+}{\pi_-}.
\tag{7}
\]
This discards a possible negative vertical contribution but
makes the right side convex in \(\kappa\). The common
\(\kappa\) and \(I_{sb}\) remain in the force and debit formulas.

## 3. The forced trial and its force share one endpoint value

Let \(B_+\) be the upper real endpoint of the projected \(b\)
interval, and set
\[
 q(x)=\Re g'(x+iH),\qquad q_e=q(B_+),\qquad
                         q_{1/2}=\log(1+e^{2\pi H}).
\tag{8}
\]
On \([.24,.5]\), \(q'=g_H''\ge0\) and \(q''=g_H'''<0\),
by the same elementary cotangent calculation as in the
cancellation theorem. Also \(q>0\): in
\[
 |1-e^{2\pi H-2\pi ix}|^2
             =1+e^{4\pi H}-2e^{2\pi H}\cos(2\pi x),
\]
the last two terms have positive sum because
\(\cos(2\pi x)<1/5\) and \(e^{2\pi H}>1\).
Since \(\Re g(1/2+iH)=0\), monotonicity and the chord lower
bound for the concave function \(q\) give
\[
\begin{split}
 \Re g(\Re b+iH)
 &\le \Re g(B_++iH)\\
 &=-\int_{B_+}^{1/2}q(x)\,dx\\
 &\le-\frac{1/2-B_+}{2}\{q_e+q_{1/2}\}.
\end{split}
\tag{9}
\]

Use the same actual \(q_e\) when bounding the forced force:
\[
                 A_{b,0}\le A_{b,1}+q_e .
\tag{10}
\]
The forced target is \([.4,.45]\), whereas every center
is at most \(B_+\le.36\). Every displacement is therefore
strictly positive, so its scalar conjugate is nondecreasing
in force. This proves that replacing the actual \(q(\Re b)\)
by \(q_e\) in (10) is an upper bound. No such monotonicity
replacement is made for the factorial branch.

Only one exponential, two cosines and three real logarithms
are needed for these data, in addition to one \(\pi\):
\[
 E=e^{2\pi H},\quad
 q_e=\tfrac12\log(1+E^2-2E\cos(2\pi B_+))
                  \quad\text{for each }\epsilon,\quad
 q_{1/2}=\log(1+E).
\tag{11}
\]
Every logarithm argument must have a strictly positive outward
lower endpoint. The \(q_e\) interval remains a shared variable
in (9)--(10); \(q_{1/2}\) is replaced by its lower endpoint.

## 4. Signed scalar gains and the finite vertex sets

Use the exact uncertain-center cubic gain
\[
 G_K(q;[A,B],[L,R])=
 \max_{c\in[A,B],\,x\in[L,R]}
       \{q(x-c)-K[h(x)-h(c)-h'(c)(x-c)]\},
 \quad h(x)=x^2/4-x^3/6 .
\tag{12}
\]
All center and target intervals must lie in \([.18,.5]\).
The [two-edge theorem](research_signed_cubic_gain_with_uncertain_center.md)
reduces (12) exactly to \(c=B\) or \(x=R\). Use
\[
 G_r(q)=G_{88/5}(q;\Re r,[.22,.5]),\qquad
 G_{b,\mu}(q)=G_{(\mu+1)49/5}(q;\Re b,I_\mu),
\tag{13}
\]
where \(I_1=P\), \(I_0=[.4,.45]\).
The latter is the proved complete-weight dominant forced interval.
Its signed gain is never replaced by its maximum with zero.

For the factorial branch maximize the following containing
upper over the sixteen vertices of
\((\kappa,I_b,I_{rb},I_{sb})\):
\[
\begin{split}
 U_1={}&\frac{\kappa^2V_+}{\pi_-}-2\pi_-H
       +G_r\bigl(\kappa(1-I_{rb})\bigr)\\
 &+G_{b,1}\bigl(\kappa(3I_b-I_{rb}-I_{sb}-1)\bigr)
       +\mathcal D(\kappa,I_{sb}).
\end{split}
\tag{14}
\]
For the forced branch use the thirty-two vertices with the
additional variable \(q_e\):
\[
\begin{split}
 U_0={}&\frac{\kappa^2V_+}{\pi_-}
       -\frac{1/2-B_+}{2}(q_e+q_{1/2}^{\rm lower})
       +G_r\bigl(\kappa(1-I_{rb})\bigr)\\
 &+G_{b,0}\bigl(\kappa(3I_b-I_{rb}-I_{sb}-1)+q_e\bigr)
       +\mathcal D(\kappa,I_{sb}).
\end{split}
\tag{15}
\]
Each gain is convex in its force. Each force is separately
affine in the displayed variables, the positive-part debit is
separately convex, and the first term is convex in \(\kappa\).
The forced trial is affine in the same \(q_e\) as its gain.
Successive endpoint bounds therefore prove (14)--(15) on the
whole containing interval product. This argument does not
claim that extrema of different actual means occur together.
Nor does it assume convexity of a rounded numerical gain.

There are \(2(16+32)=96\) vertices and exactly two gains
per vertex, for 192 signed gain evaluations. Repeated endpoint
values of a degenerate interval are retained as distinct
vertices, so the inventory is independent of degeneracy.

For each gain keep both endpoints on each of its two edges.
On \(c=B\), also retain the real roots
\[
 x=\tfrac12\pm\sqrt{(\tfrac12-B)^2-2q/K};
\tag{16}
\]
on \(x=R\), retain
\[
 c=\frac{R+1/2\pm\sqrt{(R-1/2)^2+4q/K}}{2}.
\tag{17}
\]
A negative discriminant removes only that pair of roots.
Use a fixed 240-bit dyadic enclosure of each nonnegative
square root, proved by integer squaring, with no iterative
precision change. Intersect each resulting root interval
with its edge interval. Discard it only if the intersection
is empty; retain endpoint-touching and repeated roots.
Interval evaluation of the exact cubic on every retained
candidate yields an upper for its value. The maximum of
these finitely many upper endpoints bounds (12).
There are at most eight candidates and two square roots
per gain, hence at most 1536 candidates and 384 square roots.
No zero candidate is added unless it is already an allowed
endpoint or root.

## 5. Execution, evidence and failure handling

The standalone driver is
experiments/evaluate_mixed_terminal_two_selected_lift_budgets.py.
It verifies all literal and inherited input hashes, successful
projection status, exact coordinate names, case/slab inventory,
theta endpoints and original boundary associations before
importing the analytic library. It records the projection
case hashes and exact argument endpoints.

The only analytic calls permitted are the fixed 128 cotangents
and the seven additional calls in (11), counting \(\pi\).
All integral weights, vertex forces, debits, cubic candidates
and final sums use exact rational arithmetic after directed
endpoint extraction. The record retains each analytic input
and enclosure, all 96 vertices and 192 gain witnesses,
every finite upper regardless of sign, and before/after hashes.
Output is a new exclusive deterministic gzip file; no old
record is overwritten.

Failure of a mathematical or arithmetic guard is inconclusive,
not a geometric exclusion. The partial case and all completed
calls remain in the record. Unexpected errors are marked
separately and stop the run; interrupted or altered-input
outputs carry no comparison flag. There is no fallback,
refinement, alternate interval, root, optimizer or retry.

If all four upper bounds are nonpositive, the composition
and cancellation theorems transfer raw gap \(1/2600\) and
finite gap \(1/5200\) for the stated two-selected suffixes.
Otherwise the corresponding bounds remain inconclusive.
Even success would concern the specified local kernel and
its authorized assemblies, not a whole-word asymptotic or
a new knot-volume theorem.
