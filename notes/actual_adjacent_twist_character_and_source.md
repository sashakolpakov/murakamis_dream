# Exact adjacent-twist character coupling with its physical source

28 October 2026. Adjacent original twist blocks have an exact coupled
quantum-character algebra, not independent spectral phases. The
identities below give a denominator-free braid recursion, fix the
nearest-neighbor spectral phase ratios, and impose a **strict integer
spectral window** on the original generic-meridian family. An actual
cup port restricts the total Casimir without changing the marked
co-source. These are reusable local identities at arbitrary width.

They do not estimate the original whole-source q-Racah contour or
prove a sharp volume upper bound or noncancellation. The exact phase
coupling is a step beyond estimating separate repeated-crossing norms.

## 1. Physical trace coordinates

Use the actual balanced generators K_i,F_i,Ecal_i=rho^2E_i on three
physical heads, with q=exp(pi i/N), rho=q-q^(-1), delta=q+q^(-1).
Let e_i=q Ecal_i and form the literal matrices

    L_(+,i)=[[K_i,e_i],[0,1]],
    L_(-,i)=[[1,0],[-K_iF_i,K_i]],
    G_i=L_(-,i)^(-1)L_(+,i).

Keep the actual prefix-based meridians H_i from the shared quantum
flags: H_1=G_1 and H_i=P_(i-1)^(-1)G_i P_(i-1), where
P_(i-1)=L_(-,i-1)...L_(-,1). Define tr_q(T)=qT_11+q^(-1)T_22 and

    A=tr_q(H_2H_1)=Omega_12,
    B=tr_q(H_3H_2)=Omega_23,
    C=tr_q(H_3H_1),
    D=tr_q(H_3H_2H_1)=Omega_123.                       (1)

The two displayed intermediate Casimirs are the actual coproduct
Casimirs of the original physical heads. The prefix conjugation in
B drops out of tr_q with its required q-ordering, not by ordinary
trace cyclicity. Each head has central Casimir a_i; for common original
meridian M, a_i=-(M+M^(-1)); at completeness a_i=-2.

Set central coefficients

    alpha=a_1a_2+a_3D,
    beta=a_2a_3+a_1D,
    gamma=a_1a_3+a_2D.                                (2)

The full original common Cartan cancels in conjugation statements,
but remains on the actual crossing operators and their powers.

## 2. Exact quantum Fricke identities

The following are finite polynomial identities, including N=2:

    q^(-1)AB-qBA=rho(delta C-gamma),
    q^(-1)BC-qCB=rho(delta A-alpha),
    q^(-1)CA-qAC=rho(delta B-beta),                    (3)
    [D,A]=[D,B]=[D,C]=0.

They retain the coupled cubic

    q^(-1)ABC+q^(-2)A^2+q^2B^2+q^(-2)C^2
       -q^(-1)A alpha-qB beta-q^(-1)C gamma
     =delta^2-a_1^2-a_2^2-a_3^2-D^2-a_1a_2a_3D.       (4)

No division by delta, rho, a clock determinant, or a nilpotent face
is needed to state (3)--(4).

Here is a reproducible algebraic proof, separate from finite-level
numerical checks. Take independent quantum tori Z_i S_i=q^2S_i Z_i,
and independent formal meridians M_i. Substitute

    K_i=-M_i q^(-1)Z_i^(-1),
    F_i=S_i(1-q^2 Z_i),
    Ecal_i=S_i^(-1)(M_i Z_i^(-1)-M_i^(-1)).            (5)

Their single-head Casimir is -(M_i+M_i^(-1)). Expand (1) using the
two-by-two triangular inverse matrices, then put every product into
the order S_1^u Z_1^v S_2^w Z_2^x S_3^y Z_3^z. Multiplication supplies
only the scalar q^(2sum v_i u_i'). The accompanying certificate uses
integer Laurent coefficients in q,M_1,M_2,M_3 and verifies that every
coefficient of (3)--(4) is zero. A,B,C,D have respectively 14,14,62,34
Laurent terms before those identities are expanded.

This is an exact generic-q polynomial certificate, not a sample at
roots or an imported q-Racah theorem. It applies to the original
finite nilpotent heads too. Indeed the single-head algebra with
fixed Casimir has normal forms K^aF^b and K^aEcal^c; the mixed product
FEcal is its fixed nonzero Laurent polynomial in K. The torus
realization (5) is faithful on those normal forms: distinct F/Ecal
degrees have distinct S powers, and the remaining nonzero Laurent
factor cannot kill a Laurent polynomial in Z. Thus the certified
identities hold in that central quantum-group quotient and then in
its finite-head representations. This argument does not add the
generic cyclic E endpoint to the original module.

## 3. Actual braid action and the retained twist phases

The already directly verified original Hurwitz transport acts on
H_1,H_2,H_3. Taking its ordered traces gives the exact identities,
for equal colors (a_1=a_2=a_3=a, alpha=beta=gamma=a^2+aD),

    Ad(R_12):(A,B,C) -> (A,q alpha-qBA-q^2C,B),
    Ad(R_23):(A,B,C) -> (C,B,q alpha-qCB-q^2A).          (6)

The trace reductions in (6) are also included in the exact Laurent
certificate, using H_i^(-1)=q^(-1)a_i I-q^(-2)H_i. Thus (6) does not
infer a trace identity from a classical mnemonic. For distinct colors,
the same proof retains the permuted a_i and the appropriate alpha,
beta,gamma in (2); the present common-color formulas suffice for the
original knot family. Literal inverse crossings give the inverse
polynomial maps; no new scalar is supplied.

Put B_t=R_12^t B R_12^(-t). The complete adjacent-block transport is

    B_(t+1)=-q B_t A-q^2 B_(t-1)+q alpha,
    B_0=B, B_(-1)=C.                                  (7)

This formula holds at every signed integer t and every N, with the
whole physical boundary and original source unchanged. It retains
the q-phase; replacing it by a real modulus recurrence is not valid.

On the genuine generic-meridian family the first pair has distinct
Casimir nodes and original eigenvalues

    c_j(Y)=q^(-1)YQ^(-j)+qY^(-1)Q^j,
    lambda_j(Y)=nu_jY^(-j),
    nu_j=(-1)^j q^(j(j+1)), 0<=j<N.                    (8)

The normalized physical fusion/projector formulas in
[the factorial-frame theorem](actual_twist_block_factorial_frame_bound.md)
realize these operators with their actual normalizers. In particular
the two homogeneous multipliers of (7) at A=c_j(Y) are

    -Q^(j+1)Y^(-1)=lambda_(j+1)/lambda_j,
    -Q^(-j)Y=lambda_(j-1)/lambda_j.                    (9)

These are precisely the neighboring ratios of the original twist
phases, not independently selected semiclassical characters.

## 4. A strict spectral window, rather than a cyclic replacement

Let E_i(Y) denote the meromorphic actual pair-Casimir projectors,
extended by the third head. For i!=j, project (7) between E_i and E_j.
The central forcing disappears, and its scalar characteristic equation
is

    (lambda_i/lambda_j)^2
        +q c_j(Y)(lambda_i/lambda_j)+q^2=0.

By (9), equality as a meromorphic function of Y forces the exponent
of Y in lambda_i/lambda_j to be +1 or -1. Therefore

    E_i(Y) B E_j(Y)=0 unless i=j or i=j+1 or i=j-1     (10)

as INTEGER indices in [0,N-1]. For N>=3 the apparent cyclic neighbor
(0,N-1) is excluded. Casimir nodes alone are cyclic, but the original
braiding eigenvalues (8) have a nontrivial endpoint norm character;
discarding it would incorrectly allow that extra edge.

The diagonal is fixed as well:

    (delta+c_j(Y)) E_j B E_j=E_j alpha E_j.             (11)

This follows from Ad(R_12)C=B and the diagonal part of (6).
It is stated without dividing at a zero of the factor on the left.
Equations (10)--(11) are the actual finite three-term spectral
coupling underlying a q-Racah overlap. They remain identities of whole
meromorphic germs at completeness; the colliding projectors cannot
be independently evaluated or replaced by a semisimple root basis.

For an adjacent sequence R_12^ell R_23^m, its exact kernel is obtained
by composing the actual C_T E_i C_T^(-1) projector matrices with their
lambda_i^ell and lambda_j^m factors, then applying the original
co-source. Formula (10) supplies the coupling recurrence rather than
treating those spectral labels as independent or modulo N. It does
not yet evaluate the resulting multidimensional contour.

## 5. The original cup port gives the parabolic total character

At completeness let p be the original cup on heads 1,2. Its actual
Hopf identities E_tot p=F_tot p=0 and K_tot p=p imply that both
two-head coproduct triangular matrices are identity on p. Consequently

    (D+2I)(p tensor v)=0 for EVERY third-head vector v. (12)

Every actual word in R_12 and R_23 commutes with D, so (12) remains
true on the entire transported cup-generated subspace. Spectator
heads may be included. An original ordinary cap and full marked row
can be left untouched: inserting D+2 into that original whole network
gives zero by (12), with no change of co-source or division by a knot
period. This is a forward source restriction, not an assertion that
the unrestricted marked row is an invariant covector.

One may NOT impose D=-2 on an arbitrary three-head port which has
already interacted with outside heads. At such a port the full D in
(2)--(7) must be retained and sewn to its actual exterior source.

On a commutative principal chart, (4) at a_i=-2 becomes the usual
four-punctured character cubic. On the actual cup slice D=-2 it is

    A^2+B^2+C^2+ABC-8(A+B+C)+28=0,
    (X+Y+Z)^2+XYZ=0, X=A-2,Y=B-2,Z=C-2.               (13)

This identifies the coupled trace support and its original parabolic
source. It does not establish that the original spectral cycle has a
nonzero intersection with its geometric place, or bound every complex
boundary phase by knot volume.

## 6. Audit and remaining analytic problem

    python3 experiments/audit_actual_adjacent_twist_character.py

The certificate checks nine generic Laurent identities with three
independent formal meridians, including the cubic, centrality and both
ordered Hurwitz trace reductions. Separate actual finite matrices test
complete and generic M, four iterates of (7), and the original cup
restriction with the FULL marked four-head plat closure. Both level
parities and N=2 are included.
[Saved results](../experiments/actual_adjacent_twist_character_results.json).

What remains is an analytic/source theorem for the **joint** q-Racah
overlap period: retain (8)--(11), its endpoint and meridian currents,
and prove a contour bound or nonzero geometric coefficient after full
closure. Character support and correct local phase ratios alone do
not prove that estimate. No sharp-volume conclusion is claimed here.

## 7. A specific obstruction to leaving the spectral contour real

At completeness the original spectral nodes are

    c_j(1)=2cos((2j+1)pi/N),

and their real-angle limit lies in [-2,2]. On a regular physical
classical chart, A is the actual trace of the product of its two
based parabolic meridians, by (1). A nontrivial element in a discrete
faithful hyperbolic manifold group cannot have real trace strictly
between -2 and 2: such a matrix is elliptic, whereas the manifold's
deck group acts freely and discretely on hyperbolic space. Thus a
regular discrete-faithful pair-product trace cannot occur in the
interior of this real spectral interval. A loxodromic pair product
requires either a nonreal trace or a real trace outside that interval.
Parabolic/central pair products belong to the turning values +/-2
and need their own retained boundary analysis.

Consequently a proposed real-spectral-angle stationary proof cannot
simply identify its real optimizer with a regular geometric pair
whose product is loxodromic. The q-Racah spectral variable must undergo
a complex deformation, or one must perform another actual polarization
change with its source. This criterion is local and applies at any
width; it is not a knot census or a disproof of a complex-contour route.
Real eigenvalues of a nonnormal finite Casimir do not exclude complex
principal characters in the original physical polarization. The claim
concerns leaving THIS diagonal spectral contour real.

This is why the coupled trace identities above still do not turn the
local block bound into a sharp volume estimate: the actual complex
spectral contour and its endpoint/normal source currents remain to be
transported and bounded. They have not been selected by the algebraic
cubic alone.
