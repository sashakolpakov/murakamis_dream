# A revived-row obstruction on the untrimmed auxiliary product

Research proof, 5 November 2026. The last-row affine-plane comparison
fails on one of the complete reduced-disk conditional images, even
when the first type-four factorial halfweight is retained. The two
external inputs violate the already proved ordinary and attached-leg
height bounds. Thus this is an obstruction to using the whole
auxiliary product for the comparison, not an actual-word or
finite-kernel counterexample.

## 1. The original reference and the comparison

Use the original zero-lift two-leg map from the
[reduced-disk source theorem](research_mixed_reduced_disk_conditional_packets.md).
The own vertex has type three. Its external inputs, in the order
used by the saved source certificate, are
\[
 \begin{split}
 c&=\frac7{20}-\frac{i}{100}
             +\frac{83}{1000}e^{2\pi i(17/20)},\\
 a&=\frac3{10}-\frac{13i}{250}
             +\frac3{50}e^{2\pi i(159/200)}.
 \end{split}
 \tag{1}
\]
Thus \(c\in\partial P_3\), \(a\in\partial P_4\).
Write the original roots in the certificate order as \((b,s)\).
They satisfy both original logarithmic equations
\[
 \begin{split}
 0&=g'(b+s)+g'(b+c)-2g'(b)+2\pi ic,\\
 0&=g'(b+s)+g'(s+a)-2g'(s)+2\pi ia.
 \end{split}
 \tag{2}
\]
The conditional orientation under consideration is therefore
\((s;a,b)\), namely side one of the saved type case \((0,0,1)\).
No exponential equation is used to select its branch.

Retain the primitive and additive constant of the original source,
and the first type-four halfweight:
\[
 \begin{split}
 F(s;a,b)&=g(s+a)+g(s+b)-2g(s)
                  -\tfrac32g(a)-g(b)+2\pi ias,\\
 M&=\Re F(s;a,b),\\
 p_a&=\Re\{g'(s+a)-\tfrac32g'(a)+2\pi is\},\qquad
 p_b=\Re\{g'(s+b)-g'(b)\}.
 \end{split}
 \tag{3}
\]
For target real parts \(x=z=9/20\), keep the reference heights.
Since \(\Im a<0<\Im b\), the complete revived-row carrier and
the allocated last-row rate in the
[endpoint reduction](research_mixed_horizontal_revived_endpoint.md) are
\[
 E_1=2\pi(-\Im a+\Im b)
           -\tfrac12\Re g(9/20+i\Im a).
 \tag{4}
\]
This retains the same halfweight as (3). In particular the example
does not rely on removing the favorable factorial energy from the
[four-corner sufficient criterion](research_mixed_last_row_own_root_normal_form.md).

**Proposition.** At the original reference (1)--(2),
\[
 E_1-M-p_a(9/20-\Re a)-p_b(9/20-\Re b)
       >\frac9{2000}.
 \tag{5}
\]
The comparison also fails with the smaller affine-quadratic plane
obtained by subtracting
\(\{(9/20-\Re a)^2+(9/20-\Re b)^2\}/2500000\).

## 2. One inherited witness and outward evaluation

The exact parameters (1) lie in the accepted leaf at node 127 of the
original case tree. Its parameter rectangle is
\[
 [27/32,55/64]\times[25/32,13/16].
 \tag{6}
\]
The focused checker reconstructs that rectangle using the original
right-child-first traversal. It compares author and independent
replay trees, revalidates the saved affine root witness on the whole
rectangle, and restricts the same witness to (1). It makes no root
proposal and subdivides no parameter cell.

For fourteen fixed tightening steps it uses that witness's unchanged
rational inverse \(Y\). If \(Z\) encloses the original root and
\(z_0\) is its midpoint, then
\[
 z_0-Yf(z_0)+(I-Yf'(Z))(Z-z_0)
 \tag{7}
\]
still encloses it by the integral mean-value formula. All intervening
single-leg and two-leg arguments remain in their original regular
strips. This is an enclosure of the already identified root, not a
new branch-selection argument.

The resulting enclosures include
\[
 \begin{split}
 a&\simeq .31673946636235-.10961762114062i,\qquad
 c\simeq .39878617594028-.07714841053312i,\\
 s&\simeq .40052928206580+.02074036874709i,\qquad
 b\simeq .33821502157972+.01655806034572i,\\
 E_1&\simeq .80286686016416,\qquad
 M+p_a(9/20-\Re a)+p_b(9/20-\Re b)
       \simeq .79832341966208.
 \end{split}
 \tag{8}
\]
The outward difference is greater than \(.00454344050208\),
which proves (5). The checker uses the original dilogarithmic
values, both original logarithmic equations and the exact signed
first-argument chirp.

## 3. Why this is not an actual open-word obstruction

The [ordinary image bounds](research_mixed_cyclic_critical_height_bounds.md),
transferred to open ordinary vertices by
[local factor coverage](research_mixed_open_local_factor_coverage.md),
give \(\Im a>-.102\) at an ordinary type-four input and
\(\Im c>-.065\) at an ordinary type-three input. Both fail in
(8). Even the weaker
[attached endpoint bounds](research_mixed_open_word_endpoint_rectangles.md)
give \(\Im a>-.108\) and \(\Im c>-.072\), and both also
fail. Private endpoint legs have still higher lower height bounds.
The fixed auxiliary inputs (1) therefore cannot be the corresponding
legs of an actual open word.

The proposition concerns the stated allocated entropy formula and
its moving reference plane. It does not establish a lower bound for
the signed finite conditional sum, a nonzero revived physical row,
failure of a complete finite-source estimate, or noncancellation or
cancellation of a knot invariant. In particular it does not enlarge
any physical Fourier-rate domain. It shows that the untrimmed
auxiliary reduced product cannot prove the required endpoint
comparison by itself. The known ordinary/attached geometry must be
retained in any subsequent uniform use.

Reproduction, with no search or new cover:

```sh
python3 experiments/check_mixed_last_row_auxiliary_obstruction.py --precision 256 --output repro/results/research-mixed-last-row-auxiliary-obstruction.json
python3 experiments/check_mixed_last_row_auxiliary_obstruction.py --precision 320 --input repro/results/research-mixed-last-row-auxiliary-obstruction.json --output repro/results/research-mixed-last-row-auxiliary-obstruction-replay.json
```
