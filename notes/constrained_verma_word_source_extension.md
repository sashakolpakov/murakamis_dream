# Exact finite-word source extension with all head constraints retained

Research proof, 27 October 2026. The actual locally compressed braid
word has a finite presentation inside the common Verma transport with
one multiplier for each internal tail constraint. Explicit unimodular
maps identify this pointed source complex with the original finite-head
complex over the whole two-wall ring. Neither wall nor the head
characteristic operator is inverted.

The unconstrained ambient word also admits an exact finite Feshbach
expansion, resumming every excursion. The two constructions distinguish
the actual constrained source from the uncompressed ambient period.
Their difference is a specified two-wall memory operator, not an
assumed vanishing normal correction.

This continues [the common two-wall source](common_verma_two_wall_source.md),
[the whole crossing factorization](rees_whole_crossing_source_factorization.md),
and [the actual scalar/monodromy source map](source_lattice_monodromy_chainmap.md).
It constructs a source-preserving network extension for every braid
word. It does not identify the unconstrained geometric period with
the selected finite invariant or select its large-level phase.

## 1. A finite ambient module for an arbitrary actual word

Fix N, a braid on b strands, and a specified word with m crossings
of either sign. Use the genuine balanced common-Verma crossings,
including their prescribed Cartan and scalar factors. Put

    delta=1-Q^N, w=M Q^(-N)-M^(-1), t=delta w.

The local coefficient ring retains Q,M and both wall parameters.
Its finite head H has basis the tuples 0<=a_i<N. On head inputs
every crossing preserves total integer index, so every relevant
ambient path lies in the finite free module

    V=span{(a_1,...,a_b): a_i>=0, sum a_i<=b(N-1)}.

Write V=H direct_sum T. Its ranks are

    h=N^b, v=binomial(bN,b), s=v-h.                         (1.1)

The regular balanced coefficients and the first-exit/first-return
calculation in the common-Verma note prove, for each actual crossing
matrix A_i and its inverse sign,

    A_i=[[a_i, w b_i], [delta c_i,d_i]],                    (1.2)

with all four blocks regular over the whole local ring. Here a_i
is exactly the original locally compressed finite-head crossing.
Equation (1.2) holds for all crossings of the specified word, not
only for a particular knot or a small number of tensor factors.

Consequently the original word is

    W_H=a_m ... a_1,

whereas the ambient compressed word is p A_m ... A_1 i. Their
scalar evaluations below use the same original cut, literal pivot,
zero-framing scalar and full modified-dimension line. None is
absorbed into a newly normalized source.

## 2. One finite memory operator resums all excursions

Introduce head variables h_0,...,h_m and internal tail variables
q_1,...,q_(m-1). Set q_0=q_m=0 at the endpoints. Define the head
operator E by an initial or boundary row and the interior rows

    (E h)_i=h_i-a_i h_(i-1), 1<=i<=m.                      (2.1)

For the open pointed word the first row is h_0. More general
boundary rows involving h_0,h_m may be retained, including matrix
or Ore-operator coefficients. Define

    (F q)_i=q_i-d_i q_(i-1), 1<=i<m,
    (C h)_i=c_i h_(i-1), 1<=i<m,
    (B q)_i=b_i q_(i-1), 2<=i<=m,                          (2.2)

with zero in the other head rows. The ambient word equations are

    L=[[E,-w B],[-delta C,F]].                             (2.3)

The tail operator is F=I-D with D strictly lower in word time.
Thus F^(-1)=I+D+...+D^(m-2) is a finite whole matrix. No tail
spectral denominator has been introduced. Direct block elimination
gives

    U_F L V_F=diag(S,F),
    S=E-t K, K=B F^(-1)C,                                 (2.4)
    U_F=[[I,w B F^(-1)],[0,I]],
    V_F=[[I,0],[delta F^(-1)C,I]].

These identities keep the written order and are valid over any
coefficient ring in which delta,w are central. They follow by
two block multiplications. Their source maps are equally literal:
an input (f,0) becomes (f,0), and its head solution is S^(-1)f
where that notation is defined. Thus (2.4) is a pointed Feshbach
reduction, not merely equality of determinants.

The memory kernel has the explicit entries

    K_(j,i-1)=b_j d_(j-1) ... d_(i+1)c_i, 1<=i<j<=m.       (2.5)

This is one full tail visit from exit i to return j. All visits
are resummed by the single matrix S. In the open initial-value
case E is also unit lower triangular, so the complete expansion
is finite:

    S^(-1)=sum_(r=0)^floor(m/2)
                   t^r (E^(-1)K)^r E^(-1).                (2.6)

Every K increases word time by at least two. This proves the
truncation, independently of the dimension of T. Taking the final
head row and initial head column gives the exact all-excursion
expansion of p A_m ... A_1 i. The r=0 term is W_H. In particular

    p A_m ... A_1 i-W_H=t H_beta,                           (2.7)

with its entire quotient computed by (2.5)--(2.6). This refines
the earlier divisibility assertion to an explicit memory resolvent.

### 2.1 A whole excursion-counting source

Replace the upper-right block in (2.3) by -lambda w B. Equivalently,
weight every return from the tail by the central variable lambda.
For the open word the resulting head transfer is a polynomial

    W(lambda)=W_H+sum_(r=1)^floor(m/2)lambda^r t^r W_r.       (2.8)

Here W(1) is the compressed ambient word, and W(0) is exactly the
original finite word. The constant-term extraction is therefore
an actual source operation, uniform for arbitrary word length.
This bookkeeper does not assert braid coherence for intermediate
lambda or define a new knot invariant. It records the internal
source constraints of the specified actual word.

At the intersection delta=w=0 the mixed coefficient in (2.7) is
the explicit one-excursion operator

    sum_(1<=i<j<=m)
      a_m ... a_(j+1) b_j d_(j-1) ... d_(i+1)c_i
                                  a_(i-1) ... a_1,          (2.9)

with all blocks evaluated there. Its rank need not be one.
The complete integral path w=0 and root auxiliary wall delta=0
both kill all ordinary excursions, while retaining their two
different normal directions.

## 3. The constrained whole-source extension needs no localization

Feshbach reduction of the unconstrained word produces S=E-tK,
not E. To retain the actual word on a characteristic locus where
E may be singular, add internal tail multipliers l. Define the
finite matrix operator

    K_con=[[E,       -w B, 0],
           [-delta C, F,    I],
           [0,       I,    0]].                           (3.1)

Its second row is the genuine ambient tail equation with a source
multiplier, and its third row imposes q=0. Thus every internal
finite-head projection is retained. For an actual head solution h,
the full sourced state is

    I_0 h=(h,0,delta C h),
    I_1 f=(f,0,0),
    K_con I_0=I_1 E.                                       (3.2)

The multipliers are the exact boundary currents needed to enforce
the finite source; they are not required to vanish off the walls.

**Whole constrained-extension theorem.** Over any ring, even a
noncommutative Ore ring, the complex K_con is the direct sum of E
and a contractible free pair, by explicit unimodular maps. There
is no inverse of E,F,delta,w or any characteristic factor in these
maps.

Proof: the more general matrix

    K_gen=[[A,B_0,0],[C_0,D,I],[0,I,0]]

satisfies

    U K_gen V=diag(A,J), J=[[0,I],[I,0]],
    U=[[I,0,-B_0],[0,I,-D],[0,0,I]],
    V=[[I,0,0],[0,I,0],[-C_0,0,I]].                        (3.3)

Both U and V are invertible unipotent matrices. Multiplication
first subtracts B_0 and D times the constraint row, then subtracts
the multiplier column times C_0. This proves (3.3) in the displayed
order without commuting any coefficients. The two-term complex J
is contractible because J^2=I. Taking A=E,B_0=-wB,C_0=-delta C,D=F
proves the theorem. It also works for rectangular A; the free row
and column operations merely have the corresponding different sizes.

The exact retractions are

    P_0(h,q,l)=h,
    P_1(f,g,k)=f+w B k,
    P_1 K_con=E P_0,
    P_0 I_0=P_1 I_1=I.                                    (3.4)

Consequently kernels, cokernels and all derived two-term source
classes of the actual head operator are preserved. In a presentation
over a commutative coefficient ring, det K_con=(-1)^rank(T_time)det E
when square. Over an Ore ring the stronger unimodular presentation
equivalence is available directly, with no determinant convention.

The number of extra multiplier/constraint pairs is only

    (m-1)[binomial(bN,b)-N^b].                              (3.5)

Thus the presentation has size linear in word length, despite
the potentially exponentially many excursion patterns. It does
not assert a rank bound independent of N.

## 4. The selected cut and the actual normal source survive exactly

For the open source let f=(psi,0,...,0), with the original head
source at time zero. Applying the original final cut to h_m gives
the actual word evaluation. Extend any such cut by P_0 in (3.4).
Then the extension (3.2) preserves it identically, including all
scalar factors and the physical meridian derivative. An arbitrary
pivotal matrix trace can equivalently be treated as its literal
linear functional on the resulting head transfer matrix; no new
rank-one normalization is needed.

The preservation is stronger than point evaluation. Suppose a
regular whole Q-family has E(Q)h(Q)=epsilon f_1+O(epsilon^2),
Q=zeta(1+epsilon), and h_0 is in ker E_0. Write coefficient
subscripts 0,1. Differentiating (3.2) and taking cokernels gives

    [K_(con,1) I_(0,0)h_0]
                    =I_(1,0)[E_1 h_0] in coker K_(con,0).  (4.1)

The terms K_(con,0)I_(0,1)h_0 and I_(1,1)E_0h_0 disappear in
this quotient. The same exact chain map preserves every higher
normal jet, since (3.2) is a whole identity, and preserves the
marked co-source through (3.4).

If a specified scalar quantum-A/source complex has already been
mapped to an actual head presentation by maps J,R satisfying

    E J=R P,

the new whole sourced-module map is explicitly

    K_con(I_0 J)=(I_1 R)P.                                 (4.2)

In the cited companion-monodromy construction the target is
E=M=T^N-I, with J and R=S_N r as proved there. It is not
automatically the word-time head operator E of Section 2. Applying
the abstract constrained-extension theorem with E=M gives an
extension of that known source complex; identifying it with the
specific Verma word presentation would require a supplied chain
map between those presentations. Equation (4.2) does not construct
that missing map. Wherever the supplied map exists, its factors
N and its physical derivation

    D_phys=Y partial_Y+N U partial_U

are unchanged. The normal X=2 cut remains a co-source on its
thickened lattice; it is not replaced by an ordinary reduced-fiber
evaluation. Formula (4.2) requires the supplied head presentation;
it does not manufacture an all-level bounded-order scalar equation
from a fixed-N matrix calculation.

More generally, established elimination relations on the original
pointed head network survive the contractible extension (3.3)
exactly. It keeps the actual period and its established source
relations without removing a lattice factor. It does not prove
an equivalence with an unspecified scalar quantum-A presentation.
The ambient Verma presentation of this same pointed network now
has all its constraint currents visible.

## 5. Exact behavior under the actual irregular Rees transformation

There is an intrinsic form of (3.1). Let i_T,p_T be the internal
tail inclusion and projection. Then

    K_con=[[L,i_T],[p_T,0]].                                (5.1)

This formulation transports under any actual ambient gauge C_V,
including the ramified irregular Rees gauge, by

    L'=C_V L C_V^(-1),
    i_T'=C_V i_T, p_T'=p_T C_V^(-1),
    K_con'=diag(C_V,I)K_con diag(C_V^(-1),I).                (5.2)

The source maps and cut are conjugated by the same matrices.
The multiplier is an abstract copy of the discarded-state source
module; no regular geometric identification of that copy is assumed.

On the image of the original finite total-index module this is a
finite-rank identity. Its Rees image is spanned by explicit irregular
vectors and need not be a regular finite-rank submodule of the full
cyclic root chart. Each finite u-jet has the known pole bounds,
while the whole source retains its exponential and head flags.

In particular i_T'p_T'=C_V(1-P)C_V^(-1). Its complementary head
projector is the actual transformed projector, containing the
factor exp[-sum p_i u_i/d]. Dropping that factor from the constraint
changes (5.1) and destroys the source equivalence. The whole crossing
factorization gives a regular cyclic matrix and a resonant base
period, but these source constraints remain alongside both.

## 6. The remaining comparison is now a finite memory/source residual

Removing the constraints gives L and the exact Schur operator
S=E-tK. Keeping them gives K_con and exactly E. The mismatch is
the explicitly computed operator

    S-E=-delta w B F^(-1)C.                                (6.1)

Equation (2.9) is its first mixed-normal contribution to the actual
word. Its Rees conjugate must be evaluated with the constraints
and source poles retained; its apparent two-wall vanishing does
not authorize discarding it before contraction.

At a head characteristic point one cannot generally identify E
with S by a regular source-preserving gauge. Already in rank one,
E=x, B=C=F=1 gives S=x-delta w. Their characteristic loci differ.
The augmented operator K_con is still unimodularly equivalent to
diag(x,J), including at x=0. Thus the constrained extension works
where an E^(-1)-based correction would have removed the actual
characteristic point from the comparison.

This gives a concrete next target rather than a proposed phase:
transport the actual constraint/source complex (5.1) to the chosen
geometric framing module, or prove that its memory and co-source
residuals have the required marked transgression there. Smoothness
of the geometric algebraic place alone does not make (6.1) zero.

The exact source extension is uniform in braid word and works before
quantum jets. It does not make the intermediate excursion-counting
family topological, prove a new geometric source identification, or
infer a selected exponential from its whole equality. The normal d
at fixed N and the physical large-level parameter remain distinct.

The [universal algebra audit](../experiments/audit_constrained_verma_word_source_extension.py)
checks the finite excursion sums, two-wall coefficients, constrained
source maps and stable equivalence, including noncommutative entries.
The [independent proof audit](constrained_verma_word_independent_audit.md)
also checks the finite-word rank, ordered Feshbach maps, constrained
source equivalence and normal-jet formulas, with the distinct
word-time/companion-presentation qualification in Section 4 retained.
