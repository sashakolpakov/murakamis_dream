# The positive face coefficient has one global saddle

30 October 2026. The coefficient
below has an exact compact torus integral and a uniform finite Gaussian
asymptotic through both folded parities. The determinant contraction
proves the global angular gap. This is a coefficient theorem; its
identification with the original source uses the separately checked
marked face-grid identity. It does not estimate external filling colors.
Setting the two marked face variables to zero uses only a connected
geometric certificate; it needs neither the finite-r Bessel chart nor
a one-main-component hypothesis.

## 1. The polynomial and its prescribed coefficient

Fix the labeled original right-angled matching graph with R crossing
circles and R+2 white faces. Let u,v be the two marked faces. Set their
variables to zero. Give the other R faces positive variables l_f.
For each actual label vector a=(a_i), let

    P_N(l)=product_i [D_ai(x_i,b_i,y_i)D_ai(x_i,c_i,y_i)
                                      P_si(x_i,y_i)],
    s_i=N-1-2a_i, d=N-1.

Every argument here is its original shared face variable, including
its specified zero when the face is u or v. The
[local source factorization](actual_complete_circle_positive_face_polynomial.md)
proves that P_N is homogeneous of degree dR with nonnegative coefficients.
The coefficient of interest is

    A_N=[product_(f!=u,v) l_f^d] P_N(l).                 (1)

All scalar factors k_ai beta_ai^2, original half twists, and the exact
finite-grid measure are outside P_N and must be restored by the source
identity. They are not absorbed in A_N.

Assume S=sum_i s_i=o(N), with the graph fixed. Both maximal-fold parities
and arbitrary integer near-fold label sequences are included. Let
l^geom be the positive finite white-circle normal coefficients from the
certified packing with u,v represented by parallel lines. Fix one finite
face variable to1 by homogeneity, leaving n=R-1 logarithmic variables.

## 2. An exact global determinant contraction

For any positive semidefinite matrices X_1,...,X_t with M=sum X_j>0,
put A_j=M^-1/2 X_j M^-1/2. Then sum A_j=I. For real theta_j put

    B(theta)=sum_j exp(i theta_j) A_j.

This is a contraction: Vz=(A_j^1/2 z)_j is an isometry and
B=V* diag(exp(i theta_j))V. Cyclicity of trace gives exactly

    Tr(I-B*B)=sum_(j<k)|exp(i theta_j)-exp(i theta_k)|^2
                                               Tr(A_j A_k). (2)

Every pair trace is nonnegative. Since the squared singular values
lambda_l of B are at most1, log lambda_l<=lambda_l-1 proves

    |det B|<=exp[-(1/2)sum_(j<k)|exp(i theta_j)
                              -exp(i theta_k)|^2 Tr(A_j A_k)]. (3)

A zero determinant satisfies the same bound by continuity. No limiting
matrix, independent-entry positivity, or commutativity is required.

Apply (3) to each original D_a, with its nonzero summands bI,
xH_-/2,yH_+/2. When all three are present, the two pair traces involving
the identity summand have lower bounds cN from the exact bulk-square
argument in the [curvature theorem](actual_q_hahn_boundary_model_curvature.md).
For a two-variable220/022 determinant its single pair trace has the
same bound. For202, with b=0, the pair trace is precisely its log-radius
variance; the exact positive-polynomial variance proof gives cN.
A one-variable200/002 determinant is a monomial and has no angular gap.
All constants are uniform on positive compact radius sets near l^geom.

The resulting active pair graph connects all R finite faces. Indeed each
shaded triangle equates its finite-face potentials, and the
[exact rank proof](actual_original_boundary_transverse_rank.md) shows
that deleting u,v leaves a connected graph. The forced polynomials P_s
also have nonnegative coefficients, so their modulus ratio on the torus
is at most1 and cannot weaken (3). Consequently, after fixing one phase,

    |P_N(l exp(i theta))/P_N(l)|
           <=exp[-c_D N dist(theta,0)^2]               (4)

on the entire n-dimensional torus, with its usual periodic distance.
To see the uniform comparison, use a fixed spanning tree: the complex
unit phase difference of any vertex from the fixed vertex is at most
the sum of the edge differences along its path. Compactness then
compares their squared sum with squared torus distance. The only common
zero is the constant phase. Every edge row has literal coefficients
+1,-1, so there are no other angular aliases.

## 3. The finite positive critical radius

In logarithmic finite-face coordinates define

    Phi_N(z)=log P_N(l^geom exp z)-d sum_f z_f.          (5)

The actual circle-center angle force at the fold gives

    N^-1 partial Phi_N(0) ->0.                         (6)

For each shaded triangle the determinant derivative tends to
sum_j theta_j dlog l_j/(2pi). The consecutive center triangles give
angle sum2pi at each finite white circle, so the total is1 per finite
face; d/N tends to1. The retained P_s derivatives are O(S), and hence
vanish after division by N. This uses the uniform original finite
angle-force theorem, not independent local maximization.

The finite Hessian is real positive on the fixed gauge slice, and its
bounds are c_D N I<=H_N<=C_D N I on a fixed small real neighborhood.
Its fixed higher derivatives are O(N) on a uniform complex neighborhood:
preconditioning a D determinant gives a small perturbation of I, while
near-fold forced roots stay separated from the positive radius compact.
These are the same finite curvature and holomorphic bounds already proved.

The quantitative implicit-function argument now gives a real critical
radius l_N=l^geom exp z_N with z_N=o(1). Use the Hessian at zero as
preconditioner: the normalized gradient error tends to zero, and the
Newton remainder is O(|z|^2) with uniform constant, so contraction on
a ball of radius C|partial Phi_N(0)|/N gives existence and uniqueness
there. Strict convexity of log P_N on the gauge slice implies that no
other real critical radius exists. Strictness follows directly from
the positive determinant monomial support and the connected active
pair graph. Let H_N be the Hessian at this actual finite critical radius.

## 4. The exact coefficient integral and its nonzero asymptotic

The Cauchy coefficient formula, with one variable fixed by homogeneity,
is exactly

    A_N=P_N(l_N)/product_f l_N,f^d
        *(2pi)^(-n) integral_[−pi,pi]^n
          [P_N(l_N exp(i theta))/P_N(l_N)]
                         exp[-i d sum_f theta_f] dtheta. (7)

There is no unknown source-cycle coefficient in this integral for A_N.
Equation (4) makes the part outside any fixed small neighborhood
exponentially small relative to its prefactor. At the origin the exact
critical equation removes the linear term and the exponent equals

    -(1/2)theta^T H_N theta + O(N|theta|^3).

Uniform fourth and higher derivative bounds, rescaling by N^-1/2,
and symmetry of the Gaussian give

    A_N= P_N(l_N)/product_f l_N,f^d
          /[(2pi)^(n/2) sqrt(det H_N)] *[1+O(N^-1)].   (8)

The cubic term is odd, so its first Gaussian integral is zero; its
square and the quartic term cost O(N^-1). Gaussian domination from
(4) controls the remaining expansion and tails. The square root is
positive. Thus the coefficient is strictly positive for all sufficiently
large N in this near-fold window, and has the displayed global relative
asymptotic. This proves more than a constructed local contour statement.

## 5. Absolute value and remaining source tasks

The [absolute facet-coning computation](actual_original_boundary_stationary_character.md)
of the endpoint determinant action is

    2pi lim (1/N)log[P_N(l^geom)/product_f(l_f^geom)^d]
             =2 Vol(Q)=Vol(Y_D).                      (9)

For clarity its geometric input is explicit: each white cyclic-face
pyramid contributes the sum of Lambda(theta_j/2), and each shaded
contact triangle coned to the marked ideal vertex contributes the sum
of Lambda((pi-theta_j)/2). These actual coned facets tile Q. The source
Legendre potential is twice this sum, with additive constant fixed by
the exact single-positive-variable Cholesky product. This uses the
absolute marked action proof, not a volume chosen to normalize P_N.

The shift z_N=o(1) changes the normalized saddle value by o(1), and the
Hessian prefactor is subexponential. All exact circle scalars beta_ai
also have normalized log tending to zero when S=o(N). Therefore the
original fixed near-fold sector, ONCE the exact marked coefficient
identity is restored, has absolute rate Vol(Y_D)/(2pi). Its retained
half-twist scalar has modulus1 but may affect sums of different sectors.

Combining this coefficient theorem with a common-radius all-channel
upper bound gives a whole-source equality for the untwisted complete
source, since all its sectors are nonnegative in the specified common
normalization. The [complete untwisted source theorem](general_untwisted_augmented_source_volume.md)
performs this combination with the exact measure and scalar. Signed sums
and mixed external filling colors remain distinct tasks. No filled-knot volume equality is asserted.

Focused audit: [finite determinant contraction and original coefficients](../experiments/audit_actual_positive_face_coefficient_saddle.py), with [saved results](../experiments/actual_positive_face_coefficient_saddle_results.json). It checks 256 original matrix torus cases, 96 pair traces, and 16 literal tetrahedral-graph coefficients against exact finite Cauchy quadrature. Gaussian profile errors are diagnostics; the global graph-wide estimate is proved above.

The coefficient theorem does not settle the whole signed channel sum or external colors.