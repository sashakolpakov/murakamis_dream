# A uniform incoming bound at a low terminal coordinate

Research deduction, 5 November 2026. An unused part of the established
real one-small bound strengthens the cyclic occupation inequality.
It then bounds the incoming potential for a general terminal triple
\((a,x,\text{baseline})\) with \(x\le.1\), without optimizing
any predecessor symbols. This does not assert the remaining uniform
right-interface sign.

## 1. Retaining the one-small surplus

Use the actual periodic reference \(r\), original residual weights
\(w_j\), and the proved occupation
\[
 \omega_j=\frac1{4000}\min\{1,\sigma_j+
  400(\operatorname{clamp}_{[.22,.45]}(x_j)-\Re r_j)^2\}
                    +\frac{(x_j-.45)_+}{10}.
 \tag{1}
\]
Fix \(0<\rho\le.001\), and let all real symbols lie in
\([\rho,.5]\) on the original hybrid graph. Put
\(c_j=\Im r_j\), and mark the positions
\(L=\{j:x_j\le.1\}\). An edge \(j\) joins \(j-1,j\).
For an edge incident to \(L\), define
\[
 b_j=\begin{cases}
  9/200,&j-1,j\in L,\\
  9/200-(11/2)c_j^2,&j-1\in L,\ j\notin L,\\
  9/200-(151/20)c_{j-1}^2,&j\in L,\ j-1\notin L.
 \end{cases}
 \tag{2}
\]
All these quantities are positive: the largest possible charge is
\((151/20)(.057)^2=.02452995<.045\).

**Proposition 1.** For every cyclic type word and every original
selection,
\[
          \sum_jw_j\le-\sum_j\omega_j-
                    \sum_{j:\{j-1,j\}\cap L\ne\varnothing}b_j.
 \tag{3}
\]
The sum counts each original edge once, including loops and the two
parallel edges of a two-cycle.

**Proof.** First raise each coordinate in \([\rho,.1]\) to .1
using the [deep-low phase comparison](research_mixed_deep_low_half_region.md).
This preserves every height and does not decrease the complete rate.
It also preserves (1), the marked set \(L\), and all constants (2).

Apply exactly the subsequent right-clamping and fixed-early transport
used in the [occupation proof](research_mixed_nonlow_occupation_loss.md),
with its [improved constant](research_mixed_extracted_plateau_curvature.md).
Every marked coordinate remains .1. Right clamping and selection
removal operate only above .45; the later transport leaves all early
coordinates in \([.1,.12]\) fixed. At the final configuration every
edge incident to a marked coordinate has both heights zero. Its true
selected correction is zero, and the
[real one-small phase comparison](research_mixed_real_one_small_support.md)
therefore gives its original residual strictly below \(-11/200\).
The comparison at a real half endpoint follows either from its affine
certificate and the closed half-endpoint phase, or by continuity.

In the [early/plateau charge proof](research_mixed_early_plateau_clusters.md),
an early edge is allotted loss \(1/100\). If its other endpoint is
a plateau endpoint requiring an adjoining reset credit, it is also
allotted \(q c^2\), where \(q=11/2\) when the early endpoint
is first and \(q=151/20\) when it is second. The stronger real
bound supplies in addition
\[
                    \frac{11}{200}-\frac1{100}-q c^2
                           =\frac9{200}-q c^2.
 \tag{4}
\]
If both endpoints are early, no plateau credit is assigned; its full
additional loss is \(9/200\). When the other endpoint is early
but unmarked, (2) merely reserves an unnecessary nonnegative credit,
so it remains a valid smaller surplus. Fixed isolated vertices between
two early vertices also have no plateau incidence; the same reasoning
applies to them.

Retain these surpluses without changing any reset allocation. The
original exact early reserve remains
\[
 \frac{6349}{4000000}n_E>\frac5{4000}n_E,
 \tag{5}
\]
which still pays the occupation of every vertex within distance two
of the early set. Clean plateau edges retain their original independent
losses, paying all remaining occupations. The gain from right clamping
still pays the last term of (1). Thus the complete original occupation
argument proves (3) with the extra edge losses (2) left unused. No
local derivative or reset estimate has been strengthened by assumption.
The earlier incidence proof already retains loops and parallel edges;
the marked-edge sum also uses that convention. \(\square\)

## 2. A general low terminal state

Fix \(0<\theta<1\), write \(a_\theta=1-\theta\), and use
the incoming potential for
\(t_i=w_i+\theta(\omega_{i-1}+\omega_i)/2\), normalized to
zero on every baseline state. Consider a terminal state at layer \(i\),
\[
 v=((y,\tau),(x,\sigma),(\Re r_i,0)),\qquad
 \rho\le y\le.5,\quad \rho\le x\le.1,
 \tag{6}
\]
with all permitted selections \(\tau,\sigma\). The first symbol
is arbitrary; it need not be a reference or a plateau symbol. Let
\(E_i^{[3]}(v)\) be the weight of appending three baseline symbols,
and let \(\Psi_i(v)\) be the sum of the three terminal occupations.
Put
\[
 \Delta_i=\frac9{100}-\frac{151}{20}c_{i-2}^2
                              -\frac{11}{2}c_i^2.
 \tag{7}
\]
The uniform typed-height bounds give
\[
 \Delta_i\ge .04760055,
 \qquad
 \Delta_i\ge .078255\quad
          \hbox{if both neighboring types are three}.
 \tag{8}
\]

**Theorem 2.** Uniformly over every incoming history to (6),
\[
 H_i(v)\le -E_i^{[3]}(v)-a_\theta\Psi_i(v)-\Delta_i.
 \tag{9}
\]
Append the three baseline exit symbols to any such history and add
baseline steps to align the period. Baseline padding can ensure that
the terminal low position and its two incident edges are distinct in
this repeated cycle, even when the primitive period is one or two.
The marked terminal position contributes the two surpluses whose sum
is at least (7). If its preceding neighbor is itself low, the left
surplus is \(9/200\), which only improves this lower bound. All
other marked-edge surpluses are nonnegative and may be discarded.
Equation (3) then gives the closed \(t\)-weight at most
\(-a_\theta\sum\omega-\Delta_i\). The path occupation contains
the whole terminal triple, proving (9) after taking a supremum.

The exit in (9) is particularly simple. Its first appended baseline
coordinate has height zero, because its neighbor is the fixed low
coordinate \(x\). All subsequent baseline rows are full reference
rows. Consequently
\[
 E_i^{[3]}(v)=
 w_i(x,\Re r_i)
 +w_{i+1}(\Re r_i,r_{i+1})
                  +\frac\theta2\omega_{i-1}(x,\sigma).
 \tag{10}
\]
In (10), the displayed arguments specify the two actual targets in
each edge: the first edge is wholly real, and the second has its first
argument real and its second at the complex reference. Each \(w\)
includes its original complex tangent subtraction. The third exit
edge is at its reference and has zero weight. Formula (10) is
independent of \(y,\tau\); they remain only in the favorable
\(-a_\theta\Psi_i(v)\) term of (9). Selected factors at \(x\)
have unit modulus and their true \(\chi\) correction is zero.

## 3. The resulting right-interface criterion

For a right component whose left A endpoint is low, use (9) at its
left-exit state and any literal incoming path at its right-entry state.
Its exact common-potential expression is bounded above by
\[
 \sum_{j\text{ in the component}}D_j
      -E_i^{[3]}(v)-A_{\rm right}^{[h]}(z)
      -a_\theta\Psi_i(v)-\Delta_i,
 \tag{11}
\]
before subtracting the already available AA occupation shares.
Here the \(D_j\) are the full original raw right-incident defects,
not coherent phases at right arguments. A lower trial for the literal
right incoming maximum is sufficient if all other terms are bounded
rigorously. Every reference term and selected Fourier branch remains.

Equation (11) improves the failed independent-entry/exit relaxation
by a uniform positive amount. It is valid for arbitrary first terminal
real coordinates and their selections, all word lengths, and all
histories in the fixed half-period alphabet. It does not establish
that (11) is negative for every right-interface state. A quantitative
comparison of its explicit right source and finite connector functions
remains necessary. No finite-source monotonicity, full-period
asymptotic, or new knot-family theorem is asserted here.

Reproduction:

```sh
python3 experiments/check_mixed_low_terminal_incoming_bound.py
```

The focused checker verifies the exact ordered surplus arithmetic and
the current completed source/proof bindings. The transport, retained
charge, and incoming-closure implications are the written argument;
no numerical cover or incoming optimization is rerun.
