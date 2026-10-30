# A fixed-radius smoothing bound and its explicit limitation

30 October 2026. Independently reviewed; source-coverage correction below.
A one-variable test at
the ORIGINAL positive face variables gives a strict source upper bound after a
literal untwisted L_1 insertion. It needs neither a balanced split nor
an attained smoothed capacity. The test is not universal: an explicit
certified family below makes its best possible gap tend to minus
infinity. This is a failure of fixed old radii, not a counterexample
to a fully optimized smoothing gap or a volume conjecture. The family is
proved as a labeled right-angled MATCHED-GRAPH capacity example. Its
identification with the fixed flat-plat source coefficient is conditional
on an additional source-preserving presentation adapter; section3 does
not supply that adapter.

## 1. An exact sufficient source test

Use the original connected certified source, actual marked faces u,v,
and the normalization of
[the smoothing capacity theorem](actual_matching_smoothing_angle_capacity.md).
Let a specified UNTWISTED port have triangles (x,b,y),(x,c,y).
Its replacement L_1=I deletes those two triangles and identifies b,c.
Assume the resulting projection is connected, the marked faces remain
distinct, and b,c are distinct unmarked faces. All repeated incidences
after the identification are retained. The deleted port's original
half twist must be zero; a remaining R^epsilon is not an identity.

Let l^0 be the ORIGINAL positive finite face curvatures (reciprocals
of Euclidean circle radii), with the two marked line variables zero.
The established term "fixed-radius bound" refers to these face variables;
it does not identify them with Euclidean radii. Write F for the source-normalized local fold
rate, with

    F(t l_0,t l_1,t l_2)=F(l_0,l_1,l_2)+(1/2)log t,
    partial_(log l_j) F=theta_j/(2pi),
    theta_j=2atan(l_j/sqrt(l_0 l_1+l_1 l_2+l_2 l_0)).   (1)

At a one-positive-variable triple the nonzero angle is pi. These are
the continuous boundary values, not a different local model. The exact
original action is

    Phi_old=sum_(all triangles) F(l_t^0)
                         -sum_(old finite faces) log l_f^0.

For s real, replace BOTH b,c by z=exp(s), leaving every other finite
face variable at l^0. Sum over the actual remaining triangles, and count the
merged face only once in the target monomial. Define

    P_sm(s)=sum_(remaining triangles) F(l_t(s))
                         -sum_(smoothed finite faces) log l_f(s),
    G(s)=Phi_old-P_sm(s).                               (2)

If G(s_*)=g>0 for one finite s_*, then the original marked contraction
with that L_1 insertion and all other circles complete satisfies

    limsup_(N->infinity) N^-1 log|A_N^(L1)|
                                    <=Phi_old-g.       (3)

Every retained half twist on another port stays in its exact source
sum. Its channel phase has modulus one, so the upper bound is valid
with those phases. The original mark, N-power measure, multiplicities,
beta factors, and full range of every remaining channel are retained.

Proof: the exact marked face-coefficient theorem applies to the
literal shorter diagram. For each label assignment its positive
coefficient is bounded by evaluation at the shared radii in (2),
divided by its actual target monomial. The degenerate local cases in
the smoothing theorem bound every original beta^2 D D P factor by
its fold rate at these same radii. Finite labels and original scalar
factors contribute only a polynomial in N. Taking the sum in absolute
value proves (3). No minimizer of the smoothed capacity is used.
If a remaining source factor is identically zero, the bound is already
stronger. The statement does not move the mark or substitute a second
boundary trace.

Log-radius convexity of F makes P_sm convex, hence G concave. Its
derivative is the explicit actual incidence sum

    G'(s)=1-(1/(2pi))sum_(remaining b/c corners) theta_corner(s).
                                                               (4)

If a triangle acquires the merged label twice, both corners occur in
this sum. Thus the best test in (2) is a one-dimensional convex
minimization, with no split-side imbalance hypothesis. It may hold
when the full smoothed minimizer escapes to a boundary. It is only a
sufficient test; section3 proves that it need not hold at all.

## 2. Boundary regularization and the precise charged extension

The strict bound has a useful continuity margin. Set the two marked
face variables to small FIXED positive values eta_u,eta_v before
coefficient extraction. Keep their target exponents zero, and keep
all other target exponents d=N-1. Each nonzero local triple in (2)
has a continuous F limit as eta_u,eta_v tend to zero. Hence these
values can be fixed sufficiently small that the new evaluation rate
is at most Phi_old-g/2. This does not assign target degree d to a
marked face and does not take a quantum-level-dependent limit.

More precisely, let P_N be one of the actual nonnegative-coefficient
polynomial products after smoothing, including beta factors, and let
n* be the actual target vector. At the fixed positive evaluation l*,
any integer shift nu obeys

    |[L^(n*+nu)]P_N| <= P_N(l*)/(l*)^(n*)
                                  exp(C_l ||nu||_1).   (5)

A negative target exponent gives zero. Phased identifications such
as c=Q^p b cost nothing in this bound: take absolute values of the
polynomial coefficients before evaluation. A finite sum of such
specified coefficients with total scalar norm at most N^C C_0^H
and ||nu||_1<=C_1 H therefore costs only N^C exp(C_2 H) in addition
to the regularized capacity. If H<=delta N with delta sufficiently
small, it still has a strict exponential gap.

Equation(5) is a coefficient bound, NOT an already proved L_h source
expansion. Actual L_h paths retain their unwrapped physical endpoints,
their c=Q^p b identifications and all clock charges. In particular,
after a charged modular face average a target congruence can cross
N and admit a new exponent shifted by an ENTIRE N, not merely O(h).
Those aliases are not controlled by (5) with H=O(h). They must either
be excluded by the actual support or be estimated separately. The
fixed positive marked radii resolve the elementary Laurent-coefficient
bound; they do not silently remove these finite-source questions.
No signed deleted-port R^epsilon norm is discarded.

## 3. A certified matched-graph family where the capacity test fails

The initial white triangulation is the octahedral sphere with equator
0,1,2,3 and poles4,5: its triangles are

    (p,j,j+1 modulo4), p=4,5, j=0,1,2,3.

Mark the actual MAIN edge23. Choose the matching edges of the dual
cubic source by the white edges

    {01,12,34,35}.                                     (6)

They cover each triangle exactly once, and do not contain the marked
edge. Starting with b_0=5, insert b_n into the triangular interstice
(0,1,b_(n-1)), replacing that triangle by its three subdivisions.
Add the matching white edge b_(n-1)b_n at each step; the matching
edge01 stays. This is again a perfect matching: the new triangle
(0,1,b_n) inherits01, while the other two new triangles are paired
by b_(n-1)b_n. The complement is the actual union of main cycles.

To specify the marked diagram, use this EMBEDDED dual cubic graph,
not just its abstract isomorphism class. Replace a small neighborhood
of every selected matching edge by the standard untwisted complete
crossing-circle box, with its four main half-edges in their inherited
cyclic order. Join these half-edges along the complementary embedded
edges, and put the original mark on edge23. This is an explicit
augmented-link diagram. Each subdivision above replaces one trivalent
source vertex in a small disk by a three-vertex triangle, retaining
its three external ports and adding the specified matching edge.
It therefore preserves this literal construction and its marking;
no assertion that an arbitrary abstract cubic graph is an admissible
source is needed. A Morse presentation gives its actual cups, caps,
and complete-circle tensors. This construction does NOT prove that the
diagram has the fixed flat-plat presentation required by the
[marked face-coefficient theorem](actual_original_marked_face_coefficient.md),
sections1--3, with the same designated circle ports and mark. That
theorem's gap sweep and marked conservation argument cannot simply be
imported into an arbitrary Morse presentation. Neither a uniform bridge
width over this family nor a source-preserving flat-plat adapter at a
fixed depth is established here.

Here is the labeled geometric certificate, not just a combinatorial
example. In the boundary plane use the two marked parallel lines
y=0 and y=2 for faces3 and2. The four finite initial circles have

    face0: center(0,1/2), radius1/2;
    face1: center(0,3/2), radius1/2;
    face4: center(-sqrt2,1), radius1;
    face5: center(+sqrt2,1), radius1.

The inserted circles have center and radius

    center(b_n)=((2n+sqrt2)/B_n,1), radius(b_n)=1/B_n,
    B_n=4n^2+4sqrt2 n+1.                               (7)

They are tangent to circles0,1 and b_(n-1), and lie strictly inside
that triangle's old interstice. These statements follow directly by
squaring the center distances; equivalently their curvatures satisfy
the positive Descartes recurrence with the two fixed curvatures2,2.
All other old circles and contacts are unchanged. Thus this is a
labeled packing with precisely the stated triangulation at every n.

Its halfspace certificate can also be read directly. Take the
geodesic planes of these white circles and the circles through the
three contact points of each complementary triangle. The latter are
orthogonal to its three white circles. Their inward halfspaces give
the initial ideal right-angled cuboctahedron. Each insertion attaches
the ideal right-angled octahedron with the three old and three new
contact points along the old shaded triangle. Its adjacent white
planes are the same planes, so the seams are flat and all remaining
dihedral angles are pi/2. The three new outward shaded disks are
contained in the old outward shaded disk and tangent to its boundary
at the old contacts. Every new ideal vertex satisfies all the other
old supporting inequalities, strictly when it is not incident to
that facet. Thus the coplanar seams disappear and the union is the
intersection of precisely the retained and new inward halfspaces;
it is convex, rather than merely locally right-angled. Induction gives a convex ideal
right-angled polyhedron with the exact new labeled facets. No
unlabeled volume match is used as a certificate.

Consequently the labeled packing face curvatures are exactly

    l_0=l_1=2, l_4=l_5=1, l_2=l_3=0, l_(b_j)=B_j.

The dual cubic graph is 3-connected: the initial cube is 3-connected,
and replacing a vertex by its three-edge triangle preserves this
property. Remove the matching port01 and its two triangles
(0,1,b_n),(0,1,4), and merge b_n with4. The remaining projection is
connected (already deleting the two old cubic vertices leaves a
connected graph), and the marked faces2,3 remain distinct. Thus this
is the literal opposite matching-edge smoothing of this marked graph.
Applying section1 to its actual quantum source would additionally
require the presentation adapter just specified. The geometric and
capacity calculations do not require the main cycles to have one
component.

Only five remaining triangle terms depend on the new common radius z:
two are (2,B_(n-1),z), two are (2,z,0), and one is (z,0,0).
The graph capacity functional (2) is therefore exactly

    G_n(z)=C_n-2F(2,B_(n-1),z)-2F(2,z,0)+(1/2)log z,
    C_n=F(2,B_n,2)+2F(2,B_(n-1),B_n)
                  +F(2,1,2)+2F(2,1,0)-log B_n.       (8)

This includes both deleted triangles and the changed face-target
monomial. In particular it is not just a comparison of local volumes.

We prove the obstruction uniformly over ALL z>0. Monotonicity and
homogeneity of F give

    2F(2,B_(n-1),z)>=log B_(n-1),
    2F(2,z,0)>=log max(2,z).

Thus the z-dependent expression in (8) is bounded above by its
n-dependent constant minus (1/2)|log(z/2)|. Evaluation at z=2
and the following limits show that its maximizers stay in one fixed
compact subset of (0,infinity). On that compact, continuity and
homogeneity give uniformly

    F(2,B_n,2)=(1/2)log B_n+o(1),
    F(2,B_(n-1),B_n)=(1/2)log B_n+F(0,1,1)+o(1),
    2F(2,B_(n-1),z)=log B_(n-1)+o(1).

The limiting z-dependent function is
-2F(2,z,0)+(1/2)log z. Its derivative vanishes only when the angle
at z is pi/2, namely at z=2; strict log-radius convexity makes this
its unique maximum. Substituting in (8) proves

    sup_(z>0) G_n(z)=-log n+K+o(1),
    K=F(2,1,2)+2F(2,1,0)-(3/2)log2.                  (9)

In particular the best fixed-old-radius test is NEGATIVE for every
sufficiently large n. Full radius readjustment is essential here.
This does not say that the fully optimized smoothed capacity exceeds
the original capacity: the former is an infimum over ALL remaining
radii, whereas (8) varies only the merged radius.

## 4. Remaining general comparison

Literal smoothing identifies opposite middle faces. It is not ordinary
deletion of the shared white edge01, and a generic graph-minor volume
inequality is not automatically its capacity inequality. Section3
also rules out promoting the one-variable test to a theorem forced
by every positive labeled certificate.

The general connected untwisted smoothing gap and its near-complete
small-color corridor are now [proved separately](actual_smoothed_block_representation_volume.md)
in the original fixed flat-plat scope. That theorem does not provide the
missing presentation adapter for the family in section3. The present
note retains its exact sufficient source bound in section1 and its
independent matched-graph functional limitation. Signed varied ports
and far-color source bounds remain separate.

Focused audit: [original source and labeled certificate checks](../experiments/audit_actual_smoothing_fixed_radius_gap.py),
with [saved results](../experiments/actual_smoothing_fixed_radius_gap_results.json).
At 80 digits it checks ten literal original marked L_1 contractions
against the shorter face-coefficient source, retaining every remaining
half twist and the original cups, mark, and measure. These original
matrix fixtures test section1; they are NOT the Apollonian graphs of
section3 and do not establish the missing adapter. The audit also checks two
symbolic tangency identities; nine perfect matchings, three-connected
graphs, and connected literal smoothings; 2,340 white and 3,816 shaded
support values; and 432 original right-angle incidences. Seven finite
optimized one-variable profiles and one positive-marked regularization
check diagnose the exact normalization. The analytic argument, not
those finite profiles, proves the all-n limitation in (9).

Primary full analytical proof and audit-code review: PASS. Independent
targeted geometric review: PASS, including the literal embedded matched graph,
perfect matching, interstice insertion, convex supporting-halfspace
induction, and the actual opposite-face smoothing. These reviews do
not infer a full optimized smoothing gap or an L_h alias bound.

Independent full analytical proof/code review and fresh redirected
80-digit replay: PASS. Every reported source, certificate, and profile
count was reproduced. The review retains the sufficient nature of (3),
the exact charge/alias qualifications after (5), and the fixed-old-face
scope of the counterfamily.

### Source-coverage correction, 30 October 2026

The earlier wording called the section3 family an original source
counterexample to the fixed-radius strategy. The verified statement is
the narrower geometric matched-graph CAPACITY obstruction (9). The
frozen exact face identity proves a fixed flat-plat formula, not the
general Morse formula that the earlier inference would need. An
arbitrary link-to-plat isotopy does not verify preservation of the
designated complete-circle tensors, their original mark or the face
coefficient normalization. All displayed geometry, functional formulas
and asymptotics remain unchanged. The audit code and saved results are
unchanged; no rerun or new original-source comparison is claimed by
this correction.
Independent coherent targeted review of this coverage correction:
PASS. No mathematical geometry or functional estimate was changed.
