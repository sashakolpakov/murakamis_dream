# A nonzero canonical cutoff period with an exponentially controlled defect

Private written proof, 18 November 2026.

This note combines the actual finite-Laplace current [B], the
polynomial horn [H], and the canonical monodromy [J]. It constructs
a nonidentically-zero analytic period satisfying the original
quantum equation up to one explicitly bounded cutoff exponential.
Neither a leading geometric exponential nor a lower bound at the
physical levels is inferred.

## 1. The actual source and the contour geometry

Use the source and the actual finite-shift operator of [J] and [B]:
\[
 \widehat{\mathscr W}(h,Y)=\sum_{j\ge0}h^j w_j(Y),\qquad
 \mathcal P(h)=\sum_{\nu\in J_0}p_\nu(h,Y)T^\nu,\qquad
 T f(Y)=f(e^hY),\qquad \mathcal P\widehat{\mathscr W}=0.
 \tag{1}
\]
Here \(h=\log Q\), coefficients stand on the left, and \(J_0\)
is finite. The coefficients are holomorphic near \((0,\alpha)\).
The point \(\alpha\ne0,1\) is a simple Alexander root, and the
classical symbol has the transverse-node properties of [J].
Retain its constants
\[
 r=\Delta_K'(\alpha)^{-1},\qquad
 A=\frac{\alpha^2}{2}P_{LL}(\alpha,1),\qquad
 B=\alpha P_{YL}(\alpha,1),\qquad \eta_*=\frac{B}{2A}\ne0.
 \tag{2}
\]
Write \(z=Y-\alpha\). To distinguish the two Borel coordinates, put
\[
 \mathfrak b(z,\eta)=
   \sum_{j\ge0}z^{2j+1}w_j(\alpha+z)\frac{\eta^j}{j!},
 \qquad
 \mathfrak B(Y,\xi)=\sum_{j\ge0}w_j(Y)\frac{\xi^j}{j!}.
 \tag{3}
\]
Initially \(\mathfrak B(Y,\xi)=z^{-1}\mathfrak b(z,\xi/z^2)\).
Every continuation below is the one of this canonical germ.

Choose a small nonzero base point \(\eta_b\) in its initial
\(\eta\)-disk. Choose a simple closed loop \(\lambda\), based there,
winding once around \(\eta_*\) and not around zero. Choose a simple
tail \(\tau\) from \(\eta_b\), otherwise disjoint from the loop,
lying in the exterior of its Jordan domain and eventually equal
to an outward straight ray. Its finite initial portion avoids zero.
There is no topological restriction in these choices: after rotating
the plane so that \(\eta_*>0\), one can take
\(0<\eta_b<\eta_*\) small and the circle centered at \(\eta_*\)
through \(\eta_b\). A tail starts into its exterior and goes around
that circle before following a ray to infinity.

Let \(\sigma\) be a path from zero to \(\eta_b\) in the original
germ. For a sufficiently large tail endpoint \(\eta_e\), use the
two paths
\[
 \gamma_0=\sigma\,\tau_{\eta_e},\qquad
 \gamma_1=\sigma\,\lambda\,\tau_{\eta_e}.
 \tag{4}
\]
The two occurrences of the tail have the same projection and the
branches obtained from their respective histories. The paths are
fixed geometric paths; the loop has not been removed by a homotopy
of a single-valued density.

The loop difference \(\Delta\mathfrak b\) at the base is holomorphic
near \(z=0,\eta=\eta_b\), and [J] gives
\[
 \Delta\mathfrak b(0,\eta_b)
       =-2r(1-\eta_b/\eta_*)^{-1/2}\ne0.
 \tag{5}
\]
After shrinking that neighborhood the difference stays nonzero.
Its continuation along the tail therefore cannot vanish identically
on any open tail segment.

## 2. A common fixed-\(\xi\) contour and meridian disk

Use [H] for the two path histories in (4), with a slightly enlarged
angular interval around the eventual tail ray. Let \(\kappa\ge2\)
be a common horn exponent. Fix a sufficiently small \(z_0\ne0\),
write \(Y_0=\alpha+z_0\), and choose the endpoint on that ray with
\[
 |\eta_e|=c_0|z_0|^{-1/\kappa},\qquad
 \Gamma_i=z_0^2\gamma_i,\qquad
 R=z_0^2\eta_e.
 \tag{6}
\]
The constant \(c_0>0\) is fixed and sufficiently small. For small
\(z_0\), the endpoint lies beyond the compact portions of both paths.
The common endpoint \(R\) and the two \(\xi\)-paths are independent
of the variable \(Y\) below.

There is a fixed \(\delta>0\) such that, for
\[
        D_1(z_0)=\{Y:|Y-Y_0|<\delta|z_0|\},
 \tag{7}
\]
both canonical densities are jointly holomorphic along the common
paths \(\Gamma_i\) and this meridian disk. Here is the required
uniform check. If \(z=Y-\alpha\), then \(z/z_0\) is close to one
and the corresponding scaled path is
\[
                  \eta=(z_0/z)^2\gamma_i.
 \tag{8}
\]
Small fixed \(\delta\) keeps its compact part in the same finite
continuation charts, with the same winding and without meeting
the two punctures. Its tail remains in the enlarged angular
interval. All such compact portions have uniformly bounded length
and separation from the punctures after the common initial segment.
The proof of [H] uses precisely those bounds and therefore applies
uniformly to this family.

Along (8), \(|z|\asymp|z_0|\) and
\(|\eta|\le C(1+|\eta_e|)\). Choose \(c_0\) small enough, and then
\(z_0\) small enough, that every point lies in a strictly smaller
horn, for instance with its defining product at most \(1/4\).
The strict inequality also provides neighborhoods of the paths.
The bound of [H] and division by \(z\) give
\[
 \sup_{D_1(z_0),\,\Gamma_i}|\mathfrak B(Y,\xi)|
                      \le C|z_0|^{-2}.
 \tag{9}
\]
One may replace \(D_1\) by a slightly smaller closed disk in (9).
The constants below are uniform for all sufficiently small nonzero
\(z_0\). The finite compact portions of (4) do not change
the length estimate
\[
       \operatorname{length}(\Gamma_i)
          \le C|z_0|^{2-1/\kappa},\qquad
       |R|=c_0|z_0|^{2-1/\kappa}.
 \tag{10}
\]

The scaled loop in (8) gives the same local monodromy near its moved
base. Indeed these scaled compact loops are homotopic in the
punctured plane, with their bases joined inside the original germ.
Equation (5), by continuity in both variables, is uniformly nonzero
for small \(z_0\), small fixed \(\delta\), and all \(Y\) in a smaller
disk about \(Y_0\). Consequently the difference of the two
\(\mathfrak B\)-densities is nonzero near the initial tail on
every such meridian fiber.

## 3. The exact endpoint current and its scale

Define the two analytic cutoff periods
\[
 U_i(h,Y)=\frac1h\int_{\Gamma_i}
               e^{-\xi/h}\mathfrak B(Y,\xi)\,d\xi,\qquad h\ne0.
 \tag{11}
\]
Each integral uses its own continued branch. Work on
\(D_0(z_0)\Subset D_1(z_0)\), with a fixed smaller relative radius.
For \(|h|\le c_1|z_0|\), all actual finite shifts
\(e^{\nu h}Y\) stay in \(D_1(z_0)\) for \(Y\in D_0(z_0)\).
The original \(p_\nu\) are bounded there by a fixed constant.

Write \(\mathcal P(h)=\sum_{n\ge1}h^n L_n\), as in [B].
Cauchy's estimate for the actual analytic compositions
\(p_\nu(h,Y)\mathfrak B(e^{\nu h}Y,\xi)\), on the preceding
\(h\)-disk, proves
\[
 \|L_n\mathfrak B\|_{D_0,\Gamma_i}
       \le M C_d^n,\qquad
 M\le C|z_0|^{-2},\qquad C_d\le C/|z_0|.
 \tag{12}
\]
This uses the whole finite-shift operator, including negative shifts
and its original coefficient functions.

Let \(I\) be the primitive along the entire path from zero. The exact
current of [B] is
\[
 \mathcal P(h)U_i=e^{-R/h}J_i(h,Y),\qquad
 J_i=\sum_{n\ge1}\sum_{j=0}^{n-1}
              h^j I^{n-j}L_n\mathfrak B(Y,R).
 \tag{13}
\]
In particular all path histories are retained. The amplitude is
holomorphic also at \(h=0\), and \(J_i(0,Y)=0\).
For \(|h|<c_2|z_0|\), with fixed sufficiently small \(c_2\),
[B]'s actual estimate yields
\[
\begin{split}
 |J_i|
 &\le 2M\left(e^{C_d\,\operatorname{length}(\Gamma_i)}-1\right)\\
 &\le C|z_0|^{-2}
           \left(e^{C|z_0|^{1-1/\kappa}}-1\right)
 \le C|z_0|^{-1-1/\kappa}.
\end{split}
 \tag{14}
\]
All estimates are uniform on a smaller closed meridian disk.
Every fixed meridian derivative satisfies the analogous bound with
one further factor \(C/|z_0|\) per derivative, by Cauchy's estimate.
No \(Y\)-derivative of \(R\) occurs: its value in (6) is fixed on
this common disk.

For any fixed \(0<\sigma<\pi/2\), restrict further to
\[
       |\arg h-\arg R|\le\pi/2-\sigma .
 \tag{15}
\]
Then, still with \(|h|<c_2|z_0|\),
\[
 |\mathcal P(h)U_i|
 \le C|z_0|^{-1-1/\kappa}
       \exp\!\left(-c_\sigma
                    \frac{|z_0|^{2-1/\kappa}}{|h|}\right).
 \tag{16}
\]
The same bounds hold for the difference \(U_1-U_0\), with its
exact current \(J_1-J_0\). The analyticity range
\(|h|<c_2|z_0|\) and the regime of small exponential defect are
different statements; the latter requires the ratio in (16)
to be large.

The cutoff scale is beyond the local quadratic action scale:
\[
       \frac{|z_0|^{2-1/\kappa}}{|z_0|^2}
                         =|z_0|^{-1/\kappa}\longrightarrow\infty.
 \tag{17}
\]
For example, for any fixed \(C_*>0\), sufficiently small \(z_0\)
makes the exponential in (16) bounded by
\(\exp(-2C_*|z_0|^2/|h|)\).
This compares absolute defects and scales. It is not a relative
error estimate for either period or for their difference.

## 4. Nonzero monodromy gives a nonzero analytic period

We prove that for every meridian \(Y\) in the smaller disk just
specified, \(U_1(h,Y)-U_0(h,Y)\) is not identically zero as a
function of \(h\ne0\). This does not mean it is nonzero at every
individual \(h\).

The common initial path cancels in the difference. For a fixed
such \(Y\), write its remaining integral as
\[
 U_1-U_0=\frac1h\left[
   \int_{\lambda_\xi}e^{-\xi/h}B_\lambda(\xi)\,d\xi+
   \int_{\tau_\xi}e^{-\xi/h}\Delta B(\xi)\,d\xi\right].
 \tag{18}
\]
Here the subscript denotes scaling by \(z_0^2\).
\(B_\lambda\) is the density continued along the loop.
\(\Delta B\) is the difference of the two branches along the
shared tail. It is analytic in local neighborhoods along that tail
and is nonzero near its initial point by Section 2.

The bracket in (18), with \(1/h\) replaced by \(t\) in the
exponential, defines an entire function \(F_Y(t)\): both contours
are finite and both densities are bounded on their parameterized
paths. If \(U_1-U_0\) were identically zero on a punctured \(h\)-disk,
then \(F_Y(t)\) would vanish on an open set and hence identically.
Its derivatives at \(t=0\) would give all the moment identities
\[
 \int_{\lambda_\xi}\xi^nB_\lambda(\xi)\,d\xi+
 \int_{\tau_\xi}\xi^n\Delta B(\xi)\,d\xi=0,\qquad n\ge0.
 \tag{19}
\]

Consider the single-valued Cauchy transform of these fixed densities,
\[
 K_Y(w)=\int_{\lambda_\xi}\frac{B_\lambda(\xi)}{w-\xi}\,d\xi
       +\int_{\tau_\xi}\frac{\Delta B(\xi)}{w-\xi}\,d\xi.
 \tag{20}
\]
Its geometric-series expansion at infinity converges and is zero
by (19). It is holomorphic off the projected contour trace.
The identity theorem therefore makes it zero on the unbounded
component of that complement.

Both sides of any interior subarc of the final straight tail lie
in that same component. To see this directly, follow small parallel
curves along the two sides towards the free endpoint \(R\), and
join them around \(R\) in a small disk disjoint from the loop.
The tail is simple and exterior to the loop, so these curves avoid
the projected trace; they also connect to infinity. This is why a
shared exterior tail with a free endpoint was retained.

The Cauchy jump across a short straight subarc is elementary here.
Its density \(d(\xi)=\Delta B(\xi)\) is holomorphic near the subarc.
For \(w\) near an interior point write
\[
 \frac{d(\xi)}{w-\xi}
   =\frac{d(\xi)-d(w)}{w-\xi}+\frac{d(w)}{w-\xi}.
 \tag{21}
\]
The first integral extends holomorphically across the subarc.
For endpoints \(a,b\) of that short subarc, the second integral is
\(d(w)[\log(w-a)-\log(w-b)]\); its two continuations differ by
\(\pm2\pi i\,d(w)\), with sign fixed by the orientation.
The other contour pieces are holomorphic near this point.
Since both outside values of (20) are zero, \(d(w)\) must vanish
on the whole open subarc.

Analytic continuation along the tail would then make
\(\Delta B\) zero near its initial point. This contradicts Section 2.
Thus (19) cannot hold, proving the asserted nonidentical vanishing.
The argument uses actual canonical monodromy, not an arbitrary
choice of a homogeneous solution.

There is also a precise nontriviality statement modulo the cutoff
amplitude. Put \(D_Y(t)=tF_Y(t)\). It is entire, nonzero, and
\(D_Y(0)=0\). It cannot have the form
\[
                 D_Y(1/h)=e^{-R/h}H(h)
 \tag{22}
\]
on a full punctured neighborhood of \(h=0\), with \(H\) holomorphic
at zero. Indeed \(e^{Rt}D_Y(t)\) would be entire and equal to
\(H(1/t)\) for all sufficiently large \(|t|\). It would be bounded
at infinity and therefore constant. Its value at zero is zero,
contradicting the nonzero period. Thus the actual monodromy period
has a nonzero class modulo \(e^{-R/h}\mathcal O_{h=0}\).
This is a full punctured-germ assertion, not a quotient by arbitrary
sectorially flat functions.

## 5. Exact scope and complete proof sources

Equations (11)--(16) construct canonical analytic quasimodes for the
actual supplied quantum operator, with the original normal gauge
retained as in [B]. Equation (18) is a nonzero analytic quasimode
difference. Its defect consists solely of the displayed endpoint
exponential and the explicitly retained current. Its nonzero
punctured-germ class modulo holomorphic cutoff amplitudes is distinct
from a selected asymptotic contribution.

The result does not identify these integrals with the original
finite-color scalar, locate the nearby moving Borel singularity,
compute a leading \(e^{-S/h}\) coefficient, or rule out zeros at
the physical root-of-unity sequence. It proves no fixed-\(z\)
infinite Laplace sum or arbitrary-short-filling volume lower bound.
The transverse-node assumptions remain those of the actual source
in [J]; they are not asserted for every knot.

The complete proof directs are:

| Label | Complete source | SHA256 |
|---|---|---|
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |
| H | notes/research_classical_verma_borel_polynomial_horn.md | 35347248ca73a1d37ab76fda8df13d3502ad042df7f13fd30ff8b24a5ae35fd1 |
| J | notes/research_classical_verma_borel_joint_continuation.md | 67cbb4c1577af04336b53985e867f6d2adc7e184c6d4276c53a0888f57d8ded8 |

B supplies the exact cutoff current, H the quantitative continued
source bounds, and J its nonzero canonical monodromy. The common
meridian disk, endpoint scale, uniform current estimate, and
Cauchy-transform nonvanishing argument are proved above.
No external proof, mathematical program, test, or build is used.
Frozen proofs and public manuscripts are unchanged.
