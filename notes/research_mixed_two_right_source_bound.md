# A full-source bound when both outer angles are on the right

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This proves a geometric supporting-plane bound for the original finite
conditional kernel when both target angles lie in \([1/2,1]\) at height
zero. All rows and the true Fourier polynomial remain present. It disposes
of this exterior region, including wrapped terms; it does not dispose of
regions with only one right-half target.

## 1. Original source and reference plane

Use \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\[
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}(rX;r)_j(rY;r)_j}{P_j^{2+\epsilon}},
 \qquad
 \mathcal B_{\eta\epsilon,N}
 =|C_{\epsilon,N}(X,Y)|\,|d_N(X)|^{\eta/2}|d_N(Y)|^{\epsilon/2}.
 \tag{1}
\]
The original polynomial \(d_N\) interpolates \(1/P_j\) on the root grid.
The exponents \(\eta,\epsilon\in\{0,1\}\) specify the neighboring
and own types. The half powers in (1) are nonnegative modulus powers,
not holomorphic square roots.

For a three-block word \((e_0,e_1,e_2)\), let its selected open-window
solution be \((s_0,t_0,s_1,t_1,s_2,t_2)\), with the two external
parameters in their typed rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{2}
\]
This global holomorphic branch is supplied by the
[open-window theorem, Lemma 2](research_mixed_cyclic_critical_height_bounds.md#2-arbitrary-finite-open-windows-have-global-root-branches).
Put \(a=t_0,s=s_1,b=t_1\), \(\eta=e_0\), \(\epsilon=e_1\), and
\[
 \begin{split}
 F(s,a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias\\
 &\hspace{8mm}-(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \Phi(a,b)&=F(s_*(a,b),a,b),\qquad
 \Gamma_{x,y}=\Phi+\Phi_a(x-a)+\Phi_b(y-b),
 \end{split}
 \quad
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \tag{3}
\]
All lifts are the original zero lifts. The
[support-slope theorem](research_mixed_geometric_support_slopes.md)
gives \(-1/5<\Re\Phi_a,\Re\Phi_b<1/4\) on these entire
reference products. In particular the lower slope bound used below
holds before any source estimate is made.

**Theorem 1.** Uniformly on all these reference products, for
\(x,y\in[1/2,1]\), \(X=e^{-2\pi ix}\), \(Y=e^{-2\pi iy}\),
and both parities,
\[
 \mathcal B_{\eta\epsilon,N}(X,Y)
       \le C N^A\exp N\{\Re\Gamma_{x,y}-1/100\}.
 \tag{4}
\]
Any selected wrapped factor has modulus one here, so the same bound
includes every selection of the two type-four half-wraps. The constant
and polynomial power are uniform over the finite list of types.

## 2. Exact reduction to four corner-row maxima

The whole-product bound and the forced Fourier estimate in
[the right-half reduction](research_mixed_right_half_source_reduction.md)
give, with an arbitrarily small positive rate error, the upper exponent
\[
 \sup_{0\le u\le1}
     \{I_0(u,x)+I_0(u,y)-(2+\epsilon)J(u)\},
 \qquad J=\Re g.
 \tag{5}
\]
Both true Fourier weights have zero upper rate on this closed
half-period, including the seam. There is no discarded factorial
endpoint or assumed replacement of \(d_N\) in (5).

Let \(p,q\ge-1/5\) be the two real supporting slopes. The maximum
of (5) minus \(px+qy\) is attained with
\(x,y\in\{1/2,1\}\). Here is the argument including the mixed
candidate/endpoint case. For \(u\ge1/2\), both angular functions
are convex. For \(1/5\le u<1/2\), the slope bound excludes every
extra angular maximum. For \(u<1/5\), each extra maximum has gain
at most \(3(1/5-u)^2\) over its value at angle \(1/2\), by (14)
of the cited reduction.

Suppose a maximizing pair at such a row has \(k\ge1\) extra
candidates. Replace these by \(1/2\), leaving any other endpoint
unchanged. If \(m\) of the two resulting endpoints equal \(1/2\),
then \(m\ge k\), and its row-dependent part is
\[
 f_{m,\epsilon}(u)=mI_0(u,1/2)-(m+\epsilon)J(u),\qquad
 f_{m,\epsilon}''
   =-m\pi\tan\pi u-(m+\epsilon)\pi\cot\pi u\le-2m\pi.
 \tag{6}
\]
For \(m\ge1\), its derivative at \(1/5\) is positive. The worst
case is \(m=1,\epsilon=1\), where it is
\(\log(2\cos(\pi/5))-2\log(2\sin(\pi/5))>0\).
Moving the row to \(1/5\) therefore gains at least
\(m\pi(1/5-u)^2>3k(1/5-u)^2\). This absorbs all extra
candidates. In particular, one candidate paired with endpoint one
uses \(m=k=1\); two candidates use \(m=k=2\). Endpoint limits
cover the logarithmic zeros and the rows zero and one.

Define the six exact constants
\[
 c_{\epsilon,0}=\begin{cases}0,&\epsilon=0,\\-J(1/6),&\epsilon=1,
 \end{cases}
 \qquad
 c_{\epsilon,m}=mJ(1/2+u_{\epsilon,m})-(m+\epsilon)J(u_{\epsilon,m}),
 \quad m=1,2.
 \tag{7}
\]
For \(\epsilon=0\), both maximizing rows equal \(1/4\). For
\(\epsilon=1\), writing \(v=\sin(\pi u)\), the positive roots are
\[
 v^2=(\sqrt{17}-1)/8\quad(m=1),\qquad
 2v^3+v^2-1=0\quad(m=2),\qquad u=\arcsin(v)/\pi.
 \tag{8}
\]
Indeed the derivative equation is
\((2\cos\pi u)^m=(2\sin\pi u)^{m+\epsilon}\), with both sides
positive. Strict concavity in (6) gives the unique maximum on
\((0,1/2)\). There \(I_0(u,1/2)>0\) and \(J(u)<0\), so
\(f_{m,\epsilon}(u)>0\) for \(m\ge1\). On the upper half of the row interval,
\(f_{m,\epsilon}(1-u)=-f_{m,\epsilon}(u)\), so no larger value
occurs there. For \(m=0\), the maximum is the first part of (7).

Consequently the full scalar support function is exactly
\[
 \max\{c_{\epsilon,0}-p-q,
 c_{\epsilon,1}-p/2-q,
 c_{\epsilon,1}-p-q/2,
 c_{\epsilon,2}-(p+q)/2\}.
 \tag{9}
\]
This equality concerns the continuous upper envelope of the complete
finite sum; it is not an assertion about the value of that signed sum.

## 3. Outward comparison on the reference products

The certificate proves, for each of the four corners,
\[
       \Re\Gamma_{x,y}-c_{\epsilon,m}>1/50,
       \qquad m=\mathbf1_{x=1/2}+\mathbf1_{y=1/2}.
 \tag{10}
\]
There are eight internal words, four external type choices, and sixteen
products of external rectangle edges. The checker re-evaluates all
4,820 cells of the existing 512-product slope cover with the unchanged
six-variable affine Newton primitive. It checks exact coverage and
current input provenance. Floating root and derivative values remain
proposals; every acceptance uses outward arithmetic and the original
logarithmic equations.

For completeness, the source comparison uses a derivative enclosure,
not interval evaluation at a sampled root. Let \(\mathcal J\) be the
six-variable Jacobian, \(\mathcal E\) its external-parameter derivative,
and let \(Y,D\) be the fixed inverse and affine-response proposals in
an accepted witness. With its positive component radii \(r_i\), put
\[
 A=I-Y\mathcal J,\quad
 \rho=\max_i\sum_j|A_{ij}|r_j/r_i<1,\quad
 U=Y(\mathcal J D+\mathcal E).
 \tag{11}
\]
The true response satisfies
\[
 T=-\mathcal J^{-1}\mathcal E
   =D-\sum_{j=0}^4 A^jU-\mathcal R,\qquad
 |\mathcal R_{ik}|\le
 r_i\frac{\rho^5}{1-\rho}\max_j\frac{|U_{jk}|}{r_j}.
 \tag{12}
\]
This is a weighted Neumann-series bound. The already-verified self-map
implies the strict inequality in (11). The cancellation-sensitive
differences in the original witness enclose \(\mathcal J\),
\(\mathcal E\), and the residual in (11).

The conditional Hessian \(H=\Phi''\) is obtained by eliminating
the single stationary index \(s\). In particular, with
\(d=g''(s+a)+g''(s+b)-(2+\epsilon)g''(s)\),
\(U_a=g''(s+a)+2\pi i\), \(U_b=g''(s+b)\),
\[
 \begin{split}
 H_{aa}&=g''(s+a)-(1+\eta/2)g''(a)-U_a^2/d,\\
 H_{bb}&=g''(s+b)-(1+\epsilon/2)g''(b)-U_b^2/d,\\
 H_{ab}&=-U_aU_b/d.
 \end{split}
 \tag{13}
\]
Since the corner is fixed,
\(d\Gamma=(H(x-a,y-b)^T)_a\,da+
(H(x-a,y-b)^T)_b\,db\). Composing this identity with the two
selected rows of (12) gives the external derivatives of \(\Gamma\).
At every boundary-cell midpoint, a separate degenerate-parameter
Newton test encloses the true point value. The real mean-value
bound with those derivatives proves (10) throughout that cell.

Each \(\Gamma_{x,y}\) is holomorphic on its full external product.
Successive harmonic minimum principles therefore extend (10) from
the distinguished boundary to the whole product. The least certified
gap in the author cover exceeds \(0.036\); the proof uses only
the rational threshold \(1/50\). Equations (5) and (9), followed by
an arbitrarily small fixed error in the true Fourier upper rate,
give (4). All scalar products, half-weights, and original finite
normalizations have been retained.

## 4. The all-right cyclic region and the remaining scope

At an actual cyclic critical point, unroll three neighboring blocks,
including repeated incidences for cyclic lengths one and two. The
proved actual domains put both external legs in (2), and uniqueness
identifies the reference used above. Summing (3) over the cycle
cancels every linear term by the original stationary equations.
The constant sum is its original critical action \(M\).

Thus for every fixed cyclic word with \(m\) blocks, the absolute
integral over the region in which **all** outer angles lie in
\([1/2,1]\) at height zero is at most
\(\operatorname{poly}(N)e^{N(M-m/100)}\), for every wrapped subset.
The exact Fourier carriers contribute only the already-retained
polynomial level power, and the wraps have modulus one. This is
an upper bound for a specified full-source exterior region.
It is not a lower bound for the whole cycle. Regions with one
right-half neighbor and one left-half neighbor still require the
remaining scalar supporting-plane comparisons.

## 5. Reproduction

    python3 experiments/certify_mixed_two_right_source_bound.py --precision 256

The record includes all 512 boundary products, their exact dyadic
cover, all four corner comparisons, the algebraic maximizing-root
checks, and current proof/script/input hashes. The decimal summaries
are informational; all acceptance predicates use exact rational
thresholds and outward intervals.
