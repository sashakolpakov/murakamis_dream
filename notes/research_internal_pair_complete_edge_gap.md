# A complete-edge gap at every positive internal pair

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The coupled complete-end pair equations improve the height bound to
\(H<107/100\). On the resulting angular box the complete-edge action
exceeds the entire radical's growth by a fixed positive amount.
Consequently the nonzero logarithmic asymptotic for the low complete-end
kernel also holds for the full kernel, through both level parities,
on a fixed complex neighborhood containing every selected angle of
these pairs. The other outside endpoint remains complete.

## 1. The height bound uses the actual two incidences

Fix integer powers \(n,p\ge3\), charges in \([0,1]^2\), and the
positive geometric solution with one complete outside endpoint
attached to each selected vertex. By the
[pair angle theorem](research_internal_pair_angle_bound.md), every
active selected angle \(t=a-iH\) satisfies
\[
                    0<a<\pi/2,\qquad H>0.
 \tag{1}
\]
The [cosine maximum principle](research_positive_path_real_wire_order.md)
also gives \(|\cos(u/2)|<1\) at an active neighbor; a complete or
zero-charge neighbor has cosine one.

The two original principal returns at \(t\) are
\[
 r_0=\operatorname{asinh}(\tan(t/2)),\qquad
 r_1=\operatorname{asinh}(\tan(t/2)\cos(u/2)).
 \tag{2}
\]
Their positive real parts obey
\(\Re r_0+\Re r_1=nH/2\).
Since
\[
 |\tan(t/2)|^2
       =\frac{\cosh H-\cos a}{\cosh H+\cos a}<1,
 \tag{3}
\]
and \(|\sinh(k+ig)|^2=\sinh^2 k+\sin^2g\), one has
\(\Re r_1<\operatorname{asinh}1\).
At fixed \(H\), the real part of \(r_0\) increases with \(a\):
its derivative is \(\frac12\Re\sec(t/2)>0\), on the branch
continued from completeness. At \(a=\pi/2\) its value is exactly
\(\operatorname{asinh}\sqrt{\operatorname{sech}H}\). Therefore
\[
 \frac{3H}{2}\le\frac{nH}{2}
   <\operatorname{asinh}\sqrt{\operatorname{sech}H}
          +\operatorname{asinh}1 .
 \tag{4}
\]

**Proposition 1.** Every active height in this family satisfies
\[
                              H<107/100.
 \tag{5}
\]
Indeed the right side of (4) decreases with \(H\). At \(h_0=107/100\),
\[
 \begin{split}
 \cosh(h_0)\sinh^2(18/25)&>1,\\
 \sinh(441/500)&>1,\qquad
 18/25+441/500=801/500<321/200=3h_0/2.
 \end{split}
 \tag{6}
\]
All three comparisons are exact. For the first two it suffices
to retain the terms through degree six of the positive cosh
series and through degree seven of the positive sinh series.
Thus the right side of (4) is less than \(801/500\) if
\(H\ge h_0\), a contradiction. Inactive angles are zero.

## 2. A uniform gap on the whole pair box

Let
\[
 \mathcal R=\{a-iH:0\le a\le\pi/2,\ 0\le H\le107/100\}.
 \tag{7}
\]
Keep the original complete-end phase, with its complete constant:
\[
 \psi(t,0)=-4J(1/4+t/(4\pi))-4J(1/4-t/(4\pi)),
 \quad J'(z)=\Log(2\sin\pi z),\quad J(0)=0.
 \tag{8}
\]
All factorial arguments in (8) stay in their regular strips
on a neighborhood of this rectangle.

**Theorem 2.** Uniformly on \(\mathcal R\),
\[
                    \Re\psi(a-iH,0)-H>1/500.
 \tag{9}
\]

*Proof.* Write \(r_0=k_0+ig_0\) for the first return in (2).
The original branch gives
\(\psi_t(t,0)=-r_0/\pi\), with \(k_0\ge0\) and
\(-\pi/2<g_0\le0\). Hence
\[
 \partial_a\Re\psi=-k_0/\pi\le0,\qquad
 \partial_H(\Re\psi-H)=-g_0/\pi-1<-1/2.
 \tag{10}
\]
It suffices to check \(a=\pi/2,H=h_0\). At this real part the
exact return formula is
\[
              g_0=-\arctan(\sqrt2\sinh(H/2)).
 \tag{11}
\]
Consequently
\[
 \begin{split}
 \Re\psi(\pi/2-iH,0)-H
 &=\psi(\pi/2,0)-H
       +\frac1\pi\int_0^H\arctan(\sqrt2\sinh(s/2))\,ds\\
 &\ge\psi(\pi/2,0)-H
           +\frac{H^2/2-H^4/24}{\sqrt2\,\pi}.
 \end{split}
 \tag{12}
\]
For the last inequality use \(\sqrt2\sinh(s/2)\ge s/\sqrt2\)
and \(\arctan x\ge x-x^3/3\) for \(x\ge0\). The latter follows
by differentiation, since the derivative of its difference is
\(x^4/(1+x^2)\).

Here is a short rational lower bound for the remaining constant.
The integrated Fourier series of \(\log(2\sin\pi z)\) gives
\[
 \psi(\pi/2,0)=\frac{2\sqrt2}{\pi}
 \sum_{j=0}^{\infty}
 \left\{\frac1{(8j+1)^2}+\frac1{(8j+3)^2}
             -\frac1{(8j+5)^2}-\frac1{(8j+7)^2}\right\}.
 \tag{13}
\]
For example, integrate the Abel-regularized cosine series and
then use the absolute convergence of the resulting sine series.
Each block displayed in (13) is positive. The first three blocks,
with \(\sqrt2>707/500\) and \(\pi<22/7\), give
\[
                         \psi(\pi/2,0)>239/250.
 \tag{14}
\]
For the integral correction use \(\sqrt2<99/70\) and
\(\pi<22/7\). At \(H=h_0\), the excess of the resulting
lower bound over \(1/500\) is exactly
\[
 \frac{239}{250}-\frac{107}{100}
 +\frac{h_0^2/2-h_0^4/24}{(99/70)(22/7)}-\frac1{500}
                =\frac{261699551}{522720000000}>0 .
 \tag{15}
\]
This proves (9). \(\square\)

## 3. The full complete-end kernel at both parities

Let \(\mathcal K_N(t)\) be the original low complete-end factor,
with indices \(0\le j\le N-1-\lfloor N/2\rfloor\). The
[odd last-row theorem](research_last_physical_row_riccati.md)
and [even low-index comparison](research_even_complete_low_kernel.md)
give on a fixed complex neighborhood of \(\mathcal R\)
\[
 \mathcal K_N(t)=\exp\{N\psi(t,0)+e_N(t)\},\qquad
             |\partial_t^\ell e_N(t)|\le C_\ell\log N
 \tag{16}
\]
for every fixed \(\ell\), after shrinking that neighborhood
for derivative estimates. This use is legitimate because
\(\Re(-2\cos t)\le0\) on \(\mathcal R\).

Write \(D_N(t)=K_N(t,0)-\mathcal K_N(t)\). The
[original radical Fourier bound](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials)
gives, at both parities,
\[
                          |D_N(t)|\le N^2e^{(N-1)|\Im t|}.
 \tag{17}
\]
At odd levels it is identically zero. This bound needs no
restriction such as \(|\Im(-2\cos t)|>1\).

**Corollary 3.** There is a fixed complex neighborhood
\(\mathcal V\) of \(\mathcal R\) on which, through all sufficiently
large integer levels,
\[
 \begin{split}
 K_N(t,0)&=\exp\{N\psi(t,0)+\widehat e_N(t)\}\ne0,\\
 |\partial_t^\ell\widehat e_N(t)|&\le C_\ell\log N,\\
 K_N(t,0)/\mathcal K_N(t)&=1+O(e^{-cN})
 \end{split}
 \tag{18}
\]
for some \(c>0\), with the same exponential relative error for
every fixed derivative on smaller neighborhoods.

*Proof.* By compactness, (9) persists with a smaller positive
gap for \(\Re\psi(t,0)-|\Im t|\) on a complex neighborhood of
\(\mathcal R\). Equations (16)--(17) then bound
\(|D_N/\mathcal K_N|\) by a polynomial times a strictly
decaying exponential, uniformly there. For all large levels
this ratio has modulus less than \(1/2\). Define
\(\widehat e_N=e_N+\Log(1+D_N/\mathcal K_N)\) using the
logarithm near zero. Cauchy's formula on smaller neighborhoods
proves all derivative statements. \(\square\)

The normal derivatives here are in the selected ordinary
spectral variable \(w=-2\cos t\), on neighborhoods of its
nonzero geometric selected angles. Since \(\sin t\ne0\) there,
fixed \(w\)-derivatives follow from (18). The other boundary
argument of the kernel remains exactly complete. This theorem
does not analytically continue the estimates to a fixed
nonzero neighborhood in that outside argument.

In particular the
[local internal-pair Gaussian theorem](research_internal_pair_local_gaussian.md)
may use the full original complete-end kernels at both parities.
The global low-wire and trace cycle still needs its own bounds.
There is no contradiction with the even-level bare-kernel
counterexamples at homogeneous longer-path angles with
\(\Re t>\pi/2\), outside \(\mathcal R\).

## 4. Exact scalar check

The [independent rational check](../experiments/check_internal_pair_complete_edge_gap.py)
uses only positive Taylor partial sums and exact fractions.
It checks the height comparisons, the three positive Fourier
blocks, and the strict margin (15). Its
[saved record](../repro/results/research-internal-pair-complete-edge-gap.json)
retains script and proof hashes.

~~~sh
python3 experiments/check_internal_pair_complete_edge_gap.py
~~~
