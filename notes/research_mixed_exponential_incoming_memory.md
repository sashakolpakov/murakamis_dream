# Exponential decay of the effect of an incoming history

Research deduction, 5 November 2026. The common boundary potential can
be approximated by a finite incoming path with an error that decreases
exponentially in the path length. This holds throughout the controlled
half-period, including transition coordinates and every permitted
Fourier selection. It does not require that the path stay in the
unselected plateau. The boundary comparisons with the remaining parts
of the integration domain are still separate questions.

## 1. Boundary states, weights and occupation

Fix one of the original periodic type-three/type-four words and its
actual geometric reference. A symbol consists of a real integration
coordinate and its permitted Fourier selection. A state at layer \(i\)
is the triple of symbols at positions \(i-2,i-1,i\). Appending one
symbol gives the next state. All types and references are extended
periodically, but target symbols in different periods remain independent.

Use the weights and occupation function of the
[relative finite-depth theorem](research_mixed_finite_depth_subaction.md).
The real coordinates first range over \([.1,.5]\). Write
\[
 a=1-\theta,\qquad
 t_i=w_i+\frac\theta2(\omega_{i-1}+\omega_i),\qquad
 \Psi_i(v)=\omega_{i-2}+\omega_{i-1}+\omega_i,
 \qquad 0<\theta<1.
 \tag{1}
\]
Here \(w_i\) is the original allocated phase minus its complex
geometric tangent, including the selected Fourier corrections.
The nonnegative number \(\omega_j\) is the already proved occupation
penalty: it vanishes precisely at an unselected reference symbol.
For completeness its formula on this alphabet is
\[
 \omega_j=\frac1{4000}
    \min\{1,\sigma_j+400(\operatorname{clamp}_{[.22,.45]}(x_j)
                                      -\Re r_j)^2\}
                          +\frac1{10}(x_j-.45)_+.
 \tag{2}
\]
The selection \(\sigma_j\) is either zero or one; type three only
permits zero. In (2), \(u_+=\max(u,0)\) and the clamp replaces a
real number below .22 or above .45 by that nearest endpoint.

Let \(H_i(v)\) be the supremum of all incoming \(t\)-weights
from the baseline state at layer zero. Baseline symbols are the
unselected reference symbols. Let \(A_i^{[h]}(v)\) be the maximum
of the weights of paths of exactly \(h\) steps from the baseline
at layer \(i-h\) to \(v\). The phase-aligned definitions and
zero-weight baseline padding give \(A_i^{[h]}\le H_i\), with
equality zero at baseline terminal states.

Write \(E_i^{[3]}(v)\) for the weight of appending three baseline
symbols to \(v\), and put
\[
 D_i(v)=-A_i^{[3]}(v)-E_i^{[3]}(v),\qquad
 C=\max\{200,24000K_\theta\},
 \quad\lambda=1-\frac aC.
 \tag{3}
\]
The compact local bound \(K_\theta\) and the following inputs have
already been proved:
\[
 \sum_{\text{cycle}}t_i\le-a\sum_{\text{cycle}}\omega_j,
 \qquad 0\le D_i(v)\le C\Psi_i(v),
 \qquad A_i^{[3]}(v)\le H_i(v)\le-E_i^{[3]}(v).
 \tag{4}
\]
In particular \(0<\lambda<1\). Cycles in (4) may be any positive
integer repetition of the original type word with its repeated actual
reference. This is sufficient for all closing arguments below.

## 2. Every prefix of a nearly optimal history is nearly optimal

Take an incoming path with appended symbols \(q_1,\ldots,q_T\),
initial baseline state, terminal state \(v_T\), and total weight
\(W_T\ge H_T(v_T)-\varepsilon\), where \(\varepsilon>0\).
Let \(v_j\) and \(W_j\) denote its state and weight after \(j\)
steps. Then
\[
                   H_j(v_j)-\varepsilon\le W_j\le H_j(v_j).
 \tag{5}
\]
The upper inequality follows from the definition of the supremum.
For the lower inequality, suppose the deficit of a prefix exceeded
\(\varepsilon\). Replace it by an incoming path to the same state
whose weight is sufficiently close to \(H_j(v_j)\), then retain
the original suffix exactly. This would give weight greater than
\(H_T(v_T)\), a contradiction. The replacement may have a different
length, but its terminal layer agrees modulo the original period.
Consequently the unchanged suffix has the same types, reference
coordinates and weights. No maximum of the infinite incoming problem
is needed.

Define the cumulative occupation
\[
 P_j=\sum_{s=1}^j\omega_s,
 \qquad P_0=0,
 \qquad\Psi_j(v_j)=P_j-P_{j-3}\quad(j\ge3).
 \tag{6}
\]
Close the prefix by its three baseline exit steps and enough baseline
steps to restore layer zero. All added symbols have occupation zero;
the occupation of each appended original symbol occurs once in the
closed cycle. From (4)--(5),
\[
 aP_j\le -W_j-E_j^{[3]}(v_j)
             \le D_j(v_j)+\varepsilon
             \le C\Psi_j(v_j)+\varepsilon.
 \tag{7}
\]
The closing steps supply the missing endpoint half-shares in the
original transition weights. Thus (7) counts full symbol occupations,
not just those of the middle two symbols in the final transition.

Substituting (6) into (7) gives the elementary backward recurrence
\[
                    P_{j-3}\le\lambda P_j+\frac\varepsilon C.
 \tag{8}
\]
The terminal version of (7) is
\(P_T\le(C/a)\Psi_T+\varepsilon/a\). Iteration of (8) therefore
yields, whenever \(T-3k\ge0\),
\[
 P_{T-3k}\le\frac Ca\lambda^k\Psi_T(v_T)
                                      +\frac\varepsilon a.
 \tag{9}
\]
Indeed the error sum is a finite geometric series and
\(1-\lambda=a/C\). Formula (9) is a quantitative bound for the
entire early part of a nearly optimal path, including its selected
or transition symbols.

There is also a uniform bound on where those symbols can occur.
Let \(\kappa=1/4000\) and choose
\[
 k_0=1+\left\lceil\frac Ca\log\frac{126C}{a}\right\rceil.
 \tag{9a}
\]
Since \(\Psi_T\le63\kappa\),
\((C/a)\lambda^{k_0}\Psi_T<\kappa/2\).
For \(0<\varepsilon<a\kappa/2\), (9) gives
\[
                         P_{T-3k_0}<\kappa.
 \tag{9b}
\]
If the incoming history is shorter than \(3k_0\), there is no early
part to consider. Otherwise each symbol in that early part has
occupation less than \(\kappa\). By (2) and the established
reference bounds \(.27<\Re r_j<.39\), it is unselected and its
real coordinate lies strictly between .22 and .45. Indeed a selected
symbol pays \(\kappa\), while a coordinate outside that interval
has clamped distance at least .05 from its reference and also pays
\(\kappa\).

Thus every sufficiently nearly optimal incoming history has all its
selected or transition symbols within its final \(3k_0\) positions.
This is stronger than a bound on their number: an isolated excursion
cannot occur arbitrarily far before the prescribed boundary state.
The early symbols can still move within the plateau; they are not
asserted to be exactly at their references.

## 3. A uniform exponential approximation

**Theorem 1.** For every integer \(k\ge0\), put \(h=3k+3\).
For every original word, layer and terminal state,
\[
 0\le H_i(v)-A_i^{[h]}(v)
       \le\frac{C^2}{a}\lambda^k\Psi_i(v).
 \tag{10}
\]
The constants are independent of the word length and terminal state.

**Proof.** Take the nearly optimal path used above. Prepend whole
baseline periods so that \(T\ge h\). This adds no occupation or
weight. Cut it at \(j=T-3k\), where \(j\ge3\). Replace its
prefix by the literal three-step entry to the same state \(v_j\).
The remaining \(3k\) transitions are unchanged. This gives a path
of length exactly \(h\) from the correctly aligned baseline to
\(v_T\).

The weight lost is at most
\[
 W_j-A_j^{[3]}(v_j)
       \le H_j(v_j)-A_j^{[3]}(v_j)
       \le D_j(v_j)\le C\Psi_j(v_j)\le CP_j.
 \tag{11}
\]
Unlike a reset of the three symbols, this replacement preserves the
boundary state exactly, including all three selections. Every weight
in the suffix is therefore literally the original weight. Combining
(9) and (11) gives
\[
 H_T(v_T)-A_T^{[h]}(v_T)
       \le\frac{C^2}{a}\lambda^k\Psi_T(v_T)
                                      +(1+C/a)\varepsilon.
\]
Let \(\varepsilon\) tend to zero. Neither the depth nor the terminal
state changes. This proves (10), including the baseline case.
\(\square\)

Thus a prescribed relative error \(e>0\) is achieved, for example, by
\[
 k=\left\lceil\frac Ca
         \max\left\{0,\log\frac{C^2}{ae}\right\}\right\rceil,
 \qquad h=3k+3.
 \tag{12}
\]
The estimate \((1-a/C)^k\le\exp(-ak/C)\) proves this claim.
This improves the earlier inverse-error depth bound to logarithmic
dependence on \(1/e\). The constants remain defined by compact local
bounds; (12) does not assert that their numerical values or a practical
small depth have been certified.

## 4. Consequences and limits

Choose \(e=\theta/6\) in (12), and define
\[
 V_i(v)=A_i^{[h]}(v)
                +\theta\left(\frac{\omega_{i-1}}6+
                                      \frac{\omega_i}3\right).
 \tag{13}
\]
The exact Bellman and gauge identities from the relative theorem give
\[
            w_i(v,v')\le V_{i+1}(v')-V_i(v)
                                      -\frac\theta6\Psi_{i+1}(v').
 \tag{14}
\]
No approximation error accumulates when (14) is summed over an open
chain. The new result supplies a better sufficient depth for the same
exact inequality, not an estimate for a new finite quantum kernel.

For every fixed \(\rho>0\) allowed by the hybrid contour, all the
arguments also hold on \([\rho,.5]\). Use the definitions and
proved inputs of the
[seam boundary reduction](research_mixed_seam_boundary_potential_reduction.md),
with \(K_{\rho,\theta}\) and
\(C_{\rho,\theta}=\max\{200,24000K_{\rho,\theta}\}\).
The bound for \(D\) close to the baseline is unchanged; away from
it the compact bound applies. Constants may depend on \(\rho\).

The argument handles primitive periods one and two by phase-aligned
padding on the integer-indexed path. Symbols that repeat a layer are
not identified. The three-symbol occupation in (6) and the original
edge incidences therefore keep their literal multiplicities.

None of (9)--(14) bounds the right-region or near-zero boundary
expressions involving \(V\). Their comparison with the available
source decay remains necessary before a full-period asymptotic can be
deduced. A lower bound for a physical boundary contraction, or stability
under arbitrary short partial fillings, does not follow here.

Reproduction:

```sh
python3 experiments/check_mixed_exponential_incoming_memory.py
```

The focused checker verifies the recurrence, geometric-error sum,
depth allocation and current source bindings. Prefix replacement and
cycle closure are the written arguments above, not claims supplied
by numerical sampling or by checking file hashes.
