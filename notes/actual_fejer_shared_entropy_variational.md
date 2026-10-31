# The actual Fejér source: a general shared entropy theorem

Status update, 31 October 2026: the separate [full endpoint theorem](general_fejer_endpoint_source_volume.md) now proves the geometric upper bound (14), and the [unique-maximizer theorem](actual_fejer_unique_geometric_maximizer.md) proves concentration at the complete configuration. The pattern-specific support theorem below is preserved; full-kernel support no longer requires pattern selection. The filled-knot quantum limit remains open.

31 October 2026. This concerns the positive
endpoint numerator in the original homogeneous compiler, at even levels.
It does not assert a quantum filling asymptotic or identify the new
maximum with hyperbolic volume. All faces, incidences and marked targets
are the actual ones. No independently optimized local norm is substituted.

Let N=2m, d=N-1, M=m-1. Fix a connected original flat plat D with R
ports, R ordinary faces and the two original protected faces u,v. Write
the ordered local faces at port e as (x_e,b_e,c_e,y_e), allowing repeated
global labels through the literal incidence map. Let

    P_e=-H_(V_N(-2)), V_N(sigma)=chi_N(sigma)(sigma-Omega)^(-1),
    Z_(D,N)=[prod_(f ordinary)L_f^d] prod_e P_e |_(L_u=L_v=0).

The sign has made each local polynomial positive. The [original homogeneous theorem](actual_homogeneous_casimir_face_source.md) makes this the same marked endpoint-numerator source,
up to its recorded common sign, with no new powers of N. All statements
below are about this source; it is not being renamed Kashaev's invariant.

## 1. The local entropies, including boundary degrees

Define on 0<=mu<=nu<=1/2, 0<=xi<=nu-mu

    E(mu,nu,xi)=inf_(l in R){integral_mu^nu g(t,l)dt-xi*l},
    g(t,l)=l/2+log(tan(pi*t))
                     +asinh(tan(pi*t)*cosh(l/2)).          (1)

The integral is improper at 0 and 1/2, with integrable logarithmic
singularities. If mu=nu then xi=0 and E=0. The [closed-coefficient theorem](actual_fejer_half_block_entropy.md)
proves continuity of E on this compact domain and uniform convergence
of the logarithms of ALL actual half-block coefficients divided by N
to E, including zero outer degrees and endpoint rows. Its proof uses
the original continuant, negative-root coefficient factorization in
strict interiors, and explicit monomer bounds at the endpoints. It
does not infer coefficient asymptotics by differentiating a weighted
limit. The multiplier 4/a_i has logarithm O(log N) uniformly.

The left type has normalized exponent vector and entropy

    q_left=(xi,mu,1-nu,nu-mu-xi),   E_left=E(mu,nu,xi), (2)

in the order (x,b,c,y). Right paths are the actual row reflection, so

    q_right=(xi,1-nu,mu,nu-mu-xi), E_right=E(mu,nu,xi). (3)

For a triangular maximal complete block, put

    C(alpha_x,alpha_b,alpha_y)=E(alpha_b,1/2,alpha_x),
    alpha_x+alpha_b+alpha_y=1/2, alpha_j>=0.            (4)

This is the ACTUAL triangular coefficient entropy. Indeed its path
polynomial D_b=R_M^* is coefficientwise between R_M/sqrt(C_N) and R_M,
with 1<=C_N<2, while the j=M term of P_left is exactly 2c^m R_M.
The leading-coefficient normalization C_front is only polynomial in N.
Thus (4) follows from the same closed half-block lemma, with its absolute
normalization. Equivalently, using the already fixed triangle potential,

    C(alpha)=V(2pi*alpha)/(2pi),
    V(theta)=2sum_j[Lambda(theta_j/2)+Lambda((pi-theta_j)/2)],
    sum_j theta_j=pi.                                 (5)

One can verify (5) by the source triangle gradient formula and its
already normalized positive-radius Legendre duality. Formula (4) alone
suffices for the theorem below.

A cross type uses two triangular vectors alpha,beta, each of sum1/2:

    q_cross=(alpha_x+beta_x,alpha_b,beta_c,alpha_y+beta_y),
    E_cross=C(alpha)+C(beta).                         (6)

When a local exponent vector q is fixed, maximize the right side of (6)
over its allowed outer split. The exact identity
B=4(x+y)D_b D_c and the coefficientwise comparison
(N/2)H_M<=P_cross<=(3N/2)H_M prove this local coefficient limit. The
forced x+y has degree1 and must be retained at finite N; its contribution
to the limiting degree vector is zero. There are only O(N) outer splits.
Boundary splits are included by the continuous closed lemma, not omitted.

## 2. Retain eventual feasibility before taking the scaled limit

At a finite even level the local supports are EXACTLY:

    cross: nonnegative (k,i,t,l), sum=d, i,t<=m-1;
    left:  nonnegative (k,i,t,l), sum=d, t>=m;
    right: nonnegative (k,i,t,l), sum=d, i>=m.          (7)

Every allowed coefficient is positive. For left/right a path consisting
entirely of one-steps supplies every outer monomial. For cross the two
positive triangular polynomials and their forced x+y supply every vector
in (7); their coefficientwise comparison transfers positivity to P_cross.

Fix one assignment s in {cross,left,right}^R. Its shared exponent arrays
are bounded bipartite flows: a port supplies d, an ordinary face demands d,
a protected face demands0, and each literal incidence is an arc. Impose
the middle-arc bounds in (7), with all other bounds0<=q<=d. Multiple
incidences remain separate arcs. All supplies, demands and bounds are
integers affine in m. Subtract lower bounds and apply the elementary
augmenting-path max-flow argument. Feasibility is equivalent to a finite
set of cut inequalities, each of the form a*m+b>=0, together with the
nonnegative residual supplies/demands. Therefore each assignment is either
feasible at EVERY sufficiently large integer m, or infeasible at every
sufficiently large m. There is no unproved arithmetic subsequence.

There is also a uniform explicit test level. Each residual port supply
has constant term -1; each residual ordinary-face demand has constant
term -1 and each protected demand has constant term0. Every residual
incidence capacity has constant term -1. In a cut inequality

    sum_(f in B) demand_f + sum_(e in A,f notin B) capacity_(e,f)
                                      -sum_(e in A) supply_e >=0,

the constant term therefore lies between -5R and R, since there are
R ordinary faces and 4R incidence arcs. The other nonnegativity conditions
have constant terms -1 or0. Every slope is an integer. Hence at
m_*=5R+1 all positive-slope inequalities hold and all negative-slope
inequalities fail; the zero-slope conditions are unchanged. Consequently
an assignment is eventually feasible IF AND ONLY IF its bounded integer
flow is feasible at this ONE level m_*. The same verdict then holds at
every m>=m_*. This is a finite source-incidence test, not a numerical
asymptotic heuristic; no entropy convexity is used.

Let A_D consist of the eventually feasible assignments. This is a finite,
level-independent combinatorial test. It is essential to make this test
before replacing m/N by1/2: a limiting inequality can be an equality
while its original finite inequality is violated by1. In particular two
overloads on one ordinary face are impossible because 2m>d, even though
their limiting loads would sum to1. No protected face can be overloaded.
The [original gap-graph theorem](actual_fejer_cross_half_source_reduction.md) then makes every noncross assignment in
A_D a rooted forest, with its prescribed orientation. No arbitrary graph
or re-marking is introduced.

An exact example shows why a terminal equality does not permit deleting
one forest label. For the certified width-three word [1,3,0,2,4,1,3],
the protected faces are 0,8 and the ordered port quartets are

    (1,0,4,2), (2,0,5,3), (0,1,6,4), (4,2,7,5),
    (5,3,8,0), (6,4,0,7), (7,5,0,8).

Take right types at ports4,6 (zero-based) and cross types elsewhere.
For every m>=2, the following rows give an actual feasible integer flow:

    (m,0,1,m-2), (m,0,0,m-1), (0,m-1,m-1,1),
    (2m-3,1,1,0), (m-1,m,0,0), (m,0,0,m-1),
    (m-1,m,0,0).

All ordinary targets equal 2m-1. Its scaled terminal point has nu_4=1/2,
where the local right entropy and degree vector admit a cross description.
Nevertheless changing ONLY port4 to cross is infeasible at every m:
its protected c8,y0 force x5>=m since b3<=m-1, while the retained
right port6 forces b5>=m. Face5 would receive at least 2m>2m-1.
This is an obstruction to that relabeling step, not to the volume bound.

For s in A_D, let P_s be the closed limiting flow polytope: port supply1,
ordinary demand1, protected demand0, cross middle upper bounds1/2, and
one-sided middle lower bound1/2. On cross ports retain the triangular
split in (6), or equivalently maximize over that split after fixing q.

## 3. Every limiting flow is approximated by actual integer source degrees

Here is an elementary argument avoiding any convexity hypothesis on E.
Fix q in P_s. Clamp its entries to the finite-N bounds after division by N.
This changes each entry by O(1/N), so the node-balance defects are O(1/N).
Choose ANY feasible real finite-N flow, which exists by eventual
feasibility. Its signed difference from the clamped flow is a directed
residual flow. Decompose it into simple defect-to-defect paths and cycles.
Discard cycles. Each retained edge adjustment is in the direction of the
chosen feasible flow and has no larger magnitude, so it respects the
finite bounds. The path part has the required divergences. Its total
mass is O(1/N), and each simple path has length bounded by the FIXED
incidence graph. Thus it repairs q by O(1/N) to a feasible finite-N flow.
The estimate is uniform in q.

Multiply by N. Supplies, demands and bounds are integers. Round inside
the floor/ceiling interval of each entry by cancelling fractional cycles
in the bipartite graph. A node incident to a fractional edge cannot have
fractional degree1 because its balance is integer. Hence a fractional
cycle exists until all entries are integral. Alternating increments on
that cycle preserve every balance; move until some entry is integral.
Each step respects the original integer bounds. The final rounding error
is at most1 in each entry. This constructs an actual source degree vector
whose scaled value tends to q.

For cross ports choose the two triangular outer allocations and the
one forced x/y factor after the incidence rounding. All local allocations
are intervals with integer endpoints. Their rescaled endpoints converge
to the endpoints of the limiting allocation interval, so any prescribed
limiting split has an integer approximation, still respecting the SAME
total q. This retains the finite forced factor even at zero outer degrees;
the finite support has at least one outer unit.

Conversely every sequence of scaled feasible integer flows has a
subsequence converging to P_s. These two statements supply precisely
the lattice approximation needed below.

## 4. General shared variational theorem

Define the finite classical optimization problem

    W_D=max_(s in A_D) max_(q in P_s)
                   sum_e E_(s_e)(q_e),                (8)

with the triangular splitting variables of (6) retained. All domains
are compact and all local entropies are continuous. Then, provided
A_D is nonempty,

    lim_(even N->infinity) N^(-1) log Z_(D,N)=W_D.      (9)

Proof. Expand the original positive product by the three disjoint local
supports in (7), then by its incidence degrees. At cross ports the exact
coefficientwise bounds B<=P_cross<=3B permit replacing P_cross by
B=4(x+y)D_b D_c for this rate calculation: after the other positive
factors and the SAME target extraction, the whole assignment is trapped
between the replaced coefficient and 3^(number of cross ports) times it.
Only this replaced coefficient is expanded into triangular splits; an
exact factorization of P_cross itself is not asserted. The number of
terms is polynomial in N because D is fixed. Every
nonzero term has its logarithmic rate given by the uniform closed local
coefficient theorems in section1. Compactness therefore bounds the
limsup by (8). For the liminf choose a maximizer, use section3 to realize
its actual integer degrees and splits at every sufficiently large even
N, and retain that single positive term. Its rate tends to (8). There
is no cancellation and no independent optimization of repeated faces.

If A_D is empty, the original positive coefficient is eventually zero;
one can use W_D=-infinity. Under the [existing labeled right-angled
geometric certificate](general_signed_augmented_source_volume.md) the all-cross term is nonzero and has rate

    Phi_D=Vol(Y_D)/(2pi),

so W_D>=Phi_D. The theorem does NOT prove the reverse inequality.

## 5. The central forest corridor already has the geometric rate

Under the same labeled right-angled certificate, there is a genuine
shared coefficient estimate near the central row. For a left path put
k=M-j, so its overloaded exponent is m+k; for a right path use the
reflected k=i-m. If all such k are at most delta*N, then the source
formed by these terms together with the all-cross term obeys

    Phi_D <= liminf_(even N) N^-1 log Z_(D,N,delta)
           <=limsup_(even N) N^-1 log Z_(D,N,delta)
           <=Phi_D+C_D*delta*(1+log(1/delta)).          (10)

In particular if every noncross excess is restricted to K_N=o(N),
the restricted source INCLUDING all-cross has limit Phi_D. The bound
is valid at arbitrary fixed width and keeps both protected targets.

Here is the exact transfer estimate behind this assertion. Put
A_j=2+c_j, delta_N=A_M, and let R_j be the lower-block path numerator
starting at j with all b powers retained. A positive path injection
gives

    R_(j+1)>=A_j*b*R_j, 0<=j<M.                        (11)

To prove it, raise every visited row by1. Both allowed sine step
weights increase on this half interval. If U is the old unused set,
the new unused set is {0} union(U+1), and its spectral-factor ratio is

    A_0*product_(r in U)(A_(r+1)/A_r)>=A_j,

since all omitted ratios are at most1 and the full product telescopes.
The outer exponents are unchanged and the b power increases by1.
Iterating in the positive LAURENT coefficient order and using the
literal half-block expansion gives

    P_left<=2c^m R_M sum_(j=0)^M (delta_N/A_j)(c/b)^(M-j).

The paired-root comparison supplies R_M<=sqrt(C_N)D_b and
D_c>=C_front*c^M, where

    C_N=4(4-delta_N)/(delta_N*N^2),
    C_front=N/sqrt(delta_N*(4-delta_N)),
    H_M=8(x+y)D_bD_c/N.

Consequently the individual excess-k piece is bounded coefficientwise by

    P_(left,k)<=a_(N,k)*[H_M/(x+y)]*c^(k+1)*b^(-k),
    a_(N,k)=(4-delta_N)/(2N)*delta_N/A_(M-k)<=2/N.     (12)

The reflected formula interchanges b,c. This is an inequality for
the original polynomials inside a finite Laurent ring; it does not
replace a one-sided port by an identity coupon. In particular the
remaining coefficient target changes by

    gamma_e=(k_e+1)e_overloaded-k_e e_parent.          (13)

A protected parent may therefore acquire a POSITIVE remaining target.
It must not be set to zero before extracting that shifted coefficient.

To obtain (10), take the original complete geometric curvature vector
and replace its two zero marked entries by one epsilon>0, leaving all
ordinary entries unchanged. This is ONE shared radius vector, fixed
before N. At a certified port the outer matching pair cannot be the
marked MAIN pair, so x+y stays bounded below; a fixed power of epsilon
would also suffice here. The Laurent factors in (12) cost at most
exp[C_D*delta*N*(1+log(1/epsilon))], with fixed extra constants.
There are polynomially many k choices and finitely many assignments.
Positive Cauchy applied to the original target thus bounds the entire
restricted coefficient by the complete product at that shared vector
times this exponential cost and a polynomial in N. No shifted marked
target is discarded.

The complete capacity at these regularized radii is at most
Phi_D+C_D*sqrt(epsilon). Indeed its log-radius derivative is the actual
center angle divided by2pi. A single regularized zero corner has angle
O(epsilon); two simultaneously regularized zero corners in a triangle
have angles O(sqrt(epsilon)). Integrating from0 to epsilon and summing
the finitely many triangles gives this modulus. The original target
logs involve only the unchanged ordinary faces. All beta, forced-factor
and other retained scalar logarithms are o(N).

Choose epsilon=delta^2, FIXED before N. This proves the upper estimate
in (10); all-cross gives its lower estimate. For K_N=o(N), first let
N tend to infinity at each fixed delta, then delta tend to zero.
This argument does not use a downhill-radius condition. It shows that
the unresolved positive-source maximum requires a genuinely macroscopic
one-sided excess, rather than an omitted central endpoint window.

## 6. The geometric comparison and the remaining quantum assertion

The geometric problem isolated by this variational theorem was the inequality

    W_D<=Vol(Y_D)/(2pi).                               (14)

This is a problem about the actual compact constrained entropy maximum,
including every admissible forest and boundary stratum. It is not the
unjustified interchange of inf over shared radii and max over local
weighted branches. Indeed the fixed-degree coefficient entropy can be
nonconvex in a terminal row, so that shortcut is unavailable.

At full interior critical points, the half-block equations have the
parabolic Casimir energy sigma=-2 and the actual local action
F(x,b,y)-F(x,c,y)+log c (or its reflected version). Developing these
critical points and their boundary strata into actual augmented-group
representations with the correct regulator proves (14) in the separate
[endpoint theorem](general_fejer_endpoint_source_volume.md); it is not
assumed in (9). The positive endpoint identity (9) still does not select the original Gaussian filling cycle or its
nonzero geometric coefficient. The fixed signed long-filled knot
volume conjecture remains a further phase-sensitive assertion.

## 7. Verification and scope

The [focused shared-source audit](../experiments/audit_actual_fejer_shared_entropy_variational.py)
and [results](../experiments/actual_fejer_shared_entropy_variational_results.json)
compare 228 original numerator coefficients, 4590 actual marked support
patterns against bounded integer flows, 748302 affine-cut conditions,
118 explicit one-level certificates, and 236 eventual-flow checks.
The width-three chart has 39 feasible path assignments at N=4 and 40
at N=6; the finite support distinction is retained. These checks support
the exact source/flow interface, not a numerical proof of the limit.

The [separate transfer audit](../experiments/audit_actual_fejer_forest_transfer.py)
and [results](../experiments/actual_fejer_forest_transfer_results.json)
check the exact path injection and Laurent coefficient comparison used
in section5: 3045 injection coefficients, 679 paired-root comparisons,
39599 Laurent-transfer coefficients, 42 scalar identities and 42 conditional
radius checks at 14 even levels and 90 digits. The conditional radius
checks are not substituted for the shared regularization argument.

The full asymptotic theorem follows from sections 1–4 and the uniform local theorem. The later endpoint theorem evaluates the geometric maximum. This note alone does not settle the phase-sensitive filled-knot limit.

The finite source checks include the all-m terminal-relabel countercertificate and the width-three support distinction of 39 versus 40. They do not establish a geometric maximum or a quantum-cycle estimate.