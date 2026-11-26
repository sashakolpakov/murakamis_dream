# Positive pressure, and even coefficientwise relative accuracy, do not transfer signed suprema

31 October 2026. Private elementary obstruction to an unsupported parity
adapter. This is NOT an actual source polynomial or a counterexample to
any knot volume conjecture.

For d>=2 and j=floor(d/2), put

\[
 Q_d(A,C)=(A+C)^d,\qquad
 P_d(A,C)=Q_d(A,C)+2^{d/2}A^jC^{d-j}.
\]

Both are homogeneous of degree d with strictly positive coefficients.
The only changed coefficient has relative change
2^{d/2}/binom(d,j). Since the central binomial coefficient is the
largest of the d+1 coefficients summing to 2^d,

\[
 0\le [A^rC^{d-r}](P_d-Q_d)
 \le (d+1)2^{-d/2}[A^rC^{d-r}]Q_d
\]

for EVERY r. Therefore every positive evaluation satisfies

\[
 1\le P_d(A,C)/Q_d(A,C)
 \le1+(d+1)2^{-d/2}\qquad(A,C>0).
\]

In particular all positive real pressures, and all coefficient
exponential rates, agree. This holds globally in positive fugacity,
not merely near equal weights. On a fixed sufficiently small complex
z disk about any real z0, the extra term divided by Q_d(e^z,1)
is also exponentially small: its pointwise base at real z0 has rate
(log2)/2+z0/2-log(1+exp(z0)) <= -(log2)/2, and continuity provides
a smaller complex disk with a uniform negative margin. The floor j
only contributes a bounded factor on each fixed disk. Hence all local
normalized analytic pressure derivatives agree as well.

Nevertheless, define the same two negative-axis suprema as in the
actual cap reduction, over0<=t<=1. For Q_d both suprema are exactly1.
For P_d, the triangle inequality gives each supremum at most1+2^{d/2}.
At t=1, Q_d(-1,1)=0 and the extra monomial has absolute value2^{d/2}.
The same point occurs in the reciprocal branch. Thus

\[
 \lim_{d\to\infty}d^{-1}\log\sup_{0\le t\le1}|P_d(-t,1)|
 =\lim_{d\to\infty}d^{-1}\log\sup_{0\le t\le1}|P_d(-1,t)|
 =\frac{\log2}{2},
\]

whereas both corresponding rates for Q_d are zero.

This proves that even exponentially accurate coefficientwise comparison
with a stable polynomial, and equality of the entire positive real
pressure, cannot by themselves transport its negative-axis suppression.
The real-stability hypothesis in the classical root-measure theorem is
substantive. An even-level adapter must exploit the literal quantum
polynomial or a signed norm estimate strong enough for its error.
