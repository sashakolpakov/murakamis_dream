# A uniform connector bound near the half-angle endpoints

Research proof, 5 November 2026. This compares the original source at a
zero seam with two coherent blocks whose middle coordinate is its geometric
reference. It gives a uniform reserve when the two neighboring angles are
\(1/2\), then a fixed one-sided neighborhood of those angles. Simultaneous
replacement of isolated seams gives a bound for the corresponding whole
integration region. The remaining seam configurations and the right half
of the period are not covered by this result.

## 1. The comparison at angle one half

Use the original cyclic three/four word and its actual geometric reference.
Let \((a,b,c)\) be three consecutive reference coordinates, with type
indicators \((\alpha,\beta,\gamma)\in\{0,1\}^3\). The allocated
critical phases \(\phi_{\eta\epsilon}\) retain their original
logarithmic lifts and additive constants. Set
\[
 F=\phi_{\alpha\beta}(a,b)+\phi_{\beta\gamma}(b,c),\quad
 P_L=F_a,\quad P_R=F_c,\quad
 G=F+P_L(1/2-a)+P_R(1/2-c).
 \tag{1}
\]
The actual middle equation is \(F_b=0\). Thus \(G\) is the sum of
the two tangent planes at outer targets \(1/2,1/2\), whatever real
value is placed at the middle seam.

The [half-angle source theorem](research_mixed_half_angle_seam_source.md)
proves the complete row ceilings
\[
 \begin{split}
 c_0&=-2J(1/4)<q_0:=291561/10^6,\\
 c_1&=J(1/2+u_1)-2J(u_1)<q_1:=443534/10^6,\\
 u_1&=\frac1\pi\arcsin\sqrt{\frac{\sqrt{17}-1}{8}},
 \qquad J(t)=\int_0^t\log(2\sin\pi u)\,du.
 \end{split}
 \tag{2}
\]
These constants include every row and both level parities. The actual
Fourier halfweight at the half-angle has zero upper exponential rate;
it is not removed from the finite expression.

Define
\[
 D(a,b,c)=\Re G-q_\beta-q_\gamma-\frac1{50}
       -\frac{11}{2}(1/2-\Re a)^2
       -\frac{151}{20}(1/2-\Re c)^2.
 \tag{3}
\]
The common allowance \(1/50\) covers the full real-collar cost
\(2\Delta_\rho+\beta\nu_\rho\) for every fixed
\(0<\rho\le1/1000\), where
\(\nu_\rho=-J(\rho)\) and
\(\Delta_\rho=\rho\log2-J(\rho)\).

**Theorem 1.** At every actual consecutive reference triple of every
fixed cyclic three/four word,
\[
                              D(a,b,c)>1/20.
 \tag{4}
\]
Consequently
\[
 \Re\{\phi_{\alpha\beta}(1/2,b)+\phi_{\beta\gamma}(b,1/2)\}
                       >q_\beta+q_\gamma+1/50+1/20.
 \tag{5}
\]
The statement is uniform in word length and in the actual geometric
reference. Repeated coordinates in short periods retain their incidences.

We first explain why (4) gives (5). Write a block Hessian as
\(\phi''=-A+iB\). The
[oriented reset theorem](research_mixed_oriented_height_reset.md)
proves the pointwise quadratic bounds
\[
 \Re(w^T\phi''w)\le11(\Im w_0)^2\quad(\Im w_1=0),
 \qquad
 \Re(w^T\phi''w)\le\frac{151}{10}(\Im w_1)^2
                                      \quad(\Im w_0=0).
 \tag{6}
\]
Apply these at the original parameter point to \(iw\), rather than
rotating a parameter domain. After integrating on the original straight
reference-to-target segment, they give
\[
 \Re\{\phi(z)-\Gamma_r(z)\}\ge
 \begin{cases}
 -\frac{11}{2}(\Re(z_0-r_0))^2,&\Re(z_1-r_1)=0,\\
 -\frac{151}{20}(\Re(z_1-r_1))^2,&\Re(z_0-r_0)=0.
 \end{cases}
 \tag{7}
\]
Both imaginary components may change within the admitted unselected
products. For the two targets \((1/2,b)\) and \((b,1/2)\), these
segments lie in those products at actual references. Their tangent planes
sum to (1), and (7) proves (5). Selected factors at a real half-angle
have zero rate, so the same comparison covers all allowed physical
selections there. These are lower bounds for coherent phases, not lower
bounds for the moduli of finite quantum kernels.

## 2. Proof of the uniform geometric reserve

Use the original five-vertex open window from
[the complete seam-pair theorem](research_mixed_hybrid_zero_pair_support.md).
Its three middle reference legs are \((a,b,c)\). The established window
theorem gives their holomorphic dependence on the two external reference
parameters on neighborhoods of the full typed rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{8}
\]
The identity \(F_b=0\) holds throughout that window branch. Every actual
cyclic reference is included, after repeating a short period if needed.

The negative of (3) is separately subharmonic in the two external
parameters: the real part of its holomorphic term is harmonic, and the
two positive squares of real parts of holomorphic functions are
subharmonic. Successive maximum principles reduce (4) to all products
of external rectangle sides. This argument uses the prior whole-product
branch; it does not infer branch existence from boundary samples.
The auxiliary internal legs along that boundary need not satisfy the
narrow actual-reference rectangles used for (7). We test (3) there as
a holomorphic-window expression; (7) is needed only at actual references.

The exact differential to be enclosed on a boundary cell is
\[
 \begin{split}
 dD={}&\Re\{(1/2-a)\,dP_L+(1/2-c)\,dP_R\}\\
 &+11(1/2-\Re a)\Re da
       +\frac{151}{10}(1/2-\Re c)\Re dc.
 \end{split}
 \tag{9}
\]
Indeed \(dF=P_L\,da+P_R\,dc\), since \(F_b=0\), so the
first derivatives of the reference legs cancel in \(dG\).

The companion certificate tests all 32 ordered five-vertex words, four
external type pairs and sixteen external-side products: 2,048 complete
boundary domains. The 18,988 cells of the previous seam-pair cover are
used as starting cells only. The new calculation recomputes original
root enclosures, midpoint values of (3), and the full-cell derivative
(9). A cell is accepted only when its outward lower bound exceeds
\(1/20\); any needed refinement retains an exact binary cover. The
window response uses the original logarithmic residual, the established
Neumann corrections and their outward tail bound. Each case and its
entire parameter square must be present exactly once.

Thus neither the old seam margin nor the positive corner pilot is a
premise of (4). The complete new cover and the preceding maximum
principles prove (4), and (7) completes the proof of Theorem 1.

## 3. A uniform one-sided neighborhood

For fixed selections write the original complete coherent edge rate as
\[
 e_{\eta\epsilon}^{\sigma_0,\sigma_1}(z_0,z_1)
 =\Re\phi_{\eta\epsilon}(z_0,z_1)
       +\frac{\sigma_0}{2}\chi(z_0)+\frac{\sigma_1}{2}\chi(z_1),
 \quad\chi(z)=\max\{\Re g(z),-2\pi\Im z\}.
 \tag{10}
\]
Both true Fourier alternatives are retained. At a half-angle,
\(\chi(1/2)=0\).

Consider physical neighbors
\(z_L=x_L+ih_L\), \(z_R=x_R+ih_R\), and comparison neighbors
\(\widetilde z_L=x_L+i\widetilde h_L\),
\(\widetilde z_R=x_R+i\widetilde h_R\). Keep the selections
the same, and require all four heights to lie in their physical typed
bands, with
\[
 .5-\eta\le x_L,x_R\le.5,\qquad
 |h_j|,|\widetilde h_j|\le\frac{57}{1000}\,400(.5-x_j)^2.
 \tag{11}
\]
Every original hybrid height and every reference-halo repair has these
bounds, independently of the seam attenuation and other neighboring
coordinates. Let \(\mathcal B\) denote the original allocated kernel
modulus, including its two actual Fourier halfweights.

**Corollary 2.** There is a fixed \(\eta>0\), which may be chosen
smaller than \(1/20\), such that for every fixed collar
\(0<\rho\le1/1000\), every real seam coordinate \(x\in[0,\rho]\),
and all targets in (11),
\[
 \begin{split}
 &\mathcal B_{\alpha\beta,N}^{\sigma_L,\sigma_s}(z_L,x)
       \mathcal B_{\beta\gamma,N}^{\sigma_s,\sigma_R}(x,z_R)\\
 &\quad\le C N^A\exp N\left\{
 e_{\alpha\beta}^{\sigma_L,0}(\widetilde z_L,b)
 +e_{\beta\gamma}^{0,\sigma_R}(b,\widetilde z_R)-\frac1{40}
                                  \right\}.
 \end{split}
 \tag{12}
\]
The left side may instead use both absolute row sums. The constants may
depend on the fixed collar; \(\eta\) is independent of word length,
all original selections and attenuation parameters. Both parities are
included. No numerical value for \(\eta\) is asserted.

**Proof.** The half-angle source theorem proves uniform continuity of
the full row exponent near \(1/2\), including zeros, top rows and the
actual Fourier forcing. Choose a neighborhood in which the two source
rates, including their finite comparison tolerances, total at most
\(q_\beta+q_\gamma+1/100\). The real collar adds less than
\(1/50\). This retains the original complex-first-argument chirp and
both middle halfweights.

The coherent phases in (10) are uniformly continuous on the relevant
compact source products. Their original branches and complete packets
are established in the
[independent right products](research_mixed_unselected_right_taper_products.md)
and [half-endpoint theorem](research_mixed_half_endpoint_conditional_packet.md).
There are finitely many types and selections, and the actual references
range in compact subsets. Decrease \(\eta\) so that the comparison
rate on the right of (12) differs from the left side of (5) by less than
\(1/100\). Equations (4)--(5) then leave a reserve greater than
\(1/20-1/100-1/100=3/100>1/40\). This proves (12).
The neighborhood is one-sided within the auxiliary half-period.
No extension of its boundary potentials above \(1/2\) is used.
\(\square\)

## 4. Replacing all isolated seams at once

This local comparison can be assembled without optimizing a boundary
potential. Fix an original cyclic word of length \(m\), a selection,
and its hybrid contour. Let \(S\) be a nonempty set of seam positions,
with no two positions adjacent in the physical cycle. Suppose
\[
 x_s\in[0,\rho]\ (s\in S),\qquad
 x_j\in[\rho,.5]\ (j\notin S),\qquad
 x_j\in[.5-\eta,.5]\ \text{if }j\text{ is adjacent to }S.
 \tag{13}
\]
The same nonseam position can neighbor two seams. Distinct physical
edges are always counted separately, including the two-cycle edges.
A one-cycle has no nonempty independent seam set.

Replace every \(x_s\), \(s\in S\), by \(\Re r_s\) and its
selection by zero. Keep every other real coordinate and selection.
Evaluate the original hybrid height rule at this new configuration,
and denote its targets by \(z_j^\#\). Each replaced seam now has
target exactly \(r_s\): its own cutoff and the cutoffs of both
neighbors are one, and its own right factor is one. Only neighboring
nonseam heights can change. They satisfy
\[
                |\Im(z_j-z_j^\#)|
                     \le\frac{57}{1000}\,400\eta^2.
 \tag{14}
\]
This uses the same selection and height multiplier before and after
replacement, so no factor two is needed in (14).

Let \(E_A\) be the edges with neither endpoint in \(S\). On the
compact nonlow source products, let \(L\) bound each vertical
derivative of every branch of the complete rate (10). Such a finite
constant, uniform over types, selections and reference boxes, is
provided by the original holomorphic branches and compactness; its
numerical value is not needed here. The maximum of the two Fourier
branches is Lipschitz with the same bound. A nonzero change on an edge
in \(E_A\) forces its other endpoint above .1; otherwise that endpoint
resets both physical and repaired heights to zero. Thus this fixed
nonlow derivative bound covers every changed edge.

Each changed nonseam position is incident to at most one edge in
\(E_A\). If both its neighbors are seams it is incident to none.
There are at most \(2|S|\) changed positions. Therefore
\[
 \sum_{j\in E_A}\{e_j(z_{j-1},z_j)-e_j(z_{j-1}^\#,z_j^\#)\}
            \le2|S|L\frac{57}{1000}\,400\eta^2.
 \tag{15}
\]
When one edge has two changed endpoints, use two vertical segments
in its same product domain. This proves (15) for two-symbol runs with
one joint change; the edge itself is not counted twice.

Decrease \(\eta\) once more so that the right side of (15) is at
most \(|S|/200\). The two seam-incident edges at each \(s\) obey
(12) with comparison targets \(z^\#\). Their pairs are disjoint
as physical edges, because \(S\) has no adjacent positions. Hence
each original Fourier halfweight is allocated exactly once, even when
two pairs share a nonseam position.

The repaired configuration lies entirely in \([\rho,.5]^m\).
The [deep-low half-region theorem](research_mixed_deep_low_half_region.md)
therefore gives its pointwise coherent bound
\[
                \sum_j e_j(z_{j-1}^\#,z_j^\#)\le M,
                 \qquad M=\Re\sum_j\phi_j(r_{j-1},r_j).
 \tag{16}
\]
For each edge in \(E_A\), use its established complete finite upper
bound with tolerance below \(1/(200m)\). Combining (12), (15) and
(16) bounds the original product by a polynomial factor times
\[
 \exp N\{M-|S|/40+|S|/200+1/200\}
                       \le\exp N\{M-|S|/100\}.
 \tag{17}
\]
No inequality between the finite kernels before and after replacement
is asserted. The comparison uses the proved physical finite-source upper
bounds and the original coherent phases only.

**Theorem 3.** For some fixed \(\eta>0\), the sum of the original
selected integrals over the union of all nonempty regions (13) obeys
\[
                     |\mathcal Z_N|\le C N^A e^{N(M-1/100)}.
 \tag{18}
\]
For every fixed word and collar, this holds at all sufficiently large
integer levels, with both parities retained. Sum the finitely many
seam sets and selections, and use the bounded hybrid Jacobian to pass
from (17) to (18). Common closed-piece boundaries have measure zero
and do not affect the integral.

This region theorem allows arbitrarily many isolated seams and arbitrary
remaining half-period coordinates. It requires all their adjacent angles
to lie in the fixed neighborhood specified in (13). Adjacent seams,
other seam-neighbor angles and the remaining right-half configurations
still require separate estimates. The volume conjecture and stability
under arbitrary short partial fillings do not follow from this result.

## Reproduction

The certificate checks the new geometric inequality (3)--(4) throughout
its full reference boundary. The subharmonic extension, phase lower
bounds, continuity argument and arbitrary-length incidence proof are
the written arguments above.

```sh
python3 experiments/certify_mixed_half_angle_connector_lower.py --precision 256
python3 experiments/certify_mixed_half_angle_connector_lower.py \
  --precision 320 \
  --input repro/results/research-mixed-half-angle-connector-lower.json \
  --output /tmp/research-mixed-half-angle-connector-lower-review.json
```
