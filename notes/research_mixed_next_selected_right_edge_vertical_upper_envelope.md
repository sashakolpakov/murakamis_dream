# The selected shortened edge on the right vertical

Private finite-source theorem, 9 November 2026. The complete upper
envelope for the selected right edge extends down the vertical first
angle \(2\pi/3\), to first height \(1/10\). The real row need not be
claimed unimodal on this larger family: its original upward normal
derivative is strictly negative, which supplies the bottom-boundary
condition in the contour argument. Both physical endpoint groups,
external caps and complete Fourier corrections remain present.

No mathematical numerical evaluation, saved-value arithmetic or
frozen-source edit is used. No comparison with the inner critical
action is asserted.

## 1. Family and statement

Let \(u=u_\delta=\beta-iK\), \(0\le\delta\le1/2\), be the
original selected charged curve, and put
\[
 t=\frac{2\pi}{3}-iH,\qquad \frac1{10}\le H\le1.
 \tag{1}
\]
The adopted [selected cut guards](research_mixed_next_selected_right_edge_cut_guards.md)
give, for positive \(\delta\),
\[
 0<\beta<4/3,\qquad0<K<\min(\beta/2,1/2),\qquad
 |\cos u|<1,\quad\Re\cos u>7/30,\quad\Im\cos u>0.
 \tag{2}
\]
At \(\delta=0\), \(u=0\). Keep the literal ordinary source
\[
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u).
 \tag{3}
\]
Let \(\psi(t,u)\) denote the original calibrated zero-charge
edge phase. Its closed primitive on (1) is supplied by
[the positive phase extension, Section 1](research_mixed_next_inner_three_positive_horizontal_phase_extension.md).
Set
\[
 m=\Re\psi(t,u),\qquad e=\frac{H+K}{2},\qquad M=\max\{m,e\}.
 \tag{4}
\]

**Theorem.** For each fixed \(\tau>0\), uniformly on (1) at
both parities and all sufficiently large \(N\),
\[
                    |K_N^<(t,u)|\le C_\tau e^{N(M+\tau)}.
 \tag{5}
\]
The sum and phase in this statement are unchanged. This is an
absolute upper estimate, not a relative saddle packet.

## 2. The same cuts, simple root and original charge

Write
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad D_0=A+B-AB,
 \quad W=AB/D_0.
 \tag{6}
\]
Every cut calculation in Section 2 of the selected cut-guard
theorem used only \(1\le C=\cosh H<8/5\), together with
\(\cos(\Re t)\in[-1/2,0]\) and (2). It did not use
\(H\ge2/3\). In particular both original upper cuts
\[
 y=x+iH/(2\pi),\quad x\ge1/6,
 \qquad
 y=x+iK/(2\pi),\quad x\ge\frac12-\frac{\beta}{2\pi}
 \tag{7}
\]
have the full force bounds, respectively,
\[
 \mathfrak f(y):=
 \left|\frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
 {(1-\cos2\pi y)^2}\right|,\qquad
 \mathfrak f\le\sqrt{23/24}<1,\quad
 \mathfrak f\le\frac{13\sqrt{79}}{150}<1.
 \tag{8}
\]
This includes the first cut's negative real
coordinate part and both starting zeros. At \(u=0\) the second
cut has no open interior segment. The possible interchange of
the two cut heights does not change either calculation.

The elementary guards (20)--(21) of that theorem also used
only \(C<8/5\), not its lower height bound. Explicitly,
\[
 \Re A=\frac{1-C/2}{2}>\frac1{10},\qquad
 |A|=\frac{C-1/2}{2}<\frac45,
 \quad \Re B>\frac{37}{60},\quad |B|^2\le\Re B,
\]
\[
 |1-A|<\frac{21}{20},\quad |1-B|<\frac9{20},\quad
 \Re D_0>\frac{211}{400},\quad
 \Re(1/W)>\frac5{32}.
 \tag{9}
\]
Here \(\Im A>0\) since \(H\ge1/10\), while \(\Im B\ge0\).
Thus \(\Im(1/W)<0\), and \(W\) stays in a compact subset of
the upper right quadrant. The original algebraic critical point
\[
 y_* =\pi^{-1}\arctan\sqrt W
 \tag{10}
\]
stays a positive distance from the boundary of the upper half-strip.
Its force identity is
\[
 e^{F_y}-1=-\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
 \qquad z_y=\tan\pi y.
 \tag{11}
\]
It is the unique finite algebraic root in \(0<\Re y<1/2\).

For each \(u\), start at the original height \(H(u)>2/3\),
at first real angle \(2\pi/3\), where the selected cut-guard
theorem already fixes the charge and critical value. Vary \(H\)
to its value in (1). Equations (8)--(11) prevent the critical
point from crossing an original cut or zero. Its original
logarithmic derivative remains continuous and belongs to
\(2\pi i\mathbb Z\), so it remains zero. Continuation of the
same closed primitive gives
\[
 F_y(y_*)=0,\qquad F(y_*)=\psi(t,u),\qquad
 -F_{yy}(y_*)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0.
 \tag{12}
\]
No logarithmic reset or new phase constant enters this argument.

## 3. Bottom and side boundaries

Let \(\mathcal V=\mathfrak b(\,\cdot\,,t)+
\mathfrak b(\,\cdot\,,u)\) be the unchanged zero-safe
factorial envelope. The reflection proof of subharmonicity
and cut descent in [the upper-envelope theorem, Section 3](research_mixed_next_selected_right_edge_upper_envelope.md)
applies without change, using (8). The remaining bottom condition
has the following direct proof.

For a lower angular parameter \(z=\theta-iA_0\), its original
one-leg derivative on the open real wire has exponential
\[
 e^{b_y(x,z)}=\frac{\cos2\pi x+\cos z}{1-\cos2\pi x}.
 \tag{13}
\]
If \(0<\theta<\pi\), \(A_0>0\), its numerator has positive
imaginary part for every \(0<x<1/2\). Its logarithmic lift
in (13) is the principal argument in \((0,\pi)\). To verify
the lift, at \(x\downarrow0\) the original two shifted sine
logarithms give imaginary part
\(2\arg\cos(z/2)\in(0,\pi)\); the own sine is positive
on this real interval. The quotient never crosses the real axis
or zero as \(x\) increases, so that argument remains the
original one. This proof does not require \(\Re\cos z\ge0\).

Apply this to \(t\), and to \(u\) for \(\delta>0\). At
\(\delta=0\), the outgoing quotient is positive real on
the open wire and its original imaginary logarithm is zero.
There is no real interior numerator zero in either case.
The upper envelope agrees with the original regular phase in
a neighborhood above each such bottom point. Therefore
\[
 \partial_v\mathcal V(x+iv)\big|_{v=0+}
             =-\Im F_y(x)<0,
                         \qquad0<x<1/2.
 \tag{14}
\]
No point of the open bottom is a local minimum relative to the
closed upper rectangle. No real-row unimodality is needed.

The one-leg side identities (11)--(12) in the upper-envelope
theorem are valid for every \(r=\theta/(2\pi)<1/2\).
Here the incoming value is \(r=1/3\), and the outgoing
one is smaller. The left trace is strictly increasing from
zero. On the right, each leg decreases before its own cut
height and has derivative at least \(\pi\) afterwards.
Before a cut its derivative is strictly greater than
\(-\pi\) when its real angle is nonzero. Hence the summed
right trace decreases to \(\min(H,K)/(2\pi)\) and then
increases strictly; equal heights cause no exception. If
\(K=0\), the outgoing derivative is \(\pi\) above zero
and the increasing interval starts at zero. The endpoint
values remain
\[
             \mathcal V(0)=0,\qquad\mathcal V(1/2)=e.
 \tag{15}
\]
Every strict side sublevel is connected or empty.

At a sufficiently large fixed upper height,
\[
 \mathcal V(x+iv)=2\pi v-
       \frac{(2\pi/3)H+\beta K}{2\pi}+o(1)
 \tag{16}
\]
is above \(m+1\), uniformly in all parameters and the closed
wire interval. Apply the component/Jordan proof in the
upper-envelope theorem. Every strict-sublevel component
below \(m\) must have a minimum on a vertical side, by (8),
(14), harmonicity off the cuts and (16). There are at most
two components. The simple saddle (12) forces its two
descending sectors to lie in distinct components by the
subharmonic maximum principle on the resulting Jordan loop.
Thus there are exactly two, meeting different sides.

The left side connects to its real endpoint below \(m\).
The right decrease-then-increase trace connects to its real
endpoint at rate at most \(\max(m,e)\). Consequently, for
every fixed \(\varepsilon>0\), sufficiently small fixed real
cuts \(\alpha,\gamma\) admit an upper unweighted path from
\(\alpha\) to \(\gamma\) with
\[
                    \mathcal V\le M+\varepsilon.
 \tag{17}
\]
As in the cited finite-cover argument, these paths have uniform
length and height bounds after choosing finitely many parameter
charts. Small midpoint displacements are covered by the same
endpoint collars. No continuity of one global path choice is
required.

## 4. A deeper pair of complete alias paths

Both original penalized side bounds remain valid:
\[
 \mathcal V(\pm iv)-2\pi v
       \le D:=\frac{(2\pi/3)H+\beta K}{2\pi},
 \qquad
 \mathcal V(1/2\pm iv)-2\pi v\le e.
 \tag{18}
\]
They follow from the original sidewise reflection formulas,
whose only real-angle restriction is \(0\le\theta<\pi\).
The quantitative left reserve is now
\[
       D\le\frac H3+\frac K4,\qquad
       e-D\ge\frac H6+\frac K4\ge\frac1{60}.
 \tag{19}
\]

Use fixed wire height \(v=2\) for both deep alias horizontals.
The original \(J_\pm\) formulas in
[lower continuation, (15)--(20)](research_mixed_next_shortened_edge_lower_continuation.md)
give polynomial penalized part of absolute value at most \(D\).
All dilogarithm arguments have modulus at most
\[
                  e^{1-4\pi}<e^{-10}<1/10000.
 \tag{20}
\]
Indeed \(\pi>3\), and the written positive-series witness
\(e^5>100\) in that source gives \(e^{10}>10000\).
The sum of the absolute coefficients of the two legs' complete
remainders is \(4/\pi\). Thus their total error is less than
\[
             \frac4{9999\pi}<\frac1{600}.
 \tag{21}
\]
Equations (19)--(21) prove
\[
             \mathcal V(x\pm2i)-4\pi
                   < e-\frac3{200},\qquad0\le x\le1/2.
 \tag{22}
\]
All reflection terms and their original constants are included.

Uniform continuity on the compact side columns \(0\le v\le2\)
moves (18) to interior endpoint columns. Choose \(\alpha,\gamma\)
as in Section 3, a small fixed cap height \(h_c>0\), and
the original midpoints
\[
 \alpha_N=\frac{\lfloor N\alpha\rfloor+1/2}{N},\qquad
 \gamma_N=\frac{\lceil N\gamma\rceil-1/2}{N}.
 \tag{23}
\]
Both complete alias paths may be
\[
 \alpha_N\pm ih_c\longrightarrow\alpha_N\pm2i
 \longrightarrow\gamma_N\pm2i
 \longrightarrow\gamma_N\pm ih_c.
 \tag{24}
\]
Their penalized rates are at most \(e+\varepsilon\). The
unweighted endpoint collars and every physical row in the
two removed endpoint groups also have rate at most
\(e+\varepsilon\).

## 5. Exact finite assembly and scope

Keep the same canonical interpolation as the upper-envelope
theorem:
\[
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},
 \quad T_N=B_N(y,t)B_N(y,u).
 \tag{25}
\]
Its shifted real arguments still lie between \(-1/3\) and
\(5/6\). The original reciprocal reflection proves
holomorphy in \(0<\Re y<1/2\), at every finite height.
The uniform factorial theorem gives
\(|T_N|\le C N^{-2}e^{N\mathcal V}\) on the compact paths.
Its zero-safe endpoint extension gives the same exponential
rate with a polynomial prefactor for every physical
\(0\le j\le U_N\); the proof uses exactly
\(N|J(x+1/(2N))-J(x)|=O(\log N)\), \(0\le x\le1/2\).
Thus no endpoint row or odd cutoff has been replaced.

Set \(\zeta=e^{2\pi iNy}\). With both paths in (24) oriented
left to right, the unchanged exact residue identity is
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
 \tag{26}
\]
At midpoint columns, \(\zeta=-e^{-2\pi Nv}\), so the full
cap reciprocal has modulus at most one. Split
\((1-\zeta)^{-1}=1+\zeta/(1-\zeta)\) above the real line.
Move the entire unweighted term to (17). The two resulting
endpoint segments are exactly
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy
       +N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy.
 \tag{27}
\]
Both lie in the paid collars. On the remaining two paths
(24), the exact rational factors supply
\(e^{-2\pi N|\Im y|}\) with a uniformly bounded multiplier,
since \(|\Im y|\ge h_c\). Equations (17)--(27) therefore
give
\[
               |K_N^<(t,u)|\le C_\varepsilon N^A
                                          e^{N(M+\varepsilon)}.
 \tag{28}
\]
Taking \(\varepsilon<\tau/2\) and absorbing the polynomial
proves (5).

The complete source is now bounded on this right vertical.
To pay its contribution to the inner contour one still needs
an action comparison for both rates
\[
 \Re\psi(t,0)+\Re\psi(t,u),
 \qquad
 \Re\psi(t,0)+\frac{H+K}{2},
 \tag{29}
\]
because the original crossing-plus-trace rate
\(3(2\pi/3)H/(2\pi)-H\) vanishes on this vertical. Neither comparison is
proved here. The interval with first real angle greater
than \(2\pi/3\), a nonzero edge packet, and any full outer
observation remain outside this theorem.

## Frozen source bindings

- Selected cut and phase guards: `8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc`.
- Complete original upper envelope: `c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699`.
- Enlarged original closed phase: `a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c`.
- Upper component/Jordan proof: `b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542`.
- Exact joined representation: `1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d`.
- Original lower primitive and its complete remainder: `79a0e9fb0c9b8d22819cc0acbf4495664f2c6608ca6430bbde9a2c2c0732503c`.
- Uniform zero-safe factorial bounds: `4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11`.
