# The exact low-index source after coherent high-tail removal

Research deduction, 7 November 2026. The retained index is split
before any estimate of the outgoing sum. The complete high-index
group has already been paid coherently. This note retains the exact
remaining low-index group and gives its own finite contour reduction.
Its physical complement needs only three real faces; the central
contour also retains the fourth, artificial truncation face.

The resulting four-face comparison is a sufficient condition, not a
proved sign. In particular a separately estimated face can lose
cancellation. The coherent high-tail bound is never inserted as a
termwise estimate for the old two-dimensional contour decomposition.
No analytic function, root, source, or candidate is evaluated.

## 1. The split and the original finite source

Keep the actual reference and normalization of the
[bare inner-source completion](research_mixed_fourier_right_cap_bare_inner_completion.md):
\[
 \eta\in\{0,1\},\quad a_*\in K_{3+\eta},\quad
 (s_*,q_*)\in O_4^2,\quad
 a=x+i\Im a_*,\quad x\in P=[11/50,9/20],\quad y=x_0.
 \tag{1}
\]
Set
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\quad X=e^{-2\pi ia},\quad Y=e^{2\pi iy},
 \]
and retain the original cardinal coefficients
\[
 f_l(y)=\frac{e^{-\pi i(N-1)y}}N\,
                  Y^l\prod_{k=l+1}^{N-1}(1-Yr^k).
 \tag{2}
\]
Define \(M_N=\lceil N/2\rceil-1\) and the literal polynomial
\[
 C_N^{<}(X,Z)=
       \sum_{j=0}^{M_N}X^{-j}\frac{p_j(X)p_j(Z)}{P_j^3}.
 \tag{3}
\]
The low-index source is exactly
\[
 \begin{split}
 V_N^{<}(y,X)
 &=\sum_{l=0}^{N-1} C_N^{<}(X,r^l)f_l(y)\\
 &=\sum_{j=0}^{M_N}
           X^{-j}\frac{p_j(X)}{P_j^3}H_{j,N}(y),\\
 H_{j,N}(y)&=\sum_{l=0}^{N-j-1}\frac{P_{j+l}}{P_l}f_l(y).
 \end{split}
 \tag{4}
\]
The equality follows from the original factorial recurrence and
the exact vanishing of \(p_j(r^l)\) when \(j+l\ge N\).
It is a finite reordering, with no off-grid substitution.
Every \(H_{j,N}\) in (4) still contains its whole outgoing sum.
In particular \(j=0\) and \(l=0,N-1\) retain their original
physical values.

Write \(V_N^{\rm F}=V_N^{<}+V_N^{\ge}\).
The [coherent high-tail payment](research_mixed_fourier_right_cap_coherent_high_tail_payment.md)
proves, with the same incoming allocation,
\[
 |d_N(X)|^{\eta/2}|V_N^{\ge}|
 \le C_\tau N^{A_\tau}
         e^{N\{B_\eta(x)-1/35000+\tau\}},
 \tag{5}
\]
where
\[
 \begin{split}
 B_\eta(x)&=M_\eta+p_\eta(x-\Re a_*)
                                  -\kappa(x-\Re a_*)^2,\\
 \mathcal L_\eta(x,z)&=B_\eta(x)-\kappa(z-\Re q_*)^2,
                   \qquad \kappa=1/2500000.
 \end{split}
 \tag{6}
\]
All actions, marginals and quadratic costs are the original ones.
Equation (5) applies only to the complete group \(V_N^\ge\).

## 2. The truncated source inherits the proved plateau upper bound

Put \(q=z+i\Im q_*\), \(z\in P\), and
\(C_N^\ge=C_{1,N}-C_N^<\).
The original individual real-row argument in Section 4 of the
[bare inner-contour theorem](research_mixed_fourier_right_cap_bare_inner_contour.md)
bounds every row \(j/N\ge1/2\) by the larger of the two profiles
at \(1/2\) and \(1\). Its source hypotheses are unchanged here:
\(a,q\) have their actual negative outgoing critical-height
allocation, and both horizontal targets belong to \(P\).
The [completed three margins](research_mixed_fourier_right_cap_bare_inner_completion.md),
equation (6), therefore give
\[
 |d_N(X)|^{\eta/2}
 |C_N^\ge(X,e^{-2\pi iq})f_N(q;y)|
 \le C_\tau N^{A_\tau}
      e^{N\{\mathcal L_\eta(x,z)-1/35000+\tau\}}.
 \tag{7}
\]
This is a direct estimate for the high real rows at this fixed
complex \(q\), not an application of (5).

Subtract (7) from the exact full conditional source, using the
triangle inequality and its proved upper bound. One obtains
\[
 |d_N(X)|^{\eta/2}
 |C_N^<(X,e^{-2\pi iq})f_N(q;y)|
 \le C_\tau N^{A_\tau}e^{N\{\mathcal L_\eta(x,z)+\tau\}}.
 \tag{8}
\]
On this same compact negative-height strip, the exact factorial
suffix interpolation \(\widehat f_N\) and \(f_N\) have their
proved matching calibrated expansions and ratio \(1+O(N^{-1})\).
Thus (7)--(8) also hold with \(\widehat f_N\), after changing
constants. This comparison is used only on the stated strip.
Neither (7) nor (8) bounds the physical outgoing endpoints or
the tall outgoing contours.

## 3. An exact rectangle inside the low-index group

Let
\[
 L_{s,N}=\lceil N/8\rceil,\qquad
 L_{q,N}=\lceil11N/50\rceil,\qquad
 U_{q,N}=\lfloor9N/20\rfloor.
 \tag{9}
\]
The central physical rectangle consists of
\[
 L_{s,N}\le j\le M_N,\qquad
 L_{q,N}\le l\le U_{q,N}.
 \]
For all sufficiently large \(N\), every such point has
\(j+l<N\). The remaining supported points of (4) are partitioned
disjointly into:

1. the two outgoing tails \(l<L_{q,N}\) or \(l>U_{q,N}\),
   with \(0\le j\le M_N\);
2. the low retained rows \(j<L_{s,N}\), with
   \(L_{q,N}\le l\le U_{q,N}\).

Every point still has its original support condition \(j+l<N\).
These two sets and the rectangle exhaust (4).

Use half-grid contour cuts
\[
 \ell_{s,N}=(L_{s,N}-1/2)/N,\quad
 u_{s,N}=(M_N+1/2)/N,
 \quad
 \ell_{q,N}=(L_{q,N}-1/2)/N,\quad
 u_{q,N}=(U_{q,N}+1/2)/N.
 \tag{10}
\]
In particular \(u_{s,N}=1/2-1/(2N)\) at even levels and
\(u_{s,N}=1/2\) at odd levels. Their limit rectangle is
\[
                         C=[1/8,1/2]\times P.
 \tag{11}
\]
Its exact central row is the same specific factorial interpolation
as in the [outer-contour theorem](research_mixed_fourier_right_cap_outer_contour.md):
\[
 T_N(s,q;a,y)=e^{2\pi iNas}
    \frac{\Pi_N(s+a)\Pi_N(s+q)}
         {\Pi_N(a)\Pi_N(q)\Pi_N(s)^3}\,
                         \widehat f_N(q;y).
 \tag{12}
\]
It matches exactly every central physical row. The real parts of
all factorial arguments, including \(q-y\), stay strictly between
zero and one on a neighborhood of this rectangle. Thus the fixed
contour heights
\[
              s:\ [-1/5,5/4],\qquad q:\ [-1/5,1/2]
 \tag{13}
\]
are legal for this very source, with no endpoint extension of
\(\widehat f_N\). The row power remains \(N^{-5/2}\), and the
two-index zero-mode coefficient is exactly \(+N^2\).

## 4. Three faces control the literal physical complement

Use the original allocated physical row rate, continuous on its
closed supported triangle,
\[
 \begin{split}
 E_\eta(s,q;a)={}&I_a(s)+J(s+q)-J(q)-3J(s)-2\pi h_a s\\
 &-\frac\eta2\Re g(a)+\Re\ell_q(y),\\
 I_a(s)&=\int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt,\qquad
 h_a=\Im a.
 \end{split}
 \tag{14}
\]
The uniform zero-safe product bounds and the original physical
cardinal product give this rate on every physical row, including
both true outgoing ends. For real \(q\), its cardinal phase uses
the original unit-disk formula on the entire period; it does not
use (12) beyond its regular strip.

The outgoing monotonicities from the outer-contour theorem are
\[
 \begin{array}{ll}
 E_{\eta,q}<-\log(7/5),&
 q\ge9/20,\quad s+q\le1,\\
 E_{\eta,q}>\log(6/5),&
 1/8\le s\le1/2,\quad 0<q\le11/50.
 \end{array}
 \tag{15}
\]
The first bound holds for every supported \(s\), including \(s=0\);
its proof above \(q=1/2\) uses
\(|1-Ye^{-2\pi iq}|>(7/5)|Y|\), not a bound by one.

The remaining low-\(s\) comparison slightly extends the domain
explicitly used in that note:
\[
 E_{\eta,s}>\frac4{25},\qquad
                  0<s\le1/8,\quad 0\le q\le9/20.
 \tag{16}
\]
Indeed \(q\le9/20\le1-2s\), so
\(\sin\pi(s+q)\ge\sin\pi s\). The exact derivative therefore
has the same lower bound as the earlier calculation:
\[
 E_{\eta,s}\ge
 \log\frac{|\sin\pi(a+s)|}{2\sin^2\pi s}-\pi h_a
   >\log(15/8)-.108\pi>\frac4{25}.
 \tag{17}
\]
Here \(\Re(a+s)\in[.22,.575]\), its sine modulus exceeds
\(3/5\), and \(\sin(\pi/8)<2/5\). All inequalities are the
same elementary witnesses; only the preceding sine comparison
needed the larger \(q\)-interval.

Every physical complement point from Section 3 can now be moved
without decreasing (14) to one of the following three closed faces:
\[
 \begin{split}
 F_L&=\{1/8\}\times P,\\
 F_-&=[1/8,1/2]\times\{11/50\},\\
 F_+&=[1/8,1/2]\times\{9/20\}.
 \end{split}
 \tag{18}
\]
For an upper outgoing tail first decrease \(q\) to \(9/20\),
preserving support; if needed, then raise \(s\) to \(1/8\).
For a lower outgoing tail, first raise a low \(s\) to \(1/8\)
using (16), then raise \(q\) to \(11/50\) using (15).
For the low retained rows with \(q\in P\), only (16) is needed.
All raised points stay supported, since their sums are at most
\(1/2+9/20<1\). The original low/high outgoing marker is
retained until it reaches its corresponding face.
The comparisons extend to true endpoints by continuity.

Define
\[
 E_3(a)=\max_{(s,q)\in F_L\cup F_-\cup F_+}E_\eta(s,q;a).
 \tag{19}
\]
The entire supported physical complement of the low-index
rectangle is bounded by
\[
 C_\tau N^{A_\tau}e^{N\{E_3(a)+\tau\}},
 \tag{20}
\]
including its incoming halfweight. The row count and the
uniform endpoint-factorial errors are polynomial. There is no
high-\(s\), low-\(q\) wedge in this restricted source.
Statement (20) is an absolute upper envelope; no comparison
of \(E_3\) with the reference plane is made.

## 5. All central corrections and the fourth face remain

On \(C\), write the original calibrated phase as
\[
 F_\eta(s,a,q)=g(s+a)+g(s+q)-3g(s)
 -(1+\eta/2)g(a)-g(q)+2\pi ias+\ell_q(y).
 \tag{21}
\]
At real \(s,q\) in \(C\), this equals the rate (14) in real
part: every numerator argument lies in the original regular strip.
Set
\[
 E_4(a)=\max_{(s,q)\in\partial C}\Re F_\eta(s,a,q).
 \tag{22}
\]
Thus \(E_3\le E_4\), and the extra face is
\[
                         F_R=\{1/2\}\times P.
 \tag{23}
\]
It is the limiting artificial truncation face of (10), rather
than a remaining high-index physical tail.

Let \(I_N^<(a,y)\) be the exact double zero-mode current of (12)
on the actual critical-height lines over the cut rectangle (10).
The original main-sheet curvature gives
\[
 \Re F_\eta(s+ih_s,a,q+ih_q)
 \le B_\eta(x)-\kappa\{(s-\Re s_*)^2+(q-\Re q_*)^2\}.
 \tag{24}
\]
The main-sheet face loss may be taken to be
\(\delta_C=\mu/5000\), \(\mu=1/1250000\), as in the
outer-contour theorem.

The exact residue calculation for the central rectangle retains
all fifteen nonmain tensor products, with both vertical sides
of each vertical factor. Its all-height derivative strips,
horizontal penalties and common-height joining paths are
unchanged by the truncation (10). The same proof therefore gives
\[
 \begin{split}
 |d_N(X)|^{\eta/2}
 |V_N^<(y,X)-I_N^<(a,y)|
 &\le C_\tau N^{A_\tau}
  e^{N\{\max(E_4(a),B_\eta(x)-\delta_C)+\tau\}},\\
 |d_N(X)|^{\eta/2}|I_N^<(a,y)|
 &\le C_\tau N^{A_\tau}e^{N\{B_\eta(x)+\tau\}}.
 \end{split}
 \tag{25}
\]
To spell out the scope of this reuse: penalized verticals reset
to their own marked real faces; horizontal outgoing aliases are
first reset into the negative critical-height interval, before
the sharper inner alias estimate is used. A lone alias retains
the other coordinate's two joining sides. The remaining zero-mode
joins use convexity along simultaneous height scaling, with
endpoints bounded by (22) and the critical-height face loss.
No independently reset, unpenalized corner is omitted.
The literal physical complement is supplied by (20), and the
half-grid perturbations are absorbed by the single prescribed
tolerance. Both parities and the original cardinal normalization
are retained.

Finally, (4)--(5) and (25) give the exact-source reduction
\[
 \begin{split}
 |d_N(X)|^{\eta/2}|V_N^{\rm F}(y,X)-I_N^<(a,y)|
 \le C_\tau N^{A_\tau}
 \exp N\Big\{\max\big(&E_4(a),B_\eta(x)-\delta_C,\\
                     &B_\eta(x)-1/35000\big)+\tau\Big\}.
 \end{split}
 \tag{26}
\]
This now has an explicit finite list of four closed, complete
real-face profiles. A uniform strict comparison of (22) with
\(B_\eta\) would complete this particular source contour bound.
Such a comparison is not asserted, and may be stronger than
necessary if its separate absolute face estimates lose cancellation.
In particular the paid coherent value at \(s=1/2\) is not a
pointwise estimate on (23): that payment retains the entire
outgoing sum, whereas (23) fixes a real outgoing coordinate.
Further coherent regrouping must be proved at the exact-source
level before those quantities can be identified.
