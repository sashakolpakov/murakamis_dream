# The missing Ward edge gives the full peripheral norm adapter

Research calculation, 27 October 2026. The literal nilpotent raising
matrix has a canonical cyclic completion with one additional edge.
Its determinant character is exactly the regular-meridian character
at the Frobenius peripheral parameter. The full modified-dimension
factor is the ratio of the missing edge to this cyclic norm defect.

This supplies a norm-character comparison and a regular degenerating
finite algebra. It does not identify the full quantum Ward flow with
the internal geometric centralizer, or prove the selected volume norm.

## 1. The actual raising matrix and its single missing edge

Fix N>=2, Q primitive of order N, q^2=Q, x=-M/q. In the balanced
actual basis, the regular scaled raising matrix Ecal=(q-q^(-1))^2 E
has upper edges

    Ecal_(a,a+1)=epsilon_a=M Q^(-a-1)-M^(-1),
    0<=a<N-1.                                      (1)

Its last cyclic edge is absent in the actual highest-weight module.
Extending the same expression to a=N-1 gives

    epsilon_(N-1)=M-M^(-1)=kappa.                  (2)

Define Ecyc by adding precisely the matrix entry

    Ecyc=Ecal+kappa E_(N-1,0).                    (3)

This is a specified rank-one completion, not an assertion that the
completed matrix defines the original quantum-group representation.
The actual cut and all actual Ward equations still use Ecal unless
their corresponding boundary term from (3) is explicitly retained.

## 2. The exact cyclic norm

Put kappa_N=M^N-M^(-N). The primitive-root product gives

    product_(a=0)^(N-1) epsilon_a
       =(-1)^(N+1)kappa_N=:delta_N.               (4)

Indeed factor M^(-1) from each edge and use
product_(j=1)^N(1-M^2 Q^(-j))=1-M^(2N).
Every path of length N around the cyclic matrix uses every edge
once. Its characteristic polynomial and determinant are therefore

    Ecyc^N=delta_N I,
    det(lambda I-Ecyc)=lambda^N-delta_N,
    det(I+t Ecyc)=1+kappa_N t^N.                 (5)

The determinant formula also follows directly: only the diagonal
permutation and the complete N-cycle survive in its expansion.
All signs in (4)--(5) are retained, including even N.

Over k(M), the algebra

    A_N=k(M)[e]/(e^N-delta_N)                    (6)

has the displayed matrix as its regular multiplication operator
after a diagonal basis change, whenever all edges are units.
Thus (5) is also the exact algebra norm

    Norm_(A_N/k(M))(1+t e)=1+kappa_N t^N.        (7)

Generically delta_N!=0 and this is an etale finite algebra. In a
neighborhood of M=1 the first N-1 edges in (1) are units. The same
diagonal basis change is regular there, while the missing edge
vanishes: use v_(N-1), Ecyc v_(N-1), ..., Ecyc^(N-1)v_(N-1)
as the cyclic basis. Only the first N-1 edge factors enter its
invertible diagonal/reversal change; no kappa inverse occurs.
At M=1, Ecyc=Ecal is a single regular nilpotent Jordan
block and A_N becomes k[e]/(e^N). The meridian lattice, rather than
only the generic norm-one torus, retains this special source fiber.

## 3. The peripheral multiplier is the defect ratio

Define the full regular-meridian adapter

    u_N(M)=kappa_N/kappa
          =M^(1-N)(1+M^2+...+M^(2N-2)).          (8)

This is a Laurent polynomial, with u_N(1)=N. Equations (2) and (4)
give the whole-germ ratio

    kappa/kappa_N=1/u_N(M).                      (9)

The actual modified dimension in the retained convention is exactly

    d_N(M)=i^(N+3)/u_N(M).                       (10)

Thus the finite raising-matrix completion accounts for the entire
peripheral adapter, including its meridian normal germ and divisors.
One must cancel the common kappa factor before evaluating at M=1;
the result there is i^(N+3)/N. Replacing kappa and kappa_N separately
by zero would discard this source value.

The normal determinant coefficient is also fixed:

    det(I+t Ecyc)=1+N kappa t^N+O(kappa^2)        (11)

near M=1. It is a first eigenvalue-gap normal with multiplier N,
not the N-squared trace normal described in
[the Newton resolution](newton_resolution_and_regulator_cut.md).

## 4. The norm character agrees with the geometric regular centralizer

The existing marked regular centralizer is

    C_M(b)=I+b J_M, J_M^2=kappa J_M,
    det C_M(b)=1+kappa b.                        (12)

At the Frobenius peripheral value M^N it has determinant
1+kappa_N b. Equation (7) is precisely this character after b=t^N.
Hence the cyclic Ward completion and the regular centralizer have
an exact matching determinant character, with their marked
peripheral power map specified. This is stronger than matching
their numerical complete values.

It is a comparison of characters, not of the entire groups. For
N>2 the one-parameter family I+t Ecyc is not in general closed
under multiplication, and its unit algebra has dimension N.
The regular centralizer is one-dimensional. No group isomorphism
or compatible bulk action follows merely from (7) and (12).

The actual nilpotent Ward relative class is constructed in
[the coherent-cut/Ward note](coherent_cut_obstruction_and_ward_relative_class.md).
The remaining task is to transport this cyclic edge and norm data
through the actual partial Gaussian/adjoint diagram, retaining the
boundary source and the prescribed cut. The selected regulator
period and its volume growth remain unproved.

## 5. A literal quantum-factorial gauge and its scalar cyclic source

The norm comparison has an explicit affine transport realization.
Define the finite quantum-factorial polynomial

    f_N(t,e)=sum_(j=0)^(N-1) (-t e)^j/(Q;Q)_j.    (13)

Every denominator is nonzero at the primitive root. Its coefficients
obey f_j(Q^j-1)=t f_(j-1). Consequently, as a polynomial identity,

    f_N(t,Qe)-(1+t e)f_N(t,e)
                   =-t(-t)^(N-1)e^N/(Q;Q)_(N-1). (14)

The primitive-root product (Q;Q)_(N-1)=N follows by evaluating
(z^N-1)/(z-1) at z=1. In A_N, (14) becomes the exact affine
source equation

    f_N(t,Qe)-(1+t e)f_N(t,e)
                         =-kappa_N t^N/N.         (15)

This sign and scalar hold at even and composite levels as well.
On the actual nilpotent Ecal, the right side is zero because
Ecal^N=0. The gauge f_N(t,Ecal) is unipotent and invertible for
every t. On the cyclic completion its failure is precisely the
displayed scalar, not an unspecified numerical normalization.

There is also an actual matrix shift implementing this equation.
The literal root matrix K satisfies

    K Ecyc K^(-1)=Q Ecyc,                        (16)

including the last cyclic edge. Thus (15) is a finite matrix Ward
equation with Ad_K on its first term. At the ideal fiber it is
an explicit meridian-regular Hilbert-90 gauge in k[e]/(e^N), with constant
coefficient one. More generally the connected special norm-one
units have a finite nilpotent logarithm; in the basis e^j the
equation (sigma-1)g=log a is solved by dividing its j-th coefficient
by Q^j-1, j=1,...,N-1. The disconnected constant phases mu_N
remain separate: an integral unit coboundary has constant term
one, so those phases cannot be silently removed by such a gauge.

Here meridian regularity is over the characteristic-zero cyclotomic
coefficient field. The displayed cyclotomic factorial inverses are
retained; arithmetic integrality at their primes is not asserted.

Dividing the scalar source in (15) by the actual missing edge
kappa retains

    -u_N(M)t^N/N, with complete value -t^N.       (17)

Multiplication by the whole d_N in (10) instead gives the exact
normal source -i^(N+3) kappa t^N/N. These are different recorded
regularizations; neither replaces u_N by its numerical value
before the common zero is canceled.

The field norm, quantum-factorial transport, cyclic endpoint defect
and peripheral adapter have therefore been computed in one literal
matrix model. Matching this model's action on the internal geometric
framing class remains necessary; an equality of norm characters
alone does not construct that map or prove the volume conjecture.

## 6. Subsequent whole group and function transfers

The [norm-root period theorem](cyclic_ward_norm_root_period.md)
now strengthens the character comparison to an explicit group
morphism. For a unit u in the retained cyclic normal order, choose
the marked root nu^N=Norm(u), nu=1 modulo kappa. Then

    u -> C_M((nu-1)/kappa)

is a regular group morphism with norm-one kernel. On u=1+t e
it takes the full marked path t=0,...,M to the regular centralizer
path with endpoints b=0,M, and its invariant differential integrates
exactly to Log(M^2)/kappa. The bare kappa=0 fiber does not retain
this morphism's first-normal character.

The [coherent Ward unfolding](unfolded_ward_factorial_and_regulator.md)
also reconstructs the whole factorial from the actual all-level
nilpotent jets. Its logarithmic cyclotomic pole is a dilogarithm,
its marked regular part gives the normalized Hilbert-90 gauge,
and its normal derivative gives exactly (17). On the genuine
integral complete-color tensor lift, that same pole evaluates to
the [finite divided-power exponential](divided_ward_factorial_fusion.md)
exp[(-t)^N J_b/N], with J_b^b=0. This lift follows M=-q^N;
its normal must not be substituted for the fixed-root kappa normal.

The [literal crossing Ward currents](local_r_ward_transfer_currents.md)
prove ordinary global cancellation of the cyclic-edge wall source.
In contrast, the [marked divided-normal cut](divided_adjoint_marked_edge_pairing.md)
has a specified nonzero missing-edge pairing and is cohomologous
to the original normalized cut. It returns exactly the original
Kashaev value on every closed cut tangle. The full geometric
source comparison still has to preserve this relative cut before
its contraction; ordinary wall nonvanishing is no longer a premise.

The [common-Verma source](common_verma_two_wall_source.md) now
also realizes a literal regular-centralizer action on the actual
completed block module. Its shift and divided F-power form a Weyl
pair; the normalized coherent kernel carries the group action and
the marked period as an explicit source matrix coefficient. The
[balanced crossing comparison](balanced_verma_coherent_braiding.md)
keeps this coherent source through the genuine root crossing.
This strengthens the group transfer without identifying its
reducible source base with the internal geometric framing.

[Exact audit](../experiments/audit_cyclic_ward_norm_adapter.py).
[Results](../experiments/cyclic_ward_norm_adapter_results.json).
