# Full conditional sources on the two outer transition strips

Research proof, 4 November 2026. Frozen manuscripts and completed source
certificates are unchanged. The author outward cover, independent
written/code reviews, and a fresh higher-precision replay have passed.

This extends the full conditional packets to the independent real range
\([.22,.45]\), at all the original and selected heights. It supplies
source information on both sides of the old central region. It does
not compare the remaining outer integral with its geometric action.

## 1. A larger product and a fresh global root

Put
\[
 B_3=[.22,.45]+i[-.030,.020],\qquad
 B_4=[.22,.45]+i[-.057,.0141].
 \tag{1}
\]
The ordered families are
\((\epsilon,\alpha,\beta)=(0,B_3,B_3),(0,B_4,B_3),
(1,B_3,B_4),(1,B_4,B_4)\).
Use the original functions
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad
 Q_\epsilon(s;\alpha,\beta)
 =g(s+\alpha)+g(s+\beta)-(2+\epsilon)g(s)+2\pi i\alpha s.
 \tag{2}
\]
Every logarithmic equation below is on the original strip
\(0<\Re z<1\).

**Lemma 1.** On each full product, the original equation
\(Q_{\epsilon,s}=0\) has a unique holomorphic root on a
neighborhood of the closed parameter product, in
\[
                    D=[.10,.49]+i[-.17,.17].
 \tag{3}
\]
The full fixed index rectangle
\([.10,.49]+i[-.20,.20]\) has
\(-\Re Q_{\epsilon,ss}>1/8\).

Here is the curvature reduction used by the certificate. Write
\[
 c(x,y)=\frac{\sin(2\pi x)}
                   {\cosh(2\pi y)-\cos(2\pi x)}.
 \tag{4}
\]
For \(.10\le x\le.28\), the real part of each shifted cotangent
is at most \(c(x+.22,d)\), or zero if the latter is negative,
where \(d\) is the distance of zero from its allowed shifted
imaginary interval. Indeed a positive real cotangent decreases
with the imaginary magnitude. On the positive real-part interval
here, \(x+.22\ge.32\), it decreases with its real argument.
All shifted cotangents with real argument at least \(1/2\)
are nonpositive. Thus the lower bound
\[
 \pi\bigl[(2+\epsilon)c(x,y)
       -\max\{0,c(x+.22,d_\alpha)\}
       -\max\{0,c(x+.22,d_\beta)\}\bigr]>1/8
 \tag{5}
\]
reduces to two real variables. The checker encloses it on
128 by 256 exact cells for each family. For
\(.28\le x\le.49\), both shifted cotangents are nonpositive,
and the own term gives the direct bound
\[
 -\Re Q_{\epsilon,ss}\ge
 \frac{2\pi\sin(.98\pi)}{\cosh(.40\pi)-\cos(.98\pi)}>1/8.
 \tag{6}
\]
No derivative of a root proposal is a premise of these bounds.

For existence use the smaller typed rectangles with the same real
interval, bottom heights \(b_0=-.15,\ b_1=-.17\), and common
top height \(+.15\). The checker proves all four original pointing signs:
\[
 \Re Q_s(.10+iy)>1/50,\quad \Re Q_s(.49+iy)<-1/50,\quad
 \Im Q_s(x+i b_\epsilon)>1/50,\quad
 \Im Q_s(x+.15i)<-1/50.
 \tag{7}
\]
Each face has 128 exact slabs. The two parameter contributions
are harmonic separately; their extrema reduce to the four sides
of each parameter rectangle, each covered by 32 exact intervals.
Poincaré--Miranda proves existence of an original zero in each
typed rectangle. Strict negative real derivative on the larger
convex rectangle (3) proves
injectivity and simplicity. The implicit function theorem and
strict compact margins give the claimed global holomorphic branch.

## 2. Every finite row and contour current

Retain the same single canonical finite function as in the
[central source theorem](research_mixed_central_conditional_rectangles.md):
\[
 \mathcal L_{\epsilon,N}(\alpha,\beta)
 =\widehat P_N(N\alpha)\widehat P_N(N\beta)
 \sum_{j=0}^{N-1}
 \frac{e^{2\pi i\alpha j}
       (r^{N\alpha+1};r)_j(r^{N\beta+1};r)_j}
      {P_j^{2+\epsilon}},
 \quad r=e^{-2\pi i/N},\quad P_j=(r;r)_j .
 \tag{8}
\]
In particular no row is deleted when a physical zero is revived
off grid.

**Theorem 2.** Uniformly on each product (1), for both parities,
\[
 \mathcal L_{\epsilon,N}
 =N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}A_\epsilon(s_*;\alpha,\beta)}
      {\sqrt{-Q_{\epsilon,ss}(s_*;\alpha,\beta)}}
 e^{NQ_\epsilon(s_*;\alpha,\beta)}(1+O(N^{-1})).
 \tag{9}
\]
The symbol and square-root branch are exactly those in the
central theorem. They are holomorphic and nonzero; the statement
has all fixed derivatives and all fixed orders on smaller products.

The source cover has 64 distinguished-boundary pieces.
Every accepted rational affine Newton witness verifies the original
logarithmic equation and
\[
                  .20<\Re s_*<.46,\qquad |\Im s_*|<.17.
 \tag{10}
\]
Set \(\ell=.10,\ u=.49,\ h=.20\) and \(M=\Re Q_\epsilon(s_*)\).
On each full parameter cell the certificate proves
\[
 \begin{split}
 M-\Re Q_\epsilon(\ell)&>10^{-4},&
 M-\Re Q_\epsilon(u)&>10^{-4},\\
 M-H_\epsilon(1)&>10^{-4},&
 M-\Re Q_\epsilon(x\pm ih)+2\pi h&>10^{-3}
                       \quad(\ell\le x\le u).
 \end{split}
 \tag{11}
\]
All four analytic branches for the full periodic last-row entropy
\(H_\epsilon(1)\) are retained. The exact right-tail polynomial
is below one up to both of its quadratic vertices, so the entire
right real tail is controlled by its two endpoints \(u,1\).
The left real tail is increasing: for \(0<s\le.10\),
\[
 \Re Q_s(s)\ge
 2\log\frac{\sin(.22\pi)}{\sin(.10\pi)}-.08\pi>1 .
 \tag{12}
\]
Indeed the real shifted arguments lie in \([.22,.55]\),
their sine moduli are at least \(\sin(.22\pi)\). The exact
logarithmic modulus contributes
\(\pi(\Im\beta-\Im\alpha)\ge-.077\pi>-.08\pi\);
this includes the exponential factors in both shifted sines and
the original chirp. Finally,
\(2\sin(\pi s)<1\), so the extra four-type denominator
only increases this lower bound.

The finite cotangent trace has the unchanged \(+N\) zero mode.
Both horizontal aliases and the half-grid vertical currents are
retained. The latter have penalty \(2\pi|\Im s|\); height
convexity from Lemma 1 reduces them to the real and horizontal
endpoints in (11). At the selected height, the zero-mode vertical
joins have a strict gap at least
\((.03)^2/16\), by (10) and the curvature bound.
All strict bounds survive half-grid rounding.

The exact summand symbol is
\(N^{-\epsilon/2}A_\epsilon e^{NQ_\epsilon}\).
Combining \(+N\) with the Gaussian gives (9), with the original
normalization. The normalized error is holomorphic on each full
parameter product; Lemma 1 supplies its nonvanishing leading
denominator. The maximum-modulus principle in the two parameters
extends the boundary estimate throughout the products.

For the Laurent kernel
\(C_{\epsilon,N}=\mathcal L_{\epsilon,N}/
[\widehat P_N(N\alpha)\widehat P_N(N\beta)]\), the phase remains
\(Q_\epsilon(s_*)-g(\alpha)-g(\beta)\) and the level power remains
\(N^{-(1+\epsilon)/2}\). This is an extension of the actual finite
source, not only of its formal selected phase.

## 3. Scope and reproduction

The products contain all original critical heights, all selected
heights up to \(+.014\), and every intermediate height in the
periodic graph taper whenever its real coordinate lies in
\([.22,.45]\). They do not include the whole left or right
outer complement. No supporting-plane inequality, global
mixed-word asymptotic, or ordinary-boundary packet follows from
Theorem 2 alone.

Run

    python3 experiments/certify_mixed_transition_conditional_rectangles.py

The author cover has 64 source pieces and 1,903 accepted cells,
16 root-existence faces with 2,048 slabs, and 131,072 curvature
cells. The new checker retains exact binary coverage, rational affine
witnesses, all original source endpoints and aliases, fresh
root-existence faces, and the two-variable curvature cover.
Completed central artifacts are inputs and are not modified.
