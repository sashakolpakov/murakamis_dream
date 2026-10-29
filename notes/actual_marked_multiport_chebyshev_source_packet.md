# An explicit marked multiport Chebyshev packet

29 October 2026. The correctly marked original plat source has an
explicit coherent multivariate polynomial packet. After its actual
complete-circle quotient, every variable has half bandwidth and exact
tensor Chebyshev/Parseval reconstruction with polynomial dual cost.
This works at arbitrary FIXED bridge width, both level parities and
all composite levels. The physical source-to-packet transform may
carry exponential factorial energy; no sharp volume estimate for that
energy is asserted.

The construction uses C on ordinary pairs and H on the marked pair.
It therefore avoids the proved all-C six-port source obstruction.
It is a final-source identity/inequality, not a claim that arbitrary
split-pair crossings descend to the quotient or that node values may
replace the original generic-q normal germ.

## 1. Original source and the exact middle-degree extraction

Put N>=2,d=N-1,q=exp(pi i/N),Q=q^2,x=q^d, M=floor(d/2).
For a 2k-head plat, let v=W p^tensor k be the COMPLETE original
output state after any fixed signed braid word, with its full Cartan
and source factors. Retain the external normalization chi_N explicitly.
The following identities more generally hold for any input v of
TOTAL integer degree kd, so apply with every allowed degree-preserving
exterior. Write the original ordinary and full marked rows as

    ell_(a,b)=x^a/N delta_(a+b,d),
    m_(a,b)=x^b/N^2  (unrestricted a,b),
    K_raw=(ell^tensor(k-1) tensor m)v.

Let P_mid project EACH consecutive physical pair to degree d and
define its actual coefficient tensor

    psi_(a1,...,ak)
       =v_(a1,d-a1,...,ak,d-ak),    0<=ai<=d.           (1)

The ordinary caps force their k-1 pair degrees to d. The TOTAL
integer degree then forces the last pair degree to d too. Hence

    K_raw=(ell^tensor(k-1) tensor m_d) P_mid v,          (2)

where m_d is the marked row RESTRICTED only after this argument.
No arbitrary local marking replacement is made. Every C=P L_N and
H=L_N P is block diagonal in pair degree, so P_mid COMMUTES with
the actual positive product G_top=C^tensor(k-1) tensor H. Thus

    E_mid=(P_mid v)^dagger G_top(P_mid v)
                               <=v^dagger G_top v.      (3)

The source is preserved while the positive energy is reduced.

## 2. The literal pair-CD polynomials, not a new spectral model

Let A be the ORIGINAL middle-degree pair Casimir, in the physical
basis |a,d-a>, a=0,...,d. Its entries are

    A_(a,a)=D_a=4qQ^a-q(1+Q)Q^(2a),
    A_(a,a+1)=A_(a+1,a)=t_a=-(1-Q^(a+1))^2.

All t_a for a<d are nonzero. Define the actual continuants

    f_0(z)=1, f_1(z)=(z-D_0)/t_0,
    f_(a+1)(z)=((z-D_a)f_a(z)-t_(a-1)f_(a-1)(z))/t_a.  (4)

Then f_a(c_j) is component a of the normalized actual Casimir
eigenvector v_j with first component one. The distinct nodes are
c_j=2cos((2j+1)pi/N), j=0,...,M, with multiplicities m_j=2 except
the odd simple endpoint m_M=1. The
[full physical CD proof](actual_complete_circle_reflection_positive.md)
gives

    H_d=N sum_j m_j v_j v_j^dagger,
    C_d=N sum_j m_j conjugate(v_j) v_j^T.               (5)

Indeed H=L_N P has the first resolution. In degree d, physical
reversal obeys P v_j=(x^d nu_j) conjugate(v_j), with
nu_j=(-1)^j q^[j(j+1)] of unit modulus, proving the second.
The weights in (5) come from the first normals of the COMPLETE
circle at its double Casimir zeros; they have not been supplied by
discarding the root Jordan data. The original cup also proves

    f_a(c_0)=x^a.                                      (6)

## 3. The coherent polynomial and its exact original marked corner

Define the KNOWN linear transform of the physical tensor (1)

    F_N(z_1,...,z_k)=sum_(a1,...,ak) psi_(a1,...,ak)
       f_(a1)(z_1)...f_(a(k-1))(z_(k-1)) f_(ak)#(z_k),   (7)

where # conjugates coefficients in the real Casimir variable.
The conjugate on the MARKED variable is essential. Its presence
is forced by H rather than C, not a freely chosen phase.
All physical colors are coherently summed in (7) BEFORE an absolute
value or positive norm is taken. Equations (5),(6) prove EXACTLY

    E_mid=N^k sum_(j1,...,jk) m_j1...m_jk
                             |F_N(c_j1,...,c_jk)|^2,    (8)
    K_raw=x^d N^(-(k+1)) F_N(c_0,...,c_0).              (9)

The actual invariant is chi_N K_raw; no external normalization is
silently omitted. Formula (9) concerns the original marked scalar,
not an unknown terminal amplitude chosen to define the transform.
The full corner value uses only f_a(c_0)=x^a and the literal factors
in (2): its last phase is x^(d-ak), not x^ak.

Consequently

    |K_raw|^2 <= E_mid/(2^k N^(3k+2)),                  (10)

because c_0 is a DOUBLE node of weight 2 for every N>=2. This is
the original cap Cauchy budget, now a concrete all-port polynomial
kernel with an explicit physical source and positive measure.

## 4. Exact half-bandwidth fold and polynomial tensor DCT

Raw F_N has degree at most d in EACH variable. Let

    G_N(z)=product_(j=0)^M(z-c_j).

Take the remainder of (7) by G_N in each variable, independently,
and call it Fbar_N. This is an explicit SOURCE-INDEPENDENT linear
fold, of degree at most M in every variable. All grid values in
(8),(9) are unchanged. This folding is made only AFTER the full
circle/source identity (5); it is not an all-input replacement of
the original pair algebra C[z]/P_N by a semisimple algebra before
its coupon acts. It makes no assertion about q-normal derivatives
or about arbitrary analytic continuation off the physical grid.

Expand

    Fbar_N=sum_(0<=ri<=M) A_r product_i T_(ri)(z_i/2).

The exact weighted discrete orthogonality 2M<N gives the tensor DCT

    A_r=(2^s(r)/N^k) sum_j (product_i m_ji)
                   F_N(c_j1,...,c_jk) product_i cos(ri theta_ji),
    theta_j=(2j+1)pi/N, s(r)=#{i:ri>0}.                 (11)

In particular |A_r|<=2^k max_grid|F_N| and
max_[-2,2]^k |Fbar_N|<=N^k max_grid|F_N|. The DCT itself has no
hidden exponential condition factor at fixed k. Exact Parseval is

    (1/N^k) sum_j (product_i m_ji)|F_N(c_j1,...,c_jk)|^2
                       =sum_r 2^(-s(r))|A_r|^2,
    E_mid=N^(2k) sum_r 2^(-s(r))|A_r|^2.                (12)

The original source in these COHERENT coefficient coordinates is

    K_raw=x^d/N^(k+1) sum_r A_r product_i cos(ri pi/N).

Its exact squared dual norm for the Parseval coefficient norm is

    N^(-2k-2)(N/2)^k=1/(2^k N^(k+2)),                 (13)

since sum_(r=0)^M 2^(r>0) cos(r pi/N)^2=N/2. This is a
polynomial original-source cost at every fixed width. In particular
the six-port case k=3 has a literal three-variable marked packet,
full tensor-grid reconstruction, and dual cost 1/(8N^5) in the
coefficient norm, equivalently 1/(8N^11) against E_mid.

## 5. Scope and the branching gate that remains

The three-C trivalent observation on the unchanged saturated source
has a proper simplex support and an exact marked null-direction,
as proved in [the marked metric audit](actual_three_belt_saturated_source_and_marked_metric.md).
The present CCH packet is DIFFERENT: final pair-degree extraction
and its marked coefficient conjugation keep the literal original
co-source. They do not claim that its values form the zero-current
three-object Hopf invariant. The last pair's physical reversal has
the explicit moment currents in that note, equations (16),(17).

The DCT in (11) is controlled, but the source-to-continuant map in
(7), the high-degree fold, and the resulting coefficients A_r need
not have polynomial norms in the original physical metric. Their
actual coherent energy is exactly what (8),(12) retain. Also a
corner value is not automatically as large as the grid maximum.
Thus no general sharp upper, original-cycle survival, geometric
edge equations, or trivalent augmented-graph volume equality follows
merely from this positive representation. A geometric energy
certificate for the actual packet (7), keeping its last-pair current,
would be a substantive next step.

Audit: [literal marked braid sources, pair CD, coherent grid and tensor Parseval](../experiments/audit_actual_marked_multiport_chebyshev_source_packet.py).

Independent analytical review rederived the physical C/H conjugations,
the unrestricted-to-middle marked-source step, all normalization
powers, the two-parity DCT reproducing kernel and exact dual norm.
A separate fresh replay passed seven original CD levels, 21 all-input
tensor packets and four coupled six-head marked braid sources. These
checks do not assert a sharp geometric bound or a generic-q germ.
