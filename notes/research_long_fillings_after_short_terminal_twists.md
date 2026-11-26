# Long fillings after terminal twists of two crossings

Research proof, 2 November 2026. The frozen manuscripts are unchanged.
This note proves a partial-filling theorem for the original Kashaev
invariant of a circle-tree knot. The short fillings are at chosen
terminal vertices and have signed crossing power $2$ or $-2$. All
other crossing powers are fixed before the quantum level tends to
infinity and are sufficiently large independently in sign and size.

The argument uses the exact finite tree contraction and the marked
cell identities already proved in the circle-tree papers. Its new
short-boundary input is the theorem in
[A two-crossing terminal filling with a free boundary](research_two_crossing_terminal_filling.md).
That theorem estimates the actual open polynomial, including its
global remainder. A volume formula for a closed short tangle would
not provide the input needed here.

## 1. The diagrams and the theorem

Let $\mathcal T=(V,E)$ be a fixed finite ordered tree with at least
one edge. Each vertex carries an original crossing-circle tangle,
and every joining edge is the prescribed physical quarter-turn.
The ordered stacks, disk frames, strand orientations, cylindrical
closure and reduced cut are those of the
[circle-tree geometry paper](../papers/circle-tree-geometry/main.tex).
There are no bare product junctions.

For each vertex $v$, retain a half-twist
$\eta_v\in\{-1,0,1\}$. If $p_v\in\mathbb Z$ is the surgery
coefficient in its original disk framing, the physical crossing
power is

\[
 n_v=\eta_v-2p_v.
\]

The filled primitive curve is the original
$\mu_v+p_v\lambda_v$. Fix the parity pattern so that the literal
strand tracing gives one main component and no internal closed
component. These conditions specify a knot template, not merely an
abstract tree.

Choose a subset $\mathcal L$ of the original terminal vertices.
At every $\ell\in\mathcal L$, require $\eta_\ell=0$ and fix

\[
 n_\ell=2\sigma_\ell,\qquad \sigma_\ell\in\{1,-1\}.
\]

Thus $p_\ell=-\sigma_\ell$. Assume that at least one vertex
remains. Write

\[
 V_0=V\setminus\mathcal L,\qquad
 E_0=\{vw\in E:v,w\in V_0\},\qquad
 r=|V_0|,\qquad e_0=|E_0|=r-1.
\]

For a remaining vertex $v$, let $m_v$ be the number of selected
leaves attached to it and let $s_v$ be the sum of their signs:

\[
 m_v=\#\{\ell\in\mathcal L:\ell\sim v\},\qquad
 s_v=\sum_{\substack{\ell\in\mathcal L\\\ell\sim v}}
                    \sigma_\ell.
\]

**Theorem.** There is a finite threshold $B$, depending on this
fixed marked template and the chosen short-leaf signs, such that
the following holds. Choose any fixed remaining integer powers
$n_v\equiv\eta_v\pmod2$ with $|n_v|\ge B$, independently in
sign and relative size. The resulting knot $K$ is hyperbolic, and
its reduced zero-framed Kashaev invariant satisfies

\[
 \langle K\rangle_N
 =\Omega_N N^{3/2}D\,e^{N S}
       \bigl(1+O_{\mathbf n}(N^{-1})\bigr),
 \qquad |\Omega_N|=1,\qquad D\ne0,
                                                        \tag{1}
\]

through all sufficiently large integer levels, including both
parities. The constants $S$ and $D$ are independent of $N$, and

\[
 2\pi\Re S=\operatorname{Vol}(S^3\setminus K).
                                                        \tag{2}
\]

In particular the original Kashaev volume identity holds for these
knots. The statement also permits $\mathcal L=\varnothing$, in
which case it recovers the corresponding long-filling theorem.
The threshold is not asserted to be uniform over different trees.

The rest of the note proves the analytic and geometric parts of
this statement. No assertion is made here about a short internal
vertex, an arbitrary fixed short power, or a component with no free
filling parameter left.

## 2. Exact elimination of the selected leaves

Fix $N\ge3$, put $d=N-1$ and $q=e^{\pi i/N}$, and use

\[
 S_k=\prod_{j=1}^k2\sin(\pi j/N),\qquad
 e_k(z)=S_k^{-2}\prod_{j=0}^{k-1}
             \{2\cos((2j+1)\pi/N)-z\}.
\]

The pair algebra is $\mathbb C[z]/(T_N(z)+2)$, where $T_N$ is
the monic Chebyshev polynomial, and the closing functional is

\[
 \phi(f)=(-1)^dN^2[z^d]\operatorname{rem}_{T_N+2}f,
 \qquad \phi(e_i e_j)=\mathbf1_{i+j=d}.
\]

At the complete meridian, the physical turn reverses the Newton
coefficients. The actual positive crossing is

\[
 R=q^{d^2/2}\sum_{k=0}^d(-q)^k e_k.
\]

Define the complete edge kernel and the terminal message by

\[
 K_N(t,u)=\sum_{k=0}^d e_k(-2\cos t)e_k(-2\cos u),
\]

\[
 H_{n,N}(u)=\sum_{k=0}^d\phi(R^n e_k)e_k(-2\cos u).
\]

Summing each selected terminal edge in the original finite
contraction gives the exact remaining source

\[
 B_N(\mathbf t)=
 \prod_{vw\in E_0}K_N(t_v,t_w)
 \prod_{\ell\in\mathcal L}
                   H_{2\sigma_\ell,N}(t_{p(\ell)}),       \tag{3}
\]

where $p(\ell)$ is the remaining neighbor of $\ell$. It is an
entire, separately even, $2\pi$-periodic trigonometric polynomial.
Its degree in $-2\cos t_v$ is at most
$(\deg_{E_0}(v)+m_v)(N-1)$. We retain this raw polynomial; a
reduction modulo the spectral relation before estimating it could
change its values away from the interpolation nodes.

For a polynomial $f(t)=f^\sharp(-2\cos t)$ define the physical
crossing trace

\[
 \mathcal D_{n,0,N}f=\phi(R^n f^\sharp).
\]

With $w(D)$ the oriented writhe of the original diagram, the exact
reduced invariant is

\[
 \langle K\rangle_N
 =\zeta_N\left(\prod_{v\in V_0}
                      \mathcal D_{n_v,0,N}^{(v)}\right)B_N,
 \qquad \zeta_N=q^{d^2w(D)/2},\qquad |\zeta_N|=1.        \tag{4}
\]

Equations (3) and (4) are finite algebraic identities, valid at
both parities and composite levels. They retain the first
derivatives at double spectral roots. They use the exact finite
source identity in
[the circle-tree source section](../papers/circle-tree-volume/finite-bounds.tex).

## 3. The complete local expansion and the global source bound

Let $v_{\rm oct}$ be the regular ideal-octahedron volume. The
edge phase is the separately even holomorphic function determined
near zero by

\[
 \psi(0,0)=\frac{v_{\rm oct}}\pi,\qquad
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                         (\tan(t/2)\cos(u/2)).
\]

The existing full-kernel theorem gives

\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                           (1+O(N^{-1})),               \tag{5}
\]

uniformly and holomorphically on a fixed bidisk. Its amplitude is
nonzero there after shrinking the disk. Its global real and thin
complex bounds retain a positive angular loss in both variables.
These statements precede the degree-and-twist hypotheses in
[the edge analysis](../papers/circle-tree-volume/edge-packet.tex).

The short-leaf theorem supplies, for $\sigma=\pm1$,

\[
 H_{2\sigma,N}(u)
 =\frac{e^{-\sigma i\pi/4}}{2\sqrt{\cos(u/2)}}
   \exp N\left\{\frac12\psi(u,0)
              +\frac{\sigma i\pi}{8}
              -\frac{\sigma i u^2}{8\pi}\right\}
   (1+O(N^{-1})),                                      \tag{6}
\]

with a uniform holomorphic error, and

\[
 |H_{2\sigma,N}(a+ib)|\le CN^A
 \exp N\left\{\frac{v_{\rm oct}}{2\pi}
                   -c(1-\cos a)+C_0b^2\right\}         \tag{7}
\]

on a fixed thin strip about the entire real circle. In particular,
(6) is an estimate of the whole finite message, not of one
formally selected summand.

Define

\[
 \Psi(\mathbf t)=\sum_{vw\in E_0}\psi(t_v,t_w)
                    +\frac12\sum_v m_v\psi(t_v,0),
 \qquad \beta_v=\frac{s_v}{2}.                          \tag{8}
\]

Multiplying (5) and (6) gives

\[
 B_N(\mathbf t)=\epsilon_N N^\alpha a(\mathbf t)
 \exp N\left\{\Psi(\mathbf t)
                    -\frac{i}{4\pi}\sum_v\beta_vt_v^2\right\}
 (1+O(N^{-1})),                                        \tag{9}
\]

where

\[
 \epsilon_N=\exp\left(\frac{i\pi N}{8}
                             \sum_{\ell\in\mathcal L}\sigma_\ell\right),
 \qquad \alpha=-\frac32e_0.
\]

The amplitude $a$ is the product of the amplitudes in (5) and
(6), so it is holomorphic and nonzero on a smaller polydisk.
The real phase satisfies

\[
 \Phi:=\Psi(0)=\frac{(2e_0+|\mathcal L|)v_{\rm oct}}{2\pi},
 \qquad
 \Psi''(0)=-\operatorname{diag}(a_v),
 \quad a_v=\frac{\deg_{E_0}(v)+m_v/2}{2\pi}>0.         \tag{10}
\]

Positivity follows because a remaining vertex either meets a
remaining edge or, when the remaining tree has one vertex, meets
at least one selected leaf. Multiplying the full-kernel bounds
and (7) yields constants $c,b,C_0>0$ such that

\[
 |B_N(\mathbf x+i\mathbf y)|\le CN^A
 \exp N\left\{\Phi-c\sum_v(1-\cos x_v)
                              +C_0\sum_v y_v^2\right\},
 \quad |x_v|\le\pi,\quad |y_v|\le b.                  \tag{11}
\]

All constants in (9)--(11) depend on the fixed partially filled
template, not on the later remaining powers.

## 4. A filling lemma allowing the fixed quadratic phase

We prove the analytic statement needed to pass from (9)--(11)
to the complete original evaluation. The use of the original
integer crossings in this proof is important: the numbers
$n_v-\beta_v$ introduced below are not fractional surgery slopes.

**Lemma.** Suppose an entire, separately even, periodic polynomial
source satisfies (9)--(11), with $\Psi$ real on real arguments,
$a(0)\ne0$ and the diagonal positive Hessian constants (10).
The separate degrees may be any fixed multiples of $N-1$.
For all independently sufficiently large fixed signed integers
$n_v$, put

\[
 \nu_v=n_v-\beta_v,\qquad
 T_{\boldsymbol\ell}(\mathbf t)
   =\Psi(\mathbf t)+\frac{i}{4\pi}\sum_v\nu_vt_v^2
                                      -i\sum_v\ell_vt_v.\tag{12}
\]

The unit-charge phase has a unique small critical point
$\mathbf t_*$, and the full physical trace evaluation is

\[
 \begin{aligned}
 \left(\prod_v\mathcal D_{n_v,0,N}^{(v)}\right)B_N
 ={}&\epsilon_N\prod_v C_{N,n_v}(0)
           N^{\alpha+3r/2} D\,e^{N T_{\mathbf1}(\mathbf t_*)}
           (1+O_{\mathbf n}(N^{-1})),\\
 D={}&\left(-\frac1{\pi i}\right)^r(2\pi)^{r/2}
 \frac{a(\mathbf t_*)\prod_v\sin t_{*,v}}
      {\sqrt{\det[-T_{\mathbf1}''(\mathbf t_*)]}}\ne0,    \tag{13}
 \end{aligned}
\]

where
$C_{N,n}(0)=q^{n(N-1)^2/4}$. The Gaussian branch is determined
by translating the real integration box. The entire error in
(13) includes all nonunit Fourier charges and endpoint currents.

### Exact finite grids and their Fourier charges

Introduce temporary independent parameters $\sigma_v$. At a
generic parameter, the actual crossing trace is exactly

\[
 \mathcal D_{n,\sigma,N}f
 =\frac{(-1)^{N-1}N C_{N,n}(\sigma)}{\sin(2\pi\sigma)}
 \sum_{j=0}^{N-1}\sin\tau_j\,f(\tau_j)
                       e^{inN\tau_j^2/(4\pi)},           \tag{14}
\]

\[
 \tau_j=\frac{2\pi}{N}\left(\frac{N-1}{2}+\sigma-j\right),
 \qquad C_{N,n}(\sigma)=q^{n((N-1)^2/4-\sigma^2/2)}.
\]

This formula is polynomial interpolation followed by the actual
closing functional. It holds for every polynomial degree; its
holomorphic limit includes the double-root derivatives. Choose
$0<\rho<1/2$ and first put $|\sigma_v|=\rho$.
The source remains the fixed polynomial $B_N$ during this device;
no theorem about the physical invariant at a moving main meridian
is assumed or concluded.

The kernel

\[
 K_\sigma(t)=\frac{iN e^{iNt}}
             {e^{iNt}-(-1)^{N-1}e^{2\pi i\sigma}}
\]

has residue one at the grid in (14). Integrate it around the
rectangle translated by $2\pi\sigma/N$, retaining its vertical
sides. On those sides its value is
$iN e^{-Nv}/(1+e^{-Nv})$. Expand it geometrically on the two
horizontal sides and truncate each expansion there. Keep every
omitted infinite tail on its original translated horizontal
contour. Only the finitely many retained terms are moved to fixed
real intervals, keeping their endpoint connectors. Reflecting one
of these retained intervals uses the separate evenness of the
source and the odd sine factor. It produces positive integer
charges with coefficients

\[
 c_{\ell,N}(\sigma)=(-1)^{(N-1)(\ell-1)}
                   U_{\ell-1}(\cos2\pi\sigma),
 \qquad c_{1,N}=1.                                    \tag{15}
\]

The resulting finite-charge functional is

\[
 \mathcal P_{n,\sigma,N}^{L}f
 =-\frac{N^2C_{N,n}(\sigma)}{\pi i}
 \sum_{\ell=1}^{L}c_{\ell,N}(\sigma)
 \int_{-\pi}^{\pi}\sin t\,f(t)
                       e^{N(in t^2/(4\pi)-i\ell t)}dt.  \tag{16}
\]

The exact contour also retains the infinite horizontal tails,
the original endpoint currents, and the finitely many connectors
just described. No infinite family of endpoint connectors is
created. The zero-frequency real integral is zero by oddness;
its endpoint currents are not discarded.

Only the original integer $n$ occurs in (14)--(16). In particular,
we have not globally multiplied the source by
$\exp(iN\sum_v\beta_vt_v^2/(4\pi))$: that operation would
destroy its periodicity and invalidate this Fourier step.

### The infinite charge tails

Set $c_2=2c/\pi^2$, so (11) supplies a real loss $c_2t^2$ in
each coordinate. Choose a small fixed $a_0>0$ and put

\[
 L_v=\lfloor a_0|n_v|\rfloor,\qquad
 y_v=A_0a_0/|n_v|.
\]

On a lower horizontal side, with other variables real or on
their actual $O(N^{-1})$ translated grids, the real rate for
an omitted positive charge is bounded by

\[
 \Phi-c_2t^2+\frac{|n_v||t|y_v}{2\pi}
                         -\ell y_v+C_0y_v^2.
\]

Maximizing in $t$ bounds the first two variable terms by
$n_v^2y_v^2/(16\pi^2c_2)$. Since $\ell\ge L_v+1>a_0|n_v|$,
the rate is at most

\[
 \Phi+a_0^2\left\{\frac{A_0^2}{16\pi^2c_2}-A_0
                     +\frac{C_0A_0^2}{n_v^2}\right\}
                 -(\ell-L_v-1)y_v.
\]

Choose $A_0$ so the first positive term is at most $A_0/4$,
then enlarge the lower bound on $|n_v|$ so the last one is at
most $A_0/4$. This gives a fixed loss $A_0a_0^2/2$.
The omitted tails are still on the original translated contours.
There the upper Fourier character is
$e^{-2\pi i\ell\sigma}e^{i\ell Nt}$ and the lower one is
$e^{2\pi i\ell\sigma}e^{-i\ell Nt}$. Substituting
$t=w+2\pi\sigma/N$ cancels the parameter character exactly.
Thus the tail is geometrically summable with ratio $e^{-Ny_v}$,
without an unestimated parameter growth or an infinite connector
family. The source and physical chirp at this $O(N^{-1})$
translation change only the prefactor for each fixed power.
The coefficients (15) occur only in the retained finite sum;
their bound $\ell e^{2\pi\rho(\ell-1)}$ is harmless there.

At the original endpoints the source has a fixed angular loss.
The physical chirp costs $O(|n_v|y_v)=O(a_0)$, and the retained
charge connectors cost $O(L_vy_v)=O(a_0^2)$. Reducing $a_0$
preserves a fixed positive endpoint loss, including the zero-mode
current.

To pass to all variables, telescope the product of exact traces
against the product of (16). Earlier factors are finite real
integrals; later factors are the exact finite grid sums. They
have polynomial cost in $N$, with constants depending on the
fixed powers. No spectator is moved to another coordinate's
slope-dependent height. The whole omitted contribution therefore
has rate at most $\Phi-\gamma$ for a fixed $\gamma>0$.

This difference is holomorphic in each temporary $\sigma_v$.
The maximum principle extends its bound from the parameter circles
to their disks, including $\sigma_v=0$. Thus the estimate controls
the complete Hermite trace, not just values at distinct nodes.

### Critical points for every retained charge

For sufficiently large powers, $|\nu_v|\ge|n_v|/2$, so every
retained charge satisfies $\ell_v/|\nu_v|\le2a_0$.
Inside the local box, insert (9) into (16); this is where the
effective coefficient $\nu_v$ enters. Separate evenness gives

\[
 \Psi_v(\mathbf t)=t_v Q_v(\mathbf t),\qquad Q_v(0)=-a_v.
\]

Shrink the polydisk until $\Re Q_v<-a_v/2$. The critical
equation of (12) becomes

\[
 t_v=\frac{2\pi(\ell_v/\nu_v)}
                      {1-2\pi iQ_v(\mathbf t)/\nu_v}.    \tag{17}
\]

It is a contraction on a fixed small polydisk when $a_0$ is
small and the remaining powers are large. This is uniform over
all retained charges and independent signs and ratios. The unique
solution satisfies

\[
 \Im t_v=
 \frac{4\pi^2\ell_v\Re Q_v(\mathbf t)}
      {\nu_v^2|1-2\pi iQ_v(\mathbf t)/\nu_v|^2}<0.       \tag{18}
\]

Thus each coordinate and its sine are nonzero. Moreover
$-\Re\Psi''$ is positive definite on the small polydisk, so
the negative phase Hessian has positive definite real part.

Let $S_{\boldsymbol\ell}$ be the stationary value, and vary
the positive charges continuously. Stationarity gives

\[
 \partial_{\ell_v}\Re S_{\boldsymbol\ell}=\Im t_v.
\]

Using (18), then integrating one charge at a time, gives
constants $b_v>0$ such that

\[
 \Re S_{\boldsymbol\ell}\le\Re S_{\mathbf1}
       -\sum_v\frac{b_v}{\nu_v^2}(\ell_v^2-1).          \tag{19}
\]

Integration from zero charge to unit charge also gives
$\Phi-\Re S_{\mathbf1}=O(\sum_v\nu_v^{-2})$.
None of these steps requires $\nu_v$ to be integral.

### Deformation of the finite integrals and noncancellation

The complement of a small real box has a fixed loss by (11).
Translate the box by the imaginary part of its critical point.
Locally, the phase is real on the real box and satisfies

\[
 \Re\Psi(\mathbf x-i\mathbf y)
       \le\Phi-c_3|\mathbf x|^2+C_3|\mathbf y|^2.
\]

The effective chirp contributes at most
$\sum_v|\nu_vx_vy_v|/(2\pi)$. The heights are
$O(\ell_v/\nu_v^2)$. Young's inequality absorbs this cost into
half the real quadratic loss plus
$C\sum_v(\ell_v/\nu_v)^2$. On each connecting face, at least
one real coordinate stays at the fixed box boundary. Reducing
$a_0$ relative to that boundary size preserves a fixed loss.
The Fourier factors decrease under the downward displacement.
These estimates justify using the entire local holomorphic
expansion, including its remainder, on the translated contour.

Gaussian integration gives (13). Its amplitude is nonzero because
$a(\mathbf t_*)\ne0$, every sine is nonzero, and the Hessian is
accretive. The unit charge has coefficient exactly one in every
coordinate by (15). There is no remaining sum of equal-action
sign choices.

The other retained charges are smaller by (19). All discarded
regions and currents have fixed losses from $\Phi$. Enlarge the
power threshold so that the unit-charge drop from $\Phi$ is less
than half each fixed loss. These errors are then below that same
filled action. This proves the lemma for the full original trace.

Applying it to (3), the power of $N$ is

\[
 \alpha+\frac32r=-\frac32(r-1)+\frac32r=\frac32.        \tag{20}
\]

## 5. The partially filled metric and its primitive periods

It remains to identify the real stationary action with the actual
knot-complement volume. We retain all original marked peripheral
curves in this comparison.

The short-leaf theorem constructs a positive primitive cone path
from the complete augmented leaf to its filling with crossing
power $2\sigma$. Its endpoint has cone angle $2\pi$, positive
core length and a holomorphic continuation in the parent angle
near zero. Its marked stationary action is exactly

\[
 S^{\rm geom}_{2\sigma}(u)
 =\frac12\psi(u,0)-\frac{3\sigma i\pi}{8}
                         -\frac{\sigma i u^2}{8\pi}.    \tag{21}
\]

The finite source phase in (6) differs from (21) by
$\sigma i\pi/2$, a specified unit phase. Each such filled leaf
and its original edge block has volume $v_{\rm oct}$ when the
parent is complete. The path retains positive ordered tetrahedral
shapes, the original primitive periods and complete main cusps.
These are the conclusions proved in Section 8 of
[the short-leaf note](research_two_crossing_terminal_filling.md).

Fill all selected leaves by these paths while every remaining
angle is zero. The paths act in their disjoint edge blocks;
$\psi_u(t,0)=0$ leaves every unfilled peripheral period zero.
The result is the complete partially filled exterior $Y'$, with

\[
 \operatorname{Vol}(Y')=(2e_0+|\mathcal L|)v_{\rm oct}.
                                                        \tag{22}
\]

Here is the absolute volume calculation for this first stage. For
one selected leaf of sign $\sigma$, let $t_\sigma(\lambda)$ be its
positive cone path at complete parent, with cone angle
$2\pi\lambda$. Its stationary action is

\[
 C_\sigma(\lambda)
 =\psi(t_\sigma(\lambda),0)
       +\frac{i\sigma}{2\pi}t_\sigma(\lambda)^2
       -i\lambda t_\sigma(\lambda).
\]

Stationarity gives
$d\Re C_\sigma/d\lambda=\Im t_\sigma$. The core length is
$-2\Im t_\sigma$, so Schläfli's formula gives the volume
derivative $2\pi\Im t_\sigma$ along the same marked path.
At $\lambda=0$, this edge block consists of two regular ideal
octahedra and has volume
$2v_{\rm oct}=2\pi\Re C_\sigma(0)$. At $\lambda=1$,
(21) gives $\Re C_\sigma(1)=v_{\rm oct}/(2\pi)$.
The volume therefore decreases by exactly $v_{\rm oct}$ for
each selected leaf. The remaining edge blocks stay at their
complete values during this stage. Starting from the original
volume $2|E|v_{\rm oct}$ proves (22), because
$|E|=e_0+|\mathcal L|$.

The use of Schläfli here concerns the actual cone metric. The
[geometric paper's volume differential and fundamental-chain comparison](../papers/circle-tree-geometry/main.tex),
equations `ctg:volume-differential` and `ctg:chain-volume`, apply
along a positive family with the full marked periods; their
proofs do not require the separate large-power criterion. The
tetrahedral volumes are continuous at the complete endpoint, so
the differential comparison also fixes the constant there. Main
cusps remain complete throughout: in a short block
$k=\cos(t_\sigma/2)$ has positive real part, and its corner
translation $E-1=2ik/(1-ik)$ never vanishes. Positivity and the
original edge returns give the same nonsingular Euclidean cusp
links as in the geometric paper's metric construction.

For small remaining angles define its continued potential

\[
 \begin{aligned}
 P(\mathbf t)
   &=\sum_{vw\in E_0}\psi(t_v,t_w)
                  +\sum_{\ell\in\mathcal L}
                     S^{\rm geom}_{2\sigma_\ell}(t_{p(\ell)})\\
   &=\Psi(\mathbf t)-\frac{i}{4\pi}\sum_v\beta_vt_v^2
                      -\frac{3i\pi}{8}\sum_\ell\sigma_\ell.
                                                        \tag{23}
 \end{aligned}
\]

The derivative of each eliminated leaf action is the derivative
of the original edge potential with respect to its parent: the
leaf derivative cancels by stationarity. Therefore the original
marked peripheral identities continue as

\[
 U_v=-2\pi P_v-i\eta_vt_v,\qquad V_v=2it_v,
\]

\[
 U_v+p_vV_v=-2\pi\left(P_v+\frac{in_v}{2\pi}t_v\right).
                                                        \tag{24}
\]

Here $U_v,V_v$ are the full continued logarithmic periods of
$\mu_v,\lambda_v$. They are not eigenvalue logarithms with an
unrecorded half factor. Their lifts agree with the original ones
along the short-leaf paths. At $\mathbf t=0$ all remaining
chosen logarithms are zero. To verify that they give the actual
periods when the remaining fillings begin, apply the
[geometric paper's subsection “Fixing the winding integer”](../papers/circle-tree-geometry/main.tex)
at the complete partially filled exterior $Y'$. Let $c$ denote
the remaining cone parameter used in Section 6. In a continuous
affine frame, the longitude acts as
$z\mapsto a_v(c)z+b_v(c)$, where
$a_v(c)=e^{V_v(c)}\to1$. Its complete Euclidean cusp has a
nonzero primitive longitude translation, so $b_v(0)\ne0$.
The second fixed point
$q_v(c)=b_v(c)/(1-a_v(c))$ consequently tends to infinity.

For either fixed primitive path $\gamma$, its developed image
and Euclidean length remain bounded by constants $B_v,L_v$ as
$c\downarrow0$. The logarithmic-link period therefore satisfies

\[
 |P_\gamma(c)|\le\frac{L_v}{|q_v(c)|-B_v}\longrightarrow0,
\]

which is the estimate `ctg:period-limit` of the geometric paper.
The differences between these actual periods and the chosen
$U_v,V_v$ are continuous multiples of $2\pi i$. Both sides
tend to zero, so the multiples vanish near $c=0$ and remain
zero along the positive remaining-filling path. This establishes
the full-period interpretation of (24) without resetting a
principal logarithm at $Y'$.

## 6. Completing all remaining primitive fillings

For $0\le c\le1$, solve

\[
 P_v(\mathbf t)+\frac{in_v}{2\pi}t_v=ic.
                                                        \tag{25}
\]

By (23), these are the same critical equations as (12) with
every charge equal to $c$ and effective coefficient
$\nu_v=n_v-\beta_v$. The contraction argument (17) applies
uniformly for $c\in[0,1]$ once all remaining powers are large.
It gives $\mathbf t(0)=0$, small angles throughout the path,
and $\Im t_v(c)<0$ for $c>0$ by (18).

The original core-edge shapes are positive near zero. The
eliminated short-leaf shapes remain in a positive neighborhood
of their smooth filled endpoints, because their parent angles
stay small. Their primitive meridians continue to have period
$-2\pi i$ and their core lengths stay positive. All original
face and edge gluing identities still hold, and the main cusps
remain complete.

For each remaining auxiliary torus, (24) and (25) give

\[
 U_v+p_vV_v=-2\pi i c,
 \qquad \ell_v(c)=\Re V_v=-2\Im t_v(c)>0.              \tag{26}
\]

The primitive solid-torus completion from the geometric paper
therefore gives cone angle $2\pi c$. At $c=1$ this completion
is smooth and complete on the actual filled exterior. The local
disk surgery still restores the original powers
$n_v=\eta_v-2p_v$ in $S^3$. By the stipulated strand matching,
the completed manifold is $S^3\setminus K$.

The coefficients $\nu_v$ have only organized the stationary
equations. Equations (24)--(26) use the original integer surgery
coefficients $p_v$ and the original primitive basis throughout.

## 7. Absolute volume and the invariant asymptotic

Define the stationary geometric action along the remaining cone
path by

\[
 \mathcal C(c)=P(\mathbf t(c))
       +\frac{i}{4\pi}\sum_v n_vt_v(c)^2
                         -ic\sum_v t_v(c).              \tag{27}
\]

Stationarity gives

\[
 \frac{d}{dc}\Re\mathcal C(c)=\sum_v\Im t_v(c).
\]

The already filled short cores have constant angle $2\pi$.
Schläfli's differential for the remaining positive cone path
and (26) give

\[
 \frac{d}{dc}\operatorname{Vol}_c
   =-\frac12\sum_v\ell_v(c)\frac{d}{dc}(2\pi c)
   =2\pi\sum_v\Im t_v(c).
\]

At $c=0$, equations (22) and (23) supply the absolute anchor
$\operatorname{Vol}(Y')=2\pi\Re\mathcal C(0)$.
The volume differential therefore proves

\[
 \operatorname{Vol}(S^3\setminus K)
                         =2\pi\Re\mathcal C(1).         \tag{28}
\]

This identifies metric volume on the original marked completion,
not just a regulator value up to an additive constant.

The analytic unit-charge action in (12) and the geometric action
are related by

\[
 T_{\mathbf1}(\mathbf t_*)
       =\mathcal C(1)+\frac{3i\pi}{8}\sum_\ell\sigma_\ell.
\]

Combining this with the source phase $\epsilon_N$ in (9), the
exact finite identity (4), and the asymptotic (13), gives (1)
with $S=\mathcal C(1)$ and

\[
 \Omega_N=\zeta_N\prod_{v\in V_0}C_{N,n_v}(0)
                  \exp\left(\frac{i\pi N}{2}
                                    \sum_\ell\sigma_\ell\right).
\]

Every factor has modulus one. The coefficient $D$ is the nonzero
constant in (13), with the amplitudes from (5) and (6). It is
independent of level parity. Equation (28) proves (2), completing
the theorem.

## 8. What this establishes for the finite-exception programme

The theorem permits arbitrarily many selected terminal twists of
absolute power two in any fixed tree, while the other powers are
independently sufficiently long. It removes genuine short-filling
strata from the earlier long-twist hypothesis.

It does not establish stability under every fixed partial filling.
In particular, adjacent short-filled vertices and terminal powers
of larger fixed absolute value need their own complete boundary
estimates and geometric continuation. Once no free parameter
remains, the finite-branching argument stops; this theorem does
not silently assert a result for those fully specified leaves.

The universal finite-exception goal remains open. This note records
a proved partial-filling step and the exact original-source and
primitive-geometric interfaces needed to reuse it.
