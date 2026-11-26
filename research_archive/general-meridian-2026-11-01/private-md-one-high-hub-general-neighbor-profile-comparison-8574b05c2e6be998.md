# A coupled profile comparison for one high incidence

Private derivation, 1 November 2026. This note concerns the original coupled action and a conditional source bound. It does not restore the false pointwise moving-to-complete tensor inequality.

## 1. Original profiles and the comparison principle

Let \(f_B\) be the complete positive coefficient profile of the unturned product of \(B\ge2\) ordinary rigid leaves. Their variable profile is
\[
 g(x)=J(2x)-4J(x),\qquad
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad G_0=g(1/4).
 \tag{1}
\]
Fixed additive constants can be restored on the corresponding branches throughout. Let \(A\) be an actual unturned product of two or more inputs of strict type L or A, with original optimized profile \(f_A\). The neighboring product may contain an arbitrarily large fixed tree and its own physical turns. The product-response theorem gives
\[
                         f_A'(b)\ge f_2'(b),\qquad 0<b<1.
 \tag{2}
\]
It retains the constants and the actual positive branch of the response equations. The proof is in `notes/actual_conway_unflagged_probe_geometry.md`, Appendix A: at the last gate \(B_i\le X\), so
\(Y^2=(B_1-B)(B_2-B)\le(X-B)^2\); hence \(X\ge X_2(B)\), and the logarithmic derivative is increasing in \(X\). No independent cap action is assigned to \(A\).

The actual complete contraction across one physical turn has coupled pressure
\[
 F_{B,A}=\max_{0\le b\le1}\{f_B(b)+f_A(b)\}.
 \tag{3}
\]
At a covariant incidence \(z\), each rooted ordinary output is \(1-z\). Thus if the central incidence is high, the neighboring output is \(v=1-z\le1/2\). Define the genuine two-product comparison
\[
                         F_{B,2}=\max_b\{f_B(b)+f_2(b)\}.
 \tag{4}
\]
The maximum in (4) occurs at a point \(b_*\ge1/2\): both derivatives are positive below half, since \(f_B'\ge f_2'>0\) there. At \(B=2\), symmetry gives \(b_*=1/2\); otherwise the strict derivative inequality puts it above half.

For any \(0\le v\le1/2\), integration of (2) from \(v\) to \(b_*\), followed by evaluation of (3) at this *same coupled state*, proves
\[
 \boxed{\quad
 F_{B,A}-f_A(v)\ \ge\ F_{B,2}-f_2(v).
 \quad}
 \tag{5}
\]
Closed endpoints follow by continuity. Every additive constant on \(A\) cancels in its left side. This is a comparison of actual boundary profiles relative to their prescribed boundary value. It is not a comparison of separately maximized branch norms.

## 2. What coefficient hypothesis permits a quantum conclusion

Suppose the central moving junction has \(B\) low incidences \(u_1,\ldots,u_B\) and one high incidence \(z\), with \(v=1-z\). The fixed-polynomial full-jet and Chebyshev-folding estimates give its absolute tensor rate at most \(\sum_i g(u_i)\). If its attached low rigid branches satisfy their original coefficient cones, their additional contribution is at most \(\sum_i g(u_i)\), with their constants retained.

To use the classical comparison, the actual neighboring branch must have a coefficient estimate at its prescribed output of the form
\[
 |[e_{\lfloor vd\rfloor}]A_{N,s}|
       \le \exp\{N(f_A(v)+o(1))\},
 \tag{6}
\]
with the appropriate actual rounding, full normals, and uniformity in the parameters under consideration. The existence of the old profile \(f_A\), or inequality (2), alone does not imply (6) for a moving subtree.

Under (6), the whole contribution at the prescribed central indices has rate
\[
                  2\sum_{i=1}^B g(u_i)+f_A(v),
 \tag{7}
\]
plus the explicitly retained central boundary constants. It follows from (5) that it is separated from the same original pressure whenever
\[
 \boxed{\quad
 F_{B,2}-f_2(v)-2\sum_{i=1}^B g(u_i)>0.
 \quad}
 \tag{8}
\]
This criterion depends only on the two genuine reference product profiles and the current labels. It is valid for every neighboring \(A\) satisfying the hypotheses; it is not a new valence-only test. A fixed positive margin persists on a closed neighborhood and after summing polynomially many label tuples.

For complete-admissible central tuples, every \(u_i\le v\). A more convenient, weaker sufficient condition is
\[
 F_{B,2}-f_2(v)-2B\,g\bigl(\min(v,1/4)\bigr)>0.
 \tag{9}
\]
No claim is made that (8) or (9) holds for every one-high tuple. A coarse spectral bound can fail to provide the required margin even when the actual contraction is smaller.

There is a useful class where (6) is already a direct exact source consequence. If the neighboring constant-quotient junction is the unturned product of \(K\ge2\) rigid coefficient-cone inputs, then at output \(v<1/2\) the complete positive Newton support forces every input index to be at most the output index. All contributing inputs are therefore low. Their actual coefficient bounds, the old positive multiplication coefficients, and its closed Laplace estimate give (6) with \(f_A=f_K\), including the sum of their constants. This is a whole positive product estimate at the actual boundary value. Its inputs may carry their independent physical colors and fixed half-twist signs through the established cones.

Thus (8) is an unconditional source criterion for the indicated sectors of the literal two-hub expression \(C(h^B T(h^K))\) in the type where the first junction is moving and the second constant. A more complicated neighboring moving subtree requires a separate proof of (6).

## 3. Uniform compensation of the valence-nine witness

The complete intrinsic product identity is
\[
 f_B(\beta_B)+g(\beta_B)=2BG_0,
                  \qquad \beta_B=\frac{\arctan B}{\pi}<\frac12.
 \tag{10}
\]
It follows either from the positive Newton evaluation or from the original \(X=1\) response \((B_{h^B},Y_{h^B})=(1/B,1/B)\). Since \(f_B\) is increasing below half, evaluating (3) at \(b=1/2\) gives the simpler lower witness
\[
 F_{B,A}\ge2BG_0-g(\beta_B)+f_A(1/2).
 \tag{11}
\]
For \(B=8\), \(v=u_i=1/5\), inequality (2) yields
\[
\begin{split}
 F_{8,A}-\{16g(1/5)+f_A(1/5)\}
 &\ge16\{G_0-g(1/5)\}\,-g(\beta_8)\\
 &\qquad+f_2(1/2)-f_2(1/5).
\end{split}
 \tag{12}
\]
The elementary estimates in `/private/tmp/md-valence-nine-coupled-two-leaf-compensation.md`, Section 4, are
\[
       g(\beta_8)<\frac14,
       \qquad f_2(1/2)-f_2(1/5)>\frac{131}{512}.
 \tag{13}
\]
For clarity, the first follows by integrating \(-\log\tan t\) to \(\arctan(1/8)<1/8\). The second integrates
\(f_2'(b)=2\log(2X_2(\cot\pi b)^2)\) on \([1/5,1/4]\) and \([1/4,1/3]\), using the right-endpoint bounds \(2+\sqrt3>7/2\) and \((4+\sqrt7)/3>11/5\). The positive logarithm series gives \(\log(7/2)>5/4\) and \(\log(11/5)>201/256\).

Therefore
\[
 \boxed{\quad
 F_{8,A}-\{16g(1/5)+f_A(1/5)\}
   >16\{G_0-g(1/5)\}+\frac3{512}>0.
 \quad}
 \tag{14}
\]
This is a general neighboring-profile inequality, uniform over all such profiles after their own constants are retained. With (6), it suppresses the exact family \(N=5a+1\), \(e_{4a}e_a^8\), and a fixed small neighborhood of its normalized labels. In particular it holds for every constant neighboring rigid product \(h^K\), \(K\ge2\), without a new calculation for each \(K\).

The pointwise trace counterexample remains valid. Its complete value at the same tuple is exponentially too small to dominate the deformation. What compensates it in (14) is the original neighboring profile evaluated in the same coupled maximum. No inference about a whole arbitrary bare component, a new filled invariant limit, or an unknown moving-subtree coefficient profile is made.
