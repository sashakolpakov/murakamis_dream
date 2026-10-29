# Algebraic volume shapes at every positive-source maximum

29 October 2026. This removes the isolated-complex-critical-point
hypothesis from the algebraicity assertion for positive Conway sources.
It also includes boundary maxima and nonunique optimizers. The nonflat
tetrahedral shapes at the maximum are algebraic. Flat directions can
remain free; they do not change this volume period.

This is a theorem about the actual source's already proved variational
limit, not an identification of its atoms with the complement. The
subsequent [Bloch regulator theorem](actual_positive_source_bloch_regulator.md)
uses this theorem and full constrained stationarity to prove that the
conjugate-antisymmetrized shape sum has zero rational Bloch boundary.
The geometric incidence and full-source transport gaps remain separate.

## 1. A general rational angle theorem

Let P be a nonempty compact rational polytope in a finite-dimensional
real affine space. For finitely many indices j prescribe rational affine
maps

    alpha_j=(alpha_j1,alpha_j2,alpha_j3):P -> closed angle simplex,
    alpha_jr>=0, sum_r alpha_jr=1,

and positive rational weights w_j. Define

    V(x)=sum_j w_j V_ideal(alpha_j(x)).                 (1)

Here V_ideal(a,b,c) is the volume of the positive ideal tetrahedron
with angles pi a, pi b, pi c; its continuous extension vanishes on
the boundary of the simplex. Let M be the nonempty maximum set of
(1), and F the smallest face of P containing M.

**Theorem.** Let I consist of the atoms whose three angles are positive
on the relative interior of F. Then:

1. Every atom outside I is flat throughout F and contributes zero.
2. For each j in I, the complete angle triple is the SAME at every
   point of M. Its phases exp(pi i alpha_jr), and its positive ideal
   shape, are algebraic numbers.
3. The maximizers form exactly the intersection of F with one affine
   fiber of the rational map x -> (alpha_j(x))_(j in I).
4. After choosing rational affine coordinates on the ambient space,
   M contains a point all of whose coordinate phases exp(pi i x_k)
   are algebraic. This does not assert that every optimizer has that
   property, or that the angles themselves are algebraic numbers.

In particular, writing z_j for the common positive shapes,

    max_P V = sum_(j in I) w_j D(z_j), z_j algebraic, Im z_j>0. (2)

No actual triangulation, complete metric, or isolated critical point
is an assumption of this statement. Those are different requirements
for interpreting (2) as a manifold volume.

## 2. Flat atoms and the exact Hessian kernel

Concavity of each atom makes M convex. Choose x_* in the relative
interior of M. It belongs to the relative interior of F. To see this,
each defining inequality of P which vanishes at x_* vanishes throughout
M: otherwise a small segment in M through its relative-interior point
would cross that inequality. These are exactly the equalities defining
the smallest containing face.

An affine angle which is nonnegative on F and vanishes at x_* must
vanish on all of F. Thus an atom with any zero angle at x_* is flat
throughout F. Every other atom is positive on its relative interior.

For a positive atom put c=1-a-b. Its negative Hessian in (a,b) is

    -Hess V_ideal / pi^2
       = [[cot(pi a)+cot(pi c), cot(pi c)],
          [cot(pi c), cot(pi b)+cot(pi c)]].          (3)

Both diagonal entries are positive; for example the first is
sin(pi b)/(sin(pi a)sin(pi c)). The determinant is exactly one,
because cot(pi a)cot(pi b)+cot(pi b)cot(pi c)
+cot(pi c)cot(pi a)=1. Thus (3) is positive definite.

Let T be the rational tangent space of F and put

    K={v in T : d alpha_j(v)=0 for every j in I}.      (4)

On the relative interior of F the negative Hessian of (1) has EXACTLY
kernel K. Indeed it is a positive weighted sum of the positive forms
(3) pulled back by the angle maps. A zero of the sum is a zero of
each form. In particular K is a rational subspace independent of x.

If two maximizers had different angles in an atom of I, their segment
would give strict concavity for that atom and weak concavity for all
others, contradicting maximality. This remains true if one endpoint
is on the boundary: the segment next to x_* is positive, with the
strictly negative second derivative (3). Therefore all angles in I
are constant on M. Conversely any point of F with those same angles
has the same value, since every other atom is flat there. This proves
the exact fiber description in assertion 3.

## 3. Remove the flat kernel before exponentiating stationarity

Choose a rational base point x_0 in the affine hull of F and rational
bases of K and a complementary subspace H in T. Write

    x=x_0+H y+K z.                                  (5)

The positive atoms depend only on y. At x_*, write these coordinates
as (y_*,z_*). The critical equations in the y directions are valid:
x_* is interior in F, so both signs of every small tangent variation
are feasible. By (3),(4) the y-Hessian is negative definite.

All positive angles have the form

    alpha_jr = a_jr + sum_l b_jrl y_l,

with a_jr and b_jrl rational. Choose a positive integer B clearing
all denominators of the b_jrl, and set u_l=exp(pi i y_l/B). Then

    S_jr(u)=2 sin(pi alpha_jr)
       = (eta_jr prod_l u_l^(B b_jrl)
          -eta_jr^(-1) prod_l u_l^(-B b_jrl))/i,    (6)
    eta_jr=exp(pi i a_jr).

Thus S_jr is a Laurent polynomial over a cyclotomic number field.
Every S_jr is strictly positive at u_*. Differentiating ideal volume
gives dV=-pi sum_jr w_j log(S_jr) d alpha_jr. For an integer C
clearing the rational coefficients w_j b_jrl, stationarity is

    product_jr S_jr(u)^(C w_j b_jrl)=1, for each l.  (7)

Negative exponents are cleared only on the open set where all S_jr
and u_l are nonzero. These are finite algebraic equations over a
number field. No lost sign or logarithmic winding is used to select
their solution: u_* is the point obtained from the positive maximum.

The Jacobian of their left sides minus one, differentiated in y,
at u_* is

    -(C/pi) Hess_y V(y_*).                         (8)

It is invertible. The coordinate change y -> u has invertible diagonal
Jacobian, so the algebraic equations have invertible complex Jacobian
in u at that point as well. Clearing the nonzero denominators only
multiplies Jacobian rows by nonzero factors.

For clarity, this proves algebraicity, rather than assuming it from
uniqueness of a real optimum. Let k be the coefficient number field
and L=k(u_*1,...,u_*h). Differentiating the algebraic equations over k
and using the invertible Jacobian shows that every du_*l is zero in
the module of differentials of L/k. A finitely generated field of
characteristic zero with positive transcendence degree has nonzero
differentials: a transcendence basis has independent differentials,
and adjoining separably algebraic elements preserves that rank.
Consequently L/k has transcendence degree zero and is a finite
algebraic extension. The case h=0 is immediate from rational constant
angles and requires no critical equations.

Formula (6) now makes every visible angle phase algebraic. The ideal
shape, in an ordering with angle pi a at 0 and pi b at 1, is

    z=exp(pi i a) sin(pi b)/sin(pi c).              (9)

It has positive imaginary part and the prescribed angles, so (2)
follows. Rational changes of the y coordinates preserve algebraicity
of their phases by taking finite roots of nonzero algebraic numbers.

Finally choose rational z sufficiently close to z_* that the point
x_0+H y_*+K z remains in the relative interior of F. Openness there
allows this choice. It is still a maximum by the exact fiber result,
and all coordinate phases in (5) are algebraic. Free flat directions
can equally well be chosen with transcendental phases; this explains
why assertion 4 is an existence statement.

## 4. Consequence for every robust Conway source

The rational polytope, affine angle triples and positive whole-source
limit are already proved in
[the general Conway variational theorem](actual_positive_conway_variational_limit.md).
Apply the theorem to its two leaf atoms and three product atoms, all
with weight one. For EVERY fixed robust expression E, at both level
parities and along the full sequence,

    lim_(N -> infinity) (2pi/N) log Z_(E,N)
       = 2 sum_(j in I_E) D(z_j),
    z_j algebraic and Im z_j>0.                    (10)

The set I_E and its shapes refer to the minimal maximizing face.
They need not include every formal atom. In particular the forced-flat
final seam is discarded for this period expression, without deleting
any physical source term or auxiliary link component. If all atoms
are flat, the right side is zero.

This strengthens the earlier conditional algebraicity assertion:
one need not separately assume an isolated complex solution, an
interior maximum in the original polytope, or uniqueness of all wire
coordinates. The definite Hessian on the quotient by K supplies the
needed isolation automatically.

The UNSYMMETRIZED expression sum_j [z_j] has not been proved to have
zero Bloch boundary or the appropriate relative peripheral boundary.
The [separate wedge calculation](actual_positive_source_bloch_regulator.md)
does prove that (1/2)sum_j([z_j]-[bar z_j]) is a rational Bloch cycle
with regulator equal to the maximum. Neither this vanishing nor
Hessian definiteness supplies face identifications or the marked
fundamental class. The next geometric task is still to prove that
the source regulator is the volume of the actual hyperbolic complement
on a broad topologically specified class.

## 5. A nonisolated example and the finite checks

Consider the rational box 0<=x<=1/3, 0<=y<=1/2, 0<=z<=1 and
the three atoms

    (x,2x,1-3x), (y,1/2-y,1/2), (z,1-z,0).

The last atom is flat, so the maximum has a free z coordinate. The
second has its unique maximum at y=1/4. For the first, stationarity
and positivity give

    sin(pi x) sin(2pi x)^2 = sin(3pi x)^3,
    4t=(4t-1)^3, t=cos(pi x)^2 in (1/4,1).        (11)

The cubic 64t^3-48t^2+8t-1 has exactly one root in that interval.
The maximizing phase is algebraic by
exp(pi i x)=sqrt(t)+i sqrt(1-t), although the whole optimizer set
is a segment. Adding the rational inequality x<=1/6 moves the
maximum to that boundary face, with x=1/6 and the same free z.
The theorem covers both cases without a global strictness assumption.

The [finite audit](../experiments/audit_positive_source_algebraic_volume_period.py)
checks the Hessian determinant identity, exact critical polynomial,
its isolating interval, and the rank after removing the flat direction.
These checks supplement the proof in sections 1--3; they do not
identify a triangulation. An independent full analytical read by the
geometry agent passed, including the boundary-face and rational-kernel
steps and the absence of a claimed Bloch-cycle or manifold conclusion.
