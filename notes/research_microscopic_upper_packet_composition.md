# Upper packets survive a common filling with microscopic insertions

Private written proof, 16 November 2026.

There is an upper-bound class of actual received sources that is
preserved by a sufficiently high-curvature common-circle filling,
even after inserting a fixed product of microscopic endpoint kernels
at that circle. The received sources retain their nontrivial
exponential phases. A fixed sharp repair saving pays the explicit
small loss between their complete action and the selected common
filling action.

Only upper bounds are propagated. The output remains eligible for
another such join without a nonzero leading coefficient hypothesis.
This does not cover arbitrary low-valence short components.

## 1. The incoming upper class

An incoming packet is an actual ordinary spectral polynomial
\(F_{j,N}(t,\mathbf u;\boldsymbol\alpha)\), separately even and
periodic in its boundary angles. It retains the original first
normals wherever a boundary variable is subsequently traced.
Its degree in each spectral variable is at most \(c_jN\), with
\(c_j\) fixed. The parameters \(\boldsymbol\alpha\) are any previously
introduced microscopic parameters in a fixed bounded complex set.

The packet has a specified separately even holomorphic phase
\(W_j(t,\mathbf u)\), independent of those microscopic parameters.
On a fixed complex neighborhood of zero require the actual envelope
\[
 |F_{j,N}(t,\mathbf u;\boldsymbol\alpha)|
             \le C N^p e^{N\Re W_j(t,\mathbf u)}.
 \tag{1}
\]
Require also the whole-boundary envelope on a fixed thin strip
\[
 |F_{j,N}(x+iy,\mathbf a+i\mathbf b;\boldsymbol\alpha)|
 \le CN^p\exp N\!\left\{
 M_j-c(1-\cos x)-c\sum_\ell(1-\cos a_\ell)
                  +C_1y^2+C_1\sum_\ell b_\ell^2\right\},
 \quad M_j=\Re W_j(0,\mathbf0).
 \tag{2}
\]
Constants are uniform on larger parameter compacts when derivatives
are requested. A zero-free amplitude or an asymptotic expansion is
not part of this definition.

Use a fixed finite collection of such packets, with common constants
and charts. Their phase data satisfy the explicit common-circle
hypotheses: writing
\[
 W_{j,tt}(0,\mathbf0)=-a_j+ib_j,\qquad a_j>0,\quad b_j\in\mathbb R,
 \tag{3}
\]
the external real Hessians are strictly negative. On smaller common
charts the phase-only bounds (10) of the common-circle source apply:
\[
 \widetilde W_j=W_j-\tfrac i2b_jt^2,\qquad
 Q_j=-\widetilde W_{j,t}/(a_jt),\qquad
 |Q_j-1|\le1/100,\quad |\partial_tQ_j|\le L_0,
 \tag{4}
\]
\[
 \Re(-W_{j,tt})\ge a_j/2,\quad
 \Re(-W_{j,\mathbf u\mathbf u})\ge\beta I,\quad
 \|W_{j,t\mathbf u}\|\le B_1|t|.
 \tag{5}
\]
The quotient in (4) is removable. Conditions involving external
variables are omitted when none occur. These are conditions on
explicit phases and actual upper estimates, not a claim that a
classical Hessian by itself supplies (1) or (2).

Verified initial members are the original bare terminal packets
with fixed signed powers of magnitude at least two, any fixed
eligible zero-subtree packets, and the original bare edge. The
uniform terminal-family theorem supplies common constants over
all terminal powers, if that larger initial family is desired.
Only its upper estimates and phase data are used here.

## 2. The exact join and an explicit additional threshold

Attach \(m\) packets at one original common color \(t\), retaining
their other boundary variables \(\mathbf u^{(\nu)}\) separately.
The packets may themselves be outputs of earlier eligible joins.
Let \(n\) be any fixed signed integer and insert
\[
 B_N(C)=\prod_{\ell=1}^rK_N(2\cosh(\xi_\ell/N),C),
       \qquad |\xi_\ell|\le A,
 \tag{6}
\]
with \(r,A\) fixed. The actual output is
\[
 \mathcal P_N(\mathbf U)=
 \phi_N^{(t)}\!\left[
 R_N^n B_N(-2\cos t)
                 \prod_{\nu=1}^{m}F_{j_\nu,N}
                         (t,\mathbf u^{(\nu)})\right].
 \tag{7}
\]
The common variable is multiplied before the original full trace.
All carriers, shared-color product normals and any repeated
microscopic parameters remain in this expression.
Explicitly, with \(C=-2\cos t\), \(c_j=2\cos((2j+1)\pi/N)\),
and \(\eta=(-1)^{N-1}\), that trace is
\[
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
       \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
                    +\mathbf1_{N\ {\rm odd}}f(-2).
\]
The crossing representative is
\[
 e^{\pi i n(N-1)^2/(4N)}e^{inNt^2/(4\pi)}.
\]
Its value and first spectral normal are the original ones.

Here are constants giving a sufficient threshold. Use the notation
and explicit phase-chart choices of the common-circle source:
\[
 a_{\min}=\min a_j,\quad b_{\max}=\max|b_j|,\quad
 d_{\min}=2\pi a_{\min},\quad k_0=2c/\pi^2,
\]
\[
 L_*=\frac7{2d_{\min}},\qquad
 K_*=\frac{49}{d_{\min}^2}
       \left(C_1+\frac{b_{\max}^2}{2k_0}\right)
                              +\frac{49}{32\pi^2k_0}.
 \tag{8}
\]
Choose its fixed central angular half-width \(a>0\) smaller if
necessary so the uniform fold construction applies on a larger
cap, with cutoff \(1/4\). Fix
\[
 0<\gamma<
 \inf_{|t|\le a_{\rm out}}
 I_{1/4}\!\left(\frac{\pi-t}{2\pi}\right),
 \qquad a_{\rm out}>a .
 \tag{9}
\]
The right side is positive for sufficiently small fixed
\(a_{\rm out}\), since its value at zero is \(2G/\pi\).
The required slightly larger spatial and parameter buffers are
fixed before \(N\) varies.

Let \(m_0\) be the explicit sufficient common-circle threshold
from section 3 of the pinned common-circle source, after this
chart reduction. This includes its outer-angle, Schur, and
whole-boundary inequalities. Only its phase and upper-envelope
inequalities are used; its separate nonzero-amplitude condition
is unnecessary here. Enlarge it to
\[
 \boxed{\qquad
 m\ge m_1:=\max\left\{
 m_0,\ \left\lceil\frac{4(K_*+L_*)}{\gamma}\right\rceil+1
                       \right\}.
 \qquad} \tag{10}
\]
The additional inequality is numerical and involves only previously
given phase and envelope constants. It contains no unknown output
source bound. The threshold does not depend on the fixed central
integer, the level, or the number of microscopic factors in (6).
Polynomial constants and starting levels may depend on all those
fixed data and on their bounded parameter sets.

Put
\[
 W(t,\mathbf U)=\sum_\nu W_{j_\nu}(t,\mathbf u^{(\nu)}),\qquad
 \Phi(t,\mathbf U)=W(t,\mathbf U)+\frac{in}{4\pi}t^2-it .
 \tag{11}
\]
The phase-only common-circle construction gives a unique selected
critical point \(t_*(\mathbf U)\) in the small disk, below the real
axis, and the holomorphic action
\[
 \mathcal S(\mathbf U)=\Phi(t_*(\mathbf U),\mathbf U),\qquad
                         M=\Re\mathcal S(\mathbf0).
 \tag{12}
\]
All original phase constants in the \(W_j\) and the original
integer \(n\) are retained.

**Theorem.** The actual output (7) obeys on a fixed smaller
complex boundary neighborhood
\[
                  |\mathcal P_N(\mathbf U)|
                         \le CN^p e^{N\Re\mathcal S(\mathbf U)}.
 \tag{13}
\]
If there are outside variables, it also obeys a whole-boundary
bound of the same class:
\[
 |\mathcal P_N(\mathbf X+i\mathbf Y)|
 \le CN^p\exp N\!\left\{
 M-c_*\sum_\ell(1-\cos X_\ell)
                         +C_*\sum_\ell Y_\ell^2\right\}
 \tag{14}
\]
on a sufficiently thin fixed strip, with \(c_*>0\).
The output phase has the same separately even holomorphic
structure and strictly negative external real Hessian required
in (3)--(5), after shrinking its chart.
Its spectral degrees remain \(O(N)\). Thus a finite collection
of such outputs is again an eligible incoming upper family.

All bounds are uniform on bounded complex microscopic parameter
sets and retain fixed parameter and physical normal derivatives
with polynomial losses. No nonzero output assertion is made.

## 3. Phase facts used in the proof

These facts use only (3)--(5), not an incoming asymptotic amplitude.
Set
\[
 A=\sum_\nu a_{j_\nu},\quad B=\sum_\nu b_{j_\nu},\quad
 D=2\pi A,\quad \widetilde n=n+2\pi B,\quad
                        R=(D^2+\widetilde n^2)^{1/2}.
 \tag{15}
\]
The exact phase identity
\[
 \Phi=\sum_\nu\widetilde W_{j_\nu}
                           +\frac{i\widetilde n}{4\pi}t^2-it
 \tag{16}
\]
is used for estimates; it does not change the crossing in (7).
For unit charge the contraction in the pinned proof gives
\[
 |t_*|\le7/R,\qquad
 0<-\Im t_*\le7D/R^2,\qquad
 \Re W(0,\mathbf U)-\Re\mathcal S(\mathbf U)
                                  \le L_*/m.
 \tag{17}
\]
These inequalities hold throughout the chosen smaller complex
boundary chart. One can see the last constant directly by
integrating the charge-\(\lambda\) estimate
\(-\Im t_\lambda\le7\lambda D/R^2\) from zero to one.

The real second derivative of \(\Phi\) on the central chart is
at most \(-A/2\). The horizontal line through \(t_*\) therefore
has a unique maximum \(\Re\mathcal S\). Its endpoints at the
fixed cuts have a strict gap. At each vertical side, the real
phase is convex in height; its real endpoint has a strict gap
by (17), the real curvature and the threshold \(m_0\).
The top endpoint has the horizontal gap. This controls the
entire vertical side.

For arbitrary real outside angles the global incoming envelopes,
on the center contours of height \(h_*=-\Im t_*(0)\), give the
completed-square budget
\[
 M_{\rm base}-cT
    +mC_1h_*^2+\frac{n^2h_*^2}{16\pi^2mk_0}
 \le M_{\rm base}-cT+\frac{K_*}{m},
 \quad
 T=\sum_\ell(1-\cos U_\ell),\quad
 M_{\rm base}=\sum_\nu M_{j_\nu}.
 \tag{18}
\]
This is the original-\(n\) calculation: use
\(n^2\le2\widetilde n^2+8\pi^2m^2b_{\max}^2\) and (17).
It bounds every central exterior side, with the full rational
sampling kernel, not only the local saddle segment.
For small imaginary outside angles the same calculation adds
\(C_1\sum_\ell(\Im U_\ell)^2\).

Finally the external Schur correction has norm at most
\[
 \frac{98B_1^2}{a_{\min}D^2}.
 \tag{19}
\]
The threshold \(m_0\) makes this smaller than half the incoming
strict Hessian margin. Separate evenness eliminates the mixed
external entries at zero. Thus the claimed phase and Hessian
properties of \(\mathcal S\) follow from the phase calculation
already used for the bare composition.

## 4. Exact microscopic insertion and every central current

The full endpoint-product theorem gives polynomial real norm
for (6), uniformly in its bounded complex parameters. Markov
controls its physical first normals. Consequently multiplication
by (6) changes the estimates for the original outer physical
rows only by powers of \(N\). The incoming global bound (2),
its buffered derivatives, and the original trace therefore
retain the outer-window gaps used in \(m_0\).

On the central cap use the fold theorem's actual baseline
\(B_N^0=\prod_\ell V_{\ell,N}\) and exact half-representatives
\(B_N^\pm\). They preserve the original shared physical jets
and satisfy on their designated halves
\[
 |B_N^0|+|B_N^\pm|\le CN^p,\qquad
                  |B_N^\pm-B_N^0|\le CN^p e^{-\gamma N}.
 \tag{20}
\]
For the real interface, in the coordinate
\(t=\pi-2\pi x-\pi/N\), their exact removable difference obeys
\[
 |D_h(x)(B_N^+(x)-B_N^-(x))|
                       \le CN^p e^{-\gamma N},
 \qquad D_h=(\pi/h)^2\csc^2(\pi x/h).
 \tag{21}
\]
The fixed centered weight in the fold theorem gives these
uniform estimates through the odd simple value and even last
normal. No part of the full endpoint kernel is discarded.

Insert (20) into the exact full-mirror trace identity with
spectator \(\prod_\nu F_{j_\nu,N}\). Its prefactor is
\(-\eta/(4\pi^2i)\), where \(\eta=(-1)^{N-1}\).
It contains the two exterior half-contours, all four vertical
half-sides, and the real interface (21). The spectator and
the original Gaussian carrier stay inside every term.
Reflection pairs the two exterior halves; the sine and
the contour differential both change sign, so the usual
common-circle orientation is recovered without deleting a
boundary contribution.

For the local bound (13), the received factors are estimated
by their actual envelopes (1) throughout this contour.
The baseline horizontal integral is bounded by a polynomial
times \(e^{N\Re\mathcal S(\mathbf U)}\), by (17) and the
horizontal concavity. The same holds for its two full vertical
sides by the endpoint convexity comparison. The corrections
in (20) have the additional saving \(\gamma\). The rational
kernel retains every alias; at the fixed nonzero height their
sum has the same leading unit-character bound with polynomial
prefactor, while at a midpoint vertical side its exact modulus
is a constant times \(N^2\operatorname{sech}^2(NH/2)\).

The only new term not carrying that unit-character height loss
is the real interface. Since \(W\) is even in \(t\) and has
the strict real curvature in (5), its real rate is at most
\[
 \Re W(0,\mathbf U)-\gamma
 \le\Re\mathcal S(\mathbf U)+L_*/m-\gamma
 \le\Re\mathcal S(\mathbf U)-3\gamma/4 .
 \tag{22}
\]
Here the last inequality is implied by (10). Fixed derivatives
in any shared outside parameter retain the product rule and
cost only powers of \(N\). All outer physical rows, horizontal
halves, vertical sides, real interface and sampling aliases
have now been estimated. This proves (13).

This proof did not replace a received exponential factor by
a microscopic one or by a scalar complete-output value.
The whole holomorphic received source occurs inside the same
central trace throughout.

## 5. Whole-boundary bounds and iteration

For the far outside-angle bound use the same central contour
at the fixed height \(h_*=-\Im t_*(0)>0\), independently of
those outside angles. Equations (2), (18), and (20) bound
its exterior pieces by
\[
 CN^p\exp N\left\{M_{\rm base}-cT+K_*/m
                           +C_1\sum_\ell(\Im U_\ell)^2\right\}.
 \tag{23}
\]
The real interface is bounded instead by the same expression
with \(K_*/m\) replaced by \(-\gamma\), using (21).
Outer physical rows have their original fixed angular loss.
Thus (23) is a valid upper bound for the whole source.

On the complement of the small outside-angle chart, \(T\)
has a fixed positive lower bound \(s_0\). The original
common-circle threshold includes
\[
                  (K_*+L_*)/m<c s_0/2 .
 \tag{24}
\]
Since \(M\ge M_{\rm base}-L_*/m\), (23) gives a strict
whole-boundary angular loss there. On the smaller chart,
(13), the even phase and (19) give
\[
 \Re\mathcal S(\mathbf X+i\mathbf Y)
                  \le M-c'\sum_\ell X_\ell^2
                                      +C'\sum_\ell Y_\ell^2 .
 \tag{25}
\]
Choose overlapping near and far angular regions and a common
thin imaginary strip. Combining (23)--(25), and reducing the
positive angular constant, proves (14). If no outside variables
remain, this step is empty and (13) is the scalar upper bound.

The actual output is holomorphic and separately even in each
uncontracted spectral boundary angle. Its degree is \(O(N)\):
the trace contracts only the common variable and does not
increase the degrees of the other fixed input polynomials.
The normalized function
\(\mathcal P_N e^{-N\mathcal S}\) is holomorphic and
polynomially bounded on a fixed larger local chart, so Cauchy
gives all its fixed derivatives on smaller charts. The
whole-boundary envelope has the analogous buffered derivative
bounds. Fixed microscopic parameter derivatives follow on
larger bounded complex sets.

This proves exact iterative closure of the upper class.
For a finite tree of eligible joins, start with actual members,
apply (7) at each node, keep each child's complete free-boundary
packet, and compute the phase by (11)--(12). Before the next
join take common constants for its finite list of children
and recheck (10). Induction gives (13)--(14) at every output.
No previous output is required to have a nonzero coefficient.
Eligibility and constants are checked anew at each node;
there is no uniform threshold over arbitrary generated trees.

## 6. Geometry and limitations

For initial phases already calibrated to marked positive
blocks, the phase law (11)--(12), with the original signed
crossing and the retained absolute constants, is the same
classical common-circle gluing law as in the pinned source.
The local Hessian and Schur calculation is inherited, not a
new identification of a global source cycle.

The microscopic ports in (6) sit near the opposite spectral
endpoint. Their polynomial insertion rate does not identify
their saturated-edge constants or outside work with those
of a positive parent geometry. A parent-volume comparison
must still impose the original retained rows and boundary
work. No new volume equality is asserted here.

The theorem supplies an actual post-turn upper estimate on
a family of received exponential sources and preserves the
upper data needed for another eligible composition. It does
not establish the line/complement feedback or scalar closing
conditions of the observation-composition criterion. In
particular it gives no general low-valence closure, no
arbitrary-short-component theorem, and no lower bound.
At a purely imaginary central saddle the nonreal insertion
imbalance can fail; the proof never uses such an imbalance.

The previous common-circle theorem already closes undecorated
packets with nonzero local amplitudes. The new implication is
its upper-only, iterable version with arbitrary fixed
microscopic insertions, whose exact real interface is paid
by the explicit additional inequality (10). The earlier
positive-CROSS tangle composition and weighted-jet observation
criteria concern different contractions and do not prove
this estimate.

## 7. Complete direct sources

* [Common-circle source and explicit phase budgets](research_amplified_finite_block_source.md),
  SHA256 430fc688372dd36c0656dd458f4de3ea6c56b56a1a96bce941461cf2b358a8c2.
* [Uniform initial terminal family and bare edge](research_uniform_terminal_family_and_star_fillings.md),
  SHA256 d9da305e1567393f5f714f11bd646cd2dca37b7d7569b9ab12d6a63014ece4f9.
* [Uniform sharp fold cap and exact full-mirror trace](research_endpoint_uniform_fold_cap.md),
  SHA256 5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
* [Actual microscopic product norms](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.

All four complete source texts were read at these matching pins,
with their used implications checked. Only written mathematics
and source text/hash reads were used. No mathematical program, numerical experiment,
test, build or compilation was run. Adopted and public notes
are unchanged.
