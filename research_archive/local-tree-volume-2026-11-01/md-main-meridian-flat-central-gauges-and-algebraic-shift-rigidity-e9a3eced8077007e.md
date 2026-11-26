# Full formal microscopic data, central gauges, and algebraic shift ratios

Private derivation, 1 November 2026.

This note separates two questions. Full formal microscopic asymptotics need not determine the exact meridian state, even when every ordinary color and its pointing are retained. On the other hand, a multiplier whose shift ratio belongs to one fixed algebraic family cannot change that ratio while remaining invisible to every microscopic order. Neither statement identifies a source-selected characteristic with a geometric representation curve.

## 1. A flat central modification preserving the actual root operator

Let \(q_N=e^{\pi i/N}\), \(Y=M^2\), and \(U=Y^N=M^{2N}\). Fix an integer \(J\ge0\), and set
\[
 g_N(M)=1+2^{-N}(U-1)^{J+1},\qquad
 \widetilde F_N(M)=g_N(M)F_N(M).
 \tag{1}
\]
Here \(F_N\) is any given even Laurent family, for example the actual zero-framed reduced state. The modified family is a manufactured scalar family; no assertion makes it an invariant of a knot or a functor on tangles.

The multiplier is central for the exact root shift \(M\mapsto q_NM\). Therefore, for every rational-coefficient root difference operator \(P_N\),
\[
 P_N(\widetilde F_N)=g_N P_N(F_N).
 \tag{2}
\]
Since \(g_N\) is a nonzero element of \(\mathbb C(M)\), the two scalar families have exactly the same rational annihilator ideal at each level. In particular every specified fixed all-level operator annihilates one if and only if it annihilates the other.

At every allowed ordinary point \(M=-q_N^j\), including the complete point \(M=1\), one has \(U=1\), hence
\[
 \widetilde F_N(-q_N^j)=F_N(-q_N^j).
 \tag{3}
\]
The difference vanishes to order at least \(J+1\) at every such point. Thus all fixed meridian jets through order \(J\) are preserved. The Laurent-degree increase is at most \(2N(J+1)\), still linear in \(N\) with a fixed constant.

On the microscopic coordinate \(M=q_N^s\), however,
\[
 g_N(q_N^s)
   =1+2^{-N}(e^{2\pi i s}-1)^{J+1}.
 \tag{4}
\]
On every fixed complex compact in \(s\), this differs from one by \(O(2^{-N})\), with the same estimate for each fixed derivative. It is a unit there for large \(N\). The two families have identical asymptotic expansions to all algebraic orders in \(N^{-1}\), including logarithmic expansions wherever the original normalized family is nonzero.

There is also an explicit off-root lift of the multiplier:
\[
 D_N(q,Y)=\prod_{j=1}^{N}(Y-q^{2j}),\qquad
 g_N(q,Y)=1+2^{-N}D_N(q,Y)^{J+1}.
 \tag{5}
\]
At \(q=q_N\), the product is \(Y^N-1\). Along each generic ordinary curve \(Y=q^{2j}\), \(1\le j\le N\), the lift is identically one. Thus it preserves every derivative taken along that ordinary curve of any supplied finite lift of the state. At a root ordinary point it also preserves every mixed \((q,Y)\) jet of total order at most \(J\), because the additional term has a zero of order at least \(J+1\). This does not preserve an entire quantum-normal source as a function of a free meridian: (5) is generally nontrivial off those curves.

The same fixed full modified dimension can be retained. Multiplying \(F_N\) by (1) introduces no new normalization convention, and \(g_N=1\) at each ordinary pole means the corresponding principal residue of \(d_NF_N\) is unchanged. This is a scalar ambiguity in the state, not permission to change the actual source.

Most importantly, (2) means this example cannot disprove selection of a classical operator factor. It leaves the annihilator itself unchanged. It shows why exact state reconstruction and characteristic selection are different problems.

## 2. Rigidity of a fixed algebraic microscopic shift ratio

Here is a complementary elementary statement. Suppose \(g_N\) is a nonzero meromorphic family for which, on a fixed open microscopic region containing a disk and its translate by one,
\[
 g_N(q_N^s)=1+O_L(N^{-L})
 \tag{6}
\]
for every fixed \(L\), locally uniformly. Suppose also that its shift ratio
\[
 a_N(M)=\frac{g_N(q_NM)}{g_N(M)}
 \tag{7}
\]
satisfies a single nonzero algebraic equation
\[
 A(q_N,M,a_N(M))=0,
 \qquad A(q,M,Z)\in\mathbb C[q^{\pm1},M^{\pm1},Z].
 \tag{8}
\]
The equation and its degrees are independent of \(N\). It may be obtained from a fixed rational equation by clearing denominators. Then \(a_N(M)\equiv1\) for all sufficiently large levels.

To prove this, remove the greatest power of \(Z-1\) from \(A\), writing
\[
 A=(Z-1)^mB,\qquad B(q,M,1)\ne0.
 \tag{9}
\]
If \(a_N\not\equiv1\), the identity of meromorphic functions (8) forces
\(B(q_N,M,a_N(M))\equiv0\). Equation (6) on the two translated regions gives \(a_N(q_N^s)=1+O_L(N^{-L})\) on their common base disk.

Put \(h=\pi i/N\). The function
\[
 B(e^h,e^{hs},1)
 \tag{10}
\]
is analytic in \(h,s\) and is not identically zero. Indeed the map
\((h,s)\mapsto(e^h,e^{hs})\) has nonzero Jacobian for \(h\ne0\), so it cannot send an open set into the zero set of a nonzero Laurent polynomial. Consequently (10) has a finite first nonzero coefficient \(h^r b_r(s)\), with \(b_r\) not identically zero. Choose \(s_0\) in the base disk with \(b_r(s_0)\ne0\).

The coefficients of \(B(e^h,e^{hs_0},Z)\) remain bounded near \(h=0\). Substitution of \(a_N(q_N^{s_0})=1+O_L(N^{-L})\) changes (10) by a quantity smaller than every power of \(h\), whereas (10) itself has nonzero leading term \(h^r b_r(s_0)\). This contradicts its asserted zero for an unbounded sequence of levels with \(a_N\not\equiv1\). The theorem follows.

The conclusion is centrality at the roots, not \(g_N=1\). The explicit multiplier (1) is consistent with it, since its shift ratio is already identically one. The theorem also needs asymptotics on the shifted region. A disk too small to compare \(s\) and \(s+1\) does not supply (7) from (6).

If several fixed algebraic relations cover finitely many residue classes or branches, apply the argument separately. Finitely many exceptional levels at which all coefficients of a cleared relation vanish do not matter. No numerical growth estimate for \(g_N\) substitutes for the fixed algebraic relation in (8).

## 3. Application boundary

The actual finite source, its fixed pointing, and a selected relative lattice contain more information than the formal microscopic series. Equations (1)--(5) deliberately do not preserve that full source. Conversely, the algebraic shift-ratio hypothesis (8) has not been proved for the quotient of the actual selected state and a geometric normal block; supplying it without an independent construction would hide the missing comparison in the assumptions.

The filtered-action argument in the separate all-order report follows a different route. It derives a source-selected analytic phase from the exact packet, proves its degree filtration, uses the actual operator on all needed shifted charts, and extracts its classical characteristic. The flat central example does not obstruct this route. Identifying that characteristic with the geometric A-curve still requires the marked nonparabolic source-to-representation adapter described there.
