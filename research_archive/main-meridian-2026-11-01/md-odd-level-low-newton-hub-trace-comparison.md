# A cancellation-preserving low-Newton hub bound at odd levels

Private proof, 1 November 2026. No repository file is changed.

At odd levels, a whole multiplication hub admits an exact signed-trace comparison with its complete positive kernel. The comparison is made after summing the return sectors. It does not bound their separate absolute envelopes. The argument covers low input and low output/probe coordinates; its high-output limitation is explicit.

## 1. The Laurent coefficients of a low Newton polynomial

Fix \(q=e^{\pi i/N}\), \(d=N-1\), \(M=\lfloor d/2\rfloor\), and retain the fixed Newton normalization
\[
e_n(z)=S_n^{-2}\prod_{j=0}^{n-1}(c_j-z),\qquad
S_n=\prod_{r=1}^n2\sin(r\pi/N),\quad
c_j=2\cos((2j+1)\pi/N).
\]
For \(n\le M\),
\[
e_n(-u-u^{-1})
=\frac{u^{-n}}{S_n^2}
 \prod_{j=0}^{n-1}(1+q^{2j+1}u)(1+q^{-2j-1}u).
\tag{1}
\]
The \(2n\) exponents are consecutive odd integers from \(-2n+1\) to \(2n-1\). The finite binomial formula therefore gives the real Laurent coefficients
\[
[u^{k-n}]e_n(-u-u^{-1})
=\frac{S_{2n}}{S_n^2S_kS_{2n-k}}>0,
\qquad 0\le k\le2n.
\tag{2}
\]
All indices are below \(N\); no root factorial is divided by zero. The coefficients are symmetric. For \(1\le k\le n\), their consecutive ratio is
\[
\frac{\sin((2n-k+1)\pi/N)}{\sin(k\pi/N)}\ge1.
\tag{3}
\]
The inequality follows by subtracting the two sines and using
\((2n+1)\pi/N\le\pi\). Equality throughout occurs at the largest low index of an odd level.

Thus the coefficient sequence is nonnegative, symmetric, and nonincreasing as the distance from its center increases. Products and nonnegative linear combinations preserve these properties. One elementary proof for products writes each symmetric unimodal sequence as a nonnegative sum of the interval indicators \(\mathbf1_{|k|\le r}\). The convolution of two such indicators is symmetric and unimodal. Consequently, for every product of nonnegative low-Newton polynomials,
\[
F(-u-u^{-1})=\sum_{k=-D}^{D}a_ku^k,\qquad
 a_{-k}=a_k\ge a_{k+1}\ge0\quad(k\ge0).
\tag{4}
\]
The coefficients outside the finite support are zero.

## 2. Exact trace formula at either parity

Let
\[
P_s(z)=\mathcal T_N(z)+2\cos(2\pi s),\qquad
\phi_s(F)=(-1)^dN^2[z^d](F\bmod P_s),
\qquad \eta=(-1)^{N+1}.
\tag{5}
\]
For an arbitrary polynomial \(F\), expand \(F(-u-u^{-1})=\sum a_ku^k\). Its coefficients are symmetric, but need not be positive. Put
\[
L=\left\lfloor\frac{D+1}{N}\right\rfloor,
\qquad d_\ell=a_{\ell N-1}-a_{\ell N+1}.
\]
Then the exact finite identity is
\[
\boxed{\quad
\phi_s(F)=N^2\sum_{\ell=1}^{L}
 \eta^{\ell+1}d_\ell
 U_{\ell-1}(\cos(2\pi s)).
\quad}
\tag{6}
\]
Here \(U_{\ell-1}(\cos\tau)=\sin(\ell\tau)/\sin\tau\), with its polynomial continuation through every resonance. If \(L=0\), the sum is zero.

For a proof at generic \(s\), choose the \(N\) roots satisfying
\(u_j^N=\eta e^{2\pi i s}\), and put \(z_j=-u_j-u_j^{-1}\). They are the distinct roots of \(P_s\). Direct differentiation gives
\[
P_s'(z_j)=\frac{2iN\sin(2\pi s)}{u_j-u_j^{-1}}.
\tag{7}
\]
Lagrange interpolation of the canonical remainder gives
\[
\phi_s(F)=\frac{\eta N}{2i\sin(2\pi s)}
 \sum_{j=0}^{N-1}(u_j-u_j^{-1})F(-u_j-u_j^{-1}).
\]
The root sum selects exponents divisible by \(N\). Pairing its positive and negative exponents, and using \(a_{-k}=a_k\), gives (6). Both sides are entire functions of \(s\): on the left polynomial division by the monic \(P_s\) has entire coefficients; on the right the quotients are the displayed Chebyshev polynomials. Thus the identity holds at every complex \(s\), including all collisions. This is an identity for the full coefficient trace, not a value-only replacement at repeated roots.

At completeness,
\[
\phi_0(F)=N^2\sum_{\ell=1}^{L}\eta^{\ell+1}\ell d_\ell.
\tag{8}
\]
The parity signs in (6)–(8) are essential.

## 3. Odd levels: a whole signed comparison

Suppose now that \(N\) is odd and \(F\) satisfies (4). Then \(\eta=1\) and every \(d_\ell\ge0\). For \(|s|\le R\), the finite exponential formula for \(U\) gives
\[
|U_{\ell-1}(\cos(2\pi s))|
\le \ell\exp\{2\pi(\ell-1)|\operatorname{Im}s|\}.
\tag{9}
\]
Consequently, if \(L\ge1\),
\[
\boxed{\quad
|\phi_s(F)|
\le e^{2\pi(L-1)R}\phi_0(F),\qquad |s|\le R.
\quad}
\tag{10}
\]
This holds uniformly at every odd level. If the complete trace is zero, all the nonnegative \(d_\ell\) vanish and the deformed trace is identically zero as well. If the number of multiplied low-degree factors is fixed, then \(L\) is bounded independently of \(N\); the comparison constant therefore has no exponential cost. Fixed parameter derivatives are also bounded by the same type of comparison on a slightly larger disk, by Cauchy's formula.

The statement extends to arbitrary complex low-coordinate arrays in a multilinear form. Let
\[
F_b=\sum_{n=0}^{M}f_{b,n}e_n,\qquad
F_b^{\mathrm{abs}}=\sum_{n=0}^{M}|f_{b,n}|e_n.
\]
Expand the product in its input Newton indices, apply (10) to each product of basis elements, and only then use the triangle inequality. The old complete trace on each such basis product is nonnegative. This proves
\[
\boxed{\quad
\left|\phi_s\!\left(\prod_{b=1}^{B}F_b\right)\right|
\le C_{B,R}\,
 \phi_0\!\left(\prod_{b=1}^{B}F_b^{\mathrm{abs}}\right).
\quad}
\tag{11}
\]
It would be incorrect to bound a difference of two Laurent coefficients of an arbitrary complex polynomial by the corresponding difference of its positive majorant. The multilinear basis argument avoids that step.

## 4. Low output of an unflagged multiplication hub

Let \(A_s=F_1*_s\cdots *_sF_B\), with all inputs supported in low fixed Newton coordinates. Associativity means that closing the hub is the trace of the ordinary polynomial product, reduced only at the end. The exact fixed-frame turn gives
\[
[e_k]\mathscr T_s^{\mathrm{fix}}A_s
=\frac{\gamma_N(s)W_{d-k}(s)}{H_N(s)}
       \phi_s(e_k*_sA_s).
\tag{12}
\]
For every low output \(k\le M\), the extra factor \(e_k\) is another low Newton polynomial. Equations (11)–(12) therefore imply, on \(|s|\le R<1\),
\[
\left|[e_k]\mathscr T_s^{\mathrm{fix}}A_s\right|
\le C_{B,R}\phi_0\!\left(e_k\prod_bF_b^{\mathrm{abs}}\right).
\tag{13}
\]
The paired prefactor is uniformly bounded. Summing (13) against any nonnegative low probe weights gives the old positive low-probe bound for this whole hub. In particular, whenever its input arrays satisfy the old coefficient cone, the old intrinsic probe action bounds this low-output contribution with the same exponential rate. Return sectors have already been summed inside (6), so the bound bypasses their separate absolute envelopes.

This result does not include a high output/probe index: \(e_k\) with \(k>M\) does not have the positive unimodal Laurent sequence used in Section 1. It also does not yet iterate through an arbitrary component containing internal turns, since an intermediate turned output can have high coordinates. At even levels \(\eta=-1\), the aliases in (8) alternate; positivity of the differences alone does not compare their absolute sum to their signed complete trace. These are the precise additional steps needed for a full all-parity unflagged-component theorem.
