# A uniform connector lower bound at the left cutoff

Research proof, 5 November 2026. This proves a local lower bound when
both neighbors of an isolated zero seam have real coordinate \(1/10\),
and a qualitative one-sided neighborhood consequence. A stronger real
pair bound uses sixty-four outward scalar comparisons, not a parameter
cover. It also gives an arbitrary-length region estimate for independent
seams whose neighbors lie in this small neighborhood. It does not assert
the full transition comparison or a whole-period estimate.

## 1. The original reference and repaired comparison

Let \((r_{-1},r_0,r_1)\) be an actual cyclic critical reference,
with type indicators \((\alpha,\beta,\gamma)\in\{0,1\}^3\).
The proved reference rectangles are
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{1}
\]
Write \(\phi_0=\phi_{\alpha\beta}\),
\(\phi_1=\phi_{\beta\gamma}\), retaining the original conditional
root, primitive, chirp and Fourier half-factorial allocation. The middle
critical equation is
\[
 \phi_{0,b}(r_{-1},r_0)+\phi_{1,a}(r_0,r_1)=0.
 \tag{2}
\]
Fix \(0<\ell\le1/1000\), independently of \(N\). The seam
coordinate is real in \([0,\ell]\), with attenuation
\(\lambda\in[0,1]\). Both adjacent nonseam coordinates are first
set equal to
\[
                       e=1/10,\qquad \xi=\Re r_0.
 \tag{3}
\]
All their permitted selections, inner A coordinates and inner halos
are retained. At \(e\), both slow and fast left cutoffs vanish.
Thus the physical and baseline-repaired endpoint heights are zero,
and both exact AA repair differences vanish. A selected correction
at \(e\) is also zero, since
\(\max\{\Re g(e),0\}=0\).

Use the baseline-halo three-step bound from the
[admissible-halo theorem](research_mixed_admissible_boundary_halos.md).
The outgoing state is \((q_{-2},q_{-1},p_0)\), and the incoming
state is \((p_0,q_1,q_2)\), at their prescribed layers. Here
\(p_0=(\xi,0)\) is an unselected reference symbol, whose actual
complex target in a connector can be reset by a neighboring real
coordinate. At (3), that target is \(\xi\), not \(r_0\).

Expanding the literal three-step functions leaves the four coherent
connector phases
\[
 \begin{split}
 {\cal C}={}&f_{\alpha\beta}(e,\xi)
             +\Re\phi_{\beta\gamma}(\xi,r_1)\\
            &+\Re\phi_{\alpha\beta}(r_{-1},\xi)
             +f_{\beta\gamma}(\xi,e),
 \qquad f_{\eta\epsilon}=\Re\phi_{\eta\epsilon}
       \text{ on real arguments}.
 \end{split}
 \tag{4}
\]
The other two connector edges are baseline edges of zero defect.
Their nonzero occupation shares and the additional outgoing/run
occupation losses are nonnegative and may be discarded in an upper
bound. Expanding the four original tangent planes and subtracting the
physical seam-pair plane gives exactly
\[
 F_* =\Re\{\phi_{\alpha\beta}(r_{-1},r_0)
                    +\phi_{\beta\gamma}(r_0,r_1)\}.
 \tag{5}
\]
Indeed the middle target coefficients cancel by (2), and the two
endpoint targets in this comparison are unchanged. Consequently the
complete local repaired-halo proxy is at most
\[
                          U_{\alpha\beta\gamma}+F_*-{\cal C},
 \tag{6}
\]
where \(U\) is the height-zero source ceiling with its full collar
cost, defined below. No additional reset debit is introduced.

## 2. Vertical convexity removes the complex reference variables

Define the background pair
\[
 B(z)=\phi_{\alpha\beta}(r_{-1},z)
                         +\phi_{\beta\gamma}(z,r_1).
 \tag{7}
\]
The straight vertical segment from \(r_0\) to \(\xi\) lies in
the unselected products of the
[full-height-reset theorem](research_mixed_full_height_reset.md).
Its positive negative-real Hessian makes
\(h\mapsto\Re B(\xi+ih)\) strictly convex. Equation (2) gives
\(B'(r_0)=0\); hence its minimum on this segment is at the
reference height. Therefore
\[
                         \Re B(\xi)\ge F_*.
 \tag{8}
\]
Inserting (8) into (4)--(6) reduces the required bound to the real
two-block function
\[
 L_{\alpha\beta\gamma}(x)
          =f_{\alpha\beta}(e,x)+f_{\beta\gamma}(x,e).
 \tag{9}
\]
The [real-outer support theorem](research_mixed_real_outer_support.md)
proves strict real concavity of both summands on the entire open
half-square. Thus (9) is concave on the closed middle interval
\[
 I_0=[.30,.39],\qquad I_1=[.27,.33],
 \quad
 L_{\alpha\beta\gamma}(x)
 \ge\min\{L_{\alpha\beta\gamma}(\inf I_\beta),
          L_{\alpha\beta\gamma}(\sup I_\beta)\}.
 \tag{10}
\]
This is a lower bound from concavity; no complex reference is substituted
into a real supporting-plane theorem. The only complex-reference step
was the vertical convexity argument (8).

## 3. Sixty-four scalar comparisons with the complete source

At height zero the proved
[height-resolved endpoint profiles](research_mixed_height_resolved_seam_sources.md)
give the exact rational upper values
\[
 \begin{array}{c|cc}
 A_{\beta,\alpha}(0)&\alpha=0&\alpha=1\\\hline
 \beta=0&.325066&.386681\\
 \beta=1&.460764&.515591
 \end{array}
 \qquad B_0(0)=.325066,\quad B_1(0)=.515591.
 \tag{11}
\]
Selected factors at these real targets have modulus one. Set
\[
 \nu_\ell=-J(\ell),\quad
 \Delta_\ell=\ell\log2-J(\ell),\quad
 U_{\alpha\beta\gamma}
 =A_{\beta,\alpha}(0)+B_\gamma(0)
                       +2\Delta_{1/1000}+\beta\nu_{1/1000}.
 \tag{12}
\]
This fixed larger collar cost bounds every \(\ell\le1/1000\):
on that interval \(J'(x)=\log(2\sin\pi x)<0\), so both
\(\nu_\ell\) and \(\Delta_\ell\) increase with \(\ell\).
The source estimate bounds every original finite row and its complete
Fourier halfweight, uniformly in both parities and every selection.
An arbitrarily small positive Fourier tolerance is kept separately.

The focused checker proves all sixty-four strict inequalities
\[
 f_{\alpha\beta}(a,x)+f_{\beta\gamma}(x,c)
                       -U_{\alpha\beta\gamma}>\frac{11}{50},
 \quad (\alpha,\beta,\gamma)\in\{0,1\}^3,
 \quad (a,c)\in\{1/10,1/2\}^2,\quad
 x\in\{\inf I_\beta,\sup I_\beta\}.
 \tag{13}
\]
It encloses twenty-four distinct inner roots by strict complex-disk self-maps
of the original logarithmic equation, checks their original regular
strips and selected cotangent chamber, and evaluates the original
dilogarithm primitive outward. Polynomial roots only propose disk
centers. The original zero-lift root theorem identifies the roots.
The smallest certified reserve in (13), before subtracting \(11/50\),
exceeds .2292.

In fact the sum in (13) is jointly concave in its three real arguments:
each summand is concave by the real-outer support theorem. Continuity
of the original root and phase through the closed half endpoint,
proved in the
[half-endpoint packet](research_mixed_half_endpoint_conditional_packet.md),
extends concavity to this closed box. Successive one-variable endpoint
comparisons therefore give
\[
 f_{\alpha\beta}(a,x)+f_{\beta\gamma}(x,c)
      >U_{\alpha\beta\gamma}+11/50,\qquad
 a,c\in[.1,.5],\quad x\in I_\beta .
 \tag{14}
\]
This is a real-argument lower bound. It does not replace generally
nonzero hybrid heights by zero.

**Theorem 1.** Uniformly over all actual reference types and values in
(1), all allowed selections, all inner nonseam coordinates and halos
in \([.1,.5]\),
and all \(\lambda\in[0,1]\), the local repaired-halo upper proxy
with both adjacent real coordinates equal to \(1/10\) is below
\(-11/50\), before the separately chosen source tolerance.

The conclusion follows from (6), (8), (10), and (13). It is independent
of word length: the original reference is used only through its fixed
rectangles and middle critical equation. Repeated reference positions
cause no problem in this local statement. It does not replace the
separate joint-edge accounting required for a physical two-symbol run.

## 4. A qualitative neighborhood, with the source domain unchanged

There is \(\eta>0\), independent of the word and \(N\), such that
the same distinct-edge repaired proxy is below \(-1/5\) whenever
both adjacent endpoint reals belong to \([.1,.1+\eta]\).
This width is not computed.

To see this, take the closed set of typed reference five-tuples in
the established compact rectangles satisfying the three relevant
original critical equations. It is compact and contains every actual
reference window. The remaining inner coordinates and halos vary in
\([.1,.5]\); selection choices are finite and \(\lambda\in[0,1]\).
All physical and repaired heights are continuous functions of these
data and stay in the already-proved nonlow source polygons. The
original critical phases are holomorphic on neighborhoods of those
compact products. Their true selected corrections are maxima of two
continuous branches; the source height profiles and all occupations
are continuous as well. Therefore the exact repaired proxy is uniformly
continuous on this compact set. Its uniform gap at both endpoints .1
from Theorem1 persists in a fixed one-sided square, with reserve
\(1/5\).

This argument perturbs a phase comparison inside existing complete
finite-source domains. It does not infer a finite-sum error estimate
by analytic continuation. The original conditional packets, raw seam
rows and Fourier factors remain those of the cited theorems. A smaller
strict gap may absorb their prescribed finite tolerance. No explicit
width or full interval \([.1,.22]\) is asserted by this continuity
argument. The direct pair bound gives the separate assembly below.

## 5. Direct pair replacement and independent low-neighbor seams

Fix \(0<\rho\le1/1000\), use that value in the original periodic
hybrid contour, and keep the word fixed for the finite-source estimate.
Let \(S\ne\varnothing\) be an independent set of cyclic positions,
meaning that no original edge has both endpoints in \(S\). Suppose
\[
 x_s\in[0,\rho]\ (s\in S),\qquad
 x_j\in[\rho,.5]\ (j\notin S),\qquad
 x_{s-1},x_{s+1}\in[.1,.1+\eta]\ (s\in S).
 \tag{15}
\]
The width \(\eta>0\) is sufficiently small as specified below.
All permitted selections are retained initially.

Simultaneously replace \(x_s\) by \(\Re r_s\) and remove its selection
for every \(s\in S\). Denote the resulting hybrid targets by \(z^\#\).
This is a comparison of phases and source upper bounds, not a
substitution in the original integral. The new real vector belongs to
\([\rho,.5]^m\), and every unchanged row keeps its original selection.

At the exact endpoints \(x_{s-1}=x_{s+1}=.1\), both physical and
repaired neighboring heights vanish. The repaired middle target is
\(\Re r_s\), with height zero: its own cutoff is one, but the two
neighbor cutoffs are zero. Its two coherent block rates are exactly
the two terms in (13) with \(a=c=.1\). The complete raw physical
seam-pair rate is at most \(U_{\alpha\beta\gamma}\). Thus (13) is
already a direct pair replacement gain \(11/50\); no background
convexity or boundary-potential estimate is needed for this deduction.

For positive \(\eta\le.02\), the repaired seam height and the two
physical or repaired neighboring heights satisfy
\[
 |\Im z_s^\#|\le\frac{19}{40}\eta,\qquad
 |\Im z_j|,\ |\Im z_j^\#|\le\frac7{10}\eta,\qquad
 |\Im(z_j^\#-z_j)|\le\frac7{10}\eta\quad(j=s\pm1).
 \tag{16}
\]
Indeed the slow cutoff at such a neighbor is at most \(\eta/.12\),
and the selected fast cutoff is at most \(\eta/.02\).
The largest resulting row slope is
\(\max\{.03/.12,.057/.12,.014/.02\}=.7\).
Replacing seam cutoff values by one can only increase the minimum,
so the last bound uses .7 rather than twice .7. This remains true when
one row neighbors two seam positions.

For an allocated coherent block write
\[
 e_j(u,v)=\Re\phi_j(u,v)
       +\frac{\sigma_{j-1}}2\chi(u)+\frac{\sigma_j}2\chi(v),
 \qquad \chi(z)=\max\{\Re g(z),-2\pi\Im z\}.
 \tag{17}
\]
The physical seam coordinate has height zero, so removal of its
selection changes no raw source modulus. The moving endpoint
halfweights stay in the height profiles in (11)--(12); the middle
full Fourier weight is retained by the \(\beta\nu_\rho\) collar term.
At the exact real endpoints all corrections in (17) vanish.
Continuity of these two true Fourier branches, the source profiles,
and the complete coherent phases now permits a common \(\eta\) such
that each physical raw seam pair is bounded in rate by its repaired
pair minus \(1/5\). This comparison is uniform over all references
in (1), all inner cutoff values, all seam attenuations and selections.
The input products are the established early cap and plateau products;
the strict endpoint reserve is not an analytic continuation of a
finite-sum error estimate.

Only rows adjacent to \(S\) can change outside \(S\). On an original
edge not incident to \(S\), only these row heights change; its real
arguments and selections stay fixed. The compact source products in
the [deep-half theorem](research_mixed_deep_low_half_region.md) give
a finite uniform Lipschitz constant \(L_\rho\) for (17) per endpoint
height. To justify use along the interpolation, if the other endpoint
has real coordinate at least .1, both targets stay in the already
proved convex early-cap, plateau, and interface products. If that
endpoint is below .1, its cutoff is zero before and after repair,
so the neighboring row does not change at all. Consequently no
unproved complex source product with a deep-low endpoint is used.

There are at most \(2|S|\) changed endpoint incidences on nonseam
edges. Count a shared edge once with both endpoint changes if needed.
By (16), the total discrepancy is at most
\[
                    \frac75 L_\rho\eta\,|S|.
 \tag{18}
\]
Shrink \(\eta\) further until the coefficient in (18) is strictly
below \(1/20\). The seam pairs have disjoint original edges because
\(S\) is independent. A shared neighboring coordinate contributes
one halfweight to each pair, never a duplicated full weight. Summing
the raw pair bounds and all remaining coherent edges gives a rate
strictly below
\[
 \sum_j e_j(z_{j-1}^\#,z_j^\#)-\frac3{20}|S|
                         \le M-\frac3{20}|S|,
 \tag{19}
\]
where the last inequality is the completed deep-half phase theorem.

**Theorem 2.** For every fixed word and fixed \(\rho\), a positive
width \(\eta\) can be chosen such that the original selected integrals
over every region (15), summed over all allowed selections and all
nonempty independent \(S\), have absolute value bounded by
\[
                    C N^A \exp\{N(M-1/10)\}
 \tag{20}
\]
for all sufficiently large levels of either parity. Pointwise, the
rate bound can retain \(|S|/10\).

Choose the total finite-source tolerance below \(|S|/20\) in (19).
The complete seam-row estimates are uniform through zero; all other
blocks use the original complete conditional packets. Multiply the
allocated moduli to restore every original Fourier factor once.
The unchanged hybrid Jacobian is bounded for fixed \(\rho\), and
the original normalization and carriers introduce only their already
accounted polynomial factors. The finite sums over regions and
selections prove (20). Neither a ratio of kernels nor a change of
integration variables is used.

For \(m=1\) there is no nonempty independent \(S\), since the diagonal
edge has both endpoints at that position. For \(m=2\) the two
parallel original edges form the single seam pair and no remaining
edge is charged. For \(m=3\) the one remaining edge may have both
endpoints changed and is bounded once by the sum of its two
incidences. These are the same incidence rules used in (18), with
no word-length enumeration.

The width is qualitative and may depend on the fixed collar.
The theorem does not cover adjacent seams, arbitrary neighboring
angles, or a coordinate in the right half of the period. It proves
a restricted-region suppression, not a full cyclic asymptotic or a
new knot-family theorem.

## 6. Mixing the two proved endpoint neighborhoods

The [half-angle connector theorem](research_mixed_half_angle_connector_lower.md),
Corollary 2 and Theorem 3, proves the corresponding independent-seam
comparison when both adjacent angles lie in \([.5-\eta,.5]\).
Its complete finite pair reserve is \(1/40\).

Each neighbor of an independent seam set may independently belong to
\[
          I_{\rm low}=[.1,.1+\eta]\quad\hbox{or}\quad
          I_{\rm half}=[.5-\eta,.5].
 \tag{21}
\]
Take the common width below .02 and below the necessary continuity
widths. At the three corner pairs
\((.1,.1),(.1,.5),(.5,.1)\), at least one low neighbor resets the
repaired seam target to the real number \(\Re r_s\).
The direct real bound (14) therefore supplies the same \(11/50\)
pair reserve at every such corner, with the original height-zero
source ceiling. Compact continuity retains the low comparison in
neighborhoods of all three corner pairs, including its true selected
halfweights. At the remaining corner \((.5,.5)\), the repaired seam
target is \(r_s\), and the half-angle theorem supplies its \(1/40\)
finite reserve. The types and these four corners form a finite set,
so one common width suffices.

Perform the same simultaneous replacement for all seams. If at least
one neighbor is low, the replaced seam height is bounded by
\(.475\eta\); if both neighbors are in the half neighborhood, the
replaced seam target equals the actual \(r_s\), since both neighbor
cutoffs are one. At a half-neighborhood vertex its height change is at
most \(22.8\eta^2\le.7\eta\). Thus every changed nonseam row
satisfies the same bound used in (18). An AA edge can connect a
low-class and a half-class neighbor: both target coordinates and
their height interpolation lie in the completed
[left/right interface product](research_mixed_left_right_interface_source.md).
No new complex source region is needed.

Choose the common width still smaller so that the AA discrepancy
is at most \(|S|/200\). Use the low comparison with finite
tolerances small enough to retain \(1/40\), and the already-proved
half comparison with its full \(1/40\) finite reserve. Assign the
remaining nonseam-edge tolerances a total below \(1/200\).
The repaired deep-half phase bound gives
\[
 M-\frac{|S|}{40}+\frac{|S|}{200}+\frac1{200}
                              \le M-\frac{|S|}{100}.
 \tag{22}
\]
The exact halfweight and short-cycle accounting is unchanged.
Consequently the union of all these independently chosen endpoint
neighborhood regions, with all
original selections, has a bound \(CN^A e^{N(M-1/100)}\).
The same nonseam vertex may neighbor two seams; its single interval
membership determines its physical value in both pairs without
forcing the other endpoints of those pairs into the same interval.
This does not include adjacent seams, general intervening angles,
or right-half coordinates.

The canonical certificate evaluates all 64 corners using 24 original-log
root disks. The higher-precision command below reuses those exact rational
centers and checks every self-map and phase bound afresh; it proposes
no new roots. The assembly and qualitative widths are the written
compactness and incidence proofs, not additional numerical covers.

Reproduction:

```sh
python3 experiments/check_mixed_low_endpoint_connector_lower.py --precision 256
python3 experiments/check_mixed_low_endpoint_connector_lower.py --precision 320 \
  --input repro/results/research-mixed-low-endpoint-connector-lower.json \
  --output /tmp/research-mixed-low-endpoint-connector-lower-review.json
```
