# Both terminal main alternatives at the same higher contour

Research result, 6 November 2026. At each of the four already certified
canonical suffix references, both original terminal joint main
alternatives have gap greater than \(1/200\) at the single common
height \(H=27/2000=.0135\). The bound is uniform over the full
original real main target products, including \(a_R\in P\) for
both alternatives. This is a main-current comparison, not a complete
terminal-source theorem.

## 1. The comparison and why the height change is legitimate

Use the original allocation and defects from
[the joint-main theorem](research_mixed_terminal_joint_main_budget.md).
The preceding ordinary own flag is one,
\(\beta,\epsilon\in\{0,1\}\) are the incoming and terminal flags,
and the canonical external parameters are
\[
 b_0=.35-.01i,\qquad b_1=.30-.052i.
 \tag{1}
\]
Existence, zero logarithmic lifts, and stationarity of these four
references were certified previously. They are not asserted to be
realized by finite mixed words.

The [curvature completion](research_mixed_terminal_joint_main_curvature_completion.md)
controlled both main alternatives at \(H_0=.01\), with common
gap \(1/800\). The new [common-height theorem](research_mixed_terminal_joint_main_common_height.md)
retains the same ordinary-index and terminal-index convex costs in
the forced phase. Its selected-coordinate force is positive in all
four saved cases, so its full-\(P\) affine support still uses the
right endpoint \(.45\). Discarding only the nonnegative selected
convex cost gives a stronger forced bound on **all** of \(P\),
without relying on the smaller forced interval at \(H_0\).

The exact saved-data check verifies the three additional guards
\[
 T_0<-\frac{109}{1000},\qquad
 0<A_{a,0}<\frac{63}{200},\qquad
 \Re a_*>\frac7{25},
 \tag{2}
\]
along with every original height, stationarity-certificate association,
and curvature-input guard. The initial full-target budgets therefore
satisfy
\[
 B_1<-\frac{50063}{39680000},\qquad
 B_0<-\frac{843167}{39680000}.
 \tag{3}
\]
The factorial rate decreases by at least \(11\Delta H/10\);
the forced rate increases by at most \(1241\Delta H/300\).
These are pointwise estimates on a common legitimate maximizing
product, derived from the original logarithms and shared chirp.
Thus at \(\Delta H=7/2000\), both estimates concern the same
height \(H=27/2000\):
\[
 \begin{split}
 \sup D_1(H)&<-\frac{202831}{39680000}<-\frac1{200},\\
 \sup D_0(H)&<-\frac{4030001}{595200000}<-\frac1{200}.
 \end{split}
 \tag{4}
\]
The respective rational reserves beyond \(1/200\) are
\(4431/39680000\) and \(1054001/595200000\).
No estimate at one height is combined with the other Fourier
alternative at a different height.

The original main target intervals remain
\(b_R,a_R\in P=[.22,.45]\), \(s_R\in[.125,.5]\),
\(t_R\in[.15,.5]\), and the complete private interval
\([.1,.4]\) for terminal type three or \([.27,.49]\) for
terminal type four. Their other heights are the original reference
heights. Existing pointwise index barriers justify the smaller
maximizing domains used in the proof, without changing these targets.
The complete selected weight is bounded by the sum of its factorial
and forced alternatives throughout.

## 2. Isolated finite-main consequence

Let \(\mathcal M_N(b,a)\) be the contribution obtained by selecting
the ordinary main contour and both terminal main contours in the
original finite-current decomposition, retaining the full selected
weight, its monomial, and the allocated incoming modulus halfweight.
This is the same isolated contribution as in the earlier curvature
completion, now on the common height \(H=27/2000\).

The original regular-contour symbol bounds admit this height. With
the original reference action \(M_*\) and incoming complex marginal
\(p_*\), (4) gives
\[
 |\mathcal M_N(b,a)|\le C_\tau N^{A_\tau}
 \exp N\left\{\Re[M_*+p_*(b-b_*)]-\frac1{200}+\tau\right\}.
 \tag{5}
\]
It holds uniformly on the stated targets and an original sufficiently
small ordinary-color disk, through both level parities. Taking
\(\tau<1/800\) and absorbing the polynomial prefactor into the
remaining strict tolerance yields the finite-main rate gap \(1/400\)
for all sufficiently large \(N\). This argument does not bound the
sum of the other terminal currents.

## 3. Evidence and scope

The single [saved-data checker](../experiments/check_mixed_terminal_joint_main_common_height.py)
run has SHA256 1f9680fc15362516df2b82c8bbcdb99e9720f2861e04209641669ddb191d2e03.
Its [result](../repro/results/research-mixed-terminal-joint-main-common-height.json)
has SHA256 53789515f1b33ffe9397c7a4405be7bcaa3db865267ad1e7da0495399c691cba.
All 50 input bindings remained unchanged. It verifies four source
associations, the inherited original height and curvature guards,
the new guards (2), the full-\(P\) gain sums, and the exact rational
transport and reserves in (3)--(4). No analytic evaluator, primitive,
root, optimizer, grid or finite source is called or replayed.
This discharges the saved-application check left explicit in Section 3
of the frozen common-height theorem, SHA256
3c7a3ef14df887676ca8e35c1b9b37957f2e09d0945fcadc15c947f687b9fbab.

The reusable result is the common-height criterion, not a new uniform
cover of the external reference disks. The other terminal profiles
and the original outer cycles remain outside this comparison.
No complete terminal-kernel gap, nonzero whole-source coefficient,
whole-invariant asymptotic, or arbitrary short-filling theorem is
claimed.
