# A sourced primitive gauge for the whole actual word and its meridian boundary

27 October 2026. The k=1 source sector can be gauged on the ENTIRE
actual word to a fixed, unit Frobenius density. Its resulting Euler
orientation is the one with a quadratic classical boundary position.
Thus that orientation, which is incorrect for the unsplit original
cap, is legitimate for this precisely transported primitive sector.
The exact quantum clock equations and meridian adapter retain the
adjacent boundary divisors. No equality of the full invariant with
one primitive sector is asserted.

The source decomposition and all normalizations are those of
[the actual all-strand Fourier traces](actual_source_fourier_twisted_traces.md).
This note supplies a concrete word/source transgression, rather than
identifying a sector with a geometric period without a source map.

## 1. The whole-word identity fixes the density and Euler orientation

Use the common right coefficient algebra B=Mat_r(A_0), r=N^(b-2),
with A_0=<H,f | H^N=1,Hf=Q^-1 fH,f^N=0>. Its actual Frobenius
functional is T=sum tau on diagonal entries, with

    tau(f^a e_j)=delta_(a,N-1),
    nu(H)=QH, nu(f)=f, T(ab)=T(b nu(a)).

Write z=xf, u=u_N(z), u_Q=u_N(Qz), v=u^-1, v_Q=u_Q^-1,
J=[(1-z)(1-Qz)]^-1. Scalar functions of z below mean the same
block-diagonal element in B. Let A be the COMPLETED actual word
coefficient matrix, including every off-diagonal tail transition.
The original Euler source uses b=u^-1 A u.

In the primitive k=1 sector its actual density simplifies to

    C_1=Q^-1 H J I_r,       C_1^0=Q^-1 H I_r.

The diagonal tail phases really are independent of the tail label
in this sector; this follows from -j+(j-1)=-1 in the original
marked Fourier resolution. Let

    g=v v_Q=[u u_Q]^-1.

Then the following identities are exact at every original root:

    nu(g)=g,      g^-1 C_1 g=C_1^0,
    c:=g^-1 b g=u_Q A u_Q^-1,
    Phi_1(b)=T(C_1 b)=T(C_1^0 c).                (1)

For the density identity use g(Qz)=J(z)g(z) and Hh(z)=h(Q^-1z)H.
For the trace identity, T is invariant under conjugation by a unit
fixed by nu: T(g^-1 a g)=T(a). The last equality follows by applying
that fact to C_1 b. There is no extra factor of Q from an ordinary
cyclic rotation; T is a Nakayama-twisted trace.

Equation (1) preserves full word composition: conjugation is applied
to the complete matrix A, or to every factor before multiplication.
It never discards off-diagonal tail channels. The original scalar
period remains chi_W gamma_0/N times the sum of ALL Fourier sectors.
The k=1 term in that sum is exactly chi_W gamma_0 T(C_1^0 c)/N.
The other sectors have not been proved negligible or identified
with this one.

For two physical/fused heads with actual fusion C, right multiplication
reverses coefficient composition. Consequently the new-to-physical
basis for c is

    C R_(u_Q),                                          (2)

and in the common multi-head module it is the corresponding common
fusion followed by this same block-diagonal right multiplication.
Indeed (C R_(u_Q))^-1 W (C R_(u_Q))=R_c. This is the opposite
Euler orientation to C R_(u^-1), the basis of the unsplit cap.
The density change in (1) is essential for (2) to represent an
ACTUAL source sector.

## 2. The exact primitive-sector clock equations

Keep the relative clocks D_a=diag(Q^a), D_j=diag(Q^j), right shift
R_f and z=x R_f. Put U_Q=R_(u_Q). Direct nilpotent Euler cancellation
gives the ordered finite matrix identities

    U_Q D_a U_Q^-1=(1-Qz)^-1 D_a,
    U_Q D_j U_Q^-1=(1-z)D_j,
    U_Q^-1 D_a U_Q=(1-Qz)D_a=:A',
    U_Q^-1 D_j U_Q=(1-z)^-1 D_j=:J',
    A'J'=D_aD_j.                                      (3)

The factors 1-z and 1-Qz are units in this nilpotent algebra.
Let U_phys=diag(Q^u) on the physical first head and define its
primitive-basis version U_prim=(C U_Q)^-1 U_phys(C U_Q).
Conjugating the EXACT fusion clock equation yields

    (1-U_prim^-1 A')z=(1-Q A')(1-J').                   (4)

This equation includes every wrapped and top-degree endpoint of
the original fusion. The apparent denominator 1-U_prim^-1 A'
is nilpotent, just as in the original fusion relation. Thus (4)
is an exact polynomial transport equation, not an inverse formula
in the finite root representation.

On the regular commutative principal chart, put delta=1-z and
let A,J denote its undressed relative clock values. At Q=1,
(3) becomes A'=A delta,J'=J/delta. In the rational fusion chart
this gives

    D_-=J-AJ delta+(A-1)delta^2,
    U=A z delta^2/D_-,
    V=J D_-/(z delta^2),
    delta^-2 U -> A/J,       delta^2 V -> J^2.           (5)

Therefore the quadratic classical boundary exists on the correctly
sourced primitive sector, even though it does not arise from the
unsplit cap's orientation. Equation (5) alone does not mark U as
the internal second meridian of the geometric cut. Here V is the
FUSED tail clock, and UV=AJ stays a unit on the stated fixed-A,J
chart. A geometric framing can have a nonunit total braid-axis
clock, so matching the valuation of one position does not identify
the full representation/source map.

There is also a necessary order-of-limits qualification. Equation
(3) retains 1-Qz. If delta=epsilon*zeta and Q=exp(2pi*i*epsilon),

    1-Qz=epsilon*(zeta-2pi*i)+O(epsilon^2).

Thus setting Q=1 before that boundary rescaling loses a leading
term. Formula (5) is a regular classical chart followed by a
classical boundary limit. It is not a uniform quantum boundary
profile or a Gamma normalization formula.

## 3. The full primitive meridian gauge increment is controlled

At fixed Q use the original meridian x=-M/q and sigma(M)=qM.
Keep the same abstract coefficient basis, so sigma(z)=qz. Define

    D_N(z)=sigma(g)g^-1=g(qz)g(z)^-1.

For the actual half-step adapters B_N=u(qz)/u(z), A_N=B_N^-1,
the exact factorization is

    D_N(z)=A_N(z)A_N(Qz),
    D_N(z)^-1=B_N(z)B_N(Qz).                            (6)

Using [the proved half-step bounds](actual_euler_meridian_half_step.md),
in the same flat right-regular metric on |M|=1,

    ||D_N|| <= 64N,     ||D_N^-1|| <= (1+6pi)^2.        (7)

The gauge g itself has exponential condition number, but its
one-step meridian increment has polynomial condition number.
Both statements concern a specified coefficient metric, without
an unproved transfer through physical fusion.

For any actual whole-word family b(M), let c(M)=g(M)^-1 b(M)g(M).
The fiberwise meridian equation is EXACTLY

    sigma(c)=D_N^-1 [g^-1 sigma(b)g]D_N.                 (8)

In particular the sector density C_1^0 is independent of M,
but one must retain the two-sided D_N in (8). Omitting it is not
permitted by the fact that (1) is an inner change at each fiber.
The original chi_W(M), gamma_0(M) and full peripheral ratio still
multiply their original fiber values. At a peripheral pole their
whole rational-map/source-lattice product must be combined before
evaluation; they are not replaced by numerical complete values.

The actual longitude insertion of the original finite state remains
the one in [the marked longitude theorem](quantum_longitude_and_regulator_action.md).
Its internal inserted network need not commute with the Borel
action at the original color. Equation (8) does not assert that
such a coupon is an element of B. It transports the actual
uninserted word families at M and qM, and any supplied two-fiber
linear network map can be conjugated on BOTH fibers before its
original source pairing. This distinction retains the current
terms required by the full geometric comparison.

There are actual-word witnesses for the increment in (8). For
the positive one-crossing word at generic M=3, using the original
balanced color matrices, the correct and omitted-adapter k=1
source values are, respectively,

    N=3 over F_1009: 439 and 293,
    N=4 over F_1009: 630 and 956.

The known external factors are identical in each comparison and
are nonzero on that generic chart. A single sector is not a knot
invariant, but altering only this term while retaining the rest
of the prescribed Fourier sum changes the original source value.

## 4. Regular action transgression and the marked longitude

On the regular multiplication-symbol chart where the actual gauge
has the proved action F(z)=2Li_2(z), conjugating a word kernel by
g changes its phase by

    S_new(z_out,z_in)=S_old(z_out,z_in)
                         -F(z_out)+F(z_in).              (9)

The transported co-source kernel has the OPPOSITE boundary term.
For a full kernel/co-source composition these terms cancel before
taking critical values. This is a whole-word statement: applying
the gauge to successive kernels also telescopes at every internal
node. On a common marked logarithmic chart no imaginary constant
is introduced by (9), since identical endpoint branches cancel.

For the primitive k=1 trace, its bare twisting automorphism
Ad_(C_1^0) composed with nu shifts logarithms only by O(h);
its principal canonical twist is the identity. This does NOT
prove that T(C_1^0 .) has a nonzero regular co-source there:
T detects the nilpotent top degree, and a regular geometric
realization of that source remains a separate construction.
Whenever a source-compatible regular kernel branch is supplied,
the cancellation above preserves its critical action and its
meridian derivative. If that branch is already identified with
the marked geometric critical branch, the longitude derivative
and Bloch-regulator action from the marked longitude theorem
remain the same after (1).

The corresponding one-step scalar symbol is also explicit.
The actual normal-form estimate for g gives, uniformly on
|z|<=1/4,

    D_N(z)=(1-z)^-1(1+O(1/N)).                          (10)

To prove this for the CANONICAL polynomial D_N, not an invalid
quotient of polynomial evaluations, take its finite logarithm:

    log D_N=sum_(a=1)^(N-1)
                      (1+q^(2a))z^a/[a(1+q^a)] modulo z^N.

On each fixed disk of radius<1 its ordinary polynomial right-hand
side tends to -log(1-z), with error O(1/N). For a<=N/2 the
coefficient difference from 1/a is O(1/N); the upper half is
bounded by 2/(N-a) times a geometric tail. The logarithm is
uniformly bounded on |z|<=1/2. Cauchy's Taylor-tail bound for
its exponential is therefore O(2^-N) on |z|<=1/4. This proves
(10) for the canonical finite polynomial. Its leading action
also agrees with 2[Li_2(qz)-Li_2(z)]/h=-log(1-z)+O(h).
This is a real boundary/longitude correction for an UNTRANSPORTED
word kernel; the co-source supplies its inverse in the complete
period. Formula (8) is its finite, ordered counterpart. One
cannot discard it and keep only the bulk longitude symbol.

This transgression does NOT prove that the actual finite sector
selects the regular marked geometric graph, that the other Fourier
sectors cancel subexponentially, or that the full boundary profile
has been transported. In particular the original highest-input
source lies at a fusion wall; a generic regular interior chart
does not itself move that source through the wall. Thus the
geometric identification and global growth gates remain open.

## 5. Verification

[The exact audit](../experiments/audit_whole_word_primitive_source_gauge.py)
and [saved results](../experiments/whole_word_primitive_source_gauge_results.json)
check the whole-word density equality, the opposite Euler basis,
all ordered clocks in (3)-(4), the exact meridian factorization,
and generic actual-word omitted-adapter witnesses. They retain the
entire actual signed word before extracting source diagonal blocks.
The symbolic check verifies (5), the adjacent boundary shift and
the retained product of both position clocks. The direct proofs
above are all-level; tests check conventions and source scope.
