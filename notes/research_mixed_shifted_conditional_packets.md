# Complete conditional packets at the shifted outer height

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The canonical conditional sources remain controlled when any selected
four-type outer variables are moved to height \(7/500\). The theorem
below includes every finite row, including revived rows, and every
original index-contour current. It concerns fixed parameter rectangles;
it does not estimate the remainder of a whole outer torus.

## 1. Five affected source families

Put
\[
 \begin{split}
 R_3&=[.267,.433]+i[-.065,.068],\\
 R_-&=[.27,.33]+i[-.057,-.001],\\
 R_+&=[.27,.33]+i[.01399,.01401].
 \end{split}
 \tag{1}
\]
Use the single canonical finite sum \(\mathcal L_{\epsilon,N}\),
phase \(Q_\epsilon\), and symbol \(A_\epsilon\) from equations
(3)--(4) of the
[critical-image source theorem](research_mixed_conditional_critical_images.md).
The required ordered families are exactly
\[
 (\epsilon,\alpha,\beta)\in
 (0,R_+,R_3),\quad(1,R_3,R_+),\quad
 (1,R_-,R_+),\quad(1,R_+,R_-),\quad(1,R_+,R_+).
 \tag{2}
\]
They distinguish the left neighbor from the vertex's own outer leg.
An unaffected conditional factor is left at its actual critical-image
germ; no larger unshifted independent-parameter theorem is assumed.

Lemma 1 of the
[reoptimized-action theorem](research_mixed_reoptimized_alias_action.md)
gives the unique original root \(z=z_\epsilon(\alpha,\beta)\) of
\(Q_{\epsilon,z}=0\) in
\([.15,.49]+i[-.12,.12]\), holomorphically on a neighborhood of
each whole product in (2). Its parameter rectangles contain (1),
including the open margin around height \(.014\).

**Theorem 1.** Uniformly on all five products (2), for both level
parities and the entire original canonical finite sum,
\[
 \mathcal L_{\epsilon,N}(\alpha,\beta)
 =N^{(1-\epsilon)/2}
   \frac{\sqrt{2\pi}A_\epsilon(z;\alpha,\beta)}
        {\sqrt{-Q_{\epsilon,zz}(z;\alpha,\beta)}}
   e^{NQ_\epsilon(z;\alpha,\beta)}(1+O(N^{-1})).
 \tag{3}
\]
The coefficient is holomorphic and nonzero. The normalized expansion
has every fixed holomorphic derivative on smaller products and every
fixed stationary-phase order. Equivalently, the actual Laurent kernel
\(C_{\epsilon,N}=\mathcal L_{\epsilon,N}/
 [\widehat P_N(N\alpha)\widehat P_N(N\beta)]\) has power
\(N^{-(1+\epsilon)/2}\), phase
\[
       Q_\epsilon(z;\alpha,\beta)-g(\alpha)-g(\beta),
 \tag{4}
\]
and coefficient
\[
 \frac{\sqrt{2\pi}A_\epsilon(z;\alpha,\beta)}
      {\sqrt{-Q_{\epsilon,zz}(z;\alpha,\beta)}}
 \frac{e^{\pi i(\alpha+\beta)/2}}
      {\sqrt{2\sin\pi\alpha}\sqrt{2\sin\pi\beta}}.
 \tag{5}
\]
Thus no unspecified continuation through the physical grid is used.

## 2. The full source certificate

Each parameter rectangle has four oriented sides. The checker covers
all \(5\cdot4^2=80\) distinguished-boundary pieces by exact dyadic
two-parameter cells. Its affine one-variable Newton enclosures retain
the original logarithmic equation. The polynomial stationary equation
is used only to propose a center; the unsquared equation and a point
Newton test fix its original lift.

On every accepted cell the selected root is enclosed in
\[
                 .20<\Re z<.44,\qquad |\Im z|<.12.
 \tag{6}
\]
With \(\ell=.15\), \(u=.49\), \(h=.2\), and
\(M=\Re Q_\epsilon(z;\alpha,\beta)\), the outward checks are
\[
 \begin{split}
 M-\Re Q_\epsilon(\ell;\alpha,\beta)&>10^{-4},\\
 M-\Re Q_\epsilon(u;\alpha,\beta)&>10^{-4},\\
 M-H_\epsilon(1;\alpha,\beta)&>10^{-4},\\
 M-\Re Q_\epsilon(x\pm ih;\alpha,\beta)+2\pi h&>10^{-3}
                  \quad(\ell\le x\le u).
 \end{split}
 \tag{7}
\]
Here \(H_\epsilon\) is the original periodic product entropy of the
full finite sum. Its last-row expression is checked as the same four
holomorphic branches used in (8) of the critical-image proof.
The exact quartic/sextic right-tail test is also checked on twelve
intervals, with an upper bound strictly below one on each. The whole
right tail therefore has its maximum at \(u\) or \(1\).
The analytic left-tail slope and the uniform
\(-\Re Q_{\epsilon,zz}>1/8\) on
\([\ell,u]+i[-h,h]\) follow from the
[contour reductions](research_mixed_conditional_image_contours.md).

The parameter gap derivatives here simplify because the neighbors are
independent. For a fixed contour point \(c\), they are
\[
 \begin{split}
 \partial_\alpha\{Q_\epsilon(z)-Q_\epsilon(c)\}
     &=g'(z+\alpha)-g'(c+\alpha)+2\pi i(z-c),\\
 \partial_\beta\{Q_\epsilon(z)-Q_\epsilon(c)\}
     &=g'(z+\beta)-g'(c+\beta).
 \end{split}
 \tag{8}
\]
The \(z\)-response vanishes from these formulas by the original
stationarity equation. The checker integrates outward real-part
bounds of (8) along each affine boundary parameter; it does not
replace a parameter cell by its midpoint value.

The complete contour argument is now the one proved in Sections 3--4
of the critical-image theorem. Absolute real tails retain the revived
endpoint. The original counterclockwise cotangent constants give
exactly \(+N\) times the zero-mode integral. Both horizontal
remainders carry \(e^{-2\pi Nh}\); the half-grid vertical remainders
carry \(e^{-2\pi N|y|}\). Height convexity bounds those full vertical
currents by (7). Deforming only the zero mode to the selected critical
height introduces two vertical joins; (6) and the \(1/8\) curvature
give their critical-height endpoint loss at least \(1/6400\).
Their real endpoints are covered by (7), so height convexity also
controls these joins. All margins survive half-grid rounding.

The exact regular factorial interpolant has symbol
\(N^{-\epsilon/2}A_\epsilon e^{NQ_\epsilon}\).
The zero-mode scalar \(+N\) and its Gaussian factor \(N^{-1/2}\)
give precisely (3). This proves the packet on every distinguished
boundary. Its normalized error is a holomorphic function on the
entire parameter product, with a nonzero leading denominator.
Two maximum-modulus applications prove it on the full products (2).
The same argument gives higher symbols and normalized derivatives.
Dividing by the two original marked factorial symbols proves (4)--(5).

## 3. What this supplies for the wrapped outer terms

Every conditional factor affected by moving a nonempty subset of
four-type outer variables to \(\Im t=.014\) belongs to one of (2).
Unaffected factors retain the previously proved actual-critical germ.
Hence Theorem 1 supplies the complete conditional kernels in the
local configuration of the reoptimized-action theorem, with their
original coefficients and level powers.

Combining that theorem with the exact torus formula consequently gives
the following **local full-conditional-density** bound. For every fixed
word and nonempty wrapped subset \(S\), at the outer coordinates
whose selected heights are \(.014\) and whose real parts are the
original geometric real parts,
\[
 |\text{the exact outer density of this wrapped term}|
     \le \operatorname{poly}(N)e^{N(M-|S|/125)}.
 \tag{9}
\]
The actual polynomial Fourier weights \(d_N\) and the exact outer
\(N\)-powers are retained. A fixed small real neighborhood retains
the weaker gap \(|S|/250\), for each fixed word. This conclusion
uses the reoptimized action; the internal critical coordinates are
not frozen at their pre-shift values.

This is a genuine source bound for the local outer density because
each conditional sum is complete. It is still not a bound for the
rest of an outer contour or for the total wrapped integral.
No mixed-word knot-volume theorem follows from this local statement.

## 4. Reproduction

Run:

    python3 experiments/certify_mixed_shifted_conditional_packets.py

The record contains all exact dyadic cells and rational affine Newton
witnesses. It checks the original logarithmic equations, every
inequality in (7), the complete tail-shape intervals, and exact
coverage of all 80 pieces. Root existence on the whole parameter
products remains the explicit independently proved input cited above.
