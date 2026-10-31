# An exact cap/CROSS convolution with the original MAIN-face demand

The proposed inequality (8) remains open. This note keeps the even-level, original-demand convolution; an unconstrained positive envelope is a different problem.

**Later status, 31 October 2026.** The
[all-demand contraction theorem](research_cap_cross_all_demand_subexponential_contraction.md)
proves the subexponential version of (8), uniformly over every original
remaining degree, and supplies the actual odd-level regularized
comparison. The polynomial factor proposed in (8) remains open.
The [two-spectrum continuation](research_cap_cross_two_spectrum_neighborhood_stability.md)
also controls complex neighborhoods of both endpoints, with a rate
excess tending to zero with their radius. The original internal demand
and incidence hypothesis remain essential to this paired-reference
comparison; the counterexample
in section 4 still rules out arbitrary exterior face demands.

## 1. The actual local source and the demand that must be extracted first

Put \(N=2m\ge4\), \(d=N-1\), \(M=m-1\), and \(\theta=\pi/N\).
Let \(H_N(\sigma)\) denote the original raw cleared numerator and put
\(P_N=(-1)^dH_N(-2)\), its positive endpoint polynomial.

Consider two actual adjacent ports whose specialized ordered quartets are
\[
 E=(A,0,C,Z),\qquad F=(0,A,0,C).
\]
The two zeros in \(F\) are the original distinct protected faces,
specialized to zero. The output triangle \((A,C,Z)\) of \(E\) and input
triangle of \(F\) meet on the ordinary MAIN edge \(AC\).
Restrict \(E\) to its genuine CROSS support and \(F\) to its genuine
RIGHT support. These projections are parts of the original homogeneous
polynomials; they are not asserted to be covariant Casimir coupons.

Assume the ordinary face \(A\) has no incidence outside these two ports.
Its original demand is then exactly \(d\), and must be extracted before
taking a local bound. The unchanged exterior tensor may depend on
\(C,Z\) and other faces, but not on \(A\).

This is a local incidence hypothesis at arbitrary fixed width. For an
explicit check of its original-source typing, it occurs in the certified
seven-port word \([1,3,0,2,4,1,3]\) with the first cap marked.
The protected faces are \(0,6\); take
\[
 E=\text{port }0=(1,0,4,2),\qquad
 F=\text{port }2=(0,1,6,4),
 \qquad (A,C,Z)=(L_1,L_4,L_2).
\]
The [original seven-port dictionary](research_shared_energy_excess_obstruction.md)
shows that face \(1\) belongs only to these ports. No other original
face or target changes.

## 2. Exact coefficients with all unused factors

Set
\[
 a_r=2+2\cos((2r+1)\theta)
       =4\cos^2((r+\tfrac12)\theta),\qquad
 s_r=2\sin(r\theta).
\]
The [actual endpoint tail](research_original_one_sided_four_state_transfer.md)
is
\[
 \begin{aligned}
 K_0&=1,\qquad K_1=s_1^2(A+Z),\\
 K_r&=s_r^2(A+Z)K_{r-1}
       +s_rs_{r-1}a_{r-1}AZK_{r-2}\qquad(r\ge2).
 \end{aligned}
\]
For \(0\le h\le M\), define
\[
 C_{j,h}
 =\left[A^jZ^{d-h-j}\right]K_{d-h}
       \prod_{r=d-h+1}^{d}a_r,
 \tag{1}
\]
with \(C_{j,h}=0\) unless \(0\le j\le d-h\). These are precisely the
coefficients of the positive CROSS endpoint at \(E\):
\[
 P_{E,\mathrm{CROSS}}(A,0,C,Z)
 =\sum_{h=0}^{M}\sum_j
       C_{j,h}A^jC^hZ^{d-h-j}.
 \tag{2}
\]
Every unused row is included in (1). In particular
\(C_{0,0}=N^2\), since
\(\prod_{r=1}^{d}s_r^2=N^2\). The raw \(E\) coupon at \(-2\)
is \((-1)^d\) times (2).

At \(F\), literal row reflection gives
\[
 \begin{aligned}
 H_{F,\mathrm{RIGHT}}(0,A,0,C;2)
   &=\sum_{j=0}^{M}(-1)^jU_jA^{d-j}C^j,\\
 P_{F,\mathrm{RIGHT}}(0,A,0,C)
   &=\sum_{j=0}^{M}V_jA^{d-j}C^j,
 \end{aligned}
 \tag{3}
\]
where
\[
 \begin{aligned}
 U_j&=\csc^2(\theta/2)
       \prod_{r=1}^{j}
       \frac{\sin^2(r\theta)}
            {\sin^2((r+\tfrac12)\theta)},\\
 V_j&=\sec^2(\theta/2)
       \prod_{r=1}^{j}
       \frac{\sin^2(r\theta)}
            {\cos^2((r+\tfrac12)\theta)}.
 \end{aligned}
 \tag{4}
\]
Both are positive. The first is the
[exact flat-cap raw formula](research_flat_cap_no_local_exponential_angular_gap.md).
The second follows by retaining all unused rows at \(-2\) and using
\(\prod_{r=0}^{d}a_r=4\). There is no additional normalization factor.

## 3. The exact original-demand convolution

Define
\[
 \begin{aligned}
 B_N(C,Z)
  &=[A^d]\,H_{F,\mathrm{RIGHT}}(2)
                  H_{E,\mathrm{CROSS}}(-2),\\
 B_N^0(C,Z)
  &=[A^d]\,P_{F,\mathrm{RIGHT}}P_{E,\mathrm{CROSS}}.
 \end{aligned}
 \tag{5}
\]
Both have degree \(d\) in \(C,Z\). Neither has a \(C^d\) term,
because the two original middle degrees are each at most \(M\).
For \(0\le n\le d-1\), put
\[
 J_n=\{j:\max(0,n-M)\le j\le\min(M,n)\}.
\]
Then
\[
 [C^nZ^{d-n}]B_N
   =(-1)^d\sum_{j\in J_n}(-1)^jU_jC_{j,n-j},
 \tag{6}
\]
\[
 [C^nZ^{d-n}]B_N^0
   =\sum_{j\in J_n}V_jC_{j,n-j}.
 \tag{7}
\]
The equality of the two occurrences of \(j\) is forced by the original
\(A\)-face demand \(d\). It is not a new state identification.
Both remaining face degrees stay in the polynomial. Multiplying
\(B_N\) by the untouched exterior tensor and extracting every remaining
original target reproduces the chosen two-port contribution exactly.

The concrete possible elimination lemma is the existence of constants
\(C_0,\kappa<\infty\), independent of \(N,n\), such that
\[
 \boxed{\quad
   \lvert B_N\rvert_{\mathrm{coeff}}
       \le C_0N^\kappa B_N^0
       \quad\text{coefficientwise.}\quad}
 \tag{8}
\]
**Equation (8) is not proved.** Even a proof would address this particular
incidence and support pattern, not every odd MAIN cycle. It would not
permit arbitrary other spectral coupons to be replaced by endpoints.

The two extreme coefficients do admit direct polynomial comparisons.
For \(n=0\), only \(j=h=0\) occurs and the absolute ratio in (6)–(7) is
\(\cot^2(\theta/2)\le N^2\). For \(n=d-1=2M\), only \(j=h=M\)
occurs. Pairing complementary angles gives
\[
 \frac{U_M}{V_M}
 =\prod_{r=0}^{m-1}\cot^2((r+\tfrac12)\theta)=1,
\]
so the absolute ratio is exactly one. These endpoint checks do not
control the interior alternating sums.

## 4. Relaxing the original face demand gives a false inequality

A stronger comparison on every coefficient of the uncontracted product
fails. Extract \(Z^d\) from \(E\): homogeneity forces its unique
monomial \(N^2Z^d\), leaving \(F\) alone on \(A,C\). Thus the ratio of
the absolute coefficient at \(A^{d-j}C^jZ^d\) to the paired endpoint
coefficient is exactly
\[
 \frac{U_j}{V_j}
   =\prod_{r=0}^{j}\cot^2((r+\tfrac12)\theta).
 \tag{9}
\]
For \(N\) divisible by \(8\), \(N\ge16\), choose \(j=N/8\).
Every angle in (9) is at most \(\pi/6\), so this ratio is at least
\(3^{N/8+1}\). No fixed polynomial comparison holds for all
coefficients of the uncontracted pair.

But this exponent has \(A\)-degree \(d-j<d\), and the actual exterior
has no \(A\) incidence. It is absent from the original full coefficient.
Hence (9) is not a counterexample to (8), to an original shared-target
inequality, or to the volume conjecture.

## 5. Exact remaining finite problem

A proof of (8) must control the signed finite convolution (6), including
both summation endpoints. A terminating orthogonality or continuant
identity would have to be derived with the original cutoff and unused
products intact. No such identity is currently established here.

The [two-anchor minimax estimate](actual_coefficient_minimax_upper.md)
and [blockwise source transport](actual_blockwise_sublevel_source_transport.md)
concern unit-factor anchor cores with other clocks fixed. They do not
identify these conditional two-port values with the complete volume.
The [cycle-packing estimate](research_regular_window_cycle_packing.md)
provides loss relative to an envelope and does not prove (8).

A private 80-digit probe evaluated (1), (4), (6), and (7) at five even
levels through \(128\). It is a diagnostic, not an audit or proof, and
is not part of this note's supporting evidence. No rate, universal
polynomial comparison, or theorem for the remaining skeletons is
inferred from those values.

Any proof of (8) must control the original finite constrained sum, not replace it by an unconstrained envelope.