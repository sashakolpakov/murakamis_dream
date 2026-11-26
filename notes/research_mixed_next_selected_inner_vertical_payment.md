# Paying the selected inner right vertical

Private finite-source deduction, 9 November 2026. The original
shortened-kernel current on the vertical first angle \(2\pi/3\)
has a fixed exponential gap below the selected inner action.
The geometric sector is controlled by convexity between its
two endpoints. The physical endpoint sector is controlled by
monotonicity in the first height. Both sectors retain the
complete finite source.

No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used.

## 1. Source, path and statement

Use the selected \(u=u_\delta=\beta-iK\), \(0\le\delta\le1/2\),
and its original inner critical point
\[
 t_*(u)=a_*(u)-iH_*(u),\qquad
 S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u),
\]
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it.
\tag{1}
\]
All primitives and constants are those in
[the original positive phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md).
The selected guards and
[angle-depth correlation](research_mixed_next_selected_charged_angle_depth_correlation.md)
give
\[
 0\le\beta<8/7,\qquad 0\le K<2/5,\qquad
 K<\beta/2\ \ (\delta>0),\qquad
 2/3<H_*<1,\qquad 0<a_*<\pi/2.
\tag{2}
\]

Keep the literal source from
[the one-remaining-current assembly](research_mixed_next_inner_three_single_remaining_current.md):
\[
\begin{gathered}
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u),\\
 g_N^{<<}(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)
                              e^{3iNt^2/(4\pi)},\\
 \eta_N=(-1)^{N-1},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\qquad
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)} .
\end{gathered}
\tag{3}
\]
The vertical is oriented upwards:
\[
 \gamma_V(u):\quad
 \frac{2\pi}{3}-iH_*(u)
             \longrightarrow\frac{2\pi}{3}-\frac{i}{10}.
\tag{4}
\]

**Theorem.** At both parities and all sufficiently large \(N\),
uniformly in \(0\le\delta\le1/2\),
\[
 \left|-\frac{N^2C_{N,3}}{\pi i}
       \int_{\gamma_V(u)}g_N^{<<}(t,u)W_N(t)\,dt\right|
                  \le C e^{N(s(u)-1/1000)} .
\tag{5}
\]
This is one part of the unchanged remaining current. It neither
changes the first-edge trace deletion nor estimates a current with
the full first kernel pointwise.

## 2. A direct low-height geometric bound

Put \(a=2\pi/3\), \(h_0=1/10\), and \(t_0=a-ih_0\).
We prove
\[
                        \Re\Phi(t_0,u)<\frac85 .
\tag{6}
\]

First consider the real first edge. Its exact primitive satisfies
\[
 \psi(0,0)=2b_2,\qquad
 \partial_a\psi(a,0)
                 =-\frac1\pi\operatorname{arsinh}\tan(a/2).
\tag{7}
\]
The original complete-edge normalization and elementary
\(b_2<7/12\) bound are those in
[the complete action bound](research_inner_three_complete_action_upper_bound.md).
For \(0\le x<\pi/2\), the identity
\(\sec''x=\sec x(\tan^2x+\sec^2x)\ge1\) gives
\(\sec x\ge1+x^2/2\). Since
\[
 \frac{d}{dv}\operatorname{arsinh}\tan(v/2)=\frac12\sec(v/2),
\]
two integrations of (7) yield
\[
 2\psi(a,0)\le
       4b_2-\frac{a^2}{2\pi}-\frac{a^4}{96\pi}.
\tag{8}
\]
At \(a=2\pi/3\), use \(\pi>25/8\) in the quadratic term
and \(\pi>3\) in the quartic term. Then
\[
 2\psi(2\pi/3,0)
       <\frac73-\frac{25}{36}-\frac1{18}
        =\frac{19}{12}.
\tag{9}
\]

Raising the first depth from zero to \(h_0\) costs at most
\(h_0^2/\pi\) for two copies of this first edge. Indeed
\[
 \partial_h^2\Re\psi(a-ih,0)
                    =\frac1{2\pi}\Re\sec((a-ih)/2).
\]
At \(a=2\pi/3\), writing \(r=\sinh(h/2)\), one has
\[
 \Re\sec((a-ih)/2)
             =\frac{\frac12\sqrt{1+r^2}}{\frac14+r^2}\le2.
\tag{10}
\]
The last inequality follows by squaring
\(\sqrt{1+r^2}\le1+4r^2\). The first height derivative
vanishes at zero by the original real Schwarz symmetry.
Consequently
\[
                 2\Re\psi(t_0,0)
                    <\frac{19}{12}+\frac1{300}.
\tag{11}
\]

We next compare the outgoing edge with this first edge.
On the real output segment \(0\le v\le\beta\),
\[
 \psi_u(t_0,v)
  =-\frac1\pi\operatorname{arsinh}
                    \{\cos(t_0/2)\tan(v/2)\}
\]
has nonpositive real part, since \(\cos(t_0/2)\) lies in
the first quadrant and the original return is principal.
Thus
\[
                   \Re\psi(t_0,\beta)\le\Re\psi(t_0,0).
\tag{12}
\]
Its initial outgoing-height derivative at \(u=\beta\) is
nonpositive as well: it is the negative imaginary part
of that principal return, divided by \(\pi\).

Along \(u=\beta-ik\), \(0\le k\le K\), put
\[
 c=\cos(t_0/2),\quad C=\cos(u/2),\quad
 A=c^2,\quad B=C^2,\quad D=A+B-AB.
\tag{13}
\]
The already proved \(k\le K<\beta/2\) gives
\(|\cos(\beta-ik)|\le1\), by the same sine/hyperbolic-sine
comparison in the selected cut guards. Hence \(\Re B\le1\).
Also
\[
 \Re B\ge\cos^2(\beta/2)>
              (41/49)^2,\qquad \Im B\ge0,\qquad
 \Re A>0,\quad\Im A>0.
\tag{14}
\]
Here \(\cos(4/7)>1-8/49=41/49\). It follows directly that
\[
 \Re D=\Re B+\Re A(1-\Re B)+\Im A\Im B
                         \ge\Re B>(41/49)^2.
\tag{15}
\]
Moreover
\[
 |c|^2=\frac14+\sinh^2(1/20)
        <\frac14+\frac1{19^2}<\frac{13^2}{25^2}.
\tag{16}
\]
For example \(\sinh(1/20)\le120/2399<1/19\) follows
from its positive series; the last squared comparison is
\(228125<244036\).
The original second derivative, with the root fixed by
the positive phase extension, is
\[
 \psi_{uu}(t_0,u)=-\frac{c}{2\pi C\sqrt D}.
\]
Equations (14)--(16) therefore give
\[
 |\psi_{uu}(t_0,u)|
    <\frac{31213}{84050\pi}<\frac{2}{5\pi}.
\tag{17}
\]
The final rational comparison is \(156065<168100\).
Starting from the nonpositive height derivative in (12),
integration of (17) yields
\[
 \Re\psi(t_0,\beta-iK)
 \le\Re\psi(t_0,\beta)+\frac{K^2}{5\pi}
 <\Re\psi(t_0,0)+\frac4{375}.
\tag{18}
\]
At \(a=2\pi/3\), the real crossing/charge contribution
\(3ah_0/(2\pi)-h_0\) is exactly zero. Thus (11),(18) imply
\[
 \Re\Phi(t_0,u)
 <\frac{19}{12}+\frac1{300}+\frac4{375}<\frac85,
\tag{19}
\]
where the last gap is \(1/375\). The case \(u=0\) follows
directly from (11), and is also the continuous limit.

## 3. Paying both sectors along the full vertical

The [selected action-sector theorem](research_mixed_next_selected_action_floor_and_endpoint_payment.md)
supplies
\[
 s(u)>\frac{331}{200},\qquad
 E_{\rm end}(a,H_*,u)<s(u)-\frac1{200}
       \quad\left(\frac\pi2\le a\le\frac{2\pi}{3}\right),
\tag{20}
\]
where
\[
 E_{\rm end}(a,h,u)=
 \Re\psi(a-ih,0)+\frac{h+K}{2}
                       +\frac{3ah}{2\pi}-h.
\tag{21}
\]

At the upper first height \(H_*\), the original horizontal
concavity gives
\[
 \Re\Phi(2\pi/3-iH_*,u)
 <s(u)-\frac{(2\pi/3-a_*)^2}{8\pi}
 <s(u)-\frac{\pi}{288}
 <s(u)-\frac1{100}.
\tag{22}
\]
Here \(a_*<\pi/2\) and \(\pi>3\).
At the lower height, (6),(20) give a gap greater than
\(11/200\). The same original phase theorem proves
\[
 \frac{d^2}{dh^2}\Re\Phi(2\pi/3-ih,u)
                   =-\Re\Phi_{tt}(2\pi/3-ih,u)>0.
\tag{23}
\]
A convex function on a closed interval is bounded above
by the larger endpoint value. Therefore the geometric
sector has a gap \(1/100\) throughout (4).

For the endpoint sector, at \(a=2\pi/3\),
\[
 E_{\rm end}(a,h,u)=\Re\psi(a-ih,0)+\frac h2+\frac K2.
\]
The principal \(\operatorname{arsinh}\tan((a-ih)/2)\)
has negative imaginary part when \(h>0\). Equation (7)
therefore shows that this expression increases strictly
with \(h\). Its maximum on (4) is the already paid
height \(H_*\) in (20). Combining the two sectors gives
\[
 \Re\psi(t,0)+
 \max\{\Re\psi(t,u),(h+K)/2\}
             +\frac{3ah}{2\pi}-h
                     <s(u)-\frac1{200}
\tag{24}
\]
everywhere on (4).

## 4. The literal finite current

The first shortened kernel obeys
\[
 |K_N^<(t,0)|
          \le C_\tau e^{N(\Re\psi(t,0)+\tau)}
\]
on the fixed vertical compact, by
[the all-row slit theorem](research_mixed_next_first_short_edge_slit_plane_bound.md).
Indeed \(-2\cos t\) stays in its fixed slit domain.
The second shortened kernel obeys the complete envelope
\[
 |K_N^<(t,u)|
 \le C_\tau
   e^{N(\max\{\Re\psi(t,u),(h+K)/2\}+\tau)}
\tag{25}
\]
by [the finite vertical-edge theorem](research_mixed_next_selected_right_edge_vertical_upper_envelope.md).
That estimate retains every row, both physical endpoint
groups, original wire currents, caps and aliases.

For every \(t\) on (4), \(h\ge1/10\), and the complete
angular multiplier satisfies
\[
 |W_N(t)|\le
       \frac{e^{-Nh}}{(1-e^{-N/10})^2}.
\tag{26}
\]
There is no angular Fourier truncation here.
The crossing exponential has modulus
\(e^{3Nah/(2\pi)}\). Equations (24)--(26), the uniformly
bounded sine and path length, and the literal \(N^2/\pi\)
factor in (5) prove that current bound after taking, for
example, \(\tau=1/10000\), and absorbing the remaining
polynomial factor with a fixed fraction of the gap.
This proves (5), with the original upward orientation,
unchanged \(C_{N,3}\), and both parities.

Only the vertical current (4) has been paid. The low
horizontal connection to the far endpoint remains a
separate source estimate.

## Frozen source bindings

- Original single-current assembly:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
- Selected angle-depth correlation:
  49d0d81bb39dcdb8946893c8bc0b712e00b2eaad15b3f5476b62736fce1df1f4.
- Selected action and endpoint-sector payment:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Original positive phase extension:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
- Complete first-action upper bounds:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- All-row first-short slit theorem:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Complete vertical-edge upper envelope:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.

