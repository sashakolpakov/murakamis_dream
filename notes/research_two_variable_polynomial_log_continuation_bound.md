# A product-contour bound for two-variable polynomial-log densities

Private written proof, 18 November 2026.

For a rational-plus-logarithmic density with the three specified
divisors below, an initial product-contour bound propagates to every
fixed continued compact with an exponential cost in the numerator
degrees and divisor orders. The proof recovers both polynomial
numerators on the initial contour before continuing either variable.
It therefore introduces no artificial singularity when the moving
endpoint meets zero at \(w=1\).

This is a function-class theorem. Membership of the full marked
source in this bounded-complexity class is a separate source calculation.

## 1. Precise class and quantitative statement

Fix \(\sigma\in\mathbb C\setminus\{0\}\), and put
\[
                 a(w)=\frac{1-w}{2\sigma},\qquad
                 \mathcal L(w,\theta)
                         =\log\!\left(1-\frac{a(w)}{\theta}\right).
 \tag{1}
\]
The initial logarithm is its series at large \(\theta\).
Choose
\[
 0<\varepsilon<1,\qquad
 a_0=\frac{\varepsilon}{2|\sigma|},\qquad R>a_0,
 \qquad
 \mathbb T=\{|w-1|=\varepsilon,\ |\theta|=R\}.
 \tag{2}
\]
The series
\(\mathcal L=-\sum_{m\ge1}a(w)^m/(m\theta^m)\)
converges uniformly on this product contour and fixes its branch.

Let
\[
 F(w,\theta)=
 \frac{A(w,\theta)+B(w,\theta)\mathcal L(w,\theta)}
 {w^{r_w}\theta^{r_0}(\theta-a(w))^{r_a}},
 \qquad r_w,r_0,r_a\in\mathbb Z_{\ge0}.
 \tag{3}
\]
The numerator polynomials have degree at most \(d\) in each variable
separately. A total-degree bound of \(d\) is sufficient but not required.
Zero polynomials and zero divisor orders are allowed.
Two different rational coefficients multiplying \(1\) and
\(\mathcal L\) can first be put over their common displayed denominator.

Let \(K\) be a compact on a specified continuation cover of
\[
 \{(w,\theta):w\theta(\theta-a(w))\ne0\}.
 \tag{4}
\]
Its logarithm is continued from (2) along the prescribed paths.
Define
\[
 \begin{split}
 M&=\sup_{\mathbb T}|F|,\qquad
 \lambda_0=-\log(1-a_0/R),\\
 H_0&=2^{11}(R/a_0)\max(1,a_0^{-1}),\\
 C_0&=2H_0\max(1,R)(1+\lambda_0),\\
 q_w&=\max(1,\sup_K|w-1|/\varepsilon),\qquad
 q_\theta=\max(1,\sup_K|\theta|/R),\\
 \delta_w&=\inf_K|w|>0,\qquad
 \delta_0=\inf_K|\theta|>0,\qquad
 \delta_a=\inf_K|\theta-a(w)|>0,\qquad
 L_K=\sup_K|\mathcal L|<\infty .
 \end{split}
 \tag{5}
\]
The suprema of coordinates refer to the projection of the compact.

**Theorem.** With \(n=d+1\),
\[
 \boxed{\displaystyle
 \sup_K|F|
 \le M(1+L_K)(4C_0q_wq_\theta)^n
    \left(\frac{1+\varepsilon}{\delta_w}\right)^{r_w}
    \left(\frac R{\delta_0}\right)^{r_0}
    \left(\frac{R+a_0}{\delta_a}\right)^{r_a}.}
 \tag{6}
\]
In particular the cost is exponential in \(d+r_w+r_0+r_a+1\)
for fixed contour and continued compact. No separate bound on the
density, endpoint coefficients, or either numerator is assumed.
Cancellation between the rational and logarithmic terms is included.

## 2. The finite inverse estimate used in the recovery

For \(N\ge1\), the Hilbert matrix
\[
                 H_{ij}=\frac1{i+j+1},\qquad 0\le i,j<N,
 \tag{7}
\]
has
\[
 (H^{-1})_{jm}
 =(-1)^{j+m}(j+m+1)
   \binom{N+j}{N-m-1}\binom{N+m}{N-j-1}
   \binom{j+m}{j}^{\!2}.
 \tag{8}
\]
Here is a finite proof of the formula and the bound we need.
Set
\[
 D(z)=\prod_{j=0}^{N-1}(z+j+1),\qquad
 \Lambda_m(z)=
       \prod_{\substack{0\le i<N\\i\ne m}}\frac{z-i}{m-i}.
 \tag{9}
\]
The rational function \(D(m)\Lambda_m(z)/D(z)\) equals
\(\mathbf1_{i=m}\) at \(z=i\). Its residue at \(-j-1\) is
the \(j\)-th coefficient of the partial fraction solution of
\(Hb=e_m\). Taking that residue gives (8). Equivalently its magnitude is
\[
 \frac{(N+m)!(N+j)!}
 {(m!)^2(j!)^2(N-1-m)!(N-1-j)!(j+m+1)} .
 \tag{10}
\]
Each binomial coefficient is at most the corresponding power of two.
Thus an entry of (8) is at most \(2N\,2^{8N}\), and a row sum is
at most \(2N^2\,2^{8N}\le2^{11N}\). Consequently
\[
                         \|H^{-1}\|_{\infty\to\infty}
                                  \le2^{11N}.
 \tag{11}
\]
The factorials were combined into binomial coefficients before
estimating them. There is no \(N^{cN}\) loss.

## 3. Recover the logarithmic numerator on the original circle

Clear the exact denominator in (3), writing
\[
 \begin{split}
 G(w,\theta)&=A(w,\theta)+B(w,\theta)\mathcal L(w,\theta),\\
 M_0&=M(1+\varepsilon)^{r_w}R^{r_0}(R+a_0)^{r_a}.
 \end{split}
 \tag{12}
\]
Then \(\sup_{\mathbb T}|G|\le M_0\).
Expand
\[
                  B(w,\theta)=\sum_{j=0}^d b_j(w)\theta^j.
 \tag{13}
\]
For fixed \(w\) on \(|w-1|=\varepsilon\), the endpoint \(a=a(w)\)
has modulus exactly \(a_0>0\). The negative Laurent coefficients
of \(G\) in \(\theta\) are therefore
\[
 \begin{split}
 c_m(w)&=\frac1{2\pi i}\int_{|\theta|=R}
                                  G(w,\theta)\theta^{m-1}\,d\theta,\\
 c_m(w)&=-a^m\sum_{j=0}^d\frac{a^j b_j(w)}{m+j},\qquad m\ge1,\\
 |c_m(w)|&\le M_0R^m.
 \end{split}
 \tag{14}
\]
The polynomial \(A\) contributes no negative powers.
Use only \(m=1,\ldots,n=d+1\). With unknowns \(a^j b_j(w)\),
this is (7), with right side \(-c_{i+1}(w)/a^{i+1}\).
Since \(R/a_0>1\), (11) gives
\[
 \begin{split}
 \max_j|a^j b_j(w)|
      &\le2^{11n}M_0(R/a_0)^n,\\
 \max_j|b_j(w)|
      &\le M_0 H_0^n.
 \end{split}
 \tag{15}
\]
The second inequality uses
\(a_0^{-j}\le\max(1,a_0^{-1})^n\).
These bounds are uniform on the entire initial \(w\)-circle;
no continuation in \(w\) has yet been used.

On the \(\theta\)-circle, \(n\le2^n\) and (15) imply
\[
 \sup_{\mathbb T}|B|
 \le n M_0H_0^n\max(1,R)^d
 \le M_0[2H_0\max(1,R)]^n .
 \tag{16}
\]
The original logarithm has \(\sup_{\mathbb T}|\mathcal L|\le\lambda_0\).
Subtract \(B\mathcal L\) from \(G\). The definition of \(C_0\) then gives
\[
                         \sup_{\mathbb T}|A|,\ 
                         \sup_{\mathbb T}|B|\le M_0 C_0^n.
 \tag{17}
\]
In particular this recovery is injective even if the original
two summands nearly cancel. If \(M=0\), (14)--(15) first give
\(B=0\) on the product contour and hence as a polynomial, and
then \(A=0\).

## 4. Continue the recovered polynomials jointly

For either polynomial \(V=A,B\), expand around \(w=1,\theta=0\):
\[
                 V(w,\theta)=
                 \sum_{i,j=0}^d v_{ij}(w-1)^i\theta^j.
 \tag{18}
\]
Two successive Cauchy coefficient integrals on the same product
contour give
\[
                 |v_{ij}|\le M_0 C_0^n\varepsilon^{-i}R^{-j}.
 \tag{19}
\]
Thus
\[
 \sup_K|V|
 \le n^2 M_0C_0^n q_w^d q_\theta^d
 \le M_0(4C_0q_wq_\theta)^n .
 \tag{20}
\]
Both numerator polynomials are single valued. The logarithm alone
retains the chosen continuation label, whose size is bounded by
\(L_K\). Dividing by the three exact factors in (3) proves (6).

This argument includes target points with \(w=1\), provided
\(\theta\ne0\). At those points \(a(w)=0\), but none of the three
allowed divisors is crossed. We divided by \(a(w)\) only on the
original circle, where its modulus is the fixed positive \(a_0\).
We did not use a parameter-dependent one-variable estimate at the
target. On a returned logarithmic sheet the value at \(a=0\) may be
a nonzero integer multiple of \(2\pi i\); it is still included in \(L_K\).

## 5. Exponential families and uniform continued charts

Suppose \(F_k\) has the displayed form with
\[
 d_k+r_{w,k}+r_{0,k}+r_{a,k}+1\le C_1(k+1),\qquad
                       \sup_{\mathbb T}|F_k|\le M A_1^k,
 \tag{21}
\]
where \(A_1>0\) and the fixed data do not depend on \(k\).
Set
\[
 C_*=\max\left(
  1,\ 4C_0q_wq_\theta,\ 
  \frac{1+\varepsilon}{\delta_w},
  \frac R{\delta_0},\ \frac{R+a_0}{\delta_a}\right).
 \tag{22}
\]
Equation (6) gives the explicit bound
\[
                  \sup_K|F_k|
   \le M(1+L_K)C_*^{C_1}(A_1 C_*^{C_1})^k .
 \tag{23}
\]
On a compact neighborhood of \(K\) in the chosen continuation
cover, the same constants can be enlarged once. Consequently
\(\sum_k z^kF_k(w,\theta)\) converges normally for a positive
\(z\)-radius there. This proves joint holomorphy of that continued
sum and agreement with the initial sum, wherever the latter was
already defined.

All constants are uniform over compact parameter sets on which
\(\sigma\ne0\), \(0<\varepsilon<1\), \(R-a_0>0\) stay uniformly
separated from their excluded values, the target coordinates stay
bounded, the three divisor distances stay positive, and the
continued logarithms stay bounded. They are not asserted uniform
over all winding numbers or when one of the specified divisors is
approached.

The bound uses degrees and pole orders of the whole cleared
representation. It does not require termwise estimates for a
particular decomposition, and it retains every logarithmic sheet
and connector. It proves no statement that the actual full-clock
source has this representation, no localization of its spectral
cycle, and no geometric or physical scalar lower bound.

## 6. Proof provenance

The proof is self-contained. The finite Hilbert inverse is derived
in (7)--(11), the moving-endpoint moment normalization is explicit
in (14), and all continuation estimates follow from the two
polynomial coefficient integrals.

The entire earlier note
notes/research_polynomial_log_cauchy_continuation_bound.md
was read for coverage. It treats one fixed endpoint parameter by
the same Hilbert recovery. The present product-contour argument
recovers polynomial dependence on the endpoint parameter itself,
and so also covers its collision with zero at target points.
No estimate or source theorem not proved above is a premise.

Only written mathematics and text/hash operations were used.
Frozen proofs and public manuscripts are unchanged.
