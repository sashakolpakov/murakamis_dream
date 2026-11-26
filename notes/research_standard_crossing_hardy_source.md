# Standard crossing classes with universal Hardy caps

Private written proof, 22 November 2026.

The crossing Gaussians in the initialized reduced Hardy source can be
absorbed into the canonical numerator. The new caps have zero crossing
power and are universal. A retained-cut Hermite interpolation estimate
proves a global error with a strict gap below the complete action.
Consequently the new source has the actual all-order small-charge
initializer and the original unit-charge value.

Its exact charge-shift forcing contains the same filled boundary row,
rather than changing that vertex to zero crossing power. The comparison
does not give the sharp upper bound at the smaller filled action.

## 1. Original classes and the new source

Fix the graph and complete outside data of the reduced-source proof.
The selected set \(I\) is nonempty and has no isolated vertex.
Every original retained edge remains, including complete-only factors.
Write
\[
 N\ge2,\quad D=N-1,\quad\eta=(-1)^D,\quad
 P_N(z)=2T_N(z/2)+2,\quad
 \mathcal A_N=\mathbb C[z]/(P_N),\quad
 B_r(z)=T_r(-z/2).
 \tag{1}
\]
Canonical representatives have degree less than \(N\). They retain
the first normals at double spectral roots and the odd simple value.

For fixed real powers \(\boldsymbol b\), let
\[
 V_{b,N}=C_{N,b}^{-1}R_b,\qquad
 C_{N,b}=e^{\pi ibD^2/(4N)} .
 \tag{2}
\]
The class \(V_{b,N}\) has the full Hermite data of
\(e^{ibNt^2/(4\pi)}\) at the original physical angular lifts.
For integral \(b\), \(R_b\) is the literal original signed crossing
power. The same finite Hermite definition gives its real-power
extension when that extension is used.

Let
\[
 F_N=\prod_{\{v,w\}\in E}K_N(t_v,t_w),\qquad
 Q_N=\mathcal R_I F_N,\qquad M_0=|E|M_\infty ,
 \tag{3}
\]
where \(\mathcal R_I\) is the full Hermite remainder in the selected
spectral variables \(z_v=-2\cos t_v\). Define the standard numerator
and the universal-cap source by
\[
 A_{N,\boldsymbol b}
    =\mathcal R_I\!\left(Q_N\prod_{v\in I}V_{b_v,N}(z_v)\right),
 \qquad
 \mathscr S_{N,\boldsymbol\sigma}^{\,\boldsymbol b}
       (\boldsymbol\chi)
    =\left[\bigotimes_{v\in I}
                  \mathscr T_{\sigma_v,0,\chi_v}\right]
                                     A_{N,\boldsymbol b}.
 \tag{4}
\]
Here \(\mathscr T\) is the height-free Hardy cap of the direct source.
It uses orthogonal positive or negative angular Fourier projection
followed by the original derivative sampling. All carriers (2) are
restored at the end. No power or scalar is fitted to a closed invariant.

There are \(C,A,c>0\), depending on this fixed graph and power vector,
such that for every complex charge vector,
\[
 \left|\mathscr G_{N,\boldsymbol\sigma}
               (\boldsymbol b,\boldsymbol\chi)
          -\mathscr S_{N,\boldsymbol\sigma}^{\,\boldsymbol b}
               (\boldsymbol\chi)\right|
 \le CN^A\prod_v(1+|\chi_v|)^2
       e^{N\{M_0-c+\pi\sum_v|\Im\chi_v|\}} .
 \tag{5}
\]
The source \(\mathscr G\) on the left is the initialized reduced
Hardy source before absorption. Constants may be chosen uniformly
on a fixed bounded real power box. In particular (5) is a global
complete-action-gap estimate at real powers and charges.

## 2. The one-slot Hermite divisor

Keep all other selected angles real, and regard \(Q_N\) as a canonical
polynomial in one variable \(z=-2\cos t\). Let
\[
 \Theta(z)=\arccos(-z/2),\qquad
 f_N(z)=Q_N(z)e^{ibN\Theta(z)^2/(4\pi)} .
 \tag{6}
\]
The square \(\Theta^2\), continued from \([-2,2)\), is single valued
and holomorphic on \(\mathbb C\setminus[2,\infty)\). Its apparent
singularity at \(-2\) is removable: the local inverse cosine has
a square-root zero there, whose square is analytic. At the right
cut the two boundary values are \(\Theta_\pm(2\cosh y)=\pi\pm iy\).

Let \(I_Nf_N\) be the degree-less-than-\(N\) Hermite interpolant at
the full physical spectrum. Its exact class is
\[
                I_Nf_N=\operatorname{can}_{P_N}(V_{b,N}Q_N).
 \tag{7}
\]
This is equality of all required jets, including the odd simple node.

Choose a fixed small \(h>0\), and let \(\Gamma_h\) be the positively
oriented ellipse \(z=-2\cos(s-ih)\), \(-\pi\le s\le\pi\), with its
two banks at the cut point interpreted separately. For real
\(z<2\) in the enclosed interval, the interpolation error is
\[
 \begin{split}
 E_N(z)&=\frac{f_N(z)-I_Nf_N(z)}{P_N(z)}\\
 &=\frac1{2\pi i}\left\{
    \int_{\Gamma_h}\frac{f_N(\zeta)}
                          {P_N(\zeta)(\zeta-z)}\,d\zeta
   +\int_{2}^{2\cosh h}
       \frac{f_{N,+}(\zeta)-f_{N,-}(\zeta)}
                          {P_N(\zeta)(\zeta-z)}\,d\zeta\right\}.
 \end{split}
 \tag{8}
\]
At physical roots the first quotient is interpreted by removal.
The upper bank is oriented from \(2\) to the outer endpoint; the
lower bank has the opposite orientation.

For completeness, this is the confluent error formula without a
source-equivalence assumption. Integrate on the boundary of the
ellipse with its slit removed. Subtract \(P_N(z)\) times the Cauchy
integral in (8) from \(f_N(z)\). The resulting kernel contains
\((P_N(\zeta)-P_N(z))/(\zeta-z)\), a polynomial in \(z\) of degree
less than \(N\). Near every physical root its difference from \(f_N\)
is divisible by the full \(P_N\). It is therefore precisely \(I_Nf_N\).
Small excision circles at the cut endpoints give (8) by limits.
No cut bank or branch-end contribution has been discarded.

We next prove, uniformly in all other real selected angles,
\[
             \sup_{-2\le z\le2}|E_N(z)|
                      \le CN^A e^{N(M_0-c_1)}
                         \qquad(c_1>0).
 \tag{9}
\]
The endpoint \(z=2\) in (9) is a continuous limit, not an assertion
that the spectral Gaussian is analytic at that branch point.

## 3. Outer ellipse and retained cut estimates

Let \(c_Q>0\) be the high-mode gap in the reduced-source proof, and
\(d_v\) the selected incidence degree. Its bounds give, for a shift
only in the chosen coordinate,
\[
 |Q_N(\boldsymbol s-ih\mathbf e_v)|
 \le CN^A\left\{
 e^{N(M_0+C_\Gamma h^2)}
             +e^{N(M_0-c_Q+d_vh)}\right\}
 \tag{10}
\]
when every real selected angle has modulus at most a sufficiently
small fixed \(a\). The first term uses the actual local full-kernel
phase, real on the real cube, so its first vertical real derivative
vanishes. The second is the actual reduction error.

Outside this cube the global real profile and its weighted extension
instead give
\[
 |Q_N(\boldsymbol s-ih\mathbf e_v)|
 \le CN^A\left\{
 e^{N\{M_0-c_a+(1+\gamma)d_vh\}}
             +e^{N(M_0-c_Q+d_vh)}\right\},
 \quad c_a=\gamma(1-\cos a)>0,\quad\gamma=1/200 .
 \tag{11}
\]
This includes the case where a different selected angle is outside
the central cube.

On the outer ellipse the continued Gaussian is \(e^{ibN(s-ih)^2/(4\pi)}\),
with modulus at most \(e^{N|b||s|h/(2\pi)}\), and
\[
 |P_N(-2\cos(s-ih))|
       \ge e^{Nh}(1-e^{-Nh})^2 .
 \tag{12}
\]
Choose \(a<\min\{1,\pi/(1+|b|)\}\), so that
\(|b|a/(2\pi)<1/2\). Next choose \(h>0\) small enough that
\(C_\Gamma h^2\) is less than \(h/4\), and that all linear height
costs in (10)--(11), including \(|b|h/2\), are smaller than fixed
fractions of \(c_Q\) and \(c_a\). The first central term then pays
at least \(Nh/4\) after (12); every other term retains a fixed gap.
The distance from the ellipse to \([-2,2]\) has a positive lower
bound depending only on this fixed \(h\). Its length is bounded.
The outer integral in (8) is therefore \(CN^A e^{N(M_0-c_2)}\)
uniformly on that interval, for some \(c_2>0\).

The cut estimate is separate. At \(\zeta=2\cosh y\), \(0\le y\le h\),
the endpoint profile plus the reduction error give
\[
 |Q_N(2\cosh y,\boldsymbol s_{\ne v})|
            \le CN^A e^{N(M_0-c_{\rm end}+C_\Gamma y)},
       \qquad c_{\rm end}=\min\{c_Q,2\gamma d_v\}>0 .
 \tag{13}
\]
The exact jump and denominator are
\[
 \begin{split}
 f_{N,+}-f_{N,-}
   &=-2Q_N(2\cosh y)
          e^{ibN(\pi^2-y^2)/(4\pi)}\sinh(bNy/2),\\
 d\zeta&=2\sinh y\,dy,\qquad
 P_N(2\cosh y)=4\cosh^2(Ny/2).
 \end{split}
 \tag{14}
\]
For real \(z\le2\), write \(\delta=2-z\). Since
\(\zeta-z\ge\delta+y^2\), the absolute cut density in (8) is bounded by
\[
 CN^{A+1}|b|\,
    e^{N\{M_0-c_{\rm end}+(C_\Gamma+|b|/2-1)y\}}
                                  \frac{y^2}{\delta+y^2}\,dy .
 \tag{15}
\]
We used \(|\sinh(bNy/2)|\le C|b|Ny\,e^{N|b|y/2}\).
Shrink \(h\) further so that the linear exponent in (15) consumes
at most \(c_{\rm end}/2\). The remaining factor is at most one
and is integrable uniformly even as \(z\uparrow2\).
This proves (9), with the right-cut contribution retained.
When \(b=0\), that contribution vanishes exactly.

For each real \(z\), \(E_N(z)\) is a canonical polynomial in every
other selected spectral variable. Cosine Parseval therefore turns
(9) into the same bound, up to a graph constant, for its Chebyshev
coefficient norm in all those variables. This is a uniform real
divisor estimate for the actual numerator, not an assumption about
the interpolation norm of an arbitrary function.

## 4. Exact ideal defect and tensor absorption

The raw angular Hardy formula extends to even functions holomorphic
on the original angular rectangle. For such a function \(p\), the
elementary identity
\[
                  P_N(-2\cos t)\,W_N(t)=-\eta
 \tag{16}
\]
cancels the complete sampling denominator. Take its zero-height
limit, including the vertical current, which tends to zero. With
\(\kappa=N(1-\chi)\), the exact rank-one defect is
\[
 \mathscr T_{\sigma,0,\chi}^{\rm raw}[P_Np]
       =-2\sigma i\eta N^2\,\frac1{2\pi}
                 \int_{-\pi}^{\pi}\sin t\,p(t)e^{i\kappa t}\,dt .
 \tag{17}
\]
The minus identity also follows by reflection; the two defects
cancel in the original cosine average. Formula (17) uses the
actual angular function, not a replacement spectral branch.

Set
\[
 A_v=\mathscr T_{\sigma_v,b_v,\chi_v},\qquad
 B_v=\mathscr T_{\sigma_v,0,\chi_v}M_{V_{b_v,N}}
                             \quad\hbox{on }\mathcal A_N .
 \tag{18}
\]
For a slice of the original \(Q_N\), their difference is the raw
zero-power cap applied to \(f_N-I_Nf_N=P_NE_N\). By (9), (17) and
Parseval, its output coefficient vector in the other variables has
norm
\[
               \|(A_v-B_v)Q_N\|_{\mathrm{coef},\,I\setminus\{v\}}
       \le CN^A e^{N\{M_0-c_1+\pi|\Im\chi_v|\}} .
 \tag{19}
\]
The pullback \(E_N(-2\cos t)\) is even and holomorphic near all
physical angles, because the full interpolation error has the
required angular double zeros. Its possible spectral branch at
\(2\) causes no angular singularity in (17). Bound (9) suffices
on the real integral.

All other factors in the tensor telescope have polynomial coefficient
norms at fixed real powers. The original \(A_u\) rows have the proved
Hardy bounds. For the absorbed \(B_u\), the Hardy coupon bound at
unit charge gives
\[
 \|V_{b_u,N}\|_{\mathrm{Cheb},2}
          \le CN^{3/2}\log(2N)(1+|b_u|)^2 .
 \tag{20}
\]
The cosine product identity bounds multiplication by its
\(\ell^1\) coefficient norm, hence by \(\sqrt N\) times (20).
The remainder map for a product of two degree-less-than-\(N\)
polynomials has a level-independent Chebyshev norm.
Consequently \(M_{V_{b_u,N}}\), and then \(B_u\), have polynomial
norms, with the cap's explicit factor
\((1+|\chi_u|)^2e^{\pi N|\Im\chi_u|}\).

Fix an order on \(I\). Operators in different slots commute. Thus
\[
 \left(\prod_vA_v-\prod_vB_v\right)Q_N
  =\sum_v\left(\prod_{u<v}B_u\right)
          \left(\prod_{u>v}A_u\right)(A_v-B_v)Q_N .
 \tag{21}
\]
In each summand the difference is applied first to the original
\(Q_N\). No endpoint or central profile of an already-twisted
numerator is assumed. Apply the polynomial row bounds to (19);
absorb the fixed logarithmic factors into a power of \(N\).
This proves the global comparison (5).

## 5. Initializer and exact original readouts

The absorbed source has the exact original cosine average and unit
endpoint:
\[
 2^{-|I|}\sum_{\boldsymbol\sigma}
       \mathscr S_{N,\boldsymbol\sigma}^{\,\boldsymbol b}
                            (\boldsymbol\chi)
       =\widetilde Z_N(\boldsymbol b,\boldsymbol\chi),\qquad
 \mathscr S_{N,\boldsymbol\sigma}^{\,\boldsymbol b}(\boldsymbol1)
       =\widetilde Z_N(\boldsymbol b,\boldsymbol1).
 \tag{22}
\]
Indeed the universal cap averages to the original zero-power trace
with its full cosine coupon, while \(V_{b_v,N}\) supplies exactly
the original crossing values and first normals. Canonical
multiplication preserves every mixed product-rule term.
The carriers (2) restore the original framing normalization.
No nilpotent direction or level parity has been dropped.

The existing Hardy initializer can start at arbitrarily small fixed
positive \(\boldsymbol\xi=\delta\boldsymbol1\), with
\(S(\boldsymbol\xi)=M_0+O(\delta^2)\). Choose \(\delta\) smaller
than the fixed comparison gap in (5), then shrink a fixed complex
seed neighborhood. Formula (5) is exponentially small relative to
the actual initialized branch there. Therefore
\(\mathscr S_{N,\mathbf+}^{\,\boldsymbol b}\) has the same nonzero
all-order expansion, marked phase and prefactor as \(\mathscr G\).
Every fixed charge derivative has the same conclusion on a smaller
neighborhood. Suppressed sign choices retain their seed gap.
Outside data are complete for this analytic assertion.

Charge reflection \(\chi_v\mapsto2-\chi_v\) exchanges the corresponding
universal caps. The equality of the cosine averages in (22) therefore
preserves every independent signed Gaussian heat readout at unit
charge: the difference from the initialized Hardy family has zero
all-even charge projection, and these heat operators commute with
reflection. Their Gaussian integrals converge by the row bounds and
polynomial multiplier norms. This statement concerns the original
prescribed readouts. The absorbed off-endpoint family is not assigned
the previous simple heat PDE; its power dependence now lies in a
finite Hermite class rather than a literal Gaussian inside the cap.

## 6. A fixed-filling rank-one connection

There is a precise additional gain from universal caps. Define
\[
 m_N(\chi)=\frac1{2\pi}\int_{-\pi}^{\pi}
                    \sin t\,e^{iN(1-\chi)t}\,dt
       =\frac{i\sin(\pi\kappa)}{\pi(1-\kappa^2)},\qquad
                         \kappa=N(1-\chi).
 \tag{23}
\]
The values at \(\kappa=\pm1\) are removable, and
\(|m_N(\chi)|\le2/\pi\) for real \(\chi\).
For a canonical \(p=\sum_{r=0}^{D}p_rB_r\), multiplication by
\(2B_1=-z\) has only one overflow. It is
\(p_D(B_N-\eta)=-\eta p_DP_N/2\). Apply (17) and
\(\phi_N(p)=N^2p_D/2\). This proves
\[
 \begin{split}
 &\mathscr T_{\sigma,0,\chi+1/N}[p]
    +\mathscr T_{\sigma,0,\chi-1/N}[p]
    +\mathscr T_{\sigma,0,\chi}[zp]\\
 &\hspace{35mm}=2\sigma i\,m_N(\chi)\phi_N(p),
 \end{split}
 \tag{24}
\]
where \(zp\) in the third cap is interpreted in the full algebra.
Every normal is retained in this identity.

Apply (24) to \(V_{b,N}p\). Multiplication by \(z\) commutes with
the original crossing class, so the forcing becomes
\[
                  2\sigma i\,m_N(\chi)\phi_N(V_{b,N}p).
 \tag{25}
\]
It is the same filled boundary row, with its original signed power,
not a zero-power surgery at that vertex. After gluing, setting one
charge to one applies the exact original filled trace at that vertex
while leaving the other charged Hardy rows intact. This is the
corresponding boundary face of the new source. Averaging the remaining
signs recovers the original charged partial source. Thus (25)
organizes the forcing over faces with fewer free charges without
changing a filling slope.
The observable \(zp\) remains part of the full \(N\)-dimensional
Hermite module; no scalar closure or bounded-rank reduction of
that module is asserted.

This fixed-filling source compatibility and the proved initializer
are the gains. The bound (5) is at complete-action scale \(M_0-c\);
it need not be below the smaller filled action at unit charge.
Neither (24) nor a polynomial local norm supplies a sharp
Rivin-relative upper estimate. No new knot class, volume lower
bound or finite-exception theorem is claimed.

## Complete direct sources

- [Initialized reduced Hardy source](research_hardy_reduced_polarized_source.md),
  443 lines, SHA256
  e5d38be5b87e3f268bee40884b43aaabd5f2a7022a075c7960c659738ac5d280:
  exact Fourier caps, polynomial rows and coupons, all source
  normalizations, signed heat readouts and actual initializer.
- [Hermite-reduced initializer](research_hermite_reduced_polarized_initializer.md),
  439 lines, SHA256
  a77d3e81cb14400cc8027055f45479b977717da7cf80dbaeb9fcecf2379dc04b:
  canonical numerator, high-mode error, exact aliases and bounded
  Chebyshev remainder maps with all normal channels.
- [Full angular source](research_full_midpoint_polarized_initializer.md),
  603 lines, SHA256
  65a91ee6538b05355bab5056d32b2fe563c47eeff1e1924b1be259ef5cd628ad:
  actual full-kernel central expansion, global real profile and its
  weighted continuation, complete normalization and arbitrary tiny seed.

The entire proof and all three complete direct sources were read at
these matching versions before author freeze. Root's whole-draft
mathematical review is complete; matching entire-final reviews are
separate. Only written mathematics, text reads, hashes and this
new-file patch are used. No mathematical programs, numerical
experiments, tests, builds or git commands are run. No previous final
or public manuscript is edited.
