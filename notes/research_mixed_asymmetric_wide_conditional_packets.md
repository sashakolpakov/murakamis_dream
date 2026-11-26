# A wider independent own-angle conditional four-source chart

Research proof, 4 November 2026. Frozen manuscripts and completed
source artifacts are unchanged. A separate outward cover proves the wider
own-angle range below, retaining every original finite row and current.

The two independent products considered here have a low left angle and
a central own angle. This does not enlarge both neighbor angles toward
zero, and it does not prove a geometric supporting-plane comparison.

## 1. Domains and the original conditional root

Set
\[
 A_3=[.15,.22]+i[-.030,.020],\quad
 A_4=[.15,.22]+i[-.057,.0141],\quad
 B_4=[.24,.46]+i[-.057,.0141].
 \tag{1}
\]
The two products are \(A_3\times B_4\) and \(A_4\times B_4\).
This extends the proved [narrower own-angle chart](research_mixed_asymmetric_low_conditional_packets.md)
with own angle \([.28,.42]\), retaining a margin around \([.25,.45]\).
The variables \(\alpha,\beta\) are independent. Use the original
primitive, logarithmic lift and four-type phase
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad
 Q(s;\alpha,\beta)=g(s+\alpha)+g(s+\beta)-3g(s)+2\pi i\alpha s.
 \tag{2}
\]
All arguments used in the root and contour equations lie in the
regular strip \(0<\Re z<1\).

**Lemma 1.** On each entire product (1), \(Q_s=0\) has a unique
holomorphic root on a neighborhood of the closed product in
\[
 D=[.08,.49]+i[-.22,.15].
 \tag{3}
\]
On the larger index contour rectangle
\[
                   K=[.08,.49]+i[-.25,.20]
 \tag{4}
\]
one has \(-\Re Q_{ss}>1/8\).

Here are the analytic reductions for the outward check. Write
\[
 c(x,y)=\Re\cot\pi(x+iy)
       =\frac{\sin(2\pi x)}
              {\cosh(2\pi y)-\cos(2\pi x)}.
 \tag{5}
\]
The smallest shifted real argument is \(.08+.15=.23\).
The largest absolute shifted height is \(.307\).
The scalar inequality
\[
              \cos(.46\pi)\cosh(.614\pi)<1
 \tag{6}
\]
therefore makes every positive shifted real cotangent decrease
with its real argument. It also decreases with the absolute
imaginary part. For fixed index height \(y\), let \(d_\alpha\)
and \(d_\beta\) be the distances from zero to the allowed shifted
height intervals. On \(.08\le x\le.35\), it follows that
\[
 -\Re Q_{ss}\ge\pi\bigl[
 3c(x,y)-\max\{0,c(x+.15,d_\alpha)\}
          -\max\{0,c(x+.24,d_\beta)\}\bigr]>1/8.
 \tag{7}
\]
The checker proves the last inequality on 192 by 320 exact
cells for each product. Shifted-height interval endpoints are
rounded outward before taking their distance from zero.
For \(.35\le x\le.49\), both shifted cotangents are nonpositive,
so the uniform lower bound is simply
\[
       \frac{3\pi\sin(.98\pi)}
                    {\cosh(.50\pi)-\cos(.98\pi)}>1/8.
 \tag{8}
\]

On the four faces of (3), the checker proves
\[
 \Re Q_s(.08+iy)>1/50,\quad \Re Q_s(.49+iy)<-1/50,\quad
 \Im Q_s(x-.22i)>1/50,\quad \Im Q_s(x+.15i)<-1/50.
 \tag{9}
\]
Each original parameter contribution is harmonic separately.
Its extrema reduce to the four sides of its parameter rectangle,
covered by exact intervals. Every index face is covered as well.
Poincaré--Miranda gives an original zero; (7)--(8) imply
injectivity and simplicity on the convex root rectangle.
The implicit function theorem and compact strict margins then
give the global holomorphic branch. No exponentiated polynomial
equation is substituted for the logarithmic lift.

## 2. The complete finite packet

Retain the single canonical source
\[
 \mathcal L_{1,N}(\alpha,\beta)=
 \widehat P_N(N\alpha)\widehat P_N(N\beta)
 \sum_{j=0}^{N-1}
 \frac{e^{2\pi i\alpha j}
       (r^{N\alpha+1};r)_j(r^{N\beta+1};r)_j}{P_j^3},
 \quad r=e^{-2\pi i/N},\quad P_j=(r;r)_j .
 \tag{10}
\]
This is the same original finite function as in the
[transition-source theorem](research_mixed_transition_conditional_rectangles.md);
all revived rows remain in its sum.

**Theorem 2.** Uniformly on both products (1), for both parities,
\[
 \mathcal L_{1,N}=
 \frac{\sqrt{2\pi}\,A_1(s_*;\alpha,\beta)}
      {\sqrt{-Q_{ss}(s_*;\alpha,\beta)}}
 e^{NQ(s_*;\alpha,\beta)}(1+O(N^{-1})).
 \tag{11}
\]
The original factorial symbol \(A_1\) and Gaussian branch are
unchanged. They are holomorphic and nonzero. The result has all
fixed derivatives and fixed asymptotic orders on smaller products.

The distinguished-boundary source cover has 32 pieces. Every
rational affine Newton witness certifies the original root and
\[
                .24<\Re s_*<.42,\qquad -.21<\Im s_*<.15.
 \tag{12}
\]
Put \(\ell=.08,\ u=.49,\ h_-=-.25,\ h_+=.20\).
With \(M=\Re Q(s_*)\), the full-cell checks prove
\[
 \begin{split}
 M-\Re Q(\ell)&>10^{-4},\qquad M-\Re Q(u)>10^{-4},\\
 M-H_1(1)&>10^{-4},\\
 M-\Re Q(x+i h_\pm)+2\pi|h_\pm|&>10^{-3},
                                  \qquad \ell\le x\le u.
 \end{split}
 \tag{13}
\]
For each horizontal segment the checker evaluates the phase at its midpoint,
then bounds its whole real-index range by the concavity tangent
\(\Re Q(x+ih_\pm)\le\Re Q(x_0+ih_\pm)+\Re Q_s(x_0+ih_\pm)(x-x_0)\).
The derivative is enclosed on the full parameter cell. This uses the
fresh whole-index curvature bound, retaining every horizontal point
without a wide complex-dilogarithm interval overestimate.

The four last-row branches for \(H_1(1)\) and the exact right-tail
polynomial are all retained. That polynomial is below one up to
both quadratic vertices, reducing the whole right real tail
to its endpoints \(u,1\). The left real tail is increasing:
\[
 \Re Q_s(s)\ge
 \log\frac{4\sin(.15\pi)\sin(.24\pi)}
                {(2\sin(.08\pi))^3}-.08\pi>2,
                       \qquad 0<s\le.08.
 \tag{14}
\]
The exact height term here is
\(\pi(\Im\beta-\Im\alpha)\ge-.077\pi\), including both
shifted exponential-sine factors and the original chirp.
The shifted real sine arguments lie in \([.15,.30]\) and
\([.24,.54]\), respectively.

The exact cotangent trace has the original \(+N\) zero mode.
The lower and upper aliases carry their different penalties
\(2\pi|h_-|\) and \(2\pi h_+\). Neither is discarded.
The half-grid vertical currents have penalty \(2\pi|\Im s|\);
height convexity from Lemma 1 reduces them to the corresponding
real and horizontal endpoints in (13). The zero-mode vertical
joins at the selected height have a gap at least
\((.07)^2/16\), by (12) and the curvature bound.
All strict inequalities survive half-grid rounding.

The summand symbol has level power \(N^{-1/2}\); the trace
factor \(+N\) and one Gaussian give the \(N^0\) normalization
in (11). The normalized finite-source error is holomorphic with
a nonzero leading denominator throughout each parameter product.
Successive maximum-modulus principles extend the boundary estimate
to the full independent products. Strict compact margins justify
the derivative and higher-order assertions.

For the actual Laurent kernel \(C_{1,N}\), divide (11) by the
two original factorial interpolants. Its level power is \(N^{-1}\),
and its phase is \(Q(s_*)-g(\alpha)-g(\beta)\); the same exact
factorial symbol and branch conversion as in the transition
theorem applies.

## 3. Joining to the transition source

**Corollary 3.** The original root, phase and full source packet glue with
the transition theorem to one holomorphic packet on a neighborhood of
each closed product
\[
 \begin{split}
 \alpha&\in[.15,.45]+iH_\eta,\qquad
 \beta\in[.24,.45]+i[-.057,.0141],\\
 H_0&=[-.03,.02],\qquad H_1=[-.057,.0141].
 \end{split}
 \tag{15}
\]
The same original \(N^0\) coefficient in (11), or \(N^{-1}\) coefficient
for \(C_{1,N}\), is retained.

Indeed the low-left part is Theorem 2 and the part with
\(\Re\alpha\ge.22\) is the transition theorem. On their common slice
\(\Re\alpha=.22\), the transition root lies in
\([.10,.49]+i[-.17,.15]\), which is contained in (3).
It is an original logarithmic zero, so uniqueness in Lemma 1 identifies
it with this note's root. Simplicity identifies the holomorphic germs on
an open neighborhood of every point of the common compact slice.
The two branches therefore glue on a neighborhood of (15).

The phase formulas use the same original logarithms and factorial
symbols. The root agreement fixes their values and the Gaussian branch;
equivalently \(-\Re Q_{ss}>0\) fixes the same Gaussian square root on the
overlap. A finite subcover gives a uniform packet and all fixed
derivatives on smaller products. This is not a new off-grid
interpolation choice: the finite function (10) is identical on both
parts.

The joined product (15) is convex and contains the actual geometric
reference angles in its own-four coordinate. Consequently it can
support a later connected phase comparison to low-left targets.
That comparison, including the height change along a taper, is not
proved here.

## 4. Scope and reproduction

This is a full source chart with only the left real parameter
small. It does not control the both-low parameter corner.
In particular, proving that its selected phase lies below the
geometric supporting plane on a proposed graph contour is still
a separate comparison. No full outer-complement or mixed-word
lower bound is asserted.

    python3 experiments/certify_mixed_asymmetric_wide_conditional_packets.py

The new checker proves fresh root faces and the whole index
curvature, retains all finite-row and alias comparisons, and
verifies exact binary coverage of the 32 source pieces.
The author cover has 829 accepted source cells, eight root faces
with 1,024 exact slabs, and 122,880 curvature cells.
Completed proof and certificate files are not modified.
