# A flat cap has no uniform local exponential angular mismatch bound

The flat-cap example is a local limitation on phase suppression. It is not a lower bound for the full source or a filling period.

At the residual cap \(x=b=0\), \(\sigma=2\), the literal raw coefficient is

\[
 [c^{d-j}y^j]H_V=(-1)^j A_j,\qquad
 A_j=\csc^2\frac{\theta}{2}\prod_{r=1}^j
        \frac{\sin^2(r\theta)}{\sin^2((r+\tfrac12)\theta)},
 \qquad \theta=\frac{\pi}{N},\quad d=N-1.
 \tag{1}
\]

This follows directly from the
[full-interval source identity](research_original_one_sided_four_state_transfer.md).
At \(x=b=0\), the only start is \(i=0\) and
\[
 K_{0,j}=y^j\prod_{r=1}^j4\sin^2(r\theta),\qquad
 \alpha_r=-4\sin^2((r+\tfrac12)\theta).
\]
The exact product
\[
 \prod_{r=0}^{d}4\sin^2((r+\tfrac12)\theta)=4
\]
then gives (1), including the sign from the original unused factors
and the common raw sign. No factor is removed.

For \(0\le j\le M=\lfloor N/2\rfloor-1\), the sequence \(A_j\) is positive
and decreasing, because
\(\sin(j\theta)\le\sin((j+\tfrac12)\theta)\) on this range. Also

\[
 A_j\le A_0=\csc^2(\theta/2)\le N^2.
 \tag{2}
\]

The monotonicity of sine gives the telescoping lower bound

\[
 \prod_{r=1}^j\frac{\sin(r\theta)}{\sin((r+\tfrac12)\theta)}
 \ge\prod_{r=1}^j\frac{\sin(r\theta)}{\sin((r+1)\theta)}
 =\frac{\sin\theta}{\sin((j+1)\theta)}.
\]

Consequently, for \(N\ge3\),

\[
 A_j\ge\frac{4\cos^2(\theta/2)}{\sin^2((j+1)\theta)}
      \ge4\cos^2(\theta/2)\ge3.
 \tag{3}
\]

Fix \(0<a<b<1/2\) and choose integer endpoints \(L_N\sim aN\),
\(U_N\sim bN\) with \(U_N-L_N\) even. They lie in the original LEFT
range for all sufficiently large \(N\). At the ordinary positive radius
and common phase \(c=y=1\), the sharp stop-window polynomial and its
actual absolute envelope are

\[
 W_N=\sum_{j=L_N}^{U_N}(-1)^j A_j,\qquad
 E_N=\sum_{j=L_N}^{U_N}A_j.
\]

Pairing consecutive terms of the decreasing sequence and keeping the
last term gives

\[
 |W_N|\ge A_{U_N}\ge3,\qquad E_N\le N^3,\qquad
 \frac{|W_N|}{E_N}\ge\frac3{N^3}.
 \tag{4}
\]

The actual cap character is aligned only when the \(c\) and \(y\) phases
differ by \(\pi\). At the phases used in (4), they are equal, so their
distance to that supported alignment is \(\pi/2\), measured by the
smallest maximum circular distance after optimizing the common phase.
Nevertheless no fixed constants \(C,\kappa>0\) can satisfy
\(\lvert W_N\rvert\le C e^{-\kappa N}E_N\) on all these levels.
The retained alternating terms leave endpoint currents of at least
polynomial size; there is no strict local stop-action gap at the cap.

Therefore the regular-window angular theorem cannot be extended to a
flat cap merely by assigning it the same opposite-sign incidence labels.
An odd MAIN cycle involving such a cap does not by itself supply the
product-envelope exponential loss used by the regular cycle-packing
argument. This does not exclude cancellation after original shared
coefficient extraction, a combined analytic block estimate with other
ports, or a different source-preserving treatment of the cap boundaries.
It makes no assertion that \(W_N\) occurs uncoupled in the full invariant.

The proof is exact for every \(N\ge3\) and window lying in the stated range. It uses no asymptotic coefficient formula or numerical experiment.

The [stationary MAIN-cycle theorem](research_stationary_noncross_main_cycle_obstruction.md)
uses the cap character while keeping this limitation explicit.
