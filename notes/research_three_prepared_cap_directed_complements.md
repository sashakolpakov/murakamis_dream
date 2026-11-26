# Directed output bounds for the original prepared-cap complements

Research proof, 4 November 2026. Previous source theorems, their
certificates and frozen manuscripts are unchanged.

This note extends two upper estimates to the directed output chart
needed by the proposed four-vertex closing contour. It estimates the
literal retained real-index summands, including their cardinal factors.
It does not by itself prove a prepared-source packet or a closing
coefficient.

## 1. Exact source and domains

Use the original retained vertex \(\widetilde V_N^{(40)}\), with
the square \(i,j\le L_{40}=\lfloor N/40\rfloor\) deleted, from
[the bidisk source theorem](research_three_vertex_bidisk_packet.md).
Set
\[
 x_h=\frac16+iY_h,\qquad Y_h=\frac{\log2}{2\pi},\qquad
 h_-=\frac{10135867}{10^8},\quad h_+=\frac{10135871}{10^8},
 \tag{1}
\]
and define the closed outgoing rectangle
\[
 \mathcal D=x_h+[-3/500,7/1000]+i[-33/8000,0].
 \tag{2}
\]
All statements below hold at both level parities and for every fixed
wire derivative. The derivatives are of the actual finite source;
no physical value or first normal is replaced.

**Proposition 1 (the two joins).** For
\(\Re x\in\{7/50,1/5\}\), \(h_-\le\Im x\le Y_h\),
and \(y\in\mathcal D\),
\[
 \sum_{\text{all retained real indices}}|\text{summand}(x,y)|
                  \le CN^A e^{6471N/10000}.
 \tag{3}
\]

**Proposition 2 (the central real-index complement).** For
\(7/50\le\Re x\le1/5\), \(h_-\le\Im x\le h_+\),
\(y\in\mathcal D\), and \(B=[1/4,9/20]\),
\[
 \sum_{\substack{\text{retained real indices}\\(i/N,j/N)\notin B^2}}
       |\text{summand}(x,y)|\le CN^A e^{6455N/10000}.
 \tag{4}
\]
The same bounds hold for any subset of the indicated indices.
Half-grid cuts within \(O(N^{-1})\) of the displayed fixed cuts
have the same conclusion.

## 2. Global reduction and the exact finite certificate

Write the original exponent, with its cardinal contribution, as
\[
 \mathcal E(s,t;x,y)=\Re\{F(s,t;X,Y)-\pi i(x+y)\},
 \quad X=e^{2\pi ix},\quad Y=e^{2\pi iy},\quad
 s,t\ge0,\ s+t\le1.
 \tag{5}
\]
Here \(F\) is the exact phase of the finite-product interpolation
used in the [original join estimate](research_three_prepared_cap_join_vertex.md).
Both wire radii are less than \(r=27/50\), and both real phases
lie in \([7/50,1/5]\). Indeed the largest outgoing radius is
\(\tfrac12 e^{33\pi/4000}<r\); the input maximum is
\(e^{-2\pi h_-}<r\). The checker verifies these strict bounds.

The same global high-index reduction as in the original join proof
therefore applies. For \(9/20\le s\le7/8\),
\[
 e^{\mathcal E_s}
 =\frac{|X|\,|1-e^{-2\pi i(s+t)}|}{|1-Xe^{-2\pi is}|}
 \le\frac{2r}{\sqrt{1+r^2}}<1,
 \tag{6}
\]
because \(1/4\le s-\Re x<3/4\). For \(s\ge7/8\),
the same ratio is at most \(r\pi/[4(1-r)]<1\). Both estimates
also hold for \(t\). Decreasing a high coordinate to \(9/20\)
preserves the original triangular support and the retained condition.
It increases the upper exponent. This reduction includes the last
finite rows \(i+j=N-1\); the uniform original factorial endpoint
bound contributes only a power of \(N\).

For Proposition 1 it remains to check exactly the rectangles
\[
 [0,1/40]\times[1/40,9/20],\qquad
 [1/40,9/20]\times[0,9/20].
 \tag{7}
\]
For Proposition 2, check in both index orders the three rectangles
\[
 [0,1/40]\times[1/40,9/20],\quad
 [1/40,1/4]\times[0,9/20],\quad
 \{9/20\}\times[0,9/20].
 \tag{8}
\]
The full retained lattice has \(\max(i,j)/N>1/40\), so these
closed rectangles also cover all rounding at the deleted corner.
On each rectangle \(1/40\le s+t\le9/10\); no factorial endpoint
is inside the numerical verification.

For fixed real indices and fixed input, (5) is harmonic in the
outgoing complex variable. Both radii stay strictly below one, so
the logarithms and dilogarithms are holomorphic on a neighborhood of
\(\mathcal D\). The maximum principle reduces its outgoing
maximum to the four edges of (2). The input height for the joins
remains a full parameter interval. The tiny input-height interval
for the complement remains in every center value and derivative.
There is no harmonic reduction in a variable whose analyticity has
not been established.

The four exact derivatives used by the author are \(F_s,F_t\) and
\[
 \begin{split}
 \mathcal P_x&=2\pi is+\log(1-Xe^{-2\pi is})-\log(1-X)-\pi i,\\
 \mathcal P_y&=2\pi it+\log(1-Ye^{-2\pi it})-\log(1-Y)-\pi i,
 \qquad \mathcal P=F-\pi i(x+y).
 \end{split}
 \tag{9}
\]
All logarithms retain their original branches. Each rational box is
accepted only when its center value plus the interval gradient
times the coordinate half-widths is strictly below the required
bound. There are exactly 16 join domains and 24 complement domains.
The saved 160-bit author cover has respectively 1,343 and 491
accepted boxes. The independent 192-bit replayer checks exact
multiplicity-one binary coverage and every inequality, using the
negative-frequency dilogarithm primitive and sine-log derivatives.
It imports no author code.

Uniform finite factorial estimates and the at most \(N^2\)
summands cost only polynomial factors. All domain inequalities have
strict margins on a finite compact cover. They therefore persist
on a small complex enlargement, including finite-cut rounding.
Cauchy estimates on that enlargement prove all fixed derivatives.
This proves both propositions for the original finite source.

## 3. Scope and reproduction

For example, a separately proved cap upper rate \(1.2638\) on
the joins combines with (3) to give rate strictly below \(1.9109\).
A separately proved cap rate \(1.265\) combines with (4) to give
rate strictly below \(1.9105\). These comparisons do not supply
the cap bounds, a lower critical action, the remaining contour
currents or a nonzero coefficient. In particular the rectangle (2)
is directed; no larger symmetric disk or square is asserted.

```sh
python3 experiments/certify_three_prepared_cap_directed_complements.py --precision 160
python3 experiments/replay_three_prepared_cap_directed_complements.py --precision 192
```

The [author checker](../experiments/certify_three_prepared_cap_directed_complements.py)
and [cover](../repro/results/research-three-prepared-cap-directed-complements.json),
and the [independent replayer](../experiments/replay_three_prepared_cap_directed_complements.py)
and [replay record](../repro/results/research-three-prepared-cap-directed-complements-replay.json)
retain the exact directed chart, all 40 domains and proof provenance.
