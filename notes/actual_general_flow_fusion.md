# General source-preserving fusion of the original charged network

28 October 2026. Two exact operations apply to the WHOLE original
charged source at arbitrary valency and arbitrary braid width:

1. A full length-N-1 block is the source reproducing kernel. It can
   be contracted through ANY polynomial exterior, not merely through
   one complementary Pochhammer.
2. A balanced trivalent charged star is exactly a triangle of three
   root intervals, with an explicit nonzero q-binomial scalar.

The first operation contracts every original closure adapter of a
nontrivial knot at the SOURCE level, retaining the actual pivots.
The second is a genuine higher-valency fusion. Its proof is a
root-orbit divisibility argument and degree rigidity, not a borrowed
analytic pentagon or an assumed positive source.

These operations do not yet reduce every original network or prove
its selected geometric coefficient. A degree obstruction below
explains why arbitrary charge stars cannot simply be declared balanced.

## 1. The source in which the operations are exact

Use N>=2, d=N-1, Q=exp(2*pi*i/N), q=exp(pi*i/N).
The [whole charged bridge theorem](actual_global_charged_bridge_flow.md)
has already proved, with ALL original scalar lines retained,

    K_N=chi_N/N sum_h W_h lambda(P_h),
    lambda(P)=[X_1^d ... X_k^d]P,
    deg P_h=k d.                                    (1)

All h are the actual over-monotone clocks. The canonical
[source theorem](actual_charged_socle_and_fermat_source.md) permits
the SAME lambda to be evaluated in

    A_0=K[X_1,...,X_k]/(X_1^N,...,X_k^N).           (2)

This is an exact equality of the original selected period. It is
not a rule setting every separate regular-grid factor to zero.
The perfect multiplication pairing is lambda(X^a X^b)=delta_(a+b,d).
In particular arbitrary polynomial exteriors are admissible in the
algebraic identities below. No original coupon or scalar is removed.

## 2. Full blocks reproduce arbitrary exteriors

Write B_L(X,Y;a)=product_(r=0)^(L-1)(X-Q^r aY).
Root complementation gives

    B_d(X,Y;a)=sum_(j=0)^d X^(d-j)(aQ^(-1)Y)^j.    (3)

For ANY polynomial F(X,Y,U), with U denoting all other anchors,

    [X^d] B_d(X,Y;a)F(X,Y,U)
       =F(aQ^(-1)Y,Y,U) mod (Y^N,U_i^N).           (4)

There is no valency or individual-degree restriction on F. Indeed
the left side is sum_(j<N)(aQ^(-1)Y)^j [X^j]F. Every missing term
of the substitution has a factor Y^N and vanishes in (2).
Pairing with the remaining original source proves (4) for the
whole scalar. A tail coefficient alpha contributes its actual
factor alpha^d.

The reverse contraction, which may retain a preferred anchor, is

    [Y^d] B_d(X,Y;a)F(X,Y,U)
       =(aQ^(-1))^d F(X,(aQ^(-1))^(-1)X,U)
                                                    mod (X^N,U_i^N). (5)

All displayed monomial factors in (4)--(5) remain. If the two
anchors already coincide, then

    B_d(X,X;a)=X^d G_N(aQ^(-1)),
    G_N(t)=sum_(j=0)^d t^j.

Thus its source contraction is G_N(aQ^(-1)) times evaluation of
the remaining polynomial at X=0, NOT a variable identification.
For an actual root phase t=q^m,

    G_N(t)=N                         if m=0 mod 2N,
           0                         if m even, not0 mod2N,
           2/(1-q^m)                 if m odd.      (6)

Every nonzero value has modulus between 1 and N. Its fixed-order
logarithmic derivatives are bounded by N^(p+1), directly from the
finite sum. This is a general tame fusion of a saturated source
cycle, including its resonant value; no central norm is silently
inverted at resonance.

### All original closure adapters can be contracted

The closure numerator in the actual source is

    C(Z,Y)=sum_(j=0)^d Z^(d-j)(tY)^j=B_d(Z,Y;Qt),
    t=1 on the unpivoted cut, t=Q^(-1) on a pivotal head.

Therefore its SOURCE relation is Z=tY, with the exact factors
of (4) or (5). The original pivot scalar x^(1-N) also remains.
This is the nilpotent-source contraction (4), not the forbidden
pointwise matching of distinct regular Fermat grids or a bare
Cauchy pole substitution.

In the anchored graph the closure edges have in-degree and
out-degree at most one. A closure-only cycle would follow a physical
component through only UNDER encounters and closures, without any
overbridge event. A one-component knot with at least one crossing
has no such component: each of its self-crossings has an over
encounter on the same component. Thus its closure edges form a
forest. Contracting them by (4)--(5) removes ALL b boundary-adapter
anchors, leaving exactly B anchors, one per open overbridge event
(or their canonically identified representatives).

This proves an exact globally sewn original source at the jet
fiber. It retains chi_N/N and every pivot phase. It does not claim
the raw four-Psi continuation has become periodic away from its
sampling grid. For links with a closure-only component, the
remaining cycle is instead evaluated by (6) and its accompanying
zero-anchor substitution.

## 3. Balanced star--triangle identity

Let k_1,k_2,k_3>=0, k_1+k_2+k_3=d, and L_i=d-k_i.
For arbitrary nonzero a_i, the exact polynomial identity is

    [Z^d] product_(i=1)^3 B_(L_i)(X_i,Z;a_i)
       =C a_1^(k_2)a_2^(k_3)a_3^(k_1)
          *B_(k_3)(X_1,X_2;Q^(k_2+1)a_1/a_2)
          *B_(k_1)(X_2,X_3;Q^(k_3+1)a_2/a_3)
          *B_(k_2)(X_3,X_1;Q^(k_1+1)a_3/a_1),      (7)

    C=(-1)^(k_1+k_3)
       Q^[k_1(k_1-1)/2+k_3(k_3-1)/2-k_2]
       *[d-k_2 choose k_3]_Q.                       (8)

All lengths and factorials are at most d; the scalar is NONZERO.
It must be retained. In particular its modulus need not be tame
when all k_i are proportional to N. No half-volume or unknown
period factor is absorbed into C.

The balance condition is exactly L_1+L_2+L_3=2d. The three new
lengths are k_i=d-L_i. The identity remains valid when some are
zero, and after substituting coinciding outer variables.

### Proof by root covering and degree

First set every a_i=1. The left side F has total outer degree d.
For a cyclic pair (i,j) and the remaining index l, specialize

    X_i=Q^p X_j, p=k_j+1,...,k_j+k_l.

The Z-root arcs of the two corresponding blocks are

    {Q^(p-r)X_j:0<=r<L_i},
    {Q^(-s)X_j:0<=s<L_j}.

Their union contains a FULL orbit of N roots. Equivalently their
missing intervals, of lengths k_i+1 and k_j+1, are disjoint at
precisely the displayed k_l positions. Hence the complete product
of all three blocks is divisible, as a polynomial in Z, by
X_j^N-Z^N. Its residual Z-degree is 2d-N=N-2=d-1.
The coefficient of Z^d is therefore zero: the first term cannot
reach degree d and the Z^N term already exceeds it.

Thus F is divisible by all three displayed families of linear
outer factors on the right of (7). Their total degree is
k_1+k_2+k_3=d, exactly deg F, so their quotient is a scalar.
The coefficient X_1^(L_1)X_2^(k_1) at X_3=0 fixes that scalar.
It is

    (-1)^d Q^[k_3(k_3-1)/2+L_3(L_3-1)/2]
                         [L_2 choose k_3]_Q

on the left, and

    (-1)^(k_2) Q^[k_2(k_1+1)+k_2(k_2-1)/2]

in the proposed product. Their ratio simplifies to (8).
Finally rescale X_i by a_i and extract the factors a_i^(L_i).
The remaining scalar powers are a_1^(k_2)a_2^(k_3)a_3^(k_1),
which proves the full formula (7).

Because (7) is an ordinary polynomial identity, it can be inserted
inside ANY original exterior source pairing. The removed central
anchor carries exactly its original charge d; every other anchor
keeps its original charge. No scalar knot value is used to choose
the normalization. Reversing any incident block is permitted with
its exact monomial coefficient, so all strand orientations are
covered.

### Connection and reverse move

For a block of length L, its positive sine-binomial connection is
w=-a q^(L-1). If the three star edges are oriented outer-to-center,
then the new triangle edges obey exactly

    w_(i->j,new)=w_i/w_j.                           (9)

Indeed the extra exponent is k_1+k_2+k_3+1=N and q^N=-1.
Thus the new triangle is flat and has the same boundary path
phases as the old star. Other nonflat cycles of the complete graph
are not erased or declared positive.

Conversely (7), divided by its explicit NONZERO scalar, inserts a
charged anchor into a matching flat triangle. This is an exact
source-preserving inverse move, including zero-length degeneracies.

More explicitly, orient the triangle cyclically with lengths
(k_3,k_1,k_2), sum d, and normalized root parameters
(lambda_12,lambda_23,lambda_31). Its connection is flat precisely when

    lambda_12 lambda_23 lambda_31=Q^2.              (10)

Choose a_1=1, a_2=Q^(k_2+1)/lambda_12, and
a_3=Q^(k_3+1)a_2/lambda_23. Equation (10) supplies the remaining
edge. Thus the inverse has no unsolved normalizer or extension-field
choice. A common nonzero rescaling of all a_i is simply the scale
of the introduced anchor and is canceled by the retained scalar.

This has a genuinely nonzero, nondegenerate typed application inside
the original source, rather than only in an auxiliary graph. For the
figure-eight word [1,-2,1,-2], its actual clocks

    h=(0,a,b,a+b), a>0, b>0, a+b<d,

give the three bulk blocks of lengths (a,b,d-a-b) and holonomy one.
The inverse move therefore has all three positive triangle lengths.
At N=4, a=b=1, the complete original clock-sector coefficient is
exactly 4(q^2-1), hence nonzero. The audit inserts the (2,2,2) star,
retains its original exterior and inverse scalar, and checks the
same coefficient. This example checks applicability of the general
source identity; it is not a proof of nonvanishing for all clocks
in the displayed family or a knot-volume asymptotic.

## 4. What simple source splitting can and cannot balance

The full kernel (3) is also the canonical coproduct kernel of the
source pairing. It permits splitting an anchor into two charged
anchors joined by a full length-d edge, with an arbitrary partition
of the old incident polynomial factors. This is exact by (4).

Let the old incident lengths sum to S. Replace its neighborhood by
r charged anchors and a TREE of r-1 such reproducing edges, without
changing its external factors. The total incident length, counted
at all new vertices, is

    S+2d(r-1).

If every new vertex were a balanced star, that sum would be 2dr.
Necessarily S=2d. Arc subdivision does not change S. Thus an
unbalanced anchor cannot be converted to nothing but balanced
stars merely by inserting source identity kernels and partitioning
its old factors. A two-factor piece with lengths summing to d
does give a balanced star after such a split, but its third edge
is full length d and the triangle move has a zero-length edge.
This alone is not a nondegenerate geometric triangulation.

The local defect S-2d is additive under full-edge contraction and
is unchanged at outer vertices by the balanced star--triangle
move. Defects can be transported or combined; they cannot be
silently discarded. Additional exact channel sums or a genuinely
deficient-star identity would be needed for a universal reduction.

## 5. Scope of the general advance

The full-kernel contraction performs the original boundary gluing
at arbitrary valency. The balanced star--triangle move is an exact
higher-valency rule inside the actual charge algebra, with its
normalizer fixed and its root-orbit proof given above. Both commute
with arbitrary exterior original source pairing and allow repeated
application wherever their algebraic hypotheses hold.

They do not prove that every charged knot graph admits an all-balanced
trivalent resolution. Nor do they turn a general remaining cycle
sum into positive weights or prove its geometric contribution
survives. In particular no quantum determinant or general volume
theorem is inferred from the existence of these local rules alone.

For coverage only, root-of-unity Fermat and restricted star--triangle
identities have substantial precedent, including
[Faddeev--Kashaev, *Quantum Dilogarithm*](https://arxiv.org/abs/hep-th/9310070).
No claim to the first such identity is intended. The independently
proved implementation here is the ordinary polynomial identity with
its exact scalar and the actual selected socle-source contraction;
no proof or analytic contour from that literature is imported.

## 6. Reproducible audit

    python3 experiments/audit_actual_general_flow_fusion.py

The audit checks the arbitrary-polynomial reproducing law, all
balanced length triples and generic coefficients at several roots,
connection transport, and contraction of every actual original
closure adapter inside the whole charged source before comparison
with the original signed physical word scalar.
