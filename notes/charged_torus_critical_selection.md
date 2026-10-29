# A torus generator need not select the highest regular critical value

28 October 2026. The implication

    original source generates H_k((C*)^k)
    + unique highest real regular critical action
    => that critical point contributes

is FALSE for homogeneous polynomial coefficient periods with only
coordinate poles. It remains false when every noncoordinate factor
has a root-of-unity phase and the source is the specified finite-flat
Fermat/nilpotent top coefficient. An explicit example below has a
strict Cauchy bound BELOW its unique highest regular critical value.
Thus its original torus misses that critical point's upward cycle.

These examples are not asserted to arise from an original knot
diagram. They refute an inference from the stated source/topology
properties alone. The actual fixed-diagram clock couplings and root
interval patterns may impose additional restrictions; those would
have to enter a valid knot theorem.

## 1. A completely rational example with an explicit selected limit

Put

    f(z)=z^(-1)+(91/100)z+(9/200)z^2,
    a_n=(1/(2*pi*i)) integral_(|z|=1) f(z)^n dz/z.

The source is exactly the generator of H_1(C*). The form has only
coordinate poles. Its regular logarithmic critical points satisfy

    100 z^2 f'(z)=(z-1)(z+10)(9z+10)=0.

Their values are EXACTLY

    f(1)=391/200,
    f(-10)=-47/10,
    f(-10/9)=-167/90.                                (1)

All are nonzero and nondegenerate. The unique highest real part of
log f is therefore log(47/10), at z=-10, independent of its chosen
logarithmic mark.

But on the ORIGINAL source circle the triangle inequality gives

    |f(exp(i theta))|<=391/200<47/10.

Consequently |a_n|<=(391/200)^n. In fact the strict lower rate is
selected with a nonzero coefficient:

    a_n=(391/200)^n /sqrt(2*pi*n*(418/391))
                                       *(1+O(1/n)).   (2)

Here is an elementary proof. Equality in the circle triangle
inequality requires the phases of exponents -1,1,2 to agree. Their
differences 2 and 3 have gcd one, so equality holds only at theta=0
modulo 2*pi. At that point f'(1)=0, and

    log[f(exp(i theta))/f(1)]
                     =-(418/391)*theta^2/2+O(theta^3).

Its positive quadratic coefficient gives a Gaussian leading term.
Outside any fixed neighborhood of zero the compact circle has a
strict modulus gap. Expanding on a shrinking symmetric neighborhood
gives (2); the odd third-order term integrates to zero at its first
order, and the remaining relative error is O(1/n). No unknown
normalizer or source projection is used. The coefficients are
nonnegative: a_n>0 for every n>=2 because n=2u+3v with u,v>=0.

This already disproves highest-critical-value selection. It is not
merely an exact zero at an exceptional small level.

### The same example has uniform homogeneous source charges

Set

    H(X,Y)=X Y^3+(91/100)X^3Y+(9/200)X^4.

Then deg H^n=4n and

    a_n=[X^(2n)Y^(2n)]H^n.                           (3)

Indeed with z=X/Y, H/(X^2Y^2)=f(z). The normalized product torus
integral in two variables is exactly the original circle integral;
the common homogeneous scale integrates to one. In the source algebra

    A_n=K[X,Y]/(X^(2n+1),Y^(2n+1)),

(3) is its specified top-coefficient functional, normalized by
lambda(X^(2n)Y^(2n))=1. By homogeneous center independence it is also
the same functional on every regular Fermat fiber. Perfectness and
flatness of that source do not make the higher critical value appear.

## 2. A counterexample with unit root-of-unity factors

The previous example did not require unit-modulus linear factors.
That restriction alone does not repair the implication. Put

    P(z)=(1-z^4)^2(1+z+z^2)^3(1-z+z^2),
    f(z)=P(z)/z,
    b_n=CT_z f(z)^n.                                 (4)

All sixteen roots of P, with their actual multiplicities, are roots
of unity of orders dividing twelve. The eight REGULAR critical
points of log f are the roots of the integer polynomial

    G(z)=15z^8-2z^7+11z^6+2z^5+2z^3-3z^2-2z+1.      (5)

Precisely,

    zP'(z)-P(z)
      =(z-1)(z+1)(z^2+1)(z^2+z+1)^2 G(z).

The prefactor accounts for multiple zeros of P, where log f is not
regular. The audit checks gcd(G,P)=1 and that G is squarefree.
Certified complex-root isolation gives:

| Regular critical point | Critical-value information |
| --- | --- |
| real z in (0.59700,0.59701) | f(z) in (7.22573,7.22575) |
| real z in (0.36853,0.36854) | f(z) in (6.82894,6.82897) |
| the other six roots | all critical-value moduli <1.88 |

Thus the first critical point is the UNIQUE highest real-action
regular critical point. Every regular critical point is nondegenerate.
The rational interval root/critical-value certificates are reproduced
with 256-bit complex balls in the audit, not taken from a numerical
plot.

Now use the ORIGINAL source circle |z|=R=1/3. The exact identity

    P(z)=(1-z^4)^2(1+z+z^2)^2(1+z^2+z^4)

gives the elementary uniform bound

    |f(z)|<=R^(-1)(1+R^4)^2(1+R+R^2)^2(1+R^2+R^4)
           =103408396/14348907
           <7.20671<7.22573.                         (6)

Therefore

    |b_n| <= (103408396/14348907)^n.                  (7)

The unique highest regular critical point cannot be the leading
term of this period: its action is separated from (7) by a FIXED
positive amount. No limiting interchange at a pole or infinity is
used. The circle of radius 1/3 is the same positive generator as
every other finite positive source radius.

### Exact cyclotomic and socle format along infinitely many levels

Let P_hom be the degree-sixteen homogenization of P and put

    H(X,Y)=X^16 Y^2 P_hom(X,Y),
    d_n=17n, N_n=17n+1.

Then H^n has total degree 2d_n and

    b_n=[X^(d_n)Y^(d_n)]H^n.                        (8)

Along n=7 mod12, N_n is divisible by twelve. EVERY noncoordinate
linear factor phase of H^n is consequently an actual N_n-th root
of unity. The source is exactly the fixed top-coefficient functional
of K[X,Y]/(X^(N_n),Y^(N_n)), and extends unchanged across its finite
flat Fermat family. All scalar coefficients and coordinate monomials
are retained. Dividing by the original-type tame factor N_n would
not change the exponential gap in (7).

This is still NOT an original braid/knot realization. In particular
the growing multiplicities in powers of this fixed polynomial have
not been identified with a fixed diagram's raw consecutive root
intervals. Its purpose is to show that homogeneous source charges,
unit cyclotomic phases, source flatness and torus topology together
do not imply the asserted selection theorem.

## 3. The exact accessibility obstruction

For either example choose S=log f locally. An upward gradient cycle
from its highest regular critical point has Re S greater than or
equal to that point's critical value. The source circles used above
have STRICTLY smaller Re S everywhere, by (1) or (6). Such an upward
cycle cannot intersect the source torus. This is a direct obstruction
to the proposed nonzero intersection number, not a guessed asymptotic
cancellation between equal-height critical points.

Absolute generation of H_1(C*) does not determine this relative
intersection pairing. The relevant upward/downward cycles have
asymptotic conditions involving zeros and coordinate ends. They are
not all dual to the single absolute torus generator. Source-preserving
radius deformation keeps the period fixed but need not turn it into
the downward cycle of the highest critical point.

Dominant-saddle Stokes persistence therefore needs an initial NONZERO
coefficient of that saddle. It cannot deduce one merely from highest
critical height and absolute torus topology.

## 4. Why a balanced source can behave differently

There is a genuine extra structure in the new
[balanced critical-flow theorem](charged_critical_flow_and_chambers.md).
For a product of unit-modulus binary factors and charges q_i, write
S_i for incidence count, counting a loop twice. At a regular critical
point its exact real equations are

    sum_j (|X_i|^2-|X_j|^2)/|alpha X_i-beta X_j|^2
                                            =-(S_i-2q_i). (9)

When every defect is zero and the underlying graph is connected,
the maximum principle forces all radii equal. The original torus
then does contain every regular critical point after common scaling;
on each chamber its source phase is constant and its log amplitude
is strictly concave. With a separated highest chamber this can force
noncancellation, instead of assuming the geometric thimble coefficient.

The cyclotomic example (8) has exact defects (+14n,-14n). Thus it
does not contradict the balanced theorem. Its coordinate cut deficits
are n and 15n across 16n crossing factors, so neither is sublinear.
The [cut-jet theorem](charged_source_cut_jets.md) retains these
macroscopic jets; it did not claim they were tame or negligible.
Both cuts nevertheless have UNIFORM strict Hall margin 1/16. After
peeling the coordinate monomials, this is a connected residual core
with charges (n,15n). The general radial-compactness inequality therefore
applies with fixed positive margin; all its regular critical radii stay
in a fixed annulus. No escaping regular critical or degenerating cut
margin is needed for the failure of highest-value accessibility.

For the original invariant, showing that the FULL coupled clock/source
selects balanced or otherwise accessible geometric cores is still an
additional theorem. The counterexample does not rule out that theorem.
It rules out deriving it from torus generation alone.

## 5. Exact balance is a real restriction on an alternating source

The first actual source application can be described without knot
census data. Take a nontrivial oriented alternating one-component
diagram, use its charged bridge presentation, and contract ALL original
closure kernels by the proved reproducing law. Every overbridge then
has one encounter. Between consecutive overencounters along the knot
there is exactly one underencounter. The remaining anchors are these
segments; label anchor v by its preceding overevent and let tau(v)
be its next overevent. The permutation tau is one cycle.

At anchor v the preceding overevent supplies output-block length h_v;
the next overevent supplies input-block length d-h_(tau(v)); and its
one underencounter supplies spectator incidence d. The spectator
contribution is the sum of that crossing's two block lengths d-h and h,
independent of its sign. The closure pivots change phases, not degrees.
Consequently the exact ORIGINAL incidence defect is

    S_v-2d=h_v-h_(tau(v)).                            (10)

Thus in this directly closure-contracted alternating presentation,
all defects vanish if and only if every crossing clock has the same
value. Sublinear defects force all normalized clocks to approach the
same value, since the oriented cycle has a fixed number of encounters.
This is not an automatic consequence of alternation.

Equation (10) does not show that this locus is leading, or that it
has zero invariant. Further exact fusions may combine opposite defects
and give a different core presentation. The point is the necessary
scope distinction: a theorem for balanced anchor sectors must still
be connected to the FULL original clock sum, rather than applied
to every alternating source sector without checking (10).

[Audit](../experiments/audit_charged_torus_critical_selection.py):
exact rational example and Gaussian constants, homogeneous charges,
integer critical polynomials, squarefree/nonzero critical values,
certified all-root bounds for the unit-cyclotomic example, and its
strict rational source-circle bound.
It also checks (10) against the actual signed port/closure metadata,
including the exact one-underencounter condition and the oriented
one-component return cycle.
