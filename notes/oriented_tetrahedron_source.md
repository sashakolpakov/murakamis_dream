# Shared source caps, triangle orderings and the remaining tetrahedral defect

Research note, 26 October 2026. This gives exact shared-edge cap
transport, tetrahedron reversal and coherent cyclic face orderings
for the existing pointed recoupling tensors. It also gives an explicit
counterexample to extending those results to all vertex orderings of
the bare tetrahedron tensor. Thus the ideal-triangulation comparison
still requires a source-compatible tensor symmetrization.

The actual endpoint caps and their finite-factorial normalization are
those proved in [relative pivotal duality](relative_pivotal_duality.md).
No different knot invariant or regulator realization is defined here.
The volume conjecture remains unproved.

## 1. One marked cap on each edge

Fix N>=2, q=exp(pi*i/N), Q=q^2. On a nondegenerate flag chart
choose distinct p_i=A_i^N, with A_i nonzero. Give an oriented
edge the existing affine character and endpoint module

    g_ij=(1,p_i-p_j), E_ij=E_(g_ij;A_j,A_i).

Thus g_ij g_jk=g_ik. Choose a marked K-root x_ij with
x_ij^N=1 and put

    x_ji=Q^(-1)x_ij^(-1).                         (1.1)

Let J_ij be the actual source-normalized endpoint cap from
the preceding note. It pairs E_ij with E_ji. In particular

    J_ij^(-t)J_ji=X_ij^(N-1).                    (1.2)

The cap on the total edge ik is its already assigned J_ik.
It is not chosen independently each time that edge occurs
in a triangle. For example the dual of a product mark x is
Q^(-1)x^(-1), whereas the product of two dual marks is
Q^(-2)x^(-1). These are different marked cyclic cuts.

For general multiplicative central X-characters, define

    omega_ijk=x_ij x_jk/x_ik, omega_ijk^N=1.

Direct cancellation gives

    omega_ijk omega_ikl=omega_ijl omega_jkl,
    omega_kji=Q^(-1)omega_ijk^(-1).               (1.3)

Thus the root discrepancy is coherent triangle data, with
a specified reversal law. It is not set to one independently
on each face. No division by two or three modulo N is used.

## 2. Root changes are explicit norm-one transports with a source wall

Write the finite cap scalar of the preceding note as

    c(x;a,b)=-1/(N xQ)
                product_(s=1)^(N-2)(b-a x^(-1)Q^s).

At fixed endpoints and central character,

    c(Qx;a,b)/c(x;a,b)
       =Q^(-1)(b-a/x)/(b-aQ^(-2)/x).              (2.1)

This follows by canceling the two finite products. The product
of (2.1) over the full N-orbit is one. The cap scalar itself
is an explicit Hilbert-90 primitive for this transport. These
ratios are functions; for N>=3 they are not generally phases
or constants. All zero and pole factors remain.

At the actual source choose a=x_0, b near 1 and let the
mark be Q^j x_0. In the normal coordinate b-1,

    ord c(Q^j x_0;x_0,b)
       =0 for j=0,N-1, and 1 for 1<=j<=N-2.       (2.2)

Indeed the single vanishing factor occurs exactly at s=j
in the product, and its first coefficient is nonzero. At
N=2 both charts have order zero. Thus moving the cut can
require a first normal coefficient even though its generic
cyclic norm is one. Its finite cyclic lattice and the dual
linking pairing retain that coefficient. A value at b=1
without its source lattice does not specify this transport.

There is an exact cancellation law for the face metrics.
If a change of marks rescales edge caps by J'_ij=u_ij J_ij,
then the induced face pairing obeys

    M'_ijk=(u_ij u_jk/u_ik)M_ijk.                 (2.3)

This follows immediately from the factorization defining M.
The two products of these face factors around a tetrahedron
are equal by cancellation. Consistent shared edge choices
therefore retain their full factors without an independent
tetrahedron normalization. The actual selected boundary
vectors and covectors must be transported as well.

## 3. Exact tetrahedron reversal

Use the pointed factorization

    C_ijk:E_ik tensor V_ijk -> E_ij tensor E_jk,

and the triangle metrics defined by

    C_ijk^t(J_ij tensor J_jk)P C_kji
                        =J_ik tensor M_ijk.      (3.1)

Here P is the literal flip. The total cap in (3.1) is the
shared edge cap. For four flags let

    R_0123:V_023 tensor V_012 -> V_013 tensor V_123

be the existing pointed Racah map. Then exactly

    (M_023 tensor M_012)R_3210
                    =R_0123^t(M_013 tensor M_123). (3.2)

For a proof let I_L,I_R be the two three-edge fusion tree
evaluations, with I_L=I_R(I tensor R_0123). Reverse their
leaf order and use the inverse affine characters. Applying
(3.1) twice factors the paired leaf contraction as
J_03 tensor M_023 tensor M_012 for one tree and
J_03 tensor M_013 tensor M_123 for the other. Substitution
of the tree relation and cancellation of J_03 gives (3.2).
This fixes the whole scalar, without determinant rigidity.

Equation (1.2) and the group-like pivot also give

    M_kji=M_ijk^t.                               (3.3)

Indeed the double-dual operator on the two leaves is their
tensor pivot, which is the pivot of the total edge. Removing
that same total cap leaves the identity on the relative
factor. Thus face reversal is paired exactly.

Choosing a local product mark for a total cap changes (3.2).
If r_ijk=c(x_ij x_jk;A_k,A_i)/c(x_ik;A_k,A_i), its defect is

    r_023 r_012/(r_013 r_123).                    (3.4)

The audit finds nontrivial examples at every tested N>=3.
These factors are retained as their full functions; (3.4)
is not a new permitted normalization of the knot period.

## 4. The cyclic face map from the actual invariant tensor

The relative triangle has operators

    D=X_1+Y_1Y_2^(-1), Z=-Y_1Y_2^(-1)X_2,
    DZ=QZD, D^N=lambda, Z^N=mu, lambda+mu=1.

Its endpoint parameters are u=A_j/A_k, v=A_i/A_k. Turn
the total leg of C_ijk using its assigned cap:

    T_ijk=(C_ijk tensor I)coev_ik.

Here the relative factor is retained as the argument; in
indices T_(abc,l)=sum_s C_(ab,sl)(J_ik^(-1))_(cs).
It identifies V_ijk with the invariant subspace of
E_ij tensor E_jk tensor E_ki. This space has dimension N:
rigid duality identifies it with the N-dimensional fusion
multiplicity space, and C_ijk is the explicit isomorphism.

On invariants cyclic rotation is

    rot=P_231(g_ij^(-1) tensor I tensor I),
    g_ij=X_ij^(N-1).

The antipode and pivot identities make this an invariant
tensor again. Three rotations give the inverse total pivot,
which acts as the identity on invariants. Thus there is a
unique invertible matrix L_f for f=(i,j,k), r f=(j,k,i),
such that

    T_(r f)L_f=rot T_f,
    L_(r^2 f)L_(r f)L_f=I.                        (4.1)

This is a finite construction with the scalar fixed by
the displayed actual tensors. It does not reset a unit.

The corresponding relative algebra map is

    h(D)=-D^(-1)Z, h(Z)=Q D^(-1), h^3=1,
    D_(r f)L_f=L_f h(D_f),
    Z_(r f)L_f=L_f h(Z_f).                       (4.2)

One can derive (4.2) directly on invariants. The total Y
equation gives Y_2Y_3^(-1)=-D^(-1)X_1X_2 there, while
D X_2=X_1X_2-Z. These give the first formula. The total
X equation and the Q commutation give the second formula.
Both phases in (4.2) are consequently determined.

## 5. The raw cyclic map has a matrix-valued pairing defect

Let bar f=(k,j,i), and f'=(i,k,j), so r f'=bar f and
bar(r f)=f'. The exact defect of the raw map is

    L_f^t M_(r f)L_(f')^(-1)
       =M_f G_(bar f),
    G_(bar f)=D_(bar f)^(1-N)
              =lambda_(bar f)^(-1)D_(bar f).      (5.1)

This is not a scalar for N>=2. The source cap alone does
not make the raw invariant rotation a face pairing symmetry.

Here is a uniform calibration of (5.1). The reversal
anti-map on the relative algebra is

    a(D)=-Z^(-1)D, a(Z)=QZ^(-1).

Substitution of a and h shows that the defect G commutes
with D_(bar f) and Q-commutes with Z_(bar f). Since this
pair generates the full matrix algebra, G=c D_(bar f).
To determine c, edge-cap scalar gauges may be removed by
(2.3); they cancel from G. Use the raw endpoint trace caps.
Put alpha_f=A_k^(N-1)/(p_j-p_k). Their relative unit
functional is

    (M_f e_0)(F)=alpha_f tau_D[D F/(v-uD)],        (5.2)

where tau_D is normalized multiplication trace in
k[D]/(D^N-lambda). Its defining shift recurrence follows
from a(Z)+u_(bar f)a(D)-v_(bar f), and its scalar follows
by pairing the two endpoint units in (3.1). Finite trace
cancellation gives

    (M_f)_(0,1)=alpha_f u^(N-2)lambda/mu,
    (M_f)_(N-1,0)=alpha_f lambda v^(N-1)/mu,
    (M_f)_(N-1,N-1)=0.                            (5.3)

For example tau[D/(v-uD)]=u^(N-1)lambda/mu;
the adjacent shifted denominator gives the first identity.
The last identity reduces to tau[D^(N-1)]=0.

The pointed factorial formula for C gives

    L_f e_0=ell_f e_(N-1), ell_f=lambda/mu,
    L_f^(-1)e_0=(v e_(N-1)-u lambda e_0)/(ell_f mu).
                                                        (5.4)
For the scalar in (5.4), with raw caps the invariant unit
tensor is

    (A_k-A_i X_3)sum_(s=0)^(N-1)(X_1X_2X_3)^s.

Apply the pointed finite-product formula to the rotated
relative monomial of degree N-1. The identity
product_(s=1)^(N-1)(b-aQ^s t)=(b^N-a^N)/(b-at)
at t^N=1 gives ell_f=lambda/mu. The inverse in (5.4)
then follows by (4.2) and Z^N=mu.

Now evaluate the (0,0) entry of (5.1), use (5.3)--(5.4)
on f,r f,f', and divide by (M_f)_(0,1). It gives

    c=(alpha_(r f)/alpha_f) mu/v^(N-1)
      =mu(p_j-p_k)/(p_k-p_i)
      =-mu/lambda=lambda_(bar f)^(-1).

This proves (5.1) with its full scalar at every N. The
audit checks the intermediate trace and unit formulas,
as well as the complete matrix identity.

## 6. Corrected face orderings preserve the actual pairing

Choose once a phase tau_N with tau_N^3=Q. This is an
ordinary algebraic phase choice, including when 3 divides N;
no inverse of three modulo N is required. Define

    U_f=tau_N lambda_f L_f D_f^(-1)
       =tau_N L_f D_f^(N-1).                      (6.1)

Thus the correction is exactly the relative face pivot,
with its recorded cubic phase. The second expression is
polynomial; invertibility at a degenerate central point
still requires the retained lattice and source.

These maps have exact cyclic and dual-pairing coherence:

    U_(r^2 f)U_(r f)U_f=I,
    U_f^t M_(r f)U_(f')^(-1)=M_f.                 (6.2)

For the cyclic identity, pulling the inverse D factors
through (4.2) gives

    (L D^(-1))_(r^2 f)(L D^(-1))_(r f)(L D^(-1))_f
              =h^2(D)^(-1)h(D)^(-1)D^(-1)
              =-Q^(-1)I.

The three central lambda values are lambda,-mu/lambda,1/mu;
their product is -1. Combining this with tau_N^3=Q proves
the first equation of (6.2). For the second, move D factors
through the reversal pairing using a. Equation (5.1) then
gives the scalar mu/lambda for L D^(-1). The lambda factors
in (6.1) cancel it because lambda_(f')=mu_f. The common
phase cancels as well.

The lifted quantum cyclic algebra map is now

    h_correct(D)=-Q D^(-1)Z,
    h_correct(Z)=Q D^(-1).                        (6.3)

It has order three and obeys the strict dihedral relation
with the reversal anti-map a. Equations (3.3) and (6.2)
therefore give coherent oriented triangular order changes
with the actual dual pairing. The selected vectors and
covectors are transported by these full matrices. Interior
adapters cancel in a specified finite contraction.

The inverse D and lambda in (6.1) are operator and central
data, not discarded numerical multipliers. At a wall,
whole transport is interpreted on its actual lattice and
dual source, as in the preceding note. This face result
does not assert all tetrahedron vertex symmetries.

## 7. The bare tetrahedron still fails the full vertex-order test

This is a separate, explicitly failed proposed bridge.
Use the raw R above as the positive tetrahedron map. Regard
its source duals as reversed face modules using M^(-1),
and place its four tensor legs in boundary-face order

    (123),(320),(013),(210).

For a negative tetrahedron use R^(-1) with the opposite
face orientations. For another ordered vertex list identify
its oriented faces by the corrected U maps in (6.1) and
permute its four legs back to the same boundary-face order.
This completely specifies the tensor comparison being tested.

It is false that the resulting tensors are always scalar
multiples. An even permutation already gives a counterexample:

    N=2, A=(2,3,4,5), vertex order (1,2,0,3).

There is a short exact reduction certificate. Work modulo
241 with primitive generator 7, q=177, Q=-1 and tau_N=16.
Then q^2=-1 and tau_N^3=-1. With the face tensor flattened
in the displayed boundary order, its first two coefficients
and those of the reordered tensor are

    original:  (83,239),
    reordered: (141,0).

Their proportionality minor is 0*83-239*141=41 mod 241,
which is nonzero. All denominators and required matrix
minors in the construction are nonzero at this point.
This is also a characteristic-zero obstruction to the
proposed rational identity: 241 splits the cyclotomic
coefficient field, and a zero rational identity could not
have this nonzero good reduction.

At the odd level N=3 the same even permutation has a
regular certificate modulo 397: the two coefficient pairs
are (344,139) and (10,262), with minor 207. Thus the
ordering issue also occurs on the odd-level recoupling
system covered by the matrix-dilogarithm framework.

Consistent edge-cap scalar gauges cannot remove this
counterexample. By (2.3) they rescale each face pairing,
and the T-based cyclic maps rescale by the ratio of their
total-edge cap scalars. Thus each compared four-tensor is
only rescaled. Nonproportionality is unchanged. A scalar
tetrahedron factor cannot fix it either.

This refutes this bare-tensor prescription with these face
adapters. It does not refute a literature charged matrix
dilogarithm, a different specified tetrahedral decoration,
or the actual knot invariant. The audit finds only the
identity and full reversal scalar equivalent among the
24 orders in its N=2,3,4 configurations. A source-compatible
tensor symmetrization or a comparison retaining additional
operator trace data is still required before global gluing
to an arbitrarily ordered positive ideal triangulation.

The later [root-charge diagnostic](braided_source_groupoid.md#1-fixed-face-adapters-are-not-repaired-just-by-root-charges)
checks a stronger repair proposal: keep these face adapters
and vary both literal standard-kernel root charges. At a
regular N=3 point all 81 reference/reordered charge pairs
still have nonzero proportionality minors. Thus that repair
does not supply the missing tetrahedron assignment. This is
not a test of a different published adapter prescription.
The actual source braiding and its retained spectral jets
are constructed separately in the braided source groupoid.

## 8. Coverage, verification and the remaining volume comparison

The abstract of
[Baseilhac--Benedetti, math/0306283](https://arxiv.org/abs/math/0306283)
already distinguishes a basic ordered matrix dilogarithm
from its decorated symmetrization. It supplies coverage
of this problem, not a proof premise or an identification
with the actual source used here. No novelty is claimed
for charged tetrahedral symmetry or cyclic 6j-symbols.

[The exact audit](../experiments/audit_oriented_tetrahedron_source.py)
checks N=2,3,4,5,6,8,9,10,12. Shared-cap reversal, the
raw nonscalar cyclic defect, its uniform trace calibration,
the corrected cyclic and metric identities, all 24 face
cap gauge and tetrahedral charge identities, and the root
mark norm/source formulas pass. The separate full vertex
test fails with the explicit certificate above, as recorded
in [the results](../experiments/oriented_tetrahedron_source_results.json).

    python3 experiments/audit_oriented_tetrahedron_source.py

The positive triangulation theorem supplies a geometric
marked Bloch representative. The constructions here provide
further actual source and orientation data for a comparison,
and the failed test identifies an additional operator-level
requirement. They do not identify the global selected period,
its geometric A-component, or its regulator norm across levels.

The subsequent [standard matrix comparison](standard_matrix_dilog_source_comparison.md)
now makes the candidate charged replacement concrete: the actual
pointed fusion map is written in the literature odd-level basic
kernel with four face gauges, its input permutation and selected
unit scalar. Root-charge changes become explicit Weyl leg operators
and their Heisenberg phase, while the integer-charge prefactor
remains a full function. The normal source chart has a regular
standard kernel and the same integer carry poles. This identifies
the local tensor and its actual source; it does not by itself prove
that the globally prescribed charged face pairings are the induced
ones, or repair the failed uncolored vertex-order prescription.

The subsequent [shared face proof](shared_standard_face_gluing.md)
now gives one frame per ordered triangle on the common flag chart.
In it these actual pairings and corrected cyclic maps are explicit
Gaussian matrices times their retained source-normalized scalars.
Every ordered tetrahedron has a standard-kernel formula with an
explicit clock/shift insertion. This is a compatible local frame
description; it does not assert proportionality of the different
uncolored vertex-order tensors or identify the global selected
geometric period.
