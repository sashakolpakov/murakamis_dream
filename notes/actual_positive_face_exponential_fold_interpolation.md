# An exponentially accurate analytic interpolation of the actual fold factors

30 October 2026. The construction below
uses analytic contractions on shrinking disks, then the actual positive
finite recurrence. It produces an even holomorphic fold interpolation
whose error on the original channel grid is exponentially small, uniformly
on a fixed complex face-radius neighborhood. Formal WKB existence alone
is not used. This is a local complete-circle factor theorem; the shared
coefficient period and the ordinary-color alias subsets remain separate.

## 1. Statement with the original finite anchor

Fix a compact set of positive face radii in any one of the actual zero
patterns of the [signed source theorem](general_signed_augmented_source_volume.md).
Zero faces stay zero. Set

    B_(N,a)=beta_a^2 D_a(x,b,y)D_a(x,c,y)P_(d-2a)(x,y),
    d=N-1, M=floor(d/2), s0=d-2M,
    delta_a=(d-2a)/(2N), delta_min=s0/(2N), h=1/N.

Use the explicit analytic functions E_b,J_b,a_b,V of
[the fixed-fold theorem](actual_positive_face_fixed_fold_packet.md),
equations(1),(2). In particular V is even, V(0)=0 and
V''(0)=2pi(T_b+T_c)/(x+y)>0. The T_b=0 triangle is treated as
the exact constant-pivot case, with J_b=1.

There are fixed positive delta_*,rho,c,C, a complex logarithmic
radius neighborhood O_rho of the given real compact, and even
holomorphic functions H_N(delta;l) on |delta|<2delta_*, l in O_rho,
such that H_N(0;l)=0 and

    H_N(delta;l)=-N V(delta;l)
                      -(1/2)Log[J_b(delta;l)J_c(delta;l)]+O(N^-1).
                                                               (1)

The bound is uniform on smaller closed disks and neighborhoods, with
all fixed derivatives by Cauchy estimates. Define the specified finite-N
interpolation

    mathcal B_N(delta;l)=B_(N,M)(l)
                       exp[H_N(delta;l)-H_N(delta_min;l)].       (2)

The original B_(N,M) is retained exactly; it is a holomorphic unit
on O_rho by positive-matrix preconditioning and the original forced
factor. Then for EVERY original integer a with
delta_min<=delta_a<=delta_*,

    B_(N,a)(l)/mathcal B_N(delta_a;l)=1+O(e^(-cN)),
                                                uniformly l in O_rho. (3)

The right side of (2) is even in delta. No noninteger-dimensional
matrix is introduced. For an actual retained half twist, the factor

    omega_M^epsilon
             exp[pi i epsilon N(delta^2-delta_min^2)]            (4)

agrees exactly with omega_a^epsilon on this grid, including its
common q^(d^2/2) phase. Thus (2)--(4) preserve the entire local root
complete-circle factor. They do not interpolate a different generic-q
germ or ordinary small-color coupon.

## 2. A regular analytic equation in the squared fold variable

First consider one triangle with T_b>0. Let z denote the pivot
coordinate (N/2-a)/N. On a fixed small complex disk the functions
E(z)=E_b(z), D(z)=(x+y)^2-4xy sin^2(pi z) obey
E(z)E(-z)=D(z). Write

    B0(w)=[E(z)+E(-z)]/2, C0(w)=[E(z)-E(-z)]/(2z),
    t(w)=tan(pi z)/z, w=z^2.

All are holomorphic in w near zero; t and C0 are units. Seek a
reflection-preserving approximate pivot in the form

    e_v(z)=E(z) exp[z v(z^2)],                         (5)

where v is holomorphic in w. Thus e_v(z)e_v(-z)=D(z) EXACTLY.
Clear the actual recurrence residual as in the fixed-fold proof:

    Rcal_v(z,h)=tan(pi(z+h))e_v(z)+tan(pi z)e_v(-z-h)
       -[tan(pi(z+h))+tan(pi z)]
                          [A+2b sin(pi z)sin(pi(z+h))].         (6)

It vanishes at z=0,-h and is odd under z -> -z-h. Set
z=zeta-h/2. Division therefore defines a holomorphic function of
w=zeta^2:

    G_h(v)(w)= Rcal_v(zeta-h/2,h)
                         /[zeta(zeta^2-h^2/4)].                 (7)

The values at the apparent three divisors in (7) are their removable
limits. Holomorphic divisibility follows successively by the two
zeros and centered oddness, including h=0 where the zeros coalesce.
It does not require estimating separate singular quotients.
At h=0 and v=0, G_0(0)=0. Its linearization is multiplication by
the nonzero analytic function

    L(w)=2t(w)C0(w), L(0)=4pi^2 T_b.                  (8)

This normalization resolves the formal fold pole in the analytic
equation; it does not cancel the peripheral factors of the finite
four-component operator.

## 3. The single-loss analytic estimate

Here is the estimate that controls arbitrarily many corrections.
Use sup norms on w disks, with radii in a fixed compact interval
0<R_1<=R<=R_0. For small v and 0<Delta<R-R_1, with h small
enough that Ch<Delta, analytic differentiation gives

    ||D G_h(v)-L||_(R to R-Delta)
                                  <=C(||v||_R+h/Delta).        (9)

All constants are uniform on a fixed complex radius neighborhood.
There is only ONE loss of analytic radius, not two independent
derivatives in z. We give the cancellation explicitly.

Write the even and odd parts of (5) as

    e_v(z)=B0(w)+w F_v(w)+z[C0(w)+G_v(w)].

Both F_v,G_v are pointwise analytic functions of (w,v(w)), and

    F_v=C0 v+O(v^2), G_v=B0 v+O(v^2).

For example they follow directly from cosh(zv) and sinh(zv)/z,
which are analytic in (w,v). For zeta^2=w put
a=zeta-h/2, b'=zeta+h/2 and w_-=a^2,w_+=b'^2.
The v-dependent part of (7) is exactly

    t_+ F_-+t_- F_+
      +(h/(2zeta))(t_- F_+-t_+ F_-)
      +(1/zeta)(t_+ G_--t_- G_+),                    (10)

where subscripts indicate evaluation at w_+ or w_-.
The same formula with pointwise derivatives of F,G holds for D G_h.
Every apparent divided difference is controlled by

    [K(w_+)-K(w_-)]/zeta
                =2h integral_0^1 K'(w_-+t(w_+-w_-))dt.         (11)

The segment stays in the outer disk when Ch<Delta. Cauchy's
bound for K' costs Delta^-1. Comparing the first line of (10)
with its h=0 value uses the same first-derivative estimate, since
|w_+-w|+|w_--w|<=Ch. The nonlinear h=0 difference from (8)
costs O(||v||). These facts prove (9), including w=0 by holomorphy.

## 4. Exponentially accurate analytic pivots

The explicit first correction already proved in the fixed-fold note
provides the starting function

    v^(0)(w)=h a_b(z)/z, w=z^2.

It is holomorphic and O(h); the joint residual divisibility there
gives G_h(v^(0))=O(h^2) on one fixed disk. Iterate

    v^(m+1)=v^(m)-L^-1 G_h(v^(m))                   (12)

on nested w disks, losing Delta=Kh at each step. Choose fixed K
sufficiently large, then h sufficiently small. Equation (9) makes
the map in (12) a contraction with Lipschitz factor at most1/2
between consecutive disks, as long as ||v||<=C_1 h. The first
change is O(h^2), and subsequent changes decrease geometrically.
Their sum is O(h^2), so that norm condition closes by induction.

More explicitly put R_m=R_0-m Delta and T(v)=v-L^-1 G_h(v).
Then v^(m) is defined on the disk of radius R_m. On the next disk,
v^(m+1)-v^(m)=T(v^(m))-T(v^(m-1)), with the previous iterate
restricted to R_m. Estimate (9) therefore gives
||v^(m+1)-v^(m)||_(R_(m+1))<=
(1/2)||v^(m)-v^(m-1)||_(R_m).
This is a contraction between nested analytic domains, not an
assertion that translation is bounded on one unchanged disk.

Perform m=floor(c_0/h) steps, with c_0 small enough that all disks
still contain one fixed smaller disk. Keep one more radius margin
to evaluate the final residual. The resulting analytic v_N obeys

    v_N=v^(0)+O(h^2), ||G_h(v_N)||<=C e^(-c_1/h).     (13)

Each operation is analytic in the face parameters, and all estimates
are uniform there. The finite iteration count may depend on N; no
analyticity in a varying quantum level is claimed. All functions
are real on positive real radii and real w. Put

    e_N^*(z)=E(z)exp[z v_N(z^2)].                    (14)

It preserves reflection exactly, has the original first correction,
and its ACTUAL Riccati residual is exponentially small on a fixed
complex z disk. The removable divisions in (7) only multiply it
by bounded analytic factors. For T_b=0 take e_N^*=A exactly.

## 5. Match the actual finite pivots, including complex face radii

Choose a fixed real cutoff 2delta_0 within the disk of (14). Start
the ACTUAL physical recurrence at the nearest k0 to 2delta_0 N,
and estimate only k<=delta_0 N. At real positive radii the original
pivots have A<=e_a<=2A+4b. Also e_N^*(k/N)/A>=exp(c k/N)
for sufficiently large N in a nonconstant triangle. Consequently
the exact error multiplier is bounded by

    [tan(k theta)/tan((k+1)theta)] exp[-c(k+1)/N].     (15)

This is the same source-derived positive contraction as before.
The initial error is bounded, and its propagation to k<=delta_0 N
is O(e^(-c_2 N)). The sum of exponentially small local residuals
remains exponentially small, with at most a polynomial loss.

The matching extends to a FIXED complex face neighborhood, not just
to a shrinking neighborhood. At each original principal matrix,
positive-summand preconditioning gives
M_j(l)=M_j(l_real)^(1/2)(I+E)M_j(l_real)^(1/2),
||E||<=C rho, uniformly j,N. The last inverse-entry formula then
gives the original Schur-pivot ratio

    e_a(l)/e_a(l_real)=1+O(rho)

uniformly, with no lower eigenvalue assumption beyond the stated
positive matrices. The same bound holds for (14) by its uniform
analytic unit bounds. Thus each complex error multiplier is at
most exp(C rho) times (15). Over the entire finite interval the
extra cost is at most exp(C rho N). Choose rho FIRST below both
the initial-damping and analytic-residual exponential rates. It
follows that

    e_a(l)/e_N^*((N/2-a)/N;l)=1+O(e^(-c_3 N))        (16)

uniformly in the smaller complex face neighborhood and at EVERY
physical pivot in the chosen real window, including the two parity
endpoints. This step identifies the constructed analytic function
with the actual polynomial source. No choice among homogeneous
recurrence solutions has been assumed.

## 6. An analytic discrete primitive with the exact folded anchor

Apply the construction to the two actual triangles. Their exact
reflection makes the marked logarithm

    ell_N(z)=Log[e_(b,N)^*(z)e_(c,N)^*(z)/D(z)]

odd and holomorphic on a fixed disk. Moreover

    ell_N=V'+h(a_b+a_c)+O(h^2),                     (17)

uniformly and holomorphically. We now construct the logarithm of
the channel product itself with exponential precision, instead
of summing a finite-order Euler--Maclaurin error.

Let A_h f(z)=h^-1 integral_(-h/2)^(h/2) f(z+t)dt.
It preserves odd analytic functions. On nested z disks its difference
from the identity has norm at most Ch/Delta. Start f^(0)=ell_N
and iterate f^(m+1)=f^(m)+ell_N-A_h f^(m), losing Delta=Kh
at every step. The first change is O(h^2), by the centered integral
and bounded second derivatives. The same geometric contraction
argument as in (12), now linear, gives an odd analytic f_N with

    f_N=ell_N+O(h^2), A_h f_N=ell_N+O(e^(-c_4 N)).    (18)

Define H_N(z)=-h^-1 integral_0^z f_N(t)dt. It is even, has value
zero at zero, and obeys

    H_N(z+h/2)-H_N(z-h/2)
                              =-ell_N(z)+O(e^(-c_4 N)).        (19)

Equations (17),(18) give exactly (1), since
integral_0^z(a_b+a_c)=(1/2)Log[J_b(z)J_c(z)].

For adjacent ACTUAL channel indices the forced product contributes
exactly D at the midpoint, and the two original pivots contribute
their reciprocals. By (16) their ratio is exp[-ell_N(midpoint)]
with exponentially small relative error. Compare this with (19)
and sum at most O(N) steps from the physical maximal channel.
The resulting error is still O(e^(-cN)). At the starting index
(2) uses B_(N,M) EXACTLY and delta_min=s0/(2N). This proves (3).

## 7. What the theorem supplies and what it does not

The comparison (3) is exponentially accurate on the actual channel
grid, uniformly for fixed complex face radii, while (2) is even and
holomorphic in a fixed fold disk. It therefore supplies the local
interpolation input that a fixed-frequency Fourier contour argument
requires. It is substantially stronger than a real-grid relative
O(N^-1) approximation. Its phase and amplitude are those of the
actual finite source, with all beta, forced factors, parity offsets
and half twists retained.

The full shared-face coefficient must still be assembled with its
original Cauchy period, angular tails and finite channel endpoints.
The entire complete-image core must then be distinguished from the
nonempty ordinary-color subsets in the exact external reflection
identity. No global alias gap, filled-knot conclusion, or generic-q
normal theorem is inferred here.

The focused [audit](../experiments/audit_actual_positive_face_exponential_fold_interpolation.py)
and its [recorded results](../experiments/actual_positive_face_exponential_fold_interpolation_results.json)
check 20 symbolic identities and 24 complex-face residual identities.
Numerical analytic-iteration prototypes are compared with the original
beta/D/P factors: four pivot cases through N=1024 and eight complete-circle
comparisons at both parities, including fixed complex face parameters.
These finite projections are diagnostics of the construction; they are
not premises for the uniform exponential estimate proved above.

No full mixed-color packet, ordinary-subset gap, or generic-q normal
claim follows from this interpolation theorem.