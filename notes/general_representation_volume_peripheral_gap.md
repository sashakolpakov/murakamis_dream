# A uniform representation-volume gap for fixed peripheral words

30 October 2026. This extends the supplied
[natural-map proof](general_representation_volume_kernel_strictness.md)
to a varying sequence of representations. No quantum source estimate
follows from this geometric statement alone.

Let X=Gamma\H^3 be the fixed oriented finite-volume complete hyperbolic
exterior, with its fixed marked complete PSL2 holonomy iota. For each n let
rho_n:Gamma->SL2(C), followed by its PSL2 action, and let Vol(rho_n) have
the same canonical peripheral-regulator normalization as in that note.
Then

    Vol(rho_n) -> Vol(X)

implies, after passing to a subsequence and conjugating by
orientation-preserving target isometries g_n, that

    g_n rho_n(gamma) g_n^-1 -> iota(gamma)             (1)

for every fixed gamma in Gamma, with one common conjugation and the actual
marking. A fixed final conjugation is absorbed into g_n. For absolute
volumes tending to Vol(X), pass to a constant-sign subsequence; the limit
is either iota or its orientation-reversed conjugate.

## Proof with nonuniform cusp data

Choose any s_n>2 tending to2. For rho_n choose its own cusp-adapted map
f_n and its natural map F_n=F_(s_n,f_n). The cusp estimates are used
separately at the fixed pair (s_n,rho_n), and prove exactly

    integral_X Jac F_n = Vol(rho_n).

No uniform cusp constants, uniform cusp truncation, or exchange of a cusp
limit with n is needed. The radial construction, however, gives uniform
INTERIOR estimates independent of f_n:

    |Jac F_n| <= (s_n/2)^3,
    AA^T <= H/3,     (I-H) DF_n=s_n A,
    ||D_x nu_n||_TV <= s_n,
    ||D_x^2 nu_n||_TV <= 3s_n^2/2.

The latter bounds differentiate only the domain radial kernel. Therefore

    integral_X [(s_n/2)^3-Jac F_n] ->0.             (2)

This is a nonnegative deficit. On any fixed compact lifted ball it tends
to zero in L1 as well: the projection has bounded finite multiplicity on
that ball. Choose points with Jacobians tending to1. The strict matrix
inequality forces H->I/3 and all singular values of DF_n to1 there.
Normalize their target images by orientation-preserving isometries g_n.

The same fixed-radius Hessian bootstrap as in the frozen note now gives
uniform C2 bounds near those points: positivity of I-H controls DF_n;
its first variation is bounded by C(1+||DF_n||), and the uniform second
measure derivative controls D2F_n. A C1 subsequential limit has Jacobian1
everywhere by (2). The strict matrix inequality forces its derivative
to be an orientation-preserving isometry. This convergence propagates
along finite chains of overlapping fixed-radius balls; target values
in the new ball stay bounded by the known overlap and derivative bound.
A diagonal exhaustion gives

    G_n=g_n F_n -> G_infinity locally in C1 on H^3,

where G_infinity is a global orientation-preserving hyperbolic isometry.
This construction does not assume compactness or irreducibility of the
representations and does not claim that the normalizing g_n are bounded.

It remains to use the equivariance, rather than only kernel invariance.
Set rho'_n=g_n rho_n g_n^-1. For every fixed gamma and x,

    rho'_n(gamma) G_n(x)=G_n(gamma x).              (3)

Choose four fixed source points whose G_infinity-images are noncoplanar.
Both sets of points in (3) converge. The isometries rho'_n(gamma) are
precompact: their values at one fixed target point are bounded, because
that point is o(1) from G_n(x), and the stabilizer of a point is compact.
Every limiting isometry sends the four G_infinity(x)-points to their
G_infinity(gamma x)-images. These determine an isometry uniquely, so

    rho'_n(gamma) -> G_infinity iota(gamma) G_infinity^-1.

Absorb G_infinity^-1 in the common g_n. This proves (1) simultaneously
for every fixed gamma; it also suffices to check a finite generating set.
The SL2 central signs need not stabilize, and are immaterial for trace
squared. No assertion about their lift is made.

## Uniform peripheral gap in the marked finite-dimensional problem

Fix finitely many actual peripheral words m_1,...,m_b and delta>0. Suppose
each iota(m_i) is parabolic or central, so tr^2 iota(m_i)=4. Then there is
g=g(X,{m_i},delta)>0 such that EVERY actual SL2 representation satisfying

    max_i |tr^2 rho(m_i)-4| >= delta

has

    |Vol(rho)| <= Vol(X)-g.                         (4)

Otherwise a sequence violating every positive gap would have absolute
volumes tending to Vol(X). Apply the proved compactness statement,
passing to a constant-sign subsequence. Trace squared is continuous and
conjugacy-invariant; its value at every selected word would tend to4 in
either orientation, contradicting the fixed delta. This proof supplies
a positive gap, not an effective numerical value.

For a physical peripheral eigenvalue m=e^(pi i chi) with real chi,

    |tr^2 rho(m_i)-4|=4 sin^2(pi chi).

Thus a selected real color parameter a fixed distance from the integer
aliases meets (4), IF it is the eigenvalue of an actual representation
whose volume controls the relevant source period. The latter implication
is NOT proved here: it requires the source action, its cycle, its upper
bound, and cancellation of all ordinary complementary terms to be
established separately. This statement is not a bound on F_N or L_h.

The fixed finite set is essential. One cannot take a supremum over ALL
peripheral words whose exponents are allowed to grow with n: powers of
a near-parabolic element may have trace far from ±2. The actual finite
set of marked crossing-circle meridians is within the theorem's scope.

## Validation and scope

Root full analytical review: PASS. The review checked the uniform
interior measure estimates despite varying cusp maps, the fixed-pair
volume identity, normalized isometry propagation, the use of exact
equivariance to recover the marked character, and the finite-fixed-word
quantifier. No numerical test substitutes for this analytic argument.
The source action/period upper bound and the complementary-color
cancellation remain separate requirements.

Independent full analytical review: PASS. The reviewer checked the
fixed-pair cusp normalization versus representation-independent interior
estimates, the propagated isometric limit, convergence of the conjugated
isometries from four noncoplanar points, and the fixed finite peripheral
quantifier. The absolute-volume orientation alternative and the source
limitations remain explicit. The theorem is frozen after these reviews.
