# Three complete belts: the saturated source and the marked-pair obstruction

29 October 2026. On the genuine six-head saturated source, three
disjoint positive complete-circle forms define an explicit positive
Gram. They do NOT have a finite dual norm for the original marked
co-source. There is an all-level source vector whose three-belt energy
is zero and whose original marked evaluation is exactly ONE.

The correctly typed original cap inequality uses C tensor C tensor H,
not C tensor C tensor C. It detects the same vector with a polynomial
lower bound. Thus a simple tensor-cube DCT or a scalar Frobenius
branch cannot be used to claim a marked trivalent source theorem.
This result retains the full divided-current kernel and root normals.

## 1. The actual six-port space and the three circle operators

Use d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, N>=2. The balanced physical
generators are Ecal=-F^dagger, K^dagger=K^-1. Let

    L=(-1)^d U_d(Omega/2), C=P L>=0, H=L P=P C P>=0,

where P exchanges the two physical legs, not a braid crossing. All
the literal ordinary-circle pivots and Cartan phases are retained.
Their positivity and kernels are the
[complete-circle theorem](actual_complete_circle_reflection_positive.md).

Let S be the SATURATED generic-q specialization inside the full
six-head H=0 invariants. The
[divided-power source theorem](actual_six_port_divided_power_source_kernel.md)
identifies it, with every original cup/braid word included, as

    S = Inv_root,H=0 intersect ker J_E,6,
    ext(S)=ker(J_E,4:W->Llow),
    W=(V_N^tensor4)_(degree2d), dim S=(N^3+N)/2.         (1)

The maps Phi:W->Inv and ext are the specified actual source maps,
with ext extracting final physical colors(0,d) times x^d/N.
No semisimple projection is substituted for (1).

On W the three disjoint physical pair Casimirs become

    A1=Omega12, A2=Omega34,
    A3=F4 Ecal4+(q+q^-1)I.                              (2)

For completeness A3 is EXACTLY ext Omega56 Phi. Split the six heads
into A=1234 and B=56. On an invariant vector, E_B=-K_B E_A,
F_B=-K_A F_A, K_B=K_A^-1. Using F_B K_B=Q K_B F_B and
E_A K_A=Q^-1 K_A E_A gives F_B E_B=E_A F_A on that vector.
The actual commutator [Ecal_A,F_A]=(q-q^-1)(K_A-K_A^-1)
therefore turns Omega_B into Omega_A. On W, K_A=1, proving (2).
In particular the reduced operators in (2) are not guessed trace
variables. They commute on the actual invariant space and preserve S.

The positive unmarked-belt form is

    G_C(v,v)=v^dagger(C12 tensor C34 tensor C56)v.         (3)

Its kernel equals that of L12 L34 L56, since the product of the
three physical P maps is invertible. This kernel assertion does not
identify (3) with an original marked link closure.

## 2. Full cluster projectors, including their first normals

Let c0=q+q^-1. Its actual root cluster is {0,d}: c0=cd, and it is
DOUBLE for every N>=2. The distinct other nodes are
c_j=q^(2j+1)+q^(-2j-1), 1<=j<=floor(d/2).
Let e0(z) be the FULL Hermite cluster polynomial: value one and
derivative zero at c0, and value/derivative zero at the other double
nodes (value zero at the possible odd simple node). It may be given by

    l0(z)=product_(c!=c0)(z-c)/(c0-c),
    e0(z)=l0(z)^2[1-2l0'(c0)(z-c0)] mod P_N(z).         (4)

All denominators are nonzero at the fixed level. Thus e0(Ai) is an
actual root cluster projector, not an eigenvalue-only substitution.
Write E000=e0(A1)e0(A2)e0(A3). It preserves S and every root normal
within the chosen joint cluster. Its rank on S is five, as also
follows from the five admissible generic branches of {0,d}^3.

The regular generic pair projectors give an elementary annihilation
identity. The branch (d,0,0) has no generic invariant: a positive
spin d cannot couple two spin-zero channels to an invariant. Its
joint projector is therefore zero on the saturated generic source
lattice. Multiply this projector by the THREE within-cluster gap
denominators before specializing q. This gives on E000 S

    (A1-c0)(A2-c0)(A3-c0)=0.                            (5)

There is no division by a root-zero gap in (5); it is the root value
of an exact cleared generic identity on the actual lattice. The
complete circle on this cluster is

    L_N(Ai)E000=L_N'(c0)(Ai-c0)E000,
    (4-c0^2)L_N'(c0)=(-1)^d 2N !=0.

Consequently, with ALL first normal data retained,

    L_N(A1)L_N(A2)L_N(A3)E000 S=0.                      (6)

This argument does not assume that a rank-eight generic cube would
specialize to a regular three-variable dual-number module.

## 3. An original planar source whose marked value survives

Take the actual nested planar cups joining physical ends
(1,6),(2,3),(4,5). The original cup is

    p_(a,b)=N x^(-b) delta_(a+b,d).

Let v_triangle be their tensor insertion in the physical order. It
has the regular generic cup lift, so belongs to S. Its exact W
coordinate w_triangle=ext(v_triangle) is

    w_triangle_(0,b,d-b,d)=N^2 x^(-(d-b)), 0<=b<=d,
    all other coefficients zero.                        (7)

The original whole marked co-source on W is

    lambda=ell12 tensor ell34,
    ell_(a,b)=x^a/N delta_(a+b,d).                       (8)

This is the result of the full six-head invariant identity, not a
local replacement of an unrestricted marked row. The only surviving
term in lambda w_triangle is b=d, and hence

    lambda w_triangle=1.                               (9)

On the whole invariant source lambda is a left c0 eigenvector of
ALL three Ai. For A1,A2 this is the original ordinary-cap
intertwining equation. After those two caps the remaining pair is
an actual invariant cup, with Casimir c0; applying the full marked
row afterward proves the A3 assertion too. Thus

    lambda E000=lambda on S.

Set u=Phi E000 w_triangle. It is an explicit nonzero original
saturated-source vector, with regular cluster coupons and no unknown
knot invariant in its definition. Equations (6),(9) prove

    G_C(u,u)=0,     original_marked_row(u)=1.             (10)

Therefore there is NO finite constant B_N, even one allowed to grow
exponentially, such that the original marked functional satisfies

    |original_marked_row(v)|^2 <= B_N G_C(v,v)

for all v in S. This is an actual source Riesz obstruction, not a
generic indefinite-metric example or an absolute-value estimate.
It does not assert a counterexample to a closed link's volume limit:
u uses known Casimir cluster coupons, and the failed statement is
the proposed all-exterior marked positive sewing theorem.

## 4. The genuine marked metric evades the obstruction

The correctly typed original three-pair form is

    G_m(v,v)=v^dagger(C12 tensor C34 tensor H56)v.         (11)

The [original cap/source inequality](actual_complete_circle_positive_quotient.md#5-the-complete-original-boundary-has-a-positive-cauchy-form)
gives, after the WHOLE degree restriction of the marked pair,

    |original_marked_row(v)|^2 <= G_m(v,v)/(8N^11)
                     for every six-head invariant v.    (12)

In particular the same explicit source vector (10) satisfies

    G_m(u,u)>=8N^11, while G_C(u,u)=0.                   (13)

The distinction is the physical last-pair reversal, not a harmless
choice of positive inner-product coordinates. Writing H=P C P moves
that P onto the source vector; a single-pair flip does NOT preserve
the original ordered six-head Hopf invariant space. Thus the joint
simplex support of the three unreflected pair-Casimir product cannot
simply be transferred to (11) by keeping S unchanged.

Exact full-source diagnostics give ranks of the two forms on S:

| N | dim S | rank G_C | rank G_m |
| --- | --- | --- | --- |
| 2 | 5 | 0 | 1 |
| 3 | 15 | 4 | 6 |
| 4 | 34 | 1 | 6 |
| 5 | 65 | 10 | 19 |

These finite ranks illustrate the already proved all-N distinction
(10)--(13); no rank trend is used as proof of a limiting theorem.

## 5. What remains possible at a genuine trivalent junction

For the three-C observation, joint positivity gives a sum of positive
channel weights, but its original source dual already fails (10).
The joint branch geometry also removes a full tensor-cube DCT:
missing admissible joint nodes cannot reconstruct arbitrary products
of three independent half-bandwidth polynomials. A correct simplex
interpolation/angle weight would describe that observed quotient,
not restore the missing marked functional.

One may instead keep (11), change the entire reflected source by the
actual duality/permutation braid, or point an auxiliary belt using
its FULL open-loop normal source. Each is a concrete different
physical problem. The present result neither deletes that current
nor identifies a physical leg flip with an added crossing. A
geometric trivalent-source survival theorem would need such a
source-compatible kernel before its angle or DCT estimate.

There is an explicit correctly marked all-input kernel, useful for
stating that next problem without an unknown recoupling frame. Use
the orthonormal single-pair quotient rows of the
[positive circle quotient](actual_complete_circle_positive_quotient.md),

    pi_(j,r) = w_(j,r)^dagger C / sqrt(g_j beta(2j,r)),
    w_(j,r)=F_pair^r E_j(Omega)|0,d-j>/F_r,
    0<=j<=floor(d/2), 0<=r<=2j.

Here E_j is the stated value Lagrange polynomial; use of values is
valid only AFTER its actual complete-circle map, and its g_j,
factorials and angle normalizations are exactly those proved there.
Define on every W input by the FULL original Phi

    K_(j1,r1;j2,r2;j3,r3)(w)
      =(pi_(j1,r1) tensor pi_(j2,r2) tensor pi_(j3,r3) P56)Phi_w.
                                                               (14)

Then G_m(Phi_w,Phi_w) is EXACTLY the sum of |K|^2 over all these
indices. Integer degree imposes r1+r2+r3=j1+j2+j3, including every
endpoint. The original scalar, not an auxiliary unknown invariant,
is precisely

    lambda w = K_(0,0;0,0;0,0)(w)/(sqrt(8) N^(11/2)).     (15)

This explains the polynomial dual constant in (12). It also locates
the missing moment-map constraint. With Pi=pi tensor pi tensor pi,
the vector K=Pi P56 v for v in S satisfies

    E_Q,total K=Pi [Ecal_6,P56]v,
    F_Q,total K=Pi [F_6,P56]v,                            (16)

not the zero-current trivalent invariant equations. The actual
ordered coproducts give the LOCAL currents

    [Ecal_6,P56]
      =[E5(K6-1)-E6(K5-1)]P56,
    [F_6,P56]
      =K1234^-1 [F5(1-K6^-1)-F6(1-K5^-1)]P56.           (17)

These follow by exchanging physical legs5,6 in the displayed
coproduct, and are exact finite operators. Thus the marked kernel
already has genuine normal/momentum data beyond three independent
node values. Setting (17) to zero would change the original source.
Bounding the coherent kernel (14), or constructing a differently
pointed reflected closure with its full source, remains the next
analytic step; the tensor-cube sampling proof does not supply it.

Audit: [literal six-head source, full Hermite projector and marked/unmarked forms](../experiments/audit_actual_three_belt_saturated_source_and_marked_metric.py).

The source-compatible multivariate positive correction is now [the marked middle-degree Chebyshev packet](actual_marked_multiport_chebyshev_source_packet.md), with an explicit original corner and tensor Parseval. Its geometric energy estimate remains separate.