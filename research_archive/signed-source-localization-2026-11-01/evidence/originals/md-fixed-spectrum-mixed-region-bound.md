# Mixed spectral regions with several coordinates near \(+2\)

The fixed positive-end estimate can be used when only some of the spectral variables are near \(+2\). The remaining variables need not be equal and may range over the entire real spectral interval. The price is an explicit, coarse exponential bound for each unrestricted crossing region.

The conclusion concerns the original shared polynomial and specified terms of its finite filling sum. It does not establish a bound on the whole complementary contribution. In particular, a tuple with too few coordinates near \(+2\) need not meet the sufficient inequality below.

## 1. A bound for a local coefficient at every real spectral value

Use \(N\ge3\), \(d=N-1\), and the original face operator
\[
C(x,y)z^j=c_jz^j-s_j^2(x+y)z^{j-1}
                    -s_js_{j-1}xy z^{j-2},
\qquad
c_j=2\cos\frac{(2j+1)\pi}{N},\quad
s_j=2\sin\frac{j\pi}{N}.
\]
Its resolvent numerator is the matrix polynomial
\[
V_N(\sigma;C)=\chi_N(\sigma)(\sigma I-C)^{-1},
\qquad
\chi_N(\sigma)=2T_N(\sigma/2)+2.
\]
This is the original numerator, including the values and derivatives needed at its repeated spectral roots. For \(i\le j\), let \(P_{i,j}(x,y;\sigma)\) be its interval continuant. Direct path expansion gives
\[
\begin{aligned}
P_{i,i}&=1,&
P_{i,i+1}&=-s_{i+1}^{\,2}(x+y),\\
P_{i,j}&=-s_j^{\,2}(x+y)P_{i,j-1}
 -s_js_{j-1}(\sigma-c_{j-1})xyP_{i,j-2},\\
[V_N(\sigma;C)]_{i,j}
 &=P_{i,j}\prod_{a<i\ \text{or}\ a>j}(\sigma-c_a).
\end{aligned}
\tag{1}
\]
No division by a spectral factor appears in these identities.

Write \(\|P\|_1\) for the sum of the absolute values of the coefficients of a polynomial in \(x,y\). For \(-2\le\sigma\le2\),
\[
\|P_{i,i+k}\|_1
 \le 8\|P_{i,i+k-1}\|_1+
       16\|P_{i,i+k-2}\|_1.
\tag{2}
\]
Indeed \(s_j^2\le4\), \(s_js_{j-1}\le4\), and
\(|\sigma-c_a|\le4\). The initial bounds are \(1,8\).
Set
\[
B=4(1+\sqrt2),\qquad b=\log B.
\tag{3}
\]
Since \(B^2=8B+16\) and \(8<B\), induction in (2) gives
\(\|P_{i,i+k}\|_1\le B^k\).
There are exactly \(d-k\) unused rows outside the interval.
Consequently
\[
\bigl|[x^p y^{k-p}][V_N(\sigma;C(x,y))]_{i,i+k}\bigr|
 \le 4^{d-k}B^k\le B^d.
\tag{4}
\]
for every original coefficient and every real \(\sigma\in[-2,2]\).
This elementary bound is deliberately coarse. It will be applied only at the coordinates where the sharper positive-end estimate is unavailable.

## 2. One shared coefficient, with two types of spectral interval

Fix an original diagram with \(r\) crossing regions for which the homogeneous marked source identity holds. Retain its ordinary face targets, its protected faces, its cups and caps, and its original mark. Let \(S_N\) be the full shared spectral polynomial, \(C_N\) its all-CROSS projection, and
\[
D_N=S_N-C_N.
\]
The CROSS projection selects intervals in (1); it does not separate the signed terms within their continuants. Thus both (4) and the fixed positive-end coefficient estimate apply to it.

Choose \(0<\delta\le1\), and write
\[
I_\delta=[2-\delta,2],\qquad
A_\delta=1+\delta^{-1/2},\qquad
\omega(\delta)=
\sqrt\delta\left(2+\log(1+2/\sqrt\delta)\right).
\tag{5}
\]
The [fixed positive-end proof](md-fixed-spectrum-positive-end-continuant-and-source-corner.md) establishes, for \(N\ge\pi/\sqrt\delta\), the bound
\[
\sup_{\sigma\in I_\delta}
\left|[x^p y^{j-i-p}]
       [V_N(\sigma;C(x,y))]_{i,j}\right|
 \le A_\delta N^3e^{N\omega(\delta)}.
\tag{6}
\]
It combines the signed one-step and two-step paths before making a comparison. Replacing that proof by the estimate (2) at the restricted coordinates would lose the fact that \(\omega(\delta)\to0\).

For a subset \(J\subseteq\{1,\ldots,r\}\) with \(|J|=k\), put
\[
\mathcal Q_J=
\prod_{e\in J}I_\delta
\ \times\
\prod_{e\notin J}[-2,2].
\]
Each homogeneous four-face polynomial has at most \(N^3\) monomials. Expand their product and then impose the one original shared coefficient. There are at most \(N^{3r}\) selections before that restriction. Combining (4) and (6) therefore proves
\[
\boxed{\quad
\sup_{\mathcal Q_J}|D_N|
\le
2A_\delta^k N^{3r+3k}
\exp\!\left\{
N\bigl[k\omega(\delta)+(r-k)b\bigr]
\right\}.
\quad}
\tag{7}
\]
The factor two accounts for full minus all-CROSS; either term separately has the same bound without it. A repeated face has a single target throughout this argument. No independent maximization or summation over two copies of that target is introduced.

For the union of the sets \(\mathcal Q_J\) with \(|J|\ge k\), (7) gives the same exponential rate provided \(\omega(\delta)\le b\). The maximum over the finitely many sets introduces no level-dependent cost.

## 3. The corresponding terms of the original filling functional

For a fixed signed crossing power \(n\), let \(\mathcal L_N^n\) denote the original full-Hermite filling functional. It acts on polynomials of degree at most \(d\). Its double-root terms are
\[
\frac1{N^2}
\left[
(4-c^2)(f_nH)'(c)-cf_n(c)H(c)
\right],
\tag{8}
\]
where \(f_n\) is the actual crossing polynomial, with its Cartan scalar and prescribed normal derivatives. At odd levels there is also the simple-root term \(f_n(-2)H(-2)/N^2\).

For a set \(E\) of distinct spectral roots, let
\(\mathcal L_{N,E}^n\) retain exactly the terms in (8) at \(c\in E\), and the simple-root term if \(-2\in E\). The ordinary global proof by the angular derivative inequality bounds every such restriction:
\[
|\mathcal L_{N,E}^nH|
\le(1+|n|/2)\|H\|_{[-2,2]}.
\tag{9}
\]
To see why restriction causes no difficulty, use
\(P(\phi)=H(2\cos\phi)\) and the paired angular representatives of each double root. The derivative term is bounded by
\(\|P'\|_\infty\le d\|P\|_\infty\); the derivative of the crossing phase is bounded by \(|n|N/2\). Deleting complete root terms only reduces the number of summands in this triangle-inequality estimate. This argument does not assert that the value of the restricted sum is smaller than the value of the full sum.

At roots in \(I_\delta\), the interval Markov inequality instead gives
\[
|\mathcal L_{N,I_\delta}^nH|
\le
\left(\frac{4d^2}{N}+\frac{|n|}{2}+\frac1N\right)
\|H\|_{I_\delta}.
\tag{10}
\]
Indeed \(4-c^2\le4\delta\),
\(\|H'\|_{I_\delta}\le2d^2\|H\|_{I_\delta}/\delta\),
and there are at most \(N/2\) distinct double roots. The odd simple root is outside \(I_\delta\).

Partition each root set into \(E_+=I_\delta\cap\{\text{roots}\}\)
and its complement \(E_-\). For a specified subset \(J\), the tensor product with \(E_+\) at \(e\in J\) and \(E_-\) elsewhere is an exact part of the finite original filling sum. Equations (7), (9), and (10) bound its value on \(D_N\) by
\[
\begin{aligned}
2A_\delta^kN^{3r+3k}
&\prod_{e\in J}
\left(\frac{4d^2}{N}+\frac{|n_e|}{2}+\frac1N\right)
\prod_{e\notin J}(1+|n_e|/2)\\
&\quad\times
e^{N[k\omega(\delta)+(r-k)b]}.
\end{aligned}
\tag{11}
\]
All powers are fixed before \(N\) increases, so the displayed factors outside the exponential have zero exponential rate. Taking the sum over \(|J|\ge k\) costs at most \(2^r\), since the diagram is fixed. This bounds the actual part of the complementary filling sum with at least \(k\) positive-end root coordinates.

There is an optional exact improvement. Split each functional into its \(H'\) part and its \(H\) part. Their norm bounds are
\[
a_e=
\begin{cases}
4d^2/N,&e\in J,\\
d/N,&e\notin J,
\end{cases}
\qquad
b_e=1/N+|n_e|/2.
\tag{12}
\]
The all-value tensor vanishes on \(D_N\), because the full and all-CROSS source agree on the Cartesian product of the spectral node sets. Thus the functional prefactor in (11) can be replaced by
\[
\prod_e(a_e+b_e)-\prod_e b_e.
\tag{13}
\]
This keeps all mixed derivatives; it deletes only the exactly vanishing all-value tensor.

## 4. A sufficient geometric comparison for these regions

Let \(Y\) be the original complete augmented complement, with
\(\Phi=\operatorname{Vol}(Y)/(2\pi)>0\), and assume the established nonzero all-CROSS filling theorem for this precise marked diagram. Suppose an integer \(k\le r\) satisfies
\[
(r-k)\log\bigl(4(1+\sqrt2)\bigr)<\Phi.
\tag{14}
\]
Choose \(\delta>0\) sufficiently small that \(\omega(\delta)\le b\) and
\[
E_{k,\delta}:=k\omega(\delta)+(r-k)b<\Phi.
\tag{15}
\]
For independently sufficiently long fixed signed fillings, the actual filled action \(\Phi_{\boldsymbol n}\) tends to \(\Phi\), so it exceeds \(E_{k,\delta}\) by a positive amount. The part bounded in (11), summed over all \(|J|\ge k\), is then exponentially smaller than the nonzero geometric contribution with action \(\Phi_{\boldsymbol n}\).

This is a rigorous exclusion of a union of mixed spectral regions of the original source. It includes the joint positive-end corner by taking \(k=r\). It leaves the configurations with fewer than \(k\) positive-end coordinates unresolved. No conclusion about the entire invariant follows until those remaining configurations are also controlled, with their original derivatives and phases.
