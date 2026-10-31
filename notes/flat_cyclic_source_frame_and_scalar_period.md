# The flat cyclic source frame is rigid; its scalar period is separate

Independent algebraic theorem, 27 October 2026. The actual highest-input
clock, cyclic repair and paired source have a whole matrix-algebra
description BEFORE quantum jets. On the source-cyclic chart their
scheme-theoretic classification is elementary. A rank-one defect must
be aligned with the actual source line; rank one alone does not imply
this. The rigid frame does not fix the scalar of a closed transport.

## 1. The actual source frame and its coefficient ring

Fix N>=2, Q a unit, and invert only 1-Q^k for 1<=k<N. Write

    delta=1-Q^N,
    B_0=diag(1,Q,...,Q^(N-1)),
    P_0 e_j=e_(j+1 mod N),
    E_0=E_00, A_0=e_0 1^t.

Here 1^t is the original all-ones output row. These are the literal
highest-input data of
[the actual two-wall boundary](actual_highest_whittaker_boundary_and_moving_walls.md),
not an additional state. Direct entries give

    B_0 P_0-Q P_0 B_0=delta E_(0,N-1),
    B_0 P_0 B_0^-1 P_0^-1
                    =Q[I+(Q^-N-1)E_0],
    B_0 A_0=A_0, A_0 P_0=A_0, A_0^2=A_0,
    P_0^N=I, E_0 A_0=A_0, A_0 E_0=E_0.          (1.1)

The last two identities express equality of the two IMAGE lines.
They do not identify the source row with the defect row: E_0 is
e_0 e_0^t, whereas A_0 is e_0 1^t. That distinction is retained.
The normalization A_0^2=A_0 is the specified primitive pair
1^t e_0=1. Any original external d_N(M) line remains attached
as that exact separate source factor; it is not divided away at
one of its zeros/poles to obtain this primitive matrix statement.
Without the specified normalization, BA=A and AP=A allow every
scalar multiple a A_0, so even the source scale would be free.

Work with rank-N vector bundles over this coefficient ring or any
specified COMMUTATIVE base algebra. Source and defect projectors have locally
free image of rank one. No delta inverse is adjoined.

## 2. An explicit classification on the cyclic source chart

Let E have rank N, let P be invertible with P^N=I, and let A be
an idempotent rank-one source. Put L=im A. Suppose

    BA=A, AP=A,
    im(BP-QPB) contained in L,                    (2.1)

and suppose the source orbit map

    Theta: direct_sum_(j=0)^(N-1) L -> E,
    Theta(l_0,...,l_(N-1))=sum_j P^j l_j          (2.2)

is an isomorphism. Then in this CANONICAL line-valued frame

    P=P_0 tensor I_L, B=B_0 tensor I_L,
    A=A_0 tensor I_L.                            (2.3)

Proof. AP^j=A makes A act by summing the N input copies into
the zeroth copy. P cycles them. BA=A makes the first column
of B equal to (I_L,0,...,0)^t. Every entry of B in this frame
is an endomorphism of L, hence a scalar over the base. Since
the image in (2.1) lies in the zeroth copy, the other rows give

    B_(i,j+1 mod N)=Q B_(i-1,j), 1<=i<N.         (2.4)

For i>=j this recurrence and the first column yield
B_(i,j)=Q^j delta_(i,j). For i<j they yield
B_(i,j)=Q^i B_(0,j-i). The wrap case j=N-1 in (2.4) has
left side zero, forcing every B_(0,k)=0 for 1<=k<N.
This proves (2.3). In particular B is automatically invertible.
No wall cancellation, eigenvalue argument or flatness theorem
was needed for this proof.

This is a classification over arbitrary base algebras on the
specified open chart, including algebras with nilpotents. Its
groupoid is the groupoid of line bundles L, by E=L^direct_sum N.
If E is required to be globally free, retain the corresponding
trivialization condition on that direct sum. Over a local base L
is free. Choosing a source vector v trivializing L, with Av=v,
makes Theta a canonical ordinary basis and removes all its
automorphisms. Without that vector marking the remaining
automorphisms are precisely multiplication by a central unit on L.

The cyclic hypothesis is automatic near the actual root source.
Indeed at a primitive Q_N the actual multiplicative relation
reduces to BP=Q_N PB. If Bv=v, the N vectors P^jv have distinct
eigenvalues Q_N^j. They are nonzero and independent over every
residue field. Rank N makes them a basis. In a local deformation
of that root point their determinant stays a unit, proving (2.2).
This does not assert cyclicity on unrelated global components.

## 3. The multiplicative defect and its explicit flat saturation

Suppose also that R is a rank-one idempotent with

    AR=R, RA=A,
    BPB^-1P^-1=Q[I+(Q^-N-1)R].                  (3.1)

The image of its commutator lies in im R=L, so Section 2 applies.
In its canonical frame R=e_0 rho with rho_0=1. Equations (1.1)
and (3.1) reduce EXACTLY to

    delta (R-E_0)=0,
    delta rho_j=0, 1<=j<N.                     (3.2)

If the base is flat over the normal parameter, or more generally
delta is a nonzero divisor on it, (3.2) forces R=E_0. This is
the actual normalized defect, recovered before taking jets.

The unsaturated presentation has the explicit coordinate algebra

    R_base[rho_1,...,rho_(N-1)]/(delta rho_j).   (3.3)

When delta is a nonzero divisor on R_base, this presentation is
not flat at the wall. Its delta-saturation kills the rho_j and
is just R_base. If the supplied base already has delta-torsion,
saturation also removes that base torsion. At delta=0 alone the multiplicative relation
cannot see these projector-row parameters. A rank-N module can be
locally free over this nonflat comparison base; that is not a
substitute for flatness/saturation of the base over the normal
parameter. If the module itself is flat over that normal base,
the nonzero-divisor hypothesis above applies. If R is marked to be
the actual E_0, these excess parameters never arise.

## 4. The whole endpoint-corrected algebra is a matrix algebra

Set

    chi(X)=product_(j=0)^(N-1)(X-Q^j),
    D=R[X]/chi(X),
    e_j(X)=product_(k!=j)(X-Q^k)/(Q^j-Q^k).

The node differences are units in the stated head localization.
Evaluation at them identifies D with R^N: the e_j are orthogonal
idempotents summing to one. The polynomial map

    tau(X)=Q^-1[X-delta e_0(X)]                  (4.1)

cycles these evaluations, so it is an algebra automorphism with
tau^N=I and tau(e_j)=e_(j+1 mod N). Form the explicit algebra
with basis f P^a, f in D, 0<=a<N, and multiplication

    (f P^a)(g P^b)=f tau^a(g)P^(a+b mod N).     (4.2)

Associativity follows from tau being an automorphism. Define

    E_(i,j)=e_i P^(i-j mod N).

These satisfy E_(i,j)E_(k,l)=delta_(j,k)E_(i,l), sum_i E_(i,i)=I.
They form a basis: fixing i,a recovers e_iP^a uniquely. Therefore
(4.2) is EXACTLY Mat_N(R), with no rank comparison or unverified
quiver theorem as a premise. The original source is recovered by

    A_0=e_0 sum_(j=0)^(N-1)P^j,
    Tr(A_0)=1.                                  (4.3)

Thus the original paired-source matrix can be recovered from the
flat normalized defect and cyclic transport; the defect and source
rows remain different. Every coefficient, root norm and endpoint
term is retained in (4.1), rather than imposing an impossible
whole BP=QPB with P^N=I.

This adds the explicit finite ALIGNED SOURCE classification and
whole matrix-algebra presentation to the boundary note. It does
not duplicate or contradict
[the whole clock function theorem](whole_clock_function_algebra_and_endpoint_extension.md).
That theorem concerns the UNCORRECTED infinite-order shift on a
coalescing clock and requires its endpoint tower. Here the nodes
Q^j are distinct at each fixed primitive root, and (4.1) changes
the last shift by its actual finite endpoint defect. A fixed-N
head localization is not a common neighborhood of Log Q=0 as
N grows. This finite algebra does not discard whole functions,
unwrapped Green tails or their separate source extension.

## 5. Rank one without source alignment is insufficient

There are flat rational families through the actual N=2 root
which satisfy every OTHER condition but are not the canonical
clock. Put near Q=-1

    delta=1-Q^2, h=Q-Q^-1,
    t=delta/(1-delta^2), x=delta^2/(1-delta^2),
    P=[[0,1],[1,0]], A=[[1,1],[0,0]],
    B=[[1,t h],[0,Q+x h]],
    R=[[1+x,-t],[t,-x]].                         (5.1)

All entries are rational and regular there; B is invertible.
Since t^2=x(1+x), direct multiplication proves

    R^2=R, Tr R=1, rank R=1,
    BA=A, AP=A, P^2=I,
    BPB^-1P^-1=Q[I+(Q^-2-1)R].                 (5.2)

At Q=-1 these are EXACTLY B_0,P_0,A_0,E_0. Nevertheless the
second eigenvalue Q+xh of B is generically different from Q,
so no conjugation can identify it with B_0. The rank-N module
and every displayed rational family are flat. What fails is
AR=R, namely alignment of the moving defect with the actual
source line. Even correct classical source/defect markings and
flatness of the objects do not impose that whole relation.
Taking delta replaced by delta^k in x,t makes the tilt invisible
to an arbitrarily long fixed jet, without changing this conclusion.
The ACTUAL fixed E_00 defect is aligned and is covered by the
positive theorem, not by this counterexample.

## 6. The scalar closed period is not fixed by this frame

Over any base the commutant of the matrix units in Section 4
consists of scalars: commuting with E_ii makes a matrix diagonal,
and commuting with E_ij makes all its diagonal entries equal.
Consequently a closed frame-intertwiner is

    C=c I,    Tr(A_0 C)=c,                      (6.1)

with c an ARBITRARY scalar (a unit if C is invertible). Adjoining
c, or an invertible c, gives a flat finite-type extension with
the exact same frame, defect and normalized source. Source-frame
classification alone imposes no equation on that period. It also
does not supply a regulator action or fix a leading norm.

This is a statement about insufficient structural conditions,
not permission to change the original actual knot state. Once
the complete actual crossing word and every scalar/cap/peripheral
normalization are supplied, that word fixes c. A comparison of
the FULL word evaluations through the canonical source frame
preserves it automatically. Merely identifying their clock/source
matrix algebras does not compare their selected word sections.

There is no contradiction with strict vector-pointed rigidity.
An intertwiner C preserving a specified nonzero v must satisfy
cv=v and hence c=1. A generic actual knot period C=cI is NOT
such a source-vector-preserving automorphism; it preserves the
coupon A by conjugation while its cut pairing is c. Demanding
strict preservation at that final step would assume the desired
normalization and exclude the actual nontrivial period.

Here the actual scalar-knot example is on its original ROOT fiber
with generic M. Its whole auxiliary q-normal lift need not be
scalar, as the explicit unknot in
[the one-index source audit](actual_one_index_fourier_source_and_ward_reduction.md)
shows. No extension of root scalarity is used in this argument.

[The exact audit](../experiments/audit_flat_cyclic_source_frame.py)
and [saved results](../experiments/flat_cyclic_source_frame_results.json)
check the universal recurrence equations, all matrix units/source
moments, arbitrary conjugate frames, wall parameters and the
explicit nonaligned rational family. No geometric selected-cycle
or hyperbolic-volume theorem follows from this finite-frame result.

The [independent proof audit](mobius_and_flat_source_frame_independent_audit.md)
checks the commutative-base classification, corrected crossed
product, saturation scope and nonaligned counterexample. It also
distinguishes the actual root scalar closure from its auxiliary
whole q-normal lift.
