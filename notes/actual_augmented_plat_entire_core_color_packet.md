# An exact entire Fourier color packet for every augmented plat core

30 October 2026. The original high-color core of ANY fixed augmented
plat has an explicit finite, separately-even ENTIRE interpolation in
its auxiliary deficit colors. Its frequencies are the centered actual
complete-circle channels. It is regular at the odd simple endpoint
and has exact tensor Fourier reconstruction and Parseval identities.

This supplies the finite function itself, not its required exponential
asymptotic. The full original source also contains explicit alias
subsets. Their coherent gap, the core's selected complex saddle and
its geometric period remain unproved for an arbitrary plat.

## 1. The full-algebra split, including normals

Use the original circle polynomials L_n=(-1)^(n-1)U_(n-1)(Omega/2),
L_0=0, and P_N(Omega)=2T_N(Omega/2)+2=0. Here T is the standard
first Chebyshev polynomial, T_0=1 and T_1(z/2)=z/2.
For each integer 0<=h<N, the already proved exact identity is

    L_(N-h)=(-1)^h T_h(Omega/2)L_N+(-1)^N L_h.             (1)

It follows from U_(N-h-1)=T_h U_(N-1)-T_N U_(h-1) and the
FULL polynomial quotient T_N=-1. Thus (1) keeps the Casimir first
normals and the odd simple endpoint. It is not a nodal-value identity
inserted before the complete circle acts.

Let L_(N,j) denote the actual component of L_N at its distinct
node c_j=2cos((2j+1)pi/N), j=0,...,M=floor((N-1)/2), in every
physical degree. These are the rank-one physical matrices of the
[complete compiler](actual_augmented_plat_phase_compiler.md), with
their exact normal-derived coefficients. Multiplication by T_h acts
on each such IMAGE by its value at c_j: the derivative term times
the complete-circle square-zero normal vanishes. Consequently

    (-1)^h T_h(Omega/2)L_N
          =sum_j cos(pi h m_j/N) L_(N,j),
    m_j=N-2j-1.                                          (2)

The centering is exact because h is an integer. All m_j are
nonnegative, have parity N-1, and are distinct. The odd self-node
has m_M=0, so its coefficient in (2) equals one.

## 2. The actual whole-core function

Fix the original augmented 2k-plat skeleton, with b retained auxiliary
regions and fixed signed coupons R_i^(epsilon_i)L_(N-h_i). Let
A_N(j_1,...,j_b) be its literal marked contraction after replacing
each coupon by R_i^(epsilon_i)L_(N,j_i). This includes its ORIGINAL
cups, ordinary caps, unrestricted marked cap, pivots and external
scalar. The exact source-degree argument is the one in the compiler.
No favorable boundary vector or unknown source normalization enters
the definition of A_N.

Define, for complex chi in C^b,

    C_N(chi)=sum_(0<=j_i<=M) A_N(j)
                                    product_i cos(pi m_(j_i) chi_i).
                                                               (3)

This is a finite separately-even entire function. On every physical
high-color tuple h_i=N-n_i with 0<=h_i<=M, its value at chi=h/N
is EXACTLY the original all-core source obtained from (1). In
particular C_N(0) is the full original complete-color scalar: every
alias L_0 vanishes there. Both parity classes are included literally.

The full physical high-color source has the exact expansion

    Z_N(h)=C_N(h/N)
          +sum_(nonempty alias subsets S)(-1)^(N|S|) Z_(N,S)(h),
                                                               (4)

where the coupons in S are R_i^(epsilon_i)L_(h_i), and all others
are the complete-image cosine factors of (2). Each term in (4) is
explicit by the [all-color Hermite compiler](actual_mixed_augmented_plat_compiler.md).
Equation (4) is an identity, not an assertion that those alias terms
are smaller. No alias is deleted by a change of norm.

For low ordinary colors n<=floor(N/2), use the usual physical split
with core ZERO and the full ordinary coupon as alias. The mathematical
function (3) still has values at the other grid points; these are
its Fourier extension, not a new definition of physical low-color core.

## 3. Exact two-parity Fourier reconstruction

Put w_j=1/2 when m_j>0 and w_j=1 when m_j=0. Direct finite geometric
summation gives

    (1/N) sum_(h=0)^(N-1)
      cos(pi h m_j/N) cos(pi h m_l/N)=w_j delta_jl.         (5)

To check it, expand the product into exponentials. The differences
m_j-m_l are even integers with absolute value below 2N. The sum
m_j+m_l is also even; its only zero or 2N multiple is zero at
the odd self-node j=l=M. This gives exactly the weights above.
No prime-level assumption is made.

By tensoring (5), the original channel coefficients can be recovered
from this finite function:

    A_N(j)=1/[N^b product_i w_(j_i)]
       sum_(h_i=0)^(N-1) C_N(h/N)
                           product_i cos(pi h_i m_(j_i)/N). (6)

Its exact positive Parseval identity is

    (1/N^b) sum_h |C_N(h/N)|^2
                            =sum_j product_i w_(j_i)|A_N(j)|^2.
                                                               (7)

The transform therefore has only a fixed polynomial cost in N at
fixed b. All exponential behavior is still in the ACTUAL coherent
coefficients A_N; (7) does not manufacture positivity of their sum
C_N(0), nor a nonzero geometric coefficient.

The same function satisfies exactly

    C_N(chi+e_i)=(-1)^(N-1)C_N(chi),
    C_N(-chi_i,chi_others)=C_N(chi_i,chi_others).            (8)

It is periodic at odd levels and antiperiodic at even levels.
In particular values near h=N mirror those near h=0. Thus this
symmetry carries every proved near-zero value to the opposite end.
IF a fixed-neighborhood analytic corridor asymptotic with complete
rate F0 and nonzero amplitude GERM is established, choose arbitrarily
small fixed positive real colors where that amplitude is nonzero.
Their nearby grid values have rates arbitrarily close to F0 and
reflect outside the corridor. This precludes a fixed whole-cube gap
for the extension. If the amplitude is a UNIT at zero, h=1 already
gives the complete rate and reflects to h=N-1. The unit assumption
is needed for that particular h=1 argument with an absolute remainder.

Periodicity ALONE is not an obstruction. In one variable the exact
reproducing kernel is

    sum_j w_j^-1 cos(pi m_j chi)
      =sum_(r=0)^(N-1) exp[pi i(N-1-2r)chi]
      =sin(N pi chi)/sin(pi chi).                         (8a)

Its values at chi=h/N are N delta_(h,0), for 0<=h<N, at BOTH
parities. Multiplying it by exp(N F0)/N exhibits a complete rate F0
and zero at every other physical sample. It has no fixed-scale
analytic corridor of the required form. The distinction after (4)
is essential when combining a corridor theorem with a physical
color-complement bound.

An elementary entire growth bound is

    |C_N(chi)|<=exp(pi(N-1) sum_i |Im chi_i|) sum_j |A_N(j)|.
                                                               (9)

It is an exact upper bound, much weaker than the quadratic complex
corridor estimate required for long-filling stationary phase.

## 4. The remaining analytic issue is now concrete

Unlike a direct nonintegral-color substitution into
sin(n theta)/sin theta at theta=pi, (3) is regular at the odd
self-node and specifies every finite-N continuation exactly.
Its extension is the unique one in the stated finite cosine span;
no generic-q germ of the whole pointed invariant is replaced.

A general filling theorem would still require a uniform asymptotic
of (3) on a FIXED complex neighborhood, a source-preserving selected
saddle/period, the entire physical alias and color-complement bounds,
and the actual marked hyperbolic regulator. The exact complete and
mixed compilers expose those quantities at arbitrary fixed bridge
width, but do not prove their exponential estimates. The relevant
large twisting threshold T(D) concerns a fixed diagram D; the
Fourier frequency scale N here remains the quantum level.

Audit: [full-algebra split and exact tensor Fourier identities](../experiments/audit_actual_augmented_plat_entire_core_color_packet.py).

Independent analytical review and fresh audit replay: PASS. The
review checked the physical high-color range, full-algebra normal
identity, two-parity frequency norms, reconstruction and Parseval.
It corrected the periodicity inference: the obstruction needs the
stated analytic corridor, and the exact reproducing-kernel example
now has its own finite audit. The primary-agent read and fresh replay
also passed all 162 signed split identities, 204 centered characters,
and 27 tensor Fourier packets.
