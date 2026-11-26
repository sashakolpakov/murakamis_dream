# Odd neighboring spectra: exact cofactor model and the missing adjugate comparison

This record freezes the inquiry into a fixed physical neighborhood of the neighboring central spectra. It does not extend the proved one-cap theorem. The new elementary conclusion is that stability of every spectral Taylor coefficient is false. A constant adjugate representation remains a plausible, but unproved, way to retain cancellation. The finite fits below are diagnostics, not identities established for all levels.

## 1. The original source and the direction of perturbation

Fix an odd level
\[
 N=2m+1,\qquad d=N-1,\qquad \theta=\pi/N.
\]
All face variables below are those of one original central coupon. Put
\[
 a_r=4\cos^2((r+\tfrac12)\theta),\quad
 s_r=2\sin(r\theta),\quad A=x+y,\quad P=xy,\quad
 \sigma=-2-u.
 \tag{1}
\]
The actual cleared lower polynomials satisfy
\[
 \begin{split}
 R_0(b;u)&=1,\
 R_j(b;u)&=b^j\prod_{r=0}^{j-1}(a_r+u)
       +s_j^2 A R_{j-1}(b;u)
       +s_js_{j-1}(a_{j-1}+u)P R_{j-2}(b;u),
 \end{split}
 \tag{2}
\]
where the last term is absent at \(j=1\). Set
\[
 G_b(u)=R_m(b;u),\qquad D_b(u)=R_{m-1}(b;u).
\]
The original central homogeneous numerator is exactly
\[
 P_C(u)=G_b(u)G_c(u)+u s_m^2xy D_b(u)D_c(u).
 \tag{3}
\]
The second summand is the path that skips the central row. It cannot be omitted from the polynomial or from a spectral normal derivative. In particular
\[
 \partial_u P_C(0)
 =G_b'(0)G_c(0)+G_b(0)G_c'(0)
       +s_m^2xyD_b(0)D_c(0).
 \tag{4}
\]
The original spectral derivative is \(\partial_\sigma=-\partial_u\). These identities retain the original level, polynomial degree, and face variables. They follow from the literal unused-row expansion and the last-row replacement determinant in `actual_cross_cofactor_factorization.md`, Sections 1–3. They do not introduce a new local normalization or an independent face coefficient extraction.

The physical one-sided neighborhood is
\[
 -\epsilon\le u\le0
 \quad\Longleftrightarrow\quad
 -2\le\sigma\le-2+\epsilon.
 \tag{5}
\]
Positive \(u\) lies outside the real spectral cube. An obstruction there does not disprove the required physical extension.

## 2. What is already available, and why it is insufficient

The published `research_cap_uniform_spectral_gap.md` proves an odd-level bound for the original coherent one-cap source when every other spectrum is fixed at \(-2\). The protected cap spectrum itself ranges through the whole real interval. It uses the full extracted stable binary exterior, not the sum of absolute local arrays.

The separate finite calculation in `md-odd-endpoint-spectral-row-count-and-coefficient-cost.md` gives, for \(|u|\le\epsilon\),
\[
 |P_C(u)|_{\mathrm{coef}}
 \le\left(1+\frac{\epsilon}{2s_m^2}\right)
       K_N(\epsilon)^2 P_C(0),\qquad
 K_N(\epsilon)=\frac{\sinh(N\alpha)}{N\sinh\alpha},\quad
 \alpha=\operatorname{arsinh}(\sqrt\epsilon/2).
 \tag{6}
\]
Here the notation means coefficientwise absolute domination before the original shared extraction. In particular the cost is at most
\((1+\epsilon/6)e^{N\sqrt\epsilon}\). This calculation includes the central-skipping term in (3).

Estimate (6) does not bound the signed negative-axis evaluation of the extracted exterior. That evaluation supplies the one-cap cancellation. Replacing it by the absolute coefficient polynomial returns to the known absolute-array obstruction. No neighborhood theorem follows by combining (6) with the endpoint theorem.

The nodal interpolation in `actual_cross_cofactor_global_angular_gap.md` also remains available. It gives exact stable lower-channel determinants multiplied by outer polynomials at physical spectral nodes, and polynomial interpolation costs. However, small distance of the target spectrum from \(-2\) does not make all distant nodal weights exponentially small. Consequently this interpolation alone does not transfer the endpoint's coherent gap.

## 3. Two stability shortcuts that do not work

First, for \(x=y=1\), \(b=c=z\), and \(u>0\), (3) becomes
\[
 P_C(u)=G_z(u)^2+u s_m^2D_z(u)^2.
 \tag{7}
\]
It has a nonreal zero. Indeed \(G_z(u)+i\sqrt u\,s_mD_z(u)\) has degree \(m\), real nonzero leading coefficient, and a nonzero imaginary coefficient of lower degree. If all its zeros were real, its monic normalization would have real coefficients, a contradiction. Thus the whole polynomial cannot be real stable throughout a two-sided spectral neighborhood. This observation concerns \(u>0\), not (5).

Second, the recurrence determines a high Taylor coefficient exactly:
\[
 [u^{m-1}]G_b(u)
 =b^{m-2}\left(Nb^2+s_m^2(x+y)b+s_ms_{m-1}xy\right).
 \tag{8}
\]
To verify it, the inhomogeneous term of (2) contributes
\(b^m\sum_{r<m}a_r\), the one-step term contributes
\(s_m^2(x+y)b^{m-1}\), and the two-step term contributes
\(s_ms_{m-1}xyb^{m-2}\). The finite cosine sum gives
\(\sum_{r<m}a_r=N\).

For \(x=y=1\), the discriminant of the quadratic in (8), divided by four, is
\[
 s_m^4-Ns_ms_{m-1}<0\qquad(N\ge7,\ N\ {
m odd}).
 \tag{9}
\]
For an elementary bound, write \(t=\pi/(2N)\). Then
\(s_m=2\cos t\), \(s_{m-1}=2\cos3t\), and
\(s_m^3\le8\). Since \(N\ge7\),
\[
 \cos3t\ge1-\frac{9\pi^2}{8N^2}
 >1-\frac{90}{392}>\frac34,
\]
so \(Ns_{m-1}>3N/2>8\). This proves (9). Hence not every spectral Taylor coefficient is real stable. The offending order grows with \(N\); this does not refute a theorem controlling low defects and an exponentially bounded high-defect remainder.

The independently preserved `md-odd-lower-cofactor-hard-edge-obstruction.md` proves that \(D_b(0)\) itself has unboundedly many nonreal roots along large odd levels. That also does not rule out a bounded signed sum of stable compression determinants.

## 4. The exact positive matrix and a concrete missing identity

Define \(m\)-by-\(m\) Hermitian matrices \(H_+,H_-\) as in the actual q-Hahn determinant proof. Their common diagonal is
\[
 (H_\pm)_{jj}=\frac1{\cos(j\theta)\cos((j+1)\theta)},
 \qquad0\le j<m,
 \tag{10}
\]
and, for \(1\le j<m\), their upper adjacent entries are
\[
 (H_\pm)_{j-1,j}
 =\sqrt{\beta_j}\bigl(\sin(j\theta)\pm i\cos(j\theta)\bigr),
 \quad
 \beta_j=\frac{\sin^2(j\theta)}
 {\cos^2(j\theta)\sin((2j-1)\theta)\sin((2j+1)\theta)}.
 \tag{11}
\]
The lower entries are the conjugates. Both matrices are positive definite. The original endpoint identity, with its scalar retained, is
\[
 G_b(0)=N\det M(b,x,y),\qquad
 M=bI+\frac x2H_-+\frac y2H_+.
 \tag{12}
\]
The proposed next identity is the following constant-matrix representation:
\[
 \boxed{\quad
 \frac{D_b(0)}N
   =\operatorname{Tr}\bigl(W_N\operatorname{adj}M(b,x,y)\bigr),
 \qquad W_N=W_N^*,\qquad \|W_N\|\le N^{O(1)}.
 \quad}
 \tag{13}
\]
Neither the all-level identity nor its norm bound has been proved in this inquiry. The matrix must be independent of \(b,x,y\). A solution separately chosen at each positive evaluation would not suffice.

The reason for seeking (13) is exact. For a unit vector \(v\),
\[
 v^*\operatorname{adj}M\,v
 =\det(M|_{v^\perp}),
 \tag{14}
\]
where the right side is the compression in an orthonormal basis of the fixed subspace \(v^\perp\). Its coefficient matrices are positive semidefinite, so it is a stable determinant. A Hermitian spectral decomposition of \(W_N\) would make (13) a signed sum of at most \(m\) such determinants. Its total coefficient cost would be at most \(m\|W_N\|\). Equivalently, off-diagonal adjugate entries have the usual four-term polarization by vector compressions. This does not require \(D_b(0)\) itself to be stable.

Even (13) would be an intermediate result. The first normal (4) also contains \(G_b'(0)\), and a fixed neighborhood requires control of all relevant defect orders, their original shared degree constraints, and the final coherent extracted polynomial. No such multi-defect estimate is asserted here.

## 5. What the retained diagnostic computes

`md-odd-lower-cofactor-adjugate-probe.py` constructs the full coefficient system for (13), restricted to real symmetric \(W_N\). The variables are \(b,A=x+y,P=xy\), with weights \(1,1,2\). It includes every monomial of total weighted degree \(m-1\), not just evaluations at \(x=y\).

For an interval of the tridiagonal matrix, the determinant recursion is
\[
 \Delta_{\ell,j+1}
 =\left(b+\frac{A}{2\cos(j\theta)\cos((j+1)\theta)}\right)
      \Delta_{\ell,j}
 -\beta_j\left(\frac{A^2}{4}-P\cos^2(j\theta)\right)
      \Delta_{\ell,j-1}.
 \tag{15}
\]
For an off-diagonal adjugate entry the script multiplies the left and right interval determinants by the intervening off-diagonal chain. It takes the real part by replacing even powers of \(y-x\) with \((A^2-4P)^{k}\). The target is constructed independently from recurrence (2).

The script scales each coefficient equation by the largest absolute coefficient in that row, and then uses double-precision least squares with cutoff \(10^{-13}\). The retained full-space results are:

| \(N\) | coefficient rank | largest scaled residual | fitted operator norm |
|---:|---:|---:|---:|
| 5 | 2 | \(1.2\cdot10^{-16}\) | 0.832 |
| 7 | 4 | \(3.4\cdot10^{-16}\) | 1.543 |
| 9 | 6 | \(4.9\cdot10^{-16}\) | 2.485 |
| 11 | 9 | \(8.9\cdot10^{-16}\) | 3.656 |
| 13 | 12 | \(3.3\cdot10^{-15}\) | 5.060 |
| 17 | 20 | \(2.5\cdot10^{-15}\) | 8.568 |
| 21 | 30 | \(4.7\cdot10^{-15}\) | 13.011 |

The rank is the full number of coefficient equations in these cases. Thus fitting is not particularly selective: this space can fit many targets. No inference of an exact identity, polynomial norm bound, or stability follows from the residuals. The norm trend only motivates seeking an analytic formula.

Two simpler restricted spaces were also tested: matrices commuting with the real matrix \((H_-+H_+)/2\), and real parts of matrices diagonal in an \(H_+\) eigenbasis. Their residuals are already positive at \(N=7\), and grow in these samples. These are numerical failures of the proposed restricted fits, not all-level impossibility theorems.

## 6. Independently evaluated finite identities

`md-odd-lower-cofactor-adjugate-check.py` was executed at 90 decimal digits. At \(N=5,7,9,13\), and three positive/boundary triples \((x,b,y)\) at each level, it compared:

1. recurrence (2) with the determinant of the literal triangular Casimir block after replacing its last row by \((1,b,\ldots,b^j)\), for \(j=m-1,m\);
2. \(G_b(0)/N\) with the independent positive Hermitian determinant (12).

All 12 evaluations agree to relative error below \(7.6\cdot10^{-91}\). It also checks the sign in (9) at four representative levels. These finite calculations guard the normalization and orientation of the model used by the probe. They are not proofs of (13) or of any asymptotic statement.

The original probe and its stdout, the independent-check script and JSON, and the present source are hashed in the companion manifest. Earlier unsaved exploratory calculations are not part of the evidentiary record.

## 7. Exact remaining task

The next constructive step is an all-level formula for \(W_N\) in (13), or a different source-exact signed compression representation with a controlled normalization. It should explain why the coefficients remain small despite the ill-conditioned high-degree coefficient map. A q-Hahn boundary/displacement identity is a possible route; no such identity has yet been derived.

If that first step succeeds, the neighboring-spectrum theorem still requires an expansion of the actual \(u\)-dependent cofactors, including the central-skipping term, whose total cost is \(e^{o_\epsilon(1)N}\) while preserving coherent shared extraction. A coefficientwise positive bound alone, an unconstrained matrix fit, or a pointwise stable surrogate does not supply this.

The proved odd uniform one-cap result therefore remains unchanged: all other spectra are fixed at \(-2\). No even-level extension, fixed neighboring neighborhood, multi-cap theorem, full filling theorem, or new volume equality is claimed in this record.
