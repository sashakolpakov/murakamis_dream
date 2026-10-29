# A positive original cube packet with all four rung colors retained

29 October 2026. Fix the EIGHT cycle channels of the original ordered
cube to the odd Steinberg channel, while retaining EVERY physical
complete-circle channel on its FOUR rungs. The original exposed marked
source has an explicit positive Newton contraction. This includes all
paired nilpotents, gives its exact global support, controls the entire
four-color sum by the central term at polynomial cost, and proves a
strict gap for macroscopic rung-color deficits.

This is a specified sector of the original cube source, with its eight
cycle projections still present. The remaining eight color sums and
even levels are not evaluated. No conclusion about the full cube
invariant or arbitrary cubic graphs is inferred.

## 1. The exact marked packet

Keep N=2m+1>=3, d=2m, q=exp(pi i/N), the literal ordered cube and
its EXPOSED marked white vertex from the
[central cube theorem](actual_odd_central_cube_reflection_packet.md).
Its two cycles have edge orders

    top (0,11,3,2), bottom (9,5,6,8),
    rungs (1,10,4,7).

Every cycle edge has label m. The four rung labels j_0,...,j_3 vary
independently over 0,...,m. For j<=m put

    k_j=2 if j<m, k_m=1,
    z_j(v)=s_(j+v)/[s_(j-v)s_v^2], 0<=v<=j,
    h_j=sum_(v=0)^j z_j(v) Bhat_v,
    P_(N,j)=sum_(v=0)^j z_j(v) beta(m,v)^2,
    S_N=P_(N,m),
    omega_j=kappa(-1)^j q^[j(j+1)], kappa=q^(d^2/2).

Here the Newton basis and functional are the FULL root algebra, not
the distinct-node quotient. In particular h_m is the genuine turned
isolated projector from the central cube theorem. The actual complete
circle sector L_j, paired or simple, obeys

    Rturn L_j=N k_j h_j.                            (1)

Let Z_jvec denote the RAW original marked cube source with these twelve
specified labels and no edge twists. Then

    Z_jvec=N^12 product_(r=0)^3[k_(j_r)P_(N,j_r)^2]
                               phi(h_(j_0)h_(j_1)h_(j_2)h_(j_3)). (2)

All factors and the functional in (2) are the actual ones. For any
fixed signed edge exponents multiply (2) by exactly

    omega_m^(sum_cycle e_l) product_r omega_(j_r)^(e_(rung r)). (3)

Thus a twisted individual label sector has a specified unit phase;
a sum of differently phased rung sectors is not declared positive.

The finite support of the untwisted source is particularly simple:

    Z_jvec>0 iff j_0+j_1+j_2+j_3>=d;
    Z_jvec=0 otherwise.                            (4)

Every LOCAL vertex already has total label 2m+j>=d. The additional
constraint (4) is a genuine global contraction constraint; it cannot
be deduced by keeping only the local black scalar supports.

## 2. The full normal sector turns to a positive polynomial

Let E_j be the FULL Hermite projector of the pair Casimir cluster c_j;
L_j=L_N E_j. At a double node it retains the actual nilpotent circle
normal. The complete Frobenius trace identity gives

    phi(L_j f)=N Tr(E_j m_f)=N k_j f(c_j).           (5)

It follows from the complete polynomial identity for L_N and the
trace of multiplication; the trace in the j cluster has its actual
algebraic multiplicity k_j. No spectral derivative has been removed
from L_j before this identity is used. The Newton turn and pairing
then give the v-th coefficient of Rturn L_j as

    phi(L_j Bhat_v)=N k_j Bhat_v(c_j).

Direct paired-sine factorization gives Bhat_v(c_j)=z_j(v) for v<=j,
and zero for v>j. This proves (1) as a FULL algebra identity. Its
polynomial degree is j, and hence it also specifies its first normal
at every other double node. The paired nilpotent has become an
ordinary low-degree turned polynomial by the actual nonmultiplicative
turn, not by treating it as a positive projector.

## 3. Use the actual physical source's cyclicity

For the finite generic derivation retain the physical cup

    pV(u,d-u)=cV P_d(u), cV=N zeta^(-d^2),
    P_L(u)=(-1)^u zeta^[u(L-u-1)]F_uF_(L-u)/F_L.

All factorials in this generic cup are retained. The root monomial
formula is not substituted off the root. At the root

    gamma_j=q^(2-j^2)/N^2,
    h0_j=k_j N s_(2j)/s_j^2,
    pi_j=gamma_j^(-1)D_phys(W_j),
    L_j=h0_j W_j pi_j.

Choose the regular generic W_j and pi_j lift of the original
[first-normal theorem](actual_nc_morse_graph_first_normal_source_reduction.md).
The latter identity is asserted at the root; its chosen lift is
h0_j W_j(t)pi_j(t). Every denominator in W_j and pi_j is a unit
at this odd root. Paired generic projectors are NOT used.

There is an important simplification for unequal labels: rotate the
actual black source U_abc, rather than assuming that every differently
normalized canonical Theta has the same cyclic scalar. The physical
nested-cup source has entries

    J_((a,b),(c,e),(f,g))=pV(a,g)pV(b,c)pV(e,f).

The ratio to its pair-cyclic permutation is exactly K(a)K(b), because
P_d(d-u)=K(u)^(-1)P_d(u), with d even. Covariance of each pi therefore
proves the generic all-entry identity

    U_abc(alpha,beta,gamma)
       =K_a(alpha) U_bca(beta,gamma,alpha).         (6)

This is valid before specialization and therefore for its first normal
as well. White source tensors have the corresponding genuinely dual
identity. The scalar product of the three fixed gamma factors is
symmetric and does not change (6). No plain leg permutation or
same-order Hermitian dual is introduced.

Use (6) to put each rung in the last black and first white slot, as in
the explicit four-rung table of the central cube theorem. The two
outer cycle objects are both Q_m=V_d, and the rung object is Q_j.
Let W_j:Q_j->V_d tensor V_d be its ordinary Clebsch map and let
D_can use the canonical cups on these two V_d objects. Set

    a_j=(-1)^(d-j) zeta^[-j(j+1)-d],
    Theta_mmj=(W_j tensor I)p_(2j)/a_j,
    s_j=the actual black corner s_(m,m,j),
    U_mmj=(s_j/a_j)(W_j tensor I)p_(2j).            (7)

To verify the anchor a_j, the proved lowest-column identity gives

    W_j[2j](d,j)
       =zeta^[j(d-2j)] h_(d-j),
    h_(d-j)=(-1)^(d-j)zeta^[-(d-j)(j+1)],
    P_(2j)(2j)=zeta^(-2j).

Multiplication gives exactly (7), with no endpoint division by a
zero factorial. Every a_j is a nonzero monomial.

Contracting one rung is now the ALL-SIDE-LEGS-OPEN identity

    (s_j/a_j)^2 W_j D_can(W_j).                    (8)

The two Q_j cup/cap matrices cancel in their actual order. Since the
cycle object's physical cup is cV times its canonical cup,

    D_can(W_j)=cV^2 D_phys(W_j)=cV^2 gamma_j pi_j,
    W_j D_can(W_j)
           =cV^2 gamma_j L_j/h0_j at the root.      (9)

Equations (8),(9) retain the entire paired root operator. In fact for
j<m this rung map is nonzero and nilpotent, with square zero. Splitting
it into a vanishing generic norm times a singular generic projector
would obscure this regular map; no such split is made.

The four rung maps all act on V_d tensor V_d. Their genuine full-cup
turn, cyclic four-box trace and mark are consequently exactly the
entrywise identities (9a),(9b),(10) of the central cube theorem, now
with four different self-dual regular maps. Projector idempotence
was never needed in that index substitution. The exposed physical
mark remains on a cycle V_d strand. It is not transported through
any paired Q_j image. Generic ordinary closure is [N] times the
root-open scalar; taking its first normal and dividing by nu_N is
therefore the original marked value phi of the product of turns.

## 4. All source phases cancel, with paired factors retained

Before simplifying, the preceding contraction gives at the root

    Z_jvec=(N gamma_m)^8 product_r[
         h0_j gamma_j (s_j/a_j)^2]
             phi(product_r Rturn[W_j D_can(W_j)]).

This follows from the original one-gamma-per-edge identity. Its eight
cycle edge factors are N gamma_m; each of the four rung factors is
h0_j gamma_j. The eight actual black/white source scalars are those
in (8), not inferred from a closed theta norm. The mark's single
quantum-dimension normal is treated only after this full contraction.

Insert (9) and then (1). The remaining scalar is

    (N gamma_m cV)^8 N^4
        product_r[k_j gamma_j^2 s_j^2/a_j^2].       (10)

There is no missing h0_j: its occurrence in the edge factor cancels
its explicit reciprocal in the regular map (9).

The proved actual ordered scalar formula gives

    s_j=N^3 A_N(m,m,j),
    A_N(m,m,j)=(-1)^(j+1)
                q^[m^2-2m-j-3] P_(N,j).

Its positive magnitude P_(N,j) is the finite one-leg source, and its
displayed ordered phase is from the full source theorem, not a
permutation guess. Squaring and using (7) yields exactly

    gamma_j^2 s_j^2/a_j^2
              =N^2 q^[2m^2-2]P_(N,j)^2,            (11)

INDEPENDENT of j apart from P_(N,j). Also
N gamma_m cV=q^[2-5m^2]. The complete phase in (10),(11) is

    q^[8-32m^2]=q^[8N(2-N)]=1.

The powers of N are N^4 times N^8, and this proves (2). Full Cartan
and all fixed signed crossing powers give precisely (3), as follows
from the all-normal eigenvalue equality R^e L_j=omega_j^e L_j.

## 5. Exact global support and a whole four-color bound

The positive Newton multiplication theorem applies to every h_j in
(1). Its coefficients are strictly positive at all indices 0,...,j.
If sum j_r<d, the product has degree below d, so phi=0. If sum j_r>=d,
choose integers 0<=v_r<=j_r with sum v_r=d. Their product has positive
coefficient at output d: at each multiplication choose its upper
index, the current partial sum. These partial sums stay <=d<N, so
none of the allowed products vanishes. All other coefficients are
nonnegative. Thus phi(product h_j)>0, proving (4) without a norm or
stationary-phase approximation.

For v<=j<m the exact sine quotient is

    z_(j+1)(v)/z_j(v)
       =sin[pi(j+v+1)/N]/sin[pi(j-v+1)/N]>=1.

The difference of these sines is
2cos[pi(j+1)/N]sin(pi v/N)>=0. The new coefficient at v=j+1 is
positive. In the actual Newton cone this proves

    0<=h_j<=h_m,
    0<P_(N,j)<=S_N.                                (12)

Multiplication and phi preserve the cone. Equations (2),(12), and
k_j<=2 consequently give

    0<=Z_jvec<=16 Z_(m,m,m,m).                      (13)

Let Z_four-rung be the actual source obtained by replacing the four
rung sectors by their FULL complete circles, while retaining the
eight central cycle sectors and taking zero rung twists. Linearity
of the original source makes it the sum of (2) over all four labels.
It follows that

    Z_St<=Z_four-rung<=16(m+1)^4 Z_St.              (14)

The same statement holds after removing the common unit phase of
arbitrary fixed cycle twists. It is not a triangle-inequality bound
on an oscillating rung sum: the summed source itself is positive.

There is also a strict full-source color gap. For every fixed delta>0,
the proved one-leg factorial estimate supplies gamma_delta>0 with

    max_(m-j>=delta N) P_(N,j)/S_N
                 <=poly_delta(N)exp(-gamma_delta N).

Using (12) in (2) gives the entire four-color complement bound

    sum_(max_r(m-j_r)>=delta N) Z_jvec
       <=poly_delta(N)exp(-2gamma_delta N) Z_St.    (15)

All finite source values, not only a selected term or a value-only
Casimir symbol, occur in (14),(15). The bounds are uniform over the
whole four-rung physical color cube and include j=0 and paired axes.
The empty range for an oversized delta is understood literally.

The [proved positive central period rate](actual_positive_newton_cuboctahedral_period.md)
and (14) therefore give

    lim_(N odd) (2pi/N)log Z_four-rung
       =16v8+2Vol(Q_cube)=Vol(actual augmented cube link).

The eight fixed central cycle projections are still a substantive
restriction; (14) does not allow their removal or control interference
from the remaining cycle colors. This partial-source statement is
not a full cube volume-conjecture theorem.

Audit: [all-rung actual marked contractions and full local normals](../experiments/audit_actual_cube_four_rung_positive_source.py),
with [recorded results](../experiments/actual_cube_four_rung_positive_source_results.json).
It compares every rung tuple at N=3,5,7, further physical tuples at
N=9,11, and a signed original edge word at each level. Every actual
U cyclic identity is checked including its first normal; paired rung
nilpotents and the full half-degree turn are checked as operators.
The complex positivity and global support follow from the analytical
proof above, not a sign or nonvanishing interpretation in a finite field.

Independent internal review: the crossing-period agent read the full
analytical proof and replayed all five levels, 369 untwisted original
sources and five signed cases: PASS. The review checked the generic
physical-U clocks, regular paired rung maps, canonical/physical cup
normalizations, complete phase cancellation, support, monotonicity and
whole four-color gap. This is an internal proof audit, not external
peer review or a full cube invariant equality.
