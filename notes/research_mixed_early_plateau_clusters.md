# Cycles with early and plateau coordinates

Research consequence, 4 November 2026. This note assembles the early
block bound for arbitrary cyclic arrangements. Its numerical inputs
are separate from the exact incidence argument below. It does not
estimate a coordinate in the later transition or the right region.

## 1. Contours and statement

Fix a cyclic word in types three and four, of length \(m\ge1\).
Let \(r=(r_j)\) be its original geometric critical point, and write
\(c_j=\Im r_j\), \(M=\Re\Phi(r)\). Put
\[
 E=[.1,.12],\qquad P=[.22,.45],\qquad H=7/500.               \tag{1}
\]
For every subset \(S\) of type-four positions, use the exact contour
of the [earlier selected transport note](research_mixed_early_selected_transport.md):
\[
 z_j=x_j+i h_j(x),\qquad
 h_j(x)=
 \begin{cases}
 c_j\min_{k\in\{j-1,j,j+1\}}\rho(x_k),&j\notin S,\\
 H\min_{k\in\{j-1,j,j+1\}}\widehat\rho(x_k),&j\in S.
 \end{cases}                                                \tag{2}
\]
Here \(\rho\) rises linearly from zero at .1 to one at .22,
whereas \(\widehat\rho\) rises linearly from zero at .1 to one
at .12; both are one on \(P\). Their periodic extensions are as
defined in that note. Each original selected Laurent term has an
exact integral on (2), and its Jacobian is bounded by \((38/25)^m\).

Call a block early if at least one endpoint belongs to \(E\), and
let \(n_E\) be the number of such blocks, counted in the original
cycle. A plateau endpoint is changed when its other neighbor belongs
to \(E\). For an unselected endpoint its changed height lies between
zero and \(c_j/6\); for a selected endpoint it lies between zero
and \(H\).

**Theorem 1.** On \((E\cup P)^m\), the true allocated rate of
every selected term is at most
\[
                         M-\frac{n_E}{1000}.                \tag{3}
\]
Consequently, the integral over \((E\cup P)^m\setminus P^m\),
summed over every original selection, is bounded by
\[
                         C N^A e^{N(M-1/2000)}.              \tag{4}
\]
The restricted sum over \((E\cup P)^m\) has the same nonzero
leading coefficient, action, Gaussian branch and level power as the
original unselected plateau integral. The level power remains \(N^0\).
The constants may depend on the fixed word. Both integer-level
parities are included.

## 2. Local bounds and the allocation of costs

For block \(v\), let \(\Gamma_v\) be its complex geometric
supporting plane. Original stationarity gives
\(\Re\sum_v\Gamma_v=M\) at every target, including its imaginary
coordinates. Retain all the smooth expressions \(\psi_f\) in the
true Fourier maximum; each is estimated separately.

An early block has both heights in the independent intervals of the
[early-transition theorem](research_mixed_early_transition_support.md).
For an \(EP\) or \(PE\) block that theorem gives loss
\(\delta=1/100\), together with a credit
\(q_j c_k^2\), where \(k\) is the plateau endpoint and \(j\)
is the low position in the ordered block. Here
\(q_0=11/2\), \(q_1=151/20\). An \(EE\) block has loss
\(\delta\) even if its additional credit is discarded.

If a plateau endpoint lies on a \(PP\) block and is changed, its
other incident block is a unique early/plateau block. Assign that
early block's credit to this changed incidence. Thus no credit is
used twice. A plateau vertex between two early vertices has no
\(PP\) incidence and needs no credit.

For a \(PP\) block with only one changed endpoint, the assigned
credit pays its entire possible phase increase. For an unselected
height this follows from the oriented reset estimate. For a selected
height it follows by convexity between height zero and height \(H\),
using the selected/reset and selected plateau estimates. If the
unchanged endpoint is itself selected, these same endpoint estimates
only improve the bound.

For a \(PP\) block with both endpoints changed, write its original
reference heights as \(a,b\). The full reset and same-sign reset
estimates, together with
[height convexity for all selected branches](research_mixed_partial_selected_heights.md),
give the upper cost
\[
 C_{uv}(a,b)=
 \begin{cases}
 q_0a^2+q_1b^2,&u=v=4,\\
 10(a^2+b^2),&\text{otherwise}.
 \end{cases}                                                \tag{5}
\]
For example, when one height is selected, convexity reduces its
interval \([0,H]\) and the other interval between zero and its
reference height to their four endpoint pairs. Pairs containing a
selected height \(H\) have the established negative bound. The
all-zero pair costs (5), and a pair with one zero costs no more than
(5). This proves the assertion for every mixture of selections.

The two assigned early credits are \(q_0a^2+q_1b^2\). The amount
still to be paid is therefore at most
\[
 \begin{array}{c|cccc}
 (u,v)&(3,3)&(3,4)&(4,3)&(4,4)\\\hline
 C_{uv}-q_0a^2-q_1b^2
 &.006255&.01201005&.0168255&0.
 \end{array}                                                \tag{6}
\]
These are exact rational bounds, using \(|a|,|b|\le.03\) at
type three and \(|a|,|b|\le.057\) at type four.

Each doubly changed \(PP\) block has the pattern \(EPPE\).
Its two boundary early/plateau blocks are distinct and cannot also
pay a second doubly changed \(PP\) block. Let \(d\) count these
blocks. Then \(2d\le n_{EP}\le n_E\). All remaining plateau
blocks have nonpositive defect after the assigned credits. Summing
the estimates yields
\[
 \begin{split}
 \sum_v\Re(\psi_{f,v}-\Gamma_v)
 &\le-\delta n_E+\frac{33651}{2000000}d\\
 &\le-\left(\frac1{100}-\frac{33651}{4000000}\right)n_E
 =-\frac{6349}{4000000}n_E
 \le-\frac{n_E}{1000}.
 \end{split}                                                \tag{7}
\]
This proves (3), uniformly in every forcing choice. A loop with an
early endpoint is an early block and needs no plateau credit. A
two-vertex cycle either has no early vertex, two early blocks, or
only early blocks. Thus the same statement includes lengths one and
two with their literal repeated incidences.

## 3. Passing to the finite integral

Every actual target in (2) lies in the enlarged early cap or a plateau
rectangle. The complete source estimates there keep all finite rows,
midpoint terms and Fourier alternatives. For any fixed
\(\varepsilon>0\), each block is bounded by a polynomial in \(N\)
times the exponential of its true rate plus \(\varepsilon\).
Choose \(\varepsilon<1/(2000m)\). Since \(n_E\ge1\) off
\(P^m\), (7), the fixed Jacobian bound and the finite number of
selections prove (4).

On \(P^m\), (2) is exactly the established plateau contour.
Every nonempty selection has the previous strict exponential loss;
the unselected integral has its original nonzero asymptotic. Adding
(4) leaves that asymptotic unchanged. This is a result for the
specified integration region, not for the entire knot invariant.

The interval \((.12,.22)\), coordinates below .1 and the right
region are not included in this particular assembly. Their established
individual estimates cannot be combined with (4) without also
controlling configurations that mix those regions.
