# Affine flag frames and transport of the selected vacuum

Research note, 25 October 2026. This gives full-matrix covariance under
affine changes of a flag frame. It also identifies a limitation of the
unit pointing in the preceding recoupling note: an intertwiner at fixed
central character generally transports that unit to a nonconstant vector.
The resulting period transport must be retained in the proposed torsor.
These are uniform algebraic statements, with no knot examples as inputs.

Throughout, n is odd, omega is a primitive n-th root, and all displayed
endpoint roots, affine differences and central characters are nonzero.
Work on their common splitting cover. Permutations are literal ones.

## 1. An explicit Hilbert-90 transport, including its scalar

Fix a central character g=(lambda,mu). Two endpoint pointings have

    b^n-lambda*a^n=mu=b'^n-lambda*a'^n.

Use the two modules on K[x]/(x^n-lambda), with common multiplication X
and with Y=(b-aX)sigma^(-1), Y'=(b'-a'X)sigma^(-1). Set

    r(x)=(b'-a'x)/(b-ax).

Every denominator and numerator is invertible since its cyclic norm is
mu. Their ratio has norm one. Choose alpha^n=lambda and specify

    h_0=1,
    h_j=product_(k=1)^j r(omega^k alpha),  1<=j<n.

Norm one gives h_n=h_0, including the last step at x=alpha. Let H(X)
be the unique polynomial of degree less than n with

    H(omega^j alpha)=h_j.

It can be written explicitly using the spectral idempotents

    e_j(X)=(1/n) sum_(k=0)^(n-1) [X/(omega^j alpha)]^k,
    H(X)=sum_j h_j e_j(X).                              (1.1)

All h_j are units, so H is invertible. The recurrence proves

    H X=X H,     H Y=Y' H,     H(alpha)=1.              (1.2)

These statements prove existence, not just an appeal to Hilbert 90.
They also prove uniqueness: an intertwiner commutes with X and is a
polynomial in it; its cyclic recurrence fixes it up to scalar, and the
last normalization fixes that scalar. In particular, for three pointings
at the same central character and the same marked root alpha,

    H_(2,1) H_(1,0)=H_(2,0)                            (1.3)

exactly. This follows either from the product formula or from (1.2).
Changing the marked root to omega alpha replaces H by H/h_1. Thus this
normalization is a section on a marked spectral cover, not an invariant
scalar after forgetting that cover. Its determinant is exactly product h_j.

There is an elementary test for the selected vector. If H*1 is a scalar
multiple of 1, then H itself is scalar because powers of X applied to 1
span the module. Equation (1.2) then implies a=a', b=b'. Therefore
distinct endpoint pointings at a fixed central character are not identified
by an intertwiner taking unit to unit. This does not obstruct an intrinsic
period construction: it specifies the vector that construction must transport.

## 2. Ordered flags, additive transports and triangle modules

In an affine chart, let p_i be distinct points and choose roots A_i^n=p_i.
Assign the oriented edge i<j the affine central character

    g_ij=(1,p_i-p_j),     with endpoints A_j -> A_i.

These compose: g_ij*g_jk=g_ik. The construction in
`pointed_period_descent.md`, Section 1, gives the pointed factorization

    C_ijk: E_ik tensor V_ijk -> E_ij tensor E_jk,         (2.1)

where the relative triangle module has central character and endpoints

    lambda_ijk=(p_i-p_k)/(p_j-p_k),
    mu_ijk=-(p_i-p_j)/(p_j-p_k),
    incoming=A_j/A_k, outgoing=A_i/A_k.                 (2.2)

Its normalized Steinberg parameter is

    t_ijk=p_j(p_i-p_k)/[p_i(p_j-p_k)].

This explains precisely which auxiliary affine-origin data occur in
the earlier Steinberg normalization. The unscaled central character in
(2.2) is translation invariant; the normalized pointing is not.

The explicit Racah closure of the preceding note extends to these
matched endpoint modules. The ordered relative operators (2.2) in that
note did not use X_i^n+Y_i^n=1. On four flags the right relative pair
V_013,V_123 has matching endpoints A_1/A_3. Its total and relative
pointed modules are V_023 and V_012, respectively. Thus the same
general-endpoint factorization gives

    R_0123: V_023 tensor V_012 -> V_013 tensor V_123.     (2.3)

All central powers follow from the affine product law. The four ordered
operator identities and the unit ideal certificates prove (2.3) as the
actual Racah map, with scalar one. No new choice of quantum function
or unaudited matrix identity is used.

## 3. Full affine covariance, including the triangle matrices

Translate all p_i by B and choose compatible new roots A_i'^n=p_i+B.
The edge central characters g_ij stay fixed. Since their lambda is one,
mark alpha=1 on every edge and use (1.1) to define

    T_ij: E_ij -> E_ij'.

These intertwiners compose exactly for successive endpoint choices.
There is a unique triangle map S_ijk satisfying

    (T_ij tensor T_jk) C_ijk
        =C_ijk' (T_ik tensor S_ijk).                   (3.1)

Here existence is substantive: conjugate the left side by C_ijk' and
remove T_ik on the total factor. The result commutes with the total
full matrix algebra. Its commutant is precisely identity tensor
End(V_ijk). Consequently it has the form identity tensor S_ijk.
The relative-operator identities also show that S_ijk intertwines the
two unscaled triangle algebras (2.2). Everything is invertible, which
proves uniqueness and invertibility of S_ijk.

This is a finite, explicit construction of the full triangle matrix;
it is stronger than covariance of its determinant. Naturality of the
two three-edge evaluation maps now gives the exact tetrahedral identity

    R_0123' (S_023 tensor S_012)
          =(S_013 tensor S_123) R_0123.                (3.2)

To check its scalar, insert (3.1) in the two tree evaluations, use the
pointed Racah identity, and cancel their common invertible evaluation
and T_03. Thus the identity is literal, with all scalar factors intact.
Equations (1.3) and (3.1) prove the exact composition law for the S maps.

A common scaling p_i -> u^n p_i, A_i -> u A_i identifies X with X
and Y with uY on each edge. The relative operators D=X_1+Y_1/Y_2
and -C=-(Y_1/Y_2)X_2, the endpoint ratios (2.2), and the C and R
matrices are unchanged. The edge transport ratios in (1.1) are also
unchanged by a common scaling. Together with translations this proves
full covariance for the affine group, on the compatible endpoint-root
cover. The proof applies at every odd n, including composite n.

For a finite exterior contraction, use the dual S map on the oppositely
oriented copy of each shared triangle. Interior maps cancel. The only
surviving maps act on boundary tensors and on the chosen period vectors.
No convergence or angle assumption is needed. This is a relative statement
about finite tensors with the specified duality pairings, not yet about
arbitrary literature integration cycles.

## 4. The vector and normalization lines do not disappear

For B nonzero, the incoming triangle endpoints in (2.2) change: equality
of their n-th powers would imply

    (p_j+B)/(p_k+B)=p_j/p_k,
    B(p_k-p_j)=0,

contrary to distinct flags. The intertwiner S_ijk therefore cannot map
the old unit line to the new unit line, by the test in Section 1.
The transported vector is S_ijk*1 and must be retained. Thus the unit
vacua coherent under recoupling in a fixed frame are not already a
frame-independent selected period. An argument using only scalar
commutants or determinant roots would miss this matrix-valued change.

Normalization remains equally explicit. Taking determinants in (3.1)
gives

    (det S_ijk)^n
       =[(det T_ij det T_jk)/(det T_ik)]^n
                         *det C_ijk/det C_ijk'.         (4.1)

The previously proved general-endpoint determinant yields, for translations,

    det C_ijk/det C_ijk'
       =(A_k^n/A_k'^n)^(n(n-1)/2).                    (4.2)

Both are identities of generic units. Determinant-normalized frames
require the corresponding roots and their phases. The unnormalized
construction (3.1) already chooses an exact scalar; one must not replace
(4.1) by an unspecified equality after taking absolute values or by
specializing a peripheral parameter first.

The endpoint and spectral covers, the full triangle transport and its
selected vector, and the determinant line are therefore different parts
of the proposed period object. The finite Heisenberg cover alone records
only part of it.

## 5. Literature comparison and the remaining projective problem

This is a direct reconstruction within the existing cyclic Weyl/Borel
recoupling definition, not a claim of a new quantum dilogarithm.
Baseilhac--Benedetti's
[matrix-dilogarithm construction](https://arxiv.org/abs/math/0306283),
Sections 3 and 5 and Appendix 8, is a closer existing framework than
the surface theory alone. Their
[analytic families](https://arxiv.org/abs/1212.4261), Introduction and
Section 4, already organize rational quantum-hyperbolic state sums over
covers of augmented character varieties. Neither global theorem is
assumed in the proofs above. The explicit pointed transports here record
what would need to match in a comparison with a chosen published state.

The subsequent `projective_frame_period_torsor.md` handles all projective
frames by compatible triangle Weyl rescalings and determinant rigidity
on a root cover anchored at the identity. The actual selected literature
period and its cycle still need to be identified under this local descent.
The regulator comparison across levels remains a further theorem. In
particular, finite central characters and semiclassical shape coordinates
must be matched before using the rational Faddeev formula for growth.
Those last steps are not supplied by the frame theorem or by Hilbert 90.

The later [source-flag proof](source_flag_transport.md) writes this
origin dependence intrinsically by adding a marked point s in P^1.
Changing s gives the same normalized Hilbert-90 map in the shared
face frames. Using the actual reverse edge caps fixes its face
scalar and proves dual and cyclic naturality at every level for
finite sources. Its first normal coefficient is a concrete affine
translation of normal lifts; the selected cut row moves inversely.
The global meridian/source and regulator identification remain open.
