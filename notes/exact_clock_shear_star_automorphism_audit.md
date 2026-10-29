# Audit of the exact quantum clock shear and its actual root source

Independent proof audit, 27 October 2026. The finite diagonal operator
below exactly quantizes the smooth symmetric-frame sphere shear. At
the marked root it is the entire previously proved balanced-to-symmetric
coordinate change. Its off-root quantum-factorial residual and first
normal jets remain essential.

Use [the actual global q-difference source](integral_color_global_q_difference_source.md)
and [the factorial-frame theorem](quantum_factorial_frames_and_cyclotomic_source.md).
No geometric R-intertwiner or global selected-volume claim is inferred.

## 1. Exact finite star automorphism

Let n=N-1, J x^j=jx^j, and put

    q=exp(s/(2N)), m=q^N, M=-m,
    U_j=q^[Nj-j(j+1)/2], U_0=1.                          (1)

The coherent-symbol map sigma is injective: after multiplying
by its incidence denominator, distinct matrix units have distinct
monomials v^i z^j. Its exact star product is sigma(A)*sigma(B)=sigma(AB).
Thus

    sigma(A) -> sigma(U A U^(-1))                        (2)

is a global automorphism of that finite star algebra for every N.
For imaginary s it is unitary in the Euclidean metric and in the
diagonal coherent metric. It preserves the exact normalized trace.

Let a_hat=J_-/n, b_hat=J_+/n and T_hat=J/n, where
J_-x^j=jx^(j-1), J_+x^j=(n-j)x^(j+1). The adjacent ratio is

    U_j/U_(j-1)=m q^(-j).

Hence the two transformed entries are j m^(-1)q^j/n and
(n-j)m q^(-j-1)/n. Exact binomial summation gives

    sigma(U a_hat U^(-1))
      =m^(-1)q a[1+(q-1)T]^(n-1),
    sigma(U b_hat U^(-1))
      =m q^(-1)b[1+(q^(-1)-1)T]^(n-1),
    sigma(U T_hat U^(-1))=T,                            (3)

with a=z/(1+vz), b=v/(1+vz), T=vz/(1+vz).

Their uniform fixed-derivative limits are a/r,r b,T, where
r=exp[s(1-T)/2]. In the affine source coordinates (v,a) this
is exactly Psi_s(v,a)=(rv,a/r). The elementary uniform logarithm
estimate used for the global generator symbols proves the O(1/N)
error. For imaginary s the map sends the same real compact sphere
to itself, with its orientation and clock preserved.

The quantum clock assertion is exact, not just principal:
U commutes with J, q^J, Q^J, K, every polynomial index moment,
and every diagonal endpoint projector. In particular both literal
wall probes E_00,E_nn survive unchanged. The rank-one cut coupon
is not fixed; it is conjugated by (2).

## 2. The whole actual frame comparison and the original source

The actual regular basis-vector frame is

    h_j=D_j w_j,
    D_j=(-1)^j q^[j(j+1)/2]/{n choose j}_q.

Its coordinate change is D^(-1). Direct multiplication gives

    D_j U_j=M^j/{n choose j}_q,
    D^(-1)=U V,
    V_j={n choose j}_q/M^j.                             (4)

At q=q_N, M=1 and {N-1 choose j}_(q_N)=1. Consequently

    U_(q_N)=D_(q_N)^(-1)                                (5)

exactly for every parity and every entry. Thus (2) at that root
is the literal actual balanced-to-symmetric frame conjugation,
with all tensor crossing operators transported by the same U.
This is stronger than a principal-symbol comparison, but is a
change of actual source frame rather than a geometric holonomy
intertwiner.

The balanced source transforms exactly as

    psi_h=U ones, phi_h=ones^t U^(-1)/N,
    Gamma_h=U Gamma U^(-1).                             (6)

The cup and its dual basis are transported inversely. Both actual
diagonal pivots commute with U, and their original twists and
normalization lines are retained. Thus the whole root pointed
network is the original one in the symmetric frame. Off the root,
the full coordinate change is U V and cannot be replaced by U
if the target is that specified symmetric frame.

The top value is also exact:

    U_n=q^[N(N-1)/2],
    U_n(q_N)=i^(N-1)=i^(N+3)=epsilon_N.                 (7)

The exponent N(N-1)/2 is an integer, so no hidden square-root
choice occurs in (7). This is the original phase already present
in the quantum-factorial frame, identified as one extreme source
weight. It does not determine the full modified-dimension line or
authorize deleting any other scalar factor of the network.

## 3. Its residual has nonzero root-normal jets

Although V_j(q_N)=1, its first q-logarithmic derivative is

    [q partial_q Log V_j]_(q_N)
       =-Nj+iN sum_(r=1)^j cot(pi*r/N).                  (8)

For a proof, write the q-binomial as
product_(r=1)^j [N-r]_q/[r]_q. The logarithmic derivative
of [k]_q is k coth(k Logq)-coth(Logq). At Logq=pi*i/N,
coth((N-r)Logq)=-coth(r Logq), so each binomial factor
contributes -N coth(r Logq)=iN cot(pi*r/N). The M^j
denominator contributes -Nj, proving (8).

These jets need not be small as N grows. For example V_n=M^(-n),
so its derivative is exactly -Nn even though its root value is one.
Thus U is the complete root frame, not a replacement for the whole
off-root source comparison or its normal connection.

The [exact audit](../experiments/audit_exact_clock_shear_star_automorphism.py)
checks the symbols, star multiplication/source covariance, full
clock and endpoint projectors, actual root frame and phase, and
the residual derivatives.
