# Complete far-angle removal and short vertical currents for the outer trace

Private written source proof, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source
edit is used.

The full single-three kernel has a usable rate on the far real
angular interval. This pays every removed outer sample, including
its original normal, and both complete vertical currents at a
sufficiently short fixed endpoint height. The remaining lower
contour may descend farther in its interior. No estimate for that
remaining contour is asserted.

## 1. Source and boundary statement

Use the original notation
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad
 M=\lceil N/2\rceil,\quad C_{N,3}=q^{3D^2/4},\\
 s_k=2\sin(\pi k/N),\quad S_k=\prod_{\nu=1}^k s_\nu,\quad
 c_j=2\cos((2j+1)\pi/N),\\
 e_k(x)=S_k^{-2}\prod_{j<k}(c_j-x),\qquad
 K_N^{\rm ord}(x,t)=\sum_{k=0}^{D}e_k(x)e_k(t),\\
 \mathcal K_{3,N}(-2,x)
   =\phi_N^{(t)}
       [\mathcal R_N(t)^3K_N^{\rm ord}(-2,t)K_N^{\rm ord}(x,t)] .
\end{gathered}
 \tag{1}
\]
The inner trace is complete. Its repeated-root normals and
all finite wire indices are retained.

For any ordinary polynomial \(P_N\), define
\[
 \mathcal L_N(P_N)=
 \phi_N^{(x)}
  [\mathcal R_N(x)^3e_M(x)\mathcal K_{3,N}(-2,x)P_N(x)],
\]
\[
 \mathfrak B_N=
 \sup_{\substack{\theta\in[-\pi,\pi]\\|\sigma|\le1/2}}
                  |P_N(-2\cos(\theta+i\sigma))|.
 \tag{2}
\]
The constants below are independent of this polynomial.
In particular no unproved bound for its coefficients is assumed.

Set
\[
 a=\frac{11\pi}{12},\qquad
 m_N=\lfloor N/24\rfloor,\qquad
 a_N=\pi-\frac{2\pi m_N}{N}\ge a,\qquad
 \tau_j=\frac{2\pi}{N}(D/2-j).
 \tag{3}
\]
These are the original half-grid endpoints, with
\(a_N=a+O(N^{-1})\) and \(e^{iNa_N}=-\eta_N\).
Put
\[
 g_N(u)=\sin u\,e_M(-2\cos u)
       \mathcal K_{3,N}(-2,-2\cos u)P_N(-2\cos u)
                              e^{3iNu^2/(4\pi)},
\quad
 W_N(u)=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2}.
 \tag{4}
\]

**Theorem.** There is a fixed \(h_c\in(0,1/2000]\) such that
for all sufficiently large \(N\), of either parity,
the original removed samples
\[
 \mathcal R_N^{\rm far}
   =\eta_N C_{N,3}\sum_{|\tau_j|\ge a_N}g_N'(\tau_j)
 \tag{5}
\]
and the complete paired vertical current
\[
 \mathcal V_N=
 \frac{\eta_NN^2C_{N,3}}{\pi}
   \int_{-h_c}^{h_c}
       \frac{g_N(a_N+iv)}{4\cosh^2(Nv/2)}\,dv
 \tag{6}
\]
satisfy
\[
 |\mathcal R_N^{\rm far}|+|\mathcal V_N|
   \le C N^A\mathfrak B_N
                    e^{N(8/5+1/1000)}.
 \tag{7}
\]
The same bound holds for their separate absolute sample and
integrand sums, and hence pays both vertical heights without
relying on their cancellation.
Since
\[
 B_f=\frac{77}{50}+\frac{\pi}{50},
 \qquad B_f-\frac85=\frac{\pi-3}{50}>\frac1{400},
 \tag{8}
\]
the boundary operator rate in (7) is strictly below
\(B_f-1/1000\).

For every piecewise smooth path \(\Gamma_N\) in the open lower
half-plane from \(-a_N-ih_c\) to \(a_N-ih_c\), the exact
remaining source is
\[
 \boxed{\quad
 \mathcal L_N(P_N)
   =-\frac{N^2C_{N,3}}{\pi i}
        \int_{\Gamma_N}g_N(u)W_N(u)\,du
        +\mathcal V_N+\mathcal R_N^{\rm far}.
 \quad}
 \tag{9}
\]
No height restriction is imposed on the interior of
\(\Gamma_N\). Equation (7) estimates neither that integral
nor its pointwise integrand.

## 2. A complete Newton bound on the terminal strip

The complete terminal insertion operator of
[the paired-right theorem, Section 4](research_mixed_next_right_paired_terminal_insertion.md),
with the smaller-strip justification in
[insertion recoupling, Section 4](research_mixed_next_right_insertion_recoupling_and_norm.md),
has actual trace height
\[
 h_{\rm tr}=2\operatorname{arsinh}\sqrt{(\sqrt2-1)/4},
 \qquad \cosh h_{\rm tr}=(1+\sqrt2)/2.
 \tag{10}
\]
It is strictly below \(2/3\). Indeed
\(\sqrt2<13/9\), while
\(\cosh(2/3)>1+(2/3)^2/2=11/9\).
Thus the entire strip \(|\Im t|\le2/3\) is an eligible
insertion norm, with a fixed positive derivative margin.

We prove, for every original Newton index,
\[
 \sup_{\substack{\theta\in[-\pi,\pi]\\ |h|\le2/3}}
        |e_k(-2\cos(\theta+ih))|
      \le C N^A e^{2N/3},
                     \qquad 0\le k\le D.
 \tag{11}
\]
Write
\[
 J(y)=\int_0^y\log|2\sin\pi s|\,ds,\qquad
 V_z(y)=\int_0^y
      \log|2\cos(2\pi s)+2\cos z|\,ds-2J(y).
 \tag{12}
\]
The zero-safe midpoint product argument in
[the complete kernel Fourier bound, Section 2](research_mixed_next_physical_three_kernel_fourier_bound.md)
applies on this fixed compact height range as well: the two
numerator factors have the same shifted logarithmic-sine
singularities, and their one-sided mesh error is \(O(\log N)\)
uniformly through every zero. The denominator has its original
uniform factorial estimate. Hence
\[
 |e_k(-2\cos z)|\le C N^A e^{NV_z(k/N)}
                   \qquad (|\Re z|\le\pi,\ |\Im z|\le2/3).
 \tag{13}
\]
This extends the compact height range of that mesh argument;
it does not infer an asymptotic expansion across a zero.

On \(0\le y\le1/2\), the exact angular derivative and radial
comparison give
\[
 0\le V_{\theta-ih}(y)\le V_{-ih}(y),\qquad 0\le h\le2/3.
 \tag{14}
\]
The upper inequality follows from the nonpositive angular
derivative in equation (19) of
[the spectral ellipse proof](research_mixed_next_middle_fixed_spectral_ellipse.md);
the formula holds at every positive bounded \(h\), and its
real-height limit is continuous. The lower inequality follows
from the increasing radial modulus and the original real
Newton comparison.
Also, exactly,
\[
 V_{\theta-ih}(1-y)=h-V_{\theta-ih}(y).
 \tag{15}
\]
Both identities follow from the full circle logarithm and retain
the original upper Newton half.

For the lower-half maximum, put \(C=\cosh h\).
The positive series gives
\[
 \cosh(2/3)
 \le 1+\frac29+\frac{2/243}{1-2/135}
       =\frac{491}{399}<\frac54 .
 \tag{16}
\]
Here the ratio of consecutive terms after the fourth-power term
is at most \(2/135\).
For \(3/10\le y<1/2\), \(c=\cos(2\pi y)<-1/4\), and
\[
 e^{\partial_yV_{-ih}(y)}
       =\frac{c+C}{1-c}<1 .
 \tag{17}
\]
The endpoint limits have the same decreasing comparison.
Thus its maximum occurs at \(y\le3/10\).

On that shorter interval the exact height comparison from
the kernel Fourier bound gives
\[
 V_{-ih}(y)\le V_0(y)
                    +\frac{\cosh h-1}{2\pi}\tan(\pi y)
 \le b_2+\frac7{96}<\frac23.
 \tag{18}
\]
We used \(\tan(3\pi/10)<\sqrt3<7/4\), \(\pi>3\), and
the adopted \(b_2<729/1250\).
The final rational inequality is
\[
 \frac{729}{1250}+\frac7{96}
       =\frac{39367}{60000}<\frac{40000}{60000}.
 \tag{19}
\]
Equations (14),(18) bound the entire lower half. Equations
(14)--(15) bound the upper half by \(h\le2/3\).
Together with the finite product bound (13), this proves (11).

## 3. The full single-three kernel at far real angles

Let \(m(\theta)=\max_{0\le y\le1}V_\theta(y)\). The exact
real-period derivative is
\[
 m'(\theta)=-\pi^{-1}
                      \operatorname{arsinh}(\sin(\theta/2)),
 \qquad 0<\theta<\pi,\qquad m(\pi)=0.
 \tag{20}
\]
It is proved in
[real-period Newton, Lemma 3](research_three_crossing_real_period_newton_bound.md).
Since \(\operatorname{arsinh}(1)<1\), integration gives
\[
 m(\theta)\le\frac{\pi-\theta}{\pi}\le\frac1{12},
                  \qquad 11\pi/12\le\theta\le\pi .
 \tag{21}
\]
For the strict elementary inequality, \(\sinh(1)>1\)
already follows from its positive cubic term.

The original all-index real Newton bound, including its upper
half, therefore proves
\[
 |e_k(-2\cos\theta)|\le C N^A e^{N/12}
          \quad(|\theta|\ge a,\ 0\le k\le D).
 \tag{22}
\]
For the whole polynomial
\(I_\theta(t)=K_N^{\rm ord}(-2\cos\theta,t)\),
(11),(22) give
\[
 \|I_\theta\|_{|\Im t|\le2/3}
                  \le C N^A e^{3N/4}.
 \tag{23}
\]
No physical termination or positivity is required for this
ordinary real spectral value.

The complete terminal insertion estimate, on the eligible
strip (10), is
\[
 |\phi_N[\mathcal R_N^3K_N^{\rm ord}(-2,\cdot)I]|
   \le C_\epsilon N^{A_\epsilon}
                  e^{N(M_{\rm term}+\epsilon)}\|I\|_{2/3},
                    \qquad \deg I\le N .
 \tag{24}
\]
The original terminal rate satisfies \(M_{\rm term}<17/20\),
as recorded with the full source inventory in
[the actual high-band theorem, equation (17)](research_mixed_next_right_insertion_actual_high_band.md).
Choose its positive tolerance smaller than
\(17/20-M_{\rm term}\). Applying (24) to (23) proves
\[
 \boxed{\quad
 |\mathcal K_{3,N}(-2,-2\cos\theta)|
       \le C N^A e^{8N/5},\qquad a\le|\theta|\le\pi.
 \quad}
 \tag{25}
\]
All removed wire groups, physical normals, Fourier charges,
wire aliases and endpoint connectors of that operator remain
included. In particular (25) bounds the entire inner kernel,
not a chosen saddle contribution.

As a polynomial in its second spectral argument, this kernel
has degree at most \(D<N\). The real spectral interval in
(25) is the fixed interval
\[
                      I=[\,2\cos(\pi/12),\,2\,].
 \tag{26}
\]
Ordinary Chebyshev continuation from \(I\) implies that for
each \(\epsilon>0\), some fixed \(\delta_\epsilon>0\) gives
\[
 |\mathcal K_{3,N}(-2,\xi)|
       \le C_\epsilon N^{A_\epsilon}e^{N(8/5+\epsilon)}
        \quad\hbox{if }\operatorname{dist}(\xi,I)\le\delta_\epsilon.
 \tag{27}
\]
Explicitly, map \(I\) affinely to \([-1,1]\). Its Chebyshev
coefficients are bounded by twice the real supremum. On a
filled ellipse of parameter \(e^\epsilon\), the \(k\)-th
polynomial has modulus at most \(e^{\epsilon k}\).
Summing at most \(N\) terms proves (27), and that ellipse
contains a fixed neighborhood of \(I\).

## 4. Every removed normal and both exact vertical currents

The exact radical factors are
\[
 e_M(-2\cos u)=
 \begin{cases}
 \cos(Nu/2)/N,&N\ \text{even},\\[1mm]
 -\sin(u/2)\sin(Nu/2)/
       \{N\cos^2(\pi/(2N))\},&N\ \text{odd}.
 \end{cases}
 \tag{28}
\]
They are derived from the original sine products in
[the thin-strip source calculation, Section 2](research_mixed_next_three_outer_mode_thin_strip_obstruction.md).
At every real physical point \(\tau_j\),
\(e_M(-2\cos\tau_j)=0\), and the angular derivative of
(28) is bounded by an absolute constant.
Consequently in \(g_N'(\tau_j)\) every derivative of
\(\mathcal K_{3,N}\), of \(P_N\), and of the chirp is
multiplied by that exact zero. The only surviving term
differentiates the radical factor.
Equations (2),(25) give the absolute sample bound
\[
 \sum_{|\tau_j|\ge a_N}|g_N'(\tau_j)|
                  \le C N^A\mathfrak B_N e^{8N/5}.
 \tag{29}
\]
This is the original consumed outer normal; no distinct-node
trace is substituted. It explains why even a high-degree
spectator has no unaccounted derivative cost. The inner
normals are already part of (25).

Apply (27) with \(\epsilon=1/2000\). Choose a fixed
\(h_c>0\) satisfying
\[
 h_c\le1/2000,\qquad
                 2(e^{h_c}-1)<\delta_{1/2000}.
 \tag{30}
\]
Since \(-2\cos a_N\in I\), the estimate
\[
 |-2\cos(a_N+iv)+2\cos a_N|
                         \le2(e^{|v|}-1)
 \tag{31}
\]
places the whole vertical segment in (27).
The spectator on this segment is bounded by \(\mathfrak B_N\),
since \(h_c<1/2\).

Formula (28), with the exact trace denominator, gives
\[
 |e_M(-2\cos(a_N+iv))|\le C N^{-1}e^{N|v|/2},
 \qquad
 \frac1{4\cosh^2(Nv/2)}\le e^{-N|v|}.
 \tag{32}
\]
The remaining sine is bounded by a fixed constant, and
\[
 |e^{3iN(a_N+iv)^2/(4\pi)}|
       =e^{-3Na_Nv/(2\pi)}
       \le e^{3N|v|/2}.
 \tag{33}
\]
Their total height cost is at most \(e^{N|v|}\).
Using (27),(30), this bounds the absolute integral in (6) by
\[
 C N^A\mathfrak B_N
          e^{N(8/5+1/2000+h_c)}
 \le C N^A\mathfrak B_N e^{N(8/5+1/1000)} .
 \tag{34}
\]
Together with (29), this proves (7).
The inequality in (8) uses only \(\pi>25/8\).

Finally the exact complete trace, Corollary 3 of
[the original contour identity](research_exact_complete_trace_contour.md),
is (9) with the straight lower horizontal and with the
unchanged vertical term (6). The omitted terms are exactly
(5). All its poles are on the real physical grid, so the
lower integrand is holomorphic in the open lower half-plane.
Cauchy's theorem therefore replaces the horizontal by any
path stated in (9). This changes neither vertical current
nor a physical sampling term.

## 5. Application to the actual insertion and remaining scope

Take the actual polynomial \(P_N=H_N(\cdot,Z_*)\) from
[the outer observation](research_mixed_next_three_outer_casimir_observation.md).
Thus the reference is the complete color \(w=-2\) for an actual
word in powers three and four beginning \(343\), of length at
least five, at its original output \(z_*\). Keep
\(\Lambda=\Re\mathcal P_*>419/200\) and
\(\kappa=q^{D^2/2}\).
The fixed-ellipse theorem gives, for each \(\tau>0\),
\[
 \mathfrak B_N\le C_\tau N^{A_\tau}e^{N(E_*+\tau)},
 \qquad
 E_*=\Lambda-B_0-1/50,\quad B_0=2383/1500 .
 \tag{35}
\]
This application uses that theorem's full outgoing sum and
its separately bounded small-index subtraction.
It is not inferred from a bound on a single physical value.

Taking \(\tau=1/2000\), the right side of (7) has rate at most
\[
 E_*+\frac1{2000}+\frac85+\frac1{1000}
       =\Lambda-\frac{43}{6000}
       <\Lambda-\frac1{200}.
 \tag{36}
\]
The exact outside factor \((-q)^M/(\kappa^2N)\) has modulus
\(1/N\). Thus the actual boundary contribution to the
remaining transfer is \(O(e^{N(\Lambda-1/200)})\), after
absorbing the fixed polynomial costs. Both level parities,
the full original normalization, and all boundary signs
are retained.

The unestimated part is exactly the first integral in (9),
with this same \(H_N\) and the unchanged inner full kernel.
Its endpoint height is the fixed small \(h_c\); its interior
may descend to a different height. The theorem does not
bound the long vertical segments obtained by lowering its
endpoints to \(1/2\), and does not assume that a straight
horizontal at that depth is adequate. It proves neither
the remaining signed integral's suppression nor a full
transfer asymptotic or noncancellation statement.
