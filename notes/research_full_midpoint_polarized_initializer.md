# A full-midpoint polarized source with a genuine initializer

Private written proof, 22 November 2026.

The original trace admits a polarized representative with angular cuts
at \(-\pi,\pi\), one fixed positive height per selected vertex, and no
removed-row table. For every fixed same-index graph and fixed real
crossing powers, sufficiently small positive charges initialize this
representative with the original nonzero geometric Gaussian.
The proof bounds every added horizontal wing and every full-midpoint
vertical current using the ordinary real-kernel profile.

This constructs a different representative of the same exact endpoint
and heat-readout class. It does not prove the action-relative upper
bound along a path to unit charge.
At fixed powers a holomorphic complex-height choice also centers the
horizontal contours on a supplied positive critical curve. That choice
keeps the endpoint and the initializer; it is not assigned the
fixed-height heat equation.

## 1. The exact full-midpoint family

Fix \(N\ge2\), \(D=N-1\), and \(\eta=(-1)^D\). Let \(\Gamma\) be a
fixed finite same-index graph with a nonempty selected vertex set \(I\),
\(m=|I|\), and no isolated selected vertex. Keep all retained original
edges \(E\), including edges with both endpoints outside \(I\), and put
\(e=|E|\). Loops count twice in the selected incidence degrees \(d_v\).
All outside angles equal zero. Retain the ordinary polynomial
\[
 F_N(\mathbf t)=\prod_{\{v,w\}\in E}K_N(t_v,t_w),\qquad
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u).
 \tag{1}
\]
It is separately even and has angular degree at most \(d_vD\) in
each selected variable. Complete-only edge factors remain in (1).

For an even angular spectator \(A\), set
\[
 g_n[A](t)=\sin t\,A(t)e^{inNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
\]
For fixed \(h>0\), a sign \(\sigma=\pm1\), and either fixed side
\(\epsilon=\pm1\), define the carrier-removed operators
\[
 \begin{split}
 \mathcal H_{\sigma,n,\chi}^{h}[A]
 &=-\frac{N^2}{\pi i}
   \int_{-\pi-ih}^{\pi-ih}
       g_n[A](t)e^{\sigma iN(1-\chi)t}W_N(t)\,dt,\\
 \mathcal V_{n,\chi}^{h,\epsilon}[A]
 &=\frac{\epsilon\eta N^2}{\pi}
   \int_{-h}^{h}
       \frac{g_n[A](\epsilon\pi+iv)
             \cos(N(1-\chi)(\epsilon\pi+iv))}
                  {4\cosh^2(Nv/2)}\,dv,\\
 \mathcal T_{\sigma,n,\chi}^{h}
 &=\mathcal H_{\sigma,n,\chi}^{h}
                         +\mathcal V_{n,\chi}^{h,\epsilon}.
 \end{split}
 \tag{2}
\]
These are exactly the original midpoint operators at \(a=\pi\).
Every physical angle lies strictly inside this cut, so there is no
removed-row term. Their sign average is the original full Hermite
trace with its entire cosine charge coupon, with the crossing carrier
\[
                 C_{N,n}=e^{\pi inD^2/(4N)}
 \tag{3}
\]
removed. The odd simple node and all double-node first normals are
included in that trace identity.

Choose fixed positive heights \(\mathbf h\), held fixed as powers and
charges vary, and define
\[
 \mathcal G_{N,\boldsymbol\sigma}^{\mathbf h}
       (\mathbf n,\boldsymbol\chi)
   =\left[\bigotimes_{v\in I}
       \mathcal T_{\sigma_v,n_v,\chi_v}^{h_v}\right]F_N .
 \tag{4}
\]
The side choices in (2) are fixed too. The exact identities are
\[
 \begin{split}
 2^{-m}\sum_{\boldsymbol\sigma}
       \mathcal G_{N,\boldsymbol\sigma}^{\mathbf h}
       &=\widetilde Z_N(\mathbf n,\boldsymbol\chi),\\
 \mathcal G_{N,\boldsymbol\sigma}^{\mathbf h}(\mathbf n,\mathbf1)
       &=\widetilde Z_N(\mathbf n,\mathbf1),\\
 \partial_{n_v}\mathcal G_{N,\boldsymbol\sigma}^{\mathbf h}
       &=-\frac{i}{4\pi N}\partial_{\chi_v}^2
                   \mathcal G_{N,\boldsymbol\sigma}^{\mathbf h}.
 \end{split}
 \tag{5}
\]
Here \(\widetilde Z_N\) is the literal original cosine source with
\(\prod_vC_{N,n_v}\) removed. Reflection
\(\chi_v\mapsto2-\chi_v\) exchanges \(\sigma_v\).
All operators act on the unreduced polynomial (1).

The first two identities follow from the exact trace formula (2),
by averaging signs and then setting the charge to one. For the last,
differentiate the fixed compact integrals: the Gaussian and either
charge exponential or cosine satisfy that heat equation pointwise.
No moving-endpoint derivative occurs. The same finite-integral
argument proves entirety in powers and charges.

For powers in a fixed bounded real box there are constants \(C,A,p\)
such that
\[
 |\mathcal G_{N,\boldsymbol\sigma}^{\mathbf h}|
 \le CN^p\prod_v(1+|\chi_v|)
  \exp N\left[A+\sum_v
       \{\pi|\Im\chi_v|+h_v|1-\Re\chi_v|\}\right].
 \tag{6}
\]
For fixed heights the horizontal denominators are uniformly bounded
away from zero; the vertical denominators have modulus at least four.
The weighted bound (8), proved from the ordinary real profile below,
bounds the numerator on these fixed contours by \(CN^p e^{NA_0}\).
The crossing Gaussians add a bounded exponential constant on a bounded
real-power box. The charge factors give the displayed exponential
type, proving (6). Thus the signed Gaussian heat integrals and their
finite translations are valid.

In particular (4) and the prescribed pattern-adapted family give the
same unit-charge readout after every independent signed real heat step.
Their difference has zero all-even charge projection. The independent
heat operators commute with that projection, and their signed Gaussian
integrals annihilate the remaining odd sectors. This comparison concerns
these prescribed exponential-type families: (6) and the corresponding
pattern-family bound ensure convergence of every stated readout.
This is an exact readout identity, including zero sources, rather than a comparison
of individual local saddle pieces.

## 2. A weighted polynomial continuation bound

Write \(M_\infty=\psi(0,0)\) for the original complete edge action
and \(\gamma=1/200\). The ordinary real-kernel profile in the mixed-current
source, Lemma 2, gives on the entire real square
\[
 |K_N(s,t)|\le CN^A
  \exp N\{M_\infty-\gamma(1-\cos s)-\gamma(1-\cos t)\}.
\]
Consequently the full ordinary numerator satisfies
\[
 |F_N(\mathbf s)|\le CN^A
  \exp N\left[eM_\infty-
                  \gamma\sum_{v\in I}d_v(1-\cos s_v)\right].
 \tag{7}
\]
Every original index is present; a loop contributes its two incidence
losses. No restriction to physical spectral samples is made here.

There is a useful direct extension of (7). For all real \(\mathbf s\)
and real \(\mathbf y\),
\[
 |F_N(\mathbf s+i\mathbf y)|\le CN^A
  \exp N\left[eM_\infty-
      \gamma\sum_vd_v(1-\cos s_v)
                  +(1+\gamma)\sum_vd_v|y_v|\right].
 \tag{8}
\]
To prove it, first take \(y_v\ge0\) and put \(z_v=e^{it_v}\).
The Laurent polynomial \(F_N\) has frequencies between
\(-L_v,L_v\), where \(L_v=d_vD\). Hence
\[
 P_N(\mathbf z)=\prod_v z_v^{L_v}F_N(\mathbf t)
\]
is an ordinary polynomial. On the distinguished unit torus, (7)
and the holomorphic weight
\(\exp\{N\gamma\sum_vd_v(1-z_v)\}\) bound their product by
\(CN^Ae^{NeM_\infty}\). The maximum principle on the polydisk gives
the same bound inside. Substituting \(z_v=e^{is_v-y_v}\) gives
\[
 |F_N|\le CN^A\exp\left\{NeM_\infty+\sum_vL_vy_v
                   -N\gamma\sum_vd_v(1-e^{-y_v}\cos s_v)\right\}.
\]
Use \(L_v\le Nd_v\) and \(1-e^{-y_v}\le y_v\).
This proves (8) in that orthant. Separate evenness of \(F_N\)
allows an independent sign flip of every coordinate with \(y_v<0\),
leaving \(\cos s_v\) unchanged, and proves the full assertion.
In particular the bound is uniform at the full endpoints
\(s_v=\pm\pi\); there is no square-root loss in the height.

## 3. A sufficiently small genuine seed

Fix real powers \(\mathbf b\). The phase of the selected all-plus
exponential is
\[
 \Phi_{\boldsymbol\chi}(\mathbf t)
  =\sum_{\{v,w\}\in E}\psi(t_v,t_w)
      +\sum_{v\in I}
          \left(\frac{ib_vt_v^2}{4\pi}-i\chi_vt_v\right).
 \tag{9}
\]
Its complete value is \(eM_\infty\). At zero angles and charges,
\[
 \Phi_{\mathbf t\mathbf t}(0,0)
        =-\frac1{2\pi}\operatorname{diag}(d_v-ib_v).
 \tag{10}
\]
This follows from the original edge matrix \(K_e(0,0)=I\).
Every selected \(d_v\) is positive. The holomorphic implicit function
theorem therefore gives a critical point \(\mathbf t^*(\boldsymbol\chi)\)
near zero, with
\[
 t_v^*(\boldsymbol\chi)
     =\frac{2\pi\chi_v}{b_v+id_v}
                              +O(\|\boldsymbol\chi\|^2).
 \tag{11}
\]
Choose a small real diagonal charge \(\boldsymbol\xi=\delta\mathbf1\).
For all sufficiently small \(\delta>0\),
\[
 h_v=-\Im t_v^*(\boldsymbol\xi)>0,\qquad
 h_v=O_{\Gamma,\mathbf b}(\delta),\qquad
 S(\boldsymbol\chi)
   :=\Phi_{\boldsymbol\chi}(\mathbf t^*(\boldsymbol\chi)),
 \quad S(\boldsymbol\xi)=eM_\infty+O_{\Gamma,\mathbf b}(\delta^2).
 \tag{12}
\]
Freeze exactly these heights in (4). Their choice is independent
of \(N\). Each \(t_v^*(\boldsymbol\xi)\ne0\) by (11).

Put \(T=19/20\) and \(c=\gamma(1-\cos T)>0\).
Shrink \(\delta\) so that the critical point lies in
\(|\Re t_v|<T/2\), all \(h_v<1/200\), and
\[
 \sum_v\{(1+\gamma)d_v+|b_v|/2\}h_v<c/8,\qquad
          |\Re S(\boldsymbol\xi)-eM_\infty|<c/8 .
 \tag{13}
\]
These choices are possible for every fixed graph and fixed powers.
They impose no uniform lower bound on the seed charge.

Expand (4) into horizontal and vertical terms and split each
horizontal segment at its real coordinates \(-T,T\).
Call a term exterior if it has a vertical coordinate or a horizontal
wing. In every such term some coordinate has real part of modulus
at least \(T\); its incidence loss in (8) is at least \(c\).

For \(0<\Re\chi<1\), on a horizontal line \(t=s-ih\) the two
charge choices obey
\[
 \left|W_N(t)e^{\sigma iN(1-\chi)t}\right|
           \le C_h e^{N\pi|\Im\chi|}.
\]
For \(\sigma=+\), the omitted decaying factor is
\(e^{-N\Re\chi h}\); for \(\sigma=-\) it is
\(e^{-N(2-\Re\chi)h}\). On a full-midpoint vertical side,
\[
 \frac{|\cos(N(1-\chi)(\epsilon\pi+iv))|}
              {4\cosh^2(Nv/2)}
       \le e^{N\pi|\Im\chi|}.
 \tag{14}
\]
The Gaussian crossing costs at most
\(e^{N|b_v|h_v/2}\), and the sine factors have bounded modulus.
Thus (8), (13), (14) bound the sum of every exterior pattern by
\[
 CN^A\exp N\left[eM_\infty-c+
       \sum_v\{(1+\gamma)d_v+|b_v|/2\}h_v
                              +\pi\sum_v|\Im\chi_v|\right].
 \tag{15}
\]
There are finitely many patterns for the fixed graph.
After shrinking a fixed complex neighborhood \(U\) of
\(\boldsymbol\xi\), this is
\[
        O\!\left(N^A e^{N(\Re S(\boldsymbol\chi)-c/2)}\right).
 \tag{16}
\]
This estimates the actual full wings and all full-midpoint currents.

## 4. The central coefficient and all orders

Only the all-horizontal central product remains. The actual full-kernel
theorem on \(|\Re t|,|\Re u|\le1\), \(|\Im t|,|\Im u|\le1/200\)
gives
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
               \left(1+\sum_{j=1}^{L-1}a_{e,j}(t,u)N^{-j}
                              +O_{\mathrm{hol}}(N^{-L})\right)
 \tag{17}
\]
at every fixed order, with the original holomorphic unit \(a_e\).
This includes complete-only edges and both level parities.

At the real base charge, the central product lies at the critical
heights (12). The original mixed-current Hessian bound gives on this
central rectangle
\[
 \Re(-\Phi_{\boldsymbol\xi}'')
          \succeq\frac1{10\pi}\operatorname{diag}(d_v)>0 .
 \tag{18}
\]
The real powers add only an imaginary diagonal. Hence the real
part of the central phase has a unique strict maximum at
\(\mathbf t^*(\boldsymbol\xi)\), with a fixed gap off any fixed
neighborhood of it. The rational horizontal denominators have
leading term one after extracting \(e^{-iNt_v}\), with exponentially
small error because every frozen \(h_v>0\).

For the all-plus family the holomorphic Gaussian expansion therefore
gives, with \(\beta=3(m-e)/2\),
\[
 \mathcal G_{N,\mathbf+}^{\mathbf h}(\mathbf b,\boldsymbol\chi)
  =N^\beta e^{NS(\boldsymbol\chi)}
       \left\{a_0(\boldsymbol\chi)
          +\sum_{j=1}^{L-1}a_j(\boldsymbol\chi)N^{-j}
                         +O_{\mathrm{hol}}(N^{-L})\right\},
 \tag{19}
\]
uniformly on a possibly smaller fixed \(U\), where
\[
 a_0(\boldsymbol\chi)=
   \left(\frac{i}{\pi}\right)^m(2\pi)^{m/2}
   \frac{\displaystyle\prod_{v\in I}\sin t_v^*(\boldsymbol\chi)
          \prod_{\{v,w\}\in E}
             a_e(t_v^*(\boldsymbol\chi),t_w^*(\boldsymbol\chi))}
        {\sqrt{\det[-\Phi_{\boldsymbol\chi}''
                                   (\mathbf t^*(\boldsymbol\chi))]}} .
 \tag{20}
\]
The determinant root is the Gaussian branch on complex symmetric
matrices with positive definite real part, continued from real
positive matrices. Every factor is a unit after shrinking \(U\),
by (11), (17), (18).

For complex charges in \(U\), move the local central contour through
the continued critical point. It stays below the physical angular
poles. Its connecting pieces keep the fixed central gap; all
exterior pieces retain (16). The full-kernel holomorphic errors and
Taylor expansion give (19) with every fixed derivative on smaller
neighborhoods. The powers are \(N^{2m}\) from the traces,
\(N^{-3e/2}\) from the full kernels, and \(N^{-m/2}\) from the
Gaussian, giving exactly \(\beta\).

At the real seed, a minus sign has the additional factor
\(e^{-2iN(1-\chi_v)t_v}\), whose modulus on its central horizontal
is \(e^{-2N(1-\xi_v)h_v}\). Thus every other sign vector has a
strict exponential gap below \(S(\boldsymbol\xi)\). This persists
on a smaller \(U\); its exterior pieces were already bounded by
(16). All exact currents remain in the family even though their
seed contributions have now been estimated.

## 5. One tensor row for the unreduced polynomial

Let \(z_v=-2\cos t_v\), and retain the coefficient vector
\[
 f_N^{\rm coef}\in\bigotimes_{v\in I}\mathbb C^{d_vD+1}
\]
of the full ordinary polynomial (1). Define the local monomial row
\[
 r_v(\chi_v)_j
    =\mathcal T_{+,b_v,\chi_v}^{h_v}
                         [(-2\cos t_v)^j],\qquad 0\le j\le d_vD .
\]
Then the exact polarized source has the factorization
\[
 \mathcal G_{N,\mathbf+}^{\mathbf h}(\mathbf b,\boldsymbol\chi)
       =\ell_N(\boldsymbol\chi)f_N^{\rm coef},\qquad
 \ell_N=\bigotimes_{v\in I}r_v,\qquad
                   \|\ell_N\|^2=\prod_v\|r_v\|^2 .
 \tag{21}
\]
The coefficient dimension is \(O_\Gamma(N^m)\).
The fixed full-midpoint family needs no sum over subset-dependent
height tables. Every row is its literal fixed-contour functional;
no spectral quotient reduction is made away from the endpoint.
The exact identities (5) retain the original normal terms.

For example, putting \(\lambda_N=1+\|\ell_N\|^2\), the elementary
positive quadratic
\[
 J(x)=\lambda_N\|x-f_N^{\rm coef}\|^2+|\ell_Nx|^2
 \quad\hbox{satisfies}\quad
              |\mathcal G_{N,\mathbf+}^{\mathbf h}|^2\le2J(x).
 \tag{22}
\]
Indeed apply Cauchy--Schwarz to
\(\ell_Nf_N^{\rm coef}=\ell_Nx+\ell_N(f_N^{\rm coef}-x)\).
Its coefficient matrix has condition number below two.
This supplies an exact upper trial with a factored row, not an
estimate of its action-relative size; its norms can be exponential.

The gain proved here is an actual initialized representative with
full cuts and one frozen height per vertex. Its seed is chosen for
the fixed graph and powers. No equality of its asymptotic data with
a differently based pattern initializer is presumed.
Its global sharp complex upper bound remains unproved, as do any
new volume lower bound or finite-exception theorem.

## 6. A holomorphic height choice at fixed powers

The full midpoint permits a further exact contour choice. Extend (2)
to a complex height \(h\) with \(\Re h>0\) by using the fixed-interval
parameterizations
\[
 t=s-ih,\quad -\pi\le s\le\pi,\qquad
 t=\epsilon\pi+ihr,\quad -1\le r\le1,\quad dv=h\,dr
 \tag{23}
\]
in the horizontal and vertical terms, respectively. In the vertical
formula the denominator is \(4\cosh^2(Nhr/2)\).
These operators are jointly holomorphic in \(h,n,\chi\).
The horizontal path is strictly below the real poles.
The slanted vertical side meets the real axis only at the midpoint
\(\epsilon\pi\); its denominator cannot vanish, since for real
\(r\ne0\) the argument \(Nhr/2\) has nonzero real part.
At \(r=0\) the denominator is four.

The same trace identity holds. One can either use the parallelogram
with vertices \(\pm\pi\pm ih\), enclosing exactly the original real
physical grid, or continue the identity holomorphically from real
positive \(h\) through the connected right half-plane.
Consequently the sign average and unit-charge identity in (5) remain
exact for independent complex heights. The same height must be used
for both signs at each fixed parameter.

We now fix the real powers \(\mathbf b\) and a supplied positive
unit-charge primitive target, with complete outside data. Use the
marked positive component and the primitive map \(P_v\) of the
formal-continuation source. Its independent sign-flip comparison
implies, at any positive configuration with real \(\chi_v>0\),
\[
 0<\Re\{(2P_v)\overline{2t_v}\}
                  =-4\pi\chi_v\Im t_v .
 \tag{24}
\]
Here flipping just vertex \(v\) changes only that primitive component.
Thus every selected target angle has negative imaginary part.
The same holds at the small positive seed of Section 3.
The inverse-tangent strip identifies this condition with
\(\Im w_v<0\), where \(w_v=\tan(t_v/2)\).

Both configurations therefore lie in
\(\mathcal P\cap\{\Im w_v<0\text{ for every }v\in I\}\), where
\(\mathcal P\) is the actual positive tangent domain.
Contract their radial arms into a sufficiently small polydisk about
zero, stopping before zero. Its product of lower half-disks is convex,
so it connects those contracted points while keeping every imaginary
part negative. A fixed Bernstein polynomial approximation of the
resulting compact path preserves its endpoints and stays in this open
domain. A sufficiently small complex stadium \(D_*\) about \([0,1]\)
then gives a holomorphic critical curve
\[
 w(\zeta),\quad t(\zeta)=2\arctan w(\zeta),\qquad
 \chi_v(\zeta)=\frac{i}{\pi}P_v(t(\zeta)),\qquad
                h_v(\zeta)=i\,t_v(\zeta).
 \tag{25}
\]
The parameter \(\zeta=0\) is the chosen seed and \(\zeta=1\) is the
target. The curve has \(\Re h_v=-\Im t_v>0\).
Its original marked action \(S(\zeta)\), full formal coefficients,
and leading unit are holomorphic on this stadium by the positive
formal-component theorem. Its complete-only factors are retained.

With the same complex heights for all signs define at these fixed
powers
\[
 \widehat{\mathcal G}_{N,\boldsymbol\sigma}(\zeta)
   =\left[\bigotimes_{v\in I}
       \mathcal T_{\sigma_v,b_v,\chi_v(\zeta)}^{h_v(\zeta)}
     \right]F_N .
 \tag{26}
\]
It is holomorphic on \(D_*\). Its horizontal line is exactly
\(t_v=t_v(\zeta)+s\), so its center is the original critical point.
At the target its exact value is
\[
 \widehat{\mathcal G}_{N,\boldsymbol\sigma}(1)
       =\widetilde Z_N(\mathbf b,\mathbf1).
 \tag{27}
\]
This composed family is not asserted entire in charge on the whole
plane. A charge-dependent height generally adds height-current terms
to charge derivatives, so neither the simple heat equation nor the
fixed-height all-even heat-readout quotient is asserted for (26).

There is a uniform bound needed to verify its actual initializer.
On any compact height set in the right half-plane put
\(M=\sup|\Im h|/\Re h<\infty\). Then, for every \(N\ge2\) and real \(r\),
\[
 4|\cosh(Nhr/2)|^2\ge c_M e^{N\Re h\,|r|},\qquad c_M>0 .
 \tag{28}
\]
Indeed, with \(x=N\Re h\,|r|\) and \(|\theta|\le M\), the left
side is \(4\sinh^2(x/2)+4\cos^2(\theta x/2)\).
For \(x\ge1\) its first term is at least
\((1-e^{-1})^2e^x\). On \(0\le x\le1\) its ratio to \(e^x\) has
a strictly positive minimum over the compact \((x,\theta)\)-set:
a zero would require \(x=0\), where the second term is four.
This proves (28) uniformly in the level, rather than by continuity
at each fixed level.

At the seed, all \(h_v(0)=it_v^*(\boldsymbol\xi)\) have modulus
\(O_{\Gamma,\mathbf b}(\delta)\), and their real parts are positive.
Take \(\delta\) smaller so that
\(|\Re t_v^*(\boldsymbol\xi)|<(1-T)/2\).
On a sufficiently small fixed neighborhood of \(\zeta=0\), these
properties and a finite ratio \(M\) persist. The real coordinates of
a slanted vertical side are
\(\epsilon\pi-\Im h_v\,r\); those of a horizontal wing are
\(s+\Im h_v\), \(|s|\ge T\). By taking \(\delta\) smaller before
choosing the family and shrinking its seed neighborhood, arrange
\(|\Im h_v|<T/2\). For every wing and slanted vertical coordinate,
\[
             \operatorname{dist}(\Re t_v,2\pi\mathbb Z)\ge T/2 .
\]
Indeed the wings have \(T\le |s|\le\pi\), and each side is within
\(|\Im h_v|\) of \(\epsilon\pi\).
Their angular profile loss in (8) is therefore at least the fixed
number \(\gamma(1-\cos(T/2))>0\).

Estimate (28) cancels the vertical coupon's factor
\(e^{N(1-\Re\chi_v)\Re h_v|r|}\), with the remaining cost at most
\[
 C_M\exp\{N(\pi+|\Im h_v|)|\Im\chi_v|\}.
 \tag{29}
\]
The horizontal denominators are likewise uniformly controlled,
using their imaginary height \(\Re h_v\).
The polynomial continuation cost in (8), the crossing cost, and the
real shifts of the wing coordinates are \(O_{\Gamma,\mathbf b}(\delta)\)
in the exponent. The seed action differs from \(eM_\infty\) by
\(O_{\Gamma,\mathbf b}(\delta^2)\). Choosing \(\delta>0\) sufficiently
small and then shrinking the complex seed neighborhood therefore
proves the analogue of (16) for every actual slanted exterior piece.
All path measures in (23) are retained; their factors \(h_v\) are
bounded and introduce no exponential cost.

The central horizontal directions are real displacements from
\(t^*(\zeta)\). Near the seed they stay in the same full-kernel
rectangle and satisfy (18). Thus the actual Gaussian calculation
of Section 4 applies directly, with the same local coefficients
and all orders. The other sign choices retain their strict seed
gaps. This proves a genuine initializer for (26); it is not inferred
from endpoint equality or from pointwise continuity in \(N\).

These seed coefficients are computed from the same phase (9), the
actual full kernel (17), and the literal sine and trace constants
in (2). Expanding the wire Gaussians first and then the angular
Gaussian gives the same coefficients as the canonical full unsummed
stationary rule: completing the block quadratic square fixes its
inverse form and determinant, and testing on an exponential linear
source identifies every polynomial moment. This is the Gaussian
Fubini argument in Section 2 of the positive formal-component proof.
The cut and height choices introduce no additional formal terms,
because their exterior pieces have the strict exponential gap just
proved. Thus the canonical coefficients belong to this actual seed.

The positive formal-component theorem continues these coefficients
on \(D_*\), with a nonzero target coefficient.
Hence the general analytic polynomial-upper criterion
applies if the actual moving-height family satisfies
\[
 \sup_{\zeta\in K}
 \left|N^{-\beta}e^{-NS(\zeta)}
              \widehat{\mathcal G}_{N,\mathbf+}(\zeta)\right|
       \le C_KN^{B_K}\qquad(K\Subset D_*),
 \tag{30}
\]
or its complex-area \(L^2\) alternative holds.
It would give the original endpoint asymptotic using (27) and the
literal carriers (3). Estimate (30) is not proved here.
Centering a horizontal contour on the critical point does not supply
a global factorial or kernel expansion, or bound its other sectors.
No positive lift of every short filling, action-volume calibration,
volume lower bound, or finite-exception theorem is asserted.

## Complete direct sources

All five complete proof sources were read at the matching versions:

- Exact polarized operators and source conventions,
  [research_pattern_adapted_polarized_heat_initializer.md](research_pattern_adapted_polarized_heat_initializer.md),
  370 lines, SHA256
  a27c25dae7f3be3f1ef52fb369ecca822b0896a4b034450131e05b12423c2694.
- Ordinary real-kernel profile and central Hessian,
  [research_path_mixed_trace_currents.md](research_path_mixed_trace_currents.md),
  1156 lines, SHA256
  79f1838713f5cc1b174e99f178e914692a8544f1e780552739fca1d6df4376c2.
- Actual full central kernel and all-order coefficient,
  [research_bare_kernel_thin_rectangle.md](research_bare_kernel_thin_rectangle.md),
  945 lines, SHA256
  04797c52fca87548857482461a470c46f70d3cb476b5f18249920527b733d847.
- Positive critical curve and continued actual formal coefficients,
  [research_positive_source_formal_component.md](research_positive_source_formal_component.md),
  439 lines, SHA256
  08b41e17dbdcfe6df800fe257fa6bb590f2e580e11f2ff2b4e1b7541919494f4.
- Polynomial-loss analytic continuation,
  [research_polarized_polynomial_upper_criterion.md](research_polarized_polynomial_upper_criterion.md),
  289 lines, SHA256
  1a7ca165e0bc3b6e115566859e2a780079389d3004e6915ff396eb7c9ca47d9a.

Only written mathematics and text/hash inspection have been used.
No programs, numerical experiments, tests, builds or git commands
were run. The five complete matching proof sources and the entire
final proof were read by the author before freeze. Root's pre-freeze
mathematical review is complete. Independent matching final-source
peer review is separate.
