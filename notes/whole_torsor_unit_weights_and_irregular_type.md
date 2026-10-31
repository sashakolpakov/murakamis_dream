# Whole torsor units, level weights, and the finite jet depth for a norm

Independent function-level theorem, 27 October 2026. There is a sharp
distinction between a fixed algebraic comparison section and a
horizontal period on a fixed finite-type algebraic connection.
A classically normalized algebraic unit can change a leading regulator
rate when the level character amplifies its first unseen jet.
Conversely a finite jet depth suffices once that character weight is
bounded. These are statements about whole functions, not independently
chosen levelwise tails.

They complement [exact cyclotomic Mellin uniqueness](mellin_cyclotomic_jet_uniqueness.md).
No modification below is asserted to preserve the actual knot source.

## 1. A sharp unit/weight theorem

Let \(t_N=1/N\). Suppose holomorphic units \(u_j(t)\) on one
common marked neighborhood satisfy, uniformly in their index,
\[
 u_j(t)=1+O(t^k),\qquad k\ge1.
\]
The number of factors may depend on \(N\). For integer characters
\(m_{N,j}\) assume the total weight bound
\[
 \sum_j |m_{N,j}|\le C N^d .
\]
Then the whole scalar comparison
\[
 a_N=\prod_j u_j(t_N)^{m_{N,j}}
\]
satisfies
\[
 |\log|a_N||\le C' N^{d-k},\qquad
 \frac1N\log|a_N|=O(N^{d-k-1}).                       \tag{1}
\]
Thus it has subexponential norm whenever \(k\ge d\).

Proof: choose the logarithm with \(\log u_j(0)=0\).
Uniformity and the convergent logarithm imply
\(|\log u_j(t)|\le C''|t|^k\) on a smaller common neighborhood.
Sum these bounds with the absolute character weights.
Both positive and negative exponents are covered. In particular
(1) bounds the comparison and its inverse, so multiplying a
nonzero selected scalar by it preserves every existing leading
exponential rate. It does not estimate an internal sum with
cancelling coefficients.

The threshold is sharp for \(d\ge2\). If one unit has
\(\log u(t)=\alpha t^{d-1}+O(t^d)\) and
\(m_N/N^d\to\kappa\), then
\[
 \frac1N\log|u(t_N)^{m_N}|
                 \longrightarrow\kappa\,\operatorname{Re}\alpha .
                                                               \tag{2}
\]
For a quadratic character weight \(O(N^2)\), agreement through
the first physical-arc Taylor coefficient, \(u=1+O(t^2)\),
therefore suffices. Classical agreement \(u(0)=1\) alone does not.

The uniform remainder and total weight are substantive hypotheses.
They cannot be inferred from separate algebraicity at each level
or from a common classical value.

## 2. A single algebraic unit can change the leading rate

Put \(c=2\pi i\), \(Q_N=e^{c/N}\), and take the whole rational unit
\[
 u(Q)=1+i(Q-1)\in\mathbb Q(i)(Q),\qquad u(1)=1.
\]
For all sufficiently large \(N\), it is nonzero and
\[
 \log u(e^{ct})=-2\pi t+O(t^2).
\]
Consequently
\[
 \lim_{N\to\infty}\frac1N
      \log|u(Q_N)^{N^2}|=-2\pi .                       \tag{3}
\]
Its inverse has the opposite rate. The coefficient \(i\) is a
fixed algebraic constant, as permitted on a marked geometric
coefficient field. All root values in (3) are algebraic numbers.

There is also a rational-coefficient example:
\(u(Q)=(1+Q)/2\). Since
\[
 u(Q_N)=e^{\pi i/N}\cos(\pi/N),
\]
one has
\[
 \lim_{N\to\infty}\frac1N
       \log|u(Q_N)^{N^3}|=-\pi^2/2 .                  \tag{4}
\]
The first complex logarithmic term in this example is a phase;
its first real term is quadratic.

More generally, for every fixed \(J\ge0\), take
\[
 u(Q)=1+i^{-(J+1)}(Q-1)^{J+1}.
\]
It agrees with one through all ordinary Q-jets of order \(J\)
at \(Q=1\). Nevertheless
\[
 \lim_{N\to\infty}\frac1N
   \log|u(Q_N)^{N^{J+2}}|=(2\pi)^{J+1}.               \tag{5}
\]
Thus a finite jet budget controls a norm only after the level
character weight is controlled. This is a single whole algebraic
unit, rather than a separately assigned \(a^Nz^N\) tail.

## 3. Finite type of a connection is not bounded algebraic section complexity

The preceding amplified functions occur on a fixed finite-type
algebraic connection. Work over the punctured \(t\)-base and
the open where \(u(Q)\ne0\). Introduce coordinates \(L,W\), with
\(W\ne0\), and the algebraic differential laws
\[
 dL=\frac{du}{u},\qquad
 d\log W=t^{-d}\frac{du}{u}
                   -d\,t^{-d-1}L\,dt .                \tag{6}
\]
This is a full flat connection: on its horizontal sections
the right side for \(d\log W\) is \(d(t^{-d}L)\).
Equivalently the two mixed derivatives commute directly.
There is no claim that the naive product translation on
\(L,W\) makes (6) a regular principal connection at \(t=0\).

On the marked branch \(L=\operatorname{Log} u\), its horizontal period is
\[
 W=\exp(t^{-d}\operatorname{Log} u).
\]
Restricting \(t=1/N\) gives exactly \(u(Q)^{N^d}\).
The connection has fixed algebraic rank and presentation, while
its marked horizontal period is not generally an algebraic
function of the base. Its singularity at \(t=0\) retains the
large character and cannot be omitted.

Therefore a claim of finite-type algebraic torsor or connection
does not by itself supply the bounded algebraic comparison
SECTION required by the existing reconstruction and norm
theorems. Conversely (1) identifies a finite sufficient jet depth
when the relevant character degrees are known.

This does not refute the flat pointed-comparison lifting lemma:
(6) is singular at the classical boundary and does not give a
regular pointed comparison there. It also does not preserve the
actual finite-level source equation or its pointing. Such
source conditions are precisely what can exclude (3)--(5).

## 4. Which jets and which functions

The three distinct uniqueness assertions should remain separate:

* If two functions are holomorphic at the same ordinary point and
  all their Taylor coefficients agree, they are the same analytic
  germ. Marked continuation then fixes them on a connected common
  continuation domain.
* Equality of asymptotic formal power series at an irregular
  puncture is weaker. Exponentially flat sectorial differences can
  remain, as proved in
  [the earlier function audit](global_period_rigidity_function_audit.md).
* Varying finite-dimensional root fibers are not one analytic
  function unless a whole family has been constructed. Here exact
  source and pole conditions are decisive:
  [the bounded-jet Mellin theorem](mellin_cyclotomic_jet_uniqueness.md)
  proves equality of the entire rational root function from
  orders \(0,\ldots,D(s-1)\), in its specified finite X-window
  and cyclotomic numerator lattice.

The Taylor order in (1) is along the physical arc
\(t\mapsto(t,Q=e^{ct})\) at \(t=0\). It must not be confused
with a quantum-normal Taylor derivative at a fixed root
\(Q=Q_N(1+\epsilon)\), where \(N\) is held fixed.
Exact root-normal source identities and bounded whole
presentations can relate these data; classical shape
etaleness alone cannot.

## 5. Consequence for the optimizer/torsor proposal

The algebraic Rivin optimizer fixes the chosen shape branch and
its local critical field. A marked Bloch primitive then fixes the
geometric action, with its original peripheral signs.
The new doubled-phase optimizer also gives an algebraic positive
Hessian. These are meaningful whole geometric data.

What remains is a source-compatible comparison, not another
classical uniqueness argument. One concrete sufficient route is
now finite: construct a candidate whole root Mellin function
with the ACTUAL cyclotomic numerator lattice and ACTUAL source
equation through the fixed quantum order of the bounded-jet
theorem. That theorem then identifies it exactly with the
selected actual root function, including its residue.

To infer its norm from a regulator factor, its remaining
comparison units must either belong to the bounded algebraic
section class already covered by norm control, or satisfy an
explicit level-weight estimate such as (1).
Finite-type period connections and classical unit normalization
alone are insufficient by (3)--(6).
No existence of that comparison, selected geometric coefficient,
global dominance, or volume limit is claimed here.

The complementary [doubled-phase theorem](doubled_phase_rivin_optimizer.md)
constructs the whole classical period connection explicitly, and the
[critical-source theorem](irreducible_critical_source_and_whole_norm.md)
gives a finite criterion for a genuinely descended source density
with polynomial norm bounds. Their proofs are recorded in the
[independent audit](doubled_phase_and_critical_source_independent_audit.md).

