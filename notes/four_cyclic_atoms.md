# Four literature cyclic-dilogarithm atoms for the actual crossing

Research note, 26 October 2026. This gives an exact root-level
factorization of the genuine semicyclic holonomy crossing into four
literature cyclic quantum dilogarithms. Each atom transports its center;
their determinant normalizations and external root factor are explicit.
An anchored scalar-rigidity argument fixes the remaining phase. The
factorization holds at every N, including even and composite levels.

The object being factorized is the actual crossing already identified
in [the semicyclic braid proof](semicyclic_carry_braiding.md). Its
nilpotent boundary, cut period, pivot, twist and full ADO normalization
are retained. This does not assign all colored face/turn data to an
arbitrary positive geometric triangulation or prove its selected norm.

## 1. The literature atom, including its determinant

Fix q=exp(pi*i/N), Q=q^2 and N>=2. On a split quantum torus let a
primitive monomial m have m^N=w. Choose roots

    mu^N=w, nu^N=1-w, mu nu !=0.

For its eigenvalues mu Q^j define the pointed cyclic function

    f_0=1, f_j=nu^j/(mu;Q)_j, 0<=j<N.             (1.1)

Its cyclic recurrence is f_(j+1)/f_j=nu/(1-mu Q^j).
The last step is the identity (mu;Q)_N=1-mu^N=nu^N.
Spectral idempotents define the matrix C=f(m) without choosing
an analytic infinite product. If m acts on an N^2-dimensional
two-pair torus, each eigenvalue occurs N times. Put

    F=product_(j=0)^(N-1) f_j,
    gamma^N=F^(-1), gamma=1 at mu=0,
    D_atom=gamma C.                                (1.2)

Then det C=F^N and det D_atom=1. For a general number of
spectator pairs the same normalization works by multiplicity.

This is exactly the standard alternate cyclic-dilogarithm definition

    mathfrak_d_N(z;Q)=(1-z^N)^((N-1)/(2N))
                        product_(ell=1)^(N-1)(1-Q^ell z)^(-ell/N).
                                                               (1.3)

Indeed, writing D_N(z)=product_(ell=1)^(N-1)(1-Q^ell z)^(ell/N),
finite cancellation gives

    F=nu^(-N(N-1)/2) D_N(mu)^N,
    gamma=nu^((N-1)/2)/D_N(mu),
    gamma f_j=mathfrak_d_N(mu Q^j;Q).              (1.4)

Compatible roots are part of the formulas. Include the square roots
required by half powers when N is even; no inverse of two modulo N
is used. Definition (1.3) is the literature cyclic dilogarithm, not
the full ADO dimension d_N(M), which remains a different function.

## 2. An atom is an intertwiner between changing centers

Suppose m A=Q^k A m, k integral. Formal compact conjugation has
the rational expression

    r_m(A)=A product_(ell=0)^(k-1)(1-Q^ell m)^(-1), k>0,
    r_m(A)=A product_(ell=k)^(-1)(1-Q^ell m),       k<0.         (2.1)

The value at k=0 is A. These are finite expressions; after
inverting 1-w every factor is invertible at the root.
The Nth central power changes by (1-w)^(-k).

In the splitting frame take A'=nu^(-k) A. The recurrence (1.1)
gives exactly

    r_m(A) C=C A',  r_m(A) D_atom=D_atom A'.         (2.2)

This proves the atom comparison directly, including composite
levels. In particular the atom is not evaluated repeatedly in
one frozen central representation.

## 3. The four monomials and the two independent norm factors

Use two uniform clock/shift pairs

    S_i e_a=s_i Q^a e_a, Z_i e_a=z_i e_(a+1),
    S_i Z_i=Q Z_i S_i.

Start with s_1=s_2=1, source roots z_1,z_2 nonzero, and put

    x=q^alpha, k=x^N, a=z_2/z_1, r=a^N=phi_2/phi_1.

The quantum-group embedding is the previously proved one

    F_i=Z_i, K_i=x S_i^(-1),
    rho^2 E_i=qx Z_i^(-1)(1-S_i^(-1))
                                   (1-Q^(-1)x^(-2)S_i),
    rho=q-q^(-1).

Thus E_i^N=0 initially and phi_i=z_i^N. The compact four-factor
identity of [the Verma proof](verma_tetrahedral_transport.md) has
the ordered monomials

    m_1=-Qx A S_1^(-1), m_2=x^(-1)A,
    m_3=Qx A,          m_4=-x^(-1)A S_1,
    A=Z_1^(-1)Z_2.                                 (3.1)

Their coefficients, order and q phase are retained. Define

    Delta_1=1+kr,
    Delta_2=1-r/[k(1+kr)],
    nu_1^N=Delta_1, nu_2^N=Delta_2,
    nu_3=nu_1^(-1), nu_4=nu_2^(-1).                (3.2)

Assume these factors are nonzero. They are full functions,
not constants selected after peripheral evaluation.

The root Cartan map first changes z_1,z_2 to z_1/x,z_2/x,
leaving s_1=s_2=1. Its matrix is

    C_cartan e_(i,j)=Q^(ij)e_(i,j).                 (3.3)

For each subsequent atom m=c A S_1^b, the commutation integers
with (S_1,S_2,Z_1,Z_2) are (1,-1,b,0). By (2.2) its target
roots are

    (s_1,s_2,z_1,z_2)
       -> (s_1/nu,s_2 nu,z_1/nu^b,z_2).             (3.4)

Evaluate m_i in the frame reached before that atom. Compatible
spectral roots and norm factors are

| Atom | Spectral root mu_i | nu_i^N |
| --- | --- | --- |
| 1 | q x a | Delta_1 |
| 2 | a/(x nu_1) | Delta_2 |
| 3 | Q x a/nu_1 | Delta_1^(-1) |
| 4 | q a/(x nu_1 nu_2) | Delta_2^(-1) |

The negative monomial signs are accounted for by q^N=-1 and
(A S_1^b)^N=(-1)^(b(N-1)) A^N S_1^(bN). Multiplication verifies
mu_i^N+nu_i^N=1 in every row, at every parity.

For completeness the successive clock-center product factors are

    Delta_1, Delta_2, Delta_1^(-1), Delta_2^(-1).

They restore both clock roots exactly with the compatible choices
in (3.2). The final shift roots are

    z'_1=z_1 nu_1 nu_2/x, z'_2=z_2/x.              (3.5)

Their powers are precisely the genuine holonomy targets:

    phi'_1=phi_1/k+(1-k^(-2))phi_2,
    phi'_2=phi_2/k.

Here Delta_1 Delta_2=1+kr-r/k. This is a direct center
calculation for the complete four-factor word.

## 4. The exact normalized crossing formula

Let D_i be (1.2)--(1.3) for atom i in its transported frame.
Let B_src and B_tar be the changes from the standard F-circle
bases to the uniform clock/shift bases:

    B_src e_(i,j)=z_1^i z_2^j e_(i,j),
    B_tar e_(i,j)=(z'_1)^i(z'_2)^j e_(i,j).

These are the actual monomial frame changes: v_a=z_i^a e_a
has F v_a=v_(a+1), with wrap phi_i. On the root cover anchored
by nu_1=nu_2=gamma_i=1 at a=0, the uncheck crossing is exactly

    R^0=(nu_1 nu_2)^(-(N-1)/2)
         B_src^(-1) C_cartan D_1 D_2 D_3 D_4 B_tar.           (4.1)

Products have their displayed order and changing-frame meaning.
The inverse gives the negative crossing, with its centers and
all roots transported as in the genuine braid theorem.

Here is a proof of the scalar, rather than an unspecified projective
factorization. Conjugating the generic compact four-factor identity
gives a rational quantum-torus identity. The proof in the linked
Verma note is a formal algebra identity before root specialization.
Its rational conjugations have finite expressions (2.1), so
clearing the indicated denominators specializes that identity
at every root. Equations (2.2)--(3.5) then show that the right
side of (4.1) and the genuine semicyclic R^0 intertwine the same
full matrix algebra with the same central data and Casimirs.
They differ by a scalar lambda on the generic regular chart.

Each D_i has determinant one on the N^2-dimensional pair.
The exact remaining determinants are

    det C_cartan=Q^((N(N-1)/2)^2),
    det B_tar/det B_src=(nu_1 nu_2/x^2)^(N^2(N-1)/2),
    det R^0=x^(-N^2(N-1))Q^((N(N-1)/2)^2).

The external factor in (4.1) cancels the entire extra determinant.
Thus

    lambda^(N^2)=1.                                (4.2)

This does not by itself discard lambda. Use the formal source
anchor a=0: the matrices m_i/mu_i extend there, f_j=1,
D_i=identity, and all specified norm roots equal one. The
zeroth coordinate of the right side applied to v_00 has a
regular value one. This coordinate does not involve an inverse
singular frame entry, since (B_src)_00=(B_tar)_00=1.
The genuine crossing fixes v_00. Therefore lambda has value
one at this formal anchor. A root-of-unity-valued algebraic
function is constant on the irreducible anchored component,
so lambda=1. This proves (4.1) with its phase fixed.

Other lifted components retain their phases; the theorem does
not identify independent choices of normalization roots.

## 5. The raw scalar is explicit and must be retained

If raw pointed C_i rather than the literature D_i are used,
write R_raw=B_src^(-1)C_cartan C_1 C_2 C_3 C_4 B_tar.
Then R_raw=lambda_raw R^0, with

    lambda_raw^(N^2)
      =(nu_1 nu_2)^(N^2(N-1)/2) product_i F_i^N.    (5.1)

The complete formula and branch on the anchored cover are
equivalently fixed by (4.1) and gamma_i^N=F_i^(-1).
Thus determinants control a real normalization line, with
its root phase selected by the actual pointing. They are
not permission to throw away an arbitrary scalar period.

The external root in (4.1) also remains necessary even though
the four atom norm factors multiply to one. At fixed nonzero
Delta_1,Delta_2 its log-modulus is

    -(N-1)/(2N) log|Delta_1 Delta_2|.

This is bounded across N under that fixed-central specialization.
No bound for an unrecorded moving-center specialization or
the entire selected knot period is inferred.

## 6. Peripheral functions that become numerical multipliers

For a positive checked crossing on the common fixed line of
the genuine braid theorem, its uncheck source pair is swapped.
Hence its ratio r is k. Write U=k^2=M^(2N), retaining the
actual sign k=(-1)^(N-1)M^N. Equations (3.2) give

    Delta_1=1+U, Delta_2=U/(1+U),
    Delta_3=1/(1+U), Delta_4=(1+U)/U.               (6.1)

At M=1 these specialize to 2,1/2,1/2,2. They must be
transported as the functions in (6.1), including their
compatible roots and the external product whose Nth power
is U. This is a concrete occurrence of the peripheral
factors the user asked us to retain. It does not by itself
repair the earlier positive scalar model's failed move.

The scalar, Cartan frame and source normalization of the
actual crossing are now accounted for before any such
evaluation. Taking absolute values of individual atom
entries would still change the quantum contraction.

There is also an exact framing norm check on this fixed line.
Let beta_ext=(nu_1 nu_2)^(-(N-1)/2) be the external factor
in (4.1), and theta_0=x^(1-N) the actual residual twist.
Since (nu_1 nu_2)^N=U=x^(2N),

    (beta_ext/theta_0)^(2N)=1.                     (6.2)

Their moduli therefore cancel exactly in a zero-framed braid
evaluation. The remaining phase is part of the specified root
cover and pointing; it is not discarded. This checks the
normalization of the tetrahedral presentation against the
actual framing, rather than adding a free global multiplier.

## 7. Boundary specialization and scope of the comparison

After recombination the operator (4.1) is exactly the polynomial
semicyclic crossing. Its nilpotent boundary phi_1=phi_2=0
therefore has the original regular value, even though
individual atom expressions or uniform frames can be singular.
Use the complete identity or its transported lattice for that
specialization. The common carry theorem and its bounded
normal jets describe the integral recoupling source; the
cut operator remains F_N(M)I and the full ADO factor is unchanged.

We have consequently identified actual finite root crossings,
their genuine braid maps and selected source with explicit
literature cyclic tetrahedron atoms, including scalar roots
and an external frame. This is a local operator factorization
that can be substituted into any already specified finite
braid contraction, transporting every paired and boundary leg.

It does not prove that arbitrary face turns or all colored
Pachner presentations of a positive geometric knot triangulation
carry that same relative source and evaluation. The external
semicyclic character is still reducible, and fixed root centers
still differ from fixed semiclassical shape coordinates.
The geometric A-operator/source identification and the selected
Bloch-regulator norm across levels remain unproved.

There is a concrete check on the distinction just made. At the
complete point on the fixed semicyclic center line, (6.1) gives
the four central shapes

    (-1, 1/2, 1/2, -1).

Their Bloch--Wigner regulators are all zero because they are
real. Thus that fixed-center Bloch sum is not the nonzero
hyperbolic fundamental-class regulator. This does not compute
the selected quantum period's growth; it shows why a local
factorization and matching central equations alone cannot
replace the remaining source/cycle and parameter comparison.

The subsequent [root tetrahedral pentagon](cyclic_tetrahedron_pentagon.md)
now supplies a strict local three-to-two identity for these same
finite atoms on a compatible anchored cover. It includes the
monomial shears, their changing splitting frames, and all norm
and determinant roots. Thus specified exterior contractions
can transport this local move exactly. It does not supply the
entire geometric tensor presentation. Ordinary five-term
transport preserves the zero regulator of the fixed central
cycle just computed, so the geometric comparison must still
retain the relative source and its selected realization.

## 8. Definitions, coverage and exact diagnostics

Formula (1.3) is the alternate cyclic-dilogarithm definition
displayed with Definition 3.3 in
[Ip--Yamazaki, 1412.5777](https://arxiv.org/abs/1412.5777).
Only its definition is used; (1.1)--(1.4) prove the needed
functional and determinant identities directly. The abstract
of [McPhail-Snyder--Reshetikhin, 2509.02354v2](https://arxiv.org/abs/2509.02354v2)
already covers a four-dilogarithm holonomy factorization.
No novelty or independent global invariant is claimed. No
published factorization or coherence proof is a premise above.

[The exact audit](../experiments/audit_four_cyclic_atoms.py)
constructs all transported clock/shift modules, cyclic
spectral matrices, and central roots over finite fields.
It checks 18 crossings at generic and Kashaev colors for
N=2,3,4,5,6,8,9,10,12. All 72 atom intertwiners satisfy
their four generator equations. It independently compares
the complete raw product with the actual semicyclic crossing,
records its nonzero scalar, and verifies the exact determinant
identity (5.1). It checks both restored clock roots and the
full final F central powers. Normalization phases in (4.1)
are fixed by the uniform anchored argument, rather than
unrelated numerical choices of roots. All checks passed.
Results: [four_cyclic_atoms_results.json](../experiments/four_cyclic_atoms_results.json).

    python3 experiments/audit_four_cyclic_atoms.py
