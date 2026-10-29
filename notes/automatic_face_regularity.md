# The Fourier rank conditions follow from knot-exterior homology

Research note, 25 October 2026. This supplies a uniform independent proof
of the two rank conditions in `singular_faces_and_six_two.md`. It applies
to every globally branched oriented ideal triangulation of a knot
exterior in S^3. No geometricity, quantum-invariant existence theorem,
or finite census assertion is used.

## 1. Statement

Let X be the ideal compactification of an oriented one-cusped manifold M,
with its single ideal vertex. Assume H^1(X;R)=0. For ordered face pairings
put

    D=X_0-X_1+X_2, R=X_2-X_3, E=diag(epsilon).

**Theorem.** Rank D=N. For any basis F of ker D, set

    T=E R F, U=X_0 F,
    K=basis of ker T, P=basis of im T,
    C=K^T U^T P.

Then rank C=dim ker T. Thus the Fourier reduction of the existing charged
tensor always has a well-defined convergent residual integral. The full
stacked face matrix [D;R] can still be singular.

For knot exteriors in S^3 the cohomology assumption is automatic, as
proved in Section 4. The theorem is also valid whenever the stated
ideal-compactification cohomology vanishes.

## 2. A local relation is exactly an ideal edge cocycle

Introduce three numbers (a,b,c) in an ordered tetrahedron of sign epsilon.
Define four local momentum coefficients and four position coefficients

    p=(b,b+c,c,c),
    q=(a,-a,a+epsilon*b,-epsilon*b).                     (2.1)

Suppose across every glued face pair i,j they satisfy

    p_(t,i)=p_(u,j), q_(t,i)+q_(u,j)=0.                 (2.2)

The vector space of such relations is naturally isomorphic to the space
of cellular real 1-cocycles on the ideal triangulation X.

**Proof.** In one tetrahedron give its vertices potentials

    n_0=0, n_1=c, n_2=b+c, n_3=b+c+epsilon*a.

For the face opposite i, list its three vertices as u<v<w and let
omega_i=epsilon*(-1)^i. Direct substitution gives

    p_i=n_v-n_u, q_i=omega_i*(n_w-n_v).                 (2.3)

The same face has opposite omega on its two occurrences. Because face
gluings preserve the three-vertex order, (2.2) is exactly equality of
the two independent vertex differences on that face. Consequently all
local differences lambda_ij=n_j-n_i descend to a single number on each
global oriented edge. They sum to zero around every triangular face,
so define a cellular edge cocycle.

Conversely, a global edge cocycle is locally a gradient on each
tetrahedron: set n_0=0 and n_i=lambda_0i. The triangular cocycle
relations give every other edge difference. Then recover

    c=n_1-n_0, b=n_2-n_1, a=epsilon*(n_3-n_2).

Equations (2.3) prove the face matching conditions. The constructions
are inverse. This proves the claimed isomorphism, including injectivity.

There is only one ideal vertex, so the cellular coboundary map from
0-cochains to 1-cochains is zero. Hence H^1(X;R)=0 says that the cocycle
space itself is zero. All relations (2.1)--(2.2) must therefore vanish.

## 3. Applying the local lemma to the matrices

First, if D^T a=0, use (2.1) with b=c=0 in every tetrahedron. Its
position coefficients match because their paired sums are exactly
D^T a; the momentum coefficients are zero. The lemma forces a=0.
Thus D has full row rank N.

Next suppose C has a nonzero left-null vector z. The corresponding
global face assignment k=F K z obeys

    Dk=0, Rk=0.

Let b=X_0 k. Since P spans E R(ker D), the condition z^T C=0 is

    b^T E R F=0.

Therefore R^T E b annihilates ker D and is in im D^T. Choose a with

    D^T a+R^T E b=0.                                   (3.1)

Set c=X_2 k. The equations Dk=Rk=0 say that the four occurrences of
k in a tetrahedron are (b,b+c,c,c), exactly the momentum coefficients
in (2.1). They match on paired faces since k is a global face
assignment. The local position coefficients in (2.1) sum over faces
to the left side of (3.1). Thus they match as well. The lemma forces
a=b=c=0, hence k=0. Since F K has independent columns, z=0, a
contradiction. C has full row rank as asserted.

This argument uses only real finite-dimensional linear algebra and the
explicit cocycle lemma. In particular it does not infer convergence
from a general TQFT theorem with an unaudited analytic proof.

## 4. Why the cohomology vanishes for knot exteriors

Let M be the compact exterior of a knot in S^3. Its ideal compactification
is M with its connected boundary torus collapsed to one point. Thus

    H^1(X;R)=H^1(M,boundary M;R).

In the cohomology exact sequence of this pair, H^0(M)->H^0(boundary M)
is an isomorphism. Hence H^1(M,boundary M) injects into H^1(M), with
image the kernel of restriction to H^1(boundary M).

Mayer--Vietoris for S^3=M union a solid torus gives H_1(M;Z)=Z and
shows that the boundary meridian maps to its generator. For example
H_1(boundary M)->H_1(M) direct-sum H_1(solid torus) is an isomorphism;
the meridian is zero in the solid torus, and the other boundary
generator generates its H_1. The meridian therefore generates H_1(M).
Restriction H^1(M)->H^1(boundary M) is injective, so its kernel and
H^1(M,boundary M) vanish. This proves the required hypothesis.

## 5. Consequence and the remaining distinction

The full-tensor volume theorem in `singular_faces_and_six_two.md` now
applies to **every globally branched complete positive geometric ideal
triangulation of a knot exterior in S^3**. Its Fourier rank assumptions
have a uniform topological proof, rather than being additional census
conditions. The independent geometry-to-saddle and analytic proofs
remain necessary and are supplied in that note.

This is still a statement about the full charged tensor at complete
angles. A knot quantum A-state additionally needs its specified boundary
fiber, phase, normalization, and peripheral identification. The general
preferred-longitude/fiber construction and equivalence of arbitrary
realizations are not consequences of the rank theorem alone. For 6_2
these are supplied by the separate finite certificates.

The subsequent `preferred_longitude_cochains.md` supplies the uniform
preferred-longitude relation. The ordinary-fiber construction and then
`fourier_boundary_state.md` supply the normalized meridian state for both
possible boundary ranks, preserving the complete geometric volume limit.
Geometric realization and global triangulation identification are still
separate obligations.
The subsequent `preferred_longitude_cochains.md` now gives the uniform
preferred-longitude relation. `general_boundary_state_and_framing.md`
constructs the meridian state whenever the longitude increases the B rank,
with an exact correction for any rational longitude shear. The other
boundary-rank case remains separate.

There is also no assertion here that every ideal triangulation admits
a global branching or that every hyperbolic alternating knot has the
required positive geometric realization of the chosen combinatorics.
Those are separate uniform construction questions.

The script `reduce_singular_faces.py` checks (2.3) symbolically and
recomputes the ideal edge-cocycle matrix in each finite example. As a
useful boundary check, the two-component word RLRLRL has a nonzero
cocycle and local-relation space; the one-vertex hypothesis should not
be dropped without a replacement argument.
