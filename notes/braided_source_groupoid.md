# Genuine braid transport on the retained source charts

Research note, 26 October 2026. This constructs a groupoid of the
existing source presentations with actual moving semicyclic centers,
tree changes and source-root charts. All braid and mixed comparison
identities retain the basic carry lattice, actual source sublattice,
dual source and selected cut. The meridian appears in the normalized
center map as U=M^(2N), with its raw K^N root still retained.

This is a construction of operator transport on the prescribed state.
It does not identify strand braids with tetrahedron vertex
permutations or prove the required global triangulation comparison.

## 1. Fixed face adapters are not repaired just by root charges

The [oriented-source note](oriented_tetrahedron_source.md) already
disproved the bare S4 tensor prescription with its actual face
metrics and corrected cyclic maps. There is a stronger finite
diagnostic for one proposed repair.

In the shared standard frames replace the local kernel by every
root translate L0(uQ^a,vQ^b), a,b modulo N, retaining its actual
relative-input clock/shift. Compare all root choices for the
reference order (0,1,2,3) with all choices for (1,2,0,3),
using those same actual face adapters.

At N=3, p=397, the two projective orbits are disjoint:
all 9*9=81 pairs have nonzero proportionality minors. The
[complete reduction certificate](../experiments/charged_vertex_order_results.json)
records the q-root, flags, difference roots, index pairs,
coefficient values and all 81 nonzero minors. Every required
denominator is a unit in this construction.

This refutes a rational identity for this particular repair
in characteristic zero. All odd-level integer-charge choices
are included projectively: their roots give these N^2
translates, while their full charged prefactors are nonzero
scalars. Such prefactors cannot repair nonproportionality.
They are not deleted from an actual period by this diagnostic.

The same diagnostic at N=2 and 5 also fails. Its variants
removing the relative mark or using raw cyclic rotation
likewise fail. The even-level test concerns the existing
fusion expression, not a new even charged definition.

This does not disprove the published decorated matrix
symmetries, whose full adapter prescription has not been
identified with this one. It shows that naming the charged
kernel while retaining these face maps is insufficient.
No geometric state is substituted for the selected actual cut.

## 2. Moving centers and the correct total Borel coordinate

Keep the genuine semicyclic modules V(x,phi) and their
highest-weight-normalized crossings from
[the semicyclic braid proof](semicyclic_carry_braiding.md).
Use the same color x=-M/q on b strands and put

    k=x^N=(-1)^(N-1)M^N, k^2=U=M^(2N),
    phi_j=epsilon a_j, j=0,...,b-1.

The raw checked positive center map is

    (a_j,a_(j+1)) -> (k a_(j+1),
                         k a_j+(1-k^2)a_(j+1)),      (2.1)

with the previously proved inverse for the negative crossing.
The uncheck wrap correction phi_2/k and the original twist
are retained.

For this variable-center construction choose endpoint factors

    c_j=x^(-j), S_j v_n=c_j^n v_n,
    X_j=x K_j^(-1), Y_j=c_j F_j.                    (2.2)

This choice is made for a specific reason. The normalized
Borel total is exactly the actual iterated coproduct:

    sum_j X_0...X_(j-1)Y_j
                 =sum_j K_0^(-1)...K_(j-1)^(-1)F_j
                 =Delta^(b-1)F.                    (2.3)

After the basis change S_j the normalized Y has standard
shift arrows and central wrap epsilon mu_j, with

    mu_j=k^(-j)a_j.

These inverse endpoint factors serve a different coordinate
choice from the positive powers used to make the earlier
common fixed line have equal wraps. Both choices must be
written explicitly; they are not interchangeable unmarked
normalizations.

Equation (2.1) now becomes

    L_-(U)=[[0,U],[1,1-U]],
    L_+(U)=[[1-U^(-1),1],[U^(-1),0]],              (2.4)

on (mu_j,mu_(j+1)). Their sum is preserved. Define normal flags

    delta_0=0, delta_(j+1)=delta_j-mu_j.             (2.5)

Then delta_b, the total central parameter, is preserved by
every crossing. Require distinct delta_i along the finite
path in use. This excludes finitely many linear divisors;
it does not require one finite Zariski chart to work for
every possible braid word simultaneously.

At U=1 the two classical matrices (2.4) are ordinary swaps.
The quantum pure-braid action is still nontrivial, as the
actual cup/cap identity in the companion meridian note proves.
The raw even-level sign in k has not been erased by (2.4).

## 3. All tree and source charts carry the same genuine arrows

Use the full frames of
[the source flag carry extension](source_flag_carry_extension.md),

    Ical_(T,a,s)=J_epsilon M_(T,a)(s).

At a root branch over source infinity write
M=t^(-w)Mbar, keeping the source line t^w and its dual.
Let B_i(a;epsilon) be the genuine crossing with the centers
updated by (2.1), and include the endpoint changes (2.2).
It maps both the original leaf lattice and the common carry
lattice to their target lattices. A wrap lowers the integer
residue degree by N and has one factor epsilon; its inverse
has the same property.

For an arrow from (T,a,s) to (T',a',s'), set

    Bcal_i=M_(T',a')(s')^(-1)
           J_epsilon^(-1) B_i(a;epsilon) J_epsilon
                    M_(T,a)(s).                    (3.1)

This is an integral isomorphism of the retained sources.
At infinity its coordinate matrix on the regular frames
has the explicit source-line factor t^(w'-w). The dual
uses the inverse transpose and the reciprocal line.

For zero braid length (3.1) is exactly the strict tree/source
transition. For a sequence of crossings and chart changes,
all intermediate M matrices cancel. Therefore the direct
genuine braid identity implies the same identity through
any intermediate trees and source charts, with the actual
intermediate centers. Positive/negative inverse paths
likewise close exactly. Source-line orders telescope.

This proves the mixed transport identities for source
presentations, rather than assuming a new cyclic braided
category from the Borel modules alone.

There is an additional actual module statement. The direct
coproduct intertwining in
[the holonomy construction](regular_holonomy_braiding.md#1-rational-conjugation-survives-when-a-universal-matrix-does-not)
and the correct wrap imply that (3.1) intertwines the same
total F and K on both sides, by (2.3)--(2.4). At generic
epsilon the total normalized Borel algebra is a full
N-by-N matrix algebra. Its commutant forces

    Bcal_i=I_total tensor b_i,                      (3.2)

with the entire relative operator b_i and its scalar fixed.
The identity extends to the source fiber by integral
specialization. It is not merely a trace comparison.

For the actual sublattice, substitution in
Ical^(-1)L_leaf gives

    Bcal_i B_(T,a,s)=B_(T',a',s').

The inverse transpose preserves the full dual, so the perfect
linking pairing and the lost normal directions are transported
as well. No ordinary specialization image replaces them.

## 4. The actual cut and its nontrivial braid holonomy remain

Closing all but the marked strand with the original pivot
still gives F_N(M)I. The residue-degree argument in the
carry theorem rules out every wrapped closed path. Under
(3.1), the full cut insertion is transported with the
operators. Its source and dual line factors cancel exactly;
the original ADO dimension is retained at the boundary.

On a center fixed point a braid gives a genuine loop in
this source groupoid. Its operator is not generally the
identity. The explicit identity

    e_0(B_N(1)^2-I)=(-1)^(N+1)(N-1)(q-q^(-1))Pi_N

in [the actual meridian source](meridian_casimir_source.md)
is nonzero. It has determinant-one unipotent local
monodromy, fixes the cup, and is detected by the actual
pivotal closing functional. Scalar source lines and
reduced central data do not contain that information.

This is why ordering paths cannot simply be forgotten
in a comparison using the actual strand braidings.
It is not a proof that all tetrahedron permutations are
strand braids, or that a differently decorated tetrahedron
cannot have its own S4 symmetry.

## 5. Exact checks, coverage and the remaining global task

[The groupoid audit](../experiments/audit_braided_source_groupoid.py)
checks ten variable-center cases, N=2,3,4,5,6 at generic
and Kashaev colors. The two three-letter braid paths use
different intermediate trees and source-root branches.
Their full matrices agree and both retain total line
order one. Inverse paths close; every arrow preserves
the actual specialization image and factors as (3.2).
Thirty original whole cut operators agree in the two
source charts. The Tor dimensions are retained.

The companion spectral/meridian checks in the same audit
test the actual meridian source and nontrivial full twist.
The separate [charge audit](../experiments/audit_charged_vertex_order.py)
provides the fixed-adapter counterexample in Section 1.

These are the existing cyclic recouplings and holonomy
crossings covered by
[Kashaev's cyclic 6j framework](https://arxiv.org/abs/hep-th/9411147)
and [Kashaev--Reshetikhin's root holonomy framework](https://arxiv.org/abs/math/0202212).
Only their abstracts are used for coverage; all operator,
lattice and source identities here follow from the direct
calculations already specified. No new knot invariant or
published global comparison theorem is assumed.

The subsequent [intrinsic cut theorem](intrinsic_cut_and_meridian_atlas.md)
assembles the two-copy meridian maps through a generic
even-strand braid using centralizer transitions. It proves
the full selected cut is intrinsic under fusion changes
and every module comparison, with the dimension and phase
retained. A perfect complete two-factor residue pairing
also fixes its integral Casimir order and dual.
The complete geometric triangulation presentation, its
geometric quantum-A component and selected regulator norm
remain unproved. The E^N=0 center family here is still the
reducible-character locus; it is not substituted for the
complete irreducible hyperbolic character.
