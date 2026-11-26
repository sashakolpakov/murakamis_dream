# Sharp one-sided endpoint representatives on a physical window

Private written proof, 16 November 2026.

The reflected sharp normal connection can be inserted into the exact
one-sided Hermite repair. This gives local representatives of the
original full physical jets whose real interface has any prescribed
rate below \(J_*\) at the target point. The common baseline is bounded
at every fixed target height. The original crossing, shared
spectators, and all exterior contour sides remain in the exact trace.
No bound for their closing is asserted.

## 1. The local sharp baseline

Set \(h=N^{-1}\), \(\eta_N=(-1)^{N-1}\), and
\[
 C_N(x)=2\cos(2\pi x+\pi h),\qquad x_j=jh,\qquad
 w_N(\alpha)=2\cosh(\alpha h),\qquad
 B_{i,N}(x)=K_N(w_N(\alpha_i),C_N(x)).
 \tag{1}
\]
Fix \(x_0\in(0,1/2)\), a finite number \(r\ge1\) of factors, and
parameter rectangles
\[
 |\Re\alpha_i|\le A,\qquad |\Im\alpha_i|\le\pi-\epsilon,
                    \qquad A<\infty,\quad 0<\epsilon<\pi.
 \tag{2}
\]
Larger rectangles of the same kind are reserved for derivatives.
Fix any positive loss \(\ell<J_*(\pi-2\pi x_0)\), and put
\[
 \gamma=J_*(\pi-2\pi x_0)-\ell>0,\qquad
 \delta=\frac1\pi\arcsin\frac{\sin(\pi x_0)}{\sqrt2},
\]
\[
 I_\delta(X)=\int_0^\delta
     \log\frac{\sin^2(\pi X)-\sin^2(\pi u)}
                   {\sin^2(\pi u)}\,du.
 \tag{3}
\]
Losses at least \(J_*(\pi-2\pi x_0)\) follow from any smaller
positive loss. The sharp identity is
\(I_\delta(x_0)=J_*(\pi-2\pi x_0)\), with normalization
\[
 J_*(t)=\frac1\pi\int_t^\pi
                        \operatorname{asinh}(\sin(s/2))\,ds.
\]

Choose nested real intervals about \(x_0\), with fixed positive
buffers inside \((0,1/2)\), so small that
\[
                    \min_{\text{largest real buffer}}I_\delta
                                                   \ge\gamma.
 \tag{4}
\]
Let \(I\) be the inner interval. Prescribe any fixed finite upper
and lower heights, and a larger buffered rectangle over these
intervals. The reflected connection theorem supplies one scalar
\(V_{i,N}\) on this rectangle for each factor, with polynomial
norm and polynomial bounds for every fixed spatial and parameter
derivative. It is the specified two-value-normalized sine-factor
combination, with the same cutoff on the entire rectangle.
At all physical nodes of \(I\), its actual errors
\[
 e_{i,j}=B_{i,N}(x_j)-V_{i,N}(x_j),\qquad
 d_{i,j}=B_{i,N}'(x_j)-V_{i,N}'(x_j)
 \tag{5}
\]
satisfy
\[
 |\partial_{\boldsymbol\alpha}^{\beta} e_{i,j}|
 +|\partial_{\boldsymbol\alpha}^{\beta} d_{i,j}|
                         \le C_\beta N^{p_\beta}e^{-N\gamma}.
 \tag{6}
\]
The prime in (5) is the actual angular derivative, hence
\(B_{i,N}'(x_j)=C_N'(x_j)\partial_CK_N(w_N(\alpha_i),c_j)\).
This use of both channels is the new input; it does not infer
the derivative from a values-only approximation.

## 2. Exact repair without a designated-height loss

Let \(\mathcal W_N=\{j:x_j\in I\}\), or any consecutive subwindow.
For \(\sigma\in\{+1,-1\}\) set
\[
 L_j^\sigma(x)=e^{\sigma2\pi i(x-x_j)/h}
                 \operatorname{sinc}^2((x-x_j)/h),
 \qquad \operatorname{sinc}z=\frac{\sin\pi z}{\pi z},
\]
\[
 C_{i,N}^\sigma(x)=\sum_{j\in\mathcal W_N}
 \left[e_{i,j}
    +\left(d_{i,j}-\frac{\sigma2\pi i}{h}e_{i,j}\right)(x-x_j)\right]
                                                    L_j^\sigma(x),
\qquad
 H_{i,N}^\sigma=V_{i,N}+C_{i,N}^\sigma.
 \tag{7}
\]
At its own node \(L_j^\sigma=1\) and
\((L_j^\sigma)'=\sigma2\pi i/h\); at every other node it has
a double zero. Therefore, exactly on the chosen window,
\[
 H_{i,N}^\sigma(x_j)=B_{i,N}(x_j),\qquad
 (H_{i,N}^\sigma)'(x_j)=B_{i,N}'(x_j).
 \tag{8}
\]
Since \(C_N'\) is a unit on the real buffer, these are precisely
the original values and first spectral normals.

The Fourier support of \(L_j^+\) is \([0,2/h]\), and that of
\(L_j^-\) is \([-2/h,0]\); their absolute coefficient masses
are one. On the designated half-plane \(\sigma\Im x\ge0\),
every fixed spatial derivative costs only a power of \(N\).
There are \(O(N)\) summands, and \(x-x_j\) is bounded on the
prescribed rectangle. Thus (6) gives, including its boundary,
\[
 \boxed{\quad
 |\partial_x^k\partial_{\boldsymbol\alpha}^{\beta}C_{i,N}^\sigma(x)|
                 \le C N^p e^{-N\gamma},
                 \qquad \sigma\Im x\ge0.
 \quad} \tag{9}
\]
The exponent is not reduced to absorb polynomial factors.
On an opposite collar \(|\Im x|\le d\), the corresponding bound
is \(CN^p e^{-N(\gamma-4\pi d)}\). In particular a fixed collar
with \(4\pi d<\gamma\) is allowed, but no bound on the entire
opposite half-rectangle is inferred.

The same statements hold for fixed original endpoint spectral
derivatives, with additional polynomial factors: the source
families are even in each \(\alpha_i\), and the local
\(\alpha_i^2\)-to-\(w_N(\alpha_i)\) coordinate has derivative
\(N^{-2}(1+O(N^{-2}))\).

## 3. The sharp real interface and shared products

Retain the full grid kernel
\[
                       D_h(x)=(\pi/h)^2\csc^2(\pi x/h).
 \tag{10}
\]
For one factor, write \(z=x-x_j\), \(k_h=2\pi i/h\). The exact
interface is
\[
 \begin{split}
 D_h(C_{i,N}^+-C_{i,N}^-)
 =\sum_{j\in\mathcal W_N}\frac1{z^2}
 \bigl\{&
 [e_{i,j}+(d_{i,j}-k_he_{i,j})z]e^{k_hz}\\
 &-[e_{i,j}+(d_{i,j}+k_he_{i,j})z]e^{-k_hz}\bigr\}.
 \end{split} \tag{11}
\]
Each singularity at its own \(z=0\) is removable, with value
\(4\pi i d_{i,j}/h\). For real \(z\), Taylor expansion on
\(|z|\le h\) and the direct formula on \(|z|\ge h\) bound
each term by
\(C(h^{-2}|e_{i,j}|+h^{-1}|d_{i,j}|)\).
Consequently, on the whole real window,
\[
 \boxed{\qquad
 |D_h(C_{i,N}^+-C_{i,N}^-)|\le CN^p e^{-N\gamma}.
 \qquad} \tag{12}
\]
This is the explicit weighted Hermite identity of the previous
window construction with the new sharp error data. It retains
every alias of \(D_h\).

For factors sharing one spectral variable, define
\[
 P_N^\sigma=\prod_{i=1}^r H_{i,N}^\sigma,\qquad
                         P_N^0=\prod_{i=1}^rV_{i,N}.
 \tag{13}
\]
\(P_N^+\) and \(P_N^-\) each have exactly the original shared
value and first normal at every covered node, by the ordinary
product rule. Telescoping
products gives
\[
 |P_N^\sigma-P_N^0|\le CN^p e^{-N\gamma}
                 \quad(\sigma\Im x\ge0),
\qquad
 |D_h(P_N^+-P_N^-)|\le CN^p e^{-N\gamma}
                 \quad(x\text{ real}).
 \tag{14}
\]
For the second estimate write the product difference as a sum
with exactly one factor \(H_i^+-H_i^-=C_i^+-C_i^-\), apply
(12) to that factor, and retain the other polynomially bounded
real factors. Fixed endpoint-parameter derivatives have the same
bound by the product rule. There is no multiplication of the
exponential rate by the number of factors.

## 4. Exact placement in the original full-normal trace

Write the consecutive window as \(j_0\le j\le j_1\), and choose
midpoints
\[
 a_N=(j_0-\tfrac12)h,\qquad b_N=(j_1+\tfrac12)h.
 \tag{15}
\]
Choose exterior half-contours in the prescribed rectangle.
The lower contour \(E_-\) runs down the left side, across the
bottom, and up the right side; the upper contour \(E_+\) runs
up the right side, across the top, and down the left side.
Both vertical half-sides in each contour are retained.

For a fixed original signed power \(n\), use its actual carrier
and angular crossing
\[
 \tau_N(x)=\pi-2\pi x-\pi h,\qquad
 E_{N,n}(x)=
       e^{\pi i n(N-1)^2/(4N)}e^{inN\tau_N(x)^2/(4\pi)}.
 \tag{16}
\]
Let \(A_N(C;\mathbf y)\) be the complete remaining joint
spectator, holomorphic on neighborhoods of the two closed
half-rectangles bounded by these contours and the real window,
with other traces still unapplied. Put
\[
 g_\sigma(x)=\sin(2\pi x+\pi h)\,
                  P_N^\sigma(x)E_{N,n}(x)A_N(C_N(x);\mathbf y).
 \tag{17}
\]
The original restricted full Hermite trace is exactly
\[
 \boxed{\quad
 -\frac{\eta_N}{2\pi^2 i}
 \left\{\int_{E_-}D_hg_-\,dx+\int_{E_+}D_hg_+\,dx
       +\int_{a_N}^{b_N}D_h(g_+-g_-)\,dx\right\}.
 \quad} \tag{18}
\]
Indeed, for \(g(x)=\sin(2\pi x+\pi h)f(C_N(x))\),
\[
 g'(x_j)=-\pi\{(4-c_j^2)f'(c_j)-c_jf(c_j)\}.
 \tag{19}
\]
The residue of \(D_hg\) is \(g'(x_j)\). Equations (8) and
(13) preserve this complete residue, including the derivative
of the crossing and the shared spectator. Closing the upper
half-contour along the real path from \(a_N\) to \(b_N\)
and the lower one in the opposite direction gives (18).
Their interface difference has no grid poles.

Its pointwise real bound is
\[
 \boxed{\quad
 |D_h(g_+-g_-)(x)|
 \le CN^p e^{-N\gamma}
       |\sin(2\pi x+\pi h)E_{N,n}(x)A_N(C_N(x);\mathbf y)|.
 \quad} \tag{20}
\]
The spectator remains inside this estimate. No growth bound for
it, nor a bound for the integrated closing, is supplied.
The exterior integrals in (18), all their aliases, and every
physical row outside the window remain.

For several traced colors the same replacements are coefficientwise
in the other variables and may be made before their closings.
Ordinary mixed differentiation preserves all shared first normals.
An edge coupling two such colors remains in the joint spectator;
it is not split into independent factors or estimated here.

## 5. Scope and direct sources

The previous one-sided window theorem already supplied the repair,
interface identity, and full contour normalization. The additional
consequence is that their error exponent can now be chosen arbitrarily
close to \(J_*(\pi-2\pi x_0)\) on a sufficiently small fixed window,
while the common scalar remains moderate at the prescribed heights.
It uses the new reflected full-normal baseline, not the old
modified-flow baseline.

In particular no estimate of the old baseline's fractional-grid
Green boundary packet is needed or asserted. The exterior-current
problem, spectator action comparison, and nonzero saddle coefficient
are unchanged by the exact construction above.

Both complete direct sources were read at their final matching pins,
and all directly used physical-jet, repair, and contour implications
were rechecked:

* [Reflected sharp physical normal connection](research_reflected_endpoint_sharp_normal_connection.md),
  SHA256 a8a379d7b492d7d2487de3c1397408478f66242f153ac0cab8eb3d224f226916.
* [One-sided endpoint window construction](research_unturned_endpoint_complex_baseline_and_window.md),
  SHA256 9d233d9bb11c2842e62d5523f97e9621a3bd22532e3b527ceaab8125782c1cc1.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Existing adopted and public notes are unchanged.
