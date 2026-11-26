# A terminal raw gap using the preceding ordinary equation

Research deduction, 5 November 2026. This treats an open word of length
at least three whose last two types are both three. The actual terminal
neighbor may range over its entire smaller type-three disk. A necessary
constraint from the preceding ordinary block repairs the raw comparison
that fails on the unconstrained disk. The resulting finite estimate holds
on a small ambient neighborhood of these critical inputs; the critical
equations are not imposed on integration targets.

## 1. Domain, original action, and the multiplier

Let
\[
 D=\{a:|a-(.35-.01i)|\le.083\},\qquad
 h_h=\Re\{J(1/2)+F(1/2,1/4+i\log3/(4\pi))\}.
 \tag{1}
\]
Use the original holomorphic endpoint map \((e(a),t(a),u(a))\) of
own type three and its optimized action \(P_0(a)\), with exactly the
normalization in [the calibrated raw theorem](research_mixed_terminal_raw_half_gap.md).
In particular \(P_0\) includes the bare terminal conditional phase
and the terminal coefficient phase; it is not a real maximization.

Write \(V=e^{-2\pi ia}\), \(B=e^{-2\pi it(a)}\), and set
\[
 \mathcal U(a)=\frac{1-B(1-V)^2/(1-VB)}{V},\qquad
 \psi(a)=\log|\mathcal U(a)|+\frac{13\pi}{100}.
 \tag{2}
\]
The [exact coupling constraint](research_mixed_terminal_inverse_constraint.md)
and the full-bidisk ordinary height bound show that every actual input
under the present type and length hypotheses satisfies \(\psi(a)\ge0\).
The holomorphic function \(\mathcal U\) has no poles on a neighborhood
of \(D\); zeros away from actual inputs are permitted.

The [all-height row theorem](research_mixed_terminal_half_row_envelope.md)
bounds the complete bare row envelope by the maximum of four functions:
\[
 \mathcal R_0(a)\le\max\{R_-(a),-2\pi\Im a,b_2/2,
                                      b_2/2-\pi\Im a\},
 \qquad b_2=-4J(1/4),                                   \tag{3}
\]
where
\[
 R_-(a)=\max_{0<v<1/2}\Re\{J(a+v)-J(a)+J(v+1/2)
                                      -2J(v)+i\pi av\}.
 \tag{4}
\]
Thus all upper rows are retained in (3), including at heights beyond
the old cyclic band. Each branch of (3) is continuous and subharmonic
in the unchanged complex input \(a\).

**Theorem 1.** On the circle \(\partial D\), every branch \(R_j\)
in (3) satisfies
\[
 \Re P_0(a)-h_h-R_j(a)-\frac1{200}\psi(a)>\frac1{4000}.
 \tag{5}
\]
At a zero of \(\mathcal U\), the left side is \(+\infty\).
Consequently
\[
 \Re P_0(a)-h_h-\mathcal R_0(a)>\frac1{4000}
 \quad\text{for every }a\in D\text{ with }\psi(a)\ge0.
 \tag{6}
\]

The implication follows from the superharmonic multiplier lemma in
[the coupling-barrier proof](research_terminal_coupling_barriers.md).
The numerical assertion (5) is a complete circle check on 165 existing
endpoint cells, described below. It uses no new endpoint root or
parameter subdivision. The other three own/external type families and
the length-two case are not asserted here.

## 2. Exact derivatives used on the old cells

All derivatives below are of the original equations, not finite
differences. Put \(L(z)=\log(2\sin\pi z)\) on the original strip.
For own type three the endpoint equations are
\[
\begin{split}
 f_e&=-L(e-u)+L(e+t)+i\pi(u-t),\\
 f_t&=L(e+t)+L(t+a)-2L(t)+i\pi(a-e),\\
 f_u&=2\log\cos\pi u+\log\sin\pi(e-u)
                               -3\log\sin\pi u+i\pi e.
\end{split}                                             \tag{7}
\]
Their Jacobian \(M=f_{(e,t,u)}\) is the same symmetric matrix as in
the original endpoint certificate. With \(z=(e,t,u)\),
\[
 z'=-M^{-1}(0,\pi\cot\pi(t+a)+i\pi,0)^T,
 \qquad z''=-M^{-1}r.                                   \tag{8}
\]
Writing \(z'=(e',t',u')\) and \(L''=-\pi^2\csc^2\pi z\), the
three components of the exact second forcing are
\[
\begin{split}
 r_e={}&-L''(e-u)(e'-u')^2+L''(e+t)(e'+t')^2,\\
 r_t={}&L''(e+t)(e'+t')^2+L''(t+a)(t'+1)^2
                                             -2L''(t)(t')^2,\\
 r_u={}&-2\pi^2\sec^2(\pi u)(u')^2
              +L''(e-u)(e'-u')^2-3L''(u)(u')^2.
\end{split}                                             \tag{9}
\]
The stored approximate inverse, a whole-cell Neumann series, and its
explicit geometric tail enclose both responses in (8).

The stationary-value identities give
\[
\begin{split}
 P_0'&=g'(a+t)+2\pi it-g'(a),\\
 P_0''&=g''(a+t)(1+t')+2\pi it'-g''(a).
\end{split}                                             \tag{10}
\]
The rational expression (2), differentiated twice with the product and
quotient rules, gives \(\mathcal U'\) and \(\mathcal U''\).
Its real log-modulus Hessian is the harmonic Hessian of
\[
 \mathcal L''=\mathcal U''/\mathcal U
                                      -(\mathcal U'/\mathcal U)^2.
 \tag{11}
\]
This formula is used only on old cells where the whole enclosure excludes
zero. Cells without that exclusion can instead use the direct upper
bound for \(\log|\mathcal U|\) and a separate gap lower bound.

For the lower row, let \(v=v_*(a)\) be its unique maximizer and
\(T=E_{vv}<-2\pi\), where \(E\) is the rate in (4). Set
\[
 q=g''(a+v)-g''(a),\quad
 k=g''(a+v)+2\pi i,\quad
 w=(\Re k,-\Im k)^T,\quad
 \mathsf H(c)=\begin{pmatrix}\Re c&-\Im c\\-\Im c&-\Re c\end{pmatrix}.
 \tag{12}
\]
The real optimizer response is retained exactly:
\[
 D^2R_- =\mathsf H(q)-ww^T/T,
 \quad
 D^2(\Re P_0-h_h-R_-)=\mathsf H(P_0''-q)+ww^T/T.
 \tag{13}
\]
For the three affine branches, the latter Hessian is simply
\(\mathsf H(P_0'')\). Subtracting
\(\mathsf H(\mathcal L'')/200\) gives the Hessian used for (5).
The real gradient of the lower-row gap is represented by
\(g'(a+t)+2\pi it-g'(a+v)-2\pi iv\), as in the earlier raw theorem.
The midpoint value and gradient use the original saved midpoint root
and a saved rational bracket for \(v_*\); no optimizer is replaced
by a merely sampled row value.

## 3. Complete circle coverage and the Taylor bound

The original type-three input disk has radius .09. In its normalized
parameter square the new circle therefore has radius \(83/90\).
The checker traverses all 3,439 nodes of the original \((0,0)\) endpoint
tree, including its 1,645 leaves and 75 excluded boxes. An exact rational
minimum/maximum squared-norm test retains every leaf meeting the new
circle. There are exactly 165 such leaves. No old excluded box intersects
that circle.

On every retained cell the original zero-log witness is revalidated.
Its same center and inverse also validate the midpoint with radius
\(10^{-10}\). The old whole-cell enclosure may be intersected with
the transported enclosure
\(z(a_0)+z'(\text{cell})(a-a_0)\); repeating this inclusion three times
only sharpens the enclosure on that same cell. It creates neither a new
root proposal nor a new parameter cell.

For each branch let \(F\) denote the left side of (5), and let
\(a=a_0+\delta x+i\delta y\) lie on the old cell's circle arc.
The second-order bound is
\[
 F(a)\ge F(a_0)+\nabla F(a_0)\cdot(\delta x,\delta y)
 -\frac12\{M_{xx}r_x^2+2M_{xy}r_xr_y+M_{yy}r_y^2\},
 \tag{14}
\]
where \(r_x,r_y\) are the old cell halfwidths and \(M_{jk}\) bound
the absolute Hessian entries on the whole cell. Outward midpoint-gradient
uncertainty is charged with these same halfwidths.

The minimum of the midpoint linear form on the exact cell/circle
intersection is found without an angular grid. Its candidates are the
circle intersections with the four sides and, if admitted, the unconstrained
circle minimum in the opposite gradient direction. Every candidate whose
interval enclosure might meet the cell is kept. Including an extra candidate
only weakens the lower bound. This finite list is complete, also when a
cell contains two arc components or a tangent contact.

The checker may take the better of (14), the corresponding first-order
circle bound, and the separate gap-minus-log-modulus bound. Each is an
outward lower bound for the same function. All four branches pass the fixed
floor \(1/4000\); the minimum accepted enclosure is greater than
.00034060. The single multiplier \(1/200\) is fixed in the checker.
Exploratory multiplier trials are not acceptance inputs.

## 4. The finite terminal sector near every actual reference

The feasible set \(\{a\in D:|\mathcal U(a)|\ge e^{-13\pi/100}\}\)
is compact. Continuity and the strict margin give a fixed small ambient
complex neighborhood on which the raw gap is greater than \(9/40000\).
Every actual complete-color terminal neighbor of a word of length at least
three ending \((3,3)\) belongs to this set. Points in the ambient
neighborhood need not solve the critical equations.

Apply the complete finite terminal right-angle reduction from
[the endpoint polynomial collar theorem](research_mixed_endpoint_polynomial_collar.md).
It retains all rows at arbitrary compact neighboring heights, including
the endpoint layer. On a sufficiently small fixed ordinary-color disk,
and for every fixed ordinary derivative, spend one source tolerance
\(\eta<1/40000\). This gives
\[
 \left|C_{0,N}(e^{-2\pi ia},e^{-2\pi ie})
                  H_N(w_R,e^{2\pi ie})\right|
 \le C N^A\exp N\{\Re P_0(a)-1/5000-K(e)\},
 \quad \frac12\le e\le1,
 \tag{15}
\]
where \(K(e)=-\int_{1/2}^e\log\sin\pi t\,dt\ge0\).
The terminal type is three, so its own diagonal exponent and selected
terminal exponent are zero. The external type-three halfweight remains
allocated to the preceding part of the source exactly as in the original
one-cap representation.

For each fixed word, the other unaliased coordinates may vary in a small
neighborhood at their reference heights. Combining \(P_0\) with those
ordinary phases and the surviving cut tangent uses the original one-ended
Schur estimate and retains the local interior completion loss. This is a
calibrated terminal-sector bound, not global control of the other outgoing
coordinates, selected aliases, or the opposite boundary. No arbitrary
attenuation \(a\mapsto\Re a+i\lambda\Im a\) is used.

## 5. Reproduction

    python3 experiments/check_mixed_terminal_coupled_disk_gap.py --precision 256
    python3 experiments/check_mixed_terminal_coupled_disk_gap.py --precision 320 --input repro/results/research-mixed-terminal-coupled-disk-gap.json --output repro/results/research-mixed-terminal-coupled-disk-gap-replay.json

The saved replay reuses every row bracket and old endpoint witness. It
checks the complete old tree, the circle incidences, all four branches,
and the current source/proof bindings. The earlier independent-disk
obstruction and its exact compatibility exclusion remain unchanged.
