# Actual memory-charge clocks and first-normal transfer carries

Research theorem and exact audit, 27 October 2026. A transfer clock
has an exact head/Frobenius memory-charge expression on the actual
high integral color. At the root its carry vanishes. In the first
quantum normal only one carry can occur on a tracked strand, and
its entire correction is a bounded whole scaled-clock unit.
Together with the actual quadratic first-normal R theorem, this
gives a finite differential source realization of these inserted
transfer clocks and their bounded moments.

The root clock identity alone is a rewriting of the old position
clock factorization. The additional content is its original
first-normal block carry, bounded Frobenius differential degree,
and canonical actual source germ. This is not yet a Gaussian
two-framing current map.

## 1. The integer charges and exact operator formulas

Use the actual high integral color with basis \(w_{a,s}\),
\(0\le a\le r\), \(0\le s<N\). Define diagonal operators
\[
 Rw_{a,s}=aw_{a,s},\qquad Sw_{a,s}=sw_{a,s},\qquad
 J=NR+S,\qquad C=R-S=(N+1)R-J .
\]
Here C is a MEMORY CHARGE, not a critical-field observable.
All three operators are actual finite matrices with their
constant integral grading before root specialization.

Track input strand 1 to output strand 2. The literal checked
crossing routes are
\[
 R_+:(i,j)\mapsto(j+k,i-k),\qquad
 R_-:(i,j)\mapsto(j-k,i+k).
\]
Writing \(\Delta R=R_{\mathrm{out,2}}-R_{\mathrm{in,1}}\) and likewise
\(\Delta C\), exact integer arithmetic gives
\[
 k=\Delta C-(N+1)\Delta R\quad(+),\qquad
 k=-\Delta C+(N+1)\Delta R\quad(-).                    \tag{1}
\]
These are identities of UNWRAPPED positions, not congruences.

Let \(R_\pm(w)\) multiply each literal transfer-k coefficient
by \(w^k\), with \(w\ne0\). Define the charge-twisted crossings
\[
 R_+^C(w)=(I\otimes w^C)R_+(w^{-C}\otimes I),\qquad
 R_-^C(w)=(I\otimes w^{-C})R_-(w^C\otimes I).
\]
Then at every generic q,
\[
 R_+(w)=(I\otimes w^{-(N+1)R})R_+^C(w)
                                      (w^{(N+1)R}\otimes I),
\]
\[
 R_-(w)=(I\otimes w^{(N+1)R})R_-^C(w)
                                      (w^{-(N+1)R}\otimes I).   \tag{2}
\]
The retained Cartan and mixed half-Cartan signs are unchanged:
(2) multiplies the ACTUAL coefficients in their original order.

Thus no initial diagonal projector is needed for the clock
identity. A projector correlating R and S has a separate
source/current role; it is not an R-invariant subspace.

## 2. Root and first-normal support sharply bound the carry

Put \(\delta=1-Q^N\). By
[the actual first-normal crossing theorem](high_color_first_normal_r_and_frobenius_degree.md),
all transfers \(k\ge2N\) vanish modulo \(\delta^2\).
For \(k<N\), the tracked head can cross at most one boundary.
For a resonant \(k=N+b\), its first normal factors through
\(E^{(N)}\otimes F^{(N)}\) and a root b-transfer.
The latter cannot cross another head boundary: its ordinary
root E or F edge would be zero. Hence
\[
 \Delta R=0\text{ at order zero},
\]
\[
 \Delta R\in\{0,-1\}\quad(+),\qquad
 \Delta R\in\{0,+1\}\quad(-)
                  \quad\text{through first order}.     \tag{3}
\]
A putative two-boundary carry has zero first-normal coefficient.
The negative assertion also follows by differentiating the
actual inverse crossing and its root block permutation.

Denote a first-normal charge-twisted component of block shift
d by \(R_{\pm,1}^{C,[d]}(w)\). Equations (1)--(3) give
\[
 R_{\pm}(w)=R_\pm^C(w)
       +\delta\,(w^{N+1}-1)
                     R_{\pm,1}^{C,[\mp1]}(w)+O(\delta^2).
                                                               \tag{4}
\]
The same positive carry unit appears for both recorded signs
because their nonzero tracked shifts have opposite signs.
For arbitrary components the exact unit is
\(w^{\mp(N+1)\Delta R}\), as in (2).

The interaction first normal has Frobenius PBW degree at most
two. Charge twists rescale raising/lowering operators and
act on head matrices; selecting a fixed block shift is its
ordinary weight grading and does not raise PBW degree.
Consequently the memory/carry form (4) has the SAME degree
bound. The exact one-sided source dictionary of
[the two-clock source](high_color_two_clock_normal_source.md)
turns it into an operator of differential order at most two,
with the original normalized source terms retained.

These q-derivatives belong to the original generic integral
matrix family. Replacing its ordinary pivot by a frozen
root ADO pivot before differentiating would require the
previously retained route adapter.

## 3. Whole scaled clocks and finite transfer moments

For the needed source r=N, the charge eigenvalues lie in
\([-(N-1),N]\). Put \(w=e^{z/N}\). Then \(w^C\) and its inverse
have operator norm at most \(e^{|\operatorname{Re}z|}\)
in EVERY common diagonal metric. On the first-normal carry,
\[
 w^{N+1}=e^{z(1+1/N)}\longrightarrow e^z,              \tag{5}
\]
with all fixed z-derivatives uniformly bounded on compact sets.
No exponential normalization cost in N occurs in this carry.
This is a statement about clock units, not an estimate of the
whole crossing norm or the source's quantum-normal derivatives.

Equation (1) also transports bounded normalized transfer moments:
\[
 (k/N)^h=
   [\Delta C/N-(1+1/N)\Delta R]^h\quad(+),
\]
\[
 (k/N)^h=
   [-\Delta C/N+(1+1/N)\Delta R]^h\quad(-).             \tag{6}
\]
Expand these finite binomials on the carry components (3).
Equivalently differentiate the WHOLE identity (2) in z.
Every fixed h has finitely many charge-moment/carry terms;
no endless WKB expansion is needed. Unnormalized \(k^h\)
retains its explicit \(N^h\).

The endpoint R=N is distinct from R=0 as an integer memory.
A root Q-clock cannot separate them, but the actual block
clock \(Z^R\) does so in its first normal:
\(D_Q Z^R|_{Q_N}=NR\). Folding these endpoints together
would lose precisely the additional normal current.
Zero-extended current tails and their literal cut endpoint
coupons must likewise remain; no cyclic identification is
made by (1)--(6).

## 4. The memory clock has an actual whole source

For the canonical high-color two-flag source, write \(x=tu\)
and retain its actual normalization \(U_s(q;t,u)\).
The charge character is exactly
\[
 \Phi_{h;t,u}(w^C)=
   \sum_{s=0}^{N-1}H_s(h)\,w^{-s}
                    \frac{U_s(q;tw,u)}{U_s(q;t,u)}.   \tag{7}
\]
At the root this becomes
\[
 \left(\frac{1+h/w}{1+h}\right)^{N-1}
                   \left(\frac{1+xw}{1+x}\right)^r . \tag{8}
\]
Away from the root the source-unit derivatives do NOT cancel
for this insertion, since \(w^R\) depends on the block.
They are the actual derivatives of U_s, not an arbitrary
continuation of (8).

Alternatively, for the normalized ordinary TRACE co-source,
\(w^C=w^R\otimes w^{-S}\) has the product of the exact
[dual clock lifts](dual_clock_normal_cut_source.md), in source
dimensions \(r+1\) and N respectively. Tensor products,
actual source permutations and their duals are transported
as matrix operators. They are not pointwise products of
coherent symbols. A source permutation need not have bounded
norm in every coherent metric; no such assertion is used.

The trace extension agrees with the original average cut on
the actual conserving diagonal arrays. It is not a replacement
for that average on arbitrary off-diagonal Ward matrices.

## 5. What advances beyond the old factorization

At root order, (2) is algebraically equivalent to splitting
a transfer into input/output POSITION clocks. By itself it
introduces no independent geometric co-source. In a closed
uninserted root knot, Frobenius labels are transparently
transported around the component; their normalized source
dependence cancels.

The new source content is the first-normal carry in (3)--(4):
it is an original high-color block arrow with a concrete
quadratic Frobenius operator, actual source-unit derivatives,
and a whole bounded scaled-clock factor. It can be compared
to the second current without guessing an abstract Borel
isomorphism or discarding an unwrapped carry.

A complete current map must still transport the inserted
source/coupon and its endpoints through the whole word,
including its contravariant star action. This theorem does
not identify the resulting insertion with the independent
geometric framing flow, nor equate the low/high whole color
jets or prove Gaussian naturality. It specifies the exact
finite operator data that such a map must use.

## 6. Exact audit

[The script](../experiments/audit_actual_memory_clock_and_normal_transfer.py)
uses independently assembled original positive and negative
integral R entries over a finite field with dual numbers.
At \((N,r)=(2,3),(3,3),(4,4),(5,3)\), it checks 13,188
coefficient routes, their exact integer clock factors, all
root/first-normal carry restrictions and the correction (4).
It also multiplies the full positive and negative total-position
blocks and checks their inverse relation to first normal order.
[Results](../experiments/actual_memory_clock_and_normal_transfer_results.json)
record the signs, carries and block counts.

