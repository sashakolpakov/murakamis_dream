# A rational lower certificate for the original complete R54 action

This certificate concerns the original complete marked source, with
protected vertices \(29,50\), rather than the one-sided sector or its
capacity. The certified lower bound is
\[
 \Phi>67.688246275129>67.687,\qquad
 \operatorname{Vol}(Y)=2\pi\Phi.                                \tag{1}
\]
It supplies only a lower bound for the complete action. No signed
coefficient, representation, or filled-period claim follows from (1)
alone.

## 1. Exact feasible data

The original oriented sphere and matching are fixed by
\(\texttt{actual_singleton_sector_obstruction_certificate.json}\), whose
SHA256 is
\(\texttt{324173b25db8fbe36a89ac65617663c44d1385772c1e29e394bbb6b478a11022}\).
Its 54 ordered crossing quartets are \((x,b,c,y)\). Each contributes the
two complete triangles \((x,b,y)\) and \((x,c,y)\). There are 108 rows.

The new certificate gives a rational number \(\alpha_{T,v}>0\) for every
supported corner \(v\) of every row \(T\). Protected corners have
allocation zero. The verifier checks, with exact fractions,
\[
 \sum_{v\in T}\alpha_{T,v}=\frac12\quad\text{for each of 108 rows},
 \qquad
 \sum_{T\ni v}\alpha_{T,v}=1\quad\text{for each of 54 ordinary faces}.
                                                                    \tag{2}
\]
It also checks each row against its original quartet and side; no
arbitrary permutation or replacement incidence is accepted. The minimum
supported allocation is
\[
                 \min\alpha_{T,v}
                   =\frac{97764897}{200000000000}>0.             \tag{3}
\]

The original complete variational theorem therefore gives
\[
 \Phi\geq\sum_T\sum_{v\in T} f_{\mathrm{tri}}(\alpha_{T,v}),\qquad
 f_{\mathrm{tri}}(a)=
 \frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi}.                  \tag{4}
\]
The exact source degree is a half row per triangle and one unit per
ordinary face. Thus (2), not a numerical packing residual, is the
hypothesis needed in (4). Polynomial finite-level prefactors have zero
normalized logarithmic rate and do not change this action.

## 2. Proposal and exact correction

The builder uses the previously published rational positive radii to
propose the triangle loads
\(\arctan(w_v/\sqrt{w_iw_j+w_iw_k+w_jw_k})/\pi\), with their literal
zero-coordinate limits. This stage uses floating-point arithmetic only
to locate useful rational numbers. It rounds the first supported
corners to denominator \(10^{12}\), and sets the last corner to enforce
the exact row sum \(1/2\).

Rounding leaves rational ordinary-target residuals. The graph joining
two ordinary faces when they occur in one supported row is connected.
Choose a spanning tree. For a leaf \(v\) with parent \(p\), let
\(\delta_v\) be its remaining target deficit, and choose a row containing
both. Add \(\delta_v\) at \(v\) and subtract it at \(p\) in that row.
This repairs \(v\) and transfers its deficit to \(p\), without changing
any row sum. Process the tree towards the root. The root residual
vanishes because total supply equals total demand. The certificate
stores the resulting exact fractions, and the verifier independently
checks (2) and positivity. It does not need to trust the proposal or
the correction algorithm.

## 3. Outward entropy bounds

The verifier imports the existing rational interval engine. For
\(0<t<1/2\), it bounds
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du
 =t\log(2\pi t)-t
  -\sum_{k=1}^{20}\frac{\zeta(2k)t^{2k+1}}{k(2k+1)}
  -\mathcal R(t),                                                \tag{5}
\]
where
\[
             0\leq\mathcal R(t)\leq
                   \frac{2t^{43}}{21\cdot43(1-t^2)}.            \tag{6}
\]
The tail bound follows from \(\zeta(2k)<2\), with denominators bounded
below by \(21\cdot43\). The engine encloses \(\pi\), logarithms, and
\(\zeta(2k)\) by rational series, using outward integer rounding at scale
\(10^{40}\). The endpoint values \(J(0)=J(1/2)=0\) are exact. Since
\[
                       f_{\mathrm{tri}}(a)=-J(a)-J(1/2-a),            \tag{7}
\]
summing these intervals gives
\[
 67.688246275129
 <\sum_{T,v}f_{\mathrm{tri}}(\alpha_{T,v})
 <67.688246636527.                                               \tag{8}
\]
The full rational endpoints are retained in the result JSON. All
comparisons and the claimed lower threshold are verified without
floating-point evaluation or an optimizer.

The files are:
- \(\texttt{md-r54-complete-flow-lower-certificate.json}\), exact data;
- \(\texttt{md-verify-r54-complete-flow-lower.py}\), independent verifier;
- \(\texttt{md-r54-complete-flow-lower-results.json}\), its executed result;
- \(\texttt{md-build-r54-complete-flow-lower.py}\), the nonessential proposal
  script.

The existing complete source and geometric identification supply (4)
and the normalization in (1). This finite certificate checks their
specific feasible-flow input; it does not reprove those general
geometric theorems.

