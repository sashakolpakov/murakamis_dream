# Independent audit of the actual high-color wall source

27 October 2026. The current
[high integral-color construction](high_integral_color_frobenius_wall_source.md)
passes independently, including its generic source germ and signed
crossing/closure comparison. No additional test rerun was needed.

The constant beta gauge gives precisely
\(E=(-1)^rE_{\rm St}\), \(F=F_{\rm St}\),
\(K=(-1)^rK_{\rm St}\) on every block, while retaining the
block-dependent unrolled H. The root Gaussian evaluation yields
\[
 \mathsf Fw_{k,s}=(k+1)w_{k+1,s},\qquad
 \mathsf Ew_{k,s}=(-1)^{Nr-1}(r-k+1)w_{k-1,s}.
\]
Thus the stated normalization gives the ordinary irreducible
\(\operatorname{Sym}^r\) action. The root and generic block
decompositions must remain distinct.

The two regularized between-block edges are also correct:
F gives \(\rho^{-1}f_{\rm cl}\otimes E_{0,N-1}\),
and E gives
\((-1)^{r+1}\rho^{-1}e_{\rm cl}\otimes E_{N-1,0}\).
The first \(h=\log(q/q_N)\) factors follow from
\(1-Q^N=-2Nh+O(h^2)\); the N is essential.

The exponential source has all coordinates one, while its
dual coordinates are \(2^{-r}\binom rk\). Their pairing and
coupon trace are one. With a rank-one head projector, the
normalized high trace multiplied by \(r+1\) gives exactly
\(1/(N2^r)\sum_k\binom rkJ_k\). For r=N this is the wall row,
including its final k=N entry. Replacing the marked head
projector by identity changes this normalization by N.

The new generic source germ is valid. Both integral divided
matrices are regular Gaussian-polynomial matrices and preserve
the residue classes modulo N for generic q as well. Their
exponentials terminate on each finite string. Since the source
pairing is one at the root, its denominator is a genuine unit
germ; its normalized coupon is regular, idempotent, and has
trace one. The string coupons are disjoint, so their sum has
trace N. The exact scalar high-color identity then proves
(4.4), with its actual source derivatives retained. This does
not identify those derivatives with the lower color.

For the signed crossing proof, the full Cartan ratio is
\[
 q_N^{-N[aH_W(j)+bH_W(i)]+2N^2ab}
                         =(-1)^{m(a+b)} .
\]
The factor is independent of head positions but cannot be
discarded on an inserted block-changing network. Both crossing
signs have this same ratio. The pivot block factor is one, and
the twist change is an integer multiple of \(2N^2\), giving
root phase one. On an uninserted one-knot closure the block
index is constant, so the mixed sign becomes its square.
The remaining one-dimensional shift constants cancel against
the retained pivot/twist by knot parity. Thus the original
reduced Kashaev scalar is retained exactly.

Finally, \(M_{\rm high}=(-1)^r\) at the root, and the full
modified-dimension adapter is
\((-1)^{r(N-1)}\), indeed one for r=N.
The old external ADO line remains the appropriate one.
There is no new dimension-\(N(r+1)\) modified trace inferred.

This proves an actual high-color realization of the wall
co-source and its original quantum-normal arrows. It supplies
neither the entire two-current network map nor equality of
low/high whole quantum jets. A vector multiplicity action
also does not by itself identify the full divided Hopf
adjoint on matrix observables. Those limitations are correctly
explicit in the construction.

The subsequent
[actual two-clock source](high_color_two_clock_normal_source.md)
also passes independently. Its whole retraction is regular on
\(1+tu\ne0\). Per-string normalization is what cancels all
source-weight derivatives in the first clock derivative; setting
those derivatives individually to zero would be wrong. The
remaining block mean gives \(Nr\,tu/(1+tu)\), with the required
\(N^2\) for r=N.

The exact source/dual divided-action formulas give the stated
one-sided normalized terms \(rt/(1+tu)\), \(ru/(1+tu)\).
Subtracting left and right actions gives the compact
divergence-free vector fields. The formulas hold entrywise with
head-matrix coefficients and retain the matrix/star product,
including the reversed composition order for right actions.
Their Berry curvature is \(-r\Omega\); the dual positive
prequantum connection has curvature \(+r\Omega\).
The coherent-vector \(O(-r)\) and dual \(O(r)\) clutch signs
are correct.

Combined with
[the actual first-normal R theorem](high_color_first_normal_r_and_frobenius_degree.md),
this supplies a differential realization of that crossing
correction of order at most two on the Frobenius source.
It still does not identify the independent transfer flow
with the geometric centralizer current.

The [all-order Frobenius filtration](high_color_all_normal_frobenius_filtration.md)
also passes independently. The quantum-integer coefficient at extra
normal order j has block-polynomial degree at most j after its
root sign and any forced linear zero are removed. For arbitrary
transfer \(k=aN+b\), the exact numerator/denominator zero count is
\(c_E+c_F-a\). The printed beta exponents cancel all input-block
parity signs. Factoring the forced e- and f-strings then gives
nilpotent degree \(j+a\le2j\); Cartan adds at most twice its
normal order. Inverses, root-conjugated products and ordinary
one-knot closure preserve the bound.

The source interaction ODE is exact. Root unipotent adjoint
conjugation is locally nilpotent on every PBW piece, so Duhamel
products have degree at most twice their summed normal orders.
Since the raw source jets remain in the respective Borel,
their rotated order-j vectors use only the first \(2j+1\)
source descendants, with the analogous dual statement.
The head-diagonal normalization units remain present.

The controlled-shift gauge preserves this filtration only in the
explicit enlarged algebra retaining its degree-zero finite
dilation factors. Their number and analytic norms have not been
bounded by this PBW theorem. The scalar Ward hierarchy uses the
ordinary generic integral ribbon family; a frozen root pivot does
not acquire generic scalarity from this argument.

The revised
[controlled Fourier/current dictionary](controlled_fourier_current_and_conormal_dictionary.md)
also passes. Its original INTEGRAL head currents use the exact
finite circulant \(\Psi_w=\mathcal Fw^S\mathcal F^{-1}\);
its simpler balanced-head formulas require the separately
retained diagonal adapter. The full head-clock normal resolvent
has the correct resonant coefficient \(-(N-1)/(2N)\) and all
nonresonant coefficients \(1/[N(1-\zeta^{\ell+1})]\).
The actual tensor divided-power commutator with the total
unwrapped clock follows from its exact degree N, so no mixed
coproduct term is omitted.

The old-clock scalar normal pairing with the unprojectivized
source also checks: source-unit and Fr-mean derivatives die
under the finite root sum, leaving the nonzero scale character
divided by \(N(1-\zeta)\). Its coefficient is uniformly bounded
and nonzero. This is a scale-line detection statement, not an
independent scalar Fr Ward theorem, and does not identify the
new position clock with the old physical shift.

The later [marked unprojectivized source torsor](actual_unprojectivized_frobenius_borel_torsor.md)
also passes the independent source/form calculation: the actual
paired ket/dual Borel vector fields, equivariant map to r,s,
scale and first-descendant moments, and
Omega_cut=(A/N)dlog U wedge dm are exact. Its Berry curvature
is correctly kept separate. The regular A/Omega_cut chart omits
1+C alpha^2=0. Its standard marked cover is the torsor; the
unmarked Sym^N orbit has nonnormal mu_N isotropy for N>2,
with the central-sign PGL2 exception at N=2 retained explicitly.

The [global Frobenius polynomial/Cech source](global_frobenius_cech_source_and_endpoints.md)
passes in its revised form. Both explicit contractions, the residue
Stokes sign, and the additional source-homotopy term are correct.
The matrix-unit coefficients act in the ACTUAL divided basis;
their global differential lifts are compared only up the stated
homotopies. The dual operators retain the canonical-bundle +2
and the two distinct north/south endpoint cochains. Clock actions
on a source and its adjoint row satisfy residue ADJOINTNESS;
simultaneous pairing-preserving transport uses the inverse dual
clock, as now explicitly stated.

Its whole retained-weight interval proof is exact: the actual
pairing U cancels before integration, the elementary beta integral
gives c_k/[(N+1)binom(N,k)], and both subsequent normalization
units have root one. Delta annihilates the actual source, so
K=I+psi Delta has inverse I-psi Delta, fixes that source and
has the claimed co-source orientation. The base-shift and
connection transport must include sigma(K) and dK respectively.
No uniform metric, PBW degree or geometric-current conclusion
is silently imported into this rational source gauge.

The [endpoint-completed whole Jackson current](endpoint_completed_normal_clock_euler_current.md)
also passes independently. Its actual inverse arrows are regular
germs, its shifted argument and endpoint projector orders are
essential, and its finite normal kernel and averaged factor N
are correct. The off-diagonal remainder retains the ordered
matrix currents, so the assertion remains a character-subalgebra
map. The [whole function/endpoint extension proof](whole_clock_function_algebra_and_endpoint_extension.md)
adds the infinite-order functional-quotient obstruction, an exact
flat confluent tower and its Newton lattice, and root inverse
norm N^(-1/2). The actual top spectral-polynomial defect begins
at normal order N; it cannot be discarded at the whole-function
level merely because any fixed smaller jet misses it.

The [actual relative endpoint period](actual_frobenius_relative_endpoint_period.md)
keeps the marked moving endpoints and original normalization
units through all normal orders. Its explicit first-normal
counterexample shows that the naive original divided-Borel
generator does not automatically equal that source connection.
The retained-weight uniform interval is rational; the unweighted
normalized interval is a different relative period. Their exact
distinction and the source-current correction remain necessary
for a future network/Gaussian comparison.

The [full matrix degree-elevation/current map](degree_elevation_actual_head_ward_map.md)
passes independently: its two row-index terms give exact symbol,
normalized trace and original average-cut preservation; the whole
head D and actual divided-string B_s gauges have the correct
orientations. The Hopf F-to-commutator row operation retains its
ordered K-row product. Its B_Fr homotopy is regular because the
two omitted target corners vanish IDENTICALLY on its image.
This image condition cannot be extended to arbitrary Fr currents.

The [complement Bockstein wall](degree_elevation_complement_bockstein_wall.md)
also passes: every interior fork contracts by a unit f-arrow,
even at intermediate resonant weights. The bottom remaining
arrow is a root unit and the top one is delta/(1-delta).
Its co-source must remain the ACTUAL one: selected coherent
weight2^-N and uniform interval weight1/(N+1) differ on a genuine
root Ward cycle. They cannot be equated by a fixed-current
co-source homotopy. The literal charged first-normal R current,
its wall coefficient and both displayed source pairings check.

The [explicit incidence/source audit](degree_elevation_wall_residual_and_source_moments.md)
gives the exact quotient polynomial, whole selected source
character and one-sided Green moment correction. In particular
Ad-clock covariance does not remove the auxiliary bit from
one-sided clock coupons.

Finally, the [Clebsch matrix-memory strictification](clebsch_memory_dilation_and_actual_r_excursions.md)
passes with its full lower channel, whole gauge/source/cap
transport and auxiliary trace1/2. The per-strand minimality and
metric factors are correct. Its actual R leakage and inverse-pair
defect are nonzero uniformly in N, so upper-only words cannot
replace the strictified word. This is an exact extension of the
old head R representation; matching it to the actual high-color
R or internal Gaussian currents remains a separate theorem.

The revised hybrid-metric conclusions in
[the clock/current source audit](frobenius_clock_and_internal_centralizer_map.md)
Sections 7--8 also pass independently. Keeping the Fr binomial
metric and OLD flat head metric makes G unitary and the original
Fourier/N scalar-unitary, so their conjugation is exactly isometric.
The selected coupled e_D is then an orthogonal rank-one projector.
The highest-spin Hilbert--Schmidt projection remains contractive;
converting HS to operator bounds costs only sqrt(ambient dimension).
For the phase clock its normalized highest-spin coefficient is
(1-z)^N/binom(2N,N), with the stated polynomial HS bound. This
does not alter the selected2^-N versus uniform1/(N+1) wall source
or bound the actual R word, normal neighborhood or head D gauge.
The earlier exponential G bound used a DIFFERENT head coherent
metric and remains valid there.

The whole divided-Ward/pivotal closure identities and their actual
Cartan wall inverse pass the independent proof audit recorded in
[the global Green tail/current note](global_green_cut_tails_and_wall_transport_residual.md).
It verifies the divided coproduct/adjoint q-powers, frozen cap
clock and first-normal signs, the ordered N-term cap cancellation,
the literal diagonal Cartan-unit inverse, and the nonzero sourced
R return at first order delta^N. The full selected source and
mixed coproducts remain present. This is an actual cut-current
construction; its partial-Gaussian/internal-framing map remains
the separate stated task.

The [whole Fermat-trace source](whole_frobenius_source_fermat_trace.md)
passes independently at every residue and parity. Its constant-frame
ket retains beta divided by the ACTUAL Gaussian coefficient; that
coefficient has root(-1)^(ks), leaving the stated triangular phase
in the divided-kN expansion. The dual sign cancels the symmetric
Gaussian root phase and gives binom(N,k). Each full deck block
is exactly1+t, and the leftover degree<N is killed by the filter.
The norm sign theta_s and all Z powers check as well; its fractional
head norm/trace factors multiply to the original source character.

For the first normal, zero-factor ratios have zero first relative
log derivative. Grouping nonzero residues gives kN times the
partial cotangent sum, with complementary partial sums equal;
q partial_q=-2N partial_delta gives the printed ell_s sign.
The flag derivative, whole cap-clock ratio and root-identity pair
gauge are exact. This compares whole coupons only when all inserted
operators and source connections are conjugated too; it does not
equate their untransported quantum jets or bound their growing-N
period norm.

The [whole actual Ward-grid contraction](whole_high_color_ward_grid_contraction.md)
passes independently with no correction. K separates head residues,
the actual diagonal divided Cartan separates Fr blocks, and the
selected ordinary/divided F edge entries read diagonal differences
without ANY off-diagonal contamination. The comb subtree signs,
trace-centered primitive and complete rational source row check.
Its target is correctly im(delta), an explicit direct summand;
the unrestricted four-row cokernel is not declared zero.

In the stated hybrid root metric the inverse K and H gaps have
the printed bounds. The normalized actual F edge has size at least
one, the divided edge at least sqrt(r), and the path integration
matrix has squared Frobenius norm D(r+N-1)/2. Orthogonal output
pieces therefore give exactly the stated maximum norm bound.
The selected e_D source has Hilbert--Schmidt norm one, so its
homotopy cost is polynomial. Actual whole source units, grading,
peripheral lines and all gauge adapters remain present.

The two-word variant also checks: H+K/2 has simple full-grid
root spectrum by the triangle inequality, and F+Fdiv has distinct
one-step/N-step edge positions. Subtracting its action on the
already recovered off-diagonal matrix is essential and is included.
This is an actual finite-cut contraction, with its true mixed Hopf
and pivotal current endpoints supplied by the cap theorem. It is
not yet a nonzero map from the internal geometric period complex.

