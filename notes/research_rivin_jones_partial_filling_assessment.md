# The division-free braid formula and the partial-filling problem

Written comparison, 14 November 2026. The inspected external source is
[rivin-jones, commit e956fb919ac7d1bbc7cb3d3873fbac993feb94b7](https://github.com/igorrivin/rivin-jones/tree/e956fb919ac7d1bbc7cb3d3873fbac993feb94b7).
The mathematical specification, sparse crossing implementation and tensor
contraction description were read. No code from that repository was
imported, executed, or used for a numerical calculation.

The useful contribution is a particularly explicit presentation of the
reduced colored braid scalar. It does not itself prove a volume limit.
The deductions below concern its displayed finite formulas. Identifying
them with every marked free-boundary object in our construction is a
separate task.

## 1. The exact reduced observation

The [mathematical specification](https://github.com/igorrivin/rivin-jones/blob/e956fb919ac7d1bbc7cb3d3873fbac993feb94b7/docs/MATHEMATICS.md)
uses representation dimension \(N\), \(n=N-1\), \(v=A^2\), and
Jones parameter \(q=A^{-4}\). Its crossing entries are Laurent
polynomials in \(A\): the symmetric Gaussian binomials are obtained by a
polynomial recurrence, with no division by quantum factorials.

For a braid with knot closure, one strand is cut and its input and output
are fixed to the highest-weight state. The other strands are traced with
their quantum weights, and the writhe correction is applied. Thus the
displayed scalar has a well-defined specialization at nonzero roots of
unity. It is not obtained by dividing two values that both specialize to
zero.

This is relevant to our prescribed closing functional. Any comparison
must preserve that marked scalar, its framing and its boundary
specializations. Scalar equality for closed knots alone does not identify
an unreduced polynomial at several free boundaries or its normal
derivatives.

## 2. Exact positive magnitudes and the remaining phase

For an integer \(N\ge2\), take
\[
 A_N=e^{-\pi i/(2N)},\qquad
 S_m=\prod_{r=1}^{m}2\sin(\pi r/N),\qquad S_0=1.
\]
All \(S_m\) with \(0\le m<N\) are strictly positive. At this root
the symmetric Gaussian binomial is
\[
 B(a,b)=\frac{S_a}{S_b S_{a-b}}\quad(0\le b\le a<N).
\]
Indeed the symmetric quantum integer becomes
\(\sin(\pi m/N)/\sin(\pi/N)\); its factorial quotient gives the
displayed expression. Equivalently this expression satisfies the finite
Gaussian recurrence used in the implementation.

For a positive crossing, the allowed transition is
\[
 (i,j)\longmapsto(j+k,i-k),\qquad
 0\le k\le\min(i,n-j).
\]
Its coefficient is exactly
\[
 R_+(i,j,k)=A_N^{Q_+(i,j,k)}
           \frac{S_i S_{j+k}}{S_{i-k}S_j S_k},
\]
where
\[
 Q_+=(n-2i+2k)(n-2j-2k)+k(k-1)+Nk.
\]
For a negative crossing the transition is
\[
 (i,j)\longmapsto(j-k,i+k),\qquad
 0\le k\le\min(j,n-i),
\]
and its coefficient is
\[
 R_-(i,j,k)=A_N^{Q_-(i,j,k)}
           \frac{S_j S_{i+k}}{S_{j-k}S_i S_k},
\]
where
\[
 Q_-=-(n-2i)(n-2j)-k(k-1)-Nk.
\]

To check the extra phase in the positive formula, each factor in the
implementation's product is
\[
 A_N^{2(n-i+r)}-A_N^{-2(n-i+r)}
   =-2i\sin\frac{\pi(i+1-r)}N .
\]
The product is therefore \((-i)^kS_i/S_{i-k}\), and
\((-i)^k=A_N^{Nk}\). In the negative formula the corresponding
product combines with its printed \((-1)^k\) to give
\(i^k S_j/S_{j-k}=A_N^{-Nk}S_j/S_{j-k}\).
This proves both identities directly from the displayed coefficients.

In particular every allowed local transition has nonzero coefficient
at the matched root. There is no further local zero rule that removes
the allowed transitions.

Every crossing conserves \(i+j\). After the braid connections and
highest-weight cut are imposed, the entire scalar is consequently a
sum over integer points satisfying linear equalities and inequalities:
\[
 I_N=\sum_{\mathbf m\in\mathcal P_N\cap\mathbb Z^d}
        a_N(\mathbf m)
        \exp\!\left(-\frac{\pi i}{2N}Q_N(\mathbf m)\right),
        \qquad a_N(\mathbf m)>0.
\]
Here \(a_N\) is the product of the positive ratios above. The integer
quadratic polynomial \(Q_N\) also contains the quantum trace and
writhe phases. The braid is fixed; the bounds defining
\(\mathcal P_N\) depend on \(N\).

This is an explicit oscillatory sum. An estimate of its positive
absolute sum is not a lower bound for \(I_N\).

For example, in the charge-two block of \(R_+\), \(N\ge3\), the
diagonal entries at \((i,j,k)=(1,1,0)\) and \((2,0,2)\) are both
nonzero. Their phase exponents differ by \(2n\), so their phase ratio is
\[
 A_N^{2n}=-e^{\pi i/N}.
\]
It is not positive real. Diagonal similarity leaves diagonal entries
unchanged, and multiplication by one common scalar leaves their ratio
unchanged. Hence even this block cannot be made entrywise nonnegative
by a diagonal phase change and a common scalar. This does not exclude
a different, non-diagonal or boundary-dependent construction.

## 3. What can be transferred to the general research programme

The [planned contraction implementation](https://github.com/igorrivin/rivin-jones/blob/e956fb919ac7d1bbc7cb3d3873fbac993feb94b7/docs/PLANNED_CONTRACTION.md)
keeps the same weights while changing contraction order. Slicing fixes
selected internal indices and sums every resulting slice. Backward
support propagation excludes paths that cannot reach the prescribed
output. Those are exact operations. They supply no estimate on
cancellation among paths that remain.

Our [arbitrary-power compiler](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_arbitrary_power_source_compilation.md)
already contracts finite compositions of multiplication, turns and
arbitrary fixed signed crossing powers, and retains
their free ordinary boundary polynomials and normal data. Our
[full scalar-flow construction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_full_psi_scalar_flow_cycle.md),
Section 3, already retains a bounded polytope from weight conservation.
Conservation and exact regrouping are therefore not new missing
theorems in the project.

The useful comparison is more specific. Retain the boundary indices of
an arbitrary short component in the division-free braid presentation,
and prove the exact change from those coordinates to our Newton
boundary polynomial, including the prescribed final observation and
all repeated-root normals. Then retain the complete quadratic phase
when deriving estimates. This could provide a simpler representation
for a general composition proof and an independent check of the source.
It has not yet supplied the required geometric coefficient.

Two distinctions must be maintained in such an argument. Laurent
regularity in \(A\) at fixed integer indices is not holomorphy in
continued summation indices; rewriting the amplitudes as continued
factorial ratios may introduce divisors again. Also the current external
API computes closed knot scalars, whereas the partial-filling theorem
needs boundary data before the final closure.

The repository's finite-level enclosure routines and speed improvements
are useful computational infrastructure. They do not bound the error
to the large-\(N\) limit. They have not been used as proof inputs here.
