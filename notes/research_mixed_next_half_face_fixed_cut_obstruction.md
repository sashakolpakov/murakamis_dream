# A mandatory private-cut obstruction at the selected half face

Research deduction, 7 November 2026. Lowering the private main
contour inside the existing endpoint rectangle does not, by itself,
give the uniform prefix ceiling used in the selected-plateau
comparison. One of its unchanged real cuts already exceeds that
ceiling when paired with the undeformed conditional main.

This concerns an absolute bound for specified source pieces. It
is neither a lower bound for their signed integrals nor a comparison
with the complete reference-dependent affine action. No new numerical
evaluation or saved-certificate replay is used.

## 1. The original source and the proposed ceiling

Keep
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\quad N\ge2,
\]
and the exact source
\[
 U_{0,N}(w,X)=\sum_{j<N}H_N(w,r^{-j})p_j(X)/P_j,\qquad
 C_{1,N}(X,Y)=\sum_{k<N}X^{-k}p_k(X)p_k(Y)/P_k^3.
 \tag{1}
\]
Every \(H_N\) is the complete coherent endpoint polynomial.
Write \(J\) for the original sine primitive and
\[
 g(z)=J(z)+\frac{\pi i}{2}(z-z^2),\qquad
 \lambda(e)=\Re S(e)\quad(e\text{ real}).
 \tag{2}
\]
The private interpolation from
[the cap contour reduction, equations (4)--(7)](research_mixed_cap_outer_contour_reduction.md)
has phase
\[
 \Psi_0(e,a)=S(e)+g(e+a)-g(a)-\frac{\pi i}{2}(e-e^2).
 \tag{3}
\]
Its nonzero symbol and all scalars are those of the original source.
The conditional interpolation is
\[
 \begin{split}
 T_N(t;a,y)&=e^{2\pi iNat}\Pi_N(a+t)\Pi_N(y+t)
                         E_N(a)E_N(y)E_N(t)^3,\\
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat .
 \end{split}                                                    \tag{4}
\]
At physical \(t=k/N\), this is exactly the corresponding row of
(1). Both constant residue modes have density \(+N\); their
polynomial factors do not change the exponential rates below.

The remaining selected first-coordinate main has \(a\in[1/2,7/10]\),
private indices below \(1-a-\delta_*\), and conditional indices
below \(1-a-\varepsilon\). The accepted collar constants may be
decreased so that \(\delta_*,\varepsilon<1/10\). Thus
\[
 a_0=\frac12,\qquad e_0=\frac{27}{100},\qquad
 t_0=\frac14,\qquad y_0=\frac14+\frac{i}{100}
 \tag{5}
\]
lie below both walls and strictly inside the retained conditional
interval. Here \(e_0\) is the original lower private cut and
\(y_0\) belongs to the full selected plateau.

The sufficient polynomial bound in
[the filtered selected-plateau theorem](research_mixed_next_filtered_selected_plateau.md)
uses unit-disk prefix rate \(77/50\). Degree at most \(N-1\)
costs at most \(\pi/50\) on \(|Y|=e^{\pi/50}\), giving
\[
                              \frac{77}{50}+\frac{\pi}{50}.
 \tag{6}
\]
We test only this sufficient ceiling, before multiplying by the
following conditional factor and the selected Fourier weights.
Those factors, both of their alternatives, and the full affine
target are not replaced by (6).

## 2. The mandatory real private cut

The completed
[seam source record](../repro/results/research-mixed-cap-seam-source-bounds-replay.json),
SHA256
8d907c890073955f7e1122abc78f1334ab00a885959d839316d3852e2a64f3f8,
contains the outward enclosures
\[
 \begin{split}
 \lambda(7/20)&=[\,0.864089941023120636\ldots
                                      \ \mathord\pm1.37\,10^{-94}\,],\\
 \lambda'(7/20)&=[\,-0.004747972220743908\ldots
                                      \ \mathord\pm5.18\,10^{-95}\,].
 \end{split}
 \tag{7}
\]
Only \(\lambda(7/20)>21/25\) and \(\lambda'(7/20)<0\)
are used. The full printed enclosures, rather than the abbreviated
displays above, are the recorded input. They are read, not evaluated
again.

The exact curvature formula in
[the early real-row theorem, Lemma 1](research_mixed_cap_early_taper_real_rows.md)
is
\[
 -\frac{\lambda''(e)}{\pi}
 =\cot\pi e+\frac{2}{\sin\pi e}
                    \Re\frac1{\sqrt{2-e^{-2\pi ie}}}.
 \tag{8}
\]
On \(27/100\le e\le7/20\), one has
\(\cot\pi e<1\), \(\sin\pi e>1/\sqrt2\), and
\(\Re(2-e^{-2\pi ie})>2\). Hence
\[
                       0<-\lambda''(e)<3\pi<10 .
 \tag{9}
\]
Taylor's formula with integral remainder, from \(7/20\) to
\(27/100\), proves
\[
 \lambda(27/100)>
       \frac{21}{25}-5\left(\frac{2}{25}\right)^2
       =\frac{101}{125}>\frac45 .
 \tag{10}
\]
Its linear term is positive because the displacement and the
recorded derivative are both negative.

The sine-integral identity used in
[the wrapped-private theorem, equation (13)](research_mixed_next_wrapped_private_sector.md)
gives
\[
 -J(1/4)=\frac{G}{2\pi},\qquad
 G=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}.
 \tag{11}
\]
The alternating-series bound \(G>8/9\) and \(\pi<22/7\)
imply
\[
                    -J(1/4)>\frac{14}{99}>\frac7{50}.
 \tag{12}
\]
Since \(J'>0\) on \((1/6,1/2)\), also
\(-J(23/100)>-J(1/4)\). Therefore
\[
 \begin{split}
 \Re\Psi_0(e_0,a_0)
 &=\lambda(27/100)+J(77/100)-J(1/2)\\
 &=\lambda(27/100)-J(23/100)>\frac{47}{50}.
 \end{split}                                                    \tag{13}
\]
Here \(J(1/2)=0\) and \(J(1-e)=-J(e)\). The remaining
private scalar has zero real part at this real cut.

## 3. The retained conditional main

For real \(t\), the exact outgoing numerator rate is
\[
 I_y(t)=\int_0^t
       \log|1-e^{2\pi\Im y-2\pi i(\Re y+s)}|\,ds .
 \tag{14}
\]
At (5), each angle \(\Re y_0+s\) lies in \([1/4,1/2]\).
Its doubled-angle cosine is nonpositive, so
\[
              1+R^2-2R\cos(2\pi(\Re y_0+s))
 \tag{15}
\]
strictly increases for \(R\ge1\). The selected radius exceeds one,
and consequently
\[
 I_{y_0}(1/4)\ge J(1/2)-J(1/4)=-J(1/4).
 \tag{16}
\]
The full first-argument chirp in (4) has zero real part at these
real \(a,t\), so
\[
 \begin{split}
 \Re Q(t_0;a_0,y_0)
 &=J(3/4)-J(1/2)+I_{y_0}(1/4)-3J(1/4)\\
 &\ge-5J(1/4)>\frac7{10}.
 \end{split}                                                    \tag{17}
\]
Thus
\[
 \boxed{\quad
 \Re\{\Psi_0(e_0,a_0)+Q(t_0;a_0,y_0)\}
 >\frac{41}{25}
 >\frac{77}{50}+\frac{\pi}{50}+\frac{13}{350}.
 \quad}                                                        \tag{18}
\]
The last strict inequality is exactly \(\pi<22/7\).
No new critical action has been evaluated or compared.

This witness belongs to the original finite-source domains.
The private half-grid cut tends to \(e_0\), where the complete
endpoint coefficient has its established nonzero packet on \(E_c\).
All factorial arguments in (3)--(4) at (5) are regular and away
from their walls. Their nonzero symbols show that the logarithmic
rate of the product of the two exact interpolants tends to the
left side of (18), at both parities. Half-grid changes of
size \(O(N^{-1})\) do not change that rate. At height zero,
the private remainder kernels \(\cot(\pi Ne)\pm i\) at the real
half-grid cut have modulus one, so they supply no exponential loss
there. On an adjacent height interval of size \(O(N^{-1})\),
these kernels have fixed positive upper and lower bounds, and
the regular source changes by only \(O(1)\) in its exponent.
No absence of kernel decay is asserted at a fixed nonzero height.

An absolute pointwise majorant of these mandatory real-cut pieces
therefore cannot satisfy (6), regardless of the height chosen for
the private main segment. This does not preclude cancellation after
integration, cancellation against adjoining pieces, or simultaneous
transport of the conditional main and the private cut.

## 4. The shared incoming boundary

For real \(a,e,t\), with \(a\ge1/2\) and both sums below one,
\[
 \partial_a\Re(\Psi_0+Q)
 =\log\frac{\sin\pi(a+e)\sin\pi(a+t)}{\sin^2\pi a}<0.
 \tag{19}
\]
Thus the real prewall profile is largest at the half face, not at
the already paid far end. For \(a=1/2+ih\) and fixed regular
complex \(e,t\) with real parts in \((0,1/2)\), let
\(C(z)=\Re\cot\pi z\). The exact second derivative is
\[
 \partial_h^2\Re(\Psi_0+Q)
          =-\pi\{C(a+e)+C(a+t)\}>0 ,
 \tag{20}
\]
since \(C(a)=0\) and both summed real parts lie in \((1/2,1)\).
This is valid at any finite retained private/index heights within
the regular source chart.

Incoming-height convexity can reduce these regular profiles to their
two height endpoints, but its real endpoint still contains (18).
A signed whole-cap estimate at the other endpoint cannot be assigned
to an individual private cut. The initial incoming vertical join and
the retained joint real main still require shared-cut transport,
grouped cancellation, or comparison with the actual full affine
target. Only the stated uniform-ceiling strategy, with unchanged
real cuts and undeformed conditional main, is ruled out here.
