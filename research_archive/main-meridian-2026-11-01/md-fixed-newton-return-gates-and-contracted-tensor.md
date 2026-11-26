# Fixed-Newton return gates and the exact symmetric contraction

Private proof, 1 November 2026. No repository file is changed.

This report isolates the genuine change of multiplication after the moving Newton coordinates have been removed. It proves an exact return kernel, a polynomial bound for every one of its coefficients, and a strictly negative interior entropy. It also fixes the edge convention needed to use this kernel in a tree. None of these statements alone compares a whole return-containing contraction with the geometric action of the original strict tangle.

## 1. Fixed polynomial coordinates and the return quotient

Fix
\[
N\ge2,\quad d=N-1,\quad \theta=\pi/N,\quad
c_j=2\cos((2j+1)\theta),\quad
S_n=\prod_{r=1}^n2\sin(r\theta),\quad S_0=1.
\]
Put
\[
B_n(z)=\prod_{j=0}^{n-1}(c_j-z),\qquad e_n=B_n/S_n^2,
\qquad P_0(z)=\mathcal T_N(z)+2.
\]
Here \(\mathcal T_N(2\cos t)=2\cos Nt\). The actual same-color quotient at meridian displacement \(s\) has relation
\[
P_s=P_0+\Delta_s,\qquad \Delta_s=2\cos(2\pi s)-2.
\tag{1}
\]
The coefficients below are in the fixed basis \(e_0,\ldots,e_d\), not in the moving basis. All equalities are polynomial quotient equalities and therefore retain every repeated-node normal.

For canonical polynomials \(f,g\), one division gives
\[
fg=P_0Q+R,\qquad \deg R<N,\quad\deg Q\le N-2,
\qquad f*_sg=R-\Delta_sQ.
\tag{2}
\]
Thus the change of multiplication is affine in \(\Delta_s\). When \(i+j<N\), the product \(e_ie_j\) has degree less than \(N\), and its fixed-basis coefficients are exactly the positive complete coefficients. When \(i+j\ge N\), the complete product is divisible by \(P_0\).

Indeed \(c_{d-j}=c_j\), so
\[
B_iB_{N-i}=B_N=(-1)^NP_0.
\]
Assume \(i\ge j\) and set
\[
a=N-i,\quad b=N-j,\quad h=i+j-N=N-a-b\ge0.
\]
Then \(j\ge a\), and the return quotient is the ordinary polynomial
\[
Q_{ij}=\frac{e_ie_j}{P_0}
=\frac{(-1)^N}{S_i^2S_j^2}
       \prod_{r=a}^{j-1}(c_r-z).
\tag{3}
\]
Its degree is \(h\le N-2\). Consequently
\[
e_i*_se_j=-\Delta_sQ_{ij}.
\tag{4}
\]
This exact divisibility is special to the complete fixed basis. It is different from the nonzero first derivative of multiplication coefficients in moving coordinates.

## 2. An exact alternating Newton expansion

The quotient in (3) has the expansion
\[
\boxed{\quad
Q_{ij}=\sum_{k=0}^{h}(-1)^{N+h-k}\Lambda_{ijk}e_k,
\qquad
\Lambda_{ijk}=
\frac{S_hS_k}
 {S_iS_jS_{h-k}S_{a+k}S_{b+k}}>0.
\quad}
\tag{5}
\]
Every factorial in (5) has index between zero and \(d\).

Here is a direct derivation from the finite factorial connection. The interval polynomial in (3) is \(B_h(-a,z)\), since shifting the meridian parameter by \(-a\) changes \(c_r\) into \(c_{r+a}\). In the finite connection, take \(p=q^2\), initial parameter \(q p^a\), and target parameter \(q\). If \(m=h-k\), cancellation gives
\[
B_h(-a,z)=S_h^2\sum_{k=0}^h C_{hk}e_k,
\qquad
C_{hk}=(-1)^m
\frac{S_kS_jS_{j-k-1}}
 {S_hS_mS_{a+k}S_{a-1}}.
\tag{6}
\]
For completeness, the two finite Pochhammer products have indices
\(a+k+1,\ldots,a+h\) and \(a,\ldots,a+m-1\). Each factor
\(1-q^{2r}=-iq^r(2\sin r\theta)\). Their combined phase is
\((-1)^m q^{m(2a+h)}\). The connection prefactor and the Gaussian binomial have inverse phase \(q^{-m(2a+h)}\), leaving precisely \((-1)^m\). This argument includes \(m=0\) by empty products.

Use
\[
S_iS_{a-1}=N,\qquad S_{j-k-1}S_{b+k}=N.
\]
Substitution of (6) into (3) gives (5), including its sign and normalization. The finite connection is a polynomial identity; no division by a sampled Casimir difference is used.

The complete turn reverses the fixed basis, so
\[
T_0Q_{ij}=\sum_{k=0}^{h}(-1)^{N+h-k}\Lambda_{ijk}e_{d-k}.
\tag{7}
\]
The actual fixed-frame typed turn multiplies each displayed term by its retained Gaussian scalar and \(W_k(s)/H_N(s)\). These factors and their inverses are uniformly bounded on every fixed \(|s|\le R<1\). The alternating sum in (7) remains present.

## 3. Uniform polynomial size, including all endpoints

The individual positive numbers in (5) obey
\[
\Lambda_{ijk}\le C N^2
\tag{8}
\]
for one absolute constant, every level, and every admissible \(i,j,k\).

First,
\[
\Lambda_{ij0}=
\frac1{N^2(2\sin a\theta)(2\sin b\theta)}\le\frac1{16}.
\tag{9}
\]
For \(1\le k\le h\), the exact consecutive ratio is
\[
\frac{\Lambda_{ijk}}{\Lambda_{ij,k-1}}
=\frac{\sin(k\theta)\sin((a+b+k-1)\theta)}
 {\sin((a+k)\theta)\sin((b+k)\theta)}.
\tag{10}
\]
The elementary identity
\[
\sin((a+k)\theta)\sin((b+k)\theta)
-\sin(k\theta)\sin((a+b+k)\theta)
=\sin(a\theta)\sin(b\theta)>0
\tag{11}
\]
therefore implies, when \(k<h\),
\[
\Lambda_{ijk}
\le\Lambda_{ij0}
\frac{\sin((a+b)\theta)}{\sin((a+b+k)\theta)}
\le\frac N{32}.
\tag{12}
\]
The first inequality follows by multiplying (10) and telescoping the one-step sine shifts. At the final index, if \(h\ge1\), retain its last ratio separately:
\[
\Lambda_{ijh}
\le\Lambda_{ij0}
 \frac{\sin^2((a+b)\theta)}{\sin(a\theta)\sin(b\theta)}
\le\frac{N^2}{64}.
\tag{13}
\]
The case \(h=0\) is (9). We used only
\(\sin(r\theta)\ge\sin\theta\ge2/N\) for \(1\le r<N\).
Thus no endpoint can conceal an exponential factor.

This is a coefficient statement for the return quotient in fixed coordinates. It is not a bound for the positive Newton coefficient norm after all later operations: the basis element \(e_{d-k}\) itself can have exponential spectral size, and the alternating signs in (7) can matter.

## 4. The symmetric three-input tensor

Let the fixed closing functional be
\[
\begin{aligned}
\phi_s(F)&=(-1)^dN^2\operatorname{coeff}_{z^d}F.
\end{aligned}\tag{14}
\]
for the canonical representative modulo \(P_s\). At every \(s\),
\[
\phi_s(e_i*_se_j)=\delta_{i+j,d}.
\tag{15}
\]
For \(i+j<d\), this follows from degree. At \(i+j=d\), it uses
\(S_iS_j=N\). At \(i+j\ge N\), the return quotient has degree at most \(N-2\), so its top coefficient is zero. Thus the Frobenius metric is the same anti-diagonal matrix in these fixed coordinates.

Define the covariant, symmetric vertex tensor
\[
V_s(i,j,r)=\phi_s(e_i*_se_j*_se_r).
\tag{16}
\]
Its complete part is supported on
\[
i+j,\ i+r,\ j+r\le d,\qquad i+j+r\ge d,
\]
and there it is the known positive tensor
\[
V_0(i,j,r)=
\frac{S_{i+j}S_{i+r}S_{j+r}}
 {N S_iS_jS_r S_{i+j+r-d}}.
\tag{17}
\]
The only additional support is
\[
i+j,\ i+r,\ j+r\ge N,\qquad i+j+r\ge2N-1.
\tag{18}
\]
On (18),
\[
\boxed{\quad
V_s(i,j,r)
=-\Delta_s(-1)^{i+j+r-d}
\frac{S_{i+j-N}S_{i+r-N}S_{j+r-N}}
 {N S_iS_jS_r S_{i+j+r-2N+1}}.
\quad}
\tag{19}
\]
Elsewhere it is zero. To prove (19), use (5) and the metric (15): the sole coefficient selected is \(k=d-r\). The resulting expression is symmetric after the sine-product reflection. This also proves that the listed support is independent of which two inputs are multiplied first.

Equivalently, writing \(t=i+j+r-(2N-1)\ge0\), the positive coefficient in (19) is
\[
\Lambda(i,j,r)=
\frac{N^2}
 {S_iS_jS_r S_t S_{i-t}S_{j-t}S_{r-t}}.
\tag{20}
\]
This is the same number as (5), with \(k=d-r\). It has the uniform bound (8).

There is an important convention for a network built from (16). In this fully covariant tensor convention, an unturned composition contracts **complementary** incident labels, through the inverse metric (15). Inserting the complete reversal changes this to **equal** incident labels. At a deformed typed turn there is an additional bounded diagonal paired factor. Thus the edges of a reduced-hub tree, which carry turns, join equal cubic labels. In the alternative raw product input/output convention, a turn reverses the output label; these statements are compatible but must not be interchanged in a flow argument.

The complements of the three labels in (18) have total at most \(d-1\). They satisfy the old pair-sum inequalities but fail its required total at least \(d\). The return vertex is therefore not an old positive vertex with complemented labels.

## 5. A strictly negative interior return action

Let
\[
J(u)=\int_0^u\log(2\sin\pi v)\,dv,\qquad 0\le u\le1.
\]
Uniform closed sine-factorial asymptotics applied to (20) give its logarithmic rate. With complementary normalized variables
\[
a=1-i/N,\qquad b=1-j/N,\qquad c=1-r/N,
\]
the limiting domain is \(a,b,c\ge0\), \(a+b+c\le1\), and
\[
\frac1N\log\Lambda(i,j,r)
=\mathcal R(a,b,c)+O(\log N/N),
\tag{21}
\]
where the error is uniform on the closed finite support and
\[
\boxed{\quad
\mathcal R(a,b,c)
=J(a)+J(b)+J(c)+J(a+b+c)
 -J(a+b)-J(a+c)-J(b+c).
\quad}
\tag{22}
\]
The affine \(1/N\) shifts in (20) cost only \(O(\log N/N)\).

The exact integral identity
\[
\begin{aligned}
\mathcal R(a,b,c)&=-\pi^2\int_0^a\int_0^b\int_0^c
       \frac{1}{\sin^2(\pi(u+v+w))}\,dw\,dv\,du.
\end{aligned}\tag{23}
\]
proves that \(\mathcal R<0\) whenever \(a,b,c>0\), including the face \(a+b+c=1\). One may first translate all arguments of \(J\) by a positive \(\varepsilon\) and work with total less than one, use \(J'''(x)=-\pi^2\csc^2\pi x\), and pass to the limit. The singularities at total zero, and at the opposite corner when total is one, are integrable in three dimensions: their local size is a constant times the inverse square of the distance in the sum variable. This also justifies continuity up to the closed domain.

In particular,
\[
\mathcal R(a,b,c)\le-\pi^2abc,
\tag{24}
\]
and every compact region with all three complements at least \(\delta>0\) has a strict return loss at least \(\pi^2\delta^3\). The rate vanishes on the complementary faces where one of \(a,b,c\) is zero. These are precisely the boundary regimes that an eventual whole-tree argument must control, rather than discarding them by a local interior estimate.

## 6. What is and is not supplied for a whole source

Equations (16)–(20) give a finite expansion of each same-color multiplication vertex into the complete tensor and a return tensor. Opposite-color multiplication still uses its constant quotient and has no such return correction. The actual fixed-frame turns contribute their proved bounded paired weights. For a fixed tree this gives finitely many vertex-sector choices, retaining every independent physical input and its coefficient array.

This is a genuine algebraic compiler step. It does not prove that the sum of the remaining complete-cell actions, plus (22) at return vertices, is below the original geometric action. A local nonpositive return rate does not imply that replacing a constrained positive vertex decreases the optimized global value. Nor does the polynomial coefficient estimate prove that an arbitrary exponentially weighted Newton norm is preserved.

For orientation, at a double node \(c\) a quotient \(Q=fg/P_0\) satisfies
\[
Q(c)=\frac{f''(c)g(c)+2f'(c)g'(c)+f(c)g''(c)}{P_0''(c)}.
\tag{25}
\]
Only when both \(f(c)=g(c)=0\), in particular for two radical inputs, may this be simplified to \(f'(c)g'(c)/(P_0''(c)/2)\). This distinction matters for high-low returns. No estimate has replaced a full signed contraction by those point values.

The next specific obligation is a contraction or angle-flow inequality for return-containing trees with their actual boundary profiles. The exact tensor, its signs, the finite support, and the edge convention above are intended as the inputs to that argument.
