# Casimir braiding through the recoupling lattice

Research note, 25 October 2026. This identifies the actual Kashaev-color
crossing inside the regular representation and recoupling lattices of
[the preceding note](cyclic_steinberg_lattice.md). The identities hold
at every N>=2. The crossing is the literature R-matrix already fixed in
[the direct crossing audit](kashaev_crossing_and_period_lattice.md),
not a newly chosen quantization. The proofs below are elementary tensor
and interpolation calculations; no quantum-topology theorem is imported.

## 1. The product-coordinate injection is a quantum-group map

Keep q=exp(pi*i/N), omega=q^2, rho=q-q^(-1), kappa=-q. On
E_t=C[x]/(x^N-t), let X=x and sigma f(x)=f(omega*x). For any positive
integer b define a regular quantum-group representation by

    F_b=(1-X)sigma^(-1), K_b=kappa^(-b) X^(-1),
    E_b=kappa^(-b-1)(X^(-1)-omega^b)sigma/rho^2.     (1.1)

The b=1 representation is the preceding cyclic/Steinberg family.
Direct multiplication verifies the quantum-group relations. Its
normalized Casimir and central powers are

    Omega_b=rho^2 F_b E_b+qK_b+q^(-1)K_b^(-1)
                  =-(kappa^(b-1)+kappa^(1-b)),
    F_b^N=1-t, K_b^N=kappa^(-bN)/t,
    E_b^N=kappa^(-bN)(1-t)/(t*rho^(2N)).             (1.2)

In the ordered tensor product of b copies of the b=1 family, scale
factor j by F_j -> c_j F_j, E_j -> c_j^(-1)E_j, with
c_j=kappa^(1-j), leaving K_j unchanged. Use the standard coproduct

    Delta F=F tensor 1+K^(-1) tensor F,
    Delta E=E tensor K+1 tensor E.

Then the injection m:f(x)->f(w), w=x_1...x_b, intertwines the full
quantum-group action with (1.1), not just its Borel part. The F and
K formulas are the preceding endpoint calculation. For E, every term
shifts w by omega, while its coefficient telescopes:

    rho^2 E_tot 1
       =sum_(j=1)^b kappa^(2j-b-1)
           (omega^(-1)x_j^(-1)-1)/(x_(j+1)...x_b)
       =kappa^(-b-1)(w^(-1)-omega^b).                (1.3)

For the second equality use kappa^2=omega; adjacent suffix products
cancel. Applying the same calculation to f(w) proves the assertion.
All formulas are regular at t_1=...=t_b=1. The source representation
can be reducible at this fiber when b>1; no simplicity assertion for
these higher-b colors is needed.

This completes the E-action comparison left open in the preceding
note for this injection. It does not identify every cyclic tensor
with a braided quantum-group tensor category.

## 2. The tensor Casimir on the relative recoupling factor

For two factors with parameters s,t and c_1=1,c_2=kappa^(-1), put

    Y_i=F_i, X_tot=X_1X_2, Y_tot=Y_1+X_1Y_2,
    Z=Y_1Y_2^(-1), D=X_1+Z, C=ZX_2,
    tau=(1-st)/(1-t).

Let CG be the pointed factorization
E_(st) tensor E_tau -> E_s tensor E_t. In these coordinates

    K_tot=kappa^(-2) X_tot^(-1),
    E_tot=kappa^(-1)E_1 X_2^(-1)+kappa E_2.

An ordered multiplication gives

    rho^2 Y_tot E_tot
       =kappa^(-1) D Z^(-1)(X_1+X_1^(-1)-2)X_2^(-1)
                      +kappa D(X_2+X_2^(-1)-2).

Adding qK_tot+q^(-1)K_tot^(-1) and using DC=omega CD yields

    Omega_tot=kappa^(-1)C^(-1)(D-1)^2+kappa C-2kappa D.

The relative generators are X_rel=D,Y_rel=-C. On E_tau write
X_rel=d and Y_rel=(1-d)sigma^(-1). The last formula is

    H_tau=q^(-1)(1-omega*d)sigma
                    +q(1-d)sigma^(-1)+2q*d,
    Omega_tot CG=CG (1 tensor H_tau).                (2.1)

Although the intermediate formula in C used an inverse, H_tau is
regular in tau. On the monomial basis its complete action is

    H_tau d^j=h_j d^j+a_j d^(j+1),
    h_j=q^(2j-1)+q^(1-2j),
    a_j=q(2-omega^j-omega^(-j)), d^N=tau.             (2.2)

Here a_0=0 and every a_j with 1<=j<N is nonzero. The basis chain
d,d^2,...,d^(N-1),1 therefore shows that H_tau is cyclic for tau!=0.
Its characteristic and minimal polynomial are both

    P_N(z)=T_N(z)+2,
    T_0=2, T_1=z, T_(j+1)=z T_j-T_(j-1).            (2.3)

Indeed the characteristic polynomial is product_j(z-h_j), and
h_j=u+u^(-1) with u^N=-1. This proves (2.3). The distinct roots
have multiplicity two, apart from the simple root -2 when N is odd.
The corresponding repeated eigenvalues have a size-two Jordan block.
The commutant of H_tau is exactly C[H_tau], of dimension N: a
commuting operator is determined by its value on a cyclic vector.

## 3. The actual crossing has a unique confluent polynomial

Let R_N be the finite highest-weight universal R used in the crossing
audit, and put B_N=P R_N. The version P R_N^T in the original audit
is its already proved self-dual conjugate. Let

    lambda_0=q^((N-1)^2/2),
    c_k=q^(2k+1)+q^(-2k-1),
    nu_k=(-1)^k q^(k(k+1)),
                     0<=k<=floor((N-1)/2).

There is a unique polynomial r_N of degree less than N with

    r_N(c_k)=nu_k,
    r_N'(c_k)=-nu_k*(N-1-2k)
                       /[2(q^(2k+1)-q^(-2k-1))]     (3.1)

whenever 2k+1<N. At the one simple root, when present, only its
value is specified. The total number of conditions is N. The nodes
are distinct after pairing; confluent Vandermonde interpolation is
invertible. All coefficients lie in Q(q).

**Crossing identity.** On the actual N-dimensional Kashaev color,

    B_N=lambda_0 r_N(Omega_tot).                     (3.2)

Here Omega_tot uses the ordinary, unscaled tensor factors. Constant
factorwise E,F scalings conjugate both sides in the same way.

### Direct proof from the defining finite R

Use a generic parameter z first, with m=N-1 and color

    K v_j=z^(m-2j)v_j,
    E v_j=[j]_z[m-j+1]_z v_(j-1), F v_j=v_(j+1).

At total weight 2m-2k the highest vector is
h_k=sum_(a=0)^k b_a v_a tensor v_(k-a), with b_0=1. Its E-equation
gives

    b_(a+1)/b_a=-[k-a]_z[m-k+a+1]_z
                    /([a+1]_z[m-a]_z*z^(m-2k+2a+2)),
    b_k=(-1)^k z^(-k(m-k+1)).

The generated irreducible module has dimension 2m-2k+1. One elementary
check uses E F^r h=[r]_z[2m-2k-r+1]_z F^(r-1)h. These coefficients
force nonvanishing through that dimension and rule out a negative
highest-weight vector in a finite module with nilpotent F. The
Casimir eigenvalues z^(2N-1-2k)+z^(-2N+1+2k) are distinct generically,
and the dimensions sum to N^2. This proves the direct sum without
assuming a tensor-decomposition theorem.

The defining finite R is triangular. The coefficient of v_0 tensor
v_k in P R h_k can only come from its zero-th term on v_k tensor v_0.
Consequently its scalar on this summand is

    lambda_k(z)=(-1)^k z^((N-1)^2/2-k(2N-1-k)).

Intertwining, already checked from the R-coefficient recurrence in
the crossing note, then gives a degree-less-than-N polynomial in
the tensor Casimir by ordinary interpolation.

At z=q the nodes k and l=N-1-k collide and their lambda values agree.
Set h=2k+1<N, A=q^h-q^(-h). Differentiation with respect to log z gives

    d(c_k(z)-c_l(z))/dlog z=-2N*A,
    d(lambda_k(z)-lambda_l(z))/dlog z
                              =lambda_k(q)*N*(N-h).

Dividing gives precisely the derivative in (3.1). Replace each pair
of interpolation rows by its value row and divided-difference row.
The resulting system tends to an invertible confluent Vandermonde
matrix. Thus its coefficients are regular and specialize to (3.1).
The finite R is also regular here, since [j]_q! is nonzero for j<N.
Specializing the matrix identity proves (3.2), including its nilpotent
part. This is an algebraic specialization of the prescribed R.

## 4. Inverse crossing, pointing, and the exact writhe phase

Since every nu_k is nonzero, r_N is a unit modulo P_N. Its inverse
polynomial r_N^minus is uniquely specified by

    r_N^minus(c_k)=nu_k^(-1),
    (r_N^minus)'(c_k)=-r_N'(c_k)/nu_k^2.              (4.1)

Thus B_N^(-1)=lambda_0^(-1)r_N^minus(Omega_tot). Dropping the
derivative conditions would give an incorrect crossing: P_N has
double roots, not merely a set of distinct central characters.

On the product-coordinate quantum-group submodule of Section 1,
Omega_tot=q+q^(-1)=c_0. After the corresponding factorwise conjugation,
B_N therefore acts on its vacuum and entire submodule by exactly
lambda_0. The original enhancement uses

    alpha_N=q^((N^2-1)/2), lambda_0/alpha_N=-q=kappa.

For a b-strand knot braid beta of writhe w, the self-dual standard
convention therefore gives the exact scalar cut-period formula

    <K>_N=kappa^w * cut_trace[ rho_r(beta)
                                   (1 tensor K tensor ... tensor K) ],

    rho_r(sigma_i)=r_N(Omega_(i,i+1)),
    rho_r(sigma_i^(-1))=r_N^minus(Omega_(i,i+1)).       (4.2)

The cut trace is the scalar open-strand operator, as in the original
crossing audit. The pivotal K becomes K^(-1) under the stated duality;
these conventions give the same scalar. The writhe phase kappa^w
has not been discarded. Formula (4.2) is an alternative algebraic
presentation of the existing invariant for every knot and every level.
It supplies no different definition of what the invariant means.

## 5. Braiding acts on the transported recoupling lattice

Use A=C(a,b)[[eps]], s=1-eps*a, t=1-eps*b as before, with a,b,a+b
nonzero. Let Lambda_out be the regular basic tensor lattice and set

    Lambda_in^int=CG^(-1) Lambda_out.

This is a free rank-N^2 lattice. The preceding Smith theorem gives
Lambda_in^int contained in the basic source lattice. Since Omega_tot
is regular on Lambda_out, (2.1) proves that 1 tensor H_tau preserves
Lambda_in^int. Its polynomial r_N and inverse polynomial preserve it
as well. Transport by CG and specialization then give exactly B_N
and B_N^(-1) on the nilpotent tensor fiber, with the factor lambda_0
and its inverse. This identifies both actual crossings through the
singular lattice; there is no arbitrary scalar chosen at that fiber.

There is an explicit check without an unspecified regularization.
In the evaluated product coordinate w_i, let r_i=[-i]_N, with r_0=N.
The integral source frame multiplies columns d=1,...,r_i-1 by eps.
Formula (2.2) shows immediately that H_tau preserves this frame:
the only arrow crossing from an unscaled to a scaled column would
be the zero arrow a_0. The arrow from d=r_i-1 to d=r_i vanishes on
the special fiber; for r_i=N this is the wrap arrow to 1. All other
arrows retain their recorded coefficients, with tau_0=(a+b)/b.
The scaled CG block has a unit determinant, so this computes the
nilpotent crossing on an actual integral basis.

This is an endomorphism lift r_N(Omega_tot) on the cyclic deformation.
It is not asserted to swap two distinct cyclic parameters or satisfy
a generic braided-category structure away from the nilpotent fiber.
No such assertion is needed for the specialization identity.

The later [regular holonomy-braiding construction](regular_holonomy_braiding.md)
addresses local generic transport with different data: its rational
automorphism changes the individual unrestricted central characters
by the holonomy map. Its regular module and anchored Hom line
specialize to the actual crossing. That result does not assert a
generic Yang--Baxter identity for the fixed polynomial r_N used here.

The subsequent [common carry-lattice theorem](carry_recoupling_lattice.md)
extends the integral transport to arbitrary finite recoupling
trees and the complete meridian cut family. Its proof uses
the explicit whole-tree factorial kernel and carry valuations,
rather than only this two-factor spectral polynomial. A
specified wrapped lift retains the crossing's wall terms and
has the original ADO trace. The transported cut insertion is
kept as a full matrix. This gives recoupling path independence
through degeneration without asserting a generic braid relation
for that auxiliary lift or a geometric regulator identification.

## 6. What the derivative data do and do not prove

For the specified complex root, |nu_k|=1, while

    |r_N'(c_k)|=(N-1-2k)/(4 sin(pi*(2k+1)/N))
                                      <=N^2/8.       (6.1)

Use sin(pi/N)>=2/N. These are bounds on the spectral jets. They
are not bounds on the crossing in every basis or on a closed knot
period. Recoupling frames and the cut pairing may have large norms;
contractions retain phase cancellation. Thus replacing the spectral
jet data by their magnitudes would not prove the volume conjecture.

The new comparison is that actual crossing operators, including their
nonsemisimple parts, are now defined on the same transported local
lattice as the cyclic recoupling construction. The geometric
fundamental-class period and its norm remain to be identified with
the cut pairing in (4.2). No new knot-class volume theorem is inferred.

The subsequent [actual meridian calculation](meridian_casimir_source.md)
derives the same confluent polynomial from the actual color M,
rather than varying q. Its generic tensor spectrum is
c_j=q^(-2j-1)M^2+q^(2j+1)M^(-2), with crossing values
nu_j M^(-2j). A canonical tensor meridian intertwiner gives
an affine shift with source (1+M^(-2N))E_(N-1). Its complete
projector residue is a fixed multiple of the actual cup/cap.
Thus the spectral jet above has an explicit meridian origin.
In the actual nilpotent tensor the c_0 nilpotent has rank one;
its generalized eigenspace has dimension 2N. No free-rank-N
dual-number module at that special fiber is inferred from
the generic cyclic relative representation. The full knot
source and regulator comparison still require construction.

## 7. The normalization torsor has a nonreduced spectral base

There is a precise algebra behind the derivative data. Put

    A_N=C[z]/P_N(z).

The cyclicity in Section 2 makes E_tau a free rank-one A_N-module,
with cyclic generator d. The Chinese remainder theorem gives

    A_N = product_(double nodes c) C[epsilon_c]/epsilon_c^2
                         times C if N is odd.        (7.1)

Consequently its frame torsor has structure group A_N^*, not just
one G_m. Its units include both residue scalars and the additive
jet factors 1+b_c*epsilon_c. The crossing polynomial is the unit
whose factors are nu_k+r_N'(c_k)*epsilon_c. The derivative is actual
representation data and cannot be recovered from its residue value.

The vacuum has a particularly simple integral formula. Let

    B_N(z)=P_N(z)/(z-c_0), c_0=q+q^(-1).

Then, as an exact identity in E_tau,

    B_N(H_tau)d = tau*q^(N-1)*N^2 * 1.               (7.2)

Indeed its left side is killed by H_tau-c_0 and hence lies in the
one-dimensional eigenline C*1. The polynomial B_N is monic of
degree N-1. Only the highest power can travel the entire chain from
d to 1, so the coefficient is tau*product_(j=1)^(N-1)a_j. The
two cyclotomic products in a_j=q(1-omega^j)(1-omega^(-j)) each equal
N, which proves (7.2). In particular the factor N^2 and the relative
parameter tau are retained before specialization.

Since c_0 is a double root for every N>=2, the vacuum corresponds
to the socle at that double point: it is killed by z-c_0, but is
itself in the image of multiplication by z-c_0 on that local factor.
It is not a cyclic frame for A_N. Requiring an A_N-module comparison
to fix this vector controls its residue at c_0; it leaves the jet
at c_0 and other spectral factors undetermined. Thus a rigidity
argument for a pointed eigenline alone would miss the crossing's
nonsemisimple data. The prescribed generic-q R determines them by
the confluent calculation in Section 3.

### Hilbert 90 still works with these nilpotents

This extension does not introduce an obstruction to semilinear
descent. More generally let A be a characteristic-zero Artin algebra,
J its nilradical, and S/A a cyclic finite etale algebra of degree n
with generator sigma. Suppose r in S^* has norm one. Solve
r*sigma(f_bar)=f_bar over the reduced algebra by the elementary
Hilbert-90 formula in the intrinsic norm-torsor note, and lift its
unit solution to f_0 in S^*. Put

    a=r*sigma(f_0)/f_0 in 1+J*S,
    L=log(a), sum_(j=0)^(n-1)sigma^j(L)=0,
    h=-(1/n)sum_(j=0)^(n-1) j*sigma^j(L).

The logarithm and exponential are finite nilpotent polynomials.
The telescoping identity (1-sigma)h=L gives

    f=f_0 exp(h), r*sigma(f)=f.                       (7.3)

Solutions form an A^*-torsor. This proves descent of both the residue
and jet data explicitly. It does not select an element of that torsor
from its reduced eigenline pointing alone.

For an intrinsic quantum A-module the same formulation applies when
the generalized spectral module is rank one over its finite spectral
algebra. That hypothesis must be checked; it is proved here for H_tau
by cyclicity. One must not silently replace this algebra by its reduced
curve at a repeated root. The selected global period and its metric
still require a comparison beyond the algebraic frame torsor.

## 8. The actual closing trace is a spectral-jet functional

The pivotal pairing can also be identified exactly on this spectral
algebra. For f in A_N, the partial quantum trace is scalar on the
simple original color V_N. Define Phi_N by

    tr_2[(1 tensor K) f(Omega_tot)] = Phi_N(f)*1.

In terms of the distinct nodes c_k above it is

    Phi_N(f)=-sum_(0<=k, 2k+1<N)
          [c_k f(c_k)+(c_k^2-4) f'(c_k)]
                  + f(-2) if N is odd.               (8.1)

For even N the final term is absent. This is well-defined on A_N:
P_N and its derivative vanish at double nodes, and P_N(-2)=0
at the simple node. Thus closing a strand retains exactly the same
infinitesimal data that the crossing uses. In particular

    Phi_N(1)=0,
    Phi_N(r_N)=kappa^(-1),
    Phi_N(r_N^minus)=kappa.                           (8.2)

The last two equations agree with the original enhancement and
negative enhancement, including their phases. They do not define
a freely chosen positive norm.

Here is an independent derivation. At generic z, use the elementary
tensor decomposition proved in Section 3. Taking the full pivotal
trace, and dividing by the quantum dimension of the open color,
gives the identity

    [N]_z * Phi_z(f)
       =sum_(j=0)^(N-1) [2N-1-2j]_z f(c_j(z)).       (8.3)

The partial trace itself is regular at z=q. The numerator of (8.3)
is divisible by the simple zero [N]_z. Its specialization is therefore
an algebraic first-jet evaluation; no asymptotic theorem is involved.

For a colliding pair, set h=2k+1<N, A=q^h-q^(-h), c=q^h+q^(-h).
The paired dimensions are [2N-h] and [h]. At q their values are
-A/rho and A/rho. Their sum has log-z derivative 2N*c/rho, while
the coefficient of f'(c) in the derivative of the paired numerator
is 2N*A^2/rho. The denominator has derivative -2N/rho. Their quotient
is -c*f(c)-(c^2-4)*f'(c). If N is odd, the unpaired term has dimension
[N] and specializes to f(-2). This proves (8.1). The usual finite-R
enhancement from the crossing audit then gives (8.2); they can also
be checked by substitution in (3.1) and (4.1).

Equation (8.1) identifies the local pivotal contraction, as well as
the crossings, with their actual literature definitions. It does not
turn a general braid word into a product of independent scalar
functions of one Casimir: adjacent pair Casimirs do not commute.
The full recoupling and cut pairing still matter for the global
period and its exponential norm.

## 9. Coverage and verification

Nonsemisimple braid actions on simple projective quantum sl2 modules
are existing theory; for example Karvounis,
[1909.11162](https://arxiv.org/abs/1909.11162), defines such actions using
the R-matrix of a quasitriangular extension. Its proofs are not used
here. No novelty is claimed for projective braid actions or for
polynomial functional calculus. The coverage distinction is important:
we use the prescribed color and enhancement, and do not assume a
braiding on all finite-dimensional unrestricted representations.

`experiments/audit_casimir_braiding.py` independently evaluates the
finite universal R, confluent polynomial, inverse, relative Casimir,
vacuum socle multiplier, nilpotent Hilbert 90, pivotal trace, and
special-fiber lattice blocks at even and composite levels. These
are diagnostics for the uniform proofs above.
