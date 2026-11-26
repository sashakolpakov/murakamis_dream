# Repeated endpoint unit turns retain the terminal action

Private written proof, 16 November 2026.

One unit turn of a full microscopic endpoint kernel has polynomial
real norm. Repeating that operation does not preserve this bound:
two turns of the same sign already have the positive exponential
rate of the original two-crossing terminal message. This follows
from an exact forced equation and a polynomial norm bound for its
original difference operator. No new knot calculation is involved.

## 1. Exact repeated-turn forcing

Use the original full algebra
\[
 \mathcal A_N=\mathbb C[Z]/(P_N),\quad
 P_N(Z)=2T_N(Z/2)+2,\quad D=N-1,\quad
 \theta=\pi/N,\quad \eta=(-1)^D,\quad
 \kappa=e^{i\pi D^2/(2N)}.
 \tag{1}
\]
Write \(q=e^{i\theta}\),
\(S_j=\prod_{h=1}^j2\sin(h\theta)\), \(S_0=1\),
\(c_j=2\cos((2j+1)\theta)\), and
\(e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z)\).
The Newton basis, original crossing and turn satisfy
\[
 K_N(w,Z)=\sum_{j=0}^D e_j(w)e_j(Z),\quad
 Te_j=e_{D-j},\quad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{2}
\]
All classes below have their canonical ordinary representatives
of degree at most \(D\). Set
\[
 V_n=\kappa^n T R^{-n}T,\quad n\in\mathbb Z,\qquad
 G_{n,N}=T(R^{-n}),\quad
 F_{n,N,\alpha}=V_nK_N(w_N(\alpha),\cdot),\quad
 w_N(\alpha)=2\cosh(\alpha/N).
 \tag{3}
\]
Thus \(V_\sigma=U_\sigma\) for \(\sigma=\pm1\), and
\[
                     V_nV_\ell=V_{n+\ell}.
 \tag{4}
\]
For example \(F_{2\sigma}=U_\sigma^2K_{w_N(\alpha)}\).

Let \(C\) be multiplication by \(Z\), and let
\(\mathcal L=TCT\). Multiplication by \(R^{-n}\) commutes
with \(C\), so \(V_n\) commutes with \(\mathcal L\).
The original reproducer gives
\[
 (w-\mathcal L)K_N(w,\cdot)=\frac{\eta P_N(w)}{N^2}e_D,
 \qquad V_ne_D=\kappa^nG_{n,N}.
 \tag{5}
\]
Therefore the exact full-normal identity is
\[
 \boxed{\quad
 (w_N(\alpha)-\mathcal L)F_{n,N,\alpha}
       =\frac{\eta P_N(w_N(\alpha))\kappa^n}{N^2}G_{n,N}.
 \quad}                                                     \tag{6}
\]
For one unit turn the right side contains \(G_{\sigma,N}=R^\sigma\).
For two turns it contains the actual terminal polynomial
\(T(R^{-2\sigma})\); it cannot be replaced by a unit crossing.

## 2. A real norm bound for the original difference operator

Write \(\|p\|_{\mathbb R}=\sup_{[-2,2]}|p|\). The original
off-grid difference formula, with \(t=(2r+1)\theta\), is
\[
 (\mathcal Lp)(2\cos t)
  =c_0 f(t)+
    \frac{4\sin^4((t+\theta)/2)}{\sin t\sin(t+\theta)}
                          [f(t)-f(t+2\theta)]
\]
\[
 \hspace{38mm}+
    \frac{4\sin^4((t-\theta)/2)}{\sin t\sin(t-\theta)}
                          [f(t)-f(t-2\theta)],
 \qquad f(t)=p(2\cos t),\quad c_0=2\cos\theta.
 \tag{7}
\]
All apparent singularities in the combined expression are removable
for degree at most \(D\).

Expand \(f(t)=a_0+\sum_{k=1}^D a_k\cos kt\), and put
\[
 B(t)=\sin^4(t/2)\sum_{k=1}^D a_k\sin(k\theta)
                                      U_{k-1}(\cos t),
 \tag{8}
\]
where \(U_{k-1}(\cos t)=\sin(kt)/\sin t\) is the ordinary
Chebyshev polynomial of the second kind. The two cosine differences
in (7) give exactly
\[
 \boxed{\quad
 (\mathcal Lp)(2\cos t)
       =c_0 f(t)+8\,\frac{B(t+\theta)-B(t-\theta)}{\sin t}.
 \quad}                                                     \tag{9}
\]
Here \(B\) is an even trigonometric polynomial of degree at most
\(D+1=N\).

For a trigonometric polynomial, let \(\|\cdot\|_{\mathrm F,1}\)
be the sum of the absolute values of its Fourier coefficients.
The cosine integral formula and the finite Laurent expression for
\(U_{k-1}\) give
\[
 |a_0|+\sum_{k=1}^D|a_k|\le(2D+1)\|p\|_{\mathbb R},\qquad
 \|U_{k-1}(\cos t)\|_{\mathrm F,1}=k,\qquad
 \|\sin^4(t/2)\|_{\mathrm F,1}=1.
 \tag{10}
\]
Consequently
\[
                     \|B\|_{\mathrm F,1}
                    \le D(2D+1)\|p\|_{\mathbb R}.             \tag{11}
\]
If \(B=b_0+\sum_{m=1}^N b_m\cos mt\), then
\[
 \frac{B(t+\theta)-B(t-\theta)}{\sin t}
       =-2\sum_{m=1}^N b_m\sin(m\theta)U_{m-1}(\cos t).
 \tag{12}
\]
This is a polynomial identity also at \(t=0,\pi\), and the
last term vanishes because \(\sin(N\theta)=0\).
For real \(t\), \(|U_{m-1}(\cos t)|\le m\). Thus
\[
 \boxed{\qquad
                  \|\mathcal Lp\|_{\mathbb R}
                         \le34N^3\|p\|_{\mathbb R}.
 \qquad}                                                    \tag{13}
\]
This bound concerns the complete polynomial operator. Bounding
its separate singular terms in (7) would not justify (13).

Combining (6) and (13) proves, for every integer \(n\), every
\(\alpha\in\mathbb C\), and every \(N\ge2\),
\[
 \boxed{\quad
 \|F_{n,N,\alpha}\|_{\mathbb R}
 \ge
 \frac{|P_N(w_N(\alpha))|}
      {N^2(|w_N(\alpha)|+34N^3)}
                         \|G_{n,N}\|_{\mathbb R}.
 \quad}                                                     \tag{14}
\]
This is an unconditional finite-level comparison. At a zero
of \(P_N(w_N(\alpha))\) it is simply vacuous.

## 3. A polynomial upper comparison for a fixed number of turns

Fix \(n\in\mathbb Z\) and \(A<\infty\). The endpoint-side adapter
extends exactly to this fixed power:
\[
 F_{n,N,\alpha}(Z)
   =\kappa^n[\operatorname{can}_w
                   (R(w)^{-n}K_N(w,Z))]_{w=w_N(\alpha)}.
 \tag{15}
\]
Indeed Frobenius self-adjointness of multiplication gives the
same transposed Newton matrix as for a single turn.
The original physical values of \(R^{-n}\) have modulus one
and their angular derivatives are bounded by \(|n|N/2\).
The full-Hermite Fourier reconstruction and the endpoint normal
\(Q_N=\partial_wK_N(c_0,\cdot)\), with
\(\|Q_N\|_{\mathbb R}\le N^4/4\), therefore give polynomial
initial value and first normal for (15), uniformly on
\(|\alpha|\le A\).

Apply the single-turn proof's forced propagation to (6), retaining
\(G_{n,N}\) in its forcing. In its notation the regular physical
rows have
\[
 0\le q_j<1,\qquad
 A_j\ge16(j+1)^2/(\pi^2N^2),\qquad
 |(c_0-w_N(\alpha))/A_j|\le C_A/(j+1)^2.
 \tag{16}
\]
The balanced forward matrices have norm at most
\(1+C_A/(j+1)\), so all their products are polynomial in \(N\).
The value forcing is bounded by
\[
                 C_A\|G_{n,N}\|_{\mathbb R}/(j+1)^2.
 \tag{17}
\]
For the differentiated equation, Markov bounds the spectral
derivative of the ordinary degree-\(D\) polynomial \(G_{n,N}\)
by \(C N^2\|G_{n,N}\|_{\mathbb R}\). All coefficient derivatives
have polynomial bounds. The differentiated equation has the same
homogeneous matrices, so its forcing and its propagated physical
normals have a polynomial factor times
\(1+\|G_{n,N}\|_{\mathbb R}\).
Stable full-Hermite reconstruction then yields
\[
 \|F_{n,N,\alpha}\|_{\mathbb R}
       \le C_{A,n}N^{p_{A,n}}
                       (1+\|G_{n,N}\|_{\mathbb R}).          \tag{18}
\]
The regular-row endpoints and the odd simple node are exactly those
of the single-turn proof; no coalescing next row is introduced.

The harmless \(1\) can be absorbed. In fact
\[
             \phi_N(G_{n,N})=R^{-n}(c_0)=\kappa^{-n}
 \tag{19}
\]
has modulus one. The original full trace and Markov imply
\(|\phi_N(p)|\le C N^3\|p\|_{\mathbb R}\), so
\(\|G_{n,N}\|_{\mathbb R}\ge cN^{-3}\).
For real \(|\alpha|\le A\),
\[
 P_N(w_N(\alpha))=4\cosh^2(\alpha/2)\ge4,
 \qquad |w_N(\alpha)|\le2\cosh(A/2).
 \tag{20}
\]
Equations (14),(18)--(20) therefore show
\[
 \boxed{\quad
 c_A N^{-5}\|G_{n,N}\|_{\mathbb R}
 \le\|F_{n,N,\alpha}\|_{\mathbb R}
 \le C_{A,n}N^{p_{A,n}}\|G_{n,N}\|_{\mathbb R}.
 \quad}                                                     \tag{21}
\]
Thus any existing exponential norm rate of the actual terminal
polynomial \(T(R^{-n})\) is also the rate of this endpoint orbit.
The claim holds uniformly for real microscopic parameters in
a fixed compact interval. The lower comparison is not extended
through the complex zeros in (20).

## 4. Two same-sign turns already have positive rate

The original two-crossing terminal theorem, in the same
normalization, proves
\[
 T(R^2)(-2)=\frac{e^{-i\pi/4}}2
       e^{N(2G/\pi+i\pi/8)}(1+O(N^{-1})),
 \tag{22}
\]
where \(G=\sum_{j\ge0}(-1)^j/(2j+1)^2>0\) is Catalan's
constant, and write \(M_\infty=4G/\pi\).
The negative-power polynomial has conjugate
coefficients. The theorem also bounds the entire real interval
by \(C N^a e^{N\,2G/\pi}\). Consequently
\[
        \lim_{N\to\infty}N^{-1}
                \log\|T(R^{\pm2})\|_{\mathbb R}=2G/\pi.
 \tag{23}
\]
This is through all levels, with neither parity omitted.
Combining with (21) gives
\[
 \boxed{\quad
 \lim_{N\to\infty}N^{-1}
       \log\|U_\sigma^2K_N(w_N(\alpha),\cdot)\|_{\mathbb R}
             =2G/\pi=M_\infty/2,\qquad \sigma=\pm1.
 \quad}                                                     \tag{24}
\]
The convergence is uniform for real \(|\alpha|\le A\). In
particular, for all sufficiently large \(N\),
\[
       \|U_\sigma^2K_N(w_N(\alpha),\cdot)\|_{\mathbb R}
                    \ge c_A N^{-5}e^{N\,2G/\pi}.             \tag{25}
\]
The input and its first unit-turn image both have polynomial real
norm. Their second same-sign turn has positive exponential norm.
For the input this also follows directly from (18) at \(n=0\):
\(G_{0,N}=e_D=\eta P_N/[N^2(Z-c_0)]\) has real norm at most
one, by \(\|P_N'\|_{\mathbb R}\le N^2\).
Hence the single-endpoint polynomial theorem cannot be iterated
as a polynomial-norm closure rule, even without multiplying
different endpoint factors.

For clarity, the analytic input (22) was checked from its proof,
not from its recorded experiments. The exact terminal expansion
is
\[
 T(R^2)(Z)=N\sum_{k=0}^{N-1}
            \frac{i^kq^{k(k-1)/2}}{S_k}e_k(Z).
 \tag{26}
\]
The finite binomial identity gives (26) with the original carrier
and full normals. At \(Z=-2\), its canonical-factorial phase is
\[
 F(x)=J(2x)-5J(x)+\frac{i\pi}{2}(x^2+x),\qquad
 J'(x)=\log(2\sin\pi x),
 \tag{27}
\]
with the selected saddle
\[
 e^{2\pi ix_*}=(1+2i)/5,\qquad F''(x_*)=\pi(-4+3i).
 \tag{28}
\]
On \(0<\Re x<1/2\), \(\Re F''<0\).
The finite cotangent rectangle keeps both exponentially weighted
vertical sides; reflection supplies the lower-horizontal gap.
The unweighted upper connectors have strictly smaller endpoint
values and convex vertical real part. The discarded low tails
have continuous rate \(J(2x)-5J(x)\) tending to zero at both
ends, while all high indices have polynomial complete norm.
The exact factorial normalization gives the nonzero coefficient
in (22). These are the proof steps establishing the needed
terminal exponential rate. They require no theorem about an
arbitrary descendant or its hyperbolicity.

## 5. Scope and source readback

The norm in (24) is an ordinary real-interval polynomial norm.
Further physical traces can cancel its large values; no lower
bound for an arbitrary closed graph follows. The conclusion
instead identifies the actual terminal action which a repeated
source reduction must retain. It neither refutes an action-scale
estimate nor proves one for arbitrary short components.
Complex parameters where \(P_N(w_N(\alpha))=0\) are explicitly
excluded from the lower-rate conclusion.

The following complete direct sources were read at these pins:

* [Single full endpoint under a unit turn](research_full_endpoint_unit_turn_polynomial_bound.md),
  SHA256 329ee59c992c359c42775f564f540ffeee7f142bf51b5132913bf4cf2a859d35:
  canonical forcing, both initial jets, forward physical-normal
  propagation, and stable full-Hermite reconstruction.
* [Original polynomial difference operator](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_edge_kernel_difference_and_endpoint_bound.md),
  SHA256 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da:
  exact operator and original endpoint forcing.
* [Two-crossing terminal theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_two_crossing_terminal_filling.md),
  SHA256 7aedaded3efa3058a3250b2120cc4f41bcad1f7f20aff2e7f4dd4fab19aae9ed:
  exact finite identity, complete contour proof, nonzero germ,
  and real-interval upper bound.

For the last source, its following analytic and algebraic inputs
were also read completely, and the used proof implications checked:

* [Original finite algebra](../papers/newton-calculus/finite.tex),
  SHA256 2db2d7e15df0210c32bace4c761bdabadbb5d67140473a61425dac4d1e382f8e:
  original crossing matrix, turn, and full closing normalization.
* [Finite complete-normal bounds](../papers/circle-tree-volume/finite-bounds.tex),
  SHA256 e4cf66544703af6d9a78208deae971c4d9f4367ba4b2ad660694ee489ef67ea1:
  polynomial high-index bounds and real interval reconstruction.
* [Canonical edge interpolation](../papers/circle-tree-volume/edge-packet.tex),
  SHA256 53eb6dbfbda3ca639db35911ed50947c29655840337f9d1f1ce909d435013dbb:
  exact factorial interpolant and its midpoint normalization.
* [Factorial product and uniform complex Stirling proof](../papers/conway-asymptotics/factorial.tex),
  SHA256 fa05557505927ae81f005b90edbd3d0946288e7eacf2363f070d9753db632fe1:
  normalized product, zero-free strips, and summable complex
  remainder used on the terminal contour.

Only written mathematics, text reads and file hashes were used.
No mathematical program, numerical experiment, test or build
was run. Existing private notes and public files were unchanged.
