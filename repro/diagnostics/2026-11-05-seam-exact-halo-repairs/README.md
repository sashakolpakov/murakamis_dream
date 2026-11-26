# Exact halo-repair closure: bounded saved-witness tests

These files evaluate a rigorously motivated upper proxy at finitely many
floating configurations. They are not a certificate of a uniform seam gap.
No optimizer or outward cover was run. Original helper scripts remain frozen;
the archive preserves the executed drivers with their `/tmp` imports and records
all input/helper hashes.

At a seam at position zero, replace its virtual halos by the unselected
baseline symbol p0. The exact physical-minus-repaired AA differences are

    Delta_exit = w_-1(q_-3,q_-2,q_-1,xi_left)
               - w_-1(q_-3,q_-2,q_-1,p0),
    Delta_entry = w_2(xi_right,q_1,q_2,q_3)
                - w_2(p0,q_1,q_2,q_3).

Here w is the original coherent weight, including its complex supporting
plane and selected halfcorrections. The difference of occupation allocations
on either edge is zero. The repaired states are
`out=(q_-2,q_-1,p0)` and `in=(p0,q_1,q_2)`.

With theta=1/2, the tested proxy is

    -E3(out) - A3(in) - (1-theta)*Psi(out)
    - theta*(omega_-1+omega_1)/2
    + Delta_exit + Delta_entry
    + A_beta,alpha(h_left) + B_gamma(h_right)
    + 2*Delta_collar + beta*nu_collar - Re Gamma_pair.

The height profiles are the completed source bounds from
`research_mixed_height_resolved_seam_sources.md`. The collar width is .001.
No extra Q debit is introduced. This expression uses the guaranteed
three-step outgoing upper and incoming lower bounds, not a difference of
numerically optimized incoming potentials.

The physical seam configurations are the 29 previously archived witnesses.
Because q2 is now a physical endpoint of the corrected first AA edge, both
permitted q2 selections must be tested. This gives 49 fixed evaluations.
Selections on q-3 and q3 are halo-only and do not enter these edge weights.
In the first test their real coordinates equal the actual reference reals.
All 49 values are negative, the largest approximately `-.39804414424`.

The second test varies each of q-3 and q3 on a 101-point uniform grid in
`[.1,.5]`, augmented by cutoff corners and the reference value. The corrections
depend separately on these two variables, so the two finite-grid maxima can
be combined without a two-dimensional search. All values remain negative;
the largest is again `-.39804414424`. The largest increase in an individual
case relative to reference halos is approximately `.00105452417`.

This only samples the two extra halos at the already chosen physical
configurations. It neither maximizes over the other physical variables nor
covers all actual references. References are genuine periodic critical
solutions repeated along the local window; target symbols in that window
are independent. The diagnostic does not impose a short physical cycle.

For an A-run of length two, the first and last AA edge coincide. Both halo
changes must then be made jointly in one physical-minus-repaired difference,
counted once. This diagnostic does not include that case. A singleton has
no AA edge or repair. Distinct end corrections apply directly to runs of
length at least three; the two end windows can be enlarged independently
for a local upper comparison.
