# Explicit interface costs for the nonlow full period

Research deduction, 5 November 2026. This gives an exact boundary reduction
for the original finite source on \([.1,1]^m\). It does not establish
the remaining interface inequalities. In fact, the simple unoptimized
interface test below has a positive bounded diagnostic. All completed
source and contour artifacts remain unchanged.

## 1. The physical allocation and the available right-edge bounds

Fix an original cyclic type word \(\epsilon_j\in\{0,1\}\), its
actual geometric reference \(r_j\), and its original complex tangent
planes \(\Gamma_j\). Edge \(j\) joins vertices \(j-1,j\).
Keep the calibrated phase, symbols and weight \(w_j\) of
[the open-chain boundary theorem](research_mixed_nonlow_open_chain_boundary.md),
equations (1)--(4). In particular
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad J(x)=\Re g(x),\qquad M=\Re\sum_j\phi_j(r_{j-1},r_j).
 \tag{1}
\]
Use the exact [split-cutoff hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
On the present domain its target is
\[
 z_j=x_j+i c_j R(x_j)
       \min_{k=j-1,j,j+1}L_{b_j}(x_k),
 \quad L_b(x)=\min\{1,(x-.1)/(b-.1)\},
 \tag{2}
\]
where \(R=1\) through .45, \(R=400(.5-x)^2\) between .45
and .5, and \(R=0\) on \([.5,1]\). If unselected,
\(b_j=.22,c_j=\Im r_j\); if selected, \(b_j=.12,c_j=.014\).
The cutoff belongs to its row. Selections are allowed only at type four.

Partition the real symbols into \(A=[.1,.5)\) and
\(R_+=[.5,1]\). The disjoint convention at .5 is only for counting;
the uniform bounds below include the closed endpoints. Write
\(q_j=(x_j,\sigma_j)\) and \(p_j=(\Re r_j,0)\).

For an edge with at least one right symbol, define the complete raw rate
\[
\begin{split}
 \mathscr F_j(z,w)=\sup_{0\le u\le1}\bigg\{&
 I_h(u,x)+I_k(u,y)-(2+\epsilon_j)J(u)-2\pi hu\\
 &+\frac{\epsilon_{j-1}}2
   [\max\{-\Re g(z),2\pi h_+\}-2\pi\sigma_{j-1}h]\\
 &+\frac{\epsilon_j}2
   [\max\{-\Re g(w),2\pi k_+\}-2\pi\sigma_jk]\bigg\},\\
 I_h(u,x)&=\int_0^u\log|1-e^{2\pi h-2\pi i(x+t)}|\,dt,
 \quad z=x+ih,\quad w=y+ik,\\
 D_j&=\mathscr F_j(z_{j-1},z_j)-\Re\Gamma_j(z_{j-1},z_j).
 \tag{3}
\end{split}
\]
The first-argument chirp, both true Fourier alternatives, every row
including zero and one, and both selected halfweights remain present.
On a real right argument the Fourier upper rate is zero and its selected
frequency has modulus one. Formula (3) is an absolute-row upper rate;
it does not assert a coherent conditional saddle at a right argument.
The uniform finite-product and forced-Fourier estimates in the cited
right-source proofs give the corresponding finite bound with arbitrarily
small positive rate tolerance.

The current complete source inputs are as follows. Each entry means
the original allocated finite modulus relative to its actual plane;
no phase approximation is assumed at a right argument.

| Other argument beside a real right argument | Full finite defect bound |
|---|---|
| Another real right argument | \(-1/100\), by [the two-right theorem](research_mixed_two_right_source_bound.md) |
| \([.1,.22]\), with its physical cap heights | \(-1/2000\), by [the transition/right theorem](research_mixed_transition_right_support.md) |
| \([.4,.5]\), with full independent typed height bands | \(-1/2000\), by [the upper-transition extraction](research_mixed_upper_transition_right_support.md) |
| Plateau \([.22,.45]\), at its prescribed full height | \(-1/2000\), by [the right-half theorem](research_mixed_right_half_block_bound.md) |
| Plateau \([.22,.45]\), at an arbitrary fraction of that height | \(+1/100\), by [the partial-reset theorem](research_mixed_partially_reset_right_support.md) |

All rows, orientations, permitted selections and both level parities
are included. In particular, \((.45,.5)\)--right edges are covered.
The remaining positive local ceiling can occur only on a partially
attenuated type-four plateau leg below .4: the type-three rectangle is
already fully enclosed by the original `all3` source profiles. Beside a
right coordinate, such attenuation is caused by the plateau leg's other
neighbor below .22; a selected leg is fully raised once that neighbor
is at least .12. These observations classify the source domains but do
not bound the aggregate interface cost derived next.

## 2. Four explicit closing weights for an A-run

Use the improved occupation supplied by
[the extracted-curvature corollary](research_mixed_extracted_plateau_curvature.md),
equations (7)--(8):
\[
 \omega_j=\frac1{4000}\min\{1,\sigma_j+
       400(\max\{.22,\min\{x_j,.45\}\}-\Re r_j)^2\}
       +\frac{(x_j-.45)_+}{10}.
 \tag{4}
\]
Only A symbols will receive (4) in this note; a baseline symbol has
zero occupation.

Let \(I=[l,r]\) be a maximal nonempty A-run in a mixed cycle.
Extend its symbols to the integer line by
\(\widetilde q_j=q_j\) on \(I\) and
\(\widetilde q_j=p_j\) outside \(I\). Set
\[
\begin{split}
 \mathcal L_l={}&
 w_{l-1}(p_{l-3},p_{l-2},p_{l-1},q_l)
 +w_l(p_{l-2},p_{l-1},q_l,\widetilde q_{l+1}),\\
 \mathcal R_r={}&
 w_{r+1}(\widetilde q_{r-1},q_r,p_{r+1},p_{r+2})
 +w_{r+2}(q_r,p_{r+1},p_{r+2},p_{r+3}).
 \tag{5}
\end{split}
\]
These are literal original weights, with the actual conditional
branches, complex planes and both selected alternatives. Their signs
are not prescribed. They depend only on the first or last two run
symbols and their reference windows.

**Proposition 1.** The actual AA edges of the run satisfy
\[
 \sum_{j=l+1}^{r}w_j+\sum_{j=l}^{r}\omega_j
                  \le-\mathcal L_l-\mathcal R_r.
 \tag{6}
\]

**Proof.** An actual AA edge has coordinate support
\(j-2,\ldots,j+1\), and selection support \(j-1,j\).
Replacing any R halo symbol by its baseline symbol leaves its two
target heights unchanged: both real coordinates have \(L_b=1\),
and the halo's selection is irrelevant. Thus each weight on the left
is exactly its weight in the integer-line extension above.

Apply the weighted six-closing-edge theorem to path edges
\(l+1,\ldots,r\), with initial triple
\((p_{l-1},q_l,\widetilde q_{l+1})\) and final triple
\((\widetilde q_{r-1},q_r,p_{r+1})\). The outermost entrance
and exit weights are entirely baseline and vanish. The other four
are exactly (5). The weighted closing formula charges every run
vertex once and its two baseline halo vertices zero. This proves (6).
For a singleton run the path is empty and the two triples agree;
the same zero-length closing theorem applies. \(\square\)

The synthetic weights in (5) are not extra factors in the physical
integrand. They are boundary functions in an inequality. Integer-index
copies are retained when the original reference has a short period.
Thus (6) handles a singleton A-run in a two-cycle without duplicating
either physical edge. A one-cycle cannot be mixed; its all-A and all-R
cases already have their respective source theorems.

## 3. The exact interface reduction

Let \(\mathcal R\) denote the set of original edges incident to a
right vertex. The original finite allocated product obeys, for every
fixed word and every \(\delta>0\),
\[
 \prod_{j=1}^m\mathcal B_{j,N}
 \le C_{m,\delta}N^{B_m}
       \exp N\{M+\mathscr D(x,\sigma)+\delta\},
 \tag{7}
\]
where
\[
 \mathscr D=
 \sum_{j\in\mathcal R}D_j
 -\sum_{I=[l,r]}(\mathcal L_l+\mathcal R_r)
 -\sum_{j:x_j\in A}\omega_j.
 \tag{8}
\]
Indeed the complete AA packets give their coherent weights \(w_j\),
while (3) bounds the other original blocks. Their two Fourier halves
recombine once at each original vertex. Use (6) on each disjoint
A-run. Finally original critical stationarity gives
\(\sum_j\Re\Gamma_j=M\), including every imaginary tangent term.
Choose source tolerance below \(\delta/m\) on each original block.
There are no additional tolerances for the virtual closing weights.
The bounded hybrid Jacobian changes the fixed-word prefactor only.

One explicit sufficient interface condition would be a common
\(\eta>0\) such that every entrance and exit obeys
\[
 D_l-\mathcal L_l-\omega_l/2\le-\eta,
 \qquad
 D_{r+1}-\mathcal R_r-\omega_r/2\le-\eta.
 \tag{9}
\]
The unused run occupation is
\(\sum_{j=l}^{r}\omega_j-(\omega_l+\omega_r)/2\ge0\).
For a singleton its two endpoint halves use exactly its one penalty.
Together with the RR gap, (9) would bound every mixed cycle with a
uniform strict loss before the single finite tolerance in (7).
Equation (9) is an explicit finite-dimensional test, not a proved
inequality.

More generally, for a maximal R-run \([s,t]\), retain its two
interfaces together:
\[
 \mathcal J_{s,t}=\sum_{j=s}^{t+1}D_j
 -\mathcal R_{s-1}-\mathcal L_{t+1}
 -\frac{\omega_{s-1}+\omega_{t+1}}2.
 \tag{10}
\]
Each original R-incident edge occurs in exactly one such expression.
Each A endpoint occupation is charged at most once, with the same
singleton convention. Therefore (8) is at most the sum of (10).
All selections and original type/reference correlations remain in
these functions.

A finite verification scheme can consist of explicit interface ceilings
\(B_-,B_+\), a strict comparison for R-run lengths \(1,\ldots,h\),
and an integer \(h\) satisfying
\(B_-+B_+-h\eta_R<0\), where \(\eta_R\) is an available RR
rate loss. Longer runs contain at least \(h\) internal RR edges.
This reduces the proposed comparison to finitely many bounded windows
once those quantitative ceilings are supplied. No value of \(h\),
nor success of these comparisons, is asserted here. For this raw-rate
formulation one may use \(\eta_R=1/100\): equation (10) of the
two-right proof certifies the underlying raw support gap \(1/50\),
before its finite-source tolerance. This use does not infer a raw-row
inequality merely from the value of a coherent finite sum.

## 4. Optimized finite closing functions

Merely moving the cut one AA edge deeper does not improve (8): the
added actual edge also occurs in the shifted closing path and cancels.
A different, explicit improvement is to optimize the connecting symbols.

Put
\[
 t_j=w_j+\tfrac12(\omega_{j-1}+\omega_j).
 \tag{11}
\]
Every all-A cycle has \(\sum_jt_j\le0\). For a triple state
\(v\) at layer \(i\), and a chosen integer \(h\ge3\), define
\(A_i^{[h]}(v)\) as the maximum total \(t\)-weight of all
length-h paths from the baseline state at layer \(i-h\) to \(v\).
Define \(E_i^{[h]}(v)\) as the corresponding maximum from \(v\)
to the baseline state at layer \(i+h\). In each problem the initial
triple is fixed, and exactly \(h-3\) appended symbols are free.
The entrance's last three appended symbols are its prescribed terminal
triple; the exit's last three are baseline. Free symbols range over
the closed interval \([.1,.5]\), with their allowed selections,
even though physical run counting used the half-open interval A.
All phases in these finite optimization problems are supplied by the
complete nonlow-half source theorem. The maxima exist by continuity.

For any A-run with initial and final states \(v_l,v_r\) from the
proof of Proposition 1,
\[
 \sum_{j=l+1}^{r}t_j
       \le-A_{l+1}^{[h_-]}(v_l)-E_{r+1}^{[h_+]}(v_r).
 \tag{12}
\]
To prove this, combine any entrance connector, the actual path, and
any exit connector, then insert baseline transitions until the length
is a multiple of the original period. The repeated-reference cyclic
inequality applies. The two connector choices are independent, so
their maxima may be taken separately. Padding with baseline transitions
also proves that each family of maxima is nondecreasing in h.

At depth three the two functions reduce exactly to
\[
 A_{l+1}^{[3]}(v_l)=\mathcal L_l+\omega_l/2,
 \qquad E_{r+1}^{[3]}(v_r)=\mathcal R_r+\omega_r/2.
 \tag{13}
\]
Thus larger fixed depths can only strengthen the boundary allowance.
Replacing the two costs in (9)--(10) by (12) gives a strictly specified
finite-window interface problem. Its variables, source branch and
normalization are explicit; an unspecified multiple of a compact
bound does not replace its evaluation. No uniform convergence rate
for these optimized connectors is claimed. The established
[plateau forgetting theorem](research_mixed_plateau_boundary_forgetting.md)
can approximate a fixed-height unselected plateau subproblem, but does
not automatically apply to arbitrary selected A connectors.

Equivalently, apply the anchored incoming-potential construction to
the weight (11). It gives a continuous \(H^t\), zero on baseline
states, with
\[
 \sum_{j=l+1}^{r}t_j\le H^t(v_r)-H^t(v_l),\qquad
 A_i^{[h]}(v)\le H^t(v)\le-E_i^{[h]}(v).
 \tag{14}
\]
Thus the potential-adjusted entrance and exit are respectively
\(D_l-H^t(v_l)\) and \(D_{r+1}+H^t(v_r)\).
The finite-depth functions supply explicit upper bounds on those two
quantities. Although this potential is bounded uniformly in word
length, its numerical values are not supplied by the existence proof;
they cannot be set to zero at arbitrary interface states.

## 5. What the present reduction does and does not resolve

The existing [geometric-replacement obstruction](research_mixed_geometric_right_replacement_obstruction.md)
rules out replacing a right coordinate by its geometric real part and
comparing just its two raw incident edges. The four-cost reduction above
retains the omitted AA boundary changes and therefore has different
bookkeeping. Nevertheless a bounded floating pilot also finds a
positive value of (10) for a one-R component on the actual alternating
reference. The diagnostic files are
`/tmp/diagnose_adjusted_right_components.py` and
`/tmp/adjusted-right-components-diagnostic.json`.
One unselected configuration has adjusted value about \(+.0625\).
These files are not an outward certificate. They provide no universal
source conclusion and do not compare the full cycle with its critical
rate. They are a reason not to promote (9) or (10) as nonpositive.

The half-period minimum-raising inequalities also cannot be applied at
an R endpoint without a new argument. They differentiate conditional
phases on the proved half-period source domains. A right incident
block here has instead the full raw bound (3); its derivative is not
one of those half-stencil inputs. Fixing several initial A symbols can
leave a fixed low cutoff controlling the next row, so it does not by
itself justify ordinary minimum transport on the remaining segment.

Equations (7)--(13) are the resulting structural deduction: all physical
factors occur once, every boundary function is an explicit fixed-window
original-phase quantity, and the remaining sufficient comparisons can
be tested without a word-length cover. Their signs, or a sharper
replacement retaining enough coherent cancellation, remain open.
No full-period asymptotic, external-boundary packet or knot statement
is inferred.
