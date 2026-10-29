# What fixed algebraic rigidity can force for the actual selected period

28 October 2026. Exact cyclotomic pointing already determines the
actual quantum period. It does not automatically make its geometric
coefficient nonzero. Two precise facts sharpen the torsor target:

1. The SAME original figure-eight family has exponential growth on
   its complete meridian arc and bounded values on every fixed-color
   meridian arc approaching the same complete classical point. A
   uniform dominant geometric comparison regular on the raw central
   fibre is therefore impossible. The divided normal source is
   essential, rather than an optional choice of coordinates.
2. The explicit whole-word Kummer period has a fixed number of
   variables, but growing cover genus and growing character homology.
   It has not yet supplied the fixed finite-rank algebraic object
   required by the existing whole-comparison rigidity theorem.

These are proofs about the original anchored state and its actual
cover. No rescaled invariant or adjustable levelwise source is used.

## 1. The source is already fixed; uniqueness is not the missing datum

Use the actual family and conventions of
[the all-level operator theorem](all_level_a_period.md) and
[the normal-period theorem](peripheral_normal_period.md):

    q_N=exp(pi*i/N), Q_N=q_N^2, Y=M^2,
    F_N(1)=K_N,
    F_N(Q_N^j)=C_j(q_N), 1<=j<N.

For each FIXED j, C_j(q) is the specified Laurent-polynomial
ordinary-color period, C_j(1)=1. The exact all-level recurrence,
its actual finite initial window and its bounded quantum jets
determine K_N uniquely. The
[Mellin theorem](mellin_cyclotomic_jet_uniqueness.md) strengthens
this to the entire rational root section with its pole lattice.

There is consequently no freedom to alter the knot period while
keeping those exact data. The unresolved assertion is that this
unique anchored object has the required selected regulator
character. Uniqueness cannot be converted into existence of a
regulator comparison without producing a candidate satisfying
the original source, lattice and quantum-normal equations.

## 2. Fixed algebraic coefficients have polynomial size on a fixed-color arc

Put t=1/N and retain the root source coordinates (t,Q,Y) on the
central slice U=Y^N=1. Let E be a fixed finite FIELD extension
of k(t,Q,Y), k a fixed embedded characteristic-zero field. A
specified finite residue-field mark and an etale selected place
can be retained. Let a be a nonzero element of E, regular on
the marked chart where the arc is tested.

For all sufficiently large FIXED positive integers j, every
specialized conjugate of a on

    gamma_j(t)=(t,exp(2pi*i*t),exp(2pi*i*j*t))      (1)

has upper and lower polynomial bounds at t=1/N, for all large N.
The required lower bound on j depends on the fixed presentation
of a, not on N. In particular it cannot be exponentially small
or zero at infinitely many large levels.

Here is a direct proof, including the possible vanishing issue.
Choose a polynomial relation for a with nonzero constant and
leading coefficients, clear all denominators, and consider each
nonzero coefficient P(t,Q,Y). Write

    P=sum_(r,s) p_(r,s)(t) Q^r Y^s.

Let A be the span of its Q exponents. For j>A the integers
r+js belonging to different collected pairs (r,s) are distinct.
Thus

    P(gamma_j(t))=sum_(r,s) p_(r,s)(t)
                                      exp(2pi*i*(r+js)t)

is not identically zero. Independence follows by successively
applying the constant-coefficient operators
partial_t-2pi*i*(r+js), with powers exceeding the polynomial
degrees, to isolate one exponential. A nonzero resulting
analytic germ has finite vanishing order at t=0. Apply this
to the finitely many relation coefficients. Cauchy's root bound
and the same bound for the reciprocal polynomial give

    c N^(-B)<=|a_(i,N)|<=C N^B.                  (2)

The proof is uniform over all roots of the selected relation.
It does not assume bounded absolute cyclotomic degree or heights.

In particular, the complete figure-eight scalar itself cannot
be a fixed algebraic function of (t,Q) on a finite cover: (2)
would give zero exponential rate, contradicting (3) below.
This does not exclude a fixed algebraic connection or torsor
with a transcendental marked horizontal period. Its irregular
regulator character must be retained before applying algebraic
coefficient rigidity.

For algebraic sections on a finite integral shape cover, apply
the argument to a fixed nonzero norm or a polynomial relation
on the selected irreducible component. Clearing actual poles
must precede specialization. A statement about a fixed algebraic
section is much stronger than algebraicity at each separate N.

## 3. An original-source obstruction to a regular central-fibre comparison

Take the ORIGINAL figure-eight knot. The independently proved
[whole-source identity](figure_eight_whole_source_identity.md)
gives

    lim_(N->infinity) N^-1 Log|F_N(1)|
                              =Vol(4_1)/(2pi)>0. (3)

For every fixed j>=1, the SAME family and SAME original cap give

    F_N(Q_N^j)=C_j(q_N)->1.                       (4)

No normalization, operator or source was changed between (3)
and (4). Both arcs approach (Q,Y,U)=(1,1,1), and U=1 on both.
More literally, the actual pivot has
g_k(M)=M^(1-N)g_k(1). On these unit-meridian arcs its change
is a specified common unit for every closed head. Moving that
unchanged factor into its retained external line leaves the
same numerical cut functional. Thus this growth contrast does
not hide an independently chosen co-source.

Suppose a proposed whole geometric comparison on the raw
central fibre had the form

    F_N(Y)=a_N(Y) G_N(Y)+R_N(Y),                  (5)

where a is a nonzero section of the fixed algebraic type in
Section 2. Suppose on every fixed-color arc (1) its geometric
period and remainder satisfied, for a common V>0,

    N^-1 Log|G_N(Q_N^j)|->V,
    |R_N(Q_N^j)|<=exp(N(V-delta_j)), delta_j>0.   (6)

Then (5) is impossible. Choose a fixed j larger than the
presentation bound of Section 2. Its a_N(Q_N^j) is nonzero and
polynomially bounded above and below. Equations (5)--(6), by
the reverse triangle inequality, give positive exponential
growth on that arc, contradicting (4).

Equivalently, if bounded ordinary-color values force the
coefficient to vanish on EVERY fixed-color arc, the exponential
separation proof in Section 2 forces its algebraic restriction
to the raw central fibre to vanish identically. It cannot then
give the nonzero complete value by ordinary regular evaluation.

This excludes a tempting shortcut: a uniform dominant geometric
block with a regular algebraic scalar coefficient on that fibre.
It does NOT exclude a source-preserving normal extension, a
nonregular meridian lattice, or cancellation between blocks
with the same exponential size. The latter possibilities are
precisely data which raw algebraic point rigidity does not fix.

### The original divided source explains the necessary distinction

The exact actual source is already known to use the normal
extension. With U=Y^N and t_mu=U-1, set

    Y_r(t_mu)=Q_N^r(1+t_mu)^(1/N),
    v_N(t_mu)_r=(Y_r(t_mu)-1)F_N(Y_r(t_mu)).

Then the unconditional original state identity is

    K_N=N e_0^*[t_mu^1]v_N,

whereas the central state v_N(0) contains only the polynomially
bounded ordinary-color row. The source has degree minus one;
it is not ordinary evaluation of the lowest state degree.
See [the source-adapted filtration](source_adapted_leading_filtration_and_actual_scale_test.md).

The elementary expression

    (U-1)/(Y-1), U=Y^N,

likewise vanishes at every proper root-orbit point and has
complete whole-germ value N. It is not a regular function on
the raw two-variable fibre U=1 at Y=1. This illustrates the
required divided lattice; it does not define a replacement
invariant or prove its regulator coefficient is nonzero.

Thus the actual source-anchored example supports the user's
normal-torsor viewpoint, while ruling out its regular scalar
version on the unextended central fibre.

## 4. The explicit Kummer period has growing ambient rank

For an odd prime p the actual one-variable cyclic cover is

    C_p: y^p=product_(j=1)^(p-1)(1-Q_p^j t)^j.

It is connected. Its p-1 finite branch points have ramification
index p, since each j is coprime to p. Infinity is unramified:
the polynomial degree p(p-1)/2 is divisible by p. Counting the
Euler characteristic of the punctured p-sheeted cover and
filling its ramified points gives

    2-2g=p*2-(p-1)*(p-1),
    g=(p-1)(p-3)/2.                               (7)

The growth persists in the particular nontrivial deck character
used by y^-1 dt. Remove the finite branch points from the base
sphere. It retracts to a graph with one vertex and p-2 loops.
In any nontrivial deck-character component the covering graph
chain groups have dimensions 1 and p-2, and its boundary map
has rank one: a branch generator acts by a nontrivial p-th root.
Hence that character's H_1 has dimension p-3. Filling the
ramification points changes only the trivial character, because
each such point is deck-fixed. Therefore

    dim H_1(C_p)_chi=p-3                           (8)

for every nontrivial character chi, including the selected one.

The small-circle source has an additional important feature.
Removing the p preimages of t=0 adds one boundary-circle
dimension to each nontrivial character. The original selected
circle projects into that canonical one-dimensional boundary
subspace. Thus growing ambient rank DOES NOT rule out a
smaller selected period object. It does show that fixed variable
count alone has not constructed such an object uniformly in p.

In particular the compact C_p cannot all be the smooth proper
fibres of one fixed finite-type algebraic curve family on finitely
many strata: their genus is unbounded. A fixed selected torsor
must be a genuinely constructed reduction or comparison, not
an automatic consequence of the displayed Kummer equations.

## 5. What a successful rigidity certificate would now have to contain

The existing
[whole-comparison rigidity theorem](whole_period_cyclotomic_rigidity.md)
can promote bounded algebraic quantum-jet identities to an exact
whole comparison. The existing
[critical-source theorem](irreducible_critical_source_and_whole_norm.md)
can then force every geometric coefficient nonzero from an
irreducible descended critical line and a nonzero exact source
moment, or from a faithful trace realization. Fixed algebraic
coefficients automatically have polynomial norms on the root arc.

Those theorems would remove a separately assumed nonzero
geometric weight. Their inputs are substantive and finite:

* a fixed algebraic comparison space or an explicitly bounded
  selected quotient of the actual Kummer/quantum object;
* the source-normal pairing, its meridian pole lattice and its
  quantum-normal connection retained by that comparison;
* an actual descended critical line/observable with its exact
  source moments, rather than only a classical shape field;
* control of the TOTAL compact remainder after that projection.

The first three have not been supplied for the selected knot
period. The new exact cut construction supplies the original
cycle, and its infinity bound removes a real global escape
obstacle. It does not make their fixed algebraic reduction or
critical source moment automatic. Equations (3)--(4) show why
that reduction must retain the divided source before passing
to a central or associated-graded fibre.
