# Complete free boundaries in the local marked Fourier source

Private written assembly corollary, 16 November 2026.

The retained Fourier-sector theorem describes a literal factorial
germ. The original source instead retains cardinal polynomials at
free endpoints, even when their boundary value is complete. The
archived complete-boundary comparison closes this local placement
gap at every target admitted by that theorem. Its use is incidence
by incidence, before ordinary multiplication at a shared boundary.
The result does not identify a coefficient of the original cycle.

## 1. The boundary factors at an admitted target

Use the same-index tree, selected set \(S\), powers, marking, and
admitted positive or classified radial limiting target of the pinned
Fourier-sector theorem. In particular the selected angles satisfy
\(|\Re t_v|<\pi\), \(\Im t_v<0\), and outside angles are zero.
Every retained edge has its original independent index \(x_e\).
Write \(\mathcal I_\partial\) for its free outside incidences.

Each edge meeting a complete outside endpoint is strictly positive,
including at the classified limits. Here this also follows directly.
For its other angle \(t=s-iH\), the continued edge square root is
\[
 q=\sec(t/2),\qquad a=\tan(t/2),\qquad
 \Re q=\frac{\cos(s/2)\cosh(H/2)}{|\cos(t/2)|^2}
      >|\Re a|
       =\frac{|\sin(s/2)|\cos(s/2)}{|\cos(t/2)|^2}.
 \tag{1}
\]
The inequality uses \(|s|<\pi\); it also covers \(t=0\).
The root agrees with the original positive approach and cannot
switch sign. Thus its canonical stationary index satisfies
\[
                 \cot(\pi x_e^*)=q,\qquad
                         0<\Re x_e^*<1/2.
 \tag{2}
\]
The inverse cotangent is the branch continued from \(q=1\).
The right half-plane maps to this open strip. Finitely many free
incidences therefore have a common compact margin in (2).

Put \(D=N-1\), \(\eta=(-1)^D\),
\(P_N(z)=2T_N(z/2)+2\), and retain the original factors
\[
 \begin{split}
 \widetilde B_N(x,z)
   &=\sum_{j=0}^{D}
       \frac{\sin(\pi N(x-j/N))}{N\sin(\pi(x-j/N))}\,e_j(z),\\
 B_N(x,u)
   &=\frac{N}{
       G_N(D/2-Nx+Nu/(2\pi))
       G_N(D/2-Nx-Nu/(2\pi))G_N(Nx)^2}.
 \end{split}
 \tag{3}
\]
The first is the prescribed ordinary polynomial of degree at most
\(D\). At traced endpoints the full Hermite classes agree; this
alone would not justify replacing a free endpoint.

Choose a slightly larger compact rectangle
\(0<\alpha\le\Re x\le\beta<1/2\), \(|\Im x|\le H_0\),
containing all the indices in (2). The pinned boundary-comparison
theorem supplies fixed \(r,\delta>0\) and a neighborhood of this
rectangle on which
\[
 \frac{\widetilde B_N(x,-2\cos u)}{B_N(x,u)}
       =1+O_{\rm hol}(e^{-\delta N}),\qquad |u|<r.
 \tag{4}
\]
Its factorial expansion has leading term
\[
 B_N(x,u)
   =\frac{e^{Nb(x,u)}}{2N\sin(\pi x)}(1+O_{\rm hol}(N^{-1})).
 \tag{5}
\]
Here \(b(x,u)=-J(1/2-x+u/(2\pi))-J(1/2-x-u/(2\pi))-2J(x)\),
where \(J'(z)=\log(2\sin\pi z)\) is continued from \((0,1)\)
and \(J(0)=0\). All these arguments stay in that canonical strip
on the neighborhood being used.
Consequently the denominator in (4) is a holomorphic unit on a
fixed smaller neighborhood for all sufficiently large \(N\).
No all-level unit assertion is required or made.

## 2. Exact local assembly and ordinary shared boundaries

Initially give every \(\iota=(e,b)\in\mathcal I_\partial\) its own
outside angle \(u_\iota\), and define the exact local ratio
\[
 Q_N(\mathbf x,\mathbf u)
   =\prod_{\iota=(e,b)\in\mathcal I_\partial}
       \frac{\widetilde B_N(x_e,-2\cos u_\iota)}
            {B_N(x_e,u_\iota)}.
 \tag{6}
\]
An empty product is one. On a fixed smaller neighborhood of the
target, independently of level parity,
\[
 Q_N=1+O_{\rm hol}(e^{-\delta N}),\qquad Q_N\ne0
                                      \quad(N\ge N_0).
 \tag{7}
\]
Every fixed mixed derivative has the corresponding estimate.
Now identify \(u_\iota=u_b\) for incidences at the same outside
vertex. This substitution preserves (7), by the chain rule and
the fixed finite number of incidences.

All products before and after this substitution are ordinary
boundary products. No reduction modulo \(P_N\) is made at any
outside vertex. In particular the argument does not first multiply
several degree-\(D\) factors and then treat their reduced polynomial
as the prescribed boundary source.

Let \(\Omega_{\rm mix}\) be the exact original joint-lens density:
factorial representatives at traced endpoints and the prescribed
cardinal representatives at free endpoints, with all original
Gaussian, coupon, sine, and \(W_N\) factors retained. Let
\(\Omega_{\rm fac}\) replace also its free endpoints by (3),
on this local neighborhood only. Then the ordinary identity is
\[
                       \Omega_{\rm mix}=Q_N\Omega_{\rm fac}.
 \tag{8}
\]
All original exterior scalar normalizations are the same on the
two sides. Formula (8) is an identity of local densities; it
requires no interpolation of a shared-boundary product.

The derivative claim includes spectral boundary derivatives at
completeness. Each ratio in (6) is even and holomorphic in
\(u_\iota\), so it descends holomorphically through
\(z_\iota=-2\cos u_\iota\) to a fixed neighborhood of \(z_\iota=-2\).
Since \(z_\iota+2=u_\iota^2+O(u_\iota^4)\), this is a regular
change of variable in \(u_\iota^2\). Cauchy estimates on smaller
disks give (7) for every fixed spectral derivative as well.
Identifying the ordinary spectral variables afterward retains
these estimates.

## 3. Deployment of the marked sector

Use precisely the common factor and Fourier multiplier of the
pinned sector theorem:
\[
 \Omega_{\rm fac}
   =N^{-2|E|}e^{N\Phi_c}A_N
       \left(\prod_{v\in S}\sin t_v\right)
       \mathcal R_{N,c}\,d\mathbf x\,d\mathbf t,\qquad
 A_N\sim A_0+\frac{A_1}{N}+\cdots,
 \quad A_0=\prod_{e\in E}(2\sin\pi x_e)^{-2}.
 \tag{9}
\]
The original nonzero exterior scalar is suppressed on both sides
of (9), exactly as in that theorem. The free incidence arguments
remain in their positive-real-part factorial strip on the chosen
neighborhood; hence they introduce no additional wall factors.
Its formulas extend holomorphically to the small independent
outside angles used in (6).

Specifically \(\Phi_c=S_{\rm geom}
+\sum_{v\in S}(in_vt_v^2/(4\pi)-ic_vt_v)\), where
\(S_{\rm geom}\) is the sum of the original marked incidence
primitives, using the above \(b(x_e,u_\iota)\) at a free end.
If \(\mathcal B\) is the fixed wall list of the cited theorem,
\(z_j=1/2-x_e+\varepsilon_jt_v/(2\pi)\) and
\(\sigma_j\in\{-1,1\}\) are its retained affine arguments and
marking signs, then
\[
 \mathcal R_{N,c}
   =\prod_{j\in\mathcal B}(1+e^{-2\pi iN\sigma_jz_j})
      \prod_{v\in S}
       \frac{\tfrac12(1+e^{-2iN(1-c_v)t_v})}
            {(1-\eta e^{-iNt_v})^2}.
 \tag{9a}
\]
No member of \(\mathcal B\) is a free outside incidence.

Define the exact common unit
\[
                         \widehat A_N=A_NQ_N.
 \tag{10}
\]
Equations (7)--(10) represent the original mixed source with the
same marked action and the same explicit multiplier
\(\mathcal R_{N,c}\). The all-order holomorphic expansion of
\(\widehat A_N\) is identical to that of \(A_N\), including all
fixed ordinary boundary derivatives. The factor \(Q_N\),
exponentially close to one, is absorbed into this specified common unit; it is
not assigned an independent Fourier expansion.

It follows that the marked-frequency coefficient of the retained
multiplier is still \(\mathcal M\ge1\) for unit charges, and
\(2^{-|S|}\mathcal M\) for common charge \(1/2<\chi<1\), with
\(\mathcal M\) exactly as in the sector theorem. The leading
marked symbol of the original mixed density is therefore
\[
 A_0\left(\prod_{v\in S}\sin t_v\right)
       \begin{cases}
         \mathcal M,&c_v=1,\\
         2^{-|S|}\mathcal M,&c_v=\chi\in(1/2,1).
       \end{cases}
 \tag{11}
\]
It is nonzero at the target, at both level parities. The exact
identities and expansions may be differentiated in the free
boundary variables; this does not assert that each differentiated
coefficient is nonzero. For example odd angular derivatives at
completeness vanish by evenness.

This completes the free-complete-boundary local deployment of that
specific marked-sector calculation. It does not make its coefficient
independent of the chosen common-factor normalization, prove a
pointwise lower bound for the sum of competing sectors, or place
the marked descending disk in the original relative cycle.
Exponentially small terms in the common unit may still interact
with exponentially larger competing sectors in a period estimate.
No estimate on a full index period, connecting chain, or original
closed scalar is inferred.

Only the same-index edges of the cited theorem are covered.
A reversed free halfwire whose actual argument is \(D/N-x_e\)
need not satisfy (2); it requires its own valid boundary chart.
The local neighborhood here cannot be enlarged to cover such an
argument by reducing or resetting its index.

## Direct sources and author readback

The following four complete sources and their directly used
implications were read at the pinned versions.

* [Marked tree Fourier sector](research_tree_factorial_marked_fourier_sector.md),
  SHA256 05dfd92e125f70af4df441efcad2f5766f4ff7168afcaf57c2eec9e67e305e14:
  admitted targets, original common factor and Fourier marking,
  positive resonances, and the explicit free-boundary limitation.
* [Complete-boundary cardinal/factorial comparison](research_free_boundary_cardinal_factorial_comparison.md),
  SHA256 9ed5b69bad33d7e62a7b40070d86d9d2233f2c34bc7674ddcf8a82e8e0091d5d:
  the already established exponentially small comparison on a
  complex complete-boundary disk, both parities and all fixed
  derivatives, including its restriction to low wire indices.
* [Joint factorial-lens source](research_joint_factorial_lens_relative_source.md),
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54:
  exact mixed-source placement, original normalization and full
  Hermite data, and unreduced ordinary free-boundary variables.
* [Radial two-square primitive lift](research_radial_two_square_primitive_lift.md),
  SHA256 21d9af750653621cc82bd73373a99a138210fc4cdb10407faabcb209505df9ad:
  canonical angular bounds at the classified limits, complete
  outside endpoints, and the original continued square roots.

The contribution is this assembly corollary, not a new boundary
comparison estimate. Only written proofs, source-text reads and
hashes were used. No mathematical program, numerical calculation,
test or compilation was run. Frozen sources, manuscripts and
public documents were unchanged.
