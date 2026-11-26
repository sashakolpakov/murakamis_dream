# A complete inner majorant on the remaining physical outgoing half-period

Private finite-source theorem, 8 November 2026. A single contour
at the original critical height for outgoing angle \(\pi/2\)
bounds the complete inner three-trace at every physical outgoing
angle at least \(\pi/2\). The second shortened edge is an exact
physical row. Monotonicity of its calibrated slit-plane profile
gives a strict outgoing-angle improvement without continuing
the critical point to these new angles.

This is an absolute upper bound, not a nonzero packet or an
estimate of the subsequent outer signed observation. No
mathematical numerical evaluation or frozen-source edit is used.

## 1. Original source and statement

Retain the definitions of
[the physical outgoing packet](research_mixed_next_inner_three_physical_outgoing_packet.md):
\[
\begin{gathered}
D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\quad
q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
c_j=2\cos((2j+1)\pi/N),\qquad
u_{j,N}=\pi-(2j+1)\pi/N,\qquad c_j=-2\cos u_{j,N},\\
K_N^<(t,u)=\sum_{k=0}^{U}e_k(-2\cos t)e_k(-2\cos u),\\
Q_N(u)=\phi_N^{(x)}
 \left[R_N(x)^3K_N^{\mathrm{ord}}(-2,x)
                  K_N^{<,\mathrm{ord}}(x,-2\cos u)\right],\\
Q_N^{<<}(u)=\phi_N^{(x)}
 \left[R_N(x)^3K_N^{<,\mathrm{ord}}(-2,x)
                  K_N^{<,\mathrm{ord}}(x,-2\cos u)\right].
\end{gathered}                                                     \tag{1}
\]
The first edge of \(Q_N\) is full. Both traces in (1) are the
original full Hermite traces; no distinct-node trace is substituted.
Set
\[
\begin{gathered}
u_0=\pi/2,\quad t_*(u_0)=a_0-iH_0,\quad
0<a_0<\pi/2,\quad 1/2<H_0<1,\\
\Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,\qquad
s_0=\Re\Phi(t_*(u_0),u_0),\\
\kappa_0=\frac1\pi\operatorname{arsinh}
                       \left(\sin\frac{\pi}{8000}\right),
\qquad 0<\kappa_0<\frac1{8000}.
\end{gathered}                                                     \tag{2}
\]
The symbol \(\kappa_0\) here is a positive real slope, not the
original crossing scalar. The action, charge, and additive
constant in (2) are unchanged.

**Theorem.** For every fixed \(\tau>0\), there is \(C_\tau\)
such that, at all sufficiently large levels of both parities,
\[
\boxed{\quad
 |Q_N(u_{j,N})|+|Q_N^{<<}(u_{j,N})|
 \le C_\tau
  \exp N\left\{s_0-\kappa_0(u_{j,N}-\pi/2)+\tau\right\}
\quad}                                                           \tag{3}
\]
uniformly for
\[
                 0\le j\le U,\qquad u_{j,N}\ge\pi/2.
                                                                    \tag{4}
\]
In particular this covers the previously uncovered physical
band \(\pi/2<u_{j,N}<11\pi/12\), and also the remaining
physical angles up to \(u_{0,N}=\pi-\pi/N\). There is no
off-grid or outgoing-derivative assertion.

## 2. Exact physical rows and quantitative profile monotonicity

For every index in (4), the original Newton zero factors give
the ordinary polynomial identity
\[
          K_N^{<,\mathrm{ord}}(w,c_j)=F_{j,N}(w).
                                                                    \tag{5}
\]
Here \(F_{j,N}=K_N^{\mathrm{ord}}(c_j,w)\) is the actual
physical row, including \(F_{0,N}=1\). This is exactly
equation (5) of the physical outgoing packet.

Use the original normalized slit-plane profiles from
[the all-row slit theorem, Theorem 1](research_mixed_next_first_short_edge_slit_plane_bound.md):
\[
\Psi_x(w)=\int_0^x
 2\operatorname{arsinh}\left(\frac{\sqrt{2-w}}2
                                      \cot(\pi r)\right)\,dr,
\qquad 0\le x\le1/2.
                                                                    \tag{6}
\]
The square root and return are principal, normalized at
\(w=-2\). On each fixed compact subset of
\(\Omega=\mathbb C\setminus[2,\infty)\), uniformly in every
physical row including both index endpoints,
\[
 |F_{j,N}(w)|\le
       \exp N\{\Re\Psi_{j/N}(w)+\epsilon\}
                                                                    \tag{7}
\]
for sufficiently large \(N\), for any prescribed
\(\epsilon>0\).

Put
\[
a_F=\pi-\frac{\pi}{2000},\qquad
a_+=\pi-\frac{\pi}{4000},\qquad
T_N=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N}.
                                                                    \tag{8}
\]
For \(N\ge8000\), one has \(a_F\le T_N\le a_+\), and
\(e^{iNT_N}=-\eta_N\). The angular rectangle
\[
                  |\Re t|\le a_+,\qquad |\Im t|\le H_0
                                                                    \tag{9}
\]
maps to a fixed compact subset of \(\Omega\) by
\(w_t=-2\cos t\). Indeed its real values are strictly
less than two, and a nonreal image cannot meet the removed
real ray. At \(\Re t=0\) its image is negative real.
Throughout (9),
\[
\frac{\sqrt{2-w_t}}2=\cos(t/2)=c_t,\qquad
\Re c_t\ge\sin\frac{\pi}{8000}>0 .
                                                                    \tag{10}
\]

If \(\Re z>0\), write its principal inverse hyperbolic sine
as \(X+iY\), where \(X>0\), \(|Y|<\pi/2\). Then
\(\Re z=\sinh X\cos Y\le\sinh X\), and hence
\[
                    \Re\operatorname{arsinh}z
                              \ge\operatorname{arsinh}(\Re z).
                                                                    \tag{11}
\]
For \(0<r\le1/4\), \(\cot(\pi r)\ge1\). Equations
(10)--(11) therefore give
\[
 \Re\Psi_{1/4}(w_t)-\Re\Psi_{j/N}(w_t)
 \ge 2\pi\kappa_0\left(\frac14-\frac jN\right)
 =\kappa_0\left(u_{j,N}-\frac\pi2+\frac\pi N\right).
                                                                    \tag{12}
\]
The interval of integration is nonnegative because (4)
implies \(j/N\le1/4-1/(2N)\). This proof also includes
the zero row by the integrability at \(r=0\). Discarding
the favorable last term in (12), (7) becomes
\[
 |K_N^<(t,u_{j,N})|
 \le \exp N\left\{\Re\Psi_{1/4}(w_t)
               -\kappa_0(u_{j,N}-\pi/2)+\epsilon\right\}.
                                                                    \tag{13}
\]
No half-grid shift has been approximated in this inequality.

The original calibrated identities, proved in Section 2
of the physical outgoing packet and continued by the
same slit primitive, are
\[
\Psi_{1/2}(w_t)=\psi(t,0),\qquad
\Psi_{1/4}(w_t)=\psi(t,\pi/2).
                                                                    \tag{14}
\]
For signed first angles, these identities use evenness and
real-coefficient Schwarz reflection. They have the same
constant as their positive-angle versions.
The complete-end part of the slit theorem also gives
\[
 |K_N^<(t,0)|
     \le C_\epsilon N^{A_\epsilon}
                 e^{N(\Re\Psi_{1/2}(w_t)+\epsilon)}
                                                                    \tag{15}
\]
uniformly on (9). Thus (13)--(15) are finite bounds for
both literal shortened factors throughout the full
rectangle, not only near a saddle.

## 3. One fixed horizontal contour

Define the unchanged angular source
\[
\begin{gathered}
g_N^{<<}(t,u)=
 \sin t\,K_N^<(t,0)K_N^<(t,u)e^{3iNt^2/(4\pi)},\\
W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered}                                                     \tag{16}
\]
Take the left-to-right horizontal segment
\[
          \Gamma_N=[-T_N,T_N]-iH_0.
                                                                    \tag{17}
\]
Its full multiplier satisfies
\[
 |W_N(t)|\le
            \frac{e^{-NH_0}}{(1-e^{-NH_0})^2}.
                                                                    \tag{18}
\]
This bounds all angular Fourier charges together.

For \(0\le a\le T_N\), the adopted
[positive-horizontal phase theorem, equation (26)](research_mixed_next_inner_three_positive_horizontal_phase_extension.md)
at the fixed reference \(u_0=\pi/2\) gives
\[
                    \Re\Phi(a-iH_0,u_0)\le s_0.
                                                                    \tag{19}
\]
The negative half needs no mixed-height source continuation.
Since the second reference angle is real, the calibrated
edge primitives satisfy
\[
\Re\psi(-a-iH_0,0)=\Re\psi(a-iH_0,0),\qquad
\Re\psi(-a-iH_0,u_0)=\Re\psi(a-iH_0,u_0).
                                                                    \tag{20}
\]
Their sum is exactly the real part of the two slit profiles.
The unit-charge term has real part \(-H_0\) on both halves,
while the crossing changes its sign. Consequently
\[
\Re\Phi(-a-iH_0,u_0)
 =\Re\Phi(a-iH_0,u_0)-\frac{3aH_0}{\pi}\le s_0.
                                                                    \tag{21}
\]
This includes the center \(a=0\).

The sine, length, original \(N^2\), and the interpolation
factor in (15) cost only powers of \(N\). Combining
(13)--(21), for any \(\epsilon>0\),
\[
\frac{N^2}{\pi}\int_{\Gamma_N}
 |g_N^{<<}(t,u_{j,N})W_N(t)|\,|dt|
 \le C_\epsilon N^{B_\epsilon}
 e^{N\{s_0-\kappa_0(u_{j,N}-\pi/2)+2\epsilon\}}.
                                                                    \tag{22}
\]
No assertion about a stationary point for the new outgoing
angle was needed.

## 4. The full original endpoint vertical

We retain the whole vertical term at height \(H_0\), including
both signs:
\[
\mathcal V_N^{<<}(u)=
 \frac{\eta_NN^2C_{N,3}}{\pi}
 \int_{-H_0}^{H_0}
 \frac{g_N^{<<}(T_N+iv,u)}
                        {4\cosh^2(Nv/2)}\,dv .
                                                                    \tag{23}
\]
The upper and lower halves are not separated from the trace
by a new identity. This is its original exact vertical
with its original sign.

In (13), additionally use
\(\Re\Psi_{1/4}\le\Re\Psi_{1/2}\), which follows from
the positive real part of the integrand in (6).
Writing \(h=|v|\), reflection and the original return give
\[
\begin{gathered}
\Re\psi(T_N+iv,0)=\Re\psi(T_N-ih,0),\\
0\le\partial_h\Re\psi(a-ih,0)<1/2
       \quad(0<a<\pi,\ 0\le h\le1),\\
2\Re\psi(T_N-ih,0)\le 2\psi(T_N,0)+h .
\end{gathered}                                                     \tag{24}
\]
The derivative statement follows from
\(-\pi/2<\Im\operatorname{arsinh}\tan((a-ih)/2)\le0\);
it is the same original branch as
[the left-connector proof, equation (22)](research_mixed_next_inner_three_left_connector.md).
That proof's equations (25)--(26) give the exact uniform
far-real bound
\[
                   \psi(T_N,0)<1/200.
                                                                    \tag{25}
\]
Its hypotheses hold since \(T_N\ge a_F\).

Keep the exact denominator and both crossing signs:
\[
\frac1{4\cosh^2(Nv/2)}\le e^{-N|v|},\qquad
\left|e^{3iN(T_N+iv)^2/(4\pi)}\right|
                         \le e^{3N|v|/2}.
                                                                    \tag{26}
\]
Thus the absolute vertical source, with the outgoing
loss retained, has rate at most
\[
2\psi(T_N,0)+\frac32|v|
       -\kappa_0(u_{j,N}-\pi/2)+2\epsilon
<
\frac32+\frac1{100}
       -\kappa_0(u_{j,N}-\pi/2)+2\epsilon .
                                                                    \tag{27}
\]
The original
[action floor](research_mixed_next_inner_three_action_floor_and_top_rows.md)
gives \(s_0>3/2+853/63000\), and
\[
\frac{853}{63000}-\frac1{100}=\frac{223}{63000}>0.
                                                                    \tag{28}
\]
After a fixed sufficiently small choice of \(\epsilon\)
and polynomial absorption, (23) and its entire absolute
integral have a strict gap below the rate in (3) without
the \(\tau\). In particular no limiting \(v=0\) term or
odd-level endpoint was discarded.

## 5. Far derivative samples, full trace, and first-edge restoration

The exact complete-trace formula is
\[
\begin{split}
Q_N^{<<}(u)
={}&-\frac{N^2C_{N,3}}{\pi i}
        \int_{\Gamma_N}g_N^{<<}(t,u)W_N(t)\,dt\\
&+\mathcal V_N^{<<}(u)+\mathcal R_N^{<<}(u),\\
\mathcal R_N^{<<}(u)
={}&\eta_N C_{N,3}
 \sum_{\substack{0\le r<N\\|\tau_r|\ge T_N}}
               \partial_tg_N^{<<}(\tau_r,u),\qquad
\tau_r=\frac{2\pi}{N}(D/2-r).
\end{split}                                                       \tag{29}
\]
This is the original
[full inner trace identity, equation (20)](research_mixed_next_outer_fold_and_inner_source_lift.md),
applied to the degree-\(2U<N\) polynomial
\(K_N^{<,\mathrm{ord}}(-2,x)K_N^{<,\mathrm{ord}}(x,-2\cos u)\).
It is valid for every fixed \(u\), rather than only the old
geometric outgoing box.

For the removed real samples, the actual termwise Newton
and Markov proof in
[short-pair transfer, Section 5](research_mixed_next_inner_three_short_pair_source_transfer.md)
is uniform on the entire real outgoing period. Its only
outside-variable input is the all-index strip bound
\[
\sup_{|\Re u|\le\pi,\ |\Im u|\le2/3}
                 |e_k(-2\cos u)|\le C N^A e^{2N/3}.
                                                                    \tag{30}
\]
Thus, without importing an action comparison outside that
source's stated geometric box, its absolute source estimate is
\[
 \sum_{|\tau_r|\ge T_N}
          |\partial_tg_N^{<<}(\tau_r,u)|
 \le C N^A e^{N E_{\rm far}},\qquad
 E_{\rm far}=b_2+\frac23+\frac1{1000}<\frac{18763}{15000}.
                                                                    \tag{31}
\]
The first normal at each removed double node is included:
on the whole fixed far-real spectral interval the source
has degree at most \(2U\), so Markov gives only a polynomial
cost. Crossing differentiation likewise costs a power of \(N\).
All retained nodes and normals, including the odd central
simple pole, remain in the exact integral (29).

The exact first-edge contraction also has a whole-period
absolute statement:
[first-edge tail theorem, equation (3)](research_mixed_next_inner_three_first_edge_tail_contraction.md)
gives
\[
 |Q_N(u)-Q_N^{<<}(u)|
       \le C N^A e^{N(b_2+2/3)},\qquad
 |\Re u|\le\pi,\quad|\Im u|\le1/2.
                                                                    \tag{32}
\]
At odd levels its explicit simple-node value is retained
in that contraction; it is not called radical.

Both exponents in (31)--(32) are less than \(4/3\).
Meanwhile (2) and the action floor imply, uniformly for
every angle in (4),
\[
s_0-\kappa_0(u_{j,N}-\pi/2)
  >\frac32-\frac{\pi}{16000}
  >\frac32-\frac1{4000}>\frac43.
                                                                    \tag{33}
\]
Thus the far samples and the restored first-edge tail
are strictly smaller than the desired envelope.
Combine (22)--(23), (29), and (31)--(33); take the
two slit tolerances sufficiently small relative to the
prescribed \(\tau\), then absorb polynomial factors.
This proves (3) at both parities.

The theorem preserves the original full trace, crossing,
physical indices, finite kernels, and all endpoint terms.
It does not assert that \(s_0\) lies below the budget of an
outer observation, that the physical values have a common
phase, or that relative errors may be discarded inside an
outer oscillatory sum. Those are separate questions.
