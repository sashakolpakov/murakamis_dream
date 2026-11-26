# A literal short-crossing source cannot be discarded at the old action

Research deduction, 7 November 2026. The complete original cap supplies
an exact source witness for a limitation of local packet propagation.
After three negative crossings, its whole finite function is
exponentially smaller than the original cap on the original reference
neighborhood. Three positive crossings recover the cap exactly.
Consequently exponential smallness in that original local normalization
is not preserved by fixed short crossings.

The complete connection formula also gives its actual new endpoint
packets. Their phases are affine and differ on the two sides of real
incoming height. They cannot form a single nonzero holomorphic packet
across that height. This is an obstruction to a proposed boundary
approximation, not to a filled-knot volume identity. No numerical
evaluation is used.

## 1. The exact signed-run orbit and the observed return

Keep the original conventions
\[
 D=N-1,\qquad \kappa=e^{\pi iD^2/(2N)},\qquad
 Z_N(a,y)=c_N(a)^TS h(y),\qquad N\ge2.
 \tag{1}
\]
Here \(h\) is the original half-band cardinal column, \(S\) is the
original Newton-to-Fourier change of basis, and \(M\) is the original
crossing matrix, including its repeated-root first normals.
The [closing interface, equations (3) and (12)](research_mixed_fourier_boundary_closing_interface.md)
gives
\[
 N\int_\Gamma h(t)h(t)^T\,dt=I,\qquad
 (\mathcal M_nF)(y)
       =N\int_\Gamma F(t)h(t)^TM^nh(y)\,dt .
 \tag{2}
\]
Every \(\Gamma\) is a complete horizontal period. The pairing is
bilinear, and (2) holds at both level parities.

For \(G_{n,N}=\mathcal M_n Z_N\), the
[complete all-power identity](research_mixed_fourier_negative_three_full_source.md),
equation (4), is
\[
 G_{n,N}(a,y)
   =c_N(a)^TSM^nh(y)
   =\frac{e^{\pi iDa}}{\kappa^2N}
                      h(a)^TM^*M^{n+3}h(y).
 \tag{3}
\]
In particular all scalars in this identity are part of the finite
source; neither the adjoint \(M^*\) nor its observation is removed.

**Proposition 1.** Consecutive signed runs on this same boundary
compose exactly:
\[
 \mathcal M_mG_{n,N}=G_{n+m,N},\qquad
                         \mathcal M_3G_{-3,N}=Z_N .
 \tag{4}
\]
More generally, for any original column \(b_N\),
\[
 \boxed{\quad
 N\int_\Gamma G_{-3,N}(a,t)h(t)^TM^3b_N\,dt
                            =c_N(a)^TSb_N .
 \quad}
 \tag{5}
\]
The column may depend on retained outside variables.

*Proof.* Substitute the first equality of (3) in (2) and use its
exact reproducing identity. This gives
\(c_N(a)^TSM^nM^mh(y)\). The same calculation with \(M^3b_N\)
gives \(c_N(a)^TSM^{-3}M^3b_N\), proving (5). All sums and
integrals here are finite-band identities. \(\square\)

For example \(b_N=B_Nv(w)\) gives the original ordinary-output
observation after any fixed matrix word \(B_N\) from the closing
interface. More generally the
[exact arbitrary-power compiler](research_arbitrary_power_source_compilation.md),
Sections 1--2, supplies such a column for a literal context attached
at one canonical open leg; all its turns, products, traces and normal
data stay inside that column. No estimate for that column is used
in (5), and no free higher-degree ordinary polynomial is reduced
without its prescribed trace.

The runs in (4) contain no intervening physical turn or multiplication
vertex. Thus this identity is not
\(A_{-3}A_3=I\) for \(A_n=JM^n\). It permits consecutive crossing
powers to be combined before estimating them. It does not collapse
an arbitrary path or branching tangle to its total crossing number.

## 2. An actual exponentially small input with a non-small return

Fix any actual incoming reference \(a_*\) of the original cap and
the original output \(x_0\), in either admitted incoming type.
The [whole cap packet](research_mixed_fourier_right_cap_holomorphic_packet.md)
is nonzero on a fixed complex neighborhood of \((a_*,x_0)\) for all
sufficiently large \(N\). On a smaller neighborhood, the
[complete pole-and-current theorem](research_mixed_fourier_negative_three_pole_current.md),
equation (30), proves
\[
 \left|\partial^\alpha
           \frac{G_{-3,N}(a,y)}{Z_N(a,y)}\right|
       \le C_\alpha e^{-N/200}
 \tag{6}
\]
for every fixed multi-index \(\alpha\). This is an estimate for the
whole crossed function, not just its zero-index projection. In
particular it retains the explicit infinite current as well as
the nonzero pole product. The comparison action in (6) is the
original cap action.

Choose a closed product neighborhood \(K\) with nonempty interior
inside this domain, and put
\[
              \|F\|_{Z,K,N}=\sup_{(a,y)\in K}
                                  \left|\frac{F(a,y)}{Z_N(a,y)}\right|.
 \tag{7}
\]
On the finite space of incoming Laurent polynomials of band
\([-D,0]\) and outgoing half-band Fourier functions, (7) is a norm
for all sufficiently large \(N\). Indeed its denominator is nonzero,
and vanishing on the interior of \(K\) forces the finite function
to vanish identically. The crossing acts in the outgoing variable
and preserves this space.

**Theorem 2.** In this original local normalization,
\[
 \boxed{\quad
 \|\mathcal M_3\|_{Z,K,N}\ge C^{-1}e^{N/200}.
 \quad}
 \tag{8}
\]
The lower bound is witnessed by the literal source \(G_{-3,N}\).

*Proof.* Equations (4) and (6) give
\[
 \|\mathcal M_3G_{-3,N}\|_{Z,K,N}=1,\qquad
                  0<\|G_{-3,N}\|_{Z,K,N}\le Ce^{-N/200}.
 \tag{9}
\]
The strict positivity follows from invertibility and the nonzero
cap. Taking their ratio proves (8). \(\square\)

Thus neither exponentially small local relative errors nor errors
smaller than every inverse power of \(N\) define a class preserved
by these short crossings in the unchanged normalization. The same
literal witness has small normalized derivatives of every fixed
order by (6). Keeping those derivatives does not repair the
failure. This is stronger in its source scope than the artificial
modified-germ example in
[the turn-remainder note](research_source_germ_truncation_and_turn_remainders.md):
the input in (9) is itself a complete fixed signed-crossing source.
The operations and boundary coordinates differ, so no conclusion
about the ordinary angular norm is being substituted.

In particular a procedure that discards \(G_{-3,N}\) as an old-action
remainder, then applies the positive return in (4), deletes the
entire leading cap. Formula (5) shows the same deletion before the
prescribed final observation, with that observation retained.
This conclusion does not assert that an arbitrary ordinary closing
column has nonzero value.

## 3. The changed action and the necessary transition

Write the known original cap packet as
\[
 Z_N(a,y)=\omega_NN^{-3/2}A_0(a,y)
                    e^{N\Phi_0(a,y)}(1+O(N^{-1})),
 \qquad |\omega_N|=1,\quad A_0\ne0.
 \tag{10}
\]
If the complete crossed source has a nonzero packet
\[
 G_{-3,N}(a,y)=\omega'_NN^\beta A_-(a,y)
                    e^{N\Phi_-(a,y)}(1+O(N^{-1})),
 \qquad |\omega'_N|=1,\quad A_-\ne0
 \tag{11}
\]
on a neighborhood inside \(K\), with \(\beta\) fixed.
Then (6), at each fixed parameter, implies
\[
                         \Re\Phi_-\le\Re\Phi_0-\frac1{200}.
 \tag{12}
\]
Indeed divide (11) by (10), take the logarithm of the modulus,
divide by \(N\), and let \(N\) tend to infinity. The nonzero
amplitudes and all fixed powers of \(N\) disappear from that limit.

Consequently the old action, even up to a purely imaginary additive
constant, cannot normalize that packet.

The [complete connection formula](research_mixed_fourier_negative_three_connection.md),
Corollary 2 and equation (17), now supplies two such actual packets.
On each fixed negative-height neighborhood of the original plateau,
including every actual type-four reference, its action is
\[
                   \Phi_-(a,y)=2\pi ia-\pi iy .
 \tag{13}
\]
On each corresponding positive-height neighborhood its action is
\[
                   \Phi_+(a,y)=-\pi iy .
 \tag{14}
\]
Both have power \(N^{-3}\), their specified nonzero amplitudes and
the original unit scalar \(\kappa^{-3}\). Thus (12) is an actual
action comparison on these domains, not only a necessary test for a
future packet. Both action Hessians vanish. The leading contribution
is the endpoint current; the canonical pole product is subordinate
on either fixed nonzero-height side.

**Proposition 3.** Near any real incoming point in the interior of
the original plateau, no single nonzero holomorphic packet of fixed
power of \(N\), phase independent of \(N\), and holomorphic
relative \(O(N^{-1})\) error can represent \(G_{-3,N}\) on a
connected neighborhood containing both incoming height signs.

*Proof.* Such a packet with phase \(W\) and nonzero amplitude would
give
\[
                  \frac1N\frac{\partial_aG_{-3,N}}{G_{-3,N}}
                                  \longrightarrow\partial_aW
 \tag{15}
\]
locally uniformly. On the negative-height open subset, the proved
packet (13) makes this limit \(2\pi i\). On the positive-height
open subset, (14) makes it zero. The holomorphic function
\(\partial_aW\) cannot have both values on a connected
neighborhood, by the identity theorem. \(\square\)

The same derivative argument shows that on either open side every
such packet has the derivative of the corresponding affine phase;
one cannot restore strict phase curvature by a harmless choice of
its additive constant. Across height zero the exact connection
formula instead retains the factor \(X^{-N}-1\) and the pole
product. At the physical incoming nodes the former vanishes and
the latter equals the whole function exactly. This transition
cannot be discarded when an incoming observation uses those nodes.

For comparison, the endpoint-current bound for the twice-crossed
conditional source is paid relative to \(\Phi_0\), whereas its newly
constructed left saddle has its own action. A bound below
\(\Re\Phi_0-\delta\) proves dominance at a new action
\(M_{\rm new}\) only after a comparison with \(M_{\rm new}\).
The exact three-negative-crossing calculation illustrates why that
distinction matters; it does not make the twice-crossed comparison.

## 4. Consequence for short partial fillings

This deduction removes one possible shortcut rather than adding a
new conditional composition theorem. The existing
[source-adapted observation criterion](research_source_adapted_observation_composition.md)
already includes branching feedback and the final closing row.
The existing
[dominant-saddle transport theorem](research_dominant_saddle_transport.md)
already explains how a nonzero cycle coefficient survives when the
new action filtration, original cycle and lower-chain estimates
are controlled. Neither hypothesis follows from (6).

There are two concrete source requirements exposed by (3)--(12).
First, each short-component estimate must retain its own calibrated
action and the complete representative of its original integration
cycle. A single strictly curved Gaussian description is insufficient:
the regular Newton-index phase of \(G_{-3,N}\) has no critical point,
its actual endpoint phase is affine, and its complete formula switches
between that endpoint term and its pole product at the physical
nodes. Second, the remaining turns, multiplication
vertices and final ordinary trace must act on that retained object;
an old-reference local negligible quotient cannot be used in their
place. Formula (5) gives an exact test any proposed replacement
must pass.

Once actual component packets, whole ordinary boundary estimates
and marked geometric germs are proved, their assembly into long
remaining fillings is already supplied by
[the component argument](research_three_chain_short_filling_stability.md),
Sections 4--5, and
[the complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md).
Products and fixed crossing multipliers are also already controlled
within the proved concentrated ordinary class by
[boundary packet preservation](research_boundary_crossing_packet_preservation.md),
Section 5. What is not supplied is a theorem for every required
turned short-component output, including changed geometric classes,
with the nonzero observed coefficient and the new action.

The [finite-branching lemma](research_finite_exceptions_under_partial_fillings.md)
allows all constants to depend on the fixed partial assignment.
It therefore requires no universal metric or uniform threshold over
all short words. But
[original tree padding](research_original_tree_padding_equivalence.md),
Theorem 2 and Corollary 3, forbids disposing of unresolved cores
as a finite list: one fixed zero slice repeats any represented
hyperbolic core infinitely often, even with two free powers both
becoming long. This includes the possible nonhyperbolic intermediate
sources. The exact signed-run reductions and the present obstruction
do not prove their volume identities or enlarge the established
knot class.
