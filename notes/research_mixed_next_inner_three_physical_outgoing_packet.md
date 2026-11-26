# The complete inner three-trace at physical outgoing colors

Private finite-source theorem, 8 November 2026. The complete inner
trace has its original nonzero geometric asymptotic at every outgoing
double node in the positive half-period. The proof uses the exact
physical-row identity for the second edge and the uniform slit-plane
asymptotics of those rows. It does not require an off-grid estimate
for that edge on the right connection.

No mathematical numerical evaluation or change to a frozen proof
is used. The conclusion below concerns the stated physical nodes
and the complete endpoint. It is not a uniform asymptotic on a
complex outgoing neighborhood.

## 1. Actual nodes and source

Use the unchanged notation of
[the single-current assembly theorem](research_mixed_next_inner_three_single_remaining_current.md):
\[
\begin{gathered}
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\quad
 q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 u_{j,N}=\pi-(2j+1)\pi/N,\qquad c_j=-2\cos u_{j,N},\\
 K_N^{<,\mathrm{ord}}(x,w)=\sum_{k=0}^{U}e_k(x)e_k(w),\qquad
 K_N^<(t,u)=K_N^{<,\mathrm{ord}}(-2\cos t,-2\cos u),\\
 Q_N(u)=\phi_N^{(x)}
 \left[R_N(x)^3K_N^{\mathrm{ord}}(-2,x)
                           K_N^{<,\mathrm{ord}}(x,-2\cos u)\right].
\end{gathered} \tag{1}
\]
Here \(R_N\) and \(\phi_N\) are the original crossing and full
Hermite trace. The first edge in the definition of \(Q_N\) remains
full.

Let
\[
 \mathcal U_N^{\mathrm{phys}}
   =\{u_{j,N}:0\le j\le U,\ 0<u_{j,N}\le\pi/2\},
 \qquad \mathcal U_N^0=\mathcal U_N^{\mathrm{phys}}\cup\{0\}.
 \tag{2}
\]
The index bound \(j\le U\) includes all the eligible double nodes.
It excludes the odd-level simple node at \(u=0\). The separately
adjoined complete angle zero in \(\mathcal U_N^0\) will be handled
directly rather than called a double node.

For real \(u\in[0,\pi/2]\), retain the original selected data
\[
\begin{gathered}
 t_*(u)=a_*(u)-iH(u),\qquad0<a_*<\pi/2,\qquad1/2<H<1,\\
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,\qquad
 S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u).
\end{gathered} \tag{3}
\]
The phase constant, logarithmic charge, and selected branch are
unchanged.

**Theorem.** Uniformly for \(u\in\mathcal U_N^0\), through all
sufficiently large levels of both parities,
\[
 \boxed{\quad
 Q_N(u)=C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                              (1+O(N^{-1})).
 \quad} \tag{4}
\]
The coefficient \(\mathcal A\) is the original nonzero Gaussian
coefficient (7) of the single-current assembly theorem; its
modulus is uniformly bounded away from zero on the whole real
interval \([0,\pi/2]\).

## 2. The second edge is exactly a physical row

For \(0\le j\le U\), every Newton polynomial \(e_k(c_j)\)
with \(k>j\) vanishes. Therefore
\[
 K_N^{<,\mathrm{ord}}(x,c_j)
     =K_N^{\mathrm{ord}}(c_j,x)
     =F_{j,N}(x)
 \tag{5}
\]
as ordinary polynomial identities in \(x\). The last expression
is the actual physical row in
[the slit-plane source theorem](research_mixed_next_first_short_edge_slit_plane_bound.md).
No interpolation in the outgoing variable has been made.
The full and shortened sums agree here by literal zero factors.

That theorem proves, uniformly over every physical row and every
fixed compact subset \(\mathcal C\) of
\(\Omega=\mathbb C\setminus[2,\infty)\),
\[
 \frac1N\mathscr L_{j,N}(w)=\Psi_{j/N}(w)+o(1),\qquad
 F_{j,N}(w)=e^{\mathscr L_{j,N}(w)},
 \tag{6}
\]
where the logarithm is normalized at \(w=-2\), and
\[
 \Psi_x(w)=\int_0^x
       2\operatorname{arsinh}
       \left(\frac{\sqrt{2-w}}2\cot(\pi r)\right)\,dr .
 \tag{7}
\]
Both endpoint row regimes are included in (6).

We identify the profile with the original two-angle phase,
keeping the half-step of the physical grid. For
\(w_t=-2\cos t\), \(0\le\Re t<\pi\), and bounded lower height,
the principal square root in (7) satisfies
\[
                   \frac{\sqrt{2-w_t}}2=\cos(t/2).
 \tag{8}
\]
On the right connector below, the latter has positive real part,
so (8) fixes the branch.
For \(0\le u\le\pi/2\), set \(x=(\pi-u)/(2\pi)\).
Differentiating (7) gives
\[
 \frac{d}{du}\Psi_{(\pi-u)/(2\pi)}(w_t)
   =-\frac1\pi\operatorname{arsinh}
               \bigl(\cos(t/2)\tan(u/2)\bigr)
   =\psi_u(t,u).
 \tag{9}
\]
At \(u=0\), the normalized slit-plane source gives
\(\Psi_{1/2}(w_t)=\psi(t,0)\).
Integrating (9), on these original principal branches, proves
\[
          \Psi_{(\pi-u)/(2\pi)}(w_t)=\psi(t,u).
 \tag{10}
\]
The same identity holds on a fixed slightly larger real interval
about \([0,\pi/2]\), on every compact first-angle set used below:
all the returns avoid their cuts there.

At a physical angle the exact index is
\[
              \frac jN=\frac{\pi-(u_{j,N}+\pi/N)}{2\pi}.
 \tag{11}
\]
Equations (10)--(11) therefore give the exact relation
\[
        \Psi_{j/N}(w_t)=\psi(t,u_{j,N}+\pi/N).
 \tag{12}
\]
On a fixed compact connector the return in (9) is bounded,
uniformly for \(u\in[0,\pi/2]\) and its small extension.
Hence replacing \(u_{j,N}+\pi/N\) by \(u_{j,N}\) changes
the action by \(O(N^{-1})\), uniformly in the node and level.
The resulting factor in the finite upper bound is only a
fixed constant.

Combining (5)--(6) and (12), for every \(\tau>0\),
\[
 |K_N^<(t,u_{j,N})|
       \le C_\tau e^{N(\Re\psi(t,u_{j,N})+\tau)}
 \tag{13}
\]
uniformly over the physical angles in (2), on every fixed
eligible compact first-angle set. This is an upper bound
with the actual two-angle phase, in contrast to the coarser
complete-period bound with an outside-height cost.

At the additional angle \(u=0\), (13) holds directly by
the first-shortened-edge conclusion of the slit theorem,
since \(K_N^<(t,0)\) is precisely that kernel. Thus (13)
holds uniformly on \(\mathcal U_N^0\).

## 3. The entire remaining right path

Choose for the current in the single-current assembly theorem
the following path:
\[
 \gamma(u):
 \pi/2-iH(u)\longrightarrow5\pi/6-iH(u)
                         \longrightarrow5\pi/6-i/10 .
 \tag{14}
\]
Both segments are in the lower half-plane. The compact rectangle
\[
       \pi/2\le a\le5\pi/6,\qquad1/10\le h\le1,
                       \qquad t=a-ih
 \tag{15}
\]
contains every such path and maps to a fixed compact subset
of \(\Omega\). Thus (13) and the first-shortened-edge bound
are eligible throughout the path, uniformly in all the nodes.

Let
\[
 a_{\max}=\max_{u\in[0,\pi/2]}a_*(u)<\pi/2,\qquad
 \epsilon_R=\frac{(\pi/2-a_{\max})^2}{8\pi}>0.
 \tag{16}
\]
The original
[positive-horizontal phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md)
gives
\[
       \Re\Phi(a-iH(u),u)\le s(u)-\epsilon_R
                           \quad(\pi/2\le a\le5\pi/6).
 \tag{17}
\]
Indeed its quantitative concavity gives this loss through
\(2\pi/3\), and its strictly negative horizontal derivative
continues the comparison thereafter.

For the second segment of (14), the outgoing angle is real.
The two original returns are
\[
 r_0=\operatorname{arsinh}\tan((a-ih)/2),\qquad
 r_1=\operatorname{arsinh}
          \bigl(\tan((a-ih)/2)\cos(u/2)\bigr).
 \tag{18}
\]
Their arguments have positive real part and nonpositive imaginary
part. Both principal returns therefore have nonpositive imaginary
part. Keeping the original crossing and charge,
\[
 \partial_h\Re\Phi(a-ih,u)
     =-\frac1\pi\Im(r_0+r_1)+\frac{3a}{2\pi}-1 .
 \tag{19}
\]
At \(a=5\pi/6\) this is at least \(1/4\), for every
\(h\in[1/10,H(u)]\). Moving upwards from depth \(H(u)\)
to depth \(1/10\) decreases the real phase. Thus (17)
also bounds the entire vertical segment:
\[
                \Re\Phi(t,u)\le s(u)-\epsilon_R
                              \qquad(t\in\gamma(u)).
 \tag{20}
\]

## 4. The literal finite current and the full inner asymptotic

The source in the remaining current is unchanged:
\[
 g_N^{<<}(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)
                                      e^{3iNt^2/(4\pi)} .
 \tag{21}
\]
For all \(t=a-ih\) in (15), the full Fourier multiplier obeys
\[
 |W_N(t)|
       \le\frac{e^{-Nh}}{(1-e^{-N/10})^2}\le C e^{-Nh}.
 \tag{22}
\]
There is no omitted angular charge in (22).
The sine and path lengths are uniformly bounded. Apply (13)
and the first-shortened-edge estimate with, for example,
\(\tau=\epsilon_R/8\) for each factor. The crossing and
the leading decay in (22) give exactly the real phase
\(\Re\Phi(t,u)\). Equations (20)--(22) consequently show
\[
 \frac{N^2}{\pi}\int_{\gamma(u)}
     |g_N^{<<}(t,u)W_N(t)|\,|dt|
        \le C e^{N(s(u)-\epsilon_R/2)}
                              \quad(u\in\mathcal U_N^0).
 \tag{23}
\]
The reserve between the source loss
\(\epsilon_R-2\tau=3\epsilon_R/4\) and
\(\epsilon_R/2\) absorbs the original \(N^2\) prefactor.
The unit scalar \(C_{N,3}\) does not change this bound.

The single-current assembly theorem applies at every angle
in (2). Substituting (23) into its exact reduction proves
(4): the remaining exponential errors are uniformly smaller
than the leading term, whose coefficient is bounded away
from zero. Their relative errors are absorbed into the
already proved \(O(N^{-1})\) Gaussian error. The same original
phase, amplitude, crossing scalar, parity conventions, and
odd central contribution are retained.

## 5. Scope for the outer calculation

The physical-row identity (5) is the reason the missing bound
is available here. At a generic complex outgoing value the
second shortened kernel is not a single physical row, so
(13) cannot be asserted there from the slit theorem.

Formula (4) is uniform over all eligible positive-half-period
double nodes and over the additional complete angle. It does
not estimate the other outgoing nodes with angle greater
than \(\pi/2\), nor provide derivatives with respect to an
off-grid outgoing variable.

In particular a relative \(O(N^{-1})\) error at these nodes
cannot be inserted into a later oscillatory sum without
controlling that sum's cancellation. The result alone gives
neither the required outer asymptotic nor the theorem for
arbitrary fixed short fillings.
