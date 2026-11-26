# Sharp physical Grams and a positive history sum for the actual coproduct

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

The actual cyclic-source coproduct has a canonical positive invariant
Gram. Its optimal distortion in the original physical metric has an
explicit sharp exponential rate. A positive sum of squared power norms
has a stronger asymptotic with its prefactor, and determines the norms
of every cyclic spectral projector exactly. The rate is a regular ideal
bipyramid value. It is a metric and projector rate, not a knot-volume rate.

## 1. The original source family and the statement

Fix an integer \(b\ge1\), independently of \(N\ge2\). Put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \gamma=(-1)^{N+1},\quad x=-q^{-1},\quad
 s_a=\prod_{h=1}^a2\sin(\pi h/N),\quad s_0=1.
 \tag{1}
\]
Give the balanced physical basis \(w_0,\ldots,w_d\) its ordinary
orthonormal metric, and use the tensor-product metric on \(b\) heads.
Stars, operator norms and unnormalized Hilbert--Schmidt norms below
refer to this physical metric.

Use [B]'s regular complete-color source chart, at \(M=1\):
\[
 E_iw_a=(Q^{-a}-1)w_{a-1}\ (a>0),\qquad E_iw_0=\mu_iw_d,\qquad
 K_iw_a=xQ^{-a}w_a.
 \tag{2}
\]
Choose the fixed source line
\[
 |\mu|=1/N,\qquad \mu_i=\gamma^{1-i}\mu,\qquad
 X_i=E_iK_{i+1}\cdots K_b,\quad
 E_{\rm tot}=\sum_{i=1}^bX_i,\quad K_{\rm tot}=\prod_{i=1}^bK_i.
 \tag{3}
\]
The coproduct is the literal one in [M]. The source freedom in [B]
preserves the whole original selected knot operator on this line.
That statement retains its crossings, pivots, framing and external
normalization. It does not permit resetting an intermediate exterior.
No off-meridian extension of this root-level construction is asserted.

Since \(\prod_{a=1}^d(Q^{-a}-1)=\gamma N\), direct multiplication gives
\[
 X_iX_j=QX_jX_i\ (i<j),\qquad
 X_i^N=cI,\quad c=\gamma^bN\mu,\quad |c|=1.
 \tag{4}
\]
Indeed \(E_i^N=\gamma N\mu_iI\) and \(K_i^N=\gamma I\).
The root multinomial identity therefore gives
\[
 E_{\rm tot}^N=bcI.
 \quad\text{Choose }e^N=bc,\qquad T=E_{\rm tot}/e.
 \quad T^N=I,\quad |e|=b^{1/N},\quad K_{\rm tot}T=QT K_{\rm tot}.
 \tag{5}
\]
Every choice of the root \(e\) is allowed.

Define
\[
 \mathcal A_N=\max_{0\le k<N}\|T^k\|_{\rm op},\qquad
 J_{\rm av}=\sum_{k=0}^{N-1}(T^k)^*T^k,\qquad
 \mathcal H_N=\operatorname{Tr}J_{\rm av}
                         =\sum_{k=0}^{N-1}\|T^k\|_{\rm HS}^2.
 \tag{6}
\]
These are specified from the actual coproduct, without a knot value.
For a positive Hermitian Gram \(J\), write
\(\kappa(J)=\lambda_{\max}(J)/\lambda_{\min}(J)\).
Let \(\mathcal J_N\) be the Grams satisfying both
\(T^*JT=J\) and \(K_{\rm tot}^*JK_{\rm tot}=J\).

Put
\[
 n=2b+1,\quad \delta=\pi/n,\quad
 h(u)=\int_0^u\log(2\sin\pi v)\,dv,\quad
 M_b=-n h(1/n)>0,
 \tag{7}
\]
\[
 C_b=
 \frac{2^{1-b}b^{-4b/n}\sin\delta}
                  {\sqrt n\,\sin(2\delta)^b}.
 \tag{8}
\]
**Theorem.** The class \(\mathcal J_N\) contains \(J_{\rm av}\), and
\[
 \mathcal A_N\le\inf_{J\in\mathcal J_N}\sqrt{\kappa(J)}
                         \le\sqrt N\,\mathcal A_N.
 \tag{9}
\]
The same inequalities hold when only \(T\)-invariance is required.
Through all integer levels,
\[
 \log\mathcal A_N=NM_b+O_b(\log N),\qquad
 \log\inf_{J\in\mathcal J_N}\sqrt{\kappa(J)}
                              =NM_b+O_b(\log N).
 \tag{10}
\]
Moreover the positive history sum has the asymptotic
\[
 \boxed{\quad \mathcal H_N=C_bN e^{2NM_b}(1+O_b(N^{-1})).\quad}
 \tag{11}
\]
For the actual spectral projectors
\[
 P_j=\frac1N\sum_{k=0}^{N-1}Q^{-jk}T^k,\qquad 0\le j<N,
 \tag{12}
\]
one has the exact identities and their common asymptotic
\[
 J_{\rm av}=N\sum_jP_j^*P_j,\qquad
 \|P_j\|_{\rm HS}^2=\mathcal H_N/N^2
       =\frac{C_b}{N}e^{2NM_b}(1+O_b(N^{-1})).
 \tag{13}
\]
The finite identities hold at every \(N\ge2\); the asymptotics have
fixed \(b\) and no parity restriction. They are independent of the
phases of \(\mu,e\).

## 2. Exact physical power entries, including every wrap

For \(0\le k<N\), the finite quantum multinomial formula is
\[
 E_{\rm tot}^k=
 \sum_{\substack{k_1+\cdots+k_b=k\\k_i\ge0}}
       \frac{(Q;Q)_k}{\prod_i(Q;Q)_{k_i}}\,
                         X_b^{k_b}\cdots X_1^{k_1}.
 \tag{14}
\]
It follows by induction from (4), with the displayed descending order.
All factorial denominators are nonzero. For the \(N\)-th power, every
mixed coefficient vanishes because its numerator contains \(1-Q^N\)
and its denominators do not. The remaining pure terms prove (5).

On an input \(w_{\boldsymbol a}\), set
\(r_i=[a_i-k_i]_N\), with residues in \(0,\ldots,d\).
The \(K\) dressings have unit modulus. On one head, exactly
\[
 |\langle r|E_i^{\,u}|a\rangle|=s_a/s_r,\qquad
 r=[a-u]_N,\quad 0\le u<N.
 \tag{15}
\]
Without a wrap this is the consecutive sine product.
With a wrap, \(a<u\), its modulus is
\(s_a|\mu_i|\,s_d/s_r=s_a/s_r\), since \(s_d=N\).
There is at most one wrap in (15).

For fixed input and output, each \(k_i\) is determined modulo \(N\);
its required range \(0\le k_i\le k<N\) determines it uniquely.
Thus (14) has at most one term at any specified matrix entry. Its
nonzero modulus is exactly
\[
 |\langle\boldsymbol r|T^k|\boldsymbol a\rangle|
 =b^{-k/N}s_k\prod_{i=1}^b\frac{s_{a_i}}{s_{k_i}s_{r_i}}.
 \tag{16}
\]
The full complex coefficient remains (14) applied to the literal
matrices (2); no phase has been removed from an original contraction.
Absolute values in (16) are used for norms and the positive sum (6).
The history sum is parametrized once by
\[
 0\le a_i<N,\quad k_i\ge0,\quad k:=\sum_i k_i<N.
 \tag{17}
\]
There is no transfer-path multiplicity or lattice-index factor.

## 3. A global maximum on the full wrapped support

Use scaled variables \(u_i=k_i/N\), \(t=\sum_i u_i\le1\), and
\(a_i/N=y_i\). On each wrap sector put
\(z_i=y_i-u_i\) without a wrap and \(z_i=y_i-u_i+1\) with a wrap.
The endpoint-uniform sine estimate in [G] gives the logarithm of
(16) as \(NS+O_b(\log N)\), uniformly on (17), where
\[
 S=h(t)-\sum_i h(u_i)+\sum_i\{h(y_i)-h(z_i)\}.
 \tag{18}
\]
The factor \(b^{-t}\) is bounded above and below and is kept in the
amplitude below. The sector actions extend continuously to their
closed supports, using \(h(0)=h(1)=0\).

Fix \(0<u<1\). In the sector without a wrap,
\(D_u(y)=h(y)-h(y-u)\), \(u\le y\le1\), is strictly concave:
\[
 D_u''(y)=
 -\frac{\pi\sin(\pi u)}
           {\sin(\pi y)\sin(\pi(y-u))}<0.
 \tag{19}
\]
Its unique maximum is at \(y=(1+u)/2\), with value
\(-2h((1-u)/2)\), by \(h(1-v)=-h(v)\).
In the wrapped sector, \(0\le y\le u\), its value is instead
\(h(y)+h(u-y)\). This is strictly convex in the interior, with
second derivative \(\pi\sin(\pi u)/
[\sin(\pi y)\sin(\pi(u-y))]\). Its maximal value is \(h(u)\)
at the endpoints. The difference of the two sector maxima is
\[
 -2h((1-u)/2)-h(u)=-2h(u/2)>0.
 \tag{20}
\]
Here \(h(u)=2h(u/2)-2h((1-u)/2)\), proved by differentiation;
\(h\) is strictly negative on \((0,1/2)\).

After maximizing every \(y_i\), (18) becomes
\(h(t)-2\sum_i h(u_i/2)\).
Strict convexity of \(h\) on \([0,1/2]\) makes the transfers equal
at fixed \(t\). The remaining one-variable function is
\[
 F_b(t)=h(t)-2b h(t/(2b)),\qquad
 F_b'(t)=\log\frac{\sin(\pi t)}{\sin(\pi t/(2b))}.
 \tag{21}
\]
The sine-difference formula gives its unique maximum at
\[
 t_*=\frac{2b}{n},\quad u_{i,*}=\frac2n,\quad
 y_{i,*}=\frac12+\frac1n,\quad z_{i,*}=\frac12-\frac1n,
 \qquad F_b(t_*)=M_b.
 \tag{22}
\]
For example \(F_b''<0\) follows because \(v\cot v\) strictly
decreases on \((0,\pi)\). The one-variable endpoint values and
continuity cover \(t=0,1\). Equality in the preceding optimizations
at this maximum is unique. In particular the maximum has no wraps,
all factorial lengths are strict interior points, and every closed
wrap sector is separated from it by a positive action gap.

There are only polynomially many entries for fixed \(b\).
An operator norm lies between a maximal entry and \(N^b\) times it.
The uniform estimate in (18), followed by rounding (22) on its strict
interior lattice, proves the first part of (10).

For geometric calibration, let
\(\Lambda(\theta)=-\int_0^\theta\log(2\sin v)\,dv\).
Then \(2\pi M_b=2n\Lambda(\pi/n)\).
The regular ideal \(n\)-gonal bipyramid splits about its axis into
\(n\) tetrahedra of angles
\((2\pi/n,\pi/2-\pi/n,\pi/2-\pi/n)\).
The duplication identity for \(\Lambda\) gives volume
\(2\Lambda(\pi/n)\) for each. This is the familiar bipyramid value;
its occurrence as the sharp physical Gram rate is the assertion here.

## 4. A canonical invariant Gram attains the sharp rate

For any \(J>0\) with \(T^*JT=J\), every power is \(J\)-unitary.
Converting its two norms gives
\(\|T^k\|_{\rm op}\le\sqrt{\kappa(J)}\). This proves the lower
bound in (9), without a spectral-basis assumption.

Since \(T^N=I\), shifting the sum in (6) shows
\(T^*J_{\rm av}T=J_{\rm av}\). Also
\[
 I\le J_{\rm av}\le N\mathcal A_N^2 I.
 \tag{23}
\]
The physical unitary \(K_{\rm tot}\) conjugates \(T^k\) to \(Q^kT^k\);
the phase cancels in each summand of \(J_{\rm av}\).
Thus \(K_{\rm tot}^*J_{\rm av}K_{\rm tot}=J_{\rm av}\).
This proves existence and the upper bound in (9), and completes (10).
The optimum is asserted at exponential scale, not as an exact
finite-level condition number for \(J_{\rm av}\).

## 5. The positive history sum and its prefactor

Near (22), no term wraps. In the \(2b\) variables
\((\boldsymbol u,\boldsymbol y)\), let \(H=-S''\) at the maximum.
Put \(\alpha=\pi\cot\delta\), \(\beta=\pi\tan\delta\).
Differentiation of (18) gives
\[
 H_{uu}=\alpha\boldsymbol1\boldsymbol1^{\mathsf T}
                         +\frac{\alpha+\beta}{2}I,\quad
 H_{uy}=-\beta I,\quad H_{yy}=2\beta I.
 \tag{24}
\]
Eliminating the \(y\) block leaves
\((\alpha/2)(I+2\boldsymbol1\boldsymbol1^{\mathsf T})\).
Therefore \(H>0\) and
\[
 \det H=n\pi^{2b}.
 \tag{25}
\]
The interior sine-product expansion proved in [G] yields for (16)
\[
 (2N)^{(1-b)/2}b^{-t}A(\boldsymbol u,\boldsymbol y)
                         e^{NS}(1+O_b(N^{-1})),\qquad
 A^2=\sin(\pi t)\prod_i
       \frac{\sin(\pi y_i)}{\sin(\pi u_i)\sin(\pi z_i)}.
 \tag{26}
\]
At the maximum \(A_*^2=\sin\delta/\sin(2\delta)^b\).
The grid in (17) has mesh \(1/N\) in each of its \(2b\) coordinates.
Summing the squared leading Gaussian consequently gives
\[
 N^{2b}(2N)^{1-b}N^{-b}
       \frac{\pi^b}{\sqrt{\det H}}\,
       b^{-2t_*}A_*^2 e^{2NM_b}
                       =C_bN e^{2NM_b}.
 \tag{27}
\]
There is no hidden factor from a residue class or a wrap.

Here is an error justification at the asserted relative order.
On a fixed interior neighborhood use the all-order expansion [G, (13)]
in (16). Taylor expansion at (22), in rescaled coordinates of mesh
\(N^{-1/2}\), gives its squared density as a Gaussian times
\(1+N^{-1/2}p_1+O(N^{-1})(1+|v|^L)\), with a Gaussian-polynomial
remainder on a shrinking central neighborhood. The first polynomial
is odd. Gaussian-polynomial mesh sums have exponentially small
sum-to-integral errors uniformly in their fractional centers, by
periodization and the Gaussian Fourier integral as in [G].
The odd term therefore contributes no algebraic first correction.
Negative local curvature controls the intermediate tail; the strict
global maximum, wrap gap and endpoint-uniform factorial estimate
control all other terms exponentially. The proof of [G, (16)]
applies with \(2b\) variables and this density. It yields the relative
\(O_b(N^{-1})\) error in (11), through both parities.

## 6. Orthogonal powers and corrected spectral packets

Conjugation by the physical unitary \(K_{\rm tot}\) is unitary on
matrix Hilbert--Schmidt space. Its eigenvalues on \(T^k\) are \(Q^k\).
Hence the \(N\) powers in (6) are exactly pairwise orthogonal.
The polynomial identity \(T^N=I\) has simple roots, so (12) gives
its complete spectral projectors. Conjugation by \(K_{\rm tot}\)
cycles their eigenspaces; they all have rank \(N^{b-1}\).
Hilbert--Schmidt orthogonality of powers proves the norm identity
in (13). Finite Fourier orthogonality also proves
\(N\sum_jP_j^*P_j=J_{\rm av}\) exactly.
Thus this canonical positive Gram orthogonalizes the actual spectral
packets, with their physical sizes and history sum explicitly known.

At \(b=1\) there is also an exact normalization check. Writing
\(B_N=\sum_{a=0}^d s_a^{-2}\), (15) and reflection give
\(\mathcal H_N=(\sum_a s_a^2)(\sum_a s_a^{-2})=N^2B_N^2\).
Formula (8) gives \(C_1=1/\sqrt3\), consistently with (11).

## 7. What this supplies to the original source

The theorem computes a positive history sum and a sharp invariant-metric
rate for an actual coproduct, including every wrapped physical entry.
It does not make the original pivotal tail functional a norm.
The original \(g=K^{1-N}\), marked projection, neighboring crossings,
and all their transported interfaces must remain when using this Gram.
The source freedom invoked in Section 1 concerns the whole assembled
selected knot operator; it does not identify arbitrary local sectors.
The intermediate tensor-product Casimir and multiplicity channels are
not replaced by one-head scalar eigenvalues.

Already at \(b=1\) this positive metric rate is nonzero, although a
normalized unknot cut has value one. Therefore neither (11) nor (13)
is a Kashaev nonvanishing statement, a selected geometric coefficient,
or a hyperbolic-volume lower bound. General short-component propagation
and the finite-exception volume assertion remain open.

[C] already proves conditioning lower bounds for a different actual
cyclic Wall operator. [F] already gives sharp positive angle costs for
actual divided fusion in its source-fixed factorial metric.
The addition here is the matching upper and lower optimal distortion
rate in the original physical metric, together with (11)--(13) for
this cyclic-source coproduct. No novelty is claimed for finite-group
averaging, quantum multinomials, or the bipyramid volume formula.

## Complete inputs and coverage

All five complete matching texts were read. Only written mathematics
and text/hash operations were used. No earlier final was edited.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| B, source, 247 lines | [Balanced cyclic source](balanced_verma_coherent_braiding.md) | 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4 |
| M, source, 602 lines | [Actual coproduct and complete multiplicities](actual_complete_source_multiplicity_module.md) | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| G, estimates, 306 lines | [Physical sine-factorial Gaussian bounds](research_full_physical_crossing_gaussian_packet.md) | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| C, coverage, 257 lines | [Cyclic Wall conditioning](research_mixed_fourier_wall_cyclic_conditioning.md) | f8e2691bc4f816058f4bbb9d3f3b51858d3f2db153ec65d49c55e618a0c09d2e |
| F, coverage, 286 lines | [Source-fixed divided fusion norm](actual_source_fixed_divided_fusion_norm.md) | 65c3eac321ef680199c86d1775e0044b70b2886e2e1b1fd7d8404367c61750e4 |
