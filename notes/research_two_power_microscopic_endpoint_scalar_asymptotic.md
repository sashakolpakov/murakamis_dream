# The whole two-power scalar with microscopic endpoint products

Private written proof, 16 November 2026.

The optimized physical fold estimate and the actual shortened-wire
coefficient close the original scalar trace for powers \(2\) and
\(-2\), with any fixed product of bounded real microscopic endpoint
kernels. The fold error is polynomially smaller than the nonzero
local coefficient. All other original currents have strict
exponential gaps after their actual boundary packets are joined.

The result is at the fixed output color \(-2\). It supplies neither
a fixed complex output neighborhood nor an output-normal estimate.
The first normals consumed by the original trace are retained
throughout.

## 1. Original source and statement

Put \(h=N^{-1}\), \(D=N-1\), and \(\eta=(-1)^D\). Use
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),\qquad
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),
\]
\[
 K_N(C,Z)=\sum_{k=0}^{D}e_k(C)e_k(Z),\qquad
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
 \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
             +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{1}
\]
The derivative in (1) is the original spectral first normal, applied
to the whole product. Fix \(r\ge0\), \(A<\infty\), real
\(\alpha_i\in[-A,A]\), and \(n=2\sigma\), \(\sigma=\pm1\). Set
\[
 B_N(C)=\prod_{i=1}^rK_N(2\cosh(\alpha_i/N),C),\qquad
 \mathcal L_{N,n}=\phi_N[R_N^n B_N K_N(\cdot,-2)].
 \tag{2}
\]
The empty product is one. Parameters may depend on \(N\) within
the stated compact. Products are formed before any canonical
reduction in the traced variable.

Write
\[
 C_N(x)=2\cos(2\pi x+\pi h),\qquad
 t=\pi-2\pi x-\pi h,\qquad
 \mathfrak c_{N,n}=\exp\!\left(\frac{\pi i nD^2}{4N}\right).
 \tag{3}
\]
The angular representative
\(\mathfrak c_{N,n}e^{inNt^2/(4\pi)}\) preserves the original
crossing values and first normals.

Let \(t_2=a-iH_2\), \(0<a<\pi\), \(H_2>0\), be the branch fixed by
\[
 \cos(t_2/2)=\frac{1+i}{2},\qquad
 \operatorname{asinh}(\tan(t_2/2))=it_2-i\pi .
 \tag{4}
\]
Set \(t_\sigma=a-i\sigma H_2\) and retain the original phase
\[
 \psi(t,0)=\int_0^{1/2}
       2\operatorname{asinh}(\cos(t/2)\cot(\pi v))\,dv,
 \qquad
 \Phi_\sigma(t)=\psi(t,0)+\frac{in}{4\pi}t^2-i\sigma t .
 \tag{5}
\]
Its branches and additive constant are those of the pinned
two-power wire theorem, with conjugation for negative power. In
particular
\[
 \Phi_\sigma'(t_\sigma)=0,\qquad
 \lambda_\sigma=-\Phi_\sigma''(t_\sigma)
                    =\frac{1-3i\sigma}{2\pi},\qquad
 \Re\Phi_\sigma(t_\sigma)=\mathcal I_2=\frac{2G}{\pi},
 \quad G=\int_0^{\pi/4}\log(\cot s)\,ds .
 \tag{6}
\]

The actual shortened wire coefficient \(a_e(t,u)\) is normalized
in the wire theorem by
\[
 K_N^<(-2\cos t,-2\cos u)
    =N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                            (1+O_{\rm hol}(N^{-1})),
 \quad
 K_N^<(C,Z)=\sum_{k<\lfloor N/2\rfloor}e_k(C)e_k(Z).
 \tag{7}
\]
It is nonzero on a fixed neighborhood of \((t_\sigma,0)\).
Define the fixed nonzero coefficient
\[
 \mathcal A_\sigma=
 \frac{\sigma i}{\pi}\sin t_\sigma\,a_e(t_\sigma,0)
                         \sqrt{\frac{2\pi}{\lambda_\sigma}},
 \tag{8}
\]
with the Gaussian square root having positive real part.

Choose the compatible sharp physical representatives on the saddle
patch, using a common actual bulk reference as in section 2, and put
\[
 \mathcal B_N(t)=
   \prod_{i=1}^rH_{i,N}^{\sigma}
       \!\left(\frac{\pi-\pi h-t}{2\pi},\alpha_i\right).
 \tag{9}
\]
Each \(H_{i,N}^{\sigma}\) preserves both physical jets on that patch.
On a fixed neighborhood of \(t_\sigma\), the actual insertion
estimate in the wire theorem gives
\[
 cN^{-r}\le|\mathcal B_N(t_\sigma)|,\qquad
 |\partial_t^k\mathcal B_N(t)|
       \le C_k\left(\frac{1+\log N}{N}\right)^r .
 \tag{10}
\]
For \(r=0\) these statements mean \(\mathcal B_N=1\).

**Theorem.** Uniformly for the stated real parameters and both level
parities,
\[
 \boxed{\quad
 \mathcal L_{N,2\sigma}
   =\mathfrak c_{N,2\sigma}
       e^{N\Phi_\sigma(t_\sigma)}
       \mathcal A_\sigma\mathcal B_N(t_\sigma)
                     [1+O(\varepsilon_{N,r})],
 \quad}
 \tag{11}
\]
where
\[
 \varepsilon_{N,r}=
   \frac{(1+\log N)^{2r}}{N^{1/4}}
       +\frac{(1+\log N)^{r+1}}{\sqrt N}
                     \longrightarrow0 .
 \tag{12}
\]
The first term can be omitted when \(r=0\). Thus the whole scalar
is nonzero for every sufficiently large level, uniformly on the
parameter compact, and
\[
 \lim_{N\to\infty}\frac1N\log|\mathcal L_{N,2\sigma}|
                         =\mathcal I_2 .
 \tag{13}
\]
More explicitly its modulus is between
\(cN^{-r}e^{N\mathcal I_2}\) and
\(C[(1+\log N)/N]^r e^{N\mathcal I_2}\) for large \(N\).
These are scalar assertions at complete output. No lower bound
for a derivative, or for complex microscopic parameters, is asserted.

## 2. Fixed compact pieces and the actual fold normalization

Choose a fixed sufficiently small \(T_0>0\) for the optimized fold
theorem. Its actual physical cap has mirrored midpoint boundaries
at \(t=\pm T_N\), \(T_N=T_0+O(h)\). The theorem uses the rowwise
cutoff
\[
 m_j=\lfloor N\delta(t_j)\rfloor,\qquad
 \delta(t)=\pi^{-1}\arcsin(\cos(t/2)/\sqrt2),\qquad
 x_j=jh,\quad t_j=t(x_j).
 \tag{14}
\]
The error actions used below are
\[
 I_\delta(x)=\int_0^\delta
   \log\frac{\sin^2(\pi x)-\sin^2(\pi v)}
                 {\sin^2(\pi v)}\,dv,\qquad
 J_*(t)=I_{\delta(t)}((\pi-t)/(2\pi)).
\]
Within each maximal constant-cutoff block its baseline uses the
common actual fold anchor
\[
 j_*=\begin{cases}N/2-1,&N\ {\rm even},\\
                         (N-1)/2,&N\ {\rm odd}.
          \end{cases}
 \tag{15}
\]
All these choices are the literal ones of the adopted fold theorem.
They include the odd simple value and the even last first normal.

Choose a second fixed cut \(T_+<\pi\), sufficiently close to \(\pi\).
On the remaining positive interval \([T_0,T_+]\), take the finite
compatible patch collection of the compact-current theorem. It
contains a fixed neighborhood of the saddle's real coordinate \(a\)
inside one patch. The real interfaces obey
\[
 \psi(t,0)-J_*(t)<\mathcal I_2\qquad(0<t<\pi).
 \tag{16}
\]
Hence this fixed compact interval has a positive uniform margin.
The patches and their repair losses can be chosen sufficiently
small to preserve it.

All compact patches use the same fixed physical bulk reference
\(x_b=j_bh<1/2\), to the right of their real buffers. For joining
the fold, choose it between the first seam and the fold. The
reference stays a fixed distance from \(1/2\), although that
distance may depend on \(T_0\). The compatible factorial and
coalesced recipes remain unchanged.

Here is the source-specific anchor comparison. For any adjacent
cutoff, extend its regular divided-color frame to the fold and set
\[
 \mathcal V_f(x)=
  \binom{f(x)}
  {[f(x)-f(x-h)]/[C_N(x)-C_N(x-h)]},\qquad
 \mathcal F=(\mathcal V_{H_0},\mathcal V_{H_1}),\qquad
 a(x)=\mathcal F(x)^{-1}
            \mathcal V_{K_N(w,C_N(\cdot))}(x).
 \tag{17}
\]
At coincident colors use its ordinary spectral divided difference.
The frame and its inverse are bounded through the fold. The full
kernel's ordinary residual and its first angular derivative vanish
at physical rows. The exact coefficient equation there is
\[
 a(x_{j+1})=(I+M_j)a(x_j),\qquad
 \|M_j\|\le CN^p e^{-NI_\delta(x_j)} .
 \tag{18}
\]
Actual states and coefficients have polynomial bounds. Monotonicity
of \(I_\delta\) towards the fold, summation of (18), and the harmless
last reflected row give
\[
 |a(x_{j_*})-a(x_b)|
                \le CN^p e^{-NI_\delta(x_b)} .
 \tag{19}
\]
This is the exact anchor argument proved in the whole-scalar source;
it uses no inequality \(\mathcal I_2<\mathcal I_n\). Multiplication
by the same bounded modes proves (19) for the two baselines on the
whole fixed tall overlap, with fixed spatial derivatives. Its
saving is at least the saving at the seam to the left.

The last optimized fold block's literal cutoff differs by \(O(1)\)
from \(\lfloor N\delta(T_0)\rfloor\). Retain that finite tail, as
well as (19), when comparing with the adjacent compact patch.
The actual finite-tail estimate in the fold and compact sources
bounds both by the same sharp seam exponential, up to a polynomial.
The compact representative's one-sided repair is a third retained
term with that saving. At the real seam endpoint its rate is
strictly below \(\mathcal I_2\), by (16), with a fixed margin of
order \(T_0^4\). At height \(H_2\), its saving is positive and the
bare horizontal phase is at most \(\mathcal I_2\). Vertical
convexity controls the full joining side. Every tolerance can be
chosen smaller than these fixed margins.

Thus the fold exterior sides can be joined while retaining the
actual bulk normalization on the saddle patch. In particular (10)
applies to the very representative used in the local coefficient.
No arbitrary homogeneous component or independent normal is set
to zero in this comparison.

## 3. Exhausting the trace at the critical scale

The exact outgoing split (7) is made before deforming any contour.
The entire remaining high sector, including the odd middle term,
has polynomial real norm and first normals. Its original restricted
trace with \(R_N^n B_N\) is polynomial, including the sum of the
absolute physical terms. This is the high-sector estimate of the
compact-current source. It is retained as an error source; the
full off-grid kernel is never assigned the shortened phase.

The optimized fold theorem applies directly to the actual cap:
\[
 \phi_{\rm cap}[R_N^nB_NK_N(\cdot,-2)]
    =\mathcal V_{\rm out,N}
      +O\!\left((1+\log N)^{2r}
               N^{-r-1/4}e^{N\mathcal I_2}\right).
 \tag{20}
\]
Equivalently subtract its polynomial cap-high trace to obtain the
same estimate for the low cap. In the global split the high trace
is restored exactly once.
Here \(\mathcal V_{\rm out,N}\) is precisely its four exterior
vertical half-sides at \(\pm T_N\), reaching angular heights
\(\pm H_2\), with the
adjacent block's baseline and the prefactor
\(-\eta/(4\pi^2i)\). It is not a newly supplied boundary datum.
The theorem has already summed the actual physical errors and
all growing internal block jumps. Their latter raw and anchor
contributions have bounds \(N^{-r-5/4}\) and \(N^{-r-1}\),
respectively, times \((1+\log N)^{2r}e^{N\mathcal I_2}\).
Its horizontals and retained high trace are exponentially smaller.
For \(r=0\), the replacement errors and all cutoff jumps vanish.

Pair each compact block with its angular reflection, using the
same half normalization. At the cap boundary its exterior
integrals and the corresponding terms of
\(\mathcal V_{\rm out,N}\) combine into the actual baseline
and repair differences described in section 2. Their strict
gap absorbs all four sides of (20); there is no separate
unestimated cap boundary packet.

For completeness the other original terms are as follows.

1. Every compact real interface has a strict \(\mathcal I_2\)
   gap by (16). Every internal compact vertical seam and every
   horizontal repair has a strict gap by the actual finite-tail
   comparison and the full rational sampling estimate.
2. At \(t=T_+\), the unweighted outer vertical is bounded by
   convexity between \(\psi(T_+,0)<\mathcal I_2\) and its strict
   top endpoint bound. The remaining original positive-spectral-end
   physical window has rate \(h_0(2\epsilon)\to0\) as its fixed
   width tends to zero; choose it below \(\mathcal I_2\). The
   full trace and its first normals are used in this window.
3. At height \(H_2\), the designated baseline horizontal phase is
   strictly concave with its unique maximum at \(a\). All its
   pieces outside a fixed saddle neighborhood have a strict gap.
   On the opposite half over the positive compact interval its
   rate is smaller by \(2tH_2/\pi>0\). Fold horizontals have their
   separate strict gap from the optimized fold theorem.
4. On the fixed local saddle segment, the exact rational sampling
   kernel retains every alias. All nonleading aliases lose the
   fixed height \(H_2>0\), as in the wire theorem.

These estimates use the coherent shortened-kernel slit bound
only on contours with a strict gap, with its exponential tolerance
smaller than that gap. Near the saddle, whose color has real
part \(2\), the actual local wire expansion (7) is used instead.
No half-plane bound valid only for \(\Re C<2\) is used there.

There are only finitely many compact and outer pieces. Taking the
minimum of their strict gaps, while retaining the polynomially
small fold error in (20), gives
\[
 \mathcal L_{N,n}=\mathfrak L_{N,n}^{\rm loc}
   +O\!\left((1+\log N)^{2r}N^{-r-1/4}
                            e^{N\mathcal I_2}\right)
   +O(N^p e^{N(\mathcal I_2-c)}).
 \tag{21}
\]
For \(r=0\) the first error in (21) is absent. This is an equality
of the complete original scalar with one paired favored local
piece and controlled errors, not a deduction from a local saddle
alone.

## 4. Signed mirror coefficient and relative comparison

Put \(D_h(x)=(\pi/h)^2\csc^2(\pi x/h)\). Under the holomorphic
reflection \(\mathcal R x=1-h-x\),
\[
 C_N(\mathcal R x)=C_N(x),\qquad
 D_h(\mathcal R x)=D_h(x),\qquad
 t(\mathcal R x)=-t(x),\qquad d(\mathcal R x)=-dx .
 \tag{22}
\]
The original crossing is unchanged. Choose reflected compact
representatives by
\(H_{\rm mirror}^{-\sigma}(\mathcal R x)=H^\sigma(x)\);
their full physical jets are the correct mirrored jets.
Write \(g(x)\) for their product times
\(\sin t\,\mathfrak c_{N,n}e^{inNt^2/(4\pi)}
K_N^<(C_N(x),-2)\).
The sine factor in this integrand changes sign, so
\[
 g_{\rm mirror}(\mathcal R x)=-g(x),\qquad
 \int_{\mathcal R\Gamma}D_hg_{\rm mirror}\,dx
                         =\int_\Gamma D_hg\,dx .
 \tag{23}
\]
An upper side directed right-to-left reflects to the inherited
lower side directed left-to-right. The two signs in (23) give
addition. The two half-prefactors recover the positive-lift
coefficient once, rather than twice.

Consequently the local term in (21) is exactly
\[
 \mathfrak L_{N,n}^{\rm loc}
  =\frac{\sigma iN^2}{\pi}\mathfrak c_{N,n}
    \int_{-b}^{b}
     \sin t\,K_N^<(-2\cos t,-2)\mathcal B_N(t)
     e^{inNt^2/(4\pi)}
       \frac{e^{-i\sigma Nt}}
            {(1-\eta e^{-i\sigma Nt})^2}\,ds,
 \qquad t=t_\sigma+s ,
 \tag{24}
\]
where \(b>0\) is a small fixed local half-width. The exact signed
orientation and rational denominator in (24) are those of the
wire theorem. Its local Gaussian gives
\[
 \mathfrak L_{N,n}^{\rm loc}
  =\mathfrak c_{N,n}e^{N\Phi_\sigma(t_\sigma)}
       \mathcal A_\sigma\mathcal B_N(t_\sigma)
       \left[1+
          O\!\left(\frac{(1+\log N)^{r+1}}{\sqrt N}\right)\right].
 \tag{25}
\]
The factors \(N^2\), \(N^{-3/2}\), and \(N^{-1/2}\) from trace,
shortened kernel, and Gaussian cancel exactly.

By (8), (10), and (6), the leading expression in (25) has
modulus at least \(cN^{-r}e^{N\mathcal I_2}\), uniformly on the
real parameter compact. Divide (21) by this quantity. Its fold
error has relative bound
\(C(1+\log N)^{2r}N^{-1/4}\); its remaining error is exponentially
small relative to it. Equation (25) proves (11)--(12).
The upper bound in (10) and the same comparison give the stated
two-sided polynomial amplitude bounds and the uniform limit (13).

## 5. Scope and complete sources

The undecorated case \(r=0\) already belongs to the terminal
theorems. The earlier microscopic-product scalar theorem handles
all fixed \(|n|\ge3\). The new assertion here completes the two
remaining signs \(n=\pm2\) at fixed complete output, using the
optimized physical fold error and its complete exterior join.
It is not an extension obtained from a bare contraction through
the endpoint product.

The error in (20) is only polynomially smaller than the main
term. Polynomial continuation from \(Z=-2\), or bounds for a
finite collection of output derivatives, do not extend (11)
to a fixed output disk. No such conclusion is made. Nor is
there a claim for complex microscopic lower bounds, arbitrary
received exponential factors, or a marked filled-volume
identification.

All four complete direct source texts were read at these matching
pins, with the used original trace and normalization implications
checked:

* [Optimized physical fold blocks and all their exterior sides](research_critical_fold_optimized_block_assembly.md),
  SHA256 d55f935b72ade9b11c2565790da7040d3c7fa1f0fd6d90c1b83ad8be80802b76.
* [Actual shortened two-power wire and local trace](research_two_power_shortened_wire_packet.md),
  SHA256 f3ae7c6cad975224f8e93f0de8466707fea22c0ae9d712c437d49053ca7cbd87.
* [Compact interfaces, seams, high source, and positive endpoint](research_sharp_endpoint_compact_interface_and_seams.md),
  SHA256 178e49b99b51fe767bc29ceadafb00159c179cd42f9ba5469921f64a6eabdde9.
* [Actual bulk/fold anchor conversion and mirror bookkeeping](research_microscopic_endpoint_filled_leaf_scalar_asymptotic.md),
  SHA256 33ef2e3ee2090fa69c58df03bc141f6249dcaa35b0ae62598213a88ce65979d0.

The complete three direct sources of the optimized fold theorem
were also read at its unchanged pins: the actual cap error
08a6a612, uniform fold source 5cdb5933, and compact source 178e49.
The two former full pins are respectively
08a6a612536931629567733d63b2161eca52000f3bea0973c79528c023677bb8 and
5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted and public notes are unchanged.
