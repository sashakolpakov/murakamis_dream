# One shared face frame for pointed fusion and the standard matrix kernel

Research note, 26 October 2026. The preceding
[standard matrix comparison](standard_matrix_dilog_source_comparison.md)
has four explicit face factors for a tetrahedron. This note makes them
compatible on a shared affine flag chart: there is one frame for each
ordered triangular face. In that frame the actual dual pairing and
corrected cyclic map are fixed Gaussian matrices times their retained
source-normalized scalars. Every ordered tetrahedron is the standard
kernel with an explicit clock/shift insertion and a specified scalar.

This is a local gluing result for an already specified pointed network.
It does not assert invariance of the bare uncolored tetrahedron under
vertex permutations. The earlier counterexample in
[the oriented-source note](oriented_tetrahedron_source.md) still applies.
Equivariance on a knot's developing cover, global literature charge
conditions, the actual source/cut comparison and the regulator norm
remain to be established.

## 1. Shared roots and a face frame

Fix N>=2, q=exp(pi*i/N), Q=q^2, and lambda_0=-q. Thus

    lambda_0^2=Q, lambda_0^N=(-1)^(N-1).

On a finite affine flag chart choose distinct nonzero p_i=A_i^N.
Orient each edge once and choose B_ij^N=p_i-p_j on that orientation.
Define the reverse root by B_ji=q B_ij. Consequently, for an
arbitrary ordered edge,

    r_ij=B_ji/B_ij is q or q^(-1), r_ji=r_ij^(-1).     (1.1)

The reversal prescription is made once per edge, not afresh on each
triangle. It does not prescribe B_ji=q B_ij in both directions.

For f=(i,j,k), the actual relative endpoint module has generators

    D_f^N=lambda_f=(p_i-p_k)/(p_j-p_k),
    Y_f=(v_f-u_f D_f)sigma^(-1),
    u_f=A_j/A_k, v_f=A_i/A_k.

Here sigma(D_f)=Q D_f. Put

    beta_f=B_ik/B_jk,
    rho_f=(A_j/A_i) beta_f,
    a_f=(A_k/A_i) B_ji/B_jk,
    nu_f=B_ji/B_jk.                                  (1.2)

Then rho_f^N=t_f=(p_j/p_i)lambda_f and a_f^N=1-t_f.
All these quantities and their indicated factorials are nonzero.
Define

    phi_f(n)=(Q rho_f;Q)_n/a_f^n,
    H(beta)_(a,b)=(beta Q^a)^b,
    G_f=diag(phi_f^(-1)) H(beta_f).                    (1.3)

The factorial is periodic in n. Let Z e_n=Q^n e_n and
S e_n=e_(n+1). Direct evaluation gives

    G_f D_f G_f^(-1)=beta_f Z,
    G_f Y_f G_f^(-1)=nu_f S.                          (1.4)

Indeed H(beta) evaluates polynomials at beta Q^a. In that basis
Y_f is (v_f-u_f beta_f Z)S. The adjacent ratio
phi_f(a)/phi_f(a-1)=(1-rho_f Q^a)/a_f cancels this coefficient
and leaves v_f a_f=nu_f. Thus the same G_f works regardless of
which tetrahedron contains the ordered face.

## 2. The actual face pairing is a fixed Gaussian times a fixed scalar

Write bar f=(k,j,i). Let M_f be the actual pairing induced from
the shared endpoint caps and pointed fusion maps, as in the
[relative pivotal proof](relative_pivotal_duality.md). Its scalar
is already fixed by those caps. In the new frames its matrix is

    M_f^st=G_f^(-t) M_f G_(bar f)^(-1).                (2.1)

The proved reversal anti-map on the raw relative generators is

    a(D)=-Y^(-1)D, a(Y)=QY^(-1).

Substitute (1.4), retaining transpose and generator order. With
c_f=-r_ik^(-1), the resulting two equations are

    M_f^st S=Q S M_f^st,
    M_f^st Z=c_f Z S M_f^st.                         (2.2)

They determine every matrix entry from its (0,0) entry. Namely

    M_f^st=mu_f Mcal_f, mu_f=(M_f^st)_(0,0),
    Mcal_f(a,b)=Q^b c_f^n Q^(n(n+1)/2),
    n=a-b mod N.                                    (2.3)

For a direct proof, the first equation gives M_(a,b)=Q^b F_(a-b).
The second gives F_n=c_f Q^n F_(n-1). Its cyclic consistency is
c_f^N Q^(N(N+1)/2)=1. This proves (2.3) at every parity, without
dividing by two modulo N. The Gaussian is a product of two
invertible diagonal matrices and the Fourier matrix (Q^(-ab)).
Since the original pairing is invertible, mu_f is nonzero.

If r_ik=q, (2.3) is equivalently

    Mcal_f(a,b)=Q^b lambda_0^((a-b)^2).

If r_ik=q^(-1), it is the transpose of this matrix. Thus its
entire matrix dependence on the flag parameters has disappeared;
mu_f is the actual remaining scalar function. It is not set to one.

## 3. The corrected cyclic map has the same property

Write r f=(j,k,i). The preceding oriented-source proof constructed
the actual cyclic map

    U_f=tau_N lambda_f L_f D_f^(-1), tau_N^3=Q,

with exact cyclic and pairing coherence. Define

    U_f^st=G_(r f) U_f G_f^(-1).

Its raw generator equations are
D_(r f) U_f=-Q U_f D_f^(-1)Y_f and
Y_(r f) U_f=Q U_f D_f^(-1). Therefore (1.4) gives

    Z U_f^st=crot_f U_f^st Z^(-1)S,
    S U_f^st=drot_f U_f^st Z^(-1),
    crot_f=-Q r_ik, drot_f=Q r_ik/r_jk.               (3.1)

Solving the entry recurrences yields

    U_f^st=xi_f Ucal_f, xi_f=(U_f^st)_(0,0),
    Ucal_f(a,b)=drot_f^(-a) crot_f^(-b)
                            Q^(ab+b(b+1)/2).         (3.2)

The second equation of (3.1) first gives
U_(a,b)=drot_f^(-a)Q^(ab) U_(0,b). The first then gives
U_(0,b+1)=crot_f^(-1)Q^(b+1)U_(0,b). These are precisely (3.2).
Again Ucal_f is a diagonal--Fourier--diagonal product and
xi_f is nonzero. The chosen tau_N is retained in xi_f.

Conjugating the already proved identities gives

    U_(r^2 f)^st U_(r f)^st U_f^st=I,
    (U_f^st)^t M_(r f)^st (U_(i,k,j)^st)^(-1)=M_f^st.
                                                        (3.3)

Thus the scalar functions in (2.3) and (3.2) obey the exact
coherence relations forced by the Gaussian products. They are
not independent normalizations assigned at the end of each move.

## 4. A standard kernel for every ordered tetrahedron

For an ordered tetrahedron (i,j,k,l), name its faces

    A=(i,k,l), B=(i,j,k), C=(i,j,l), D=(j,k,l).

Use their shared roots from (1.2). They satisfy rho_A=rho_C rho_D.
Put

    alpha=rho_C, beta=rho_D, eta=rho_A,
    gamma=a_A/a_D, v=a_C/a_A, u=alpha/gamma.

Then u^N+v^N=1. Define the marked integers e,d modulo N by

    Q^e=gamma/rho_B=r_ik/r_jk,
    Q^d=-lambda_0 gamma beta v/a_B=q/r_jk.            (4.1)

The first root defect uses the edges ik and jk; it does not
use ij. Since every r is q or q^(-1), e is 0,1 or -1 and
d is 0 or 1 modulo N. These are explicit orientation data.

The central standard shape has the projective expression

    u^N=(p_i-p_l)(p_k-p_j)/((p_j-p_l)(p_k-p_i)).       (4.1a)

With the convention r(infinity,0,1,z)=z used in the crossing
fundamental-cycle note, (4.1a) is r(p_i,p_j,p_k,p_l)^(-1).
The reciprocal and the corresponding oriented tetrahedron order
must be carried into any regulator comparison. They cannot be
removed by calling both coordinates the geometric shape. The
formula concerns the root center at fixed N; it does not specify
the quantum-parameter trajectory of a selected period across N.

Let R_raw be the actual pointed fusion of the raw face modules
C and D, with total face A and relative face B. Let P exchange
the total and relative input factors. The exact shared-frame
formula is

    (G_C tensor G_D) R_raw
              (G_A^(-1) tensor G_B^(-1)) P
       =kappa phi_B(e) L0(u,v)(Z^d S^(-e) tensor I),

    kappa=(1/N)sum_(b=0)^(N-1)
                     gamma^(-b)(Q eta;Q)_b/(Q beta;Q)_b.
                                                        (4.2)

Here kappa is the nonzero unit-fixed scalar from the preceding
local comparison. At odd N, L0 is exactly the published basic
matrix kernel without its h(u) prefactor. At every N it is the
same existing pointed-fusion expression

    L0_(k,l)^(i,j)=Q^(kj)lambda_0^(k^2)
                    Omega(u,v|i-k) delta_(i+j,l).

This all-level expression does not extend the literature's
odd-level charge definition by dividing by two at even N.

Here is a direct derivation of (4.2). Normalize each raw endpoint
module by X_tilde=(u_f/v_f)D_f and Y_tilde=Y_f/v_f. The polynomial
basis change diag((u_f/v_f)^n) sends this normalized module to the
raw one. These changes intertwine both the total and relative
generators of the fusion, so the preceding four-frame comparison
applies with parameters s=rho_C^N,t=rho_D^N.

The total and two output factors then cancel against the shared
face frames. The natural relative evaluation root is gamma rather
than rho_B, so its evaluation map differs by S^(-e). Its remaining
diagonal entry at k is

    D_gamma(k) lambda_0^(-k^2) phi_B(k+e),
    D_gamma(k)=(beta v)^k /
                    product_(j=1)^k(1-gamma^(-1)Q^(-j)).

Periodicity and finite-product cancellation give

    phi_B(k+e)=phi_B(e)(Q gamma;Q)_k/a_B^k,
    product_(j=1)^k(1-gamma^(-1)Q^(-j))
         =(-gamma)^(-k)Q^(-k(k+1)/2)(Q gamma;Q)_k.

Consequently that entry is exactly

    phi_B(e)(-lambda_0 gamma beta v/a_B)^k
       =phi_B(e)Q^(dk).

This proves the whole clock/shift factor and its scalar, including
at even and composite levels. If the tetrahedron order agrees
with all its edge orientations, e=d=0 and (4.2) is kappa L0.

## 5. The scalar line and source evaluation are retained

The scalar functions can be evaluated by the specified (0,0)
entries; their determinant equations also give exact norm data:

    mu_f^N=det M_f /
                  (det G_f det G_(bar f) det Mcal_f),
    xi_f^N=(det G_(r f) det U_f) /
                  (det G_f det Ucal_f).                 (5.1)

These equations do not authorize new phase choices. The original
caps and trivalent tensors determine mu_f and xi_f themselves.
For the normalized literature kernel L=h(u)L0, the multiplier in
(4.2) is kappa phi_B(e)/h(u), with exactly the same Weyl insertion.
Full integer-charge lifts and their non-phase multipliers remain
as in the preceding comparison note.

For any already specified finite contraction, (1.3), (2.1) and
(3.2) are honest changes of bases. All interior inverse frames
cancel. A source column p changes to G_f p; its cut row changes
to ell G_f^(-1). A raw unit is therefore the generally nonconstant
column (phi_f(n)^(-1))_n, not a new unit in the standard coordinates.
At a source wall, the lattice and its normal quotient must move
with the frame, using the retained carry/linking constructions.

These observations prove preservation of a given contraction.
They do not construct that contraction on an arbitrary positive
geometric triangulation. Projective/deck equivariance, the global
charge constraints, its actual source extension and selected cut
must still be matched. In particular the fixed Gaussian matrices
above have not been declared equal to a published choice with its
scalar normalizations omitted.

The audited ideal triangulation theorem supplies the desired
geometric developing flags and marked fundamental-class period.
This note supplies shared face algebra for a proposed quantum
comparison. Equality of the actual and triangulation source
classes, integral pointings and regulator norms does not follow
from either existence statement alone.

The subsequent [source-flag proof](source_flag_transport.md) makes
the origin an extra marked point. Its finite-source transports
are fixed by actual edge duality and preserve fusion, caps and
cyclic maps exactly. It also expresses the normal chart and its
non-scalar first coefficient as jets of that same source family.
This supplies more of the local source comparison; the genuine
degenerate edge lattice and selected global norm remain necessary.

## 6. Independent finite-field audit

[The audit](../experiments/audit_standard_face_gluing.py) constructs
four distinct affine flags and roots of all six edge differences
in exact finite fields. For each N=2,3,4,5,6,9, it checks the
24 ordered face pairings and cyclic maps against (2.3),(3.2),
retaining their actual scalars, and all 24 ordered tetrahedron
identities (4.2), including the two root-defect formulas (4.1).
Thus 144 pairings, 144 cyclic maps and 144 full ordered kernels
passed. [Results](../experiments/standard_face_gluing_results.json).
The uniform proofs above are separate from these finite tests.

    python3 experiments/audit_standard_face_gluing.py
