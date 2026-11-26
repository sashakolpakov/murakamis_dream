# The low right horizontal from an earlier angular cut

Private finite-source deduction, 9 November 2026. On the selected
charged curve, the original short-by-short inner integrand has rate
less than \(329/200\) on a fixed horizontal beginning before the
previous far region. This estimates the complete finite integrand,
with the original crossing and trace denominator.

No mathematical numerical evaluation, saved-value arithmetic or
frozen-source edit is used.

## 1. Source and statement

Keep the original selected curve \(u=u_\delta=\beta-iK\),
\(0\le\delta\le1/2\). The
[selected-depth theorem](research_mixed_next_selected_charged_depth_bound.md)
proves \(0\le K<2/5\). Put
\[
 h=\frac1{10},\qquad a_0=\arccos(-13/20),\qquad
 \gamma:\ a_0-ih\longrightarrow5\pi/6-ih .
 \tag{1}
\]
The inverse cosine in (1) is the real value in \((0,\pi)\).
Use exactly the finite source from
[the right far-region theorem, equation (1)](research_mixed_next_inner_three_right_far_region.md):
\[
\begin{gathered}
 U=\lfloor N/2\rfloor-1,\quad \eta_N=(-1)^{N-1},\quad
 C_{N,3}=\exp\!\left(\frac{3\pi i(N-1)^2}{4N}\right),\\
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 g_N^{<<}(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)
                                  e^{3iNt^2/(4\pi)},\\
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered}
\tag{2}
\]
All physical rows and both parity cutoffs are retained.

**Theorem.** Uniformly over the selected curve and both level
parities, for all sufficiently large \(N\),
\[
 \sup_{t\in\gamma}|g_N^{<<}(t,u)W_N(t)|
       +\frac{N^2}{\pi}\int_\gamma
                 |g_N^{<<}(t,u)W_N(t)|\,|dt|
                \le C e^{329N/200}.
 \tag{3}
\]
In particular, any separately proved selected action floor
\(s(u)>331/200\) makes this entire current smaller than the
inner action by \(1/100\). The proof of (3) does not assume
that action floor or any global quantum packet.

## 2. The calibrated complete-edge phase

The original closed primitive has
\[
 \psi(0,0)=2b_2,\qquad b_2<7/12,\qquad
 \psi_t(t,0)=-\pi^{-1}\operatorname{arsinh}\tan(t/2),\qquad
 \psi_{tt}(t,0)=-\frac{\sec(t/2)}{2\pi}.
 \tag{4}
\]
These are the unchanged constants and principal return in
[the complete-action bound, equations (2),(8),(17)](research_inner_three_complete_action_upper_bound.md)
and
[the positive phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md).
They hold on the compact angular domains used below.

For \(0\le v<\pi/2\),
\[
                    \sec v\ge1+\frac{v^2}{2}+\frac{5v^4}{24}.
 \tag{5}
\]
Here is a direct proof of the required polynomial inequality.
With \(y=\sec v\), one has \(y''=2y^3-y\), \(y(0)=1\),
and \(y'(0)=0\). Since \(y\ge1\), first \(y''\ge1\),
so \(y\ge1+v^2/2\). The function \(2y^3-y\) increases for
\(y\ge1\); substitution of this last bound gives
\(y''\ge1+(5/2)v^2\). Integration twice proves (5).

For real \(0\le a<\pi\), integration of (4)--(5) therefore yields
\[
 2\psi(a,0)
 \le4b_2-\frac{a^2}{2\pi}
                -\frac{a^4}{96\pi}-\frac{a^6}{2304\pi}.
 \tag{6}
\]
The first derivative at zero vanishes, so no affine term is missing.

The chosen cut obeys
\[
                         \frac94<a_0<\frac{3\pi}{4}.
 \tag{7}
\]
For the lower bound the alternating cosine series gives
\[
 \cos(9/4)\ge
 1-\frac{81}{32}+\frac{6561}{6144}
                   -\frac{531441}{2949120}
 =-\frac{1898001}{2949120}>-\frac{13}{20}.
 \tag{8}
\]
The last comparison has numerator difference \(18927>0\).
Cosine is decreasing on \([0,\pi]\).
For the upper bound use
\(\cos(3\pi/4)=-\sqrt2/2<-13/20\).

Using \(\pi<22/7\), (7) gives the three strict losses
\[
 \frac{a_0^2}{2\pi}>
        \frac{567}{704}>\frac{161}{200},\qquad
 \frac{a_0^4}{96\pi}>
        \frac{45927}{540672}>\frac{21}{250},\qquad
 \frac{a_0^6}{2304\pi}>\frac7{396}>\frac1{60}.
 \tag{9}
\]
For the last bound, \((9/4)^6>128\), since
\(531441>524288\). For the first two comparisons the positive
cross-product differences are respectively \(56\) and \(127638\).

The height change in the first edge has a small explicit cost.
Writing \(c=\cos(a/2)>0\), \(s=\sinh(v/2)\) and
\(C_v=\cosh(v/2)\), one has
\[
       \Re\sec((a-iv)/2)=\frac{cC_v}{c^2+s^2}\le\frac1c.
 \tag{10}
\]
Indeed \(c^2(C_v-1)\le(C_v-1)(C_v+1)=s^2\).
The first height derivative of the real phase vanishes at height
zero. Thus (4),(10) imply
\[
 2\Re\psi(a-ih,0)-2\psi(a,0)
                     \le\frac{h^2}{2\pi}\sec(a/2).
 \tag{11}
\]
At \(a=a_0\), (7) implies
\[
 \cos^2(a_0/2)>
 \cos^2(3\pi/8)=\frac{2-\sqrt2}{4}>
                    \frac17>\frac9{64}.
 \tag{12}
\]
Here \(\sqrt2<10/7\). Therefore (11) at \(h=1/10\) is
strictly less than \(1/(75\pi)<1/225\).

## 3. The complete rate decreases along the horizontal

The original slit-plane estimates supply the rate
\[
 R(a,u)=2\Re\psi(a-i/10,0)+\frac K2-\frac1{10}
                                      +\frac{3a}{20\pi}.
 \tag{13}
\]
The first two terms are the two complete shortened edges with the
outside-variable degree cost. The last two are the exact trace
penalty and crossing growth, respectively.

Since \(a_0>2\pi/3\), the original return comparison in
the positive phase extension, equations (17),(23), gives
\[
 \Re\operatorname{arsinh}\tan((a-i/10)/2)>19/20
                         \qquad(a_0\le a\le5\pi/6).
 \tag{14}
\]
For the inequality \(a_0>2\pi/3\), use
\(\cos a_0=-13/20<-1/2=\cos(2\pi/3)\).
Consequently
\[
                 R_a<-\frac7{4\pi}<0.
 \tag{15}
\]
It suffices to estimate (13) at \(a_0\).
Equations (4),(6),(9)--(12), \(K<2/5\), and
\(a_0<3\pi/4\) give
\[
\begin{split}
 R(a_0,u)
 &<\frac73-\frac{161}{200}-\frac{21}{250}-\frac1{60}
                     +\frac1{225}+\frac15+\frac1{80}\\
 &=\frac{33}{20}-\frac{97}{18000}
  =\frac{329}{200}-\frac7{18000}.
\end{split}
 \tag{16}
\]
In the crossing term we used
\(3a_0/(20\pi)-1/10<1/80\).
All inequalities are written rational or elementary function
comparisons on the original phase.

## 4. The finite current and its exact denominator

The compact set
\[
 \{-2\cos(a-i/10):a_0\le a\le5\pi/6\}
                          \subset\mathbb C\setminus[2,\infty)
 \tag{17}
\]
is eligible for
[the full slit-plane theorem, equations (18),(24)](research_mixed_next_first_short_edge_slit_plane_bound.md).
For any fixed \(\tau>0\) it gives, at both parities,
\[
\begin{split}
 |K_N^<(a-i/10,0)|
 &\le C_\tau e^{N(\Re\psi(a-i/10,0)+\tau)},\\
 |K_N^<(a-i/10,u)|
 &\le C_\tau e^{N(\Re\psi(a-i/10,0)+K/2+\tau)}.
\end{split}
 \tag{18}
\]
The second line bounds the full coherent kernel by interpolation
at every double physical node, followed by its exact degree-\(U\)
complex continuation. No new Newton truncation is made.

The original denominator satisfies
\[
 |W_N(a-i/10)|\le
        \frac{e^{-N/10}}{(1-e^{-N/10})^2}
                         \le C e^{-N/10}.
 \tag{19}
\]
This retains all angular sampling corrections. The sine in (2)
is bounded on the compact path, and the crossing has modulus
\(\exp(3Na/(20\pi))\). Combining (13),(16),(18),(19), with
\(\tau=7/72000\) for each edge, leaves rate at most
\[
                         \frac{329}{200}-\frac7{36000}.
 \tag{20}
\]
The path length is bounded independently of \(N,\delta\), and
\(|C_{N,3}|=1\). Absorbing the original factor \(N^2/\pi\)
into the remaining strict margin in (20) proves (3).

The theorem starts at \(a_0-i/10\). It does not bound the preceding
horizontal from \(2\pi/3-i/10\), the vertical descent to that point,
or the high horizontal from \(\pi/2-iH(u)\). Those segments require
their own finite-source and action comparisons. The previously
proved far-region theorem continues from the endpoint \(5\pi/6-i/10\).

## Frozen source bindings

- Selected depth:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
- Original complete-action constants and secant derivative:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- Original enlarged phase and return bound:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
- Complete slit-plane source:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.

