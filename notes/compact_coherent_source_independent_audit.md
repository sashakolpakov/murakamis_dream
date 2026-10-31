# Independent audit of the compact coherent source period

Audit, 27 October 2026. Sections 1--5 of
[compact_coherent_source_period.md](compact_coherent_source_period.md)
pass this independent check. The finite centered star derivatives,
global primitive, both walls and physical Poisson scale are correct.
No test rerun was needed.

## 1. Fixed compact cycle and exact products

The degree \(n=N-1\) kernel is a section of \(O(n,n)\).
Its quotient by the identity kernel is regular on the fixed surface
\(X=(\mathbb P^1)^2\setminus D\); its form has the correct canonical
degree and no poles outside \(D\). The real sphere
\(w=v,z=\bar v\) is disjoint from \(D\), including infinity.
Its orientation gives
\[
 -\frac1{2\pi i}\frac{dw\wedge dz}{(1+wz)^2}
   =\frac{d(\operatorname{area}v)}
           {\pi(1+|v|^2)^2}.
\]
Angular integration and the printed beta integral therefore yield
\(\int_\Gamma\omega_A=\operatorname{Tr}(A)/N\).
The factor \(N\) in kernel composition precisely cancels the
middle beta pairing; no intermediate binomial remains.

The centered star formula is exact. At the origin, its two
derivatives are \(r!\binom nr A_{0r}\) and \(r!B_{r0}\), so
the coefficient \((n-r)!/(r!n!)\) produces \(A_{0r}B_{r0}\).
For the general point, put \(d=1+wz\) and
\[
 g=d^{-1/2}\begin{pmatrix}1&-w\\z&1\end{pmatrix}.
\]
Its column action sends \(b\) to \((z+b)/(1-wb)\);
the dual row action sends \(a\) to \((w+a)/(1-za)\).
The symmetric-power basis with the printed column binomials
therefore gives exactly the stated two centered derivatives.
Both differentiated expressions are finite polynomials of degree
at most \(n\). The square-root sign cancels in conjugation.

## 2. The global rational primitive

The commutator vector fields check directly:
\[
 \sigma_{[J_0,B]}=(w\partial_w-z\partial_z)\sigma_B,\qquad
 \sigma_{[J_-,B]}=(\partial_w+z^2\partial_z)\sigma_B.
\]
For the second identity, acting on the numerator produces
\(\partial_w+z^2\partial_z-nz\); differentiating its denominator
gives exactly the same correction. Both fields are global and
preserve the identity two-form.

The off-diagonal matrix is recovered by division by \(i-j\).
For the diagonal primitive, the \(j\)-th commutator entry is
\((j+1)b_j-jb_{j-1}\); the last entry is correct because the
remaining diagonal has trace zero. Cartan's formula then gives
\[
 d(\sigma_B\iota_V\omega_I)=(V\sigma_B)\omega_I
\]
with the printed sign. Hence the rational primitive is global
on \(X\), and Stokes on the actual compact sphere proves its
zero period. The identity form itself has period one and is
not being declared exact.

## 3. Whole walls and the physical Gauss scale

Summing the truncated binomial kernels gives all three formulas
in Section 4, including the lower-vacuum subtraction
\(-\kappa(1-t)^n\) and upper-head subtraction \(-\delta t^n\).
The latter uses \(n+1=N\), which fixes its coefficient and sign.
Their normalized beta moments and falling-factorial number
moments are exact with the stated factors of \(N\).

The physical principal clock is \(A=e^{2\pi it}\), and \(p=1/w\)
gives the printed balanced Gauss symbols. Direct differentiation
gives
\[
 d\log A\wedge d\log p
       =2\pi i\,\frac{dw\wedge dz}{(1+wz)^2}.
\]
On the real sphere this is \(2\pi\,dt\wedge d\phi\).
Thus the trace measure is precisely the normalized Liouville
measure \(\Omega/(4\pi^2)=dt\,d\phi/(2\pi)\).
The first star commutator has sign
\((1+wz)^2(a_zb_w-b_za_w)/n\); division by
\(h_N=2\pi i/N\) gives the inverse tensor of this same form.
No fixed-root normal has been substituted for \(h_N\).

## 4. Source and asymptotic scope

The original coupon functional equals normalized trace on the
diagonal closed arrays and their number-moment weights, as stated.
It does not equal it on arbitrary off-diagonal Ward insertions.
For those, the exact compact expression would retain the coupon:
\[
 \Phi(A)=\operatorname{Tr}(eA)
       =N\int_\Gamma(\sigma_e\star\sigma_A)\,\omega_I.
\]
This follows immediately from the exact product and trace formulas.
No such replacement is needed for the diagonal arrays considered
in the note.

The fixed algebraic surface and compact cycle are genuine. The
symbol degree and allowed pole order still grow with \(N\);
fixed dimension alone does not provide the bounded presentation
required by the separate cyclotomic reconstruction theorem.
Likewise the finite star formula does not imply a uniform
semiclassical expansion for an arbitrary growing full-word
matrix. The note correctly restricts its Poisson expansion to a
controlled symbol class and leaves the global geometric source
coefficient and its norm unproved.

## 5. The full top cohomology and uniform primitive bounds

The added global cohomology statement also checks. Normalize the
Segre matrix to have trace one:
\[
 \begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
 a+d=1,\quad ad=bc.
\]
Then \(h=2a-1,e=2b,f=2c\) identifies \(X\) with the smooth affine
split quadric \(h^2+ef=1\). Every regular algebraic top form on \(X\)
has finite pole order \(mD\) on the compactification. Since
\[
 \Omega^2_{\mathbb P^1\times\mathbb P^1}(mD)
       =O(m-2,m-2),
\]
it has exactly the displayed kernel form with \(n=m-2\), after
increasing the allowed pole order if necessary. The primitive
therefore proves
\[
 H^2_{\mathrm{dR}}(X)
    =k\left[\frac{dw\wedge dz}{(1+wz)^2}\right].
\]
Its period is \(-2\pi i\), so it is nonzero. This is the fixed
source's rank-one algebraic cohomology; it is not the full knot's
Bloch-regulator period.

For \(G_{jj}=\binom nj^{-1}\), the symbol on \(\Gamma\) is the
normalized \(G\)-expectation in the column
\(c_j=\binom nj\bar v^j\). Hence
\(|\sigma_A|\le\|A\|_G\).
Both primitive matrices actually have bounds independent of \(N\).
For the off-diagonal part the exact integral
\[
 B_{\mathrm{off}}
   =\frac1{2\pi}\int_0^{2\pi}
       i(\theta-\pi)e^{i\theta J_0}Ae^{-i\theta J_0}\,d\theta
\]
has entry \(A_{ij}/(i-j)\) off the diagonal and zero diagonal.
The conjugations are \(G\)-unitary, so
\[
 \|B_{\mathrm{off}}\|_G\le\frac\pi2\|A\|_G.
\]
For the raising part, let
\(s_j=\sum_{k=0}^j(A_{kk}-\tau)\).
Using both the prefix and its trace-zero complementary suffix gives
\[
 |s_j|\le2\min(j+1,n-j)\|A\|_G.
\]
Its weighted shift entry is
\[
 \frac{s_j}{j+1}\sqrt{\frac{j+1}{n-j}},
\]
whose modulus is at most \(2\|A\|_G\). Therefore
\(\|B_{\mathrm{diag}}\|_G\le2\|A\|_G\).
These strengthen the polynomial estimates without changing the
primitive or source.

The qualification is the same-metric one: \(G\) itself is
exponentially conditioned against the original Euclidean basis.
These are uniform bounds for the source contraction in the coherent
metric, not an unproved polynomial comparison with another metric
or a bound on the actual crossing-word norm.

## 6. Fixed-order actual A-period and removal of its normal poles

The subsequent fixed-matrix-size application is also valid.
Use an actual order-\(r\) generic color recurrence and its
companion matrices, fixed initial column \(v_0\), and last-coordinate
row \(\ell\). For
\[
 H_N=A_{N-r}\cdots A_{j_0},\qquad
 R_N^{\mathrm{left}}(q)=v_0(q)\ell H_N(q)
\]
the all-level color theorem gives
\(\operatorname{Tr}R_N^{\mathrm{left}}=\ell H_Nv_0=C_N(q)\).
Applying the coherent calculus at matrix size \(r\), rather
than color size \(N\), therefore gives
\[
 \Omega_N=r\,\omega_{(r,R_N^{\mathrm{left}})},\qquad
 \int_\Gamma\Omega_N=C_N(q).
\]
The surface, cycle and pole-order bound \(r+1\) are independent
of the level. The case \(r=1\) is simply the scalar \(n=0\)
coherent formula.

The whole companion product has poles of order at most the
uniform total leading-germ budget. Write its outer product at
the marked root as
\[
 R_N^{\mathrm{left}}(q)=\sum_{j=-B}^{\infty}R_{N,j}\epsilon^j .
\]
Because \(C_N(q)\) is regular, every negative coefficient has
trace zero. For each such coefficient the global primitive gives
\(\omega_{(r,R_{N,j})}=d_{\mathrm{ext}}\eta_{R_{N,j}}\).
Subtracting
\[
 d_{\mathrm{ext}}\left(
       r\sum_{j=-B}^{-1}\epsilon^j\eta_{R_{N,j}}\right)
\]
therefore removes every normal pole, leaves the period unchanged,
and introduces no division by \(C_N\). In particular this works
at a level where \(K_N=0\). The regularized representative remains
in the same fixed pole-order top-form space.

The order matters for interpreting this pole removal. The alternative
matrix
\[
 R_N^{\mathrm{right}}=H_Nv_0\ell
\]
is already regular entrywise: its column \(H_Nv_0\) consists of
actual Laurent-polynomial colors. The earlier ordering used in this
audit was therefore valid for the period identity but made polar
removal vacuous. In the revised left ordering, nonzero traceless
polar coefficients can occur. The exact difference
\[
 R_N^{\mathrm{left}}-R_N^{\mathrm{right}}
       =[v_0\ell,H_N]
\]
has trace zero, and its global primitive identifies the two
whole period classes without dividing by the selected scalar.
This supplies an explicitly regular representative as well as
the coefficientwise regularization above.

This is a local regularization at the specified root, not a
uniform bounded-height presentation of the growing companion
product. Its rational coefficient degrees and heights can still
grow with \(N\). Conversely, since the coherent matrix size is
now fixed, its metric and primitive bounds do not acquire the
exponential-in-color-size distortion mentioned in Section 5.
Neither fact determines the physical norm or the geometric
comparison.
