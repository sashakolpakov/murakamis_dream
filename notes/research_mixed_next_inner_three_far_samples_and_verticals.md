# Complete far samples and endpoint verticals of the shortened inner three-trace

Private source proof, 8 November 2026. No mathematical numerical
evaluation, saved-value calculation, or frozen-source edit is used.

A uniform lower bound for the actual continued inner action pays
every sufficiently far real angular sample of the original shortened
inner trace, including its first normal, and both full endpoint
vertical currents at a fixed small height. The central angular
integral remains unchanged and unestimated.

## 1. Actual source and statement

Keep
\[
 \begin{gathered}
 N\ge3,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\quad
 U=\lfloor N/2\rfloor-1,\\
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),\qquad
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 f_N(t,u)=K_N(t,0)K_N^<(t,u),\qquad
 Q_N(u)=\phi_N^{(t)}[R_N(t)^3f_N(t,u)] .
 \end{gathered}
 \tag{1}
\]
These are the exact first edge, shortened second edge, crossing,
and full Hermite trace in
[the low-edge reduction, equation (12)](research_mixed_next_outer_exact_low_edge_reduction.md).
The first edge is not truncated. The second terminates at the
same \(U\) at both parities.

Let
\[
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\}.
 \tag{2}
\]
The original cubic branch is \(t_*(u)=a_*(u)-iH_*(u)\), with
\(0<a_*<\pi/2\), \(0<H_*<1\), and stationary action
\[
 S(u)=\Phi(t_*(u),u),\qquad
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it .
 \tag{3}
\]
The action constant and zero logarithmic charge are those of
[the continued original cubic](research_mixed_next_inner_three_cubic_continuation.md).

Use the fixed cutoff and its exact physical midpoint
\[
 a=\pi-\frac{\pi}{2000},\qquad
 m_N=\lfloor N/4000\rfloor,\qquad
 T_N=\pi-\frac{2\pi m_N}{N}\ge a,\qquad
 \tau_j=\frac{2\pi}{N}(D/2-j).
 \tag{4}
\]
Thus \(T_N=a+O(N^{-1})\) and
\(e^{iNT_N}=-\eta_N\). Put
\[
 \widetilde g_N(t,u)=\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
 \tag{5}
\]

**Theorem.** There is a fixed \(h_c\in(0,1/2000]\), independent
of \(u\in\mathcal U_+\), such that
\[
 \begin{split}
 \mathcal R_N(u)&=\eta_NC_{N,3}
        \sum_{|\tau_j|\ge T_N}\partial_t\widetilde g_N(\tau_j,u),\\
 \mathcal V_N(u)&=\frac{\eta_NN^2C_{N,3}}{\pi}
        \int_{-h_c}^{h_c}
        \frac{\widetilde g_N(T_N+iv,u)}
                          {4\cosh^2(Nv/2)}\,dv
 \end{split}
 \tag{6}
\]
obey, for all sufficiently large \(N\) of either parity,
\[
 |\mathcal R_N(u)|+|\mathcal V_N(u)|
       \le C e^{N(\Re S(u)-1/500)} .
 \tag{7}
\]
The corresponding absolute sample sum and absolute vertical
integral satisfy the same estimate. Consequently, for any
piecewise smooth lower-half-plane path \(\Gamma_N\) from
\(-T_N-ih_c\) to \(T_N-ih_c\),
\[
 \boxed{\quad
 Q_N(u)=-\frac{N^2C_{N,3}}{\pi i}
      \int_{\Gamma_N}\widetilde g_N(t,u)W_N(t)\,dt
             +O(e^{N(\Re S(u)-1/500)}).
 \quad}
 \tag{8}
\]
No bound for the remaining integral is part of this theorem.
All inner physical nodes not in (6), including the odd-level
central simple node, remain in that exact integral.

## 2. A written uniform floor for the actual stationary action

The original edge phase is the holomorphic primitive on the full
independent box
\[
 0\le\Re t,\Re u\le\pi/2,\quad
 0\le-\Im t\le1,\quad0\le-\Im u\le1/2
 \tag{9}
\]
proved in
[the shortened-edge endpoint theorem, Lemma 1](research_mixed_next_shortened_edge_endpoint_gap.md).
In particular
\[
 \psi_u(t,u)=-\frac1\pi
      \operatorname{arsinh}\{\tan(u/2)\cos(t/2)\},
 \tag{10}
\]
and the analogous \(t\)-derivative use their original principal
returns, with nonnegative real parts. No logarithmic lift is reset.

The [horizontal concavity theorem](research_mixed_next_inner_three_horizontal_concavity.md)
gives the actual fixed-height comparison
\[
 \Re S(u)\ge\Re\Phi(\pi/2-iH_*(u),u).
 \tag{11}
\]
This comparison concerns the original phase, not an absolute
finite-kernel estimate. Its source use here is solely to lower-bound
the target action in (7).

Write \(H=H_*(u)\), and set \(t_R=\pi/2-iH\).
At fixed heights, nonnegativity of the real returns in (10) gives
\[
 \Re\psi(t_R,b-iK)\ge\Re\psi(t_R,\pi/2-iK).
 \tag{12}
\]
We record the height cost on the right side directly. For
\(0\le k\le K\), let
\[
 z_k=\tan(\pi/4-ik/2)\cos(\pi/4-iH/2).
 \tag{13}
\]
Its real part is positive by the original cut-safe box lemma.
The tangent in (13) has argument at most zero, whereas
\[
 0<\arg\cos(\pi/4-iH/2)
       =\arctan(\tanh(H/2))<H/2.
 \tag{14}
\]
It follows that
\[
                 \Im\operatorname{arsinh}z_k<H/2.
 \tag{15}
\]
Here is a direct branch check. If \(\Im z_k\le0\), the principal
return has nonpositive imaginary part. Otherwise write it as
\(\xi+i\nu\), where \(\xi>0\) and \(0<\nu<\pi/2\).
The identity \(z_k=\sinh(\xi+i\nu)\) gives
\(\arg z_k=\arctan(\coth\xi\tan\nu)>\nu\).
This proves (15) from (14) without replacing the original return.
Since the derivative with respect to downward height is
\(-\Im\operatorname{arsinh}z_k/\pi\), integration gives
\[
 \Re\psi(t_R,\pi/2-iK)
       \ge\Re\psi(t_R,\pi/2)-\frac{HK}{2\pi}.
 \tag{16}
\]

For a real second angle \(0\) or \(\pi/2\), the argument of
the first return along \(t=\pi/2-ih\), \(h>0\), has negative
imaginary part. Thus \(\Re\psi(\pi/2-ih,\cdot)\) increases
with \(h\), and real-angle monotonicity further gives
\[
 \Re\psi(t_R,0)\ge\psi(\pi/2,0)
                   \ge\psi(\pi/2,\pi/2),\qquad
 \Re\psi(t_R,\pi/2)\ge\psi(\pi/2,\pi/2).
 \tag{17}
\]
The exact real-corner value and its written sine witness in that
same endpoint theorem are
\[
 \psi(\pi/2,\pi/2)=-5J(1/6)>\frac{50}{63}.
 \tag{18}
\]
At \(t_R\) the crossing and unit trace charge in (3) have real
part \(-H/4\). Equations (11)--(18) therefore prove
\[
 \boxed{\quad
 \Re S(u)>
 \frac{100}{63}-\frac{HK}{2\pi}-\frac H4
 >
 \frac{100}{63}-\frac1{4\pi}-\frac14
 >
 \frac{79}{63}.
 \quad}
 \tag{19}
\]
The last comparison uses only \(\pi>3\). This is uniform on the
closed actual family and includes \(b=0\) and \(K=0\).

## 3. Full finite source on the far real interval

Use the original all-index Newton estimates from
[real-period Newton](research_three_crossing_real_period_newton_bound.md)
and
[the complete outer boundary source, Sections 2--3](research_mixed_next_outer_far_angles_and_verticals.md):
\[
 \begin{split}
 |e_j(-2)|&\le CN^A e^{Nb_2},
                       &&0\le j\le D,\\
 \sup_{\substack{|\theta|\le\pi\\|h|\le2/3}}
 |e_j(-2\cos(\theta+ih))|
            &\le CN^A e^{2N/3},
                       &&0\le j\le D,\\
 |e_j(-2\cos\theta)|&\le CN^A e^{Nm(\theta)},
                       &&0\le j\le D.
 \end{split}
 \tag{20}
\]
Here the complete upper Newton half and its zeros are included.
The notation is \(b_2=-4J(1/4)\) and
\[
 m(\theta)=\max_{0\le y\le1}
 \left\{\int_0^y\log|2\cos(2\pi s)+2\cos\theta|\,ds-2J(y)\right\}.
\]
The cited source proves
\[
 b_2<\frac{729}{1250},\qquad
 m(\pi)=0,\quad
 m'(\theta)=-\frac1\pi\operatorname{arsinh}(\sin(\theta/2))
                      \quad(0<\theta<\pi).
 \tag{21}
\]
Evenness gives the negative real half. Since
\(\operatorname{arsinh}(1)<1\), the last two identities imply
\[
 m(\theta)\le\frac{\pi-|\theta|}{\pi}
                   \le\frac1{2000}\qquad(a\le|\theta|\le\pi).
 \tag{22}
\]
All estimates (20) are uniform finite upper bounds with a
polynomial prefactor, obtained from the original zero-safe
logarithmic products. They are not asymptotic expansions through
moving zeros.

Apply (20) term by term to the two original finite sums in (1).
The first uses every \(0\le j\le D\); the second uses exactly
\(0\le j\le U\). The outer \(u\)-height is at most \(1/2<2/3\).
Consequently
\[
 \sup_{\substack{a\le|\theta|\le\pi\\u\in\mathcal U_+}}
 |f_N(\theta,u)|
 \le CN^A e^{NE_{\rm far}},\qquad
 E_{\rm far}=b_2+\frac23+\frac1{1000}
                          <\frac{18763}{15000}.
 \tag{23}
\]
Both finite sums have at most \(N\) terms. No coherent cancellation
is required for (23), nor is a full-kernel bound assigned to a
partial sum.

As a polynomial in the traced spectral variable \(x=-2\cos\theta\),
\(f_N\) has degree at most
\[
                         D+U<3N/2.
 \tag{24}
\]
Its bound (23) holds on the fixed whole interval
\[
                         I=[2\cos(\pi/2000),2].
 \tag{25}
\]
Markov's inequality on \(I\), valid also for complex coefficients,
therefore bounds its first spectral derivative at a polynomial
cost, uniformly in \(u\). The original angular derivative is this
derivative times \(2\sin\theta\). The derivative of the crossing
exponential contributes only a further factor \(O(N)\) on the
real axis. Thus the exact complete derivative sampling formula
gives
\[
 \sum_{|\tau_j|\ge T_N}
       |\partial_t\widetilde g_N(\tau_j,u)|
                 \le CN^A e^{NE_{\rm far}}.
 \tag{26}
\]
In particular every retained first normal in these removed
samples has been estimated.

## 4. Fixed small verticals, with their original denominator

Map the fixed interval \(I\) affinely to \([-1,1]\).
Expand the polynomial in (24) in ordinary Chebyshev polynomials.
Its coefficients are bounded by twice the supremum in (23).
On the filled ellipse of parameter \(e^{1/6000}\), (24) gives
the additional cost at most \(N/4000\). The sum of the
coefficients costs only another polynomial factor. This ellipse
contains a fixed complex neighborhood of \(I\).
Choose \(h_c>0\) so small that
\[
 h_c\le1/2000,\qquad
 -2\cos(T_N+iv)
 \ \text{lies in that neighborhood for all }|v|\le h_c .
 \tag{27}
\]
Such a common choice exists: \(-2\cos T_N\in I\) and
\[
 |-2\cos(T_N+iv)+2\cos T_N|
                       \le2(e^{|v|}-1).
 \tag{28}
\]
This proves the full finite source estimate
\[
 |f_N(T_N+iv,u)|
       \le CN^A e^{N(E_{\rm far}+1/4000)}
                 \qquad(|v|\le h_c,\ u\in\mathcal U_+).
 \tag{29}
\]
No expansion or division by a factorial zero was used.

The exact vertical denominator and crossing satisfy
\[
 \frac1{4\cosh^2(Nv/2)}\le e^{-N|v|},\qquad
 \left|e^{3iN(T_N+iv)^2/(4\pi)}\right|
          \le e^{3N|v|/2}.
 \tag{30}
\]
The sine factor is bounded on this compact rectangle.
The remaining height cost is therefore at most
\(Nh_c/2\le N/4000\). Including the original \(N^2\)
and integrating the full interval gives
\[
 |\mathcal V_N(u)|
       \le CN^A e^{N(E_{\rm far}+1/2000)} .
 \tag{31}
\]
This also bounds its absolute integrand integral; no cancellation
between the two height signs has been used.

The exact rational reserve is
\[
 \frac{79}{63}
       -\left(\frac{18763}{15000}+\frac1{2000}\right)
       =\frac{1639}{630000}>\frac1{400}.
 \tag{32}
\]
Equations (19), (26), and (31), with polynomial absorption into
the difference between \(1/400\) and \(1/500\), prove (7).
The exact complete-trace contour identity, with its half-grid
endpoint signs, then proves (8).

The interior angular path may descend farther than \(h_c\).
Its source away from the selected cubic neighborhood, its
coefficient of the selected local Gaussian, and the remaining
outer positive-half observations have not been estimated here.
No complex-parameter jet assertion or full inner packet is
inferred from these pointwise uniform boundary bounds.
