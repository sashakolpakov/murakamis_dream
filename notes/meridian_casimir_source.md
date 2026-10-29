# An actual meridian source on the tensor Casimir cover

Research note, 26 October 2026. This derives an inhomogeneous meridian
equation from the literature ADO crossing itself. Its source is a
specified spectral projector, with the full factor 1+M^(-2N).
The coincident spectral directions at completeness are the actual
meridian confluence, not a separately chosen infinitesimal model.
Their source residue is a fixed rank-one cup/cap operator.

The result is local to two tensor factors. It is not an identification
of the full knot quantum-A operator with its geometric A-polynomial,
nor a proof of the selected regulator norm. The connection constructed
below still has to be assembled through the whole colored network.

## 1. The fixed operator and its generic meridian spectrum

Use q=exp(pi*i/N), Q=q^2, rho=q-q^(-1), N>=2, and the actual
ADO color x=-M/q. Put

    Y=M^2, U=Y^N=M^(2N).

On V(x), the matrices E,F,K and checked crossing B_N(M)
are exactly those in [the semicyclic source proof](semicyclic_carry_braiding.md),
restricted here to F^N=0. In particular K v_a=xQ^(-a)v_a,
F v_a=v_(a+1), F v_(N-1)=0, and E v_a=e_a(x)v_(a-1).

Let Omega be the actual tensor Casimir,

    E_tot=E tensor K+1 tensor E,
    F_tot=F tensor 1+K^(-1) tensor F,
    Omega=rho^2 F_tot E_tot+q K_tot+q^(-1)K_tot^(-1).

For generic M its N distinct Casimir nodes and crossing values are

    c_j(Y)=q^(-2j-1)Y+q^(2j+1)Y^(-1),
    lambda_j(Y)=nu_j Y^(-j),
    nu_j=(-1)^j q^(j(j+1)), 0<=j<N.                  (1.1)

Each component has dimension N. Here is an elementary verification.
At total degree j write the highest vector as
h_j=sum_(a=0)^j b_a v_a tensor v_(j-a), b_0=1. Its E-equation is

    b_(a+1)/b_a=-e_(j-a)(x)/
                  (e_(a+1)(x) x Q^(-(j-a-1))).

For generic x the denominators are nonzero. Multiplication gives
b_j=(-1)^j x^(-j)Q^(j(j-1)/2). The defining finite R is
triangular, so the coefficient of v_0 tensor v_j in B h_j
comes only from its zero-th term on v_j tensor v_0. Thus

    lambda_j=(-1)^j x^(-2j)Q^(j(j-1)/2)=nu_jY^(-j).

The N descendants F_tot^r h_j are nonzero generically: the
E F^r recurrence has no zero coefficient for 0<r<N.
F_tot^N=0 by the root q-binomial identity. Their different
Casimir nodes imply a direct sum, and the dimensions total
N^2. This proves the spectrum and complete decomposition
without importing a tensor-decomposition theorem.

Define T_0(z)=2,T_1(z)=z,T_(n+1)=zT_n-T_(n-1).
Since T_n(a+a^(-1))=a^n+a^(-n), (1.1) proves

    product_j(z-c_j(Y))=P_(N,U)(z),
    P_(N,U)(z)=T_N(z)+U+U^(-1).                     (1.2)

Thus the actual local spectral algebra is

    A_(N,U)=C(U)[z]/P_(N,U)(z).

It splits after the specified root cover Y^N=U. The polynomial
r(Y,z) of degree less than N with r(Y,c_j)=lambda_j satisfies

    B_N(M)=r(Y,Omega).                              (1.3)

The scalar conventions are explicit. At M=1 the usual
highest-weight quantum-group R in the earlier crossing
calculation has checked matrix lambda_0 B_N(1), with
lambda_0=q^((N-1)^2/2). The ADO crossing used here is already
B_N(1); its original pivot, zero-framing twist and full
modified dimension are not changed.

## 2. The affine meridian equation and its full peripheral source

Let sigma(Y)=QY and sigma(z)=z on the split spectral algebra.
The nodes obey c_j(QY)=c_(j-1)(Y), with indices modulo N.
For the values in (1.1),

    lambda_(j+1)(QY)=-Y^(-1)lambda_j(Y), j<N-1,
    lambda_0(QY)=1,
    -Y^(-1)lambda_(N-1)(Y)=-U^(-1).

Let E_(N-1)(Y,z) be the spectral idempotent with value one at
c_(N-1) and zero at the other nodes. Interpolation therefore
proves the exact equation

    sigma(r)=-Y^(-1)r+(1+U^(-1)) E_(N-1).            (2.1)

This source has not been chosen to obtain a desired period:
the exceptional last component is forced by the actual
highest-weight eigenvalues. The generic idempotent is

    E_(N-1)=product_(j=0)^(N-2)
               (z-c_j(Y))/(c_(N-1)(Y)-c_j(Y)).       (2.2)

The homogeneous cyclic norm is exactly

    Norm_sigma(-Y^(-1))=-U^(-1),                    (2.3)

because Q^(N(N-1)/2)=(-1)^(N-1), at both parities.
Thus 1+U^(-1) is precisely 1 minus that norm. It becomes
two at completeness, but it must first be retained as a
whole function multiplying (2.2).

There are two different norms here. The Casimir-algebra norm
of r is

    Norm_spec(r)=(product_j nu_j)Y^(-N(N-1)/2),
    det B_N=Norm_spec(r)^N.                          (2.4)

The root phase product_j nu_j is retained. Equation (2.3)
instead concerns the cyclic meridian transport.

Iterating (2.1) gives an affine monodromy with homogeneous
block -U^(-1) and source s=(1+U^(-1))r. Away from U=-1
the cyclic resolvent reconstructs the unique solution r.
These are identities before any polar specialization. At
a resonance or a node collision a displayed zero times
a projector pole cannot be evaluated separately.

## 3. A genuine matrix meridian comparison, including parity

There is an explicit operator realization of sigma in (2.1).
Let H(M) have columns F_tot^r h_j(M), ordered by j and then r.
Let P send label j to j+1 modulo N, keeping r fixed. Put

    G(M)=H(qM) P H(M)^(-1).                          (3.1)

The highest K-root of component j at M is
x^2 Q^(-j). It equals that of component j+1 at qM.
The descendants use the same fixed F normalization.
Consequently G intertwines all three actual total E,F,K
operators. In particular it keeps the Casimir observable z fixed.

Equations (1.1) and (3.1) give the actual matrix identity

    G(M)^(-1) B_N(qM) G(M)
       =-Y^(-1)B_N(M)
                  +(1+U^(-1)) E_(N-1)(Y,Omega).      (3.2)

This is not merely equality of spectra. H and G are specified
rational matrices on the generic color chart; no unrelated
normalization is chosen at each shift.

The meridian cover also keeps its sign. After N shifts,
M becomes -M. If S_2 is the sign matrix (-1)^a on the
second factor, the highest-vector recurrence gives

    H(-M)=S_2 H(M) diag_(j,r)((-1)^j).               (3.3)

Thus the N-step matrix transport is
H(-M)H(M)^(-1), with both its color parity and spectral-sign
unit retained. The 2N-step transport is identity. On the
abstract Casimir algebra (2.1) already uses Y, whose shift
has order N; forgetting the parity on the actual tensor
module would require the explicit identification (3.3).

The subsequent [intrinsic cut and meridian atlas](intrinsic_cut_and_meridian_atlas.md)
assembles these maps on a generic even-strand braid using explicit
centralizer transitions and preserves the full selected cut. It does
not construct the integral geometric triangulation comparison.

## 4. Its complete spectral jet is the actual meridian confluence

Write u=Log M near M=1. Pair j with l=N-1-j, and put
h=2j+1<N. Then nu_l=nu_j and exactly

    c_j-c_l=-(q^h-q^(-h))(Y-Y^(-1)),
    lambda_j=nu_j M^(-2j),
    lambda_l=nu_j M^(-2l).

The confluent divided difference is therefore

    [(lambda_j-lambda_l)/(c_j-c_l)]_(M=1)
       =-nu_j(N-1-2j)/(2(q^h-q^(-h))).               (4.1)

The double point is an honest finite flat meridian algebra.
In the pair factor, eta=z-c_j(M) satisfies

    eta(eta+c_j-c_l)=0.                             (4.2)

At completeness it becomes eta^2=0. The unit r specializes
to nu_j plus the coefficient (4.1) times eta. Replacing
its value-and-divided-difference interpolation rows by the
confluent rows gives an invertible Hermite Vandermonde.
Thus the coefficients of r are regular at M=1. Equation
(1.3) specializes to the earlier crossing polynomial,
including its nilpotent part.

For odd N the node with 2j+1=N is simple and has only its
value condition. No inverse of two modulo an even N is used.

This supplies a meridian derivation of the same jet that
the earlier proof obtained by varying q. In particular it
identifies a specific actual spectral jet with the
meridian collision; the internal carry parameter epsilon
and the auxiliary source coordinate remain different data.

## 5. The polar source residue is the actual cup/cap

Let c_0=q+q^(-1), and let e_0 be the idempotent of the
double c_0 factor of P_(N,1). On the actual nilpotent
tensor module write

    J_N=(Omega-c_0)e_0, J_N^2=0.                    (5.1)

Let J_x be the actual self-duality matrix at the Kashaev
color, (J_x)_(N-1-a,a)=q^(a^2), and g=K^(1-N).
Use the existing cup and right cap to form

    cup=vec(J_x^(-t)),
    cap=vec(g J_x)^t,
    Pi_N=cup*cap.                                   (5.2)

Then exactly

    Pi_N^2=0, rank Pi_N=1,
    ptr_g(Pi_N)=I,
    J_N=(-1)^N rho^2 Pi_N.                          (5.3)

Here is a proof of the last identity. At generic q the
total degree-d Casimir characteristic polynomial has labels
0 through min(d,2N-2-d), by the highest-vector decomposition
already proved in the preceding Casimir note. At this root,
the node c_0 occurs with multiplicity two only at degree
N-1, and with multiplicity one in every other degree.
Hence J_N has rank at most one and is zero off degree N-1.
Commutation with E_tot,F_tot then makes its image invariant.
The invariant vector and covector spaces are one-dimensional,
by simplicity and the actual self-duality of V_N. Thus J_N
is a scalar multiple of the cup/cap in (5.2).

The independently proved closing functional in
[the Casimir trace calculation](casimir_braiding_and_recoupling_lattice.md#8-the-actual-closing-trace-is-a-spectral-jet-functional)
gives ptr_K(J_N)=-rho^2 I. Since
g=(-1)^(N-1)K here, and direct cup/cap contraction gives
ptr_g(Pi_N)=I, the scalar is (-1)^N rho^2. It is nonzero,
proving both the rank and the normalization in (5.3).

The generic projector (2.2) has a simple pole. Its actual
first meridian coefficient is

    [u E_(N-1)(Y,Omega(M))]_(M=1)=J_N/(4rho),
    [(U-1) E_(N-1)]_(M=1)=N J_N/(2rho).            (5.4)

Indeed c_(N-1)-c_0=rho(Y-Y^(-1)) has u-derivative
4rho; every other denominator factor is a unit. This
also follows by evaluating its full product numerator,
without a small numerical parameter.

Keeping the source coefficient in (3.2) gives

    [(U-1)(1+U^(-1)) E_(N-1)]_(M=1)
        =N J_N/rho=(-1)^N N rho Pi_N.               (5.5)

This is an actual meridian-normal source residue with its
full N and parity factor. Its pivotal closing is nonzero.
The individual shifted frame and projector may be polar;
the regular crossing and its complete cyclic identity
retain the resulting cancellation.

## 6. A pure braid detects the same nonreduced source

At completeness r(c_0)=1 and r'(c_0)=-(N-1)/(2rho).
On the double c_0 block the actual full twist therefore obeys,
for every integer m,

    e_0(B_N(1)^(2m)-I)
        =(-1)^(N+1)m(N-1)rho Pi_N.                  (6.1)

Its actual pivotal partial trace is the same nonzero
coefficient times I. Thus closing with this specified
Casimir projector detects the jet. This is an inserted
operator test, not a claim that every knot period couples
to this block by itself.

The localized unit I+(-1)^(N+1)(N-1)rho Pi_N has determinant
one and fixes the cup. Nevertheless it is nontrivial.
On a two-dimensional invariant subspace it acts on a lift
of its fixed quotient by a nonzero affine translation.
Its m-th power multiplies that translation by m.

Consequently the actual strand braiding cannot descend
projectively to strand permutations on the full retained
source: a transposition would have scalar square. No
finite-index cover kills this unipotent holonomy in
characteristic zero. This is not a contradiction to the
finite cyclic Hilbert-90 theorem, whose norm-one hypothesis
is different. The infinite-order conclusion uses (6.1)
in characteristic zero; finite-field tests alone would
not prove it.

The appropriate local frame group includes the units of
the nonreduced Casimir algebra, not only its reduced
scalars or determinant line. This does not disprove a
published decorated tetrahedral symmetry using different
adapters, and does not identify strand braids with
geometric tetrahedron permutations.

The [subsequent actual-braid theorem](actual_braid_group_and_spectral_source.md)
strengthens this test. Raising both adjacent original
crossings to the power 2N gives square-zero logarithms J_12,
J_23 with a strictly negative mixed ordinary trace. Their
pivotal moment has the exact value -2N^2/rho. A nonzero
product eigenvalue gives an SL_2 quotient in the connected
braid-image closure, and every finite-index restriction
retains it. This concerns the full braid-source realization,
not an assertion about the selected minimal A-operator's
difference-Galois group or its geometric period quotient.

## 7. Verification, coverage and the remaining theorem

[The audit](../experiments/audit_braided_source_groupoid.py)
compares the literal ADO crossing to its generic-color
Casimir interpolation at N=2,3,4,5,6,9. It constructs
H and G, checks all total E,F,K intertwinings and (3.2),
the Chebyshev equation, both distinct norm calculations,
and the retained N-step parity.

At ten levels through 15 it also checks the actual
rank-one cup/cap identity, the meridian source residue,
the full-twist powers and the nonzero pivotal closing.
These are exact finite-field diagnostics for the uniform
arguments above. [Results](../experiments/braided_source_groupoid_results.json).

The definitions remain the actual cyclic/quantum-group
crossings and recouplings. The literature coverage is
[Kashaev's cyclic 6j framework](https://arxiv.org/abs/hep-th/9411147)
and [Kashaev--Reshetikhin's holonomy R-matrices](https://arxiv.org/abs/math/0202212).
Only their abstracts were consulted here for coverage;
their proofs are not premises.

The [braided source groupoid](braided_source_groupoid.md)
supplies coherent recoupling/source transport with moving
semicyclic centers. The subsequent
[intrinsic cut theorem](intrinsic_cut_and_meridian_atlas.md)
proves a basis-independent full cut, with its actual modified
dimension, and assembles generic braid meridian charts with
their non-scalar centralizer transitions. It also identifies
the complete two-factor Casimir order and its full dual by
a perfect pivotal residue pairing. The integral relative
geometric source still needs to be compared; it is not
supplied by positive ideal shapes or by generic assembly.

The cover (1.2) is the actual local tensor Casimir cover.
It is not asserted to be the geometric knot A-curve.
The geometric quantum-A component, selected global source
and marked Bloch-regulator norm remain unproved. The
original Kashaev volume conjecture remains the active goal.
