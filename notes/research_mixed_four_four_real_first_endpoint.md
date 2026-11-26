# Closing the real first four/four interval at zero

Private written deduction, 10 November 2026. The complete real-interval
bound for the first four/four pair extends to zero at arbitrarily small
exponential cost. The argument uses the literal Laurent degree, retaining
both first Fourier choices and the original outgoing half allocation.
No old collar estimate or extra word-length hypothesis is needed.

## 1. Exact source and the bound away from zero

Fix an actual positive three/four word of length \(m\ge3\) beginning
with four and four. Retain the reference, lifts, ordinary color \(w\),
and outgoing target
\[
 b=z+id,\qquad z\in P=[11/50,9/20],\qquad d\in[-.102,-.001]
\tag{1}
\]
of the [complete real-interval theorem](research_mixed_four_four_real_first_interval.md).
The length-three attached next-input case is included. Put
\(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(X=e^{-2\pi ix}\), \(Y=e^{-2\pi ib}\), and retain
\[
\begin{split}
 U_N(w,X)&=\sum_{i=0}^{N-1}
       \frac{H_N(w,q_N^{-i})(q_NX;q_N)_i}{P_i^2},\\
 C_N(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{P_j^3},\\
 K_{\sigma,N}(w;X,Y)&=
       U_N(w,X)C_N(X,Y)d_N(X)X^{-N\sigma},
                    \qquad \sigma\in\{0,1\}.
\end{split}
\tag{2}
\]
Here \(H_N\) is the complete original cap coefficient. The
[original Fourier polynomial](research_mixed_fourier_weight_continuation.md)
has \(\deg d_N<N\), with its forcing retained. The outgoing allocation
is \(|d_N(Y)|^{1/2}\), not a chosen holomorphic square root.

Let \(\Lambda(z)\) be the original geometric affine rate. Corollary 2
of the real-interval theorem gives, for every fixed \(0<\rho<1/10\)
and every \(\tau>0\),
\[
 |K_{\sigma,N}(w;e^{-2\pi ix},Y)|\,|d_N(Y)|^{1/2}
 \le C_{\rho,\tau}N^{A_{\rho,\tau}}
 \exp N\left\{\Lambda(z)-\frac1{1000}
                         -\frac{1/10-x}{3}+\tau\right\},
 \qquad \rho\le x\le1/10.
\tag{3}
\]
This is uniform for real \(w\in[-2,2]\), both parities and both
\(\sigma\), at the actual private heights. Its constants may depend
on \(\rho\) and the fixed word.

The Laurent exponent support of (2) in \(X\) is contained in
\[
 \left[-(1+\sigma)N+1,\ (2-\sigma)N-2\right].
\tag{4}
\]
Indeed \(U_N\) has degrees in \([0,N-1]\); each \(C_N\) term
has degrees in \([-j,0]\); \(d_N\) has degrees in \([0,N-1]\);
and the selected monomial subtracts \(N\sigma\). Hence every
exponent has absolute value at most \(2N\). No nonvanishing of
an extreme coefficient is required.

## 2. Small-cost extension across a missing endpoint

The following is the tangent-substitution estimate in Section 1 of
[the polynomial continuation theorem](research_mixed_horizontal_complex_extension.md),
with the choices made explicit.

**Lemma 1.** For every \(\varepsilon>0\), there exist fixed
\(0<\rho<a<1/10\), independent of \(N\), such that every
\[
 F_N(x)=\sum_{|\nu|\le2N}c_{\nu,N}e^{-2\pi i\nu x}
\]
satisfying \(|F_N|\le M_N\) on \([\rho,a]\) obeys
\[
 |F_N(x)|\le2(4N+1)M_Ne^{\varepsilon N},
                         \qquad 0\le x\le a.
\tag{5}
\]
The coefficients may depend on additional parameters.

*Proof.* Choose \(\chi>1\) so close to one that
\(4\log\chi<\varepsilon/2\), and put
\(A_\chi=(\chi+\chi^{-1})/2>1\). Next choose \(a>0\) so small that
\[
 r_0=\tan(\pi a/2),\qquad A_\chi r_0<1,\qquad
 2\log\frac{1+r_0^2}{1-A_\chi^2r_0^2}<\varepsilon/2.
\tag{6}
\]
Continuity at \(a=0\) permits these choices with \(a<1/10\).
Finally choose \(0<\rho<a\) so small that, writing
\[
 c=(a+\rho)/2,\quad\alpha=(a-\rho)/2,\quad
 r=\tan(\pi\alpha),\quad R=A_\chi r,
\]
one has
\[
                         \tan(\pi c)<A_\chi r.
\tag{7}
\]
At \(\rho=0\), the ratio of the left side to \(r\) is one;
continuity and \(A_\chi>1\) prove the existence of (7).
All choices are fixed before \(N\).

Set \(D=2N\) and \(t=\tan(\pi(x-c))\). Since
\(e^{-2\pi i(x-c)}=(1-it)/(1+it)\),
\[
                         p_N(t)=(1+t^2)^D F_N(x)
\]
is a polynomial of degree at most \(2D\): each Laurent term
contributes a constant times
\((1-it)^{D+\nu}(1+it)^{D-\nu}\).
On \([-r,r]\), corresponding to \([\rho,a]\),
\(|p_N|\le(1+r^2)^D M_N\). Let \(E_\chi\) be the closed
ellipse with foci \(\pm1\) and semimajor axis \(A_\chi\).
The elementary Chebyshev bound gives
\[
 |p_N(t)|\le2(2D+1)(1+r^2)^D M_N\chi^{2D},
                                      \qquad t\in rE_\chi.
\tag{8}
\]
On that ellipse \(|t|\le R<1\), so \(|1+t^2|\ge1-R^2\).
Dividing only by this explicit nonvanishing clearing factor gives
\[
 |F_N(x)|\le2(2D+1)M_N
 \exp\left\{D\left[
       \log\frac{1+r^2}{1-R^2}+2\log\chi\right]\right\}.
\tag{9}
\]
The first logarithm increases with \(r\), and \(r\le r_0\).
Since \(D=2N\), (6) and the choice of \(\chi\) bound the
exponent by \(\varepsilon N\).

For \(0\le x\le a\), the real \(t\) lies in
\([-\tan(\pi c),r]\), strictly inside the real diameter of
\(rE_\chi\) by (7). Thus (9) proves (5). If \(M_N=0\),
the polynomial vanishes on an interval and hence identically.
No source polynomial or quantum factorial has been divided out.
\(\square\)

The starting interval is nondegenerate and fixed. The lemma neither
lets \(\rho\) depend on \(N\) nor assumes uniformity of the source
constants as \(\rho\) tends to zero.

## 3. The complete closed real interval

**Theorem 2.** For every \(\tau>0\), both parities and both first
Fourier choices,
\[
 |K_{\sigma,N}(w;e^{-2\pi ix},Y)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
       e^{N\{\Lambda(z)-1/2000+\tau\}},
                    \qquad 0\le x\le1/10.
\tag{10}
\]
This holds uniformly for all real \(w\in[-2,2]\), and on a
sufficiently small fixed ordinary-color disk about \(-2\). Each
fixed color derivative has the same rate on a smaller disk with
polynomial cost. The actual-reference and \(m\ge3\) scope is unchanged.

*Proof.* Use Lemma 1 with \(\varepsilon=1/4000\), fixing its \(a,\rho\).
In (3) choose tolerance \(1/4000\) and discard the favorable linear
loss. For each \(N,w,b,\sigma\), apply the lemma to
\[
 F_N(x)=|d_N(Y)|^{1/2}K_{\sigma,N}(w;e^{-2\pi ix},Y).
\tag{11}
\]
The multiplier is constant in \(x\), so the support bound (4) persists,
including when the multiplier is zero. On \([\rho,a]\), (3) gives
\[
 M_N=C_{\rho,1/4000}N^{A_{\rho,1/4000}}
                         e^{N\{\Lambda(z)-3/4000\}}.
\]
Equation (5) gives exponent \(\Lambda(z)-1/2000\) on \([0,a]\).
On \([a,1/10]\), (3) has the stronger exponent
\(\Lambda(z)-3/4000\). Absorb the factor \(2(4N+1)\) into
the common polynomial. The choices are uniform in \(w,z,\sigma\).
Any finitely many small levels are included by increasing the constant,
using continuity of the exact finite functions on the fixed compact
parameter set. No division by the outgoing multiplier occurs.

The exact source has degree less than \(N\) in \(w\), as retained
in the real-interval theorem. At fixed \(x,b,\sigma,N\), (11) is
therefore a polynomial of that same degree in \(w\). The rescaled
Chebyshev estimate on \([-2,2]\) extends the uniform real-color
bound to a fixed ellipse with arbitrarily small added exponential
allowance. This ellipse contains a fixed disk about \(-2\).
Choose the allowance below \(\tau\), then apply Cauchy's formula
on a smaller disk for all fixed derivatives. The multiplier is
constant in \(w\), so these are precisely the weighted derivatives
of \(K_{\sigma,N}\), also when the multiplier vanishes. No modulus
halfweight is differentiated. This proves (10). \(\square\)

Any prescribed gap strictly smaller than \(1/1000\) can be retained:
choose the continuation cost and source tolerance with sum smaller
than the difference of the gaps. The displayed \(1/2000\) is a
convenient fixed choice.

At \(x=0\), \(X=1\), and (2) is the same finite Laurent polynomial
at a nonzero argument. No factorial symbol is continued through a
logarithmic endpoint. The complete rows, aliases, endpoint terms and
both original contour densities were retained in (3) before the degree
argument was applied; their normalization is unchanged.

This closes the real segment from zero to the one-tenth face for both
first selections without a collar input or a length-\(m\ge4\) restriction.
It does not estimate a height-changing join, alter the outgoing
reference, identify the remaining Fourier portions, or prove whole-word
or knot noncancellation.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_four_four_real_first_interval.md | b848eb005f99d57259662ef3a864b207e093b6ebfaf4c34c2dbcc1e9727d58fc |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The full written proof and directly used source implications were read.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.

