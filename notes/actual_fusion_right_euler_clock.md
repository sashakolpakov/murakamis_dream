# Exact fusion relates the right Euler operator to physical clocks

Research proof, 27 October 2026. The actual two-leg fusion kernel
gives an exact polynomial operator relation between the RIGHT
lowering coefficient and physical/relative clocks. All nilpotent
endpoints are retained. This provides a concrete coordinate
relation for the Euler cap rather than guessing that its argument
is a physical Fourier momentum. It does not yet supply a geometric
period map or a selected geometric sector.

## 1. The actual finite kernel

Use the [actual Borel fusion](actual_borel_regular_fusion_and_divided_cap_period.md)
on two nilpotent heads. Their highest K eigenvalues x,y are
invertible. Set F_j=(Q;Q)_j, with Q of exact order N. Relative
basis vectors are f^a e_j, where f is the TOTAL physical lowering
operator acting on the LEFT. Their images under the actual fusion
C are f^a(e_0 tensor e_j). In the physical basis (u,v), the kernel
is exactly

\[
 C_{u,v;a,j}=
 \begin{cases}
 x^{u-a}\displaystyle\frac{F_aF_v}{F_{a-u}F_j},
       &0\leq u\leq a,\quad v=j+a-u<N,\\
 0,&\text{otherwise}.
 \end{cases}                                                \tag{1}
\]

To prove (1), write f=A_0+B_0 with A_0=F_1 and
B_0=K_1 inverse F_2. Then B_0 A_0=Q A_0 B_0. In the
q-binomial expansion of f^a, the term with u first-leg lowering
steps has coefficient F_a/[F_u F_(a-u)]. Acting on the source
gives F_u from the first leg, x^(u-a) from the K_1 inverses,
and F_v/F_j from the second leg. Terms exceeding the second
nilpotent head vanish. This gives (1) with no asymptotic step.

In the ordering by a on the relative side and u on the physical
side, C is upper block triangular. Its diagonal blocks are
F_a times the identity. They are units, so C is invertible.
The kernel depends on x, but not on y.

Let D_a and D_j be the relative diagonal clocks Q^a and Q^j.
Let U,V be the physical diagonal clocks Q^u and Q^v. Equation
(1) immediately gives

\[
                      C D_aD_j=UV C.                      \tag{2}
\]

## 2. Right lowering and its exact clock equation

Right multiplication R_f in the coefficient algebra is

\[
 R_f(f^a e_j)=
 \begin{cases}f^{a+1}e_{j-1\bmod N},&a<N-1,\\0,&a=N-1.
 \end{cases}                                               \tag{3}
\]

This is different from physical total lowering, which is LEFT
multiplication in the fused module. Define the transported
operators

\[
 A=C D_a C^{-1},\qquad J=C D_j C^{-1},\qquad
                          f_R=C R_f C^{-1}.
\]

Then the following are exact finite matrix identities:

\[
 \boxed{\quad
       x(1-U^{-1}A)f_R=(1-QA)(1-J),\qquad AJ=UV.
 \quad}                                                    \tag{4}
\]

They are not assertions merely about interior matrix entries.
Before conjugating, the first identity reads

\[
 x C R_f-xQ U^{-1}C R_fD_a=C(1-QD_a)(1-D_j).              \tag{5}
\]

For j>0 and a<N-1, use (1) at consecutive relative labels:

\[
 \frac{C_{u,v;a+1,j-1}}{C_{u,v;a,j}}
 =x^{-1}\frac{(1-Q^{a+1})(1-Q^j)}{1-Q^{a+1-u}}.          \tag{6}
\]

The polynomial equation obtained by clearing the denominator
in (6) is valid even when that denominator is zero. At the new
support u=a+1, the left coefficient vanishes and the old kernel
entry is zero. At any other excluded row both sides vanish.

For j=0, R_f sends the second label to N-1. Its new kernel
support is ONLY u=a+1,v=N-1. The left coefficient
1-Q^(a+1-u) is then zero, and the right side is zero because
1-Q^j=0. This is an actual wrapped endpoint, not a discarded
row. For a=N-1 the left side is zero by (3), while the right
side has factor 1-Q^N=0. These observations establish (5) on
every matrix entry.

Finally R_f D_a=Q^(-1)D_a R_f, so conjugating (5) gives the
ordered equation in (4). Also, exactly,

\[
 [A,J]=0,\qquad A f_R=Q f_R A,\qquad
                  J f_R=Q^{-1}f_R J.                     \tag{7}
\]

These follow directly from the relative basis, including its
cyclic j endpoint, at the root Q^N=1.

## 3. The apparent denominator is nilpotent at the actual root

It would be incorrect to divide the first equation in (4) by
1-U inverse A as an actual finite operator. In fact

\[
                         (1-U^{-1}A)^N=0.                \tag{8}
\]

Indeed C is upper block triangular with scalar diagonal blocks
F_a. Conjugating D_a by C yields an upper block triangular A
with diagonal blocks Q^u. Therefore U inverse A is upper block
triangular with every diagonal block equal to one. Its difference
from one is strictly upper block triangular, which proves (8).

Thus (4) is an exact polynomial transport identity through this
endpoint, not a rational inverse formula for f_R. It retains a
singular clock divisor that a prospective period transform must
handle. No scalar normalization removes (8).

## 4. A useful prospective principal relation, with its scope

The [actual cap](actual_euler_cap_cauchy_boundary.md) uses the
Euler argument x f in the RIGHT coefficient algebra. On a
commutative principal-symbol chart associated with (4), that
argument would satisfy

\[
 z(1-A/U)=(1-A)(1-J),\qquad AJ=UV.                       \tag{9}
\]

Where 1-A/U is invertible this can be written

\[
                        z=\frac{(1-A)(1-J)}{1-A/U}.       \tag{10}
\]

Equations (9)-(10) specify the algebraic symbol relation forced
by the exact kernel. They do not prove that a particular
semiclassical symbol chart exists for the full selected word,
that it is symplectic, that z equals a geometric Fourier
momentum, or that its divisor is traversed by the original
source class. In particular (10) is NOT the finite root
matrix equation, because of (8).

This still makes a concrete step beyond the former unspecified
right-Euler/physical-clock relation: the actual finite kernel
and all its endpoint terms are now explicit. A geometric
comparison must use this relation and the original cap, rather
than silently replacing the cap argument by another momentum.

## 5. Truncated generic-Q kernel exposes a top-degree defect

For a Q not satisfying Q^N=1, retain the SAME finite formula
(1), provided F_1,...,F_(N-1) are units, and the SAME nilpotent
shift (3). These are well-defined matrices, without claiming
they form the actual generic-q word module. Let Pi_top project
to a=N-1. The exact finite-kernel identity is now

\[
 \begin{aligned}
 x C R_f-xQ U^{-1}C R_fD_a
 &=C(1-QD_a)(1-D_j)\\
 &\quad -(1-Q^N)C(1-D_j)\Pi_{\mathrm{top}}.                  \tag{11}
 \end{aligned}
\]

The same entry proof applies away from a=N-1, including j=0.
At a=N-1 the left side vanishes by truncation. The correction
in (11) subtracts exactly the nonzero right side there.

Consequently the root identity has a visible normal endpoint
term before root specialization. Dividing (11) by 1-Q^N and
discarding its last term would change the kernel calculation.
This is only a statement about this explicit finite kernel;
it does not provide a moving-q extension of actual braid
intertwining, fusion of divided powers, or the original whole
q-normal source. Those further comparisons remain necessary.

## 6. Exact checks

The [audit](../experiments/audit_actual_fusion_right_euler_clock.py)
and [saved output](../experiments/actual_fusion_right_euler_clock_results.json)
pass at N=2,...,9 with unequal x=3,y=7. At each actual root
they compare (1) to the literal coproduct fusion matrix and
check (2), (4), (7), (8). Eight additional generic-Q kernel
cases check the full nonzero endpoint correction (11).
The all-level entry proofs above establish the theorem;
these exact checks verify its conventions and endpoints.
