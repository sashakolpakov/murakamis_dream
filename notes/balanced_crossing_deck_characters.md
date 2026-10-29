# Exact deck characters of the original four-function crossing

28 October 2026. The exact balanced Fourier crossing has a specified
continuation away from its sampling grids. Its four full-turn
characters are explicit rational functions of the central coordinates.
They compute the logarithmic seams in a contour deformation of the
original period. A function that is periodic at the original grid
need not remain periodic between the grid points.

This calculation uses the full function, its Gaussian and every affine
logarithmic mark. It does not infer a geometric cycle from a rational
character or identify the central variety below with the knot A-curve.

## 1. The fixed continuation and its four characters

Use the EXACT kernel (14) of
[the balanced crossing theorem](actual_balanced_fourier_crossing_kernel.md).
Put h=2*pi*i/N, t=2*pi*i, X=pi*i-h/2, x=exp(X), s=x^N,
and retain the port logarithms a,b,c,d. In particular s=(-1)^(N+1).
Let

    A=exp(Na), B=exp(Nb), C=exp(Nc), D=exp(Nd),
    beta=b-a-X, f=d-c-X, rho=c-a,
    lambda=d-b+t, G=d-a-X, H=b-c+X,
    E=N f+(N+1)lambda/2+(G H+lambda^2/2)/h.

The full continuation is

    M=constant * (C/A)(1-C/A)^2 exp(E)
       *Psi(beta)Psi(h-f)Psi(lambda+t+h)/Psi(rho).       (1)

The constant includes the original kappa*zeta_0^2/N. The old central
parameters are used as the values of these exponentials, rather than
replacing exp(Nrho) by a new independent constant off the grid.

For a full positive turn of the indicated port, the exact ratios are

    M(a+t,b,c,d)/M = mu_a = s C(A-sB)/[B(A-C)],
    M(a,b+t,c,d)/M = mu_b = s(D-B)/(A-sB),
    M(a,b,c+t,d)/M = mu_c = s(A-C)/(D-sC),
    M(a,b,c,d+t)/M = mu_d = s B(D-sC)/[C(D-B)].         (2)

These are meromorphic identities on the retained logarithmic cover;
the displayed quotients are first interpreted where all factors are
regular. No imaginary part is reset to a principal argument.

Proof: the full function obeys

    Psi(z+t)/Psi(z)=1/(1-exp(Nz)),
    Psi(z-t)/Psi(z)=1-exp(Nz).

The four exponential arguments in (1) have central values

    U=sB/A, V=sC/D, W=D/B, R=C/A.

The Gaussian factors exp(Delta E), for turns in a,b,c,d respectively,
are

    sC/B, -U, sA/D, -sD/C.                         (3)

For example a turn in b has
Delta E=-(N+1)t/2+N G-N lambda+Nt/2
        =-t/2+N(beta-t),
so its factor is -U, including the half-turn sign. Combining (3)
with the four full-function multipliers gives (2). Thus neither a
Gaussian phase nor a complete-color sign was dropped.

## 2. Balanced grids and their off-grid seams

On the local sampling multisection C=sB, D=sA all four characters
equal one. More precisely,

    mu_a-1 = A(sC-B)/[B(A-C)],
    mu_b-1 = (sD-A)/(A-sB),
    mu_c-1 = (sA-D)/(D-sC),
    mu_d-1 = D(sB-C)/[C(D-B)].                     (4)

Hence, on this regular chart, the simultaneous unit-character
locus is EXACTLY C=sB, D=sA. The converse follows from the first
two numerators, since A,B are nonzero. The other two equations
are redundant. Also

    mu_a mu_b mu_c mu_d=1.                         (5)

This is the common-scale symmetry, not four independent gluing
equations. All four shifts commute because the characters depend
only on A,B,C,D, which are invariant under full logarithmic turns.

For example, start with a balanced grid (A0,B,C,D), C=sB and
D=sA0, and vary only its a-port away from A=A0. Then mu_a=1
still, but

    mu_b-1=(A0-A)/(A-sB),
    mu_c-1=s(A-A0)/(D-sC).

The other ports acquire seams. Periodicity in the moved port alone
therefore does not justify a simultaneous closed-torus deformation.
These formulas locate the exact central differences that recur in
the [wire-current calculation](whole_fermat_toric_residue_and_wire_source.md).

## 3. Sewn characters and the limitation of grid periodicity

For an internal variable shared by two original crossing ports,
the full-turn ratio of the product is the product of its two
characters from (2), with the orientations and negative-crossing
conjugate transport retained. The rational boundary co-source is
single-valued in that variable; it adds no logarithmic multiplier.
Thus the sewn scalar form has a directly computable rational deck
character nu_e. On the propagated balanced central multisection,
nu_e=1 because each incident local character is one.

Off that multisection, imposing nu_e=1 is a NONTRIVIAL equation,
not a consequence of the Fourier frame change. A logarithmic
branch lip contributes a multiple of (nu_e-1) times the complete
kernel. Such a lip cannot be omitted on the grounds that its
value at the root grid is zero. In particular, zeros on the grid
may cancel the grid denominator and leave a regular but nonzero
relative source term. The exact Newton/Rogers examples in the
linked wire note exhibit that mechanism.

The open-braid frame theorem now removes all interior frame adapters,
but it does not remove the logarithmic seams of this off-grid full
continuation. The characters (2) specify those seams without an
unspecified torsor multiplier. Geometric selection still requires
an actual relative-period transformation, with these terms retained.

## 4. Verification

[The independent finite-product audit](../experiments/audit_balanced_crossing_deck_characters.py)
computes Psi from its rational product and dilogarithm definition,
then checks every full-turn ratio at both parities, without applying
the shift law in the evaluator. Symbolic checks verify (4), (5),
and the unit-character locus. These checks supplement the uniform
calculation (2)--(3); they are not a knot volume test.
