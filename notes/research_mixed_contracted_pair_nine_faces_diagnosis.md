# The two failed physical-tail faces exceed the actual critical action

Saved-data deduction, 7 November 2026. The sole prescribed
[nine-face calculation](research_mixed_contracted_pair_nine_faces_protocol.md)
is inconclusive: seven tangent bounds pass and two fail. The two
failures are not merely loose affine supports or a coarse lower
bound on the critical action. The saved **lower** rate bounds at
the corresponding rational trial points already exceed the actual
critical action. This obstructs the proposed absolute real-rate
comparison on the present physical complement; it is not a
counterexample to an estimate for the original signed finite source.

## 1. Immutable evidence and the actual action interval

The new record is
[`research-mixed-contracted-pair-nine-faces.json`](../repro/results/research-mixed-contracted-pair-nine-faces.json),
SHA-256
`174752c3b6f5c026dc4153287e153515d7f94e12959a0188f188d4cbf4d42cbc`.
Its generating checker has SHA
`94b35c6d1877737ca020d128e52a6bde77416ecbebc9d4c6ed01d82c1eb415ac`,
and its fixed protocol has SHA
`957aadc2dfc00126dd8474d0f3159081001c565326401adeb8f9d69fe43cfa74`.
All nine rigorous support bounds are valid, the record reports no
changed input, and its 33 input hashes still agree. The checker,
protocol and result are unchanged.

Let \(M=\Re\Phi_3+\Re\Phi_4\) be the absolutely calibrated
action in [the original contraction](research_mixed_contracted_pair_rectangle.md),
equation (10). Its two previously saved scalar enclosures are:

| Saved record | Scalar field | Enclosed margin |
| --- | --- | --- |
| [three reference](../repro/results/research-three-vertex-mixed-reference.json) | `critical total action exceeds .6562` | \(0.00007511472117960696605\pm3.35\cdot10^{-24}\) |
| [four index contours](../repro/results/research-power-four-index-contours.json) | `critical total action exceeds .8562` | \(0.000038597102117414432\pm5.22\cdot10^{-22}\) |

The respective record hashes are
`be27579fe6329c85d9617d00a7299ef67d75d1342ad7b0af5b589838c82650f2`
and
`10c9deacd149b8130867c659a1fb45d5793e4b318ea85424e8656dcdad71e79a`.
Both records and their generating scripts are bound by the new
record. The generating scalar checks explicitly subtract
\(3281/5000\) and \(4281/5000\) from the original calibrated
actions. Adding those constants and the displayed outward decimal
enclosures, as exact rational numbers, gives
\[
 \frac{30250274236465940427950493}{20000000000000000000000000}
 \ \le M\le\
 \frac{30250274236465940427971507}{20000000000000000000000000}
 <\frac{756257}{500000}=1.512514.
 \tag{1}
\]
This uses the upper endpoint of the actual action enclosure; it
does not substitute the protocol's weaker lower bound \(1.5124\).

## 2. Two exact supported trial excesses

Use the coordinate order \((s,t,p,q)\) and the original real
rate \(E\) from equation (3) of the protocol. The two saved
trial points, written as terminating rational decimals, are
\[
\begin{split}
 y_s&=(.45,\ .305175316565,\ .281506716344,\ .307605897026),\\
 y_t&=(.405298167609,\ .25,\ .285223641740,\ .307199619348).
\end{split}
 \tag{2}
\]
They lie on the indicated central-box faces. All coordinates are
positive and all three physical support sums are strictly below
one. No zero factorial or prohibited support face is involved.

The saved exact fractions in each row's `E_at_support.lower_rational`
give the strict comparisons
\[
 \begin{split}
 E(y_s)&>\frac{761517}{500000}=1.523034,\\
 E(y_t)&>\frac{757451}{500000}=1.514902.
 \end{split}
 \tag{3}
\]
Combining (1) and (3), using exact rational arithmetic, proves
\[
                       E(y_s)>M+\frac1{100},\qquad
                       E(y_t)>M+\frac1{500}.
 \tag{4}
\]
These use the saved rate lower endpoints, not the larger
`whole_face_upper_rational` tangent bounds. The latter are about
\(1.5230342\) and \(1.51490245\), respectively, and are
consistent with the same diagnosis.

The obstruction is not caused by assigning boundary points to the
tail. Continuity of the regular rate and the strict margins in (4)
give the same strict excess in sufficiently small neighborhoods.
Moving \(y_s\) slightly to \(s>9/20\), or \(y_t\) slightly
to \(t<1/4\), stays strictly inside the physical support and
outside the closed original central box. Thus the excess persists
in the genuinely exterior physical region.

## 3. Consequence for the next proof step

The criterion \(\sup_T E<M\) for the present real physical
complement \(T\) is false. Refining its Newton proposals,
improving its tangent accuracy, or replacing the coarse action
lower bound by its exact value cannot make that criterion true.
The seven successful face bounds remain valid statements about
their original faces.

This conclusion concerns the rate obtained by taking absolute
values of the supported physical rows. It gives no lower bound
for their signed sum, no obstruction to a deformation retaining
cancellation through the two high-rate neighborhoods, and no
failure of the knot-volume assertion. A different central domain
or a coherent treatment of these regions requires a new source
decomposition and proof of its contour and complement estimates.
The nonmain complex currents remain a separate obligation.

Only the saved decimal and rational enclosures were recombined
here. No analytic function, root, new trial point, optimizer or
contour calculation was evaluated, and the prescribed experiment
was not retried.
