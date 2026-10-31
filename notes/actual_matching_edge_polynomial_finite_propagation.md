# Exact polynomial action away from a physical endpoint

30 October 2026. The original exceptional
Casimir polynomial acts by its scalar value on a genuine forward or
backward continuant in an explicit part of the physical block. The
identity is finite and generic, so it retains the actual q normals.
It does not say that the surrounding selected boundary state is such
a continuant or is supported in that part of the block.

## 1. Original matrix, continuants and endpoint residual

Fix N, d=N-1 and a physical low degree 0<=t<=d. Let J_t(q) be the
ACTUAL generic Casimir matrix of the
[physical generic-jet theorem](actual_q_hahn_physical_generic_jet_bound.md),
with diagonal D_u, upper entries A_u^+ and lower entries A_u^-.
These entries are the original coproduct entries before root
specialization; their generic upper and lower values are different.

For an arbitrary spectral parameter z define

    C_0(z)=1,
    C_u(z)=det(zI-J_[u](q))/product_(r=0)^(u-1) A_r^+,
                                      1<=u<=t,               (1)

where J_[u] is the first u rows and columns. Equivalently these
are the normalized forward recurrence with C_-1=0. They are
polynomials in z with rational generic-q coefficients. Every A_r^+
is a root unit when 0<=r<t, so (1) is holomorphic near the actual
root for every z, including z outside the physical spectrum.

The recurrence gives EXACTLY

    (J_t-zI)C(z)=r_t(z)e_t,
    r_t(z)=-det(zI-J_t)/product_(r=0)^(t-1) A_r^+.   (2)

The empty product has value one. Thus C(z) is an exact solution
on every row except the final row. For an eigenvalue, its residual
vanishes and this is the actual normalized eigenvector; at an
arbitrary z it is an endpoint-residual vector, not an invented
complex-color eigenvector of the finite matrix.

The backward vector C^back(z), normalized to value one at u=t,
is defined from the reversed ACTUAL generic matrix. It similarly
satisfies

    (J_t-zI)C^back(z)=r_0(z)e_0.                  (3)

No root-only conjugation symmetry is differentiated to obtain (3).

## 2. Finite propagation for the original exceptional polynomial

For any scalar polynomial p of degree at most a, put

    h_z(X)=(p(X)-p(z))/(X-z), deg h_z<=a-1.

Polynomial division and (2) give the exact vector identity

    p(J_t)C(z)-p(z)C(z)=r_t(z) h_z(J_t)e_t.        (4)

A tridiagonal matrix can move the support of a vector by at most
one row in one multiplication. Consequently h_z(J_t)e_t is
supported in rows u>=t-a+1. Therefore

    [p(J_t)C(z)]_u=p(z)C_u(z), 0<=u<=t-a.         (5)

The backward version is

    [p(J_t)C^back(z)]_u=p(z)C^back_u(z), a<=u<=t.  (6)

For a=0 both equalities hold everywhere. A negative upper limit
or an excessive lower limit denotes an empty window. These are
exact finite identities, independent of any limit or positivity.

In particular take the original degree-a polynomial p_a of
[the geometric target theorem](actual_matching_edge_geometric_target_polynomial.md).
For 0<=a<=floor(d/2), all of its displayed generic coefficients
are root regular. Its actual completed exceptional operator is
D_a^-1 p_a(J_t), with the same regular scalar D_a. Multiplying
(4)--(6) by D_a^-1 therefore proves the same finite identities for
that completed operator. They hold as generic-q germs before
specialization, hence after EVERY fixed generic derivative, with
all continuant and scalar derivatives retained. They neither
discard the nilpotent term nor replace a q derivative by a spectral
one. They also hold for a chosen holomorphic z(q).

The high physical block has total degree T>d. Use the already
proved GENERIC adapter t=2d-T and u'=u-(T-d). Its matrix is exactly
J_t(q), so (5),(6) apply to u'. No new high-degree convention or
root-only reflection is introduced.

The windows are generically sharp. If a>=1 and t>=a-1, the first
possibly affected forward row is u=t-a+1. In (4) only the leading
term of h_z can reach that row from e_t, giving

    [p(J_t)C-p(z)C]_(t-a+1)
       =r_t(z) lead(p) product_(r=t-a+1)^(t-1) A_r^+.
                                                               (7)

It is nonzero whenever the three displayed factors are nonzero.
The corresponding backward statement uses the lower entries.
Thus one cannot generally extend (5) through the remaining rows
by merely observing that z is a classical geometric trace.

## 3. Exact Green-column formulation

When z is outside the actual finite spectrum, (2) also gives

    (zI-J_t)^-1 e_t=-C(z)/r_t(z).                  (8)

Equations (4),(8) are an exact resolvent-column identity. It can
be used in a functional-calculus or boundary-state representation
without assigning an artificial noninteger color. For example,
any row functional ell supported on 0<=u<=t-a satisfies

    ell p_a(J_t)C(z)=p_a(z) ell C(z).               (9)

An actual representation of the surrounding state as such a vector,
or a controlled integral of such vectors, remains additional input.
An arbitrary row functional, dense mark or boundary tensor is not
declared to have the support in (9). All physical bends, pivotal
turns and the exposed mark remain the original ones.

## 4. Macroscopic windows and the remaining interface

In scaled low coordinates, a/N->xi, t/N->tau, the two safe regions
are respectively

    nu<=tau-xi,               nu>=xi.              (10)

At the folded row xi=1/2 and a strict physical degree tau<1, their
union leaves the central interval (tau-1/2,1/2). The existing
selected-factor localization proves a physical packet outside the
exceptional matching edge. It does not prove that the target
environment equals (1), or that its output belongs to (10).

Moreover (5),(6) are statements at ACTUAL integer physical rows.
Evaluating them at complex geometric magnetic coordinates would
require a proved continuation of these continuants and their
boundary identity. The ordinary packet alone, whose channel stays
real and discrete, does not supply that off-spectrum continuation.

The exact identity consequently identifies a concrete sufficient
interface for scalar evaluation, while preserving the unresolved
environment, continuation and source-cycle questions. It is not
a degree-O(N) functional-calculus approximation.

Focused audit: [actual generic Casimir propagation and sharp boundary defects](../experiments/audit_actual_matching_edge_polynomial_finite_propagation.py).

The finite-propagation result requires the stated environment and complex-row continuation assumptions.

An arbitrary boundary state is not identified with a continuant, and no whole-source asymptotic is inferred.