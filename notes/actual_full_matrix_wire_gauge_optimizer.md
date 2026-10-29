# The finest crossing bound is unchanged by arbitrary matrix wire gauges

29 October 2026. Allowing off-diagonal matrices on individual physical
wires does not improve the existing alternating-sign crossing bound.
This extends the earlier diagonal optimizer theorem to every positive
definite one-wire matrix, with the original paired source fixed. The
proof uses the full one-head density matrices, not only their diagonal
entries. It does NOT exclude entangled metrics on several wires,
coherent clock packets, or norms formed after block contraction.

## 1. Exact source-preserving matrix gauges

Use the original balanced crossing matrices and paired plat source of
[the weighted energy theorem](actual_weighted_fourier_plat_energy.md).
At the bottom a cup pair is, up to its retained scalar, vec(U), where
U is an anti-diagonal unitary matrix. At the top the ordinary or marked
co-source similarly has an anti-diagonal unitary coefficient matrix;
the ordinary pair includes its actual pivot. The marked pair is used
only after the already proved whole-degree reduction. No source is
changed on a separately dephased state.

On each physical wire segment choose an arbitrary positive matrix
P_e=exp(H_e), H_e Hermitian. At a bottom pair require

    P_o U P_e^T=U,
    H_e=-U^T H_o^T bar(U).                         (1)

The second identity is equivalent to the first, by the unique Hermitian
matrix logarithm. At a top pair apply the same formula to the conjugate
of its actual cap matrix. These relations fix the actual input vector
and output covector. In particular their diagonal entries obey

    (H_e)_(b,b)=-(H_o)_(d-b,d-b), d=N-1,            (2)

regardless of the off-diagonal entries or the retained root phases.
Bottom and top gauges can be chosen independently subject to their
own source relations. Untouched wires keep the same matrix at both ends.

For a gate v define

    C_v=(P_out,1 tensor P_out,2) R_v
                         (P_in,1 tensor P_in,2)^(-1),
    F(P)=sum_v log ||C_v||_HS.                     (3)

All interior gauges cancel in the full original product. Equations
(1) retain its endpoint source, so the standard whole-source bound
using (3) remains valid, with the same external polynomial factors.

## 2. The full one-head densities are diagonal

Every literal R_v preserves total INTEGER head degree. Therefore
R_v R_v^* and R_v^*R_v commute with the sum of the two degree
operators. Taking either partial trace shows that EACH one-head
reduced density commutes with the simple one-head degree operator.
It is consequently diagonal. This is an exact matrix statement,
including the complete-color endpoint and its nilpotent source.

Normalize these reduced matrices by ||R_v||_HS^2. For R_+, symmetry
R_+^T=R_+ makes its input and output first-head densities equal,
and likewise for its second head. Denote their diagonal probabilities
by p_H and p_L. The literal factorial reflection gives

    p_H(a)=p_L(d-a).                              (4)

For R_- the two one-head densities are exchanged. These are the
same exact coefficient identities proved in
[the diagonal gauge theorem](actual_convex_gauge_block_energy.md),
now supplemented by the off-diagonal vanishing above. The common
Cartan/framing scalar is a unit phase and remains external.

## 3. Convexity along every Hermitian gauge ray proves the optimizer

Assume the actual signed word has

    sign(sigma_i)=epsilon*(-1)^(i+1), epsilon=+1 or -1,          (5)

at each occurrence of generator i. Its index sequence, number of
crossings and even width are otherwise arbitrary. When its plat is
a one-component knot, all original source identifications above apply.

For ANY collection H satisfying (1), set P_e(t)=exp(t H_e).
The endpoint relations hold at every real t. Vectorizing a gate gives

    vec(C_v(t))=exp(t K_v) vec(R_v),
    K_v=H_out,1+H_out,2-H_in,1^T-H_in,2^T,          (6)

where each term acts on its own tensor leg. Thus K_v is Hermitian.
By its finite spectral decomposition,

    log ||C_v(t)||_HS
      =one_half log sum_j w_j exp(2t lambda_j), w_j>=0.        (7)

Its second derivative is twice the variance of lambda_j under
the displayed normalized weights, hence nonnegative. No assumption
that different H_e commute is used: the four operators in (6) act
on separate legs. F(P(t)) is therefore convex in t.

At t=0 its derivative is the sum, over every outgoing wire, of
Tr(H_e rho_out,e), minus the corresponding incoming terms. Under
(5), every odd physical wire has the same normalized one-head
density at all its incident gates, and every even wire has its
reflected density. All interior terms cancel. At a paired boundary
the remaining terms cancel by (2),(4). Off-diagonal H entries
contribute zero because the full densities are diagonal. Therefore

    dF(P(t))/dt at t=0 =0.                        (8)

Convexity on the ray from identity to any prescribed P proves the
EXACT finite-level theorem

    inf_{all positive matrix wire gauges preserving source} F(P)
                       =m log ||R_+||_HS,          (9)

where m is the number of crossings. Flat gauges attain the right side.
This is a proof for all admissible matrices, not numerical optimization
over a chosen finite set of off-diagonal perturbations.

The same conclusion holds if invertible complex one-wire gauges are
allowed. Write each as U_e P_e by polar decomposition. At every gate
the outer unitary factors do not change its HS norm. The positive
parts preserve the unitary paired source too: if A U B^T=U, then
B=U^T A^(-T)bar(U), whose positive polar factor is
U^T P_A^(-T)bar(U). The analogous cap formula follows from
A^T L B=L with its unitary L. Thus (9) applies to their positive parts.

## 4. Operator norms and the actual scope

Each crossing acts on N^2 dimensions, so

    ||C_v||_HS/N <= ||C_v||_op <= ||C_v||_HS.

Consequently the optimum product of operator norms differs from the
HS optimum by at most a power N^m. The already proved crossing
factorial asymptotic gives, for all these matrix wire gauges,

    inf sum_v log ||C_v||_op
                      =m N v_8/(2pi)+O_word(log N).            (10)

This is a limitation of the finest local norm estimate, not a lower
bound on the knot invariant. It leaves all cross-gate interference
outside the norm, which is precisely what the desired coherent Gram
must recover. The normalized-star identities and the new Pascal
packet metric act on coupled boundary/coefficient data; they are not
excluded by (9). Neither a general tensor-product wire metric nor a
diagonal clock metric can by itself supply the sharp geometric bound
for the alternating-sign class (5).

The original source and degree hypotheses are explicit. This theorem
does not apply an ordinary positive pivotal trace at color N, nor does
it assert that every alternating knot presentation has pattern (5).

[Audit](../experiments/audit_actual_full_matrix_wire_gauge.py): literal
positive/negative crossing reduced densities, original cup/cap matrix
gauges, zero derivatives and finite off-diagonal gauge rays at several
widths. The proof of the all-matrix optimizer is (6)-(9).
