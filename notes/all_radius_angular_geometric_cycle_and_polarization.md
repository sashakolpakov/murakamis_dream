# A full lifted angular geometric cycle, and a subunit-polarization obstruction

28 October 2026. For every supplied positive complete ideal
triangulation in a nonsingular marked quad chart, the classical
potential has an explicit product of FULL lifted angular intervals
on its complete radii. Its geometric point is the unique global
maximum of the real exponential action on that whole product,
with a strict boundary gap. This is not restricted to the positive
angle polytope or to shapes of modulus below one.

The corresponding reference relative cycle has unit local geometric
degree. Its equality with the original reduced quantum cycle has
not been proved. In particular, the lifted endpoints need not glue
without a nonzero monodromy/keyhole completion.

There is also a precise reason not to impose subunit shapes while
using B^(-1): the positive five-tetrahedron triangulation of the
hyperbolic knot 8_1 below has NO all-subunit cyclic quad choice with
nonsingular B, even if both peripheral rows are available.

## 1. The marked potential and its fixed-radii separation

Use the supplied full-rank positive chart of
[the Legendre/Rivin construction](general_legendre_rivin_contour.md):

    W(x)=sum_j Li_2(exp x_j)+(1/2)x^t(I-C)x
                                      +i(kappa-pi*1)^t x,
    C=C^t real,
    x_*=rho+i theta_*, 0<theta_*j<pi,
    W_x(x_*)=0.                                      (1)

Its marked critical imaginary value is the hyperbolic volume.
On the COMPLETE fixed radii, x=rho+i theta, its imaginary part is

    Im W=sum_j f_j(theta_j)+(kappa-pi*1)^t rho,
    f_j(theta)=Im Li_2(r_j exp(i theta))+L_j theta,
    r_j=exp(rho_j), L_j=((I-C)rho)_j
                           =log|1-z_*j|.             (2)

The last equality is the real part of the actual critical equation.
Thus all angular variables separate, despite the generally coupled
matrix C. Each dilogarithm in (2) is continued on the branch
containing the original upper-half-plane shape z_*j.

## 2. A full lifted interval with a unique global maximum

Fix ANY r>0 and 0<theta_*<pi. Put

    L=log|1-r exp(i theta_*)|,
    mu=log^+r=max(0,log r).

Choose the marked full interval

    J=[0,2pi]    if L<=mu,
    J=[-pi,pi]   if L>=mu.                           (3)

When equality holds either is allowed. Continue the dilogarithm
along this interval from its value at theta_*.

Then f(theta)=Im Li_2(r exp(i theta))+L theta has theta_* as
its UNIQUE global maximum on J. Indeed,

    f'(theta)=L-log|1-r exp(i theta)|,
    f''(theta)=-r sin(theta)/|1-r exp(i theta)|^2.     (4)

On (0,pi), the distance in (4) increases strictly, so f increases
to theta_* and decreases afterwards. On each negative-half interval
it is convex, so its maximum is at an endpoint. Finally

    f(theta+2pi)-f(theta)=2pi(L-mu).                  (5)

For r<1, integrate the convergent logarithmic Fourier series to
see that the mean of log|1-r exp(i theta)| is zero. For r>1,
factor out r and use that same series for r^(-1); the mean is
log r. Continuity proves the r=1 case. Equation (5) then proves
the endpoint comparison in precisely the direction chosen in (3).

There is an explicit positive endpoint gap:

    delta=f(theta_*)-pi max(L,mu)>0.                 (6)

For the first interval, the larger endpoint value is pi*mu;
for the second it is pi*L. These values use the continued branch.
For example, when r>1, the upper-side limit at theta=0 has
Im Li_2(r)=pi log r, while continuation to theta=2pi has
-pi log r. Continuation into negative theta from the upper side
adds 2pi log r to the principal lower-half imaginary part.
These lifts cannot be discarded as a harmless phase.

If r=1, the possible dilogarithm branch point is at an interval
endpoint, far from theta_*. The theorem uses its continuous
boundary value. Small boundary indentations retain the positive
gap; no critical point is placed on that branch point.

Apply (3) to every tetrahedron. On the product box B=product J_j,
the whole Im W has its unique global maximum at theta_* and

    max_(boundary B) Im W <= Im W(x_*)-min_j delta_j. (7)

This controls ALL angular cells of this SPECIFIED lift, not just
the cell whose angles are positive. It does not compare the
different weak alias-face potentials of another lift.

## 3. What degree has actually been computed

The fixed-radii product box is a reference relative cycle, with
boundary in the strict lower sublevel (7). Near theta_* its
complex Gaussian is nondegenerate. In fact

    Re Hess_theta [W/(2pi i)]
       =-(1/(2pi))diag Im[z_*j/(1-z_*j)]<0.          (8)

Therefore for a holomorphic amplitude nonzero at x_*, the
integral over THIS lifted box has a nonzero usual Gaussian
leading coefficient. Its exponential rate is
Im W(x_*)/(2pi)=Vol/(2pi). The local geometric relative
degree is +1 with the box's coordinate orientation: its upper
superlevel slice is one negatively curved disk through the
critical point. The strict gap (7) localizes that relative
class to this one disk.

This proves a property of an explicit reference chain. It does
not assume or establish a quantum invariant defined by that
chain. To use it for the original source one still must compare
the reduced cycle from
[the exact Hardy forest](actual_hardy_forest_residue_reduction.md)
to this MARKED lift, including its endpoints and root factors.
The +1 degree of eliminated Hardy normals is not that comparison.

In particular, if L differs from mu, equation (5) says that a
full angular turn changes the leading imaginary action. A bare
ordinary base torus cannot be identified with the lifted box
while ignoring the required deck/monodromy completion. A norm-one
cyclic atom is actually single-valued around a sufficiently large
circle; outside its initial disk additional leading terms restore
that periodicity. Its small-disk Li_2 symbol cannot simply be
continued there and used in (7). A full rational quantum
dilogarithm and its pointed completion may provide the correct
object, but this requires an exact source identity.

## 4. Why a subunit quad choice does not repair this issue in general

Consider the standard five-tetrahedron triangulation m074 of 8_1.
Let b be the root near -0.035467991584+1.775303570695i of

    P(b)=b^6+b^5+5b^4+4b^3+6b^2+3b+1=0.

Set

    a=-(b^2+b+1)/(b^2+2),
    (z_0,...,z_4)=(a,a^(-2),b,b,(1-b)^(-1)).         (9)

The raw gluing rows, with triples (z,z',z'') and both peripheral
rows last, are

    [2,0,0, 1,0,0, 0,0,0, 0,0,0, 0,0,0]
    [0,2,1, 0,0,2, 0,1,0, 0,1,0, 0,0,0]
    [0,0,1, 0,2,0, 0,1,1, 0,1,1, 0,2,1]
    [0,0,0, 1,0,0, 1,0,0, 1,0,0, 0,0,1]
    [0,0,0, 0,0,0, 1,0,1, 1,0,1, 2,0,0]
    [0,0,0, 0,-1,-1, 1,0,0, 1,-1,0, 0,-1,0]
    [0,0,0, 1,-1,-1, 3,0,-1, 0,-3,0, 0,-2,0].   (10)

Exact reduction modulo P verifies every product equals one.
Arb enclosures verify all shapes are positive and the marked
logarithmic sums are 2pi*i at edges and zero at both peripheral
rows. Thus the geometry is complete, not merely a positive
angle assignment. The associated triangulation is combinatorially
isomorphic to the installed 8_1 knot triangulation by a
meridian-preserving map; see the optional topology audit.

The ONLY cyclic quad choices with every modulus below one are

    (1,0,1,1,0), (1,1,1,1,0).                     (11)

Here a rotation r means the new triple is the old triple cyclically
rotated by r. Write G_0,G_1,G_2 for these rotated incidence blocks
and B=G_2-G_1. For BOTH choices (11), using ALL rows in (10),

    B (0,0,1,1,-2)^t=0.                           (12)

The full B rank is four, below the required five. Therefore
neither selecting another omitted edge nor changing the marked
peripheral slope produces an invertible B with all quad shapes
subunit. In particular the stronger lens condition
|z|<=1 and |1-z|<=1 cannot universally be combined with B^(-1).

This does not obstruct the positive chart theorem: for example
the quad choice (0,1,0,0,0), with rows (0,1,2,3,5), has det B=1.
It necessarily contains shapes outside the unit disk. The
all-radius lifted maximum theorem applies to that chart.
The required quantum cycle still has to carry its correct
nonperiodic lift rather than a guessed periodic Li_2 branch.

## 5. Reproducible checks

`experiments/audit_all_radius_angular_chart.py` proves the gluing
products and kernel witness by exact polynomial/matrix arithmetic,
certifies the sextic root, positivity, complete logarithmic marks,
the subunit choices and explicit positive angular gaps with Arb,
and checks the elementary full-interval theorem at sample radii.
The sample checks supplement the proof (4)-(7).

Its optional `--topology` check compares the full gluing data
with m074 and checks an actual combinatorial isomorphism to 8_1
preserving its meridian. The result is a polarization obstruction,
not a counterexample to the volume conjecture or a nonzero
unwanted quantum contribution.
