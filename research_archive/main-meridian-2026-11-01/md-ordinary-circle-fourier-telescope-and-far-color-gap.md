# The ordinary circle trace and its far-color gap

Private derivation, 1 November 2026. No repository source is changed.

The ordinary auxiliary-circle character gives a finite telescoping identity for the full moving quotient trace. It remains valid at both parities and at colliding Casimir roots. When the remaining raw polynomial has a quadratic complex-strip bound, the identity yields a strict loss for auxiliary colors a fixed distance below the complete color. No root crossing polynomial is inserted in this statement.

## 1. Exact normalizations

Let \(N\ge2\), \(d=N-1\), and let \(\mathcal T_N\) be normalized by \(\mathcal T_N(u+u^{-1})=u^N+u^{-N}\). Put
\[
 P_\sigma(z)=\mathcal T_N(z)+2\cos(2\pi\sigma),\qquad
 \phi_\sigma(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_\sigma}F,
 \qquad \eta=(-1)^{N+1}.
 \tag{1}
\]
The actual root object uses either \(\sigma=s\) or \(\sigma=0\). The latter is the opposite-color order. All products below can be formed as ordinary polynomials and reduced only when taking the trace.

The actual encircling operator of the ordinary auxiliary color \(1\le j\le N\), including the prescribed pivot sign, is
\[
 L_j(z)=(-1)^{j-1}U_{j-1}(z/2).
 \tag{2}
\]
Consequently
\[
 L_j(-u-u^{-1})
   =\sum_{a=0}^{j-1}u^{j-1-2a}.
 \tag{3}
\]
This finite string is the reason that the circle trace simplifies. Omitting the pivot sign in (2) would change (3) by an overall sign.

For any polynomial \(E\) of degree \(D\), write
\[
 E(-u-u^{-1})=\sum_{k=-D}^{D}b_ku^k,\qquad b_{-k}=b_k.
 \tag{4}
\]
The coefficients can be complex and need not be positive. They may depend holomorphically on the microscopic main-meridian parameter.

## 2. The finite trace identity

The exact formula is
\[
 \boxed{\displaystyle
 \phi_\sigma(L_jE)
 =N^2\sum_{\ell=1}^{\lfloor(D+j)/N\rfloor}
 \eta^{\ell+1}U_{\ell-1}(\cos 2\pi\sigma)
       \bigl(b_{\ell N-j}-b_{\ell N+j}\bigr).}
 \tag{5}
\]
Coefficients outside the support of (4) are zero. In particular an empty sum is exactly zero.

Here is a derivation that retains the full trace at repeated roots. For an arbitrary polynomial \(F\) with Laurent expansion \(F(-u-u^{-1})=\sum a_ku^k\), generic Lagrange interpolation at the \(N\) roots \(u_r^N=\eta e^{2\pi i\sigma}\) gives
\[
 \phi_\sigma(F)
 =N^2\sum_{\ell\ge1}\eta^{\ell+1}
 U_{\ell-1}(\cos2\pi\sigma)
       (a_{\ell N-1}-a_{\ell N+1}).
 \tag{6}
\]
For completeness, if \(z_r=-u_r-u_r^{-1}\), then
\[
 P_\sigma'(z_r)=
 \frac{2iN\sin(2\pi\sigma)}{u_r-u_r^{-1}}.
 \tag{7}
\]
Multiplying the Lagrange top-coefficient formula by \((-1)^dN^2=\eta N^2\), summing the resulting powers of \(u_r\), and pairing positive and negative powers yields (6). The quotient \(\sin(2\pi\ell\sigma)/\sin(2\pi\sigma)\) is exactly \(U_{\ell-1}(\cos2\pi\sigma)\). Both sides are polynomials in the coefficients of the monic relation and hence extend through every collision. Thus (6) is not a value-only trace formula.

By (3), the coefficients of \(F=L_jE\) are
\[
 a_k=\sum_{a=0}^{j-1}b_{k-j+1+2a}.
 \tag{8}
\]
The difference selected by (6) telescopes:
\[
 \begin{aligned}
 a_{\ell N-1}-a_{\ell N+1}
 &=\sum_{a=0}^{j-1}
   \bigl(b_{\ell N-j+2a}-b_{\ell N-j+2a+2}\bigr)\\
 &=b_{\ell N-j}-b_{\ell N+j}.
 \end{aligned}
 \tag{9}
\]
Its degree bound is \(\deg(L_jE)=D+j-1\), giving the upper limit in (5). The parity factor \(\eta^{\ell+1}\) is retained; there is no odd-level restriction.

## 3. A uniform gap from a quadratic strip bound

Fix \(R<1\), a degree constant \(A\), and positive constants \(y_0,C\). Suppose a family of raw polynomials \(E_{N,s}\), \(D_N\le AN\), satisfies uniformly for \(|s|\le R\)
\[
 \left|E_{N,s}(-u-u^{-1})\right|
 \le N^K\exp\!\left\{N(F+C y^2+\epsilon_N)\right\},
 \qquad |u|=e^y,\quad |y|\le y_0,\qquad
 \epsilon_N\longrightarrow0.
 \tag{10}
\]
The exponent \(K\), constants, and convergence are uniform in all other retained physical colors. A fresh angular Gaussian centered at \(z=-2\) implies (10); its additional negative angular term is not required in the following coefficient estimate.

Cauchy's coefficient formula on \(|u|=e^y\) gives, for \(k\ge0\) and \(0<y\le y_0\),
\[
 |b_k|\le N^K\exp\!\left\{N(F+C y^2+\epsilon_N)-ky\right\}.
 \tag{11}
\]
Fix \(0<\delta<1\), and restrict the actual auxiliary color by
\[
 1\le j\le(1-\delta)N.
 \tag{12}
\]
Every nonzero frequency selected in (5) then satisfies
\[
 \ell N-j\ge\delta N,\qquad \ell N+j\ge\delta N.
 \tag{13}
\]
Choose
\[
 y_*=\min\{y_0,\delta/(2C)\},\qquad
 c_*=\delta y_*-Cy_*^2\ge\delta y_*/2>0.
 \tag{14}
\]
Only \(\ell\le A+1\) occurs, so the number of trace terms is bounded independently of \(N\). Also
\[
 |U_{\ell-1}(\cos2\pi\sigma)|
 \le\ell\,e^{2\pi(\ell-1)|\operatorname{Im}\sigma|}
 \tag{15}
\]
is uniformly bounded on the fixed parameter disk. Combining (5), (11), and (13)--(15), and absorbing polynomial factors and \(\epsilon_N\), gives a fixed \(c>0\) such that for all sufficiently large \(N\),
\[
 \boxed{\displaystyle
 |\phi_\sigma(L_jE_{N,s})|
 \le \exp\{N(F-c)\},
 \quad |s|\le R,\quad j\le(1-\delta)N.}
 \tag{16}
\]
Both \(\sigma=s\) and \(\sigma=0\) are covered. The full primitive closing factor \(H_N(s)\), if present, is bounded on this disk and does not change the strict exponential loss. Fixed derivatives in \(s\) have the same type of bound on a smaller disk when (10) holds holomorphically on a larger one.

The polynomial in (10) is deliberately the raw finite-degree product. Its degree is \(O(N)\) for a fixed number of canonical factors. There is no need to preserve a Gaussian under quotient reduction before (5). In particular, if each raw factor has a quadratic strip bound at its assigned action, their product has (10) at the sum of those actions.

## 4. The remaining root crossing issue

The lemma directly applies to a closing root coupon \(L_j\), with no root half-twist. It also applies if a separate argument proves (10) for the actual raw product \(R_s^\epsilon E_{N,s}\), but a polynomial spectral-jet norm bound for \(R_s^\epsilon\) alone does not do that.

Indeed ordinary canonical interpolation from that norm yields growth of the form \(e^{N|y|}\) in a fixed complex angular strip. Multiplying this into (10) replaces the quadratic exponent by \(F+|y|+Cy^2\). The frequency separation \(\delta N\), with \(\delta<1\), cannot pay this linear term by the argument in (11)--(14). An actual crossing-specific oscillatory or strip estimate, or a different exact summation argument, is therefore needed for a root carrying a half-twist. No global far-color statement for those roots is proved here.

The result is also an upper bound only. It supplies neither a noncancelling main contribution nor the filled knot's smaller critical action. The old complete geometry identifies \(F\) when the separate source induction provides the original action budget; it is not used to assert an unproved complex gluing comparison.
