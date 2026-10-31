# Continuous full-kernel entropy and exact identity reduction of maxima

Completion: the [general endpoint theorem](general_fejer_endpoint_source_volume.md) assembles this local result into the actual augmented-volume equality. Its [unique geometric maximum](actual_fejer_unique_geometric_maximizer.md) gives concentration; the original filling conjecture remains open.

31 October 2026. Independently reviewed full-kernel entropy and identity-reduction theorem. This uses the [proved uniform closed local coefficient limits](actual_fejer_half_block_entropy.md). It does not assume that an infeasible
fixed half-label pattern becomes feasible. It sums the full positive
local kernel before forgetting its type.

## 1. The full local coefficient entropy is continuous

For q=(X,B,C,Y)>=0, X+B+C+Y=1, define h(q) as follows.

If C>=1/2, put h=E(B,1-C,X). If B>=1/2, put h=E(C,1-B,X).
If B,C<=1/2, put

 h(q)=max_s { Ctri(s,B,1/2-B-s)
                  +Ctri(X-s,C,1/2-C-X+s) },          (1)

where max(0,X+C-1/2)<=s<=min(X,1/2-B), and
Ctri(alpha)=V(2pi alpha)/(2pi) is the proved triangle entropy.
The conventions agree on every overlap. At C=1/2 the second triangle
is pure-middle, of entropy zero, and (1) is Ctri(X,B,Y), which is
EXACTLY E(B,1/2,X). The B=1/2 boundary is reflected. At B=C=1/2
all entropies are zero. The interval in (1) has continuous endpoints,
so compact maximization and continuity of Ctri prove h is continuous
on the whole simplex. The closed half-block theorem proves the same
for its two one-sided pieces. In particular

 h(0,B,1-B,0)=0 for every 0<=B<=1.                    (2)

Let p_N(n) be the coefficient of the FULL positive polynomial P in a
nonnegative local exponent vector n of total degree d=N-1. Every such
coefficient is positive. The exact supports partition all these vectors
into cross (both middle<=m-1), left (c>=m), and right (b>=m).
The uniform half-block limits, positive cross convolution and
B_cross<=P_cross<=3B_cross give

 sup_(n>=0, sum n=d) |N^-1 log p_N(n)-h(n/d)| ->0.    (3)

For the cross convolution the allowed outer-split interval has integer
endpoints. Every limiting split has an O(1/N) integer approximation;
there are O(N) summands. Uniform continuity of Ctri therefore makes
its log-sum rate uniformly the maximum (1), including the terminal
faces. The finite forced outer unit is retained in this argument.
The changes from i/N,j/N to n/d are O(1/N) in the closed parameters,
so continuity justifies that normalization. This is NOT a bound on
an individual cross term by H1 at zero outer degree.

## 2. A shared variational theorem without fixed half labels

Take any fixed finite incidence graph of these homogeneous degree-d
polynomials, allowing repeated global labels among a port's four
separate incidences. Give every ordinary face target d and each
protected face target zero. Let P be the nonnegative real flow polytope
with port supplies1, ordinary face demands1 and protected demands0.
If its total supplies/demands disagree, or the polytope is empty, the
coefficient is zero. Otherwise

 lim_(even N) N^-1 log [original target] product_e P_e
                 =max_(q in P) sum_e h(q_e).          (4)

The upper bound follows by (3) and the polynomial number of arrays.
For the lower bound, take a maximizing q and multiply by d. This gives
EXACT integer node balances with real edge values. Fractional-cycle
rounding inside each floor/ceiling interval gives an integral flow,
with error at most one per incidence. The local polynomial contains
EVERY degree-d monomial, so this rounded array is an actual positive
term, regardless of which half label it receives at that level.
Continuity of h and (3) give its desired rate. Repeated incidences
remain parallel arcs in the rounding graph.

Thus (4) agrees with the previously proved W_D on the original diagram,
since both are limits of the SAME source. It does not deny the original
eventual-feasibility test for FIXED patterns; it avoids assigning a
fixed pattern at the seams, where h has the same continuous value.
The formulation also applies to actual identity-smoothed incidence
maps even when they are not simplicial right-angled certificates.
No arbitrary graph-to-original-plat adapter is asserted.

The same argument permits some local H1 factors. At such an identity
port remove its two outer incidence arcs; the remaining middle loads
sum to one and its coefficient entropy is identically zero. All its
allowed coefficients are one, and fractional-cycle rounding respects
this reduced incidence graph. Thus the corresponding mixed flow maximum
is the ACTUAL mixed positive coefficient rate as well.

## 3. A maximum with pure-middle ports is an exact lower-port problem

Let q attain (4), and let D be ANY collection of its pure-middle ports,
including ordinary one-sided diagonals and a pure-middle cross endpoint
(0,1/2,1/2,0). Replace those full local P factors by H1. The SAME q is
feasible in the mixed identity flow polytope and has the same entropy
by (2). Therefore the mixed maximum is at least W_D. Conversely,
coefficientwise H1<=P_diag<=P, so its actual mixed coefficient rate is
at most W_D. Hence

 W_D = rate of the actual mixed source with H1 on D. (5)

This equality is about the FULL summed local kernel and its rate.
It makes no false finite comparison between a cross boundary monomial
and H1. In particular it repairs the pure-middle cross seam only after
(3)--(4), without relabeling an infeasible fixed source pattern.

Feasibility forces the diagonal middle graph to be a forest: every
possible original even-gap cycle contains the protected exterior, and
its unit edge supplies exceed that component's ordinary demands.
A tree cannot contain two protected vertices either. The [exact subtree coefficient identity](actual_fejer_diagonal_identity_forest_reduction.md)
therefore identifies the mixed H1 coefficient with the true connected
identity smoothing, with all face targets and no multiplicity. Thus
(5) is a genuine reduction to fewer remaining positive P ports.

What it does NOT yet prove is that the resulting non-simple smoothed
incidence graph has a regular entropy maximizer or that its W is bounded
by the original complete volume. Matching/matching cuts can still carry
asymmetric Green loads; their complete-source block factorization is
not assumed. The remaining geometry must retain the actual smoothing
and, when restoring deleted cusps, its literal identity meridians.

Independent analytical review: root, coherent and cluster each completed
a full proof read of the continuous seam values, uniform local rate,
unrestricted original coefficient rounding, mixed H1 supports and exact
maximum identity reduction. This review does not infer a volume bound
for every non-simple smoothed source or a quantum filling asymptotic.
