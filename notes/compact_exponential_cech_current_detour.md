# The exponential framing detour and its exact compact-source current

Research proof, 27 October 2026. The natural exponential homotopy
does not patch in the fixed complete-meridian framing space. Its
precise Cech defect is a nonzero affine-cotangent cocycle. Allowing
the meridian eigenvalue to vary absorbs that defect and produces a
global whole-function detour. The induced compact-source current
has an explicit primitive for every actual finite matrix, including
all weighted Green-current matrices. Its meridian-normal poles
are exact and its finite part retains the original trace.

The detour changes the meridian and the physical clock. It is not
an intertwiner of the actual quantum word or a proof of the
geometric/source pushforward. The fixed-complete obstruction and
the varying-meridian repair are kept separate below.

## 1. The fixed framing space and the failed exponential interpolation

Use the actual compact-source charts

    V=1/v, a'=v-v^2 a, T=v a, T'=V a'=1-T,
    omega_0=dv wedge da, omega_I=-omega_0/(2pi*i).

The resolved complete framing threefold has the additional normal
coordinate

    eta'=-v^2 eta.

Its actual principal full framing form is

    H=-dlog eta wedge omega_0/(1-eta v).         (1)

The nonzero constant `c=2pi*i` is fixed. The physical graph is

    eta_phys=(1-exp(-c T))/v,
    eta'_phys=(exp(c T')-1)/V.                  (2)

The equality of these expressions uses `exp(c)=1`. The apparent
divisions by v or V are removable at their respective compact
poles. These are the explicit actual meridian/source formulas
proved in [the framing bridge](compact_framing_gauge_and_boundary_residue.md).

On the first chart consider the nonvanishing-denominator path

    eta_lambda=(1-exp(-c lambda T))/v,
    1-eta_lambda v=exp(-c lambda T).            (3)

The transition forced by the fixed threefold is

    eta'_lambda
      =[exp(-c lambda)exp(c lambda T')-1]/V.    (4)

For nonintegral real lambda, (4) has a genuine pole at V=0.
The tempting regular second-chart expression
`[exp(c lambda T')-1]/V` differs by

    [exp(-c lambda)-1]exp(c lambda T')/V.       (5)

Thus (3) supplies a whole path only on the punctured source chart.
It does not define a homotopy of the whole fixed compact source
into the complement of the additional divisor `1-eta v=0`.

This is also an elementary fixed-base relative obstruction. On
the real compact sphere let T run from zero to one along a fixed
angular meridian. Any continuous section with finite pole-chart
coordinates has `1-eta v=1` at both endpoints. If it avoids zero,
this function is a based loop in C^*. Its winding is zero for the
zero section and -1 for (2). A homotopy through such sections
cannot change that integer. This argument concerns sections with
their two pole fibers retained. The stronger fixed-space tube
statement is developed independently in the resolved-relative-cycle
calculation; no conclusion about unrestricted deformations of
cycles is needed here. The actual fixed-space tube and the
generic-meridian source-wall charges are computed in
[the meridian homotopy wall theorem](meridian_homotopy_wall_and_source_residues.md).

## 2. The Cech defect is absorbed by changing the conjugacy class

Put

    h_lambda=exp(-c lambda), u_lambda=exp(-c lambda T),
    k_lambda=1-h_lambda.

Define the whole matrix

    mu_lambda=
      [u_lambda, (1-u_lambda)/v;
       v(u_lambda-h_lambda), 1+h_lambda-u_lambda].          (6)

It has determinant h_lambda and fixes the retained eigenflag
`[1:v]` with eigenvalue one. The other eigenvalue is h_lambda.
On the second chart `u_lambda=h_lambda exp(c lambda T')`;
therefore its potentially bad lower entry is exactly

    h_lambda[exp(c lambda T')-1]/V,

which is removable. Formula (6) is a global holomorphic matrix on
the entire compact-source surface for every lambda. It equals I
at lambda=0 and the physical complete meridian at lambda=1.
Its 11 entry never vanishes on the real homotopy, including its
two endpoints in each compact fiber.

Write its upper off-diagonal coordinate as eta_N and its lower
off-diagonal coordinate as eta_S. Their exact transition is

    eta_S=k_lambda v-v^2 eta_N.                (7)

For k_lambda!=0 this is the affine cotangent torsor with class
k_lambda. Its class is nonzero: a correction by functions regular
on the two affine base charts would have to express v, after
division by v^2, as Laurent powers >=0 and <=-2. The missing
v^(-1) coefficient prevents this. At lambda=0,1 the affine
translation vanishes and (7) returns to the nilpotent line bundle.
Thus the repair is a family of conjugacy classes, not a missing
regular correction to (4) inside the fixed space.

The inverse-cut-eigenflag convention of the actual knot model
fixes the SL2 lift as

    M_lambda=exp(-c lambda/2), h_lambda=M_lambda^2,
    mu_tilde_lambda=M_lambda^(-1)mu_lambda,
    p=1/v, s=(u_lambda-h_lambda)/M_lambda.

Then (6) is exactly the existing generic-meridian Gauss matrix

    mu_tilde_lambda=
      [M+s, -(M-M^(-1)+s)p;
       s/p, M^(-1)-s].                       (8)

The actual cut coordinate is consequently

    A_cut=M/(M+s)=h_lambda/u_lambda.            (9)

At lambda=1 it returns `exp(c T)`. The SL2 endpoint is the
recorded M=-1 sign, whereas its projective meridian is the desired
complete meridian. The full kappa term, modified dimension, pivot
and other source factors cannot be replaced by their M=1 values
in the interior. No analytic continuation of a knot's geometric
A-branch along this eigenvalue path has been proved by (6).

## 3. A global whole-function map of the actual compact source

When k_lambda!=0 set

    a_lambda=(1-exp(-c lambda v a))/(k_lambda v),
    Phi_lambda(v,a)=(v,a_lambda).              (10)

Equation (7) divided by k_lambda says exactly

    a'_lambda=v-v^2 a_lambda.

Hence Phi_lambda is a global holomorphic endomorphism of the
actual compact-source surface, not merely its meridian chart.
It extends at lambda=0 with `Phi_0=id`. For 0<lambda<1 its
fiber derivative is

    J_lambda=partial_a a_lambda
       =c lambda exp(-c lambda T)/k_lambda !=0.             (11)

No properness or global injectivity follows from (11). The
whole exponential functions, with their marked branches, are
retained rather than replaced by their jets.

There is an exact global primitive

    Phi_lambda^*omega_0-omega_0=d B_lambda,
    B_lambda=-(a_lambda-a)dv.                 (12)

Indeed differentiation gives (11) minus one. On the second chart
both `a'_lambda-a'` and dV acquire their inverse factors, so
B_lambda patches without a Cech remainder. In particular

    integral_Gamma Phi_lambda^*omega_I=1.       (13)

Directly on the compact cycle this is the elementary identity

    integral_0^1 J_lambda(T)dT=1.

This supplies an exact compact cohomology/current deformation;
there is no free period normalization in it.

## 4. The current formula applies to every actual finite word

Let C be any actual finite N-by-N matrix, including the completed
weighted word or one of its Green-current matrices. Put n=N-1.
Its actual coherent scalar symbol is the regular function

    f_C(v,a)=sum_(i,j=0)^n C_ij binom(n,j)
                  v^i a^j(1-va)^(n-j).        (14)

The source form is `alpha_C=f_C omega_0`. Define the explicit
current

    B_(C,lambda)
       =-[integral_(a)^(a_lambda) f_C(v,b) db]dv.           (15)

The integral in (15) is finite polynomial antiderivation in b;
it does not use the value of the trace or the knot period.
The coordinate transformation of the scalar f_C and of `db dv`
proves that (15) is a global holomorphic one-form on X. Direct
differentiation proves the strict current identity

    Phi_lambda^*alpha_C-alpha_C=d B_(C,lambda).             (16)

Thus the original finite source is preserved exactly:

    integral_Gamma Phi_lambda^*(f_C omega_I)=Tr(C)/N.       (17)

For a separate verification, all off-diagonal terms of (14)
have angular weight i-j and integrate to zero. A diagonal term
reduces under `t_lambda=v a_lambda` to polynomial antiderivation
along the complex path from t_lambda=0 to t_lambda=1:

    binom(n,j)integral_0^1 t_lambda^j
                            (1-t_lambda)^(n-j)dt_lambda=1/N.

Whole-word products and every original head projector are formed
before (14)--(16). Pullback is not used as a replacement matrix
product. Since Phi_lambda is independent of crossing couplings,
all coupling Euler operators and the explicit Green moment
operators commute with this current map. In particular the
full weighted source identity and both remaining framing Green
currents retain their literal matrix coefficients and endpoints.

This gives an actual compact-current deformation of those
specified sources. It has not identified their image with the
internal geometric Gaussian current.

### 4.1 The actual polar-fiber support complex is preserved

This map retains more than the absolute compact period. Let
`L_infinity` be the actual deleted polar fiber `v=infinity`, and
`U=X minus L_infinity`, with its affine coordinates (v,a). The
source support complex proved in
[the compact localization theorem](compact_source_localization_boundary.md)
is

    C_(L,alg)^k=Omega_alg^k(X) direct_sum Omega_alg^(k-1)(U),
    D(alpha,beta)=(d alpha,alpha|_U-d beta).     (17a)

Here the exponential detour requires the specified extension

    C_(L,hol)^k=Gamma(X_an,Omega_hol^k)
                    direct_sum Gamma(U_an,Omega_hol^(k-1)).

The original algebraic source complex maps to this holomorphic
complex by inclusion. All subsequent current maps and finite
parts in this note take values in this holomorphic complex;
they are not asserted to remain algebraic. Equivalently one
can use its explicitly generated whole exponential-period
subcomplex, including the stated primitives.

Phi_lambda fixes the base v. It therefore preserves L_infinity
and U and defines a strict pullback chain map on C_(L,hol),
and hence from the actual algebraic source into this extension. This
retains the actual polar-fiber co-source rather than replacing
it by an unspecified integration functional.

For an explicit homotopy, the affine-fiber interpolation

    H_tau(v,a)=(v,a+tau(a_lambda-a))

is global: the difference of two fiber coordinates transforms
linearly. It preserves U as well. Its Cartan homotopy operator
on one-forms and two-forms is

    K_lambda beta=integral_(a)^(a_lambda) beta_a(v,b) db,
    K_lambda(f omega_0)=-[integral_(a)^(a_lambda)f(v,b)db]dv.

It satisfies `Phi_lambda^*-id=d K_lambda+K_lambda d` directly
by differentiation, or by integrating the derivative in tau.
In particular `K_lambda alpha_C=B_(C,lambda)`.

Take the actual primitive beta_C on U with d beta_C=alpha_C;
it is obtained without using its trace by polynomial integration
in the v coordinate, as in the localization theorem. The
complete source pair has the exact relative identity

    Phi_lambda^*(alpha_C,beta_C)-(alpha_C,beta_C)
       =D(B_(C,lambda),-K_lambda beta_C).       (17b)

Indeed its second component is
`B_(C,lambda)+d K_lambda beta_C`, precisely the homotopy formula
for beta_C. This fixes the endpoint sign in (17b).
The source residue and all co-source endpoint data survive this
specified relative chain map. Every coupling derivative commutes
with both K_lambda and (17b). Thus (17b) applies coefficientwise
to every literal finite Green-current matrix formed from the
whole weighted word. It does not replace those matrices by a
scalar before composing the word. Commutation with an internal
formal Gaussian pushforward has not been proved here.

## 5. Exact finite-part regularization at the complete resonance

Near lambda=1 use the marked normal `k=1-exp(-c lambda)` and
the local branch

    lambda=1-Log(1-k)/c.

Put `u=exp(-c T)` and `eta_phys=(1-u)/v`. Then the whole map has

    a_lambda=eta_phys/k+a u+O(k),
    J_lambda=c u/k+u(1-c T)+O(k).              (18)

For the identity matrix, (12) gives the explicit pole and finite
part

    Phi_lambda^*omega_0
       =(c u/k)omega_0+u(1-c T)omega_0+O(k),
    (c u)omega_0=d[-eta_phys dv],
    u(1-c T)omega_0-omega_0=d[a(1-u)dv].        (19)

Thus the pole is exact and the finite-part compact period is
one. In particular discarding only the pole coefficient preserves
the selected source; discarding the entire current would not.

More generally (14) has degree at most n in a. Therefore (15)
and (16) have poles of order at most n+1=N in k, with a finite
principal part. Comparing Laurent coefficients in (16) gives

    every negative coefficient=d(explicit coefficient of B),
    finite_part(Phi_lambda^*alpha_C)
                         =alpha_C+d finite_part(B_(C,lambda)). (20)

For the original relative primitive beta_C its a-degree is at
most n, so K_lambda beta_C has the same pole bound N. Comparing
Laurent coefficients in (17b) therefore strengthens (20): every
negative coefficient is exact in the stated holomorphic support
complex, and the finite part represents the identical selected
relative source class after holomorphic comparison. These
coefficients can contain exp(-c T) and are not generally algebraic
forms. In particular all negative coefficients have zero
compact period, while the finite part retains `Tr(C)/N` with the
original 1/N. No inversion of that trace or nonvanishing
assumption is used. The same statement holds coefficientwise
for all actual coupling moments.
The bound N is color dependent; it is not a color-uniform bound
on the uncontracted word or on unknown geometric Gaussian loops.
Here lambda is auxiliary and the coefficients of C are fixed,
or regular in this source normal. If the actual meridian is
coupled to M_lambda, poles of the full modified dimension and
other coefficient factors must be added separately. They are
not removed by the fiber current (15).

## 6. The remaining quantum/source comparison is explicit

The preceding current construction is a genuine global compact
source map, but it is not the full sought geometric map. At an
image point its ordinary physical coherent clock would be
`exp(c v a_lambda)`. The Gauss detour (6)--(9), instead, has

    A_cut=h_lambda/u_lambda.

These are different whole functions. Pullback by Phi_lambda is
not asserted to preserve the finite star product or to implement
the actual quantum-group dressing. The generic-meridian word
also contains the complete nonzero vacuum and source factors,
which must be transported rather than omitted.

Consequently (16)--(20) preserve all actual source currents as
compact currents, and (6)--(9) give a global noncrossing classical
matrix detour, but their compatibility with the actual whole
R/base transport still requires a source-preserving map. Simply
equating the two clocks would skip that missing step. Coupling
lambda to the meridian likewise requires the appropriate chain
rule for meridian shifts; it is not implied by their commutation
when lambda is an independent auxiliary parameter.

The fixed-space defect (4)--(5) and the varying-class torsor
(7) supply exact data for that comparison. They do not remove
the fixed-complete wall tube by a Weyl relabeling. Nor do they
prove geometric-branch continuation, all-loop logarithmic
extension, selected geometric source survival, or a volume limit.

## 7. Exact audit

[audit_compact_exponential_cech_current.py](../experiments/audit_compact_exponential_cech_current.py)
and its
[results](../experiments/compact_exponential_cech_current_results.json)
verify the determinant, retained eigenflag, inverse-flag meridian
normalization, affine transition, whole exponential source gluing,
and normal pole/finite-part coefficients. For every matrix unit at
sizes 2 through 5 they also verify (16), global one-form gluing,
both components and the sign of the actual relative support
identity (17b), the stated pole bound, and the normalized
polynomial trace endpoint. The proof applies to arbitrary N; these are convention
and algebra checks, not finite-level evidence for topology or
geometric period selection.
