# The original exceptional operator as a continuant period

30 October 2026. The completed matching
block has an exact generic contour representation whose entries are
original forward and backward continuants. It retains the paired
double poles, moving-q normals, physical target order and finite
propagation. This separates an actual operator period from evaluation
of its scalar polynomial at a classical trace.

No geometric saddle contribution or sharp complementary contraction
estimate is asserted.

## 1. The original generic matrix and its actual spectrum

Put d=N-1 and use zeta=q exp(h), q=exp(pi i/N). In a physical
total-degree block 0<=t<=d, the ORIGINAL Casimir J_t(zeta) has
diagonal A_r, upper U_r and lower L_r, r=0,...,t:

    Q=zeta^2,
    A_r=zeta^-1 Q^(r-t)(1-Q^(N-r))(1-Q^r)
       +zeta^(-2d-1)Q^r(1-Q^(N-t+r))(1-Q^(t-r))
       +zeta^(2d+1)Q^-t+zeta^(-2d-1)Q^t,
    U_r=zeta^-N Q^(2r+1-t)(1-Q^(N-r-1))(1-Q^(t-r)),
    L_r=zeta^-N(1-Q^(N-t+r))(1-Q^(r+1)).             (1)

The offdiagonals are indexed 0<=r<t. These are the actual entries
proved in [the physical generic-jet theorem](actual_q_hahn_physical_generic_jet_bound.md).
In particular U and L are NOT identified away from the root.
All internal offdiagonals are nonzero at q. The actual generic
high-degree adapter identifies total degree 2d-t with this same
matrix, with the translated physical indices; no new norm or
complex conjugation is imposed.

Its generic characteristic polynomial is

    chi_t(zeta,z)=product_(m=0)^t (z-lambda_m(zeta)),
    lambda_m(zeta)=zeta^(2N-2m-1)+zeta^(-2N+2m+1).    (2)

This follows from the original normalized Clebsch columns for
m=0,...,t and their distinct generic eigenvalues. Their generic
source identity then extends (2) to q. The target label used in
the recoupling is g=d-m, so (2) is exactly the target Casimir
zeta^(2g+1)+zeta^(-2g-1), with its original moving-q derivative.

At q the only repeated eigenvalues are the pairs m and d-m when
both occur in this block. Their multiplicity is two. An odd-level
middle label is simple. An unreduced tridiagonal matrix has
one-dimensional eigenspaces: its first coordinate determines an
eigenvector recursively and cannot vanish. Therefore every paired
node here has a genuine Jordan block of size two, rather than
two independent eigenspaces.

## 2. Exact Green entries with both continuants retained

Define the prefix and suffix determinants

    P_r(z)=det(zI-J_t[0,...,r-1]), P_0=1,
    S_r(z)=det(zI-J_t[r,...,t]),   S_(t+1)=1.         (3)

All quantities retain their dependence on zeta. They satisfy the
original forward and backward determinant recurrences. For example

    P_(r+1)=(z-A_r)P_r-U_(r-1)L_(r-1)P_(r-1).

For z outside the actual spectrum, set R_t(zeta,z)=(zI-J_t)^-1.
The exact entries are

    (R_t)_(u,v)=
       (product_(r=u)^(v-1) U_r) P_u S_(v+1)/chi_t,  u<=v,
       (product_(r=v)^(u-1) L_r) P_v S_(u+1)/chi_t,  v<=u.      (4)

Empty products are one, so the two formulas agree on the diagonal.
Expanding a tridiagonal cofactor proves (4): the intervening chain
uses exactly the indicated upper or lower entries, and the two
remaining blocks supply the prefix and suffix. Equivalently direct
multiplication by zI-J_t verifies (4) using (3). No root-only
reflection is differentiated to obtain the backward factor.

## 3. The exact generic operator period and its bandwidth

Let p_a(zeta,z) and D_a(zeta) be the original polynomial and face
factor in [the generic target identity](actual_matching_edge_geometric_target_polynomial.md).
For the original folded range 0<=a<=floor(d/2), their coefficients
are holomorphic near q after the displayed common face zero is
canceled. The completed operator before the fixed physical bend
and pivotal turn is

    E_a(zeta)=D_a(zeta)^-1 p_a(zeta,Omega(zeta)).      (5)

Fix one contour Gamma enclosing ALL the root spectral nodes, for
example the positively oriented circle |z|=3. For zeta in a
sufficiently small neighborhood of q, the same contour encloses
every moving node and meets none. On each physical block,

    E_(a,t)(zeta)
      =D_a(zeta)^-1/(2pi i)
          integral_Gamma p_a(zeta,z) R_t(zeta,z) dz.              (6)

This follows either by Cauchy's formula on the generic eigenspaces,
then holomorphic continuation, or by expanding the resolvent at
infinity and taking the coefficient of z^-1. Thus (6) is valid
at the paired root WITHOUT deleting its double poles. Substitution
of (4) is an exact single spectral-period representation of every
native magnetic matrix entry.

The original polynomial has degree a. Since J_t is tridiagonal,

    (E_(a,t)(zeta))_(u,v)=0 if |u-v|>a.             (7)

This is a generic identity, so every fixed moving-q derivative
has the SAME bandwidth. Equivalently (6) has exact cancellation
outside this band. This assertion is about the actual target
physical coordinates BEFORE the recorded bend and pivotal turn;
it does not silently permute the original outside ports.

The full source substitution retains beta_N times the original
bend and turn, the row factor and half-twist, and the whole-source
marked normal, exactly as in the completed target theorem. Those
factors have not been absorbed into a chosen resolvent norm.

## 4. Genuine moving-q normals and the reduced pole budget

Differentiate in h with z FIXED. The exact identity is

    partial_h R_t=R_t (partial_h J_t) R_t.

Consequently the first normal of (6) is

    partial_h E_(a,t)
      =-(partial_h D_a)/D_a *E_(a,t)
       +D_a^-1/(2pi i) integral_Gamma
          [(partial_h p_a)R_t+p_a R_t(partial_h J_t)R_t] dz.     (8)

The partial derivative of p_a retains every generic-q coefficient.
The derivative of J_t is the derivative of (1), including the
distinct generic upper and lower entries. Formula (8) therefore
includes moving spectral nodes and moving generalized eigenspaces,
not merely a derivative of the scalar root value.

There is a useful exact reduction at a paired node lambda. Let Q(h)
be its analytic two-dimensional cluster projector, and let its two
actual analytic eigenbranches be lambda_1(h),lambda_2(h). At h=0
put

    Q=Q(0), M=(J_t(q)-lambda)Q, M^2=0.

Then the root resolvent on this cluster is

    R_cluster=Q/(z-lambda)+M/(z-lambda)^2.           (9)

The apparent fourth-order pole in R(partial_h J)R vanishes. Indeed
differentiate the exact cluster identity
(J-lambda_1)(J-lambda_2)Q(h)=0 and sandwich it by Q. It gives

    Q J' M+M J' Q=(lambda_1'+lambda_2')M,
    M J' M=0.                                     (10)

The second equation follows by multiplication by M. Thus the
same-cluster contribution to R J' R is exactly

    Q J' Q/(z-lambda)^2
       +(lambda_1'+lambda_2')M/(z-lambda)^3.         (11)

Terms between different spectral clusters remain in (8); they
must not be discarded. They contain the actual motion of the
cluster projectors. The source derivative of the paired gap is
lambda_j'-lambda_(d-j)'=-2N(q^(2j+1)-q^(-2j-1)), in convention (2).

More generally the r-th moving-q derivative of the resolvent has
pole order at most r+2 at a paired node and at most r+1 at a simple
node. To see this WITHOUT assuming diagonalizability at the root,
the exact analytic cluster resolvent is

    R_cluster(h,z)=
       [(z-lambda_1(h))Q(h)+(J(h)-lambda_2(h))Q(h)]
       /[(z-lambda_1(h))(z-lambda_2(h))].            (12)

Each h derivative increases the specialized denominator pole order
by at most one. All numerators and cluster projectors in (12) are
holomorphic. The corresponding scalar spectral derivatives needed
in an r-th operator normal consequently have order at most r+1,
with the actual q derivatives still retained. In particular the
first normal needs scalar spectral derivatives only through order
two, consistent with the prior Taylor-two calculation. These are
exact pole budgets, not size bounds on the cluster projectors.

## 5. Scalar continuation is distinct from contour contribution

The [source-polynomial root theorem](actual_matching_edge_racah_root_location.md)
gives a canonical Log p_a and a leading scalar action throughout
C minus [2,infinity). This is a statement about p_a, not about
R_t. The latter has the actual nodes of (2), all in [-2,2] at q,
including their double poles.

In particular a target below -2 is off the root spectrum. A
general target in (-2,2) lies in its spectral interval, among
nodes that become dense as N grows. Any deformation of (6) must
avoid those actual poles or account for their residues. The
scalar's zero-free continuation does not permit deleting them.

The exact numerator in (4) is where selected forward/backward
boundary estimates can enter. A proof of a geometric contribution
must still analyze that numerator together with chi_t, the fixed
spectral contour, and the actual surrounding coherent state. It
cannot replace p_a(Omega) by p_a(lambda_geometric) pointwise.
Equations (4),(6),(8),(12) expose that remaining operator problem
while preserving its original source and every required normal.

Audit: [actual Green entries, contour coefficients, normal poles and bandwidth](../experiments/audit_actual_matching_edge_continuant_operator_period.py).

Independent review: the root agent and cluster/source agent checked
the complete generic Green/contour proof, actual spectrum and Jordan
structure, moving-q normal, reduced pole budget and source bandwidth.
A fresh cluster replay passed 534 original Green three-jets, 1,902
contour operator entries with 5,706 jet coefficients, 868 bandwidth
zeros, and 29 genuine double clusters with their fourth-pole
cancellations. The reviewed scope includes no contour deformation
or scalar-to-operator asymptotic.
