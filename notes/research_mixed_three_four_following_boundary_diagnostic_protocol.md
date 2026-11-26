# A fixed full-circle cover for two following-reference remainder margins

Protocol, 7 November 2026. This proposes one nonadaptive certified cover
of both complete reduced-disk boundary circles. It is not authorized
for execution until the root and an independent peer have reviewed the
protocol and standalone checker, and a final manifest binds their bytes
and the complete source/provenance dependencies. Only the root executes
the single frozen attempt. No numerical evaluation was used to choose
or write this protocol.

## 1. Original source, action and scope

Use exactly the five-variable action, variable order, original logarithmic
equations, Hessian and primitive of the completed
[two-center protocol](research_mixed_three_four_following_action_diagnostic_protocol.md),
Equations (1)--(3) and (8). Write its unknowns as
\(v=(e,a,u,t,z)\), its external input as \(c\), and its critical action as
\[
 \mathscr P(c)=P(v_*(c))=H(v_*(c);c)-G(z_*(c),c).
 \tag{1}
\]
The absolute constant and endpoint chirp are unchanged. The final Gram
contribution is removed explicitly; no post-Gram value is substituted
for (1). The checker copies these formulas literally and does not import
or execute either prior checker.

The [actual following-sheet theorem](research_mixed_three_four_following_critical_curve.md)
proves the unique original-log branch on a neighborhood of the full
closed typed disks \(D_3,D_4\). Its last leg \(z(c)\) lies in \(O_4\),
and its action and last leg are holomorphic. It also proves that
\[
 D_0(c)=7/4-\Re\mathscr P(c),\qquad
 D_+(c)=\mathfrak C(e^{2\pi\Im z(c)})-\Re\mathscr P(c)
 \tag{2}
\]
are respectively harmonic and subharmonic. Here, without optimization,
\[
 \begin{split}
 \mathfrak C(R)&=17539/9600-23/64000-6\beta(R)/25+\beta(R)^2/20,\\
 \beta(R)&=\tfrac12\log\frac{2}{1+R^2}.
 \end{split}                                                     \tag{3}
\]
These are the established bounds for the complete initial interval and
complete complementary-contour source, respectively. Neither one is an
estimate for the unexamined plateau/taper pieces at following references.

The proposed cover uses the two **full closed reduced disks**
\[
 P_3=\{|c-(7/20-i/100)|\le83/1000\},\qquad
 P_4=\{|c-(3/10-13i/250)|\le3/50\}.
 \tag{4}
\]
They are strictly inside \(D_3,D_4\), respectively, and contain all four
clipped following domains \(A_3,O_3,A_4,O_4\). If every circle cell has
both positive certified margins, the maximum principles for (2) extend
those two margins to both full disks. There is consequently no missing
clipping chord: those chords lie inside disks whose entire circles were
covered. A failed or inconclusive cell remains in the result and does
not license a reduced-domain assertion by omission.

## 2. Complete fixed inventory and starting points

For \(\nu=3,4\), write the center and radius in (4) as
\(c_\nu,\rho_\nu\). The exact boundary parameterization is
\[
 c_\nu(\theta)=c_\nu+\rho_\nu e^{i\theta},\qquad
 I_k=[2\pi k/512,2\pi(k+1)/512],\quad 0\le k<512.
 \tag{5}
\]
Both endpoints of every cell are retained; the first and last cells
share the periodic endpoint. The prescribed order is all 512 type-three
cells followed by all 512 type-four cells. There are exactly 1,024 cells,
no exclusions, adaptive subdivision or changed order.

The midpoint is \(\theta_k=(2k+1)\pi/512\), with halfwidth
\(\omega=\pi/512\). Arb enclosures of \(\pi\), sine and cosine enclose
the exact midpoint and full closed cell. No floating approximation to a
cell endpoint is used.

Every cell of a given circle starts independently from the exact rational
`final_center` of the corresponding `c3` or `c4` case in
`repro/results/research-mixed-three-four-following-action-centers-attempt01.json`,
SHA `43e55892e025cc21a88a749b0517102eb35164a98fa0558c8dd7903d238e8958`.
These are the recorded rational proposals, not assertions that a root is
rational. The manifest repeats these two vectors exactly. No result of
an earlier boundary cell is used as a later starting point.

At 256-bit precision perform exactly 24 Newton proposal steps for each
cell midpoint, rounding each coordinate after each step to its exact
binary64 rational midpoint, as in the prior protocol. Proposals are not
certificates. There is no early success stop. If proposals fail, record
the exception and processed history, then proceed to the next prescribed
cell from its original saved seed. There is no restart or alternative
proposal for the failed cell.

## 3. Two fixed complex-disk inclusions per cell

Let \(v_k\) be the final exact rational midpoint proposal. Form an exact
rational matrix \(Y_k\) by rounding the midpoint Jacobian inverse in the
same prescribed way. The following two tests use this **same** inverse:

1. At the exact circle midpoint, certify the root in the product of
   five complex disks centered at \(v_k\), each of radius
   \(r_0=2^{-30}\).
2. For every external \(c=c_\nu(\theta)\), \(\theta\in I_k\), certify
   its root in the product of five complex disks with the same center
   and the fixed radius \(r_1=1/256\).

For either test, let \(C\) enclose the prescribed midpoint or full
circle cell, and let \(B_r\) be Cartesian squares containing the five
complex disks. Require \(Y_k\) invertible and, for all five rows,
\[
 \begin{split}
 K_i&=\sum_j|(I-Y_kH_{vv}''(B_r;C))_{ij}|<1,\\
 |(Y_k\nabla_vH(v_k;C))_i|+rK_i&<r.
 \end{split}                                                     \tag{6}
\]
These are bounds in the maximum norm of the five complex coordinates.
The square enclosure is used only to evaluate derivatives and source
bounds; the contracted sets are products of disks. Formula (6) applies
for each fixed parameter in \(C\), so the second test is uniform on the
entire cell. This also makes its midpoint root agree with the first
test by uniqueness in the admitted original chamber.

For both radii retain every original branch, coordinate, typed-disk,
reduced-output-disk and negative-height guard in the two-center checker.
Every primitive argument must remain in its original regular real strip;
\(0<\Re u<1/2\) and \(0<\Re(e-u)<1/2\) retain the original auxiliary
logarithms. Disk membership uses center distance plus the disk radius;
height and primitive checks use the containing squares. Verify the
outgoing radius stays strictly between \(1/2\) and one on the entire
uniform box. Also verify the parameter enclosure remains in the
corresponding original typed disk. All failures are retained. The fixed
radius is never changed to make these tests succeed.

The known global existence and uniqueness theorem identifies both
inclusions with the actual half-chain branch. No agreement of
exponentiated equations, or of approximate roots alone, is used.

## 4. Midpoint actions and rigorous margin transport

Evaluate \(P,H,G\) only on the small \(r_0\) midpoint box, using the
original dilogarithm primitive. Record both midpoint margin intervals
from (2)--(3). No action is evaluated on the wider \(r_1\) box.

On that uniform box evaluate the original Hessian inverse and retain
\[
 \begin{split}
 Q&=e^{-2\pi iz},\qquad C=e^{-2\pi ic},\\
 z'(c)&=-(H_{vv}''(v_*(c);c)^{-1})_{zz}
                              \frac{2\pi i}{1-QC},\\
 p_z&=\mathcal P_{\rm act}'(z)=g'(t+z)-g'(z),\\
 c'(\theta)&=i\rho_\nu e^{i\theta}.
 \end{split}                                                     \tag{7}
\]
The denominator and the enclosed Hessian inverse must be certified
nonzero/finite. Formula (7) is the exact implicit derivative of the last
original equation. It uses no conjugation and no differentiated numerical
root approximation.

With \(h=\Im z\), the real derivative of the sharp ceiling is
\[
 B_h=\left(-6/25+\beta/10\right)
                \frac{-2\pi R^2}{1+R^2},\qquad R=e^{2\pi h}.
 \tag{8}
\]
Consequently the exact derivatives of the two margins along the circle
are
\[
 \frac{d m_0}{d\theta}=\Re[p_z z'(c)c'(\theta)],\qquad
 \frac{d m_+}{d\theta}
       =\Re[(p_z+iB_h)z'(c)c'(\theta)].
 \tag{9}
\]
In particular the sign of the second term in (9) is fixed by
\(\Re(iB_h\dot z)=-B_h\Im\dot z\).

Let \(L_0,L_+\) be outward bounds for the absolute values of these
**real** derivatives throughout the uniform cell enclosure. The full
cell margins lie in the recorded midpoint intervals enlarged by
\([-\omega L_j,\omega L_j]\). A cell is positive only if the lower
endpoints of both enlarged intervals are positive. Negative and
inconclusive interval verdicts are recorded without stopping the rest
of the inventory. A midpoint failure or an uncertified inverse is a
failed cell, not evidence of an action sign.

If all 1,024 cells pass, their finitely many strictly positive lower
bounds give a positive common margin on both circles and hence both
disks, by Section 1. Existing complete-source bounds then pay exactly
the two named remainders on these disks, with any smaller fixed margin
after polynomial factors; continuity and the existing normalized
holomorphic estimates give fixed local parameter derivatives. This does
not establish the remaining incoming contour estimates, a whole prefix
packet on the disks, either sector of the next attachment, a nonzero
next-word observation, or a knot-family theorem.

## 5. Frozen provenance, exclusive output and failure inventory

Checker: `experiments/check_mixed_three_four_following_boundary_cover.py`.
Manifest: `repro/protocols/research-mixed-three-four-following-boundary-cover.json`.
Output: `repro/results/research-mixed-three-four-following-boundary-cover-attempt01.json`.

The manifest binds this protocol and checker, the completed center result
and its original manifest, the final critical-curve theorem, all original
action/source/domain references, the sharp radial majorant, and every
saved dependency transitively. It records root and independent peer
static approvals before execution. The completed center result is used
only for its two fixed seeds and provenance; no old source checker is
imported, executed or replayed. Saved author/replay provenance is checked
with the same full inventories as in the center checker.

The result records all 1,024 identifiers at initialization, their circle,
cell index and exact rational angle multiples of \(\pi\), every rational
proposal and inverse, both complete inclusion tests and domain checks,
small-box actions, midpoint comparisons, uniform derivative enclosures,
transport debits and full-cell comparisons. It retains counters,
exceptions, the exact unprocessed inventory, all input hashes and any
hash invalidation. No failed cell is silently omitted. A global preflight
failure leaves the full inventory unprocessed and is recorded.

Only a complete inventory with every cell certified positive can have
verdict `both_full_disks_have_positive_margins`. Other completed covers
retain their pointwise cell verdicts and assert no full-disk comparison.
The single fixed output is opened exclusively and never overwritten.
All bound files and the manifest are rehashed after the attempt; a change
invalidates it. There is no automatic replay, optimization or refinement.
