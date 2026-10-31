# A regular actual mixed-circle port chart at the belt boundary

29 October 2026. The old diagonal pair chart for the actual mixed
circle is singular at w=-1, precisely where the new belt packet is
concentrated. This note resolves that local chart with bounded
meridian matrices and preserves the FULL threaded-circle equations.
It does not select a bare-crossing state/observable convention, nor
identify the complete global stack representation from vertex flags.

The later [typed global composition](actual_belt_stack_typed_character_composition.md)
now completes the outer closed-leg/peripheral checks kept separate in
this local note, and the [full filling assembly](actual_long_filled_octahedral_belt_stack_volume.md)
records the resulting any-subset volume equality. The local calculations
below remain the independent input to that global proof.

The local all-port convention is the one in
[the original literal port lift](actual_pretzel_port_lift_and_geometric_anchor.md):
incoming rotated pair (g(z),h(z)), outgoing (g(Uz),h(Uz)), with

    h(z)g(z)=diag(w,w^(-1)),
    U=(wY-1)/(w-Y).                                    (1)

Here Y is the SOURCE-selected inner critical parameter. In the new
[physical-color packet](actual_belt_stack_auxiliary_color_inner_packet.md)
it is holomorphic near w=-1,Y=i,H=1. It is not the physical meridian.

## 1. A bounded irreducible pair

Put c=w+w^(-1) and use

    a=-[[1,1],[0,1]],
    b=-[[1,0],[c-2,1]],
    A=ba=[[1,1],[c-2,c-1]].                            (2)

Both main meridians have trace -2 and determinant one. Their product
has trace c. At c=-2 it is a NONCENTRAL trace-minus-two parabolic.
The fixed flags of a,b are infinity and zero, so the pair stays
irreducible for c near -2. This avoids diagonalizing the parabolic
product and then calling a diverging diagonal frame bounded.

For w!=+1,-1 this pair is simultaneously conjugate to the original
g,h pair: their product eigenvalues and the two parabolic traces
agree, and their distinct flags determine the conjugacy on the
irreducible chart. The following formulas also give an explicit
regular continuation of its rotated action.

Choose sqrt(U) through 1 near w=-1,Y=i, and set

    beta=w(Y-1)/[(w-1)(w-Y)sqrt(U)],
    alpha=[sqrt(U)+1/sqrt(U)-beta*c]/2,
    K=alpha I+beta A.                                 (3)

All displayed denominators are nonzero in a fixed neighborhood.
For w!=+1,-1 this equals

    beta=[sqrt(U)-1/sqrt(U)]/[w-w^(-1)].               (4)

Indeed U-1=(w+1)(Y-1)/(w-Y). Thus K has determinant one and
eigenvalues sqrt(U),1/sqrt(U) on the A-eigenflags w,w^(-1).
It is exactly the conjugate of diag(sqrt(U),1/sqrt(U)), which sends
g(z) to g(Uz) in the old chart. Consequently the ACTUAL rotated
mixed-circle map is

    (a,b) -> (K a K^(-1), K b K^(-1)).                 (5)

This is a local all-port statement, not an inference solely from a
trace identity. Under w->w^(-1) one has U->U^(-1), and (4) and
alpha are unchanged. The regular K therefore descends holomorphically
to c near -2 when the selected Y is even in eta for w=-exp(eta).
This is exactly the evenness supplied by the physical-color packet.

## 2. Original unrotated ports and the auxiliary meridian

The literal bends, including their inverses, give the unrotated ports

    (a_orig,b_orig)=(K b K^(-1), b^(-1)),
    (r_orig,s_orig)=(K a^(-1)K^(-1), a).               (6)

Their common disk product is

    P=b_orig a_orig
     =b^(-1)K b K^(-1)
     =a K a^(-1)K^(-1).                               (7)

The last equality uses [K,A]=0, with A=ba. Direct multiplication gives
the REGULAR trace formula

    D=Tr P
     =2+(w-1)^2(Y-1)^2/[(w-Y)(wY-1)].                (8)

For w!=-1 this is exactly the old formula
((w-1)/(w+1))^2(U+U^(-1))+8w/(w+1)^2; its apparent pole is
removable on the SOURCE relation(1).

Put Delta=1-YD+Y^2, choose sqrt(Delta) through 1+i, and define

    J=(I-YP)/sqrt(Delta),
    C=(YI-P)/sqrt(Delta).                             (9)

They commute with P, have determinant one, and JC=-P. The original
threaded half-twist equations remain EXACTLY

    r_orig=C^(-1)b_orig C,
    s_orig=C^(-1)b_orig a_orig b_orig^(-1) C.           (10)

One can verify them without roots by using I-YP and YI-P; their
common scalar cancels from conjugation. Equivalently Ja_orig=aJ,
together with(7) and JC=-P, proves(10). They are rational identities
on the old nonsingular chart and both sides are regular here, so
their continuation includes w=-1. No group relation is replaced by
only its trace.

On the full stationary mixed source, the previously proved identities
give D=-(L+L^(-1)), L=(H-X)/(1-HX), and the marked auxiliary meridian
C has eigenvalue H^(-1/2) on the P-eigenflag with eigenvalue -L^(-1).
This is the same ACTUAL circle and preferred disk-word marking as
[the typed longitude theorem](actual_mixed_crossing_circle_preferred_longitude.md).
The eigenflag may move through the parabolic limit; the matrices in
(2)--(10) remain bounded. Nothing here asserts a moving-q continuation.

## 3. Exact complete matrices and the six octahedral flags

At w=-1,Y=i,H=1,

    A=[[1,1],[-4,-3]],
    K=I-(i/2)(A+I),
    P=[[-1+2i,-1],[-4,-1-2i]],
    C=I-(P+I)/(1+i).                                 (11)

The outer flag of A is -1/2; the inner flag of P and C is -i/2.
The four actual rotated port flags are

    a:infinity, b:0,
    KaK^(-1):-(1+i)/2, KbK^(-1):-(1+i)/4.

The HOLomorphic Möbius map

    M(zeta)=(zeta+1/2)/(zeta+i/2)                      (12)

sends, in that order, the outer/inner flags to 0/infinity and the
four port flags to 1,-i,i,-1. These are the six ideal vertices of
a regular octahedron. In this exact frame one obtains

    M A M^(-1)=[[-1,0],[2-2i,-1]],
    M P M^(-1)=[[-1,-2+2i],[0,-1]],
    M C M^(-1)=[[1,-2i],[0,1]],
    M J M^(-1)=[[1,2],[0,1]].                         (13)

In particular the actual inner meridian translates by -2i, while
the preferred disk product translates by 2-2i (its central sign
has no projective effect). Their ratio is 1+i. This is a literal
matrix/peripheral calculation, not a ratio guessed from a Hessian.
The source prediction agrees: at eta=chi=0 its physical color action
has j_chi_chi=(-1+i)/pi; with U_geom=-2i chi and the marked longitude
log V_geom=-2 partial_(Log H)(2pi i j), the same ratio is 1+i.

## 4. The separate global geometric lift

The old local source-to-character construction now extends regularly
through the ACTUAL belt saddle and retains every port and auxiliary
meridian. Its six complete ideal flags and the inner peripheral word
are also explicit. These remove a genuine singular-chart problem.

They do NOT alone identify the full global stack holonomy with its
two-octahedron face quotient. The global argument additionally
transports the actual bare R interfaces and bends in their literal
orientation, composes the typed maps, imposes the outer auxiliary
closure, and matches its primitive meridian/longitude. A bare R
eigenphase can give the inverse of a state-versus-observable Hurwitz
graph; it cannot select that convention by analogy. Matching six
ideal flags is also weaker than checking all the face maps.

The [separate typed composition proof](actual_belt_stack_typed_character_composition.md)
now supplies that finite marked map, including the original nested
head snakes, incident mixed coupons and untouched auxiliary pivot.
That proof, the
[uniform filling-existence theorem](finite_geometric_certificate_uniform_filling_existence.md)
and general completion/calibration theorem identify the selected
long-filling action with the actual filled hyperbolic volume. Neither
the local regularization nor the quantum color packet substitutes
for that independent marked-map proof.

Section6 below checks the complete CUT-PIECE face anchor as well.
The global outer collar and closed-leg peripheral dictionary are
proved in the linked typed-composition note.

## 5. The opposite retained half twist, with its actual circle meridian

There is an additional exact all-port statement using the SAME K and P.
The positive unrotated half-Hurwitz rule with an auxiliary centralizer
Q is

    r_orig=Q^(-1) a_orig^(-1)b_orig a_orig Q,
    s_orig=Q^(-1) a_orig Q.

It is solved by Q=J^(-1). Indeed Ja_orig=aJ gives the second
equation; the first then reduces to a^(-1)P=K a^(-1)K^(-1),
which follows from(7). Thus the opposite retained half twist has
circle meridian J^(-1), rather than silently using C unchanged.
At completeness this meridian translates by -2 in the frame(12),
whereas C translates by -2i. The SAME preferred disk product P
translates by 2-2i. Its two primitive cusp ratios are consequently

    (2-2i)/(-2i)=1+i,   (2-2i)/(-2)=-1+i.             (14)

These are the actual two half-twist meridians. On the full mixed
branch the positive-circle color condition is imposed on J^(-1),
not on C. Matching that flag condition to the typed reflected source
is still required; one must not reuse the negative-half mixed
parameter H without this check. This addition proves both complete
typed matrices, not an unproved global sharp/reflection adapter.

## 6. Every complete white and inner shaded face map

Use the normalized frame(12), now with the PRECISE labels

    X0=0, X1=infinity, Y+=1, Y-=-1, Z+=-i, Z-=i.

The white faces of the existing literal two-octahedron cut table are

    W0=(0,1,i), W1=(0,-1,-i),
    W2=(infinity,1,-i), W3=(infinity,-1,i).

Their reflections are the following antiholomorphic maps, with
c0=(1+i)/2:

    r0(z)=c0+(1/2)/(conjugate(z)-conjugate(c0)),
    r1(z)=-c0+(1/2)/(conjugate(z)+conjugate(c0)),
    r2(z)=i conjugate(z)+1-i,
    r3(z)=i conjugate(z)-1+i.                         (15)

Direct Gaussian-rational matrix multiplication gives the FULL PSL
isometries (hats denote conjugation by M):

    a_hat=r2 r0, b_hat=r1 r2,
    a'_hat=r3 r0, b'_hat=r1 r3,
    A_hat=r1 r0.                                    (16)

Thus all white-face holonomies are matched, not only the fixed
flags of the meridians. Develop the second octahedron as r0(P_+),
using W0 as the face-tree pairing.

The inner shaded faces are

    C_face=(infinity,1,i), D_face=(infinity,-1,-i).

The literal threaded-port equations give the two shaded pairing
maps gamma_+=J a', gamma_-=b'J^(-1)=J^(-1)a. In the M frame they
are EXACTLY

    gamma_+=[[3i,1-i],[1+i,-i]],
    gamma_-=[[i,1-i],[-1-i,i]].                       (17)

They have the following complete three-vertex actions:

    gamma_+ r0(infinity,-1,-i)=(infinity,1,i),
    gamma_- r0(infinity,1,i)=(infinity,-1,-i).          (18)

These are r0(D_face)->C_face and r0(C_face)->D_face, precisely
the TWO cross-copy shaded gluings of the actual retained half twist.
They check the third vertex as well as the circle flag and one port.
A holomorphic Mobius map is uniquely determined by three distinct
ideal points; therefore these are the entire face isometries in the
existing positive regular-octahedron certificate. Its matched canonical
horospheres and edge/cusp completion are consequently the same ones.

Equations(16)--(18), together with the reversible original disk cut,
identify the COMPLETE local source representation with the actual
geometric cut-piece holonomy. The reflected half twist uses the same
unmarked cut quotient with its actual changed inner meridian
J^(-1)=-C P^(-1); the preferred disk word P is retained. Bare outer
R collars must still be read with their literal bends and primitive
peripheral words. No global deformed-stack claim is deduced solely
from this complete-point calculation.

The [focused symbolic audit](../experiments/audit_actual_belt_stack_regular_parabolic_port_chart.py)
checks EXACT rational-function/Gaussian-rational identities: the
regular centralizer and reciprocal descent, both signed threaded
port equations, complete matrices and flags, all five white identities,
and BOTH three-vertex shaded maps. It does not replace the separate
global outer collar/peripheral proof.

## 7. The oriented outer-pants boundary word

There is a concrete boundary-path check that is useful for that last
peripheral proof. The incoming pants has shaded triangle
(X0,Y+,Z+)=(0,1,-i). The holomorphic map

    T(zeta)=((1+i)/2)(zeta-1)/zeta

sends its three punctures to infinity, zero, one. Conjugating the
EXACT white-face meridians in(16) gives

    a_T=[[-1,0],[-2,-1]],
    b_T=[[-3,2],[-2,1]],
    A_T=[[-1,-2],[0,-1]].                             (19)

Use the upper-half-plane orientation for its doubled ideal triangle.
At punctures zero and one, the upper-half-plane cusp coordinates
-1/zeta and -1/(zeta-1) make a_T and b_T each translation by -2.
At infinity, A_T^(-1) is translation by -2 as well. They are therefore
the consistently oriented boundary loops of a compact truncation of
the pants: its oriented top horocycle goes to the left. Their based
boundary relation is EXACTLY

    (A^(-1)) b a=I.                                  (20)

Thus the oriented OUTER boundary word of these actual puncture paths
is A^(-1), not A. Reversing the pants orientation reverses all three
paths together. This is an oriented face/path certificate, independent
of any computed source Hessian.

To call(20) the preferred POSITIVE auxiliary longitude, the actual
closed auxiliary orientation and its original ordinary cup/pivot
are transported to this pants boundary in the linked typed-composition
proof. That operation also determines which A-eigenflag has the
positive auxiliary meridian eigenvalue. Neither choice is inferred
just from(19). The geometric boundary calculation supplies its
explicit path, while preserving that distinction.

The local signed boundary charts and oriented pants word are inputs to the separate global filled-volume assembly, not a replacement for it.