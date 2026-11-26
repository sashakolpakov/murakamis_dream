# Wire sums from the reduced-disk source witnesses

Research deduction, 5 November 2026. This extracts geometric inequalities
from the existing complete source witnesses. It proves every ordinary
wire sum lies in the desired half-plane. One internal type-four vertex
sum remains unresolved by these enclosures. No source witness, domain or
acceptance condition is changed.

## 1. The proved inequalities

Use the disks, zero-lift block map and six type products of
[the reduced-disk conditional source theorem](research_mixed_reduced_disk_conditional_packets.md).
Thus the external variables are \(a,b\), the inner variables are \(s,t\),
and the own type and unordered external types are

\[
 (3+\epsilon;3+\alpha,3+\beta),\qquad
 \epsilon\in\{0,1\},\quad
 (\alpha,\beta)\in\{(0,0),(0,1),(1,1)\}.
 \tag{1}
\]

**Proposition 1.** On every full closed external disk product in (1),

\[
 \frac{109}{200}<\Re(a+s)<\frac{77}{100},\qquad
 \frac{109}{200}<\Re(t+b)<\frac{77}{100},
 \tag{2}
\]

In addition,

\[
 \Re(s+t)<\frac{77}{100},\qquad
 \Re(s+t)>
 \begin{cases}
 3/5,&\epsilon=0,\\
 49/100,&(\epsilon,\alpha,\beta)=(1,0,0),\\
 21/40,&(\epsilon,\alpha,\beta)=(1,0,1),\\
 11/20,&(\epsilon,\alpha,\beta)=(1,1,1).
 \end{cases}
 \tag{3}
\]

Swapping the external variables swaps \(s,t\), so both orientations
and all ordered external types are included. In particular the two
wire inequalities \(1/2<\Re(a+s),\Re(t+b)<1\) hold universally.

The exact record retains the rational whole-cell extrema and the
addresses where their lower bounds are smallest. The following
decimals are deliberately rounded outward from those bounds:

| Own / external types | Lower bound for \(\Re(s+t)\) | Lower bound for \(\Re(a+s)\) | Lower bound for \(\Re(t+b)\) |
| --- | ---: | ---: | ---: |
| 3 / 3,3 | .61371521 | .59650850 | .59650850 |
| 3 / 3,4 | .63551794 | .58931062 | .59774260 |
| 3 / 4,4 | .65945042 | .59045376 | .59045376 |
| 4 / 3,3 | .49653824 | .54655782 | .54655782 |
| 4 / 3,4 | .52743034 | .54528383 | .54647282 |
| 4 / 4,4 | .55863533 | .54508883 | .54508883 |

These are certified enclosure bounds, not assertions that the true
minimum is attained at the displayed value. In particular the fourth
row does **not** prove or disprove \(\Re(s+t)>1/2\). No positive
geometric branch or source-to-geometry identification is inferred.

## 2. Extraction without a new root problem

On each accepted angle rectangle, the original witness proves

\[
 \binom{s}{t}=z_0+D(p-p_0)+\eta,
 \qquad p=(a,b),\qquad |\eta_i|\le r_i.
 \tag{4}
\]

The same rational centers, affine matrix and radii are retained.
For the three sums, combine their affine coefficients before taking
real parts:

\[
\begin{array}{c|c|c|c}
 &\text{constant}&\text{coefficients of }p-p_0&\text{error radius}\\
 s+t&z_{0,1}+z_{0,2}&D_{1j}+D_{2j}&r_1+r_2\\
 a+s&z_{0,1}+p_{0,1}&(D_{11}+1,D_{12})&r_1\\
 t+b&z_{0,2}+p_{0,2}&(D_{21},D_{22}+1)&r_2.
\end{array}
\tag{5}
\]

For a circle \(p_j=c_j+R_j e^{2\pi i\theta_j}\), a fixed
coefficient \(d\ne0\) has the exact real support expression

\[
 \Re\bigl(d(p_j-p_{0,j})\bigr)
 =R_j|d|\cos(2\pi\theta_j+\arg d)
       -\Re\bigl(d(p_{0,j}-c_j)\bigr).
 \tag{6}
\]

The zero coefficient contributes zero. Outward interval evaluation
of (6) on the entire saved angle interval, followed by the error
radius in (5), gives the bounds above. The checker validates each
original affine self-map again, but makes no new root proposal and
does not alter or subdivide a cell.

All six exact trees are exhausted: 4,409 accepted cells and 8,812
nodes, with the two source orientations retained. The selected block
map is holomorphic on a neighborhood of the disk products. Each real
part in (2)–(3) is therefore separately harmonic in \(a,b\). Two
maximum principles extend the strict distinguished-boundary bounds
to the full closed products. This last step uses the original unique
zero-lift map, not an independent choice of a root in each cell.

## 3. Scope and reproduction

The completed [nonprivate-leg inclusion theorem](research_mixed_open_local_factor_coverage.md) places the external
legs of every ordinary open-word vertex in these products. Hence
the two wire conclusions apply to every such incidence, regardless
of word length. Endpoint blocks require their separate endpoint
data. The unresolved fourth row prevents this deduction alone from
placing every internal vertex sum in the strict pair-sum chamber.

The focused checker binds both saved source runs and their current
proof/code inputs. Its output is an extraction record, not a new
source cover or a proof of full open-contour dominance.

```sh
python3 experiments/check_mixed_reduced_disk_pair_sums.py --precision 256
python3 experiments/check_mixed_reduced_disk_pair_sums.py --precision 320 --input repro/results/research-mixed-reduced-disk-pair-sums.json --output repro/results/research-mixed-reduced-disk-pair-sums-replay.json
```
