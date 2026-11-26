# Orientation-dependent costs for resetting one outer height

Research proof, 4 November 2026. The outward certificate passes all 64 boundary products on 74,677 cells; earlier source artifacts remain unchanged.

The original allocated conditional phase \(\phi_{\eta\epsilon}(a,b)\), with its zero logarithmic lift and additive constant, is the one in [the full height-reset theorem](research_mixed_full_height_reset.md). Its complete finite-source packet is available on
\[
 U_3=[.22,.50]+i[-.03,.02],\qquad U_4=[.22,.50]+i[-.057,0].
\tag{1}
\]
Write \(\phi''=-A+iB\), where \(A,B\) are real symmetric. The earlier theorem proves \(A>0\). Let
\[
 K=A+BA^{-1}B.
\tag{2}
\]
The new certificate proves the sharper diagonal bounds
\[
 K_{00}<11,\qquad K_{11}<151/10.
\tag{3}
\]
These concern the ordered arguments of the original chirped phase. They do not assert the matrix inequality \(K<\operatorname{diag}(11,151/10)\).

For a complex displacement \(w=u+iv\), completion of the real square gives the exact identity
\[
 \Re(w^T\phi''w)
 =-(u+A^{-1}Bv)^TA(u+A^{-1}Bv)+v^TKv.
\tag{4}
\]
If only the first height changes, (3) therefore gives \(\Re(w^T\phi''w)<11v_0^2\), while only changing the second gives the bound \((151/10)v_1^2\). Both real components of \(u\) remain arbitrary.

It suffices to certify these inequalities on products of rectangle sides. For each fixed real \(u\) and each one-coordinate \(v\), the left side of (4) is harmonic in each complex parameter. Successive maximum principles extend its quadratic upper bound throughout the full product. This applies the maximum principle to the holomorphic Hessian quadratic form, not to \(K_{jj}\). The source theorem supplies the holomorphic phase on a neighborhood of the closed product.

Let \(r\) be a reference in the original typed rectangles, and let \(z\in U_{3+\eta}\times U_{3+\epsilon}\) have arbitrary real coordinates, with precisely one height changed from its reference value. Put \(\Gamma_r(z)=\phi(r)+\phi'(r)\cdot(z-r)\). Integrating (4) on the straight segment gives
\[
 \Re\{\phi(z)-\Gamma_r(z)\}
 \le
 \begin{cases}
 (11/2)(\Im z_0-\Im r_0)^2,&\Im z_1=\Im r_1,\\
 (151/20)(\Im z_1-\Im r_1)^2,&\Im z_0=\Im r_0.
 \end{cases}
\tag{5}
\]
When the changed height is reset to zero, the respective costs are \((11/2)(\Im r_0)^2\) and \((151/20)(\Im r_1)^2\). The full finite block has the same upper rate, with any fixed positive exponential tolerance, from its original packet and the true Fourier upper bound. On real-coordinate compact subsets of \((0,1/2)\), the unselected Fourier comparison is relative and no positive exponential tolerance is needed. Selection at the reset real coordinate has modulus one. Selection at the unchanged complex coordinate is not included.

The certificate starts from the already checked full-matrix cover, independently rechecks each affine Newton self-map, and subdivides when the diagonal tests require it. The formulas tested are, with
\(A=\left(\begin{smallmatrix}a&c\\c&d\end{smallmatrix}\right)\) and
\(B=\left(\begin{smallmatrix}e&f\\f&g\end{smallmatrix}\right)\),
\[
 K_{00}=a+\frac{de^2-2cef+af^2}{ad-c^2},\qquad
 K_{11}=d+\frac{df^2-2cfg+ag^2}{ad-c^2}.
\tag{6}
\]
All 64 ordered typed boundary products are covered exactly. Source, original cover, helper, proof and script hashes are bound and checked for immutability.

This is a local reset estimate. A two-incident-block or four-block right-region theorem still requires a separate comparison of its original raw rows against the correlated geometric supporting planes. No such reserve, all-word source bound, or volume conclusion follows from (5) alone.

```sh
python3 experiments/certify_mixed_oriented_height_reset.py --precision 256
python3 experiments/certify_mixed_oriented_height_reset.py --precision 320 --input repro/results/research-mixed-oriented-height-reset.json --output /tmp/research-mixed-oriented-height-reset-review.json
```
