# The sharp positive norm of charge-period increments

Research note, 3 November 2026.

The charge-period increment removes the original first-normal
channel and has an exact positive Fourier norm. For a whole fixed
graph of same-index edge kernels, this norm has a sharp asymptotic:
its exponential rate is the sum of the **unfilled** edge rates,
independently of all integer crossing powers. This is a genuine
lower bound for a vector of original charge observations. It is
not a lower bound for its central closing coefficient. The
three-crossing terminal source below gives an explicit exponential
separation between them.

The exact projection and its radical kernel are treated in
[the charge-transport note](research_current_free_aw_crossing_transport.md).
Here the new statements are the sharp prefactor, its tensor
extension, and the resulting comparison for an actual source.
The [one-sided Hermite representation](research_one_sided_hermite_projection.md)
already distinguishes an original central coefficient from a
positive norm of its representative; no positivity of that
coefficient is assumed here.

## 1. Original observations and the positive graph sum

Fix a finite graph, allowing loops and repeated edges, and a
nonempty set \(I\) of selected vertices. Put \(m=|I|\), let \(e\)
be the number of edges, and let \(d_v>0\) be the number of original
incidences at each selected vertex, including its outside edges
and counting a loop twice. All
unselected endpoints are kept complete. Every edge carries the
original same-index kernel
\[
 K_N(t,u)=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u).
 \tag{1}
\]
This assumption does not replace a reversed-index kernel by (1).
The number of vertices, edges, and signed integer powers \(n_v\)
is fixed before \(N\) tends to infinity.

Write
\[
 D=N-1,\quad \eta=(-1)^D,\quad
 \tau_a=\frac{\pi(D-2a)}N,\quad c_a=-2\cos\tau_a .
 \tag{2}
\]
The actual charged source is
\[
 Z_{\mathbf k,N}=
 \left(\prod_{v\in I}\phi_N^{(z_v)}\right)
 \left[
   \prod_{v\in I} R(z_v)^{n_v}T_{k_v}(-z_v/2)
   \prod_{vw\in E}K_N(z_v,z_w)
 \right],
 \tag{3}
\]
where \(z_w=-2\) at an outside vertex. In (3), the notation
\(K_N(z,w)\) means the same ordinary spectral polynomial as (1).
All crossing scalars, reductions, and first normals are the
original ones. In particular \(Z_{\mathbf0,N}\) is the
uninserted closing source.

Let
\[
 \Delta_v Z_{\mathbf k,N}
   =Z_{\mathbf k+N\mathbf e_v,N}-\eta Z_{\mathbf k,N},
 \qquad
 \mathcal Q_{\Gamma,N}
   =\sum_{\mathbf k\in\{0,\ldots,N-1\}^I}
                       |(\Delta_I Z)_{\mathbf k,N}|^2,
 \quad \Delta_I=\prod_{v\in I}\Delta_v .
 \tag{4}
\]
The full derivative-sampling identity and finite Parseval give
exactly
\[
 \mathcal Q_{\Gamma,N}
  =N^{3m}\sum_{\mathbf a\in\{0,\ldots,N-1\}^I}
       \left(\prod_{v\in I}\sin^2\tau_{a_v}\right)
       \prod_{vw\in E}|K_N(\tau_{a_v},\tau_{a_w})|^2 .
 \tag{5}
\]
An outside angle in this formula is zero. Indeed one increment
is the finite Fourier transform
\(-iN\sum_a e^{-ik\tau_a}\sin\tau_a F(c_a)\);
the crossing values have modulus one. Applying this in each
selected variable gives (5), with no remaining crossing phase.
This is also why (5) is exactly independent of the powers.
For the tensor product of the two-block orthogonal projections
in Section 13 of the charge-transport note, the squared norm is
\(2^{-m}\mathcal Q_{\Gamma,N}\). Formula (5) instead uses the
increments themselves.

There is a uniform finite-level lower bound directly from the
original source pin:
\[
 \mathcal Q_{\Gamma,N}\ge
      N^{3m}\{2\sin^2(\pi/N)\}^m\ge(8N)^m.
 \tag{5a}
\]
Retain the \(2^m\) grid tuples with
\(\tau_v=\pm(\pi-\pi/N)\). Each selected spectral value is
\(c_0\), every incident kernel is exactly \(K_N(c_0,w)=1\),
and every crossing value has modulus one. A complete edge
between two unselected endpoints contributes
\(K_N(0,0)\ge1\). The sine chord inequality proves the second
bound. If every edge has a selected endpoint, the same argument
proves (5a) for arbitrary complex outside spectral values.
It bounds the observation vector; it does not specify which
charge has nonzero observation.

At odd levels the grid point \(\tau=0\) has weight zero.
Thus the increment also loses the simple-node value channel
there; it is not an invertible observation of the full physical
algebra. The normals disappeared by the exact difference in
(4), not by deleting them from the definition (3).

## 2. Sharp asymptotics at both parities

Put \(M_\infty=4G/\pi\), where \(G\) is Catalan's constant, and
define
\[
 \mathfrak c_\Gamma
   =16^{-e}\left(\frac{\pi}{\sqrt2}\right)^m
                             \prod_{v\in I}d_v^{-3/2}.
 \tag{6}
\]

**Theorem 1.** At every integer level tending to infinity,
\[
 \boxed{\displaystyle
 \mathcal Q_{\Gamma,N}
  =\mathfrak c_\Gamma\,N^{5m/2-3e}
        e^{\,2NeM_\infty}\bigl(1+O_\Gamma(N^{-1})\bigr).}
 \tag{7}
\]
In particular this positive quantity is nonzero for all
sufficiently large levels. Its square root has rate
\(eM_\infty\), for every choice of the integer crossing powers.

**Proof of the global localization.** At a physical spectral
node every nonzero Newton value is nonnegative and comes from
an index \(j\le\lfloor N/2\rfloor\). To see this directly, the
distinct nodes \(2\cos((2a+1)\pi/N)\) decrease before the
midpoint. The Newton product is positive until it reaches its
own zero; all subsequent products vanish. The odd simple node
\(-2\) has the same property through \(j=(N-1)/2\).
Consequently the physical kernels in (5) are real and positive.

The uniform
[real Newton entropy bound](research_three_crossing_real_period_newton_bound.md)
gives
\[
 |e_j(-2\cos t)|\le CN^A e^{NV_t(j/N)},\qquad
 \max_yV_t(y)=m(t),\qquad
 m(t)\le\frac{M_\infty}{2}
                        -\frac{1-\cos t}{2\pi}.
 \tag{8}
\]
Use only the nonzero physical indices in (1). Summing them
therefore gives
\[
 |K_N(t,u)|\le CN^A
  \exp N\!\left[M_\infty
       -\frac{(1-\cos t)+(1-\cos u)}{2\pi}\right]
 \tag{9}
\]
on the full physical grid, including its odd simple endpoint.
The product in (5) has the resulting loss
\(\sum_{v\in I}d_v(1-\cos\tau_{a_v})/(2\pi)\) before
squaring. Since every \(d_v>0\), the part where any selected
angle lies outside a fixed neighborhood of zero has a strict
exponential gap. All finite grid factors and the prefactor
in (5) are polynomial in \(N\).

**Proof of the local normalization.** The
[proved full bare-kernel packet](research_bare_kernel_thin_rectangle.md)
gives, on a fixed neighborhood of the complete real angles,
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                                  (1+O(N^{-1})),
\]
\[
 a_e(0,0)=\frac14,\qquad
 a_e(t,u)=\frac14+O(t^2+u^2),\qquad
 \psi(t,u)=M_\infty-\frac{t^2+u^2}{4\pi}
                              +O((t^2+u^2)^2).
 \tag{10}
\]
The separate evenness in \(t,u\) gives the amplitude estimate.
The quadratic phase follows either from the original return
formula or from \(\psi''(0,0)=-(2\pi)^{-1}I\).
All formulas concern the full original kernel, not only its
low indices.

Multiplying (10) over the graph and squaring produces the
constant \(16^{-e}\), the power \(N^{-3e}\), and the Gaussian
\[
 e^{2NeM_\infty}
       \exp\!\left[-\frac N{2\pi}
                         \sum_{v\in I}d_v t_v^2\right].
 \tag{11}
\]
Moreover
\(\prod_v\sin^2t_v=(\prod_v t_v^2)
[1+O(\sum_vt_v^2)]\), with the identity interpreted
continuously when a coordinate is zero.

The needed one-dimensional grid moment is, for each fixed \(d>0\),
\[
 \sum_{a=0}^{N-1}\tau_a^2
                       e^{-Nd\tau_a^2/(2\pi)}
   =\frac{\pi}{\sqrt2\,d^{3/2}}\,N^{-1/2}
                                      (1+O(e^{-c_dN})).
 \tag{12}
\]
At odd levels the local lattice is
\((2\pi/N)\mathbb Z\), and at even levels it is
\((2\pi/N)(\mathbb Z+\tfrac12)\).
To verify (12), extend the finite lattice to the whole line;
the omitted terms are exponentially small. The Fourier
transform of \(x^2e^{-\beta x^2}\) is a polynomial times a
Gaussian. Fourier expansion of its absolutely convergent
periodization therefore compares either shifted lattice sum
with its integral, with exponential error. After scaling
\(x=\sqrt N\,t\), the integral is
\[
 \frac N{2\pi}\int_{\mathbb R}
       t^2e^{-Nd t^2/(2\pi)}\,dt
              =\frac{\pi}{\sqrt2\,d^{3/2}}\,N^{-1/2}.
 \tag{13}
\]
The two shifts change only unit phases of the nonzero Fourier
modes, so the leading constant is the same. The zero grid
point at odd levels contributes zero to both sides of the
local moment calculation; no simple-node term is substituted
for it.

For clarity, the Taylor errors in (10) also give the stated
relative \(O(N^{-1})\) after summation. In a sufficiently small
fixed box, the quadratic loss bounds the remainder by a fixed
Gaussian. The error is bounded by that Gaussian times
\[
       C_\Gamma\{N^{-1}+\textstyle\sum_vt_v^2
                                   +N(\sum_vt_v^2)^2\}.
 \tag{14}
\]
Gaussian lattice moments, with the factor \(\prod_vt_v^2\)
retained, make the relative sum of (14) \(O(N^{-1})\).
One may first restrict to a shrinking Gaussian window;
its complement has superpolynomial loss, and the fixed-box
complement was already bounded by (9). This justifies the
expansion without a relative estimate at a vanishing sine
factor. Finally multiply (12) over the \(m\) selected vertices
and include \(N^{3m}\) from (5). The power is
\(3m-3e-m/2=5m/2-3e\), proving (7). \(\square\)

## 3. A lower bound for the observation vector, not its center

Let \(\mathbf Z_N=(Z_{\mathbf k,N})_{0\le k_v<N}\).
The physical evenness and period relations imply that a
single increment on this finite block is the map
\[
 (\mathsf D_\eta z)_0=0,\qquad
 (\mathsf D_\eta z)_k=\eta z_k-z_{N-k}\quad(1\le k<N).
 \tag{15}
\]
Its operator norm is at most two. Tensoring (15) gives the
actual quantitative lower bound
\[
 \|\mathbf Z_N\|_2
       \ge2^{-m}\mathcal Q_{\Gamma,N}^{1/2}.
 \tag{16}
\]
The corresponding exponential rate is sharp:
\[
              \lim_{N\to\infty}\frac1N
                       \log\|\mathbf Z_N\|_2=eM_\infty.
 \tag{17}
\]
For the upper bound, every crossing has unit physical values
and polynomially bounded first normals for a fixed power.
The insertions \(T_k\), \(0\le k<N\), have real norm at most
one and ordinary derivatives of polynomial size. The real
Newton entropy bound together with the radical Fourier bound
gives \(\|K_N\|_{\rm real}\le CN^A e^{NM_\infty}\).
Markov inequalities give the same rate for its fixed mixed
normals. Apply the original full physical residue at every
vertex in (3). The finite node sum and the number of charge
observations add only polynomial factors. This gives the
upper rate in (17), while (7) and (16) give the lower one.

In particular, a positive norm of the full charge state can
be proved without the desired unit-charge lower bound. The
map (15) annihilates the central coordinate rather than
recovering it. Its tensor version likewise observes no
coefficient for which one selected charge is zero.

There is a sharp example entirely within the original source.
For one selected vertex with one complete outside edge, put
\[
 Z_{k,N}^{(n)}(-2)=
   \phi_N[R^nK_N(\,\cdot\,,-2)T_k(-z/2)] .
 \tag{18}
\]
Theorem 1 gives, for every integer power \(n\),
\[
 \|\Delta Z^{(n)}\|_2^2
     =\frac{\pi}{16\sqrt2}N^{-1/2}e^{2NM_\infty}
                                           (1+O(N^{-1})).
 \tag{19}
\]
Its left side is exactly independent of \(n\), not merely
asymptotically so. On the other hand the proved
[three-crossing terminal packet](research_three_crossing_terminal_filling.md)
has the actual central observation
\[
 Z_{0,N}^{(3)}(-2)
    =C_{N,3}A_3(0)e^{NS_3(0)}(1+O(N^{-1})),
 \quad |C_{N,3}|=1,\quad A_3(0)\ne0,\quad
 M_3=\Re S_3(0).
 \tag{20}
\]
Combining these two all-level results gives
\[
 \frac{|Z_{0,N}^{(3)}(-2)|}{\|\Delta Z^{(3)}\|_2}
  =\frac{4\,2^{1/4}|A_3(0)|}{\sqrt\pi}\,
       N^{1/4}e^{-N(M_\infty-M_3)}(1+O(N^{-1})).
 \tag{21}
\]
The gap is strictly larger than \(3/10\). The
[saved outward action certificate](../repro/results/research-terminal-three-central-phase.json)
gives \(M_3<17/20\). The alternating Catalan series and
\(\pi<22/7\) give
\[
 M_\infty>
 \frac4{22/7}\left(1-\frac19+\frac1{25}-\frac1{49}\right)
 =\frac{23}{20}+\frac{433}{69300}.
 \tag{22}
\]
Thus this is exponential invisibility of a specified original
closing observation to an otherwise explicit positive norm.
It does not assert that the closing observation vanishes;
(20) proves precisely the opposite.

For any graph family whose original central geometric packet
has already been independently proved with rate \(M_\Gamma\),
(7) gives the analogous normalized rate
\(M_\Gamma-eM_\infty\). In the positive geometric convention
the energy identity writes this as \(-F_\Gamma/\pi\).
This comparison is not a proof of that packet for a new graph.
Nor is a formal kernel network automatically identified with
a knot invariant. The conclusions above apply to the exact
finite source (3), and to an original knot or tangle only when
its marked source is that expression.
