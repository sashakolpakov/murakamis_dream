# A common complex endpoint baseline with its original window currents

Private written proof, 16 November 2026.

The unturned microscopic kernel has a common polynomially bounded
analytic baseline on every buffered bounded subdomain of
\(0<\Re x<1/2\). Exact representatives on the two half-domains retain
both physical channels and differ from that baseline exponentially.
Their real interface and every exterior current remain explicit.
No extra complex characteristic-separation hypothesis is needed:
the original balanced two-component step is already \(I+O(N^{-1})\).

There is also a direct estimate for the entire positive-spectral-end
window of a filled-leaf trace, including the derivative of the outgoing
kernel. That window has arbitrarily small exponential cost. Neither
result supplies the still-missing generic-parameter scalar seed for
the filled leaf: the opposite endpoint and the coherent interface
remain to be estimated at the terminal action.

## 1. Original data and the complex domain

Put \(h=N^{-1}\), \(D=N-1\), \(\eta=(-1)^D\), and retain
\[
 c_N(x)=2\cos(2\pi x+\pi h),\qquad x_j=jh,\qquad
 c_j=c_N(x_j),\qquad w_N(\alpha)=2\cosh(\alpha h),
\]
\[
 e_k(Z)=S_k^{-2}\prod_{a<k}(c_a-Z),\qquad
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),\qquad
 B_N(Z,\alpha)=K_N(w_N(\alpha),Z)=\sum_{k=0}^D e_k(w_N)e_k(Z).
 \tag{1}
\]
The trace is the original full Hermite functional:
\[
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
       \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
             +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{2}
\]
All endpoint parameters below range over arbitrary fixed bounded
complex disks. Larger disks are used for parameter derivatives.

Fix a real compact interval \(I\Subset(0,1/2)\), with larger real
buffers, and a bounded target rectangle whose closure lies in
\[
                         \mathcal V=\{0<\Re x<1/2\}.
 \tag{3}
\]
Enlarge the rectangle, still inside \(\mathcal V\), to contain the
real buffers and choose three nested rectangles with fixed positive
separations. Every bounded compact subset of \(\mathcal V\), together
with a chosen real base interval, admits this construction. Thus the
statement below also applies to arbitrary such compact subdomains.
The rectangles and all their margins are independent of \(N,\alpha\).

**Theorem 1.** There is a jointly holomorphic baseline
\(A_N^0(x,\alpha)\), polynomially bounded on the target rectangle,
and constants \(C,p,\kappa>0\), such that on the buffered real window
\[
 \begin{split}
 \varepsilon_j&=B_N(c_j,\alpha)-A_N^0(x_j,\alpha),\\
 \omega_j&=c_N'(x_j)\partial_ZB_N(c_j,\alpha)
                             -\partial_xA_N^0(x_j,\alpha),
 \end{split}
 \qquad |\varepsilon_j|+|\omega_j|\le C N^p e^{-\kappa N}.
 \tag{4}
\]
There are exact scalar representatives
\[
                 H_N^\sigma=A_N^0+C_N^\sigma,\qquad \sigma=\pm1,
 \tag{5}
\]
whose value and \(x\)-derivative equal the two original data in (4)
at every node of the window. On every fixed compact part of the
target rectangle with \(\sigma\Im x\ge0\),
\[
                |C_N^\sigma|\le C'e^{-\kappa_1N}.
 \tag{6}
\]
All fixed derivatives have the same form on smaller domains.
The constants may depend on the target height and buffers, but the
one-sided repair in (6) does not lose an exponential factor at that
height. The baseline and representatives are not asserted to be
periodic or to extend through the two real spectral endpoints.

## 2. The exact near-identity step and the common baseline

Write \(s_r=2\sin(\pi r/N)\), and set
\[
 A_N(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C_N(r)=\frac{s_r^4}{s_{2r}s_{2r+1}},
\]
\[
 q_N(x)=\frac{C_N(Nx)}{A_N(Nx)},\qquad
 d_N(x)=\frac{c_0-w_N(\alpha)}{A_N(Nx)},\qquad
 T_N(x)=
 \begin{pmatrix}1+d_N&h q_N\\d_N/h&q_N\end{pmatrix}.
 \tag{7}
\]
For \(F_j=B_N(c_j,\alpha)\) the exact physical value state is
\[
                  X_j=(F_j,h^{-1}(F_j-F_{j-1}))^t,
                    \qquad X_{j+1}=T_N(x_j)X_j.
 \tag{8}
\]
This is the original kernel recurrence. Its ordinary endpoint
source is retained; its value and first derivative vanish at the
bulk nodes used in (8), as established in the two-channel source.

On every buffered rectangle in (3), direct substitution gives
\[
 A_N(Nx)=\tan^2(\pi x)+O(h),\quad q_N=1+O(h),\quad
 d_N=O(h^2),\qquad T_N=I+hB_h,\quad \|B_h\|\le C.
 \tag{9}
\]
The assertions are holomorphic and uniform on larger bounded
parameter disks. The sine and cosine zeros in the exact coefficients
are real and approach the boundaries of (3); no denominator vanishes
on these rectangles for large \(N\). Their limiting factors are
units there. Cauchy's estimates give every fixed derivative.
This verifies (9) at any fixed complex height in the strip, not
only in the original thin interpolation tube.

The full endpoint-product bound and Markov's inequality give
\(\|X_j\|\le CN^p\) on the real buffers. We apply the bounded modified
differential-equation construction from the one-sided continuation
source directly to (9). Here is its estimate in the present setting.
For a bounded analytic matrix \(A\), let \(\Phi_h(A;x)\) be its
fundamental flow from \(x\) to \(x+h\), and put
\[
 Q_h(A)=\frac{\Phi_h(A)-I}{h}-A,\qquad
                      \mathcal F_h(A)=B_h-Q_h(A).
 \tag{10}
\]
Between domains eroded by \(\delta\ge2h\), the flow integral and
Cauchy's estimate imply, on a fixed bounded matrix ball,
\[
 \|Q_h(A)-Q_h(\widetilde A)\|
                \le C(h+h/\delta)\|A-\widetilde A\|.
 \tag{11}
\]
Indeed the two terms in \(Q_h\) are the average of
\(A(x+s)-A(x)\) and the average of \(A(x+s)(\Phi_s(A)-I)\).
Their differences cost respectively \(Ch/\delta\) and \(Ch\).

Start at \(A^{(0)}=B_h\). A fixed initial shrink makes its first
increment \(O(h)\). Thereafter choose \(\delta=Mh\) with fixed
large \(M\), so (11) is at most \(1/2\). A fixed remaining buffer
permits \(K\ge c/h\) iterations. They remain in the bounded ball
and give a bounded analytic matrix \(A_h\) with
\[
                  \Phi_h(A_h;x)-T_N(x)=O(e^{-c_1/h}).
 \tag{12}
\]
Reserve another fixed buffer for derivatives. This is a finite
analytic iteration, with an estimated residual, not a formal series.

Solve \(Y'=A_hY\) with \(Y(x_{j_*})=X_{j_*}\) at an actual interior
row. Rectangular paths have bounded lengths, so both its fundamental
matrix and inverse have bounds \(e^{CL}\). Hence \(Y\) has polynomial
norm throughout the target rectangle. On the real buffer,
\(\|T_N^{\pm1}\|\le1+Ch\); comparison of its steps with (12), in
both directions, gives
\[
                          Y(x_j)-X_j=O(N^p e^{-c_2N}).
 \tag{13}
\]
Take \(A_N^0\) to be the first component of \(Y\).

The derivative assertion in (4) is not inferred from (8).
Use the actual scalar Hermite representative supplied by the bulk
compatibility theorem on a fixed thin real tube. It and \(A_N^0\)
have polynomial analytic norms. Repair the exponentially small nodal
differences in (13) temporarily with a finite sinc sum. On a
sufficiently narrow buffered tube the repair, and its derivative,
remain exponentially small. The repaired functions have \(cN\)
common zeros in each local disk. The disk Blaschke estimate, followed
by Cauchy's formula and a finite cover, makes their derivative
difference exponentially small on an inner tube. Undoing the temporary
repair proves the second equation of (4). This uses the proved
normal compatibility of the actual unturned kernel.

## 3. Exact one-sided Hermite repair and the original interface

Sum over the window's nodes and define
\[
 L_j^\sigma(x)=e^{\sigma2\pi i(x-x_j)/h}
                  \operatorname{sinc}^2((x-x_j)/h),
\]
\[
 C_N^\sigma(x)=\sum_j
  [\varepsilon_j+(\omega_j-\sigma2\pi i\varepsilon_j/h)(x-x_j)]
                                                  L_j^\sigma(x).
 \tag{14}
\]
At its own node the summand has value \(\varepsilon_j\) and
derivative \(\omega_j\);
at every other node it has a double zero. The Fourier support of
\(L_j^+\) is \([0,2/h]\), and of \(L_j^-\) is \([-2/h,0]\), with
absolute coefficient mass one. Thus \(|L_j^\sigma|\le1\) on its
designated half-plane. Formula (4), the \(O(N)\) summands, and the
fixed bounded domain prove (6). Fixed derivatives add polynomial
factors. On the opposite half-plane the cost is
\(e^{4\pi|\Im x|/h}\), so only a sufficiently thin fixed opposite
collar is asserted.

Use the uncentered grid kernel
\[
                         D_h(x)=(\pi/h)^2\csc^2(\pi x/h).
 \tag{15}
\]
Writing \(z=x-x_j\), \(k=2\pi i/h\), the exact cancellation is
\[
 D_h(C_N^+-C_N^-)
 =\sum_j\frac{[\varepsilon_j+(\omega_j-k\varepsilon_j)z]e^{kz}
                    -[\varepsilon_j+(\omega_j+k\varepsilon_j)z]e^{-kz}}{z^2}.
 \tag{16}
\]
The apparent singularity at zero is removable, with value
\(4\pi i\omega_j/h\). For real \(z\), separate \(|z|\le h\) and
\(|z|\ge h\), using Taylor's formula in the first region. Each
term is at most
\(C(h^{-2}|\varepsilon_j|+h^{-1}|\omega_j|)\). Consequently
\[
          \sup_{\text{real window}}|D_h(C_N^+-C_N^-)|
                                  \le C e^{-\kappa_2N}.
 \tag{17}
\]
The constants \(\kappa_1,\kappa_2\) are positive, not freely adjustable.

For a fixed shared product of microscopic kernels, multiply the
baselines and, separately, the two exact representatives. The
ordinary product rule preserves all first normals. A telescoping
product difference and (16)--(17) give the same exponential real
interface bound with a changed polynomial prefactor. All shared
parameters remain shared.

Let \(A_N(Z;\mathbf y)\) be the whole remaining actual spectator,
with any other traces still unapplied. Include the original crossing
through
\[
 \tau_N(x)=\pi-2\pi x-\pi h,\quad
 E_{N,n}(x)=\mathfrak c_{N,n}e^{inN\tau_N(x)^2/(4\pi)},\quad
 \mathfrak c_{N,n}=e^{\pi i nD^2/(4N)}.
 \tag{18}
\]
For a positive-row window \(j_0\le j\le j_1\), choose midpoint
boundaries \(a_N=(j_0-\tfrac12)h\), \(b_N=(j_1+\tfrac12)h\)
and exterior half-contours inside the target rectangle. Put
\[
 g_\sigma(x)=\sin(2\pi x+\pi h)\,
                    H_N^\sigma(x)E_{N,n}(x)A_N(c_N(x);\mathbf y).
 \tag{19}
\]
For shared products replace \(H_N^\sigma\) by their product. Then
the original restricted full trace is exactly
\[
 -\frac{\eta}{2\pi^2i}\left\{
   \int_{E_-}D_hg_-\,dx+\int_{E_+}D_hg_+\,dx
       +\int_{a_N}^{b_N}D_h(g_+-g_-)\,dx\right\}.
 \tag{20}
\]
Here \(E_-\) runs down the left side, across the bottom, and up
the right side; \(E_+\) runs up the right side, across the top,
and down the left side. All vertical half-sides are included.
To check normalization, if \(g=\sin(2\pi x+\pi h)f(c_N(x))\),
then \(g'(x_j)=-\pi\{(4-c_j^2)f'(c_j)-c_jf(c_j)\}\).
The residue of \(D_hg\) is \(g'(x_j)\). The interface sign follows
by closing the upper half-contour with the real path from \(a_N\)
to \(b_N\); the difference has no grid poles because its two jets
vanish. This proves (20) with the original crossing normal.

The interface in (20) is bounded pointwise by
\[
 C e^{-\kappa_2N}
       |\sin(2\pi x+\pi h)E_{N,n}(x)A_N(c_N(x);\mathbf y)|.
 \tag{21}
\]
No spectator is factored or replaced. On real rows the crossing
has modulus one. On midpoint verticals and nonzero horizontal
heights, \(D_h=O(N^2e^{-2\pi N|\Im x|})\); all its original aliases
are retained. The exterior integrals are still present.

For every fixed positive power \(m\ge2\), the selected terminal
saddle satisfies \(0<\Re t_m<\pi\), \(\Im t_m<0\).
For power \(-m\), use the reflected Fourier sector on this right
angular chart: its saddle is \(t_{-m}=\overline{t_m}\), so
\(\Im t_{-m}>0\). Equivalently, the source's reflection
\(t\mapsto-\overline t\) is followed by the even angular reflection
back to the right chart; the Fourier sector is reflected with it.
Under \(t=\tau_N(x)\), both nearby fixed charts lie in (3) for
large \(N\). The positive-power saddle uses \(H_N^+\), since
\(\Im x>0\); the negative-power saddle uses \(H_N^-\), since
\(\Im x<0\). Theorem 1 therefore supplies the unturned insertion
there with no additional exponential amplitude cost. This removes
a complex-baseline continuation obstacle; it does not estimate the
other terms in (20) or assert a filled-leaf scalar seed.

## 4. The actual positive-endpoint window, with both kernel channels

Let \(M_{a,N}=K_N(c_a,-2)\). The positive-row source proves
\[
 M_{a,N}\le(a+1)(C_0N/a)^{2a},\qquad C_0=\pi e^2/2,
 \qquad
 M_{a,N}\le N e^{N h_0(\varepsilon)}
 \quad(a\le\varepsilon N),
\]
\[
                    h_0(\varepsilon)=2\varepsilon\log(C_0/\varepsilon).
 \tag{22}
\]
The case \(a=0\) is read separately as \(M_{0,N}=1\).
Write \(Q_{a,N}(Z)=\partial_1K_N(c_a,Z)\); it need not have
the low degree of \(K_N(c_a,Z)\).

For fixed \(0<\varepsilon<1/8\), uniformly for
\(0\le a\le\varepsilon N\) and all sufficiently large \(N\),
\[
 \|K_N(c_a,\cdot)\|_{[-2,2]}
          +N^{-2}\|Q_{a,N}\|_{[-2,2]}
                       \le C N^2 M_{a+1,N}.
 \tag{23}
\]
Indeed \(c_a-c_{a+1}=4\sin(2(a+1)\pi/N)\sin(\pi/N)\ge c/N^2\),
with an absolute positive margin in this range. Choose an absolute
\(\rho>0\) so the disk \(|w-c_a|\le\rho/N^2\) lies in
\(|w-2|\le2-c_{a+1}\). The physical-row root product, whose roots
are all above \(2\), gives
\[
                 |K_N(w,c_j)|\le K_N(c_{a+1},c_j)\le M_{a+1,N}.
 \tag{24}
\]
The distinct-node low interpolant consequently has real norm at most
\(NM_{a+1,N}\). The remaining high Newton factors each have real
norm at most \(\sqrt{N-1}\). The disk just chosen lies in a Bernstein
ellipse of parameter \(e^{C/N}\): its endpoint extension is
\(O(N^{-2})\) and its minor semiaxis is \(O(N^{-1})\).
Their values in that disk are therefore at most \(C\sqrt N\).
The entire high sum has real norm \(O(N^2)\). This proves
\(\sup_{|w-c_a|\le\rho/N^2}\|K_N(w,\cdot)\|\le CN^2M_{a+1,N}\);
Cauchy's formula proves (23). The entire first normal, not just
the derivative of the low physical row, is bounded here.

Now fix any integer \(n\) and any fixed microscopic product
\(B(Z)=\prod_i K_N(w_N(\alpha_i),Z)\). Let \(W_{N,\varepsilon}(Z)\)
be the literal part of \(\phi_N[R^n B K_N(\cdot,Z)]\) with
\(0\le a\le\varepsilon N\). Every term of (2) and its full product
derivative is retained. The bound for \(B,B'\) is polynomial by
the endpoint-product theorem and Markov. The original crossing
values and first normals cost a polynomial, by (18) and
\(dZ/d\tau=2\sin\tau\). Equations (22)--(23) thus give
\[
 \boxed{\quad
 \sup_{|\boldsymbol\alpha|\le A}
 |W_{N,\varepsilon}(-2\cos u)|
       \le C N^p
             \exp\{N[h_0(2\varepsilon)+|\Im u|]\}.
 \quad}
 \tag{25}
\]
For the real-output estimate, sum the \(O(N)\) rows after applying
(23); \(a+1\le2\varepsilon N\) for large \(N\).
The resulting ordinary output polynomial has degree at most \(D\).
Its Chebyshev coefficient bound gives the displayed complex
continuation, with a polynomial factor. In particular the
continuation cost is \(|\Im u|\), not
\(\varepsilon|\Im u|\): \(Q_{a,N}\) can still have degree \(D\).
Fixed output and microscopic-parameter derivatives have the same
form on smaller parameter sets, with polynomial losses.

Since \(h_0(2\varepsilon)\to0\), this actual endpoint window is
strictly below any fixed positive terminal action on a sufficiently
small fixed output disk. It includes neither the opposite spectral
endpoint nor a connecting integral. It is not a scalar seed by itself.

## 5. The remaining action budget and a real product-rate diagnostic

The baseline theorem provides a positive \(\kappa_2\), but does not
prove that it pays the whole terminal deficit. At real complete
output the reference edge rate is \(M_\infty=4G/\pi\), whereas
\(\mathcal I_2=2G/\pi\). An absolute real-interface estimate from
(21) has reference budget \(M_\infty-\kappa_2\), so this route
would require \(\kappa_2\ge M_\infty-\mathcal I_n\).
The explicit two-subgrid estimate in the scalar-compatibility source
supplies \(R\log3/16\) on a buffered \(x\)-disk of radius
\(R<\min(x,1/2-x)\le1/4\), before subsequent losses.
These displayed constants do not establish the required inequality:
\[
             \log3/64<\log2/4<2G/\pi=M_\infty-\mathcal I_2.
 \tag{26}
\]
For the middle inequality, integrate \(\log\cot s>\log2\) on
\((0,\pi/8)\). This comparison does not upper-bound the true
error exponent or prove growth of the actual interface.

There is an exact real diagnostic from the central lowering products
in the scalar source. Put \(z=\sin^2(t/2)\), \(0<t<\pi\), and
\[
 J_\delta(t)=-\int_0^\delta
           \log\left|\frac{z-\sin^2(\pi u)}{\cos^2(\pi u)}\right|du,
                      \qquad 0<\delta<1/2.
 \tag{27}
\]
This is their logarithmic product rate. To check the statement on
real angles, take nearest midpoint sequences \(t_N=t+O(N^{-1})\),
at distance at least \(c/N\) from each product zero. Factor the numerator as
\(\sin(t/2+\pi u)\sin(t/2-\pi u)\). Removing its possible logarithmic
zero leaves smooth Riemann sums; the removed shifted factorial sum
has \(O(\log N)\) error. The two parity offsets change that error
only by \(O(\log N)\). The bounded microscopic parameter perturbation
of the cosine factor contributes \(O(N^{-1})\) to the logarithm.
Thus the finite products from the scalar source have logarithm
\(-NJ_\delta(t)+O(\log N)\) along these midpoint sequences.
At actual zeros they vanish; no nonzero rate is assigned there.

For each \(t\), the unique maximum is obtained at
\[
 \sin^2(\pi\delta_*)=(1+z)/2,\qquad
 J_*(t):=J_{\delta_*}(t)
       =\frac1\pi\int_t^\pi\operatorname{asinh}(\sin(s/2))\,ds.
 \tag{28}
\]
Indeed the \(\delta\)-derivative in (27) changes sign precisely
when the absolute ratio is one. Differentiation in \(t\), with
the logarithmic singularity interpreted as its elementary principal
value, gives
\[
 J_*'(t)=-\frac{\sin(t/2)\cos(t/2)}{\pi}
  \operatorname{PV}\int_0^{\pi\delta_*}
       \frac{dv}{\sin^2(t/2)-\sin^2v}
             =-\frac{\operatorname{asinh}(\sin(t/2))}{\pi}.
 \tag{29}
\]
For the last equality substitute \(y=\tan v\); the real
antiderivative is an inverse hyperbolic cotangent at the upper
endpoint. The boundary term is zero because its logarithm is zero.
The limit \(J_*(\pi)=0\) fixes (28): away from \(u=1/2\) the
logarithm in (27) tends uniformly to zero, and its remaining
shrinking endpoint interval has an integrable logarithmic bound
with integral tending to zero.
Also \(\int_0^{\pi/2}\operatorname{asinh}(\sin v)\,dv=G\):
differentiating the same integral with a parameter \(k\) multiplying
\(\sin v\) gives \(\arctan k/k\), then integrate \(0\le k\le1\).
Consequently \(J_*(0)=2G/\pi\).

The calibrated edge derivative is
\(\psi_t(t,0)=-\operatorname{asinh}(\tan(t/2))/\pi\). Hence
\[
                 \psi(t,0)-J_*(t)\le\mathcal I_2,
 \tag{30}
\]
strictly for \(t>0\); near zero the difference is
\(\mathcal I_2-t^4/(64\pi)+O(t^6)\).
This compares an exact real central-product rate with the action.
It is not an estimate for the baseline error, its real interface,
or their coherent complex continuation. In particular (28)--(30)
do not establish the missing generic-parameter filled-leaf seed.

## 6. Coverage and direct sources

The thin scalar compatibility, one-sided cardinal repair, and
modified differential equation are prior results. The additional
assembly uses the actual unturned near-identity system on the
whole buffered vertical strip, without a new characteristic
separation premise, and supplies the full-normal estimate (25).
The hypergeometric value-connection theorem supplies a real-bulk
leading profile, not a controlled fixed-height alias remainder;
it is not used as a substitute for the source current.

The following complete sources were read at unchanged pins, with
their used implications checked:

* [Actual two-channel recurrence](research_microscopic_endpoint_two_channel_interpolation.md),
  SHA256 44f6db0f8afdf1205ab8b0935b95b8a4fd9fa16c6414be2467b8b40a123c0ffe.
* [Actual unturned scalar compatibility](research_microscopic_endpoint_bulk_scalar_compatibility.md),
  SHA256 2b8713ed16b66f5faa004403ac1d032021eee0a6f8f38082481d002c672c0b2e.
* [Bounded modified ODE and one-sided repair](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_terminal_one_sided_characteristic_continuation.md),
  SHA256 1316cfb9ed7fec208a8aa8308ea7015c7cf32534a8662500892f9a62b5e9b475.
* [Full endpoint products and original trace](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.
* [Positive-row coefficient mass](research_physical_row_charge_transport.md),
  SHA256 d09d5c669848f0389504cea613244570eca18be03f2b608a359773e423e97040.
* [Original terminal action calibration](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Frozen notes and public manuscripts are unchanged.
