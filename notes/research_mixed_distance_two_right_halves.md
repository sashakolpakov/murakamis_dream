# Conditioned half derivatives with a right vertex at distance two

Research certificate formulation, 5 November 2026. The exact reduction
and acceptance implication below concern one half of a minimum-flow
derivative. The complete sign assertion requires a passed record for
every one of the 400 specified domains. A bounded construction that
stops early does not establish that assertion.

## 1. Literal halves, states and conditioned reference coefficients

Keep the original allocated phase \(\phi_{\eta\epsilon}\), normalized
primitive \(g\), and zero logarithmic lift from
[the local half theorem](research_mixed_minimum_level_half_stencils.md).
Let \(t\in[.12,.22]\) be a moving minimum, \(y\in[t,.5]\) its
nonright neighbor, and
\[
 \rho=(t-.1)/.12,\qquad
 R(y)=
 \begin{cases}1,&y\le.45,\\400(.5-y)^2,&.45\le y\le.5.\end{cases}
 \tag{1}
\]
The outer vertex of this half is right and has already been fixed
at \(.5\). All other nonright coordinates are at least \(t\).
There are no early or collar coordinates in this assertion.

The center and neighbor states are \(U_3,U_4,S_4\). For unselected
states their original reference height coefficients are \(c_c,c_n\);
their targets are
\[
 z_c=t+ic_c\rho,\qquad z_n=y+ic_nR(y)\rho.
 \tag{2}
\]
A selected state instead has target height \(H=.014\) at the center
or \(HR(y)\) at the neighbor. Its height velocity coefficient is
zero. Thus put
\[
 b_c=\begin{cases}c_c/.12,&U,\\0,&S,\end{cases}
 \qquad
 b_n=\begin{cases}c_nR(y)/.12,&U,\\0,&S.\end{cases}
 \qquad q=1+i\chi b_c,\quad v=i\xi b_n .
 \tag{3}
\]
Unselected switches \(\chi,\xi\) range independently over
\(\{0,1\}\); a selected state's switch is zero. In particular,
the factor \(R(y)\) occurs in both the neighbor target height
and its height velocity.

For a four-type window \(w=(w_0,w_1,w_2,w_3)\in\{0,1\}^4\),
the right half uses center index 1 and neighbor index 2, with
index 3 right. The left half uses center index 2 and neighbor
index 1, with index 0 right. The remaining outer type only
conditions the center's reference height. The exact coefficient
intervals are obtained as follows.

1. Start with \(C_3=[-.03,.02]\), \(C_4=[-.057,-.02]\).
2. Intersect each coefficient with the middle-coordinate height
   interval for its known triple in the
   [conditioned critical table](research_mixed_neighbor_conditioned_critical_boxes.md).
3. Also use that table's first-coordinate interval for the following
   triple. When its last type is unspecified, take the interval hull
   over its two possible types before intersecting.
4. For a type-four coordinate followed by type four, intersect with
   \([-.056,-.048]\), as proved by the
   [consecutive-four extraction](research_mixed_four_before_four_height_lower.md).
   If its preceding type is also four, intersect its upper endpoint
   with \(-.053\) by the
   [three-four corollary](research_mixed_three_consecutive_four_height.md).

These are closed containing intervals for actual cyclic references.
The two coefficients remain shared throughout each half; their
independent interval enlargement does not assert realization of
every pair by an actual reference. The checker reconstructs the
intervals from the exact integer table, not displayed extrema.
Short cyclic words are repeated before applying these geometric
window theorems, as in their proofs.

## 2. The optimized raw contribution and the two orientations

For the neighbor raw edge let \(\alpha\) be its neighbor type
indicator and \(d=1\) if that neighbor is the first argument.
Its row \(u_*\) is the unique maximum from the
[raw-row theorem](research_mixed_raw_row_stationarity.md), with
\[
 1/5<u_*<2/5,\qquad
 K(z,u)=g'(z+u)-(1+\alpha/2)g'(z)+2\pi i d u.
 \tag{4}
\]
All nonzero neighbor velocities here are unselected. A selected
neighbor has \(v=0\), so both true Fourier alternatives have zero
local derivative. A selected center moves only in real part below
\(.22\); its strict true correction is the constant \(-2\pi H\).
Thus (4) and the allocated coherent partials retain the full
selected derivative. No forcing branch is discarded at a moving
state.

Let \(\kappa=3/2\) and \(\gamma=\mathbf1_{\{c\text{ selected}\}}/10\).
For the right half \(c\to n\to R\), define
\[
 \mathcal D_R
 =\Re\!\left[
 q\{\phi_{\alpha_c\alpha_n,1}(z_c,z_n)-i\kappa\}
 +v\{\phi_{\alpha_c\alpha_n,2}(z_c,z_n)
                            +K(z_n,u_*)\}\right]-\gamma,
 \quad d=1,\quad \epsilon=w_3 .
 \tag{5}
\]
For the left half \(R\to n\to c\), define
\[
 \mathcal D_L
 =\Re\!\left[
 q\{\phi_{\alpha_n\alpha_c,2}(z_n,z_c)+i\kappa\}
 +v\{\phi_{\alpha_n\alpha_c,1}(z_n,z_c)
                            +K(z_n,u_*)\}\right]+\gamma,
 \quad d=0,\quad \epsilon=\alpha_n .
 \tag{6}
\]
The own raw indicator \(\epsilon\) is retained when determining
\(u_*\), even though it does not occur explicitly in \(K\).
Both gauges are precisely those of
[constant selected transport](research_mixed_constant_selected_height_transport.md);
they cancel against the opposite half when the shared center
coefficient and switch agree.

**Certificate implication.** If every complete domain specified in
Section 4 is accepted, then (5) and (6) are strictly positive for
all actual configurations in this note. Their contribution to the
conservative whole derivative is therefore nonnegative. This
does not alone treat the opposite half, an early minimum, or a
full complementary region.

All coherent targets lie in the established early-cap, plateau
and right-triangle union. Its original complete packets are given
by the [early-cap theorem](research_mixed_early_selected_source_cap.md),
the [interface theorem](research_mixed_left_right_interface_source.md)
and the [right-square theorem](research_mixed_unselected_right_taper_products.md).
They give the same original holomorphic phase on overlaps before
any derivatives or interval enclosures are taken.

## 3. Original real-row enclosure and exact derivatives

The row equation and its uniform slope are
\[
\begin{split}
 T(u,z)&=\Re\{g'(u+.5)+g'(u+z)
       -(2+\epsilon)g'(u)+2\pi i[dz+(1-d)/2]\},\\
 T(u_*,z)&=0,\qquad T_u\le-2\pi .
\end{split}                                                     \tag{7}
\]
For any rational trial \(u_0\in[1/5,2/5]\), the mean-value
theorem gives the whole-parameter enclosure
\[
 |u_*(z)-u_0|\le |T(u_0,z)|/(2\pi).
 \tag{8}
\]
Intersect it with the original bracket. Construction chooses a
trial by signed interval bisections at the parameter midpoint;
acceptance uses (8), not the proposed accuracy. Each retained
witness stores the rational trial. Replay checks (8) anew using
that trial and makes no row proposal.

For any real parameter \(p\), differentiation gives
\[
\begin{split}
 M&=g''(z_n+u_*)+2\pi i d,\qquad
 K_z=g''(z_n+u_*)-(1+\alpha_n/2)g''(z_n),\\
 (u_*)_p&=-\Re(M(z_n)_p)/T_u,\\
 K_p&=K_z(z_n)_p+M(u_*)_p .
\end{split}                                                     \tag{9}
\]
The real implicit response is essential. Complex critical
stationarity is not substituted for (7).

The original coherent Schur Hessian gives the derivatives of
its two partials. For either orientation write \(G_c,G_n\) for
those partials, \(H_{ij}\) for that Hessian in center/neighbor
order, and \(s=+1\) for left, \(-1\) for right. The acceptance
gradient is exactly
\[
\begin{split}
 \partial_p\mathcal D={}\Re\big[
 &q_p(G_c+s i\kappa)
   +q\{H_{cc}(z_c)_p+H_{cn}(z_n)_p\}\\
 &+v_p(G_n+K)
   +v\{H_{nc}(z_c)_p+H_{nn}(z_n)_p+K_p\}\big].
\end{split}                                                     \tag{10}
\]
In the upper piece, derivatives of \(R(y)\) occur in both
\((z_n)_p\) and \(v_p\). Selected actual heights remain \(H\)
or \(HR(y)\), even though their coefficients in (3) are zero.

The complex root and its midpoint are separately enclosed by the
frozen original-logarithm affine disk self-map. The row midpoint
is enclosed separately by (8). The direct interval value and the
midpoint value minus full-box derivative radii are valid lower
bounds. Their larger outward lower endpoint is used. Every
nonfinite Schur or row derivative causes rejection/subdivision.

## 4. Complete finite family and saved-cover acceptance

For each four-type window, orientation, permitted center/neighbor
selection and switch, use four parameters in \([0,1]^4\).
Their exact map is
\[
\begin{split}
 t&=.12+.10v_0,\qquad c_c=\ell_c+(h_c-\ell_c)v_2,\qquad
 c_n=\ell_n+(h_n-\ell_n)v_3,\\
 y&=t+(.45-t)v_1 &&\text{in the lower piece},\\
 y&=.45+.05v_1 &&\text{in the upper piece}.
\end{split}                                                     \tag{11}
\]
Selected coefficients are unused and set to zero only in the
velocity expressions; their actual target heights are defined
in Sections 1 and 3. Degenerate inactive directions remain in
the unit cube without being split.

For each endpoint type, the combined state/switch count is two
for type three and three for type four. The two unrestricted
outside types and the two orientations therefore give
\[
                  4\cdot2\cdot(2+3)^2=200                    \tag{12}
\]
domains in each real piece, hence 400 domains in the exact
ordered family. No word-length enumeration is used.

Each binary split has both exact rational children. A monotonic
node retains its minimizing endpoint only after the relevant
partial derivative has a strict sign on the whole box, using
that node's full original root witness. A leaf requires a
strictly positive outward lower bound. A saved replay reconstructs
the exact initial cube of each domain, consumes every node and
checks every root witness, row trial, monotonicity decision and
inequality. Missing domains or remaining boxes prevent a complete
pass. All proof, arithmetic and inherited geometric/source hashes
are checked before and after the run.

Construction has a total cap of 200,000 visits or 120 seconds.
The cap does not apply to a replay, which must consume its complete
prescribed cover. An incomplete construction is retained explicitly
as incomplete and cannot satisfy the certificate implication.

For a one- or two-cycle there is no new assumption of four distinct
vertices: actual repeated variables satisfy additional equalities
inside the independently enlarged local domains. The two gradient
incidences and the shared center switch are retained. The usual
conservative negative-height accounting counts repetitions in the
safe direction. This is a local derivative result, not a finite
kernel lower bound or a new knot-family theorem.

    python3 experiments/certify_mixed_distance_two_right_halves.py --precision 256
    python3 experiments/certify_mixed_distance_two_right_halves.py --precision 384 --input repro/results/research-mixed-distance-two-right-halves.json --output /tmp/research-mixed-distance-two-right-halves-replay.json
