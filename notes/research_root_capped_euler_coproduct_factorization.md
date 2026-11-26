# Exponentially small root carries in an actual Euler coproduct

Private written proof, 18 November 2026.

The finite Euler polynomial of the actual total lowering operator
factors, up to an exponentially small operator carry, into a reversed
ordered product of the finite one-head coproduct factors. The
agreement below total degree \(N\) is exact. The carry is bounded
before any coherent evaluation and remains exponentially small after
multiplication by either actual operator inverse.

The estimates hold in the original binomial metric, including a
genuine complex meridian collar and its fixed derivatives. On any
fixed compact coherent chart away from incidence, shrinking the
activity disk makes the carry beat the exact conditioning cost of
coherent evaluation. This does not prove a nonzero phase for the
individual factors or for their product.

The complete directs C and J are pinned below. C supplies the
finite logarithm estimate; J supplies the actual ordered coproduct
and source conventions. The factorization, norm estimates, and
coherent comparison are proved here.

## 1. Actual finite operators and the required order

Fix \(r\ge1\) heads and
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 f_n=\prod_{j=1}^n(1-Q^j),\quad f_0=1.
 \tag{1}
\]
The quantum root remains fixed. Each head has the original metric
\[
                    \|w_a\|^2=\binom da^{-1}.
 \tag{2}
\]
At common meridian \(M\ne0\), the actual matrices are
\[
 E(M)w_a=(MQ^{-a}-M^{-1})w_{a-1}\quad(a>0),\quad E(M)w_0=0,
 \qquad K(M)w_a=-M q^{-1}Q^{-a}w_a.
 \tag{3}
\]
All tensor metrics are products of (2). Define
\[
 X_i(M)=E_i(M)\prod_{j>i}K_j(M),\qquad
 X(M)=\sum_{i=1}^rX_i(M)=E_{\rm tot}(M).
 \tag{4}
\]
These are exactly J's ordered lowering coproduct terms, with all
Cartan factors present.

Since \(KE=QEK\), one has
\[
 X_iX_j=QX_jX_i\quad(i<j),\qquad X_i^N=0,\qquad X^N=0.
 \tag{5}
\]
For the last identity, the finite binomial formula has zero
intermediate coefficients in degree \(N\): its numerator contains
\(1-Q^N\), whereas its denominators in the intermediate terms
contain only \(1-Q^j\), \(0<j<N\). Induction over the heads proves
the assertion. These are whole-meridian finite-matrix identities.

Write
\[
 E_N(t)=\sum_{n=0}^{d}\frac{t^n}{f_n},\qquad
 \mathcal G_N(t,M)=E_N(tX(M)),\qquad
 \mathcal P_N(t,M)=E_N(tX_r(M))\cdots E_N(tX_1(M)).
 \tag{6}
\]
The order in \(\mathcal P_N\) is decreasing head index.
For \(n<N\), the finite binomial identity gives
\[
 \frac{X^n}{f_n}
 =\sum_{n_1+\cdots+n_r=n}
       \frac{X_r^{n_r}\cdots X_1^{n_1}}
            {f_{n_r}\cdots f_{n_1}}.
 \tag{7}
\]
One elementary proof for two terms with \(AB=QBA\) is to
expand \((A+B)^n\) in the order \(B^bA^a\).
Multiplication by \(A+B\) gives the finite Gaussian-binomial
recurrence, with coefficient \(f_n/(f_af_b)\).
All denominators are nonzero for \(n<N\). Iteration gives (7).

Thus
\[
 \boxed{\quad
 \mathcal G_N=[\mathcal P_N]_{<N},\qquad
 \mathcal C_N:=\mathcal P_N-\mathcal G_N
                    =\sum_{n=N}^{rd}P_{N,n}(M)t^n .
 \quad}\tag{8}
\]
For \(r=1\) this carry is zero. For more heads it is retained
as the specified finite polynomial. No exact generic-parameter
infinite-product factorization has been specialized through a
root singularity.

## 2. Exact finite logarithms and both inverses

Set
\[
 L_N(t)=\sum_{j=1}^{d}\frac{t^j}{j(1-Q^j)}.
 \tag{9}
\]
C proves directly from the coefficient recurrence that
\(E_N\) is the degree-\(d\) Taylor polynomial of \(\exp L_N\).
It follows, for every actual matrix \(Y\) with \(Y^N=0\), that
\[
 \boxed{\quad
 E_N(tY)=\exp L_N(tY),\qquad
 E_N(tY)^{-1}=\exp[-L_N(tY)] .
 \quad}\tag{10}
\]
These are exact matrix identities for every \(t\), not small-\(t\)
asymptotics. Terms of degree at least \(N\) vanish because they
contain \(Y^N\). In particular both matrices in (6) are invertible
for all \(t\). The inverse of the product has the reversed
factor order.

There is an absolute \(C>0\) such that
\[
 \|L_N(tY)\|\le CN|t|\,\|Y\|,
                       \qquad |t|\,\|Y\|\le1/4.
 \tag{11}
\]
For clarity this does not require a spectral norm equality.
Bound the sum in (9) by
\(\sum_j(|t|\|Y\|)^j/[j|1-Q^j|]\).
The elementary sine inequality
\[
                 |1-Q^j|\ge4\min(j,N-j)/N
\]
bounds the terms \(j\le N/2\) by
\(N(|t|\|Y\|)^j/(4j^2)\). The upper half has a geometric
factor \((|t|\|Y\|)^{N/2}\) and a harmonic sum, uniformly
bounded by the right side of (11). This proves the estimate.
Consequently
\[
 \|E_N(tY)\|,\ \|E_N(tY)^{-1}\|
                         \le \exp(CN|t|\,\|Y\|).
 \tag{12}
\]
The inverse bound is essential to the relative carry estimate.

## 3. Original-metric bounds on a genuine meridian collar

At \(M=1\), the weighted lowering coefficient in (3) has norm
\[
 2\sin(\pi a/N)\sqrt{\frac{N-a}{a}}
                       \le 2\pi\sqrt{\frac aN(1-a/N)}\le\pi.
 \tag{13}
\]
Here \(1\le a\le d\); the forced bottom arrow is zero.
If \(Lw_a=w_{a-1}\) with its bottom zero, then
\[
 \|L\|=\sqrt d,\qquad
 E(M)=M E(1)+(M-M^{-1})L,\qquad
 \|K(M)\|=|M|.
 \tag{14}
\]
Thus no unscaled meridian disk with a uniform small-activity
domain is being assumed.

Fix \(\eta>0\) and use the actual complex collar
\[
                      M=\exp(u/\sqrt N),\qquad |u|\le\eta.
 \tag{15}
\]
Equations (13)--(14) give
\[
 \|E(M)\|\le \pi e^\eta+2\eta e^\eta,\qquad
 \|X_i(M)\|\le B,\qquad \|X(M)\|\le rB,
 \tag{16}
\]
where \(B=B(r,\eta)\) is independent of \(N\).
For example the first bound follows from
\(|M-M^{-1}|\le2|u|e^{|u|/\sqrt N}/\sqrt N\);
the remaining Cartan factors in (4) give a bounded factor
\(e^{r\eta}\). Their exact values have not been dropped.
The customary smaller collar \(M=\exp(v/N)\), with bounded
\(v\), is contained in (15) for large \(N\).

Choose \(R>0\) with \(RrB\le1/4\).
Equations (12),(16) imply, for \(|t|\le R\),
\[
 \begin{split}
 \|\mathcal G_N(t,M)\|,\ \|\mathcal G_N(t,M)^{-1}\|
                                        &\le e^{A N|t|},\\
 \|\mathcal P_N(t,M)\|,\ \|\mathcal P_N(t,M)^{-1}\|
                                        &\le e^{A N|t|},
 \end{split}\tag{17}
\]
with \(A=CrB\), enlarged if needed.
All matrices are holomorphic in \(t,u\) on a neighborhood of
each smaller closed bidisk.

## 4. The retained carry is exponentially small

On \(|t|=R\), (17) and the operator-valued Cauchy estimate give
\[
                         \|P_{N,n}(M)\|\le e^{ANR}R^{-n}.
\]
Apply this only to the actual high-degree coefficients in (8).
For \(0<\rho<1\) and \(|t|\le\rho R\),
\[
 \boxed{\quad
 \|\mathcal C_N(t,M)\|
       \le \frac{\rho^N}{1-\rho}e^{ANR}.
 \quad}\tag{18}
\]
Multiplication by either actual inverse in (17) gives the
two-sided relative bounds
\[
 \boxed{\begin{split}
 \|\mathcal G_N^{-1}\mathcal P_N-I\|,\
 \|\mathcal P_N\mathcal G_N^{-1}-I\|
 &\le \frac1{1-\rho}
       \exp\{N[\log\rho+AR(1+\rho)]\},\\
 \|\mathcal P_N^{-1}\mathcal G_N-I\|,\
 \|\mathcal G_N\mathcal P_N^{-1}-I\|
 &\le \frac1{1-\rho}
       \exp\{N[\log\rho+AR(1+\rho)]\}.
 \end{split}}\tag{19}
\]
No commuting of an inverse through the carry is used.

In particular, fixing a sufficiently small \(R\) and
\(\rho=1/2\) proves an exponentially small relative carry.
More generally, for any prescribed \(\Lambda>0\), one can
keep \(R\) fixed and choose \(\rho>0\) sufficiently small so
that all four relative errors and the absolute error in (18)
are \(O(e^{-\Lambda N})\). This gives a nonempty activity disk,
whose size is allowed to depend on \(\Lambda,r,\eta\).
It does not assert that a given geometric source point lies
inside that disk.

The same conclusions hold with all fixed \(t\)- and
\(u\)-derivatives on smaller bidisks. To see this, first choose
a slightly larger activity disk and a slightly larger collar
on which the desired exponential rate holds, then apply
Cauchy estimates to the exact holomorphic errors in (18)--(19).
In the original meridian variable this gives, for each fixed
\(j\), the corresponding bound with at most a factor
\(O(N^{j/2})\) for \(\partial_M^j\). Indeed
\(M\partial_M=\sqrt N\,\partial_u\), and \(M\) stays bounded
away from zero. These are genuine meridian derivatives of
the actual fixed-root matrices, not quantum-parameter
derivatives of a root identity.

## 5. Coherent evaluation and its explicit conditioning

Retain the exact original binomial kernels of J:
\[
 c(\mathbf z)=\bigotimes_i
             \sum_{a=0}^d\binom da z_i^aw_a,\qquad
 v(\mathbf w)=\bigotimes_i\sum_{a=0}^d w_i^aw_a^*,\qquad
 \sigma_N(B)=
   \frac{v(\mathbf w)B c(\mathbf z)}
        {\prod_i(1+w_i z_i)^d}.
 \tag{20}
\]
There is no change of metric or of the finite caps.
For any matrix \(B\), Cauchy--Schwarz in (2) gives
\[
 |\sigma_N(B)|
 \le \|B\|\prod_i
 \left[
 \frac{\sqrt{(1+|w_i|^2)(1+|z_i|^2)}}{|1+w_i z_i|}
 \right]^d.
 \tag{21}
\]
The bracket is projectively well defined and continuous off
the incidence divisor. For each fixed compact
\[
 \mathcal K\Subset
 \bigl((\mathbb P^1\times\mathbb P^1)
                     \setminus\{1+wz=0\}\bigr)^r
\]
there is therefore a finite \(\kappa_{\mathcal K}\ge0\) with
\[
             \sup_{\mathcal K}|\sigma_N(B)|
                             \le e^{\kappa_{\mathcal K}N}\|B\|.
 \tag{22}
\]
On the original real coherent cycle \(z_i=\bar w_i\) the
brackets are exactly one.

Given \(\mathcal K\) and \(\Lambda>0\), choose the activity
disk in (18)--(19) with rate larger than
\(\Lambda+\kappa_{\mathcal K}\). Then
\[
 \boxed{\quad
 \sup_{\mathcal K}
 |\sigma_N(\mathcal P_N-\mathcal G_N)|
                           =O(e^{-\Lambda N}).
 \quad}\tag{23}
\]
The same holds for the normalized kernels of each relative
operator error in (19). Every fixed coherent-coordinate
derivative has the same conclusion on smaller charts:
use (22) on slightly larger projective charts and apply
Cauchy estimates to the holomorphic normalized kernel.
The meridian-normal statement from §4 remains valid.

This is an absolute comparison after the stated identity-cap
normalization. It is not a relative scalar estimate obtained
by dividing by \(\sigma_N(\mathcal G_N)\), which may vanish.
In particular neither (19) nor (23) supplies a selected
coherent phase or a nonzero amplitude for the product factors.
A paired exterior remains an actual matrix or kernel; its
norm or conditioning must be included before (18) is used
inside the full source.

## 6. The fixed-denominator family and the original normal row

The theorem estimates precisely the family in (6):
\(E_N(tE_{\rm tot}(M))\), with the fixed denominators \(f_n\)
and all meridian dependence in the actual operators.
It retains the complete cap and uses no continuation of an
occupation index.

It does not replace a different coefficient family such as
\[
 \sum_{n=0}^d
       \frac{t^n E_{\rm tot}(M)^n}{(M^{-2}Q;Q)_n}.
 \tag{24}
\]
Although (24) agrees with \(\mathcal G_N\) at \(M=1\), its
meridian derivative also differentiates the denominator.
For example that extra coefficient at \(M=1\) is exactly
\[
 \left.\partial_M
 \frac{f_n}{(M^{-2}Q;Q)_n}\right|_{M=1}
                =-2\sum_{j=1}^n\frac{Q^j}{1-Q^j}.
 \tag{25}
\]
This finite normal insertion must be retained in any use of
the theorem for such a contracted source. No bound or
cancellation for its pairing with the quotient is supplied
by silently replacing (24) by (6).

Likewise no ordinary quantum-parameter normal follows by
differentiating (5), (7), or (10) away from the root.
The result is a controlled factorization of an actual finite
coproduct factor, with its carry and coherent conditioning
quantified. The quotient, turnover, all source coupons, and
relative-window defects of J remain in the full period.

## Complete proof directs

* C: notes/research_factorial_coupon_small_activity_saddle.md,
  SHA256 9ab9fef5bfab21872aa9c6ec72990e9695df24e5cfffddb02902aaced4e16465.
* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.

Both complete directs were freshly read nontruncated in this active
author sequence and retained unchanged. Every used implication was
checked. Only written mathematics and text/hash operations were used.
Frozen and public files were not changed.

