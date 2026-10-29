# A polynomial-cost critical-value upper bound for two-anchor source cores

28 October 2026. A genuine minimax deformation is available for any
two-anchor residual core of the actual unit-factor source. Its original
coefficient is bounded by its largest regular critical modulus times an
explicit polynomial in its degree. No positivity, accessible highest
saddle, nonzero thimble coefficient, or lower bound on critical values
is assumed. This is an upper bound only.

It does NOT prove the knot upper bound. These anchor critical points
are conditional on the remaining integer clocks; they are not
automatically FULL critical points of the knot's coupled phase. The
sharp regulator theorem cannot be applied to them without that step.

## 1. Statement with its original coefficient normalization

After extracting the actual scalar and any monomial factors, a
two-anchor core with strict Hall support has the form

    f(z)=gamma z^(-q) product_(j=1)^m (z-u_j),
    |u_j|=1, gamma!=0, 1<=q<=m-1,
    I=CT_z f(z)=(1/(2*pi*i)) integral f(z) dz/z.    (1)

Here m and q can depend on N. Repeated roots and arbitrarily close
unit roots are allowed. All extracted source scalars remain in gamma.
This is exactly the homogeneous two-anchor coefficient after removing
its common scale. Put p=m-q and

    M=max_(f'(z)=0, z!=0, f(z)!=0)|f(z)|,

with M=0 if the regular critical set is empty. Then

    |I| <=4 m^2 log(m+1) M.                       (2)

In particular m=O(N) gives only polynomial transport cost. If a
separate argument bounds EVERY such full-source critical modulus
by exp(N V+o(N)), (2) would give the same exponential upper bound.
It is not inferred here that these conditional critical values
have V=Vol(knot)/(2*pi).

## 2. The critical-value contour exists without selecting its saddle

Fix R>M. The Laurent polynomial f is a proper finite map from C*
to C: its only poles on the sphere are 0 of order q and infinity
of order p. There is no finite asymptotic value at either pole.
Over {|w|>R}, f has no critical point. Every component of its
preimage is therefore an unramified finite cover of an annulus.
Such a component is an annulus with one end over infinity. It
contains exactly one of the two pole ends. Thus there is one
component around 0 and one around infinity, of degrees q and p.

The finite boundary Gamma_R of the component around 0 is a smooth
closed level curve |f|=R. It winds once around 0, and so represents
the ORIGINAL positive generator in (1). This proves

    |I| <= R/(2*pi) integral_(Gamma_R)|dz/z|.       (3)

The assertion is not that the source reaches every critical point.
The contour uses a level above all critical values; an inaccessible
highest point is entirely compatible with (3).

For completeness the annular-cover statement can be read locally
and topologically. A connected finite cover of the punctured disk
at infinity corresponds to a finite-index subgroup of Z, hence is
again a punctured disk. Filling its puncture adds one pole. It
cannot contain both poles or a third component without a pole.
Its regular level boundary is an embedded circle. No transport
norm has yet been assumed; it is estimated next.

## 3. A uniform logarithmic length estimate

The level equation is a real algebraic curve of degree 2m:

    |gamma|^2 product_j |z-u_j|^2-R^2 |z|^(2q)=0.

Every radial ray meets it at most 2m times: along a fixed ray it
is a nonzero real polynomial of degree 2m in the radius. Every
circle meets it at most 2m times: the restriction is a nonzero
trigonometric polynomial of degree m. It cannot vanish identically
on a circle, since its highest harmonic has the nonzero product
of the leading and constant coefficients of product(z-u_j).

The elementary one-dimensional coarea/total-variation count therefore
gives, writing r_min,r_max for the extreme radii of Gamma_R,

    integral |dArg z| <=4*pi*m,
    integral |d log|z|| <=2m log(r_max/r_min).

Since |dz/z|<=|dArg z|+|d log|z||,

    integral_(Gamma_R)|dz/z|
                      <=4*pi*m+2m log(r_max/r_min). (4)

These are bounds on a single component by the number of intersections
of the whole level curve. Tangencies affect a set of measure zero
and do not invalidate the total-variation estimate.

## 4. Unit roots prevent an exponential transport constant

Put A_+(R)=max(0,log(R/|gamma|)+m log2). For |z|>=2,

    |f(z)|>=|gamma| 2^(-m)|z|^p,

and for |z|<=1/2,

    |f(z)|>=|gamma| 2^(-m)|z|^(-q).

Hence on the level curve

    log(r_max/r_min)
                <=2log2+A_+(R)(1/p+1/q).           (5)

This does NOT require a lower bound on M/|gamma|. If that ratio
is extremely small, the positive-part expression clips to zero
once its logarithm is below -m log2. Root clustering causes no
hidden log(1/M) transport factor.

The exact two-anchor critical-flow equation bounds every regular
critical radius between 1/m and m; it is the two-vertex case of
[the cut maximum principle](charged_critical_flow_and_chambers.md).
It also follows directly by comparing the real parts of
sum_j z/(z-u_j)=q inside and outside the unit circle. Thus, for M>0,

    M/|gamma| <=(m+1)^(2m).

Take R down to M in (3)--(5), without deforming through the
critical level. Since 1/p+1/q<=2,

    |I|/M <=2m+(m/pi)[2log2+2(2m log(m+1)+m log2)]
                                             <=4m^2 log(m+1).

This proves (2). If M=0, use any R>0 and let R decrease to zero
in the same estimates; the bounded positive-part expression gives
I=0. The proof is uniform in the unit-root positions and their
multiplicities, with no assumption of a fixed saddle Hessian.

## 5. The precise higher-dimensional issue

The one-variable proof uses a proper map C*->C. A Laurent polynomial
on a torus of dimension at least two is generally NOT a proper map
to C, even when every ordinary critical radius is bounded. Nonzero
finite asymptotic values and critical values on boundary restrictions
must be included before repeating the annular fibration argument.
In the original source these are not removed merely by saying the
torus generates its absolute homology.

The [exact cut/flag jets](charged_source_cut_jets.md) retain coordinate
boundary currents and bound their small-deficit normal cost. They do
not bound the remaining core periods or force a constrained boundary
stationary point into the saturated genuine critical variety. The
[critical regulator compactification](saturated_critical_regulator_compactification.md)
controls limits of FULL genuine critical points, not arbitrary such
restricted boundary points. Those distinctions are essential for
extending (2) to the complete clock-coupled knot period.

Thus (2) supplies an actual polynomial-cost minimax estimate for a
source class to which it applies. The missing general upper-bound
theorem is still to prove that the FULL phase, with all its retained
relative boundary strata, has no larger relevant stratified critical
value. No new knot or broad knot class is proved here.

## 6. A rigorous logarithmic-mass estimate for a prospective global chain

There is one higher-dimensional quantitative step which can be proved
without assuming a controlled gradient flow. Let an oriented real
r-cycle Gamma in (C*)^r be a finite sum of semialgebraic pieces Gamma_a
with integer multiplicities c_a. Suppose each piece is contained in
a real algebraic support whose complexification has dimension r and
degree D_a. Suppose also |log|z_i||<=B on the chain. Then

    integral_Gamma |dlog z_1 wedge ... wedge dlog z_r|
               <=4^r (B+pi)^r sum_a |c_a|D_a.      (8)

Lower-dimensional strata have zero r-dimensional integral. Supports
can be split into their regular pieces without changing their total
degree bound. Singular pieces of full real dimension r require their
own r-dimensional support; an arbitrary algebraic superset of larger
dimension does not satisfy the hypothesis.

Proof. Write dlog z_i=d rho_i+i d theta_i. The absolute r-form is
bounded by the sum of the 2^r real wedge forms obtained by selecting
rho_i or theta_i at every coordinate. For each corresponding
projection, the area formula integrates its absolute Jacobian by
counting fibers. A fixed rho_i imposes the quadratic equation
Re(z_i)^2+Im(z_i)^2=exp(2rho_i); a fixed theta_i imposes one real
linear equation, with an extra ray inequality. At a regular fiber
point these equations cut the complexified r-dimensional support
in an isolated point. Bezout's inequality bounds their number by
2^r D_a. This remains a bound on the isolated points even if an
unrelated positive-dimensional complex intersection is present;
the singular/projection-critical locus has image measure zero.

If s radial coordinates were selected, the projection box has volume
at most (2B)^s(2pi)^(r-s). Sum these bounds over all coordinate
choices and over the chain pieces. The result is

    2^r sum_a|c_a|D_a * (2B+2pi)^r,

which is (8). Angular seams are omitted sets of measure zero and
the absolute-Jacobian count includes all windings.

Consequently an ACTUAL homologous sublevel representative with
polynomial sum|c_a|D_a and polynomial logarithmic radius range would
have polynomial log-form mass. Bounding its exponential integrand
would then give the desired upper estimate without a hidden
exponential transport constant. This is a proved mass lemma, not
a claim that an effective semialgebraic triangulation constructs
that representative. Construction with the original relative source,
and control of its full stratified critical values, remain separate.

[Audit](../experiments/audit_actual_coefficient_minimax_upper.py):
exact source normalizations, complete regular critical sets for root
families including repeated roots, the critical radius and level-radius
bounds, the explicit polynomial prefactor, and the inaccessible-highest
example as a check that an upper estimate does not assert selection.
