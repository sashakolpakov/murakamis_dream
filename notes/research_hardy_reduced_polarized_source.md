# A height-free Hardy polarization of the reduced source

Private written proof, 22 November 2026.

The canonically reduced numerator admits a polarized source with no
contour heights. Its local operators are ordinary orthogonal Fourier
projections followed by the original derivative sampling. Their
Chebyshev row norms grow only polynomially at real powers and charges.
The corresponding coupons have an explicit finite parity-sum formula.
An endpoint-current estimate proves that this source has the actual
nonzero small-charge initializer, to every fixed order.

The derivative closing is retained literally. It is not a positive
norm, and these local bounds do not give the sharp geometric upper
bound for the whole source.

## 1. The exact zero-height operators

Fix \(N\ge2\), \(D=N-1\), and write
\[
 \eta=(-1)^D,\qquad \tau_j=\frac{\pi(D-2j)}N,\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N).
 \tag{1}
\]
The representative of a class in \(\mathcal A_N\) always has degree
less than \(N\). Both spectral values and the first normals at double
roots remain; the odd simple root has its original value condition.

Let \(p\) be this representative and set
\[
 f_{n,\chi,p}(t)=
 \sin t\,p(-2\cos t)
       \exp iN\left\{\frac{nt^2}{4\pi}+(1-\chi)t\right\},
                  \qquad -\pi\le t\le\pi .
 \tag{2}
\]
Join the endpoints periodically. Since \(f(\pi)=f(-\pi)=0\), the
joined function is continuous and piecewise smooth. Its first
derivative may jump at that joining point. No periodic continuation
of the Gaussian as an analytic function is asserted.

On the circle with normalized Haar measure, let \(P_+\) and \(P_-\)
be the orthogonal projections onto the strictly positive and strictly
negative integer Fourier frequencies. Define
\[
 \mathscr T_{\sigma,n,\chi}[p]
       =2\eta\sum_{j=0}^{D}
             (P_\sigma f_{n,\chi,p})'(\tau_j),
                         \qquad \sigma\in\{+,-\}.
 \tag{3}
\]
The derivatives at these points are well defined. The grid has distance
at least \(\pi/N\) from the only possible joining singularity.

These operators are the actual zero-height limits of the full-midpoint
operators in the direct source:
\[
 \mathscr T_{\sigma,n,\chi}[p]
       =\lim_{h\downarrow0}
          \{\mathcal H_{\sigma,n,\chi}^h+
                         \mathcal V_{n,\chi}^h\}[p].
 \tag{4}
\]
The limit is taken at fixed \(N\), locally uniformly in the complex
parameters \(n,\chi\). It is not an interchange with \(N\to\infty\).

Here is a boundary-distribution proof of (4). On the lower line,
\[
 W_N(t)=\sum_{a\ge1}a\eta^{a-1}e^{-iaNt}.
 \tag{5}
\]
At every interior grid point its boundary value is a double-pole
distribution. Localize in disjoint neighborhoods of those points,
using smooth cutoffs supported away from the joining point. The
holomorphic functions in (2), evaluated at \(s-ih\), converge in every
local smooth test-function norm. The boundary distributions of
\(W_N(s-ih)\) therefore give the limit on these neighborhoods.
On the remaining part of the interval the denominator stays away
from zero and ordinary convergence applies, including at the two
midpoint endpoints. This justifies the limit without replacing
\(f(s-ih)\) by a fictitious periodic analytic continuation.

Equivalently one may use the Abel boundary value of (5) against the
joined function. If \(\widehat f_k\) are its Fourier coefficients,
the plus limit is
\[
 2iN^2\sum_{a\ge1}^{\rm Abel}
                      a\eta^{a-1}\widehat f_{aN}.
 \tag{6}
\]
Derivative sampling of \(P_+f\) gives
\(iN^2\sum_{a\ge1}^{\rm Abel}a\eta^a\widehat f_{aN}\).
Multiplication by \(2\eta\) proves (3) for the plus sign.
For the minus horizontal, its test function is \(-f(-t)\).
Reflection of the symmetric grid changes the positive projection
into \(P_-\), proving the minus formula. The vertical integral tends
to zero: at fixed \(N\), its path length is \(2h\) and its sine factor
at \(\pm\pi+iv\) is \(O(h)\).

There is also an elementary way to justify the only test-function
replacement in this argument. Put
\(V_h(s)=(1-\eta e^{-iN(s-ih)})^{-1}\). Then
\(W_N(s-ih)=i(N\eta)^{-1}\partial_sV_h(s)\).
At fixed \(N\), \(f(s-ih)-f(s)=O_N(h)\) in \(C^1\) on the interval.
Integration by parts bounds its pairing with \(W_N(s-ih)\) by
\(O_N(h)+O_N(h)\|V_h\|_{L^1}=O_N(h\log(1/h))\), which tends to zero.
The endpoint values of \(V_h\) are bounded because they are
\((1+e^{-Nh})^{-1}\). One may therefore apply the Abel Fourier
formula to the joined \(f\) after taking this controlled difference.
The same proof is locally uniform with every fixed parameter
derivative. Thus (3) is entire in \(n,\chi\). All statements use the
full original angular derivative, including the odd simple node.

## 2. Polynomial local row bounds

Let \(\mathcal H\) be the periodic Hilbert transform with Fourier
multiplier \(-i\,\operatorname{sgn}k\). Since \(f\) is continuous,
its distributional derivative is its bounded piecewise smooth
derivative, with no point mass at the joining point. Consequently
\[
 (P_\pm f)'=\tfrac12(f'\pm i\mathcal H f')
 \tag{7}
\]
at every physical grid point. The mean of \(f'\) is zero.

For a grid point \(\tau_j\), split the principal-value Hilbert
integral at circular distance \(1/N\). This neighborhood does not
meet the joining point. Subtracting \(f'(\tau_j)\) in the near
integral bounds that part by \(CN^{-1}\|f''\|_\infty\).
The absolute integral of the cotangent kernel on the complement
is \(O(\log(2N))\). Hence
\[
 |(P_\pm f)'(\tau_j)|
 \le C\{N^{-1}\|f''\|_\infty+
                          \log(2N)\|f'\|_\infty\}.
 \tag{8}
\]
The norms on the right are one-sided norms on the closed interval;
the possible joining jump of \(f'\) causes no extra term.

Use the Chebyshev basis \(B_r(z)=T_r(-z/2)\), \(0\le r<N\).
For \(p=B_r\), put \(\Lambda=1+|n|+|\chi|\). Direct differentiation
of (2) gives
\[
 \|f'\|_\infty\le CN\Lambda\,\mathcal E_N,\qquad
 \|f''\|_\infty\le CN^2\Lambda^2\,\mathcal E_N,\qquad
 \mathcal E_N=
     e^{\pi N|\Im\chi|+\pi N|\Im n|/4}.
 \tag{9}
\]
The constants are absolute; the real parts of the two parameters
only enter \(\Lambda\). Equations (3) and (8) prove
\[
 |\mathscr T_{\sigma,n,\chi}[B_r]|
       \le CN^2\log(2N)\Lambda^2\mathcal E_N,\qquad
 \|\boldsymbol\ell_{\sigma,n,\chi}^{\,0}\|_2
       \le CN^{5/2}\log(2N)\Lambda^2\mathcal E_N ,
 \tag{10}
\]
where \(\boldsymbol\ell^0\) is the row on this \(N\)-element basis.
In particular its norm is polynomial in \(N\) at fixed real powers
and charges, with no contour-height exponential cost.
These are Chebyshev coefficient norms, not monomial or physical
Hilbert--Schmidt norms.

## 3. Exact coupons by a finite parity sum

The original bilinear Frobenius trace is
\(\phi_N(p)=\eta N^2[z^D]\operatorname{rem}_{P_N}p\).
Its Chebyshev matrix has a particularly simple form. Let
\[
 S=\operatorname{diag}(2,1,\ldots,1),\qquad
 Je_j=e_{D-j},\qquad
 Ue_j=\begin{cases}e_{j-1}&j>0,\\0&j=0.\end{cases}
 \tag{11}
\]
The vectors \(e_j\) in (11) are coordinate vectors only, not Newton
polynomials. Then
\[
 H_B=(\phi_N(B_iB_j))_{0\le i,j<N}
        =\frac{N^2}{4}S J(I-U^2)S .
 \tag{12}
\]
Indeed, among \(0\le k\le2D\), the only nonzero
\(\phi_N(B_k)\) are \(N^2/2\) at \(k=D\), and \(-N^2/2\)
at \(k=D+2\) when that index is in the range. This follows either
from the exact Hermite alias or the top-coefficient formula.
Apply \(B_iB_j=(B_{i+j}+B_{|i-j|})/2\).
The entries with an index zero account exactly for the two factors
of \(S\). This also verifies (12) at \(N=2\).

Since \(U\) is nilpotent,
\[
 H_B^{-1}=\frac4{N^2}
       S^{-1}\left(\sum_{a=0}^{\lfloor D/2\rfloor}U^{2a}\right)
                           J S^{-1},\qquad
 \|H_B^{-1}\|\le\frac{4\lceil N/2\rceil}{N^2}.
 \tag{13}
\]
For the column \(\boldsymbol r=(\mathscr T_{\sigma,n,\chi}[B_j])_j\),
set \(\boldsymbol c=H_B^{-1}\boldsymbol r\) and
\(\mathfrak b_{\sigma,n,\chi}^{\,0}=\sum_jc_jB_j\).
It is the unique original full-algebra coupon satisfying
\[
 \phi_N(\mathfrak b_{\sigma,n,\chi}^{\,0}p)
        =\mathscr T_{\sigma,n,\chi}[p],\qquad
 \|\boldsymbol c\|_2
        \le CN^{3/2}\log(2N)\Lambda^2\mathcal E_N .
 \tag{14}
\]
Thus coupon reconstruction is a known finite parity cumulative sum.
There is no division by a closed source. The positive coefficient
norm in this estimate does not make \(H_B\) a positive pairing.

## 4. The literal source identities

For the fixed graph of the reduced-source direct, keep every retained
edge, including complete-only factors. Let \(I\) be its selected set,
\(m=|I|\), and let
\[
 F_N(\boldsymbol t)=\prod_{\{v,w\}\in E}K_N(t_v,t_w),\quad
 Q_N=\mathcal R_I F_N,\quad
 \mathscr G_{N,\boldsymbol\sigma}(\boldsymbol n,\boldsymbol\chi)
       =\left[\bigotimes_{v\in I}
                    \mathscr T_{\sigma_v,n_v,\chi_v}\right]Q_N .
 \tag{15}
\]
Here \(\mathcal R_I\) is the full Hermite Euclidean remainder in
each selected spectral variable. The outside angles are complete
for all analytic assertions below. Ordinary outside polynomials
are retained in the exact algebraic identities.

The exact sign average, unit readout, and signed heat equation are
\[
 \begin{split}
 2^{-m}\sum_{\boldsymbol\sigma}\mathscr G_{N,\boldsymbol\sigma}
       &=\widetilde Z_N(\boldsymbol n,\boldsymbol\chi),\\
 \mathscr G_{N,\boldsymbol\sigma}(\boldsymbol n,\boldsymbol1)
       &=\widetilde Z_N(\boldsymbol n,\boldsymbol1),\\
 \partial_{n_v}\mathscr G_{N,\boldsymbol\sigma}
       &=-\frac{i}{4\pi N}\partial_{\chi_v}^2
                                      \mathscr G_{N,\boldsymbol\sigma}.
 \end{split}
 \tag{16}
\]
They follow from (4) and the exact finite-height identities. Directly,
\(P_++P_-=I-P_0\), whose constant term vanishes after differentiation;
reflection of the grid turns the remaining sample into the original
cosine derivative trace. At \(\chi=1\), (2) is odd, so its positive
and negative contributions have the same sampled derivative.
The heat equation also follows directly by differentiating (2).

Every crossing carrier
\(C_{N,n}=\exp(\pi inD^2/(4N))\) is restored in the original manner.
In particular, for integral \(n\),
\[
                  \mathfrak b_{\sigma,n,1}^{\,0}
                                      =C_{N,n}^{-1}R_n
                          \quad\hbox{in }\mathcal A_N .
 \tag{17}
\]
No value, first normal, mixed normal, parity or framing phase is
discarded from these identities. The off-endpoint Hardy family is
generally different from a positive-height family; its seed comparison
is proved below. These are local coupons on canonical representatives,
not power-independent charge coupons.

The prescribed signed Gaussian charge readouts are convergent, and
their finite-height identities pass to (4) with uniform domination.
To see the needed bound on the unbounded readout line, fix \(N\),
\(H\), \(p\), and a compact power set. The exact height current (20)
below and the elementary global sine bound give
\[
 \frac{|\sin(N(1-\chi)(\pi\pm ih))|}
                      {4\cosh^2(Nh/2)}
 \le e^{\pi N|\Im\chi|+Nh|1-\Re\chi|-Nh}
 \le e^{N(\pi+H)|\chi|},\qquad 0\le h\le H .
\]
The remaining factors in the current are bounded on this fixed
endpoint interval. Combine its integral from zero to \(h\) with
the Hardy bound (10). There are constants, allowed to depend on
these fixed data, such that
\[
 \sup_{0\le h\le H}|\mathcal T_{\sigma,n,\chi}^h[p]|
       \le C_N(1+|\chi|)^2e^{C_N|\chi|}.
\]
Tensor products give the same form with a fixed larger polynomial
power. On each prescribed signed Gaussian contour the negative
quadratic real exponent dominates this common linear exponential
bound, uniformly as the heights tend to zero. Dominated convergence
therefore preserves the same original unit endpoint after the heat
steps. No arbitrary nonconvergent heat contour is asserted.

## 5. The actual initializer survives the zero-height limit

Fix the real powers \(\boldsymbol b\). Use a sufficiently small
positive seed \(\boldsymbol\xi=\delta\boldsymbol1\) and real heights
\(H_v=O_{\Gamma,\boldsymbol b}(\delta)\) from the full-midpoint
initializer, choosing \(\delta\) still smaller below.
The reduced-source direct proves, for \(E_N=F_N-Q_N\),
\[
 |E_N(\boldsymbol s+i\boldsymbol y)|
   \le CN^A
       \exp\{N(M_0-c)+\sum_v d_vD|y_v|\},\qquad
                     M_0=|E|M_\infty,\quad c>0 .
 \tag{18}
\]
Its real profile for \(F_N\) gives, at either endpoint in coordinate
\(v\), with all other selected angles real,
\[
 |Q_N(\pi\pm ih,\boldsymbol s_{\ne v})|
       \le CN^A e^{N(M_0-c_*+C_\Gamma h)},\qquad
       c_*=\min\{c,\,2\gamma\min_{v\in I}d_v\}>0 ,
       \quad 0\le h\le\max_vH_v,\quad\gamma=1/200 .
 \tag{19}
\]
Here \(Q_N(\pi\pm ih)\) means evaluation at
\(z_v=2\cosh h\). Formula (19) follows by adding the two bounds:
the original endpoint loses \(2\gamma d_v\), and (18) loses \(c\).
The coefficient norm in the other Chebyshev variables obeys the
same bound up to a graph constant, by cosine Parseval. This does
not use a monomial-coordinate norm bound.

We spell out uniformity when some other heights have already
reached zero. With \(k=N(1-\chi)\), \(K=-N^2/(\pi i)\), the exact
height-current direct gives
\[
 J_\sigma^h[p]=-\frac{\sigma\eta K}{4\cosh^2(Nh/2)}
 \{g(\pi-ih)\sin(k(\pi-ih))
                       -g(\pi+ih)\sin(k(\pi+ih))\},
 \quad
 g(t)=\sin t\,p(-2\cos t)e^{inNt^2/(4\pi)} .
 \tag{20}
\]
It extends continuously to zero. For real \(n\), bounded small
\(h\ge0\), and \(0<\Re\chi<1\),
\[
 |J_\sigma^h[p]|
 \le CN^2h\,
      e^{N(|n|h/2+\pi|\Im\chi|)}
                                  |p(2\cosh h)|.
 \tag{21}
\]
Indeed
\(|\sin(k(\pi\pm ih))|/(4\cosh^2(Nh/2))
\le e^{-N\Re\chi h+\pi N|\Im\chi|}\), and
\(|g(\pi\pm ih)|\le C h\,|p(2\cosh h)|e^{N|n|h/2}\).
There is no inverse power of \(h\) in this estimate.

For \(p=B_r\), \(r<N\), its endpoint value is bounded by \(e^{Nh}\).
Integrating (21) from zero to \(h\), and using (10), proves a
uniform row bound throughout the entire height interval:
\[
 \|\boldsymbol\ell_{\sigma,b,\chi}^{\,h}\|_2
 \le CN^{5/2}\log(2N)
      e^{N\{(1+|b|/2)h+\pi|\Im\chi|\}},
                 \qquad 0\le h\le H .
 \tag{22}
\]
The parameters \(b,\chi\) here range over their fixed seed compact.
At \(h=0\), this is precisely the polynomial Hardy bound.

Telescope the coordinates of
\(\bigotimes_v\mathcal T_{\sigma_v,b_v,\chi_v}^{H_v}Q_N\),
changing one height at a time to zero. At the changed vertex,
integrate (20) from zero to \(H_v\). Bound its coefficient vector
in the other variables by (19) and (21). Apply (22) to those other
variables. Already-zero heights cost only polynomial factors;
the remaining positive heights cost \(e^{O_{\Gamma,\boldsymbol b}
(\delta)N}\). Thus every integrand has a bound
\[
 CN^A\exp N\{M_0-c_*+
             C_{\Gamma,\boldsymbol b}\delta+
                                \pi\sum_v|\Im\chi_v|\}.
 \tag{23}
\]
Choose \(\delta\) small, then a fixed complex neighborhood \(U\) of
that seed small. Since the initialized marked action satisfies
\(S(\delta\boldsymbol1)=M_0+O(\delta^2)\), (23) and its integrated
telescoping sum are bounded, with some \(\epsilon_*>0\), by
\[
 \left|
 \mathscr G_{N,\boldsymbol\sigma}(\boldsymbol b,\boldsymbol\chi)
 -\mathcal G_{N,\boldsymbol\sigma}^{\mathrm{red},\boldsymbol H}
                         (\boldsymbol b,\boldsymbol\chi)
 \right|
       \le CN^A e^{N(\Re S(\boldsymbol\chi)-\epsilon_*)},
                              \qquad\boldsymbol\chi\in U .
 \tag{24}
\]
All constants are fixed before the level tends to infinity.
Both parities and \(N=2\) belong to the exact construction;
finitely many initial levels may be absorbed in the estimates.

The known reduced initializer therefore proves the same nonzero
all-order all-plus expansion for \(\mathscr G\), with the same
phase, prefactor and original carriers. The suppressed sign
families retain their seed gap. Every fixed charge derivative
obeys (24) on a smaller neighborhood, by Cauchy's formula.
No open-outside or varying-power initializer is inferred.

## 6. What this simplifies

This construction removes every height choice from the new reduced
family. Its coefficient space has dimension \(N^{|I|}\), its local
row and coupon norms have the polynomial real-parameter bounds
(10) and (14), and its polarized Fourier projections are genuinely
orthogonal on the ordinary angular \(L^2\) space.

The source is still read by the original derivative-grid functional.
Neither that functional nor the bilinear Frobenius trace becomes a
positive norm. The actual reduced numerator can have large coherent
Chebyshev channels whose observations cancel. No absolute-channel
majorant or Rivin-relative upper estimate is proved by this note.
In particular (24) is a proved initializer comparison, not a
continuation theorem to unit charge. There is no new knot class,
volume lower bound or finite-exception theorem.

## Complete direct sources

- [Hermite-reduced initializer](research_hermite_reduced_polarized_initializer.md),
  439 lines, SHA256
  a77d3e81cb14400cc8027055f45479b977717da7cf80dbaeb9fcecf2379dc04b:
  the canonical numerator, full Hermite aliases, high-frequency
  error, exact source identities, Chebyshev metric and initializer.
- [Full-midpoint source](research_full_midpoint_polarized_initializer.md),
  603 lines, SHA256
  65a91ee6538b05355bab5056d32b2fe563c47eeff1e1924b1be259ef5cd628ad:
  the literal full-period operators, original source, real profile,
  sufficiently small seed and signed heat-readout scope.
- [Exact height current](research_polarized_height_current_transport.md),
  290 lines, SHA256
  63273441891ce682acf46495e2707a8a72c28d2b74b3d4bed2d6861d568014fb:
  the entire endpoint-current identity with its original normalization.

The entire proof and all three complete direct sources were read at
these matching versions before author freeze. Root's whole-draft
mathematical review is complete; matching entire-final reviews are
separate. Only written mathematics, text reads, hashes and this
new-file patch are used. No mathematical programs, numerical
experiments, tests, builds or git commands are run. No earlier final
or public manuscript is edited.
