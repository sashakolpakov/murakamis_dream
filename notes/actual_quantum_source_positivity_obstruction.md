# The original source is a tame nilpotent extension, not a positive trace

28 October 2026. There is a universal, source-specific obstruction to
obtaining geometric nonvanishing from an ordinary faithful positive
trace on the actual root quantum-group category. Its tensor-closing
map sends the identity to zero but a canonical nilpotent cup/cap to
the identity. This holds at every level and can be inserted into ANY
original knot cut without changing its value.

The source extension is polynomially tame in the actual flat metric.
Consequently this is not an obstruction to a later geometric norm
comparison or emergent positive integral. It rules out deriving that
comparison just from positivity/unitarity of the original categorical
trace, or from a positive semisimplification which discards its jets.

## 1. Keep the actual turns and boundary projector

Put N>=2, d=N-1, q=exp(pi*i/N), Q=q^2 and x=-q^(-1).
Use the original balanced factorial basis w_a. The actual pivot is

    g_a=x^(1-N)Q^(-a), sum_a g_a=0, |g_a|=1.          (1)

At this color the dual color x^(-1)Q^(-1) equals x. The exact actual
turns in [the bridge-source proof](quantum_bridge_cap_source.md) give
the cup column p and right-cap row l on V_N tensor V_N:

    p_(i,j)=N x^(-j) delta_(i+j,d),
    l_(i,j)=x^j g_i/N delta_(i+j,d).                  (2)

These retain the actual N, 1/N and pivot, rather than rescaling the
turns to obtain a desired state. Define Pi_N=p l. Then

    l p=sum_i g_i=0, Pi_N^2=0, rank Pi_N=1.          (3)

The original pivotal partial closing is

    Phi_N(T)=Tr_2[T(I tensor g)].                     (4)

By direct evaluation of (2),

    Phi_N(I_(N^2))=0,
    Phi_N(Pi_N)=I_N.                                (5)

For the second identity the only retained diagonal term has j=d-i;
its coefficient is g_i g_(d-i)=1, using x^2=Q^(-1). The actual snake
normalization is therefore fixed. No zero quantum dimension is divided
out and no full peripheral multiplier is replaced by its root value.

On the open cut retain its original e=psi phi, psi_i=1, phi_i=1/N.
Thus e is an orthogonal rank-one projector in this flat metric. Define
the actual two-head scalar functional

    Lambda_N(T)=Tr[e Phi_N(T)].

It has the exact values

    Lambda_N(I)=0, Lambda_N(Pi_N)=1.                 (6)

The positive open-cut functional Tr(e C) has not been replaced. The
failure of positivity is at the compulsory pivotal tensor-closing
map Phi_N, before that boundary functional is applied.

## 2. No positive realization of that closing map or full source

Suppose Phi_N were positive as a linear map between operator algebras
with ANY positive definite Hermitian metrics. Every positive A obeys
0<=A<=r I for some r. Positivity and Phi_N(I)=0 then force
0<=Phi_N(A)<=0. Positive matrices linearly span the whole algebra,
so Phi_N would be zero, contradicting Phi_N(Pi_N)=I.

This proves that no change of positive head metric makes the SAME
original pivotal closing a positive map. The argument does not assume
the flat metric, a particular knot or an asymptotic expansion.

Similarly no positive functional on a unital star algebra can have
both values in (6). Cauchy--Schwarz gives

    |tau(a)|^2<=tau(I) tau(a^*a)=0

if tau(I)=0. It would vanish on every a. Therefore the restriction
of Lambda_N to the unital actual intertwiner algebra cannot be a
positive state or trace for any involution respecting that algebra.
A global nonzero scalar phase does not repair a zero value on I.

One cannot evade this by first taking a positive spectral corner while
keeping its actual nilpotent source. The earlier direct Casimir proof
gives, on the actual tensor module,

    Pi_N=(-1)^N (q-q^(-1))^(-2)(Omega-c_0)e_0,
    c_0=q+q^(-1),                                    (7)

where e_0 is the actual double-node projector. This makes Pi_N a
CENTRAL nilpotent in the quantum-group intertwiner algebra. Every
positive star realization of a finite-dimensional algebra kills a
central nilpotent: its image commutes with its adjoint, hence is a
normal nilpotent and is zero. Equivalently Cauchy--Schwarz iterated
on the nilpotent selfadjoint Pi_N^* Pi_N proves its positive functional
vanishes. This applies even if the corner's identity has nonzero trace.

Equation (7) is the retained actual confluence, proved in
[the meridian Casimir-source theorem](meridian_casimir_source.md), not
an assumed property of an abstract quantum topology construction.
Thus a positive reduced spectral quotient cannot preserve (6). It
must retain a source/normal extension outside that ordinary quotient.

## 3. This obstruction is functorial for EVERY original knot

For ANY finite cut matrix C, not only a scalar intertwiner, linearity
of the partial closing and (5) give

    Phi_N[(C tensor I)Pi_N]=C,
    Lambda_N[(C tensor I)Pi_N]=Tr(e C).               (8)

In particular let C_K be the actual cut operator of a knot with its
specified crossings, pivots and framing convention. Its original
external line chi_N is retained, so its scalar is

    P_(K,N)=chi_N Tr(e C_K)
           =chi_N Lambda_N[(C_K tensor I)Pi_N].      (9)

This is a canonical cup/cap realization of the SAME period for all
knots and levels, not an arbitrary inserted coupon chosen to defeat
a positivity claim. The actual complete cut is scalar by the already
proved original quantum-group intertwining and irreducibility. If
C_K=f_(K,N)I, the state in (9) is f_(K,N)Pi_N, a nilpotent multiple.
Dropping the nilpotent source would erase its whole original value,
not just a dispensable local correction.

This explains why ordinary-color positive traces do not extend by
formal faithfulness to the Kashaev color. The exact ordinary-color
positive realization has zero quantum dimension at this endpoint;
its positive semisimplification kills precisely the object/source
which (5)-(9) retain. The separate regular-period theorem correctly
uses that positivity only below color N, not for the volume target.

## 4. Original braiding is also not positively unitarizable

The all-N actual Casimir interpolation retains the nonzero derivative
at c_0. If B=R_checked/kappa removes only the recorded common Cartan
scalar, its double-node block obeys

    e_0(B^2-I)=(-1)^(N+1)(N-1)(q-q^(-1))Pi_N !=0,    (10)

and the right side has square zero. Therefore B^2, hence B, has a
nontrivial Jordan block. A unitary matrix in a positive definite
metric is diagonalizable. No positive metric and no common phase
normalization makes the original checked crossing unitary.

This is an exact all-N consequence of the original R coefficient
and the actual cap jet. The derivative interpolation and its direct
matrix derivation are already in
[the Casimir braiding proof](casimir_braiding_and_recoupling_lattice.md)
and [the meridian source proof](meridian_casimir_source.md). We use
them with their scalar and parity, rather than assuming a literature
unitarity theorem.

## 5. The necessary extension is tame, but does not give a lower bound

In the actual flat complex root metric, (2) gives exactly

    ||p||_2=N^(3/2), ||l||_2=N^(-1/2), ||Pi_N||_op=N.

Also ||Phi_N||_(op->op)=N and ||Lambda_N||=N. The upper bounds follow
from summing N unitary-pivot diagonal blocks. Equality for Phi uses
T=I tensor g^(-1); equality for Lambda uses T=e tensor g^(-1).

Thus the universal source extension costs only polynomial factors,
not an unknown exponential normalization. For the assembled scalar
cut there is the exact positive norm identity

    |P_(K,N)|=|chi_N| ||(C_K tensor I)Pi_N||_op/N.    (11)

Equation (11) is useful normalization information but NOT a new
noncancellation mechanism: C_K already contains the original internal
pivotal sums. The right side is the same unknown scalar in a canonical
nilpotent line. A local geometric amplitude or ambient operator norm
does not supply a lower bound for it.

No source-specific broad positivity/nonvanishing theorem has been
obtained here. What is decided is that the actual cyclic/Hopf source
does not force it through ordinary positive trace, unitarity or a
positive reduced torsor. A successful positive geometric comparison
must explicitly transport the retained nilpotent/relative source and
prove its nonzero geometric image. Emergent positivity of a suitably
reduced global integral is not excluded by this result.

[Audit](../experiments/audit_actual_quantum_source_positivity.py): direct
actual cups/caps, pivot, Hopf invariance, original full-twist nilpotent,
and functorial reconstruction of actual whole-knot cut operators.
