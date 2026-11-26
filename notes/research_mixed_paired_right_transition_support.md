# Two incident blocks at an unselected right transition

Research proof, 4 November 2026. The universal 2,048-product outward
cover and independent written/code review have passed. Completed
source artifacts are unchanged.

## 1. Actual reference, common cutoff, and bound

Write
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \quad
 \phi_{\eta\epsilon}(a,b)
 =Q_\epsilon(s_*;a,b)-(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \tag{1}
\]
with the literal logarithmic root and original normalization of the
[full right-square packet](research_mixed_unselected_right_taper_products.md).
Take three consecutive actual outer legs \(z=(a,b,c)\) of a cyclic
word, with indicators \((\alpha,\beta,\gamma)\), and put
\[
 F(z)=\phi_{\alpha\beta}(a,b)+\phi_{\beta\gamma}(b,c),
 \quad \Gamma_z(w)=F(z)+F'(z)\cdot(w-z).
 \tag{2}
\]
For real \(p,q\in P=[.22,.45]\) and \(t\in[.45,.5]\), set
\[
 \tau=20(.5-t),\qquad
 w=(p,t,q)+i\tau(\Im a,\Im b,\Im c),
 \quad C(z)=\frac{151}{20}(\Im a)^2+\frac{11}{2}(\Im c)^2.
 \tag{3}
\]
All three coordinates are unselected. Their common fraction in (3)
is essential and is not replaced by independent height intervals.

**Theorem 1.** Uniformly over every
actual finite cyclic word and the displayed targets,
\[
 \Re\{F(w)-\Gamma_z(w)\}+(1-\tau)^2C(z)<-1/125.
 \tag{4}
\]
The complete original pair of allocated finite kernels consequently
has rate at most
\[
             \Re\Gamma_z(w)-(1-\tau)^2C(z)-1/250.
 \tag{5}
\]
Polynomial losses and both parities are retained. Half-moduli are
allocation notation; derivative assertions apply only to the resulting
original holomorphic products with integer powers.

## 2. Boundary source comparison, retaining height dependence

Use a five-vertex open window with original right legs
\(t_0,\ldots,t_4\), and choose \(z=(t_1,t_2,t_3)\). Its two
external legs lie in the established rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                              \tag{6}
\]
Whole-product holomorphy and uniqueness come first from the
[open-window theorem](research_mixed_cyclic_critical_height_bounds.md).
The original middle stationary equation gives \(F_b(z)=0\) on this
whole branch. In particular, (2) retains the two outside complex
gradient terms, without an artificial independent-reference equation.

There are 32 ordered five-vertex words, four external type pairs,
and sixteen external-side products, giving 2,048 boundary products.
Each has three real parameters: the two external-side coordinates
and \(v=20(t-.45)\in[0,1]\). The full outward cover checks
\[
 \begin{split}
 .24<\Re z_j<.40,\qquad |\Im z_j|&<.063,\\
 B_\ell:=\sum_{i,j=1}^3
 |(\partial_\ell z_i)(\partial_\ell z_j)F''_{ij}(z)|&<1/5
                                      \quad(\ell=1,2),\\
 D:=\Re\{F(w)-\Gamma_z(w)\}+(1-\tau)^2C(z)&<-1/100.
 \end{split}                                             \tag{7}
\]
The first two bounds do not depend on \(t\), but retaining them on
every accepted cell simplifies complete coverage verification.

The image bounds in (7) extend over the external rectangle product
by harmonic maximum principles. Each summand defining \(B_\ell\)
is the modulus of a holomorphic function, so its sum also extends
by successive subharmonic maximum principles. This use of the
boundary is legitimate for these quantities, not automatically for
the height-dependent defect \(D\).

For all auxiliary targets with real coordinates in \([.22,.5]\)
and heights of modulus at most .063,
\[
 |\Im\cot(\pi w_j)|
 \le\frac{\sinh(.126\pi)}{\cosh(.126\pi)-\cos(.44\pi)}
 <1/2.                                                    \tag{8}
\]
The maximum follows by monotonicity in the cosine and in absolute
height; the latter derivative is positive since
\(\cosh(.126\pi)\cos(.44\pi)<1\).
The real cotangents are nonnegative. The
[closed-cotangent theorem](research_mixed_closed_cotangent_roots.md)
therefore gives the original holomorphic conditional branch and
\(-\Re\phi''>0\) throughout the auxiliary target products, including
real endpoint .5. Summing the two blocks gives \(-\Re F''>0\).
This auxiliary assertion concerns phase and curvature; it does not
enlarge a finite-source packet.

Apply the [height-coupled reference lemma](research_mixed_height_coupled_reference_extension.md)
to (7), holding \(p,t,q,\tau\) fixed while differentiating the
references. Both external rectangle widths are at most \(.05\).
The total extension cost is at most
\[
 \frac{\tau}{4}\sum_{\ell=1}^2B_\ell h_\ell^2
 \le\frac14\cdot\frac15\cdot2(.05)^2=\frac1{4000}.
 \tag{9}
\]
Since \(1/100-1/4000>1/125\), the certified bounds (7) prove (4).

## 3. What each boundary cell checks

The original ten-variable logarithmic affine Newton self-map is the
unchanged open-window primitive. Its positive weighted radii and
strict contraction identify the original zero lift. The response
matrix \(T=\partial z_{\rm full}/\partial(a_{\rm ext},b_{\rm ext})\)
is enclosed using the exact differentiated equations, the residual
and four Neumann corrections, and a weighted row-norm tail. Global norms maximize outward
upper endpoints explicitly. No floating root or matrix inverse has
acceptance authority.

The phase derivatives are the exact condensed Hessians, including
both chirps and the allocated half-factorials. At a rational target
support point \((p_0,q_0)\in P^2\), real concavity gives the complete
target bound
\[
 \max_{p,q\in P}D\le
 D(p_0,t,q_0)
 +\max_{p\in P}G_p(p-p_0)
 +\max_{q\in P}G_q(q-q_0),                                \tag{10}
\]
where \(G_p=\Re(F_a(w)-F_a(z))\), and similarly for \(G_q\).
The maxima in (10) are just the two endpoint maxima of affine
functions. A floating optimizer proposes \(p_0,q_0\) only; the
checker tests their rational values and all terms of (10) outward.

For each real parameter differential, let \(R=dz\), \(W=dw\).
The exact differential used for the mean-value enclosure is
\[
 dD=\Re\{(F'(w)-F'(z))\cdot W
                -(F''(z)R)\cdot(w-z)\}
       +d\{(1-\tau)^2C(z)\}.                             \tag{11}
\]
For an external parameter, \(W=i\tau\Im R\). For the normalized
cutoff parameter \(v\),
\[
 R=0,\quad W=(-i\Im a,\ .05-i\Im b,\ -i\Im c),\quad
 d\{(1-\tau)^2C(z)\}/dv=2(1-\tau)C(z).
 \tag{12}
\]
The derivative of either tangent slope in (10) is the corresponding
row of \(F''(w)W-F''(z)R\). Thus the whole three-dimensional cell,
not only its midpoint or its edge, satisfies the accepted bound.
The midpoint target root uses a fresh radius \(10^{-10}\)
contraction, because its reference input already carries the
window enclosure of order \(2^{-40}\). The contraction, chamber,
and original residual are checked at this radius.

Every accepted binary leaf is checked. Each internal node records
its split axis and partitions that coordinate into its exact two
rational halves. Reference-only failures split an external parameter;
other failures may split any of the three parameters. This affects
efficiency only. Prefix freedom, exact dyadic mass one, the exact set
of internal prefixes, and the complete ordered 2,048-case set verify coverage.
Source/proof/code/record hashes are frozen before and after a run.
The optional saved-address replay reevaluates every inequality;
stored decimal maxima are never acceptance inputs.

The complete 256-bit cover passed all 2,048 products, with 68,903
accepted cells and 135,758 visits. The largest certified boundary
defect is below \(-.01000153\), and the two response sums remain
below \(1/5\). The record preserves the original numerical run and
its original proof hash when this proof-only status and count update
is recorded; it does not describe that update as a new numerical run.

## 4. Finite-source and isolated-star scope

An actual cyclic reference is the corresponding open-window root,
by uniqueness. Repeat a period before taking the window when its
length is less than five; all repeated equations are retained.
Its actual target heights lie in the unchanged full right-square
finite-source domain. At unselected type-four targets,
\(h\le0\) and \(0<x\le.5\), so the genuine Fourier upper rate is
\(\max\{-\Re g,0\}+\delta=-\Re g+\delta\), including the forcing
value at .5. Choosing the fixed tolerance small enough in the two
allocated blocks gives (5). No row, alias, or forcing contribution
is discarded, and no finite-source assertion is made for auxiliary
window references outside the already proved packet domain.

When there is one right-transition coordinate, both its neighbors
are plateau coordinates, and the two next coordinates are also
plateau coordinates, the minimum-neighbor graph has exactly the
three lowered heights in (3). Each outside block has one height
changed by \(-(1-\tau)\Im a\) or \(-(1-\tau)\Im c\).
The proof of the oriented reset bound, integrated over this shorter
segment in its unchanged convex source domain, costs respectively
\((151/20)(1-\tau)^2(\Im a)^2\) and
\((11/2)(1-\tau)^2(\Im c)^2\), with both real coordinates free.
These are precisely the debits in (3). Hence the four distinct
blocks retain a strict gap. This four-block interpretation requires
length at least four; at length four the common outer coordinate
does not identify any of the four blocks.

This note does not allocate overlapping transition stars, prove
arbitrary transition clusters, handle selections, or complete the
whole outer-period estimate. Those tasks remain separate from this
local bound.

Reproduction and saved-cell replay:

```sh
python experiments/certify_mixed_paired_right_transition_support.py --precision 256
python experiments/certify_mixed_paired_right_transition_support.py --precision 320 --input repro/results/research-mixed-paired-right-transition-support.json --output /tmp/mixed-paired-right-transition-review.json
```
