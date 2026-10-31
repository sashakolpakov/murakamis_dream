# Independently long fillings of signed octahedral belt stacks

29 October 2026. This note assembles the quantum, peripheral, regulator and geometric inputs for the stated theorem.

## 1. The actual family and statement

Fix n>=1, a word epsilon of length n in {+,-}, and an integer a.
Use the two literal mirror/reversed pieces D_+,D_- of the
[octahedral stack construction](actual_balanced_octahedral_belt_stack_volume.md),
with ONE retained outer complete circle and the actual outer R^a.
Denote this ACTUAL augmented link by B_(epsilon,a). It has n inner
crossing circles and one outer belt. Its complement is complete
hyperbolic of volume2n v8, by its exact regular-cell/collar proof.

Choose ANY subset I of those n+1 auxiliary circles. For each i in I
use its preferred meridian and crossing-disk longitude to fill
the primitive slope mu_i+p_i lambda_i, for fixed nonzero integers
p_i. Equivalently perform the literal1/p_i surgery/full-twist
substitution in the original oriented diagram. Circles outside I
remain components with their literal color N/L_N; this is NOT
p_j=0, which would meridionally fill and remove them. Denote the
resulting link in S^3 by J_(epsilon,a,I)(p).

There is a source-dependent finite P such that, whenever

    min_(i in I) |p_i|>P,

the actual filled complement is hyperbolic and its original
single-cut reduced Kashaev evaluation satisfies

    lim_(N->infinity) (2pi/N)log|K_N(J_(epsilon,a,I)(p))|
                    =Vol(S^3 minus J_(epsilon,a,I)(p)). (1)

For I empty this is the already proved COMPLETE stack theorem,
with no filling threshold. For nonempty I the threshold may depend
on I; for a fixed stack take the maximum over its finitely many
subsets if desired.

The limits include every parity and composite level. The slopes
may have independent signs and arbitrarily unequal lengths. They
are fixed before N tends to infinity. No numerical value of P,
uniformity as n or a grows with N, or arbitrary branched-graph
theorem is claimed. Full twists preserve the main permutation.
When ALL n+1 circles are filled, J is a KNOT for odd a and has
TWO components for even a. For a proper subset its unfilled
auxiliary circles remain: the total is n+2-|I| for odd a and
n+3-|I| for even a.

## 2. Whole original quantum source, not a formal critical value

The exact color expansion inserts every R^(-2p_i) using the
original ordinary mixed circles L_j and the complete Hermite
filling coefficients. It retains the marked cut, original pivot,
full half-Cartan and all dimension endpoints. Coefficient mass is
polynomial for each fixed slope. No closed auxiliary component is
assigned an extra modified dimension.

The [inner auxiliary-color theorem](actual_belt_stack_auxiliary_color_inner_packet.md)
proves source-fixed nonzero analytic packets through the quarter-
index transition, for the ACTUAL colors j_i=N-h_i. Its exact
finite factorial completion agrees with the actual physical low
core on the grid, with a quantitatively retained exponential
replacement error in a faithful norm containing every first
Casimir normal. The nonzero RP band and the ENTIRE physical
inner-color complement have strict gaps, for every fixed n>=1.

The [outer squared-kernel theorem](actual_outer_color_squared_kernel.md)
retains the actual full-Hermite outer ordinary color. Its exact
double-pole kernel kills the dangerous false h≈N Fourier alias;
it proves the remaining outer-color complement gap, together with
a fixed-complex-neighborhood, separately even packet for ALL
n+1 circle colors. This is not a spectral eta=meridian guess.

Write p and q for the numbers of plus and minus pieces and
m=q-p+a. In x_i=h_i/N its local source action has

    phi(x)=n v8/pi - pi x_0^2/[n-im]
                  +(pi/2)sum_(i=1)^n(-1+i sigma_i)x_i^2+O_4,
    sigma_i=+1 for z, -1 for z^sharp.

The real quadratic part is strictly negative in every color. The
ENTIRE source cube complement is gapped, not just the individual
box coefficients. Thus the hypotheses of the
[general original-source long-filling transfer](general_original_source_long_filling_transfer.md)
hold. Restrict every unfilled color literally to h_j=0/L_N and
apply only the original filling functionals indexed by I. The
exact complex packet, nonzero amplitude, negative real Hessian
and entire-cube complement gap restrict to these coordinates.
It proves a NONZERO full-source asymptotic, and the selected
point tends to the complete source point as
min_(i in I)|p_i|->infinity. The empty subset instead uses the
already proved nonzero complete-stack asymptotic directly.
Fixed normal jets, endpoint currents and all nonleading charge
sectors are controlled by that proof before its conclusion.

## 3. The selected point is an actual marked representation

The [typed character composition](actual_belt_stack_typed_character_composition.md)
supplies the group/flag lift which is essential after the source
estimate. Its input is the source-selected internal critical root,
not an arbitrary branch of a trace polynomial. The local pair
matrices a,b,A=ba remain bounded and irreducible through A's
parabolic trace -2. The selected inner box, its sharp type and
every actual bare R interface satisfy their literal threaded
Hurwitz equations and ordinary-pivot flag conditions.

At the outer seam, TWO original nested main-head snakes reverse
dual tensor order and invert the main meridian paths. Every
incident mixed crossing is transported through the SAME original
Hopf duality, including its full Cartan and nilpotent factors.
The auxiliary cut/pivot and unrestricted marked co-source stay
on their original side. This proves the actual outer disk word
P_0=A^(-1), not a word selected from a matching cusp derivative.
Irreducibility uniquely gives C_0=K_tot at closure.

All complete white and BOTH inner shaded face maps match the
regular octahedron certificate, as full three-vertex maps. The
actual signed pants collars and outer R^a match too. The outer
generator is then uniquely forced by closure to be the geometric
one. Consequently the ENTIRE complete representation is the
positively oriented holonomy of the ACTUAL B_(epsilon,a), not only
a representation with matching flags, trace coordinates or Hessian.

Let z_i=Log H_i and G be the actual logarithmic source primitive,
with its real Cartan/spin constant retained. The preferred flagged
peripheral data at ALL n+1 auxiliary circles are exactly

    M_i=exp(-z_i/2),
    lambda_i=-exp(-ell_i), ell_i=partial_(z_i)G.        (2)

For the outer circle ell_0=eta=Log(-w). The preferred minus sign
is fixed by the original ordinary pivot and the disk framing.
Simultaneously inverting both generators and swapping their common
flag is equivalent; inverting only one is not. All surviving
main meridians are noncentral parabolic, so BOTH small logs at
each unfilled main cusp are zero, including the merged odd-a cusp.

## 4. The source action is the absolute regulator

Keep the spin term in Gbar=G-pi i sum z_i. The actual source
and preferred peripheral data give

    u_i=-z_i/2, v_i=pi i-ell_i,
    dGbar=2 sum_i v_i du_i,
    D_src=Im G-sum_i Re z_i Im ell_i.                  (3)

The developed fundamental chain for the SAME marked representation
has Bloch boundary -2 sum M_i wedge lambda_i. Its elementary
Bloch--Wigner differential equals dD_src, including its factor2.
Both sides have complete value2n v8 by the full geometric anchor.
They therefore agree on the connected selected germ. No equality
of an unproved transformed dilogarithm list is assumed.

The exact source filling equations are

    z_i+2p_i ell_i=2pi i m_i, m_i=+1 or -1, i in I,
    z_j=0, j not in I.                                (4)

Separate exact evenness gives ell_j=0 for every unfilled auxiliary
coordinate, even as all the other colors vary. Its actual
peripheral group remains noncentral parabolic near completeness.

Its kept quadratic chirp is
sum_(i in I)(z_i-2pi i m_i)^2/(4p_i). On(4) its imaginary part
equals -sum_i Re z_i Im ell_i. Hence the imaginary FULL filled
source action is exactly the marked representation volume D_src.
This establishes the volume normalization, not just a numerical
quadratic/cusp comparison.

## 5. Primitive completion supplies equality with hyperbolic volume

The small geometric squared-eigenvalue logs are

    U_i=-z_i, V_i=-2ell_i,
    U_i+p_i V_i=-2pi i m_i, i in I,
    U_j=V_j=0, j not in I.                             (5)

Thus the filled slope has its actual primitive2pi angular period.
The preferred SL longitude sign in(2) is kept before passing to
these small geometric logs. A mere exponentiated PSL identity
would not establish this unit winding.

The actual selected representations and peripheral flags tend
to the now identified complete geometric ones as the chosen slopes
become independently long. For each filled coordinate separate
evenness implies ell_i divisible by z_i, so z_i=0 would contradict
(4). The full geometric completion theorem therefore applies to
these source-selected representations. Its explicit logarithmic
torus/tube construction adds a smooth core at each primitive
slope, with no missing axis sheet. The compact core and every
unfilled main AND auxiliary cusp remain positive and complete.

This constructs the COMPLETE hyperbolic metric on the actual
filled topology; it is not merely a nearby incomplete metric.
The oriented fundamental class and the two-way Gromov-volume
comparison identify its regulator with the actual hyperbolic
volume. Combining this with the NONZERO whole-source asymptotic
and (3)--(4) proves(1).

## 6. Scope ledger

The theorem expands a cyclic one-belt source family. It does not
assert an arbitrary six-port tensor estimate, arbitrary branched
augmentation, or the volume conjecture for every fixed bridge
number. The possible overlap of these actual belt-stack diagrams
with known Whitehead-chain families remains a coverage caveat;
no novelty claim about a literature family is used in the proof.

For partial filling, every unfilled color remains the literal L_N. Its two geometric logarithms vanish by exact separate evenness, and primitive completion leaves that cusp complete. The linked composition note gives the detailed marked proof.