# The wider edge above its endpoint rate, and the right-face vertical

Private finite-source deduction, 9 November 2026. The complete wider
positive-edge envelope has a nonzero relative packet wherever its
critical value strictly exceeds the endpoint rate. This supplies a
comparison between that critical value and the complete row norms.
It then reduces the right-face inner vertical to its two endpoint
bounds. The high endpoint comparison and the low row bound are
retained explicitly.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation or frozen-source edit is used.

## 1. Exact wider source and the strict region

Fix \(a_L>0\). Use precisely the parameter box and original
reciprocal-factorial interpolation of the
[positive wider-edge theorem](research_mixed_symmetric_closing_positive_first_angle_wider_edge.md):
\[
 \begin{gathered}
 t=a-iH,\quad a_L\le a\le2\pi/3,\quad1/10\le H\le1,\\
 u=\beta-iK,\quad0\le\beta\le2\pi/3,\quad0\le K\le7/10,\\
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u).
 \end{gathered}
 \tag{1}
\]
Put
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D=A+B-AB,\quad W=AB/D,\quad
 m=\Re\psi(t,u),\quad e=(H+K)/2.
 \tag{2}
\]
Here \(\psi\) is the same original zero-charge primitive as in
that theorem, including its complete-edge constant.

**Strict-region packet.** On every compact subset of (1) where
\(m>e\), the literal finite kernel has, on a fixed independent
complex neighborhood, the asymptotic
\[
 K_N^<(t,u)=
 N^{-3/2}\frac{e^{N\psi(t,u)}}{4\sqrt D\,W^{1/4}}
                  (1+O_{\mathrm{hol}}(N^{-1})).
 \tag{3}
\]
The roots and orientation are the original continued Gaussian
ones. The coefficient is nonzero. Fixed derivatives of the
normalized remainder satisfy the same bound on smaller
neighborhoods. No relative statement is made across \(m=e\).

Here is the full source justification for upgrading the envelope.
The wider positive-edge proof gives the original force-one point
\[
 y_*=\pi^{-1}\arctan\sqrt W,\qquad
 F_y(y_*)=0,\quad F(y_*)=\psi,\quad
 -F_{yy}(y_*)=\frac{2\pi D(1+W)^2}{W^{3/2}}\ne0,
 \quad F=b(\,\cdot\,,t)+b(\,\cdot\,,u).
 \tag{4}
\]
It is the unique finite critical point in the upper half-strip.
All four original cut-force bounds are strict; the original
real-wire inward derivative excludes a bottom minimum. The left
side increases from rate zero. Each right-side strict sublevel is
connected or empty, with its real endpoint at rate \(e\).
The original subharmonic component argument therefore sends the
two descending germs to different sides. They cannot rejoin in
one component: a finite crosscut would enclose an ascending germ
with smaller boundary values. Thus the main contour crosses the
saddle once, from the left-side component to the right-side
component, with the same orientation as the original branch.

On a compact set \(m-e\ge\epsilon_0>0\), both real endpoints
are strictly below the saddle. The side connections, the
descending germs outside a fixed Morse chart, and the short
endpoint connections can consequently be chosen with a strict
gap below \(m\). Their lengths and gaps are uniform on fixed
parameter charts; a finite cover gives uniformity on the compact
set. This is the same strict-sublevel step used in Sections 5--6
of the adopted
[opposite-height theorem](research_mixed_symmetric_closing_opposite_height_high_edge.md).
Here the critical point stays in the upper half-strip, so its
real-transition analysis is not needed.

To retain every finite term, write \(\zeta=e^{2\pi iNy}\) and
keep the wider theorem's exact identity
\[
 \begin{split}
 K_N^<={}&N\int_{\Gamma_+}\frac{T_N}{1-\zeta}\,dy
          +N\int_{\Gamma_-}\frac{T_N}{\zeta-1}\,dy+C_N+E_N,\\
 C_N={}&N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
                       \frac{T_N}{\zeta-1}\,dy
       -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
                       \frac{T_N}{\zeta-1}\,dy,\\
 E_N={}&\sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N)
           +\sum_{j=\lceil N\gamma\rceil}^{U_N}T_N(j/N).
 \end{split}
 \tag{5}
\]
The midpoint columns, orientations and interpolation \(T_N\)
are unchanged. Splitting the upper denominator leaves the whole
unweighted integral and the exact added caps
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy+
 N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy .
 \tag{6}
\]
The two complete aliases retain their full denominators and
height-two paths. Their boundary rates are at most \(D_*\) and
\(e\), where \(D_*=(aH+\beta K)/(2\pi)\) and
\(e-D_*\ge1/60\); their deep rates are below \(e-3/200\).
The original midpoint cap denominators have reciprocal modulus
at most one. Both physical endpoint groups and all added caps
have rates at most \(e+\epsilon\), with collars chosen first
so that \(\epsilon<\epsilon_0/4\). Their polynomial factors do
not affect the strict gap. In particular no parity-dependent
last row, cap or alias is discarded.

Off the original cuts, the unchanged local factorial symbol is
\[
 T_N(y)=\frac{e^{NF(y)}}{4N^2\sin^2(\pi y)}
                         (1+O_{\mathrm{hol}}(N^{-1})).
 \tag{7}
\]
The unique saddle crossing in (4) gives
\[
 N\,N^{-2}N^{-1/2}
 \frac{\sqrt{2\pi}}
 {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*)}}
       =N^{-3/2}\frac1{4\sqrt D\,W^{1/4}}.
 \tag{8}
\]
This proves (3), with all remaining contributions exponentially
smaller. Strict source margins persist in independent complex
charts. Holomorphy and normalized Cauchy estimates give the
stated derivative conclusion. This proof uses the exact source
decomposition; an upper envelope alone would not imply (3).

## 2. A critical-value comparison with complete row norms

For any angular argument \(z\) define the complete row profile
\[
 \begin{split}
 V_z(y)&=\int_0^y
       \log|2\cos(2\pi x)+2\cos z|\,dx-2J(y),\\
 J(y)&=\int_0^y\log(2\sin\pi x)\,dx,\qquad
 m_{\rm row}(z)=\max_{0\le y\le1/2}V_z(y).
 \end{split}
 \tag{9}
\]
The zero-safe product proof in Section 2 of the
[low-horizontal norm theorem](research_mixed_symmetric_closing_low_horizontal_norm.md)
is uniform on every fixed bounded angular-height rectangle,
including (1). It estimates every initial product even after
a numerator zero and at both index endpoints. Hence
\[
 |K_N^<(t,u)|
 \le
 \left(\sum_{j=0}^{U_N}|e_j(-2\cos t)|^2\right)^{1/2}
 \left(\sum_{j=0}^{U_N}|e_j(-2\cos u)|^2\right)^{1/2}
 \le C N^A e^{N(m_{\rm row}(t)+m_{\rm row}(u))}.
 \tag{10}
\]
At any point \(m>e\), taking the exponential rate of (3) and
then (10) gives \(m\le m_{\rm row}(t)+m_{\rm row}(u)\).
At points \(m\le e\) no packet is needed. Consequently,
throughout (1),
\[
 \boxed{\quad
 \Re\psi(t,u)\le
       \max\{(H+K)/2,\ m_{\rm row}(t)+m_{\rm row}(u)\}.
 \quad}
 \tag{11}
\]
This is an inequality for the original critical value. It does
not identify the signed kernel with its positive row bound.

## 3. The positive right-face vertical

Now restrict \(u\) to the outer hyperbola of the
[positive saddle-path theorem](research_mixed_symmetric_closing_wider_positive_saddle_path.md):
\[
 \pi/2\le\beta\le2\pi/3,\qquad
 K=\frac{\pi K_g}{2\beta}.
 \tag{12}
\]
Let \(t_R=2\pi/3-iH_R(u)\) be the endpoint of its explicitly
defined positive path, and set
\[
 a_0=2\pi/3,\quad h_0=1/10,\quad t_0=a_0-ih_0,\qquad
 \gamma_V:t_R\longrightarrow t_0 .
 \tag{13}
\]
The whole vertical stays in (1). Retain its two literal rates
\[
 \begin{split}
 G(H)&=\Re\Phi(a_0-iH,u),\\
 E(H)&=\Re\psi(a_0-iH,0)+(H+K)/2
                           +3a_0H/(2\pi)-H .
 \end{split}
 \tag{14}
\]
Both functions are convex in \(H\). Indeed the Hessian signs
proved in the positive saddle-path theorem give
\[
 G''(H)=-\Re\Phi_{tt}>0,\qquad
 E''(H)=-\Re\psi_{tt}(a_0-iH,0)
       =\frac{\Re\sec((a_0-iH)/2)}{2\pi}>0.
 \tag{15}
\]
Thus each rate on (13) is bounded by the larger of its two
endpoint values.

At the upper endpoint, that theorem gives
\[
 G(H_R)\le s(u),\qquad
 E(H_R)\le
 \max\{123/100+K/2,\ E_{\rm high}(u)\}.
 \tag{16}
\]
The convention is to omit \(E_{\rm high}\) if its defining
part of the positive path is empty.
At the lower endpoint, (11) gives the source-valid comparison
\[
 G(h_0)\le\max\{E(h_0),\,R_{\rm row}(u)\},\qquad
 E(h_0)<123/100+K/2,
 \tag{17}
\]
where the exact row rate is
\[
 R_{\rm row}(u)=
   \Re\psi(t_0,0)+m_{\rm row}(t_0)+m_{\rm row}(u).
 \tag{18}
\]
There is no omitted linear term in (18):
\(3a_0h_0/(2\pi)-h_0=0\).

In particular, with every original trace factor retained,
\[
 \begin{split}
 &\frac{N^2}{\pi}\int_{\gamma_V}
 \left|\sin t\,K_N^<(t,0)K_N^<(t,u)
       e^{3iNt^2/(4\pi)}
       \frac{e^{-iNt}}{(1-(-1)^{N-1}e^{-iNt})^2}\right|\,|dt|\\
 &\qquad\le C_\tau
 \exp N\left[
   \max\{s(u),\,123/100+K/2,\,
                  E_{\rm high}(u),\,R_{\rm row}(u)\}+\tau
 \right].
 \end{split}
 \tag{19}
\]
It also bounds the signed current with its original scalar
\(-N^2C_{N,3}/(\pi i)\). To prove (19), apply the first-short
slit bound and the complete wider second-edge envelope on
the fixed compact vertical, then (15)--(18). Heights are at
least \(1/10\), so the full sampling denominator is uniformly
bounded and all remaining factors are polynomial.

The first two rates in (19) have their previously proved
outer hyperbola budgets. This note retains
\(E_{\rm high}\) and \(R_{\rm row}\) explicitly.
If separate source proofs pay those two rates after adding
the outer half-weight \((\beta/\pi-1/2)K\), then the same
is true for this entire vertical. No such inequality is
assumed in deriving (19), and no full inner or outer closing
asymptotic is asserted here.

## Frozen source bindings

- Complete wider positive edge, cut guards, original charge,
  side construction and exact caps:
  f3f9cdca2307f100a5766638ae91e329be5c7f372ac9b303ede0a28c9953e22f.
- Original strict-region Gaussian extraction and local symbol:
  19aa75ce4c6c8b461e55295da4ce51c67bf4ee83d4550318773b01a302bdc74d.
- Complete zero-safe row norms:
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- Wider selected positive path and both Hessian signs:
  6e362aec94c3ae00bab51e7d4c1d6928a6c4aff8fdcdbd68a475b7e9346d7e8c.
- First-short slit bound:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Complete fixed-depth endpoint budget:
  f6dafa452dab15d307b7d2aad771b66409356ecf20aa441da38c01f45315c6b3.
