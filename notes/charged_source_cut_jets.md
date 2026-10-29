# Exact global cut jets of the original charged source

28 October 2026. Every anchor cluster has an exact finite normal-jet
description in the ORIGINAL charged source. A negative cut deficit
kills the source. A zero deficit factors it. Fixed, and even sublinear,
deficits have subexponential boundary-choice cost for a fixed diagram.
These assertions retain the two resulting periods; they are not scalar
volume estimates or claims that a nonzero period cannot cancel.

The input is the actual [charged bridge coefficient](actual_global_charged_bridge_flow.md)
and its [specified nilpotent/Fermat functional](actual_charged_socle_and_fermat_source.md):

    K_N=chi_N/N sum_h W_h lambda(P_h),
    lambda(P)=[X_1^d ... X_k^d]P, d=N-1.             (1)

All clocks, W_h, pivots, and chi_N remain. Each statement below is
termwise in these actual clocks, so summing it gives exactly (1).
The number of h states is polynomial in N for a fixed diagram; the
theorems do not replace their signed sum by a positive one.

## 1. A cluster has an exact normal deficit

It is useful to allow remaining charges q_v>=0, not only q_v=d.
Let P be a product of M nonzero binary linear factors, with
sum_v q_v=M. Multiple factors and self-loops are allowed. Evaluate
a self-loop as its actual scalar times X_v; if its scalar is zero,
P is zero. Such a monomial is a factor with its one endpoint counted
once in the definitions below. All its scalar factors are retained.

For a set I of anchors put

    m_I=number of factors supported entirely in I,
    e_I=q(I)-m_I, q(I)=sum_(v in I)q_v.             (2)

Let J be its complement and let C_I be the set of crossing factors.
Write each crossing factor with its actual coefficients as

    a_f X_(o_f)+b_f X_(i_f), o_f in J, i_f in I.

Write P_I,P_J for the internal products. Then EXACTLY

    lambda_q(P)=sum_(S subset C_I, |S|=e_I)
       (product_(f in S)b_f)(product_(f notin S)a_f)
       *[X_I^(q_I)] P_I product_(f in S)X_(i_f)
       *[X_J^(q_J)] P_J product_(f notin S)X_(o_f). (3)

An empty or impossible subset sum is zero. In particular e_I<0,
or e_I>|C_I|, kills the source. For e_I=0 this is the SINGLE product

    [X_I^(q_I)]P_I
       *[X_J^(q_J)]P_J product_(f in C_I)a_f X_(o_f). (4)

Thus a tight cut really factors the actual selected coefficient.
No normalized knot value is used to choose the scalar.

Proof. Every internal factor contributes one unit of degree in I.
Exactly e_I of the crossing factors must choose their I endpoint
to supply its source charge. Expanding only those choices proves
(3); all other variables remain in their specified source pairings.

Equivalently rescale X_v -> t X_v for v in I. Then

    P(tX_I,X_J)=t^m_I P_I P_J
                   product_(f in C_I)(a_f X_(o_f)+t b_f X_(i_f)).

The original source selects total t-degree q(I), so (3) is precisely
the order-e_I normal jet. This is an algebraic coefficient identity,
not an assumed deformation of a full-Psi contour or its logarithmic
sheets. In the usual relative radial coordinate it is the same
normal coefficient selected by t^(-e_I)dt/t.

## 2. What its norm controls

For the original crossing factors, |a_f|=|b_f|=1. Coefficients of
the boundary-jet polynomial therefore obey

    ||[t^e] product_(f in C_I)(a_f X_(o_f)+t b_f X_(i_f))||_1
                                  <=binom(|C_I|,e). (5)

This follows by counting the subsets before combining equal
monomials. It is a norm bound only on the boundary-choice polynomial,
NOT on either remaining source value in (3). Arbitrary coefficients
give the corresponding sum of products of their moduli instead.
Internal self-loop scalars, W_h and all extracted fusion scalars
are not included in or discarded by (5).

For a fixed original diagram, |C_I|<=C_diagram N. Thus fixed e costs
at most (C_diagram N)^e. More generally, if

    min(e_I, |C_I|-e_I)=o(N),

the bound (5) is exp(o(N)), using
log binom(M,e)<=u log(euler_number*M/u), u=min(e,M-e),
with the zero endpoint understood by continuity. No fixed jet-order
hypothesis is needed for this subexponential conclusion. A genuinely
macroscopic interior deficit can have exponentially many boundary
choices; (5) then supplies no tame-cost assertion.

## 3. The Hall test decides support, not the selected value

There exists an assignment of each factor to one of its endpoints,
with exactly q_v choices at every anchor, IF AND ONLY IF

    m_I<=q(I) for EVERY anchor set I.               (6)

Necessity is immediate: every internal factor must choose inside I.
For sufficiency build a largest partial assignment respecting the
charges. If an unassigned factor remains, follow its endpoints, then
factors already assigned there, and their alternative endpoints.
If a reached anchor has spare charge, an alternating path increases
the assignment. Otherwise all reached anchors are full. All their
assigned factors, and the initial unassigned factor, have both
endpoints among the reached anchors: otherwise that new endpoint
would also have been reached. There are more than q(I) such internal
factors, contradicting (6). This argument covers multiple edges and
one-endpoint factors without change.

The implication is a test for FEASIBLE ENDPOINT SUPPORT. It does NOT
say lambda_q(P) is nonzero. The two-factor polynomial
(X-Y)(X+Y), charge (1,1), satisfies (6) and has zero selected
coefficient. The actual charged source also has such phase
cancellations, including complete root-orbit annihilations.

Tight sets (e_I=0) are closed under union and intersection whenever
(6) holds. Indeed q is modular and m is supermodular. More precisely,

    e_I+e_J-e_(I union J)-e_(I intersection J)
       =number of factors joining I\J to J\I.      (7)

For two tight sets every term on the right is forced to zero, and
both new deficits vanish. Thus their factorizations are compatible,
rather than unrelated guesses about separate source sectors.

### A canonical factorization into the residual flow cores

Choose ANY feasible endpoint assignment. Direct each two-endpoint
factor from its assigned anchor to its other endpoint. A one-endpoint
factor is a loop. Take the strongly connected components of this
residual graph. A factor joining distinct components is assigned to
the SAME endpoint in every feasible assignment. To see this, the
edges changed between two assignments have equal indegree and
outdegree at every vertex, hence decompose into directed cycles of
the first residual graph. A changed edge cannot join its distinct
strong components.

Consequently every cross-component factor can be replaced by its
forced coefficient times its forced endpoint monomial. The source
then factors EXACTLY over the remaining component polynomials, with
charges reduced by those forced monomials. This is also obtained by
successively applying (4) to sink components. Reversing the cycles
which connect two feasible assignments preserves residual strong
components, so the component partition is independent of the chosen
assignment. Inside a nontrivial component no proper tight subset
remains relative to its reduced charges.

This isolates the genuine phase-coupled cores. Their coefficients
can still vanish. It is not a quantum determinant or positivity
theorem.

## 4. Nested flags control coordinate corners jointly

Let I_1 subset ... subset I_r be a proper nested flag of anchor sets.
Scale X_v by product_(ell:v in I_ell)t_ell. Factor out
product_ell t_ell^(m_(I_ell)). Let P_cell be the products of factors
whose endpoints lie in the same flag layer. The other factors form
a polynomial K_flag(X,t): each endpoint term carries precisely the
t_ell for cuts which separate that endpoint from the other one.
There is the exact joint formula

    lambda_q(P)=lambda_q[ product_cells P_cell
                    *[t_1^(e_I1)...t_r^(e_Ir)]K_flag(X,t)]. (8)

In particular these are not independent normal residues with
unretained corner corrections. The SAME boundary endpoint choice
must satisfy every cut. Its collection of selected-inside crossing
factors has cardinalities e_(I_ell), and determines that choice
uniquely. Therefore, for the original unit coefficients,

    ||[t^e]K_flag||_1
                    <=product_ell binom(|C_(I_ell)|,e_(I_ell)). (9)

Every coordinate radial cone, after removing the common homogeneous
scale, is described by an ordered nested flag. Thus (8) covers its
full finite normal jet, including corners. The flag length is bounded
by the fixed number of anchors. If all its normal deficits are at
sublinear distance from an endpoint, (9) costs exp(o(N)). At zero
deficits it reduces to compatible successive exact factorizations.

### Integral weighted rays and their exact single normal jet

For arbitrary integers w_v>=0 with min_v w_v=0, scale
X_v=t^(w_v)Y_v. Put

    l_w=sum_f min(w_(i_f),w_(j_f)),
    e_w=sum_v q_v w_v-l_w.

A one-endpoint factor contributes its one endpoint's weight to l_w.
Normalize every factor by this minimum power of t. A factor joining
different weight levels has one constant endpoint and one endpoint
of degree |w_i-w_j| in t. The EXACT source is the order-e_w normal
coefficient of this normalized product. The layer-cake identity is

    e_w=sum_(r=1)^(max w) e_(I_r), I_r={v:w_v>=r}.   (10)

It follows either by counting the thresholds below each endpoint
or by summing the indicator functions of the I_r. The charges in
(10) can be the reduced q_v left after earlier exact fusions.

If the source is feasible all summands are nonnegative. At e_w=0
the factors joining distinct levels are forced to their lower-weight
endpoints, and the source factors over its equal-weight layers.
At e_w>=0 at most e_w unequal-level factors can choose their
higher-weight endpoints. Thus their boundary-jet coefficient norm is
at most

    sum_(j=0)^min(e_w,M_cross) binom(M_cross,j)
                       <=(e_w+1) max(1,M_cross)^(e_w). (11)

This counts only boundary choices; all equal-level products and
their actual remaining source pairings are retained. For a fixed
diagram the displayed polynomial bound gives subexponential cost
if e_w log N=o(N). The sharper binomial-sum bound gives the same
conclusion already when e_w=o(N), by the elementary entropy bound
and M_cross=O(N). These statements allow weighted ray directions
depending on N; they do not replace an irrational radial path by
an unproved uniform analytic limit.

Together (8) and (10) cover the exact source jets of coordinate
flags and every integral weighted coordinate escape.
This does not control noncoordinate hyperplane collisions, nor the
remaining component periods at an escaping critical configuration.
Even a polynomially bounded boundary jet can pair to zero or to an
exponentially large exterior period. A hyperbolic-volume upper or
lower bound therefore still requires a phase-aware estimate or
geometric source comparison for the surviving cores. The result here
is the exact global source reduction and its stated normal-jet cost.

[Audit](../experiments/audit_charged_source_cut_jets.py): general
charges, loops and multiple factors, Hall feasibility versus phase
vanishing, actual original charged polynomials, cut factorizations,
residual-core factorizations, and joint nested normal jets.
