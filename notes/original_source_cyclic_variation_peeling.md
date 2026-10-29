# Exact cyclic variation and peeling the original Kashaev cut

Research note, 28 October 2026. This is an exact support theorem for the
original enhanced crossing in
[the independently derived crossing convention](kashaev_crossing_and_period_lattice.md).
It uses neither a Fourier gauge nor an asymptotic estimate. It applies to
every braid position word and every assignment of crossing signs.

## 1. The local cyclic interval

Write Q=exp(2*pi*i/N), q=exp(pi*i/N), and [x] for the representative in
{0,...,N-1}. For a checked crossing with input (a,b) and output (c,d), put

    u=[b-a-1], v=[a-c], t=[c-d], h=[d-b].

For either crossing sign the support condition is exactly

    u+v+t+h=N-1,          [a-b]=v+t+h.                  (1)

Thus, after lifting b to an integer, the output is in the cyclic interval

    b <= d_lift <= c_lift <= a_lift=b+[a-b].           (2)

This follows directly from the original four-index weight and the actual
inverse, including its Q^(-1) normalization. Negative crossings permute
the four factorial indices, so they have the same support.

Given colors x=(x_1,...,x_b) and fixed sentinels L,R, define the integer
cyclic variation

    V_(L,R)(x)=[L-x_1]+sum_(i=1)^(b-1)[x_i-x_(i+1)]
                                           +[x_b-R]. (3)

Every supported adjacent crossing makes V nonincreasing. Indeed, with
neighboring colors p,s, its three affected summands satisfy

    [p-c] <= [p-a]+v,       [d-s] <= h+[b-s],
    [c-d]=t,               v+t+h=[a-b].               (4)

The inequalities are the elementary triangle inequality for nonnegative
cyclic distance. Their defects are nonnegative multiples of N.

## 2. The actual source forces a face at every cut crossing

The original enhancement is mu=-q S, where S e_j=e_(j+1 mod N).
Fix the first cut color to zero. Each summation path in the actual
weighted partial trace runs from

    x_in =(0,[A_2+1],...,[A_b+1])
    x_out=(0,A_2,...,A_b).                             (5)

This is a statement about an individual nonzero path, before summing
coefficients. Choose L=0 and R=[A_b+1]. The interior tail distances in
(3) agree at the two endpoints. Direct subtraction gives

    V(x_in)-V(x_out) = 0   if A_2=0,
                          -N  otherwise.             (6)

Monotonicity therefore forces A_2=0, and V must be constant throughout
the path. Both inequalities in (4) are consequently equalities at
every crossing.

At any crossing in position 1, its left neighbor is the sentinel 0, so

    [0-c]=[0-a]+v.                                    (7)

Only these crossings change x_1. Telescoping (7) from x_1=0 back to
x_1=0 shows that the sum of their nonnegative v's is zero. Therefore

    x_1=0 at EVERY stage; every position-1 crossing has v=0. (8)

In particular, no original source path can lie in a chamber with all
four crossing angles positive at every vertex. Formal strict
concavity on such a chamber is not an assertion that the original
source occupies that chamber.

Before the first position-1 crossing, only position-2 crossings can
change x_2. Their left equality in (4) makes [0-x_2] nondecreasing.
It starts at N-1, because A_2=0. Hence x_2 stays 1 until the first
position-1 crossing. After the last position-1 crossing the same
quantity ends at zero, so x_2 is already zero and remains zero.
Consequently:

    first position-1 crossing: u=v=0;
    last  position-1 crossing: v=t=0.                 (9)

If there is only one such crossing, both statements hold. If there
are none, the original source has no supported paths. These statements
remain valid for links; no scalar-endomorphism assertion is required.

The original absolute crossing weight is N/|F_u F_v F_t F_h|, with
F_j=product_(r=1)^j(1-Q^r). The reflection
|F_j F_(N-1-j)|=N shows that BOTH end crossings in (9) have absolute
weight exactly one. Every other cut crossing is on the tetrahedral
three-corner face v=0. This is an actual source-support reduction.

## 3. Exact q-Pascal boundary operators

Set

    T^sigma_(k,j)=(B_sigma)_(0,k ; 0,j).

All indices below lie in {0,...,N-1}. Directly from the original
crossing formula,

    T+_(0,j)=Q^(1-j),        T+_(k,0)=0 for k>0,

    T+_(k,j)=(-1)^(j-1) Q^[k+(j-1)(j-2)/2]
                         {k-1 choose j-1}_Q,
                         1<=j<=k<=N-1,               (10)

and all remaining entries vanish. The actual inverse crossing gives

    T-_(k,j)=Q^(k-j) conjugate(T+_(k,j)).              (11)

Thus T-_(0,j)=Q^(-1), and, for 1<=j<=k<=N-1,

    T-_(k,j)=(-1)^(j-1) Q^[-j-(j-1)(j-2)/2]
                         {k-1 choose j-1}_(Q^-1).    (12)

For example, (10) follows by replacing N/F_(N-k) with bar_F_(k-1)
and bar_F_r with (-1)^r Q^[-r(r+1)/2]F_r. The wrap row k=0 is kept;
it is not an optional endpoint correction.

In fact T-=(T+)^(-1). To prove this without compressing an inverse
by fiat, let P be the positive-index block of T+, indexed r,i=0,...,N-2:

    P_(r,i)=Q^(r+1)(-1)^i Q^[i(i-1)/2]{r choose i}_Q.

The finite q-binomial theorem gives the inverse q-Pascal matrix

    ({r choose i}_Q)^(-1)
       =(-1)^(r-i)Q^[(r-i)(r-i-1)/2]{r choose i}_Q.

The resulting inverse of P is exactly (12). For the wrap row, the
finite q-hockey-stick identity and the root specialization imply

    sum_(r=i)^(N-2) P_(r,i)=-Q^(-i).

This gives the constant wrap row Q^(-1) in the inverse of T+.
The formula is valid at every N>=2, without a prime-level assumption.

## 4. The full original scalar after peeling

Let W be the braid word in its actual operator order, let w be its
writhe, and let alpha=-q. Construct a word W_peel on b-1 heads by
replacing every position-1 crossing by T+ or T-, and every crossing
in position i>=2 by the same original B+ or B- in position i-1.
No sign, ordering, Cartan scalar, or framing factor changes.

For b>=2 the exact fixed-cut scalar is

    K_N(W)=(-q) alpha^(-w)
      [ Tr_(heads 3,...,b)
          ( W_peel (I tensor mu^(tensor(b-2))) ) ]_(0,1). (13)

The trace in (13) is over the remaining heads except its first one.
For b=2 this is just (-q)alpha^(-w)(W_peel)_(0,1).
The outside factor -q is the retained pivotal coefficient on the
removed ordinary trace of original head 2. The original writhe w
is unchanged, including crossings replaced by T.

Proof: expand the original weighted partial trace into paths. Section 2
forces every first-head label to zero and A_2=0. Restrict each crossing
coefficient accordingly and perform the remaining sums. This gives
(13) term by term, before using cancellation. It is stronger than a
formal compression identity for arbitrary sources.

The first-strand shell is therefore removed uniformly for every
original braid. This differs from
[the classical arbitrary-bridge deformation reduction](arbitrary_bridge_source_reduction.md):
(13) is an identity of the actual finite quantum scalar. Iterating it
without preserving the new T boundary operators is not justified.
The remaining T/B word is complex, and this theorem supplies no
geometric saddle coefficient or volume lower bound.

## 5. Reproducible checks

`experiments/audit_original_source_cyclic_variation_peeling.py` checks
the original matrices and their actual inverses over cyclotomic prime
fields, both q-Pascal formulas and their product, every supported local
cyclic-variation inequality at small levels, full original signed-word
scalars against (13), and the forced faces path by path. The
same-position trefoil and figure-eight words have identical support
and absolute local weights, while their actual selected scalars
differ. The source reduction therefore does not remove the need to
control the original phases.
