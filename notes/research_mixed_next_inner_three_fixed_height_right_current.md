# The fixed complete-height right current at every physical output

Private finite-source theorem, 9 November 2026. Fix the right-current
path at the original complete-output critical height. Its literal
shortened-kernel current is a polynomial of degree at most
\(\lfloor N/2\rfloor-1\) in the output color. Every double physical
node has a common strict gap below the complete inner action. Exact
cardinal interpolation at both parities preserves that gap on the
whole real spectral interval, and polynomial continuation preserves
a gap on a fixed complex angular strip.

The reference action in this statement is the complete value
\(M_3\). It is not the varying action \(\Re S_3(0,u)\).
The original moving-height right current differs by an explicitly
retained vertical connector, for which no bound is asserted here.
No mathematical numerical evaluation, saved-value calculation or
frozen-source edit is used.

## 1. Fixed path, exact source and statement

Keep the original Newton polynomials, crossing and full Hermite trace,
and put
\[
\begin{gathered}
D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\quad
q=e^{\pi i/N},\quad\eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
c_j=2\cos((2j+1)\pi/N),\qquad0\le j\le U,\\
K_N^{<,\mathrm{ord}}(X,Y)=\sum_{k=0}^{U}e_k(X)e_k(Y),\qquad
K_N^<(t,u)=K_N^{<,\mathrm{ord}}(-2\cos t,-2\cos u),\\
W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered}                                                     \tag{1}
\]
The original selected complete inner point and action are
\[
t_3=a_3-iH_0=t_*(0),\qquad
0<a_3<\pi/2,\quad1/2<H_0<1,\qquad
M_3=\Re S_3(0,0).
                                                                    \tag{2}
\]
These are the branch and normalization in
[cubic continuation](research_mixed_next_inner_three_cubic_continuation.md)
and the [physical outgoing packet](research_mixed_next_inner_three_physical_outgoing_packet.md).
Set
\[
\Delta_0=\frac{(\pi/2-a_3)^2}{8\pi}>0,
\qquad \varepsilon_0=\frac{\Delta_0}{2}>0.
                                                                    \tag{3}
\]
Use the fixed, oriented two-segment path
\[
\gamma_0:\quad
\pi/2-iH_0\longrightarrow5\pi/6-iH_0
                         \longrightarrow5\pi/6-i/10.
                                                                    \tag{4}
\]
For an arbitrary spectral output \(X\), define the literal current
\[
\boxed{\quad
\mathcal R_N^0(X)=
-\frac{N^2C_{N,3}}{\pi i}
\int_{\gamma_0}
 \sin t\,K_N^<(t,0)K_N^{<,\mathrm{ord}}(-2\cos t,X)
             e^{3iNt^2/(4\pi)}W_N(t)\,dt .
\quad}                                                            \tag{5}
\]
In particular \(\mathcal R_N^0\) has exact degree at most \(U\)
in \(X\). The definition includes the original \(N^2\), sign,
unit scalar and full Fourier denominator.

**Theorem.** At both parities and all sufficiently large levels,
every double physical node satisfies
\[
\begin{split}
|\mathcal R_N^0(c_j)|
&\le\frac{N^2}{\pi}\int_{\gamma_0}
 \left|\sin t\,K_N^<(t,0)
 K_N^{<,\mathrm{ord}}(-2\cos t,c_j)
 e^{3iNt^2/(4\pi)}W_N(t)\right|\,|dt|\\
&\le C e^{N(M_3-\varepsilon_0)},\qquad 0\le j\le U.
\end{split}                                                       \tag{6}
\]
Consequently, with constants independent of \(N\),
\[
\sup_{X\in[-2,2]}|\mathcal R_N^0(X)|
       \le C N^3e^{N(M_3-\varepsilon_0)},                           \tag{7}
\]
and for every complex angle \(u\),
\[
|\mathcal R_N^0(-2\cos u)|
 \le C N^4
       \exp\{N(M_3-\varepsilon_0)+U|\Im u|\}.
                                                                    \tag{8}
\]
In particular there is a fixed full-period complex strip with a
strict common-action gap:
\[
\boxed{\quad
\sup_{\substack{|\Re u|\le\pi\\|\Im u|\le\varepsilon_0}}
 |\mathcal R_N^0(-2\cos u)|
       \le C e^{N(M_3-\varepsilon_0/4)}.
\quad}                                                            \tag{9}
\]
The powers of \(N\) in (7)--(8) may be increased without changing
the assertion. No nonzero asymptotic for this current is claimed.

## 2. One eligible physical-row bound for all the nodes

The path (4) lies in the fixed angular rectangle
\[
\pi/2\le\Re t\le5\pi/6,\qquad1/10\le-\Im t\le1.
                                                                    \tag{10}
\]
Its image \(w_t=-2\cos t\) is a compact subset of
\(\Omega=\mathbb C\setminus[2,\infty)\). In this rectangle
\(\Re\cos(t/2)>0\), and the principal square root obeys
\(\sqrt{2-w_t}/2=\cos(t/2)\).

At each of the \(U+1=m\) double nodes, literal Newton zero factors
give the ordinary identity
\[
K_N^{<,\mathrm{ord}}(w,c_j)
       =K_N^{\mathrm{ord}}(w,c_j)=F_{j,N}(w),
                         \qquad0\le j\le U.
                                                                    \tag{11}
\]
This includes \(j=0\), where the row is one, and the last double
node at both parities. It is the identity used in
[the physical packet, equation (5)](research_mixed_next_inner_three_physical_outgoing_packet.md).

The [all-row slit theorem](research_mixed_next_first_short_edge_slit_plane_bound.md)
gives, for every fixed \(\tau>0\), uniformly in all these indices
and on (10),
\[
|F_{j,N}(w_t)|
 \le C_\tau e^{N\{\Re\Psi_{j/N}(w_t)+\tau\}},\qquad
\Psi_x(w_t)=\int_0^x
2\operatorname{arsinh}\{\cos(t/2)\cot(\pi r)\}\,dr.
                                                                    \tag{12}
\]
For \(0<r<1/2\), the argument of this principal return has
positive real part. Its inverse hyperbolic sine therefore has
positive real part. The integrable endpoint at \(r=0\) and
continuity at \(r=1/2\) show that
\[
\Re\Psi_{j/N}(w_t)\le\Re\Psi_{1/2}(w_t)
                         =\Re\psi(t,0).
                                                                    \tag{13}
\]
The last equality is the original normalization, equation (20)
of the slit theorem. No action constant or logarithmic sheet has
been changed.

The same source's complete-end bound, Theorem 2, states
\[
|K_N^<(t,0)|\le C_\tau
                         e^{N\{\Re\psi(t,0)+\tau\}}.
                                                                    \tag{14}
\]
Thus both literal factors on the single fixed path have the
complete-angle profile, uniformly at **all** double output nodes.
This is stronger than just knowing a packet on the node subinterval
\(0<u_j\le\pi/2\). The physical half-step is not approximated:
(13) uses \(j/N\le1/2\) directly.

## 3. The complete-angle path gap and every Fourier charge

Retain the original complete inner phase
\[
\Phi(t,0)=2\psi(t,0)+\frac{3it^2}{4\pi}-it.
                                                                    \tag{15}
\]
The [positive-horizontal phase extension, equation (26)](research_mixed_next_inner_three_positive_horizontal_phase_extension.md)
gives
\[
\Re\Phi(a-iH_0,0)\le M_3-\Delta_0,
                            \qquad\pi/2\le a\le5\pi/6.
                                                                    \tag{16}
\]
Indeed its quadratic loss applies through \(2\pi/3\); thereafter
its strictly negative derivative continues the already larger loss.

On the vertical segment at \(a=5\pi/6\), the original principal
return \(r=\operatorname{arsinh}\tan((a-ih)/2)\) has
nonpositive imaginary part. Keeping both edge returns, the crossing
and the unit charge gives
\[
\partial_h\Re\Phi(a-ih,0)
       =-\frac2\pi\Im r+\frac{3a}{2\pi}-1\ge\frac14,
                     \qquad a=5\pi/6,\quad1/10\le h\le H_0.
                                                                    \tag{17}
\]
Moving upward from \(H_0\) to \(1/10\) therefore decreases the
real phase. Both complete segments of (4) satisfy (16).
This is the original argument in
[the physical packet, equations (17)--(20)](research_mixed_next_inner_three_physical_outgoing_packet.md),
specialized to the actual complete output.

On the whole path, the exact multiplier satisfies
\[
|W_N(a-ih)|
 \le\frac{e^{-Nh}}{(1-e^{-N/10})^2}\le C e^{-Nh}.
                                                                    \tag{18}
\]
This bounds the entire rational multiplier; no higher angular
charge is removed. The last exponential is exactly the real part
of the unit-charge term in (15).

Choose \(\tau=\Delta_0/8\) in each of (12),(14). Equations
(13)--(18) give rate at most \(M_3-3\Delta_0/4\) for the
absolute integrand in (6). The sine and path lengths are uniformly
bounded. Absorb the original \(N^2\) into \(\Delta_0/4\)
of that reserve. The resulting rate is
\(M_3-\Delta_0/2=M_3-\varepsilon_0\), proving (6).
All of these estimates are for the literal finite shortened factors,
including their original row stops and both parity endpoints.

## 4. Exact cardinal interpolation and the strip

The polynomial of the \(m\) double nodes is
\[
Q_{d,N}(X)=\prod_{j=0}^{U}(X-c_j)
 =\begin{cases}
 2T_m(X/2),&N=2m,\\
 U_m(X/2)-U_{m-1}(X/2),&N=2m+1.
 \end{cases}
                                                                    \tag{19}
\]
Here \(U_m\) denotes the Chebyshev polynomial of the second kind.
It is not the cutoff index \(U=m-1\). At odd levels the simple
node \(-2\) is absent from (19), exactly as required for interpolation
of degree at most \(U\).

For clarity, the cardinal norm calculation in
[the slit theorem, Section 6](research_mixed_next_first_short_edge_slit_plane_bound.md)
is
\[
\begin{array}{c|c|c}
&\|Q_{d,N}\|_{[-2,2]}&|Q_{d,N}'(c_j)|\\ \hline
N=2m&\le2&\ge m\\
N=2m+1&\le N&\ge N/4.
\end{array}                                                       \tag{20}
\]
The even derivative has modulus \(m/\sin((2j+1)\pi/N)\).
The odd derivative has modulus
\(N/[4\sin u_j\sin(u_j/2)]\), with
\(u_j=\pi-(2j+1)\pi/N\). The stated lower bounds follow.
Markov's inequality on \([-2,2]\) gives
\(\|Q_{d,N}'\|\le(m^2/2)\|Q_{d,N}\|\).
The mean-value formula therefore bounds each cardinal polynomial
\[
\ell_{j,N}(X)=
 \frac{Q_{d,N}(X)}{(X-c_j)Q_{d,N}'(c_j)}
\]
by \(m\) at even levels and \(2m^2\) at odd levels, including
its removable value at \(X=c_j\).

The endpoints of (5) are independent of the output. Hence the
degree assertion in Section 1 is an ordinary polynomial statement,
and exact interpolation at all \(m=U+1\) nodes applies:
\[
\mathcal R_N^0(X)=\sum_{j=0}^{U}
                       \mathcal R_N^0(c_j)\ell_{j,N}(X).
                                                                    \tag{21}
\]
Summing the cardinal bounds and using (6) proves (7). There is
no interpolation from a proper subset of the physical nodes.

For a polynomial \(P\) of degree at most \(U\), its real-interval
Chebyshev coefficients have modulus at most
\(2\|P\|_{[-2,2]}\). Therefore
\[
|P(-2\cos u)|\le2(U+1)\|P\|_{[-2,2]}e^{U|\Im u|}.
                                                                    \tag{22}
\]
Apply this to (7) to obtain (8). Since \(U<N/2\), the strip
\(|\Im u|\le\varepsilon_0\) costs at most
\(e^{N\varepsilon_0/2}\). Absorbing \(N^4\) in a further
\(\varepsilon_0/4\) proves (9).
This is polynomial continuation of the fixed current, not an
off-grid continuation of individual physical-row identities.

## 5. The original moving current and the retained connector

For the original domain
\[
\mathcal U_+=\{u:b=\Re u\in[0,\pi/2],\ -\Im u\in[0,1/2]\},
\qquad H(u)=-\Im t_*(u),
\]
the [single-current assembly](research_mixed_next_inner_three_single_remaining_current.md)
defines \(\mathcal R_N(u)\) on a path from
\(\pi/2-iH(u)\) to \(5\pi/6-i/10\). Define the literal vertical
connector, with its displayed orientation, by
\[
\begin{split}
\mathcal V_N^0(u)
={}&-\frac{N^2C_{N,3}}{\pi i}
 \int_{\pi/2-iH(u)}^{\pi/2-iH_0}
 \sin t\,K_N^<(t,0)K_N^<(t,u)
                    e^{3iNt^2/(4\pi)}W_N(t)\,dt .
\end{split}                                                       \tag{23}
\]
Both endpoints are strictly in the lower half-plane. For fixed
\(u\), the integrand is holomorphic throughout that half-plane;
all poles of \(W_N\) are real. Path independence and concatenation
therefore give the exact identity
\[
\boxed{\qquad
\mathcal R_N(u)=\mathcal V_N^0(u)
                         +\mathcal R_N^0(-2\cos u).
\qquad}                                                          \tag{24}
\]
Equivalently, (23) has prefactor \(+N^2C_{N,3}/\pi\) when
parameterized by \(t=\pi/2-ih\) and integrated from
\(h=H(u)\) to \(h=H_0\). Thus no orientation sign is implicit.

No estimate for (23) is supplied by (6)--(9). Its endpoints depend
on the output, so it is not the fixed degree-\(U\) polynomial
interpolated in (21). In particular the earlier physical packet
uses a different height \(H(u_j)\) at different nodes; those
currents cannot be silently substituted for the values of (5).

Even for the fixed part, (9) is a gap below \(M_3\). A gap below
the varying action \(s(u)=\Re S_3(0,u)\) would require a
separate comparison. Neither the whole moving current, a full
complex inner packet on the enlarged phase rectangle, nor the
complete outer observation is estimated by this theorem. All
other currents and original trace errors in the single-current
assembly remain as stated there, including its original odd
simple-node contribution and its separate first-edge tail error.

## Frozen source bindings

| Source | SHA-256 |
|---|---|
| All-row and complete-end slit theorem | efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b |
| Original cubic continuation | 8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a |
| Original horizontal concavity | a1e8eb57a7cf867b58c607b5c8d590c5a3ba00d3cba44642fd42456ff4c3298f |
| Positive-horizontal phase extension | a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c |
| Physical outgoing packet and right path | c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3 |
| Original single-current assembly | 2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421 |
