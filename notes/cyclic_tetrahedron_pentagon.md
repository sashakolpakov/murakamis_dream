# Exact root-cyclic tetrahedral pentagons with their source frames

Research note, 26 October 2026. The four-atom crossing construction
has a strict local three-to-two operator identity on a compatible
anchored root cover. The proof below retains the transported central
frames, determinant roots, monomial shears and scalar phase. It does
not identify arbitrary independent lifts of the roots, assign all
face and boundary tensors to a geometric triangulation, or prove
the selected regulator norm of the knot period.

The local function is the literature cyclic dilogarithm already
specified in [the four-atom note](four_cyclic_atoms.md). No different
knot invariant is defined. The generic formal identity is proved
directly in [the Verma transport note](verma_tetrahedral_transport.md).

## 1. The normalized finite atom

Fix N>=2, q=exp(pi*i/N), Q=q^2. For a primitive monomial m with
m^N=mu^N, choose nu^N=1-mu^N, with both factors nonzero. On the
eigenvalue mu Q^j put

    f_0=1, f_j=nu^j/(mu;Q)_j, 0<=j<N,
    C(m)=f(m), F=product_j f_j,
    D(m)=gamma C(m), gamma^N=F^(-1).                 (1.1)

The root of gamma is retained. Near a zero coefficient tag choose
nu=gamma=1; the matrix D then extends with value I. Formula (1.1)
is exactly the alternate literature cyclic dilogarithm, with its
compatible branches:

    mathfrak_d_N(z;Q)=(1-z^N)^((N-1)/(2N))
                      product_(ell=1)^(N-1)(1-Q^ell z)^(-ell/N).

On a module of dimension rN, every eigenvalue has multiplicity r,
so det C=F^r and det D=1. All half roots required at even N are
included; no division by two modulo N is used.

If m A=Q^k A m, the finite conjugation r_m obeys

    r_m(A) D(m)=D(m) A', A'=nu^(-k) A.             (1.2)

Here r_m is the rational conjugation by the generic compact
dilogarithm, expressed by finite products of 1-Q^ell m. Its
denominators are invertible when 1-m^N is. Equation (1.2), proved
by the recurrence in (1.1), specifies the changing target frame.

## 2. The primitive cyclic pentagon

Take XY=QYX, X^N=U, Y^N=V. Choose three norm roots

    a^N=1-U, b^N=1-V, h^N=H=1-U+UV.               (2.1)

Write D(m;nu) to display the root used in (1.1). Then on the
compatible root component anchored at X=Y=0,

    D(Y;b) D(bX;h)
      =D(X;a) D(-YX/a;h/a) D(Y/h;ab/h).           (2.2)

Zero here refers to the coefficient tags of fixed clock/shift
matrices, so the anchor is a regular formal matrix specialization.
Away from it the monomial centers are nonzero. The five atom
centers in their displayed order are

    left:  V, (1-V)U;
    right: U, -UV/(1-U), V/H.                    (2.3)

In particular (-YX)^N=-UV at every parity. A compatible spectral
root of the middle monomial is qxy/a if x^N=U, y^N=V.
The right norm roots h/a and ab/h are forced ratios, rather
than new independent choices. The final X,Y splitting roots on
both paths are bx,y/h.

Here is a uniform proof of the scalar in (2.2). The directly
proved compact pentagon has rational conjugations with no poles
other than the indicated norm divisors. Clearing those factors
and specializing Q therefore gives the same rational quantum
automorphism on both sides. Equation (1.2) implements it between
the same initial and final splitting representations. Those
representations generate the full matrix algebra. The ratio of
the two invertible products is consequently a scalar lambda.
Their determinants are one, so lambda^N=1. All the matrices and
normalization roots are algebraic on the specified lifted cover.
Thus lambda is constant on each irreducible component. At the
regular formal anchor every atom is I, so lambda=1 on its
component. This proves (2.2).

Independent choices of the five gamma roots can lie on other
components; their residual phase is not erased by the theorem.
Using raw C instead gives L_raw=lambda_raw R_raw, with

    lambda_raw^N=F_L1 F_L2/(F_R1 F_R2 F_R3).        (2.4)

The anchor fixes its compatible lift. Determinants alone fix only
the power in (2.4).

## 3. Include the tetrahedral monomial shears

For three leaves use uniform clock/shift pairs

    Z_i e_a=z_i e_(a+1), S_i e_a=s_i Q^a e_a,
    S_i Z_i=Q Z_i S_i.

The shear C_ij is the literal permutation

    (a_i,a_j) -> (a_i,a_j+a_i mod N).

Its target splitting roots are

    z_i'=z_i z_j, z_j'=z_j, s_i'=s_i, s_j'=s_j/s_i.   (3.1)

Indeed the source algebra images of Z_i and S_j are Z_i Z_j
and S_i^(-1)S_j. Direct action on the normalized basis proves
the two intertwining equations; the other generators are fixed.
The shears obey exactly

    C_12 C_13 C_23=C_23 C_12.                     (3.2)

In an unnormalized polynomial basis there are also carry factors
from reducing exponents modulo N. Formula (3.1) uses normalized
monomial frames and does not authorize dropping those factors
when comparing with the actual Verma or cut basis.

Evaluate m=-Q t Z_i Z_j^(-1) S_j^(-1) after the shear (3.1).
In the roots before that shear, a spectral root is

    mu=q t z_i s_i/s_j,
    nu^N=1+t^N z_i^N s_i^N/s_j^N.                (3.3)

The commutation integers of m with (Z_i,Z_j,S_i,S_j) are
(0,-1,-1,+1). Define the typed tetrahedral operator by

    T_ij(t;nu)=C_ij D(m;nu)^(-1).                 (3.4)

Combining the shear with the inverse atom gives its final roots

    z_i''=z_i z_j, z_j''=z_j/nu,
    s_i''=s_i/nu, s_j''=s_j nu/s_i.              (3.5)

Every subsequent operator is evaluated in these new roots.
Products in the formulas below are typed intertwiners from the
final module to the initial one, written in traversal order.

## 4. The strict tetrahedral three-to-two identity

Start with nonzero z_i,s_i and coefficient tags u,v. Put

    A=u^N z_1^N s_1^N/s_2^N,
    B=v^N z_2^N s_2^N/s_3^N,
    a^N=1+A, b^N=1+B, h^N=1+A+AB.               (4.1)

Use the root choices (a,h/a,ab/h) for the left three steps and
(b,h) for the right two steps. Then, on the component anchored
at u=v=0 and a=b=h=gamma_i=1,

    T_12(u;a) T_13(uv;h/a) T_23(v;ab/h)
       =T_23(v;b) T_12(u;h).                    (4.2)

Substitution in (3.5) gives the same final roots on both paths:

    z_final=(z_1 z_2 z_3, z_2 z_3/h, z_3/b),
    s_final=(s_1/h, s_2 h/(s_1 b), s_3 b/s_2).   (4.3)

The rational conjugations agree by the generic tagged tetrahedral
pentagon, whose proof uses only the compact pentagon and (3.2).
After clearing the norm divisors, it specializes exactly as in
Section 2. Both products in (4.2) therefore intertwine the same
full three-pair matrix algebra, and their ratio is scalar.
Each normalized atom has determinant one on the N^3-dimensional
module. The determinant ratio of the shear words is one by
(3.2). Thus this scalar has N^3-th power one. At u=v=0 all atoms
are I and the bare shear words agree by (3.2). Algebraic
root-of-unity rigidity on the anchored component fixes the scalar
to one. This proves (4.2) for even and composite N as well.

For raw inverse atoms retain the scalar lambda_raw. If F_Li,F_Ri
are their cycle determinants from (1.1), the exact equation is

    lambda_raw^(N^3)
      =[F_R1 F_R2/(F_L1 F_L2 F_L3)]^(N^2).       (4.4)

The diagnostic also finds the stronger Nth-power version of
(4.4) in its samples. That strengthening is not needed or asserted
as a uniform theorem here.

## 5. What an external selected evaluation inherits

Let two specified finite tensor presentations differ by (4.2),
with the same exterior maps. After identifying their boundary
frames as in (4.3), the resulting full external operators are
equal. Every transported vector/covector contraction is equal,
including the zero contraction. This is an exact local period
transport statement, not just equality of unpointed modules.

The [four-atom formula](four_cyclic_atoms.md) uses these same
finite literature atoms. Its already specified braid contraction
can therefore use this move wherever the typed internal and
boundary identifications are supplied. The Cartan, determinant,
carry, peripheral and source factors are retained by those
identifications. Arbitrary new source vectors are not allowed.

An uncolored ideal triangulation does not supply all these tensor
leg, face, turn, source and cut identifications. Nor does (4.2)
move a fixed reducible root character to the hyperbolic one.
The next [triangulation comparison criterion](triangulation_regulator_bridge.md#8-the-precise-remaining-use-of-the-ideal-triangulation-theorem)
spells out the additional relative comparison and its obstruction.

The subsequent [controlled cyclic Euler-source calculation](controlled_cyclic_euler_source.md)
extends the anchored primitive identity to a free formal central
order through its nilpotent source. It computes the complete first
mixed jet, including the required UV corner term. The completion
agrees there with the actual R Euler polynomial. An exact reflected
factorial-vector comparison transports its source and co-source,
and its scalar is polynomially bounded on marked compact charts.
This does not equate arbitrary root lifts, construct an uncolored
geometric tensor assignment, or identify the global knot period.

## 6. The classical five-term check and its limitation

Let D_B denote the Bloch--Wigner dilogarithm. The arguments (2.3)
satisfy exactly

    D_B(V)+D_B((1-V)U)
      =D_B(U)+D_B(-UV/(1-U))+D_B(V/H).            (6.1)

To verify it, use the ordinary five-term identity at x=U,
y=V/H. Its three resulting arguments are UV/H, U(1-V), V.
Finally D_B(z/(z-1))=-D_B(z), with
z=UV/H and z/(z-1)=-UV/(1-U), gives (6.1).
This also explicitly checks the changing central arguments;
using frozen arguments would lose the relation.

Every nondegenerate ordinary five-term move preserves the total
regulator. In particular it cannot carry a zero-regulator central
cycle to a positive hyperbolic fundamental cycle. This is why a
strict root pentagon is local input for the selected-period
comparison, rather than that comparison itself.

## 7. Coverage and exact checks

Root-cyclic dilogarithm pentagons and Heisenberg-double tetrahedral
operators are existing structures. The literature definitions and
coverage are recorded in the linked four-atom and Verma notes;
no novelty or published coherence proof is assumed here. The
argument above reconstructs the root transport, scalar and frame
in the actual conventions of these notes.

[The exact audit](../experiments/audit_cyclic_tetrahedron_pentagon.py)
checks nine primitive cyclic pentagons at N=2,3,4,5,6,8,9,10,12
and five full N^3-dimensional tetrahedral identities at N=2,...,6.
It checks all five shear maps, the final clock/shift roots, the
bare permutation identity, projective matrix equality and the
recorded raw determinant equations.  The normalized
phase is fixed by the uniform anchored proof, rather than by
unrelated finite-field choices of gamma roots.
[Results](../experiments/cyclic_tetrahedron_pentagon_results.json).

    python3 experiments/audit_cyclic_tetrahedron_pentagon.py

The four-atom audit was also rerun after generalizing the cycle
helper to arbitrary spectator multiplicity: all 18 crossings
and 72 atom intertwiners pass. These checks do not establish the
global selected-source or regulator-norm theorem.
