# A uniform large-power turn of a controlled boundary source

The original turn does not preserve concentration in general. A sufficiently
large crossing power before the turn does give a uniform theorem, provided
the input sources have common analytic bounds, including bounds on the
imaginary quadratic part of their phases. The power threshold below is
independent of the member of the input family. It is not asserted to be
independent of repeated applications of the theorem.

The principal application is the full boundary source
\(T(R^bT(R^a))\). There is one finite threshold \(B_*\) such that its
boundary asymptotic is proved for every fixed \(|a|\ge2\) and every
fixed \(|b|\ge B_*\), with unrelated signs. No new contour certificate
for each pair is needed. The infinitely many assignments with a short
outer power are not covered by this statement.

## 1. The exact operation and the common hypotheses

Put \(D=N-1\) and use the original algebra
\[
 \mathcal A_N=\mathbb C[z]/\bigl(2T_N(z/2)+2\bigr),
 \qquad \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{1}
\]
Here \(T_N\) on the right is the ordinary Chebyshev polynomial, whereas
\(T\) without a subscript is the physical turn. It reverses Newton
coefficients. In particular the complete kernel
\[
 K_N(t,u)=\sum_{k=0}^{D}e_k(-2\cos t)e_k(-2\cos u)
 \tag{2}
\]
satisfies the exact identity
\[
 (Tf)(-2\cos u)=\phi_N^{(t)}\bigl(f(-2\cos t)K_N(t,u)\bigr).
 \tag{3}
\]
Both sides use the full quotient, including the first normals at its
double roots. Thus the source studied here is precisely
\[
 P_{j,b,N}(u)=\phi_N^{(t)}\!\left[R^bF_{j,N}(t)K_N(t,u)\right]
       =\bigl[T(R^bF_{j,N})\bigr](-2\cos u).
 \tag{4}
\]
There is no extra factor of \(N\) in (3) or (4). The raw product in the
trace is retained before any asymptotic estimate.

Let \(j\) range over an arbitrary family of canonical boundary
polynomials of degree at most \(D\) in \(-2\cos t\). Assume the
following common data.

* On a neighborhood of one closed disk \(|t|\le r_0\),
  \[
   F_{j,N}(t)=\varepsilon_{j,N}N^{\alpha_j}A_j(t)e^{NW_j(t)}
                         (1+O_j(N^{-1})),\qquad
                         |\varepsilon_{j,N}|=1.
   \tag{5}
  \]
  The phases and amplitudes are even and holomorphic. Every \(A_j\)
  is nonzero on this same disk. The expansion and its holomorphic
  error hold on this disk, not merely at the complete boundary.
* With \(M_j=\Re W_j(0)\), there are common positive constants
  \(c,B,h_0\) such that
  \[
   |F_{j,N}(x+iy)|\le C_jN^{d_j}
       e^{N\{M_j-c(1-\cos x)+By^2\}},
       \quad |x|\le\pi,\quad |y|\le h_0.
   \tag{6}
  \]
* The normalized phases \(W_j-W_j(0)\) have a common holomorphic
  bound on the stated disk, and
  \[
                  -\Re W_j''(0)\ge a_*>0.
   \tag{7}
  \]

The constants in (5), its starting level, the exponents \(\alpha_j,d_j\),
and the sizes of \(A_j\) may depend on \(j\). No common positive lower
bound on \(|A_j(0)|\) is assumed. In particular these hypotheses allow
the terminal amplitudes to decrease like \(|a|^{-3/2}\).

The edge phase and amplitude are those of the original complete-kernel
theorem:
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \quad \psi(0,0)=M_\infty=\frac{4G}{\pi},
 \tag{8}
\]
near zero. We use also its proved whole real-angle estimates, retained
wire expansion, and full Hermite bounds; these are stated explicitly in
[the isolated-vertex theorem](research_high_degree_short_internal_vertex.md),
Sections 3--6. In particular omitted wire indices outside
\([N/5,3N/10]\) lose \(\delta_e=\pi/100\) in the exponential rate,
and the retained kernel satisfies
\[
 |K_{N,I}(t,u)|\le C N^{-3/2}
 e^{N\{\Re\psi(t,0)-\gamma(1-\cos u)\}},\quad
 \gamma=1/20,\quad u\in[-\pi,\pi],
 \tag{9}
\]
throughout a fixed small complex \(t\)-disk.

## 2. The theorem

**Theorem.** Under (5)--(7), there are a finite integer \(B_*\), a
positive radius \(\rho\), and positive whole-strip constants
\(c_*,B_1,h_1\), depending only on the common data, such that for
every member \(j\) and every fixed signed integer \(|b|\ge B_*\),
\[
 P_{j,b,N}(u)=\varepsilon_{j,N}C_{N,b}N^{\alpha_j}
      \mathcal A_{j,b}(u)e^{N\mathcal S_{j,b}(u)}
                         (1+O_{j,b}(N^{-1})),
 \quad C_{N,b}=e^{\pi i b(N-1)^2/(4N)},
 \tag{10}
\]
on one common disk \(|u|\le\rho\), through both level parities.
The amplitude is holomorphic and nonzero on that disk. Set
\[
 \Phi_j(t,u)=W_j(t)+\psi(t,u),\qquad
 \mathcal S_{j,b}(u)=
   \operatorname{stat}_t\left[\Phi_j(t,u)+\frac{ib}{4\pi}t^2-it\right].
 \tag{11}
\]
The critical point in (11) is the unique small one, denoted \(t_*(u)\),
and
\[
 \mathcal A_{j,b}(u)=i\sqrt{\frac2\pi}
 \frac{\sin t_*(u)\,A_j(t_*(u))a_e(t_*(u),u)}
 {\sqrt{-\Phi_{j,tt}(t_*(u),u)-ib/(2\pi)}}.
 \tag{12}
\]
The square root is selected by the local Gaussian integral. The
whole original polynomial also satisfies
\[
 |P_{j,b,N}(x+iy)|\le C_{j,b}N^{d_{j,b}}
 e^{N\{M_{j,b}-c_*(1-\cos x)+B_1y^2\}},
 \quad M_{j,b}=\Re\mathcal S_{j,b}(0),
 \tag{13}
\]
for \(|x|\le\pi, |y|\le h_1\). Its normalized phases have common
bounds on a fixed disk, and
\[
 \mathcal S_{j,b}''(0)=-\frac{\cos(t_*(0)/2)}{2\pi}.
 \tag{14}
\]
In particular their real curvature is bounded away from zero.
The error constants and starting levels in (10), as well as the
polynomial constants in (13), may depend on \(j,b\).

## 3. Choosing a uniform threshold and locating the saddle

Evenness, the common phase bounds, and (7) permit fixed choices
\(0<r<1/16\), \(a_0,L>0\) such that, on \(|t|,|u|\le3r\),
\[
 |\Phi_{j,tt}|\le L,\qquad
 \Re\Phi_{j,tt}\le-a_0<0.
 \tag{15}
\]
The input expansions hold there, all their amplitudes are nonzero,
and (9) holds for \(|t|\le3r\). Choose
\[
 \delta_0=\min\{\delta_e,c(1-\cos(r/2))\},\qquad
 C_h=8\pi^2L.
 \tag{16}
\]
It suffices initially to require
\[
 |b|\ge8\pi L,\qquad |b|\ge16\pi/r,\qquad
 \frac{C_h}{2b^2}<\min\{\delta_0/4,a_0r^2/8\},
 \qquad \frac{C_h}{b^2}<\min\{r,h_0\}.
 \tag{17}
\]
Increasing the resulting integer threshold once makes all the
inequalities strict and leaves room for the physical grid midpoint.

For a real charge \(0\le\lambda\le1\), the critical equation is
\[
 t=\frac{2\pi}{b}\{\lambda+i\Phi_{j,t}(t,u)\}.
 \tag{18}
\]
On \(|t|\le4\pi\lambda/|b|\) its derivative has modulus at most
\(1/4\). Since \(\Phi_{j,t}(0,u)=0\), the right side maps this
disk strictly into itself. This gives a unique critical point
\(t_\lambda(u)\), holomorphic in \(u\), and
\[
                     |t_\lambda(u)|\le4\pi\lambda/|b|.
 \tag{19}
\]
Every critical point in \(|t|\le3r\) must satisfy
\(|t|\le(2\pi/|b|)(\lambda+L|t|)\), so also lies in the
contraction disk. There are no other critical points in this chart.

Put \(Q_j(t,u)=\Phi_{j,t}(t,u)/t\), with its removable value at zero.
Equation (15) gives \(|Q_j|\le L\) and \(\Re Q_j\le-a_0\).
The exact imaginary-part formula is
\[
 -\Im t_\lambda(u)=
 \frac{-4\pi^2\lambda\Re Q_j(t_\lambda(u),u)}
 {b^2|1-2\pi iQ_j(t_\lambda(u),u)/b|^2}.
 \tag{20}
\]
It is positive for \(\lambda>0\), for either sign of \(b\), also
on the stated complex \(u\)-disk. The denominator bounds from (17)
give
\[
 \frac{2\pi^2a_0\lambda}{b^2}
 <-\Im t_\lambda(u)<\frac{C_h\lambda}{b^2}.
 \tag{21}
\]
The real derivative of the critical value with respect to \(\lambda\)
is \(\Im t_\lambda\). At \(u=0\), integration therefore proves
\[
 0<M_j+M_\infty-M_{j,b}<\frac{C_h}{2b^2}.
 \tag{22}
\]
The identical bound compares \(\Re\Phi_j(0,u)\) with the selected
critical value at complex \(u\). All these estimates depend only
on the common data, not on \(j\).

## 4. Original tails and the exact trace currents

First expand \(K_N-K_{N,I}\) in its original wire indices. The
complete Hermite norm of \(F_{j,N}\) has rate at most \(M_j\),
by (6) and polynomial Markov bounds. Multiplication, the fixed
\(R^b\), and the original trace have polynomial costs in this norm.
The omitted wire contribution thus has rate at most
\(M_j+M_\infty-\delta_e\), uniformly for every real \(u\).
This uses neither a semisimple replacement nor positivity after
quotient reduction.

Choose a midpoint \(r_N\ge r\) of the physical angle grid with
\(r_N-r=O(N^{-1})\). On the real spectral interval corresponding
to \(r/2\le|t|\le\pi\), (6) gives the loss
\(c(1-\cos(r/2))\). Markov's inequality on this fixed interval
retains it for the first normal, at polynomial cost. The kernel
and its first normal have rate at most \(M_\infty\), uniformly
in the real outside angle. The full original trace nodes with
\(|t|\ge r_N\) consequently have rate at most
\(M_j+M_\infty-\delta_0\). By (17),(22), both discarded parts
lie strictly below the selected rate.

For the remaining exact source put
\[
 f_N(t,u)=F_{j,N}(t)K_{N,I}(t,u),\qquad
 g_N(t)=\sin t\,f_N(t,u)e^{ibNt^2/(4\pi)},\quad
 \eta=(-1)^{N-1}.
\]
At any admissible depth \(h>0\), the original midpoint trace is
\[
\begin{split}
 \mathcal D^{r_N}_{b,N}f_N={}&-rac{N^2C_{N,b}}{\pi i}
  \int_{-r_N-ih}^{r_N-ih}
   g_N(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt\\
 &+\frac{\eta N^2C_{N,b}}\pi
   \int_{-h}^{h}\frac{g_N(r_N+iv)}{4\cosh^2(Nv/2)}\,dv.
\end{split}
 \tag{23}
\]
This is the full identity from
[the exact trace note](research_exact_complete_trace_contour.md), with
the Chebyshev normalization fixed in (1). In particular (23) retains
the endpoint current and the multiplicities of every Fourier charge.

At \(u=0\), choose \(h=-\Im t_*(0)\). The real part of the phase
\(\Phi_j+ibt^2/(4\pi)-it\) is strictly concave on the lower
horizontal segment, by (15). Its unique maximum is the selected
critical point. At the real endpoints evenness and (15) give a loss
at least \(a_0r^2/2\) from \(\Re\Phi_j(0,0)\); (17) preserves
a positive gap from the selected value. At the lower endpoints,
horizontal strict concavity gives another fixed gap, since
\(|\Re t_*|\le r/4\). After folding the upper endpoint current
by oddness of \(g_N\), its exponential rate is bounded by that
same phase at \(\pm r_N-iv\), \(0\le v\le h\).
Its second derivative in \(v\) is \(-\Re\Phi_{j,tt}>0\).
Convexity therefore bounds the whole current by its two endpoint
values; it cannot introduce a larger rate between them.

The rational factor on the lower side is exactly
\[
 \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}
       =e^{-iNt}\bigl(1+O(e^{-Nh})\bigr).
 \tag{24}
\]
The positive depth in (21) need not have a lower bound independent
of \(b\). For each fixed \(b\), it suppresses all higher charges
exponentially. Their starting levels may therefore depend on \(b\),
as the theorem permits.

The discarded contributions are polynomials of degree at most \(D\)
in the outside spectral variable. Their real estimates extend to a
complex angle at the cost \(e^{D|\Im u|}\), by the elementary
Laurent-polynomial maximum principle. Choose a common
\(0<\rho<r\) so this cost, and the common quadratic variation of
the selected action, use less than half the fixed gap in (17).
The local endpoint argument also holds on this disk: (15),(20)
remain valid, and the same contour may be centered at
\(t_*(u)\). This supplies a common source disk, not merely a
holomorphic formula for a putative phase.

Substitution of (5),(8) in (23) now gives the ordinary nondegenerate
Gaussian expansion. Its powers are
\(N^{\alpha_j}N^{-3/2}N^2N^{-1/2}=N^{\alpha_j}\), and its
coefficient is (12). Every factor in that coefficient is nonzero:
the two input amplitudes are nonzero, \(t_*\ne0\) by (18) at unit
charge, \(|t_*|<r/4\), and the real part of the negative Hessian
is positive. This proves (10) with all its stated uniform domains.

## 5. The full real-angle loss and the output strip

Use (9) on every retained horizontal and endpoint contour, keeping
the common factor \(e^{-N\gamma(1-\cos u)}\). The input source
has no outside variable. The bounds just proved at \(u=0\) then
give the same selected rate minus this angular loss for every real
\(u\). The discarded wires and outer trace nodes have the fixed
gap \(3\delta_0/4\) from (17),(22). Since \(1-\cos u\le2\),
one may take, for example,
\[
               c_*\le\min\{\gamma,3\delta_0/8\}.
 \tag{25}
\]
This proves (13) on the whole real period with uniform constants
in the exponent.

The envelope identity is especially useful:
\[
                  \mathcal S_{j,b}'(u)=\psi_u(t_*(u),u).
 \tag{26}
\]
It gives common bounds for all fixed derivatives of the normalized
output action on smaller fixed disks. Separate evenness gives
\(t_*'(0)=0\), so (14) follows directly. Its real part is uniformly
negative by (19). These local bounds yield
\(\Re\mathcal S(x+iy)\le M_{j,b}-c_1x^2+B_2y^2\) on one
common small disk.

For completeness the extension away from that disk uses only the
output degree \(D\), not an estimate of its Newton coefficients.
If \(P(t)\) is an even trigonometric polynomial of degree at most
\(D\), the real bound (25), applied to the polynomial
\(z^DP(t)\), \(z=e^{it}\), and a harmonic majorant on the unit
disk gives
\[
 |P(x+iy)|\le C_{j,b}N^{d_{j,b}}
 e^{N\{M_{j,b}-c_*+c_*e^{-|y|}\cos x+|y|\}}.
 \tag{27}
\]
Outside one fixed neighborhood of \(x=0\), a sufficiently narrow
common strip absorbs the linear \(|y|\) cost into half the angular
gap. Inside that neighborhood the local quadratic estimate applies.
Together they prove (13), after reducing its angular constant and
enlarging its quadratic constant if necessary.

## 6. Consequence for arbitrary inner terminal powers

The family
\(F_{a,N}=H_{a,N}=T(R^a)\), \(|a|\ge2\), satisfies every common
hypothesis above by
[the uniform terminal theorem](research_uniform_terminal_family_and_star_fillings.md).
That result proves a common full expansion disk and a common zero-free
amplitude disk, in addition to its common global strip and curvature
estimates. Its polynomial constants and starting levels may depend
on \(a\), exactly as allowed here. Also \(\alpha_a=0\).

Consequently (10)--(14) apply to the original boundary polynomial
\[
                         T(R^bT(R^a))
 \tag{28}
\]
for all fixed \(|a|\ge2\), \(|b|\ge B_*\), through both
parities. Its amplitude has power \(N^0\). The exact carriers are
\(\varepsilon_{a,N}C_{N,b}\); for the exceptional terminal powers
\(a=\pm2\), their already separated unit factors remain present.
This is an analytic source theorem. Geometric interpretation uses
the original marked gluing of the two pieces and is not inferred
from this estimate alone.

## 7. What this does not imply

The bound on normalized input phases is essential, not a dispensable
technical restriction. Fix \(|p|\ge2\) and any signed \(b\), and
form the canonical original boundary polynomial
\[
                 F_N=\operatorname{can}\bigl(R^{-b}H_{p,N}\bigr).
 \tag{29}
\]
The proved [boundary multiplication theorem](research_boundary_crossing_packet_preservation.md)
says that this is a concentrated full packet for each fixed \(b,p\).
Nevertheless the exact quotient identity gives
\[
                         T(R^bF_N)=T(H_{p,N})=R^p.
 \tag{30}
\]
At every physical node the last polynomial has modulus one. A
nonzero local packet and a strict whole-angle Gaussian loss are
impossible: nodes tending to zero force its exponential rate to
be zero, while nodes tending to any fixed nonzero angle then
contradict the claimed strict loss. A negative candidate rate
already fails at the near-zero nodes; a positive rate contradicts
the nonzero local expansion there.

The input phase in (29) has the additional term
\(-ib t^2/(4\pi)\). Its imaginary curvature cancels precisely
the proposed large crossing in (30). Thus a threshold depending
only on real curvature or on real-axis concentration would be
false. This is an actual source cancellation with all first
normals retained, not an arbitrary analytic counterexample.

Finally, (26) resets normalized phase derivatives, but the proof of
the full expansion chose \(\rho<r\) to preserve the outer-source
gaps on a complex outside disk. Large \(|b|\) does not multiply
those outer real-angle gaps. Consequently the argument does not
prove an unchanged source radius, and hence does not prove a
depth-independent threshold for arbitrary chains. Nor does (28)
settle the infinitely many pairs with fixed short \(b\) and
unbounded \(|a|\). The positive Fourier recurrence for the
specific mixed pair \((2,-2)\) supplies neither of these missing
claims: its characteristic roots already exchange modulus on
the physical circle, as shown in
[the exact Fourier transport note](research_mixed_pair_fourier_transport.md),
Sections 6--8.

A separate [fixed-domain argument](research_fixed_domain_long_power_turns.md)
supplies the missing centered full-edge estimate and proves uniform
iteration for long noninitial powers. It does not extend the theorem
to arbitrary short outer powers.
