# Joint filling contours for independently long signed twists

The first Fourier term of one filled crossing is not enough for a whole filled source. Its relative error has size \(e^{-cN/n^2}\), whereas other fillings can produce a much larger change from the complete positive exponent. The proof here retains every positive integer Fourier frequency, called a charge, until after the common wire variables have been integrated. It compares their joint critical actions, so it permits independently long and arbitrarily unequal fixed signed integers.

The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) is an input stated precisely below and proved from the finite source. Its construction retains the original positive binary resolutions. The [direct crossing trace](actual_main_meridian_direct_crossing_trace.md) supplies the exact local contour, and the [component extension](actual_main_meridian_component_extension.md) supplies the grouped high-index error bound. Together these yield the [filled-volume theorem](actual_main_meridian_filled_volume.md) for the specified class. The moving filling functional here is the polynomial crossing power itself.

## 1. The exact scalar to be transformed

Let \(m\) be the number of original crossing circles and let \(n_v\) be their fixed remaining crossing powers. In the original marked filling convention,
\[
                         n_v=\epsilon_v-2p_v.
 \tag{1}
\]
The integers \(n_v\) are fixed before \(N\) tends to infinity. Their signs are arbitrary. Put \(q=e^{\pi i/N}\), \(d=N-1\), and \(\eta=(-1)^{N-1}\).

For each circle introduce an angular variable \(\tau_v\). Before applying the crossing-power traces, the retained finite wire packet has the form
\[
 B_N(\boldsymbol\tau,s)
 =\sum_{\mathbf k/N\in\mathcal W}
    \left(\prod_{\text{bare gates }g}\mu_{N,g}(\mathbf k)\right)
    \left(\prod_{v=1}^m\prod_{e\sim v}
                     e_{k_e}(-2\cos\tau_v)\right)
    \left(\prod_e\frac{\gamma_{e,N}(s)H_N(s)}{W_{k_e}(s)}\right).
 \tag{2}
\]
The sum is over the original primitive integer variables after each complete bare tensor is expanded using a fixed ordered binary resolution. All forced relations and all \(d=N-1\) offsets are retained. A circle at an ordinary original leaf is a one-factor vertex in (2); a flagged original circle is the circle operator at its incident junction. The function is a polynomial in each \(-2\cos\tau_v\), and is separately even in the angular variables. The window is fixed and finite. The exact affine labels, not their leading continuum values, occur in (2).

The prescribed six-type compiler may put a vertex in the equal-color order, with grid parameter \(\sigma_v=s\) or \(-s\), or in the opposite-color order, with constant relation \(\sigma_v=0\). Its reference and monodromy scalars are kept in the explicit outer factor defined below. They are not included in the edge factors \(\gamma_e\). We will prove estimates uniformly for formal independent \(|\sigma_v|<1\), and then restrict to these actual assignments. This is an algebraic device for taking the full normal limit at \(\sigma_v=0\); it asserts no physical independent meridian deformation.

For an even polynomial \(f(\tau)=f^\sharp(-2\cos\tau)\), let
\[
 \mathcal D_{n,\sigma,N}[f]
       =\phi_\sigma(R_\sigma^n f^\sharp),\qquad
 C_{N,n}(\sigma)=q^{n(d^2/4-\sigma^2/2)}.
 \tag{3}
\]
All full crossing scalars are included. The exact retained filled source is
\[
 \mathcal Z_N(s,\boldsymbol\sigma)
 =\left(\prod_{v=1}^m\mathcal D_{n_v,\sigma_v,N}^{(v)}\right)
                         B_N(\boldsymbol\tau,s).
 \tag{4}
\]
The functionals act in distinct variables. Their algebraic commutation here is simply the evaluation of a fixed finite tensor contraction; no crossing operators are moved through another physical tangle.

Write \(\zeta_N(s)\) for the original closing and framing scalar, and \(\rho_{v,N}(s)\) for the prescribed scalar that identifies the actual crossing power at vertex \(v\) with the reference crossing used in (3). For an equal-color vertex that reference scalar is one. At an opposite-color vertex it is the recorded monodromy scalar. Set
\[
 \widehat\zeta_N(s)=\zeta_N(s)\prod_v\rho_{v,N}(s),
 \qquad \Gamma_N(s)=\Gamma_{\mathrm{edge},N}(s)
                   =\prod_e\gamma_{e,N}(s).
 \tag{4a}
\]
The [filled-volume theorem](actual_main_meridian_filled_volume.md) lists the reference scalars by orientation type. Equation (4a) keeps their product distinct from the closing-only scalar \(\zeta_N\), the edge product \(\Gamma_N\), and the crossing scalars \(C_{N,n_v}\). Each is included once. The actual normalized knot scalar has these factors and exactly one reduced main-cut factor:
\[
 \mathcal F_N(q^s)
 =\widehat\zeta_N(s)H_N(s)\mathcal Z_N(s,\boldsymbol\sigma(s))
       +\mathcal R_N(s).
 \tag{5}
\]
The error in (5) is the already grouped high-state, off-window, and moving-bare-to-complete error. The required bound is
\[
 |\mathcal R_N(s)|
       \le \operatorname{poly}(N)e^{N(F_0-\eta_0)}
 \tag{6}
\]
after the same harmless outer elementary factors are retained, for a fixed \(\eta_0>0\). Its exponential loss is independent of the sizes of the fixed \(n_v\); its prefactors can depend on them. The [source-bound induction](actual_main_meridian_source_bounds.md) and the [component extension](actual_main_meridian_component_extension.md), Section 6, supply (6). The fixed-power crossing bound replaces the old bounded half-twist/character operator at each decorated step.

## 2. The packet hypotheses

The proof needs the following finite, analytic facts about (2).

First, on a fixed strip around the full real angular cube, including endpoint displacements of size \(O(N^{-1})\),
\[
 |B_N(\mathbf t+i\mathbf y,s)|
 \le N^A
       \exp N\{F_0-c\|\mathbf t\|^2+C\|\mathbf y\|^2\},
 \qquad |\mathbf t|_\infty\le\pi+O(N^{-1}),
 \quad |\mathbf y|_\infty\le y_0.
 \tag{7}
\]
The same bound is allowed with a uniform \(o(1)\) in the exponent; it is absorbed into any fixed loss below. This is a raw-product bound, obtained before canonical reduction. It is uniform on every fixed main disk \(|s|\le R<1\).

Second, on a fixed complex neighborhood of the origin in the angular variables, the exact finite packet has a uniform analytic expansion
\[
 B_N(\boldsymbol\tau,s)
 =N^\nu\Gamma_N(s)\,
       a(\boldsymbol\tau)e^{N\Psi(\boldsymbol\tau)}
                       \bigl(1+O_R(N^{-1})\bigr),
 \tag{8}
\]
where the relative error is holomorphic and uniformly bounded on a slightly larger neighborhood. Here \(a\) is nonzero near the origin, \(\Gamma_N(0)=1\) after retaining its recorded constant normalization, and \(\Gamma_N\) and its inverse are uniformly bounded. The functions \(\Psi\) and \(a\) are separately even. The action is real on the real neighborhood and satisfies
\[
 \Psi(0)=F_0,\qquad
 \Psi''(0)=-\operatorname{diag}(a_1,\ldots,a_m),
                  \qquad a_v>0.
 \tag{9}
\]
The repeated use of \(a\) in (8) and \(a_v\) in (9) denotes respectively the scalar amplitude and the positive angular curvatures; there is no equality between them. In the actual Newton packet,
\[
                a_v=\frac1{2\pi}
                           \sum_{e\sim v}\tan(\pi x_e^*).
 \tag{10}
\]
The mixed angular derivatives vanish because each local Newton action is even in its own angle, so its mixed wire-angle derivative is zero at completeness. Thus optimizing the wires does not change this diagonal second derivative.

The packet interface proves (8) using the original primitive lattice, the canonical \(G_N\) interpolation of the complete bare gates, and the exact interpolation of \(e_k(-2\cos\tau)\). The analytic edge insertion is
\[
 \gamma_{e,N}(s)
   \frac{G_N(Nx_e)^2}
        {G_N(Nx_e-s)G_N(Nx_e+s)}
          =\gamma_{e,N}(s)(1+O_R(N^{-1}))
 \tag{11}
\]
on a fixed complex regular wire neighborhood. Consequently it changes the amplitude, not \(\Psi\). In particular, (8) is a uniform complex statement for the exact finite window, not a conclusion inferred from a pointwise real-grid ratio.

For the grouped Conway packet, the exact primitive count gives
\(\nu=3(1-m)/2\). The argument below is valid with any fixed \(\nu\); the displayed count then recovers the original final power \(N^{3/2}\).

## 3. Exact finite-charge truncation with a fixed source loss

Fix \(R<R'<1\), with \(R'\ne1/2\). Initially put each formal \(\sigma_v\) on the circle \(|\sigma_v|=R'\). Its sine denominator is bounded away from zero. For a single variable, the actual trace is
\[
 \mathcal D_{n,\sigma,N}[f]
 =\frac{\eta N C_{N,n}(\sigma)}{\sin(2\pi\sigma)}
       \sum_{r=0}^{N-1}
       \sin\tau_r(\sigma)\,f(\tau_r(\sigma))
            e^{inN\tau_r(\sigma)^2/(4\pi)}.
 \tag{12}
\]
Use the rectangle translated by \(2\pi\sigma/N\) and its exact kernel
\[
 K_\sigma(\tau)=
       \frac{iN e^{iN\tau}}
              {e^{iN\tau}-\eta e^{2\pi i\sigma}}.
 \tag{13}
\]
Its vertical sides obey
\(K_\sigma(\pm\pi+iv+2\pi\sigma/N)
 =iN e^{-Nv}/(1+e^{-Nv})\).
The horizontal geometric expansions, their endpoint connectors, and oddness of \(\sin\tau f(\tau)e^{inN\tau^2/(4\pi)}\) give the exact contour decomposition proved in the [direct crossing trace](actual_main_meridian_direct_crossing_trace.md), Section 2. In particular, the nonzero charge coefficients are
\[
 c_{\ell,N}(\sigma)=
       \eta^{\ell-1}U_{\ell-1}(\cos2\pi\sigma),
 \qquad \ell\ge1,\qquad c_{1,N}=1.
 \tag{14}
\]
The zero Fourier integral is zero by oddness, with its endpoint currents retained. At \(\sigma=0\), (14) gives the full normal coefficient \(\eta^{\ell-1}\ell\).

Choose a small fixed \(t_0>0\), to be decreased later, and let
\[
 L_v=\lfloor t_0|n_v|\rfloor,\qquad
 y_v=\frac{A_0t_0}{|n_v|},
 \tag{15}
\]
where \(A_0>0\) is a sufficiently small constant depending only on the Gaussian constants in (7). Require \(|n_v|\) large enough that \(L_v\ge1\).
Define a finite-charge functional on the real interval:
\[
 \mathcal P_{n,\sigma,N}^{L}[f]
 =-\frac{N^2C_{N,n}(\sigma)}{\pi i}
       \sum_{\ell=1}^{L}c_{\ell,N}(\sigma)
       \int_{-\pi}^{\pi}\sin\tau\,f(\tau)
                e^{inN\tau^2/(4\pi)-i\ell N\tau}\,d\tau.
 \tag{16}
\]

Here is the uniform tail estimate. On the lower horizontal side the real exponent from (7) and the chirp is at most
\[
 F_0-ct^2+\frac{|n|\,|t|y}{2\pi}
                       -\ell y+Cy^2.
 \tag{17}
\]
The maximum of the second and third terms is
\(n^2y^2/(16\pi^2c)\). Since \(L+1>t_0|n|\), at every \(\ell\ge L+1\) the exponent in (17) is at most
\[
 F_0+
  t_0^2\left(\frac{A_0^2}{16\pi^2c}-A_0
                              +\frac{CA_0^2}{n^2}\right)
            -(\ell-L-1)y.
 \tag{18}
\]
Choose \(A_0\) so the first positive term is at most \(A_0/4\), and then the fixed lower threshold for \(|n|\) so the last positive term is also at most \(A_0/4\). The loss is at least
\(A_0t_0^2/2\), independently of \(n\). The coefficients satisfy
\[
 |c_{\ell,N}(\sigma)|\le
             \ell e^{2\pi R'(\ell-1)}.
 \tag{19}
\]
The remaining sum converges geometrically because
\(Ny>2\pi R'\) for sufficiently large \(N\). Constants such as
\(e^{2\pi R'L}\) depend on the fixed \(n\), not on \(N\), and do not alter this exponential loss.

The original translated vertical sides and all connectors have a fixed angular loss from (7). Their chirp cost is at most \(N|n|(\pi+o(1))y/(2\pi)=O(Nt_0)\). For the finitely many retained charges, moving their horizontal paths to the real interval costs at most \(NLy=O(Nt_0^2)\). Taking \(t_0\) sufficiently small preserves a fixed positive endpoint loss. The zero-mode endpoint current has the same bound. The exact vertical kernel is \(O(N)\), so it adds only a polynomial factor.

These estimates prove a one-coordinate remainder of rate
\(F_0-\gamma\), for some fixed \(\gamma>0\), whenever all spectator variables remain on real intervals or on their physical translated grids. On such grids their imaginary parts are \(O(N^{-1})\). Their fixed-power chirps have bounded modulus, with constants depending on their fixed integers. Thus they introduce no positive exponential term involving another \(n_w\).

Apply the exact telescoping identity
\[
 \prod_{v=1}^m\mathcal D_v-\prod_{v=1}^m\mathcal P_v
 =\sum_{j=1}^m
       \left(\prod_{v<j}\mathcal P_v\right)
       (\mathcal D_j-\mathcal P_j)
       \left(\prod_{v>j}\mathcal D_v\right).
 \tag{20}
\]
Each \(\mathcal P_v\) in a spectator coordinate is a finite real integral whose absolute operator cost is polynomial in \(N\), with constants depending on the fixed \(n_v\). Each \(\mathcal D_v\) is its physical finite grid sum. Therefore the preceding one-coordinate estimate applies to every term of (20). No spectator contour is put at a slope-dependent complex height during a different coordinate's tail estimate.

The resulting identity is
\[
 \mathcal Z_N(s,\boldsymbol\sigma)
 =\left(\prod_{v=1}^m
       -\frac{N^2C_{N,n_v}(\sigma_v)}{\pi i}\right)
     \sum_{1\le\ell_v\le L_v}
       \left(\prod_v c_{\ell_v,N}(\sigma_v)\right)
       I_{\boldsymbol\ell,N}(s)
       +O\!\left(N^A e^{N(F_0-\gamma)}\right),
 \tag{21}
\]
where
\[
 I_{\boldsymbol\ell,N}(s)
 =\int_{[-\pi,\pi]^m}
       B_N(\boldsymbol\tau,s)
       \left(\prod_v\sin\tau_v\right)
       \exp N\left\{
          \frac{i}{4\pi}\sum_v n_v\tau_v^2
                           -i\sum_v\ell_v\tau_v\right\}
                                      d\boldsymbol\tau.
 \tag{22}
\]

Finally consider the *whole* difference in (21). It is holomorphic in every formal \(\sigma_v\) throughout \(|\sigma_v|<1\): the original crossing-power traces have their removable collisions, and the finite approximation has the polynomial coefficients (14). Apply the maximum principle successively from the parameter circles. This extends (21) to all \(|\sigma_v|\le R\), including opposite-color vertices \(\sigma_v=0\). It is not an assertion that each separately divided current is removable. We may now restrict to the actual \(\sigma_v=0,\pm s\).

The fixed loss \(\gamma\) in (21) is the key to the independent-slope quantifier. It does not decrease like \(1/\max|n_v|^2\).

## 4. The joint critical branch and every nonminimal charge

The real angular Gaussian (7) permits truncating (22) to a small fixed angular box, with a fixed source loss, because all chirps and Fourier factors have modulus one on the real integration domain. On this box use the exact analytic packet expansion (8).

For real nonzero \(n_v\), put
\[
 \varepsilon_v=\frac1{n_v},\qquad
 t_v=\frac{\ell_v}{n_v},
 \qquad
 \mathcal T_{\boldsymbol\ell}(\boldsymbol\tau)
 =\Psi(\boldsymbol\tau)
       +\frac{i}{4\pi}\sum_v n_v\tau_v^2
                              -i\sum_v\ell_v\tau_v.
 \tag{23}
\]
The critical equation is
\[
 \tau_v=2\pi t_v+2\pi i\varepsilon_v
                              \Psi_v(\boldsymbol\tau).
 \tag{24}
\]
The analytic implicit function theorem at
\((\mathbf t,\boldsymbol\varepsilon)=(0,0)\)
gives a unique branch on one fixed polydisk. Choose \(t_0\) in (15) within this polydisk and take every \(|n_v|\) above one fixed threshold. This covers all retained charges, regardless of the ratios \(|n_v/n_w|\).

Complete the square and define the analytic stationary remainder
\[
 \mathcal W(\mathbf t,\boldsymbol\varepsilon)
 =\operatorname{stat}_{\boldsymbol\tau}
    \left[\Psi(\boldsymbol\tau)
       +\frac{i}{4\pi}\sum_v n_v(\tau_v-2\pi t_v)^2\right].
 \tag{25}
\]
The apparent singularity at \(\varepsilon_v=0\) is removable after substitution of (24), because
\(\tau_v-2\pi t_v=O(\varepsilon_v)\). Explicitly, its value on the critical branch is
\(\Psi(\boldsymbol\tau)-i\pi\sum_v\varepsilon_v\Psi_v(\boldsymbol\tau)^2\), which is holomorphic even when some reciprocal slopes vanish.
The critical action is exactly
\[
 \mathcal T_{\boldsymbol\ell}(\boldsymbol\tau_{\boldsymbol\ell})
   =-i\pi\sum_v\frac{t_v^2}{\varepsilon_v}
                 +\mathcal W(\mathbf t,\boldsymbol\varepsilon).
 \tag{26}
\]
The first term is purely imaginary for the real signed data under consideration.

Separate evenness of \(\Psi\) makes \(\mathcal W\) separately even in every \(t_v\). At \(\boldsymbol\varepsilon=0\),
\(\mathcal W(\mathbf t,0)=\Psi(2\pi\mathbf t)\), so (9) gives
\[
 \frac{\partial}{\partial(t_v^2)}
          \operatorname{Re}\mathcal W(0,0)
                         =-2\pi^2a_v.
 \tag{27}
\]
Shrink the same fixed polydisk so every derivative in (27) is at most
\(-\pi^2a_v\). Integrating in the squared coordinates, at the fixed signed vector \(\boldsymbol\varepsilon\), proves
\[
 \boxed{\displaystyle
 \operatorname{Re}\mathcal T_{\boldsymbol\ell}
       (\boldsymbol\tau_{\boldsymbol\ell})
 \le
 \operatorname{Re}\mathcal T_{\mathbf1}
       (\boldsymbol\tau_{\mathbf1})
       -\sum_v\frac{\pi^2a_v}{n_v^2}(\ell_v^2-1).}
 \tag{28}
\]
This is a joint action comparison. All other fillings retain their damping while one charge is increased. There is no comparison between a smallest local alias gap and the total complete-to-filled volume drop.

The critical amplitude is nonzero. Indeed separate evenness writes
\(\Psi_v(\boldsymbol\tau)=\tau_v Q_v(\tau_1^2,\ldots,\tau_m^2)\), and (24) yields
\[
 \tau_{\boldsymbol\ell,v}
 =\frac{2\pi t_v}
       {1-2\pi i\varepsilon_v Q_v(\boldsymbol\tau_{\boldsymbol\ell}^2)}.
 \tag{29}
\]
Every \(t_v\ne0\), so every \(\tau_{\boldsymbol\ell,v}\ne0\). By shrinking the fixed neighborhood, these values have modulus less than \(\pi/2\), so every \(\sin\tau_{\boldsymbol\ell,v}\ne0\). Moreover, \(\operatorname{Re}Q_v<0\) there. For real signed data (29) also gives
\[
 \operatorname{Im}\tau_{\boldsymbol\ell,v}
 =\frac{4\pi^2\ell_v\operatorname{Re}Q_v}
       {n_v^2|1-2\pi i\varepsilon_vQ_v|^2}<0.
 \tag{30}
\]
This records the contour direction without assuming that all \(n_v\) have the same sign.

## 5. Complex saddle, endpoint currents, and the first coefficient

Translate the small real angular box to the nearby critical point of each retained charge. On a real tangent vector the chirp Hessian is purely imaginary; the real part of the total Hessian is therefore that of \(\Psi''\), which remains strictly negative on the fixed local neighborhood. The Gaussian determinant is nonzero.

The endpoint connectors retain a fixed action gap. To see the slope dependence explicitly, (29) gives
\[
 |\operatorname{Im}\tau_{\boldsymbol\ell,v}|
                 \le C|t_v|/|n_v|.
 \tag{31}
\]
On a face with real coordinate of size \(\rho>0\), its chirp growth is at most \(CN\rho|t_v|\). The Fourier factor is decreasing in each downward displacement by (30). Choose \(t_0\) sufficiently small compared with the fixed face loss \(c\rho^2\), and then choose the reciprocal-slope threshold. The connectors remain strictly below all the local critical actions. This order of choices uses one fixed source box and requires no relation between different \(n_v\).

Apply (8) on this translated contour, rather than integrating a merely pointwise real-grid \(O(N^{-1})\) error. Its uniform holomorphic error and the local Gaussian bound give
\[
 I_{\boldsymbol\ell,N}(s)
 =N^{\nu-m/2}\Gamma_N(s)(2\pi)^{m/2}
   \frac{a(\boldsymbol\tau_{\boldsymbol\ell})
                 \prod_v\sin\tau_{\boldsymbol\ell,v}}
        {\sqrt{\det[-\mathcal T_{\boldsymbol\ell}''
                    (\boldsymbol\tau_{\boldsymbol\ell})]}}
   e^{N\mathcal T_{\boldsymbol\ell}
                     (\boldsymbol\tau_{\boldsymbol\ell})}
                          (1+O_{\mathbf n,R}(N^{-1})).
 \tag{32}
\]
The square root is fixed by the original translated real contour. All retained factors are nonzero on the chosen branch. The local asymptotic can also be stated as an upper bound for nonminimal charges; this is enough for their sum.

For fixed \(\mathbf n\), the number of retained charges in (21) is finite. Their coefficients (14) are uniformly bounded on the parameter disk by constants depending on \(\mathbf n\) and \(R\), not on \(N\). Inequality (28) then makes every charge except \(\mathbf1\) exponentially smaller. Its coefficient is exactly
\[
                       \prod_vc_{1,N}(\sigma_v)=1.
 \tag{33}
\]
The reflected signs have already been paired in the exact contour derivation. Thus there are no remaining equal-action terms with an unexamined relative sign. In particular (33) applies simultaneously to constant opposite-color vertices and moving equal-color vertices.

Finally, the critical action at \(\mathbf1\) tends uniformly to \(F_0\) as
\(\max_v|1/n_v|\to0\). Increase the single lower threshold for all \(|n_v|\) so that its real part lies above \(F_0\) minus half every fixed error loss in (6), (21), and the real angular truncation. This absorbs those errors. It is only these *fixed* losses that are compared with the total volume drop.

Combining the exact prefactors in (21) with (32) gives
\[
 \mathcal Z_N(s,\boldsymbol\sigma)
 =\left(\prod_v C_{N,n_v}(\sigma_v)\right)
       \Gamma_N(s)N^{\nu+3m/2}
       D_{\mathbf n}
       e^{N\mathcal T_{\mathbf1}
                          (\boldsymbol\tau_{\mathbf1})}
                         (1+O_{\mathbf n,R}(N^{-1})),
 \tag{34}
\]
where
\[
 D_{\mathbf n}
 =\left(-\frac1{\pi i}\right)^m(2\pi)^{m/2}
    \frac{a(\boldsymbol\tau_{\mathbf1})
                      \prod_v\sin\tau_{\mathbf1,v}}
       {\sqrt{\det[-\mathcal T_{\mathbf1}''
                            (\boldsymbol\tau_{\mathbf1})]}}
                         \ne0.
 \tag{35}
\]
For the actual grouped count \(\nu=3(1-m)/2\), the power in (34) is \(N^{3/2}\). Any already recorded outer normalization in (5) remains outside this count.

## 6. The main-meridian profile and the marked volume

Restrict the formal grid parameters to their actual types
\(\sigma_v(s)\in\{0,s,-s\}\), with the prescribed reference factors in \(\widehat\zeta_N\) as defined by (4a), and with \(\Gamma_N=\Gamma_{\mathrm{edge},N}\). Dividing (34) by its complete-main value gives
\[
 \frac{\mathcal Z_N(s,\boldsymbol\sigma(s))}
      {\mathcal Z_N(0,\mathbf0)}
 =\Gamma_N(s)
       \prod_v q^{-n_v\sigma_v(s)^2/2}
                         (1+O_{\mathbf n,R}(N^{-1})).
 \tag{36}
\]
With the original reduced main cut and framing,
\[
 \boxed{\displaystyle
 \frac{\mathcal F_N(q^s)}{\mathcal F_N(1)}
 =\frac{\widehat\zeta_N(s)}{\widehat\zeta_N(0)}
      H_N(s)\Gamma_N(s)
      \prod_v q^{-n_v\sigma_v(s)^2/2}
                         (1+O_{\mathbf n,R}(N^{-1})).}
 \tag{37}
\]
The phase products are retained exactly. In particular, the ratio of the combined outer factors in (37) is the product of the closing/framing ratio and the explicit reference-scalar ratios from (4a). No convergence of the framing ratio to one is assumed. The recorded subexponential upper and lower bounds for these factors suffice for the logarithmic conclusion. Uniform holomorphy on larger compact disks gives all fixed derivatives of the normalized ratio on smaller disks.

The limiting action in (34) is the old marked filling action. At the level of the joint wire variables, the complete auxiliary-color packet has local circle action
\[
 \operatorname{stat}_{\tau_v}
       \left[b_v(\mathbf x,\tau_v)
          +\frac{i\epsilon_v\tau_v^2}{4\pi}
          +it_v\tau_v\right].
 \tag{38}
\]
Its auxiliary Fourier transform adds \(2\pi i t_vz_v\) and therefore sets \(\tau_v=-2\pi z_v\). Evenness gives
\(b_v(\mathbf x,2\pi z_v)+i\pi\epsilon_vz_v^2\).
Subtracting the original filling phase
\(2\pi i(p_vz_v^2+z_v)\), and using (1), gives exactly
\[
 b_v(\mathbf x,\tau_v)
          +\frac{in_v\tau_v^2}{4\pi}-i\tau_v,
                    \qquad \tau_v=2\pi z_v.
 \tag{39}
\]
The unchanged bare-gate actions and common wire stationarity can be included before either elimination. Thus (23) at charge \(\mathbf1\) is the previously selected original primitive filling branch, not an action inferred merely from its quadratic term.

The [marked geometric filling theorem](actual_conway_general_mask_marked_filling.md) identifies
\[
 2\pi\operatorname{Re}\mathcal T_{\mathbf1}
                  (\boldsymbol\tau_{\mathbf1})
                   =\operatorname{Vol}(S^3\setminus K_{\mathbf n}).
 \tag{40}
\]
Only the auxiliary circles are filled; the knot cusp remains unfilled. This geometric input applies to the fixed strict original template and its actual knot pattern, for all independently sufficiently long fixed signed fillings. No comparison between augmented and filled complements is inferred from a source identity.

Since \(H_N(s)\) and its inverse are uniformly bounded on every compact disk \(R<1\), the nonzero asymptotic (34), the actual normalization (5), the explicit framing bounds, and the geometric identity (40) imply
\[
 \frac{2\pi}{N}\log|\mathcal F_N(q^s)|
       \longrightarrow \operatorname{Vol}(S^3\setminus K_{\mathbf n})
 \tag{41}
\]
uniformly on such a disk, once the packet and global-error hypotheses of Sections 1--2 have been established for the source. The fixed main normalization, including the single factor corresponding to the reduced primitive cut, is the same as at \(s=0\).

## 7. Scope of the transfer

The analytical conclusion is conditional only on the explicit finite packet and grouped global-error statements, not on a conjectural moving full-twist coefficient expansion. The local operator \(R_s^{n_v}\), translated grid contours, all endpoint currents, and the first charge coefficient are exact.

The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) supplies these interfaces for the strict separated-bare-junction class and for its [component-path enlargement](actual_main_meridian_component_extension.md). It constructs the exact primitive lattice and its positive resolutions, proves (2), (7), and (8) with the count \(\nu=3(1-m)/2\), and proves the fixed grouped error (6). Thus the application uses a specified finite source and its finite contour representation.

Concretely, every maximal bare component may be a singleton of arbitrary valence, or a component \(\mathcal U\) with at least five rigid boundary incidences \(b_v\) at each vertex and
\[
 \max_{\mathcal P\text{ a simple path in }\mathcal U}
       \sum_{v\in\mathcal P}\varepsilon_{b_v-1}<2G_0,
 \qquad
 \varepsilon_k=(k+1)
 \left[
 J\left(\frac14+\frac1{k+1}\right)
 +J\left(\frac14-\frac1{k+1}\right)
 -2J\left(\frac14\right)\right].
 \tag{42}
\]
Here \(J(x)=\int_0^x\log(2\sin\pi u)\,du\) and \(G_0=g(1/4)\), with \(g(x)=J(2x)-4J(x)\). The coarse condition \(b_v\ge\max(8,4|\mathcal U|)\) suffices. For a fixed strict original template in this class, and its fixed knot/parity pattern, (37) and (41) therefore hold for every independently sufficiently long fixed signed filling. The original marked geometric calibration identifies the volume; the nonzero quantum lower is supplied directly by (34), not imported from an old filled-invariant asymptotic.

The lower bound on \(|n_v|\) is a single source-dependent constant. It can be maximized over the finitely many retained parity/sign conventions if the desired theorem quantifies over them. It is independent of the chosen fixed radius \(R<1\): the action, the wire and angular windows, the Gaussian constants in the exponent, and the structural high-state/bare-error margins come from the complete source. The radius enters only polynomial or bounded prefactors, the convergence of the geometric kernel tails for large \(N\), and the uniform remainder constants. Accordingly the threshold for \(N\), but not the threshold for the filling integers, may depend on \(\mathbf n\) and \(R\). There is no same-sign assumption, no bound on ratios of different \(|n_v|\), no prime-level restriction, and no limit in which the filling integers grow with \(N\).

The distinction between the two uses of an exponential gap is essential. Fixed global window and contour-tail losses can be compared with the total complete-to-filled volume drop after all fillings are sufficiently long. The charge-dependent losses in (28) are instead compared with the *same joint filled critical action*. Replacing this second comparison by a smallest local gap against the total drop would not establish the stated independent-slope result.
