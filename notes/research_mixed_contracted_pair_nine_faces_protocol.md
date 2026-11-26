# A fixed tangent certificate for the contracted pair's physical remainder

Research calculation protocol, 7 November 2026. This protocol is fixed
before the calculation. It concerns the physical indices of the exact
three-four contraction, with both outside parameters equal to the
original alternating reference. It does not estimate complex contour
corrections or prove a knot volume limit.

## 1. The written reduction and the assertion to check

[The nine-face theorem](research_mixed_contracted_pair_nine_face_tail.md)
reduces the complete physical complement to the eight faces of
\[
 C=[1/4,9/20]^2\times[1/5,21/50]^2
\]
and the additional face
\[
 F_0=\{s=0,\quad t\in[1/4,9/20],\quad p,q\in[1/5,21/50]\}.
\]
The coordinates are ordered \((s,t,p,q)\). A separate far region has
already been bounded by \(2261/1500<M-1/200\), where
\(M>3781/2500\) is the original calibrated critical action.
Each of the nine remaining restrictions of the real rate is smooth
and strictly concave on its three-dimensional closed rectangle.

For each face, with free-coordinate bounds \(L_i,U_i\), and any
point \(y\) on that face, concavity gives the global bound
\[
 \sup_F E\le E(y)+\sum_{i\text{ free}}
  \max\{E_i(y)(L_i-y_i),E_i(y)(U_i-y_i)\}.
 \tag{1}
\]
Thus no numerical claim that \(y\) is a critical point is needed.
The precise fixed target for all nine upper bounds is
\[
             U_F<\frac{3781}{2500}-\frac1{100000}.
 \tag{2}
\]
If all nine comparisons hold, the written reduction proves
\(\sup_T E<M-1/100000\) for the entire physical complement.
If any comparison fails, this calculation does not prove that bound.
No failed tangent comparison alone disproves the true maximum bound.

## 2. Parameters and the functions evaluated

The parameter \(a\) is the original isolated root of
\(4a^4-6a^3+4a^2-2a+1\), enclosed by the saved root certificate.
Use its enclosing coordinate square without shrinking it. The
original reference is
\[
 K=(1+2a-4a^2)^{-1},\qquad \rho=|K|.
\]
The branch identification is the one in
[the three-vertex reference proof](research_three_vertex_mixed_reference_packet.md),
equation (2). For real \(v\in(0,1)\), use
\[
 J(v)=\Re\left[
 -\frac{i\pi}{2}(v^2-v)
 +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iv})
 -\frac{i\pi}{12}\right],
\]
and
\[
 I_K(v)=\Re\frac{
  \operatorname{Li}_2(Ke^{-2\pi iv})-\operatorname{Li}_2(K)}{2\pi i},
 \qquad H(v)=v\log\rho-I_K(v).
\]
All factorial arguments used at support points are strictly between
zero and one; the denominator arguments lie inside the unit disk.
The exact rate is
\[
 E=-\log\rho+J(s+t)+J(t+p)+J(p+q)
       -2J(t)-3J(p)-J(q)+H(s)+H(q).
 \tag{3}
\]
At \(s=0\), its external contribution is exactly zero. No singular
factorial evaluation at zero is needed. Writing
\(d(v)=|1-Ke^{-2\pi iv}|\), the derivatives are
\[
\begin{split}
 E_s&=\log\frac{2\rho\sin\pi(s+t)}{d(s)},\\
 E_t&=\log\frac{\sin\pi(s+t)\sin\pi(t+p)}{\sin^2\pi t},\\
 E_p&=\log\frac{\sin\pi(t+p)\sin\pi(p+q)}{2\sin^3\pi p},\\
 E_q&=\log\frac{\rho\sin\pi(p+q)}{\sin\pi q\,d(q)}.
\end{split}
 \tag{4}
\]
These formulas are differentiated from (3), not inferred from a
separately normalized vertex rate.

## 3. A deterministic choice of supporting points

The calculation treats the faces in this fixed order:
\(s=1/4,9/20\), \(t=1/4,9/20\),
\(p=1/5,21/50\), \(q=1/5,21/50\), and finally \(s=0\).
On each face, start its three free coordinates at their midpoints.
Use the rational center of the saved root disk, converted to binary
floating point, to propose a supporting point. Perform exactly 32
Newton steps with the analytic three-by-three restricted Hessian.
The first eight steps have damping factor \(1/2\); the last 24
have factor one. After each step, clamp each free coordinate to
\([L_i+10^{-8},U_i-10^{-8}]\). There is no line search, tolerance
test, early termination, random input, or precision adjustment.

The Hessian uses \(c(v)=\pi\cot(\pi v)\) and
\(h(v)=2\pi\Im(Ke^{-2\pi iv})/d(v)^2\):
\[
\begin{split}
 E_{ss}&=c(s+t)+h(s),& E_{st}&=c(s+t),\\
 E_{tt}&=c(s+t)+c(t+p)-2c(t),& E_{tp}&=c(t+p),\\
 E_{pp}&=c(t+p)+c(p+q)-3c(p),& E_{pq}&=c(p+q),\\
 E_{qq}&=c(p+q)-c(q)+h(q).
\end{split}
\]
The other entries vanish. Round each proposed free coordinate to
the nearest multiple of \(10^{-12}\), then verify its interval
membership exactly using rational arithmetic. Fixed coordinates
are their exact rational face values throughout.

These floating-point operations are not proof steps. They choose
the points in (1). Their convergence or accuracy has no bearing
on the validity of an outward tangent bound. A proposal failure
is recorded as a failure; it does not trigger another procedure.

## 4. The rigorous calculation and its immutable inputs

At the selected rational points, evaluate (3)--(4) with Arb/Acb
at exactly 256 bits, using the complete saved root square. For
each free coordinate, take the larger of the two outward upper
endpoints of the products in (1). Add these upper endpoints to
the rate enclosure. Compare the resulting enclosure with (2)
by a strict interval comparison. Record all nine results, even
if one does not pass. The overall status passes only if all nine
strict inequalities pass and every input binding is valid.

The root source is
`repro/results/research-three-four-source-interface.json`, SHA-256
`9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd`.
Its status, generating-script hash, and every recorded dependency
hash must agree with the files before its root is used. The action
lower bound is inherited from the two written packet theorems;
their saved supporting records are bound without recomputing their
contours:

| File | SHA-256 |
| --- | --- |
| `repro/results/research-three-vertex-mixed-reference.json` | `be27579fe6329c85d9617d00a7299ef67d75d1342ad7b0af5b589838c82650f2` |
| `repro/results/research-power-four-index-contours.json` | `10c9deacd149b8130867c659a1fb45d5793e4b318ea85424e8656dcdad71e79a` |
| `notes/research_mixed_contracted_pair_nine_face_tail.md` | `fb68bce3c63f60d5aa5bc24469ccfba7120e6d424a9d89f7e902c5ca58c71b7b` |
| `notes/research_mixed_contracted_pair_rectangle.md` | `a784131ce05513342bf86af5c531a5419ad38234f876dbfa9bb22ddbafa5340a` |
| `notes/research_mixed_contracted_pair_outer_index_elimination.md` | `231d52a52fab4f5eb2f10cb7fa721f7be586181c2f2407d9a587cf43370fbf5f` |
| `notes/research_three_vertex_mixed_reference_packet.md` | `71e5b3c4ad29bdfe49d4fb1c95dc658e86f19ff2656621b6bcf495222b59b849` |
| `notes/research_power_four_source_packet.md` | `6d572795eb2482e988c3761d2d56910b48d8f0a9459b6db44f3ca7365328087a` |

The checker is `experiments/check_mixed_contracted_pair_nine_faces.py`.
Its final hash and this protocol's final hash are recorded before
execution, after full proof and code reads by the root and a second
agent. Only the root executes it. Its sole output is the new file
`repro/results/research-mixed-contracted-pair-nine-faces.json`, opened
with exclusive creation. The output includes the input, script and
protocol hashes, exact support coordinates, interval values and
derivatives, each tangent bound, and every success or failure.

There is one execution with these parameters. The procedure does
not permit retries, a changed threshold, new supporting-point
rules, refined root data, or a different precision after inspecting
the output. Further work, if necessary, begins with a written
mathematical explanation of what failed. The frozen manuscripts
and public documentation are not modified by this calculation.
