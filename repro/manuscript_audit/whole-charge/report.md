# Audit of the whole oscillatory filling sum

I read all of [the oscillatory filling paper](../../../papers/oscillatory-fillings/main.tex) at commit `6be87c935ca369a3697c2d842d8e09f98d06cfa7`, the actual midpoint/Hermite formula imported from [the filling-bound paper](../../../papers/filling-bounds/main.tex), and [the normalization exported by the consolidated Casimir-source paper](../../../papers/casimir-source-asymptotics/filling-input.tex). Exact source hashes, labels and line numbers are in [sources.json](sources.json). These identify the reviewed repository sources at that commit; no duplicate source snapshot is included here.

**Outcome:** no counterexample or proof defect was found under the printed Hlocal/Hgap hypotheses. I found no missing step in the infinite-tail, contour or sign arguments that requires strengthening those hypotheses. This is an independent mathematical reading and a targeted numerical falsification check, not a formal verification of the analytic theorem. It does not certify the source or geometric hypotheses for a knot.

## Findings by category

- **Proved defects:** none found.
- **Missing justification affecting the stated conclusion:** none identified.
- **Retained inputs:** the exact polynomial form and separate degree bound; Hlocal on a fixed complex neighborhood with its nonzero limiting amplitude and real, separately even finite actions; Hgap for the actual shared source in a fixed strip. The source-specific proof of those hypotheses, control of noncentral invariant sectors and the geometric action-volume equality are separate.
- **Limits of the audit:** I checked the finite midpoint identity used here against its actual formula and normalization. I did not re-audit every algebraic or topological proof elsewhere in filling-bounds. The numerical probes below verify neither an all-level assertion nor an infinite charge estimate.

## The exact finite identity

The imported formula is
$$
 \mathcal L_N^nH=-N^{-2}\sum_{k=0}^{N-1}g'(\phi_k),
 \qquad \phi_k=(2k+1)\pi/N.
$$
The two appearances of each double root and the one odd simple root are accounted for in filling-bounds, equations uf:eq-10 and uf:eq-12. At the odd point $\phi=\pi$, differentiating the sine supplies precisely $f(-2)H(-2)/N^2$. The multiplier and its lift are the same $q^{nd^2/4}$ as in uf:eq-13.

The periodic extension of $g'$ is continuous: $g$ vanishes at both endpoints and $g'$ has the same value there. Three integrations by parts give $\widehat g_k=O_{N,n}(|k|^{-3})$, retaining the second-derivative boundary difference. Hence the Fourier series of $g'$ is absolutely convergent; the Fejér uniqueness argument identifies it without an unjustified differentiation of a conditional series. The midpoint filter retains exactly $k=N\ell$. Under $\phi=\pi-2\pi\delta$, the Jacobian cancels the Fourier normalization and the phase factor becomes $(-1)^{(N+1)\ell}$. I checked the resulting factor $-i$, its charge weight $\ell$, and the stated $\Gamma_N$.

For several variables, the endpoint identities remain true after differentiation in other coordinates. Applying the exact three-IBP identity in each coordinate bounds the weighted summand by a constant depending on $N,\boldsymbol n$ times $\prod_j|\ell_j|^{-2}$. This proves absolute convergence at each fixed level and justifies the tensor Fourier identity. It is not yet the uniform asymptotic tail estimate, and the proof correctly treats that as a later argument.

## Why the infinite distant-charge tail is controlled

This is the crucial distinction from a proof that estimates only finitely many local saddles.

First, Hlocal and Hgap give a real-torus bound $e^{N(\Phi+b_N)}$, where $b_N\to0$. Separate polynomial degree at most $d=N-1$ then gives
$$
 |C_N(x+iy)|\le e^{N(\Phi+b_N)+2\pi d\sum_j|y_j|}.
$$
The successive one-variable maximum principles apply to the actual multivariate polynomial. They do not require factorization of the shared source.

Choose a distinguished positive distant charge $\ell_i$. Its interval is shifted upward on the entire original interval, with every spectator variable still real. The oriented rectangle identity has the printed minus sign on the difference of the two vertical currents.

At the endpoints the exact difference is
$$
 2i\sinh(2\pi v)\sinh(\pi n_iNv)
 e^{\pi i n_iN(1/4-v^2)}
 C_N(1/2+iv,\delta_{\ne i}).
$$
Both sine endpoint values are $-i\sinh(2\pi v)$, while the two chirps differ by $e^{-\pi n_iNv}-e^{\pi n_iNv}$. Thus the displayed sign and factor two are correct for either twist sign. The Fourier endpoint characters agree; their combination with the original parity is $(-1)^{\ell_i}$.

The paired current has a quadratic zero in $v$. Its bound is
$$
 C_{\boldsymbol n}|n_i|Nv^2e^{\pi|n_i|Nv}.
$$
This order of vanishing matters. Estimating two unpaired currents with only their separate linear sine zeros would lead to a weighted harmonic tail and would not justify absolute summation.

Spectator IBP preserves this paired zero. It differentiates only the spectator sine, chirp and shared-source factors. Periodicity in the distinguished coordinate still identifies the two source values, including all those spectator derivatives. On real spectator variables, each chirp derivative has polynomial cost in $N$, of degree at most its derivative order. The worst $N^3$ cancels the $N^{-3}$ in three IBPs. Source derivatives are estimated on a fixed Cauchy neighborhood retaining the endpoint Hgap; the large spectator twist is not moved into that complex-source estimate. The resulting spectator weights are $\prod_{j\ne i}|\ell_j|^{-2}$, with constants depending on the fixed twist tuple.

Write $b=|n_i|/2$. For $\ell_i>b+D$, the remaining vertical integral is bounded by
$$
 \int_0^\infty v^2e^{-2\pi N(\ell_i-b)v}\,dv
 =\frac{2}{[2\pi N(\ell_i-b)]^3}.
$$
After its exterior factor $N\ell_i$, the charge dependence is
$\ell_i/(\ell_i-b)^3$. Its sum is bounded by a constant times
$D^{-1}+(|n_i|+1)D^{-2}$. The source endpoint factor supplies a fixed exponential gap. All spectator sums converge.

On the shifted horizontal interval, source growth and the fixed spectator Cauchy radii cost at most $2\pi r\tau N$; the distinguished chirp and Fourier factor cost
$$
 \pi|n_i|N\tau-2\pi\ell_iN\tau.
$$
Choosing $D$ with $2\pi\tau D>2\pi r\tau+2\gamma_e$ makes the horizontal charge series a geometric tail with a fixed gap. This choice is independent of all twist magnitudes. Constants depending on a fixed twist tuple occur outside the exponential.

Reflection handles negative charges. A union bound over the distinguished coordinate covers every charge outside the finite rectangle $0<|\ell_i|\le M_i$, while all spectator charges have already been summed over their full ranges. Counting a charge several times only enlarges the upper bound. No infinite series is cut at a small cube before these summable estimates have been obtained.

## Critical points and arbitrary twist signs

Separate evenness gives
$$
 \partial_jA_N(z)=-2z_jB_{N,j}(z),\qquad
 z_j=-\frac{\ell_j/n_j}{1+iB_{N,j}(z)/(\pi n_j)}.
$$
On the fixed small neighborhood, $B_{N,j}$ remains close to the positive real $c_j$. The fixed-point map has derivative norm bounded by $Ca/n_0$, independent of twist ratios, for $0<\ell_j/|n_j|\le a$. The coordinate estimate $|z_j|\le2\ell_j/|n_j|$ follows from the same equation.

Writing $B=u+iv$ and taking the imaginary part gives exactly
$$
 \Im z_j=\frac{\ell_j}{\pi n_j^2}
 \frac{\Re B_{N,j}(z)}{|1+iB_{N,j}(z)/(\pi n_j)|^2}>0.
$$
In particular, the upward contour is appropriate for positive charges even when some twists are negative. The real part of the negative phase Hessian is uniformly positive because the twist Hessian is purely imaginary and $-\Re A_N''$ stays positive.

Differentiating the critical action in a charge gives
$\partial_{\ell_j}\Re S_{N,\ell}=-2\pi\Im z_j$. Integration over one charge at a time proves the printed charge comparison while all other coordinates remain in their allowed boxes. This gives the gap below the unit charges and the bound $A_N(0)-\Re S_{N,\mathbf1}=O(\sum_j n_j^{-2})$. No comparison of different twist sizes is needed.

## The original local contour and its side faces

The local cube is translated coordinate by coordinate to the imaginary height of the critical point. Cauchy's theorem gives its coefficient one and retains all side faces.

On every intermediate rectangle,
$$
 \Re A_N(x+iy)\le A_N(0)-c|x|^2+C|y|^2.
$$
At a side face a real coordinate has modulus $B$. The possible chirp cost is at most $Ca\sum_j|x_j|$, since $|n_j|y_j\le Ca$. The positive-charge contribution is nonpositive. Choosing $a$ sufficiently small compared with the outer radius $B$, then $n_0$ large, leaves a fixed side-face gap. This estimate remains valid for mixed twist signs.

On the translated real cube, the real part of the full phase is strictly concave with its unique maximum at the critical point. The quadratic bound controls the entire part away from that point. The source error is holomorphic and uniformly $O(N^{-1})$, so it and its fixed derivatives retain that order on a smaller domain. The centered cubic and linear Gaussian terms are odd; the next terms contribute the stated relative $O_{\boldsymbol n,\ell}(N^{-1})$ error.

The complex Gaussian formula uses the holomorphic square root on the convex domain of complex symmetric matrices with positive definite real part. Its determinant cannot vanish there; continuation from the positive real matrices fixes the branch. The limiting amplitude is nonzero: $a_N(z_N)$ tends to a nonzero value, the Hessian remains invertible, and every positive-charge saddle coordinate has strictly positive limiting imaginary part, so its sine does not vanish.

This step needs only constants for each fixed twist and charge tuple. It does not assert that the relative error stays bounded uniformly when a twist grows with $N$.

## The finite charges outside the local range

Once the infinite tail has been removed, the remaining rectangle of charge indices is finite for a fixed twist tuple. It is now legitimate to introduce a smaller cube.

If one coordinate satisfies $|\ell_i|/|n_i|>a$, reflect it to positive charge and shift only that coordinate by $ib/|n_i|$, with $0<b<a/4$. On the inner cube,
$$
 -2\pi n_ix_iv-2\pi\ell_iv
 \le-2\pi|n_i|(a-b)v.
$$
On the new horizontal face this is a fixed loss $2\pi b(a-b)$, while the source cost is $O(b^2/n_0^2)$. On a side face, the real source loss $cb^2$ remains and the preceding charge/chirp term stays nonpositive. The real exterior uses Hgap directly.

The separate inner radius is essential: the local saddle uses an outer cube, whereas this estimate is designed to exclude charges with a large ratio. The proof makes these choices in the correct order and then sums only finitely many terms.

## Phase alignment and the final threshold

The weighted integrals of all $2^r$ unit-sign choices are exactly equal. Under reflection of one coordinate the source and chirp are even, while the sine and the exterior charge weight both change sign. Their signs cancel, and the parity character is unchanged. This identity concerns the original complete integrals; it does not require the separately chosen approximate amplitude $a_N$ to be exactly even or require a new square-root branch at every reflected saddle.

The factor $2^r$, the original $(-i)^r$, and the unit parity produce the stated $(-2i)^r(-1)^{(N+1)r}$. The explicit $\Gamma_N$ is retained. The source-export substitution gives the claimed $N^{r+1/2}\sqrt{2\pi}$ and cancels the two level-parity signs at every level.

All fixed gaps used for distant charges, bounded nonlocal charges, the outer side faces and the real exterior can be fixed before enlarging $n_0$ a final time. The unit action loss is then smaller than each of them. The other local charges have positive gaps for the fixed twist tuple, although those gaps may become small as twists increase. This is sufficient for the limit actually stated.

The proof keeps $S_N$ inside the exponential. Arbitrarily slow convergence of $A_N$, $S_N$, or their derivatives is therefore allowed: it affects the level threshold and finite phase, not the asserted relative formula. No estimate with twists depending on $N$, no uniform relative error over unbounded twist tuples, and no knot-volume conclusion follows from this theorem alone.

## Falsification probes and boundary control

The script [finite_phase_probe.py](finite_phase_probe.py) compares the actual midpoint functional with the full displayed unit-charge leading expression for
$$
 C_N(\delta)=(2+\cos(2\pi\delta))^{N-1}.
$$
This is the paper's explicit polynomial example and satisfies both hypotheses. The explicit $\Gamma_N$ and complete source value are divided out consistently. The probe includes twists $12,-12,41,-41$, both level parities, and the separable two-variable tuple $(12,-41)$. It uses the actual finite $A_N$, solves its actual saddle equation, and takes the accretive Gaussian branch.

No phase or prefactor contradiction was found. For twist 12, the relative errors at levels 256, 512 and 1024 are approximately $1.003\cdot10^{-3}$, $5.016\cdot10^{-4}$, and $2.508\cdot10^{-4}$. The larger twist has appreciable competing-charge effects at the smaller levels; this is consistent with the fixed-tuple theorem and is not treated as a failure or as proof of convergence. Negative-twist values also agree with the exact conjugation symmetry.

A second source,
$$
 (2+\cos(4\pi\delta))^{\lfloor(N-1)/2\rfloor},
$$
has the required separate polynomial degree and satisfies Hlocal, but violates Hgap exactly because its value at $1/2$ equals its value at zero. The probe shows an endpoint-scale contribution for the even twist 12, rather than the small unit-saddle prediction. This is a boundary control, not a counterexample to the theorem. It exposes why a local Hessian and local packet cannot replace the global gap.

The saved samples are in [finite-phase-probe.json](finite-phase-probe.json). All numerical samples are diagnostics only. They do not prove the infinite charge bound, the fixed complex neighborhood, an all-level statement, or a volume identity. The assessment above rests on the written argument and its exact hypotheses. No modification of the theorem or proof is recommended by this audit.
