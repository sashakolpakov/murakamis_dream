# The original undamped Conway quartic has a reciprocal source integral

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

The original physical quartic needs no damping of its closing row for
a reciprocal-integral comparison at exponential scale. Its positive
integral approximates the reciprocal squared source with a universal
relative error, independent of the level, tree size and leaf packets.
No minimizer, temperature, or Hessian determinant is input.

The addition to [R] is removal of its level-dependent damping and
compensating budget. The original objective and budgets are retained.
The comparison here has a fixed error, whereas [R]'s damped formula
has a relative error tending to zero. Neither formula evaluates its
integral from geometry.

## 1. The unchanged source and the statement

Use [P]'s literal physical compiler at every integer level \(N\ge2\).
Every proper packet lies in the full algebra
\[
 \mathcal A_N=\mathbb C[\Omega]\subset
       \operatorname{End}(V_N\otimes V_N),\qquad
 \|F\|_{\rm ph}^2=\operatorname{Tr}(F^*F),\qquad
 \dim_{\mathbb C}\mathcal A_N=N.
 \tag{1}
\]
Here \(\Omega\) is the original two-head Casimir of [P,H].
This retains the first-normal directions at double Casimir roots.
All packet coordinates below are physical orthonormal coordinates.

Fix a literal tree with \(s\ge1\) proper vertices, and put
\(D=Ns\), \(m=D+1\), and \(\sigma=1/16\).
Keep exactly [P]'s budgets: a prescribed leaf \(A_v\) has budget
\(16\max(1,\|A_v\|_{\rm ph})\), products and genuine turns have
budget \(16\), and an original root \(\eta_N\lambda\), with
\(\lambda\in\{\lambda_0,\phi\}\), has budget
\(16\max(1,|\eta_N|)\). Let \(\mathcal B_N\) be their product.
All original phases, markings and external normalizations remain.

The normalized leaves, linear maps and bilinear maps have norm at
most \(\sigma\). Let \(\Phi_v\) denote these actual maps, and let
\(c_N\) be the normalized original closing row, extended by zero
off the top packet. On \(\mathbb C^D\) set
\[
 G_v(x)=\Phi_v((x_j)_{j\text{ child of }v})-x_v,\qquad
 E_N(x)=\|G(x)\|^2+|c_Nx|^2.
 \tag{2}
\]
This is the original degree-at-most-four objective of [P], without
changing its closing. The exact forward field \(a\) satisfies
\(G(a)=0\) and \(k=c_Na=K_N/\mathcal B_N\).
The field and \(k\) are used only in the proof.

Define the extended nonnegative integral, with physical real
Lebesgue measure,
\[
 \mathcal P_N=\frac{D!}{\pi^D}
                 \int_{\mathbb C^D}E_N(x)^{-D-1}\,dx.
 \tag{3}
\]
Its base is quartic; its denominator exponent and integration
dimension grow with \(N\). No bounded-total-degree assertion for
the rational integrand is intended.

Put
\[
                  \delta_0=\frac1{8192},\qquad
                  \delta=\frac1{2048}.
 \tag{4}
\]
**Theorem.** If \(K_N\ne0\), then \(0<\mathcal P_N<\infty\) and
\[
 \boxed{\quad
 \left||k|^2\mathcal P_N-1\right|\le\delta,\qquad
 (1-\delta)\frac{\mathcal B_N^2}{\mathcal P_N}
       \le |K_N|^2\le
 (1+\delta)\frac{\mathcal B_N^2}{\mathcal P_N}.
 \quad}                                                     \tag{5}
\]
If \(K_N=0\), then \(\mathcal P_N=+\infty\); with reciprocal zero,
the source inequalities in (5) hold there as well.
The constant is uniform over all tree sizes and normalized actual
leaf choices, including fixed short-filling packets.
There is no parity or prior nonvanishing hypothesis.

## 2. The physical closing estimate, at every level

Here is the multiplicity argument needed for the level dependence;
it repeats the existing physical closing estimate explicitly.
Put \(d=N-1\), \(q=e^{\pi i/N}\), and
\[
 c_j=q^{2j+1}+q^{-2j-1},\qquad
 P_N(t)=2T_N(t/2)+2=\prod_{j=0}^{d}(t-c_j).
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind.
The analytic generic ordinary highest-weight family constructed in
[H, Section 4] has pair Casimir eigenvalues
\(\zeta^{2d-2j+1}+\zeta^{-2d+2j-1}\), on summands of dimensions
\(2d-2j+1\), for \(0\le j\le d\). Their dimensions sum to \(N^2\).
Its finite matrices are analytic at \(\zeta=q\). At that root,
\(j\) and \(d-j\) have the same eigenvalue \(c_j\), and their
dimensions sum to \(2N\). The odd self-pair has dimension \(N\)
and eigenvalue \(-2\). Specializing the characteristic polynomial
therefore proves, without root semisimplicity,
\[
       \det(tI_{N^2}-\Omega)=P_N(t)^N.
 \tag{6}
\]
In particular \(c_0=q+q^{-1}\) has algebraic multiplicity \(2N\)
at every \(N\ge2\), including \(N=2\) and all composite levels.

An orthonormal invariant flag makes \(\Omega\) upper triangular.
The diagonal of \(f(\Omega)\) has values \(f(c_j)\) in those
multiplicities, so
\[
 \|f(\Omega)\|_{\rm ph}^2
       \ge N\sum_{j=0}^{N-1}|f(c_j)|^2
       \ge2N|f(c_0)|^2.
 \tag{7}
\]
All offdiagonal and independent first-normal entries remain in
the norm. The original rows obey \(\lambda_0(f(\Omega))=f(c_0)\)
and \(\lambda_0=\phi\circ\mathcal T\), with the genuine physical
turn \(\mathcal T\) unitary by [P]. Hence
\[
 N^{-1}\le\|\lambda_0\|_* =\|\phi\|_*
        \le(2N)^{-1/2},\qquad
             \|c_N\|\le\frac{\sigma}{\sqrt{2N}}.
 \tag{8}
\]
For the lower row bound use \(\lambda_0(I)=1\), \(\|I\|_{\rm ph}=N\).
The normalized root budget above proves the last inequality even
when its original scalar \(\eta_N\) varies with the level.

If \(s_v\) counts proper vertices in a subtree, forward induction
gives \(\|a_v\|\le\sigma^{s_v}\): a leaf contributes one factor,
a turn contributes one more, and a product multiplies the two
child bounds and one more factor. Consequently
\[
 |k|\le\frac{\sigma^{s+1}}{\sqrt{2N}},\qquad
 16Ds^2|k|^2\le8s^3\sigma^{2s+2}\le\delta_0.
 \tag{9}
\]
The last bound is maximal at \(s=1\), since the ratio of successive
terms \(s^3\sigma^{2s}\) is at most \(8\sigma^2=1/32<1\).
It uses no lower bound on the source.

## 3. Exact residual coordinates and the small nonlinear cap

Order children before parents. The recursion
\(x_v=\Phi_v((x_j)_j)-r_v\) gives a global polynomial inverse
\(H=G^{-1}\). Its complex Jacobian determinant is \((-1)^D\),
so its real Jacobian has absolute value one. In these exact
coordinates (3) has denominator
\[
       \|r\|^2+|f(r)|^2,\qquad f(r)=c_NH(r),\quad f(0)=k.
 \tag{10}
\]

Use the proof radius \(R_s=1/(4s)\), which changes neither the
integral nor its coefficients. On \(\|r\|\le R_s\), induction in
the inverse recursion bounds every packet by
\(\sigma+R_s\le5/16<1\).
There \(DG=-I+A\) with \(\|A\|\le\sqrt2\sigma\le1/8\):
each child enters one parent row, and each row has at most two children.
Thus \(\|DH\|\le8/7\).

Only products contribute to \(D^2G\). Their two bilinear terms,
Cauchy--Schwarz on each sibling pair, and disjointness of sibling
pairs give \(\|D^2G[h_1,h_2]\|\le\sigma\|h_1\|\|h_2\|\).
Twice differentiating \(G(H(r))=r\), and then using (8), proves
\[
 \|Df(0)\|\le\frac1{14\sqrt{2N}},\qquad
 \|D^2f\|\le\frac2{343\sqrt{2N}}
                  \quad(\|r\|\le R_s).
 \tag{11}
\]
No coefficient-tensor Hilbert--Schmidt bound for multiplication is used.
Taylor's formula therefore gives
\[
 f(r)=k+dr+p(r),\qquad d=Df(0),\qquad
              |p(r)|\le\frac{\|r\|^2}{343\sqrt{2N}}.
 \tag{12}
\]

Set \(E_{\rm aff}(r)=\|r\|^2+|k+dr|^2\).
Writing \(u=\|r\|\le R_s\), expansion of the squared cap, rather
than a relative bound on the cap itself, gives
\[
 \begin{split}
 |\|r\|^2+|f(r)|^2-E_{\rm aff}(r)|
 &\le 2(|k|+\|d\|u)|p(r)|+|p(r)|^2\\
 &\le\frac{u^2}{N}\left\{
       \frac{\sigma^{s+1}}{343}
       +\frac{u}{14\cdot343}+\frac{u^2}{2\cdot343^2}\right\}.
 \end{split}                                                \tag{13}
\]
Since \(s\sigma^{s-1}\le1\), the braces are at most \(C_*/s\), where
\[
 C_* =\frac1{87808}+\frac1{19208}+\frac1{3764768}
      =\frac{1919}{256\cdot7^6}<\frac1{8192}=\delta_0.
\]
Indeed the three terms are bounded respectively by
\(1/(87808s)\), \(1/(19208s)\), and \(1/(3764768s^2)\).
The inequality \(s\sigma^{s-1}\le1\) follows because its successive
ratio is at most \(2\sigma=1/8\).
Thus on this ball, including its origin by continuity,
\[
 (1-\delta_0/D)E_{\rm aff}
 \le \|r\|^2+|f(r)|^2
 \le(1+\delta_0/D)E_{\rm aff}.
 \tag{14}
\]
This order \(D^{-1}\) energy comparison is what removes damping.

## 4. The affine integral and the entire exterior

For \(k\ne0\), completing the Hermitian square with
\(A_0=I+d^*d\) gives residual constant
\(|k|^2/(1+\|d\|^2)\) and determinant \(1+\|d\|^2\).
Radial integration consequently gives the exact slope cancellation
\[
       \frac{D!}{\pi^D}\int_{\mathbb C^D}
                       E_{\rm aff}(r)^{-D-1}\,dr=|k|^{-2}.
 \tag{15}
\]
The scalar radial integral is
\(\int_0^\infty t^{D-1}(t+e)^{-D-1}dt=1/(De)\), obtained by
\(u=t/(t+e)\).

Both the actual residual energy and \(E_{\rm aff}\) dominate
\(\|r\|^2\). Their normalized exterior integrals satisfy
\[
       \frac{D!}{\pi^D}\int_{\|r\|>R_s}\|r\|^{-2D-2}\,dr
                         =\frac D{R_s^2}=16Ds^2.
 \tag{16}
\]
This controls the entire nonlinear exterior, without a large-field
estimate for \(H\). If \(k\ne0\), the actual energy has no zero:
a zero would require \(r=0\) and \(f(0)=0\). Compactness on the
remaining ball and (16) prove that (3) is finite and positive.

Put \(\xi_N=\delta_0/D\) and
\(\tau_N=16Ds^2|k|^2\le\delta_0\).
Using (14)--(16) on the inside and outside separately gives
\[
 (1+\xi_N)^{-m}(1-\tau_N)
       \le |k|^2\mathcal P_N
       \le(1-\xi_N)^{-m}+\tau_N.
 \tag{17}
\]
Since \(D\ge2\), put \(v=m\xi_N\le3/16384\).
Convexity gives \((1+\xi_N)^{-m}\ge1-v\).
Bernoulli's inequality gives
\((1-\xi_N)^m\ge1-v\), hence
\((1-\xi_N)^{-m}\le(1-v)^{-1}\le1+2v\).
The two sides of (17) are therefore bounded by
\[
 1-\frac5{16384}\le |k|^2\mathcal P_N
       \le1+\frac8{16384}=1+\delta.
\]
Since \(5/16384<\delta\), this proves (5).

If \(k=0\), holomorphy gives \(f(r)=O(\|r\|)\) near zero.
The actual energy is at most a constant times \(\|r\|^2\)
there, and (3) dominates a positive multiple of
\(\int_0^{R_s}u^{-3}du\). It diverges, proving the zero convention.

## 5. Logarithmic consequence and scope

Let \(S_N^{\rm rec}=\mathcal B_N^2/\mathcal P_N\), with reciprocal
zero at infinity. For every nonzero source, (5) gives
\[
 \left|\frac\pi N\log S_N^{\rm rec}
             -\frac{2\pi}N\log|K_N|\right|
       \le-\frac\pi N\log(1-\delta)
       \le\frac\pi{2047N}.
 \tag{18}
\]
Zeros coincide exactly. The same bound holds between
\(\pi N^{-1}\log(1+S_N^{\rm rec})\) and
\(\pi N^{-1}\log(1+|K_N|^2)\), including at zeros.
For any fixed positive target rate, convergence to that rate for
the reciprocal expression is therefore equivalent to convergence
for the original squared source. No eventual nonvanishing was assumed.

The comparison constant is universal, not chosen from any source
value or filling packet. The closing row, full physical algebra,
normal channels, objective and original budgets have not changed.
The integral is not claimed to be a separately topological quantity
at each finite level. Its signed source remains inside the denominator.
No geometric energy estimate, contributing-cycle coefficient,
arbitrary-short-filling volume theorem or finite-exception theorem
is supplied by this representation.

## Complete inputs and coverage

The full texts [P] and [H] fix the source and multiplicities.
[R] already supplies the damped reciprocal construction, affine
identity and fixed-ball strategy. Those steps are proved again here
with the physical closing bound retained sharply; the addition is
the undamped comparison (5), with no new budget factor.
All three complete matching texts were read. Only written mathematics
and text/hash operations were used; no earlier final was edited.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| P, source, 477 lines | [Uniform physical quartic](research_conway_uniform_physical_quartic.md) | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| H, source, 331 lines | [Complete physical pair and original trace](actual_pair_casimir_commutant_and_rotated_trace.md) | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| R, coverage, 233 lines | [Damped reciprocal source formula](research_conway_reciprocal_quartic_source_formula.md) | ead3945544c91ed81b87423f05c80dde29439d2be183b391005b133610e84e97 |
