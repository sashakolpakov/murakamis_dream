# A calibrated periodic right endpoint collar for the first four/four pair

Private written deduction, 10 November 2026. The complete real first-pair
bound near zero also pays a fixed right endpoint collar, including a
small complex neighborhood. The argument uses the actual finite Laurent
polynomial and its exact period. It does not reflect an individual
conditional kernel or reverse the Fourier polynomial.

## 1. Original source and the available real bound

Fix an actual positive three/four word of length \(m\ge3\) beginning
with four and four. Keep the exact reference, lifts and ordinary color
of [the real endpoint theorem](research_mixed_four_four_real_first_endpoint.md).
In particular
\[
 b=z+id,\qquad z\in P=[11/50,9/20],\qquad
                         -.102\le d\le-.001.
\tag{1}
\]
The height \(d\) remains the actual second-coordinate height. The
length-three attached reference is included. Put
\[
 q_N=e^{-2\pi i/N},\quad P_j=(q_N;q_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},
\]
and retain the entire finite functions
\[
\begin{split}
 U_N(w,X)&=\sum_{i=0}^{N-1}
       H_N(w,q_N^{-i})\,\frac{(q_NX;q_N)_i}{P_i^2},\\
 C_N(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{P_j^3},\\
 K_{\sigma,N}(w;X,Y)&=U_N(w,X)C_N(X,Y)d_N(X)X^{-N\sigma},
                         \qquad \sigma\in\{0,1\}.
\end{split}
\tag{2}
\]
Here \(H_N\) is the complete original endpoint coefficient.
The [forced Fourier polynomial](research_mixed_fourier_weight_continuation.md)
is the original degree-\((N-1)\) interpolant, including its forcing.
The outgoing allocation is its modulus \(|d_N(Y)|^{1/2}\).

Let \(\Lambda(z)\) be the original affine geometric rate in the
real endpoint theorem. Its Theorem 2 proves, for every \(\tau>0\),
\[
 |d_N(Y)|^{1/2}|K_{\sigma,N}(w;e^{-2\pi ix},Y)|
 \le C_\tau N^{A_\tau}
             e^{N\{\Lambda(z)-1/2000+\tau\}},
                     \qquad 0\le x\le1/10.
\tag{3}
\]
It holds for all real \(w\in[-2,2]\), and on a sufficiently small
fixed ordinary-color disk about \(-2\). Both parities and both
\(\sigma\) are included. The disk may depend on \(\tau\), and is
fixed before \(N\). Uniformity is inherited on the same compact
actual-reference families; no independent reference box is substituted.

The exponent band of \(K_{\sigma,N}\) in \(X\) is contained in
\[
 [-(1+\sigma)N+1,\ (2-\sigma)N-2]\subset[-2N,2N].
\tag{4}
\]
Indeed \(U_N,d_N\) have degrees at most \(N-1\), and each conditional
row has exponents in \([-j,0]\). Also, exactly at every complex \(a\),
\[
 K_{\sigma,N}(w;e^{-2\pi i(a+1)},Y)
                    =K_{\sigma,N}(w;e^{-2\pi ia},Y).
\tag{5}
\]
This includes the selected factor, since \(N\sigma\) is an integer.
There is no changed boundary variable or scalar in (5).

## 2. A small-cost complex continuation across zero

We spell out the needed one-variable consequence of
[Laurent polynomial continuation](research_mixed_horizontal_complex_extension.md),
Section 1. This also specifies that the collar is fixed, rather than
shrinking with \(N\).

**Lemma 1.** For every \(\varepsilon>0\), there are fixed
\(0<a_0<1/10\), \(\rho>0\), and \(\delta>0\), such that every
\[
 F_N(\zeta)=\sum_{|\nu|\le2N}c_{\nu,N}e^{-2\pi i\nu\zeta}
\]
satisfying \(|F_N|\le M_N\) on \([0,a_0]\) obeys
\[
 |F_N(\zeta)|\le 2(4N+1)M_Ne^{\varepsilon N},
 \qquad \operatorname{dist}(\zeta,[-\rho,0])\le2\delta.
\tag{6}
\]
The coefficients may depend on arbitrary extra parameter labels.

*Proof.* Choose \(\chi>1\) so close to one that
\(4\log\chi<\varepsilon/2\), and put
\(A_\chi=(\chi+\chi^{-1})/2\). Choose \(a_0>0\) sufficiently
small that, with \(r=\tan(\pi a_0/2)\),
\[
 A_\chi r<1,\qquad
 2\log\frac{1+r^2}{1-A_\chi^2r^2}<\varepsilon/2.
\tag{7}
\]
These choices exist by continuity, with \(a_0<1/10\).
Let \(E_\chi\) be the closed ellipse with foci \(\pm1\) and
semimajor axis \(A_\chi\). The map
\[
 \zeta=\frac{a_0}{2}+\frac1\pi\arctan t
\tag{8}
\]
is holomorphic and injective on \(|t|<1\), with its branch at zero.
Its image of the interior of \(rE_\chi\) is an open set
\(\Omega\) containing the entire interval \([0,a_0]\).
In particular it contains a fixed open disk about zero. Choose
\(\rho,\delta>0\), with \(\rho<1/10\), so small that
\[
 \{\zeta:\operatorname{dist}(\zeta,[-\rho,0])\le2\delta\}
                                                   \Subset\Omega.
\tag{9}
\]
Thus all three widths are chosen before \(N\).

For \(D=2N\), set \(t=\tan(\pi(\zeta-a_0/2))\). The function
\[
                         p_N(t)=(1+t^2)^D F_N(\zeta)
\]
is a polynomial of degree at most \(2D\). Each Laurent term
contributes a constant times
\((1-it)^{D+\nu}(1+it)^{D-\nu}\).
On \([-r,r]\), \(|p_N|\le(1+r^2)^D M_N\). The elementary
Chebyshev estimate, proved in the cited source, gives
\[
 |p_N(t)|\le2(2D+1)(1+r^2)^D M_N\chi^{2D},
                                           \qquad t\in rE_\chi.
\]
Since \(|1+t^2|\ge1-A_\chi^2r^2>0\), division by this explicit
clearing factor gives
\[
 |F_N(\zeta)|\le2(2D+1)M_N
 \exp\left\{D\left[
 \log\frac{1+r^2}{1-A_\chi^2r^2}+2\log\chi\right]\right\}.
\tag{10}
\]
Equations (7), \(D=2N\), and the choice of \(\chi\) bound the
exponent by \(\varepsilon N\). Equations (8)--(9) prove (6).
If \(M_N=0\), the polynomial is identically zero. No finite
source factor or quantum factorial has been divided out. \(\square\)

The starting interval \([0,a_0]\) is fixed and nondegenerate.
This lemma requires no uniform estimate as an interval length tends
to zero and no estimate for a sequence of \(N\)-dependent intervals.

## 3. The actual right collar and its complete integral

**Theorem 2.** There are fixed \(\rho,\delta>0\) and an ordinary-color
disk \(\mathcal D\) about \(-2\) such that
\[
 \boxed{\quad
 |d_N(Y)|^{1/2}|K_{\sigma,N}(w;e^{-2\pi ia},Y)|
 \le C N^A e^{N\{\Lambda(z)-1/4000\}}
 \quad}
\tag{11}
\]
whenever
\[
 \operatorname{dist}(a,[1-\rho,1])\le2\delta,\qquad
 w\in[-2,2]\ \hbox{or}\ w\in\mathcal D.
\tag{12}
\]
Both first Fourier choices, both level parities and every row of
the original source are retained. The same estimate holds, with
different constants, for each fixed derivative
\[
 |d_N(Y)|^{1/2}
 \left|\partial_a^j\partial_w^k
           K_{\sigma,N}(w;e^{-2\pi ia},Y)\right|
\tag{13}
\]
on the smaller \(a\)-neighborhood of radius \(\delta\) and a smaller
ordinary-color disk. On the real ordinary-color interval the
corresponding derivatives have at most additional polynomial cost.

*Proof.* Use (3) with \(\tau=1/8000\). Retain a closed ordinary-color
disk compactly inside the resulting disk, and include the full real
interval among the compact parameter labels. Apply Lemma 1 with
\(\varepsilon=1/8000\), fixing its \(a_0,\rho,\delta\), to
\[
 F_N(\zeta)=|d_N(Y)|^{1/2}
                    K_{\sigma,N}(w;e^{-2\pi i\zeta},Y).
\tag{14}
\]
The multiplier is constant in \(\zeta\) and \(w\). Thus (4) gives
the required Laurent band even when \(d_N(Y)=0\).
The input bound on \([0,a_0]\) has rate
\(\Lambda(z)-3/8000\); (6) therefore leaves
\(\Lambda(z)-1/4000\). Absorb \(2(4N+1)\) into the
polynomial prefactor.

Translate \(\zeta=a-1\) and use the exact identity (5).
This proves (11)--(12). In particular \(a=1\) is the identical
finite argument \(X=1\) as \(a=0\); no logarithmic factorial symbol
is continued through that point.

The weighted function (14) is holomorphic in \(\zeta,w\) for each
fixed \(N,b\). Cauchy's formula on smaller fixed neighborhoods proves
(13). If its constant multiplier vanishes, all these weighted
derivatives vanish as well. For real \(w\), use its degree less than
\(N\) and Markov's inequality on \([-2,2]\), together with the
\(a\)-neighborhood estimate and Cauchy in \(a\). No derivative in
the parameter \(b\), and no derivative of its modulus halfweight,
is asserted. \(\square\)

For any rectifiable path \(\Gamma\) lying in the neighborhood (12),
with length bounded independently of \(N\), the literal oriented
source consequently satisfies
\[
 |d_N(Y)|^{1/2}
 \left|N\int_\Gamma
       K_{\sigma,N}(w;e^{-2\pi ia},Y)\,da\right|
 \le C_\Gamma N^{A+1}e^{N\{\Lambda(z)-1/4000\}}.
\tag{15}
\]
The original factor \(+N\), orientation, and selected monomial are
unchanged. The original unit-modulus crossing scalar, if placed
outside this first-coordinate integral, is unchanged as well.
Fixed ordinary-color derivatives satisfy the same conclusion on
smaller disks. This includes the real right endpoint arc and any
fixed short connector contained in (12).

The outgoing target remains exactly (1), with its full original
modulus half allocation. There is no division by that allocation,
by either kernel, or by a value that might vanish. All aliases,
joins, physical endpoint rows and odd-level terms were retained
before the complete real estimate (3) was applied.

This pays a fixed right endpoint collar. It does not estimate the
intermediate right interval between the plateau and that collar,
or a height reset of size equal to an unrestricted actual reference
height. It is not a reflection theorem for \(C_N\), does not
identify the two Fourier sectors, and gives no whole-period,
whole-word or knot noncancellation conclusion.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The full written proof and all directly used source implications were
read. No mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation or frozen-source edit was performed.

