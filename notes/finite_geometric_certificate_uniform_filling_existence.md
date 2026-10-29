# A finite positive certificate supplies every sufficiently long filling branch

29 October 2026. This is a geometric strengthening of the
[finite real-algebraic certificate](finite_real_algebraic_geometric_certificate.md).
When that certificate succeeds for the ACTUAL marked base exterior, its
meridian-coordinate germ supplies existence, not merely a conditional
completion statement, for all independently sufficiently long primitive
slopes. The proof uses the certified Jacobian, elementary affine cusp
commutation, and a uniform contraction. It does not supply a quantum
source packet for a new diagram.

## 1. Precise scope

Let the finite certificate exhibit a positive complete shape assignment
on an oriented ideal triangulation of the marked manifold M. In
particular its edge links are circles, vertex links are tori, edge
products have winding ONE, and both primitive peripheral multipliers
are one. Its marking is a verified oriented homeomorphism to M, not
only a degree-one map or an agreement of trace data.

Use actual peripheral bases (mu_i, lambda_i) whose complete translation
ratio has positive imaginary part. Write U_i,V_i for the small logs of
their complex similarity multipliers, so these are squared-eigenvalue
logs, with central SL signs already removed. The certified edge-plus-
meridian Jacobian gives a holomorphic shape germ with coordinates
U=(U_1,...,U_h). Developing finitely many tetrahedra produces an ACTUAL
framed holomorphic representation rho_U in bounded charts near the
complete holonomy. The selected peripheral fixed flags are the developed
ideal vertices. All shapes remain positive after one fixed shrink.

For every chosen subset I of cusps and every primitive integer slope
(a_i,b_i) at i in I, put ell_i=sqrt(a_i^2+b_i^2). There is a fixed L_M
such that, whenever min_(i in I) ell_i > L_M, and for every independent
choice epsilon_i=+1 or -1, the specified germ has a UNIQUE nearby point

    U_i=0                         (i not in I),
    a_i U_i+b_i V_i=2pi i epsilon_i (i in I).             (1)

The word UNIQUE refers to this fixed marked decorated gluing germ. It
does not assert uniqueness of other character components. Its point
gives a positively oriented complete finite-volume hyperbolic metric
on the actual indicated filling, by the
[general completion construction](general_source_regulator_hyperbolic_equality.md).
The threshold is uniform over signs and over independently unequal
lengths. There is no prime-level or quantum parameter in this theorem.

## 2. Cusp commutation forces a diagonal first-order peripheral map

In the moving selected-flag frame at cusp i, write its commuting affine
holonomies as

    mu_i(w)=exp(U_i) w+B_i(U),
    lambda_i(w)=exp(V_i(U)) w+D_i(U).

The finite developed words make B_i,D_i holomorphic, and B_i(0),D_i(0)
are the nonzero complete translation periods. Commutation gives EXACTLY

    (exp(U_i)-1) D_i=(exp(V_i)-1) B_i.                  (2)

Shrink so B_i never vanishes. On U_i=0, equation(2) gives exp(V_i)=1;
the chosen small log is therefore V_i=0. Holomorphic division gives

    V_i(U)=U_i tau_i(U),
    tau_i(0)=D_i(0)/B_i(0),  Im tau_i(0)>0.             (3)

This applies also while other cusps vary. In particular dV_i/dU_j=0
at zero for j!=i, and dV_i/dU_i is the ACTUAL Euclidean cusp ratio.
This does not infer a physical quantum-color Hessian from a Casimir
spectral coordinate. Matching a source Hessian to these logs is a
separate source/peripheral calculation.

## 3. A contraction uniform over all primitive slope directions

Choose a closed complex polydisk ||U||_infinity<=r on which every tau_i
is holomorphic and

    Im tau_i>=m>0,  |tau_i|<=T,
    sum_j |partial_j tau_i|<=L.                         (4)

These inequalities hold after shrinking the certified germ. With

    c=m/sqrt(1+T^2)>0,

the real two-by-two matrix with columns (1,0) and
(Re tau_i, Im tau_i) has determinant at least m and Frobenius norm at
most sqrt(1+T^2). Consequently, for EVERY real pair (a,b),

    |a+b tau_i(U)|>=c sqrt(a^2+b^2).                    (5)

Set all unfilled U coordinates to zero, and define on the remaining
closed polydisk

    (T_sigma(U))_i=2pi i epsilon_i/[a_i+b_i tau_i(U)].   (6)

Equations(3) show that its fixed points are precisely(1). If
ell_min=min_i ell_i, then(4)--(5) give

    ||T_sigma(U)||_infinity<=2pi/(c ell_min),
    ||D T_sigma(U)||_(infinity->infinity)
                         <=2pi L/(c^2 ell_min).        (7)

For example any strict threshold

    ell_min>max(4pi/(c r),4pi L/c^2)                    (8)

makes the image lie in the radius-r/2 polydisk and the Lipschitz
constant less than one half. The mean-value estimate is valid along
complex straight segments because the polydisk is convex. Iteration
therefore converges uniformly to one fixed point, and any solution in
this germ is that fixed point. No largest-to-smallest slope comparison
is used. Primitivity is needed for the filled topology and smooth
meridional angle, not for this analytic contraction itself.

More precisely, for each filled cusp,

    |U_i|<=2pi/(c ell_i),
    U_i=2pi i epsilon_i/[a_i+b_i tau_i(0)]
                                   +O(1/(ell_i ell_min)),            (9)

with one constant for all direction/sign tuples. Subtract the two
fractions in(6) and its value at zero, use
|tau_i(U)-tau_i(0)|<=L||U||_infinity and |b_i|<=ell_i,
to obtain the error in(9). The complete point has no unproved
representation-existence input: it is the one certified shape germ.

## 4. Completion and a uniform volume check

The actual bounded representation rho_U and its flags tend uniformly
to the certified complete data as ell_min tends to infinity. Unfilled
cusps have U_i=V_i=0 by(3), and remain nontrivial parabolic near the
complete point. Filled cusps satisfy the ACTUAL small-log equation(1),
not merely its exponential. Thus the explicit local developing map,
log-link and primitive 2pi tube construction of the general theorem
applies. It fills the specified primitive slopes on the same marked
topology with a smooth complete finite-volume metric. A nonprimitive
slope or a charge of magnitude greater than one would instead be a
different topological/cone assertion and is not silently included.

There is also a useful uniform normalization check. Let Vol(rho_U)
be the absolute marked representation volume. Its already established
boundary differential is

    dVol=(1/2)sum_i[Re V_i dIm U_i-Re U_i dIm V_i].      (10)

Integrate along the straight path sU, 0<=s<=1, in the shape germ.
Using V_i=U_i tau_i(U), the leading integrand is
-s Im tau_i(0)|U_i|^2/2. All remaining terms are bounded by a constant
times ||U||_infinity sum_i |U_i|^2. Hence

    Vol(rho_U)=Vol(M)-(1/4)sum_i Im tau_i(0)|U_i|^2
                      +O(||U||_infinity sum_i |U_i|^2).             (11)

Substituting(9) gives, uniformly over independently long slopes,

    Vol(M(sigma))=Vol(M)
       -pi^2 sum_(i in I) Im tau_i(0)/|a_i+b_i tau_i(0)|^2
       +O(ell_min^(-1) sum_(i in I) ell_i^(-2)).         (12)

This proves the usual geometric volume here from the actual completed
metric and marked fundamental class, rather than assigning a volume
to a formal root of a peripheral polynomial. In particular the volume
decreases strictly for all sufficiently long nonempty fillings.

## 5. What this resolves, and the source estimate it does not replace

The finite positive certificate plus its deduced meridian Jacobian
already removes the GEOMETRIC existence qualification in the general
completion theorem for all sufficiently long primitive slopes. A
separate deformation or discrete-faithfulness theorem need not be
assumed. A source candidate matching this germ and the same primitive
logs can therefore use this result directly.

For a new original quantum source the remaining non-tautological gates
are still those in
[the exact long-filling transfer](general_original_source_long_filling_transfer.md):
an actual PHYSICAL auxiliary-color packet, its nonzero holomorphic
complex-corridor asymptotic, a strict bound on the entire complementary
physical color cube including aliases/normals, and its literal marked
representation/action map with the absolute complete regulator anchor.
The exact twist expansion is already multilinear at arbitrary width.
The new [complete-circle boundary packet](actual_complete_circle_boundary_packet.md)
controls a spectral Casimir coordinate and all its polynomial normal
derivatives. Without its exact physical-color transform and the global
color estimate it does not discharge these source gates. Nor does this
geometric contraction estimate the quantum Cauchy energy on a generic
branched graph.

No files in the frozen publication snapshot were modified in proving
this addendum. Its proof is analytical; no sampled numerical evidence
is used for the slope-uniform assertion.

Independent analytical review: the root and a second reader each
checked the affine divisibility, all-direction lower bound, contraction
and anisotropic errors, primitive-topology input, and both volume
coefficients. Both reported PASS. The uniform assertions follow from
the proof above, not from a finite collection of slope samples.
