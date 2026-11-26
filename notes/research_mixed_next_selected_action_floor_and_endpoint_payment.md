# The selected inner action pays the right-edge endpoint sector

Private written action and finite-source deduction, 9 November 2026.
The original selected inner action is uniformly greater than \(331/200\)
throughout the full charged curve. The endpoint sector of the complete
shortened second-edge bound is less than \(33/20\). This pays that
sector with a fixed gap, and completes the actual-height horizontal
segment from \(\pi/2\) to \(2\pi/3\) for the unchanged two-short-edge
inner current.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Original family and conclusions

Keep the original calibrated action and selected charged curve:
\[
\begin{gathered}
 u_\delta=\beta-iK,\qquad 0\le\delta\le1/2,\qquad
 t_*(u_\delta)=a_*(u_\delta)-iH_*(u_\delta),\\
 S(u)=S_3(0,u),\qquad s(u)=\Re S(u),\qquad
 M_3=\Re S(0)>9/5,\\
 S'(u)=-\pi^{-1}\operatorname{arsinh}
              \{c(u)\tan(u/2)\},\qquad c(u)=\cos(t_*(u)/2).
\end{gathered}
\tag{1}
\]
The derivative and its additive constant are those of
[cubic continuation, (8)](research_mixed_next_inner_three_cubic_continuation.md)
and the original complete single-three source in
[Theorem 1 and Section 4](research_all_nonzero_degree_two_fillings.md).

The adopted
[angle-depth correlation](research_mixed_next_selected_charged_angle_depth_correlation.md)
and [depth bound](research_mixed_next_selected_charged_depth_bound.md)
give
\[
 0<\beta<8/7,\qquad 0<K<2/5\quad(\delta>0).
\tag{2}
\]
At \(\delta=0\), both quantities vanish. The original
[right-edge guards](research_mixed_next_selected_right_edge_cut_guards.md)
also give
\[
             0<a_*<\pi/2,\qquad 2/3<H_*<1.
\tag{3}
\]

**Theorem.** Uniformly on this closed selected family,
\[
              s(u_\delta)>\frac{2651}{1600}>\frac{331}{200}.
\tag{4}
\]
For every
\[
             \pi/2\le a\le2\pi/3,\qquad 2/3\le H\le1,
\]
the original attached endpoint-sector rate satisfies
\[
\begin{split}
 E_{\mathrm{end}}(a,H,u_\delta)
  &:=\Re\psi(a-iH,0)+\frac{H+K}{2}
                          +\frac{3aH}{2\pi}-H\\
  &<\frac{33}{20}<s(u_\delta)-\frac1{200}.
\end{split}
\tag{5}
\]
In particular this applies at the actual height \(H=H_*(u_\delta)\).

Let
\[
 d_R=\pi/2-\max_{0\le\delta\le1/2}a_*(u_\delta)>0,\qquad
 \epsilon_R=\frac12\min\left\{\frac1{200},
                                      \frac{d_R^2}{8\pi}\right\}.
\tag{6}
\]
The exact finite current on the actual-height segment, defined in
Section 4 below, has an absolute bound
\[
                         C e^{N(s(u_\delta)-\epsilon_R)}
\tag{7}
\]
for all sufficiently large \(N\), at both parities. The constant is
uniform in \(\delta\). This is a bound for that segment, without a
claim about its subsequent taper or the remaining outer observation.

## 2. A lower bound for the selected original action

We integrate (1) first from \(0\) to the real angle \(\beta\), and then
vertically to \(\beta-iK\). This path lies in the whole original cubic
rectangle
\[
 |\Re u|\le\pi/2,\qquad |\Im u|\le1/2.
\tag{8}
\]
It is not required to lie on the selected charged curve. On all of
(8), cubic continuation, (13)--(15), gives
\[
 \Re c>3/4,\qquad 1/6<\Im c<1/3,\qquad
             |c|^2<127/144<(16/17)^2.
\tag{9}
\]
The last comparison is \(36703<36864\) after clearing denominators.
All returns below are the same principal analytic return as in (1).

For a real \(x\in[0,\beta]\), put \(w=c(x)\tan(x/2)\).
The inequalities in (9) give \(\Re(w^2)\ge0\). Therefore
\[
 \operatorname{arsinh}w
     =\int_0^1\frac{w}{\sqrt{1+t^2w^2}}\,dt,\qquad
 |\operatorname{arsinh}w|\le |w|
                       <\frac{16}{17}\tan(x/2)
\tag{10}
\]
away from the zero endpoint; there is no cut on the integration
segment and the denominator has modulus at least one. The real
action loss on this first path is consequently at most
\[
\begin{split}
 D_{\mathrm{real}}
 &<-\frac{32}{17\pi}\log\cos(\beta/2)
 \le\frac{32}{17\pi}\log(49/41)\\
 &<\frac{11520}{34153\pi}
 <\frac{3840}{34153}<\frac9{80}.
\end{split}
\tag{11}
\]
Here \(\cos(4/7)>1-(4/7)^2/2=41/49\), and the exact positive
series for the inverse hyperbolic tangent gives
\[
 \log(49/41)=2\operatorname{artanh}(4/45)
       <\frac{8/45}{1-16/2025}=\frac{360}{2009}.
\tag{12}
\]
The last two inequalities in (11) use \(\pi>3\) and
\(307200<307377\). At \(\beta=0\) the loss is zero, so the final
strict bound in (11) holds there too.

For the vertical path put \(u=\beta-iy\), \(0\le y\le K\), and
write
\[
 c=p+iq,\qquad \tan(u/2)=P-iQ,\qquad P,Q\ge0.
\]
One has
\[
 P=\frac{\sin\beta}{\cos\beta+\cosh y}
                              \le\tan(\beta/2).
\tag{13}
\]
When \(\beta>0\), the number \(w=c\tan(u/2)\) has positive real
part, and
\[
 \Re w=pP+qQ,\qquad \Im w=qP-pQ
                              <\frac13\tan(\beta/2).
\tag{14}
\]
If \(\Im w\le0\), its principal return has nonpositive imaginary
part and causes no downward action loss. If \(\Im w>0\), then
\[
               0<\frac{\Im w}{\Re w}\le\frac qp<\frac49<1.
\]
For a fixed \(X>0\) and \(0\le Y\le X\),
\(\Re(1+(X+iY)^2)\ge1\), and hence
\[
 \Im\operatorname{arsinh}(X+iY)
       =\int_0^Y\Re\{1+(X+iv)^2\}^{-1/2}\,dv\le Y.
\tag{15}
\]
Thus in both cases \(\Im\operatorname{arsinh}w\) is bounded above
by \(\tan(\beta/2)/3\). The sign in (1) gives exactly
\[
 \partial_y\Re S(\beta-iy)
          =-\pi^{-1}\Im\operatorname{arsinh}w .
\]
Using (2), (13)--(15), and the sine/cosine bounds at \(4/7\),
the total vertical loss is at most
\[
\begin{split}
 D_{\mathrm{vert}}
 &<\frac{K\tan(\beta/2)}{3\pi}
 \le\frac{2}{15\pi}\frac{28}{41}
   =\frac{56}{615\pi}\\
 &<\frac{56}{1845}<\frac{49}{1600}.
\end{split}
\tag{16}
\]
Indeed \(\tan(4/7)<(4/7)/(1-8/49)=28/41\), and the last
comparison is \(89600<90405\). Again the zero-charge case
has zero loss and satisfies the final strict inequality.

Combining (11),(16), with the original constant in (1), proves
\[
 s(u_\delta)>M_3-\frac9{80}-\frac{49}{1600}
             =M_3-\frac{229}{1600}
             >\frac{2651}{1600}.
\tag{17}
\]
This proves (4) without evaluating the selected root or action.

## 3. The endpoint sector on the enlarged first-angle interval

The original one-edge primitive extends with its unchanged constant
and principal return through \(0\le a\le2\pi/3,\ 0\le H\le1\).
This follows from
[positive horizontal phase continuation, Section 1](research_mixed_next_inner_three_positive_horizontal_phase_extension.md),
with the other angle set to zero. In particular
\[
 \psi_{tt}(t,0)=-\frac1{2\pi}\sec(t/2),\qquad
                         \psi(0,0)=2b_2,\quad b_2<7/12.
\tag{18}
\]
We explicitly extend the secant estimate in
[the complete-action bound, (9)--(15)](research_inner_three_complete_action_upper_bound.md),
whose original stated horizontal range stopped at \(\pi/2\).

Put \(c_0=\cos(a/2)\in[1/2,1]\), \(C=\cosh(H/2)\), and
\(s_0=\sinh(H/2)\). The same written positive-series bounds give
\(C<8/7\), \(s_0^2<15/49\), and
\[
                   \Re\sec((a-iH)/2)
                         =\frac{c_0C}{c_0^2+s_0^2}.
\tag{19}
\]
For fixed \(H\), the derivative with respect to \(c_0\) has the
sign of \(s_0^2-c_0^2\). Its only possible interior extremum is a
maximum, so the minimum is at an endpoint. At \(c_0=1\) it is
\(1/C>7/8\), while at \(c_0=1/2\) it is greater than
\[
           \frac{1/2}{1/4+15/49}=\frac{98}{109}>\frac78.
\tag{20}
\]
Thus \(\Re\sec(t/2)>7/8\) on the enlarged rectangle.

The original imaginary-axis estimate and zero real first derivative
at \(a=0\), followed by two horizontal integrations of (18)--(20),
now give on this whole rectangle
\[
 \Re\psi(a-iH,0)
       \le2b_2+\frac{H^2}{4\pi}-\frac{7a^2}{32\pi}
       <\frac76+\frac{H^2}{4\pi}-\frac{7a^2}{32\pi}.
\tag{21}
\]
No new primitive or logarithmic charge is introduced by this extension.

Substitute (21) and \(K<2/5\) into the literal endpoint rate in (5):
\[
 E_{\mathrm{end}}
 <\frac76+\frac{H^2}{4\pi}-\frac{7a^2}{32\pi}
                         +\frac{3aH}{2\pi}-\frac H2+\frac15.
\tag{22}
\]
For \(H\ge2/3\) the right side increases with \(a\) on the stated
interval. Its derivative is at least \(1/\pi-7/24>0\),
using \(\pi<22/7\). At \(a=2\pi/3\) it is also increasing in
\(H\ge0\); setting \(H=1\) bounds it above by
\[
 \frac{28}{15}+\frac1{4\pi}-\frac{7\pi}{72}
 <\frac{28}{15}+\frac2{25}-\frac{175}{576}
 =\frac{33}{20}-\frac{103}{14400}<\frac{33}{20}.
\tag{23}
\]
The strict middle comparison uses \(\pi>25/8\). Combining (23)
with (4) proves (5), including the claimed fixed \(1/200\) gap.

## 4. The complete actual-height finite segment

Here the finite source is exactly the two-short-edge source of
[the original trace transfer, (1) and (27)](research_mixed_next_inner_three_short_pair_source_transfer.md).
Retain
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad
 \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\quad
 U_N=\lfloor N/2\rfloor-1,\\
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u),\\
 g_N^{<<}(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)
                                      e^{3iNt^2/(4\pi)},\\
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered}
\tag{24}
\]
Define the original oriented segment contribution
\[
 \mathcal C_{N,R}^{(1)}(u_\delta)=
 -\frac{N^2C_{N,3}}{\pi i}
 \int_{\pi/2-iH_*(u_\delta)}^{2\pi/3-iH_*(u_\delta)}
                  g_N^{<<}(t,u_\delta)W_N(t)\,dt .
\tag{25}
\]
There is no replacement of the full denominator by a selected charge.

The [first-short-edge slit bound](research_mixed_next_first_short_edge_slit_plane_bound.md)
bounds its first edge at rate \(\Re\psi(t,0)+\tau\).
The complete
[right-edge upper envelope, (3)](research_mixed_next_selected_right_edge_upper_envelope.md)
bounds its second edge at
\(\max\{\Re\psi(t,u),(H+K)/2\}+\tau\).
Its proof retains both physical endpoint groups, both caps, every
Fourier correction, and the exact odd last index.

On (25), the exact denominator satisfies
\[
 |W_N(a-iH_*)|\le C e^{-NH_*},
\tag{26}
\]
uniformly at both parities, since \(H_*>2/3\). The remaining sine
and scalar factors are bounded. The two possible attached rates
are consequently the original geometric rate
\[
 \Re\Phi(t,u)=\Re\{\psi(t,0)+\psi(t,u)\}
                                  +3aH_*/(2\pi)-H_*
\]
and exactly \(E_{\mathrm{end}}\) from (5), with only the two
arbitrarily small source tolerances.

The geometric rate is paid by
[positive horizontal descent, (26)](research_mixed_next_inner_three_positive_horizontal_phase_extension.md):
\[
 \Re\Phi(a-iH_*,u_\delta)
       \le s(u_\delta)-\frac{(a-a_*)^2}{8\pi}
       \le s(u_\delta)-\frac{d_R^2}{8\pi}.
\tag{27}
\]
The maximum defining \(d_R\) exists and is strictly below \(\pi/2\)
by the compact selected family and the strict cubic guard (3).
The other rate is paid by (5).

Choose the two source tolerances sufficiently small relative to
the minimum in (6), then absorb the original \(N^2/\pi\) and
all fixed polynomial factors in the remaining reserve. Equations
(24)--(27) prove both (7) and the stronger absolute-integral version
\[
 \frac{N^2}{\pi}
 \int_{\pi/2}^{2\pi/3}
  |g_N^{<<}(a-iH_*,u_\delta)W_N(a-iH_*)|\,da
                \le C e^{N(s(u_\delta)-\epsilon_R)}.
\tag{28}
\]
This retains all higher angular charges, all original finite rows
in both shortened edges, and the original normalization.

Only the displayed segment is added to the paid contour inventory.
Neither an off-height taper from its right endpoint, a full complex
three-kernel packet, nor the remaining outer cancellation is inferred.
No derivative claim is made for a current with the moving real-valued
height \(H_*(u)\).

## Frozen source bindings

- Selected angle-depth correlation:
  49d0d81bb39dcdb8946893c8bc0b712e00b2eaad15b3f5476b62736fce1df1f4.
- Selected upper depth:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
- Original cubic and whole integration rectangle:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Original complete single-three action and normalization:
  7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c.
- Original one-edge action bound:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- Selected finite-source guards:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Original positive horizontal phase descent:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
- Complete shortened right-edge upper envelope:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
- First-short-edge slit-plane source:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Exact two-short-edge source and full trace multiplier:
  a835236285224a9df4ac41451c84882609b44b223eaa2c7c359f0f48518bccae.

