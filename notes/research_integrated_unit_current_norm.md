# The exact norm rate of the integrated unit endpoint current

Private written proof, 16 November 2026.

The original full-period vertical current has a sharp norm cost at a
fixed positive height. A fixed product of actual microscopic endpoint
kernels attains that cost, although its ordinary real-interval norm is
polynomial. This is an estimate of the integrated current itself; it
does not estimate the sum of the horizontal and vertical currents by
their separate absolute values.

A second calculation keeps the height microscopic. The extreme
coefficients of its literal charge convolution remain polynomially
large after integration. That statement concerns this specified Fourier
representation. The available normal-aware half-band folding remains
allowed, with its normal functional retained.

## 1. The original operator and the norm being estimated

Put
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 P_N(C)=2T_N(C/2)+2,
\]
\[
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),\qquad
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),\qquad
 K_N(w,C)=\sum_{k=0}^{D}e_k(w)e_k(C).
 \tag{1}
\]
The original full trace is
\[
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
       \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
                   +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{2}
\]
For \(n=0\) the unit-charge vertical current is identically zero.
Fix henceforth an integer \(n\ne0\) and a height \(H>0\), independently of \(N\).
Keep the original unit scalars
\[
 C_{N,n}=e^{\pi i nD^2/(4N)},\qquad
 \Omega_{N,n}=C_{N,n}e^{inN\pi/4}.
 \tag{3}
\]
Here \(R^n\) is the original physical crossing class, whose values
and first normals are those of
\(C_{N,n}\exp(inNt^2/(4\pi))\) at \(C=-2\cos t\).
The exact unit-charge vertical current is the ordinary-polynomial
functional
\[
 V_{n,1}^{H}[f]=\int_0^H\rho_{N,n}(y)f(2\cosh y)\,dy,
\]
\[
 \rho_{N,n}(y)=
 \frac{2i\eta N^2\Omega_{N,n}}{\pi}
 \frac{\sinh y\,\sinh(nNy/2)}
      {4\cosh^2(Ny/2)}
                 e^{-inNy^2/(4\pi)}.
 \tag{4}
\]
This is the paired vertical side of the original full trace rectangle.
In particular
\(\phi_N(R^nf)=H_{n,1}^{H}[f]+V_{n,1}^{H}[f]\), with the original
horizontal functional, for every ordinary polynomial \(f\).
Its derivation includes every first normal in (2), both parities,
and the simple odd node. Equation (4) is not a replacement of that
trace by value sampling.

For an integer \(r\ge1\), let
\[
 \mathcal P_{r,N}=\{f:\deg f\le rD\},\qquad
 \|f\|_{\mathbb R}=\sup_{C\in[-2,2]}|f(C)|,\qquad
 \kappa_{r,n}=r-1+|n|/2>0.
 \tag{5}
\]
Use the ordinary polynomial in this definition. If \(r>1\), reducing
it modulo \(P_N\) before applying (4) generally changes the current.
Such reduction preserves the closed trace, but moves an additional
holomorphic contribution between its horizontal and vertical parts.
No reduction is made here.

**Theorem 1.** The exact operator norm satisfies
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac1N
       \log\|V_{n,1}^{H}:\mathcal P_{r,N}\to\mathbb C\|
                         =\kappa_{r,n}H .
 \quad}
 \tag{6}
\]
The limit holds through both level parities. The upper estimate is
valid for polynomials with coefficients in any fixed normed space,
using the corresponding real-interval supremum norm.

For \(r=1\), this is also the exponential norm rate on the canonical
full physical value-and-normal space, under any norm polynomially
equivalent to its ordinary real norm. This includes the usual
normalized full angular-jet or spectral-jet norms. For \(r>1\), a
physical-jet seminorm cannot replace (5): it loses ordinary multiples
of \(P_N\), which the separate current need not annihilate.

## 2. Universal upper bound

Expand an ordinary degree-\(d\) polynomial in Chebyshev polynomials:
\[
 f(C)=\sum_{k=0}^{d}a_kT_k(C/2),\qquad
 \sum_k|a_k|\le(2d+1)\|f\|_{\mathbb R}.
 \tag{7}
\]
The same inequality holds for normed-space coefficients by their
cosine integral formulas and the triangle inequality. Therefore
\[
 |f(2\cosh y)|\le(2d+1)\|f\|_{\mathbb R}e^{dy}.
 \tag{8}
\]
The exact denominator in (4), and
\(|\sinh(nNy/2)|\le e^{|n|Ny/2}/2\), give
\[
 |\rho_{N,n}(y)|
 \le C_HN^2e^{N(|n|/2-1)y}\qquad(0\le y\le H).
 \tag{9}
\]
For \(d\le rD\), multiplication of (8) and (9) yields
\[
 |V_{n,1}^{H}[f]|
       \le C_{r,n,H}N^3e^{N\kappa_{r,n}H}\|f\|_{\mathbb R}.
 \tag{10}
\]
This retains the entire integration interval and all Fourier aliases
of its double-pole denominator. It proves the upper half of (6).

For completeness, polynomial equivalence with canonical physical jets
does not require discarding a normal. The angular polynomial
\(f(-2\cos t)\), of degree below \(N\), has frequencies
\(-D,\ldots,D\). At the \(N\) physical angles, the discrete Fourier
transform of its values and \(N^{-1}\) times its angular derivatives
separates each pair of frequencies \(k,k-N\). The resulting two by
two matrix has determinant of modulus one after this scaling.
Each Fourier coefficient is consequently bounded by a constant times
the maximum normalized angular jet, and summing at most \(2N-1\)
coefficients bounds \(\|f\|_{\mathbb R}\) polynomially.
The converse follows from (7), or the ordinary Markov inequality.
At double spectral roots, angular and spectral first derivatives
differ by \(2\sin t\); its reciprocal costs at most a power of \(N\).
At the odd simple root the angular derivative is automatically zero,
and only its value is required. Thus this argument uses exactly the
original full physical data.

## 3. Actual microscopic products attain the rate

Fix \(A<\infty\) and first let all \(\alpha_i\) be real with
\(|\alpha_i|\le A\). Set
\[
 w_i=2\cosh(\alpha_i/N),\qquad
 B_N(C)=\prod_{i=1}^rK_N(w_i,C),
\]
\[
 a(\alpha)=\frac{\cosh^2(\alpha/2)}{\pi^2+\alpha^2},\qquad
 b_r(y,\boldsymbol\alpha)
       =\sinh y\prod_{i=1}^r
                     \frac{a(\alpha_i)}{\sinh^2(y/2)},
\]
\[
 \Psi_{r,n}(y)=\kappa_{r,n}y-\frac{in}{4\pi}y^2.
 \tag{11}
\]
The function \(a\) is entire after removing its singularities at
\(\alpha=\pm i\pi\), and is positive and uniformly bounded away
from zero on every bounded real interval.

**Theorem 2.** The actual integrated source has the uniform relative
asymptotic
\[
 \boxed{\quad
 V_{n,1}^{H}[B_N]
 =\frac{i\eta\,\operatorname{sgn}(n)\Omega_{N,n}}{\pi}
  N^{\,1-2r}
  \frac{b_r(H,\boldsymbol\alpha)}
       {\kappa_{r,n}-inH/(2\pi)}
  e^{N\Psi_{r,n}(H)}
                 \{1+O_{r,n,H,A}(N^{-1})\}.
 \quad}
 \tag{12}
\]
It holds uniformly for level-dependent real marks in the stated
compact set. In particular the leading coefficient is nonzero.
All original signed and parity-dependent scalars are displayed.

There is also an absolute form on bounded complex parameter sets:
replace the braces in (12) by putting an \(O(N^{-1})\) error
additively after the fraction involving \(b_r\). That form and all
fixed parameter derivatives hold on buffered parameter sets.
Original spectral derivatives in the microscopic colors have the
corresponding polynomial losses. No nonzero derivative coefficient
is asserted.

**Proof.** Reserve a fixed interval \(y\in[H/2,H]\). The actual
canonical off-real source theorem, with
\[
 x=-\frac1{2N}+\frac{iy}{2\pi},\qquad
 C_N(x)=2\cosh y,
\]
gives
\[
 K_N(w_i,2\cosh y)
 =\frac{P_N(2\cosh y)}{N^2}
       \left\{\frac{a(\alpha_i)}{\sinh^2(y/2)}
                                     +O(N^{-1})\right\}.
 \tag{13}
\]
The error and every fixed \(y\)- or parameter derivative are uniform
on a slightly larger interval and parameter set. The centered leading
term follows from its stated uncentered \(-a(\alpha_i)\csc^2(\pi x)\)
by an \(O(N^{-1})\) change. The exact identity is
\[
                 P_N(2\cosh y)=4\cosh^2(Ny/2).
 \tag{14}
\]
Thus (13) concerns the original canonical kernel, including its high
Newton terms. It is not a moderate representative substituted into
the off-grid integral.

Insert (13) into (4). One factor (14) cancels its entire denominator
exactly. On the reserved interval the remaining factors satisfy
\[
 P_N(2\cosh y)^{r-1}
       =e^{N(r-1)y}\{1+O(e^{-Ny})\},
\]
\[
 \sinh(nNy/2)=\tfrac12\operatorname{sgn}(n)
        e^{N|n|y/2}\{1+O(e^{-N|n|y})\}.
 \tag{15}
\]
Consequently the integrand is
\[
 \frac{i\eta\,\operatorname{sgn}(n)\Omega_{N,n}}{\pi}
 N^{2-2r}e^{N\Psi_{r,n}(y)}
            \{b_r(y,\boldsymbol\alpha)+O(N^{-1})\}.
 \tag{16}
\]
The error has bounded fixed derivatives after multiplication by \(N\).
On real parameter compacts \(b_r\) is a uniform positive unit.

There is no endpoint stationary point:
\[
 \Psi_{r,n}'(y)=\kappa_{r,n}-iny/(2\pi),\qquad
 |\Psi_{r,n}'(y)|\ge\kappa_{r,n}>0,\qquad
 \Re\Psi_{r,n}'=\kappa_{r,n}.
 \tag{17}
\]
Integrating once by parts, and bounding the remaining integral by
\(\int_{H/2}^He^{N\kappa_{r,n}y}dy\), proves
\[
 \int_{H/2}^He^{N\Psi_{r,n}(y)}
       \{b_r(y)+O(N^{-1})\}\,dy
 =\frac{e^{N\Psi_{r,n}(H)}}{N}
       \left\{\frac{b_r(H)}{\Psi_{r,n}'(H)}
                                      +O(N^{-1})\right\}.
 \tag{18}
\]
The lower endpoint has a fixed exponential gap. This proves a
uniform endpoint Laplace expansion with the signed complex phase,
not just a comparison of absolute integrands.

It remains to control \(0\le y\le H/2\), where (13) is not uniform.
The full endpoint-product theorem gives
\[
              \|B_N\|_{\mathbb R}\le CN^p,\qquad
              \deg B_N\le rD,
 \tag{19}
\]
uniformly for bounded complex microscopic parameters. The proof of
(10), applied to this shorter interval, bounds its current by
\(CN^{p+3}e^{N\kappa_{r,n}H/2}\). This is exponentially smaller
than (18), including its polynomial scale. Equations (16)--(19)
prove (12) and its absolute complex-parameter version.

Holomorphic parameter derivatives follow on larger compacts by
Cauchy's formula. Each factor is even in its microscopic parameter.
In the coordinate \(\beta_i=\alpha_i^2\), the change
\(w_i=2+\beta_i/N^2+O(\beta_i^2/N^4)\) is locally uniformly invertible
on bounded \(\beta_i\) sets for large \(N\). Thus each fixed original
\(w_i\)-derivative costs at most a further \(N^2\) per derivative on
buffered sets. The original full-jet equations are retained; no
independent normal is replaced by a sampled value. \(\square\)

Since \(B_N(c_0)=1\), (19) gives \(1\le\|B_N\|_{\mathbb R}\le CN^p\).
Dividing (12) by this norm proves the lower half of (6).
This saturation holds for every fixed \(r\), not for a specially
chosen sequence of arbitrary polynomial coefficients.

## 4. A microscopic integrated Fourier coefficient

The fixed-height theorem cannot be specialized to a height tending
to zero. A separate exact calculation is useful at \(H=A_0/N\),
where \(A_0>0\) is fixed. For one cut incidence define the actual
integrated coupon
\[
 Q_{N,n}^{A_0}(Z)=
       \int_0^{A_0/N}\rho_{N,n}(y)K_N(2\cosh y,Z)\,dy.
 \tag{20}
\]
It is an ordinary polynomial of degree at most \(D\). For any
surviving original trace, integration commutes with that trace and
with its free-variable derivatives. Write its ordinary expansion as
\[
 Q_{N,n}^{A_0}(Z)=\sum_{k=0}^{D}\bar\beta_{N,k}T_k(-Z/2).
 \tag{21}
\]
The exact cosine product rule in the full physical algebra gives
the two charge shifts \(\chi\mapsto\chi\pm k/N\), each with
coefficient \(\bar\beta_{N,k}/2\), inside the surviving trace.
All normal product rules, other edge factors and shared variables
stay inside that trace.

The top Newton identity and the two leading coefficients give
\[
 e_D(w)=\frac{\eta P_N(w)}{N^2(w-c_0)},\qquad
 \beta_D(w)=\frac{2e_D(w)}{N^2}
 \quad\hbox{for }K_N(w,Z)=\sum_k\beta_k(w)T_k(-Z/2).
 \tag{22}
\]
The quotient in (22) is its ordinary removable polynomial.
Substitute (22) in (20), use (14), and put \(\alpha=Ny\).
Each extreme charge coefficient is exactly
\[
 a_{N,n}^{A_0}:=\frac{\bar\beta_{N,D}}2
 =\frac{2i\Omega_{N,n}}{\pi N^3}
  \int_0^{A_0}
  \frac{\sinh(\alpha/N)\sinh(n\alpha/2)}
       {2\cosh(\alpha/N)-c_0}
                     e^{-in\alpha^2/(4\pi N)}\,d\alpha .
 \tag{23}
\]
In particular no height-zero endpoint of measure zero was used.
The full vertical density was integrated before taking the estimate.

Uniform Taylor expansion on this fixed interval gives
\[
 \boxed{\quad
 a_{N,n}^{A_0}
 =\frac{2i\Omega_{N,n}}{\pi N^2}
       \left\{\int_0^{A_0}
          \frac{\alpha\sinh(n\alpha/2)}{\alpha^2+\pi^2}\,d\alpha
                       +O(N^{-1})\right\}.
 \quad}
 \tag{24}
\]
The integral is real, has the sign of \(n\), and is nonzero.
Thus both extreme coefficients are of order \(N^{-2}\) after
the original carrier is retained. At surviving unit charge their
locations are \(1/N\) and \(2-1/N\).

This is a nonvanishing statement for the literal convolution (21).
It does not assert dominance of either term in its coherent closing.
Nor does it prohibit the archived half-band folding: that operation
moves high frequencies to lower ones together with an explicit
normal functional. Dropping that functional would change the
source. Formula (24) alone supplies no intrinsic localization
obstruction after every allowed full-normal change of representation.

## 5. Consequences and limitations

The compensating horizontal current can be identified explicitly.
On every double physical node the original crossing has unit-modulus
value. Its angular derivative is \(O_n(N)\); division by
\(2\sin t\), whose nonzero physical minimum is bounded below by
\(c/N\), gives a polynomial spectral-normal bound. Markov's
inequality for \(f\in\mathcal P_{r,N}\) and the \(O(N)\) terms
of (2) therefore give
\[
 |L_{n,1}[f]|=|\phi_N(R^nf)|
                  \le C_{r,n}N^3\|f\|_{\mathbb R}.
 \tag{25}
\]
At the odd simple node only the unit-modulus crossing value is used.
The full product rule retains both derivatives at every double node.

Since \(H_{n,1}^{H}=L_{n,1}-V_{n,1}^{H}\), equations (6),(25)
also prove
\[
 \lim_{N\to\infty}N^{-1}\log
       \|H_{n,1}^{H}:\mathcal P_{r,N}\to\mathbb C\|
                           =\kappa_{r,n}H.
 \tag{26}
\]
The upper bound is immediate, and the actual product \(B_N\) proves
the lower bound: by (12),(19),(25),
\[
 H_{n,1}^{H}[B_N]=-V_{n,1}^{H}[B_N]+O(N^p),\qquad
 \frac{H_{n,1}^{H}[B_N]}{V_{n,1}^{H}[B_N]}
                    =-1+O(N^{p'}e^{-N\kappa_{r,n}H}).
 \tag{27}
\]
Thus the displayed exponential leading term is canceled by the
original horizontal current. This is an actual coherent cancellation
for all the microscopic products in Theorem 2, not merely the
possibility of cancellation between two upper estimates.

At fixed positive height the optimal exponential cost in an ordinary
real-norm estimate is already positive for a single canonical
microscopic kernel. A proposed estimate of \(V_{n,1}^H\) below (6)
therefore needs additional source-specific cancellation or a different
height/phase budget; polynomial physical bounds alone do not provide
it. The current-free finite adjoint identities remain exact, but do
not remove this cost from the separately integrated current.

No analogous lower bound for the whole original closed trace follows.
Both parts must remain when the representation is changed. Likewise (24)
does not control the surviving charged descendant sources in the
finite convolution. An estimate closed under arbitrary fixed short
components still requires their actual coherent observation or
retained-boundary action bounds.

The full-period current note already supplies the exact shared
convolution and its supremum-based upper estimate. Its nonlocal
coefficient example was at height zero. The present additions are
the sharp norm rate for the integrated fixed-height operator, its
saturation by actual microscopic products, and the explicit integrated
microscopic extreme coefficient. No source or public manuscript was
modified to obtain them.

## 6. Complete direct sources

All three complete direct sources were read at the following pins;
the actual density, canonical off-real source, normal and polynomial
norm implications were checked:

* [Full-period current and charge convolution](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595.
* [Actual canonical source on nonreal bands](research_unturned_endpoint_forced_off_real_asymptotic.md),
  SHA256 022c86dc122a647cb09cd2233292094501cf25719f87d928d019f03423f09f33.
* [Full microscopic product and normal bounds](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Adopted notes and public manuscripts are unchanged.
