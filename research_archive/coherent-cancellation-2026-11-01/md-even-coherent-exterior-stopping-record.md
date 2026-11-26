# Even central exteriors: bounded stopping record

1 November 2026. This inquiry ends without an even cancellation theorem
and without a counterexample for a globally extracted exterior. All
artifacts are private. No publication source, manuscript or guide was
changed.

## 1. The precise open implication

At level \(N=2m\), put \(d=N-1\), \(M=m-1\),
\[
 a_j=2+2\cos((2j+1)\pi/N),\qquad s_j=2\sin(j\pi/N).
\]
The original cleared cofactor recurrence is
\[
 R_j(b)=b^j\prod_{r<j}a_r+
 s_j^2(x+y)R_{j-1}(b)+
 s_js_{j-1}a_{j-1}xyR_{j-2}(b),\qquad R_0=1 .
\]
With \(D_b=R_M(b)\), \(E_b=a_MR_{M-1}(b)\), the sign-adjusted raw
central numerator is exactly
\[
 P_C=4(x+y)D_bD_c+
 s_ms_{m-1}xy(D_bE_c+E_bD_c).
 \tag{1}
\]
The level and all finite scalars are retained. There is no replacement
by the nearest physical node.

For one original protected singleton, form the product of the other
central numerators, set the two protected faces to zero, and extract
degree \(d\) at every ordinary face except the two boundary variables
\(A,C\). The remaining homogeneous polynomial \(P_N(A,C)\) has
degree \(d\). The question is whether its negative-axis values admit
an estimate strong enough to replace the real-stability input in the
odd cap argument.

The complete read of research_even_cross_stability_obstruction.md
confirmed that its obstructions are local. Its level-six specialization
has discriminant
\[
                     -6000+3456\sqrt3<0,
\]
and its shorter level-eight cofactor is also nonstable. Neither
calculation performs the exterior extraction above. Conversely, the
exact stable reference \(Q_N\) satisfies
\[
 Q_N\le_{\rm coef}P_N\le_{\rm coef}3^{R-1}Q_N,
\]
but this does not compare the two polynomials on a negative axis.
The source note's elementary positive-polynomial example proves that
even exponentially sharp coefficient comparison is insufficient.

The finite sine-Cauchy spectral bound and its cutoff degrees work at
both parities. The additional alternating-section estimate in
research_cap_uniform_spectral_gap.md requires a positive linear-factor
decomposition of the actual binary exterior. The common-axis and
Dirichlet response criteria likewise retain that input. A common
positive-pressure limit alone does not supply it.

## 2. Completed original-target tests

Two exact coefficient engines were written, at \(N=6\) and \(N=8\).
They start from the original recurrence and (1). At \(N=6\) all
coefficients lie in \(\mathbb Z[\sqrt3]\). At \(N=8\) they lie in
\(\mathbb Z[t]/(t^4-4t^2+2)\), with
\[
 t=\sqrt{2+\sqrt2},\qquad
 \sqrt2=t^2-2,\qquad
 \sqrt{2-\sqrt2}=t^3-3t .
\]
Field signs are evaluated exactly: a squared-integer comparison at
level six, and rational isolating intervals obtained by integer square
roots at level eight.

Each input retains an oriented simple sphere, a perfect dual matching,
and its actual quartet order. The selected mark is the nonmatching
edge \(by\) of the anchor quartet \((x,b,z,y)\). Its protected variables
are \(L_b=L_y=0\), and the two unextracted ordinary variables are
\(A=L_z\), \(C=L_x\). The code checks opposite edge orientations,
Euler characteristic two, and a connected degree-two link at every
vertex. All other face demands are exactly \(d\). Coefficients are
multiplied and extracted using integer field arithmetic; no positive
radius approximation or independently summed local boundary is used.

The completed set at each of the two levels contains:

- 74 marked matching instances on the tetrahedron, one- and two-stellar
  refinements, and octahedron;
- 234 marked matching instances on twelve fixed generated spheres,
  with \(R=5,6,7,8\), using three recorded matchings per sphere.

The generated spheres and every tested matching, quartet, cap and
coefficient vector are preserved in the result files. The seed is
fixed; the legal flips and spheres are checked before extraction.
Repeated equivalent instances have not been removed. These are finite
diagnostic cases, not a claim of exhaustive coverage of those sizes.

For \(P_N(A,C)=\sum_{j=0}^d p_jA^jC^{d-j}\), every tested vector
satisfied the exact necessary Newton inequalities
\[
 j(d-j)p_j^2\ \ge\
 (j+1)(d-j+1)p_{j-1}p_{j+1},
 \qquad 1\le j\le d-1.
 \tag{2}
\]
Numerical root location found no off-real roots in the tested
polynomials. This latter calculation is explicitly a locator, not a
certified root count. Equation (2) alone does not prove real-rootedness.
Thus the test produced no exact extracted-stability obstruction and
no new stability theorem.

## 3. What remains unproved

No exact odd/even contiguity map was constructed. Changing the level
changes the root, original degree, endpoint factors and every shared
face demand, so the odd factorization cannot be substituted into the
even source. The same-level nearest-node comparison retains the
demands but loses negative-axis signs.

No subexponential negative-axis comparison
between the actual even exterior and its stable reference was proved.
No finite-degree root test here establishes such an asymptotic estimate.
The known local nonreal roots also do not disprove it.

Accordingly, the even analogue of the actual signed cap estimate
remains open in this record. No all-real-spectra statement, even source
gap, filling theorem or new knot-volume class follows. The earlier
both-parity absolute-array lower bound is a separate result and is
unchanged.

## 4. Artifacts and exact reading scope

The four scripts are:

- md-even-coherent-exterior-check.py;
- md-even-coherent-exterior-n8.py;
- md-even-coherent-exterior-locate.py;
- md-even-coherent-exterior-n8-locate.py.

Their four result files use the same stems, with check-results,
n8-results, locating-results and n8-locating-results respectively.
They record exact field coefficients; numerical root locations are
labeled separately. The final replay repeated only the already
completed cases to preserve their records, without extending the
test set.

The new engines use the written local recurrence. They are not an
independent reconstruction of the physical coproduct/source adapter.
No new topology of a filled knot or primitive filling was checked.
The source interpretation is the existing matched-sphere compiler.

The current pass read the even stability obstruction completely,
reopened the exact central factorization and half-block normalization,
and checked the finite and asymptotic hypothesis interfaces of the
cap uniform, common-axis and Dirichlet notes. It did not reprove all
their imported coefficient, response or metric theorems. The retained
private shorter-cofactor and five-term reports were consulted to avoid
repeating their already known obstructions. The source and artifact
hashes are in the accompanying snapshot.
