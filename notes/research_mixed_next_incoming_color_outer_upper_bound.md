# Incoming ordinary colors in the complete outer upper bound

Private finite-source theorem, 9 November 2026. The full outer
observation has its original selected-action upper bound, with any
prescribed fixed exponential tolerance, uniformly for every real
incoming ordinary color. The proof bounds the intact finite contours.
It does not assert a nonzero packet at variable incoming color.

The exact incoming degree and the already proved outgoing source
continuation then give a fixed independent complex neighborhood for
the complete right physical remainder. The left remainder and local
geometric integral are separate inputs to a whole-transfer statement.
No mathematical numerical evaluation, import, compilation, or
frozen-source edit is used.

## 1. The exact source and the statement

Retain the original conventions
\[
\begin{gathered}
D=N-1,\quad m=\lfloor N/2\rfloor,\quad M=\lceil N/2\rceil,\quad
U=m-1=D-M,\quad q=e^{\pi i/N},\quad r=q^{-2},\\
\eta_N=(-1)^D,\quad \kappa_N=q^{D^2/2},\quad
C_{N,3}=q^{3D^2/4},\quad
c_j=2\cos((2j+1)\pi/N),\\
K_N(w,X)=\sum_{j=0}^De_j(w)e_j(X),\qquad
K_N^<(w,X)=\sum_{j=0}^Ue_j(w)e_j(X).
\end{gathered}                                                   \tag{1}
\]
All \(\phi_N\)'s below are the original full Hermite functionals.
In particular no first normal or odd simple-node value is omitted.
Define ordinary polynomials in \(X\) by
\[
\begin{split}
Q_{N,w}^{\rm full}(X)
 &=\phi_N^{(x)}[R_N(x)^3K_N(w,x)K_N(x,X)],\\
Q_{N,w}^{\rm sh}(X)
 &=\phi_N^{(x)}[R_N(x)^3K_N(w,x)K_N^<(x,X)],\\
Q_{N,w}^{<<}(X)
 &=\phi_N^{(x)}[R_N(x)^3K_N^<(w,x)K_N^<(x,X)],\\
\mathcal O_{N,k}(w)
 &=\phi_N^{(X)}[R_N(X)^3e_M(X)Q_{N,w}^{\rm full}(X)
                                      T_k(-X/2)] .
\end{split}                                                     \tag{2}
\]
We write \(Q_{N,w}^\star(u)=Q_{N,w}^\star(-2\cos u)\) when
using an angular argument. The incoming degree in every expression
in (2) is at most \(D\), while the outgoing degree of \(Q^{\rm sh}\)
and \(Q^{<<}\) is at most \(U\).

The reference actions in this note remain those at complete incoming
color. Thus \(S(u)=S_3(0,u)\), \(M_3=\Re S(0)\), and
\[
\Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\qquad
u_\delta=\beta_\delta-iK_\delta,\qquad
\Gamma(\delta)=\Re\Psi_\delta(u_\delta),\qquad
\delta=\frac12-\frac{k}{N}.                                    \tag{3}
\]
They are majorants for variable \(w\); they are not declared to
be its stationary actions.

**Theorem 1.** For every \(\varepsilon>0\), there is \(C_\varepsilon\)
such that, at both parities and all sufficiently large \(N\),
\[
\boxed{\quad
 \sup_{w\in[-2,2]}|\mathcal O_{N,k}(w)|
 \le C_\varepsilon
       \exp N\{\Gamma(1/2-k/N)+\varepsilon\},
                     \qquad 0\le k\le U .
\quad}                                                         \tag{4}
\]
The constants may depend on \(\varepsilon\). No relative asymptotic
or lower bound at variable \(w\) is part of (4).

For the actual complete \(343\) references of length at least five,
fix \(Z_*=e^{-2\pi iz_*}\), and write
\[
\Lambda_*=\Re P(-2,z_*),\qquad P(w,z)=\mathcal P_0^+(w,z),\qquad
g_0=\frac1{2\cdot10^{13}}.                                      \tag{5}
\]
The action and its local chart are the original next local source.
Define the exact right physical contribution by
\[
\begin{split}
F_N^+(X,Z)
 &=\sum_{b=M}^D(-q)^b C_{0,N}(r^b,Z)\frac{e_b(X)}{e_M(X)}
   =\sum_{k=0}^Uf_{k,N}(Z)T_k(-X/2),\\
\mathcal R_N^+(w,Z)
 &=\frac1{\kappa_N^2N}\,
       \phi_N[R_N^3e_M Q_{N,w}^{\rm full}F_N^+(\cdot,Z)] .
\end{split}                                                     \tag{6}
\]
Each quotient in (6) is an ordinary polynomial.

**Corollary 2.** There are fixed disks \(B\) about \(-2\) and
\(V\) about \(z_*\) such that
\[
\boxed{\quad
 \sup_{(w,z)\in B\times V}
 \left|e^{-NP(w,z)}
       \mathcal R_N^+(w,e^{-2\pi iz})\right|
       \le C e^{-g_0N/2}.
\quad}                                                         \tag{7}
\]
Every fixed mixed ordinary derivative of this normalized expression
satisfies the same bound on smaller fixed disks, with its own
constant. This is a statement about \(\mathcal R_N^+\) alone.
For a compact family of references the disks and constants may be
chosen uniformly when the original action charts and outgoing
source neighborhoods have their stated uniform compact scope.

## 2. Eligible replacement of the first edge

The adopted
[incoming-color source theorem](research_mixed_next_incoming_color_kernel_upper_bounds.md),
(3), (19), and (23a), supplies the following three facts.

First, on each fixed compact subset of
\(\mathbb C\setminus[2,\infty)\), for every \(\tau>0\),
\[
 \sup_{w\in[-2,2]}|K_N^<(w,-2\cos t)|
       \le C_\tau e^{N\{\Re\psi(t,0)+\tau\}}.                   \tag{8}
\]
The slit primitive and every logarithmic lift here are the original
ones. This applies on every old first-angle path with
\(|\Re t|\le a_F'<\pi\), \(|\Im t|\le1\).
Those paths include the \(N\)-dependent midpoint cuts: their
limiting angles are strictly below \(\pi\).

Second, the exact full first-edge trace difference satisfies
\[
 \sup_{w\in[-2,2]}
 |Q_{N,w}^{\rm sh}(u)-Q_{N,w}^{<<}(u)|
 \le CN^A e^{NE_{\rm tail}},\qquad
 E_{\rm tail}=b_2+\frac23<\frac43,\qquad |\Im u|\le\frac12 .
                                                                    \tag{9}
\]
This is a bound on the sum of the absolute contraction terms.
At even levels these are all radical rows \(b=m,\ldots,D\).
At odd levels they include both every revived radical row
\(b=m+1,\ldots,D\) and the separate \(b=m\) contraction, including
its simple \(-2\) value. In particular (9) does not reuse the
complete-color vanishing of the odd radical coefficients.

Third, the removed far first-angle samples, including their actual
first derivatives, and the entire two-sided inner endpoint vertical
have their old absolute rates
\[
 E_{\rm far}=b_2+\frac23+\frac1{1000},\qquad
 E_{\rm far}+\frac1{2000}<\frac43,                               \tag{10}
\]
uniformly in real \(w\). The sample bound is termwise. Its normal
bound uses the actual spectral degree \(2U<N\), and the endpoint
vertical retains \(1/(4\cosh^2(Nv/2))\) at both signs of \(v\).
There is no slit-plane continuation at the removed point \(t=\pi\).

For clarity the exact inner contour identity underlying these uses is
\[
\begin{split}
g_{N,w}(t,u)&=\sin t\,
 K_N^<(w,-2\cos t)K_N^<(-2\cos t,-2\cos u)
                                      e^{3iNt^2/(4\pi)},\\
W_N(t)&=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\\
Q_{N,w}^{<<}(u)
 &=-\frac{N^2C_{N,3}}{\pi i}\int_{\gamma_{\rm in}}g_{N,w}(t,u)W_N(t)\,dt
       +\mathcal V_{N,w}(u)+\mathcal R_{N,w}(u).
\end{split}                                                     \tag{11}
\]
Here \(\gamma_{\rm in}\) runs from
\(-T_N^{\rm in}-ih_c\) to \(T_N^{\rm in}-ih_c\) in the open lower
half-plane,
\[
 T_N^{\rm in}=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N},
\]
and \(\mathcal V,\mathcal R\) are exactly (23a) of the cited source.
Their signs and \(N^2C_{N,3}/\pi\) factors have not been changed.
The trace has not become a distinct-node trace; in particular its
odd central pole stays inside (11).

Both kernels in \(g_{N,w}\) are even in \(t\), for every \(w\).
Thus the original oddness used in the full trace deformation is
unchanged. The second bare kernel and all of its finite factorial
rows, aliases, cap currents and zero-safe limits are unchanged.
Equation (8) replaces only the first factor in their upper estimates.

## 3. Complete inner envelopes with variable incoming color

Put \(s(u)=\Re S(u)\). We claim, for every \(\tau>0\), uniformly
for real \(w\), the three complete bounds
\[
\begin{array}{ll}
 |Q_{N,w}^{\rm sh}(\beta-iK)|
    \le C_\tau e^{N(s(\beta-iK)+\tau)},
       &0\le\beta\le8/7,\quad0\le K\le2/5,\\[1mm]
 |Q_{N,w}^{\rm sh}(\beta-iK)|
    \le C_\tau e^{N(\max\{s(\beta-iK),33/20\}+\tau)},
       &8/7\le\beta\le\pi/2,\quad0\le K\le2/5,\\[1mm]
 |Q_{N,w}^{\rm sh}(\beta+iK)|
    \le C_\tau e^{N(\max\{s(\beta+iK),17/10\}+\tau)},
       &0\le\beta\le4/3,\quad0\le K\le2/5 .
\end{array}                                                      \tag{12}
\]
We prove these by transferring the upper estimates of the complete
finite contours, rather than substituting \(w\) in an already
computed packet.

On the signed central first-angle horizontal the old second-edge
source theorems give the phase \(\psi(t,u)\), uniformly away from
a fixed small central interval in \(t\). The positive case is the
complete positive-horizontal source; the negative case is its
adopted mixed-height source and bare conjugation. For the reflected
outgoing rectangle, the exact height order
\(H_*(\beta+iK)\le H_*(\beta-iK)\) is the one proved and used in
[the reflected full-source theorem, Sections 2--4](research_mixed_next_reflected_rectangle_full_inner_bound.md).
It licenses the same mixed-height bounds there. None of these
second-edge statements depends on \(w\).

Multiplying those bounds by (8), then retaining the full \(W_N\),
gives the same reference phase
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it.                  \tag{13}
\]
The original signed-horizontal concavity bounds it by \(s(u)\),
with a uniform gap on any fixed part away from \(t_*(u)\).
The central maximum therefore needs only a bounded-length integral
of \(e^{N(s+\tau)}\). A first-edge Gaussian coefficient at variable
\(w\) is unnecessary.

The small interval crossing the imaginary \(t\)-axis must still
be estimated from a finite source. Here is its degree justification.
For \(H=H_*(u)\), put
\[
 \zeta_H(x)=-2\,
 \frac{\cosh H(1-x^2)+2i\sinh H\,x}{1+x^2}.
\]
For each fixed \(w,u\),
\[
 (1+x^2)^{2U}
 K_N^<(w,\zeta_H(x))K_N^<(\zeta_H(x),-2\cos u)                  \tag{14}
\]
is a polynomial of degree at most \(4U<2N\).
On a fixed small positive interval \(\eta\le a\le A\),
\(x=\tan(a/2)\), the preceding source bound and the reference
concavity give a uniform phase gap from \(s\).
The choices in
[the center bridge, (5)--(18)](research_mixed_next_inner_three_center_bridge.md)
apply to (14): its clearing and Chebyshev costs are smaller
than the original degree-\(D+U\) costs.
The extra tolerance in (8) may be chosen smaller than any fixed
fraction of that gap before choosing \(N\).
Restoring \(W_N\) cancels the positive \(NH\) cost exactly as in
(19)--(21) of that proof. The central interval is paid, with its
odd contribution retained. The same argument on the reflected
rectangle uses its compact critical-point family and its proved
concavity, as in the reflected source theorem. All constants are
uniform in real \(w\), since the positive-interval input (8) is
uniform.

For the remaining inner contours we use the following precise
source inventory.

* On the lower positive rectangle, use the complete paths in
  [the independent rectangle theorem, Sections 3--6](research_mixed_next_positive_rectangle_inner_packet.md)
  and its wedge input. The high right segment, vertical at \(2\pi/3\),
  and initial low horizontal use the unchanged complete second-edge
  envelope
  \(\max\{\Re\psi(t,u),(H+K)/2\}\).
  Together with (8) these give exactly its geometric and
  endpoint-sector estimates. The wedge uses the old far low
  continuation; on \(K\ge\beta/2\) the earlier cut
  \(a_1=\arccos(-3/5)\) has ceiling \(1217/720<17/10<s\).
  All other endpoint sectors are below \(s\) by that theorem's
  action floors. The left and far pieces retain their original
  absolute estimates from the same first-edge bound.
* On the lower right half-period, use
  [the half-period envelope, Sections 3--5](research_mixed_next_right_half_period_inner_envelope.md).
  Its high right segment has geometric rate at most \(s\) and
  endpoint rate \(33/20\); height convexity on the vertical retains
  \(\max\{s,33/20\}\), because the low geometric endpoint is below
  \(8/5\). The initial low horizontal decreases in the first angle,
  and the far slit horizontal has rate \(329/200<33/20\).
  The other original currents have rate at most \(s\).
* On the reflected upper rectangle, use all the contours in
  [the reflected full-source theorem, Sections 4--7](research_mixed_next_reflected_rectangle_full_inner_bound.md).
  Its high and vertical geometric sectors have rates at most
  \(\max\{s,121/75\}\), and its endpoint sector is below \(33/20\).
  The left connection has rate below \(8/5\).
  The low right slit horizontal has rate at most \(1217/720\);
  its far vertical has rate below \(9/25\).
  All are bounded by \(\max\{s,17/10\}\).

Every first-angle contour just listed is eligible for (8).
Whenever the original proof used a complete first-edge packet,
only its upper bound is needed here, and (8) supplies that same
bound for the retained shortened first edge. The second-edge
proofs already include both full aliases, their actual residue
and cap factors, and both physical endpoints. We do not remove
any of them by a first-edge substitution. The exact double-pole
\(W_N\), including its higher charges, is retained on each path.

The removed terms (10) and the first-tail error (9) have rates
below \(4/3\). This is below all the constant ceilings just used,
and below the lower positive rectangle's floor \(s>331/200\).
Thus they are eligible in every row of (12).
Choose the finitely many source tolerances smaller than a fixed
fraction of the desired \(\tau\); all original polynomial
prefactors and contour lengths are absorbed in the remaining
tolerance. This proves (12) for the full first-edge source
\(Q^{\rm sh}\), with no relative variable-color packet.

## 4. Physical nodes, including the upper half-period

On the real interval \(0\le u\le\pi/2\), the reference derivative
and cubic guard give
\[
       s(u)\le M_3-\frac{3u^2}{16\pi}.                          \tag{15}
\]
This is exactly the original integrated estimate (14) in
[the far-node theorem](research_mixed_next_outer_far_nodes_and_paired_contour.md);
its proof concerns the reference phase only and is unchanged.

For the remaining physical double nodes \(u_j\ge\pi/2\), use
the full finite proof of
[the upper physical majorant, Sections 2--5](research_mixed_next_inner_three_upper_physical_majorant.md).
At such a node the exact second short kernel is its physical
row \(F_{j,N}(-2\cos t)\).
The original index-monotonicity estimate on its fixed first-angle
rectangle is
\[
 \Re\Psi_{j/N}(-2\cos t)
 \le \Re\Psi_{1/4}(-2\cos t)
                   -\kappa_0(u_j-\pi/2+\pi/N),\qquad\kappa_0>0.
                                                                    \tag{16}
\]
Replace its first-edge estimate (15) by (8). The rectangle remains
a fixed slit compact. All signed horizontal and both full vertical
estimates are consequently unchanged for \(Q^{<<}\), including the
original \(W_N\). Adding (9)--(10) afterwards gives the safe form
\[
 |Q_{N,w}^{\rm sh}(u_j)|
 \le C_\tau\exp N\left\{
 \max\!\left(s(\pi/2)-\kappa_0(u_j-\pi/2),
             E_{\rm tail},E_{\rm far}+1/2000\right)+\tau\right\}.
                                                                    \tag{17}
\]
No favorable slope is assigned to the restored first-tail error.

At noncentral physical double nodes the exact low-edge reduction
gives \(Q_{N,w}^{\rm full}=Q_{N,w}^{\rm sh}\).
Their reflected copies have the same values by evenness.
The odd central term has zero weight in the *outer* observation;
this does not delete the odd central contribution in the inner
source (11).

Since \(M_3>46/25>33/20\), (12), (15), and (17) imply the
coarse complete nodal bound
\[
       \sup_{w\in[-2,2]}|Q_{N,w}^{\rm sh}(u_j)|
                        \le C_\tau e^{N(M_3+\tau)}.             \tag{18}
\]
At all far nodes \(|u_j|\ge3/2\), they give instead
\[
 |Q_{N,w}^{\rm sh}(u_j)|
 \le C_\tau\exp N\left\{
       \max(M_3-189/1408,33/20)+\tau\right\}.                    \tag{19}
\]
Here (15) supplies the original loss \(189/1408\) on
\([3/2,\pi/2]\) and at its endpoint; (17) supplies the rest.
The two flat rates in (17) are less than \(4/3<33/20\).

The reference charged depth gives
\[
 \Gamma(\delta)>M_3-34/275>472/275,\qquad
 \frac{189}{1408}-\frac{34}{275}
       =\frac{4103}{387200}>\frac1{100},\qquad
 \frac{472}{275}-\frac{33}{20}=\frac{73}{1100}>\frac1{100}.
                                                                    \tag{20}
\]
All real crossing and cosine factors have modulus at most one,
the original nodal weights are bounded, and there are \(O(N)\)
nodes. Choose \(\tau\) small and absorb these polynomial factors.
Thus every subset of the original far nodes contributes in
absolute value at most
\[
                   C e^{N(\Gamma(\delta)-1/200)}               \tag{21}
\]
uniformly for all the frequencies in (4) and real \(w\).
This proof retains the flat ceilings; it does not claim a
variable-\(w\) nonzero physical packet.

## 5. Exact outer contour and the uniform upper bound away from zero charge

The algebraic identity
\(e_M(X)(K_N(X,x)-K_N^<(X,x))=0\)
in the original Hermite quotient is independent of \(w\).
It permits \(Q^{\rm sh}\) in the complete outer sampling formula.
With
\[
 u_j=\pi-(2j+1)\pi/N,\qquad
 a_N(u)=
 \begin{cases}
 \sin u,&N\ {\rm even},\\
 \sin u\,\sin(u/2)/\cos^2(\pi/(2N)),&N\ {\rm odd},
 \end{cases}
 \qquad
 \chi_N=\begin{cases}i,&N\ {\rm even},\\-1,&N\ {\rm odd},
 \end{cases}
\]
that exact formula is
\[
 \mathcal O_{N,k}(w)=
 \frac{\chi_N C_{N,3}}2\sum_{j=0}^D
 a_N(u_j)Q_{N,w}^{\rm sh}(u_j)
                  e^{N(3iu_j^2/(4\pi)-i\delta u_j)}.            \tag{22}
\]
It is the consumed-normal formula of the original observation,
not a new distinct-node definition of \(\phi_N\).

Fix \(0<\delta_1\le1/2\) and henceforth take
\(\delta\in[\delta_1,1/2]\). Let
\[
 T_N=\frac{2\pi}{N}
 \left(\left\lceil\frac{3N}{4\pi}-\rho_N-\frac12\right\rceil
                                    +\rho_N+\frac12\right),
 \qquad
 \rho_N=\begin{cases}1/2,&N\ {\rm even},\\0,&N\ {\rm odd}.
 \end{cases}
\]
Thus \(3/2\le T_N<3/2+2\pi/N<\pi/2\) for large \(N\), and
\(\eta_Ne^{-iNT_N}=-1\). Write
\[
\begin{split}
H_N(u)&=\frac1{1-\eta_Ne^{-iNu}},\\
f_{N,w,\sigma}(u)
 &=a_N(u)Q_{N,w}^{\rm sh}(u)
                     e^{N(3iu^2/(4\pi)-i\sigma u)},\\
g_{N,w,k}(u)&=H_N(u)f_{N,w,\delta}(u)(1+e^{-2iku}),\\
\mathcal I_{N,w,k}(\gamma)
 &=\frac{\chi_N C_{N,3}N}{4\pi}\int_\gamma g_{N,w,k}(u)\,du .
\end{split}                                                     \tag{23}
\]
The residue of \(H_N\) at a physical node is \(1/(iN)\).
The original counterclockwise midpoint rectangle and its parity
fold, together with (21), therefore give
\[
 \mathcal O_{N,k}(w)
 =\mathcal I_{N,w,k}([-T_N-iK_\delta,T_N-iK_\delta])
  +\mathcal I_{N,w,k}([T_N-iK_\delta,T_N+iK_\delta])
  +O(e^{N(\Gamma-1/200)}).                                     \tag{24}
\]
This is exactly the old residue normalization \(N/(4\pi)\).
Because \(Q_{N,w}^{\rm sh}\) is even in \(u\), the full meromorphic
paired integrand still obeys
\[
                         g_{N,w,k}(-u)=-g_{N,w,k}(u).          \tag{25}
\]
Both charges, including their factor two at \(k=0\), remain present.

We bound (24) directly, with no local asymptotic inserted.
Use the old positive height-minimizing taper from \(8/7-iK_\delta\)
to \(T_N-i/N\), and its cap to \(T_N+i/N\).
After (25) reflects the rest of the upper vertical, its negative
prefix deforms to
\[
 -T_N-i/N\longrightarrow-4/3-i/N
                       \longrightarrow-4/3-iK_\delta.         \tag{26}
\]
Join (26) to the horizontal segment
\[
                  [-4/3-iK_\delta,\ 8/7-iK_\delta] .           \tag{27}
\]
All deformations except the explicitly retained midpoint cap are
inside the open lower half-plane. The cap crosses the real line
at the original midpoint and no sampling pole. Thus their sum
is exactly the two currents in (24), with no missing connector.

Here is the full upper estimate on this path.

On the positive part of (27), the first line of (12) and the
original two-sided phase descent give
\[
                 \Re\Psi_\delta(x-iK_\delta)\le\Gamma(\delta).
                                                                    \tag{28}
\]
On its negative part, evenness uses the last line of (12).
The geometric sector again satisfies (28). Its constant sector
is at most
\[
          \frac{17}{10}
             -K_\delta\left(\frac{3|x|}{2\pi}+\delta\right)
                  \le\frac{17}{10}<\Gamma(\delta),             \tag{29}
\]
by (20). The joins at \(x=0\) use the closed rectangles in
(12); no off-grid inference from a single physical color is made.
The entire (27) therefore has an upper bound
\(C_\tau e^{N(\Gamma+\tau)}\) before its bounded-length integral.

For (26), the negative height-descent proof (12)--(20) of
[the negative-contour criterion](research_mixed_next_outer_negative_contour_criterion.md)
uses exactly the last line of (12), evenness, and
\(\Gamma>472/275\). It bounds its second segment with a fixed
gap: the geometric part decreases with height, and the constant
part has the favorable sign in (29). Its first segment is paid
from the genuine real-continuum second line of (12), on an
interval containing \([4/3,3/2]\) in its interior. Its exact
degree \(U<N/2\) permits the same fixed Chebyshev ellipse and
height \(1/N\) continuation. This is not interpolation from a
proper subset of physical nodes.

For the positive taper and cap, use
[the taper theorem, Sections 2--5](research_mixed_next_outer_positive_taper_and_midpoint_cap.md).
Its height graph minimizes the original \(V_\delta(x,h)\);
the source it requires is exactly the first two lines of (12).
Its extra endpoint sector has rate below \(83/50<\Gamma\).
The graph is floored at \(h=1/N\), and all its phase changes
there have bounded \(O(1/N)\) cost.
The two-sided cap is again licensed by a bound on a complete
real interval near \(3/2\) and the ordinary degree \(U\).
The entire positive taper and cap thus retain fixed gaps after
the source tolerance is chosen sufficiently small.

On all lower path portions,
\[
 |H_N(x-ih)|\le(1-e^{-1})^{-1},\qquad
 |1+e^{-2ik(x-ih)}|\le2,\qquad Nh\ge1.                          \tag{30}
\]
On the midpoint cap \(u=T_N+iy,\ |y|\le1/N\),
\[
 H_N(T_N+iy)=\frac1{1+e^{Ny}},\qquad
 |H_N|\le1,\qquad |1+e^{-2iku}|\le1+e.                          \tag{31}
\]
The crossing, character, parity amplitudes and cap length have
exactly the bounded costs in the taper proof. In particular no
truncated alias expansion replaces the full denominator near
the real axis.

All paths have uniformly bounded length on the fixed charge
interval. Choose every inner-source allowance smaller than a
fixed fraction of a prescribed \(\varepsilon\) and of the finite
remote gaps, and absorb polynomial factors in the remaining
allowance. Equations (21)--(31) prove
\[
 \sup_{w\in[-2,2]}|\mathcal O_{N,k}(w)|
                 \le C_{\varepsilon,\delta_1}
                         e^{N(\Gamma(\delta)+\varepsilon)}
                \quad(\delta_1\le\delta\le1/2).                \tag{32}
\]
No nonzero coefficient or relative packet at variable \(w\)
has been used.

## 6. Charges approaching zero

Equation (22), or its original cosine-weighted form, and (18)
give for every \(\tau>0\)
\[
 \sup_{w\in[-2,2]}|\mathcal O_{N,k}(w)|
                         \le C_\tau N^A e^{N(M_3+\tau)}
                                      \qquad0\le k\le U.       \tag{33}
\]
The real crossing and characters have unit modulus and the
physical cosine weights have modulus at most one. The bounded
parity weights and \(N\) samples account for only the displayed
polynomial factor. This retains all consumed-normal factors.

Since \(\Gamma\) is continuous at zero with \(\Gamma(0)=M_3\),
choose a fixed \(\delta_1>0\) so small that
\(M_3-\Gamma(\delta)<\varepsilon/4\) for \(0\le\delta<\delta_1\).
Take \(\tau<\varepsilon/4\) in (33), then absorb its polynomial
factor using another \(\varepsilon/4\).
Use (32) on the complementary compact charge interval.
This proves Theorem 1 uniformly over every \(0\le k\le U\).
There is no shrinking-contour or uniform Gaussian assertion
as \(\delta\to0\). The extra even endpoint \(k=N/2\), if the
observation is defined there as well, is exactly zero by its
physical cosine weights.

## 7. The full right attachment on an independent bidisk

The exact identity (5) of
[the boundary-extension source note](research_mixed_next_attachment_boundary_extension_scope.md)
holds as a polynomial identity in \(w,Z\):
\[
\begin{split}
\mathcal R_N^+(w,Z)
 &=\frac1{\kappa_N^2N}
     \sum_{b=M}^D(-q)^b\ell_b(w)C_{0,N}(r^b,Z)\\
 &=\sum_{b=M}^D\frac{F_{34,N}(w,r^b)}{(r;r)_b}C_{0,N}(r^b,Z),
 \qquad
 \ell_b(w)=\phi_N[R_N^3e_bQ_{N,w}^{\rm full}].
\end{split}                                                     \tag{34}
\]
Thus (6) is the original physical right contribution with its
literal \(M,\ldots,D\) endpoints, not an unproved new decomposition.
Its incoming degree is at most \(D\).

The actual
[endpoint-dominance theorem](research_mixed_next_positive_transition_endpoint_dominance.md),
(22), gives
\[
 \mathcal D(t,Z_*)+\Gamma(1/2-t)\le\Lambda_*-g_0,
                                          \qquad0\le t\le1/2. \tag{35}
\]
For each prescribed \(\varepsilon>0\), equations (10)--(13) of
the boundary-extension source note provide a fixed disk
\(\mathcal Z_\varepsilon\) about \(Z_*\) on which
\[
 |f_{k,N}(Z)|
    \le C_\varepsilon N^{A_\varepsilon}
             e^{N\{\mathcal D(k/N,Z_*)+\varepsilon\}},
                                  \qquad0\le k\le U.           \tag{36}
\]
This continuation uses the complete endpoint-uniform outgoing
finite formula and its nonzero analytic symbol. It retains its
factor \(S_b/N\), every row through \(D\), both parity shifts
and the exact positive transition weights. It is not continuation
of a pointwise value bound by holomorphy alone.

Expand (6) in its exact Chebyshev basis and apply (4), (35)--(36):
\[
 \sup_{w\in[-2,2],\,Z\in\mathcal Z_\varepsilon}
 |\mathcal R_N^+(w,Z)|
       \le C_\varepsilon N^{A_\varepsilon}
                    e^{N(\Lambda_*-g_0+2\varepsilon)}.          \tag{37}
\]
This bounds the absolute sum of the complete mode contributions.
The original scalar has modulus \(1/N\), and the number of
modes is at most \(N\); neither changes the action comparison.
No transformed outgoing forcing or terminal coefficient is
removed. In particular (35)--(37) cover the literal highest
degree \(U\) as well as \(k=0\) with its doubled reflected factor.

Here are explicit rate allocations for the independent incoming
continuation. Set \(\varepsilon=g_0/16\) in (37), and absorb its
polynomial factor into \(g_0/16\). This leaves
\(\Lambda_*-13g_0/16\) on the entire incoming real interval
and the same outgoing disk. Let \(\mathcal E_h^{(w)}\) be the
filled spectral ellipse with foci \(\pm2\) and height
\(h=g_0/16\). Since \(\deg_w\mathcal R_N^+\le D<N\), the exact
Chebyshev coefficient bound gives
\[
 \sup_{w\in\mathcal E_h^{(w)}}|\mathcal R_N^+(w,Z)|
 \le(2D+1)e^{Dh}
             \sup_{\xi\in[-2,2]}|\mathcal R_N^+(\xi,Z)|.        \tag{38}
\]
Its exponential cost is at most \(g_0/16\), and its polynomial
factor costs another \(g_0/16\). Thus (38) has rate
\(\Lambda_*-11g_0/16\).

The ellipse contains \(-2\) in its interior. Choose an ordinary
disk \(B\) about \(-2\) inside it and a disk \(V\) about \(z_*\)
whose exponential image lies in \(\mathcal Z_\varepsilon\).
Shrink both inside the original local action chart so that
\[
             \Re P(w,z)\ge\Lambda_*-g_0/16
                              \qquad(w,z)\in B\times V.       \tag{39}
\]
The normalized rate is then at most \(-10g_0/16=-5g_0/8\).
Weakening it to \(-g_0/2\) proves (7).
The normalized exact polynomial composed with \(e^{-2\pi iz}\)
is holomorphic on these fixed disks. Cauchy's formula on smaller
fixed bidisks gives every stated mixed derivative.

This deduction supplies an incoming ordinary-color neighborhood
for the exact right remainder. It makes no new assertion about
a nonzero variable-color outer coefficient. Combining it with
the separately proved left remainder and the original local
integral is a further, explicit full-transfer assembly. Ordinary
closing and stability after arbitrary fixed short fillings are
not inferred here.

## Frozen source bindings

| Source | SHA-256 |
| --- | --- |
| [Incoming-color kernel and tail bounds](research_mixed_next_incoming_color_kernel_upper_bounds.md) | 9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db |
| [Positive rectangle finite packet](research_mixed_next_positive_rectangle_inner_packet.md) | a1520474da2d389cb9cf67e92618f6ca9c552d499f35a039e842f9fc4e5075eb |
| [Right half-period complete envelope](research_mixed_next_right_half_period_inner_envelope.md) | 5994df2b37ebc8bd016300d5285701827add2d8c25cf170629dca00b3181798a |
| [Reflected rectangle full source](research_mixed_next_reflected_rectangle_full_inner_bound.md) | 577fa285f774b4eb93cd2a995f22faff6d0b7f72c20e375b95db57c690ecf85f |
| [Center polynomial bridge](research_mixed_next_inner_three_center_bridge.md) | 0ddff6c7a588128a32f862e113f4e8253d9da6f3e56a4fc3bc5955cab02f7097 |
| [Short-pair exact source transfer](research_mixed_next_inner_three_short_pair_source_transfer.md) | a835236285224a9df4ac41451c84882609b44b223eaa2c7c359f0f48518bccae |
| [Upper physical half-period majorant](research_mixed_next_inner_three_upper_physical_majorant.md) | 6fd4d8c0d67e184312f0d1106b112ac00a965f7d40716aae8ac7b502eb709c18 |
| [Far physical nodes and exact paired contour](research_mixed_next_outer_far_nodes_and_paired_contour.md) | 4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7 |
| [Positive taper and full midpoint cap](research_mixed_next_outer_positive_taper_and_midpoint_cap.md) | 630fc00e67395f04fd44b8c32618202c67b9f457900d0cced44ed8f6f0da3e22 |
| [Negative contour and exact oddness](research_mixed_next_outer_negative_contour_criterion.md) | ae0bbd44353baa5f6679d9c3b7ea3d61f40490dcdfdf7837f505c45dd75ea99a |
| [Two-sided phase descent](research_mixed_next_charged_curve_two_sided_descent.md) | 102daa403519833ca13414ca2e0e20f351c572a5740ab9ca6ffb1c204d2eda7f |
| [Complete action lower bound](research_inner_three_complete_action_lower_bound.md) | dd5153c7eabefe865b6fd1ed03e6f2fb08c63283f20fd48a999b625ec4836c42 |
| [Actual endpoint dominance and attachment gap](research_mixed_next_positive_transition_endpoint_dominance.md) | 85d5c740d1c8c3481f5d6be5dd29d826879a366f5d07a079700cb4cbd7c92804 |
| [Exact boundary identities and outgoing continuation](research_mixed_next_attachment_boundary_extension_scope.md) | 74bca3cd11850a0ab0b507de69fb42ae6e73d61434dc1bc67b1872bd5710d54a |

