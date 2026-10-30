# The matching-edge target gauge and its completed projector pairs

Follow-up: the [native-energy theorem](actual_matching_edge_native_projector_energy.md)
now gives the column measures and polynomial relative derivative costs
for these completed operators. Their explicit magnetic energy can be
exponential; its sharp use in the joint contraction remains open.

30 October 2026. The remaining scalar
target normalization in the exact four-port block is the actual
Casimir projector normalization times a regular face factor. Its
universal physical scale cancels the cup bend. Pairing the two
colliding target channels BEFORE specialization gives a regular
Hermite block with explicitly controlled scalar jets.

The native norms of the completed projectors and their derivatives
remain to be estimated. This theorem neither makes the root channels
orthogonal in a positive metric nor bounds a surrounding contraction.

## 1. Exact objects and the generic norm

Use the original conventions of the
[marked four-port block](actual_matching_edge_marked_four_port_block.md).
Put d=N-1, zeta=q exp(t), q=exp(pi i/N), Q=zeta^2, and

    0<=g<=d, E=2g, n=d-g,
    L=N zeta^(-d^2), pV=L p_d, ellV=pV^-1.

The canonical ordinary channel cup p_(2g) has first coefficient one.
Let W_g=W_dd^(2g), and retain its genuine categorical dual

    D(W_g)=p_(2g)^T W_g^T(ellV^T tensor ellV^T)P,
    N_g=W_g D(W_g),
    D(W_g)W_g=theta_g I_(2g+1).                      (1)

These are generic rational identities, including high g. The last
scalar follows from covariance and the generic highest-weight basis.
No root value of theta_g is inverted.

Let Omega be the ORIGINAL generic two-physical-head Casimir. Its
distinct generic eigenvalues are

    lambda_g=zeta^(2g+1)+zeta^(-2g-1), 0<=g<=d,
    Pi_g=product_(h!=g)(Omega-lambda_h I)/(lambda_g-lambda_h).
                                                               (2)

The Clebsch images are independent because their eigenvalues differ,
and sum_g(2g+1)=N^2. Thus they exhaust the generic tensor product.
Consequently N_g=theta_g Pi_g as an identity of ACTUAL operators.

The exact scalar is

    theta_g=(-1)^(d-g) zeta^(2d^2-g^2)/N^2
                       *[d+g+1]!/([d-g]![2g+1]!).   (3)

Here is a direct proof from the original matrix, without a quoted
theta or quantum-group norm formula. In physical degree d the
entry of the bent tensor S_(2g) at (d,0,0,d) is the previously
derived chi X. Undoing the physical bend gives

    (N_g)_(d,0)=zeta^[2g(g-d)] F_d^2 /
                            (L^2 F_(d-g)^2 F_(2g)),  (4)

where the two indices in (4) are the first physical magnetic index
in that degree-d block. In particular its row d means (d,0), and
its column zero means (0,d). The product of the original lower
offdiagonals of that tridiagonal block is

    product_(r=0)^(d-1) zeta^-N(1-Q^(r+1))^2
                                      =zeta^(-Nd) F_d^2.

The extreme adjugate entry of zI-Omega therefore gives

    (Pi_g)_(d,0)=zeta^(-Nd)F_d^2/chi'(lambda_g),
    chi(z)=product_(h=0)^d(z-lambda_h).              (5)

This adjugate identity is the unique lower path through a
tridiagonal matrix; it also follows by induction on its size.
The elementary factorization of eigenvalue differences yields

    chi'(lambda_g)=(zeta-zeta^-1)^(2d)(-1)^(d-g)
                              [d-g]![d+g+1]!/[2g+1]. (6)

Divide (4) by (5). Since
F_k=zeta^[k(k-1)/2](1-Q)^k[k]!, the residual exponent before
inserting L is -g^2. Substituting L=N zeta^-d^2 proves (3).

## 2. The actual target scalar becomes a face factor

The exact target product of the preceding block theorem is

    h_g=1/(b_(2g)J_(d-g)V_(d-g))
       =(-1)^d zeta^(g^2+d)
           [g]!^2[d-g]!^2[2g+1]![2d+1]! /
                                 ([d]!^2[d+g+1]!^2).

Define the already proved regular face factor and a universal scalar

    D_g=(-1)^g[N][g]!^2[d-g]!/[d+g+1]!,
    beta_N=zeta^(2d^2+d)/N^2
                          *[2d+1]!/([N][d]!^2).     (7)

Multiplication of the ACTUAL products gives exactly

    h_g theta_g=beta_N D_g.                          (8)

At the root D_g(q)=1 for every g, while

    beta_N(q)=(-1)^d q^(d+2)/N^2.                    (9)

All these root-zero cancellations are performed generically. Both
D_g and beta_N/beta_N(q) are holomorphic units on a uniform disk
of radius c/[N^2(1+log N)], and every fixed relative jet has
polynomial cost, by their explicit root-unit factorial products.

For clarity, let R be the ACTUAL last-to-first cyclic tensor turn

    (R Psi)(u,v,w,z)=(-1)^d zeta^(d-2u) Psi(v,w,z,u),
    B(K)=K(pV tensor pV)P.

Equations (1)--(8) give the exact typed target identity

    h_g T_(2g)=beta_N R B(D_g Pi_g).                 (10)

It holds at generic zeta through the entire range 0<=g<=d.
The physical reversal and odd-d turn remain in (10). At the root
the norm of B on Hilbert--Schmidt matrices is N^2, and the norm
of R is one. Equation (9) cancels that physical scale. Fixed
generic derivatives of the combined map beta_N R B have only
polynomial cost. This removes its scalar factorial cost; it says
nothing by itself about the operator norms of the Pi_g.

## 3. Pair before taking the normal

Fix the original folded row a, and put

    F_ag=G_ag D_g,
    G_ag=(-1)^d S_ag/[N],
    F_ag(q)=R_N(a,g)>0.

For a paired target choose 0<=g<g'=d-g and set

    Q_g=Pi_g+Pi_g',
    M_g=(Omega-lambda_g' I)Q_g,
    H_ag=(F_ag-F_ag')/(lambda_g-lambda_g').           (11)

Each of the three quantities in (11) is holomorphic at the root.
For Q_g, the quadratic cluster factor
(z-lambda_g)(z-lambda_g') is coprime there to the product of the
other cluster factors. Bezout gives its spectral projector as a
polynomial in Omega with coefficients regular at q. This is the
generic sum in (11), so it remains regular through the collision.
The polynomial identity product_h(Omega-lambda_h I)=0 holds
generically and hence at q; in particular

    Q_g(q)^2=Q_g(q),
    M_g(q)^2=0.                                     (12)

The odd simple target g=d/2 is kept separately and its Pi_g is
already regular. No positivity or Hermitian self-adjointness is
asserted for any of these projectors.

For H_ag, the numerator vanishes because the positive scalar
partners have the same root value and D_g(q)=D_g'(q)=1. The
denominator has a SIMPLE zero, with its actual TARGET convention

    lambda_g-lambda_g'
       =-(zeta^s-zeta^-s)(zeta^N-zeta^-N), s=d-2g,
    partial_t(lambda_g-lambda_g')(0)=2N Delta_g,
    Delta_g=q^(2g+1)-q^(-2g-1).                      (13)

This sign is opposite to the compiler's small-index minus large-index
gap: its channel index is m=d-g. It must not be inferred from a
root-only eigenvalue formula.

The exact regular paired identity is

    F_ag Pi_g+F_ag' Pi_g'
                       =F_ag' Q_g+H_ag M_g.          (14)

Thus at the root it is R_N(a,g)Q_g(q)+H_ag(q)M_g(q).
The nilpotent Hermite term is retained; equality of the two scalar
root values does not remove it.

There are uniform scalar jet estimates, for every fixed r,

    |[t^r]F_ag|<=C_r P_N^r R_N(a,g),
    |[t^r]H_ag|<=C_r P_N^(r+1) R_N(a,g),
    P_N=N^2(1+log N).                               (15)

Indeed the first bound is the existing scalar/face theorem. On a
slightly smaller common disk, (F_ag-F_ag')/t has size at most
C P_N R_N(a,g) by Cauchy's formula and its zero at the center.
The function (lambda_g-lambda_g')/t is a unit on that disk,
uniformly bounded below: its root magnitude is
4N sin(pi s/N)>=8, and its two elementary factors have controlled
relative changes there. Dividing and applying Cauchy again proves
the second bound. Both numerator and gap derivatives are included.

## 4. The resulting source interface and its remaining estimate

The full weighted recoupling inside the block is now

    sum_(g=0)^d G_ag h_g T_(2g)
       =beta_N R B[ sum_(g<d-g)(F_ag' Q_g+H_ag M_g)
                  + the odd simple term F_(a,d/2) Pi_(d/2) ].   (16)

The last term is included only when d is even. Its a is still the
original folded row label.

Every term on the right is regular BEFORE the whole-network first
normal is taken. Its first derivative uses only Q_g,M_g and their
FIRST generic-q derivatives. The scalar H_ag' already retains the
necessary second derivatives of the original F weights. Equation
(16) is equivalent to the prior Taylor-two Laurent extraction, with
the partner cancellation performed explicitly rather than left
between separate singular target terms.

There is also a complete cancellation of the original universal
scalar. Retain u_a=rho_a/rho_a(q) from the marked block theorem,
put v_N=beta_N/beta_N(q), and define the ACTUAL physical reshuffle

    A(t)=B(t)^-1 R(t) B(t).

The original measure identity and (9) give

    h0_a gamma_a^-1 rho_a(q) beta_N(q)=k_a N,
    h0_a K_a(t)=k_a N u_a(t)v_N(t) A(t) E_a(t),      (17)

where E_a denotes the regular completed sum in square brackets in
(16). Every factor in (17) is regular. At the root A is an isometry
for the Hilbert--Schmidt norm: B is N^2 times a unitary map, R is
unitary, and B^-1 is N^-2 times a unitary map. Its fixed jets have
polynomial cost. The equalities use the original physical cups,
not a new metric on the internal channels.

Let C(t) be the ordinary complementary closure and nu_N its original
trace-normal constant as in the preceding marked block theorem.
Then the exact signed weighted sector is

    h0_a omega_a^epsilon Z_Delta
       =k_a N omega_a^epsilon/nu_N
                 *[t^1]{u_a v_N C(t)(A(t)E_a(t))}.  (18)

The retained phase omega_a^epsilon remains unchanged. For a concrete
upper bound define, in the ORIGINAL physical basis,

    J_C^(1)=max_(r=0,1)||[t^r]C||,
    J_g^cl=max_(r=0,1)(||[t^r]Q_g||_HS+||[t^r]M_g||_HS),
    J_mid=max_(r=0,1)||[t^r]Pi_(d/2)||_HS
                                      (only when d is even).

Using (15),(17) and |nu_N|=N/sin(pi/N) gives

    |h0_a omega_a^epsilon Z_Delta|
       <=C k_a sin(pi/N) P_N^2 J_C^(1)
           *[sum_(g<d-g) R_N(a,g)J_g^cl
                         + R_N(a,d/2)J_mid].        (19)

The last summand is again omitted when d is odd. A weighted Cauchy
inequality can be applied to this positive scalar sum, with these
specified native cluster costs. Formula (19) improves the earlier
unpaired target bound: only regular completed cluster first jets
remain, and no target scalar factorial gauge is left unidentified.
It does not assert that the J_g^cl are polynomial or subexponential.

The [physical generic-jet theorem](actual_q_hahn_physical_generic_jet_bound.md)
controls all fixed q jets of original normalized physical columns
and their genuine divided pair. It is relevant to the next step,
but does not automatically bound the Q_g,M_g here. Their exact
column and dual measures, their operator norms, and their sewing
against the complementary network must still be controlled.
In particular a root spectral derivative cannot be substituted
for Q_g' or M_g'. The latter contain the variation of the actual
Casimir matrix and its generic spectral data.

The progress in (16) is an exact regular target block with no
unidentified exponential scalar normalization, uniformly at both
parities. A sharp bound for its native completed projector costs
and the nonzero global selected contribution remain separate tasks.

Audit: [actual target norm and completed projector identity](../experiments/audit_actual_matching_edge_completed_projector_block.py).
The focused audit passed 54 original categorical norms, 58,014 full
projector operator entries, 54 actual clocked target identities, and
30 original completed rows. Exact root computations checked eleven
cluster second jets, their first-order idempotent and moving-gap
nilpotent identities, 33 weighted Hermite second jets, and fourteen
complete original-measure cancellations.

An independent analytical review and fresh audit replay passed the
extreme-entry norm derivation, all target/root signs and valuations,
the categorical bend and cyclic turn, the phase-free k_a N factor,
and the regular paired identity with its retained nilpotent term and
second scalar derivatives. The replay reproduced all reported counts.
It did not infer a bound for the native completed projector norms.

A second independent full analytical review also passed the genuine
theta derivation, beta and k_a N cancellations, target-gap orientation,
regular Hermite pairing, scalar-versus-cluster derivative orders, and
the P_N^2 estimate. The completed projector norms and coherent global
energy remain outside this result.
