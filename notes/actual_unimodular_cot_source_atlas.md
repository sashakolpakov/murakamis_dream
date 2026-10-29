# Exact cotangent source atlases and their universal-transport limitation

28 October 2026. The TU pulling atlas of the ORIGINAL physical source
has a finite compatible residue implementation, with explicit fixed
integer coefficients and no exponentially conditioned chart adapter.
Elementary cotangent changes retain calculable side currents. Artificial
chart divisors cancel in their complete aggregate.

There is an essential limit: these are UNIVERSAL identities on every
holomorphic test function. Such identities cannot move the whole source
to a cycle on which the completed original state is smaller than its
largest physical lattice value. This follows from a direct holomorphic
hull argument below, and does not require an unproved knot example.
Thus the atlas solves an algebraic source-coordinate problem, not the
state-specific cancellation needed for the sharp volume bound.

## 1. The exact original source functional

Fix a nonempty one-component signed braid with m crossings, put
r=m+1 and d=N-1, and keep its actual integral coordinates
u=(t,k_1,...,k_m). Let

    Lambda_N=dP intersect Z^r,
    T_N(f)=sum_(n in Lambda_N) f(n).                 (1)

Here P is the physical polytope in
[the physical-face proof](actual_physical_face_outward_action.md).
The cardinal-completed original scalar F_N is holomorphic on the
specified O(N) complex box D, equals the EXACT original state at each
valid n, and vanishes at every invalid integer state in the box.
The complete original invariant is chi_N/N times T_N(F_N), with
kappa, pivots, half-Cartan and every conversion phase inside F_N.
No scalar line is altered below.

Let kappa_0(s)=1/(1-exp(2*pi*i*s)); this symbol denotes a cotangent
kernel, NOT the original crossing scalar kappa. At an integer n its
residue is -1/(2*pi*i). Thus, on a sufficiently small product torus
Gamma_n around n,

    integral_(Gamma_n) f(u) product_i[-2*pi*i*kappa_0(u_i) du_i]
                     /(2*pi*i)^r=f(n).             (2)

The same is true with product_i pi*cot(pi*u_i) du_i. Exactly,

    pi*cot(pi*s)=-2*pi*i*kappa_0(s)+pi*i.           (3)

Every term in the difference of these PRODUCT kernels lacks at least
one coordinate pole and integrates to zero on the FULL small torus.
These terms are not zero on arbitrary partial chart chains. If (3)
is used on a partial domain, its explicit 2^r-1 lower-pole terms
are retained as source currents.

The original finite source is therefore the coherent middle-dimensional
cycle sum Gamma_Lambda=sum_n Gamma_n with either COMPLETE kernel.
It has at most N^r local components. No norm estimate on F_N is used.

## 2. Finite compatible affine-unimodular charts

The proved pulling triangulation gives finitely many cells

    u=d v_j+B_j y, y in d*Delta,
    B_j in GL_r(Z),                                 (4)

with their number and matrices depending only on the fixed diagram.
Assign shared lattice faces once using a fixed half-open convention.
Let Lambda_j be the resulting disjoint partition of Lambda_N.
This is a partition of the ORIGINAL finite states, not a new source.

Put A_j=B_j^(-1). Since d v_j is integer and A_j is unimodular,
the joint poles of the new chart kernel are the SAME integer lattice.
For each n in Lambda_j take

    Gamma_(j,n)=n+A_j^(-1) T_epsilon,
    omega_j=(-2*pi*i)^r det(A_j)
                    product_i kappa_0((A_j u)_i) du_1...du_r. (5)

The affine translation in (4) is harmless by INTEGER periodicity;
no exponential monomial multiplier has been canceled. The induced
orientation in (5) retains its determinant +/-1. The ordinary
multivariate Cauchy residue calculation gives exactly

    integral_(Gamma_(j,n)) f omega_j/(2*pi*i)^r=f(n).

Consequently

    T_N(f)=sum_j integral_(sum_(n in Lambda_j) Gamma_(j,n))
                                      f omega_j/(2*pi*i)^r. (6)

This identity is valid for EVERY f holomorphic near these cycles and
their enclosed local polydiscs. All coefficients are one, all counting
Jacobians are one, and it is the exact original functional (1).

There is a simultaneous quantitative initial-cycle construction.
Collect the finite integer row forms appearing in all chart matrices
and in the elementary side currents of Section 3. Choose small radii
epsilon_1 >> epsilon_2 >> ... >> epsilon_r with ratios less than
1/(4rC), where C bounds their integer coefficients in any chosen
chart. Choose epsilon_1 so every linear form has modulus below 1/4.
Its FIRST nonzero term then dominates the remaining terms, so every
such form has modulus at least a fixed positive multiple of epsilon_r
on the corresponding hierarchical torus. It cannot hit an integer.
These radii depend on the diagram, not on N or n.

All source kernels and chart Jacobians on this initial atlas are
bounded by diagram constants. Its total logarithmic/Euclidean mass
is O_word(N^r). This is a polynomial INITIAL mass bound, not a bound
for an unconstructed global steepest-descent deformation. The union
may still pass near individual large state values.

## 3. Explicit elementary side-current algebra

Write x,y for two affine integer row forms. Their integer constants
do not affect the periodic kernels. The exact identities are

    kappa_0(x)kappa_0(y)
       =kappa_0(x+y)kappa_0(y)
                    -kappa_0(x+y)kappa_0(-x),

    kappa_0(x)kappa_0(y)
       =kappa_0(x-y)kappa_0(y)
                    +kappa_0(x)kappa_0(y-x),

    kappa_0(-x)=1-kappa_0(x).                     (7)

For example they follow immediately, with all terms retained, from

    kappa_0(x)kappa_0(y)
       =kappa_0(x+y)[kappa_0(x)+kappa_0(y)-1].

The first line changes the first row from x to x+y and leaves y;
the second changes it from x to x-y. The extra product is an
EXPLICIT side-current kernel in another unimodular basis. A sign
change has the displayed lower-pole current. A row swap only changes
the recorded coordinate orientation. Multiplying by all spectator
kernels gives the r-dimensional identities without hidden factors.

Factor each fixed GL_r(Z) chart matrix into unit row shears, row
swaps and sign changes. This is constructive integer elimination.
Follow just the intended main basis through this fixed sequence;
at each step retain its one extra kernel from (7). Telescoping gives

    K_reference=c_main K_chart+sum_n c_n K_side,n,  (8)

where every c is +1 or -1, and every side kernel is specified by
that step. The number of terms is at most the number of steps plus
one. It is independent of N. The ordinary powers of 2*pi*i and all
determinants in converting (8) to normalized forms are fixed diagram
constants. Products of lower-pole terms from (3) are also explicit
and finite. None is silently declared source-null on a partial cycle.

The side currents can carry the ENTIRE selected residue. Already
in two local variables, the leading Cauchy identity is

    1/(xy)=1/[(x+y)y]+1/[x(x+y)].                  (9)

On |x|<<|y|, the first right-hand term has integral zero, the
second integral one, while the left integral is one. Thus retaining
only the main new chart fails even for f=1. This is not an
exponentially large adapter; it is a compulsory unit source current.

## 4. Aggregate cancellation and its exact chain qualification

Equations (7)--(8) are pointwise meromorphic identities. In any
common compact domain remove the SAME small tubes about the union
of all appearing chart divisors. Apply Stokes on the remaining
chains, retaining every tube boundary and every partial-chart side
prism. Sum the kernels BEFORE taking the tube limit.

At a divisor artificial to the reference kernel, every principal
part cancels exactly in that aggregate. The same is true at dependent
intersections: on each common regulator boundary the sum IS the
reference meromorphic form, so it is not necessary to pretend that
the individual singular currents have independent limits. Original
coordinate divisors remain genuine source divisors and retain their
original residues. No physical point is deleted by (8).

This proves tame gluing on any PROVIDED compatible common chain
homotopy. If neighboring chart homotopies have the same embedded
interface with opposite induced orientations and the same regulator,
their full side-current sums agree with the reference form and cancel.
No exponential chart-change coefficient is introduced. On regions
whose distances to all appearing integer hyperplanes are at least
N^(-A), every kernel is bounded by N^C: globally

    |kappa_0(z)|<=C[1+dist(z,Z)^(-1)].             (10)

In a fixed O(N) real box there are O_word(N) parallel translates
per row form, hence polynomially many arrangement cells in fixed
dimension. Piecewise-linear common chains with polynomial complexity
therefore have polynomial source-kernel overhead.

What is NOT proved is that separately chosen descending chart cycles
have compatible interfaces or that their remaining side currents have
small phase. The local identity does not construct that homotopy.
Replacing each chart by an independently convenient contour and then
omitting the difference currents is invalid. In fact there is a
general obstruction to closing that gap by UNIVERSAL cot algebra alone.

## 5. Universal source rewrites cannot lower the state maximum

Let D be a complex domain, Lambda a finite nonempty set in D, and
w_p nonzero fixed complex weights. Suppose a compact union C of
contours and finite complex source measure mu satisfy

    sum_(p in Lambda) w_p f(p)=integral_C f dmu       (11)

for EVERY holomorphic f on D. Each p belongs to the O(D)-holomorphic
hull of C. Here is a direct proof, independent of any source model.

If p is outside that hull, choose a holomorphic g with
|g(p)|>sup_C|g|. Choose an ordinary polynomial L_p equal to one at p
and zero at every other point of Lambda; for instance interpolate a
generic linear coordinate separating the finite set. Apply (11) to
f=L_p g^k. The result is

    |w_p| |g(p)|^k
       <=||mu|| sup_C|L_p| (sup_C|g|)^k,

which is impossible as k tends to infinity. Therefore, for EVERY
holomorphic F on D,

    max_(p in Lambda)|F(p)|<=sup_C|F|.             (12)

The conclusion holds for any finite number of chart cycles and
kernels: combine their measures on their union. It still holds if
the cycle was chosen after inspecting F, provided the resulting
source identity remains valid for all holomorphic test functions.
No polynomial-versus-exponential estimate is needed for this
obstruction; finite total variation is enough.

All constructions in Sections 1--4 are universal in this sense.
Thus they cannot, by themselves, produce a low-|F_N| source cycle
below a larger original lattice summand. An ordinary homotopy in
the complement of every genuine integer source divisor is an even
more restrictive instance: it separately preserves each Cauchy
evaluation. Rewriting the cotangent form does not defeat that issue
while its full test-function functional is preserved.

The issue occurs in the actual model: the independently derived
[signed Markov source family](actual_cotangent_homology_and_global_gluing_criterion.md)
keeps the SAME hyperbolic knot and normalized period while each
additional alternating-sign stabilization adds v_8/(2pi) to one
valid original state's exponential rate. Its complete original
pivotal traces are checked directly. Exact normalization pruning
evades this family by composing the ACTUAL source cell first; it is
not an identity on arbitrary multipliers of each intermediate state.

This does NOT forbid a sharp upper bound for the original scalar.
That bound concerns cancellations among the values of the PARTICULAR
original F_N. Exact q-binomial fusion, Hopf-Ward equations and matched
normalization cells can relate those values in ways invalid for an
arbitrary holomorphic multiplier. Such an operation can change the
individual-evaluation source homology while preserving its actual
scalar. Pure coordinate changes and the universal algebra (7) do not.

## 6. Result and the precise outstanding step

The original finite residue functional has a finite affine-unimodular
atlas, polynomial initial mass, explicit fixed-coefficient side
currents, and exact aggregate cancellation of ARTIFICIAL cotangent
divisors. These statements include its complete original source.

A global phase-small cycle does not follow. Beyond choosing compatible
interfaces, one must use an ORIGINAL-STATE-specific Ward/fusion
identity to recombine genuine evaluation residues. The transport must
then control the resulting full currents. A construction that stays
universal on all holomorphic test functions cannot accomplish that
step, by (12). This is a mathematical limitation of that proposed
route, not a claim that the volume conjecture is false.

[Supplementary audit](../experiments/audit_actual_unimodular_cot_source_atlas.py)
checks the exact shear algebra, compulsory unit side current and
whole original source reindexing in fixed affine-unimodular charts.
