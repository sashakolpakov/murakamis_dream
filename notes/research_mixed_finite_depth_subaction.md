# An exact finite-depth potential inequality on the half-period

Research deduction, 5 November 2026. This strengthens the uniform
finite-depth approximation to a relative estimate and then to an exact
local inequality for the original allocated phase. It requires no new
interval cover. The generic depth is large and depends on the compact
local bound already defined; a numerically usable small depth still
requires its own residual verification. Right-region interface signs
and the full-period asymptotic remain open.

## 1. The Bellman residual and its correct occupation budget

Use the original word, reference, weights \(w_i\), occupation
\(\omega_j\), and triple states of
[the finite-depth potential theorem](research_mixed_finite_depth_boundary_potential.md).
All auxiliary real symbols lie in the closed interval \([.1,.5]\).
Fix \(0<\theta<1\) and write
\[
 t_i^\theta=w_i+\frac\theta2(\omega_{i-1}+\omega_i),
 \quad K_\theta=K_*+\frac{21\theta}{4000},
 \quad\Psi_i(v)=\omega_{i-2}+\omega_{i-1}+\omega_i.
 \tag{1}
\]
Here \(v=(q_{i-2},q_{i-1},q_i)\) is a state at layer i.
Let \(H_\theta\) be the anchored incoming potential and
\(A_{\theta,i}^{[h]}\) its length-h incoming maximum from the
phase-aligned baseline. Both use \(t^\theta\). Their established
properties include
\[
 A^{[h]}\le A^{[h+1]}\le H_\theta,\qquad
 H_\theta(\text{baseline})=A^{[h]}(\text{baseline})=0.
 \tag{2}
\]
We suppress the subscript \(\theta\) on A where unambiguous.

The exact finite Bellman identity is
\[
 A_{i+1}^{[h+1]}(v')
  =\max_{v\to v'}\{A_i^{[h]}(v)+t_i^\theta(v,v')\}.
 \tag{3}
\]
The maximum is over the one predecessor symbol, with its allowed
selection; the other two symbols are fixed by \(v'\). The two sides
start at the same baseline layer \(i-h\). Compactness gives actual
maxima, so (3) is an equality, not just a dynamic-programming bound.

For \(V_i=A_i^{[h]}\), let
\(\Delta_{h,i+1}(v')=A_{i+1}^{[h+1]}(v')-A_{i+1}^{[h]}(v')\).
The largest original residual over predecessors is exactly
\[
 \max_{v\to v'}\{w_i(v,v')+V_i(v)-V_{i+1}(v')\}
   =\Delta_{h,i+1}(v')-\frac\theta2(\omega_{i-1}+\omega_i).
 \tag{4}
\]
Thus the symmetric allocation yields a genuine a posteriori criterion
in three output symbols. A numerical lower trial for either maximum
does not certify their difference. To prove (4) nonpositive one needs
the exact functions or an upper bound for \(A^{[h+1]}\) and lower
bound for \(A^{[h]}\), with their correlated source variables retained.

The budget on the right of (4) vanishes when the first two output
symbols are reference symbols, even if the third halo is arbitrary.
Uniform absolute convergence alone does not resolve that locus.
The following allocation avoids it. Put
\[
 B_i(v)=\theta\left(\frac{\omega_{i-1}}6+
                              \frac{\omega_i}3\right),
 \quad
 \bar t_i=t_i^\theta+B_{i+1}(v')-B_i(v)
          =w_i+\frac\theta3\Psi_{i+1}(v').
 \tag{5}
\]
The incoming maxima for \(\bar t\) are
\(\bar A_i^{[h]}=A_i^{[h]}+B_i\), because the baseline has
B-value zero. Their successive-depth increments are still exactly
\(\Delta_h\). Therefore the candidate
\(V_i=A_i^{[h]}+B_i\) has exact maximal residual
\[
 \max_{v\to v'}\{w_i+V_i-V_{i+1}\}
                      =\Delta_{h,i+1}-\frac\theta3\Psi_{i+1}.
 \tag{6}
\]
The new budget is zero only at the baseline triple. On a cycle every
occupation still appears three times in the output triples and hence
receives total share \(\theta\). Formula (5) does not change the
original phase, Fourier normalization or any physical source factor.

## 2. A state-relative finite-depth estimate

Let \(A_i^{[3]}(v)\) be the three-step entry and let
\(E_i^{[3]}(v)\) be the three-step baseline exit, both for
\(t^\theta\). Define
\[
 \mathcal D_i(v)=-A_i^{[3]}(v)-E_i^{[3]}(v),\qquad
 C_\theta=\max\{200,24000K_\theta\}.
 \tag{7}
\]
Then
\[
             (1-\theta)\Psi_i(v)\le\mathcal D_i(v)
                                          \le C_\theta\Psi_i(v).
 \tag{8}
\]
The lower bound follows by joining the entry and exit, adding baseline
steps to align the period, and applying the cyclic occupation inequality.
The three prescribed symbols occur once each; all other symbols are
baseline.

For the upper bound, suppose first \(\Psi_i(v)<\kappa=1/4000\).
Every symbol is then unselected and lies strictly inside the plateau.
If \(d_j=x_j-\Re r_j\), the clamp is inactive and
\(\omega_j=d_j^2/10\). The complete lower/upper plateau Hessian
inputs used in the finite-depth theorem give
\[
 A_i^{[3]}(v)\ge-10(2d_{i-2}^2+d_{i-1}^2),\qquad
 E_i^{[3]}(v)\ge-10(d_{i-1}^2+2d_i^2).
 \tag{9}
\]
All affected rows have their full unselected reference heights. Some
windows contain nonbaseline plateau halos; they nevertheless have the
same targets as the corresponding baseline halos. Summing (9) gives
\(\mathcal D_i\le20\sum d_j^2=200\Psi_i\). If instead
\(\Psi_i\ge\kappa\), the six local bounds give
\(\mathcal D_i\le6K_\theta\le24000K_\theta\Psi_i\). This proves (8).

**Theorem 1 (relative approximation).** For \(0<e\le1\), set
\[
 Q_{\theta,e}=\frac{400(C_\theta+1)}{(1-\theta)e},\qquad
 M_{\theta,e}=\lfloor Q_{\theta,e}\rfloor+1,\qquad
 h_{\theta,e}=5M_{\theta,e}+3.
 \tag{10}
\]
For every original word, actual reference, layer and state,
\[
 0\le H_\theta(v)-A_i^{[h_{\theta,e}]}(v)\le e\Psi_i(v).
 \tag{11}
\]
The depth is independent of the state and word length.

**Proof.** If \(\Psi_i(v)=0\), all three symbols are baseline,
so (11) follows from (2). Otherwise choose an incoming path of weight
\(W\ge H_\theta(v)-\varepsilon\), with
\(0<\varepsilon<\Psi_i(v)\). Since \(H_\theta\ge A_i^{[3]}\),
appending the three-step exit and aligning by baseline steps gives
\[
 (1-\theta)\sum_{\rm path}\omega_j
 \le\mathcal D_i(v)+\varepsilon
 <(C_\theta+1)\Psi_i(v).
 \tag{12}
\]
The initial and closing baseline symbols have zero occupation; all
appended original path symbols are counted once, including its final
prescribed triple.

Choose a radius depending on this terminal state only:
\[
 d^2=\frac{e\Psi_i(v)}{40},\qquad
 0<d^2\le\frac{63}{160000}<\frac1{1600}.
 \tag{13}
\]
The bound uses \(\Psi_i\le3(21/4000)\). A symbol that is
selected or at real distance at least d from its reference costs at
least \(d^2/10=e\Psi_i/400\). Hence (12) permits fewer than
\(Q_{\theta,e}\) bad symbols, independently of the terminal state.

Prepend enough baseline periods and divide the \(5M_{\theta,e}\)
positions immediately before the final three appended symbols into
five-symbol blocks. One block is entirely good. Cut after its third
symbol. The quadratic five-good argument of
[the finite-depth theorem, Corollary 2](research_mixed_finite_depth_boundary_potential.md)
applies with this fixed d: the discarded prefix is at most \(30d^2\),
and resetting the suffix's initial triple to baseline costs at most
\(10d^2\). The suffix has at least five appended symbols, so its
terminal triple is unchanged. Its length is at most \(5M_{\theta,e}\);
pad with baseline steps to length \(h_{\theta,e}\).
Consequently \(W\le A_i^{[h_{\theta,e}]}(v)+40d^2\).
Let \(\varepsilon\) tend to zero. The radius and depth stay fixed,
and \(40d^2=e\Psi_i(v)\), proving (11). \(\square\)

## 3. An exact finite-depth inequality for every original block

**Corollary 2.** Choose \(e=\theta/6\), \(h=h_{\theta,e}\), and
\[
                        V_i(v)=A_i^{[h]}(v)+B_i(v).
 \tag{14}
\]
Then every admissible half-period transition satisfies
\[
 w_i(v,v')\le V_{i+1}(v')-V_i(v)
                                -\frac\theta6\Psi_{i+1}(v').
 \tag{15}
\]
Indeed \(0\le\Delta_h\le H_\theta-A^{[h]}\le e\Psi\).
Substitute this in the exact residual identity (6). More generally
any \(e<\theta/3\) retains loss \((\theta/3-e)\Psi\).

For example \(\theta=1/2,e=1/12\) permits
\[
 h=5\bigl(\lfloor9600(C_{1/2}+1)\rfloor+1\bigr)+3,
 \qquad w_i\le V_{i+1}-V_i-\Psi_{i+1}/12.
 \tag{16}
\]
No numerical value of \(K_*\), \(C_{1/2}\), h or the functions
V has been certified here. Formula (16) is a proved finite choice in
terms of the specified compact bound, not a claim that this generic
depth is computationally small.

All these functions vanish on baseline states. They are continuous
finite maxima and use only a fixed finite window of the actual periodic
reference, whose size is bounded by h plus the state halo. No arbitrary
reference-box point replaces that actual reference in the cyclic input.
The independent boxes are used only to bound the compact constants.
The phase-aligned padding and the three occupation incidences remain
literal for primitive periods one and two. In particular a one-cycle
has one original block and three occurrences in the output triple,
not three physical copies of that block.

On a full half-period cycle, (15) sums to
\(\sum_iw_i\le-(\theta/2)\sum_i\omega_i\). This is weaker
than the already proved full cyclic occupation loss, but supplies its
new finite-memory local realization. It is not a new asymptotic inferred
from finitely many words.

## 4. Consequence for the physical open components

Retain the A/R partition, raw R-incident defects \(D_j\), actual
A-run states and original finite allocation from
[the interface reduction](research_mixed_nonlow_interface_reduction.md).
An A-run \([l,r]\) now has the exact phase bound
\[
 \sum_{j=l+1}^r w_j
 \le V(v_r)-V(v_l)
                 -\frac\theta6\sum_{j=l+1}^r\Psi_{j+1}.
 \tag{17}
\]
The sum on the right is over its literal output triples, including
the baseline halos. There is no approximation tolerance per run.
For a singleton the two states coincide and the sum is empty.

The complete finite allocated product of a mixed cycle therefore has
upper exponent
\[
 M+\sum_{j\text{ incident to R}}D_j
   +\sum_{\text{A-runs}}\{V(v_r)-V(v_l)\}
   -\frac\theta6\sum_{\text{AA edges }j}\Psi_{j+1}+\delta,
 \tag{18}
\]
with its fixed-word polynomial prefactor and one chosen total
finite-source tolerance \(\delta>0\). The two Fourier halves
recombine once at each physical vertex and the original complex
tangents cancel by critical stationarity. Neither a potential nor
an auxiliary connector introduces a new physical kernel factor.

Thus the remaining R-component function is explicitly
\[
 J_{s,t}^{V}=\sum_{j=s}^{t+1}D_j
                +V(v_{\rm left\ exit})-V(v_{\rm right\ entry}).
 \tag{19}
\]
If a separate quantitative comparison made these functions negative,
it could be used directly in (18), with no AA Bellman verification and
no accumulated potential-approximation errors. Their values and signs
are not evaluated here. Long R-runs still have the proved internal RR
loss; that fact does not by itself pay the interface terms in (19).

For practical smaller h, the exact residual test (6) remains available.
It can retain a loss once
\(\Delta_h\le(\theta/3-\rho)\Psi\) is certified. The theorem
above proves that some uniform finite h succeeds; it does not certify
a particular small-depth numerical optimizer or a difference of its
two lower trial values.

```sh
python3 experiments/check_mixed_finite_depth_subaction.py
```

The focused checker validates the gauge, allocation and relative-depth
arithmetic and the current completed source bindings. It performs no
potential optimization or new interval cover and does not establish a
right-interface sign or a full-period or knot theorem.
