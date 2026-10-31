# Both original crossing signs have the same flat Green transport

28 October 2026. At complete color, the original negative crossing
is the flip-conjugate of the positive crossing in the SAME balanced
flat metric. The apparent diagonal comparison in an unbalanced frame
cancels to a phase depending only on total integer degree. This
transports the proved clock/ground Green system to negative crossings
without an ill-conditioned factorial change of metric.

All original Cartan, twist, pivotal and cap normalizations are retained.
This is a local operator theorem; it gives no lower bound for the
final scalar source pairing.

## 1. Exact antiunitary including the common Cartan phase

Put q=exp(pi*i/N), Q=q^2, x=q^(N-1)=-q^(-1), rho=q-q^(-1),
and eta=exp(pi*i/(2N)). Write the original crossings as

    R_+=kappa K_0^+, R_-=kappa^(-1)K_0^-,
    kappa=eta^((N-1)^2), |kappa|=1.

Let P swap the two heads and let C be coefficientwise conjugation
in the original balanced basis. Then EXACTLY

    R_-=P overline(R_+)P,
    K_0^-=P overline(K_0^+)P.                         (1)

Thus J=P C is an antiunitary involution and R_-=J R_+ J^(-1).
It is not an assertion that R_+ itself is unitary.

Here is a direct proof fixing the frame and phase. In the real
unbalanced basis, F is the real unit shift and E_j=[j]_q^2 is real
at this complete color. The common-scalar-removed checked crossing is

    B=P D Theta,
    D_(a,b)=x^(-a-b)q^(2ab).

D is unitary diagonal. The finite nilpotent Euler factor Theta has
coefficients q^(k(k-1)/2)rho^k/[k]_q!. Conjugating them gives the
ordinary inverse Euler coefficients; the finite q-binomial convolution
proves overline(Theta)=Theta^(-1). Hence

    overline(B)=D^(-1)P B^(-1)P D.                   (2)

The actual balanced gauge is g_j=(Q;Q)_j, up to a REAL nonzero
diagonal. Since

    (Q;Q)_j=(-rho)^j q^(j(j+1)/2)[j]_q!,
    g_j/overline(g_j)=(-1)^j q^(j(j+1)),

the residual pair phase after transporting (2) to the balanced frame
is

    (g_a g_b)/(overline(g_a g_b)) D_(a,b)
                                        =q^((a+b)(a+b+2)). (3)

This depends only on total INTEGER head degree a+b. The actual
crossings and P preserve that degree, so this phase commutes with
them and cancels from the conjugation relation. This proves (1).
The full scalar obeys overline(kappa)=kappa^(-1), so there is no
unrecorded sign or framing multiplier. No factorial modulus remains
in the comparison and no unbalanced norm is used in the result.

## 2. Negative clock and ground families

Take the proved original positive clock and ground operators
K_m^+,H_m^+ from Section 8 of
[the original source theorem](actual_rogers_sink_opposite_beta_source.md).
Their clock is Q^(m J_second) immediately after C^(-1), and all
indices are physical 0,...,N-1. Define the negative auxiliary families
by the exact antiunitary transport

    K_m^-=P overline(K_m^+)P,
    H_m^-=P overline(H_m^+)P.                         (4)

At m=0 this is the literal original negative crossing with its
common scalar removed. These definitions transport a specified
original clock insertion; they do not replace the negative crossing
by its transpose or assume a new local metric. Both families are
N-periodic in m.

For an array X_(c,d;a,b) let the positive Green shift be

    (A_+ X)_(c,d;a,b)=x^(-1)X_(c,d-1;a-1,b)

when a,d>=1, with zero outside the physical range. Its antiunitary
transport is

    (A_- X)_(c,d;a,b)=x X_(c-1,d;a,b-1),              (5)

when b,c>=1, zero otherwise. In scalar kernel coordinates this is
the monomial x z_first-output/z_second-input. The exact signed
source Ward equations are

    K_m^+-A_+ K_(m+1)^+=H_m^+,
    K_m^--A_- K_(m+1)^-=H_m^-.                       (6)

The second is the antiunitary image of the first, with all original
support conditions transported, so no negative-current endpoint is
discarded independently.

For input (a,b), the negative ground output is (0,a+b), provided
a+b<N, with coefficient

    Q^(-m a)x^a {a+b choose b}_(Q^(-1))
                             (Q^(-m)x^2;Q^(-1))_b.   (7)

It is zero if a+b>=N. This is the conjugate of the EXACT positive
ground coefficient with its two input indices exchanged. In
particular both ground channels have rank N and the same singular
values. Their exponential bulk factorial weight has not disappeared.

## 3. Flat Green conditioning is identical for both signs

Use the clock-family Hilbert space

    H_clock=direct_sum_(m mod N) HS(V_N tensor V_N),
    ||X||^2=sum_m ||X_m||_HS^2,
    (T_+ X)_m=A_+X_(m+1),
    (T_- X)_m=A_-X_(m+1).

All head basis vectors have norm one. The clock advance is a
permutation, and (5) is a partial permutation with a unit scalar,
so

    ||T_+||<=1, ||T_-||<=1, T_+^N=T_-^N=0.             (8)

The nilpotence follows from the strictly increasing first input
demand for the positive sign and second input demand for the negative
sign. It concerns source transport, not the full braid image group.
The exact inverses are finite:

    G_+=(1-T_+)^(-1)=sum_(j=0)^(N-1)T_+^j,
    G_-=(1-T_-)^(-1)=sum_(j=0)^(N-1)T_-^j,
    ||G_+||,||G_-||<=N,
    ||G_+^(-1)||,||G_-^(-1)||<=2.                    (9)

Thus the local transformations have condition number at most 2N in
the SAME metric for either sign. They reconstruct the original signed
crossings from (6), with scalar kappa or kappa^(-1) respectively.

For clarity, the family shifts are partial permutations with finite
chains of length at most N; some chains have length exactly N. After
unit phase gauges on each chain, 1-T is the elementary bidiagonal
matrix. Its squared singular values on a chain of length L are
4 sin^2[(2j-1)pi/(4L+2)], j=1,...,L. Consequently the exact full
family norms are

    ||G_+||=||G_-||=1/[2 sin(pi/(4N+2))],
    ||G_+^(-1)||=||G_-^(-1)||=2 cos(pi/(2N+1)).        (10)

The coarser bounds (9) already suffice for polynomial-cost tensor
transport at fixed word length. These estimates do NOT lower-bound
the final scalar period: the pulled-back original source can still
be nearly orthogonal to the tensor of ground channels.

## 4. Original source and scope

Equation (1) is used locally to represent the negative matrix at its
actual four ports. It is NOT applied as a global conjugation of the
word or to change the knot into its mirror. All original cups, caps,
pivots, common Cartan and zero-framing lines stay in their prescribed
places. In particular no metric change or scalar normalization is
hidden in passing from positive to negative Green transport.

The [exact root audit](../experiments/audit_signed_green_antiunitary_transport.py)
checks the full original negative crossing, all negative clock Ward
and ground coefficients, nilpotent reconstruction and original
whole signed pivotal sources. Small bidiagonal singular-value checks
verify (10) independently of the phase calculation; the proof of
the all-N bounds is the explicit partial-permutation structure.
