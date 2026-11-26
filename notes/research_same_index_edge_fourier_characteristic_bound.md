# A Fourier characteristic bound for the actual same-index edge source

Private written proof, 23 November 2026.

The actual same-index edge kernels satisfy a homogeneous, fixed-degree
quantum-torus equation on their entire Laurent polynomials. An exact
Gaussian analysis frame turns that equation into a quantitative bound:
outside its real characteristic set, the normalized Fourier energy is
at most \(C/(N\delta^2)\). The estimate also holds before vertex gluing
for arbitrary coupled channel coefficients on any fixed graph.

All Laurent coefficients and endpoint channels are retained. The norm
here is the Fourier coefficient norm in separate incidence activities.
It is not identified with a marked cap norm or a closed knot invariant.

## 1. The literal edge family and its equation

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\qquad
 S_k=\prod_{j=1}^k2\sin(\pi j/N),\quad S_0=1.
 \tag{1}
\]
The actual common Newton basis in [F] is
\(e_k(X)=S_k^{-2}\prod_{j=0}^{k-1}(2\cos((2j+1)\pi/N)-X)\).
Consequently its complete angular Laurent representative is exactly
\[
 B_k(z):=e_k(-z-z^{-1})
 =\frac{q^{-k^2}(-qz;Q)_k(-q/z;Q)_k}{S_k^2},
 \qquad 0\le k\le d.
 \tag{2}
\]
Indeed each paired factor on the right is
\(q^{-(2j+1)}(1+q^{2j+1}z)(1+q^{2j+1}/z)
 =2\cos((2j+1)\pi/N)+z+z^{-1}\).
No denominator in (2) vanishes.

Write \(T_zf(z)=f(Qz)\), and put
\[
 a_z=1+qz,\quad b_z=1+q^{-1}/z,\qquad
 A_z=a_zT_z-b_z,\quad D_z=b_zT_z-a_z.
 \tag{3}
\]
The two shifted products in (2) give the cleared identity
\[
 (a_z+Q^kb_z)B_k(Qz)=(b_z+Q^ka_z)B_k(z),
 \qquad A_zB_k=-Q^kD_zB_k.
 \tag{4}
\]
For example, before clearing, their quotient is
\((1+qQ^kz)b_z/[a_z(1+q^{-1}Q^k/z)]\).
The denominator times \(B_k(Qz)\) is cleared in (4), so the proof
includes its zeros, \(k=0\), \(k=d\), and both level parities.

For arbitrary complex numbers \(\mu_0,\ldots,\mu_d\), define
\[
 K_N(z,y)=\sum_{k=0}^d\mu_k B_k(z)B_k(y),\qquad
 P_N=A_zD_y-D_zA_y.
 \tag{5}
\]
The two terms in \(P_N[B_k(z)B_k(y)]\) agree by (4). Thus

\[
                         P_NK_N=0
 \tag{6}
\]
as an identity of full Laurent polynomials. It holds for arbitrary
activity-independent insertion weights, and with any channel cutoff
implemented by zero coefficients. No channel shift or partial summation
has produced an endpoint current.

The physical coefficients in [F] include
\(\gamma_e(s)H_N(s)/W_k(s)\), with their prescribed orientation
scalars. They are independent of both angular activities and hence
are examples of (5), at every parameter where they are defined.
The same assertion applies to finite Laurent coefficients of those
weights: it does not require their positivity or a bound on their size.

There is also a coupled version. For a fixed graph with \(E\ge1\)
edges, give every edge two separate incidence variables \(z_e,y_e\),
and allow any complex coefficient array:
\[
 F_N(\mathbf z,\mathbf y)=
 \sum_{\mathbf k\in\{0,\ldots,d\}^E}
 \mu_{\mathbf k,N}\prod_{e=1}^E B_{k_e}(z_e)B_{k_e}(y_e).
 \tag{7}
\]
The coefficients may couple every channel and depend on the level
and all nonangular source parameters. With \(P_{e,N}\) acting only
on its own incidence pair, (4) proves \(P_{e,N}F_N=0\) for every
edge. No independence of the edge coefficients is assumed.
Every individual Laurent exponent in (7) lies between \(-d\) and \(d\).

## 2. An exact full-lattice Gaussian frame

For a dimension \(n\ge1\), identify Laurent Fourier coefficients
with \(f\in\ell^2(\mathbb Z^n)\). Fix \(\sigma>0\), let

\[
 \begin{split}
 c_{N,n}&=(N/(\pi\sigma))^{n/4},\\
 (\mathcal F_Nf)(\theta,\xi)
 &=c_{N,n}\sum_{m\in\mathbb Z^n}
 e^{-|m-N\xi|^2/(2\sigma N)}e^{im\cdot\theta}f_m,\\
 d\nu&=\frac{d\theta}{(2\pi)^n}\,d\xi,
 \quad\theta\in\mathbb T^n,\quad\xi\in\mathbb R^n.
 \end{split}
 \tag{8}
\]
First define this on finitely supported vectors. Integration in
\(\theta\) removes cross terms, and
\[
 c_{N,n}^2\int_{\mathbb R^n}
       e^{-|m-N\xi|^2/(\sigma N)}d\xi=1.
 \qquad
 \int|\mathcal F_Nf|^2d\nu=\|f\|_2^2.
 \tag{9}
\]
This extends \(\mathcal F_N\) isometrically to the full lattice.
The centers range over all of \(\mathbb R^n\); they are not cut off
at a finite Fourier support boundary. The frame principle is the
same elementary resolution already used in [G], with a full lattice
here rather than a finite Newton interval.

Let \(Z_j\) mean multiplication by the \(j\)-th Laurent variable,
so \((Z_jf)_m=f_{m-e_j}\), and let
\((T_jf)_m=Q^{m_j}f_m\). Both are unitary on the full lattice.
For integer vectors \(a,b\), set
\(z^a=e^{ia\cdot\theta}\), \(Y^b=e^{2\pi ib\cdot\xi}\).
The following errors have exact norms:
\[
 \begin{split}
 \|\mathcal F_N Z^af-z^a\mathcal F_Nf\|_{L^2}^2
 &=2(1-e^{-|a|^2/(4\sigma N)})\|f\|_2^2,\\
 \|\mathcal F_N T^bf-Y^b\mathcal F_Nf\|_{L^2}^2
 &=2(1-e^{-\pi^2\sigma|b|^2/N})\|f\|_2^2.
 \end{split}
 \tag{10}
\]
For the first identity, reindex \(m\mapsto m+a\) and integrate the
squared difference of two translated real Gaussians. Their normalized
overlap is \(e^{-|a|^2/(4\sigma N)}\). For the second, angular
integration leaves \(|Q^{b\cdot m}-e^{2\pi ib\cdot\xi}|^2\)
against the squared window. Its Gaussian characteristic function is
\(e^{-\pi^2\sigma|b|^2/N}\). These computations are independent
of the lattice index and prove (10) for all \(f\).

For a normal-ordered, fixed-degree quantum-torus polynomial
\(P_N=\sum_{a,b}c_{ab,N}Z^aT^b\), define
\(p_N(\theta,\xi)=\sum_{a,b}c_{ab,N}z^aY^b\).
Assume its finite exponent set and coefficient bounds are uniform.
Applying (10) first to \(Z^aT^bf\), then to \(T^bf\), and summing
gives
\[
 \|\mathcal F_N(P_Nf)-p_N\mathcal F_Nf\|_{L^2}
                  \le C_{P,\sigma}N^{-1/2}\|f\|_2.
 \tag{11}
\]
All noncommutative ordering phases stay in the coefficients \(c_{ab,N}\).
The proof uses full shifted output vectors, without a finite compression.

## 3. The actual real characteristic bound

For (5), its exact left-ordered expression and symbol are
\[
 \begin{gathered}
 c_{1,N}=a_zb_y-b_za_y,\qquad c_{2,N}=b_zb_y-a_za_y,\\
 P_N=c_{1,N}(T_zT_y-1)+c_{2,N}(T_z-T_y),\\
 p_N=c_{1,N}(z,y)(Y_zY_y-1)+c_{2,N}(z,y)(Y_z-Y_y).
 \end{gathered}
 \tag{12}
\]
On the frame phase space, \(|z|=|y|=|Y_z|=|Y_y|=1\).
The coefficient bounds and exponent set are absolute, uniformly
for every \(N\ge2\). As \(q\to1\), the symbol differs by \(O(N^{-1})\)
uniformly from
\[
 p_0=
 \frac{(1+z)(1+y)}{zy}
 \{(z-y)(Y_zY_y-1)+(1-zy)(Y_z-Y_y)\}.
 \tag{13}
\]
The prefactor in (13) is retained. In particular its zeros at
\(z=-1\) or \(y=-1\) are part of this characteristic set.
No division by that factor is used.

Apply (11) to the exact null vector (6), and use (9) to replace
\(p_N\) by \(p_0\). This proves, without a source hypothesis,
\[
 \int|p_0|^2|\mathcal F_NK_N|^2d\nu
                      \le\frac{C_\sigma}{N}\|K_N\|_2^2,
 \quad
 \int_{\{|p_0|\ge\delta\}}|\mathcal F_NK_N|^2d\nu
                \le\frac{C_\sigma}{N\delta^2}\|K_N\|_2^2
 \quad(\delta>0).
 \tag{14}
\]
Here \(n=2\). The norm is exactly the full Laurent coefficient norm.
The constant is independent of all coefficients \(\mu_k\).
If the kernel is zero, the same inequalities hold trivially.

For (7), use \(n=2E\), and let \(p_{e,0}\) be (13) on its
edge coordinates. Tensoring the frame calculations, or applying
(10) in those two coordinates only, gives
\[
 \int\sum_{e=1}^E|p_{e,0}|^2|\mathcal F_NF_N|^2d\nu
                   \le\frac{C_\sigma E}{N}\|F_N\|_2^2.
 \tag{15}
\]
In particular the mass on \(\{\max_e|p_{e,0}|\ge\delta\}\),
outside the common \(\delta\)-characteristic neighborhood, is at
most \(C_\sigma E/(N\delta^2)\) times the full mass. This holds
for arbitrary entangled channel weights, not only products of
independent edge kernels.

## 4. Normalized angular jets retain their forcing

Let \(\mathscr D_j=z_j\partial_{z_j}\), including every incidence
variable, and let \(\mathcal A\) be a fixed finite downward-closed
set of multiindices containing zero. Define the actual jet vectors
\[
 u_\alpha=N^{-|\alpha|}\mathscr D^\alpha F_N,
                           \qquad\alpha\in\mathcal A.
 \tag{16}
\]
Since each Fourier exponent of (7) is in \([-d,d]\),
\(\|u_\alpha\|_2\le\|F_N\|_2\). These derivatives do not
automatically satisfy the homogeneous equation. The exact product
rule, because every \(\mathscr D_j\) commutes with the shifts, is
\[
 P_{e,N}u_\alpha=
 -\sum_{\beta<\alpha}\binom\alpha\beta
 N^{-(|\alpha|-|\beta|)}
       (\mathscr D^{\alpha-\beta}P_{e,N})u_\beta.
 \tag{17}
\]
Here \(\beta<\alpha\) means componentwise inequality and inequality
somewhere, and \(\mathscr D^\gamma P\) differentiates its coefficients
only. Every resulting fixed-degree operator has uniformly bounded
norm. Thus the right side of (17) is \(O(N^{-1})\) as an operator
on the fixed direct sum of predecessor jets. Applying (11) to each
jet, including that residual, proves
\[
 \begin{split}
 \int\sum_e|p_{e,0}|^2
       \sum_{\alpha\in\mathcal A}|\mathcal F_Nu_\alpha|^2d\nu
 &\le\frac{C_{\sigma,\mathcal A}E}{N}
                        \sum_{\alpha\in\mathcal A}\|u_\alpha\|_2^2.
 \end{split}
 \tag{18}
\]
Its off-characteristic version has the additional factor \(\delta^{-2}\).
All jet coordinates and their commutator forcing remain. This is
not an assertion about moving-quantum-parameter derivatives or an
automatic conversion of angular derivatives to Casimir normals at
parabolic angles.

## 5. What remains at the original gluing

The fixed graph and arbitrary coefficient array in (7) give a broad
pre-gluing source class, including physical insertions and retained
low or high channel sums. The actual vertex operations in [F] still
identify incidence activities, multiply by their prescribed crossing
polynomials, reduce in their proper relations, and apply the original
marked functionals. Those operations, with all their scalar factors,
remain the original closing map \(\Lambda_N\); none is replaced by
the positive Fourier norm above.

In particular (15) does not commute a positive phase-space cutoff
through \(\Lambda_N\), nor bound its effect on the complementary
normal channels. No ordinary-color Plancherel energy is identified
with this norm. The real variables in (8) describe a unitary torus
phase space, not a complex hyperbolic critical chart. The estimates
are polynomial concentration bounds, not exponential complementary
gaps, a selected geometric cycle coefficient, or a scalar lower bound.
They impose the explicit relation (13) on the full normalized source
energy before those remaining operations.

## Complete inputs and coverage

The sole complete original-source proof direct is [F],
`papers/circle-tree-asymptotics/finite-bounds.tex` (227 lines),
SHA256 `e4cf66544703af6d9a78208deae971c4d9f4367ba4b2ad660694ee489ef67ea1`.
Its basis, edge weights, and full marked source are used above.
All new finite identities and Gaussian estimates are proved inline.

Complete comparison texts read are the companion
`papers/circle-tree-asymptotics/edge-packet.tex` (268 lines),
`53eb6dbfbda3ca639db35911ed50947c29655840337f9d1f1ce909d435013dbb`;
[G], `notes/research_gaussian_frame_newton_transport.md` (335 lines),
`b6ed7fa19097323f76b0b22fb4fc7361b9d4e52c3f19d17c12d94c6fff623af9`;
`notes/research_finite_gabor_pointed_source_sewing.md` (455 lines),
`8a954f9f2bec9e0fc8971b08ea0ca493f712d4e2ace6bb9fc2c1fcf705699c37`;
`notes/actual_pointed_a_bulk_agmon_energy.md` (199 lines),
`df1bccf577f5732dd7697bf2ae03901077d63b48f85820544dba10395391effd`;
and `notes/actual_pointed_a_interval_observability.md` (215 lines),
`2e35ceb58d9488b7b383bbce4af123243270ddeff86570eff8ac20efb010b136`.
The Gaussian frame and off-characteristic method are standard;
no novelty is claimed for that general calculus. The specific result
here is its quantitative application to the exact edge source (5),
the coupled source (7), and their retained angular jets.
Only written mathematics and source-text/hash operations were used.
