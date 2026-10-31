# Exact leakage and the limitation of middle-only D reassociation

31 October 2026. **Research limitation; no global score counterexample.** This preserves the actual shared
incidence flow. It does not disprove the joint/min score inequality and does
not claim that an uncrossed interval arrangement is an actual source flow.

Orient each strict one-sided middle edge from its parent to its overloaded
child. On a directed pair e1 -> v -> e2, write the corresponding LEFT
coordinates after literal reflection as

    parent mass mu_i, child mass 1-nu_i, interval I_i=[mu_i,nu_i].

The ordinary target at v is exactly one. If ell_v is the sum of ALL other
original incidences at that face, its exact balance is

    (1-nu_1)+mu_2+ell_v=1,
    nu_1=mu_2+ell_v, ell_v>=0.                            (1)

The term ell_v includes outer corners and any remaining middle incidence;
it is not licensed to vanish because the selected middle edges form a
forest. Thus the middle intervals concatenate only if ell_v=0. Even an
ordinary path may produce overlaps, containment, or a reversal of their
starting order. No prescribed interval-tree parenthesization follows from
middle incidence alone.

For a proper overlap, write

    I1=[a,a+p+ell], I2=[a+p,a+p+ell+q],
    a,p,ell,q>=0, a+p+ell+q<=1/2.

For D(u,v)=f(u)+f(v)-f(u+v), direct cancellation gives

    D(a,p+ell)+D(a+p,ell+q)
     -D(a,p+ell+q)-D(a+p,ell)
      = f(p+ell)+f(ell+q)-f(ell)-f(p+ell+q).              (2)

For p,q>0 the right side is strictly positive. Indeed it equals

    integral_0^p [f'(ell+t)-f'(ell+q+t)] dt >0,

with endpoint cases understood by integrability and continuity. Therefore
replacing overlapping intervals by their union and intersection preserves
the coverage multiplicity but DECREASES their middle-D sum. This is the
opposite of the upper-bound direction needed to dominate the original
joint score. A valid proof must account for the other two D terms of every
one-sided port, or for a distinct complete-triangle entropy gain.

An exact original full-flow witness for nonzero leakage is retained in
the [exact rational certificate](../experiments/research_joint_middle_interval_leakage_certificate.json),
verified by the [portable audit](../experiments/audit_research_joint_middle_interval_leakage.py)
and its [recorded results](../experiments/research_joint_middle_interval_leakage_results.json). It uses the literal17-port word

    [1,3,0,2,4,1,3,0,2,4,1,3,0,2,4,1,3], marks0,16.

At ports5=(6,4,9,7) and10=(11,9,14,12), take quartet loads

    q5=(1/8,1/10,13/20,1/8),
    q10=(1/8,3/20,3/5,1/8).

Both are actual strict LEFT loads, and the two equal outer loads select
the symmetric coefficient tilt. Their middle intervals are

    I5=[1/10,7/20], I10=[3/20,2/5],

with overlap ell=1/5. All remaining ports are retained as actual full
four-incidence rows; the saved exact denominator40 allocation satisfies
ALL17 ordinary targets and both protected zero targets. It is not claimed
that the other ports are all CROSS. The actual source has full monomial
support, so integer multiples of this flow are literal coefficient arrays
at levels d divisible40 (and ordinary floor/ceil rounding also applies).

For this pair the three-D identity itself remains exact. Formula(2) only
rules out ignoring leakage and claiming entropy-nondecreasing middle-only
uncrossing. It says nothing about whether the outer-D terms can compensate
in a global face-preserving reorganization, nor whether the complete
geometric capacity dominates the resulting joint score.

The [outer-completion identity](research_joint_outer_completion_dual_work.md)
keeps the two other D terms and gives a separate sufficient shared-flow
criterion. The middle-only obstruction here does not refute that route.

The verifier checks 17 literal ports, 17 ordinary and two protected targets, all 68 rational quartet coordinates, the actual symmetric coefficient endpoints and the symbolic uncrossing identity.