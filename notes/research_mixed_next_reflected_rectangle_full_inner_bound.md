# The full inner source on the reflected outgoing rectangle

Private finite-source upper theorem, 9 November 2026. Every part of
the original inner Hermite trace is estimated on the independent
upper outgoing rectangle. The result is an upper bound, with an
explicit alternative endpoint ceiling. No relative inner packet
on this rectangle is required or asserted.

No mathematical numerical evaluation, saved-value arithmetic,
or frozen-source edit is used.

## 1. Exact source and statement

Retain the original Newton polynomials, full Frobenius functional
\(\phi_N\), and crossing \(R_N\). Put
\[
\begin{gathered}
 D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
 \eta_N=(-1)^D,\quad C_{N,3}=e^{3\pi iD^2/(4N)},\\
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),\qquad
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 Q_N^{\rm sh}(u)=
 \phi_N^{(x)}[R_N(x)^3K_N^{\rm ord}(-2,x)
                              K_N^{<,\rm ord}(x,-2\cos u)],\\
 Q_N^{\rm full}(u)=P_{3,N}(0,u).
\end{gathered}
\tag{1}
\]
The first edge in the definition of \(Q_N^{\rm sh}\) is full.
Both sources retain the original complete inner Hermite trace,
including every first normal and the odd simple node.

Let
\[
 \mathcal R^\uparrow
 =\{u=\beta+iK:0\le\beta\le4/3,\quad0\le K\le2/5\}.
\tag{2}
\]
Use the original cubic branch and calibrated action
\[
\begin{gathered}
 t_*(u)=a_*(u)-iH(u),\qquad
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,\\
 S(u)=\Phi(t_*(u),u)=S_3(0,u),\qquad s(u)=\Re S(u).
\end{gathered}
\tag{3}
\]
They are holomorphic on a neighborhood of the larger original
rectangle \(|\Re u|\le\pi/2,\ |\Im u|\le1/2\).

**Theorem.** For every fixed \(\tau>0\), there is \(C_\tau\) such
that, uniformly on (2), through both level parities and all
sufficiently large \(N\),
\[
 \boxed{\quad
 |Q_N^{\rm sh}(u)|+|Q_N^{\rm full}(u)|
 \le C_\tau\exp N\{\max(s(u),17/10)+\tau\}.
 \quad}
\tag{4}
\]
The action and its complete constant in (4) are unchanged.
No complex-conjugation rule for the cubic crossing is used.

## 2. The original upper critical height and its ordering

Write \(C=\cos(u/2)\) and \(v=2\cos(t_*(u)/2)=x+ib\).
The [original cubic theorem](research_mixed_next_inner_three_cubic_continuation.md)
gives, on the entire complex rectangle containing (2),
\[
\begin{gathered}
 v^3-2iv^2-3v+2i-2C=0,\quad
 3/2<x<15/8,\quad1/3<b<2/3,\quad |v|^2<127/36<4,\\
                   0<a_*<\pi/2,\qquad0<H<1.
\end{gathered}
\tag{5}
\]
These are the original logarithmic branch, not a newly selected
cubic root.

In fact
\[
                            2/3<H(u)<1\qquad(u\in\mathcal R^\uparrow).
\tag{6}
\]
Indeed \(\Re C\ge\cos(2/3)>7/9\), and the real cubic equation gives
\[
 2\Re C=x(x^2-3b^2+4b-3)\le x(x^2-5/3).
\]
If \(x\le8/5\), its right side is at most
\(536/375<14/9\), a contradiction. Thus \(x>8/5\).
For fixed \(x\), the imaginary cubic polynomial
\[
 F_x(b)=(3b-2)x^2-b^3+2b^2-3b+2
\]
increases strictly on \([1/3,2/3]\). At \(b=1/2\),
\[
 F_x(1/2)=-x^2/2+7/8<-81/200.
\]
On the other hand,
\[
 2\Im C=-2\sin(\beta/2)\sinh(K/2)
       >-\frac43\,\frac{30}{149}
       =-\frac{40}{149}>-\frac{81}{200}.
\tag{7}
\]
Here \(\sinh(1/5)<30/149\) is its positive series bounded by
successive ratios \(1/150\). Since \(F_x(b)=2\Im C\), this
proves \(b>1/2\). If \(H\le2/3\), then
\[
 b=2\sin(a_*/2)\sinh(H/2)
 <\sqrt2\,\sinh(1/3)<\frac{180}{371}<\frac12,
\]
the original height contradiction. This proves (6).

We also need the actual ordering
\[
                   H(\beta+iK)\le H(\beta-iK).
\tag{8}
\]
The original derivative is
\[
 t_C=-\frac4{\sqrt{4-v^2}\,\Delta},\qquad
                        \Delta=3v^2-4iv-3.
\tag{9}
\]
On the convex original \(C\)-rectangle, (5) gives
\[
 \Re\Delta>19/4,\quad-15/4<\Im\Delta<0,\quad
 \Re(4-v^2)>0,\quad\Im(4-v^2)<0.
\]
The arguments of \(\Delta\) and the original
\(\sqrt{4-v^2}=2\sin(t_*/2)\) both belong to
\((-\pi/4,0)\). Their product therefore has positive real
part, and \(\Re t_C<0\). Along the vertical \(C\)-segment,
\(\partial_{\Im C}H=-\Re t_C>0\).
The two values \(C(\beta\pm iK)\) have the same real part
and opposite imaginary parts. This proves (8) without
changing the selected root or its logarithmic lift.

## 3. The signed central horizontal, with its finite source

On \(|\Re t|\le\pi/2,\ |\Im t|\le1,\ u\in\mathcal R^\uparrow\),
put
\[
 c=\cos(t/2),\quad C=\cos(u/2),\quad
 A=c^2,\quad B=C^2,\quad D_0=A+B-AB.
\]
The original signed primitive extends to this box. Here
\[
 |1-A|<4/5,\quad |1-B|<4/7,\quad |1-D_0|<16/35,
 \quad |\arg c|<1/2,\quad |\arg C|<6/35.
\tag{10}
\]
The last bound uses
\(\tan(2/3)<6/7\) and \(\tanh(1/5)<1/5\).
The exact return identities \(1+z_t^2=D_0/c^2\) and
\(1+z_u^2=D_0/C^2\), where
\(z_t=C\tan(t/2)\), \(z_u=c\tan(u/2)\), exclude the
principal inverse-hyperbolic-sine cuts: their arguments
stay strictly between \(-\pi\) and \(\pi\).
The roots and closed primitive therefore agree by continuation
with those in the [signed phase proof](research_mixed_next_inner_three_negative_horizontal_phase.md),
including its complete constant and its evenness in \(t\).

The original Hessian consequently remains
\[
 \Phi_{tt}=-\frac1{2\pi}
       \left(\frac1c+\frac{C}{c\sqrt{D_0}}\right)
                              +\frac{3i}{2\pi}.
\tag{11}
\]
One has \(\Re(1/c)>1/2\). Moreover
\[
 \left|\arg\frac{C}{c\sqrt{D_0}}\right|
 <\frac{47}{70}+\frac\pi4<\frac\pi2,
\]
using \(|\arg\sqrt{D_0}|<\pi/4\) and
\(47/70<3/4<\pi/4\). Thus
\[
 \Re\Phi_{tt}<-\frac1{4\pi},\qquad
 \Re\Phi(a-iH(u),u)
 \le s(u)-\frac{(a-a_*(u))^2}{8\pi},
                 \quad-\pi/2\le a\le\pi/2.
\tag{12}
\]
The derivative at \(a_*(u)\) is zero on the original charge-one
sheet. No reflection of the crossing is involved.

For every fixed \(0<\eta\le |a|\le\pi/2\), the needed finite
second-edge estimate follows from
[the complete mixed-height theorem](research_mixed_next_shortened_edge_mixed_height_packet.md).
Its lower outgoing partner is \(\bar u=\beta-iK\).
By (8), both signed first heights \(\pm H(u)\) lie in that
theorem's allowed interval
\([-H(\bar u),H(\bar u)]\).
At positive \(a\), simultaneous bare-kernel conjugation gives
\[
 K_N^<(a-iH,u)=\overline{K_N^<(a+iH,\bar u)}.
\tag{13}
\]
At negative \(a\), use angular evenness first and then the
same conjugation. The edge primitive has the corresponding
joint Schwarz symmetry, calibrated by its real complete
constant. Thus both finite edge bounds have the original
rate \(\Re\psi(a-iH,u)\), including all edge aliases, caps,
physical rows, and the exact cutoff \(U\).

The [short-pair transfer, equations (10)--(11)](research_mixed_next_inner_three_short_pair_source_transfer.md)
separately gives the first-short/full comparison on this signed
first-angle box, independently of \(u\).
Consequently the entire short-by-short integrand on
\(\eta\le|a|\le\pi/2\) has the upper rate in (12), with
only polynomial factors. The exact multiplier
\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}
\tag{14}
\]
satisfies \(|W_N(a-iH)|\le C e^{-NH}\), uniformly by (6).
This retains all angular trace charges.

For completeness the interval \(|a|\le\eta\) is controlled
by the actual polynomial center argument, not by assuming
an edge packet at \(a=0\). Put \(a_0=\min a_*(u)>0\) and
\(\epsilon_0=a_0^2/(32\pi)\). Choose fixed \(A<a_0/2\)
with \(\log(1+\tan^2(A/2))<\epsilon_0/8\).
On \(\eta\le a\le A\), (12)--(13) bound the exact product
\(F_N(-2\cos(a-iH),u)\) by
\[
 CN^B e^{N(s-\epsilon_0+H)},\qquad \deg_x F_N\le2U<N.
\tag{15}
\]
With \(x=\tan(a/2)\), multiply by \((1+x^2)^{2U}\).
The result is a polynomial of degree at most \(4U<2N\)
in \(x\), using the exact identity
\[
 -2\cos(a-iH)=-2
 \frac{\cosh H(1-x^2)+2i\sinh H\,x}{1+x^2}.
\]
The [center proof](research_mixed_next_inner_three_center_bridge.md)
applies with these smaller degrees. Its affine Chebyshev
continuation costs \(2N\rho_\eta\), where
\[
 \rho_\eta=\operatorname{arcosh}
       \left(1+\frac{4\tan(\eta/2)}
                         {\tan(A/2)-\tan(\eta/2)}\right).
\]
Choose fixed \(\eta>0\) so that
\(2\rho_\eta<\epsilon_0/8\) and
\(3\eta/(2\pi)<\epsilon_0/8\).
The denominator (14) cancels the \(NH\) in (15); the
crossing costs at most \(3N\eta/(2\pi)\).
After polynomial absorption the center has rate at most
\(s-\epsilon_0/2\). This argument keeps the odd central
physical contribution inside the original lower contour.
Together these estimates bound the whole signed horizontal
by a polynomial times \(e^{Ns}\). No local Gaussian is
extracted or approximated in this upper-bound argument.

## 4. The complete right middle path

Set \(h_0=1/10\), \(a_1=\arccos(-3/5)\). Use
\[
 \pi/2-iH\longrightarrow2\pi/3-iH
 \longrightarrow2\pi/3-ih_0
 \longrightarrow a_1-ih_0.
\tag{16}
\]
Equation (6) places every point on the three precise families
of the [reflected edge-envelope theorem](research_mixed_next_reflected_rectangle_edge_envelope.md).
Combining its complete finite bound with the first-short
slit-plane bound and (14) leaves the two attached rates
\[
 \Re\Phi(t,u),\qquad
 E(a,H,K)=\Re\psi(a-iH,0)+\frac K2-\frac H2+
                                     \frac{3aH}{2\pi}.
\tag{17}
\]
Both retain the original trace charge and crossing.

For the first rate, the original Hessian calculation extends
to \(\pi/2\le a\le2\pi/3\):
\[
 |1-D_0|<(21/20)(17/40)=357/800<1/2,\quad
 |\arg\sqrt{D_0}|<\pi/12,\quad
 0\le\arg c<\pi/4,\quad|\arg C|<\pi/12.
\]
Hence \(\Re(C/(c\sqrt{D_0}))>0\), and (11)--(12)
continue through \(a=2\pi/3\).
The original mixed branch in (13) and the reflected edge's
charge calibration identify these same derivatives.
The high horizontal therefore has rate at most \(s(u)\).
At fixed \(a=2\pi/3\) the rate is convex in \(H\).

Here is an absolute bound for its low endpoint
\(t_0=2\pi/3-i/10\). The existing first-edge bound gives
\[
                2\Re\psi(t_0,0)<19/12+1/300.
\tag{18}
\]
For the second edge along the real outgoing interval,
\(\Re\psi(t_0,\beta)\le\Re\psi(t_0,0)\).
At real \(\beta\), its initial upward-height derivative is
at most \(\arg c/\pi<1/(10\pi)\): the original principal
return satisfies
\(\Im\operatorname{arsinh}(c\tan(\beta/2))\le\arg c\),
and
\(\tan(\arg c)=\sqrt3\tanh(1/20)<7/80<1/10\).
Throughout the vertical outgoing segment,
\[
 |c|<13/25,\quad |C|>3/4,\quad \Re D_0>443/800>1/2,
 \qquad
 |\psi_{uu}|=\left|\frac{c}{2\pi C\sqrt{D_0}}\right|
                                      <\frac1{2\pi}.
\tag{19}
\]
The last comparison follows from
\(32\cdot169<9\cdot625\).
The derivative branch is the one just calibrated above.
Integrating up to \(K\le2/5\) gives the increase
\[
             \frac{K}{10\pi}+\frac{K^2}{4\pi}
                       \le\frac2{25\pi}<\frac2{75}.
\]
The crossing-plus-charge rate is zero at \(t_0\).
Consequently
\[
                 \Re\Phi(t_0,u)<\frac{121}{75}<\frac{17}{10}.
\tag{20}
\]
Convexity now bounds the whole vertical in (16) by
\(\max(s(u),121/75)\).

For the second rate in (17), the independent first-edge
calculation in
[endpoint payment, Section 2](research_mixed_next_selected_action_floor_and_endpoint_payment.md)
gives \(E<33/20\) when \(a\le2\pi/3\),
\(2/3\le H\le1\), \(K\le2/5\). It depends on no outgoing
phase or sign. On the vertical, \(E_H>0\), so its maximum
is at the already controlled height \(H(u)\).

Along the low horizontal in (16), both rates decrease.
The original first return has
\(\Re\operatorname{arsinh}\tan(t/2)>19/20\).
The second return has positive real part. Indeed, writing
\(\tan(t/2)=P-iQ\), \(C=P_c-iQ_c\), one has
\[
 \frac QP=\frac{\sinh(1/10)}{\sin a}
 <\frac{101}{800},\qquad
 \frac{Q_c}{P_c}<\frac6{35},
\]
so \(\Re(C\tan(t/2))>0\).
Thus \(\partial_a\Re\Phi<-4/(5\pi)\), while
\(\partial_aE<-4/(5\pi)\) as well.
All these are original principal returns; the reflected
edge proof supplies their continued charge on this path.
The complete finite current on (16) is therefore bounded
at rate \(\max(s(u),17/10)\), with arbitrarily small
fixed allowance for its polynomial factors.

## 5. The left connection and the far right tail

Use the unchanged far midpoint and endpoint height
\[
 T_N=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N},\qquad
       0<h_c\le1/2000,\qquad e^{iNT_N}=-\eta_N.
\tag{21}
\]
For large \(N\), \(a_F=\pi-\pi/2000\le T_N\le
\pi-\pi/4000<\pi\). All first angles below lie in a
fixed compact subset of the original slit domain.

The full-period [first-short slit theorem](research_mixed_next_first_short_edge_slit_plane_bound.md)
gives, for either outgoing height sign, the product ceiling
\[
 2\Re\psi(a-ih,0)+K/2
\tag{22}
\]
up to an arbitrarily small fixed allowance. Its degree-\(U\)
outside continuation is an estimate of the exact finite
polynomial. At negative traced angle use real-coefficient
conjugation and angular evenness only for the two bare kernels.

Choose the left connection
\[
            -T_N-ih_c\longrightarrow-T_N-iH
                              \longrightarrow-\pi/2-iH.
\tag{23}
\]
The horizontal attached rate is
\[
 L(a,H,K)=2\Re\psi(a-iH,0)+K/2-H-3aH/(2\pi),
                                               \quad a\ge\pi/2.
\]
It decreases with \(a\). The original complete-action
upper proof, equation (15), yields at \(a=\pi/2\)
\[
 L\le\frac73+\frac{H^2}{2\pi}-\frac{7\pi}{64}
                                      +\frac15-\frac{7H}{4}.
\tag{24}
\]
The right side decreases for \(2/5\le H\le1\). Using
\(H>2/3>2/5\) and \(\pi>3\), it is strictly less than
\[
             \frac{11}{6}+\frac2{75}-\frac{21}{64}
                                      <\frac85.
\tag{25}
\]
For the last comparison, \(7/30+2/75=13/50<21/64\).
On the entire negative far vertical the rate decreases
as the downward height increases, since
\(\partial_h\Re\psi(a-ih,0)<1/2\). Its ceiling is
\[
                    2\psi(T_N,0)+K/2<1/100+1/5.
\tag{26}
\]
The first term is the exact small real-end estimate in
[the original left connector, equations (25)--(27)](research_mixed_next_inner_three_left_connector.md).
The midpoint denominator is bounded even at height zero;
no pole estimate is suppressed here.

For the right low tail \(a_1-i/10\to T_N-i/10\), the
full attached slit rate is
\[
 R(a,K)=2\Re\psi(a-i/10,0)+K/2+3a/(20\pi)-1/10.
\tag{27}
\]
The written first-edge calculation in
[the positive-rectangle proof, equations (23)--(27)](research_mixed_next_positive_rectangle_inner_packet.md)
depends only on \(K=|\Im u|\). It gives
\[
                  R(a_1,K)<1217/720<17/10.
\tag{28}
\]
In detail, \(a_1>11/5\), and the quadratic, quartic and
sextic real losses exceed \(77/100,3/40,3/200\);
the height cost is below \(1/225\) and the net crossing
cost below \(1/80\). Their exact sum is \(1217/720\).
The same first return has real part greater than \(19/20\)
for every \(a\ge a_1\), so \(R_a<-7/(4\pi)\) all the
way to \(T_N\). This uses the slit estimate on a fixed
compact ending strictly below \(\pi\).

Finally join \(T_N-i/10\) to \(T_N-ih_c\).
The exact half-grid denominator obeys
\(|W_N(T_N-ih)|\le e^{-Nh}\) for \(h\ge0\).
Using \(2\Re\psi(T_N-ih,0)\le2\psi(T_N,0)+h\),
the whole joining vertical has rate at most
\[
                    \frac1{100}+\frac15+\frac3{20}
                                =\frac9{25}<17/10.
\tag{29}
\]
Thus (23) and every remaining far right part are bounded
with strict absolute reserves below \(17/10\).

## 6. Exact full-trace assembly and both restorations

Write
\[
\begin{gathered}
 f_N(t,u)=K_N^<(t,0)K_N^<(t,u),\qquad
 g_N(t,u)=\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)},\\
 Q_N^{<<}(u)=\phi_N[R_N^3 f_N(\,\cdot\,,u)],\qquad
 \tau_j=2\pi(D/2-j)/N.
\end{gathered}
\]
The exact complete trace, with its original orientation, is
\[
\begin{split}
 Q_N^{<<}(u)
 ={}&-\frac{N^2C_{N,3}}{\pi i}\int_{\Gamma_N}g_N(t,u)W_N(t)\,dt\\
 &+\frac{\eta_NN^2C_{N,3}}{\pi}
   \int_{-h_c}^{h_c}\frac{g_N(T_N+iv,u)}
                                  {4\cosh^2(Nv/2)}\,dv
   +\eta_NC_{N,3}
       \sum_{|\tau_j|\ge T_N}\partial_tg_N(\tau_j,u).
\end{split}
\tag{30}
\]
Choose \(\Gamma_N\) by concatenating (23), the full signed
horizontal of Section 3, the path (16), the low tail (27),
and the final vertical in (29). It lies strictly in the lower
half-plane. All deformations there preserve (30), since every
sampling pole is real.

The two last terms of (30) are already bounded absolutely
by the source proof in
[short-pair transfer, Section 5](research_mixed_next_inner_three_short_pair_source_transfer.md).
Before its lower-outgoing action comparison, that proof uses only
\(|\Im u|\le1/2\). Its literal far derivative sum and complete
small vertical have rate at most
\[
 \frac{18763}{15000}+\frac1{2000}<\frac{17}{10}.
\tag{31}
\]
The degree \(2U<N\), Markov control of the first normals,
both halves of the midpoint vertical, and every removed
physical sample are retained. The odd central sample
was never part of this removed far set; it remains in (30).

Likewise [first-edge tail contraction, Theorem (3)](research_mixed_next_inner_three_first_edge_tail_contraction.md)
states the absolute, two-sign estimate
\[
 |Q_N^{\rm sh}(u)-Q_N^{<<}(u)|
        \le CN^A e^{N(b_2+2/3)},\qquad b_2<7/12.
\tag{32}
\]
Its proof includes the odd middle row and the odd simple
node with their exact coefficients. We use (32) itself,
not its later relative-action corollary restricted to
lower outgoing angles.

Sections 3--5 bound the entire integral in (30), including
its original \(N^2/(\pi i)\), at the rate on the right
of (4). Choose the finitely many fixed slit and edge
tolerances sufficiently smaller than \(\tau\), and absorb
all remaining fixed powers of \(N\) in the unused allowance.
Equations (30)--(32) prove (4) for \(Q_N^{\rm sh}\).

The independent [full outgoing-tail restoration theorem](research_mixed_next_outgoing_tail_trace_restoration.md)
then gives on (2)
\[
 |Q_N^{\rm full}(u)-Q_N^{\rm sh}(u)|
       \le CN^A e^{N(2b_2+K)}
       \le CN^A e^{47N/30}.
\tag{33}
\]
Since \(47/30<17/10\), it proves the full-source assertion
as well. This is a proved trace estimate, not an off-grid
algebraic identification of two different kernels.

Every original current and both trace corrections have now
been included. The conclusion is the upper envelope (4);
no nonzero leading coefficient, normalized relative error,
or derivative estimate for such a relative packet is inferred.
Attaching this envelope to a subsequent outer contour requires
that contour's own exact scalar, multiplier, and action comparison.

## Frozen source bindings

- Original full cubic branch and calibration:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Signed primitive:
  fd3f89e30e108e1b9911d0bcb55f0948b41b2c91ffa3aadefa894ea4224fd347.
- Complete mixed-height edge:
  fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07.
- Reflected three-path finite edge envelope:
  aa6af497469b294d545afad67e4364221c29eae0353ab9abfc949eadab27aaee.
- Exact short-pair source and all far normals:
  a835236285224a9df4ac41451c84882609b44b223eaa2c7c359f0f48518bccae.
- Original polynomial center:
  0ddff6c7a588128a32f862e113f4e8253d9da6f3e56a4fc3bc5955cab02f7097.
- Whole-period first-short slit source:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Original first-edge upper action and height bounds:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- Complete first-edge and enlarged positive phase:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
- Original low vertical first-edge estimate:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.
- Independent endpoint-sector bound:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Earlier low slit tail:
  a1520474da2d389cb9cf67e92618f6ca9c552d499f35a039e842f9fc4e5075eb.
- Original left slit connector:
  0981672faffc8d4cb94848a59ce01eeeb9627110e05fed16a2664ba8c27f930f.
- Absolute first-edge trace tail:
  b31ac2d1cbf5f0e3ab4b71b36af9718151bced51e6959ee32b26ccf7fac5dfe6.
- Absolute full outgoing restoration:
  8b30fb2a8258d49fd8c162d5822c4652129ffc5a39ee77019e1b00aa2db7596e.
