# A full-interval comparison with exact spectral prefix gauges

This note concerns the full original polynomial resolvent numerator, not only its CROSS block. It gives an exact signed factorization on the entire real spectral interval and a coefficient bound in which all possible amplification is assigned to the two original middle incidences. The unused spectral factors remain. The comparison can therefore be inserted into the literal cyclic transfer without changing its targets or grades.

It does not prove a gap for the sewn full-minus-CROSS source. In particular the diagonal factors below need not cancel. The failure of polynomial domination by the same unweighted value at \(-2\) is already proved in actual_cross_cofactor_factorization.md, equations (29)–(32); it is not a new obstruction here.

The inputs checked before this derivation are actual_cross_cofactor_global_angular_gap.md, actual_global_cross_spectral_gap.md, actual_continuous_real_tail_coefficient_positivity.md, actual_global_left_weighted_spectral_envelope.md, actual_terminal_green_capacity_bound.md, and the full unused-row formula in actual_gaussian_resolvent_numerator_and_cap.md. The terminal Green norm in the last cited capacity argument has a different literal adjacent inverse; it is not substituted for the present source.

## 1. The full original numerator

Set
\[
 N\ge2,\qquad d=N-1,\qquad
 s_r=2\sin(\pi r/N),\qquad
 c_r=2\cos((2r+1)\pi/N),\qquad
 \chi_N(z)=2T_N(z/2)+2=\prod_{r=0}^{d}(z-c_r).
 \tag{1}
\]
The repeated factors in the product are retained separately. On degree at most \(d\),
\[
 C(x,y)z^j=c_jz^j-s_j^2(x+y)z^{j-1}
                    -s_js_{j-1}xy z^{j-2},
 \qquad
 V_N(\sigma;C)=\frac{\chi_N(\sigma)-\chi_N(C)}{\sigma-C}.
 \tag{2}
\]
The quotient is a polynomial. The identity \(\chi_N(C)=0\) does not license removing its repeated-root data.

For \(0\le i\le j\le d\), put \(k=j-i\) and
\[
 U_a(\sigma)=\prod_{r=0}^{a-1}(\sigma-c_r),\qquad U_0=1.
 \tag{3}
\]
The actual interval continuant \(P_{ij}\) gives
\[
 V_N(\sigma;C)_{ij}
       =U_i(\sigma)U_{d-j}(\sigma)P_{ij}(\sigma;x,y).
 \tag{4}
\]
Here reflection \(c_{d-r}=c_r\) identifies the second factor with the unused suffix. Formula (4) is a polynomial identity, including every spectral node. No factor depending on \(\chi_N\) is omitted: the interval continuant contains the internal unused rows and (3) contains precisely the exterior rows.

Normalize
\[
 P_{ij}=(-1)^k\left(\prod_{r=i+1}^{j}s_r^2\right)H_{i,k}.
 \tag{5}
\]
Empty products are one.

## 2. Positivity in the spectral distance from \(c_0\)

Define the homogeneous free polynomial
\[
 F_k(x,y)=\sum_{a=0}^{k}x^a y^{k-a}.
 \tag{6}
\]
The exact row identity \(c_0-c_{r-1}=s_rs_{r-1}\) converts the original continuant into
\[
 \begin{split}
 H_{i,0}&=1,\qquad H_{i,1}=x+y,\\
 H_{i,k}&=(x+y)H_{i,k-1}-xyH_{i,k-2}
   +\frac{c_0-\sigma}{s_{i+k}s_{i+k-1}}xyH_{i,k-2}
       \quad(k\ge2).
 \end{split}
 \tag{7}
\]
Only rows \(i+k\ge2\) occur in its last denominator; all those sine products are positive.

Solving the free second-order recurrence gives the division-free-in-\(\sigma\) identity
\[
 H_{i,k}=F_k+
 \sum_{r=2}^{k}
  \frac{c_0-\sigma}{s_{i+r}s_{i+r-1}}\,
          xyF_{k-r}H_{i,r-2}.
 \tag{8}
\]
Induction proves that \(H_{i,k}\), as a polynomial in the three variables \(c_0-\sigma,x,y\), has nonnegative coefficients. This positivity concerns the normalized interval, not the unused exterior products.

Consequently, if \(\beta<c_0\) is real and
\[
                    |c_0-\sigma|\le c_0-\beta,
 \tag{9}
\]
then
\[
             |H_{i,k}(\sigma;x,y)|_{\mathrm{coef}}
                       \le H_{i,k}(\beta;x,y).
 \tag{10}
\]
The notation on the left takes absolute values of the coefficients in \(x,y\). This is stronger than a comparison at positive scalar values. Since \(c_0\ge0\), condition (9) holds on the entire interval \([-2,2]\) whenever \(\beta\le-2\). In particular the short interval above \(c_0\) causes no problem: the positive expansion in \(c_0-\sigma\) controls its coefficient moduli without claiming positivity there.

## 3. Exact factorization and a zero-safe comparison

Use the same baseline at every level:
\[
 \nu_N=N^{-2},\qquad \beta_N=-2-\nu_N,\qquad
 A_a(\sigma)=\frac{U_a(\sigma)}{U_a(\beta_N)},\qquad
 G_a(\sigma)=|A_a(\sigma)|.
 \tag{11}
\]
Every denominator here is a fixed nonzero real number. Zeros of \(U_a(\sigma)\) are retained, not divided out.

For each outer monomial of degree \(k\), define its residual coefficient
\[
 B_{ij,p}(\sigma)=
 \left|U_i(\beta_N)U_{d-j}(\beta_N)\right|
 \left(\prod_{r=i+1}^{j}s_r^2\right)
 [x^p y^{k-p}]H_{i,k}(\sigma).
 \tag{12}
\]
Then the full coefficient has the exact factorization
\[
 [x^p y^{k-p}]V_N(\sigma;C)_{ij}
      =(-1)^d A_i(\sigma)A_{d-j}(\sigma)B_{ij,p}(\sigma).
 \tag{13}
\]
The sign follows from \(i+(d-j)+k=d\). Equations (10) and (12) imply, for every real \(\sigma\in[-2,2]\),
\[
 |B_{ij,p}(\sigma)|\le B_{ij,p}(\beta_N),\qquad
 |[x^p y^{k-p}]V_N(\sigma;C)_{ij}|
 \le G_i(\sigma)G_{d-j}(\sigma)
       |[x^p y^{k-p}]V_N(\beta_N;C)_{ij}|.
 \tag{14}
\]
There is no polynomial or exponential loss in (14).

For \(\sigma\le c_0\), the residual coefficients \(B_{ij,p}\) are nonnegative. Thus the signs are exactly those of the two real prefix polynomials \(A_i,A_{d-j}\), together with \((-1)^d\). For \(c_0<\sigma\le2\), the exact factorization still holds, while (14) bounds the potentially signed residual coefficients.

At even levels one may replace \(\beta_N\) by \(-2\) in (11)–(14), since none of the \(c_r\) equals \(-2\). At odd levels that replacement is invalid. The next section gives a reference that retains the necessary normal at the odd simple node.

## 4. A positive endpoint-plus-first-normal reference at both parities

Let
\[
 \mathcal P_N(u;x,b,c,y)
       =(-1)^d H_{V_N(-2-u)}(x,b,c,y).
 \tag{15}
\]
The original downward-path expansion makes this polynomial coefficientwise nonnegative in all five variables. Each path contributes its positive step weight times a product of \(2+c_r+u\) over its unvisited rows. A row occurs at most once even when two rows have the same spectral value.

The following uniform comparison is exact:
\[
 \mathcal P_N(\nu_N)
 \le_{\mathrm{coef}}
 2\left(\mathcal P_N(0)+\nu_N\mathcal P_N'(0)\right).
 \tag{16}
\]
The derivative is with respect to \(u\), so it is the original first spectral normal with its prescribed minus sign under \(\sigma=-2-u\).

To prove (16), write
\[
 \eta_N=2\operatorname{arsinh}\frac1{2N},
 \qquad \nu_N=2(\cosh\eta_N-1),\qquad N\eta_N\le1.
 \tag{17}
\]
At even levels all \(a_r=2+c_r\) are positive, and
\[
 \prod_{r=0}^{d}\left(1+\frac{\nu_N}{a_r}\right)
       =\frac{\cosh(N\eta_N)+1}{2}
       \le\frac{\cosh1+1}{2}<2.
 \tag{18}
\]
The product over any unused subset is smaller. Hence each path at \(\nu_N\) is at most twice its value at zero.

At odd levels exactly one row has \(a_r=0\). The product over all other rows is
\[
 \prod_{a_r>0}\left(1+\frac{\nu_N}{a_r}\right)
       =\frac{2(\cosh(N\eta_N)-1)}{N^2\nu_N}
       \le2(\cosh1-1)<2.
 \tag{19}
\]
Here \(\prod_{a_r>0}a_r=N^2\), the derivative of \(\chi_N\) at its simple root \(-2\). A path that visits this row is bounded by twice its zero value. A path that leaves it unused contains exactly one zero factor and is bounded by twice \(\nu_N\) times its first derivative at zero. Summing positive paths proves (16).

Thus the baseline in (14) can be bounded by one literal positive tensor
\[
 \mathcal J_N=\mathcal P_N(0)+N^{-2}\mathcal P_N'(0).
 \tag{20}
\]
This is a comparison tensor built from the original endpoint value and normal. It is not a newly defined link invariant. In particular \(\mathcal J_N\) cannot be replaced at odd levels by the value alone: one-sided coefficients vanish there and can have nonzero first normal.

## 5. Complementary gauges have only polynomial cost

For \(0\le a\le d\), reflection gives the exact polynomial identity
\[
 U_a(\sigma)U_{d-a}(\sigma)
                  =\frac{\chi_N(\sigma)}{\sigma-c_a}.
 \tag{21}
\]
The right side means its polynomial quotient, including at \(c_a\). Therefore
\[
 G_a(\sigma)G_{d-a}(\sigma)
 =\frac{|\chi_N(\sigma)/(\sigma-c_a)|}
        {|\chi_N(\beta_N)/(\beta_N-c_a)|}
 \le5N^2,\qquad -2\le\sigma\le2.
 \tag{22}
\]
Indeed \(\|\chi_N'\|_{[-2,2]}\le N^2\), by the elementary Chebyshev derivative bound, and \(\chi_N(c_a)=0\). The mean-value inequality bounds the numerator by \(N^2\). For the denominator,
\[
 N\eta_N\ge\frac1{\sqrt{1+1/(4N^2)}}\ge\frac4{\sqrt{17}},
 \qquad
 |\chi_N(\beta_N)|\ge\frac{16}{17},\qquad
 |\beta_N-c_a|\le\frac{17}{4}.
 \tag{23}
\]
The first inequality follows by integrating the decreasing derivative of \(\operatorname{arsinh}\). The second uses \(2(\cosh t-1)\ge t^2\) at odd levels; at even levels the stronger bound \(4\) holds. Thus the denominator is at least \(64/289>1/5\), proving (22).

This estimate concerns complementary indices at the same spectrum. An arbitrary interface in the original source does not satisfy those two conditions automatically.

## 6. What the comparison does after original sewing

In the literal bipyramid transfer, a row entry has middle exponents
\[
                 a=t_{j-1}-u,\qquad c=v'.
 \tag{24}
\]
Use the original north/south reversal and set the common south variable to one only after total homogeneity has fixed its degree. Formula (13) yields
\[
 T_j(\sigma_j)
   =(-1)^d D_j^{\mathrm{in}}B_j(\sigma_j)D_j^{\mathrm{out}},
 \qquad
 D_j^{\mathrm{in}}(u,v)=A_{t_{j-1}-u}(\sigma_j),
 \quad D_j^{\mathrm{out}}(u',v')=A_{v'}(\sigma_j).
 \tag{25}
\]
Unsupported negative indices can be assigned any diagonal value, since their outgoing rows vanish. The residual matrix satisfies
\[
 |B_j(\sigma_j)|_{\mathrm{entry}}
       \le T_j^+(\beta_N),
 \tag{26}
\]
where \(T_j^+(\beta_N)\) is the nonnegative transfer of \(\mathcal P_N(\nu_N)\). All original states, coefficient targets, and grade changes remain.

The exact intervening diagonal is
\[
 A_v(\sigma_{j-1})A_{t_{j-1}-u}(\sigma_j).
 \tag{27}
\]
Its signs are retained in (25); for spectra at most \(c_0\), they are the previously derived signed seam holonomy. The good/bad masks commute with these diagonal factors. Hence the same factorization applies inside every original finite excursion.

There is also a rigorous positive upper bound for the entire difference. Replace each residual matrix in its exact signed closed-path expansion by \(T_j^+(\beta_N)\), and replace (27) by its absolute value
\[
 W_j(u,v)=G_v(\sigma_{j-1})G_{t_{j-1}-u}(\sigma_j).
 \tag{28}
\]
Sum only closed paths that are not entirely good. The resulting nonnegative weighted path sum bounds \(|\mathscr S-\mathscr S_{\mathrm C}|\), with no extra factor two. Indeed subtracting CROSS removes exactly the all-good paths before the triangle inequality. This retains the same shared ordinary face targets and protected marked jump; it does not replace them by independent local coefficient maximizations.

Replacing each \(T_j^+(\beta_N)\) by the transfer of \(2\mathcal J_N\) gives a further bound with factor \(2^m\). For a fixed diagram this is not exponential in \(N\). It retains the genuine endpoint first normals; no normal is reconstructed from endpoint values.

For an explicit relative formulation, let \(\mathcal M_N(\boldsymbol\sigma)\) be the maximum of the product of (28) over all feasible complementary closed paths in this same transfer. Then
\[
 |\mathscr S(\boldsymbol\sigma)-\mathscr S_{\mathrm C}(\boldsymbol\sigma)|
 \le \mathcal M_N(\boldsymbol\sigma)\,
       \mathscr D_N^+(\nu_N,\ldots,\nu_N).
 \tag{28a}
\]
Here \(\mathscr D_N^+\) is the original shared coefficient of the positive full-minus-CROSS product from (15), with its actual targets. It is nonnegative. Empty path sets give zero. No independent coefficient loads enter \(\mathcal M_N\); it is a maximum-product calculation on the original finite support graph.

Thus, on a source class where an independent near-complete estimate proves \(\mathscr D_N^+(\nu_N,\ldots,\nu_N)\le \exp[N(\Phi-\eta+o(1))]\), a bound \(\limsup N^{-1}\log\mathcal M_N<\eta\) supplies a strict remainder gap on the specified spectral set. This is a precise sufficient transfer statement, not a claim that the gauge inequality holds on the whole cube. Nor does it extend the scope of an existing near-complete theorem to a different diagram class without checking its source identity.

The weights (28) are the remaining obstruction to an unweighted endpoint comparison. Even at an ordinary target \(t=d\), they involve \(v\) and \(d-u\), not generally complementary indices. Neighboring spectra are independent as well. Applying (22) to every interface would therefore be incorrect. At a complementary same-spectrum interface (22) gives a polynomial cost, but no assertion is made that all interfaces of an actual excursion have that form.

## 7. Limitation and a precise quantitative continuation

The known one-sided example uses \(N\) divisible by \(24\), a pure one-step interval with \(i=0\), \(j=N/4-1\), and \(\sigma=\sqrt3\). The tail coefficient for its pure outer monomial is independent of \(\sigma\). Its whole exponential amplification relative to \(-2\) is consequently exactly in the two unused-row factors in (4). The established lower bound is
\[
 \frac{|[x^j c^{d-j}]H_{V_N(\sqrt3)}|}
      {|[x^j c^{d-j}]H_{V_N(-2)}|}
      \ge(3+2\sqrt3)^{N/12}.
 \tag{29}
\]
This explains concretely why the gauges in (28) cannot simply be replaced by a polynomial constant. It does not prove exponential growth of the fully sewn remainder.

Equations (13), (16), and (25) reduce the spectral dependence of a full actual coefficient to explicit prefix polynomials and a residual coefficient bounded by one positive endpoint-plus-normal tensor. They hold on the fixed full interval, including spectral zeros and both parities. Every equality preceding an absolute bound is polynomial, so all required Hermite data remain available by differentiating the whole equality.

A useful next estimate must control the weighted complementary closed paths in (28), or exploit the signed version (27), at the original drilled action with a strict loss. The complementary estimate (22) identifies a legitimate local cancellation of gauge size; it does not justify changing unequal spectra, state indices, or the actual source pairing. No spectral gap or new volume conclusion follows from this note alone.

## 8. Bounded finite checks

The companion md-global-coefficient-prefix-gauge-audit.py constructs the full numerator independently by powers of the literal two-variable Casimir, using the frozen builder in md-shifted-cyclic-excursion-audit.py. It compares that construction with the free-Green expansion (8) and full unused-factor formula (4), without substituting the matrix coefficients into the Green recurrence.

At \(N=2,3,4,7,8,12\), two finite fields and five spectral values per field give 60 exact cases and 6,020 individual coefficient equalities. The construction also checks the original full polynomial resolvent equation. Separate 80-digit real diagnostics check 602 endpoint-plus-normal coefficients, 3,612 tail coefficient comparisons, and 216 complementary gauge products at representative real spectra.

All checks completed. The finite real inequalities are diagnostics only; the proofs of (10), (16), and (22) are the uniform algebraic arguments above. No sewn spectral gap, filling asymptotic, or source-class extension is tested. Results are saved in md-global-coefficient-prefix-gauge-results.json, with both script hashes retained.
