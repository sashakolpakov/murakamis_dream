# An exact compatibility constraint at the terminal boundary

Research deduction, 5 November 2026. The independent endpoint-input disks
contain points that cannot occur in an actual open word. This note derives
one necessary compatibility condition and excludes the previously certified
raw-envelope obstruction at its exact input. It proves neither a raw gap on
the remaining domain nor an asymptotic theorem for the full open source.

## 1. The ordinary vertex preceding the endpoint

Use the original logarithmic critical point from
[open localization](research_mixed_open_word_critical_localization.md).
For a word of length \(m\ge3\), let its penultimate ordinary vertex have
type \(3+\nu\), and write
\[
 a=t_{m-1},\quad s=s_{m-1},\quad c=t_{m-2},\quad
 b=s_m,\qquad d=2+\nu.                                  \tag{1}
\]
The last endpoint map, of its own type \(3+\epsilon\), gives
\(b=b_\epsilon(a)\). In particular \(a\) and \(b\) cannot be
chosen independently. Set
\[
 V=e^{-2\pi ia},\quad U=e^{-2\pi is},\quad
 A=e^{-2\pi ic},\quad B=e^{-2\pi ib}.                    \tag{2}
\]
The two original zero-log equations at the ordinary vertex are
\[
\begin{split}
 g'(s+a)+g'(a+b)-d g'(a)+2\pi ib&=0,\\
 g'(s+a)+g'(s+c)-d g'(s)+2\pi ic&=0,
\end{split}                                             \tag{3}
\]
where \(g'(z)=\log(1-e^{-2\pi iz})\) is the original lift.
Exponentiating these already established equations gives the necessary
identities
\[
 (1-UV)(1-VB)=B(1-V)^d,\qquad
 (1-UV)(1-UA)=A(1-U)^d.                                 \tag{4}
\]
Consequently every such actual point satisfies
\[
 U=\frac{1-B(1-V)^d/(1-VB)}{V},\qquad
 A^{-1}=U+\frac{(1-U)^d}{1-UV}.                          \tag{5}
\]
All denominators in this necessary deduction are nonzero. Exponentials
are nonzero, and the original leg-sum strips have real parts in \((0,1)\),
so \(1-VB\ne0\) and \(1-UV\ne0\). Equivalently the denominator
in the solved expression for \(A\) is \((1-UV)/A\ne0\).
No converse to (4) is asserted: exponentiation has forgotten the
logarithmic residual integers.

Every original ordinary leg lies in
\(Q=[.23,.45]+i[-.12,.12]\). Thus the first expression in (5) must obey
\[
                    e^{-.24\pi}\le |U|\le e^{.24\pi}.  \tag{6}
\]
The stronger universal ordinary-block bounds from
[Proposition 1 of the critical-height note](research_mixed_cyclic_critical_height_bounds.md)
also apply here. That proposition first bounds the holomorphic block map
on the whole external bidisk; its subsequent cyclic fixed-point application
is unnecessary for this use. The two external legs of the actual
penultimate block are in the original typed disks, and uniqueness identifies
the same ordinary branch. It follows that
\[
\begin{array}{c|c}
 \nu=0&e^{-13\pi/100}<|U|<e^{17\pi/125}\\
 \nu=1&e^{-51\pi/250}<|U|<e^{-\pi/500}.
\end{array}                                             \tag{7}
\]
For the preceding leg, the common smaller disks give
\(\Im c<.073\) or \(\Im c<.008\), according to its type.
Hence \(\log|A^{-1}|+2\pi h_{\max}>0\), using the appropriate
one of these two upper heights. This remains valid when that preceding
leg is the first endpoint's attached leg. An ordinary-block-only upper
height must not be imposed there.

When \(m=2\), the penultimate vertex is the first endpoint. Equations
(3) do not apply. Instead its attached coordinate \(a\) lies in the
corresponding actual endpoint image from
[the exact image extraction](research_mixed_open_word_endpoint_rectangles.md).
For \(m=1\) there is no terminal conditional factor of this form.

## 2. The fixed raw-envelope obstruction is incompatible with an open word

The [archived fixed-point comparison](../repro/diagnostics/2026-11-05-terminal-raw-full-disk-boundary/README.md)
uses last type three, preceding type three, and
\[
             a=\frac{967}{3200}+\frac7{128}i.            \tag{8}
\]
It is an allowed independent endpoint-map input in the smaller type-three
disk. Its literal lower raw row at \(v=67/250\) exceeds the optimized
terminal phase by more than \(7/10000\). That remains a valid obstruction
to the independent-disk raw comparison.

The focused certificate here uses exactly the old endpoint root witness
at node 1685 of the \((\epsilon,\nu)=(0,0)\) family. It revalidates
both its original whole parameter cell and its radius-\(10^{-10}\)
point self-map at (8), retaining the original zero-log equations. The
first expression in (5), with \(d=2\), then satisfies
\[
                         |U|<e^{-.24\pi}.               \tag{9}
\]
This contradicts even the coarse necessary condition (6), so (8) cannot
be the actual terminal neighbor of an open word of length at least three
with these types. No logarithm or inverse-log branch is used in this
exclusion. For length two, \(\Im a=7/128>.021\), whereas the
type-three first-endpoint attached image has imaginary part below .021.
Thus length two is excluded separately.

This removes one proposed actual-word realization, not a neighborhood
theorem. In particular, deleting infeasible pieces of the outer disk
boundary does not by itself establish a minimum principle on the remaining
feasible set: its newly introduced boundary also needs control.

## 3. Reproduction and separate cell evidence

The focused checker is
[check_mixed_terminal_inverse_constraint.py](../experiments/check_mixed_terminal_inverse_constraint.py).
It verifies four rational identities for (4)--(5), the exact point and
original tree location, both old zero-log self-maps, the strict modulus
exclusion, and the separate length-two image exclusion. It binds the
original author/replay and fixed raw-obstruction record. It proposes no
new root and no parameter subdivision.

The separate
[22-cell extraction](../repro/diagnostics/2026-11-05-terminal-raw-full-disk-boundary/check_inverse_exclusions.py)
tests the old failed cells using whole-cell enclosures and the same implicit
endpoint response. Its successful exclusions are necessary-condition
exclusions; its surviving cells are merely interval-inconclusive. That
diagnostic extraction is not an acceptance input for the point theorem
(9), and neither record asserts a full feasible-domain raw gap.
