# An earlier selected contour and its transport implication

Research note, 4 November 2026. The exact contour and the implications
below are proved here. The enlarged finite-source domain is established;
the local derivative inequalities are still being checked. This note
does not assert a completed selected-term theorem.

## 1. Two cutoffs on one exact contour

Fix an original cyclic three/four word, its critical point \(r\), and
a subset \(S\) of its type-four positions. Write \(c_j=\Im r_j\)
and \(H=7/500\). Let \(\rho\) be the original cutoff: zero on
\([0,.1]\), linear from zero to one on \([.1,.22]\), one on
\([.22,.45]\), linear from one to zero on \([.45,.5]\), and zero
on \([.5,1]\). Define a second cutoff
\[
 \widehat\rho(x)=
 \begin{cases}
 0,&0\le x\le .1,\\
 50(x-.1),&.1\le x\le .12,\\
 1,&.12\le x\le .45,\\
 20(.5-x),&.45\le x\le .5,\\
 0,&.5\le x\le1.
 \end{cases}                                                   \tag{1}
\]
Both functions are extended periodically. The new contour is
\[
 z_j=x_j+iH_{S,j}(x),\qquad
 H_{S,j}(x)=
 \begin{cases}
 c_j\min_{k\in(j-1,j,j+1)}\rho(x_k),&j\notin S,\\
 H\min_{k\in(j-1,j,j+1)}\widehat\rho(x_k),&j\in S.
 \end{cases}                                                   \tag{2}
\]
Repeated cyclic indices have their literal meaning in the minimum.

This is a continuous periodic piecewise affine graph. Almost everywhere,
each row of its derivative has at most one nonzero entry. An unselected
row has absolute derivative at most \(.057\cdot20=57/50\), and a
selected row at most \(H\cdot50=7/10\). The same Hadamard bound as
before therefore applies:
\[
              |\det(I+iDH_S)|<(38/25)^m.                       \tag{3}
\]
The [exact graph identity](research_mixed_coupled_outer_graph.md)
applies to every original selected Laurent term, with its scalar,
polynomial Fourier factors and powers of \(N\) unchanged.

On the closed low/plateau/right sets
\[
 L=[0,.1],\quad P=[.22,.45],\quad R=[.5,1],
\]
both cutoffs take the same values, zero or one. Thus (2) agrees exactly
with the previously proved minimum-neighbor graph on
\((L\cup P\cup R)^m\). The complete three-region estimate transfers
there without a new source comparison. The central unselected contour
is unchanged as well.

## 2. The source domain and the exact selected rate

For real coordinates in \([.1,.45]\), every selected target lies
under the upper boundary of the cap
\[
 T_4^+=\operatorname{conv}\{.1,\ .22-.057i,\ .22+Hi,\ .12+Hi\}
\]
or in the adjacent plateau rectangle. Indeed the minimum in (2) is at
most the selected coordinate's own cutoff. Unselected targets stay in
their old ramp/plateau polygons. The
[enlarged-cap source estimate](research_mixed_early_selected_source_cap.md)
therefore supplies a complete conditional packet on
all the required independent parameter products.

Write the original allocated phase and cyclic gradient as
\[
 \Phi(z)=\sum_j\phi_j(z_j,z_{j+1}),\qquad G_j=\partial_{z_j}\Phi.
\]
On
\(Y=[.12,.45]^m\), every selected height in (2) is exactly \(H\).
The true upper rate, retaining both Fourier alternatives, is
\[
 F_S(x)=\Re\Phi(z(x))+
       \sum_{j\in S}\max\{\Re g(x_j+iH),-2\pi H\}.           \tag{4}
\]
Unselected type-four targets have nonpositive heights and
\(-\Re g>0\), so their forcing alternative is dominated as in
the unselected transport argument.

The [transition branch inequality](research_mixed_selected_minimum_flow_obstruction.md),
equation (8), proves
\[
 -\Re g(x+ih)-2\pi h>3/40
     \quad(.1\le x\le.22,\ 0\le h\le H).                    \tag{5}
\]
Consequently a selected coordinate moving below \(.22\) has correction
exactly \(-2\pi H\) in (4), independent of its real coordinate.
Every selected coordinate not moving has both its real part and height
fixed. Thus the entire correction sum in (4) is constant along the
minimum-level path below. This uses the actual maximum in (4), not a
discarded forcing branch.

## 3. A local derivative hypothesis

Put \(s=25/3\), and distinguish the height used to evaluate the phase
from its coefficient of change along the path:
\[
 \widetilde c_j=\begin{cases}c_j,&j\notin S,\\0,&j\in S.
 \end{cases}
\]
A selected target has height \(H\), even though its coefficient
\(\widetilde c_j\) is zero. For a position \(i\) attaining the
minimum real coordinate, define
\[
 D_{S,i}(x)=\Re G_i(z(x))+
     \sum_{j\in(i-1,i,i+1)}
        \min\{-s\widetilde c_j\Im G_j(z(x)),0\}.              \tag{6}
\]
The sum has three terms with cyclic multiplicity. The hypothesis is
\[
 D_{S,i}(x)\ge0\quad\text{when }x\in Y,
                 \ x_i=\min_jx_j<.22.                        \tag{7}
\]

There are three local states: unselected type three, unselected type
four, and selected type four. The last state has constant actual
height \(H\) and zero height derivative. The half-stencil reduction
for (7) adds 78 domains to the 192 wholly unselected domains:

| Center and neighbor | New domains |
|---|---:|
| Neighbor selected; center arbitrary | 10 |
| Center selected, neighbor unselected, neighbor-height switch zero | 4 |
| Center selected, neighbor unselected, neighbor-height switch active | 48 |
| Center and neighbor unselected, outer coordinate selected | 16 |

For the 48 cases, the outer domain has six edges for unselected type
three, five for unselected type four, and one horizontal segment for a
selected outer coordinate. A selected center has no height switch; a
selected neighbor has no height-cost term and makes the outer coordinate
irrelevant. The common imaginary gauge cancels between the two halves.
Adding \(1/10\) to the left half and subtracting it from the right
half when the center is selected is another exact cancellation.
Neither gauge changes the finite invariant. These reductions organize
the pending local verification; they do not assert (7).

## 4. Consequence for every fixed word and selected subset

**Proposition 1.** Suppose (7) holds. If \(S\ne\varnothing\), then
\[
                       F_S(x)\le M-1/100\qquad(x\in Y),        \tag{8}
\]
where \(M=\Re\Phi(r)\) is the original geometric critical rate.

**Proof.** Let \(t_0=\min_jx_j\), and if \(t_0<.22\), set
\(x_j(t)=\max\{x_j,t\}\) for \(t_0\le t\le.22\).
At almost every parameter value the moving coordinates form a set
\(A(t)\), all attaining the current minimum. The unselected heights
whose neighborhoods meet \(A(t)\) have derivative \(s c_j\).
Selected heights have derivative zero. By (5), differentiation of
the full rate (4) therefore gives
\[
 \frac{dF_S}{dt}
 =\sum_{i\in A(t)}\Re G_i
     -s\sum_{j\in N(A(t))}\widetilde c_j\Im G_j,
\]
where \(N(A)\) consists of distinct affected positions. Summing (6)
over \(A(t)\) can only decrease this expression: it discards positive
height terms and may count negative ones more than once. Hence (7)
makes \(F_S\) nondecreasing. Absolute continuity justifies integration
through changes of the minimizing set, including the repeated cyclic
incidences for lengths one and two.

The endpoint belongs to \(P^m\), with the original reference height
at each unselected coordinate and height \(H\) at each selected
coordinate. The completed selected plateau theorem bounds every active
selected block at least \(1/100\) below its full complex tangent;
unselected plateau blocks lie below their own tangents. There is at
least one active selected block. Their tangent sums are \(M\) by
the original cyclic critical equations. This proves (8), also when
the starting point already belongs to \(P^m\). \(\square\)

**Corollary 2.** If (7) and the complete enlarged-cap source estimate
both hold, the contribution from \(Y\) of each nonempty original
selected subset satisfies
\[
                  |\mathcal I_{N,S}(Y)|
             \le C N^A e^{N(M-1/200)}                         \tag{9}
\]
at every sufficiently large integer level. The same bound, with a
different constant, holds after summing these subsets for a fixed word.

Indeed the complete conditional packets and the literal Fourier upper
bounds give rate at most \(F_S+m\varepsilon\). Choose
\(\varepsilon<1/(200m)\), and use (3), (8) and the fixed measure
of the integration domain. All original normalization factors have at
most polynomial cost, and there are finitely many subsets for a fixed
word. No sign or positivity of the original summands is assumed.

The early interval \((.1,.12)\), configurations involving low or right
coordinates together with transitions, and the right taper remain
outside (9). Agreement on \((L\cup P\cup R)^m\) does not estimate
those missing mixed configurations. In particular this conditional
selected result is one step toward the full-period theorem, not that
theorem itself.
