# A general marked positive gluing certificate, without a convex polyhedron

30 October 2026. A finite positive ideal gluing certificate is enough
for the geometric anchor in the general augmented-plat program. No
convex right-angled polyhedron, checkerboard decomposition, Conway
expression, or bridge-width restriction is needed. There is also a
useful simplification: for an actual ideal triangulation with torus
links, positivity and the MULTIPLICATIVE edge equations already force
unit edge winding. One need not impose an additional logarithmic
angle equation at every edge.

This is a direct sufficient certificate theorem. It does not establish
that every augmented diagram has such a solution, or select the original
quantum source's geometric period. The existing general source-regulator
completion theorem requires still less geometric structure: an actual
complete marked hyperbolic base and a nearby framed representation.
The certificate below supplies that base and its absolute volume by
finite algebraic data.

## 1. Exact hypotheses and the marked topological certificate

Let Y be the interior of a compact oriented three-manifold with
nonempty torus boundary. In the intended application Y is the ACTUAL
augmented plat exterior, with its given crossing disks, main components,
half twists and primitive peripheral paths.

Supply a finite oriented ideal triangulation T with all of the following:

* Every tetrahedron face is paired. There are no finite vertices,
  unpaired boundary faces, material boundary faces or extra cone points.
* Away from the deleted ideal vertices, the face quotient is a
  three-manifold; every ideal vertex link is a compact torus. The
  orientation is coherent across the face pairings.
* The quotient has a specified orientation-preserving homeomorphism to
  Y, taking its labeled ideal ends and peripheral paths to the ACTUAL
  marked ones. A triangulation of an unrelated link, the same number
  of cusps, or the same numerical volume does not supply this datum.

This topology condition is finite and reviewable: for example a common
subdivision with the literal disk/projection cut and its labeled boundary
maps gives a simplicial certificate. It is separate from solving shape
equations. One can instead begin with a triangulation constructed
directly on the specified exterior.

Give each oriented tetrahedron t a shape z_t with Im(z_t)>0, and set

    z'_t=1/(1-z_t),   z''_t=1-1/z_t.                     (1)

The tetrahedral ordering assigns these parameters to its three opposite
edge pairs. Use precisely those orderings in every equation. Require

    product_(tetrahedral edge incidences at e) w_(t,e)=1 (2)

for every global edge e, where w is its assigned z,z',or z''. Incidences
are counted with multiplicity, including identified edges of one
tetrahedron. These are full complex equalities, not modulus equations.

Finally require completeness of every cusp. One explicit algebraic
version is that the complex linear similarity multipliers of both
recorded primitive peripheral paths are one:

    a_mu=1,   a_lambda=1.                                (3)

They are computed from the actual face-path words in the corner
triangles, with their literal signs. They are rational monomials in
the tetrahedral shapes in a fixed convention. They are PROJECTIVE
similarity multipliers; SL eigenvalues require their selected square
roots and central signs. An equivalent finite horosphere certificate
is given in section 4.

THEOREM. These data construct a positively oriented complete finite-
volume hyperbolic metric on the actual Y, with

    Vol(Y)=sum_t D(z_t)>0.                                (4)

Here D is the Bloch--Wigner dilogarithm, once for each oriented
fundamental tetrahedron. There is no unrecorded factor two. The
geometric holonomy, its peripheral paths and its fundamental-class
regulator are those of the given marked topology.

## 2. Why multiplicative edge equations force winding one

Write n for the number of tetrahedra, e for the number of global
edges, and h for the number of ideal vertices. There are 2n paired
faces. End-compactify Y by coning each boundary torus to its deleted
ideal vertex. Since chi(Y_compact)=0 and each torus has Euler
characteristic zero, the end compactification has Euler characteristic
h. The tetrahedral cell count gives

    h-e+2n-n=h,   hence e=n.                              (5)

For completeness, chi(Y_compact)=0 follows by doubling the oriented
compact three-manifold: its double has Euler characteristic zero by
pairing complementary cells, and the gluing boundary has Euler
characteristic zero. Alternatively count the triangulated cusp links:
there are 4n link triangles, 6n link edges, and 2e link vertices, with
multiplicity at the two ends of every global edge. Their total Euler
characteristic is 2e-2n=0. The actual manifold/link hypothesis excludes
an edge reversal that would invalidate this count.

All three parameters in (1) have positive imaginary part. Their
arguments lie in (0,pi), and zz'z''=-1 gives

    Arg z+Arg z'+Arg z''=pi.                             (6)

Indeed the sum lies strictly between zero and 3pi and is pi modulo
2pi. Thus the sum of all six dihedral angles of one ideal tetrahedron
is 2pi. At an edge e, equation (2) implies that its positive total
angle is 2pi m_e for a positive integer m_e. Summing over ALL edges,

    sum_e m_e=n=e.                                       (7)

Every summand is at least one and there are e summands. Consequently
m_e=1 for EVERY edge. This is the promised unit-winding proof; it
uses positivity and torus links globally, not an arbitrarily chosen
branch of Log(2).

The same edge product also removes longitudinal translation. To see
both parts directly, develop the edge to the vertical line from 0 to
infinity. Consecutive incident faces determine rays in its transverse
complex plane. The next tetrahedral sector changes their ratio by its
assigned w. Multiplying all sectors gives exactly (2). The modulus
records translation along the edge and the argument records rotation.
Thus translation is zero, while (7) says the sectors fill one full
turn. The local edge development is an ordinary ball neighborhood,
not a branched 4pi-or-higher neighborhood with the same PSL word.

Ideal faces are all isometric triangles, so their specified vertex
maps glue by actual isometries. Face interiors, tetrahedron interiors
and the just-checked finite edge neighborhoods therefore carry a
nonsingular oriented hyperbolic metric.

## 3. Complete cusps from the actual similarity links

A horospherical corner of an ideal tetrahedron is an oriented Euclidean
triangle, defined up to positive scale. The face maps glue these as
oriented Euclidean SIMILARITIES on the compact topological cusp torus.
Section 2 makes every link vertex nonsingular: its incident angles
sum to 2pi and its transverse edge holonomy is identity. The similarity
structure consequently has a well-defined linear holonomy character
of the torus group.

By (3) this character is trivial on its actual two generators and
hence on the whole group. Choose one corner's scale and transport it
along link paths. The scale returns to itself around every loop, so
the corner triangles acquire compatible Euclidean metrics. The compact
link is a nonsingular flat Euclidean torus, and is complete. Its lifted
local development covers the whole Euclidean plane: lift finite line
segments using completeness, and use that the plane is simply connected.
Its deck group is therefore a discrete rank-two translation lattice.
In particular the two primitive paths have nonzero, real-linearly
independent translation periods; these are a CONSEQUENCE, not an
extra numerical assumption hiding in (3).

Realize these compatible corner scales by actual horospheres in each
tetrahedron. A uniform shrink makes all the chosen corner neighborhoods
disjoint. Their face maps agree on the horospheres, and each assembled
end has the standard metric

    dt^2+exp(-2t) ds_link^2.

There are finitely many tetrahedra, so the part left after truncating
these ends is compact. The metric on all of Y is complete and has
finite volume. Its universal developing cover is H3, by the same
complete-local-isometry segment-lifting argument. Thus its actual
holonomy is discrete and faithful. Summing the oriented volumes of
its disjoint tetrahedral interiors proves (4).

## 4. A finite real-algebraic test and a local decoration alternative

Write z_t=x_t+i y_t. Positivity is y_t>0. Equations (1)--(3), after
clearing only their specified nonzero denominators, are real polynomial
equalities and equalities in finitely many variables. Every denominator
in (1) is nonzero automatically by y_t>0. Literal peripheral paths
must still be evaluated in the same marked convention. If an exact
algebraic point is supplied, isolating intervals distinguish its real
embedding and certify all strict inequalities. A numerical residual
alone is not an exact solution certificate.

One may replace (3) by finite COMPATIBLE HOROSPHERE data. Give each
corner triangle a positive scale and require equality of the corner
segment lengths under every paired face. These equations are algebraic:
canonical squared side lengths are rational expressions in x_t,y_t;
positive scale squares remove square roots. All transitions are then
Euclidean isometries. The resulting nonsingular compact torus is flat
and complete as above. Its orientation-preserving deck isometries must
be translations, since a nontrivial rotation of the Euclidean plane
has a fixed point and cannot act as a deck transformation. Hence its
full complex linear holonomy is one, recovering (3).

This decoration version is sometimes easier to audit than long
peripheral monomials. It does NOT remove the primitive paths: those
remain needed to identify a filling slope and source peripheral logs.

A strictly positive angle assignment alone is weaker than this
certificate. It controls angle sums, but does not supply the complex
edge modulus equations or complete cusp scales. Conversely an arbitrary
nondegenerate complex solution with negatively oriented tetrahedra
cannot be used in (7): its winding terms need not be positive. Such
data need a different nonsingular developing-map certificate.

## 5. Absolute regulator and the source comparison that remains

The actual tetrahedral quotient is an oriented degree-one fundamental
chain. Its developed ideal shapes therefore give

    beta_T=sum_t [z_t],    D(beta_T)=Vol(Y).                (8)

This is the absolute geometric anchor. If all shapes lie in a common
number field, (8) is its actual marked algebraic Bloch chain; the
complete peripheral boundary vanishes after tensoring with Q, by the finite fundamental-chain
boundary calculation already proved in the repo. No assertion about
integral flattenings or an identification of different fields is needed
for the real regulator identity (8).

For a nearby actual framed representation, develop the SAME marked
ideal vertices using its peripheral fixed flags and take cross-ratios.
Positivity and nondegeneracy persist in a small neighborhood. This
constructs shapes from an existing representation; it does not assume
existence of a representation for arbitrary specified peripheral values.
The marked peripheral and regulator calculations of
[the general source-regulator theorem](general_source_regulator_hyperbolic_equality.md)
then apply on that connected branch.

In particular a proposed source action G must still satisfy

    dG=(1/2) sum_s V_s dU_s,
    Im G(0)=sum_t D(z_t),                                  (9)

with the ACTUAL primitive projective logs. Then
Im G-(1/2)sum_s Re U_s Im V_s equals the actual representation volume.
At nearby unit-charge primitive filling points the existing general
completion theorem identifies this with the filled hyperbolic volume.
Neither solving (2) nor knowing (8) proves (9) for the original quantum
source. Whole-color control, normal sectors, selected cycles, nonzero
amplitudes and the source's branch selection remain additional tasks.

## 6. The exact variational criterion, in both directions

Let A_T be the angle polytope of this ACTUAL triangulation. Its variables
are three opposite-pair angles per tetrahedron, each nonnegative;
their tetrahedral sums are pi and their global edge sums are 2pi.
Write A_T^+ for its strictly positive part and define

    V(theta)=sum_t [Lambda(alpha_t)+Lambda(beta_t)+Lambda(gamma_t)],
    Lambda(a)=-integral_0^a log(2 sin s) ds.                  (10)

The following equivalent criteria give the same complete metric:

* There is a positive complete gluing certificate of section 1.
* V has a critical point in A_T^+.
* The maximum of V on the closed angle polytope is attained in A_T^+.

When these hold, the critical point is UNIQUE, including as a maximizer
of the closed polytope, and its value is the actual Vol(Y). This is
the needed general Casson--Rivin optimization statement. Here is a
direct proof of both directions and the normalization; no geometric
existence theorem is being inserted into the implication.

### The elementary horocycle and length identity

For one positive ideal tetrahedron, choose an arbitrary horosphere at
each of its four corners. At corner a, its Euclidean triangle has angles
theta_ab, theta_ac, theta_ad. The sine law gives one positive number
C_a such that its side in the ideal face abc has length

    s_(a;bc)=C_a sin(theta_ad).

In an ideal triangle, the signed truncated length of its edge ab is

    ell_ab=-log[s_(a;bc) s_(b;ac)].

To check the constant directly, send that triangle to (infinity,0,1).
The corner segment at infinity on height H has length 1/H; the
segment at zero on a horocycle of Euclidean diameter d has length d.
Their edge distance is log(H/d), proving the formula. Overlapping
horospheres give its signed version, with the same identity.

Put S=sin(alpha)sin(beta)sin(gamma) and

    u_a=-log C_a-(1/2)log S.

The two opposite angle pairs other than theta_ab occur in the product
of the two corner segments. Consequently

    ell_ab=log sin(theta_ab)+u_a+u_b.                       (11)

Conversely ANY four real values u_a are realized by positive corner
horospheres: take C_a=exp(-u_a)/sqrt(S).

On tetrahedral angle variations, the sum of the three angles at every
corner is fixed. Equation (11) and opposite-pair equality therefore give
the differential identity

    dV_t=-(1/2) sum_(six tetrahedral edges ab) ell_ab dtheta_ab.
                                                                  (12)

Indeed the four u terms cancel by the corner angle sums, and each
opposite pair supplies -log sin(alpha) d alpha; the missing log 2
also cancels because d alpha+d beta+d gamma=0. This derives the
ideal Schlaefli formula used here directly from (10) and actual
horocycle lengths.

### Complete gluing implies a critical point and the unique maximum

At the complete metric choose the compatible cusp horospheres of
section 3. Each global edge e has ONE truncated length ell_e in all
incident tetrahedra. Summing (12) gives

    dV=-(1/2) sum_e ell_e d(total angle at e)=0              (13)

on the tangent space of A_T. Thus the geometric point is critical.

The Hessian of V_t on gamma=pi-alpha-beta is negative definite.
The negative Hessian matrix is

    [[cot alpha+cot gamma, cot gamma],
     [cot gamma, cot beta+cot gamma]].

Its first diagonal entry is sin(beta)/(sin(alpha)sin(gamma))>0,
and its determinant is 1, by the cotangent addition identity when
alpha+beta+gamma=pi. Hence V is strictly concave on the product of
positive tetrahedral angle simplices and on A_T^+. It extends
continuously to the compact closed angle polytope. Along a segment
from its critical positive point to ANY other closed point, all
intermediate points are positive, the initial derivative is zero,
and the second derivative is strictly negative. The volume strictly
decreases, so the endpoint also has smaller value. This proves the
unique global maximum assertion, including boundary points.

### A positive critical point reconstructs complete gluing

Conversely let theta in A_T^+ be critical. Since its constraints are
linear, elementary row-space/kernel duality supplies real multipliers
lambda_t for the tetrahedral sums and eta_e for the global edge sums:

    -log(2 sin alpha_t)=lambda_t+eta_e+eta_f,                (14)

where e,f are the two opposite edge incidences carrying alpha_t.
The same formula holds for beta and gamma, with multiplicity if
e=f. Constraint dependencies do not affect this statement.

Construct the positive ideal tetrahedron with these angles, for example

    z_t=[sin(beta_t)/sin(gamma_t)] exp(i alpha_t).

Put L_e=-2 eta_e. Equation (14) gives

    L_e+L_f-2log sin(alpha_t)=2lambda_t+2log 2,

the SAME value for all three opposite pairs in t. Therefore there
exist four real numbers u_a, one per tetrahedral corner, such that

    L_(ab)=log sin(theta_ab)+u_a+u_b                       (15)

for all six incidences. Here is the entire linear algebra: set
b_ab=L_(ab)-log sin(theta_ab). The three opposite-pair sums of b
are equal, which is precisely the two compatibility conditions for
the six equations b_ab=u_a+u_b. They have a unique solution, starting
with u_a=(b_ab+b_ac-b_bc)/2 and then u_b=b_ab-u_a, etc.

By (11), choose the actual tetrahedral corner horospheres realizing
these u_a. Thus EVERY incident tetrahedron now has the same prescribed
truncated length L_e on a global edge. The three side lengths of an
ideal face determine its three corner horocycle sizes uniquely:
if s_a s_b=exp(-L_ab), then

    log s_a=(-L_ab-L_ac+L_bc)/2.

Consequently all face pairings match all corner horospheres. Around
each global edge these maps preserve the two endpoint horospheres,
so its dilation is zero. Its total angle is 2pi by the angle-polytope
constraint, so its full edge holonomy is identity and the local
development is nonsingular. The compatible corner decorations give
complete flat cusp tori by section 4. Thus these shapes satisfy the
edge and complete peripheral equations and construct the actual
complete geometric metric. This proves the converse.

In particular, a nonempty strict angle polytope alone is NOT the
criterion. Its volume maximum must lie in the strict interior.
The proof above explains exactly what that interior optimum supplies.

## 7. A purely algebraic certificate for that strict optimum

The variational criterion has a finite real-algebraic form with no
logarithms. For each opposite angle pair take a unit phase w_(t,a)
in the upper half-plane. Require

    |w_(t,a)|^2=1, Im w_(t,a)>0,
    product_(three pairs in t) w_(t,a)=-1,
    product_(incidences at global edge e) w_(t,a)=1.        (16)

The tetrahedral argument is pi by the same range check as (6), and
the global arguments are exactly 2pi by (5)--(7). Thus these are an
actual strict angle structure, with no missing angle winding.

Add positive real variables A_t and B_e and require, at every opposite
pair whose global edges are e,f,

    2 Im(w_(t,a)) A_t B_e B_f=1.                          (17)

Taking real logarithms gives precisely (14), with lambda_t=log A_t
and eta_e=log B_e. Therefore (16)--(17) imply a positive critical
point, hence actual complete geometry and the unique volume maximum.
Conversely every such complete positive geometric point supplies
these multipliers by the preceding proof. Equations (16)--(17) and
strict positivity are finite polynomial conditions in real and
imaginary parts. Repeated edge incidences retain the corresponding
factor B_e^2.

This is a simple algebraic sufficient criterion on ANY actual marked
ideal triangulation, without first finding a convex Q_Delta. It is
not a purely combinatorial classification: proving nonemptiness of
this strict semialgebraic system for a chosen broad diagram class is
still an existence problem. Its distinguished strict point is an
honest geometric optimum, rather than an arbitrary branch of the
exponentiated equations.
Failure for one supplied triangulation is not a proof that Y is
nonhyperbolic; a different marked triangulation may admit the certificate.

The unique positive optimum also has ALGEBRAIC phases and shapes.
Normalize its angles by pi. The closed angle polytope is rational,
and its atoms are the rational coordinate angle triples, with weight
one. The already proved
[rational angle-optimizer theorem](positive_source_algebraic_volume_period.md)
therefore applies directly. More explicitly, choose a rational tangent
basis, exponentiate stationarity after clearing its denominators, and
use the strictly negative Hessian to obtain an invertible complex
Jacobian at the selected phase point. Differentiating those polynomial
equations forces its coordinates to have zero transcendence degree
over the coefficient number field. Formula z=exp(i alpha) sin(beta)/sin(gamma)
then gives algebraic positive shapes. This proves algebraicity of the
marked optimum; it does not make its dilogarithm value algebraic or
identify any cyclotomic quantum source with that period.

There is also a precise DECORATION TORSOR in this certificate. With
the strict phases fixed, all positive multiplier solutions (A_t,B_e)
correspond exactly to compatible choices of cusp horospheres. Indeed
the reconstruction above converts each solution to corner horospheres;
between two solutions their corner scale ratios agree across every
paired face, and hence are constant on each actual cusp. If changing
the horosphere at cusp v changes its corner term u by s_v, then
L_e changes by s_v+s_w at an edge with endpoints v,w. Put t_v=exp(s_v/2).
The exact action is

    A_t -> A_t product_(four corners v of t) t_v,
    B_e -> B_e/(t_v t_w),        t_v>0.                    (18)

It preserves (17) because the two opposite edges together use all
four corners. The preceding horosphere comparison proves transitivity.
It is free: a fixed B would give s_v+s_w=0 on every edge; the three
edge equations of any tetrahedral face force each of its corner
values to be zero, even when some global cusp labels coincide.
Thus the positive solution fiber is a torsor for one positive scale
per cusp. This is the actual geometric cusp-decoration gauge, NOT
the still-unidentified quantum-period selection torsor. No assertion
that the same monomial action is free over C is made; its sign
kernels and square-root choices would have to be retained there.

## 8. The weakest useful general class and what was removed

There are three different levels of geometric input:

1. An actual complete finite-volume marked hyperbolic base Y is enough
   for the already proved general geometric completion/regulator
   implication. It needs no ideal triangulation at all.
2. An actual marked positive complete gluing certificate as above gives
   that base and its regulator by finite explicit equations, uniformly
   for arbitrary plat width and arbitrary triangulation incidence.
3. A convex positive right-angled Q_Delta certificate gives such a
   triangulation by the coning construction in
   [the matching-graph theorem](general_augmented_plat_matching_geometry.md).

Thus (2) is a broader usable certificate than requiring (3). We do not
claim a new existence theorem for positive ideal triangulations of all
hyperbolic manifolds, nor a combinatorial characterization of all graphs
admitting Q_Delta. Neither is needed for the implication proved here.
For the general long-twist target, one can retain its existing hypothesis
that the ACTUAL augmented exterior is hyperbolic, and use ANY independently
certified geometric base instead of first reconstructing a right-angled
convex polyhedron. A common marked positive triangulation is a convenient
way to compare a source Bloch chain with its actual fundamental class.

The broad quantum theorem remains about the original augmented source
on this geometric base; the certificate has not replaced that source by
a state sum defined from T.

## 9. Coverage and independent exact checks

For coverage, the antecedent is explicit in
[Futer--Gueritaud, *From angled triangulations to hyperbolic structures*](https://arxiv.org/abs/1004.0440):
its abstract states the Casson--Rivin theorem that a critical point of
the angle-structure volume functional gives a complete hyperbolic
structure. No novelty of that theorem is claimed. Sections 2--7 above
give the direct proof and exact marked-certificate form used here;
they do not import an existence theorem for arbitrary augmented plats.

[The exact audit](../experiments/audit_general_marked_positive_gluing_certificate.py)
constructs an eight-tetrahedron face quotient from two regular ideal
octahedra with the original two bowtie pairings. It checks orientation
of every face map, three torus vertex links, all eight complex edge
products, and angle sum exactly 2pi at every edge. Ninety-six paired
corner-segment checks give compatible horospheres. The same exact
data satisfy the critical-point multiplier equations independently;
the restricted Hessian determinant and four-corner compatibility
identity are checked symbolically. These test the stated geometric
and variational certificate, not a quantum source selection theorem.

[Recorded results](../experiments/general_marked_positive_gluing_certificate_results.json).

The Bloch-boundary statement is rational. The gluing criterion does not establish existence of a positive certificate for every diagram or select its quantum period.