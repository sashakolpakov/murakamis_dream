# Analytical check of the coupled protected spectral bound

The checked draft is
\(\texttt{md-protected-coupled-spectral-polynomial-bound.md}\),
SHA256
\(\texttt{03c01d8f819d01cc1ed4fc26c614eeaafdb6e518a4bf07f027dbc9fd94466df8}\).
This record concerns its finite matrix identity, density bound, and
finite-degree comparison. It does not certify a spectator-energy or
geometric-volume estimate.

## 1. Cutoff and self-adjointness

The genuine one-sided cutoff is \(M=\lfloor N/2\rfloor-1\). At odd
\(N=2m+1\), the central \(j=m\) row belongs to the complete crossing
sector, so it is not part of this one-sided vector. Consequently
\(2M=N-2\) at even levels and \(2M=N-3\) at odd levels.

For the sine-Cauchy matrix,
\[
 C_{ij}=\frac{\sin\theta}{\sin((i+j+1)\theta)},
 \qquad
 A_{jj}=2\cos((2j+1)\theta),\quad A_{j,j-1}=4\sin^2(j\theta),
\]
the \((i,j)\) entry of \(AC-CA^T\) reduces, for \(i+j>0\), to
\[
 \sin\theta\left[
 \frac{-4\sin((i+j+1)\theta)\sin((i-j)\theta)}
      {\sin((i+j+1)\theta)}
 +\frac{4\sin((i+j)\theta)\sin((i-j)\theta)}
      {\sin((i+j)\theta)}\right]=0.
\]
When one index is zero the corresponding subdiagonal coefficient is
zero, and this same formula remains valid. At \(i=j=0\), the equality
is direct. The allowed cutoff keeps all denominators away from their
zero endpoints.

Thus \(C^{-1}A=A^TC^{-1}\). The eigenvalues \(c_0,\ldots,c_M\) are
distinct and lie in \([-2,2]\). The full polynomial
\(\chi_N=2(T_N(\sigma/2)+1)\) vanishes on this matrix, although
\(\chi_N\) itself has repeated roots. The polynomial divided difference
\[
 q_\sigma(z)=\frac{\chi_N(\sigma)-\chi_N(z)}{\sigma-z}
\]
therefore gives \(g=U_0^{-1}q_\sigma(A)e_0\) by the original lower
bidiagonal recurrence and polynomial continuation. Its operator norm in
the \(C^{-1}\) metric is at most \(N^2\), using
\(\sup_{[-2,2]}|\chi_N'|\le N^2\). No unresolved resolvent pole appears
at a spectral node.

## 2. Density comparison

For a beta variable \(Y_a\) with parameters \((a,1/2)\),
\[
 f(a)=\mathbb E\log Y_a
 =-\int_0^\infty\frac{e^{-at}}{1+e^{-t/2}}\,dt,
 \quad f'(a)=\operatorname{Var}(\log Y_a)\le a^{-2}.
\]
The mean difference for a ratio in the draft has parameter separation
\(3/2\). Since \(kN-1/2\ge5kN/6\), both its positive mean and its
variance are less than \(3/(kN)^2\). Summing both copies gives the stated
\(12/N^2\) bounds.

Removing the independent inverse-beta factor decreases the variance.
The new mean lies between \(-1/(N-1/2)\) and \(12/N^2\), so its absolute
value is at most \(4/N\) for \(N\ge3\). Chebyshev displacement \(8/N\)
has failure probability at most \(12/64<1/4\), and the claimed
\(\pm24/N\) events safely contain these intervals.

The product of the two initial beta variables has density
\[
 \frac14\int_y^1\frac{dx}{\sqrt{x}\sqrt{1-x}\sqrt{x-y}}
 \ge\frac{\pi}{4}.
\]
Conditioning on \(|\log G|\le24/N\) therefore proves the first density
range. For the other range, each initial beta variable lies in
\([e^{-60/N},e^{-50/N}]\) with probability at least
\(5e^{-20}/N\). On those events and the independent \(G_*\) event,
\[
 e^{-144/N}\le R\le e^{-76/N}.
\]
For \(a=N-1/2\), the conditional density of \(R/A_{1,1}\) is
\[
 \frac{R^a}{B(a,1/2)}t^{-a-1}(1-R/t)^{-1/2}.
\]
Here \(B(a,1/2)\le2\), \(R^a\ge e^{-144}\), and \(t>R\) on the
range used. This gives the coefficient
\((75/8)e^{-184}N^{-2}\) before \(t^{-N-1/2}\), which is stronger
than the claimed \(e^{-200}N^{-2}\).
The two density ranges cover the whole positive half-line.

## 3. The finite-degree tail

The elementary polynomial supremum inequality on \([0,1]\) gives
\(\|q\|_\infty^2\le(M+1)^2A_0\).
For \(\delta=1/[2(M+1)^2]\), at most half of \(A_0\) lies below
\(\delta\). Hence \(A_1\ge A_0/[4(M+1)^2]\), and
\(\|q\|_\infty^2\le4(M+1)^4A_1\). Integrating \(t\|q\|_\infty^2\)
below \(\delta\) again gives at most \(A_1/2\).
These are precisely the two cases needed for
\[
 A_\alpha\le2\sqrt2(M+1)A_{\alpha+1/2},
 \qquad \alpha=0,1.
\]

For the reversal \(q(t)=t^Mp(1/t)\), the two exterior tail exponents
become \(N-2M-2\) and \(N-2M-3/2\), respectively. The first is
exactly \(0\) or \(1\), so the preceding inequalities apply. Combining
the interior and exterior integrals loses only their maximum constant,
not their sum. It yields
\[
 H\succeq
 \frac{e^{-200}}{2\sqrt2(M+1)N^2}\,C.
\]
Inverting positive matrices and inserting the self-adjoint spectral
bound proves the stated \(e^{210}N^5\) estimate. The argument applies to
complex spectator coefficient vectors as well.

This proof depends on the original cutoff and the exact coupled Gram
matrix. It is not an entrywise comparison, a tensor-product norm bound,
or a geometric comparison for the remaining energy.

