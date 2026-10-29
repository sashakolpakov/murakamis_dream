# The complete quantum period as a marked fibre after ramified Weyl descent

Research note, 26 October 2026. The complete Kashaev value, previously
written as a first normal derivative, is an ordinary linear evaluation
on a specified descended lattice. This is an exact algebraic construction
at each level, with the first-order information retained in the lattice.
It is not an asymptotic argument or an identification with the Bloch
regulator. A comparison that fixes only the ordinary root fibre can
still change the period; an explicit example below exhibits the missing
marking.

The input is the [actual Weyl theorem](actual_weyl_descent.md), including
the primitive normal operator's half-root and sign. The
[actual peripheral calculation](actual_peripheral_fusion.md) fixes its
boundary lattice. No different state or quantization is introduced.

## 1. The actual orbit and its two involutions

Fix N>=2, q=exp(pi*i/N), Q=q^2, Y=M^2, and the central coordinate
U=Y^N. The actual normal state is v_N(Y)=(Y-1)F_N(Y). At a regular
operator specialization write

    B=sum_j b_j(q,Y)T^j, T Y=QY T,
    B J=J' B,
    J=-Y R, J'=sigma*q^(dm)*Y^m*T^d R,
    R h(Y)=h(Y^(-1)), sigma in {1,-1}, m in Z.     (1.1)

These quantum symmetries are proved for the actual primitive minimal
normal operator. The state satisfies J v_N=v_N. All statements below
also apply to a specified nonminimal operator with the checked same
kind of intertwiner; their rank conclusions must be checked separately.

Near U=1 choose the algebraic roots

    Y_r(U)=Q^r U^(1/N), 0<=r<N, U^(1/N)|_(U=1)=1.

Let B_N(U) be the matrix acting on the orbit values. Its entries are

    (B_N(U))_(r,r+j)=b_j(q,Q^r U^(1/N)),          (1.2)

with coincident columns added modulo N. The quantum involutions on
orbit vectors act semilinearly over U->U^(-1):

    (J_U h)(U)=U^(1/N)*J_0*h(U^(-1)),
    (J'_U h)(U)=U^(m/N)*J'_0*h(U^(-1)),
    (J_0)_(r,-r)=-Q^r,
    (J'_0)_(r,-r-d)=sigma*q^(dm)*Q^(mr).          (1.3)

All indices are modulo N. Direct multiplication gives J_0^2=J'_0^2=I.
They are unitary in the orbit metric. This includes even levels;
the q^(dm) in the second involution has not been replaced by a
guessed Q-power.

The semilinear identity corresponding to (1.1) is

    B_N(U) U^(1/N) J_0
          =U^(m/N) J'_0 B_N(U^(-1)).             (1.4)

## 2. Linearizing the ramification, with explicit algebraic frames

Use the marked rational parameter

    z=(U-1)/(U+1), U=(1+z)/(1-z), s=z^2.

Then U inversion is exactly z->-z. The completed local rings are
R_z=C[[z]] and R_s=C[[s]]. Choose the units

    Gamma_in=U^(1/(2N)), Gamma_out=U^(m/(2N)),

both equal to one at z=0. They are algebraic roots, unramified there.
Thus the formal calculation may equally be performed on an etale
local algebraic cover with these specified roots. Set

    x_N=Gamma_in^(-1)*v_N,
    B_tilde=Gamma_out^(-1)*B_N*Gamma_in
           =U^((1-m)/(2N))*B_N.

Equations (1.3)--(1.4) become

    x_N(z)=J_0 x_N(-z),
    B_tilde(z)J_0=J'_0 B_tilde(-z).              (2.1)

This is an explicit linearization, rather than a presumed unramified
descent theorem. Write E_+,E_- for the two eigenspaces of J_0 and
E'_+,E'_- for those of J'_0.

## 3. The descended lattice retains the negative first coefficient

An invariant vector has a unique form

    x(z)=a(s)+z b(s), a(s) in R_s E_+,
                            b(s) in R_s E_-.

Consequently its invariant lattice is the free R_s-module

    Lambda_in=R_s E_+ direct-sum z R_s E_-.       (3.1)

The symbol z e_- is a generator of the second summand as an
R_s-module. Its class is nonzero in Lambda_in/s Lambda_in,
even though its value as a function at z=0 is zero. There is
the exact special-fibre sequence

    0 -> E_- -> Lambda_in/s Lambda_in -> E_+ -> 0. (3.2)

The last map records the ordinary value a(0); the kernel records
the coefficient b(0). Evaluating first at z=0 and then taking the
J_0 invariants retains only E_+ and discards that kernel. The two
operations are therefore different.

There is also an intrinsic filtration. The invariants of z times
the original lattice are

    F_(1/2)Lambda_in=s R_s E_+ direct-sum z R_s E_-.

Its special fibre is the subspace E_- in (3.2). This is the elementary
weight-one-half parabolic structure of the ramified double cover.
The output lattice is constructed identically using E'_+,E'_-.

### The descended actual operator

Use constant eigenframes for the four eigenspaces. Equation (2.1)
forces the exact block form

    B_tilde(z)=[ A(s)    z C(s) ]
               [ z D(s)    E(s) ].

Therefore its map on the invariant lattices is

    B_desc(s)=[ A(s)    s C(s) ]
              [ D(s)      E(s) ],
    B_desc(0)=[ A(0)       0  ]
              [ D(0)    E(0) ].                  (3.3)

The blocks may be rectangular; the total matrix is N by N. If
B_N(U)=B_0+(U-1)B_1+..., then

    B_tilde_z(0)=2B_1+(1-m)B_0/N.               (3.4)

Thus D(0) is its block from E_+ to E'_-. The negative block E(0)
is exactly B_0 restricted from E_- to E'_-, the operator previously
called B_-.

This construction is functorial. If an equivariant matrix G(z) has
the analogous blocks, its descended matrix is obtained by the same
replacement of z C by s C and z D by D. Substitution shows
(G_1 G_2)_desc=(G_1)_desc (G_2)_desc. In particular an invertible
equivariant lattice comparison descends to an invertible comparison
preserving the filtration in (3.2). This proves the needed elementary
descent directly.

## 4. The original Kashaev value is a special-fibre evaluation

For the actual state, let (a_0,b_0) be the class of x_N in the fibre
of (3.1). The ordinary part is already specified:

    a_0=v_0,
    (v_0)_r=(Q^r-1)C_r(q), 1<=r<N,
    (v_0)_0=0,
    (a_0)_1/(Q-1)=1.                             (4.1)

The last equality is the fixed ordinary-color anchor. It shows that
the actual section is primitive at the branch point; it has not been
multiplied by a vanishing central factor.

Let e_0 be the complete-coordinate vector. It lies in E_-. Since
dU/dz=2 at zero and Gamma_in,z(0)=1/N, differentiating the explicit
algebraic frame gives

    x_N,z(0)=2v_N,U(1)-v_0/N=b_0,
    K_N=F_N(1)=(N/2)*e_0^* b_0,
    N_N(1)=(eta_N/2)*e_0^* b_0, eta_N=i^(N+3).    (4.2)

The final equation is the complete full ADO period. Thus its value
is an ordinary linear functional on a specified algebraic fibre.
The derivative notation is no longer needed to evaluate it once
the descended lattice is retained. Its first-order data have not
been removed; they are the second summand in that fibre.

This statement uses no kernel-rank or sector-injectivity hypothesis.
It applies to the actual state for every knot and N. At fixed N,
the state, its frames, a(s), b(s), and this evaluation are algebraic.
Their presentations vary with N; this is not a fixed-degree
algebraic normalization across all levels or a growth bound.

### The affine source is a lifting equation in the same fibre

The actual equation descends to

    A(0)a_0=0, E(0)b_0=-D(0)a_0.                (4.3)

For this particular a_0, (3.4) and B_0 a_0=0 give
D(0)a_0=2B_1 a_0. Thus the second equation is exactly the preceding
normal-source equation, with its reflection sector built into the
algebraic fibre. Its set of lifts b_0, if nonempty, is an affine
torsor under ker E(0). The actual state supplies a point.

If E(0) is injective, this point and the period are determined by
the source alone. More generally the scalar is unique when e_0^*
annihilates ker E(0). These are the previous precise conditions;
ramified descent does not prove them automatically.

When the generic kernel over C((s)) is a line, its saturated
intersection with Lambda_in is a free rank-one R_s-module. The
actual section (4.1) generates it, because its anchor is a unit.
This supplies a pointed line whose fibre and (4.2) remain defined
even if B_desc(0) itself has an extra kernel. One must specialize
the saturated kernel lattice, rather than replace it by the
possibly larger kernel of the special matrix. Generic rank one
is an additional hypothesis for this operator-only description;
the actual state-defined line does not require it.

The subsequent [torsion initial-rank theorem](torsion_initial_rank.md)
supplies a finite sufficient condition for this generic line. A
rational-coefficient actual annihilator with exactly one occupied
binomial torsion curve in its initial form has generic rational
rank one at all sufficiently large levels, even with non-toric
remaining factors. Its primitive minimal actual right factor
inherits the rank. This is an operator certificate, not a claim
that every knot operator satisfies it; the special-sector rank
and marked regulator norm remain additional questions.

## 5. Identity on the ordinary fibre does not fix this marking

There is a sharp two-dimensional example. Use J_0=diag(1,-1),

    B_tilde(z)=[ 0  0 ], x(z)=(1,-z)^t.
               [ z  1 ]

Then B_tilde*x=0 and the equivariance (2.1) holds. The descended
operator is [[0,0],[1,1]], and the descended fibre vector is (1,-1).
Its second coordinate is the retained normal period.

For any c, the equivariant invertible frame change

    G(z)=[ 1   0 ], G(0)=I,
         [ cz  1 ]

descends to G_desc(0)=[[1,0],[c,1]]. It sends that fibre vector
to (1,c-1). Hence a frame change that is identity on the ordinary
root fibre, and preserves the lattice and its filtration, can
change the normal period by an arbitrary scalar. Transporting
the period functional along with G restores its value; omitting
that transport loses precisely the extra marking.

This is an algebraic example about comparisons, not a knot
counterexample. It shows why ordinary-fibre agreement or a
normalization of a determinant does not alone identify the
selected source period.

## 6. A parity obstruction to the optional injectivity condition

The dimensions of the domain sectors are

    dim E_-=(N+1)/2 if N is odd, N/2 if N is even,
    tr J_0=-1 if N is odd, 0 if N is even.

The range trace, including the full half-root, is exactly

    tr J'_0=sum_(0<=r<N, 2r+d=0 mod N)
                 sigma*(-1)^(m*(d+2r)/N).        (6.1)

Only fixed coordinates contribute to the trace, and q^N=-1
gives the displayed sign. Consequently E(0):E_->E'_- cannot
be injective whenever tr J'_0>tr J_0.

For even N this obstruction occurs precisely when d and m
are even and sigma=+1. For odd N>d, it occurs precisely when
sigma*(-1)^m=+1 for odd d, or sigma=+1 for even d. The general
formula (6.1) also covers the finitely many smaller levels.

These are diagnostics for the proposed first-order inversion,
not restrictions already proved for every primitive knot operator.
If the obstruction occurs, one must keep the saturated kernel
and the further source/lifting data; assuming sector injectivity
would be false for that signature.

## 7. Metric and the remaining regulator comparison

Choose orthonormal constant frames of E_+,E_-. Along |U|=1 the
specified Gamma_in is unitary. Orthogonality then gives exactly

    ||v_N(U)||^2=||a(s)||^2+|z|^2||b(s)||^2.      (7.1)

The regular metric on the descended fibre records the coefficients
as ||a_0||^2+||b_0||^2. This is a renormalization of the vanishing
negative-weight part; it is not the result of setting z=0 in
the original orbit norm. The Kashaev functional has norm N/2,
and the full ADO functional has norm 1/2. Neither gives a lower
bound on its overlap with the actual vector. The specified
functional remains essential.

The positive triangulation and
[actual classical action](quantum_longitude_and_regulator_action.md)
already supply the marked Bloch period with norm logarithm 2Vol/pi.
The quantum object to compare now has an explicit algebraic
special fibre, its filtration, ordinary anchor, and functional
(4.2). A geometric comparison must carry that marked source
period; matching only an unpointed module or its ordinary fibre
does not suffice. The target becomes

    (4/N)log|e_0^* b_0| -> 2Vol/pi,

equivalent to the original statement because e_0^*b_0=2K_N/N.
No such norm comparison or nonzero geometric contribution is proved
here. Ramified descent identifies the exact object to compare;
it does not establish its volume growth.

The subsequent [threaded-character theorem](ado_threaded_shadow.md)
also fixes interior data on this marked fibre. Every 2N-threaded
loop acts by two at U=1 on both a_0 and b_0, and null-homologous
loops act by two on the full family. A commutator separates this
character from fixed hyperbolic central data. An actual source
extension carrying a compatible separating observable can select
its horizontal source-one point by a spectral projector, without
a further rank assumption; the extension and its marked regulator
norm have not been constructed by that criterion alone.

## 8. Coverage and checks

The later [Frobenius Verma-period construction](frobenius_verma_period.md)
gives an explicit alternate root realization F_N/Delta_K(U), retaining
the entire Alexander factor. Reciprocity and Delta_K(1)=1 give
1/Delta_K(U)=1+O(z^2), z=(U-1)/(U+1). Consequently both marked
fiber coordinates a_0,b_0 and the complete period functional above
are unchanged. This is a specified central gauge, including its
polar divisor away from the complete fiber; it is not an arbitrary
normalization of the period.

This elementary ramified descent belongs to existing parabolic-bundle
theory. Coverage includes Borne,
[Fibres paraboliques et champ des racines](https://arxiv.org/abs/math/0604458),
and Biswas--Borne,
[Tamely ramified torsors and parabolic bundles](https://arxiv.org/abs/1706.06733).
Only their abstracts and scope were consulted; no descent or torsor
proof from either is used above, and no novelty claim is made for
the general framework. The concrete contribution here is the
explicit linearization and marked fibre for the fixed ADO state,
including its half-root, source, metric and parity signatures.

[The audit](../experiments/audit_ramified_weyl_fibre.py) checks 18 actual
knot cut polynomials through z-order five at levels 2 through 7,
recovering their exact complete values without a rank assumption.
Eleven tests of the previously certified finite cyclotomic operator
check the descended equation through s-order two and its special
rank, at even/composite/odd levels through 18. Equality with the actual
figure-eight cut is tested only at the seven listed levels through 8;
an all-level state equality is not inferred. Another 528 signatures
check the trace and dimension formulas, and exact symbolic examples
check functoriality and the change-of-frame obstruction in Section 5.
[Results](../experiments/ramified_weyl_fibre_results.json) are algebraic
diagnostics, not an asymptotic proof.
