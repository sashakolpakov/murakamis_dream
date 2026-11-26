# The real-index complement for a quantified prepared cap

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

Use the literal \(L_{40}=\lfloor N/40\rfloor\) retained vertex
\(\widetilde V_N^{(40)}\) and its finite summands from
[the bidisk theorem](research_three_vertex_bidisk_packet.md).
Put \(x_h=1/6+i\log2/(2\pi)\), and consider
\[
 \frac7{50}\le\Re x\le\frac15,\qquad
 \frac{10135867}{10^8}\le\Im x\le\frac{10135871}{10^8},
 \qquad
 |\Re(y-x_h)|,|\Im(y-x_h)|\le\frac1{200}.
 \tag{1}
\]
Let \(B=[1/4,9/20]\).

**Proposition 1.** The sum of absolute values of all original retained
real-index summands with \((i/N,j/N)\notin B^2\), including both
cardinal factors, satisfies
\[
                  \sum_{\rm complement}|\text{summand}|
                         \le CN^A e^{6455N/10000}.
 \tag{2}
\]
The same bound holds for any subset of this complement and for each
fixed wire derivative, at both level parities. Half-grid cuts within
\(O(N^{-1})\) of the ends of \(B\) give the same conclusion.

*Proof.* Write
\(\mathcal E=\Re(F(s,t;x,y)-\pi i(x+y))\), retaining the original
phase and cardinal constant. Both wire radii are less than \(27/50\),
and both real phases lie in \([7/50,1/5]\). The high-index
monotonicity proved in
[the conditional join estimate](research_three_prepared_cap_join_vertex.md),
equation (4), therefore applies throughout this parameter domain.
Each index above \(9/20\) may be decreased to \(9/20\), increasing
the exponent while preserving the undeleted support. Low-index
complements can likewise have their other high index decreased.
Consequently it suffices to bound, in both index orders,
\[
 \begin{split}
 &[0,1/40]\times[1/40,9/20],\qquad
 [1/40,1/4]\times[0,9/20],\qquad
 \{9/20\}\times[0,9/20].
 \end{split}
 \tag{3}
\]
The retained condition \(\max(i,j)>L_{40}\) supplies the positive
lower endpoint in the first rectangle. Every rectangle has
\(1/40\le s+t\le9/10\); thus the compact verification avoids
the sine-factorial endpoints entirely. The original endpoint entropy
estimate still controls every finite term reduced to these rectangles,
including rows with \(i+j=N-1\).

For fixed real indices and input wire, the exponent is harmonic in
\(y\). Reduce its maximum to the four sides of the outgoing square.
There are exactly twenty-four domains: four outgoing sides, both
index orders, and the three regions (3). Their four real coordinates
are \(\Re x\), the outgoing-side parameter, and the two index
parameters. The narrow input-height interval in (1) is retained in
every center value and interval derivative.

The author certificate uses the original sine primitive and exact
logarithmic derivatives; the independent replay uses the negative-
frequency dilogarithm primitive and sine-log derivatives. Each
outward center estimate includes the full interval derivative times
the rational half-width in every coordinate. All twenty-four domains
are covered by 556 accepted rational boxes, each proving
\[
                            \mathcal E<6455/10000.
 \tag{4}
\]
The independent replayer checks exact multiplicity-one binary coverage
and the full inequalities, without importing author code.

Uniform original factorial endpoint bounds and the at most \(N^2\)
summands cost only polynomial factors. The finite cutoff rounding
and half-grid perturbations preserve the strict compact margins.
The same margins permit a fixed complex parameter enlargement, so
Cauchy estimates retain each fixed wire derivative. These are estimates
of the literal finite source; all physical values and first normals
remain present. This proves (2). \(\square\)

An actual cap upper rate \(253/200=1.265\) on this input contour
therefore puts its real-index complementary product below rate
\(1.9105\). The cap bound and the lower critical action are separate
source and phase inputs; no nonzero coefficient follows from (2)
alone.

Run

```sh
python3 experiments/certify_three_prepared_cap_real_complement.py --precision 160
python3 experiments/replay_three_prepared_cap_real_complement.py --precision 192
```

The [author checker](../experiments/certify_three_prepared_cap_real_complement.py)
and [cover](../repro/results/research-three-prepared-cap-real-complement.json),
together with the
[independent replayer](../experiments/replay_three_prepared_cap_real_complement.py)
and [record](../repro/results/research-three-prepared-cap-real-complement-replay.json),
record all original-source domains and provenance.
