# Phase-weighted leaf representatives and the exact window interface

Private written proof, 16 November 2026.

The actual filled-leaf row profile supplies exact holomorphic
representatives with its calibrated phase upper bound on either
half-plane separately. They preserve both physical jets on a fixed
bulk window. Joining them in the original trace retains an explicit
holomorphic real interface and both outer vertical sides.

This is a source-preserving replacement inside that trace window,
not a bound for the canonical polynomial at a free complex color.
On the positive regular leaf chart its weight is the retained-boundary
Legendre profile, with the signed imaginary coordinate retained.
No estimate of the entire joined current at the parent action follows.

## 1. Actual data and a fixed phase

Fix an integer \(n\), a nonnegative integer \(r\), and bounded complex
microscopic parameters \(|\alpha_i|\le A\). Use the original source
\[
 B_N=\operatorname{can}\prod_{i=1}^rK_N(2\cosh(\alpha_i/N),Z),
 \qquad F_N=T(R^nB_N),\qquad \eta=(-1)^{N-1}.
 \tag{1}
\]
Here \(N\ge2\), \(P_N(Z)=2T_N(Z/2)+2\), \(T_N\) is the
Chebyshev polynomial, and \(\operatorname{can}\) is the full
remainder of degree at most \(N-1\). The letter \(T\) in (1)
denotes the original tangle turn.
All carriers, shared colors, and first normals in (1) are unchanged.
Choose fixed intervals
\[
 I=[a,b]\Subset I_0\Subset(0,1/2),\qquad
 c_N(z)=2\cos\nu_N(z),\quad \nu_N(z)=2\pi z+\pi/N.
 \tag{2}
\]
Write \(u_j=j/N\), \(v_j=F_N(c_N(u_j))\), and
\[
 d_j=\left.\partial_z F_N(c_N(z))\right|_{z=u_j}.
 \tag{3}
\]
Every node in this window is double, at both parities for large \(N\).
The odd simple endpoint is outside it and is not altered.

For \(|n|=m\ge2\), let \(S_n(t)\) be exactly the signed terminal
phase of the action-calibration source. For positive \(n\),
\[
 S_m(t)=\psi(t_m(t),t)+\frac{im}{4\pi}t_m(t)^2-it_m(t);
 \qquad S_{-m}(t)=\overline{S_m(\bar t)}.
 \tag{4}
\]
The specified primitive and constant, in particular
\(S_m(\pi)=-i\pi/m\), are retained. Its simple selected branch
extends holomorphically to a fixed neighborhood of the compact
real angle interval corresponding to \(I_0\). Choose a sufficiently
small fixed rectangle in that neighborhood, and put
\[
 \mathcal S_N(z)=S_n(\pi-2\pi z-\pi/N).
 \tag{5}
\]
For \(n=0,\pm1\), instead put \(\mathcal S_N=0\). This latter choice
only records their subexponential source bound, not a positive
stationary leaf phase.

Write \(\mathcal J_n(u)=\int_0^u L_n(v)\,dv\), where \(L_n\)
is the maximal logarithmic modulus of the terminal physical
shift roots in the row-profile theorem, and
\(\mathcal I_n=\mathcal J_n(1/2)\). For \(n=0,\pm1\) these
functions are zero.
The physical-row theorem and the exact partial-action identity give
\[
 |v_j|+|d_j|\le
       \exp\{N\mathcal J_n(u_j)+o(N)\},\qquad
 \Re\mathcal S_N(u_j)=\mathcal J_n(u_j+1/(2N))
 \tag{6}
\]
for \(|n|\ge2\), uniformly over the stated grid and parameter sets.
For \(n=0,\pm1\) both quantities in the first display have
subexponential bounds. Since \(\mathcal J_n\) is smooth on the
buffered bulk interval, the half-row displacement in (6) costs
only a bounded factor. Define the exact normalized jets
\[
 a_j=e^{-N\mathcal S_N(u_j)}v_j,\qquad
 b_j=e^{-N\mathcal S_N(u_j)}
           [d_j-N\mathcal S_N'(u_j)v_j].
 \tag{7}
\]
On a larger fixed microscopic parameter set there is a sequence
\[
 M_N:=1+\max_{j:\,u_j\in I}\sup_{\boldsymbol\alpha}
                   (|a_j|+|b_j|/N),\qquad
                         \frac{\log M_N}{N}\longrightarrow0 .
 \tag{8}
\]
Enlarging the parameter set permits all fixed exterior derivatives.
No normal has been recovered by differentiating a value estimate:
the actual normal bound in (6) is used separately.

## 2. Exact one-sided Hermite interpolation with that weight

For \(\sigma=\pm1\), define
\[
 L_{j,N}^{\sigma}(z)
   =e^{\sigma2\pi iN(z-u_j)}\operatorname{sinc}^2(Nz-j),
 \qquad \operatorname{sinc}w=\frac{\sin\pi w}{\pi w},
 \tag{9}
\]
and, summing only over \(u_j\in I\), set
\[
 \boxed{\quad
 H_N^\sigma(z)=e^{N\mathcal S_N(z)}
  \sum_j\{a_j+[b_j-\sigma2\pi iN a_j](z-u_j)\}
                                      L_{j,N}^{\sigma}(z).
 \quad}
 \tag{10}
\]
The kernels are entire; (10) is holomorphic wherever the fixed
phase is. At grid points their values and derivatives are
\[
 L_{j,N}^{\sigma}(u_k)=\mathbf1_{j=k},\qquad
 (L_{j,N}^{\sigma})'(u_k)
                   =\sigma2\pi iN\,\mathbf1_{j=k}.
 \tag{11}
\]
Thus the linear correction in (10) proves the exact full-jet identities
\[
 H_N^\sigma(u_j)=v_j,\qquad (H_N^\sigma)'(u_j)=d_j.
 \tag{12}
\]
Since \(c_N'\) is a unit on a fixed bulk neighborhood, these are
exactly the value and first spectral normal on this chart.

**Theorem 1.** On every fixed bounded subdomain of the phase
rectangle with \(\sigma\Im z\ge0\),
\[
 |H_N^\sigma(z)|\le C N^2 M_N
                                  e^{N\Re\mathcal S_N(z)}.
 \tag{13}
\]
Every fixed derivative of the representative in \(z\), or in its
exterior parameters, has the same exponential bound with an
additional fixed polynomial factor. These derivative statements
concern (10); they do not estimate higher off-grid derivatives of
the original canonical polynomial.

*Proof.* The integral formula
\(\operatorname{sinc}w=\int_{-1/2}^{1/2}e^{2\pi iws}\,ds\)
shows that \(L^+_{j,N}\) is a Fourier integral with frequencies
in \([0,2N]\), and \(L^-_{j,N}\) has frequencies in \([-2N,0]\).
The coefficient measure is the translate of the nonnegative
triangular convolution measure and has total mass one. Consequently
\[
 |L_{j,N}^{\sigma}(z)|\le1,\qquad
 |(\partial_z^k L_{j,N}^{\sigma})(z)|\le(4\pi N)^k
                                  \quad(\sigma\Im z\ge0).
 \tag{14}
\]
There are \(O(N)\) nodes, \(|z-u_j|\) is bounded, and the
coefficient in braces in (10) is \(O(NM_N)\). This proves (13),
including its boundary \(\Im z=0\).
Differentiate the finite sum and \(e^{N\mathcal S_N}\) for the
stated index derivatives. Cauchy's formula on larger microscopic
parameter sets proves the exterior assertion. The same even
\(\alpha_i^2\) coordinate used by the row theorem converts fixed
derivatives in \(w_i=2\cosh(\alpha_i/N)\) into polynomial costs.
All constructions are linear in the normalized jets and holomorphic
in the original exterior parameters. \(\square\)

The two representatives are not identified off the grid. Their
opposite half-plane bounds are not combined into a bound on a
full strip. In particular no scalar value/normal compatibility
statement beyond the exact interpolation (12) is assumed.

## 3. The original window trace and its oriented interface

Let \(j_0=\lceil Na\rceil\), \(j_1=\lfloor Nb\rfloor\), and use the
midpoint boundaries
\[
 a_N=(j_0-\tfrac12)/N,\qquad b_N=(j_1+\tfrac12)/N.
 \tag{15}
\]
Fix positive heights \(h_-,h_+\) sufficiently small that the
closed rectangle with these real endpoints and imaginary endpoints
\(-h_-,h_+\) is in the phase domain, for all sufficiently large \(N\).
Let \(E_-\) run from \(a_N\) down the left side, across the lower
horizontal, and up to \(b_N\). Let \(E_+\) run from \(b_N\) up
the right side, across the upper horizontal, and down to \(a_N\).
These are the original counterclockwise exterior half-boundaries;
every outer vertical half-side is included.

Let \(p_N(Z;\mathbf y)\) be the entire actual ordinary spectator,
possibly with other trace variables and free boundary parameters
still uncontracted. It may include the original crossing at the
receiving vertex. Put
\[
 f_N(z;\mathbf y)=p_N(c_N(z);\mathbf y),\qquad
 g_\sigma(z)=\sin\nu_N(z)\,H_N^\sigma(z)f_N(z;\mathbf y),
 \qquad D_N(z)=(\pi N)^2\csc^2(\pi Nz).
 \tag{16}
\]
The selected physical-row contribution to the original trace is
\[
 \begin{split}
 \phi_{N,I}(F_Np_N)
  =\eta\sum_{j=j_0}^{j_1}
     \{(4-c_j^2)[F_N'p_N+F_Np_N'](c_j)
                               -c_j(F_Np_N)(c_j)\}.
 \end{split}
 \tag{17}
\]
All products and their normals in this formula are ordinary products
before evaluation.

**Theorem 2.** With the above orientations, exactly
\[
 \boxed{\begin{split}
 \phi_{N,I}(F_Np_N)=-\frac{\eta}{2\pi^2i}
 \left\{\int_{E_-}D_Ng_-\,dz+\int_{E_+}D_Ng_+\,dz
       +\int_{a_N}^{b_N}D_N(g_+-g_-)\,dz\right\}.
 \end{split}}
 \tag{18}
\]
The last integrand is holomorphic at every grid point in the
window. This identity holds coefficientwise in all retained
variables and after their ordinary fixed derivatives.

*Proof.* Since \(c_N'=-4\pi\sin\nu_N\), each summand in (17) is
\[
 -\frac{\eta}{\pi}
        \left.\partial_z[
          \sin\nu_N(z)F_N(c_N(z))f_N(z)]\right|_{z=u_j}.
 \tag{19}
\]
The double-pole expansion of \(D_N\) at \(u_j\) is
\((z-u_j)^{-2}+O(1)\), with no simple-pole term. Equations
(12),(19) therefore give
\[
 \phi_{N,I}(F_Np_N)
            =-\frac{\eta}{2\pi^2i}\oint D_Ng_-\,dz
            =-\frac{\eta}{2\pi^2i}\oint D_Ng_+\,dz.
 \tag{20}
\]
The difference \(g_+-g_-\) vanishes to order two at each
enclosed grid point. Thus \(D_N(g_+-g_-)\) is holomorphic
on the rectangle. The upper half-rectangle has real boundary
oriented from \(a_N\) to \(b_N\). Applying Cauchy's theorem
there to \(D_N(g_--g_+)\) replaces the upper part of the
first integral in (20) by the upper part in (18) and the
displayed positive interface. This proves (18). \(\square\)

Here is a completely explicit form of that interface. With
\(d=z-u_j\), cancellation of the double-pole denominator gives
\[
 \begin{split}
 D_N(z)(H_N^+(z)-H_N^-(z))
 =2i e^{N\mathcal S_N(z)}\sum_j
 \frac{(a_j+b_jd)\sin(2\pi Nd)
                       -2\pi Na_jd\cos(2\pi Nd)}{d^2}.
 \end{split}
 \tag{21}
\]
The \(j\)-summand has removable value \(2\pi N b_j\) before
the factor \(2i e^{N\mathcal S_N}\) at \(d=0\).
For real \(d\),
\[
 \left|\frac{\sin(2\pi Nd)-2\pi Nd\cos(2\pi Nd)}{d^2}\right|
       \le C N^2,\qquad
 \left|\frac{\sin(2\pi Nd)}d\right|\le2\pi N.
 \tag{22}
\]
For the first estimate use Taylor's formula for \(|Nd|\le1\),
and the elementary bound \(1+2\pi N|d|\) otherwise.
Consequently the real interface obeys
\[
 |D_N(g_+-g_-)(x)|
   \le C N^3 M_N e^{N\Re\mathcal S_N(x)}
                              |\sin\nu_N(x)f_N(x)|.
 \tag{23}
\]
Its exponent is the actual row profile, with no independent
absolute normalization of the original leaf.

On midpoint verticals,
\[
 |D_N(a_N+iy)|=|D_N(b_N+iy)|
                 =(\pi N)^2\operatorname{sech}^2(\pi Ny).
 \tag{24}
\]
On each fixed nonzero horizontal height it is at most
\(C N^2e^{-2\pi N|y|}\); (24) gives the same bound on the
entire verticals with an absolute constant. Thus (13),(18),(23)
give the unconditional estimate
\[
 \begin{split}
 |\phi_{N,I}(F_Np_N)|\le C N^4M_N\bigg\{
 &\int_{E_-\cup E_+}
 e^{N[\Re\mathcal S_N(z)-2\pi|\Im z|]}
                  |\sin\nu_N(z)f_N(z)|\,|dz|\\
 &+\int_{a_N}^{b_N}e^{N\Re\mathcal S_N(x)}
                  |\sin\nu_N(x)f_N(x)|\,dx\bigg\}.
 \end{split}
 \tag{25}
\]
The spectator in this estimate is the actual retained source.
No action bound for it is assumed or proved here.

The full sampling kernel has not been replaced by its first Fourier
term. On \(\sigma\Im z>0\),
\[
 D_N(z)=-4\pi^2N^2
                   \sum_{\ell\ge1}\ell e^{\sigma2\pi i\ell Nz}.
 \tag{26}
\]
If \(t=\pi-2\pi z-\pi/N\), then
\[
 D_N(z)=-4\pi^2\eta N^2
             \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{27}
\]
In particular the usual \(\ell\eta^{\ell-1}\) angular aliases
are all present, as are the finite crossing carrier and every
normal inside \(p_N\).

## 4. Signed geometric interpretation and the remaining current

The row coordinate reverses the imaginary direction:
\[
 t=\pi-2\pi z-\pi/N=s+i h_w,\qquad h_w=-2\pi\Im z.
 \tag{28}
\]
Thus the upper representative \(H_N^+\), not the lower one,
is used at a lower angular boundary \(t=s-ih\), \(h>0\).
The exterior sampling debit in (25) is exactly \(-|h_w|\).

Retain the leaf profile \(\mathfrak e_n(s,G;\boldsymbol\beta)\)
with its original cut incidences from the retained-boundary theorem.
Here \(M_\infty=4G_{\rm Cat}/\pi\) is the original complete-edge
constant. This geometric identification concerns \(|n|\ge2\).
Consider a compact part of the calibrated positive stationary branch
where the leaf minimizer and the \(G\)-minimizer are interior and all
cut inequalities are inactive. On that locus, and only with that
branch identification, its full work identity says
\[
 \mathfrak e_n=\pi(M_\infty-\Re S_n(t))+h_wG,\qquad
                             \partial_G\mathfrak e_n=h_w.
 \tag{29}
\]
Convexity makes this interior stationary point the global minimum
over the same closed \(G\)-capacity fiber. Hence
\[
 \boxed{\quad
 \Re S_n(s+i h_w)
   =M_\infty-\frac1\pi
       \min_G\{\mathfrak e_n(s,G;\boldsymbol\beta)-h_wG\}.
 \quad}
 \tag{30}
\]
In particular for a lower angular height \(h\ge0\) the minimized
expression is \(\mathfrak e_n+hG\), not \(\mathfrak e_n-hG\).
The absolute exterior exponent supplied by (25) is (30) minus
\(|h_w|\). It retains the incidence work before any neighboring
row is imposed. The constants are those of (4),(29); no phase
constant or crossing carrier has been adjusted to fit the bound.

Thus there is an actual full-normal source representative with
the desired convex-profile envelope on either such half-domain.
The real interface in (18),(21) lies at \(h_w=0\). It is not
removed, moved to the parent's positive height, or bounded by
the parent's boundary gap. The outer vertical sides also remain.
At active constraints, empty fibers, or a continuation outside
the calibrated positive branch, (30) is not asserted; the
analytic representative and its phase bound still have their
stated purely source-theoretic meaning.

For several shared leaf messages use their representatives together
before tracing the receiving vertex. Products of matching first
jets give the original product rule. The two joint half-plane
representatives carry the sum of their fixed phases; their joint
difference again has double grid zeros, so the proof of (18)
applies without separating a shared color. Telescoping the difference
of the two products and using (13),(23) gives the analogous
polynomial-times-\(e^{N\Re\sum\mathcal S_N+o(N)}\) real-interface
bound for any fixed number of such messages. Distinct traced
variables can be treated coefficientwise in any order. All real
interfaces, vertical sides, their intersections, and the remaining
physical rows must still be retained. No reduction or replacement
is made at an ordinary free boundary variable.

## 5. Coverage and direct-source readbacks

The earlier two-half-plane theorem used unweighted finite Fourier
projection of microscopic endpoint products. The added statement
here uses the actual filled-leaf row action to construct weighted
finite-window representatives and estimates their explicit joined
current. It does not assert that physical samples alone control
the canonical polynomial between nodes.

Indeed at odd levels the exact canonical simple-node cardinal is
\[
 E_N(Z)=\frac{P_N(Z)}{N^2(Z+2)}.
 \tag{31}
\]
It has value one at \(-2\) and zero full jets at every double node:
\(P_N'(-2)=N^2\). For \(m\ge2\), the polynomial
\(e^{N\mathcal I_m}E_N\) obeys the physical profile
\(\mathcal J_m(j/N)+o(1)\) in logarithmic scale, since its only
nonzero physical datum is at the last row. But at real midpoints
\(Z_N=2\cos(2\pi k/N)\), \(k/N\to u\in(0,1/2)\), its rate is
\(\mathcal I_m>\mathcal J_m(u)\). Here \(P_N(Z_N)=4\), and
\(Z_N+2\) stays bounded away from zero.
This is not an actual filled-leaf solution. It explains why (10)
is a trace-compatible representative, rather than a claimed
off-grid consequence for the canonical output of (1).

Complete direct sources were read at the following unchanged pins,
and their used implications and hashes checked:

* [Actual physical-color profile](research_filled_leaf_physical_color_profile.md),
  SHA256 8d9d8feea838832950fbe85f049d33111224ffd3d12e37067c16cd2dc4e3fae9:
  complete fresh read; the original row values, first normals,
  complex microscopic parameters, and partial-action normalization.
* [Calibrated terminal phase](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd:
  complete unchanged read retained from the preceding author/source
  cycle; its analytic branch, signed reflection and constants
  were reread here.
* [Retained-boundary energy](research_retained_boundary_leaf_energy_profile.md),
  SHA256 e6d91b27e4c87e573e1f3cd471ea759a39ebff37f3f0e90622678cc5ed3579e7:
  complete fresh read; the full signed work differential,
  capacity domain and restricted positive-branch interpretation.
* [Two-half-plane original source](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  complete fresh read; the full-normal residue normalization,
  relative-interface orientation and shared-source scope.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or compilation
was run. Adopted notes and public manuscripts remain unchanged.
