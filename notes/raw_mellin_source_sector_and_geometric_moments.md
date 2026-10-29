# The actual raw Mellin limit sees the source sector before the residue

Independent actual-state diagnostic, 27 October 2026. The exact
cyclotomic Mellin formula shows where an action-normalized geometric
moment cannot be read off. Under the already used domination of the
ordinary-color tail, the whole selected root function becomes constant
after division by its Kashaev residue, on an open X-region. Its leading
shift sector there is the complete/source branch. The geometric
exponential can still occur in that constant residue.

For the figure-eight, the required domination follows from the
already independently proved selected positive-sum asymptotic. Thus
this is an actual prototype conclusion, not a competing state.

## 1. Exact root functions and the open-region theorem

Use [the actual cyclotomic Mellin fiber](cyclotomic_mellin_residue.md):
\[
 Z_N(X)=\frac{A_N(X)+K_NX^N}{1-X^N}-p_N(X),\qquad
 A_N(X)=\sum_{r=1}^{N-1}C_r(Q_N)X^r,
\]
where \(p_N\) is the fixed starting-color prefix and
\(|C_r(Q_N)|\le D_N\). Its degree and coefficient bounds are
polynomial in \(N\); its length is fixed for \(p_N\).
Suppose along the sequence in question that
\[
              ND_N/|K_N|\longrightarrow0.             \tag{1}
\]
Then locally uniformly on \(\{|X|>1\}\),
\[
 \frac{Z_N(X)}{K_N}\longrightarrow-1,\qquad
 \frac{Z_N(Q_NX)}{Z_N(X)}\longrightarrow1.              \tag{2}
\]

Proof: for a compact set with \(|X|\ge R>1\),
\[
 \left|\frac{A_N(X)}{1-X^N}\right|
       \le \frac{D_N}{1-R^{-N}}
                   \sum_{j=1}^{N-1}|X|^{-j}
       \le C_R D_N .
\]
The fixed prefix is \(O_K(D_N)\). Meanwhile
\(X^N/(1-X^N)\to-1\) exponentially and uniformly.
This proves the first limit using even the weaker condition
\(D_N/|K_N|\to0\). The Q-rotated compact set remains in the
same exterior region. Apply the same uniform bound to get the
second limit; its denominator stays nonzero for large \(N\).

Cauchy's formula gives every fixed X-derivative of the first
limit. In particular
\[
     D_X^jZ_N(X)/K_N\longrightarrow0,\qquad j\ge1.
\]
The errors are exponentially small from the complete term and
polynomially bounded ordinary tails divided by \(K_N\).
If \(K_N\) has a positive exponential lower bound, multiplying
these errors by any fixed power of \(N\) still sends them to zero.

Thus every fixed-order X-differential moment with only a bounded
Laurent pole in \(Q-1\) has the same leading source-sector
collapse. It does not expose the geometric residue action.
This is consistent with the actual homogeneous Mellin operator:
its canonical source quotient supplies the \(S=1\) branch.

## 2. A second open region when a positive rate is known

If \(\log|K_N|/N\to s>0\), then on every compact annulus
\[
                    e^{-s}<|X|<1
\]
one instead has
\[
 \frac{Z_N(X)}{K_NX^N}\longrightarrow1,\qquad
 \frac{Z_N(Q_NX)}{Z_N(X)}\longrightarrow1.              \tag{3}
\]
Indeed the ordinary numerator is \(O(D_N/(1-|X|))\),
whereas \(K_N|X|^N\) grows exponentially on that compact
annulus. The complete term is exactly root-shift invariant.
At the intervening transition scale the estimates do not
claim a normal-family limit.

For the actual figure-eight, the selected asymptotic already
proves \(s=\operatorname{Vol}(4_1)/(2\pi)>0\).
Equations (2)--(3) therefore hold for that actual finite state.
They do not prove a positive rate for another knot.

## 3. Consequence for the next source moment

The residue identity remains exactly
\[
           K_N=\operatorname{Res}_{X=\infty}Z_N(X)\,dX/X .
\]
The coefficient can have positive geometric exponential growth
while the raw normalized function in (2) is constant and its
root shift ratio is one. A geometric critical algebra cannot
therefore be inferred from a nontrivial leading fixed-X branch
of this raw selected function.

This matches the exact centralizer obstruction: a whole
commuting endomorphism preserving the actual starting lattice
acts on the selected generic Mellin section by a scalar in
\(k(Q)\). Its observable quotient is shift-invariant, hence
constant in X; affine source uniqueness then fixes its action.
At roots, monodromy moments of the selected section are exactly
one and have rank-one Hankel matrix.

The productive next moment must be defined after the residue,
action normalization, or an actual relative quantum-normal
source construction. The field/trace nonvanishing theorem can
then be tested on that new object. Neither the whole compact
source trace nor its Gauss-wall row has yet supplied that map.

This diagnostic does not rule out such a relative construction.
It fixes the order of operations and prevents interpreting
the already scalar closed cut as a decomposition of geometric
phases.

## 4. Independent check of the formal critical-observable adapter

The construction in
[the actual commutant/critical-observable note](actual_pointed_commutant_and_critical_observable.md)
passes independently. Normalized actual Gaussian insertion moments
form a formal matrix M with a nonzero Vandermonde leading determinant.
Thus \(M^{-1}\operatorname{diag}(\sigma\theta)M\) is defined,
Galois-descended, and satisfies the exact critical polynomial.
Its differential and difference covariance rules follow by direct
conjugation; they are not commuting endomorphism rules on the raw
pointed Mellin lattice.

The observable is formally corrected. In general its action on
the unit source is not the raw first-insertion basis vector:
that raw moment already has higher Gaussian corrections.
Its powers therefore require the corresponding formal combinations
of the actual insertion columns. The construction gives no final
selected co-source on this corrected module. That is precisely
the remaining moment transport, rather than an additional
monodromy eigenvalue of the raw selected state.

