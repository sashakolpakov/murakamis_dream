# Retained-vertex bounds on prepared-cap wire joins

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The input wire below is on one of the two vertical joins already used
in the complete-cap attachment. The outgoing wire varies over a genuine
complex neighborhood. Keeping the input's actual real phase gives a
stronger bound than maximizing over both real phases independently.

Use the exact \(L_{40}=\lfloor N/40\rfloor\) retained source
\(\widetilde V_N^{(40)}\) from
[the bidisk theorem](research_three_vertex_bidisk_packet.md), and put
\[
 Y_h=\frac{\log2}{2\pi},\qquad x_h=\frac16+iY_h,\qquad
 h_-=\frac{10135867}{10^8},\qquad
 \mathcal Q=\{x_h+u+iv:|u|,|v|\le1/200\}.
 \tag{1}
\]

**Proposition 1.** For \(\xi=7/50\) or \(\xi=1/5\),
\(h_-\le h\le Y_h\), and \(y\in\mathcal Q\),
\[
       |\widetilde V_N^{(40)}(\xi+ih,y)|
                   \le CN^A e^{6469N/10000}.
 \tag{2}
\]
This is an upper bound for the sum of the absolute values of the
literal retained summands. It therefore also applies to every real-index
subset. Both parities and every fixed wire derivative are retained.
The actual base-attachment joins lie strictly within the height range
in (1). No lower input height or moving saddle contour is asserted.

*Proof.* The original finite-product bound gives the real exponent
\[
 \mathcal E(s,t;x,y)=\Re\{F(s,t;x,y)-\pi i(x+y)\},
 \qquad s,t\ge0,\quad s+t\le1.
 \tag{3}
\]
The cardinal exponential is included. The two wire radii are at most
\(r=27/50\), and their real phases lie in \([7/50,1/5]\).
For \(9/20\le s\le7/8\),
\(1/4\le s-\Re x<3/4\), hence
\[
 e^{\mathcal E_s}
 =\frac{|X|\,|1-e^{-2\pi i(s+t)}|}{|1-Xe^{-2\pi is}|}
 \le\frac{2r}{\sqrt{1+r^2}}<1.
 \tag{4}
\]
For \(s\ge7/8\), the same ratio is at most
\(r\pi/(4(1-r))<1\). The identical argument applies to \(t\)
and the outgoing phase. Decreasing any index above \(9/20\)
therefore increases (3), preserves feasibility and leaves the index
outside the deleted corner. Apply this to both coordinates.
Consequently the whole retained triangle reduces to the union
\[
 [0,1/40]\times[1/40,9/20],\qquad
 [1/40,9/20]\times[0,9/20].
 \tag{5}
\]
On these rectangles \(1/40\le s+t\le9/10\), so the phase has
no factorial endpoint singularity. The original finite factorial
entropy still controls all omitted endpoints in the reduction (4),
with its uniform polynomial loss.

For fixed real \(s,t\) and fixed input wire, (3) is harmonic in
the outgoing complex variable \(y\). Its maximum on \(\mathcal Q\)
therefore occurs on its four sides. The input height is left as a full
interval, not reduced to endpoints by an unproved convexity claim.
There are exactly sixteen compact domains: two input real phases,
four outgoing sides, and the two index rectangles (5). Each domain has
four real coordinates. Its exact derivatives are the original
\(F_s,F_t\) and
\[
 \mathcal P_x=2\pi is+\log(1-Xe^{-2\pi is})-\log(1-X)-\pi i,
 \quad
 \mathcal P_y=2\pi it+\log(1-Ye^{-2\pi it})-\log(1-Y)-\pi i,
 \tag{6}
\]
where \(\mathcal P=F-\pi i(x+y)\). Thus the input-height
derivative is \(-\Im\mathcal P_x\). The fixed compact bounds
\(|X|,|Y|<1\) retain all logarithmic branches.

The outward certificate encloses (3) by its exact rational-center
value plus interval derivatives times the coordinate half-widths.
All sixteen domains have a complete rational cover, with 1,732
accepted boxes, each proving \(\mathcal E<6469/10000\).
The independent negative-frequency primitive replay verifies the
same full boxes and exact partition coverage without importing
author code. The cover includes all cut faces and corners.

The floor in \(L_{40}\) and the finite upper index \(N-1\)
preserve the strict entropy margins. Uniform original factorial
estimates contribute only polynomial factors, and there are at most
\(N^2\) summands. This proves (2). The strict compact margins persist
on a small complex neighborhood of the joins and of \(\mathcal Q\);
Cauchy estimates give every fixed wire derivative. No original
physical jet has been changed, since the exact finite cardinal/Newton
source was retained throughout. \(\square\)

For example, combining (2) with an actual cap upper rate \(1.2638\)
gives rate strictly below \(1.9107\). Comparison with a moving
prepared-cap critical action still requires a uniform lower bound for
that action, and the remaining central and exterior currents remain
separate. The present proposition does not supply those premises.

Run

```sh
python3 experiments/certify_three_prepared_cap_join_vertex.py --precision 160
python3 experiments/replay_three_prepared_cap_join_vertex.py --precision 192
```

The [author checker](../experiments/certify_three_prepared_cap_join_vertex.py)
and [cover](../repro/results/research-three-prepared-cap-join-vertex.json)
retain all sixteen domains. The
[independent replayer](../experiments/replay_three_prepared_cap_join_vertex.py)
and [record](../repro/results/research-three-prepared-cap-join-vertex-replay.json)
retain the exact-cover and arithmetic audit. This estimate uses the
larger original deleted corner and is not a claim about the older
\(L_{50}\) source.
