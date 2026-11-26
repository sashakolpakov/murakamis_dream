# Two type-four height changes with the same sign

Research proof, 4 November 2026. This is a cone estimate for the original
allocated type-four/type-four conditional phase. Both real coordinates
may change freely; the restriction is on the signs of the two height
changes.

On the proved full-source product
\[
 U_4^2,\qquad U_4=[.22,.50]+i[-.057,0],
 \qquad \phi_{11}''=-A+iB,\quad K=A+BA^{-1}B,            \tag{1}
\]
retain the original logarithmic lift and additive constant. The
[oriented reset theorem](research_mixed_oriented_height_reset.md)
proves \(A>0\), \(K_{00}<11\), and \(K_{11}<151/10\).

**Theorem 1.** For all real vectors \(u,v\in\mathbb R^2\) with
\(v_0v_1\ge0\), throughout \(U_4^2\),
\[
 \Re\{(u+iv)^T\phi_{11}''(u+iv)\}
                  \le11v_0^2+\frac{151}{10}v_1^2.      \tag{2}
\]
Consequently, if \(r,z\in U_4^2\) and
\((\Im z_0-\Im r_0)(\Im z_1-\Im r_1)\ge0\), then
\[
 \Re\{\phi_{11}(z)-\phi_{11}(r)-\phi_{11}'(r)\cdot(z-r)\}
 \le\frac{11}{2}(\Im z_0-\Im r_0)^2
       +\frac{151}{20}(\Im z_1-\Im r_1)^2.             \tag{3}
\]
In particular, resetting both negative reference heights to zero costs
at most \((11/2)(\Im r_0)^2+(151/20)(\Im r_1)^2\), with both
real target coordinates arbitrary in \([.22,.50]\).

The new outward check proves \(K_{01}<0\) on all sixteen products
of boundary sides of \(U_4^2\). With
\(A=\left(\begin{smallmatrix}a&c\\c&d\end{smallmatrix}\right)\)
and \(B=\left(\begin{smallmatrix}e&f\\f&g\end{smallmatrix}\right)\),
it uses the exact formula
\[
 K_{01}=c+\frac{def-c(eg+f^2)+afg}{ad-c^2}.             \tag{4}
\]
The complete saved type-four/type-four cover of the oriented theorem
is replayed. Every affine Newton witness is checked against the
original logarithmic equation; every accepted edge product has an
exact prefix-disjoint dyadic cover of area one. The diagonal bounds
and positivity of \(A\) are rechecked as well. No floating sample
enters acceptance.

On these boundary products, completing the real square gives
\[
 \Re\{(u+iv)^T\phi''(u+iv)\}
 =-(u+A^{-1}Bv)^TA(u+A^{-1}Bv)+v^TKv.
                                                               \tag{5}
\]
The off-diagonal term \(2K_{01}v_0v_1\) is nonpositive, proving
(2) on the boundary for each fixed \(u,v\) in the indicated cone.
For that fixed pair, the left side is harmonic in each original
complex parameter. Successive maximum principles give (2) on the
whole product. This does not apply a maximum principle to \(K_{01}\)
and does not assert \(K\le\operatorname{diag}(11,151/10)\) on
all real directions. Integrating the exact Taylor remainder along
the straight segment gives (3).

The existing original conditional packet and true Fourier-weight
upper bound convert (3) into a finite-block upper rate with any
fixed positive exponential tolerance, including the endpoint
\(\Re z_j=.50\). On compact subsets with real parts below one half,
the unselected Fourier comparison is relative. Selection at a reset
real coordinate has modulus one. No assertion is made here for a
selected coordinate whose target height remains nonzero. This
result alone supplies no right-region source gap or cyclic
contribution bound.

```sh
python3 experiments/certify_mixed_same_sign_height_reset.py --precision 256
python3 experiments/certify_mixed_same_sign_height_reset.py --precision 320 --input repro/results/research-mixed-same-sign-height-reset.json --output /tmp/research-mixed-same-sign-height-reset-review.json
```
