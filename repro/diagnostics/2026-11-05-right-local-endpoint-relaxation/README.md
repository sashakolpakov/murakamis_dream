# Local derivative tests after reducing the raw rows to endpoints

These six floating calculations test a sufficient local inequality for
raising a minimum coordinate next to a right-half coordinate. They are
diagnostics, not a proof of a uniform lower bound. The reference heights
are released independently over their full typed intervals; they are not
claimed to come from six particular knots or geometric references.

The center has real coordinate \(t\in[.12,.22]\). Its right neighbor is
fixed at \(.5\). The three patterns are:

1. The left neighbor and the next coordinate to its left are ordinary
   half-period coordinates.
2. The left neighbor is ordinary and its other neighbor is right-half.
3. Both neighbors of the center are right-half.

Every retained coordinate is unselected. Each pattern is tested with all
local types three, and then with all local types four. The height
coefficients range independently in \([-.03,.02]\) or \([-.057,-.02]\),
respectively. Let \(r=(t-.1)/.12\) and
\[
 T(x)=\begin{cases}1,&x\le.45,\\400(.5-x)^2,&.45\le x\le.5.\end{cases}
\]
The center has height \(c_0r\); its left neighbor has height
\(c_{-1}T(x_{-1})r\). When the next coordinate is ordinary, its height
is \(c_{-2}T(x_{-2})\lambda\), where
\[
 r\le\lambda\le
 \min\{1,(x_{-2}-.1)/.12,(x_{-1}-.1)/.12\}.
\]
This releases only the next exterior cutoff and keeps the correlation
imposed by the immediate neighbor.

For each raw edge, the script substitutes both row endpoints \(u=.2,.4\)
in its original directional derivative. It takes the least value among
the endpoint choices. Coherent edges retain their original complex
critical phase. If \(G_0,G_{-1}\) are the resulting sums of incident
partials, the tested expression is
\[
 \Re G_0+
 \min\{-c_0\Im G_0/.12,0\}+
 \min\{-c_{-1}T(x_{-1})\Im G_{-1}/.12,0\}.
\]
The last term is absent when the left neighbor is right-half. Thus the
test retains both incident contributions and the unfavorable neighboring
height change, without splitting them using an imaginary constant.

The six smallest values found were positive. For type four they were
approximately \(.11512,.05109,.24847\) in the order above; for type three
they were approximately \(.71017,.65538,.68682\). These are values at
trial points, hence upper bounds for the infima being investigated.
They are not certified lower bounds. In particular, the calculation
does not cover mixed types, selected endpoints, or every placement of a
right-half coordinate in a full local neighborhood.

The optimization budget is fixed at forty iterations and six population
members per parameter, separately for each of the six problems. The
saved result binds the driver and the copied original-phase helper.
No saved proof cover is recomputed. Run it with

```sh
python3 repro/diagnostics/2026-11-05-right-local-endpoint-relaxation/diagnose.py
```
