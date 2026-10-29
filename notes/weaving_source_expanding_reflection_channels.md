# The weaving reflection source has expanding nonordinary channels

28 October 2026. A bounded negative correction would be enough to
evade the exact indefinite-Gram obstruction at the leading exponential
scale. This note tests a specific way to obtain that correction:
ordinary-color unitary traces and finitely many of their source jets.
The ORIGINAL five-strand weaving source does not admit that particular
reflection-positive decomposition. Its retained projective source has
nonreal EXPANDING moment channels, not only the constant channel seen
at N=2.

This is a fixed-root, word-growth theorem. It is NOT a disproof of a
polynomial-in-N correction for each fixed knot, an asymptotic positive
formula valid only at large N, or a word-dependent scalar norm. Those
would require additional arguments. In particular nothing below
identifies the negative source terms with the bounded ordinary-color
tail of the [regular meridian period](regularized_kashaev_period.md).

## 1. The exact arbitrary-width reflection pairing

At complete color the ORIGINAL balanced crossing matrices are symmetric:

    R_plus^t=R_plus, R_minus^t=R_minus.

For example the positive coefficient with input (a,b), output
(c,j), c=a+b-j, is

    kappa x^(-b-j) Q^(jb) F_c F_a/(F_(a-j)F_bF_j).

Transposing exchanges (a,b) with (c,j); c-b=a-j makes this coefficient
identical. The negative statement follows by inversion. The proved
[complete antiunitary identity](signed_green_antiunitary_transport.md)
therefore gives R_minus=P R_plus^dagger P, including kappa.

Let the width p be odd. Put U=product_(i odd)R_i^+, and let J reverse
the p head factors. Since the odd crossings are disjoint,

    V=product_(i even)R_i^-=J U^dagger J,
    B=VU=J U^dagger J U,
    B^dagger J=J B.                               (1)

The actual first-cut source is F=P_0 tensor g^(tensor(p-1)); the
equivalent averaged marked row may be used only through its already
proved whole-source identity. With the original writhe-zero framing
and its external line retained, the reduced weave moments are

    k_n=Tr(F B^n),
    h(X,Y)=Tr(F J X^dagger J Y),
    h(B^i,B^j)=k_(i+j).                           (2)

Thus a definite reflection subspace containing these half-states
would give a positive Hankel form on the sequence (k_n). Equations
(1)--(2) are an actual source pairing. They do not assert that the
involution J, or its original marked co-source, is positive.

For p=5 the time-ordered braid block is [1,3,-2,-4]. Its physical
over and under encounters alternate, and its strand permutation is
a five-cycle. In particular the closures at n=5m+2 are knots.
The scalar is the original reduced Kashaev value. Restoring the
full ADO dimension line multiplies every moment at this fixed N
by the same known nonzero scalar; it changes none of the poles below.

## 2. An exact selected-source computation at N=3

Put omega=Q=exp(2 pi i/3). Then x=omega and g_a=omega^(1-a).
The two positive and two negative common Cartan factors cancel
in B. Its entries lie in Z[omega]. The audit constructs this
literal operator and its original source exactly, rather than
sampling its spectrum numerically.

The resulting rational generating function is

    G(z)=sum_(n>=0) k_n z^n=A(z)/D(z),             (3)

where A and D are COPRIME integer polynomials and deg D=43. The
full coefficient lists are saved in the audit certificate. The
denominator is

    D=-(z-1)^3 P4a^2 P4b P8^2 P12,

    P4a=z^4-17z^3+55z^2-17z+1,
    P4b=z^4-5z^3+7z^2-5z+1,

    P8=z^8-19z^7+126z^6-380z^5+557z^4
                      -380z^3+126z^2-19z+1,

    P12=z^12-57z^11+1032z^10-8306z^9+34071z^8
          -75492z^7+95323z^6-75492z^5+34071z^4
          -8306z^3+1032z^2-57z+1.                 (4)

The first moments are

    0,1,217,15349,707317,26955828,936961969,... .

This is not an inferred finite recurrence. After discovering its
coefficients, the audit verifies the reversed denominator polynomial
as an EXACT annihilating matrix identity on every source-supported
integer-degree block. It then verifies the numerator and coprimeness.
Cayley--Hamilton-style multiplication of that displayed identity
proves (3) at ALL n, independently of any finite fit.

The ordinary source includes only first-head index zero, hence
supports total integer degrees 0,...,8. The exact arithmetic represents
a+b omega by the integer matrix [[a,-b],[b,a-b]], so the calculation
uses neither floating eigenvalues nor approximate cancellation.
The local matrices and pivot are also checked directly against the
existing independently assembled ORIGINAL balanced crossing.

## 3. The retained source couples to nonreal expanding modes

Exact rational root isolation places a root z_0 of P8 in

    .41<Re z_0<.42, .11<Im z_0<.13.              (5)

In particular |z_0|<1. Numerically z_0 is approximately
.4133686+.1189402i, giving |1/z_0| approximately 2.324825.
The numerical values are explanatory only; (5) proves expansion.
Since gcd(A,P8)=1, this is a genuine DOUBLE pole of the selected
whole source. Its moment contribution has the form
(a+b n)lambda^n with b!=0 and lambda=1/z_0.

It survives on the all-knot subsequence n=5m+2. Indeed the exact
fifth-power resultant is

    Res_z(P8(z),w-z^5)
      =w^8-58634w^7+98866981w^6-2511273890w^5
         +449769171292w^4-2511273890w^3
         +98866981w^2-58634w+1.                   (6)

This polynomial is squarefree and coprime to the corresponding
resultant of D/P8^2. Thus no two relevant fifth powers collide and
cancel the selected double pole. The box (5) also proves
Im(z_0^5)>0: for z_0=x+iy it is
y(5x^4-10x^2y^2+y^4), whose lower bound on that box is positive.
Consequently the generating series of k_(5m+2) has a NONREAL pole
strictly inside the unit disk.

This selected-source assertion is stronger than noticing nonreal
eigenvalues in the ambient transfer matrix. Such eigenvalues could
have been invisible to the marked cap; coprimeness in (3) proves
that these are visible.

## 4. What this rules out, and what it leaves open

An ordinary-color braid action in the positive path model is unitary.
At fixed N, its closing trace is therefore uniformly bounded as
the weave repetition varies. Finitely many fixed-order analytic
jets of those finite matrices have at most polynomial growth in
the repetition: differentiating a product chooses only polynomially
many factors, with the remaining zero-order factors unitary. Their
generating functions are analytic in |z|<1.

Suppose the reflection form (2), restricted even to nonempty
half-states B^(1+5i), split into a positive form plus such an
ordinary-color/finite-unitary-jet correction. Then the sequence
k_(5m+2) would differ by a polynomially bounded sequence from a
positive Hankel moment sequence. This is impossible because of
the nonreal pole just proved.

Here is an elementary justification, avoiding a spectral-positivity
assumption about B. A positive Hankel sequence a_m of exponential
size defines the inner product <X^i,X^j>=a_(i+j) on polynomials.
Multiplication T by X is symmetric. Iterated Cauchy--Schwarz gives

    ||Tf||<=||f||^(1-2^(-j)) ||T^(2^j)f||^(2^(-j)).

The exponential moment bound makes ||T^n f||<=C_f R^n, so letting
j tend to infinity proves ||Tf||<=R||f||. Thus T extends to a
bounded self-adjoint operator on the Hilbert completion. Its scalar
resolvent <1,(I-zT)^(-1)1> is analytic at EVERY nonreal z. One may
verify the usual resolvent fact directly from
||(T-w)f||>=|Im w| ||f|| and the same inequality for its adjoint.
It agrees near zero with the moment series. Subtracting a
polynomially bounded sequence changes that series by a function
analytic in the unit disk, which cannot remove the nonreal pole
in (5)--(6). This is the contradiction.

The conclusion concerns a source-compatible REFLECTION/HANKEL
decomposition with a correction uniformly polynomial in repetition.
The nonordinary source radical cannot be bounded in that way just
by invoking ordinary-color unitarity. It retains expanding channels.

It remains possible that, for each fixed knot as N tends to infinity,
a different marked extension has a polynomially bounded negative
part; this fixed-N computation does not decide that question.
Likewise a nonlinear or word-dependent norm formula need not give
the Hankel form (2), and is not excluded. The positive cyclic norm
already known for all knots is a different construction. No broad
volume theorem, asymptotic counterexample, or positivity failure for
the scalar values themselves follows here.

## 5. Reproducible certificate

    python3 experiments/audit_weaving_source_expanding_reflection_channels.py

The certificate contains the exact numerator/denominator lists, the
matrix-recurrence verification, the rational isolating rectangle,
and the disjoint fifth-power resultants. The whole proof uses the
original local matrices, source, word and ordinary-color unitarity
already independently derived in this repository.
