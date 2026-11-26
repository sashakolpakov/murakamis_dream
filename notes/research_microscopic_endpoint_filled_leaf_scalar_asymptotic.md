# The whole filled-leaf scalar with microscopic endpoint products

Private written proof, 16 November 2026.

For every fixed signed power of magnitude at least three, the original
one-vertex trace at complete output has the same exponential action
after multiplication by any fixed number of microscopic endpoint
kernels with bounded real parameters. Its actual leading coefficient
is nonzero, although it can depend polynomially and oscillate in the
level. The proof joins every original contour piece; it is not a
lower bound inferred from one local saddle alone.

The upper estimate also retains bounded complex endpoint parameters
and fixed complete-output derivatives. No corresponding derivative
lower bound, complex-parameter lower bound, or geometric volume
identification is asserted.

## 1. Original source and statement

Put
\[
 h=N^{-1},\quad D=N-1,\quad \eta=(-1)^D,\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 C_N(x)=2\cos(2\pi x+\pi h),\quad
 t=\pi-2\pi x-\pi h.
 \tag{1}
\]
Use the original Newton kernel and full trace
\[
 K_N(C,Z)=\sum_{k=0}^{D}e_k(C)e_k(Z),\qquad
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),\quad
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),
\]
\[
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
       \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
                +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{2}
\]
For a fixed integer \(r\ge0\), define
\[
 B_N(C;\boldsymbol\alpha)=
       \prod_{i=1}^rK_N(2\cosh(\alpha_i/N),C),\qquad
 L_{N,n}(Z;\boldsymbol\alpha)
       =\phi_N[R_N^n B_N K_N(\cdot,Z)] .
 \tag{3}
\]
The original crossing has angular representative
\[
 E_{N,n}(x)=\mathfrak c_{N,n}e^{inNt^2/(4\pi)},\qquad
 \mathfrak c_{N,n}=e^{\pi i nD^2/(4N)}.
 \tag{4}
\]
It represents its original physical values and first normals. All
products in (3) are formed before applying (2).

Fix \(n=\sigma m\), where \(m\ge3\) and \(\sigma=\pm1\).
The phase constant is fixed by
\[
 \psi(t,0)=\int_0^{1/2}
       2\operatorname{asinh}\!\bigl(\cos(t/2)\cot(\pi v)\bigr)\,dv,
\]
continued from \(0<t<\pi\). The positive-power selected point
\(t_m=2A_m-iH_m\) is the source's specified branch of
\[
 \operatorname{asinh}(\tan(t_m/2))=im t_m/2-i\pi,\qquad
       0<A_m<\pi/m,\quad H_m>0.
\]
Let
\[
 t_*=2A_m-i\sigma H_m,\qquad
 \Phi(t)=\psi(t,0)+\frac{in}{4\pi}t^2-i\sigma t,\qquad
 \lambda_n=-\Phi''(t_*).
 \tag{5}
\]
These are the calibrated right-angular saddle and phase in the local
source theorem. In particular
\[
 \Phi'(t_*)=0,\qquad \Re\lambda_n>0,\qquad
 \Re\Phi(t_*)=\mathcal I_n>\mathcal I_2=2G/\pi,
 \quad G=\int_0^{\pi/4}\log\cot v\,dv .
 \tag{6}
\]
Let the exact shortened kernel be
\[
 \Lambda_N(t)=
 \sum_{k<\lfloor N/2\rfloor}e_k(-2\cos t)e_k(-2)
              =e^{N\psi(t,0)+E_N(t)}
 \tag{7}
\]
on the fixed saddle neighborhood supplied by that theorem.
There \(E_N\) and every fixed derivative are \(O(\log N)\).
The exponential in (7), rather than a choice of its logarithm,
specifies the coefficient below.

**Theorem.** For every real parameter bound \(A<\infty\), uniformly
for \(\alpha_i\in[-A,A]\), including level-dependent choices,
\[
 \boxed{\quad
 L_{N,n}(-2;\boldsymbol\alpha)=
 \frac{\sigma iN^{3/2}}{\pi}\,\mathfrak c_{N,n}\,
 e^{N\Phi(t_*)+E_N(t_*)}\,
 \mathcal B_N(t_*)\sin t_*
       \sqrt{\frac{2\pi}{\lambda_n}}\,[1+o(1)] .
 \quad} \tag{8}
\]
Choose \(\sqrt{\lambda_n}\) with positive real part. Here
\(\mathcal B_N\) is the actual shared product of the designated-half
sharp physical representatives on the saddle patch, normalized at
one common fixed bulk reference row as specified below. It obeys
\[
 |\mathcal B_N(t_*)|\ge cN^{-r},\qquad
 |\partial_t^k\mathcal B_N(t)|
       \le C_k\left(\frac{1+\log N}{N}\right)^r
 \tag{9}
\]
on a fixed smaller saddle neighborhood. All displayed factors in
(8) are nonzero for sufficiently large \(N\), at both parities.
Consequently
\[
 \lim_{N\to\infty}\frac1N
        \log|L_{N,n}(-2;\boldsymbol\alpha)|=\mathcal I_n
 \tag{10}
\]
uniformly on this real parameter set.

Separately, for every bounded complex parameter set and fixed
multiindex \(\nu\) and integer \(q\ge0\), there are \(C,p\) such that
\[
 \left|
 \partial_{\boldsymbol\alpha}^{\nu}\partial_Z^q
                  L_{N,n}(Z;\boldsymbol\alpha)\big|_{Z=-2}
 \right|\le CN^p e^{N\mathcal I_n}.
 \tag{11}
\]
No nonzero conclusion for the quantities in (11) is implied.
The power, product count and derivative orders are fixed before
letting \(N\) tend to infinity.

## 2. Actual anchors and compatibility of the patch collection

Choose a small fixed fold width \(T>0\) such that the fold theorem's
bound satisfies
\[
                 \mathcal I_2+C T^4<\mathcal I_n .
 \tag{12}
\]
The constant is uniform on the bounded parameter set after fixing
the power and contour heights. Choose the other real endpoint close
enough to \(t=\pi\) that its physical-window bound is below
\(\mathcal I_n\). Between these endpoints take the finite patch
collection of the compact-interface theorem, with the saddle in
the interior of one patch.

All compact patches use the same fixed physical bulk reference
\(x_b=j_b/N<1/2\), to the right of their real buffers. The reference
may vary by \(O(h)\) with the physical grid but remains in a fixed
compact interval. Their cutoff and chart recipes are the compatible
ones of that theorem. This is exactly the two-value normalization
eligible for the actual nonreal insertion estimate.

The fold patch instead uses its physical fold anchor
\[
 j_*=\begin{cases}N/2-1,&N\ {\rm even},\\(N-1)/2,&N\ {\rm odd}.
 \end{cases}
 \tag{13}
\]
Here is the precise comparison needed to join these choices. On the
adjacent cutoff's common real extension to the fold, write
\[
 \mathcal V_f=
 \binom{f(x)}{[f(x)-f(x-h)]/[C_N(x)-C_N(x-h)]},\qquad
 \mathcal F=(\mathcal V_{H_0},\mathcal V_{H_1}),\qquad
 a(x)=\mathcal F(x)^{-1}\mathcal V_{K_N(w,C_N(\cdot))}(x).
 \tag{14}
\]
All quantities are regular in the divided-color frame, including
the fold. The actual ordinary kernel forcing and its angular
derivative vanish at every physical row. The exact coefficient
equation there is
\[
 a(x_j+h)=(I+M_j)a(x_j),\qquad
 \|M_j\|\le CN^p e^{-NI_\delta(x_j)} .
 \tag{15}
\]
The actual vectors \(a(x_j)\) have polynomial norm, by the original
endpoint bound and the uniformly invertible frame. Since
\(I_\delta\) increases towards the fold, summing (15) gives
\[
 |a(j_*h)-a(x_b)|\le CN^p e^{-NI_\delta(x_b)}.
 \tag{16}
\]
Reflecting a last row when necessary changes neither this estimate
nor its constants. The \(O(h)\) offset of the fold anchor costs
only a bounded factor.

Multiplying (16) by the same bounded modes proves an exponentially
small difference of the two actual baselines on the whole fixed
tall overlap. Fixed spatial and parameter derivatives follow from
the same buffered mode bounds. Its saving at \(x_b\) is at least
the saving required at the seam to its left. Thus the fold theorem's
common-anchor join remains valid when the adjacent compact patch
retains its bulk reference: the additional difference (16) is
another jump with the same or better budget.

This also explains why no arbitrary homogeneous normalization enters
the saddle coefficient. On the saddle patch, the insertion theorem
applies directly to its bulk reference. If a fold normalization is
used instead on a common extension, (16) changes that representative
by an exponentially small amount and preserves the lower bound
\(c/N\). The one-sided corrections are exponentially small in the
designated half. Taking the original shared product therefore proves
(9), including its fixed spatial derivatives. No independent normal
has been substituted for either of the two actual anchor values.

## 3. Mirror orientation and the actual local coefficient

For clarity use full angular mirror blocks for the entire partition.
Each double spectral color then occurs twice, and the odd simple
color at the fold occurs once. The full-mirror trace prefactor is
\(-\eta/(4\pi^2i)\), half the positive-angle-only prefactor.
The fold theorem proves this directly from (2), including the odd
simple value and the even last spectral normal.

Set \(\mathcal R x=1-h-x\). Define the representatives on a reflected
compact block by
\[
 H_{\rm mirror}^{-\sigma}(\mathcal R x)=H^\sigma(x).
 \tag{17}
\]
This is an exact choice preserving its mirrored physical jets.
On a fold block it is already the reflection identity of the
weighted repair. With \(D_h=(\pi/h)^2\csc^2(\pi x/h)\), one has
\[
 D_h(\mathcal R x)=D_h(x),\quad
 C_N(\mathcal R x)=C_N(x),\quad
 E_{N,n}(\mathcal R x)=E_{N,n}(x).
 \tag{18}
\]
The sine factor reverses sign. Thus for the complete scalar source
on the corresponding horizontal pieces,
\[
 g_{\rm mirror}(\mathcal R x)=-g(x),\qquad
       d(\mathcal R x)=-dx,\qquad
 \int_{\mathcal R\Gamma}D_h g_{\rm mirror}\,dx
                         =\int_\Gamma D_h g\,dx .
 \tag{19}
\]
The reflected path is exactly the other half's inherited boundary
path: an upper horizontal side directed right-to-left maps to a
lower side directed left-to-right. The two signs in (19) therefore
give addition, with no extra change of integration orientation.
Their two half-prefactors recover the positive-angle-only
prefactor exactly.

In particular the two reflected favored saddle pieces together are
the exact local source
\[
 \frac{\sigma iN^2}{\pi}\mathfrak c_{N,n}
 \int_{-a}^{a}
    \sin t\,\Lambda_N(t)\mathcal B_N(t)
       e^{inNt^2/(4\pi)}
       \frac{e^{-i\sigma Nt}}
            {(1-\eta e^{-i\sigma Nt})^2}\,du,
 \qquad t=t_*+u .
 \tag{20}
\]
This is precisely the local theorem's coefficient, not twice it.
For either sign the rational factor in (20) is the original
sampling kernel on that half; all its aliases are retained before
its leading-sector estimate. The local Gaussian theorem applied
to (20) gives (8) for this paired local piece, with relative error
\(O((1+\log N)^{r+1}/\sqrt N)\).

## 4. Exhaustion of the original trace

We record every term outside (20). The partition is fixed for the
fixed power. Its cuts are physical-grid midpoints differing from
their prescribed real positions by \(O(h)\).

1. Split the outgoing kernel exactly as
   \(K_N=K_N^<+K_N^{\rm hi}\) before deformation. The original
   high-sector trace, including its odd middle term, is polynomial
   with all the stated parameter and output derivatives.
2. At the positive spectral endpoint, the original physical window
   has rate tending to zero with its fixed width. Choose that width
   so its rate is below \(\mathcal I_n\). The adjoining outer
   vertical side is bounded by convexity from its strictly smaller
   real and top endpoint rates. Nothing there is silently canceled.
3. Every compact real interface is strictly below
   \(\mathcal I_2\). Every compact internal seam and horizontal
   repair has a strict \(\mathcal I_n\) gap, with the actual
   difference of the two normalized representatives on each seam.
4. The fold real interface, repair horizontals and repair verticals
   have rate at most \(\mathcal I_2+C T^4<\mathcal I_n\).
   Its unweighted baseline verticals are retained until they meet
   the adjacent compact sides. They then form precisely the
   actual jumps estimated by the fold theorem, with the extra
   normalization difference (16). Their rate is strictly below
   \(\mathcal I_n\). There is no remaining separate baseline packet.
5. Fold baseline horizontals at the calibrated height have a strict
   gap by horizontal strict concavity and their separation from the
   selected real saddle coordinate. Every other designated baseline
   horizontal outside a fixed saddle neighborhood has the same
   strict gap. The opposite half on each positive compact block has
   a strict gap; its reflected copy has the identical estimate.
6. On the selected local segment, the nonleading grid aliases lose
   the fixed positive height \(H_m\). Their derivatives cost only
   powers of \(N\); they are already estimated in the exact local
   Gaussian theorem.

These are the original high trace, all real windows and interfaces,
every exterior side, every internal seam, both horizontal halves,
and all sampling aliases. The odd simple value and even last normal
are included in item 4 with their actual trace multiplicities.
Taking the minimum of the finitely many strict losses gives
\[
 L_{N,n}(-2;\boldsymbol\alpha)
           =\mathfrak L_{N,n}^{\rm loc}
                      +O(N^p e^{N(\mathcal I_n-\epsilon)})
 \tag{21}
\]
for some fixed \(\epsilon>0\), uniformly on the bounded parameter
set. Here \(\mathfrak L^{\rm loc}\) is (20); there is just one paired
favored local contribution.

For real parameters, (7), (9), and the local theorem give a polynomial
lower bound on \(|e^{-N\Phi(t_*)}\mathfrak L^{\rm loc}|\).
Hence (21) is exponentially smaller relative to it and proves
(8)--(10). This step uses the exact orientation (19), not an
assumption that two candidate geometric cycles cannot cancel.

For completeness the upper bound can have a polynomial prefactor,
not merely \(e^{o(N)}\). Near the selected point the local theorem
places \(-2\cos t\) strictly in \(\Re C<2\). The fold theorem's
half-plane kernel estimate therefore gives
\[
 |\partial_Z^q K_N^<(-2\cos t,-2)|
                       \le CN^p e^{N\Re\psi(t,0)}.
 \tag{22}
\]
The baseline and its one-sided corrections have polynomial norm
for bounded complex endpoint parameters. The actual horizontal
phase has a nondegenerate maximum \(\mathcal I_n\), so (22) bounds
this neighborhood by \(CN^p e^{N\mathcal I_n}\).
Away from it, choose the slit-domain exponential tolerances smaller
than the strict gaps already listed; they are absorbed by those
gaps. This proves (11) for \(\nu=0\). Cauchy on a larger bounded
complex parameter set proves the asserted fixed parameter
derivatives. Fixed output derivatives were retained in every listed
piece. None of this supplies a lower bound for an output normal.

## 5. Coverage and precise new scope

The existing
[uniform-terminal/star theorem](research_uniform_terminal_family_and_star_fillings.md)
already proves the bare
case \(r=0\) for all fixed signed \(|n|\ge2\), on a common small
boundary disk, and proves certain sufficiently high-valence stars
with arbitrary fixed terminal powers and central power. Its common
nonvanishing source chart has small angular boundary colors.

The microscopic inputs in (3) instead have spectral colors near
\(+2\), hence angular colors near \(\pi\). An arbitrary fixed number
of them on this one vertex is not a consequence of that chart or
its high-valence threshold. The new assertion is the whole original
scalar (3) with these inputs, for every fixed \(|n|\ge3\), with the
actual local coefficient and all remaining source pieces accounted
for. The coverage comparison is not used as a proof dependency.

The two-power fold budget reaches equality, and the local shortened
kernel theorem also excludes its boundary-half-plane saddle.
No result for \(n=\pm2\) with these insertions is asserted here.
Nor is (8) a source expansion on an output boundary disk or a theorem
for an arbitrary tree of received transformed factors.
Finally, \(\mathcal I_n\) is the calibrated bare terminal action.
Identifying the present microscopic boundary specialization with a
marked filled manifold requires separate geometry; (10) alone is
not a filled-volume statement.

## 6. Direct sources

All four complete direct source texts were read at the following
matching final pins, with the used trace, normalization, upper
budget and local coefficient implications checked:

* [Compact interfaces and actual seams](research_sharp_endpoint_compact_interface_and_seams.md),
  SHA256 178e49b99b51fe767bc29ceadafb00159c179cd42f9ba5469921f64a6eabdde9.
* [Uniform fold cap and actual join](research_endpoint_uniform_fold_cap.md),
  SHA256 5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
* [Actual shortened local Gaussian](research_shortened_endpoint_decorated_local_gaussian.md),
  SHA256 8e65d3885c88ea358e6c14fab59d9b1c825cc5e2d6a7a14f9a57e8c0810ab109.
* [Actual nonreal endpoint insertion](research_endpoint_nonreal_insertion_lower_bound.md),
  SHA256 ab3b4687b53c2168d22342c0e822b243a563f716d2a7a0de18d87c372546d7d0.

Only written mathematics and source text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Existing adopted and public notes are unchanged.
