# Quantitative transport of the selected outgoing action

Private phase deduction, 8 November 2026. The original selected
outgoing action, with the square-root sine-product metric included,
decreases at a fixed rate along the real physical middle arc.
This follows from the proved weighted-energy margin and the exact
signed period pairing. No mathematical numerical evaluation or
frozen-source edit is used.

The conclusion concerns the original critical action. It does not
establish a finite conditional packet, dominance of a coefficient,
or suppression of the remaining coherent observation.

## 1. Original selected phase

Retain all coordinates, domains, and logarithmic choices of
[the selected outgoing sheet theorem](research_mixed_next_outer_selected_outgoing_sheet.md):
\[
 a\in[1/2,5/6],\quad x=e^{2\pi ia},\quad Y=x^{-1},\quad
 z_*=u+ih,\quad
 u\in[3/10,39/100],\quad h\in[-3/100,1/50].
                                                                    \tag{1}
\]
The original output is \(Z=e^{-2\pi iz_*}\).
That theorem proves a simple original zero-lift root \(s_*(a,z_*)\)
with
\[
 0<\Re s_*<1-a,\qquad \Im s_*>0,\qquad Q_s(s_*;a,z_*)=0,
\]
for the unchanged phase
\[
 Q(s;a,z_*)=g(a+s)+g(z_*+s)-2g(s)-g(a)-g(z_*)+2\pi ias .
                                                                    \tag{2}
\]
Define its critical value and the real sine primitive by
\[
 \mathcal S(a,z_*)=Q(s_*(a,z_*);a,z_*),\qquad
 J(a)=\int_0^a\log|2\sin(\pi v)|\,dv,\qquad J(1/2)=0.
                                                                    \tag{3}
\]
No additive constant in (2) is changed.

Write \(z_{\rm per}\) for the paired period root, distinct from
the outgoing coordinate \(z_*\). The source sheet theorem gives
\[
 \sigma=|x-1|=2\sin(\pi a),\qquad
 |z_{\rm per}|>\sqrt{\sigma},\qquad
 e^{\partial_a Q(s_*;a,z_*)}=-z_{\rm per}^{-1}.
                                                                    \tag{4}
\]

## 2. A fixed separation from the weighted circle

The principal energy calculation in
[the exact outgoing weighted-energy theorem, (13)--(14)](research_mixed_next_outgoing_weighted_energy.md)
has the uniform margin \(51/350\) on the entire actual containing
outgoing region. In the sine-product metric, its two normalized
off-diagonal principal terms have modulus \(\sigma^{3/2}\)
on the weighted circle. They are conjugates there. The fixed
additional rotation is \(1+3i\).

Set
\[
                       r=|z_{\rm per}|/\sqrt{\sigma}>1 .
\]
Compare the zero of the principal symbol at \(z_{\rm per}\)
with the point of the same argument on
\(|z|=\sqrt{\sigma}\). The two off-diagonal terms change
their moduli by the factors \(r\) and \(r^{-1}\); the
diagonal is unchanged. The modulus of the change after
the fixed rotation is at most
\[
 \sqrt{10}\,\sigma^{3/2}
              \{(r-1)+(1-r^{-1})\}
       =\sqrt{10}\,\sigma^{3/2}(r-r^{-1})
       <9(r-r^{-1}),                                               \tag{5}
\]
because \(1\le\sigma\le2\) and \(\sqrt{80}<9\).
This comparison also follows directly by replacing the
outgoing sequence ratio by its reciprocal period ratio;
both give the same two factors in (5).

At the weighted-circle point the rotated real part exceeds
\(51/350\), whereas at the root it is zero. If
\(r\le126/125\), then
\[
 9(r-r^{-1})<\frac{18}{125}<\frac{51}{350};
\]
the last comparison is \(6300<6375\) after clearing
positive denominators. This contradicts (5). Hence
\[
 \boxed{\qquad
 |z_{\rm per}|>\frac{126}{125}\sqrt{2\sin(\pi a)}.
 \qquad}                                                          \tag{6}
\]
This is a quantitative separation of the selected principal
root, not a statement about ratios of the actual finite
outgoing coefficient sequence.

## 3. Action transport with its original metric

The implicit critical point is holomorphic near each real
parameter, and \(Q_s=0\). Thus
\[
 \partial_a\mathcal S=\partial_a Q(s_*;a,z_*).
\]
Taking moduli in (4) and using (6) gives
\[
 \boxed{\qquad
 \partial_a\Re\mathcal S(a,z_*)
  <-\frac12\log(2\sin(\pi a))
                         -\log(126/125).
 \qquad}                                                          \tag{7}
\]
In particular the unweighted real action is strictly decreasing,
since \(2\sin(\pi a)\ge1\) on the whole interval.

For any \(1/2\le a_1<a_2\le5/6\), integration proves
\[
 \boxed{\quad
 \Re\mathcal S(a_2,z_*)+\tfrac12J(a_2)
 <
 \Re\mathcal S(a_1,z_*)+\tfrac12J(a_1)
             -(a_2-a_1)\log(126/125).
 \quad}                                                           \tag{8}
\]
The fixed extra slope is positive; explicitly
\[
 \log(126/125)=2\operatorname{artanh}(1/251)>2/251.
\]
All comparisons are uniform over the original compact
outgoing domain (1).

The weight in (8) is the one from the actual recurrence.
For \(S_b=\prod_{\nu=1}^b2\sin(\pi\nu/N)\) and \(a=b/N\),
the original uniform sine-factorial estimate, also used in
[the physical outgoing envelope, (6)](research_mixed_next_physical_three_outgoing_attachment_budget.md), gives
\[
 \frac1N\log S_b=J(a)+O((\log N)/N)
\]
uniformly on the physical middle interval. Thus \(J/2\)
is the action cost of the metric multiplier \(S_b^{1/2}\).
This interpretation does not identify the finite conditional
sum with its selected critical value: such a conclusion still
requires its complete contour and error analysis.

Neither (6) nor (8) excludes the original period
characteristic from the selected outside-root branch.
Transformed forcings, endpoint observations, and the full
coherent transfer remain subject to their separate exact
source estimates.

