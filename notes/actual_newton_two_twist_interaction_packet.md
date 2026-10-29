# A coherent two-twist/turn source packet with a sharp norm rate

29 October 2026. Set A=T_2 P_rev T_2 in the COMPLETE original Newton
metric. The whole source vector A1 has an exact second-order Ward
recurrence, an exact reflected boundary equation with an inhomogeneous
current, and a sharp all-level norm exponent. The proof uses both actual
source endpoints and never assumes that distinct spectral roots alone
prevent conversion. It does not identify the reflected circuit with a
hyperbolic link or prove the rate for arbitrary longer reduced words.

## 1. Exact original coefficient and Ward equation

Use the original N,d,q,Q,kappa,F_i,s_i of
[the Newton metric](actual_newton_turn_positive_gram.md). Define

    W_i=F_i^2 sum_(j=0)^i
           (-1)^j Q^[(3j^2+j)/2]/(F_j^3 F_(i-j)),
    H_i=F_i W_i,                  0<=i<=d.

The all-entry T_2 formula and F_j F_(d-j)=N nu_j give the exact
SOURCE vector, with no phase or endpoint discarded,

    (A1)_i=kappa^4 N(-q)^(i+d) W_i.                       (1)

Indeed T_2 1 has entries kappa^2(-q)^j F_j. Apply the genuine
reversal and then T_2; its inner j coefficient is nu_j^3 Q^(-j),
exactly (-1)^j Q^[(3j^2+j)/2].

The whole-index recurrence is

    (1-Q^i)W_i=(1+Q-3Q^i)W_(i-1)
                          -Q(1-Q^(i-1))^2 W_(i-2),
    H_i=(1+Q-3Q^i)H_(i-1)
                          -Q(1-Q^(i-1))^3 H_(i-2),       (2)
    H_0=1, H_1=1-2Q.

At i=1 the second coefficient is ZERO; no H_(-1) is needed. These
equations hold for every physical index i<=d and all N>=2.

For an own derivation, put a_j=(-1)^jQ^[(3j^2+j)/2]/F_j^3,
G_i=sum_j a_j/F_(i-j), and use formal generating series modulo z^N.
The shift T:f(z)->f(Qz) gives

    (1-T)^3 a(z)=-Q^2 z T^3 a(z),
    E(Qz)=(1-z)E(z), E(z)=sum z^k/F_k, G=aE.

Consequently

    (1-z)(1-Qz)G(z)-3(1-Qz)G(Qz)
                                      +3G(Q^2z)-G(Q^3z)=0.

Coefficient extraction gives
(1-Q^i)^3G_i=(1+Q-3Q^i)G_(i-1)-QG_(i-2), hence (2).
This argument can first be made at generic Q and then specialized
coefficientwise below degree N. It never divides a zero root factorial.
The physical source identification (1) uses the root complementation
identity. A generic-Q continuation of this displayed scalar recurrence
is not thereby identified with the actual generic-q tangle/source germ.
All estimates here use its exact physical root values.

## 2. The second source endpoint is exactly the known Gaussian

Let P_d be the ORIGINAL normalization endpoint, with its already proved
identities and all-parity Gaussian asymptotic:

    P_d=N^2 sum_(j=0)^d Q^j/F_j^2
       =sum_(j=0)^d F_j
       =N^(3/2) exp[i pi(1/4-N/12+1/(4N))]+O(sqrt N).

See [the endpoint proof](actual_normalization_endpoint_gaussian_asymptotic.md).
In particular cN^(3/2)<=|P_d|<=CN^(3/2) for all large N.
Root factorial complementation in the actual sum gives

    W_d=N sum_j Q^(j^2)/F_j^2
       =(Q/N)sum_j Q^j F_j^2=conjugate(P_d)/N,
    H_d=conjugate(P_d).                                  (3)

The penultimate coefficient is also fixed, not a free backward datum:

    (conjugate(F_1))^3 H_(d-1)
                         =(1-2/Q)H_d+Q^(-1).             (4)

For completeness set C(t)=sum_j F_j^2t^j. Its exact finite Ward is

    (1-t)C(t)+2Qt C(Qt)-Q^2t C(Q^2t)=1.

At t=1 this evaluates C(Q^2) from C(Q); substituting the complemented
finite expression for H_(d-1) gives (4).

Define J_0=0,J_1=1 and evolve J by (2) only for i>=2. Direct reversal
of (2), with g_k=conjugate(F_k)^3 H_(d-k), now proves

    g_k=H_d conjugate(H_k)+Q^(-1)conjugate(J_k), 0<=k<=d.  (5)

The corresponding PHASED source coefficient, useful before any future
color-contour deformation, is exactly

    (A1)_(d-k)=kappa^4 Q^(-1) q^(k^2)/s_k^2
                 [H_d conjugate(H_k)+Q^(-1)conjugate(J_k)]. (5a)

Indeed W_(d-k)=nu_k g_k/(N s_k^2); the actual factor
(-q)^(2d-k)nu_k=Q^(-1)q^(k^2) gives (5a).

The constant term Q^(-1) in (4)--(5) is a retained original boundary
current. It is not set to zero. The independent J solution does not
satisfy the resetting i=1 source equation, which is why that current
cannot be absorbed into a second homogeneous source at the endpoint.

## 3. A regular gapped half-circle and a uniform envelope

Put u=pi i/N and Y=exp(2iu). The classical monic transfer has roots

    mu_±(u)=[2-3Y ± Y sqrt(4Y-3)]/2.                     (6)

Choose the square root continuously from +1 at u=0. On 0<=u<=pi/2,
the minus root mu is nonzero and dominant until the terminal equality
of moduli; write rho(u)=|mu(u)|. The eigenvalue difference has modulus
|sqrt(4Y-3)|>=1, so its eigenframe and first derivatives are uniformly
bounded on this entire closed half-circle.

Here is a direct modulus check. For a=2-3Y, b=(1-Y)^3 and 0<u<=pi/2,

    a^2/b=(9+16sin^2u)/(8sin^2u)
             -i cos(u)(1-16sin^2u)/(8sin^3u).

Two roots of lambda^2-a lambda+b have equal modulus exactly when
a^2/b belongs to [0,4]. The imaginary part vanishes only at
sin u=1/4 or cos u=0. The first gives 20, outside that interval;
the second gives25/8. Thus the only modulus equality is u=pi/2.
At u=0 the roots are -1,0 and the source selects -1.

Let I(u)=pi^(-1)integral_0^u log rho(v)dv. Uniformly for all physical
i with 0<=i<=d/2, the exact transfer matrix differs by O(1/N) from
its classical matrix. In the bounded moving eigenframe, each normalized
step has norm at most rho(u_i)(1+C/N). Hence

    |H_i|+|J_i| <= C exp[N I(pi i/N)].                    (7)

The constants do not deteriorate at the terminal modulus equality:
the eigenVALUES remain separated. The sum-to-integral error is O(1).

On every smaller interval 0<=u<=u_0<pi/2 the source is sharper:

    log|H_i|=N I(pi i/N)+O_(u0)(1),
    |J_i/H_i|<=C_(u0).                                  (8)

To justify the nonzero statement, write h_i=H_i/H_(i-1). The exact
Riccati map is h_i=a_i-b_i/h_(i-1). Its derivative at the dominant
classical root is mu_other/mu, of modulus uniformly less than one.
An O(1/N) disk around the smooth nonzero dominant root is therefore
invariant under every step, by induction. The literal reset
H_1=1-2Q starts inside that disk. Thus every h_i is nonzero and
h_i=mu(u_i)+O(1/N). Summing logarithms proves (8)'s first assertion.
For the second, the difference of successive J_i/H_i has consecutive
ratio b_i/(h_i h_(i-1)), uniformly less than one; its first difference
is1/H_1. This proves the uniform bound. No claim of adiabatic survival
is made across the modulus crossing.

## 4. Sharp whole-source norm from the two actual endpoint solutions

For the first half, (7) and the uniform sine-factorial estimate give

    log|W_i| <= N[I(u)+Lambda(u)/pi]+O(log N).

For the second half put k=d-i, u=pi k/N. Equations (3),(5), and
s_i s_k=N give

    |W_i|=|g_k|/(N s_k^2),
    log|W_i| <= N[I(u)+2Lambda(u)/pi]+O(log N).            (9)

These bounds cover EVERY index, including the middle and endpoints.
Since Lambda(u)>=0 on [0,pi/2], the backward profile dominates the
forward one. Write B(u)=I(u)+2Lambda(u)/pi. For each fixed
u in(0,pi/2), (3),(5),(8) also give the matching lower rate in(9):
the J term is relatively O(N^(-3/2)) and cannot cancel the main term.

There is a unique maximizer u_* of B. Indeed

    B'(u)=pi^(-1)log[rho(u)/(2sin u)^2].

For 2sin u<1, rho>=|b|^(1/2)=(2sin u)^(3/2)>(2sin u)^2.
For u>=pi/6, an equality rho=(2sin u)^2 can occur only when

    z^3-4z^2+3z-1=0, z=4sin^2u.                        (10)

One can verify this without choosing a root phase: impose |mu|^2=z^2
in mu^2-a mu+b=0 and its conjugate. The resulting equality is
z(1-z)^2=1-2z+2z^2, exactly (10); here
|conjugate(b)a-conjugate(a)z^2|^2=z^3(1-2z+2z^2)>0.
The polynomial has a unique root z_* in[1,4], in fact in(3,4).
At pi/6 the ratio rho/(2sin u)^2 is greater than one, whereas at
pi/2 it is1/sqrt2<1. Continuity and uniqueness therefore prove the
claimed strict maximum, with u_*=arcsin(sqrt(z_*)/2).

Using (1), the polynomial number of positive norm terms and a rounded
index near the backward maximizer now prove the ALL-LEVEL estimate

    log||T_2 P_rev T_2 1||_Newt^2 = N L+O(log N),
    L=(2/pi)[integral_0^(u_*)log rho(v)dv+2Lambda(u_*)].   (11)

Numerically L is approximately .9060724478038353. This number is only
a calibration; formula (11) is the proved constant. It comes from the
fully coherent source vector before taking its positive norm.

## 5. Scope and reuse

The actual adjoint-word closure of A^dagger A is the original numerator
source ||A1||^2, with the unrestricted marked cap and kappa retained.
Thus (11) is a new coherent estimate for an ENTIRE specified original
source circuit, not an expanded positive path. Its link topology,
hyperbolicity and regulator identification are separate questions;
no volume equality is asserted from its numerical rate.

This proof offers a checkable recurrence mechanism beyond distinct
eigenvalues: an exact resetting source endpoint, a regular half-domain
modulus gap, an independently evaluated nonzero opposite endpoint,
and a reflection identity retaining the inhomogeneous current. Those
inputs allow the two gapped solutions to be estimated separately.
There is no unsupported propagation through a general modulus crossing.
The [modular reduction](actual_newton_coherent_turn_reduction.md)
removes arbitrarily many redundant turns; genuinely longer reduced
mixed words still require their own coherent packet/current estimate.

Audit: [literal original matrices, exact sums/recurrences/endpoints and norm calibration](../experiments/audit_actual_newton_two_twist_interaction_packet.py).

Independent analytical review and fresh replay passed: the reflection
indices/current, endpoint normalization, separated-frame bound through
the midpoint, strictly gapped Riccati lower bound, and cubic maximum
were each rederived. The finite profiles supplement that proof; they
are not its justification.
