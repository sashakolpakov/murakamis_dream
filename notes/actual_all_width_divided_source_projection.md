# One explicit divided-current kernel for every original plat source

29 October 2026. The source-specific six-port kernel extends to EVERY
fixed plat width. This supplies a concrete, proper original-source
restriction before a coherent metric is chosen. It does not infer a
sharp energy estimate from a small coefficient in an algebraic projector.

## 1. The actual regular divided currents

Use the generic balanced original V_d, d=N-1, and the original
coproducts from
[the six-port normal-current proof](actual_six_port_divided_power_source_kernel.md).
For an ordered block of 2r physical heads let H be its unrolled total
weight. The regular first-normal operators are

    J_E=[Ecal_(2r)^N/(1-zeta^(2N))]_(zeta=q),
    J_F=[F_(2r)^N/(1-zeta^(2N))]_(zeta=q).                (1)

These are defined by generic division before specialization. Their
ordered divided-coproduct formula is finite, with every nonzero local
factorial index<N. They change H by +2N and -2N, respectively.
Their normalization and all Cartan signs are those of the literal
original matrices, not an abstract replacement representation.

Consider the full physical K_total=1 sector

    Lcal=direct_sum_(k in Z) (V_N^tensor(2r))_(H=2Nk).     (2)

The source degree space is just its H=0 summand. Sector(2) is NOT
being identified with the much smaller Hopf invariant space.

## 2. An ordinary sl2 action is an exact consequence of the normal Ward

The generic divided commutation identity gives, at a vector of weight H,

    E^[N] F^[N]=sum_(t=0)^N [H choose t]_zeta
                                      F^[N-t]E^[N-t].

For H=2Nk, EVERY integer k, the root coefficients are

    [2Nk choose t]_q=0 (0<t<N),
    [2Nk choose N]_q=2k(-1)^N.                           (3)

Here is a proof including negative k. In the finite product for the
last Gaussian, the numerator contains [2Nk]; every other nonzero
numerator factor specializes to [-j]=-[j], 1<=j<N. The zero ratio
[2Nk]/[N] has derivative ratio -2k at q. Thus its value is
(-1)^(N-1)(-2k)=2k(-1)^N. For t<N the numerator zero has no denominator
zero. At k=0 the finite product is identically zero, consistent with(3).
No semisimple or tilting theorem is used.

The exact scalar connecting (1) with divided powers is

    alpha_N=N q^[-N(N-1)/2]/(1-Q)^N,
    alpha_N^2 rho^(2N)=N^2(-1)^(N-1), rho=q-q^-1.

Consequently on(2)

    [J_E,J_F]=-N H.                                     (4)

Put

    e=J_E/N, f=-J_F/N, h=H/N.

Equations(1),(4) give EXACTLY

    [e,f]=h, [h,e]=2e, [h,f]=-2f.                        (5)

This is a finite-dimensional ordinary sl2 action on a KNOWN physical
sector, derived from the first normal of the actual quantum operators.
It is not a statement that the physical braids are positive-unitary,
and no Hermitian condition on e,f is assumed.

## 3. A finite explicit right inverse, with no complete-reducibility premise

On the h=2 subspace define

    R=sum_(j>=0) (-1)^j f^(j+1)e^j/[(j+1)!(j+2)!].        (6)

The sum is finite. Since |H|<=2r(N-1)<2rN, terms j>r-2 vanish.
For r<2 this h=2 space is zero. On a vector v of weight2, (5) gives

    e f^(j+1)e^j v
      =f^(j+1)e^(j+1)v+(j+1)(j+2)f^j e^jv.

Successive terms in eR cancel, and the first coefficient is
2/(1!2!)=1. Therefore

    e R=I on the ENTIRE weight2 space.                  (7)

Thus J_E maps its weight0 space onto its weight2 space at every N
and width. This argument proves the needed surjectivity directly;
it does not import complete reducibility of a classical module.

## 4. The source is exactly that kernel at arbitrary width

For an original 2k-head plat put r=k-1 and C=r d. The complete root
invariant theorem identifies all invariants with

    W_r=(V_N^tensor(2r))_(degree C).

Its literal coefficient extraction and original turns are those of
[the complete source module](actual_complete_source_multiplicity_module.md),
section5. The target of J_E is the physical degree C-N space, call it L_r.
If C-N<0 interpret it as zero.

Let S_N^(2k) be the saturated specialization of GENERIC invariant
tensors inside V_d(zeta)^tensor(2k), as in
[the deformable-source construction](actual_six_port_deformable_source_and_recoupling.md).
Every generic invariant is killed by the regular divided current.
Extraction of its last two colors(0,d) gives

    ext(S_N^(2k)) subset ker(J_E:W_r->L_r).               (8)

The extraction proof is unchanged at arbitrary prefix width: fifth
in the six-port argument is now head 2k-1. If that head has input c>0,
its c ordinary lowerings leave E_prefix^(N-c) E_prefix^c=0 at the root;
c=0 retains the full divided prefix operator. Last head color d forces
zero lowering there. Thus no endpoint or derivative source is removed.

It remains to compare exact dimensions. Write

    S(z)=1+z+...+z^d,
    a_j=[z^j] S(z)^(2r), a_j=0 outside its actual support.

The full root space has dimension a_C and L_r has dimension a_(C-N).
Over generic q, the invariant dimension in 2k heads is the weight-zero
dimension minus the weight-two dimension:

    rank S_N^(2k)=[z^(kd)](1-z) S(z)^(2k).

This follows either from the elementary generic highest-vector tensor
decomposition, or by observing that each nontrivial even highest weight
has one weight0 and one weight2 while the trivial module has only weight0.
Using

    (1-z)S(z)^2=(1-z^N)S(z)

and coefficient symmetry a_(C+j)=a_(C-j), its value telescopes to

    rank S_N^(2k)=a_C-a_(C-N).                           (9)

Surjectivity(7) says the kernel on the right of(8) has exactly the SAME
dimension. Saturation makes the specialization injective, so (8) is
an equality:

    BOXED: ext(S_N^(2k))=ker(J_E:W_r->L_r).               (10)

In the full 2k-head root invariant space this is equivalently the
kernel of its total J_E; adjoining total J_F changes nothing because
all generic invariant lifts are killed by both. This is a VALUE source
theorem: derivatives of the whole source still obey their differentiated
inhomogeneous Ward equations, not a falsely homogeneous version of(10).

## 5. A completely explicit all-width source projector

On W_r=weight0, (6)--(7) give the algebraic projection I-Re. In the
original normal-current normalization its finite formula is

    P_source=I+sum_(m=1)^(r-1)
                    J_F^m J_E^m/[N^(2m) m!(m+1)!].       (11)

For r<=1 the sum is empty. Its range is exactly(10), and it is the
identity there; P_source^2=P_source follows from eR=I. For six heads
r=2 this reduces to I+J_F J_E/(2N^2), with the previously proved right
inverse J_E J_F=-2N^2 I on L_r.

All original regular generic braids, interval Casimirs and polynomial
circle coupons preserve the source subspace. Therefore (11) may be
inserted between their reduced gates on an original source orbit without
changing any literal exterior co-source. It need not commute on the
larger unrestricted root module, and a root-only Hopf coupon with no
regular generic lift is not covered by this assertion.

The operator(11) is generally oblique. Its polynomial coefficients in
N do NOT make its norm polynomial: J_E and J_F themselves may have
exponentially large entries in a specified frame. If a positive metric
is needed, the orthogonal projector onto the SAME explicit kernel has
norm one. In the physical W_r coordinates, the exact original boundary
data satisfy

    ||w0||=N^[3(k-1)/2], ||lambda||=N^[-(k-1)/2],
    ||w0|| ||lambda||=N^(k-1).

Orthogonal compression does not increase that boundary cost and retains
the literal marked cap only after its proved whole-invariant reduction.
This does not yet estimate the coherent word energy on(10).

## 6. Consequence for the first genuinely non-tree source block

At six heads, the full root module has dimension(2N^3+N)/3, whereas
the actual deformable source has dimension(N^3+N)/2. A generic 6j
construction belongs on this latter saturated module. It must keep its
complete confluence/normal coefficients, and must NOT be equated to
the larger raw-root invariant space or to three free scalar circle
registers. Formula(10) supplies its missing normal source equation
explicitly; formula(11) provides an actual algebraic insertion enforcing
that equation before positivity.

The sharp analytic task remains the coherent Clebsch/Racah contraction
on this constrained source, including its complex corridor and global
complement. Neither dimension compression nor the ordinary sl2 relation
is a sharp hyperbolic-volume estimate. No additional knot/link equality
is claimed here merely from this source theorem.
