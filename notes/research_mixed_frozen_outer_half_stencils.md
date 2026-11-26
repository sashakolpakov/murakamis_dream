# Frozen adjacent heights when the moving center has no early neighbor

Research note, 4 November 2026. This is a local phase-derivative result.
It supplies fifty additional half-stencil inequalities for a moving
center with no early neighbor. All earlier source and half-stencil
artifacts are unchanged. The class with exactly one early neighbor is
separate.

Use the frozen sets \(B,I,A\) and derivative coefficients \(d_j\) of
[the frozen-early transport reduction](research_mixed_frozen_early_transport.md).
Fix a moving minimum \(i\in A\), with \(t=x_i\in[.12,.22]\),
and assume \(\{i-1,i,i+1\}\cap B=\varnothing\). Put
\(r_t=(t-.1)/.12\) and \(H=7/500\). The center has one of the
three states in the
[constant-selected half-stencil note](research_mixed_constant_selected_height_transport.md):
its actual height is \(r_tc_i\), with derivative coefficient \(c_i\),
or it is selected, with actual height \(H\) and coefficient zero.
All real coordinates retained in either half are at least \(t\).
Indeed, a neighborhood disjoint from \(B\) cannot contain a vertex
of \(I\), whose two neighbors are early.

## 1. An adjacent height fixed by an early position

Suppose the height of the neighboring position \(n=i\pm1\) is
fixed by an early position at distance two from the center. Then
\(d_n=0\). Its actual height lies in
\[
 [-.005,1/300]\quad(3),\qquad[-.0095,0]\quad(4\text{ unselected}),
 \qquad[0,H]\quad(4\text{ selected}).                    \tag{1}
\]
Since \(r_t\ge1/6\), the type-three interval is already included
in \(r_t[-.03,.02]\). The old neighbor-height-switch-zero cases
therefore cover it; the coefficient used in that unused height term
has no effect on the half expression.

For type four, the portion of (1) below \(-.02r_t\) lies in
\(r_t[-.057,-.02]\), so the same observation applies to the old
type-four cases. Every remaining frozen or selected height belongs to
\[
                         [-.02r_t,H].                       \tag{2}
\]
The actual type is four throughout (2), and its height derivative is
zero throughout. Its original selection flag does not enter the bare
phase half expression. Thus one additional interval handles these two
origins of a frozen height. There are ten new inner-half domains:
five center/switch choices, times the two orientations. Their neighbor
height-switch is zero, so no released outer variable occurs.

## 2. The released outer coordinate of an active height term

If the neighbor-height switch is active, that neighbor is unselected
and its closed neighborhood misses \(B\). The released outer position
\(o=i\pm2\) is therefore non-early and non-isolated, with real
coordinate \(x_o\in[t,.45]\). Its height can nevertheless be fixed
by an early vertex one position farther out.

A type-three outer coordinate fixed in this way has height in
\([-.005,1/300]\). This band is already inside the old polygon
\(\Omega_3(t)\), because \(\rho(x_o)\ge r_t\ge1/6\).
No new type-three outer test is needed.

For type four, all active, frozen and selected outer heights lie in
\[
 \widehat\Omega_4(t)=\operatorname{conv}\{
 (t,-.057r_t),(.22,-.057),(.45,-.057),(.45,H),(t,H)\}.         \tag{3}
\]
The polygon (3) is contained in the ramp/plateau polygon with the
[enlarged positive cap](research_mixed_early_selected_source_cap.md):
its lower boundary is \(-.057\rho(x)\), and its upper boundary is
\(H\) for every \(x\ge.12\). That compact polygon lies in the
strict outer cotangent chamber, so the global root theorem supplies
the original holomorphic phase before any boundary reduction. Only
this phase-domain inclusion is used here, not a new packet estimate.

With the center, neighbor and their coefficients fixed, the half
expression is the real part of a holomorphic function of this outer
variable. Its minimum on (3) is on the boundary. The two lower edges
are old tests. The top edge is the constant-selected outer segment
already tested in the 78-domain family. The lower portions of the two
vertical edges are also old tests. What remains consists exactly of
\[
 x_o=t\ \text{or}\ x_o=.45,\qquad
                       -.02r_t\le\Im z_o\le H.             \tag{4}
\]
There are forty new domains: five center/switch choices, two active
neighbor types, two orientations, and two vertical sides.

## 3. The unchanged half decomposition

Use the same imaginary gauge \(\kappa=3/2\), and the real gauge
\(+1/10\) on the left and \(-1/10\) on the right only when the
center is selected. A selected center still has actual height \(H\)
and zero height derivative. In (2) the neighbor has variable actual
height but zero height derivative. In (4) the outer selection flag is
irrelevant to the phase derivative and is not introduced as an extra
state. These are distinct roles of an actual height and its derivative
coefficient.

**Theorem 1 (frozen outer half stencils).** Both half expressions are
positive on all fifty new domains. Together with the
[192 unselected domains](research_mixed_minimum_level_half_stencils.md)
and the 78 constant-selected domains, this proves the frozen-early
local inequality for every moving center with no early neighbor.

More explicitly, write \(G_j=\partial_j\Phi\) and let \(d_j\) be
the actual height derivative coefficient, including the value zero at
a selected or frozen position. The halves are
\[
\begin{split}
 L_i(\chi,\xi)={}&\Re\bigl[
 (1+i\chi d_i/.12)(\partial_2\phi_{i-1}+i\kappa)
       +i\xi d_{i-1}G_{i-1}/.12\bigr]+\gamma_i,\\
 R_i(\chi,\xi)={}&\Re\bigl[
 (1+i\chi d_i/.12)(\partial_1\phi_i-i\kappa)
       +i\xi d_{i+1}G_{i+1}/.12\bigr]-\gamma_i,
\end{split}                                                     \tag{5}
\]
where \(\gamma_i=\mathbf1_{i\in S}/10\). The same switch
\(\chi\) occurs in both halves. Both gauges cancel, and minimizing
over the three switches gives exactly
\[
 \Re G_i+\sum_{j\in(i-1,i,i+1)}
             \min\{-(25/3)d_j\Im G_j,0\}\ge0.                \tag{6}
\]
The sum is over incidences, so repeated cyclic indices are retained.
Releasing repeated variables independently only enlarges the tested
sets. This covers cycles of lengths one and two as well.

The saved-cover checker uses the original logarithmic equation and the
same rational affine self-maps and Schur formulas as the earlier
half-stencil checker. Its five exact real parameters are the current
minimum, neighboring real coordinate, outer vertical parameter when
present, center height coefficient when present, and either the active
neighbor coefficient or the frozen neighbor's actual height. The lower
endpoint \(-.02r_t\) in both new intervals moves with \(t\); its
parameter derivative is retained. No sampled minimum is an acceptance
criterion. The exact split/monotonicity tree covers every domain.

The complete cover has 50 domains, 132,360 accepted leaves, 265,547
visited nodes and 877 monotonicity reductions. Every root witness and
every full-cell signed derivative is rechecked. The separate replayer
uses the independent sine-logarithm and real-cotangent arithmetic from
the previous replayer, with explicit derivatives of the new five-real-
parameter maps. It does not import the author arithmetic. In particular
it retains the derivative of the moving lower endpoint \(-.02r_t\)
in (2) and (4). Both implementations reconstruct the whole original
cube, consume every tree node, and verify all provenance bindings
before and after the replay.

Reproduction:

```sh
python3 experiments/certify_mixed_frozen_outer_half_stencils.py --precision 256 --input repro/results/research-mixed-frozen-outer-half-stencils.json --output /tmp/research-mixed-frozen-outer-half-stencils-review.json
python3 experiments/replay_mixed_frozen_outer_half_stencils.py --precision 320 --jobs 3
```

The class with one early neighbor of the moving center is separate.
A center with two early neighbors is in \(I\) and is deliberately not
moved. This note adds neither a finite-source interpolation nor an
unrestricted minimum-raising argument.
