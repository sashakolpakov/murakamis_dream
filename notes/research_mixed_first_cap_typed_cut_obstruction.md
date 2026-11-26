# A positive first-cap cut deficit inside the typed auxiliary domain

Research obstruction, 5 November 2026. Two prescribed rational inputs
to the original endpoint map give a positive deficit at the real
private cut \(e=.27\). Thus reducing the requested positive gap cannot
repair that cut comparison on the whole typed auxiliary domain. This
does not identify either input with an actual open word, and it is not
a failure of the complete finite cap, its local packet, or the volume
conjecture. No new parameter search or root proposal is involved.

## 1. Exact inputs and the original branch

Use the own-four, neighbor-four endpoint map of
[open localization](research_mixed_open_word_critical_localization.md).
Write its external input as
\[
 b=\frac3{10}-\frac{13}{250}i+\frac8{125}(\xi+i\eta).
\]
Take the two points
\[
 (\xi,\eta)=\left(-\frac{15359}{16384},0\right),
 \qquad
 (\xi,\eta)=\left(-\frac{15359}{16384},\frac1{1024}\right).
 \tag{1}
\]
Both lie strictly in the typed input envelope
\[
 K_4=\{|b-(.30-.052i)|\le.060\}
                         \cap\{-.108\le\Im b\le-.001\}.
 \tag{2}
\]
Indeed its normalized radius is \(15/16=15360/16384\), and
the positive squared-radius numerators for (1) are respectively
\[
 15360^2-15359^2=30719,
 \qquad 15360^2-15359^2-16^2=30463.
 \tag{3}
\]
Their normalized heights are strictly between \(-7/8\) and
\(51/64\). Their common real part is \(61441/256000\),
and their imaginary parts are \(-13/250\) and \(-831/16000\).

The original complete root tree places both points in global
accepted-cell index 4933, with normalized parameter rectangle
\[
 [-15/16,-29/32]\times[0,1/16].
 \tag{4}
\]
This is the zero-based accepted-cell index in the four original
right-first trees, not a tree-node index. The inherited rational
center, inverse and radius certify the original unexponentiated
root \((e_*,z_*,u_*)\) on the whole rectangle (4). The same
root witness, with both own and neighboring flags equal to one,
is retained at each point. Interval Taylor-image intersections
only tighten its enclosure; they neither propose another root nor
change a logarithmic lift.

## 2. The comparison that fails

Use exactly the original allocated phase and marginal from
[the first-cap certificate](research_mixed_first_cap_plateau_certificate.md):
\[
 \begin{split}
 \Xi_1(e,z)&=S(e)+J(e+z)-J(z)-i\pi ez-g(e)-g(z)/2,\\
 L(z_*)&=F(e_*,u_*)+J(e_*+z_*)-J(z_*)-i\pi e_*z_*
                                      -g(e_*)-g(z_*)/2,\\
 p&=J'(e_*+z_*)-J'(z_*)-i\pi e_*-g'(z_*)/2.
 \end{split}
 \tag{5}
\]
Here \(S(e)=F(e,u_c(e))\) is the canonical complete-end
action on the proved endpoint-cap rectangle. The reference action
uses the inherited original \(u_*\), with no independent root
substitution. The outgoing argument is the attached output \(z_*\),
not the external parameter \(b\).

Set
\[
 y_0=\frac{372948142107}{10^{12}},\quad
 z_0=y_0+i\Im z_*,\quad d=y_0-\Re z_*,\quad
 \kappa=\frac1{2500000}.
\]
The fixed-target, zero-penalty left-cut deficit is
\[
 G=\Re\Xi_1(.27,z_0)-\Re L(z_*)-\Re p\,d+\kappa d^2.
 \tag{6}
\]
The target \(y_0\in[.22,.45]\) is the rational trial already
saved in the incomplete typed-domain attempt; it is not optimized
over new external inputs. Both the private factorial and the outgoing
physical halfweight remain in (5).

The existing fixed-point record reports the outward intervals
\[
 \begin{split}
 G(b_0)&\in[7.52703674266\cdot10^{-6}\ \mathord\pm\ 3.09\cdot10^{-18}],\\
 G(b_1)&\in[1.965356443722\cdot10^{-6}\ \mathord\pm\ 9.00\cdot10^{-19}].
 \end{split}
 \tag{7}
\]
These are enclosures of the **value at the fixed target**, before
adding any nonnegative target-optimization gain. Their lower
endpoints are positive. A failed upper-envelope acceptance alone
would not establish this conclusion.

The focused checker below verifies the conservative strict bounds
\(G(b_0)>1/200000\) and \(G(b_1)>1/1000000\). It uses the
unchanged audited source helpers, original author and saved replay,
and the same whole-cell witness. It checks exact membership (3),
both prescribed points, the saved rational trial, and all bindings.
No source or root cover is rerun. Equation (7) is the already
performed 256-bit author diagnostic, whose code has been independently
read. The new checker permits only a higher-precision saved replay of
that exact pinned diagnostic. It has not yet been executed; no second
256-bit author calculation is needed.

## 3. Consequence and limits

Once the two fixed comparisons are independently replayed, the
uniform assertion \(G\le-\delta\) over all of (2) is false for
**every** \(\delta\ge0\). Merely decreasing the requested
strict margin cannot establish that auxiliary cut comparison.
A narrower reference set or a different treatment of the real cut
is needed for this route.

This conclusion concerns a correlated original endpoint-map image,
not freely chosen independent output legs. Nevertheless neither input
is asserted to occur in an actual word. In particular both have real
part less than \(.246\), so the proved attached-endpoint rectangle
already excludes them as the opposite attached input of a length-two
word. Further restrictions from the ordinary neighboring equations
must be assessed with their own proved image bounds; this note does
not replace them by the whole auxiliary envelope.

The complete cap may cancel its real rows coherently. A positive
cut deficit therefore does not disprove a full finite-source upper
plane, a nonzero complete cap packet, or any knot asymptotic.
The previous incomplete author records remain immutable and make
no claim to prove the failed uniform condition.

## 4. Focused reproduction

The existing diagnostic is
[research-mixed-first-cap-typed-cut-fixed-points.json](../repro/results/research-mixed-first-cap-typed-cut-fixed-points.json).
The sole higher-precision checker is
[check_mixed_first_cap_typed_cut_obstruction.py](../experiments/check_mixed_first_cap_typed_cut_obstruction.py).
It requires the exact existing diagnostic path and hash, and permits
only the same two prescribed points and trial. The 256-bit author
record remains unchanged.

```sh
python3 experiments/check_mixed_first_cap_typed_cut_obstruction.py --precision 320 --input repro/results/research-mixed-first-cap-typed-cut-fixed-points.json --output repro/results/research-mixed-first-cap-typed-cut-obstruction-replay.json
```
