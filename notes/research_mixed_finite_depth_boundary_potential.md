# Uniform finite-depth approximation of the boundary potential

Research deduction, 5 November 2026. A fixed fraction of the proved
occupation loss is left unused. It gives a quantitative approximation
of the same incoming boundary potential at both ends of an open chain.
The principal bound, Corollary 2, has error \(40d^2\) at a depth
of order \(d^{-2}\), independent of the cyclic word length. The compact
constants below are defined explicitly but have not been numerically
evaluated; no interface sign or full-period source conclusion is asserted.

## 1. A local weight with unused occupation

Use the original phase, reference, symbols and four-coordinate weights
\(w_j\) from [the open-chain theorem](research_mixed_nonlow_open_chain_boundary.md).
All auxiliary symbols in this note range over the closed half-period
\([.1,.5]\), with selections \(\sigma_j\in\{0,\epsilon_j\}\).
The reference real part is \(a_j=\Re r_j\), with
\(.27<a_j<.39\). Use the proved occupation
\[
 \omega_j=\frac1{4000}\min\{1,\sigma_j+
   400(\operatorname{clamp}_{[.22,.45]}x_j-a_j)^2\}
          +\frac{(x_j-.45)_+}{10},
 \qquad 0\le\omega_j\le\frac{21}{4000}.
 \tag{1}
\]
Its original cyclic inequality is
\(\sum_jw_j\le-\sum_j\omega_j\), by
[the extracted-curvature corollary](research_mixed_extracted_plateau_curvature.md).
Fix any \(0<\theta<1\), and put
\[
 t_j^\theta=w_j+\frac\theta2(\omega_{j-1}+\omega_j).
 \quad\text{Thus}\quad
 \sum_jt_j^\theta\le-(1-\theta)\sum_j\omega_j.
 \tag{2}
\]
The inequality holds for every repetition of every original word, with
the same repeated actual reference. This is the proved pointwise phase
statement, not a consequence of an integral upper bound.

Let \(K_*\) be the compact local bound defined in Section 3 of
the open-chain theorem. We may use
\[
                  K_\theta=K_*+\frac{21\theta}{4000}
                  \quad\text{so that }|t_j^\theta|\le K_\theta.
 \tag{3}
\]
There is also a uniform Lipschitz constant \(L_\theta<\infty\)
in the sup norm of the four real coordinates, when their selections
and reference data are held fixed. The same constants work for all
types, references and word lengths.

For an explicit compact definition, let \(C_\phi\) bound each
first partial derivative of the original allocated phase on the
complete typed source products, let \(C_\Gamma\) bound each
reference tangent coefficient on the enclosing reference rectangles,
and let \(C_g\) bound \(|g'|\) on all the target polygons.
These suprema are finite because the established branches are
holomorphic on neighborhoods of their closed products. One may take
\[
 L_\theta=\max\left\{1,
 7\left[2C_\phi+2C_\Gamma+\max\{C_g,2\pi\}\right]
                 +\frac{17\theta}{125}\right\}.
 \tag{4}
\]
Indeed the right cutoff is Lipschitz 40, every left cutoff is
Lipschitz at most 50, and \(|c_j|\le.057\). A target changes
by at most \([1+.057(40+50)]\) times the sup change of its
three real inputs, which is less than 7. Taking a minimum, or the
maximum in the true selected Fourier correction, preserves these
Lipschitz estimates. Finally the clamp displacement in (1) is at
most .18, so a valid Lipschitz bound for \(\omega_j\) is
\(800(.18)/4000+1/10=17/125\). Its two half shares give the
last term of (4). No derivatives across a cutoff corner are required.
These comparisons follow the piecewise Lipschitz real-input segment;
its targets remain on the proved source domains. No straight complex
chord outside those domains is presumed.

## 2. The incoming potential and its finite versions

A state at layer \(i\pmod m\) is its last three symbols
\(v=(q_{i-2},q_{i-1},q_i)\). Appending \(q_{i+1}\) has
weight \(t_i^\theta\). A baseline symbol is \(p_j=(a_j,0)\).
Four baseline symbols have zero weight.

Let \(H_\theta(v)\) be the supremum of all finite incoming
path weights from the baseline state at layer zero to \(v\).
The anchored construction of the open-chain theorem applies to (2):
\[
 |H_\theta(v)|\le3K_\theta,\qquad
 H_\theta(\text{baseline at any layer})=0,\qquad
 t^\theta(v\to v')\le H_\theta(v')-H_\theta(v).
 \tag{5}
\]
For \(h\ge3\), define \(A_{\theta,i}^{[h]}(v)\) as the
maximum weight of length-h paths from the baseline at layer \(i-h\)
to \(v\). The initial triple and last three appended symbols are
fixed; the other \(h-3\) appended symbols are free. The maximum
exists on the compact product of the closed half-period and the
finite selection sets. Baseline padding proves
\[
 A_{\theta,i}^{[h]}(v)\le A_{\theta,i}^{[h+1]}(v)
                  \le H_\theta(v).
 \tag{6}
\]
Layer alignment in (5)--(6) uses zero-weight baseline paths and
integer repetitions of the reference word. It does not identify two
independent target symbols because their type labels have the same
primitive period.

**Theorem 1.** For \(0<d\le1/40\), set
\[
 B_d=\frac{10(6K_\theta+1)}{(1-\theta)d^2},\qquad
 M_d=\lfloor B_d\rfloor+1,\qquad h_d=3M_d+3.
 \tag{7}
\]
Then, simultaneously for all original words, references, layers and
states,
\[
              0\le H_\theta(v)-A_{\theta,i}^{[h_d]}(v)
                          \le6L_\theta d.
 \tag{8}
\]
In particular, for any requested error \(e>0\), choose
\(d=\min\{1/40,e/(6L_\theta)\}\). This gives an explicit
word-length-independent depth \(h_d\) and error at most \(e\).
The depth is \(O(e^{-2})\) with the fixed compact constants
(3)--(4).

**Proof.** Call a symbol bad if it is selected or
\(|x_j-a_j|\ge d\). Every bad symbol has
\[
                              \omega_j\ge d^2/10.           \tag{9}
\]
Inside the plateau this follows directly from (1). Outside it the
clamp is at distance greater than .05 from the actual reference,
so the same implication holds. A selected symbol costs at least
\(1/4000\), which is larger than \(d^2/10\) for our range of d.

Choose an incoming path of weight
\(W\ge H_\theta(v)-\varepsilon\), where \(0<\varepsilon<1\).
Prepend enough whole baseline periods that it has at least \(h_d\)
appended symbols; this changes neither its weight nor terminal state.
Append the three baseline exit symbols and then baseline steps until
the path closes at the original layer. If the exit weight is E, then
\(E\ge-3K_\theta\), while (5) gives
\(W\ge-3K_\theta-1\). The original cyclic inequality (2) gives
\[
 (1-\theta)\sum_{\text{appended path symbols}}\omega_j
                      \le6K_\theta+1.
 \tag{10}
\]
The closing symbols have zero occupation. The original path symbols
are counted once, including its final triple; all initial symbols are
baseline. Thus there are at most \(B_d\) bad symbols in the path.

If the final layer is i, partition the \(3M_d\) positions
\(i-3M_d-2,\ldots,i-3\) into disjoint consecutive triples.
They lie among the last \(h_d\) appended symbols and precede
the prescribed final triple. Since \(M_d>B_d\), some triple
has no bad symbol. Let j be its last layer. Then
\[
                      3\le i-j\le3M_d<h_d.                \tag{11}
\]
Its state \(v_j\) has no selections and is within distance d
of the baseline triple in the sup norm.

The weight of the discarded prefix is at most
\(H_\theta(v_j)\). Its three-step exit differs from the
zero-weight baseline exit in at most three weights, each by at most
\(L_\theta d\). The exit bound in the anchored construction
therefore gives \(H_\theta(v_j)\le3L_\theta d\).
Replace the starting triple of the remaining suffix by baseline and
keep every appended suffix symbol unchanged. Only its first three
weights can change, by a total of at most \(3L_\theta d\).
Because (11) leaves at least three appended suffix symbols, its
prescribed terminal triple is unchanged.

The modified suffix starts at baseline, ends at v, and has length
at most \(h_d\). Prepending baseline steps makes its length
exactly \(h_d\), with the correct starting layer. Hence
\(W\le A_{\theta,i}^{[h_d]}(v)+6L_\theta d\).
Let \(\varepsilon\) tend to zero. The same depth and constants
work for every \(\varepsilon<1\), proving (8). \(\square\)

This proof retains primitive periods one and two. The long path and
its closure have independent target symbols; only the coefficients
repeat. No unconstrained maximizer, attainment of \(H_\theta\),
or differentiability of the maximizing path is assumed.

**Corollary 2 (quadratic finite-depth error).** With the same
\(B_d,M_d\) as in (7), put \(h_d^{\rm q}=5M_d+3\). Then
\[
       0\le H_\theta(v)-A_{\theta,i}^{[h_d^{\rm q}]}(v)
                               \le40d^2.
 \tag{12}
\]
For error \(e>0\), the choice
\(d=\min\{1/40,\sqrt{e/40}\}\) gives error at most e and
depth \(O(e^{-1})\). This sharper error uses the proved plateau
Hessian bounds, rather than the unevaluated Lipschitz constant.

**Proof.** Repeat (9)--(10), but partition the \(5M_d\) positions
\(i-5M_d-2,\ldots,i-3\) into consecutive five-symbol blocks.
One block is entirely good. Cut after its third symbol, at layer j.
The suffix has length between 5 and \(5M_d\), so its final
prescribed triple is retained.

All five good symbols are unselected and lie in the plateau: their
real displacements from \(a\) are less than \(d\le1/40\).
Write these displacements as \(\Delta_k\). Their occupation is
exactly \(\omega_k=\Delta_k^2/10\), and every block with its
four-coordinate window in this five-symbol block has both targets at
their full reference heights. The existing local real Hessian bounds
\((1/5)I\le-\Re\phi''\le20I\) therefore give
\[
 -10(\Delta_{k-1}^2+\Delta_k^2)
 \le t_k^\theta
 \le-\left(\frac1{10}-\frac\theta{20}\right)
                         (\Delta_{k-1}^2+\Delta_k^2)\le0.
 \tag{13}
\]
Within these plateau windows, the left inequality also holds when
one or both symbols are baseline.

The three-step baseline exit from the good state at j has lower
bound \(-10(\Delta_{j-1}^2+2\Delta_j^2)\): its first edge
has both displacements, its second only \(\Delta_j\), and its
third has baseline endpoints and plateau halos, hence weight zero.
Thus the discarded prefix has weight
\[
                       W_{\rm prefix}\le H_\theta(v_j)
                                           \le30d^2.
 \tag{14}
\]
Replace the suffix's initial triple by baseline, keeping its appended
symbols fixed. Its first edge becomes zero, while its old weight was
nonpositive. Its second new edge is at least
\(-10\Delta_{j+1}^2\), while the old edge was nonpositive.
The third and all later weights are identical: the only remaining
modified halo coordinate stays in the plateau, where every left cutoff
equals one. This last assertion holds even if the next symbol after
the good block is bad; it changes neither of the compared third-edge
targets. Thus
\[
                    W_{\rm suffix}-W_{\rm modified\ suffix}
                                                    \le10d^2.
 \tag{15}
\]
Combine (14)--(15), pad the modified suffix with baseline steps to
length \(h_d^{\rm q}\), and let the near-optimal-path error tend
to zero. This proves (12). No optimization restricted to plateau
paths is assumed: only the five symbols at the chosen cut are good.
\(\square\)

## 3. The same potential at the two physical interfaces

Use the physical A/R partition, full raw right defects \(D_j\),
and A-run states \(v_l,v_r\) from
[the interface reduction](research_mixed_nonlow_interface_reduction.md).
For a run \(I=[l,r]\), put
\[
 \Omega_I=\sum_{j=l}^r\omega_j-\frac{\omega_l+\omega_r}{2}
            \ge0.
 \tag{16}
\]
A singleton has \(\Omega_I=0\) and \(v_l=v_r\).
The original coherent AA weights satisfy
\[
 \sum_{j=l+1}^r w_j
       \le H_\theta(v_r)-H_\theta(v_l)-\theta\Omega_I.
 \tag{17}
\]
Thus an entrance is adjusted by \(-H_\theta\), and an exit by
\(+H_\theta\). These are values of one and the same incoming
potential, not two independently optimized closing costs.

Choose h from Theorem 1 or Corollary 2 so that
\(0\le H_\theta-A_\theta^{[h]}\le e\). Then
\[
 \sum_{j=l+1}^r w_j\le
 A_\theta^{[h]}(v_r)-A_\theta^{[h]}(v_l)
                         +e-\theta\Omega_I.
 \tag{18}
\]
For a singleton the two finite potential values cancel exactly and
the error e may be omitted. Consequently, for a mixed cycle, its
full finite allocated product has upper exponent
\[
 M+\sum_{j\text{ incident to R}}D_j
  +\sum_I\{A_\theta^{[h]}(v_r)-A_\theta^{[h]}(v_l)}
  +e\,n_{A,\ge2}-\theta\sum_I\Omega_I+\delta,
 \tag{19}
\]
with its original fixed-word polynomial prefactor. Here
\(n_{A,\ge2}\) is the number of A-runs of length at least two,
and \(\delta>0\) is one freely chosen total finite-source tolerance.
Every physical source, Fourier halfweight and complex tangent appears
once, as in the interface reduction. No source tolerance is charged
to a potential or a virtual connector.

For example, define the finite adjusted R-component function
\[
 J_{s,t}^{[h]}=\sum_{j=s}^{t+1}D_j
      +A_\theta^{[h]}(v_{\rm left\ exit})
      -A_\theta^{[h]}(v_{\rm right\ entry})
 \tag{20}
\]
for a maximal R-run \([s,t]\). The sum of (20) is precisely
the raw-defect sum and potential-difference sum in (19).
Let \(n_R\) be the number of
maximal R-runs. If a future finite-window comparison
proved \(J_{s,t}^{[h]}\le-\eta\) for every R-component, with
\(\eta>e\), then (19) would give a strict mixed-cycle rate gap
at least \((\eta-e)n_R\) before the final tolerance, because
\(n_{A,\ge2}\le n_R\). Long R-components can be truncated in
such a verification by their already proved internal RR losses and
explicit interface ceilings, as described in the interface note.

The remaining occupation in (19) may instead be retained in a sharper
component budget. Equations (19)--(20) are sufficient comparison
criteria, not established signs. Their finite potential approximation
is uniform in word length; the required h depends on the constants
and desired error, not on that word.

Using the same incoming potential is essential. The limiting incoming
maximum is \(H_\theta\), whereas an independently optimized exit
cost need not have limit \(-H_\theta\). A nonreference state can
retain a strictly dissipative barrier between the two. The six- or
four-cost bounds remain valid, but improving their two sides separately
need not remove this slack. The paired use in (17)--(20) avoids that
extra relaxation.

The result is structural. It evaluates neither \(K_*\), the local
derivative suprema, nor the finite functions in (20). It proves no
positivity or nonzero coefficient of an open source, no joint
word-length/level asymptotic, and no full nonlow-period or knot theorem.

```sh
python3 experiments/check_mixed_finite_depth_boundary_potential.py
```

The focused checker validates the rational loss coefficients, arbitrary-
length cut indices, and current lower/upper Hessian, reference and
half-period source bindings. It does not evaluate the compact constants,
optimize a potential, or rerun the inherited interval covers.
