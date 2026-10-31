# The actual cap wall has an exact Fermat-residue quad transition

28 October 2026. This proves a boundary extension of the finite quantum
quad transition, including its source, co-source, and every actual
arbitrary-plat corner. The actual cup corner is an algebraic RESIDUE
of the cyclic source, not an unnormalized limiting vector. Output
covectors require a cyclic shift in addition to the scalar transition.
The local parameter change also has an explicit central Jacobian.
Neither correction may be omitted away from the cusp.

The regular Fourier/chirp source transform was already proved in
[the quad transport note](exact_quantum_quad_source_transport.md).
The new results here are its extension across all Fermat cusps, the
divisor and exact Nth power of its scalar, the actual cap residues,
the dual shift correction, and their simultaneous whole-network
transport. The construction does NOT decompose the transformed
crossing kernels into positive geometric tetrahedron tensors or
select a global geometric integration cycle.

## 1. The compact source line and an identity without denominators

Fix N>=2, d=N-1, q=exp(pi i/N), Q=q^2, and gamma=-q. Let

    Z e_n=Q^n e_n,       S e_n=e_(n+1 mod N),
    W_(k,n)=N^(-1/2)gamma^n Q^(kn+n(n+1)/2).

All root and chirp phases are retained; no division by two modulo N
is used. W is unitary and has the previously proved relations

    W Z^-1 W^-1=S,       W Z^-1 S W^-1=gamma Z.

On the smooth projective Fermat curve

    C_N: u^N+v^N=w^N

put `B(u,v,w)=wI-uZ-vS`. This matrix has rank N-1 at EVERY point
of C_N. For v!=0, its first-order cyclic recurrence determines
every kernel vector from its zeroth coefficient. If v=0, then
u,w!=0 and exactly one diagonal entry w-uQ^j vanishes. These
arguments also cover u=0 and w=0. Thus its right kernels form a
line subbundle L of the trivial rank-N bundle over the entire curve.

The projective quad rotation is the regular automorphism

    rho[u:v:w]=[qv:w:u],      rho^3=id projectively.

The following is an EXACT polynomial matrix identity:

    B(qv,w,u) W = -W Z^-1 B(u,v,w).                      (1)

It follows by multiplying B by -Z^-1 and using the two W relations.
In particular W identifies the kernel fibers even when u, v or w
vanishes. Formula (1) has no forbidden division by a cusp coordinate.
At both even and odd N, `(qv)^N+w^N=u^N`, as required.

## 2. Meromorphic source and co-source frames

Use the homogeneous degree-zero frames

    P_n(u,v,w)=v^n/product_(j=1)^n(w-uQ^j),
    L_n(u,v,w)=v^-n product_(j=0)^(n-1)(w-uQ^j),
    P_0=L_0=1.                                         (2)

Here P is a column, L a row. Direct recurrence gives
`B P=0` and `L B=0`. On the open set uvw!=0 all their entries
are well defined and neither frame vanishes. There exist uniquely
specified meromorphic scalars c and e such that

    W P = c (P composed with rho),
    L W^-1 = e (L composed with rho) S.                  (3)

The S in the second formula is COMPULSORY. Indeed (1) implies
that `L Z W^-1`, rather than `L W^-1`, is a left kernel of the
target B. Since `W Z^-1 W^-1=S`, formula (3) follows. Its scalars
are fixed by the zeroth components:

    c=(W P)_0,
    e=(L Z W^-1)_0.

Thus the same original output cap cannot be transported merely
as an unshifted left Fermat source. It must keep this cyclic shift
or absorb it into the adjacent transformed kernel.

Two direct telescoping identities determine the paired scalar:

    L P = N(w-u)w^(N-1)/v^N,
    L S P = N(w-u)/v.

For the first, the nth summand is `(w-u)/(w-uQ^n)` and the sum
is the logarithmic derivative of `w^N-u^N`. For the second,
each summand is `(w-u)/v`, including the wrapped n=0 term.
Substitute (3) to obtain the exact WHOLE factor

    c e = (w-u)w^N / [v^N(u-qv)].                       (4)

No value of a central norm has been substituted in (4).

## 3. All cusp frames and the exact scalar divisor

Write

    A_j=[Q^-j:0:1], 0<=j<N.

Near A_j use v as local parameter and
`u(v)=Q^-j(1-v^N)^(1/N)`, with the branch equal to Q^-j at zero.
For j>=1 set

    alpha_j=N(-1)^(j-1)Q^(j(j-1)/2)/F_(j-1),
    beta_j=(-1)^j Q^(-j(j+1)/2)F_j,
    F_j=(Q;Q)_j.

Exact root-factorial reflection also gives the simpler forms
`alpha_j=F_(N-j)` and `beta_j=N/F_(d-j)`.

Then the following are regular NONZERO vector/covector frames at A_j:

    P_hat_j(v)=v^(N-j) P(u(v),v,1)/alpha_j,
    L_hat_j(v)=v^j L(u(v),v,1)/beta_j,
    P_hat_j(0)=e_j,       L_hat_j(0)=e_j^t.              (5)

At A_0, P and L themselves are regular with values e_0 and e_0^t.
To prove (5), the only zero factor of the P denominator is at
index j. Its leading term is `v^N/N`. For the L numerator the
zero at index j occurs precisely when n>j. Thus the minimum
orders of the components are respectively `-(N-j)` and `-j`,
attained uniquely at n=j. The other finite factors give exactly
alpha_j and beta_j. Notice the full identity

    alpha_j beta_j=N(1-Q^-j).                           (6)

This covers every v=0 cusp; their two rho-images cover the u=0
and w=0 cusps as well. In particular the kernel line extends at
all 3N cusp points, including even N.

The source P has divisor

    div(P)=-sum_(j=1)^d (N-j) A_j

as a meromorphic section of L. It has no other poles and no zeros,
since its zeroth coefficient is one. Consequently

    degree L=-N(N-1)/2.                                 (7)

This nontrivial degree is a concrete obstruction to a single global
regular normalized source frame. Normalization factors with cusp
zeros and poles are structurally necessary.

Because W is an everywhere invertible constant matrix, (3) now
determines the full divisor of c. It has poles of order N-j at
A_j and zeros of that order at rho^-1 A_j. The tangent line
`w-uQ^j=0` cuts C_N at A_j with multiplicity N; the line
`u-qvQ^j=0` similarly cuts it at rho^-1 A_j. Hence their divisors
and the anchor `c(A_0)=N^-1/2` give the exact algebraic identity

    c(u,v,w)^N = N^(-N/2)
      product_(j=1)^d [
        (1-Q^j)(u-qvQ^j)/(w-uQ^j)
                     ]^(N-j).                          (8)

For completeness, divide the two sides of (8). The divisor
calculation shows that their quotient has neither poles nor zeros
on the smooth compact curve, so it is constant. Evaluation at A_0
sets that constant to one. This also proves that c has no additional
zeros on uvw!=0. Its actual branch is the Fourier sum in (3), not
an independently chosen Nth root. Formula (4) then fixes e with
its original phase. Thus (8) specifies a genuine marked algebraic
source torsor, including the boundary divisor.

## 4. Actual corners are residues, not discarded limiting factors

For j>=1, (5) gives the exact algebraic residue formulas

    e_j = alpha_j^-1 Res_(A_j) v^(N-j-1) P dv,
    e_j^t = beta_j^-1 Res_(A_j) v^(j-1) L dv.           (9)

At A_0 they are `Res P dv/v=e_0` and `Res L dv/v=e_0^t`.
Only the nth component with n=j has exponent -1 in (9);
every other component is regular in that differential.

For the actual fused cup corner j=d, the constants simplify to

    alpha_d=1-Q,       beta_d=N.

Therefore

    e_d=(1-Q)^-1 Res_(A_d) P dv,
    e_d^t=N^-1 Res_(A_d) v^(N-2) L dv.                 (10)

In particular the ordinary unregularized cyclic source has a
SIMPLE pole at this actual cap wall, with residue `(1-Q)e_d`.
Omitting it would remove the actual cup. The output d-corner
instead requires the displayed power `v^(N-2)` and factor N^-1.
These factors are determined by the source and co-source and
cannot be replaced by a common guessed normalization.

Let `a_j=gamma^j Q^(j(j+1)/2)`. At A_j the regularized transitions
in (3),(5) have the exact nonzero coefficients

    lim v^(N-j)c/alpha_j = a_j/sqrt(N),
    lim v^j e/beta_j = Q^j/[sqrt(N)a_j].                 (11)

Indeed W e_j is `a_j/sqrt(N)` times the Fourier vector Q^(jn).
The target left frame is Q^(-jn), and its cyclic shift contributes
Q^-j, giving the second factor in (11). Their product is Q^j/N,
which also follows from (4),(6). The A_0 values are both N^-1/2.
Thus every actual corner survives this quad transition, with its
original nonzero phase and a polynomial, explicitly known factor.

If the target affine coordinate is

    zeta=qv/u(v),

the exact differential change is

    dv/v=(1-v^N)d zeta/zeta
         = [1/(1-zeta^N)]d zeta/zeta.                   (12)

The factor in (12) is another REQUIRED central factor. It is one
at the cusp, but must be retained when transporting the whole
relative form or continuing it away from that point. This is
particularly relevant when a norm later specializes to a number.

## 5. The whole actual arbitrary-plat source transports at once

Use the exact actual pair-fused word B_beta and its current quotient
from [the arbitrary-bridge transport theorem](actual_rogers_bridge_transport.md).
Its original reduced scalar is

    P_(beta,N)=chi_beta N^(1-k)
                    <e_out|B_beta|e_in>,                (13)

where every input pair is `(d,0)`, each ordinary output pair is
`(0,d)`, and the marked output pair is `(d,0)`. The original
Cartan, framing and peripheral factors remain chi_beta, or remain
inside B_beta according to the original convention.

Replace EACH of the 2k input columns and 2k output rows by its
corresponding independent residue in (9)--(10). This is an exact
4k-variable residue presentation of the FULL source matrix element,
not only an equality of one source vector. Equivalently, use the
regular frames P_hat_j,L_hat_j in (5) and take the product of the
small source circles with measures `dv_h/(2pi i v_h)`. Every form
then has a specified original local lift and coefficient. In the
unregularized form the explicit additional normalization is

    [N(1-Q)]^-k,

with factors `v^(N-2)` on the k output d-corners, ordinary dv on
the k input d-corners, and dv/v on all 0-corners.

At any selected head insert W as the quantum quad frame change.
For a full tensor T use

    T'=(tensor W_out) T (tensor W_in)^-1.

The transformed input is exactly c times the target P frame.
The transformed output is exactly e times the target L frame
WITH its S insertion, as in (3). If desired that S is absorbed
into T' by literal multiplication on that output. Consecutive
slice changes cancel exactly. Apply the actual coordinate change
rho to each corresponding source curve, retaining (12), and take
the image of the specified small source cycle. Thus all input
and output cap residues and their pairings are preserved for an
arbitrary number of bridges and any actual word. This is an exact
source-preserving nonlinear quad transition at the cap wall.

This statement is about the original full word and its transported
marker. The Ward corner in (13) cannot be applied separately to
cyclic bulk/sewing summands that are not Hopf intertwiners. Such
summands must retain the full marked row from the bridge theorem
and their actual Ward defects. The complementary
[marked augmentation theorem](ward_cyclic_wall_contraction_and_marked_augmentation.md)
gives the exact co-source homotopy and rank-two current correction,
while proving that the unit augmented wall class survives.

## 6. Uniform source bounds at the wall and on fixed-log root charts

There is no exponential normalization hidden at the original cap
corners. More precisely, there are absolute constants c,C>0 such
that, for every N>=2, every j, and `|v|<=1/(16N)`, the regular
frames in (5) (with P,L at j=0) satisfy

    c <= ||P_hat_j||_2, ||L_hat_j||_2 <= C.              (14)

Here u(v) has the specified local branch. The corresponding target
P and L composed with rho have norms between `c sqrt(N)` and
`C sqrt(N)`. The S insertion is unitary. Thus the regularized c
and e coefficients in (11) have magnitudes between `c/sqrt(N)`
and `C/sqrt(N)` throughout that micro-collar, including its cusp.

Here is a direct uniform estimate. Every nonzero root factor has
`|1-Q^r|>=4/N`. The perturbation of u from Q^-j is at most
`C|v|^N/N`. Relative errors in the products of nonzero factors
are therefore bounded uniformly, above and below. The unique
vanishing factor is exactly

    1-(1-v^N)^(1/N)
       =v^N/[1+delta+...+delta^(N-1)],
    delta=(1-v^N)^(1/N),

whose denominator has magnitude comparable to N. After dividing
by alpha_j or beta_j, all components are bounded by a geometric
sequence in their cyclic distance from j. For example, the right
components with n>=j are bounded by
`C |v|^(n-j)/|F_(n-j)| <= C/64^(n-j)`; the wrapped components
with n<j have distance N-j+n. The latter formula follows by the
same exact factorial reflection used in the bridge source note.
The left components use distance j-n modulo N. Their jth
components remain bounded away from zero. This proves (14).
At rho A_j the first target coordinate is O(v), while the ratio
of its other two coordinates is a unit root times `1+O(|v|^N/N)`.
Its N individual source coefficients are consequently bounded
above and below by constants. Unitarity of W proves the stated
transition bounds.

For the original corners j=0,d the normalization constants themselves
are polynomial: they are 1, 1-Q, and N. The algebraic factors
alpha_j,beta_j for a bulk j can have factorial size; (5) retains
them exactly and makes no contrary assertion.

There is also a two-sided polynomial bound on NONDEGENERATE
fixed-log root charts. Let U+V=1, with U,V in a fixed compact
subset of C minus {0}, and choose bounded compatible logarithms
a,b, `exp(a)=U`, `exp(b)=V`. Put

    u=exp(a/N), v=exp(b/N), w=1.

Then for some C_K independent of N,

    N^(-C_K) <= |c|, |e| <= N^(C_K).                   (15)

This follows directly from the exact algebraic norm (8). The
weighted baseline product has magnitude

    product_(j=1)^d |1-Q^j|^(N-j)=N^(N/2),

by pairing j and N-j. The remaining ratio in (8) is
`(u-qvQ^j)/(1-uQ^j)`. Its logarithmic magnitude is
`O(1/min(j,N-j))`, apart from a fixed number of endpoint factors
which remain bounded above and below. Those endpoint limits do
not vanish: a or a-b-pi*i could equal the relevant 2pi*i integer
only if U=1 or U=-V, both excluded by U+V=1 with UV!=0.
Summing with weights N-j, and dividing by N in (8), gives
`|log|c||<=C_K log N`. In (4), `1-u` and `u-qv` each have
size comparable to 1/N on this chart, so ce is bounded above
and below, proving the bound for e.

The actual cap branch is `a=2pi*i+Log(1-V)`, and the 0-corner
branch has `a=Log(1-V)`. Their regularizations multiply c by
`v/(1-Q)` or 1, and multiply e by `v^d/N` or 1. These factors
are also bounded by powers of N on the stated charts. The
central Jacobian in (12) is a retained nonzero bounded function
there. Thus neither the source nor co-source transition introduces
an exponential loss on a marked nondegenerate chart. This is a
local source statement, not a selected geometric saddle estimate.

## 7. What this crosses, and what it does not

The original source corner now has an actual compactified cyclic
source realization, nonzero local quad coefficient, exact co-source
correction, and fixed boundary cycle. Its scalar torsor is specified
by (8) and the Fourier anchor, with no arbitrary root choice and no
lost central Jacobian. The distinction between a source flag and a
geometric tetrahedron shape has not been bypassed: the central
Fermat ratio U=u^N/w^N undergoes the rational map `U -> 1-1/U`,
but U has not thereby been marked as an actual triangulation shape.

Nor has the conjugated ACTUAL crossing T' been factored here into
the desired positive geometric tetrahedron tensors. A unitary
change of the finite head basis always defines T'; that definition
does not prove the missing factorization. Finally, the nonzero
local cusp residue does not alone show that its global continuation
has nonzero intersection with the hyperbolic critical cycle.
Those are the remaining kernel and global-cycle comparisons.

The source correction this note forces is nevertheless explicit:
keep the cap residue, the dual cyclic shift, the scalar branch (8),
and the central Jacobian (12). A proposed positive-quad transition
that omits any one of them is not the original pointed network.

## 8. Exact checks

The [audit](../experiments/audit_cap_wall_fermat_quad_residue.py) and [saved results](../experiments/cap_wall_fermat_quad_residue_results.json) check 240 generic Fermat points at N=2,...,11, the exact polynomial intertwiner, compulsory dual shift, whole paired scalar, and (8). They check all 195 projective cusps at these levels, all corner residue orders and constants, and nine full tensor source contractions with one, two and three bridges. Finite fields use the unnormalized matrix sqrt(N)W, so these are exact checks with no numerical square-root choice. Twenty high-precision micro-collar diagnostics through N=64 also check the source and co-source norm conventions in (14); the uniform proof is the product estimate in Section 6. The arguments above, rather than the finite checks, prove all N.