# A uniform bound for the high-index free-boundary polynomial

Private research proof, 12 November 2026. Frozen manuscripts are unchanged.

The canonical interpolation of a Newton wire is an ordinary polynomial
in every free boundary coordinate. On the second half of the index
period it cannot be assigned the factorial phase at the complete
boundary: that phase can be negative while an actual Fourier
coefficient is only polynomially small. Here we bound the entire
polynomial instead. The bound is uniform through zero index height,
retains all spectral derivatives, and applies independently to every
high-index incidence of a finite network.

The starting physical-value calculation is already in Section 1 of
[the high-half-period estimate](research_internal_pair_three_high_half_bound.md).
That calculation uses one fixed nonzero height. The additions here are
uniformity down to height zero, the passage from physical data to the
ordinary free polynomial, and the resulting bound for any finite set
of free incidences. No particular crossing power is assumed.

## 1. The polynomial and the estimate

For an integer \(N\ge2\), put \(D=N-1\) and
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 c_j=2\cos\frac{(2j+1)\pi}{N},\qquad
 e_j(z)=\frac{\prod_{r<j}(c_r-z)}
                   {\prod_{r=1}^j4\sin^2(\pi r/N)}.
 \tag{1}
\]
Here \(T_N(\cos t)=\cos Nt\). Define the entire cardinal function
and its original free-boundary interpolation by
\[
 s_N(x)=\frac{\sin(\pi Nx)}{N\sin(\pi x)},\qquad
 \widetilde B_N(x,z)=\sum_{j=0}^{D}s_N(x-j/N)e_j(z).
 \tag{2}
\]
Removable values are understood. The degree in \(z\) is at most
\(D\). Its index frequencies are
\(-D/2,-D/2+1,\ldots,D/2\); in particular,
\(\widetilde B_N(x+1,z)=(-1)^D\widetilde B_N(x,z)\).

**Theorem 1.** For each fixed integer \(k\ge0\), there is a
constant \(C_k\), independent of \(N,x,u\), such that
\[
 \left|\partial_z^k\widetilde B_N(x,-2\cos u)\right|
 \le C_k N^{6+2k}
       \exp\{\pi N|\Im x|+D|\Im u|\},
 \qquad \frac12\le\Re x\le1,\quad u\in\mathbb C.
 \tag{3}
\]
There is no bound on \(|\Im x|\) in this assertion. On a fixed
strip \(|\Im u|\le b\), every fixed angular derivative satisfies
the analogous estimate, with a constant depending on \(b\) and
a further fixed power of \(N\).

In particular, on the real boundary interval and the real second
half-period, the entire polynomial and every fixed boundary derivative
have polynomial size. At nonzero index height, the cost
\(\pi N|\Im x|\) is retained. The free-boundary continuation
cost \(D|\Im u|\) is also retained; neither is declared to be
smaller than a geometric action.

## 2. Uniform physical values and first normals

The distinct physical roots have angles
\[
 \tau_j=\pi-\frac{(2j+1)\pi}{N},\qquad
 0\le j\le\lfloor D/2\rfloor.
 \tag{4}
\]
Every root is double except for \(-2\), which is simple at odd
levels. At every double root \(\tau_j>0\). The full Fourier-band
theorem gives the following exact values and angular derivatives:
\[
 \begin{split}
 V_j(x)&=\widetilde B_N(x,c_j)
   =\frac{\sin(\pi Nx)}{N\sin(\pi x)}
       \prod_{r=1}^{j}
        \frac{\sin\pi(x+r/N)}{\sin\pi(r/N-x)},\\
 H_j(x)&=\left.\partial_u\widetilde B_N(x,-2\cos u)
                                     \right|_{u=\tau_j}
   =-\frac12V_j(x)
            \sum_{r=j+1}^{D-j}\cot\pi(r/N-x).
 \end{split}
 \tag{5}
\]
Both functions are entire in \(x\). The apparent poles cancel in
the finite sine-product formulas of that theorem. At the odd simple
root only \(V_j\) is required; its empty sum in (5) gives zero
angular derivative and does not prescribe an extra spectral normal.

We prove the uniform bounds
\[
 |V_j(a+ih)|\le C e^{\pi N|h|},\qquad
 |H_j(a+ih)|\le C N^2e^{\pi N|h|},
 \qquad \frac12\le a\le1.
 \tag{6}
\]
For \(1\le r\le j<N/2\),
\[
 |\sin\pi(a+ih+r/N)|^2
       -|\sin\pi(r/N-a-ih)|^2
       =\sin(2\pi a)\sin(2\pi r/N)\le0.
 \tag{7}
\]
Thus each ratio in (5) has modulus at most one whenever \(h\ne0\).
If \(|h|\ge1/N\), then
\[
 |\sin\pi(a+ih)|\ge\sinh(\pi|h|)\ge\pi/N,
 \qquad
 |\cot\pi(r/N-a-ih)|\le\coth(\pi|h|)\le C N.
 \tag{8}
\]
Together with \(|\sin\pi N(a+ih)|\le e^{\pi N|h|}\),
these prove (6) on that region, including the two horizontal sides
\(h=\pm1/N\).

To cross zero height, apply the maximum principle to the entire
functions in (5) on
\[
              \frac12\le a\le1,\qquad |h|\le1/N.
 \tag{9}
\]
The two vertical sides require care at their removable zeros.
At \(a=1\), every ratio in (5) has modulus one and
\[
 \frac{|\sin\pi N(1+ih)|}{N|\sin\pi(1+ih)|}
   =\frac{\sinh(\pi N|h|)}{N\sinh(\pi|h|)}
   \le e^{\pi(N-1)|h|}.
 \tag{10}
\]
The value at zero is its continuous limit. The inequality follows
from
\(\sinh(Ny)\le N\sinh(y)e^{(N-1)y}\) for \(y\ge0\),
obtained by summing its finite geometric expression. Every cotangent
in (5) on this side is bounded by \(CN\): its real argument is a
nonzero multiple of \(\pi/N\), and
\[
 |\cot(v+iy)|^2
      =\frac{\cos^2v+\sinh^2y}{\sin^2v+\sinh^2y}
      \le\max(1,\cot^2v).
 \tag{11}
\]
There are at most \(N\) terms. Thus this side has
\(|V_j|\le C\), \(|H_j|\le CN^2\).

At \(a=1/2\), every ratio again has modulus one and
\(|V_j|\le e^{\pi N|h|}/N\). All cotangents except possibly
\(r=N/2\) are bounded by \(CN\), since their nonzero real
arguments are at distance at least \(\pi/(2N)\) from a multiple
of \(\pi\). The exceptional term occurs only at even levels.
For that term, its product with \(V_j\), rather than the
cotangent separately, obeys
\[
 |V_j(1/2+ih)\cot(-\pi ih)|
 \le\frac{\sinh(\pi N|h|)\coth(\pi|h|)}
                {N\cosh(\pi|h|)}
 =\frac{\sinh(\pi N|h|)}{N\sinh(\pi|h|)}
 \le e^{\pi(N-1)|h|}.
 \tag{12}
\]
This also has a finite limit at zero. The left side of (9) therefore
has the same polynomial bounds. The maximum principle on (9),
together with the horizontal bounds, proves (6) for the missing
heights as well. The constants are absolute.

At a double root the spectral normal is
\[
 U_j(x)=\partial_z\widetilde B_N(x,c_j)
                      =\frac{H_j(x)}{2\sin\tau_j}.
 \tag{13}
\]
Since \(\sin\tau_j\ge\sin(\pi/N)\ge2/N\), (6) gives
\[
 |U_j(x)|\le C N^3e^{\pi N|\Im x|}.
 \tag{14}
\]
There is no spectral derivative imposed at the odd simple root.

## 3. Recovering the whole free polynomial

Here a bound on the physical data is sufficient, because the
ordinary polynomial has degree below \(N\). We give a polynomial
bound for the full confluent interpolation map, rather than replace
that map by interpolation at distinct roots.

For a double root \(c\), put
\[
 Q_c(z)=\frac{P_N(z)}{(z-c)^2},\qquad
 \lambda_c=\frac{Q_c'(c)}{Q_c(c)},
\]
and define
\[
 A_c(z)=\{1-\lambda_c(z-c)\}\frac{Q_c(z)}{Q_c(c)},
 \qquad
 B_c(z)=(z-c)\frac{Q_c(z)}{Q_c(c)}.
 \tag{15}
\]
These are the value and derivative cardinal polynomials: at \(c\)
their respective data are \((1,0)\) and \((0,1)\); at every other
root they have the required zeros with multiplicity. Their degrees
are at most \(N-1\). At odd levels the simple-root cardinal is
\[
                  A_-(z)=\frac{P_N(z)}{N^2(z+2)}.
 \tag{16}
\]
Therefore every polynomial \(p\) of degree below \(N\) satisfies
\[
 p(z)=\sum_{c\ {m double}}
            \{p(c)A_c(z)+p'(c)B_c(z)\}
       +\mathbf1_{N\ {m odd}}p(-2)A_-(z).
 \tag{17}
\]
Indeed the two sides have identical full physical data; their
difference has degree below \(N\) and is divisible by \(P_N\).

The Chebyshev differential equation gives
\[
 Q_c(c)=\frac{N^2}{4-c^2},\qquad
 \lambda_c=\frac{c}{4-c^2},\qquad
 P_N'(-2)=N^2\quad(N\ {m odd}).
 \tag{18}
\]
For clarity, differentiate
\((4-z^2)P_N''-zP_N'+N^2(P_N-2)=0\) once and evaluate at a
double root. This yields
\(P_N''(c)=2N^2/(4-c^2)\) and
\(P_N'''(c)/P_N''(c)=3c/(4-c^2)\), proving the first two
identities in (18). The last follows from differentiating
\(T_N(\cos t)=\cos Nt\) at the endpoint.

On \([-2,2]\), \(|P_N|\le4\). Markov's polynomial derivative
inequality, scaled from \([-1,1]\), gives
\(\|P_N''\|\le CN^4\). Taylor's formula about the double root
then gives \(\|Q_c\|\le CN^4\). Also
\(Q_c(c)\ge N^2/4\) and \(|\lambda_c|\le CN^2\), uniformly
over all double roots. Thus
\[
 \|A_c\|_{[-2,2]}\le CN^4,\qquad
 \|B_c\|_{[-2,2]}\le CN^2,\qquad
 \|A_-\|_{[-2,2]}\le C.
 \tag{19}
\]
For the last bound use the first derivative estimate and the simple
zero at \(-2\). These bounds are deliberately polynomial rather
than optimized.

Apply (17)--(19) with \(p=\widetilde B_N(x,\cdot)\) and use
(6), (14). There are at most \(N\) distinct roots, giving
\[
       \|\widetilde B_N(x,\cdot)\|_{[-2,2]}
                      \le CN^6e^{\pi N|\Im x|}.
 \tag{20}
\]
Repeated Markov inequalities add a factor \(C_kN^{2k}\)
for the \(k\)-th spectral derivative. For complex coefficients,
the real Markov inequality applies by rotating the derivative at
the point under consideration and taking the real part.

Finally, a polynomial \(p\) of degree at most \(D\) obeys
\[
 |p(-2\cos(a+iv))|\le e^{D|v|}\|p\|_{[-2,2]}.
 \tag{21}
\]
To verify it for \(v\ge0\), set \(w=e^{i(a+iv)}\).
The function \(w^Dp(-w-w^{-1})\) is a polynomial, bounded by
\(\|p\|\) on the unit circle. Apply the maximum principle inside
that circle and divide by \(|w|^D\). Replacing \(w\) by
\(w^{-1}\) proves the other half-plane. Apply (21) to each
spectral derivative. This proves (3). Angular derivatives follow
from the chain rule on every fixed angular strip.

## 4. Arbitrary free incidences in an exact network

Consider an original finite network and its exact cardinal all-wire
integrand. A free vertex \(v\) has the ordinary boundary coordinate
\(z_v=-2\cos u_v\). An incidence \(h\) at that vertex contributes
\(\widetilde B_N(y_h,z_v)\), where its actual oriented argument is
either \(y_h=x_e\) or \(y_h=D/N-x_e\), with any integer period
translation retained by its exact multiplier \((-1)^D\).
Choose any set \(\mathcal H\) of free incidences whose actual
arguments have real parts in \([1/2,1]\), after such translations.
Define their product before reducing any free coordinate:
\[
        Q_{\mathcal H,N}
           =\prod_{h\in\mathcal H}
                \widetilde B_N(y_h,-2\cos u_{v(h)}).
 \tag{22}
\]
If \(m_v\) counts its incidences at \(v\), its degree in \(z_v\)
is at most \(m_vD\). The free polynomial is not reduced modulo
\(P_N(z_v)\).

For every fixed multi-index of spectral derivatives \(\nu\),
Leibniz's rule and (3) give the uniform bound
\[
 \left|\partial_{\mathbf z}^{\nu}Q_{\mathcal H,N}\right|
 \le C_{\mathcal H,\nu}N^{6|\mathcal H|+2|\nu|}
 \exp\left\{
       \pi N\sum_{h\in\mathcal H}|\Im y_h|
           +D\sum_v m_v|\Im u_v|
      \right\}.
 \tag{23}
\]
The graph and \(\nu\) are fixed before \(N\) grows. Repeated
incidences at the same free vertex are included; they keep the same
boundary coordinate and the same derivative. Any other factors remain
in the original integrand. Multiplying their existing bounds by (23)
does not change the source, crossing powers, framing, or closing map.

There is also a direct bound after integrating any fixed measurable
portion \(\Gamma\) of the index cycle. If the remaining integrand
is \(R_N\), the absolute value of that portion is at most
\[
 C N^A\int_\Gamma |R_N|\,
 \exp\left\{
       \pi N\sum_{h\in\mathcal H}|\Im y_h|
           +D\sum_v m_v|\Im u_v|
      \right\}|d\mathbf x|,
 \tag{24}
\]
with the original circle normalization \(N^{|E_{\rm int}|}\)
retained in \(N^A\) if it is part of this integral. On a fixed
translated real index torus, the first sum in (24) is constant.
With boundary derivatives, apply the same argument term by term
after Leibniz expansion; derivatives of \(R_N\) are not discarded.

The all-wire identity remains exact at all levels because its paired
bands stay inside \([-N+1,N-1]\). Consequently no aliases or side
currents are removed by this estimate. For an unturned wire, its two
arguments need not both belong to the high half-period; (23) is
applied only to the incidences satisfying its hypothesis.

This gives general control of the previously unestimated high-index
free polynomial. It does not prove that the cost in (24) lies below
the selected geometric exponent. Nor does an upper bound establish
the nonzero coefficient of the remaining signed integral. Those
comparisons must be made with the actual original period.

## 5. Direct sources and scope

The proof uses the following recorded statements, with their full
normalization:

| Source | Implication used | SHA256 |
|---|---|---|
| `research_newton_interpolation_finite_fourier_band.md` | Equations (7)--(8), Theorem 2: entire physical data (5), cardinal representative, repeated-root derivatives | `2e2d95184081ba6440b56268cb597624d97a5f1931e8c0df886fa754e6684304` |
| `research_internal_wire_exact_circle_averaging.md` | Section 3 and the cardinal extension in Section 5: exact finite-network identity with the original free polynomial | `0efa85a43da064197f25422d86ef37688971f2dface55da9d5efef3ccb0d08ef` |

Section 1 of
`research_internal_pair_three_high_half_bound.md`
(`24b58d2a6a51964183da4abcc4cf3574a7b8f24c148202c7db3e9eccf8f11179`)
contains the prior fixed-height physical estimate. Its particular
power-three action comparison is not used. The low-index comparison
and the obstruction to extending its complete-boundary phase are in
Sections 1--6 of
`research_free_boundary_cardinal_factorial_comparison.md`
(`9ed5b69bad33d7e62a7b40070d86d9d2233f2c34bc7674ddcf8a82e8e0091d5d`).
They provide context, not an estimate imported into the high half-period.

All estimates above are written inequalities for the original finite
polynomial. No numerical calculation or finite test is a proof input.
