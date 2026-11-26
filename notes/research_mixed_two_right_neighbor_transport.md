# Raising a coordinate between two right-half neighbors

This note proves one complete local inequality needed for the mixed
minimum-coordinate flow. Both immediate neighbors of the moving coordinate
are right-half coordinates, already fixed at \(1/2\) in the upper bound.
The moving coordinate may have either type and either permitted selection.
The proof covers its full interval \([.12,.22]\), rather than only the
face at its upper endpoint. It does not address a moving coordinate with
just one right neighbor, or a right coordinate two steps away.

## 1. The actual coordinate and its two incident edges

Put \(a=1/10\), \(b=11/50\), \(H=7/500\), and
\(r(t)=(t-a)/(b-a)=(t-.1)/.12\). Let \(\alpha\in\{0,1\}\)
be the type-four indicator of the moving coordinate, and let
\(\sigma\in\{0,\alpha\}\) be its selection. Its hybrid target is
\[
 z(t)=\begin{cases}
        t+icr(t),&\sigma=0,\\
        t+iH,&\sigma=1,
       \end{cases}
 \qquad .12\le t\le .22,
 \tag{1}
\]
where the fixed reference height satisfies
\[
 c\in[-.03,.02]\quad(\alpha=0),\qquad
 c\in[-.057,-.02]\quad(\alpha=1,\ \sigma=0).
 \tag{2}
\]
The right neighbors have height zero and left cutoff one. Thus (1) is
the literal hybrid target; no other target height changes when this
coordinate moves. In particular, \(c\) is a reference height, not the
current target height \(cr(t)\).

Let \(u_L,u_R\) denote the inner rows of the incoming and outgoing
raw edges. Their own-factorial indicators may differ. The complete
[row bracket](research_mixed_right_boundary_row_bracket.md) puts each
maximizing row in \((1/5,2/5)\), irrespective of those indicators.
Selections at the two real right endpoints have unit modulus and zero
directional derivative. Their actual Fourier weights remain in the
original source estimate.

Use \(g'(z)=\log(1-e^{-2\pi iz})\), with the original logarithm on
\(0<\Re z<1\). For \(q\in\{0,\sigma\}\), the sum of the two
target marginals is
\[
 K_q(z;u_L,u_R)=g'(z+u_L)+g'(z+u_R)
                 -(2+\alpha-q)g'(z)
                   +2\pi i(u_R+\sigma-q).
 \tag{3}
\]
Here \(q=0\) retains the factorial Fourier alternative and, when
selected, \(q=1\) retains the forcing alternative. Each edge allocates
one half of the moving vertex's Fourier weight. Its two allocations in
(3) therefore restore one full weight, including the selected monomial.
Only the outgoing edge has the moving coordinate as its first argument;
this accounts for the chirp \(2\pi i u_R\).

## 2. The local derivative inequality

For an unselected coordinate introduce the two switches
\(\chi\in\{0,1\}\) and set
\[
 D_{\chi,q}(t,c;u_L,u_R)
       =\Re\{(1+i\chi c/.12)K_q(z(t);u_L,u_R)\}.
 \tag{4}
\]
For a selected coordinate use only \(\chi=0\), so that the velocity
is exactly one and there is no height parameter. Taking the smaller
unselected value in (4) gives the horizontal derivative plus the
unfavorable part of its height derivative. This is the conservative
local quantity used in the minimum-flow criterion.

**Theorem 1.** On all domains (1)--(2), for every permitted branch
and switch, the two original row maxima satisfy
\[
       D_{\chi,q}(t,c;u_L^*,u_R^*)>\frac15.
 \tag{5}
\]
The statement is uniform in both neighboring types. It also includes
the case where the two right neighbors are the same physical vertex
of a two-cycle: its incoming and outgoing edges, and hence its two
row variables, remain distinct.

**Proof.** The [directional row theorem](research_mixed_raw_row_stationarity.md)
applies to each summand of (3). For every switch in (4), the real
velocity is one and the height velocity has absolute value at most
\(19/40\). Each row-dependent summand is concave on \([1/5,2/5]\).
Consequently
\[
 D_{\chi,q}(t,c;u_L^*,u_R^*)
 \ge \min_{u_L,u_R\in\{1/5,2/5\}}
                          D_{\chi,q}(t,c;u_L,u_R).
 \tag{6}
\]
All outer variables and the common height coefficient stay fixed in
this comparison. The two row maxima are not assumed equal. Neither a
complex critical equation nor a split using imaginary constants enters
(6).

It remains to check elementary logarithmic functions on three compact
rectangles: the two unselected \((t,c)\) rectangles in (1)--(2), and
the selected \(t\)-interval. Each has eight functions: four endpoint
row pairs and either two height switches or two Fourier branches.
The following formulas make the finite verification reproducible.
Write
\[
 B_q=g''(z+u_L)+g''(z+u_R)-(2+\alpha-q)g''(z),
 \qquad g''(z)=\pi\cot\pi z-\pi i,
 \qquad v=1+i\chi c/.12.
 \tag{7}
\]
For an unselected rectangle, the exact parameter derivatives are
\[
 \begin{split}
 \partial_t D_{\chi,0}
    &=\Re\{vB_0(1+ic/.12)\},\\
 \partial_c D_{\chi,0}
    &=\Re\{(i\chi/.12)K_0+vB_0\,ir(t)\}.
 \end{split}
 \tag{8}
\]
For the selected interval, \(\partial_tD_{0,q}=\Re B_q\).
All arguments stay in the regular strips
\(.12\le\Re z\le.22\) and \(.32\le\Re(z+u)\le.62\).
Thus these derivatives and the original logarithms are regular on
every box used below.

The accompanying checker encloses (3)--(8) with outward complex-ball
arithmetic. On each rational parameter box it takes the better of
direct interval evaluation and the midpoint lower bound minus the
full-box derivative bounds times the parameter radii. Each is a valid
lower bound by the ordinary real mean-value formula. A box is accepted
only when all eight lower bounds exceed \(1/5\).

Otherwise an exact binary split partitions one parameter interval.
The stored trees partition the three complete initial rectangles; a
saved replay reconstructs every box and recomputes every inequality.
It never accepts an old numerical bound as evidence. The selected
rectangle has a degenerate second interval, which is never split.
No floating optimizer or root proposal is used. The completed records
give (5) on all three closed domains, and (6) proves the claim for
the true row maxima. \(\square\)

## 3. Consequence and limitation

At a differentiable point of the actual unselected motion, the height
velocity is \(c/.12\), hence its derivative uses \(\chi=1\).
The stronger assertion for both switches also proves positivity of the
conservative local criterion. A selected motion uses \(\chi=0\).
At a tie of the two Fourier alternatives, the one-sided derivative
of their maximum is the larger of the active derivatives; (5) bounds
both. The endpoint assertions use one-sided velocities within the
stated interval.

Thus an isolated coordinate between two fixed right-half neighbors can
be raised from \(t\in[.12,.22]\) to \(.22\), increasing the mixed
upper rate by at least \((.22-t)/5\). This compares upper rates, not
finite kernel values. It proves no finite-source lower bound and does
not control the other local patterns needed for the complete mixed
minimum flow or for arbitrary short partial fillings.

Run the focused check with

```sh
python3 experiments/check_mixed_two_right_neighbor_transport.py
```

The saved record contains all trees, the final lower bounds and the
current proof and input bindings. Its replay option checks precisely
those trees at any requested higher precision.
