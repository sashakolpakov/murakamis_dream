# Fejér entropy signs and the remaining homogeneous-tail comparison

31 October 2026. This checks the actual [closed local coefficient entropy](actual_fejer_half_block_entropy.md) and [full-kernel entropy](actual_fejer_full_kernel_entropy_identity_reduction.md). It disproves nonnegativity of the full local entropy, proves strict positivity at every port of the original simple-white geometric flow, and gives a scoped shared-capacity reduction. No estimate for a complementary source with arbitrary signed crossing powers follows.

## 1. An exact source coefficient disproves nonnegativity

Use the original even level $N=2m$, $d=N-1$, $M=m-1$, with

$$
s_r=2\sin(\pi r/N),\qquad a_r=4\cos^2\!\left(\frac{\pi(r+1/2)}N\right).
$$

For a left path from $j$ to $i=0$, the coefficient of $x^j c^{d-j}$ has no $y$ and therefore has no dimer. There is exactly one path, using all single-$x$ steps. The original half-block identity gives exactly

$$
[x^j c^{d-j}]P_N=\frac4{a_0}\prod_{r=1}^j\frac{s_r^2}{a_r},
\qquad 0\leq j\leq M.\tag{1}
$$

No other half or cross part has these degrees when $j<M$. The source scalar $4/a_0$ is retained and has zero exponential rate. For $j/N\to\nu\in(0,1/2)$, the elementary log-sine/cosine Riemann limit, with its integrable lower endpoint, gives

$$
h(\nu,0,1-\nu,0)=E(0,\nu,\nu)
=2\int_0^\nu\log\tan(\pi t)\,dt<0.\tag{2}
$$

The integral is strictly negative for every $0<\nu<1/2$: its derivative changes sign only at $1/4$ and its total value at $1/2$ is zero by $t\mapsto1/2-t$. In particular, for $N=4k$ and $j=k$,

$$
h(1/4,0,3/4,0)=-\frac{2G}{\pi},\qquad
G=-\int_0^{\pi/4}\log\tan u\,du>0.\tag{3}
$$

Here $G$ is Catalan's constant. This is the entropy of an actual coefficient of the full positive numerator, not a factorwise estimate or a missing exponential normalization. Continuity of $h$ also supplies strictly negative points in the interior of the four-face simplex. Thus restricting away from zero faces cannot repair the assertion $h\geq0$.

There is an exact global floor. The closed coefficient formula gives

$$
E(\mu,\nu,\xi)\geq2\int_\mu^\nu\log\tan(\pi t)\,dt
\geq-\frac{2G}{\pi}.
$$

The last minimum takes the whole negative interval $[0,1/4]$ and no positive part. The cross entropy is nonnegative by Section 2. Therefore

$$
\min_{\text{simplex}}h=-\frac{2G}{\pi}.\tag{4}
$$

## 2. The geometric port entropy is strictly positive

For a triangle of loads $\alpha_x+\alpha_b+\alpha_y=1/2$, write

$$
C_{\mathrm{tri}}(\boldsymbol\alpha)=\sum_j f(\alpha_j),\qquad
f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi}.
$$

Direct differentiation gives $f'(t)=\log\cot(\pi t)$, while $f(0)=f(1/2)=0$ and $f(1/2-t)=f(t)$. Hence $f(t)>0$ for $0<t<1/2$. Thus $C_{\mathrm{tri}}\geq0$, with equality only at a triangle vertex. In particular every cross port has $h\geq0$, including all seams.

Now use the actual simple white triangulation, with the two adjacent protected faces $u,v$ joined by the marked MAIN edge. A matching port has triangles $(x,b,y)$ and $(x,c,y)$, with distinct middle vertices $b,c$ and common MATCHING edge $xy$. The geometric ordinary curvatures are strictly positive; the two protected curvatures are zero. In the actual angle formula a corner load is positive exactly when its curvature is positive, except that the one remaining positive corner in a two-line triangle carries the whole $1/2$.

The two triangles cannot both have zero entropy. If $x,y$ are ordinary, both triangles have at least two positive corners. If exactly one of $x,y$ is protected, at most one of the distinct $b,c$ can be the other protected vertex, so the other triangle has at least two positive corners. Both $x,y$ cannot be protected, because their edge is MATCHING while $uv$ is the marked MAIN edge. These exhaust the cases.

Therefore the geometric split has a strictly positive sum of its two triangle entropies at every port $e$. The definition of $h$ as the maximum over cross splits yields

$$
h(\mathbf q_{\mathrm{geom},e})>0\qquad\text{for every }e.\tag{5}
$$

This is pointwise for each fixed certified diagram. No diagram-uniform positive lower bound is asserted. Simplicity and the actual MAIN/MATCHING label are used; the conclusion is not silently extended to a repeated-incidence multigraph.

## 3. Exact mixed rate and a strict partial comparison

Let $J$ be any nonempty set of ports. Replace their positive full kernels by

$$
h_d(x,b,c,y)=\sum_{\substack{a+i+t+s=d\\a,i,t,s\geq0}}x^a b^i c^t y^s,
$$

whose every coefficient is one. This polynomial has the full degree-$d$ simplex support and local coefficient entropy zero. It is only the absolute homogeneous bound supplied by the [far-tail Fourier adapter](actual_far_charge_homogeneous_insertion.md); it is not identified with the identity coupon $H_1$ or any original covariant coupon.

Keep $F_N$ at all other ports, with its original parity-appropriate positive definition, all original ordinary targets $d$, and both protected targets zero. The same unrestricted degree-$d$ bipartite-flow rounding and uniform local entropy theorem prove that this positive mixed coefficient has rate

$$
\Psi_J=\max_{\mathbf q\in\mathcal P_D}H_J(\mathbf q),\qquad
H_J(\mathbf q)=\sum_{e\notin J}h(\mathbf q_e).\tag{6}
$$

Here $\mathcal P_D$ is the original marked flow polytope. The number of arrays is polynomial in $N$; floor/ceiling cycle rounding respects the actual balances and incurs only $O(1/N)$ in local loads. Full supports eliminate a fixed-pattern feasibility issue. This argument is valid at both parities using the established common local $h$.

The [endpoint theorem](general_fejer_endpoint_source_volume.md) and [unique geometric maximum](actual_fejer_unique_geometric_maximizer.md) give

$$
H(\mathbf q)=\sum_e h(\mathbf q_e)\leq\Phi_D,\qquad
H(\mathbf q)=\Phi_D\ \Longleftrightarrow\ \mathbf q=\mathbf q_{\mathrm{geom}}.
$$

Define the compact restricted set

$$
\mathcal K_J^+=\{\mathbf q\in\mathcal P_D:h(\mathbf q_e)\geq0\text{ for every }e\in J\}.
$$

There is a strict gap on this set:

$$
\max_{\mathbf q\in\mathcal K_J^+}H_J(\mathbf q)<\Phi_D.\tag{7}
$$

Indeed $H_J\leq H\leq\Phi_D$ there. Equality at a maximizer would force $H=\Phi_D$ and every removed entropy zero. Uniqueness would then give $\mathbf q=\mathbf q_{\mathrm{geom}}$, contradicting (5) and $J\ne\varnothing$. Compactness and continuity turn this pointwise exclusion into a positive fixed-diagram gap.

Consequently, if the full comparison $\Psi_J<\Phi_D$ fails, every maximizing flow reaching or exceeding $\Phi_D$ has at least one inserted port with $h(\mathbf q_e)<0$. Such a port is strictly one-sided: one middle exceeds $1/2$, its interval has positive length, and it is neither a pure-middle diagonal nor a cross seam. These overloaded edges obey the same original rooted-forest constraint, because each ordinary face has total demand $1$, each protected face demand $0$, and every original middle-gap cycle contains the protected exterior. Subsets of those edges remain forests.

This is a general reduction of the remaining $h_d$ majorant problem to negative-entropy one-sided forest branches. It is not a bound for those branches. The tempting deduction from unique geometric maximality alone is invalid, since replacing a negative $h$ by zero increases the local objective. Formula (4) gives only the crude unconditional estimate

$$
\Psi_J\leq\Phi_D+|J|\frac{2G}{\pi},
$$

which is not the desired strict gap.

The exact far Fourier tails retain covariance and alternating spectral data that the $h_d$ majorant discards. Neither (6) nor (7) is a bound for a complementary source with arbitrary remaining signed $R$ powers; that stronger source problem still requires its own estimate.

## Validation and scope

Independent analytical review checked the exact original coefficient, the global entropy floor, the triangle-vertex zero criterion, the protected MAIN versus MATCHING incidence, and the compact restricted-capacity gap. No numerical sample is used to prove these statements. The local negative-entropy obstruction does not disprove a general shared-source bound, and the positive mixed comparison remains restricted to the explicitly stated subset of its original flow polytope.
