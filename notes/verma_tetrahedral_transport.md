# Pointed tetrahedral transport of the Verma root period

Research note, 26 October 2026. This factors the actual untruncated
Verma crossing into four compact quantum dilogarithms, derives a
scalar-one algebraic tetrahedral pentagon, and proves that finite
formal pentagon rewrites preserve its selected root period after
compression to the Verma lattice. It retains the boundary frame,
its entire norm character and its poles. Individual compact
products are not evaluated at roots of unity.

The resulting root period is still the one independently identified
in the [Frobenius Verma note](frobenius_verma_period.md):

    V_N(M)=F_N(M)/Delta_K(M^(2N)).

This supplies local operator moves for the proposed triangulation
comparison. It does not establish that an arbitrary positive
geometric triangulation carries the required colored network and
pointing, or identify its selected quantum period with the Bloch
regulator. The volume conjecture remains unproved.

## 1. A pointed compact pentagon

For generic Q put

    P_Q(t)=(t;Q)_infinity
      =sum_(n>=0)(-1)^n Q^(n(n-1)/2)t^n/(Q;Q)_n.

Use it as a formal series. Its constant term is one and
P_Q(Qt)=P_Q(t)/(1-t). If AB=QBA, Gaussian expansion gives

    P_Q(A+B)=P_Q(A)P_Q(B).                         (1.1)

For XY=QYX, conjugation by P_Q(Y) sends X to
X(1-Q^(-1)Y)=X-YX. The two summands X and -YX satisfy the
commutation required in (1.1). Consequently

    P_Q(Y)P_Q(X)=P_Q(X)P_Q(-YX)P_Q(Y).            (1.2)

This proves the pentagon directly from the series and its shift
equation. It is an equality with scalar one, fixed by the constant
term. The ordered middle argument -YX, including its Q phase in
an X-before-Y monomial basis, is part of the identity.

To make completions unambiguous, attach formal variables u,v to
X,Y. The middle argument has tag uv. Every coefficient is finite
in the (u,v)-adic completion of the quantum Laurent algebra.
Inverses of P are defined in the same completion. No analytic
branch or root-level value of an individual infinite product is
assumed.

## 2. A tetrahedral operator, including its shear and phase

On Laurent monomials in z_1,...,z_b let Z_i multiply by z_i and
S_i f(z)=f(...,Qz_i,...). Put x_i=Z_i, y_i=S_i^(-1), so
x_i y_i=Q y_i x_i. Define a monomial shear

    (C_ij f)(z)=f(...,z_i z_j,...,z_j,...),
    a_ij=-Q x_i x_j^(-1)y_j,
    T_ij(t)=C_ij P_Q(t a_ij)^(-1).                 (2.1)

The shear conjugates x_i to x_i x_j and y_j to y_i^(-1)y_j.
Its exact monomial action gives
C_12 C_13 C_23=C_23 C_12. Move the dilogarithms past these
shears in the two products below. On the left their arguments
become A,-AC,C; on the right they become C,A, where

    A=u a_12, C=v a_23, CA=QAC.

Indeed the transformed a_13 has coefficient -Q uv, whereas
AC has coefficient Q uv. Inverting (1.2) therefore proves

    T_12(u)T_13(uv)T_23(v)=T_23(v)T_12(u).        (2.2)

This is the algebraic three-to-two tetrahedral operator identity
with its exact shear and scalar. It is not a claim that the
uncolored geometric triangulation theorem supplies the extra
tensor data needed to apply it globally.

For a direct coefficient check, T_ij(t) sends a Laurent monomial
of exponent vector n to vectors with

    n'_i=n_i+m, n'_j=n_j+n_i,
    coefficient=t^m(-1)^m Q^(m(m+1)/2-m n_j)/(Q;Q)_m,

summed over m>=0. Tagged coefficients are finite. Omitting the
Q in a_ij already violates (2.2); it is not a removable scalar
normalization.

## 3. Four factors for the actual Verma crossing

Use the same infinite Verma basis v_a=z^a, x=q^alpha, Q=q^2,
rho=q-q^(-1). On one factor put S v_a=Q^a v_a and Z v_a=v_(a+1).
Then

    K=xS^(-1), F=Z,
    rho^2 E=qx Z^(-1)(1-S^(-1))(1-Q^(-1)x^(-2)S).

The right side kills v_0 and preserves the polynomial Verma module.
Let G=P_Q(x^(-2)S), initially as a tagged formal diagonal operator.
The functional equation gives

    rho^2 E=qx G[Z^(-1)(1-S^(-1))]G^(-1).         (3.1)

For a pair set A=Z_1^(-1)Z_2, S=S_1 and

    W=x^(-2)S, U=Qx A, V=-Qx A S^(-1).

Here AS=QSA and VU=QUV. The formal universal uncheck R, with
its common Cartan scalar removed, is D times its nilpotent series,
where

    D(v_a tensor v_b)=x^(-a-b)Q^(ab)v_a tensor v_b.

Using the independently derived R coefficients and (3.1) gives

    R^0=D P_Q(W)P_Q(V)P_Q(U)P_Q(W)^(-1).          (3.2)

Indeed the middle product is P_Q(U+V), with U+V=Qx A(1-S^(-1));
its action terminates on each polynomial input before the diagonal
conjugation. Equation (3.2) is therefore the actual Verma operator,
not a replacement cyclic crossing.

Two applications of (1.2) remove the diagonal G:

    P_Q(W)P_Q(V)=P_Q(V)P_Q(-WV)P_Q(W),
    P_Q(W)P_Q(U)P_Q(W)^(-1)=P_Q(U)P_Q(-WU).

Since -WV=x^(-1)A and -WU=-x^(-1)AS, the four-monomial formula is

    R^0=D P_Q(-Qx AS^(-1))P_Q(x^(-1)A)
                    P_Q(Qx A)P_Q(-x^(-1)AS).      (3.3)

The checked crossing is the usual flip times (3.3). Its inverse
is the inverse word, with the same external conventions. All
Cartan, flip and zero-framing factors remain in the period.

## 4. Compression fixes the boundary lattice

The individual factors in (3.3) can send a polynomial input to
infinitely many negative powers of z_1. The complete product has
an elementary cancellation. Introduce a color tag h and a transfer
tag d in (3.2): replace W by hW and U,V by dU,dV. In (3.3) this
tags the second and fourth arguments by hd, and the first and
third by d.

After grouping the whole product, the coefficient sending
(a,b) to (a-n,b+n), before the checked flip, is exactly

    d^n x^(-a-b+n)Q^((a-n)b){a choose n}_Q
                       (h x^(-2)Q^(a-n);Q)_n, 0<=n<=a,       (4.1)

and is zero for n>a. Here the Gaussian coefficient is a
polynomial, not a divided-factorial value at a root.

For a uniform proof, first expand P_Q(d(U+V)). Its n-th power
acts by the factor product_(j=0)^(n-1)(1-Q^(-a+j)), which
vanishes for n>a. Combining this factor with the Euler coefficient
gives d^n x^n Q^(-n(a-n)){a choose n}_Q. The diagonal ratio from
G is (h x^(-2)Q^(a-n);Q)_n. Applying D at the output gives
(4.1). This is also the direct untruncated crossing coefficient
of the preceding note at h=d=1.

Every fixed homogeneous total-index sector of the combined
operator is thus a finite matrix of Laurent polynomials in q,x
and polynomials in h,d. The inverse has the same property, by
the terminating inverse R series. Its determinant is the invertible
Cartan monomial times that of a unipotent triangular matrix.
The combined operator preserves the original polynomial Verma
lattice. Neither this fact nor its root specialization is obtained
by specializing its four compact factors separately.

## 5. A precise pointed transport theorem

Start with the Verma braid operator and a fixed cut, pivot and
grading insertion as in the [graded trace construction](frobenius_verma_period.md).
Expand its crossings and inverses by (3.2) or (3.3), with independent
auxiliary tags for the occurrences. Permit a finite sequence of
the formal pentagon identities, their inverse identities, exact
monomial/shear identities and cancellations of adjacent inverse
factors, with their argument tags and external leg identifications
transported throughout. These are equalities of the external
operator, before taking its trace.

Then compress the entire rewritten operator to the original Verma
lattice, set its tags to one, and specialize q=q_N. The resulting
graded cut period and its rational continuation at tau=1 are
exactly the original ones:

    rewritten V_beta(q_N,x;tau)=V_beta(q_N,x;tau),
    rewritten V_N(M)=F_N(M)/Delta_K(M^(2N)).       (5.1)

Here is the proof, including the otherwise missing specialization
step. All factors have positive auxiliary tag degree, so every
rewrite is defined in a common formal completion of the Laurent
module. The initial complete operator has the polynomial matrix
entries of Section 4. Formal operator equality forces the
rewritten complete entries to equal those polynomials, including
the vanishing of every forbidden negative-index transfer. Thus
setting the tags to one and specializing q use a known regular
polynomial entry. No root limit of an individual factor is used.

Each coefficient of the cut grading tau sums only finitely many
input and intermediate indices after this compression. The
coefficientwise period identity follows. At a root the initial
period has the rational formula proved in the preceding note.
Two rational functions with the same series at tau=0 are equal;
hence their entire rational continuations, poles and regular
whole specializations agree. This proves (5.1), including the
Kashaev fiber and its marked normal coordinate. Multiplying by
the full d_N(M) retains the full ADO normalization as before.

This theorem transports the actual selected period under the
specified formal operator moves. It does not assert that every
Pachner or face-permutation operation on arbitrary ideal
triangulations has already been assigned such an operator identity.
For such an application the coloring, polarization, turns and
boundary identifications must be constructed and checked.

## 6. The relative norm torsor at the Kashaev boundary

Normalize the diagonal operator in (3.2) on v_0. Its finite ratio is

    g_a=P_Q(x^(-2)Q^a)/P_Q(x^(-2))
                  =1/(x^(-2);Q)_a, g_0=1.

The finite expression specifies its meromorphic root frame even
though the two infinite products individually have no such value.
For q=q_N and U=M^(2N)=x^(2N),

    g_(a+1)/g_a=(1-x^(-2)Q^a)^(-1),
    g_(NA+r)=(1-U^(-1))^(-A)g_r, 0<=r<N.          (6.1)

This is an explicit rank-one cyclic norm character

    Norm((1-x^(-2)Q^a)^(-1))=(1-U^(-1))^(-1).

It is invertible away from its divisor; at U=1 its meromorphic
filtered lattice, with pole order A on the A-th polynomial block,
must be retained. Every finite total-index filtration has finite
pole order. At the actual Kashaev color x=q_N^(N-1), x^(-2)=Q,
so the first N frame entries are

    g_r=1/(Q;Q)_r, 0<=r<N.

They are exactly the factorial frame of the already fixed
[actual cut boundary](marked_braid_holonomy.md). The next entry
has a pole. The combined crossing is regular nevertheless by
(4.1), and the complete rational trace is regular there because
Delta_K(1)=1. Evaluating this diagonal frame separately at its
pole would lose the prescribed boundary data.

The middle arguments in pentagons also retain nontrivial central
norms. If XY=QYX and Q has order N, direct ordered multiplication
gives

    (-YX)^N=-X^N Y^N                              (6.2)

at every parity. Thus its binomial norm factor is 1+X^N Y^N,
which can specialize to a numerical multiplier. In the tetrahedral
operator (2.1), a_ij^N=-Z_i^N Z_j^(-N)S_j^(-N), with the same
sign. Such factors must be carried as functions before a whole
boundary specialization. The strict formal identities above
do not justify discarding them or repair a different numerical
state model by fiat.

The subsequent [factorial source-torsor calculation](factorial_source_torsor.md)
identifies this frame directly with the literature cyclic primitive.
For h=Q^(-1)x^(-2), write p_a(h)=(Qh;Q)_a=nu^a phi_a(h),
nu^N=1-U^(-1). Then the exact Verma frame is

    g_a=1/p_a(h)=nu^(-a) phi_a(h)^(-1).

Its block pole character in (6.1) is the N-step transport of
this same singular cyclic frame. The new two-direction affine
extension and cut-root adapters retain its source channel and
the full endpoint factors. They do not supply the remaining
global colored/polarized network or its selected regulator norm.

The subsequent [four cyclic-atom proof](four_cyclic_atoms.md)
now constructs a finite root counterpart for the genuine
semicyclic crossing: each atom is the literature alternate
cyclic dilogarithm, acting between explicitly transported
centers. Two independent Fermat norm roots and their inverses
restore the external clocks. Their determinant normalization,
an external root and the actual source anchor fix the whole
crossing scalar. This is not a termwise evaluation of (3.3);
the finite cyclic atoms include the required center transport
and boundary frame. Recombination has exactly the original
regular crossing and full cut period.

The subsequent [root tetrahedral pentagon](cyclic_tetrahedron_pentagon.md)
constructs the corresponding finite cyclic move with monomial
shears and changing centers. Compatible roots give the same
final clock/shift frame on both paths; a determinant and formal
zero-tag anchor fix the scalar to one on the stated lifted
component. This supplies an exact root move for specified
exterior contractions, rather than a separate specialization
of the compact infinite factors. The global geometric tensor
presentation and selected regulator norm are still missing.

## 7. Role in the regulator comparison

There are now actual four-factor crossing data, an algebraic
tetrahedral pentagon and a pointed root-period transport theorem
for finite formal operator rewrites. The cyclic norm character
and its relative lattice are explicit. These are local algebraic
inputs for a triangulation presentation of the source period.

The positive geometric triangulation supplies the marked classical
Bloch fundamental class, as already audited. To apply Section 5
to it requires a compatible colored/polarized tensor presentation
and a move transport of the cut and its relative gluing data.
Existence of positive tetrahedra alone does not supply that
presentation or a global branching. Nor does the operator move
identity show that a chosen hyperbolic character contribution
is the selected quantum period or has its regulator norm.
The original distinction between root-central and semiclassical
shape coordinates remains in force.

In particular (5.1) preserves the actual state and its source;
it does not equate its abelian interior root character with the
different fixed hyperbolic character separated in the
[threading note](ado_threaded_shadow.md). The needed comparison
remains a relative marked-period theorem. Its norm statement
and the volume conjecture are not proved here.

The subsequent [pointed tetrahedron gluing construction](pointed_tetrahedron_gluing.md)
does resolve local order coherence and nonvanishing at the root
module level. Integral edge primitivity gives a nonzero saturated
rank-N boundary block for S^3 knots at all N. It also specifies
the projected tetrahedron generator, without proving that vector
nonzero or identifying it with the selected relative Verma trace.
The full tensor-face presentation and marked regulator norm are
still additional comparisons.

## 8. Coverage and exact diagnostics

[Kashaev, q-alg/9503005](https://arxiv.org/abs/q-alg/9503005)
already covers a canonical Heisenberg-double pentagon and
reconstruction of Yang--Baxter solutions. The abstract of
[Suzuki, 1612.08262](https://arxiv.org/abs/1612.08262) covers a
Heisenberg-double construction on colored ideal triangulations
and colored moves. These are coverage of the framework, not
proof premises or an unrestricted geometric-triangulation
comparison. The earlier consulted
[four-dilogarithm holonomy-R coverage](https://arxiv.org/abs/2509.02354)
also prevents a novelty claim for the general factorization idea.
The formulas and polynomial-specialization proof above are
reconstructed directly in the fixed actual Verma conventions.

[The audit](../experiments/audit_verma_tetrahedral_transport.py)
checks the compact pentagon symbolically, the tagged tetrahedral
operator on Laurent monomials, forbidden-transfer cancellations
in the four-factor product, root-specialized compressed entries
and their actual ADO restrictions, the full meromorphic frame,
and the period through the grading using independent finite ADO
and classical Burau data. See
[the results](../experiments/verma_tetrahedral_transport_results.json).
These diagnostics verify the stated constructions and not the
remaining global geometric or regulator-norm theorem.

The saved checks include 28 symbolic compact-pentagon coefficients,
81 Laurent inputs and 1,215 coefficients for the tagged tetrahedral
operator, 49 symbolic four-factor compressions with 21 forbidden
transfers canceled, 3,360 compressed root entries, nine full pole
lattice levels through 12, and 210 graded coefficients in 30
transported trace cases. Even and composite levels and the exact
Kashaev boundary are included.
