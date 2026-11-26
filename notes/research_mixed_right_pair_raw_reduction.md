# Reducing every real right-hand row to a concave half-row support

Research proof, 4 November 2026. This note preserves every original finite row. It gives a source-side reduction and the exact two-block tangent cancellation; it does not assert a uniform geometric gap for right-region stars.

Use the normalized primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad J(t)=\Re g(t),\qquad I(u,x)=J(x+u)-J(x),
\tag{1}
\]
where \(J\) is continuous and one-periodic on the real axis. In particular
\(J(1-t)=-J(t)\), \(J(0)=J(1/2)=0\), and \(J(t)<0\) for \(0<t<1/2\).
The original row-product upper estimate, uniform through zeros and the finite endpoint rows, is proved in [the boundary-strip note](research_mixed_boundary_strip_bounds.md).

## 1. The upper rows require no separate support grid

Let the right target satisfy \(x\in[1/2,1]\), and let its other real target be \(p\in(0,1/2)\). For indicators \(e,\alpha\in\{0,1\}\), define
\[
 R_{e\alpha}(u;x,p)=I(u,x)+I(u,p)-(2+e)J(u)-\frac\alpha2J(p).
\tag{2}
\]
The type-four half-weight at \(x\) has rate zero: \(\max\{-J(x),0\}=0\). All selected Fourier monomials have modulus one on these real targets. Thus (2) is the actual allocated raw-row envelope, irrespective of which ordered argument is the right target.

For each \(0\le u\le1\), the maximum of \(I(u,x)\) on the right semicircle occurs at \(x=1/2\) or \(x=1\). Indeed its derivative has the sign of
\[
 \sin^2\!\pi(x+u)-\sin^2\!\pi x
 =\sin\pi u\,\sin\pi(2x+u),
\tag{3}
\]
so there is just one interior minimum. The endpoint comparison gives
\[
 I(u,x)\le
 \begin{cases}
 J(u+1/2),&0\le u\le1/2,\\
 J(u),&1/2\le u\le1.
 \end{cases}
\tag{4}
\]
Zeros of a factor produce downward logarithmic singularities in the derivative, not omitted intervals; continuity of \(I\) includes them.

For an upper row set \(v=1-u\in[0,1/2]\). Equations (2) and (4) give
\[
 R_{e\alpha}(u;x,p)
 \le J(p-v)+(1+e)J(v)-(1+\alpha/2)J(p)
 \le J(p-v)+J(v)-(1+\alpha/2)J(p).
\tag{5}
\]
The last inequality uses \(J(v)\le0\), including both endpoints. The derivative of \(J(p-v)+J(v)\) has the sign of
\[
 \sin^2\pi v-\sin^2\pi(p-v)
 =\sin\pi p\,\sin\pi(2v-p).
\tag{6}
\]
It decreases to its unique minimum at \(v=p/2\), then increases. Its maximum on \([0,1/2]\) is consequently the larger of \(J(p)\) and \(J(p-1/2)=J(p+1/2)\). The second is positive and the first negative. Therefore every upper row is bounded by the single lower-row boundary value
\[
 R_{e\alpha}(u;x,p)
 \le J(p+1/2)-(1+\alpha/2)J(p)
 =R_{e\alpha}(1/2;1/2,p),\qquad u\ge1/2.
\tag{7}
\]
This includes the literal \(u=1\) limiting row. No high row is deleted and no oscillatory cancellation is used.

**Proposition 1.** For every real slope \(k\), every closed interval \(P\subset(0,1/2)\), and all the original type indicators,
\[
 \sup_{\substack{x\in[1/2,1],\ p\in P\\0\le u\le1}}
 \{R_{e\alpha}(u;x,p)-kp\}
 =S_{e\alpha,P}(k),
\quad
 S_{e\alpha,P}(k)=
 \max_{\substack{0\le u\le1/2\\p\in P}}
 \{J(u+1/2)+J(u+p)-(2+e)J(u)-(1+\alpha/2)J(p)-kp\}.
\tag{8}
\]
The reverse inequality follows by choosing the original angle \(x=1/2\). Thus this is an equality of complete raw envelopes, not merely a relaxed upper bound.

## 2. Concavity supplies certified supports without a target grid

The real triangle function
\(V(u,p)=J(u+p)-J(u)-J(p)\) is strictly concave on \(u,p>0,\ u+p<1\): the normalized negative Hessian has positive diagonal entries and determinant one, by the cotangent addition formula. The expression maximized in (8) equals
\[
 V(u,1/2)+V(u,p)-eJ(u)-\frac\alpha2J(p)-kp.
\tag{9}
\]
For \(0<u<1/2\) and \(p\in P\subset(0,1/2)\), all four terms are concave and the triangle term is strictly concave. A tangent at any rational interior trial point therefore bounds the whole closed rectangle, by continuity at \(u=0,1/2\). The trial point need not be stationary or even approximately optimal.

The checker uses \(P=[11/50,9/20]\), all four \((e,\alpha)\), and slopes \(k=-1/5+j/40\), \(j=0,\ldots,18\). At every grid value it evaluates the original primitive and both derivatives outward, then adds the exact maximum of the affine tangent on the target rectangle. These 76 rational upper bounds yield upper chords for every intervening slope because \(S\), as a supremum of affine functions of \(k\), is convex. There is no slope extrapolation.

For the complete finite products, the uniform row bound gives the corresponding exponential rate (8), multiplied by a fixed power of \(N\). The true Fourier-polynomial bound on the right semicircle has upper rate zero; using its uniform absolute theorem with any fixed positive tolerance gives a bound with rate \(S+\delta\) for every \(\delta>0\). At \(p\in P\), its half-weight comparison is relative. This statement is uniform at product zeros, the real seam, and both parities. It is an upper bound only, and includes every selected real Fourier monomial.

## 3. Exact cancellation for two incident blocks

Let \(a,b,c\) be consecutive outer coordinates at an actual zero-lift cyclic critical point, with type indicators \(\alpha,\beta,\gamma\). Denote their original allocated phases by \(\phi_{\alpha\beta}(a,b)\) and \(\phi_{\beta\gamma}(b,c)\). Original critical stationarity gives
\[
 \phi_{\alpha\beta,b}+\phi_{\beta\gamma,a}=0.
\tag{10}
\]
Hence the sum of their full complex tangent planes at the real targets \((p,x,q)\) is exactly
\[
 C+P_Lp+P_Rq,
\quad C=\phi_{\alpha\beta}+\phi_{\beta\gamma}-P_La-P_Rc,
\quad P_L=\phi_{\alpha\beta,a},\quad P_R=\phi_{\beta\gamma,b}.
\tag{11}
\]
It has no dependence on the right target \(x\), including the displacement from the nonreal reference \(b\). This uses the complex stationarity equation, not only its real part.

By Proposition 1 the full two-row raw source defect is at most
\[
 S_{\beta\alpha,P}(\Re P_L)+S_{\gamma\gamma,P}(\Re P_R)-\Re C.
\tag{12}
\]
The common maximizing right angle is \(x=1/2\), so replacing the common angle by two independent optimizations loses nothing at this envelope level. The center type-four half-weights combine to a full weight of rate zero on the real right semicircle.

For an isolated right target, the adjacent two plateau blocks reset respectively their second and first height. The [oriented reset theorem](research_mixed_oriented_height_reset.md) gives the sufficient total debit
\[
 \frac{151}{20}(\Im a)^2+\frac{11}{2}(\Im c)^2.
\tag{13}
\]
The negative of (12), compared against (13), is an exact remaining correlated-reference question. Independent reference rectangles are not substituted for the original cyclic equations. No sign for this comparison is asserted here. In particular this note does not promote floating word tests to an arbitrary-word star or cycle theorem.

```sh
python3 experiments/check_mixed_right_pair_raw_reduction.py
```
