# A joint complex packet in the deficient geometric chamber

30 October 2026. Independently reviewed. The actual monic
q-Hahn numerator has an N-independent joint complex-degree and
magnetic corridor around the real deficient frame. Both its selected
root amplitude and its genuine generic-q numerator derivatives are
controlled there. The proof uses the original finite determinant,
an explicitly bounded low block, and a positive tail matrix.

This does not continue the full exceptional operator's generic
boundary factors or select a nonzero global period. The original
forbidden integer-degree slices remain identically zero.

## 1. The finite determinant and the joint domain

Fix

    0<sigma_*<kappa<alpha_0<1/2.

Put theta=pi/N, a/N=alpha in [alpha_0,1/2], with the actual integer
channel 0<=a<=floor((N-1)/2). The degree t=N sigma may be complex.
Use the ORIGINAL root monic numerator R_a(z;c) from the joint source
theorem, with

    c=-cos(pi(sigma+1/N)), C=-c,
    d_n=1/[cos(n theta)cos((n+1)theta)],
    b_n=sin(n theta)/[cos(n theta)
              sqrt(sin((2n-1)theta)sin((2n+1)theta))].        (1)

Its exact recurrence is

    R_0=1, R_1=z-C d_0,
    R_(n+1)=(z-C d_n)R_n
                   -b_n^2[C^2-cos^2(n theta)]R_(n-1).       (2)

No physical integer-degree assumption is used in (2): it is the
already proved polynomial identity for the literal finite Newton
numerator, for every complex degree.

For each fixed sufficiently small angle vartheta>0 there are
epsilon>0 and R>1, independent of N and a, such that R_a has no
zeros on the PRODUCT domain

    |sigma-sigma_*|<epsilon,
    Omega_R={z: |z|>R,
                   vartheta<Arg z<2pi-vartheta}.             (3)

Here Arg is the logarithm cut on the positive real axis. Both
epsilon and R may depend on vartheta; R can be chosen O(1/sin
vartheta), while epsilon can be chosen proportional to vartheta.
All statements below concern sufficiently large N and fixed
compact subsets of (3), uniformly in the allowed discrete channels.

## 2. A positive tail plus a bounded error

Choose m=floor(kappa N), so 0<m<a for large N. In the determinant
matrix with characteristic polynomial (2), take indices 0,...,m-1
as a low block. Its diagonal entries are C d_n; take its upper
entries to be 1 and its lower entries to be
b_n^2(C^2-cos^2(n theta)). These entries and their C derivatives
are uniformly bounded. Indeed n/N<=kappa+o(1)<1/2, and

    b_n cos^2(n theta)
       =sin(2n theta)/[2 sqrt(sin((2n-1)theta)
                                  sin((2n+1)theta))]<=1.     (4)

The last inequality holds throughout the used range, for N>=5:
sin(2n theta)>=sin(2theta), and
sin((2n-1)theta)sin((2n+1)theta)
=sin^2(2n theta)-sin^2(theta). Thus the low block J_L has
operator norm at most a constant L, independent of N.

On the tail m,...,a-1 choose the analytic square root
sqrt(C^2-cos^2(n theta)) positive at C=cos(pi sigma_*), and
take the symmetric adjacent entry b_n times this square root.
All these branches exist on a fixed C disk: kappa>sigma_*
separates every radicand uniformly from zero. Let D_T be the
principal tail submatrix of the positive matrix whose diagonal
is d_n and whose adjacent entries are b_n. Its positivity is
already proved by the exact principal minors in the joint source
determinant theorem. The tail matrix is EXACTLY

    J_T(C)=C D_T+E_T(C),
    (E_T)_(n-1,n)=(E_T)_(n,n-1)
       =-b_n cos^2(n theta)
                  /[C+sqrt(C^2-cos^2(n theta))],              (5)

with zero diagonal. Formula (4) and the strict cutoff show

    ||E_T(C)||+||partial_C E_T(C)||<=E_0.                     (6)

The same conclusion for every fixed C derivative follows on a
slightly smaller disk. No lower eigenvalue bound for D_T, and no
uniform bound on its largest eigenvalue, is required.

Keep the interface upper entry equal to 1 and the lower entry
gamma_m=b_m^2(C^2-cos^2(m theta)), which is uniformly bounded.
The resulting tridiagonal determinant is exactly R_a by (2).
This bounded nonsymmetric low block avoids choosing square roots
at the moving integer-degree zero of a recurrence coefficient.

If C stays in a sufficiently small disk about cos(pi sigma_*),
and z is in (3), then

    dist(z,C[0,infinity))>=c |z| sin(vartheta).                (7)

The inverse of zI-C D_T therefore has norm at most the reciprocal
of the right side. Choosing R sufficiently large, (6) gives the
same bound, up to a factor two, for (zI-J_T)^-1. The low inverse
has norm at most (|z|-L)^-1. Its Schur complement changes the
tail by the rank-one matrix

    gamma_m [(zI-J_L)^-1]_(m-1,m-1) e_0 e_0^T.              (8)

Its norm is O(1/|z|). A second Neumann estimate proves that the
FULL determinant is nonzero and that its displayed tridiagonal
matrix M has

    ||M^-1||<=C_vartheta/|z|.                               (9)

This proves (3) using the actual finite determinant, including
both parities and the folded endpoint.

## 3. Joint logarithmic bounds and the source-selected amplitude

Fix a negative reference z_*=-R_* with R_*>R. The product domain
(3) is simply connected. Define the logarithm of R_a(z)/R_a(z_*)
to be zero at z_*, for every sigma. Then

    |partial_z Log R_a|+|partial_sigma Log R_a|<=C_K N         (10)

on each fixed compact K, with analogous normalized higher
derivative bounds on smaller compacts.

For completeness the large D_T causes no loss in (10). The
Schur tail is S=zI-C D_T-E_T-gamma e_0e_0^T, with gamma the
bounded expression in (8), and

    C S^-1 D_T=z S^-1-I-S^-1 E_T
                               -gamma S^-1 e_0e_0^T.         (11)

Thus its trace against a C derivative is O(N) by (6),(9).
The low-block derivative is bounded; gamma and its derivatives
are bounded by the low resolvent formula. This proves (10).

There are functions S_(sigma,alpha)(z), A_(sigma,alpha)(z),
holomorphic jointly in sigma and z on (3), with S(z_*)=0,
A(z_*)=1 and A nowhere zero, such that

    R_a(z;c)/R_a(z_*;c)
       =A_(sigma,alpha)(z) exp[N S_(sigma,alpha)(z)]
                                             (1+O(N^-1)).    (12)

The error and its fixed derivatives are uniform on compacts.
The phase and amplitude depend smoothly on the real channel
parameter alpha, which always remains the ACTUAL a/N.

The anchor is selected by an exact source identity, not by a
choice of an algebraic root. For every complex sigma put

    t_hi=N(1-sigma)-2,
    u_hi=t_hi/2+iN log(R_*)/(2pi),
    beta_a=s_(2a)/s_a^2.

The reflection R_a(z;-c)=(-1)^a R_a(-z;c) and the original
ordinary normalization give exactly

    R_a(-R_*;c)=(-1)^a beta_a^-1
       product_(r=0)^(a-1)2sin(pi(t_hi-r)/N)
       *q^[-(N-1)u_hi-(a^2-(N-1)a)/2]
       *fhat_a(t_hi,u_hi).                                 (13)

This is in the already proved JOINT high-degree physical packet:
Re(t_hi/N)>1/2, its real magnetic coordinate is centered, and
the complete-channel margins follow from alpha_0>sigma_*.
Its two wire coordinates remain strictly inside their domains
for a small fixed complex sigma disk. The offset -2, the actual
half-integer center when present, and every phase in (13) remain
literal. All sine factors have a fixed distance from their zeros.
Consequently (13) supplies a nonzero relative absolute anchor,
jointly in sigma, by that ordinary packet and an elementary
finite-product Euler--Maclaurin estimate. It also does so on an
open interval of negative z around z_*.

The bounds (10) give a normal family for the normalized logarithms.
Every limit agrees on that negative interval with the anchor's
source-selected leading phase. The identity theorem fixes it on
Omega_R, for each complex sigma; compactness makes convergence
uniform jointly in sigma and the real parameter alpha. There is
no interpolation from integer degree samples in this argument.

Here are explicit transport equations proving the relative error.
Put D=z partial_z, kappa_q=2pi i,

    U=exp(pi i sigma)/z, T=exp(2pi i sigma),
    J=exp(2pi i alpha).

The original finite numerator satisfies the exact root equation

    (QU-1)(U-T)R(z/Q)+(QT-U)(1-U)R(Qz)
      +[2U+2QTU-(1+Q)U^2-T(Q^-a+Q^(a+1))]R(z)=0.           (14)

Set A0=(U-1)(U-T), C0=2U(1+T-U)-T(J+J^-1) and

    H(p,z)=A0(e^(kappa_q p)+e^(-kappa_q p))+C0.

The selected p=D S satisfies H=0. Its discriminant is

    C0^2-4A0^2=-16T^2 sin^2(pi alpha) W/z^2,
    W=1-2cos(pi sigma)z+cos^2(pi alpha)z^2.                   (15)

All roots of W remain in the excluded small positive sector.
Indeed write C_s=cos(pi sigma), b=cos(pi alpha), and use the
analytic sqrt(C_s^2-b^2) positive at the real center. The roots
are 1/(C_s+sqrt(C_s^2-b^2)) and
(C_s+sqrt(C_s^2-b^2))/b^2, with the second omitted at b=0.
The gap alpha_0>sigma_* gives uniform branches and a uniform
argument bound, even as b tends to zero. Shrink epsilon if
necessary. Also A0 has zeros only near the unit circle, outside
Omega_R. Hence H_p is nonzero throughout the domain.

The exact first transport term is

    H1=kappa_q[U(U-T)e^(-kappa_q p)
             +T(1-U)e^(kappa_q p)+2TU-U^2-TJ],
    rho=-(H1+(D p)H_(p,p)/2)/H_p.                            (16)

Larger-compact Cauchy bounds, the exact shifts in (14), and the
proved actual leading convergence first give p_N-p=O(N^-1),
where p_N=D(N^-1 Log R_a). A second substitution then gives
p_N=p+rho/N+O(N^-2), uniformly jointly in sigma and z.
Define D Log A=rho and A(z_*)=1 and integrate along compact
paths from z_*. This proves (12), including fixed derivatives.
It is the actual finite-shift bootstrap, not a formal WKB choice.

## 4. Genuine generic-q numerator normals

Now use the original generic recurrence with B=Q^-N, not the
root-only recurrence (2). Hold t=N sigma and a fixed while
q=q0 exp(epsilon_q) varies. A marked magnetic lift u is also
held fixed, with |u|<=C N and z(q)=q^(t-2u). Assume its root
parameters lie in a compact subset of (3). Then

    |partial_(epsilon_q)^r R_a(q;t,z(q))|_0
           <=C_r N^(10r) |R_a(q0;t,z(q0))|.                  (17)

The same estimate applies to the original unnormalized Newton
numerator after retaining its exact K_a and monomial factors.
The bounded marked lift is necessary: u->u+NL leaves the root
coordinate unchanged but changes its genuine q derivatives.

To prove (17), first conjugate the root matrix above by the
diagonal unitary with entries (-1)^n, so its offdiagonal signs
are positive in the following convention. Its inverse bound
(9) is unchanged. In the low
block and at the interface freeze the upper entries at 1. In
the tail freeze each upper entry at its ROOT complex value
b_n sqrt(C^2-cos^2(n theta)); it is bounded away from zero.
Set every generic lower entry to minus the actual generic
recurrence coefficient beta_n divided by that frozen upper
entry. The diagonals use the actual generic alpha_n. This
determinant is exactly the original generic R_a.

The previously proved generic recurrence estimates, with t/N
in a fixed complex compact, give |alpha_n'|<=C N^5 and
|beta_n'|<=C N^7 on the required small generic disk. The same
bounds follow directly by differentiating their finite rational
formulas: the only small denominators are the original spectral
gaps, while q^t and its marked derivatives have bounded scaled
parameters. Thus the matrix changes by at most
C N^7 |epsilon_q|; z(q) changes by O(N|epsilon_q|).
By (9), on |epsilon_q|<=c N^-10 the determinant ratio and its
inverse are bounded, since its dimension is at most N.
Cauchy's formula gives (17). The original K_a and monomials
are controlled on this same disk by their finite root-unit
products. No derivative of a root-only reflection is used.

## 5. The actual geometric chart and the remaining period

The real-deficient-frame theorem has sigma_*=1/6. Its two
determinant arguments have |z| asymptotic to a positive constant
times X^2 and imaginary parts of opposite sign, each comparable
to X, with X arbitrarily large. Keep the midpoint in a compact
subinterval of its allowed range. Choose vartheta proportional
to 1/X and then X sufficiently large. The proof above needs
only R=O(1/sin vartheta)=O(X), so BOTH actual arguments lie
strictly in (3). A small fixed complex neighborhood of this
chosen geometric frame, or a fixed compact family around it,
is therefore covered. One fixed vartheta does not cover the
entire unbounded X-family, whose arguments approach the cut.

The negative-real anchor in (13) is exactly the reflected source
branch calibrated in that framing theorem. At the folded limit
its magnetic characteristic is

    Y=(z-i sqrt(1-2cos(pi/6)z))^2
                          /[1-2cos(pi/6)z+z^2],             (18)

with the square root continued from positive values at negative
z through the upper or lower half-plane respectively. The two
values agree with the actual input/output geometric momenta,
including the output's C^-1 disk shift. This comparison uses
the proved anchor and corridor, not arbitrary root selection.

The entire completed root kernel is a residual sine product
times two such R polynomials. In this deficient corridor the
residual sine arguments, after removing their recorded integer
sign, lie in a strict zero-free strip because alpha>Re sigma
by a fixed margin. Thus its exact product and (12),(13) give
a nonzero joint ROOT packet, including complex degree, in a
neighborhood of the actual geometric frame. At a maximal folded
channel the residual product remains empty or one factor as
specified by the exact source, so both level parities are kept.

The normal estimate (17) is for the ORIGINAL q-Hahn numerators.
The full exceptional generic operator still has its unspecialized
boundary factors and requires its own lift; it cannot be obtained
by varying q in the canceled root kernel. In particular, an actual
large-partner column cannot be replaced by the small-channel
numerator in (17) solely because their root values coincide;
their genuine generic derivatives are different. Most importantly,
the complete fixed forbidden integer-separation physical slice
is identically zero. Its magnetic deformation alone must retain
that zero. Joint degree analysis now has a local analytic input,
but no degree contour, nonzero global coefficient, complementary
source gap, or general volume equality has been proved here.

Focused audit: [original joint numerator, tail determinant and
selected amplitude](../experiments/audit_actual_q_hahn_joint_deficient_degree_packet.py).
It checks 248 independent-degree original four-jet identities,
124 exact finite-shift equations, 72 determinant and Schur identities,
24 positive tail matrices and 586 endpoint coefficient bounds.
At 120 digits, 12 literal reflected high anchors, 24 joint complex
amplitudes and 72 genuine numerator checks pass. The finite matrix
and asymptotic samples remain diagnostics; the uniform estimates
are proved above.

Primary-agent full analytical review: PASS. The reader checked the
exact determinant, bounded tail correction through the folded
endpoint, Schur inverse and logarithmic trace bounds, joint reflected
anchor with its -2 offset, both finite-shift orders, genuine small
numerator normal disk and the finite-X geometric coverage. The
full generic operator and selected degree period remain open.

Independent geometric and analytical review: PASS. A second reader
checked the positive-tail argument, joint high anchor, marked
geometric upper/lower branches and finite-X neighborhood, including
the residual sine strip. The small/large generic partner distinction
and the exact zero-slice limitation are retained.

Independent source and analytic review with fresh audit replay: PASS.
A third reader checked the original recurrence and both finite-shift
orders, the exact joint reflected anchor, the determinant perturbation
with bounded marked lifts, and all source-normalization limitations.
Its redirected replay reproduced all 248/124 exact source/shift checks,
72 determinant/Schur checks, 24 positive tails, 586 coefficient checks,
12 literal anchors, 24 amplitudes and 72 genuine numerator checks.
