# A strict physical diagonal-strip gap for the merged pair

Research deduction, 7 November 2026. The total physical index near
the support boundary is exponentially below the merged pair's own
critical action. Together with the proved end strips, this removes
the entire boundary of the physical triangle before any contour
deformation. The proof uses the original complex boundary products
and evaluates no source or
critical point numerically.

## 1. The exact boundary rate

Use the literal source, output \(x=y=x_0=\xi+i\upsilon\), and
continuous absolute rate \(\mathcal E\) from
[the physical end-strip theorem](research_mixed_two_adjacent_physical_end_strips.md),
equations (1)--(5). Write
\[
 R=e^{2\pi\upsilon},\qquad \rho=R^{-1},\qquad
 \theta=2\pi\xi,\qquad
 L(a)=\int_0^a\log|1-Re^{-2\pi i(\xi+t)}|\,dt.
 \tag{1}
\]
On the diagonal \(s=1-a\), the real factorial terms cancel
exactly: \(J(1)=0\) and \(J(1-a)=-J(a)\). Thus
\[
 \mathcal E(a,1-a)=H(a):=L(a)+L(1-a)-\log R,
                      \qquad 0\le a\le1.
 \tag{2}
\]
This is the limiting rate of the supported rows just below the
wall. The physical rows on or beyond \(j+k=N\) remain exact
zeros; no assertion that nearby supported rows vanish is used.

**Lemma 1.** The rate in (2) is strictly increasing on
\((0,1/2)\) and strictly decreasing on \((1/2,1)\).

*Proof.* Its derivative is the logarithm of the ratio of the
two moduli
\[
 |1-Re^{-2\pi i(\xi+a)}|,\qquad
 |1-Re^{-2\pi i(\xi-a)}|.
\]
The first squared modulus minus the second is
\[
                    4R\sin(2\pi\xi)\sin(2\pi a).
 \tag{3}
\]
Both moduli are nonzero because \(R>1\), and
\(0<\xi<1/2\). This proves both signs. No concavity assumption
is required. \(\square\)

## 2. An analytic upper bound at the unique maximum

The original output bounds imply
\[
       0<\rho<5/8,\qquad \sin\theta<23/25,\qquad
                    \pi<3\theta<3\pi/2.
 \tag{4}
\]
For the first, \(\upsilon>39/500\) and \(\pi>157/50\)
give \(2\pi\upsilon>12/25\). The positive cubic exponential
sum gives \(e^{12/25}>8/5\). The sine bound is the explicit
alternating-polynomial estimate in
[the original output-cotangent proof](research_mixed_three_fourier_conditional_right_critical_sheet.md),
equation (7). The last inequalities use
\(1/6<\xi<1/4\).

Since \(\rho<1\), the ordinary logarithm series is absolutely
and uniformly convergent on the integration interval. Factoring
out \(R\) in (1) gives the exact Fourier identity
\[
\begin{split}
 H(1/2)
 &=2\int_0^{1/2}\log|1-\rho e^{2\pi i(\xi+t)}|\,dt\\
 &=\frac2\pi\sum_{\substack{n\ge1\\n\text{ odd}}}
                 \frac{\rho^n\sin(n\theta)}{n^2}.
\end{split}
 \tag{5}
\]
The \(n=3\) term is strictly negative by (4). Retain the
\(n=1\) term and bound the remaining odd terms in absolute value:
\[
\begin{split}
 H(1/2)
 &<\frac2\pi\left\{\rho\frac{23}{25}
                     +\frac{\rho^5}{25(1-\rho^2)}\right\}\\
 &<\frac{100}{157}\left\{\frac{23}{40}
                          +\frac{125}{19968}\right\}
   =\frac{290165}{783744}<\frac{3703}{10000}.
\end{split}
 \tag{6}
\]
The last cross-product difference is
\(3703\cdot783744-10000\cdot290165=554032>0\).

The same pair's original critical action has the proved lower bound
\[
 M_{22}>\frac{187049}{504000}>\frac{3711}{10000};
 \tag{7}
\]
the last cross-product difference is
\(10000\cdot187049-3711\cdot504000=146000>0\).
Combining Lemma 1 with (6)--(7) proves the strict whole-edge gap
\[
       \sup_{0\le a\le1}\mathcal E(a,1-a)
                       <M_{22}-\frac1{1250}.
 \tag{8}
\]

## 3. The original finite-source consequence

**Theorem 2.** There is a fixed \(\delta>0\) such that the sum
of the absolute values of all original supported rows with
\[
                    1-\delta<(j+k)/N<1
 \tag{9}
\]
is bounded by
\[
                      CN^A e^{N(M_{22}-1/2500)}.
 \tag{10}
\]
This holds for both level parities. After shrinking the fixed
complex endpoint neighborhood, it also holds there with the
continued critical action and gap \(1/5000\).

*Proof.* The rate \(\mathcal E\) is continuous on the full
closed supported triangle. The compact edge gap (8) therefore
persists with gap \(1/2500\) on a fixed collar of that edge.
Apply the original uniform physical factorial and product estimates
from the cited end-strip theorem and sum at most \(N^2\) rows.
This includes the last nonzero rows \(j+k=N-1\) and every
endpoint intersection. The exact rows on or beyond \(j+k=N\)
remain zero. Parameter continuity gives the stated smaller uniform
gap near \((x_0,x_0)\). \(\square\)

Combining this result with the physical end strips leaves a genuine
compact triangle
\[
                   a\ge\epsilon,\qquad s\ge\epsilon,\qquad
                              a+s\le1-\delta,
 \tag{11}
\]
for some fixed positive \(\epsilon,\delta\), containing the
actual critical real parts after decreasing the two widths if
necessary. Every deleted physical row is bounded at the original
pair action with a common positive loss. This is a source estimate
before any subsequent deformation, not an estimate for the whole
zero-extended complex rectangle. No remaining current, prescribed
closing functional, or arbitrary adjacent short-component theorem
is inferred from (10).
