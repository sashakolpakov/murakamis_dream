# Sharp compact endpoint interfaces and their joined vertical seams

Private written proof, 16 November 2026.

The sharp endpoint representatives give an actual strict real-interface
gap on every compact interior angular interval. Their explicitly
truncated modes also control the difference between adjacent spatial
patches. After retaining the high Newton part of the outgoing kernel
as a separately bounded original trace, vertical convexity and the
calibrated horizontal saddle bound pay every internal patch seam for
every fixed signed power of magnitude at least two.

This is a compact-current statement. The outer boundary adjoining the
negative spectral endpoint is retained. No complete filled-leaf
asymptotic or nonzero saddle coefficient is asserted.

## 1. Original source and the compact statement

Put \(h=N^{-1}\), \(D=N-1\), \(\eta=(-1)^D\), and retain
\[
 c_j=2\cos((2j+1)\pi/N),\quad C_N(x)=2\cos(2\pi x+\pi h),
 \quad \tau_N(x)=\pi-2\pi x-\pi h,
\]
\[
 P_N(C)=2T_N(C/2)+2,\quad
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),\quad
 S_k=\prod_{j=1}^k2\sin(\pi j/N),\quad
 K_N(C,Z)=\sum_{k=0}^{D}e_k(C)e_k(Z).
 \tag{1}
\]
The endpoint insertion is the ordinary shared product
\[
 B_N(C)=\prod_{i=1}^rK_N(2\cosh(\alpha_i/N),C),
 \qquad |\alpha_i|\le A,
 \tag{2}
\]
where \(r,A\) are fixed. Its canonical reduction, when used, is
performed only in the originally traced variable and preserves all
physical jets. The original outgoing source is
\[
 L_{N,n}(Z)=\phi_N^{(C)}[R_N(C)^n B_N(C)K_N(C,Z)],
 \qquad n\in\mathbb Z\text{ fixed}.
 \tag{3}
\]
The full trace is
\[
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
       \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
             +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{4}
\]
Here \(R_N\) is the original Gaussian full-jet coupon. With
\(q=e^{\pi i/N}\), its physical values are
\(R_N(c_j)=q^{D^2/2}(-1)^j q^{j(j+1)}\); its first normals
are those of the angular representative \(E_{N,1}\) in (22),
differentiated before physical evaluation.
All assertions about output derivatives below concern every fixed
ordinary \(\partial_Z^q\) at the complete output \(Z=-2\).
Fixed endpoint-parameter derivatives are included as well.

Write \(\psi(t)=\psi(t,0)\) for the calibrated complete-edge phase
and \(G=\int_0^{\pi/4}\log\cot s\,ds\), so that
\[
 M_\infty=\psi(0)=4G/\pi,\qquad
 J_*(t)=\frac1\pi\int_t^\pi\operatorname{asinh}(\sin(s/2))\,ds,
 \qquad \mathcal I_2=2G/\pi.
 \tag{5}
\]
Fix a compact interval \(K=[t_-,t_+]\Subset(0,\pi)\), and define
\[
 d_K=\mathcal I_2-\max_{t\in K}\{\psi(t)-J_*(t)\}>0.
 \tag{6}
\]
The positivity is proved below, including its normalization.

**Theorem.** A finite collection of sharp spatial patches can be
chosen over \(K\), with a common physical normalization anchor and
compatible local parameter charts, so that:

1. The sum of their actual weighted real interfaces, with the
   complete outgoing kernel and every fixed output normal retained,
   is bounded by \(CN^p\exp\{N(\mathcal I_2-d_K/2)\}\).
2. On every common designated half-rectangle, adjacent representatives
   differ by \(CN^p e^{-N\gamma_s}\), where \(\gamma_s>0\) is their
   common sharp local saving. The difference is an estimate for the
   actual normalized representatives, not only for their residuals.
3. For \(|n|\ge2\), put \(H_n=|\Im t_{|n|}(0)|\), the calibrated
   saddle height. After the exact low/high outgoing split in section
   2, all internal vertical seams reaching height \(H_n\), and all
   horizontal repair corrections there, have a strict rate gap below
   \(\mathcal I_n\). The bound holds on both half-contours and retains
   their exact rational sampling kernels.

The remaining baseline horizontal integrals have rate at most
\(\mathcal I_n\), with a strict gap outside any fixed neighborhood
of the selected saddle on the designated half. The opposite half
has a strict gap on \(K\). The two outer vertical boundaries and
all physical rows outside \(K\) are still present.

Constants are uniform on bounded complex endpoint-parameter sets,
using the finite local atlas. Representatives on different parameter
charts need not agree away from the physical nodes.

## 2. Retaining the outgoing high sector at its original trace

Let \(m=\lfloor N/2\rfloor\), and split exactly
\[
 K_N=K_N^<+K_N^{\rm hi},\qquad
 K_N^<(C,Z)=\sum_{k=0}^{m-1}e_k(C)e_k(Z).
 \tag{7}
\]
Every high polynomial has polynomial real norm. At even levels these
are the radical polynomials with norm at most \(\sqrt{N-1}\).
At odd levels the additional middle polynomial has norm at most one;
all subsequent polynomials satisfy the radical bound. Markov's
inequality consequently gives, for all fixed \(a,q\ge0\),
\[
 \sup_{C\in[-2,2]}
 |\partial_C^a\partial_Z^qK_N^{\rm hi}(C,-2)|\le CN^p.
 \tag{8}
\]
This uses the ordinary polynomial derivatives, including the output
normal at the angular branch point \(Z=-2\).

The full endpoint-product theorem gives polynomial real norm for
(2), and Markov gives its first traced normal. The original crossing
values have modulus one. At a double physical node its angular
derivative has size \(O_n(N)\); division by \(2\sin\tau_j\), whose
nonzero physical values are bounded below by a constant times
\(N^{-1}\), gives a polynomial spectral-normal bound. At the odd
simple node only the original value is used. Formula (4), with its
ordinary product rule, therefore proves
\[
 \left|\partial_Z^q\phi_N[R_N^n B_N K_N^{\rm hi}(\cdot,Z)]_{Z=-2}
                                                        \right|\le CN^p.
 \tag{9}
\]
The same estimate holds for the sum of the absolute terms and for
any restricted subset of physical rows. All fixed parameter
derivatives follow on a larger bounded parameter set. Thus (9)
retains, rather than cancels or discards, the entire high-sector
source. Its full-normal character is essential here.

For the exact low kernel, the pinned slit-domain theorem gives the
following consequence. On every compact angular set with
\(0<\Re t<\pi\) and bounded imaginary part, for every \(\epsilon>0\),
\[
 |\partial_C^a\partial_Z^qK_N^<(C,-2)|_{C=-2\cos t}
        \le C_\epsilon N^p e^{N(\Re\psi(t)+\epsilon)}.
 \tag{10}
\]
Indeed its spectral compact set lies in
\(\mathbb C\setminus[2,\infty)\). The theorem bounds the low
kernel on a fixed complex neighborhood of every real output color,
with arbitrary positive exponential tolerance. Its normalized
Cauchy estimates give (10). The branch and its additive constant
are those in (5). No termwise Newton absolute estimate replaces this
coherent low-kernel bound.

On a compact real \(t\)-interval, \(\psi(t)>0\). Combining (8)
and (10) gives the same bound for the full outgoing kernel there
and for its fixed ordinary derivatives. On a tall contour we use
(10) only after the exact trace separation (9); we do not replace
the full off-grid high sector by the low phase.

## 3. Compatible optimized patches

For a real \(x\in(0,1/2)\), write \(t=\pi-2\pi x\) and
\[
 I_\delta(x)=\int_0^\delta
    \log\frac{\sin^2(\pi x)-\sin^2(\pi v)}{\sin^2(\pi v)}\,dv,
 \qquad
 \delta(x)=\pi^{-1}\arcsin(\sin(\pi x)/\sqrt2).
 \tag{11}
\]
The sharp source proves \(I_{\delta(x)}(x)=J_*(t)\).
For \(0<\delta<x<1/2\), \(I_\delta(x)\) increases with \(x\).
For fixed \(x\), its integrand decreases with \(\delta\), changes
sign once, and hence \(\delta\mapsto I_\delta(x)\) first increases
and then decreases. In particular,
\[
 I_v(x)\ge\min\{I_{\delta_1}(x),I_{\delta_2}(x)\}
       \quad(\delta_1\le v\le\delta_2<x).
 \tag{12}
\]

Choose finitely many small patches around the \(x\)-image of \(K\),
each with cutoff \(M_i=\lfloor\delta_iN\rfloor\), where
\(\delta_i=\delta(x_i)\). Enlarge their overlaps slightly so both
cutoffs lie strictly below the real coordinates on each overlap.
Reserve larger parameter charts and larger spatial rectangles for
derivatives. Every patch's real domain can also be extended to a
common fixed right anchor \(x_{j_*}\), lying to the right of all
patch buffers and strictly below \(1/2\), and to its backward
neighbor: the cutoffs remain below that real
interval, and its lower action bound cannot decrease to the right.

Use the same factorial normalization and the same local parameter
chart recipe on every spatial patch. The raw modes are
\[
 F_z(x)=4^{-z}\frac{G_N(Nx+z)}{G_N(Nx-z)},\qquad
 U_{M_i}(z,x)=\sum_{k=0}^{M_i}a_k(z)F_{z-k}(x).
 \tag{13}
\]
The coefficients \(a_k(z)\) do not depend on the cutoff. On a
common fixed-height rectangle their exact summands obey
\[
 |\partial_x^a\partial_z^b(a_kF_{z-k})(x)|
           \le CN^p e^{-NI_{k/N}(\Re x)}.
 \tag{14}
\]
For parameters away from resonances, subtraction of (13), followed
by (12), proves
\[
 \|H_i-H_j\|+\|\mathcal F_i-\mathcal F_j\|
 \le CN^p e^{-N\min(I_{\delta_i}(\Re x),I_{\delta_j}(\Re x))}.
 \tag{15}
\]
Here \(H_i\) denotes the row of two scalar modes and
\(\mathcal F_i\) their divided-color frame. The latter quotient
costs only a polynomial on this compact interior domain. Spatial
derivatives may also be obtained on disks of radius \(c/N\).

The same assertion holds on every chart of the finite parameter
atlas. At zero the coalesced difference quotient is controlled by
Cauchy's formula on a fixed parameter circle. At an odd resonance
the mode extends holomorphically. At an even resonance \(L\), the
chart uses
\[
 U_{M_i}(z)-\frac{R_{N,L}}{z-z_0}U_{M_i-L}(-z-1),
 \qquad U_{M_i-L}(-z-1).
 \tag{16}
\]
The residue \(R_{N,L}\) is independent of \(M_i\). Differences
of (16) are therefore again finite tails, now with fixed cutoff
shifts \(L\). Such shifts change (15) only by a polynomial or a
bounded factor. Prove the estimate on the reserved parameter circle
and extend the holomorphic difference inside by the maximum
principle. This also proves its fixed parameter derivatives.

Let \(v_*\) be the actual divided-color state of the full endpoint
kernel at the common physical anchor. Its norm is polynomial.
Normalize each patch by
\[
 A_i=\mathcal F_i(x_{j_*})^{-1}v_*,\qquad V_i(x)=H_i(x)A_i.
 \tag{17}
\]
All frames and inverses are uniformly bounded. The inverse identity
and (15) give the same small bound for \(A_i-A_j\), evaluated at
the anchor. Monotonicity in \(x\) makes its exponent at least the
one required at every overlap point to its left. Thus
\[
 |\partial_x^a\partial_{\boldsymbol\alpha}^b(V_i-V_j)(x)|
 \le CN^p e^{-N\min(I_{\delta_i}(\Re x),I_{\delta_j}(\Re x))}.
 \tag{18}
\]
This is an actual coefficient comparison using the same two source
values. No arbitrary homogeneous packet has been set to zero.

Apply the exact one-sided Hermite repairs in each patch. If
\(\gamma_i\le\inf I_{\delta_i}\) on its reserved real buffer,
their corrections satisfy \(CN^p e^{-N\gamma_i}\) on the designated
half-rectangle. Hence adjacent repaired representatives satisfy
\[
 |H_i^\sigma-H_j^\sigma|\le CN^p e^{-N\gamma_s},
 \qquad \gamma_s=\min(\gamma_i,\gamma_j)>0,
 \qquad \sigma\Im x\ge0.
 \tag{19}
\]
The same statements hold for fixed shared products, by telescoping,
with the minimum saving and the ordinary full normal product rule.
There is no multiplication of the saving by the number of factors.

## 4. The actual real-interface gap

The edge calibration gives
\[
 \psi'(t)=-\pi^{-1}\operatorname{asinh}(\tan(t/2)),\qquad
 J_*'(t)=-\pi^{-1}\operatorname{asinh}(\sin(t/2)).
 \tag{20}
\]
Their difference is strictly negative for \(0<t<\pi\).
Moreover \(J_*(0)=2G/\pi\): differentiating
\(\int_0^{\pi/2}\operatorname{asinh}(k\sin v)\,dv\) with respect
to \(k\) gives \(\arctan(k)/k\), whose integral from zero to one
is \(G\). Thus \(\psi(0)-J_*(0)=\mathcal I_2\), proving (6).

Choose the patches and their losses small enough that, on each
patch, \(\psi(t)-\gamma_i\le\mathcal I_2-3d_K/4\).
The \(O(h)\) difference between \(t\) and \(\tau_N(x)\) costs only
a bounded exponential factor on \(K\). The exact sampling kernel is
\[
 D_h(x)=(\pi/h)^2\csc^2(\pi x/h),
\]
and the exact weighted product-interface estimate is
\[
 |D_h(P_i^+-P_i^-)(x)|\le CN^p e^{-N\gamma_i}
                         \quad(x\text{ real}).
 \tag{21}
\]
Multiply by the actual sine, crossing and outgoing kernel. The
crossing has modulus one on the real segment. Apply (10), (8), and
an output Cauchy tolerance smaller than \(d_K/4\). The real integral
has bounded length, and there are only finitely many patches.
This proves assertion 1, with every fixed output normal. The
traced normal was preserved exactly before taking this bound.

## 5. Exact seam placement and a general phase comparison

Partition the physical rows over \(K\) into consecutive blocks,
with midpoint cuts lying in the patch overlaps. For each block use
its exact two-half-contour identity, with
\[
 E_{N,n}(x)=e^{\pi i n(N-1)^2/(4N)}
             e^{inN\tau_N(x)^2/(4\pi)},\qquad
 g_i^\sigma=\sin(2\pi x+\pi h)P_i^\sigma E_{N,n}
                                      K_N^<(C_N(x),Z).
 \tag{22}
\]
The normalization is \(-\eta/(2\pi^2i)\) times the sum of the
lower exterior integral, upper exterior integral, and positively
oriented real interface, each with \(D_h\). This is the original
full-Hermite identity. At a shared midpoint, exterior sides combine
to their difference \(g_i^\sigma-g_{i+1}^\sigma\), with the
inherited orientations. They are retained as jumps, not cancelled
by an assertion that the two representatives coincide.

At a midpoint \(x=a_N+i\sigma H/(2\pi)\),
\[
 |D_h(x)|=(\pi N)^2\operatorname{sech}^2(NH/2)
                                      \le4\pi^2N^2e^{-NH}.
 \tag{23}
\]
Thus (10), (19), and the exact crossing in (22) give the seam rate
\[
 \mathcal P_{n,\sigma}(t,H)-\gamma_s+\epsilon,\qquad
 \mathcal P_{n,\sigma}(t,H)
 =\Re\psi(t-i\sigma H)
                      +\left(\frac{\sigma nt}{2\pi}-1\right)H.
 \tag{24}
\]
All signs refer to the original \(n\); positive \(\sigma\) is the
upper \(x\)-half and lower angular half. Formula (23) is exact for
the full rational grid kernel and therefore retains all aliases.

On \(0<\Re t<\pi\), the calibrated branch obeys
\[
 \psi''(t)=-\frac1{2\pi\cos(t/2)},\qquad
                         \Re\sec(t/2)>0.
 \tag{25}
\]
Consequently \(H\mapsto\mathcal P_{n,\sigma}(t,H)\) is convex.
It is enough to bound the two endpoints of any vertical seam.
This is the precise general seam criterion; no intermediate-height
maximum is left unchecked.

For \(|n|\ge2\), put \(m=|n|\), \(\sigma_0=\operatorname{sign}n\),
and \(H_n=-\Im t_m(0)>0\). Calibration and horizontal strict
concavity give
\[
 \mathcal P_{n,\sigma_0}(t,H_n)\le\mathcal I_n,
 \tag{26}
\]
with equality only at \(t=\Re t_m(0)\). Indeed its second derivative
in real \(t\) is \(-\Re\sec((t-iH_n)/2)/(2\pi)<0\), and its first
derivative vanishes at the calibrated saddle. The opposite half has
\[
 \mathcal P_{n,-\sigma_0}(t,H_n)
 =\mathcal P_{n,\sigma_0}(t,H_n)-\frac{m tH_n}{\pi}
                                                   <\mathcal I_n.
 \tag{27}
\]
At the real seam endpoint, section 4 gives
\(\psi(t)-\gamma_s<\mathcal I_2\le\mathcal I_n\), provided the
patch losses were chosen with the common compact margin. At the
top endpoint, (26)--(27) and \(\gamma_s>0\) give a strict gap.
Convexity, a smaller Cauchy tolerance, and the finite number of
seams prove assertion 3. The same argument bounds each horizontal
repair correction. The baseline horizontal bounds and their
strictness away from the saddle follow directly from (26)--(27).

This reuses the general concavity/convexity mechanism of the bare
terminal contour. It does not import an exact bare q-binomial
contraction through the additional insertion. Equations (7)--(9)
are the source-preserving reason the low-phase upper bound is
eligible here; applying (26) directly to the full off-grid kernel
would in general be unjustified.

## 6. What remains for the whole leaf

At a right angular cutoff \(T<\pi\) sufficiently close to \(\pi\),
\(\psi(T)<\mathcal I_n\), and the horizontal endpoint in (26) is
strictly below \(\mathcal I_n\). Its outer vertical side, now
without a small jump factor, is paid by the same convexity proof.
The actual remaining positive-spectral-end physical window has
the pinned full-normal bound
\[
 CN^p\exp\{Nh_0(2\varepsilon)\},\qquad
 h_0(2\varepsilon)\longrightarrow0,
 \tag{28}
\]
including fixed complete-output derivatives and bounded complex
endpoint parameters. Thus this end can be placed below every fixed
positive terminal action. The high trace (9) is retained throughout.

At a left cutoff tending to \(t=0\), the unweighted baseline
vertical side is not covered by the compact seam theorem: its real
endpoint has rate \(\psi(t)\), not \(\psi(t)-J_*(t)\).
It must be joined to the actual fold-cap representation and its
endpoint packets. Even the real-interface margin degenerates as
\[
 \psi(t)-J_*(t)=\mathcal I_2-\frac{t^4}{64\pi}+O(t^6).
 \tag{29}
\]
The present proof has fixed compact buffers and supplies no uniform
shrinking-fold constants or strict two-power cap estimate. The odd
simple value and even last spectral normal cannot be removed when
that joining is carried out.

Accordingly the remaining obligations are the fold cap and its
actual join to the compact patches, together with the local
nonzero saddle coefficient if a lower asymptotic is desired.
Every compact real interface, compact internal seam, designated
horizontal repair, and positive-end contribution specified above
has been estimated. For \(n=0,\pm1\) only the source identities,
polynomial high trace and compact rate bound in assertion 1 are
claimed; \(\mathcal I_1=0\) gives no corresponding terminal gap.

## 7. Coverage and direct sources

The sharp local atlas, outgoing slit bound, original endpoint-product
norms, and calibrated terminal saddle are prior results. The new
steps are the source-normalized finite-tail overlap (15)--(19), its
compact full-interface consequence, the explicit polynomial high
trace with all output normals, and the resulting all-power internal
seam estimate. No global scalar gluing or whole-source lower bound
is inferred.

All complete direct sources were read at the following unchanged
pins, and their used implications were checked:

* [Sharp local parameter atlas](research_endpoint_sharp_local_parameter_atlas.md),
  SHA256 37cbfdab768bad41aa643859a75f9dfeaa5f1db57888ef14f6d5beeb5b29e019.
* [Incoming-color kernel upper bounds](research_mixed_next_incoming_color_kernel_upper_bounds.md),
  SHA256 9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db.
* [Terminal action calibration](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd.
* [Full endpoint products](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.
* [Original baseline and endpoint window](research_unturned_endpoint_complex_baseline_and_window.md),
  SHA256 9d233d9bb11c2842e62d5523f97e9621a3bd22532e3b527ceaab8125782c1cc1.

Only written mathematics and source text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Adopted notes and public manuscripts are unchanged.
