# The exact shortened kernel at a decorated local terminal saddle

Private written proof, 16 November 2026.

For every fixed signed power of magnitude at least three, the exact
shortened outgoing kernel has a nonzero holomorphic amplitude near
the calibrated terminal saddle. Its logarithmic derivatives are
\(O(\log N)\). This is sufficient for a relative local Gaussian
formula with the actual microscopic endpoint insertion. The proof
uses the original shortened kernel and rational trace denominator;
no bare terminal contraction is moved through the insertion.

The local coefficient may depend polynomially on \(N\). This note
does not give a whole-cycle lower bound, a fold estimate, or a
nonzero lower bound for an output derivative.

## 1. Exact outgoing source and selected points

Put \(h=N^{-1}\), \(D=N-1\), \(\eta=(-1)^D\), and use
\[
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 S_k=\prod_{j=1}^k2\sin(\pi j/N).
 \tag{1}
\]
The exact shortened complete-output kernel used by the compact
contour theorem is
\[
 \Lambda_N(t)=K_N^<(-2\cos t,-2)
       =\sum_{k=0}^{\lfloor N/2\rfloor-1}
                           e_k(-2\cos t)e_k(-2).
 \tag{2}
\]
Its omitted high sector, including the odd middle polynomial, is
the explicit polynomial-budget original trace in that theorem.
It is not reinserted into the off-grid amplitude (2).

The original holomorphic phase is normalized by
\[
 \psi(t,0)=\int_0^{1/2}
     2\operatorname{asinh}\!\bigl(\cos(t/2)\cot(\pi u)\bigr)\,du,
 \tag{2a}
\]
continued from \(0<t<\pi\). The branch on the neighborhoods below
is its continuation within the original angular strip.

For \(m\ge3\), let \(t_m=2A_m-2iB_m\) be the calibrated
positive-power saddle at complete output. The source equations give
\[
 0<A_m<\pi/m,\quad B_m>0,\qquad
 \sin A_m=\cosh B_m\tanh(mB_m),
\]
\[
 \operatorname{asinh}(\tan(t_m/2))
                  =im t_m/2-i\pi.
 \tag{3}
\]
For \(n=\sigma m\), \(\sigma\in\{+1,-1\}\), use the right angular
chart
\[
 t_{n,*}=2A_m-i\sigma H_m,\qquad H_m=2B_m.
 \tag{4}
\]
For negative \(n\), this is the even angular reflection of the
usual lower-chart point \(-\overline{t_m}\). The reflected Fourier
sector is retained. Define
\[
 \Phi_{n,\sigma}(t)=
       \psi(t,0)+\frac{in}{4\pi}t^2-i\sigma t.
 \tag{5}
\]
Then
\[
 \Phi'_{n,\sigma}(t_{n,*})=0,\qquad
 \Re\Phi_{n,\sigma}(t_{n,*})=\mathcal I_n,\qquad
 \Re\Phi''_{n,\sigma}(t_{n,*})<0.
 \tag{6}
\]
These are identities for the original calibrated phase and signed
unit character.

Every point (4) lies strictly in the free-color half-plane required
by the row theorems, with a uniform elementary margin:
\[
                 \Re(-2\cos t_{n,*})<\frac32<2.
 \tag{7}
\]
Here is a proof for all \(m\ge3\), without an enumeration of powers.
Writing \(s=\sinh B_m\), one has
\[
 \cosh B_m\tanh(3B_m)
                   =\frac{s(3+4s^2)}{1+4s^2}.
\]
This expression increases with \(B_m\) and equals one when
\(s=1/2\). Equation (3) and \(\sin A_m<1\) therefore give
\[
 \sinh B_m<1/2,\qquad B_m<\operatorname{asinh}(1/2)<1/2.
 \tag{8}
\]
Since \(A_m<\pi/3\),
\[
 \Re\cos^2(A_m-iB_m)
   =\cos^2A_m+\cos(2A_m)\sinh^2B_m
   >\frac14-\frac12\frac14=\frac18.
\]
Now \(-2\cos t=2-4\cos^2(t/2)\), proving (7). For each fixed
power, reserve a complex neighborhood of the horizontal segment
through (4) whose image stays in \(\Re C<2\).

## 2. A nonzero source amplitude at both parities

**Lemma 1.** On a fixed sufficiently small complex neighborhood of
\(t_{n,*}\), the exact polynomial (2) has the representation
\[
       \Lambda_N(t)=\exp\{N\psi(t,0)+E_N(t)\},\qquad
       |\partial_t^kE_N(t)|\le C_k\log N
 \tag{9}
\]
for every fixed \(k\ge0\), at all sufficiently large levels of both
parities. In particular it is nonzero there, and \(e^{E_N}\) is
bounded above and below by fixed powers of \(N\).

*Proof.* At even \(N\), the exact low-kernel theorem compares (2)
with the actual last physical row by the relative factor
\(1+O_{\rm hol}(N^{-1/2})\). Its equation (21), using the last-row
normalization, is precisely (9) after \(C=-2\cos t\). The error
logarithm and all its fixed derivatives are \(O(\log N)\) on every
buffered compact subset of \(\Re C<2\). Thus the coefficient is
source-specific; it is not inferred from a whole terminal integral.

At odd \(N=2m_0+1\), the last physical color is \(-2\). The last-row
theorem gives
\[
 K_N(C,-2)=\exp\{N\Psi(C)+E_N^{\rm full}(C)\},\qquad
 |\partial_C^kE_N^{\rm full}|\le C_k\log N,
 \quad \Psi(-2\cos t)=\psi(t,0).
 \tag{10}
\]
The cutoff (2) removes the middle index \(m_0\) as well as the
higher radicals. The higher radicals vanish at \(-2\); the middle
one does not. Its exact formula is
\[
 e_{m_0}(C)=\frac{(-1)^{m_0}}{N}
              \{U_{m_0}(C/2)-U_{m_0-1}(C/2)\},
 \qquad e_{m_0}(-2)=1.
 \tag{11}
\]
It has real norm at most one. Its degree and Chebyshev continuation
therefore imply
\[
 |e_{m_0}(-2\cos t)|
             \le CN^p e^{m_0|\Im t|}.
 \tag{12}
\]
The middle term is exponentially smaller than (10) near the
selected saddle. Indeed calibration gives
\[
 \Re\psi(t_m,0)
   =\mathcal I_m+
               \left(1-\frac{mA_m}{\pi}\right)H_m
   >\mathcal I_m\ge\mathcal I_2>\frac12>B_m.
 \tag{13}
\]
For the elementary strict inequality \(\mathcal I_2>1/2\), use
\(\mathcal I_2=2G/\pi\) and
\(G=\int_0^1\arctan u\,du/u>\pi/4\); strict concavity puts
\(\arctan u\) above the chord \(\pi u/4\) for \(0<u<1\).
The gap in (13) persists on a small complex neighborhood.
Equations (10)--(12) consequently give
\[
 \frac{e_{m_0}(-2\cos t)}{K_N(-2\cos t,-2)}
                         =O_{\rm hol}(e^{-cN})
 \tag{14}
\]
after reducing \(c>0\), including every fixed derivative.
Since \(\Lambda_N=K_N(\cdot,-2)-e_{m_0}\) exactly, add the
holomorphic logarithm of \(1\) minus the ratio (14) to
\(E_N^{\rm full}\). This proves (9) at odd levels. The negative
power case is its coefficientwise conjugate. \(\square\)

The middle-index correction in (11)--(14) is necessary: at odd
levels the shortened sum (2) is not literally the full kernel.

## 3. Actual local insertion and the exact trace prefactor

Let \(r\ge0\) be fixed and let the endpoint parameters be real with
\(|\alpha_i|\le A\). Choose the sharp designated-half representatives
of the actual shared product, on a patch containing the selected
point, and put
\[
 x_N(t)=\frac{\pi-\pi/N-t}{2\pi},\qquad
 \mathcal B_N(t)=\prod_{i=1}^r
       H_{i,N}^{\sigma}(x_N(t),\alpha_i).
 \tag{15}
\]
These preserve the original physical values and first normals.
At (4), \(\sigma\Im x_N>0\) and \(0<\Re x_N<1/2\) for large
\(N\). In this strip the imaginary part of
\(\sin(\pi x)\) has the sign of \(\Im x\); hence
\(\Im\Log\sin(\pi x_N)\) is bounded away from zero on a small
fixed neighborhood of the selected point. On that common
complex neighborhood, the nonreal insertion theorem gives
\[
 |\mathcal B_N(t_{n,*})|\ge cN^{-r},\qquad
 |\partial_t^k\mathcal B_N(t)|
                \le C_k\left(\frac{1+\log N}{N}\right)^r.
 \tag{16}
\]
This includes \(\alpha_i=0\), shared factors and \(N\)-dependent
real parameters in the compact interval. The \(O(N^{-1})\) shift
in \(x_N\) stays in that same fixed nonreal compact; its derivative
is the fixed constant \(-1/(2\pi)\). Thus (16) follows directly
from the spatially uniform theorem. For \(r=0\), use
\(\mathcal B_N=1\).

Retain the original carrier and rational sampling kernel
\[
 C_{N,n}=e^{\pi i nD^2/(4N)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{17}
\]
Choose a small fixed \(a>0\) so the horizontal segment
\(t=t_{n,*}+u,\ |u|\le a\), lies inside all the reserved
neighborhoods. The exact favored-half contribution of this segment
to the original shortened trace, with positive \(u\)-orientation, is
\[
 \mathfrak L_{N,n}^{\rm loc}
  =\frac{\sigma iN^2}{\pi}\,C_{N,n}
     \int_{-a}^{a}
       \sin t\,\Lambda_N(t)\mathcal B_N(t)
          e^{inNt^2/(4\pi)}W_N(t)\,du.
 \tag{18}
\]
To check the normalization, the compact source has prefactor
\(-\eta/(2\pi^2i)\), and
\[
 D_h(x)=-4\eta\pi^2N^2W_N(t),\quad
 dx=-dt/(2\pi),\quad \sin(2\pi x+\pi h)=\sin t.
 \tag{19}
\]
For positive \(n\), the upper \(x\)-horizontal side maps to
increasing real \(t\). For negative \(n\), the lower \(x\)-side
maps to decreasing real \(t\), producing the additional sign
\(\sigma\) when (18) is written with increasing \(u\).
Both carriers and orientations are thus inherited from the actual
full-normal trace.

On this segment the exact identity is
\[
 W_N(t)=e^{-i\sigma Nt}
             (1-\eta e^{-i\sigma Nt})^{-2}.
 \tag{20}
\]
For \(\sigma=-1\), it follows by dividing numerator and denominator
by \(e^{-2iNt}\); \(\eta^2=1\). Since
\(|e^{-i\sigma Nt}|=e^{-NH_m}\),
the last factor is \(1+O(e^{-NH_m})\), with all fixed derivatives
costing only powers of \(N\). Formula (20) retains all aliases
before estimating them.

## 4. Relative Gaussian formula with the actual slow amplitude

**Theorem 2.** Put
\(\lambda_n=-\Phi''_{n,\sigma}(t_{n,*})\), so \(\Re\lambda_n>0\).
Choose its square root with positive real part. Uniformly for the
real endpoint parameters in (16),
\[
 \boxed{\quad
 \mathfrak L_{N,n}^{\rm loc}
 =\frac{\sigma iN^{3/2}}{\pi}\,C_{N,n}\,
       e^{N\Phi_{n,\sigma}(t_{n,*})+E_N(t_{n,*})}
       \mathcal B_N(t_{n,*})\,\sin t_{n,*}
       \sqrt{\frac{2\pi}{\lambda_n}}\,[1+o(1)] .
 \quad}
 \tag{21}
\]
The local coefficient is nonzero for all sufficiently large \(N\),
and the logarithmic growth rate of its absolute value is
\(\mathcal I_n\). No limit of its \(N\)-dependent polynomial
amplitude is asserted.

*Proof.* Reduce \(a\) so
\[
 \Re(\Phi(t_{n,*}+u)-\Phi(t_{n,*}))\le-cu^2
                       \quad(|u|\le a)
 \tag{22}
\]
and all source bounds hold on a larger complex neighborhood.
From (9),
\[
 |E_N(t_{n,*}+u)-E_N(t_{n,*})|
                              \le C|u|\log N.
 \tag{23}
\]
The insertion bounds give
\[
 \left|\frac{\mathcal B_N(t_{n,*}+u)}
                    {\mathcal B_N(t_{n,*})}-1\right|
                           \le C(1+\log N)^r|u|.
 \tag{24}
\]
The sine is nonzero at the saddle. Equations (20),(23),(24)
therefore show that the normalized amplitude differs from
\(\sin t_{n,*}\) by at most
\[
 C(1+\log N)^{r+1}|u|e^{C|u|\log N}
                    +CN^p e^{-NH_m}e^{C|u|\log N}.
 \tag{25}
\]
The separately normalized amplitude need not have a uniform bound
on a fixed neighborhood. Instead use
\[
 C|u|\log N\le \tfrac14cNu^2+C'\frac{(\log N)^2}{N}.
 \tag{26}
\]
Thus its growth is absorbed into the actual Gaussian bound (22).
Integrating (25) against that bound costs
\(O((1+\log N)^{r+1}/N)\), plus an exponentially small term.

Taylor's formula gives
\(\Phi(t_{n,*}+u)=\Phi(t_{n,*})-\lambda_nu^2/2+O(u^3)\).
After another fixed reduction of \(a\), the cubic remainder is
absorbed into a further portion of the quadratic decay. Its
integrated error is \(O(N^{-1})\): bound the difference of the
two exponentials by \(CN|u|^3e^{-c'Nu^2}\) and integrate.
The Gaussian outside \([-a,a]\) is exponentially small, and
\[
 \int_{\mathbb R}e^{-N\lambda_nu^2/2}\,du
                      =N^{-1/2}\sqrt{2\pi/\lambda_n}.
 \tag{27}
\]
Equations (25)--(27) give a relative error
\(O((1+\log N)^{r+1}/\sqrt N)=o(1)\). Substitution into
(18) proves (21).

All its displayed factors are nonzero: \(\sin t_{n,*}\ne0\),
\(\Re\lambda_n>0\), the exact exponential in (9) never vanishes,
and (16) bounds the insertion away from zero polynomially.
Their logarithms have size \(O(\log N)\), apart from the stated
phase. Formula (6) proves the rate assertion. \(\square\)

This proof adapts the local multiplier argument to the actual
\(N\)-dependent slow amplitude. It does not assert that the
separately uniformly bounded bare-amplitude hypothesis in the
earlier conditional corollary holds automatically.

## 5. Scope and direct sources

Equation (18) is an actual local piece of the exact shortened
horizontal contour, with its original carrier, sampling aliases
and consumed traced normal. The compact-current theorem retains
the outgoing high trace, the real interfaces, internal seams,
both outer sides and all physical rows outside the compact
windows. This note adds no estimate for the fold join and no
claim that other original contributions cannot cancel (21).
Fixed output normals remain in that source assembly; (21) is
a nonzero value coefficient at complete output, not a lower
bound for those derivatives.

The power-two saddle has \(\Re(-2\cos t_2)=2\), outside the
half-plane assertion used here. No extension to \(n=\pm2\)
is inferred from its different bare terminal contraction.

All complete direct sources were read at the following matching
pins, and their used implications were checked:

* [Even low complete-end kernel](research_even_complete_low_kernel.md),
  SHA256 ea3a8b7becbed501a28969f9cd6715c2b5e0b660aba7c5eb57229b1977220ed1.
* [Last physical row normalization](research_last_physical_row_riccati.md),
  SHA256 a6a79106b81b94f5d163022b056c9c6a51e0cdb4f602f090c9f3401436f87c7d.
* [All-power phase calibration](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd.
* [Original outgoing kernel bounds](research_mixed_next_incoming_color_kernel_upper_bounds.md),
  SHA256 9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db.
* [Compact source contours](research_sharp_endpoint_compact_interface_and_seams.md),
  SHA256 178e49b99b51fe767bc29ceadafb00159c179cd42f9ba5469921f64a6eabdde9.
* [Actual nonreal microscopic insertion](research_endpoint_nonreal_insertion_lower_bound.md),
  SHA256 ab3b4687b53c2168d22342c0e822b243a563f716d2a7a0de18d87c372546d7d0.

Only written mathematics and source text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Adopted notes and public manuscripts are unchanged.
