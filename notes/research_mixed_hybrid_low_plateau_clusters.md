# Low and plateau coordinates on the periodic hybrid contour

Research theorem, 5 November 2026. This controls the closed low/plateau
region on the periodic hybrid itself. Near-zero coordinates need not
reset their neighbors completely. The proof retains those partial
heights and all original selections. Transition and right-region
coordinates are not included in this theorem.

## 1. One fixed collar and the literal finite source

Put
\[
 L=[0,1/10],\qquad P=[11/50,9/20],\qquad H=7/500.
 \tag{1}
\]
Use the exact periodic graph in
[the split-cutoff hybrid theorem](research_mixed_split_cutoff_hybrid_contour.md),
equations (2)--(4), separately for each original selected subset.
Choose its collar width \(\varepsilon\) once, independently of \(N\),
so that
\[
 0<\varepsilon\le1/1000
 \tag{2}
\]
and the complete
[all-endpoint theorem](research_mixed_all_endpoint_support.md), together
with its [remaining orientation](research_mixed_43_endpoint_support.md),
has finite gap at least \(d=1/4000\) whenever one argument is real
in \([0,\varepsilon]\). The other argument may have any real angle
and any of its full physical typed heights. Such a positive width
exists: the endpoint theorem has gap \(1/2000\), and its uniform
raw-product thickening cost tends to zero. There are finitely many
types, orientations and selections. No claim that this radius equals
\(1/1000\), or any level-dependent choice of radius, is needed.

For a fixed real target, partition its low vertices disjointly as
\[
 S=\{j:0\le x_j\le\varepsilon\},\qquad
 D=\{j:\varepsilon<x_j\le1/10\}.
 \tag{3}
\]
The convention at \(\varepsilon\) is literal; changing it on that
measure-zero face would not change the integral. Every low target has
height zero. A vertex in \(D\) also resets both neighboring heights
to zero. A vertex in \(S\) can leave either neighbor at any fraction
of its prescribed height. On \((L\cup P)^m\), each plateau height
is therefore \(t_jc_j\), where \(0\le t_j\le1\), and
\(c_j=\Im r_j\) if unselected, \(c_j=H\) if selected. If no low
incidence meets that vertex then \(t_j=1\).

Write \(B_{e,N}\) for the original allocated nonnegative block
modulus, including its two actual Fourier halfweights and selected
monomials. Multiplication restores the literal integer weights.
Let \(\Gamma_e\) be its full complex tangent at the actual critical
reference, and let \(M\) be the real part of the original critical
action. All incidences are retained before identifying variables;
in particular
\[
                       \Re\sum_e\Gamma_e=M.
 \tag{4}
\]
There is one original edge for a one-cycle and two parallel original
edges for a two-cycle.

## 2. A common plateau cost for every partial selection

Call a plateau endpoint affected if it has a low incidence. For a
\(PP\) edge, let \(A_e\) be its affected endpoint incidences. Then,
for every fixed \(\tau>0\), uniformly on the indicated hybrid box,
\[
 B_{e,N}\le C_\tau N^A
   \exp N\left\{\Re\Gamma_e+
                10\sum_{j\in A_e}(\Im r_j)^2+\tau\right\}.
 \tag{5}
\]
Both real target coordinates may readjust throughout \(P\).

Here is the branchwise justification. For each selection and each
actual Fourier alternative use
\[
 \psi_f(z)=\phi(z)+\sum_{j=0}^1
       \{f_jg(z_j)/2+\pi i(\sigma_j-f_j)z_j\}.
 \tag{6}
\]
The whole right-square source and its positive Schur Hessian imply
convexity of \(\Re(\psi_f-\Gamma_e)\) in each target height.
For selected branches this is also the explicit
[selected right-taper curvature lemma](research_mixed_selected_right_taper_support.md),
Lemma 2. For the unselected branch it is the full-height-reset
accretivity input. Interpolate successively in each affected endpoint:
its two corners are zero and its prescribed height, either the
reference height or \(H\). Unaffected endpoints stay prescribed.

At a corner with a selected height \(H\), the
[selected plateau](research_mixed_selected_plateau_support.md) or
[selected/reset](research_mixed_selected_reset_plateau_support.md)
comparison gives a negative defect. A selected endpoint at height
zero adds either zero or \(\Re g(x)/2<0\) to the unselected phase.
At every remaining corner, the
[full matrix reset bound](research_mixed_full_height_reset.md)
gives at most \(10\sum c_j^2\) over endpoints reset to zero.
The corner with no reset is bounded by its own plane. These corner
bounds are all at most the right side of (5) without \(\tau\).
Height convexity proves that same coarse ceiling for every partial
height, including two partial selections. This is a bound for each
branch; it does not assume the maximum of the branches is holomorphic.

The complete conditional packet is uniform on this compact plateau
product. The actual Fourier-polynomial upper bound contributes any
chosen \(\tau>0\); it retains its forcing alternative at positive
selected heights. This proves (5) for the original finite functions.
The more precise formulas in
[partial selected heights](research_mixed_partial_selected_heights.md)
are consistent with, but are not needed in place of, this common ceiling.

## 3. Fractional allocation of every seam pair

Let \(E(S)\) be the set of original edges having at least one endpoint
in \(S\). For \(j\in S\), the
[complete seam-pair theorem](research_mixed_hybrid_zero_pair_support.md),
Corollary 2, gives
\[
 B_{j-1,N}B_{j,N}
 \le C N^A\exp N\{\Re(\Gamma_{j-1}+\Gamma_j)-Q_j-G\},
 \qquad G=1/5,\quad Q_j\ge0.
 \tag{7}
\]
This remains an actual finite inequality when the two incidences are
the same original loop. It also holds for the sum of absolute rows.
No interpretation of \(Q_j\) as a bound for exterior blocks is used.

Take every inequality (7) to power \(1/2\). An edge with \(k_e\)
seam endpoint incidences receives exponent \(k_e/2\), with
\(k_e=1\) or \(2\) on \(E(S)\). Supply its remaining exponent
\(1-k_e/2\) using the direct endpoint bound from Section 1.
All factors are nonnegative, so this multiplication requires neither
division by a kernel nor a nonvanishing assumption. Since
\(\sum_{e\in E(S)}k_e=2|S|\), the result is
\[
 \prod_{e\in E(S)}B_{e,N}
 \le C_mN^{A_m}\exp N\left\{
   \Re\sum_{e\in E(S)}\Gamma_e
   -\frac{|S|}{10}-d(|E(S)|-|S|)-\frac12\sum_{j\in S}Q_j
                         \right\}.
 \tag{8}
\]
In a degree-two cycle, \(|E(S)|\ge|S|\). Thus the last two
terms are nonpositive and may be dropped. This allocation includes
adjacent seam vertices and overlapping pairs without counting an
original source edge twice.

Every remaining low edge is \(DP\), \(PD\), or \(DD\).
The first two have both heights zero, and the
[uniform real low-source theorem](research_mixed_uniform_real_low_support.md)
gives loss \(1/20\). The
[closed both-low raw theorem](research_mixed_both_low_raw_support.md)
gives loss \(1/100\) on \(DD\). The selected frequency monomials
at these real coordinates have modulus one; the actual Fourier
polynomial weights remain in the stated source bounds. Edges between \(D\) and \(S\)
already belong to \(E(S)\) and are not used a second time.

## 4. The incidence budget

Let \(n_{SP}\), \(n_{DP}\), and \(n_{DD}\) count the indicated
original edges, combining the two orientations. A plateau vertex
with \(k\) low incidences has \(2-k\) plateau incidences. If it
is affected, \(k\in\{1,2\}\), and \(2-k\le k\). Assign each
possible plateau-endpoint charge to a distinct adjacent low incidence.
For \(k=1\) this uses its unique low edge; for \(k=2\) there is
no plateau edge to charge. Thus
\[
 10\sum_{e\text{ of type }PP}\sum_{j\in A_e}(\Im r_j)^2
 \le a(n_{SP}+n_{DP}),\qquad
 a=10(57/1000)^2=3249/100000.
 \tag{9}
\]
The rule counts endpoint incidences of a doubly affected \(PP\)
edge separately. It does not assume that an edge with no low endpoint
has unchanged heights. Also \(n_{SP}\le2|S|\).

Combining (5), (8), and the other low-edge bounds leaves, before the
plateau tolerances, the following loss:
\[
 \begin{split}
 \frac{|S|}{10}+\frac{n_{DP}}{20}+\frac{n_{DD}}{100}
       -a(n_{SP}+n_{DP})
 &\ge \frac{1751}{50000}|S|
       +\frac{1751}{100000}n_{DP}+\frac1{100}n_{DD}.
 \end{split}
 \tag{10}
\]
If a low vertex is present, either \(S\ne\varnothing\), or a
\(DP\) or \(DD\) edge is present. Hence (10) is at least
\(1/100\). Choose one tolerance \(0<\tau_m<1/(200m)\) for
every plateau block. Their total costs less than \(1/200\).
All the low-edge and pair bounds used above were already finite-source
bounds; their rounded gaps are not charged another Fourier tolerance.

For a one-cycle, a low loop has two low endpoint incidences. If it is
a seam loop, (7) bounds the square of its one source block and its
half-power restores that block. If it is a deep-low loop, use the
\(DD\) bound. There is no plateau reset cost. In a mixed two-cycle,
the plateau vertex has two low incidences and no \(PP\) edge. Its
two parallel edges remain distinct throughout (8)--(10). These
observations also verify the repeated-incidence cases of the general
degree-two argument.

## 5. Restricted original integral and scope

**Theorem 1.** On the exact periodic hybrid with any sufficiently small
fixed collar satisfying (2) and Section 1, every original selected
density on \((L\cup P)^m\setminus P^m\) has the uniform bound
\[
 |\mathcal D_{N,S_0}(x)\det(I+iD\mathcal H_{S_0}(x))|
              \le C_mN^{A_m}e^{N(M-1/200)}.
 \tag{11}
\]
Here \(S_0\) is the selected subset, distinct from the seam set
\(S\). Both level parities and every approach to a zero coordinate
are included. The graph Jacobian is bounded for this fixed collar
by the hybrid theorem; it has no exponential cost. The original unit
factor has modulus one, and all original scalar powers of \(N\)
are included in the polynomial factor.

On \(P^m\) the graph is exactly the previously proved constant-height
plateau graph for every selection. Its nonempty selections have the
existing finite gap \(1/200\). Therefore the sum of the original
selected integrals on \((L\cup P)^m\) differs from the unselected
plateau integral by \(O(N^A e^{N(M-1/200)})\). It retains the same
nonzero central coefficient and cyclic power \(N^0\).

This statement concerns this restricted region of the hybrid, not an
unmatched older low-region graph. Configurations with a real coordinate
in \((.1,.22)\) or \((.45,1]\) are still outside it. In particular,
the proof supplies no universal reset bound for a transition or right
exterior block, and no whole-period or knot-volume conclusion.

```sh
python3 experiments/check_mixed_hybrid_low_plateau_clusters.py
```

The checker verifies the complete current source inputs and the exact
loss, corner and incidence arithmetic. The written degree-two argument,
not finite enumeration of cyclic words, proves arbitrary length.
