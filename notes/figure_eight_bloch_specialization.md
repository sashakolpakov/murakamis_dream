# Exact actual Bloch calibration of the figure-eight source

Research check, 27 October 2026. This evaluates the original crossing
Bloch class at an exact parabolic representation. It identifies the
marked regulator appearing in the newly proved whole-source formula
without importing a separate two-tetrahedron triangulation of 4_1.

Put

    z=(1+sqrt(-3))/2,   t_Riley=1-z.

The upper-half-plane z is the positive regular ideal shape. The
geometric Riley embedding used by the actual braid is instead the
lower root t_Riley; this distinction fixes the orientation sign.
The marked noncentral parabolic normal form has equation
t^2-t+1=0, as the exact Hurwitz fixed-point calculation verifies.
The complete hyperbolic holonomy is irreducible and parabolic and
therefore occurs among these two conjugate embeddings. The positive
fundamental-class regulator below selects the geometric embedding;
no separate triangulation recognition is needed for that selection.
Use the exact meridians

    A=[1 1;0 1], B=[1 0;t_Riley 1],
    C=A^(-1) B A B^(-1) A,

and the actual framing F=[2 -1;-2 2], corresponding to (r,s)=(2,-2).
Conjugate by F, apply the original prefix/Gauss reconstruction, and
follow the actual four Hurwitz crossings in the order
(sigma_1,sigma_2^(-1),sigma_1,sigma_2^(-1)).

The five-factor shape lists are exactly

| Crossing | Shape list, with signs (+,+,+,-,-) |
| --- | --- |
| Positive | 1, 1, -1, 1, -1 |
| Negative | -1, -1/2, 2z, 1/2, -z |
| Positive | z-1, z, 1, -1, z |
| Negative | 1-z, 1/2, 2, (1-z)/2, 1 |

These lists are calculated in Q(sqrt(-3)) directly from the original
holonomy reconstruction and crossing map. They are not guessed from
an expected volume. The [exact audit](../experiments/audit_figure_eight_bloch_specialization.py)
reproduces them and verifies closure of the physical states.

Some factors in this frame are degenerate. This is a specialization
of the whole normalized idealized configuration chain: repeated-point
tetrahedra are zero, and D(0)=D(1)=D(infinity)=0. Real nondegenerate
arguments also have D=0. The physical Gauss reconstructions are finite.
No Gaussian determinant or individual quantum normalization is
evaluated at this degenerate shape frame.

Consequently the actual total regulator is

    D_actual=D(2z)-D(-z)+D(z-1)
                      +D(1-z)-D((1-z)/2)
            =2D(z/2)-2D(-z)-D(z).               (1)

For the second equality, use z-1=-conjugate(z), 1-z=conjugate(z),
2z=1/(conjugate(z)/2), conjugation reverses D, and inversion also
reverses D.

This last expression can be evaluated by elementary Lobachevsky
identities. Let Lambda(theta)=-integral_0^theta log(2sin u)du. For
an upper-half-plane cross-ratio w, the triangle with vertices 0,1,w
has angles alpha,beta,gamma, and

    D(w)=Lambda(alpha)+Lambda(beta)+Lambda(gamma). (2)

One can verify (2) directly: the sine rule gives
log|w|=log(sin beta/sin gamma) and
log|1-w|=log(sin alpha/sin gamma). Differentiating both sides using
dD=log|w| dArg(1-w)-log|1-w| dArg w gives equality; their real
degenerate boundary values fix the constant.

The relevant angle triples are

    z:            (pi/3,pi/3,pi/3),
    z/2:          (pi/3,pi/6,pi/2),
    -conjugate(z):(2pi/3,pi/6,pi/6).

The elementary symmetry Lambda(pi-theta)=-Lambda(theta), the value
Lambda(pi/2)=0, and duplication give

    2Lambda(pi/6)=3Lambda(pi/3).

For example duplication follows by differentiating
Lambda(2theta)=2Lambda(theta)+2Lambda(theta+pi/2), and setting
theta=pi/6. Equation (2) now yields

    D(z)=3Lambda(pi/3),
    D(z/2)=5D(z)/6,   D(-z)=-2D(z)/3.

Substitution in (1) proves the exact marked evaluation

    D_actual=2D(z)=6Lambda(pi/3)=4Lambda(pi/6).  (3)

The already proved actual-crossing fundamental-class theorem
identifies D_actual with the oriented hyperbolic volume. Thus (3)
is the marked volume normalization of the selected source formula,
with no separate triangulation-identification input in this case.

There is also an exact check of the algebraic selected coefficient.
The earlier principal residue is

    rho_4=-1/(2t_Riley-1)=1/sqrt(-3),
    sqrt(|rho_4|)=3^(-1/4).

The discrete Laplace coefficient from the actual positive source
has this same modulus. Its first correction is

    11pi/(36sqrt(3)N)=(11/36) rho_4 h_N,
    h_N=pi*i/N.

In H=Log Q=2h the corresponding coefficient is (11/72)rho_4.
These are consistency checks with the marked algebraic density;
the selection and asymptotic in this prototype are proved from the
whole finite source identity, not inferred from this numerical match.

[Audit results](../experiments/figure_eight_bloch_specialization_results.json).
