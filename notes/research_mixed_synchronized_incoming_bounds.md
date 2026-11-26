# Finite comparisons of incoming histories

Research deduction, 5 November 2026. These bounds compare two terminal
states by changing the end of the same history. They give explicit
finite upper bounds for the already constructed incoming potential;
they do not certify a uniform right-interface sign. All source and
contour results cited below remain unchanged.

## 1. The common history and its finite tail

Fix an original periodic type word and its actual geometric reference.
Use the triple states, original allocated weights \(w_i\), occupation
\(\omega_j\), and incoming potential \(H_i\) of the
[exponential incoming-memory theorem](research_mixed_exponential_incoming_memory.md).
Thus
\[
 t_i=w_i+\frac\theta2(\omega_{i-1}+\omega_i),\qquad
 0<\theta<1,\qquad H_i(p_i)=0,\qquad
 p_i=((\Re r_{i-2},0),(\Re r_{i-1},0),(\Re r_i,0)).
 \tag{1}
\]
One may use either the alphabet \([.1,.5]\), or its already proved
extension \([\rho,.5]\) for fixed \(0<\rho\le.001\). All
symbols have their permitted selections, and all targets are generated
by the same row-dependent hybrid cutoffs. References and types extend
periodically, but different target symbols are not identified.

For a predecessor state \(u\) at layer \(i-3\), let
\(C_i(u,v)\) be the total \(t\)-weight of the unique three-step
path obtained by appending the three letters of the terminal state
\(v\) at layer \(i\). Put
\[
 B_i(v)=\max_u\{C_i(u,v)-C_i(u,p_i)\}.
 \tag{2}
\]
This maximum ranges over three real predecessor symbols and their
allowed selections. It is a finite compact maximum of the original
phase expressions, with their complete selected corrections. In
particular \(B_i(p_i)=0\).

**Proposition 1.** For every terminal state,
\[
                  A_i^{[3]}(v)\le H_i(v)\le B_i(v).
 \tag{3}
\]
The lower inequality is the existing literal-entry bound. For the
upper inequality, take any incoming history ending at \(v\), padding
its beginning by baseline periods if necessary so its last three
transitions are present. If \(W\) is the prefix weight and \(u\)
its state before those transitions, replacing only the final three
appended letters by \(p_i\) gives another admissible incoming history.
Its weight is \(W+C_i(u,p_i)\le H_i(p_i)=0\). Hence the original
weight is at most \(C_i(u,v)-C_i(u,p_i)\). Take the supremum over
histories and then the finite maximum in (2). No finite-depth
approximation error or independent exit connector is used.

There is a modest additional occupation reserve. Closing the common
prefix by its three baseline letters counts every prefix occupation
once. If \(\Psi(u)\) is the sum of its last three occupations, the
cyclic occupation inequality therefore gives
\[
 H_i(v)\le
 \max_u\{C_i(u,v)-C_i(u,p_i)-(1-\theta)\Psi(u)\}.
 \tag{4}
\]
The full prefix has at least this much occupation; (4) discards the
remaining nonnegative terms. The case of an initially short history
again follows by baseline padding. These are phase inequalities, not
lower bounds on a finite kernel.

## 2. A direct difference of two incoming potentials

Let the left terminal state \(v\) be at layer \(i\), and the right
terminal state \(z\) at layer \(i+d\), where \(d\ge0\). For
each predecessor \(u\) at layer \(i-3\), let
\(C_{i,d}^{\rm right}(u,z)\) be the maximum weight of all
\(d+3\)-step paths from \(u\) to \(z\). The first \(d\)
appended symbols are free and the last three are the prescribed
terminal symbols. Then
\[
 H_i(v)-H_{i+d}(z)
 \le\max_u\{C_i(u,v)-C_{i,d}^{\rm right}(u,z)\}.
 \tag{5}
\]
Indeed retain the common prefix of any incoming history to \(v\)
and append a maximizing right tail instead of its final three letters.
The resulting incoming weight is at most \(H_{i+d}(z)\). Subtraction
and passage to a supremum prove (5). The right-tail maximum exists
by compactness. Replacing that maximum by the weight of any explicitly
specified admissible right tail gives a weaker but still valid upper
bound. Thus lower trial values are usable on the right side of this
comparison, provided the remaining outer maximum is bounded above.

For a right run \([s,t]\) in the
[full-period interface reduction](research_mixed_nonlow_interface_reduction.md),
the left-exit layer is \(i=s\), the right-entry layer is \(t+2\),
and \(d=t-s+2\). Consequently the right tail in (5) has length
\(t-s+5\). An isolated right coordinate needs a five-step right
tail with two free symbols. This is a fixed finite comparison for a
bounded run, not a numerical claim about its sign.

The same-history argument is valid for primitive periods one and two.
Only reference phases are aligned periodically; free appended symbols
at repeated layers remain distinct. It never identifies two different
physical edges or adds a new factor to the original integrand.

## 3. An acute upper bound at a real low terminal coordinate

There is a useful specialization of (3) which removes the predecessor
optimization altogether. Let the three terminal reference coordinates
be \(a=r_{i-2}, b=r_{i-1}, c=r_i\), with type indicators
\(\alpha,\beta,\gamma\). Consider
\[
 v=((\Re a,0),(x,\sigma),(\Re c,0)),\qquad
 \rho\le x\le.1,
 \tag{6}
\]
where \(\sigma\) is permitted by type \(\beta\). In the alphabet
\([.1,.5]\), this means \(x=.1\). Put
\[
 h_a=\Im a,\quad \vartheta_a=\pi(1/2-\Re a),\quad
 P_a=\phi_{\alpha\beta,a}(a,b),\quad
 W_{\alpha\beta}(\Re a,x)
   =f_{\alpha\beta}(\Re a,x)-\Re\Gamma_{\alpha\beta}(\Re a,x),
 \tag{7}
\]
where \(f=\Re\phi\) on real arguments and \(\Gamma\) is the
original complex tangent at \((a,b)\). Define the explicit fee
\[
 Q_a=\max\left\{0,
     h_a\left(\Im P_a-\frac\alpha2\vartheta_a\right)
                      +\frac\pi2(-h_a)_+\right\}.
 \tag{8}
\]
**Proposition 2.** Every incoming history to (6) satisfies
\[
 H_i(v)\le W_{\alpha\beta}(\Re a,x)+Q_a
                                      +\frac\theta2\omega_{i-1}(x,\sigma).
 \tag{9}
\]

To prove it, compare the two three-step tails in (2). Their first
transition agrees, because their first appended symbol is the same
baseline symbol. Let \(z\) be the preceding target. It is the same
in both tails. In the tail ending at \(p_i\), the first terminal
coordinate is \(a_h=\Re a+ih\), with \(h\) between zero and
\(h_a\); the middle coordinate is exactly \(b\). In the tail
ending at \(v\), both coordinates are real, because \(L_b(x)=0\)
for both row cutoffs. The last two coherent phase differences are
\[
 \Re\phi_{\eta\alpha}(z,\Re a)
       -\Re\phi_{\eta\alpha}(z,a_h)
       +f_{\alpha\beta}(\Re a,x)
       -\Re\phi_{\alpha\beta}(a_h,b).
 \tag{10}
\]
The preceding endpoint's selected correction cancels. The middle
selected correction vanishes on the real half-period, and the first
terminal coordinate is unselected. The two original tangent
derivatives at \(a\) sum to zero by actual cyclic stationarity.
The only remaining tangent change is the last edge's derivative at
\(b\). The occupation change in these incoming transitions is
exactly \(\theta\omega_{i-1}/2\).

Vertical convexity at the original reference gives
\[
 \Re\phi_{\alpha\beta}(a_h,b)
 \ge \Re\phi_{\alpha\beta}(a,b)-\Im P_a(h-h_a).
 \tag{11}
\]
For the preceding edge, supporting at its real second endpoint and
using the [acute gradient theorem](research_mixed_acute_gradient_height_transfer.md)
gives
\[
 \Re\phi_{\eta\alpha}(z,\Re a)
       -\Re\phi_{\eta\alpha}(z,a_h)
 \le -\frac\alpha2\vartheta_a h+\frac\pi2(-h)_+.
 \tag{12}
\]
This holds for arbitrary preceding selections and admitted complex
targets \(z\). A preceding real deep-low target is also covered by
the acute real half-period theorem. Combining (10)--(12), including
the tangent terms just described, bounds the tail difference by
\[
 W_{\alpha\beta}(\Re a,x)
 +h\left(\Im P_a-\frac\alpha2\vartheta_a\right)
 +\frac\pi2(-h)_++\frac\theta2\omega_{i-1}.
 \tag{13}
\]
On the interval between zero and \(h_a\), the maximum of the
height expression is exactly (8). Proposition 1 proves (9). The
reference tangent, its imaginary part and its cyclic incidence are
essential; replacing them by a plane at unrelated reference data
would not justify the cancellation.

## 4. Original source use and the bounded diagnostic

For an A-run, the original phase bound uses the same \(H\) at both
ends. Hence an R-component can be bounded by its complete raw defects
plus (5), or more coarsely by its raw defects plus \(B\) at the left
exit minus a literal incoming value at the right entry. The unused
AA occupation remains nonnegative. All finite-source tolerances are
spent only on physical edges, exactly as in the existing interface
reduction. No auxiliary path is a new finite kernel factor.

The archive
[`2026-11-05-right-short-connectors`](../repro/diagnostics/2026-11-05-right-short-connectors/README.md)
records two fixed configurations at the original alternating reference.
Depth-four and depth-five independent entry/exit optimization barely
improves the already positive three-step proxy. The synchronized
two-symbol upper-envelope diagnostic is instead close to the incoming
trial value. Formula (9) gives a somewhat larger, but explicit,
phase upper bound at those terminal states. These numerical values are
floating diagnostics only: neither their outer maxima nor the raw row
maxima have been certified outward. No uniform R-interface inequality,
full-period asymptotic or enlarged knot-family result follows here.
