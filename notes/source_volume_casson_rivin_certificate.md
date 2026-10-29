# From the selected source volume to hyperbolic volume

29 October 2026. The task here starts AFTER an original-source theorem
has proved

    lim_N (2pi/N) log|K_N| = V_src.

It is to prove that this particular V_src is the hyperbolic volume of
the actual complement. The argument below isolates a finite classical
certificate for that equality. It does not assume that the displayed
quantum limit has been proved for arbitrary knots.

The existing [filled-source proof](actual_long_pretzel_casson_rivin_equality.md)
already supplies this certificate for its selected long-filling branch.
The [independent tangent-space audit](source_angle_stationarity_critical_audit.md)
checks the distinction between a source saddle and a critical point on
the FULL angle domain. Sections 2--3 below give an elementary proof of
the complete-cusp Casson--Rivin implication, including completeness.

## 1. The exact certificate

Let T be an actual oriented ideal triangulation of a manifold with
torus ends. Write theta for its three opposite-edge-pair angles in
each tetrahedron. Let A impose the tetrahedral sums and E count the
local edge occurrences at each global edge, with multiplicities.
The positive angle domain is

    P={theta>0: A theta=pi*1, E theta=2pi*1}.

Put

    V_T(theta)=sum_i Lambda(theta_i),
    Lambda(theta)=-integral_0^theta log(2sin t)dt.

For a complete cusped complement the certificate consists of:

1. A specified theta_src in P, on the actual triangulation and with
   every tetrahedron positive.
2. The absolutely normalized equality V_src=V_T(theta_src).
3. Full constrained stationarity:

       grad V_T(theta_src) in rowspace(A,E).          (1)

Equivalently, one exhibits real vectors mu,eta such that for each
tetrahedral opposite edge pair i=(e,e'),

    -log(2sin theta_src,i)=mu_t+eta_e+eta_e'.          (2)

The conclusion is

    V_src=max_(closure P) V_T=Vol(M).                (3)

Row dependencies cause no problem: (1) is precisely annihilation of
ker(A,E). A constrained source saddle proves (1) only if all omitted
angle directions have also been accounted for. Section 4 explains
two ways to do this without requiring the source variables themselves
to parametrize every angle variation.

For a filled manifold replace P by the actual filled-slope angle
slice, and retain its primitive angular lifts and its end-completion
certificate; see section 5. Imposing the unfilled boundary conditions
would compute a different volume.

## 2. Strict concavity proves the maximum, including the boundary

For one tetrahedron put beta=pi-alpha-gamma. Its negative volume
Hessian, in independent coordinates alpha,gamma, is

    H=[[cot alpha+cot beta, cot beta],
       [cot beta, cot gamma+cot beta]].              (4)

The first diagonal entry is sin gamma/(sin alpha sin beta)>0 and
det H=1. Thus H is positive definite throughout the positive simplex.
The sum over tetrahedra is strictly concave on every affine slice.

If theta_src is an interior stationary point, follow the straight
segment to any distinct point theta of the closure. This segment is
positive except possibly at its final endpoint. Its volume derivative
starts at zero and its second derivative is strictly negative. The
continuous extension of Lambda to [0,pi] therefore gives

    V_T(theta)<V_T(theta_src)  for theta!=theta_src.  (5)

The feasible domain is convex; V_T is concave. The convex function is
-V_T. Neither nonemptiness of P nor strict concavity alone guarantees
that its maximum lies in its interior. Positivity of theta_src in
the certificate supplies the needed interior point directly.

## 3. Why the complete-cusp critical point is a complete metric

This proves the geometric implication rather than merely naming the
maximum a volume. It uses (2), not a presumed complete representation.

Assign one real number to each global edge:

    l_e=-2 eta_e.                                    (6)

An ideal tetrahedron admits horospherical decorations whose six signed
truncated edge lengths are exactly these numbers. Here is the explicit
compatibility check. For any decorated ideal tetrahedron, the three
opposite-pair length sums have differences

    (l_e+l_e')-(l_f+l_f')
                  =2log(sin theta_i/sin theta_j).   (7)

For example normalize its vertices to infinity,0,1,z. If the three
finite horospheres have Euclidean diameters d_0,d_1,d_z and the
horosphere at infinity has height H, the six lengths are

    l_(infinity,a)=log(H/d_a),
    l_(a,b)=log(|a-b|^2/(d_a d_b)).

The opposite sums are a common constant plus respectively
2log|1-z|, 2log|z|, 0. The sine rule proves (7) in the corresponding
angle order. Equation (2) shows that the target lengths (6) have
exactly these differences.

Conversely those two independent differences are the ONLY
restrictions. Changing the four horospheres adds r_v+r_w to the
length of edge vw. A six-vector delta is of this form precisely when

    delta_01+delta_23=delta_02+delta_13
                                  =delta_03+delta_12.

For instance r_0=(delta_01+delta_02-delta_12)/2 determines the other
three, and the displayed conditions check the remaining edges.
Thus each tetrahedron has the required decoration.

Glue the ideal faces according to T. The unique face isometry with
the prescribed vertex matching preserves its three horocycles:
the signed lengths on the three sides agree. Indeed a change of the
three horocycles preserving all three side lengths would have
r_0+r_1=r_1+r_2=r_2+r_0=0, hence all r_i=0.

These decorations therefore match across EVERY face. Around an edge
there is no residual dilation, since the horospheres at its ends
return to themselves. Its total positive dihedral angle is exactly
2pi by E theta=2pi. Thus the edge has an ordinary hyperbolic
neighborhood, with neither a cone angle nor a translation defect.
There are no finite vertices to check.

First shrink the compatible horospheres, by one common factor for
each cusp, until they cut actual triangular corners and the finitely
many corner neighborhoods are disjoint. Their matched triangles then
form a nonsingular Euclidean metric on each compact link torus. It is
complete; its universal development is the whole Euclidean plane.
These corner neighborhoods give full complete
horoball ends. The remaining core is compact. Hence the glued metric
is complete, of curvature -1 and finite volume, on the ACTUAL M.
Its volume is the sum of its tetrahedral volumes, V_T(theta_src).
This proves (3). To compare with a separately specified complete
metric, one can also apply the two marked representation-volume
inequalities in opposite directions, as in the existing
[geometric equality proof](general_source_regulator_hyperbolic_equality.md).

No universal existence theorem for positive ideal triangulations is
used in this implication. An actual positive theta_src is an input.

## 4. Eliminating internal variables is legitimate when they are optimized

There are two sufficient ways to verify the full stationarity in (1).

**Reduced optimization.** Choose affine coordinates (y,x) on the
allowed angle domain, with y internal and x the retained source
variables. Suppose the internal solution y(x) is an interior critical
point in EVERY y direction, and define

    W(x)=V_T(y(x),x).

Strict concavity makes each such internal point the unique fiber
maximum. Its internal Hessian is invertible, so the implicit function
theorem gives a smooth local y(x). The chain rule gives

    dW=partial_x V_T,

because partial_y V_T=0. A critical point of W is therefore a critical
point of the full V_T. This justifies coherent elimination if the
eliminated action has been proved to be THIS fiber maximum. Naming
an arbitrary reduced source action W is insufficient.

**Full gluing and the boundary pairing.** The route already used by
the actual source is more intrinsic. With x_t=Log z_t,
y_t=Log(1-z_t^(-1)), a direct sine-rule calculation gives

    dV_T(delta theta)
       =sum_t[Re x_t delta Im y_t-Re y_t delta Im x_t].

At a full complex edge-gluing solution, the edge/peripheral
symplectic reduction yields, for EVERY edge-angle tangent,

    dV_T=(1/2)sum_i[Re V_i dIm U_i-Re U_i dIm V_i].  (8)

Here U_i,V_i are the actual small logarithms of the squared peripheral
eigenvalues, in the fixed oriented marking of our notes. Full edge
gluing kills the internal directions; the remaining quotient consists
of these boundary directions. At a complete point U_i=V_i=0, (8)
proves stationarity on all of P.

The [tangent-space audit](source_angle_stationarity_critical_audit.md)
states the necessary full-rank edge/peripheral hypotheses and proves
the analogous equivalence for arbitrary Lagrangian boundary slices.
In particular this is stronger than differentiating volume merely
along a family of already-glued representations.

## 5. The actual long-filling source passes the filled certificate

For a filled cusp, take a primitive slope a_i mu_i+b_i lambda_i and
its actual log equation

    a_i U_i+b_i V_i=2pi i epsilon_i, epsilon_i=+/-1. (9)

The affine angle constraints fix
a_i Im U_i+b_i Im V_i=2pi epsilon_i. The real part of (9)
annihilates (8) on every tangent to that constraint. Retained cusps
are complete. Thus a positive source point satisfying full complex
edge gluing and (9) is stationary on the ENTIRE filled angle slice.
Strict concavity again makes it the unique global maximum.

For our selected source these inputs are established as follows:

* The [literal port lift](actual_pretzel_port_lift_and_geometric_anchor.md)
  is a representation of the actual augmented-link group, based at
  its explicitly constructed complete oriented geometry. The
  [direct positive ideal subdivision](actual_pretzel_positive_ideal_angle_certificate.md)
  supplies a compatible ideal chart for these actual cells, with no
  general triangulation existence assumption. Transporting this fixed
  positive triangulation by its marked flags gives the
  positive source point for sufficiently long fixed fillings.
* Its source equation is U_i+p_i V_i=-2pi i on the selected unit-charge
  branch. The [primitive-period proof](actual_long_pretzel_primitive_filling_angle.md)
  fixes this as an actual period, not a congruence modulo 2pi i.
* The [marked action calculation](actual_pretzel_marked_regulator_and_filling_action.md)
  proves V_src,s(p)=V_T(theta_p), including the actual filling
  quadratic and the absolute complete-volume anchor. There is no
  unidentified boundary constant left in this equality.
* The [geometric completion](actual_long_pretzel_geometric_filling_completion.md)
  proves that these primitive periods close to smooth solid tori,
  with complete retained ends. This rules out a cone metric or a
  multiple covering at the core.

Consequently

    V_src,s(p)=max_(closure P_p) V_T
                           =Vol(S^3 minus K_p).      (10)

The complete augmented value V_s instead belongs to the unfilled
boundary problem. It cannot simply be substituted for V_src,s(p).

The [improved whole-source bound](actual_pretzel_all_width_extension.md)
gives the original quantum limit needed above for every fixed odd
width s>=9 and independently sufficiently long fixed signed p_i.
The same note records even widths s>=10 for the specified single-cut
two-component link invariant. These are the current quantum scopes;
the classical certificate itself has no pretzel-width restriction.

For a new source, once its limit is proved, the next work is precisely
to supply its positive angle point, full stationarity and absolutely
normalized volume equality on the actual topology. No further
asymptotic theorem is needed AFTER those certificates hold. The
existence of an abstract source rate alone supplies none of them.
