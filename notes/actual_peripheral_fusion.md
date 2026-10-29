# Actual peripheral action, fusion poles, and the normal boundary lattice

Research note, 26 October 2026. This reconstructs a peripheral-module
comparison directly from the literature ADO matrices. The two elementary
boundary curves act by specified difference operators, and the fusion
pole at the complete meridian has a nonzero square-zero Casimir residue.
The proof is uniform in the knot and in every level N>=2. It does not
identify the actual quantum period with a geometric gluing period or
prove its exponential norm.

The [positive ideal triangulation](ge_geometric_triangulation_audit.md)
supplies the marked geometric Bloch class. The
[crossing/action comparison](quantum_longitude_and_regulator_action.md)
already identifies the classical action of the actual state with that
class. The present calculation specifies additional *quantum boundary
data* that a period comparison must preserve, including its singular
specialization at M=1.

## 1. Fixed colors, parameter, and duality

Use exactly the conventions of [the ADO definition audit](kashaev_ado_pointing.md):

    q=exp(pi*i/N), D=q-q^(-1), x=q^alpha, M=-qx,
    [z]=(q^z-q^(-z))/D, T h(M)=h(qM).

On V_alpha, with 0<=j<N,

    E v_j=[j][alpha-j+1]v_(j-1), F v_j=v_(j+1),
    K v_j=xq^(-2j)v_j, H v_j=(alpha-2j)v_j,
    Delta E=E tensor K+1 tensor E,
    Delta F=F tensor 1+K^(-1) tensor F.

Let W be the two-dimensional highest-weight-one color, with basis w_0,w_1.
Its E,F entries are one and its K eigenvalues are q,q^(-1). The actual
pivot and twist on W are

    g_W=K_W^(1-N)=diag(-q,-q^(-1)),
    theta_W=q^(3/2-N)=-q^(3/2).                    (1.1)

A right partial trace over W uses g_W; a left partial trace over the
first factor W uses g_W^(-1). Interchanging these is an actual error:
it changes the fusion weights derived below.

For completeness, choose A=q^(1/2)=exp(pi*i/(2N)), with that root retained.
An invariant cup and cap on W are

    b(1)=w_0 tensor w_1-q^(-1)w_1 tensor w_0,
    d(w_0 tensor w_1)=-q, d(w_1 tensor w_0)=1,
    d(w_0 tensor w_0)=d(w_1 tensor w_1)=0.

Direct contraction gives both zigzags equal to identity and db=-q-q^(-1).
For e=bd, the actual fundamental crossing satisfies

    checkR_WW=A*I+A^(-1)*e, e^2=-(q+q^(-1))*e.    (1.2)

Indeed its only nontrivial two-by-two block, in order 01,10, is
q^(-1/2)[[0,1],[1,D]], while e has block [[-q,1],[1,-q^(-1)]].
Closing (1.2) gives the twist in (1.1). Thus a link colored by W
obeys the framed Kauffman bracket relations in this root convention.
This is checked from the matrices, not imported as a skein-comparison
theorem. It remains valid at N=2, when the loop value is zero.

## 2. An explicit fusion basis and its exact degeneracy

For generic alpha, define in W tensor V_alpha

    h_+=w_0 tensor v_0,
    h_-=[alpha]w_1 tensor v_0-x w_0 tensor v_1.

The coproduct kills both by E. Their H weights are alpha+1 and alpha-1.
Iteration of the displayed Delta F gives, with v_N=0,

    F^j h_+=q^(-j)w_0 tensor v_j+[j]w_1 tensor v_(j-1),
    F^j h_-=-xq^(-j)w_0 tensor v_(j+1)
                                      +[alpha-j]w_1 tensor v_j.  (2.1)

Both chains have length N: the next terms vanish by [N]=0 and v_N=0.
The commutator [E,F]=(K-K^(-1))/D now gives on a chain of highest
weight beta exactly E F^j h=[j][beta-j+1]F^(j-1)h. This can also be
verified directly in (2.1). The two chains are therefore the specified
colors V_(alpha+1) and V_(alpha-1).

Set

    delta=[alpha+1]=-(M-M^(-1))/D.                 (2.2)

In each intermediate weight space, in the basis w_0 v_r,w_1 v_(r-1),
the two columns of (2.1) are

    (q^(-r),[r])^t,
    (-xq^(1-r),[alpha-r+1])^t.

Their determinant is exactly delta. The top weight is one-dimensional;
the last coefficient is [alpha-N+1]=-delta. Hence the whole fusion
change of basis has determinant +/-delta^N, with the sign depending
only on the ordering of columns and weight spaces. Consequently

    W tensor V_alpha = V_(alpha+1) direct-sum V_(alpha-1)
                                                        if delta!=0. (2.3)

This is a direct basis proof, including composite and even levels.
It identifies the precise divisor where the splitting fails.

### Casimir projectors, with their poles retained

The Casimir in these conventions is

    C=FE+(qK+q^(-1)K^(-1))/D^2.

The generator relations show that it commutes with E,F,K,H. On a
highest-weight beta color it has value
c_beta=(q^(beta+1)+q^(-beta-1))/D^2. On W tensor V_alpha put

    c_-=(x+x^(-1))/D^2,
    c_+=(q^2*x+q^(-2)*x^(-1))/D^2,
    A_alpha=C_total-c_-*I.

Then c_+-c_-=delta, and (2.3) gives

    A_alpha^2=delta*A_alpha,
    P_+=A_alpha/delta, P_-=I-P_+.                 (2.4)

These are the actual projectors at delta!=0. Equation (2.4), after
clearing delta, is a Laurent identity, so its first equation also
holds on the divisor. No projector is evaluated separately there.

## 3. The two elementary boundary curves act on the actual period

Let F_N^L(M) be the reduced cut evaluation of a zero-framed knot
colored V_alpha, with any fixed framed W-colored link L in its
complement. In particular F_N^empty=F_N is the already specified knot
period. This construction also makes sense for linear combinations
of such links.

Write lambda for adding a W-colored, zero-framed preferred parallel
of the knot and mu for adding a positive W meridian. The exact formulas are

    F_N^(lambda L)(M)
       =-f(qM)/f(M)*F_N^L(qM)
        -f(q^(-1)M)/f(M)*F_N^L(q^(-1)M),
    F_N^(mu L)(M)=(M+M^(-1))*F_N^L(M),
    f(M)=M-M^(-1).                                (3.1)

These are identities of whole meromorphic germs; apparent poles in
the first line cancel when the actual finite evaluation is regular.

### Proof of the longitude weights

Coloring the knot by W tensor V_alpha is the framed parallel
construction by the following finite-product check. Write
R=D_Cartan*sum_(k=0)^(N-1)c_k E^k tensor F^k, with
c_k=q^(k(k-1)/2)*D^k/[k]!. The two summands of Delta E
q^2-commute. Their ordered q-binomial coefficients give

    c_(i+j)*binomial_(q^(-2))(i+j,i)=c_i*c_j,

which follows at once by writing
[k]!=q^(k(k-1)/2)*(q^(-2);q^(-2))_k/(1-q^(-2))^k.
Moving the Cartan factors past E and F then gives, term by term,

    (Delta tensor id)R=R_13 R_23,
    (id tensor Delta)R=R_13 R_12.

Only i+j<N contributes, because the remaining E^N or F^N is zero;
all factorial denominators used here are nonzero. The common Cartan
scalars agree by additivity of the highest weights. Tensor-product
cups, caps and pivots contract directly. This proves the required
local parallel replacement, retaining its framing. It retains
the preferred zero framing; its twist is the twist of the tensor
color, not a scalar twist chosen for one summand. Naturality with
the two explicit submodule inclusions in (2.3) gives its cut map

    Z_alpha^L=F_N^L(qM)P_++F_N^L(q^(-1)M)P_-.     (3.2)

For generic alpha each summand is simple; its cut endomorphism is
therefore its scalar by the same quantum-group intertwining argument
as for the original ADO cut. Possible exceptional colors are handled
after clearing the explicit denominators.

Taking the left pivotal partial trace over the first W gives the
weights. On the highest vector v_0, P_+ has coefficient one in
w_0 v_0 and x/delta in w_1 v_0, by the two-column inverse above.
Consequently, with g_W^(-1)=diag(-q^(-1),-q),

    ptr_W^left(P_+)=-q^(-1)-qx/delta
                   =-[alpha+2]/[alpha+1],
    ptr_W^left(P_-)=-[alpha]/[alpha+1].           (3.3)

The partial trace is an intertwiner of a generic simple V_alpha,
so this highest diagonal entry is its scalar on the whole module.
Substituting x=-M/q in (3.3) gives the first line of (3.1).
There is no assumed modified-trace additivity theorem in this proof.

The full modified dimension

    d_N(M)=eta_N*f(M)/(M^N-M^(-N)), eta_N=i^(N+3)

has exactly these ratios:

    d_N(q^(+/-1)M)/d_N(M)=-f(q^(+/-1)M)/f(M).    (3.4)

Here q^N=-1 changes the sign of the denominator; it is essential.
Thus for the full period N_N^L=d_N F_N^L, equations (3.1) become

    N_N^(lambda L)=(T+T^(-1))N_N^L,
    N_N^(mu L)=(M+M^(-1))N_N^L.                  (3.5)

### Proof of the marked meridian

On V_alpha tensor W use the actual unstripped double crossing
R_21 R and take the right trace over W. This is an intertwiner of
V_alpha, so evaluate its highest diagonal entry. The two W weights
contribute -q*x and -q^(-1)*x^(-1), respectively. Terms containing
E kill the highest vector or change its index and cannot contribute
to that diagonal entry. Hence the scalar is

    -(qx+q^(-1)x^(-1))=M+M^(-1).                 (3.6)

This fixes the meridian sign in the marking M=-qx. At the trivial
highest-weight color alpha=0, M=-q, it gives the actual fundamental
loop -q-q^(-1). At completeness M=1 it gives +2. The preferred
longitude and meridian signs must not be independently guessed
from a trace convention at q=1.

### A direct route from peripheral relations to actual annihilators

Let P be a finite linear combination of words in the two specified
boundary curves. Suppose P acting on the empty link is zero in the
Kauffman bracket skein module of the knot complement. Evaluate that
relation using (1.2), with its coefficient square roots retained.
Repeated use of (3.5), valid for every intermediate L, gives

    P(M+M^(-1),T+T^(-1)) N_N=0.                 (3.7)

The order in each word is preserved. Rational coefficient poles
allow only the usual finite exceptional set of levels. When the
word coefficients lie in C(q), (3.7) belongs to the literature
all-level ADO ideal. Coefficients in C(q^(1/2)) are kept over that
explicit extension; no descent to C(q) is silently asserted.

Thus peripheral skein relations yield actual knot-state annihilators
by an independent local proof. No equality of the peripheral ideal
with the full annihilator ideal, and no AJ specialization theorem,
is inferred. Such an equality or a survival argument would still
be needed to force its geometric classical component into a
primitive minimal operator.

## 4. A regular boundary lattice and the exact normal functional

Define w_N^L=f(M)F_N^L(M). Conjugating (3.1) gives regular Laurent
boundary operators on this specified normal state:

    lambda_w=-(T+T^(-1)), mu_w=M+M^(-1).         (4.1)

The denominator f(M) in the reduced-state action is therefore a
genuine change of boundary lattice with a divisor at M=1. It is
not a numerical multiplier. The original reduced period is still
recovered from that lattice and its normal derivative.

For the empty link, the [actual Weyl theorem](actual_weyl_descent.md)
makes F_N invariant under M->M^(-1), so w_N is odd. With u=Log M,

    w_N(1)=0, K_N=F_N(1)=(1/2)*d_u w_N|_(u=0).   (4.2)

This is the prescribed normal functional, not a choice of a new
solution. Put Y=M^2, U=Y^N and v_N=(Y-1)F_N=M*w_N. Then

    lambda_v=-q^(-1)T-qT^(-1)=kappa*T+kappa^(-1)T^(-1),
    kappa=-q^(-1), kappa^N=(-1)^(N-1),
    K_N=N*partial_(U-1)v_N|_(U=1,M=1).           (4.3)

These agree with the independently derived full ADO character and
[normal period](peripheral_normal_period.md). The full period has
the regular whole-germ value eta_N*K_N/N at M=1.

In particular, a peripheral word relation P as in (3.7) has a
regular normal representative

    B_w=P(M+M^(-1),-(T+T^(-1))),
    B_w*w_N=0, (B_w*f(M))*F_N=0.                 (4.4)

Thus the cleared reduced operator has its right boundary factor f(M)
without assuming positive volume growth. Passing from w_N to v_N
conjugates each T by q^(-1); the right factor becomes Y-1, with the
unit M explicitly retained. If the word has even meridian parity
and coefficients in C(q), its normal coefficients descend to C(q,Y) and this is exactly an
integral operator B_v*(Y-1) of the preceding normal-period theory.
It need not be the primitive minimal operator, and taking an
additional left factor can introduce extra root-fiber kernels.

Adding a fundamental meridian changes meridian parity. Thus mixed
W-colored links are kept on the marked M cover; one must not assume
their reduced evaluations are even in M just because the original
knot period is. In the even meridional subalgebra, mu^2-2 becomes
Y+Y^(-1). Formula (4.3) retains the half-root and the even-level
longitude sign rather than passing to an unsigned 2N-th norm.

## 5. The complete fusion fiber has a nonzero square-zero residue

At alpha=N-1 we have M=1 and delta=0. The matrix A_alpha in
(2.4) is regular. Write A_0 for its value there. Each of its
intermediate two-dimensional weight blocks is

    [[q^(-r)[r], -q^(-2r)],
     [[r]^2,     -q^(-r)[r]]],  1<=r<N.          (5.1)

Each block has rank one and square zero; [r]!=0 in this range.
The top and bottom weight blocks are zero. Consequently, uniformly,

    A_0^2=0, rank(A_0)=N-1,
    ptr_W^left(A_0)=I_(V_(N-1)).                 (5.2)

The last equality also follows from delta*ptr(P_+)=-[alpha+2]
in (3.3) and [N+1]=-1. It fixes the residue normalization exactly.
The colliding Casimir eigenblocks have N-1 Jordan blocks of size
two and two blocks of size one. In particular the generic split
fusion cannot be specialized as a direct sum of scalar-Casimir
blocks. No classification of projective modules is needed for
this conclusion, nor is indecomposability of the whole tensor
module asserted.

There is also an exact knot-dependent coefficient of this nilpotent
residue. The pointing and Weyl identities give F_N(q)=F_N(q^(-1))=1.
Apply (3.2) as a whole germ, rewriting it as

    Z_alpha=F_N(q^(-1)M)*I
               +(F_N(qM)-F_N(q^(-1)M))/delta * A_alpha.

The quotient has a removable singularity. Using (2.2) and the
reflection identity to differentiate, its complete value is

    Z_0=I+tau_N*A_0,
    tau_N=-(q-q^(-1))*(M partial_M F_N)(q).       (5.3)

Closing the fundamental color gives

    F_N^(lambda)(1)=-(q+q^(-1))+tau_N.           (5.4)

This is a specified nilpotent extension coefficient in the actual
state, computed without assuming a geometric contribution. It is
not K_N itself: (4.2) evaluates a normal derivative at M=1, while
(5.3) evaluates one at the adjacent ordinary color M=q. No equality
of their exponential rates is asserted. For the unknot F_N=1,
tau_N=0 even though the universal residue A_0 is nonzero. Thus
the local extension's existence does not force its excitation by
the selected knot period.

## 6. Where this meets the ideal triangulation theorem

The ideal triangulation provides the positive representative
beta_T with D(beta_T)=Vol and fixes the marked regulator norm.
The [actual classical action proof](quantum_longitude_and_regulator_action.md)
already matches that regulator without an imaginary additive
constant. The present calculation adds exact quantum peripheral
operators, a regular normal boundary lattice, and its nonsemisimple
specialization. These are specific data available for every knot.

A geometric gluing construction can now be asked to match these
operators and this normal functional, rather than merely a generic
central equation. It must also carry the actual vacuum/source
class. One concrete common object is the skein module of the knot
complement: (1.2) and (3.5) give its actual ADO evaluation as a
peripheral-module map. A proposed triangulation evaluation must
intertwine the same boundary action, preserve the retained normal
lattice, and send the same empty-link class to the selected period.
An isomorphism of unpointed modules alone would not prove those
evaluation maps agree. Equation (3.7) supplies one direction of peripheral-operator
compatibility, not equality of modules. The nonzero geometric
contribution of the selected normal period, and its norm

    (4/N)log|K_N| -> log||P_hyp||=2Vol/pi,

remain unproved. Existence of a positive triangulation supplies the
geometric representative; it does not identify or bound the
knot-dependent extension coefficient or the selected inverse pairing.

The subsequent [ramified Weyl-fibre construction](ramified_weyl_fibre.md)
now realizes the prescribed normal functional as an ordinary algebraic
evaluation on a descended fibre. The ramification retains the first
negative-sector coefficient; evaluating on the root orbit before
descent would discard it. An explicit equivariant frame change shows
that agreement on that ordinary root fibre is insufficient to fix
the period. The marked ramified fibre is therefore additional
comparison data; its regulator norm remains unproved.

The subsequent [threaded-character proof](ado_threaded_shadow.md)
extends the boundary calculation to arbitrary interior loops.
Explicit integral Weyl exact sequences replace singular root-level
projectors, and filtered auxiliary traces give the exact degree-N
phases and degree-2N abelian even character. This supplies an
interior central-data test for a geometric comparison and a
separating-observable criterion for an actual source extension;
it does not identify that extension or its regulator norm.

## 7. Coverage and independent verification

Representation theory and projective colors of this unrolled
quantum group are covered by Costantino--Geer--Patureau-Mirand,
[Some remarks on the unrolled quantum group of sl(2)](https://arxiv.org/abs/1406.0410).
The torus skein/noncommutative-torus relationship is covered by
Frohman--Gelca, [Skein Modules and the Noncommutative Torus](https://arxiv.org/abs/math/9806107).
The coverage check uses their abstracts and bibliographic scope;
none of their representation, skein, or comparison proofs is a
premise of the calculations above. No novelty is claimed for these
general constructions. The relevant concrete results here are the
normalization-matched formulas and their independently checked wall.
Derivative-valued knot invariants from the radical of the restricted
quantum-group center also have coverage in Murakami,
[From colored Jones invariants to logarithmic invariants](https://arxiv.org/abs/1406.1287).
Its abstract is used for coverage only. No identity between tau_N
and its named invariants, or any asymptotic theorem, is assumed.

[audit_actual_peripheral_fusion.py](../experiments/audit_actual_peripheral_fusion.py)
constructs the coproduct, Casimir, and actual R matrices independently
of the displayed projectors. It checks 45 fusion/wall cases, 30
heterogeneous Hopf cases, and 15 fundamental skein/duality cases at
15 levels including even and composite levels through 24. Six additional
tensor-color cases verify both parallel-crossing identities through
level 8, including their common Cartan scalars. A separate
16 cabled-knot checks construct the actual R and twist of the full
2N-dimensional tensor color, rather than defining its knot map by
fusion. They verify generic decomposition and the nilpotent
derivative coefficient at the ideal color, at levels 2,3,4,5 for
two signed two-strand braids. Results are in
[actual_peripheral_fusion_results.json](../experiments/actual_peripheral_fusion_results.json).
The finite diagnostics support the uniform proofs; they establish
no asymptotic statement.
