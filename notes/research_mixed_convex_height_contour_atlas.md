# Exact outer joins and a convex-height contour atlas

Research deduction, 6 November 2026. A prescribed smooth taper is not
required for the original Laurent source. Rectilinear outer paths are
exact cycles if all their vertical joins are retained. More generally,
overlapping fixed-height source certificates can be blended into one
periodic contour without a rate loss when their common upper envelope
is convex in height. Neither construction needs concavity along the
resulting graph or a bound on its second derivatives.

This gives a finite certificate format for replacing a boundary taper.
It does not assert that the required nonplateau patch inequalities
have been proved. An original type-four source example below shows why
one cannot simply release every plateau height independently down to
zero and expect the geometric upper bound to survive.

## 1. The exact source admits rectilinear outer cycles

Fix a word, a type-compatible selected Fourier summand, and any fixed
ordinary-color jets. Let \(F_N(X_1,\ldots,X_d)\) be its complete
Laurent-polynomial density, including all \(d_N\), \(X_j^{-N}\),
ordinary kernels and complete endpoint factors. The
[exact torus identity](research_mixed_conditional_torus_composition.md)
supplies this polynomial and its original outside scalar. Alternatively
one may first perform an exact retained-variable contraction; the
argument applies to the resulting entire Laurent density.

Choose \(0<L_j<R_j<1\) and a fixed real height \(c_j\). On the
complex cylinder \(\mathbb C/\mathbb Z\), let \(\gamma_j\) be the
following five oriented segments:
\[
0\longrightarrow L_j\longrightarrow L_j+ic_j
\longrightarrow R_j+ic_j\longrightarrow R_j
\longrightarrow1.
\tag{1}
\]
The path also makes sense when \(c_j<0\); both vertical orientations
are those displayed in (1). Then
\[
\operatorname{CT}F_N
 =\int_{\gamma_1\times\cdots\times\gamma_d}
 F_N(e^{-2\pi iz_1},\ldots,e^{-2\pi iz_d})
                         \,dz_1\cdots dz_d.
\tag{2}
\]
The sign in (2) is positive. In one variable a nonconstant Fourier
monomial has an entire periodic primitive, while
\(\int_{\gamma_j}dz_j=1\). Expand the finite Laurent polynomial
and apply these identities in every variable. This proves (2)
with all ordinary jets and both parities, without a logarithmic
interpolation or a contour at infinity.

Expanding the product of paths produces every horizontal/vertical
face with its orientation and multiplicity. In particular, a
discontinuous height prescription consisting only of the horizontal
pieces would omit terms. Here no such term is omitted. The total
variation of the product chain is at most
\[
                         \prod_j(1+2|c_j|).
\tag{3}
\]
This is a fixed-word prefactor, independent of \(N\).
Different selected Laurent summands may use different paths.
One may also replace only some coordinate circles and leave the
others unchanged.

## 2. Whole joins reduce to height corners

Let a real face have horizontal coordinates \(x_i\) in fixed
intervals and some vertical coordinates with fixed real parts
\(x_j=L_j\) or \(R_j\). Suppose a finite set of original, calibrated
holomorphic profiles \(\Phi_\rho\) bounds the complete source on
a neighborhood of the resulting tube:
\[
 |F_N(e^{-2\pi i(x+ih)})|
 \le C_\tau N^{A_\tau}
       \exp N\{\mathcal E(x,h)+\tau\},\qquad
 \mathcal E(x,h)=\max_\rho\Re\Phi_\rho(x+ih).
\tag{4}
\]
Original complex affine debits may be included in the profiles.
All full Fourier alternatives and all finite currents must occur
in this upper envelope. Its constants must be uniform on the
closed tube under consideration.

**Lemma 1.** If each profile is horizontally concave on the whole
complex tube, then \(\mathcal E(x,h)\) is convex in the height
variables on each convex height fiber. In particular, on a
rectangular vertical face,
\[
\mathcal E(x,h)
 \le \max_{\eta\in\operatorname{Vert}Y}\mathcal E(x,\eta).
\tag{5}
\]

*Proof.* Holomorphy gives the exact matrix identity
\[
                 \partial_h^2\Re\Phi_\rho
                            =-\Re\Phi_\rho''\succeq0.
\tag{6}
\]
The maximum of finitely many convex functions is convex. Repeated
linear interpolation in the height coordinates proves (5).
Fixed real rows or absent index coordinates cause no extra term.
Affine chirps and affine supporting planes have zero pure-height
Hessian, with their original values still retained. \(\square\)

For ordinary plateau windows, the
[finite profile theorem](research_mixed_plateau_window_concave_profiles.md)
supplies the seven labels and the needed bare Hessians on the full
common height box. For each fixed choice of its main indices,
(6) applies in the outer heights. Taking the maximum over those
indices preserves height convexity too. The four last-row carriers
are affine; the two actual Fourier alternatives are included before
taking this maximum. The assertion therefore controls the complete
ordinary upper envelope, not only a chosen main saddle.

With \(L_j=.22,R_j=.45\), every vertical join lies at a real
plateau boundary. Its other active real coordinates may also
remain in the plateau, so (5) reduces such faces to fixed-height
profiles eligible for the tangent rule. A join coordinate is fixed
at its cut, even at its zero-height corner. It must not subsequently
be released over all of \(P\). Sections 4 and 5 explain why that
extra relaxation can destroy the desired sign.

For each height corner, the supporting-affine bound of the profile
theorem controls the remaining real variables. If every such
corner has rate at most \(M-\delta\), (3)--(5) bound the entire
join integral by a polynomial prefactor times
\(e^{N(M-\delta+\tau)}\). This is a continuous-height theorem;
there is no mesh approximation to a vertical side.

The horizontal real tails in (1) are different faces. A plateau
Hessian does not cover their real targets. Those faces still need
their full finite source bounds, as do mixed faces involving a
terminal transform. No maximum principle on a rectangle removes
them from (2).

## 3. Blending certified heights, with no join loss

Here is a more flexible construction that avoids explicit vertical
faces. Its data are finite, but the conclusion holds at every
point of the resulting contour.

For each \(x\in\mathbb T^d\), let \(Y_x\subset\mathbb R^d\) be a
convex admissible height set, and suppose the literal source bound
(4) holds with an envelope \(\mathcal E(x,\cdot)\) convex on \(Y_x\).
The real dependence of \(\mathcal E\) need not be concave. A piecewise
definition in \(x\) is allowed, provided the same bound and height
convexity hold on every piece and its boundary.

Take finitely many real patches \(O_a\), height fields \(h^a\)
defined near them, and nonnegative periodic Lipschitz functions
\(\chi_a\), subordinate to these patches, with
\(\sum_a\chi_a=1\). Constant fields \(h^a\) are the main
certificate format. Require, whenever \(\chi_a(x)>0\),
\[
h^a(x)\in Y_x,\qquad
\mathcal E(x,h^a(x))\le M-\delta(x),
\qquad \delta(x)\ge0.
\tag{7}
\]
Membership and the bound may instead be checked on the closed
support of \(\chi_a\), which is convenient for finite certificates.
All fields and their first derivatives are bounded, and the source
bound holds on their full fiberwise convex hull.

**Theorem 2.** The height field
\[
                         H(x)=\sum_a\chi_a(x)h^a(x)
\tag{8}
\]
defines an exact periodic contour for the original Laurent integral
and obeys
\[
\mathcal E(x,H(x))\le M-\delta(x).
\tag{9}
\]
Its Jacobian has a finite \(N\)-independent bound. No derivative
of \(\mathcal E\), no graph Hessian, and no fixed active profile
are required.

*Proof.* Convexity of \(Y_x\) gives admissibility of (8).
The pointwise convex inequality, with \(x\) fixed, gives
\[
\mathcal E(x,H(x))
 \le\sum_a\chi_a(x)\mathcal E(x,h^a(x))
 \le M-\delta(x).
\tag{10}
\]
For explicit derivative control, suppose
\(\|Dh^a\|_{\mathrm{op}}\le L\),
\(\|h^a\|_2\le R\), and
\(\sum_a\|\nabla\chi_a\|_2\le C_\chi\). Then almost everywhere
\[
\|DH\|_{\mathrm{op}}\le L+RC_\chi,\qquad
|\det(I+iDH)|\le
             \{1+(L+RC_\chi)^2\}^{d/2}.
\tag{11}
\]
The second inequality follows from Hadamard's row bound for real
\(DH\). The exact
[periodic graph identity](research_mixed_coupled_outer_graph.md)
therefore applies. Its Lipschitz extension is proved in Section 3
of [minimizing-height transport](research_mixed_minimizing_height_transport.md)
by periodic smoothing and convergence of all Jacobian minors.
It retains the closed holomorphic form, all selected factors,
ordinary jets, and the original scalar. There are no missing
seam or transition currents. \(\square\)

One explicit finite construction of the \(\chi_a\) is to choose
buffered real boxes and nonnegative piecewise-linear bump functions
\(\psi_a\) supported in them, with \(\sum_a\psi_a\ge\eta>0\).
Set \(\chi_a=\psi_a/\sum_b\psi_b\). The strict cover margin
\(\eta\), the finitely many slopes and support bounds give
\(C_\chi<\infty\). All these choices are fixed independently
of \(N\).

For constant fields, (7) is precisely a collection of fixed-height
profile tests on real boxes. Each labeled real-target maximum can
be bounded by one rigorously enclosed trial value and gradient.
Overlapping heights are then interpolated by (8), with no extra
exponential allowance. A new stationary height, or a claim of
concavity of the pointwise maximum in real variables, is unnecessary.

There is an important compatibility requirement: the envelopes used
for the active height choices must give one common convex envelope
on their overlap. Taking the minimum of different patch-specific
upper bounds does not preserve convexity. Nor do separate packet
theorems at two heights prove (4) throughout their height segment.
Both the finite-source domain and the profile curvature must cover
the full segment before (10) may be used.

The construction can be local. Keep the old periodic height field
outside a boundary region and on a collar of its boundary, and
include it among the certified fields wherever a transition is
made. Formula (10) then glues a new certified field to that old
field without loss, if both satisfy the common bound on the collar.
To preserve the original geometric coefficient, require the field
to equal the original constant reference heights on a neighborhood
of the unselected critical point. For example all active \(h^a\)
there can equal that reference vector. The finite local integral,
its orientation and nonzero Gaussian coefficient are then literally
unchanged.

Thus, conditional on a complete patch certificate with a fixed
positive \(\delta\) off that neighborhood and the existing local
packet, the complement is exponentially small on this new contour.
This is an exact sufficient criterion for a whole fixed-word source
estimate. It does not assert that the required patches exist.

**Corollary 3 (compact pointwise feasibility).** Let \(K\) be a compact
real region. Suppose the common source tube is open in a neighborhood
of \(K\times\mathbb R^d\), with convex height fibers, and
\(\mathcal E\) is continuous on this tube and convex in height.
Assume the complete source bound is uniform on its compact subsets.
If for every \(x\in K\) there is an admissible height \(h_x\) with
\(\mathcal E(x,h_x)<M\), then finitely many constant-height patches
as in (7) cover \(K\) with one uniform gap \(\delta>0\).
They give a Lipschitz height field with this gap on \(K\).

*Proof.* Openness of the common tube makes the chosen constant
height \(h_x\) permissible on a real neighborhood of \(x\).
Continuity shrinks that neighborhood so that its rate is at most
\(M-\delta_x\), for some \(\delta_x>0\). Choose buffered
subpatches and then a finite subcover of \(K\). The minimum of
their finitely many positive margins is positive. Their height
vectors are bounded, and the subordinate construction above gives
(8)--(11). In particular no continuity, uniqueness or differentiability
of a pointwise minimizing height is used. \(\square\)

If \(K\) is the full torus, this already gives the closed contour.
For a proper compact region it only gives a local field. An exact
replacement of part of an existing cycle additionally needs the
gluing collar in Theorem 2: the old field and the new active heights
must be admissible and satisfy the common bound there. Compactness
does not provide that collar, does not extend this conclusion to a
noncompact or degenerating source domain, and does not establish
pointwise feasibility for the actual nonplateau source.

## 4. Why unrestricted reset corners cannot supply the certificate

There is a source-specific obstruction to the simplest proposed
relaxation. Consider an original homogeneous type-four cycle and
its unselected conditional phase
\[
\Phi(z)=\sum_j\phi_{11}(z_j,z_{j+1}),
\qquad r=x_*+ic,\qquad \Phi'(r)=0.
\tag{12}
\]
Its actual retained heights are nonzero and belong to
\((-.057,-.02)\); its real coordinates belong to \((.27,.33)\).
The [full height-reset theorem](research_mixed_full_height_reset.md)
proves strict positive allocated negative real Hessians on the
full product containing the segment
\[
                         z(t)=x_*+i(1-t)c,\quad 0\le t\le1.
\tag{13}
\]
Sum those edge forms, including repeated incidences for short cycles.
By compactness there is \(\mu_*>0\) such that
\(-\Re\Phi''(z(t))\succeq\mu_*I\) on this segment. Hence
\[
\begin{split}
\Re\Phi(x_*)-\Re\Phi(r)
 &=\int_0^1(1-t)\,
       c^T[-\Re\Phi''(z(t))]c\,dt\\
 &\ge\tfrac12\mu_*\|c\|_2^2>0 .
\end{split}
\tag{14}
\]
The first derivative at \(t=0\) is zero by original stationarity;
the displacement is \(-ic\), so the sign in (14) is positive.

This is the actual marked phase. At the target \(x_*\), the
[complete right-square packet](research_mixed_unselected_right_taper_products.md)
has its original nonzero coefficient. The
[Fourier continuation criterion](research_mixed_fourier_weight_continuation.md),
Section 5, is relative there because \(-\Re g(x_{*,j})>0\)
on \((.27,.33)\), while the forcing rate at height zero is zero.
Thus the modulus of the entire unselected Laurent density has
rate \(\Re\Phi(x_*)\), including its polynomial powers.
An absolute geometric-rate upper bound on the whole independently
reset plateau is false, even though the geometric integral may
have its established asymptotic.

Equation (14) does not obstruct a rectilinear contour whose reset
corners occur only at distant real cuts, or an atlas whose
admissible heights preserve the reference near \(x_*\). It shows
why the real-coordinate location of a reset must remain in each
face/patch certificate. Cancellation in the final integral has
not been replaced by positivity or a scalar lower bound.

## 5. Relation to the remaining open boundary problem

For ordinary plateau targets, the new finite-profile Hessians
already give the height-convexity input of Theorem 2 on their
full source tubes. The known selected right-taper argument also
uses height-corner convexity on its own proved source products.
The present contribution is the exact outer-cycle and gluing
mechanism: fixed-height certificates can select the contour,
rather than merely estimate a previously prescribed taper.
It differs from the minimizing-height theorem, which requires a
single holomorphic phase and optimizes it on a common height box.
Here the complete finite maximum of all source/Fourier profiles
is retained, and only height convexity is used.

Outside these domains, three obligations remain explicit:

- Real tails and low/terminal sectors need a complete upper envelope
  on the proposed height tubes, including every revived row and
  original Fourier branch.
- Each active fixed-height choice must satisfy the desired original
  action/tangent comparison on its entire real patch. Local packets
  or geometric root existence alone do not imply these signs.
- Overlaps, collars and the original critical neighborhood must
  satisfy the compatibility conditions in Section 3.

The existing [full-period occupation theorem](research_mixed_full_period_occupation.md)
is tied to its actual hybrid heights and their incidences. It is
not automatically a theorem on (1) or (8). A local boundary
replacement can retain that middle argument by leaving all its
height variables and closing-term inputs unchanged; only the
literal boundary source factors then need new estimates. Otherwise
the affected occupation comparisons must also be reproved.

All exact Fourier weights, boundary polynomials, ordinary jets and
finite Jacobians remain present. No new source gap, complete open-word
asymptotic, or cofinite filling-volume result is claimed here.
