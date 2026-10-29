# Volume limits constructed from the A-polynomial

Research note, 26 October 2026. This is an auxiliary classical
A-polynomial volume identity. The intended full route starts
with Kashaev's own quantum A-module or torsor and uses its
structure to prove the invariant's volume growth. This
classical construction calibrates the geometric period; it
does not replace that actual invariant. Jones is separate.

Here is a direct classical construction. It produces marked
roots of integer polynomials built from the A-equation by
finite-algebra norms, with a proved volume limit on the stated
connected geometric class. The remaining choices are a marked
curve, path and sampling. No standard quantum A-state is claimed
for this construction. It is a discretization of the existing
classical regulator, not a claim to have proved the original
Kashaev conjecture or to have discovered the regulator identity.

## 1. Conventions and the relative period

Use the squared peripheral functions m,l of
[the marked regulator note](boundary_regulator_period.md).
In SL_2 eigenvalues M,L these are m=M^2,l=L^2, with the
recorded orientation of the longitude. Write the corresponding
geometric A-equation as A(m,l)=0. It is obtained from the
ordinary eigenvalue A-polynomial by its stated finite
monomial image, not by renaming M as M^2 without elimination.

Let C be a connected marked algebraic curve of representations
or a finite augmented cover, containing the geometric and
conjugate complete points p_+,p_-. Let beta be its rational
crossing or triangulation Bloch class. The already proved
boundary identity and complete fundamental-class values are

    delta beta=-(1/2)m wedge l,
    D(beta)(p_+)=Vol(X), D(beta)(p_-)=-Vol(X).    (1.1)

They follow from the actual
[boundary-wedge calculation](marked_braid_holonomy.md#8-a-global-boundary-wedge-and-complete-frame-regulator-rigidity)
and [fundamental-cycle calculation](crossing_fundamental_cycle.md).
No selected quantum state is a premise.

Put

    eta=log|l| darg m-log|m| darg l.

The elementary Bloch--Wigner derivative is
dD(z)=log|z|darg(1-z)-log|1-z|darg z. Applying it to
(1.1) gives dD(beta)=eta/2. Consequently every piecewise
C^1 path gamma from p_- to p_+, avoiding the finite shape
and coordinate divisors, has

    integral_gamma eta=4 Vol(X).                 (1.2)

The normalized complete places must be retained: their
peripheral coordinate pairs can coincide even though their
regulator values differ. This fixes the absolute volume by
two specified endpoints, without a zero-volume reference.

If C is finite over a normalized A-component, its real
primitive descends. Pass to a connected Galois closure.
A deck transformation changes the primitive by a constant,
since it fixes eta. Its finite order makes that constant
zero. Thus the primitive is invariant and descends on the
common regular open curve. This is an elementary finite-cover
descent argument; it does not concern a quantum state.

## 2. Integer products of A-roots

Parametrize gamma on [0,1]. Choose continuous argument lifts
theta=arg m, phi=arg l along it. For large N put

    r=floor(sqrt(N)), h=2pi/N, t_j=j/r.

For each interval choose an algebraic point q_(N,j) on C
within N^(-2) of gamma((j+1/2)/r), in a fixed finite
collection of regular coordinate charts. Such points exist:
use a local finite algebraic projection and approximate its
regular value by an algebraic number. Avoid its finitely many
ramification and coefficient exceptions. Set

    m_j=m(q_(N,j)), l_j=l(q_(N,j)),
    a_j=nearest_integer((theta(t_(j+1))-theta(t_j))/h),
    b_j=nearest_integer((phi(t_(j+1))-phi(t_j))/h),
    Z_N=product_(j=0)^(r-1) l_j^(a_j) m_j^(-b_j). (2.1)

Fix either convention at a rounding tie. These are finite
algebraic evaluations with integer exponents; no volume
value occurs in their definition. All pairs satisfy the
A-equation, with the branch specified by gamma.

**Theorem.** Under Section 1's connectedness and marking
hypotheses,

    lim_(N->infinity) [pi/(2N)]log|Z_N|=Vol(X).   (2.2)

**Proof.** Logs of the moduli are bounded on the compact
path. Integer rounding changes h log|Z_N| by O(r/N).
Replacing the midpoint values by their algebraic
approximants changes it by o(1); the total argument
variation is bounded. The remaining sum is the midpoint
Riemann sum for integral eta. Its error tends to zero
for a piecewise C^1 path. For a C^2 path the total error
is O(r^(-1)+r/N+N^(-2)), hence O(N^(-1/2)). Equation
(1.2), and h/4=pi/(2N), prove (2.2).

The limit is independent of the allowed path, samples and
rounding choices because eta has the stated real primitive.
The finite values need not be independent of those choices.

## 3. A polynomial defined by norms, not just an informal root product

Here is an explicit polynomial containing the marked value
Z_N. Let F_N be a number field containing the coefficients
of A and the sampled meridians m_j. Require only that the
leading and constant l-coefficients at each sample are
nonzero; finite exceptional sample points can be avoided.
Normalize each A(m_j,L_j) to be monic and form

    E_N=tensor_(j,F_N) F_N[L_j]/(A(m_j,L_j)).

It is a finite algebra. Each L_j is a unit. Let

    H_N=product_j L_j^(a_j)m_j^(-b_j) in E_N,
    Q_N(T)=det(T-Mult_(H_N)) in F_N[T],
    P_N(T)=primitive_integer_multiple
                          of Norm_(F_N/Q)(Q_N(T)). (3.1)

All operations are polynomial remainders, multiplication
matrices, determinants and number-field norms. Equivalently
one can use successive resultants. Evaluation L_j->l_j
sends H_N to Z_N, so Q_N(Z_N)=P_N(Z_N)=0. Thus (2.2)
is a marked-root limit for explicitly A-generated integer
polynomials P_N.

The chosen root is essential. A field norm or the largest
root over all independent sheet choices can combine other
periods. No formula for such an unmarked choice is asserted.
This construction is a classical polynomial period, with an
existing algebraic norm definition; it is not a new definition
of the literature quantum A-operator.

## 4. Cover transfer is exact before taking the limit

For a peripheral monomial map

    m'=m^a l^b, l'=m^c l^d, k=ad-bc>0,

use the same sampled marked points upstairs and transfer
the integer increments by

    a'_j=a a_j+b b_j, b'_j=c a_j+d b_j.

Then ordinary multiplication proves exactly

    product_j (l'_j)^(a'_j)(m'_j)^(-b'_j)=Z_N^k. (4.1)

Thus this algebraic period has the correct degree law before
any asymptotic argument. For a connected one-cusped manifold
cover, k is the manifold degree. Laurent elimination gives
the upstairs geometric A-factor as in
[the cover calculation](regge_period_covers_and_a_curves.md).
Independent rounding upstairs changes the scaled log by
o(1), so it gives the same limiting law.

## 5. A connected infinite class from the twist presentation

Here is an independent algebraic connectedness argument,
which avoids assuming an irreducibility theorem from the
literature. Use the signed twist convention

    G_k=<a,b | a w^k=w^k b>, w=ab^(-1)a^(-1)b.

Reading a full pair in the twist box conjugates by w;
after k pairs the clasp closes by a w^k=w^k b. For k=1
the relation reduces to aba=bab. The hyperbolic twist
members have k<=-1 or k>=2. The independently certified
families in [the twist topology note](twist_topology_and_peripherals.md)
have parameters p=-k-1 (even family) and p=k-2 (odd
family), respectively. Their geometry is supplied by the
explicit positive face/angle proof, rather than a cited
character-variety irreducibility theorem.

On the nonabelian meridian chart use

    A=[M 1;0 M^(-1)], B=[M 0;-u M^(-1)],
    s=M^2+M^(-2), W=AB^(-1)A^(-1)B,
    z=Tr(W)=u^2+(2-s)u+2.

Direct multiplication gives

    A W-W B=(s-u-1)(A-B).

Let S_(-1)=0,S_0=1,S_(j+1)=z S_j-S_(j-1), extended
to all integer indices, and put S=S_(k-1),T=S_(k-2).
Cayley--Hamilton gives the single relation

    (s-u-1)S-T=0.                               (5.1)

Consecutive S,T have no common root. Also S(2)=k,
T(2)=k-1. Set v=s-u-1; then z=2+u(1-v).
On (5.1), S!=0 and v!=1: otherwise z=2 and S-T=1
would contradict (5.1). Hence every point of this chart is
given by the rational parametrization

    v=T/S, u=(z-2)S/(S-T),
    s=z-1/[S(S-T)].                             (5.2)

The last equality uses S^2+T^2-z S T=1. This proves
absolute irreducibility of the relevant (s,u) curve.

The squared meridian m=M^2 gives the double cover

    m^2-s(z)m+1=0.                              (5.3)

It is also absolutely irreducible. For k>0, D=S(S-T)
has degree 2k-2, so (z-2)D-1 has odd degree 2k-1,
is coprime to D, and has an odd-order zero. Thus
s(z)^2-4 cannot be a square in C(z).

For k=-h<0, take the largest real root z_0 of S_h,
which lies in [0,2). At that point T=0, S^2=1, D=1,
so s(z_0)=z_0-1 is strictly between -2 and 2. The
real rational function s(z)^2-4 is negative there and
positive for large real z, since s(z)~z. A real rational
function that is a square in C(z) is either a real square
or minus a real square: conjugating its square root gives
the same root up to sign. Such a function cannot change
sign on its real regular locus. This proves (5.3).

Consequently this real irreducible marked eigenvalue curve
contains both conjugate complete holonomies. The preferred
squared longitude is a rational function on it, obtained
from its peripheral word; its A-image is nonconstant and
the map to that curve is finite on regular open sets.
The complete volume values and boundary differential are
(1.1). Therefore the polynomial limit theorem applies to
every hyperbolic member of this twist family.

The rational parametrization and connectedness are the
additional algebraic checks here. The full hyperbolic
geometry and preferred-peripheral certificates are the
previously reconstructed ones; their conventions still
have to be kept when writing a numerical A-polynomial.

## 6. A simpler cone product when a zero-volume endpoint is available

This gives a useful direct numerical test, independent of
the rounded two-endpoint construction. In ordinary SL_2
coordinates take the expanding longitude L(alpha), with
M(alpha)=exp(i alpha/2), 0<=alpha<=Theta, along a geometric
cone family ending at volume zero. Schlaefli gives

    Vol(X)=integral_0^Theta log|L(alpha)| d alpha.

If M_E=exp(i Theta/2) is algebraic, choose q_N^N=M_E
on that arc and L_j the continued A-root at M_j=q_N^j.
Then

    lim_(N->infinity) (Theta/N)
                         log|product_(j<N) L_j|=Vol(X). (6.1)

The proof is the Riemann-sum theorem, including continuous
or integrable logarithmic endpoint singularities. The
geometric cone and zero-volume endpoint are hypotheses,
not consequences of alternatingness. The earlier
[cone-transfer note](quantum_a_volume.md) supplies this
geometry and its quadratic A-factor for the figure-eight.
Here the left side is the algebraic root product itself;
no transfer-state dominance assumption is required.

## 7. Scope and coverage

The classical regulator/volume framework is existing work.
[Guilloux--Marche, 1804.01395](https://arxiv.org/abs/1804.01395)
studies exact polynomials, their volume functions and Mahler
measures. Its abstract was checked for coverage; its proofs
are not premises for the arguments above. A bare Mahler
measure is a different observable from the marked product
here and can collect several volume contributions.
[Hoste--Shanahan, math/0311051](https://arxiv.org/abs/math/0311051)
provides adjacent coverage of twist-character recursions.
The matrix, Chebyshev and irreducibility arguments above
are independent of that proof.

This is a proved classical marked polynomial-period limit,
with an explicit broad connectedness criterion and the twist
family application. Its finite sampling is not canonical.
Constructing a preferred sequence from an existing quantum
A-definition, and proving its volume limit, remains a further
goal. Recovering Kashaev directly is its own subsequent
objective, as distinguished from a relation with Jones.

## 8. Relation to the actual Kashaev torsor program

The intended quantum route uses the A-structure attached to
Kashaev itself to prove its volume growth. Its comparison
with the previous repo is in
[the primary status, Section 0](a_polynomial_torsor_status.md#0-comparison-with-the-previous-work-in-this-repo).

The finite classical products above are not already that
invariant. A direct small-level calibration is instructive:
for the figure-eight at N=2 the cone product in Section 6
is 2+sqrt(3), whereas the original enhanced Kashaev crossing
gives 5. The audit evaluates the latter directly from its
W-symbol and pivotal closure, without a Jones evaluation.
This only distinguishes this particular classical product
from the finite invariant. It is not an obstruction to the
invariant's own quantum A-torsor route.

There is already a direct operator-period mechanism in
[the all-level A-period note](all_level_a_period.md): a
specified actual quantum annihilator and finitely many
fixed initial periods recover Kashaev exactly by a companion
product and whole-germ root evaluation. Its verification
uses the original cut and quantum-group quotient modules.
Jones need not be a definition or a proof input there.

There is no need to reconstruct the invariant from the bare
classical polynomial alone. The intrinsic route already
starts with its actual annihilator and pointed source.
Its geometric classical support and selected regulator norm
are the missing conclusions. The classical product identity
above supplies neither conclusion for that quantum object.
A comparison to Jones is additional.

[Audit](../experiments/audit_a_polynomial_volume_limits.py).
[Results](../experiments/a_polynomial_volume_limits_results.json).
