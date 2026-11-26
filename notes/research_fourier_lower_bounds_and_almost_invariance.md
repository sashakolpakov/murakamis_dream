# Fourier lower bounds and almost-invariant vectors

Research note, updated 4 November 2026.

There are two different uses of a positive norm in this problem.
For the complete-color Fourier state, its norm differs from the
squared Kashaev invariant by a proved polynomial remainder. A lower
bound for that norm would therefore prove a lower bound for the
invariant. For the positive sums obtained by replacing local terms
by their absolute values, the available comparison goes in the other
direction. Positivity of the comparison sum does not supply the
missing lower bound.

There is now an actual initial family for changing the Fourier
charge. The [small-charge theorem](research_small_charge_path_source.md)
proves a nonzero leading contribution for every fixed positive path
with crossing powers at least three, after inserting
\(T_{N-j_v}(-w_v/2)\) in its original traces and taking
\(j_v/N\in[1/640,1/320]\). The coefficient is computed from the
exact trace contour; every competing charge and endpoint term is
bounded. Continuing this coefficient to \(j_v=N\), where the
insertions disappear, remains the lower-bound problem. A nonzero
starting contribution and a continuous geometric critical point do
not themselves prove that continuation.

On \([1/4000,1/2000]\), the statement extends to any fixed finite
graph carrying these edge kernels, with no isolated selected vertex,
and allows arbitrary fixed signed integer crossing powers, including
zero. Section 16 verifies the Gaussian analogue of almost-invariance
for this initialized source: its rescaled integrand has a nonzero
independently computed norm and an \(O(N^{-1/2})\) relative
annihilation residual. These estimates currently hold on the small
charge box; a knot realization of an arbitrary such graph is not
part of the assertion.

The [exact charge recurrence](research_current_free_aw_crossing_transport.md#10-a-closed-recurrence-for-the-original-charge-observations)
retains the free boundary color and has nonvanishing outer coefficients.
With the physical period and reflection relations imposed, its solution
space has dimension two at every free color. The original endpoint
condition selects the actual source line. The extra solution has zero
physical values and only first-normal data. This removes an ambiguity
in the finite equation, but line uniqueness does not bound a particular
Fourier observation of that line.

The [charge-increment norm](research_charge_increment_graph_norm.md)
now gives an exact positive identity and a sharp asymptotic for every
fixed graph carrying these same-index kernels. Its increments discard
the normals by an exact period difference, and Parseval removes the
unit crossing phases from their squared norm. The resulting growth is
the sum of the unfilled edge rates, independent of the twists. For the
proved three-crossing terminal source, the central coefficient divided
by this norm is exponentially small. The full charge vector therefore
has a rigorous lower bound without a corresponding lower bound for its
specified central entry. This is an actual-source limitation of this
particular positive Fourier norm.

There is already a stronger local lower bound in the
[all-color theorem](research_all_color_path_normal_bound.md#5-the-complete-normal-determinant-at-every-color-assignment).
For a fixed filled tree with crossing powers of one sign, suppose
\(Q_G=\operatorname{diag}(|n_v|)-\operatorname{Adj}(G)\) is
positive definite. At each physical color assignment, the complete
first-normal factor is a determinant with a positive definite
imaginary part after the stated normalization. Its modulus is bounded
below by a power of \(N\) times the positive kernel product, and
bounded above at polynomial additional cost. Thus cancellation within
one color assignment is already controlled under this condition.
The outstanding cancellation is between different assignments,
which retain their original crossing and determinant phases. The
tree determinant estimate is an established input, not a new
consequence of the charge-increment calculation.

The [explicit source reconstruction](research_physical_normal_lift.md)
connects these facts for one charged edge with real free color.
The period increment determines its double-node values by inverse
Fourier transformation. A final Jacobi recurrence recovers the odd
simple node, and the existing relative normal formula reconstructs
all derivatives with polynomial cost. The resulting map from the
increment vector to all original charge observations has polynomial
operator norm. Its particular closing row can still be exponentially
small on the source; the positive norm theorem supplies an example.

The positivity now extends to an exact boundary problem with a complex
geometric free color. The
[cosine-phase maximum principle](research_geometric_phase_maximum_principle.md)
places every such color in \(\Re w<7/4\) along the positive-path
charge cube. For \(N\ge16\), the ordinary Jacobi inverse has norm
at most \(5\). Its
[Fourier image](research_physical_jacobi_charge_boundary.md)
is coercive in an explicit positive metric of condition number at
most \(N/2\), with the original endpoint forcing. A Ward
representative bounds the first normals by a polynomial in \(N\)
inside subsequent original traces, preserving the mixed derivatives.
This is a positive transport equation; its closing row is still the
original signed observation.

The [Riccati estimate](research_physical_row_riccati_transport.md)
also proves a nonzero local transport factor directly from the
normalized physical solution. Its consecutive ratios contract in a
right half-plane and approach the growing root uniformly, even with
complex free color. The product over an interior row interval has
the original edge-phase difference as exponent, with a factor bounded
above and below independently of \(N\). This establishes the local
coefficient for physical rows. The endpoint normalization also gives
the absolute bound
\[
 N^{-C}e^{N\Re\psi(\tau_j,u)}
 \le |K_N(c_j,-2\cos u)|
 \le N^C e^{N\Re\psi(\tau_j,u)}
\]
on compact physical-row intervals, uniformly over the stated complex
free-color region and for sufficiently large \(N\), after increasing
\(C\) if needed. The
[endpoint extension](research_last_physical_row_riccati.md)
now reaches the last physical row, with logarithmic error and all
fixed free-color derivatives. At odd levels this row is the complete
color. At even levels the
[Chebyshev interpolation argument](research_even_complete_low_kernel.md)
proves that the original low-index complete-end kernel divided by
the last row is \(1+O(N^{-1/2})\). Its alternating weights have
sum one, and the exact row recurrence controls their cancellation.
Thus the low complete-end factors have a nonzero holomorphic
amplitude of polynomial size at both parities. This still does not
estimate their signed trace over the selected colors.
The [bare-kernel parity example](research_even_complete_radical_asymptotic.md)
shows that the restriction to the low sector matters: at an explicit
complex color the full even-level kernel has a strictly larger
exponential rate than its odd-level counterpart. This is a kernel
evaluation before tracing, not a statement about a knot invariant.

This distinction can be tested on the original source itself. The
[central-readout polynomial](research_central_readout_half_plane_zeros.md)
has a zero in the positive Jacobi half-plane at every level and power.
At that zero, the row values remain nonzero and the Jacobi inverses
are bounded by one. Hence those two facts alone cannot force a
positive overlap with the closing row. The zeros have not been
located on the actual geometric locus, so this does not exclude a
more specific lower-bound theorem there.

The [charge characteristic](research_charge_characteristic_two_mode_block.md)
explains a further difficulty with a universal almost-invariance
argument. For every positive power at least three, the geometric mode
belongs to an isolated two-dimensional block in the interior charge
interval. The two moduli cross at charge \(1/2\), and the block
collides with additional modes at the endpoints. Its one-step leakage
is \(O(N^{-1})\), but faster complementary modes prevent summing
that estimate as a relative error. A source-level bound for this
transport and the prescribed scalar observation is still needed.

The geometric domain needed for a central contour comparison is now
known at every actual geometric critical point of a positive path with
powers at least three. The
[wire-order proof](research_positive_path_real_wire_order.md)
keeps that saddle in the original regular factorial chart, using the
coupled period equations. The
[horizontal-concavity proof](research_positive_path_horizontal_concavity.md)
puts the angular saddle inside the rectangle where the reduced phase
is strictly concave. For an internal pair with complete outer ends,
the full mixed phase has a strictly concave central domain as well.
Thus this part of the geometric location problem no longer requires
a separate check for each short pair. The
[pair-angle theorem](research_internal_pair_angle_bound.md)
also places both selected angles below \(\pi/2\) when the outside
ends are complete and the two powers are integers at least three.
The [complete-edge gap](research_internal_pair_complete_edge_gap.md)
sharpens their heights to \(H<107/100\) and proves
\(\Re\psi(t,0)-H>1/500\) throughout this smaller angular box.
The full complete-end kernel therefore has the same nonzero
geometric factor there at both parities. The bare-kernel parity
example lies outside this box.

There is now a source-level local lower bound for **every fixed such
pair**, at both level parities. The
[local Gaussian theorem](research_internal_pair_local_gaussian.md)
uses the actual complete outside kernels, the exact shared-wire
interpolation, and the full double-pole trace factors. The endpoint
recurrence supplies the nonzero normalization. After scaling by
\(N^{-1/2}\) around the geometric point, the density has a positive
limiting norm and relative Gaussian annihilation residual
\(O(N^{-1/2})\), using the sharper normalization in Section 7.
Its local integral has an explicit nonzero coefficient multiplying
\(N^{-3/2}\) at the geometric exponential rate, with a fixed
complex neighborhood in both outside colors.
Its proof first controls the low-index factors, then bounds the
outside radical both locally and after the original traces.
This supplies the proposed
almost-invariance from actual finite equations. The remaining task
is to show that this local piece occurs in the deformation of the
whole source and to control its complementary currents. No global
lower bound for arbitrary short pairs follows from the local result.

The [free-boundary edge theorem](research_pair_free_boundary_kernel.md)
now extends each outside edge factor to a fixed complex neighborhood
of its complete color. It gives the explicit nonzero coefficient
and the full Gaussian expansion of the original finite kernel at
both level parities, including ordinary outside-color derivatives.
Its whole-real-period estimate and quadratic complex-strip bound
also retain ordinary outside normals. These prepare the edge factors
needed for composition. They do not choose the joint two-trace cycle
or bound its entire complement.

The subsequent
[finite contour reduction](research_internal_pair_combined_contour_reduction.md)
makes that complement explicit: one shared-index contour and
two exact folded trace identities give sixteen currents. Its
principal local piece has coefficient one, but another current
could still cancel its leading term. The
[joint endpoint taper](research_internal_pair_endpoint_taper.md)
now proves a strict gap for both shared-index endpoint collars,
including their trace and wire endpoint currents. The middle
interval requires the further comparisons described next.
The [angular-tail transport theorem](research_internal_pair_angular_tail_transport.md)
now removes the omitted original physical trace rows even after
shifting the shared circle to its actual height. Its proof combines
nonnegative coefficients in the exact row recurrence with
\(2\pi\Im x_*<3/4\) and separate half-band Fourier inversion.
This bounds whole original sums; it does not treat a new folded
connector as if it were a removed physical row.

The [grouped connector theorem](research_internal_pair_grouped_angular_connectors.md)
now bounds those folded angular connectors as well, at complete
outside colors. Its exact decomposition pairs each connector with
the entire other trace before applying the estimate. For all fixed
integer powers \(n,p\ge3\), their rate is less than \(2.51\), while
the geometric rate exceeds \(2.52\). This avoids an unsupported
pointwise estimate for a complex internal edge kernel.

Two further comparisons apply within the regular factorial region.
The [joint wire-reflection bound](research_internal_pair_wire_alias_reflection.md)
puts the lower Fourier alias strictly below the paired upper
absolute density. The
[negative-angle bound](research_internal_pair_negative_angle_reflection.md)
compares the negative trace angle to the positive one, with an
explicit exponential loss. These are comparisons of original
densities, not lower bounds for signed integrals. The principal
middle region still needs a global estimate, particularly where
one trace enters the reflected factorial region and the other
remains regular. The
[exact reflection formula](research_internal_pair_reflected_current_identity.md)
retains the moving poles there; their residues are original
physical values and cannot be deleted.

For the remaining finite terms there is also a proved
[first-normal region bound](research_pair_triangular_normal_region.md).
When both selected values vanish below the shared Newton index,
the surviving first derivatives form an explicit signed sum with
positive magnitudes. Monotonicity of those magnitudes bounds the
part with \(j/N\le1/4\) or \(j/N\ge49/100\) strictly below
the geometric rate. It does not bound the intervening band or the
terms where only one selected value vanishes. Those terms still
retain their original phases and possible mutual cancellation.

Those terms can also be regrouped exactly. The
[combined trace theorem](research_trace_normal_defect_positive_form.md)
uses the difference between the true first derivative and the
derivative of the value interpolant. This removes the artificial
triangular boundary without dropping a normal term. Its even-level
crossing matrix is positive definite, with an explicit Fourier
Gram representation; a precisely weighted odd-level subspace is
positive as well. The unrestricted odd endpoint correction remains.

The same theorem gives the exact evolution formula
\(H_{n,N}=\int_0^nU_t^*G_NU_t\,dt\), where \(U_t\) is the
original crossing evolution and \(G_N\) its positive observation
matrix. For the actual source this energy is an integral of
squared ordinary interpolation observations. The original signed
trace is instead the integral of two such observations at
complementary times, without complex conjugation. Thus the Fourier
representation is exact, including the original first normals;
its signed observation still requires an estimate.

This gives a positive observation only for the specified adjoint
cap. The actual knot contraction retains a different, phased
bilinear observation. Moreover, the
[small-eigenvalue theorem](research_pick_form_small_eigenvalues.md)
constructs nonnegative unit vectors on which the even crossing
form is exponentially small for every fixed positive power.
Thus neither positive definiteness nor nonnegative input entries
provides a uniform subexponential lower bound. The next useful
estimate must concern the actual source vector and the actual
closing functional.

That distinction has now been checked on the actual complete-end
source. The [fixed-time observation theorem](research_complete_source_pick_observation.md)
proves that its positive observation energy is exponentially
smaller than its squared physical-value norm, for every fixed
positive crossing horizon at even levels. Its sharper Theorem 2
now determines that smaller rate for every fixed real \(n\ge3\):
the exact alternating observation has a nonzero coefficient
times \(N^{-1}e^{N\mathcal S_n}\), where \(\mathcal S_n\) is
the half-charge leaf action. The positive energy consequently
equals \(C_nN^{-2}e^{2N\Re\mathcal S_n}(1+O(N^{-1}))\), with
an explicit \(C_n>0\). The proof bounds both the original
physical tails and every connecting contour. This is a sharp
lower bound for a specified original observation, rather than
positivity inferred from an absolute-value envelope.
The signed pair still combines these observations without
conjugation, so its coefficient requires a further argument.
The [odd-level observation theorem](research_odd_half_charge_observation.md)
now supplies the corresponding nonzero coefficient using the full
distinct-node interpolant. Its sine contour retains the simple
endpoint at the complete color with the correct ramified residue.
The original odd trace has a separate top-degree term; that term
is computed explicitly and its pair product lies below
\(2M_\infty\). No positive-energy identity for this unweighted
odd observation is inferred from the even Gramian.
The [pair action comparison](research_pair_half_charge_action_gap.md)
now places the color at either vertex of every fixed positive
pair \(n,p\ge3\) strictly outside this observation contour.
It also proves a strict action gap between the direct term
and the interpolation correction. The proof uses the original
logarithmic periods and bounds for \(n+i\sec(t/2)\), rather
than numerical comparisons of individual pairs. Together with
the exact complex-color residue formula, this determines which
term dominates the actual first-normal interpolation defect near
the geometric point, now at both level parities.
Away from that neighborhood both terms
must still be retained.

The [physical-color theorem](research_physical_normal_defect_packet.md)
now gives a uniform, nonzero leading coefficient for the actual
interpolation derivative defect at every physical color. Its
[boundary version](research_free_boundary_half_charge_observation.md)
includes a fixed complex outside-color neighborhood, all ordinary
outside derivatives, and decay on the whole real outside period.
These results provide more than a norm bound, but the relative
\(O(N^{-1})\) error still cannot be inserted into an exponentially
ill-conditioned closing transform without further control.
The same defect estimate now holds on a fixed complex neighborhood
of every retained real interval away from color \(2\). This permits
Cauchy estimates for the whole reduced trace, with an explicit
logarithmic potential in the exponent. It still does not justify
exchanging a fixed-order asymptotic expansion with a divided
difference whose order grows with the level.

There is nevertheless a useful absolute estimate after that
transform. The [outer-index theorem](research_real_pair_geometry_and_tail_gap.md)
proves that, for every fixed positive integer pair \(n,p\ge3\),
the shared indices outside \(1/50<j/N<12/25\) have a fixed
exponential gap below the pair's geometric rate. At even levels
the [remaining sum has an exact Fourier representation](research_pair_regular_support_cells.md).
Its decomposition into cells retains explicit shared boundary
terms. One individual term already has an absolute-integral rate
larger than the full rate for \((3,3)\); its cancellation with the
other terms must be used. This is a limitation of a termwise
absolute estimate for the actual source, not merely a hypothetical
counterexample constructed from unrelated coefficients.
The exact block formulas in Section 7 of that note retain the
correction either as a support-projected kernel with its Cauchy
diagonal, or as omitted original first-normal rows. The latter
replacement is valid after taking wire residues; it is not a
pointwise identity that deletes an interpolation contribution.

The [crossing-overlap calculation](research_complete_source_crossing_overlap.md)
also proves, at both parities,
\[
 \frac{\langle F_N,U_{t,N}F_N\rangle}{\|F_N\|^2}
       \longrightarrow(1-it/2)^{-1/2}.
\]
Thus this source is not almost invariant under a fixed nonzero
crossing, even up to scalar phase. A step of size \(1/N\) has
relative defect \(\sqrt3/(4N)+o(N^{-1})\), but its \(N\)-fold
iterate has a positive limiting defect. The geometric Gaussian
almost-invariance above is a statement after removing the phase
and rescaling, with a different operator.

There is also an exact positive expression for certain original
three-crossing chains. The
[positive spectral-moment theorem](research_positive_three_crossing_cycle.md)
conjugates the original transfer matrix \(JM^3\) to
\(\kappa H\), where \(H=M^*M>0\) and \(|\kappa|=1\).
A cyclic contraction is \(\kappa^m\operatorname{Tr}(H^m)\),
and the specified original capped word \((3,\ldots,3,2)\)
is \(\kappa^{m-1}\langle e_0,H^m e_0\rangle\).
The latter has nonnegative spectral weights and genuine exponential
lower bounds for every fixed length. A general two-boundary chain
instead has two different transformed boundary vectors, so this
positivity statement does not extend to its closing coefficient.
The capped source's sharp geometric rate remains to be identified.

The [fourth-moment lower bound](research_positive_fourth_cap_observation.md)
now estimates one specified coefficient of \(H^2e_0\) directly.
Its exact finite sum has a real stationary point and a unique maximum
of the absolute summand; the original complex phase is retained.
Writing \(\mu_m=\langle e_0,H^me_0\rangle\), this proves
\(\mu_4\ge c_4N e^{wN}\), where \(w\simeq1.504207135\)
and the strict bound \(w>3/2\) is certified by rational
enclosures. Positive-moment log-convexity consequently gives, for
every fixed \(m\ge4\),
\[
 \mu_m\ge c_m N^{3-m/2}
     \exp\!\left(N\bigl[(m-3)w-(m-4)v\bigr]\right),
 \qquad v\simeq0.906072448.
\]
This improves the earlier lower bound for every such length.
It is a lower bound for the actual cap, not a sharp asymptotic
for the fourth moment or a new identification with volume.

The [third-moment calculation](research_positive_three_crossing_cap_seed.md)
now links this positive source to a previously proved Fourier
profile: \(\langle e_0,H^3e_0\rangle=\|MJM^3e_0\|^2\).
Its sharp asymptotic strengthens the lower bounds for every longer
fixed capped chain. It also shows that the actual state
\(He_0/\|He_0\|\) has exponentially small weight in every fixed
upper spectral window of \(H/\|H\|\); its expectation of
\(I-H/\|H\|\) tends to one. The available spectral gap therefore
does not make this original cap almost invariant.
For matching caps whose norm and next-crossing norm are already
controlled, the
[positive transport estimate](research_positive_three_crossing_cycle.md#6-transporting-independently-proved-source-norms-through-positive-blocks)
instead gives the direct lower bound
\(f^*H^m f\ge\|Mf\|^{2m}/\|f\|^{2m-2}\).
This has an explicit original closing word and requires no
unproved preparation of a leading eigenvector.

The [finite cap recursion](research_positive_cap_fourier_recursion.md)
gives an exact Fourier evolution for these positive moments,
including both polynomial projections and their endpoint terms.
It also replaces \(H^re_0\) by
\([(M-M^T)^*(M-M^T)]^re_0\) with exponentially small relative
error for each fixed \(r\ge2\). This supplies a positive operator
and a controlled original input. The recurrence still contains a
complex convolution before taking the positive weighted norm; its
sharp lower bound has not been proved for arbitrary fixed length.

This note makes the distinction explicit and records what
an almost-invariance argument would have to establish. Section 8
records the separate contour proofs for two distinct short pieces:
the pendant pair of powers \(3,3\), with one remaining boundary,
and the internal pair, with two remaining boundaries. Both now
have nonzero original geometric packets and whole outside-period
bounds. General short-partial-filling stability and finite exclusions
remain open.

The [Gaussian observation criterion](research_shifted_gaussian_observation.md)
states a possible general lower-bound argument after shifting the
exact Fourier contour. A small relative residual for the Gaussian
annihilation operator forces a nonzero Gaussian component, and the
bilinear overlap of the two limiting Gaussians is explicitly nonzero.
This standard inequality still needs independent exponential norm
bounds and control of the complementary cycle. For the internal
\(3,3\) pair these inputs follow from the proved packet; deriving
them from the quantum recurrence for general short components
remains a separate task.

The [one-crossing calculation](research_one_crossing_gaussian_window.md)
now supplies an actual positive operator with a uniform spectral gap.
After explicit phase changes, centering, and division by its exponential
growth, the original crossing converges in Hilbert--Schmidt norm to a
Gaussian integral operator. Its squared singular values form a geometric
sequence with ratio \((5-\sqrt{21})/2\). This proves a nonzero lower bound
for an explicitly prepared Gaussian input. It does not prepare the
original cap: that cap has exponentially small projection onto the top
right singular vector. Thus the gap is available in this local model,
but the required almost-invariance of the original transported state is
not a consequence of it.

The [exact Gaussian frame](research_gaussian_frame_newton_transport.md)
retains the original cap and closing row, and writes every finite word
as an integral of its crossing kernels. Its positive resolution of the
identity gives a precise setting for attempting that transport. It does
not make the crossing kernels nonnegative or change the closing
bilinear pairing into a norm.

Taking the trace at each vertex does not automatically repair this
problem. The [three-crossing vertex calculation](research_traced_three_vertex_endpoint.md)
finds an endpoint term whose local rate is larger than the geometric
vertex action, while its next exact Fourier contraction is bounded.
Thus a lower-bound argument must retain cancellation between
neighboring factors. The
[polynomial cap chart](research_polynomial_cap_chart_and_product_closure.md)
does preserve the original boundary vector through the step \(JM\),
but its additional clock factor for \(M\) prevents an immediate
transport of that vector through an arbitrary word.

There is now an exact test of the suggested positivity shortcut:
[Section 5 of the frame note](research_gaussian_frame_newton_transport.md#5-diagonal-weights-cannot-make-the-original-gram-matrix-nonnegative)
proves that no positive diagonal weights and phase changes make
the original crossing's Gram matrix entrywise nonnegative.
This does not exclude a non-diagonal positive form or a controlled
local approximation. For an independent adjoint trial in the
forced quantum equation, the
[endpoint estimate](research_complete_boundary_coefficient_transport.md#a-boundary-condition-for-an-independent-adjoint-trial)
gives a separate necessary condition: a norm lower bound above
the contour's cap rate requires exponentially accurate cancellation
in an explicit boundary row, in addition to a small bulk residual.

There is now also a uniform path result. The
[original-trace assembly](research_uniform_path_trace_assembly.md)
proves a nonzero contribution for every fixed circle-tree path
with signed crossing powers of magnitude at least sixty-four.
Its local lower bound is the nonzero complex Gaussian integral
in equations (16) and (25) there. The exact Fourier contour has
coefficient one at this point, and bounds for all remaining
parts of the original trace prevent its cancellation.
This does not require the raw real-source phases to be nearly
constant. It still leaves general connected short pieces open.

An exact coefficient formulation is available in the
[one-sided Hermite note](research_one_sided_hermite_projection.md).
It expresses the whole original source as one central coefficient
of a finite polynomial, with all double-root normals retained.
This coefficient is also an explicitly normalized value at zero.
The lower-bound problem concerns this specified coefficient;
neither the change of representative nor positivity of an
auxiliary norm controls it automatically.

There is now an exact simplification of the problematic high-index
sector. The [radical contraction theorem](research_high_newton_radical_contraction.md)
groups it into physical-color sums with polynomially bounded
weights, retaining all shared edges. Its weight matrix is positive
definite, but its least eigenvalue is exponentially small, and
the original crossing phases remain. This supplies useful upper
control before a lower-bound argument; it does not provide a
uniform gap. Section 6 of the one-sided Hermite note gives an
actual terminal source whose Hardy norm is exponentially large
while its closing evaluation has size \(2/N^2\).

Discrete Parseval also gives an actual uniform estimate here.
[Section 7 of the radical note](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials)
proves that every radical Newton polynomial, expressed in the
angular variable, has Fourier coefficient norm at most
\(\sqrt{N-1}\). The proof uses its exact physical values and
first normals. It bounds the entire radical over the real period
and gives the explicit growth allowed on a complex strip.

For the internal pair of powers \(3,3\), the
[strict sector comparison](research_radical_path_sector_gap.md)
now puts the entire contracted radical below the geometric rate.
The [midpoint-forcing estimate](research_bare_kernel_power_three_obstruction.md#6-the-midpoint-forcing-after-the-original-internal-pair-trace)
does the same for the exact cutoff current, at both level parities.
These are upper bounds on two potential competing contributions.
The [full internal-pair theorem](research_internal_pair_three_full_boundary_packet.md)
now proves the nonzero coefficient of the whole source by a separate
exact circle argument. The sector bounds alone did not supply it.

The same geometric gap now holds for every real pair \(n,p\ge3\)
with complete outside boundaries. An
[exact interpolation of the crossing powers](research_real_power_source_transport.md)
preserves the original values and first normals, so both error
estimates remain uniform on the compact square \([3,64]^2\).
The interpolation does not transport the geometric coefficient
by itself: its derivative contains an uncontrolled bulk term.

There is a more direct finite Fourier formulation at the complete
boundary. The [coefficient transport note](research_complete_boundary_coefficient_transport.md)
writes the same-sign pair as
\(\sum_j w_{n,j}^2=N\int_0^1W_{n,N}(x)^2\,dx\).
Reversing one crossing power gives the positive expression
\(\sum_j|w_{n,j}|^2\), a different source.
The actual vector \(w_n\) is uniquely determined by an exact
forced recurrence and a specified last coefficient. At power
three this recurrence has four successive shifts. For that power,
the mixed-source contour theorem supplies a nonzero packet near
the selected complex wire point and controls the whole complementary
circle. A comparable connection theorem for arbitrary short powers
is not supplied by the recurrence.

The positive opposite-power norm cannot simply replace the same-sign
source at exponential scale. Section 7 of the coefficient note
proves, for every sufficiently large fixed integer \(n\),
\[
 \frac{|P_{n,n,N}(0,0)|}{P_{n,-n,N}(0,0)}
   =C_n e^{-N\Delta_n}(1+O(N^{-1})),\qquad
 \Delta_n=\frac{16\pi^3}{n^6}+O(n^{-7})>0.
\]
Here the arguments \(0,0\) are angular boundary coordinates.
Both sources already have nonzero geometric asymptotics in this
range. Their different rates therefore disprove an unqualified
subexponential phase-coherence bound in the original coefficient
norm. A pairing-preserving change of coordinates that makes those
coefficients coherent must have exponentially growing condition
number. The proved internal \(3,3\) packet instead uses a complex
contour with its actual exponential weights and a controlled
complement; it does not assert coherence in the raw coefficient norm.

Sections 10--11 give quantitative phase criteria and test them
against the settled pendant pair. The test matters: its raw absolute sum
has a strictly larger exponential rate than its signed sum.
Consequently a lower bound asserting that the raw phases are
nearly constant would be false. The positive-norm approach in
Section 2 remains a different possibility, because it uses the
norm of the actual complete-color Fourier vector.

The obstruction also survives the internal summations that
produce the original Newton coefficients. The
[local phase criterion](research_three_crossing_real_period_newton_bound.md#7-the-local-phase-can-force-cancellation-in-the-newton-coefficients)
proves this from the nonreal boundary derivative of the
geometric action. In the specified peripheral basis that
derivative records the real part of the cusp parameter.

## 1. Which lower bounds have actually been proved?

The following statements concern different objects.

| Object | Proved lower-bound mechanism | Scope |
|---|---|---|
| A genuinely positive finite partition | Retain a positive summand near a maximizing admissible state | Only the specified positive model and its proved identifications |
| The original reflected source \(\phi_N(R^{-2k}T(R^{2k}))\) | Exact equality with \(\|M^{2k}\mathbf e_0\|^2\), followed by the nonzero original endpoint mode and a summand near the action maximum | The reflected family and its stated fixed insertions |
| The original long-twist sources | A nonzero Gaussian coefficient on a proved contributing contour, with a strict bound on all remaining currents and charges | The hypotheses of the corresponding composition theorem |
| The original traces with the specified small-charge Chebyshev insertions | Explicit nonzero Gaussian coefficient; all other charges, vertical currents, and removed rows have strict bounds | Every fixed graph carrying the specified edge kernels, with no isolated selected vertex, and arbitrary fixed signed integer powers (including zero), for charges in \([1/4000,1/2000]\); continuation to the unmodified source at charge one is open |
| The pendant \(3,3\) source | A nonzero complex Gaussian with exact coefficient \(+1\), after bounds on all horizontal and boundary currents | One free boundary, with its proved whole-period bound |
| The internal \(3,3\) source | Exact full-period circle averaging of two mixed packets; one nonzero shared Gaussian and a strict bound on the whole complementary circle | Two free boundaries, both level parities, all fixed boundary derivatives and the proved angular/strip bound; also the mirrored \(-3,-3\) block |
| The original capped word \((3,\ldots,3,2)\) | Exact positive spectral moment \(\langle e_0,(M^*M)^m e_0\rangle\); proved second and third moments, the fourth-moment coefficient bound, and log-convexity give exponential lower bounds | Every fixed number of these blocks, with the stated cap; the sharp rate has not been identified with the knot-complement volume |
| Three-crossing chains between matching original caps | The positive form \(f^*H^m f\), bounded below by independently established norms of \(f\) and \(Mf\) | Explicit original closing words, including the actual input \(M^2e_0\); different caps require the additional overlap estimate (30) of the positive-cycle note |
| One physical color assignment on a filled tree | A nonzero normal determinant, bounded above and below by powers of \(N\) relative to the positive kernel product | Powers of one sign and \(\operatorname{diag}(|n_v|)-\operatorname{Adj}(G)>0\); this does not bound the sum over assignments |
| An original physical edge row with complex free color | Contracting exact Riccati ratios, normalized at \(F_0=1\), give the absolute geometric rate and a polynomial lower factor; the endpoint barrier reaches the last row | Bounded \(\Re w\le2-\gamma\), including the last physical row at both parities; no signed trace over rows is estimated |
| The low-index complete-end kernel | At odd levels it is the last physical row; at even levels exact alternating Chebyshev interpolation gives a ratio \(1+O(N^{-1/2})\) to that row | Nonzero holomorphic factor of polynomial size on compact subsets of \(\Re w<2\); the full even-level off-grid kernel also has a radical sector |
| The local mixed contour at any fixed internal pair \(n,p\ge3\) | The actual edge normalization and factorial expansion give a positive rescaled norm, relative oscillator residual \(O(N^{-1/2})\), and an explicit nonzero \(N^{-3/2}\) coefficient | Both level parities, a fixed complex neighborhood in both outside colors, and all fixed ordinary normals; occurrence in the whole source cycle and the remaining complementary bounds are open |
| The cyclic three-crossing network | Exact positive trace \(\operatorname{Tr}((M^*M)^m)\), with a trace-norm Gaussian operator limit | A sharp rate for the specified network; no identification with an arbitrary original knot closure |
| A shared positive Fourier comparison partition \(Z_N\) | No general lower bound for the original signed source follows; weighted Cauchy gives \(|K_N|^2\le \operatorname{poly}(N)Z_N\) | An upper comparison only |

The reflected statements are proved in the
[sharp growth theorem](research_even_run_sharp_reflected_growth.md)
and the [original knot-volume theorem](research_reflected_even_kashaev_volume_theorem.md).
The sign and direction of the last comparison are given explicitly
in the [shared positive Fourier partition](actual_matching_graph_positive_fourier_partition.md).
A positive term in that latter partition is not necessarily a
positive term of the invariant.

For example, a signed sum \(a-a\) vanishes even though its positive
square sum is \(2|a|^2\). Replacing this example by a Fourier transform
does not change the issue: the transform preserves the actual norm,
not the norm obtained by discarding the phases before summing.

## 2. The actual complete-color Fourier state

Fix one zero-framed knot and a braid presentation with \(b\) strands.
At level \(N\), put \(Q=e^{2\pi i/N}\). Let \(K_N\) be its original
reduced complete-color invariant and let \(C_j\), \(1\le j<N\),
be its original reduced ordinary-color values at this same root.
Define
\[
 c_0=K_N,\qquad c_j=C_j,\qquad
 \widehat c_k=\frac1{\sqrt N}\sum_{j=0}^{N-1}Q^{-kj}c_j,\qquad
 u_N=\frac1{\sqrt N}(1,\ldots,1).
 \tag{1}
\]
All norms below are the ordinary Euclidean norms of these finite
vectors. The [ordinary-color proof](ordinary_color_plancherel_bound_audit.md)
establishes, without a volume theorem as a premise,
\[
 |C_j|\le
 \left(\frac{\sin(\pi j/N)}{\sin(\pi/N)}\right)^{b-1}.
 \tag{2}
\]
It uses the positive path trace for the ordinary colors, the literal
colored crossing matrices, and the one-component quotient argument.
It does not extend that positive representation to the complete
color, whose quantum dimension is zero.

Finite character orthogonality gives the exact decomposition
\[
 \widehat c=K_Nu_N+e_N,\qquad e_N\perp u_N,\qquad
 \|e_N\|^2=R_N:=\sum_{j=1}^{N-1}|C_j|^2.
 \tag{3}
\]
In particular
\[
 \|\widehat c\|^2=|K_N|^2+R_N,\qquad
 0\le R_N\le (N-1)(N/2)^{2b-2}.
 \tag{4}
\]
The fixed presentation makes the last bound polynomial in \(N\).

Thus, for a positive target volume \(V\), an independently proved
lower bound
\[
 \|\widehat c\|^2\ge \exp\{NV/\pi-o(N)\}
 \tag{5}
\]
would imply
\[
 |K_N|^2=\|\widehat c\|^2-R_N
       \ge \exp\{NV/\pi-o(N)\}.
 \tag{6}
\]
Indeed the polynomial divided by the lower bound in (5) tends to
zero exponentially. Eventual nonvanishing follows; it is not a
premise. A matching upper bound would give the volume limit.
Equation (5) is the missing estimate for this positive-energy route.
The upper comparison in Section 1 does not prove it.

Even a single actual Fourier coefficient would suffice. Since
\(|(e_N)_k|\le\sqrt{R_N}\), (3) gives
\[
 |K_N|\ge
 \sqrt N\bigl(|\widehat c_k|-\sqrt{R_N}\bigr).
 \tag{7}
\]
An exponential lower bound for one specified \(\widehat c_k\)
would survive the polynomial subtraction. Such a bound has not
been proved uniformly for arbitrary connected short pieces.
Section 8 describes the specified adjacent pair settled by the
separate contour argument.

## 3. Almost-invariance already present, and the relevant scale

Let \(S\) be the cyclic shift \((Sf)_k=f_{k+1\bmod N}\), and let
\(P=u_Nu_N^*\). The shift \(S\) is unitary and \(Pu_N=u_N\).
Equation (3) gives, uniformly over all integers \(r\),
\[
 \|S^r\widehat c-\widehat c\|
     \le2\sqrt{R_N}.
 \tag{8}
\]
This is a polynomial bound on the absolute defect. If (5) were
known, the defect divided by \(\|\widehat c\|\) would be
exponentially small. It is therefore unnecessary to postulate
almost-invariance of this state: the ordinary-color estimate
already supplies the absolute bound. The unresolved issue is its
large norm.

For an arbitrary vector \(v\), the exact cyclic Poincaré inequality is
\[
 \|(I-P)v\|^2
   \le\frac{\|(S-I)v\|^2}{4\sin^2(\pi/N)}.
 \tag{9}
\]
To prove it, expand in the orthonormal characters \(N^{-1/2}Q^{jk}\).
The squared eigenvalues of \(S-I\) are \(4\sin^2(\pi j/N)\);
the least nonzero one occurs at \(j=1,N-1\).
This is the gap-normalized version of the
[existing cyclic-current contraction](actual_fourier_source_cancellation.md).

The dependence on \(N\) matters. The unit vector
\(v_k=N^{-1/2}Q^k\) is exactly orthogonal to \(u_N\), although
\(\|Sv-v\|=2\sin(\pi/N)\to0\).
Qualitative almost-invariance under one generator therefore does
not imply a nonzero constant coefficient. To obtain that conclusion
from (9), the defect must be smaller than the square root of the
gap, in proportion to \(\|v\|\).

Averaging the entire cyclic group has a different normalization:
\[
 \frac1N\sum_{r=0}^{N-1}\|S^rv-v\|^2
          =2\bigl(\|v\|^2-\|Pv\|^2\bigr).
 \tag{10}
\]
This follows by expanding the squares and using
\(N^{-1}\sum_rS^r=P\). It has no small gap, but controls all
translations, rather than only one small step.

## 4. The representation-theoretic implication

Here is the precise finite-dimensional statement. Let \(U_s\) be
unitary operators and let \(\chi_s\) be unit complex numbers. Set
\[
 \Delta_\chi=\sum_s(U_s-\chi_sI)^*(U_s-\chi_sI),\qquad
 F_\chi=\bigcap_s\ker(U_s-\chi_sI),
 \tag{11}
\]
and let \(P_\chi\) be orthogonal projection onto \(F_\chi\).
If a positive number \(\gamma_N\) satisfies
\(\Delta_\chi\ge\gamma_N(I-P_\chi)\), then
\[
 \|(I-P_\chi)v\|^2
 \le\gamma_N^{-1}\sum_s\|U_sv-\chi_sv\|^2.
 \tag{12}
\]
This is immediate by taking the quadratic form of the assumed
operator inequality. If \(F_\chi=\mathbb Cz\), \(\|z\|=1\), it gives
\[
 |\langle z,v\rangle|^2\ge
 \|v\|^2-\gamma_N^{-1}\sum_s\|U_sv-\chi_sv\|^2.
 \tag{13}
\]
For a different observation vector \(w\), a further overlap is
needed. Writing \(r=(I-P_\chi)v\), the triangle inequality gives
\[
 |\langle w,v\rangle|
 \ge |\langle w,z\rangle|
       \sqrt{\|v\|^2-\|r\|^2}
       -\|(I-P_\chi)w\|\,\|r\|.
 \tag{14}
\]
Consequently a gap, a sufficiently small relative defect, and a
nonvanishing observed overlap are separate requirements. If the
character space has dimension greater than one, a small defect
alone does not even select a line inside it.

There is also an independent scale requirement. Equations
(12)--(14) are homogeneous in \(v\); they do not prove that its
norm grows exponentially. For example, in the rank-one case,
if \(\sum_s\|U_sv-\chi_sv\|^2\le(1-\delta_N)\gamma_N\|v\|^2\),
then (13) gives
\(|\langle z,v\rangle|\ge\sqrt{\delta_N}\|v\|\).
This transfers a known norm rate when
\(\delta_N\ge e^{-o(N)}\). It neither establishes that rate nor
replaces the overlap condition for a different observation.
For the actual state in Section 2, the observed line and absolute
shift-defect bound are already known; the independent exponential
norm lower bound (5) is still the missing general input.

This is the usual quantitative setting of almost-invariant-vector
arguments; see Bekka, de la Harpe and Valette,
[Kazhdan's Property (T), Chapter 1](https://www.cambridge.org/core/books/abs/kazhdans-property-t/definitions-first-consequences-and-basic-examples/21A0D7F3B446FB0607DA14F1479F7394).
Equations (12)--(14) have been proved here directly. No property
(T), uniform gap, or positive unitarization of the full quantum
source is being assumed.

In fact, exact positive unitarization of the original crossing is
impossible at every \(N\ge2\). This is already proved in the
[original operator note, Section 1](research_original_almost_invariance_and_observation.md).
At each double physical root
\(c_a=2\cos((2a+1)\pi/N)\), \(0\le a<\lfloor N/2\rfloor\),
the local algebra is \(\mathbb C[\epsilon]/(\epsilon^2)\), and
multiplication by the crossing is
\[
 R(c_a)I+R'(c_a)\epsilon,\qquad
 \frac{R'(c_a)}{R(c_a)}
   =\frac{i(N-1-2a)}{4\sin((2a+1)\pi/N)}\ne0.
\]
Here \(\epsilon\) denotes the nonzero square-zero multiplication
operator. Thus there is a nontrivial Jordan block, already at
\(a=0\) for every \(N\ge2\). If \(M^*HM=H\) for \(H>0\), then
\(H^{1/2}MH^{-1/2}\) would be unitary and diagonalizable, a
contradiction. The exact identity \(M^*JM=J\) instead preserves
the indefinite reversal form. Positive unitarity of the different
ordinary-color representations therefore does not extend to this
full physical source with its normal directions. This does not
exclude approximate estimates or new source-adapted operators and
gauges; their scaling and observed coefficient must still be kept.

For the finite clock and shift, their nontrivial commutator is a
further distinction. If \(SX=QXS\), \(Q\ne1\), they have no common
nonzero character vector: applying the relation to a supposed
common eigenvector gives \((1-Q)\chi_S\chi_Xv=0\).
Approximate common eigenvectors as \(Q\to1\) are possible. They
describe localized states, not an exact invariant subspace.
A lower bound based on them must specify an isolated approximate
state and its overlap with the actual observation.

## 5. A positive envelope gives a different, direct lower bound

Positivity can be used quantitatively even when the original
coefficients are not themselves positive. Suppose, in \(\mathbb C^N\),
that \(v=D(ag+r)\), where \(D\) is a specified unitary diagonal
phase, \(a\ne0\), \(g\ne0\) has nonnegative real entries, and
\(\|r\|\le\varepsilon |a|\|g\|\). The specified unit test vector
\(t=D(1,\ldots,1)/\sqrt N\) then satisfies
\[
 |\langle t,v\rangle|\ge
 |a|\|g\|
 \left(\frac{\|g\|_1}{\sqrt N\|g\|_2}-\varepsilon\right).
 \tag{15}
\]
Indeed the positive contribution is \(a\sum_jg_j/\sqrt N\),
and the error in this coefficient is at most \(\|r\|\).
Since \(\|g\|_1\ge\|g\|_2\), even the bound
\(\varepsilon=o(N^{-1/2})\) suffices for a polynomially
nonvanishing overlap. A more spread-out positive envelope gives a
stronger bound. This argument proves a particular coefficient
lower bound; it does not infer it from almost-invariance.

The [three-crossing Fourier theorem](research_three_crossing_fourier_packet.md)
establishes this situation for the actual column
\(\alpha=M^3\mathbf e_0\), with
\[
 g_j=S_j^2,\quad D_{jj}=q^{j(j+2)},\quad
 a=\kappa^3\omega_NN^{-1/2},\quad \varepsilon=O(N^{-1}).
\]
Here \(S_j\) is the original sine factorial and \(\omega_N\)
is the explicitly retained unit phase in that theorem.
The positive envelope is concentrated in a window of width
\(\sqrt N\) about \(j=5N/6\). For its normalized dechirped
original vector \(v_N\), the theorem proves
\[
 \|Sv_N-v_N\|
   =\sqrt{\pi\sqrt3/N}+O(N^{-1}),\qquad
 |\widehat v_N(0)|
   \sim (2/\sqrt3)^{1/4}N^{-1/4}.
 \tag{16}
\]
The inverse convention for the cyclic shift in that theorem gives
the same residual norm. Its full Gaussian Fourier window is also
proved. Thus there is an actual source of almost-invariance and
a proved nonzero Fourier overlap in this example.

This is a different vector from the complete-color state in (1).
Its specified Fourier coefficient is not \(K_N\). The literal turn
reflects and shifts its Fourier window by one. The next dense
crossing has since been treated: the
[next-column theorem](research_three_crossing_next_crossing_fourier.md)
proves its full real coefficient growth and a second Gaussian
Fourier window, and the
[complex-column theorem](research_three_crossing_complex_next_step.md)
proves its actual complex continuation near the remaining saddle.
The final original closing row is still a different test vector
from the one in (15).

## 6. An adjoint estimate must also see the original forcing

There is also a useful adjoint formulation for the
[exact pair equation](research_three_crossing_boundary_current.md)
\(\mathcal A_Nf=b_N\).
For every trial vector \(v\),
\[
 \|f\|\ge\frac{|\langle v,b_N\rangle|}
                    {\|\mathcal A_N^*v\|}
 \tag{17}
\]
whenever the denominator is nonzero. This is Cauchy--Schwarz
applied to \(\langle v,b_N\rangle
=\langle\mathcal A_N^*v,f\rangle\).
An exponentially accurate adjoint approximate nullvector would
give an exponential lower bound only if it has a quantitatively
nonzero overlap with the original forcing.

For a specified linear observation \(\langle a,f\rangle\), an
approximate adjoint solution instead gives
\[
 |\langle a,f\rangle|
 \ge|\langle v,b_N\rangle|
       -\|\mathcal A_N^*v-a\|\,\|f\|.
 \tag{18}
\]
Thus the useful next construction is tied to the original source
and its marked observation. The geometric characteristic curve
alone supplies neither the required residual bound nor the
forcing overlap. These estimates remain open for the general
short-pair source.

The [original operator and observation calculation](research_original_almost_invariance_and_observation.md)
shows that this qualification occurs inside our actual matrices.
For \(T=C-qX\), the explicit factorial vector \(h\) satisfies
\(Th=q^{-1}e_0\). The unit vector \(Jh/\|h\|\) has an exponentially
small adjoint residual, but its overlap with forcing at \(e_{N-1}\)
is exactly as small. The equation \(Tx=e_{N-1}\) consequently has
the norm-one solution \(q^{-1}e_{N-1}\).
The same note gives a Hermitian formulation of the adjacent-pair
equation; its form is indefinite. The complete free-boundary
polynomial is a matrix element of its inverse with the specified
boundary-dependent observation. Its simple top-coefficient cap is
already polynomially bounded and is different from the full
boundary evaluation at \(-2\). The latter is now controlled for
this pendant source by the contour theorem in Section 8.
Neither operator reformulation supplies that lower bound
automatically, or a lower bound for arbitrary short sources.

## 7. A positive almost-invariant vector can have a zero Fourier coefficient

An exact elementary example separates the two issues. For an integer
\(d\ge2\), put
\[
 v_j=\frac{\binom{d-1}{j}}{\sqrt{\binom{2d-2}{d-1}}},
 \qquad 0\le j<d .
 \tag{19}
\]
Every entry is positive and Vandermonde's identity gives \(\|v\|_2=1\).
For the cyclic shift on these \(d\) entries,
\[
 \|Sv-v\|_2^2
    =\frac2d-\frac{2}{\binom{2d-2}{d-1}}=O(d^{-1}).
 \tag{20}
\]
Indeed the sum of the noncyclic adjacent products before normalization
is \(\binom{2d-2}{d-2}\); the cyclic endpoint product adds \(1\).
The ratio of that binomial coefficient to
\(\binom{2d-2}{d-1}\) is \((d-1)/d\), proving (20).

Nevertheless the exact unitary Fourier transform is
\[
 \widehat v(k)=
 \frac{(1+e^{-2\pi i k/d})^{d-1}}
      {\sqrt{d\binom{2d-2}{d-1}}}.
 \tag{21}
\]
This follows directly from the binomial theorem. In particular
\[
 \frac{|\widehat v(k)|}{|\widehat v(0)|}
        =|\cos(\pi k/d)|^{d-1}.
 \tag{22}
\]
The constant coefficient has size
\(\pi^{1/4}d^{-1/4}(1+o(1))\), by Stirling's formula.
For even \(d\), the coefficient at \(k=d/2\) is exactly zero.
For \(k/d\) tending to any fixed number in \((0,1)\) other than
\(1/2\), the ratio in (22) is exponentially small.

Thus positivity supplies a lower bound when the observation sums
the coefficients with a common phase. It does not supply a lower
bound after an arbitrary character is inserted. This example has
the same \(d^{-1/2}\) shift-defect scale and \(d^{-1/4}\) constant
Fourier-coefficient scale as a normalized Gaussian window. Knowing
those two scales alone cannot determine a different prescribed
Fourier coefficient.

## 8. The proved pendant and internal short-pair coefficients

### One free boundary: the pendant pair

For the adjacent three-crossing piece, the exact observation is
\[
 F_N(w)=\sum_j\ell_{N,j}(w)\gamma_{N,j},\qquad
 \ell_N(w)=\mathbf e(w)^TJM^2,\qquad
 \gamma_N=MJM^3e_0 .
 \tag{23}
\]
Both factors are fixed by the original finite matrices. Fourier
orthogonality rewrites (23) as
\(\sum_k\widehat\ell_N(-k)\widehat\gamma_N(k)\);
it does not insert a complex conjugate.
The proved nonzero Fourier window of \(\gamma_N\) must therefore be
paired with this particular \(\ell_N\); it is not itself the desired
observation.

The current source reduction is stronger than a formal stationary
calculation. The
[whole preparation-error estimate](research_three_crossing_global_preparation_error.md)
shows that replacing the original column by its explicit factorial
preparation changes (23) by a term of exponential rate less than
\(3/2\). Its Section 6 also removes the outer real color ranges
with a rate strictly below \(153/100\).
The
[geometric action calculation](research_three_crossing_action_volume_calibration.md)
proves that the selected stationary rate is the actual partial
exterior volume divided by \(2\pi\), and this rate exceeds
\(153/100\).

The [full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
now proves how much of the local Gaussian integral occurs in the
original sum. The exact cellwise residue identity gives its
coefficient \(+1\); seven horizontal bounds and all 144 boundary
inequalities put every complementary term below it. The resulting
asymptotic is
\[
 F_N(-2\cos u)=\kappa^2\omega_N C(u)e^{NW(u)}(1+O(N^{-1})),
 \qquad C(u)\ne0 ,
\]
on a fixed complex neighborhood of zero, including every integer
level and all fixed ordinary boundary derivatives.
This proves the required local observation. It uses the phase
information in the exact finite sum, rather than turning the
bilinear Fourier pairing into a positive norm.

A representation-theoretic argument would be useful if it supplied
the quantitative observation estimate (14) or (18) for these
actual vectors and their forcing. Its normalization matters.
If the product \(\|\ell_N\|_2\|\gamma_N\|_2\) has a rate larger
than the geometric rate, an exponentially small normalized overlap
can be the correct answer. A subexponential overlap loss is
sufficient only after a normalization whose rate is already the
desired geometric one.

The [dual-row calculation](research_three_crossing_dual_closing_row.md)
now gives the exact backward recurrence of \(\ell_N(w)\), with
its endpoint value, value forcing, and ordinary derivative forcing.
It also identifies a difficulty with extending the existing
single-mode proof: at the middle color, the normalized frozen
recurrence has two dominant conjugate roots of equal modulus.
Their relative coefficient must be controlled. This supplies a
specific representation problem to solve, rather than an assumed
almost-invariance property of the closing row.

For the local volume limit, this asymptotic is stronger than necessary.
In particular it proves
\[
 |F_N(-2)|\ge
   \exp\{N\operatorname{Vol}(M_{3,3})/(2\pi)-o(N)\}
 \tag{24}
\]
together with the matching upper bound, along every integer level.
This concerns the original free-boundary source at its complete
value. The separate
[whole-period theorem](research_three_crossing_whole_period_source.md)
proves the upper gap needed on the rest of the real boundary period.
Together these results give the
[long-closing theorem](research_three_crossing_long_closing_fiber.md):
with the two original negative fillings fixed at \(2,2\), every
sufficiently long signed final filling satisfies the original
Kashaev volume conjecture. The conclusion covers all but finitely
many integers in that specified remaining filling parameter.
It does not establish the conjecture for arbitrary connected short
regions or cofinite coverage on an arbitrary fixed template.

### Two free boundaries: the internal pair

The internal pair has selected degrees \((2,2)\) and three original
edges; it is a different source from (23). In the notation of the
[coefficient-transport note](research_complete_boundary_coefficient_transport.md),
\[
 \mathcal P_N(u,v)
   =w_3(-2\cos u)^{\mathsf T}w_3(-2\cos v)
   =N\int_{iY}^{1+iY}W_{3,N}(x,u)W_{3,N}(x,v)\,dx .
\]
This identity holds exactly in both ordinary boundary polynomials
and retains all original physical first normals. The products
have frequencies in \([-(N-1),N-1]\), so no internal alias or
endpoint correction is dropped.

The [mixed packet](research_internal_pair_three_mixed_packet.md)
is \(W_{3,N}=C_{N,3}N^{-1}Ae^{NS}(1+O(N^{-1}))\), with
\(A\ne0\), at the actual selected point
\(x_*\approx0.1871617+0.0908106i\).
The proof first controls the original outer-wire tails and
trace endpoint currents. On the shifted circle it bounds all
nineteen central contour surfaces and the left, right and high
complements. Each complementary contribution lies strictly below
the selected rate. These are bounds on the whole exact source,
not just a comparison of critical values.

The [full two-boundary theorem](research_internal_pair_three_full_boundary_packet.md)
therefore gives
\[
 \mathcal P_N(u,v)=C_{N,3}^{\,2}N^{-3/2}
       \mathcal A(u,v)e^{N\mathcal S(u,v)}(1+O(N^{-1})),
 \qquad \mathcal A(u,v)\ne0.
\]
Here \(C_{N,3}=e^{3\pi i(N-1)^2/(4N)}\), and at zero
\[
 \mathcal A(0,0)
   =\sqrt{\frac{\pi}{-S_{xx}(x_*,0)}}A(x_*,0)^2,\qquad
 M_{\rm pair}=\Re\mathcal S(0,0)
   =\frac{\operatorname{Vol}Y_{3,3}}{2\pi}.
\]
Thus the concrete lower bound used is
\[
 |\mathcal P_N(0,0)|
       \ge cN^{-3/2}e^{NM_{\rm pair}}
\]
for all sufficiently large integer \(N\). The nonzero Gaussian
amplitude supplies \(c>0\); the global complement estimates
prevent cancellation of that term. The result includes both
parities, fixed ordinary boundary derivatives, and the mirrored
\((-3,-3)\) source.

For composition, the same theorem also proves, on a fixed strip,
\[
 |\mathcal P_N(u+is,v+it)|
 \le CN^a e^{N\{M_{\rm pair}
     -c_1(1-\cos u)-c_1(1-\cos v)+B(s^2+t^2)\}} .
\]
The angular loss is retained from the outside factorial factors;
strictly smaller finite error terms absorb their complex-strip
cost. This is additional information beyond a scalar lower bound.

The positive norm \(w_3^*w_3\) is instead the opposite-power source.
Neither its sharp rate nor a subexponential lower bound on
\(|w_3^{\mathsf T}w_3|/\|w_3\|^2\) is a premise or conclusion here.
The complex-contour proof is compatible with the actual long-power
coherence obstruction above. It settles this fixed two-boundary
block, not arbitrary connected short fillings or the full
finite-exception goal.

## 9. A local source asymptotic and a small coefficient norm do not suffice

There is an elementary counterexample to an automatic whole-period
principle for arbitrary canonical polynomials. It does not come
from a fixed knot or tangle. Its purpose is to show that a
nonzero local asymptotic, strict local curvature, and the norm
condition \(M>U+c\) do not alone control the rest of the period.

Use the original Newton basis \(e_j(w)\), multiplication matrix
\(C\), and constants
\[
 b_2=\frac{2G}{\pi},\qquad c=2J(5/6),\qquad M=\frac9{20}.
 \tag{25}
\]
They satisfy \(\|C\|_2\le6\), \(29/50<b_2<3/5\), and \(c<1/3\).
For every sufficiently large integer \(N\), put
\[
 k_N=\lfloor N/4\rfloor,\quad d_N=N/4-k_N,\quad
 m_N=\lfloor N/100\rfloor,\quad K_N=\lceil\log N\rceil,
 \]
and define the ordinary polynomial
\[
\begin{split}
 P_N(w)&=\sum_{\ell=0}^{K_N}(-1)^\ell
          \binom{d_N}{\ell}\left(\frac{w+2}{2}\right)^\ell,\\
 f_N(w)&=N e_{k_N}(w)
       \left[e^{N(M-b_2)}P_N(w)
                  +\left(\frac{w+2}{4}\right)^{m_N}\right].
\end{split} \tag{26}
\]
Here \(d_N\in\{0,1/4,1/2,3/4\}\), and the logarithm in \(K_N\)
is natural. The degree is less than \(N\), so this is an
ordinary canonical polynomial without a quotient reduction.

**Proposition.** Write \(f_N(w)=\mathbf e(w)^Tv_N\). This
all-integer-level family has the following properties:

1. \(\|v_N\|_2\le\operatorname{poly}(N)e^{NU}\), with
   \(U=(\log2)/100\), and \(M>U+c\).
2. On a fixed complex disk about \(w=-2\),
   \[
   f_N(w)=2^{-1/2}e^{NW(w)}(1+O(N^{-1})),
   \qquad W(-2)=M ,
   \tag{27}
   \]
   with a nonzero amplitude, a holomorphic relative error,
   and all its fixed derivatives controlled. In angular
   coordinates, \(\frac{d^2}{du^2}W(-2\cos u)|_{u=0}
   =-1/(2\pi)<0\).
3. At the fixed real angle \(u=1/2\),
   \[
   \liminf_{N\to\infty}N^{-1}
           \log|f_N(-2\cos(1/2))|>\frac{13}{25}>M .
   \tag{28}
   \]

Thus even an upper bound with rate \(M\) on the whole real
period fails for this family.

**Proof.** Multiplication by \((w+2)/4\) acts on coefficients
by \((C+2I)/4\), of norm at most two. Multiplication by
\((w+2)/2\) has norm at most four. Also
\(|\binom d\ell|\le1\) for \(0\le d<1\).
The Taylor polynomial \(P_N(C)\) consequently has norm at
most a fixed polynomial in \(N\), since its degree is
\(\lceil\log N\rceil\). The first term of (26) has coefficient
norm at most
\(\operatorname{poly}(N)e^{N(M-b_2)}\), and the second has
norm at most \(N2^{m_N}\). This proves the first assertion.
Indeed \(U<7/1000\) and \(c<1/3\), whose sum is less than
\(9/20\). All intermediate polynomial degrees remain below
\(N\), so the multiplication estimates introduce no
quotient artifact.

Let \(b(y,u)\) be the canonical Newton phase and
\(w=-2\cos u\). Its fixed-color expansion at
\(y=k_N/N=1/4-d_N/N\) gives
\[
 e_{k_N}(w)=\frac{e^{Nb(1/4,u)}}{\sqrt2\,N}
       (-w/2)^{-d_N}(1+O(N^{-1})).
 \tag{29}
\]
This uses \(b_y(1/4,u)=\operatorname{Log}(-w/2)\), with
the logarithm zero at \(w=-2\). The expansion is uniform
and holomorphic on a fixed sufficiently small complex disk.
The polynomial \(P_N\) is the Taylor truncation of
\((-w/2)^{d_N}\). On any disk
\(|(w+2)/2|\le r<e^{-2}\), its error is \(O(N^{-2})\),
by a geometric tail bound. Its multiplication therefore
removes the entire rounding factor in (29).

On the smaller fixed disk \(|w+2|\le4e^{-20}\), the
second bracket term in (26), divided by the first, is
at most
\[
 O\!\left(e^{N(b_2-M)-20m_N}\right)
                                      =O(e^{-N/20}).
 \]
The Taylor factor is bounded away from zero there.
Equation (27) follows with
\(W(w)=b(1/4,u)-b_2+M\). Evenness in \(u\) makes this a
holomorphic function of \(w\). Its angular second
derivative is the stated \(-1/(2\pi)\). Cauchy's formula
on smaller fixed disks gives the derivative assertion.

It remains to check the larger off-center value. Put
\(w_*=-2\cos(1/2)\). Then \(e_{k_N}(w_*)>0\).
For \(0<d<1\), every nonconstant coefficient of
\((1-t)^d\) is negative. Its Taylor partial sum is
therefore at least \((1-t)^d>0\) when \(0<t<1\).
This also holds for \(d=0\). Thus \(P_N(w_*)>0\), and
both bracket terms in (26) are positive. Consequently
\[
 f_N(w_*)\ge
  N e_{k_N}(w_*)\left(\sin^2(1/4)\right)^{m_N}.
 \tag{30}
\]

The real Newton entropy satisfies
\[
 V_{1/2}(1/4)>\frac{11}{20}.
 \]
Here is a direct bound requiring no numerical quadrature.
For \(0\le u\le1/2\),
\[
 -\partial_u V_u(1/4)
   =\frac{\operatorname{arctanh}(\tan(u/2))}{\pi}
   \le\frac{496u}{897\pi}.
 \]
Use \(\tan(u/2)\le16u/31\) and
\(\operatorname{arctanh}t\le t/(1-t^2)\).
After integration, the loss from \(b_2\) is at most
\(62/(897\pi)<62/2691\). The lower bound \(b_2>29/50\)
then proves the displayed inequality. That lower bound
already follows from the first six terms of Catalan's
alternating series and \(\pi<22/7\).

Finally \(\sin(1/4)\ge95/384\), so
\(\sin^2(1/4)>1/18>e^{-3}\); the last inequality follows
from the first six terms of the series for \(e^3\).
Taking lower exponential rates in (30) yields
\(11/20-3/100=13/25\), with strict inequalities.
This proves (28). \(\square\)

The same counterexample can have purely cyclotomic coefficients.
Replace \(e^{N(M-b_2)}\) in (26) by \((7/8)^N\) and set
\(M=b_2+\log(7/8)\). Then
\[
 \frac{29}{50}-\frac17<M<\frac35-\frac18<\frac{13}{25},
 \]
and the lower bound still exceeds \(U+c\).
The local error estimate is unchanged, since
\(\log(8/7)<1/7<3/20\). Every Taylor coefficient in
\(P_N\) is rational, and the original Newton basis and
multiplication matrix have coefficients in the cyclotomic
field. Thus algebraicity of the finite coefficients does
not eliminate this example.

The construction uses an \(N\)-dependent insertion and is
not a counterexample to any theorem about a fixed tangle.
It excludes only a deduction from the local asymptotic
and coefficient norm alone. A general argument for the
original tangle sources needs further structure, such as
control of their complete coefficient phases or of the
new complex boundary currents.

## 10. A quantitative criterion using the actual phases

There is a direct version of the almost-invariance argument for
an actual finite closing sum. Write its nonzero summands as
\[
 Z_N=\sum_{k\in\Omega_N}w_{N,k}u_{N,k},\qquad
 w_{N,k}>0,\quad |u_{N,k}|=1,\qquad
 W_N=\sum_k w_{N,k},\quad p_{N,k}=w_{N,k}/W_N.                 \tag{31}
\]
Here the weights are the absolute values of the original summands,
and \(u_{N,k}\) are their actual phases, including the prescribed
observation. They are not phases chosen to make the sum positive.
A common unit scalar is harmless; an index-dependent rephasing
changes the observation unless it is transferred to that row.

Let \(B_N\subseteq\Omega_N\) be a connected lattice window carrying
mass \(1-\varepsilon_N\). Give its conditional probability
\(\pi_N=p_N(\,\cdot\,|B_N)\) the nearest-neighbor Dirichlet form
\[
 \mathcal E_{\pi_N}(f)=
 \sum_{\{k,l\}\text{ a lattice edge in }B_N}
       \min(\pi_{N,k},\pi_{N,l})\,|f_l-f_k|^2.                 \tag{32}
\]
Each unoriented edge is counted once. Suppose its Poincaré gap
\(\lambda_N>0\) means
\(\operatorname{Var}_{\pi_N}f\le
 \mathcal E_{\pi_N}(f)/\lambda_N\). Set
\[
 d_N=\frac{\mathcal E_{\pi_N}(u_N)}{\lambda_N}.
\]
If \(d_N<1\), then the exact finite sum satisfies
\[
 \boxed{\quad
 |Z_N|\ge W_N\left[
       (1-\varepsilon_N)\sqrt{1-d_N}-\varepsilon_N\right].
 \quad}                                                       \tag{33}
\]
The right side is useful when its bracket is positive.

To prove (33), the conditional mean \(m_N=\sum_{B_N}\pi_{N,k}u_{N,k}\)
satisfies
\(\operatorname{Var}_{\pi_N}u_N=1-|m_N|^2\).
Poincaré therefore gives \(|m_N|\ge\sqrt{1-d_N}\).
The entire complementary sum has modulus at most
\(\varepsilon_NW_N\). This proves the claim without an
assumption on its phase or sign.

The relevant gap is of order \(N^{-1}\) on a window of width
\(\sqrt N\), instead of the order \(N^{-2}\) gap of the full
cyclic color set. Here is one explicit sufficient bound. Suppose
\(B_N\) is a rectangular \(d\)-dimensional lattice box, each side
has at most \(L\sqrt N\) sites, and
\[
             \frac{\max_{B_N}\pi_N}{\min_{B_N}\pi_N}\le K       \tag{34}
\]
with fixed \(L,K\). Then
\[
                         \lambda_N\ge\frac4{K L^2N}.           \tag{35}
\]
Indeed the uniform Neumann path with \(m\) sites has gap
\(4\sin^2(\pi/(2m))\); products have the least of their coordinate
gaps. The comparison of its variance and conductances with
\(\pi_N\) costs at most \(K\). Finally
\(\sin(\pi/(2m))\ge1/m\). Coordinates with one site can simply
be omitted.

If the actual phase chords on edges in direction \(i\) obey
\[
            |u_{N,k+e_i}-u_{N,k}|\le\ell_i/\sqrt N,            \tag{36}
\]
then the total conductance in each direction is at most one,
so
\[
 d_N\le\frac{K L^2}{4}\sum_{i=1}^d\ell_i^2.                    \tag{37}
\]
This gives a quantitative, checkable coherence condition. A uniform
pointwise Gaussian absolute-weight profile on a fixed rescaled window
supplies (34); its tail supplies \(\varepsilon_N\).
The constants in (37), not merely the notation
\(O(N^{-1/2})\), decide whether this particular bound proves
nonvanishing. No uniform spectral gap or positive unitarization
of the original crossing matrix is being assumed.

For the standard variance/Dirichlet-form characterization of the
gap and comparison of reversible chains, see Levin and Peres,
with contributions by Wilmer,
[Markov Chains and Mixing Times, second edition, Sections 13.2--13.3](https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf).
The finite inequalities above were proved directly with the
normalizations used here.

There is a stronger criterion when the actual phase has a controlled
quadratic limit. Let \(s=(k-k_N)/\sqrt N\), and suppose the probability
law of \(s\) under \(p_N\) converges to the centered Gaussian with
positive covariance \(\Sigma\). Suppose, for a common unit scalar
\(e^{i\theta_N}\), that the actual phases satisfy
\[
 e^{-i\theta_N}u_{N,k}\longrightarrow
       \exp\{i(b^Ts+\tfrac12s^TCs)\}                            \tag{38}
\]
uniformly on every bounded rescaled window, where \(b\) is real
and \(C\) is real symmetric. Tightness and the modulus-one bound
control the complement of those windows. Therefore
\[
 \frac{e^{-i\theta_N}Z_N}{W_N}\longrightarrow
 \mathcal C=
 \det(I-i\Sigma C)^{-1/2}
  \exp\!\left\{-\frac12b^T(\Sigma^{-1}-iC)^{-1}b\right\}
                  \ne0.                                     \tag{39}
\]
The square-root branch continues from \(C=0\).
This follows by integrating the limiting Gaussian; its real
quadratic part is strictly positive. For explicit constants, put
\(A=\Sigma^{1/2}C\Sigma^{1/2}\). If
\(\|A\|\le T\) and \(b^T\Sigma b\le B^2\), then
\[
                  |\mathcal C|
        \ge(1+T^2)^{-d/4}e^{-B^2/2}.                          \tag{40}
\]
Indeed \(\Re(I-iA)^{-1}=(I+A^2)^{-1}\le I\), and the determinant
modulus is \(\det(I+A^2)^{-1/4}\).
The error can be made explicit on a bounded rescaled window.
Suppose the phase approximation there has error at most
\(\delta_N\), the probability outside it is at most \(\eta_N\),
and the expectation of the limiting quadratic exponential
under the rescaled discrete law differs from its Gaussian
expectation by at most \(\rho_N\). Then the error in (39)
is at most \(\delta_N+2\eta_N+\rho_N\). If this is smaller
than half the right side of (40), it gives an explicit
finite-level lower bound.
For a fixed tangle composition the dimension \(d\) is fixed
before the level tends to infinity. A small but nonzero
constant in (40) therefore does not alter its volume rate.
This observation does not provide uniform estimates when
the number of tangles grows with the level.

This Gaussian criterion permits bounded linear and quadratic
phase variation across the entire \(\sqrt N\) window. For a
smooth phase of the form \(e^{iN\vartheta(k/N)}\), with the
corresponding controlled Taylor remainder, (38) requires its
center gradient modulo \(2\pi\mathbb Z^d\) to be of order
\(N^{-1/2}\); its rescaled limit is \(b\). A fixed nontrivial frequency cannot
be removed by choosing a new test vector and then treating its
coefficient as the original closing coefficient.

## 11. The raw adjacent triple has exponentially small mean phase

For the prepared original pair, let \(a_{N,i,j,k}\) denote the
complete summands in equation (4) of
[the exact prepared formula](research_three_crossing_prepared_boundary_sum.md),
evaluated at \(w=-2\), including its common prefactor. Define
\[
 Z_N^0=F_N^0(-2)=\sum_{i,j,k}a_{N,i,j,k},\qquad
 W_N^{\rm abs}=\sum_{i,j,k}|a_{N,i,j,k}|.                       \tag{41}
\]
This is the literal positive absolute partition of that exact
sum. The proved source theorem implies
\[
 \limsup_{N\to\infty}\frac1N
       \log\frac{|Z_N^0|}{W_N^{\rm abs}}
       \le M-\frac{11G}{2\pi}<-\frac3{50},                    \tag{42}
\]
where \(M=\Re W(0)\) is the geometric action of the full pair.
Thus its actual mean phase is exponentially small.

Here is an all-integer-level proof. Choose
\[
       j_N=\lfloor N/2\rfloor,\qquad
       i_N=k_N=\lfloor N/4\rfloor .
\]
For every sufficiently large \(N\) these are admitted original
indices: \(i_N+j_N<N\), \(k_N\le j_N\), and
\(e_{i_N}(-2)>0\) at both parities. Their normalized point tends
to \((x,y,z)=(1/2,1/4,1/4)\), strictly inside every factorial
strip used in this summand. In particular no simple-root zero
or normal term is substituted for a nonzero value.
The exact scalar \(A_N\) has only polynomial size, and the uniform
factorial expansion gives
\[
 \begin{split}
 \log|a_{N,i_N,j_N,k_N}|
  &=N\{\mathcal J(3/4)-10\mathcal J(1/4)\}+O(\log N)\\
  &=N\frac{11G}{2\pi}+O(\log N).
 \end{split}                                                  \tag{43}
\]
The rounding is \(O(N^{-1})\) on a regular compact bulk set and
therefore changes the exponent by only \(O(1)\).
Retaining this one positive absolute summand proves the lower
bound for \(W_N^{\rm abs}\).

The [full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
gives rate \(M\) for \(F_N(-2)\) with nonzero amplitude. The
[whole preparation-error estimate](research_three_crossing_global_preparation_error.md)
has rate less than \(3/2<M\). Consequently its prepared main
\(Z_N^0\) has the same rate and is bounded above by
\(\operatorname{poly}(N)e^{NM}\). The
[outward action certificate](../repro/results/research-three-crossing-closing-action.json)
gives \(M<77/50\). Also \(11G/(2\pi)>8/5\): for example,
the first ten terms of Catalan's alternating series give
\(G>32/35\), and \(\pi<22/7\). Combining these strict
inequalities with (43) proves (42).
The negative pair is coefficient conjugate and has the identical
absolute partition and mean-phase modulus.

The actual phase increments show directly why a coherent real
Gaussian window is the wrong target here. On every nonzero
summand at \(w=-2\), all factorials and the Newton value are
positive. Apart from a common phase, its leading phase is
\[
 \vartheta(x,y,z)=\frac\pi2
        \{(x-y)^2-x+y+2xz+2z^2\}.
 \tag{44}
\]
The exact finite differences of the phase are
\[
 \begin{split}
 \Delta_j\arg a_N&=\pi(x-y+z-\tfrac12)+\pi/N,\\
 \Delta_i\arg a_N&=\pi(-x+y+\tfrac12),\\
 \Delta_k\arg a_N&=\pi(x+2z)+\pi/N
                      \pmod {2\pi}.
 \end{split}                                                  \tag{45}
\]
There is no strict real point of \(x,y>0,\ x+y<1,\ 0<z<x\)
where all three limiting increments are zero modulo \(2\pi\).
Indeed the second belongs to \((-\pi/2,3\pi/2)\), so if it
vanishes modulo \(2\pi\) then \(x=y+1/2\). The first then
equals \(\pi z\in(0,\pi)\), which cannot vanish modulo \(2\pi\).
Thus any regular real Gaussian window has a nontrivial phase
frequency in at least one direction. Its actual phase energy is
not of the small size required by (33)--(37), and it does not
satisfy (38). More fundamentally, (42) rules out a
subexponential lower bound for the mean phase of the full raw
absolute partition, independently of how its concentration is
proved.

This distinction also retains fixed ordinary boundary normals.
For real \(w=-2\), every factor \(c_a-w\) is nonnegative, so
\((-1)^r e_i^{(r)}(-2)\ge0\) for every fixed derivative order
\(r\). At the rounded low index in (43), its magnitude differs
from \(e_i(-2)\) by polynomial factors and is bounded below by
\(r!\binom{i}{r}4^{-r}e_i(-2)\). Thus the corresponding absolute
derivative partition still has rate at least \(11G/(2\pi)\).
The holomorphic source theorem and preparation-error theorem
bound the differentiated coherent sum by a polynomial times
\(e^{NM}\), using Cauchy on a radius of order \(N^{-1}\).
The same exponential mean-phase obstruction therefore remains.

Equations (33) and (39) are useful when their phase hypotheses
hold for the original observation. They do not hold at the raw
absolute rate of this pair. Its proved geometric contribution
comes from the specified complex contour and its retained
currents, not from near constancy of the raw real-lattice phases.

## 12. A local norm law must include the change of volume

The positive Fourier energy in (4) cannot be preserved up to
subexponential loss by every original tangle operation. There
is an exact example among the reflected rational knots already
treated here. Fix \(k\ge2\) and put
\[
 \mathcal K_k=C\bigl(R^{-2k}T(R^{2k})\bigr),\qquad
 V_k=\operatorname{Vol}(S^3\setminus\mathcal K_k)>0 .
 \tag{46}
\]
The [reflected theorem](research_reflected_even_kashaev_volume_theorem.md)
proves
\[
 |K_N(\mathcal K_k)|=\|M^{2k}e_0\|_2^2,\qquad
 \lim_{N\to\infty}N^{-1}\log
       \|\widehat c(\mathcal K_k)\|_2^2=V_k/\pi .
 \tag{47}
\]
The second assertion follows from the first, its proved
volume limit, and the polynomial ordinary-color remainder
in (4).

Now insert the fixed crossing block \(R^{2k}\) immediately
outside \(R^{-2k}\). The two blocks cancel exactly. The
remaining closure is \(C(T(R^{2k}))\), an unknot with
removable curls. Its zero-framed value is one at every
color, so its Fourier energy is exactly \(N\). Consequently
this original operation has energy ratio
\[
 \frac{\|\widehat c(C(T(R^{2k})))\|_2^2}
      {\|\widehat c(\mathcal K_k)\|_2^2}
        =\exp\{-NV_k/\pi+o(N)\}.
 \tag{48}
\]
At complete color the finite algebra also checks the
unknot value directly:
\(\phi_N(T(R^{2k}))=(M^{2k}e_0)_0=\kappa_N^{2k}\);
the scalar is the removable framing phase.

This is the expected loss when the hyperbolic knot is
untwisted to an unknot. It is not a counterexample to a
bound for geometrically admissible compositions, or to a
bound that includes the change of volume. Such a bound
would compare the states after their specified exponential
volume factors have been removed. Equation (48) explains
why a lower-norm law that ignores that factor is too strong.

## 13. The sharp error threshold for an original turn

A weighted analytic model must control errors below the loss in the
selected action. This requirement can be made sharp without replacing
the original turn by an integral operator. Write
\(\mathcal Q_{b,N}f=T(R^bf)\), with fixed signed integer \(b\), and use
the complete physical Hermite norm
\[
 \|f\|_{\mathcal J,N}=
 \max\bigl(\{|f(c)|,|f'(c)|:c\text{ is a double root of }P_N\}
       \cup\{|f(-2)|:N\text{ is odd}\}\bigr).
 \tag{49}
\]
The simple odd root has no derivative condition. All elements are
canonical polynomials of degree less than \(N\), and multiplication
is in the full original quotient. For each fixed \(r\ge0\), equip the
output with the ordinary \(C^r([-2,2])\) norm, including order zero.
Then
\[
 \lim_{N\to\infty}\frac1N\log
   \|\mathcal Q_{b,N}\|_{\mathcal J,N\to C^r([-2,2])}
       =M_\infty=\frac{4G}{\pi}.
 \tag{50}
\]
The same limit holds if the output is only evaluation at \(-2\).

To prove the upper bound, use the exact identity
\(\mathcal Q_bf(u)=\phi_N(R^bfK_N(\cdot,u))\).
The [finite Hermite estimates](../papers/circle-tree-volume/finite-bounds.tex)
give polynomial costs for multiplication by fixed \(R^b\) and for
\(\phi_N\), while the full kernel and its required first normals
have rate at most \(M_\infty\), uniformly on the real boundary.
Fixed output derivatives cost only powers of \(N\) by the polynomial
Markov inequality. Thus the upper bound is
\(C_{b,r}N^{a_{b,r}}e^{NM_\infty}\).
For the lower bound, take \(f=R^{q-b}\) with any fixed \(q\ge32\).
Its norm (49) is polynomial in \(N\), whereas
\(\mathcal Q_bf=H_{q,N}\) has a nonzero complete-boundary packet of
rate \(M_q\). The [terminal theorem](research_terminal_large_fixed_powers.md)
proves \(M_q\to M_\infty\). First take the lower limit in \(N\)
for each fixed \(q\), then let \(q\to\infty\). This proves (50)
through both level parities, with all first normals retained.

Suppose a model input \(F_N^0\) has a proved nonzero turned packet
of rate \(S\), the reference input rate is \(M\), and put
\(\Delta=M+M_\infty-S\). If the actual input error satisfies
\[
 \|F_N-F_N^0\|_{\mathcal J,N}
       \le C N^a e^{N(M-\delta)},\qquad \delta>\Delta,
 \tag{51}
\]
then (50)'s upper bound makes its turned error exponentially smaller
than \(e^{NS}\), with gap \(\delta-\Delta\). The strict margin also
preserves the full packet on a sufficiently small complex boundary
disk: finite-degree Bernstein bounds add an arbitrarily small
exponential cost as that disk shrinks. Cauchy then retains every
fixed ordinary boundary derivative. This is an error-transport
criterion for an already proved model contribution, not a proof that
the model's geometric saddle belongs to the original cycle.

The threshold cannot be weakened universally. Indeed, let \(F_N\)
have a concentrated holomorphic input packet of rate \(M\), with
phase \(W\) and nonzero amplitude, and let
\(P_N^\mathrm{out}=\mathcal Q_bF_N\) have a proved nonzero packet
at \(-2\) of rate \(S<M+M_\infty\). Choose fixed \(q\ge32\) with
\(M_q>S-M\). For all sufficiently large \(N\), set
\[
 c_N=\frac{P_N^\mathrm{out}(-2)}{H_{q,N}(-2)},\qquad
 \widetilde F_N=F_N-c_NR^{q-b},\qquad
 \delta_q=M+M_q-S>0.
 \tag{52}
\]
The denominator is eventually nonzero. Finitely many earlier levels
can be defined separately. These exact original-algebra identities give
\[
 (\mathcal Q_b\widetilde F_N)(-2)=0,\qquad
 \|c_NR^{q-b}\|_{\mathcal J,N}
       \le\operatorname{poly}(N)e^{N(M-\delta_q)}.
 \tag{53}
\]
Moreover \(\delta_q\to\Delta\) as \(q\to\infty\). Thus, for
every proposed error exponent \(\delta<\Delta\), a correction obeying
that error bound can cancel the original observation exactly.

This correction preserves the complete local asymptotic packet of
the input on a smaller fixed disk, including every already established
inverse-power term. Indeed the exact
[Hermite Fourier coefficients of a crossing](research_polynomial_crossing_fourier_trace.md)
give
\( |R^{q-b}(-2\cos(x+iy))|\le C_qN e^{N|y|}\).
Shrink the disk until \(|y|<\delta_q/8\) and
\(\Re W(t)>M-\delta_q/8\); the correction is then relatively
exponentially small. It also satisfies a weakened full Gaussian strip
bound with input rate \(M\): use
\(|y|\le\delta_q/2+y^2/(2\delta_q)\) and choose the angular loss
coefficient at most \(\delta_q/8\). Consequently an identical local
phase and amplitude, even with the same selected positive geometric
gluing, and the existence of some whole-period Gaussian bound do not
force a nonzero short-turn observation.

The sequence (52) is an engineered linear combination in the original
algebra, not a claim about a single fixed tangle. It does not contradict
a theorem controlling the actual source on a prescribed complex domain
reaching the charged saddle. It shows what that stronger weighted
space must exclude: errors which are locally invisible but exceed the
global threshold (51). Exact Gaussian residue formulas still retain
the endpoint currents and all Hermite charges; a local phase alone
does not estimate those terms.

The starting hypothesis is nonvacuous for every fixed \(b\): take
\(F_N=\operatorname{can}(R^{a-b}H_{2,N})\) with fixed sufficiently
large \(a\). Boundary multiplication preserves its input packet, and
the [large-power turn theorem](research_uniform_large_power_turn.md)
proves the output \(T(R^aH_{2,N})\), including its strict positive
action loss \(\Delta\). Only the correcting linear combination in
(52), not this starting input or its selected gluing, is engineered.

## 14. What the exact clock and shift equations determine

The all-color Fourier vector in Section 2 and the Fourier array
obtained by opening two strands are different states. Their
constant coefficients both recover the invariant with their
specified normalizations, but their other coefficients need
not satisfy the same estimates.

For the all-color vector, define
\[
 (Sv)_k=v_{k+1\bmod N},\qquad (Xv)_k=Q^kv_k,\qquad
 D=\frac{S-I}{Q-1},\qquad P=u_Nu_N^* .
 \tag{54}
\]
Then \(SX=QXS\). On the nonconstant Fourier modes,
\(D\) has inverse \(h\) with multipliers
\((Q-1)/(Q^{-j}-1)\), \(1\le j<N\). Each multiplier
has modulus at most one. Extend \(h\) by zero on
the constant line. Thus
\[
 hD=Dh=I-P,\qquad \|h\|\le1,\qquad
 D\widehat c=g_N,\qquad
 \widehat c=h g_N+K_Nu_N .
 \tag{55}
\]
Here \(g_N\) depends only on the ordinary colors:
its \(j\)-th Fourier coefficient is
\((Q^{-j}-1)C_j/(Q-1)\), while its constant coefficient
is zero. In particular
\(\|g_N\|\le\sqrt{R_N}/\sin(\pi/N)\), a polynomial
bound. The cyclic forcing equation determines the
orthogonal remainder exactly; its homogeneous constant
coefficient is the unknown invariant.

The clock orbit does give complete observation, in the
following precise sense:
\[
 \sum_{r=0}^{N-1}X^{-r}PX^r=I,\qquad
 \langle u_N,X^r\widehat c\rangle=c_r .
 \tag{56}
\]
Indeed the vectors \(X^{-r}u_N\) form an orthonormal
basis. This recovers all the color observations together,
not a lower bound for the one at \(r=0\).
Adding the formal clock transform of (55) provides no
new bounded source, since the exact identity is
\[
                    DX=X(QD+I).
 \tag{57}
\]
Its right side contains the original unknown state itself.

The actual all-color vector also cannot be a state
approximately fixed by both this clock and this shift
when its norm is exponentially large. For any
\(r\not\equiv0\pmod N\) and any \(|\chi|=1\), (3) gives
\[
 \left|\,
   \|(X^r-\chi I)\widehat c\|-\sqrt2\,|K_N|
                         \,\right|\le2\sqrt{R_N}.
 \tag{58}
\]
To prove it, use \(u_N\perp X^ru_N\) for the leading
term and \(\|X^r-\chi I\|\le2\) for the remainder.
If \(\|\widehat c\|\) has a positive exponential rate,
(4) makes \(|K_N|/\|\widehat c\|\to1\), and the
relative defect in (58) tends to \(\sqrt2\), uniformly
in \(r\) and \(\chi\). The shift defect, by contrast,
is polynomially bounded by (8).

The exact Weyl system therefore supplies full observation and a
controlled inverse on the nonconstant modes, but does not determine
the homogeneous complete coefficient. The local packet obstruction
in [Section 13](#13-the-sharp-error-threshold-for-an-original-turn)
also shows why a selected geometric germ alone cannot replace that
missing source information. A volume-weighted composition estimate
must retain the actual forcing, closing row, and error threshold.

## 15. The exact finite system for changing a Fourier charge

The positive fractional-charge geometry provides a critical point for
every real charge in a cube. To use that cube as a quantum continuation,
one must also specify a finite source at each charge. There are two
different finite objects: individual Fourier coefficients, and the
original Hermite observations with all their aliases. The following
identities keep that distinction explicit.

Fix one selected variable, with any other variables treated as
spectators. Put \(D=N-1\), \(\eta=(-1)^D\), and
\[
 \tau_a=\pi(D-2a)/N,\qquad
 q_N(w)=\mathcal R_{n,N}(w)f_N(w),\quad
 Q_N(t)=q_N(-2\cos t),\qquad
 g_N(t)=\sin t\,Q_N(t)=\sum_m b_{m,N}e^{imt}.
 \tag{59}
\]
Here \(\mathcal R_{n,N}\) is the canonical polynomial representative of the
original signed crossing power in
\(\mathbb C[w]/(2T_N(w/2)+2)\). The spectator \(f_N\) is the
actual product of incident kernels and attached sources before
this variable is traced. It may have degree larger than \(D\).
Thus \(Q_N\) is an even trigonometric polynomial, \(g_N\) is odd,
and the sum in (59) is finite. In particular \(b_{-m,N}=-b_{m,N}\)
and \(b_{0,N}=0\). No Gaussian representative has replaced the
canonical crossing away from its physical jets.

For an integer \(k\), define two finite observations:
\[
 \begin{split}
 V_k&=\sum_{a=0}^{N-1}e^{-ik\tau_a}g_N(\tau_a),\\
 D_k&=\sum_{a=0}^{N-1}e^{-ik\tau_a}
                   \bigl(g_N'(\tau_a)-ikg_N(\tau_a)\bigr).
 \end{split}
 \tag{60}
\]
The symbol \(D_k\) here denotes a scalar observation, not the
dimension parameter \(D\). The original trace is
\(\phi_N(q_N)=\eta D_0\), by the full derivative-sampling identity.
All formulas also hold for spectator-polynomial coefficients.

**Exact charge identities.** At every level and every integer \(k\),
\[
 \begin{split}
 V_k&=N\sum_{\ell\in\mathbb Z}\eta^\ell b_{k+\ell N,N},\\
 D_k&=iN^2\sum_{\ell\in\mathbb Z}
                              \ell\eta^\ell b_{k+\ell N,N},\\
 V_{k+N}&=\eta V_k,\qquad
 D_{k+N}=\eta(D_k-iNV_k),\\
 D_{k+2N}-2\eta D_{k+N}+D_k&=0.
 \end{split}
 \tag{61}
\]
The sums are finite. To prove them, use
\(\sum_a e^{ir\tau_a}=0\) unless \(r\) is divisible by \(N\),
in which case the sum is \(N\eta^{r/N}\).
The derivative in (60) contributes \(i(m-k)\) at frequency \(m\).
Alternatively, the last two lines follow directly from
\(e^{-iN\tau_a}=\eta\). This proves the finite equations,
including their normal terms and endpoints.

Oddness gives \(V_{-k}=-V_k\) and \(D_{-k}=D_k\). Therefore
these are genuine original polynomial insertions:
\[
 \boxed{\quad
 \phi_N\!\left(q_N(w)\,T_k(-w/2)\right)=\eta D_k,
 \qquad V_0=0,\qquad D_N=\eta D_0 .
 \quad}
 \tag{62}
\]
Indeed \(T_k(\cos t)=\cos(kt)\), and the derivative trace
of \(g_N(t)\cos(kt)\) is \((D_k+D_{-k})/2\).
The endpoint identity also follows from
\(T_N(-w/2)=\eta\) in the original quotient.
Thus the insertion at \(k=N\) returns, up to the stated sign,
the original trace. It is not a known complete bare-edge
observation from which that trace can be inferred.

The finite transport itself has a controlled norm. Use the angular
Hermite space
\[
 \mathscr H_N=\mathbb C[\zeta,\zeta^{-1}]
                    /(\zeta^N-\eta)^2,\qquad \zeta=e^{-it},
 \quad
 \|F\|_{\mathrm{jet},N}^2
   =\frac1N\sum_a\left(|F(\tau_a)|^2+
                         N^{-2}|F'(\tau_a)|^2\right).
 \tag{63}
\]
Multiplication by \(\zeta\), denoted \(U\), is an exact invertible
operator on this \(2N\)-dimensional space. It retains each value
and first angular derivative. It satisfies
\[
 (U^N-\eta I)^2=0,\qquad
 \frac{\|F\|_{\mathrm{jet},N}}{1+|k|/N}
 \le \|U^kF\|_{\mathrm{jet},N}
 \le(1+|k|/N)\|F\|_{\mathrm{jet},N}.
 \tag{64}
\]
For the inequalities, the normalized jet at each grid point is
multiplied by a unit scalar and the matrix
\(\left(\begin{smallmatrix}1&0\\-ik/N&1\end{smallmatrix}\right)\).
Its norm and its inverse norm are at most \(1+|k|/N\).
In particular the full state changes by at most a factor two
for \(0\le k\le N\). This is a norm estimate for the transported
state; it is not a lower bound for the derivative observation
\(D_k\).

For comparison, if \(q_N\) itself has already been reduced to
degree at most \(D\), then \(g_N\) has Fourier degree at most
\(N\), and (61) simplifies to
\[
 D_k=iN^2\eta b_{N-k,N}\quad(1\le k<N),
 \qquad D_0=2iN^2\eta b_{N,N}.
 \tag{65}
\]
At \(k=N\) one must instead use \(D_N=\eta D_0\).
The vanishing coefficient \(b_{0,N}\) does not replace that
endpoint observation. Reducing the product first is a valid
operation in a traced variable, but it has already combined
the cancellations between all unreduced Fourier aliases.

These identities apply independently at every selected vertex.
They give commuting finite charge shifts and their exact
endpoint equations. The continuous geometric parameter
\(\lambda\) in the
[fractional-charge cube](research_positive_path_fractional_charge_cube.md)
is a separate variable. A proposed identification
\(\lambda=j/N\) concerns a selected Fourier mode of a
particular representative. Formula (61) shows which other
modes contribute to the actual finite observation. Neither
the positive geometry nor (64) removes those modes.

The [finite charge reduction](research_adjacent_components_and_charge_cancellation.md)
describes changes of representative by the original relation.
Such changes leave every observation in (60) unchanged, since
they vanish with their full physical jets, but they can change
the individual coefficients \(b_{j,N}\). A charge continuation
must therefore control a specified representative or the whole
alias sum. The radical-matching gap concerns a different
decomposition, into high Newton indices on edges; it does not
by itself bound this Fourier alias sum or its scalar observation.
What is still needed is a source estimate that follows the
selected coefficient, including the initial observation and
the remaining modes, along the discrete charge path. The
finite equations above supply its exact algebra, without a
nonzero-observation conclusion.

### A contiguous relation with the exact wrapped endpoint

There is also an exact relation that shifts the charge by the
crossing power. It uses the original Gaussian jet representative,
with its specified logarithm, and keeps the term caused by wrapping
one physical grid point. Let \(n\) be a signed integer,
\(\delta=2\pi/N\), \(t_L=-\pi+\pi/N\), and let \(h\) be a
periodic trigonometric polynomial. Define
\[
 F_k[h](t)=h(t)\exp\!\left(\frac{inN}{4\pi}t^2-ikt\right),
 \quad
 \mathscr V_k[h]=\sum_a F_k[h](\tau_a),\quad
 \mathscr D_k[h]=\sum_a F_k[h]'(\tau_a).
 \tag{66}
\]
For the original spectator in (59), take
\(h(t)=\sin t\,f_N(-2\cos t)\). The canonical crossing and
the Gaussian representative have the same full physical jets,
so
\((V_k,D_k)=C_{N,n}(\mathscr V_k[h],\mathscr D_k[h])\),
where \(C_{N,n}=\exp(\pi inD^2/(4N))\).
All these are finite sums; no Gaussian has been equated to the
canonical crossing away from the physical data.

Write \(h^+(t)=h(t+\delta)\), \(\epsilon=(-1)^n\), and
\(E_k=\exp(i\pi(n+2k)/N)\). Then
\[
 \begin{split}
 \mathscr V_k[h^+]
 &=E_k\left\{\mathscr V_{k+n}[h]
                  +(\epsilon-1)F_{k+n}[h](t_L)\right\},\\
 \mathscr D_k[h^+]
 &=E_k\left\{\mathscr D_{k+n}[h]
       +(\epsilon-1)F_{k+n}[h]'(t_L)
       +inN\epsilon F_{k+n}[h](t_L)\right\}.
 \end{split}
 \tag{67}
\]
Indeed completing the square gives the entire identity
\(F_k[h^+](t)=E_kF_{k+n}[h](t+\delta)\).
The shifted grid replaces \(t_L\) by \(t_L+2\pi\).
Periodicity of \(h\), with integer \(k,n\), gives
\[
 F_{k+n}[h](t+2\pi)
       =e^{inN(t+\pi)}F_{k+n}[h](t).
 \]
Its value at \(t_L\) has factor \(\epsilon\); differentiating
also produces \(inN\epsilon F_{k+n}[h](t_L)\).
This proves both equations in (67). In particular even crossing
power removes the value discrepancy, but not the wrapped normal
term. This is the charge-observation version of the same wrapped
Gaussian calculation used in the
[signed Ward identity](research_signed_gaussian_ward_endpoint_packet.md),
equations (5)--(10).

For the actual incident kernels the endpoint is simpler than a
general value of the integrand. Write
\[
 \theta=\pi/N,\qquad c_0=2\cos\theta,\qquad
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),
 \quad
 h(t)=\sin t\prod_{w=1}^{d}K_N(t,u_w).
 \]
Since \(e_0(c_0)=1\) and \(e_j(c_0)=0\) for \(j\ge1\),
one has exactly
\[
 h(t_L)=\sin t_L,\qquad
 h'(t_L)=\cos t_L+\sum_{w=1}^{d}E_N(u_w),
 \quad
 E_N(u)=\sum_{j=1}^{D}
       \frac{(-1)^j\sin\theta}{2\sin(j\theta)}
                         e_j(-2\cos u).
 \tag{68}
\]
To check the normal coefficient, the original Newton product gives
\[
 e_j'(c_0)=
       \frac{(-1)^j}{4\sin\theta\sin(j\theta)}
       \quad(1\le j<N).
 \tag{69}
\]
Apply the product rule and \(d(-2\cos t)/dt=2\sin t\).
The coefficient of every Newton mode in \(E_N\) has modulus
at most \(1/2\), including the last mode. Thus the wrapped
endpoint contains a sum of terms with at most one surviving
incident boundary factor. It does not contain a product of
all \(d\) such factors. Equations (68)--(69) are identities
of the full ordinary boundary polynomials, so their derivatives
are retained when another vertex is traced.

There is a stronger bound than the individual coefficient bound.
The [full normal estimate](research_all_color_path_normal_bound.md),
Lemma 5, proves
\(\sup_{w\in[-2,2]}|\partial_zK_N(c_0,w)|\le N^4/4\).
Since \(E_N(u)=2\sin^2(\pi/N)\partial_zK_N(c_0,-2\cos u)\),
\[
                  \sup_{u\in\mathbb R}|E_N(u)|
                              \le \frac{\pi^2}{2}N^2 .
 \tag{70}
\]
Every fixed angular derivative is also polynomially bounded,
by the trigonometric Bernstein inequality and degree at most
\(D\). This retains the cancellation within the original
endpoint polynomial.

This reduction is useful source information for a possible
charge transport proof. The translated spectator \(h^+\)
in (67) remains part of that proof; the equation is not a
closed scalar recurrence for one fixed \(h\). Moreover \(E_N\)
contains low as well as high Newton indices. Its polynomial
whole-boundary bound does not by itself bound the result of
attaching an arbitrary short component. A geometric edge-cut
comparison would have to be paired with a quantum estimate
for these actual endpoint insertions. Neither the wrapped
normal term nor the translated spectator is removed by
continuity of the geometric critical point.

### A source-fixed family with a small positive leading charge

The exact insertions in (62) also give an actual initial family for
starting the charge continuation. Choose integers \(0<j<N\)
and insert \(T_{N-j}(-w/2)\). This is a specified polynomial
in the original algebra. In the lower contour of the
[complete trace formula](research_exact_complete_trace_contour.md),
its kernel is exactly
\[
 \begin{split}
 W_N(t)\cos((N-j)t)
 &=\frac{e^{-iNt}\cos((N-j)t)}
                   {(1-\eta e^{-iNt})^2}\\
 &=\frac12e^{-ijt}
       \frac{1+e^{-2i(N-j)t}}{(1-\eta e^{-iNt})^2}.
 \end{split}
 \tag{71}
\]
Thus its first phase has charge \(\chi=j/N\), with coefficient
\(1/2\). Every other Fourier charge is still present in the
displayed rational kernel. On \(-\Im t\ge h>0\), with
\(e^{-Nh}\le1/2\), one has the explicit bound
\[
 \left|\,2e^{ijt}W_N(t)\cos((N-j)t)-1\,\right|
 \le12\left(e^{-Nh}+e^{-2(N-j)h}\right).
 \tag{72}
\]
This follows by expanding the difference of
\((1-\eta e^{-iNt})^{-2}\) from one and bounding its
denominator below by \(1/4\).

The coupon has modulus at most one on every real physical
angle, and its first angular derivative has modulus at most
\(N\). Hence inserting it costs only a polynomial factor in
an estimate of removed physical grid points. The exact
vertical endpoint current, however, is multiplied by the
same cosine and must still be estimated. Formula (72)
controls other charges only on a contour already known to
have a suitable whole-source upper bound.

For a fixed small \(\chi>0\), the geometric charge-cube
solution is near the complete point. Its factor \(\sin t_\chi\)
is nonzero. The
[small-charge source theorem](research_small_charge_path_source.md)
now proves the uniform physical-tail and endpoint-current
estimates for this actual coupon family on every fixed
positive path with powers at least three, for charges in
\([1/640,1/320]\). Its Section 7 proves a smaller initial
box \([1/4000,1/2000]\) for arbitrary fixed signed integer
powers, including zero; Section 8 extends that box to every
fixed graph carrying the same edge kernels, with no isolated
selected vertex. These statements supply a nonzero
coefficient using the specified source, without an assumed
value of \(b_{0,N}\). They do not extend it to charge one.
At \(\chi=1\) the numerator terms in (71) coincide and the
factor \(1/2\) disappears. At \(\chi=0\), the original
endpoint identity (62) and the odd zero-frequency coefficient
must instead be retained. Neither endpoint is obtained by
discarding its companion terms.

## 16. Gaussian preparation is now proved for the small-charge source

The [small-charge source theorem](research_small_charge_path_source.md)
verifies the Gaussian preparation condition for an actual finite
source. The underlying harmonic-oscillator estimate is standard and
was proved directly in
[the Gaussian observation note](research_shifted_gaussian_observation.md).
Here its input norm and residual can both be calculated independently
of the period being observed.

Use its finite-graph corollary, Section 8: the graph is fixed,
every selected vertex has degree at least one, every edge is the
same-index kernel, and the fixed integer powers may have either
sign or be zero. Repeated edges and loops are allowed, with a
loop counted twice in its vertex degree. Charges lie in
\([1/4000,1/2000]\); the larger proved positive-path box may
also be used in that special case. Write
\(\mathbf t^*=\boldsymbol\theta-i\mathbf H\),
\[
 W=\Phi_{\boldsymbol\chi}(\mathbf t^*),\qquad
 \mathcal H=-\Phi_{\boldsymbol\chi}''(\mathbf t^*)=R+iB,
 \qquad R\succeq\frac1{10\pi}\operatorname{diag}(d_v)>0.
 \tag{73}
\]
All matrices in (73) are complex symmetric, with \(R,B\) real
symmetric. Let \(m\) be the number of selected vertices and \(e\)
the number of original edges. Choose a smooth function
\(\zeta:\mathbb R^m\to[0,1]\) which equals one near zero and
is supported in a fixed small ball. The ball is chosen inside the
retained horizontal rectangle, uniformly on the compact charge box.
For real \(x\), put \(t_v=t_v^*+x_v/\sqrt N\) at selected
vertices, and retain zero at the complete vertices. Define
\[
 \begin{split}
 G_N(x)={}&\zeta(x/\sqrt N)\,
       N^{3e/2}e^{-NW}
       \prod_{\{v,w\}\in E}K_N(t_v,t_w)\\
 &{}\times
       \prod_{v\in I}
       \left[
        \sin t_v\,e^{in_vNt_v^2/(4\pi)}
        \frac{2e^{-iNt_v}\cos((N-j_v)t_v)}
                    {(1-\eta e^{-iNt_v})^2}
       \right].
 \end{split}
 \tag{74}
\]
This is the actual horizontal integrand with explicit elementary
normalizing factors and a cutoff. In particular it uses the full
finite edge kernels and the full rational trace kernels. Its
normalization does not divide by an unknown quantum period.

Let
\[
 a_*=\prod_{v\in I}\sin t_v^*
                 \prod_{\{v,w\}\in E}a_e(t_v^*,t_w^*)\ne0,
 \qquad
 (\mathcal L_{\mathcal H}f)_v
              =\partial_{x_v}f+(\mathcal Hx)_vf.
 \tag{75}
\]
The squared norm of the vector \(\mathcal L_{\mathcal H}f\) is the sum
of the squared \(L^2\) norms of its components.

**Proposition.** Uniformly over the small positive charge box,
\[
 \begin{split}
 \left\|G_N-a_*e^{-x^T\mathcal Hx/2}\right\|_{L^2}
                                      &=O(N^{-1/2}),\\
 \|\mathcal L_{\mathcal H}G_N\|_{L^2}
                                      &=O(N^{-1/2}),\\
 \|G_N\|_{L^2}
   &=|a_*|\,\frac{\pi^{m/4}}{(\det R)^{1/4}}
                                      +O(N^{-1/2}).
 \end{split}
 \tag{76}
\]
The last expression is bounded below by a positive constant
for each fixed graph and powers. Therefore
\[
        \frac{\|\mathcal L_{\mathcal H}G_N\|_{L^2}}
                          {\|G_N\|_{L^2}}=O(N^{-1/2}).
 \tag{77}
\]

*Proof.* The full thin-box edge expansion, including its derivatives,
and (71)--(72) give the normalized integrand in the support of
\(\zeta\) as
\[
 a(\mathbf t)e^{N(\Phi_{\boldsymbol\chi}(\mathbf t)-W)}
                  (1+O(N^{-1})),
 \quad
 a(\mathbf t)=\prod_v\sin t_v\prod_e a_e(t_v,t_w),
 \tag{78}
\]
with exponentially small additional errors from the other Fourier
charges. Those errors and their fixed derivatives remain
exponentially small. The heights are bounded away from zero on
the compact box. All functions in (78) have uniform holomorphic
derivative bounds on a fixed neighborhood of the chosen ball.

The horizontal Hessian bound gives
\[
 \Re\{\Phi_{\boldsymbol\chi}(\mathbf t^*+x/\sqrt N)-W\}
                       \le-\frac{c|x|^2}{N}
 \tag{79}
\]
for a fixed \(c>0\). Taylor's formula at the full complex critical
point gives
\[
 \sqrt N\,\nabla\Phi_{\boldsymbol\chi}
                     (\mathbf t^*+x/\sqrt N)
             +\mathcal Hx=O(|x|^2/\sqrt N).
 \tag{80}
\]
Differentiate (78), use (79)--(80), and integrate its bound
\(CN^{-1/2}(1+|x|^2)e^{-c|x|^2}\).
The cutoff derivative has its additional factor \(N^{-1/2}\)
and is supported where \(|x|\) is a fixed positive multiple
of \(\sqrt N\), so its contribution is exponentially small.
This proves the second line of (76).

For the first line, put
\(u=N(\Phi_{\boldsymbol\chi}(\mathbf t^*+x/\sqrt N)-W)\)
and \(v=-x^T\mathcal Hx/2\). Taylor's formula on the
cutoff gives \(|u-v|\le C|x|^3/\sqrt N\). The elementary
inequality
\[
 |e^u-e^v|\le |u-v|\max(e^{\Re u},e^{\Re v})
\]
and the negative quadratic real-part bounds for both phases
give an \(L^2\) error \(O(N^{-1/2})\) on the whole cutoff.
The amplitude error is bounded by
\(C|x|N^{-1/2}e^{-c|x|^2}\). The Gaussian outside the
cutoff is exponentially small. Its squared norm is
\(|a_*|^2\pi^{m/2}/\sqrt{\det R}\), giving the last line.
Nonvanishing and compactness of \(a_*\) give the lower bound.
\(\square\)

For clarity, this defect has a uniform spectral meaning.
Multiplication by \(e^{-ix^TBx/2}\) conjugates
\(\nabla+Rx\) to \(\mathcal L_{\mathcal H}\).
The real Gaussian oscillator has a one-dimensional nullspace
and a gap \(2\lambda_{\min}(R)\) above it. If \(P_{\mathcal H}\)
is the orthogonal projection onto
\[
 g_{\mathcal H}(x)
       =(\det R/\pi^m)^{1/4}e^{-x^T\mathcal Hx/2},
 \]
then the directly proved Gaussian estimate gives
\[
 \|G_N-P_{\mathcal H}G_N\|_{L^2}^2
 \le\frac{\|\mathcal L_{\mathcal H}G_N\|_{L^2}^2}
                     {2\lambda_{\min}(R)}
 \le5\pi\,\|\mathcal L_{\mathcal H}G_N\|_{L^2}^2.
 \tag{81}
\]
Thus the relative non-Gaussian part is \(O(N^{-1/2})\).
The initial norm in this assertion is independently fixed by
(76), and the original mixed currents and removed rows have
the separate strict gaps proved in the small-charge theorem.

This explains the source of the near-invariance in this example:
after the known complex phase is removed and the selected
variables are rescaled, the actual integrand approaches the
Gaussian nullstate of the annihilation operators (75). It does
not say that the unmodified finite color vector is fixed by
both clock and shift, or that the original crossing is unitary.
No estimate (76)--(81) is presently asserted along the rest
of the path to charge one. Extending it requires control of
the actual source there, including its observation and all
the other contour terms.

## 17. The actual resonant projector can be exponentially large

The original forced recurrence gives a concrete distinction between
an eigenvalue separation and a useful norm bound for the closing
observation. The first calculation is at odd levels, followed by
the actual even-level forced equation. The only exponential
input is the already proved full internal \(3,3\) source; it does not
assume a packet for other powers.

Use the matrices of the
[complete-boundary coefficient theorem](research_complete_boundary_coefficient_transport.md):
\(N=2m+1\ge3\), \(D=N-1\),
\(\kappa=\exp(\pi iD^2/(2N))\), \(J_{ij}=\mathbf1_{i+j=D}\),
\(M\) is the original crossing multiplication, \(Z\) is multiplication
by the spectral variable, and \(v=v(-2)=(e_j(-2))_{j=0}^D\).
For a fixed integer \(n\), put
\[
 A_n=JM^n,\quad w_n=A_nv,\quad
 C_n=A_n(Z^{\mathsf T}+2I)A_n^{-1}.
 \tag{82}
\]
These are the full original vectors, including their high Newton
coordinates. They obey \(C_nw_n=0\) and
\((w_n)_D=\kappa^n\). The finite equation has zero forcing at odd
levels, but its cap pin is nonzero.

The original identities
\(\overline M=M^{-1}\) and \(M^{\mathsf T}J=JM\) imply
\(A_n^*JA_n=J\) and \(C_n^*J=JC_n\).
The normalization of the pinned vector is exactly
\[
 w_n^*Jw_n=v^{\mathsf T}Jv
          =\frac{P_N'(-2)}{N^2}=1.
 \tag{83}
\]
Here \(P_N=2T_N(z/2)+2\), and \(P_N'(-2)=N^2\) at odd
levels. The middle equality follows from the exact Newton
identity kernel, including its first normals, rather than
from a positive metric.

**Proposition.** Zero is a simple eigenvalue of \(C_n\). Its
actual spectral projector and Euclidean operator norm are
\[
 \Pi_n=w_nw_n^*J,\qquad
              \|\Pi_n\|_2=\|w_n\|_2^2
                         =\mathcal P_{n,-n,N}(-2,-2).
 \tag{84}
\]
Every other eigenvalue is real and at least
\(g_N=4\sin^2(\pi/N)\). Nevertheless, writing
\(M_{33}=\Re\mathcal S_{33}(0,0)\) for the proved original
internal-pair rate, there is \(c>0\) such that
\[
 \|\Pi_3\|_2\ \ge\
       |\mathcal P_{3,3,N}(-2,-2)|
       \ \ge\ cN^{-3/2}e^{NM_{33}}
       \qquad(N\text{ odd and sufficiently large}).
 \tag{85}
\]
In particular,
\(\liminf_{N\ {\rm odd}}N^{-1}\log\|\Pi_3\|_2
 \ge M_{33}>63/25\).

*Proof.* The similarity in (82) preserves the spectrum and
Jordan multiplicities of \(Z\). At odd levels its physical
root \(-2\) is simple; the nearest other root is
\(-2\cos(2\pi/N)\). This proves the spectral assertions.
Equation (83) shows that \(w_n^*J\) is a normalized left
zero eigenvector, giving the projector in (84).
Its rank-one norm is
\(\|w_n\|_2\|Jw_n\|_2=\|w_n\|_2^2\).
The opposite-power identity in (84) is the original
bilinear contraction, since \(w_{-n}=\overline{w_n}\).
The same original contraction gives
\(\mathcal P_{3,3,N}=w_3^{\mathsf T}w_3\), whose modulus
is at most \(\|w_3\|_2^2\).
Finally the [full \(3,3\) theorem](research_internal_pair_three_full_boundary_packet.md#1-original-source-and-statement)
has a nonzero amplitude, level scalar of modulus one, and
prefactor \(N^{-3/2}\), through both parities. It therefore
implies (85). The strict rational rate bound
\(M_{33}>63/25\) is the certified normalization used in
[the pair tail comparison](research_real_pair_geometry_and_tail_gap.md#3-comparing-the-pair-action-with-the-two-half-charge-actions).
\(\square\)

Thus an inverse eigenvalue gap of order \(N^2\) does not bound
this projector. For example its Riesz contour immediately gives
\[
 \sup_{|z|=g_N/2}\|(zI-C_3)^{-1}\|_2
                     \ge \frac{2\|\Pi_3\|_2}{g_N}.
 \tag{86}
\]
Also, if a change of coordinates \(S_N\) makes
\(\|S_N\Pi_3S_N^{-1}\|_2\le e^{o(N)}\), its condition
number must satisfy
\(\liminf N^{-1}\log\kappa_2(S_N)\ge M_{33}\).
This permits exponentially weighted spaces, but requires
their effect on the actual source and closing functional
to be tracked.

There is an exact Green identity retaining the resonant term.
For fixed integers \(n,p\), define
\[
 G_{n,p,N}=\int_0^\infty
   \left[e^{-sC_n^{\mathsf T}}e^{-sC_p}
                        -\Pi_n^{\mathsf T}\Pi_p\right]\,ds .
 \tag{87}
\]
For each finite odd level this converges: the nonzero eigenvalues
are positive, their Jordan blocks have size at most two, and
the subtraction removes the zero eigenspaces. Differentiating
the matrix exponential and integrating gives
\[
 \begin{split}
 I={}&C_n^{\mathsf T}G_{n,p,N}+G_{n,p,N}C_p
                                      +\Pi_n^{\mathsf T}\Pi_p,\\
 \Pi_n^{\mathsf T}\Pi_p
    ={}&\ell_n\,\mathcal P_{n,p,N}(-2,-2)\,\ell_p^{\mathsf T},
       \qquad \ell_n=J\overline{w_n}.
 \end{split}
 \tag{88}
\]
The second line follows directly from (84); no complex conjugate
has been inserted into the desired pairing.
Contracting the first line with \(w_n^{\mathsf T}\) and \(w_p\)
cancels the entire Green part, leaving precisely the original
closing coefficient in the rank-one term.

For power three the complementary Green operator itself must be
exponentially large. This follows with an explicit constant from
the original four-step matrix, rather than an estimate for an
arbitrary similar matrix. In the notation of the coefficient
theorem, \(q=e^{\pi i/N}\), \(B=Z^{\mathsf T}\), and
\[
 \begin{split}
 \mathcal D_3={}&q^{-2}(B^2-I)L_1+q^{-3}BZ
                              -8q^{-2}B+8q^{-1}I,\\
 C_3={}&\mathcal D_3+2I,\qquad
                 \|C_3\|_2\le612 .
 \end{split}
 \tag{89}
\]
Indeed \(\|Z\|_2=\|B\|_2\le6\), from its diagonal bounded
by \(2\) and subdiagonal bounded by \(4\). The tridiagonal
\(L_1\) has diagonal bounded by \(6\) and two off-diagonals
bounded by \(4\), so \(\|L_1\|_2\le14\).
Since \(|q|=1\), the right side of (89) is bounded by
\((36+1)14+36+48+8+2=612\).
The rank-one identity in (88) gives
\(\|\Pi_3^{\mathsf T}\Pi_3\|_2
 =|\mathcal P_{3,3,N}|\|w_3\|_2^2\).
Consequently every solution of the first equation in (88), and
in particular (87), satisfies at odd levels
\[
 \|G_{3,3,N}\|_2
   \ge\frac{|\mathcal P_{3,3,N}(-2,-2)|^2-1}{1224},
 \qquad
 \liminf_{N\ {\rm odd}}\frac1N\log\|G_{3,3,N}\|_2
                                    \ge2M_{33}>126/25.
 \tag{90}
\]
To see this, take norms in
\(C_3^{\mathsf T}G+GC_3=I-\Pi_3^{\mathsf T}\Pi_3\),
use the reverse triangle inequality and (89), and then apply
\(\|w_3\|_2^2\ge|\mathcal P_{3,3,N}|\) and (85).
Choosing a different Green solution cannot give a polynomial
Euclidean bound for this same right-hand side.

At even levels there is no zero eigenvalue: the actual equation is
\(C_3w_3=4\kappa^3\mathbf e_0/N^2\), with
\(\|\mathbf e_0\|_2=1\) and \(|\kappa|=1\).
The same full \(3,3\) source theorem therefore gives
\[
 \begin{split}
 \operatorname{dist}(0,\operatorname{spec}C_3)
       &=4\sin^2\!\frac{\pi}{2N},\\
 \|C_3^{-1}\|_2
       &\ge \frac{N^2}{4}\|w_3\|_2
        \ge cN^{5/4}e^{NM_{33}/2}
               \qquad(N\text{ even and sufficiently large}).
 \end{split}
 \tag{91}
\]
The first line follows from the same exact similarity with
\(Z^{\mathsf T}+2I\). The second retains the literal original
forcing: the square root of the nonzero \(N^{-3/2}\) pair
packet gives \(\|w_3\|_2\ge cN^{-3/4}e^{NM_{33}/2}\).
Thus the inverse spectral distance is only of order \(N^2\),
whereas the actual inverse already has an exponential lower
bound on its specified cap column.

This supplies a source-exact summation-by-parts decomposition,
but the cap normalization in (83) does not determine that
coefficient: it fixes the left-right pairing for each individual
mode, whereas the desired observation is
\(w_n^{\mathsf T}w_p\). Nor does \(g_N\) bound
\(G_{n,p,N}\) in a useful norm without control of the nonnormal
spectral projectors and decaying semigroups. Equations (85),
(90), and (91) show these losses for actual sources at both
parities. A universal almost-invariance argument still
needs a compatible positive form and a quantitative closing
overlap; the ordinary eigenvalue separation alone supplies
neither.

## 18. The canonical positive form in full physical coordinates

There is an explicit positive form supplied by the original turn
and the full physical trace. It preserves the closing observation
exactly, including the first normals; it does not turn that
observation into a positive square.

Let \(V_N\) send a Newton coefficient vector to its value and first
derivative at each double physical root \(c_a\). At odd levels append
only the value at the simple root \(-2\). Confluent interpolation
makes \(V_N\) real and invertible. The trace matrix in these
coordinates is
\[
 \mathsf J_N=V_N^{-{\mathsf T}}JV_N^{-1}
  =\bigoplus_{\text{double }a}
       \eta\begin{pmatrix}-c_a&4-c_a^2\\4-c_a^2&0\end{pmatrix}
       \ \oplus\ \boldsymbol1_{\{N\ {\rm odd}\}}(1).
 \tag{92}
\]
The last notation means that the scalar block is present only at
odd levels. Formula (92) is the original product rule
\(\phi(fg)=\eta\sum_a\{(4-c_a^2)(f'g+fg')-c_afg\}\),
with the additional odd simple value. No derivative is assigned
to that simple node.

The actual turn and its associated positive form are
\[
 \mathsf T_N=V_NJV_N^{-1},\qquad
 \mathsf G_N=\mathsf J_N\mathsf T_N
             =V_N^{-{\mathsf T}}V_N^{-1}>0,\qquad
 \mathsf T_N^2=I .
 \tag{93}
\]
These identities follow by multiplication, using \(J^2=I\).
In particular \(\mathsf T_N\) is a fundamental symmetry for the
indefinite trace form: multiplying by it gives the positive wire
metric. Positivity here means ordinary positive definiteness on
the full complex space, since
\(y^*\mathsf G_Ny=\|V_N^{-1}y\|_2^2\).

For the actual original sources \(w_n=JM^nv(-2)\), put
\(y_n=V_Nw_n\), and use
\(\langle a,b\rangle_{\mathsf G}=a^*\mathsf G_Nb\).
Their exact closing and reflected norm become
\[
 \begin{split}
 \mathcal P_{n,p,N}(-2,-2)
   &=y_n^{\mathsf T}\mathsf G_Ny_p
     =\langle\overline{y_n},y_p\rangle_{\mathsf G},\\
 \|y_n\|_{\mathsf G}^2
   &=\|w_n\|_2^2=\mathcal P_{n,-n,N}(-2,-2).
 \end{split}
 \tag{94}
\]
Reality of \(V_N\) and \(\mathsf G_N\) makes conjugation an
antiunitary map for this metric. Thus the required scalar is
its specified overlap with the source, not the positive norm
in the second line. Every further real Jacobi or physical-row
coordinate change, equipped with the corresponding pullback
of \(\mathsf G_N\), preserves both quantities.

This distinction is exponential for actual sources. The proved
[long-power same-sign/reflected comparison](research_complete_boundary_coefficient_transport.md#7-exponentially-small-coherence-in-an-actual-long-power-family)
therefore reads unchanged in these physical coordinates:
\[
 \frac{|\langle\overline{y_n},y_n\rangle_{\mathsf G}|}
      {\|y_n\|_{\mathsf G}^2}
  =c_n e^{-N\Delta_n}(1+O(N^{-1})),\qquad
 \Delta_n=\frac{16\pi^3}{n^6}+O(n^{-7})>0,
 \tag{95}
\]
for every sufficiently large fixed positive integer \(n\);
\(c_n>0\) is its nonzero fixed prefactor. This does not
assert that rate formula for \(n=3\). The odd-level projector
norm in Section 17 is likewise unchanged when transported
isometrically to (93).

A value-only Jacobi form does not include the full space in
(92). Even a different positive metric \(\mathsf H_N\) on all
the jets must retain the observation operator:
\[
 y_n^{\mathsf T}\mathsf G_Ny_p
       =\langle\overline{y_n},
                   \mathsf H_N^{-1}\mathsf G_Ny_p\rangle_{\mathsf H}.
 \]
Dropping that operator changes the source pairing.
The [positive physical Pick form](research_trace_normal_defect_positive_form.md)
offers another useful positive observation, with its explicitly
chosen adjoint cap. It does not identify that cap with the
original one in (94). The full-jet construction therefore gives
a natural positive representation, but a lower bound for the
original closing still requires its actual antiunitary overlap.
