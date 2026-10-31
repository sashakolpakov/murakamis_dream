# Positive angle majorants: half-period gluing and the affine source charge

28 October 2026. Failure of a bare 2-to-3 identity does NOT disqualify
the positive angle-factorial partition function as an upper comparison.
For a fixed complete geometric triangulation its already proved
exponential rate is the desired one, and fixed constants or polynomial
measure corrections have zero exponential rate.

There is a constructive distinction between the N-clock and the FULL
2N-clock q=exp(pi*i/N). On STRICT angle support, the full clock already
forces the geometric edge lift by positivity and the total-angle
identity. A second lemma shows that the AFFINE charge d=N-1 removes
all winding aliases even on weak nonnegative support, provided the
full clock selects edge residue 2d. The resulting positive norm has
the sharp geometric upper exponent.

These are genuine bounds for the stated angle tensors. An exact map
from the full original source to those tensors has not yet been
proved. A weak sum-N angle tensor, with zero angles permitted, does
retain an exponentially excessive winding face even with the full
2N-clock. That is the precise boundary scope of the obstruction below;
it must NOT be applied to the strict-support lemma.

This does NOT disprove a subexponential upper comparison for the FULL
original Kashaev scalar. No nonzero original-source coefficient is
assigned to the bad winding. Such a comparison remains possible if
the actual source removes or cancels it before positivity is taken.

## 1. The correct normalization for an upper comparison

For a fixed complete positive ideal triangulation T let

    w_N(k)=product_i s_N(k_i)^(-1),
    s_N(a)=product_(j=1)^a 2sin(pi*j/N),

and let P_N be its strict integral angle structures: each tetrahedral
triple sums to N and each global edge sums to 2N. The positive model
is Z_N(T)=sum_(k in P_N)w_N(k). On its allowed lattice progression,

    (pi/N)log Z_N(T)->Vol(M).                       (1)

This is the independently proved positive-volume theorem in
[the comparison note (historical context omitted)](quantum_a_volume.md).
The desired upper comparison is

    |K_N|² <= exp(o(N)) Z_N(T),                     (2)

or equivalently |K_N|<=exp(o(N))sqrt(Z_N(T)). The square root is
essential: Z has the ENERGY rate Vol/pi, not the amplitude rate
Vol/(2pi). Any unchanged full peripheral/dimension line multiplies
both sides with its exact square modulus; at the marked complete
point the known such lines have polynomial magnitude and do not
change (1). They cannot remove an exponential gap.

For a fixed T, (1) means (2) is equivalent, on that progression,
to the sharp original-source exponential upper bound. Merely knowing
(1) does not prove (2); the nontrivial input must be an independent
source-preserving comparison. Conversely, a finite move multiplier
8, N, or any fixed-degree boundary unit is not an obstruction to (2).

## 2. Exact positive Fourier gluing gives a different norm

Let H_N have orthonormal basis indexed by

    k_i in{0,...,N-1}, each tetrahedral triple summing EXACTLY to N.

Zero angles are allowed in this finite vector space, because
s_N(0)=1. The forbidden all-pi triple would require an entry N and
is absent. Define the positive vector

    v_N=sum_k sqrt(w_N(k)) |k>.

Let E be the actual integral edge-angle incidence matrix and mu,nu
the marked peripheral angle rows. The geometric projection P_geo,
with peripheral restrictions included, is the diagonal orthogonal
projector onto

    E k=2N*1, mu k=nu k=0.                         (3)

Write P_geo^edge for the projector imposing ONLY E k=2N*1. One
may impose the same EXACT peripheral restrictions on both sides of
a comparison, or omit them on both. No modular-to-exact peripheral
conclusion is used below. On the strict
coordinates its squared norm is the corresponding positive angle
partition. Allowing zero angles on the SAME integer fiber still
has maximum volume at most Vol(M), by the same continuous concavity
argument; zeros alone are not the problem.

Now use the finite root Q=exp(2pi*i/N), as in the actual quantum
Fourier transform. The character average on a constraint row c is

    (1/N)sum_(r=0)^(N-1) Q^[r(c k-bN)]
       =1 if c k=bN modulo N, and0 otherwise.       (4)

It sees no difference between b=0,1,2. Multiplying (4) over the
edge and peripheral rows gives the orthogonal projector P_cyc onto

    E k in N Z^edges, mu k,nu k in N Z.             (5)

Hence an INDEPENDENT finite-Fourier/Plancherel gluing of these positive
angle tensors gives exactly

    ||P_cyc v_N||²
       =sum_(k satisfying5) w_N(k)=:Z_N^cyc(T),
    P_geo<=P_cyc.                                 (6)

This is an equality of positive Hilbert-space norms. Replacing this
N-clock cyclic projector by the exact geometric projection decreases
the norm; it is not an automatic upper-bound operation. A unitary
Fourier change of basis does not alter this projection order.

### 2.1 The FULL 2N-clock is sufficient on strict support

For a cusped ideal triangulation with torus cusps, the edge count
equals the tetrahedron count t. Each quad angle is counted twice in
the sum of all edge incidences, so for every tetrahedral sum-N state,

    sum_edges (E k)_e=2Nt.                         (6a)

The full q-character average is

    (1/(2N))sum_(r=0)^(2N-1) q^[r((E k)_e-2N)]
        =1 iff (E k)_e=0 modulo2N.                (6b)

On STRICT support every edge sum is positive. Equation(6b) then
makes every edge sum at least2N. Their total is exactly2Nt and
there are t edges; hence EACH sum is exactly2N. Consequently

    P_(2N-edge-cyclic)=P_geo^edge
                         on strict angle support. (6c)

The equality remains true after imposing the SAME exact peripheral
restrictions on both sides. The sum argument does not upgrade
modular peripheral conditions to exact ones. Thus one does not need
a separate EDGE integer-lift projector if an original-source
comparison retains both the full 2N edge character and strict angle
support. This conclusion is constructive and independent of a local
Pachner equality.

### 2.2 The affine d-charge is stronger, including at zero angles

There is an equally useful variant matching the original reflected
trivalent source equation h0+h4+h2=d=N-1. Suppose nonnegative angle
indices satisfy tetrahedral sum d, and the full q-character selects

    (E k)_e=2d modulo2N at EVERY edge.             (6d)

The least nonnegative representative of 2d is 2d, strictly positive
for N>=2. Each edge sum is therefore at least2d, while their total
is exactly2dt. Since the number of edges is t, all sums MUST equal
2d, even if some individual angles vanish. No bad winding sector
survives. This is a finite support identity, not an asymptotic claim.

Let Z_N^aff be the positive factorial sum over this nonnegative
sum-d/full-clock space. Then

    Z_N^aff <=N^C exp[N Vol(M)/pi]                 (6e)

for a fixed triangulation-dependent C (and trivially if the set is
empty). Indeed k/d is an exact weak geometric angle structure.
The geometric volume bound gives sum_i Lambda(pi*k_i/d)<=Vol(M).
The uniform modulus of continuity

    |Lambda(x)-Lambda(y)|
        <=C |x-y|(1+|log|x-y||)

follows by integrating its two logarithmic endpoint singularities.
Since |k_i/N-k_i/d|<=1/N, it changes the volume by O(logN/N).
The uniform sine-factorial estimate then bounds EVERY weight by
N^C exp[N Vol(M)/pi], and there are at most N^(3t) states.
This proves(6e), with the original zero-angle weights retained.

On any allowed nonempty progression for the strict model(1), its
rounding proof gives the quantitative lower bound
Z_N(T)>=N^(-C')exp[N Vol(M)/pi]. Indeed the rounded geometric
angles differ by O(1/N), remain in a fixed strict neighborhood,
and their volume differs by O(1/N); the uniform factorial error is
O(logN). Thus(6e) actually gives Z_N^aff<=N^C'' Z_N(T), and in
particular Z_N^aff<=exp(o(N))Z_N(T). A source-preserving norm map
to THIS affine angle space, of subexponential norm and with the
actual full-clock residue(6d), WOULD give the requested upper
comparison. No lower/survival theorem would be required for that step.

The local actual trivalent d-charge is already established in the
source notes. What is not established here is its global realization
as the tetrahedral angle indices of an arbitrary geometric T, with
the full edge character(6d) after all Fourier/Gaussian/source adapters.

The subsequent [supporting-plane and defect theorem](positive_angle_supporting_plane_and_defect_bound.md)
weakens this target further: O(1) TRUE integer edge-charge errors
cost only a polynomial, and o(N) errors preserve the sharp volume
upper exponent, with an explicit Gaussian deficit. This is not a
statement about bounded changes of residues modulo2N.

## 3. A certified exponential gap on a complete geometric triangulation

Use the actual positive nine-tetrahedron 5_2 triangulation and exact
rational angle vector alpha from
[the previously certified fixture](positive_geometric_alias_volume_counterexample.md).
The new conclusion here is the positive NORM comparison (6), not a
claim about the coefficient of that fixture in the original state.

All entries of alpha lie in[0,19/20], its tetrahedral triples sum
to1, and its actual edge/peripheral rows obey exactly

    E alpha=2*(1,1,1,1,1,1,2,0,1)^t,
    mu alpha=nu alpha=0.                          (7)

For 20|N, k_N=N alpha is therefore a legitimate basis vector in
P_cyc H_N, with BOTH original marked peripheral equations exact.
Its edge sums are even multiples of N, so it also survives the FULL
2N-clock on WEAK sum-N support. It fails the exact geometric edge
lift. The three zero-angle
tetrahedra are flat, and all other tetrahedra are strictly positive.

The exact geometry and outward-rounded dilogarithm evaluation give

    3.76403<V_alias<3.76404,
    2.82812<Vol(M)<2.82813.                        (8)

The uniform sine-factorial estimate, including k_i=0, implies

    log w_N(k_N)=N V_alias/pi+O(log N).

Retaining this ONE nonnegative term in (6), and using (1) along
a common allowed progression, proves the rigorous gap

    liminf (pi/N)log[Z_N^cyc(T)/Z_N(T)]
             >=V_alias-Vol(M)>.93590.             (9)

Here the common progression can be any multiple of20 and of a
denominator of a strict rational geometric angle structure. Such
a denominator exists: rational solutions of the fixed rational
affine equations are dense in their real affine solution space,
and a complete positive point has an open strict neighborhood.
Thus the denominator Z_N(T) is nonempty on that progression.

If peripheral rows are added to the denominator, either it is
nonempty on a further progression and the same upper volume bound
applies, or an attempted all-level comparison already encounters
an empty denominator. For (9) it suffices to use the original
edge-only Z_N(T) of (1).

In amplitude norm the unavoidable loss of this cyclic relaxation
is at least exp[N(V_alias-Vol)/(2pi)+o(N)]. Neither a finite fixed
number of move constants nor any polynomial measure/source factor
changes it. The defect in(7) is O(N), so shifting angle indices by
O(1) to correct N-versus-N-1 conventions also cannot repair it.

This is a triangulation-based positive Gram obstruction for the
WEAK sum-N model, already after exact tetrahedral equations and
both peripheral rows, and even with the full 2N-clock. The strict
alias locus for this particular face is empty: its zero edge forces
three flat tetrahedra. It does NOT contradict(6c) or the differently
charged affine model(6d). It does not rely on an oversized raw
crossing state or on positivity of an unnormalized local pentagon.

## 4. A useful exact local connection, and its limit

For 1<=L<N and0<=a<=L, reflection gives

    s_N(L)s_N(N-L)=2N sin(pi*L/N).

Consequently the modulus of a genuine Gaussian coefficient is
EXACTLY a positive tetrahedral angle weight times a polynomial
factor:

    |[L choose a]_Q|
      =2N sin(pi*L/N)
         /[s_N(a)s_N(L-a)s_N(N-L)].                (10)

The three indices on the right sum to N. Formula(10) applies also
at a=0,L, where the tetrahedron is flat. It connects the original
root-factorial magnitudes to the positive model more directly than
merely sharing the same dilogarithm asymptotic. It can be applied
to the Gaussian blocks AFTER any independently proved exact fusion.

It does not, by itself, prove that the resulting triples have
the complete knot triangulation's GLOBAL edge constraints with the
correct full character and affine residue. A coefficientwise
Cauchy--Schwarz estimate, or a convex majorization of factorial
magnitudes, does not specify those constraints. The full phases and
relative source may supply them. Lemmas(6c),(6d) show that this is
a more concrete sufficient target than independently imposing
unwrapped winding after every Fourier transform.

## 5. What would still establish the requested majorant

The 29 October [length-normalized star and Gram identities](actual_length_normalized_star_gram.md)
now give exact local square-root weights with all normalizers retained.
The [original singleton clock source](actual_length_gauge_clock_source.md)
has polynomial Riesz norm at arbitrary signed braid width. These
establish a genuine original-source Cauchy framework. Its remaining
energy must retain clock interference: [a fully contracted figure-eight
sector](actual_figure_eight_clock_gram_obstruction.md) excludes every
positive diagonal clock metric from the sharp geometric budget.
The desired global Gram can be exponentially conditioned; its actual
source dual norm, state energy, and true angle defects must be bounded
together. The [source-compatible Hermitian reflection](phase_ratio_double_and_fermat_source.md)
provides an exact doubled-word input without selecting its angle support.

The original paired factorial gauge really fixes the complete
cup/cap source, and the existing
[weighted Fourier theorem](actual_weighted_fourier_plat_energy.md)
retains the compulsory dual metric. It does not presently produce
a map from the full original source to the strict or affine angle
space above for an arbitrary positive geometric triangulation.
The normalized finite Fourier transform supplies a SPECIFIED modular
character, so its modulus and affine residue matter. The dual metric
cannot be silently flattened.

Nor does merely remembering that the scalar q has order2N prove
that the source map implements(6b) or(6d). For instance, on the
N-dimensional cyclic head let S|a>=|a+1 moduloN> and T|a>=q^a|a>.
Then exactly

    T S-q S T=2|0><N-1|.                          (11)

The strict nilpotent shift has no such wrap term. Thus changing an
N-cyclic clock to a half-period clock while dropping its endpoint
current is not an exact basis change. The subsequent
[source-exact half-clock dilation](actual_half_clock_source_dilation.md)
now supplies a faithful 2N ambient physical window: its weighted
E/F shifts, genuine dual turns, original N-normalization, unrolled H,
half-Cartan, pivot and selected one-component cut are all retained.
It legitimately permits a unitary 2N Fourier transform of the FULL
original physical network. This does not replace an auxiliary
unweighted N-cyclic atom shift by the 2N shift X. Its exact lift is
S_hat=X(I-P_wall)+X^(1-N)P_wall, with P_wall the two top-window
projectors, and it retains
T S_hat-q S_hat T=-2q X^(1-N)P_wall T. Only the weighted E/F endpoint
zeros remove their corresponding wrap terms. What remains to be proved is its map
to geometric tetrahedral angle indices and the GLOBAL edge
characters(6b) or(6d); physical degree conservation alone does not
identify those characters. The unrolled half-Cartan and source
signs must still be transported through that angle-coordinate map.

The local pointed tetrahedron gives a useful nonarbitrary charge
check. In the conventions of
[the pointed module](pointed_tetrahedron_gluing.md), for positive
orientation,

    Z0 Z1 Z2=-Q.

Setting zeta_i=q^-1 Z_i gives EXACTLY

    zeta0 zeta1 zeta2=-q^-1=q^d.                   (12)

Thus the d-charge is consistent with the original half-period
ordering, rather than chosen solely to make an optimization work.
The three quad operators do not commute, however, so(12) is not
itself a joint positive angle basis or a full tensor gluing theorem.

There is also a central-sign constraint on transporting this local
rescaling globally. If a chosen edge corner word has valence v_e,
rescaling every corner by q^-1 multiplies that word by q^(-v_e).
For its NEW character to equal q^-2=q^(2d), its OLD character would
have to be q^(v_e-2), in that same specified ordering. But zeta_i^N
=-Z_i^N. For ODD N, every ordinary corner word on the original
geometric central fiber has Nth power1: all Q-commutation factors
have trivial Nth-power correction and the classical edge product
is1. At an ODD-valence edge, the proposed old character has

    (q^(v_e-2))^N=-1,                            (13)

so it cannot simply be imposed on that SAME geometric central
fiber. For example, the initial positive three-tetrahedron 5_2
triangulation has valencies7,6,5. A Weyl/Maslov normalization using
an additional half-period factor, or a transported Frobenius/sign
fiber, could repair this. It must be recorded; it is not supplied
by the local identity(12). This is a necessary sign check, not a
no-go for a properly transported charged state.

In fact the existing pointed edge-module construction leaves
compatible edge characters prescribed but free. Multiplying them
by a mu_N character of the primitive edge lattice preserves the
central data; every compatible edge quotient has its proved rank.
The projected tensor generator and actual ADO source have not been
identified there. Thus that module theorem does not select the
specific global character(6d) for the original source. This is the
exact unresolved global operator/source calculation.

A valid upper proof could instead establish an exact source map
whose image lies on the strict/full-clock or affine/full-clock
fiber just proved sufficient, with a norm bound
exp(o(N)), or prove that all excessive winding channels cancel
as original relative currents with that same cost. Either would
be sufficient for an angle-majorant argument. No lower-bound or
nonzero geometric coefficient would be needed for this UPPER step.

Nothing in the calculation rules out that construction. It identifies
the exact extra statement that is missing from the proposed
Fourier/Plancherel comparison, and proves that it cannot be replaced
by the cyclic positive relaxation in(6).

Reproduction:

```sh
python3 experiments/audit_positive_angle_majorant_winding.py
```

The script independently checks the projector character identity,
the exact rational full marked angle data, the certified volume gap,
and(10). It asserts no nonzero original quantum coefficient for the
wrong-winding state and no broad original-source upper bound.
