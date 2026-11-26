# A positive reciprocal integral for the original Conway quartic

23 November 2026. Research proof. Earlier finals and public manuscripts
remain unchanged.

Supersedes [the initial version](research_conway_reciprocal_quartic_source_formula.md).

The actual normalized source has a positive integral which approximates
its reciprocal squared modulus with a uniform relative error. A known
polynomial damping of the original closing row suffices. Neither a
minimizer, its Hessian determinant, nor a chosen temperature is input.
The proof uses the triangular residual map and a fixed residual ball.
It does not evaluate the integral from hyperbolic geometry.

## 1. The original physical source and the integral

Use the complete physical compiler of [P]. At level \(N\ge2\), every
proper packet belongs to its full \(N\)-dimensional complex physical
algebra, with the uniform Hilbert--Schmidt metric. This retains the
first derivatives at double Casimir roots. Fix a literal expression
with \(s\ge1\) proper vertices, and put \(D=Ns\), \(m=D+1\).
Choose physical orthonormal coordinates on their direct sum
\(\mathbb C^D\); \(dx\) means real Lebesgue measure in these coordinates.

Keep [P]'s known budgets and their positive product \(B\).
Each normalized leaf has norm at most \(\sigma=1/16\); turns and the
original closing row have operator norm at most \(\sigma\); products
have bilinear norm at most \(\sigma\). No small coefficient-tensor
Hilbert--Schmidt norm for constant-budget physical multiplication is
assumed. Write \(c\) for the normalized original row, extended by zero
off the top packet, and
\[
 G_v(x)=\Phi_v((x_j)_{j\text{ child of }v})-x_v,\qquad
 G(a)=0,\qquad k=ca=K_N/B,\qquad |k|\le\sigma^2.
 \tag{1}
\]
Here \(a\) is the exact forward field. It is used in the proof, not
supplied to define the integral. All original phases, turns, markings,
and prescribed short-filling packets remain in the known coefficients.

For \(0<\varepsilon\le1\), damp only the closing row and record the
compensating budget:
\[
 E_\varepsilon(x)=\|G(x)\|^2+\varepsilon^2|cx|^2,\qquad
 B_\varepsilon=B/\varepsilon,\qquad k'=\varepsilon k.
 \tag{2}
\]
The base \(E_\varepsilon\) has degree at most four. Define the extended
nonnegative integral
\[
 \mathcal P_\varepsilon=
       \frac{D!}{\pi^D}\int_{\mathbb C^D}
                             E_\varepsilon(x)^{-D-1}\,dx .
 \tag{3}
\]
The exponent grows with \(D\): the rational integrand does not have
bounded total degree. For the rational damping used below, its base
coefficients are algebraic at each level for the original finite source.
The normalization \(\pi^{-D}\) is explicit; no assertion about an
algebraic period class is needed.

**Theorem.** Take the known damping \(\varepsilon=m^{-3}\), and put
\(\delta=m^{-2}\). If \(K_N\ne0\), the integral is finite and positive,
and
\[
 \left||k'|^2\mathcal P_\varepsilon-1\right|\le\delta,\qquad
 (1-\delta)\frac{B_\varepsilon^2}{\mathcal P_\varepsilon}
 \le |K_N|^2\le
 (1+\delta)\frac{B_\varepsilon^2}{\mathcal P_\varepsilon}.
 \tag{4}
\]
If \(K_N=0\), then \(\mathcal P_\varepsilon=+\infty\); with
\(1/(+\infty)=0\), the two source inequalities remain exact at zero.
There is no parity or nonvanishing assumption in this convention.

## 2. Source-exact residual coordinates and a local bound

Order children before parents. The inverse of \(G\) is the finite
polynomial recursion
\[
 x_v=\Phi_v((x_j)_j)-r_v,\qquad
 \det_{\mathbb C}DG=(-1)^D,\qquad |\det_{\mathbb R}DG|=1.
 \tag{5}
\]
Thus \(G\) is a global polynomial automorphism. This is the residual
change already used in [R], now in the physical coordinates of [P].
Let \(H=G^{-1}\) and \(f_\varepsilon(r)=\varepsilon cH(r)\).
Then (3) is exactly the same integral with denominator
\(\|r\|^2+|f_\varepsilon(r)|^2\).

Fix \(\rho=1/4\). For \(\|r\|\le\rho\), upward induction in (5)
gives \(\|H(r)_v\|\le\sigma+\rho=5/16<1\).
Indeed a leaf is bounded by \(\sigma+\rho\); a turn or product of
previously bounded inputs has norm at most \(\sigma\), before
subtracting \(r_v\). This also covers prescribed constant leaves.

On these packet balls write \(DG=-I+A\). Each child enters one
parent row and each row has at most two children, so
\(\|A\|\le\sqrt2\sigma\le1/8\) and \(\|DH\|\le8/7\).
Only products contribute to \(D^2G\). At one product the two terms
are \(\Phi(h_L,k_R)+\Phi(k_L,h_R)\). Cauchy--Schwarz on that
pair, followed by disjointness of sibling pairs, proves
\[
 \|D^2G[h,k]\|\le\sigma\|h\|\|k\|,\qquad
 \|D^2(cH)\|\le\sigma^2(8/7)^3<1.
 \tag{6}
\]
The second inequality follows by twice differentiating \(G(H(r))=r\);
there are three factors of \(DH\) and one of \(D^2G\).
No dimension factor or unknown source value occurs.

Taylor's formula on the residual ball consequently gives
\[
 f_\varepsilon(r)=k'+d'r+p(r),\qquad
 d'=Df_\varepsilon(0),\qquad
 |p(r)|\le\frac{\varepsilon}{2}\|r\|^2 .
 \tag{7}
\]
These are holomorphic derivatives, equivalently their real variations.

## 3. The affine reciprocal and both tails

Suppose first that \(k'\ne0\), and put
\(E_{\rm aff}(r)=\|r\|^2+|k'+d'r|^2\).
Completing the Hermitian square uses
\(A_0=I+d'^*d'\), whose determinant is \(1+\|d'\|^2\).
The remaining constant is \(e_0=|k'|^2/(1+\|d'\|^2)\).
Radial integration after this linear change gives
\[
 \frac{D!}{\pi^D}\int_{\mathbb C^D}E_{\rm aff}^{-D-1}\,dr
       =\frac1{e_0\det A_0}=\frac1{|k'|^2}.
 \tag{8}
\]
For example, the radial substitution reduces the scalar integral to
\(\int_0^\infty t^{D-1}(t+e_0)^{-D-1}dt=1/(De_0)\).
The last equality follows by \(u=t/(t+e_0)\).
Thus the affine slope cancels exactly, not approximately.

Both residual energies dominate \(\|r\|^2\). For either one, the
normalized integral outside the fixed ball is bounded by
\[
 \frac{D!}{\pi^D}\int_{\|r\|>\rho}\|r\|^{-2D-2}\,dr
                         =\frac D{\rho^2}=16D.
 \tag{9}
\]
This controls the entire nonlinear exterior without a large-field
estimate for \(H\). If \(k'\ne0\), the energy has no zero: a zero
would require \(r=0\) and \(f_\varepsilon(0)=k'=0\).
Continuity on the remaining compact ball proves finiteness of (3).

## 4. Uniform relative error without a source lower bound

On \(\|r\|\le\rho\), (7) gives
\[
 |p(r)|\le(\varepsilon/8)\sqrt{E_{\rm aff}(r)},\qquad
 (1-\varepsilon/8)^2E_{\rm aff}
 \le\|r\|^2+|f_\varepsilon(r)|^2
 \le(1+\varepsilon/8)^2E_{\rm aff}.
 \tag{10}
\]
This follows by applying the triangle and reverse triangle inequalities
to the augmented vector \((r,k'+d'r)\).
Since \(-\log(1-t)\le t/(1-t)\), the relative integrand error is at most
\(\exp[(2/7)m\varepsilon]-1\). Indeed \(t=\varepsilon/8\le1/8\)
and the exponent of each square is \(-m\).
Comparing the two inside integrals, then using both tails (9), proves
\[
 \left||k'|^2\mathcal P_\varepsilon-1\right|
 \le \exp[(2/7)m\varepsilon]-1+32D|k'|^2.
 \tag{11}
\]
No lower bound on \(|k'|\) has been used.

For \(\varepsilon=m^{-3}\), one has \(|k'|\le\varepsilon/256\).
Writing \(a=(2/7)m^{-2}\), the elementary series bound
\(e^a-1\le a/(1-a)\) gives
\[
 e^a-1\le\frac25m^{-2},\qquad
 32D|k'|^2\le\frac{D}{2048m^6}\le\frac1{2048}m^{-2}.
 \tag{12}
\]
Their sum is less than \(\delta=m^{-2}\). Multiplication by
\(B_\varepsilon^2/\mathcal P_\varepsilon\) proves (4).
More generally (11) with any fixed integer damping
\(\varepsilon=m^{-p}\), \(p>1\), gives relative error \(O(m^{1-p})\).

If \(k'=0\), holomorphy gives \(f_\varepsilon(r)=O(\|r\|)\) near zero.
The energy is therefore at most \(C\|r\|^2\) there, and its integral
dominates a positive constant times \(\int_0^\rho t^{-3}dt\).
It diverges, proving the stated zero convention.

## 5. Temperatures, normalization, and the remaining geometric task

For \(t>0\), define
\(Z_\varepsilon(t)=(t/\pi)^D\int e^{-tE_\varepsilon(x)}dx\).
Residual coordinates show \(0<Z_\varepsilon(t)\le1\).
Tonelli and the elementary scalar Gamma integral give the exact identity
\[
                  \mathcal P_\varepsilon
                         =\int_0^\infty Z_\varepsilon(t)\,dt .
 \tag{13}
\]
This also holds as an extended nonnegative equality at a source zero.
All temperatures are integrated; the intrinsic small-source scale
has not disappeared from the value of the integral.

For a fixed expression \(D=Ns\), (4) has relative error \(O(N^{-2})\).
The extra budget \(m^3\) is polynomial and explicitly restored.
This improves the previous constant-factor minimum comparison to a
relative reciprocal-integral comparison, including arbitrarily small
nonzero sources. Unlike [L], no selected temperature, minimum or
Gaussian determinant is needed. The argument uses only the bilinear
physical bounds; [R]'s coefficient-Hilbert--Schmidt determinant theorem
is not transferred to a different metric.

The original signed closing is still inside \(E_\varepsilon\).
Neither positivity nor (13) evaluates the integral at a hyperbolic-volume rate.
No geometric source coefficient, arbitrary-short-filling volume
theorem, or finite-exception result follows.

## Complete inputs and coverage

All four complete matching texts were read; [P] is the source input,
and [C], [R], [L] locate the preceding constructions. Only written
mathematics and text/hash operations were used.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| P, 477 lines | [Uniform physical source](research_conway_uniform_physical_quartic.md) | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| C, 329 lines | [Normalized convex source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| R, 265 lines | [Residual Jacobian and Gaussian determinant](research_conway_residual_jacobian_gaussian_determinant.md) | db22b86a97302926fed77385f82ff2284109e288ec3d03dd99538d3671c926b2 |
| L, 257 lines | [Uniform growing-level Laplace comparison](research_conway_uniform_growing_level_laplace.md) | 98e509be87f5445b43400df8341c8d902cab2ac9206c49ec248427dc32099e6f |

